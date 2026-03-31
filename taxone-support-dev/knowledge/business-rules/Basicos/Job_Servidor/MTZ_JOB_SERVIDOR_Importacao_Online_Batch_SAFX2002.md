# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2002

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2002.docx
- **Modificado:** 2020-12-28
- **Tamanho:** 67 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX2002

Tabela do Plano de Contas

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Carga 🡪 Execução

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

\- Exportação Dados 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS9667

Lara Aline

Definição das regras de carga, exportação, importação Online e Batch da SAF2002, campo Demonstrar conta no plano de contas consolidado\.

MSF28287

José Roberto

Alteração no processo de importação\. validação da data de validade da Conta Contábil \(campo VALID\_CONTA\)\.

MFS57995

Andréa Rocha

Alteração da regra do campo Código de Conta Sintética\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN02

__Campo ‘Demonstrar conta no plano de contas consolidado’ __

Opções válidas:

S – Sim

N – Não

Campo de preenchimento não obrigatório\.

Quando informado uma opção inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Campo Demonstrar conta no plano de contas consolidado com opção invalida”\.

MFS9667

RN03

Alteração no processo de importação\. O processo __verifica a data de validade__ do código da conta contábil  e caso __seja inferior a “01/01/2000”__ será inserida uma nova linha idêntica mas com a data de validade\(__VALID\_CONTA__\)  igual  a “01/01/2000”\.

MFS28287

RN06

__Campo Código de Conta Sintética__

Campo não obrigatório\.

Quando a conta for preenchida, deve ser verificada a existência da conta na SAFX2002:

Caso a conta não exista na tabela, o registro não será importado e no log de erros será gravada a seguinte mensagem: 

*“Codigo da Conta Sintetica não cadastrado”*

Quando a conta existir, deve ser verificado o campo “Indicador de Situação da Conta” da conta sintética, se for igual a “I” \(Inativa\) e o  campo “Indicador de Situação da Conta” da conta a ser importada for igual a “A” \(Ativa\), o registro não será importado e no log de erros será gravada a seguinte mensagem:

*“Conta Sintetica inativa não pode ser associada a uma Conta Contábil ativa”*

MFS57995

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

