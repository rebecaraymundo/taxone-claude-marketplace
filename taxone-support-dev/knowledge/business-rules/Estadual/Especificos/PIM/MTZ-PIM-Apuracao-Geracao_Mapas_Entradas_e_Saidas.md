# MTZ-PIM-Apuracao-Geracao_Mapas_Entradas_e_Saidas

- **Fonte:** MTZ-PIM-Apuracao-Geracao_Mapas_Entradas_e_Saidas.docx
- **Modificado:** 2022-04-28
- **Tamanho:** 81 KB

---

THOMSON REUTERS

                                                 __Módulo PIM – Geração dos Mapas de Entradas e Saídas__

__ __

__ __

__Localização__: Menu Específicos, Módulo PIM, item Apuração 🡪 Geração dos Mapas 🡪 Entradas e Saídas

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS4593\-A

Tratamento das subapurações do Sped Fiscal no módulo PIM

Correção de erro na chamada da geração do mapa das entradas

17/09/2014

\(criação do docto\)

MFS85056

Liliane Assaf

Alteração na geração dos mapas de saídas incentivadas \(componente 01\) para gravar a Tabela de Itens de Nota Fiscal para emissão do Relatório Analítico dos Mapas \(ICT\_AM\_AP\_IT\_NF\)

A tabela ICT\_AM\_AP\_IT\_NF foi criada pela MFS\-84429

28/04/2022

MFS67675

Liliane Assaf

Alteração na geração dos mapas de entradas incentivadas e não incentivadas \(componentes 02 e 04\) e saídas não incentivadas \(componente 03\) para gravar a Tabela de Itens de Nota Fiscal para emissão do Relatório Analítico dos Mapas \(ICT\_AM\_AP\_IT\_NF\)

A tabela ICT\_AM\_AP\_IT\_NF foi criada pela MFS\-84429

28/04/2022

	

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

Correção de erro \- OS4593\-A:

 

A geração dos mapas das entradas e saídas trabalha com várias procedures\. Foi identificado um erro na chamada da geração das entradas, que não tratava a possibilidade da coluna IND\_CALC\_ENT da tabela ICT\_ESTAB\_IESTAD estar sem informação \(tabela do cadastro das IE’s, menu “Cadastros 🡪 Inscrição Estadual por Estabelecimento”\)\. Esta coluna corresponde ao parâmetro “Árvore de Produtos”, que __não__ é mais utilizado no Módulo PIM *\(para maiores detalhes, consultar o item 2\.1\.9 do documento de requisito da OS4593\-A\)*\. 

Com a correção a apuração das entradas passou a ser executada da seguinte forma:

       \- Se parâmetro \(IND\_CALC\_ENT\) = “0” 🡪 chama a procedure SAF\_AP\_ICMS\_AM\_EN \(s\_iaapen\)

       \- Se parâmetro \(IND\_CALC\_ENT\) __nulo ou__ = “1” 🡪 chama a procedure SAF\_AP\_ICMS\_AM\_EN2 \(s\_iaape2\)

__RN01__

__                                     Regra para Geração do Mapa das Saídas \(Incentivadas e Não Incentivadas\)__

Componentes: 01 – ICMS Normal Referente a Saídas Incentivadas

                        03 \-  ICMS Normal Referente a Saídas Não Incentivadas

Procedure: SAF\_AP\_ICMS\_AM\_SA

Recuperação das notas fiscais \(SAFX07, SAFX08\) que obedeçam aos critérios a seguir:

\- Notas fiscais que pertençam ao estabelecimento e inscrição estadual selecionados em tela,

\- Notas fiscais com item de mercadoria 

  Ou

  Notas fiscais sem item de mercadorias

\- Notas fiscais de saída \(MOVTO\_E\_S = ‘9’\),

\- Notas fiscais não canceladas,

\- Classificação de mercadoria igual a ‘1’, ’ 3’ e ‘4’,

Para notas com itens de mercadoria, recuperar:

