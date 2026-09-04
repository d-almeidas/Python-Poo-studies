from rich import print
class Produto:
    def __init__(self, nome:str, preco:float):
        self.__nome=nome
        self.__preco=preco

    @property
    def preco(self):
        return self.__preco

    def __str__(self):
        return f'Produto: {self.__nome} - Preço: R${self.__preco:.2f}'

    def __add__(self, other):
        return Carrinho([self,other])
    

class Carrinho:
    def __init__(self, produtos=None):
        self.__produtos = produtos if produtos is not None else []

    @property
    def produtos(self):
        return self.__produtos

    def __add__(self, produto):
        self.__produtos.append(produto)
        return self
    
    def __str__(self):
        linhas = '\n'.join(str(p) for p in self.__produtos)
        total = sum(p.preco for p in self.__produtos)
        return f'[red]Produtos no carrinho[/red]:\n{linhas}\nPreço total: R${total:.2f}'
    

print("[green]Sistema de carrinho de compras[/green]")
print("1 - Adicionar produto")
print("2 - Visualizar carrinho")
print("3 - Sair")

carrinho_de_Compras=Carrinho()
while True:
    opcao= int(input("Escolha uma opção: "))
    if opcao==1:
        nome=input("Digite o nome do produto: ")
        preco=float(input("Digite o preço do produto: "))
        produto=Produto(nome,preco)
        carrinho_de_Compras= carrinho_de_Compras + produto
        print(f"[green]{produto} adicionado ao carrinho![/green]")


    elif opcao==2:
        print(carrinho_de_Compras)
        if not carrinho_de_Compras.produtos:
            print("[yellow]O carrinho está vazio![/yellow]")

    elif opcao==3:
        print("[blue]Saindo do sistema...[/blue]")
        break
    else:
        print("[red]Opção inválida![/red]")