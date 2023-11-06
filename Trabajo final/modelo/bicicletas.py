from modelo.alquiler import alquilar



class bicicleta:
    def __init__(self):
        self.alquiler=alquilar()

    def seleccionar(self,seleccion:int):
        if seleccion in self.alquiler.catalogo :
            bicicleta_alquilada=self.alquiler.catalogo.pop(seleccion)
            self.alquiler.bicicletas_en_uso[seleccion]=bicicleta_alquilada
            print(f"La bicicleta que escogiste fue: {bicicleta_alquilada}")
        else:
            print("La bicicleta no esta en el catalogo")
    
    
        

    def delvolver_bicicleta(self,devolver:int):
        if devolver in self.alquiler.bicicletas_en_uso:
            bicicleta_a_devolver=self.alquiler.bicicletas_en_uso.pop(devolver)
            self.alquiler.catalogo[devolver]=bicicleta_a_devolver
            print(f"La bicicleta que devolviste fue {bicicleta_a_devolver}")
        else:
            print("La bicicleta seleccionada no estaba alquilada")