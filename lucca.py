import requests

from tkinter import *

import matplotlib.pyplot as plt

from tkinter import ttk

import sqlite3

import math

import matplotlib.pyplot as plt

import numpy as np



def tipo_secao(a):
    
    if a == 1:
                
        print("seção Retangular (1) ")
                
    if a == 2:
                
        print("seção I (2) ")
            
    return 

def calc_secao_retang(h,bw,fck,fyk,cob,combinação,dmáx_agr,Øest,Øarm,msd):
    

    Ac = h*bw
    
    if fck == 20 or fck == 25 or fck == 30:
        
        Asmín = (Ac*0.15)/100
        
    if fck == 35:
        
        Asmín = (Ac*0.164)/100
        
    if fck == 40:
        
        Asmín = (Ac*0.179)/100
        
    if fck == 45:
        
        Asmín = (Ac*0.194)/100
        
    if fck == 50:
        
        Asmín = (Ac*0.208)/100
        
    if fck == 55:
        
        Asmín = (Ac*0.211)/100
        
    if fck == 60:
        
        Asmín = (Ac*0.219)/100
        
    if fck == 65:
        
        Asmín = (Ac*0.226)/100
        
    if fck == 70:
        
        Asmín = (Ac*0.233)/100
        
    if fck == 75:
        
        Asmín = (Ac*0.239)/100
        
    if fck == 80:
        
        Asmín = (Ac*0.245)/100
        
    if fck == 85:
        
        Asmín = (Ac*0.251)/100
        
    if fck == 90:
        
        Asmín = (Ac*0.256)/100
    
    
    
    
    
    
    if h <= 60:
        
        Aspele_face = 0
        Aspele_tot = 0
        
    if h > 60:
        
        if (0.0005*Ac)*2 <= 5:
            Aspele_face = 0.0005*Ac
            Aspele_tot = (0.0005*Ac)*2 
            
        if (0.0005*Ac)*2 > 5:
             Aspele_face = 5/2
             Aspele_tot = 5
        
    
    d = h-(cob+(Øest/10)+(Øarm/(2*10)))
    dlinha = cob+(Øest/10)+(Øarm/(2*10))
    ecu = 0.0035
    Es = 21000
    Asmáx = Ac*0.04
    
    
    if combinação == 1:
        yc = 1.4
        ys = 1.15
        
    if combinação == 2:
        yc = 1.2
        ys = 1.15
        
    if combinação == 3:
        yc = 1.2
        ys = 1
    
    
    if fck <=50:
        λ = 0.8
        ac = 0.85
        x_d = 0.45
    
    if 50< fck <= 90:
        λ = 0.8-((fck-50)/400)
        ac = 0.85*(1-((fck-50)/200))
        x_d = 0.35
        
    fcd = fck/(10*yc)
    
    fyd = fyk/(10*ys)
    
    Msd = msd*100
    
    
    xlim = x_d*d
    
    x = (d-(((d**2)-(2*(Msd/(ac*fcd*bw))))**(0.5)))/λ
    
    
    
    if x <= xlim:
        
        z = d-(0.5*λ*x)
        
        As = Msd/(z*fyd)
        
        Aslim = 0
        
        Aslinha = 0
        
        σsd = 0
        
        e_s = 0
        
        eyd = 0
        
        ΔM = 0
        
        
        
    if x > xlim:
        
        Msdlim = ac*fcd*bw*((λ*xlim*d)-(((λ**2)*(xlim**2))/2))
        
        z = d-(0.5*λ*xlim)
        
        Aslim = Msdlim/(z*fyd)
        
        ΔM = Msd-Msdlim
        
        e_s = (ecu*(xlim-dlinha))/xlim
        
        eyd = fyd/Es
        
        if e_s > eyd:
            
            σsd = fyd
        
        if e_s <= eyd:
            
            σsd = Es*e_s
            
        Aslinha = ΔM/(σsd*(d-dlinha))
        
        As = Aslim+Aslinha
        
        
    print("h = ", h, "cm")
    print("bw = ", bw, "cm")
    print("fck = ", fck, "MPa")
    print("fyk = ", fyk, "MPa")
    print("cobrimento = ", cob, "cm")

    if combinação ==1:
        print("Combinação Normal")
    if combinação ==2:
        print("Combinação Especial/Construção")
    if combinação ==3:
        print("Combinação Excepcional")

    print("dim. máx. agregado = ", dmáx_agr, "mm")
    print("Ø estribo = ", Øest, "mm")
    print("Ø armadura longitudinal = ", Øarm, "mm")
    print("Msd = ", msd, "kNm")
    print("Área da seção = ", Ac, "cm²")
    print("d = ", d, "cm")
    print("d' = ", dlinha, "cm")
    print("yc = ", yc)
    print("ys = ", ys)
    print("λ = ", λ)
    print("ac = ", ac)
    print("x/d = ", x_d)
    print("fcd = ", fcd, "kN/cm²")
    print("fyd = ", fyd, "kN/cm²")
    print("x = ", x, "cm")
    print("xlim = ", xlim, "cm")
    print("ΔM = ", ΔM/100, "kNm")
    print("z = ", z, "cm")
    print("As = ", As, "cm²")
    print("Aslim = ", Aslim, "cm²")
    print("As' = ", Aslinha, "cm²")
    print("σsd' = ", σsd, "kN/cm²")
    print("Asmáx = ", Asmáx, "cm²")
    print("Asmín = ", Asmín, "cm²")
    print("Aspele total = ", Aspele_tot, "cm²")
    print("Aspele/face = ", Aspele_face, "cm²")
        
          

    
    
    return d,As,Aslinha

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

    plt.figure(figsize=(bw/20,h/20),dpi=300)
    plt.axis('off')

    plt.ylim(0, h)
    plt.xlim(0, bw)

    plt.plot(x1,y1, "black",)
    plt.plot(x2,y2, "black")
    plt.plot(x3,y3, "black")
    plt.plot(x4,y4, "black")
    
    plt.fill_between(x,0,h,alpha=0.5,color='grey')
    

    plt.show()
    
    return

