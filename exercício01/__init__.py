
def gerar_comprovativo_nib():
    nome_arquivo = "comprovativo_nib.pdf"

    doc = SimpleDocTemplate(nome_arquivo)
    estilos = getSampleStyleSheet()
    elementos = []

    titulo = Paragraph("<b>Comprovativo de NIB</b>", estilos["Title"])
    elementos.append(titulo)
    elementos.append(Spacer(1, 12))

    data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

    texto = f"""
    Nome do Titular: {conta['nome']}<br/>
    NIB: {conta['nib']}<br/>
    Data: {data}<br/>
    """

    conteudo = Paragraph(texto, estilos["BodyText"])
    elementos.append(conteudo)

    doc.build(elementos)

    print("✅ PDF gerado com sucesso: comprovativo_nib.pdf")