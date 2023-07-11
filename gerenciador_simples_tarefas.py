class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def remover_tarefa(self, tarefa):
        self.tarefas.remove(tarefa)

    def listar_tarefas(self):
        if self.tarefas:
            print("Lista de Tarefas:")
            for i, tarefa in enumerate(self.tarefas, 1):
                print(f"{i}. {tarefa}")
        else:
            print("Não há tarefas na lista.")


gerenciador = GerenciadorTarefas()

while True:
    print("\n===== Gerenciador de Tarefas =====")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Listar Tarefas")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa a ser adicionada: ")
        gerenciador.adicionar_tarefa(tarefa)
        print("Tarefa adicionada com sucesso!")
    elif opcao == "2":
        tarefa = input("Digite a tarefa a ser removida: ")
        gerenciador.remover_tarefa(tarefa)
        print("Tarefa removida com sucesso!")
    elif opcao == "3":
        gerenciador.listar_tarefas()
    elif opcao == "4":
        print("Saindo do gerenciador de tarefas...")
        break
    else:
        print("Opção inválida. Tente novamente.")
