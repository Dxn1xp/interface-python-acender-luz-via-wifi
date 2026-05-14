import requests
import tkinter as tk


try:
   
    def ligar_luz():
        requests.get('http://192.168.0.175/ligar')

except:
    print("Erro ao conectar com o dispositivo.")


try:

    def desligar_luz():
        requests.get('http://192.168.0.175/desligar')


except:
    print("Erro ao conectar com o dispositivo.")

#VISUAL-------------------------------------------


janela = tk.Tk()
janela.title("Controle de Luz")
janela.geometry("400x300")
janela.config(bg="black")  #bg = background

texto = tk.Label(
    janela,
    text="Controle de Luz",
    font=("Arial", 20),
    bg="black",
    fg="white"
)

botao = tk.Button(
    janela,
    text="Ligar Luz",
    font=("Arial", 16),
    bg="green",
    fg="white",
    command=ligar_luz
)

botao.pack(pady=20)  #Espaço


botao2 = tk.Button(
    janela,
    text="Desligar Luz",
    font=("Arial", 16),
    bg="red",
    fg="white",
    command=desligar_luz
)

botao2.pack(pady=20)  #Espaço

janela.mainloop() #MAINLOOP chama a interface e o programa fica rodando até o usuário fechar a janela