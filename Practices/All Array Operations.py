def Traversing(LA,N):
    K = 0
    print("The Linear array is:",end= " ")
    while K < N:
        print(LA[K], end =" ")
        K = K + 1
    print("\n")

def Insertion(LA,N,ITEM,K):
    LA.append(None)
    J = N
    while J>=K:
        LA[J] = LA[J-1]
        J = J - 1
    LA [K] = ITEM
    N = N + 1
    res = print("The list after insertion is- ",LA,"\n")
    return res

def Deletion(LA,N,ITEM,K):
    J = K
    while J < N -1:
        LA [J] = LA[J + 1]
        J = J + 1
    LA.pop()
    N = N - 1
    res = print("The list after Deletion- ",LA,"\n")
    return res

def LINERSEARCH(LA,ITEM,N):
    LOC = 1
    while LOC <= N:
        if ITEM == LA[LOC]:
            print("Item is found at LOC- ", LOC,"\n")
            break
        LOC = LOC + 1

def BinarySearch(LA,ITEM,N):
    BEG = 0
    END = N - 1 
    while BEG <= END:
        MID = int((BEG+END)/2)
        if ITEM == LA[MID]:
            print("Item found at location- ",MID,"\n")
            break
        elif ITEM < LA[MID]:
            END = MID - 1
        else:
            BEG = MID + 1
    if BEG > END:
        print("Item is not found!")


LA = [10,20,30,40,50,60,70,80,90,100]
N = len(LA)
ITEM = 50
K = 2
Traversing(LA,N)
Insertion(LA,N,ITEM,K)
Deletion(LA,N,ITEM,K)
LINERSEARCH(LA,ITEM,N)
BinarySearch(LA,ITEM,N)
