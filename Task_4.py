# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное (без встроенных функций).

def binary(num):
    count = 0
    num1 = num
    while (num1 >= 2):
        num1 /= 2
        count += 1
    n = count
    numbers = []
    for i in range(n + 1):
        if ((num) >= (2**(n))):
            numbers.append(1)
            num -= (2**n)
        else:
            numbers.append(0)
        n -=1
    ansswer = 0
    d = len(numbers)-1
    for i in range(len(numbers)):
        ansswer += (numbers[i]*(10**d))
        d -= 1
    return(ansswer)

    
num = int(input('Число : '))
print(f'{num} = {binary(num)}')
