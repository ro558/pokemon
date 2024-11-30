from tkinter import Tk, Frame, Label, Button, END
from tkinter import ttk
from crud.crud import select


janela = Tk()


class Tela():
    # istanciamento da classe
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frame()
        self.label()
        self.botao()
        self.atores()
        self.janela.mainloop()
        pass

    # janela do programa
    def tela(self):
        self.janela.title("Pokedex")   # título
        self.janela.geometry("750x750")
        self.janela.configure(background="white")
        self.janela.resizable(True, True)
        self.janela.maxsize(width=880, height=880)
        self.janela.minsize(width=200, height=200)

    # frames da janela
    def frame(self):
        self.frame1 = Frame(self.janela, bd=2, bg="red")
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheigh=0.10)

        self.frame2 = Frame(self.janela, bd=2, bg="white")
        self.frame2.place(relx=0.02, rely=0.10, relwidth=0.96, relheigh=0.95)

    def label(self):

        self.label1 = Label(self.frame1, text="Configuração", bg="red", font=2,
                            foreground="white")
        self.label1.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.6)

    def botao(self):

        self.pesquisar = botao1 = Button(text="Pesquisar")
        self.pesquisar = botao1.place(relx=0.30, rely=0.9, relwidth=0.1,
                                      relheight=0.05)

        botao2 = Button(text="Deletar")
        botao2.place(relx=0.55, rely=0.9, relwidth=0.1, relheight=0.05)

    def atores(self, pesquisa=False):

        self.tabela_sono = ttk.Treeview(self.janela, selectmode="browse",
                                        show="headings",
                                        columns=("id", "nome"))
        self.tabela_sono.place(rely=0.25, relx=0.2)

        self.tabela_sono.heading("id", text="id")
        self.tabela_sono.heading("nome", text="nome")

        # os registros vão ser pegos do banco de dados
        if pesquisa:
            registros = self.pesquisar()
        else:
            registros = select()
            for registro in registros:
                self.tabela_sono.insert("", END, values=registro)


if __name__ == '__main__':
    Tela()
