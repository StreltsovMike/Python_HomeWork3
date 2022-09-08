# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
def fibanachi(num):
    fiba = [0, 1]
    for i in range(num):
        sum = fiba[len(fiba)-1] + fiba[len(fiba)-2]
        fiba.append(sum)
    n =0
    for i in range(1, len(fiba)):
        min = fiba[i+n] * ((-1)**n)
        fiba.insert(0, min)
        n += 1
    return(fiba)

num = int(input('Сколько итераций провести? '))
print(fibanachi(num))



