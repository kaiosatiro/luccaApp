import matplotlib.pyplot as plt
import numpy as np


ECU = 0.0035
ES = 21000
DIC = {
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
COMBINACAO = {
            1: {'yc': 1.4, 'ys': 1.15},
            2: {'yc': 1.2, 'ys': 1.15},
            3: {'yc': 1.2, 'ys': 1}
        }



#CADA TIPO DE VIGA SERA UMA CLASSE
class CalculoRetangular:
    def __init__(
            self, h:float, 
            bw:float, fck:float, 
            fyk:float, cobrimento:float, 
            combinacao:int, 
            dmax_agreg:float, est:float, 
            arm:float, msd:float
    ):
        #INICIAMOS O OBJETO JA RECEBENDO OS DADOS DE ENTRADA
        self.h = h
        self.bw = bw
        self.fck = fck
        self.fyk = fyk
        self.cobrimento = cobrimento
        self.combinacao = combinacao
        self.dmax_agreg = dmax_agreg
        self.Øest = est
        self.Øarm = arm
        self.msd = msd

        #E TAMBEM INICIAMOS O OBJETO JA COM VARIAVEIS PARA ARMAZENAR O RESULTADO DOS CALCULOS
        self._AC = float
        self._asmin = float
        self._aspele_face = float
        self._aspele_tot = float
        self._asmax = float
        self._yc = float
        self._ys = float
        self._λ = float
        self._ac = float
        self._x_d = float
        self._fcd = float
        self._fyd = float
        self._d = float
        self._dlinha = float
        self._xlim = float
        self._x = float
        self._MSD = float
        self._z = float
        self._σsd = float
        self._ΔM = float
        self._aslim = float
        self._aslinha = float
        self._as_ = float

    
    def _area_de_Concreto(self):
        """ac = (h *bw)"""
        self._AC = self.h *self.bw
        
    def _asmin_Func(self):
        self._asmin = (self._AC *DIC[self.fck]) / 100

    def _aspele(self):
        """Retorna CÁLCULO DA ÁREA DE ARMADURA DE PELE 
            (aspele_face, aspele_tot)
        """
        if self.h <= 60:
            self._aspele_face, self._aspele_tot =  0,0
        elif self.h > 60:
            i = (0.0005 *self._AC) *2
            if i <= 5:
                self._aspele_face = 0.0005 *self._AC
                self._aspele_tot = i         
            elif i > 5:
                self._aspele_face = 5 /2
                self._aspele_tot = 5    

    def _as_Max(self):
        """Retorna (Ac * 0.04)"""
        self._asmax = self._AC *0.04

    def _ycys(self):
        """Retorna (yc, ys)
        """
        self._yc = COMBINACAO[self.combinacao]['yc']
        self._ys = COMBINACAO[self.combinacao]['ys']

    def _par_fck(self):
        """Retorna PARÂMETROS PELO FCK (λ, ac, x_d)
        """
        if self.fck <= 50:
            self._λ = 0.8
            self._ac = 0.85           
            self._x_d = 0.45
        elif 50 < self.fck <= 90:
            self._λ = 0.8 -((self.fck -50) /400)
            self._ac = 0.85 *(1 -((self.fck -50) /200))        
            self._x_d = 0.35

    def _calc_fcd(self):
            """Retorna CÁLCULO fcd  (fck /(10 *yc))
            """
            self._fcd = self.fck /(10 *self._yc)

    def _calc_fyd(self):
            """Retorna CÁLCULO fyd (fyk /(10 *ys))
            """
            self._fyd = self.fyk /(10 *self._ys)
    
    def _dFuncao(self):
        """retorna o d | Equacao: h -(cob +(Øest /10) +(Øarm /(2 *10)))
        """
        self._d = self.h -(self.cobrimento +(self.Øest /10) +(self.Øarm /(2 *10)))
    
    def _dLinha(self):
        """retorna o dlinha | Equacao: cob +(Øest /10) +(Øarm /(2 *10))
        """
        self._dlinha = self.cobrimento +(self.Øest /10) +(self.Øarm /(2 *10))          
      
    def _calc_xlim(self):
        """Retorna CÁLCULO X LIMITE (x_d *d)"""
        self._xlim = self._x_d *self._d

    def _calc_x(self):
        """Retorna o Calculo X ((d -(((d **2) -(2 *(Msd /(ac *fcd *bw)))) **(0.5))) /λ)"""
        self._x =  (self._d -(((self._d **2) -(2 *(self.msd /(self._ac *self._fcd *self.bw)))) **(0.5))) /self._λ

    def _msdZFuncao(self):
        """Retorna (Msd, z) de acordo com o tipo de secao. O primeiro argumento determina a secao 'ret' ou 'I'. 
        O seguintes argumento são qualquer passados como dicionario"""
        self._MSD = self.msd *100
    
    def _funcaoDiversos(self):
        ''' Retorna  de acordo com a secao:
            'ret' ENTRA (x, xlim, λ, Msd, fyd, d, dlinha, ac, fcd, bw) RETORNA (z, σsd, ΔM, Aslim, Aslinha, As)
        '''
        if self._x <= self._xlim:
            self._z = self._d -(0.5 *self._λ *self._x)
            e_s, self._σsd, self._ΔM, self._aslim, self._aslinha = 0,0,0,0,0
            self._as_ = self._MSD /(self._z *self._fyd)

        elif self._x > self._xlim:
            eyd = self._fyd /ES
            self._z = self._d -(0.5 *self._λ *self._xlim)
            e_s = (ECU *(self._xlim -self._dlinha)) /self._xlim

            if e_s > eyd:
                self._σsd = self._fyd
            elif e_s <= eyd:
                self._σsd = ES *e_s

            _msdlim = self._ac *self._fcd *self.bw *((self._λ *self._xlim *self._d) -(((self._λ **2) *(self._xlim **2)) /2))
            self._ΔM = self._MSD -_msdlim        
            self._aslim = _msdlim /(self._z *self._fyd)
            self._aslinha = self._ΔM /(self._σsd *(self._d -self._dlinha))
            self._as_ = self._aslim +self._aslinha


#- FUNCAO QUE CHAMA TODOS OS CALCULOS -----------------------------------------
    def calc_secao_retang(self):
        self._area_de_Concreto()
        self._asmin_Func()       
        self._aspele()
        self._as_Max()

        self._ycys()

        self._par_fck()

        self._calc_fcd()
        self._calc_fyd()

        self._dFuncao()
        self._dLinha()    
        
        self._calc_xlim()
        self._calc_x()

        self._msdZFuncao()
        
        self._funcaoDiversos()

    def __str__(self):
        if self.combinacao == 1:
            comb = "Combinação Normal"
        elif self.combinacao == 2:
            comb = "Combinação Especial/Construção"
        elif self.combinacao == 3:
            comb = "Combinação Excepcional"
        return f"""
--------------------------
h...........{self.h} cm
bw..........{self.bw} cm
fck.........{self.fck} MPa
fyk.........{self.fyk} MPa
comprimento.{self.cobrimento} cm
--------------------------
{comb}
--------------------------
dim. máx. agregado......{self.dmax_agreg} mm
Ø estribo...............{self.Øest} mm
Ø armadura longitudinal.{self.Øarm} mm
Msd.....................{self._MSD} kNm
Área da seção...........{self._ac} cm²
d.......................{self._d} cm
d'......................{self._dlinha} cm
yc......................{self._yc}
ys......................{self._ys}
λ.......................{self._λ}
ac......................{self._ac}
x/d.....................{self._x_d}
fcd.....................{self._fcd} kN/cm²
fyd.....................{self._fyd} kN/cm²
x.......................{self._x} cm
xlim....................{self._xlim} cm
ΔM......................{self._ΔM/100} kNm
z.......................{self._z} cm
As......................{self._as_} cm²
slim....................{self._aslim} cm²
As'.....................{self._aslinha} cm²
σsd'....................{self._σsd} kN/cm²
Asmáx...................{self._asmax} cm²
Asmín...................{self._asmin} cm²
Aspele total............{self._aspele_tot} cm²
Aspele/face.............{self._aspele_face} cm²

"""

#--------------------------------------------------------------------------------------- PLOTAGEM RETANGULAR ----------------------------------------------
# def plotagem_secao_retang(h,bw):
#     x1 = [0,bw]
#     y1 = [0,0]

#     x2 = [0,0]
#     y2 = [0,h]

#     x3 = [bw,bw]
#     y3 = [0,h]

#     x4 = [0,bw]
#     y4 = [h,h]

#     x = (0,bw,1000)

#     plt.figure(figsize=(bw /20,h /20), dpi=300)
#     plt.axis('off')

#     plt.ylim(0, h)
#     plt.xlim(0, bw)

#     plt.plot(x1,y1, "black",)
#     plt.plot(x2,y2, "black")
#     plt.plot(x3,y3, "black")
#     plt.plot(x4,y4, "black")
    
#     plt.fill_between(x, 0, h, alpha=0.5, color='grey')
#     plt.show()



if __name__ == '__main__':
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
    objetoCalculoRet.calc_secao_retang()
    print(objetoCalculoRet)