\- Produto do item de Mercadoria

\- CFOP <a id="_Hlk101375683"></a>do item de Mercadoria

\- Natureza de Operação do item de Mercadoria

\- Valor Contabil Item do item de Mercadoria

\- Valores de Bases e tributo do ICMS do item de Mercadoria

Para nota sem item de mercadoria recuperar:

\- CFOP <a id="_Hlk101375839"></a>da capa da nota \(safx07\)

\- Natureza de Operação da capa da nota \(safx07\)

\- Valor Total da Nota da capa da nota \(safx07\)

\- Valores de Bases e tributo do ICMS da capa da nota \(safx07\)

Para os documentos fiscais recuperados, verificar:

\- Verificar se o produto é incentivado ou não incentivado;

\- Verificar se o CFOP ou CFOP/Natureza está parametrizado para o componente 01 – Saída Incentivada  ou 03 – Saída Não Incentivada\.

Serão considerados os documentos fiscais com item de mercadoria com produtos incentivados:

\- Produto está parametrizado para uma linha de incentivo \(Cadastros > Linhas de incentivos > Linhas de produtos incentivados\), e CFOP ou CFOP/Natureza está parametrizado para o componente 01 \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza\)\.

Serão considerados os documentos fiscais com item de mercadoria com produtos não incentivados:

\- Produto NÃO está parametrizado para uma linha de incentivo \(Cadastros > Linhas de incentivos > Linhas de produtos incentivados\), e CFOP ou CFOP/Natureza está parametrizado para o componente 03 \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza\)\.

Serão considerados os documentos fiscais sem item de mercadoria:

\- CFOP ou CFOP/Natureza está parametrizado para o componente 03 \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza\)\.

O resultado deve ser gravado nas seguintes tabelas:

\- Resumo por CFOP \(ICT\_AP\_CFO\_IES\)

\- Resumo por Produto \(ICT\_AM\_AP\_PRD\) 🡪 usada no cálculo do componente 05\.

\- Mapa Entrada/Saída \(ICT\_AM\_AP\_E\_S\)

\- Itens de Nota Fiscal para Relatório Analítico dos Mapas \(ICT\_AM\_AP\_IT\_NF\)

__\[MFS85056\]: __<a id="_Hlk102071511"></a>__Gravação da Tabela de Itens de Nota Fiscal na geração do componente 01__

__\[MFS67675\]: Gravação da Tabela de Itens de Nota Fiscal na geração do componente 03__

__Gravação da Tabela de Itens de Nota Fiscal para Relatório Analítico dos Mapas__:

Todas as notas foram consideradas na geração dos componentes 01 e 03, devem ser gravadas na tabela a seguir, a fim de gerar o Relatório Analítico dos Mapas\. 

O Relatório Analítio dos Mapas está disponivel no módulo PIM, menu: Relatórios 🡪 Emissão dos Mapas 🡪 Relatório Analítico dos Mapas\.

__Tabela ICT\_AM\_AP\_IT\_NF__:

Campo

Regra de Preenchimento

COD\_EMPRESA

Código da empresa de login

COD\_ESTAB

Código do estabelecimento da nota fiscal considerada nessa geração

INSC\_ESTADUAL

Inscrição Estadual PIM da nota fiscal \(campo 126 da SAFX07\)

DAT\_APURACAO

Data Fim do Periodo informado na Tela de Geração dos Mapas de Entrada/Saída

COD\_LINHA\_PRD

Código da Linha de Incentivo parametrizado para o produto da nota fiscal\.

Se a nota não tiver item de mercadoria, ou se o produto não for incentivado, preencher este campo com ‘ ‘ \(um espaço\)\.

COD\_COMP\_APUR

Código do Componente \(01 ou 03\) parametrizado ao CFOP ou CFOP/Natureza da nota em \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza\)

COD\_ESTRUT

Código da Estrutura parametrizado ao CFOP ou CFOP/Natureza da nota em \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza\)

COD\_ITEM\_APUR

