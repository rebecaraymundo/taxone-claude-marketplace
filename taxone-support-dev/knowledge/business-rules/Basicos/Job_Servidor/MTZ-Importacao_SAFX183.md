# MTZ-Importacao_SAFX183

- **Fonte:** MTZ-Importacao_SAFX183.docx
- **Modificado:** 2025-01-17
- **Tamanho:** 46 KB

---

    

# Módulo Job Servidor – Importação – Demais Receitas – Lucro Presumido \- \(SAFX183\)

*\(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX183, conforme o Manual de Layout,  o que facilita a consulta\) *

*\(Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00\)*

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3169\-GE25

Criação da SAFX183

Será criada uma tabela para atendimento do Bloco F \(Registros F500/F510/F550 e F560\), para a pessoa jurídica submetida ao regime de apuração com base no lucro Presumido\.

05/04/2012

OS3169\-G5CDW

Alteração

Inclusao dos campos Código da Situação do Documento e Tipo de Faturamento

OS3932

Alteração

Inclusão do campo Código da Natureza da Receita

22/02/2013

OS4316

Criação de Campos

Criação dos campos Código e Descrição da SCP

30/12/2013

OS4579

Alteração no tamanho do campo 

Alteração no tamanho do campo NUM\_LANCTO para 40 posições\.

26/01/2015

MFS747447

Andréa Rocha

Alteração da regra de preenchimento dos campos Alíquota do PIS e Alíquota do COFINS, de acordo com a definição dos códigos de CST PIS/COFINS\.

17/01/2024

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN00__

__Regras gerais__

*\(espaço reservado para regras genéricas, que não dizem respeito a campos específicos\)*

OS3169\-GE25

__RN01__

__Campo 01 – Código da empresa__

 

__Tabela: __SAFX183

__Item: __01

__Nome do Campo: __COD\_EMPRESA

__Descrição: __Código da empresa

__Tipo:__ A

__Tamanho: __003

__Comentário: __Campo destinado ao código da Empresa\.

__Chave Primária__

__Obrigatório__

OS3169\-GE25

__RN02__

__Campo 02 – Código do estabelecimento__

__Tabela: __SAFX183

__Item: __02

__Nome do Campo: __COD\_ESTAB

__Descrição: __Código do estabelecimento

__Tipo:__ A

__Tamanho: __006

__Comentário: __Campo destinado ao código do Estabelecimento\.

__ Chave Primária__

__Obrigatório__

OS3169\-GE25

__RN03__

__Campo 03 – Tipo de Regime__

__Tabela: __SAFX183

__Item: __03

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Regime escolhido pela empresa

__Tipo:__ A

__Tamanho: __001

__Comentário: __Campo destinado ao tipo de regime adotado pela empresa \(Caixa ou Competência Consolidada\)\.

__Valores Válidos:__

1 – Caixa

2\- Competência Consolidada

__ Chave Primária__

__Obrigatório__

OS3169\-GE25

__RN04__

__Campo 04 – Indicador da Composição da Receita__

__Tabela: __SAFX183

__Item: __04

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Indicador da composição da Receita 

__Tipo:__ A

__Tamanho: __002

__Conteúdo do Campo: __Campo destinado ao indicador da composição da Receita, recebida pela pessoa jurídica no período da escrituração\.

__Valores Válidos:__

01 – Clientes

02 – Administradora de cartão de débito/crédito

03 – Título de crédito – Duplicata, nota promissória, cheque, etc\.

04 – Documento Fiscal

05 –Item vendido \(produtos e serviços\)

99 – Outros

__Chave Primária__

__Não obrigatório__

Validação: Este campo é obrigatório quando o regime escolhido for CAIXA \(campo 03 preenchido com 1\)\. 

Caso o regime adotado pelo cliente seja Caixa e o campo 04 não estiver preenchido, exibir a seguinte msg: “Para regime Caixa, o campo Indicador da Composição da Receita é de preenchimento obrigatório”

OS3169\-GE25

__RN05__

__Campo 05 – Informação Complementar da Composição da Receita__

__Tabela: __SAFX183

__Item: __05

__Nome do Campo: __Será definido pelo A&D__ __

__Descrição: __Informação complementar da composição da Receita 

__Tipo:__ A

__Tamanho: 255__

__Conteúdo do Campo: __Campo destinado à informação complementar da composição da Receita\.

__Chave Primária__

__Não obrigatório__

Validação: Este campo é obrigatório quando o indicador da Compoisção da Receita \(campo 04\), estiver preenchido com ‘99’\. 

