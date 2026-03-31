# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX179

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX179.docx
- **Modificado:** 2021-10-27
- **Tamanho:** 78 KB

---

THOMSON REUTERS

Regras de Importação Online e Batch SAFX179

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-2711

Marcos de Paula

Definição das regras de importação, Online e Batch, da SAFX179\.

MFS\-14377

João Henrique\. 

Inclusão do campo de arquivamento na importação, Online e Batch, da SAFX179\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN00

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX179 – Livro Razão Auxiliar das Subcontas, que deve ser criada com a seguinte estrutura:

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

Código do Livro Auxiliar

A

003

SIM

SIM

Natureza da Subconta Correlata

A

002

SIM

SIM

Código da Subconta

A

070

SIM

SIM

Código do Centro de Custos

A

020

NÃO

SIM

CNPJ da Empresa Investida

A

014

NÃO

SIM

Código do Item \(ativo/passivo\)

A

010

SIM

SIM

Código Individualizado do Bem

A

030

SIM

SIM

Data do Reconhecimento Contábil do Item

A

008

SIM

SIM

Data do Lançamento Contábil

A

008

SIM

SIM

Número do Lançamento

A

040

SIM

SIM

Descrição Resumida do Item

A

050

NÃO

NÃO

Quantidade Inicial do Item

N

015V002

NÃO

NÃO

Saldo Inicial da Conta que Registrada o Item

N

015V002

NÃO

NÃO

Indicador do Saldo Inicial da Conta

A

001

NÃO

NÃO

Realização do Item

N

015V002

NÃO

NÃO

Indicador da Realização do Item

A

001

NÃO

NÃO

Saldo Final da Conta que Registra o Item

N

015V002

NÃO

NÃO

Indicador do Saldo Final da Conta

A

001

NÃO

NÃO

Saldo Inicial na Subconta Antes do Lançamento Contábil

N

015V002

NÃO

NÃO

Indicador do Saldo Inicial da Subconta

A

001

NÃO

NÃO

Valor Registrado a Débito na Subconta 

N

015V002

NÃO

NÃO

Valor Registrado a Crédito na Subconta 

N

015V002

NÃO

NÃO

Saldo Final na Subconta após o Lançamento Contábil\.

N

015V002

NÃO

NÃO

Indicador do Saldo Final da Subconta

A

001

NÃO

NÃO

Valor do Lançamento Contábil

N

015V002

NÃO

NÃO

Indicador do Lançamento

A

001

NÃO

NÃO

Indicador de Registro Relativo a Adoção Inicial

A

001

NÃO

NÃO

Arquivamento

A

050

NÃO

SIM

 

MFS\-2711

MFS\-14377

RN01

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-2711

RN02

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-2711

RN03

__Campo Código do Livro Auxiliar__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido\. Utilizar a mensagem: “Código do Livro Auxiliar não informado”\.

Caso tenha sido informado um código, deve ser verificado se para o código informado existe cadastro correspondente na Tela “Livros Auxiliares ao Diário” \(Módulo: SPED >> ECD – Escrituração Contábil Digital / Menu: Parâmetros\), cujo tipo de livro esteja preenchido com a opção “Z – Razão Auxiliar \(Livro Contábil Auxiliar conforme leiaute definido nos registros I500 a I555\)” __E__ que __não__ tenha sido cadastrado na Tela  “Impressão do Livro Auxiliar” \(Módulo: SPED / ECD – Escrituração Contábil Digital, Menu: Parâmetros\)\. Caso não exista o cadastro com os critérios indicados, retornar mensagem de erro: “Não existe cadastro na tela de “Livros Auxiliares ao Diário” com Tipo “Z – Razão Auxiliar” para o Código do Livro indicado”\.

MFS\-2711

RN03

__Campo Natureza da Subconta Correlata__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido\. Utilizar a mensagem “92727” da TFIX22: “Natureza da Subconta nao preenchida”\.

Caso tenha sido informada uma Natureza da Subconta Correlata, verificar a existência de cadastro correspondente para o código na tabela TACES90, considerando registro cuja data de atualização da taces seja menor ou igual à Data do Lançamento Contábil informada no registro que está sendo importado\. Caso não exista um cadastro com os critérios indicados, retornar mensagem de erro: “Código da Natureza da Subconta Correlata não cadastrado na TACES90”\.

