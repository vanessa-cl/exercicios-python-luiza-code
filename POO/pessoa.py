class Pessoa:
    def __init__(self, nome: str, cpf: str, idade: int):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
    
    def retorna_documento(self):
        return f"{self.nome} possui {self.idade} anos e CPF número {self.cpf}"
        
    def determina_se_eh_fumante(self, opcao: str):
        if opcao == 'F' or opcao == 'f':
            self.fumante = True
            return f"{self.nome} é fumante"
        elif opcao == 'N' or opcao == 'n':
            self.fumante = False
            return f"{self.nome} não é fumante"
        else:
            return "Opção incorreta! Tente novamente"

pessoa = Pessoa("Vanessa", "123.456.789-00", 21)
print(pessoa.retorna_documento())
print(pessoa.determina_se_eh_fumante("N"))