Se o campo 4 for preenchido com ‘99’ e não for informado o campo 5, exibir a seguinte msg: “Campo de preenchimento obrigatório,  quando ao indicador da composição da Receita for ‘’99’\.

OS3169\-GE25

__RN06__

__Campo 06 – Número do documento__

__Tabela: __SAFX183

__Item: __06

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Número do documento

__Tipo:__ A

__Tamanho: __012

__Comentário: __

Número de identificação do documento/Operação se houver

__Chave Primária__

__Não Obrigatório__

OS3169\-GE25

__RN07__

__Campo 07 – Série do documento__

__Tabela: __SAFX183

__Item: __07

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Série do documento/Operação

__Tipo:__ A

__Tamanho: __003

__Comentário: __

Informar a série do documento/Operação se houver

__Chave Primária__

__Não Obrigatório__

OS3169\-GE25

__RN08__

__Campo 08 – Subsérie do Documento__

__Tabela: __SAFX183

__Item: __08

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Subsérie do documento/Operação

__Tipo:__ A

__Tamanho: __002

__Comentário: __

Informar a subsérie do documento/Operação se houver

__Chave Primária__

__Não Obrigatório__

OS3169\-GE25

__RN09__

A rotina de Importação do módulo JOB Servidor deve ser ajustada para que contemple a alteração no campo NUM\_LANCTO da tabela SAFX183 – Demais documentos e Receitas – Lucro Presumido, que deve ser criada com a seguinte estrutura:

__ __

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

NUM\_LANCTO

A

40

NAO

NAO

OS3169\-GE25/__ OS4579__

__RN10__

__Campo 10 – Data da Operação__

__Tabela: __SAFX183

__Item: __10

__Nome do campo: __Será definido pelo A&D

__Descrição: __Data da Operação

__Tipo:__ N

__Tamanho: __008

__Formato:__ DDMMAAAA

__Comentário:__Data da operação \(data do lançamento da nota, ou data contábil, ou data da operação de acordo  com os registros contábeis\)\.

__Obrigatório__

__ Chave Primária__

OS3169\-GE25

__RN11__

__Campo 11 –Código do Modelo__

__Tabela: __SAFX183

__Item:__ 11

__Nome do Campo: __COD\_MODELO

__Descrição: __Código do Modelo

__Tipo:__ A

__Tamanho: __002

__Chave Primária__

__Não Obrigatório__

__Conteúdo do Campo: __Deverá estar registrado na Tabela de Modelos de Documentos Fiscais \(SAFX 2024\)

OS3169\-GE25

__RN12__

__Campo 12 –Código Fiscal__

__Tabela: __SAFX183

__Item:__ 12

__Nome do Campo: __COD\_CFO

__Descrição: __Código Fiscal\.

__Tipo:__ A

__Tamanho: __004

__Chave Primária__

__Não Obrigatório__

__Conteúdo do Campo: __Informar o Código Fiscal de Operação e Prestação que deverá estar registrado na Tabela de Códigos Fiscais \(SAFX2012\)\.

OS3169\-GE25

__RN13__

__Campo 13 – Indicador da Pessoa física/Jurídica__

__Tabela: __SAFX183

__Item: __13

__Nome do Campo: __IND\_FIS\_JUR

__Descrição:__ Indicador de Pessoa Física/Jurídica

__Tipo:__ A

__Tamanho: __1

__Comentário: __Campo que deverá ser preenchido com o Indicador de Pessoa Física/Jurídica

 relacionada na Tabela de Pessoa Física/Jurídica \(SAFX04\), conforme segue:

1 – Fornecedor;

2 – Cliente;

3 – Estabelecimento;

4 – Transportadora;

5 – Cliente/Fornecedor/Transportadora\.

__Chave Primária__

__Não Obrigatório__

OS3169\-GE25

__RN14__

__Campo 14 – Código/Destinatário/Emitente/ Remetente__

__Tabela: __SAFX183

__Item: __14

__Nome do Campo: __COD\_FIS\_JUR

__Descrição:__ Código/Destinatário/Emitente/ Remetente

__Tipo:__ A

__Tamanho: __014

__Comentário: __

