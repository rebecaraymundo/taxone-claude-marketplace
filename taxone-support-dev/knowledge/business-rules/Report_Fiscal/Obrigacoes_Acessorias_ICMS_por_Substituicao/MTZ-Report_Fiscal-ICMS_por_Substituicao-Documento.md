---
source: "MTZ-Report_Fiscal-ICMS_por_Substituicao-Documento.doc"
category: Report_Fiscal
converted: auto
---

Relatório de ICMS Substituição ? Por Documento

BÁSICOS ? REPORT FISCAL ? Obrigações Acessórias ? ICMS por Substituição ? Operações com Substituição Tributária ? Documento


DOCUMENTO DE REQUISITO

DR
Nome
Descrição
OS2626-D1
Contemplar parâmetro de notas de serviço

Permitir que no relatório sejam geradas as notas fiscais de serviço, conforme Ajuste Sinief 03/04.
CH21473_2016
Lara Aline
Ajustar a informação da coluna num_cfo no relatório salvo em excel.
MFS24131
Andréa Rocha
Incluir o filtro de UF na tela.
MFS-33584
Alessandra Cristina Navatta
Incluir filtro 'Considerar Somente NFs com Crédito de ICMS-ST (Flag Apropria Marcado)', na tela

REGRAS DE NEGÓCIO

Cód.
Descrição
DR
RN00
Regras Gerais:


RN01
Tela de Critérios:

[MFS24131]

UF: Deverá mostrar todas as UF's da tabela Estado, mais a opção "Todas". Após realizar a seleção, no campo Estabelecimento desta mesma tela, somente deverão aparecer os estabelecimentos que pertencerem à UF selecionada (Campo UF da tabela ESTABELECIMENTO). Se selecionar a opção "Todas", deverão ser mostrados todos os estabelecimentos.

Período: Deverá ter um campo para o usuário informar a data inicial e um para a data final.

Tipo de Movimento: Deverá conter as seguintes opções:
1 - Entrada
2 - Saída

Normal/Devolução: Deverá conter as seguintes opções:
1 - Normal
2 - Devolução

Tipo: Deverá conter as seguintes opções: Analítico e Sintético

[ALTERAÇÃO - MFS-33584] - Inclusão do filtro 'Considerar Somente NFs com Crédito de ICMS-ST (Flag Apropria Marcado)'

Considerar Somente NFs com Crédito de ICMS-ST (Flag Apropria Marcado): Virá por default desmarcado
Se desmarcado, busca o registro independente se o flag 'Apropria' está ou não marcado. Considere o campo 78- IND_CRED_ICMSS da SAFX08 com 'N' ou 'S', quando existir itens na nota; caso a nota não possua item, considere o indicador da capa (campo 82- IND_CRED_ICMSS da SAFX7 com 'N' ou 'S').
Se marcado, busca apenas os registros que possuem o flag 'Apropria' marcado. Considere o campo 78- IND_CRED_ICMSS da SAFX08 com 'S', quando existir itens na nota; caso a nota não possua item, considere o indicador da capa (campo 82- IND_CRED_ICMSS da SAFX7 com 'S').


Recuperar UF Origem/Destino dos Documentos Fiscais: Virá por default desmarcado.
Se desmarcado, busca os dados de UF/Município da pessoa fis/jur da NF
Se marcado, busca os dados de UF/Município da capa da NF

Estabelecimento: deverá mostrar um quadro com todos os estabelecimentos que o usuário tiver acesso, de acordo com a seleção do campo UF.  Deverão ter as opções "Selecionar Todos" e "Desmarcar Todos".

Considerar Notas de Serviço com CFOP's do Ajuste Sinief 03/04: Virá por default desmarcado.
Se desmarcado, busca os dados das NF's classificação 1 - mercadoria e 3 - mista, apenas com o item de mercadoria.
Se marcado, busca os dados das NF's classificação 1 - mercadoria, 3 - mistas, 2 - serviços

OS2626-D1/
MFS24131
MFS-33584
RN02
Parâmetro "Considerar Notas de Serviço com CFOP's do Ajuste Sinief 03/04":

SE não estiver marcado:
Buscar as NF's de mercadoria e mistas (apenas com o item de mercadoria) que tenham valores de ST (apropriados ou não).

SE estiver marcado:
Buscar as NF's de mercadoria e mistas (classificação 1, 3 e 2) que tenham valores de ST (apropriados ou não).
As NF's  com classificação 3 (mistas), deverão gerar com o item de mercadoria e com o item do serviço.
As NF's com classificação 2 (serviço), somente serão consideradas se o CFOP estiver parametrizado em:
Estadual ? ICMS ? Manutenção ? Parâmetros para Serviços de NF's Conjugadas ? CFOP para Itens de Serviço conforme Ajuste Sinief

OS2626-D1
RN03
Coluna CFOP em excel

Gravar a informação do código de CFOP na coluna num_cfo no relatório em formato excel, atualmente ao salvar o relatório em excel existe uma coluna para informação do CFOP do documento (num_cfo), porém, sem nenhuma informação gravada. Dessa forma será ajustado o relatório salvo em excel para gravar a informação do CFOP desses documentos na coluna num_cfo.

CH21473_2016


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN


