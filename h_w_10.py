while True:
    s = input('Введите действие (+,-,/,*): ')
    d = ('+', '-', '/', '*')
    if s in d:
        print('Пока все верно')
    else:
        print('Неверный знак операции!')
        continue
    try:
        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите второе число: '))
    except ValueError:
        print('Пожалуйста, вводите только числа')
    else:
        if s == '+':
            print(num1 + num2)
        elif s == '-':
            print(num1 - num2)
        elif s == '*':
            print(num1 * num2)
        elif s == '/':
            try:
                if num2 == 0:
                    print(num1 / num2)
            except ZeroDivisionError:
                print('Делить на ноль нельзя')
            else:
                print(num1 / num2)
    if input('Если не хотите продолжить введите "n": ') == 'n':
        break