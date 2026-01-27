import tkinter as tk
from tkinter import filedialog, messagebox


class BlocoNotas:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title('Bloco de Notas')
        # State define o estado da janela
        # normal (é o padrão)
        # iconic (minimiza a janela)
        # withdraw (janela fica aberta por trás das cortinas)
        # zoomed (maximizado)
        self.root.state('zoomed')

        # Criar a área de escrita
        self.text_area = tk.Text(self.root, undo=True, font=('Helvetica', 18), bg="#25213f", fg='white')
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # criar um menu que simule "Ficheiro"
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # adicionar ficheiro ao menu, gravar e o sair
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='Ficheiro', menu=file_menu)
        file_menu.add_command(label='Gravar', command=self.gravar_ficheiro)
        file_menu.add_separator()
        file_menu.add_command(label='Sair', command=self.root.quit)

    def gravar_ficheiro(self):
        
        ficheiro = filedialog.asksaveasfilename(
            initialfile='fansfans.txt',
            defaultextension='.txt',
            filetypes=[('Ficheiros de texto', '*.txt'), ('Todos os ficheiros', '*.*')]
        )

        if ficheiro:
            try:
                conteudo = self.text_area.get(1.0, tk.END)
                
                with open(ficheiro, 'w', encoding='utf-8', errors='ignore') as f:
                    f.write(conteudo)

                self.root.title(f'Bloco de Notas - {ficheiro}')
                
            except Exception as e:
                messagebox.showerror('ERRO! CRLH!', f'Não foi possível guardar: {str(e)}')

root = tk.Tk()
app = BlocoNotas(root)
root.mainloop()