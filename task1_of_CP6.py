import random
a = []
b = []
common_numbers = []
size_a = input("Введите размер первого массива (должно быть целое число): ")
size_b = input("Введите размер второго массива (должно быть целое число): ")


def fill_array(massive, size):
    for i in range(size):
        number = random.randint(-1000, 1000)/10
        massive.append(number)
    print(massive)


try:
    size_a = int(size_a)
    size_b = int(size_b)
    Check = True
except ValueError:
    print("Ввод некорректен, введите целые числа")
    Check = False

if Check:
    fill_array(a, size_a)
    fill_array(b, size_b)
    for i in a:
        if i in b:
            common_numbers.append(i)
    print("Общие числа: ", common_numbers)
