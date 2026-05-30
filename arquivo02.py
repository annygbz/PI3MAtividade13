class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'Nome: {self.nome} | Idade: {self.idade} | Profissão: {self.profissao}'

    def aniversario(self):
        self.idade += 1


pessoa1 = Pessoa('Anny', 17, 'Estudante')

print('Dados da pessoa:')
print(pessoa1)

pessoa1.aniversario()

print('\nApós aniversário:')
print(pessoa1)