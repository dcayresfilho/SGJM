from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
from banco import *
from datetime import date


ficha = Tk()
ficha.geometry('900x600')
ficha.resizable(False, False)
ficha.configure(background='#f9f9f9')
ficha.title('FICHA DE AVALIAÇÃO')

styl = ttk.Style()
styl.configure('roxo.TSeparator', background='#7b4f86',)
ttk.Separator(ficha, takefocus=0, orient=HORIZONTAL, style='roxo.TSeparator', ).place(
    x=10, y=70, relwidth=0.97, relheight=0.005)

l_titulo = Label(master=ficha, text='FICHA DE AVALIAÇÃO', anchor=NW,
                 font=('Ivy 25 bold'), bg='#f9f9f9', fg='#7b4f86')
l_titulo.place(x=25, y=20)

b_registrar = Button(ficha, text='REGISTRAR', width=20, height=2,
                     font=('Ivy 10 bold'), bg='#45075d', fg='white', relief='raised', overrelief='ridge', command='registrar')
b_registrar.place(x=700, y=20)

nb = ttk.Notebook(ficha)

nb.place(x=30, y=90, width=850, height=500)

tbDados = Frame(nb)
tbGeral = Frame(nb)
tbHabitos = Frame(nb)
tbSaude = Frame(nb)
tbCapilar = Frame(nb)
tbFacial = Frame(nb)
tbPele = Frame(nb)
tbCorporal = Frame(nb)
nb.add(tbDados, text='Dados do Cliente')
nb.add(tbGeral, text='Informaçoes Gerais   ')
nb.add(tbHabitos, text='Habitos            ')
nb.add(tbSaude, text='Estado de Saude     ')
nb.add(tbCapilar, text='Avaliação Capilar')
nb.add(tbFacial, text='Avaliação Facial')
nb.add(tbPele, text='Avaliação da Pele      ')
nb.add(tbCorporal, text='Avaliação Corporal       ')


# tbdados
lista = nomes()
escolaridade = ['Fundamental Completo', 'Fundamental Incompleto',
                'Médio Completo', 'Médio Incompleto', 'Superior Completo', 'Superios Incompleto']

l_cliente = Label(tbDados, font=('Ivy 12'),
                  text='Cliente',  fg='#414141')
l_cliente.place(x=5, y=20)
c_cliente = ttk.Combobox(
    tbDados, font=('Ivy 12'), state='readonly', width=20)
c_cliente['values'] = [
    item for result in lista for item in result if item]
c_cliente.place(x=5, y=50)

l_escolaridade = Label(tbDados, font=('Ivy 12'),
                       text='Escolaridade:', fg='#414141')
l_escolaridade.place(x=5, y=80)
c_escolaridade = ttk.Combobox(tbDados, font=(
    'Ivy 12'), state='readonly', width=20)
c_escolaridade['values'] = escolaridade
c_escolaridade.place(x=5, y=110)

l_profissao = Label(tbDados, font=('Ivy 12'),
                    text='Profissão:', fg='#414141')
l_profissao.place(x=5, y=140)
e_profissao = Entry(tbDados, relief='solid', width=22,
                    justify='left', font=('Ivy 12'))
e_profissao.place(x=5, y=170)


l_dtnascimento = Label(tbDados, font=('Ivy 12'),
                       text='Data de Nascimento', fg='#414141')
l_dtnascimento.place(x=5, y=200)
e_dtnascimento = DateEntry(tbDados, width=30, background='#c0c3c8', foreground='white',
                           borderwidth=2, year=1960, month=1, day=1, date_pattern="d/m/y")
e_dtnascimento.place(x=5, y=230, height=25)

l_cpf = Label(tbDados, text='CPF',
              font=('Ivy 12'), fg='#414141')
l_cpf.place(x=250, y=20)
e_cpf = Entry(tbDados, relief='solid', width=22,
              justify='left', font=('Ivy 12'))
e_cpf.place(x=250, y=50)

l_cidade = Label(tbDados, text='Endereço',
                 font=('Ivy 12'), fg='#414141')
l_cidade.place(x=250, y=80)
e_cidade = Entry(tbDados, relief='solid', width=22,
                 justify='left', font=('Ivy 12'))
e_cidade.place(x=250, y=110)

estado_civil = ['Solteiro(a)', 'Casado(a)',
                'Dirvociado(a)', 'Viúvo(a)']

l_civil = Label(tbDados, text='EST. Civil',
                font=('Ivy 12'), fg='#414141')
l_civil.place(x=250, y=140)
e_civil = ttk.Combobox(tbDados, width=20,
                       justify='left', font=('Ivy 12'), values=estado_civil)
e_civil.place(x=250, y=170, height=25)

hoje = date.today().strftime('%d/%m/%Y')

l_hoje = Label(tbDados, text=hoje,
               font=('Ivy 12'), fg='#414141')
l_hoje.place(x=250, y=230)

# tbgeral

l_patologia = Label(tbGeral, font=('Ivy 12'),
                    text='Patologias Crônicas', fg='#414141')
l_patologia.place(x=5, y=20)
e_patologia = Text(tbGeral, relief='solid', width=25,
                   font=('Ivy 12'))
e_patologia.place(x=5, y=50, height=70)

l_medicamentos = Label(tbGeral, font=('Ivy 12'),
                       text='Medicamentos*', fg='#414141')
l_medicamentos.place(x=5, y=140)
l_continuo = Label(tbGeral, font=('Ivy 12'),
                   text='Uso Contínuo', fg='#414141')
l_continuo.place(x=5, y=160)
e_continuo = Entry(tbGeral, relief='solid', width=25,
                   font=('Ivy 12'))
e_continuo.place(x=5, y=190)
l_momento = Label(tbGeral, font=('Ivy 12'),
                  text='Uso Momentâneo', fg='#414141')
l_momento.place(x=5, y=220)
e_momento = Entry(tbGeral, relief='solid', width=25,
                  font=('Ivy 12'))
e_momento.place(x=5, y=250)

# tbhabitos
l_agua = Label(tbHabitos, font=('Ivy 12'),
               text='Ingestão de água(L/dia)', fg='#414141')
l_agua.place(x=5, y=20)
e_agua = Entry(tbHabitos, relief='solid', width=25,
               font=('Ivy 12'))
e_agua.place(x=5, y=50)


l_exercicio = Label(tbHabitos, font=('Ivy 12'),
                    text='Exercício Físico', fg='#414141')
