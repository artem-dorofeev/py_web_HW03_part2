from multiprocessing import Pool, current_process, cpu_count
from time import time


class Number():
    def __init__(self, number: int) -> None:
        self.number = number

    def dividing_of_numbers(self):
        result = [n for n in range(1, int(self.number / 2) + 1) if self.number % n == 0]
        result.append(self.number)
        return result


def factorize_process(num):
    factorize_proc = Number(num)
    result = factorize_proc.dividing_of_numbers()
    return result


def callback(result):
    print(f"Result in callback: {result}")


if __name__ == "__main__":
    print(f"Count CPU: {cpu_count()}")
    st_time = time()
    a = (128, 255, 99999, 10651060)
    with Pool(cpu_count()) as p:
        p.map_async(
            factorize_process,
            a,
            callback=callback,
        )
        p.close()  # перестати виділяти процеси в пулл
        p.join()  # дочекатися закінчення всіх процесів

    print(f'End {current_process().name}')
    end_time = time()
    delta_time = end_time - st_time
    print(f"Test with map - {delta_time}")