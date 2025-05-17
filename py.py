
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

def fatorial(n: int) -> int:
    if n < 0: return None
    if n == 0: return 1
    else:
        return n * fatorial(n-1)

def calcular_fatorial():
    try:
        numero = int(entrada_dados.get())
        resultado = fatorial(numero)
        resultado_label.config(text=f"Resultado: {resultado}")
    except ValueError:
        resultado_label.config(text="Por favor, insira um número válido")

janela = Tk()
janela.title("Fatorial")
janela.geometry("300x300")

Label(janela, text="Fatorial").pack()
entrada_dados = Entry(janela)
entrada_dados.pack()
botao = Button(janela, text="Clique aqui", command=calcular_fatorial)
botao.pack()
resultado_label = Label(janela, text="")
resultado_label.pack()

janela.mainloop()



"""
# Define a função do segundo grau
def funcao_segundo_grau(a, b, c, x):
    return a * x**2 + b * x + c

# Gera valores de x
x = np.linspace(-100, 100, 100)

# Calcula os valores de y usando a função do segundo grau
a, b, c = 1, 2, 5  # Coeficientes da função do segundo grau
y = funcao_segundo_grau(a, b, c, x)

# Plota a função do segundo grau
plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Função do Segundo Grau')
plt.legend()
plt.grid(True)
plt.show()
"""