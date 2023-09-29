import pandas as pd
import numpy as np
from datetime import datetime, date

df_carteira = pd.read_csv("/content/drive/MyDrive/base/04_09_2023_carteira.csv", delimiter=";")

class AnaliseCarteira:
    def calcular_porcento_investimentos(row, tipo_investimento):
        # Transformando os numeros em porcento
        return round(row[tipo_investimento] / row['pl'], 2)


    def calcular_diferenca_investimentos(row, persona, tipo_investimento):
        return round(row[tipo_investimento] - persona[persona['ips'] == tipo_investimento][row['perfil']], 2)


    def calcular_reais_investimentos(row, tipo_investimento):
        # Transformando os numeros em porcento
        return round(row[tipo_investimento] * row['pl'], 2)


    def sugestao(ordenado):
        valores = {'ativo':[], 'realocar':[], 'valor_estimado':[]}

        for col in range(len(ordenado.columns)):
            valor = ordenado.iloc[0, col]

            while valor < 0:
                for i in range(col + 1, len(ordenado.columns)):
                    proximo_ativo = ordenado.columns[i]
                    proximo = ordenado.iloc[0, i]

                    if proximo > 0:
                        sobra = valor + proximo
                        valores['ativo'].append(ordenado.columns[col])
                        valores['realocar'].append(proximo_ativo)
                        valores['valor_estimado'].append(proximo if sobra < 0 else abs(valor))
                        valor = 0 if sobra > 0 else sobra
                        ordenado.iloc[0, i] = sobra if sobra > 0 else 0
                    else:
                        pass
                else:
                    break

        return pd.DataFrame(data=valores), abs(ordenado)


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