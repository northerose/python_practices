"""Realizar una clase que administre una agenda. Se debe almacenar para cada contacto 
el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones:

    Añadir contacto
    Lista de contactos
    Buscar contacto
    Editar contacto
    Cerrar agenda"""

import string


class Agenda:
    def __init__(self):
        self.contacto = [
                        {"nombre": "rose", "telefono": 1234567890, "email": "roselin@gmail.com"},
                        {"nombre": "yuki", "telefono": 1122334455, "email": "yuki@gmail.com"},
                        {"nombre": "lin", "telefono": 6677889900, "email": "lin@gmail.com"}
                        ]
        self.opcion = 0 

    def menu_opciones(self):
        print ("""      Menú de Opciones:\n
                    1.- Añadir contacto
                    2.- Ver lista de contactos
                    3.- Buscar contacto
                    4.- Editar contacto
                    5.- Eliminar contacto
                    6.- Salir""")
        opcion = input("Introduce la opción deseada: ")
        try:
            opcion = int(opcion)
        except:
            print ("Opcion no válida, por favor vuelve a intentarlo")
            self.menu_opciones()
            # raise 
        if opcion == 1:
            self.registrar_contacto()
        elif opcion == 2:
            self.ver_lista()
        elif opcion == 3:
            self.buscar_contacto()
        elif opcion == 4:
            self.editar_contacto()
        elif opcion == 5:
            self.eliminar_contacto()
        elif opcion == 6:
            self.salir()
        elif opcion > 6:
            print ("Opcion no válida, por favor vuelve a intentarlo")
        self.menu_opciones()

    def entrada_datos(self):
        nombre = input("Introduce el nombre: ")
        telefono = input("Introduce el número de teléfono: ")
        email = input("Introduce el email: ")
        errores = self.validaciones(nombre, telefono, email)
        if errores:
            print (errores)
            self.menu_opciones()
        return nombre, telefono, email
      
    def validar_nombre(self, nombre):
        chars = string.punctuation
        numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for element in nombre:
            if element in chars or element in numeros:
                raise ValueError("NameError, El nombre solo debe contener letras")

    def validar_telefono(self, telefono):    
        try:
            telefono == int(telefono)
        except:
            raise ValueError ("El teléfono solamente debe estar conformado por números")
    
    def validar_email(self, email):
        contador_arroba = 0
        contador_punto = 0
        for element in email:
            if element == "@" or element == ".":
                contador_arroba = contador_arroba + 1
                contador_punto = contador_punto + 1
        
        if contador_arroba == 0 or contador_punto == 0:
            raise ValueError ("El formato email no es válido")

    def validaciones(self, nombre, telefono, email):
        errores = []
        try:
            self.validar_nombre(nombre)
        except Exception as error:
            errores.append(error)
        try:
            self.validar_telefono(telefono)
        except Exception as error:
            errores.append(error)
        try:
            self.validar_email(email)
        except Exception as error:
            errores.append(error)
        return errores
        
    def anadir_contacto(self, nombre, telefono, email):
        self.contacto.append({"nombre": nombre, "telefono": telefono, "email": email})
        
    def registrar_contacto(self):
        nombre, telefono, email = self.entrada_datos()
        for element in self.contacto:
            if nombre in element.values():
                sobrescribir = input("El contacto ya se encuentra agendado, ¿lo desea sobrescribir?: ")
                if sobrescribir == "si":
                    self.contacto.remove(element)
                    self.anadir_contacto(nombre, telefono, email)
                    self.ver_lista()
                    break
                elif sobrescribir == "no":
                    print ("Recuerde que el nombre de contacto se duplicará, posteriormente lo podrá editar")
                    self.anadir_contacto(nombre, telefono, email)
                    self.ver_lista()
                    break
        else:
            self.anadir_contacto(nombre, telefono, email)
            self.ver_lista()
            self.menu_opciones()
        
    def ver_lista(self):
        for element in self.contacto:
            print (f"\t {element['nombre']},\t {element['telefono']}, \t {element['email']}")
        self.menu_opciones()
    
    def buscar_contacto(self):
        resultados = []
        buscar = input("Introduce el nombre del contacto: ")
        for element in self.contacto:
            if buscar == element['nombre']:
                resultados.append(element)
        if resultados:
            print (f"Contacto Encontrado {resultados}")
        else:
            print ("El contacto no se encuentra agendado, por favor vuelva a intentarlo")
        self.menu_opciones()
       
    def editar_contacto(self):
        editar = input("Introduce el nombre del contacto: ")
        for element in self.contacto:
            if editar == element['nombre']:
                self.contacto.remove(element)
                print ("A continuación introduzca los nuevos datos del contacto")
                nombre, telefono, email = self.entrada_datos()
                self.anadir_contacto(nombre, telefono, email)
        else:
             print ("El contacto no se encuentra agendado, por favor vuelva a intentarlo")
        self.ver_lista()
        self.menu_opciones()	
		
    def eliminar_contacto(self):
        nombre = input("Por favor introduzca el contacto que desea eliminar: ")
        for element in self.contacto:
            if nombre in element.values():
                eliminar = input(f"Desea eliminar el siguiente contacto {element}: ")
                if eliminar == "si" or eliminar == "sí":
                    self.contacto.remove(element)
                    self.ver_lista()
                    break
                if eliminar == "no":
                    self.menu_opciones()
        else:
            print ("El contacto no se encuentra agendado, por favor vuelva a intentarlo")
            self.menu_opciones()

    def salir(self):
            print("Adios")

prueba = Agenda()
prueba.menu_opciones()

"""mejorar editar, validar nombre, validar email, validar telefono,
 capturar excepciones, raisear errores, traducir al inglés, hacer commit en github"""
