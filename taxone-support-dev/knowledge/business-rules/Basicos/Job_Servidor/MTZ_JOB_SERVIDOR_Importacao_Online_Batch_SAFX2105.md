# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2105

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2105.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 71 KB

---

THOMSON REUTERS

Regras de Importação Online e Batch SAFX2105

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4745

Marcos G\. de Paula

Criação da SAFX2105\.

MFS6498

Jorge Neto

Permitir que a subconta seja igual à conta

CH18547/2016

Lara Aline

Ajuste no campo Grupo Conta\-Subconta para não permitir parametrizar o mesmo grupo para mais de uma conta contábil, conforme solicita regra do PVA versão 3\.3\.8

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX2105 – Subcontas Correlatas, que deve ser criada com a seguinte estrutura:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Conta Contábil

A

070

SIM

SIM

Grupo Conta\-Subconta

A

006

SIM

NÃO

Natureza da Subconta

A

002

SIM

NÃO

Subconta Correlata

A

070

SIM

SIM

 

OS4745

RN02

__Campo Conta Contábil__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS4745

RN03

__Campo Grupo Conta\-Subconta__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso esse não esteja preenchido: “Gr\. Conta\-Subconta não informado”\.

__\[ALTERADO CH18547/2016\]__

Não deve ser permitida a parametrização de um mesmo “Grupo Conta\-Subconta” para mais de uma “Conta Contábil”\. Caso o usuário informe o mesmo código de grupo para mais de uma conta, não permitir a gravação e retornar a mensagem: “Não é permitido utilizar o mesmo Gr\. Conta\-Subconta para mais de uma Conta Contábil”\.

Não deve ser permitida a parametrização de mais de um “Grupo Conta\-Subconta” por “Conta Contábil”\. Caso o usuário informe um código de grupo distinto para a mesma conta, não permitir a gravação e retornar a mensagem: “Não é permitido mais de um Gr\. Conta\-Subconta por Conta Contábil”\.

OS4745

CH18547/2016

RN04

__Campo Natureza da Subconta__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Natureza da Subconta não informada”\.

Quando informado, o conteúdo informado neste campo deve existir na tabela TACES90\. Caso não exista, retornar a mensagem: “Natureza da Subconta inválida”

OS4745

RN05

__Campo Subconta Correlata__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

Esta informação não poderá se repetir para a conta contábil indicada no campo Conta Contábil\. Caso seja repetida a informação, retornar a mensagem: “Código da Subconta Correlata não deve ser igual à Conta pai informada e não pode se repetir por Conta Pai”\.

OS4745

MFS6498

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

