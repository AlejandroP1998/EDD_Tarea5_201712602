from Analizadores.nodoT import node

class listaT:
    def __init__(self):
        self.header = None
        self.last = None
    def empty(self):
        if self.header == None:
            return True
        else:
            return False
    
    def insert_header(self,carnet,nombre,descripcion,materia,fecha,hora,estado):
        if self.empty():
            self.header = self.last = node(carnet,nombre,descripcion,materia,fecha,hora,estado)
        else:
            aux = node(carnet,nombre,descripcion,materia,fecha,hora,estado)
            aux.next = self.header
            self.header.prev = aux
            self.header = aux
    def insert_last(self,carnet,nombre,descripcion,materia,fecha,hora,estado):
        if self.empty():
            self.header = self.last = node(carnet,nombre,descripcion,materia,fecha,hora,estado)
        aux = self.last
        self.last = aux.next = node(carnet,nombre,descripcion,materia,fecha,hora,estado)
        self.last.prev = aux
    
    def link_nodes(self):
        if self.header != None:
            self.header.prev = self.last
            self.last.next = self.header
        
    def travel_header_to_last(self):
        aux = self.header
        print('Lista de tareas (Primera a la ultima)')
        while aux:
            print(aux.carnet)
            print(aux.nombre)
            aux = aux.next
            if aux == self.header:
                break
    def travel_last_to_header(self):
        aux = self.last
        print('Lista de tareas \n')
        while aux:
            print(aux.carnet)
            print(aux.nombre)
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
    
    def search(self,carnet):
        aux = self.header
        while aux:
            if aux.carnet == carnet:
                return True
            else:
                aux = aux.next
                if aux == self.header:
                    return False