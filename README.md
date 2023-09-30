# wallet_Carteira
Repo destinada ao modelo de análise de investimento englobando carteira e classes em geral (software)

### Mapa do repositório:
/banco_dados: Todos os arquivos usado como fonte (csv e json)

	- IPS-persona.csv (Perfil dado pela Wealth)
	- carteira_macro-visao.csv (Carteira mockada com dados simulando várias carteiras fora do padrao)
	- carteira_tabela_1.json (Arquivo com o percentual de diferença do perfil atribuido)
	- carteira_tabela_2.json (Arquivo com sugestão de onde está fora do range e da onde tirar para realocar (demanda - oferta))
	- carteira_tabela_3.json (Arquivo de como a carteira deveria ficar se seguisse os ranges do perfil)
	- data-original_carteira.json (Versão em json da carteira mockada)
/analise_carteira.py: a lógica aplicada para analisar e sugerir a realocacao das classes
/app.py: Chamada do software

### Síntese da Lógica Aplicada (Perfil: Defensivo):
| classe                 | Valor Líquido (R$) | Valor vs. PL (%) ps. sem truncar | Proporção (%) vs. Ranges(%) ps. sem truncar | Saúde (%) vs Margem [(+/-)2%] ps. peso de 1 para 11 = 0.099 | Valor para Alocar (R$) |
|------------------------|--------------------|----------------------------------|---------------------------------------------|-------------------------------------------------------------|------------------------|
| renda fixa pos         | 305.291,00         | 0.132625                         | -61.737475                                  | 0.099                                                       | 1.421.139,25           |
| renda fixa hy          | 26.708,00          | 0.011603                         | -6.839745                                   | 0.099                                                       | 157.444,56             |
| renda fixa pre         | 165.775,00         | 0.072016                         | 7.201638                                    | 0.099                                                       | 78.611,68              |
| renda fixa inflacao cp | 151.579,00         | 0.065849                         | -3.415068                                   | 0.099                                                       | 0.0                    |
| multimercado           | 376.982,00         | 0.163769                         | 9.376943                                    | 0.099                                                       | 0.0                    |
| imobiliarios           | 78.008,00          | 0.033888                         | 3.388842                                    | 0.099                                                       | 0.0                    |
| renda variavel br      | 52.052,00          | 0.022613                         | 2.261256                                    | 0.099                                                       | 0.0                    |
| renda fixa global      | 323.396,00         | 0.140490                         | 14.049047                                   | 0.099                                                       | 0.0                    |
| multimercado global    | 310.652,00         | 0.134954                         | 13.495419                                   | 0.099                                                       | 0.0                    |
| renda variavel global  | 312.949,00         | 0.135952                         | 13.595206                                   | 0.099                                                       | 0.0                    |
| alternativos           | 198.515,00         | 0.086239                         | 8.623937                                    | 0.099                                                       | 0.0                    |
| TOTAL                  | 2.301.907,00       | 1.00000                          | 0.00000                                     | 1.0                                                         | 1.657.195,49           |
