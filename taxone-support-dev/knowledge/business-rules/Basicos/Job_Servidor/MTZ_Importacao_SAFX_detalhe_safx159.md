# MTZ_Importacao_SAFX_detalhe_safx159

- **Fonte:** MTZ_Importacao_SAFX_detalhe_safx159.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 52 KB

---

    

# Módulo Job Servidor – Importação – Detalhe do Crédito/Contribuição Extemporâneo – Itens Notas Fiscais de Serviços

#   \(SAFX159\)

*\(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX159, conforme o Manual de Layout, o que facilita a consulta\)*

*\(Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00\)*

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3169\-DW11

Criação da SAFX159

Criação da tabela de detalhe de crédito/contribuição extemporâneo do item das notas fiscais de serviços “filha’’ da SAFX09 para atendimento do registro 1101, 1102, 1501, 1502, 1200, 1210, 1600 e 1610 do Bloco 1 do Anexo Único do Ato Declaratório executivo COFINS Nº 31, de 08 de julho de 2010

21/02/2011

CH110004

Alteração

Ao importar a SAFX159 , o campo \(IND\_PIS\_COFINS\_EXTEMP\) da SAFX09, deve ser alterado para S automaticamente\. 

22/08/2011

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN00__

__Regras gerais__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alterados para contemplar os campos descritos abaixo na tabela SAFX159\.

Na importação deve conter a seguinte regra de importação:

__Validação:__

Não existe registro na X09 com a mesma chave \(Empresa, Estabelecimento, Data da Escrita Fiscal, Movimento Entrada/Saída, Normal ou Devolução, Tipo do Documento, Indicador da Pessoa Física/Jurídica, Código do Destinatário/Emitente, Número do Documento Fiscal, Série, Sub Série, código do Serviço, Item do Documento Fiscal, Data de Lançamento do Crédito/Débito, Crédito/Débito Extemporâneo\) do registro que está sendo importado na SAFX159\.

__Mensagem:__

Não existe item do documento fiscal de mercadoria para esse detalhe de crédito/débito extemporâneo\.

__Solução: __

Importar a SAFX09 para esse item de nota fiscal de serviços, com competência menor à competência informada na SAFX159\.

OS3169\-DW14

__RN01__

__Campo 01 \- Código da empresa__

 

__Item: __01

__Nome do Campo: __COD\_EMPRESA

__Descrição: __Código da empresa

__Tipo:__ A

__Tamanho: __003

__Comentário: __Campo destinado ao código da Empresa\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN02__

__Campo 02 \- Código do estabelecimento__

__Item: __02

__Nome do Campo: __COD\_ESTAB

__Descrição: __Código do estabelecimento

__Tipo:__ A

__Tamanho: __006

__Comentário: __Campo destinado ao código do Estabelecimento\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN03__

__Campo 03 \- Data da Escrita Fiscal__

__Item: 03__

__Nome do Campo: __DATA\_FISCAL

__Descrição:__ Data da Escrita Fiscal

__Tipo__: N

__Tamanho:__ 008

C__omentário__:

Para as Notas Fiscais de:

Entradas: Data do Recebimento do Documento\.

Saídas: Data de Emissão do Documento\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN04__

__Campo 04 \- Movimento Entrada/Saída__

__Item: __04

__Nome do Campo: __MOVTO\_E\_S

__Descrição: __Movimento Entrada/Saída

__Tipo:__ A

__Tamanho: __001

__Comentário: __

Informar de acordo com:

1 \- Documento de Entrada, Documento de Terceiros;

2 \- Documento de Entrada emitida pelo Estabelecimento, acolhendo Notas de Produtores Agropecuários;

3 \- Documento de Entrada emitida pelo Estabelecimento, por retorno de mercadorias não entregues ao destinatário;                                                                                                                                        4 \- Documento de Entrada emitida pelo Estabelecimento, outros motivos legais;

5 \- Documento de Entrada emitida pelo Estabelecimento, globalizando Conhecimento de Frete ou Material Uso/Consumo;

9 \- Documento de Saída\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN05__

__Campo 05 \- Normal ou Devolução__

__Item:__ 05

__Nome do Campo: __NORM\_DEV

__Descrição: __Normal ou Devolução 

__Tipo:__ A

__Tamanho: __001

__Comentário: __

Qualifica o motivo da Entrada / Saída:

1 \- Normal;

2 – Devolução

\.__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN06__

__Campo 06 – Tipo do Documento__

__Item: 06__

__Nome do Campo: __COD\_DOCTO

__Descrição: __Tipo do Documento

__Tipo:__ A

__Tamanho: __005

__Comentário:__

Tipo de Documento de acordo com a Tabela de Tipo de Documento \(SAFX2005\) \- \(Duplicata,  Fatura, Nota Fiscal Fatura, Recibo e etc\.\)\.\.

__Chave Primária__

__Obrigatório__ 

OS3169\-DW14

__RN07__

__Campo 07 – Indicador da Pessoa Fis/Jur Adquirente__

__Item: __07