MFS\-2711

RN04

__Campo Código da Subconta__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido\. Utilizar a mensagem “92726” da TFIX22: “Codigo da Subconta correlata nao preenchido”\.

Verificar a existência do Código da Conta Analítica de Resultado na tabela SAFX2002, com Data Início/Inclusão/Alteração menor ou igual a Data do Lançamento Contábil\. Caso não exista, retornar mensagem de erro\. Utilizar a mensagem “91860” da TFIX22: “Plano de Contas nao encontrado”\.

MFS\-2711

RN05

__Campo Código do Centro de Custo__

Verificar a existência do código do Centro de Custo na tabela SAFX2003 com Data Início/Inclusão/Alteração menor ou igual a Data do Lançamento Contábil\. Caso não exista, retornar mensagem de erro\. Utilizar a mensagem “91861” da TFIX22: “Centro de Custo nao encontrado”\.

MFS\-2711

RN06

__Campo CNPJ da Empresa Investida__

Caso seja informado um CNPJ, verificar se o código informado é válido, conforme função padrão de validação de CNPJ\. Caso não seja, retornar mensagem de erro\. Utilizar a mensagem “90082” da TFIX22: “Numero de CNPJ informado nao e valido, conforme regras da Secretaria de Fazenda”\.

MFS\-2711

RN07

__Campo Código do Item \(ativo/passivo\)__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido\. Utilizar a mensagem: “Codigo do Item \(ativo/passivo\) nao preenchido”\.

MFS\-2711

RN08

__Campo Código Individualizado do Bem__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido\. Utilizar a mensagem: “Código Individualizado do Bem nao preenchido”\.

MFS\-2711

RN09

__Campo Data do Reconhecimento Contábil do Item__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido\. Utilizar a mensagem: “Data do Reconhecimento Contábil do Item não informada”\.

MFS\-2711

RN10

__Campo Indicador do Saldo Inicial__

O conteúdo informado para este campo deve ser igual a “D” ou “C”\. Caso seja diferente destes valores, retornar mensagem de erro: "Indicador do Saldo Inicial invalido\. Informe <D> ou <C>”\.

MFS\-2711

RN11

__Campo Indicador da Realização do Item__

O conteúdo informado para este campo deve ser igual a “D” ou “C”\. Caso seja diferente destes valores, retornar mensagem de erro: "Indicador da Realização do Item invalido\. Informe <D> ou <C>”\.

MFS\-2711

RN12

__Campo Indicador do Saldo Final__

O conteúdo informado para este campo deve ser igual a “D” ou “C”\. Caso seja diferente destes valores, retornar mensagem de erro: "Indicador do Saldo Final invalido\. Informe <D> ou <C>”\.

MFS\-2711

RN13

__Campo Data do Lançamento Contábil__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido\. Utilizar a mensagem “90102” da TFIX22: “O Campo de Data do Lancamento Contabil deve ser preenchido”\.

MFS\-2711

RN14

__Campo Número do Lançamento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido\. Utilizar a mensagem “91313” da TFIX22: “O Numero do Lancamento nao pode ser nulo”\.

MFS\-2711

RN15

__Campo Indicador do Lançamento__

O conteúdo informado para este campo deve ser igual a “D” ou “C”\. Caso seja diferente destes valores, retornar mensagem de erro: "Indicador do Lançamento invalido\. Informe <D> ou <C>”\.

MFS\-2711

RN16

__Campo Indicador de Registro Relativo a Adoção Inicial__

O conteúdo informado para este campo deve ser igual a “1” ou “2”\. Caso seja diferente destes valores, retornar mensagem de erro: "Indicador de Registro Relativo à Adoção Inicial invalido\. Informe <1> ou <2>”\.

MFS\-2711

RN17

__Campo Arquivamento __

O conteúdo para este campo possui o objetivo de indicar o documento que originou o lançamento contábil\. Não será obrigatório, caso o usuário não preencha, será gravado com espaço\. 

MFS\-14377

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

