# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции

from random import Random, randint
n = int(input('Введите N : '))
n_list = []
for i in range(n):
    n_list.append(randint((-n),(n)))
print(n_list)


def sum_1(n_list):
    sum =0
    for i in range(1, n, 2):
        sum += n_list[i] 
    print(sum)
    return(sum)

sum_1(n_list)