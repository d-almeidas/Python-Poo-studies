from rich import print
from rich.panel import Panel

class Mensagem: 
    def __init__(self, mensagem:str, tipo:str=None):
        self.__mensagem=mensagem
        self.__tipo=tipo

    def mostrar(self):
        conteudo=self.__mensagem
        self.__tipo="Aviso"
        painel=Panel(conteudo,title=self.__tipo,width=35)
        print(painel)

class Alerta(Mensagem):
    def __init__(self, mensagem:str):
        super().__init__(mensagem, tipo="Alerta")

    def mostrar(self):
        conteudo=self._Mensagem__mensagem
        self._Mensagem__tipo="Alerta"
        painel=Panel(conteudo,title=self._Mensagem__tipo,width=35,style="bold yellow")
        print(painel)

class Erro(Mensagem):
    def __init__(self , mensagem:str):
        super().__init__(mensagem, tipo="Erro")
    
    def mostrar(self):
        conteudo=self._Mensagem__mensagem
        self._Mensagem__tipo="Erro"
        painel=Panel(conteudo,title=self._Mensagem__tipo,width=35,style="bold red")
        print(painel)

print("[green]Sistema de mensagens[/green]")
print("1 - Mensagem")
print("2 - Alerta")
print("3 - Erro")

while True:
    opcao=int(input("Escolha uma opção: "))
    if opcao==1:
        msg=input("Digite a mensagem: ")
        mensagem=Mensagem(msg)
        mensagem.mostrar()
    elif opcao==2:
        msg=input("Digite a mensagem: ")
        alerta=Alerta(msg)
        alerta.mostrar()
    elif opcao==3:
        msg=input("Digite a mensagem: ")
        erro=Erro(msg)
        erro.mostrar()
    else:
        print("[red]Opção inválida![/red]")
        