l_exercicio.place(x=5, y=80)
e_exercicios = Checkbutton(tbHabitos, font=(
    'Ivy 12'), text='Sim', fg='#414141')
e_exerciciom = Checkbutton(tbHabitos, font=(
    'Ivy 12'), text='Não', fg='#414141')
e_exerciciom.place(x=5, y=110)
e_exercicios.place(x=5, y=140)

l_qual = Label(tbHabitos, font=('Ivy 12'),
               text='Qual', fg='#414141')
l_qual.place(x=5, y=170)
e_qual = Entry(tbHabitos, relief='solid', width=25,
               font=('Ivy 12'))
e_qual.place(x=5, y=200)

l_frequencia = Label(tbHabitos, font=('Ivy 12'),
                     text='Frequencia', fg='#414141')
l_frequencia.place(x=5, y=230)
e_frequencia = Entry(tbHabitos, relief='solid', width=25,
                     font=('Ivy 12'))
e_frequencia.place(x=5, y=260)

l_alimentacao = Label(tbHabitos, font=('Ivy 12'),
                      text='Alimentação', fg='#414141')
l_alimentacao.place(x=250, y=20)
e_acucar = Checkbutton(tbHabitos, font=(
    'Ivy 12'), text='Açucar/Doces', fg='#414141')
e_fritura = Checkbutton(tbHabitos, font=(
    'Ivy 12'), text='Frituras/Gordura', fg='#414141')
e_massa = Checkbutton(tbHabitos, font=(
    'Ivy 12'), text='Massas/Molhos', fg='#414141')
e_frutas = Checkbutton(tbHabitos, font=(
    'Ivy 12'), text='Frutas', fg='#414141')
e_verduras = Checkbutton(tbHabitos, font=(
    'Ivy 12'), text='Verduras', fg='#414141')
e_legumes = Checkbutton(tbHabitos, font=(
    'Ivy 12'), text='Legumes', fg='#414141')
e_leite = Checkbutton(tbHabitos, font=(
    'Ivy 12'), text='Leite/Derivados', fg='#414141')
e_industrializados = Checkbutton(tbHabitos, font=(
    'Ivy 12'), text='Industrializados', fg='#414141')
e_diet = Checkbutton(tbHabitos, font=(
    'Ivy 12'), text='Diet/Light', fg='#414141')
e_cereais = Checkbutton(tbHabitos, font=(
    'Ivy 12'), text='Cerais', fg='#414141')
e_oleaginosas = Checkbutton(tbHabitos, font=(
    'Ivy 12'), text='Oleaginosas', fg='#414141')
e_acucar.place(x=250, y=40)
e_fritura.place(x=250, y=60)
e_massa.place(x=250, y=80)
e_frutas.place(x=250, y=100)
e_verduras.place(x=250, y=120)
e_legumes.place(x=250, y=140)
e_leite.place(x=250, y=160)
e_industrializados.place(x=250, y=180)
e_diet.place(x=250, y=200)
e_cereais.place(x=250, y=220)
e_oleaginosas.place(x=250, y=240)

l_sono = Label(tbHabitos, font=('Ivy 12'),
               text='Sono', fg='#414141')
l_sono.place(x=450, y=20)
e_sono = Entry(tbHabitos, relief='solid', width=25,
               font=('Ivy 12'))
e_sono.place(x=450, y=50)


enquete = ['Sim', 'Não']
l_tabaco = Label(tbHabitos, font=('Ivy 12'),
                 text='Tabagismo', fg='#414141')
l_tabaco.place(x=450, y=80)
e_tabaco = ttk.Combobox(tbHabitos, width=23,
                        justify='left', font=('Ivy 12'))
e_tabaco['values'] = enquete
e_tabaco.place(x=450, y=110)

l_alcool = Label(tbHabitos, font=('Ivy 12'),
                 text='Ingestão de bebida alcoólica', fg='#414141')
l_alcool.place(x=450, y=140)
e_alcools = Checkbutton(tbHabitos, font=(
    'Ivy 12'), text='Sim', fg='#414141')
e_alcooln = Checkbutton(tbHabitos, font=(
    'Ivy 12'), text='Não', fg='#414141')
e_alcools.place(x=450, y=170)
e_alcooln.place(x=450, y=190)

l_alcoolfreq = Label(tbHabitos, font=('Ivy 12'),
                     text='Frequência', fg='#414141')
l_alcoolfreq.place(x=450, y=220)
e_alcoolfreq = Entry(tbHabitos, relief='solid', width=25,
                     font=('Ivy 12'))
e_alcoolfreq.place(x=450, y=250)

# tbsaude
l_menstruacao = Label(tbSaude, font=('Ivy 12'),
                      text='Data da última menstruação', fg='#414141')
l_menstruacao.place(x=5, y=20)
e_menstruacao = DateEntry(tbSaude, width=35, background='#c0c3c8', foreground='white',
                          borderwidth=2, year=2023, month=1, day=1, date_pattern="d/m/y")
e_menstruacao.place(x=5, y=50, height=23)

l_ciclo = Label(tbSaude, font=('Ivy 12'),
                text='Ciclo menstruação', fg='#414141')
l_ciclo.place(x=5, y=80)
e_ciclor = Checkbutton(tbSaude, font=(
    'Ivy 12'), text='Regular', fg='#414141')
e_cicloi = Checkbutton(tbSaude, font=(
    'Ivy 12'), text='Irregular', fg='#414141')
e_ciclor.place(x=5, y=100)
e_cicloi.place(x=5, y=120)

l_reprodutor = Label(tbSaude, font=('Ivy 12'),
                     text='Alteração do Sistema Reprodutor', fg='#414141')
l_reprodutor.place(x=5, y=150)
e_reprodutor = Entry(tbSaude, relief='solid', width=25,
                     font=('Ivy 12'))
e_reprodutor.place(x=5, y=180)

l_tegumentar = Label(tbSaude, font=('Ivy 12'),
                     text='Alterações do Sistema \n Tegumentar/Alergias da pele', fg='#414141')
l_tegumentar.place(x=5, y=210)
e_tegumentar = Entry(tbSaude, relief='solid', width=25,
                     font=('Ivy 12'))
e_tegumentar.place(x=5, y=260)

l_vasculares = Label(tbSaude, font=('Ivy 12'),
                     text='Alterações Vasculares', fg='#414141')
