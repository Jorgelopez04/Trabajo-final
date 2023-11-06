from modelo.usuario import Usuario


class UsuarioError(Exception):
    def __init__(self,usuario:Usuario):
        self.usuario= usuario
