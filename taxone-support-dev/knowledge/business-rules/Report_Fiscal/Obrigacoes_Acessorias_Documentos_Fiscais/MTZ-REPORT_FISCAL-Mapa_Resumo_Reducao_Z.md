---
source: "MTZ-REPORT_FISCAL-Mapa Resumo Reducao Z.doc"
category: Report_Fiscal
converted: auto
---

Report Fiscal - Obrigações Acessórias - Doc. Fiscais - Mapa Resumo Redução Z


DOCUMENTO DE REQUISITO

DR
Nome
Descrição
OS2918
Criação de Relatório de Mapa Resumo de ECF a partir da Redução Z

Criação de um relatório semelhante ao Mapa Resumo, lendo a SAFX991.
OS4835
Altera preenchimento do Número de Ordem da Operação
Este documento tem como objetivo alterar os campos Inicial e Final da coluna Número de Ordem da Operação para receber até 09 posições.


REGRAS DE NEGÓCIO

Cód.
Descrição
DR
RN00
Criar o Menu:
* Obrigações Acessórias - Documentos Fiscais - "Mapa Resumo ECF/Redução Z"
OS2918
RN01
Ao clicar no menu conforme RN00 o sistema irá abrir a tela com opções de filtro conforme abaixo:
Título: Emissor de Cupom Fiscal 

1. Selecionar Estabelecimento da UF.
Irá listar todas as UF.

2. Estabelecimento
Irá listar todos os Estabelecimentos da UF escolhida. Também terá a opção "TODOS" que irá gerar a informação de todos os Estabelecimentos daquela determinada UF se selecionado

3. Período
Terá a opção de preenchimento de Inicial e Final. Compreenderá o período da movimentação


OS2918
RN02
O relatório terá o mesmo Layout do Report Fiscal => Obrigações Acessórias - Documentos Fiscais - Mapa Resumo de ECF (com algumas exceções), sendo que as informações de cada campo serão carregadas conforme regras deste documento.
OS2918
RN03
Campo 1: Número do Caixa.
Esse campo será abastecido com informações do campo 04 da SAFX991
OS2918
RN04
Campos 2 e 3: Número de Ordem da Operação.

[ALTERADA - OS4835]
2 - Inicial => Esse campo será abastecido com informações do campo 11 da SAFX991, devendo aceitar até nove posições.

3 - Final => Esse campo será abastecido com informações do campo 12 da SAFX991, devendo aceitar até nove posições.
OS2918
OS4835
RN05
Campos 4 e 5: Totalizador.

4 - Inicial => Esse campo será abastecido com informações do campo 13 da SAFX991

5 - Final => Esse campo será abastecido com informações do campo 14 da SAFX991
OS2918
RN06
Campo 6: Movimento do Dia.
Esse campo será abastecido com o resultado da subtração do campo 14 da SAFX991 pelo campo 13 da SAFX991
OS2918
RN07
Campo 7: Desconto.
Esse campo será abastecido com informações do campo 24 da SAFX991
OS2918
RN08
Campo 8: Cancelamento.
Esse campo será abastecido com informações do campo 26 da SAFX991
OS2918
RN09
Campo 9: Valor Contábil.
Esse campo será abastecido com o resultado da subtração do campo 06 (Movimento do Dia) pelo campo 07 (Desconto)
OS2918
RN10
Campo 10: Isento ICMS.
Informar o somatório das mercadorias isentas e não tributadas, ou seja, o somatório de todas as vendas do dia acumuladas no totalizador parcial "In" relativo à respectiva Redução Z.
Esse campo será abastecido com informações do campo 22 (VLR_OPER_ISENTA_ICMS) da SAFX991. 
OS2918
RN11
Campo 11: Não Incidência ICMS.
Informar o somatório de todas as mercadorias com não incidência de ICMS, ou seja, o somatório de todas as vendas do dia acumuladas no  totalizador parcial "Nn" relativo à respectiva Redução Z.
Esse campo será abastecido com informações do campo 23 (VLR_OPER_N_INCID_ICMS) da SAFX991.
OS2918
RN12
Campo 12: Substituição Tributária ICMS.
Informar o somatório das mercadorias sujeitas ao regime de substituição tributária, ou seja, o somatório de todas as vendas do dia acumuladas no  totalizador parcial "Fn" relativo à respectiva Redução Z.
Esse campo será abastecido com informações do campo 21 (VLR_OPER_ICMS_ST) da SAFX991.
OS2918
RN13
Campo 13: Base de Cálculo ICMS.
Informar o somatório do valor da operação das mercadorias tributadas pelo ICMS, ou seja, o somatório de todas as vendas do dia acumuladas no totalizador parcial "Tnnnn" relativo à respectiva Redução Z.

Esse campo será abastecido com informações do campo 19 (VLR_BASE_ICMS) da SAFX991.
OS2918
RN14
Campo 15: Imposto Debitado.
Esse campo será abastecido com informações do campo 20 da SAFX991
OS2918
RN15
Campo 16: Contador de Redução.
Esse campo será abastecido com informações do campo 05 da SAFX991
OS2918
RN16
O Relatório irá demonstrar uma página para cada dia, sumarizando os valores de cada Equipamento (Cupom) ao final do dia (seguindo o mesmo comportamento do relatório de Mapa Resumos)
OS2918
RN17
O relatório terá 2 níveis de quebra de acordo com a ordem abaixo:

1. Terá uma quebra por número de Caixa (Conforme campo 01)
2. Terá uma quebra por Alíquota (Conforme campo 14)

Obs. O campo 14 irá recuperar a informação da alíquota relacionada aos itens de Cupom. O relatório deverá demonstrar todas as alíquotas por dia, de cada Cupom Fiscal
OS2918


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

