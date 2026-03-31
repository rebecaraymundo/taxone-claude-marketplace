# RNG-C_Segmento_ECF_v4

> Fonte: RNG-C_Segmento_ECF_v4.doc

Regras de Recuperação para os registros do bloco C:
Registro C400 – Equipamento ECF (Códigos 02 e 2D)
RNG-C400	
SE Indicador da Escrituração (NF-e e ECF): (parâmetro nos dados iniciais da obrigação)
     Igual a “1 – Apuração com base nos registros consolidados...”	
 
	Não gravar dados nesse registro.

SE Indicador da Escrituração (NF-e e ECF): (parâmetro nos dados iniciais da obrigação)
     Igual a “2 – Apuração com base nos registros individualizados...”

Deve ser gerado um registro C400 para cada equipamento ECF gravado na SAFX2087 que tenha sido movimentado nos registros C405 do período (para identificar os equipamentos ECF movimentados no período, utilizar o campo “04 – Número do Caixa” da SAFX991). Devem ser considerados apenas os modelos 02, 2D, 59 e 60. Sendo que o modelo 59 será considerado se na tela de “Dados Iniciais” (menu: Parâmetros >> Dados Iniciais) o registro C010 estiver com indicador 2 – Apuração com base nos registros individualizado de NF-e(C100 e C170) e de ECF(C400). Caso o período selecionado anterior a 01/05/2015. [OS4762].

Alteração MFS-19270: Inclusão do modelo 60. Conforme orientação do GP de vrs 1.26 sem publicação de ato legal, apenas orientação da Receita Federal em 21/06/2018 de acordo com a disponibilização do PVA 3.00. Atenção: considerar os modelos nos registros filhos.
		
Registro C405 – Redução Z (Códigos 02 e 2D)
RNG-C405	SE Indicador da Escrituração (NF-e e ECF): (parâmetro nos dados iniciais da obrigação)
	Igual a “1 – Apuração com base nos registros consolidados...”

Não gravar dados nesse registro.

SE Indicador da Escrituração (NF-e e ECF): (parâmetro nos dados iniciais da obrigação)
	Igual a “2 – Apuração com base nos registros individualizados...”

Deve ser gerado um registro C405 para cada redução Z gravada na SAFX991 que atenda aos critérios abaixo:
Data de Movimento: (campo 06 da SAFX991)
	Entre a data inicial e final de geração do arquivo.

Obs1: Se o campo 15 da SAFX991 estiver igual “0” significa que o campo “VL_BRT” no registro C405 será gravado com “0,00”, então:
Se o campo 15 (venda bruta diária) da SAFX991 = 0;
         Se campo 16 (venda líquida diária) = 0; 
                  Se o valor do campo 13 (GT inicial) for = ao valor do campo 14 (GT final),
                        Não gerar o registro C400 e os filhos C405, C481, C485 e C489.

Obs2: Nos casos em que todos os cupons do dia (numa determinada Redução Z), estiverem cancelados, não gerar os registros C400 e os filhos C405, C481, C485 e C489.
[OS4316-A] Tratamento para Geração de SCPs

Quando a geração for realizada através da tela de "Geração dos Registros" do menu "Obrigações SCP", além da regra padrão de seleção, deve ser considerado:

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados (considerando a regra padrão de seleção) e que não tenham o campo Código do SCP preenchido.

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados (considerando a regra padrão de seleção) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento (considerando a regra padrão de seleção) e que não tenham o campo Código do SCP preenchido.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento (considerando a regra padrão de seleção) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração.
[OS4316-C] Observar a parametrização de "Dados Iniciais" (menu: Parâmetros >> Dados Iniciais) para geração ou não do registro. Se houver um cadastro de "Dados Iniciais" cujo campo Código da SCP esteja preenchido para a SCP que o arquivo está sendo gerado e que o registro se enquadre no critério de geração, respeitar o parametrizado para a SCP. Se não houver, considerar o cadastro de Dados Iniciais do Sócio Ostensivo (Código da SCP não informada) como valido também para a SCP para o qual o arquivo está sendo gerado.
Para a geração do arquivo do Sócio Ostensivo, permanece como válido o registro cujo campo código da SCP não está preenchido.		RNC405-05	Campo NUM_COO_FIN:

