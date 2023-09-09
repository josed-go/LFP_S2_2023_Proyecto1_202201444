from operaciones_arit import *
from operaciones_trigo import *
from lexema import *
from numero import *
from errores import *

class analizador:
    def __init__(self):

        self.numero_linea = 1
        self.numero_columna = 1

        self.lista_lexema = []
        self.lista_instrucciones = []
        self.lista_errores = []

        self.palabras_reservadas = {
            'OPERACIONES': 'operaciones',
            'Operacion': 'operacion',
            'VALOR1': 'valor1',
            'VALOR2': 'valor2',
            'SUMA': 'suma',
            'RESTA': 'resta',
            'MULTIPLICACION': 'multiplicacion',
            'DIVISION': 'division',
            'POTENCIA': 'potencia',
            'RAIZ': 'raiz',
            'INVERSO': 'inverso',
            'SENO': 'seno',
            'COSENO': 'coseno',
            'TANGENTE': 'tangente',
            'MOD': 'mod',
            'CONFIGURACIONES': 'configuraciones',
            'TEXTO': 'texto',
            'FONDO': 'fondo',
            'FORMA': 'forma',
            'TEXTO' : 'Operaciones',
            'FONDO' : 'azul',
            'FUENTE' :'blanco',
            'FORMA': 'circulo',
            'Textos' : 'textos',
            'Fondo' : 'fondo',
            'Fuente' : 'fuente',
            'Forma' : 'forma',
            'Circulo' : 'circulo',
            'COMA': ',',
            'PUNTO': '.',
            'PUNTOS': ':',
            'CORCHETEI': '[',
            'CORCHETEF': ']',
            'LLAVEI': '{',
            'LAVEF': '}'
        }

        self.lexemas = list(self.palabras_reservadas.values())

    def instruccion(self, cadena):
        lexema = ''
        puntero = 0

        while cadena:
            char = cadena[puntero]
            puntero += 1

            if char == '\"':
                lexema, cadena = self.grupo_lexema(cadena[puntero:])
                if lexema and cadena:
                    self.numero_columna += 1
                    if lexema not in self.lexemas:
                        error = errores((len(self.lista_errores)+1),lexema, "Error lexico", self.numero_linea, self.numero_columna)
                        self.lista_errores.append(error)
                        self.numero_columna += len(lexema) +1
                        puntero = 0
                        cadena = self.borrar(cadena)
                        self.lista_lexema.pop(-1)
                    else:
                        lex = Lexema(lexema, self.numero_linea, self.numero_columna)

                        self.lista_lexema.append(lex)
                        self.numero_columna += len(lexema) + 1
                        puntero = 0
            elif char.isdigit():
                token, cadena = self.numeros(cadena)

                if token and cadena:
                        self.numero_columna += 1

                        num = numero(token, self.numero_linea, self.numero_linea)

                        self.lista_lexema.append(num)
                        self.numero_columna += len(str(token)) + 1
                        puntero = 0
            elif char == '[' or char == ']':

                c = Lexema(char, self.numero_linea, self.numero_columna)

                self.lista_lexema.append(c)


                cadena = cadena[1:]
                puntero = 0
                self.numero_columna += 1

            elif char == '\t':
                self.numero_columna += 4
                cadena = cadena[4:]
                puntero = 0
            elif char == '\n':
                cadena = cadena[1:]
                puntero = 0
                self.numero_linea += 1
                self.numero_columna = 1
            else:
                cadena = cadena[1:]
                puntero = 0
                self.numero_columna += 1
        print("--------------------")
        for error in self.lista_errores:
            print("Error encontrado: No.: {}, Lexema: {}, Tipo: {}, Fila: {}, Columna: {}".format(
                error.numero, error.lexema, error.tipo, error.obtener_Fila(), error.obtener_Columna()))
        print("--------------------")

        """for lexema in self.lista_lexema:
            print("Lexema: {}, Fila: {}, Columna: {}".format(
                lexema.lexema, lexema.obtener_Fila(), lexema.obtener_Columna()))"""

    def borrar(self, cadena):
        """puntero = ''
        prueba = ''
        for char in cadena:
            puntero += char

            if char == '{' and char:
                prueba += char
            
        return None"""
        puntero = 0
        while cadena:
            char = cadena[puntero]
            puntero += 1

            if char == '}' and cadena[puntero] == ',':
                return cadena[puntero:]
            
        return None


    def grupo_lexema(self, cadena):
        lexema = ''
        puntero = ''

        for char in cadena:
            puntero += char
            if char == '\"':
                return lexema, cadena[len(puntero):]
            else :
                lexema += char
        return None, None
    
    def numeros(self, cadena):
        numero = ''
        puntero = ''
        es_decimal = False
        for char in cadena:
            puntero += char
            if char == '.':
                es_decimal = True
            if char == '\"' or char == ' ' or char == '\n' or char == '\t' or char == ',':
                if es_decimal:
                    return float(numero), cadena[len(puntero)-1:]
                else:
                    return int(numero), cadena[len(puntero)-1:]
            else:
                numero += char
        return None, None
    
    def operaciones(self):
        operacion = ''
        num1 = ''
        num2 = ''

        while self.lista_lexema:
            lexema = self.lista_lexema.pop(0)
            if lexema.operar(None) == 'operacion':
                operacion = self.lista_lexema.pop(0)
            elif lexema.operar(None) == 'valor1':
                num1 = self.lista_lexema.pop(0)
                if num1.operar(None) == '[':
                    num1 = self.operaciones()
            elif lexema.operar(None) == 'valor2':
                num2 = self.lista_lexema.pop(0)
                if num2.operar(None) == '[':
                    num2 = self.operaciones()

            if operacion and num1 and num2:
                return operaciones_arit( num1, num2, operacion, f'Inicio: {operacion.obtener_Fila()}: {operacion.obtener_Columna()}', f'Fin: {num2.obtener_Fila()}:{num2.obtener_Columna()}')
            elif operacion and num1 and operacion.operar(None) == ('seno' or 'coseno' or 'tangente'):
                return operaciones_trigo(num1, operacion, f'Inicio: {operacion.obtener_Fila()}: {operacion.obtener_Columna()}', f'Fin: {num1.obtener_Fila()}:{num1.obtener_Columna()}')
        return None
    
    def recursivo_operar(self):
        while True:
            operacion = self.operaciones()
            if operacion:
                self.lista_instrucciones.append(operacion)
            else :
                break

        return self.lista_instrucciones