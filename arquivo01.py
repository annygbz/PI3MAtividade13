class Tarefa:
    tarefas = []

    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.concluido = False
        Tarefa.tarefas.append(self)

    def __str__(self):
        return f'{self.titulo} | {self.descricao}'

    @classmethod
    def listarTarefas(cls):
        for tarefa in cls.tarefas:
            print(tarefa)

    @classmethod
    def quantidadeTarefas(cls):
        return len(cls.tarefas)


tarefa_01 = Tarefa('Corrigir Provas', 'Corrigir provas 01')
tarefa_02 = Tarefa('Estudar Python', 'Estudar Orientação a Objetos')
tarefa_03 = Tarefa('Expor Projeto', 'Apresentar Projeto Integrador')

print('Lista de tarefas:')
Tarefa.listarTarefas()

print(f'\nQuantidade de tarefas: {Tarefa.quantidadeTarefas()}')