Neste campo deve gravar o conteúdo do campo 07 – COO da tabela SAFX991.

[ALTERADA – OS4835]
ALTERADA – MFS18316]
Tratamento:
-	Se o campo estiver preenchido com mais de seis posições permitidas pelo layout, truncar a informação considerando as seis primeiras ultimas posições e emitir a seguinte mensagem no log: “O Número do Contador de Ordem de Operação (COO) do Registro C405 excede o tamanho permitido, favor verificar Redução Z”.		
Registro C481 – Resumo Diário de Documentos Emitidos por ECF – PIS/PASEP (Códigos 02 e 2D)
RNG-C481	Este registro deverá ser gerado com a sumarização diária dos produtos comercializados na Redução Z, ou seja, todos os itens vendidos no dia.
O sistema deve identificar os cupons fiscais que integram cada redução Z gerada no registro C405 através dos seguintes filtros:
Passo 1: Selecionar na SAFX991 o COO Inicial (Campo 11), o COO Final (Campo 12), a data de movimento (campo 06) e o número do caixa (campo 04).
Passo 2: Selecionar na SAFX993 os cupons com número do caixa (campo 04) igual ao número do caixa encontrado no passo 1 e com situação (campo 10) igual a “1”.
Passo 3: Nos cupons encontrados no passo 2, selecionar na SAFX993 os cupons com data de emissão (campo 06) igual à data de movimento encontrada no passo 1 e com hora final de emissão (campo 19) >= 02:00, OU, com data de emissão (campo 06) um dia maior que a data de movimento encontrada no passo 1 e com hora final de emissão (campo 19) <= 02:00.
Obs.: Se o campo Hora Final de Emissão não estiver preenchido, considerar apenas os registros da SAFX993 com data de emissão (campo campo 06) igual à data de movimento encontrada no passo 1.
Passo 4:
Se o COO Inicial da redução Z for menor que o COO Final (ambos selecionados no passo 1):
	Nos cupons encontrados no passo 3, selecionar na SAFX993 os cupons que possuírem COO 	(campo 05) entre o COO Inicial e o COO Final.

Se o COO Inicial da redução Z for maior que o COO Final (ambos selecionados no passo 1):
	Nos cupons encontrados no passo 3, selecionar na SAFX993 os cupons que possuírem COO 	(campo 05) entre o COO Inicial e o COO Final p/ Reinício (campo 38 da SAFX2087 referente ao 	equipamento ECF em questão), e também os cupons que possuírem COO (campo 05) entre 	“000000” e o COO Final.

Passo 5: Dos cupons encontrados no passo 4, selecionar na SAFX994 os registros que possuam a mesma chave (abaixo) da SAFX993 e cuja situação do item no cupom (campo 11) igual a “1” ou “3”.

Empresa;
Estabelecimento;
Modelo Documento;
Nº do Caixa;
COO;

Passo 6: Deve ser gerado um registro C481 para cada combinação de (produto/serviço, CST PIS, Alíquota PIS, Alíquota PIS – em reais e Conta Contábil) presente nos detalhes de cupom fiscal encontrados no passo 5.		
Registro C485 – Resumo Diário de Documentos Emitidos por ECF – COFINS (Códigos 02 e 2D)
RNG-C485	Este registro deverá ser gerado com a sumarização diária dos produtos comercializados na Redução Z, ou seja, todos os itens vendidos no dia.
O sistema deve identificar os cupons fiscais que integram cada redução Z gerada no registro C405 através dos seguintes filtros:
Mesma regra do registro C481 até o passo 5

