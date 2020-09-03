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

def quick_sort(lista):
   quickSortHelper(lista,0,len(lista)-1)

def quickSortHelper(lista,first,last):
   if first<last:

       splitpoint = partition(lista,first,last)
       quickSortHelper(lista,first,splitpoint-1)
       quickSortHelper(lista,splitpoint+1,last)


def partition(lista,first,last):
   pivotvalue = lista[first]
   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and lista[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while lista[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = lista[leftmark]
           lista[leftmark] = lista[rightmark]
           lista[rightmark] = temp

   temp = lista[first]
   lista[first] = lista[rightmark]
   lista[rightmark] = temp


   return rightmark

def desenhaGrafico(x,y,xl = "Entradas", yl = "Saídas", z='Tempo'):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = z)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig('teste.png', format='png')
    plt.show()

def iniciarquicksort(lista):
    quick_sort(lista)
    return 0

if __name__ == '__main__':
    
    z = [100000, 200000, 300000, 400000, 500000, 1000000, 2000000]
    lista = []
    newlista = []
    x = []
    for i in range(len(z)):
        x.append(geralista(z[i]))
    y = []
    for i in range(len(x)):
        y.append(timeit.timeit("iniciarquicksort({})".format(x[i]), setup="from __main__ import iniciarquicksort", number=1))

    desenhaGrafico(z,y)
    
    
