from tkinter import Tk, Label, Button, CENTER, mainloop


def destruir():
    global visualizar, gerenciar
    visualizar.destroy()
    gerenciar.destroy()


def gerir():
    from view.código_tela_de_adicionamento import Tela
    destruir()
    Tela()


def ver():
    from view.personagens import personagens
    destruir()
    personagem()


if __name__ == '__main__':
    master = Tk()
    master.geometry('720x480')

    titulo = Label(master, text='Pokedex')
    titulo.pack()

    gerenciar = Button(master, text='Tela de CRUD', command=None)
    gerenciar.place(relx=0.3, rely=0.5, anchor=CENTER)

    visualizar = Button(master, text='Ver pokemons', command=None)
    visualizar.place(relx=0.7, rely=0.5, anchor=CENTER)

    mainloop()
