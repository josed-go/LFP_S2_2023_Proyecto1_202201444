import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import tkinter.font as font
import json

class app:
    def __init__(self, raiz):
        self.archivo = ""

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

        self.analizar_B = tk.Button(self.menu_frame, text="Analizar", padx=20, height=1, bg="#fdf9c4", activebackground="#ffda9e")
        self.analizar_B.grid(row=0, column=1, padx=10, pady=10)
        self.analizar_B['font'] = self.fuente

        self.errores_B = tk.Button(self.menu_frame, text="Errores", padx=20, height=1, bg="#fdf9c4", activebackground="#ffda9e")
        self.errores_B.grid(row=0, column=2, padx=10, pady=10)
        self.errores_B['font'] = self.fuente

        self.reporte_B = tk.Button(self.menu_frame, text="Reporte", padx=20, height=1, bg="#fdf9c4", activebackground="#ffda9e")
        self.reporte_B.grid(row=0, column=3, padx=10, pady=10)
        self.reporte_B['font'] = self.fuente

        self.opciones_menu.config(background="#fdf9c4")
        self.raiz.config(menu=self.menu)

    def center_window(self, window):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - 1350) // 2
        y = (screen_height - 850) // 2
        window.geometry(f"1350x850+{x}+{y}")

    def actualizar_lineas(self, event = None):
        cantidad = self.editor.get('1.0', tk.END).count('\n')
        if cantidad != self.cantidad_lineas:
            self.lineas_bar.config(state = tk.NORMAL)
            self.lineas_bar.delete(1.0, tk.END)
            for linea in range(1, cantidad + 1):
                self.lineas_bar.insert(tk.END, f"{linea}\n")
            self.lineas_bar.config(state = tk.DISABLED)
            self.cantidad_lineas = cantidad

    def abrir_archivo(self):
        self.archivo = filedialog.askopenfilename(filetypes=[("Archivo JSON", "*.json")])
        if self.archivo:
            with open(self.archivo, 'r') as file:
                datos_json = json.load(file)
                self.editor.delete("1.0", tk.END)
                self.editor.insert("1.0", json.dumps(datos_json, indent=4))
            self.actualizar_lineas()

    def guardar_archivo(self):
        if self.editor and self.archivo:
            try:
                with open(self.archivo, 'w') as file:
                    file.write(self.editor.get("1.0", tk.END))
                messagebox.showinfo("Exito!", "El archivo se ha guardado correctamente")
            except Exception as e:
                messagebox.showinfo("Error!", "Error al guardar el archivo "+ str(e))

    def guardar_como(self):
        if self.editor:
            self.archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivo JSON", "*.json")])
            if self.archivo:
                with open(self.archivo, "w") as file:
                    file.write(self.editor.get("1.0", tk.END))
            messagebox.showinfo("Exito!", "El archivo se ha guardado correctamente")

raiz = tk.Tk()
ventana = app(raiz)
ventana.center_window(raiz)

raiz.mainloop()