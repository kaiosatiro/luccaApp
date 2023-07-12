import matplotlib.pyplot as plt
import numpy as np


def asmin(fck, ac):
    dic = {
        20: 0.15,
        25: 0.15,
        30: 0.15,
        35: 0.164,
        40: 0.179,
        45: 0.194,
        50: 0.208,
        55: 0.211,
        60: 0.219,
        65: 0.226,
        70: 0.233,
        75: 0.239,
        80: 0.245,
        85: 0.251,
        90: 0.256,
    }
       
    return (ac *dic[fck]) / 100


def aspele(h, Ac):
    """Retorna CÁLCULO DA ÁREA DE ARMADURA DE PELE 
        (aspele_face, aspele_tot)
    """
    if h <= 60:
        return  0, 0
    elif h > 60:
        i = (0.0005 *Ac) *2
        if i <= 5:
            aspele_face = 0.0005 *Ac
            aspele_tot = i         
        elif i > 5:
            aspele_face = 5 /2
            aspele_tot = 5
        
        return aspele_face, aspele_tot


def area_de_Concreto( h, bw):
    """Retorna (h *bw)"""
    return h *bw


def as_Max(ac):
    """Retorna (Ac * 0.04)"""
    return ac *0.04


def ycys(combinacao):
    """Retorna (yc, ys)
    """
    dic = {
        1: {'yc': 1.4, 'ys': 1.15},
        2: {'yc': 1.2, 'ys': 1.15},
        3: {'yc': 1.2, 'ys': 1}
    }
    return dic[combinacao]['yc'], dic[combinacao]['ys']


def funcaoDiversos(secao, x=None, xlim=None, λ=None, Msd=None, fyd=None, d=None, dlinha=None, ac=None, fcd=None, bw=None, Msk=None, z=None):
    ''' Retorna  de acordo com a secao:
        
        'ret' ENTRA (x, xlim, λ, Msd, fyd, d, dlinha, ac, fcd, bw) RETORNA (z, σsd, ΔM, Aslim, Aslinha, As)

        'I' ENTRA (d, Msd, Msk, z, fyd, xlim, dlinha) RETORNA (ΔM, As, Aslim, Aslinha, σsd)
    '''
    if secao == 'ret':
        if x <= xlim:
            z = d -(0.5 *λ *x)
            e_s, σsd, ΔM, Aslim, Aslinha = 0,0,0,0,0
            As = Msd /(z *fyd)
        elif x > xlim:
            eyd = fyd /ES
            z = d -(0.5 *λ *xlim)
            e_s = (ECU *(xlim -dlinha)) /xlim
            if e_s > eyd:
                σsd = fyd
            elif e_s <= eyd:
                σsd = ES *e_s
            Msdlim = ac *fcd *bw *((λ *xlim *d) -(((λ **2) *(xlim **2)) /2))
            ΔM = Msd -Msdlim        
            Aslim = Msdlim /(z *fyd)
            Aslinha = ΔM /(σsd *(d -dlinha))
            As = Aslim +Aslinha
            
        return z, σsd, ΔM, Aslim, Aslinha, As
    
    elif secao == 'I':
        if Msd /100 <= Msk:        
            As = Msd /(z *fyd)       
            Aslim, Aslinha, ΔM, σsd, e_s, eyd = 0,0,0,0,0,0
        elif Msk > Msd /100:       
            Aslim = Msd /(z *fyd)        
            ΔM = 100 *Msk -Msd        
            e_s = (ECU *(xlim -dlinha)) /xlim        
            eyd = fyd /ES        
            if e_s > eyd:            
                σsd = fyd        
            if e_s <= eyd:            
                σsd = ES *e_s            
            Aslinha = ΔM /(σsd *(d -dlinha))        
            As = Aslim +Aslinha

        return ΔM, As, Aslim, Aslinha, σsd


def par_fck(fck):
    """Retorna PARÂMETROS PELO FCK (λ, ac, x_d)
    """
    if fck <= 50:
        λ = 0.8
        ac = 0.85           
        x_d = 0.45
    elif 50 < fck <= 90:
        λ = 0.8 -((fck -50) /400)
        ac = 0.85 *(1 -((fck -50) /200))        
        x_d = 0.35
    
    return λ, ac, x_d