Passo 6: Deve ser gerado um registro C481 para cada combinação de (produto/serviço, CST COFINS, Alíquota COFINS, Alíquota COFINS – em reais e Conta Contábil) presente nos detalhes de cupom fiscal encontrados no passo 5.		
Registro C489 – Processo Referenciado
RNG-C489	Este registro deverá ser gerado para cada processo referenciado informado na tela “Registro C489 – Processo Referenciado” da Capa Cupom Fiscal (SAFX993) do módulo Básicos – MasterSAF DW, item de menu Manutenção >> Cupom Fiscal (EFD\ REDF) >> Movimentos >> Capa Cupom Fiscal >> (Botão   Registro C489 – Processo Referenciado).

Poderão ser gerados N registros. 	MFS-14228		RNC489-01	Campo REG

Gravar o texto fixo “C489”.	MFS-14228		RNC489-02	Campo NUM_PROC

Recuperar o conteúdo do campo Número do Processo informado na tela “Registro C489 – Processo Referenciado” da Capa Cupom Fiscal (SAFX993).	MFS-14228		RNC489-03	Campo IND_PROC

Recuperar o conteúdo do campo Indicador da Origem do Processo informado na tela “Registro C489 – Processo Referenciado” da Capa Cupom Fiscal (SAFX993).

Gravar “1”, caso a opção selecionada seja igual a “1 – Justiça Federal”;
Gravar “3”, caso a opção selecionada seja igual a “3 – Secretaria da Receita Federal do Brasil”; 
Gravar “9”, caso a opção selecionada seja igual a “9 – Outros”.	MFS-14228		
Registro C490 – Consolidação de Documentos Emitidos por ECF (Códigos 02, 2D e 60)
RNG-C490	Este registro deverá ser gerado com a sumarização mensal dos documentos emitidos por ECF, de acordo com a seguinte regra:
Indicador da Escrituração (NF-e e ECF): (parâmetro nos dados iniciais da obrigação)
	SE for igual “1 – Apuração com base nos registros consolidados...”

Gerar um registro para cada modelo de documento movimentado na SAFX994 no período (data do movimento entre a data inicial e final de geração do arquivo). Devem ser considerados apenas os modelos 02, 2D, 59 e 60. Sendo que o modelo 59 será considerado se na tela de “Dados Iniciais” (menu: Parâmetros >> Dados Iniciais) o registro C010 estiver com indicador 1 – Apuração com base nos registros de consolidação das operações por NF-e(C180 e C190) e por ECF(C490). Caso o período selecionado anterior a 01/05/2015. [OS4762].

Seguindo os passos abaixo:

Passo 1: Selecionar na SAFX991 o COO Inicial (Campo 11), o COO Final (Campo 12), a data de movimento (campo 06) e o número do caixa (campo 04).

Passo 2: Selecionar na SAFX994 os cupons com número do caixa (campo 04) igual ao número do caixa encontrado no passo 1 e com situação (campo 10) igual a “1”.

Passo 3: Nos cupons encontrados no passo 2, selecionar na SAFX994 os cupons com data de emissão (campo 06) igual à data de movimento encontrada no passo 1 e com hora final de emissão (campo 19) >= 02:00, OU, com data de emissão (campo 06) um dia maior que a data de movimento encontrada no passo 1 e com hora final de emissão (campo 19) <= 02:00.

Obs.: Se o campo Hora Final de Emissão não estiver preenchido, considerar apenas os registros da SAFX994 com data de emissão (campo 06) igual à data de movimento encontrada no passo 1.

Exemplo: Documento emitido em 11/01/2012 até as 02hs – A data de movimento será o próprio dia 11/01/2012, se emitido depois das 2hs o movimento será 12/01/2012.
	SENÃO (igual a “2 – Apuração com base nos registros individualizados...)

Não gravar dados nesse registro.

[OS4316-A] Tratamento para Geração de SCPs

Quando a geração for realizada através da tela de "Geração dos Registros" do menu "Obrigações SCP", além da regra padrão de seleção, deve ser considerado:

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados (considerando a regra padrão de seleção) e que não tenham o campo Código do SCP preenchido.

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados (considerando a regra padrão de seleção) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento (considerando a regra padrão de seleção) e que não tenham o campo Código do SCP preenchido.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento (considerando a regra padrão de seleção) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração.

