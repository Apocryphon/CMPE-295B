####################################################
# Author: Sascha Fahl <fahl@dcsec.uni-hannover.de> #
####################################################

from androguard.core.bytecodes import apk, dvm
from androguard.core.analysis import analysis
from androguard.decompiler.dad import decompile
import sys

def onreceivedsslerror(vm, vmx, java=None, smali=None):
	for method in vm.get_methods():
		if method.get_code() == None:
			continue

		if method.get_name() == "onReceivedSslError" and not "abstract" in method.get_access_flags_string() and not "Landroid/webkit/WebViewClient;" == method.get_class_name():
			print "\n\n########## Found customized onReceivedSslError method: "
			print "{:s}{:s}{:s};[access_flags={:s}]".format(method.get_class_name(),method.get_name(),method.get_descriptor(),method.get_access_flags_string())

			count_locals = method.get_locals() 
			count_instructions = count_instr_in_method(method)
			print "########## Information: "
			print "{:d} local variables.".format(count_locals)
			print "{:d} instructions.".format(count_instructions)


			if smali:
				print_pretty4method(method)

			if java:
				print_java4method(method, vmx)

def trustmanager(vm, vmx, java=None, smali=None):
	for method in vm.get_methods():
		if method.get_code() == None:
			continue
		
		if method.get_name() == "checkServerTrusted" and not "abstract" in method.get_access_flags_string():
			print "\n\n########## Found customized checkServerTrusted method: "
			print "{:s}{:s}{:s};[access_flags={:s}]".format(method.get_class_name(),method.get_name(),method.get_descriptor(),method.get_access_flags_string())
			
			count_locals = method.get_locals() 
			count_instructions = count_instr_in_method(method)
			print "########## Information: "
			print "{:d} local variables.".format(count_locals)
			print "{:d} instructions.".format(count_instructions)
			
			info = method.get_information()
			local_vars = info['registers']
			params = info['params']
			certs_p = None
			for param in params:
				if param[1] == "java.security.cert.X509Certificate[]":
					certs_p = param[0]
					print "java.security.cert.X509Certificate[] param is register number {:d}".format(certs_p)

			print "########## Check if there are instructions which have the certs param as operand: "
			hits = check_if_certs_are_operands(method, certs_p)
			if hits > 0:
				print ''.join(["########## ", str(hits), " instructions have certs param as operand."])
			else:
				print "########## Found no instructions that have certs param as operand."

			if smali:
				print_pretty4method(method)
			if java:
				print_java4method(method, vmx)

def hostnameverifiers(vm, vmx, java=None, smali=None):
	for method in vm.get_methods():
		if method.get_code() == None:
			continue

		code = method.get_code()
		bc = code.get_bc()
		
		for i in bc.get_instructions():
			op = ' '.join([i.get_name(), i.get_output()]).lower()
			if "sethostnameverifier" in op:
				print "\n\n########## Found method which sets a hostname verifier: "
				print "{:s}{:s}{:s};[access_flags={:s}]".format(method.get_class_name(),method.get_name(),method.get_descriptor(),method.get_access_flags_string())
				
				if java:
					print_java4method(method, vmx)


			

def print_pretty4method(method):
	method.pretty_show()
	print ""

def print_java4method(method, vmx):
	mx = vmx.get_method(method)
	ms = decompile.DvMethod(mx)
	ms.process()
	print "########## De-compiled JavaCode of Method: "
	print ms.get_source()
	print ""

def check_if_certs_are_operands(mx, certs_p):
	code = mx.get_code()
	bc = code.get_bc()
	instr_count = 0
	idx = 0
	cert_op =  ''.join(["v", str(certs_p)])
	hits = 0
	for i in bc.get_instructions() :
		op = ' '.join([i.get_name(), i.get_output()])
		if cert_op in op:
			print "\t",idx,op
			hits += 1
		idx += i.get_length()
	
	return hits
		
def count_instr_in_method(mx):
	code = mx.get_code()
	bc = code.get_bc()
	instr_count = 0
	for i in bc.get_instructions() :
		instr_count += 1
	
	return instr_count

def parseargs():
	import argparse
	import sys
	parser = argparse.ArgumentParser(description="Analyse Android Apps for broken SSL certificate validation.")
	parser.add_argument("-f", "--file", help="APK File to check", type=str, required=True)
	parser.add_argument("-j", "--java", help="Show Java code for results", action="store_true", required=False)
	parser.add_argument("-s", "--smali", help="Show Smali code for results", action="store_true", required=False)
	args = parser.parse_args()

	return args



def main():

	args = parseargs()

	apk_file = args.file

	a = apk.APK(apk_file)
	print "Analyse file: {:s}".format(apk_file)
	print "Package name: {:s}".format(a.get_package())
	
	d = dvm.DalvikVMFormat(a.get_dex())
	vmx = analysis.VMAnalysis(d)
	if 'INTERNET' in vmx.get_permissions([]):
		print "App requires INTERNET permission. Continue analysis..."
		trustmanager(d, vmx, java=args.java, smali=args.smali)
		onreceivedsslerror(d, vmx, java=args.java, smali=args.smali)
		hostnameverifiers(d, vmx, java=args.java, smali=args.smali)
	else:
		print "App does not require INTERNET permission. No need to worry about SSL misuse... Abort!"
	
if __name__ == "__main__":
	main()