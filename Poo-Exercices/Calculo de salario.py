from rich import print
from rich.panel import Panel
from abc import ABC,abstractmethod
import math

class Funcionario(ABC):
    def __init__(self,nome,sal_bruto):
        
        self.salario_bruto=sal_bruto
        self.nome=nome
        self.salario_Min=1612
        self.inss=7.5 # Desconto
        
        
    @abstractmethod
    def calc_salario(self):
        pass
    
    def analisar_salario(self):
        pass
    
    def quantos_salarios_min(self):
        pass
    
class Horista(Funcionario):
    def __init__(self,nome,valor_hora,horas_trabalhadas):
        super().__init__(nome,sal_bruto=0)
        
        self.horas_trabalhadas=horas_trabalhadas
        self.valor_hora=valor_hora
        
    def calc_salario(self):
        return ((self.horas_trabalhadas*self.valor_hora)*(1-self.inss/100))
    
    def quantos_salarios_min(self):
        return (self.calc_salario()/self.salario_Min)
    
    def analisar_salario(self):
        mensagem=(f'[green]{self.nome}[/] [red]({type(self).__name__}) [/]o seu salario e de: R${self.calc_salario():.2f}\n')
        mensagem+=(f'E corresponde a : {self.quantos_salarios_min():.1f} salarios min')
        
        painel=Panel(mensagem,title='Analise de Salarios',width=38)
        print(painel)
class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome, sal_bruto)
    
    def calc_salario(self):
        return self.salario_bruto*(1-self.inss/100)
    
    def analisar_salario(self):
        mensagem =(f'[green]{self.nome}[/] [red]({type(self).__name__})[/] o seu salario e de: R${self.calc_salario():.2f}\n')
        mensagem+=(f'E corresponde a : {self.quantos_salarios_min():.1f} salarios min')
        
        painel=Panel(mensagem,title='Analise de Salarios',width=38)
        print(painel)
        
    def quantos_salarios_min(self):
            return (self.calc_salario()/self.salario_Min)

print('[1] -> Horista(recebe por horas de trabalho)\n'
                 '[2] -> Mensalista(recebe salario mensal)\n')
while True:
    opcoes=int(input('Em qual dessas opçoes vc se encaixa: '))

    if opcoes not in (1,2):
        print('Opção inválida')
        continue
    
    if opcoes == 1:
        while True:
            pergunta_nome=input('Digite seu nome ')
            if pergunta_nome.replace(' ','').isalpha():
                break
            else:   
                print('ERROR, digite apenas letras')
                
        prgunta_valor_hora=float(input('Quanto vc ganha por hora de trabalho: '))
        pergunta_horas_trabalho=float(input('Quantas horas vc trabalha ao todo: '))
        h1=Horista(pergunta_nome,prgunta_valor_hora,pergunta_horas_trabalho)
        h1.analisar_salario()
        break
    
    if opcoes==2:
            while True:
                pergunta_nome_2=input('Digite seu nome: ')
                if pergunta_nome_2.replace(' ','').isalpha():
                    break
                else:
                    print('ERROR, digite apenas letras')
            pergunta_valor_bruto=float(input('Digite o valor do seu salario: '))
            m1=Mensalista(pergunta_nome_2,pergunta_valor_bruto)
            m1.analisar_salario()
            break
     
