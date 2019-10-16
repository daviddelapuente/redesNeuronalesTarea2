import random


class knapsack:
    #un knapsack tiene un arreglo de values, arreglo de pesos y un peso maximo
    def __init__(self, V, W,maxW):
        self.V = V
        self.W = W
        self.maxW=maxW

        #K es una mascara de bits que representa que articulos van en la mochila
        self.K = []
        for i in range(len(W)):
            self.K.append(random.randint(0, 1))

    #getters
    def getV(self):
        return self.V

    def getW(self):
        return self.W

    def getK(self):
        return self.K

    def setK(self,K):
        self.K=K

    def getMaxW(self):
        return self.maxW


    #fitness
    def fitness(self):
        value = self.getActualValue()
        weights = self.getActualWeight()
        if weights <= self.maxW:
            return value
        else:
            # si la mochila exede el peso, se castiga.
            #return self.autoPunishment1(weights,value)
            return self.autoPunishment2(value)

    # funcion de castigo (puede cambiar para experimentar)
    # si una mochila se pasa del peso, se le resta la diferencia a su valor.
    def autoPunishment1(self,w,value):
        return value - w + self.maxW

    #esta funcion dió mejores resultados, si un valor se pasa entonces se le castiga
    #dividiendo su value por la mitad
    def autoPunishment2(self,value):
        return value/2

    #imprime todo
    def summary(self):
        print("V="+str(self.V))
        print("W="+str(self.W))
        print("K=" + str(self.K))
        print("fitness: " + str(self.fitness()))
        print("value: "+str(self.getActualValue()))
        print("weight: "+str(self.getActualWeight()))


    #valor actual segun la mascara de bits
    def getActualValue(self):
        v=0
        for i in range(len((self.K))):
            if self.K[i]==1:
                v+=self.V[i]
        return v
    #peso actual segun la mascara de bits
    def getActualWeight(self):
        w=0
        for i in range(len((self.K))):
            if self.K[i]==1:
                w+=self.W[i]
        return w


    #mutacion, cambia un valor al azar de k por su reciproco
    def mutate(self):
        l=len(self.K)
        i=random.randint(0, l-1)
        self.K[i]=abs(self.K[i]-1)


#cross over entre 2 knapsacks, devuelve un knapsac
#basicamente lo que hace es elegir un valor random entre 0 y el largo de K
#luego divide ambos knapsack y concatena 2 de estas partes.
def knapCrossOver(k1,k2):

    A1=k1.getK()
    A2=k2.getK()

    l = len(A1)
    gen = random.randint(0, l)
    k = []

    raux = random.randint(0, 1)
    if raux == 0:
        for i in range(l):
            if i <= gen:
                k.append(A1[i])
            else:
                k.append(A2[i])
    else:
        for i in range(l):
            if i <= gen:
                k.append(A2[i])
            else:
                k.append(A1[i])

    kson=knapsack(k1.getV(),k1.getW(),k1.getMaxW())
    kson.setK(k)
    return kson