# -*- coding: utf-8 -*-
class Professor():
    def __init__(self, nome = None, email = None, ra = None, celular = None, disciplinas = None):
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
    
    @property
    def retorna_sobrenome(self):
        sobrenome = self.__nome.split(' ')
        return sobrenome[len(sobrenome)-1]

    def adiciona_disciplina(self, disciplina):
        if self.__nome == disciplina.professor:
            return self.__disciplinas.append(disciplina)
        else:
            return 'Não foi possível adicionar a disciplina'
    
    def retorna_carga_horaria(self):
        somar = float(0)    
        for x in range(0, len(self.disciplinas), 1):
            somar += self.__disciplinas[x].carga_horaria / 20
        return somar