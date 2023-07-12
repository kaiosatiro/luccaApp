from interface import App
from backend import CalculoRetangular

ENTRADAS_PARA_CRIAR = {
    'comum': ['H', 'FCK', 'FYK', 'Cobrimento', 'DmaxAgreg', 'EST', 'Armadura'],
    'Retangular': ['BW', 'MSD'],
    'I': ['MSK']
}

app = App(ENTRADAS_PARA_CRIAR)
# app.set_default_color_theme("light")

def enter_press(index):
    dados = app.entradas.get_entradas()

    combinacao = int(dados['combinacao'])
    h = float(dados['H'])
    fck = int(dados['FCK'])
    fyk = float(dados['FYK'])
    cobrimento = float(dados['Cobrimento'])
    dmaxAgreg = float(dados['DmaxAgreg'])
    est = float(dados['EST'])
    armadura = float(dados['Armadura'])
    msd = float(dados['MSD'])
    bw = float(dados['BW'])
    msk = float(dados['MSK'])
    
    calculo = CalculoRetangular(
        h=h, bw=bw, fck=fck, fyk=fyk, cobrimento=cobrimento,
        combinacao=combinacao, dmax_agreg=dmaxAgreg,
        est=est, arm=armadura, msd=msd
    )

    calculo.calc_secao_retang()
    app.saida.recebe_texto(calculo)

# app.entradas.entradas_criadas['H']['entry'].cget('textvariable').trace_add('write', enter_press)
app.bind('<Return>', enter_press)
# app.bt_Plotar.configure(command=key_press)
app.mainloop()