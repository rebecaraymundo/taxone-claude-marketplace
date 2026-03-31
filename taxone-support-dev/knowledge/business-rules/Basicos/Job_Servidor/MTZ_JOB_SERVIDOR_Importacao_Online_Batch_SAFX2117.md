# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2117

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2117.docx
- **Modificado:** 2023-04-27
- **Tamanho:** 68 KB

---

THOMSON REUTERS

 Regras de Carga, Exportação e Importação \(Online e Batch\) SAFX2117 – Parametrização da Identificação da Natureza de Rendimento

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

Carga à Programação à Execução

 Importação à Programação à Execução     

 Importação batch à Programação à Execução

 Exportação de Dados à Programação à Execução

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

MFS\-99061

Alessandra Navatta

Definição das regras de importação, Online e Batch, da SAFX2117 – Parametrização da Identificação da Natureza de Rendimento

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS__

RN00

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX2117, que deve ser criada com a seguinte estrutura:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Natureza de Rendimento

A

009

SIM

SIM

Indicador de Pessoa Física/Jurídica

A

001

NÃO

SIM

Código da Pessoa Física/Jurídica

A

014

NÃO

SIM

Código de Receita

A

006

NÃO

SIM

Serviço para Atribuição da Natureza de Rendimento

A

010

NÃO

SIM

 

MFS\-99061

RN01

__Natureza de Rendimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

O código da natureza de rendimento deve estar previamente cadastrado na TACES101 \(campo Código da Natureza do Rendimento\), caso contrário, exibir a mensagem: “Registro nao cadastrado na Tabela de Natureza de Rendimentos\. “

Se apenas o campo Natureza de Rendimento for preenchido e nenhum dos demais campos de critério \(Indicador de Pessoa Física/Jurídica e Código da Pessoa Física/Jurídica, Código de Receita ou Serviço para Atribuição da Natureza de Rendimento\), for indicado, exibir a mensagem: “Pelo menos um dos campos de critério \(Indicador e Código da Pessoa Física/Jurídica, Código de Receita ou Serviço para Atribuição da Natureza de Rendimento\) deve estar preenchido”

MFS\-99061

RN02

__Campo Indicador Pessoa Física/Jurídica__

Indicador de Pessoa Física/Jurídica relacionada \(SAFX04\), conforme segue:

1 \- Fornecedor;

2 \- Cliente;

3 \- Estabelecimento;

4 \- Transportadora;

5 \- Cliente/Fornecedor/Transportadora\.

MFS\-99061

RN03

__Campo Código da Pessoa Física/Jurídica__

Deve ser aceito pessoa jurídica cadastrada na SAFX04 

Validações: 

Caso a pessoa não esteja cadastrada na SAFX04, exibir a mensagem: “Registro nao cadastrado na Tabela de Arquivo de Cadastro de Pessoas Físicas/Jurídicas“

MFS\-99061

RN04

__Campo Código de Receita__

Quando preenchido, este código deve estar previamente cadastrado na Taces14 \- DWT\_COD\_RECEITA, caso contrário, exibir a mensagem: “Registro nao cadastrado na Tabela de Códigos da Receita\. “

MFS\-99061

RN05

__Campo Serviço para Atribuição da Natureza de Rendimento__

Este campo não é recuperado de nenhuma tabela\.

MFS\-99061

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

