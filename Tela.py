#importando as bibliotecas.
from tkinter import *
import backend as backend
from tkinter import Entry, messagebox


selected_tuple = None


# Função para obter a linha selecionada ao clicar na lista
def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    caixa_texto.delete('1.0', END)
    open_txt()

# Função para formatar a data inserida
def format_data(event=None):
    text = e2.get().replace("/", "").replace("/", "")[:8]
    new_text = ""

    if event.keysym.lower() == "backspace":
        return
    
    for index in range(len(text)):
        if not text[index] in "01234567":
            continue
        if index in [1, 3]:
            new_text += text[index] + "/"
        elif index == 8:
            new_text += text[index] + "/"
        else:
            new_text += text[index]

    e2.delete(0, "end")
    e2.insert(0, new_text)

# Função para abrir o conteúdo do arquivo de texto na caixa de texto
def open_txt():
    text_file = open("conteudo.txt", 'r')
    texto = text_file.read()
    caixa_texto.insert(END, texto)
    text_file.close()

# Função para salvar o conteúdo da caixa de texto em um arquivo de texto
def save_txt():
    text_file = open("conteudo.txt", 'w')
    text_file.write(caixa_texto.get(1.0, END))

# Função para exibir todas as tarefas na lista
def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

# Função para adicionar uma nova tarefa
def add_command():
    # Pequena validação dos dados na Entry
    if titulo.get() == "" or data.get() == "":
        msg = "Os campos não podem estar vazios \n"
        messagebox.showinfo("AVISO!", msg)
    else:
        backend.insert(titulo.get(), data.get())
        list1.delete(0, END)
        list1.insert(END, (titulo.get(), data.get()))
        # Limpando as informações na entry
        e1.delete(0, END)
        e2.delete(0, END)
        view_command()

# Função para adicionar uma nova tarefa a partir do texto
def add_command_txt():
    # Uma pequena verificação se existem dados no arquivo txt
    text_file = open("conteudo.txt", 'r')
    texto = text_file.read()
    if texto == "":
        msg = "Texto vazio \n"
        messagebox.showinfo("AVISO!", msg)
    else:
        e1.delete(0, END)
        e1.insert(END, texto)
        text_file.close()
    # Novamente uma validação de dados
    if titulo.get() == "" or data.get() == "":
        msg = "Os campos não podem estar vazios \n"
        messagebox.showinfo("AVISO!", msg)
    else:
        backend.insert(titulo.get(), data.get())
        list1.delete(0, END)
        list1.insert(END, (titulo.get(), data.get()))
        # Limpando as informações na entry
        e1.delete(0, END)
        e2.delete(0, END)
        view_command()

# Função para excluir a tarefa selecionada
def delete_command():
    try:
        backend.delete(selected_tuple[0])
        # Limpando as informações na entry
        e1.delete(0, END)
        e2.delete(0, END)
        view_command()

# Criando as caixas de aviso em caso de erro
    except FileNotFoundError as error:
        msg = "Não foi possível deletar arquivo \n"
        messagebox.showinfo("AVISO!", msg)

    except:
        msg = "Não foi possível deletar arquivo \n"
        messagebox.showinfo("AVISO!", msg)

# Função para atualizar a tarefa selecionada
def update_command():
    if titulo.get() == "" or data.get() == "":
        msg = "Os campos não podem estar vazios \n"
        messagebox.showinfo("AVISO!", msg)
    else:
        backend.update(selected_tuple[0], titulo.get(), data.get())
        # Limpando as informações na entry
        e1.delete(0, END)
        e2.delete(0, END)
        view_command()


#criando a tela principal do programa.
root = Tk()
root.title("GERENCIADOR DE TAREFAS")
width = 1060
height = 500

# coletando informações do monitor
sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)
# tamanho da janela principal
root.geometry("1015x543+216+95")
# cor da janela principal
root.config(bg='white')

# Criação de um frame
frame = Frame(root, bg= "#B0C4DE")
frame.place(relx=0.015, rely=0.015, relheight=0.945, relwidth=0.97)

# Criação das labels da entrada de dados

l1 = Label(root, text="Titulo da tarefa", fg='black',bg= "#B0C4DE")
l1.place(relx=0.05, rely=0.26, relheight=0.04, relwidth=0.09)
l2 = Label(root, text="Prazo", fg='black', bg= "#B0C4DE")
l2.place(relx=0.185, rely=0.26, relheight=0.04, relwidth=0.05)


# Criação das entrys para entrada de dados
titulo = StringVar()
e1 = Entry(root, bg= "white", textvariable=titulo)
e1.place(relx=0.05, rely=0.3, relheight=0.04, relwidth=0.09)
data = StringVar()
e2 = Entry(root, bg="white", textvariable=data)
e2.bind("<KeyRelease>", format_data)
e2.pack()
e2.place(relx=0.165, rely=0.3, relheight=0.04, relwidth=0.09)


# Criando list box para os dados do banco serem visualizados 
list1 = Listbox(root, bg= "white")
list1.place(relx=0.539, rely=0.07, relheight=0.4, relwidth=0.4)

list1.bind('<<ListboxSelect>>', get_selected_row)

# Criando a barra de rolamento da listbox
Scrollbarx = Scrollbar(root, orient=VERTICAL)
Scrollbarx.place(relx=0.929, rely=0.07, relheight=0.4, relwidth=0.02)

# Configurando a barra de rolamento da listbox
list1.configure(yscrollcommand=Scrollbarx.set)
Scrollbarx.configure(command=list1.yview)

# Criando caixa de texto para a visualização do arquivo txt
caixa_texto = Text(root, bg= "white")
caixa_texto.place(relx=0.045, rely=0.5, relheight=0.4, relwidth=0.9)

# Criando a barra de rolamento da caixa de texto
Scrollbarx2 = Scrollbar(root, orient=VERTICAL)
Scrollbarx2.place(relx=0.93, rely=0.5, relheight=0.4, relwidth=0.02)

# Configurando a barra de rolamento da caixa de texto
caixa_texto.configure(yscrollcommand=Scrollbarx2.set)
Scrollbarx2.configure(command=caixa_texto.yview)

# Criação de todos os botoes do programa
b1 = Button(root, text="Exibir registros",bg="#D3D3D3",command=view_command)
b1.place(relx=0.4, rely=0.09, relheight=0.06, relwidth=0.097)


b3 = Button(root, text="Incluir",bg="#8FBC8F", command=add_command)
b3.place(relx=0.06, rely=0.09, relheight=0.06, relwidth=0.075)

b4 = Button(root, text="Atualizar campo",bg="#F0E68C", command=update_command)
b4.place(relx=0.16, rely=0.09, relheight=0.06, relwidth=0.095)


b5 = Button(root, text="Deletar campo",bg="#FFA07A", command=delete_command)
b5.place(relx=0.28, rely=0.09, relheight=0.06, relwidth=0.09)


b6 = Button(root, text="Fechar",bg="#F08080", command=root.destroy)
b6.place(relx=0.409, rely=0.37, relheight=0.06, relwidth=0.075)

b7 = Button(root, text="Salvar texto",bg="#D3D3D3", command= save_txt)
b7.place(relx=0.06, rely=0.4, relheight=0.06, relwidth=0.09)

b8 = Button(root, text="Inserir do texto",bg="#D3D3D3", command=add_command_txt)
b8.place(relx=0.2, rely=0.4, relheight=0.06, relwidth=0.09)

root.mainloop()