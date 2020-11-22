# -*- coding: utf-8 -*-

import numpy as np


def isfloat(value):  # Функция, определяющая, какое значение важности введено
    try:
        float(value)
        return True
    except ValueError:
        return False

