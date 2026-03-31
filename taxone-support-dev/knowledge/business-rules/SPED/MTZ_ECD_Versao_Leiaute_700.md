# MTZ_ECD_Versao_Leiaute_700

> Fonte: MTZ_ECD_Versao_Leiaute_700.doc

THOMSON REUTERS

ECD
Atualização da Geração do Arquivo para atender ao Leiaute 7.00


DOCUMENTO DE REQUISITO

OS/CH	Nome	Descrição		MFS-8216	Lara Aline	Atualização das Informações do arquivo da ECD para atender à versão 5.00 do Leiaute da ECD.		MFS-8620	Lara Aline	Atualização das Informações do arquivo da ECD para atender à versão 5.00 do Leiaute da ECD.		CH21396/2016	Lara Aline	Ajuste na geração do campo 02 - COD_CTA_RES do I015 para os livros auxiliares (A e Z).		MFS-9689	Lara Aline	Atualização das Informações do arquivo da ECD para atender à versão 5.00 do Leiaute da ECD. De acordo com as orientações do PVA versão 4.0.0.		MFS9809/
CH2989/2017	Andrea Rocha	Atualização das informações do bloco K		MFS10727	Lara Aline	Ajuste na regra do Campo 02 – COD_PLAN_REF do Registro I051.		MFS-10358	Lara Aline	Atualização das Informações do arquivo da ECD para atender o Bloco K na versão 5.00 do Leiaute da ECD.		CH8476_2017 (MFS-10940)	Julyana Perrucini	Alteração da regra de preenchimento do campo 03 do Registro J930.		MFS-13062	Julyana Perrucini	Este documento tem como objetivo criar parametrização na tela de Dados para que o usuário possa informar como deseja gerar o Registro I015, se pela conta parametrizada em Livros Auxiliares ao Diário sem associação da conta analítica com a sintética ou se pela associação da conta analítica com a conta sintética.		MFS15525	João Henrique	Este documento tem como objetivo realizar a primeira parte das atualizações do SPED Contábil nos registros I010, J100, J150 e J210.		MFS15698	João Henrique	Este documento tem como objetivo realizar a segunda parte das atualizações do SPED Contábil. Nos registros J100, J150 e J210 será incluído o campo com a informação das Notas Explicativas através da SAFX257 ou da Tela de Manutenção das Notas Explicativas dos Demonstrativos Contábeis.		MFS11946	João Henrique	Esse documento tem como objetivo criar a regra de preenchimento do código do participante para os registros 0150 e 0180 quando a empresa não possui movimentação contábil. 		MFS17214	João Henrique	Esse documento tem como objetivo realizar o tratamento no preenchimento do campo 08 PER_CONS do registro K100 do ECD.		MFS17883	João Henrique	Essa atualização legal tem como objetivo atender o Ato ADE Cofis nº27/2018. As alterações são nos registros I051, J100. J150, J210.		MFS18238	João Henrique	Essa alteração tem como finalidade mapear diversas contas de empresas controladas a uma determinada conta analítica do plano de contas.		MFS23322	João Henrique	Essa demanda tem como objetivo realizar a segunda parte das atualizações do SPED Contábil 2019 nos registros I010 e I200 em relação a geração do arquivo magnético.		MFS22414	João Henrique	Essa demanda tem como objetivo realizar a terceira parte das atualizações do SPED Contábil 2019 referente ao bloco J – Demonstrações Contábeis.		MFS26093	Andréa Rocha	Essa demanda tem como objetivo criar a regra para a geração do registro J005.		MFS-31598	Jorge Neto	Geração dos registros do bloco K somente em dezembro.		MFS-29278	Alessandra Cristina Navatta	Ajustar as regras da recuperação das demonstrações contábeis, considerando a nova solução criada nas demandas da reestruturação da ECD (tela Geração das Demonstrações Contábeis).		MFS-35407	Alessandra Cristina Navatta	Gerar as demonstrações contábeis no arquivo, se as mesmas foram processadas na tela de demonstração contábil (considerando o período da geração do arquivo) e se as mesmas estiverem geradas e selecionadas no perfil de geração. 		

REGRAS DE NEGÓCIO


CÓD	DESCRIÇÃO	OS/CH		RN00	Regra Geral

Este documento tem como objetivo demonstrar as alterações da versão 5.00 do leiaute da ECD em relação à versão 4.00. Este novo leiaute será obrigatório a partir do ano-calendário 2016.

Todos os registros deverão ser mantidos conforme layout anterior, incluindo as alterações e criação dos novos registros que estarão definidos nas regras de negócios descritas neste documento, documento de requisito e documentos matriz relacionados na alteração da versão.
	MFS-8216		

Alterações Registro 0000

CÓD	DESCRIÇÃO	OS/CH		RN0000-14	Registro 0000 – Campo 14 – IND_FIN_ESC

Indicador de Finalidade de Escrituração

Preencher com ‘0’ se na tela de geração o indicador de finalidade de escrituração estiver selecionado: ‘0 – Original’;
Preencher com ‘1’ se na tela de geração o indicador de finalidade de escrituração estiver selecionado: ‘1 – Substituta’

Campo de preenchimento obrigatório. 
	MFS-8216		RN0000-16	[EXCLUÌDO] Registro 0000 – Campo 16 – NIRE_SUBST.

Este campo foi excluído a partir do layout da versão 5.00. 

Importante: Deverá ser reposicionada a numeração dos campos posteriores.	MFS-8216		RN0000-20	Registro 0000 – Campo 20 – IND_ESC_CONS

Este campo existe a partir da versão 5.00. Inicialmente será gerado com conteúdo fixo: “N”

Será gerado conforme parâmetro “Escriturações Contábeis Consolidadas” da tela de Dados Iniciais (menu Parâmetros):
Se o referido parâmetro estiver desmarcado, será gerado com conteúdo “N”.
Se o parâmetro estiver selecionado, será gerado com conteúdo “S”.	MFS-8216
MFS-10358		

Alterações Registro 0150

CÓD	DESCRIÇÃO	OS/CH		RN0150-02	Registro 0150 – Campo 02 – COD_PART

Se o parâmetro “Gerar Código do Participante (SAFX39) ” estiver marcado na tela de Dados Iniciais (SPED >> ECD – Escrituração Contábil Digital >> Parâmetros >> Dados Iniciais):

Buscar o  GRUPO_ESTAB da tabela RELAC_TAB_GRUPO com maior validade inicial.

A rotina de geração deverá verificar os registros da SAFX39 - Identificação do Relacionamento e realizar a seguinte validação: Verificar se os registros da tabela em que a DT_INI_REL for <= que a data final do arquivo ECD E a DT_FIN_REL for > = a data inicial do arquivo ECD OU for ‘nula’ <= que a data final de geração do arquivo da ECD.

Através da maior data de validade, buscar o IDENT_FIS_JUR que possua o mesmo Grupo, COD_FIS_JUR e IND_FIS_JUR,  demais informações na SAFX04 para geração dos registros 0150.

Caso não possua registros na SAFX04, o sistema não irá gerar o registro 0150.

