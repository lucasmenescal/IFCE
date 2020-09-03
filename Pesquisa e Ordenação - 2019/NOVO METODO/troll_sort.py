from random import randint
import random
    
def geraLista(tam):
    lista = []
    lista = random.sample(range(tam), tam)
    return lista

def troll_sort(lista):
    end = len(lista)
    mid = int(end/2)
    right = []
    left = []
    elementos = mid-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False
                print(lista)
    elementos = (end-1)
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(mid,elementos):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False
                print(lista)
    elementos = (end-1)
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False
                print(lista)
    return lista

if __name__ == '__main__':
    x = int(input("Tamanho da Lista: "))
    y = []
    z = []
    y = geraLista(x)
    z = troll_sort(y)
    print("------------------------------------------------------------")
    print(z)
