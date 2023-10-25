import tkinter as tk
from tkinter import messagebox

# Dicionário para armazenar os livros
livros = {}

# Função para cadastrar livros
def cadastrar_livro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    disponiveis = entry_disponiveis.get()

    if not titulo or not autor or not disponiveis:
        messagebox.showwarning("Erro", "Preencha todos os campos.")
    else:
        try:
            disponiveis = int(disponiveis)
            if disponiveis > 0:
                if titulo in livros:
                    livros[titulo][1] += disponiveis
                else:
                    livros[titulo] = [autor, disponiveis]
                entry_titulo.delete(0, tk.END)
                entry_autor.delete(0, tk.END)
                entry_disponiveis.delete(0, tk.END)
                messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso.")
            else:
                messagebox.showwarning("Erro", "O número de exemplares deve ser maior que zero.")
        except ValueError:
            messagebox.showwarning("Erro", "O número de exemplares deve ser um valor válido.")

# Função para pesquisar livros
def pesquisar_livro():
    termo = entry_pesquisa.get()
    resultados.delete(0, tk.END)

    if not termo:
        messagebox.showwarning("Erro", "Digite um título ou autor para pesquisa.")
    else:
        for titulo, (autor, disponiveis) in livros.items():
            if termo.lower() in titulo.lower() or termo.lower() in autor.lower():
                resultados.insert(tk.END, f"Título: {titulo} - Autor: {autor} - Disponíveis: {disponiveis}")

# Configuração da janela
root = tk.Tk()
root.title("Catálogo de Livros")

# Labels
label_titulo = tk.Label(root, text="Título do Livro:")
label_autor = tk.Label(root, text="Autor:")
label_disponiveis = tk.Label(root, text="Exemplares Disponíveis:")
label_pesquisa = tk.Label(root, text="Pesquisar por Título ou Autor:")

# Entradas
entry_titulo = tk.Entry(root)
entry_autor = tk.Entry(root)
entry_disponiveis = tk.Entry(root)
entry_pesquisa = tk.Entry(root)

# Botões
botao_cadastrar = tk.Button(root, text="Cadastrar Livro", command=cadastrar_livro)
botao_pesquisar = tk.Button(root, text="Pesquisar Livros", command=pesquisar_livro)

# Lista de resultados
resultados = tk.Listbox(root, width=50, height=10)

# Posicionamento na janela
label_titulo.grid(row=0, column=0)
entry_titulo.grid(row=0, column=1)
label_autor.grid(row=1, column=0)
entry_autor.grid(row=1, column=1)
label_disponiveis.grid(row=2, column=0)
entry_disponiveis.grid(row=2, column=1)
botao_cadastrar.grid(row=3, column=0, columnspan=2)
label_pesquisa.grid(row=4, column=0)
entry_pesquisa.grid(row=4, column=1)
botao_pesquisar.grid(row=5, column=0, columnspan=2)
resultados.grid(row=6, column=0, columnspan=2)

root.mainloop()