def calc_fcd(fck, yc):
        """Retorna CÁLCULO fcd 
        (fck /(10 *yc))
        """
        fcd = fck /(10 *yc)
        
        return fck


def calc_fyd(fyk, ys):
        """Retorna CÁLCULO fyd (fyk /(10 *ys))
        """
        fyd = fyk /(10 *ys)
        
        return fyd

    
def calc_xlim(d, x_d):
    """Retorna CÁLCULO X LIMITE (x_d *d)"""
    return x_d *d


def calc_x(d, Msd, ac, fcd, bw, λ):
    """Retorna o Calculo X ((d -(((d **2) -(2 *(Msd /(ac *fcd *bw)))) **(0.5))) /λ)"""
    return (d -(((d **2) -(2 *(Msd /(ac *fcd *bw)))) **(0.5))) /λ


def dFuncao(h, cob, Øest, Øarm):
    """retorna o d | Equacao: h -(cob +(Øest /10) +(Øarm /(2 *10)))
    """
    return h -(cob +(Øest /10) +(Øarm /(2 *10)))


def dLinha(cob, Øest, Øarm):
    """retorna o dlinha | Equacao: cob +(Øest /10) +(Øarm /(2 *10))
    """
    return cob +(Øest /10) +(Øarm /(2 *10))


def bwFuncao(xlim):
    """Retorna bw"""
    if 0 <= xlim <= 35:
        bw = 40
    elif 35 < xlim <= 47.5:
        x_auxiliar = xlim -35
        bw = (-2 *x_auxiliar) +40        
    elif 47.5 < xlim <= 85:
        bw = 15    
    elif 85 < xlim <= 100:
        bw = 40
    
    return bw


def msdZFuncao(secao, **_):
    """Retorna (Msd, z) de acordo com o tipo de secao. O primeiro argumento determina a secao 'ret' ou 'I'. 
    O seguintes argumento são qualquer passados como dicionario"""
    if secao == 'ret':
        return _['msd'] *100
    elif secao == 'I':
        Q = _['fcd'] *_['λ'] *_['ac']        
        Rc = _['bw'] *_['xlim'] *Q
        z = _['d'] -(0.5 *_['xlim'] *_['λ'])
        Msd = (Rc *z)
        return Msd, z

#--------------------------------------------------------------------------------------- CAlCULO SECAO RETANGULAR -----------------------------------------
def calc_secao_retang(h, bw, fck, fyk, cob, combinação, dmáx_agr, Øest, Øarm, msd):
    Ac = area_de_Concreto(h, bw)
    Asmín = asmin(fck, Ac)       
    Aspele_face, Aspele_tot = aspele(h, Ac)
    Asmáx = as_Max(Ac)

    yc, ys = ycys(combinação) # constantes?

    λ, ac, x_d = par_fck(fck)

    fcd =  calc_fcd(fck, yc)
    fyd = calc_fyd(fyk, ys)

    d = dFuncao(h, cob, Øest, Øarm)
    dlinha = dLinha(cob, Øest, Øarm)    
       
    xlim = calc_xlim(d, x_d)
    x = calc_x(d, msd, ac, fcd, bw, λ)

    Msd = msdZFuncao('ret', msd=msd)
    
    z, σsd, ΔM, Aslim, Aslinha, As = funcaoDiversos('ret', x=x, xlim=xlim, λ=λ, Msd=Msd, fyd=fyd, d=d, dlinha=dlinha, ac=ac, fcd=fcd, bw=bw)

    print(f"""
        --------------------------
        h...........{h} cm
        bw..........{bw} cm
        fck.........{fck} MPa
        fyk.........{fyk} MPa
        comprimento.{cob} cm
        --------------------------
""")

    if combinação == 1:
        print("Combinação Normal")
    elif combinação == 2:
        print("Combinação Especial/Construção")
    elif combinação == 3:
        print("Combinação Excepcional")

    print(f"""
        ------------------------------------------
        dim. máx. agregado......{dmáx_agr} mm
        Ø estribo...............{Øest} mm
        Ø armadura longitudinal.{Øarm} mm
        Msd.....................{msd} kNm
        Área da seção...........{Ac} cm²
        d.......................{d} cm
        d'......................{dlinha} cm
        yc......................{yc}
        ys......................{ys}
        λ.......................{λ}
        ac......................{ac}
        x/d.....................{x_d}
        fcd.....................{fcd} kN/cm²
        fyd.....................{fyd} kN/cm²
        x.......................{x} cm
        xlim....................{xlim} cm
        ΔM......................{ΔM/100} kNm
        z.......................{z} cm
        As......................{As} cm²
        slim....................{Aslim} cm²
        As'.....................{Aslinha} cm²
        σsd'....................{σsd} kN/cm²
        Asmáx...................{Asmáx} cm²
        Asmín...................{Asmín} cm²
        Aspele total............{Aspele_tot} cm²
        Aspele/face.............{Aspele_face} cm²
        ------------------------------------------
""")

    return d, As, Aslinha

