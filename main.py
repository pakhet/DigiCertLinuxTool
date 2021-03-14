from OpenSSL import crypto
import os
from createkey import generatekey
from generatecsr import generatecsr

# Variables
cn = input("Common Name: ")
key = crypto.PKey()
dir_path = os.path.dirname(os.path.realpath(__file__))
keypath = dir_path + "/" + cn.replace(".", "_") + ".key"
csrpath = dir_path + "/" + cn.replace(".", "_") + ".csr"

# create private key

generatekey(key, keypath)

# create CSR

generatecsr(key, csrpath, cn)
