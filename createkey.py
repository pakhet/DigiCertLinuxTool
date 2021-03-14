from OpenSSL import crypto
TYPE_RSA = crypto.TYPE_RSA

def generatekey(key, keypath):
    # set key size
    print("Generating private key.")
    keysize = input("Key size[2048]: ")
    if not keysize:
        keysize = 2048
    keysize = int(keysize)
    key.generate_key(TYPE_RSA, keysize)
    keyfile = open(keypath, "wb")
    keyfile.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))
    keyfile.close()
    print("Private key created!")