Código do Item parametrizado ao CFOP ou CFOP/Natureza da nota em \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza\)

DATA\_FISCAL

Data Fiscal da nota fiscal

MOVTO\_E\_S

Indicador Movimento Entrada/Saída da nota fiscal \(campo 03 da SAFX07\)

NORM\_DEV

Indicador de Normal ou Devolução da nota fiscal \(campo 04 da SAFX07\)

IDENT\_DOCTO

Identificador do Tipo do Documento da nota fiscal \(referente ao campo 05 da SAFX07\)

IDENT\_FIS\_JUR

Identificador Pessoa Física Jurídica da nota fiscal \(referente ao campo 06, 07 da SAFX07\)

NUM\_DOCFIS

Número do Documento Fiscal \(campo 08 da SAFX07\)

SERIE\_DOCFIS

Série do Documento Fiscal \(campo 09 da SAFX07\)

SUB\_SERIE\_DOCFIS

Subsérie do Documento Fiscal \(campo 10 da SAFX07\)

DISCRI\_ITEM

Preencher com o DISCR\_ITEM da DWT\_ITENS\_MERC\.

Se a nota não tiver item de mercadoria, não preencher este campo\.

NUM\_ITEM

Número do Item de mercadoria \(campo 18 da SAFX08\)

Se a nota não tiver item de mercadoria, não preencher este campo\.

IDENT\_PRODUTO

Identificador do Produto do item de mercadoria \(referente aos campos 13, 14 da SAFX08\)\.

Se a nota não tiver item de mercadoria, não preencher este campo\.

IDENT\_CFO

Identificador do CFOP do item de mercadoria \(referente ao campo 22 da SAFX08\)\.

Se a nota não tiver item de mercadoria, considerar o CFOP da capa \(campo 14 da SAFX07\)\.

IDENT\_NATUREZA\_OP

Identificador da Natureza de Operação do item de mercadoria \(referente ao campo 23 da SAFX08\)\.

Se a nota não tiver item de mercadoria, considerar a Natureza da Operação da capa \(campo 15 da SAFX07\)\.

VLR\_CONTAB\_ITEM

Valor Contabil do Item de mercadoria \(campo 64 da SAFX08\)\.

Se a nota não tiver item de mercadoria, considerar o Valor Total da Nota  da capa \(campo 23 da SAFX07\)\.

ALIQ\_TRIBUTO\_CMS

Alíquota do Tributo ICMS do item de mercadoria \(campo 42 da SAFX08\)\.

Se a nota não tiver item de mercadoria, considerar a Alíquota do ICMS da capa \(campo 34 da SAFX07\)\.

VLR\_TRIBUTO\_ICMS

Valor do Tributo ICMS do item de mercadoria \(campo 43 da SAFX08\)\.

Se a nota não tiver item de mercadoria, considerar o Valor do ICMS da capa \(campo 35 da SAFX07\)\.

VLR\_BASE\_ICMS\_TRIB

Base Tributada ICMS do item de mercadoria \(VLR\_BASE\_ICMS\_1 da DWT\_ITENS\_MERC\)

Se a nota não tiver item de mercadoria, considerar a Base Tributada ICMS da capa \(campo 51 da SAFX07\)\.

VLR\_BASE\_ICMS\_ISENT

Base Isenta \+ Reduzida ICMS do item de mercadoria \(VLR\_BASE\_ICMS\_2 \+  VLR\_BASE\_ICMS\_4 da DWT\_ITENS\_MERC\)\.

Se a nota não tiver item de mercadoria, considerar a Base Isenta \+ Reduzida ICMS da capa \(campo 52, 54 da SAFX07\)\.

VLR\_BASE\_ICMS\_OUTR

Verificar o parâmetro “ICMS Retido/Outras” da Tela de Geração dos Mapas Entrada/Saída\.

Se parâmetro “ICMS Retido/Outras” estiver marcado, então:

  Preencher este campo com Base Outras ICMS \+ Valor do ICMS\-ST\.

