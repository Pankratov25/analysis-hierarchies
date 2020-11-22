# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 19:31:40 2020

@author: nik25
"""


import numpy as np


def isfloat(value):  # Функция, определяющая, какое значение важности введено
    try:
        float(value)
        return True
    except ValueError:
        return False

def matrix(k): 
    M = np.ones([k, k])  # Создаем матрицу из единиц
    for i in range(0, k):
        for j in range(0, k):
            if i < j:  # Все, что выше главной диагонали, меняем на введенные польз-лем значения
                print("Насколько критерий", i + 1, "важнее чем", j + 1, "? Введите число от 0.1 до 9: ", end='')
                a = input()
                if isfloat(a) and (0.11 <= float(a) <= 9):
                    M[i, j] = float(a)
                    M[j, i] = 1 / float(a)
                else:  # Учитываем ошибки
                    print("Введены неверные данные. Попробуйте еще раз.")
                    print("Насколько критерий", i + 1, "важнее чем", j + 1, "? Введите число от 0.1 до 9: ", end='')
                    a = input()
                    if isfloat(a) and (0.11 <= float(a) <= 9):
                        M[i, j] = float(a)
                        M[j, i] = 1 / float(a)
                    else:  # Если во второй раз введены неверные значения, устанавливаем важность = 1
                        print("Введены неверные данные. Критерии одинаково важны.")
                        a = 1
                        M[i, j] = float(a)
                        M[j, i] = 1 / float(a)
    return M
