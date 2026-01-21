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



*******

    def obter_comprovativo(self):
    # dar o nome ao ficheiro
    nome_arquivo = f'{self.__titular}-comprovativo-nib.pdf

    # criar a variável que representa uma folha do pdf
    c = canvas.Canvas (nome_arquivo)

    # definir o tipo de letra
    c.setFont('Helvetica', 22)

    # escrever as coisas
    c.drawString(100,700,self.__str__())

    # gravar o pdf
    c.save()

    print(f'{nome_arquivo} gerado com sucesso.')