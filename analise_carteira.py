import pandas as pd
import numpy as np
from datetime import datetime, date

class AnaliseCarteira:
    """
        Macrovisão: Analisando carteiras e estimando a diferença entre o perfil
            - Levantar a diferença entre a carteira e o perfil de acordo com os threshold do perfil escolhido.
            - Sinalizar em porcento entre -100% e +100% o valor esperado para cada perfil.
            - Sinalizar em moeda corrente o valor em diferença.
            
        Metodo:
            - porcento_classe: Transforma os valores em proporcoes equivalentes ao patrimonio liquido total
            - bandeira_classe: Enquadra a carteira no perfil designado e sinaliza onde está fora do padrao
            - reais_classe: Informa o quanto em reais(R$) está fora ou dentro do range do perfil designado
            - alinhamento_classe: Informa onde deve ser feita a alocação e a quantidade de montante em reais (R$)
    """
    
    def porcento_classe(self, row, tipo_investimento):
        """
            Transforma as classes em porcentagem de acordo com a proporcao devida
            em relacao ao patrimonio liquido total
        """
        return round(row[tipo_investimento] / row['pl'], 2)


    def bandeira_classe(self, row, persona, tipo_investimento):
        """
            Sinaliza onde está para mais ou menos de acordo com os ranges acordados no ips.
            Lógica Aplicada:
                - O cliente tem que ter 0 para estar dentro do padrão do perfil.
                - Se estiver negativo, quer dizer que está abaixo do esperado (oportunidade de venda)
                - Se estiver positivo, quer dizer que ultrapassou o limite do perfil (realocar)
        """
        return round(row[tipo_investimento] - persona[persona['ips'] == tipo_investimento][row['perfil']], 2)


    def reais_classe(self, row, tipo_investimento):
        """
            Transforma os valores sinalizados em montante de real (R$)
        """
        return round(row[tipo_investimento] * row['pl'], 2)


    def alinhamento_classe(self, ordenado):
        """
            Cria uma matriz com os valores alinhados com o perfil proposto pela ips e indica onde
            deve ser feita a alocacao para chegar ao balanco dos ranges
        """
        valores = {'ativo':[], 'realocar':[], 'valor_estimado_R$':[]}

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
