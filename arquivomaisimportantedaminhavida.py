import customtkinter as ctk
from datetime import datetime
from PIL import Image, ImageTk  # Importando o Pillow para trabalhar com imagens

# Função para validar a data
def validar_data(data_str):
    try:
        # Tenta converter a string para o formato dd/mm/aaaa
        datetime.strptime(data_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

# Função que será chamada quando o botão for pressionado
def agendar_férias():
    inicio_usuario = entry_inicio.get()  # Pega a data do campo de entrada
    fim_usuario = entry_fim.get()        # Pega a data do campo de entrada
    
    # Validação das datas
    if not validar_data(inicio_usuario) or not validar_data(fim_usuario):
        label_confirmacao.configure(text="Por favor, insira as datas no formato dd/mm/aaaa!")
        return
    
    # Mensagem de confirmação
    label_confirmacao.configure(text="Seu pedido de férias foi agendado com sucesso!")

# Criando a janela principal
root = ctk.CTk()

# Título da janela
root.title("GMEQ/EM - Previsão de Férias")

# Definindo o tamanho da janela
root.geometry("600x500")  # Aumentei o tamanho da janela

# Carregando a imagem usando PIL
icone_imagem = Image.open("C:/Users/thiag/Downloads/baixados.png")

# Redimensionando a imagem para um tamanho apropriado (tamanho típico de ícone)
icone_imagem = icone_imagem.resize((16, 16))  # Tamanho adequado para ícone

# Convertendo a imagem para o formato que o Tkinter aceita
icone_imagem_tk = ImageTk.PhotoImage(icone_imagem)

# Definindo o ícone da janela
root.iconphoto(True, icone_imagem_tk)

# Criando um frame para centralizar os widgets
frame_central = ctk.CTkFrame(root)
frame_central.place(relx=0.5, rely=0.5, anchor="center")  # Colocando o frame no centro da janela

# Criando widgets com fontes e tamanhos maiores
label_boas_vindas = ctk.CTkLabel(frame_central, text="Bem-vindo à GMEQ/EM", font=("Arial", 24))
label_boas_vindas.grid(row=0, column=0, pady=10)

label_previsao = ctk.CTkLabel(frame_central, text="Insira aqui sua previsão de férias", font=("Arial", 18))
label_previsao.grid(row=1, column=0, pady=10)

label_inicio = ctk.CTkLabel(frame_central, text="Data início (dd/mm/aaaa):", font=("Arial", 16))
label_inicio.grid(row=2, column=0, pady=10)
entry_inicio = ctk.CTkEntry(frame_central, font=("Arial", 16))
entry_inicio.grid(row=3, column=0, pady=10)

label_fim = ctk.CTkLabel(frame_central, text="Data fim (dd/mm/aaaa):", font=("Arial", 16))
label_fim.grid(row=4, column=0, pady=10)
entry_fim = ctk.CTkEntry(frame_central, font=("Arial", 16))
entry_fim.grid(row=5, column=0, pady=10)

# Botão para agendar com fonte maior
botao_agendar = ctk.CTkButton(frame_central, text="Agendar Férias", font=("Arial", 16), command=agendar_férias)
botao_agendar.grid(row=6, column=0, pady=20)

# Label para exibir a confirmação com fonte maior
label_confirmacao = ctk.CTkLabel(frame_central, text="", font=("Arial", 18))
label_confirmacao.grid(row=7, column=0, pady=10)

# Iniciando a interface gráfica
root.mainloop()




