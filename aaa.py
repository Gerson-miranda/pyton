import os
import tkinter as tk
from tkinter import messagebox

# Funções para desligar e reiniciar
def desligar():
    resposta = messagebox.askyesno("Desligar", "Tem certeza que deseja desligar o computador?")
    if resposta:
        if os.name == "nt":  # Windows
            os.system("shutdown /s /t 0")
        

def reiniciar():
    resposta = messagebox.askyesno("Reiniciar", "Tem certeza que deseja reiniciar o computador?")
    if resposta:
        if os.name == "nt":  # Windows
            os.system("shutdown /r /t 0")
        

# Criando a interface
janela = tk.Tk()
janela.title("Controle do PC")
janela.geometry("300x150")

# Botões
btn_desligar = tk.Button(janela, text="Desligar", command=desligar, bg="red", fg="white", width=15)
btn_desligar.pack(pady=20)

btn_reiniciar = tk.Button(janela, text="Reiniciar", command=reiniciar, bg="green", fg="white", width=15)
btn_reiniciar.pack()

janela.mainloop()
