import tkinter as tk
import json
from tkinter import simpledialog


class InterfazGrafica:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Tienda de alquiler de bicicletas")

        
        self.nombre_label = tk.Label(ventana, text="Nombre:")
        self.nombre_label.pack()

        self.nombre_entry = tk.Entry(ventana)
        self.nombre_entry.pack()

        self.dni_label = tk.Label(ventana, text="DNI:")
        self.dni_label.pack()

        self.dni_entry = tk.Entry(ventana)
        self.dni_entry.pack()

        self.telefono_label = tk.Label(ventana, text="Teléfono:")
        self.telefono_label.pack()

        self.telefono_entry = tk.Entry(ventana)
        self.telefono_entry.pack()

        self.correo_label = tk.Label(ventana, text="Correo:")
        self.correo_label.pack()

        self.correo_entry = tk.Entry(ventana)
        self.correo_entry.pack()

        

       

        self.resultado_label = tk.Label(ventana, text="")
        self.resultado_label.pack()

        self.registrado = False
        self.bicicleta_seleccionada = None
        self.horas_alquiler = None
        self.tarifa_por_hora = 10000  

        
        self.boton_registro = tk.Button(ventana, text="Registrar", command=self.registro)
        self.boton_registro.pack()

       
        self.boton_mostrar_catalogo = tk.Button(ventana, text="Mostrar Catálogo", command=self.mostrar_catalogo, state=tk.DISABLED)
        self.boton_mostrar_catalogo.pack()

       
        self.boton_seleccionar_bicicleta = tk.Button(ventana, text="Seleccionar Bicicleta", command=self.seleccionar_bicicleta, state=tk.DISABLED)
        self.boton_seleccionar_bicicleta.pack()

       
        self.boton_devolver_bicicleta = tk.Button(ventana, text="Devolver Bicicleta", command=self.devolver_bicicleta, state=tk.DISABLED)
        self.boton_devolver_bicicleta.pack()

       
        self.boton_generar_factura = tk.Button(ventana, text="Generar Factura", command=self.generar_factura, state=tk.DISABLED)
        self.boton_generar_factura.pack()

        self.boton_salir = tk.Button(ventana, text="Salir", command=self.salir)
        self.boton_salir.pack()

        
        self.bicicletas = {
            1: "Bicicleta Roja",
            2: "Bicicleta Azul",
            3: "Bicicleta Amarilla",
            4: "Bicicleta Negra",
            5: "Bicicleta Verde",
            6: "Bicicleta Blanca"
        }

    def registro(self):
        nombre = self.nombre_entry.get()
        dni = self.dni_entry.get()
        telefono = self.telefono_entry.get()
        correo = self.correo_entry.get()

        if not nombre or not dni or not telefono or not correo:
            self.resultado_label.config(text="Por favor, complete todos los campos.")
            return

        
        if "@" not in correo:
            self.resultado_label.config(text="El correo no es válido. Debe contener '@'.")
            return

        nuevo_usuario = {
            "nombre": nombre,
            "DNI": dni,
            "telefono": telefono,
            "correo": correo
        }

        usuarios = cargar_usuarios()

        
        for usuario in usuarios:
            if usuario["DNI"] == dni:
                self.resultado_label.config(text="Este DNI ya está registrado. No se puede registrar nuevamente.")
                return

        usuarios.append(nuevo_usuario)
        guardar_usuarios(usuarios)
        self.resultado_label.config(text="Usuario registrado exitosamente.")

        self.registrado = True
        self.boton_mostrar_catalogo.config(state=tk.NORMAL)
        self.boton_seleccionar_bicicleta.config(state=tk.NORMAL)
        self.boton_devolver_bicicleta.config(state=tk.NORMAL)
        self.boton_generar_factura.config(state=tk.NORMAL)

    def mostrar_catalogo(self):
        catalogo = "Catálogo de bicicletas disponibles:\n"
        for num, nombre in self.bicicletas.items():
            catalogo += f"{num}. {nombre}\n"

        catalogo_ventana = tk.Toplevel(self.ventana)
        catalogo_etiqueta = tk.Label(catalogo_ventana, text=catalogo)
        catalogo_etiqueta.pack()

    def seleccionar_bicicleta(self):
        bicicleta_seleccionada = simpledialog.askinteger("Seleccionar Bicicleta", "Por favor, copie el número de la bicicleta:")
        if bicicleta_seleccionada in self.bicicletas:
            horas_alquiler = simpledialog.askinteger("Horas de Alquiler", "Ingrese la cantidad de horas que desea alquilar la bicicleta:")
            if horas_alquiler is not None:
                if horas_alquiler > 0:
                    self.bicicleta_seleccionada = bicicleta_seleccionada
                    self.horas_alquiler = horas_alquiler
                    self.resultado_label.config(text=f"Bicicleta seleccionada: {self.bicicletas.get(bicicleta_seleccionada, 'Desconocida')}, Horas de alquiler: {horas_alquiler}")
                    self.boton_devolver_bicicleta.config(state=tk.NORMAL)
                else:
                    mensaje_ventana = tk.Toplevel(self.ventana)
                    mensaje_label = tk.Label(mensaje_ventana, text="Las horas de alquiler no pueden ser 0 o negativas. Por favor, ingrese un número de horas válido.")
                    mensaje_label.pack()
            else:
                mensaje_ventana = tk.Toplevel(self.ventana)
                mensaje_label = tk.Label(mensaje_ventana, text="Por favor, ingrese un número de horas válido.")
                mensaje_label.pack()

    def devolver_bicicleta(self):
        if not self.registrado:
            mensaje_ventana = tk.Toplevel(self.ventana)
            mensaje_label = tk.Label(mensaje_ventana, text="Antes de devolver una bicicleta, por favor regístrese.")
            mensaje_label.pack()
        elif not self.bicicleta_seleccionada:
            mensaje_ventana = tk.Toplevel(self.ventana)
            mensaje_label = tk.Label(mensaje_ventana, text="Por favor, seleccione una bicicleta del catálogo antes de devolverla.")
            mensaje_label.pack()
        else:
            bicicleta_devuelta = simpledialog.askinteger("Bicicleta a Devolver", "Ingrese el número de la bicicleta que está devolviendo:")
        if bicicleta_devuelta == self.bicicleta_seleccionada:
            nombre_bicicleta = self.bicicletas.get(bicicleta_devuelta, "Desconocida")
            mensaje_ventana = tk.Toplevel(self.ventana)
            mensaje_label = tk.Label(mensaje_ventana, text=f"Ha devuelto la bicicleta: {nombre_bicicleta}.")
            mensaje_label.pack()
        else:
            mensaje_ventana = tk.Toplevel(self.ventana)
            mensaje_label = tk.Label(mensaje_ventana, text="Esta no es la bicicleta que seleccionaste.")
            mensaje_label.pack()
    def generar_factura(self):
        if self.bicicleta_seleccionada is not None and self.horas_alquiler is not None:
            nombre_bicicleta = self.bicicletas.get(self.bicicleta_seleccionada, "Desconocida")
            monto = self.horas_alquiler * self.tarifa_por_hora

            factura = f"Factura:\n"
            factura += f"Factura para {self.nombre_entry.get()}:\n"
            factura += f"La Bicicleta que es escogiste fue : {nombre_bicicleta}\n"
            factura += f"Las Horas de alquiler fueron : {self.horas_alquiler}\n"
            factura += f"Monto que debes pagar es de: ${monto}\n"

            factura_ventana = tk.Toplevel(self.ventana)
            factura_etiqueta = tk.Label(factura_ventana, text=factura)
            factura_etiqueta.pack()
    def salir(self):
        self.ventana.destroy()
def cargar_usuarios():
    try:
        with open("usuarios.json", "r") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

def guardar_usuarios(usuarios):
    with open("usuarios.json", "w") as archivo:
        json.dump(usuarios, archivo)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazGrafica(ventana)
    ventana.mainloop()