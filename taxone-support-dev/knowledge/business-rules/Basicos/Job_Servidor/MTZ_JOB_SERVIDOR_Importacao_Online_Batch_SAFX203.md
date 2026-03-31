# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX203

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX203.docx
- **Modificado:** 2021-04-19
- **Tamanho:** 70 KB

---

THOMSON REUTERS

Regras de Importação Online e Batch SAFX203

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS3810\-G

Marcos G\. de Paula

Definição das regras de importação, Online e Batch, da SAFX203\.

MFS61556

Andréa Rocha

Inclusão de novos códigos \(02 a 05\) para os campos de Código de Situação Tributária do PIS e Código de Situação Tributária do COFINS, de acordo com os códigos disponibilizados no Guia Prático\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX203 \- Lançamentos de Ajuste EFD\-Contribuições Financeiras, que deve ser criada com a seguinte estrutura:

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

Data da Operação

N

008

SIM

SIM

Código da Situação Tributária PIS

N

002

SIM

SIM

Valor da Alíquota PIS

N

003V004

NÃO

NÃO

Código da Situação Tributária COFINS

N

002

SIM

SIM

Valor da Alíquota COFINS

N

003V004

NÃO

NÃO

Código da Receita/ Dedução/ Exclusão

A

005

SIM

SIM

Código do Atributo da Receita/ Dedução/ Exclusão

A

003

NÃO

SIM

Código do Complemento da Receita/ Dedução/ Exclusão

A

020

SIM

SIM

Código Natureza Receita

N

003

NÃO

SIM

Código da Conta Contábil

A

070

NÃO

SIM

Valor do Ajuste

N

015V002

NÃO

NÃO

Tipo do Ajuste

A

001

NÃO

NÃO

 

OS3810\-G

RN02

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS3810\-G

RN03

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS3810\-G

RN04

__Campo Data da Operação__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS3810\-G

RN05

__Campo Código da Situação Tributária PIS__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

__\[MFS61556\]__ Inclusão dos códigos 02, 03, 04 e 05, conforme a lista de códigos disponibilizada pelo Guia Prático

Só serão permitidos os seguintes códigos da Situação Tributária PIS:

- 1 – Operação Tributável com Alíquota Básica
- 2 – Operação Tributável com Alíquota Diferenciada
- 3 – Operação Tributável com Alíquota por Unidade de Medida de Produto
- 4 – Operação Tributável Monofásica \- Revenda a Alíquota Zero
- 5 – Operação Tributável por Substituição Tributária
- 6 – Operação Tributável a Alíquota Zero
- 7 – Operação Isenta da Contribuição
- 8 – Operação sem Incidência da Contribuição
- 9 – Operação com Suspensão da Contribuição
- 49 – Outras Operações de Saída
- 99 – Outras Operações

Caso durante a importação o Código da Situação Tributária não esteja preenchido, o sistema deve exibir a seguinte mensagem de erro “O Codigo de PIS/COFINS deve ser preenchido com :  <1>, <6>, <7>, <8>, <9>, <49> ou <99>”\. A importação não deve ser permitida\.

OS3810\-G

MFS61556

RN06

__Campo Valor Alíquota PIS__

O valor informado neste campo deve ser nulo ou maior ou igual a zero\. Se for informado valor menor que zero, retornar mensagem de erro: “Valor Alíquota PIS deve ser maior que 0”\.

OS3810\-G

RN07

__Campo Código da Situação Tributária COFINS__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

__\[MFS61556\]__ Inclusão dos códigos 02, 03, 04 e 05, conforme a lista de códigos disponibilizada pelo Guia Prático

Só serão permitidos os seguintes códigos da Situação Tributária COFINS:

- 1 – Operação Tributável com Alíquota Básica
- 2 – Operação Tributável com Alíquota Diferenciada
- 3 – Operação Tributável com Alíquota por Unidade de Medida de Produto
- 4 – Operação Tributável Monofásica \- Revenda a Alíquota Zero
- 5 – Operação Tributável por Substituição Tributária
- 6 – Operação Tributável a Alíquota Zero
- 7 – Operação Isenta da Contribuição
- 8 – Operação sem Incidência da Contribuição
- 9 – Operação com Suspensão da Contribuição
- 49 – Outras Operações de Saída
- 99 – Outras Operações

Caso durante a importação o Código da Situação Tributária não esteja preenchido, o sistema deve exibir a seguinte mensagem de erro “O Codigo de PIS/COFINS deve ser preenchido com :  <1>, <6>, <7>, <8>, <9>, <49> ou <99>”\. A importação não deve ser permitida\.

OS3810\-G

MFS61556

RN08

__Campo Valor Alíquota COFINS__

O valor informado neste campo deve ser nulo ou maior ou igual a zero\. Se for informado valor menor que zero, retornar mensagem de erro: “Valor Alíquota COFINS deve ser maior que 0”\.

OS3810\-G

RN09

__Campo Código da Receita/ Dedução/ Exclusão__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido: “O Cód\. Receita/Dedução/Exclusão deve ser preenchido”\.

Caso o código indicado pelo usuário não esteja na TACES82, retornar mensagem de erro: “Cód\. Receita/Dedução/Exclusão inválido”\.

OS3810\-G

__Campo Código do Complemento da Receita/ Dedução/ Exclusão__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido: “O Cód\. Complemento Receita/Dedução/Exclusão deve ser preenchido”\.

Caso o código indicado pelo usuário não esteja na TACES83, retornar mensagem de erro: “Cód\. Complemento Receita/Dedução/Exclusão inválido”\.

OS3810\-G

RN10

__Campo Código Natureza Receita__

Como o campo é obrigatório de preenchimento quando o CST do PIS ou da COFINS seja igual a 6, 7, 8 ou 9 e deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido: “Não existe Natureza Receita para o Código de Situação Tributária PIS/COFINS\. Favor preencher o Cód\. Natureza”\.

OS3810\-G

RN11

__Campo Código da Conta Contábil__

Caso não seja possível recuperar para o estabelecimento o grupo de centralização, retornar mensagem de erro: “Nao foi possivel recuperar para o estabelecimento o grupo de centralizacao do Codigo Conta Contabil”\.

Caso não exista conta contábil cadastrada, retornar mensagem de erro: “Conta Contabil nao cadastrada”\.

OS3810\-G

RN12

__Campo Tipo do Ajuste__

Deverá ser informado para este campo o conteúdo “P” ou “N”\. Caso seja informado um conteúdo diferente, retornar a mensagem de erro: “Tipo do Ajuste deve ser preenchido com <P> ou <N>”\.

 

OS3810\-G

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