Se o parâmetro “Gerar Código do Participante (SAFX39) ” estiver desmarcado na tela de Dados Iniciais (SPED >> ECD – Escrituração Contábil Digital >> Parâmetros >> Dados Iniciais) a regra de geração deve se manter inalterada, gerando a partir do participante movimentado (na SAFX01).	
MFS-11946		

Alterações Registro 0180

CÓD	DESCRIÇÃO	OS/CH		RN0180-02	Registro 0180 – Campo 03 – COD_REL

Se o parâmetro “Gerar Código do Participante (SAFX39)” estiver marcado na tela de Dados Iniciais (SPED >> ECD – Escrituração Contábil Digital >> Parâmetros >> Dados Iniciais), o sistema deverá recuperar o código  de relacionamento
do participante da SAFX39 localizado tela de cadastro da Pessoa Física/Jurídica onde a DT_INI_REL for <= que a data final do arquivo ECD E a DT_FIN_REL for > = a data inicial do arquivo ECD OU for ‘nula’ <= que a data final de geração do arquivo da ECD.

Se o parâmetro “Gerar Código do Participante (SAFX39)” estiver desmarcado na tela de Dados Iniciais (SPED >> ECD – Escrituração Contábil Digital >> Parâmetros >> Dados Iniciais) a regra de geração deve se manter inalterada, gerando a partir do participante movimentado (na SAFX01).
	
MFS-11946		

Alterações Registro I010

CÓD	DESCRIÇÃO	OS/CH		RNI010-03	Registro I010 – Campo 03 – COD_VER_LC

Para a versão 5.00, será gerado com o código “5.00”. 
Para a versão 6.00, será gerado com o código “6.00”. Essa atualização se faz necessária a partir do ano calendário de 2017.
Para a versão 7.00, será gerado com o código “7.00”. Essa atualização se faz necessária a partir do ano calendário de 2018.

	MFS-8216
MFS-15525
MFS23322		

Alterações Registro I200

CÓD	DESCRIÇÃO	OS/CH		RNI200-05	Registro I200 – Campo 05 – IND_LCTO

Neste campo são apresentadas as opções do “Indicador do Tipo de Lançamento”, recuperado através do TIPO_LANCTO.

Regras:
As opções válidas para o campo são:

‘N’ – Lançamento Normal (todos os lançamentos exceto os de encerramento das contas de resultado).
‘E’ – Lançamento de Encerramento de contas de resultado.
‘X’ – Lançamento Extemporâneo – Nova Opção (MFS-22309)

As validações necessárias encontram-se na Importação/Manutenção das SAFX.

Cada SAFX é destinada a um tipo de livro na geração do arquivo da ECD:
SAFX01 - Arquivo ContábilSAFX101 - Arquivo Contábil AuxiliarSAFX225 - Lançamento Contábil em Moeda FuncionalSAFX228 - Lançamento Contábil Auxiliar em Moeda Funcional

Tipo: Alfanumérico
Tamanho: 1 Posição
	MFS23322		RNI200-06	Registro I200 – Campo 06 – DT_LCTO_EXT

Neste campo o usuário informa a Data do Lançamento Extemporâneo, se o “Indicador de Lançamento” estiver preenchido com a opção “X”. As validações necessárias encontram-se na Importação/Manutenção das tabelas:

SAFX01 - Arquivo ContábilSAFX101 - Arquivo Contábil AuxiliarSAFX225 - Lançamento Contábil em Moeda FuncionalSAFX228 - Lançamento Contábil Auxiliar em Moeda Funcional

Tipo: Numérico
Tamanho: 8 Posições
	MFS-22309		
Alterações Registro I015

CÓD	DESCRIÇÃO	OS/CH		RNI015-02	Registro I015 – Campo 02 – COD_CTA_RES

[ALTERADA – MFS-13062]
Se a opção “Gerar Conta Resumida parametrizada em Livros Auxiliares ao Diário”, localizada na aba Dados Iniciais da tela Dados Iniciais do item de menu Parâmetros da ECD, estiver desmarcada, então:

Para os livros auxiliares ‘A’ ou ‘Z’ nesse campo será gerada a informação da conta sintética (campo COD_CONTA_SINT da SAFX2002) associada à conta analítica movimentada encontrada, nesse caso será gerada sempre a primeira conta sintética encontrada. Exemplo:

Conta
Tipo
Conta Pai
Nível


1.1.1
S

1


1.1.1.01
S
1.1.1
2


1.1.1.01.0001
A
1.1.1.01
3


1.1.1.01.0001.01
A
1.1.1.01.0001
4


------\\------


Livros Auxiliares ao Diário
1.1.1.01.0001


Auxiliar


Como deve ser gerado:


I015 - 1.1.1.01


I050 - 1.1.1


I050 - 1.1.1.01


I050 - 1.1.1.01.0001


No caso do exemplo acima para a conta analítica 1.1.1.01.0001 está associada a conta sintética 1.1.1.01, que será gerado no registro I015 para os livros ‘A’ ou ‘Z’.

Obs.: Para os outros Livros a geração desse campo continua conforme o padrão, ou seja, gerando a conta analítica movimentada encontrada.

Se a opção “Gerar Conta Resumida parametrizada em Livros Auxiliares ao Diário”, localizada na aba Dados Iniciais da tela Dados Iniciais do item de menu Parâmetros da ECD, estiver marcada, então:

Para os livros auxiliares ‘A’ ou ‘Z’ nesse campo será gerada a informação da conta contábil parametrizada em Livros Auxiliares ao Diário, localizada no item de menu Parâmetros da ECD, sem a necessidade de associar a conta sintética.
	CH21396_2016
MFS-13062		

Alterações Registro I051

CÓD	DESCRIÇÃO	OS/CH		RNI051-02	Registro I051 – Campo 02 – COD_PLAN_REF

A partir da versão 5.00 nesse campo foi incluído um novo Código da Entidade “10- Financeiras – Lucro Presumido” e foi alterado o tamanho do campo para 2 posições.

A partir da versão 5.00 este registro será gerado apenas quando o Código da Entidade for igual a “1 - PJ em Geral”, ”2 - PJ em Geral - Lucro Presumido”, “3 – Financeiras”, “4 – Seguradoras”, “5 - Imunes e Isentas em Geral”, “6 - Financeiras - Imunes e Isentas”, “7 - Seguradoras - Imunes e Isentas”, “8 - Entidades Fechadas de Previdência Complementar”, “9 - Partidos Políticos”. ou “10- Financeiras – Lucro Presumido/ Secretaria da Receita Federal” ou “10 – Financeiras – Lucro Presumido”, (obs. A partir de 2015)

Caso o usuário não tenha realizado parametrização para uma destas entidades indicadas acima em Dados Iniciais e/ou Plano de Contas Referencial X Plano de Contas Empresa e esteja gerando a versão 5.00 do Leiaute, será demonstrada uma mensagem no log: “A partir da versão 5.00 do leiaute não serão válidas as Contas Referenciais de entidade 00-SUSEP ou 20- Banco Central do Brasil (COSIF)”.	MFS8620
MFS10727
MFS17883		
Alterações Registro I052

