from .contato import Contato
from .tarefa import Tarefa


class Agenda:

    def _init_(self):
        self.__proprietario = ""
        self.__ano = 0
        self.__contatos = []
        self.__tarefa = []

    def get_proprietario(self):
        return self.__proprietario

    def set_proprietario(self, proprietario):
        self.__proprietario = proprietario

    def get_ano(self):
        return self.__ano

    def set_ano(self, ano):
        self.__ano = ano

    def get_contatos(self):
        return self.__contatos

    def add_contatos(self, contatos):
        self.__contatos.append(contatos)

    def get_tarefa(self):
        return self.__tarefa

    def add_tarefa(self, tarefa):
        self.__tarefa.append(tarefa)

    def remover_contato(self,contato):
        sel.__contato.remove(contato)

    def get_contato(self, posicao_contato):
        return self.__contato[posicao_contato]

    def remover_tarefa(self,tarefa):
        sel.__tarefa.remove(tarefa)

    def get_tarefa(self, posicao_tarefa):
        return self.__tarefa[posicao_tarefa]

