# -*- coding: utf-8 -*-
#from professor import Professor
#from disciplina import Disciplina
from aluno import Aluno
'''
#dados do professor

professor1 = Professor('Felipe Santos Silva', 'felipe.santos@impacta.com.br', '180002', '11 9 8000 2222', list())

professor2 = Professor('João Ferreira', 'joao.ferreira@impacta.com.br', '180031', '11 9 9999 3333', list())

#dados da disciplina
disciplina1 = Disciplina('Matematica', 80, 100, professor1.nome)
disciplina2 = Disciplina('SQL', 40, 50, professor1.nome)
disciplina3 = Disciplina('LPI', 20, 25, professor1.nome)
'''
#dados do aluno
aluno1 = Aluno('Áureo Fujisawa', 'aureo261@gmail.com', '1701913', '11 9 8620 0214', 0, [])
#aluno2 = Aluno('Fernanda Nunes', 'fernanda.n@gmail.com', '1701914', '11 9 8080 2121', 10, [])

def test_nome_aluno():
    assert aluno1.nome == 'Áureo Fujisawa'
    #assert aluno2.nome == 'Fernanda Nunes'
'''
def test_email_aluno():
    assert aluno1.email == 'aureo261@gmail.com'
    assert aluno2.email == 'fernanda.n@gmail.com'

def test_ra_aluno():
    assert aluno1.ra == '1701913'
    assert aluno2.ra == '1701914'

def test_celular_aluno():
    assert aluno1.celular == '11 9 8620 0214'
    assert aluno2.celular == '11 9 8080 2121'

def test_desconto_aluno():
    assert aluno1.desconto == 0
    assert aluno2.desconto == 10

def test_retorna_sobrenome_aluno():
    assert aluno1.retorna_sobrenome == 'Fujisawa'
    assert aluno2.retorna_sobrenome == 'Nunes'

def test_disciplinas_aluno():
    assert aluno1.disciplinas == []
    assert aluno2.disciplinas == []

def test_adiciona_disciplina():
    aluno1.adiciona_disciplina(disciplina1)
    aluno1.adiciona_disciplina(disciplina2)
    aluno1.adiciona_disciplina(disciplina3)

    assert aluno1.disciplinas[0].nome == 'Matematica'
    assert aluno1.disciplinas[1].nome == 'SQL'
    assert aluno1.disciplinas[2].nome == 'LPI'

def test_aumenta_desconto():
    aluno1.aumenta_desconto(50)
    aluno2.aumenta_desconto(10)

    assert aluno1.desconto == 50
    assert aluno2.desconto == 20

def test_diminui_desconto():
    aluno1.diminui_desconto(10)
    aluno2.diminui_desconto(5)

    assert aluno1.desconto == 40
    assert aluno2.desconto == 15

def test_retorna_carga_horaria():
    assert aluno1.retorna_carga_horaria() == 140
    assert aluno2.retorna_carga_horaria() == 0

def test_retorna_valor_mensalidade():
    assert aluno1.retorna_valor_mensalidade() == 135
    assert aluno2.retorna_valor_mensalidade() == -15
'''