# -*- coding: utf-8 -*-
class Disciplina():
    def __init__(self, nome = None, carga_horaria = None, mensalidade = None, professor = None):
        if nome != None:
            self.__nome = nome
        if carga_horaria != None:
            self.__carga_horaria = float(carga_horaria)
        if mensalidade != None:
            self.__mensalidade = float(mensalidade)
        if professor != None:
            self.__professor = professor
    
    @property
    def nome(self):
        return self.__nome
    @property
    def carga_horaria(self):
        return self.__carga_horaria
    @property
    def mensalidade(self):
        return self.__mensalidade
    @property
    def professor(self):
        return self.__professor

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    @carga_horaria.setter
    def carga_horaria(self, carga_horaria):
        self.__carga_horaria = carga_horaria
    @mensalidade.setter
    def mensalidade(self, mensalidade):
        self.__mensalidade = mensalidade
    @professor.setter
    def professor(self, professor):
        self.__professor = professor

    def retorna_valor_hora(self):
        return float(self.__mensalidade * 6 / self.__carga_horaria)