import random, datetime
from tree import SplayTree, Registo

class Menu:
    def __init__(self):
        self.arv= SplayTree()
        self.raiz=None

    def acrescenta(self,registo):
        self.raiz = self.arv.insert(self.raiz,registo)

    def consulta(self,nome):
        self.raiz=self.arv.procura(self.raiz,nome)

        if(self.arv.flag==False):
            self.raiz.d.nome
            print("CLIENTE NAO REGISTADO")



        self.arv.flag=False

    def aquisicao(self,nome,money):
        self.raiz=self.arv.aquisicao(self.raiz,nome,money)

        if(self.arv.flag==False):
            print("CLIENTE NAO REGISTADO")


        self.arv.flag=False

    def listagem(self):
        self.arv.printPorOrdem(self.raiz)
        print("FIM")

    def apaga(self):
        if (self.raiz != None):
            self.raiz = None

        print("LISTAGEM DE CLIENTES APAGADA")

if __name__ == '__main__':
    menu = Menu()
    linhas = []

    n = int(input())

    #[Second scenery]
    numeros=[str(i+1) for i in range(int(n/4))]

    for i in range(int(n/4)):
        index=random.randint(0,int(n/4)-1-i)
        menu.acrescenta(Registo(numeros[index], "rua aed", 400))
        numeros.remove(numeros[index])

    for i in range(int(n/4)):
        linhas.append("CONSULTA "+str(i+1))
        linhas.append("CONSULTA "+str(i+1))
        linhas.append("CONSULTA "+str(i+1))
        linhas.append("CONSULTA "+str(i+1))

    #print(linhas)

    random.shuffle(linhas)

    #print(linhas)

    '''
    [First scenery]
    nomes=[]

    for i in range(1,int(0.05*n)+1):
        nomes.append(str(i))

    for i in range(int(0.9*n)):
        linhas.append("CONSULTA "+nomes[random.randint(0,len(nomes)-1)])

    for i in range(int(0.1*n)):
        linhas.append("CONSULTA "+str(random.randint(1,n)))
    '''



    '''
    [TO RUN MANUALLY]
    l = input()

    while l!="FIM":
        linhas.append(l)
        l = input()
    '''

    start = datetime.datetime.now()
    for linha in linhas:
        chave = linha.split(" ")

        if chave[0] == "CLIENTE":
            menu.acrescenta(Registo(chave[1],chave[2]+" "+chave[3],int(chave[4])))
        elif chave[0] == "LISTAGEM":
            menu.listagem()
        elif chave[0] == "CONSULTA":
            menu.consulta(Registo(chave[1]))
        elif chave[0] == "AQUISICAO":
            menu.aquisicao(Registo(chave[1]),int(chave[2]))
        elif chave[0] == "APAGA":
            menu.apaga()

    print("%.3f milliseconds" % ((datetime.datetime.now() - start).total_seconds() * 1000))

