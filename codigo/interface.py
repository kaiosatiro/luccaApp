import customtkinter as ctk


# ctk.set_appearance_mode("light")
class App(ctk.CTk):
    def __init__(self, entradas:dict):
        super().__init__()
        
        #DEFINICAO DO GRID
        self.title('luccaApp')
        self.geometry('1200x600')
        self.grid_columnconfigure((0, 1), weight=0)
        self.grid_columnconfigure(2, weight=0)
        self.grid_columnconfigure(3, weight=2)
        self.grid_rowconfigure((0, 2), weight=0)
        self.grid_rowconfigure(1, weight=4)

        #FRAMES SECUNDARIOS
        self.entradas = FrameEntrada(self, entradas)
        self.entradas.grid(row=0, column=2, pady=10, padx=(10, 0), sticky='ewsn', rowspan=3)

        self.title_Saida = ctk.CTkLabel(self, text='Saidas', font=('', 16, 'bold'))
        self.title_Saida.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='w')
        self.saida = FrameSaida(self)
        self.saida.grid(row=1, column=0, pady=5, padx=(10, 0), sticky='ewsn', rowspan=1, columnspan=2)

        self.title_Plot = ctk.CTkLabel(self, text='Plotagem', font=('', 16, 'bold'))
        self.title_Plot.grid(row=0, column=3, padx=10, pady=(10, 0), sticky='e')
        self.plotagem = FramePlotagem(self)
        self.plotagem.grid(row=1, column=3, pady=10, padx=10, sticky='ewsn', rowspan=3)

        #BOTOES DO FRAME PRINCIPAL(WINDOW)
        self.bt_Plotar = ctk.CTkButton(self, text='Plotar', fg_color='red')
        self.bt_Plotar.grid(row=2, column=1, pady=(20,30), padx=(10, 0), sticky='ew')        
        self.bt_Salvar = ctk.CTkButton(self, text='Salvar', fg_color='green')
        self.bt_Salvar.grid(row=2, column=0, pady=(20,30), padx=(10, 0), sticky='ew')


#FRAME DOS DADOS DE ENTRADA
class FrameEntrada(ctk.CTkFrame):
    def __init__(self, master, entradas:dict):
        super().__init__(master)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.title = ctk.CTkLabel(self, text='Entradas', fg_color='gray20', corner_radius=6, font=('', 16, 'bold'))
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='ewn', columnspan=3)

        #VARIAVEIS
        self.entradas_recebidas = entradas
        self.entradas_criadas = {}
        self.radios_criados = []
        self.tipo = ctk.StringVar(value='')
        self.combinacao = ctk.StringVar(value='1') # NORMAL-1, ESPECIAL/CONSTRUÇÃO-2, EXPEPCIONAL-3
       

        #CAIXAS DE ENTRADAS E ETIQUETAS
        ent_set = []
        for i in self.entradas_recebidas.values():
            ent_set.extend(i)

        for i, value in enumerate(ent_set):
            entry = ctk.CTkEntry(
                self, 
                textvariable=ctk.StringVar(name=f'PY_{value}', value='0'),
                corner_radius=6
            )
            label = ctk.CTkLabel(
                self, text=value,
                font=('', 12, 'bold'),
                fg_color='#1f538d',
                corner_radius=6
            )
            entry.grid(row=i+5, column=1 ,padx=5, pady=5, sticky='ew', columnspan=2)
            label.grid(row=i+5, column=0 ,padx=5, pady=5, sticky='ew')
            
            self.entradas_criadas[value] = {
                'label': label,
                'entry': entry
            }

        #BOTAO RADIO TIPO DE VIGA
        self.radio_Label = ctk.CTkLabel(self, text='Tipo de viga', font=('', 14, 'bold'))
        self.radio_Label.grid(row=1, column=0, padx=10, pady=(10, 0), sticky='ew', columnspan=3)

        for i, value in enumerate(self.entradas_recebidas):
            if i == 0:
                continue
            radio = ctk.CTkRadioButton(self, text=value, value=value, variable=self.tipo, command=self._radio_callback)
            radio.grid(row=2, column=i-1 ,padx=10, pady=(10, 0), columnspan=2)
            self.radios_criados.append(radio)
            self.tipo.set(value)
            self._radio_callback() 

        #BOTAO RADIO TIPO COMBINACAO
        self.radio_Label = ctk.CTkLabel(self, text='Combinação', font=('', 12, 'bold'))
        self.radio_Label.grid(row=3, column=0, padx=5, pady=5, sticky='ew', columnspan=3)

        self.comb_Normal = ctk.CTkRadioButton(self, text='Normal', value='1', variable=self.combinacao)
        self.comb_Normal.grid(row=4, column=0 ,padx=5, pady=5)
        self.comb_Especial = ctk.CTkRadioButton(self, text='Especial', value='2', variable=self.combinacao)
        self.comb_Especial.grid(row=4, column=1 ,padx=5, pady=5)
        self.comb_Expecional = ctk.CTkRadioButton(self, text='Expecional', value='3', variable=self.combinacao)
        self.comb_Expecional.grid(row=4, column=2 ,padx=5, pady=5)
        
    def _radio_callback(self):
        tipo = self.tipo.get()
        for i, value in enumerate(self.entradas_recebidas):
            if i == 0:
                continue
            if value == tipo:
                for e in self.entradas_recebidas[value]:
                    self.entradas_criadas[e]['label'].configure(fg_color='#1f538d')
                    self.entradas_criadas[e]['entry'].configure(state='normal')
            else:
                for e in self.entradas_recebidas[value]:
                    self.entradas_criadas[e]['label'].configure(fg_color='gray40')
                    self.entradas_criadas[e]['entry'].configure(state='disable')
           
    def get_entradas(self):
        dic = {}
        dic['combinacao'] = self.combinacao.get()
        for k, v in self.entradas_criadas.items():
            valor = v['entry'].get()
            dic[k] = valor
        return dic
        

class FrameSaida(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        #CONSTRUCAO DA CAIXA DE TEXTO DE SAIDA
        self.cx_Txt = ctk.CTkTextbox(self, corner_radius=3, font=('', 16, 'bold'))
        self.cx_Txt.grid(row=0, column=0, sticky="nsew")
        self.cx_Txt.insert('0.0', '...')

    
    def recebe_texto(self, texto:str):
        self.cx_Txt.delete('0.0', 'end')
        self.cx_Txt.insert('0.0', texto)
        self.cx_Txt.configure(font=('', 12, 'bold'))


class FramePlotagem(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)


if __name__ == '__main__':
    entradas_para_criar = {
    'comum': ['H', 'FCK', 'FYK', 'Cobrimento', 'DmaxAgreg', 'Armadura', 'MSD'],
    'Retangular': ['BW', 'MSK'],
    'I': ['MSD']
}
    app = App(entradas_para_criar)
    app.mainloop()