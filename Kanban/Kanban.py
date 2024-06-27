from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox


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
    if tarefa:
        listbox.insert(END, tarefa)
    else:
        messagebox.showerror('ERRO', 'Tarefa não foi definida')


def adicionar_cor_na_linha(index: int, listbox: Listbox):
    cor = '#FCDBDB'
    if listbox == listbox_central:
        cor = '#DFEBFD'
    if listbox == listbox_direito:
        cor = '#D6F9D5'
    listbox.itemconfig(index, bg=cor if index % 2 == 0 else 'white')


def reconfigurar_todas_as_cores_nas_linhas(lb: Listbox):
    linhas = lb.size()
    if linhas:
        for linha_index in range(linhas):
            adicionar_cor_na_linha(linha_index, lb)


def contar_tarefas(lb: Listbox) -> str:
    quantidade_de_tarefas = lb.size() if lb.size() < 100 else '+99'
    return str(quantidade_de_tarefas)


def atualizar_label_de_contagem(label: Label, lb: Listbox):
    quantidade_de_tarefas = contar_tarefas(lb)
    label.config(text=quantidade_de_tarefas)
    

def adicionar_tarefa_e_cor_na_listbox(parent, listbox: Listbox):
    adicionar_tarefa(parent, listbox)
    index = listbox.size() - 1
    adicionar_cor_na_linha(index, listbox)
    label_correspondente = encontrar_label_contador_correspondente(listbox)
    atualizar_label_de_contagem(label_correspondente, listbox)


def mostrar_pop_up_esquerdo(evento):
    pop_up_esquerdo.post(evento.x_root, evento.y_root)


def mostrar_pop_up_central(evento):
    pop_up_central.post(evento.x_root, evento.y_root)


def mostrar_pop_up_direito(evento):
    pop_up_direito.post(evento.x_root, evento.y_root)


def encontrar_label_contador_correspondente(listbox: Listbox) -> Label:
    if listbox == listbox_esquerdo:
        return label_contagem_esquerdo
    if listbox == listbox_central:
        return label_contagem_central
    if listbox == listbox_direito:
        return label_contagem_direito


def excluir_linhas_selecionada(lb: Listbox):
    usuario_deseja_excluir = messagebox.askyesno('Aviso', 'Deseja realmente excluir?')
    if usuario_deseja_excluir:
        linhas_selecionadas = lb.curselection()
        if linhas_selecionadas:
            for linha_index in linhas_selecionadas[::-1]:
                lb.delete(linha_index)
            reconfigurar_todas_as_cores_nas_linhas(lb)
            label_correspondente = encontrar_label_contador_correspondente(lb)
            atualizar_label_de_contagem(label_correspondente, lb)
        else:
            messagebox.showerror('Erro', 'Linha não foi selecionda').title()


def editar_linhas_selecionadas(lb: Listbox, pai):
    linhas_selecionadas = lb.curselection()
    if linhas_selecionadas:
        for linha_index in linhas_selecionadas:
            tarefa_antiga = lb.get(linha_index)
            novo_titulo = simpledialog.askstring('Editar Tarefa', 'Edite sua tarefa', parent=pai, initialvalue=tarefa_antiga)
            if novo_titulo:
                lb.delete(linha_index)
                lb.insert(linha_index, novo_titulo)
                reconfigurar_todas_as_cores_nas_linhas(lb)
    else:
        messagebox.showerror('Erro', 'Linha não foi selecionda').title()


def mudar_estado_da_tarefa(estado_atual: Listbox, novo_estado: Listbox):
    linhas_selecionadas = estado_atual.curselection()
    if linhas_selecionadas:
        for linha_index in linhas_selecionadas:
            tarefa = estado_atual.get(linha_index)
            novo_estado.insert(END, tarefa)
        for linha_index in linhas_selecionadas[::-1]:
            estado_atual.delete(linha_index)
        reconfigurar_todas_as_cores_nas_linhas(estado_atual)
        reconfigurar_todas_as_cores_nas_linhas(novo_estado)
        label_correspondente = encontrar_label_contador_correspondente(estado_atual)
        atualizar_label_de_contagem(label_correspondente, estado_atual)
        label_correspondente = encontrar_label_contador_correspondente(novo_estado)
        atualizar_label_de_contagem(label_correspondente, novo_estado)
    else:
        messagebox.showerror('Erro', 'Linha não foi selecionda')


