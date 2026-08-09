from rich import inspect
from rich import print

class Diario():
    def __init__(self,senha):
        self.__segredos=[]
        self.__senha=senha
        
    def escrevr(self, msg):
        self.__segredos.append(msg)
        
    def ler(self, senha=None):
        if senha==self.__senha:
            print('[green]Segredos do diario:[/green]')
            for segredo in self.__segredos:
                print(f'[yellow]{segredo}[/yellow]')
        else:
            print('[red]Senha incorreta! pare de tentar ler meu diario[/red]')
        
print('[green]Diario criado com sucesso![/green]')
diario_Senha=input('Digite a senha do diario: ')
diario=Diario(diario_Senha)
while True:
    segredinhos=input('Digite um segredo para escrever no diario: ')
    diario.escrevr(segredinhos)
    quer_continuar=input('Quer continuar escrevendo no diario? [s/n]: ')
    if quer_continuar.lower()=='n':

        acessar_diario=(input('Digite a senha para ler o diario: '))
        if acessar_diario==diario_Senha:
            diario.ler(acessar_diario)
        else:
            print('[red]Senha incorreta! pare de tentar ler meu diario[/red]')
        break
    
        
    