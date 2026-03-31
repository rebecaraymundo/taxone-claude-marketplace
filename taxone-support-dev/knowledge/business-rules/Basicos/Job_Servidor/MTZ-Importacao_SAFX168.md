# MTZ-Importacao_SAFX168

- **Fonte:** MTZ-Importacao_SAFX168.docx
- **Modificado:** 2022-03-31
- **Tamanho:** 49 KB

---

__    __

# Módulo Job Servidor – Importação Crédito Extemporâneo \- Documentos e Operações de Períodos Anteriores – \(1101/1501\)

# \(EFD\-PIS/PASEP – COFINS\) \- \(SAFX168\)

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3169\-GE24

Criação da SAFX 168

Será criada uma tabela para atendimento do Bloco 1 registros 1101 e 1501, da EFD – PIS/PASEP COFINS, estes registros são para informação de créditos de documentos/operação extemporâneo

08/08/2011

OS3903

Alteração campo 17

Retiradas as críticas de obrigatoriedade do campo 17\-Código Fiscal \(ver __RN17__\)

12/06/2014

MFS\-65742

Melhoria de mensagem de validação

Melhoria na mensagem 92292\. Inserido exemplo de preenchimento

29/03/2022

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN00__

__Regras gerais__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar os campos descritos abaixo na tabela SAFX168\.

OS3169\-GE24

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

OS3169\-GE24

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

OS3169\-GE24

__RN03__

__Campo 03  – Mês/Ano Competência__

__Item:__ 03

__Nome do Campo:__ Será definido pelo A&D

__Descrição:__ Mês / Ano de Competência no formato MMAAAA

__Tipo:__ N

__Tamanho:__ 006

__Comentário:__ Informar o Mês e Ano em que os Créditos Extemporâneos serão declarados

__Chave Primária__

__Obrigatório__

OS3169\-GE24

__RN04__

__Campo 04 – Indicador da Pessoa Física/Jurídica__

__Item: __04

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Código do participante

__Tipo:__ A

__Tamanho: __001

__Comentário: __Indicador da pessoa remetente/destinatária do documento fiscal registrada no cadastro de pessoas físicas/jurídicas \(SAFX04\)\.Campo que deverá ser conforme segue:

1 \- Fornecedor;

2 \- Cliente;

3 \- Estabelecimento;

4 \- Transportadora;

5 \- Cliente/Fornecedor/Transportadora\.

__Chave Primária__

__Não Obrigatório__

OS3169\-GE24

__RN05__

__Campo 05 \- Código da Pessoa Física/Jurídica__

__Item: __05

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Código do participante

__Tipo:__ A

__Tamanho: __014

__Comentário: __Código da pessoa remetente/destinatária do documento fiscal registrada no cadastro de pessoas físicas/jurídicas \(SAFX04\)\.

__Chave Primária__

__Não Obrigatório__

OS3169\-GE24

__RN06__

__Campo 06 \- Indicador do Produto__

__Item: __06

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Indicador de Produto

__Tipo:__ A

__Tamanho: __001

__Comentário: __Informar o indicador do produto de acordo com a tabela de produtos \(SAFX2013\):

1 \- Produto Acabado;

2 \- Insumos;

3 \- Embalagem;

4 \- Consumo;

5 \- Outros;

6 \- Em Elaboração;

7 \- Intermediário;

8 \- Miscelâneas\.

__Chave Primária__

__Não Obrigatório, __porém caso o Indicador do Produto \(campo 06\) e o Código do Produto \(campo 07\) estejam preenchidos em conjunto com o Código do Serviço \(campo 08\), deverá ser exibida a seguinte mensagem de erro no log de Importação: “Documento referente à Crédito Extemporâneo não pode possuir Produto e Serviço simultaneamente\.”

OS3169\-GE24

__RN07__

__Campo 07 \- Código do Produto__

__Item: 07__

__Nome do Campo: __Será definido pelo A&D

__Descrição:__ Código do Item

__Tipo__: A

__Tamanho: __035

C__omentário__: Código do produto de acordo com a tabela de produtos \(SAFX2013\)\.

__Chave Primária__

__Não Obrigatório, __porém caso o Indicador do Produto \(campo 06\) e o Código do Produto \(campo 07\) estejam preenchidos em conjunto com o Código do Serviço \(campo 08\), deverá ser exibida a seguinte mensagem de erro no log de Importação: “Documento referente à Crédito Extemporâneo não pode possuir Produto e Serviço simultaneamente\.”

