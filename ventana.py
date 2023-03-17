import tkinter as tk
from PIL import ImageTk, Image

class Chistes:
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.chistes = [
            "Dios es real, a no ser que lo declares como entero.",
            "La barriga de un programador es directamente proporcional a la cantidad de información que maneja.",
            "¿Cuál es la mayor mentira de todo el universo? He leído y acepto los Términos y Condiciones",
            "¿Cuántos tipos de personas hay en el mundo? Hay 10 tipos de personas en el mundo: los que entienden el binario y los que no.",
            "¿Cuántos programadores hacen falta para cambiar una bombilla? Ninguno, porque es un problema de hardware"
        ]
        self.etiqueta_chiste = tk.Label(self.ventana, text=self.chistes[0], font=("Arial", 12))
        self.etiqueta_chiste.pack(pady=50)
        self.boton_cambiar = tk.Button(self.ventana, text="Siguiente chiste", command=self.cambiar_chistes)
        self.boton_cambiar.pack()
        self.indice_chiste = 0
    
    def cambiar_chistes(self):
        self.indice_chiste += 1
        if self.indice_chiste >= len(self.chistes):
            self.indice_chiste = 0
        self.etiqueta_chiste.config(text=self.chistes[self.indice_chiste])
 

root = tk.Tk()
root.title("Chistes")

image_frame = tk.Frame(root)
image_frame.pack(side=tk.TOP, pady=10)

image = Image.open("perromeme.png")
image = image.resize((300, 300), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(image_frame, image=photo)
image_label.pack()

title_label = tk.Label(root, text="¿Quieres ver chistes de informáticos?", font=("Arial", 16))
title_label.pack()

def abrir_ventana2():
    ventana = tk.Toplevel(root)
    ventana.title("Chistes")
    chistes = Chistes(ventana)
    chistes.etiqueta_chiste.pack()

button = tk.Button(root, text="Si", command=abrir_ventana2)
button.pack(pady=10)

root.mainloop()