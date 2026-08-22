from abc import ABC,abstractmethod

class Arquivo(ABC):
    def __init__(self,nome,tamanho):
        self.nome=nome
        self.tamanho=tamanho
    
    @abstractmethod
    def abrir(self):
        pass
    
class PDF(Arquivo):
    def __init__(self, nome:str, tamanho:float):
        super().__init__(nome,  tamanho)
        
    def nome_completo(self):
        nome_arquivo_Completo=f'{self.nome}.{__class__.__name__}'
        return nome_arquivo_Completo
    
    def peso_arquivo(self):
        tamanho_Mb=self.tamanho/1000000
        return tamanho_Mb
        
    def abrir(self):
        print(f'Arquivo {self.nome_completo()} ({self.peso_arquivo():.2f}MB) aberto no Adobe reader')
    
class DOC(Arquivo):
    def __init__(self, nome:str,  tamanho:float):
        super().__init__(nome,  tamanho)
        
    def nome_completo(self):
        nome_arquivo_Completo=f'{self.nome}.{__class__.__name__}'
        return nome_arquivo_Completo
    
    def peso_arquivo(self):
            tamanho_Mb=self.tamanho/1000000
            return tamanho_Mb
        
    def abrir(self):
        print(f'Arquivo {self.nome_completo()} ({self.peso_arquivo()}MB) aberto no Microsoft world')
    
def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print('Error ao abrir esse arquivo')

print('[1] - PDF\n'
      '[2] - DOC')
escolha=int(input('Escolha o formato do seu arquvivo: '))
if escolha==1:
    nome_pdf=input('Nome: ')
    tamanho_pdf=float(input('Tamanho em bytes: '))
    p=PDF(nome_pdf,tamanho_pdf)
    tentar_abrir(p)

elif escolha==2:
    nome_doc=input('Nome: ')
    tamanho_doc=float(input('Tamanho em bytes: '))
    d=DOC(nome_doc,tamanho_doc)
    tentar_abrir(d)
else:
    print('Escolha inexistente')