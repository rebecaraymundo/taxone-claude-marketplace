# MTZ_Consolidação_de_documentos_de_Utilities

> Fonte: MTZ_Consolidação_de_documentos_de_Utilities.doc

THOMSON REUTERS

Módulo ICMS

Consolidação de Documentos de Utilities


DOCUMENTO DE REQUISITO

OS/CH	Nome	Descrição	Data		OS342	Vinicius Siani	OS – 342 – 05/2001 – SAFIC: Geração dos Mapas Resumo de Documentos Fiscais de Telecom
	01/05/2001
(criação do documento)		MFS83772	Rogério Ohashi	Inclusão do campo de valor de FECP na Consolidação dos documentos de Utilities, no DE/PARA x43/08.	01/04/2022		MFS85342	Rogério Ohashi	Readequação da regra dos campos VLR_BASE_ICMS_2 (Conforme regra CST 40/Cclass 560) e Campo VLR_CONTAB_ITEM, referente ao cálculo de abatimento dos campos de Valor de Serviço/energia injetada e/ou Outras deduções (Regra Campo 05 do Registro C590 – Sped Fiscal.	03/05/2022		MFS94542	Rogério Ohashi	Tratamento para clientes equiparados em indústria que são obrigados a entregar as informações de IPI, readequação para considerar o novo parâmetro “Preencher Base de IPI Outras”	08/10/2022		MFS432827	Liliane Assaf	O objetivo dessa MFS é atualizar as regras de preenchimento do Valor Contábil e do Valor do ICMS da Capa e do Item de Mercadoria das notas de Mapa Resumo geradas através da consolidação das notas de modelo 62 (NFCom), compatibilizando com as regras de geração dos registros D700 e D750 do Sped Fiscal.	09/10/2023		MFS788119	Andréa Rocha	Alteração da regra de preenchimento do campo VLR_CONTAB_ITEM, de acordo com o parâmetro criado na tela de geração.  Essa regra está seguindo o que foi feito no SPED-EFD (Regra Campo 05 do Registro C590 – Sped Fiscal, para não considerar o valor de outras deduções	26/03/2025		MFS875520	Andréa Rocha	Alteração da regra de geração para permitir consolidar documentos fiscais de modelo igual a 62, sem o preenchimento do número do ciclo.	11/08/2025		

UPGs:  56
 
Descrição Geral: 

Geração dos Mapas Resumo de notas fiscais de saída (modelo 22, 62) de telecom a partir das tabelas X42_CAPA_TELECOM e X43_ITEM_TELECOM, sendo estes gravados nas tabelas X07_DOCTO_FISCAL, X08_ITENS_MERC, X08_TRIB_MERC, X08_BASE_MERC, DWT_DOCTO_FISCAL e DWT_ITENS_MERC (DATAMART);

OBS: Os livros P2 Convênio serão adaptados para exibir os mapas resumo com número de documento inicial e final na próxima UPG.

Cliente Solicitante: Vésper

Analista OS: Vinicius Siani

Responsável OS: Vinicius Siani

Responsável Power Builder: Marcelo Pessanha

Responsável Stored Procedure: Luciano Santos

Localização no Mastersaf:

-      ICMS: 	SAFIC

Funções no Menu:

Módulo: 	ICMS
Menu:		DATAMART => Consolidação de Documentos de UTILITIES

Procedimentos para os Usuários:

Módulo: 	DW (SAFDW) 
Menu: 		Manutenção => Cadastros => Estabelecimento X Pessoa Física Jurídica:
Procedimento:	Cadastrar pessoa fís./jur. relativa ao estabelecimento.

Módulo: 	DW (SAFDW) 
Menu: 		Manutenção => Códigosos => Unidades de Medida:
Procedimento:	Cadastrar unidade de medida a ser utilizada para gravação dos mapas resumo.

Módulo: 	DW (SAFDW) 
Menu: 		Manutenção => Códigosos => Unidades Padrão:
Procedimento:	Cadastrar unidade padrão a ser utilizada para gravação dos mapas resumo.

Módulo: ICMS(SAFIC) 
Menu:   DATAMART => Consolidação de Documentos de UTILITIES – Neste item o usuário poderá gerar os mapas resumo de TELECOM passando os estabelecimentos desejados, mês/ano, ciclo de faturamento, unidade padrão e unidade de medida.
OBS: A leitura se dará a partir das tabelas de documentos fiscais de TELECOM (SAFX42/43) e a gravação dos mapas será realizada nas tabelas de documentos fiscais padrão(SAFX07/08).

Procedimentos para Interface:

Não existem procedimentos para interface.


Procedimentos para Informação:

1.  Atualizar o Help do módulo segundo funcionamento descrito nesta OS;


Procedimentos para os DBAs:

1-TABELA ICT_LVR_P1_M2_UF      Capa de detalhes de NF Telecom
CRIAÇÃO DE COLUNA

COLUNA		TIPO/TAM        	(*)NÃO NULO 
NUM_DOCFIS_FIM		VARCHAR2(12)

2-TABELA ICT_LVR_P1A_M2_UF      Capa de detalhes de NF Telecom
CRIAÇÃO DE COLUNA

COLUNA		TIPO/TAM        	(*)NÃO NULO 
NUM_DOCFIS_FIM		VARCHAR2(12)

3-TABELA ICT_LVR_P2_M2_UF      Capa de detalhes de NF Telecom
CRIAÇÃO DE COLUNA

COLUNA		TIPO/TAM        	(*)NÃO NULO 
NUM_DOCFIS_FIM		VARCHAR2(12)

4-TABELA ICT_LVR_P1_M2           Capa de detalhes de NF Telecom
CRIAÇÃO DE COLUNA

COLUNA		TIPO/TAM        	(*)NÃO NULO 
NUM_DOCFIS_FIM		VARCHAR2(12)

5-TABELA ICT_LVR_P1A_M2        Capa de detalhes de NF Telecom
CRIAÇÃO DE COLUNA
COLUNA		TIPO/TAM        	(*)NÃO NULO 
NUM_DOCFIS_FIM		VARCHAR2(12)

6-TABELA ICT_LVR_P2_M2          Capa de detalhes de NF Telecom
CRIAÇÃO DE COLUNA

COLUNA		TIPO/TAM        	(*)NÃO NULO 
NUM_DOCFIS_FIM		VARCHAR2(12)

7-TABELA ICT_CONF_ERR_TELE	(erros encontrados no documento)
CRIAÇÃO DE TABELA
PRIMARY KEY: PK_ICT_CON_ER_TELE
COLUNA		TIPO/TAM        	(*)NÃO NULO/PK

 USUARIO                         		VARCHAR2(40)	*
 SEQ_REG                         		NUMBER(12)	*
 COD_ERRO                        		NUMBER(6)	*

8-TABELA ICT_CAD_ERR_TELE	(erros a verificar no documento)
CRIAÇÃO DE TABELA
PRIMARY KEY: PK_ICT_CAD_ER_TELE
COLUNA		TIPO/TAM        	(*)NÃO NULO/PK

 USUARIO                         		VARCHAR2(40)	*
 COD_ERRO                        		NUMBER(6)	*


9-TABELA ICT_CONF_TELE	(documentos consistidos em relação aos erros)
CRIAÇÃO DE TABELA
PRIMARY KEY: PK_ICT_CONF_TELE
COLUNA		TIPO/TAM        	(*)NÃO NULO	PK

 USUARIO                         		VARCHAR2(40)	*		*
 COD_EMPRESA                     	VARCHAR2(3)	*		*
 COD_ESTAB                       	 	VARCHAR2(6)	*		*
 DATA_FISCAL                     		DATE		*		*
 COD_FIS_JUR                     		VARCHAR2(14)	*		*
 NUM_DOCFIS                      		VARCHAR2(12)	*		*
 SERIE_DOCFIS                    		VARCHAR2(3)	*		*
 SUB_SERIE_DOCFIS                	VARCHAR2(2)	*		*
 NUM_ITEM                                 	NUMBER(5)	*		*
 COD_CFO                                  	VARCHAR2(4)
 SITUACAO                        		CHAR(1)	*
 VLR_SERVICO                              	NUMBER(17,2)
 VLR_TOT_NOTA                             	NUMBER(17,2)
 VLR_OUTRAS_DESP                          	NUMBER(17,2)
 VLR_ABAT_DEDUCAO                        NUMBER(17,2)
 VLR_TOT_PAGAR                            	NUMBER(17,2)
 VLR_ICMS_B1                              	NUMBER(17,2)
 VLR_ICMS_B2                              	NUMBER(17,2)
 VLR_ICMS_B3                              	NUMBER(17,2)
 VLR_ICMS_B4                              	NUMBER(17,2)
 VLR_ICMS_TRIB                            	NUMBER(17,2)
 VLR_ICMS_ALIQ                            	NUMBER(7,4)
 VLR_BASE_ICMS_DEST                      NUMBER(7,4)
 VLR_TRIB_ICMS_DEST                       NUMBER(7,4)
 VLR_ALIQ_ICMS_DEST                       NUMBER(7,4)
 VLR_SUBST_TRIB                           	NUMBER(17,2)
 VLR_BASE_SUB_TRIB                        	NUMBER(17,2)
 VLR_BASE_ISS                             	NUMBER(17,2)
 VLR_ALIQ_ISS                             	NUMBER(17,2)
 VLR_ISS                                  	NUMBER(17,2)
 VLR_DESC_COND                            	NUMBER(17,2)
 SEQ_REG                         		NUMBER(12)	*
 COD_PRODUTO                                   VARCHAR2(60)
 COD_ESTADO                                      VARCHAR2(2)
 VLR_CONT_ITEM                                NUMBER(17,2)
 VLR_CONT_ITEM_TOT                       NUMBER(17,2)
 VLR_CONT_ICMS                                NUMBER(17,2)
 VLR_CONT_ICMS_TOT                       NUMBER(17,2)
 VLR_ADIC_DESC                                 NUMBER(17,2)
 VLR_SERVICO_TOT                            NUMBER(17,2)


10-TABELA ICT_CONF_DF          	Tabela de relatório de conferência de ICMS/IPI
CRIAÇÃO DE COLUNA

COLUNA		TIPO/TAM        	(*)NÃO NULO 
NUM_DOCFIS_FIM		VARCHAR2(12)

Procedimentos Operacionais:

0. Pré-requisitos para processamento

Módulo: 	DW (SAFDW) 
Menu: 		Manutenção => Códigosos => Unidades de Medida:
Procedimento:	Cadastrar unidade de medida a ser utilizada para gravação dos mapas resumo.

Módulo: 	DW (SAFDW) 
Menu: 		Manutenção => Códigosos => Unidades Padrão:
Procedimento:	Cadastrar unidade padrão a ser utilizada para gravação dos mapas resumo.


Módulo: 	DW (SAFDW) 
Menu: 		Manutenção => Cadastros => Estabelecimento X Pessoa Física Jurídica:
Procedimento:	Cadastrar pessoa fís./jur. relativa ao estabelecimento.

1. Geração de Mapas Resumo – TELECOM

Módulo: 	ICMS (SAFIC) 
Menu: 		DATAMART => Consolidação de Documentos de UTILITIES:
PowerBulider:
Desenvolver tela para chamada da procedure de geração dos mapas resumo oferecendo opção de seleção de todos os estabelecimentos para os quais o usuário tenha permissão no PowerLock, mês/ano relativa a geração dos mapas resumo;

Desenvolver opção de se especificar o ciclo de faturamento que será gerado. Caso um ciclo seja escolhido, apenas este será gerado, caso nenhum ciclo seja especificado, serão gerados os mapas relativos a todos os ciclos do mês.
OBS: O ciclo é numérico de 2 posições, pode ser preenchido ou deixado nulo para realização da geração;

Desenvolver duas pastas para recuperar respectivamente o CÓDIGO DE MEDIDA e o CÓDIGO DE UNIDADE PADRÃO que deverão ser utilizados nos mapas (resumo) para fins de IN68.
OBS: Estas pastas não deverão permitir digitação devido ao problema que isto poderá causar na recuperação dos grupos, pois neste momento ainda não temos data definida e podemos estar trabalhando com mais de um estabelecimento.

Desenvolver opção relativa a inicialização (relacionada ao parâmetro IND_EXCL_DIG):
(Check box) - Excluir registros digitados (‘S’ ou ‘N’)

Desenvolver chamada da procedure SAF_ICMS_MAPA_RES passando os seguintes parâmetros:
IN – COD_EMPRESA	VARCHAR2
IN – COD_ESTAB	VARCHAR2
IN – MES		NUMBER
IN – ANO 		NUMBER
IN – CICLO 		NUMBER
IN – IND_EXCL_DIG	VARCHAR2
IN – COD_MEDIDA 	VARCHAR2
IN – COD_UND_PADR 	VARCHAR2
IN – USUARIO 		VARCHAR2
IN – NUM_PROCESSO	NUMBER

OUT – STATUS		NUMBER

[MFS875520] Permitir fazer a consolidação para notas fiscais de modelo 62 que não tenha o ciclo preenchido

Stored Procedure
Desenvolver procedure acima citada seguindo os seguintes passos:

Gravar warnings relativos a registros com dados inconsistentes nas tabelas de TELECOM no período:
X43_ITEM_TELECOM.IDENT_CFO não preenchido em notas não canceladas;
X43_ITEM_TELECOM.IDENT_PRODUTO não preenchido em notas não canceladas;
X42_CAPA_TELECOM que não tenha item vinculado em notas não canceladas;
X42_CAPA_TELECOM.NUM_CICLO não preenchido em notas não canceladas e modelo diferente de 62;

Recuperar da tabela DWT_PFJ_ESTAB a pessoa física jurídica referente ao estabelecimento:
Esta será utilizada como pessoa fís./jur. nos mapas resumo;

Controle de concorrência - Inicialização: conforme procedure de geração de notas fiscais de transferência de crédito.

Inicializar registros de mapas resumo na base de documentos fiscais na seguinte ordem:
X07_BASE_DOCFIS, 
X07_CUPOM_FISCAL, 
X07_TRIB_DOCFIS, 
X08_BASE_MERC, 
X08_TRIB_MERC, 
X08_ITENS_MERC, 
X07_DOCTO_FISCAL

Critérios:
Se IND_EXCL_DIG = ‘N’
    X07_DOCTO_FISCAL.IDENT_MODELO	=> correspondente a 
             X2024_MODELO_DOCTO.COD_MODELO = 22;
    X07_DOCTO_FISCAL.DATA_FISCAL 	=> dentro do mês em questão;
    X07_DOCTO_FISCAL.MOVTO_E_S 	=> ‘9’;
    X07_DOCTO_FISCAL.IND_GRAVACAO	=> ‘6’;
    X07_DOCTO_FISCAL.IDENT_DOCTO	=> correspondente a 
             X2005_TIPO_DOCTO.COD_DOCTO = ‘NFST’;

Se IND_EXCL_DIG = ‘S’
    X07_DOCTO_FISCAL.IDENT_MODELO	=> correspondente a 
             X2024_MODELO_DOCTO.COD_MODELO = 22;
    X07_DOCTO_FISCAL.DATA_FISCAL 	=> dentro do mês em questão;
    X07_DOCTO_FISCAL.MOVTO_E_S 	=> ‘9’;
    X07_DOCTO_FISCAL.IDENT_DOCTO	=> correspondente a 
             X2005_TIPO_DOCTO.COD_DOCTO = ‘NFST’;

Ler X42_CAPA_TELECOM para determinação dos intervalos de notas que compõem cada mapa resumo segundo os seguintes critérios:
Ordenação por:
- NUM_CICLO (Considerar número do ciclo sem preenchimento p/ NF modelo 62)
- SERIE_DOCFIS
- SUB_SERIE_DOCFIS
- NUM_DOCFIS

Quebra por:
- NUM_CICLO (Considerar número do ciclo sem preenchimento p/ NF modelo 62)
- SERIE_DOCFIS
- SUB_SERIE_DOCFIS
- SITUACAO = ‘S’ 
 A cada quebra encontrada, será determinado o intervalo como:
 num_docfis_ini: 1o documento posterior a quebra anterior;
 num_docfis_fim: último documento antes da quebra;
 OBS: A existência de um documento cancelado determina uma quebra. O documento cancelado não
 fará parte de nenhum mapa e constituirá um documento normal a ser gerado na base fiscal (X07);
 OBS2: Caso a seqüência das notas seja quebrada, também será feita a quebra dos mapas;

Exemplo(NFs – X42 e X43    X     Mapas – X07 e X08):
NFs:
Num Ciclo	Série	S-Série	NumDocfis	Situação
01		A		1		N
01		A		2		N
01		A		3		S
01		A		4		N
01		A		5		N
02		A		6		N
02		A		7		N
02		A		9		N
02		A		10		N
02		B		11		N
02		B		12		N
02		B		15		N
 
Mapas:
Num Ciclo	Série	S-Série	NumDocfisINI	NumDocfisFIM
01		A		1		2		(mapa, quebra próx Nf cancelada)
01		A		3		(nota, cancelada)
01		A		4		5		(mapa, quebra próx Nf outro ciclo)
02		A		6		7		(mapa, quebra próx Nf fora sequencia)
02		A		9		10		(mapa, quebra próx Nf outra série)
02		B		11		12		(mapa, quebra na seqüência de Nfs)
02		B		15		15		(mapa, fim do movimento)

De / Para (X42 p/ X07):

DWT_DOCTO_FISCAL	X07_DOCTO_FISCAL/ X07_TRIB_DOCFIS/   X07_BASE_DOCFIS	X42_CAPA_TELECOM /             VALORES FIXOS		IDENT_DOCTO_FISCAL             	---	Recuperação do próximo ident a ser utilizado da tabela IDENT_SUBSTITUTO		 COD_EMPRESA                    	COD_EMPRESA	COD_EMPRESA		 COD_ESTAB 	COD_ESTAB	COD_ESTAB		 DATA_FISCAL                    	DATA_FISCAL	DAT_FISCAL (de uma das notas do ciclo, todas têm a mesma data)
Obs.: NF de modelo 62 pode ter o ciclo não preenchido.		 MOVTO_E_S                      	MOVTO_E_S	‘9’		 NORM_DEV                       	NORM_DEV	‘1’		 IDENT_DOCTO                    	IDENT_DOCTO	X2005_TIPO_DOCTO.IDENT_DOCTO (o ident correspondente a maior data de  validade que seja menor ou igual à DATA_FISCAL para COD_DOCTO = ‘NFST’)		 IDENT_FIS_JUR                  	IDENT_FIS_JUR	Mapas resumo: X04_PESSOA_FIS_JUR.IDENT_FIS_JUR (o ident correspondente a maior data de validade que seja menor ou igual à DATA_FISCAL, correspondente à pessoa fís./jur. do estabelecimento – DWT_PFJ_ESTAB)

Notas canceladas: IDENT_FIS_JUR		 NUM_DOCFIS                     	NUM_DOCFIS	NUM_DOCFIS (número do documento fiscal inicial do mapa resumo ou número do documento fiscal da nota cancelada)		 NUM_DOCFIS_FIM           	NUM_DOCFIS_FIM	NUM_DOCFIS (número do documento fiscal final do mapa resumo ou nulo para nota cancelada)		 SERIE_DOCFIS                   	SERIE_DOCFIS	SERIE_DOCFIS		 SUB_SERIE_DOCFIS               	SUB_SERIE_DOCFIS	SUB_SERIE_DOCFIS		 DATA_EMISSAO                   	DATA_EMISSAO	DAT_FISCAL (de uma das notas do ciclo, todas têm a mesma data)
Obs.: NF de modelo 62 pode ter o ciclo não preenchido		 COD_CLASS_DOC_FIS              	COD_CLASS_DOC_FIS	‘3’		 IDENT_MODELO                   	IDENT_MODELO	X2024_MODELO_DOCTO.IDENT_MODELO (o ident correspondente a maior data de validade que seja menor ou igual à DATA_FISCAL para COD_MODELO = ‘22’)		 IDENT_CFO                      	IDENT_CFO	Mapas resumo: nulo
Notas canceladas: IDENT_CFO		 VLR_PRODUTO                    	VLR_PRODUTO	Mapas resumo: SOMA(VLR_SERVICO) de todos os documentos contidos no mapa resumo;

Notas canceladas: VLR_SERVICO		 VLR_TOT_NOTA                   	VLR_TOT_NOTA	Mapas resumo: SOMA(VLR_TOT_NOTA) de todos os documentos contidos no mapa resumo;

Notas canceladas: VLR_TOT_NOTA		 VLR_OUTRAS                     	VLR_OUTRAS	Mapas resumo: SOMA(VLR_OUTRAS_DESP) de todos os documentos contidos no mapa resumo;

Notas canceladas: VLR_OUTRAS_DESP		 VLR_DESCONTO                   	VLR_DESCONTO	Mapas resumo: SOMA(VLR_ABAT_DEDUC) de todos os documentos contidos no mapa resumo;

Notas canceladas: VLR_ABAT_DEDUC		 SITUACAO                       	SITUACAO	Mapas resumo: ‘N’
Notas canceladas: ‘S’		 IND_NF_ESPECIAL                	IND_NF_ESPECIAL	‘N’		 ALIQ_TRIBUTO_ICMS              	X07_TRIB_DOCFIS.ALIQ_TRIBUTO para
X07_TRIB_DOCFIS.COD_TRIBUTO = ‘ICMS’	Mapas resumo: 
   Dwt: 0
   X07: não gravar
Notas canceladas:VLR_ALIQ_ICMS 		 VLR_TRIBUTO_ICMS               	X07_TRIB_DOCFIS.VLR_TRIBUTO para
X07_TRIB_DOCFIS.COD_TRIBUTO = ‘ICMS’	Mapas resumo: 
   Dwt: 0
   X07: não gravar
Notas canceladas:VLR_TRIB_ICMS		 VLR_TRIBUTO_ICMSS              	X07_TRIB_DOCFIS.VLR_TRIBUTO para
X07_TRIB_DOCFIS.COD_TRIBUTO = ‘ICMS-S’	Mapas resumo: 
   Dwt: 0
   X07: não gravar
Notas canceladas:VLR_SUBST_TRIB		 VLR_BASE_ICMS_1                	X07_BASE_DOCFIS.VLR_BASE para
X07_BASE_DOCFIS.COD_TRIBUTO = ‘ICMS’ e
X07_BASE_DOCFIS.COD_TRIBUTACAO = 1	Mapas resumo: 
   Dwt: 0
   X07: não gravar
Notas canceladas: VLR_BASE_ICMS_1		 VLR_BASE_ICMS_2                	X07_BASE_DOCFIS.VLR_BASE para
X07_BASE_DOCFIS.COD_TRIBUTO = ‘ICMS’ e
X07_BASE_DOCFIS.COD_TRIBUTACAO = 2	Mapas resumo: 
   Dwt: 0
   X07: não gravar
Notas canceladas: VLR_BASE_ICMS_2		 VLR_BASE_ICMS_3                	X07_BASE_DOCFIS.VLR_BASE para
X07_BASE_DOCFIS.COD_TRIBUTO = ‘ICMS’ e
X07_BASE_DOCFIS.COD_TRIBUTACAO = 3	Mapas resumo: 
   Dwt: 0
   X07: não gravar
Notas canceladas: VLR_BASE_ICMS_3		 VLR_BASE_ICMS_4                	X07_BASE_DOCFIS.VLR_BASE para
X07_BASE_DOCFIS.COD_TRIBUTO = ‘ICMS’ e
X07_BASE_DOCFIS.COD_TRIBUTACAO = 4	Mapas resumo: 
   Dwt: 0
   X07: não gravar
Notas canceladas: VLR_BASE_ICMS_4		 VLR_BASE_ICMSS                 	X07_BASE_DOCFIS.VLR_BASE para
X07_BASE_DOCFIS.COD_TRIBUTO = ‘ICMS-S’ e
X07_BASE_DOCFIS.COD_TRIBUTACAO = 1	Mapas resumo: 
   Dwt: 0
   X07: não gravar
Notas canceladas:VLR_BASE_SUB_TRIB		 NUM_PROCESSO                   	NUM_PROCESSO	Número do processo de geração dos mapas resumo.		 IND_GRAVACAO                   	IND_GRAVACAO	‘6’		 IND_TRANSF_CRED                	IND_TRANSF_CRED	‘0’		 IND_CRED_ICMSS 	IND_CRED_ICMSS	‘S’		 BASE_ICMS_ORIGDEST             	BASE_ICMS_ORIGDEST	0		 VLR_ICMS_ORIGDEST              	VLR_ICMS_ORIGDEST	0		 ALIQ_ICMS_ORIGDEST             	ALIQ_ICMS_ORIGDEST	0		 VLR_DESC_CONDIC                	VLR_DESC_CONDIC	Mapas resumo: SOMA(VLR_DESC_COND) de todos os documentos contidos no mapa resumo;

Notas canceladas: VLR_DESC_COND		OBS: Na tabela DWT_DOCTO_FISCAL, todos os campos de valor não citados deverão receber valor 0(zero).		

Conforme DE PARA acima:
Gravação das tabelas X07_DOCTO_FISCAL, DWT_DOCTO_FISCAL relativas aos mapas resumo;
Gravação das tabelas X07_DOCTO_FISCAL, X07_TRIB_DOCFIS, X07_BASE_DOCFIS,  DWT_DOCTO_FISCAL relativas às notas canceladas; 

Totalização e gravação dos itens de mercadoria (X08_ITENS_MERC, X08_TRIB_MERC, X08_BASE_MERC, DWT_ITENS_MERC) para cada mapa resumo existente (NUM_CICLO, SERIE_DOCFIS, SUB_SERIE_DOCFIS, NUM_DOCFIS_INI, NUM_DOCFIS_FIM):
OBS: Notas fiscais canceladas não terão estas tabelas gravada!!! Considerar número do ciclo sem preenchimento p/ NF modelo 62.

Tabelas relacionadas:
X42_CAPA_TELECOM
X43_ITEM_TELECOM
X2013_PRODUTO
X2012_COD_FISCAL

Quebras por:
GRUPO/IND/COD_PRODUTO (X2013)
COD_CFO (X2012)
VLR_ALIQ_ICMS (X43)
OBS: Dentro de um mesmo mapa resumo a variação de qq um destes elementos ocasionará a gravação de um novo item.

[ALTERAÇÃO- MFS83772] Inclusão dos Campos de Valores de FECP e Alíquota FECP

De Para (X43 / X08):

DWT_ITENS_MERC	X08_ITENS_MERC /        X08_TRIB_MERC /          X08_BASE_MERC 	X43_ITEM_TELECOM / 
VALORES FIXOS 		 IDENT_DOCTO_FISCAL  	---	Recuperação do próximo ident a ser utilizado da tabela IDENT_SUBSTITUTO 		 IDENT_ITEM_MERC          	---	Incrementado na própria geração a cada novo item criado para um mapa resumo.		 COD_EMPRESA                 	 COD_EMPRESA                 	COD_EMPRESA		 COD_ESTAB                      	 COD_ESTAB                      	COD_ESTAB		 DATA_FISCAL                    	 DATA_FISCAL                    	DAT_FISCAL (de uma das notas do ciclo, todas têm a mesma data)
Obs.: NF de modelo 62 pode ter o ciclo não preenchido		 MOVTO_E_S                      	 MOVTO_E_S                      	‘9’		 NORM_DEV                       	 NORM_DEV                       	‘1’		 IDENT_DOCTO                    	 IDENT_DOCTO                    	X2005_TIPO_DOCTO.IDENT_DOCTO (o ident correspondente a maior data de validade que seja menor ou igual à DATA_FISCAL para COD_DOCTO = ‘NFST’)		 IDENT_FIS_JUR                  	 IDENT_FIS_JUR                  	Mapas resumo: X04_PESSOA_FIS_JUR.IDENT_FIS_JUR (o ident correspondente a maior data de validade que seja menor ou igual à DATA_FISCAL, correspondente à pessoa fís./jur. do estabelecimento – DWT_PFJ_ESTAB)

Notas canceladas: IDENT_FIS_JUR		 NUM_DOCFIS                     	 NUM_DOCFIS                     	NUM_DOCFIS (número do documento fiscal inicial do mapa resumo ou número do documento fiscal da nota cancelada)		 SERIE_DOCFIS                   	 SERIE_DOCFIS                   	SERIE_DOCFIS		 SUB_SERIE_DOCFIS            	 SUB_SERIE_DOCFIS            	SUB_SERIE_DOCFIS		 DISCRI_ITEM                    	 DISCRI_ITEM                    	IDENT_PRODUTO (preenchido c/zeros a esquerda até a 12a posição) +
NUM_ITEM (preenchido c/zeros a esquerda até a 5a posição) +
8 espaços (no lugar onde deveria estar gravado o COD_UND_PADRAO)
		 IDENT_PRODUTO              	 IDENT_PRODUTO              	X2013_PRODUTO.IDENT_PRODUTO (o ident correspondente a maior data de validade que seja menor ou igual à DATA_FISCAL para GRUPO/IND/COD_PRODUTO correspondentes ao produto em questão no mapa resumo)		 NUM_ITEM                       	 NUM_ITEM                       	Incrementado na própria geração a cada novo item criado para um mapa resumo.		 IDENT_CFO                      	 IDENT_CFO                      	X2012_COD_FISCAL.IDENT_CFO (o ident correspondente a maior data de validade que seja menor ou igual à DATA_FISCAL para COD_CFO correspondente ao CFO em questão no mapa resumo)		 VLR_ITEM                       	 VLR_ITEM                       	SOMA(VLR_SERVICO) de todos os registros da tabela X43_ITEM_TELECOM relativos a este item do mapa resumo)		 VLR_DESCONTO             	 VLR_DESCONTO             	 SOMA(VLR_DESCONTO) de todos os registros da tabela X43_ITEM_TELECOM relativos a este item do mapa resumo)		 ALIQ_TRIBUTO_ICMS          	 ALIQ_TRIBUTO_ICMS          	VLR_ALIQ_ICMS		 VLR_TRIBUTO_ICMS             	 VLR_TRIBUTO_ICMS             	MFS432827: NFCOM