def calc_secao_i(h,fck,fyk,cob, combinação, dmáx_agr,Øest,Øarm,Msk,b_banzo_inf,h_banzo_inf,b_banzo_sup,h_banzo_sup,b_alma,h_alma,b_misula_inf,h_misula_inf,b_misula_sup,h_misula_sup):


    Ac = (b_banzo_inf*h_banzo_inf)+(b_banzo_sup*h_banzo_sup)+(b_alma*h_alma)+(2*(b_misula_inf*h_misula_inf)/2)+(2*(b_misula_sup*h_misula_sup)/2)+(h_misula_inf*b_alma)+(h_misula_sup*b_alma)

    if fck == 20 or fck == 25 or fck == 30:
        
        Asmín = (Ac*0.15)/100
        
    if fck == 35:
        
        Asmín = (Ac*0.164)/100
        
    if fck == 40:
        
        Asmín = (Ac*0.179)/100
        
    if fck == 45:
        
        Asmín = (Ac*0.194)/100
        
    if fck == 50:
        
        Asmín = (Ac*0.208)/100
        
    if fck == 55:
        
        Asmín = (Ac*0.211)/100
        
    if fck == 60:
        
        Asmín = (Ac*0.219)/100
        
    if fck == 65:
        
        Asmín = (Ac*0.226)/100
        
    if fck == 70:
        
        Asmín = (Ac*0.233)/100
        
    if fck == 75:
        
        Asmín = (Ac*0.239)/100
        
    if fck == 80:
        
        Asmín = (Ac*0.245)/100
        
    if fck == 85:
        
        Asmín = (Ac*0.251)/100
        
    if fck == 90:
        
        Asmín = (Ac*0.256)/100
    
    
    
    if h <= 60:
        
        Aspele_face = 0
        Aspele_tot = 0
        
    if h > 60:
        
        if 0.0005*Ac*2 <= 5:
            Aspele_tot = (0.0005*Ac)*2
            Aspele_face = 0.0005*Ac
        if 0.0005*Ac*2 > 5:
            Aspele_tot = 5
            Aspele_face = 5/2
            
    Asmáx = Ac*0.04
    

    if combinação == 1:
        yc = 1.4
        ys = 1.15
        
    if combinação == 2:
        yc = 1.2
        ys = 1.15
        
    if combinação == 3:
        yc = 1.2
        ys = 1
    
    
    if fck <=50:
        λ = 0.8
        ac = 0.85
        x_d = 0.45
    
    if 50< fck <= 90:
        λ = 0.8-((fck-50)/400)
        ac = 0.85*(1-((fck-50)/200))
        x_d = 0.35
        
    
    fcd = fck/(10*yc)
    
    fyd = fyk/(10*ys)
    
    d = h-(cob+(Øest/10)+(Øarm/(2*10)))
    
    dlinha = cob+(Øest/10)+(Øarm/(2*10))
    ecu = 0.0035
    Es = 21000
    
    
    
    xlim = x_d*d
    
    
    x = float
    Msd = float
    
       
    
    if 0<=xlim<=35:
        bw = 40
    
    if 35<xlim<=47.5:
        x_auxiliar = xlim-35
        bw = (-2*x_auxiliar)+40
           
    if 47.5<xlim<=85:
        bw = 15
    
    if 85<xlim<=100:
        bw = 40
    
    Q = fcd*λ*ac
    
    Rc = bw*xlim*Q
    
    z = d-(0.5*xlim*λ)
    
    Msd = (Rc*z)
       
    
    if Msd/100 <= Msk:
        
        As = Msd/(z*fyd)
        
        Aslim = 0
        
        Aslinha = 0
        
        ΔM = 0
        
        σsd = 0
        
        e_s = 0
        
        eyd = 0
    
    
    if Msk > Msd/100:
       
        Aslim = Msd/(z*fyd)
        
        ΔM = 100*Msk-Msd
        
        e_s = (ecu*(xlim-dlinha))/xlim
        
        eyd = fyd/Es
        
        if e_s > eyd:
            
            σsd = fyd
        
        if e_s <= eyd:
            
            σsd = Es*e_s
            
        Aslinha = ΔM/(σsd*(d-dlinha))
        
        As = Aslim+Aslinha
    
    print("\n\n\n")
    print("h = ", h, "cm")
    print("bw = ", bw, "cm")
    print("fck = ", fck, "MPa")
    print("fyk = ", fyk, "MPa")
    print("cobrimento = ", cob, "cm")

    if combinação ==1:
        print("Combinação Normal")
    if combinação ==2:
        print("Combinação Especial/Construção")
    if combinação ==3:
        print("Combinação Excepcional")

    print("dim. máx. agregado = ", dmáx_agr, "mm")
    print("Ø estribo = ", Øest, "mm")
    print("Ø armadura longitudinal = ", Øarm, "mm")
    print("Ac = ", Ac, "cm²")
    print("Msk = ", Msk, "kNm")
    print("Msd = ", Msd, "kNm")
    print("Área da seção = ", Ac, "cm²")
    print("d = ", d, "cm")
    print("d' = ", dlinha, "cm")
    print("yc = ", yc)
    print("ys = ", ys)
    print("λ = ", λ)
    print("ac = ", ac)
    print("x/d = ", x_d)
    print("fcd = ", fcd, "kN/cm²")
    print("fyd = ", fyd, "kN/cm²")
    print("xlim = ", xlim, "cm")
    print("ΔM = ", ΔM/100, "kNm")
    print("z = ", z, "cm")
    print("As = ", As, "cm²")
    print("Aslim = ", Aslim, "cm²")
    print("As' = ", Aslinha, "cm²")
    print("σsd' = ", σsd, "kN/cm²")
    print("Asmáx = ", Asmáx, "cm²")
    print("Asmín = ", Asmín, "cm²")
    print("Aspele total = ", Aspele_face*2, "cm²")
    print("Aspele/face = ", Aspele_face, "cm²")
    
    return As and Aslinha 
 
