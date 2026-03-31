# MTZ-DW-Manutencao_SAFX116

- **Fonte:** MTZ-DW-Manutencao_SAFX116.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 70 KB

---

THOMSON REUTERS

Módulo DW – Manutenção da SAFX116

Documentos Fiscais Referenciados

__                                       __

__Localização__: Menu Básicos, Módulo: MasterSAF DW, menu Manutenção 🡪 Documento Fiscal 🡪 Novo Documento Fiscal 🡪 Doc\. Fiscal de Mercadoria 

__Aba__: Informações Complementares >> Doc\. Fiscais Referenciados\.

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS\-4880

Atualização da Estrutura da Tabela

Inclusão de novo campo na tela de manutenção\.

14/07/2016

CH26141\_2016

Alteração da validação do campo “Chave de Acesso da NF\-Eletrônica”

Este documento tem como objetivo retirar a validação da data do campo “Chave de Acesso da NF\-Eletrônica”\.

13/12/2016

REGRAS DE NEGÓCIO

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Chave de Acesso da NF\- Eletrônica

Editbox

N

S

Não Possui

__\[ALTERADA – CH26141\_2016\]__

Permitir o usuário informar a chave de Acesso da NF\- Eletrônica do documento fiscal referenciado, se a data de emissão do documento fiscal for maior ou igual a ‘01/01/2017’ e se o Código do Modelo for igual a ‘55’ ou ‘57’:

__Validação 1__

Para o preenchimento da “Chave de Acesso da NF\-Eletrônica”, verificar se a DATA\_FISCAL\_REF \(campo 19\) SAFX116 é __maior__ ou __igual__ a ‘01/01/2017’:

Crítica: Data fiscal do documento de referencia invalida, quando a chave de acesso e informada\.

Solução: A data fiscal ref deve ser maior ou igual a 01/01/2017\.

__Validação 1  2__

Para o preenchimento da “Chave de Acesso da NF\-Eletrônica” é necessário que os modelos de documento fiscal sejam iguais a “55” ou “57”:

Crítica: Modelo invalido para a nota fiscal de referencia, quando a chave de acesso e informada\.

Solução: O codigo de modelo ref deve ser 55 ou 57\.

MFS4880

CH26141\_2016

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

