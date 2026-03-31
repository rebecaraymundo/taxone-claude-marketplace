# Lancamentos_Contabeis_Tela_Lancamentos_Parte_A-SAFX256

> Fonte: Lancamentos_Contabeis_Tela_Lancamentos_Parte_A-SAFX256.doc

Módulo Job Servidor – Importação SAFX256
(Tabela de Associação dos Lançamentos Contábeis - Parte A (M312, M362) do ECF

                                           Documento de Requisito

Doc	Alteração	Data	Resp		MFS15687	Criação do Documento	04/01/2018	Liliane Assaf		

Sumário
 TOC \o "1-5" \h \z \u  HYPERLINK \l "_Toc502934853" Introdução	 PAGEREF _Toc502934853 \h 2
 HYPERLINK \l "_Toc502934854" Composição para Manual de Layout	 PAGEREF _Toc502934854 \h 2
 HYPERLINK \l "_Toc502934855" Regra Geral	 PAGEREF _Toc502934855 \h 3
 HYPERLINK \l "_Toc502934856" Consistências de Campos	 PAGEREF _Toc502934856 \h 6
 HYPERLINK \l "_Toc502934857" RN01 – Código da Empresa	 PAGEREF _Toc502934857 \h 6
 HYPERLINK \l "_Toc502934858" RN02 – Código do Estabelecimento	 PAGEREF _Toc502934858 \h 6
 HYPERLINK \l "_Toc502934859" RN03 – Ano Exercício	 PAGEREF _Toc502934859 \h 6
 HYPERLINK \l "_Toc502934860" RN04 – Data Inicial	 PAGEREF _Toc502934860 \h 6
 HYPERLINK \l "_Toc502934861" RN05 – Período	 PAGEREF _Toc502934861 \h 6
 HYPERLINK \l "_Toc502934862" RN06 – Registro da Tabela Dinâmica	 PAGEREF _Toc502934862 \h 7
 HYPERLINK \l "_Toc502934863" RN07 – Linha da Tabela Dinâmica	 PAGEREF _Toc502934863 \h 7
 HYPERLINK \l "_Toc502934864" RN08 – Código da Conta Contábil	 PAGEREF _Toc502934864 \h 7
 HYPERLINK \l "_Toc502934865" RN09 – Código do Centro de Custo	 PAGEREF _Toc502934865 \h 8
 HYPERLINK \l "_Toc502934866" RN10 – Data do Lançamento Contábil	 PAGEREF _Toc502934866 \h 8
 HYPERLINK \l "_Toc502934867" RN11 – Débito/Crédito do Lançamento Contábil	 PAGEREF _Toc502934867 \h 8
 HYPERLINK \l "_Toc502934868" RN12 – Arquivamento	 PAGEREF _Toc502934868 \h 9
 HYPERLINK \l "_Toc502934869" Consistências Específicas do ECF	 PAGEREF _Toc502934869 \h 9
 HYPERLINK \l "_Toc502934870" RN13 - Existência de Escrituração (Informação ECF)	 PAGEREF _Toc502934870 \h 9
 HYPERLINK \l "_Toc502934871" RN14 - Existência de Abertura de Apuração	 PAGEREF _Toc502934871 \h 9
 HYPERLINK \l "_Toc502934872" RN15 - Validação do Status da Abertura de Apuração	 PAGEREF _Toc502934872 \h 9
 HYPERLINK \l "_Toc502934873" RN16 - Existência de Registro/Linha nos Lançamentos Parte A (M300, M350) na Apuração	 PAGEREF _Toc502934873 \h 9
 HYPERLINK \l "_Toc502934874" RN17 - Existência de Detalhamento por Conta Contábil/Centro nos Lançamentos Parte A (M300, M350):	 PAGEREF _Toc502934874 \h 10
 HYPERLINK \l "_Toc502934875" Regras Gravação do Lançamento Contábil – Parte A (M312/M362)	 PAGEREF _Toc502934875 \h 10
 HYPERLINK \l "_Toc502934876" RN18 – Gravação do Lançamento Contábil – Parte A (M312/M362)	 PAGEREF _Toc502934876 \h 10
 HYPERLINK \l "_Toc502934877" Procedimentos para Atualização do Lançamento Parte A (M300/M350) - ECF:	 PAGEREF _Toc502934877 \h 11
 HYPERLINK \l "_Toc502934878" RN19 – Atualização do “Valor Total” do Detalhamento por Conta Contábil/Centro nos Lançamentos Parte A (M300, M350):	 PAGEREF _Toc502934878 \h 11
 HYPERLINK \l "_Toc502934879" RN20 – Atualização do “Valor do Lançamentos/Ajuste” e “Valor a Considerar” do Detalhamento por Conta Contábil/Centro nos Lançamentos Parte A (M300, M350):	 PAGEREF _Toc502934879 \h 12
 HYPERLINK \l "_Toc502934880" RN21 – Atualização do Registro/Linha Lançamento Parte A (M300, M350)	 PAGEREF _Toc502934880 \h 12
 HYPERLINK \l "_Toc502934881" RN22 – Atualização do Status Apuração	 PAGEREF _Toc502934881 \h 13


Introdução

A tabela SAFX256 foi criada com objetivo de carregar os lançamentos contábeis direto na apuração do ECF, associando-os às Contas Contábeis/Centros de Custo, que são os detalhamentos dos Lançamentos Parte A (registros M300, M350). 
A criação da importação da SAFX256 veio a substituir o trabalho de inclusão manual dos lançamentos via Tela de Lançamento Parte A (M300, M350), no módulo ECF - menu Apuração ( Ajustes Manuais. 

Procedimentos para a Importação da SAFX256:
A importação da SAFX256 tem como premissa a existência de uma Escrituração ECF com uma Abertura de Apuração. 

Com essas informações efetuar os seguintes passos:

1º - Processar a Transcrição de Valores.
Realizar o Processamento da Transcrição de Valores Empresa para Referenciais Fisco para a Apuração ECF na qual os lançamentos serão carregados via importação da SAFX256.
Módulo ECF, menu Apuração ( Processamento em Lote, opção Transcrição de Valores Empresa para Referenciais Fisco.
Ao final deste processo, o status da Apuração é atualizado para “Importação dos Saldos Realizado” ou “Aguardando Alteração Manual”.

Caso a execução da Transcrição de Valores finalize com status “Aguardando Alteração Manual”, é necessário efetuar o rateio no módulo ECF, menu Apuração ( Ajustes Manuais ( Balanço/DRE (Bloco K), antes de importar a SAFX256.

2º – Ratear dos Saldos das Contas Contábeis com mais de uma Conta Referencial. 
Módulo ECF, menu Apuração ( Ajustes Manuais ( Balanço/DRE (Bloco K).
Ratear todas as contas contábeis/centros de Custo que possuam associação com mais de uma Conta Referencial. Desta forma o status da Apuração é alterado para “Alteração Manual Realizada”.
Enquanto a Apuração estiver status “Aguardando Alteração Manual”, os lançamentos não poderão ser importação via SAFX256.

3º - Importar a SAFX256.
Módulo Job Servidor, menu Importação ( Execução. Ou Importação Batch ( Programação ( Execução.

4º - Enquanto a Abertura da Apuração não estiver com status de Calculo Realizado, a importação pode ser repetida.


Composição para Manual de Layout

Obrig	pk	Descrição	Nome	Comentário	Tam	tipo		(*)	(*)	Código da Empresa	COD_EMPRESA	Código da Empresa. Deve pertencer a uma Informação ECF – módulo ECF.	3	A		(*)	(*)	Código do Estabelecimento	COD_ESTAB	Código do Estabelecimento. Deve pertencer a uma Informação ECF – módulo ECF	6	A		(*)	(*)	Ano Exercício	ANO_EXERCICIO	Ano Exercício pertencente a uma Informação ECF – módulo ECF.	4	N		(*)	(*)	Data Inicial	DATA_INICIAL	Data Inicial da Informação ECF – módulo ECF. 	8	N		(*)	(*)	Período	IND_CALC_PER	Período da Apuração – módulo ECF (Abertura Apuração). Preencher com:
A01 - Janeiro, 
A02 - Fevereiro,
...
A12 - Dezembro
T01 – 1º Trimestre
...
T04 – 4º Trimestre	3	A		(*)	(*)	Registro da Tabela Dinâmica	COD_RECORD	Informar o Código do Registro M300 ou M350 relacionado ao Cadastro da Tabela Dinâmica do ECF (TFIX88). M300A, M300B, M300C, M350A, M350B, M350C.
O registro e Linha da Tabela Dinâmica devem pertencer ao resultado apurado pelo Processo de Transcrição de Valores da Apuração ECF.	8	A		(*)	(*)	Código da Linha da Tabela Dinâmica	COD_CALC_ITEM	Informar o Código da Linha relacionada ao Cadastro da Tabela Dinâmica do ECF (TFIX89).
O registro e Linha da Tabela Dinâmica devem pertencer ao resultado apurado pelo Processo de Transcrição de Valores da Apuração ECF.	50	A		(*)	(*)	Código da Conta Contábil	COD_CONTA	Informar o Código da Conta Contábil. Esta conta deve estar cadastrada na Tabela de Plano de Contas (SAFX2002).
A Conta Contábil informada deve pertencer ao detalhamento do registro e Linha da Tabela Dinâmica, apurados pelo Processo de Transcrição de Valores, do ECF.	70	A		(*)	Código do Centro de Custo	COD_CUSTO	Informar o Código do Centro de Custos. Este código deve estar cadastrado na Tabela de Centro de Custos (SAFX2003).
Caso o Centro de Custo seja informado, este juntamente com a Conta Contábil,  devem pertencer ao detalhamento do registro e Linha da Tabela Dinâmica, apurados pelo Processo de Transcrição de Valores, do ECF.	20	A		(*)	(*)	Data do Lançamento Contábil	DATA_LANCTO	Data do Lançamento Contábil. Deve pertencer a Tabela de Lançamentos SAFX01.	8	N		(*)	(*)	Débito/Crédito do Lançamento Contábil	IND_DEB_CRE	Indicador Débito/Crédito do Lançamento Contábil. Deve pertencer a Tabela de Lançamentos SAFX01.
Informar de acordo com:
D - Se o Lançamento foi a Débito da Conta.
C - Se o Lançamento foi a Crédito da Conta.	1	A		(*)	(*)	Arquivamento	ARQUIVAMENTO	Arquivamento do Lançamento Contábil. Deve pertencer a Tabela de Lançamentos SAFX01.
	50	A		

Regra Geral

A importação deve realizar os seguintes procedimentos: 
1º ) Consistências Básicas:
Campos obrigatórios;
Campos Data inválidos
Campos Numéricos inválidos
Consistência da Conta Contábil no seu cadastro de origem (SAFX2002)
Consistência do Centro de Custo no seu cadastro de origem (SAFX2003)
Consistência do Lançamento Contábil na sua tabela de origem (SAFX01)

2º) Consistências Específicas oriundas de regras do ECF:
Existência de Escrituração (Informação ECF);
Existência de Abertura de Apuração com Status diferente de “Cálculo Realizado” e “Aguardando Alteração Manual”. 
Existência de Registro/Linha nos Lançamentos Parte A (registros M300, M350), resultado da Apuração.
Existência de Detalhamento por Conta Contábil/Centro dos Lançamentos Parte A (registros M300, M350) no resultado da Apuração.

Caso o registro seja consistido com sucesso então:
3º) Gravar o Lançamento Contábil associado ao registro de “Detalhamento por Conta Contábil/Centro dos Lançamentos Parte A (registros M300, M350)” no resultado da Apuração.

4º) Realizar os mesmos procedimentos executados na tela “Lançamentos da Parte A (M300, M350)” do módulo ECF:
4.1) Recalcular o “Valor Total” do registro pai “Detalhamento por Conta Contábil/Centro dos Lançamentos Parte A (registros M300, M350)” no resultado da Apuração.
Ver Imagem 1.

4.2) Recalcular os valores “Lançamentos/Ajutes” e “Valor a Considerar” do registro pai “Detalhamento por Conta Contábil/Centro dos Lançamentos Parte A (registros M300, M350)” no resultado da Apuração.
Ver Imagem 2.

4.3) Recalcula os valores “Somatório de Contas Contábeis” e “Valor (Parte A)” do “Registro/Linha nos Lançamentos Parte A (registros M300, M350)” no resultado da Apuração.
Ver Imagem 3.

4.4) Atualizar o Status da Apuração para “Alteração Manual Realizada”.


Imagem 2:


Imagem3:


Consistências de Campos


RN01 – Código da Empresa

Crítica padrão: quando o campo não estiver preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

 90001 “O código da empresa deve ser preenchido”

RN02 – Código do Estabelecimento

Crítica padrão: quando o campo não estiver preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

 90002 “O código do estabelecimento deve ser preenchido”

Crítica padrão: quando o estabelecimento não estiver cadastrado, o registro não será importado, e no log de erros será gravada a seguinte mensagem: 

90949 Empresa e Estabelecimento nao cadastrado

RN03 – Ano Exercício

Crítica padrão: quando o campo não estiver preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

93060 “O Ano exercício deve ser preenchido.”

Crítica padrão: se o campo estiver preenchido com caracter não numérico, ou não for um ano válido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:
 
93061 “O Ano exercício preenchido com valor inválido.”

RN04 – Data Inicial

Crítica padrão: quando o campo não estiver preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

93062 “Data Inicial deve ser preenchida”

Crítica padrão: quando o campo estiver preenchido com um conteúdo que não seja uma data, o registro não será importado, e no log de erros será gravada a seguinte mensagem:
 
91212 “O campo Data Inicial e invalido”

RN05 – Período

Crítica padrão: quando o campo não estiver preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

93063 “Período da Apuração deve ser preenchido”

Crítica padrão: quando o campo estiver preenchido, com um valor que não pertença à lista de valores válidos, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

93064 “Período da Apuração preenchido com valor inválido. Os valores aceitos são: <A01>,<A02>,<A03>,<A04>,<A05>,<A06>,<A07>,<A08>,<A09>,<A10>,<A11>,<A12>,<T01>,<T02>,<T03>,<T04>”,

Lista de Valores Válidos:
A01, A02, A03, A04, A05, A06, A07, A08, A09, A10, A11, A12, T01, T02, T03, T04


RN06 – Registro da Tabela Dinâmica

Crítica padrão: quando o campo não estiver preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

913066 “Campo Registro da Tabela Dinâmica obrigatorio nao preenchido.”

Crítica padrão: quando o campo estiver preenchido, com um valor que não pertença à lista de valores válidos, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

93065 “Campo Registro da Tabela Dinâmica preenchido com valor inválido. Os valores aceitos são: <M300A>,<M300B>,<M300C>,<M350A>,<M350B>,<M350C>”,

Lista de Valores Válidos:
M300A. M300B, M300C, M350A, M350B, M350C


RN07 – Linha da Tabela Dinâmica

Crítica padrão: quando o campo não estiver preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

913067 “Campo Linha da Tabela Dinâmica obrigatorio nao preenchido.”

Crítica padrão: quando o código informado não pertencer ao seu cadastro de Origem – Linhas da Tabela Dinâmica (TFIX89), o registro não será importado, e no log de erros será gravada a seguinte mensagem:

913071 “Código da Linha da Tabela Dinâmica informado, não cadastrado na Tabela 	Dinâmica da ECF (TFIX89).”

RN08 – Código da Conta Contábil

Crítica padrão: quando o campo não estiver preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

                            90011 “Conta Contabil deve ser preenchida”

Crítica padrão: quando o código informado não pertencer ao seu cadastro de Origem – Tabela de Plano de Contas (SAFX2002), o registro não será importado, e no log de erros será gravada a seguinte mensagem:
		
90012 “Conta Contabil nao cadastrada ou data de validade posterior a data do lancamento”	
Obs: O identificador da Conta Contábil deve ser recuperado considerando a Data do Lançamento.


RN09 – Código do Centro de Custo

Campo não obrigatório.
Quando preenchido, deve ser um código cadastrado na Tabela de Centros de Custo (SAFX2003).
Caso não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

90381 ”O Campo Codigo de Centro de Custo nao esta cadastrado”

OBS: O identificador do Centro de Custo deve ser recuperado considerando a Data do Lançamento.

RN10 – Data do Lançamento Contábil

Crítica padrão: quando o campo não estiver preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

                               90102 “O Campo de Data do Lancamento Contabil deve ser preenchido”

Crítica padrão: quando o campo estiver preenchido com um conteúdo que não seja uma data, o registro não será importado, e no log de erros será gravada a seguinte mensagem:
 
93066 “O Campo de Data do Lancamento Contabil com formato invalido”

Crítica padrão: quando a Data estiver fora do período Inicial e Final definido para a importação, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

93067 “O Campo de Data do Lancamento Contabil esta fora do periodo definido para importação”.

Crítica padrão: quando a Data for menor que a data de fechamento do grupo 1 - Contabilidade, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

90809 “Registro Contabil nao pode ser importado, pois a Data de Lancamento e menor ou igual a Data de Fechamento do Grupo de Contabilidade”.
Obs: utilizar procedure SAF_FECHAMENTO_OL


RN11 – Débito/Crédito do Lançamento Contábil

Crítica padrão: quando o campo não estiver preenchido, ou com valor diferente de “D”, “C”, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

90100 “O Campo Debito/Credito deve ser preenchido com <D> ou <C>”

RN12 – Arquivamento
Crítica padrão: quando o campo não estiver preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

90099 “O Campo Arquivamento e obrigatorio - deve ser preenchido”

Crítica padrão: quando o registro informado não pertencer a tabela origem de Lançamento Contábil (SAFX01), o registro não será importado, e no log de erros será gravada a seguinte mensagem:

                            92557 “Lancamento Contabil nao encontrado.”


Consistências Específicas do ECF

RN13 - Existência de Escrituração (Informação ECF)

Será verificada a existência da Escrituração em questão, ou seja, se já existe uma registro em Informação ECF para a Empresa/Estabelecimento/Ano Exercício/Data Inicial. 
Tabela física (ECF_CLC_ICT_BKKPING)
Caso não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

93068 “Não existe Informação ECF o estabelecimento, ano exercício e data inicial informados”

RN14 - Existência de Abertura de Apuração

Será verificada a existência da Apuração em questão, ou seja, se já existe uma registro em Abertura Apuração (módulo ECF) para a Empresa/Estabelecimento/Ano Exercício/Data Inicial/Período. 
Tabela física (ECF_CLC_OP_CALCTION)

Caso não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

93069  “Não existe Abertura Apuração ECF para o estabelecimento, ano exercício data inicial e período informados”

RN15 - Validação do Status da Abertura de Apuração

Se o status da apuração for igual a “Cálculo Realizado” ou “Aguardando Alteração Manual”, então o registro não será importado, e no log de erros será gravada a seguinte mensagem:

93070 “Não é permitida a importação de lançamentos contábeis da Parte A, para a Abertura da Apuração com Status de Cálculo Realizado ou Aguardando Alteração Manual”.

RN16 - Existência de Registro/Linha nos Lançamentos Parte A (M300, M350) na Apuração
Será verificada a existência do Registro/Linha na Apuração em questão, ou seja, se já existe um registro de Lançamento Parte A (M300, M350) na Apuração (módulo ECF) para a Empresa/Estabelecimento/Ano Exercício/Data Inicial/Período/Registro/Linha. 
Tabela física (ECF_CLC_ITEM_BAL)

Caso não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

93071 “Não existe Lançamento Parte A (M300,M350) na Apuração ECF para o registro e linha informados.”


RN17 - Existência de Detalhamento por Conta Contábil/Centro nos Lançamentos Parte A (M300, M350):
Será verificada a existência do registro de “Detalhamento por Conta Contábil/Centro dos Lançamentos Parte A (M300, M350)” na Apuração (módulo ECF) para a Empresa/Estabelecimento/Ano Exercício/Data Inicial/Período/Registro/Linha/Conta Contábil e Centro de Custo, caso este último esteja preenchido. 
Lembrando que o centro de Custo não é obrigatório. 
Tabela física (ECF_CLC_CIB_CALCMEM)

Caso não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

93072 “Conta Contábil/Centro de Custo informados não estão registrados como Detalhamento do Lançamento Parte A (M300,M350) da Apuração ECF.”


Regras Gravação do Lançamento Contábil – Parte A (M312/M362)


RN18 – Gravação do Lançamento Contábil – Parte A (M312/M362)

Após o registro foco da importação ser validado, gravá-lo na tabela X256_LANCTO_PA:
  IDT_X256_LANCTO_PA:   sequence SEQ_X256_LANCTO_PA
  IDT_CLC_CIB_CALCMEM:  identificador do registro pai
                        Detalhamento Conta Contábil/Centro de Custo (ECF_CLC_CIB_CALCMEM)
  COD_EMPRESA           : campo do layout da SAFX256
  COD_ESTAB             : campo do layout da SAFX256
  DATA_LANCTO           : campo do layout da SAFX256
  IDENT_CONTA           : Idenficador da X2002_PLANO_CONTAS recuperado com o GRUPO_CONTA, 
                          COD_CONTA considerando a DATA_LANCTO como referência.
  IND_DEB_CRE           : campo do layout da SAFX256
  ARQUIVAMENTO          : campo do layout da SAFX256
  GRUPO_CONTA           : Grupo recuperado considerando a DATA_LANCTO como referência. 
  COD_CONTA             : campo do layout da SAFX256
  GRUPO_CUSTO           : Grupo recuperado considerando a DATA_LANCTO como referência.  COD_CUSTO               : campo do layout da SAFX256
  IDENT_CUSTO           : Idenficador da X2003_CENTRO_CUSTO recuperado com o GRUPO_CUSTO, 
                          COD_CUSTO considerando a DATA_LANCTO como referência.
  GRUPO_HISTPADRAO      : campo GRUPO_HISTPADRAO da X2020_HIST_PADRAO a partir do 
                          IDENT_HISTPADRAO da X01_CONTABIL
  COD_HISTPADRAO        : campo COD_HISTPADRAO da X2020_HIST_PADRAO a partir do 
                          IDENT_HISTPADRAO da X01_CONTABIL
  DESC_HISTPADRAO       : campo DESCRICAO da X2020_HIST_PADRAO a partir do IDENT_HISTPADRAO 
                          da X01_CONTABIL
  IDENT_HISTPADRAO      : IDENT_HISTPADRAO da X01_CONTABIL
  TXT_HISTCOMPL         : TXT_HISTPADRAO da X01_CONTABIL
  NUM_LANCAMENTO        : NUM_LANCAMENTO da X01_CONTABIL
  VLR_LANCTO            : VALOR_LANCTO da X01_CONTABIL
  IDT_CLC_ICT_BKKPING   : identificador do registro da Escrituração (ecf_clc_ict_bkkping)
  IDT_CLC_OP_CALCTION   : identificador do registro da Abertura Apuração 
                          (ecf_clc_op_calction)
  IDT_CLC_ITEM_BAL      : identificador do registro de Lançamento Parte A(ECF_CLC_ITEM_BAL)
  NUM_PROCESSO          : numero do processo da importação
  IND_GRAVACAO          : preencher com 1 ou 2.
                        A lista de valores completo deste campo conforme padrão DW é:
1.  Incluído por Importação
2.  Atualizado por Importação
3.  Incluído por Importação / Atualizado por Digitação
4.  Incluído por Digitação
5.  Incluído por Digitação / Atualizado por Digitação
6.  Gerado pelo Sistema
7.  Gerado pelo Sistema  / Atualizado por Digitação
8. Gerado pelo Sistema  / Atualizado por Importação
O valor 8 foi criado na OS2388-AA, A4, e somente está considerado nas importações das SAFX112 e SAFX113.


Procedimentos para Atualização do Lançamento Parte A (M300/M350) - ECF:

As regras descritas neste tópico se referem as mesmas atualizações executadas na tela “Lançamentos da Parte A (M300, M350)” do módulo ECF.

Este procedimento deve ser executado ao final da importação do arquivo SAFX, caso pelo menos um registro de “Lançamento Contábil – Parte A (M312/M362)” seja importado com sucesso.

Recuperar os registros de Lançamentos Contábeis – Parte A (M312/M362) importados com sucesso na tabela X256_LANCTO_PA. Identificá-los pelo número do processo. Em seguida recuperar os registros “pai” de “Detalhamento por Conta Contábil/Centro dos Lançamentos Parte A (M300, M350)” na tabela ECF_CLC_CIB_CALCMEM. Efetuar os procedimentos:
4.1) Recalcular o “Valor Total” do registro pai de “Detalhamento por Conta Contábil/Centro dos Lançamentos Parte A (M300, M350)” no resultado da Apuração. ( HYPERLINK  \l "_RN19_–_Atualização" RN19)

4.2) Recalcular os valores “Lançamentos/Ajutes” e “Valor a Considerar” do registro pai “Detalhamento por Conta Contábil/Centro dos Lançamentos Parte A (M300, M350)” no resultado da Apuração. ( HYPERLINK  \l "_RN20_–_Atualização" RN20)

