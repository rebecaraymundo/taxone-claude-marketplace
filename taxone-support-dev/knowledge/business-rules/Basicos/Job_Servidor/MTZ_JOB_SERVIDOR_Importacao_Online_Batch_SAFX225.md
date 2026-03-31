# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX225

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX225.docx
- **Modificado:** 2022-05-09
- **Tamanho:** 72 KB

---

THOMSON REUTERS

Regras de Importação Online e Batch 

SAFX225 \- Lançamento Contábil em Moeda Funcional

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Carga 🡪 Execução

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

\- Exportação Dados 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-2631

Marcos G\. de Paula

Definição das regras de importação, Online e Batch, da SAFX225\.

MFS22309

João Henrique de Araujo

Inclusão de novo valor válido para o campo TIPO\_LCTO e Criação do campo DT\_LCTO\_EXT\.

MFS85477

Rogério Ohashi

Retirada a regra que impede a importação dos Lançamentos Extemporâneas, quando se tratar de Contas de Resultado\. \(Indicador de Natureza igual à 3, 4 e 8\)\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX225 \- Lançamento Contábil em Moeda Funcional, que deve ser criada com a seguinte estrutura:

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

Conta Débito/Crédito do Lançamento

A

070

SIM

SIM

Débito/Crédito do Lançamento Contábil

A

001

SIM

SIM

Arquivamento

A

050

SIM

SIM

Valor do Lançamento Contábil

N

015V002

SIM

NÃO

Conta Contra Partida

A

070

 NÃO

NÃO

Centro de Custo

A

020

 NÃO

NÃO

Histórico Padrão

A

006

 NÃO

NÃO

Histórico Complementar

A

255

 NÃO

NÃO

Número do Lançamento

A

040

 NÃO

NÃO

Tipo de Lançamento

A

001

 NÃO

NÃO

Operação com Participante Vinculado \- Indicador da Pessoa Física/Jurídica

A

001

 NÃO

NÃO

Operação com Participante Vinculado \- Código da Pessoa Física/Jurídica

A

014

 NÃO

NÃO

Data do Lançamento Extemporâneo

N

008

NÃO

NÃO

 

MFS\-2631

MFS22309

RN02

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-2631

RN03

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-2631

RN04

__Campo Data da Operação__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso esse não esteja preenchido\. Utilizar a mensagem “90102” da TFIX22: “O Campo de Data do Lancamento Contabil deve ser preenchido”\.

MFS\-2631

RN05

__Campo Conta Débito/Crédito do Lançamento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso esse não esteja preenchido\. Utilizar a mensagem “90095” da TFIX22: “O Codigo da Conta Contabil deve ser preenchido”\.

Verificar a existência do código da Conta Débito/Crédito do Lançamento na tabela SAFX2002, com Data Início/Inclusão/Alteração menor ou igual a Data da Operação do Lançamento\. Caso não exista, retornar mensagem de erro\. Utilizar a mensagem “91860” da TFIX22: “Plano de Contas nao encontrado”\.

MFS\-2631

RN06

__Campo Débito/Crédito do Lançamento Contábil__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso esse não esteja preenchido ou esteja com conteúdo diferente de “D” ou “C”\. Utilizar a mensagem “90100” da TFIX22: “O Campo Debito/Credito deve ser preenchido com <D> ou <C>”\.

MFS\-2631

RN07

__Campo Arquivamento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso esse não esteja preenchido\. Utilizar a mensagem “90099” da TFIX22: “O Campo Arquivamento e obrigatorio \- deve ser preenchido”\.

MFS\-2631

RN08

__Campo Valor do Lançamento Contábil__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso esse não esteja preenchido\. Utilizar a mensagem “90101” da TFIX22: “O Campo Valor do Lancamento Contabil deve ser preenchido”\.

MFS\-2631

RN09

__Campo Conta Contra Partida__

Verificar a existência do código da Conta Contra Partida na tabela SAFX2002 com Data Início/Inclusão/Alteração menor ou igual a Data da Operação do Lançamento\. Caso não exista, retornar mensagem de erro\. Utilizar a mensagem “90096” da TFIX22: “A Conta Contabil de Contra\-Partida nao esta cadastrada”\.

MFS\-2631

RN10

__Campo Centro de Custo__

Verificar a existência do código do Centro de Custo na tabela SAFX2003 com Data Início/Inclusão/Alteração menor ou igual a Data da Operação do Lançamento\. Caso não exista, retornar mensagem de erro\. Utilizar a mensagem “91861” da TFIX22: “Centro de Custo nao encontrado”\.

MFS\-2631

RN11

__Campos Histórico Padrão e Histórico Complementar__

Estes campos estão relacionados e ao menos um deles deve estar preenchido\. Se nenhum deles for preenchido, retornar mensagem de erro\. Utilizar a mensagem “90098” da TFIX22: “Os Campos Codigo do Historico e Historico Complementar sao relacionados, pelo menos um deve ser informado”\.

Caso tenha sido informado o campo Histórico Padrão, verificar a existência do Cadastro correspondente na tabela SAFX2020 com Data Início/Inclusão/Alteração menor ou igual a Data da Operação do Lançamento\. Caso não exista, retornar mensagem de erro\. Utilizar a mensagem “90383” da TFIX22: “O Campo Codigo de Historico Padrao nao esta cadastrado”\.

MFS\-2631

RN12

__Campo Tipo de Lançamento__

Verificar o conteúdo do campo que deve ser igual a <N>, <E> ou <X>\. Se for diferente, retornar mensagem de erro: “Indicador do tipo de lançamento deve ser <N>, <E> ou <X>” \(criar mensagem na TFIX22\)\.

__Regras:__

- As opções válidas para o campo são:

‘N’ – Lançamento Normal \(todos os lançamentos exceto os de encerramento das contas de resultado\)\.

‘E’ – Lançamento de Encerramento de contas de resultado\.

‘X’ – Lançamento Extemporâneo – __*Nova Opção \(MFS\-22309\)*__

__\[MFS85477\] __Retirar Regra \(Solicitação cliente BAUMGART\)

- Se a conta possuir o TIPO\_LANCTO da tabela SAFX01 preenchido com ‘X’ __E__ o IND\_NATUREZA da tabela SAFX2002 preenchido com 4 – Receita __OU__ 3 – Despesa __OU__ 8 – Custo, o sistema não deve permitir que a conta seja importada\. Se o usuário tentar importar uma conta nessas condições, o sistema deverá emitir uma mensagem de log: *“Não é permitido importar contas de resultado com o tipo de Lançamento “X” \(Lançamento Extemporâneo\)”\.*

Tipo: Alfanumérico

Tamanho: 1 Posição

MFS\-2631

MFS22309

MFS85477

RN13

__Campo Indicador da Pessoa Física/Jurídica e Código da Pessoa Física/Jurídica__

Quando informado, verificar a existência do cadastro da PFJ na tabela SAFX04\. Caso não exista, retornar mensagem de erro\. Utilizar a mensagem “509015” da TFIX22: “O codigo da Pessoa Fisica/Juridica nao esta cadastrado\.”\.

MFS\-2631

RN14

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

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

