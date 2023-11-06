from modelo.Excepcion import UsuarioError
from modelo.usuario import Usuario

class correo_no_valido(Exception):

    def __init__(self,usuario:Usuario):
        self.usuario=usuario



    
