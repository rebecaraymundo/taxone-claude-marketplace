# MTZ-Importacao_SAFX147

- **Fonte:** MTZ-Importacao_SAFX147.docx
- **Modificado:** 2022-09-19
- **Tamanho:** 50 KB

---

C    

# Módulo Job Servidor – Importação – Demais documentos e Operações Geradoras de crédito \(SAFX147\)

*\(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX147, conforme o Manual de Layout,  o que facilita a consulta\) *

*\(Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00\)*

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3169\-Dw2

Criação da SAFX147

Será criada uma tabela para atendimento do Bloco F100 do Anexo Único do Ato Declaratório Executivo COFINS Nº 31, de 08 de julho de 2010\.

20/09/2010

OS3169\-DW3A

Alteração da SAFX 147

Inclusão dos campos número do documento, série,  subsérie e número do lançamento para diferenciar quando para uma ou mais operações existir a mesmas informações nos campos chaves nesta SAFX 

14/12/2010

OS4316

Criação de Campos

Criação dos campos Código e Descrição da SCP

30/12/2013

OS4579

Alteração no tamanho do campo 

Alteração no tamanho do campo NUM\_LANCTO para 40 posições\.

26/01/2015

MFS36163

Criação de Campos

RN24, RN26, RN27: inclusão do Código Situação Tributária PIS e Código Situação Tributária COFINS

15/07/2020

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN00__

__Regras gerais__

*\(espaço reservado para regras genéricas, que não dizem respeito a campos específicos\)*

__RN01__

__Campo 01 \- Código da empresa__

 

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Código da empresa na tabela SAFX147\.

__Tabela: __SAFX147

__Item: __01

__Nome do Campo: __COD\_EMPRESA

__Descrição: __Código da empresa

__Tipo:__ A

__Tamanho: __003

__Comentário: __Campo destinado ao código da Empresa\.

__Chave Primária__

OS3169\-Dw2

__RN02__

__Campo 02 \- Código do estabelecimento__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Código do estabelecimento na tabela SAFX147\.

__Tabela: __SAFX147

__Item: __02

__Nome do Campo: __COD\_ESTAB

__Descrição: __Código do estabelecimento

__Tipo:__ A

__Tamanho: __006

__Comentário: __Campo destinado ao código do Estabelecimento\.

__ Chave Primária__

OS3169\-Dw2

__RN03__

__Campo 03 \- Tipo de documento__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Tipo de documento na tabela SAFX147\.

__Tabela: __SAFX147

__Item: __03

__Nome do Campo: __COD\_DOCTO

__Descrição: __Código do documento

__Tipo:__ A

__Tamanho: __005

__Conteúdo do Campo: __Campo destinado ao código do documento da SAFX2005\.__ __

__Chave Primária__

OS3169\-Dw2

__RN04__

__Campo 04 \- Indicador da Pessoa física/Jurídica__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Indicador da Pessoa física/Jurídica na tabela SAFX147\.

__Tabela: __SAFX147

__Item: __04

__Nome do Campo: __IND\_FIS\_JUR

__Descrição:__ Indicador de Pessoa Física/Jurídica

__Tipo:__ A

__Tamanho: __1

__Comentário: __Campo que deverá ser preenchido com o Indicador de Pessoa Física/Jurídica

 relacionada na Tabela de Pessoa Física/Jurídica \(SAFX04\), conforme segue:

1 \- Fornecedor;

2 \- Cliente;

3 \- Estabelecimento;

4 \- Transportadora;

5 \- Cliente/Fornecedor/Transportadora\.

__Chave Primária__

__Não Obrigatório__

OS3169\-Dw2

__RN05__

__Campo 05 \- Código/Destinatário/Emitente/ Remetente__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Código/Destinatário/Emitente/ Remetente na tabela SAFX147\.

__Tabela: __SAFX147

__Item: __05

__Nome do Campo: __COD\_FIS\_JUR

__Descrição:__ Código/Destinatário/Emitente/ Remetente

__Tipo:__ A

__Tamanho: __060

__Comentário: __

