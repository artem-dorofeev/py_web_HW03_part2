from multiprocessing import Process, Pool, current_process, cpu_count
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



if __name__ == '__main__':
    process = []
    # a = (99999, 2555555, 999999, 100651060)
    a = (128, 255, 99999, 10651060)
    st_time = time()
    for i in a:
        pr = Process(target=factorize_process, args=(i, ))
        pr.start()
        process.append(pr)
        # print(pr)


    [pr.join() for pr in process]
    end_time = time()
    delta_time = end_time - st_time
    print(f"Test with class Process - {delta_time}")
 