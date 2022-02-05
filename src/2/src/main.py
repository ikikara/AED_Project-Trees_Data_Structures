import datetime, random
from tree import Arvore, Registo

class Menu:
    def __init__(self):
        self.arv= Arvore()
        self.raiz=None

    def acrescenta(self,registo):
        self.raiz = self.arv.addNo(self.raiz,registo)

    def consulta(self,numero):
        self.arv.procura(self.raiz,numero)
        self.arv.flag=False

    def listagem(self):
        self.arv.printPorOrdem(self.raiz)

    def apaga(self):
        if (self.raiz != None):
            self.raiz = None


if __name__=="__main__":
    menu = Menu()
    linhas=[]

    nums=[]
    vacs=["covid","tuberculose","tetano","astrazeneca","pfizer","hpv","bcg","schrodinger","vacaloka"]

    n = int(input())

    '''
    [First scenery]
    for i in range(int(n * 0.1)):
        num=random.randint(10000,99999)
        nums.append(str(num))
        linhas.append("ACRESCENTA "+str(num)+" "+vacs[random.randint(0,8)]+" "+str(random.randint(10000000,99999999)))

    for i in range(int(n * 0.9)):
        linhas.append("CONSULTA "+str(nums[random.randint(0,len(nums)-1)]
    '''

    #[Second scenery]
    for i in range(int(n * 0.9)):
        num=random.randint(10000,99999)
        nums.append(str(num))
        linhas.append("ACRESCENTA "+str(num)+" "+vacs[random.randint(0,8)]+" "+str(random.randint(10000000,99999999)))

    for i in range(int(n * 0.1)):
        linhas.append("CONSULTA "+str(nums[random.randint(0,len(nums)-1)]))


    start = datetime.datetime.now()
    for linha in linhas:
        chave=linha.split(" ")

        if chave[0]=="ACRESCENTA":
            r=Registo(int(chave[1]))
            r.insereDados(chave[2], int(chave[3]))
            menu.acrescenta(r)
        elif chave[0]=="LISTAGEM":
            menu.listagem()
        elif chave[0]=="CONSULTA":
            menu.consulta(int(chave[1]))
        elif chave[0]=="APAGA":
            menu.apaga()

    print("%.3f milliseconds" % ((datetime.datetime.now() - start).total_seconds() * 1000))

