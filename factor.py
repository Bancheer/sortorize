import time
from multiprocessing import Pool, cpu_count

def factorize_number(number):
    factors = [i for i in range(1, number + 1) if number % i == 0]
    return factors

def factorize(*numbers):
    return [factorize_number(number) for number in numbers]

def parallel_factorize_number(number):
    with Pool(cpu_count()) as pool:
        factors = pool.map(factorize_number, range(1, number + 1))
    return factors

def parallel_factorize(*numbers):
    with Pool(cpu_count()) as pool:
        return pool.map(parallel_factorize_number, numbers)


a, b, c, d = factorize(128, 255, 99999, 10651060)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]


start_time_sync = time.time()
factorize(128, 255, 99999, 10651060)
end_time_sync = time.time()
print(f"Synchronous Execution Time: {end_time_sync - start_time_sync} seconds")


start_time_parallel = time.time()
parallel_factorize(128, 255, 99999, 10651060)
end_time_parallel = time.time()
print(f"Parallel Execution Time: {end_time_parallel - start_time_parallel} seconds")