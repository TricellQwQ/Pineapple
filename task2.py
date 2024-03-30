data = [line.rstrip("\n").split(";") for line in open("cars.csv", mode="r", encoding="UTF-8").readlines()[1:]]
# Распаковка данных в формате вложенных списков
for i in range(len(data)):
    for j in range(i):
        if float(data[j][4]) > float(data[i][4]):
            data = data[:j] + [data[i]] + data[j:i] + data[i + 1:]
# Сортировка списка по пробегу методом вставок
print("Вам могут подойти:")
for i in range(3):
    elem = data[i]
    print(f"{elem[2]} {elem[3]}; Цвет: {elem[5]} ; Пробег: {elem[4]}; Цена: {elem[0]}")
# Вывод ответа в консоль
