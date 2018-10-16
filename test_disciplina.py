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

def test_nome_disciplina():
    assert disciplina1.nome == 'Matematica'
    assert disciplina2.nome == 'SQL'
    assert disciplina3.nome == 'LPI'

def test_carga_horaria_disciplina():
    assert disciplina1.carga_horaria == 80
    assert disciplina2.carga_horaria == 40
    assert disciplina3.carga_horaria == 20

def test_mensalidade_disciplina():
    assert disciplina1.mensalidade == 100
    assert disciplina2.mensalidade == 50
    assert disciplina3.mensalidade == 25

def test_professor_disciplina():
    assert disciplina1.professor == 'Felipe Santos Silva'
    assert disciplina2.professor == 'Felipe Santos Silva'
    assert disciplina3.professor == 'Felipe Santos Silva'

def test_retorna_valor_hora():
    assert disciplina1.retorna_valor_hora() == 7.5
    assert disciplina2.retorna_valor_hora() == 7.5
    assert disciplina3.retorna_valor_hora() == 7.5