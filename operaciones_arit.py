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
            return valor_izq + valor_dere 
        elif self.tipo.operar(arbol) == 'resta':
            return valor_izq - valor_dere 
        elif self.tipo.operar(arbol) == 'multiplicacion':
            return valor_izq * valor_dere 
        elif self.tipo.operar(arbol) == 'division':
            return valor_izq / valor_dere 
        elif self.tipo.operar(arbol) == 'mod':
            return valor_izq % valor_dere 
        elif self.tipo.operar(arbol) == 'potencia':
            return valor_izq ** valor_dere 
        elif self.tipo.operar(arbol) == 'raiz':
            return valor_izq ** (1/valor_dere)
        elif self.tipo.operar(arbol) == 'inverso':
            return 1/valor_izq
        else:
            return 'Error'
        
    def obtener_Fila(self):
        return super().obtener_Fila()
    
    def obtener_Columna(self):
        return super().obtener_Columna()