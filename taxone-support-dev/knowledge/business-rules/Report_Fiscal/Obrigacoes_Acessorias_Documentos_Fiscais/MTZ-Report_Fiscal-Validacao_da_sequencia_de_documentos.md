---
source: "MTZ-Report_Fiscal-Validacao_da_sequencia_de_documentos.doc"
category: Report_Fiscal
converted: auto
---

REPORT FISCAL


                                         BÁSICOS > REPORT FISCAL > Obrigações Acessórias -> Validação na Sequência de Documentos


DOCUMENTO DE REQUISITO

DR
Nome
Descrição
CH75631
Alteração Relatório Report Fiscal

Incluir opção por UF e "Todos" os estabelecimentos no critério de seleção

CH81499
Incluir a X130 na validação de sequencia de documentos fiscais
A verificação da seqüência de documentos fiscais será feita a partir da X07 e X130.

CH50256
Alteração Relatório Report Fiscal
Incluir opção de separação do tipo de notas de serviço e mercadoria na seleção do relatório.
MFS35601
Andréa Rocha
Alterar a definição do parâmetro de tela "Tipo de Documento"

REGRAS DE NEGÓCIO

Cód.
Descrição
DR
RN00
Criar o listbox "UF", onde serão exibidas todas as UF's para seleção do usuário, com os critérios abaixo:
1 - A primeira opção de seleção deve ser NULO, caso o usuário não queira utilizar esse filtro;
2 - Caso o usuário selecione determinada UF, somente devem ser gerados os dados referentes a UF selecionada.
CH75631
RN01
O listbox "ESTABELECIMENTO" deve ficar abaixo do listbox "UF" e possuir o seguinte comportamento;
1 - Caso o usuário selecione determinada UF, deverão aparecer somente os Estabelecimentos situados naquela determinada UF;
2 - Para o caso 1 (acima) deverá aparecer no listbox a opção "TODOS" e caso o usuário a selecione, deverão ser gerados os dados de todos os Estabelecimentos daquela determinada UF.
CH75631
RN02
Criar o listbox "Tipo de Documento" - Incluindo as 3 opções: "Documento de Serviço", "Documento de Mercadoria" e "Documento de Mercadoria e Serviço" 
-A primeira opção de seleção deve ser NULO, caso o usuário não queira utilizar esse filtro;

Criar o listbox "Classificação do Documento" com as opções:

 - Todos
 - 1 - Documento de Mercadoria
 - 2 - Documento de Serviço
 - 3 - Documento Misto 

CH50256
MFS35601
RN03
O listbox "Classificação do Documento"  deve possuir o seguinte comportamento:

1 - Caso o usuário selecione a opção "Documento de Mercadoria", o critério de seleção das notas deve utilizar o campo cod_class_doc_fis = 1 da tabela x07_docto_fiscal
2 - Caso o usuário selecione a opção "Documento de Serviço", o critério de seleção das notas deve utilizar o campo cod_class_doc_fis = 2 da tabela x07_docto_fiscal
3 - Caso o usuário selecione a opção "Documento Misto", o critério de seleção das notas deve utilizar o campo cod_class_doc_fis = 3  da tabela x07_docto_fiscal
4 - Caso o usuário selecione a opção "Todos", o critério de seleção das notas deve utilizar o campo cod_class_doc_fis = 1, 2 ou 3  da tabela x07_docto_fiscal

CH50256
MFS35601
RN04
A verificação da seqüência de notas fiscais deve ser feita utilizando as tabelas X07 e X130.

Uma nota só será considerada "faltante" quando ela não existir na X07 e nem na X130 (lembrando que na X130 deve-se utilizar o range de 'número de documento inicial' e 'número de documento final', já que não é necessário cadastrar um registro na X130 para cada nota denegada/inutilizada).

Para realizar a verificação de numeração na X130 deve-se utilizar os mesmos parâmetros que utilizamos hoje para consulta à X07, com o detalhe já exposto acima sobre o 'número de documento inicial' e 'número de documento final'.
CH81499


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

