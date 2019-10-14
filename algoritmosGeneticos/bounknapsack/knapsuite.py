import random


def generateRandomknapsack(W):
    knapsack=[]
    for i in range(len(W)):
        knapsack.append(random.randint(0,1))
    return knapsack


def knapsackFit(V,W,maxW):
    pass

a=generateRandomknapsack([4,1,2])

print(generateRandomknapsack(a))
