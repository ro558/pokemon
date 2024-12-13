from tkinter import Toplevel, Frame, Label, Button, Entry, END, Tk
from tkinter import ttk
from model.crud import select, delete, salvar

class Tela:
    # Instanciamento da classe
    def __init__(self, master):
        self.janela = Toplevel(master)
        self.tela()
        self.frame()
        self.label()
        self.botao()
        self.janela.mainloop()

    # Janela do programa
    def tela(self):
        self.janela.title("Pokedex")   # Título
        self.janela.geometry("750x750")
        self.janela.configure(background="white")
        self.janela.resizable(True, True)
        self.janela.maxsize(width=880, height=880)
        self.janela.minsize(width=200, height=200)

    # Frames da janela
    def frame(self):
        self.frame1 = Frame(self.janela, bd=2, bg="red")
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.10)

        self.frame2 = Frame(self.janela, bd=2, bg="white")
        self.frame2.place(relx=0.02, rely=0.10, relwidth=0.96, relheigh=0.95)

    def label(self):
        self.label1 = Label(self.frame1, text="Configuração", bg="red", font=2,
                            foreground="white")
        self.label1.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.6)

    def botao(self):
        # Botão de pesquisa
        self.botao1 = Button(self.janela, text="Pesquisar", command=self.pesquisar)
        self.botao1.place(relx=0.70, rely=0.18, relwidth=0.1, relheight=0.05)

        # Botão de deletar
        self.botao2 = Button(self.janela, text="Deletar", command=self.deletar)
        self.botao2.place(relx=0.55, rely=0.9, relwidth=0.1, relheight=0.05)

        # Botão de salvar
        self.botao3 = Button(self.janela, text="Adicionar", command=self.salvar)
        self.botao3.place(relx=0.35, rely=0.9, relwidth=0.1, relheight=0.05)

        # Labels e caixas de entrada
        self.label_nome = Label(self.janela, text="Nome:")
        self.label_nome.place(rely=0.20, relx=0.05)
        self.caixa_nome = Entry(self.janela)
        self.caixa_nome.place(relx=0.15, rely=0.20)

        self.label_tipo1 = Label(self.janela, text="Tipo 1:")
        self.label_tipo1.place(rely=0.25, relx=0.05)
        self.caixa_tipo1 = Entry(self.janela)
        self.caixa_tipo1.place(relx=0.15, rely=0.25)

        self.label_tipo2 = Label(self.janela, text="Tipo 2:")
        self.label_tipo2.place(rely=0.30, relx=0.05)
        self.caixa_tipo2 = Entry(self.janela)
        self.caixa_tipo2.place(relx=0.15, rely=0.30)

        self.label_foto = Label(self.janela, text="Foto:")
        self.label_foto.place(rely=0.35, relx=0.05)
        self.caixa_foto = Entry(self.janela)
        self.caixa_foto.place(relx=0.15, rely=0.35)

        self.label_descricao = Label(self.janela, text="Descrição:")
        self.label_descricao.place(rely=0.40, relx=0.05)
        self.caixa_descricao = Entry(self.janela)
        self.caixa_descricao.place(relx=0.15, rely=0.40)

        self.label_hp = Label(self.janela, text="HP:")
        self.label_hp.place(rely=0.45, relx=0.05)
        self.caixa_hp = Entry(self.janela)
        self.caixa_hp.place(relx=0.15, rely=0.45)

        self.label_forca = Label(self.janela, text="Força:")
        self.label_forca.place(rely=0.50, relx=0.05)
        self.caixa_forca = Entry(self.janela)
        self.caixa_forca.place(relx=0.15, rely=0.50)

        self.label_defesa = Label(self.janela, text="Defesa:")
        self.label_defesa.place(rely=0.55, relx=0.05)
        self.caixa_defesa = Entry(self.janela)
        self.caixa_defesa.place(relx=0.15, rely=0.55)

    def salvar(self):
        # Captura os valores das caixas de entrada
        nome = self.caixa_nome.get()
        tipo1 = self.caixa_tipo1.get()
        tipo2 = self.caixa_tipo2.get()
        foto = self.caixa_foto.get()
        descricao = self.caixa_descricao.get()
        hp = self.caixa_hp.get()
        forca = self.caixa_forca.get()
        defesa = self.caixa_defesa.get()

        # Chama a função 'salvar' para salvar os dados no banco
        salvar(nome, tipo1, tipo2, foto, descricao, hp, forca, defesa)

        # Limpa os campos após salvar
        self.caixa_nome.delete(0, END)
        self.caixa_tipo1.delete(0, END)
        self.caixa_tipo2.delete(0, END)
        self.caixa_foto.delete(0, END)
        self.caixa_descricao.delete(0, END)
        self.caixa_hp.delete(0, END)
        self.caixa_forca.delete(0, END)
        self.caixa_defesa.delete(0, END)

    def pesquisar(self):
        prompt = self.caixa_nome.get().capitalize()
        registros = self.select(prompt)
        self.atores(pesquisa=True, registros=registros)

    def select(self, prompt=""):
        registros = select()
        if prompt:
            return [registro for registro in registros if prompt.lower() in registro[1].lower()]
        return registros

    def deletar(self):
        registro = self.tabela_sono.set(self.tabela_sono.selection())[0]
        if registro is None:
            return
        delete(int(registro))
        self.tabela_sono.delete(*self.tabela_sono.get_children())
        self.atores()

    def atores(self, pesquisa=False, registros=None):
        self.tabela_sono = ttk.Treeview(self.janela, selectmode="browse", show="headings", columns=("id", "nome"))
        self.tabela_sono.place(rely=0.25, relx=0.2, relwidth=0.6, relheight=0.6)
        self.tabela_sono.heading("id", text="id")
        self.tabela_sono.heading("nome", text="nome")

        if pesquisa:
            registros = registros or []
        else:
            registros = select()

        for registro in registros:
            self.tabela_sono.insert("", END, values=registro)

if __name__ == '__main__':
    root = Tk()
    Tela(root)
