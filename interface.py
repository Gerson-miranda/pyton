from tkinter import *
from tkinter import messagebox
def mensagem():
    # messagebox.showinfo("Mensagem","wellcome ")
    # messagebox.showerror("Mensagem","erro")  
    # messagebox.showwarning("Mensagem","Atenção")
    # resposta = messagebox.askyesno("Pergunta","Deseja continuar?")
    # if resposta:
    #     print("O usuário clicou em Sim")
    # else:
    #     print("O usuário clicou em Não")
    # resposta = messagebox.askokcancel("Pergunta","Deseja continuar?")
    resposta = messagebox.askretrycancel("Pergunta","Deseja continuar?")



menu_inicial = Tk()# Cria a janela principal
menu_inicial.title("Minha janela") # Define o título da janela
menu_inicial.geometry("500x250") # Define o tamanho inicial da janela
menu_inicial.geometry("500x250+500+200") # Define o tamanho e a posição inicial da janela
# menu_inicial.resizable(False, False) # Desabilita o redimensionamento da janela
menu_inicial.minsize(300,150) # Define o tamanho mínimo da janela
menu_inicial.maxsize(800,600)# Define o tamanho máximo da janela
# menu_inicial.state("iconic") # Abre a janela minimizada
menu_inicial.state("zoomed") # Abre a janela maximizada
menu_inicial.iconbitmap("AVGAntivirus_11712.ico")
Label1 = Label(menu_inicial,text="Welcome my app",font=("Arial",20),fg="blue",bg="yellow")
Label1.pack(pady=20)

botao = Button(menu_inicial, text="Clique aqui", command= mensagem) # Cria um botão
botao.pack() # Adiciona o botão à janela



menu_inicial.mainloop()
