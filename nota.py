import tkinter as tk
from tkinter import messagebox

def verificar_nota():
    nota_texto = entry_nota.get() #Espaçamento significa que está dentro da função #Irá pegar a informação
    
    if  nota_texto.replace(".", "", 1).isdigit(): #Verifica se é número 
        nota = float(nota_texto)

        if nota == 10:
            resultado = "Parabéns nota máxima!!"
        elif nota >= 9 and nota == 9.9: 
            resultado = "Quase perfeito !!"
        elif nota >=0 and nota <= 4.9:
            resultado = "Reprovado !!"

        messagebox.showinfo("Resultado", f"Situação: {resultado}") #Titulo e informação
    else:
        messagebox.showerror("Erro", "Digite um número válido.")
    
    #Janela principal
    root = tk.Tk()
    root.title("Verificador de Nota")
    root.geometry("300x200") #Altura e largura da janela
    root.configure(bg="#F0E68C") #Fundo amarelo

    #Widgets 
    tk.Label(root, text="Digite a nota do aluno:", bg="#F0E68C", fg="black", font=("Arial", 11, "bold")).pack(pady=10)
    entry_nota = tk.Entry(root)
    entry_nota.pack(pady=5)

    tk.Button(root, text="Verificar", command=verificar_nota, bg="blue", fg="white", font=("Arial", 11, "bold")).pack(pady=15)

    root.mainloop()