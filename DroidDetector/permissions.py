__author__ = 'm4cr010'

#!/usr/bin/python
# List of all known system permissions

# This is from MIT code
NORMAL = 0
DANG = 1
SIG = 2
SIGSYS = 3

text2perm = {
    "0": NORMAL,
    "normal": NORMAL,
    "1": DANG,
    "dangerous": DANG,
    "signature": SIG,
    "2": SIG,
    "signatureOrSystem":SIGSYS,
    "3":SIGSYS,
    "signature|system":SIGSYS}