Deve estar registrado na Tabela de Pessoa Física/Jurídica \(SAFX04\)\. Quando se tratar de Outros Documentos Fiscais, tais como Resumo de ECF ou por Ciclo de Faturamento de Telecomunicações, Energia Elétrica e Gás Canalizado pode\-se informar  o Código do Estabelecimento\. Outro questão a ser levantada, é que o Cliente MasterSAF, pode tratar este Código seja ele Um Código Interno, ou sejam os Códigos de Cadastros na SRF se for CPF ou MF se for um CNPJ\. Ou seja, se o Sistema transacional trabalhar com CFP e CNPJ, estes códigos também poderão ser os CFP e CNPJ\. É recomendável que o tratamento seja o mesmo do Sistema transacional para evitar transtornos, embora qualquer solução atenderá ao Fisco, seja código Interno ou Códigos de Cadastros na SRF e MF\.  
Observação: Para o Convênio 51/00, este campo deve ser preenchido da seguinte forma:  
• Faturamento Direto para Leasing \- preencher com o Destinatário da Nota Fiscal de Leasing, no caso a Financeira do Veículo;  
• Faturamento Direto \- preencher com o Dealer de Entrega do Veículo \(Concessionária\)\.

__   Chave Primária__

__   Não Obrigatório__

OS3169\-Dw2

__RN06__

__Campo 06 \- Indicador do Produto__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Indicador do Produto na tabela SAFX147\.

__Tabela: __SAFX147

__Item: __06

__Nome do Campo: __IND\_PRODUTO

__Descrição: __Indicador do Produto

__Tipo:__ A

__Tamanho: __001

__Comentário: __

Identificadores:  
1 \- Produto Acabado;  
2 \- Insumos;  
3 \- Embalagem;  
4 \- Consumo;  
5 \- Outros;  
6 \- Em Elaboração;  
7 \- Intermediário;  
8 \- Miscelâneas\.  
Esta Discriminação para Identificar a Mercadoria se é Produto Acabado, Insumo, Produto em Elaboração, não é mais solicitada pela IN SRF 86/01, porém é obrigatória para outras obrigações da RIPI, tal como o Inventário, por isso, deve continuar a atender a SRF\. Obs: O preenchimento dos campos 13 e 14 exclui o preenchimento dos campos 15 e 16, e vice\-versa\.

__Chave Primária__

__Não Obrigatório__

OS3169\-Dw2

__RN07__

__Campo 07 \- Produto__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Produto na tabela na tabela SAFX147\.

__Tabela: __SAFX147

__Item: __07

__Nome do campo: __COD\_PRODUTO

__Descrição: __Produto

__Tipo:__ A

__Tamanho: __035

__Conteúdo do Campo: __

Informar o Código do Produto/Mercadoria, de acordo com  as solicitações da dos Convênios ICMS, RIPI e IN SRF, devidamente registradas na Tabela de Produto \(SAFX2013\)\. Esta codificação de mercadorias/produtos deve representar os códigos dos registrados nos sistemas corporativos e nos sistemas de faturamento \(Billing\)\. Assim, para simples ilustração podemos citar que para empresas industriais e comerciais, devem ser informados os códigos internos, para telecomunicações, os serviços que especificam os tipos de ligações, etc\. Para o registro do “Resumo Diário” e Outros Resumos referentes a outros Modelos de Documentos Fiscais, não existe a exigência de Códigos específicos, bem como para registrar aquisições de Bens do Ativo e/ou as Alienações\. Por isso, para cada Tipo de Modelo de Documento Fiscal, deve ser definido os critérios  e os códigos a serem utilizados e analisar se as Legislações requerem ou não Códigos para o Atendimento a Escrituração, Meios Magnéticos e Obrigações Acessórias\. Obs: O preenchimento dos campos 13 e 14 exclui o preenchimento dos campos 15 e 16, e vice\-versa\.

__Chave Primária__

__Não Obrigatório__

OS3169\-Dw2

__RN08__

__Campo 08 – Data da Operação__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Data da Operação na tabela SAFX147\.

__Tabela: __SAFX147

__Item: __08

__Nome do campo: __DATA\_OPER

__Descrição: __Data da Operação

__Tipo:__ N

__Tamanho: __008

__Formato:__ DDMMAAAA

__Comentário: __Data da operação \(data do lançamento da nota, ou data contábil, ou data da operação de acordo  com os registros contábeis\)\.

__ Chave Primária__

OS3169\-Dw2

__RN09__

__Campo 09 – Valor da Operação / Item__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Valor da Operação / Item na tabela SAFX147\.

