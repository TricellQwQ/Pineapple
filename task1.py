data = [line.rstrip("\n").split(";") for line in open("cars.csv", mode="r", encoding="UTF-8").readlines()[1:]]
# Распаковка данных в формате вложенных списков
ans = []
volvo = ["Volvo"]
# Переменные для хранения итоговых строк
# ans - переменная для хранения данных о красных машинах
# volvo - переменная для хранения данных о красных машинах марки volvo
for elem in data:
    if elem[5] == "красный":
        ans.append(f"У {elem[2]} {elem[3]} есть машина красного цвета. Ее стоимость {elem[0]}")
        # Занесение итоговых строк в переменную ans
        if elem[2] == "volvo":
            volvo.append(f"{elem[3]} есть машина красного цвета. Ее стоимость {elem[0]}")
            # Занесение итоговых строк в переменную volvo
with open("red_car.txt", mode="w", encoding="UTF-8") as f:
    f.write("\n".join(ans))
    # Запись файла red_car.txt
for line in volvo:
    print(line)
    # Вывод ответа в консоль
