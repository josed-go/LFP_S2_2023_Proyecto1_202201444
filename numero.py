from abstraccion import Expression

class numero(Expression):
    def __init__(self, valor, fila, columna):
        self.valor = valor
        super().__init__(fila, columna)

    def operar(self, arbol):
        return self.valor
    
    def obtener_Fila(self):
        return super().obtener_Fila()
    
    def obtener_Columna(self):
        return super().obtener_Columna()