Se o Campo “13-Modelo de Documento” da tabela SAFX42 (X42_capa_telecom)  for igual à ‘62’;
   Se o Campo IND_ADIC_DESC for igual à ‘D’;
     E se o campo de CST_ICMS for igual à ‘00’,’10’,’20’,’70’:
           O sistema deverá utilizar a soma dos campos
           [22-Valor ICMS] + [103-FECEP ICMS] do Item para 
           subtrair do valor total do Campo VLR_TRIBUTO_ICMS.
   Senão 
       Se o campo de CST_ICMS for igual à ‘00’,’10’,’20’,’70’:
           O sistema deverá utilizar a soma dos campos
           [22-Valor ICMS] + [103-FECEP ICMS] do Item para
           somar ao valor total do Campo VLR_TRIBUTO_ICMS.
Senão
   Se o Campo IND_ADIC_DESC for igual à ‘D’;
           O sistema deverá utilizar o campo [22-Valor ICMS] 
          do Item para subtrair do valor total a ser gerado no 
          Campo VLR_TRIBUTO_ICMS.
   Senão 
           O sistema deverá utilizar o campo [22-Valor ICMS] 
          do Item para somar ao valor total a ser gerado no 
          Campo VLR_TRIBUTO_ICMS.
Somar todos os registros da tabela X43_ITEM_TELECOM relativos a este item do mapa resumo)		 VLR_TRIBUTO_ICMSS             	 VLR_TRIBUTO_ICMSS             	 SOMA(VLR_SUBST_TRIB) de todos os registros da tabela X43_ITEM_TELECOM relativos a este item do mapa resumo)		 VLR_BASE_ICMS_1                	 VLR_BASE_ICMS_1                	SOMA(VLR_BASE_ICMS_1) de todos os registros da tabela X43_ITEM_TELECOM relativos a este item do mapa resumo)		 VLR_BASE_ICMS_2  

              	 VLR_BASE_ICMS_2    

            	SOMA(VLR_BASE_ICMS_2) de todos os registros da tabela X43_ITEM_TELECOM relativos a este item do mapa resumo).
