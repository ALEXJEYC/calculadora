import tkinter as tk
import math
from tkinter import Menu

# Función para agregar valores a la operación
def click_button(valor):
    actual = entrada_operacion.get()
    entrada_operacion.delete(0, tk.END)
    entrada_operacion.insert(tk.END, actual + valor)

# Función para limpiar las entradas
def limpiar():
    entrada_operacion.delete(0, tk.END)
    entrada_resultado.delete(0, tk.END)

# Función para calcular el resultado
def calcular():
    try:
        operacion = entrada_operacion.get()
        resultado = eval(operacion)
        entrada_resultado.delete(0, tk.END)
        entrada_resultado.insert(tk.END, str(resultado))
        agregar_historial(operacion, resultado)
    except Exception as e:
        entrada_resultado.delete(0, tk.END)
        entrada_resultado.insert(tk.END, "Error")

# Función para agregar la operación al historial
def agregar_historial(operacion, resultado):
    historial.insert(tk.END, f"{operacion} = {resultado}\n")
    historial.yview(tk.END)

# Función para cambiar el color de la calculadora
def cambiar_color(color):
    if color == 'rosado':
        color_fondo = "#FF1493"  # Rosado
        color_boton = "#FF69B4"  # Rosado claro
    elif color == 'verde':
        color_fondo = "#004d00"  # Verde oscuro
        color_boton = "#008000"  # Verde medio
    elif color == 'negro':
        color_fondo = "#000000"  # Negro
        color_boton = "#333333"  # Gris oscuro
    elif color == 'azul':
        color_fondo = "#00008B"  # Azul oscuro
        color_boton = "#1E90FF"  # Azul claro
    else:
        return

    # Actualizar colores de la ventana
    ventana.configure(bg=color_fondo)
    entrada_operacion.config(bg=color_fondo, fg="#FFFFFF", insertbackground="#FFFFFF")
    entrada_resultado.config(bg=color_fondo, fg="#FFFFFF", insertbackground="#FFFFFF")
    historial.config(bg=color_fondo, fg="#FFFFFF")
    
    # Actualizar los botones
    for boton in botones_creados:
        boton.config(bg=color_boton, fg="#FFFFFF")

# Función para mostrar el menú de cambio de color
def mostrar_menu(event):
    menu.post(event.x_root, event.y_root)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Científica")
ventana.geometry("500x600")  # Tamaño inicial de la ventana

# Fuentes y tamaños de texto para las entradas
fuente = ("Arial", 18)

# Cuadro de entrada para la operación
entrada_operacion = tk.Entry(ventana, width=35, borderwidth=5, bg="#004d00", fg="#FFFFFF", insertbackground="#FFFFFF", font=fuente)
entrada_operacion.grid(row=0, column=0, columnspan=5, padx=10, pady=5, sticky="nsew")

# Cuadro de entrada para el resultado
entrada_resultado = tk.Entry(ventana, width=35, borderwidth=5, bg="#004d00", fg="#FFFFFF", insertbackground="#FFFFFF", font=fuente)
entrada_resultado.grid(row=1, column=0, columnspan=5, padx=10, pady=5, sticky="nsew")

# Botones de la calculadora
botones = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3), ('sqrt', 2, 4), 
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3), ('sin', 3, 4),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3), ('cos', 4, 4),
    ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), ('=', 5, 3), ('tan', 5, 4),
    ('(', 6, 0), (')', 6, 1), ('log', 6, 2), ('exp', 6, 3), ('pi', 6, 4),
]

botones_creados = []
for (texto, fila, columna) in botones:
    if texto == '=':
        boton = tk.Button(ventana, text=texto, width=10, height=3, command=calcular, bg="#008000", fg="#FFFFFF", font=fuente)
    elif texto == 'sqrt':
        boton = tk.Button(ventana, text=texto, width=10, height=3, command=lambda: click_button('math.sqrt('), bg="#008000", fg="#FFFFFF", font=fuente)
    elif texto == 'sin':
        boton = tk.Button(ventana, text=texto, width=10, height=3, command=lambda: click_button('math.sin('), bg="#008000", fg="#FFFFFF", font=fuente)
    elif texto == 'cos':
        boton = tk.Button(ventana, text=texto, width=10, height=3, command=lambda: click_button('math.cos('), bg="#008000", fg="#FFFFFF", font=fuente)
    elif texto == 'tan':
        boton = tk.Button(ventana, text=texto, width=10, height=3, command=lambda: click_button('math.tan('), bg="#008000", fg="#FFFFFF", font=fuente)
    elif texto == 'log':
        boton = tk.Button(ventana, text=texto, width=10, height=3, command=lambda: click_button('math.log('), bg="#008000", fg="#FFFFFF", font=fuente)
    elif texto == 'exp':
        boton = tk.Button(ventana, text=texto, width=10, height=3, command=lambda: click_button('math.exp('), bg="#008000", fg="#FFFFFF", font=fuente)
    elif texto == 'pi':
        boton = tk.Button(ventana, text=texto, width=10, height=3, command=lambda: click_button('math.pi'), bg="#008000", fg="#FFFFFF", font=fuente)
    else:
        boton = tk.Button(ventana, text=texto, width=10, height=3, command=lambda t=texto: click_button(t), bg="#008000", fg="#FFFFFF", font=fuente)
    boton.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")
    botones_creados.append(boton)

# Botón para limpiar
boton_limpiar = tk.Button(ventana, text='C', width=10, height=3, command=limpiar, bg="#008000", fg="#FFFFFF", font=fuente)
boton_limpiar.grid(row=7, column=0, columnspan=5, padx=10, pady=5, sticky="nsew")

# Área de texto para el historial
historial = tk.Text(ventana, height=10, width=50, bg="#004d00", fg="#FFFFFF", state='normal', font=fuente)
historial.grid(row=8, column=0, columnspan=5, padx=10, pady=5, sticky="nsew")

# Crear un menú desplegable para los colores
menu = Menu(ventana, tearoff=0)
menu.add_command(label="Rosado", command=lambda: cambiar_color('rosado'))
menu.add_command(label="Verde", command=lambda: cambiar_color('verde'))
menu.add_command(label="Negro", command=lambda: cambiar_color('negro'))
menu.add_command(label="Azul", command=lambda: cambiar_color('azul'))

# Botón para abrir el menú de cambio de color
boton_color = tk.Button(ventana, text="Cambiar Color", width=20, height=3, font=fuente)
boton_color.grid(row=9, column=0, columnspan=5)
boton_color.bind("<Button-1>", mostrar_menu)

# Hacer que los widgets se ajusten cuando se cambia el tamaño de la ventana
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_rowconfigure(1, weight=1)
ventana.grid_rowconfigure(2, weight=1)
ventana.grid_rowconfigure(3, weight=1)
ventana.grid_rowconfigure(4, weight=1)
ventana.grid_rowconfigure(5, weight=1)
ventana.grid_rowconfigure(6, weight=1)
ventana.grid_rowconfigure(7, weight=1)
ventana.grid_rowconfigure(8, weight=1)

ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_columnconfigure(2, weight=1)
ventana.grid_columnconfigure(3, weight=1)
ventana.grid_columnconfigure(4, weight=1)

# Ejecutar la ventana
ventana.mainloop()
