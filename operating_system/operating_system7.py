import ctypes

mylib = ctypes.cdll.LoadLibrary("./mylib.so")
print(mylib.add(3, 4))
