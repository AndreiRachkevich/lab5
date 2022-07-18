# 1. Создайте итерируемый объект, возвращающий генератор тридцати пяти чисел трибоначчи и выведите эти числа.


class TribonacciIterator:
    def __init__(self):
        self.f_1 = 0
        self.f_2 = 0
        self.f_3 = 1

    def __next__(self):
        result = self.f_1
        self.f_1, self.f_2, self.f_3 = self.f_2, self.f_3, self.f_1 + self.f_2 + self.f_3
        return result

    def __iter__(self):
        return self

for i in TribonacciIterator():
    print(i)

    if i == 181997601:
        break