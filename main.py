# Arquivo: main.py

# Importa a sua classe principal do arquivo gerenciador.py
from gerenciador_do_sistema import gerenciador_alunos

def menu_interativo():
    # Cria o objeto principal que gerencia tudo
    sistema = gerenciador_alunos()
    print("Bem-vindo ao Sistema de Vestibular da FATEC Rio Claro!")
    
    # Pergunta se o usuário quer carregar dados de um arquivo no início
    carregar = input("Deseja carregar dados do arquivo 'vestibulandos.csv'? (s/n): ").lower()
    if carregar == 's':
        sistema.carregar_vestibulandos_de_csv('vestibulandos.csv')

    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Inscrever Candidato Manualmente")
        print("2. Cadastrar Aplicador")
        print("--- Operações ---")
        print("3. Calcular Salas Necessárias")
        print("4. Distribuir Candidatos por Sala")
        print("5. Ver Relatório Candidato/Vaga")
        print("6. Iniciar Processo de Aprovação")
        print("--- Listagens ---")
        print("7. Listar Candidatos Inscritos")
        print("8. Listar Aplicadores")
        print("9. Listar Aprovados")
        print("0. Sair")
        
        escolha = input("Escolha uma opção: ")

        try:
            if escolha == '1':
                nome = input("Nome do candidato: ")
                cpf = input("CPF do candidato (ex: 123.456.789-00): ")
                curso = input("Curso (IA ou ESG): ")
                boleto_pago_str = input("Boleto foi pago? (s/n): ").lower()
                boleto_pago = (boleto_pago_str == 's')
                sistema.inscrição(nome, cpf, curso, boleto_pago)

            elif escolha == '2':
                nome = input("Nome do aplicador: ")
                cargo = input("Cargo do aplicador: ")
                sistema.cadastrar_aplicador(nome, cargo)

            elif escolha == '3': 
                sistema.calcular_salas_necessarias()

            elif escolha == '4': 
                sistema.distribuir_alunos_em_salas()

            elif escolha == '5': 
                sistema.exibir_relatorio_candidato_vaga()

            elif escolha == '6': 
                sistema.processar_aprovacao_manual()

            elif escolha == '7': 
                sistema.listar_os_vestubulandos()

            elif escolha == '8': 
                sistema.listar_aplicadores()

            elif escolha == '9':
                sistema.listar_aprovados()

            elif escolha == '0':
                print("Saindo do sistema. Até logo!")
                break
            else:
                print("[ERRO] Opção inválida, por favor tente novamente.")
        
        except Exception as e:
            # Proteção para qualquer erro inesperado
            print(f"[ERRO INESPERADO] Ocorreu um problema: {e}")

# --- Ponto de Entrada do Programa ---
if __name__ == "__main__":
    menu_interativo()