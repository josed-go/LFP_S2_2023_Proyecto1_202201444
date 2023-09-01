import tkinter as tk
from tkinter import ttk
import tkinter.font as font

def center_window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - 1350) // 2
    y = (screen_height - 850) // 2
    window.geometry(f"1350x850+{x}+{y}")

raiz = tk.Tk()
raiz.config(bg="#fdf9c4")
#raiz.config(bg="#FDF9E0")
raiz.title("Analizador lexico")

raiz.resizable(0,0)
#raiz.geometry("1350x850")
#raiz.eval('tk::PlaceWindow . center')

menu_frame = tk.Frame(raiz, width="1350", height="60", bg="#FDF9DF")
menu_frame.pack_propagate(False)
menu_frame.grid_propagate(False)
menu_frame.pack()
#menu_frame.config(bg="#ffda9e")
#menu_frame.config(width="1350", height="50")

menu_frame.columnconfigure(0, weight=1)  # Columna vacía
menu_frame.columnconfigure(1, weight=1)  # Columna para el botón "Analizar"
menu_frame.columnconfigure(2, weight=1)  # Columna para el botón "Errores"
menu_frame.columnconfigure(3, weight=1) 

editor_frame = tk.Frame()

editor_frame.pack()
editor_frame.config(width="1350", height="800", bg="#fdf9c4")

editor = tk.Text(editor_frame, width="140", height="39", padx=20, pady=20, font=('Arial', 12))
editor.grid(row=0, column=0, padx=10, pady=25)

scroll_editor = tk.Scrollbar(editor_frame, command=editor.yview)
scroll_editor.grid(row=0, column=0, pady=25, sticky="nse")
editor.config(yscrollcommand=scroll_editor.set)


menu = tk.Menu(raiz, background='blue', fg='white')


opciones_menu = tk.Menu(menu, tearoff=0, background='#fdf9c4')
opciones_menu.add_command(label="Abrir", background='#fdf9c4')
opciones_menu.add_command(label="Guardar", background='#fdf9c4')
opciones_menu.add_command(label="Guardar como", background='#fdf9c4')
opciones_menu.add_separator(background='#fdf9c4')
opciones_menu.add_command(label="Salir", background='#fdf9c4', command=raiz.quit)

menu.add_cascade(label="Archivo", menu=opciones_menu)

fuente = font.Font(weight="bold")

analizar_B = tk.Button(menu_frame, text="Analizar", padx=20, height=1, bg="#fdf9c4", activebackground="#ffda9e")
analizar_B.grid(row=0, column=1, padx=10, pady=10)
analizar_B['font'] = fuente

errores_B = tk.Button(menu_frame, text="Errores", padx=20, height=1, bg="#fdf9c4", activebackground="#ffda9e")
errores_B.grid(row=0, column=2, padx=10, pady=10)
errores_B['font'] = fuente

reporte_B = tk.Button(menu_frame, text="Reporte", padx=20, height=1, bg="#fdf9c4", activebackground="#ffda9e")
reporte_B.grid(row=0, column=3, padx=10, pady=10)
reporte_B['font'] = fuente

opciones_menu.config(background="#fdf9c4")
raiz.config(menu=menu)


center_window(raiz)

raiz.mainloop()