'''Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12'''

'''from random import randint 
#эмуляция случайности, Чтобы обращаться к функциям, надо импортировать модуль random (в этом случае отдельные функции из него)
n, m = [int(input()) for _ in range(2)] 
#сохраняем введенное пользователем цикл задает значение индексной переменной
first_set = set(randint(1, 100) for _ in range(n))
second_set = set(randint(1, 100) for _ in range(m))
print(first_set, second_set, sep='\n')
#\убирает ковычки
print(*sorted(first_set.intersection(second_set)))'''

from random import randint
n, m = [int(input()) for _ in range(2)]
first_set = set(randint(1, 100) for _ in range(n))
second_set = set(randint(1, 100) for _ in range(m))
print(first_set, second_set, sep='\n')
print(*sorted(first_set.intersection(second_set)))
