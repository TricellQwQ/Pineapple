data = [line.rstrip("\n").split(";") for line in open("cars.csv", mode="r", encoding="UTF-8").readlines()[1:]]
# Распаковка данных в формате вложенных списков
new_data = []
# new_data - список с изменёнными данными об автомобилях по скидке
for elem in data:
    if float(elem[4]) > 70000:
        new_data.append([elem[2], elem[3], elem[4], str(int(elem[0]) * 0.88)])
# Заполнение нового списка данными
for i in range(10):
    print(f"{new_data[i][0]} {new_data[i][1]}; Пробег: {new_data[i][2]}; Цена: {new_data[i][3]}")
# Вывод ответа