CÓD	DESCRIÇÃO	OS/CH		RGI052	Regra Geral

Se os registros J100 E J150 estiverem preenchidos com o indicador 03 – IND_COD_AGL, campos 07 e 08 da SAFX2102 DIFERENTE de ‘T’, o código de aglutinação, campo 02 – COD_ALG deve ser apresentado no registro I052.

Então, são gerados no registro I052 apenas as aglutinações de detalhe:

Balanço Patrimonial – J100
Se o código de aglutinação for classificado como “1 - Ativo” ou “2 - Passivo” campo 07 da SAFX2102, na geração do registro J100 da ECD esse indicador é preenchido com a opção “D”.

Demonstração de Resultado do Exercício – J150
Se o código de aglutinação for classificado como “1 – Receita/Despesa” ou “3 - Receita” ou “4 - Despesa” campo 08 da SAFX2102, na geração do registro J150 da ECD, esse campo é preenchido com a opção “D”.
	MFS-22414		
Alterações Registro I053

CÓD	DESCRIÇÃO	OS/CH		RNI053-04	Registro I053 – Campo 04 – NAT_SUB_CNT

Será gerado com o conteúdo do campo Natureza da Subconta da tela de Subconta Correlata.

Não deverão ser considerados os códigos de Natureza da Subconta que estejam fora do período de validade na TACES90. 
	MFS-8216		

Alterações Registro J005

CÓD	DESCRIÇÃO	OS/CH		RNJ005	Regra Geral – Registro J005

[EXCLUÍDA MFS-29278]
O registro J005 somente será gerado se pelo menos um dos parâmetros abaixo estiver marcado na tela de geração do meio magnético:
- Balanço Patrimonial
- Demonstração do Resultado

Obs: Esta regra só deve ser feita a partir da versão 7.00.

[Alteração MFS-29278]:
Recuperar a demonstração de acordo com o campo Período do Arquivo da ECD (tela de Geração das Demonstrações Contábeis). As demonstrações serão recuperadas se o campo do período do arquivo coincidir com o período de geração do meio magnético e o parâmetro Apenas Conferência da tela de geração das demonstrações contábeis, estiver selecionado como ‘Não’. Neste cenário, considerar a informação da geração da demonstração processada. 

Alteração MFS-35407]
Além das regras de recuperação das demonstrações mencionadas acima, as demonstrações contábeis (bloco J) só devem ser apresentadas no arquivo, se estiverem marcadas no perfil de geração.
	MFS-26093
MFS-29278
MFS-35407		

Alterações Registro J100

CÓD	DESCRIÇÃO	OS/CH		RNJ100-03	Registro J100 – Campo 03 – IND_COD_AGL


[EXCLUÍDA MFS-29278]

Nesse campo o sistema preenche com o tipo do código de aglutinação das linhas. As opções válidas são:

‘T’ – Totalizador (nível que totaliza um ou mais níveis inferiores da demonstração financeira).
‘D’ – Detalhe (nível mais detalhado da demonstração financeira).

Regras:
Se o código de aglutinação for classificado como “1 - Ativo” ou “2 - Passivo” campo 07 da SAFX2102, na geração do registro J100 da ECD esse indicador é preenchido com a opção “D”.
Se o código de aglutinação for classificado como “3 - Subtotalizador/Totalizador do Ativo” ou “4 - Subtotalizador/Totalizador do Passivo ou PL” campo 07 da SAFX2102, na geração do registro J100 da ECD esse indicador é preenchido com a opção “T”.

Campo Obrigatório.
1 posição – Caractere

[Alteração MFS-29278]:

Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis.	MFS-22414
MFS-29278		RNJ100-05	Registro J100 – Campo 05 – COD_ALG_SUP

[EXCLUÍDA MFS-29278]

Nesse campo o sistema preenche com o código de aglutinação sintético/grupo de código de aglutinação de nível superior. 

Regras:
Verificar os códigos de aglutinação parametrizados no campo 10 - EXPRESSAO_ORD que são totalizadores, ou seja, opções “3 - Subtotalizador/Totalizador do Ativo” ou “4 - Subtotalizador/Totalizador do Passivo ou PL” campo 07 da tabela SAFX2102 para buscar e preencher com a conta de nível superior “Conta Mãe” na geração do arquivo magnético da ECD.

Exemplo:


[Alteração MFS-29278]:

Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis.
	MFS-22414
MFS-29278		RNJ100-06	Registro J100 – Campo 06 – IND_GRP_BAL

[EXCLUÍDA MFS-29278]
Nesse campo o sistema preenche com o indicador de grupo do balanço campo 07 da SAFX2102. Até o layout 6.0 o campo é gerado da seguinte forma: 
‘1’ – Ativo
‘2’ – Passivo e Patrimônio Líquido
‘3’ – Subtotalizador/Totalizador do Ativo
‘4’ – Subtotalizador/Totalizador do Passivo ou PL


[Alteração MFS-29278]:

Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis e aplicar as regras abaixo:


Regras:
A partir do layout 7.0 na geração do arquivo magnético o sistema deverá preencher da seguinte forma:
Se a opção do campo for igual a ‘1’ ou ‘3’, na geração do arquivo preencher como “A” – Ativo.
Se a opção do campo for igual a ‘2’ ou ‘4’, na geração do arquivo preencher como “P” – Passivo e Patrimônio Líquido.

Campo obrigatório
1 posição
Caractere
	MFS-22414
MFS-29278		RNJ100-12	Registro J100 – Campo 12 – NOTA_EXP_REF

Esse campo deverá ser gerado com pipe “||”. A solução será desenvolvida em uma próxima MFS do SPED Contábil 
Observação: Esse campo será gerado a partir da versão 6.00 do ECD.

[EXCLUÍDA MFS-29278]
Recuperar o campo 10 – NOTA_EXP_REF 11 – NOTA_EXP_NUM_REF do registro J100 com base no IND_BALANCO_DRE = ‘B’ associados ao código de aglutinação, considerando como período de referência para seleção dos registros o mês e ano da data informada no campo 03 - DT_FIN do registro J005 (desta forma atendemos geração anual, trimestral e semestral) em relação à DAT_DEMONSTRACAO da tabela SAFX257 mais atual, limitado ao final do período de geração do arquivo magnético.

12 posições – Caractere

[Alteração MFS-29278]:

Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis

	MFS-15525
MFS-15698
MFS-22414
MFS-29278		


Alterações Registro J150

CÓD	DESCRIÇÃO	OS/CH		RNJ150-03	Registro J150 – Campo 03 – IND_COD_AGL


[EXCLUÍDA MFS-29278]
Nesse campo o sistema preenche com o tipo do código de aglutinação das linhas. As opções válidas são:

‘T’ – Totalizador (nível que totaliza um ou mais níveis inferiores da demonstração financeira).
‘D’ – Detalhe (nível mais detalhado da demonstração financeira)

