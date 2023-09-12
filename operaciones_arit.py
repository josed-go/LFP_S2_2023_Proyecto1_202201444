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

        if self.tipo.operar(arbol).lower() == 'suma':
            return round(valor_izq + valor_dere,2) 
        elif self.tipo.operar(arbol).lower() == 'resta':
            return round(valor_izq - valor_dere,2) 
        elif self.tipo.operar(arbol).lower() == 'multiplicacion':
            return round(valor_izq * valor_dere,2) 
        elif self.tipo.operar(arbol).lower() == 'division':
            return round(valor_izq / valor_dere,2) 
        elif self.tipo.operar(arbol).lower() == 'mod':
            return round(valor_izq % valor_dere,2) 
        elif self.tipo.operar(arbol).lower() == 'potencia':
            return round(valor_izq ** valor_dere,2) 
        elif self.tipo.operar(arbol).lower() == 'raiz':
            return round(valor_izq ** (1/valor_dere),2)
        elif self.tipo.operar(arbol).lower() == 'inverso':
            return round(1/valor_izq,2)
        else:
            return None
        
    def obtener_Fila(self):
        return super().obtener_Fila()
    
    def obtener_Columna(self):
        return super().obtener_Columna()