Ou
[MFS85342] 
 
Para as notas de saída de Modelo 66 com Situação Tributária B = 00 e Grupo cClass NF3e = 560:

Se data_fiscal  >= 01/01/2022 (X42_CAPA_TELECOM)
E Modelo do documento da X42_CAPA_TELECOM (COD_MODELO) igual à ‘66’
  E Situação Tributária B da X43_ITEM_TELECOM (COD_SIT_TRIB_B) igual à ‘00’
    E Grupo cClass NF3e da X43_ITEM_TELECOM (COD_GRUPO_CCLASS) igual à ‘560’

SOMA(VLR_BASE_ICMS_1) de todos os registros da tabela X43_ITEM_TELECOM relativos a este item do mapa resumo).
		 VLR_BASE_ICMS_3                	 VLR_BASE_ICMS_3 	SOMA(VLR_BASE_ICMS_3) de todos os registros da tabela X43_ITEM_TELECOM relativos a este item do mapa resumo)		 VLR_BASE_ICMS_4                	 VLR_BASE_ICMS_4                	SOMA(VLR_BASE_ICMS_4) de todos os registros da tabela X43_ITEM_TELECOM relativos a este item do mapa resumo)		 VLR_BASE_ICMSS                 	 VLR_BASE_ICMSS                 	SOMA(VLR_BASE_SUB_TRIB) de todos os registros da tabela X43_ITEM_TELECOM relativos a este item do mapa resumo)		VLR_BASE_IPI_3	X08_BASE_DOCFIS.VLR_BASE para
