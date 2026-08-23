from abc import ABC,abstractmethod

class Pagamento(ABC):
    def __init__(self,valor):
        self._valor=valor
        
    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self,quantidade):
        if quantidade < 0:
            print("Coloque um valor maior que 0")
        self._valor=quantidade
        
    @property
    def valor_formatado(self):
        return f"{self._valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    
    @abstractmethod
    def pagar(self):
        pass
    
class Boleto(Pagamento):
    def __init__(self, valor):
        super().__init__(valor)
        
    def pagar(self):
        print(
        f"Pagamento de R$ {self.valor_formatado} realizado via"
        f" {self.__class__.__name__}"
    )
class Pix(Pagamento):
    def __init__(self, valor):
        super().__init__(valor)
        
    def pagar(self):
         print(
        f"Pagamento de R$ {self.valor_formatado} realizado via"
        f" {self.__class__.__name__}"
    )
    
class Credito(Pagamento):
    def __init__(self, valor):
        super().__init__(valor)
        
    def pagar(self):
         print(
        f"Pagamento de R$ {self.valor_formatado} realizado via"
        f" {self.__class__.__name__}"
    )
    
def tentar_pagar(objeto):
    try:
        objeto.pagar()
    except:
        print('Näo foi possivel efetuar o pagamento')
        
print('-'*30)
print('Nota'.center(30))
print('-'*30)
print()
try:
    valor = float(input('Digite o valor da compra: '))
except ValueError:
    print('Valor inválido!')
    exit()
print('[1] - Boleto\n'
      '[2] - Pix\n'
      '[3] - Credito')
opcao_De_pagamento=int(input('Qual opçäo de pagamento: '))
if opcao_De_pagamento==1:
    b=Boleto(valor)
    tentar_pagar(b)
elif opcao_De_pagamento==2:
    p=Pix(valor)
    tentar_pagar(p)
elif opcao_De_pagamento==3:
    c=Credito(valor)
    tentar_pagar(c)
else:
    print('Näo existe esta opçäo')