Deve estar registrado na Tabela de Pessoa Física/Jurídica \(SAFX04\)\. Quando se tratar de Outros Documentos Fiscais, tais como Resumo de ECF ou por Ciclo de Faturamento de Telecomunicações, Energia Elétrica e Gás Canalizado pode\-se informar  o Código do Estabelecimento\. Outra questão a ser levantada, é que o Cliente MasterSAF, pode tratar este Código seja ele Um Código Interno, ou sejam os Códigos de Cadastros na SRF se for CPF ou MF se for um CNPJ\. Ou seja, se o Sistema transacional trabalhar com CFP e CNPJ, estes códigos também poderá ser os CFP e CNPJ\. É recomendável que o tratamento seja o mesmo do Sistema transacional para evitar transtornos, embora qualquer solução atenderá ao Fisco, seja código Interno ou Códigos de Cadastros na SRF e MF\.  
Observação: Para o Convênio 51/00, este campo deve ser preenchido da seguinte forma:  
• Faturamento Direto para Leasing – preencher com o Destinatário da Nota Fiscal de Leasing, no caso a Financeira do Veículo;  
• Faturamento Direto – preencher com o Dealer de Entrega do Veículo \(Concessionária\)\.

__   Chave Primária__

__   Não Obrigatório__

OS3169\-GE25

__RN15__

__Campo 15 – Indicador do Produto__

__Tabela: __SAFX183

__Item: __15

__Nome do Campo: __IND\_PRODUTO

__Descrição: __Indicador do Produto

__Tipo:__ A

__Tamanho: __001

__Comentário: __

Identificadores:  
1 – Produto Acabado;  
2 – Insumos;  
3 – Embalagem;  
4 – Consumo;  
5 – Outros;  
6 – Em Elaboração;  
7 – Intermediário;  
8 – Miscelâneas\.  
Esta Discriminação para Identificar a Mercadoria se é Produto Acabado, Insumo, Produto em Elaboração, não é mais solicitada pela IN SRF 86/01, porém é obrigatória para outras obrigações da RIPI, tal como o Inventário, por isso, deve continuar a atender a SRF\. Obs: O preenchimento dos campos 13 e 14 exclui o preenchimento dos campos 15 e 16, e vice\-versa\.

__Chave Primária__

__Não Obrigatório__

OS3169\-GE25

__RN16__

__Campo 16 – Produto__

__Tabela: __SAFX183

__Item: __16

__Nome do campo: __COD\_PRODUTO

__Descrição: __Produto

__Tipo:__ A

__Tamanho: __035

__Conteúdo do Campo: __

Informar o Código do Produto/Mercadoria, de acordo com  as solicitações da dos Convênios ICMS, RIPI e IN SRF, devidamente registradas na Tabela de Produto \(SAFX2013\)\. Esta codificação de mercadorias/produtos deve representar os códigos dos registrados nos sistemas corporativos e nos sistemas de faturamento \(Billing\)\. Assim, para simples ilustração podemos citar que para empresas industriais e comerciais, devem ser informados os códigos internos, para telecomunicações, os serviços que especificam os tipos de ligações, etc\. Para o registro do “Resumo Diário” e Outros Resumos referentes a outros Modelos de Documentos Fiscais, não existe a exigência de Códigos específicos, bem como para registrar aquisições de Bens do Ativo e/ou as Alienações\. Por isso, para cada Tipo de Modelo de Documento Fiscal, deve ser definido os critérios  e os códigos a serem utilizados e analisar se as Legislações requerem ou não Códigos para o Atendimento a Escrituração, Meios Magnéticos e Obrigações Acessórias\. Obs: O preenchimento dos campos 13 e 14 exclui o preenchimento dos campos 15 e 16, e vice\-versa\.

__Chave Primária__

__Não Obrigatório__

OS3169\-GE25

__RN17__

__Campo 17 – Código da conta analítica debitada/creditada __

__Tabela: __SAFX183

__Item: __17

__Nome do Campo:__ COD\_CONTA

__Descrição: __Código da conta analítica debitada/creditada

__Tipo:__ A

__Tamanho: __070

__Não Obrigatório__

__Chave Primária__

__Comentário: __

Conta Contábil referente ao Imposto, utilizada para Contabilização, de acordo com a Tabela     de Plano de Contas \(SAFX2002\)\. 

OS3169\-GE25

__RN18__

__Campo 18 – Centro de Custo__

__Tabela: __SAFX183

__Item: __18

__Nome do Campo:__ COD\_CUSTO

__Descrição: __Centro de Custo

__Tipo:__ A

__Tamanho: __020

__Não Obrigatório__

__Chave Primária__

__Comentário: __O Código deve estar registrado na Tabela de Centro de Custos \(SAFX2003\)\.

OS3169\-GE25

__RN19__

__Campo 19 – Descrição complementar do Documento/Operação__

__Tabela: __SAFX183

__Item: __19

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Descrição complementar do Documento/Operação

__Tipo:__ A

__Tamanho: __255

__Não Obrigatório__

__Chave Primária__

__Comentário: __

Descrição complementar do Documento/Operação\.

OS3169\-GE25

__RN20__

__Campo 20 – Valor Total da Receita__

__Tabela: __SAFX183