OS3169\-GE24

__RN08__

__Campo 08 \- Código Serviço__

__Item: 08__

__Nome do Campo: __Será definido pelo A&D

__Descrição:__ Código do serviço

__Tipo__: A

__Tamanho: __004

__Comentário__: Código do serviço de acordo com a tabela de cadastro de serviços \(SAFX2018\)\.

__Chave Primária__

__Não Obrigatório, __porém caso o Indicador do Produto \(campo 06\) e o Código do Produto \(campo 07\) estejam preenchidos em conjunto com o Código do Serviço \(campo 08\), deverá ser exibida a seguinte mensagem de erro no log de Importação: “Documento referente à Crédito Extemporâneo não pode possuir Produto e Serviço simultaneamente\.”

OS3169\-GE24

__RN09__

__Campo 09 \- SER__

__Item: 09__

__Nome do Campo: Será definido pelo A&D__

__Descrição: __Série do documento fiscal

__Tipo: A__

__Tamanho: __003

__Comentário: __informar a serie do documento fiscal

__Chave primaria__

__Não Obrigatório__

OS3169\-GE24

__RN10__

__Campo 10\- SUB SER__

__Item: __10

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Subsérie do documento fiscal

__Tipo: __A

__Tamanho: __002

__Comentário: __informar a subsérie do documento fiscal

__Chave primaria__

__Não Obrigatório__

OS3169\-GE24

__RN11__

__Campo 11 – NUM DOC __

__Item: __11

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Numero do documento

__Tipo: __N

__Tamanho: __012

__Comentário: __Número do documento fiscal

__Chave primaria__

__Não Obrigatório__

OS3169\-GE24

__RN12__

__Campo 12– DT OPER__

__Item: __12

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Data da operação 

__Tipo: __N

__Tamanho: __008

__Comentário:__ inserir data da operação no formato \(DDMMAAAA\)

__Chave Primária__

__Obrigatório__

OS3169\-GE24

__RN13__

__Campo 13 – Nº Item__

__Item: __13

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Número do item do documento fiscal\.

__Tipo: __N

__Tamanho: __005

__Comentário: __Número do item constante do documento fiscal, quando for o caso\.

__Chave Primária__

__Não Obrigatório__

OS3169\-GE24

__RN14__

__Campo 14 – Modelo de documento__

__Item: __14

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Mês/Ano em que foi registrado o documento/operação

__Tipo: __N

__Tamanho: __002

__Comentário: __Código do modelo do documento fiscal conforme tabela de cadastro de modelos \(SAFX2024\)\.

__Não Obrigatório__

OS3169\-GE24

__RN15__

__Campo 15– CHV NFE__

__Item: __15

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Chave da nota fiscal eletrônica

__Tipo: __N

__Tamanho: __080

__Comentário: __se houver Nota fiscal eletrônica informar a chave

__Não Obrigatório__

OS3169\-GE24

__RN16__

__Campo 16\- VL OPER__

__Item: __16

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Valor da operação

__Tipo: __N \(Decendial\)

__Tamanho: __015V002

__Comentário: __Informar valor total da operação, 

__Obrigatório__

OS3169\-GE24

__RN17__

__Campo 17 \- CFOP__

__Item: __17

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Código fiscal de operação e prestação

__Tipo: __N

__Tamanho: __004

__Comentário: __informar o CFOP referente a operação

__Obrigatório__

__Não obrigatório__

__Alteração da OS3903 __– O campo não será mais obrigatório, desta forma, *não* será mais gerada mensagem de erro quando o campo *não* for preenchido\. Quando preenchido, permanece a crítica original  que  verifica a existência do código informado  na Tabelas dos Códigos Fiscais \(SAFX2012\), e caso não exista, é gravada a mensagem de erro 90594 no log  \(“CFOP \- Código de Operação  e Prestação não Cadastrado”\)  e o registro não é importado\.  

OS3169\-GE24

__RN18__

__Campo 18– NAT BC CRED__

__Item: __18

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Código da base de calculo do credito

__Tipo: __N

__Tamanho: __002

__Comentário: __Informar neste campo o código da base de cálculo do crédito, conforme a Tabela “4\.3\.7 – Base de Cálculo do Crédito” referenciada no Manual do Leiaute da EFD\-PIS/Cofins

__Obrigatório__

OS3169\-GE24

__RN19__

__Campo 19 – IND ORIG CRED__