__Tabela: __SAFX147

__Item: __09

__Nome do Campo:__ VLR\_OPER

__Descrição: __Valor da operação

__Tipo:__ N

__Tamanho: __015V002

__Comentário: __

Valor da Operação ou do Item do documento fiscal de acordo com as operações do Registro:  
Receitas Financeiras auferidas no período;  
Receitas auferidas de Juros sobre o Capital Próprio;  
Receitas de Aluguéis auferidas no período;  
Despesas de Aluguéis de prédios, máquinas e equipamentos utilizados nas atividades da empresa;  
Contraprestações de Arrendamento Mercantil;  
Outros bens e serviços utilizados como insumos, não relacionados nos Blocos A, C e D\.

OS3169\-Dw2

__RN10__

__Campo 10 – Valor da Base de cálculo do PIS__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Valor da Base de cálculo do PIS na tabela SAFX147\.

__Tabela: __SAFX147

__Item: 1__0

__Nome do Campo:__ VLR\_BASE\_PIS

__Descrição: __Valor da Base de cálculo do PIS

__Tipo:__ N	

__Tamanho: __015V002

__Comentário:__

Valor da Base de cálculo do PIS/PASEP de acordo com a operação\.

OS3169\-Dw2

__RN11__

__Campo 11 – Alíquota do PIS__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Alíquota do PIS na tabela SAFX147\.

__Tabela: __SAFX147

__Item: __11

__Nome do Campo:__ VLR\_ALIQ\_PIS

__Descrição:__ Alíquota do PIS

__Tipo:__ N

__Tamanho: __008V004

__Comentário: __

Alíquota do PIS/PASEP \(em percentual\) de acordo com a tributação da empresa, informado no lançamento ou documento fiscal\.

OS3169\-Dw2

__RN12__

__Campo 12 – Valor do PIS__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Valor do PIS na tabela SAFX147\.

__Tabela: __SAFX147

__Item: __12

__Nome do Campo:__ VLR\_PIS

__Descrição:__ Valor do PIS

__Tipo:__ N

__Tamanho: __015V002

__Comentário: __

Valor do PIS/PASEP calculado pela multiplicação dos campos Valor da Base de cálculo do PIS/PASEP \* Alíquota do PIS/PASEP informado no lançamento ou documento fiscal\.

OS3169\-Dw2

__RN13__

__Campo 13 – Valor da Base de Cálculo da COFINS__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Valor da Base de Cálculo da COFINS na tabela SAFX147\.

__Tabela: __SAFX147

__Item: __13

__Nome do Campo:__ VLR\_BASE\_COFINS

__Descrição: __Valor da Base de Cálculo da COFINS 

__Tipo:__ N	

__Tamanho: __015V002

__Comentário: __

Valor da Base de cálculo da COFINS de acordo com a operação informado no lançamento ou documento fiscal\.

OS3169\-Dw2

__RN14__

__Campo 14 – Alíquota da COFINS__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Alíquota da COFINS na tabela SAFX147\.

__Tabela: __SAFX147

__Item: __14

__Nome do Campo:__ VLR\_ALIQ\_COFINS

__Descrição: __Alíquota da COFINS

__Tipo:__ N

__Tamanho: __008V004

__Comentário: __

Alíquota da COFINS \(em percentual\) de acordo com a tributação da empresa informada nos lançamentos ou documento fiscal\.

OS3169\-Dw2

__RN15__

__Campo 15 – Valor da COFINS__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Valor da COFINS na tabela SAFX147\.

__Tabela: __SAFX147

__Item: __15

__Nome do Campo:__ VLR\_COFINS

__Descrição: __Valor da COFINS

__Tipo:__ N

__Tamanho: __015V002

__Comentário: __

Valor da COFINS calculado pela multiplicação dos campos Valor da Base de cálculo da COFINS \*  Alíquota da COFINS informada nos lançamentos ou documento fiscal\.

OS3169\-Dw2

__RN16__

__Campo 16 – Indicador da Origem do Crédito__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Indicador da Origem do Crédito na tabela SAFX147\.

__Tabela: __SAFX147

__Item: __16

__Nome do Campo:__ IND\_ORIGEM\_CRED

__Descrição: __Indicador da Origem do Crédito

__Tipo:__ A

__Tamanho: __001

__Comentário: __