def plotagem_secao_i(h,h_banzo_inf,b_banzo_inf,h_alma,b_alma,misula_inf,h_misula_inf,b_misula_inf,h_banzo_sup,b_banzo_sup,misula_sup,h_misula_sup,b_misula_sup):
    
    
    plt.figure(dpi=300)
    
    x1 = [0,b_banzo_inf]
    y1 = [0,0]

    x2 = [0,0]
    y2 = [0,h_banzo_inf]

    x3 = [b_banzo_inf,b_banzo_inf]
    y3 = [0,h_banzo_inf]


    if misula_inf ==("não"):
        
        x4 = [0,(b_banzo_inf-b_alma)/2]
        y4 = [h_banzo_inf,h_banzo_inf]
            
        x5 = [b_banzo_inf,b_banzo_inf-((b_banzo_inf-b_alma)/2)]
        y5 = [h_banzo_inf,h_banzo_inf]
        
        h_1 = h_banzo_inf
        b_1_dir = (b_banzo_inf-b_alma)/2
        b_1_esq = b_banzo_inf-((b_banzo_inf-b_alma)/2)

    if misula_inf ==("sim"):
        
        x4 = [0,b_misula_inf]
        y4 = [h_banzo_inf,h_banzo_inf+h_misula_inf]
            
        x5 = [b_banzo_inf,b_banzo_inf-b_misula_inf]
        y5 = [h_banzo_inf,h_banzo_inf+h_misula_inf]
        
        h_1 = h_banzo_inf+h_misula_inf
        b_1_dir = b_misula_inf
        b_1_esq = b_banzo_inf-b_misula_inf


    x6 = [b_1_dir,b_1_dir]
    y6 = [h_1,h_1+h_alma]

    x7 = [b_1_esq,b_1_esq]
    y7 = [h_1,h_1+h_alma]

    h_2 = h_1+h_alma



    if misula_sup ==("não"):

        x8 = [b_1_dir,b_1_dir-((b_banzo_sup-b_alma)/2)]
        y8 = [h_2,h_2]

        x9 = [b_1_esq,b_1_esq+(b_banzo_sup-((b_banzo_sup-b_alma)/2))]
        y9 = [h_2,h_2]

        h_3 = h_2
        b_2_dir = b_1_dir-((b_banzo_sup-b_alma)/2)
        b_2_esq = b_1_esq+(b_banzo_sup-((b_banzo_sup-b_alma)/2))
        
    if misula_sup ==("sim"):

        x8 = [b_1_dir,b_1_dir-b_misula_sup]
        y8 = [h_2,h_2+h_misula_sup]

        x9 = [b_1_esq,b_1_esq+b_misula_sup]
        y9 = [h_2,h_2+h_misula_sup]
        
        h_3 = h_2+h_misula_sup
        b_2_dir = b_1_dir-b_misula_sup
        b_2_esq = b_1_esq+b_misula_sup

    x10 = [b_2_dir,b_2_dir]
    y10 = [h_3,h_3+h_banzo_sup]

    x11 = [b_2_esq,b_2_esq]
    y11 = [h_3,h_3+h_banzo_sup]

    x12 = [b_2_dir, b_banzo_sup]
    y12 = [h_3+h_banzo_sup, h_3+h_banzo_sup]


    if b_banzo_inf >= b_banzo_sup:
        bw = b_banzo_inf
    
    if b_banzo_inf < b_banzo_sup:
        bw = b_banzo_sup
        
    plt.figure(figsize=(bw/20,h/20),dpi=300)
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
    
    return
    