[OS4316-C] Observar a parametrização de "Dados Iniciais" (menu: Parâmetros >> Dados Iniciais) para geração ou não do registro. Se houver um cadastro de "Dados Iniciais" cujo campo Código da SCP esteja preenchido para a SCP que o arquivo está sendo gerado e que o registro se enquadre no critério de geração, respeitar o parametrizado para a SCP. Se não houver, considerar o cadastro de Dados Iniciais do Sócio Ostensivo (Código da SCP não informada) como valido também para a SCP para o qual o arquivo está sendo gerado.

Para a geração do arquivo do Sócio Ostensivo, permanece como válido o registro cujo campo código da SCP não está preenchido.		RNC490-02	Campo DT_DOC_INI:
Gravar nesse campo a menor data de movimento dos registros de SAFX991 encontrados para aquele modelo de acordo com a RNG-C490.		RNC490-03	Campo DT_DOC_FIM:
Gravar nesse campo a maior data de movimento dos registros de SAFX991 encontrados para aquele modelo de acordo com a RNG-C490.		
Registro C491 – Detalhamento da Consolidação de Documentos Emitidos por ECF (Códigos 02, 2D e 60) – PIS/PASEP
RNG-C491	Se for gerado registro C490, para cada modelo de documento movimentado:

Deverão ser agrupados nesse registro todos os cupons gerados de acordo com as regras dos registros C481 no período. O agrupamento deverá considerar os seguintes campos:

- Código do Item
- CST PIS
- CFOP
- Alíquota PIS (em percentual)
- Alíquota PIS (em reais)
- Código da Conta		RNC491-04	Campo CFOP:

Este campo pode ser preenchido de 2 formas:
Gravar o conteúdo do campo 14-CFOP da SAFX994.
Se o CFOP não estiver preenchido na SAFX994, a partir do conteúdo do campo 15 da SAFX994 ir na tabela “Totalizador Parcial do ECF”, e se preenchido gravar conteúdo do campo 13-CFOP. 		RNC491-10	Campo VL_PIS
Se alíquota em Reais:
Campo 08 - QUANT_BC_PIS * Campo 09 – ALIQ_PIS_QUANT
Se alíquota em Percentual:
Campo 06 - VL_BC_PIS * Campo 07 – ALIQ_PIS /100

Gravar o somatório do campo VLR_PIS, campo 26 da SAFX994

	CH32048_2012
MFS11424		
Registro C495 – Detalhamento da Consolidação de Documentos Emitidos por ECF (Códigos 02, 2D e 60) – COFINS
RNG-C495	Se for gerado registro C490, para cada modelo de documento movimentado:

Deverão ser agrupados nesse registro todos os cupons gerados de acordo com as regras dos registros C485 do período. O agrupamento deverá considerar os seguintes campos:

- Código do Item
- CST COFINS
- CFOP
- Alíquota COFINS (em percentual)
- Alíquota COFINS (em reais)
- Código da Conta		RNC495-04	Campo CFOP:

Este campo pode ser preenchido de 2 formas:
Gravar o conteúdo do campo 14-CFOP da SAFX994.
Se o CFOP não estiver preenchido na SAFX994, a partir do conteúdo do campo 15 da SAFX994 ir na tabela “Totalizador Parcial do ECF”, e se preenchido gravar conteúdo do campo 13-CFOP. 		RNC495-10	Campo VL_COFINS
Se alíquota em Reais:
Campo 08 - QUANT_BC_COFINS * Campo 09 – ALIQ_COFINS_QUANT
Se alíquota em Percentual:
Campo 06 - VL_BC_COFINS * Campo 07 – ALIQ_COFINS / 100	CH32048_2012		
Registro C499 – Processo Referenciado
RNG-C499	Este registro deverá ser gerado para cada processo referenciado informado na tela “Registro C499 – Processo Referenciado” do Detalhe do Cupom Fiscal (SAFX994) do módulo Básicos – MasterSAF DW, item de menu Manutenção >> Cupom Fiscal (EFD\ REDF) >> Movimentos >> Detalhe do Cupom Fiscal >> (Botão   Registro C499 – Processo Referenciado).

