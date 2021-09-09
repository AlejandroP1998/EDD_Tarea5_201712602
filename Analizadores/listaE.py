from Analizadores.nodoE import node

class listaE:
    def __init__(self):
        self.header = None
        self.last = None
    def empty(self):
        if self.header == None:
            return True
        else:
            return False
    
    def insert_header(self,carnet,dpi,nombre,carrera,password,creditos,edad):
        if self.empty():
            self.header = self.last = node(carnet,dpi,nombre,carrera,password,creditos,edad)
        else:
            aux = node(carnet,dpi,nombre,carrera,password,creditos,edad)
            aux.next = self.header
            self.header.prev = aux
            self.header = aux
    def insert_last(self,carnet,dpi,nombre,carrera,password,creditos,edad):
        if self.empty():
            self.header = self.last = node(carnet,dpi,nombre,carrera,password,creditos,edad)
        aux = self.last
        self.last = aux.next = node(carnet,dpi,nombre,carrera,password,creditos,edad)
        self.last.prev = aux
    
    def link_nodes(self):
        if self.header != None:
            self.header.prev = self.last
            self.last.next = self.header
        
    def travel_header_to_last(self):
        aux = self.header
        print('Lista de estudiantes (Primero al ultimo)')
        while aux:
            print(aux.nombre)
            print(aux.dpi)
            aux = aux.next
            if aux == self.header:
                break
    def travel_last_to_header(self):
        aux = self.last
        print('Lista de estudiantes \n')
        while aux:
            print(aux.nombre)
            print(aux.dpi)
            aux = aux.prev
            if aux == self.last:
                break
        print('\n')
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
    
    def search(self,dpi):
        aux = self.header
        while aux:
            if aux.dpi == dpi:
                return True
            else:
                aux = aux.next
                if aux == self.header:
                    return False