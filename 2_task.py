# 2'. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# * 6 -> [2,3]
# * 144 -> [2,3]

def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans


def get_unique_numbers(Ans):
    unique = []

    for number in Ans:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique


print(get_unique_numbers(Factor(int(input('Задайте натуральное число N: ')))))