# MTZ-Job-Servidor-Importacao_SAFX317

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX317.docx
- **Modificado:** 2021-10-22
- **Tamanho:** 73 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS73697

Liliane Assaf

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>Definição das regras de importação, Online e Batch, dos novos campos incluídos na SAFX317\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de carga do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX126 \- Vendas com Cartão de Crédito/Débito, que deve ser criada com a seguinte estrutura:

__Descrição__

__CAMPO__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Empresa

COD\_EMPRESA

A

003

SIM

SIM

Estabelecimento

COD\_ESTAB

A

006

SIM

SIM

Data Movimento

DATA\_MOVTO

N

008

SIM

SIM

Indicador Pessoa Física/Jurídica da Instituição Financeira e de pagamento

IND\_FIS\_JUR

A

001

SIM

SIM

Código da Pessoa Física/Jurídica da Instituição Financeira e de pagamento

COD\_FIS\_JUR

A

014

SIM

SIM

Indicador Pessoa Física/Jurídica Intermediador da Transação

IND\_FIS\_JUR\_IT

A

001

__NÃO__

__SIM__

Código da Pessoa Física/Jurídica Intermediador da Transação

COD\_FIS\_JUR\_IT

A

014

__NÃO__

__SIM__

Total das Operações com ICMS

VLR\_TOT\_OP\_ICMS

N

015V002

NÃO

NÃO

Total das Operações com ISS

VLR\_TOT\_OP\_ISS

N

015V002

NÃO

NÃO

Total de Outras Operações

VLR\_TOT\_OP\_OUTR

N

015V002

NÃO

NÃO

 

__Observação__: 

O campo Pessoa Fis/Jur Intermediador da Transação faz parte da chave mas não é obrigatório\. Ou seja, É possível não ter Pessoa Fis/Jur Intermediador da Transação, como também existir um ou vários intermediadores relacionados a mesma empresa, estabelecimento, data movimento e Pessoa Física/Jurídica da Instituição Financeira e de pagamento\.

MFS73697

RN02

__Campo Código da Empresa__

Campo de preenchimento obrigatório\.

Quando o campo não estiver preenchido,* *o registro não será importado e no log de erros será gravada mensagem de erro padrão:

*                                                      “O código da empresa deve ser preenchido”*

MFS73697

RN03

__Campo Código do Estabelecimento__

Campo de preenchimento obrigatório\.

Quando o campo não estiver preenchido,* *o registro não será importado e no log de erros será gravada mensagem de erro padrão:

*                                                      “O código do estabelecimento deve ser preenchido”*

MFS73697

RN04

__Campo Data Movimento__

Campo de preenchimento obrigatório\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “O campo Data Movimento é de preenchimento obrigatório e não foi informado”*

Caso o campo esteja preenchido, se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “O campo Data Movimento é invalido”*

MFS73697

RN05

__Campo Indicador Pessoa Física/Jurídica da Instituição Financeira e de pagamento__

Campo de preenchimento obrigatório\.

Valores válidos \(= indicadores da SAFX04\):

1 \(Fornecedor\)

2 \(Cliente\)

3 \(Estabelecimento\)

4 \(Transportadora\)

5 \(Cliente/Fornecedor/Transportadora\)

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

“*O Indicador de Pessoa Fisica/Juridica da Instituição Financeira não esta preenchido ou preenchido com informação inválida\.*”\.

MFS73697

RN06

__Campo Código da Pessoa Física/Jurídica da Instituição Financeira e de pagamento__

Campo de preenchimento obrigatório\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a mensagem: 

“*O Código da Pessoa Fisica/Juridica da Instituição Financeira e de Pagamento é de preenchimento obrigatório e não foi informado*”\)\.

A partir do conteúdo dos campos 04 e 05 \(indicador e código da pessoa fis/jur\) será verificada a existência da pessoa informada na Tabela de Pessoas Fis/Jur \(SAFX04\)\. Quando não encontrada, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

“*O Código da Pessoa Fisica/Juridica da Instituição Financeira e de Pagamento não está cadastrado*”\)\.

MFS73697

RN07

__Campo Indicador Pessoa Física/Jurídica Intermediador da Transação__

Campo de preenchimento não obrigatório\.

Valores válidos \(= indicadores da SAFX04\):

1 \(Fornecedor\)

2 \(Cliente\)

3 \(Estabelecimento\)

4 \(Transportadora\)

5 \(Cliente/Fornecedor/Transportadora\)

Quando preenchido com valor inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

“*O Indicador de Pessoa Fisica/Juridica Intermediador da Transação preenchido com informação inválida\.*”\.

MFS73697

RN08

__Campo Código da Pessoa Física/Jurídica Intermediador da Transação__

Campo de preenchimento não obrigatório\.

Quando preenchido partir do conteúdo dos campos 06 e 07 \(indicador e código da pessoa fis/jur\) será verificada a existência da pessoa informada na Tabela de Pessoas Fis/Jur \(SAFX04\)\. Quando não encontrada, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

“*O Código da Pessoa Fisica/Juridica da Intermediador da Transação não esta cadastrado*”\)\.

MFS73697

RN09

__Campo Total das Operações com ICMS__

Campo de preenchimento não obrigatório, aceitar conteúdo numérico inclusive nulo\.

MFS73697

RN10

__Campo Total das Operações com ISS__

Campo de preenchimento não obrigatório, aceitar conteúdo numérico inclusive nulo\.

MFS73697

RN11

__Campo Total de Outras Operações__

Campo de preenchimento não obrigatório, aceitar conteúdo numérico inclusive nulo\.

MFS73697

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

