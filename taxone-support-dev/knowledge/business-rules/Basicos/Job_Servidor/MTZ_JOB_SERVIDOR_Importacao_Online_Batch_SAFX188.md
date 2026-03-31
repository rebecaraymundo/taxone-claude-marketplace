# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX188

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX188.docx
- **Modificado:** 2020-08-03
- **Tamanho:** 69 KB

---

THOMSON REUTERS

Regras de Importação Online e Batch SAFX188

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS3835\-C1

Marcos G\. de Paula

Definição das regras de importação, Online e Batch, da SAFX188\.

MFS10643

Lara Aline

Ajuste na importação para considerar o novo campo Grupo X188 na tela de Programação de Jobs de Importação\.

MFS36746

Andréa Rocha

Ajuste na regra do campo “Valor do Saldo Inicial do Período”\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN00

__Regras Gerais__

Quando o campo “Grupo X188” da tela de programação da importação on line e da importação batch estiver preenchido, na importação os campos conta contábil e centro de custos do Plano de Contas Anterior \(campos 05 e 06 da SAFX188\) serão validados com dados da SAFX2002 do grupo indicado\. Se o campo estiver desmarcado, a importação deve considerar o mesmo grupo do estabelecimento da importação, conforme padrão\. 

MFS10643

RN00a

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX188 \- Transferência de Saldos de Plano de Contas Anterior, que deve ser criada com a seguinte estrutura:

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

Conta Débito/Crédito do Lançamento

A

070

SIM

SIM

Data da Operação

N

008

SIM

SIM

Conta Débito/Crédito do Lançamento do Plano de Contas Anterior

A

070

SIM

SIM

Centro de Custo do Plano de Contas Anterior

A

020

NÃO

SIM

Valor do Saldo Inicial do Período

N

015V002

NÃO

NÃO

Débito/Crédito do Lançamento Contábil

A

001

SIM

NÃO

 

OS3835\-C

RN01

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS3835\-C

RN02

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS3835\-C

RN03

__Identificação do Saldo Contábil correspondente__

Verificar através dos campos Código da Empresa, Código do Estabelecimento, Conta Débito/Crédito do Lançamento e Data da Operação se existe registro correspondente na tabela SAFX02 – Arquivo de Saldos Mensais\. Caso não exista, retornar mensagem de erro: “Saldo Mensal não encontrado\.”\.

OS3835\-C

RN04

__Campo Conta Débito/Crédito do Lançamento do Plano de Contas Anterior__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Conta Débito/Crédito do Lançamento do Plano de Contas Anterior não informado”\.

Verificar a existência do código da Conta Débito/Crédito do Lançamento do Plano de Contas Anterior na tabela SAFX2002\. Caso não exista, retornar mensagem de erro: “Não existe cadastro para a Conta Débito/Crédito do Lançamento do Plano de Contas Anterior informada”\.

OS3835\-C

RN05

__Campo Centro de Custo do Plano de Contas Anterior__

Verificar a existência do código do Centro de Custo do Plano de Contas Anterior na tabela SAFX2003\. Caso não exista, retornar mensagem de erro: “Não existe cadastro para o Centro de Custo do Lançamento do Plano de Contas Anterior informado”\.

OS3835\-C

RN06

__Campo Débito/Crédito do Lançamento Contábil__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Débito/Crédito do Lançamento Contábil não informado”\.

O conteúdo do campo Débito/Crédito do Lançamento Contábil deve ser igual a “D” ou “C”\. Caso seja informado conteúdo diferente, retonar mensagem de erro: “Débito/Crédito do Lançamento Contábil inválido\. Informe <D> ou <C>”\.

OS3835\-C

RN07

__Campo Valor do Saldo Inicial do Período__

__\[MFS36746\]__

Campo não obrigatório\.

O conteúdo do campo pode ser igual a zero\.  Conforme legislação do SPED Contábil, que aceita zero para o valor do saldo inicial do registro I157\.

MFS36746

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

