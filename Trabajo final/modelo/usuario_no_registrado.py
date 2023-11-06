from modelo.Excepcion import UsuarioError
from modelo.usuario import Usuario
class UsuarioNoRegistrado(UsuarioError):

    def __init__(self,usuario:Usuario):
        super().__init__(usuario)


    def __str__(self):
        return "Debes registrarte antes de poder realizar otra opcion"

