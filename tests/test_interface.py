import pytest
from codigo.interface import App


E_P_C = {
    '_': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'tipo1': ['1a', '1b'],
    'tipo2': ['2a']
}


@pytest.fixture
def objeto1():
    app = App(E_P_C)
    return app


def test_tipo_dados_de_retorno(objeto1):
    dados = objeto1.entradas.get_entradas()
    assert isinstance(dados, dict)


def test_nomes_radios(objeto1):
    lista = objeto1.entradas.radios_criados  
    assert 'tipo1' in lista[0].cget('text')
    assert 'tipo2' in lista[1].cget('text')


def test_valores_radio(objeto1):
    lista = objeto1.entradas.radios_criados
    lista[0].select()
    assert objeto1.entradas.tipo.get() == lista[0].cget('value')

    lista[1].select()
    assert objeto1.entradas.tipo.get() != lista[0].cget('value')


def test_nomes_entradas(objeto1):
    lista = objeto1.entradas.entradas_criadas.keys()
    assert '1b' in lista
    assert 'd' in lista
    assert 'h' not in lista


def test_valores_entradas(objeto1):
    for i in objeto1.entradas.entradas_criadas:
        var = objeto1.entradas.entradas_criadas[i]['entry'].cget('textvariable')
        assert var.get() == '0'

    for i in objeto1.entradas.entradas_criadas:
        var = objeto1.entradas.entradas_criadas[i]['entry'].cget('textvariable')
        var.set('abc')

    for i in objeto1.entradas.entradas_criadas:
        var = objeto1.entradas.entradas_criadas[i]['entry'].cget('textvariable')
        assert var.get() == 'abc'


def test_caixa_texto_de_saida(objeto1):
    txt = objeto1.saida.cx_Txt.get('0.0', 'end')
    assert txt.strip() == '...'

    objeto1.saida.cx_Txt.delete('0.0', 'end')
    test = 'Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...'
    objeto1.saida.cx_Txt.insert('0.0', test)

    txt = objeto1.saida.cx_Txt.get('0.0', 'end')
    assert txt.strip() == test

def test_funcao_recebe_texto(objeto1):
    texto = 'Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...'
    objeto1.saida.recebe_texto(texto)
    saida = objeto1.saida.cx_Txt.get('0.0', 'end')
    
    assert saida.strip() == texto

