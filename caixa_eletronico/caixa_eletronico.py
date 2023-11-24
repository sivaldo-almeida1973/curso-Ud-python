from tkinter import *

from PIL import Image, ImageTk


janela = Tk()

janela.title('Caixa Eletrônico')
janela.geometry('500x380')
janela.configure(bg='blue')#cor de fundo da tela
#enfeitar janela

saldoAtual = 5000

#nome = input('Nome:')
nome = 'Bart'

introducao = Label(janela, text=f'Bem_vindo(a) ao caixa eletrônico , senhor(a) {nome.title()}', font=1)
introducao.grid(column=1, row=2, padx=5, pady=10)#indica a posicao desse elemento

img = ImageTk.PhotoImage(Image.open('bancoImagem.png'))
imagem = Label(janela, image=img)
imagem.grid(colum=1, row=2)

janela.mainloop()

