import customtkinter
from tkinter import messagebox

def click_Botao():

    messagebox.showinfo("Info","Botão customtkinter clicado!")


app = customtkinter.CTk()
app.geometry("400x300")
app.title("Exemplo customtkinter")
app.resizable(False,False)

label1 = customtkinter.CTkLabel(app,text="Hello customtkinter",fg_color="transparent",font=("Arial",20))
label1.pack(padx=20,pady=25)


botao = customtkinter.CTkButton(app,text="Ok")
botao.pack(pady=50,padx=25)

app.mainloop()