class ContaBancaria:
    """Cria conta bancaraia e cria saques e depositos, além de mostrar o saldo atual.
    """
    def __init__(self, id, nome, saldo=0.0):
        self.id = id
        self.titular = nome
        self.saldo = saldo

    def __str__(self):
        return f'A Conta: \033[36m{self.id}\033[0m de: \033[32m{self.titular}\033[0m possui: R${self.saldo:.2f} de saldo'
     
    def deposito(self, msg):
        while True:
            try:
                valor = float(input(msg))
                
                if valor <= 0:
                    print("Valor do depósito deve ser maior que zero. Por favor, tente novamente.")
                    continue
                
                self.saldo += valor
                return f'Depósito de \033[32m${valor:.2f}\033[0m na conta \033[36m{self.id}\033[0m realizado com sucesso. Novo saldo: \033[32mR${self.saldo:,.2f}\033[0m'
            
            except ValueError:
                print("Valor inválido. Por favor, informe um número.")
                
    def saque(self, msg):
        while True:
            try:
                valor = float(input(msg))
                if valor <= 0:
                    print("Valor do saque deve ser maior que zero. Por favor, tente novamente.")
                    continue
                if valor > self.saldo:
                    print(f"Saldo insuficiente na conta \033[36m{self.id}\033[0m. Saldo atual: \033[32mR${self.saldo:,.2f}\033[0m")
                    continue
                
                if self.saldo >= valor:
                    self.saldo -= valor
                    return f'Saque de \033[32m${valor:.2f}\033[0m na conta \033[36m{self.id}\033[0m realizado com sucesso. Novo saldo: \033[32mR${self.saldo:,.2f}\033[0m'
                
            except ValueError:
                print("Valor inválido. Por favor, informe um número.")


print('Bem-vindo ao sistema bancário!'.center(40))
print('=' * 40)
print('Primeiro passo, nos informe seu id da conta: ')

while True:
    try:
        id_conta = int(input('Informe seu id da conta: '))
        break
    except ValueError:
        print("\033[31mID inválido. Por favor, informe um número inteiro.\033[0m")
        
print('=' * 45)
print(f'Id da conta \033[36m{id_conta}\033[0m registrado com sucesso.')
print('=' * 45)
    
print('Agora, nos informe seu nome: ')
nome_titular = input()

while nome_titular == '':
    print('Nome do titular não pode ser vazio. Por favor, tente novamente.')
    nome_titular = input('Informe seu nome: ')
else:
    print('=' * 45)
    print(f'Nome do titular \033[32m{nome_titular}\033[0m registrado com sucesso.')
    print('=' * 45)
    
c1 = ContaBancaria(id=id_conta, nome=nome_titular)
print(f'Conta criada com sucesso! \n{c1}')
depositar=('Qual valor a depositar? R$')
print(c1.deposito(depositar))
sacar=('Qual valor a sacar? R$')
print(c1.saque(sacar))

