import sqlite3

conn = sqlite3.connect('memoria')

cursor = conn.cursor()


def adicionar(i):
    with conn as con:
        query = 'INSERT INTO cadastrocliente (nome, cpf, email, telefone, nascimento, estcivil) VALUES (?, ?, ?, ?, ?, ?)'
        con.execute(query, i)
        con.commit()


def exibir():
    lista = []
    with conn:
        query = 'SELECT * FROM cadastrocliente'
        infos = conn.execute(query)
        for instance in infos:
            lista.append(instance)
    return lista


def agendar(i):
    with conn as con:
        query = 'UPDATE cadastrocliente SET procedimento=?, valor=?, data=?, horario=?, obs=? WHERE nome=?'
        con.execute(query, i)
        con.commit()


def linha(lista):
    with conn as con:
        linha = 'INSERT INTO infoscliente (nome, procedimento, data, retorno, obs, valor, horario) VALUES (?, ?, ?, ?, ?, ?, ?)'
        con.execute(linha, lista)
        con.commit()


def nomes():
    lista = []
    with conn:
        query = 'SELECT nome FROM cadastrocliente'
        infos = conn.execute(query)
        for instance in infos:
            lista.append(instance)
    return lista


def procedimentos():
    lista = []
    with conn as con:
        query = 'SELECT tecnica FROM procedimentos'
        infos = conn.execute(query)
        for instance in infos:
            lista.append(instance)
    return lista


def procedimentoscompleto():
    lista = []
    with conn as con:
        query = 'SELECT * FROM procedimentos'
        infos = conn.execute(query)
        for instance in infos:
            lista.append(instance)
    return lista


def atualizarProcedimento(i):
    with conn as con:
        query = 'UPDATE procedimentos SET tecnica=?, valor=? WHERE id =?'
        con.execute(query, i)
        con.commit()


def receberValor(i):
    with conn as con:
        query = 'SELECT valor FROM procedimentos WHERE tecnica=?'
        return con.execute(query, [i]).fetchone()


def excluir(i):
    with conn as con:
        query = 'DELETE FROM procedimentos WHERE id=?'
        con.execute(query, [i])
        con.commit()


def listagemCliente(i):
    lista = []
    with conn as con:
        query = 'SELECT procedimento, data, retorno, obs FROM infoscliente WHERE nome=?'
        info = con.execute(query, i)
        for instance in info:
            lista.append(instance)
        return lista


def excluirCliente(i):
    with conn as con:
        query = 'DELETE FROM cadastrocliente WHERE id=?'
        con.execute(query, [i])
        con.commit()


def updateCliente(i):
    with conn as con:
        query = 'UPDATE cadastrocliente SET nome=?, cpf=?, email=?, telefone=?, nascimento=?, estcivil=? WHERE id=? '
        con.execute(query, i)


def updateinfos(i):
    with conn as con:
        linha = 'UPDATE infoscliente SET nome=? WHERE nome=?'
        con.execute(linha, i)


def diadehoje(i):
    lista = []
    with conn as con:
        query = 'SELECT nome, procedimento, valor, horario FROM infoscliente WHERE data=?'
        info = con.execute(query, i)
        for instance in info:
            lista.append(instance)
    return lista


def user(i):
    lista = []
    with conn as con:
        query = 'SELECT password FROM usuario WHERE user=?'
        info = con.execute(query, [i])
        for instance in info:
            lista.append(instance)
    return [item for result in lista for item in result if item]


# lin = ['tin', 'pro', 'val', 'dat', 'hor', 'Daniel Clemente']

# print(agendar(lin))

# conn.close()
