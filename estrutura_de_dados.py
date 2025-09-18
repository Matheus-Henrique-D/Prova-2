class atributos_alunos:
    def __init__(self, nome, cpf, curso, boleto, matricula):
        if not nome.replace(' ','').isalpha():
            raise ValueError("Nome inválido. Use apenas letras e espaços.")
        self.nome = nome

        cpf_limpo = cpf.replace('.', '').replace('-', '')
        if not (cpf_limpo.isdigit() and len(cpf_limpo) == 11):
            raise ValueError("CPF inválido. Deve conter 11 dígitos.")
        self.cpf = cpf

        if curso.upper() not in ["IA", "ESG"]:
            raise ValueError("Curso inválido. Escolha apenas entre 'IA' e 'ESG'.")
        self.curso = curso.upper()
        
        self.boleto = bool(boleto)
        self.matricula = int(matricula)
        self.next = None

    def verificador(self):
        if self.boleto:
            return "Efetivada"
        else:
            return "Pendente"

    def __str__(self):
        status = self.verificador()
        return f"Matrícula: {self.matricula}, Nome: {self.nome}, Curso: {self.curso}, Status: {status}"

class aplicador:
    def __init__(self, nome, cargo): 
        self.nome_aplicador = nome
        self.cargo = cargo
        self.next = None

    def __str__(self):
        return f"Nome: {self.nome_aplicador}, Cargo: {self.cargo}"

class Aprovado:
    def __init__(self, nome, cpf, curso):
        self.nome = nome
        self.cpf = cpf
        self.curso = curso
        self.next = None

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Curso: {self.curso}"