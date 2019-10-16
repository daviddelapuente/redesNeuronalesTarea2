from algoritmosGeneticos.boundknapsack.knapsuite import *

#inicia una poblacion de largo population len y el largo de la mochila es el largo de W
def initPopulation(populationLen,V,W,maxW):
    population=[]
    for i in range(populationLen):
        population.append(knapsack(V,W,maxW))
    return population

#calcula el fitness de cada mochila segun su V, W y maxW
def fitnesses(population):
    fitness=[]
    for p in population:
        fitness.append(p.fitness())
    return fitness

#devuelve un arreglo de largo n, el que contiene numeros aleatoreos entre 0 y l-1
def randIndex(l,n):
    r=[]
    for i in range(n):
        r.append(random.randint(0, l - 1))
    return r

##############################################################


def findKnapSack(V,W,maxW,trys,populationLen,Ncompetitors):
    print("buscando knapsack para W="+str(W)+" y V="+str(V))

    population = initPopulation(populationLen,V,W,maxW)

    #como queremos encontrar la mejor mochila, hacemos trys iteraciones
    for t in range(trys):

        #aca se ira guardando la desendencia de la nueva poblacion.

        newPopulation=[]

        #queremos que el largo de la poblacion sea  el mismo siempre, por lo que vamos
        #agregando nuevos valores a newPopulation hasta que sus valores sean iguales.

        while(len(newPopulation)<len(population)):

            #buscamos indices al azar
            competitorsI=randIndex(len(population),Ncompetitors)

            #buscamos a los competidores, por los indices anteriores
            competitors=[]
            for i in competitorsI:
                competitors.append(population[i])


            #calculamos sus fitness, tal que fitness corresponde 1 a 1 con competitors y competitorsI
            fitness=fitnesses(competitors)
            # tournament
            max1 = -1
            max2 = -1
            winner1 = competitors[0]
            winner2 = competitors[0]
            for i in range(len(competitors)):
                if fitness[i] > max1:
                    max1=fitness[i]
                    winner1 = competitors[i]

            for i in range(len(competitors)):
                if competitors[i] != winner1 and fitness[i] > max2:
                    max2=fitness[i]
                    winner2 = competitors[i]

            son = knapCrossOver(winner1,winner2)
            newPopulation.append(son)

        population=newPopulation

    maxfit=-1
    best=0
    F=fitnesses(population)
    for i in range(len(F)):
        if F[i]>maxfit:
            maxfit=F[i]
            best=i



    population[best].summary()

W=[12,2,1,1,4]
V=[4,2,2,1,10]
maxW=15


findKnapSack(V,W,maxW,1000,10,3)









