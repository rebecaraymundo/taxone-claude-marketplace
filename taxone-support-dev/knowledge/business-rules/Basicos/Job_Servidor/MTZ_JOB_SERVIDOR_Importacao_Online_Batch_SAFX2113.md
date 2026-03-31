# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2113

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2113.docx
- **Modificado:** 2025-04-09
- **Tamanho:** 68 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS14461

Lara Aline

Definição das regras de importação, Online e Batch, da SAFX2113\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX2113 \- Processos relacionados à Suspensão da CPRB, que deve ser criada com a seguinte estrutura:

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

Data Inicial

N

008

SIM

SIM

Indicador correspondente à atividade sujeita a incidência da Contribuição Previdenciária sobre a Receita Bruta

N

008

SIM

SIM

Código da Receita

A

006

SIM

SIM

Código da conta analítica debitada/creditada

A

070

SIM

NÃO

Tipo do Processo

A

001

SIM

SIM

Número do Processo

A

021

SIM

SIM

Código do Indicativo da Suspensão de Exigibilidade de Tributos

A

014

NÃO

NÃO

Alíquota da Contribuição Previdenciária sobre a Receita Bruta

N

008V004

SIM

NÃO

Valor da Contribuição Previdenciária com exigibilidade suspensa

N

015V002

SIM

NÃO

 

MFS14461

RN02

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS14461

RN03

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS14461

RN04

__Campo Data Inicial__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Data Inicial não informado”\.

MFS14461

RN05

__Campo Indicador correspondente à atividade sujeita a incidência da Contribuição Previdenciária sobre a Receita Bruta__

Campo destinado à ao código indicador correspondente à atividade sujeita a incidência da Contribuição Previdenciária sobre a Receita Bruta, conforme a tabela 5\.1\.1\. 

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Indicador da Atividade Econômica não informado”\. 

O Indicador do Código da Atividade Econômica deve constar na tabela 5\.1\.1 \(TACES75\), caso contrário exibir msg ao usuário\.

MFS14461

RN06

__Campo Código da Receita__

Código da Receita referente à Contribuição Previdenciária, conforme informado na DCTF\.

Valores Válidos: 

Grupo do cód\_tributo 34

298501 \- Empresas Prestadoras de Serviço de Tecnologia da Informação – TI e Tecnologia da Informação e Comunicação – TCI

298502 	\- Contribuicao Previdenciaria Sobre Receita Bruta \- Empresas Prestadoras de Servicos TI e TIC  \- 13º Salario

299101 \- Contribuição Previdenciária sobre a Receita Bruta – Demais

299102 \- Contribuicao Previdenciaria Sobre Receita Bruta \- Demais 13º Salario 

Atenção: Este campo deve estar cadastrado na dwt\_cod\_receita 

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Código da Receita não informado”\.

MFS14461

RN07

__Campo Código da conta analítica debitada/creditada__

Conta Contábil referente ao Imposto, utilizada para Contabilização, de acordo com a Tabela de Plano de Contas \(SAFX2002\)\.

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Código da conta analítica não informada”\.

MFS14461

RN08

__Campo Tipo do Processo__

Tipo do Processo, sendo:

1 \- Administrativo;

2 – Judicial\.

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Tipo do Processo não informado”\. 

O cadastro do processo deve existir na tabela de Processo Administrativo/Judicial \(SAFX2058\), caso contrário exibir msg ao usuário\.

MFS14461

RN09

__Campo Número do Processo__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Número do Processo não informado”\. 

O número do processo deve existir na tabela de Processo Administrativo/Judicial \(SAFX2058\), caso contrário exibir msg ao usuário\.

MFS14461

RN10

__Campo Código do Indicativo da Suspensão de Exigibilidade de Tributos __

Campo de preenchimento não obrigatório\. 

Caso informado, o Código do Indicativo da Suspensão de Exigibilidade de Tributos deve existir na tabela de Informação de Suspensão de Exigibilidade de Tributos \(SAFX2059\), caso contrário exibir msg ao usuário\. 

MFS14461

RN11

__Campo Alíquota da Contribuição Previdenciária sobre a Receita Bruta__

Valor da alíquota correspondente à receita da atividade tributável\. A alíquota informada deve constar na Tabela 5\.1\.1

__Validação 01:__ Se o indicador da Atividade Econômica for 99999999 permitir qualquer valor de alíquota, mesmo que não esteja cadastrada na TACES75

__Validação 02:__ Se o indicador da Atividade Econômica for diferente de 99999999, só permitir as alíquotas que estão informada na tabela 5\.1\.1  \(TACES 75\), caso contrário exibir a msg ao usuário\.

__Validação 03:__ O valor informado neste campo deve ser maior que zero, senão exibir a seguinte msg ao usuário: “O valor informado no campo Alíquota da Contribuição Previdenciária sobre a Receita Bruta deve ser maior que zero\.”

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Alíquota da Contribuição Previdenciária sobre a Receita Bruta não informado”\.

MFS14461

RN12

__Campo Valor da Contribuição Previdenciária com exigibilidade suspensa__

O valor informado neste campo deve ser maior que zero, senão exibir a seguinte msg ao usuário: “O valor informado no campo Valor da Contribuição Previdenciária com exigibilidade suspensa deve ser maior que zero\.”

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Valor da Contribuição Previdenciária com exigibilidade suspensa não informado\.”\.

MFS14461

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

