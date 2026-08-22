from abc import ABC,abstractmethod

class Funcionario:
    def __init__(self,nome,salario):
        self.nome=nome
        self.__salario=salario
        
    @abstractmethod
    def calcular_bonus(self):
        pass
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self,valor):
        if valor < 0:
            print('Adicione um valor valido')
        else:
            self.__salario=valor
            
class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        
    def calcular_bonus(self):
        bonus_gerente=self.salario*0.15
        return bonus_gerente
    
    def __str__(self):
        return f'{self.nome} ganha {self.salario} e por ser {self.__class__.__name__} tem um bonus de {self.calcular_bonus()}'
                
class Design(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        
    def calcular_bonus(self):
        bonus_design=self.salario*0.08
        return bonus_design
    
    def __str__(self):
        return f'{self.nome} ganha {self.salario} e por ser {self.__class__.__name__} tem um bonus de {self.calcular_bonus()}'

class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        
    def calcular_bonus(self):
        bonus_Desenvolvedor=self.salario*0.10   
        return bonus_Desenvolvedor
    
    def __str__(self):
     return f'{self.nome} ganha {self.salario} e por ser {self.__class__.__name__} tem um bonus de {self.calcular_bonus()}'
            
print('Calculo de bonus salarial')
print('-'*30)
print('[1]- Design\n'
      '[2]- Desenvolvedor\n'
      '[3]- Gerente')
opcao=int(input('Digite o numero referido ao seu cargo: '))
if opcao==1:
    nome_design=input('Digite seu nome: ')
    salario_design=float(input('Sua renda salarial: '))
    design=Design(nome_design,salario_design)
    print(design)
elif opcao==2:
    nome_desenvolvedor=input('Digite seu nome: ')
    salario_desenvolvedor=float(input('Sua renda salarial: '))
    desenvolvedor=Desenvolvedor(nome_desenvolvedor,salario_desenvolvedor)
    print(desenvolvedor)
elif opcao==3:
    nome_gerente=input('Digite seu nome: ')
    salario_gerente=float(input('Sua renda salarial: '))
    gerente=Gerente(nome_gerente,salario_gerente)
    print(gerente)
else:
    print('Não existe esta opção')
