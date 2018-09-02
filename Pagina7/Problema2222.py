
for i in range(int(input())):
    conjuntos = []
    for j in range(int(input())):
        itens = input().split()
        conjuntos.append(itens[1:])
    for p in range(int(input())):
        lista = map(int,input().split())
        n1,n2,n3 = lista
        if n1==1:
            print(len(set(conjuntos[n2-1]) & set(conjuntos[n3-1])))
        else:
            print(len(set(conjuntos[n2-1]) | set(conjuntos[n3-1])))
    