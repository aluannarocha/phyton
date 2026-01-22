from reportlab.pdfgen import canvas
class Conta:
    def __init__ (self, titular:str, saldo:float, nib:str, limite: float):
        self.__titular = titular
        self.__saldo = saldo
        self.__nib = nib
        self.__limite =limite

    def __str___ (self):
        return (f' BANCO FANS FANS \n'
                f'titular: {self.__titular}\n'
                f'Limite: {self.__nib}')

    # --- TITULAR ---
    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, novo_titular):
        self.__titular = novo_titular

    # --- SALDO ---
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        self.__saldo = novo_saldo

    # --- NIB ---
    @property
    def nib(self):
        return self.__nib

    # --- LIMITE ---
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        if novo_limite < 0:
            print("Erro: O limite não pode ser negativo.")
        else:
            self.__limite = novo_limite

    def obter_comprovativo(self):
    nome_arquivo = f'{self.__titular.lower()}-comprovativo-nib.pdf'

    # criar a variável que representa uma folha do pdf
    c = canvas.Canvas (nome_arquivo)

    # definir o tipo de letra
    c.setFont('Helvetica', 22)

    # escrever as coisas
    c.drawString(100,700,self.__str__())

    # gravar o pdf
    c.save()

    print(f'{nome_arquivo} gerado com sucesso.')