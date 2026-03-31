# Notas_Especiais_C100_v8

> Fonte: Notas_Especiais_C100_v8.doc

Notas com tratamento especial na geração dos registros C100 / C170 (Nota e Itens)


MFS/CH	Nome	Descrição		MFS35664	Andréa Rocha	Incluir a regra de geração para a NF de Transferência de Crédito/Débito – RN  		MFS44246	Vânia Mattos	Inclusão do registro C180 na regra de exceção 2, sobre gravação dos itens no C170 (ver “NF Eletrônica emitida pelo contribuinte” 		MFS45380	Vânia Mattos	Inclusão do registro C181 na regra de exceção 2, sobre gravação dos itens no C170 (ver “NF Eletrônica emitida pelo contribuinte” 		MFS58290	Rogério Ohashi	Alteração da Regra de geração do Campo 06 – COD_SIT do Registro C100, específico para “NF de Transferência de Crédito / Débito”, COD_SIT = 08, conforme “Exceção 4” (C100) do Manual do Guia Prático.
		MFS-36422	Liliane Videira Assaf	Atendimento a Nota Técnica 002/2010 do Rio Grande do Norte
Alteração na NF de Transferência de Crédito/Débito – RN  (IND_TRANSF_CRED <> 0 e UF =RN)
Para não zerar o valor do ICMS nos registros C100, C170 e C190		MFS75220	Andréa Rocha	Inclusão de regra para tratar o novo parâmetro “Preenchimento do Campo 06-Código da Situação para notas fiscais em consignação e de simples faturamento” da tela de dados iniciais. 		MFS77885	Rogério Ohashi	Alteração na regra geral, para o Registro C100, a partir do Layout EFD115 (CAD_LAYOUT– COD_VERSAO>=115) não gerar as Notas Fiscais Denegadas e Inutilizadas de Saídas. Conforme ajuste Sinief nº 038 DOU de 08/10/2021 que altera o Ajuste Sinief nº 7/05.		MFS86283	Rogério Ohashi	Inclusão de regra para os Estabelecimentos da UF=RS, para preencher os campos de valores de VL_DOC (C100) e VL_OPR (C190), quando se tratar de NF com o COD_SIT igual a “08” (Documento Fiscal emitido com base em Regime Especial).		MFS90103	Rogério Ohashi	Inclusão de Regra para os Contribuinte da UF=GO para preencher os Campos de ICMS e ICMS-ST para as Notas extemporâneas de saídas, dos Registros C100, C170 e C190.		MFS91697	Andréa Rocha	Inclusão de uma nova regra para gerar o registro C170 para NF eletrônica emitida pelo contribuinte, para a UF = RO, considerando a IN 33/18 com vigência em 25/10/2018.		MFS80572	Andréa Rocha	Inclusão do tratamento para a geração das informações do registro C177 para estabelecimentos que sejam de Pernambuco e sejam Comércio Atacadista. Ou seja, o registro C177 também vai ser gerado para estabelecimentos que não sejam beneficiários do Prodepe.		MFS516681	Andréa Rocha	Alteração do campo 05 – QTD do registro C170 para as notas fiscais complementares.		MFS517158	Andréa Rocha	Alteração do campo 05 – QTD do registro C170 para as notas fiscais, quando se tratar de NF com o COD_SIT igual a “08” (Documento Fiscal emitido com base em Regime Especial).		MFS628422	Andréa Rocha	Atendimento a Instrução Normativa n° 03/2024, do Ceará Alteração na NF de Transferência de Crédito –  (IND_TRANSF_CRED = 1) para não zerar o valor do ICMS nos registros C100, C170 e C190.  Essa alteração não vai ficar vinculada ao estado do Ceará, poderá ser usada por qualquer estado, que faça a transferência de saldo credor de ICMS para compensar saldo devedor de outro estabelecimento. Será utilizado o parâmetro 96 da tela de Parâmetros por UF, que foi criado para validar essa regra.		MFS670091	Andréa Rocha	Alteração de regra que trata o parâmetro “Preenchimento do Campo 06-Código da Situação para notas fiscais em consignação e de simples faturamento” da tela de dados iniciais.   O campo 20 - VL_OUT_DA do registro C100 deve ser gerado com zero.		MFS673714	Andréa Rocha	Alteração da regra de geração para a NF de Transferência de Crédito/Débito, para o campo VL_DOC do C100.		REGRAS DE NEGÓCIO


As notas deverão ser geradas de acordo com a planilha DE-PARA e com as regras específicas de cada campo, mas existem alguns tipos de nota que terão um tratamento diferenciado. 

Estas exceções se devem a dois tipos de situação: 

Regras descritas no documento “PVA” (validador);
Regras específicas da escrituração das notas nos livros fiscais (P1/P2/P9);

De acordo com as orientações do documento “GT” do Sped Fiscal, os registros de nota fiscal devem seguir as regras de escrituração dos livros P1, P2 e P9, ou seja, o valor do imposto só deve ser lançado no campo próprio quando ele for realmente utilizado na apuração do período.
 
Como o Bloco E será gerado a partir dos dados da apuração feita no Mastersaf, é importante que a escrituração da nota nos registros C100 e seus “filhos” sigam as mesmas regras utilizadas na apuração.

Somente desta forma se dará a consistência entre os dados da apuração (registros E110 e E210) e o registro C190, de acordo com as regras de validação dos totais de débito e crédito descritas no documento “PVA”.

O Mastersaf tem tratamento diferenciado para a escrituração de vários tipos de nota, que são as notas canceladas e as notas  com o campo “Situação Especial” preenchido (campo 125 da SAFX07).  

Obs: as notas com o campo “Situação Especial - ST” preenchido (campo 168 da SAFX07 e 132 da SAFX08) também têm tratamento diferenciado nos livros, no entanto, são procedimentos que não interferem no lançamento do valor do imposto, não interferindo portanto no resultado da apuração (como por exemplo a geração automática de observações).  

Notas com tratamento especial:

NF Cancelada  (SITUACAO = ‘S’)
NF-e inutilizada e denegada  (SITUACAO = ‘S’) e (IND_NFE_DENEG_INUT =  1/2)
NF Complementar   (IND_SITUACAO_ESP= 5)
NF Venda Globalizada   (IND_SITUACAO_ESP= 1)
NF Acompanhamento ECF   (IND_SITUACAO_ESP= 2)
NF Remessa por Conta e Ordem  (IND_SITUACAO_ESP= 8)
NF de Transferência de Crédito/Débito (IND_TRANSF_CRED <> 0) 
NF Importação sem lancto do ICMS no P1/P9  (IND_SITUACAO_ESP=9)
NF emitida com base em regime/norma específica   (IND_NF_REG_ESPECIAL = ‘S’)
NF Eletrônica emitida pelo contribuinte (COD_MOD = 55 e IND_EMIT = 0)
NF extemporânea de SAÍDA (MOVTO_E_S = ‘9’ e DAT_ESCR_EXTEMP > 0)
- 	NF Simples Faturamento e parâmetro de Dados Iniciais = ‘08’ (IND_SITUACAO_ESP = ‘D’ e CFOP’s =  “1922, 2922, 3922, 1117, 2117, 3117, 5922, 6922, 7922, 5116, 6116 ou 7116” (campos 14 da SAFX07, 22 da SAFX08 ou 17 da SAFX09 – COD_CFOP). 
NF de Transferência de Crédito/Débito – MS  (IND_TRANSF_CRED <> 0 e UF =MS)

[MFS-35664] Inclusão do tratamento para NF de Transferência de Crédito / Débito - RN 
NF de Transferência de Crédito/Débito – RN  (IND_TRANSF_CRED <> 0 e UF = RN)
NF de Transferência de Crédito – CE  (IND_TRANSF_CRED = 1 e UF = CE)
NFC-e
NF Simples Faturamento e parâmetro de Dados Iniciais = ‘00’ (IND_SITUACAO_ESP = ‘D’ e CFOP’s =  “1922, 2922, 3922, 1117, 2117, 3117, 5922, 6922, 7922, 5116, 6116 ou 7116” (campos 14 da SAFX07, 22 da SAFX08 ou 17 da SAFX09 – COD_CFOP). 
NF em Consignação e parâmetro de Dados Iniciais = ‘00’


Segue quadro com a situação de cada nota no Mastersaf, as regras do validador do Sped Fiscal, e a definição de como cada uma delas deverá ser tratada na geração dos registros C100 e “filhos”.
 
A coluna “Escrituração Mastersaf” mostra como a nota é tratada no Mastersaf.

A coluna “Regra do Validador” cita a regra do validador (caso exista), conforme o documento “PVA”.

A coluna “Gravação do C100 e filhos” mostra como a nota deverá ser gravada nos registros C100 e seus filhos. 


NF Cancelada   
                                                               (SITUACAO = ‘S’)
		Escrituração Mastersaf	P1/P2 – a nota é lançada apenas com os dados de identificação (sem os valores)
P8 /P9 – a nota não é considerada na apuração		Regra do Validador	Não gerar os filhos do C100
No C100 preencher apenas os campos chave (com exceção do campo COD_PART), e também o IND_OPER e o COD_SIT:
-REG
-IND_OPER
-IND_EMIT
-COD_MOD
-COD_SIT
-SER
-NUM_DOC

Se o documento for NFE, ou seja, campo 13 (COD_MODELO) da SAFX07 = “55”, e a data fiscal (campo 03 da SAFX08, DATA_FISCAL) for maior ou igual á ‘01/01/2011’, apresentar os campos acima citados incluindo o campo “Chave NFE” (CHV_NFE), referente ao campo 226 da SAFX07.

Crítica da chave da NFe :       (OS3598)
Quando não existir a informação da chave da NF-e, e o período da geração for >= Jan/2012, será gerada mensagem de aviso ao usuário sobre a obrigatoriedade do preenchimento. A msg é a mesma que consta no documento de regras (regra RNC100-09).

(conforme teste feito pelo QA em Maio/2012, o validador (vrs 2.0.25) só obriga o preenchimento deste campo p/as notas canceladas a partir de Jan/2012).

[ALTERADA – CH2518_2014]
Se o documento for NFC-e, ou seja, campo 13 (COD_MODELO) da SAFX07 = “65”, e a data fiscal (campo 03 da SAFX08, DATA_FISCAL) for maior ou igual a ‘01/04/2012’, e o documento for de emissão própria, ou seja, campo 03 do C100 igual á “0”), apresentar os campos acima citados incluindo o campo “Chave NFE” (CHV_NFE), referente ao campo 226 da SAFX07.

(A partir de abril de 2012, a chave da NF-e é obrigatória em todas as situações, exceto para NFe com numeração inutilizada (COD_SIT = 05)).		Gravação do C100 e filhos	Proceder exatamente de acordo com a regra do validador.		Obs	

		
NF-e denegada e inutilizada 
                               (SITUACAO = ‘S’) e (IND_NFE_DENEG_INUT = ‘1’ ou ‘2’)
		Escrituração Mastersaf	Para Geração c/ leiaute anterior a EFD115 (CAD_LAYOUT – COD_VERSAO<115):

O indicador desta situação da NF-e é novo (OS2388B-2), mas o tratamento é o mesmo da nota cancelada.  

[CH8643_2012 – Retirada a chave nfe das notas inutilizadas]
Se o documento for NFE, ou seja, campo 13 (COD_MODELO) da SAFX07 = “55”, 
        E a DATA_FISCAL for maior ou igual á janeiro de 2012
        E o documento for de emissão própria, ou seja, campo 03 do C100 igual á “0”)
           E o código da situação, campo 06 do C100 for igual á “04” ou “05” (Nota Fiscal denegada ou inutilizada)
Então informar o valor do campo 226 da Safx07 (NUM_AUTENTIC_NFE)  no campo 09 do registro C100 (CHV_NTE), além dos campos citados no tratamento de nota fiscal cancelada.

[ALTERADA – CH2518_2014]
Se o documento for NFC-e, ou seja, campo 13 (COD_MODELO) da SAFX07 = “65”, 
        E a DATA_FISCAL for maior ou igual a abril de 2012
        E o documento for de emissão própria, ou seja, campo 03 do C100 igual á “0”)
           E o código da situação, campo 06 do C100 for igual á “04” (Nota Fiscal denegada)
Então informar o valor do campo 226 da Safx07 (NUM_AUTENTIC_NFE) no campo 09 do registro C100 (CHV_NTE), além dos campos citados no tratamento de nota fiscal cancelada.

[OS-3673 - Alteração]
Mesma regra permanece para quando a origem dos dados for a tabela SAFX130:

Informar o valor do campo 12 da SAFX130 (NUM_AUTENTIC_NFE)  no campo 09 do registro C100 (CHV_NFE), além dos campos citados no tratamento de nota fiscal cancelada, se:

Modelo igual “55”:
O Campo 10 do C100 (Data de emissão) for maior ou igual á janeiro de 2012,
Campo IND_OPER do C100 =  “0”, ou seja, emissão própria,
E o código da situação, campo 06 do C100 for igual á “04” (Nota Fiscal denegada).

[ALTERADA – CH2518_2014]
Modelo igual “65”:
O Campo 10 do C100 (Data de emissão) for maior ou igual a abril de 2012,
Campo IND_OPER do C100 = “0”, ou seja, emissão própria,
E o código da situação, campo 06 do C100 for igual á “04” (Nota Fiscal denegada).

Crítica da chave da NFe  para as notas denegadas:  (OS3598)
Quando não existir a informação da chave da NF-e, e o período da geração for >= Jan/2012, será gerada mensagem de aviso ao usuário sobre a obrigatoriedade do preenchimento. A msg é a mesma que consta no documento de regras (regra RNC100-09). [ALTERADA – CH2518_2014] Para o modelo 65 se aplica apenas emissão própria da (regra RNC100-09).

(conforme teste feito pelo QA em Maio/2012, o validador (vrs 2.0.25) só obriga o preenchimento deste campo p/as notas denegadas a partir de Jan/2012).

Para Geração c/ leiaute a partir da EFD115 (CAD_LAYOUT – COD_VERSAO>=115):

[MFS77885] Tratamento p/ Notas Fiscais Denegadas e Inutilizadas com Origem da SAFX07 e SAFX130

Origem SAFX130

As notas gravadas no Registro C100 a partir da tabela SAFX130 (notas denegadas ou inutilizadas) não devem ser consideradas no arquivo meio magnético, a partir do layout versão 1.15 (Janeiro/2022); 

Origem SAFX07

Se o Campo 231 - IND_NFE_DENEG_INUT da tabela SAFX07 for igual à ‘1’ ou ‘2’;
    Não preencher o Registro C100, Notas Fiscais denegadas ou inutilizadas não devem ser consideradas no arquivo meio magnético, a partir do layout versão 1.15 (Janeiro/2022)

1 - Nota Fiscal Eletrônica denegada;
2 - Nota Fiscal Eletrônica inutilizada.
		Regra do Validador	Idem NF Cancelada		Gravação do C100 e filhos	Idem NF Cancelada		Obs	 		
NF Complementar
                                                         (IND_SITUACAO_ESP= 5)

O tratamento desta nota nos livros P1/P2/P9 está associado ao parâmetro 48 (“Tratamento das NFs de Complemento de ICMS”)  da parametrização por UF.		Escrituração Mastersaf	P1/P2 - Se o parâmetro 48 estiver ativo, a nota não será apresentada no livro.
P9 - Se o parâmetro 48 estiver ativo, a nota não será considerada p/a apuração.
(Obs: no P8 não existe nenhum tratamento especial p/esta nota)		Regra do Validador	No C100 são obrigatórios apenas os campos: 
-IND_EMIT
-COD_MOD
-COD_SIT
-SER
-NUM_DOC
-COD_PART
-DT_DOC

Os outros campos e os registros filhos são facultativos, exceto o C190.		Gravação do C100 e filhos	
Alteração da OS2388-E10 (Release 32/33/34):       (Abr/2009) 

A partir desta OS a gravação das notas complementares será feita normalmente sem considerar a regra do PVA, ou seja, gravando normalmente todos os registros filhos.

Gravar o C100 de acordo com as regras do validador (gravando os campos descritos acima), e além destes campos, deverão ser gravados também os seguintes valores:

-VL_DOC
-VL_BC_ICMS
-VL_ICMS
-VL_BC_ICMS_ST
-VL_ICMS_ST
-VL_IPI

(os valores passaram a ser gravados na OS2388-E5ge p/evitar problema no PVA)

Não gravar nenhum filho, exceto o C190, que deverá ser gerado normalmente, a partir dos itens da nota, e considerando a seguinte regra:

[ALTERAÇÃO – CH6679_2016/ CH9420_2018 (MFS-18812)]
[MFS516681] Alteração da geração do campo 05-QTD do registro C170

Se o parâmetro 48 estiver ativo, os valores referentes ao ICMS (Aliquota do ICMS, Base ICMS, ICMS, Base ST, ST e Base Reduzida) não devem ser considerados, nem para gravação dos registros C100 e C170, nem na totalização dos itens. O campo Quantidade do registro C170 também não deve ser considerado, devendo gerar || (pipe-pipe). O preenchimento do campo Quantidade do registro C170 deve seguir a seguinte regra:
- Se a quantidade do item (campo 24 da SAFX08) for igual a 0 ou nulo, o campo de quantidade do Registro C170 deverá ser gerado vazio (“||” pipe-pipe);
- Se a quantidade do item (campo 24 da SAFX08) for igual a 0 ou nulo, o campo de quantidade do Registro C170 deverá ser gerado com 0 (zero);
- Senão considerar a quantidade do item preenchida (campo 24 da SAFX08).

Se o parâmetro 48 estiver desativado a totalização deve ser feita normalmente, e os campos do C100, C170 e C190 serão preenchidos normalmente, exceto com campo Quantidade do registro C170 que deverá seguir a seguinte regra: não deve ser considerado, devendo gerar || (pipe-pipe). 
- Se a quantidade do item (campo 24 da SAFX08) for igual a 0 ou nulo, o campo de quantidade do Registro C170 deverá ser gerado vazio (“||” pipe-pipe);
- Se a quantidade do item (campo 24 da SAFX08) for igual a 0 ou nulo, o campo de quantidade do Registro C170 deverá ser gerado com 0 (zero);
- Senão considerar a quantidade do item preenchida (campo 24 da SAFX08).		Obs	OBS1: Será que o validador prevê a  existência do C190 sem o C170? (pelas regras do validador, a validação do C190 é feita baseado nos valores do C170).
OBS 2: Quando esta situação for utilizada, e a nota for gravada sem carregar os valores de ICMS, é  preciso que o código CST seja preenchido corretamente, para evitar críticas do validador. Deve ser utilizado um código de acordo com a escrituração da nota, ou seja, considerando se haverá ou não o crédito/débito.

No CT foi utilizado o CST_ICMS = 090.		
NF Venda Globalizada  
                                                       (IND_SITUACAO_ESP = 1)
		Escrituração Mastersaf	P1/P2 - A nota é lançada no livro sem os valores, e também sem o CFOP.
P8/P9 – A nota não é considerada na apuração		Regra do Validador	(não consta)		Gravação do C100 e filhos	Gravar o registro C100 sem preencher os campos de valor e base de todos os impostos:
VL_BC_ICMS e VL_ICMS
VL_BC_ICMS_ST e VL_ICMS_ST
VL_IPI
VL_PIS e VL_COFINS
VL_PIS_ST e VL_COFINS_ST
VL_DOC e VL_MERC  [MFS33153]
Os demais campos devem ser preenchidos normalmente.

Gravar o C170 também sem preencher os campos de valor, alíquota e base dos impostos, que são os campos:
VL_BC_ICMS, ALIQ_ICMS e VL_ICMS
VL_BC_ICMS_ST, ALIQ_ST e VL_ICMS_ST
VL_BC_IPI, ALIQ_IPI e VL_IPI
VL_BC_PIS, ALIQ_PIS, QUANT_BC_PIS, ALIQ_PIS e VL_PIS
VL_BC_COF, ALIQ_COF, QUANT_BC_COF, ALIQ_COF e VL_COF
Os demais campos devem ser preenchidos normalmente.

O C190, como é uma totalização dos itens (ou da capa, quando for o caso), também apresentará os mesmos resultados, ou seja, sem preencher os campos:
ALIQ_ICMS, VL_BC_ICMS e VL_ICMS
VL_BD_ICMS_ST e VL_ICMS_ST
VL_RED_BC
VL_IPI
VL_OPER  [MFS33153]

Todos os outros registros filhos do C100 (os não citados nesta regra), devem ser gravados normalmente.
		Obs	Este procedimento poderá ter problemas com o validador se o código CST-ICMS não for informado corretamente na nota. O código utilizado deve estar de acordo com a escrituração da nota. Se o imposto destacado na nota não será lançado nos livros, a nota não poderá ter um código CST referente à operação tributada (como por exemplo o “00”). 

No CT foi utilizado o CST_ICMS = 090		
NF Acompanhamento ECF  
                                                       (IND_SITUACAO_ESP = 2)
		Escrituração Mastersaf	P1/P2 - A nota é lançada no livro sem os valores, e também sem o CFOP.
P8/P9 – A nota não é considerada na apuração		Regra do Validador	(não consta)		Gravação do C100 e filhos	Idem NF de Venda Globalizada		Obs	Idem NF de Venda Globalizada		
NF Remessa por Conta e Ordem  
                                                       (IND_SITUACAO_ESP = 8)
		Escrituração Mastersaf	P1/P2 - A nota é lançada no livro sem os valores
P8/P9 – A nota não é considerada na apuração		Regra do Validador	(não consta)		Gravação do C100 e filhos	Idem NF de Venda Globalizada

Alteração conforme chamado 61506 (Abr/2009):
Quando este tipo de nota estiver marcado como uma nota de regime especial, ou seja, quando IND_NF_REG_ESPECIAL da SAFX07 = “S”, os campos VL_DOC,  VL_MERC do C100 e o VL_ITEM do C170 também não serão preenchidos. Mas somente quando for nota de regime especial, caso contrário, a alteração não poderia ser feita pois o PVA dá erro (o validador não aceita notas sem valor (VL_DOC = 0), exceto no caso de notas de regime especial ou norma específica). Assim, quando a nota atender as duas situações (remessa e regime especial), a geração passa a ser feita da mesma forma que as notas de venda globalizada, exceto sobre estes campos, que não serão mais preenchidos.

No C100 passam a ser gravados apenas os campos: 
-IND_EMIT
-COD_MOD
-COD_SIT
-SER
-NUM_DOC
-COD_PART
-DT_DOC

Gravar o C170 também sem preencher os campos de valor. Os demais campos devem ser preenchidos normalmente.

O C190, como é uma totalização dos itens (ou da capa, quando for o caso), também apresentará os mesmos resultados, ou seja, sem os valores.

Os registros não citados nesta regra devem ser gravados normalmente.
 
Importante (histórico): 
Os campos VL_DOC (C100) e o VL_ITEM (C170), eram anteriormente preenchidos para não ocorrer crítica no PVA (que não aceita notas sem valor, com exceção de regime especial). A alteração do chamado 61506 foi feita às pressas pela equipe de Suporte da Fábrica-RJ  para atender ao cliente. No entanto, para que o PVA não dê erro, é pré-requisito que o indicador de notas com regime/norma específica seja ativado, caso contrário, o PVA vai dar erro. 
Cabe observar que ficamos sujeitos a erros no PVA se a nota complementar não for um regimelnorma específica. O certo seria fazer um call com a RFB para esclarecer o assunto, antes de efetuar a alteração, já que o PVA não cita regras sobre este tipo de nota. 
		Obs	Idem NF de Venda Globalizada		

NF de Transferência de Crédito / Débito 
(IND_TRANSF_CRED <> 0)
		Escrituração Mastersaf	P1/P2 - A nota é lançada no livro sem os valores
P8/P9 – A nota não é considerada na apuração		Regra do Validador	(não consta)		Gravação do C100 e filhos	[MFS32361] – Alteração do código de situação de 08 para 00, conforme alteração do guia prático.

[MFS58290] – Alteração de regra para o código de situação 08, conforme Exceção 4 (C100) do Manual do Guia Prático.

Esta nota deverá ser gravada conforme definido para a nota de Venda Globalizada, mas além disso, ela deverá ser gravada com o código de situação = ‘00’ (COD_SIT do C100). 

Esta nota deverá ser gravada conforme definido para a nota de Venda Globalizada, mas além disso:

SE o Campo IND_NF_REG_ESPECIAL da Tabela DWT_DOCTO_FISCAL for = SIM;
     Gravar o com o código de situação = ‘08’ (COD_SIT do C100);

SENÂO Gravar o com o código de situação = ‘00’ (COD_SIT do C100);

[MFS33017] – Alteração do preenchimento dos campos de valor.
[MFS673714] – Alteração do preenchimento dos campos VL_DOC (C100) e VL_OPR (C190).

Se o parâmetro “Preencher o Campo 12-VL_DOC para as notas fiscais de transferência”  estiver marcado na tela de dados iniciais
       Gravar o registro C100 com o campo 12-VL_DOC  preenchido e os demais   
       campos de valor devem ser preenchidos com zero 
       Gravar o registro C170 com o campo 07-VL_ITEM  preenchido e os demais   
       campos de valor devem ser preenchidos com zero
       Gravar o registro C190 com o campo 05-VL_OPR  preenchido e os demais   
       campos de valor devem ser preenchidos com zero. Somente serão 
       preenchidos os campos de CST_ICMS e CFOP
Senão
       Gravar o registro C100 sem preencher todos os campos de valor, preencher 
       com zero nestes campos
       O C190, como é uma totalização dos itens (ou da capa, quando for o caso),  
       também apresentará os mesmos resultados, ou seja, sem os valores.        
       Somente serão preenchidos os campos de CST_ICMS e CFOP.

Este procedimento será realizado para que o validador aceite o fato da nota não ter valor da operação. Se utilizarmos o código ‘00’ o validador não aceita a ausência do VL_OPR no C190. 
		Obs	Idem NF de Venda Globalizada		
NF Importação sem lancto do ICMS no P1/P9  
                                                        (IND_SITUACAO_ESP = 9)
		Escrituração Mastersaf	Este tipo de nota é tratado no P1 e P9. 
P1 ( A nota é lançada no livro preenchendo-se todas as colunas normalmente, mas o valor do ICMS e a base tributada não são lançados nas suas respectivas colunas. A base tributada é lançada na coluna “Outras”.
P9 ( O valor do ICMS não é considerado na apuração, mas a nota é registrada no demonstrativo dos CFOP’s da seguinte forma: a base tributada aparece na coluna “Outras”, e os valores de ICMS e base tributada não são lançados nas suas respectivas colunas.
(Obs: no P8 não existe nenhum tratamento especial p/esta nota)		Regra do Validador	(não consta)		Gravação do C100 e filhos	Gravar o C100 com todas as informações da nota normalmente, mas sem preencher os valores de ICMS:
VL_BC_ICMS e VL_ICMS, 
VL_BC_ICMS_ST e VL_ICMS_ST.

O C170 também deve ser gravado normalmente, mas aplicando-se a mesma regra citada para o C100, ou seja, sem preencher  os valores referentes ao ICMS:
VL_BC_ICMS, ALIQ_ICMS e VL_ICMS
VL_BC_ICMS_ST,  ALIQ_ST e VL_ICMS_ST
 
O C190, como é uma totalização dos itens (ou da capa, quando for o caso), também apresentará os mesmos resultados, ou seja, sem preencher os campos:
ALIQ_ICMS, VL_BC_ICMS e VL_ICMS
VL_BD_ICMS_ST e VL_ICMS_ST

Todos os outros registros filhos do C100 (os não citados nesta regra), devem ser gravados normalmente.		Obs	OBS1: da mesma forma que nos outros casos, o CST_ICMS devera ser informado corretamente, caso contrario, poderão aparecer criticas no validador.

No CT foi utilizado o CST_ICMS = 090		
NF emitida com base em regime/norma específica  
(IND_NF_REG_ESPECIAL = ‘S’ e COD_SIT = ‘08’)
		Escrituração Mastersaf	Não existe tratamento especial para notas emitidas com base em regime especial.
(o indicador IND_NF_REG_ESPECIAL é novo, foi criado na OS2388B-1, para atender ao Sped Fiscal)

Situação Especial: 		Regra do Validador	No C100 são obrigatórios apenas os campos: 
-IND_EMIT
-COD_MOD
-COD_SIT
-SER
-NUM_DOC
-COD_PART
-DT_DOC

[MFS517158] Alteração da geração do campo 05-QTD do registro C170

 Se a quantidade do item (campo 24 da SAFX08) for igual a 0 ou nulo, o campo de quantidade do registro C170 deverá ser gerado com nulo.

Os outros campos e os registros filhos são facultativos, exceto o C190.		Gravação do C100 e filhos	
Alteração da OS2388-E10 (Release 32/33/34):       (Abr/2009) 

A partir desta OS a gravação das notas de regime especial será feita normalmente sem considerar a regra do PVA, ou seja, gravando normalmente todos os registros filhos.

Gerar o C100 de acordo com as regras do validador (gravando os campos descritos acima), e além destes campos, deverão ser gravados também os seguintes valores:

-VL_DOC
-VL_BC_ICMS
-VL_ICMS
-VL_BC_ICMS_ST
-VL_ICMS_ST
-VL_IPI

(os valores passaram a ser gravados na OS2388-E5ge p/evitar problema no PVA)
 
Não gravar nenhum filho, exceto o C190, que deverá ser gerado normalmente, a partir dos itens da nota, com todos os valores.		Obs	OBS1: Será que o validador prevê a  existência do C190 sem o C170? (pelas regras do validador, a validação do C190 é feita baseado nos valores do C170).

[ALTERAÇÃO- MFS86283] Tratamento COD_SIT igual à 08 para UF=RS.

  
    Se o Campo 06- COD_SIT do Registro ‘C100’ for  igual à ‘08’;
         E se a UF do estabelecimento for igual à ‘RS’.

   Preencher os campos abaixo:

         - Campo 12 – ‘VL_DOC’ do Registro ‘C100’; 
         - Campo 05 – ‘VL_OPR’ do Registro ‘C190’.


Obs.: De acordo com o Estado do Rio Grande do Sul, ao informar uma nota fiscal com sua situação fiscal igual a 08 (COD_SIT = 08), deverá ser informado nos registros C100 e C190 a informação do valor documento fiscal "total da nota fiscal", sendo: VL_DOC (C100) e VL_OPR (C190).
		
NF Eletrônica emitida pelo contribuinte 
                                             (COD_MOD = 55 e IND_EMIT = 0)
 		Escrituração Mastersaf	Não existe nenhum tratamento especial nos livros.		Regra do Validador	Para as NF-e de emissão própria, não será necessário gerar todos os filhos do C100.
Deve ser gerado o registro C100, e apenas os “filhos” C190, C195 e C197.

Alteração do Guia Prático vrs 1.0.4:     (Maio/2009) 
Criada a regra “Exceção 6” no registro C100. De acordo com a nova regra, no caso das NF’e de saída, deverão ser gravados também os registros C170 e C176, mas apenas para os itens da nota que se enquadrem na situação de gerar direito a ressarcimento.

[MFS80572] Inclusão do tratamento para a geração das informações do Registro C177 para estabelecimentos que sejam de Pernambuco e sejam Comércio Atacadista.  A partir dessa alteração, o estabelecimento não necessita ser beneficiário do Prodepe para gerar o Registro C177.

Alteração do Guia Prático vrs 3.0:   (a partir de Jan/2019) 
Criada a regra “Exceção 10” no registro C100. De acordo com a nova regra, no caso dos estabelecimentos de PE, que sejam beneficiários do PRODEPE ou Comércio Atacadista, os registros C170 e C177 deverão ser gravados, exceto nos casos de cancelamento ou denegada/inutilizada (COD_SIT = 02, 03, 04 ou 05). Ver detalhes no documento de regras da geração do Bloco C.

[CH20080_2012]
Seguindo a regra de exceção 2 no registro C100: 

Gerar o registro C170 apenas quando houver direito de ressarcimento, ou seja, se houver o C176. Caso contrário, o registro C170 não deve ser gerado. 
Obs.: esta regra já está valendo para saídas conforme descrito na exceção 6, porém também deve ser considerado para entrada.

Gerar os registros C110 e C120 a partir de julho/2012, ou seja, quando o código de leiaute selecionado na geração for maior ou igual á versão “1.0.5”.

MFS44246: Gerar o registro C170 a partir de Jan/2020 (vrs 1.13), dos itens para os quais existir informações complementares a serem prestadas no registro C180;

MFS45380: Gerar o registro C170 a partir de Jan/2021 (vrs 1.14), dos itens para os quais existir informações complementares a serem prestadas no registro C181;

A partir de janeiro de 2020, também poderá ser informado o Registro C185, a critério de cada UF. A partir de janeiro de 2021, poderá ser informado o Registro C186, a critério de cada UF.

MFS91697: Gerar o registro C170 a partir de Out/2018, para demonstrar as operações realizadas pelo cliente em "devolução ou transferência de mercadoria quando não houve aproveitamento do crédito na entrada", específico para a UF=RO, considerando a IN 33/18 com vigência em 25/10/2018.

[ALTERADA – OS3892]

Os registros C110 e C120, e filhos (C111 à C116) deixam de ser gerados quando o novo parâmetro Não gerar C110 e C120 – NF-e de emissão própria for devidamente selecionado.

Parâmetro “Não gerar C110 e C120 – NF-e de emissão própria”:

Se o usuário selecionar esse parâmetro, os registros C110 e C120, além dos filhos (C111 à C116) não devem ser gerados quando:

Campo 03 - MOVTO_E_S = ‘2’,’3’, ‘4’, ‘5’ e ‘9’
Campo 11 - DATA_EMISSAO for pertinente ao período de geração;
Campo 13 - COD_MODELO = ‘55’.

Caso o parâmetro não seja selecionado, a geração do meio magnético não deve sofrer nenhuma alteração.
		Gravação do C100 e filhos	Gerar de acordo com as regras do validador:
Gerar o C100 normalmente
Não gerar os registros filho, exceto o C190, C195 e C197.

Alteração OS2388-N1-A (Release 32/33/34/34.1):   (Maio/2009) 
A partir desta OS, serão gravados também os registros C170 e C176, quando for o caso dos itens de nota que geram direito a ressarcimentos de ICMS. Ver detalhes na OS2388-N1-Age. 

[CH20080_2012]
Gerar o registro C170 apenas quando houver direito de ressarcimento, ou seja, se houver o C176. Caso contrário, o registro C170 não deve ser gerado.

Gerar os registros C110 e C120 a partir de julho/2012, ou seja, quando o código de leiaute selecionado na geração for maior ou igual à versão “1.0.5”.
[MFS91697]
Gerar o registro C170 a partir de outubro/2018 para o estabelecimento cuja UF=RO, e que tenha um registro de ajuste na SAFX113 referente a nota de saída, com o código de ajuste (campo 13) igual a ‘RO20000004’.
		Obs	OBS1: Será que o validador prevê a  existência do C190 sem o C170? (pelas regras do validador, a validação do C190 é feita baseado nos valores do C170).		
NF extemporânea de SAÍDA
(MOVTO_E_S = ‘9’ e DAT_ESCR_EXTEMP > 0)
		Escrituração Mastersaf	P2 – a nota é lançada apenas com os dados de identificação (sem os valores)
P8/P9 - Desconsiderar as notas fiscais de saída Extemporânea, já que os seus valores não serão considerados nos livros P2 e P2A. Esta alteração deve ser feita tanto na apuração do ICMS, como do ICMS-ST também, tendo em vista que a apuração do ICMS-ST é “embutida” na apuração do ICMS, ou seja, as duas são realizadas no mesmo item simultaneamente.
		Regra do Validador	No C100 apresentar apenas os campos de identificação do documento.
Apresentar o valor zero (0,00) para os campos listados abaixo: 

[ALTERADA – CH14204_2014]
- VL_DESC
- VL_ABAT_NT
- VL_SEG
- VL_OUT_DA
- VL_BC_ICMS
- VL_ICMS
- VL_BC_ICMS_ST
- VL_ICMS_ST
- VL_IPI
- VL_PIS
- VL_COFINS
- VL_PIS_ST
- VL_COFINS_ST

[ALTERADA – MFS90103] Tratamento para os Contribuintes do Estado de Goiás para preencher os Valores de ICMS e ICMS-ST.

Se a UF do estabelecimento foe igual à “GO”.
  E o Campo 06- COD_SIT do Registro ‘C100’ for  igual à ‘01’, ‘07’;

  Seguir conforme regra abaixo:

No C100 apresentar apenas os campos de identificação do documento.
Apresentar o valor zero (0,00) para os campos listados abaixo: 

- VL_DESC
- VL_ABAT_NT
- VL_SEG
- VL_OUT_DA
- VL_IPI
- VL_PIS
- VL_COFINS
- VL_PIS_ST
- VL_COFINS_ST

Obs¹.: Alteração efetuado conforme orientação Manual Guia Prático da EFD ICMS/IPI de GO. “GuiaPraticodaEFD-Goiasv4.8.pdf”.


Os outros registros filhos são facultativos, exceto o C190.		Gravação do C100 e filhos	O C170 também deve ser gravado normalmente, mas aplicando-se a mesma regra citada para o C100, ou seja, apresentar apenas os campos de identificação do documento.
Apresentar o valor zero (0,00) para os campos listados abaixo: 

- VL_ITEM
- VL_DESC
- VL_BC_ICMS
- ALIQ_ICMS
- VL_ICMS
- VL_BC_ICMS_S0054
- ALIQ_ST
- VL_ICMS_ST
- VL_BC_IPI
- ALIQ_IPI
- VL_IPI
- VL_BC_PIS
- ALIQ_PIS
- QUANT_BC_PIS
- ALIQ_PIS_R
- VL_PIS
- VL_BC_COFINS
- ALIQ_COFINS
- QUANT_BC_COFINS
- ALIQ_COFINS_R
- VL_COFINS

[ALTERADA – MFS90103] Tratamento para os Contribuintes do Estado de Goiás para preencher os Valores de ICMS e ICMS-ST.

Se a UF do estabelecimento foe igual à “GO”.
  E o Campo 06- COD_SIT do Registro ‘C100’ for  igual à ‘01’, ‘07’;

  Seguir conforme regra abaixo:

No C170  apresentar o valor zero (0,00) para os campos listados abaixo: 

- VL_ITEM
- VL_DESC
- VL_BC_IPI
- ALIQ_IPI
- VL_IPI
- VL_BC_PIS
- ALIQ_PIS
- QUANT_BC_PIS
- ALIQ_PIS_R
- VL_PIS
- VL_BC_COFINS
- ALIQ_COFINS
- QUANT_BC_COFINS
- ALIQ_COFINS_R
- VL_COFINS

Obs¹.: Alteração efetuado conforme orientação Manual Guia Prático da EFD ICMS/IPI de GO. “GuiaPraticodaEFD-Goiasv4.8.pdf”.

O C190 deve totalizar a escrituração dos documentos fiscais/itens, aplicar também a regra citada no registro C100.
Apresentar o valor zero (0,00) para os campos listados abaixo: 

- ALIQ_ICMS
- VL_OPR (VLR_ITEM)
- VL_BC_ICMS
- VL_ICMS
- VL_BC_ICMS_ST
- VL_ICMS_ST
- VL_RED_BC
- VL_IPI

[ALTERADA – MFS90103] Tratamento para os Contribuintes do Estado de Goiás para preencher os Valores de ICMS e ICMS-ST.

Se a UF do estabelecimento for igual à “GO”.
  E o Campo 06- COD_SIT do Registro ‘C100’ for  igual à ‘01’, ‘07’;

  Seguir conforme regra abaixo:

No C190  apresentar o valor zero (0,00) para os campos listados abaixo: 

- VL_OPR
- VL_BC_ICMS_ST
- VL_ICMS_ST
- VL_RED_BC
- VL_IPI

Obs¹.: Alteração efetuado conforme orientação Manual Guia Prático da EFD ICMS/IPI de GO. “GuiaPraticodaEFD-Goiasv4.8.pdf”.
		Obs		
NF Simples Faturamento e 
parâmetro de Dados Iniciais = ‘08’

[MFS75220] Inclusão do tratamento do parâmetro que indica a forma de preenchimento do campo 06 do registro C100

(IND_SITUACAO_ESP = ‘D’ e CFOP’s =  “1922, 2922, 3922, 1117, 2117, 3117, 5922, 6922, 7922, 5116, 6116 ou 7116” (campos 14 da SAFX07, 22 da SAFX08 ou 17 da SAFX09 – COD_CFOP) e o parâmetro “Preenchimento do Campo 06-Código da Situação para notas fiscais em consignação e de simples faturamento”  igual a ‘08’ da tela de dados iniciais 
		Escrituração Mastersaf	P1 e P2 - A nota é lançada apenas com os dados de identificação (sem os valores)
P8/P9 - Desconsiderar as notas fiscais de simples faturamento, já que os seus valores não serão considerados nos livros P1, P1A, P2 e P2A. Esta alteração deve ser feita tanto na apuração do ICMS, como do ICMS-ST também, tendo em vista que a apuração do ICMS-ST é “embutida” na apuração do ICMS, ou seja, as duas são realizadas no mesmo item simultaneamente.		Regra do Validador	Exceção 4: Notas Fiscais emitidas por regime especial ou norma específica (campo COD_SIT igual a “08”). Para
documentos fiscais emitidos com base em regime especial ou norma específica, deverão ser apresentados os registros C100
e C190, obrigatoriamente, e os demais registros “filhos”, se estes forem exigidos pela legislação fiscal. Nesta situação,
somente os campos REG, IND_EMIT, COD_PART, COD_MOD, COD_SIT, NUM_DOC e DT_DOC são de
preenchimento obrigatório. Os demais campos, com exceção do campo NUM_ITEM do registro C170, são facultativos (se
forem preenchidos, inclusive com valores iguais a Zero, serão validados e aplicadas as regras de campos existentes) e
deverão ser preenchidos, quando houver informação a ser prestada.
		Gravação do C100 e filhos	O sistema deve considerar a seguinte parametrização para a geração do C100 e filhos:

Módulo: SPED ( EFD – Escrituração Fiscal Digital 
Menu: Parâmetros ( Dados Iniciais
Parâmetro: “Situação Especial 08 – Faturamento Simples”

Se todas opções estiverem desmarcadas, então apresentar para o registro C100 e filhos apenas os campos de identificação do documento.

Apresentar o valor zero (0,00) para os campos listados abaixo: 

- VL_DOC
- VL_DESC
- VL_ABAT_NT
- VL_MERC
- VL_MERC
- VL_SEG
- VL_OUT_DA
- VL_BC_ICMS
- VL_ICMS
- VL_BC_ICMS_ST
- VL_ICMS_ST
- VL_IPI
- VL_PIS
- VL_COFINS
- VL_PIS_ST
- VL_COFINS_ST

Os outros registros filhos são facultativos, exceto o C190.
O C170 também deve ser gravado normalmente, mas aplicando-se a mesma regra citada para o C100, ou seja, apresentar apenas os campos de identificação do documento.
Apresentar o valor zero (0,00) para os campos listados abaixo: 

- VL_ITEM
- VL_DESC
- VL_BC_ICMS
- ALIQ_ICMS
- VL_ICMS
- VL_BC_ICMS_ST
- ALIQ_ST
- VL_ICMS_ST
- VL_BC_IPI
- ALIQ_IPI
- VL_IPI
- VL_BC_PIS
- ALIQ_PIS
- QUANT_BC_PIS
- ALIQ_PIS
- VL_PIS
- VL_BC_COFINS
- ALIQ_COFINS
- QUANT_BC_COFINS
- ALIQ_COFINS
- VL_COFINS


O C190 deve totalizar a escrituração dos documentos fiscais/itens, aplicar também a regra citada no registro C100.
Apresentar o valor zero (0,00) para os campos listados abaixo: 

- ALIQ_ICMS
- VL_OPR
- VL_BC_ICMS
- VL_ICMS
- VL_BC_ICMS_ST
- VL_ICMS_ST
- VL_RED_BC
- VL_IPI


Se alguma opção do parâmetro estiver marcada, apresentar apenas os valores dos campos acima correspondentes ao imposto selecionado no parâmetro.
		Obs		

NF de Transferência de Crédito / Débito - MS 
(IND_TRANSF_CRED <> 0 e UF =MS)

Esta regra apenas deverá ser aplicada se for enquadrada na seguinte condição:

Se a UF do Estabelecimento = ‘MS’;
E o parâmetro “Beneficiário do ANEXO I À PORTARIA/SAT nº 2.184, DE 10 DE JANEIRO DE 2011.”, estiver marcado;
E o campo 74 da SAFX07, Nota Fiscal Transferência de Crédito/ Débito (IND_TRANSF_CRED) <> 0;
E o CFOP = ‘5602’ ou ‘5605’ ou ’1602’ ou ‘1605’.
		Escrituração Mastersaf	P1/P2 - A nota é lançada no livro sem os valores
P8/P9 – A nota não é considerada na apuração		Regra do Validador	(não consta)		Gravação do C100 e filhos	Esta nota deverá ser gravada com o código de situação = ‘08’ (COD_SIT do C100). 

No registro C100, Apresentar o valor zero (0,00) para os campos listados abaixo: 
Campo 12 : VL_DOC
Campo 14 : VL_DESC
Campo 15: VL_ABAT_NT
Campo 16: VL_MERC
Campo 18: VL_FRT
Campo 19: VL_SEG
Campo 20: VL_OUT_DA
Campo 21: VL_BC_ICMS
Campo 22: VL_ICMS
Campo 23: VL_BC_ICMS_ST
Campo 24: VL_ICMS_ST
Campo 25: VL_IPI
Campo 26: VL_PIS
Campo 27: VL_COFINS
Campo 28: VL_PIS_ST
Campo 29: VL_COFINS_ST

Os campos 11, 13 e 17 que devem ser preenchidos como vazio, ou seja, “||”: 
Campo 11: DT_E_S 
Campo 13: IND_PGTO 
Campo 17: IND_FRT 


Não gerar o registro C170, devido á regra de exceção 4 do Guia Prático:
Exceção 4: Notas Fiscais emitidas por regime especial ou norma específica (campo COD_SIT igual a “08”). Para documentos fiscais emitidos com base em regime especial ou norma específica, deverão ser apresentados os registros C100 e C190, obrigatoriamente, e os demais registros “filhos”, se estes forem exigidos pela legislação fiscal.


O registro C190, os campos abaixo devem ser gerados normalmente:
Campo 01: REG
Campo 02: CST_ICMS
Campo 03: CFOP
Campo 12: COD_OBS

Do campo 04 até o campo 11 deve ser preenchido com zeros, são eles:
Campo 04: ALIQ_ICMS
Campo 05: VL_OPR
Campo 06: VL_BC_ICMS
Campo 07: VL_ICMS
Campo 08: VL_BC_ICMS_ST
Campo 09: VL_ICMS_ST
Campo 10: VL_RED_BC
Campo 11: VL_IPI
		Obs		
[MFS-35664] Inclusão do tratamento para NF de Transferência de Crédito / Débito - RN 
[MFS-36422] Alteração na regra para não zerar o valor de ICMS nos registros C100, C170 e C190.

NF de Transferência de Crédito / Débito - RN 
(IND_TRANSF_CRED <> 0 e UF =RN)

Esta regra apenas deverá ser aplicada se for enquadrada na seguinte condição:

Se a UF do Estabelecimento = ‘RN’;
     E o campo 74 da SAFX07, Nota Fiscal Transferência de Crédito/ Débito (IND_TRANSF_CRED) <> 0;		Escrituração Mastersaf	P1/P2 - A nota é lançada no livro sem os valores
P8/P9 – A nota não é considerada na apuração		Regra do Validador	(não consta)		Gravação do C100 e filhos	Esta nota deverá ser gravada com o código de situação = ‘08’ (COD_SIT do C100). 

No registro C100, Apresentar o valor zero (0,00) para os campos listados abaixo: 
Campo 14 : VL_DESC
Campo 15: VL_ABAT_NT
Campo 16: VL_MERC
Campo 18: VL_FRT
Campo 19: VL_SEG
Campo 20: VL_OUT_DA
Campo 21: VL_BC_ICMS
Campo 22: VL_ICMS [MFS-36422]
Campo 23: VL_BC_ICMS_ST
Campo 24: VL_ICMS_ST
Campo 25: VL_IPI
Campo 26: VL_PIS
Campo 27: VL_COFINS
Campo 28: VL_PIS_ST
Campo 29: VL_COFINS_ST

O campo 11 que deve ser preenchido como vazio, ou seja, “||”: 
Campo 11: DT_E_S 

O C170 também deve ser gravado normalmente, mas aplicando-se a mesma regra citada para o C100, ou seja, apresentar apenas os campos de identificação do documento, mais os campos QTD, VL_ITEM e VL_ICMS. [MFS-36422]
Apresentar o valor zero (0,00) para os campos listados abaixo: 

- VL_DESC
- VL_BC_ICMS
- ALIQ_ICMS
- VL_ICMS [MFS-36422]
- VL_BC_ICMS_ST
- ALIQ_ST
- VL_ICMS_ST
- VL_BC_IPI
- ALIQ_IPI
- VL_IPI
- VL_BC_PIS
- ALIQ_PIS
- QUANT_BC_PIS
- ALIQ_PIS
- VL_PIS
- VL_BC_COFINS
- ALIQ_COFINS
- QUANT_BC_COFINS
- ALIQ_COFINS
- VL_COFINS

O registro C190, os campos abaixo devem ser gerados normalmente:
Campo 01: REG
Campo 02: CST_ICMS
Campo 03: CFOP
Campo 05: VL_OPR
Campo 07: VL_ICMS [MFS-36422]
Campo 10: VL_RED_BC

Os campos abaixo devem ser preenchido com zeros, são eles:
Campo 04: ALIQ_ICMS
Campo 06: VL_BC_ICMS
Campo 07: VL_ICMS[MFS-36422]
Campo 08: VL_BC_ICMS_ST
Campo 09: VL_ICMS_ST
Campo 11: VL_IPI
		Obs		
[MFS628422] Inclusão do tratamento para NF de Transferência de Crédito, quando o parâmetro 96 da tela de Parâmetros por UF estiver marcado

NF de Transferência de Crédito – Parâmetro 96 
(IND_TRANSF_CRED = 1 e Parâmetro 96 = marcado)

Esta regra apenas deverá ser aplicada se for enquadrada na seguinte condição:

Se a UF do Estabelecimento estiver com o parâmetro “96-Tratamento da Transferência de Crédito - Compensação (P9)” marcado
     E o campo 74 da SAFX07, Nota Fiscal Transferência de Crédito/ Débito (IND_TRANSF_CRED) = 1 (Transferência de Crédito);
Obs.: Parâmetro 96 da tela de Parâmetros por UF (módulo ICMS)		Escrituração Mastersaf	P1/P2 - A nota é lançada no livro sem os valores
P8/P9 – A nota é considerada no resumo da apuração		Regra do Validador	(não consta)		Gravação do C100 e filhos	Esta nota deverá ser gravada com o código de situação = ‘08’ (COD_SIT do C100). 

No registro C100, Apresentar o valor zero (0,00) para os campos listados abaixo: 
Campo 14 : VL_DESC
Campo 15: VL_ABAT_NT
Campo 16: VL_MERC
Campo 18: VL_FRT
Campo 19: VL_SEG
Campo 20: VL_OUT_DA
Campo 21: VL_BC_ICMS
Campo 23: VL_BC_ICMS_ST
Campo 24: VL_ICMS_ST
Campo 25: VL_IPI
Campo 26: VL_PIS
Campo 27: VL_COFINS
Campo 28: VL_PIS_ST
Campo 29: VL_COFINS_ST

O campo 11 que deve ser preenchido como vazio, ou seja, “||”: 
Campo 11: DT_E_S 
Obs.: O campo 22 – VL_ICMS deve ser preenchido.

O C170 também deve ser gravado normalmente (quando houver itens), mas aplicando-se a mesma regra citada para o C100, ou seja, apresentar apenas os campos de identificação do documento, mais os campos QTD, VL_ITEM e VL_ICMS. 
Apresentar o valor zero (0,00) para os campos listados abaixo: 

- VL_DESC
- VL_BC_ICMS
- ALIQ_ICMS
- VL_BC_ICMS_ST
- ALIQ_ST
- VL_ICMS_ST
- VL_BC_IPI
- ALIQ_IPI
- VL_IPI
- VL_BC_PIS
- ALIQ_PIS
- QUANT_BC_PIS
- ALIQ_PIS
- VL_PIS
- VL_BC_COFINS
- ALIQ_COFINS
- QUANT_BC_COFINS
- ALIQ_COFINS
- VL_COFINS

O registro C190, os campos abaixo devem ser gerados normalmente:
Campo 01: REG
Campo 02: CST_ICMS
Campo 03: CFOP
Campo 05: VL_OPR
Campo 07: VL_ICMS
Campo 10: VL_RED_BC

Os campos abaixo devem ser preenchido com zeros, são eles:
Campo 04: ALIQ_ICMS
Campo 06: VL_BC_ICMS
Campo 08: VL_BC_ICMS_ST
Campo 09: VL_ICMS_ST
Campo 11: VL_IPI
		Obs		
[ALTERADA - CH15343_2013/ MFS-20986]

NFC Eletrônica 
(COD_MOD = 65)
		Escrituração Mastersaf	Não existe nenhum tratamento especial nos livros.		Regra do Validador	Via de regra, devem ser apresentados somente os registros C100 e C190 e, se existirem ajustes de documento fiscais determinados por legislação estadual (tabela 5.3 do Ato COTEPE ICMS 09/08), devem ser apresentados também os registros C195 e C197.
		Gravação do C100 e filhos	Gerar de acordo com as regras do validador:
Gerar o C100 normalmente, não devem ser informados os campos COD_PART, VL_BC_ICMS_ST, VL_ICMS_ST, VL_IPI, VL_PIS, VL_COFINS, VL_PIS_ST e VL_COFINS_ST. Os demais campos seguirão a obrigatoriedade definida pelo registro. As NFC-e não devem ser escrituradas nas entradas, mas isso está sendo tratado direto no documento matriz do Bloco C.
Não gerar os registros filhos, exceto o C190, C195 e C197 (os dois últimos serão de responsabilidade do contribuinte de acordo com sua legislação vigente).
		
NF Simples Faturamento e 
parâmetro de Dados Iniciais = ‘00’

[MFS75220] Inclusão do tratamento do parâmetro que indica a forma de preenchimento do campo 06 do registro C100

(IND_SITUACAO_ESP = ‘D’ e CFOP’s =  “1922, 2922, 3922, 1117, 2117, 3117, 5922, 6922, 7922, 5116, 6116 ou 7116” (campos 14 da SAFX07, 22 da SAFX08 ou 17 da SAFX09 – COD_CFOP) e o parâmetro “Preenchimento do Campo 06-Código da Situação para notas fiscais em consignação e de simples faturamento”  igual a ‘00’ da tela de dados iniciais 
		Escrituração Mastersaf	P1 e P2 - A nota é lançada apenas com os dados de identificação (sem os valores)
P8/P9 - Desconsiderar as notas fiscais de simples faturamento, já que os seus valores não serão considerados nos livros P1, P1A, P2 e P2A. Esta alteração deve ser feita tanto na apuração do ICMS, como do ICMS-ST também, tendo em vista que a apuração do ICMS-ST é “embutida” na apuração do ICMS, ou seja, as duas são realizadas no mesmo item simultaneamente.		Regra do Validador	(não consta)		Gravação do C100 e filhos	O sistema deve considerar a seguinte parametrização para a geração do C100 e filhos:

Módulo: SPED ( EFD – Escrituração Fiscal Digital 
Menu: Parâmetros ( Dados Iniciais
Parâmetro: “Preenchimento do Campo 06-Código da Situação para notas fiscais em consignação e de simples faturamento” igual a ‘00’

Esta nota deverá ser gravada com o código de situação = ‘00’ (COD_SIT do C100). 

Preencher todos os campos do C100 e apresentar o valor zero (0,00) para os campos listados abaixo: 

-VL_DOC
- VL_MERC

Os outros registros filhos são facultativos, exceto o C190.
O C170 também deve ser gravado normalmente, mas aplicando-se a mesma regra citada para o C100, ou seja, apresentar todos os campos do documento.
Apresentar o valor zero (0,00) para o campo listado abaixo: 

- VL_ITEM

O C190 deve totalizar a escrituração dos documentos fiscais/itens, aplicar também a regra citada no registro C100.
Apresentar o valor zero (0,00) para o campo listado abaixo: 

- VL_OPR
		Obs		
NF em consignação e 
parâmetro de Dados Iniciais = ‘00’

[MFS75220] Inclusão do tratamento do parâmetro que indica a forma de preenchimento do campo 06 do registro C100
[MFS670091] Inclusão do preenchimento do campo 20 - VL_OUT_DA do registro C100 com zero.

Nota Fiscal com CFOP parametrizado em NF’s em Consignação e o parâmetro “Preenchimento do Campo 06-Código da Situação para notas fiscais em consignação e de simples faturamento”  igual a ‘00’ da tela de dados iniciais 
		Escrituração Mastersaf	(não consta)		Regra do Validador	(não consta)		Gravação do C100 e filhos	O sistema deve considerar as seguintes parametrizações para a geração do C100 e filhos:

Módulo: SPED ( EFD – Escrituração Fiscal Digital 
Menu: Parâmetros ( Dados Iniciais
Parâmetro: “Preenchimento do Campo 06-Código da Situação para notas fiscais em consignação e de simples faturamento” igual a ‘00’

Módulo: SPED ( EFD – Escrituração Fiscal Digital 
Menu: Parâmetros ( Registro C100 ( NF’s em Consignação - CFOP

Esta nota deverá ser gravada com o código de situação = ‘00’ (COD_SIT do C100). 

Preencher todos os campos do C100 e apresentar o valor zero (0,00) para os campos listados abaixo: 

- VL_DOC
- VL_MERC
- VL_OUT_DA

Os outros registros filhos são facultativos, exceto o C190.
O C170 também deve ser gravado normalmente, mas aplicando-se a mesma regra citada para o C100, ou seja, apresentar todos os campos do documento e apresentar o valor zero (0,00) para o campo listado abaixo: 

- VL_ITEM

O C190 deve totalizar a escrituração dos documentos fiscais/itens, aplicar também a regra citada no registro C100.
Apresentar o valor zero (0,00) para o campo listado abaixo: 

- VL_OPR
		Obs