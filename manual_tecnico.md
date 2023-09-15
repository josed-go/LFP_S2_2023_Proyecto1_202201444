# *Manual tecnico Proyecto 1*

* *José David Góngora Olmedo*
* *202201444*

## Introducción

Aplicación Numérica con Análisis Léxico, donde se puede analizar, generar reporte y ver los errores. Con interfaz grafica.

## Características

Se pueden generar y leer archivos con estructura JSON:

- Analizar un archivo JSON
- Mostrar los errores lexicos en el archivo
- Generar reporte de las operaciones.

## Contenido

Este programa contiene las siguientes funcionalidades:

### Archivo ```app.py```

Este archivo es el principal, donde se encuentra toda la interfaz grafica y donde se llaman las funciones de la clase ```analizador.py```

#### Interfaz grafica

Codigo de toda la interfaz grafica, donde se crear los widgets.

```python
self.raiz = raiz
        self.cantidad_lineas = 1
        self.raiz.config(bg="#fdf9c4")
        self.raiz.title("Analizador lexico")
        self.raiz.resizable(0,0)
        self.menu_frame = tk.Frame(self.raiz, width="1350", height="60", bg="#FDF9DF")
        self.menu_frame.pack_propagate(False)
        self.menu_frame.grid_propagate(False)
        self.menu_frame.pack()

        self.menu_frame.columnconfigure(0, weight=1)  # Columna vacía
        self.menu_frame.columnconfigure(1, weight=1)  # Columna para el botón "Analizar"
        self.menu_frame.columnconfigure(2, weight=1)  # Columna para el botón "Errores"
        self.menu_frame.columnconfigure(3, weight=1) 

        self.editor_frame = tk.Frame()

        self.editor_frame.pack()
        self.editor_frame.config(width="1350", height="800", bg="#fdf9c4")

        self.editor = tk.Text(self.editor_frame, width="140", height="39", padx=35, pady=20, font=('Arial', 12))
        self.editor.grid(row=0, column=0, padx=10, pady=25)

        self.lineas_bar = tk.Text(self.editor_frame, width=3, padx=4, pady=20, takefocus=0, border=0, background='lightgrey', state='disabled', font=('Arial', 12))
        self.lineas_bar.tag_configure("center", justify="center")
        self.lineas_bar.tag_add("center", "1.0", "end")
        self.lineas_bar.grid(row=0, column=0, pady=25, sticky="nsw")

        self.editor.bind('<Key>', self.actualizar_lineas)
        self.editor.bind('<MouseWheel>', self.actualizar_lineas)

        self.scroll_editor = tk.Scrollbar(self.editor_frame, command=self.editor.yview)
        self.scroll_editor.grid(row=0, column=0, pady=25, sticky="nse")
        self.editor.config(yscrollcommand=self.scroll_editor.set)

        self.menu = tk.Menu(self.raiz, background='blue', fg='white')


        self.opciones_menu = tk.Menu(self.menu, tearoff=0, background='#fdf9c4')
        self.opciones_menu.add_command(label="Abrir", background='#fdf9c4', command = self.abrir_archivo)
        self.opciones_menu.add_command(label="Guardar", background='#fdf9c4', command = self.guardar_archivo)
        self.opciones_menu.add_command(label="Guardar como", background='#fdf9c4', command = self.guardar_como)
        self.opciones_menu.add_separator(background='#fdf9c4')
        self.opciones_menu.add_command(label="Salir", background='#fdf9c4', command=self.raiz.quit)

        self.menu.add_cascade(label="Archivo", menu=self.opciones_menu)

        self.fuente = font.Font(weight="bold")

        self.label = tk.Label(self.menu_frame, textvariable=self.variable_archivo, bg="#FDF9DF")
        self.label.grid(row=0, column=0, padx=10, pady=10)
        self.label['font'] = self.fuente

        self.analizar_B = tk.Button(self.menu_frame, text="Analizar", padx=20, height=1, bg="#fdf9c4", activebackground="#ffda9e", command = self.analizar_datos)
        self.analizar_B.grid(row=0, column=1, padx=10, pady=10)
        self.analizar_B['font'] = self.fuente

        self.errores_B = tk.Button(self.menu_frame, text="Errores", padx=20, height=1, bg="#fdf9c4", activebackground="#ffda9e", command=self.errores)
        self.errores_B.grid(row=0, column=2, padx=10, pady=10)
        self.errores_B['font'] = self.fuente

        self.reporte_B = tk.Button(self.menu_frame, text="Reporte", padx=20, height=1, bg="#fdf9c4", activebackground="#ffda9e", command= self.generar_reporte)
        self.reporte_B.grid(row=0, column=3, padx=10, pady=10)
        self.reporte_B['font'] = self.fuente

        self.opciones_menu.config(background="#fdf9c4")
        self.raiz.config(menu=self.menu)
```

