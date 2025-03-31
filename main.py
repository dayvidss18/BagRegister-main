#Biblioteca Ultilizada CustomTkinetr, por enquanto ainda devo ultilizar esta biblioteca até achar outra que tenha uma variedade melhor.
import customtkinter
import requests
import webbrowser

#Dicionario da bagagem, posteriormente deve-se referenciar diretamente para o banco de dados, então ainda é bem rustico.
bagagem = {
    "nomePessoa": "",
    "cpf": "",
    "tipoBagagem": "",
    "destinoBagagem"
    "pesoBagagem" : 0,
    "valorBagagem" : 0,
    "quantidadeItens" : 0
}

#Função de Cadastro principal da bagagem, ela deve ter todas as informações da bagagem, futuramente refatorar para limpar possiveis linhas adicionais inuteis.
def cadastraBagagem():
    bagagem["nomePessoa"] = entradaNome.get(),
    bagagem["cpf"] = entradaCpf.get(),
    bagagem["pesoBagagem"] = entradaPesoBagagem.get(),
    bagagem["tipoBagagem"] = entradaTipoBagagem.get(),
    bagagem["quantidadeItens"] = entradaQtdBagagem.get()
    print(bagagem)
    telaDashboard()

def calculaPrecoBagagem():
    precoUnidade = 4
    if entradaDestinoBagagem.get() == "Terminal":
        bagagem["valorBagagem"] = precoUnidade * bagagem["quantidadeItens"]
    elif entradaDestinoBagagem.get() == "Rua":


#Função que define valor da bagagem, ela vai receber uma formula que trata uma serie de condições e para onde a bagagem deve ser levada
#Ex: se a bagagen for levada para dentro do terminal mesmo, somente sera levado em consideração o peso da bagagem e não a distancia.
#Ex2: Se a bagagem for levada para fora da rodoviaria sera levada em consideração o peso e a distancia, ainda não defini o preço a cada metragem mas esta no processo.



#Função que exibe a tela de dashboard da aplicação, ela abre a janela e fecha a janela app(Principal).
def telaDashboard():
    dashboard = customtkinter.CTkToplevel()
    dashboard.geometry("800x500")
    app.iconify()

    dashboard.grid_rowconfigure(0, weight=1)
    dashboard.grid_rowconfigure(1, weight=1)
    dashboard.grid_rowconfigure(2, weight=1)
    dashboard.grid_rowconfigure(3, weight=1)
    dashboard.grid_rowconfigure(4, weight=1)

    dashboard.grid_columnconfigure(0, weight=1)
    dashboard.grid_columnconfigure(1, weight=1)
    dashboard.grid_columnconfigure(2, weight=1)
    dashboard.grid_columnconfigure(3, weight=1)
    dashboard.grid_columnconfigure(4, weight=1)

    labelDashboard = customtkinter.CTkLabel(dashboard, text="Dashboard Principal" ,width=50, height=50, fg_color='transparent' )
    labelDashboard.grid(column=2 ,row=0)
    #labelDashboard.pack(padx=10,pady=10)

    InfoNomeCliente = customtkinter.CTkLabel(dashboard, text= bagagem["nomePessoa"],
                                                       width=50, height=50, fg_color='white',text_color="black",corner_radius=10 )
    InfoNomeCliente.grid(column=0 ,row=1)
    #InfoNomeCliente.pack(padx=10,pady=10)

    InfoCpfCliente = customtkinter.CTkLabel(dashboard, text= bagagem["cpf"],
                                                       width=50, height=50, fg_color='white',text_color="black" )
    InfoCpfCliente.grid(column=0 ,row=2)
    #InfoCpfCliente.pack(padx=10,pady=10)


    dashboard.grab_set_global()

    

#Função que inicia a janela principal do app, posteriormente terá que ser modificada para uma tela de acesso de usuario, não sei ainda se é necessario o uso de credencial.
app = customtkinter.CTk()
app.geometry("800x600")

labelTiltulo = customtkinter.CTkLabel(app, text='Cadastro', width=50, height=50, fg_color='transparent')
labelTiltulo.grid(column=1 ,row=1)
labelTiltulo.pack(padx=10,pady=10)

entradaNome = customtkinter.CTkEntry(app,placeholder_text="Nome Do Cliente",width=300,height=40,)
entradaNome.pack(padx=10,pady=10)

entradaCpf = customtkinter.CTkEntry(app,placeholder_text="Cpf do Cliente",width=300,height=40,)
entradaCpf.pack(padx=10,pady=10)

#Função que exibe os tipos de bagagem e define o tipo.

labelTiltuloTipoBagagem = customtkinter.CTkLabel(app, text='Tipo De Bagagem', width=50, height=30, fg_color='transparent')
labelTiltuloTipoBagagem.pack()

entradaTipoBagagem = customtkinter.CTkComboBox(app, values=["Malas/Bolsas", "Comércio/Logista", "Motores/Mecânica"])
entradaTipoBagagem.pack(pady=10)

labelTiltuloDestinoBagagem = customtkinter.CTkLabel(app, text='Destino Da Bagagem', width=50, height=30, fg_color='transparent')
labelTiltuloDestinoBagagem.pack()

entradaDestinoBagagem = customtkinter.CTkComboBox(app, values=["Terminal", "Rua"])
entradaDestinoBagagem.pack(padx=10,pady=10)

entradaPesoBagagem = customtkinter.CTkEntry(app,placeholder_text="Peso Bagagem",width=300,height=40,)
entradaPesoBagagem.pack(padx=10,pady=10)

labelTiltuloQtdBagagem = customtkinter.CTkLabel(app, text='Quantidade De Itens', width=50, height=30, fg_color='transparent')
labelTiltuloQtdBagagem.pack()

entradaQtdBagagem = customtkinter.CTkEntry(app,placeholder_text="Nome",width=300,height=40,)
entradaQtdBagagem.pack(padx=10,pady=10)


btnCadastro = customtkinter.CTkButton(app,text="Cadastrar",width=50, height=30,command=cadastraBagagem)
btnCadastro.pack(padx=10,pady=10)

app.mainloop()