#--------------------------------------------------------------------------------------- PLOTAGEM RETANGULAR ----------------------------------------------
def plotagem_secao_retang(h,bw):
    x1 = [0,bw]
    y1 = [0,0]

    x2 = [0,0]
    y2 = [0,h]

    x3 = [bw,bw]
    y3 = [0,h]

    x4 = [0,bw]
    y4 = [h,h]

    x = (0,bw,1000)

    plt.figure(figsize=(bw /20, h /20), dpi=300)
    plt.axis('off')

    plt.ylim(0, h)
    plt.xlim(0, bw)

    plt.plot(x1,y1, "black",)
    plt.plot(x2,y2, "black")
    plt.plot(x3,y3, "black")
    plt.plot(x4,y4, "black")
    
    plt.fill_between(x, 0, h, alpha=0.5, color='grey')
    plt.show()
#----------------------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------- CAlCULO SECAO I --------------------------------------------------
def calc_secao_i(
        h, fck, fyk, 
        cob, combinação, 
        dmáx_agr,
        Øest, Øarm,
        Msk,
        b_banzo_inf, h_banzo_inf, b_banzo_sup, h_banzo_sup,
        b_alma, h_alma,
        b_misula_inf, h_misula_inf, b_misula_sup, h_misula_sup
):
    
    # Criar funcao para Ac
    Ac = (b_banzo_inf*h_banzo_inf)+(b_banzo_sup*h_banzo_sup)+(b_alma*h_alma)+(2*(b_misula_inf*h_misula_inf)/2)+(2*(b_misula_sup*h_misula_sup)/2)+(h_misula_inf*b_alma)+(h_misula_sup*b_alma)
    
    Asmín = asmin(fck, Ac) 
    Aspele_face, Aspele_tot = aspele(h, Ac)        
    
    Asmáx = as_Max(Ac)
    
    yc, ys = ycys(combinação)    #Truque, para ajudar na pesquisa com ctrl+F, coloque comentarios
    λ, ac, x_d = par_fck(fck)     

    fcd =  calc_fcd(fck, yc)
    fyd = calc_fyd(fyk, ys)
    
    d = dFuncao(h, cob, Øest, Øarm)
    dlinha = dLinha(cob, Øest, Øarm)
    
    xlim = calc_xlim(d, x_d)
    bw = bwFuncao(xlim)

    Msd, z = msdZFuncao('I', fcd=fcd, λ=λ, ac=ac, bw=bw, xlim=xlim, d=d)
    ΔM, As, Aslim, Aslinha, σsd = funcaoDiversos('I', d=d, Msd=Msd, Msk=Msk, z=z, fyd=fyd, xlim=xlim, dlinha=dlinha)

    print(f"""
        --------------------------
        h...........{h} cm
        bw..........{bw} cm
        fck.........{fck} MPa
        fyk.........{fyk} MPa
        comprimento.{cob} cm
        --------------------------
""")

    if combinação ==1:
        print("Combinação Normal")
    elif combinação ==2:
        print("Combinação Especial/Construção")
    elif combinação ==3:
        print("Combinação Excepcional")

    print(f"""
        ------------------------------------------
        dim. máx. agregado......{dmáx_agr} mm
        Ø estribo...............{Øest} mm
        Ø armadura longitudinal.{Øarm} mm
        Msd.....................{Msd} kNm
        Área da seção...........{Ac} cm²
        Msk.....................{Msk}kNm
        d.......................{d} cm
        d'......................{dlinha} cm
        yc......................{yc}
        ys......................{ys}
        λ.......................{λ}
        ac......................{ac}
        x/d.....................{x_d}
        fcd.....................{fcd} kN/cm²
        fyd.....................{fyd} kN/cm²
        xlim....................{xlim} cm
        ΔM......................{ΔM/100} kNm
        z.......................{z} cm
        As......................{As} cm²
        Aslim...................{Aslim} cm²
        As'.....................{Aslinha} cm²
        σsd'....................{σsd} kN/cm²
        Asmáx...................{Asmáx} cm²
        Asmín...................{Asmín} cm²
        Aspele total............{Aspele_tot} cm²
        Aspele/face.............{Aspele_face} cm²
        ------------------------------------------
""")

    return As, Aslinha 

