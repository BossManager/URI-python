
for i in range(int(input())):
    conjuntos = []
    for j in range(int(input())):
        conjuntos.append(input().split()[1:])
    for p in range(int(input())):
        n1,n2,n3 = map(int,input().split())
        if n1==1:
            print(len(set(conjuntos[n2-1]) & set(conjuntos[n3-1])))
        else:
            print(len(set(conjuntos[n2-1]) | set(conjuntos[n3-1])))
    