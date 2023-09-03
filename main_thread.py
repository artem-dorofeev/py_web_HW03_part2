from threading import Thread
from time import time


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
    return result


if __name__ == '__main__':

    thr = []
    # a = [99999, 2555555, 999999, 1006510600]
    a = (128, 255, 99999, 10651060)
    st_time = time()

    for i in a:
        
        th = Thread(target=factorize, args=(i, ))
        th.start()
        thr.append(th)


    ft_time = time()
    delta_time = ft_time - st_time

    print(f"Test with Thread - {delta_time}")