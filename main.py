from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
from banco import *
from datetime import date

janela = Tk()
janela.geometry('400x500')
janela.title('SISTEMA GERAL ESPAÇO DE BELEZA JU MARQUES')
janela.resizable(False, False)
janela.configure(bg='#ffffff')

# menu de opções


def login():
    usuario = e_usuario.get()
    senha = [e_senha.get()]
    key = user(usuario)
    if senha == key:
        return menu()
    else:
        return messagebox.showerror('Erro', 'USUARIO OU SENHA INCORRETOS')


def menu():
    janela.destroy()
    menu = Tk()
    menu.title('SISTEMA GERAL ESPAÇO DE BELEZA JU MARQUES')
    menu.geometry('900x500')
    menu.resizable(False, False)
    menu.configure(bg='#f9f9f9')

    def botao_tecnica(event):
        frame_tecnica = Frame(menu)
        frame_tecnica = Frame(menu, width=829, height=430,
                              bg='#f9f9f9', relief='flat')
        frame_tecnica.place(x=170, y=70)
        styl = ttk.Style()
        styl.configure('roxo.TSeparator', background='#7b4f86',)
        ttk.Separator(menu, takefocus=0, orient=HORIZONTAL, style='roxo.TSeparator', ).place(
            x=10, y=70, relwidth=0.97, relheight=0.005)

        ttk.Separator(menu, takefocus=0, orient=HORIZONTAL,
                      ).place(x=10, y=280, relwidth=0.18,)

        ttk.Separator(menu, takefocus=0, orient=VERTICAL,
                      ).place(x=170, y=75, relheight=1)

        lista = procedimentoscompleto()

        threeview_procedimentos = ttk.Treeview(frame_tecnica, columns=(
            'id', 'Tecnica', 'valor'), show='headings', height=20)
        threeview_procedimentos.column('id', minwidth=0, width=36)
        threeview_procedimentos.column('Tecnica', minwidth=0, width=336)
        threeview_procedimentos.column('valor', minwidth=0, width=336)
        threeview_procedimentos.heading('id', text='ID')
        threeview_procedimentos.heading('Tecnica', text='PROCEDIMENTO')
        threeview_procedimentos.heading('valor', text='VALOR')
        threeview_procedimentos.pack()

        for instance in lista:
            threeview_procedimentos.insert("", "end", values=(
                instance))

        def atualizacao(event):

            treev_dados = threeview_procedimentos.focus()
            treev_dicionario = threeview_procedimentos.item(treev_dados)
            tree_lista = treev_dicionario['values']

            if tree_lista != '':
                frame_atualizacao = Frame(menu)
                frame_atualizacao = Frame(menu, width=829, height=430,
                                          bg='#f9f9f9', relief='flat')
                frame_atualizacao.place(x=170, y=70)
                styl = ttk.Style()
                styl.configure('roxo.TSeparator', background='#7b4f86',)
                ttk.Separator(menu, takefocus=0, orient=HORIZONTAL, style='roxo.TSeparator', ).place(
                    x=10, y=70, relwidth=0.97, relheight=0.005)

                ttk.Separator(menu, takefocus=0, orient=HORIZONTAL,
                              ).place(x=10, y=280, relwidth=0.18,)

                ttk.Separator(menu, takefocus=0, orient=VERTICAL,
                              ).place(x=170, y=75, relheight=1)

                valor_id = tree_lista[0]

                l_procedimento = Label(frame_atualizacao, text='Tecnica',
                                       bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
                l_procedimento.place(x=20, y=20)

                e_procedimento = Entry(frame_atualizacao, relief='solid', width=40,
                                       justify='left', font=('Ivy 10'))
                e_procedimento.place(x=20, y=50, height=25)

                l_valor = Label(frame_atualizacao, text='Valor',
                                bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
                l_valor.place(x=20, y=90)

                e_valor = Entry(frame_atualizacao, relief='solid', width=40,
                                justify='left', font=('Ivy 10'))
                e_valor.place(x=20, y=120, height=25)

                e_procedimento.insert(0, tree_lista[1])
                e_valor.insert(0, tree_lista[2])

                def atualizarTecnica():

                    tecnica = e_procedimento.get()
                    preco = e_valor.get()

                    listaatt = [tecnica, preco, valor_id]

                    if tecnica == '':
                        messagebox.showerror(
                            'ERRO', 'Preencha a tecnica por favor')
                    else:
                        atualizarProcedimento(listaatt)
                        messagebox.showinfo(
                            'Atualizado', 'procedimentos atualizado com sucesso')
                        botao_tecnica(event)

                b_alterar = Button(frame_atualizacao, text='ALTERAR', width=29, height=2,
                                   font=('Ivy 10 bold'), bg='#45075d', fg='white', relief='raised', overrelief='ridge', command=atualizarTecnica)
                b_alterar.place(x=20, y=190)
            else:
                messagebox.showerror('Erro', 'Nenhuma tecnica selecionada')

        b_atualizar = Label(master=menu, text='⟲ ATUALIZAR', anchor=NW,
                            font=('Ivy 16 '), bg='#f9f9f9', fg='#9f71ab')
        b_atualizar.place(x=10, y=290)
        b_atualizar.bind('<Button-1>', atualizacao)

        def deletarProcedimento(event):
            treev_dados = threeview_procedimentos.focus()
            treev_dicionario = threeview_procedimentos.item(treev_dados)
            tree_lista = treev_dicionario['values']

            if tree_lista != '':
                valorid = tree_lista[0]
                excluir(valorid)
                messagebox.showinfo('Excluido', 'Procedimento excluido')
                botao_tecnica(event)

            else:
                messagebox.showerror('Erro', 'Nenhum procedimento selecionado')

        b_excluir = Label(master=menu, text='⨂ EXCLUIR', anchor=NW,
                          font=('Ivy 16 '), bg='#f9f9f9', fg='#9f71ab')
        b_excluir.place(x=10, y=330)
        b_excluir.bind('<Button-1>', deletarProcedimento)

    def botao_agendar(event):
        frame_agendar = Frame(menu)
        frame_agendar = Frame(menu, width=829, height=430,
                              bg='#f9f9f9', relief='flat')
        frame_agendar.place(x=170, y=70)
        styl = ttk.Style()
        styl.configure('roxo.TSeparator', background='#7b4f86',)
        ttk.Separator(menu, takefocus=0, orient=HORIZONTAL, style='roxo.TSeparator', ).place(
            x=10, y=70, relwidth=0.97, relheight=0.005)

        ttk.Separator(menu, takefocus=0, orient=HORIZONTAL,
                      ).place(x=10, y=280, relwidth=0.18,)

        ttk.Separator(menu, takefocus=0, orient=VERTICAL,
                      ).place(x=170, y=75, relheight=1)

        lista = nomes()

        l_cliente = Label(frame_agendar, text='Cliente',
                          bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
        l_cliente.place(x=20, y=20)

        c_cliente = ttk.Combobox(
            frame_agendar, font=('Ivy 12'), state='readonly', width=30)
        c_cliente['values'] = [
            item for result in lista for item in result if item]

        c_cliente.place(x=20, y=50)

        listaprocedimento = procedimentos()

        l_procedimento = Label(frame_agendar, text='Procedimento',
                               bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
        l_procedimento.place(x=320, y=20)

        l_data = Label(frame_agendar, text='Data',
                       bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
        l_data.place(x=20, y=90)

        e_data = DateEntry(
            frame_agendar, width=17, background='#c0c3c8', foreground='white', borderwidth=2, year=2023, month=1, day=1, date_pattern="m/d/y")
        e_data.place(x=20, y=120, height=25)

        l_valor = Label(frame_agendar, text='Valor',
                        bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
        l_valor.place(x=188, y=90)

        l_obs = Label(frame_agendar, text='Observação',
                      bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
        l_obs.place(x=320, y=90)

        e_obs = Entry(frame_agendar, relief='solid', width=41,
                      font=('Ivy 10'))
        e_obs.place(x=320, y=120, height=150)

        l_horario = Label(frame_agendar, text='Horario',
                          bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
        l_horario.place(x=20, y=160)

        horarios = ['08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30',
                    '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00']

        c_horario = ttk.Combobox(
            frame_agendar, font=('Ivy 12'), state='readonly', width=11)
        c_horario['values'] = horarios

        c_horario.place(x=20, y=190)

        l_sugdata = Label(frame_agendar, text='Retorno',
                          bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
        l_sugdata.place(x=188, y=160)

        e_sugdata = DateEntry(frame_agendar, width=17, background='#c0c3c8', foreground='white',
                              borderwidth=2, year=2023, month=1, day=1, date_pattern="m/d/y")
        e_sugdata.place(x=188, y=190, height=25)

        def setvalor(val):
            e_valor.delete(0, 'end')
            recprocedimento = c_procedimento.get()
            recvalor = [receberValor(recprocedimento)]
            e_valor.insert(
                0, recvalor)

        val = StringVar()
        val.trace('w', lambda name, index, mode, val=val: setvalor(val))

        c_procedimento = ttk.Combobox(
            frame_agendar, font=('Ivy 12'), state='readonly', width=30, textvariable=val)

        c_procedimento['values'] = [
            item for result in listaprocedimento for item in result if item]
        c_procedimento.place(x=320, y=50)

        e_valor = Entry(frame_agendar, relief='solid', width=17,
                        justify='left', font=('Ivy 10'))
        e_valor.place(x=188, y=120, height=25)

        def registrar():
            if c_cliente.get() == '':
                messagebox.showerror('ERRO', 'Preencha o nome por favor')
            else:

                listaRegistro = c_procedimento.get(
                ), e_valor.get(), e_data.get_date(), c_horario.get(), e_obs.get(), c_cliente.get()

                linhaRegistrada = c_cliente.get(), c_procedimento.get(
                ), e_data.get_date(), e_sugdata.get_date(), e_obs.get(), e_valor.get(), c_horario.get()

                agendar(listaRegistro)
                linha(linhaRegistrada)

                messagebox.showinfo('REGISTRADO', 'Registrado com sucesso!')
                c_cliente.set('')
                c_procedimento.set('')
                e_data.delete(0, 'end')
                e_valor.delete(0, 'end')
                e_obs.delete(0, 'end')

        b_registrar = Button(frame_agendar, text='AGENDAR', width=29, height=2,
                             font=('Ivy 10 bold'), bg='#45075d', fg='white', relief='raised', overrelief='ridge', command=registrar)
        b_registrar.place(x=20, y=240)

    def botao_cliente(event):
        frame_cliente = Frame(menu)
        frame_cliente = Frame(menu, width=829, height=430,
                              bg='#f9f9f9', relief='flat')
        frame_cliente.place(x=170, y=70)
        styl = ttk.Style()
        styl.configure('roxo.TSeparator', background='#7b4f86',)
        ttk.Separator(menu, takefocus=0, orient=HORIZONTAL, style='roxo.TSeparator', ).place(
            x=10, y=70, relwidth=0.97, relheight=0.005)

        ttk.Separator(menu, takefocus=0, orient=HORIZONTAL,
                      ).place(x=10, y=280, relwidth=0.18,)

        ttk.Separator(menu, takefocus=0, orient=VERTICAL,
                      ).place(x=170, y=75, relheight=1)

        threeview_cliente = ttk.Treeview(frame_cliente, columns=(
            'id', 'Cliente', 'CPF', 'Email', 'Telefone', 'DT. Nascimento', 'EST. Civil'), show='headings', height=20)
        threeview_cliente.column('id', minwidth=0, width=19)
        threeview_cliente.column('Cliente', minwidth=0, width=100)
        threeview_cliente.column('CPF', minwidth=0, width=100)
        threeview_cliente.column('Email', minwidth=0, width=137)
        threeview_cliente.column('Telefone', minwidth=0, width=118)
        threeview_cliente.column('DT. Nascimento', minwidth=0, width=118)
        threeview_cliente.column('EST. Civil', minwidth=0, width=118)
        threeview_cliente.heading('id', text='ID')
        threeview_cliente.heading('Cliente', text='CLIENTE')
        threeview_cliente.heading('CPF', text='CPF')
        threeview_cliente.heading('Email', text='EMAIL')
        threeview_cliente.heading('Telefone', text='TELEFONE')
        threeview_cliente.heading('DT. Nascimento', text='DT. NASCIMENTO')
        threeview_cliente.heading('EST. Civil', text='EST. Civil')
        threeview_cliente.pack()

        lista = exibir()
        for item in lista:
            threeview_cliente.insert('', 'end', values=item)

        # aqui a desgraça acontece

        def dadosClilente(event):
            treev_dados = threeview_cliente.focus()
            treev_dicionario = threeview_cliente.item(treev_dados)
            tree_lista = treev_dicionario['values']

            if tree_lista != '':
                frame_dados = Frame(menu)
                frame_dados = Frame(menu, width=829, height=430,
                                    bg='#f9f9f9', relief='flat')
                frame_dados.place(x=170, y=70)
                styl = ttk.Style()
                styl.configure('roxo.TSeparator', background='#7b4f86',)
                ttk.Separator(menu, takefocus=0, orient=HORIZONTAL, style='roxo.TSeparator', ).place(
                    x=10, y=70, relwidth=0.97, relheight=0.005)

                ttk.Separator(menu, takefocus=0, orient=HORIZONTAL,
                              ).place(x=10, y=280, relwidth=0.18,)

                ttk.Separator(menu, takefocus=0, orient=VERTICAL,
                              ).place(x=170, y=75, relheight=1)

                valor_id = tree_lista[0]

                l_cliente = Label(frame_dados, text=tree_lista[1],
                                  bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
                l_cliente.place(x=30, y=20)

                l_nascimento = Label(frame_dados, text=tree_lista[5],
                                     bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
                l_nascimento.place(x=230, y=20)

                # b_avaliacao = Label(frame_dados, text='Ficha de Avaliação',
                #                  bg='#f9f9f9', font=('Ivy 12 bold'), fg='#414141')
                #b_avaliacao.place(x=430, y=20)
                #b_avaliacao.bind('<Button-1>', )

                frame_procedimentos = Frame(menu)
                frame_procedimentos = Frame(menu, width=525, height=230,
                                            bg='#f0f0f0', relief='flat')
                frame_procedimentos.place(x=200, y=120)
                threeview_procedimento = ttk.Treeview(frame_procedimentos, columns=(
                    'Procedimento', 'Data', 'Retorno', 'Obs'), show='headings', height=15)
                threeview_procedimento.column(
                    'Procedimento', minwidth=0, width=200)
                threeview_procedimento.column('Data', minwidth=0, width=100)
                threeview_procedimento.column('Retorno', minwidth=0, width=100)
                threeview_procedimento.column('Obs', minwidth=0, width=200)
                threeview_procedimento.heading(
                    'Procedimento', text='PROCEDIMENTO')
                threeview_procedimento.heading('Data', text='DATA')
                threeview_procedimento.heading('Retorno', text='RETORNO')
                threeview_procedimento.heading('Obs', text='Observações')
                threeview_procedimento.pack()

                recProcedimento = listagemCliente([tree_lista[1]])
                for item in recProcedimento:
                    threeview_procedimento.insert('', 'end', values=item)

            else:
                messagebox.showerror('Erro', 'Nenhum cliente selecionado')

        def deletarCliente(event):
            treev_dados = threeview_cliente.focus()
            treev_dicionario = threeview_cliente.item(treev_dados)
            tree_lista = treev_dicionario['values']

            if tree_lista != '':
                valorid = tree_lista[0]
                excluirCliente(valorid)
                messagebox.showinfo('Excluido', 'Cliente excluido com sucesso')
                botao_cliente(event)
            else:
                messagebox.showerror('Erro', 'Nenhum cliente selecionado')

        def attCliente(event):

            treev_dados = threeview_cliente.focus()
            treev_dicionario = threeview_cliente.item(treev_dados)
            tree_lista = treev_dicionario['values']

            if tree_lista != '':
                frame_atualizacao = Frame(menu)
                frame_atualizacao = Frame(menu, width=829, height=430,
                                          bg='#f9f9f9', relief='flat')
                frame_atualizacao.place(x=170, y=70)
                styl = ttk.Style()
                styl.configure('roxo.TSeparator', background='#7b4f86',)
                ttk.Separator(menu, takefocus=0, orient=HORIZONTAL, style='roxo.TSeparator', ).place(
                    x=10, y=70, relwidth=0.97, relheight=0.005)

                ttk.Separator(menu, takefocus=0, orient=HORIZONTAL,
                              ).place(x=10, y=280, relwidth=0.18,)

                ttk.Separator(menu, takefocus=0, orient=VERTICAL,
                              ).place(x=170, y=75, relheight=1)

                valor_id = tree_lista[0]

                l_nome = Label(frame_atualizacao, text='Nome',
                               bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
                l_nome.place(x=20, y=20)

                e_nome = Entry(frame_atualizacao, relief='solid', width=40,
                               justify='left', font=('Ivy 10'))
                e_nome.place(x=20, y=50, height=25)

                l_cpf = Label(frame_atualizacao, text='CPF',
                              bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
                l_cpf.place(x=320, y=20)

                e_cpf = Entry(frame_atualizacao, relief='solid', width=40,
                              justify='left', font=('Ivy 10'))
                e_cpf.place(x=320, y=50, height=25)

                l_iemail = Label(frame_atualizacao, text='Email',
                                 bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
                l_iemail.place(x=20, y=90)

                e_iemail = Entry(frame_atualizacao, relief='solid', width=40,
                                 justify='left', font=('Ivy 10'))
                e_iemail.place(x=20, y=120, height=25)

                l_telefone = Label(frame_atualizacao, text='Telefone',
                                   bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
                l_telefone.place(x=320, y=90)

                e_telefone = Entry(frame_atualizacao, relief='solid', width=40,
                                   justify='left', font=('Ivy 10'))
                e_telefone.place(x=320, y=120, height=25)

                l_nascimento = Label(frame_atualizacao, text='DT. Nascimento',
                                     bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
                l_nascimento.place(x=20, y=160)

                e_nascimento = Entry(
                    frame_atualizacao, width=17, background='#f9f9f9', fg='#414141', borderwidth=2)
                e_nascimento.place(x=20, y=190, height=25)

                l_civil = Label(frame_atualizacao, text='EST. Civil',
                                bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
                l_civil.place(x=160, y=160)

                estado_civil = ['Solteiro(a)', 'Casado(a)',
                                'Dirvociado(a)', 'Viúvo(a)']
                e_civil = ttk.Combobox(frame_atualizacao, width=17,
                                       justify='left', font=('Ivy 10'), values=estado_civil)
                e_civil.place(x=160, y=190, height=25)

                e_nome.insert(0, tree_lista[1])
                e_cpf.insert(0, tree_lista[2])
                e_iemail.insert(0, tree_lista[3])
                e_telefone.insert(0, tree_lista[4])
                e_nascimento.insert(0, tree_lista[5])
                e_civil.insert(0, tree_lista[6])

                def atualizando():
                    listaatt = e_nome.get(), e_cpf.get(), e_iemail.get(
                    ), e_telefone.get(), e_nascimento.get(), e_civil.get(), tree_lista[0]
                    updateCliente(listaatt)

                    linhaatt = e_nome.get(), tree_lista[1]
                    updateinfos(linhaatt)

                    messagebox.showinfo(
                        'Atualizado', 'Cliente atualizado com sucesso!')
                    botao_cliente(event)

                b_cadastrar = Button(frame_atualizacao, text='Atualizar', width=29, height=2,
                                     font=('Ivy 10 bold'), bg='#45075d', fg='white', relief='raised', overrelief='ridge', command=atualizando)
                b_cadastrar.place(x=20, y=290)

            else:
                messagebox.showerror('Erro', 'Nenhum cliente selecionado')

        b_excluir = Label(master=menu, text='⨂ EXCLUIR', anchor=NW,
                          font=('Ivy 16 '), bg='#f9f9f9', fg='#9f71ab')
        b_excluir.place(x=10, y=330)
        b_excluir.bind('<Button-1>', deletarCliente)

        b_atualizar = Label(master=menu, text='⟲ ATUALIZAR', anchor=NW,
                            font=('Ivy 16 '), bg='#f9f9f9', fg='#9f71ab')
        b_atualizar.place(x=10, y=290)
        b_atualizar.bind('<Button-1>', attCliente)

        b_infos = Label(master=menu, text='▤ DADOS', anchor=NW,
                        font=('Ivy 16 '), bg='#f9f9f9', fg='#9f71ab')
        b_infos.place(x=10, y=370)
        b_infos.bind('<Button-1>', dadosClilente)

    def botao_incluir(event):
        frame_incluir = Frame(menu)
        frame_incluir = Frame(menu, width=829, height=430,
                              bg='#f9f9f9', relief='flat')
        frame_incluir.place(x=170, y=70)
        styl = ttk.Style()
        styl.configure('roxo.TSeparator', background='#7b4f86',)
        ttk.Separator(menu, takefocus=0, orient=HORIZONTAL, style='roxo.TSeparator', ).place(
            x=10, y=70, relwidth=0.97, relheight=0.005)

        ttk.Separator(menu, takefocus=0, orient=HORIZONTAL,
                      ).place(x=10, y=280, relwidth=0.18,)

        ttk.Separator(menu, takefocus=0, orient=VERTICAL,
                      ).place(x=170, y=75, relheight=1)

        # def ficha_avaliacao(event):
        #     ficha = Tk()
        #     ficha.geometry('900x600')
        #     ficha.resizable(False, False)
        #     ficha.configure(background='#f9f9f9')
        #     ficha.title('FICHA DE AVALIAÇÃO')

        #     styl = ttk.Style()
        #     styl.configure('roxo.TSeparator', background='#7b4f86',)
        #     ttk.Separator(ficha, takefocus=0, orient=HORIZONTAL, style='roxo.TSeparator', ).place(
        #         x=10, y=70, relwidth=0.97, relheight=0.005)

        #     l_titulo = Label(master=ficha, text='❢ FICHA DE AVALIAÇÃO', anchor=NW,
        #                      font=('Ivy 25 bold'), bg='#f9f9f9', fg='#7b4f86')
        #     l_titulo.place(x=25, y=20)

        #     lista = nomes()
        #     escolaridade = ['Fundamental Completo', 'Fundamental Incompleto',
        #                     'Médio Completo', 'Médio Incompleto', 'Superior Completo', 'Superios Incompleto']

        #     l_cliente = Label(ficha, font=('Ivy 12'),
        #                       text='Cliente:', bg='#f9f9f9', fg='#414141')
        #     l_cliente.place(x=20, y=90)
        #     c_cliente = ttk.Combobox(
        #         ficha, font=('Ivy 12'), state='readonly', width=20)
        #     c_cliente['values'] = [
        #         item for result in lista for item in result if item]
        #     c_cliente.place(x=120, y=90)

        #     l_escolaridade = Label(ficha, font=('Ivy 12'),
        #                            text='Escolaridade:', bg='#f9f9f9', fg='#414141')
        #     l_escolaridade.place(x=20, y=130)
        #     c_escolaridade = ttk.Combobox(ficha, font=(
        #         'Ivy 12'), state='readonly', width=20)
        #     c_escolaridade['values'] = escolaridade
        #     c_escolaridade.place(x=120, y=130)

        #     l_profissao = Label(ficha, font=('Ivy 12'),
        #                         text='Profissão:', bg='#f9f9f9', fg='#414141')
        #     l_profissao.place(x=20, y=170)
        #     e_profissao = Entry(ficha, relief='solid', width=22,
        #                         justify='left', font=('Ivy 12'))
        #     e_profissao.place(x=120, y=170)

        #     l_patologia = Label(ficha, font=('Ivy 12'),
        #                         text='Patologia:', bg='#f9f9f9', fg='#414141')
        #     l_patologia.place(x=20, y=210)
        #     e_patologia = Entry(ficha, relief='solid', width=22,
        #                         justify='left', font=('Ivy 12'))
        #     e_patologia.place(x=120, y=210)

        #     l__medicamento = Label(ficha, font=('Ivy 12'),
        #                            text='Medicamento:', bg='#f9f9f9', fg='#414141')
        #     l__medicamento.place(x=20, y=250)
        #     e_medicamento = Entry(ficha, relief='solid', width=22,
        #                           justify='left', font=('Ivy 12'))
        #     e_medicamento.place(x=120, y=250)

        #     agua = ['Menos de 1L/Dia', '1 Litro/Dia',
        #             '2 Litros/Dia', '3 Litros/Dia', 'Mais de 4L/Dia']
        #     l_agua = Label(ficha, font=('Ivy 12'),
        #                    text='Agua(L/Dia):', bg='#f9f9f9', fg='#414141')
        #     l_agua.place(x=20, y=290)
        #     c_agua = ttk.Combobox(ficha, font=(
        #         'Ivy 12'), state='readonly', width=20)
        #     c_agua['values'] = agua
        #     c_agua.place(x=120, y=290)

        #     simnao = ['Sim', 'Não']
        #     l_exercicios = Label(ficha, font=('Ivy 12'),
        #                          text='Exercicios:', bg='#f9f9f9', fg='#414141')
        #     l_exercicios.place(x=20, y=330)
        #     e_exercicios = Entry(ficha, relief='solid', width=22,
        #                          justify='left', font=('Ivy 12'))
        #     e_exercicios.place(x=120, y=330)

        #     l_alimentacao = Label(ficha, font=('Ivy 12'),
        #                           text='Alimentação:', bg='#f9f9f9', fg='#414141')
        #     l_alimentacao.place(x=20, y=370)
        #     check_acucar = Checkbutton(
        #         ficha, text='Açucar/Doces', bg='#f9f9f9', fg='#414141', font=('Ivy 12'))
        #     check_acucar.place(x=120, y=370)
        #     check_frutas = Checkbutton(
        #         ficha, text='Frutas', bg='#f9f9f9', fg='#414141', font=('Ivy 12'))
        #     check_leite = Checkbutton(
        #         ficha, text='Leite/Derivados', bg='#f9f9f9', fg='#414141', font=('Ivy 12'))
        #     check_fritura = Checkbutton(
        #         ficha, text='Frituras/Gordura', bg='#f9f9f9', fg='#414141', font=('Ivy 12'))
        #     check_verdura = Checkbutton(
        #         ficha, text='Verduras', bg='#f9f9f9', fg='#414141', font=('Ivy 12'))
        #     check_industrializados = Checkbutton(
        #         ficha, text='Industrializados', bg='#f9f9f9', fg='#414141', font=('Ivy 12'))
        #     check_massa = Checkbutton(
        #         ficha, text='Massa/Molho', bg='#f9f9f9', fg='#414141', font=('Ivy 12'))
        #     check_legumes = Checkbutton(
        #         ficha, text='Legumes', bg='#f9f9f9', fg='#414141', font=('Ivy 12'))
        #     check_diet = Checkbutton(
        #         ficha, text='Diet/Light', bg='#f9f9f9', fg='#414141', font=('Ivy 12'))
        #     check_cereais = Checkbutton(
        #         ficha, text='Cereais', bg='#f9f9f9', fg='#414141', font=('Ivy 12'))
        #     check_oleaginosas = Checkbutton(
        #         ficha, text='Oleaginosas', bg='#f9f9f9', fg='#414141', font=('Ivy 12'))
        #     check_frutas.place(x=120, y=390)
        #     check_leite.place(x=120, y=410)
        #     check_fritura.place(x=120, y=430)
        #     check_verdura.place(x=120, y=450)
        #     check_industrializados.place(x=120, y=470)
        #     check_massa.place(x=120, y=490)
        #     check_legumes.place(x=120, y=510)
        #     check_diet.place(x=120, y=530)
        #     check_cereais.place(x=120, y=550)
        #     check_oleaginosas.place(x=120, y=570)

        #     l_sono = Label(ficha, font=('Ivy 12'),
        #                    text='Sono:', bg='#f9f9f9', fg='#414141')
        #     l_sono.place(x=330, y=90)
        #     e_sono = Entry(ficha, relief='solid', width=22,
        #                    justify='left', font=('Ivy 12'))
        #     e_sono.place(x=430, y=90)

        #     l_tabagismo = Label(ficha, font=('Ivy 12'),
        #                         text='Tabagismo:', bg='#f9f9f9', fg='#414141')
        #     l_tabagismo.place(x=330, y=130)
        #     c_tabagismo = ttk.Combobox(ficha, font=(
        #         'Ivy 12'), state='readonly', width=20)
        #     c_tabagismo['values'] = simnao
        #     c_tabagismo.place(x=430, y=130)

        #     l_alcool = Label(ficha, font=('Ivy 12'),
        #                      text='Alcool', bg='#f9f9f9', fg='#414141')
        #     l_alcool.place(x=330, y=170)
        #     e_alcool = Entry(ficha, relief='solid', width=22,
        #                    justify='left', font=('Ivy 12'))
        #     e_alcool.place(x=430, y=170)

        #     ficha.mainloop()

        l_nome = Label(frame_incluir, text='Nome',
                       bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
        l_nome.place(x=20, y=20)

        e_nome = Entry(frame_incluir, relief='solid', width=40,
                       justify='left', font=('Ivy 10'))
        e_nome.place(x=20, y=50, height=25)

        l_cpf = Label(frame_incluir, text='CPF',
                      bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
        l_cpf.place(x=320, y=20)

        e_cpf = Entry(frame_incluir, relief='solid', width=40,
                      justify='left', font=('Ivy 10'))
        e_cpf.place(x=320, y=50, height=25)

        l_iemail = Label(frame_incluir, text='Email',
                         bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
        l_iemail.place(x=20, y=90)

        e_iemail = Entry(frame_incluir, relief='solid', width=40,
                         justify='left', font=('Ivy 10'))
        e_iemail.place(x=20, y=120, height=25)

        l_telefone = Label(frame_incluir, text='Telefone',
                           bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
        l_telefone.place(x=320, y=90)

        e_telefone = Entry(frame_incluir, relief='solid', width=40,
                           justify='left', font=('Ivy 10'))
        e_telefone.place(x=320, y=120, height=25)

        l_nascimento = Label(frame_incluir, text='DT. Nascimento',
                             bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
        l_nascimento.place(x=20, y=160)

        e_nascimento = DateEntry(
            frame_incluir, width=17, background='#c0c3c8', foreground='white', borderwidth=2, year=1999, month=1, day=1, date_pattern="m/d/y")
        e_nascimento.place(x=20, y=190, height=25)

        l_civil = Label(frame_incluir, text='EST. Civil',
                        bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
        l_civil.place(x=160, y=160)

        estado_civil = ['Solteiro(a)', 'Casado(a)',
                        'Dirvociado(a)', 'Viúvo(a)']
        e_civil = ttk.Combobox(frame_incluir, width=17,
                               justify='left', font=('Ivy 10'), values=estado_civil)
        e_civil.place(x=160, y=190, height=25)

      #  b_avaliacao = Label(frame_incluir, text='Cadastro da Avaliação',
      #                      bg='#f9f9f9', font=('Ivy 14 bold'), fg='#7b4f86')
      #  b_avaliacao.place(x=320, y=190)
      #  b_avaliacao.bind('<Button-1>', ficha_avaliacao)

        def cadastrar():
            if e_nome.get() == '':
                messagebox.showerror('ERRO', 'Preencha o nome por favor')
            else:
                lista = e_nome.get(), e_cpf.get(), e_iemail.get(
                ), e_telefone.get(), e_nascimento.get_date(), e_civil.get()

                adicionar(lista)

                messagebox.showinfo('INCLUIDO', 'Cliente Incluido')
                e_nome.delete(0, 'end')
                e_cpf.delete(0, 'end')
                e_iemail.delete(0, 'end')
                e_telefone.delete(0, 'end')
                e_civil.delete(0, 'end')

        b_cadastrar = Button(frame_incluir, text='INCLUIR', width=29, height=2,
                             font=('Ivy 10 bold'), bg='#45075d', fg='white', relief='raised', overrelief='ridge', command=cadastrar)
        b_cadastrar.place(x=20, y=290)

    def botao_hoje(event):
        frame_hoje = Frame(menu)
        frame_hoje = Frame(menu, width=829, height=430,
                           bg='#f9f9f9', relief='flat')
        frame_hoje.place(x=170, y=70)
        styl = ttk.Style()
        styl.configure('roxo.TSeparator', background='#7b4f86',)
        ttk.Separator(menu, takefocus=0, orient=HORIZONTAL, style='roxo.TSeparator', ).place(
            x=10, y=70, relwidth=0.97, relheight=0.005)

        ttk.Separator(menu, takefocus=0, orient=HORIZONTAL,
                      ).place(x=10, y=280, relwidth=0.18,)

        ttk.Separator(menu, takefocus=0, orient=VERTICAL,
                      ).place(x=170, y=75, relheight=1)

        threeview_hoje = ttk.Treeview(frame_hoje, columns=(
            'Cliente', 'Procedimento', 'Valor', 'Horario'), show='headings', height=20)
        threeview_hoje.column('Cliente', minwidth=0, width=250)
        threeview_hoje.column('Procedimento', minwidth=0, width=250)
        threeview_hoje.column('Valor', minwidth=0, width=105)
        threeview_hoje.column('Horario', minwidth=0, width=105)
        threeview_hoje.heading('Cliente', text='CLIENTE')
        threeview_hoje.heading('Procedimento', text='PROCEDIMENTO')
        threeview_hoje.heading('Valor', text='VALOR')
        threeview_hoje.heading('Horario', text='HORARIO')
        threeview_hoje.pack()

        datahoje = date.today()
        clienteHoje = diadehoje([datahoje])

        for item in clienteHoje:
            threeview_hoje.insert('', 'end', values=item)

    def botao_menu(event):
        frame_menu = Frame(menu)
        frame_menu = Frame(menu, width=829, height=430,
                           bg='#f9f9f9', relief='flat')
        frame_menu.place(x=170, y=70)
        styl = ttk.Style()
        styl.configure('roxo.TSeparator', background='#7b4f86',)
        ttk.Separator(menu, takefocus=0, orient=HORIZONTAL, style='roxo.TSeparator', ).place(
            x=10, y=70, relwidth=0.97, relheight=0.005)

        ttk.Separator(menu, takefocus=0, orient=HORIZONTAL,
                      ).place(x=10, y=280, relwidth=0.18,)

        ttk.Separator(menu, takefocus=0, orient=VERTICAL,
                      ).place(x=170, y=75, relheight=1)

        l_bemvindo = Label(
            frame_menu, text='SISTEMA GERAL ESPAÇO DE BELEZA JU MARQUES', bg='#f9f9f9', font=('Ivy 16 bold underline'), fg='#414141')
        l_bemvindo.place(x=20, y=20)

        l_infomacoes = Label(frame_menu, text='Escolha uma das opções ao lado', bg='#f9f9f9', font=(
            'Ivy 14'), fg='#414141')
        l_infomacoes.place(x=20, y=50)

        l_info_hoje = Label(frame_menu, text='* Opção HOJE lista os clientes de hoje',
                            bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
        l_info_hoje.place(x=20, y=80)

        l_info_cadastro = Label(frame_menu, text='* Opção INCLUIR para cadastrar novos clientes',
                                bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
        l_info_cadastro.place(x=20, y=110)

        l_info_cliente = Label(frame_menu, text='* Opção CLIENTE para listar clientes e atualizar cadastros',
                               bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
        l_info_cliente.place(x=20, y=140)

        l_info_agendar = Label(frame_menu, text='* Opção AGENDAR para agendar um cliente',
                               bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
        l_info_agendar.place(x=20, y=170)

        l_info_procedimento = Label(frame_menu, text='* Opção TÉCNICA para listar e atualizar procedimentos',
                                    bg='#f9f9f9', font=('Ivy 12'), fg='#414141')
        l_info_procedimento.place(x=20, y=200)

    b_menu = Label(master=menu, text='◀  MENU', anchor=NW,
                   font=('Ivy 25 bold'), bg='#f9f9f9', fg='#7b4f86')
    b_menu.place(x=25, y=20)
    b_menu.bind("<Button-1>", botao_menu)

    b_hoje = Label(master=menu, text='☁ HOJE', anchor=NW,
                   font=('Ivy 16 '), bg='#f9f9f9', fg='#9f71ab')
    b_hoje.place(x=10, y=80)
    b_hoje.bind('<Button-1>', botao_hoje)

    b_incluir = Label(master=menu, text='✚ INCLUIR', anchor=NW,
                      font=('Ivy 16 '), bg='#f9f9f9', fg='#9f71ab')
    b_incluir.place(x=10, y=120)
    b_incluir.bind('<Button-1>', botao_incluir)

    b_cliente = Label(master=menu, text='✱ CLIENTE', anchor=NW,
                      font=('Ivy 16 '), bg='#f9f9f9', fg='#9f71ab')
    b_cliente.place(x=10, y=160)
    b_cliente.bind('<Button-1>', botao_cliente)

    b_agendar = Label(master=menu, text='✎ AGENDAR', anchor=NW,
                      font=('Ivy 16 '), bg='#f9f9f9', fg='#9f71ab')
    b_agendar.place(x=10, y=200)
    b_agendar.bind('<Button-1>', botao_agendar)

    b_procedimento = Label(master=menu, text='✂ TÉCNICA', anchor=NW,
                           font=('Ivy 16 '), bg='#f9f9f9', fg='#9f71ab')
    b_procedimento.place(x=10, y=240)
    b_procedimento.bind('<Button-1>', botao_tecnica)

    styl = ttk.Style()
    styl.configure('roxo.TSeparator', background='#7b4f86',)
    ttk.Separator(menu, takefocus=0, orient=HORIZONTAL, style='roxo.TSeparator', ).place(
        x=10, y=70, relwidth=0.97, relheight=0.005)

    ttk.Separator(menu, takefocus=0, orient=HORIZONTAL,
                  ).place(x=10, y=280, relwidth=0.18,)

    ttk.Separator(menu, takefocus=0, orient=VERTICAL,
                  ).place(x=170, y=75, relheight=1)

    b_atualizar = Label(master=menu, text='⟲ ATUALIZAR', anchor=NW,
                        font=('Ivy 16 '), bg='#f9f9f9', fg='#9f71ab')
    b_atualizar.place(x=10, y=290)

    b_excluir = Label(master=menu, text='⨂ EXCLUIR', anchor=NW,
                      font=('Ivy 16 '), bg='#f9f9f9', fg='#9f71ab')
    b_excluir.place(x=10, y=330)

    b_infos = Label(master=menu, text='▤ DADOS', anchor=NW,
                    font=('Ivy 16 '), bg='#f9f9f9', fg='#9f71ab')
    b_infos.place(x=10, y=370)

    botao_menu('')

    menu.mainloop()


# tela de login
top_frame = Frame(janela)
top_frame = Frame(janela, width=390, height=490, bg='#fdfdfd', relief='flat')
top_frame.grid(row=0, column=0, padx=5, pady=5)

l_login = Label(janela, text='Login', anchor=NW,
                font=('Ivy 25 '), bg='#fdfdfd', relief='flat', fg='#414141')
l_login.place(x=158, y=30)

l_sgjm = Label(janela, text='Espaço de Beleza Ju Marques', anchor=NW,
               font=('Ivy 10 underline'), bg='#fdfdfd', relief='flat', fg='#414141')
l_sgjm.place(x=105, y=75)

l_usuario = Label(top_frame, text='Usuario *', anchor=NW,
                  font=('Ivy 12 '), bg='#fdfdfd', relief='flat', fg='#414141')
l_usuario.place(x=48, y=100)

l_senha = Label(top_frame, text='Senha *', anchor=NW,
                font=('Ivy 12 '), bg='#fdfdfd', relief='flat', fg='#414141')
l_senha.place(x=48, y=180)

l_esqueceu = Label(janela, text='Esqueceu a senha?', anchor=NW,
                   font=('Ivy 10 underline'), bg='#fdfdfd', relief='flat', fg='#414141')
l_esqueceu.place(x=48, y=255)

e_usuario = Entry(top_frame, relief='solid', width=46, justify='left',)
e_usuario.place(x=48, y=130, height=36)

e_senha = Entry(top_frame, relief='solid', width=46, justify='left')
e_senha.place(x=48, y=210, height=36)

b_login = Button(top_frame, text='Login', width=30, height=2,
                 font=('Ivy 12'), bg='#414141', fg='white', relief='raised', overrelief='ridge', command=login)
b_login.place(x=48, y=320)

l_cnpj = Label(janela, text='CNPJ: 32.768.837/0001-71', anchor=NW,
               font=('Ivy 10'), bg='#fdfdfd', relief='flat', fg='#414141')
l_cnpj.place(x=48, y=380)

l_proprietario = Label(janela, text='Proprietário(a): Juliana Marques dos Santos', anchor=NW,
                       font=('Ivy 10'), bg='#fdfdfd', relief='flat', fg='#414141')
l_proprietario.place(x=48, y=400)

l_dev = Label(janela, text='Desenvolvedor(a): Daniel Clemente de Cayres Filho', anchor=NW,
              font=('Ivy 10'), bg='#fdfdfd', relief='flat', fg='#414141')
l_dev.place(x=48, y=420)

l_email = Label(janela, text='Email para contato: dcfcontato@icloud.com', anchor=NW,
                font=('Ivy 10'), bg='#fdfdfd', relief='flat', fg='#414141')
l_email.place(x=48, y=440)

janela.mainloop()
