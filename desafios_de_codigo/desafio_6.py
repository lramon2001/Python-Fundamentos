n = int(input())
#Informe o seu código aqui
if n%2 != 0:
    print("Estranho")
elif n%2 == 0 and n<10:
    print("Não é estranho")
elif n%2 == 0 and n>10 and n<20:
    print("Estranho")
else :
    print("Não é estranho")
