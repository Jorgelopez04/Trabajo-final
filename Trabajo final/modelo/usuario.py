import json

class Usuario:
    def __init__(self,nombre:str,DNI:int,telefono:int,correo:str):
        self.nombre:str=nombre
        self.DNI:int=DNI
        self.telefono:int=telefono
        self.correo:str=correo


    @staticmethod
    def toJson(usuario:'Usuario'):
        if isinstance(usuario,Usuario):
            return {
                "nombre": usuario.nombre,
                "DNI":usuario.DNI,
                "telefono":usuario.telefono,
                "correo":usuario.correo



            }
        

    def guardar_usuario_en_json(self):
        with open("registros.json", "w") as archivo:
            json.dump(obj=self, fp=archivo,
                      default=Usuario.toJson)
            








        

   


        


    
    