#--------------------------------------------------------------------------------------- PLOTAGEM I #------------------------------------------------------
def plotagem_secao_i(
        h,
        h_banzo_inf, b_banzo_inf,
        h_alma, b_alma,
        misula_inf, h_misula_inf,  b_misula_inf,
        h_banzo_sup, b_banzo_sup,
        misula_sup, h_misula_sup,  b_misula_sup
):
    
    plt.figure(dpi=300)

    x1 = [0, b_banzo_inf]
    y1 = [0,0]

    x2 = [0,0]
    y2 = [0, h_banzo_inf]

    x3 = [b_banzo_inf, b_banzo_inf]
    y3 = [0, h_banzo_inf]

    if misula_inf == ("nao"):        
        x4 = [0, (b_banzo_inf - b_alma) /2]
        y4 = [h_banzo_inf, h_banzo_inf]
            
        x5 = [b_banzo_inf, b_banzo_inf -((b_banzo_inf - b_alma) /2)]
        y5 = [h_banzo_inf, h_banzo_inf]
        
        h_1 = h_banzo_inf
        b_1_dir = (b_banzo_inf - b_alma) /2
        b_1_esq = b_banzo_inf -((b_banzo_inf - b_alma) /2)

    if misula_inf == ("sim"):        
        x4 = [0, b_misula_inf]
        y4 = [h_banzo_inf, h_banzo_inf + h_misula_inf]
            
        x5 = [b_banzo_inf, b_banzo_inf - b_misula_inf]
        y5 = [h_banzo_inf, h_banzo_inf + h_misula_inf]
        
        h_1 = h_banzo_inf + h_misula_inf
        b_1_dir = b_misula_inf
        b_1_esq = b_banzo_inf - b_misula_inf

    x6 = [b_1_dir, b_1_dir]
    y6 = [h_1, h_1 +h_alma]

    x7 = [b_1_esq, b_1_esq]
    y7 = [h_1,h_1 +h_alma]

    h_2 = h_1 +h_alma

    if misula_sup == ("nao"):
        x8 = [b_1_dir, b_1_dir -((b_banzo_sup - b_alma) /2)]
        y8 = [h_2, h_2]

        x9 = [b_1_esq, b_1_esq + (b_banzo_sup -((b_banzo_sup - b_alma) /2))]
        y9 = [h_2, h_2]

        h_3 = h_2
        b_2_dir = b_1_dir -((b_banzo_sup -b_alma) /2)
        b_2_esq = b_1_esq +(b_banzo_sup- ((b_banzo_sup - b_alma) /2))
        
    if misula_sup == ("sim"):
        x8 = [b_1_dir, b_1_dir - b_misula_sup]
        y8 = [h_2,h_2 + h_misula_sup]

        x9 = [b_1_esq, b_1_esq + b_misula_sup]
        y9 = [h_2, h_2 + h_misula_sup]
        
        h_3 = h_2 + h_misula_sup
        b_2_dir = b_1_dir - b_misula_sup
        b_2_esq = b_1_esq + b_misula_sup

    x10 = [b_2_dir, b_2_dir]
    y10 = [h_3,h_3 + h_banzo_sup]

    x11 = [b_2_esq, b_2_esq]
    y11 = [h_3,h_3 + h_banzo_sup]

    x12 = [b_2_dir, b_banzo_sup]
    y12 = [h_3 + h_banzo_sup, h_3 + h_banzo_sup]

    bw = max([b_banzo_inf, b_banzo_sup])
        
    plt.figure(figsize=(bw/20,h/20), dpi=300)
    plt.axis('off')

    plt.ylim(0, h)
    plt.xlim(0, bw)

    plt.plot(x1,y1, "black")
    plt.plot(x2,y2, "black")
    plt.plot(x3,y3, "black")
    plt.plot(x4,y4, "black")
    plt.plot(x5,y5, "black")
    plt.plot(x6,y6, "black")
    plt.plot(x7,y7, "black")
    plt.plot(x8,y8, "black")
    plt.plot(x9,y9, "black")
    plt.plot(x10,y10, "black")
    plt.plot(x11,y11, "black")
    plt.plot(x12,y12, "black")    

