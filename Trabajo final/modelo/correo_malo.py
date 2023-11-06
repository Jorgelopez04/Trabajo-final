from modelo.correo import correo_no_valido
from modelo.usuario import Usuario

class correoMalo(correo_no_valido):
    def __init__(self,usuario:Usuario):
        super().__init__(usuario)
        
    def __str__(self):
        
            if "@" in self.usuario.correo:
                return "Su correo es valido"
            
            else:
                return "Su correo es invalido"