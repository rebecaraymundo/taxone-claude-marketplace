# MTZ-DW-Manutencao_Documento_Fiscal_Exclusao

- **Fonte:** MTZ-DW-Manutencao_Documento_Fiscal_Exclusao.docx
- **Modificado:** 2026-02-03
- **Tamanho:** 63 KB

---

THOMSON REUTERS

Documento Fiscal – Rotina de Exclusão

Mastersaf DW

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4169

Julyana Perrucini

Criação de tabela para armazenamento de documento fiscal excluído\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral de Gravação:__

Quando os documentos fiscais forem excluídos pelo processo Básicos >> Mastersaf DW >> Manutenção >> Documento Fiscal >> Novo Documento Fiscal >> Exclusão, as informações precisam ser gravadas em uma tabela para serem recuperados posteriormente pela geração do relatório de conferência\.

Dados para gravação:

- __Estabelecimento__
- __Número de Controle__ 
- __Movimento Entrada/Saída__ 
- __Número__ 
- __Série__ 
- __Data Fiscal__ 
- __Data Saída/Recebimento__ 
- __Data e Hora de Exclusão__ 
- __Usuário__ 

OS4169

RN01

Campo __Estabelecimento__:

Gravar com o nome do Estabelecimento do documento fiscal excluído\.

OS4169

RN02

Campo __Data Fiscal __\(DATA\_FISCAL da SAFX07\):

Gravar com a Data Fiscal do documento fiscal excluído\. 

OS4169

RN03

Campo __Data Saída\\Recebimento __\(20 \- DATA\_SAIDA\_REC da SAFX07\):

Gravar com a Dt E/S do documento fiscal excluído\.

OS4169

RN04

Campo __Data/Hora Exclusão__:

Gravar com a data e o horário em que o documento fiscal excluído\.

OS4169

RN05

Campo __E/S __\(03 \- MOVTO\_E\_S da SAFX07\):

Gravar com o tipo de movimento do documento fiscal excluído\.

OS4169

RN06

Campo __Número __\(08 \- NUM\_DOCFIS da SAFX07\):

Gravar com o número do documento fiscal excluído\. 

OS4169

RN07

Campo __Série __\(09 \- SERIE\_DOCFIS da SAFX07\):

Gravar com o número da série do documento fiscal excluído\.

OS4169

RN08

Campo __Número de Controle__ \(69 \- NUM\_CONTROLE\_DOCTO da SAFX07\):

Gravar com o Número de Controle da Nota Fiscal do documento fiscal excluído\.

OS4169

RN09

Campo __Usuário__:

Gravar com o Usuário que excluiu o documento fiscal de acordo com o parâmetro de seleção\.

__Tratamento:__

\- Usuário que estiver “logado” no sistema e efetuar a rotina de exclusão do documento fiscal\.

OS4169

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