Após atualizar todos os Detalhamentos por Conta Contábil/Centro de um Registro/Linha nos Lançamentos Parte A (M300, M350), efetuar:
4.3) Recalcular os valores “Somatório de Contas Contábeis” e “Valor (Parte A)” do “Registro/Linha nos Lançamentos Parte A (M300, M350)” no resultado da Apuração. ( HYPERLINK  \l "_RN21_–_Atualização" RN21)

Ao final efetuar:
4.4) Atualizar o Status da Apuração para “Alteração Manual Realizada”.( HYPERLINK  \l "_RN22_–_Atualização" RN22)


RN19 – Atualização do “Valor Total” do Detalhamento por Conta Contábil/Centro nos Lançamentos Parte A (M300, M350): 

<<Regra definida a partir do funcionamento da tela manutenção.
Baseada passo 5.2 do FB – Manter Contas Contábeis – ABA Conta Contábil>>

Atualizar o campo do Detalhamento Conta Contábil/Centro de Custo (ECF_CLC_CIB_CALCMEM):
Valor Total (CUR_LANCTO_PA/ IND_LANCTO_PA)

Regra: 
Ler os Lançamentos Contábeis – Parte A (M312/M362) gravados na tabela X256_LANCTO_PA relacionados ao registro de Detalhamento de Conta Contábil/Centro de Custo. 
Totalizar o campo VLR_LANCTO da tabela X256_LANCTO_PA somando ou subtraindo o valor de acordo com o IND_DEB_CRED.
Gravar os campos na ECF_CLC_CIB_CALCMEM:
CUR_LANCTO_PA = valor absoluto resultante da totalização. 
IND_LANCTO_PA = indicador de débito/crédito resultante.


