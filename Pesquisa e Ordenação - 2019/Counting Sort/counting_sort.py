from random import randint
import timeit
import random
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
def geralista(tam):
    lista =[]
    lista = random.sample(range(0,tam),tam)
    return lista

def counting_sort(lista, max_val):
    m = max_val + 1
    count = [0] * m                
    
    for a in lista:
        count[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            lista[i] = a
            i += 1
    return lista
def desenhaGrafico(x,y,xl = "Entradas", yl = "Saídas", z='Tempo'):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = z)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig('teste.png', format='png')
    plt.show()



if __name__ == '__main__':
    z = [100000, 200000, 300000, 400000, 500000, 1000000, 2000000]
    lista = []
    newlista = []
    x = []
    for i in range(len(z)):
        x.append(geralista(z[i]))
    y = []
    for i in range(len(x)):
        y.append(timeit.timeit("counting_sort({},{})".format(x[i],z[i]), setup="from __main__ import counting_sort", number=1))
    desenhaGrafico(z,y)
    
    
