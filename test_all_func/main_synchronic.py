from time import time


class Number():
    def __init__(self, number: int) -> None:
        self.number = number

    def dividing_of_numbers(self):
        result = [n for n in range(1, int(self.number / 2) + 1) if self.number % n == 0]
        result.append(self.number)
        return result


def factorize_synhron(*number):
    result_list = []
    for i in number:
        factorize_num = Number(i)
        result_list.append(factorize_num.dividing_of_numbers())
    return [*result_list]


if __name__ == '__main__':


    st_time = time()
    a, b, c, d = factorize_synhron(128, 255, 99999, 10651060)
    # a, b, c, d = factorize_synhron(99999, 2555555, 999999, 100651060)
    ft_time = time()
    delta_time = ft_time - st_time
    # print(a)
    # print(b)
    # print(c)
    # print(d)
    # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    # assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    print(f"Test without process - {delta_time}")


