import multiprocessing
import time
from typing import List


def cpu_bound(number: int) -> int:
    return sum(i * i for i in range(number))


def find_sums(numbers: List[int]) -> List[int]:
    with multiprocessing.Pool() as pool:
        return pool.map(cpu_bound, numbers)


if __name__ == "__main__":

    numbers: List[int] = [5_000_001 + x for x in range(20)]
    print(f"Input list of integers: : {numbers}")

    start_time = time.time()

    sums: List[int] = find_sums(numbers)
    duration = time.time() - start_time

    print(f"Output list of integers: : {sums}")

    print(f"Duration {duration} seconds")
