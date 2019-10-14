import random

binAbc=['0','1']

def stringToArray(string):
    A=[]
    for s in string:
        A.append(s)
    return A

def arrayToString(A):
    s=""
    for a in A:
        s+=a
    return s

def matchString(s1,s2):
    return matchArray(stringToArray(s1),stringToArray(s2))

def matchArray(A1,A2):
    l=len(A1)
    p=0
    for i in range(l):
       if A1[i]==A2[i]:
           p+=1
    return p

def generateRandomArray(n,abc):
    l=len(abc)
    RA=[]
    for i in range(n):
        RA.append(abc[random.randint(0, l-1)])
    return RA

def generateRandomString(n,abc):
    return arrayToString(generateRandomArray(n,abc))

def crossOverArray(A1,A2):
    l=len(A1)
    gen=random.randint(0,l)
    son=[]

    raux=random.randint(0,1)
    if raux==0:
        for i in range(l):
            if i<=gen:
                son.append(A1[i])
            else:
                son.append(A2[i])
    else:
        for i in range(l):
            if i<=gen:
                son.append(A2[i])
            else:
                son.append(A1[i])

    return son

def crossOverString1(s1,s2):
    return arrayToString(crossOverArray(stringToArray(s1),stringToArray(s2)))


def mutateArray(A,abc):
    i=random.randint(0, len(A) - 1)
    j=random.randint(0,len(abc)-1)
    A[i]=abc[j]
    return A

def mutateString(s1,abc):
    A=stringToArray(s1)
    A=mutateArray(A,abc)
    return arrayToString(A)