X08_BASE_DOCFIS.COD_TRIBUTO = ‘IPI’ e
X08_BASE_DOCFIS.COD_TRIBUTACAO = 3	Mapas resumo:
- Se o parâmetro “Tratamento  p/ Clientes Equiparados a Industria (Base IPI Outras)”,  estiver marcado:
SOMA(VLR_SERVICO) de todos os registros da tabela X43_ITEM_TELECOM relativos a este item do mapa resumo);
- Se o parâmetro “Tratamento  p/ Clientes Equiparados a Industria (Base IPI Outras)”,  estiver desmarcado:
      Não preencher		NUM_PROCESSO                   	 NUM_PROCESSO                   	Número do processo de geração dos mapas resumo.		IND_GRAVACAO                   	 IND_GRAVACAO                   	‘6’		VLR_CONTAB_ITEM               	 VLR_CONTAB_ITEM               	[MFS85342] 
[MFS788119] Alteração do cálculo para desconsiderar o valor de Outras Deduções, de acordo com o parâmetro criado em tela “Desconsiderar Vlr Outras Deduções p/ cálculo do Vlr Operação dos registros C590/C790”.
MFS820156] Alteração do cálculo para desconsiderar o valor de Energia Injetada, de acordo com o parâmetro criado em tela “Desconsiderar Vlr Outras Deduções/Energia Injetada p/ Valor Contábil Item”.

