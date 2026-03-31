# RNG-P_V4

> Fonte: RNG-P_V4.doc

Regras de Recuperação para os registros do bloco P:
Registro P001 – Abertura do Bloco
RNG-P001	Deve ser gerado um registro por arquivo.	OS3584-GE		RNP001-02	Campo IND_MOV:

Gravar "0" se existir movimentação a ser gerada no bloco P no período informado na tela de geração. Senão, gravar ‘’1’’

ATENÇÃO: Só deve ser gerado o P001 se existir pelo menos um registro 0145 no período.

	OS3584-GE / 
CH13843_2012		
Registro P010 – Identificação do Estabelecimento
RNG-P010
	Gerar um registro P010 para cada CNPJ de estabelecimento que possua movimentação nos registros do bloco P e que na Tela Empresa/Estabelecimento o parâmetro‘Código indicador da incidência de tributação da contribuição previdenciária’ esteja com as opções ‘1 – Contribuição Previdenciária apurada exclusivamente com base na Receita Bruta;’ ou ‘2 – Contribuição Previdenciária apurada com base na Receita Bruta e nas Remunerações pagas. ‘

As movimentações do bloco P devem ser geradas imediatamente abaixo do registro P010 do CNPJ do estabelecimento correspondente.

* Foi incluída observação para gerar por CNPJ do estabelecimento por conta de situações onde a empresa tem mais de um estabelecimento com o mesmo CNPJ. Neste caso, deve ser gerado apenas um A010 por CNPJ e as movimentações serão vinculadas abaixo do CNPJ.
	OS3584-GE
CH27235/2013
		
Registro P100 – Contribuição Previdenciária sobre a Receita Bruta
RNG-P100
	O Bloco pode ser gerado no regime Lucro Real e no Lucro Presumido.
Se apenas existir as informações referente ao Bloco P na base, se faz necessário à abertura e encerramento dos demais blocos (como já gerados no Lucro Real)  e os registros M200 e M600 deverão ser gerados zerados.

Gerar um registro P100 para cada registro gravado na SAFX185 no período, desde que o parâmetro‘Código indicador da incidência de tributação da contribuição previdenciária’ da  Tela Empresa/Estabelecimento esteja com as opções ‘1 – Contribuição Previdenciária apurada exclusivamente com base na Receita Bruta;’ ou ‘2 – Contribuição Previdenciária apurada com base na Receita Bruta e nas Remunerações pagas. ‘
Considerar os campos 03 - Data Inicial e 04- Data Final
		
[OS4316-A] Tratamento para Geração de SCPs

Quando a geração for realizada através da tela de "Geração dos Registros" do menu "Obrigações SCP", além da regra padrão de seleção, deve ser considerado:

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados (considerando a regra padrão de seleção) e que não tenham o campo Código do SCP preenchido.

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados (considerando a regra padrão de seleção) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento (considerando a regra padrão de seleção) e que não tenham o campo Código do SCP preenchido.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento (considerando a regra padrão de seleção) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração.
[OS4316-C] Observar a parametrização de "Dados Iniciais" (menu: Parâmetros >> Dados Iniciais) para geração ou não do registro. Se houver um cadastro de "Dados Iniciais" cujo campo Código da SCP esteja preenchido para a SCP que o arquivo está sendo gerado e que o registro se enquadre no critério de geração, respeitar o parametrizado para a SCP. Se não houver, considerar o cadastro de Dados Iniciais do Sócio Ostensivo (Código da SCP não informada) como valido também para a SCP para o qual o arquivo está sendo gerado.
Para a geração do arquivo do Sócio Ostensivo, permanece como válido o registro cujo campo código da SCP não está preenchido.	OS3584-GE
CH13843_2012		RNP100-02	Campo DT_INI

Considerar o campo 03 – Data inicial da SAFX185
	OS3584-GE		RNP100-03	Campo DT_FIN

Considerar o campo 04 – Data Final da SAFX185
	OS3584-GE		RNP100-04	Campo VL_REC_TOT_EST

Considerar o Campo 09 – Valor da Receita Bruta Total da SAFX185

	OS3584-GE		RNP100-05	Campo COD_ATIV_ECON

Considerar o Campo 05 – Indicador da Atividade Econômica da SAFX185
	OS3584-GE		RNP100-06	Campo VL_REC_ATIV_ESTAB
	
Considerar o Campo 10 – Valor da Receita Bruta do Estabelecimento  da SAFX185	OS3584-GE		RNP100-07	
Campo VL_EXC
Considerar o Campo 12 – Valor das Exclusões da Receita Bruta da SAFX185	OS3584-GE		RNP100-08	Campo VL_BC_CONT

Considerar o Campo 13– Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta da SAFX185	OS3584-GE		RNP100-09	Campo ALIQ_CONT

Considerar o Campo 14 - Alíquota da Contribuição Previdenciária sobre a Receita Bruta da SAFX185
	OS3584-GE		RNP100-10	Campo VL_CONT_APUR

Considerar o Campo 15 – Valor da Contribuição Previdenciária Apurada sobre a Receita Bruta da SAFX185	OS3584-GE		RNP100-11	Campo COD_CTA

Considerar o Campo 07 – Código da conta analítica debitada/creditada da SAFX185	OS3584-GE		RNP100-12	Campo INFO_COMPL

Considerar o Campo 16 – Descrição complementar do Registro da SAFX185	OS3584-GE		
Registro P110 – Complemento da Escrituração – Detalhamento da Apuração da Contribuição
RNG-P110
	Neste momento, este registro não será contemplado na geração do Meio Magnético		


