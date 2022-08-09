import re

n = int(input())

for i in range(0, n):
    regex = input()
    try:
        re.compile(regex)
        print("Válida")
    except:
        print("Inválida")