l_vasculares.place(x=5, y=290)
e_vasculares = Entry(tbSaude, relief='solid', width=25,
                     font=('Ivy 12'))
e_vasculares.place(x=5, y=320)

l_cardiacas = Label(tbSaude, font=('Ivy 12'),
                    text='Alterações/Patologias Cardíacas', fg='#414141')
l_cardiacas.place(x=5, y=350)
e_cardiacas = Entry(tbSaude, relief='solid', width=25,
                    font=('Ivy 12'))
e_cardiacas.place(x=5, y=380)

l_osteomuscular = Label(tbSaude, font=('Ivy 12'),
                        text='Alterações do Sistema Osteomuscular', fg='#414141')
l_osteomuscular.place(x=250, y=20)
e_osteomuscular = Entry(tbSaude, relief='solid', width=25,
                        font=('Ivy 12'))
e_osteomuscular.place(x=250, y=50)

l_reumaticas = Label(tbSaude, font=('Ivy 12'),
                     text='Doenças Reumáticas', fg='#414141')
l_reumaticas.place(x=250, y=80)
e_reumaticas = Entry(tbSaude, relief='solid', width=25,
                     font=('Ivy 12'))
e_reumaticas.place(x=250, y=110)

l_digestivo = Label(tbSaude, font=('Ivy 12'),
                    text='Alterações do Sistema Digestivo\n (gastrite, colite, úlceras, cálculos biliares)', fg='#414141')
l_digestivo.place(x=250, y=140)
e_digestivo = Entry(tbSaude, relief='solid', width=25,
                    font=('Ivy 12'))
e_digestivo.place(x=250, y=180)

l_intestinal = Label(tbSaude, font=('Ivy 12'),
                     text='Funcionamento Intestinal', fg='#414141')
l_intestinal.place(x=250, y=210)
e_intestinalr = Checkbutton(tbSaude, font=(
    'Ivy 12'), text='Regular', fg='#414141')
e_intestinali = Checkbutton(tbSaude, font=(
    'Ivy 12'), text='Irregular', fg='#414141')
e_intestinalr.place(x=250, y=240)
e_intestinali.place(x=250, y=270)

l_respiratorio = Label(tbSaude, font=('Ivy 12'),
                       text='Alterações do Sistema Respiratório', fg='#414141')
l_respiratorio.place(x=250, y=300)
e_respiratorio = Entry(tbSaude, relief='solid', width=25,
                       font=('Ivy 12'))
e_respiratorio.place(x=250, y=320)

l_nervoso = Label(tbSaude, font=('Ivy 12'),
                  text='Sistema Nervoso/Epilepsia', fg='#414141')
l_nervoso.place(x=250, y=350)
e_nervoso = Entry(tbSaude, relief='solid', width=25,
                  font=('Ivy 12'))
e_nervoso.place(x=250, y=380)

l_urinario = Label(tbSaude, font=('Ivy 12'),
                   text='Alterações Sistema Urinário', fg='#414141')
l_urinario.place(x=600, y=20)
e_urinario = Entry(tbSaude, relief='solid', width=25,
                   font=('Ivy 12'))
e_urinario.place(x=600, y=50)

l_endocrino = Label(tbSaude, font=('Ivy 12'),
                    text='Alterações Sistema Endócrino', fg='#414141')
l_endocrino.place(x=600, y=80)
e_endocrino = Entry(tbSaude, relief='solid', width=25,
                    font=('Ivy 12'))
e_endocrino.place(x=600, y=110)

l_oncologico = Label(tbSaude, font=('Ivy 12'),
                     text='Antecedentes Oncológicos', fg='#414141')
l_oncologico.place(x=600, y=140)
e_oncologico = Entry(tbSaude, relief='solid', width=25,
                     font=('Ivy 12'))
e_oncologico.place(x=600, y=170)

l_gestante = Label(tbSaude, font=('Ivy 12'),
                   text='Está gestante?', fg='#414141')
l_gestante.place(x=600, y=200)
e_gestantes = Checkbutton(tbSaude, font=(
    'Ivy 12'), text='Sim', fg='#414141')
e_gestanten = Checkbutton(tbSaude, font=(
    'Ivy 12'), text='Não', fg='#414141')
e_gestantes.place(x=600, y=230)
e_gestanten.place(x=600, y=260)

l_gestacoes = Label(tbSaude, font=('Ivy 12'),
                    text='Gestações', fg='#414141')
l_gestacoes.place(x=600, y=290)
e_gestacoes = Entry(tbSaude, relief='solid', width=25,
                    font=('Ivy 12'))
e_gestacoes.place(x=600, y=320)

l_psicologico = Label(tbSaude, font=('Ivy 12'),
                      text='Estado Psicológico', fg='#414141')
l_psicologico.place(x=600, y=350)
e_psicologico = Entry(tbSaude, relief='solid', width=25,
                      font=('Ivy 12'))
e_psicologico.place(x=600, y=380)

e_queloide = Checkbutton(tbSaude, font=(
    'Ivy 12'), text='Quelóide', fg='#414141')
e_alergia = Checkbutton(tbSaude, font=(
    'Ivy 12'), text='Alergia a metal', fg='#414141')
e_plaquetopenia = Checkbutton(tbSaude, font=(
    'Ivy 12'), text='Plaquetopenia', fg='#414141')
e_proteses = Checkbutton(tbSaude, font=(
    'Ivy 12'), text='Próteses metálicas/implantes', fg='#414141')
e_marcapasso = Checkbutton(tbSaude, font=(
    'Ivy 12'), text='Marcapasso/Stents', fg='#414141')
e_lente = Checkbutton(tbSaude, font=(
    'Ivy 12'), text='Lentes de contato', fg='#414141')
e_dengue = Checkbutton(tbSaude, font=(
    'Ivy 12'), text=' Dengue recente', fg='#414141')
e_queloide.place(x=20, y=410)
e_alergia.place(x=120, y=410)
e_plaquetopenia.place(x=260, y=410)
e_proteses.place(x=390, y=410)
e_marcapasso.place(x=630, y=410)
e_lente.place(x=20, y=440)
e_dengue.place(x=180, y=440)

# tbcapilar
l_carac = Label(tbCapilar, font=('Ivy 12'),
                text='CARACTERÍSTICAS DO FIO E COURO CABELUDO', fg='#414141')
l_carac.place(x=20, y=20)

l_densidade = Label(tbCapilar, font=('Ivy 12'),
                    text='Densidade', fg='#414141')
