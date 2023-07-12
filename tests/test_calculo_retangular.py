import pytest
from codigo.backend import CalculoRetangular

@pytest.fixture
def objeto1():
    objetoCalculoRet = CalculoRetangular(
        h=50,
        bw=20,
        fck=30,
        fyk=500,
        cobrimento= 2.5,
        combinacao=1,
        dmax_agreg=14,
        est=5,
        arm=10,
        msd=300
    )

    return objetoCalculoRet

# @pytest.fixture
# def objeto2():
#     objetoCalculoRet = CalculoRetangular(
#         h=50,
#         bw=20,
#         fck=30,
#         fyk=500,
#         cobrimento= 2.5,
#         combinacao=1,
#         dmax_agreg=14,
#         est=5,
#         arm=10,
#         msd=300
#     )
#     objetoCalculoRet.calc_secao_retang()

#     return objetoCalculoRet

def test_calculo_da_area_de_concreto(objeto1):
    objeto1._area_de_Concreto()
    assert objeto1._AC == ...

def test_calculo_asmin(objeto1):
    objeto1._asmin_Func() 
    assert objeto1._asmin == ...

def test_calculo_aspele(objeto1):
    objeto1._aspele()
    assert objeto1._aspele_face == ...
    assert objeto1._aspele_tot == ...          

def test_calculo_as_Max(objeto1):
    objeto1._as_Max()
    assert objeto1._asmax == ...

def test_calculo_ycys(objeto1):
    objeto1._ycys()
    assert objeto1._yc == ...
    assert objeto1._ys == ...

def test_calculo_par_fck(objeto1):
    objeto1._par_fck()
    assert objeto1._λ == ...
    assert objeto1._ac == ...
    assert objeto1._x_d == ...

def test_calculo_calc_fcd(objeto1):
    objeto1._calc_fcd()
    assert objeto1._fcd == ...

def test_calculo_calc_fyd(objeto1):
    objeto1._calc_fyd()
    assert objeto1._fyd == ...

def test_calculo_dFuncao(objeto1):
    objeto1._dFuncao()
    assert objeto1._d == ...

def test_calculo_dLinha(objeto1):
    objeto1._dLinha()   
    assert objeto1._dlinha == ...

def test_calculo_calc_xlim(objeto1):
    objeto1._calc_xlim()
    assert objeto1._xlim == ...

def test_calculo_calc_x(objeto1):
    objeto1._calc_x()
    assert objeto1._x == ... 

def test_calculo_msdZFuncao(objeto1):
    objeto1._msdZFuncao()
    assert objeto1._MSD == ... 

def test_calculo_funcaoDiversos(objeto1):
    objeto1._funcaoDiversos()
    assert objeto1._z == ...
    assert objeto1._σsd == ... 
    assert objeto1._ΔM == ... 
    assert objeto1._aslim == ... 
    assert objeto1._aslinha == ... 
    assert objeto1._as_ == ... 

def test_todos_os_calculos_retangular(objeto2):
    ...
