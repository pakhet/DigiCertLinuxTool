from OpenSSL import crypto
req = crypto.X509Req()


def generatecsr(key, csrpath, cn):
    c = input("Enter your country: ")
    st = input("Enter your state: ")
    l = input("Enter your locality: ")
    o = input("Enter your organization: ")

    req.get_subject().CN = cn
    req.get_subject().C = c
    req.get_subject().ST = st
    req.get_subject().L = l
    req.get_subject().O = o
    req.set_pubkey(key)
    req.sign(key, "sha256")
    csrfile = open(csrpath, "wb")
    csrfile.write(crypto.dump_certificate_request(crypto.FILETYPE_PEM, req))
    csrfile.close()
    print("CSR created!")