#### Función 1

Función para generar el numero de lineas que tenga el editor de texto.

```python
def actualizar_lineas(self, event = None):
        cantidad = self.editor.get('1.0', tk.END).count('\n')
        if cantidad != self.cantidad_lineas:
            self.lineas_bar.config(state = tk.NORMAL)
            self.lineas_bar.delete(1.0, tk.END)
            for linea in range(1, cantidad + 1):
                self.lineas_bar.insert(tk.END, f"{linea}\n")
            self.lineas_bar.config(state = tk.DISABLED)
            self.cantidad_lineas = cantidad
```

#### Función 2

Funcion para realizar la lectura del archivo y colocar el contenido en el widget de Texto.

```python
def abrir_archivo(self):
        self.analizador.limpiar_listas()
        self.archivo = filedialog.askopenfilename(filetypes=[("Archivo JSON", "*.json")])
        self.nombre_archivo(self.archivo)
        if self.archivo:
            with open(self.archivo, 'r') as file:
                self.datos_json = file.read()
                self.editor.delete("1.0", tk.END)
                self.editor.insert("1.0", self.datos_json)
            self.actualizar_lineas()
```

#### Función 3

Funcion para guardar archivo con el contenido en el editor.

```python
def guardar_archivo(self):
        if self.editor and self.archivo:
            try:
                self.datos_json = self.editor.get("1.0", tk.END)
                with open(self.archivo, 'w') as file:
                    file.write(self.editor.get("1.0", tk.END))
                messagebox.showinfo("Exito!", "El archivo se ha guardado correctamente")
            except Exception as e:
                messagebox.showinfo("Error!", "Error al guardar el archivo "+ str(e))
```

#### Función 4

Funcion para guardar como, el cual creara un nuevo archivo para guardarlo.

```python
def guardar_como(self):
        if self.editor:
            self.archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivo JSON", "*.json")])
            self.nombre_archivo(self.archivo)
            self.datos_json = self.editor.get("1.0", tk.END)
            if self.archivo:
                with open(self.archivo, "w") as file:
                    file.write(self.editor.get("1.0", tk.END))
            messagebox.showinfo("Exito!", "El archivo se ha guardado correctamente")
```

#### Función 5

Funcion para analizar los datos que se encuentran en el editor de texto. Llama a una funcion de la clase ```analizador.py```

```python
def analizar_datos(self):
        if self.datos_json != '':
            self.analizador.limpiar_listas()
            self.analizador.instruccion(self.datos_json)
            
            results = self.analizador.recursivo_operar()
            resultados_operaciones = ""
            num_operacion = 1
            
            for resultado in results:
                if isinstance(resultado.operar(None), int) or isinstance(resultado.operar(None),float) == True:
                    resultados_operaciones += str(f"Operacion: {num_operacion} --> {resultado.tipo.operar(None)} = {resultado.operar(None)}") + "\n"
                    num_operacion += 1

            messagebox.showinfo("Resultados de operaciones", resultados_operaciones)
        else:
            messagebox.showerror("Error", "No hay un archivo cargado")
```

