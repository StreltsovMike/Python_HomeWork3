# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
import math

n_list = [1.1, 2.2, 3.1, 4.5001, 6.01]
ostatok_list = []
for i in range(len(n_list)):
    #ostatok = n_list[i] - math.floor(n_list[i])
    #ostatok = n_list[i] - int(n_list[i])
    ostatok = n_list[i] % 1
    #ostatok = math.floor(ostatok*1000)/1000
    ostatok = round(ostatok, 5)
    ostatok_list.append(ostatok)
print(ostatok_list)

max, min = 0, 1

for i in range(len(ostatok_list)):
    if(ostatok_list[i] > max):
        max = ostatok_list[i]
    elif(ostatok_list[i] < min):
        min = ostatok_list[i]

print(f'{max} - {min} = {max-min}')