Regras:
Se o código de aglutinação for classificado como “1 – Receita/Despesa” ou “3 - Receita” ou “4 - Despesa” campo 08 da SAFX2102, na geração do registro J150 da ECD, esse campo é preenchido com a opção “D”.
Se o código de aglutinação for classificado como “2 - Subtotalizador/Totalizador da DRE” ou “5 - Subtotalizador/Totalizador de Receita” ou “6 - Subtotalizador/Totalizador de Despesa” campo 08 da SAFX2102, na geração do registro J150 da ECD esse campo é preenchido com a opção “T”.

Campo Obrigatório.
1 posição – Caractere


[Alteração MFS-29278]:

Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis

	MFS-22414
MFS-29278		RNJ150-05	Registro J150 – Campo 05 – COD_ALG_SUP

[EXCLUÍDA MFS-29278]
Nesse campo o sistema preenche com o código de aglutinação sintético/grupo de código de aglutinação de nível superior. 

Regras:
Verificar os códigos de aglutinação parametrizados no campo 10 - EXPRESSAO_ORD que são totalizadores, ou seja, opções “2 - Subtotalizador/Totalizador da DRE” ou “5 - Subtotalizador/Totalizador de Receita” ou “6 - Subtotalizador/Totalizador de Despesa” campo 08 da tabela SAFX2102 para buscar e preencher com a conta de nível superior “Conta Mãe” na geração do arquivo magnético da ECD.

Exemplo:
 EMBED PBrush  


[Alteração MFS-29278]:

Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis
	MFS-22414
MFS-29278		RNJ150-08	Registro J150 – Campo 08 – IND_DC_CTA


[EXCLUÍDA MFS-29278]
Nesse campo o sistema preenche com o indicador da situação do valor total do código de aglutinação. 

As opções válidas são:
D – Devedor;
C – Credor; 

Regras:
O sistema verifica qual o indicador dos saldos das 2 parcelas:
Se as parcelas são iguais (Débito com Débito, o sistema preenche com “D” ou Crédito com Crédito preenche com “C”), somam-se ou subtraem-se os saldos conforme o operador da expressão. O indicador de débito e crédito final é igual ao das parcelas.

Se as parcelas são diferentes (Débito com Crédito), não importando se a expressão indica soma ou subtração, subtraem-se os valores e o indicador final é o da parcela de maior saldo.
Exemplo: 
Se o saldo da parcela de Débito for > que a parcela do Crédito, o sistema preenche com o indicador “D” para essa aglutinação.
Senão preenche com “C”

Campo Obrigatório.
1 posição – Caractere


[Alteração MFS-29278]:

Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis
	MFS-22414
MFS-29278		RNJ150-09	Registro J150 – Campo 09 – IND_GRP_DRE


[EXCLUÍDA MFS-29278]
Nesse campo o sistema preenche com o indicador de grupo da DRE, as opções válidas são:
‘D’ – Linha totalizadora ou de detalhe da demonstração que, por sua natureza de despesa represente redução do lucro. 
‘R’ – Linha totalizadora ou de detalhe da demonstração que, por sua natureza de receita represente incremento do lucro. 

O preenchimento do indicador de grupo da DRE é baseado nas opções válidas do campo 08 da SAFX2102. Até o layout 6.0, o campo possui os seguintes valores validos: 
‘1’ – Receita/Despesa
‘2’ – Subtotalizador/ Totalizador da DRE

A partir do layout 7.0, este campo passa a ter os seguintes valores válidos:
‘1’ – Receita/Despesa
‘2’ – Subtotalizador/ Totalizador da DRE
‘3’ – Receita (novo)
‘4’ – Despesa (novo)
‘5’ – Subtotalizador/ Totalizador de Receita (novo)
‘6’ – Subtotalizador/ Totalizador de Despesa (novo)

Regras para geração do indicador:

Se para o código de aglutinação o indicador de grupo da DRE estiver preenchido com as opções ‘1’ ou ‘2’, o sistema deve verificar se a conta é Credora ou Devedora através do indicador 08– IND_DC_CTA do J150.

Se a aglutinação for “Devedora”, na geração do arquivo magnético do SPED o IND_GRP_DRE é preenchido com ‘D’
Se a aglutinação for “Credora”, na geração do arquivo magnético do SPED o IND_GRP_DRE é preenchido com ‘R’


Se para o código de aglutinação o indicador de grupo da DRE estiver preenchido com as opções ‘4’ ou ‘6’, na geração do arquivo magnético da ECD esse campo será preenchido com o valor ‘D’.

Se para o código de aglutinação o indicador de grupo da DRE estiver preenchido com as opções ‘3’ ou ‘5’, na geração do arquivo magnético da ECD esse campo será preenchido com o valor ‘R’.


[Alteração MFS-29278]:

Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis

	MFS-22414
MFS-29278		RNJ150-10	Registro J150 – Campo 10 – NOTA_EXP_REF

Esse campo deverá ser gerado com pipe “||”. A solução será desenvolvida em uma próxima MFS do SPED Contábil 
Observação: Esse campo será gerado a partir da versão 6.00 do ECD.


[EXCLUÍDA MFS-29278]
Recuperar o campo 10 – NOTA_EXP_REF 11 – NOTA_EXP_NUM_REF do registro J150 com base no IND_BALANCO_DRE = ‘D’ associados ao código de aglutinação, considerando como período de referência para seleção dos registros o mês e ano da data informada no campo 03 - DT_FIN do registro J005 (desta forma atendemos geração anual, trimestral e semestral) em relação à DAT_DEMONSTRACAO da tabela SAFX257 mais atual, limitado ao final do período de geração do arquivo magnético.

12 posições – Caractere

[Alteração MFS-29278]:

Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis	MFS-15525
MFS-15698
MFS-22414
MFS-29278		


Alterações Registro J200

CÓD	DESCRIÇÃO	OS/CH		RGJ200	Regra Geral:

De acordo com o manual layout de 2018, o registro J200 não faz parte do leiaute 7.0 do SPED Contábil. Este será inibido do perfil de geração da ECD.
	MFS-22414		
.


Alterações Registro J210

CÓD	DESCRIÇÃO	OS/CH		RNJ210-09	Registro J210 – Campo 09 – NOTA_EXP_REF

Esse campo deverá ser gerado com pipe “||”. A solução será desenvolvida em uma próxima MFS do SPED Contábil 
Observação: Esse campo será gerado a partir da versão 6.00 do ECD.

[EXCLUÍDA MFS-29278]
Recuperar o campo 10 – NOTA_EXP_REF 11 – NOTA_EXP_NUM_REF do registro J210 com base no IND_BALANCO_DRE = ‘L’ OU ‘M’ associados ao código de aglutinação, considerando como período de referência para seleção dos registros o mês e ano da data informada no campo 03 - DT_FIN do registro J005 (desta forma atendemos geração anual, trimestral e semestral) em relação à DAT_DEMONSTRACAO da tabela SAFX257 mais atual, limitado ao final do período de geração do arquivo magnético.

12 posições – Caractere

[Alteração MFS-29278]:

Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis	MFS-22414
MFS-29278		

Alterações Registro J215