Indicador da origem do bem incorporado ao ativo imobilizado, gerador de crédito de acordo com o Manual de leiaute EFD\-PIS/COFINS:  
    0 – Aquisição no Mercado Interno  
    1 – Aquisição no Mercado Externo \(Importação\)

OS3169\-Dw2

__RN17__

__Campo 17 – Código da conta analítica debitada/creditada __

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Código da conta analítica debitada/creditada na tabela SAFX147\.

__Tabela: __SAFX147

__Item: __17

__Nome do Campo:__ COD\_CONTA

__Descrição: __Código da conta analítica debitada/creditada

__Tipo:__ A

__Tamanho: __070

__Comentário: __

Conta Contábil referente ao Imposto, utilizada para Contabilização, de acordo com a Tabela     de Plano de Contas \(SAFX2002\)\. 

OS3169\-Dw2

__RN18__

__Campo 18 – Código do centro de custos__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Código do centro de custos na tabela SAFX147\.

__Tabela: __SAFX147

__Item: __18

__Nome do Campo:__ COD\_CUSTO

__Descrição: __Código do centro de custos

__Tipo:__ A

__Tamanho: __020

__Comentário: __

O Código deve estar registrado na Tabela de Centro de Custos \(SAFX2003\)\.

OS3169\-Dw2

__RN19__

__Campo 19 – Descrição complementar do Documento/Operação__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Descrição complementar do Documento/Operação na tabela SAFX147\.

__Tabela: __SAFX147

__Item: __19

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Descrição complementar do Documento/Operação

__Tipo:__ A

__Tamanho: __050

__Comentário: __

Descrição complementar do Documento/Operação\.

OS3169\-Dw2

__RN20__

__Campo 20 – Número do documento__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Descrição complementar do Documento/Operação na tabela SAFX147\.

__Tabela: __SAFX147

__Item: __20

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Número do documento

__Tipo:__ A

__Tamanho: __012

__Comentário: __

Número de identificação do documento/Operação se houver

__Chave Primária__

__Não Obrigatório__

OS3169\-DW3A

__RN21__

__Campo 21 – Série do documento__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Descrição complementar do Documento/Operação na tabela SAFX147\.

__Tabela: __SAFX147

__Item: __21

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Série do documento/Operação

__Tipo:__ A

__Tamanho: __003

__Comentário: __

Informar a série do documento/Operação se houver

__Chave Primária__

__Não Obrigatório__

OS3169\-DW3A

__RN22__

__Campo 22 – Subsérie do Documento__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Descrição complementar do Documento/Operação na tabela SAFX147\.

__Tabela: __SAFX147

__Item: __22

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Subsérie do documento/Operação

__Tipo:__ A

__Tamanho: __003

__Comentário: __

Informar a subsérie do documento/Operação se houver

__Chave Primária__

__Não Obrigatório__

OS3169\-DW3A

__RN23__

__Campo 23 – Número do Lançamento__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Descrição complementar do Documento/Operação na tabela SAFX147\.

__Tabela: __SAFX147

__Item: __23

__Nome do Campo:__ NUM\_LANCTO

__Descrição: __Número do lançamento

__Tipo:__ A

__Tamanho: __040

__Comentário: __

Informar o número de lançamento destinado à identificação do conjunto de registros representativos do documento/operação\.

__Chave Primária__

__Não Obrigatório__

OS3169\-DW3A/__ OS4579__

__RN24__

__Campo 24 – Código da Natureza da Receita__

__Tabela: __SAFX147

__Item: __24

__Nome do Campo:__ COD\_NAT\_REC

__Descrição: __Código da Natureza da Receita

__Tipo:__ N

__Tamanho: __003

__Comentário: __

Informar o código da Natureza da Receita  da operação/serviço não tributada ou não sujeita ao pagamento da contribuição PIS/COFINS, conforme as tabelas externas da EFD PIS/PASEP–COFINS, disponibilizadas pela RFB\. 

Obs\. A informação desse campo será utilizada no campo 02 do registro M410 da EFD PIS/PASEP\-COFINS\.

__Não Obrigatório__

__Consistência:__

Verificar se o código da natureza da receita do registro que está sendo importado, existe na Tabela de Código da Natureza da Receita \(TACES72\) \- DWT\_NAT\_REC\. 