root = Tk()
root.title('Kanban')
root.geometry('780x500')
root.resizable(False, False)
centralizar_janela(root)

frame_principal = Frame(root)
frame_principal.place(relx=0, rely=0, relwidth=1, relheight=1)

terceira_parte_da_janela = ((100/3)/100)

# Definindo configurações
width_widget = {'label_contador': 35/260,'label_titulo': 125/260, 'listbox': 235/260, 'button_add': 125/260}
height_widget = {'label_contador': 35/500, 'label_titulo': 35/500, 'listbox': 340/500, 'button_add': 35/500}
relx = {'label_contador': 215/260, 'label_titulo': 15/260, 'listbox': 14/260, 'button_add': 14/260}
rely = {'label_contador': 35/500, 'label_titulo': 35/500, 'listbox': 85/500, 'button_add': 440/500}

# Criando e configrando Frames
frame_esquerdo = Frame(frame_principal, bg='#F5F5F5')
frame_esquerdo.place(relx=0, rely=0, relwidth=terceira_parte_da_janela, relheight=1)

frame_central = Frame(frame_principal, bg='#F5F5F5')
frame_central.place(relx=terceira_parte_da_janela, rely=0, relwidth=terceira_parte_da_janela, relheight=1)

frame_direito = Frame(frame_principal, bg='#F5F5F5')
frame_direito.place(relx=terceira_parte_da_janela*2, rely=0, relwidth=terceira_parte_da_janela, relheight=1)

# Criando e configrando Labels

# Labels título
label_titulo_esquerdo = Label(frame_esquerdo, text='Para Fazer', bg='#FCDBDB', fg='#B42C2C', font=('Verdana', 10))
label_titulo_esquerdo.place(relx=relx['label_titulo'],
                            rely=rely['label_titulo'],
                            relwidth=width_widget['label_titulo'],
                            relheight=height_widget['label_titulo'])

label_titulo_central = Label(frame_central, text='Em Progresso', bg='#DFEBFD', fg='#013482', font=('Verdana', 10))
label_titulo_central.place(relx=relx['label_titulo'],
                           rely=rely['label_titulo'],
                           relwidth=width_widget['label_titulo'],
                           relheight=height_widget['label_titulo'])

label_titulo_direito = Label(frame_direito, text='Concluído', bg='#D6F9D5', fg='#039400', font=('Verdana', 10))
label_titulo_direito.place(relx=relx['label_titulo'],
                           rely=rely['label_titulo'],
                           relwidth=width_widget['label_titulo'],
                           relheight=height_widget['label_titulo'])

# Criando e configrando Listbox
listbox_esquerdo = Listbox(frame_esquerdo, font=('Roboto', 11), selectmode="multiple")
listbox_esquerdo.place(relx=relx['listbox'],
                       rely=rely['listbox'],
                       relwidth=width_widget['listbox'],
                       relheight=height_widget['listbox'])

listbox_central = Listbox(frame_central, font=('Roboto', 11), selectmode="multiple")
listbox_central.place(relx=relx['listbox'],
                      rely=rely['listbox'],
                      relwidth=width_widget['listbox'],
                      relheight=height_widget['listbox'])

listbox_direito = Listbox(frame_direito, font=('Roboto', 11), selectmode="multiple")
listbox_direito.place(relx=relx['listbox'],
                      rely=rely['listbox'],
                      relwidth=width_widget['listbox'],
                      relheight=height_widget['listbox'])

# Criando e configrando Buttons
button_adicionar_esquerdo = Button(frame_esquerdo, text='Adicionar +', font=('Verdana', 10))
button_adicionar_esquerdo.place(relx=relx['button_add'],
                                rely=rely['button_add'],
                                relwidth=width_widget['button_add'],
                                relheight=height_widget['button_add'])

