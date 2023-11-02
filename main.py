print('Введите числа последовательности')
x = int(input())
s = 0
while not x == 0:
    y = x
    if y < 0:
        s = s + x
    else:
        x = int(input())
        print(s)