# *Manual de usuario Proyecto 1*

* *José David Góngora Olmedo*
* *202201444*

### Descripción

Este programa se encarga de analizar el contenido para verificar si tiene errrores Lexicos. El programa puede leer, escribir, analizar archivos y generar reportes y archivos de salida. Está diseñado para que sea fácil de utilizar y agradable para la vista del usuario.

### Requisitos mínimos

#### Sistemas operativos

* Windows
* macOS
* Linux

#### Memoria

* 4 GB de RAM

#### Almacenamiento

* Al menos 5 GB de espacio

### Inicio

Al ejecutar el programa se podra ver la interfaz

![Pantalla de inicio](/img/img1.JPG)

1. Boton de las opciones de archivo
    * Abrir
    * Guardar
    * Guardar como

2. Botones para analizar, generar los errores y generar reporte.

3. Editor de texto, donde se podra escribir y editar el texto de los archivos.

### Abrir archivo

Al dar click en la opción de abrir, se abrira una ventana para elegir el archivo a abrir (JSON).

![Ventana abrir](/img/img2.JPG)

Al seleccionar el archivo se mostrara en el programa.

![Archivo abierto](/img/img3.JPG)

1. Se mostrara el nombre del archivo que se esta editando.

3. El contenido del archivo cargado se mostrara en el editor.

### Guardar archivo

Al dar click en guardar, se guardaran todos los cambios realizados.

![Mensaje archivo guardado](/img/img4.JPG)

Se mostrara el siguiente mensaje para indicar que se han guardado los cambios.

### Guardar como

Al dar click en guardar como, se mostrara una ventana para elegir como desea guardar el archivo.

![Ventana guardar como](/img/img5.JPG)

Y se guardara el archivo.

### Analizar

Al dar click en el boton de analizar, el programa comenzara a analizar todo el contenido del archivo para mostrar los resultados.

![Mensaje de resultados](/img/img6.JPG)

Se mostrara una ventana donde se veran todas las operaciones realizadas

### Errores

Al dar click en el boton de errores, se creara un archivo ```RESULTADOS_202201444.json``` donde se mostraran los errores encontrados.

```json
{
    "errores": [
        {
            "No": 1,
            "descripcion": {
                "lexema": "*",
                "tipo": "Error lexico",
                "columna": 4,
                "fila": 1
            }
        },
        {
            "No": 2,
            "descripcion": {
                "lexema": "?",
                "tipo": "Error lexico",
                "columna": 12,
                "fila": 19
            }
        },
        {
            "No": 3,
            "descripcion": {
                "lexema": "!",
                "tipo": "Error lexico",
                "columna": 12,
                "fila": 33
            }
        },
        {
            "No": 4,
            "descripcion": {
                "lexema": "$",
                "tipo": "Error lexico",
                "columna": 13,
                "fila": 33
            }
        },
        {
            "No": 5,
            "descripcion": {
                "lexema": "%",
                "tipo": "Error lexico",
                "columna": 8,
                "fila": 39
            }
        },
        {
            "No": 6,
            "descripcion": {
                "lexema": "%",
                "tipo": "Error lexico",
                "columna": 9,
                "fila": 39
            }
        }
    ]
}
```

Ejemplo del archivo JSON de salida.

### Reporte

Al dar click en el boton de reporte, se generara una grafica con todas las operaciones realizadas y con las configuraciones establecidas en el archivo de entrada.

![Reporte de operaciones](/img/REPORTE_202201444.png)