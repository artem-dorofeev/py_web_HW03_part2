from random import randint
from multiprocessing import Pool, current_process, cpu_count
from time import sleep, ctime, time



# def worker():
#     name = current_process().name
#     print(f"Start process {name}: {ctime()}")
#     r = randint(1, 3)  # Імітуємо якусь роботу
#     sleep(r)
#     print(f"End work process {name}: {ctime()}")
#     return f"Process{name} time run: {r} sec."


def callback(result):
    print(result)


# if __name__ == "__main__":
#     print(f"Count CPU: {cpu_count()}")
#     with Pool(cpu_count()) as pool:
#         pool.apply_async(worker, callback=callback)
#         print(f"pool in st 22")
#         pool.apply_async(worker, callback=callback)
#         print(f"pool in st 24")
#         pool.close()  # перестати виділяти процеси в пулл
#         # p.terminate()  # убити всіх
#         pool.join()  # дочекатися закінчення всіх процесів

#     print(f"End {current_process().name}")



# from multiprocessing import Process, Pool, current_process, cpu_count
# from time import time
# # import sys


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
    a = (128, 255, 99999, 10651060)
    print(f"Count CPU: {cpu_count()}")
    st_time = time()
    with Pool(cpu_count()) as pool:
        pool.apply_async(factorize_process(128), callback=callback)
        print(f"pool 1")
        pool.apply_async(factorize_process(255), callback=callback)
        print(f"pool 2")
        pool.apply_async(factorize_process(99999), callback=callback)
        print(f"pool 3")
        pool.apply_async(factorize_process(10651060), callback=callback)
        print(f"pool 4")
        pool.close()  # перестати виділяти процеси в пулл
        # p.terminate()  # убити всіх
        pool.join()  # дочекатися закінчення всіх процесів

    print(f"End {current_process().name}")


    # process = []
    # # a = (99999, 2555555, 999999, 100651060)
    # a = (128, 255, 99999, 10651060)
    # st_time = time()
    # for i in a:
    #     pr = Process(target=factorize_process, args=(i, ))
    #     pr.start()
    #     process.append(pr)
    #     # print(pr)


    # [pr.join() for pr in process]
    end_time = time()
    delta_time = end_time - st_time
    print(f"Test with class Process - {delta_time}")
 