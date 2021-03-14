from OpenSSL import crypto

req = crypto.X509Req()


def generatecsr(key, csrpath, cn, c, st, l, o):
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
    return c, st, l, o
