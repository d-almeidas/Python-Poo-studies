from rich import print
from rich import inspect
import hashlib

class Credencial():
    def __init__(self, senha):
        self.__hash=hashlib.sha256(senha.encode('utf-8')).hexdigest()

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def hash(self, senha):
        hash_Senha=hashlib.sha256(senha.encode('utf-8')).hexdigest()
        self.__hash=hash_Senha

    def validar_senha(self, senha):
        if hashlib.sha256(senha.encode('utf-8')).hexdigest() == self.__hash:
            print('[green]Senha correta![/green]')
            return True
        else:
            print('[red]Senha incorreta![/red]')
            return False

print('[blue]Bem vindo ao sistema de autenticação![/blue]')
senha=input('Digite a senha para criar a credencial: ')
c=Credencial(senha)
quer=input('Sua senha agora esta protegida deseja ver?[s/n]: ')
if quer.lower() == 's':
    print(f'[yellow]Hash da senha: {c.senha}[/yellow]')
else:
    print('[yellow]Saindo do sistema...[/yellow]')
