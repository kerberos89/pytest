# -*- coding: utf-8 -*-
class Pessoa():
    def __int__(self, nome = None, email = None, ra = None, celular = None, disciplinas = None):
        if nome != None:
            self.__nome = nome
        if email != None:
            self.__email = email
        if ra != None:
            self.__ra = ra
        if celular != None:
            self.__celular = celular
        if disciplinas != None:
            self.__disciplinas = list(disciplinas)

    @property
    def nome(self):
        return self.__nome
    @property
    def email(self):
        return self.__email
    @property
    def ra(self):
        return self.__ra
    @property
    def celular(self):
        return self.__celular
    @property
    def disciplinas(self):
        return self.__disciplinas
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    @email.setter
    def email(self, email):
        self.__email = email
    @ra.setter
    def ra(self, ra):
        self.__ra = ra
    @celular.setter
    def celular(self, celular):
        self.__celular = celular
    @disciplinas.setter
    def disciplinas(self, disciplinas):
        self.__disciplinas = disciplinas