Senão

  Preencher este campo com Base Outras ICMS\.  

Se a nota não tiver item de mercadoria, considerar a Base Outras ICMS e Valor ICMS\-ST da capa \(campo 53, 48 da SAFX07\)\.

Se a nota tiver item de mercadoria, considerar os valores do item de mercadoria \(VLR\_BASE\_ICMS\_3 e VLR\_TRIBUTO\_ICMSS da DWT\_ITENS\_MERC\)\.

ALIQ\_TRIBUTO\_ICMSS

Alíquota do Tributo ICMS\-ST do item de mercadoria \(campo 51 da SAFX08\)\.

Para nota sem item de mercadoria, considerar a Alíquota ICMS\-ST da capa \(campo 47 da SAFX07\)\.

VLV\_TRIBUTO\_ICMSS

Valor do Tributo ICMS\-ST do item de mercadoria \(campo 52 da SAFX08\)\.

Para nota sem item de mercadoria, considerar o valor ICMS\-ST da capa \(campo 48 da SAFX07\)\.

VLR\_BASE\_ICMSS

Valor da Base ICMS\-ST do item de mercadoria \(campo 61 da SAFX08\)\.

Para nota sem item de mercadoria, considerar a base ICMS\-ST da capa \(campo 64 da SAFX07\)\.

VLR\_TAXA

Não Preencher

VLR\_CONTRIBUICAO

Não Preencher

USUARIO

Usuário de login da aplicação

NUM\_PROCESSO

Número do processo da Geração dos Mapas de Entrada e Saída

__RN02__

__                                Regra para Geração do Mapa das Entradas \(Incentivadas e Não Incentivadas\)__

Componentes: 02 \- ICMS Normal Referente a Entradas Incentivadas

                        04 \-  ICMS Normal Referente a Entradas Não Incentivadas

                        05 \- Operações com Proporcionalidade dos Créditos nas Entradas \(pendência de especificação\)

Procedure: SAF\_AP\_ICMS\_AM\_EN2

Recuperação das notas fiscais \(SAFX07, SAFX08\) que obedeçam aos critérios a seguir:

\- Notas fiscais que pertençam ao estabelecimento e inscrição estadual selecionados em tela,

\- Notas fiscais com item de mercadoria 

  Ou

  Notas fiscais sem item de mercadorias

\- Notas fiscais de entrada \(MOVTO\_E\_S <> ‘9’\),

\- Notas fiscais não canceladas,

\- Classificação de mercadoria igual a ‘1’, ’ 3’,

Para notas com itens de mercadoria, recuperar:

\- Produto do item de Mercadoria

\- CFOP do item de Mercadoria

\- Natureza de Operação do item de Mercadoria

\- Valor Contabil Item do item de Mercadoria

\- Valores de Bases e tributo do ICMS do item de Mercadoria

Para nota sem item de mercadoria recuperar:

\- CFOP da capa da nota \(safx07\)

\- Natureza de Operação da capa da nota \(safx07\)

\- Valor Total da Nota da capa da nota \(safx07\)

\- Valores de Bases e tributo do ICMS da capa da nota \(safx07\)

Para os documentos fiscais recuperados, verificar:

\- Verificar se o produto é incentivado ou não incentivado;

\- Verificar se o CFOP ou CFOP/Natureza está parametrizado para o componente 02 – Entrada Incentivada  ou 04  – Entrada Não Incentivada\.

Serão considerados os documentos fiscais com item de mercadoria com produtos incentivados:

\- Produto está parametrizado para uma linha de incentivo \(Cadastros > Linhas de incentivos > Linhas de produtos incentivados\), e CFOP ou CFOP/Natureza está parametrizado para o componente 02 \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza\)\.

Serão considerados os documentos fiscais com item de mercadoria com produtos não incentivados:

\- Produto NÃO está parametrizado para uma linha de incentivo \(Cadastros > Linhas de incentivos > Linhas de produtos incentivados\), e CFOP ou CFOP/Natureza está parametrizado para o componente 04 \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza\)\.

