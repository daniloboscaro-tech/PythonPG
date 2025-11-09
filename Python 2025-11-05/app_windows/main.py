import tkinter as tk
from tkinter import messagebox

def hello():
    Nome = name_text.get()
    Cognome = cognome_text.get()

    messagebox.showinfo('Hello', f'{Nome} {Cognome}')
    name_text.delete(0, tk.END)
    cognome_text.delete(0, tk.END)


windows = tk.Tk()
windows.title('Calcolo quantità pediatrica farmaco')
windows.geometry('800x450')

lable_main = tk.Label(text = 'Prima applicazione Python per Windows')
lable_main.pack(pady = 10)

label_name = tk.Label(
    text = 'Inserisci il tuo nome'
)
label_name.pack()
name_text = tk.Entry()
name_text.pack()

label_cognome = tk.Label(
    text = 'Inserisci il tuo cognome'
)
label_cognome.pack(pady = 10)
cognome_text = tk.Entry()
cognome_text.pack()

hello_buttom = tk.Button(
    text = 'Clicca dopo inserimento',
    background = 'cyan',
    command = hello
)
hello_buttom.pack(pady = 10)

windows.mainloop()