# Arquivo: gerenciador.py

import math
import csv
import os

# Importa as classes de estrutura do outro arquivo
from estrutura_de_dados import atributos_alunos, aplicador, Aprovado

# As Constantes Globais 
VAGAS_IA = 40
VAGAS_ESG = 40
CAPACIDADE_SALA = 30 

class gerenciador_alunos:
    def __init__(self):
        self.vestibulando_inicio = None
        self.aplicador_inicio = None
        self.aprovados_inicio = None 
        self.id_ia = 1000
        self.id_esg = 3000

    def inscrição(self, nome, cpf, curso, boleto, silencioso=False):
        # Validação de CPF duplicado
        p = self.vestibulando_inicio
        while p is not None:
            if p.cpf == cpf:
                if not silencioso: print(f"[ERRO] CPF {cpf} já cadastrado para '{p.nome}'.")
                return
            p = p.next

        try:
            # Tenta criar o aluno. Se nome, CPF ou curso for inválido,
            # a classe atributos_alunos vai lançar um ValueError aqui.
            id_aluno = 0
            if curso.upper() == "IA": id_aluno = self.id_ia; self.id_ia += 1
            elif curso.upper() == "ESG": id_aluno = self.id_esg; self.id_esg += 1
            
            novo_aluno = atributos_alunos(nome, cpf, curso, boleto, id_aluno)
            
            if self.vestibulando_inicio is None:
                self.vestibulando_inicio = novo_aluno
            else:
                p_final = self.vestibulando_inicio
                while p_final.next is not None: p_final = p_final.next
                p_final.next = novo_aluno
            
            if not silencioso:
                print(f"-> Inscrição de {nome} (matrícula {id_aluno}) realizada com sucesso.")
        
        except ValueError as e:
            # Captura o erro de validação e mostra uma mensagem amigável.
            if not silencioso:
                print(f"[ERRO NA INSCRIÇÃO] Não foi possível inscrever '{nome}': {e}")

    def cadastrar_aplicador(self, nome, cargo):
        novo_aplicador = aplicador(nome, cargo)
        if self.aplicador_inicio is None: self.aplicador_inicio = novo_aplicador
        else:
            p = self.aplicador_inicio
            while p.next is not None: p = p.next
            p.next = novo_aplicador
        print(f"-> Aplicador '{nome}' cadastrado.")

    def listar_os_vestubulandos(self):
        print("\n--- Lista de Vestibulandos Inscritos ---")
        p = self.vestibulando_inicio
        if not p: print("Nenhum vestibulando inscrito."); return
        while p is not None: print(p); p = p.next

    def listar_aplicadores(self):
        print("\n--- Lista de Aplicadores Cadastrados ---")
        p = self.aplicador_inicio
        if not p: print("Nenhum aplicador cadastrado."); return
        while p is not None: print(p); p = p.next

    def _obter_vestibulandos_efetivados(self):
        efetivados = []
        p = self.vestibulando_inicio
        while p is not None:
            if p.boleto: 
                efetivados.append(p)
            p = p.next
        return efetivados

    def calcular_salas_necessarias(self):
        efetivados = self._obter_vestibulandos_efetivados()
        if not efetivados: print("\n-> Nenhum candidato efetivado para alocar."); return
        num_salas = math.ceil(len(efetivados) / CAPACIDADE_SALA)
        print(f"\nTotal de candidatos efetivados: {len(efetivados)}")
        print(f"-> Serão necessárias {num_salas} salas de aula.")

    def distribuir_alunos_em_salas(self):
        efetivados = self._obter_vestibulandos_efetivados()
        if not efetivados: print("\nNenhum candidato efetivado."); return
        print("\n--- Distribuição de Alunos por Sala ---")
        sala_atual, contador = 1, 0
        print(f"\n====== SALA {sala_atual} ======")
        for aluno in efetivados:
            if contador == CAPACIDADE_SALA:
                sala_atual += 1; contador = 0
                print(f"\n====== SALA {sala_atual} ======")
            print(f"- {aluno.nome} (Matrícula: {aluno.matricula})")
            contador += 1

    def exibir_relatorio_candidato_vaga(self):
        print("\n--- Relatório Candidato/Vaga ---")
        efetivos_ia, efetivos_esg = 0, 0
        p = self.vestibulando_inicio
        while p is not None:
            if p.boleto:
                if p.curso.upper() == "IA": efetivos_ia += 1
                elif p.curso.upper() == "ESG": efetivos_esg += 1
            p = p.next
        print(f"\n** IA (Vagas: {VAGAS_IA}) **")
        if VAGAS_IA > 0: print(f"Relação (efetivados): {efetivos_ia / VAGAS_IA:.2f} cand./vaga")
        print(f"\n** ESG (Vagas: {VAGAS_ESG}) **")
        if VAGAS_ESG > 0: print(f"Relação (efetivados): {efetivos_esg / VAGAS_ESG:.2f} cand./vaga")

    def processar_aprovacao_manual(self):
        print("\n--- Iniciando Processo de Aprovação Manual ---")
        efetivados = self._obter_vestibulandos_efetivados()
        if not efetivados: print("Nenhum candidato efetivado para aprovar."); return
        
        vagas_preenchidas_ia, vagas_preenchidas_esg = self.aprovados_por_curso()
        
        for candidato in efetivados:
            aprovado = False
            if candidato.curso.upper() == "IA" and vagas_preenchidas_ia < VAGAS_IA:
                resp = input(f"Aprovar {candidato.nome} ({candidato.matricula}) para IA? (s/n): ").lower()
                if resp == 's': vagas_preenchidas_ia += 1; aprovado = True
            elif candidato.curso.upper() == "ESG" and vagas_preenchidas_esg < VAGAS_ESG:
                resp = input(f"Aprovar {candidato.nome} ({candidato.matricula}) para ESG? (s/n): ").lower()
                if resp == 's': vagas_preenchidas_esg += 1; aprovado = True
            
            if aprovado:
                novo_aprovado = Aprovado(candidato.nome, candidato.cpf, candidato.curso)
                if self.aprovados_inicio is None: self.aprovados_inicio = novo_aprovado
                else:
                    p = self.aprovados_inicio
                    while p.next is not None: p = p.next
                    p.next = novo_aprovado
                print(f"-> {candidato.nome} APROVADO(A).")
        print("\n--- Processo de Aprovação Finalizado ---")

    def listar_aprovados(self):
        print("\n--- Lista Final de Aprovados ---")
        p = self.aprovados_inicio
        if not p: print("Nenhum aluno aprovado ainda."); return
        while p is not None: print(p); p = p.next

    def aprovados_por_curso(self):
        count_ia, count_esg = 0, 0
        p = self.aprovados_inicio
        while p is not None:
            if p.curso == "IA": count_ia += 1
            elif p.curso == "ESG": count_esg += 1
            p = p.next
        return count_ia, count_esg
    
    def carregar_vestibulandos_de_csv(self, nome_arquivo):
        if not os.path.exists(nome_arquivo):
            print(f"[ERRO] O arquivo '{nome_arquivo}' não foi encontrado."); return
        
        count = 0
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            leitor = csv.reader(f)
            next(leitor)
            for linha in leitor:
                nome, cpf, curso, boleto_str = linha
                self.inscrição(nome, cpf, curso, (boleto_str == 'True'), silencioso=True)
                count += 1
        print(f"-> {count} registros de vestibulandos carregados do arquivo com sucesso!")