Poderão ser gerados N registros. 	MFS-14228		RNC499-01	Campo REG

Gravar o texto fixo “C499”.	MFS-14228		RNC499-02	Campo NUM_PROC

Recuperar o conteúdo do campo Número do Processo informado na tela “Registro C499 – Processo Referenciado” do Detalhe do Cupom Fiscal (SAFX994).	MFS-14228		RNC499-03	Campo IND_PROC

Recuperar o conteúdo do campo Indicador da Origem do Processo informado na tela “Registro C499 – Processo Referenciado” da Capa Cupom Fiscal (SAFX994).

Gravar “1”, caso a opção selecionada seja igual a “1 – Justiça Federal”;
Gravar “3”, caso a opção selecionada seja igual a “3 – Secretaria da Receita Federal do Brasil”;
Gravar “9”, caso a opção selecionada seja igual a “9 – Outros”.	MFS-14228		
Registro C800 – Cupom Fiscal Eletrônico – CF-e (Código 59)
RNG-C800	


	OS4316-E/OS4762		RNC800-01		OS4316-E/OS4762		RNC800-02		OS4316-E/OS4762		RNC800-03		OS4316-E/OS4762		RNC800-04		OS4316-E/OS4762		RNC800-05		OS4316-E/OS4762		RNC800-06		OS4316-E/OS4762		RNC800-07		OS4316-E/OS4762		RNC800-08		OS4316-E/OS4762		RNC800-09		OS4316-E/OS4762		RNC800-10		OS4316-E/OS4762		RNC800-11		OS4316-E/OS4762		RNC800-12		OS4316-E/OS4762		RNC800-13		OS4316-E/OS4762		RNC800-14		OS4316-E/OS4762		RNC800-15		OS4316-E/OS4762		RNC800-16		OS4316-E/OS4762		RNC800-17		OS4316-E/OS4762		
Registro C810 – Detalhamento do Cupom Fiscal Eletrônico – CF-e (Código 59) – PIS/PASEP e COFINS
RNG-C810	

	OS4316-E/OS4762		RNC810-01	
	OS4316-E/OS4762		RNC810-02	
	OS4316-E/OS4762		RNC810-03		OS4316-E/OS4762		RNC810-04	
.	OS4316-E/OS4762		RNC810-05		OS4316-E/OS4762		RNC810-06		OS4316-E/OS4762		RNC810-07		OS4316-E/OS4762		RNC810-08		OS4316-E/OS4762		RNC810-09		OS4316-E/OS4762		RNC810-10		OS4316-E/OS4762		RNC810-11		OS4316-E/OS4762		RNC810-12		OS4316-E/OS4762		RNC810-13	
	OS4316-E/OS4762		
Registro C820 – Detalhamento do Cupom Fiscal Eletrônico – CF-e (código 59) – PIS/PASEP e COFINS Apurado por Unidade de Medida de Produto
RNG-C820	
	OS4316-E/OS4762		RNC820-01		OS4316-E/OS4762		RNC820-02	
	OS4316-E/OS4762		RNC820-03	
	OS4316-E/OS4762		RNC820-04	


	OS4316-E/OS4762		RNC820-05		OS4316-E/OS4762		RNC820-06		OS4316-E/OS4762		RNC820-07	

	OS4316-E/OS4762		RNC820-08	
	OS4316-E/OS4762		RNC820-09		OS4316-E/OS4762		RNC820-10		OS4316-E/OS4762		RNC820-11		OS4316-E/OS4762		RNC820-12		OS4316-E/OS4762		RNC820-13		OS4316-E/OS4762		
Registro C830 – Processo Referenciado
RNG-C830	
Origem das Informações:

Regra de Seleção:

Agrupamento:

Registro pai:
		RNC830-01	Campo REG		RNC830-02	Campo NUM_PROC		RNC830-03	Campo IND_PROC		