l_densidade.place(x=20, y=50)
e_pouca = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Pouca', fg='#414141')
e_moderada = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Moderada', fg='#414141')
e_densa = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Densa', fg='#414141')
e_pouca.place(x=20, y=70)
e_moderada.place(x=20, y=90)
e_densa.place(x=20, y=110)

l_espessura = Label(tbCapilar, font=('Ivy 12'),
                    text='Espessura', fg='#414141')
l_espessura.place(x=140, y=50)
e_fina = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Fina', fg='#414141')
e_media = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Média', fg='#414141')
e_grossa = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Grossa', fg='#414141')
e_fina.place(x=140, y=70)
e_media.place(x=140, y=90)
e_grossa.place(x=140, y=110)

l_couro = Label(tbCapilar, font=('Ivy 12'),
                text='Couro cabeludo', fg='#414141')
l_couro.place(x=240, y=50)
e_sensivel = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Sensível', fg='#414141')
e_poucosensivel = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Pouco sensível', fg='#414141')
e_sensivel.place(x=240, y=70)
e_poucosensivel.place(x=240, y=90)

l_elasticidade = Label(tbCapilar, font=('Ivy 12'),
                       text='Elasticidade', fg='#414141')
l_elasticidade.place(x=390, y=50)
e_ausente = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Ausente', fg='#414141')
e_normal = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Normal', fg='#414141')
e_anormal = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Anormal', fg='#414141')
e_exarcebado = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Exacerbado', fg='#414141')
e_ausente.place(x=390, y=70)
e_normal.place(x=390, y=90)
e_anormal.place(x=390, y=110)
e_exarcebado.place(x=390, y=130)

l_hidratacao = Label(tbCapilar, font=('Ivy 12'),
                     text='Hidratação', fg='#414141')
l_hidratacao.place(x=510, y=50)
e_ausentehid = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Ausente', fg='#414141')
e_normalhid = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Normal', fg='#414141')
e_ausentehid.place(x=510, y=70)
e_normalhid.place(x=510, y=90)

l_nutricao = Label(tbCapilar, font=('Ivy 12'),
                   text='Nutrição', fg='#414141')
l_nutricao.place(x=610, y=50)
e_ausentenut = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Ausente', fg='#414141')
e_normalnut = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Normal', fg='#414141')
e_ausentenut.place(x=610, y=70)
e_normalnut.place(x=610, y=90)

l_queda = Label(tbCapilar, font=('Ivy 12'),
                text='Queda', fg='#414141')
l_queda.place(x=710, y=50)
e_quedapouca = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Pouca', fg='#414141')
e_quadanormal = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Normal', fg='#414141')
e_quedaanormal = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Anormal', fg='#414141')
e_grave = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Grave', fg='#414141')
e_quedapouca.place(x=710, y=70)
e_quadanormal.place(x=710, y=90)
e_quedaanormal.place(x=710, y=110)
e_grave.place(x=710, y=130)

l_quebra = Label(tbCapilar, font=('Ivy 12'),
                 text='Quebra', fg='#414141')
l_quebra.place(x=20, y=160)
e_quebrapouca = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Pouca', fg='#414141')
e_quebranormal = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Normal', fg='#414141')
e_quebraanormal = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Anormal', fg='#414141')
e_quebragrave = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Grave', fg='#414141')
e_quebrapouca.place(x=20, y=180)
e_quebranormal.place(x=20, y=200)
e_quebraanormal.place(x=20, y=220)
e_quebragrave.place(x=20, y=240)

l_alisamento = Label(tbCapilar, font=('Ivy 12'),
                     text='Alisamento', fg='#414141')
l_alisamento.place(x=120, y=160)
e_alisamentosim = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Sim', fg='#414141')
e_alisamentonao = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Não', fg='#414141')
e_alisamentosim.place(x=120, y=180)
e_alisamentonao.place(x=120, y=200)
e_quais = Entry(tbCapilar, relief='solid', width=15,
                font=('Ivy 12'))
e_quais.place(x=120, y=230)
e_ultima = DateEntry(tbCapilar, width=19, background='#c0c3c8', foreground='white',
                     borderwidth=2, year=2023, month=1, day=1, date_pattern="d/m/y")
e_ultima.place(x=120, y=260)


l_coloracao = Label(tbCapilar, font=('Ivy 12'),
                    text='Coloração', fg='#414141')
l_coloracao.place(x=280, y=160)
e_coloracaosim = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Sim', fg='#414141')
e_coloracaonao = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Não', fg='#414141')
e_coloracaosim.place(x=280, y=180)
e_coloracaonao.place(x=280, y=200)
e_quaiscoloracao = Entry(tbCapilar, relief='solid', width=15,
                         font=('Ivy 12'))
e_quaiscoloracao.place(x=280, y=230)
e_ultimacoloracao = DateEntry(tbCapilar, width=19, background='#c0c3c8', foreground='white',
                              borderwidth=2, year=2023, month=1, day=1, date_pattern="d/m/y")
e_ultimacoloracao.place(x=280, y=260)

l_descoloracao = Label(tbCapilar, font=('Ivy 12'),
                       text='Descoloração', fg='#414141')
l_descoloracao.place(x=440, y=160)
e_descoloracaosim = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Sim', fg='#414141')
e_descoloracaonao = Checkbutton(tbCapilar, font=(
    'Ivy 12'), text='Não', fg='#414141')
e_descoloracaosim.place(x=440, y=180)
e_descoloracaonao.place(x=440, y=200)
e_ultimadescoloracao = DateEntry(tbCapilar, width=19, background='#c0c3c8', foreground='white',
                                 borderwidth=2, year=2023, month=1, day=1, date_pattern="d/m/y")
e_ultimadescoloracao.place(x=440, y=230)


l_cuidados = Label(tbCapilar, font=('Ivy 12'),
                   text='Cuidados em casa', fg='#414141')
l_cuidados.place(x=20, y=300)
e_cuidados = Text(tbCapilar, relief='solid', width=25,
                  font=('Ivy 12'))
e_cuidados.place(x=20, y=330, height=70)


l_queixas = Label(tbCapilar, font=('Ivy 12'),
                  text='QUEIXA PRINCIPAL', fg='#414141')
l_queixas.place(x=280, y=300)
e_queixas = Text(tbCapilar, relief='solid', width=25,
                 font=('Ivy 12'))