__Item: __19

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Indicador da origem do crédito

__Tipo: __A

__Comentário: __deve ser indicado a origem do credito, sendo:

0 – Operação no mercado interno

1 – Operação de importação

__Tamanho: __001 

__Obrigatório__

OS3169\-GE24

__RN20__

__Campo 20– CST PIS__

__Item:__ 20

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Código da Situação Tributária referente ao PIS/PASEP__ __

__Tipo: __N

__Comentário: __Informar o CST referente ao PIS/PASEP, conforme tabela referenciada no Manual Leiaute da EFD\-PIS/Cofins__\. __

__Tamanho: __002

__Chave Primária__

__Obrigatório__

OS3169\-GE24

__RN21__

__Campo 21 – VL BC PIS__

__Item: __21

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Valor base de Cálculo PIS/PASEP 

__Tipo: __N

__Tamanho: __015V002

__Comentário: __informar neste campo a base de cálculo do PIS/PASEP referente à operação/item, para fins de apuração do crédito\.

__Não Obrigatório__, porém caso tenha sido preenchido o campo de Alíquota em Percentuais, este campo deverá ser informado, se não, emitir mensagem no log de importação: Se Alíquota em Percentuais é informado, deverá ser preenchido o campo Valor Base PIS\.

OS3169\-GE24

__RN22__

__Campo 22 – Quantidade – Base PIS/PASEP__

__Item: __22

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Quantidade de base de Cálculo PIS/PASEP 

__Tipo: __N

__Tamanho: __015V003

__Comentário: __informar neste campo a quantidade de base cálculo do PIS/PASEP referente à operação/item, para fins de apuração do crédito\.

__Não Obrigatório, __porém caso tenha sido preenchido o campo Alíquota em Reais, este campo deverá ser informado, se não, emitir mensagem no log de importação: Se Alíquota em Reais é informado, deverá ser preenchido o campo Quantidade de Base PIS\.

OS3169\-GE24

__RN23__

__Campo 23 \- ALIQ PIS__

__Item: __23

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Alíquota do PIS/PASEP em porcentagem

__Tipo: __N

__Tamanho: __003V004

__Comentário: __informar neste campo a alíquota aplicável para fins de apuração do crédito, deve ser informado somente alíquota em Porcentagem

__Chave Primária__

__Não Obrigatório, __porém caso tenha sido preenchido o campo Valor Base Pis, este campo deverá ser informado, se não, emitir mensagem no log de importação: Se Valor Base PIS  é informado, deverá ser preenchido o campo Alíquota em Percentuais\.

OS3169\-GE24

__RN24__

__Campo 24\- ALIQ PIS\_REAIS__

__Item: __24

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Alíquota do PIS/PASEP em Reais

__Tipo: __N

__Tamanho: __015V004

__Comentário: __informar neste campo a alíquota aplicável para fins de apuração do crédito, deve ser informado somente alíquota em Moeda REAL

__Não Obrigatório, __porém caso tenha sido preenchido o campo Quantidade Base Pis, este campo deverá ser informado, se não, emitir mensagem no log de importação: Se Quantidade Base PIS, é informado, deverá ser preenchido o campo Aliquota PIS em Reais\.

OS3169\-GE24

__RN25__

__Campo 25– VL PIS__

__Item: __25

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Valor de credito de PIS/PASEP

__Tipo: __N

__Tamanho: __015V002

__Comentário: __Informar o valor do crédito do PIS/PASEP referente à operação/item escriturado neste registro\.

__Obrigatório__

OS3169\-GE24

__RN26__

__Campo 26 – CST COFINS__

__Item:__ 26

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Código da Situação Tributária referente ao COFINS

__Tipo: __N

__Comentário: __Informar o CST referente ao COFINS, conforme tabela referenciada no Manual Leiaute da EFD\-PIS/COFINS__\. __

__Tamanho: __02

__Chave Primária__

__Obrigatório__

OS3169\-GE24

__RN27__

__Campo 27 – VL BC COFINS__

__Item: __27

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Valor base de Cálculo COFINS 

__Tipo: __N

__Tamanho: __015V002

__Comentário: __informar neste campo a base de cálculo do COFINS referente à operação/item, para fins de apuração do crédito\.

__Não Obrigatório__, porém caso tenha sido preenchido o campo de Alíquota em Percentuais, este campo deverá ser informado, se não, emitir mensagem no log de importação: Se Alíquota em Percentuais é informado, deverá ser preenchido o campo Valor Base COFINS

