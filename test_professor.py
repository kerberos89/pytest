# -*- coding: utf-8 -*-
from professor import Professor
from disciplina import Disciplina
from aluno import Aluno

#dados do professor
professor1 = Professor('Felipe Santos Silva', 'felipe.santos@impacta.com.br', '180002', '11 9 8000 2222', list())

professor2 = Professor('João Ferreira', 'joao.ferreira@impacta.com.br', '180031', '11 9 9999 3333', list())

#dados da disciplina
disciplina1 = Disciplina('Matematica', 80, 100, professor1.nome)
disciplina2 = Disciplina('SQL', 40, 50, professor1.nome)
disciplina3 = Disciplina('LPI', 20, 25, professor1.nome)

def test_nome_professor():
    assert professor1.nome == 'Felipe Santos Silva'
    assert professor2.nome == 'João Ferreira'

def test_email_professor():
    assert professor1.email == 'felipe.santos@impacta.com.br'
    assert professor2.email == 'joao.ferreira@impacta.com.br'

def test_ra_professor():
    assert professor1.ra == '180002'
    assert professor2.ra == '180031'

def test_celular_professor():
    assert professor1.celular == '11 9 8000 2222'
    assert professor2.celular == '11 9 9999 3333'

def test_disciplinas_professor():
    assert professor1.disciplinas == []
    assert professor2.disciplinas == []

def teste_add_disciplina():
    professor1.adiciona_disciplina(disciplina1)
    professor1.adiciona_disciplina(disciplina2)
    professor1.adiciona_disciplina(disciplina3)

    assert professor1.disciplinas[0].nome == 'Matematica'
    assert professor1.disciplinas[1].nome == 'SQL'
    assert professor1.disciplinas[2].nome == 'LPI'
    assert professor2.adiciona_disciplina(disciplina1) == 'Não foi possível adicionar a disciplina'

def test_retorna_sobrenome():
    assert professor1.retorna_sobrenome == 'Silva'
    assert professor2.retorna_sobrenome == 'Ferreira'    

def test_retorna_carga_horaria():  
    assert professor1.retorna_carga_horaria() == 7