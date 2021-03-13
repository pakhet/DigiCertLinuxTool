from OpenSSL import crypto
import os
import sys
import datetime
import whois

#Variables
TYPE_RSA = crypto.TYPE_RSA
cn = input("Common Name: ")
key = crypto.PKey()
req = crypto.X509Req()
dir_path = os.path.dirname(os.path.realpath(__file__))
keypath = dir_path + "/" + cn.replace(".", "_") + ".key"
csrpath = dir_path + "/" + cn.replace(".", "_") + ".csr"

#create private key
def generatekey():
    #set key size
    print("Generating private key.")
    keysize = input("Key size[2048]: ")
    if not keysize:
        keysize = 2048
    keysize = int(keysize)
    key.generate_key(TYPE_RSA, keysize)
    keyfile = open(keypath, "wb")
    keyfile.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))
    keyfile.close()

generatekey()

#create CSR
def generatecsr():
