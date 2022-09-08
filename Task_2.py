# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


n_list = [1, 2, 3, 4, 5, 6]

def multi(n_list):
    multi_list = []
    for i in range (len(n_list)-(len(n_list)//2)):
        a = n_list[i] * n_list[len(n_list) - 1 -i]
        multi_list.append(a)
    return(multi_list)  

print(multi(n_list))