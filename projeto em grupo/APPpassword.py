'''Desenvolva uma aplicação gráfica que permite ao utilizador gerar
passwords seguras. A interface deve incluir um campo para se definir o
comprimento da password, com um intervalo entre 8 e 16 caracteres, e
checkboxes para selecionar os tipos de caracteres desejados, como letras
maiúsculas, minúsculas, números e símbolos. Após definir os critérios, o
utilizador pode clicar num botão para gerar a password, que será exibida
num campo de texto somente leitura. Além disso, deve haver um botão
que permite copiar a password diretamente para a área de transferência.'''

import tkinter as tk
from random import choice
import string

class Menu():
    def __init__(self, root):
        self.root = root
        self.root.title('Password Generator')
        self.root.geometry('400x600')
        self.root.resizable(False, False)
        self.root.configure(background="#005cad")

        self.length_password()
        self.rules_btn()

    def length_password(self):
        self.pass_length_label = tk.Label(self.root, text= "Password Length:  ", font=('Helvetica', 14), 
        bg="#00297a", fg="#ffffff")
        self.pass_length_label.pack(pady=(5,5))
        self.pass_length_entry = tk.Spinbox(root, from_=8, to=16, width=2, relief="sunken",font=("Arial", 12), bg="lightgrey", fg="blue")
        self.pass_length_entry.pack(pady=(10,10))


    def rules_btn(self) -> None:
        self.maiusculas_out = tk.BooleanVar()
        self.minusculas_out = tk.BooleanVar()
        self.numeros_out = tk.BooleanVar()
        self.simbolos_out = tk.BooleanVar()

        self.boxes_geral_label = tk.Label(self.root, text= "Password Rules", font=('Helvetica', 14), bg="#00297a", fg="#ffffff")
        self.boxes_geral_label.pack(pady=(5,5))
        var_maiusculas = False
        var_minusculas = False
        var_numeros = False
        var_simbolos = False
        self.maiusculas = tk.Checkbutton(self.root, text="Uppers Case Letters",variable = self.maiusculas_out, command='')
        self.maiusculas.pack(pady=(5,5))
        self.minusculas = tk.Checkbutton(self.root, text="Lower Case Letters",variable = self.minusculas_out,  command='')
        self.minusculas.pack(pady=(5,5))
        self.numeros = tk.Checkbutton(self.root, text="Numbers", variable = self.numeros_out, command='')
        self.numeros.pack(pady=(5,5))
        self.simbolos = tk.Checkbutton(self.root, text="Symbols", variable = self.simbolos_out,  command='')
        self.simbolos.pack(pady=(5,5))
        self.generate_btn = tk.Button(self.root,text="Generate", font=('Helvetica', 10, 'bold'), width=10, bg = 'grey',command=self.generate_password, relief="sunken")
        self.generate_btn.pack(pady=(20,5))
        self.pass_lbl = tk.Label(self.root)
        self.pass_lbl.pack()

    def generate_password(self) -> None:
        self.pass_length = int(self.pass_length_entry.get())
        
        if self.pass_length > 16:
            self.pass_length = 16

        available_digits = ''
        password = ''
        if self.maiusculas_out.get():
            available_digits += string.ascii_uppercase
        if self.minusculas_out.get():
            available_digits +=  string.ascii_lowercase  
        if self.numeros_out.get():
            available_digits +=  string.digits
        if self.simbolos_out.get():
            available_digits +=  string.punctuation

        for i in range(self.pass_length):
            password += choice(available_digits)

        self.pass_lbl.config(text=password)

        
    def main(self):
        self.root = self.root_settings()
        self.length_password(self.root)
        self.rules_btn(self.root)
        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    app = Menu(root)
    root.mainloop()