#----------------------------------------------------------------------------------------------------------------------------------------------------------
def n_arm_e_espaçamento(d, bw, As, Aslinha, cob, Øest, Øarm, dmáx_agr):    
    ah = float(0)
    av = float(0)
    
    n_tot = As /(np.pi *((Øarm /(10 *2)) **2))
    n_tot = float(round(n_tot +0.5))

    fator1 = 20 /10
    fator2 = Øarm /10
    fator3 = (dmáx_agr *1.2) /10
    fator4 = (dmáx_agr *0.5) /10

    ah = max([fator1, fator2, fator3, fator4])

    n_linha = float((bw -(2 *(Øest /10)) -2 *cob +ah)/(ah +(Øarm /10)))
    n_linha = float(round(n_linha -0.5))

    ah_d = (bw -(2 *(Øest /10)) -(2 *cob) -(n_linha *(Øarm /10))) /(n_linha -1)

    n_camadas = n_tot /n_linha 
    n_camadas = float(round(n_camadas +0.5)) # pode reunir as duas em uma expressao?
        
    if n_linha * n_camadas == n_tot:        
        n_ult_camada = 0
        
    elif n_linha * n_camadas != n_tot:        
        n_ult_camada = n_tot -(n_linha *(n_camadas -1))
        
    # SEQUENCIA DE IF PARA NUMERO DE CAMADAS ATÉ 10:        
    dist = (Øarm /(2 *10)) +av +(Øarm /(2 *10))

    if n_camadas == 1:
        t = 0
    elif n_camadas > 1:
        for i in range(1, n_camadas -1):
            t += n_linha *dist *i
        t += n_ult_camada *dist *(n_camadas-1)
        t = t / n_tot
    
    d = d-t
    print(f"""
        n barras total...........{n_tot}
        Fator 1.................{fator1},"cm
        Fator 2.................{fator2},"cm
        Fator 3.................{fator3},"cm
        ah......................{ah_d} cm
        nmáx de barras na linha.{n_linha}
        n de camadas............{n_camadas}
        n na última camada......{n_ult_camada}
        dist....................{dist}
        cg novo.................{t}
        d.......................{d}
""")
    
    return d, t
        
# def plotagem_bitola(Ø):  
#         theta = np.linspace( 0 , 2 * np.pi , 1000 )         
#         Ø = float(input('Ø arm.lon. (mm) = '))
#         r = (Ø/(2*10))
#         cob = 3        
#         coordx = cob
#         coordy = cob        
#         rx = r * np.cos( theta ) + coordx
#         ry = r * np.sin( theta ) + coordy 
#         plt.plot(rx,ry,'black' ) 
#         plt.fill(rx,ry,color='black')         
#         plt.show()     


