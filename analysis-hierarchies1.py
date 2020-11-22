# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 17:51:30 2020

@author: nik25
"""


import numpy as np


def isfloat(value):  # Функция, определяющая, какое значение важности введено
    try:
        float(value)
        return True
    except ValueError:
        return False


