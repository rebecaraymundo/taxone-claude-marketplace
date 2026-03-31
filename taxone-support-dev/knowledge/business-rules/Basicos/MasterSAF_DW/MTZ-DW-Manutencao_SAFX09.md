# MTZ-DW-Manutencao_SAFX09

- **Fonte:** MTZ-DW-Manutencao_SAFX09.docx
- **Modificado:** 2022-11-09
- **Tamanho:** 37 KB

---

# Módulo – Básicos – Documento de Item de Serviço \(SAFX09\)

__Atenção__: O layout da tela de Documento Fiscal foi alterada para o produto TAXONE\. 

Os ajustes para este produto devem ser indicados nos documentos 

MTZ\_Tela\_Doc\_Fiscal\_de\_Servico\_TAXONE\.docx

MTZ\_Tela\_Doc\_Fiscal\_de\_Servico\_TAXONE\.xlsx, no caminho “\\Thomson Reuters Incorporated Requisitos \- Mastersaf DW TaxOne\\Documento\_Matriz\\Basicos\\MasterSAF\_DW\\Tela\_Documento\_Fiscal\_Servico\_TAXONE”

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3003

Incluir tratamento que compõe o Valor do INSS

O objetivo desta OS é passar a carregar a informação de INSS Retido na SAFX09\.

14/09/2010

OS3065\-DW

Novos campos

Inclusão de novos campos na SAFX07 para atendimento ao SEF II \- PE

15/09/2011

OS3749

Inclusão de novos campos

Incluir na SAF08 campos reservados numéricos e alfanuméricos

25/10/2012

OS3924

Inclusão de novo campo

Incluir o campo NBS

15/02/2013

OS4514

Inclusão de novos campos

Inclusão de campos para atendimento e\-Social

26/05/2014

OS4667

Inclusão de novo campo

Inclusão de campo para atendimento aos códigos CST do ISS\.

17/11/2014

MFS8798

Inclusão de novos campos

Inclusão de campos para atendimento ao REINF \(Registros R\-2010 e R\-2020\)

13/01/2017

MFS9748

Inclusão de novos campos

Inclusão de campos de valores referente a INSS\.

22/02/2017

MFS10357

Inclusão de novos campos

Inclusão de campos para atendimento ao REINF \(Registros R\-2010 e R\-2020\)

04/04/2017

MFS13205

Inclusão de novos campos

Inclusão de campos para atendimento ao REINF \(Registros R\-2010 e R\-2020\)

20/09/2017

MFS\-20985

Inclusão de novo campo

Este documento tem como objetivo criar o campo Valor Abatimento não tributado

18/09/2018

MFS24154

Alteração do campo 86

Alteração na lista de valores válidos do campo 86 \- Natureza da Base de Crédito \(EFD\-PIS/PASEP\-COFINS\)

01/02/2019

MFS31367

Andréa Rocha

Inclusão de campo de código de atividade

17/12/2019

MFS31262

Andréa Rocha

Inclusão de campos reservados

19/06/2020

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

RN01

Deverá ser criado o campo __Base INSS__ na tabela __DWT\_ITENS\_SERV__ 

__Base INSS__: esse campo deverá ser do tipo numérico e deverá possuir 17 posições, sendo 15 posições inteiras e 2 casas decimais\. Caso não esteja informado, deve vir preenchido com zeros\.

 

Na tela antiga de itens de serviço \(módulo DW – menu: Manutenção – Documento Fiscal – Item de Serviço \(aba: Valores\)\), deverá ser criado o campo abaixo do quadro da IN86 \(ADE 55/09\)\.

__\[ALTERADA MFS9748\]__

Na tela nova de itens de serviço \(Módulo Básicos – menu: MasterSAF DW – Manutenção – Documento Fiscal – Novo Documento Fiscal – Doc\. Fiscal de Serviço\), deverá ser criado o campo abaixo do quadro da IN86 \(ADE 55/09\)\. deverá ser criado o campo abaixo dos Valores de IPI\. 