__Nome do Campo: __IND\_FIS\_JUR 

__Descrição: __Indicador da Pessoa Física/Jurídica 

__Tipo:__ A

__Tamanho: __001

__Comentário: __

Campo que deverá ser preenchido com o Indicador da Pessoa Física/Jurídica \(SAFX04\) relacionada, conforme segue:

1 \- Fornecedor;

2 \- Cliente;

3 \- Estabelecimento;

4 \- Transportadora;

5 \- Cliente/Fornecedor/Transportadora\.

__Chave Primária__

__Obrigatório__ 

OS3169\-DW14

__RN08__

__Campo 08 – Código da Pessoa Fis/Jur Adquirente__

__Item: __08

__Nome do Campo: __COD\_FIS\_JUR

__Descrição: __Código do Destinatário/Emitente

__Tipo:__ A

__Tamanho: __014

__Comentário: __

Preencher com Indicador da Pessoa Fis/Jur do documento fiscal da SAFX07\. Preencher de acordo com a Tabela de Pessoas Física/Jurídicas \(SAFX04\)\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN09__

__Campo 09 – Número do Documento Fiscal__

__Item: __09

__Nome do Campo: __NUM\_DOCFIS

__Descrição: __

__Tipo:__ A

__Tamanho: __012

__Comentário: __

Neste Campo deve ser informado o Número do Documento Fiscal\.\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN10__

__Campo 10 \- Série do Documento Fiscal__

__Item: __10

__Nome do Campo: __SERIE\_DOCFIS 

__Descrição: Série do Documento Fiscal__

__Tipo:__ A

__Tamanho: __003

__Comentário: __

A ausência deste dado deve ser representada com espaços ou outra informação não nula\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN11__

__Campo 11 \- Subsérie do Documento Fiscal__

__Item: __11

__Nome do Campo: __SUB\_SERIE\_DOCFIS

__Descrição: __Subsérie do Documento Fiscal

__Tipo:__ A

__Tamanho: __002

__Comentário: __

A ausência deste dado deve ser representada com espaços ou outra informação não nula\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN12__

__Campo 12 \- Código de Serviço__

__Item: __12

__Nome do Campo: __COD\_SERVICO

__Descrição: __Código de Serviço

__Tipo:__ A

__Tamanho: __004

__Comentário: __

Preencher de acordo com a Tabela de Código de Serviços \(SAFX2018\)

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN13__

__Campo 13 \- Item Documento Fiscal__

__Item: __13

__Nome do Campo: __NUM\_ITEM

__Descrição: __Item Documento Fiscal 

__Tipo:__ N

__Tamanho: __005

__Comentário: __

Informar o número do item da Nota Fiscal\. Apesar do campo possibilitar o tamanho de 05 posições, ou seja, notas fiscais com até 99\.999 itens, quanto da geração dos meios magnéticos \(Sintegra, IN86, IN89, SEF\-PE, etc\.\.\.\) o sistema irá considerar somente 03 posições, ou seja, notas fiscais com até 999 itens\. Esta consideração deve\-se ao fato dos layouts destes meios magnéticos estarem solicitando somente 03 posições\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN14__

__Campo 14 \- Data de Lançamento do Crédito/Débito__

__Item:__ 14

__Nome do Campo: __DAT\_LANC\_PIS\_COFINS

__Descrição: __Data de Lançamento do Crédito/Débito

__Tipo:__ N

__Tamanho: __008

__Comentário: __

Informar a data de lançamento dos valores de crédito ou débito de PIS/COFINS informados no documento fiscal

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN15__

__Campo 15 \- Crédito/Débito Extemporâneo__

__Item: __15

__Nome do Campo: __IND\_PIS\_COFINS\_EXTEMP

__Descrição: __Crédito/Débito Extemporâneo

__Tipo:__ A

__Tamanho: __001

__Comentário: __

Campo utilizado para identificar se os valores de crédito ou débito dos valores de PIS/COFINS do documento fiscal serão considerados extemporâneos\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN15\.01__

Ao importar o documento na SAFX159, o campo 82 \(IND\_PIS\_COFINS\_EXTEMP\) da SAFX09 \(referente à mesma nota\), deve ser alterado para ‘S’ automaticamente\. 

CH110004

__RN16__

__Campo 16 \- Natureza da Base de Crédito__

__Item:__ 16

__Nome do Campo: __Será definido pelo A&D__ __

__Descrição: __Natureza da Base de Crédito

__Tipo:__ N

__Tamanho: __002

__Comentário: __Informar o código da natureza da base de crédito, referenciada  no Manual do Leiaute do EFD PIS/PASEP\- COFINS

__Não Obrigatório__

OS3169\-DW14

__RN17__

__Campo 17 \- Quantidade de Serviços:__

__Item: __17

__Nome do Campo: __QUANTIDADE

__Descrição: Quantidade de Serviços__

__Tipo:__ N

__Tamanho:__ 011V006

__Comentário: __

Informar a quantidade de serviços que irá apropriar o crédito extemporâneo\.

