from rich import print 
from rich.traceback import install
install()
from time import sleep

class Livro():
    def __init__(self, titulo, paginas):
        self.titulo=titulo
        self.paginas=paginas
        self.pagina_Atual=1

    def avancar_paginas(self,quantidade=0):
        avancadas=0
        if quantidade==0:
            print(f'Bem vindo ao [yellow]{self.titulo}[/] você agora esta na pagina {self.pagina_Atual}') 
            return
        for _ in range(quantidade):
            if self.pagina_Atual >= self.paginas:
                print(f'[red]Você chegou a o final do livro[/] [yellow]{self.titulo}[/]')
                break
            print(f'Pag{self.pagina_Atual} >', end=' ')
            self.pagina_Atual+=1
            avancadas+=1
            sleep(0.75)
        print(f'Você avançou {avancadas} paginas e agora esta na pagina [green]{self.pagina_Atual}[/]') 
        
    def voltar_paginas(self, quantidade_voltar=0):
        voltadas=0
        if quantidade_voltar==0:
            print(f'Você voltou {quantidade_voltar} paginas')
            return
        for _ in range(quantidade_voltar,0,-1):
            if self.pagina_Atual == 1:
                print(f'[red]Você chegou a o final do livro[/] [yellow]{self.titulo}[/]')
                break
            self.pagina_Atual -=1
            print(f'Pag{self.pagina_Atual-1} >', end=' ')
            voltadas+=1
            sleep(0.75)        
        print(f'Você retornou {voltadas} paginas e agora esta na pagina {self.pagina_Atual}')
        
l1=Livro('Minha jornada de Poo', 20)
l1.avancar_paginas()
l1.avancar_paginas(6)
l1.voltar_paginas(3)
l1.avancar_paginas(2)
l1.voltar_paginas(8)
