import multiprocessing
import time
from typing import List


def cpu_bound_workload(number: int) -> int:
    return sum(i * i for i in range(number))


def compute_sums(numbers: List[int]) -> List[int]:
    with multiprocessing.Pool() as pool:
        # This will call the function in parallel once for each element in the list.
        # This is similar to a parallel-for loop found in other programming languages.
        return pool.map(cpu_bound_workload, numbers)


if __name__ == "__main__":
    print(f"Number of CPU cores: {multiprocessing.cpu_count()}")

    numbers: List[int] = [5_000_001 + x for x in range(20)]
    print(f"Input list of integers: : {numbers}")

    start_time = time.time()

    sums: List[int] = compute_sums(numbers)
    duration = time.time() - start_time

    print(f"Output list of integers: : {sums}")

    print(f"Duration {duration} seconds")
