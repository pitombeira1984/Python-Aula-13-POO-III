from Operador import Projeto

def main():
    while True:
        print("1 - Adicionar Tarefa")
        print("2 - Remover Terefa")
        print("3 - Mostrar Tarefas")
        print("4 - Editar Tarefa")
        print("5 - Marcar Tarefa Concluida")
        print("6 - Sair")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            tarefa = input("Digite a tarefa: ")
            projeto.adicionar_tarefa(tarefa)
        elif opcao == 2:
            tarefa = input("Digite a tarefa: ")
            projeto.remover_tarefa(tarefa)
        elif opcao == 3:
            projeto.mostrar_tarefas()
        elif opcao == 4:
            tarefa = input("Digite a tarefa: ")
            nova_tarefa = input("Digite a nova tarefa: ")
            projeto.editar_tarefa(tarefa, nova_tarefa)
        elif opcao == 5:
            tarefa = input("Digite a tarefa: ")
            projeto.marcar_tarefa_concluida(tarefa)
        elif opcao == 6:
            break
        else:
            print("Opção inválida")
            
if __name__ == "__main__":
    projeto = Projeto([])
    main()