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
    print(result)



if __name__ == '__main__':
    a = (128, 255, 99999, 10651060)
    print(f"Count CPU: {cpu_count()}")
    st_time = time()
    with Pool(cpu_count()) as pool:
        pool.apply_async(factorize_process(128), callback=callback)
        pool.apply_async(factorize_process(255), callback=callback)
        pool.apply_async(factorize_process(99999), callback=callback)
        pool.apply_async(factorize_process(10651060), callback=callback)
        pool.close()  # перестати виділяти процеси в пулл
        # p.terminate()  # убити всіх
        pool.join()  # дочекатися закінчення всіх процесів

    print(f"End {current_process().name}")

    end_time = time()
    delta_time = end_time - st_time
    print(f"Test with class Process - {delta_time}")
 