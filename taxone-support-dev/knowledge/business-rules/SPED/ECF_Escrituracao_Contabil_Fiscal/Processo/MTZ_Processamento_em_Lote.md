# MTZ_Processamento_em_Lote

- **Fonte:** MTZ_Processamento_em_Lote.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 185 KB

---

			

THOMSON REUTERS

Processamento em Lote

__ECF \- Escrituração Contábil Fiscal \(DW\)__

##### DOCUMENTO DE REQUISITO

__Data__

__MFS__

__Descrição__

__Autor__

29/08/2017

MFS\-13202

Criação do documento

Alessandra Cristina Navatta

08/09/2017

MFS\-12636

Geração da apuração A00 \(RNI09\)

Validações \(RNI03\.01\)

Processamento do Bloco K \(rateio das contas\) \(RNI07\)

Recuperar Saldo Inicial das contas de rateio \(RNI08\)

Manter Ajustes Manuais \(RNI10, RNI10\.01 e RNI10\.2\)

Alessandra Cristina Navatta

19/09/2017

MFS\-12620

Inclusão das Regras de Cálculo

Alessandra Cristina Navatta

25/09/2017

MFS\-12620

Inclusão de Regras do Lançamento de Encerramento

Alessandra Cristina Navatta

25/10/2017

MFS\-13995

Inclusão de Regras dos Registros L100 e L300

Alessandra Cristina Navatta

27/10/2017

MFS\-13997

Inclusão de Regras do Registro L210

Alessandra Cristina Navatta

27/10/2017

MFS\-13999\-B

Rateio de Atividade Mista

Alessandra Cristina Navatta

31/10/2017

MFS\-13997

Processamento dos Blocos M e N

Alessandra Cristina Navatta

13/11/2017

MFS\-14668

Inclusão de validação das linhas do tipo NS do registro L210 \(DW00131\)\.

Alessandra Cristina Navatta

21/11/2017

MFS\-14779

Inclusão de regras para o bloco M considerando a Recuperação de Valores e Fixar Saldo Inicial nas linhas de reversão de saldos

Alessandra Cristina Navatta

01/12/2017

MFS\-15014

