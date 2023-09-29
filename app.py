import pandas as pd
import numpy as np
import json
from datetime import datetime, date
import analise_carteira as analise_carteira


if __name__=='__main__':
    wallet = analise_carteira.AnaliseCarteira()
    
    df_carteira = pd.read_csv("banco_dados/carteira_macro-visao.csv", delimiter=";").set_index('id') # INPUT! COMO? ESTUDANDO...
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

    DATA_PORCENTO = df_carteira.copy()
    for tipo_investimento, coluna in tipo_investimento_para_coluna.items():
        DATA_PORCENTO[coluna] = DATA_PORCENTO.apply(lambda row: wallet.porcento_classe(row, tipo_investimento),axis=1)
    
    DATA_BANDEIRA = DATA_PORCENTO.copy()
    for tipo_investimento, coluna in tipo_investimento_para_coluna.items(): # sinalizar se está saudavel ou nao // salvar tudo! como json
        DATA_BANDEIRA[coluna] = DATA_BANDEIRA.apply(lambda row: wallet.bandeira_classe(row, df_persona, tipo_investimento),axis=1)

    DATA_BANDEIRA['status_saude'] = DATA_BANDEIRA.loc[:, 'renda fixa pos':'alternativos'].apply(wallet.saude_investimentos, axis=1)
    DATA_BANDEIRA[['id','perfil','renda fixa pos','renda fixa hy','renda fixa pre','renda fixa inflacao cp','multimercado','imobiliarios',
	  'renda variavel br','renda fixa global','multimercado global','renda variavel global','alternativos','status_saude','pl']]

    # salvar antes de continuar
    DATA_BANDEIRA.to_json("banco_dados/carteira_tabela_1.json", orient="table")
    
    DATA_REAL = DATA_BANDEIRA.copy()
    for tipo_investimento, coluna in tipo_investimento_para_coluna.items():
        DATA_REAL[coluna] = DATA_REAL.apply(lambda row: wallet.reais_classe(row, tipo_investimento),axis=1)
    
    CARTEIRA_SUGESTAO = DATA_REAL.loc[:,'renda fixa pos':'alternativos'].copy()    
    
    index = CARTEIRA_SUGESTAO.loc[0] # for loop here
    
    ORDENACAO = pd.DataFrame(data=[{k: v for k, v in sorted(index.items(), key=lambda item: item[1])}])
    SUGESTAO_ORDEM, STANDARD = wallet.alinhamento_classe(ORDENACAO)
    
    # salvando as outras duas tabelas
    SUGESTAO_ORDEM.to_json('banco_dados/carteira_tabela_2.json', orient="table")
    STANDARD.to_json('banco_dados/carteira_tabela_3.json', orient="table")
    
    # SALVANDO O DADOS CARTEIRA COMO JSON TBM
    df_carteira.to_json('banco_dados/data-original_carteira.json', orient="table")
    
    