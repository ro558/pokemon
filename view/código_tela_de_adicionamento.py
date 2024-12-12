from tkinter import Toplevel, Frame, Label, Button, Entry, END
from tkinter import ttk
from model.crud import select, delete

class Tela:
    # Instanciamento da classe
    def __init__(self, master):
        self.janela = Toplevel(master)
        self.tela()
        self.frame()
        self.label()
        self.botao(select, delete)
        self.atores()
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
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheigh=0.10)

        self.frame2 = Frame(self.janela, bd=2, bg="white")
        self.frame2.place(relx=0.02, rely=0.10, relwidth=0.96, relheigh=0.95)

    def label(self):
        self.label1 = Label(self.frame1, text="Configuração", bg="red", font=2,
                            foreground="white")
        self.label1.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.6)

    def botao(self, select, delete):
        self.botao1 = Button(self.janela, text="Pesquisar", command=select)
        self.botao1.place(relx=0.30, rely=0.9, relwidth=0.1, relheight=0.05)

        self.botao2 = Button(self.janela, text="Deletar", command=self.deletar)
        self.botao2.place(relx=0.55, rely=0.9, relwidth=0.1, relheight=0.05)

        
        self.label1 = Label(self.janela, text="Digite o nome:")
        self.label1.place(rely=0.15, relx=0.2)

        self.caixa1 = Entry(self.janela)
        self.caixa1.place(relx=0.2, rely=0.2)



    def pesquisar(self):
        prompt = self.caixa1.get().capitalize()
        resultados = list()
        for resultado in self.select():
            if resultado[1].startswith(prompt):
                resultados.append(resultado)
        return tuple(resultados)



    def deletar(self):
        registro = self.tabela_sono.set(self.tabela_sono.selection()).get('id')
        if registro is None:
            return
        delete(int(registro))
        self.tabela_sono.delete(*self.tabela_sono.get_children())  # Limpa a tabela
        self.atores()  # Recarrega a tabela

    def atores(self, pesquisa=False):
        self.tabela_sono = ttk.Treeview(self.janela, selectmode="browse",
                                        show="headings", columns=("id", "nome"))
        self.tabela_sono.place(rely=0.25, relx=0.2, relwidth=0.6, relheight=0.6)

        self.tabela_sono.heading("id", text="id")
        self.tabela_sono.heading("nome", text="nome")

        # Os registros vão ser pegos do banco de dados
        registros = select() if not pesquisa else self.pesquisar()
        for registro in registros:
            self.tabela_sono.insert("", END, values=registro)

        if pesquisa:
            registros = self.pesquisar()
        else:
            registros = self.select()
        for registro in registros:
            self.tabela_sono.insert("", END, values=registro)


if __name__ == '__main__':
    root = Tk()  # Você precisa de uma instância da janela principal
    Tela(root)