__Item: __20

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Valor Total da Receita

__Tipo:__ N

__Tamanho: __015V002

__Obrigatório__

__Comentário: __Valor Total da Receita auferida no período da escrituração\.

Neste campo, deverá ser informado o valor que originou a Operação\.

OS3169\-GE25

__RN21__

__Campo 21 – Código Situação Tributária do PIS__

__Tabela: __SAFX183

__Item: __21

__Nome do Campo:__ Será definido pelo A&D

__Descrição:__ Código da Situação Tributária do PIS/PASEP

__Tipo:__ N

__Tamanho: 002__

__Obrigatório__

__Chave Primária__

__Comentário: __Código da Situação Tributária referente ao PIS/PASEP__ __

OS3169\-GE25

__RN22__

__Campo 22 – Alíquota do PIS__

__Tabela: __SAFX183

__Item: 2__2

__Nome do Campo:__ Será definido pelo A&D

__Descrição:__ Alíquota do PIS

__Tipo:__ N

__Tamanho: __008V004

__Não obrigatório__

__Chave Primária__

__Comentário: __

Alíquota do PIS/PASEP \(em percentual\) de acordo com a tributação da empresa, informado no lançamento ou documento fiscal\.

Validação: Quando o campo Código Situação Tributária do PIS for diferente de “6” e o campo Valor da Base de cálculo do PIS estiver preenchido, o campo Alíquota do PIS deve ser preenchido\.  Caso contrário exibir, a seguinte mensagem de erro ao usuário: 

         “Se Valor Base PIS  e informado, devera ser preenchido o campo Aliquota em Percentuais\.”

OS3169\-GE25

MFS747447

__RN23__

__Campo 23 – Valor da Base de cálculo do PIS__

__Tabela: __SAFX183

__Item: 23__

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Valor da Base de cálculo do PIS

__Tipo:__ N	

__Tamanho: __015V002

__Não obrigatório__

__Comentário:__

Valor da Base de cálculo do PIS/PASEP de acordo com a operação\.

OS3169\-GE25

__RN24__

__Campo 24 – Alíquota do PIS em Reais__

__Tabela: __SAFX183

__Item: __24

__Nome do Campo:__ Será definido pelo A&D

__Descrição:__ Alíquota do PIS em Reais

__Tipo:__ N

__Tamanho: __015V004

__Não obrigatório__

__Chave Primária__

__Comentário: __

Alíquota do PIS/PASEP \(em real\) de acordo com a tributação da empresa, informado no lançamento ou documento fiscal\.

OS3169\-GE25

__RN25__

__Campo 25 – Quantidade – Base PIS__

__Tabela: __SAFX183

__Item: 25__

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Valor da Base de cálculo do PIS em quantidade

__Tipo:__ N	

__Tamanho: __015V003

__Não obrigatório__

__Comentário:__

Valor da Base de cálculo do PIS/PASEP \(em quantidade\)\.

OS3169\-GE25

__RN26__

__Campo 26 – Valor do Desconto do PIS__

__Tabela: __SAFX183

__Item: 26__

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Valor do Desconto do PIS/PASEP 

__Tipo:__ N	

__Tamanho: __015V002

__Não obrigatório__

__Comentário:__

Valor do Desconto do PIS/PASEP\.

OS3169\-GE25

__RN27__

__Campo 27 – Valor do PIS__

__Tabela: __SAFX183

__Item: __27

__Nome do Campo:__ Será definido pelo A&D

__Descrição:__ Valor do PIS

__Tipo:__ N

__Tamanho: __015V002

__Não obrigatório__

__Comentário: __

Valor do PIS/PASEP calculado pela multiplicação dos campos Valor da Base de cálculo do PIS/PASEP \* Alíquota do PIS/PASEP informado no lançamento ou documento fiscal\.

OS3169\-GE25

__RN28__

__Campo 28 – Código Situação Tributária da COFINS__

__Tabela: __SAFX183

__Item: __28

__Nome do Campo:__ Será definido pelo A&D

__Descrição:__ Código da Situação Tributária da COFINS

__Tipo:__ N

__Tamanho: 002__

__Obrigatório__

__Chave Primária__

__Comentário: __Código da Situação Tributária referente ao COFINS__ __

OS3169\-GE25

__RN29__

__Campo 29 – Alíquota da COFINS__

__Tabela: __SAFX183

__Item: __29

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Alíquota da COFINS

__Tipo:__ N

__Tamanho: __008V004

__Não obrigatório__

__Chave Primária__

__Comentário: __

Alíquota da COFINS \(em percentual\) de acordo com a tributação da empresa informada nos lançamentos ou documento fiscal\.

