# MTZ_Conferencias_Relatorio_Exclusao_Documento_Fiscal

- **Fonte:** MTZ_Conferencias_Relatorio_Exclusao_Documento_Fiscal.docx
- **Modificado:** 2026-02-03
- **Tamanho:** 61 KB

---

THOMSON REUTERS

Relatório de Conferência – Exclusão Documento Fiscal

Mastersaf DW

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4169

Julyana Perrucini

Criação de relatório para conferência de exclusão de documento fiscal\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral de Recuperação:__

Quando os documentos fiscais forem excluídos pelo processo Básicos >> Mastersaf DW >> Manutenção >> Documento Fiscal >> Novo Documento Fiscal >> Exclusão, as informações serão gravadas em uma tabela para serem recuperados posteriormente pela geração do relatório de conferência\.

Dados para recuperação:

- __Estabelecimento__ do documento fiscal excluído
- __Número de Controle__ que deverá ser refletido do Nº Processo do documento fiscal excluído
- __Movimento Entrada/Saída__ do documento fiscal excluído
- __Número__ do documento fiscal excluído
- __Série__ do documento fiscal excluído
- __Data Fiscal__ do documento fiscal excluído
- __Data Saída/Recebimento__ do documento fiscal excluído
- __Data e Hora de Exclusão__ de acordo com a data e o horário em que a nota for excluída
- __Usuário__ que estiver “logado” no sistema e efetuar a rotina de exclusão do documento fiscal

As informações dessa tabela para serem recuperadas de acordo com a seleção de filtro na tela de geração precisam que a empresa e estabelecimento sejam selecionados, cuja Data Fiscal ou Data Exclusão seja referente ao Período informado em tela\.

__Tratamentos:__

- Quando o campo Empresa for selecionado como “\- Todos”, automaticamente o campo Estabelecimento deverá ser preenchido como “\-Todos” devendo quebrar o relatório por empresa/estabelecimento\.
- Quando o campo Estabelecimento for selecionado como “\- Todos”, quebrar relatório por estabelecimento\.
- Ordenar por Empresa\\Estabelecimento\\Movimento Entrada/Saída\\Data Fiscal\\Data Saída/Recebimento\\Número\\Série\\Usuário\.

OS4169

RN01

Campo __Estabelecimento__:

Preencher com o nome do Estabelecimento selecionado na geração do relatório\.

__Tratamento:__

Para opção “\- Todos”, trazer o nome de cada estabelecimento cadastrado no sistema em Parâmetros de acordo com a empresa selecionada na tela inicial do MastersaDW\.

OS4169

RN02

Campo __Página__:

Preencher com sequencial de acordo com a quantidade de páginas geradas\.

OS4169

RN03

Campo __Data__:

Preencher com a data e o horário em que foi gerado o relatório\.

Formato: DD/MM/AAAA\.

OS4169

RN04

Campo __Período__:

Preencher com o Período de acordo com o critério preenchido: por Data Fiscal ou Data Exclusão\.

Formato: DD/MM/AAAA\.

OS4169

RN05

Campo __Data Fiscal__:

Preencher com a Data Fiscal do documento fiscal excluído\. 

Formato: DD/MM/AAAA\.

OS4169

RN06

Campo __Data Saída\\Recebimento__:

Preencher com a Data de Saída do documento fiscal excluído\.

Formato: DD/MM/AAAA\.

OS4169

RN07

Campo __Data/Hora Exclusão__:

Preencher com a data e o horário em que o documento fiscal foi excluído\.

Formato: DD/MM/AAAA\.

OS4169

RN08

Campo __E/S__:

Preencher com o tipo de movimento selecionado na geração do relatório\.

__Tratamento:__

- Se selecionado na tela de geração “Entrada” buscar apenas documentos fiscais de entrada e preencher com “E”\.
- Se selecionado na tela de geração “Saída” buscar apenas documentos fiscais de saída e preencher com “S”\.
- Se selecionado na tela de geração “Entrada/Saída” buscar todos os documentos fiscais, preencher com “E” para notas de entrada e “S” para notas de saída\.

OS4169

RN09

Campo __Número__:

Preencher com o número do documento fiscal excluído\.

__Tratamento:__

Se preenchido o campo Documento Fiscal da tela de geração do relatório deve respeitar o filtro selecionando apenas documentos com o número mencionado\. 

OS4169

RN10

Campo __Série__:

Preencher com o número da série do documento fiscal excluído\.

OS4169

RN11

Campo __Número de Controle__:

Preencher com o Número de Controle da Nota Fiscal do documento fiscal excluído\.

OS4169

RN12

Campo __Usuário__:

Preencher com o Usuário que excluiu o documento fiscal de acordo com o parâmetro de seleção\.

__Tratamento:__

- Se selecionado um usuário específico, deve mostrar apenas os documentos fiscais excluídos por esse usuário que realizou a rotina de exclusão\.
- Para opção “\- Todos”, deve mostrar os documentos fiscais excluídos por esse usuário que realizou a rotina de exclusão\.

OS4169

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