Serão considerados os documentos fiscais sem item de mercadoria:

\- CFOP ou CFOP/Natureza está parametrizado para o componente 04 \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza\)\.

O resultado deve ser gravado nas seguintes tabelas:

\- Resumo por CFOP \(ICT\_AM\_MPRES\_CFO\)

\- Mapa Entrada/Saída \(ICT\_AM\_AP\_E\_S\)

\- Itens de Nota Fiscal para Relatório Analítico dos Mapas \(ICT\_AM\_AP\_IT\_NF\)

__\[MFS67675\]: Gravação da Tabela de Itens de Nota Fiscal na geração dos componentes 02 e 04__

__Gravação da Tabela de Itens de Nota Fiscal para Relatório Analítico dos Mapas__:

Todas as notas foram consideradas na geração dos componentes __02__ e __04__, devem ser gravadas na tabela a seguir, a fim de gerar o Relatório Analítico dos Mapas\. 

O Relatório Analítio dos Mapas está disponivel no módulo PIM, menu: Relatórios 🡪 Emissão dos Mapas 🡪 Relatório Analítico dos Mapas\.

OBS: Não estamos gravando as notas consideradas para geração do componente 05, pois não há demanda de cliente\.

__Tabela ICT\_AM\_AP\_IT\_NF__:

Campo

Regra de Preenchimento

COD\_EMPRESA

Código da empresa de login

COD\_ESTAB

Código do estabelecimento da nota fiscal considerada na geração

INSC\_ESTADUAL

Inscrição Estadual PIM da nota fiscal \(campo 126 da SAFX07\)

DAT\_APURACAO

Data Fim do Periodo informado na Tela de Geração dos Mapas de Entrada e Saída

COD\_LINHA\_PRD

Código da Linha de Incentivo parametrizado para o produto da nota fiscal\.

Se a nota não tiver item de mercadoria, ou se o produto não for incentivado, preencher este campo com ‘ ‘ \(um espaço\)\.

COD\_COMP\_APUR

Código do Componente \(02, 04\) parametrizado ao CFOP ou CFOP/Natureza da nota em \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza\)

COD\_ESTRUT

Código da Estrutura parametrizado ao CFOP ou CFOP/Natureza da nota em \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza\)

COD\_ITEM\_APUR

Código do Item parametrizado ao CFOP ou CFOP/Natureza da nota em \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza\)

DATA\_FISCAL

Data Fiscal da nota fiscal

MOVTO\_E\_S

Indicador Movimento Entrada/Saída da nota fiscal \(campo 03 da SAFX07\)

NORM\_DEV

Indicador de Normal ou Devolução da nota fiscal \(campo 04 da SAFX07\)

IDENT\_DOCTO

Identificador do Tipo do Documento da nota fiscal \(referente ao campo 05 da SAFX07\)

IDENT\_FIS\_JUR

Identificador Pessoa Física Jurídica da nota fiscal \(referente ao campo 06, 07 da SAFX07\)

NUM\_DOCFIS

Número do Documento Fiscal \(campo 08 da SAFX07\)

SERIE\_DOCFIS

Série do Documento Fiscal \(campo 09 da SAFX07\)

SUB\_SERIE\_DOCFIS

Subsérie do Documento Fiscal \(campo 10 da SAFX07\)

DISCRI\_ITEM

Preencher com o DISCR\_ITEM da DWT\_ITENS\_MERC\.

Se a nota não tiver item de mercadoria, não preencher este campo\.

NUM\_ITEM

Número do Item de mercadoria \(campo 18 da SAFX08\)

Se a nota não tiver item de mercadoria, não preencher este campo\.

IDENT\_PRODUTO

Identificador do Produto do item de mercadoria \(referente aos campos 13, 14 da SAFX08\)\.

Se a nota não tiver item de mercadoria, não preencher este campo\.

IDENT\_CFO

