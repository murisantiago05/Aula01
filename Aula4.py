from tkinter import *

def clique():
    texto.configure(text="ligado")

janela = Tk() 
janela.title("Minha Janela")

#janela.iconbitmap("caminha/para/o/arquivo.ico")

janela.geometry("400x300")
janela.resizable(True,True)

texto = Label(janela, text = "Desligado")
texto.pack()
botao = Button(janela, text= "Ligar", command=clique)
botao.pack()

janela.mainloop()