# DECLARACAO DE CONSTANTES GLOBAIS
ECU = 0.0035
ES = 21000



if __name__ == '__main__':  
    print("SELECIONE O TIPO DE SEÇÃO TRANSVERSAL")
    o = int(input('Tipo de Seção (retangular - 1, viga I - 2): '))
    if o == 1:
        print("********Seção Retangular (1) ********")
    elif o == 2:                
        print("******** Seção I (2) ********")

    if o == 1:
        H = float(input('h (cm) = '))
        BW = float(input("bw (cm) = "))
        FCK = float(input("fck (MPa) = "))
        FYK = float(input("fyk (MPa) = "))
        COB = float(input("cobrimento (cm) = "))
        COMBINAÇÃO = int(input("Combinação (NORMAL-1,ESPECIAL/CONSTRUÇÃO-2,EXPEPCIONAL-3 = "))
        DMÁX_AGR = float(input("dim. máx. do agregado (mm) = "))
        ØEST = float(input("Ø estribo (mm) = "))
        ØARM = float(input("Ø armadura long. (mm) = "))
        MSD = float(input("Msd (kNm) = "))
        
        print("\n"*3)

        B = calc_secao_retang(H, BW, FCK, FYK, COB, COMBINAÇÃO, DMÁX_AGR, ØEST, ØARM, MSD) 
        plotagem_secao_retang(H, BW)
        
    if o == 2:    
        H_BANZO_INF = float(input('h do banzo inferior (cm) = '))
        B_BANZO_INF = float(input('b do banzo inferior (cm) = '))
        H_ALMA = float(input('h da alma (cm) = '))
        B_ALMA = float(input('b da alma (cm) = '))
        
        MISULA_INF = input('Existe mísula infeior?(sim,nao): ') #CONSTANTE para coleta de input de opcao
        if MISULA_INF == ("sim"):        
            H_MISULA_INF = float(input('h da misula inferior (cm) = '))
            B_MISULA_INF = float(input('b da misula inferior (cm) = '))

        if MISULA_INF == ("nao"):
            H_MISULA_INF = 0
            B_MISULA_INF = 0    
        H_BANZO_SUP = float(input('h do banzo superior (cm) = '))
        B_BANZO_SUP = float(input('b do banzo superior (cm) = '))
        MISULA_SUP = input('Existe mísula superior?(sim,nao): ')

        if MISULA_SUP == ("sim"):        
            H_MISULA_SUP = float(input('h da misula superior (cm) = '))
            B_MISULA_SUP = float(input('b da misula superior (cm) = '))
        if MISULA_SUP == ("nao"):
            H_MISULA_SUP = 0
            B_MISULA_SUP = 0
        
        H = float(input('h (cm) = '))
        FCK = float(input("fck (MPa) = "))
        FYK = float(input("fyk (MPa) = "))
        COB = float(input("cobrimento (cm) = "))
        COMBINAÇÃO = int(input("Combinação (NORMAL-1,ESPECIAL/CONSTRUÇÃO-2,EXPEPCIONAL-3 = "))
        DMÁX_AGR = float(input("dim. máx. do agregado (mm) = "))
        ØEST = float(input("Ø estribo (mm) = "))
        ØARM = float(input("Ø armadura long. (mm) = "))
        MSK = float(input("MsK (kNm) = "))
        
        print("\n"*3)
        
        C = calc_secao_i(H,FCK,FYK,COB, COMBINAÇÃO, DMÁX_AGR,ØEST,ØARM,MSK,B_BANZO_INF,H_BANZO_INF,B_BANZO_SUP,H_BANZO_SUP,B_ALMA,H_ALMA,B_MISULA_INF,H_MISULA_INF,B_MISULA_SUP,H_MISULA_SUP)
        print(C)
        C_plot = plotagem_secao_i(H,H_BANZO_INF,B_BANZO_INF,H_ALMA,B_ALMA,MISULA_INF,H_MISULA_INF,B_MISULA_INF,H_BANZO_SUP,B_BANZO_SUP,MISULA_SUP,H_MISULA_SUP,B_MISULA_SUP)