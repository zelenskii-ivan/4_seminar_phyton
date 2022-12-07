# 4'. Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать 
# в файл многочлен степени k.(записать в строку)
# Пример:
# k=2 => 2*x^2 + 4*x + 5 или x^2 + 5 или 10*x**2
# k=3 => 2*x^3 + 4*x^2 + 4*x + 5

from random import randint

coefficients = []
k = int(input('Введите степень многочлена: '))
for i in range(k + 1):
    num = randint(- 10, 10)
    coefficients.append(num)

print(coefficients)
result = ''
for i in range(len(coefficients)):
    if len(result) > 0 and coefficients[i] > 0:
        result = result + ' + '
    if coefficients[i] == 0:
        continue

    result = result + str(coefficients[i]) + 'X^' + str(k - i)

if coefficients[- 1] != 0:
    result = result[:len(result) - 3]
result = result + ' = 0'
print(result)

with open('test.txt', 'w') as f:
    f.write(result)