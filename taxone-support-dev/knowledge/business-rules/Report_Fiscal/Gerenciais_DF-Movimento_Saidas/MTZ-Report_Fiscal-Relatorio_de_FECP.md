---
source: "MTZ-Report_Fiscal-Relatorio_de_FECP.doc"
category: Report_Fiscal
converted: auto
---

REPORT FISCAL - Relatório de FECP

BÁSICOS ? REPORT FISCAL ? Gerenciais --> Documentos Fiscais --> Conferência de Notas Fiscais / FECEP


DOCUMENTO DE REQUISITO

DR
Nome
Descrição
CH77131
Inclusão de Filtro p/ Notas Fiscais de "Entrada / Saídas / Ambos".

O relatório de Conferência de Notas Fiscais/FECP terá a partir de agora um filtro de Documentos Fiscais de Entrada / Saída ou Ambos, para facilitar a conferência dos usuários
OS4026
Melhoria Report Fiscal
Inclusão de filtro para considerar apenas os itens com FECEP (ver RN02)
MFS6705
Relatório CONFERENCIA NOTAS FISCAIS FECEP
Melhoria na geração do relatório CONFERENCIA NOTAS FISCAIS FECEP apareça a mensagem que o mesmo está sem movimento
MFS27079
Andréa Rocha
Inclusão do filtro de UF na tela.
MFS29811
Andréa Rocha
Inclusão do filtro de UF para a geração do campo UF do relatório.
MFS84762
Rogério Ohashi
Inclusão de parâmetro para considerar também o valor de Base Outras (ver RN05)

REGRAS DE NEGÓCIO

Cód.
Descrição
DR
RN00
Tela de Critérios:

[MFS27079]

UF: Deverá mostrar todas as UF's da tabela Estado, mais a opção "Todas". Após realizar a seleção, no campo Estabelecimento desta mesma tela, somente deverão aparecer os estabelecimentos que pertencerem à UF selecionada (Campo UF da tabela ESTABELECIMENTO). Se selecionar a opção "Todas", deverão ser mostrados todos os estabelecimentos.

Documentos: Deverá conter as seguintes opções:
- Todos Documentos;
- Documentos Cancelados;
- Documentos Com Situação Normal.

Tipo de Movimento: Deverá conter as seguintes opções:
1 - Entrada;
2 - Saída;
3 - Ambos.

Período: Deverá ter um campo para o usuário informar a data inicial e um para a data final.

Somente itens com FECEP: Campo do tipo checkbox, default desmarcado.

[MFS29811]
Identificação da UF: Deverá ser um campo do tipo Radiobutton, com as seguintes opções:
- PFJ da Nota
- Campo Destino da NF (esta opção deve vir marcada como default)

Estabelecimento: Deverá mostrar um quadro com todos os estabelecimentos que o usuário tiver acesso, de acordo com a seleção do campo UF.  Deverão ter as opções "Selecionar Todos" e "Desmarcar Todos".

CH77131/
MFS27079/
MFS29811
RN01
Quando o cliente selecionar a opção:
1 - Entrada: O sistema deverá seguir os padrões de filtros atuais e recuperar os documentos cujo campo 03 da SAFX07 esteja classificado como 1; 2; 3; 4 ou 5.
2 - Saída: O sistema deverá seguir os padrões de filtros atuais e recuperar os documentos cujo campo 03 da SAFX07 esteja classificado como 9
3 - Ambos: O sistema deverá seguir os padrões de filtros atuais e recuperar os documentos cujo campo 03 da SAFX07 esteja classificado como 1; 2; 3; 4; 5 ou 9.
CH77131
RN02

Parâmetro "Somente itens com FECEP":

Este parâmetro foi incluído na OS4026, e funciona da seguinte forma:

Default --> desmarcado (conforme funcionamento original)

Utilização do parâmetro na geração do relatório:

Se desmarcado --> a geração considera todos os itens que atendam aos demais critérios de seleção do relatório,
                            independente do item ter ou não valores de FECEP (conforme funcionamento original);
 
Se marcado --> a geração considera apenas os itens que atendam aos demais critérios de seleção do relatório e que tenham
                       algum dos campos de FECEP preenchido com valor <> zero (campo "138-FECEP ICMS", "139-FECEP
                       Diferencial de Alíquota", "140-FECEP ICMS-ST" ou "141-FECEP Regime Fonte");


OS4026
RN03
De acordo com os critérios informados na tela de emissão caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a mensagem "SEM MOVIMENTO".
MFS6705
RN04
Parâmetro "Identificação da UF":

SE for selecionada a opção "PFJ da Nota", deve recuperar os dados da UF da PFJ, ou seja, do campo 19 - UF da SAFX04.

SE for selecionada a opção "Campo Destino da NF", deve recuperar os dados do campo 122 - UF_DESTINO (SAFX07)

MFS29811
RN05
Parâmetro "Considerar Base Outras":

Este parâmetro deverá funcionar da seguinte forma:

Default --> desmarcado (conforme funcionamento original)

Utilização do parâmetro na geração do relatório para tratamento da coluna "BASE":

Se desmarcado --> a geração considera os itens com valor constante no campo 56 - BASE_ICMS para campo 55 - TRIB_ICMS = 1 e 61 - BASE_SUB_TRIB_ICMS (SAFX08) que atendam aos demais critérios de seleção do relatório (conforme funcionamento original);
 
Se marcado --> a geração deverá considerar os itens que atendam aos demais critérios de seleção do relatório e, considerar a soma dos campos abaixo:

Base (ICMS Próprio): Considerar a soma dos valores constantes do campo de Base de ICMS (Campo 56 - BASE_ICMS para campo 55 - TRIB_ICMS = '1') (+) Base ICMS Outras (Campo 56 - BASE_ICMS para campo 55 - TRIB_ICMS = '3') da tabela SAFX08;

                        --> VLR_BASE_ICMS_1 + VLR_BASE_ICMS_3  da tabela DWT_ITENS_MERC.
              

Base (ICMS ST): Considerar a soma dos valores constantes do campo de Base ICMS-ST (Campo 61 - BASE_SUB_TRIB_ICMS (+) Base ICMS-ST Outras (Campo 61 - BASE_SUB_TRIB_ICMS e 94 - TRIB_ICMSS = 3) da SAFX08.  
 
                       --> VLR_BASE_ICMSS + VLR_BASE_ICMSS_3  da tabela DWT_ITENS_MERC.

MFS84762


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