Se pelo menos um dos códigos de Situação Tributária PIS ou COFINS \(COD\_SITUACAO\_PIS, COD\_SITUACAO\_COFINS \) estiverem preenchidos, então:

A consulta na Tabela de Código da Natureza da Receita \(TACES72\) \- DWT\_NAT\_REC, deve consider os critérios:

\- Código da Natureza da Receita = ao código que está sendo importado;

\- Data Início Validade <=  a Data da Operação \(DATA\_OPER\) importada;

\- Código do CST PIS/COFINS:

Se Código Situação Tributária PIS \(COD\_SITUACAO\_PIS\) estiver preenchido, então:

Código do CST PIS/COFINS = Código Situação Tributária PIS \(COD\_SITUACAO\_PIS\);

Senão

Se Código Situação Tributária COFINS \(COD\_SITUACAO\_COFINS\) estiver preenchido, então:

Código do CST PIS/COFINS = ao Código Situação Tributária COFINS \(COD\_SITUACAO\_COFINS\);

Recuperar o registro de maior validade que atenda aos critérios acima\.

Se os códigos de Situação Tributária PIS e COFINS \(COD\_SITUACAO\_PIS, COD\_SITUACAO\_COFINS\) NÃO estiverem preenchidos, então:

A consulta na Tabela de Código da Natureza da Receita \(TACES72\) \- DWT\_NAT\_REC, deve considerar os critérios:

\- Código da Natureza da Receita = ao código que está sendo importado;

\- Data Início Validade <=  a Data da Operação \(DATA\_OPER\) importada;

Recuperar o registro de maior validade que atenda aos critérios acima\.

Caso o código de natureza da receita não exista na tabela, exibir a seguinte mensagem o Relatório de Erros da Importação, e não importar o registro\.

*92141 \- Natureza da Receita nao Cadastrada\.*

__MFS36163__

__RN25__

__Campo 25 \- Código da SCP__

Alterar a rotina de importação para que seja considerado o novo campo:

Tabela: SAFX147

Item: 25

__Nome do Campo__: COD\_SCP

__Descrição: __Código da SCP

Tipo: A

Tamanho: 014

Comentário: Código da Sociedade em Conta de Participação

__Consistência:__

Deverá existir um cadastro correspondente na SAFX2057 para o código informado\. Caso não exista, retornar a mensagem: “Cadastro da SCP não encontrado”\.

__OS4316__

__RN26__

__Campo Código Situação Tributária PIS__

Item: 26

Nome do Campo: COD\_SITUACAO\_PIS

Descrição: Código Situação Tributária PIS

Tipo: N

Tamanho: 002

Comentário: Informar o código da situação tributária indicado para PIS, conforme tabela de Códigos Situação Tributária \(TACES65\)\.

Não Obrigatório

__Consistência__:

Verificar se o código da situação PIS que está sendo importado, existe na Tabela de Códigos Situação Tributária \(TACES65\) \- Y2027\_SIT\_TRIBUTARIA, com os seguintes critérios:

\- Data Início Validade menor ou igual a Data da Operação \(campo DATA\_OPER\)\.

\- Indicador  = 1 \- PIS

Caso o mesmo não exista, exibir a seguinte mensagem o Relatório de Erros da Importação, e não importar o registro\.

*91627 \- Codigo da Situacao Tributaria PIS inexistente ou invalido para a data do documento\.*

__MFS36163__

__RN27__

__Campo Código Situação Tributária COFINS__

Item: 27

Nome do Campo: COD\_SITUACAO\_COFINS

Descrição: Código Situação Tributária COFINS

Tipo: N

Tamanho: 002

Comentário: Informar o código da situação tributária indicado para COFINS, conforme tabela de Códigos Situação Tributária \(TACES65\)\.

Não Obrigatório

__Consistência:__

Verificar se o código da situação PIS que está sendo importado, existe na Tabela de Códigos Situação Tributária \(TACES65\) \- Y2027\_SIT\_TRIBUTARIA, com os seguintes critérios:

\- Data Início Validade menor ou igual a Data da Operação \(campo DATA\_OPER\)\.

\- Indicador  = 2 \- COFINS

Caso o mesmo não exista, exibir a seguinte mensagem o Relatório de Erros da Importação, e não importar o registro\.

*91628 \- Codigo da Situacao Tributaria COFINS inexistente ou invalido para a data do documento\.*

__MFS36163__

