class DequeDobleExtremo:
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def insertar_frente(self, elemento):
        self.items.insert(0, elemento)
    
    def insertar_final(self, elemento):
        self.items.append(elemento)
    
    def eliminar_frente(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        raise IndexError("El deque está vacío")
    
    def eliminar_final(self):
        if not self.esta_vacia():
            return self.items.pop()
        raise IndexError("El deque está vacío")
    
    def tamano(self):
        return len(self.items)