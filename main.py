from classes import contato
from classes.agenda import Agenda
from classes.contato import Contato
from tarefa import Tarefa

class Main:

    def __init__(self):
        self.em_execucao = True
        self.agenda = Agenda()
        self.agenda.set_proprietario("hiuri")
        self.agenda.set_ano(2021)

    def mostrar_menu(self):
        print("")
        print("==========================")
        print("A G EN D A  V I R T U A L")
        print("==========================")
        print("selecione uma opção: ")
        print("1 Cadastrar contato: ")
        print("2. Listar contatos: ")
        print("3. Excluir contato: ")
        print("4. listar tarefas: ")
        print("5. Listar tarefa: ")
        print("6. Excluir tarefa: ")
        print("0. Sair do programa: ")

    def ler_opcao_menu(self):
        opcao = input("'>'")

        if (opcao == "0"):
            print("Obrigado por usar nossa agenda virtual")
            self.em_execucao = False
            return

        if(opcao == "1"):
            self.cadastrar_contato()
        elif (opcao == "2"):
            self.listar_contato()
        elif (opcao == "3"):
            self.excluir_contato()
        elif(opcao == "4"):
            self.cadastrar_tarefa()
        elif(opcao == "5"):
            self.listar_tarefas()
        elif(opcao == "6"):
            self.excluir_tarefa()


    def cadastrar_contato(self):
        print("novo contato")
        nome = input("Nome: ")
        telefone = input("telefone: ")
        email = input("email: ")
        cpf = input("cpf: ")

        contato = Contato()
        contato.set_nome(nome)
        contato.set_telefone(telefone)
        contato.set_email(email)
        contato.set_cpf(cpf)

        self.agenda.add_contatos(contato)
        print("contato adicionado com sucesso")

    def cadastrar_tarefa(self):
        print("nova tarefa")
        descricao = input("descrição: ")
        status = input("concluido? 1 - sim / 0 - não: ")

        tarefa = Tarefa()
        tarefa.set_descricao(descricao)
        if(status == "1"):
            tarefa.set_status_concluida()
        elif(status == "0"):
            tarefa.set_status_pendente()
        else:
            print('status invalido.')
            return

        self.agenda.sdd_tarefa(tarefa)
        print("tarefa adicionado com sucesso")

    def listar_tarefas(self):
            print("lista de tarefas")
            tarefas_da_agenda = self.agenda.get_tarefa()
            for indice, contato in enumerate(contatos_da_agenda):
                print("numero: " + str(indice) + ". - " + tarefa.get_descricao() + "status /" + tarefa.get_status())


    def listar_contato(self):
        print("lista de contatos")
        contatos_da_agenda = self.agenda.get_contatos()
        for indice, contato in enumerate(contatos_da_agenda):
            print("numero: " + str(indice) + ". - Contato: " + contato.get_nome() + " / Tel:" + contato.get_telefone())

    def excluir_contato(self):
        self.listar_contato()
        indice_para_excluir = input("digite o numero de ordem do contato: ")

        try:
            contato_selecionado = self.agenda.get_contato(int(indice_para_excluir))
        except:
            print("contato inválido")
            return
        self.agenda.remover_contato(contato_selecionado)
        print("Contato Excluido com sucesso")

def excluir_tarefa(self):
        self.listar_tarefas()
        indice_para_excluir = input("digite o numero de ordem da tarefa: ")

        try:
            tarefa_selecionada = self.agenda.tarefa(int(indice_para_excluir))
        except:
            print("tarefa inválida")
            return

        self.agenda.remover_tarefa(contato_selecionado)
        print("tarefa Excluida com sucesso")
