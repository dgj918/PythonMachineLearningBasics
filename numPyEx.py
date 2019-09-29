import numpy as np


def printList(L, message="List"):
    print(message, L)

def printNumArr(numArr, message="NumArr"):
    print(message, numArr)

def resetList():
    return [1,2,3]

def resetNumArr():
    return np.array([1,2,3])

def appendToList(L, additions):
    L.append(additions)
    return L

def addListToList(L1, L2):
    return L1 + L2

def mulList(L1, L2):
    return L1 * L2

def squareList(L1):
    sqL = []

    for e in L1:
        sqL.append(e*e)
    
    return sqL

def numArrAdd(A1, A2):
    return A1 + A2

def numArrMul(A1, A2):
    return A1 * A2

def numArrSq(A):
    return A**2

def numArrSqrt(A):
    return np.sqrt(A)

def numArrLog(A):
    return np.log(A)

def numExp(A):
    return np.exp(A)

def numArrSumOfMul(a,b):
    return np.sum(a*b)

L = [1,2,3]
A = np.array([1,2,3])
LAdd = [4,5,6]
addL = 4
vect = 3

printList(L)
printNumArr(A)

L2 = appendToList(L,addL)
printList(L2, "List Append")
L = resetList()

L3 = mulList(L, addL)
printList(L3, "List Multiply by %s" %(addL))
L = resetList()

L4 = addListToList(L, LAdd)
printList(L4, "List Added to %s" %(LAdd))
L = resetList()

Aadd = numArrAdd(A, A)
printNumArr(Aadd, "NumArr Add")
A = resetNumArr()

Amul = numArrMul(A, vect)
printNumArr(Amul, "NumArr Multiply")
A = resetNumArr()

Asq = numArrSq(A)
printNumArr(Asq, "NumArr Squared")
A = resetNumArr()

Asqrt = numArrSqrt(A)
printNumArr(Asqrt, "Square root NumArr")
A = resetNumArr()

Alog = numArrLog(A)
printNumArr(Alog, "Log NumArr")
A = resetNumArr()

AsqLog = numArrSqrt(numArrSq(A))
printNumArr(AsqLog, "Sq then Sqrt NumArr")
A = resetNumArr()

Aexp = numExp(A)
printNumArr(Aexp, "NumArr Exp")
A = resetNumArr()
