n = int(input())

for i in range(0, n):
    try:
        a, b = input().split()
        print(int(a) // int(b))
    except ZeroDivisionError as e:
        print ("Erro:",e)
    except ValueError as e:
        print ("Erro:",e)