button_adicionar_central = Button(frame_central, text='Adicionar +', font=('Verdana', 10))

button_adicionar_central.place(relx=relx['button_add'],
                               rely=rely['button_add'],
                               relwidth=width_widget['button_add'],
                               relheight=height_widget['button_add'])

button_adicionar_direito = Button(frame_direito, text='Adicionar +', font=('Verdana', 10))
button_adicionar_direito.place(relx=relx['button_add'],
                               rely=rely['button_add'],
                               relwidth=width_widget['button_add'],
                               relheight=height_widget['button_add'])

# Criando e configurando pop-ups
pop_up_esquerdo = Menu(frame_principal, tearoff=0, font=('Roboto', 9))
pop_up_esquerdo.add_command(label='Add in "Em progresso"', command=lambda: mudar_estado_da_tarefa(listbox_esquerdo, listbox_central))
pop_up_esquerdo.add_command(label='Editar', command=lambda: editar_linhas_selecionadas(listbox_esquerdo, frame_principal))
pop_up_esquerdo.add_command(label='Excluir', command=lambda: excluir_linhas_selecionada(listbox_esquerdo))

pop_up_central = Menu(frame_principal, tearoff=0, font=('Roboto', 9))
pop_up_central.add_command(label='Adicionar em "Concluído"', command=lambda: mudar_estado_da_tarefa(listbox_central, listbox_direito))
pop_up_central.add_command(label='Voltar em "Para Fazer"', command=lambda: mudar_estado_da_tarefa(listbox_central, listbox_esquerdo))
pop_up_central.add_command(label='Editar', command=lambda: editar_linhas_selecionadas(listbox_central, frame_principal))
pop_up_central.add_command(label='Excluir', command=lambda: excluir_linhas_selecionada(listbox_central))

pop_up_direito = Menu(frame_principal, tearoff=0, font=('Roboto', 9))
pop_up_direito.add_command(label='Voltar para "Em Progresso"', command=lambda: mudar_estado_da_tarefa(listbox_direito, listbox_central))
pop_up_direito.add_command(label='Editar', command=lambda: editar_linhas_selecionadas(listbox_direito, frame_principal))
pop_up_direito.add_command(label='Excluir', command=lambda: excluir_linhas_selecionada(listbox_direito))

# Definindo funções dos Buttons
button_adicionar_esquerdo.config(command=lambda: adicionar_tarefa_e_cor_na_listbox(frame_principal, listbox_esquerdo))
button_adicionar_central.config(command=lambda: adicionar_tarefa_e_cor_na_listbox(frame_principal, listbox_central))
button_adicionar_direito.config(command=lambda: adicionar_tarefa_e_cor_na_listbox(frame_principal, listbox_direito))

# Labels de contagem
label_contagem_esquerdo = Label(frame_esquerdo, text=contar_tarefas(listbox_esquerdo), bg='#FCDBDB', fg='#B42C2C', font=('Verdana', 10))
label_contagem_esquerdo.place(relx=relx['label_contador'], 
                              rely=rely['label_contador'], 
                              relwidth=width_widget['label_contador'], 
                              relheight=height_widget['label_contador'])

label_contagem_central = Label(frame_central, text=contar_tarefas(listbox_central), bg='#DFEBFD', fg='#013482', font=('Verdana', 10))
label_contagem_central.place(relx=relx['label_contador'], 
                              rely=rely['label_contador'], 
                              relwidth=width_widget['label_contador'], 
                              relheight=height_widget['label_contador'])
                              
label_contagem_direito = Label(frame_direito, text=contar_tarefas(listbox_direito), bg='#D6F9D5', fg='#039400', font=('Verdana', 10))
label_contagem_direito.place(relx=relx['label_contador'], 
                              rely=rely['label_contador'], 
                              relwidth=width_widget['label_contador'], 
                              relheight=height_widget['label_contador'])

# Definindo eventos
listbox_esquerdo.bind('<Button-3>', mostrar_pop_up_esquerdo)
listbox_central.bind('<Button-3>', mostrar_pop_up_central)
listbox_direito.bind('<Button-3>', mostrar_pop_up_direito)

root.mainloop()
