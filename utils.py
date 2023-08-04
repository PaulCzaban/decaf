
def readcstr(f):
    buf = bytearray()
    while True:
        b = f.read(1)
        if b is None or b == b'\x00' or not b:
            return str(buf.decode("utf-8"))
        else:
            buf.append(b[0])
