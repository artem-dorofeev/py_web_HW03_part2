# import sys
from multiprocessing import Process
from time import time


class MyProcess(Process):

    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args
        self.kwargs = kwargs  # here could be data

    def run(self) -> None:
        self.args(self.kwargs)


class Number():
    def __init__(self, number: int) -> None:
        self.number = number

    def dividing_of_numbers(self):
        result = [n for n in range(1, int(self.number / 2) + 1) if self.number % n == 0]
        result.append(self.number)
        # print(f"Class Number({self.number}) - {result}")
        return result


def factorize_process(num):
    factorize_proc = Number(num)
    result = factorize_proc.dividing_of_numbers()
    # print(f"Func factorize({num}) - {result}")
    return result


if __name__ == '__main__':
    proc = []
    # a = (99999, 2555555, 999999, 100651060)
    a = (128, 255, 99999, 10651060)
    st_time = time()
    for i in a:
        pr = MyProcess(args=factorize_process, kwargs=i)
        # print(i)
        pr.start()
        proc.append(pr)

    [el.join() for el in proc]

    end_time = time()
    delta_time = end_time - st_time
    print(f"Test with class MyProcess(Process) - {delta_time}")