Regras do Manter Ajustes \(Lançamentos da Parte A \(M300, M350\)

Alessandra Cristina Navatta

18/01/2018

MFS\-15678

Criação e recalculo dos lançamentos de origem de contrapartida, dos registros M410 com o campo ‘Ajuste com Origem na Parte B’ = Incremental, na apuração anterior e recalculo do registro M500 \(RNC08, RNC09 e RNC10\)\.

Alessandra Cristina Navatta

22/01/2018

MFS\-15958

Revisão / criação das regras de manter ajustes manuais \(RNI10\.03\)\.

Alessandra Cristina Navatta

01/02/2018

MFS\-12632

Inserção das Regras básicas do Bloco N: 

- Importação: \(RNI03\.01, RNI04, RNI04\.03, RNI09, RNI10\)
- Processamento dos Registros: \(RNP01, RNP09, RNP10, RNP11, RNP12, RNP13, RNP14, RNP15, RNP16\)

Alessandra Cristina Navatta

07/02/2018

MFS\-16531

Inclusão das Regras do bloco N:

- Cálculo: \(RNC02, RNC05, RNC11\)

Alessandra Cristina Navatta

01/03/2018

MFS\-16928

Inclusão das Regras do bloco N \(comparativo\)

- Importação: RNI03\.01 e RNI04\.03
- Cálculo: RNC02 e RNC12 
- Processamento: RNP12 e RNP15

Alessandra Cristina Navatta

12/03/2018

MFS\-17089

Processamento dos registros M310 e M360

Alessandra Cristina Navatta

13/03/2018

MFS\-12623

Incentivo Fiscal

- Importação: RNI10
- Cálculo: RNC13
- Processamento: RNP19

Alessandra Cristina Navatta

28/03/2018

MFS\- [17491](http://ent.jira.int.thomsonreuters.com/browse/MFS-17491)

Inclusão das Regras de Compensação de Prejuízos e Base Negativa \(RNC15, RNC16 e RNC17\)

Alessandra Cristina Navatta

02/04/2018

MFS\-17657

Inclusão de Validação nos registros M310 e M360 \(RNI03\.01\)

Inclusão da RNI04\.08, Percentual Receita Bruta \(Registros N500, N650\)

Alessandra Cristina Navatta

20/04/2018

MFS\-17913

Inclusão das regras para cálculo do PAT \(Programa de Alimentação do Trabalhador\) – RNC18, RNC19 e RNC20\.

Alessandra Cristina Navatta

25/04/2018

MFS\-18089

Validação do Plano Referencial e Tabela Dinâmica \(RNI03\.01\)

Alessandra Cristina Navatta

03/07/2018

MFS\-19471

Inclusão de [Validação no Processamento sobre existência de parametrização de 'Recuperação de Valores \- Apuração IRPJ/CSLL'](http://ent.jira.int.thomsonreuters.com/browse/MFS-19471) \(RNI03\.01\)

Alessandra Cristina Navatta

Sumário

[INTRODUÇÃO	6](#_Toc512254964)

[AGRUPAMENTO DE REGRAS DE NEGÓCIO	6](#_Toc512254965)

[DOCUMENTOS DE REFERÊNCIA	6](#_Toc512254966)

[1\.	REGRAS – IMPORTAÇÃO DE SALDOS	7](#_Toc512254967)

[2\.	REGRAS CÓPIA DE AJUSTES MANUAIS	56](#_Toc512254968)

[3\.	REGRAS – CÁLCULO	58](#_Toc512254969)

[4\.	REGRAS – PROCESSAMENTO DOS REGISTROS	82](#_Toc512254970)

[3\.1 Regra Geral \- Processamento dos Blocos K, N, L, M	83](#_Toc512254971)

[3\.2 Registro L100: Balanço Patrimonial	83](#_Toc512254972)

[3\.3	Registro L300: Demonstração do Resultado do Lucro Líquido Fiscal	84](#_Toc512254973)

[3\.4	Registro K155: Detalhes dos Saldos Contábeis \(Depois do Encerramento do Resultado do Período\)	84](#_Toc512254974)

[3\.5	Registro K156: Mapeamento Referencial do Saldo Final	85](#_Toc512254975)

[3\.6	Registro K355: Saldos Finais das Contas Contábeis de Resultado Antes do Encerramento	85](#_Toc512254976)

[3\.7 Registro K356: Mapeamento Referencial dos Saldos Finais das Contas Contábeis de Resultado Antes do Encerramento	86](#_Toc512254977)

[3\.8	Registro L210: Informativo de Composição de Custos	86](#_Toc512254978)

[3\.9	Registro N500: Base de Cálculo do IRPJ Sobre o Lucro Real Após as Compensações de Prejuízos	86](#_Toc512254979)

[3\.10	Registro N600: Demonstração do Lucro da Exploração	87](#_Toc512254980)

[3\.11	Registro N610: Cálculo da Isenção e Redução do Imposto Sobre o Lucro Real	87](#_Toc512254981)

[3\.12	Registro N620: Cálculo do IRPJ Mensal por Estimativa	88](#_Toc512254982)

[3\.13	Registro N630: Cálculo do IRPJ Com Base no Lucro Real	88](#_Toc512254983)

[3\.14	Registro N650: Base de Cálculo da CSLL Após as Compensações da Base de Cálculo Negativa	89](#_Toc512254984)

[3\.15	Registro N660: Cálculo da CSLL Mensal por Estimativa	90](#_Toc512254985)

[3\.16	Registro N670: Calculo da CSLL Com Base no Lucro Real	90](#_Toc512254986)

[3\.17	Registro M300: Lançamentos da Parte A do e\-Lalur	91](#_Toc512254987)

[3\.18	Registro M350: Lançamentos da Parte A do e\-Lacs	92](#_Toc512254988)

[3\.19	Registro N615: Informações da Base de Cálculo de Incentivos Fiscais	93](#_Toc512254989)

[3\.20	Registro M310: Contas Contábeis Relacionadas ao Lançamento da Parte A do e\-Lalur	94](#_Toc512254990)

[3\.21	Registro M360: Contas Contábeis Relacionadas ao Lançamento da Parte A do e\-Lacs	94](#_Toc512254991)

<a id="_Toc361822343"></a>

# <a id="_Toc503179326"></a><a id="_Toc512254964"></a><a id="_Toc370303430"></a><a id="_Toc370915114"></a>INTRODUÇÃO

O processamento tem como objetivo a transcrição dos valores dos dados de origem para os referenciais do fisco, de acordo com as associações parametrizadas, a manutenção de ajustes manuais efetuados no sistema e o cálculo das formulas dos registros referentes a tabelas dinâmicas\.

O Processo é iniciado a partir do acionamento do Botão “Processar” da Tela “Processamento em Lote” e são recebidos os seguintes parâmetros:

- Transcrição dos Valores Empresa para Referenciais Fisco as regras iniciam na [RNI01\.](#RNI01)
- Cálculo dos Registros e Fórmulas  [RNC01](#RNC01)\.

# <a id="_Toc503179327"></a><a id="_Toc512254965"></a>AGRUPAMENTO DE REGRAS DE NEGÓCIO

- RNI – Regras de Importação de Saldos
- RNA – Regras de Associação de Lançamentos 
- RNCP – Regras Cópia de Ajustes Manuais
- RNC – Regras de Cálculo
- RNP – Regras de Processamento

# <a id="_Toc503179328"></a><a id="_Toc512254966"></a>DOCUMENTOS DE REFERÊNCIA

*Lista de documentos relacionados ao processamento\.*

- Tela Processamento em Lote\.doc
- Mensagens\_Sistema\_DWECF\.xlsx
- Regras\_Gerais\_DWECF\.doc

# <a id="_Toc512254967"></a><a id="regrasimportacao"></a>REGRAS – IMPORTAÇÃO DE SALDOS

__Considerações gerais:__

O saldo a ser considerado no ECF \- Escrituração Contábil Fiscal, deve ter passado pela rotina de ‘Recomposição de Saldos Contábeis‘ \(documento MTZ\_ARQ\_MOV0002\.docx\)\.

__CÓD__

###### __DESCRIÇÃO__

__MFS__

<a id="RNI01"></a>RNI01

Criar um processo para a importação dos saldos para que os saldos das contas e centro de custo que serão utilizados na apuração dos tributos e geração do arquivo sejam identificados conforme critérios abaixo:

O sistema deve executar o processo de importação de saldos seguindo as regras abaixo: 

Com base na parametrização da tela “Processamento em Lote”, o processamento deverá ocorrer para todas as empresas selecionadas\.

Quando houver mais de uma empresa selecionada para a execução ao término da importação de uma empresa o sistema automaticamente começa a importação da próxima empresa da lista da lista, finalizando quando efetuado a importação de todos os estabelecimentos\.

Ao término das rotinas executas na tela, o sistema exibirá o status do processo e mensagens de erros ou avisos estarão disponíveis na aba de processos, existente na própria tela de Processamento em Lote\.

MFS\-13202

RNI02

Etapas do Processo:

- [Zerar Linhas da Tabela Dinâmica e das Contas Referenciais](#ZerarLinhaseContas)
- [Validações](#Validações)
-  [Recuperar uma Associação Plano Referencial](#AssociacaoTabReferencial) 
	- [Atribuir Saldo na Conta Referencial](#Atribuindo_saldo_conta_referencial) 
	- Calcular Percentual da Atividade Mista
	- [Pré – Processamento do bloco K \(Rateio e Lançamento de Encerramento\)](#Processamento_BlocoK) 
	- Valor da Conta Referencial [RNI05\.01 – Recuperação Acumulada dos Saldos](#AtribuiçãodosSaldosApurAnual)  e  RNG00031 \- Recuperação de Saldos
- [Recuperar uma Associação Tabela Dinâmica](#RecuperaçãoSaldosTabelaDinâmica) 
	- [Atribuir Saldo na Linha da Tabela Dinâmica](#AtribuicSaldosTabelaDinâmicaApurAnuTrim) 
		- [Atribuição Saldo na Linha da Tabela Dinâmica com base no Tipo de Receita](#AtribuicSaldosTabelaDinâmicaTipodeReceit)
			- [Atribuição de Saldos para Linhas Específicas do Registro L210](#AtribuicSaldosLinhaL210)

MFS\-13202

MFS\-13995

MFS\-13997

RNI03

<a id="ZerarLinhaseContas"></a>__[Zerar](#Recuperando_Associação) Linhas da Tabela Dinâmica e das Contas Referenciais:__

Com base na Apuração selecionada na tela de Processamento em Lote, verificar as informações dos campos versão e qualificação da pessoa jurídica, \(Tela Informações ECF\), para identificar qual o plano referencial e registros da tabela dinâmica está compatível com essa escrituração \(conforme RNG00003 e RNG00005\)\.

Zerar todas as linhas da tabela dinâmica \(exceto as linhas do tipo ‘R’\) e as contas do plano referencial que foram recuperadas\.  As linhas do tipo ‘R’ devem ficar nulas \(sem informação\)\.

MFS\-13202

RNI03\.01

<a id="Validações"></a>Validações:

- A mensagem DW00015 deve ser exibida quando de acordo com a parametrização efetuada na tela de “Processamentos em Lote” não houver informações na tabela de saldos para o período a ser processado\.
- __Verificar na apuração anterior:  __RNG00049 \- Sem escolha do tipo de receita\.
- Se encontrar uma associação vinculada na tela de Informações ECF e Forma de Tributação igual a ‘Lucro Real, Lucro Presumido, Lucro Arbitrado’, verificar se está parametrizado nas associações algum registro por quebra \(finalizados por A,B ou C\), se existir, verificar se há pelo menos uma compatível com o campo Qualificação da Pessoa Jurídica \(conforme RNG00005 \- Associações compatíveis com o campo ‘Qualificação da Pessoa Jurídica’ da tela Informação ECF\), caso contrário exibir a mensagem DW00017 \(para associação do plano referencial com o plano empresa, verificar os registros L100A, L100B, L100C,L300A, L300B, L300C,P100, P100B, P150 e P150B\) e DW00119 \(para associação da tabela dinâmica com o plano empresa, verificar os registrosM300A, M300B, M300C, M350A, M350B, M350C, N630A, N630B, N630C\)\. Se além da associação compatível com o campo ‘Qualificação da Pessoa Jurídica’ da tela Informação ECF, se existir uma associação incompatível, exibir a mensagem DW00003 \(para associação do plano referencial com o plano empresa\) e DW00016 \(para associação da tabela dinâmica com o plano empresa\)\.
- Caso não seja encontrada nenhuma associação da tabela referencial com o plano empresa, aplicar a RNG00006 \- Validação Campo Escrituração\.
- Deve ser exibida a mensagem de aviso DW00267 ao usuário se existir uma parametrização na tela Recuperação de Valores \- Apuração IRPJ/CSLL válida \(para a empresa e período que está sendo processado\) e nenhuma parametrização for encontrada na tela de Informações ECF\. 
- __Para as escriturações a partir da versão 3\.00__:

Verificar se a conta contábil e o centro de custo \(este último, quando existir\), gerados a partir dos mapeamentos para os registros M300 e ou M350, estão também no mapeamento dos registros L100 ou L330\. Caso não seja encontrado, exibir a mensagem DW00193\.

__Outras Validações com relação á Versão do layout da obrigação que não são validadas na tela de Informações ECF:__

- Se a versão não for compatível com a data da ECF \(período de vigência\), exibir a DW00018

Exemplo: Data Inicial 01/01/2014 \(independente se houver situação especial ou não\) com versão 2\.00

- Se a versão for compatível com a data da ECF \(período de vigência\), mas a versão não for compatível com a ocorrência de situação especial, exibir a DW00019\.

Exemplo: Data Inicial 01/01/2015 \(com situação especial\) com versão 2\.00

Se a versão for compatível com a data da ECF \(período de vigência\), mas a versão não é compatível sem a ocorrência de situação especial, exibir a DW00020\.  
Exemplo: Data Inicial 01/01/2015 \(sem situação especial\) com versão 1\.00\.

MFS\-13202

MFS\-12636

MFS\-13995

MFS\-12632

MFS\-16928

MFS\-17657

MFS\-18089

MFS\-19471

RNI04

<a id="RecuperaçãoSaldosTabelaDinâmica"></a>__Recuperação dos saldos para associações com a Tabela Dinâmica__

- Deverá ser respeitada a hierarquia entre os registros e os códigos dos registros, pois pode haver dependência entre as linhas de um mesmo registro\. Tal hierarquia pode ser identificada com base na planilha Compara Dinamicas\.xls pelas colunas “Registro”, “Ordem”, “Linha do ECF” e “Fórmula”\.
- Saldo a ser atribuído ao código do registro deve ser correspondente ao saldo das contas contábeis associadas\. 
- Deverá ser respeitado o agrupamento dos saldos de acordo com o registro conforme coluna “Registro”\. Para os registros N630, M300 e M350 verificar os critérios abaixo:
- Se na tela Informações ECF campo Qualificação da Pessoa Jurídica = “PJ em Geral”, considerar apenas as linhas da tabela dinâmica cujo coluna Registro = N630A, M300A e M350A
- Se na tela Informações ECF campo Qualificação da Pessoa Jurídica = “PJ Componente do Sistema Financeiro”, considerar apenas as linhas da tabela dinâmica cujo campo registro = N630B, M300B e M350B\.
- Se na tela Informações ECF campo Qualificação da Pessoa Jurídica = “Sociedades Seguradoras, de Capitalização ou Entidade Aberta de Previdência Complementar”, considerar apenas as linhas da tabela dinâmica cujo campo registro = N630C, M300C e M350C\.
- Para a atribuição dos saldos, deverá ser respeitada a sequência contida na coluna “Linha do ECF”\.
- Quando o resultado do saldo que será atribuído à linha da tabela dinâmica corresponder ao indicador “D”, ou seja, saldo devedor, para as linhas da tabela dinâmica que possuírem o Tipo = NS, o saldo a ser atribuído à linha receberá o SINAL NEGATIVO\. Se for indicador “C”, ou seja, saldo credor, o saldo a ser atribuído à linha não receberá o SINAL NEGATIVO\. 
- As contas contábeis que possuem associações com linhas do Bloco M, o campo referente a Status deverá ser preenchido com o status “Considerar Movimento”\.

MFS\-13997

MFS\-12632

RNI04\.01

<a id="AtribuicSaldosTabelaDinâmicaApurAnuTrim"></a>__Atribuição dos saldos para Apuração = Anual ou Trimestral \(Tabela Dinâmica\)__

__Apuração Anual:__

Para tais tipos de apuração, os saldos devem atribuídos à linha de forma acumulada considerando a parametrização realizada na tela de Associação da Tabela Dinâmica com o Plano Empresa\.  O conceito de forma acumulada consiste em recuperar os valores de forma acumulada até o período que está sendo processado conforme RNG00033 – Recuperação Acumulada dos Saldos\.

Os saldos devem ser recuperados de acordo com a parametrização citada na RNG00031 – Recuperação de Saldos\.

MFS\-13997

RNI04\.02

<a id="AtribuicSaldosLinhaL210"></a>__Atribuição dos Saldos linhas específicas do Registro L210__

O valor atribuído para as linhas diferentes de 2, 3, 4, 33, 39, 71, 72 e 73 deve ser o valor do saldo final, conforme informado na RNI04\.01\.

O valor atribuído para as linhas 2, 33, 39, 71, 72 e 73 deve ser o valor do saldo inicial, conforme regras abaixo:

__Apuração = Anual ou Trimestral__

Recuperar o Saldo Inicial na tabela de Saldos Contábeis do primeiro mês \(Anual\) ou primeiro mês do trimestre \(Trimestral\) para cada linha da tabela dinâmica que possua associação com conta contábil e centro de custo tela Associação da Tabela Dinâmica com Plano Empresa, buscar na tabela de saldos os valores que serão atribuídos as linhas com base na parametrização realizada na tela Processamento em Lote utilizando como parâmetro de busca o Exercício e as Aberturas das Apurações selecionadas para o processamento\.

Para a atribuição do saldo para a linha da tabela dinâmica quando há mais de uma conta contábil associada na apuração anual ou trimestral, verificar RNG00035 – Soma dos Saldos\.

Se primeiro mês do período de apuração não tiver saldo informado ou o saldo inicial for zerado, considerar o valor zerado para o lançamento na tabela dinâmica\.

__O valor atribuído para as linhas 3, 4 depende da parametrização Fixar Movimento do Mês para as linhas 3 e 4 do Registro L210:__

Verificar se o parâmetro “Fixar Movimento do Mês para as linhas 3 e 4 do Registro L210” da tela Abertura de Apuração está preenchido para o Período de Apuração correspondente, Em caso positivo:

Recuperar da tabela de Saldos Contábeis o movimento de débito e crédito de todos os Saldos Contábeis, informados ou zerados, \(acumulados até o mês\) ou do trimestre considerando a parametrização realizada na tela Processamento em Lote utilizando como parâmetro de busca o Exercício e as Aberturas das Apurações selecionadas para o processamento\.

Ao final do processamento, exibir a mensagem DW00111\.

Se existir ajuste manual nas linhas 3 ou 4 de algum período anterior que está sendo processado e o parâmetro, “Fixar Movimento do Mês para as linhas 3 e 4 do Registro L210” está marcado na tela abertura de apuração, exibir a mensagem DW00112\.

Se o parâmetro “Fixar Movimento do Mês para as linhas 3 e 4 do Registro L210” da tela de Abertura da Apuração está sem preenchimento para o Período de Apuração correspondente, deve ser considerado o valor do saldo final, conforme informado na RNI04\.01\.

__Linhas com sinal negativo \(Formato NS\)__

As linhas que possuem formato “NS” poderão receber sinal de negativo\. A tabela abaixo deve ser considerada para saber se o valor será negativo ou positivo, de acordo com as naturezas:

__Registro L210__

__Natureza da Conta Contábil__

__Crédito__

__Débito__

Patrimonial \- \(Ativo, passivo, Patrimônio Líquido, 0 \- Compensação, 5 \- Mutações Ativas \(“Variações Patrimoniais” anuais\), 6 \- Mutações Passivas \(“Variações Patrimoniais” anuais\) e Outros\)

Positivo

Negativo

Resultado \(Despesa, Receita e Custo\)

Negativo

Positivo

Para as linhas de formato NS e que estão com valor negativo, exibir a mensagem DW00131\.

__Validações Para Apuração Anual:__

A partir da segunda abertura de apuração, verificar se o parâmetro ‘Fixar saldo inicial na linha do M300’, da tela de Abertura da Apuração, está com a mesma informação que a abertura anterior, caso a parametrização seja diferente, exibir a mensagem DW00116\.

A partir da segunda abertura de apuração, verificar se o parâmetro ‘Fixar saldo inicial na linha do M350’, da tela de Abertura da Apuração, está com a mesma informação que a abertura anterior, caso a parametrização seja diferente, exibir a mensagem DW00117\.

A partir da segunda abertura de apuração, verificar se o parâmetro ‘Fixar Movimento do Mês para as Linhas 3 e 4 do Registro L210’, da tela de Abertura da Apuração, está com a mesma informação que a abertura anterior, caso a parametrização seja diferente, exibir a mensagem DW00118\.

MFS\-13997

MFS\-14668

RNI04\.03

__Bloco N \- Geração dos Registros com base no Tipo de Receita__

- Os registros gerados na visão balanço, independentemente do parâmetro Tipo de Receita: Todos os registros dos blocos K, L, M e registros N600, N610, N615, N630, N670\. 
- Registros N500, N650 \(linha1\) são gerados na visão balanço, independente do parâmetro Tipo de Receita\.
- Registros N500, N650 \(linha 2\) são gerados na visão Receita Bruta, apenas se o parâmetro Tipo de Receita = “Receita Bruta” ou “Comparativo”\.
- Registros N620, N660: 
	- Se Tipo de Receita = Balanço, então gerar os registros na visão Balanço\.
	- Se Tipo de Receita = Receita Bruta, então gerar os registros na visão Receita Bruta\.
	- Se Tipo de Receita = “Comparativo”, então gerar os registros nas duas visões: visão Receita Bruta e Balanço\.
	- Aplicar RNG00048 – Registros N620 e N660

__Atribuição dos saldos para Apuração = Anual ou Trimestral para Tipos de Receita = Receita Bruta ou Balanço Suspensão ou Redução ou Comparativo__

Quando for identificada associação efetuada na tela Tabelas Dinâmicas com Plano Empresa para os Registros N620, N660 e parametrização do tipo de receita igual = Comparativo \(na Tela de Abertura da Apuração\), as linhas serão geradas nas duas visões: Receita Bruta e Balanço Suspensão ou Redução partindo do princípio de que a escolha por um dos tipos de receita será realizada após o cálculo em uma tela específica \(tela de Comparativo\)\. 

A visão Receita Bruta será gerada quando o Tipo de receita for Receita Bruta ou Comparativo, para identificar o valor a ser atribuído à linhas, será necessário recuperar o movimento do período\. O movimento corresponde ao total de débito e crédito do mês ou do trimestre cujos valores deverão ser recuperados atendendo a regra RNG00031\- Recuperação de Saldos\. 

Para entendimento da recuperação com base no movimento verificar a RNG00032\- Recuperação do Movimento do Saldo

A visão Balanço Suspensão ou Redução será gerada quando o Tipo de Receita for igual a “Balanço Suspensão ou Redução” ou “Comparativo”\. Neste cenário, a regra de recuperação dos saldos é a conforme [ RNG00033 – Recuperação Acumulada dos Saldos\.](#_RG-P07_–_Recuperação)

MFS\-12632

MFS\-16928

RNI04\.04

__Atribuição dos saldos para apuração para as linhas dos registros M300A, M300B, M300C e/ou M350A, M350B, M350C__

Objetivo: Se aplica somente às linhas correspondentes aos registros do Bloco M\. Consiste na parametrização de contas contábeis cujo valor a ser utilizado na apuração poderá ser composto pelo Saldo Contábil, Movimentação \(Total de Débito ou Total de Crédito\) ou Lançamentos Contábeis\.

Para cada conta contábil parametrizada na Tela Recuperação dos Valores \- Apuração IRPJ/CSLL que possua associação com linhas da tabela dinâmica que possua parametrização no campo __Lançamento de Adição e Exclusão __igual a:

01 \- “Um Lançamento \(Consolidando o Movimento de todas as Contas\)” ou 

02 \- “Dois Lançamentos \(Movimento de Contas a Crédito na Adição e Movimento de Contas a Débito na Exclusão\)” ou 

05 \- “Dois Lançamentos \(Total de Crédito de todas as Contas na Adição e Total de Débito de todas as Contas na Exclusão\)” ou 

06 \- “Um Lançamento \(Consolidando o Saldo de todas as Contas\)” ou 

07 \- “Dois Lançamentos \(Saldo de Contas a Débito na Adição e Saldo de Contas a Crédito na Exclusão\)” ou 

08 \- “Dois Lançamentos \(Total de Débito de todas as Contas na Adição e Total de Crédito de todas as Contas na Exclusão\)”:

 

Deve ser verificado em cada registro \(M300A, M300B, M300C, M350A, M350B ou M350C\):

- Se o lançamento na tabela dinâmica é um de Adição \(Tipo Lançamento = “A”\), verificar se a conta do “Plano Empresa” correspondente está associada a outro lançamento de Exclusão \(Tipo Lançamento = “E”\) na tabela dinâmica, caso contrário, exibir a mensagem DW00134\.
- Se o lançamento na tabela dinâmica é um de Exclusão \(Tipo Lançamento = “E”\), verificar se a conta do Plano Empresa correspondente está associada a outro lançamento de Adição \(Tipo Lançamento = “A”\), caso contrário, exibir a mensagem DW00134\.
- Se o lançamento na tabela dinâmica é diferente de Exclusão \(Tipo Lançamento = “E”\) e diferente de Adição \(Tipo Lançamento = “A”\), exibir a mensagem DW00134\.
- Verificar se a conta do Plano Empresa correspondente está associada a dois ou mais __outros__ lançamentos de Adição ou Exclusão, se positivo, exibir a mensagem DW00135\.
- Verificar se o lançamento na tabela dinâmica possui outras contas vinculadas com Lançamento de Adição e Exclusão preenchido e diferente de \(“Não se Aplica” , “Associar Lançamentos Contábeis \(Lançamentos a Crédito na Exclusão e Lançamentos a Débito na Adição\)” e “Associar Lançamentos Contábeis \(Um Lançamento Consolidando todos os Lançamentos Contábeis\)” e “Associar Lançamentos Contábeis \(Lançamentos a Crédito na Adição e Lançamentos a Débito na Exclusão\)”  e se estas possuem a parametrização de Lançamento de Adição e Exclusão iguais ou equivalentes entre as naturezas \(conforme tabela abaixo\) para as contas associadas, caso contrário, exibir  a mensagem DW00136\.

Tabela de Lançamento de Adição e Exclusão equivalentes entre as Naturezas:

__Natureza Patrimonial__

__Natureza de Resultado__

01 \- Um Lançamento \(Consolidando o Movimento de todas as Contas\)

NÃO equivalente a

06 \- Um Lançamento \(Consolidando o Saldo de todas as Contas\)

02 \- Dois Lançamentos \(Movimento de Contas a Crédito na Adição e Movimento de Contas a Débito na Exclusão\)

equivalente a

07 \- Dois Lançamentos \(Saldo de Contas a Débito na Adição e Saldo de Contas a Crédito na Exclusão\)

05 \- Dois Lançamentos \(Total de Crédito de todas as Contas na Adição e Total de Débito de todas as Contas na Exclusão\)

equivalente a

08 \- Dois Lançamentos \(Total de Débito de todas as Contas na Adição e Total de Crédito de todas as Contas na Exclusão\)

 <a id="regrasaplicacaolancamentosdeAE"></a>__Regra de totalização de valores de aplicação dos Lançamentos de A/E__

1. <a id="UmLançamentoConsolidandooMovTodasContas"></a>Se Lançamento de Adição e Exclusão = 01 \-  “__Um Lançamento \(Consolidando o Movimento de todas as Contas\)__” recuperar o movimento de todas as contas associadas ao lançamento e calcular o total do movimento \(acumulado até o mês\) ou do trimestre:

- Se o total do movimento acumulado das contas associadas possuir indicador de __Crédito__: Efetuar o lançamento no registro de __Adição__ da tabela dinâmica\. Criar na Grid de Contas Contábeis da Tela de Lançamentos da Parte A um registro para cada conta associada à __Adição __com seu valor para Movimento\. Criar na Grid de Contas Contábeis da Tela de Lançamentos da Parte A um registro para cada conta associada à __Exclusão__ com seu valor zerado e indicador a __Débito\.__
- Se o total do movimento acumulado das contas associadas possuir indicador de __Débito__: Efetuar o lançamento no registro de __Exclusão__ da tabela dinâmica\. Criar na Grid de Contas Contábeis da Tela de Lançamentos da Parte A um registro para cada conta associada à Exclusão com seu valor para Movimento\. Criar na Grid de Contas Contábeis da Tela de Lançamentos da Parte A um registro para cada conta associada à __Adição __com seu valor zerado e indicador a __Débito__\.
- Cada conta é tratada separadamente\. Considerar o movimento da conta do período que está sendo processado e somar ao valor calculado para o mês anterior\.

1. Se Lançamento de Adição e Exclusão = 06 \- “Um Lançamento \(Consolidando o Saldo de todas as Contas\)” recuperar o movimento de todas as contas associadas ao lançamento:

- Se o total do saldo das contas associadas possuir indicador de __Débito__: Efetuar o lançamento no registro __de Adição__ da tabela dinâmica\. Criar na Grid de Contas Contábeis da Tela de Lançamentos da Parte A um registro para cada conta associada à __Adição __com seu valor de Saldo\. Criar na Grid de Contas Contábeis da Tela de Lançamentos da Parte A um registro para cada conta associada à __Exclusão __com seu valor zerado e indicador a __Débito\.__
- Se o total do saldo das contas associadas possuir indicador de __Crédito__: Efetuar o lançamento no registro de __Exclusão __da tabela dinâmica\. Criar na Grid de Contas Contábeis da Tela de Lançamentos da Parte A um registro para cada conta associada à __Exclusão __com seu valor de Saldo\. Criar na Grid de Contas Contábeis da Tela de Lançamentos da Parte A um registro para cada conta associada à __Adição__ com seu valor zerado e indicador a __Débito\.__

1. Se Lançamento de Adição e Exclusão = 02 \- “Dois Lançamentos \(Movimento de Contas a Crédito na Adição e Movimento de Contas a Débito na Exclusão\)”: 

- Recuperar as contas associadas ao lançamento com indicador de__ Crédito__ para o movimento, calcular o total do movimento \(acumulado até o mês\) ou do trimestre e lançar no registro de __Adição __da tabela dinâmica\. Criar na Grid de Contas Contábeis da Tela de Lançamentos da Parte A um registro para cada conta associada à __Adição__ com seu valor de Movimento para as Contas de__ Crédito__ e o valor zerado e indicador a __Débito__ para as Contas de Débito\.
- Recuperar as contas associadas ao lançamento com indicador de __Débito __para o movimento, calcular o total do movimento \(acumulado até o mês\) ou do trimestre e lançar no registro de __Exclusão__ da tabela dinâmica\. Criar na Grid de Contas Contábeis da Tela de Lançamentos da Parte A um registro para cada conta associada à __Exclusão__ com seu valor de Movimento para as Contas de __Débito __e o valor zerado e indicador a __Débito __para as Contas de Crédito\.
- Cada conta é tratada separadamente\. Considerar o movimento da conta do período que está sendo processado e somar ao valor calculado para o mês anterior\.

1. Se Lançamento de Adição e Exclusão = 07 \- “Dois Lançamentos \(Saldo de Contas a Débito na Adição e Saldo de Contas a Crédito na Exclusão\)”: 

- Recuperar as contas associadas ao lançamento com indicador de__ Débito__ para o saldo, e lançar o saldo no registro de __Adição __da tabela dinâmica\. Criar na Grid de Contas Contábeis da Tela de Lançamentos da Parte A um registro para cada conta associada à __Adição __com seu valor de Saldo para as Contas de __Débito __e o valor zerado e indicador a __Crédito__ para as Contas de Crédito\.
- Recuperar as contas associadas ao lançamento com indicador de __Crédito__ para o saldo, e lançar o saldo no registro de __Exclusão__ da tabela dinâmica\. Criar na Grid de Contas Contábeis da Tela de Lançamentos da Parte A um registro para cada conta associada à __Exclusão__ com seu valor de Saldo para as Contas de __Crédito__ e o valor zerado e indicador a __Débito__ para as Contas de Débito\.

1. Se Lançamento de Adição e Exclusão = 05 \- “Dois Lançamentos \(Total de Crédito de todas as Contas na Adição e Total de Débito de todas as Contas na Exclusão\)”: 

- Recuperar o movimento de __Crédito __das contas associadas ao lançamento, calcular o total do movimento de crédito \(acumulado até o mês\) ou do trimestre e lançar no registro de__ Adição__ da tabela dinâmica\. Criar na Grid de Contas Contábeis da Tela de Lançamentos da Parte A um registro para cada conta associada à__ Adição__ com seu valor de Movimento de __Crédito\.__
- Recuperar o movimento de __Débito __das contas associadas ao lançamento, calcular o total do movimento de débito \(acumulado até o mês\) ou do trimestre e lançar no registro de __Exclusão__ da tabela dinâmica\. Criar na Grid de Contas Contábeis da Tela de Lançamentos da Parte A um registro para cada conta associada à __Exclusão __com seu valor de Movimento de __Débito\.__

1. Se Lançamento de Adição e Exclusão = 08 \- “Dois Lançamentos \(Total de Débito de todas as Contas na Adição e Total de Crédito de todas as Contas na Exclusão\)”: 

- Recuperar o movimento de __Débito__ das contas associadas ao lançamento, calcular o total do movimento de débito \(acumulado até o mês\) ou do trimestre e lançar no registro de__ Adição__ da tabela dinâmica\. Criar na Grid de Contas Contábeis da Tela de Lançamentos da Parte A um registro para cada conta associada à __Adição __com seu valor de Movimento de __débito__\.
- Recuperar o movimento de __Crédito__ das contas associadas ao lançamento, calcular o total do movimento de crédito \(acumulado até o mês\) ou do trimestre e lançar no registro de __Exclusão__ da tabela dinâmica\. Criar na Grid de Contas Contábeis da Tela de Lançamentos da Parte A um registro para cada conta associada à __Exclusão __com seu valor de Movimento de__ crédito__\.

Se a linha da tabela dinâmica está associada a demais contas do Plano Empresa com parâmetro de Lançamento de Adição e Exclusão não preenchido ou igual a “Não se Aplica” recuperar o valor do lançamento calculado no item *a\) *[*Se Lançamento de Adição e Exclusão = “*__*Um Lançamento \(Consolidando o Movimento de todas as Contas\)*__*”*,](#UmLançamentoConsolidandooMovTodasContas) e considerar para o lançamento na tabela dinâmica a __soma__ do valor do lançamento calculado ao valor recuperado das contas associadas conforme [RN\-I04\.05 – Atribuição de Saldos – Linhas dos Registro M300/M350](#RNI0405AtualizaçãodoscamposLançamAjust)\.

__Manter Ajustes Manuais:__

Ao efetuar novamente o processamento em lote, com a opção de manter ajustes manuais, executa [as regras acima](#regrasaplicacaolancamentosdeAE) e depois mantem o valor informado manualmente para a linha \(valor parcial, valor de ajustes\)\.

MFS\-14779

RNI04\.05

<a id="RNI0405AtualizaçãodoscamposLançamAjust"></a>__Atualização dos campos Lançamentos/Ajustes e Saldo da tela de Lançamentos da Parte A \(M300,M350\)__

Deverá ser verificada se a linha da tabela dinâmica utiliza lançamentos contábeis para composição dos valores\. Considerar que todos os registros de lançamentos da parte A do exercício, que possuem valor na coluna “Lançamentos/Ajustes” da aba “Contas Contábeis” no período ou para qualquer período anterior ao processado, utiliza Lançamentos contábeis para compor o saldo\.

Se a conta que está sendo processada utilizar lançamentos contábeis ou ajustes, o resultado do processamento populará os campos “Saldo” e “Lançamentos/Ajustes”\. Caso a conta que está sendo processada não utiliza lançamentos contábeis ou ajustes, somente o campo “Saldo” deve ser populado\.

O valor total da linha parametrizada para os registros M300 e M350 pode ser positivo ou negativo\. Para identificar esta característica de cada saldo recuperado, é necessário realizar a tabela de conversão dos valores para totalização conforme RNG00039 – Conversão de valores para totalização\.

Considerar a somatória dos valores contidos na coluna Lançamentos/Ajustes \+ o valor da coluna Saldo correspondente às linhas onde o campo lançamentos/Ajustes for igual a zero, conforme RNG00040\- Somatória coluna Lançamentos/Ajustes\. 

- Se o resultado do cálculo for negativo, exibir a mensagem DW00137

Deverá ser verificada a tabela a parametrização no campo Recuperação dos Valores da Tela Recuperação dos Valores \- Apuração IRPJ/CSLL e o saldo deverá ser recuperado conforme definição abaixo:

<a id="RecupValores_Saldo"></a>

1. __Se conteúdo do campo Recuperação dos Valores = Saldo ou Não houver parametrização: __

__Cálculo do campo Saldo:__

Buscar todos os Saldos Finais Acumulado dos registros que estão na tabela de Saldos Contábeis conforme \- RNG00033 – Recuperação Acumulada dos Saldos\.

Os saldos devem ser recuperados de acordo com a parametrização citada na RNG00031 – Recuperação de Saldos\.

A partir da checagem acima, o sistema recupera os saldos finais das contas contábeis e centros de custo associados se houver, a cada uma das contas das tabelas dinâmicas parametrizadas\. 

__Cálculo do campo Lançamentos/Ajustes:__

a \- Deve ser recuperado da tabela de Saldos Contábeis somente o movimento de débito e crédito do mês ou trimestre conforme  RNG00032 – Recuperação do Movimento do Saldo 

b\- Os saldos devem ser recuperados de acordo com a parametrização citada na RNG00031– Recuperação de Saldos\.

c\- Soma\-se os valores conforme RNG00035 – Soma dos Saldos,  para cada uma das contas das tabelas dinâmicas parametrizadas\.

d\- Deve ser recuperado o valor processado no campo lançamentos/ajustes para a mesma linha da tabela dinâmica no mês anterior, quando existir processamento para o mesmo exercício\.

1. Se o valor recuperado no item “C” possuir o mesmo indicador de débito ou crédito do valor recuperado no item B, apresenta o resultado da soma dos dois valores recuperados \(b \+c\)\.
2. Se o valor recuperado no item “C” não possuir o mesmo indicador de débito ou crédito do valor recuperado no item B, apresentar o valor absoluto do resultado da subtração dos dois valores recuperados \(b \- c\) e manter o indicador do maior valor\.
3. __Se conteúdo do campo Recuperação dos Valores = Movimento: __

	

1. Deve ser recuperado da tabela de Saldos Contábeis o movimento de débito e crédito de todos os Saldos Contábeis, informados ou zerados, \(acumulados até o mês\) ou do trimestre conforme [ RNG00032– Recuperação do Movimento do Saldo](#_RG-P07_–_Recuperação)\.
2. Os saldos devem ser recuperados de acordo com a parametrização citada na   RNG00031– Recuperação de Saldos\.
3. Deve ser recuperado o valor processado para a mesma linha e conta da tabela dinâmica no mês anterior para os campos Lançamento e Saldo da tela de lançamentos da parte A, quando existir processamento para o mesmo exercício,
4. O campo Lançamentos/Ajustes só deve ser calculado quando o valor recuperado para este campo no mês anterior for diferente de nulo\. O campo Saldo sempre deve ser calculado\. Para compor dos dois campos verificar:
	- 
		1. Se o valor recuperado no item “C” possuir o mesmo indicador de débito ou crédito do valor recuperado no item B, apresenta o resultado da soma dos dois valores recuperados \(b \+c\)\.
		2. Se o valor recuperado no item “C” não possuir o mesmo indicador de débito ou crédito do valor recuperado no item B, apresentar o valor absoluto do resultado da subtração dos dois valores recuperados \(b \- c\) e manter o indicador do maior valor\.
5. __Se conteúdo do campo Recuperação dos Valores = Total de Crédito ou Total de Débito:__
6. Deve ser recuperado da tabela de Saldos Contábeis o movimento de crédito ou débito de todos os Saldos Contábeis, informados ou zerados, \(acumulados até o mês\) ou do trimestre\.
7. Deve ser recuperado o valor processado para a mesma linha e conta da tabela dinâmica no mês anterior para os campos Lançamento e Saldo da tela de lançamentos da parte A, quando existir processamento para o mesmo exercício,
8. O campo Lançamentos/Ajustes só deve ser calculado quando o valor recuperado no para este campo no mês anterior for diferente de nulo\. O campo Saldo sempre deve ser calculado\. Realizar o cálculo abaixo para composição dos valores destes dois campos:
9. Apresenta o resultado da soma dos dois valores recuperados acima \(a \+b\)\.
10. __Se conteúdo do campo Recuperação dos Valores = Lançamentos Contábeis:__
11. O campo Saldo deve ser calculado conforme  [item 1 desta regra](#RecupValores_Saldo)\.
12. O campo Lançamentos/Ajustes só deve ser calculado quando o valor recuperado para este campo no mês anterior for diferente de nulo\. \(Este campo será atualizado no processo de geração automática dos lançamentos\)
13. Apresenta no campo Valor da Parte A o valor recuperado no item b acima\. 

__Atenção:__ Ao utilizar a parametrização de Recuperação de valores, se no período anterior for informado valores no campo Lançamentos/Ajustes, o valor só será considerado, se o usuário confirmar no modal da tela de Lançamentos da Parte A tal informação, ou seja, a parametrização é sempre prioridade\.

__Preenchimento do campo Histórico__

Após o processamento de atribuição dos saldos para as contas contábeis associadas a lançamentos da parte A \(M300 e M350\):

Para cada lançamento da parte A com valor diferente de zero preencher o campo Histórico da linha do registro M300/M350 com o valor padrão do parâmetro “Histórico Padrão” cadastrado na tela de “Informações ECF”, \(aba LALUR e LACS\)\. Se o lançamento já possuir Histórico preenchido e o parâmetro “Manter Ajustes Manuais Realizados” estiver selecionado, não substituir o conteúdo do campo e aplicar __RNI04\.07__

RNI04\.06

__Regra Fixar Saldo Inicial nas linhas de reversão de saldos__

__Objetivo: __Fazer com que os valores que estiverem nas linhas 95, 94 ou 81 sempre serão sobrepostos pelo saldo inicial das contas\. Essa regra corresponde a um conceito contábil\.

Na tela Abertura da Apuração agrupamento Cálculo das Contas da Parte A e da Parte B  item Contas da Parte A, é permitido fixar o saldo inicial das contas patrimoniais naturezas \(1 – Ativo, 2 – Passivo e 7 – Patrimônio Líquido\), associadas às linhas de reversão de saldos por meio da parametrização dos campos “Fixar saldo inicial na linha do M300” e “Fixar saldo inicial na linha do M350” que se selecionados \(um ou outro, ou ambos\), irão fixar o saldo inicial, conforme abaixo:

- Nos registros M300A/M350A aplicar a regra na linha 95
- Nos registros M300B/M350B aplicar a regra na linha 94
- Nos registros M300C/M350C aplicar a regra na linha 81

__Observações:__

- Contas de resultado cujos indicadores equivalem a: 3 – Despesa, 4 – Receita e 8 – Custos, não serão incluídas nesta regra\.
- Esta parametrização funcionará independentemente da parametrização da Recuperação de Valores\.
- Nos casos de apuração anual, fixar o saldo inicial de janeiro ou do primeiro período em caso de situação especial, em todos os meses da apuração\. 
- Para apuração Trimestral, fixar o saldo inicial do primeiro mês do trimestre que está sendo processado\.

Ao final do processamento, exibir a mensagem DW0013, demonstrando a linha de acordo com a parametrização da tela de Informações ECF \- Qualificação da PJ\.                         

MFS\-14779

RNI04\.07

__Efetuar Ajuste na Conta da Parte B associadas com contas da Parte A__

Objetivo:__ __Este processo depende da combinação Associação das Contas da Parte B com a Parte A \+ seleção do parâmetro Efetuar Ajuste na Conta da Parte B” tela Abertura da Apuração e tem como objetivo gerar umajuste automático na conta da parte b com base na associação das contas da parte A\.

Após a atribuição dos saldos para as contas contábeis associadas aos registros \(M300 e M350\) quando a flag “Efetuar Ajuste na Conta da Parte B” tela Abertura da Apuração correspondente à Abertura de Apuração que está sendo processada estiver preenchida:

- 
	- Verificar a existência de parametrização na tela “Associação das Contas da Parte B com Contas da Parte A” para a Central de Cadastros com Data Inicial menor ou igual à data inicial informada na tela Informações do ECF e Registros \(M300 M350\) igual ao registro que está sendo processado\.
		- Se houver mais de uma associação, recuperar a mais próxima à Data Inicial informada na tela Informações do ECF\. Vide exemplo especificado na RNI02\.
- Se não for encontrada nenhuma associação o sistema deve exibir a mensagem TR00905\.

__Identificação da conta para gerar ajuste__

Recuperar as Contas da Parte B na tela Lançamentos da Parte B \(M410\) considerando como  critério de busca, os registros da tela de Ajustes da Parte B\(M010\) que possuírem as equivalências abaixo com os Lançamentos da Parte A\(M300, M350\):

__Ajustes da Parte B\(M010\)__

__Equivalência__

__Lançamentos da Parte A \(M300, M350\)__

CNPJ da Empresa

= \(igual\)

CNPJ da Empresa

CNPJ do Estabelecimento Matriz/SCP

= \(igual\)

CNPJ do Estabelecimento Matriz/SCP

Tipo de Tributo \(IRPJ ou CSLL\)

= \(igual\)

Tipo de Tributo: IRPJ \(M300\) ou CSLL \(M350\) 

Data Inicial

Igual

Data Inicial da Informações ECF correspondente à Data Inicial da Abertura da Apuração 

Data Limite

ǿ ou >\-\(nulo, maior ou igual\)

Data Inicial

Exercício

= \(igual à\)

Exercício

Para cada Conta da Parte B parametrizada não encontrada o sistema deve exibir a mensagem TR00906\.

__Identificando a associação realizada__

Para as Contas da Parte B corretamente cadastradas identificar as linhas da tabela dinâmica e/ou as contas contábeis e centros de custo associados\. 

Se houver linha da tabela dinâmica associada com a conta da parte B: Considerar como ajuste da parte B o valor da conta contábil \+ centro de custo associado a linha da tabela dinâmica\. 

Se não houver linha da tabela dinâmica associada com a conta da parte B: Considerar que todos os valores da conta contábil associada \+ centro de custo irá compor o valor do Ajuste da Parte B\.

Se for informado Centro de Custo na associação:

Verificar se para uma conta do plano empresa foram parametrizados os mesmos centros de custos na “Associação das Contas da Parte B com Contas da Parte A” e na “Associação das Tabelas Dinâmicas com o Plano da Empresa” para a linha que está sendo processada e considerar os centros de custo informados na associação\.

Se não for informado Centro de Custo na Associação das Contas da Parte B com Contas da Parte A: Considerar todos os centros de custo, nulos ou não\.

__Composição do valor para o ajuste__

Para cada conta da parte B executar o processo abaixo:

Recupera da memória de cálculo dos registros M300/M350 os valores diferentes de zero calculados para as linhas da tabela dinâmica e/ou contas contábeis e centro de custo associadas a conta da parte B\.

Somar o valor das contas contábeis encontradas conforme [RG\-P05 – Conversão de valores para totalização](#_RG-P05_–_Conversão)\.

Efetuar um único lançamento de ajuste na parte B com as seguintes informações:

__Ajustes da Parte B\(M010\)__

__Valor__

Origem

"Parte A"

Histórico

<Desc\.da Linha da Tabela Dinâmica> <Período de Apuração> <Exercício>

Data Lancto\.

<Data Final> informada na tela de Abertura da Apuração processada\.

Valor

Valor calculado para as contas do plano empresa associadas

Ind\. do Valor

Verificar __Regra do Indicador__\*

Ajuste com Origem na Parte B

“Incremental”

\*__Regra do Indicador: __O Indicador do Lançamento da Conta da Parte B deve ser recuperado a partir do tipo de lançamento conforme tabela abaixo: 

__Tipo de Lançamento__

__Indicador do lançamento de ajuste da parte B__

Adição ou Lucro

D – Devedor

Exclusão ou Compensação de Prejuízo

C – Credor

O Sistema deve garantir que não sejam duplicados os lançamentos de ajuste da parte B na ocorrência de um reprocessamento\.

Se for localizado um Lançamento para a mesma conta da parte B para o mesmo lançamento da parte A criado pelo usuário e o parâmetro “Manter Ajustes Manuais Realizados” estiver selecionado, o lançamento não deve ser substituído\. Caso o parâmetro “Manter Ajustes Manuais Realizados” não esteja preenchido o lançamento deve ser substituído\.

A inclusão do ajuste e atualização dos valores deve seguir as mesmas regras contidas no botão “Salvar” \(RN000\) da tela Lançamentos da Parte B \(M410\)\. Tela Lancamentos da Parte B \(M410\)\.doc\.

Este registro de ajuste deve estar visível na tela de Lançamentos da Parte A aba Contas da Parte B – Ajustes \(M010\) e visível na tela Lançamentos da Parte B \(M410\)\.

Deve ser atualizado o Tipo de Relacionamento da Tela de Lançamentos da Parte A para “Com conta da Parte B e Conta Contábil”

Atualizar o Valor do Lançamento da Parte A: O valor do somatório de todos os ajustes da parte B e o parâmetro Somatório das Contas da Parte B deve ser marcado\. \(Considerando que os valores a Crédito devem subtrair os valores a Débito e o sinal de acordo com a tabela abaixo\)\. 

__Tipo de Lançamento__

__Sinal no campo "Valor"__

__Indicador do somatório de todos os ajustes da parte B__

Adição ou Lucro

\+ \(positivo\)

D – Devedor

Adição ou Lucro

\- \(negativo\)

C – Credor

Exclusão ou Compensação de Prejuízo

\+ \(positivo\)

C – Credor

Exclusão ou Compensação de Prejuízo

\- \(negativo\)

D \- Devedor

Se o sistema localizar algum ajuste da parte B com Indicador igual C \- Credor e tipo de lançamento igual a  Adição ou Lucro ou Indicador  igual D – Devedor  e tipo de lançamento igual a Exclusão ou Compensação de Prejuízo exibir a mensagem TR01143\.

OBS: Quando o status da apuração for __Reapurar__ e for identificada associação das contas contábeis geradas pelo processo definido quando na RNC03 quando o flag Incluir Lançamento automático com Relacionamento ESTIVER selecionado, na composição do valor do ajuste na conta da parte B, as contas contábeis devem ser desconsideradas\.

MFS\-14779

RNI04\.08

__Percentual Receita Bruta N500 e N650__

Objetivo: Permitir que na linha 2 do registro N500 seja informado percentuais a serem aplicado no movimento da conta contábil associado à linha, pois na linha 2 devem ser considerados valores da receita bruta e valores da receita bruta correspondem ao movimento do período que é o movimento real que ainda pode ter um percentual aplicado de acordo com a tabela do governo\.

Para atribuir o saldo para as linhas 1 e 2 do registro N500 e N650 respeitar os critérios abaixo:

A linha 1 deverá ser gerada com valor independentemente do conteúdo do campo Tipo de Receita preenchido na tela Abertura da Apuração considerando os valores acumulados conforme [RG00033 – Recuperação Acumulada dos Saldos](#_RG-P07_–_Recuperação)\.

__Quando informado na tela de associação das tabelas dinâmicas com o plano empresa um percentual, considerar as regras abaixo:__

A linha 2 deverá ser gerada com valor somente quando na tela Abertura da Apuração o campo Tipo de Receita = “Receita Bruta” ou “Comparativo” considerando os valores de total de débito e total de crédito conforme [RG00032 – Recuperação do Movimento do Saldo](#_RG-P08_–_Recuperação) e as regras abaixo:

- Soma\- se separadamente o total de crédito e o total de débito das contas contábeis associadas às linhas da tabela dinâmica que possuem o mesmo percentual\. 
- Soma\-se os valores conforme [ RNG00035 \- Soma dos Saldos Contábeis ](#_RG-P04_–_Soma), considerando a regra abaixo para aplicar o percentual:
- Neste valor \(vamos chamá\-lo de Valor da Receita Bruta Sujeita a X,XX%’\) deve ser aplicado o percentual associado \(apenas se o valor for a crédito\) e este resultado será chamado de Valor Calculado \(referente ao percentual associado\)\. Caso o valor encontrado seja débito, exibir a mensagem DW00156\.
- Se crédito, na tela de Entrada Manual de Valores, atualizar os campos ‘Valor da Receita Bruta Sujeita a X,XX%’ e ‘Valor Calculado’, conforme regras abaixo:
- Campo Valor da Receita Bruta Sujeita a X,XX%, com o valor calculado sem o indicador;
- Campo Valor Calculado \(correspondente ao percentual associado\), deve ser considerado o resultado da expressão: __Valor da Receita Bruta Sujeita a X,XX%  \* \(valor do percentual\)/100 __, onde os percentuais podem variar de acordo com os registros:

__N500 \(linha 2\)__ 1,6%, 8%, 16%, 32%, 100%

__N650 \(linha 2\) \- __12%, 32%, 100%

- O valor encontrado para o campo ’Somatório do Valor Calculado’, será o saldo a ser considerado para a linha 2 do registro N500 e N650\.

__Se não informado o percentual da receita bruta na tela de associação das tabelas dinâmicas com o plano empresa, considerar:__

A linha 2 deverá ser gerada com valor somente quando na tela Abertura da Apuração o campo Tipo de Receita = “Receita Bruta” ou Comparativo considerando os valores de total de débito e total de crédito conforme [RG00032 – Recuperação do Movimento do Saldo](#_RG-P08_–_Recuperação)\.

__Validações:__

\-Se pelo menos uma conta contábil possuir Percentual da Receita Bruta, todas as contas contábeis também devem possuir Percentual de Receita Bruta para tal linha/registro, caso contrário exibir a mensagem DW00208\.

\- Se pelo menos uma conta contábil possuir Percentual da Receita Bruta definido por centro de custo, todos os Centros de Custo relacionados para tal Conta Contábil /linha/ registro, também devem possuir Percentual de Receita Bruta, caso contrário exibir a mensagem DW00208\.

MFS\-17657

RNI05

Origem dos Saldos = Associações

<a id="AssociacaoTabReferencial"></a>__Associação do Plano Referencial com Plano Empresa:__

Recuperar a associação informada na tela de Informações ECF \(campo Associação Tabela Referencial com o Plano Empresa\)\.

<a id="Atribuindo_saldo_conta_referencial"></a>__Para a atribuição do saldo para cada conta do Plano Referencial atender os seguintes critérios:__

__Recuperação dos saldos para associações com o Plano Referencial__

- Deverá ser utilizado como apoio a planilha \[Plano de contas referencial\.xlsx\]
	- 
		1. Deverá ser respeitado o agrupamento dos saldos de acordo com o registro conforme coluna “Registro”\. Para os registros L100 e L300 recuperar as contas referenciais do plano de acordo com a qualificação da pessoa jurídica \(RNG00005\)
- Deverá ser respeitada a sequência do número de ordem exibido na coluna “Ordem” para realizar atribuição de valor na conta referencial
- Aplicar RNG00036 \- Escrituração X Forma de Tributação

__*Sequência de execução das Regras:*__

- 
	- 
		- 
			1. __*Se possuir atividades mistas – *__[__*RNI06 – Calculo Atividade Mista*__](#Calculo_percentual_ativ_mista)
			2. __*Se houver rateio – *__[__*Etapa 1 \- Rateio Bloco K*__](#Etapa1_Rateio_BlocoK)

__*2\.1 Saldo Inicial no Período – *__[__*RNI08 – Saldo Inicial das contas de rateio Bloco K*__](#RecuperarSaldoInicialRateio)

- 
	- 
		- 
			1. __*Valor na Conta Referencial  \- *__[__*RNI05\.01 – Recuperação Acumulada dos Saldos*__](#AtribuiçãodosSaldosApurAnual)__*  e  RNG00031 \- *__Recuperação de Saldos

MFS\-13202

MFS\-13995

RNI05\.01

<a id="AtribuiçãodosSaldosApurAnual"></a>__Atribuição dos saldos para Apuração = Anual, de forma acumulada conforme associação efetuada na tela Plano com Plano Empresa:__

Exemplo \- Recuperação Acumulada dos Saldos

Visão de recuperação acumulada com base nos saldos do Exemplo \- Tabela de Saldos Mensais

__Mês__

__Conta Contábil__

__Plano Referencial__

__Saldo Inicial__

__Indicador__

__Débitos__

__Créditos__

__Saldo Final__

__Indicador__

Jan

2\.3\.1

XXXXX

400

 D

100

             \-   

500

 D

Fev

2\.3\.1

XXXXX

400

 D

300

             \-   

700

 D

Mar

2\.3\.1

XXXXX

400

 D

400

             \-   

800

 D

Abr

2\.3\.1

XXXXX

400

 D

500

25

975

 D

- Buscar todos os Valores Totais de Débitos Acumulados, Valores Totais de Créditos Acumulados, Saldos Iniciais do início do período e Saldos Finais Acumulado dos registros que estão na tabela de Saldos Contábeis respeitando os parâmetros informados na tela “Processamento em Lote” \(exceto as contas desconsideradas na verificação anterior\), considerando conteúdo dos campos “Data Inicial” e “Data Final” referente ao “Período de Apuração de forma agrupada e totalizada por Plano Referencial, Plano Empresa e Centro de Custo\(quando informado na associação\) conforme associação efetuada nas telas Plano Referencial com Plano Empresa\.
	- 
		1. Conforme Exemplo – Tabelas de Saldos Mensais, para a conta referencial XXXXX, até o mês de Abril o Saldo Inicial corresponderá a 400, a movimentação de Débitos corresponderá a 500, a movimentação de Créditos corresponderá a 25 e o Saldo Final corresponderá 975\.
- A partir da checagem acima item 1, o sistema recupera os Valores Totais de Débitos Acumulados, os Valores Totais de Créditos Acumulados, os Saldos Iniciais do início do período e Saldos Finais das contas contábeis e centros de custo associados se houver, a cada uma das contas do plano referencial parametrizada\.
	- 
		1. Conforme Exemplo – Tabelas de Saldos Mensais, para a conta referencial XXXXX, deverá ser recuperado em Abril 500 à Débito e 25 à Crédito\.
		2. Para a atribuição do saldo para a conta referencial quando há mais de uma conta contábil associada, efetuar a seguinte verificação:
		3. Verificado o indicador do saldo das contas e quando for identificado saldos a débitos ou saldo a créditos para uma mesma conta referencial, deverá ser identificada a diferença positiva entre os saldos a débito e a crédito e deverá ser mantido o indicador de débito ou crédito do maior valor\. 

Exemplo:

Período Inicial da Apuração: Janeiro

Período de Apuração = Fevereiro

Data Inicial = 01/02/2014

Data Final = 28/02/2014

De acordo com o cenário acima, para o Saldo Inicial, deve ser recuperado o saldo inicial do primeiro mês do Período de Apuração \(saldo inicial do mês de Janeiro\), para o Saldo Final, deve ser recuperado o saldo Final acumulado do último mês \(ou dia\) do Período de Apuração e para os Totais de Débitos e Créditos, deve ser recuperado a somatória de todos os meses do Período de Apuração\.

No final do processo, apresentar a mensagem DW00049

MFS\-13995

RNI06

<a id="Calculo_percentual_ativ_mista"></a>__Calculo dos percentuais de rateio das atividades mistas:__

Exibir para o usuário o percentual de cada atividade permitindo alteração

Os valores encontrados no processamento serão considerados pela rotina de percentuais de rateio das atividades mistas \(tela Percentuais de Rateio das Atividades Mistas\)

Para a realização desta rotina, serão consideradas as contas referenciais 3\.01\.01\.01 que correspondem às atividades gerais e 3\.11\.01\.01 que correspondem às atividades rurais considerado os registros L300A dos registros L300A quando o campo Atividade Rural, na aba parâmetros complementares estiver marcado \(tela Informações ECF\)\. Caso as contas referenciais não forem encontradas exibir a DW00021 e DW00022\.

O valor total do saldo da conta contábil vinculado às contas referenciais \(sintética\) 3\.01\.01\.01 e 3\.11\.01\.01, é o total das atividades mistas\. 

Os valores das atividades gerais e rurais devem ser somados, desprezando os indicadores\. 

Ex\. Atividade Geral: 400D, Atividade Rural: 400C\. Atividade Mista: 800\.

Caso o valor da atividade geral ou rural for zero, gravar zero com indicador crédito \(para a atividade em questão\)\.

O valor do saldo correspondente a atividades geral deve ser gravado no campo VLR\. ATIVIDADE GERAL e o valor do saldo correspondente a atividade rural deve ser gravado no campo VLR\. ATIVIDADE RURAL\.

O percentual de rateio das atividades é o valor do saldo da conta referencial dividido pelo valor total das atividades mistas, multiplicado por 100\. Considerar 4 casas decimais e o valor deve ser arredondado\. Caso o valor da atividade geral for zero, gravar zero no percentual\.

O percentual da atividade geral será gravado no campo PERC\. GERAL CALCULADO

O percentual da atividade rural será gravado no campo PERC\. RURAL CALCULADO

MFS\-13999\-B

RNI07

<a id="Processamento_BlocoK"></a>__Processamento do Bloco K __

Consiste na identificação de uma conta contábil associada a mais de uma conta referencial no momento da importação dos saldos com base na geração do Bloco J \(Registros J050 e J051\), Bloco L \(L100 e L300\), ou uma conta contábil associada a uma conta referencial\.

- Quando este cenário for identificado, o sistema exibirá as contas na tela de Ajuste Manual do Bloco K nas abas Rateio e Demais Ajustes\. 
- Com base na memória do cálculo dos blocos L \(L100 e L300\) \(Contas Contábeis e Centro de Custos associadas as Contas Referenciais\), o sistema processará o Bloco K\.
- Após o ajuste efetuado por meio da tela de Ajuste Manual do Bloco K automaticamente os Blocos L, serão atualizados\.

<a id="Etapa1_Rateio_BlocoK"></a>

1. __Etapa 1 – Verificando a necessidade de efetuar o Rateio do valor do saldo da conta contábil entre os referenciais:__

Após a execução da RNI05, [‘Para a atribuição do saldo para cada conta do Plano Referencial’](#Atribuindo_saldo_conta_referencial), se for encontrada na associação do plano referencial x plano empresa, uma conta contábil, centro de custo associada para mais de uma conta referencial e para o mesmo Registro, será necessário fazer o rateio do saldo para essas contas\. 

- Se na tela associação do plano referencial x plano empresa uma conta contábil for encontrada em mais de uma conta referencial e em uma conta referencial usar centro de custo e em outra referencial esta mesma conta contábil não possuir centro de custo exibir a DW00023\.

Veja exemplo:

Registro

Cta Ref

Cta Contabil

Centro Custo

L300A

3\.01\.01\.07\.01\.15

YMB\.000000\.35615

L300A

3\.01\.01\.09\.01\.99

YMB\.000000\.35615

XXX

- As informações de conta contábil e contas referenciais serão carregadas automaticamente, para a tela de ‘Ajustes do Bloco K’, aba ‘Rateio’\.
- O usuário deverá efetuar este rateio manualmente através da tela ‘Balanço/DRE\(BlocoK\)’, aba ‘Rateio’, conforme Tela  Ajuste  Manual do Bloco K\.doc
- Enquanto o usuário não efetuar o rateio nas contas referenciais, o sistema deverá atribuir à Abertura da Apuração processada o status “Aguardando Alteração Manual” até que o usuário efetue o rateio para todas as contas contábeis exibidas na tela exibindo a mensagem: DW00024\.
- Após a execução da RNI05, [‘Para a atribuição do saldo para cada conta do Plano Referencial’](#Atribuindo_saldo_conta_referencial), se for encontrada na associação do plano referencial x plano empresa, uma conta contábil associada apenas para uma conta referencial, o usuário poderá efetuar algum ajuste no valor do saldo da conta na aba Demais Ajustes\. 
- Aplicar RNI08\.

MFS\-13202  
MFS\-12636

RNI08

<a id="RecuperarSaldoInicialRateio"></a>__Recuperar o saldo inicial de contas de rateio do bloco K a partir do saldo final das apurações anteriores__

Aplicar regra para o primeiro período da apuração anual e todos os períodos de apuração trimestral:

1. Identificar as contas de natureza patrimonial que na associação do plano referencial x plano empresa, uma conta contábil, centro de custo está associada para mais de uma conta referencial, ou uma conta contábil associada apenas para uma conta referencial, conforme [Etapa 1 do Processamento do Bloco K](#Etapa1_Rateio_BlocoK) \(RNI07\):

Para as contas identificadas o sistema deve buscar o Saldo Final e Indicador de Saldo Final da tela ‘Ajuste Manual do Balanço/DRE \(Bloco K\)’, aba ‘Rateio’ e ‘Demais Ajustes’ do período anterior\.

__Busca de Saldo Final__

Se o saldo final não teve ajuste manual, considerar o campo “Saldo Final Calculado”\.

Se o saldo teve ajuste manual, considerar o campo “Saldo Final Informado”\.

__Busca de Período Anterior__

Se o período processado é o primeiro de Apuração Anual ou o primeiro de Apuração Trimestral, o sistema deve identificar se existe uma escrituração anterior com o último período de apuração imediatamente anterior ao período que está sendo processado e com status igual à “Cálculo Realizado”\.

Se o período processado não é o primeiro de Apuração Trimestral o sistema deve identificar se existe apuração anterior na mesma escrituração com status igual à “Cálculo Realizado”\.

Se não for localizado registro anterior de apuração o sistema deve exibir a mensagem: DW00045\.

Se a parametrização da conta contábil for diferente entre uma escrituração e outra, não transportar o saldo final para o saldo inicial e exibir a mensagem DW00006\.

__Preenchimento do Saldo inicial __

__Aba Rateio:__

O Sistema deve preencher o campo Saldo Inicial Informado e Indicador de Saldo Inicial Informado da tela ‘Ajuste Manual do Balanço/DRE \(Bloco K\)’ aba ‘Rateio’ tabela de ‘Contas Referenciais’ do período processado com o resultado da busca de saldo final \(saldo final informado se preenchido, caso contrário o saldo final calculado\)\.

O sistema deve preencher o campo Saldo Inicial Informado e Indicador de Saldo Inicial Informado da tela ‘Ajuste Manual do Balanço/DRE \(Bloco K\)’ aba ‘Rateio’ tabela de ‘Contas Contábeis’ de acordo os valores recuperados \(valores dos campos de saldo inicial Informado e calculado das contas contábeis\)\.

__Aba Demais Ajustes:__

Para a aba de ‘Demais Ajustes’ preencher os campos de Saldo Inicial e Indicador de Saldo Inicial do período processado \(na tabela, uma vez que essas informações não constam em tela\) com o resultado da busca de saldo final recuperado do período anterior \(saldo informado se preenchido, caso contrário o saldo calculado\)\. 

1. __Etapa 2 – Verificando a necessidade de efetuar o Lançamento de Encerramento:__

- Após a execução das RNI05, ‘Para a atribuição do saldo para cada conta do Plano Referencial’ e RNP01, o sistema verificará se foi criado a Forma de Tributação = correspondente ao período da data do evento da situação especial, ou “A12”\.
- Em caso negativo: não será necessário criar lançamentos de encerramento\.
- Em caso afirmativo, o sistema deve verificar se:

__Se A __igual__ \(P __mais__ PL\) __\- utilizando a comparação dos resultados conforme item 2\.1 e utilizando a verificação do indicador do Saldo Final para os cálculos conforme item 2\.2 e 2\.3\.

Não será necessário criar os lançamentos de encerramento

__Se A __menos__ \(P __mais__ PL\) __for diferente__ R __menos__ \(D __mais__ C\)  \- __ utilizando a comparação dos resultados conforme item 2\.1 e utilizando a verificação do indicador do Saldo Final para os cálculos conforme item 2\.2 e 2\.3\. 

Exibir a mensagem ‘DW00062’

__                   __

__Se A __menos__ \(P __mais__ PL\) __for maior que zero e igual a__ R __menos__ \(D __mais __C\) \-__ utilizando a comparação dos resultados conforme item 2\.1 e utilizando a verificação do indicador do Saldo Final para os cálculos conforme item 2\.2 e 2\.3\. 

O sistema deve criar o lançamento de encerramento definido na etapa 3, recuperando os saldos de acordo com a natureza \(RNG00015\)\.

__2\.1 __Para fazer a comparação dos resultados, considerar apenas os valores absolutos, sem os indicadores\.

__2\.2 __Deve ser considerado o Indicador do Saldo Final para todos os cálculos conforme abaixo:

Se Indicador for diferente, deve\-se fazer a subtração dos valores e manter o indicador do maior valor \(que posteriormente será invertido\)\. 

__Natureza__

__Crédito__

__Débito__

__Total__

Passivo \+ Patrimônio Líquido

500,00

 

100,00

 C 

Ativo

 

400,00

Receita

500,00

 

100,00

 C 

Despesa \+ Custo

 

400,00

__Encerramento__

__     100,00 __

__D \(indicador invertido\)__

Se Indicador for igual, deve\-se fazer a soma dos valores e manter o indicador \(que posteriormente será invertido\)\.

__Natureza__

__Crédito__

__Débito__

__Total__

Passivo \+ Patrimônio Líquido

500,00

 

900,00

 C 

Ativo

400,00

 

Receita

500,00

 

900,00

 C 

Despesa \+ Custo

400,00

 

__Encerramento__

__     900,00 __

__D \(indicador invertido\)__

1. __Etapa 3 – Efetuando o Lançamento de Encerramento__

__3\.1 __Verificando existência da conta na tela de Informações ECF

Se não existir uma conta contábil de natureza = ‘Patrimônio Líquido’ na tela de Informações ECF– __LANÇAMENTO DE ENCERRAMENTO – INFORMAÇÕES PARA A CRIAÇÃO DO LANÇAMENTO DE ENCERRAMENTO DO BLOCO K__, exibir a mensagem ‘DW00063’, ou se a conta contábil não estiver na associação do plano referencial com o plano empresa \(associação parametrizada na tela de Informações ECF\), exibir a mensagem DW00066\.

Se houver a parametrização acima, deverá ser criado um lançamento de encerramento automaticamente pelo sistema e sua visualização será permitida na tela de Ajuste do Bloco K, aba Lançamento de Encerramento\. 

O Sistema deve atualizar o Movimento e Saldo Final da conta parametrizada na tela de Informações ECF e visualizada no Ajuste Manual do Balanço/DRE \(Bloco K\)\. No momento da atualização, caso não seja encontrado o registro, o sistema deve criar um novo registro com saldo inicial zero, movimento e saldo final igual ao valor do lançamento de encerramento\.

__3\.2 Gerar Lançamento de Encerramento__

A criação do lançamento implica na alteração do saldo contábil desta conta e do movimento \(de Débito ou Crédito, de acordo com o indicador invertido de A menos \(P mais PL\)\), que deverá atualizar este valor do lançamento no saldo do período \(na memória de cálculo, tabela de resultado do processamento da importação de saldos, saldo por conta referencial, conta contábil e centro de custo\) conforme regras abaixo:

__3\.2\.1 Apuração Anual:__

Gerar o lançamento de encerramento com o valor do resultado da expressão: A menos \(P mais PL\) \(Saldo Final\) e com o indicador invertido\.

Exemplo: A menos \(P mais PL\) = 300C, o valor do lançamento de encerramento será 300D para a conta contábil de natureza = ‘7’ indicado na tela de Informações do ECF,

Segue estrutura do lançamento:

CNPJ do Estabelecimento/SCP

Informar o CNPJ do Estabelecimento Matriz/SCP

Data do Lançamento

Data Final da tela de Informações do ECF \(escrituração\) gerada com base nas situações abaixo:

- Data do último mês
- Data do evento quando se tratar de situação especial

Valor do Lançamento

Valor do Lançamento de encerramento gerado

Código da Conta Contábil

Código da conta contábil informada na tela Informações ECF \(Aba Lançamento de Encerramento\) 

Código do Centro de Custo

Centro de custo referente a conta contábil informada no campo Código da Conta Contábil\.

Total do Ativo

Referente a conta contábil

Total de Despesas

Referente a conta contábil

Total de Receitas

Referente a conta contábil

Total do Passivo

Referente a conta contábil

Indicador do Lançamento

Indicador do valor do lançamento \(D, C\)\.

MFS\-13202

MFS\-12636

MFS\-12620

RNI09

<a id="A00"></a>__Geração automática da Apuração Anual \(A00\)__

- O A00 deverá ser criado para os registros que serão processados conforme RNP \- REGRAS – PROCESSAMENTO DOS REGISTROS \(com exceção dos registros de abertura, identificação e encerramento\) dos blocos L K, M, N e U\.
- Deverá ser gerado na apuração com base nas apurações realizadas de Janeiro \(A01\)\.\.\.Dezembro \(A12\) quando a Forma de Tributação = “Lucro Real” com base na visão de [Recuperação Acumulada dos Saldos](#Recuperação_Acumulada_Saldos) conforme RNI05\.
- A apuração Anual \(A00\) será gerada sempre e de forma automática utilizando como base os valores do último mês processado\. 
- Os valores existentes nas linhas das tabelas dinâmicas e/ou plano referencial no mês utilizado para o processamento do Janeiro \(A01\)\.\.\.Dezembro \(A12\)  deverá ser replicado para a apuração Anual \(A00\) e após este processamento será possível visualizar o resultado na tela Lucro Real, com as informações dos registros processados\.
- Para as linhas correspondentes aos registros N620, N660 não deverá ser gerado A00 e para a linha 2 dos registros N500 e N650 deverá ser gerado zero\.

 

MFS\-12636

MFS\-12632

RNI10

__Parâmetro “Manter Ajustes Manuais Realizados”__

Se na execução do “Processamento em Lote” a rotina de “Transcrição dos Valores Empresa para Referenciais Fisco” e o parâmetro “Manter Ajustes Manuais Realizados” estiverem selecionados, verificar se para os Estabelecimentos e Abertura das Apurações há inserção de forma manual e/ou via importação \(upload\) nas telas/tabelas abaixo:

1. “Entrada Manual de Valores” \(todos os ajustes na tela\)
	- 
		- Modal Entrada Manual \(campos: Valor, Percentual de Receita Bruta e Justificativa\)\.

Se houver inserção manual realizada na tela/tabela de “Entrada Manual de Valores”, aplicar a regra abaixo:

- Executar a rotina de “Transcrição dos Valores Empresa para Referenciais Fisco”, porém o registro que contenha algum dado inserido ou alterado manualmente no processamento anterior efetuado para o mesmo “Estabelecimento” e para a mesma “Abertura da Apuração” e que não tenha sido selecionado através do ícone “Descartar Entrada Manual” ou através do botão “Descartar todas as Entradas Manuais” deverão ser mantidos na base de dados e após a execução da rotina de “Importação dos Saldos”, os status dessa Abertura da Apuração deverá ser atualizado para “Importação dos Saldos Realizada”\. As linhas que forem alteradas de NS para N e que possuem valor negativo \(na tela de entrada manual de valor\), atualizar esta informação na tela \(campo valor sem sinal negativo\) e considerar no processamento este valor atualizado \(sem o sinal\)\.
	- Se o usuário selecionar o botão “Descartar Entrada Manual” ou “Descartar todas as Entradas Manuais”, as informações inseridas para a\(s\) linha\(s\) do\(s\) registro\(s\) devem ser substituídas pelas informações originais decorrente da Importação dos Saldos, como se o usuário não tivesse optado por manter os ajustes para essas linhas desses registros\.

1. Telas__ \- “Lançamentos da Parte A”__ e campos abaixo:

- Lançamentos vinculados, Processos vinculados, Ajustes vinculados e Status

Verificar definições específicas na regra \(RNI10\.03\), tópicos:

[Tipo de Relacionamento – Conta Contábil](#_RN-M01.01_–_)

[Tipo de Relacionamento –  Com Conta da Parte B e Com Conta Contábil](#_RN-M01.02_–_)

[Tipo de Relacionamento –  Sem Relacionamento](#_RN-M01.03_–_)

[Tipo de Relacionamento – Com Conta da Parte B](#_RN-M01.04_–_)

[Tipo de Relacionamento – Com Conta Contábil e Associação](#_RN-M01.05_–_)

1. __Tela \- Ajustes da Parte B__ – Somente quando o relacionamento for com Parte A

Verificar definições específicas na regra \(RNI10\.03\), tópicos:

[Tipo de Relacionamento –  Com Conta da Parte B e Com Conta Contábil](#_RN-M01.02_–_)

[Tipo de Relacionamento – Com Conta da Parte B](#_RN-M01.04_–_)

1.  “Ajustes do Bloco K” \(RNI10\.01\)

- Conteúdo da Aba Rateio \(Origem do Conteúdo \- Inserção manual e/ou via importação \(upload\)\)
- Conteúdo da Aba Demais Ajustes \(Origem do Conteúdo \- Inserção manual\)
- Justificativas \- Se houverem justificativas para contas contábeis e ou referenciais que foram apagadas, as justificativas deverão ser removidas juntamente com as respectivas contas, caso contrário, manter as justificativas existentes\.

1. “Tela Lucro Real \(RNI10\.02\)”

- Anexos \(Origem do Conteúdo \- Inserção manual\)

1. “Percentual de Rateio de Atividades Mistas”

- Conteúdo do campo \- Perc\. Geral Ajustado
- Conteúdo do campo \- Perc\. Rural Ajustado

1. “Percentual de Receita Bruta

- Todos os percentuais de Receita Bruta ajustados no modal Percentuais de Receita Bruta, da tela Entrada Manual de Valores\.

1. Para as tabelas listadas nos itens “b”, “c”, “d”, “e”, “f” e “g” executar a rotina de “Transcrição dos Valores Empresa para Referenciais Fisco”, porém o registro que contenha dados inseridos ou alterados manualmente dentro do processamento anterior efetuado para o mesmo “Estabelecimento” e para a mesma “Abertura da Apuração” deverão ser recuperados para a base de dados e as particularidades da recuperação estão definidas nas RNS RNI10\.01 e RNI10\.02\.

__Não manter ajustes manuais realizados nas seguintes condições:__

- Se não houver entrada manual realizada nas telas/tabelas listadas nos itens “a”, “b”, “c”, “d”, “e”, “f” e “g” desta regra, não haverá dados a serem mantidos no processo;
- Se na execução do “Processamento em Lote” a rotina de “Importação dos Saldos” estiver selecionada, porém o parâmetro “Manter Ajustes Manuais Realizados” não estiver selecionado, efetuar a limpeza das telas/tabelas de listadas nos itens “a”, “b”, “c”, “d”, “e”, “f” e “g” desta regra\.
	- 
		1. Para o campo Status do item “b” não será realizada a limpeza, logo se o Status antes da “Importação de Saldos” era diferente de “Considerar Movimento” após a nova importação de saldos o status deverá ser retornado para “Considerar Movimento”\. 

__Tela Incentivos Fiscais:__

Se houver inserção manual realizada na tela/tabela de “Incentivos Fiscais”, independentemente da seleção do parâmetro “Manter Ajustes Manuais Realizados”, os dados não deverão serão mantidos, pois essas informações são calculadas pelo sistema \(Cálculos dos Registros e Fórmulas\)\.

__Linhas das Tabelas Dinâmica e Conta Referencial:__

No momento da Transcrição de Valores se a linha da tabela dinâmica ou conta referencial deixar de existir, devido alteração na tabela dinâmica devido alteração no manual leiaute aplicar as regras abaixo:

- Para a linha da tabela dinâmica, exibir a DW00157;
- Para a conta referencial, exibir a DW00158\.

MFS\-12636

MFS\-12632

MFS\-12623

RNI10\.01

__Parâmetro “Manter Ajustes Manuais Realizados” selecionado – Ajustes do Bloco K__

As regras definidas abaixo podem ter dependência com as regras existentes na tela de Ajuste manual do Balanço/DRE \(Bloco K\)\.  No caso de dúvidas, verificar o documento Tela Ajuste  Manual do Bloco K\.doc

1. __Comportamento dos dados na “Aba Rateio”__

Exemplo do dado existe na tela/tabela de rateios antes da nova importação dos saldos com parâmetro manter selecionado:

__Conta Contábil__

__Saldo Calculado__

__Saldo Informado__

__Conta Referencial__

__Saldo Informado__

Conta Contábil1

150,00

150,00

Cta Ref 1

50,00

Cta Ref 2

50,00

Cta Ref 3

50,00

__Cenários:__

Foi realizada uma nova " Transcrição dos Valores Empresa para Referenciais Fisco" com o parâmetro "Manter os Ajustes Manuais Realizados", selecionado, porém uma conta contábil foi desassociada da conta referencial\. Apagaremos a conta referencial \(Cta Ref 1\) e o saldo informado \(50,00\) correspondente, recuperaremos os demais valores e será exibida a DW00047 e o status dessa abertura da apuração deverá ser “Aguardando Alteração Manual”\. Neste cenário a justificativa será removida \(conforme item 3 desta regra\)\. Conforme exemplo abaixo:

__Conta Contábil__

__Saldo Calculado__

__Saldo Informado__

__Conta Referencial__

__Saldo Informado__

Conta Contábil1

150,00

150,00

Cta Ref 1

50,00

Cta Ref 2

50,00

Cta Ref 3

50,00

- Foi realizada uma nova " Transcrição dos Valores Empresa para Referenciais Fisco" com o parâmetro "Manter os Ajustes Manuais Realizados", selecionado, porém uma conta contábil foi desassociada de uma conta referencial\. Apagaremos a conta referencial \(Cta Ref 1\) e o saldo informado \(50,00\) correspondente e pelo fato da conta contábil estar associada apenas a uma conta referencial, tal associação será visualizada na aba “Demais Ajustes” com o conteúdo do campo Saldo Informado e Indicador do Saldo informado \(Cta Ref 2\), e os ícones Validar e Justificar preenchidos conforme estava na aba Rateio, será exibida a DW00047 e o status dessa  abertura da apuração deverá ser “Importação de Saldos Realizada”\. Neste cenário a justificativa será removida \(conforme item 3 desta regra\)\. Conforme exemplo abaixo:

__Conta Contábil__

__Saldo Calculado__

__Saldo Informado__

__Conta Referencial__

__Saldo Informado__

Conta Contábil1

100,00

100,00

Cta Ref 1

50,00

Cta Ref 2

50,00

- Foi realizada uma nova " Transcrição dos Valores Empresa para Referenciais Fisco" com o parâmetro "Manter os Ajustes Manuais Realizados" selecionado, porém o saldo da conta contábil ou o indicador foi alterado\. Os saldos da conta contábil serão atualizados, recuperaremos as contas referenciais e os saldos correspondentes existentes antes da importação dos saldos será exibida a DW00048 e o status dessa abertura da apuração deverá ser “Aguardando Alteração Manual”\. Neste cenário a justificativa será removida \(conforme item 3 desta regra\)\. Conforme exemplo abaixo:

__Conta Contábil__

__Saldo Calculado__

__Saldo Informado__

__Conta Referencial__

__Saldo Informado__

Conta Contábil1

200,00

150,00

Cta Ref 1

50,00

Cta Ref 2

50,00

Cta Ref 3

50,00

- Foi realizada uma nova "Transcrição dos Valores Empresa para Referenciais Fisco" com o parâmetro "Manter os Ajustes Manuais Realizados" selecionado, porém a conta contábil não existe mais, não há valores a serem recuperados e será exibida a DW00051 e a conta referencial e o rateio serão apagados e o status dessa abertura deverá ser alterado para “Importação dos Saldos Realizada”\. \(Neste cenário tudo será excluído\)\. Conforme exemplo abaixo:

__Conta Contábil__

__Saldo Calculado__

__Saldo Informado__

__Conta Referencial__

__Saldo Informado__

Conta Contábil1

150,00

150,00

Cta Ref 1

 50,00

Cta Ref 2

 50,00

Cta Ref 3

 50,00

- Foi realizada uma nova "Transcrição dos Valores Empresa para Referenciais Fisco" com o parâmetro "Manter os Ajustes Manuais Realizados" selecionado, porém a conta referencial nova foi incluída exibir a DW00024 e o status dessa abertura da apuração deverá ser “Aguardando Alteração Manual”\. Neste cenário a justificativa será removida \(conforme item 3 desta regra\)\. Conforme exemplo abaixo:

__Conta Contábil__

__Saldo Calculado__

__Saldo Informado__

__Conta Referencial__

__Saldo Informado__

Conta Contábil1

150,00

150,00

Cta Ref 1

 50,00

Cta Ref 2

 50,00

Cta Ref 3

 50,00

Cta Ref 4

150,00

- Foi realizada uma nova "Transcrição dos Valores Empresa para Referenciais Fisco" com o parâmetro "Manter os Ajustes Manuais Realizados" selecionado, porém uma conta contábil foi incluída na associação de mais de uma conta referencial\. Será exibida a DW00024 e deverá ser aplicada as tratativas existentes na tela de rateio e o status dessa abertura da apuração deverá ser “Aguardando Alteração Manual”\. Conforme exemplo abaixo:

__Conta Contábil__

__Saldo Calculado__

__Saldo Informado__

__Conta Referencial__

__Saldo Informado__

Conta Contábil1

200,00

Cta Ref 1

200,00

Cta Ref 2

200,00

Cta Ref 3

200,00

Cta Ref 4

200,00

Se não houve rateio distribuído para as contas referenciais associadas às contas contábeis \(ou seja, se não houver ajuste manual no campo Saldo Informado\), e na nova importação dos saldos com o parâmetro “Manter Ajustes Manuais Realizados” selecionado, foi identificada a mesma conta contábil, todavia o saldo da conta contábil é diferente do saldo identificado na importação anterior, o conteúdo do campo “Saldo Informado” de cada conta referencial será atualizado com base no novo saldo da conta contábil\. Conforme exemplo abaixo:

“Transcrição dos Valores Empresa para Referenciais Fisco” sem edição do campo Saldo Informado

__Conta Contábil__

__Saldo Calculado__

__Saldo Informado__

__Conta Referencial__

__Saldo Informado__

Conta Contábil1

200,00

Cta Ref 1

200,00

Cta Ref 2

200,00

“Transcrição dos Valores Empresa para Referenciais Fisco” com o parâmetro “Manter Ajustes Manuais Realizados” selecionado, saldo da “Conta Contábil1” alterado para 300,00\. 

__Conta Contábil__

__Saldo Calculado__

__Saldo Informado__

__Conta Referencial__

__Saldo Informado__

Conta Contábil1

300,00

Cta Ref 1

300,00

Cta Ref 2

300,00

1. __Comportamento dos dados na “Aba Ajustes” __

- Foi realizada uma nova "Transcrição dos Valores Empresa para Referenciais Fisco" com o parâmetro "Manter os Ajustes Manuais Realizados" selecionado, porém não foi encontrada a mesma conta referencial para a mesma conta contábil, será exibida uma mensagem DW00047 e o registro será apagado\.

1. __Justificativas__

- Se houverem justificativas para contas contábeis e pelo menos uma conta referencial for apagada ou incluída ou ainda, se o saldo for alterado tais justificativas deverão ser removidas caso contrário, manter as justificativas existentes\.

1. __Outros tratamentos:__

Os tratamentos dos ícones Validar e Justificar, botões e abas existentes na tela Ajustes Manual do Balanço/DRE \(Bloco K\) deverão ser mantidos conforme Tela Ajuste  Manual do Bloco K\.doc\.

MFS\-12636

RNI10\.02

__Parâmetro “Manter Ajustes Manuais Realizados” selecionado – Tela Lucro Real \- Anexos__

Os anexos são vinculados às linhas da tabela dinâmica, independentemente da seleção do parâmetro “Manter Ajustes Manuais Realizados” se houver anexo, o mesmo será mantido\.

MFS\-12636

RNI10\.03

__Parâmetro “Manter Ajustes Manuais Realizados” selecionado – Tela Lançamentos da Parte A \(M300, M350\)__

As regras definidas abaixo podem ter dependência com as regras existentes na tela de lançamentos da parte A\. No caso de dúvidas, verificar o Tela Lancamentos Parte A\.doc 

__Tipo de Relacionamento “Com Conta Contábil”\- __

- Foi realizada uma nova "Importação de Saldos" com o parâmetro "Manter os Ajustes Manuais Realizados" selecionado e o tipo de relacionamento é “Com Conta Contábil”, porém todas as contas contábeis foram removidas da associação da linha da tabela dinâmica e havia lançamentos ou ajustes associados\. Não recuperaremos a conta contábil e nem os vínculos existentes, pois não há conta pai\. Será exibida a DW00138 e a DW00139 e o status dessa abertura da apuração deverá ser “Importação de Saldos Realizada”\.
- Se apenas algumas contas contábeis foram desassociadas da linha da tabela dinâmica e o Status da conta contábil é igual a “Considerar Movimento” e não havia lançamentos ou ajustes para cada conta contábil, o status dessa abertura da apuração deverá ser “Importação de Saldos Realizada” e será exibida a DW00138\.
- Se algumas contas contábeis foram desassociadas e o Status da conta contábil é igual a “Considerar Movimento” e não havia lançamentos ou ajustes para cada conta contábil, o status dessa abertura da apuração deverá ser “Importação de Saldos Realizada”\.
- Se as mesmas contas contábeis com os respectivos saldos foram encontradas na nova importação de saldos e o Status da conta contábil é igual a “Considerar Movimento” o saldo será recalculado, mas o conteúdo do campo “Valor” tem que ser o mesmo conteúdo que o campo “Valor” antes da nova importação dos saldos\.
- Se as mesmas contas contábeis foram encontradas e o Status da conta contábil é igual a “Considerar Movimento” ou houve contas contábeis incluídas ou removidas na nova importação de saldos, porém os saldos de uma ou mais contas são diferente, o conteúdo do campo do “Valor” não deverá ser recuperado e sim recalculado\.
- Se as contas contábeis existirem na associação, porém não houver mais saldo nesta conta no período da importação de saldos, exibir a mensagem DW00143, desprezando este valor para a composição do valor da linha da tabela dinâmica\.
- Se o saldo da conta contábil for alterado, considerar o novo valor para a composição do valor da linha e exibir a mensagem DW00142\.
- Para cada conta contábil recuperada, recuperar o conteúdo do campo Status informado apuração anterior\.
- Para este tipo de relacionamento, quando for realizada uma nova "Importação de Saldos" com o parâmetro "Manter os Ajustes Manuais Realizados" e o Status da conta contábil é igual a “Considerar Movimento” o campo “Vlr\. a Utilizar” será recalculado automaticamente com base nos conteúdos recuperados dos campos “Vlr\. Parcial” e/ou “Vlr\. dos Ajustes”, se houver\. O conteúdo do campo “Vlr\. a Utilizar”, será replicado no campo “Lançamentos/Ajustes” e exibido no campo “Valor”\. O conteúdo do campo “Valor” corresponderá a somatória da coluna “Lançamentos/Ajustes” de todas as contas contábeis associadas à linha da tabela dinâmica\. Se a conta contábil deste ajuste está parametrizada na tela de recuperação de valores, aplicar primeiro as regra referente a parametrização, conforme RNI04\.04, tópico ‘__Atribuição dos saldos para apuração para as linhas dos registros M300A, M300B, M300C e/ou M350A, M350B, M350C’, __restaurando o valor informado no ajuste \(“Lançamentos/Ajustes” e seu indicador\), considerando o recalculo do campo Valor, aplicando a regra que é feita natela\.
-  Se não houver ajustes vinculados a conta contábil, o conteúdo do campo “Valor” corresponderá ao resultado da importação dos saldos \(processo existente hoje\)\.
- Foi realizada uma nova "Importação de Saldos", com o parâmetro "Manter os Ajustes Manuais Realizados" selecionado e o “Status” recuperado da Conta Contábil é “Desconsiderar Movimento”\. Os lançamentos contábeis, se houver não deverão ser recuperados e os campos Vlr\. Períodos Anteriores / Ind\. do Vlr\. Períodos Anteriores e Vlr\. dos Ajustes/Ind\. do Vlr\. dos Ajustes deverão ser recuperados, se houver conteúdo e o campo Vlr\. a Utilizar, será atualizado automaticamente\. Na coluna Saldo e Ind\. do Saldo deverá ser exibido os valores da conta\. O conteúdo do campo “Vlr\. a Utilizar”, será replicado no campo “Lançamentos/Ajustes” e exibido no campo “Valor”\. O conteúdo do campo “Valor” corresponderá a somatória da coluna “Lançamentos/Ajustes” de todas as contas contábeis associadas à linha da tabela dinâmica\. Se a conta contábil está parametrizada na tela de recuperação de valores, aplicar primeiro as regras referente a parametrização, conforme RNI04\.04, tópico ‘__Atribuição dos saldos para apuração para as linhas dos registros M300A, M300B, M300C e/ou M350A, M350B, M350C’, __restaurando o valor informado no ajuste \(“Lançamentos/Ajustes” e seu indicador\), considerando o recalculo do campo Valor, aplicando a regra que é feita na tela\.

__Tipo de Relacionamento “Com Conta da Parte B e Com Conta Contábil”__

- Foi realizada uma nova "Importação de Saldos" com o parâmetro "Manter os Ajustes Manuais Realizados" selecionado e o tipo de relacionamento é “Com Conta da Parte B e Com Conta Contábil”, porém todas as contas contábeis foram desassociadas da linha da tabela dinâmica\. O tipo de relacionamento será alterado para “Com Conta da Parte B”, os lançamentos contábeis se houver e o conteúdo do campo “Exibição do Conteúdo do Campo Valor” serão apagados e será exibida a DW00138 e a DW00139 e o status dessa abertura da apuração deverá ser “Importação de Saldos Realizada”\.
- Se apenas algumas contas contábeis foram desassociadas exibir a DW00138 e o tipo de relacionamento não será alterado devendo ser mantido o tipo de relacionamento Com Conta da Parte B e Com Conta Contábil o conteúdo do campo “Valor” deverá ser recalculado de acordo com o conteúdo do campo “Exibição do Conteúdo do Campo Valor” e o status dessa abertura da apuração deverá ser “Importação de Saldos Realizada”\.
- Se as mesmas contas contábeis foram encontradas e o Status da conta contábil é igual a “Considerar Movimento” ou houve contas contábeis incluídas na nova importação de saldos, porém os saldos de uma ou mais contas são diferente, o conteúdo do campo do “Valor” deverá ser recalculado e o conteúdo do campo “Exibição do Conteúdo do Campo Valor” deverá ser recuperado\.
- Para cada conta contábil recuperada, recuperar o conteúdo do campo Status informado apuração anterior\.
- Para este tipo de relacionamento, quando for realizada uma nova "Importação de Saldos" com o parâmetro "Manter os Ajustes Manuais Realizados" e o Status da conta contábil é igual a “Considerar Movimento” selecionado, os ajustes recuperados nos campos “Vlr\. Parcial” e/ou “Vlr\. dos Ajustes” , para a conta contábil, se houver, serão automaticamente recalculados e o valor será atribuído ao campo “Vlr\. a Utilizar”, replicados no campo “Lançamentos/Ajustes” e no campo “Valor”, deverá ser recuperado o  conteúdo existente antes da nova importação dos saldos  e o  parâmetro “Exibição do conteúdo do campo Valor” deverá ser recuperado\. 
- Se não houver conta contábil, não haverá o recalculo do campo “Vlr\. a Utilizar” e “Lançamentos/Ajustes”\.

Atualizar o Valor do Lançamento da Parte A: o valor do somatório de todos os ajustes da parte B \(Considerando que os valores a Crédito devem subtrair os valores a Débito e o sinal de acordo com a a RNG00047 – Recalculo do Valor\. 

__Tipo de Relacionamento “Sem Relacionamento” __

- Foi realizada uma nova "Importação de Saldos" com o parâmetro "Manter os Ajustes Manuais Realizados selecionado" e o tipo de relacionamento é “Sem Relacionamento” com ou sem processos judiciais/administrativo vinculado\. Recuperaremos o conteúdo do campo “Valor” \(inserido manualmente\) e se houver processos vinculados, se tratando do tipo de relacionamento “Com Conta da Parte B” este também será recuperado e o status dessa abertura da apuração deverá ser “Importação de Saldos Realizada”\. 
- Se na primeira importação dos saldos a linha da tabela dinâmica possuía o tipo de relacionamento igual “Sem Relacionamento” e na nova importação dos saldos for identificada a associação de uma ou mais conta contábil para a mesma linha da tabela dinâmica, o tipo de relacionamento que antes era “Sem Relacionamento”, será alterado para “Com Conta Contábil” o campo “Valor” será calculado com base no saldo da conta contábil e será exibida a DW00139\.

Se na primeira importação dos saldos a linha da tabela dinâmica possuía o tipo de relacionamento igual “Com Conta da Parte B” e se na nova importação dos saldos ainda for identificada a associação com a conta da parte B e também identificada a associação de uma ou mais conta contábil para a linha da tabela dinâmica, o tipo de relacionamento que antes era “Com Conta da Parte B”, será alterado para “Com Conta da Parte B e Com Conta Contábil”, será exibida a DW00139 e o conteúdo do campo “Valor” existente antes da nova importação dos saldos será mantido\.

__Tipo de Relacionamento “Com Conta da Parte B”__

- Foi realizada uma nova "Importação de Saldos" com o parâmetro "Manter os Ajustes Manuais Realizados selecionado" e o tipo de relacionamento é “Com Conta da Parte B” o status dessa abertura da apuração deverá ser “Importação de Saldos Realizada”\. 

O Conteúdo do campo Valor deve ser o valor do somatório de todos os ajustes da parte B \(Considerando que os valores a Crédito devem subtrair os valores a Débito e o sinal de acordo com a RNG00047 – Recalculo do Valor\)\. 

__Tipo de Relacionamento “Com Conta Contábil” e “Associação Automática de Todos os Lançamentos Contábeis \(M312 M362\)”:__

Foi realizada uma nova "Importação de Saldos", com o parâmetro "Manter os Ajustes Manuais Realizados" selecionado, havia sido executada a rotina de “Associação Automática de Todos os Lançamentos Contábeis \(M312 M362\)”, o tipo de relacionamento “Com Conta Contábil”  o Status da conta contábil é igual a “Considerar Movimento”  e o saldo da conta é igual ao saldo inserido manualmente pelo usuário\. Recuperaremos os saldos, os valores dos ajustes e processos inseridos manualmente antes da nova importação dos saldos\. Os valores dos ajustes recuperados nas abas “Lançamentos Contábeis e/ou Valores dos Lançamentos Associados ao Mês/Trimestre” para a conta contábil, se houver, recalcularão automaticamente o campo “Vlr\. a Utilizar” com base nos valores recuperados dos campos “Vlr\. Total” e/ou “Vlr\. Parcial” e/ou “Vlr\. dos Ajustes”\. O valor recalculado no campo “Vlr\. a Utilizar” será replicado no campo “Lançamentos/Ajustes” e exibidos no campo “Valor”\. O conteúdo do campo “Valor” corresponderá a somatória da coluna “Lançamentos/Ajustes” de todas as contas contábeis associadas à linha da tabela dinâmica\.

- Foi realizada uma nova "Importação de Saldos", com o parâmetro "Manter os Ajustes Manuais Realizados", selecionado, havia sido executada a rotina de “Associação Automática de Todos os Lançamentos Contábeis \(M312 M362\)”, o tipo de relacionamento “Com Conta Contábil” e a conta contábil possui o saldo diferente da importação anterior\. Recuperaremos os valores ajustes manuais realizados nas abas “Lançamentos Contábeis e/ou Valores dos Lançamentos Associados ao Mês/Trimestre” para a conta contábil, se houver, recalcularão automaticamente o campo “Vlr\. a Utilizar” com base nos valores recuperados dos campos “Vlr\. Total” e/ou “Vlr\. Parcial” e/ou “Vlr\. dos Ajustes”\. O valor recalculado no campo “Vlr\. a Utilizar” será replicado no campo “Lançamentos/Ajustes” e exibidos no campo “Valor”\. O conteúdo do campo “Valor” corresponderá a somatória da coluna “Lançamentos/Ajustes” de todas as contas contábeis associadas à linha da tabela dinâmica\. Os campos de cálculo automático funcionarão de acordo com os tratamentos da tela\. Será exibida a TR00830 e o status dessa abertura da apuração deverá ser “Importação de Saldos Realizada”\. Se a conta contábil deste ajuste está parametrizada na tela de recuperação de valores, aplicar primeiro as regra referente a parametrização, conforme RNI04, tópico ‘__Atribuição dos campos Lançamentos/Ajustes e Saldo para as contas contábeis associadas aos registros M300A, M300B, M300C e/ou M350A, M350B, M350C’, __restaurando o valor informado no ajuste \(“Lançamentos/Ajustes” e seu indicador\), considerando o recalculo do campo Valor, aplicando a regra RN18 da tela\.
- Foi realizada uma nova "Importação de Saldos", com o parâmetro "Manter os Ajustes Manuais Realizados", selecionado, havia sido executada a rotina de “Associação Automática de Todos os Lançamentos Contábeis \(M312 M362\)”, o tipo de relacionamento “Com Conta Contábil” e todas as contas contábeis foram desassociadas da linha da tabela dinâmica\. Será exibida a TR00826, e a conta contábil e os ajustes se houverem serão apagados\.
- Se apenas algumas contas contábeis com o Status da conta contábil é igual a “Considerar Movimento” foram desassociadas da linha da tabela dinâmica, os valores dos ajustes manuais realizados nas abas “Lançamentos Contábeis e/ou Valores dos Lançamentos Associados ao Mês/Trimestre” para a conta contábil, se houver, serão automaticamente atualizados no campo “Vlr\. a Utilizar”, replicados no campo “Lançamentos/Ajustes” e exibidos no campo “Valor”\. O conteúdo do campo “Valor” corresponderá a somatória da coluna “Lançamentos/Ajustes” de todas as contas contábeis associadas à linha da tabela dinâmica\. Exibir a TR00826 para cada conta contábil e o status dessa abertura da apuração deverá ser “Importação de Saldos Realizada”\.
- Foi realizada uma nova "Importação de Saldos", com o parâmetro "Manter os Ajustes Manuais Realizados" selecionado, havia sido executada a rotina de “Associação Automática de Todos os Lançamentos Contábeis \(M312 M362\)”, o tipo de relacionamento “Com Conta Contábil” e há uma conta contábil com Status igual a “Considerar Movimento” nova\. Serão aplicados os tratamentos existentes na tela conforme MTZ\_Tela\_Lancamentos\_Parte\_A\.doc, pois se trata do fluxo existente\.
- Foi realizada uma nova "Importação de Saldos", com o parâmetro "Manter os Ajustes Manuais Realizados" selecionado, havia sido executada a rotina de “Associação Automática de Todos os Lançamentos Contábeis \(M312 M362\)”, o tipo de relacionamento “Com Conta da Parte B e Com Conta Contábil” e todas as contas contábeis foram desassociadas\. Apagaremos os valores dos ajustes manuais vinculados à conta contábil, recuperaremos o conteúdo do campo “Valor” \(inserido manualmente ou calculado por meio da conta contábil associada\) anteriormente existente antes da nova importação dos saldos, o tipo de relacionamento será alterado para “Com Conta da Parte B” e será exibida a TR00826 e a TR00828 e o status dessa abertura da apuração deverá ser “Importação de Saldos Realizada”\.
- Se apenas algumas contas contábeis com o Status igual a “Considerar Movimento” foram desassociadas, os valores dos ajustes recuperados para a conta contábil, se houver, serão automaticamente atualizados no campo “Vlr\. a Utilizar”, replicados no campo “Lançamentos/Ajustes” e no campo “Valor”, deverá ser recuperado o  conteúdo existente antes da nova importação dos saldos\.
- Se não houver conta contábil, não haverá atualização nos campos “Vlr\. a Utilizar” e “Lançamentos/Ajustes” e será recuperado o conteúdo campo “Valor”\.

Foi realizada uma nova "Importação de Saldos", com o parâmetro "Manter os Ajustes Manuais Realizados" selecionado e havia sido executada a rotina de “Associação Automática de Todos os Lançamentos Contábeis \(M312 M362\)”, o tipo de relacionamento “Com Conta Contábil” e o “Status”  recuperado da Conta Contábil é “Desconsiderar Movimento”\. Os lançamentos contábeis não deverão ser recuperados e os campos Vlr\. Períodos Anteriores / Ind\. do Vlr\. Períodos Anteriores e Vlr\. dos Ajustes/Ind\. do Vlr\. dos Ajustes deverão ser recuperados se houver valor e o campo Vlr\. a Utilizar, será atualizado automaticamente\. Na coluna Saldo e Ind\. do Saldo deverá ser exibido os valores da conta\. O conteúdo do campo “Vlr\. a Utilizar”, será replicado no campo “Lançamentos/Ajustes” e exibido no campo “Valor”\. O conteúdo do campo “Valor” corresponderá a somatória da coluna “Lançamentos/Ajustes” de todas as contas contábeis associadas à linha da tabela dinâmica\. Se a conta contábil estiver parametrizada na tela de recuperação de valores, aplicar primeiro as regra referente a parametrização, conforme RNI04, tópico ‘__Atribuição dos campos Lançamentos/Ajustes e Saldo para as contas contábeis associadas aos registros M300A, M300B, M300C e/ou M350A, M350B, M350C’, __restaurando o valor informado no ajuste \(“Lançamentos/Ajustes” e seu indicador\), considerando o recalculo do campo Valor , aplicando a regra RN18 da tela\.

__Recuperação do campo Histórico \(Tela \- Lançamentos da Parte A\) ou Justificativa \(Aba Valores dos Lançamentos Associados ao Mês/Trimestre\)__

- Toda vez que houver conteúdo nos campos “Histórico” na tela Lançamentos da Parte A e/ou “Justificativa” na Aba – Valores dos Lançamentos Associados ao Mês/Trimestre e for efetuada uma nova importação dos saldos com o parâmetro “Manter Ajustes Manuais Realizados” selecionado, os mesmos conteúdos serão recuperados com a informação contida antes da nova importação dos saldos\.

MFS\-15014

MFS\-15958

# <a id="_Toc503179371"></a><a id="_Toc512254968"></a>REGRAS CÓPIA DE AJUSTES MANUAIS

Agrupamento de regras utilizadas para o processo para a cópia dos ajustes manuais que ocorrerá após a execução do processo de importação dos saldos conforme tópico [REGRAS – IMPORTAÇÃO DOS SALDOS](#regrasimportacao) e antes do processo de cálculo conforme tópico [REGRAS – CÁLCULO\.](#regrascalculo)

 

__CÓD__

__DESCRIÇÃO__

__MFS__

RNCP01

__Cópia dos Ajustes Manuais para os registros N620 e/ou N660__

A execução deste processo não altera o status da abertura da apuração\.

Este processo é executado para o último período de apuração, sendo que a aba anual dos registros constará os dados do último período processado\. Caso seja solicitado o processamento para um período da apuração que não é o último, exibir, a TR01191\.

__Copiar Ajustes Manuais do Registro N620: __Verificar se para os Estabelecimentos Matriz/SCPs e Abertura das Apurações selecionadas há inserção de forma manual e/ou via importação \(upload\) no campo “Valor” na tela/tabela “Entrada Manual de Valores” para o Registro N620\.

Se houver, copiar os valores de entrada manual \(Valor e Justificativa\) do registro N620 para os Registros N630, de acordo com a Qualificação da Pessoa Jurídica:

- Registro N630A quando PJ em Geral; 
- Registro N630B quando PJ Componente do Sistema Financeiro;
- Registro N630C quando Sociedades Seguradoras;

Realizar cópia dos valores somente para as linhas equivalentes do Registro N620 para os Registros do N630, e somente das linhas do tipo “E” e “CA”, conforme documento Compara Dinâmica\.xls \(Aba Cópia Registro N620/N630\)\.

Se Apuração = Anual: 

A cópia deve ser realizada também para a aba Anual A00 do registro N630\.

Caso existam linhas que não possuírem equivalência entre os registros não devem ser alteradas\.

Ao final da cópia exibir a mensagem TR01171\.

Caso existam linhas que possuam conta específica vinculada, não efetuar a cópia e exibir a TR01088\.

Caso existam valores nos Registro N630 \(A, B ou C\) provenientes tanto de cálculo de processamento quanto de entrada manual para a linha que receberá o valor do Registro N620, este será sobreposto\. 

__Copiar Ajustes Manuais do Registro N660: __Verificar se para os Estabelecimentos Matriz/SCPs e Abertura das Apurações selecionadas há inserção de forma manual e/ou via importação \(upload\) no campo “Valor” na tela/tabela “Entrada Manual de Valores” para o Registro N660\.

Se houver, copiar os valores de entrada manual do registro N660 \(Valor e Justificativa\) para as linhas equivalentes do Registro N670 e somente das linhas do tipo “E” e “CA”, conforme documento Compara Dinâmica\.xls \(Aba Cópia Registro N660/N670\)\. 

Se Apuração = Anual: 

A cópia deve ser realizada também para a aba Anual A00 do registro N670\.

Caso existam linhas que não possuírem equivalência entre os registros não devem ser alteradas\.

Ao final da cópia exibir a mensagem TR01171\.

Caso existam linhas que possuam conta específica vinculada, não efetuar a cópia e exibir a TR01088\.

Caso existam valores nos Registro N670 para a linha que receberá o valor do Registro N660, provenientes tanto de cálculo de processamento quanto de entrada manual, este será sobreposto\. 

# <a id="_Toc512254969"></a><a id="regrascalculo"></a>REGRAS – CÁLCULO 

__Considerações gerais:__

Durante o processo de cálculo, executar as orientações abaixo:

O sistema deve executar o processo cálculo após a execução do processo de “Transcrição dos Valores Empresa para Referenciais Fisco”, seguindo as regras abaixo: 

\. Com base na parametrização da tela de Processamento em Lote e para as apurações selecionadas\.

- Aplicar a RNG00013
- Os registros e códigos dos registros que possuem fórmulas deverão ser processados de acordo com as RNIs, RNCs e de acordo com REGRAS – PROCESSAMENTO DOS REGISTROS\.

__CÓD__

###### __DESCRIÇÃO__

__MFS__

<a id="RNC01"></a>RNC01

Será criado um processo para a consolidação dos saldos e execução das fórmulas que ocorrerá após a execução do processo de importação dos saldos conforme tópico REGRAS – IMPORTAÇÃO DOS SALDOS com base nas fórmulas existentes nos registros que utilizam tabelas dinâmicas conforme coluna “Fórmula” do documento \[Compara Dinamicas\.xls\] 

MFS\-12620

RNC02

Validações que devem ser realizadas:

- Verificar na apuração anterior:  RNG00049 \- Sem escolha do tipo de receita\.

\- A Informação do ECF deve estar com a versão compatível do layout da obrigação, \(conforme RNG00003\), se não aplicar conforme abaixo:

- 
	- Se a versão não for compatível com a data da ECF \(período de vigência\), exibir a DW00018

Exemplo: Data Inicial 01/01/2014 \(independente se houver situação especial ou não\) com versão 2\.00, ou

- 
	- Se a versão for compatível com a data da ECF \(período de vigência\), mas a versão não for compatível com a ocorrência de situação especial, exibir a DW00019\.

Exemplo: Data Inicial 01/01/2015 \(com situação especial\) com versão 2\.00, ou 

- 
	- Se a versão for compatível com a data da ECF \(período de vigência\), mas a versão não é compatível sem a ocorrência de situação especial, exibir a DW00020\.  
Exemplo: Data Inicial 01/01/2015 \(sem situação especial\) com versão 1\.00\.

MFS\-12620

MFS\-13997

MFS\-16531

MFS\-16928

RNC02\.01

Para a atribuição do saldo para cada linha da tabela dinâmica que possuir fórmula, atender os seguintes critérios:

- Deverá ser utilizado como apoio a planilha \[Compara Dinamicas\.xls\]
- Deverá ser respeitada a hierarquia entre os registros, pois algumas fórmulas deverão ser executadas com base nas fórmulas executadas em registros anteriores que também poderão ter como origem o saldo de uma conta do Plano Referencial ou o resultado de uma linha da tabela dinâmica do próprio registro\. Tal hierarquia pode ser identificada com base na planilha \[Compara Dinamicas\.xls\] pelas colunas “Registro”, “Ordem”, “Linha do ECF” e “Fórmula”\.
- Deverá ser respeitado o agrupamento dos saldos de acordo com o registro conforme coluna “Registro”\. Para o registro N630, M300 ou M350, conforme RNG00005 \- Associações compatíveis com o campo ‘Qualificação da Pessoa Jurídica’ da tela Informação ECF:
- Para as linhas da tabela dinâmica possuem a coluna “Tipo” = CNA e/ou “Tipo” = CA, aplicar a RNG00014\. Se não apresentar erro, executar as fórmulas conforme coluna “Fórmula” da planilha\.
- Para as linhas da tabela dinâmica possuem a coluna “Tipo” diferente de CNA ou “Tipo” = R atribuir o valor saldo encontrado conforme RNI04\. Exceção: Após a execução da rotina de “Importação do Saldo” as linhas que possuem o campo “Tipo” igual a “CA” e o saldo da conta for zero, aplicar a fórmula existente para a linha a ser calculada\.

MFS\-12620

RNC03

__Recuperação dos saldos com base na entrada manual de valores__

- De acordo com as aberturas da apuração informados na tela de Processamento em Lote, identificar as empresas selecionadas para o processamento e recuperar os valores de todos os estabelecimentos desta empresa enquanto houver correspondência entre a abertura da apuração selecionada na tela de processamento em lote e a abertura da apuração que possuir valores na tabela de entrada manual de valores\. Se para uma mesma linha da tabela dinâmica valores de entrada manual e valor corresponde a associação com base nas contas contábeis, deverá prevalecer o valor informado na entrada manual\.
- Deverá ser considerado e recuperado como saldo de cada linha das tabelas dinâmicas, o valor informado manualmente em cada linha da tabela dinâmica na tela Entrada Manual de Valores\.

MFS\-12620

MFS\-13997

RNC04

__Bloco K – Reprocessamento dos Registros dos Blocos __

- Durante o Processamento em Lote, após a importação do saldo se houver informações nos campos referente a [RNI07 – Pré – Processamento do Bloco K \(Rateio, Demais Ajustes e Lançamento de Encerramento\),](#Processamento_BlocoK) atualizar os saldos das contas contábeis e os saldos das contas referenciais \(contas sintéticas e analíticas\) dos registros citados abaixo:
	- 
		- Registros L100 e L300
		- Registro P100 e P150
		- Registro U100 e U150
		- Todos os registros gerados a partir de fórmulas cuja origem seja resultado de linhas do bloco L serão impactados\.

MFS\-12620

MFS\-13995

RNC05

__Refazer Apuração Anual \(A00\)__

- Para os registros que serão processados conforme RNP \- REGRAS – PROCESSAMENTO DOS REGISTROS \(com exceção dos registros de abertura, identificação e encerramento\) dos blocos L, M, N, U e registros K155 e K355, deverá ser refeito durante a rotina de execução do cálculo\.
- Para as linhas correspondente aos registros N620, N660 não deverá gerado A00 e para a linha 2 dos registros N500 e N650 deverá ser gerado zero\.

MFS\-13997

MFS\-16531

RNC06

__Arredondamento__

Quando o Processamento de Cálculo da Fórmulas efetuar um cálculo que resulte em mais casas decimais do que o definido para o campo conforme exemplo:

Quando for maior ou igual 0,000 e menor que 0,005 arredondar para baixo, e quando for entre 0,005 e 0,009 arredondar para cima\.

MFS\-12620

RNC07

__Recuperação dos saldos para associações com as Tabelas Dinâmicas – Bloco M__

Para a atribuição do saldo para cada linha da tabela dinâmica do Bloco M atender os seguintes critérios:

- Deverá ser utilizado como apoio a planilha \[Tabelas\_Dinamicas\.xls\]
- Deverá ser respeitada a hierarquia entre os registros e os códigos dos registros, pois pode haver dependência entre as linhas de um mesmo registro\. Tal hierarquia pode ser identificada com base na planilha \[Tabelas\_Dinamicas\.xls\] pelas colunas “Registro”, “Ordem”, “Linha do ECF” e “Fórmula”\.
- Deverá ser utilizado como saldo a ser atribuído ao código do registro, o conteúdo do campo “Valor” da tela Lançamentos da Parte A de acordo com o conteúdo do campo “Tipo de Relacionamento“\.
	- 
		1. Recuperar e utilizar como saldo o conteúdo no campo “Valor” da tela “Lançamentos da Parte A” quando no campo “Tipo de Relacionamento” for 1 – Com Conta da Parte B ou 2 – Com Conta Contábil ou 3 – Com conta da Parte B e Conta Contábil ou 4 – Sem Relacionamento\.
- Deverá ser respeitado o agrupamento dos saldos de acordo com o registro conforme coluna “Registro”\. Para os registros M300 e M350 verificar os critérios abaixo:
	- 
		1. Se na tela Informações ECF campo Qualificação da Pessoa Jurídica = “PJ em Geral”, considerar apenas as linhas da tabela dinâmica cuja coluna Registro = M300A ou M350A\.
		2. Se na tela Informações ECF campo Qualificação da Pessoa Jurídica = “PJ Componente do Sistema Financeiro”, considerar apenas as linhas da tabela dinâmica cujo campo registro = M300B ou M350B\.
		3. Se na tela Informações ECF campo Qualificação da Pessoa Jurídica = “Sociedades Seguradoras, de Capitalização ou Entidade Aberta de Previdência Complementar”, considerar apenas as linhas da tabela dinâmica cujo campo registro = M300C ou M350C\.
- Para a atribuição dos saldos, deverá ser respeitada a sequência contida na coluna “Linha do ECF”\.

Durante o processamento de Cálculo, recuperar e aplicar o conteúdo do campo “Histórico Padrão do Lançamento da Parte A”, cadastrado na tela de “Informações ECF” \(aba LALUR e LACS\), no campo “Histórico” das linhas que possuam valores de saldo diferentes de zero e que sejam do tipo CA \(Cálculo Alterável\) que não tenham sido ajustadas manualmente,nas linhas do tipo CNA \(Cálculo Não Alterável\) dos registros M300/M350, nas linhas do tipo E \(editável\) 173, 202 e 141 dos registros M300A, M300B e M300C respectivamente e nas linhas 348, 202 e 141 dos Registros M350A, M350B e M350C respectivamente\. Para o preenchimento das linhas 9 ou 7 do M300 e da linha de exclusão informada na no campo Cód\. do Registro na tela de “Informações ECF” \(aba LALUR e LACS\) o histórico padrão informado, deverá ser substituído pelo histórico definido na RNC08\.

MFS\-14779

RNC08

__Refazer o calculo do M500:__

Efetuar o recalculo do registro M500 \(conforme RNG00044 \- Cálculo do Registro M500\), que será apresentado nas telas de Ajustes da Parte B e Demonstrações de Resultado do Bloco M\.

Atenção: Este registro é apenas informativo para o cliente, o produto ECF DW não gera estes dados na geração do meio magnético, pois o mesmo é gerado pelo PVA\.

MFS\-15678

RNC09

__Criar/Refazer o registro M410:__

Criar ou atualizar o registro M410 \(conforme RNG00045 – Criação dos registros M410\), que será apresentado nas telas de Ajustes da Parte B e Demonstrações de Resultado do Bloco M\.

MFS\-15678

RNC10

__Criar/Refazer o registro de origem de contrapartida do lançamento da parte B:__

Criar ou atualizar o registro de origem de contrapartida \(conforme RNG00046 – Criação do registro de origem Contrapartida\), que será apresentado nas telas de Lançamentos da Parte B \(M410\) e Demonstrações de Resultado do Bloco M\.

MFS\-15678

RNC11

__Manter valor zero em algumas linhas dos registros N620 e N660, quando tipo de receita = Receita Bruta__

- Aplicar RNG00048 – Registros N620 e N660

MFS\-16531

RNC12

__N620, N660 \- Comparativo entre Receita Bruta ou __<a id="OLE_LINK21"></a><a id="OLE_LINK22"></a><a id="OLE_LINK23"></a><a id="OLE_LINK24"></a>__Balanço de Suspensão/Redução__

Objetivo: Gerar o valor do IRPJ e CSLL com base em na Receita Bruta e Balanço de Suspensão/Redução quando na Tela Abertura da Apuração, o campo Tipo de Receita = Comparativo

- O processamento dos registros N620 e N660 será realizado na visão de Receita Bruta e visão Balanço de Suspensão/Redução\. 
- O comparativo será realizado com base no resultado das linhas 26 do registro N620 para o tributo IRPJ e linha 18 do registro N660 <a id="OLE_LINK10"></a><a id="OLE_LINK19"></a><a id="OLE_LINK20"></a>para o tributo CSLL nas duas visões para apurações correspondentes ao Lucro Real
- Na tela Comparativo entre Receita e Balanço de Suspensão/Redução, será possível visualizar o resultado das linhas 26 – N620 e 18 – N660 nas duas visões permitindo a seleção do valor do imposto\.
- Se o campo “Considerar automaticamente o menor valor de imposto no comparativo” da tela de Abertura da Apuração estiver selecionado, identificar qual tipo de receita possui o menor valor e exibir a seleção permitindo a edição enquanto o status da abertura da apuração posterior for diferente de “Cálculo Realizado” e o status da abertura do período for igual a “Cálculo Realizado”\.
- Se o valor do imposto para a Receita Bruta e Balanço de Suspensão/Redução forem iguais não será identificado o menor valor e o usuário efetuará a escolha na tela "Comparativo entre Receita Bruta X Balanço de Suspensão/Redução"\.

__N620 \- Cálculo da Linha 20 do Registro __

Para cálculo da linha 20 considerar sempre os valores existentes na linha 20\.1 dos meses anteriores de acordo com o período indicado na fórmula da tabela dinâmica \(A01 até o período anterior ao período atual que está sendo calculado\), independente do tipo de receita ser por Balanço ou Suspensão ou Receita Bruta\.

Exemplo:

Janeiro – Balanço ou Suspensão: 

Linha 20\.1 – Imposto de Renda devido no mês – 100,00

Fevereiro – Receita Bruta

Linha 20\.1 – Imposto de Renda devido no mês – 150,00

Março  \- Balanço ou Suspensão

Linha 20 – \(\-\) Imposto de Renda devido em meses anteriores = 250,00

MFS\-16928

RNC13

__N615 \- Geração da base de cálculo após a finalização do Processamento em Lote__

Se o parâmetro ‘FINOR/FINAM/FUNRES ‘ da Tela Informações ECF estiver marcado e pelo uma das demais condições da regra \(RNG00054 – Incentivos Fiscais\) não forem atendidas, exibir a mensagem DW000197\. Caso todas as condições da regra \(RNG00054 – Incentivos Fiscais\) forem atendidas, calcular a base de cálculo:

1. O campo Base de Cálculo existente na tela “Incentivos Fiscais” deverá ser preenchido com o resultado da expressão abaixo:

Base de Cálculo = A \- \(B \+ C \+ D \+ E \+ F \+ G \+ H \+ I \+ J \+ L \+ M\+ N \+ O \+ P\)

Considerar as informações abaixo do registro N630:

__Código__

__Linha__

__A__

N630/3

N630/2

__B__

N630/6

N630/4

__C__

N630/7

N630/5

__D__

N630/8

N630/6

__E__

N630/9

N630/7

__F__

N630/10

N630/8

__G__

N630/11

N630/9

__H__

N630/12

N630/10

__I__

N630/13

N630/11

__J__

N630/14

N630/12

__L__

N630/15

N630/13

__M__

N630/16

N630/14

__N__

N630/18

N630/16

__O__

N630/19

N630/17

__P__

N630/27

N630/25

Se o estabelecimento ou scp processado possuir as condições de geração do registro N610 conforme RNP11, este campo deverá ser atualizado com os valores recuperados de cada linha citada acima mais as linhas que compõem o resultado da letra __Z__ aplicando seguinte expressão: 

Base de Cálculo = A \- \(__Z__ \+ B \+ C \+ D \+ E \+ F \+ G \+ H \+ I \+ J \+ L \+ M \+ N \+ O \+ P\)

__Z__ = \[Código N610/7 \+ N610/12  \+ N610/17 \+ \(N610/47 x 75%\) \+ \(N610/52 x 70%\) \+ \(N610/57x 50%\) \+ \(N610/62 x 33,33%\) \+ \(N610/67 x 25%\) \+ \(N610/72 x 12,50%\)\]

Considerar as informações abaixo do registro N610:

__Código__

__Linha__

N610/7

N610/7

N610/12

N610/12

N610/17

N610/17

N610/47

N610/47

N610/52

N610/52

N610/57

N610/57

N610/62

N610/62

N610/67

N610/67

N610/72

N610/72

1. Se há pelo menos valor em um dos códigos citados acima do registro N610, verificar se o código N630/15 está igual a zero, se sim, exibir a mensagem DW00162\.
2. Se o valor correspondente ao resultado da linha A for igual a zero, o valor correspondente as demais linhas correspondentes a expressão não devem ser recuperados e deverá ser exibida a mensagem DW00161\.
3. Após a atualização do campo Base de Cálculo, os demais campos existentes na tela, deverão ser zerados\.
4. Após a realização do cálculo deverá ser exibida a mensagem DW00163\.

MFS\-12623

RNC14

__N670 – Fórmula com PERIODO\_ATUAL\(\)="A00"__

Visto que o Registro N670 é apresentado apenas para A00 e T01\.\.\.T04\.

Quando a fórmula fizer referência a A00 deve\-se interpretar o último período processado de Apuração = Anual\. Visto que o último registro que for processado será copiado para A00\.

MFS\-16531

RNC15

<a id="CompensacaodePrejuizos"></a>__Compensação de Prejuízos de Períodos Anteriores __

O Processamento deve ocorrer após o cálculo das fórmulas dos Registros M300 e M350 e antes do RNC17 Lançamento Final do Período de Prejuízo e Base Negativa\. 

O processamento deve considerar o parâmetro “Criar ajustes mensalmente” indicado no campo “COMPENSAÇÃO DE PREJUÍZOS E DE BASE NEGATIVA DE PERÍODOS ANTERIORES” na tela de Informações ECF, na aba Lalur e Lacs: 

Se o parâmetro estiver selecionado, o processamento deve ocorrer em todos os meses do período de apuração da ECF\.

Caso contrário, o processamento deve ocorrer no último mês do período de apuração\.

Assim, no caso de apuração anual esse lançamento será feito no último mês apurado \(Dezembro, ou o último mês em caso de situação especial\)\. No caso de apuração Trimestral esse lançamento será feito trimestralmente\.

Se Apuração com Forma de Tributação igual a Lucro Real \(tela Abertura da Apuração\) verificar as parametrizações abaixo:

Se na tela Informações ECF campo Qualificação da Pessoa Jurídica igual a “__PJ em Geral__”, considerar apenas o Registro igual a __M300A__ e __M350A__ e atividade __Geral__ ou __Rural__\.

Se na tela Informações ECF campo Qualificação da Pessoa Jurídica igual a “__PJ Componente do Sistema Financeiro__”, considerar apenas o registro igual a __M300B__ e __M350B__ e atividade __Geral__\.

Se na tela Informações ECF campo Qualificação da Pessoa Jurídica igual a “__Sociedades Seguradoras, de Capitalização ou Entidade Aberta de Previdência Complementar__”, considerar apenas o registro igual a __M300C__ e __M350C__ e atividade __Geral__\.

Com base nos parâmetros acima, executar o processamento:

__Atividade Geral:__

__Prejuízo:__

Verificar a existência de ajuste manual na linha: \(M300A linha 173, ou M300B linha 202 ou M300C linha 141\)\. Caso não tenha sido feito ajuste manual, proceder com a verificação:

Verificar na tela de Informações ECF, aba Prejuízo e Base Negativa, se campo Cód\. da Conta da Parte B para LANÇAMENTO DE PREJUÍZO \- INFORMAÇÕES PARA A CRIAÇÃO DO LANÇAMENTO DE PREJUÍZO DO EXERCÍCIO – ATIVIDADE GERAL possui uma conta parametrizada\. Caso contrário, exibir a mensagem a DW00198\.

Se for encontrada Conta da Parte B, verificar se ela possui Saldo Inicial maior que zero e com indicador de Débito, recuperar o valor da linha indicado abaixo e seguir com o cálculo\. Caso contrário exibe a mensagem DW00199\. Se a conta não possuir saldo para o tributo IRPJ, exibir a mensagem DW00200\.

Recuperar o valor da linha: \(M300A linha 169, ou M300B linha 201 ou M300C linha 140\) e considera\-lo o LUCRO REAL ANTES DA COMPENSAÇÃO

Aplicar [RNC16 – Calcular Compensação](#CalcularCompensacao)

Se Valor para COMPENSAÇÃO maior que zero:

Efetuar lançamento na linha: \(M300A linha 173, ou M300B linha 202 ou M300C linha 141\) com o valor da COMPENSAÇÃO da [RNC16 – Calcular Compensação](#CalcularCompensacao)\)\. Caso contrário, exibir a mensagem DW00201\.

\.

__Base Negativa:__

Verificar a existência de ajuste manual na linha: \(M350A linha 173, ou M350B linha 202 ou M350C linha 141\)\. Caso não tenha sido feito ajuste manual, proceder com a verificação:

Verificar na tela de Informações ECF, aba Prejuízo e Base Negativa, se campo Cód\. da Conta da Parte B para LANÇAMENTO DE BASE NEGATIVA \- INFORMAÇÕES PARA A CRIAÇÃO DO LANÇAMENTO DE BASE DE CÁLCULO NEGATIVA DA CSLL – ATIVIDADE GERAL possui uma conta parametrizada\. Caso contrário, exibir a mensagem a DW00198\.

Se for encontrada Conta da Parte B, verificar se ela possui Saldo Inicial maior que zero e com indicador de Débito, recuperar o valor da linha indicado abaixo e seguir com o cálculo\. Caso contrário exibe a mensagem DW00199\. Se a conta não possuir saldo para o tributo CSLL, exibir a mensagem DW00200\.

Recuperar o valor da linha: \(M350A linha 169, ou M350B linha 201 ou M350C linha 140\) e considera\-lo o LUCRO REAL ANTES DA COMPENSAÇÃO

Aplicar [RNC16 – Calcular Compensação](#CalcularCompensacao)

Se Valor para COMPENSAÇÃO maior que zero:

Efetuar lançamento na linha: \(M350A linha 173, ou M350B linha 202 ou M350C linha 141\) com o valor da COMPENSAÇÃO da [RNC16 – Calcular Compensação](#CalcularCompensacao)\)\. Caso contrário, exibir a mensagem DW00201\.

__Atividade Rural:__

__Prejuízo:__

Verificar a existência de ajuste manual na linha: \(M300A linha 348\)\. Caso não tenha sido feito ajuste manual, proceder com a verificação:

Verificar na tela de Informações ECF, aba Prejuízo e Base Negativa, se campo Cód\. da Conta da Parte B para LANÇAMENTO DE PREJUÍZO \- INFORMAÇÕES PARA A CRIAÇÃO DO LANÇAMENTO DE PREJUÍZO DO EXERCÍCIO – ATIVIDADE RURAL possui uma conta parametrizada\. Caso contrário, exibir a mensagem a DW00198\. 

Se for encontrada Conta da Parte B, verificar se ela possui Saldo Inicial maior que zero e com indicador de Débito, recuperar o valor da linha indicado abaixo e seguir com o cálculo\. Caso contrário exibe a mensagem DW00199\. Se a conta não possuir saldo para o tributo IRPJ, exibir a mensagem DW00200\.

Recuperar o valor da linha: M300A linha 343 e considera\-lo o LUCRO REAL ANTES DA COMPENSAÇÃO

Aplicar [RNC16 – Calcular Compensação](#CalcularCompensacao)

Se Valor para COMPENSAÇÃO maior que zero:

Efetuar lançamento na linha: M300A linha 348 com o valor da COMPENSAÇÃO \([RNC16 – Calcular Compensação](#CalcularCompensacao)\)\. Caso contrário, exibir a mensagem DW00201\.

__Base Negativa:__

Verificar a existência de ajuste manual na linha: \(M350A linha 348\)\. Caso não tenha sido feito ajuste manual, proceder com a verificação:

Verificar na tela de Informações ECF, aba Prejuízo e Base Negativa, se campo Cód\. da Conta da Parte B para LANÇAMENTO DE BASE NEGATIVA \- INFORMAÇÕES PARA A CRIAÇÃO DO LANÇAMENTO DE PREJUÍZO DO EXERCÍCIO – ATIVIDADE RURAL possui uma conta parametrizada\. Caso contrário, exibir a mensagem a DW00198\.

Se for encontrada Conta da Parte B, verificar se ela possui Saldo Inicial maior que zero e com indicador de Débito, recuperar o valor da linha indicado abaixo e seguir com o cálculo\. Caso contrário exibe a mensagem DW00199\. Se a conta não possuir saldo para o tributo CSLL, exibir a mensagem DW00200\.

Recuperar o valor da linha: M350A linha 343 e considera\-lo o LUCRO REAL ANTES DA COMPENSAÇÃO

Aplicar [RNC16 – Calcular Compensação](#CalcularCompensacao)

Se Valor para COMPENSAÇÃO maior que zero:

Efetuar lançamento na linha: M350A linha 348 com o valor da COMPENSAÇÃO \([RNC16 – Calcular Compensação](#CalcularCompensacao)\)\. Caso contrário, exibir a mensagem DW00201\.

MFS\- [17491](http://ent.jira.int.thomsonreuters.com/browse/MFS-17491)

RNC16

<a id="CalcularCompensacao"></a>__Calcular Compensação__

__Considerar os seguintes valores:__

1. 30% sobre o LUCRO REAL ANTES DA COMPENSAÇÃO \(30% do M300A/M350A linha 169, M300B/M350B linha 201, M300C/M350C linha 140\) ou 100% em caso de Atividade Rural \(100% do M300A/M350A linha 343\)\.
2. Saldo Inicial da Conta da Parte B
3. __Apenas para “PJ em Geral” M300A e M350A__: Valor da linha: M300A/M350A linha 171 \(Apenas para __Atividade Geral__\) ou M300A/M350A linha 345 \(Apenas para __Atividade Rural__\)\.

Recuperar o menor valor dentre os dois \(ou três para “PJ em Geral”\) e considerar como o valor para COMPENSAÇÃO

Se o valor da COMPENSAÇÃO for maior que __zero:__

Efetuar um lançamento na tela Lançamentos da Parte A \(M300, M350\) para a conta parametrizada no Registro M305 \(IRPJ\) ou Registro M355 \(CSLL\)\.

- 
	- ORIGEM = Preencher o campo com o texto “Parte A”
	- HISTÓRICO = 
		- “Compensação de Prejuízos Fiscais de Períodos Anteriores de Atividade Geral”\. Apenas para Atividade Geral ou 
		- “Compensação de Prejuízos Fiscais de Períodos Anteriores de Atividade Rural”\. Apenas para Atividade Rural
	- DATA LANCTO = <Data Final> informada na tela de Abertura da apuração correspondente ao registro processado\.
	- VALOR = __<Valor para COMPENSAÇÃO>__
	- IND\. DO VALOR = Crédito

__No registro M300 ou M350 atualizar:__

- Histórico do lançamento da parte A: Recuperar o Histórico Padrão do Lançamento da Parte A da tela Informações ECF, aba LALUR e LACS\.
- Tipo de Relacionamento da Tela de Lançamentos da Parte A para “Com conta da Parte B”\.
- A inclusão do ajuste e atualização dos valores, seguindo as mesmas regras \(RNG00047 \- Recalculo do Valor\) da tela Lançamentos da Parte A \(M300, M350\)\. Tela Lancamentos Parte A\.doc

Retornar para a [RNC15](#CompensacaodePrejuizos) o valor de COMPENSAÇÃO\.

MFS\- [17491](http://ent.jira.int.thomsonreuters.com/browse/MFS-17491)

RNC17

__Lançamento Final do Período de Prejuízo e Base Negativa NA PARTE B__

O Processamento deve ocorrer após o cálculo das fórmulas dos Registros M300 e M350 e após o [RNC15 \-  Compensação de Prejuízos de Períodos Anteriores](#CompensacaodePrejuizos)\.

O processamento deve considerar o parâmetro “Criar ajustes mensalmente” indicado no campo “COMPENSAÇÃO DE PREJUÍZOS E DE BASE NEGATIVA DE PERÍODOS ANTERIORES” na tela de Informações ECF, na aba Lalur e Lacs: 

Se o parâmetro estiver selecionado o processamento deve ocorrer em todos os meses do período de apuração\.

Se o parâmetro não estiver selecionado, o processamento deve ocorrer no último mês do período de apuração\. Assim, deve recuperar o Valor Calculado para os Registros da apuração Anual A12 \(Ou último mês em caso de situação especial\) ou Trimestral T1, T2, T3 e T4 com os Códigos conforme tabela abaixo:

__Registro__

__Código__

__Prejuízo__

M300A – Ativ\. Geral

175

M300A – Ativ\. Rural

349

M300B

203

M300C

142

__Base Negativa__

M350A – Ativ Geral

175 

M350A – Ativ\. Rural

349

M350B

203

M350C

142

Se o Valor Recuperado para __Prejuízo__ para um dos registros é menor do que zero:

Se o valor recuperado para umas das linhas \(175, 203 ou 142\) referentes a Atividade Geral for menor que zero:

Verificar na tela de Informações ECF, aba LALUR e LACS, se campo Cód\. da Conta da Parte B para LANÇAMENTO DE PREJUÍZO \- INFORMAÇÕES PARA A CRIAÇÃO DO LANÇAMENTO DE PREJUÍZO DO EXERCÍCIO – ATIVIDADE GERAL possui uma conta parametrizada\. Caso contrário, exibir a mensagem a DW00205\. Se a conta parametrizada não possuir saldo para o tributo IRPJ, exibir a mensagem DW00206\.

Caso o valor da linha recuperada \(175, 203 ou 142\) for maior ou igual a zero, exibir a mensagem DW00207\. 

Se o valor recuperado para umas da linha \(349\) referente a Atividade Rural for menor que zero:

Verificar na tela de Informações ECF, aba LALUR e LACS, se campo Cód\. da Conta da Parte B para LANÇAMENTO DE PREJUÍZO \- INFORMAÇÕES PARA A CRIAÇÃO DO LANÇAMENTO DE PREJUÍZO DO EXERCÍCIO – ATIVIDADE RURAL possui uma conta parametrizada\. Caso contrário, exibir a mensagem a DW00205\. Se a conta parametrizada não possuir saldo para o tributo IRPJ, exibir a mensagem DW00206\.

Caso o valor da linha recuperada \(349\) for maior ou igual a zero, exibir a mensagem DW00207\. 

Efetuar um lançamento na tela Lançamentos da Parte B \(M410\) para a conta parametrizada com os parâmetros abaixo:

- 
	- ORIGEM = Preencher o campo com o texto “Parte B”
	- HISTÓRICO = “Ajuste referente ao\(s\) código\(s\) <Código da Tabela Dinâmica> da tabela dinâmica\. 
	- DATA LANCTO = <Data Final> informada na tela de Abertura da apuração correspondente ao registro selecionado\.
	- SALDO CORRIGIDO= <Valor do saldo corrigido>
	- IND\. DO SALDO CORRIGIDO= <Indicador do saldo corrigido> 
	- VALOR = __<Valor Absoluto Recuperado para Prejuízo>__
	- IND\. DO VALOR = Preencher o campo com o texto __“Prejuízo do Exercício”__
	- SALDO DISPONIVEL = <saldo disponível da conta da parte B>
	- IND\. DO SALDO DISPONIVEL = <indicador do saldo disponível da conta da parte B>
	- Tributação Diferida = Não
	- Ajuste com Origem na Parte B = Cumulativo

Só deve existir um registro de lançamento de __Prejuízo do Exercício __para a conta parametrizada e para o código da tabela dinâmica para a apuração\. Para garantir isso, no momento de efetuar o Lançamento, se já existir registro o mesmo deve ser substituído\.

A inclusão do ajuste e atualização dos valores deve seguir as mesmas regras contidas na tela Lançamentos da Parte B \(M410\)\. Tela Lancamentos da Parte B \(M410\)\.doc

Se o Valor Recuperado para __Base Negativa__ para um dos registros é menor do que zero:

Se o valor recuperado para umas das linhas \(175, 203 ou 142\) referentes a Atividade Geral for menor que zero:

Verificar na tela de Informações ECF, aba Prejuízo e Base Negativa, se campo Cód\. da Conta da Parte B para LANÇAMENTO DE BASE NEGATIVA \- INFORMAÇÕES PARA A CRIAÇÃO DO LANÇAMENTO DE BASE DE CÁLCULO NEGATIVA DA CSLL – ATIVIDADE GERAL possui uma conta parametrizada\. Caso contrário, exibir a mensagem DW00205\. Se a conta parametrizada não possuir saldo para o tributo CSLL, exibir a mensagem DW00206\.

Caso o valor da linha recuperada \(175, 203 ou 142\) for maior ou igual a zero, exibir a mensagem DW00207\. 

Se o valor recuperado para umas da linha \(349\) referente a Atividade Rural for menor que zero:

Verificar na tela de Informações ECF, aba Prejuízo e Base Negativa, se campo Cód\. da Conta da Parte B para LANÇAMENTO DE BASE NEGATIVA \- INFORMAÇÕES PARA A CRIAÇÃO DO LANÇAMENTO DE BASE DE CÁLCULO NEGATIVA DA CSLL – ATIVIDADE RURAL possui uma conta parametrizada\. Caso contrário, exibir a mensagem DW00205\. Se a conta parametrizada não possuir saldo para o tributo CSLL, exibir a mensagem DW00206\.

Caso o valor da linha recuperada \(349\) for maior ou igual a zero, exibir a mensagem DW00207\. 

Efetuar um lançamento na tela Lançamentos da Parte B \(M410\) para a conta parametrizada com os parâmetros abaixo:

- 
	- ORIGEM = Preencher o campo com o texto “Parte B”
	- HISTÓRICO = “Ajuste referente ao código <Código da Tabela Dinâmica> da tabela dinâmica\. 
	- DATA LANCTO = <Data Final> informada na tela de Abertura da apuração correspondente ao registro selecionado\.
	- VALOR = __<Valor Absoluto Recuperado para Base Negativa>__
	- IND\. DO VALOR = Preencher o campo com o texto __“Base de Cálculo Negativa da CSLL”__
	- SALDO DISPONIVEL = <saldo disponível da conta da parte B>
	- IND\. DO SALDO DISPONIVEL = <indicador do saldo disponível da conta da parte B>

Só deve existir um registro de lançamento de __Base de Cálculo Negativa da CSLL__ para a conta parametrizada e para o código da tabela dinâmica para a apuração\. Para garantir isso, no momento de efetuar o Lançamento, se já existir registro o mesmo deve ser substituído\.

A inclusão do ajuste e atualização dos valores deve seguir as mesmas regras da tela de Lançamentos da Parte B \(M410\)\. Tela Lancamentos da Parte B \(M410\)\.doc

No caso de apuração Anual, Executar RNC05 após esse processamento\.

MFS\- [17491](http://ent.jira.int.thomsonreuters.com/browse/MFS-17491)

RNC18

__Conceito do PAT__

__Introdução básica as regras de legislação:__

1. O que é o PAT?

Incentivo dado ao empregador pelo fato fornecer ao empregado alguma forma de alimentação\.

1. Como é calculado o incentivo? 

É aplicado um percentual sobre as contas contábeis correspondentes a despesa acumulada de alimentação\. Este percentual é de 15% sobre o valor dessas despesas\. Logo o resultado referente aos 15% é o que pode ser utilizado como Incentivo do PAT, porém o governo determina que o resultado dos 15% só pode ser utilizado respeitando o limite de 4% do valor do imposto no período\.

Caso o resultado de 15% não seja utilizado por completo no período devido o limite de 4%, se faz necessário guardar este valor para ser utilizado nos períodos seguintes\. O prazo de utilização deste valor expira dois anos\-calendários subsequentes\.

1. PDTI/PDTA o que é isto?

Trata\-se de um outro incentivo que pode ser deduzido do imposto à pagar no período\. O PDTI/PDTA deve ser utilizado dentro do período de apuração, pois não há um período longo de utilização como o PAT\. Por isto, quando houver os dois incentivos no mesmo período deve ser priorizado para a dedução o incentivo PDTI/PDTA e depois o incentivo do PAT deverá ser considerado\.

__Exibição do Valor do Incentivo calculado: __O Valor do PAT Atualizado que corresponde ao valor a ser utilizado no período será lançado nas seguintes linhas N620 – Linha 9 e N630 \(A, B e C\) – Linha 8 das tabelas dinâmicas\.

__Valor Disponível – PAT Períodos Anteriores: __Corresponde ao valor de Limite de 15% que não foi utilizado em sua totalidade no período de apuração e que ficou acumulado para utilização em períodos posteriores\. Este valor poderá ser utilizado em até 24 meses anteriores ao período processado\. Para maiores detalhamentos em relação a utilização deste valor no período verificar a [RNC20 – Cálculo \- PAT Períodos Anteriores](#UtilizacaodoPeriodosAnteriores)\.

MFS\-17913

RNC19

__Cálculo do PAT __

O produto considera apenas uma forma de calcular o valor do PAT\. Sempre considera o valor de PAT de Períodos Anteriores, abatendo primeiro o valor mais antigo, respeitando o limite de 24 meses, até chegar ao PAT do período\. 

Se o PAT for calculado pelo sistema, os valores poderão ser consultados pela tela Programa de Alimentação do Trabalhador\. 

__Pré\-Requisitos:__

- Se existir saldo \(após a transcrição de valores\) na linha 9 N620 ou 8 N630, seguir com as validações indicadas abaixo e o cálculo do PAT, caso contrário, nada deverá ser efetuado \(se existir valor de entrada manual em uma dessas linhas, o cálculo do PAT para o registro não deve ser efetuado\)\.

__Validações:__

- 
	- Verificar se existe Conta da Parte B informada na tela de Informações ECF \(AJUSTE DA PARTE B AUTOMÁTICO PARA INCENTIVO PAT\), caso não exista, exibir a mensagem DW00249 e seguir com o cálculo do PAT;
	- Se existir Conta da Parte B informada na tela de Informações ECF \(AJUSTE DA PARTE B AUTOMÁTICO PARA INCENTIVO PAT\), mas esta não possuir saldo para o tributo IRPJ, exibir a mensagem DW00250 e seguir com o cálculo do PAT, conforme as regras abaixo:

__Cálculo PAT__

__Regra básica: __O PAT atualizado será o limite de 4% \(com ou sem PDTI/PDTA\), abatendo sempre do valor do PAT de períodos anteriores e o valor que não for utilizado no mês do limite de 15% ficará disponível para ser utilizado em períodos posteriores\.

O registro N620 será calculado sempre mensalmente e de acordo com o tipo de receita parametrizado na tela de Abertura da Apuração, \(caso a opção escolhida seja comparativo, as duas visões, devem ser calculadas e apresentadas na tela\)\. O registro N630, será calculado sempre na visão Balanço Suspensão ou Redução e sempre com os dados do último mês processado\. O valor de saldo disponível a ser utilizado até dois anos\-calendários subsequentes, será o valor calculado no registro N630\. 

No processamento da primeira abertura de uma escrituração \(transcrição de valores ou cálculo\), o valor do PAT disponível para uso posterior \(calculado no N630\) será copiado para o registro N620 dos dois anos calendários anteriores\. 

__Exemplos: PAT sem PDTI/PDTA__

1. __Se o valor dos Limites 15% e 4% forem iguais:__

- Atualizar as linhas 9 e 8 \(N620 e N630\) da tabela dinâmica com Limite de 4% = Valor do PAT Atualizado\.

1. __Limite de 15% for maior que Limite 4%:__

- Atualizar as linhas 9 e 8 \(N620 e N630\) da tabela dinâmica com o Limite 4% = Valor do PAT Atualizado;
- Se não houver Valor de PAT de Períodos Anteriores a ser recuperado, realiza o seguinte cálculo: Limite de 15% \- Limite de 4% e armazena o resultado na tabela de Valor de PAT de Períodos Anteriores para utilização em períodos posteriores e cria um ajuste da parte B a crédito com o Valor de PAT de Períodos Anteriores\.
	- Se houver Valor Disponível – PAT Períodos Anteriores verificar a [RNC20 – Cálculo \- PAT Períodos Anteriores](#UtilizacaodoPeriodosAnteriores)\.

1. __Limite de 4% for maior que Limite de 15%:__

- Atualizar as linhas 9 e 8 \(N620 e N630\) da tabela dinâmica com o Limite 4% = Valor do PAT Atualizado;
- Se não houver Valor de PAT de Períodos Anteriores a ser recuperado, considerar como Valor do PAT Atualizado o valor correspondente ao Limite de 15%\.
	- Se houver Valor Disponível – PAT Períodos Anteriores, verificar a [RNC20 – Cálculo \- PAT Períodos Anteriores](#UtilizacaodoPeriodosAnteriores)\.

__Exemplos Cálculo PAT com PDTI/PDTA:__

__PDTI/PDTA:__ Corresponde aos valores das linhas 10 do registro N620 e linha 9 do registro N630A, N630B ou N630C 

__Identificação do valor do Imposto para identificação do limite de 4% com PDTI/PDTA: __Realiza o cálculo: Limite de 4% \- PDTI/PDTA = Limite de 4% com PDTI/PDTA 

1. __Se Limite de 4% com PDTI/PDTA__ __menor ou igual a zero:__

- Atualizar as linhas 9 e 8 \(N620 e N630\) da tabela dinâmica com zero = Valor do PAT Atualizado, armazena o Limite de 15% na tabela de Valor de PAT de Períodos Anteriores para utilização em períodos posteriores, criando um ajuste da parte B a crédito com este valor\. 

1. __Se Limite de 4% com PDTI/PDTA for maior que zero:__ 

- Verifica qual é o maior valor Limite de 15% ou Limite de 4% com PDTI/PDTA\. 
	1. __Se o valor dos Limites 15% e 4% com PDTI/PDTA forem iguais:__
- Atualiza as linhas 9 e 8 \(N620 e N630\) da tabela dinâmica com o Limite de 4% com PDTI/PDTA = Valor do PAT Atualizado\. 
	- Caso exista período anterior, verificar a  [RNC20 – Cálculo \- PAT Períodos Anteriores](#UtilizacaodoPeriodosAnteriores)\.

	1. __Se o Limite 15% maior que o Limite de 4% com PDTI/PDTA__
- Atualiza os valores das linhas 9 e 8 \(N620 e N630\) com o Limite de 4% com PDTI/PDTA = Valor do PAT Atualizado\.
- Se não houver Valor de PAT de Períodos Anteriores a ser recuperado realiza o seguinte cálculo: Limite de 15% \- Limite de 4% com PDTI/PDTA e armazena o resultado na tabela de Valor de PAT de Períodos Anteriores para utilização em períodos posteriores e cria um ajuste da parte B a crédito com o Valor de PAT de Períodos Anteriores\.
	- Se houver Valor Disponível – PAT Períodos Anteriores verificar a  [RNC20 – Cálculo \- PAT Períodos Anteriores](#UtilizacaodoPeriodosAnteriores)\.

	1. __Limite de 4% com PDTI/PDTA for maior que Limite de 15%:__
- Atualiza os valores das linhas da tabela dinâmica com o Limite 4% com PDTI/PDTA = Valor do PAT Atualizado;
- Se não houver Valor de PAT de Períodos Anteriores a ser recuperado considerar como Valor do PAT Atualizado o valor correspondente ao Limite de 15%\.
	- Se houver Valor Disponível – PAT Períodos Anteriores verificar a  [RNC20 – Cálculo \- PAT Períodos Anteriores](#UtilizacaodoPeriodosAnteriores)\.

Obs\.: Os valores recuperados de períodos anteriores não utilizados no período corrente continuarão na tabela para utilização em períodos posteriores\.

MFS\-17913

RNC20

<a id="UtilizacaodoPeriodosAnteriores"></a>__Utilização dos Períodos Anteriores no cálculo do PAT – \(Ajuste na ParteB\)__

__Se o valor dos períodos anteriores for maior ou igual ao Limite 4% ou Limite 4% com PDTI/PDTA:__

- Atualiza as linhas 9 e 8 \(N620 e N630\) da tabela dinâmica com o Limite de 4% com PDTI/PDTA = Valor do PAT Atualizado\.
- Cria um ajuste a débito na tabela de controle do Valor de PAT dos períodos anteriores, com o mesmo valor contido no campo Limite 4% ou Limite 4% com PDTI/PDTA\.

A parcela correspondente ao valor limite de 15% \(valor total, que não foi utilizado no período\), será acumulada e deverá ser armazenada na tabela de controle correspondente Valor de PAT de Períodos Anteriores e cria um ajuste da parte b a crédito, com este valor\. Este ajuste automático, só deve ser criado na conta da parte B informada no campo conta da parte b \(AJUSTE DA PARTE B AUTOMÁTICO PARA INCENTIVO PAT\) na tela de Informações ECF \(aba LALUR e LACS\), considerando o valor obtido apenas do registro N630\. 

__Se o valor dos períodos anteriores for menor que o Limite 4% ou Limite 4% com PDTI/PDTA:__

- Atualiza as linhas 9 e 8 \(N620 e N630\) da tabela dinâmica com o Limite de 4% com PDTI/PDTA = Valor do PAT Atualizado\.
- Utilizar todo o valor dos períodos anteriores e recuperar do Limite 15% \(do período de apuração\) o valor restante para atingir o Limite 4% ou Limite de 4% com PDTI/PDTA;
- Valor do limite 15% não utilizado será armazenado na tabela correspondente ao Valor de PAT de Períodos Anteriores e deverá ser criado um ajuste da parte B a crédito com este valor \(Valor de PAT de Períodos Anteriores\)\. Este ajuste automático, só deve ser criado na conta da parte B informada no campo conta da parte b \(AJUSTE DA PARTE B AUTOMÁTICO PARA INCENTIVO PAT\) na tela de Informações ECF \(aba LALUR e LACS\), considerando o valor obtido apenas do registro N630\. Caso a conta não tenha sido informada, exibir a mensagem DW00249 e não criar o ajuste da parte B\.

__Criação dos Lançamentos da Parte B, \(somente será criado em função do cálculo do PAT do registro N630\):__

Esse lançamento será feito no último mês apurado \(Dezembro, ou o último mês em caso de situação especial\)\. No caso de apuração Trimestral esse lançamento será feito trimestralmente\.

__Regra de preenchimento dos campos:__

__Origem:__ Parte B

__Histórico:__ Programa de Alimentação do Trabalhador – <<MM/AAAA ou Trimestre/AAAA>>

Onde: MM/AAAA = Mês e Ano Processado

Ex: 01/2015

Trimestre/AAAA = Trimestre e Ano Processado

Ex: 1º Trimestre/2015

__Data Lancto:__ Último dia do mês ou trimestre que está sendo processado ou a Data do Evento em caso de Situação Especial

__Valor:__ Valor do Ajuste conforme cálculo do PAT

__Indicador:__ Crédito ou Débito, conforme cálculo do PAT \(RNC18\)

__Tributação Diferida:__ Não

__Contrapartida__: Em branco \(não preencher\)

__Ajuste com Origem na Parte B:__ Incremental

__Obs\. Não criamos um lançamento automático na conta da parte b dos valores de PAT não utilizados que ultrapassaram o limite de dois anos\-calendários subsequentes\.__

MFS\-17913

# <a id="_Toc434585164"></a><a id="_Toc512254970"></a>REGRAS – PROCESSAMENTO DOS REGISTROS 

__Considerações gerais:__

O processamento dos registros deverá ocorrer com base na importação dos saldos e/ou cálculo\.

__CÓD__

###### __DESCRIÇÃO__

__MFS__

RNP01

## <a id="_Toc434585165"></a><a id="_Toc512254971"></a>3\.1 Regra Geral \- Processamento dos Blocos K, N, L, M

Ordenação de processamento dos Blocos: K, L, M e N\.

1. Para o processamento dos blocos K, N, L e M devem ser atendidos os critérios abaixo:

- Período de recuperação dos registros: Data Inicial e Final do Período de Apuração informada na tela de Abertura da Apuração durante o Processamento em Lote\.
- Forma de Tributação da tela de Abertura da Apuração = “Lucro Real”\. Para o bloco K, considerar também Forma de Tributação da tela de Abertura da Apuração = “Lucro Presumido”\.

1. __Se na tela abertura da apuração o campo Período da Apuração = “Anual” __

Para cada abertura de apuração da escrituração, com forma de tributação = “Lucro Real” deverá ser processado os meses de Janeiro à Dezembro\. \(Forma de Tributação = “A01\.\.\. A12”\)\. Após este processamento será possível visualizar o resultado nas telas de demonstração dos resultados dos registros nas abas de Janeiro à Dezembro e na aba Anual com base na execução da regra de geração da Apuração [A00](#A00)\.

1. __Se na tela abertura da apuração o campo Período da Apuração = “Trimestral” __

Para cada abertura de apuração da escrituração, com forma de tributação = “Lucro Real” ou “Lucro Presumido” ou “Lucro Arbitrado” ou “Imune do IRPJ” ou “ Isenta do IRPJ”\. Neste caso, deverá ser processado os trimestres 1º Trimestre à 4 º Trimestre\.  \(Forma de Tributação = “T01\.\.\. T04”\)\.

MFS\-13202

MFS\-13997

MFS\-12632

RNP02

## <a id="_Toc383595391"></a><a id="_Toc406578355"></a><a id="_Toc418782053"></a><a id="_Toc434585174"></a><a id="_Toc512254972"></a>3\.2 Registro L100: Balanço Patrimonial

__Condições Gerais: __

- Campo Qualificação da Pessoa Jurídica = “PJ em Geral” ou “PJ Componente do Sistema Financeiro” ou “Sociedades Seguradoras, de Capitalização ou Entidade Aberta de Previdência Complementar” na tela Informações ECF\.

__Regras de Recuperação:__ 

Com base na visão de balanço, recuperar os saldos inicial referente ao início do período inicial da apuração e final dos registros que foram processados na importação de saldos, através da tabela referencial cujo campo registro seja iniciado com “L100A”, “L100B” ou “L100C”\.

O resultado do processamento deste registro deverá ser exibido na tela Lucro Real, registro L100\.

MFS\-13202

RNP03

## <a id="_Toc383595394"></a><a id="_Toc406578358"></a><a id="_Toc418782055"></a><a id="_Toc434585176"></a><a id="_Toc512254973"></a>Registro L300: Demonstração do Resultado do Lucro Líquido Fiscal 

__Condições Gerais: __

- Campo Qualificação da Pessoa Jurídica = “PJ em Geral” ou “PJ Componente do Sistema Financeiro” ou “Sociedades Seguradoras, de Capitalização ou Entidade Aberta de Previdência Complementar” na tela Informações ECF\.

__Regras de Recuperação:__ 

Com base na visão de balanço, recuperar os saldos inicial referente ao início do período inicial da apuração e final dos registros que foram processados na importação de saldos, através da tabela referencial cujo campo registro seja iniciado com “L300A”, “L300B” ou “L300C”\.

O resultado do processamento deste registro deverá ser exibido na tela Lucro Real, registro L300\.

MFS\-13202

RNP04

## <a id="_Toc418782060"></a><a id="_Toc434585181"></a><a id="_Toc512254974"></a><a id="RNP04"></a>Registro K155: Detalhes dos Saldos Contábeis \(Depois do Encerramento do Resultado do Período\)

__Condições Gerais: __

Para o registro L100:

- Campo Qualificação da Pessoa Jurídica = “PJ em Geral” ou “PJ Componente do Sistema Financeiro” ou “Sociedades Seguradoras, de Capitalização ou Entidade Aberta de Previdência Complementar” na tela Informações ECF\.

__Regras de Recuperação:__ 

Com base na visão do balanço, recuperar o valor total de crédito acumulado, o valor total de débito acumulado, o saldo inicial referente ao início do período inicial da apuração e saldo final, dos registros que foram processados na importação de saldos \(cuja natureza da conta = ‘1’, ‘2’  ou ‘3’\), através da tabela referencial cujo campo registro seja iniciado com “L100A”, “L100B”, “L100C”\.

O resultado do processamento deste registro deverá ser exibido na tela Lucro Real, registro K155\.

MFS\-13202

RNP05

## <a id="_Toc434585182"></a><a id="_Toc512254975"></a>Registro K156: Mapeamento Referencial do Saldo Final

__Condições Gerais: __

- [Pré\-processamento do bloco K, com situações de rateio \(etapa1\)\.](#Etapa1_Rateio_BlocoK)
- Execução da [RNP04](#RNP04)

__Regras de Recuperação:__ 

Com base na visão do balanço, recuperar o valor do saldo final, das contas referenciais dos registros que foram processados na importação de saldos, e que foram rateadas na tela de Ajustes do Bloco K, aba Rateio, através da tabela referencial cujo campo registro seja iniciado com “L100A”, “L100B”, “L100C\.

O resultado do processamento deste registro deverá ser exibido na tela Lucro Real, registro K155 \.

MFS\-13202

RNP06

## <a id="_Toc434585183"></a><a id="_Toc512254976"></a><a id="RNP06"></a>Registro K355: Saldos Finais das Contas Contábeis de Resultado Antes do Encerramento

__Condições Gerais: __

Para o registro L300:

- Campo Qualificação da Pessoa Jurídica = “PJ em Geral” ou “PJ Componente do Sistema Financeiro” ou “Sociedades Seguradoras, de Capitalização ou Entidade Aberta de Previdência Complementar” na tela Informações ECF\.

__Regras de Recuperação:__ 

Com base na visão de balanço, recuperar o valor do saldo final, dos registros que foram processados na importação de saldos \(cuja natureza da conta = ‘4’\), através da tabela referencial cujo campo registro seja iniciado com “L300A”, “L300B”, “L300C”\.

O resultado do processamento deste registro deverá ser exibido na tela Lucro Real, registro K355\.

MFS\-13202

RNP07

## <a id="_Toc434585184"></a><a id="_Toc512254977"></a>3\.7 Registro K356: Mapeamento Referencial dos Saldos Finais das Contas Contábeis de Resultado Antes do Encerramento

__Condições Gerais: __

- [Pré\-processamento do bloco K, com situações de rateio \(etapa1\)\.](#Etapa1_Rateio_BlocoK)
- Execução da [RNP06](#RNP06)

__Regras de Recuperação:__ 

Com base na visão de balanço, recuperar o valor do saldo final, das contas referenciais dos registros que foram processados na importação de saldos, e que foram rateadas na tela de Ajustes do Bloco K, aba Rateio, através da tabela referencial cujo campo registro seja iniciado com “L300A”, “L300B”, “L300C”\.

O resultado do processamento deste registro deverá ser exibido na tela Lucro Real, registro K355\.

MFS\-13202

RNP08

## <a id="_Toc406578357"></a><a id="_Toc496630852"></a><a id="_Toc512254978"></a>Registro L210: Informativo de Composição de Custos 

__Condições Gerais: __

- Campo Qualificação da Pessoa Jurídica = “PJ em Geral” da tela “Informações ECF”\.
- Este registro depende da geração de linhas específicas do registro L210A, quando não existir valores nas linhas do L210 que serão utilizadas no cálculo deste registro, aplicar a RNG00034 \- Dependência de informações entre registros da Tabela Dinâmica\.

__Regras de Recuperação:__ 

Com base na visão de balanço, recuperar os saldos que foram processados na importação de saldos e cálculo, através da tabela dinâmica cujo campo registro seja iniciado com “L210”\.

O resultado do processamento deste registro deverá ser exibido na tela Lucro Real, registro L210 \(Informativo da Composição de Custos\)

MFS\-13997

RNP09

## <a id="_Toc434585166"></a><a id="_Toc512254979"></a>Registro N500: Base de Cálculo do IRPJ Sobre o Lucro Real Após as Compensações de Prejuízos

__Condições Gerais: __

- Execução da RNP01 quando o campo Tipo de Receita \(Tela Abertura da Apuração\) for = Receita Bruta ou = Balanço Suspensão ou Redução ou = Comparativo ou forma de tributação = “T1 à T4”\.
- Neste registro, há fórmula condicionada, observar planilha \[Compara Dinamicas\.xls\]
- Este registro depende da geração de linhas específicas do registro M300\. 

__Regras de Recuperação:__ 

Recuperar os saldos que foram processados na importação de saldos e cálculo, através da tabela dinâmica cujo campo registro seja iniciado com “N500”\.

O resultado do processamento deste registro deverá ser exibido na tela Lucro Real, registroN500\.

MFS\-13997

MFS\-12632

RNP10

## <a id="_Toc434585167"></a><a id="_Toc406323649"></a><a id="_Toc406323302"></a><a id="_Toc406322786"></a><a id="_Toc406322428"></a><a id="_Toc406321758"></a><a id="_Toc406321090"></a><a id="_Toc406320666"></a><a id="_Toc512254980"></a>Registro N600: Demonstração do Lucro da Exploração

__Condições Gerais: __

- Execução da RNP01 quando o campo Tipo de Receita \(Tela Abertura da Apuração\) for = “Receita Bruta” ou “Balanço Suspensão ou Redução” ou “Comparativo” ou forma de tributação = “T1 à T4”\.
- Campo Lucro da Exploração da tela “Informações ECF” selecionado
- Este registro depende da geração de linhas específicas dos registros L300 e M300, quando não existir valores nas linhas do L300 que serão utilizadas no cálculo deste registro, aplicar a RNG00037\- Dependência de informações entre registros do Plano Referencial\.

__Regras de Recuperação:__ 

Recuperar os saldos que foram processados na importação de saldos e cálculo, através da tabela dinâmica cujo campo registro seja iniciado com “N600”\.

O resultado do processamento deste registro deverá ser exibido na tela Lucro Real, registro N600\.

MFS\-13997

MFS\-12632

RNP11

## <a id="_Toc434585168"></a><a id="_Toc418782047"></a><a id="_Toc406323650"></a><a id="_Toc406323303"></a><a id="_Toc406322787"></a><a id="_Toc406322429"></a><a id="_Toc406321759"></a><a id="_Toc406321091"></a><a id="_Toc512254981"></a>Registro N610: Cálculo da Isenção e Redução do Imposto Sobre o Lucro Real

__Condições Gerais: __

- Execução da RNP01 quando o campo Tipo de Receita \(Tela Abertura da Apuração\) for = “Receita Bruta” ou “Balanço Suspensão ou Redução” ou “Comparativo” ou forma de tributação = “T1 à T4”\.
- Parâmetro Lucro da Exploração selecionado na tela “Informações ECF” selecionado
- Este registro depende da geração de linhas específicas dos registros M300, N500, N600 e N610\. Para as linhas dos registros N500, N600 e N610 que serão utilizados no cálculo deste registro, aplicar a RNG00034 \- Dependência de informações entre registros da Tabela Dinâmica\.

__Regras de Recuperação:__ 

Recuperar os saldos que foram processados na importação de saldos e cálculo, através da tabela dinâmica cujo campo registro seja iniciado com “N610”\.

O resultado do processamento deste registro deverá ser exibido na tela Lucro Real, registro N610\.

MFS\-13997

MFS\-12632

RNP12

## <a id="_Toc434585169"></a><a id="_Toc418782048"></a><a id="_Toc512254982"></a>Registro N620: Cálculo do IRPJ Mensal por Estimativa

__Condições Gerais: __

- Execução da RNP01 quando o campo Tipo de Receita \(Tela Abertura da Apuração\) for = “Receita Bruta” ou = Balanço Suspensão ou Redução ou = “Comparativo”\. Forma de tributação =“A1 à A12”\.
- Este registro depende da geração de linhas específicas dos registros N500, N610 e N620, quando não existir valores nas linhas dos registros N500, N610 e N620 que serão utilizadas no cálculo deste registro, aplicar a RNG00034 \- Dependência de informações entre registros da Tabela Dinâmica\.

__Regras de Recuperação:__ 

Recuperar os saldos que foram processados na importação de saldos e cálculo, através da tabela dinâmica cujo campo registro seja iniciado com “N620”\.

O resultado do processamento deste registro deverá ser exibido na tela Lucro Real, registro N620\.

MFS\-13997

MFS\-12632

RNP13

## <a id="_Toc434585170"></a><a id="_Toc418782049"></a><a id="_Toc406323652"></a><a id="_Toc406323305"></a><a id="_Toc406322789"></a><a id="_Toc406322431"></a><a id="_Toc512254983"></a>Registro N630: Cálculo do IRPJ Com Base no Lucro Real

__Condições Gerais: __

- Execução da RNP01 quando o campo Tipo de Receita \(Tela Abertura da Apuração\) for = “Receita Bruta” ou “Balanço Suspensão ou Redução” ou “Comparativo” ou forma de tributação = “T1 à T4”\.
- Neste registro, há fórmula condicionada, observar a planilha \[Compara Dinamicas\.xls\]
- Este registro depende da geração de linhas específicas dos registros N500, N610 e N630, quando não existir valores nas linhas do N500, N610 e N630 que serão utilizadas no cálculo deste registro, aplicar a RNG00034 \- Dependência de informações entre registros da Tabela Dinâmica\.

__Regras de Recuperação:__ 

Recuperar os saldos que foram processados na importação de saldos e cálculo, através da tabela dinâmica cujo campo registro seja iniciado com “N630A”, “N630B” ou “N630C” 

O resultado do processamento deste registro deverá ser exibido na tela Lucro Real, registro N630\.

MFS\-13997

MFS\-12632

RNP14

## <a id="_Toc434585171"></a><a id="_Toc406323653"></a><a id="_Toc406323306"></a><a id="_Toc406322790"></a><a id="_Toc512254984"></a>Registro N650: Base de Cálculo da CSLL Após as Compensações da Base de Cálculo Negativa

__Condições Gerais: __

- Execução da RNP01 quando o campo Tipo de Receita \(Tela Abertura da Apuração\) for = Receita Bruta ou = Balanço Suspensão ou Redução ou “Comparativo” ou forma de tributação =“T1 à T4”
- Neste registro, há fórmula condicionada, observar a planilha \[Compara Dinamicas\.xls\]
- Este registro depende da geração de linhas específicas do registro M350\.

__Regras de Recuperação:__ 

Recuperar os saldos que foram processados na importação de saldos e cálculo, através da tabela dinâmica cujo campo registro seja iniciado com “N650”\.

O resultado do processamento deste registro deverá ser exibido na tela Lucro Real, registro N650\.

MFS\-13997

MFS\-12632

RNP15

## <a id="_Toc434585172"></a><a id="_Toc418782051"></a><a id="_Toc406323654"></a><a id="_Toc406323307"></a><a id="_Toc512254985"></a>Registro N660: Cálculo da CSLL Mensal por Estimativa

__Condições Gerais: __

- Execução da RNP01 quando o campo Tipo de Receita \(Tela Abertura da Apuração\) for = “Receita Bruta” ou = “Balanço Suspensão ou Redução” ou “Comparativo”\. Forma de tributação =“A1 à A12”\.
- Neste registro, há fórmula condicionada, observar a planilha \[Compara Dinamicas\.xls\]
- Este registro depende da geração de linhas específicas dos registros N600, N650 e M350, quando não existir valores nas linhas do N600 e N650 que serão utilizadas no cálculo deste registro, aplicar a RNG00034 \- Dependência de informações entre registros da Tabela Dinâmica\.

__Regras de Recuperação:__ 

Recuperar os saldos que foram processados na importação de saldos e cálculo, através da tabela dinâmica cujo campo registro seja iniciado com “N660”\.

O resultado do processamento deste registro deverá ser exibido na tela Lucro Real, registro N660\.

MFS\-13997

MFS\-12632

RNP16

## <a id="_Toc434585173"></a><a id="_Toc418782052"></a><a id="_Toc406323655"></a><a id="_Toc512254986"></a>Registro N670: Calculo da CSLL Com Base no Lucro Real

__Condições Gerais: __

- Execução da RNP01 quando o campo Tipo de Receita \(Tela Abertura da Apuração\) for = Receita Bruta ou Balanço Suspensão ou Redução ou “Comparativo” ou forma de tributação = “T1 à T4”\.
- Neste registro, há fórmula condicionada, observar a planilha \[Compara Dinamicas\.xls\]
- Este registro depende da geração de linhas específicas dos registros N600 e N670, quando não existir valores nas linhas do N600 e N670 que serão utilizadas no cálculo deste registro, aplicar a RNG00034 \- Dependência de informações entre registros da Tabela Dinâmica\.

__Regras de Recuperação:__ 

Recuperar os saldos que foram processados na importação de saldos e cálculo, através da tabela dinâmica cujo campo registro seja iniciado com “N670”\.

O resultado do processamento deste registro deverá ser exibido na tela Lucro Real, registro N670\.

MFS\-13997

MFS\-12632

RNP17

## <a id="_Toc434585177"></a><a id="_Toc512254987"></a>Registro M300: Lançamentos da Parte A do e\-Lalur

__Condições Gerais: __

- Execução da RNP01 quando o campo Tipo de Receita \(“Tela Abertura da Apuração”\) for = Receita Bruta ou = Balanço Suspensão ou Redução ou = “Comparativo” ou forma de tributação = “T1 à T4”\.
- Campo Tipo de Relacionamento = “PJ em Geral” ou “PJ Componente do Sistema Financeiro” ou “Sociedades Seguradoras, de Capitalização ou Entidade Aberta de Previdência Complementar” na tela Informações ECF\.

__Regras de Recuperação:__ 

Recuperar os saldos que foram processados na importação de saldos, através da tabela dinâmica cujo campo registro seja iniciado com “M300A”, “M300B” ou “M300C”\.

Se o Tipo do registro da Tabela Dinâmica for “CA” e existir lançamento de ajuste manual da parte A para o registro aplicar a RNG00038 \- Fórmula – Tabela Dinâmica\.

Se o Tipo do registro da Tabela Dinâmica for “CA” ou “CNA”, Tipo Lançamento for “A” ou “E” e a fórmula fizer referência a um registro do Plano de Contas Referenciais \(L100 ou L300\) é necessário realizar a conversão dos valores para totalização conforme tabela a seguir:

__Registro do Plano de Contas Referencial__

__Indicador do saldo da conta __

__TIPO\_LANÇAMENTO \(TABELA DINÂMICA\)__

__Sinal __

__Observações __

L100

Crédito

A – Adições

Positivo

Não geramos no momento

L100

Débito

A – Adições

Negativo

Não geramos no momento

L300

Crédito

A – Adições

Negativo

L300

Débito

A – Adições

Positivo

L100

Crédito

E\- Exclusões

Negativo 

Não geramos no momento

L100

Débito

E\- Exclusões

Positivo

Não geramos no momento

L300

Crédito

E\- Exclusões

Positivo

Não geramos no momento

L300

Débito

E\- Exclusões

Negativo

Não geramos no momento

O resultado do processamento deste registro deverá ser exibido na tela Lucro Real, registro M300, M305, M310 e M312\.

MFS\-13997

RNP18

## <a id="_Toc434585178"></a><a id="_Toc512254988"></a>Registro M350: Lançamentos da Parte A do e\-Lacs

__Condições Gerais: __

- Execução da RNP01 quando o campo Tipo de Receita \(“Tela Abertura da Apuração”\) for = Receita Bruta ou = Balanço Suspensão ou Redução ou = “Comparativo” ou forma de tributação = “T1 à T4”\.
- Campo Tipo de Relacionamento = “PJ em Geral” ou “PJ Componente do Sistema Financeiro” ou “Sociedades Seguradoras, de Capitalização ou Entidade Aberta de Previdência Complementar” na tela Informações ECF\.

__Regras de Recuperação:__ 

Recuperar os saldos que foram processados na importação de saldos, através da tabela dinâmica cujo campo registro seja iniciado com “M350A”, “M350B” ou “M350C”\.

Se o Tipo do registro da Tabela Dinâmica for “CA” e existir lançamento de ajuste manual da parte A para o registro aplicar a RNG00038 \- Fórmula – Tabela Dinâmica\.

Se o Tipo do registro da Tabela Dinâmica for “CA” ou “CNA”, Tipo Lançamento for “A” ou “E” e a fórmula fizer referência a um registro do Plano de Contas Referenciais \(L100 ou L300\) é necessário realizar a conversão dos valores para totalização conforme tabela a seguir:

__Registro do Plano de Contas Referencial__

__Indicador do saldo da conta __

__TIPO\_LANÇAMENTO \(TABELA DINÂMICA\)__

__Sinal __

__Observações __

L100

Crédito

A – Adições

Positivo

Não geramos no momento

L100

Débito

A – Adições

Negativo

Não geramos no momento

L300

Crédito

A – Adições

Negativo

Não geramos no momento

L300

Débito

A – Adições

Positivo

Não geramos no momento

L100

Crédito

E\- Exclusões

Negativo 

Não geramos no momento

L100

Débito

E\- Exclusões

Positivo

Não geramos no momento

L300

Crédito

E\- Exclusões

Positivo

Não geramos no momento

L300

Débito

E\- Exclusões

Negativo

Não geramos no momento

O resultado do processamento deste registro deverá ser exibido na tela Lucro Real, registro M350, M355, M360 e M362

MFS\-13997

RNP19

## <a id="_Toc512254989"></a>Registro N615: Informações da Base de Cálculo de Incentivos Fiscais

__Condições Gerais: __

- Aplicar RNG00054 – Incentivos Fiscais\.

__Regras de Recuperação:__ 

Recuperar os registros cujo campo registro seja iniciado com “N615”\.

O resultado do processamento deste registro deverá ser exibido na tela Lucro Real, registro N615\.

MFS\-12623

RNP20

## <a id="_Toc434585179"></a><a id="_Toc512254990"></a>Registro M310: Contas Contábeis Relacionadas ao Lançamento da Parte A do e\-Lalur

__Condições Gerais: __

- Execução da RNP01 quando o campo Tipo de Receita for = Receita Bruta ou = Balanço Suspensão ou Redução ou = “Comparativo” ou forma de tributação = “T1 à T4” para o campo Tipo de Relacionamento = 2 – Com Conta Contábil
- Execução da RNC07 = 3 – Com conta da Parte B e Conta Contábil\.

__Regras de Recuperação:__ 

Recuperar os saldos que foram processados na importação de saldos, através da tabela dinâmica cujo campo registro seja iniciado com “M300A”, “M300B” ou “M300C”\.

O resultado do processamento deste registro deverá ser exibido na tela Registro M300, M305, M310 e M312\.

MFS\-17089

RNP21

## <a id="_Toc434585180"></a><a id="_Toc512254991"></a>Registro M360: Contas Contábeis Relacionadas ao Lançamento da Parte A do e\-Lacs

__Condições Gerais: __

- Execução da RNP01 quando o campo Tipo de Receita for = Receita Bruta ou = Balanço Suspensão ou Redução ou = “Comparativo” ou forma de tributação = “T1 à T4” para o campo Tipo de Relacionamento = 2 – Com Conta Contábil
- Execução da RNC07 = 3 – Com conta da Parte B e Conta Contábil\.

__Regras de Recuperação:__ 

Recuperar os saldos que foram processados na importação de saldos, através da tabela dinâmica cujo campo registro seja iniciado com “M350A”, “M350B” ou “M350C”\.

O resultado do processamento deste registro deverá ser exibido na tela Registro M350, M355, M360 e M362\.

MFS\-17089