Identificador do CFOP do item de mercadoria \(referente ao campo 22 da SAFX08\)\.

Se a nota não tiver item de mercadoria, considerar o CFOP da capa \(campo 14 da SAFX07\)\.

IDENT\_NATUREZA\_OP

Identificador da Natureza de Operação do item de mercadoria \(referente ao campo 23 da SAFX08\)\.

Se a nota não tiver item de mercadoria, considerar a Natureza da Operação da capa \(campo 15 da SAFX07\)\.

VLR\_CONTAB\_ITEM

Valor Contabil do Item de mercadoria \(campo 64 da SAFX08\)\.

Se a nota não tiver item de mercadoria, considerar o Valor Total da Nota  da capa \(campo 23 da SAFX07\)\.

ALIQ\_TRIBUTO\_CMS

Alíquota do Tributo ICMS do item de mercadoria \(campo 42 da SAFX08\)\.

Se a nota não tiver item de mercadoria, considerar a Alíquota do ICMS da capa \(campo 34 da SAFX07\)\.

VLR\_TRIBUTO\_ICMS

Valor do Tributo ICMS do item de mercadoria \(campo 43 da SAFX08\)\.

Se a nota não tiver item de mercadoria, considerar o Valor do ICMS da capa \(campo 35 da SAFX07\)\.

VLR\_BASE\_ICMS\_TRIB

Base Tributada ICMS do item de mercadoria \(VLR\_BASE\_ICMS\_1 da DWT\_ITENS\_MERC\)

Se a nota não tiver item de mercadoria, considerar a Base Tributada ICMS da capa \(campo 51 da SAFX07\)\.

VLR\_BASE\_ICMS\_ISENT

Base Isenta \+ Reduzida ICMS do item de mercadoria \(VLR\_BASE\_ICMS\_2 \+  VLR\_BASE\_ICMS\_4 da DWT\_ITENS\_MERC\)\.

Se a nota não tiver item de mercadoria, considerar a Base Isenta \+ Reduzida ICMS da capa \(campo 52, 54 da SAFX07\)\.

VLR\_BASE\_ICMS\_OUTR

Verificar o parâmetro “ICMS Retido/Outras” da Tela de Geração dos Mapas Entrada/Saída\.

Se parâmetro “ICMS Retido/Outras” estiver marcado, então:

  Preencher este campo com Base Outras ICMS \+ Valor do ICMS\-ST\.

Senão

  Preencher este campo com Base Outras ICMS\.  

Se a nota não tiver item de mercadoria, considerar a Base Outras ICMS e Valor ICMS\-ST da capa \(campo 53, 48 da SAFX07\)\.

Se a nota tiver item de mercadoria, considerar os valores do item de mercadoria \(VLR\_BASE\_ICMS\_3 e VLR\_TRIBUTO\_ICMSS da DWT\_ITENS\_MERC\)\.

ALIQ\_TRIBUTO\_ICMSS

Alíquota do Tributo ICMS\-ST do item de mercadoria \(campo 51 da SAFX08\)\.

Para nota sem item de mercadoria, considerar a Alíquota ICMS\-ST da capa \(campo 47 da SAFX07\)\.

VLV\_TRIBUTO\_ICMSS

Valor do Tributo ICMS\-ST do item de mercadoria \(campo 52 da SAFX08\)\.

Para nota sem item de mercadoria, considerar o valor ICMS\-ST da capa \(campo 48 da SAFX07\)\.

VLR\_BASE\_ICMSS

Valor da Base ICMS\-ST do item de mercadoria \(campo 61 da SAFX08\)\.

Para nota sem item de mercadoria, considerar a base ICMS\-ST da capa \(campo 64 da SAFX07\)\.

VLR\_TAXA

Não Preencher

VLR\_CONTRIBUICAO

Não Preencher

USUARIO

Usuário de login da aplicação

NUM\_PROCESSO

Número do processo da Geração dos Mapas de Entrada e Saída

= = = = = 

