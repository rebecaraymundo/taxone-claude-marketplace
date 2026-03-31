# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX271

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX271.docx
- **Modificado:** 2023-02-24
- **Tamanho:** 71 KB

---

THOMSON REUTERS

Regras de Importação Online e Batch SAFX271

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS22135

Lara Aline

Definição das regras de importação, online e Batch, da SAFX271\.

MFS22920

Lara Aline

Inclusão do campo Indicador do Tipo de Processo Judicial

CH31407\_2018

MFS23436

João Henrique

Alteração na SAFX271 para que o sistema importe os dados se um dos campos: __“Valor da Contribuição Previdenciária Não Retida” __OU__ ”Valor da contribuição para o GILRAT Não Retido” __OU__ “Valor da contribuição para o SENAR Não Retido”__ estiver preenchido com valor maior que zero\.  

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX271 – Processos Judiciais com decisão/sentença – Produtor Rural, que deve ser criada com a seguinte estrutura:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Código da Empresa

A

003

SIM

SIM

Código do Estabelecimento

A

006

SIM

SIM

Data do Movimento

N

008

SIM

SIM

Tipo do Documento

A

005

SIM

SIM

Movimento Entrada/Saída

A

001

SIM

SIM

Indicador Pessoa Física/Jurídica

A

001

SIM

SIM

Código/Destinatário/Emitente/ Remetente

A

014

SIM

SIM

Número do Documento Fiscal

A

012

SIM

SIM

Série do Documento Fiscal

A

003

NÃO

SIM

Subsérie do Documento Fiscal

A

002

NÃO

SIM

Indicador Produto

A

001

SIM

SIM

Código do Produto

A

035

SIM

SIM

Número do Processo

A

020

SIM

SIM

Código do Indicativo da Suspensão de Exigibilidade de Tributos

A

014

SIM

NÃO

Valor da Contribuição Previdenciária Não Retida

N

015V002

SIM

NÃO

Valor da contribuição para Gilrat Não Retido

N

015V002

SIM

NÃO

Valor da contribuição para o Senar Não Retida

N

015V002

SIM

NÃO

Indicador do Tipo do Processo Judicial

A

001

NÃO

NÃO

 

MFS22135

MFS22920

RN02

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS22135

RN03

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS22135

RN04

__Campo Data do Movimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Data do Movimento não informado”\. 

MFS22135

RN05

__Campo Tipo do Documento__

Tipo de Documento de acordo com a Tabela de Tipo de Documentos  \(SAFX2005\) \-  \(Duplicata,  Fatura,  Nota  Fiscal  Fatura,  Recibo  e  etc\. \.\.\. \)\. 

Quando se trata de Documentos Fiscais Modelos 2B, 2C ou 2D informar “MRC”\. 

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Tipo do Documento não informado”\. 

MFS22135

RN06

__Campo Movimento Entrada/Saída__

Movimento Entrada/Saída, de acordo com:

1 \- Documento de Entrada, Documento de Terceiros;

2 \- Documento de Entrada emitida pelo Estabelecimento, acolhendo Notas de Produtores Agropecuários;

3 \- Documento de Entrada emitida pelo Estabelecimento, por retorno de mercadorias não entregues ao destinatário;                                                                                                                                        

4 \- Documento de Entrada emitida pelo Estabelecimento, outros motivos legais;

5 \- Documento de Entrada emitida pelo Estabelecimento, globalizando Conhecimento de Frete ou Material Uso/Consumo;

9 \- Documento de Saída\.

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Movimento Entrada/Saída não informado”\. 

MFS22135

RN07

__Campo Indicador Pessoa Física/Jurídica__

Indicador de Pessoa Física/Jurídica relacionada \(SAFX04\), conforme segue:

1 \- Fornecedor;

2 \- Cliente;

3 \- Estabelecimento;

4 \- Transportadora;

5 \- Cliente/Fornecedor/Transportadora\.

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Indicador Pessoa Física/Jurídica não informado”\. 

MFS22135

RN08

__Campo Código/Destinatário/Emitente/ Remetente__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Código/Destinatário/Emitente/Remetente não informado”\. 

MFS22135

RN09

