import random

#genera un encode para un knapsack, donde un 1 en la posicion i, representa que dicho elemento esta en la mochila
def generateRandomknapsack(W):
    knapsack=[]
    for i in range(len(W)):
        knapsack.append(random.randint(0,1))
    return knapsack

#calcula el fit de una mochila (segun sus valores, sus pesos y su peso maximo)
def knapsackFit(V,W,maxW):
    value=sum(V)
    weights=sum(W)
    if weights<=maxW:
        return value
    else:
        #si la mochila exede el peso, se castiga.
        return value-punishment(weights,maxW)


#funcion de castigo (puede cambiar para experimentar)
#si una mochila se pasa del peso, se le resta la diferencia a su valor.
def punishment(w,maxW):
    return w-maxW