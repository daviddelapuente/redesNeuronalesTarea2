import random

#transforma un string en un array
def stringToArray(string):
    A=[]
    for s in string:
        A.append(s)
    return A
#transforma array en string
def arrayToString(A):
    s=""
    for a in A:
        s+=a
    return s

#calcula cuantos valores matchean entre 2 strings
def matchString(s1,s2):
    return matchArray(stringToArray(s1),stringToArray(s2))

#suma 1 por cada valor de los array que matchean
def matchArray(A1,A2):
    l=len(A1)
    p=0
    for i in range(l):
       if A1[i]==A2[i]:
           p+=1
    return p

#crea un array al azar de largo n segun el abecedario que se le pasa
def generateRandomArray(n,abc):
    l=len(abc)
    RA=[]
    for i in range(n):
        RA.append(abc[random.randint(0, l-1)])
    return RA

#crea un string al azar de largo n segun el abecedario que se le pasa
def generateRandomString(n,abc):
    return arrayToString(generateRandomArray(n,abc))

#basicamente lo que hace es elegir un indice al azar entre 0 y el largo de A1
# luego divide los array en 2 segun ese indice y concatena las partes
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

#transforma los strings a array y hace corssover de arrays
def crossOverString1(s1,s2):
    return arrayToString(crossOverArray(stringToArray(s1),stringToArray(s2)))

#elige un valor al azar del array y lo cambia por un valor al azar del abecedario
def mutateArray(A,abc):
    i=random.randint(0, len(A) - 1)
    j=random.randint(0,len(abc)-1)
    A[i]=abc[j]
    return A

#elige un valor al azar del string y lo cambia por un valor al azar del abecedario
def mutateString(s1,abc):
    A=stringToArray(s1)
    A=mutateArray(A,abc)
    return arrayToString(A)