#TALLER 02 #Trabajamos... juan jose lozano tovar , mauricio mora , kenet josep , alejandra leython , samuel tamara,juan panadero
class persona (): #se define clase
    def __init__(self,Hermanos,Padres,nombre):
        self.nombre=nombre #nombre
        self.Hermanos =Hermanos.split()# hermanos de la persona (n datos)
        self.Padres=Padres.split() # padres de la persona (2 datos o menos)
        self.bro=str(self.Hermanos)
        self.father=str(self.Padres)


    def add_siblings (self,sib):  
        self.Hermanos.append(sib)
        self.Hermanos.append(sib)
        print(sib)

    def add_parents (self,Padres):
        if len(self.Padres) < 2:
            self.Padres.append(Padres)
        else:
            print('No se puede meter')



    def search (self,nombre):
        art2=nombre.split()
        key=[]
        for i in art2:
            k=i.lower()
            key.append(k)
        self.n=key
        for j in key:
            bareto=j.capitalize()
            self.n=bareto
        H=0
        if self.nombre==self.n:
            return (self.n,"esta en la altura",H)
        for tre in self.Hermanos:
            if tre==self.n:
                H+=2
                return (self.n,"esta en la altura",H)

        for albareto in self.Padres:
            if albareto==self.n:
                H+=1
                return (self.n,"esta en la altura",H)



    def tr2_list (self):
        L=[]
        T=self
        T.Hermanos=[]
        T.Padres=[]
        L.append(T)
        L.append(self.Hermanos)
        LPO=self.tr2_list(self.Padres[0])
        LP1=self.tr2_list(self.Padres[0])
        L.append(LPO)
        L.append(LP1)
        return L

    def encript(self,nombre):
        self.nombrsearch=nombre
        loli=self.nombrsearch+'.txt'
        print(loli)
        with open(loli,'a') as file:
            file.write('\n'+self.nombre)
            file.write('\n'+self.bro)
            file.write('\n'+self.father)

    def decrip(self,nombre):
        self.nombrsearch=nombre
        loli=self.nombrearch+'.txt'
        archivo=open(loli,'rt',encoding='utf-8')
        print(archivo.read())
        return('Arbol created')

gustav = persona("Hermanos","Padres","nombre")
gustav.add_siblings("juan")
gustav.add_siblings("pablo")
gustav.add_siblings("pedro")
gustav.add_siblings("jose")
gustav.add_parents("jaime")
gustav.add_parents("luisa")
juan = persona("Hermanos","Padres","nombre")
gustav.search("juan")
print(gustav.Hermanos,gustav.Padres)