RN20 – Atualização do “Valor do Lançamentos/Ajuste” e “Valor a Considerar” do Detalhamento por Conta Contábil/Centro nos Lançamentos Parte A (M300, M350):

<<Regra definida a partir do funcionamento da tela manutenção.
Baseada passo 5.1 do FB – Manter Contas Contábeis – ABA Conta Contábil>>

Atualizar os campos do Detalhamento Conta Contábil/Centro de Custo (ECF_CLC_CIB_CALCMEM):
Valor do Lançamento/Ajuste (CUR_ACCOUNT_ENTRIES / IND_ACCOUNT_ENTRIES)
Valor a Considerar (CUR_FINAL_BALANCE / IND_FINAL_BALANCE)
Ind_dig_calc

Regra: 
Aplicar a RN23 da “ETEC – Transcricao de Valores – ECF – regras.doc”.
Esta regra está implementada na procedure Valor_lcto_ajuste da package ECF_LANCTO_PARTE_A.
Gravar os campos na tabela ECF_CLC_CIB_CALCMEM.


RN21 – Atualização do Registro/Linha Lançamento Parte A (M300, M350) 

<<Regra definida a partir do funcionamento da tela manutenção.
Baseada no passo 1 do FB – Fluxo de Atualização do Lançamento Parte A (ECF_CLC_ITEM_BAL) pelos Detalhamentos>>

