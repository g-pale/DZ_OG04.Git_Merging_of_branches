# Программа для нахождения четных чисел в диапазоне

print('Программа для нахождения четных чисел в диапазоне')

numbers = []

list_begin = int(input('Введите число начала диапазона: - '))
list_end = int(input('Введите число конца диапазона: - '))

for i in range(list_begin, list_end + 1):
  numbers.append(i)

print(f'Диапазон Ваших чисел {numbers}')


for element in numbers:
    if element % 2 == 0:
        print(f'Число {element} четное')