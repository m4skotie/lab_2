"134"
color1 = input("Введите первый цвет: ")
color2 = input("Введите второй цвет: ")

if color1 == "red" and color2 == "yellow" or color1 == "yellow" and color2 == "red":
    print("Оранжевый")
elif color1 == "red" and color2 == "blue" or color1 == "blue" and color2 == "red":
    print("Фиолетовый")
elif color1 == "blue" and color2 == "yellow" or color1 == "yellow" and color2 == "blue":
    print("Зеленый")
else:
    print("Чел ты...")