__Campo Número do Documento Fiscal__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Número do Documento Fiscal não informado”\. 

MFS22135

RN10

__Campo Série do Documento Fiscal__

Como o campo é chave, porém não é obrigatório o preenchimento, se não preenchido gravar branco \(" "\)\.

MFS22135

RN11

__Campo Subsérie do Documento Fiscal__

Como o campo é chave, porém não é obrigatório o preenchimento, se não preenchido gravar branco \(" "\)\.

MFS22135

RN12

__Campo Indicador Produto__

Indicador de Produto relacionado \(SAFX2013\), conforme segue:

1 \- Produto;

2 \- Matéria Prima/Insumo;

3 \- Embalagem;

4 \- Material Uso/Consumo;

5 \- Outros;

6 \- Em Elaboração;

7 \- Intermediário;

8 \- Miscelâneas\.

Validação deste campo: O conteúdo do Tipo de Aquisição deve ser igual a <1>, <2>, <3>, <4>, <5>, <6> e deve ser informado pois o campo é obrigatório de preenchimento\. Caso seja diferente de um destes valores ou não informado, retornar a mensagem: “Tipo de Aquisição Inválido ou não preenchido\. Conteúdo do campo deve ser igual a <1>, <2>, <3>, <4>, <5>, <6>”\.

MFS22135

RN13

__Campo Código do Produto__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Código do Produto não informado”\. 

MFS22135

RN14

__Campo Número do Processo__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Número do Processo não informado”\. 

O número do processo deve existir na tabela de Processo Administrativo/Judicial \(SAFX2058\), caso contrário exibir msg ao usuário\.

MFS22135

RN15

__Campo Código do Indicativo da Suspensão de Exigibilidade de Tributos __

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Código do Indicativo da Suspensão de Exigibilidade de Tributos não informado”\.

O Código do Indicativo da Suspensão de Exigibilidade de Tributos deve existir na tabela de Informação de Suspensão de Exigibilidade de Tributos \(SAFX2059\), caso contrário exibir msg ao usuário\. 

MFS22135

RN16

__Campo Valor da Contribuição Previdenciária Não Retida__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “O valor informado no campo Valor da Contribuição Previdenciária Não Retida deve ser maior que zero\. ”

MFS22135

CH31407\_2018

MFS23436

RN17

__Campo Valor da contribuição para Gilrat Não Retido__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “O valor informado no campo Valor da contribuição para Gilrat Não Retido deve ser maior que zero\. ”

MFS22135

CH31407\_2018

MFS23436

RN18

__Campo Valor da contribuição para o Senar Não Retida__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “O valor informado no campo Valor da contribuição para o Senar Não Retida deve ser maior que zero\. ”

MFS22135

CH31407\_2018

MFS23436

RN18\.a

__Regra para Importação da SAFX271 referente aos campos das RN16/RN17/RN18:__

O sistema deverá verificar se no campo 15 \- VLR\_CONT\_PREV\_N\_RET __ou__ 16 \- VLR\_GILRAT\_N\_RET __ou__ 17 VLR\_SENAR\_N\_RET existe valor __maior__ que zero\. Caso exista, o sistema deve importar a SAFX271 com os dados\. Se os campos estiverem sem valor, zerados, uma mensagem no log deve ser exibida: 

*“Por favor informar um valor maior que zero em ao menos um dos impostos: Valor Contrib\.ou Valor Senar ou Valor Gilrat”*\.

CH31407\_2018

MFS23436

RN19

__Campo Indicador do Tipo do Processo Judicial__

Indicador do Processo Judicial, se a informação corresponde a um processo judicial do produtor ou comum a todos os produtores \(Coletivo\), conforme segue:

1 – Processo Judicial do Produtor;

2 – Processo Judicial Coletivo\.

Validação deste campo: O conteúdo do Indicador do Tipo do Processo Judicial deve ser igual a <1> ou <2> e deve ser informado pois o campo é obrigatório de preenchimento\. Caso seja diferente de um destes valores ou não informado, retornar a mensagem: “Indicador do Tipo do Processo Judicial Inválido ou não preenchido\. Conteúdo do campo deve ser igual a <1> ou <2>”\.

MFS22920

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