#### Función 6

Funcion para generar el archivo de salida de los errores con estructura JSON. Llama a una funcion de la clase ```analizador.py```

```python
def errores(self):
    self.analizador.generar_errores()
    messagebox.showinfo("Exito!", "El archivo se ha generado correctamente")}
```

#### Función 7

Funcion para generar el reporte de las operaciones realizadas al analizar el contenido. Llama a una funcion de la clase ```analizador.py```

```python
def generar_reporte(self):
        self.analizador.generar_grafica()
        messagebox.showinfo("Exito!", "Reporte generado correctamente")
```

### Archivo ```analizador.py```

En este archivo se hace toda la logica del analizador y donde se crean los reportes y archivos de salida.

#### Función 1

En esta funcion se obtiene como argumento la cadena (El texto a analizar) para ir recorriendo caracter por caracter e ir formando los lexemas. Y tambien donde se guardan los errores lexicos si los hay.

```python
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
            elif char == ' ' or char == '\r' or char == '{' or char == '}' or char == ',' or char == ':' or char == '.':
                cadena = cadena[1:]
                self.numero_columna += 1
                puntero = 0
            else:
                cadena = cadena[1:]
                puntero = 0
                self.numero_columna += 1
                error = errores((len(self.lista_errores)+1),char, "Error lexico", self.numero_linea, self.numero_columna)
                self.lista_errores.append(error)
```

#### Función 2

Función para eliminar un elemento anterior de la lista.

```python
def borrar_anterior(self):
        while self.lista_lexema[-1].lexema != "operacion":
            self.lista_lexema.pop(-1)
```

#### Función 3

Función para agrupar los lexemas (si son una palabra).

```python
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
```

#### Función 4

Función para armar los numeros y ver si son de tipo entero o decimal.

```python
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
```

#### Función 4

Función para realizar las operaciones y almacenar los resultados, tambien para guardar las configuraciones para los reportes.

```python
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
            
            if lexema.operar(None) == 'texto':
                self.texto = self.lista_lexema.pop(0)
                #print(self.texto.lexema)
        
            if lexema.operar(None) == 'fondo':
                self.fondo = self.lista_lexema.pop(0)
                #print(self.fondo.lexema)
            if lexema.operar(None) == 'fuente':
                self.fuente = self.lista_lexema.pop(0)
                #print(self.fuente.lexema)
            if lexema.operar(None) == 'forma':
                self.forma = self.lista_lexema.pop(0)
                #print(self.forma.lexema)
            
            if operacion and num1 and num2:
                return operaciones_arit( num1, num2, operacion, f'Inicio: {operacion.obtener_Fila()}: {operacion.obtener_Columna()}', f'Fin: {num2.obtener_Fila()}:{num2.obtener_Columna()}')
            elif operacion and num1 and operacion.operar(None) == ('seno' or 'coseno' or 'tangente'):
                return operaciones_trigo(num1, operacion, f'Inicio: {operacion.obtener_Fila()}: {operacion.obtener_Columna()}', f'Fin: {num1.obtener_Fila()}:{num1.obtener_Columna()}')
        return None
```

#### Función 5

Función para hacer recursividad al momento de hacer las operaciones y ver si hay operaciones anidadas.

```python
def recursivo_operar(self):
        while True:
            operacion = self.operaciones()
            if operacion:
                self.lista_instrucciones.append(operacion)
            else :
                break
        
        return self.lista_instrucciones
```

#### Función 6

Función para generar los errores en un archivo con estrucutra JSON.

```python
def generar_errores(self):
        datos = {}

        datos["errores"] = []
        for error in self.lista_errores:
            datos["errores"].append({
                "No": int(error.numero),
                "descripcion": {
                    "lexema": error.lexema,
                    "tipo": error.tipo,
                    "columna": int(error.columna),
                    "fila": int(error.fila)
                }
            })
        
        try:
            with open('RESULTADOS_202201444.json', 'w') as file:
                json.dump(datos, file, indent = 4)
        except Exception as e:
            print(e)
```

