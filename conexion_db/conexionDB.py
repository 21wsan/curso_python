import mysql.connector
import tkinter as tk
from tkinter import messagebox, simpledialog

# Conectar a la base de datos
def conectar_db():
    return mysql.connector.connect(
        host="localhost", 
        user="root",
        password="Colombia2024",
        database="crud_python"
    )

# Crear usuario
def crear_usuario():
    conn = conectar_db()
    cursor = conn.cursor()

    nombre = simpledialog.askstring("Entrada", "Ingrese el nombre:")
    edad = simpledialog.askinteger("Entrada", "Ingrese la edad:")

    if nombre and edad:
        cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", (nombre, edad))
        conn.commit()
        messagebox.showinfo("Éxito", "Usuario registrado correctamente.")

    conn.close()

# Leer usuarios
def leer_usuarios():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    registros = cursor.fetchall()
    
    usuarios = "\n".join([f"ID: {r[0]}, Nombre: {r[1]}, Edad: {r[2]}" for r in registros])
    messagebox.showinfo("Usuarios Registrados", usuarios if usuarios else "No hay usuarios.")

    conn.close()

# Actualizar usuario
def actualizar_usuario():
    conn = conectar_db()
    cursor = conn.cursor()

    id_usuario = simpledialog.askinteger("Entrada", "Ingrese el ID del usuario a actualizar:")
    nuevo_nombre = simpledialog.askstring("Entrada", "Ingrese el nuevo nombre:")
    nueva_edad = simpledialog.askinteger("Entrada", "Ingrese la nueva edad:")

    if id_usuario and nuevo_nombre and nueva_edad:
        cursor.execute("UPDATE usuarios SET nombre=%s, edad=%s WHERE id=%s", (nuevo_nombre, nueva_edad, id_usuario))
        conn.commit()
        messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")

    conn.close()

# Eliminar usuario
def eliminar_usuario():
    conn = conectar_db()
    cursor = conn.cursor()

    id_usuario = simpledialog.askinteger("Entrada", "Ingrese el ID del usuario a eliminar:")
    
    if id_usuario:
        cursor.execute("DELETE FROM usuarios WHERE id=%s", (id_usuario,))
        conn.commit()
        messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")

    conn.close()

# Interfaz gráfica

# creacion de la ventana
root = tk.Tk()
root.title("CRUD con Tkinter y MySQL")

# establecer el tamaño de la ventana
root.geometry("350x150") # 400 pixeles de ancho y 300 alto

# creacion de los botones
btn_crear = tk.Button(root, text="Crear Usuario", command=crear_usuario)
btn_leer = tk.Button(root, text="Leer Usuarios", command=leer_usuarios)
btn_actualizar = tk.Button(root, text="Actualizar Usuario", command=actualizar_usuario)
btn_eliminar = tk.Button(root, text="Eliminar Usuario", command=eliminar_usuario)

btn_crear.pack(pady=5)
btn_leer.pack(pady=5)
btn_actualizar.pack(pady=5)
btn_eliminar.pack(pady=5)

root.mainloop()
