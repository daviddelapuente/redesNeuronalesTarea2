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
        value = sum(self.V)
        weights = sum(self.W)
        if weights <= self.maxW:
            return value
        else:
            # si la mochila exede el peso, se castiga.
            return value - self.autoPunishment(weights, self.maxW)

    # funcion de castigo (puede cambiar para experimentar)
    # si una mochila se pasa del peso, se le resta la diferencia a su valor.
    def autoPunishment(self,w, maxW):
        return w - maxW

    def summary(self):
        print("V="+str(self.V))
        print("W="+str(self.W))
        print("K=" + str(self.K))
        print("fitness " + str(self.fitness()))

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