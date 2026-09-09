from rich import print
from rich.panel import Panel

class Gamer():
    def __init__(self, nome, nick):
        self.nome=nome
        self.nick=nick
        self.biblioteca_de_jogos=[]

    def add_favoritos(self, msg):
        self.biblioteca_de_jogos.append(msg)
        
    def ficha(self):
        conteudo=f'Nome real: [blue]{self.nome}[/]\n'
        conteudo+=f'.'*20
        conteudo+= '\n'
        conteudo+= f'Jogos favoritos: \n'
        for jogo in self.biblioteca_de_jogos:
            conteudo += f'[green]•{jogo}[/]\n'
            
        paine=Panel(conteudo,title=self.nick, width=30)
        print(paine)
     
    def perguntas(self):
         while True:
            jogos=str(input('Digite seu jogo favorito: ')).upper()
            self.add_favoritos(jogos)
            q=str(input('Quer continuar [S/N]: ')).upper()
            while q not in 'S' and q not in 'N':
                q=str(input('ERROR, digite um valor valido: Quer continuar [S/N]: ')).upper()
            if q=='N':
                self.ficha()
                break


            
nome_real=str(input('Nome real: '))
nome_game=str(input('Nome no jogo: '))
j1=Gamer(nome=nome_real, nick=nome_game)
j1.perguntas()
  

