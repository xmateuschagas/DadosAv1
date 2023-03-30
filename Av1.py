import time
import matplotlib.pyplot as plt

ns = []
tempos = []
elementos = [[0,1,2,3],[11,12,13,4],[10,15,14,5],[9,8,7,6]]
lista = []

for elemento in elementos:
    for item in elemento:
        lista.append(item)

for i in range(len(lista)):
    for j in range(len(lista)-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1],lista[j]
print(lista)

for i in range(len(lista)):
    for j in range(len(lista)-1):
        if lista[j] < lista[j+1]:
            lista[j], lista[j+1] = lista[j+1],lista[j]
print(lista)

def comple():
    for elemento in elementos:
        for item in elemento:
            lista.append(item)

    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1],lista[j]

    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] < lista[j+1]:
                lista[j], lista[j+1] = lista[j+1],lista[j]

for n in range(len(lista)):
    start = time.perf_counter()
    comple()
    end = time.perf_counter()
    ms = (end-start) * 10**6
    ns.append(n)
    tempos.append(ms)

print(ns)
print(tempos)

plt.plot(ns, tempos)
plt.xlabel('Valor de n')
plt.ylabel('Tempo de execução (micro segundos)')
plt.show()
