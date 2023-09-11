from abstraccion import Expression

class operaciones_arit(Expression):
    def __init__(self, izq, dere, tipo, fila, columna):
        self.izq = izq
        self.dere = dere
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        valor_izq = ''
        valor_dere = ''
        if self.izq != None:
            valor_izq = self.izq.operar(arbol)
        if self.dere != None:
            valor_dere = self.dere.operar(arbol)

        if self.tipo.operar(arbol) == 'suma':
            return round(valor_izq + valor_dere,2) 
        elif self.tipo.operar(arbol) == 'resta':
            return round(valor_izq - valor_dere,2) 
        elif self.tipo.operar(arbol) == 'multiplicacion':
            return round(valor_izq * valor_dere,2) 
        elif self.tipo.operar(arbol) == 'division':
            return round(valor_izq / valor_dere,2) 
        elif self.tipo.operar(arbol) == 'mod':
            return round(valor_izq % valor_dere,2) 
        elif self.tipo.operar(arbol) == 'potencia':
            return round(valor_izq ** valor_dere,2) 
        elif self.tipo.operar(arbol) == 'raiz':
            return round(valor_izq ** (1/valor_dere),2)
        elif self.tipo.operar(arbol) == 'inverso':
            return round(1/valor_izq,2)
        else:
            return None
        
    def obtener_Fila(self):
        return super().obtener_Fila()
    
    def obtener_Columna(self):
        return super().obtener_Columna()