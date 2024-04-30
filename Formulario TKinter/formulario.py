import tkinter as tk
from tkinter import messagebox
#Dairo Barrios Rivero
def registrar():
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    edad = edad_entry.get()
    direccion = direccion_entry.get()
    telefono = telefono_entry.get()
    sexo = sexo_var.get()
    ciudad = ciudad_listbox.get(tk.ACTIVE)

    mensaje = f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nDirección: {direccion}\nTeléfono: {telefono}\nSexo: {sexo}\nCiudad: {ciudad}"
    messagebox.showinfo("Información Registrada", mensaje)

ventana = tk.Tk()
ventana.title("Formulario de Registro")

tk.Label(ventana, text="Nombre:").pack()
nombre_entry = tk.Entry(ventana)
nombre_entry.pack()

tk.Label(ventana, text="Apellido:").pack()
apellido_entry = tk.Entry(ventana)
apellido_entry.pack()

tk.Label(ventana, text="Edad:").pack()
edad_entry = tk.Entry(ventana)
edad_entry.pack()

tk.Label(ventana, text="Dirección:").pack()
direccion_entry = tk.Entry(ventana)
direccion_entry.pack()

tk.Label(ventana, text="Teléfono:").pack()
telefono_entry = tk.Entry(ventana)
telefono_entry.pack()

tk.Label(ventana, text="Sexo:").pack()
sexo_var = tk.StringVar()
tk.Radiobutton(ventana, text="Masculino", variable=sexo_var, value="Masculino").pack()
tk.Radiobutton(ventana, text="Femenino", variable=sexo_var, value="Femenino").pack()

tk.Label(ventana, text="Ciudad:").pack()
ciudad_listbox = tk.Listbox(ventana, selectmode=tk.SINGLE)
ciudades = ["Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena"]
for ciudad in ciudades:
    ciudad_listbox.insert(tk.END, ciudad)
ciudad_listbox.pack()

tk.Button(ventana, text="Registrar", command=registrar).pack()

ventana.mainloop()
