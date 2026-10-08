import json
import os
from datetime import datetime

# Arquivo para armazenar os cadastros
ARQUIVO_CADASTROS = "cadastros.json"

def validar_cpf(cpf):
    """Valida o formato do CPF"""
    # Remove caracteres especiais
    cpf = cpf.replace(".", "").replace("-", "").replace(" ", "")
    
    # Verifica se tem 11 dígitos
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
    # Verifica se todos os dígitos são iguais (inválido)
    if cpf == cpf[0] * 11:
        return False
    
    return True

def validar_email(email):
    """Valida o formato do email"""
    return "@" in email and "." in email and email.count("@") == 1

def validar_telefone(telefone):
    """Valida o formato do telefone"""
    # Remove caracteres especiais
    telefone = telefone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    
    # Verifica se tem 10 ou 11 dígitos
    if len(telefone) not in [10, 11] or not telefone.isdigit():
        return False
    
    return True

def validar_nome(nome):
    """Valida o nome"""
    nome = nome.strip()
    # Verifica se tem pelo menos 3 caracteres
    if len(nome) < 3:
        return False
    # Verifica se contém apenas letras e espaços
    if not all(c.isalpha() or c.isspace() for c in nome):
        return False
    
    return True

def carregar_cadastros():
    """Carrega os cadastros do arquivo JSON"""
    if os.path.exists(ARQUIVO_CADASTROS):
        with open(ARQUIVO_CADASTROS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []

def salvar_cadastros(cadastros):
    """Salva os cadastros no arquivo JSON"""
    with open(ARQUIVO_CADASTROS, "w", encoding="utf-8") as arquivo:
        json.dump(cadastros, arquivo, ensure_ascii=False, indent=4)

def novo_cadastro():
    """Cria um novo cadastro"""
    print("\n" + "="*50)
    print("NOVO CADASTRO".center(50))
    print("="*50 + "\n")
    
    # Solicita o nome
    while True:
        nome = input("Digite o NOME: ").strip()
        if validar_nome(nome):
            break
        print("❌ Nome inválido! Use pelo menos 3 letras.")
    
    # Solicita o CPF
    while True:
        cpf = input("Digite o CPF (xxx.xxx.xxx-xx ou 11 dígitos): ").strip()
        if validar_cpf(cpf):
            break
        print("❌ CPF inválido! Use o formato: xxx.xxx.xxx-xx")
    
    # Solicita o email
    while True:
        email = input("Digite o EMAIL: ").strip()
        if validar_email(email):
            break
        print("❌ Email inválido! Use o formato: example@email.com")
    
    # Solicita o telefone
    while True:
        telefone = input("Digite o TELEFONE (com DDD): ").strip()
        if validar_telefone(telefone):
            break
        print("❌ Telefone inválido! Use o formato: (XX) 99999-9999 ou XX 99999-9999")
    
    # Cria o dicionário do cadastro
    cadastro = {
        "id": len(carregar_cadastros()) + 1,
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "telefone": telefone,
        "data_cadastro": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    
    # Adiciona aos cadastros
    cadastros = carregar_cadastros()
    cadastros.append(cadastro)
    salvar_cadastros(cadastros)
    
    print("\n✅ Cadastro realizado com sucesso!")
    return cadastro

def listar_cadastros():
    """Lista todos os cadastros"""
    cadastros = carregar_cadastros()
    
    if not cadastros:
        print("\n❌ Nenhum cadastro encontrado!")
        return
    
    print("\n" + "="*100)
    print("LISTA DE CADASTROS".center(100))
    print("="*100 + "\n")
    
    for cadastro in cadastros:
        print(f"ID: {cadastro['id']}")
        print(f"Nome: {cadastro['nome']}")
        print(f"CPF: {cadastro['cpf']}")
        print(f"Email: {cadastro['email']}")
        print(f"Telefone: {cadastro['telefone']}")
        print(f"Data de Cadastro: {cadastro['data_cadastro']}")
        print("-" * 100)

def buscar_cadastro():
    """Busca um cadastro pelo CPF"""
    cpf = input("Digite o CPF para buscar: ").strip()
    
    cadastros = carregar_cadastros()
    
    for cadastro in cadastros:
        if cadastro['cpf'].replace(".", "").replace("-", "") == cpf.replace(".", "").replace("-", ""):
            print("\n" + "="*50)
            print("CADASTRO ENCONTRADO".center(50))
            print("="*50 + "\n")
            print(f"ID: {cadastro['id']}")
            print(f"Nome: {cadastro['nome']}")
            print(f"CPF: {cadastro['cpf']}")
            print(f"Email: {cadastro['email']}")
            print(f"Telefone: {cadastro['telefone']}")
            print(f"Data de Cadastro: {cadastro['data_cadastro']}\n")
            return
    
    print("\n❌ Cadastro não encontrado!")

def deletar_cadastro():
    """Deleta um cadastro pelo CPF"""
    cpf = input("Digite o CPF do cadastro a deletar: ").strip()
    
    cadastros = carregar_cadastros()
    
    for i, cadastro in enumerate(cadastros):
        if cadastro['cpf'].replace(".", "").replace("-", "") == cpf.replace(".", "").replace("-", ""):
            confirmacao = input(f"\nTem certeza que deseja deletar o cadastro de {cadastro['nome']}? (s/n): ").lower()
            if confirmacao == "s":
                cadastros.pop(i)
                salvar_cadastros(cadastros)
                print("✅ Cadastro deletado com sucesso!")
            return
    
    print("\n❌ Cadastro não encontrado!")

def menu_principal():
    """Exibe o menu principal"""
    while True:
        print("\n" + "="*50)
        print("SISTEMA DE CADASTRO".center(50))
        print("="*50)
        print("\n1. Novo Cadastro")
        print("2. Listar Cadastros")
        print("3. Buscar Cadastro")
        print("4. Deletar Cadastro")
        print("5. Sair")
        print("\n" + "="*50)
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            novo_cadastro()
        elif opcao == "2":
            listar_cadastros()
        elif opcao == "3":
            buscar_cadastro()
        elif opcao == "4":
            deletar_cadastro()
        elif opcao == "5":
            print("\n👋 Até logo!")
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu_principal()
