import sys 
from  modelo.usuario import Usuario
from modelo.alquiler import alquilar
from modelo.correo_malo import correoMalo
from modelo.usuario_no_registrado import UsuarioNoRegistrado
from modelo.bicicletas import bicicleta
from modelo.pago import pago
class UIConsola:

    def __init__(self):
        self.alquiler = alquilar()
        self.opciones = {
            "1": self.registro,
            "2": self.mostrar_catalogo,
            "3": self.seleccionar_bicicleta,
            "4": self.devolver_la_bicicleta,
            "5": self.monto_a_pagar,
            "6": self.visualizacion_monto,
            "7": self.cargar_usuario,
            "8": self.salir
        }
        self.perfil = None
        self.bicicleta=bicicleta()
        self.pago=pago()
        

    def registro(self):
        while True:
            try:
                nombre = input("Ingrese su nombre: ")
                DNI = int(input("Ingrese su DNI: "))
                telefono = int(input("Ingrese su número de teléfono: "))
                correo = input("Ingrese su correo: ")

                if "@" not in correo:
                    raise correoMalo(Usuario(nombre, DNI, telefono, correo))

                self.perfil = Usuario(nombre, DNI, telefono, correo)
                print("Has sido registrado exitosamente")
            except correoMalo as err:
                print(err)
            break

    def cargar_usuario(self):
        self.perfil.guardar_usuario_en_json()

    def mostrar_catalogo(self):
        if not self.perfil:
            raise UsuarioNoRegistrado(self.perfil)
        self.alquiler.mostrar_catalogo()

    def seleccionar_bicicleta(self):
        if not self.perfil:
            raise UsuarioNoRegistrado(self.perfil)

        self.seleccion = int(input("Ingrese la bicicleta que desea escoger: "))
        self.bicicleta.seleccionar(self.seleccion)
        self.tiempo = int(input("Ingrese las horas que desea alquilar la bicicleta: "))

    def devolver_la_bicicleta(self):
        if not self.perfil:
            raise UsuarioNoRegistrado(self.perfil)
        devolver = int(input("Ingrese la bicicleta que va a devolver: "))
        self.bicicleta.delvolver_bicicleta(devolver)

    def monto_a_pagar(self):
        if not self.perfil:
            raise UsuarioNoRegistrado(self.perfil)
        self.pago.monto(self.tiempo)
        self.monto = self.pago.monto
        print("El monto ha sido calculado exitosamente")

    def visualizacion_monto(self):
        if not self.perfil:
            raise UsuarioNoRegistrado(self.perfil)
        self.bicicleta.seleccionar(self.seleccion)
        monto = self.pago.visualizar(self.tiempo)
        print(f"El tiempo que usted alquiló la bicicleta fue de {self.tiempo} horas")
        print(f"El monto que debes pagar por el uso de la bicicleta es de: {monto}")

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE BICICLETAS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def presentar_menu():
        titulo = "Tienda de alquiler de bicicletas"
        print(f"\n{titulo:_^30}")
        print("1. Registrate")
        print("2. Mostrar catálogo")
        print("3. Seleccionar una bicicleta del catálogo")
        print("4. Devolver bicicleta")
        print("5. Calcular monto a pagar")
        print("6. Visualizar monto a pagar")
        print("7. Cargar usuario")
        print("8. Salir")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.presentar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")


