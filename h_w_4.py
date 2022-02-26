# №4/1 Создать генератор для заполнения списка
num = [i for i in range(10)]
print(num)

# №4/2. Создать функцию для генерации списков с аннотациями
txt = input('введите строку ')
def generator(txt: str) -> list:
    ls = [i for i in txt]
    print(ls)
generator(txt)


# №4/3. *Сделать функцию которая будет вызываться из генератора и отдавать текущее время
from datetime import datetime

def time():
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    return t

n = int(input('Введите число '))
num = [time() for i in range(1, n+1)]
print(*num)