Validação: Quando o campo Código Situação Tributária da COFINS for diferente de “6” e o campo Valor da Base de cálculo da COFINS estiver preenchido, o campo Alíquota da COFINS deve ser preenchido\. Caso contrário exibir, a seguinte mensagem de erro ao usuário: 

         “Se Valor Base COFINS  e informado, devera ser preenchido o campo Aliquota em Percentuais\.”

OS3169\-GE25

MFS747447

__RN30__

__Campo 30 – Valor da Base de cálculo da COFINS__

__Tabela: __SAFX183

__Item: 30__

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Valor da Base de cálculo da COFINS

__Tipo:__ N	

__Tamanho: __015V002

__Não obrigatório__

__Comentário:__

Valor da Base de cálculo do  COFINS de acordo com a operação\.

OS3169\-GE25

__RN31__

__Campo 31 – Alíquota da COFINS em Reais__

__Tabela: __SAFX183

__Item: __31

__Nome do Campo:__ Será definido pelo A&D

__Descrição:__ Alíquota da COFINS em Reais

__Tipo:__ N

__Tamanho: __015V004

__Não obrigatório__

__Chave Primária__

__Comentário: __

Alíquota da COFINS \(em real\) de acordo com a tributação da empresa, informado no lançamento ou documento fiscal\.

OS3169\-GE25

__RN32__

__Campo 32 – Quantidade – Base COFINS__

__Tabela: __SAFX183

__Item: 32__

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Valor da Base de cálculo da COFINS em quantidade

__Tipo:__ N	

__Tamanho: __015V003

__Não obrigatório__

__Comentário:__

Valor da Base de cálculo da COFINS \(em quantidade\)\.

OS3169\-GE25

__RN33__

__Campo 33 – Valor do Desconto da COFINS__

__Tabela: __SAFX183

__Item: 33__

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Valor do Desconto da COFINS 

__Tipo:__ N	

__Tamanho: __015V002

__Não obrigatório__

__Comentário:__

Valor do Desconto da COFINS\.

OS3169\-GE25

__RN34__

__Campo 34 – Valor da COFINS__

__Tabela: __SAFX183

__Item: __34

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Valor da COFINS

__Tipo:__ N

__Tamanho: __015V002

__Não obrigatório__

__Comentário: __

Valor da COFINS calculado pela multiplicação dos campos Valor da Base de cálculo da COFINS \*  Alíquota da COFINS informada nos lançamentos ou documento fiscal\.

OS3169\-GE25

__RN35__

__Campo 35 – Código da Situação do  Documento__

__Tabela: __SAFX183

__Item: __35

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Código da Situação do Documento

__Tipo:__ A

__Tamanho: __01

__Não Obrigatório__

__Comentário: __Código da Situação do Documento\. Valores Válidos:

       <Branco>

1. – Documento Regular

2\-  Documento Cancelado

3 \-  Outros

OS3169\-GE25CDW

__RN36__

__Campo 36 – Tipo de Faturamento__

__Tabela: __SAFX183

__Item: __36

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Tipo de faturamento

__Tipo:__ A

__Tamanho: __01

__Não Obrigatório__

__Comentário: __Indicador de Pagamento\. Valores Válidos:

<branco>

1 – A Vista

1. – A Prazo
2. – Sem pagamento 

OS3169\-GE25CDW

__RN37__

__Campo  \- Código da Natureza da Receita__

__Tabela: __SAFX183

__Item: __A ser definido pelo A&D

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Código da Natureza da Receita

__Tipo:__ N

__Tamanho: __03

__Não Obrigatório__

__Comentário: __Informar o Código da Natureza da Receita  da operação/serviço não tributada ou não sujeita ao pagamento da contribuição PIS/COFINS, conforme as tabelas externas da EFD PIS/PASEP–COFINS, disponibilizadas pela RFB\.

Campo Não Obrigatório\.

Validação: O campo Código da Natureza da Receita deve estar previamente cadastrado na taces 72 \(DWT\_NAT\_REC\), caso contrário exibir, a seguinte msg ao usuário: “Este campo deve estar previamente cadastrado na taces72\.”

OS3932

__RN38__

__Campo Código da SCP__

Alterar a rotina de importação e importação batch para que seja considerado o novo campo:

Tabela: SAFX183

Item: A ser reservado pelo A&D

Nome do Campo: Código da SCP

Tipo: A

Tamanho: 014

Comentário: Código da Sociedade em Conta de Participação

Deverá existir um cadastro correspondente na SAFX2057 para o código informado\. Caso não exista, retornar a mensagem: “Cadastro da SCP não encontrado”\.

__OS4316__

