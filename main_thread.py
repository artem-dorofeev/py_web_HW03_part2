from multiprocessing import cpu_count
from threading import Thread
from time import time
import sys
from multiprocessing import Process

# num_cpu = cpu_count()
# print(num_cpu)



# class MyProcess(Process):

#     def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
#         super().__init__(group=group, target=target, name=name, daemon=daemon)
#         self.args = args
#         self.kwargs = kwargs  # here could be data

#     def run(self) -> None:
#         self.kwargs.get('log')(f"args: {self.args}")
#         sys.exit(0)



class Number():
    def __init__(self, number: int) -> None:
        self.number = number

    def dividing_of_numbers(self):
        result = []
        for i in range(1, int(self.number / 2) + 1): # діапазон ділю на 2 тим самим скорочую час роботи ф-ції, але треба потім додати саме число в кінець списку
            if self.number % i == 0:
                result.append(i)
        result.append(self.number) # додаю селф останнім елементом списку
        return result


def factorize(number):
    factorize_num = Number(number)
    result = factorize_num.dividing_of_numbers()
    # print(f"{number} - {result} time for this operation {time_result}")
    return result


if __name__ == '__main__':

    thr = []
    # a = [99999, 2555555, 999999, 1006510600]
    a = (128, 255, 99999, 10651060)
    st_time = time()

    for i in a:
        
        th = Thread(target=factorize, args=(i, ))
        th.start()
        # print(th)
        thr.append(th)

    # [th.join() for th in thr]

    ft_time = time()
    delta_time = ft_time - st_time

    print(f"Test with Thread - {delta_time}")