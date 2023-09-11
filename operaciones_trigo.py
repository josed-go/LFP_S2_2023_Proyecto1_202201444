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
            return round(sin(valor_izq),2)
        elif self.tipo.operar(arbol) == 'coseno':
            return round(cos(valor_izq),2)
        elif self.tipo.operar(arbol) == 'tangente':
            return round(tan(valor_izq),2)
        else:
            return None
        
    def obtener_Fila(self):
        return super().obtener_Fila()
    
    def obtener_Columna(self):
        return super().obtener_Columna()