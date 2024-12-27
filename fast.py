import ctypes
import cProfile
# import time

# Rust kutubxonasini yuklash
rust_lib = ctypes.CDLL("./rust_test/target/release/librust_test.dylib")

# Rust funksiyasini aniqlash
rust_lib.fast_function.restype = ctypes.c_uint64

def main():
    print("Natija:", rust_lib.fast_function())

if __name__ == "__main__":
    # start = time.time()
    # main()
    # end = time.time()
    # print((end - start) * 1000, "ms")
    cProfile.run("main()")