Se o Campo “13-Modelo de Documento” da tabela SAFX42 (X42_capa_telecom)  for igual à ‘66’;
    Se o parâmetro “Desconsiderar Vlr Outras Deduções/Energia Injetada p/ Valor Contábil Item” estiver marcado na tela de Dados Iniciais
         Preencher o campo com o cálculo abaixo:
         Valor do serviço – Desconto + Outras Despesas
                 (campo 19 – campo 18 + campo 46) 
     Senão
         Valor do serviço + Outras Despesas  – Outras Deduções – 
         Energia elétrica injetada compensada pelo consumidor 
(campo 19 + campo 46 – campo 119 – campo 120)

MFS432827: NFCOM
Se o Campo “13-Modelo de Documento” da tabela SAFX42 (X42_capa_telecom)  for igual à ‘62’;
 Preencher o campo com o cálculo abaixo:
        Valor do serviço – Desconto + Outras Despesas
                 (campo 19 – campo 18 + campo 46) 
Senão
Preencher o campo com o cálculo abaixo:
        Valor do serviço – Desconto
        (campo 19 – campo 18)

Somar todos os registros da tabela X43_ITEM_TELECOM relativos a este item do mapa resumo)		IND_CRED_ICMSS 	 IND_CRED_ICMSS 	‘S’		BASE_ICMS_ORIGDEST             	 BASE_ICMS_ORIGDEST             	SOMA(VLR_BASE_ICMS_DEST) de todos os registros da tabela X43_ITEM_TELECOM relativos a este item do mapa resumo) *1		VLR_ICMS_ORIGDEST	 VLR_ICMS_ORIGDEST	SOMA(VLR_TRIB_ICMS_DEST) de todos os registros da tabela X43_ITEM_TELECOM relativos a este item do mapa resumo) *2		VLR_ALIQ_ORIGDEST	 VLR_ALIQ_ORIGDEST	*2  x  100 / *1		VLR_FECP_ICMS	VLR_FECP_ICMS	Recuperar o valor do Campo VLR_ICMS_FECEP		VLR_FECP_ALIQ_ICMS	VLR_FECP_ALIQ_ICMS	Recuperar o valor do Campo VLR_ALIQ_ICMS_FECEP		VLR_FECP_ICMS_ST	VLR_FECP_ICMS_ST	Recuperar o valor do Campo VLR_ICMS_ST_FECEP		OBS: Na tabela DWT_ITENS_MERC, todos os campos de valor não citados deverão receber valor 0(zero).		

