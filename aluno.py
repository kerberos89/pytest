# -*- coding: utf-8 -*-
from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome = None, email = None, ra = None, celular = None, desconto = None, disciplinas = []):
        super().__init__(nome = None, email = None, ra = None, celular = None, disciplinas = None)

        if desconto != None:
            self.__desconto = float(desconto)
    
    @property
    def desconto(self):
        return self.__desconto
    
    @desconto.setter
    def desconto(self, desconto):
        self.__desconto = desconto

    @property
    def retorna_sobrenome(self):
        sobrenome = self.__nome.split(' ')
        return str(sobrenome[len(sobrenome)-1])
       
    def adiciona_disciplina(self, disciplina):
        return self.__disciplinas.append(disciplina)
       
    def aumenta_desconto(self, desconto):
        self.__desconto += desconto

    def diminui_desconto(self, desconto):
        self.__desconto -= desconto

    def retorna_carga_horaria(self):
        somar = 0
        for x in range(0, len(self.__disciplinas), 1):
            somar += self.__disciplinas[x].carga_horaria
        return somar

    def retorna_valor_mensalidade(self):
        somar = 0
        for x in range(0, len(self.__disciplinas), 1):
            somar += self.__disciplinas[x].mensalidade

        somar = somar - self.__desconto

        return somar  