# Biblioteca utilizada CustomTkinter, por enquanto ainda devo utilizar esta biblioteca
# até achar outra que tenha uma variedade melhor.
import customtkinter
from tkinter import messagebox

# Dicionário da bagagem, posteriormente deve-se referenciar diretamente para o banco de dados,
# então ainda é bem rústico.
bagagem = {
    "nomePessoa": None,
    "cpf": None,
    "tipoBagagem": "",
    "destinoBagagem": "",
    "pesoBagagem": 0,
    "valorBagagem": 0,
    "quantidadeItens": 0
}

def alerta():
    messagebox.showinfo("Atenção", "ATENÇÃO OS DADOS NÃO FORAM INSERIDOS!!!")

# Função de Cadastro principal da bagagem, ela deve ter todas as informações da bagagem.
# Futuramente refatorar para limpar possíveis linhas adicionais inúteis.
def cadastraBagagem():
    bagagem["nomePessoa"] = entradaNome.get()
    bagagem["cpf"] = entradaCpf.get()
    bagagem["tipoBagagem"] = entradaTipoBagagem.get()
    bagagem["quantidadeItens"] = entradaQtdBagagem.get()
    bagagem["destinoBagagem"] = entradaDestinoBagagem.get()
    
    if not bagagem["nomePessoa"] or not bagagem["cpf"]:
        alerta()
        return
    else:
        calculaPrecoBagagem()

# Função para calcular o preço da bagagem com base no destino e na quantidade de itens.
def calculaPrecoBagagem():
    precoUnidade = 0
    if bagagem["tipoBagagem"] == "Malas/Bolsas":
        precoUnidade = 5
    elif bagagem["tipoBagagem"] == "Comércio/Logista":
        precoUnidade = 6
    elif bagagem ["tipoBagagem"] == "Motores/Mecânica":
        precoUnidade = 10
    
    if bagagem["destinoBagagem"] == "Terminal":
        bagagem["valorBagagem"] = precoUnidade * int(bagagem["quantidadeItens"])
        telaDashboard()
    
    elif bagagem["destinoBagagem"] == "Rua":
            def calculaValorDestino():
                try:
                    qtdQuarteirao = int(entradaEnderecoBagagem.get())  # Converte para inteiro
                    valorBagagemItens = float(precoUnidade) * float(entradaQtdBagagem.get())  # Calcula valor total da bagagem
                
                    qtdQuarteiraoValor = (valorBagagemItens * qtdQuarteirao) / 4  # Ajuste conforme a regra de redução
                
                    bagagem["valorBagagem"] = valorBagagemItens + qtdQuarteiraoValor  # Armazena o valor no dicionário
                
                    mostraValor.configure(text=f"Valor: R$ {bagagem['valorBagagem']:.2f}")  # Exibe o valor atualizado
                except ValueError:
                    messagebox.showerror("Erro", "Por favor, insira um número válido de quarteirões.") 

            def finalizarCalculo():
                janelaDestinoBagagem.destroy()
                telaDashboard()
        
            janelaDestinoBagagem = customtkinter.CTkToplevel()
            janelaDestinoBagagem.geometry("400x300")
            janelaDestinoBagagem.grab_set()
            
            customtkinter.CTkLabel(janelaDestinoBagagem, text="Quantidade De Quarteirões").pack(pady=10)
            entradaEnderecoBagagem = customtkinter.CTkEntry(janelaDestinoBagagem)
            entradaEnderecoBagagem.pack(pady=5)
            
            btnCalcular = customtkinter.CTkButton(janelaDestinoBagagem, text="Calcular", command=calculaValorDestino)
            btnCalcular.pack(pady=5)
            
            mostraValor = customtkinter.CTkLabel(janelaDestinoBagagem, text="Valor: R$ 0.00")
            mostraValor.pack(pady=10)
            
            btnFinalizar = customtkinter.CTkButton(janelaDestinoBagagem, text="Finalizar", command=finalizarCalculo)
            btnFinalizar.pack(pady=10)

# Função que exibe a tela de dashboard da aplicação, ela abre a janela e fecha a janela app (Principal).
def telaDashboard():
    dashboard = customtkinter.CTkToplevel()
    dashboard.geometry("800x500")
    app.iconify()
    
    customtkinter.CTkLabel(dashboard, text="Dashboard Principal").pack(pady=10)
    customtkinter.CTkLabel(dashboard, text=f"Nome: {bagagem['nomePessoa']}").pack(pady=5)
    customtkinter.CTkLabel(dashboard, text=f"CPF: {bagagem['cpf']}").pack(pady=5)
    customtkinter.CTkLabel(dashboard, text=f"Valor Total: R$ {bagagem['valorBagagem']:.2f}").pack(pady=5)
    
    dashboard.grab_set()

# Função que inicia a janela principal do app.
app = customtkinter.CTk()
app.geometry("800x600")
customtkinter.CTkLabel(app, text='Cadastro').pack(pady=10)

entradaNome = customtkinter.CTkEntry(app, placeholder_text="Nome Do Cliente", width=300)
entradaNome.pack(pady=10)

entradaCpf = customtkinter.CTkEntry(app, placeholder_text="Cpf do Cliente", width=300)
entradaCpf.pack(pady=10)

customtkinter.CTkLabel(app, text='Tipo De Bagagem').pack()
entradaTipoBagagem = customtkinter.CTkComboBox(app, values=["Malas/Bolsas", "Comércio/Logista", "Motores/Mecânica"])
entradaTipoBagagem.pack(pady=10)

customtkinter.CTkLabel(app, text='Destino Da Bagagem').pack()
entradaDestinoBagagem = customtkinter.CTkComboBox(app, values=["Terminal", "Rua"])
entradaDestinoBagagem.pack(pady=10)


customtkinter.CTkLabel(app, text='Quantidade De Itens').pack()
entradaQtdBagagem = customtkinter.CTkEntry(app, placeholder_text="Quantidade", width=300)
entradaQtdBagagem.pack(pady=10)

btnCadastro = customtkinter.CTkButton(app, text="Cadastrar", command=cadastraBagagem)
btnCadastro.pack(pady=10)

app.mainloop()