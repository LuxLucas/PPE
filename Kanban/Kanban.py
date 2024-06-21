from tkinter import *
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


root = ThemedTk(theme='arc')
root.title('Kanban')
root.geometry('780x500')
root.resizable(False, False)
centralizar_janela(root)

frame_principal = Frame(root, bg='white')
frame_principal.place(relx=0, rely=0, relwidth=1, relheight=1)

terceira_parte_da_janela = ((100/3)/100)

frame_esquerdo = Frame(frame_principal, bg='white')
frame_esquerdo.place(relx=0, rely=0, relwidth=terceira_parte_da_janela, relheight=1)

frame_central = Frame(frame_principal, bg='white')
frame_central.place(relx=terceira_parte_da_janela, rely=0, relwidth=terceira_parte_da_janela, relheight=1)

frame_direito = Frame(frame_principal, bg='white')
frame_direito.place(relx=terceira_parte_da_janela*2, rely=0, relwidth=terceira_parte_da_janela, relheight=1)

width_widget = {'label': 125/260, 'listbox': 235/260, 'button_add': 125/260}
height_widget = {'label': 35/500, 'listbox': 340/500, 'button_add': 35/500}
relx = {'label': 15/260, 'listbox': 14/260, 'button_add': 14/260}
rely = {'label': 35/500, 'listbox': 85/500, 'button_add': 440/500}

label_titulo_esquerdo = Label(frame_esquerdo, text='Para Fazer', bg='#FCDBDB', fg='#B42C2C', font=('Verdana', 10))
label_titulo_esquerdo.place(relx=relx['label'], rely=rely['label'], relwidth=width_widget['label'], relheight=height_widget['label'])

label_titulo_central = Label(frame_central, text='Em Progresso', bg='#DFEBFD', fg='#013482', font=('Verdana', 10))
label_titulo_central.place(relx=relx['label'], rely=rely['label'], relwidth=width_widget['label'], relheight=height_widget['label'])

label_titulo_direito = Label(frame_direito, text='Concluído', bg='#D6F9D5', fg='#039400', font=('Verdana', 10))
label_titulo_direito.place(relx=relx['label'], rely=rely['label'], relwidth=width_widget['label'], relheight=height_widget['label'])

listbox_esquerdo = Listbox(frame_esquerdo)
listbox_esquerdo.place(relx=relx['listbox'], rely=rely['listbox'], relwidth=width_widget['listbox'], relheight=height_widget['listbox'])

listbox_central = Listbox(frame_central)
listbox_central.place(relx=relx['listbox'], rely=rely['listbox'], relwidth=width_widget['listbox'], relheight=height_widget['listbox'])

listbox_direito = Listbox(frame_direito)
listbox_direito.place(relx=relx['listbox'], rely=rely['listbox'], relwidth=width_widget['listbox'], relheight=height_widget['listbox'])

button_adicionar_esquerdo = Button(frame_esquerdo, text='Adicionar +', font=('Verdana', 10))
button_adicionar_esquerdo.place(relx=relx['button_add'], rely=rely['button_add'], relwidth=width_widget['button_add'], relheight=height_widget['button_add'])

button_adicionar_central = Button(frame_central, text='Adicionar +', font=('Verdana', 10))
button_adicionar_central.place(relx=relx['button_add'], rely=rely['button_add'], relwidth=width_widget['button_add'], relheight=height_widget['button_add'])

button_adicionar_direito = Button(frame_direito, text='Adicionar +', font=('Verdana', 10))
button_adicionar_direito.place(relx=relx['button_add'], rely=rely['button_add'], relwidth=width_widget['button_add'], relheight=height_widget['button_add'])

root.mainloop()