CÓD	DESCRIÇÃO	OS/CH		RNJ215-03	Registro J215 – Campo 03 – DESC_FAT

[EXCLUÍDA MFS-29278]

Nesse campo o sistema preenche com a descrição do fato contábil, campo 03 – DESCRICAO da SAFX2056.

Campo obrigatório.


[Alteração MFS-29278]:

Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis
	MFS-22414
MFS-29278		


Alterações Registro J800

CÓD	DESCRIÇÃO	OS/CH		RNJ800-02	Registro J800 – Campo 02 – TIPO_DOC

Este campo existe a partir da versão 5.00, porém ele deve ser gerado para todas as versões.

Será gerado o código conforme opção selecionada pelo usuário no campo “Tipo de documento” na Aba Demonstrações Contábeis dos Dados Iniciais (menu Parâmetros) - quadro ‘Outras Informações das Demonstrações Contábeis (Balanço Patrimonial e Demonstração de Resultado)’, conforme opções a seguir:

001: Demonstração do Resultado Abrangente do Período 
002: Demonstração dos Fluxos de Caixa 
003: Demonstração do Valor Adicionado 
010: Notas Explicativas 
011: Relatório da Administração 
012: Parecer dos Auditores 
099: Outros
	MFS-8620
MFS-9689
		RNJ800-03	Registro J800 – Campo 03 – DESC_RTF

Este campo existe a partir da versão 5.00, porém ele deve ser gerado para todas as versões.

Será gerado com o conteúdo do campo Descrição (.rtf) da tela de Dados iniciais/Aba Demonstrações Contábeis - Quadro (Outras Informações das Demonstrações Contábeis (Balanço Patrimonial e Demonstração de Resultado)).	MFS-8620
MFS-9689		RNJ800-04	Registro J800 – Campo 04 – HASH_RTF

Este campo existe a partir da versão 5.00, porém ele deve ser gerado para todas as versões.

Será gerado sem informação (em branco). Pois essa informação será gerada pelo próprio PVA no momento da validação do arquivo.	MFS-8620
MFS-9689
		


Novo Registro J801 - Termo de Verificação para Fins de Substituição da ECD

CÓD	DESCRIÇÃO	OS/CH		RNJ801-00	Registro J801 – Regra Geral

Este registro existe a partir da versão 5.00, porém ele deve ser gerado para todas as versões.

Origem das informações: Tela de Dados Iniciais – Aba Demonstrações Contábeis (Módulo ECD / Menu Parâmetros > Dados Iniciais)

Regra de Seleção: Este registro será gerado sempre que no quadro ‘Termo de Verificação para Fins de Substituição da ECD (Balanço Patrimonial e Demonstração de Resultado)’ na aba Demonstrações Contábeis da tela de Dados Iniciais existir informação de um arquivo RTF.

Campo-chave: ARQ_RTF

Registro pai / Nível hierárquico: J005 / Nível 3

Ocorrência: Um por arquivo
	MFS-8620
MFS-9689		RNJ801-01	Registro J801 – Campo 01 – REG

Informação fixa “J801”.
	MFS-8620		RNJ801-02	Registro J801 – Campo 02 – TIPO_DOC

Nesse registro será gerado o tipo de documento que no caso será 001: Termo de Substituição da ECD.

Valor fixo: 001.

O quadro ‘Termo de Verificação para Fins de Substituição da ECD (Balanço Patrimonial e Demonstração de Resultado)’ foi criado justamente para o usuário informar o arquivo de formato RTF que corresponde apenas ao tipo de documento: Termo de Substituição da ECD. 	MFS-8620		RNJ801-03	Registro J801 – Campo 03 – DESC_RTF

Será gerado com o conteúdo do campo Descrição (.rtf) da tela de Dados iniciais/Aba Demonstrações Contábeis - Quadro (Termo de Verificação para Fins de Substituição da ECD (Balanço Patrimonial e Demonstração de Resultado)).
	MFS-8620		RNJ801-04	Registro J801 – Campo 04 – COD_MOT_SUBS

Nesse campo o sistema preenche com o código do motivo da substituição, as opções válidas são:

001 – Mudanças de saldos das contas que não podem ser realizadas por meio de lançamentos extemporâneos; 
002 – Alteração de assinatura; 
003 – Alteração de demonstrações contábeis; 
004 – Alteração da forma de escrituração contábil; 
005 – Alteração do número do livro;
099 – Outros; 

Regras:
Se o usuário não informar uma opção de código do motivo da substituição, uma mensagem de alerta é exibida na tela: “O campo Código do Motivo da Substituição é obrigatório de preenchimento, informe uma opção”.
Na geração do campo no arquivo magnético do SPED, o sistema preenche com código, referente aos motivos da substituição: “001”; “002”; “003”; “004”; “005”; “099”.

Campo obrigatório.
Caractere
10 posições
	MFS-22414		RNJ801-05	Registro J801 – Campo 05 – HASH_RTF

Será gerado sem informação (em branco). Pois essa informação será gerada pelo próprio PVA no momento da validação do arquivo.
	MFS-8620		RNJ801-06	Registro J801 – Campo 06 – ARQ_RTF

Será gerada uma sequência de bytes que representem um único arquivo no formato RTF (Rich Text Format).
	MFS-8620		RNJ801-07	Registro J801 – Campo 07 – IND_FIM_RTF

Informação fixa “J801FIM”.
	MFS-8620		

Alterações Registro J930

CÓD	DESCRIÇÃO	OS/CH		RNJ930-03	Registro J930 – Campo 03 – IDENT_CPF_CNPJ

Consultar DE-PARA: DE-PARA _SPED Contábil_Conf.IN RFB nº 926.09.xls.

Tratamento:
Se o campo NUM_CPF da tabela RESP_INFORMACAO não estiver preenchido, será verificada a existência do CNPJ no campo NUM_CPF da tabela RESP_CONTADOR, ambos localizados em Básicos > Parâmetros > Requisitos Legais > Responsável pelas informações.
	CH8476_2017 (MFS-10940)		RNJ930-12	Registro J930 – Campo 12 – IND_RESP_LEGAL

Este campo existe a partir da versão 5.00, porém ele dever ser gerado para todas as versões.

Será gerado conforme parâmetro “Indicação do Representante Legal Junto às Bases da RFB” na Aba Signatários dos Dados Iniciais (menu Parâmetros):
Se o referido parâmetro estiver desmarcado, será gerado com conteúdo “N”.
Se o parâmetro estiver selecionado, será gerado com conteúdo “S”.
	MFS-8216
MFS-9689		


Alterações Registro J932

CÓD	DESCRIÇÃO	OS/CH		RGJ932-00	Regra Geral para o registro J932

O registro será obrigatório na geração do arquivo da ECD quando:
O campo 14 – do registro 0000 for igual a “1 – Substituta”.
O Código de Qualificação do SPED for igual ‘910’ ou ‘920’.

Exemplo de geração do registro:

J932|TESTEECD|12345678900|CONTADOR/CONTABILISTA RESPONSÁVEL PELO TERMO DE VERIFICAÇÃO PARA FINS DE SUBSTITUIÇÃO DA ECD|910|1SP123456|TESTEECD@GMAIL.COM|2199999999|RJ|RJ/2012/001|31122020|
	MFS-22414		RNJ932-01	Registro J932 – Campo 01 – REG

Nesse campo o sistema preenche com o valor fixo “J932”.
Campo obrigatório.
	MFS-22414		RGJ932-02	Registro J932 – Campo 02 – IDENT_NOM_T

Nesse campo o sistema preenche com o Nome do Signatário do Termo de Verificação, localizado em: (Básicos > Parâmetros > Requisitos Legais > Responsável por Informações), campo “Nome/Razão Social”.

	MFS-22414		RNJ935-03	Registro J935 – Campo 03 – IDENT_CPF_CNPJ_T

Nesse campo o sistema preenche com o CPF ou CNPJ do assinante do termo de verificação, localizado em: (Básicos > Parâmetros > Requisitos Legais > Responsável por Informações), campo “CPF/CNPJ”.

Regras:
Se o campo estiver preenchido com 14 posições = Pessoa Jurídica - CNPJ
Se o campo estiver preenchido com 11 posições = Pessoa Física - CPF

Tipo: Caractere
14 posições
	MFS-22414		RNJ935-04	Registro J935 – Campo 04 – IDENT_QUALIF_T

Nesse campo o sistema preenche com a Qualificação do assinante do termo de verificação, localizado em: (Básicos > Parâmetros > Requisitos Legais > Responsável por Informações), campo “Qualificação [IN 107/2008]”.
	MFS-22414		RNJ935-05	Registro J935 – Campo 05 – COD_ASSIN_T

Nesse campo o sistema preenche com o Código de qualificação do assinante do termo de verificação, localizado em: (SPED > ECD – Escrituração Contábil Digital > Dados Iniciais > aba de Signatários), campo “ Cod. Qualificação SPED”.

Tipo: Caractere
3 posições
	MFS-22414		RNJ935-06	Registro J935 – Campo 06 – IND_CRC_T

Nesse campo o sistema preenche com o Número de inscrição do contabilista no Conselho Regional de Contabilidade, localizado em: (Básicos > Parâmetros > Requisitos Legais > Responsável por Informações), campo “CRC/Insc. Estadual”.
	MFS-22414		RNJ935-07	Registro J935 – Campo 07 – EMAIL_T

Nesse campo o sistema preenche com o E-mail do Signatário, localizado em: (Básicos > Parâmetros > Requisitos Legais > Responsável por Informações), campo “E-mail”.	MFS-22414		RNJ935-08	Registro J935 – Campo 08 – FONE_T

Nesse campo o sistema preenche com o Telefone do Signatário, localizado em: (Básicos > Parâmetros > Requisitos Legais > Responsável por Informações), conectar o campo “DDD e Telefone”.
	MFS-22414		RNJ935-09	Registro J935 – Campo 09 – UF_CRC_T

Nesse campo o sistema preenche com o Indicação da unidade da federação que expediu o CRC, localizado em: (Básicos > Parâmetros > Requisitos Legais > Responsável por Informações), campo “CRC UF”.
	MFS-22414		RNJ935-10	Registro J935 – Campo 10 – NUM_SEQ_CRC_T

Nesse campo o sistema preenche com o Número da Certidão de Regularidade Profissional do Contador no seguinte formato: UF/ano/número, localizado em: (Básicos > Parâmetros > Requisitos Legais > Responsável por Informações), campo “Num. Sequencial do CRC (Formato UF/Ano/Nº) ”.
	MFS-22414		RNJ935-11	Registro J935 – Campo 11 – DT_CRC_T

Nesse campo o sistema preenche com o Data de validade da Certidão de Regularidade Profissional do Contador, localizado em: (Básicos > Parâmetros > Requisitos Legais > Responsável por Informações), campo “Data Validade CRC”.
	MFS-22414		

Alterações Registro J935

CÓD	DESCRIÇÃO	OS/CH		RNJ935-02	Registro J935 – Campo 02 – NI_CPF_CNPJ

Nesse campo o sistema preenche com o documento do auditor independente CPF ou CNPJ, localizado em: (SPED > ECD – Escrituração Contábil Digital > Dados Iniciais > aba de Auditores Independentes), campo Documento do Auditor Independente”.

Regras:
Se o campo estiver preenchido com 14 posições = Pessoa Jurídica - CNPJ
Se o campo estiver preenchido com 11 posições = Pessoa Física - CPF

Campo Obrigatório
Caractere
14 posições 
	MFS-22414		RNJ935-04	Registro J935 – Campo 04 – COD_CVM_AUDITOR

Nesse campo o sistema preenche com o registro do auditor independente na CVM, localizado em: (SPED > ECD – Escrituração Contábil Digital > Dados Iniciais > aba de Auditores Independentes), campo “Registro do Auditor no CVM”.
	MFS-22414		
Inclusão do Bloco K - Conglomerados Econômicos (Facultativo para o ano-calendário 2016)


CÓD	DESCRIÇÃO	OS/CH		RNK001	Registro K001 – Abertura do Bloco K

A princípio não atenderemos a geração do Bloco K - Conglomerados Econômicos (Facultativo para o ano-calendário 2016), porém deverão ser gerados pelo menos os registros de Abertura e Encerramento do Bloco K.

Registro abertura: K001

	MFS8216
MFS-10358		RNK001-01	Registro K001 – Campo 1 – REG

Informação fixa “K001”.
	MFS9809		RNK001-02	Registro K001 – Campo 2 – IND_DAD

Indicador de movimento: 
Bloco com dados informados; 
Bloco sem dados informados.

Gravar a informação de acordo com os dados encontrados para esse bloco se houver dados informados gravar = 0 - Bloco com dados informados, se não encontrar dados gravar = 1 - Bloco sem dados informados.

Informação fixa “1”.

Obs.: Como a princípio não atenderemos a geração do Bloco K, o conteúdo deste campo será fixo igual a “1” (Bloco sem dados informados). 
	MFS9809
MFS-10358		RNK030-00	Registro K030 – Regra geral

Origem da Informação: SAFX240 - Relação das Empresas Consolidadas.

Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00” e a data final de geração for Dezembro, a estrutura do registro K030 será gerada conforme definida neste documento.

Como este registro é de geração facultativa, pode ocorrer do usuário não tê-lo selecionado no Perfil (menu Parâmetros >> Perfil). Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K030 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K030 – Período da Escrituração Contábil Consolidada”.


parâmetro “Escriturações Contábeis Consolidadas” da tela de Dados Iniciais (menu Parâmetros)

Campo-chave: DT_INI 

Registro pai / Nível hierárquico: K030 / Nível 2

Ocorrência: Um por arquivo.

	MFS-10358
MFS-31598		RNK030-01	Registro K030 – Campo 1 – REG

Informação fixa “K030”.
	MFS-10358		RNK030-02	Registro K030 – Campo 2 – DT_INI

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Data Inicial do período consolidado.
	MFS-10358		RNK030-03	Registro K030 – Campo 3 – DT_FIN

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Data Final do período consolidado.
	MFS-10358		RNK100-00	Registro K100 – Regra geral

