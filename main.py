from time import time
from threading import Thread
from multiprocessing import Process, Pool, current_process, cpu_count



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
        result = [n for n in range(1, int(self.number / 2) + 1) if self.number % n == 0]  # діапазон ділю на 2 тим самим скорочую час роботи ф-ції, але треба потім додати саме число в кінець списку
        result.append(self.number) # додаю селф останнім елементом списку
        return result


def factorize_synhron(*number):
    result_list = []
    for i in number:
        factorize_num = Number(i)
        result_list.append(factorize_num.dividing_of_numbers())
    return [*result_list]


def factorize(number):
    factorize_num = Number(number)
    result = factorize_num.dividing_of_numbers()
    return result


def callback(result):
    ...
    # print(f"Result in callback: {result}")


if __name__ == '__main__':

    
    st_time = time()
    a, b, c, d = factorize_synhron(128, 255, 99999, 10651060)
    # a, b, c, d = factorize_synhron(99999, 2555555, 999999, 100651060)
    ft_time = time()
    delta_time = ft_time - st_time
    print(f"Test synchronic - {delta_time}")

    thr = []
    st_time = time()
    for i in a:
        
        th = Thread(target=factorize, args=(i, ))
        th.start()
        thr.append(th)

    [th.join() for th in thr]

    ft_time = time()
    delta_time = ft_time - st_time
    print(f"Test with Thread - {delta_time}")

    print(f"Count CPU: {cpu_count()}")
    st_time = time()
    with Pool(cpu_count()) as p:
        p.map_async(
            factorize,
            a,
            callback=callback,
        )
        p.close()  # перестати виділяти процеси в пулл
        p.join()  # дочекатися закінчення всіх процесів

    # print(f'End {current_process().name}')
    end_time = time()
    delta_time = end_time - st_time
    print(f"Test with process_map - {delta_time}")


    proc = []
    st_time = time()
    for i in a:
        pr = MyProcess(args=factorize, kwargs=i)
        pr.start()
        proc.append(pr)

    [el.join() for el in proc]

    end_time = time()
    delta_time = end_time - st_time
    print(f"Test with class MyProcess(Process) - {delta_time}")

    # print(a)
    # print(b)
    # print(c)
    # print(d)
    # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    # assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]



