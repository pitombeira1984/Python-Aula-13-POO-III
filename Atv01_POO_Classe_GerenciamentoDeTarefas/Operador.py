

class Projeto():
    def __init__(self, tarefas):
        self.tarefas = tarefas

        self.tarefas_fazer = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas_fazer.append(tarefa)
    
    def remover_tarefa(self, tarefa):
        self.tarefas_fazer.remove(tarefa)
    
    def mostrar_tarefas(self):
        for tarefa in self.tarefas_fazer:
            print(tarefa)

    def editar_tarefa(self, tarefa, nova_tarefa):
        self.tarefas_fazer[self.tarefas_fazer.index(tarefa)] = nova_tarefa
    
    def marcar_tarefa_concluida(self, tarefa):
        self.tarefas_fazer.remove(tarefa)
        self.tarefas.append(tarefa)