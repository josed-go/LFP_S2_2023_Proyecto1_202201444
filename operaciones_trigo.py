import math
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
        
        if self.tipo.operar(arbol).lower() == 'seno':
            return round(sin(radians(valor_izq)),2)
        elif self.tipo.operar(arbol).lower() == 'coseno':
            return round(cos(radians(valor_izq)),2)
        elif self.tipo.operar(arbol).lower() == 'tangente':
            return round(tan(radians(valor_izq)),2)
        elif self.tipo.operar(arbol).lower() == 'inverso':
            return round(1/valor_izq,2)
        else:
            return None
        
    def obtener_Fila(self):
        return super().obtener_Fila()
    
    def obtener_Columna(self):
        return super().obtener_Columna()