def n_arm_e_espaçamento(d,bw,As,Aslinha,cob,Øest,Øarm,dmáx_agr):
    
    ah = float(0)
    av = float(0)
    


    n_tot = As/(np.pi*((Øarm/(10*2))**2))

    n_tot = float(round(n_tot+0.5))

    fator1 = 20/10
    fator2 = Øarm/10
    fator3 = (dmáx_agr*1.2)/10
    fator4 = (dmáx_agr*0.5)/10


    if fator1>=fator2 and fator1>=fator3:
        
        ah = fator1
        
    if fator2>=fator1 and fator2>=fator3:
        
        ah = fator2
        
    if fator3>=fator1 and fator3>=fator2:
        
        ah = fator3
        
        


    if fator1>=fator2 and fator1>=fator4:
        
        av = fator1
        
    if fator2>=fator1 and fator2>=fator4:
        
        av = fator2
        
    if fator4>=fator1 and fator4>=fator2:
        
        av = fator4




    n_linha = float((bw-(2*(Øest/10))-2*cob+ah)/(ah+(Øarm/10)))

    n_linha = float(round(n_linha-0.5))

    ah_d = (bw-(2*(Øest/10))-(2*cob)-(n_linha*(Øarm/10)))/(n_linha-1)

    n_camadas = n_tot/n_linha

    n_camadas = float(round(n_camadas+0.5))
        
    if n_linha*n_camadas == n_tot:
        
        n_ult_camada = 0
        
    if n_linha*n_camadas != n_tot:
        
        n_ult_camada = n_tot-(n_linha*(n_camadas-1))
        

    # SEQUENCIA DE IF PARA NUMERO DE CAMADAS ATÉ 10:

        
    dist = (Øarm/(2*10)) + av + (Øarm/(2*10))
                                
    if n_camadas == 1:
        
        t = 0
        
    if n_camadas == 2:
        
        t = ((n_linha*0)+(n_ult_camada*dist))/n_tot
        
    if n_camadas == 3:
        
        t = ((n_linha*0)+(n_linha*dist)+(n_linha*dist*2))/n_tot
        
    if n_camadas == 4:
        
        t = ((n_linha*0)+(n_linha*dist)+(n_linha*dist*2)+(n_ult_camada*dist*3))/n_tot
        
    if n_camadas == 5:
        
        t = ((n_linha*0)+(n_linha*dist)+(n_linha*dist*2)+(n_linha*dist*3)+(n_ult_camada*dist*4))/n_tot
        
    if n_camadas == 6:
        
        t = ((n_linha*0)+(n_linha*dist)+(n_linha*dist*2)+(n_linha*dist*3)+(n_linha*dist*4)+(n_ult_camada*dist*5))/n_tot
        
    if n_camadas == 7:
        
        t = ((n_linha*0)+(n_linha*dist)+(n_linha*dist*2)+(n_linha*dist*3)+(n_linha*dist*4)+(n_linha*dist*5)+(n_ult_camada*dist*6))/n_tot
       
    if n_camadas == 8:
        
        t = ((n_linha*0)+(n_linha*dist)+(n_linha*dist*2)+(n_linha*dist*3)+(n_linha*dist*4)+(n_linha*dist*5)+(n_linha*dist*6)+(n_ult_camada*dist*7))/n_tot
       
    if n_camadas == 9:
        
        t = ((n_linha*0)+(n_linha*dist)+(n_linha*dist*2)+(n_linha*dist*3)+(n_linha*dist*4)+(n_linha*dist*5)+(n_linha*dist*6)+(n_linha*dist*7)+(n_ult_camada*dist*8))/n_tot
       
    if n_camadas == 10:
        
        t = ((n_linha*0)+(n_linha*dist)+(n_linha*dist*2)+(n_linha*dist*3)+(n_linha*dist*4)+(n_linha*dist*5)+(n_linha*dist*6)+(n_linha*dist*7)+(n_linha*dist*8)(n_ult_camada*dist*9))/n_tot
       
    if n_camadas >= 11:
        
        print("NÚMERO DE CAMADAS NÃO EXISTENTE NO BANCO DE DADOS - REVISAR CÓDIGO")


    d = d-t

    print("n barras total = ",n_tot)    
    print("Fator 1 = ",fator1,"cm")
    print("Fator 2 = ",fator2,"cm")
    print("Fator 3 = ",fator3,"cm")
    # print("ah = ",ah)
    print("ah = ",ah_d,"cm")
    print("nmáx de barras na linha = ",n_linha,)
    print("n de camadas = ",n_camadas)
    print("n na última camada = ",n_ult_camada)
    print("dist = ",dist)
    print("cg novo = ", t)
    print("d = ", d)

    return (d,t)
        
    
    
    
    
    




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
    
