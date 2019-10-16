import random


class knapsack:
    def __init__(self, V, W,maxW):
        self.V = V
        self.W = W
        self.maxW=maxW
        self.K = []
        for i in range(len(W)):
            self.K.append(random.randint(0, 1))

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


    def autoPunishment2(self,value):
        return value/2

    def summary(self):
        print("V="+str(self.V))
        print("W="+str(self.W))
        print("K=" + str(self.K))
        print("fitness: " + str(self.fitness()))
        print("value: "+str(self.getActualValue()))
        print("weight: "+str(self.getActualWeight()))

    def getActualValue(self):
        v=0
        for i in range(len((self.K))):
            if self.K[i]==1:
                v+=self.V[i]
        return v

    def getActualWeight(self):
        w=0
        for i in range(len((self.K))):
            if self.K[i]==1:
                w+=self.W[i]
        return w

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