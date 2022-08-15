import binascii

binascii.unhexlify(b"507974686f6e204c696272617279")
bytes.fromhex("507974686f6e204c696272617279")

binascii.hexlify(b"Python Library")
b"Python Library".hex()

binascii.hexlify("파이썬 라이브러리".encode("utf-8"))
binascii.unhexlify(b"ed8c8ce9db4ec8dac20eb9dbcec9db4ebb88ceb9faceba6ac").decode("utf-8")
