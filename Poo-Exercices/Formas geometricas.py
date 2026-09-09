from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self,quantidade_lados):
        self.quantidade_lados=quantidade_lados
        
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass
        
class Quadrado(Poligono):
    def __init__(self,msg):
        if msg <= 0:
            raise ValueError("O lado do quadrado deve ser maior que zero.")
        super().__init__(4)
        self.comprimento_lado=msg
            
    def area(self):
        return self.comprimento_lado**2
            
    def perimetro(self):
        return self.comprimento_lado*4
            
class Circulo(Poligono):
    def __init__(self, msg_raio):
        if msg_raio <= 0:
            raise ValueError("O raio deve ser maior que zero.")
        super().__init__(0)
        self.raio=msg_raio
        
    def perimetro(self):
        return 2*3.14*self.raio
    
    def area(self):
        return (self.raio*self.raio)*3.14

Digitar=int(input('[1] - QUADRADO \n'
              '[2] - CIRCULO \n'
              'Qual deseja calcular: '))

if Digitar==1:
    try:
        comprimento_lado=int(input('Qual o comprimnto do lado do quadrado: '))
        mensagem=Quadrado(comprimento_lado)
    except ValueError as erro:
        print(F'ERROR: {erro}')
    else:
        print(F'PERIMETRO: {mensagem.perimetro():.1f}')
        print(f'Area: {mensagem.area():.1f}')
    
if Digitar==2:
    try:
        escolha_Raio=float(input('Digite o raio do circulo: '))
        mensagem_raio=Circulo(escolha_Raio)
    except ValueError as erro:
            print(F'ERROR: {erro}')
    else:    
        print(F'PERIMETRO: {mensagem_raio.perimetro():.1f}')
        print(f'Area: {mensagem_raio.area():.1f}')