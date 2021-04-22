import math
print("######Код Гилберта-Мура######")
try:
    Alfa=[str(i) for i in input("Введите алфавит: ").split()]
    P=[float(i) for i in input("Введите вероятности: ").split()]
    Q=[]
    L=[]
    d=0
    for i in range(len(P)):
        Q.append(round(d+(P[i]/2),2))
        d=d+P[i]
        L.append(math.ceil(math.fabs(-1 * (math.log(P[i],2)))+1))
    print("Qi:",Q)
    print("Li:",L)
    Bin = [[0 for j in range(L[i])] for i in range(len(Q))]
    for i in range(0,len(Q)):
       for j in range(0,L[i]):
           Q[i]=Q[i]*2
           if (Q[i]> 1):
                Bin[i][j] = math.trunc(Q[i])
                Q[i] = Q[i] - 1
           else:
                Bin[i][j]=math.trunc(Q[i])
    print("Код:",Bin)
except:
    print("Ошибка")