class Invitado:
    def __init__(self, nombre, id_unico):
        self.nombre = nombre
        self.id_unico = id_unico

class GestorInvitados:
    def __init__(self):
        self.lista_invitados = []

    def agregar_invitado(self, nombre):
        # Generame el id unico en base al id del ultimo elemento de la lista
        if self.lista_invitados:
            id_unico = self.lista_invitados[-1].id_unico + 1
        else:
            id_unico = 1 # Si la lista esta vacia, el id unico es 1
            
        invitado = Invitado(nombre, id_unico)
        self.lista_invitados.append(invitado)
        print(f"Invitado '{nombre}' agregado con ID único: {id_unico}")

    def eliminar_invitado(self, id_unico):
        for invitado in self.lista_invitados:
            if invitado.id_unico == id_unico:
                self.lista_invitados.remove(invitado)
                print(f"Invitado con ID único {id_unico} eliminado.")
                return
        print(f"No se encontró un invitado con ID único {id_unico}.")

    def mostrar_invitados(self):
        if not self.lista_invitados:
            print("La lista de invitados está vacía.")
        else:
            print("Lista de invitados:")
            for invitado in self.lista_invitados:
                print(f"ID: {invitado.id_unico}, Nombre: {invitado.nombre}")

# Uso del programa
gestor_invitados = GestorInvitados()

while True:
    print("\nMenú:")
    print("1. Agregar invitado")
    print("2. Eliminar invitado")
    print("3. Mostrar invitados")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        nombre_invitado = input("Ingrese el nombre del invitado: ")
        gestor_invitados.agregar_invitado(nombre_invitado)
    elif opcion == "2":
        id_a_eliminar = int(input("Ingrese el ID único del invitado a eliminar: "))
        gestor_invitados.eliminar_invitado(id_a_eliminar)
    elif opcion == "3":
        gestor_invitados.mostrar_invitados()
    elif opcion == "4":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
