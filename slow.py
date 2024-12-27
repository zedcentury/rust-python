import cProfile
import math

def slow_function():
    total = 0
    for i in range(1, 10_000_000):
        total += math.sqrt(i)
    return total

def main():
    print("Natija:", slow_function())

if __name__ == "__main__":
    cProfile.run("main()")
