def AND (a, b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0

def NAND (a, b):
    if a == 1 and b == 1:
        return 0
    else:
        return 1


def OR(a, b):
    if a == 1 or b ==1:
        return 1
    else:
        return 0

def NOR(a, b):
    if(a == 0) and (b == 0):
        return 1
    elif(a == 0) and (b == 1):
        return 0
    elif(a == 1) and (b == 0):
        return 0
    elif(a == 1) and (b == 1):
        return 0

def XOR (a, b):
    if a != b:
        return 1
    else:
        return 0

def XNOR(a,b):
    if(a == b):
        return 1
    else:
        return 0

def NOT(a):
    return not a


A = [0,0,1,1]
B = [0,1,0,1]
for i in range(len(A)):
    result = OR(AND(A[i], B[i]), NOT(A[i]))
    
    if result == 1:
        print(f'{A[i]}|{B[i]} -> {1} ({True})')
    else:
        print(f'{A[i]}|{B[i]} -> {0} ({False})')





