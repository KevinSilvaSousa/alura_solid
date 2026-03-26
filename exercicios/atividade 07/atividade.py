from abc import ABC, abstractmethod

class GeradorArquivo(ABC):
    @abstractmethod
    def gerar(self, conteudo: str):
        pass


class GeradorPDF(GeradorArquivo):
    def gerar(self, conteudo: str):
        print(f"Gerando PDF com o conteúdo: {conteudo}")


class GeradorExcel(GeradorArquivo):
    def gerar(self, conteudo: str):
        print(f"Gerando Excel com o conteúdo: {conteudo}")


class GeradorHTML(GeradorArquivo):
    def gerar(self, conteudo: str):
        print(f"Gerando HTML com o conteúdo: {conteudo}")


class ConversorArquivo:
    def __init__(self, gerador: GeradorArquivo):
        self.gerador = gerador

    def converter(self, conteudo: str):
        self.gerador.gerar(conteudo)

conteudo = "Relatorio"
conversor_pdf = ConversorArquivo(GeradorPDF())
conversor_pdf.converter(conteudo)

conversor_excel = ConversorArquivo(GeradorExcel())
conversor_excel.converter(conteudo)

conversor_html= ConversorArquivo(GeradorHTML())
conversor_html.converter(conteudo)