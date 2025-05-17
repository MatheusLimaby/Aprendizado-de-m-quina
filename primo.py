from tkinter import * 
import math
def primo(x: int) -> bool:
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0:
            return False
    return True
def Verificar_Primo():
    try:
        numero = int(entrada_dados.get())
        resultado = primo(numero)
        resultado_label.config(text=f"Resultado: {resultado}")
    except ValueError:
        resultado_label.config(text="Por favor, insira um número válido")

janela = Tk()
janela.title("Primo")
janela.geometry("300x300")

Label(janela, text="Teste - Primo").pack()
entrada_dados = Entry(janela)
entrada_dados.pack()
botao = Button(janela, text="Clique aqui", command=Verificar_Primo)
botao.pack()
resultado_label = Label(janela, text="")
resultado_label.pack()

janela.mainloop()

print(primo(7))