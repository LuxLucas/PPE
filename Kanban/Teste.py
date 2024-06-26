import tkinter as tk

root = tk.Tk()
mylist = ['um', 'dois', 'três']
var = tk.StringVar(value=mylist)
box = tk.Listbox(master=root, listvariable=var)
box.pack(fill=tk.BOTH, expand=True)

# Modifique a lista
mylist.append('quatro')
mylist.remove('dois')
mylist.insert(3, mylist.pop(1))
var.set(mylist)

root.mainloop()
