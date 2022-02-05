class NoArvore:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.d = val
        self.h = 1


class Arvore:
    def __init__(self):
        self.flag = False

    def addNo(self, no, val):
        if no == None:
            #print("NOVO UTENTE CRIADO")
            return NoArvore(val)
        else:
            if val.numero < no.d.numero:
                no.l = self.addNo(no.l, val)

            elif (val.numero == no.d.numero):
                if (val.vacina[0] not in no.d.vacina):
                    no.d.insereDados(val.vacina[0], val.data[0])
                    #print("NOVA VACINA INSERIDA")
                else:
                    a = no.d.vacina.index(val.vacina[0])
                    no.d.data[a] = val.data[0]
                    #print("VACINA ATUALIZADA")

            elif val.numero > no.d.numero:
                no.r = self.addNo(no.r, val)

        no.h = 1 + max(self.getH(no.l), self.getH(no.r))

        equilibrio = self.getH(no.l) - self.getH(no.r)

        if equilibrio > 1:
            if val.numero > no.l.d.numero:
                no.l = self.rodarL(no.l)
            return self.rodarR(no)
        elif equilibrio < -1:
            if val.numero < no.r.d.numero:
                no.r = self.rodarR(no.r)
            return self.rodarL(no)
        else:
            return no



    def getH(self, no):
        if not no:
            return 0
        return no.h

    def rodarL(self, s):
        t = s.r
        NoInfR = t.l

        t.l = s
        s.r = NoInfR

        s.h = 1 + max(self.getH(s.l), self.getH(s.r))
        t.h = 1 + max(self.getH(t.l), self.getH(t.r))

        return t

    def rodarR(self, u):
        t = u.l
        NoInfL = t.r

        t.r = u
        u.l = NoInfL

        u.h = 1 + max(self.getH(u.l), self.getH(u.r))
        t.h = 1 + max(self.getH(t.l), self.getH(t.r))

        return t

    def procura(self, no, val):
        if (no != None):
            if (no.d.numero > val):
                self.procura(no.l, val)
            elif (no.d.numero < val):
                self.procura(no.r, val)
            elif (no.d.numero == val):
                self.flag = True
                #print(no.d)
                #print("FIM")

    def printPorOrdem(self, no):
        if (no != None):
            self.printPorOrdem(no.l)
            #print(no.d)
            self.printPorOrdem(no.r)


class Registo:
    def __init__(self, numero=None):
        self.numero = numero
        self.vacina=[]
        self.data=[]

    def insereDados(self, vacina, data):
        self.vacina.append(vacina)
        self.data.append(data)
        self.vacina, self.data = (list(t) for t in zip(*sorted(zip(self.vacina, self.data))))

    def __str__(self):
        word = str(self.numero) + " "
        for (v, d) in zip(self.vacina, self.data):
            word += v + " " + str(d) + " "

        return word[:-1]