__Obrigatório__

__Validação:__

A quantidade informada no campo 17 da SAFX159 que está sendo importada maior que a quantidade informada no campo 19 da X09\. 

__Mensagem:__

 “A soma da quantidade do detalhe do crédito/contribuição extemporâneo do item do documento fiscal de serviços ‘’X159’’ deve ser menor ou igual à quantidade do item informado na X09 ‘’\.

OS3169\-DW14

__RN18__

__Campo 18 \- Código da Situação Tributária do PIS/PASEP__

__Item: __18

__Nome do Campo:__ COD\_SITUACAO\_PIS

__Descrição: __Código da Situação Tributária do PIS/PASEP

__Tipo:__ N

__Tamanho: __002

__Comentário: __

Informar o código da situação tributária do PIS, conforme tabela da Receita Federal\.

__Chave Primária__

__Obrigatória__

OS3169\-DW14

__RN19__

__Campo 19 \- Base de cálculo do PIS__

__Item:__ 19

__Nome do Campo:__ VLR\_BASE\_PIS

__Descrição: __Base de cálculo do PIS

__Tipo:__ N	

__Tamanho: __015V002

__Comentário:__

Valor da Base de cálculo do PIS/PASEP de acordo com a operação\.

__Não Obrigatório__

OS3169\-DW14

__RN20__

__Campo 20 \- Alíquota do PIS__

__Item: 20__

__Nome do Campo:__ VLR\_ALIQ\_PIS

__Descrição:__ Alíquota PIS

__Tipo:__ N

__Tamanho: __003V004

__Comentário: __

 Informar Alíquota do PIS/PASEP \(em percentual\) da operação

__Não Obrigatório__

OS3169\-DW14

__RN21__

__Campo 21 \- Valor do PIS__

__Item: __21

__Nome do Campo:__ VLR\_PIS

__Descrição:__ Valor do PIS

__Tipo:__ N

__Tamanho: __015V002

__Comentário: __

Informar Valor do PIS/PASEP, calculado pela multiplicação dos campos: Base de Cálculo PIS x Alíquota PIS\. 

__Não Obrigatório__

OS3169\-DW14

__RN22__

__Campo 22 \- Código da Situação Tributária COFINS__

__Item: __22

__Nome do Campo:__ COD\_SITUACAO\_COFINS

__Descrição: __Código da Situação Tributária COFINS

__Tipo:__ N

__Tamanho: __002

__Comentário: __

Informar o código da situação tributária da COFINS, conforme tabela da Receita Federal\.

__Chave Primária__

__Obrigatória__

OS3169\-DW14

__RN23__

__Campo 23 \- Base de cálculo da COFINS__

__Item:__ 23

__Nome do Campo:__ VLR\_BASE\_COFINS

__Descrição: __Base de cálculo da COFINS

__Tipo:__ N	

__Tamanho: __015V002

__Comentário:__

Valor da Base de cálculo da COFINS de acordo com a operação\.

__Não Obrigatório__

OS3169\-DW14

__RN24__

__Campo 24 \- Alíquota da COFINS__

__Item: __24

__Nome do Campo:__ VLR\_ALIQ\_COFINS

__Descrição:__ Alíquota COFINS

__Tipo:__ N

__Tamanho: __003V004

__Comentário: __

 Informar  alíquota da COFINS \(em percentual\) da operação

__Não Obrigatório__

OS3169\-DW14

__RN25__

__Campo 25 \- Valor da COFINS__

__Item: __25

__Nome do Campo:__ VLR\_PIS

__Descrição:__ Valor do PIS

__Tipo:__ N

__Tamanho: __015V002

__Comentário: __

Informar Valor da COFINS, calculado pela multiplicação dos campos: Base de Cálculo COFINS x Alíquota COFINS\. 

__Não Obrigatório__

OS3169\-DW14

__RN26__

__Campo 26 \- Conta Contábil:__

__Item: __26

__Nome do Campo:__ COD\_CONTA

__Descrição: __Código da conta analítica debitada/creditada

__Tipo:__ A

__Tamanho: __070

__Comentário: __

Conta Contábil referente ao Imposto, utilizada para Contabilização, de acordo com a Tabela de Plano de Contas \(SAFX2002\)\. 

__Não Obrigatório__

OS3169\-DW14

__RN27__

__Campo 27 \- Centro de Custo:__

__Item:__ 27

__Nome do Campo:__ COD\_CUSTO

__Descrição: __Código do centro de custos

__Tipo:__ A

__Tamanho: __020

__Comentário: __

O Código deve estar registrado na Tabela de Centro de Custos \(SAFX2003\)\.

__Não Obrigatório__

OS3169\-DW14

__RN28__

__Campo 28 \- Descrição complementar__

__Item: __28

__Nome do Campo:__ DESC\_COMPL

__Descrição: __Descrição complementar

__Tipo:__ A

__Tamanho: __255

__Comentário: __

Descrição complementar do Documento/Operação\.

__Não Obrigatório__

OS3169\-DW14

