# 3'. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.


numbers = [8, 8, 8, 1, 2, 2, 56, 4, 5, 5, 7, 9]


def get_unique_numbers(numbers):
    unique = []

    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique


print(get_unique_numbers(numbers))
