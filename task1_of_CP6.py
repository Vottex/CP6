import random
def FillMassive(Massive, Size):
    for i in range(Size):
        number = random.randint(-1000, 1000)/10
        Massive.append(number)
    print(Massive)

A = []
B = []
Common = []

SizeA = input("Введите целое число - размер первого массива: ")
SizeB = input("Введите целое число - размер второго массива: ")

try:
    SizeA=int(SizeA)
    SizeB=int(SizeB)
    Check=True
except ValueError:
    print("Ввод некорректен, введите целые числа")
    Check=False

if Check:
    FillMassive(A, SizeA)
    FillMassive(B, SizeB)
    for i in A:
        if i in B:
            Common.append(i)
    print("Общие числа: ", Common)