OS3169\-GE24

__RN28__

__Campo 28– Quantidade – Base COFINS__

__Item: __28

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Quantidade de base de COFINS

__Tipo: __N

__Tamanho: __015V003

__Comentário: __informar neste campo a quantidade de base cálculo do COFINS referente à operação/item, para fins de apuração do crédito\.

__Não Obrigatório, __porém caso tenha sido preenchido o campo Alíquota em Reais, este campo deverá ser informado, se não, emitir mensagem no log de importação: Se Alíquota em Reais é informado, deverá ser preenchido o campo Quantidade de Base COFINS\.

OS3169\-GE24

__RN29__

__Campo 29 \- ALIQ COFINS__

__Item: __29

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Alíquota do COFINS em porcentagem

__Tipo: __N

__Tamanho: __003V004

__Comentário: __informar neste campo a alíquota aplicável para fins de apuração do crédito, deve ser informado somente alíquota em Porcentagem

__Chave Primária__

__Não Obrigatório__, porém caso tenha sido preenchido o campo Valor Base COFINS, este campo deverá ser informado, se não, emitir mensagem no log de importação: Se Valor Base COFINS  é informado, deverá ser preenchido o campo Alíquota em Percentuais

OS3169\-GE24

__RN30__

__Campo 30 \- ALIQ COFINS REAIS__

__Item: __30

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Alíquota do COFINS em reais

__Tipo: __N

__Tamanho: __015V004

__Comentário: __informar neste campo a alíquota aplicável para fins de apuração do crédito, deve ser informado somente alíquota em Moeda REAL

__Não Obrigatório__, porém caso tenha sido preenchido o campo Quantidade Base COFINS, este campo deverá ser informado, se não, emitir mensagem no log de importação: Se Quantidade Base COFINS, é informado, deverá ser preenchido o campo Aliquota COFINS em Reais

OS3169\-GE24

__RN31__

__Campo 31– VL COFINS__

__Item: __31

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Valor de credito COFINS

__Tipo: __N

__Tamanho: __015V002

__Comentário: __Informar o valor do crédito do COFINS  referente à operação/item escriturado neste registro\.

__Obrigatório__

OS3169\-GE24

__RN32__

__Campo 32 – COD CTA__

__Item: __32

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Código da Conta Contábil__ __

__Tipo: __N

__Tamanho: __070

__Comentário: __informar o Código da Conta Analítica\. Exemplos: estoques, custos, despesas, etc\.

__Não Obrigatório__

OS3169\-GE24

__RN33__

__Campo 33 – COD CCUS__

__Item: __33

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Código do centro de custos

__Tipo: __N

__Tamanho: __020

__Comentário: __Informar neste campo o Código do Centro de Custo relacionado à operação, se existir\.

__Não Obrigatório__

OS3169\-GE24

__RN34__

__Campo 34 – PER ESCRIT__

__Item: __34

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Mês/Ano em que foi registrado o documento/operação, no formato MMAAAA\.

__Tipo: __N

__Tamanho: __006

__Comentário: __No caso de apropriação direta de créditos comuns, informar o Mês/Ano da Escrituração em

que foi registrado o documento/operação\. Caso contrário deixar o campo em branco

 \(Crédito pelo método da Apropriação Direta\)

__Não Obrigatório__

OS3169\-GE24

__RN35__

__Campo 35 – DESC COMPL__

__Item: __35

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Descrição complementar de documento/operação

__Tipo: __A

__Tamanho: __\- 255

__Comentário: __Neste campo pode ser informada a descrição complementar da operação ou do item\.

__Não Obrigatório__

OS3169\-GE24

__RN36__

__Validação__

- Os pares que devem ser obrigatórios são: \(Base PIS e Alíquota PIS \(em %\) ou \(Quantidade Base PIS e Alíquota PIS \(em reais\);
- Estes pares de campos devem ser exclusivos, ou seja, apenas um dos pares deve ser preenchido\.

Caso, a regra acima não seja verdadeira, exibir a mensagem: “Preenchidos campos de base/quantidade e/ou aliquota\(%\)/aliquota\(reais\) simultaneamente\. Ex\. de preenchimentos aceitos: Base PIS e Aliquota PIS\(em %\) ou Quantidade Base PIS e Aliquota PIS\(em reais\)”

As mesmas regras acima devem ser seguidas para a COFINS\.

MFS\-65742

