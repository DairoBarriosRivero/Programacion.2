import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "Hola, has hecho clic en el botón.")

def obtener_valor():
    valor = entry.get()
    if valor:
        label_resultado.config(text=f"El valor ingresado es: {valor}")
    else:
        label_resultado.config(text="No se ha ingresado ningún valor.")

def seleccionar_opcion():
    if opcion_var.get() == 1:
        label_opcion.config(text="Opción seleccionada: Opción 1")
    elif opcion_var.get() == 2:
        label_opcion.config(text="Opción seleccionada: Opción 2")

def agregar_elemento():
    elemento = entry_elemento.get()
    if elemento:
        listbox.insert(tk.END, elemento)
        entry_elemento.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor ingresa un elemento.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("App con Widgets")

# Etiqueta
label = tk.Label(ventana, text="Etiqueta")
label.pack()

# Botón
boton = tk.Button(ventana, text="Haz clic", command=mostrar_mensaje)
boton.pack()

# Entrada de texto
entry = tk.Entry(ventana)
entry.pack()

# Botón para obtener el valor de la entrada de texto
boton_valor = tk.Button(ventana, text="Obtener Valor", command=obtener_valor)
boton_valor.pack()

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

# Checkbutton
check_var = tk.IntVar()
checkbutton = tk.Checkbutton(ventana, text="Checkbutton", variable=check_var)
checkbutton.pack()

# Radiobuttons
opcion_var = tk.IntVar()
opcion1 = tk.Radiobutton(ventana, text="Opción 1", variable=opcion_var, value=1, command=seleccionar_opcion)
opcion1.pack()
opcion2 = tk.Radiobutton(ventana, text="Opción 2", variable=opcion_var, value=2, command=seleccionar_opcion)
opcion2.pack()

# Etiqueta para mostrar la opción seleccionada
label_opcion = tk.Label(ventana, text="")
label_opcion.pack()

# ListBox
listbox = tk.Listbox(ventana)
listbox.pack()

# Entrada de texto para agregar elementos a la ListBox
entry_elemento = tk.Entry(ventana)
entry_elemento.pack()

# Botón para agregar elementos a la ListBox
boton_agregar_elemento = tk.Button(ventana, text="Agregar Elemento", command=agregar_elemento)
boton_agregar_elemento.pack()

# Ejecutar la aplicación
ventana.mainloop()
