from multiprocessing import cpu_count
from threading import Thread
from datetime import datetime

# num_cpu = cpu_count()
# print(num_cpu)


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
    # result_list = []
    start_time = datetime.now()
    factorize_num = Number(number)
    result = factorize_num.dividing_of_numbers()
    end_time = datetime.now()
    time_result = end_time - start_time
    print(f"{number} - {result} time for this operation {time_result}")
    return result


if __name__ == '__main__':

    a = [128, 255, 99999, 10651060]
    start_time_all = datetime.now()

    for i in a:
        
        th = Thread(target=factorize, args=(i, ))
        th.start()

    end_time_all = datetime.now()
    time_result_all = end_time_all - start_time_all

    print(f"time for all process - {time_result_all}")