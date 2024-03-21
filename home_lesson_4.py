# Запрашиваем данные
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = input('Выберите операцию (Введите +, -, * или /): ')

if c == '+':
    d = a + b
    print(d)
elif c == '-':
    d = a - b
    print(d)
elif c == '*':
    d = a * b
    print(d)
elif c == '/':
    # Проверка деления на ноль
    if b != 0:
        d = a / b
        print(d)
    else:
        d = "Деление на ноль невозможно"
        print(d)
