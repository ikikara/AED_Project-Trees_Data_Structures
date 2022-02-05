class NoArvore():
    def __init__(self, d, l=None, r=None):
        self.d = d
        self.l = l
        self.r = r


class SplayTree():
    def __init__(self):
        self.flag=False

    def insert(self, no, val):
        if no == None:
            #print("NOVO CLIENTE INSERIDO")
            return NoArvore(val)


        else:
            no = self.splay(no, val)
            self.flag=False
            if no.d.nome==val.nome:
                print("CLIENTE JA EXISTENTE")
                return no

            new = NoArvore(val)
            if no.d.nome > val.nome:
                new.r = no
                new.l = no.l
                no.l = None

            elif no.d.nome < val.nome:
                new.l = no
                new.r = no.r
                no.r = None

            #print("NOVO CLIENTE INSERIDO")
            return new

    def rodarL(self, s):
        t = s.r
        NoInfR = t.l

        t.l = s
        s.r = NoInfR

        return t


    def rodarR(self, u):
        t = u.l
        NoInfL = t.r

        t.r = u
        u.l = NoInfL

        return t



    def splay(self, no, val):
        if no == None or no.d.nome == val.nome:
            return no

        if no.d.nome > val.nome:
            if no.l == None:
                return no

            if no.l.d.nome > val.nome:
                no.l.l = self.splay(no.l.l, val)
                no = self.rodarR(no)

            elif no.l.d.nome < val.nome:
                no.l.r = self.splay(no.l.r, val)

                if no.l.r!=None:
                    no.l = self.rodarL(no.l)


            if no.l == None:
                return no
            else:
                return self.rodarR(no)

        else:
            if no.r == None:
                return no

            if no.r.d.nome > val.nome:
                no.r.l = self.splay(no.r.l, val)

                if no.r.l!=None:
                    no.r = self.rodarR(no.r)

            elif no.r.d.nome < val.nome:
                no.r.r = self.splay(no.r.r, val)
                no = self.rodarL(no)

            if no.r == None:
                return no
            else:
                return self.rodarL(no)

    def procura(self, no, val):
        if (no != None):
            if (no.d.nome > val.nome):
                self.procura(no.l, val)
            elif (no.d.nome < val.nome):
                self.procura(no.r, val)
            elif (no.d.nome == val.nome):
                self.flag = True
                '''print(no.d)
                print("FIM")'''
                return self.splay(no,no.d)
        return no


    def aquisicao(self, no, val,money):
        if (no != None):
            if (no.d.nome > val.nome):
                self.aquisicao(no.l, val, money)
            elif (no.d.nome < val.nome):
                self.aquisicao(no.r, val, money)
            elif (no.d.nome == val.nome):
                self.flag = True
                no.d.volume+=money
                print("AQUISICAO INSERIDA")
                return self.splay(no, no.d)
        return no

    def printPorOrdem(self, no):
        if (no != None):
            self.printPorOrdem(no.l)
            print(no.d)
            self.printPorOrdem(no.r)

class Registo:
    def __init__(self, nome, morada=None, volume=None):
        self.nome = nome
        self.morada=morada
        self.volume=volume

    def __str__(self):
        return self.nome+" "+self.morada+" "+str(self.volume)