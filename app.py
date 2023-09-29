import pandas as pd
import numpy as np
from datetime import datetime, date
import analise_carteira as analise_carteira


if __name__=='__main__':
    wallet = analise_carteira.AnaliseCarteira()
    
    df_carteira = pd.read_csv("banco_dados/carteira_macro-visao.csv", delimiter=";") # INPUT! COMO? ESTUDANDO...
    df_persona = pd.read_csv("banco_dados/IPS-persona.csv", delimiter=';')
    
    tipo_investimento_para_coluna = {
        'renda fixa pos': 'renda fixa pos',
        'renda fixa hy': 'renda fixa hy',
        'renda fixa pre': 'renda fixa pre',
        'renda fixa inflacao cp': 'renda fixa inflacao cp', # mesmo que renda fixa pos
        'multimercado': 'multimercado', # mesmo que renda variavel
        'imobiliarios': 'imobiliarios', # mesmo que renda variavel
        'renda variavel br': 'renda variavel br',
        'renda fixa global': 'renda fixa global',
        'multimercado global': 'multimercado global',
        'renda variavel global': 'renda variavel global',
        'alternativos': 'alternativos'
    }

    DATA_CARTEIRA = df_carteira.copy()
    for tipo_investimento, coluna in tipo_investimento_para_coluna.items():
        DATA_CARTEIRA[coluna] = DATA_CARTEIRA.apply(lambda row: wallet.porcento_classe(row, tipo_investimento),axis=1)
        
    for tipo_investimento, coluna in tipo_investimento_para_coluna.items():
        DATA_CARTEIRA[coluna] = DATA_CARTEIRA.apply(lambda row: wallet.bandeira_classe(row, df_persona, tipo_investimento),axis=1)

    for tipo_investimento, coluna in tipo_investimento_para_coluna.items():
        DATA_CARTEIRA[coluna] = DATA_CARTEIRA.apply(lambda row: wallet.reais_classe(row, tipo_investimento),axis=1)
    
    CARTEIRA_SUGESTAO = DATA_CARTEIRA.loc[:,'renda fixa pos':'alternativos'].copy()    
    index = CARTEIRA_SUGESTAO.loc[0] # for loop here
    
    ORDENACAO = pd.DataFrame(data=[{k: v for k, v in sorted(index.items(), key=lambda item: item[1])}])
    SUGESTAO_ORDEM, STANDARD = wallet.alinhamento_classe(ORDENACAO)
    