Controle de concorrência - Finalização: conforme procedure de geração de notas fiscais de transferência de crédito.


Qualidade:
Testar geração dos mapas resumo segundo critérios e de/para relacionados na sessão de Stored Procedures:

Dicas:

Reproduzir cada situação possível para formação de mapas resumo conforme exemplos abaixo(garantir que os mapas resumo estão sendo gerados de acordo com as regras determinadas):

Exemplo(NFs – X42 e X43    X     Mapas – X07 e X08):
NFs:
Num Ciclo	Série	S-Série	NumDocfis	Situação
01		A		1		N
01		A		2		N
01		A		3		S
01		A		4		N
01		A		5		N
02		A		6		N
02		A		7		N
02		A		9		N
02		A		10		N
02		B		11		N
02		B		12		N
02		B		15		N
 
Mapas:
Num Ciclo	Série	S-Série	NumDocfisINI	NumDocfisFIM
01		A		1		2		(mapa, quebra próx Nf cancelada)
01		A		3		(nota, cancelada)
01		A		4		5		(mapa, quebra próx Nf outro ciclo)
02		A		6		7		(mapa, quebra próx Nf fora sequencia)
02		A		9		10		(mapa, quebra próx Nf outra série)
02		B		11		12		(mapa, quebra na seqüência de Nfs)
02		B		15		15		(mapa, fim do movimento)

Utilizar documentos da X42/43 com todos os campos relacionados no De/Para (validar se cada atributo está sendo gravado nos mapas resumo e NFs canceladas de acordo com o definido);

Tentar executar outra operação nos documentos fiscais (importação p/ex) simultaneamente a geração dos mapas: a aplicação deve retornar a mensagem padrão de erro de concorrência;

Incluir um mapa resumo através da manutenção de documentos fiscais e testar a geração:
Com opção de limpar apenas registros gerados (o mapa inserido via manutenção não deve ser eliminado);
Com opção de limpar todos os registros de mapas resumo/NFs modelo 22 (o mapa inserido via manutenção deve ser eliminado);

IMPORTANTE: Todas as NFs de um mesmo ciclo de faturamento (X42_CAPA_TELECOM.NUM_CICLO), devem ter a mesma data fiscal (X42_CAPA_TELECOM.DAT_FISCAL).