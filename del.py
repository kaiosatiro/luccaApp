import os

def valores_ftool(linhas,n):
  MATRIZ = []
  for i in linhas:

    t = i
    valores = t.split()
    print(i)
    MATRIZ.append(valores)

  MATRIZ.pop(0)
  print("\n")
  print(MATRIZ)
  print("\n")


  DIST = []
  VALORES = []
  for i in range(0,n):

    dist = float(MATRIZ[i][0])
    DIST.append(dist)

    valor = float(MATRIZ[i][1])
    VALORES.append(valor)

  print("\n")
  print(DIST)

  print("\n")
  print(VALORES)

  return DIST, VALORES


# INICIO DO PROGRAMA:


# Criação da pasta da viga:
nova_Viga = input('Deseja criar uma Nova Viga?\nDigite sim ou nao: ')

if nova_Viga == "sim":
  nome_viga = input('Digite o nome da viga: ')

  pasta_alvo = nome_viga
  if (not os.path.exists(pasta_alvo)):
    os.chdir("C:\\Users\\User\\Desktop\\PASTA PROGRAMA LUCCA")
    os.mkdir(pasta_alvo)
    os.chdir(pasta_alvo)


# Abertura do Ftool para modelagem da viga:
abrir_ftool = input('Deseja abrir o Ftool?\nDigite sim ou nao: ')

# ABERTURA DO FTOOL
if abrir_ftool == "sim":
  os.getcwd()
  os.startfile(r"C:\Users\User\Desktop\Ftool.exe")

  instrucoes_ftool = Tk()

  instrucoes_ftool.title("Janela")
  instrucoes_ftool.configure(background='#a0aeb8')
  instrucoes_ftool.geometry("700x200")
  instrucoes_ftool.resizable(False, False)

  label_1 = Label(instrucoes_ftool, text="Instruções para uso do Ftool com o Programa:",bg='#a0aeb8', font=('Times New Roman', 16, ))
  label_1.place(relx=0.2, rely=0.02)

  label_2 = Label(instrucoes_ftool, text="Ao iniciar o ftool e modelar sua viga, é necessário que o arquivo seja salvo para mostrar os gráficos.\n" 
                                          "Salve o arquivo 2x com os nomes de (cortante_viga, momento_viga) na pasta criada, em seguida acesse File\n"
                                          "- Export Line Results - Display Resolution, para ambos os arquivos. Após gerar os arquivos textos, feche\n"
                                          "o Ftool e retorne ao Programa e insira as entradas, por fim executando o dimensionamento da viga\n"
                                          ,bg='#a0aeb8', font=('Times New Roman', 12, ))
  label_2.place(relx=0.01, rely=0.20)

  instrucoes_ftool.mainloop()

elif abrir_ftool == "não":
  print("Como será substituído por um botão, a função if não existirá, consequentemente nem a opção não")
  

# Recepção dos valores de Cortante:
arq_cortante_ftool = open("cortante_viga.txt")
linhas_V = arq_cortante_ftool.readlines()
n_V = int(len(linhas_V)-1)

dist_V, mat_Vsk = valores_ftool(linhas_V,n_V)


# Recepção dos valores de Momento:
arq_momento_ftool = open("momento_viga.txt")
linhas_M = arq_momento_ftool.readlines()
n_M = int(len(linhas_M)-1)

dist_M, mat_Msk = valores_ftool(linhas_M,n_M)