import json
import csv
import openpyxl

name = input('Введите Ваше имя: ')
age = int(input('Введите Ваш возраст: '))
city = input('Введите Ваш город: ')

keys = ['name', 'age', 'city']
values = [name, age, city]
info = dict(zip(keys, values))


with open("file.json", 'w') as write_file:
    json.dump(info, write_file)


with open('file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(keys)
    writer.writerow(values)



book = openpyxl.Workbook()
sheet = book.active
for i, row in enumerate(info):
    sheet[f'A{i+1}'] = row
for j, row in enumerate(values):
    sheet[f'B{j+1}'] = row

book.save('info.xlsx')
book.close()


with open('info.txt', 'w') as file:
    for i in range(len(keys)):
        file.write(f'{keys[i]}: {values[i]}\n')

f = open('info.txt', 'r')
print(*f)