Origem da Informação: SAFX240 - Relação das Empresas Consolidadas.

Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K100 será gerada conforme definida neste documento. 

Como este registro é de geração facultativa, pode ocorrer do usuário não tê-lo selecionado no Perfil (menu Parâmetros >> Perfil). Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K100 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K100 – Relação das Empresas Consolidadas”.

Campo-chave: EMP_COD

Registro pai / Nível hierárquico: K100 / Nível 3

Ocorrência: Vários por arquivo.

	MFS-10358		RNK100-01	Registro K100 – Campo 1 – REG

Informação fixa “K100”. 
	MFS-10358		RNK100-02	Registro K100 – Campo 2 – COD_PAIS

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código do País. 
	MFS-10358		RNK100-03	Registro K100 – Campo 3 – EMP_COD

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da Empresa Participante.
	MFS-10358		RNK100-04	Registro K100 – Campo 4 – CNPJ

Considerando a Origem da Informação, demonstrar aqui APENAS os primeiros 8 dígitos do conteúdo informado no campo CNPJ da Empresa Participante. 
	MFS-10358		RNK100-05	Registro K100 – Campo 5 – NOME

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Nome da Empresa Participante.
	MFS-10358		RNK100-06	Registro K100 – Campo 6 – PER_PART

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Percentual de Participação Total.
	MFS-10358		RNK100-07	Registro K100 – Campo 7 – EVENTO

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Evento Ocorrido no Período.
	MFS-10358		RNK100-08	Registro K100 – Campo 8 – PER_CONS

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Percentual de Consolidação no Final Período.
	MFS-10358		RNK100-09	Registro K100 – Campo 9 – DATA_INI_EMP

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Data Início da Consolidação.
	MFS-10358		RNK100-10	Registro K100 – Campo 10 – DATA_FIN_EMP

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Data Final da Consolidação.
	MFS-10358		RNK110-00	Registro K110 – Regra geral

Origem da Informação: SAFX241 - Relação dos Eventos Societários / Empresas Participantes do Evento.

Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K110 será gerada conforme definida neste documento. Este registro é filho do K100. 

Este registro é filho do K100. Sempre que existir registro nas tabelas indicadas na Origem da Informação vinculada ao registro pai, este registro será gerado. 

Como este registro é de geração facultativa, pode ocorrer do usuário não tê-lo selecionado no Perfil (menu Parâmetros >> Perfil). Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K110 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K110 – Relação dos Eventos Societários”. 

Campo-chave: Nenhum 

Registro pai / Nível hierárquico: K110 / Nível 4

Ocorrência: Vários por arquivo.
	MFS-10358		RNK110-01	Registro K110 – Campo 1 – REG

Informação fixa “K110”.
	MFS-10358		RNK110-02	Registro K110 – Campo 2 – EVENTO

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Evento Societário ocorrido no período.
	MFS-10358		RNK110-03	Registro K110 – Campo 3 – DT_EVENTO

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Data do Evento Societário.
	MFS-10358		RNK115-00	Registro K115 – Regra geral

Origem da Informação: SAFX241 - Relação dos Eventos Societários / Empresas Participantes do Evento.

Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K115 será gerada conforme definida neste documento.

Campo-chave: Nenhum

Registro pai / Nível hierárquico: K115 / Nível 5

Ocorrência: Vários por arquivo.
	MFS-10358		RNK115-01	Registro K115 – Campo 1 – REG

Informação fixa “K115”.
	MFS-10358		RNK115-02	Registro K115 – Campo 2 – EMP_COD_PART

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da Empresa envolvida na operação.
	MFS-10358		RNK115-03	Registro K115 – Campo 3 – COND_PART

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Condição da empresa relacionada à operação.
	MFS-10358		RNK115-04	Registro K115 – Campo 4 – PER_EVT

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Percentual da empresa participante envolvido na operação.
	MFS-10358		RNK200-00	Registro K200 – Regra geral

Origem da Informação: SAFX2002 – Tabela de Plano de Contas

Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K200 será gerada conforme definida neste documento. 

Serão consideradas as contas contábeis utilizadas nas escriturações contábeis consolidadas (campo IND_CONTA_CONSOLID = S da SAFX2002) que possuam movimento (SAFX242) no período de consolidação do K030 (SAFX240).

Para a geração do Plano de Contas Consolidado, as informações serão recuperadas da tela de Plano de Contas (menu: Manutenção >> Códigos >> Plano de Contas) do módulo Mastersaf DW.

Para este cenário, deve ser gerado no arquivo as informações do cadastro das contas sintéticas (campo COD_CONTA_SINT da SAFX2002) associada à conta movimentada encontrada (SAFX242) e também o cadastro de todas as outras contas vinculadas, de nível superior, de forma que tenhamos o plano completo. 
Exemplo:
No movimento (SAFX242) temos a conta: 0001.0001.0001.0001, que no cadastro tem:

Código de Conta
Código de Conta Sintética
Nível

0001.0001.0001.0001
0001.0001.0001
4

0001.0001.0001
0001.0001
3

0001.0001
0001
2

0001

1


Neste exemplo, apenas a conta 0001.0001.0001.0001 foi movimentada, porém, no arquivo gerado devem ser demonstradas informações das contas "0001.0001.0001.0001", "0001.0001.0001", "0001.0001" e "0001".

Como este registro é de geração facultativa, pode ocorrer do usuário não tê-lo selecionado no Perfil (menu Parâmetros >> Perfil). Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K200 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K200 – Plano de Contas Consolidado”.

Campo-chave: COD_CTA

Registro pai / Nível hierárquico: K200 / Nível 2

Ocorrência: Vários por arquivo.
	MFS-10358		RNK200-01	Registro K200 – Campo 1 – REG

Informação fixa “K200”.  
	MFS-10358		RNK200-02	Registro K200 – Campo 2 – COD_NAT

Considerando a Origem da Informação, demonstrar aqui o conteúdo de acordo com campo Indicador de Natureza conforme abaixo:

Indicador de Natureza:

Se informado ‘0. Compensação’, gravar ‘05’;
Se informado ‘1. Ativo’, gravar ‘01’;
Se informado ‘2. Passivo’, gravar ‘02’;
Se informado ‘3. Despesa’, gravar ‘04’;
Se informado ‘4. Receita’, gravar ‘04’;
Se informado ‘5. Mutações Ativas ("Variações Patrimoniais" anuais)’, gravar ‘09’;
Se informado ‘6. Mutações Passivas ("Variações Patrimoniais" anuais)’, gravar ‘09’;                                                                                                                                                                                                           Se informado ‘7. Patrimônio Líquido’, gravar ‘03’;                                                                                                                                                                                      Se informado ‘8. Custo’, gravar ‘04’;
Se informado ‘9. Outros’, gravar ‘09’. 
	MFS-10358		RNK200-03	Registro K200 – Campo 3 – IND_CTA

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador de Conta.
	MFS-10358		RNK200-04	Registro K200 – Campo 4 – NIVEL

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Nível.
	MFS-10358		RNK200-05	Registro K200 – Campo 5 – COD_CTA

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da Conta.
	MFS-10358
		RNK200-06	Registro K200 – Campo 6 – COD_CTA_SUP

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código de Conta Sintética.
	MFS-10358		RNK200-07	Registro K200 – Campo 7 – CTA

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Descrição da Conta.
	MFS-10358		RNK210-00	Registro K210 – Regra geral

