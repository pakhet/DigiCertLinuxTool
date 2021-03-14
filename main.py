from OpenSSL import crypto
import os
from createkey import *
from generatecsr import *
from ordercert import *

# Variables
cn = input("Common Name: ")
key = crypto.PKey()
dir_path = os.path.dirname(os.path.realpath(__file__))
keypath = dir_path + "/" + cn.replace(".", "_") + ".key"
csrpath = dir_path + "/" + cn.replace(".", "_") + ".csr"
c = input("Enter your country: ")
st = input("Enter your state: ")
l = input("Enter your locality: ")
o = input("Enter your organization: ")

# create private key

generatekey(key, keypath)

# create CSR

generatecsr(key, csrpath, cn, c, st, l, o)

# order cert
ordercert(cn, c, st, l, o, csrpath)
