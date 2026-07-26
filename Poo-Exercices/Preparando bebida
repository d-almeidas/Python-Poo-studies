from rich import print
from rich.panel import Panel
from abc import ABC,abstractmethod
from time import sleep

class Cafeteira(ABC):
    def Preparar(self):
        self.Ferver_agua()
        self.Misturar()
        self.Servir()
        
    def Ferver_agua(self):
        print('---[red]INICIANDO O PREPARO[/red]---')
        print('1. Fervendo a agua a 100 graus celsius')
        sleep(1)
        
    @abstractmethod
    def Misturar(self):
        pass
    
    @abstractmethod
    def Servir(self):
        pass
    
class Cafe(Cafeteira):
    def Misturar(self):
        print('2. Misturando o pó de café')
        sleep(1)
        
    def Servir(self):
        print('3. Servindo em uma xicara pequena',end=' ')
        sleep(1)
        
        print('.',end=' ')
        sleep(1) 
        print('.',end=' ')
        sleep(1) 
        print('.')
        print('---[blue]BEBIDA PRONTA[/blue]---')
        
class Cha(Cafeteira):
    def Misturar(self):
        print('2. Mergulhando o sache de ervas na agua')
        sleep(1)
        
    def Servir(self):
        print('3. Servindo na caneca de porcelana com limão',end=' ')
        sleep(1)
        
        print('.',end=' ')
        sleep(1) 
        print('.',end=' ')
        sleep(1) 
        print('.')
        print('---[blue]BEBIDA PRONTA[/blue]---')

class Leite(Cafeteira):
    def Misturar(self):
        print('2. Passando o vapor pressurizado pelo bico de leite')
        sleep(1)
        
    def Servir(self):
        print('3. Servindo com café em uma caneca grande',end='')
        sleep(1)
        
        print('.',end=' ')
        sleep(1) 
        print('.',end=' ')
        sleep(1) 
        print('.')
        print('---[blue]BEBIDA PRONTA[blue]---')
    


def Menu():
    mensagem='[1] -> Café ............. 9.50\n'
    mensagem+='[2]->  Chá .............. 12.00\n'
    mensagem+='[3] -> Leite ............ 11.00'
    Cardapio_De_pedidos=Panel(mensagem,title='LaCafeteria',width=35)
    print(Cardapio_De_pedidos)
        

Menu()
while True:
    try:
        escolha=int(input('Digite o numero referente ao pedido: '))
    except ValueError:
        print('[red]Digite apenas numeros[/red]')
        continue
    
    if escolha not in (1,2,3):
        print('[red]Escolha so o numro que esta no cardapio[/red]')
        continue
    break
if escolha==1:
    c1=Cafe()
    c1.Preparar()
    
if escolha==2:
    ch=Cha()
    ch.Preparar()
    
if escolha==3:
    l=Leite()
    l.Preparar()