Atualizar os campos do Registro/Linha Lançamento Parte A (ECF_CLC_ITEM_BAL):
Somatório das Contas da Parte B
Somatório das Contas Contábeis
Valor (da parte A)*
Tipo de Relacionamento
“Exibição do conteúdo do campo Valor”
Regra: 
Aplicar a RN24 da “ETEC – Transcricao de Valores – ECF – regras.doc”.
Esta regra está implementada na procedure recalc_campos_parte_a_b da package ECF_LANCTO_PARTE_A. Chamar passando o parâmetro de entrada PROC_ID nulo!
Atualizar o registro do Lançamento Parte A (M300/M350) na tabela ECF_CLC_ITEM_BAL:
Campos da ECF_CLC_ITEM_BAL	Regra de Preenchimento		CUR_FINAL_BALANCE	Preencher com o conteúdo do campo “Valor (da parte A)”.		CUR_PB_M300_M350	Preencher com o conteúdo do campo Somatório das Contas da Parte B		CUR_CTA_M300_M350	Preencher com o conteúdo do campo Somatório das Contas Contábeis		IND_RELATIONSHIP	Preencher com o conteúdo do campo “Tipo de Relacionamento”		IND_DISPLAY_FINAL_BAL	Preencher com o conteúdo do campo “Exibição do conteúdo do campo Valor”		IND_BALANCE_DETAIL	Preencher com: ‘LANCAMENTO-PARTE-A’ 		DSC_HISTORIC	Não atualizar, para manter o histórico digitado via tela.		IND_DIG_CALC	Não atualizar.		

RN22 – Atualização do Status Apuração

(Regra definida a partir do funcionamento da tela manutenção)
<<Regra definida a partir do funcionamento da tela manutenção.
Baseada no passo 1 do FB – Fechar Tela>>

Atualizar o campo COD_STS_OP_CALCTION da ECF_CLC_OP_CALCTION da apuração em foco, para “ALTERACAOMANUALREALIZADA”, 

                                                              = = = = = / / / = = = = =