Origem da Informação: Manutenção - Mapeamento para Planos de Contas das Empresas Consolidadas

Localizaçao: Menu SPED,  Módulo: ECD - Escrituração Contábil Digital, item de menu Manutenção àð Bloco K àð Mapeamento para Planos de Contas das Empresas Consolidadas

Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro  Escriturações Contábeis Consolidadas  selecionado na tela de Dados Iniciais   menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K210 será gerada conforme definida neste documento. 

Se o campo “Código da Conta Consolidadora” estiver preenchido na tabela “SAFX262 - Mapeamento para Plano de Contas das Empresas Consolidadas”, o sistema deverá gerar o registro K210 com a informação preenchida no campo “Código da Conta da Empresa Participante E a partir deste relacionamento com a conta consolidadora inserida, esta deverá ser incluída como “filha” no registro K200.

Senão, manter a geração atual, considerando a Origem da Informação COD_CTA_EMP.

Se opção “Gerar Plano de Contas” dos Dados Iniciais da ECD (Módulo ECD> Parâmetros>Dados Iniciais) for diferente de “Completo” e o Campo COD_EMPRESA da SAFX262 for igual ao código da empresa do Manager, deverá gerar os Registros I050 para as contas constantes no campo COD_CONTA da SAFX262.

Campo-chave: COD_EMP, COD_CTA_EMP

Registro pai / Nível hierárquico: K210 / Nível 4

Ocorrência: Vários por arquivo.
	MFS-10358
MFS-18238		RNK210-01	Registro K210 – Campo 1 – REG

Informação fixa “K210”.
	MFS-10358		RNK210-02	Registro K210 – Campo 2 – COD_EMP

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código/Nome da Empresa Participante.
	MFS-10358		RNK210-03	Registro K210 – Campo 3 – COD_CTA_EMP

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da Conta.
	MFS-10358		RNK300-00	Registro K300 – Regra geral

Origem da Informação: SAFX242 - Saldos das Contas Consolidadas.

Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K300 será gerada conforme definida neste documento.

Serão considerados apenas os saldos das contas consolidadas que pertençam ao período de consolidação informado no K030 (SAFX240).

Como este registro é de geração facultativa, pode ocorrer do usuário não tê-lo selecionado no Perfil (menu Parâmetros >> Perfil). Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K300 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K300 – Saldos das Contas Consolidadas”. 

Campo-chave: COD_CTA

Registro pai / Nível hierárquico: K300 / Nível 3.

Ocorrência: Vários por arquivo.
	MFS-10358		RNK300-01	Registro K300 – Campo 1 – REG

Informação fixa “K300”.
	MFS-10358		RNK300-02	Registro K300 – Campo 2 – COD_CTA

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da conta consolidada.
	MFS-10358		RNK300-03	Registro K300 – Campo 3 – VAL_AG

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Valor absoluto aglutinado.
	MFS-10358		RNK300-04	Registro K300 – Campo 4 – IND_VAL_AG

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador da situação do valor aglutinado.
	MFS-10358		RNK300-05	Registro K300 – Campo 5 – VAL_EL

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Valor absoluto das eliminações.
	MFS-10358		RNK300-06	Registro K300 – Campo 6 – IND_VAL_EL

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador da situação do valor eliminado.
	MFS-10358		RNK300-07	Registro K300 – Campo 7 – VAL_CS

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Valor absoluto consolidado.
	MFS-10358		RNK300-08	Registro K300 – Campo 8 – IND_VAL_CS 

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador da situação do valor consolidado.
	MFS-10358		RNK310-00	Registro K310 – Regra geral

Origem da Informação: SAFX243 - Empresas Detentoras das Parcelas do Valor Eliminado Total.

Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K310 será gerada conforme definida neste documento.

Este registro é filho do K300. Sempre que existir registro nas tabelas indicadas na Origem da Informação vinculada ao registro pai, este registro será gerado.

Como este registro é de geração facultativa, pode ocorrer do usuário não tê-lo selecionado no Perfil (menu Parâmetros >> Perfil). Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K310 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K310 – Empresas Detentoras das Parcelas do Valor Eliminado Total”.

Campo-chave: EMP_COD_PARTE 

Registro pai / Nível hierárquico: K310 / Nível 4.

Ocorrência: Vários por arquivo.

	MFS-10358		RNK310-01	Registro K310 – Campo 1 – REG

Informação fixa “K310”.
	MFS-10358		RNK310-02	Registro K310 – Campo 2 – EMP_COD_PARTE

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da empresa detentora do valor aglutinado que foi eliminado.
	MFS-10358		RNK310-03	Registro K310 – Campo 3 – VALOR

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Parcela do valor eliminado total.
	MFS-10358		RNK310-04	Registro K310 – Campo 4 – IND_VALOR

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador da situação do valor eliminado.
	MFS-10358		RNK315-00	Registro K315 – Regra geral

Origem da Informação: SAFX244 - Empresas Contrapartes das Parcelas do Valor Eliminado Total.

Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K315 será gerada conforme definida neste documento.

Como este registro é de geração facultativa, pode ocorrer do usuário não tê-lo selecionado no Perfil (menu Parâmetros >> Perfil). Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K315 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K315 – Empresas Contrapartes das Parcelas do Valor Eliminado Total”. 

Campo-chave: EMP_COD_CONTRA, COD_CONTRA

Registro pai / Nível hierárquico: K315 / Nível 5.

Ocorrência: Vários por arquivo.

	MFS-10358		RNK315-01	Registro K315 – Campo 1 – REG

Informação fixa “K315”.
	MFS-10358		RNK315-02	Registro K315 – Campo 2 – EMP_COD_CONTRA

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da empresa da contrapartida.
	MFS-10358		RNK315-03	Registro K315 – Campo 3 – COD_CONTRA

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da conta consolidada da contrapartida. 
	MFS-10358		RNK315-04	Registro K315 – Campo 4 – VALOR

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Parcela da contrapartida do valor eliminado total.
	MFS-10358		RNK315-05	Registro K315 – Campo 5 – IND_VALOR

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador da situação do valor eliminado.
	MFS-10358		RNK990	Registro K990 – Encerramento do Bloco K

A princípio não atenderemos a geração do Bloco K - Conglomerados Econômicos (Facultativo para o ano-calendário 2016), porém deverão ser gerados pelo menos os registros de Abertura e Encerramento do Bloco K.

Registro encerramento: K990 	MFS8216
MFS-10358		RNK990-01	Registro K990 – Campo 1 – REG

Informação fixa “K990”. 
	MFS9809		RNK990-02	Registro K990 – Campo 2 –QTD_LIN_K 

Será preenchido com o t