e_queixas.place(x=280, y=330, height=70)


l_obs = Label(tbCapilar, font=('Ivy 12'),
              text='OBSERVAÇÕES', fg='#414141')
l_obs.place(x=540, y=300)
e_obs = Text(tbCapilar, relief='solid', width=25,
             font=('Ivy 12'))
e_obs.place(x=540, y=330, height=70)

# tbfacial

l_facial = Label(tbFacial, font=('Ivy 12'),
                 text='FICHA DE AVALIAÇÃO FACIAL', fg='#414141')
l_facial.place(x=20, y=20)

l_tratamento = Label(tbFacial, font=('Ivy 12'),
                     text='Já recebeu algum tratamento estético', fg='#414141')
l_tratamento.place(x=20, y=50)
e_tratamentosim = Checkbutton(tbFacial, font=(
    'Ivy 12'), text='Sim', fg='#414141')
e_tratamentonao = Checkbutton(tbFacial, font=(
    'Ivy 12'), text='Não', fg='#414141')
e_tratamentosim.place(x=20, y=70)
e_tratamentonao.place(x=20, y=90)
e_ultimatratamento = DateEntry(tbFacial, width=19, background='#c0c3c8', foreground='white',
                               borderwidth=2, year=2023, month=1, day=1, date_pattern="d/m/y")
e_ultimatratamento.place(x=20, y=120)
e_quaistratamento = Text(tbFacial, relief='solid', width=25,
                         font=('Ivy 12'))
e_quaistratamento.place(x=20, y=150, height=35)


l_cosmeticos = Label(tbFacial, font=('Ivy 12'),
                     text='Faz uso de Cosméticos', fg='#414141')
l_cosmeticos.place(x=300, y=50)
e_comesticossim = Checkbutton(tbFacial, font=(
    'Ivy 12'), text='Sim', fg='#414141')
e_comesticosnao = Checkbutton(tbFacial, font=(
    'Ivy 12'), text='Não', fg='#414141')
e_comesticossim.place(x=300, y=70)
e_comesticosnao.place(x=300, y=90)
e_quaiscomesticos = Text(tbFacial, relief='solid', width=25,
                         font=('Ivy 12'))
e_quaiscomesticos.place(x=300, y=150, height=35)

l_filtro = Label(tbFacial, font=('Ivy 12'),
                 text='Usa filtro / bloqueador\n solar regularmente', fg='#414141')
l_filtro.place(x=550, y=50)
e_filtrosim = Checkbutton(tbFacial, font=(
    'Ivy 12'), text='Sim', fg='#414141')
e_filtronao = Checkbutton(tbFacial, font=(
    'Ivy 12'), text='Não', fg='#414141')
e_filtrosim.place(x=550, y=90)
e_filtronao.place(x=550, y=110)
e_quaisfiltros = Text(tbFacial, relief='solid', width=25,
                      font=('Ivy 12'))
e_quaisfiltros.place(x=550, y=150, height=35)

l_exposicao = Label(tbFacial, font=('Ivy 12'),
                    text='Exposição ao sol', fg='#414141')
l_exposicao.place(x=20, y=200)
e_exposicaosim = Checkbutton(tbFacial, font=(
    'Ivy 12'), text='Sim', fg='#414141')
e_exposicaonao = Checkbutton(tbFacial, font=(
    'Ivy 12'), text='Não', fg='#414141')
e_exposicaosim.place(x=20, y=220)
e_exposicaonao.place(x=20, y=240)


l_maquiagem = Label(tbFacial, font=('Ivy 12'),
                    text='Usa maquiagem', fg='#414141')
l_maquiagem.place(x=170, y=200)
e_maquiagemsim = Checkbutton(tbFacial, font=(
    'Ivy 12'), text='Sim', fg='#414141')
e_maquiagemnao = Checkbutton(tbFacial, font=(
    'Ivy 12'), text='Não', fg='#414141')
e_maquiagemsim.place(x=170, y=220)
e_maquiagemnao.place(x=170, y=240)
e_quaismaquiagem = Text(tbFacial, relief='solid', width=15,
                        font=('Ivy 12'))
e_quaismaquiagem.place(x=170, y=270, height=35)


l_remocao = Label(tbFacial, font=('Ivy 12'),
                  text='Remove antes de dormir', fg='#414141')
l_remocao.place(x=320, y=200)
e_remocaosim = Checkbutton(tbFacial, font=(
    'Ivy 12'), text='Sim', fg='#414141')
e_remocaonao = Checkbutton(tbFacial, font=(
    'Ivy 12'), text='Não', fg='#414141')
e_remocaotalves = Checkbutton(tbFacial, font=(
    'Ivy 12'), text='as vezes', fg='#414141')
e_remocaosim.place(x=320, y=220)
e_remocaonao.place(x=320, y=240)
e_remocaotalves.place(x=320, y=260)


l_alergia = Label(tbFacial, font=('Ivy 12'),
                  text='Alergia a medicamentos \n cosméticos?', fg='#414141')
l_alergia.place(x=510, y=200)
e_alergiasim = Checkbutton(tbFacial, font=(
    'Ivy 12'), text='Sim', fg='#414141')
e_alergianao = Checkbutton(tbFacial, font=(
    'Ivy 12'), text='Não', fg='#414141')
e_alergiasim.place(x=510, y=240)
e_alergianao.place(x=510, y=260)
e_quaisalergia = Text(tbFacial, relief='solid', width=15,
                      font=('Ivy 12'))
e_quaisalergia.place(x=510, y=290, height=35)

# tbpele


fitzpatrick = ['Tipo I Pele muito clara, sempre queima, nunca bronzeia', 'Tipo II Pele clara, sempre queima e algumas vezes bronzeia', 'Tipo III Pele menos clara, algumas vezes queima e sempre bronzeia ',
               'Tipo IV Pele morena clara raramente queima e sempre bronzeia', 'Tipo V Pele morena escura, nunca queima e sempre bronzeia', 'Tipo VI Pele negra, nunca queima, sempre bronzeia ']
l_fitzpatrick = Label(tbPele, font=('Ivy 12'),
                      text='AVALIAÇÃO DA PELE\n FITZPATRICK', fg='#414141')
l_fitzpatrick.place(x=5, y=20)
c_fitzpatrick = ttk.Combobox(tbPele, font=(
    'Ivy 12'), state='readonly', width=40)
c_fitzpatrick['values'] = fitzpatrick
c_fitzpatrick.place(x=180, y=20)

