def calculator(s: str, num1: float, num2: float) -> float:
    """Простейший калькулятор"""
    while True:
        s = input('Введите действие (+,-,/,*): ')
        d = ('+', '-', '/', '*')
        if s in d:
            print('Пока все верно')
        else:
            print('Неверный знак операции!')
            continue
        try:
            num_1 = float(input('Введите первое число: '))
            num_2 = float(input('Введите второе число: '))
        except ValueError:
            print('Пожалуйста, вводите только числа')
        else:
            if s == '+':
                print(num_1 + num_2)
            elif s == '-':
                print(num_1 - num_2)
            elif s == '*':
                print(num_1 * num_2)
            elif s == '/':
                try:
                    if num2 == 0:
                        print(num_1 / num_2)
                except ZeroDivisionError:
                    print('Делить на ноль нельзя')
                else:
                    print(num_1 / num_2)
        if input('Если не хотите продолжить введите "n": ') == 'n':
            break

calculator()

