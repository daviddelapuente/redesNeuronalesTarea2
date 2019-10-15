from algoritmosGeneticos.boundknapsack.knapsuite import *


def initPopulation(populationLen,W):
    population=[]

    for i in range(populationLen):

        population.append(generateRandomknapsack(W))


    return population




def fitnesses(population,V,W,maxW):
    fitness=[]

    for p in population:
        fitness.append(knapsackFit(V,W,maxW))

    return fitness



##############################################################


def findKnapSack(W,V,trys):
    print("buscando knapsack para W="+str(W)+" y V="+str(V))




findKnapSack([10,2,3],[1,3,4],100)









