n = int(input())

lista = []
for i in range(0, n):
    values = input().split()

    if len(values) == 3:
        acao, i, e = values
    elif len(values) == 2:
        acao, e = values
    else:
        acao = values.pop()
    
    if acao == "insert":
        lista.insert(int(i), int(e))
    elif acao == "print":
        print(lista)
    elif acao == "remove":
        lista.remove(int(e))
    elif acao == "append":
        lista.append(int(e))
    elif acao == "sort":
        lista.sort()
    elif acao == "pop":
        lista.pop()
    elif acao == "reverse":
        lista.reverse()
