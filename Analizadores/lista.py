from Analizadores.nodo import node
from Analizadores.listaE import listaE
from Analizadores.listaT import listaT

le = listaE()
lt = listaT()
cont = 0
es = False
ta = False
e = []
t = []
class lista:

    def __init__(self):
        self.header = None
        self.last = None
    def empty(self):
        if self.header == None:
            return True
        else:
            return False
    def insert_header(self,dato):
        if self.empty():
            self.header = self.last = node(dato)
        else:
            aux = node(dato)
            aux.next = self.header
            self.header.prev = aux
            self.header = aux
    def insert_last(self,dato):
        if self.empty():
            self.header = self.last = node(dato)
        aux = self.last
        self.last = aux.next = node(dato)
        self.last.prev = aux
    
    def link_nodes(self):
        if self.header != None:
            self.header.prev = self.last
            self.last.next = self.header
        
    def travel_header_to_last(self):
        print('lista\n')

        aux = self.header
        while aux:
            print(aux.dato)
            aux = aux.next
            if aux == self.header:
                break
    def travel_last_to_header(self):
        print('lista\n')
        aux = self.last
        while aux:
            print(aux.dato)
            aux = aux.prev
            if aux == self.last:
                break
    def delete_header(self):
        if self.empty:
            print('No hay elementos en la lista')
        elif self.header == self.last:
            self.header = self.last = None
        else:
            self.header = self.header.next
        self.link_nodes()
    
    def delete_last(self):
        if self.empty:
            print('No hay elementos en la lista')
        elif self.header == self.last:
            self.header = self.last = None
        else:
            self.last = self.last.prev
        self.link_nodes()
    
    def search(self,dato):
        aux = self.header
        while aux:
            if aux.dato == dato:
                return True
            else:
                aux = aux.next
                if aux == self.header:
                    return False
    
    
    
    
    
    
    
    
    
    
    
    
    
    def distribucion(self):
        aux = self.last
        while aux:
            global es
            global ta
            global cont
            global e
            global t
            if aux.dato == '"user"' and cont>0 and es == True:
                #print('entro al user cont')
                le.insert_last(e[0],e[1],e[2],e[3],e[4],e[5],e[6])
                es = True
                ta = False
                e = []
            if aux.dato == '"user"' and cont>0 and es == False:
                #print('entro al user cont')
                lt.insert_last(t[0],t[1],t[2],t[3],t[4],t[5],t[6])
                es = True
                ta = False
                e = []
            if aux.dato == '"task"' and cont>0 and ta == True:
                #print('entro al task cont')
                lt.insert_last(t[0],t[1],t[2],t[3],t[4],t[5],t[6])
                es = False
                ta = True
                t = []
            if aux.dato == '"task"' and cont>0 and ta == False:
                #print('entro al task cont')
                le.insert_last(e[0],e[1],e[2],e[3],e[4],e[5],e[6])
                es = False
                ta = True
                t = []
            if aux.dato == '"user"'and cont == 0:
                #print('entro al user')
                cont += 1
                es = True
                ta = False
                e = []
            elif aux.dato == '"task"' and cont == 0:
                #print('entro al task')
                cont += 1
                ta = True
                es = False
                t = []
            
            if es == True and aux.dato != '"user"' :
                #print('añadiendo e')
                e.append(str(aux.dato))
            elif ta == True and aux.dato != '"task"':
                #print('añadiendo t')
                t.append(str(aux.dato))
            aux = aux.prev
            if aux == self.last:
                break
        le.travel_last_to_header()
        lt.travel_last_to_header()
