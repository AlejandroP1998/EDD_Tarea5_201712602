class node:
    def __init__(self,carnet,dpi,nombre,carrera,password,creditos,edad):
        self.carnet = carnet
        self.dpi = dpi
        self.nombre = nombre
        self.carrera = carrera
        self.password = password
        self.creditos = creditos
        self.edad = edad
        self.next = None
        self.prev = None
