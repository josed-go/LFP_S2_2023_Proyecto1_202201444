import tkinter as tk

def center_window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - 1350) // 2
    y = (screen_height - 850) // 2
    window.geometry(f"1350x850+{x}+{y}")

raiz = tk.Tk()

raiz.title("Analizador lexico")

raiz.resizable(0,0)
#raiz.geometry("1350x850")
#raiz.eval('tk::PlaceWindow . center')

menu_frame = tk.Frame(raiz, width="1350", height="50", bg="#ffda9e")

menu_frame.pack()
#menu_frame.config(bg="#ffda9e")
#menu_frame.config(width="1350", height="50")

editor_frame = tk.Frame()

editor_frame.pack()
editor_frame.config(width="1350", height="800")

editor = tk.Text(editor_frame, width="140", height="39", padx=20, pady=20, font=('Arial', 12))
editor.grid(row=0, column=0, padx=10, pady=25)

scroll_editor = tk.Scrollbar(editor_frame, command=editor.yview)
scroll_editor.grid(row=0, column=0, pady=25, sticky="nse")
editor.config(yscrollcommand=scroll_editor.set)


center_window(raiz)


raiz.mainloop()