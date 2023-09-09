from abstraccion import Expression
from math import *

class operaciones_trigo(Expression):
    def __init__(self, izq, tipo, fila, columna):
        self.izq = izq
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        valor_izq = ''
        if self.izq != None:
            valor_izq = self.izq.operar(arbol)
        
        if self.tipo.operar(arbol) == 'seno':
            return sin(valor_izq)
        elif self.tipo.operar(arbol) == 'coseno':
            return cos(valor_izq)
        elif self.tipo.operar(arbol) == 'tangente':
            return tan(valor_izq)
        else:
            return 0
        
    def obtener_Fila(self):
        return super().obtener_Fila()
    
    def obtener_Columna(self):
        return super().obtener_Columna()