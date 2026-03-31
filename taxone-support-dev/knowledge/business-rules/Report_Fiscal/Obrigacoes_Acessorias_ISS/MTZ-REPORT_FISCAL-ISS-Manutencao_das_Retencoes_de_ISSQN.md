---
source: "MTZ-REPORT_FISCAL-ISS-Manutencao_das_Retencoes_de_ISSQN.doc"
category: Report_Fiscal
converted: auto
---

REPORT FISCAL => ISS => Manutenção das Retenções de ISSQN


DOCUMENTO DE REQUISITO

DR
Nome
Descrição

OS3096-A3

Alteração na Manutenção das Retenções de ISSQN

Criar a opção de geração por Multi-empresa.


OS3479


Melhoria no relatório - Inclusão das informações: Código Serviço e Tipo Documento


Melhoria no relatório - Inclusão das informações: Código Serviço e Tipo Documento

OS3412
Melhoria no relatório 
Inclusão da flag Demonstrar valores de ISS igual a zero
CH120893
DW - BÁSICOS - REPORT FISCAL - Listar apenas Estabelecimentos Centralizadores e Estabelecimentos Centralizados para o Relatório das Retenções de ISSQN.
Esta demanda tem o objetivo de corrigir a recuperação dos campos Estab. Centralizador e Estab. Centralizado na tela do Report Fiscal - Obrigações Acessórias - ISS - Manutenção de Retenções de ISSQN - Relatório.

REGRAS DE NEGÓCIO

Cód.
Descrição
DR
RN00

O menu: REPORT FISCAL => ISS => Manutenção das Retenções de ISSQN

Essa opção terá os mesmos filtros que a atualmente, com inclusão do campo EMPRESA.

OS3096-A3
RN01

O campo EMPRESA irá listar:

* TODAS - Quando selecionado, todas as Empresas que tiverem movimentação (RN01) no período e demais filtros escolhidos serão demonstradas no relatório.
* Cada uma das Empresas cadastradas - Quando selecionada, caso tenha movimentação no período e demais filtros escolhidos será demonstrada no relatório.

OS3096-A3
RN02

Ao definir a EMPRESA, o usuário também deverá definir o ESTABELECIMENTO, para inserir dados com sucesso.

OS3096-A3
RN03
O Relatório terá o mesmo layout que o atual, incluindo o Código da Empresa do lado esquerdo da descrição no Cabeçalho.

Os Estabelecimentos serão ordenados por EMPRESA.

OS3096-A3
RN04
Deve-se incluir a opção EMPRESA nos critérios de busca.
OS3096-A3
RN05

Regra para campo Tipo Documento:

Módulo: Básicos ? Report Fiscal
Menu: Obrigações Acessórias ? ISS ? Manutenção das retenções de ISSQN (Geração do Relatório)

Na geração do relatório, o campo TIPO DOCUMENTO deve recuperar a informação do Campo 05 - DOC_DOCTO (SAFX07) quando:

- Campo 11 - DATA_EMISSAO for pertinente ao período de geração


OS3479

RN06
Regra para campo Código Serviço Lei 116:

Módulo: Básicos ? Report Fiscal
Menu: Obrigações Acessórias ? ISS ? Manutenção das retenções de ISSQN (Geração do Relatório)

Na geração do relatório, o campo Código Serviço Lei 116 deve recuperar a informação do Campo 20 - COD_SERV_LEI_116 (SAFX2018), referente ao Campo 01 - COD_SERVICO (SAFX2018), devendo estar cadastrada no Campo 12 - COD_SERVICO (SAFX09), quando:

- Campo 11 - DATA_EMISSAO for pertinente ao período de geração


OS3479

RN07
Tela critério de seleção Relatório das Retenções de ISSQN - Campo "Demonstração de Valores de ISS"

Campo do tipo listbox, com as seguintes opções: "Todos os valores de ISS", "Valores de ISS diferente de zero" e "Valores de ISS igual a zero". Opção "Todos os valores de ISS" selecionada por default.

Se a opção "Todos os valores de ISS" for selecionada:
       Devem ser recuperadas as notas fiscais tanto com o valor do ISS igual a zero ou diferente de zero.
Para as notas fiscais com item, considerar o campo VLR_ISS  da DWT_ITENS_SERV.
Para as notas fiscais sem item, considerar o campo VLR_ISS  da DWT_DOCTO FISCAL.

Se a opção "Valores de ISS diferente de zero" for selecionada: 
       Devem ser recuperadas somente as notas fiscais que possuírem valor de ISS > zero
Para as notas fiscais com item, considerar o campo VLR_ISS  da DWT_ITENS_SERV.
Para as notas fiscais sem item, considerar o campo VLR_ISS  da DWT_DOCTO FISCAL.

Se a opção "Valores de ISS igual a zero" for selecionada:
       Devem ser recuperadas somente as notas fiscais que possuírem valor do ISS = zero ou sem preenchimento
Para as notas fiscais com item, considerar o campo VLR_ISS  da DWT_ITENS_SERV.
Para as notas fiscais sem item, considerar o campo VLR_ISS  da DWT_DOCTO FISCAL.

OS3412
RN08
Regra para campo Estab. Centralizador:

Módulo: Básicos ? Report Fiscal
Menu: Obrigações Acessórias ? ISS ? Manutenção das retenções de ISSQN (Geração do Relatório)

Esse campo deve ser um ListBox e deve exibir apenas os estabelecimentos classificados como centralizador na tela Report Fiscal ? Obrigações Acessórias ? ISS ? Centralização do Estabelecimento. Esse campo também deverá exibir a opção "Todos", que permite que todos os estabelecimentos centralizadores sejam recuperados no relatório.

CH120893
RN09
Regra para campo Estab. Centralizado:

Módulo: Básicos ? Report Fiscal
Menu: Obrigações Acessórias ? ISS ? Manutenção das retenções de ISSQN (Geração do Relatório)

Esse campo deve ser um ListBox e deve exibir apenas os estabelecimentos classificados como centralizados, referente ao estabelecimento centralizador escolhido anteriormente, na tela Report Fiscal ? Obrigações Acessórias ? ISS ? Centralização do Estabelecimento. Esse campo também deverá exibir a opção "Todos", que permite que todos os estabelecimentos centralizados referentes ao estabelecimento centralizador sejam recuperados no relatório.

CH120893


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

