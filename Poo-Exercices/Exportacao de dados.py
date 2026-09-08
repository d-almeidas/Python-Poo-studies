import xml.etree.ElementTree as ET
import xml.dom.minidom
import json
from rich import print

class Aluno:
    def __init__(self, nome, idade, curso):
        self._nome = nome
        self._idade = idade
        self._curso = curso

class Usuario:
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email

def para_json(lista_objetos):
    dados = [
        {chave.lstrip("_"): valor for chave, valor in obj.__dict__.items()}
        for obj in lista_objetos
    ]
    return json.dumps(dados, indent=2)

def para_xml(lista_objetos, nome_grupo="itens"):
    raiz = ET.Element(nome_grupo)
    for obj in lista_objetos:
        nome_tag = obj.__class__.__name__.lower()
        item = ET.SubElement(raiz, nome_tag)
        for chave, valor in obj.__dict__.items():
            campo = ET.SubElement(item, chave.lstrip("_"))
            campo.text = str(valor)
    xml_str = ET.tostring(raiz, encoding="unicode")
    return xml.dom.minidom.parseString(xml_str).toprettyxml(indent="  ")

def coletar_alunos():
    lista_alunos = []
    while True:
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        curso = input("Digite o curso do aluno: ")
        lista_alunos.append(Aluno(nome, idade, curso))

        adicionar_mais = input("Deseja adicionar outro aluno? (s/n): ")
        while adicionar_mais.lower() not in ['s', 'n']:
            print("[red]Opção inválida! Digite 's' para sim ou 'n' para não.[/red]")
            adicionar_mais = input("Deseja adicionar outro aluno? (s/n): ")
        if adicionar_mais.lower() == 'n':
            break
    return lista_alunos

def coletar_usuarios():
    lista_usuarios = []
    while True:
        nome = input("Digite o nome do usuário: ")
        email = input("Digite o e-mail do usuário: ")
        lista_usuarios.append(Usuario(nome, email))

        adicionar_mais = input("Deseja adicionar outro usuário? (s/n): ")
        while adicionar_mais.lower() not in ['s', 'n']:
            print("[red]Opção inválida! Digite 's' para sim ou 'n' para não.[/red]")
            adicionar_mais = input("Deseja adicionar outro usuário? (s/n): ")
        if adicionar_mais.lower() == 'n':
            break
    return lista_usuarios
    
print("[green]Exportação de dados[/green]")
print("1 - Exportar lista de alunos para JSON")
print("2 - Exportar lista de alunos para XML")
print("3 - Exportar lista de usuários para JSON")
print("4 - Exportar lista de usuários para XML")
opcao = int(input("Escolha uma opção: "))
if opcao == 1:
    print(para_json(coletar_alunos()))
elif opcao == 2:
    print(para_xml(coletar_alunos()))
elif opcao == 3:
    print(para_json(coletar_usuarios()))
elif opcao == 4:
    print(para_xml(coletar_usuarios()))
    