__OBS:__ a tela informada no documento de requisito é apenas uma sugestão\. Fica a critério de a Fábrica definir a melhor usabilidade dos campos nas telas a serem alteradas\. Além disso, fica como sugestão que os campos de INSS fiquem próximos dos campos de IR\.

OS3003

MFS9748

RN02

Deverá ser criado o campo __INSS__ Retido na tabela __DWT\_ITENS\_SERV__ 

__INSS Retido: __esse campo deverá ser do tipo numérico e deverá possuir 17 posições, sendo 15 posições inteiras e 2 casas decimais\. Caso não esteja informado, deve vir preenchido com zeros\. Caso não esteja informado, deve vir preenchido com zeros\.

 

Na tela antiga de itens de serviço \(módulo DW – menu: Manutenção – Documento Fiscal – Item de Serviço \(aba: Valores\)\), deverá ser criado o campo abaixo do quadro da IN86 \(ADE 55/09\)\.

__\[ALTERADA MFS9748\]__

Na tela nova de itens de serviço \(Módulo Básicos – menu: MasterSAF DW – Manutenção – Documento Fiscal – Novo Documento Fiscal – Doc\. Fiscal de Serviço\), deverá ser criado o campo abaixo do quadro da IN86 \(ADE 55/09\)\. deverá ser criado o campo abaixo dos Valores de IPI\. 

__OBS:__ a tela informada no documento de requisito é apenas uma sugestão\. Fica a critério de a Fábrica definir a melhor usabilidade dos campos nas telas a serem alteradas\. Além disso, fica como sugestão que os campos de INSS fiquem próximos dos campos de IR\.

OS3003

MFS9748

RN03

Deverá ser criado o campo __Alíquota__ __INSS__ na tabela __DWT\_ITENS\_SERV__ 

__Alíquota INSS: __esse campo deverá ser do tipo numérico e deverá possuir 7 posições, sendo 3 posições inteiras e 4 casas decimais\. Caso não esteja informado, deve vir preenchido com zeros\.

 

Na tela antiga de itens de serviço \(módulo DW – menu: Manutenção – Documento Fiscal – Item de Serviço \(aba: Valores\)\), deverá ser criado o campo abaixo do quadro da IN86 \(ADE 55/09\)\.

__\[ALTERADA MFS9748\]__

Na tela nova de itens de serviço \(Módulo Básicos – menu: MasterSAF DW – Manutenção – Documento Fiscal – Novo Documento Fiscal – Doc\. Fiscal de Serviço\), deverá ser criado o campo abaixo do quadro da IN86 \(ADE 55/09\)\. deverá ser criado o campo abaixo dos Valores de IPI\. 

__OBS:__ a tela informada no documento de requisito é apenas uma sugestão\. Fica a critério de a Fábrica definir a melhor usabilidade dos campos nas telas a serem alteradas\. Além disso, fica como sugestão que os campos de INSS fiquem próximos dos campos de IR\.

OS3003

MFS9748

__RN87__

__Campo Valor Acréscimo:                    __\(campo criado na OS3065\-dw\)

Obrigatório 🡪 Não 

Críticas 🡪 sem críticas

OS3065\-dw

__RN09__

Inclusão do campo NBS na tela de Item de Serviço do módulo MasterSAF DW, menu: Manutenção/Documento Fiscal/Novo Documento Fiscal/Doc\. Fiscal de Serviço\.

\- O campo NBS deve ser recuperado da SAFX2055

Campo Não obrigatório

\- Recuperação do código NBS:

O sistema deve considerar o código de maior validade que seja menor ou igual a data da escrita fiscal da SAFX09 \(03 \- DATA\_FISCAL\)

__OS3924__

__RN10__

Deverá ser criado o campo “Valor Total Adicional”\. É um campo não obrigatório / Numérico / Campo de Valor com dois decimais\.

__OS4514__

__RN11__

Deverá ser criado o campo “Valor Total não Retido pelo Contratante”\. É um campo não obrigatório / Numérico / Campo de Valor com dois decimais\.

__OS4514__

__RN12__

Deverá ser criado o campo “Valor das Deduções Previdenciárias da NF”\. É um campo não obrigatório / Numérico / Campo de Valor com dois decimais\.

__OS4514__

__RN13__

