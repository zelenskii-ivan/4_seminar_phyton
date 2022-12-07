#  5'. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9

import io
from sympy import *

NUM_STEPS = 2

str_sum = ''
list_source = []

for i in range(1, NUM_STEPS + 1):
    with io.open(f'file{i}.txt', 'r') as f:
        list_source.append(f.readline()[:-1])

str_sum = ((list_source[0] + list_source[1])[: - 2])
print(str_sum)

sum = simplify(str_sum)
print(sum)

f_out = io.open('file_sum.txt', 'w')
print(sum, file=f_out)
f_out.close()