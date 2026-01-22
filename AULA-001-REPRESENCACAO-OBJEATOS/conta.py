from reportlab.pdfgen import canvas

class Conta:
    def __init__(self, titular: str, saldo: float, nib: str, limite: float):
        self.__titular = titular
        self.__saldo = saldo
        self.__nib = nib
        self.__limite = limite

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

    def __str__(self):
        return f'BANCO FANS FANS\nTITULAR: {self.__titular}\nIBAN: {self.__nib}'
    

    def obter_comprovativo(self):
        # dar o nome ao ficheiro
        nome_arquivo = f'{self.__titular.lower()}-comprovativo-nib.pdf'
        
        try:
            # criar a variavel que representa uma folha do pdf
            c = canvas.Canvas(nome_arquivo)
            # definir a localização do texto
            texto = c.beginText(20, 750)
            # definir o tipo de letra
            c.setFont('Helvetica', 22)
            # Processar o texto para entender o \n
            texto.textLines(self.__str__())
            # Escrever o texto
            c.drawText(texto)
            # gravar o pdf
            c.save()

        except:
            print('Erro ao gerar comprovativo.')

        else:
            print(f'{nome_arquivo} gerado com sucesso.')