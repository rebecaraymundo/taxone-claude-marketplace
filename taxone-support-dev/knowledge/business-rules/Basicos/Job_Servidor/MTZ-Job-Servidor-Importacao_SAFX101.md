# MTZ-Job-Servidor-Importacao_SAFX101

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX101.docx
- **Modificado:** 2022-05-09
- **Tamanho:** 66 KB

---

   

 THOMSON REUTERS

 – Arquivo Contábil Auxiliar 

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Carga 🡪 Execução

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

\- Exportação Dados 🡪 Execução

##### __DOCUMENTO DE REQUISITO__

__OS/CH/MFS__

__Nome__

__Descrição__

__Data da Alteração__

OS4579

Elenilson Coutinho

Alteração no tamanho do campo NUM\_LANCAMENTO

01/09/2014

MFS22309

João Henrique de Araujo

Inclusão de novo valor válido para o campo TIPO\_LCTO e Criação do campo DT\_LCTO\_EXT\.

20/12/2018

MFS85477

Rogério Ohashi

Retirada a regra que impede a importação dos Lançamentos Extemporâneas, quando se tratar de Contas de Resultado\. \(Indicador de Natureza igual à 3, 4 e 8\)\.

09/05/2022

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de Importação Batch do módulo JOB Servidor deve ser ajustada para que contemple a alteração no campo NUM\_LANCAMENTO da tabela SAFX101 – Arquivo Contábil Auxiliar, que deve ser criada com a seguinte estrutura:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

NUM\_LANCAMENTO

A

040

NAO

NAO

TIPO\_LANCTO

A

001

NAO

NAO

DT\_LCTO\_EXT

N

008

NAO

NAO

 

OS4579

MFS22309

RN02

__Tipo de Lançamento:__

Neste campo serão apresentadas as opções do campo “Indicador do Tipo de Lançamento”\. Esse campo é recuperado através do item 15 \- TIPO\_LANCTO da tabela SAFX101\.

__Regras:__

- As opções válidas para o campo são:

‘N’ – Lançamento Normal \(todos os lançamentos exceto os de encerramento das contas de resultado\)\.

‘E’ – Lançamento de Encerramento de contas de resultado\.

‘X’ – Lançamento Extemporâneo – __*Nova Opção \(MFS\-22309\)*__

__\[MFS85477\] __Retirar Regra de importação  \(Solicitação cliente BAUMGART\)

- Se a conta possuir o TIPO\_LANCTO da tabela SAFX01 preenchido com ‘X’ __E__ o IND\_NATUREZA da tabela SAFX2002 preenchido com 4 – Receita __OU__ 3 – Despesa __OU__ 8 – Custo, o sistema não deve permitir que a conta seja importada\. Se o usuário tentar importar uma conta nessas condições, o sistema deverá emitir uma mensagem de log: *“Não é permitido importar contas de resultado com o tipo de Lançamento “X” \(Lançamento Extemporâneo\)”\.*

Tipo: Alfanumérico

Tamanho: 1 Posição

MFS22309

MFS85477

RN03

__Data do Lançamento Extemporâneo:__

Neste campo o usuário informa a Dt\. Lançto Extemporâneo\. 

__Regras:__

- Esse campo será de preenchimento obrigatório quando a opção do campo __TIPO\_LANCTO__ for igual a __“X”__\. Se o usuário informar o Tipo de Lançamento como __“X” \- Lançamento Extemporâneo __e__ não preencher__ o campo__ Data do Lançamento Extemporâneo__, o sistema deverá emitir uma mensagem de log: 

*“Para o indicador de lançamento igual a “X – Lançamento Extemporâneo” o campo Dt\. Lançto Extemporâneo deve ser preenchido“\.*

- Se o campo o Tipo de Lançamento estiver com uma opção__ diferente__ de __“X” \- Lançamento Extemporâneo__ e o campo__ Data do Lançamento Extemporâneo estiver preenchido__, o sistema deverá emitir uma mensagem de aviso: 

*“O campo Dt\. Lançto Extemporâneo deve ser preenchido quando o indicador de Lançamento for igual a ‘X’ – Lançamento Extemporâneo “\.*

__Item: __a ser reservado pelo desenvolvimento

Tipo: Numérico

Tamanho: 8 Posições

MFS22309

<a id="_Hlk533603129"></a>Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

