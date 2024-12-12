from model.conn import connection


def salvar(nome, tipo1, tipo2, foto, descricao, hp, forca, defesa):
    mydb, mycursor = connection()
    sql = "INSERT INTO tb_pokemons (nome,tipo1,tipo2,foto,descricao,hp,forca,defesa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (nome, tipo1, tipo2, foto, descricao, hp, forca, defesa)
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "cadastro feito com sucesso")

    # Fechar a conexão
    mycursor.close()
    mydb.close()


def select():
    try:
        mydb, mycursor = connection()
        mycursor.execute("SELECT * FROM tb_pokemons")
        resultado = mycursor.fetchall()
        return resultado
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        return []
    finally:
        mycursor.close()
        mydb.close()


def delete(id):
    mydb, mycursor = connection()
    sql = "DELETE FROM tb_pokemons WHERE id = %s"
    mycursor.execute(sql, (id,))
    mydb.commit()

    print(f"{mycursor.rowcount} registro(s) deletado(s) com sucesso")

    mycursor.close()
    mydb.close()


def update(identificador, campos, valores):
    mydb, mycursor = connection()
    if len(campos) != len(valores) or not campos or not valores:
        print("erro, tamanho dos campos difere dos valores")
        return

    # Forma mais eficiente de construir os parâmetros SQL
    parametros_sql = ', '.join(f"{campo} = %s" for campo in campos)
    sql = f"UPDATE tb_pokemons SET {parametros_sql} WHERE id = %s"

    # Inclui o identificador no final dos valores
    valores.append(identificador)

    mycursor.execute(sql, valores)
    mydb.commit()
    mycursor.close()
    mydb.close()


def lista():
    mydb, mycursor = connection()

    mycursor.execute("SELECT * FROM tb_pokemons")  # Corrigido para a tabela correta

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    
    mycursor.close()
    mydb.close()

