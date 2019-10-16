
from algoritmosGeneticos.findingWords.wordSuite import *

#posibles abecedarios
wordAbc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z',' ']
binAbc=['0','1']


#inicia una poblacion de larga populationLen, con individuos de largo l definidos por el abecedario abc
def initPopulation(populationLen,l,abc):
    population=[]
    for i in range(populationLen):
        population.append(generateRandomString(l,abc))
    return population

#calcula el fitnes para un subconjunto de la poblacion
def fitnessesI(population,word,competitors):
    fitness=[]
    for i in range(len(competitors)):
        f=matchString(word, population[competitors[i]])
        fitness.append(f)
    return fitness

#calcula el fitness para la poblacion
def fitnesses(population,word):
    fitness=[]
    for p in population:
        fitness.append(matchString(word,p))
    return fitness

#devuelve un conjunto al azar de indices entre 0 y l-1
def randIndex(l,n):
    r=[]
    for i in range(n):
        r.append(random.randint(0, l - 1))
    return r

#algoritmo genetico que encuentra una palabra
def find(word,trys,populationLen,Ncompetitors,abc):
    print("buscando :"+word)


    #calculamos el largo de la palabra, para inicializar una poblacion al azar de palabras con ese largo
    #la poblacion es de largo populationLen
    l = len(word)
    population = initPopulation(populationLen, l,abc)


    #como queremos encontrar la mejor palabra, iteramos el numero de trys
    for t in range(trys):

        #aca se ira guardando la desendencia de la nueva poblacion.
        newPopulation=[]


        #queremos que el largo de la poblacion sea  el mismo siempre, por lo que vamos
        #agregando nuevos valores a newPopulation hasta que sus valores sean iguales.
        while(len(newPopulation)<len(population)):

            #buscamos indices al azar
            competitors=randIndex(len(population),Ncompetitors)

            #ahora los competidores compiten (calcular su fitness

            fitness=fitnessesI(population,word,competitors)

            # tournament
            max1 = -1
            max2 = -1

            winner1 = 0
            winner2 = 0

            for i in range(len(competitors)):
                if fitness[i] > max1:
                    max1=fitness[i]
                    winner1 = competitors[i]

            for i in range(len(competitors)):
                if competitors[i] != winner1 and fitness[i] > max2:
                    max2=fitness[i]
                    winner2 = competitors[i]

            son = mutateString(crossOverString1(population[winner1], population[winner2]),abc)

            newPopulation.append(son)

        population=newPopulation

        maxfit=-1
        best=0

        F=fitnesses(population,word)


        for i in range(len(F)):
            if F[i]>maxfit:
                maxfit=F[i]
                best=i

            if maxfit==l:
                print("encontrada!")
                print("en iteracion "+str(t))
                return population[i]



    print("best is "+str(population[best]))
    print("with fitness "+str(F[best]))



#find("como un angel cruel y sanginario vamos vuela conviertete en leyenda ahora que el viento esta golpeando la puerta de tu corazon",100,1000,10,wordAbc)

#find("0100101010100100101001000001110101010001",5,20,11,binAbc)









