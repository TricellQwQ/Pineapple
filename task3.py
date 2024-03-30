data = [line.rstrip("\n").split(";") for line in open("cars.csv", mode="r", encoding="UTF-8").readlines()[1:]]
# Распаковка данных в формате вложенных списков
request = input("Введите марку машины и цвет через пробел\n")
# Обработка запроса
while request != "car none":
    result = []
    for elem in data:
        if elem[2] == request.split()[0] and elem[5] == request.split()[1]:
            result.append(elem)
    # Поиск соответствий по запросу
    if result:
        print(f"По вашему запросу: {request.split()[0]} {request.split()[1]} найдены следующие варианты:")
        for i in range(len(result)):
            print(f" {str(i + 1)}.  {result[i][2]} {result[i][3]} цена {result[i][0]}, пробег данной машины составляет {result[i][4]}")
    else:
        print("По данным параметрам ничего не найдено")
    # Вывод ответа на запрос
    request = input("Введите марку машины и цвет через пробел\n")
    # Обработка запроса
