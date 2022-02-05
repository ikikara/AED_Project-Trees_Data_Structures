import math
import datetime, random


def hashtree(elemts):
    n = (int)(math.log2(len(elemts)))
    arvore=[]
    arvore.append([hashcode(i) for i in elemts])

    for i in range(n):
        arvore.append([ hashcode(arvore[i][j],arvore[i][j+1]) for j in range(0,len(arvore[i]),2)])

    return arvore


def printhashtree(arvore):
    for i in reversed(arvore):
        for j in i:
            print(j)


def hashcode(x,y=None):
    mod= 1000000007
    if(y!=None):
        return ((x % mod) + (y % mod)) % mod
    else:
        return x % mod

if __name__=="__main__":
    n = int(input())
    '''
    [TO RUN MANUALY]
    linhas = input()
    dados=[ (int)(elem) for elem in linhas.split(" ")]
    (if you use this, comment the next line)
    '''
    dados=[random.randint(0,999999999999) for i in range(2**n)]

    print()
    start = datetime.datetime.now()
    printhashtree(hashtree(dados))

    print()
    print( "%.3f milliseconds" % ((datetime.datetime.now()-start).total_seconds()*1000))