#         return None
       
      











print("SELECIONE O TIPO DE SEÇÃO TRANSVERSAL \n")


a = int(input('tipo de seção (retangular - 1, viga I - 2): '))

A = tipo_secao(a)
print(A)



if a == 1:
      
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
    
    print("\n")
    print("\n")
    print("\n")


    B = calc_secao_retang(H,BW,FCK,FYK,COB,COMBINAÇÃO,DMÁX_AGR,ØEST,ØARM,MSD)
    print(B)
    
    vrau = B*2
    print(vrau)
    
    B_plot = plotagem_secao_retang(H,BW)
    print(B_plot)
    
    
if a == 2:
    
    H_BANZO_INF = float(input('h do banzo inferior (cm) = '))
    B_BANZO_INF = float(input('b do banzo inferior (cm) = '))
    H_ALMA = float(input('h da alma (cm) = '))
    B_ALMA = float(input('b da alma (cm) = '))
    MISULA_INF = input('Existe mísula infeior?(sim,não): ')
    if MISULA_INF ==("sim"):
        
        H_MISULA_INF = float(input('h da misula inferior (cm) = '))
        B_MISULA_INF = float(input('b da misula inferior (cm) = '))
    if MISULA_INF ==("não"):
        H_MISULA_INF = 0
        B_MISULA_INF = 0
    
    H_BANZO_SUP = float(input('h do banzo superior (cm) = '))
    B_BANZO_SUP = float(input('b do banzo superior (cm) = '))
    MISULA_SUP = input('Existe mísula superior?(sim,não): ')
    if MISULA_SUP ==("sim"):
        
        H_MISULA_SUP = float(input('h da misula superior (cm) = '))
        B_MISULA_SUP = float(input('b da misula superior (cm) = '))
    if MISULA_SUP ==("não"):
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
    
    print("\n")
    print("\n")
    print("\n")
    
    C = calc_secao_i(H,FCK,FYK,COB, COMBINAÇÃO, DMÁX_AGR,ØEST,ØARM,MSK,B_BANZO_INF,H_BANZO_INF,B_BANZO_SUP,H_BANZO_SUP,B_ALMA,H_ALMA,B_MISULA_INF,H_MISULA_INF,B_MISULA_SUP,H_MISULA_SUP)
    print(C)
    
    C_plot = plotagem_secao_i(H,H_BANZO_INF,B_BANZO_INF,H_ALMA,B_ALMA,MISULA_INF,H_MISULA_INF,B_MISULA_INF,H_BANZO_SUP,B_BANZO_SUP,MISULA_SUP,H_MISULA_SUP,B_MISULA_SUP)
    print(C_plot)