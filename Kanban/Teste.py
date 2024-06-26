import tkinter as tk

def showSelected():
    selected_items = lb.curselection()
    selected_values = [lb.get(index) for index in selected_items]
    show.config(text=", ".join(selected_values))

def remove_selected():
    selected_items = lb.curselection()
    for index in selected_items[::-1]:  # Reverse order to avoid index shifting
        lb.delete(index)

def show_popup(event):
    popup_menu.post(event.x_root, event.y_root)

ws = tk.Tk()
ws.title('Python Guides')
ws.geometry('400x300')
ws.config(bg='#446644')

lb = tk.Listbox(ws, selectmode=tk.MULTIPLE)
lb.pack()
lb.insert(0, 'red')
lb.insert(1, 'green')
lb.insert(2, 'yellow')
lb.insert(3, 'blue')

show = tk.Label(ws)
show.pack()

show_button = tk.Button(ws, text='Show Selected', command=showSelected)
show_button.pack(pady=10)

remove_button = tk.Button(ws, text='Remove Selected', command=remove_selected)
remove_button.pack(pady=10)

# Create a popup menu
popup_menu = tk.Menu(ws, tearoff=0)
popup_menu.add_command(label="Show Selected", command=showSelected)
popup_menu.add_command(label="Remove Selected", command=remove_selected)

# Bind the right-click event to show the popup menu
lb.bind("<Button-3>", show_popup)

ws.mainloop()
