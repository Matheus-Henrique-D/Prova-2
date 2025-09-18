# Arquivo: gerador_dados.py

from faker import Faker
import random 
import csv 

# Configurações
fake = Faker('pt_BR')
cursos_possiveis = ["IA", "ESG"]
quantidade_de_alunos = 150
nome_do_arquivo = 'vestibulandos.csv'

# Abre o arquivo para escrita
with open(nome_do_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    
    # Escreve o cabeçalho
    escritor_csv.writerow(['nome', 'cpf', 'curso', 'boleto'])
    
    # Gera e escreve os dados de cada aluno
    print(f"Gerando {quantidade_de_alunos} registros de alunos...")
    for _ in range(quantidade_de_alunos):
        nome = fake.name()
        cpf = fake.cpf()
        curso = random.choice(cursos_possiveis)
        boleto_pago = random.choice([True, False])
        escritor_csv.writerow([nome, cpf, curso, boleto_pago])

print(f"\nSucesso! Os dados foram salvos no arquivo '{nome_do_arquivo}'.")