l_biotipo = Label(tbPele, font=('Ivy 12'),
                  text='BIOTIPO CUTÂNEO', fg='#414141')
l_biotipo.place(x=5, y=80)

l_acne = Label(tbPele, font=('Ivy 12'),
               text='Pele com acne', fg='#414141')
l_acne.place(x=5, y=100)
e_alipica = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Alípica', fg='#414141')
e_lipidica = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Lipídica', fg='#414141')
e_eudermica = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Eudérmica', fg='#414141')
e_mista = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Mista', fg='#414141')
e_madura = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Madura', fg='#414141')
e_alipica.place(x=5, y=120)
e_lipidica.place(x=5, y=140)
e_eudermica.place(x=5, y=160)
e_mista.place(x=5, y=180)
e_madura.place(x=5, y=200)

l_discromias = Label(tbPele, font=('Ivy 12'),
                     text='Discromias', fg='#414141')
l_discromias.place(x=130, y=100)
e_grau1 = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Grau I ', fg='#414141')
e_grau2 = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Grau II', fg='#414141')
e_grau3 = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Grau III', fg='#414141')
e_grau4 = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Grau VI', fg='#414141')
e_grau5 = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Grau V', fg='#414141')
e_grau1.place(x=130, y=120)
e_grau2.place(x=130, y=140)
e_grau3.place(x=130, y=160)
e_grau4.place(x=130, y=180)
e_grau5.place(x=130, y=200)

l_rugas = Label(tbPele, font=('Ivy 12'),
                text='Rugas', fg='#414141')
l_rugas.place(x=230, y=100)
e_efelides = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Efélides ', fg='#414141')
e_gravidicas = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Mancha gravídica ', fg='#414141')
e_melasma = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Melasma', fg='#414141')
e_hipocromias = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Hipocromias', fg='#414141')
e_senis = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Manchas senis', fg='#414141')
e_efelides.place(x=230, y=120)
e_gravidicas.place(x=230, y=140)
e_melasma.place(x=230, y=160)
e_hipocromias.place(x=230, y=180)
e_senis.place(x=230, y=200)


l_profundas = Label(tbPele, font=('Ivy 12'),
                    text='Superficiais ou profundas', fg='#414141')
l_profundas.place(x=400, y=100)
e_dinamicas = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Dinâmicas ', fg='#414141')
e_estaticas = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Estáticas', fg='#414141')
e_gravitacionais = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Gravitacionais', fg='#414141')
e_sonos = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Sono', fg='#414141')
e_dinamicas.place(x=400, y=120)
e_estaticas.place(x=400, y=140)
e_gravitacionais.place(x=400, y=160)
e_sonos.place(x=400, y=180)

l_olheiras = Label(tbPele, font=('Ivy 12'),
                   text='Olheiras', fg='#414141')
l_olheiras.place(x=590, y=100)
e_olhos = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Sim ', fg='#414141')
e_olhon = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Não', fg='#414141')
e_olhos.place(x=590, y=120)
e_olhon.place(x=590, y=140)


l_tipo = Label(tbPele, font=('Ivy 12'),
               text='Tipo/Observação', fg='#414141')
l_tipo.place(x=690, y=100)
e_tipo = Text(tbPele, relief='solid', width=20,
              font=('Ivy 8'))
e_tipo.place(x=690, y=130, height=70)

l_flacidez = Label(tbPele, font=('Ivy 12'),
                   text='Flacidez: Quantificar os itens abaixo\n (+ leve, ++ moderado, +++ Intenso, ++++ grave) ', fg='#414141')
l_flacidez.place(x=5, y=250)
e_tissular = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Tissular ', fg='#414141')
e_muscular = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Muscular', fg='#414141')
e_tissular.place(x=5, y=290)
e_muscular.place(x=105, y=290)

l_localtissular = Label(tbPele, font=('Ivy 12'),
                        text='Localização da flacidez tissular', fg='#414141')
l_localtissular.place(x=5, y=320)
e_localtissular = Text(tbPele, relief='solid', width=30,
                       font=('Ivy 8'))
e_localtissular.place(x=5, y=350, height=30)

l_localmuscular = Label(tbPele, font=('Ivy 12'),
                        text='Localização da flacidez muscular', fg='#414141')
l_localmuscular.place(x=5, y=380)
e_localmuscular = Text(tbPele, relief='solid', width=30,
                       font=('Ivy 8'))
e_localmuscular.place(x=5, y=410, height=30)


l_cutaneo = Label(tbPele, font=('Ivy 12'),
                  text='Estado cutâneo', fg='#414141')
l_cutaneo.place(x=250, y=320)
e_cutaneonormal = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Normal ', fg='#414141')
e_cutaneodesidratado = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Desidratado', fg='#414141')
e_cutaneosensibilizado = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Sensibilizado', fg='#414141')
e_cutaneoacneico = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Acneico', fg='#414141')
e_cutaneoseborreico = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Seborreico', fg='#414141')
e_cutaneonormal.place(x=250, y=340)
e_cutaneodesidratado.place(x=250, y=360)
e_cutaneosensibilizado.place(x=250, y=380)
e_cutaneoacneico.place(x=250, y=400)
e_cutaneoseborreico.place(x=250, y=420)

l_lessao = Label(tbPele, font=('Ivy 12'),
                 text='Lesões', fg='#414141')
l_lessao.place(x=400, y=320)
e_comedoes = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Comedões abertos ', fg='#414141')
e_ptose = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Ptose ', fg='#414141')
e_comedoesfechados = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Comedões fechados ', fg='#414141')
e_eritema = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Eritema ', fg='#414141')
e_foliculite = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Foliculite ', fg='#414141')
e_ceratose = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Ceratose senil ', fg='#414141')
e_cisto = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Cisto ', fg='#414141')
e_psoriase = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Psoríase ', fg='#414141')
e_millium = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Millium ', fg='#414141')
e_cicatriz = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Cicatriz ', fg='#414141')
e_escoriacao = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Escoriação ', fg='#414141')
e_queloide = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Quelóide ', fg='#414141')
e_seborreia = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Seborréia ', fg='#414141')
e_verrugas = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Verrugas ', fg='#414141')
e_herpes = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Herpes ', fg='#414141')
e_rosacea = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Rosácea ', fg='#414141')
e_telangiectasia = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Telangiectasia ', fg='#414141')
e_xantelasma = Checkbutton(tbPele, font=(
    'Ivy 12'), text='Xantelasma ', fg='#414141')
