data = [line.rstrip("\n").split(";") for line in open("cars.csv", mode="r", encoding="UTF-8").readlines()[1:]]
# Распаковка данных в формате вложенных списков
stats = {}
# stats - словарь формы [марка афтомобиля]: [колличество автомобилей марки в ключе]
for elem in data:
    stats[elem[2]] = stats.get(elem[2], 0) + 1
# Занесение информации о колличестве автомобилей по марке
print("Колличество автомобилей по марке:")
for mark in ["gmc", "chevrolet", "toyota", "ford", "jeep", "nissan", "ram", "cadillac", "honda", "dodge"]:
    print(f"{mark} - {stats[mark]}")
# Вывод ответа
