from rich import print,inspect
from abc import ABC
from datetime import date

data_atual = date.today()
ano_atual = data_atual.year

class Pessoa(ABC):
    def __init__(self,nome,nascimento):
        self._nome=nome
        self._nascimento=nascimento
        self._cursos=['ADM','ADS','ENG','CONT']
    @property
    def nascimento(self):
        return self._nascimento
    
    @nascimento.setter
    def nascimento(self,valor):
        if valor < 1914 or valor > ano_atual:
            print('Data invalida')
        else:
            self._nascimento=valor
        
    @property
    def idade(self):
        return ano_atual-self._nascimento
    
class Aluno(Pessoa):
    def __init__(self, nome, nascimento,curso):
        super().__init__(nome,nascimento)
        self.curso=curso
        
    @property
    def curso(self):
        return self._curso
    
    @curso.setter
    def curso(self, palavra):
        if palavra not in self._cursos:
            print('Curso inexistente')
        else:
            self._curso = palavra
        
    def add_curso(self,curso_novo):
        self._cursos.append(curso_novo)
        return self._cursos
    
    def analisar(self):
        print(f'Nome: {self._nome}\n'
              f'Idade: {self.idade}\n'
              f'Curso atual: {self._curso}')
        
nome_pessoa=input('Digite seu nome: ')
try:
    nascimento_pessoa=int(input('Digite sua data de nascimento: '))
    if nascimento_pessoa < 1914 or nascimento_pessoa > ano_atual:
        print('Data errada')
        exit()
except ValueError:
    print('Digite apenas numeros')
print(f'Nossos cursos disponiveis = ADM, ADS, ENG ,CONT')

curso_Pessoa=input('Digite as siglas do seu curso desejado: ').upper()
p1=Aluno(nome_pessoa,nascimento_pessoa,curso_Pessoa)
deseja=input('Deseja alterar seu curso?[S/N]  ').lower()
if deseja=='n':
    p1.analisar()
else:
    qual=input('Digite as siglas do curso que deseja: ').upper()
    p1.add_curso(qual)
    p1.curso=qual
    p1.analisar()