#### Función 7

Función para armar los nodos en dot para generar la grafica.

```python
def armar_nodos(self, tipo, num, clave, separador):
        datos = ""

        if tipo:
            if type(tipo) == numero:
                
                datos += f'nodo{num}{clave}{separador}[label="{tipo.operar(None)}"];\n'


            if type(tipo) == operaciones_arit:
                datos += f'nodo{num}{clave}{separador}[label="{tipo.tipo.lexema}\\n{tipo.operar(None)}"];\n'

                datos += self.armar_nodos(tipo.izq ,num, clave+1, separador+"_izq")

                datos += f'nodo{num}{clave}{separador} -> nodo{num}{clave+1}{separador}_izq;\n'

                datos += self.armar_nodos(tipo.dere,num, clave+1, separador+"_dere")

                datos += f'nodo{num}{clave}{separador} -> nodo{num}{clave+1}{separador}_dere;\n'
            
            if type(tipo) == operaciones_trigo:
                
                datos += f'nodo{num}{clave}{separador}[label="{tipo.tipo.lexema}\\n{tipo.operar(None)}"];\n'

                datos += self.armar_nodos(tipo.izq,num, clave+1, separador+"_tri")

                datos += f'nodo{num}{clave}{separador} -> nodo{num}{clave+1}{separador}_tri;\n'


        return datos
```

#### Función 8

Función para generar la grafica utilizando la libreria graphviz.

```python
def generar_grafica(self):
        texto = """digraph G {
                    label=" """+self.texto.lexema+""""
                    node[style=filled, color=" """+self.fondo.lexema+"""", fontcolor=" """+self.fuente.lexema+"""", shape="""+self.forma.lexema+"""]"""

        for i in range(len(self.lista_instrucciones)):
            texto += f"\nsubgraph cluster_{i}"+"{"
            texto += self.armar_nodos(self.lista_instrucciones[i], i, 0,'')
            texto += "\n}"

        texto += "\n}"
        f = open('bb.dot', 'w')

        f.write(texto)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f'dot -Tpng bb.dot -o REPORTE_202201444.png')
```

#### Función 9

Funcion para limpiar todas las listas y datos.

```python
def limpiar_listas(self):
        self.lista_lexema.clear()
        self.lista_instrucciones.clear()
        self.lista_errores.clear()


        self.numero_linea = 1
        self.numero_columna = 1
        # CONFIGURACIONES
        self.fondo = ''
        self.texto = ''
        self.fuente = ''
        self.forma = ''
```

### Archivo ```abstraccion.py```

Clase abstracta para que otras clases hereden de ella. Como la clase ```lexema.py```, ```numero.py``` y ```errores.py```. Las cuales contienen los siguientes metodos.

#### Metodos de la clase abstracta

```python
@abstractmethod
def operar(self, arbol):
    pass

@abstractmethod
def obtener_Fila(self):
    return self.fila

@abstractmethod
def obtener_Columna(self):
    return self.columna
```

### Archivo ```operaciones_arit.py```

Archivo para realizar todas las operaciones aritmeticas y devolver el resultado. Hereda de la clase ```Expression```

#### Función ```operar```

```python
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
```

### Archivo ```operaciones_trigo.py```

Archivo para realizar todas las operaciones trigonometricas y devolver el resultado. Hereda de la clase ```Expression```

#### Función ```operar```

```python
def operar(self, arbol):
        valor_izq = ''
        if self.izq != None:
            valor_izq = self.izq.operar(arbol)
        
        if self.tipo.operar(arbol).lower() == 'seno':
            return round(sin(valor_izq),2)
        elif self.tipo.operar(arbol).lower() == 'coseno':
            return round(cos(valor_izq),2)
        elif self.tipo.operar(arbol).lower() == 'tangente':
            return round(tan(valor_izq),2)
        else:
            return None
```