from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from ttkthemes import ThemedTk


def centralizar_janela(root_tk):
    root_tk.update_idletasks()
    largura_tela = root_tk.winfo_screenwidth()
    altura_tela = root_tk.winfo_screenheight()
    largura_janela = root_tk.winfo_width()
    altura_janela = root.winfo_height()
    margem_largura = (largura_tela // 2) - (largura_janela // 2)
    margem_altura = (altura_tela // 2) - (altura_janela // 2)
    root_tk.geometry(f'{largura_janela}x{altura_janela}+{margem_largura}+{margem_altura}')


def adicionar_tarefa(parent, listbox: Listbox):
    tarefa = simpledialog.askstring(title='Adicionar Tarefa', prompt='Tarefa para adicionar', parent=parent)
    if tarefa: listbox.insert(END, tarefa)
    else: messagebox.showerror('ERRO', 'Tarefa não foi definida')
    
def adicionar_cor_na_linha(index:int, listbox:Listbox):
    cor = '#FCDBDB'
    if listbox == listbox_central: cor = '#DFEBFD'
    if listbox == listbox_direito: cor = '#D6F9D5'
    if index % 2 == 0: listbox.itemconfig(index, bg=cor)
    
    
def adicionar_tarefa_e_cor_na_listbox(parent, listbox:Listbox):
    adicionar_tarefa(parent, listbox)
    index = listbox.size() - 1
    adicionar_cor_na_linha(index, listbox)
    
    
def mostrar_pop_up_esquerdo(evento):
    pop_up_esquerdo.post(evento.x_root, evento.y_root)


root = ThemedTk(theme='arc')
root.title('Kanban')
root.geometry('780x500')
root.resizable(False, False)
centralizar_janela(root)

frame_principal = Frame(root)
frame_principal.place(relx=0, rely=0, relwidth=1, relheight=1)

terceira_parte_da_janela = ((100/3)/100)

# Definindo configurações
width_widget = {'label': 125/260, 'listbox': 235/260, 'button_add': 125/260}
height_widget = {'label': 35/500, 'listbox': 340/500, 'button_add': 35/500}
relx = {'label': 15/260, 'listbox': 14/260, 'button_add': 14/260}
rely = {'label': 35/500, 'listbox': 85/500, 'button_add': 440/500}

# Criando e configrando Frames
frame_esquerdo = Frame(frame_principal, bg='#F5F5F5')
frame_esquerdo.place(relx=0, rely=0, relwidth=terceira_parte_da_janela, relheight=1)

frame_central = Frame(frame_principal, bg='#F5F5F5')
frame_central.place(relx=terceira_parte_da_janela, rely=0, relwidth=terceira_parte_da_janela, relheight=1)

frame_direito = Frame(frame_principal, bg='#F5F5F5')
frame_direito.place(relx=terceira_parte_da_janela*2, rely=0, relwidth=terceira_parte_da_janela, relheight=1)

# Criando e configrando Labels
label_titulo_esquerdo = Label(frame_esquerdo, text='Para Fazer', bg='#FCDBDB', fg='#B42C2C', font=('Verdana', 10))
label_titulo_esquerdo.place(relx=relx['label'], rely=rely['label'], relwidth=width_widget['label'], relheight=height_widget['label'])

label_titulo_central = Label(frame_central, text='Em Progresso', bg='#DFEBFD', fg='#013482', font=('Verdana', 10))
label_titulo_central.place(relx=relx['label'], rely=rely['label'], relwidth=width_widget['label'], relheight=height_widget['label'])

label_titulo_direito = Label(frame_direito, text='Concluído', bg='#D6F9D5', fg='#039400', font=('Verdana', 10))
label_titulo_direito.place(relx=relx['label'], rely=rely['label'], relwidth=width_widget['label'], relheight=height_widget['label'])

# Criando e configrando Listbox
listbox_esquerdo = Listbox(frame_esquerdo, font=('Roboto', 11), selectmode = "multiple")
listbox_esquerdo.place(relx=relx['listbox'], rely=rely['listbox'], relwidth=width_widget['listbox'], relheight=height_widget['listbox'])

listbox_central = Listbox(frame_central, font=('Roboto', 11), selectmode = "multiple")
listbox_central.place(relx=relx['listbox'], rely=rely['listbox'], relwidth=width_widget['listbox'], relheight=height_widget['listbox'])

listbox_direito = Listbox(frame_direito, font=('Roboto', 11), selectmode = "multiple")
listbox_direito.place(relx=relx['listbox'], rely=rely['listbox'], relwidth=width_widget['listbox'], relheight=height_widget['listbox'])

# Criando e configrando Buttons
button_adicionar_esquerdo = Button(frame_esquerdo, text='Adicionar +', font=('Verdana', 10))
button_adicionar_esquerdo.place(relx=relx['button_add'], rely=rely['button_add'], relwidth=width_widget['button_add'], relheight=height_widget['button_add'])

button_adicionar_central = Button(frame_central, text='Adicionar +', font=('Verdana', 10))
button_adicionar_central.place(relx=relx['button_add'], rely=rely['button_add'], relwidth=width_widget['button_add'], relheight=height_widget['button_add'])

button_adicionar_direito = Button(frame_direito, text='Adicionar +', font=('Verdana', 10))
button_adicionar_direito.place(relx=relx['button_add'], rely=rely['button_add'], relwidth=width_widget['button_add'], relheight=height_widget['button_add'])

# Criando e configurando pop-ups
pop_up_esquerdo = Menu(root, tearoff=0)
pop_up_esquerdo.add_command(label='Avançar')
pop_up_esquerdo.add_command(label='Editar')
pop_up_esquerdo.add_command(label='Excluir')

# Definindo funções dos Buttons
button_adicionar_esquerdo.config(command=lambda: adicionar_tarefa_e_cor_na_listbox(root, listbox_esquerdo))
button_adicionar_central.config(command=lambda: adicionar_tarefa_e_cor_na_listbox(root, listbox_central))
button_adicionar_direito.config(command=lambda: adicionar_tarefa_e_cor_na_listbox(root, listbox_direito))

# Definindo eventos
listbox_esquerdo.bind('<Button-3>', )


def mostrar_selecionados():
    listbox_esquerdo.selec

button_adicionar_esquerdo.bind("<Button-3>", func= mostrar_pop_up_esquerdo)

root.mainloop()
