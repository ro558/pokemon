from tkinter import Tk, Label, Entry, Button, END
from tkinter import ttk
import mysql.connector


class personagem():

    def __init__(self,):
        self.janela = Tk()
        self.atores()

        self.titulo = Label(self.janela, text='Pokedex')
        self.titulo.place(relx=0.5, rely=0.05, anchor='center')

        self.label1 = Label(self.janela, text="Nome a pesquisar:")
        self.label1.place(rely=0.15, relx=0.2)

        self.caixa1 = Entry(self.janela)
        self.caixa1.place(relx=0.2, rely=0.2)

        self.pesquisa = Button(self.janela, text='pesquisar',
                               command=self.mostrar_resultados)
        self.pesquisa.place(relx=0.5, rely=0.19)

        self.bio = Button(self.janela, text='Biografia', command=self.bio)
        self.bio.place(relx=0.5, rely=0.8, anchor='center')

        self.janela.geometry("720x480")

        self.janela.mainloop()

    def atores(self, pesquisa=False):
        self.tabela_sono = ttk.Treeview(self.janela, selectmode="browse",
                                        show="headings",
                                        columns=("id", "nome"))
        self.tabela_sono.place(rely=0.25, relx=0.2)

        self.tabela_sono.heading("id", text="Nº")
        self.tabela_sono.heading("nome", text="Nome")

        # os registros vão ser pegos do banco de dados
        if pesquisa:
            registros = self.pesquisar()
        else:
            registros = self.select()
            for registro in registros:
                self.tabela_sono.insert("", END, values=registro)

    def select(self):

        self.conect()
        self.mycursor.execute("select id, nome from tb_pokemons")
        myresult = self.mycursor.fetchall()

        self.mycursor.close()
        self.mydb.close()
        return myresult

    def conect(self):

        self.mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="Pokedex"
        )

        self.mycursor = self.mydb.cursor()

    def mostrar_resultados(self):
        self.tabela_sono.destroy()
        self.atores(True)

    def pesquisar(self):
        prompt = self.caixa1.get()
        resultados = list()
        for resultado in self.select():
            if resultado[1].startswith(prompt):
                resultados.append(resultado[1])
        return tuple(resultados)

    def bio(self):
        from view.bio import tela_biografia
        selecao = self.tabela_sono.set(self.tabela_sono.selection())
        self.tabela_sono.selection_clear()
        self.tabela_sono.place(rely=0.25, relx=0.2)
        if selecao.get('id') is None:
            return
        tela_biografia(int(selecao.get('id')))


if __name__ == '__main__':
    personagem()
