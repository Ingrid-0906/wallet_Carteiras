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
