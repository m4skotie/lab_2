N = int(input("Номер билета: "))
if 1 <= N <= 36:
    print ("Купе")
    if (N % 2 == 0):
        print ("Верхнее место")
    elif (N % 2 != 0):
        print ("Нижнее место")
elif 37 <= N <= 54:
    print ("Боковое место")
else:
    print("Чел ты...")