e_comedoes.place(x=400, y=340)
e_ptose.place(x=400, y=360)
e_comedoesfechados.place(x=400, y=380)
e_eritema.place(x=400, y=400)
e_foliculite.place(x=400, y=420)
e_rosacea.place(x=400, y=440)
e_ceratose.place(x=590, y=340)
e_cisto.place(x=590, y=360)
e_psoriase.place(x=590, y=380)
e_millium.place(x=590, y=400)
e_cicatriz.place(x=590, y=420)
e_telangiectasia.place(x=590, y=440)
e_escoriacao.place(x=720, y=340)
e_queloide.place(x=720, y=360)
e_seborreia.place(x=720, y=380)
e_verrugas.place(x=720, y=400)
e_herpes.place(x=720, y=420)
e_xantelasma.place(x=720, y=440)


# tbcorporal

l_fibroedema = Label(tbCorporal, font=('Ivy 12'),
                     text='FIBROEDEMA GELÓIDE (FEG)', fg='#414141')
l_fibroedema.place(x=5, y=20)

e_flacida = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='Flácida', fg='#414141')
e_edematosa = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='Edematosa', fg='#414141')
e_compacta = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='Compacta', fg='#414141')
e_mistafibro = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='Mista', fg='#414141')
e_flacida.place(x=5, y=40)
e_edematosa.place(x=5, y=60)
e_compacta.place(x=5, y=80)
e_mistafibro.place(x=5, y=100)

e_fibgrau1 = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='Grau I ', fg='#414141')
e_fibgrau2 = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='Grau II', fg='#414141')
e_fibgrau3 = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='Grau III', fg='#414141')
e_fibgrau4 = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='Grau VI', fg='#414141')
e_fibgrau1.place(x=130, y=40)
e_fibgrau2.place(x=130, y=60)
e_fibgrau3.place(x=130, y=80)
e_fibgrau4.place(x=130, y=100)

l_localizacao = Label(tbCorporal, font=('Ivy 12'),
                      text='Localização', fg='#414141')
l_localizacao.place(x=250, y=20)
e_localizacao = Entry(tbCorporal, relief='solid', width=22,
                      justify='left', font=('Ivy 12'))
e_localizacao.place(x=250, y=50)

l_tecido = Label(tbCorporal, font=('Ivy 12'),
                 text='Coloração do tecido', fg='#414141')
l_tecido.place(x=250, y=80)
e_tecido = Entry(tbCorporal, relief='solid', width=22,
                 justify='left', font=('Ivy 12'))
e_tecido.place(x=250, y=110)

e_dor = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='Presença de dor à palpação', fg='#414141')
e_dor.place(x=5, y=140)

e_cacifo = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='Teste do cacifo', fg='#414141')
e_cacifo.place(x=5, y=160)

e_pressao = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='Teste de digito-pressão', fg='#414141')
e_pressao.place(x=5, y=180)

l_cansaco = Label(tbCorporal, font=('Ivy 12'),
                  text='Sensação de Peso\n Cansaço em MMII', fg='#414141')
l_cansaco.place(x=250, y=140)
e_cansaco = Entry(tbCorporal, relief='solid', width=22,
                  justify='left', font=('Ivy 12'))
e_cansaco.place(x=250, y=180)

l_gordura = Label(tbCorporal, font=('Ivy 12'),
                  text='Gordura', fg='#414141')
l_gordura.place(x=5, y=210)
e_gcompacta = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='Compacta', fg='#414141')
e_gcompacta.place(x=5, y=230)
e_gflacida = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='Flácida', fg='#414141')
e_gflacida.place(x=5, y=250)

e_glocal = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='Localizada', fg='#414141')
e_glocal.place(x=130, y=230)
e_ggeral = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='Generalizada', fg='#414141')
e_ggeral.place(x=130, y=250)


l_lipodistrofia = Label(tbCorporal, font=('Ivy 12'),
                        text='LIPODISTROFIA', fg='#414141')
l_lipodistrofia.place(x=480, y=20)

e_lcompacta = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='Compacta', fg='#414141')
e_lcompacta.place(x=480, y=40)
e_lflacida = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='Flácida', fg='#414141')
e_lflacida.place(x=480, y=60)

e_llocal = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='Localizada', fg='#414141')
e_llocal.place(x=480, y=80)
e_lgeral = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='Generalizada', fg='#414141')
e_lgeral.place(x=480, y=100)

l_llocalizacao = Label(tbCorporal, font=('Ivy 12'),
                       text='Localização', fg='#414141')
l_llocalizacao.place(x=630, y=20)
e_llocalizacao = Entry(tbCorporal, relief='solid', width=22,
                       justify='left', font=('Ivy 12'))
e_llocalizacao.place(x=630, y=50)

e_ginoide = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='Ginóide', fg='#414141')
e_ginoide.place(x=630, y=80)
e_androide = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='Andróide', fg='#414141')
e_androide.place(x=630, y=100)
e_mesomorfo = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='mesomorfo', fg='#414141')
e_mesomorfo.place(x=630, y=120)
e_ectomorfo = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='ectomorfo', fg='#414141')
e_ectomorfo.place(x=630, y=140)
e_endomorfo = Checkbutton(tbCorporal, font=(
    'Ivy 12'), text='endomorfo', fg='#414141')
e_endomorfo.place(x=630, y=160)


l_Peso = Label(tbCorporal, font=('Ivy 12'),
               text='Peso', fg='#414141')
l_Peso.place(x=630, y=190)
e_Peso = Entry(tbCorporal, relief='solid', width=22,
               justify='left', font=('Ivy 12'))
e_Peso.place(x=630, y=220)

l_Altura = Label(tbCorporal, font=('Ivy 12'),
                 text='Altura', fg='#414141')
l_Altura.place(x=630, y=250)
e_Altura = Entry(tbCorporal, relief='solid', width=22,
                 justify='left', font=('Ivy 12'))
e_Altura.place(x=630, y=280)

imc = ['Abaixo de 18,5', 'Entre 18,5 e 24,9', 'Entre 25,0 e 29,9',
       'Entre 30,0 e 34,9', 'Entre 35,0 e 39,9', '40,0 e acima']

l_imc = Label(tbCorporal, font=('Ivy 12'),
              text='IMC', fg='#414141')
