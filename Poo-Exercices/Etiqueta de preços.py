from rich import print
from rich.panel import Panel
from rich.align import Align

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        conteudo= f"{self.nome.center(30, ' ')}"
        conteudo += f"{'-'*30}"
        precof = f"R${self.preco:,.2f}"
        conteudo += f"{precof.center(30,'.')}"
        etiqueta= Panel(conteudo, title='Produto', width=34)
        print(etiqueta)

p1 = Produto('Bola',79.99)
p1.etiqueta()