Registro C860 – Identificação do Equipamento SAT - CF-e
RNG-C860	
Origem das Informações: SAFX201 - Capa Cupom Fiscal Eletrônico

Regra de Seleção: Este registro e seus filhos serão gerados quando, na tela de “Dados Iniciais” o parâmetro “Registro de Cupom Fiscal Eletrônico (Modelo 59) / Geração Consolidada por Equipamento SAT CF-e” estiver selecionado, e no cadastro do perfil (Menu: Parâmetros >>Perfil) o registro C860 estiver selecionado.  

Obs: Período deverá ser igual ou superior a 01/05/2015. 

[ALTERADA – CH13996_2015] [ALTERADA – CH13683-A_2016]
Serão considerados registros da tabela SAFX201, para a empresa e estabelecimento (ou estabelecimentos, para geração centralizada) indicados e cuja Data de Emissão compreenda os totais de vendas diárias. Não devem ser consideradas informações de Documentos Cancelados.

Agrupamento: COD_MOD, NR_SAT, DOC_INI e DOC_FIM

Registro pai: C010
	OS4316-E/
OS4762/
CH13996_2015
CH13683-A_2016		RNC860-01	Campo REG

Gerar informação fixa “C860”.	OS4316-E		RNC860-02	Campo COD_MOD

Preencher com o campo Modelo do Documento (COD_MODELO) da SAFX201.	OS4316-E		RNC860-03	Campo NR_SAT

Preencher com o campo Número do Equipamento (NUM_EQUIP) da SAFX201.	OS4316-E		RNC860-04	Campo DT_DOC

Preencher com o campo Data de Emissão (DATA_EMISSAO) da SAFX201.	OS4316-E		RNC860-05	Campo DOC_INI

Preencher com o campo Número do Cupom Fiscal (NUM_CUPOM) da SAFX201, considerando o menor número encontrado para a Data de Emissão. 
O valor informado deve ser menor ou igual ao valor informado no Campo 6.	OS4316-E		RNC860-06	Campo DOC_FIM

Preencher com o campo Número do Cupom Fiscal (NUM_CUPOM) da SAFX201, considerando o maior número encontrado para a Data de Emissão.
o valor informado deve ser maior ou igual ao valor informado no Campo 5.	OS4316-E		
Registro C870 – Detalhamento do Cupom Fiscal Eletrônico (Código 59) – PIS/PASEP e COFINS
RNG-C870	
Origem das Informações: SAFX202 - Detalhe Cupom Fiscal Eletrônico

Regra de Seleção: Serão considerados registros da SAFX202, respeitando as regras de seleção do registro pai C860 e buscando Itens que tenham o campo Código de Situação Tributária PIS e Código de Situação Tributária COFINS preenchido com conteúdo diferente de “03”.

[ALTERADA – CH13683_2016] [ALTERADA – CH13683-A_2016]
Não devem ser consideradas informações de Documentos Cancelados.
 
Agrupamento: CFOP, COD_ITEM, CST_PIS, ALIQ_PIS, CST_COFINS, ALIQ_COFINS e COD_CTA

Registro pai: C860
	OS4316-E
CH13683_2016
CH13683-A_2016		RNC870-01	Campo REG

Gerar informação fixa “C870”.	OS4316-E		RNC870-0402	Campo COD_ITEM

Este campo deve ser gerado se, na tela de “Dados Iniciais” o parâmetro “Registro de Cupom Fiscal Eletrônico (Modelo 59) / Demonstrar Registros de Detalhamento por Código de Item” estiver selecionado. Caso contrário, gerar sem informação (“||”).

Considerar a seguinte regra: se o campo “Registro 0200 – Identificação do Item / Considerar o indicador no código do Item” da tela de “Dados Iniciais” estiver selecionado, gerar o campo: Indicador do Produto (IND_PRODUTO) – Código do Produto (COD_PRODUTO).

Se não estiver selecionado, gerar o campo: Código do Produto (COD_PRODUTO).

O código aqui informado deve ter seu cadastro correspondente demonstrado no registro 0200.	OS4316-E
CH13436_2015		RNC870-0203	Campo CFOP

