#!/usr/bin/env python3

import random
import tkinter as tk

def generar_numeros():
    numeros = set()
    while len(numeros) < 1:
        miles = random.randint(1, 9) * 1000
        cientos = random.randint(0, 9) * 100
        decenas_unidades = random.choice([25, 50, 75])
        numero = miles + cientos + decenas_unidades
        if numero not in numeros:
            numeros.add(numero)
    return list(numeros)

def calcular_blackjack(x):
    y = x + (x / 2)
    return y

def generar_y_mostrar_numeros():
    global numeros_aleatorios
    numeros_aleatorios = generar_numeros()
    resultado_numeros.set(f"X: {numeros_aleatorios}")

def mostrar_blackjack():
    if numeros_aleatorios:
        blackjack_valores = [calcular_blackjack(num) for num in numeros_aleatorios]
        resultado_blackjack.set(f"BJ: {blackjack_valores}")
    else:
        resultado_blackjack.set("Primero, genera los números aleatorios.")

def borrar_resultados():
    resultado_numeros.set("")
    resultado_blackjack.set("")
    global numeros_aleatorios
    numeros_aleatorios = []

# Configuración de la GUI
root = tk.Tk()
root.title("Generador de Blackjack")
root.geometry("500x500")


numeros_aleatorios = []

resultado_numeros = tk.StringVar()
resultado_blackjack = tk.StringVar()

label_resultado_numeros = tk.Label(root, textvariable=resultado_numeros)
label_resultado_numeros.pack(pady=10)

label_resultado_blackjack = tk.Label(root, textvariable=resultado_blackjack)
label_resultado_blackjack.pack(pady=10)

boton_generar = tk.Button(root, text="X=", command=generar_y_mostrar_numeros)
boton_generar.pack(pady=10)

boton_blackjack = tk.Button(root, text="BJ", command=mostrar_blackjack)
boton_blackjack.pack(pady=10)

boton_borrar = tk.Button(root, text="UP", command=borrar_resultados)
boton_borrar.pack(pady=10)

root.mainloop()