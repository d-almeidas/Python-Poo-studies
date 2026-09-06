from abc import ABC, abstractmethod
from rich import print

class Validador(ABC):
    @abstractmethod
    def validar(self, valor):
        pass

class Usuario(Validador):
    def __init__(self, nome: str):
        self.__nome = nome

    def validar(self, valor):
        if len(valor) < 5:
            raise ValueError("O valor deve ter pelo menos 5 caracteres.")
        elif any(char.isupper() for char in valor):
            raise ValueError("O valor não deve conter caracteres maiúsculos.")
        else:
            return self.__nome == valor 
     
class Senha(Validador):
    def __init__(self, senha: str):
        self.__senha = senha

    def validar(self, valor):
        if len(valor) < 8:
            raise ValueError("A senha deve ter pelo menos 8 caracteres.")
        elif not any(char.isupper() for char in valor):
            raise ValueError("A senha deve conter pelo menos uma letra maiúscula.")
        else:
            return self.__senha == valor

class Email(Validador):
    def __init__(self, email: str):
        self.__email = email

    def validar(self, valor):
        if "@" not in valor or "." not in valor or '@' == valor[0] or '.' == valor[-1] or valor .count('@') != 1 or valor.count('.') < 1:
            raise ValueError("O valor deve ser um e-mail válido.")
        else:
            return self.__email == valor


print("[green]Validação de dados[/green]")
print("1 - Validar usuário")
print("2 - Validar senha")
print("3 - Validar e-mail")
while True:
    opcao= int(input("Escolha uma opção: "))
    if opcao==1:
        nome=input("Digite o nome do usuário: ")
        usuario=Usuario(nome)
        try:
            if usuario.validar(nome):
                print("[green]Usuário válido![/green]")
            else:
                print("[red]Usuário inválido![/red]")
        except ValueError as error:
            print(f"[red]Erro: {error}[/red]")
            

    elif opcao==2:
        senha=input("Digite a senha: ")
        senha_obj=Senha(senha)
        try:
            if senha_obj.validar(senha):
                print("[green]Senha válida![/green]")
            else:
                print("[red]Senha inválida![/red]")
        except ValueError as error:
            print(f"[red]Erro: {error}[/red]")
            

    elif opcao==3:
        email=input("Digite o e-mail: ")
        email_obj=Email(email)
        try:
            if email_obj.validar(email):
                print("[green]E-mail válido![/green]")
            else:
                print("[red]E-mail inválido![/red]")
        except ValueError as error:
            print(f"[red]Erro: {error}[/red]")
            
    else:
        print("[red]Opção inválida![/red]")

    quercontinuar = input("Deseja continuar? (s/n): ")
    while quercontinuar.lower() not in ['s', 'n']:
        print("[red]Opção inválida! Digite 's' para sim ou 'n' para não.[/red]")
        quercontinuar = input("Deseja continuar? (s/n): ")
    if quercontinuar.lower() == 'n':
        print("[blue]Saindo do sistema...[/blue]")
        break 