Registro P199 – Processo Referenciado
RNG-P199
	Deverá ser gerado um registro P199  para cada registro informado na tela “Processo Referenciado (P199)” do menu Manutenção >> Registro Bloco P >>tela Contribuição Previdenciária Sobre a Receita Bruta (P100):
Poderao ser gerados N registros.	OS3584-GE		RNP199-02	Campo NUM_PROC

Deverá ser recuperado do campo “Número Processo” da tela “Processo Referenciado (P199)”.	OS3584-GE		RNP199-03	Campo IND_PROC

Deverá ser recuperado do campo “Indicador da Origem do Processo” da tela “Processo Referenciado (P199)”.

Gravar “1”, caso a opção selecionada seja “1 – Justiça Federal”
Gravar “2”, caso a opção selecionada seja “2 – Secretaria da Receita Federal do Brasil”
Gravar “9”, caso a opção selecionada seja “9 – Outros”	OS3584-GE		

Registro P200 – Consolidação da Contribuição Previdenciária sobre a Receita Bruta 
RNG-P200
	Gerar um registro P200 por  empresa  e código de receita  (Consolidação das Informações do P100)

O agrupamento dos registros deve ser feito de acordo com os campos chaves deste registro:

Empresa (Campo 01)
Código da Receita (Campo 06)

	OS3584-GE		RNP200-02	Campo PER_REF
 
Informar o período de referencia da escrituração no formato MMAAAA

(considerando os campo 03 e 04 da safx185), se não existir informação de Ajuste. Caso contrário considerar o MM/AAAA do campo ‘Data de Referência’ da tela  ‘Ajustes da Contribuição Previdenciária Apurada Sobre a Receita Bruta (P210)’
	OS3584-GE		RNP200-03	Campo VL_TOT_CONT_APU

Informar o valor total da contribuição previdenciária apurada no período , correspondendo a soma dos valores constantes no campo 10 – VL_CONT_APU dos registros P100 (Campo 15 da SAFX185)	OS3584-GE		RNP200-04	Campo VL_TOT_AJ_REDUC
Informar o valor  dos ajustes de redução  da contribuição previdenciária apurada , correspondente ao somatório dos valores informados no Campo 03 do registro P210, campo o campo 02 do P210 for igual a “0”.	OS3584-GE		RNP200-05	Campo VL_TOT_AJ_ACRES

Informar o valor  dos ajustes de acréscimo  da contribuição previdenciária apurada , correspondente ao somatório dos valores informados no Campo 03 do registro P210, campo o campo 02 do P210 for igual a “1”.
	OS3584-GE		RNP200-06	Campo VL_TOT_CONT_DEV

Informar o valor total da contribuição previdenciária a recolher no período da escrituração, devendo o valor do campo ser igual a (CAMPO 03 VL_TOT_CONT_APU – CAMPO 04  VL_TOT_AJ_REDUC + CAMPO
05 VL_TOT_AJ_ACRES)
	OS3584-GE		RNP200-07	Campo COD_REC:

Ao gerar o campo 07 – COD_REC do registro P200, a informação deverá ser recuperada do campo 06-“Código da Receita” (SAFX185) tela disponível  no Módulo: SPED ( EFD – Escrituração Fiscal Digital – PIS/PASEP/COFINS, Menu: Manutenção (Registro Bloco P,  a tela Contribuição Previdenciária Sobre a Receita Bruta (P100):
	OS3584-GE		
Registro P210 – Ajuste da Contribuição Previdenciária Apurada sobre a Receita Bruta 
RNG-P210
	Gerar um registro P210 se existir informação na tela Ajustes da Contribuição Previdenciária Apurada Sobre a Receita Bruta (P210), localizada no Módulo: SPED ( EFD – Escrituração Fiscal Digital – PIS/PASEP/COFINS, Menu: Manutenção (Registro Bloco P, para o período da geração do arquivo.

Data utilizada para a recuperação dos registros é a data do mês/Ano Apuração que deve estar entre  a data inicial e data final de geração do arquivo.
	OS3584-GE		RNP210-02	Campo IND_AJ
 
Conforme campo ‘Tipo do Ajuste’ da tela ‘Ajustes da Contribuição Previdenciária Apurada Sobre a Receita Bruta (P210)’	OS3584-GE		RNP210-03	Campo VL_AJ

Conforme campo ‘Valor do Ajuste’ da tela ‘Ajustes da Contribuição Previdenciária Apurada Sobre a Receita Bruta (P210)’	OS3584-GE		RNP210-04	Campo COD_AJ

Conforme campo ‘Código do Ajuste’ da tela ‘Ajustes da Contribuição Previdenciária Apurada Sobre a Receita Bruta (P210)’	OS3584-GE		RNP210-05	Campo NUM_DOC

Conforme campo ‘Nº do Processo/Documento/Ato Concessório Vinculado’ da tela ‘Ajustes da Contribuição Previdenciária Apurada Sobre a Receita Bruta (P210)’	OS3584-GE		RNP210-06	Campo DESCR_AJ

Conforme campo ‘Descrição Resumida’ da tela ‘Ajustes da Contribuição Previdenciária Apurada Sobre a Receita Bruta (P210)’	OS3584-GE		RNP210-07	Campo DT_REF

Conforme campo ‘Data de Referência’ da tela  ‘Ajustes da Contribuição Previdenciária Apurada Sobre a Receita Bruta (P210)’	OS3584-GE		
Registro P990: Encerramento do Bloco P
RNG-P990	Só deve ser gerado o P990 se existir pelo menos um registro 0145 no período.
	CH13843_2012