l_imc.place(x=630, y=310)
c_imc = ttk.Combobox(tbCorporal, font=(
    'Ivy 12'), state='readonly', width=20)
c_imc['values'] = imc
c_imc.place(x=630, y=340)


# l_rugas = Label(tbCorporal, font=('Ivy 12'),
#                 text='Rugas', fg='#414141')
# l_rugas.place(x=230, y=100)
# e_efelides = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Efélides ', fg='#414141')
# e_gravidicas = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Mancha gravídica ', fg='#414141')
# e_melasma = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Melasma', fg='#414141')
# e_hipocromias = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Hipocromias', fg='#414141')
# e_senis = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Manchas senis', fg='#414141')
# e_efelides.place(x=230, y=120)
# e_gravidicas.place(x=230, y=140)
# e_melasma.place(x=230, y=160)
# e_hipocromias.place(x=230, y=180)
# e_senis.place(x=230, y=200)


# l_profundas = Label(tbCorporal, font=('Ivy 12'),
#                     text='Superficiais ou profundas', fg='#414141')
# l_profundas.place(x=400, y=100)
# e_dinamicas = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Dinâmicas ', fg='#414141')
# e_estaticas = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Estáticas', fg='#414141')
# e_gravitacionais = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Gravitacionais', fg='#414141')
# e_sonos = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Sono', fg='#414141')
# e_dinamicas.place(x=400, y=120)
# e_estaticas.place(x=400, y=140)
# e_gravitacionais.place(x=400, y=160)
# e_sonos.place(x=400, y=180)

# l_olheiras = Label(tbCorporal, font=('Ivy 12'),
#                    text='Olheiras', fg='#414141')
# l_olheiras.place(x=590, y=100)
# e_olhos = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Sim ', fg='#414141')
# e_olhon = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Não', fg='#414141')
# e_olhos.place(x=590, y=120)
# e_olhon.place(x=590, y=140)


# l_tipo = Label(tbCorporal, font=('Ivy 12'),
#                text='Tipo/Observação', fg='#414141')
# l_tipo.place(x=690, y=100)
# e_tipo = Text(tbCorporal, relief='solid', width=20,
#               font=('Ivy 8'))
# e_tipo.place(x=690, y=130, height=70)

# l_flacidez = Label(tbCorporal, font=('Ivy 12'),
#                    text='Flacidez: Quantificar os itens abaixo\n (+ leve, ++ moderado, +++ Intenso, ++++ grave) ', fg='#414141')
# l_flacidez.place(x=5, y=250)
# e_tissular = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Tissular ', fg='#414141')
# e_muscular = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Muscular', fg='#414141')
# e_tissular.place(x=5, y=290)
# e_muscular.place(x=105, y=290)

# l_localtissular = Label(tbCorporal, font=('Ivy 12'),
#                         text='Localização da flacidez tissular', fg='#414141')
# l_localtissular.place(x=5, y=320)
# e_localtissular = Text(tbCorporal, relief='solid', width=30,
#                        font=('Ivy 8'))
# e_localtissular.place(x=5, y=350, height=30)

# l_localmuscular = Label(tbCorporal, font=('Ivy 12'),
#                         text='Localização da flacidez muscular', fg='#414141')
# l_localmuscular.place(x=5, y=380)
# e_localmuscular = Text(tbCorporal, relief='solid', width=30,
#                        font=('Ivy 8'))
# e_localmuscular.place(x=5, y=410, height=30)


# l_cutaneo = Label(tbCorporal, font=('Ivy 12'),
#                   text='Estado cutâneo', fg='#414141')
# l_cutaneo.place(x=250, y=320)
# e_cutaneonormal = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Normal ', fg='#414141')
# e_cutaneodesidratado = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Desidratado', fg='#414141')
# e_cutaneosensibilizado = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Sensibilizado', fg='#414141')
# e_cutaneoacneico = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Acneico', fg='#414141')
# e_cutaneoseborreico = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Seborreico', fg='#414141')
# e_cutaneonormal.place(x=250, y=340)
# e_cutaneodesidratado.place(x=250, y=360)
# e_cutaneosensibilizado.place(x=250, y=380)
# e_cutaneoacneico.place(x=250, y=400)
# e_cutaneoseborreico.place(x=250, y=420)

# l_lessao = Label(tbCorporal, font=('Ivy 12'),
#                  text='Lesões', fg='#414141')
# l_lessao.place(x=400, y=320)
# e_comedoes = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Comedões abertos ', fg='#414141')
# e_ptose = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Ptose ', fg='#414141')
# e_comedoesfechados = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Comedões fechados ', fg='#414141')
# e_eritema = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Eritema ', fg='#414141')
# e_foliculite = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Foliculite ', fg='#414141')
# e_ceratose = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Ceratose senil ', fg='#414141')
# e_cisto = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Cisto ', fg='#414141')
# e_psoriase = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Psoríase ', fg='#414141')
# e_millium = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Millium ', fg='#414141')
# e_cicatriz = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Cicatriz ', fg='#414141')
# e_escoriacao = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Escoriação ', fg='#414141')
# e_queloide = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Quelóide ', fg='#414141')
# e_seborreia = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Seborréia ', fg='#414141')
# e_verrugas = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Verrugas ', fg='#414141')
# e_herpes = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Herpes ', fg='#414141')
# e_rosacea = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Rosácea ', fg='#414141')
# e_telangiectasia = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Telangiectasia ', fg='#414141')
# e_xantelasma = Checkbutton(tbCorporal, font=(
#     'Ivy 12'), text='Xantelasma ', fg='#414141')
# e_comedoes.place(x=400, y=340)
# e_ptose.place(x=400, y=360)
# e_comedoesfechados.place(x=400, y=380)
# e_eritema.place(x=400, y=400)
# e_foliculite.place(x=400, y=420)
# e_rosacea.place(x=400, y=440)
# e_ceratose.place(x=590, y=340)
# e_cisto.place(x=590, y=360)
# e_psoriase.place(x=590, y=380)
# e_millium.place(x=590, y=400)
# e_cicatriz.place(x=590, y=420)
# e_telangiectasia.place(x=590, y=440)
# e_escoriacao.place(x=720, y=340)
# e_queloide.place(x=720, y=360)
# e_seborreia.place(x=720, y=380)
# e_verrugas.place(x=720, y=400)
# e_herpes.place(x=720, y=420)
# e_xantelasma.place(x=720, y=440)


ficha.mainloop()
