"134"
import random
s = ""
n = random.randint(1, 10)
for i in range(n):
    a = str(input("Введите слово: "))
    s = s + " " + a
print(s)