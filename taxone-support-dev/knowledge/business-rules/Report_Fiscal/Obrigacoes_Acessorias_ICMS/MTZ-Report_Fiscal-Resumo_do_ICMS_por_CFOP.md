---
source: "MTZ-Report_Fiscal-Resumo_do_ICMS_por_CFOP.doc"
category: Report_Fiscal
converted: auto
---

Report Fiscal - Resumo do ICMS por CFOP


    Localização: 
       Módulo: Básicos --> Report Fiscal
       Menu:    Obrigações Acessorias --> ICMS --> Resumo do ICMS p/Data Mart --> Código Fiscal de Operação - CFOP


DOCUMENTO DE REQUISITO

DR
Nome
Descrição
OS2484
Inclusão do Parâmetro "UF" na Emissão de Relatórios

Incluir o parâmetro "UF" na emissão dos relatórios.

CH53707
Correção do Relatório
Corrigir relatório quando o campo UF estiver me branco
CH1961_2013
Alteração para geração do documentos mistos
Alterar a geração da coluna IPI para a geração de documentos fiscais mistos.
MFS70245
Andréa Rocha
Incluir a coluna de Valor de Despesa no relatório.


REGRAS DE NEGÓCIO

Cód.
Descrição
DR
RN00
O cursor deverá apontar para o 1º campo da tela de parametrização, ou seja, para o parâmetro "UF".
OS2484
RN01
O conteúdo do campo "Estabelecimento" será de acordo com o estado selecionado no campo "UF", sendo apenas apresentado(s) o(s) estabelecimento(s) pertinente(s) àquele estado. Dessa forma o usuário poderá emitir o relatório para apenas um estabelecimento do estado selecionado ou todos os estabelecimentos do mesmo estado.
OS2484
RN02
Se o campo "UF" estiver em branco, o campo "Estabelecimento" deve apresentar todos os estabelecimentos cadastrados para a empresa em questão, deixando a critério do o usuário a emissão do relatório para apenas um estabelecimento ou todos os estabelecimentos separados por estado.
OS2484
RN03
O parâmetro "UF" deve conter as siglas dos estados da tabela TFIX04 (Tabela de Estados).
OS2484
RN04
O campo "UF" do relatório deve apresentar a sigla do estado selecionado na parametrização da emissão do relatório. 
OS2484
RN05
Se o modo de emissão for apenas para um estabelecimento específico, o campo "UF" deve apresentar a sigla do estado do estabelecimento.
OS2484
RN06

Se na tela de critério de seleção campo "UF" estiver em branco, o campo "Estabelecimento" selecionado "todos" e Tipo do relatório for sintético, o relatório impresso deverá ter os campos UF, Inscrição Estadual e CNPJ em branco no cabeçalho.


CH53707
RN07
Quando selecionada a opção "Considerar notas de Serviço com CFOP's do ajuste SINIEF 03/04" na tela de geração do relatório, os documentos fiscais de classificação mista (campo 12 da SAFX07 = 3), que não tiverem itens de mercadoria (safx08), deverão apresentar os valores de IPI que constam na SAFX07, caso alguma das bases esteja preenchida.

CH1961_2013
RN08
Incluir a coluna "Valor Despesas" no final do relatório.

Esta coluna conterá a totalização do campo "41- Valor de Outras Despesas" dos itens de documento fiscal (SAFX08) ou será preenchido com o campo "26- Valor de Outras Despesas" da capa de documento fiscal (SAFX07), para as notas sem itens.

MFS70245