Deverá ser criado o campo “Valor da Retenção Previdenciária da NF”\. É um campo não obrigatório / Numérico / Campo de Valor com dois decimais\.

__OS4514__

__RN14__

Deverá ser criado o campo “Valor da Retenção Previdenciária relativo a Serviços Subempreitados”\. É um campo não obrigatório / Numérico / Campo de Valor com dois decimais\.

__OS4514__

__RN15__

Deverá ser criado o campo “ Código da Situação Tributária ISS” na tela de Item de Serviço do módulo MasterSAF DW, menu: Manutenção/Documento Fiscal/Novo Documento Fiscal/Doc\. Fiscal de Serviço\.

É um campo não obrigatório, numérico e com 02 posições\.

\- O campo Código da Situação Tributária ISS, deve ser recuperado da TACES88\.

__OS4667__

__RN16__

Deverá ser criado o campo “Retenção Principal não Efetuada”\. 

É um campo não obrigatório / Numérico / Campo de Valor com dois decimais\.

__MFS8798__

__RN17__

Deverá ser criado o campo “Retenção Principal não Efetuada”\. 

É um campo não obrigatório / Numérico / Campo de Valor com dois decimais\.

__MFS8798__

__RN18__

Deverá ser criado o campo “Dedução por Custo de Alimentação”\.

É um campo não obrigatório / Numérico / Campo de Valor com dois decimais\.

__MFS8798__

__RN19__

Deverá ser criado o campo “Dedução por Custo de Transporte”\. 

É um campo não obrigatório / Numérico / Campo de Valor com dois decimais\.

__MFS8798__

__RN20__

Deverá ser criado o campo “Tipo do Processo Retenção Principal”

Não Obrigatório / Alfanumérico / Default: Não Selecionado / DropDown

Deverá listar as seguintes opções:

1. Administrativo
2. Judicial 
3. Judicial Prestador

__MFS10357__

__RN21__

Deverá ser criado o campo “Número do Processo Retenção Principal”

Não Obrigatório / Alfanumérico / Pasta

Deverão ser listados os processos conforme cadastro de processos na tela: \(MastersafDW >> Menu Manutenção >> Códigos >> Cadastro de Processo Admin/Judicial \(REINF\) aba Informações do Processo\) e filtro por tipo de processo\. 

Se tipo de processo = “3 – Judicial Prestador” este campo deverá ser desabilitado\.

__MFS10357__

__RN22__

Deverá ser criado o campo “Código Suspensão Principal”

Não Obrigatório / Alfanumérico / Pasta

Deverão ser listados os códigos conforme cadastro de suspensão na tela: \(MastersafDW >> Menu Manutenção >> Códigos >> Cadastro de Processo Admin/Judicial \(REINF\) aba Informações de Suspensão de Exigibilidade de Tributos\) e filtro por número de processo e tipo de processo\. Caso houver apenas um código cadastrado este deverá ser apresentado automaticamente e o campo bloqueado\.

Se tipo de processo = “3 – Judicial Prestador” este campo deverá ser desabilitado\.

__MFS10357__

__RN23__

Deverá ser criado o campo “Tipo do Processo Retenção Adicional”

Não Obrigatório / Alfanumérico / Default: Não Selecionado / DropDown

Deverá listar as seguintes opções:

1. Administrativo
2. Judicial 
3. Judicial Prestador

__MFS10357__

__RN24__

Deverá ser criado o campo “Número do Processo Retenção Adicional”

Não Obrigatório / Alfanumérico / Pasta

Deverão ser listados os processos conforme cadastro de processos na tela: \(MastersafDW >> Menu Manutenção >> Códigos >> Cadastro de Processo Admin/Judicial \(REINF\) aba Informações do Processo\) e filtro por tipo de processo\. 

Se tipo de processo = “3 – Judicial Prestador” este campo deverá ser desabilitado\.

__MFS10357__

__RN25__

Deverá ser criado o campo “Código Suspensão Adicional”

Não Obrigatório / Alfanumérico / Pasta

