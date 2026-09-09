from rich import print
from abc import ABC,abstractmethod
from rich.table import Table
from rich.console import Console
console=Console()

class CalcularFrete(ABC):
    def __init__(self,distancia):                   #Desconsiderando peso de itens
        self.distancia=distancia
        self.fator=0
        
    @abstractmethod
    def calc_frete(self):
        pass
    
class Moto(CalcularFrete):
    def __init__(self,distancia):
        super().__init__(distancia)
        self.fator=0.50

    def calc_frete(self):
        total=self.distancia*self.fator
        print(f'O frete de {type(self).__name__} em {self.distancia} Km = {total}R$')
    
class Caminhão(CalcularFrete):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator=1.20
        
    def calc_frete(self):
        if self.distancia<50:
            print('Infelizmente não e possivel fazer a entrega a essa distancia')
        else:
            total=self.distancia *self.fator
            print(f'O frete de {type(self).__name__} em {self.distancia} Km = {total}R$')
            
class Drone(CalcularFrete):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator=9.50
        
    def calc_frete(self):
        if self.distancia >10 or self.distancia<0:
            print('Infelizmente não e possivel fazer a entrega a essa distancia ')
        else:
            total= self.distancia * self.fator
            print(f'O frete de {type(self).__name__} em {self.distancia} Km = {total}R$')
            


print('[1] -> [dark_red]MOTO[/]\n'
                    '[2] -> [dark_green]CAMINHÇAO[/]\n'
                    '[3] -> [blue]DRONE[/]\n'
                    '[4] -> TODOS\n') 
while True: 
    escolha=int(input('Qual a opcao desejada: '))
    if  escolha not in (1,2,3,4):
        print("[red]DIGITE APENAS AS OPCOES DADAS")
        continue
    else:
        
        escolha_2=int(input('Digite a distançia total: '))
        if escolha==1:
            m1=Moto(escolha_2)
            m1.calc_frete()
            
        if escolha==2:
            c1=Caminhão(escolha_2)
            c1.calc_frete()

        if escolha==3:
            d1=Drone(escolha_2)
            d1.calc_frete()

        if escolha==4:
            veiculos= [Moto(escolha_2),Caminhão(escolha_2),Drone(escolha_2)]
                
            table=Table(title='Tabela de fretes')
            table.add_column('Veiculo')
            table.add_column('Distancia(KM)')
            table.add_column('Frete')
                
            for v in veiculos:
                if isinstance(v,Caminhão) and v.distancia < 50:
                    table.add_row(type(v).__name__, str(v.distancia).center(13),'[bright_red]não é possível entregar nessa distância (mínimo 50km)[/]')
                    continue
                if isinstance(v,Drone) and v.distancia > 10:
                    table.add_row(type(v).__name__, str(v.distancia).center(13),'[bright_red]não é possível entregar nessa distância (máximo 10km[/]')
                    continue
                
                total=v.distancia * v.fator
                table.add_row(type(v).__name__, str(v.distancia).center(13), f"R$ {total:.2f}")
            
            console.print(table)