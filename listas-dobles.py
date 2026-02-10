#Listas doblemente ligadas

class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    # Revisar si la lista está vacía
    def esta_vacia(self):
        return self.cabeza is None # Igual que if self.cabeza == None return True, else False
    
    # Insertar nodo al inicio
    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)

        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.siguiente = cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
    
    # Insertar nodo al final
    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo
    
    # Eliminar nodo al inicio
    def eliminar_inicio(self):
        if self.esta_vacia():
            return None
        
        if self.cabeza.dato == self.cola.dato:
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None

    # Eliminar nodo al final
    def eliminar_final(self):
        if self.esta_vacia:
            return None
        
        if self.cabeza.dato == self.cola.dato:
            self.cabeza = None
            self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None

    # Recorrer lista del primero al último
    def recorrer_adelante(self):
        if self.esta_vacia():
            print("Lista vacía")
            return
        print("Recorriendo Inicio --> Fin")
        actual = self.cabeza

        while actual: #Mientras haya un nodo != None
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("Fin")

    # Recorrer lista del último al primero
    def recorrer_atras(self):
        if self.esta_vacia():
            print("Lista vacía")
            return
        print("Recorriendo Fin --> Inicio")
        actual = self.cola

        while actual:
            print(actual.dato, end= " -> ")
            actual = actual.anterior
        print("Fin")

    # Buscar dato
    def buscar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        
        return False

    # Sobreescribir método de longitud
    def __len__(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    # Sobreescribir método para imprimir la lista
    def __str__(self):
        if self.esta_vacia():
            return "Lista vacía"
        
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato)) # Agregar dato tipo string a la lista elementos
            actual = actual.siguiente
        return " <=> ".join(elementos)


# Instanciar lista

lista = ListaDoble()

# Insertar datos (Nodos)
lista.insertar_final(10)
lista.insertar_final(20)
lista.insertar_final(30)
print(lista)

lista.recorrer_adelante()
lista.recorrer_atras()

print(f"Tamaño de la lista:  {len(lista)}")

print(lista.buscar(50))