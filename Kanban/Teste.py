from tkinter import *
from ttkthemes import ThemedTk

window = ThemedTk(theme='adapta')
window.configure(background='white')
window.geometry('200x200')

Button(window, text="Adicionar +", font=('Verdana, 10'), command=window.destroy).place(relx=0.25, rely=0.25)
window.mainloop()
