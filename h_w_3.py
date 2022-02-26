# Задание №1
name = input('Введите Ваше имя: ')
years = int(input('Введите Ваш возраст: '))
floor = input('Введите Ваш пол (Mr/Mrs): ')
if years >= 18:
    print(f'Приветствую Вас {floor} {name} в нашей игре')
else:
    print(f'Дорогой {floor} {name}, к сожалению в нашей игре могут принимать участие только совершеннолетние люди!')


 # Задание № 2
while True:
    name = input('Введите Ваше имя: ')
    years = int(input('Введите Ваш возраст: '))
    floor = input('Введите Ваш пол (Mr/Mrs): ')
    if years >= 18:
        print(f'Приветствую Вас {floor} {name} в нашей игре')
    else:
        print(f'Дорогой {floor} {name}, к сожалению в нашей игре могут принимать участие только совершеннолетние люди!')
        continue

 # Задание №3 *
import random
total = 0
print(f'Игра угадай число!')
while True:
    num = random.randrange(9)
    if num != int(input('Введите число от 1 до 9: ')):
        print('Неверно!')
        total += 1
        continue
    else:
        print(f'Поздравляем, вы угадали число {num}, количество неверных попыток равно: {total}')
        break

# Задание №3 **
import random
print('Игра суперлото третий уровень')
name = input('Представьтесь пожалуйста: ')
new_numbers = []
prize = 0
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
while len(numbers) != 0:
    num = random.choice(numbers)
    new_numbers.append(num)
    numbers.remove(num)
    print(f'{len(new_numbers)} тур игры')
    new_num = int(input(f'Введите число от 0 до 9: '))
    if new_num not in new_numbers:
        prize += 100
        print(f'{name} поздравляем, вы выиграли {prize} рублей')
        rez = input(f'Нажмите ввод, что-бы продолжить или введите "забрать" для того, чтоб забрать выигрыш ')
        if rez =='забрать':
            print(f'{name} вы выиграли {prize} рублей')
            break
    else:
        print(f'{name} вы проиграли')
        print(f'Ваш выигрыш составил {prize} рублей')
        print(f'Цифры, которые приняли участие в игре {new_numbers}')
        break