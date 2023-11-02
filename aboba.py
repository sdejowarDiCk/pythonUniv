print('Введите элементы последовательности:')
sum = 0
save = 0
x = int(input())
while not x == 0:
    if x < 0:
        sum += save
    save = x
    x = int(input())
print('Сумма таких элементов равна =', sum)
