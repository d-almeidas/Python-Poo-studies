from rich import print 
from rich.panel import Panel

class Termostato:
    def __init__(self, temperatura=24):
        self.__temperatura = temperatura
        
    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, valor):
        if valor < 16:
            print(Panel("[bold red]Temperatura mínima é 16°C[/bold red]", title="Erro", style="red", width=20))
            self.__temperatura = 16
        elif valor > 30:
            print(Panel("[bold red]Temperatura máxima é 30°C[/bold red]", title="Erro", style="red", width=20))
            self.__temperatura = 30
        elif valor % 1 == 0.5:
            self.__temperatura = valor
        elif valor % 1 != 0.5:
            self.__temperatura= round(valor * 2) / 2  # Arredonda para o número mais próximo que termina com .0 ou .5
            
    def __str__(self):
        return f'Temperatura atual: {self.__temperatura}°C'
    
while True:
    try:
        termostato = Termostato()
        qual_temperatura = float(input("Informe a temperatura desejada (entre 16°C e 30°C): "))
        termostato.temperatura = qual_temperatura
        print(termostato)
        quer = input("Deseja alterar a temperatura novamente? (s/n): ").strip().lower()
        if quer != 's':
            break
    except ValueError:
        print(Panel("[bold red]Valor inválido. Por favor, informe um número.[/bold red]", title="Erro", style="red", width=20))