---
source: "MTZ-Report_Fiscal-Geral-Razao.doc"
category: Report_Fiscal
converted: auto
---

Report Fiscal - Geral - Relatório Razão


Módulo: Básicos --> Report Fiscal
Menu: Gerenciais --> Contábil --> Geral --> Razão


DOCUMENTO DE REQUISITO

DR
Nome
Descrição
OS3337-B
Geração do Relatório Razão Geral para Todos Estabelecimentos
Incluir a opção TODOS na seleção do estabelecimento para o relatório Razão Geral 
OS3426
DW - BASICOS - REPORT FISCAL - Ajuste no relatório Razão
O objetivo deste requisito é permitir que o campo Número do Lançamento seja exibido no Livro Razão do Report Fiscal. Porém como o layout atual reflete ao livro razão original, esse campo será opcional e apenas será exibido se o campo "Exibe Número do Lançamento" estiver flegado na tela de parâmetros.

REGRAS DE NEGÓCIO

Cód.
Descrição
DR
RN00
Regra Geral

RN01
Geração do Relatório Razão Geral para Todos Estabelecimentos

Alterar o relatório para que quando o usuário escolher a opção "TODOS" em estabelecimentos, então gerar o relatório de cada estabelecimento separado por página. Deverão ser apresentados somente os estabelecimentos relacionados da empresa.
A totalização deve ser feita como nos livros, um para cada estabelecimento, inclusive com o controle de numeração de folha.


OS3337-B
RN02
Campo Exibe Número do Lançamento - Tela de Critério de Seleção

Esse campo deve ser um checkbox com as seguintes opções: "S" (marcado) e "N" (desmarcado). Sendo essa última a opção default.
OS3426
RN03
Campo Número do Lançamento - Livro Razão

Quando o campo "Exibe Número do Lançamento" estiver marcado na tela de critério de seleção, esse campo deve exibir o campo NUM_LANCAMENTO (campo 16 da SAFX01).
Quando o campo "Exibe Número do Lançamento" estiver desmarcado, o Livro deve ser emitido na forma atual.
OS3426


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

