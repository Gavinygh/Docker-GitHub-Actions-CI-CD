import hashlib
import time


def hash(i):
    f = open("tokyo.jpg", "rb").read()
    for _ in range(i):
        hashlib.sha256(f).hexdigest()

if __name__ == "__main__":
    st = time.time()
    hash(1000)
    et = time.time()
    print(et-st)