Preencher com o conteúdo do campo Código Fiscal (COD_CFO) da SAFX202.	OS4316-E
CH13436_2015		RNC870-0304	Campo VL_ITEM

Preencher com a somatória do campo Valor do Item (VLR_ITEM) da SAFX202.	OS4316-E
CH13436_2015		RNC870-05	Campo VL_DESC

Preencher com a somatória do campo “Valor da Exclusão da Base de Cálculo PIS/COFINS”, “mais” a somatória do campo “Valor do Desconto” da tela de “Cupom Fiscal Eletrônico”, aba Detalhe. Ambos os campos da SAFX202.

No caso que não houver exclusões, informar o valor “0,00”.	OS4822		RNC870-0506	Campo CST_PIS

Preencher com o conteúdo do campo Código de Situação Tributária PIS (COD_SIT_TRIB_PIS) da SAFX202.	OS4316-E		RNC870-0607	Campo VL_BC_PIS

Preencher com a somatória do campo Valor da BC PIS (VLR_BASE_PIS) da SAFX202.	OS4316-E		RNC870-0708	Campo ALIQ_PIS

Preencher com conteúdo do campo Alíquota do PIS (VLR_ALIQ_PIS) da SAFX202.	OS4316-E		RNC870-0809	Campo VL_PIS

Preencher com o resultado do cálculo VL_BC_PIS * (ALIQ_PIS / 100).	OS4316-E		RNC870-0910	Campo CST_COFINS

Preencher com o conteúdo do campo Código de Situação Tributária COFINS (COD_SIT_TRIB_COFINS) da SAFX202.	OS4316-E		RNC870-1011	Campo VL_BC_COFINS

Preencher com a somatória do campo Valor da BC COFINS (VLR_BASE_COFINS) da SAFX202.	OS4316-E		RNC870-1112	Campo ALIQ_COFINS

Preencher com conteúdo do campo Alíquota da COFINS (VLR_ALIQ_COFINS) da SAFX202.	OS4316-E		RNC870-1213	Campo VL_COFINS

Preencher com o resultado do cálculo VL_BC_COFINS * (ALIQ_COFINS / 100).	OS4316-E		RNC870-1314	Campo COD_CTA

Preencher com o conteúdo do campo Conta Contábil (COD_CONTA) da SAFX202.

O código aqui informado deve ter seu cadastro correspondente demonstrado no registro 0500.	OS4316-E		
Registro C880 – Detalhamento do Cupom Fiscal Eletrônico (Código 59) – PIS/PASEP e COFINS Apurado por Unidade de Medida de Produto
RNG-C880	
Origem das Informações: SAFX202 - Detalhe Cupom Fiscal Eletrônico

Regra de Seleção: Serão considerados registros da SAFX202, respeitando as regras de seleção do registro pai C860 e buscando Itens que tenham o campo Código de Situação Tributária PIS e Código de Situação Tributária COFINS preenchido com conteúdo igual a “03”.

Não devem ser consideradas informações de Documentos Cancelados.

Agrupamento: CFOP, COD_ITEM, CST_PIS, ALIQ_PIS, CST_COFINS, ALIQ_COFINS e COD_CTA

Registro pai: C860
	OS4316-E		RNC880-01	Campo REG

Gerar informação fixa “C880”.	OS4316-E		RNC880-02	Campo COD_ITEM

Este campo deve ser gerado se, na tela de “Dados Iniciais” o parâmetro “Registro de Cupom Fiscal Eletrônico (Modelo 59) / Demonstrar Registros de Detalhamento por Código de Item” estiver selecionado. Caso contrário, gerar sem informação (“||”).

Considerar a seguinte regra: se o campo “Registro 0200 – Identificação do Item / Considerar o indicador no código do Item” da tela de “Dados Iniciais” estiver selecionado, gerar o campo: Indicador do Produto (IND_PRODUTO) – Código do Produto (COD_PRODUTO).

Se não estiver selecionado, gerar o campo: Código do Produto (COD_PRODUTO).