Deverão ser listados os códigos conforme cadastro de suspensão na tela: \(MastersafDW >> Menu Manutenção >> Códigos >> Cadastro de Processo Admin/Judicial \(REINF\) aba Informações de Suspensão de Exigibilidade de Tributos\) e filtro por número de processo e tipo de processo\. Caso houver apenas um código cadastrado este deverá ser apresentado automaticamente e o campo bloqueado\.

Se tipo de processo = “3 – Judicial Prestador” este campo deverá ser desabilitado\.

__MFS10357__

__RN26__

Deverá ser criado o campo “Valor do Serviço Prestado em Condições Especiais para 15 anos”\. É um campo não obrigatório / Numérico / Campo de Valor com dois decimais\.

__MFS13205__

__RN27__

Deverá ser criado o campo “Valor do Serviço Prestado em Condições Especiais para 20 anos”\. É um campo não obrigatório / Numérico / Campo de Valor com dois decimais\.

__MFS13205__

__RN28__

Deverá ser criado o campo “Valor do Serviço Prestado em Condições Especiais para 25 anos”\. É um campo não obrigatório / Numérico / Campo de Valor com dois decimais\.

__MFS13205__

__RN29__

Deverá ser criado o campo “Valor Abatimento não tributado”\. É um campo não obrigatório / Numérico / Campo de Valor com dois decimais\.

__MFS\-20985__

__RN86__

__Campo 86 \- Natureza da Base de Crédito \(EFD\-PIS/PASEP\-COFINS\)__

01 \- Aquisição de bens para revenda\.

02 \- Aquisição de bens utilizados como insumo\.

03 \- Aquisição de serviços utilizados como insumo\.

04 \- Energia elétrica e térmica, inclusive sob a forma de vapor\.

05 \- Aluguéis de prédios\.

06 \- Aluguéis de máquinas e equipamentos\.

07 \- Armazenagem de mercadoria e frete na operação de venda\.

08 \- Contraprestações de arrendamento mercantil

09 \- Máquinas, equipamentos e outros bens incorporados ao ativo imobilizado \(crédito sobre encargos de depreciação\)\.

10 \- Máquinas, equipamentos e outros bens incorporados ao ativo imobilizado \(crédito com base no valor de aquisição\)\.

11 \- Amortização e Depreciação de edificações e benfeitorias em imóveis\.

12 \- Devolução de Vendas Sujeitas à Incidência Não Cumulativa\.

13 \- Outras Operações com Direito a Crédito\.

14 \- Atividade de Transporte de Cargas – Subcontratação\.

15 \- Atividade Imobiliária – Custo Incorrido de Unidade Imobiliária\.

16 – Atividade Imobiliária – Custo Orçado de Unidade não concluída

17 \- Atividade de Prestação de Serviços de Limpeza, Conservação e Manutenção – vale\-transporte, vale\-refeição ou vale\-alimentação, fardamento ou uniforme\.

18 \- Estoque de abertura de bens\.

Obs\.: Retirar a regra relativa a classificação do documento fiscal, mostrar todos os códigos independente da classificação do documento e incluir os novos códigos\.

__MFS24154__

__RN113__

__Campo 113 \- Atividade \(RJ\)__

Campo numérico de 7 posições, sem validação de conteúdo\.

Não obrigatório\.

__MFS31367__

__RN114__

__Campo 114 \-Reservado 4__

Campo alfanumérico de 50 posições, sem validação de conteúdo\.

Não obrigatório\.

__MFS31262__

__RN115__

__Campo 115 \-Reservado 5__

Campo alfanumérico de 50 posições, sem validação de conteúdo\.

Não obrigatório\.

__MFS31262__

__RN116__

__Campo 116 \-Reservado 6__

Campo numérico de 17 posições, sendo 2 decimais, sem validação de conteúdo\.

Não obrigatório\.

__MFS31262__

__RN117__

__Campo 117 \-Reservado 7__

Campo numérico de 17 posições, sendo 2 decimais, sem validação de conteúdo\.

Não obrigatório\.

__MFS31262__

__RN118__

__Campo 118 \-Reservado 8__

Campo numérico de 17 posições, sendo 2 decimais, sem validação de conteúdo\.

Não obrigatório\.

__MFS31262__

