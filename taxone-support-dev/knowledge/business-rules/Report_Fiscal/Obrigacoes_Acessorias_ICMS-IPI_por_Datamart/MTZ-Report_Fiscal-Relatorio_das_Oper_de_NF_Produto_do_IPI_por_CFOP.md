---
source: "MTZ-Report_Fiscal-Relatorio_das_Oper_de_NF_Produto_do_ IPI_por_CFOP.doc"
category: Report_Fiscal
converted: auto
---

Report Fiscal - Relatório das Operações de NF/ Produto do IPI p/ CFOP

Localização:
Módulo: Básico > Report Fiscal
Menu: Obrigações Acessórias > ICMS/ IP p/ Datamart > Relatório das Operações do IPI p/ CFOP/ Produto


DOCUMENTO DE REQUISITO

DR
Nome
Descrição
CH26175_2012
Correção na opção "Todos" no campo "Estabelecimento"
Correção na opção "Todos" no campo "Estabelecimento"
MFS-692469
Alessandra Cristina Navatta
Apenas produto TAXONE: 
 
* Migração do relatório para o Servidor de Relatórios.(RN02) 
* Criação do formato em Excel (XLSX) 
Considerando as mesmas colunas exibidas no formato PDF (RN03) 
 
Não foi realizada a reversa do relatório 


REGRAS DE NEGÓCIO

Cód.
Descrição
DR
RN01

Quando o usuário selecionar a opção "Todos" no campo "Estabelecimento", o relatório dever ser gerado (considerando normalmente os demais parâmetros informados na tela de geração) para todos os estabelecimentos pertencentes à empresa logada, sendo que deve haver quebra por Estabelecimento.

CH26175_2012
RN02
Apenas para Produto TAXONE 
 
Migrar o relatório para o servidor de relatórios. 
 
Incluir o campo Tipo de Geração na tela de geração do Relatório Demonstrativo - Notas de Devolução de Compra Dentro do Mês da Apuração.

Permite escolher a opção de geração. 
Lista de valores válidos: 
* Arquivo PDF 
* Excel (XLSX) 
  
A opção default é "Arquivo PDF" 

MFS-692469
RN03
Formato EXCEL 

Criar o formato em Excel (XLSX), considerando as mesmas colunas apresentadas no formato em PDF. 
MFS-692469


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

