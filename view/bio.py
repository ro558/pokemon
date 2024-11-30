import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from mysql.connector import connect

# Função principal para criar a tela
def tela_biografia(numero: int):
    banco = connect(host='localhost', user='root', password='', database='Pokedex')
    cursor = banco.cursor()
    cursor.execute('select * from tb_pokemons where id = ' + str(numero))
    dados = cursor.fetchall()
    cursor.close()
    banco.close()
    del cursor, banco

    janela = tk.Tk()
    janela.title("𝚋𝚒𝚘𝚐𝚛𝚊𝚏𝚒𝚊")
    janela.geometry("600x500")

    # Título centralizado
    titulo = tk.Label(janela, text="𝚋𝚒𝚘𝚐𝚛𝚊𝚏𝚒𝚊", font=("Helvetica", 24), fg="#f0f0f0", bg="black")
    janela.config(bg="black")
    titulo.pack(pady=20)  # Adiciona título com margem

    # Tentar carregar imagem
    try:
        print(dados[0][4])
        imagem = PhotoImage(file=dados[0][4])  # Substitua "imagem.png" pelo caminho da imagem
        imagem_label = tk.Label(janela, image=imagem)
        imagem_label.image = imagem  # Manter referência à imagem
        imagem_label.pack(pady=10)  # Exibe imagem abaixo do título
    except Exception as e:
        messagebox.showwarning("Erro", "A imagem não pôde ser carregada!")  # Exibe um aviso se a imagem não for carregada

    # Texto da biografia alinhado à direita
    biografia_texto = dados[-1]

    biografia_label = tk.Label(janela, text=biografia_texto, font=("Helvetica", 10), justify="left", fg="red", bg="black", wraplength=500)
    biografia_label.pack(side="right", padx=20, pady=10, anchor="e")  # Alinha à direita e adiciona margem

    # Frame para o botão de fechar
    fechar_frame = tk.Frame(janela, bg="black")  # Criar um frame com fundo preto
    fechar_frame.pack(side="bottom", pady=20, fill="x")  # Posicionar na parte inferior, ocupando toda a largura

    # Botão "Fechar" centralizado dentro do frame
    fechar_btn = tk.Button(fechar_frame, text="Fechar", command=janela.quit, font=("Helvetica", 14))
    fechar_btn.pack()  # Centraliza o botão dentro do frame

    # Executar a janela
    janela.mainloop()

# Chama a função para mostrar a janela
if __name__ == '__main__':
    tela_biografia(1)