O código aqui informado deve ter seu cadastro correspondente demonstrado no registro 0200.	OS4316-E		RNC880-03	Campo CFOP

Preencher com o conteúdo do campo Código Fiscal (COD_CFO) da SAFX202.	OS4316-E		RNC880-04	Campo VL_ITEM

Preencher com a somatória do campo Valor do Item (VLR_ITEM) da SAFX202.	OS4316-E		RNC880-05	Campo VL_DESC

Preencher com a somatória do campo “Valor da Exclusão da Base de Cálculo PIS/COFINS”, “mais” a somatória do campo “Valor do Desconto” da tela de “Cupom Fiscal Eletrônico”, aba Detalhe. Ambos os campos da SAFX202.

No caso que não houver exclusões, informar o valor “0,00”.	OS4822		RNC880-05	Campo CST_PIS

Preencher com o conteúdo do campo Código de Situação Tributária PIS (COD_SIT_TRIB_PIS) da SAFX202.	OS4316-E		RNC880-0607	Campo QUANT_BC_PIS

Preencher com a somatória do campo Quantidade da BC PIS (QTD_BASE_PIS) da SAFX202.
	OS4316-E		RNC880-0708	Campo ALIQ_PIS_QUANT

Preencher com conteúdo do campo Alíquota do PIS em Reais (VLR_ALIQ_PIS_R) da SAFX202.	OS4316-E		RNC880-0809	Campo VL_PIS

Preencher com o resultado do cálculo QUANT_BC_PIS * ALIQ_PIS_QUANT.	OS4316-E		RNC880-0910	Campo CST_COFINS

Preencher com o conteúdo do campo Código de Situação Tributária COFINS (COD_SIT_TRIB_COFINS) da SAFX202.	OS4316-E		RNC880-1011	Campo QUANT_BC_COFINS

Preencher com a somatória do campo Quantidade da BC COFINS (QTD_BASE_COFINS) da SAFX202.
	OS4316-E		RNC880-1112	Campo ALIQ_COFINS_QUANT

Preencher com conteúdo do campo Alíquota da COFINS em Reais (VLR_ALIQ_COFINS_R) da SAFX202.	OS4316-E		RNC880-1213	Campo VL_COFINS

Preencher com o resultado do cálculo QUANT_BC_COFINS * ALIQ_PIS_COFINS.	OS4316-E		RNC880-1314	Campo COD_CTA

Preencher com o conteúdo do campo Conta Contábil (COD_CONTA) da SAFX202.

O código aqui informado deve ter seu cadastro correspondente demonstrado no registro 0500.	OS4316-E		
Registro C890 – Processo Referenciado
RNG-C890	Este registro deverá ser gerado para cada processo referenciado informado na tela “Registro C890 – Processo Referenciado” do detalhe do Cupom Fiscal Eletrônico (SAFX202) do módulo Básicos – MasterSAF DW, item de menu Manutenção >> Cupom Fiscal Eletrônico >> aba Detalhe Cupom Fiscal Eletrônico – SAT >> (Botão   Registro C890 – Processo Referenciado).

Poderão ser gerados N registros. 	MFS-14228		RNC890-01	Campo REG

Gravar o texto fixo “C890”.	MFS-14228		RNC890-02	Campo NUM_PROC

Recuperar o conteúdo do campo Número do Processo informado na tela “Registro C890 – Processo Referenciado” do detalhe do Cupom Fiscal Eletrônico (SAFX202).	MFS-14228		RNC890-03	Campo IND_PROC

Recuperar o conteúdo do campo Indicador da Origem do Processo informado na tela “Registro C890 – Processo Referenciado” do detalhe do Cupom Fiscal Eletrônico (SAFX202).

Gravar “1”, caso a opção selecionada seja igual a “1 – Justiça Federal”;
Gravar “3”, caso a opção selecionada seja igual a “3 – Secretaria da Receita Federal do Brasil”;
Gravar “9”, caso a opção selecionada seja igual a “9 – Outros”.	MFS-14228