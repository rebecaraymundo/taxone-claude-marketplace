# MTZ_Geracao_Anexos I-M

- **Fonte:** MTZ_Geracao_Anexos I-M.docx
- **Modificado:** 2026-03-01
- **Tamanho:** 264 KB

---

Combustíveis e Derivados de Petróleo

Geração do Anexo I\-M para Distribuidoras

__Localização:__ Específicos à Combustíveis e Derivados de Petróleo,

Menu: Movimento Distribuidora à Geração à Anexos da Tributação Monofásica à Geração

Quadro de Revisões

__                         __

__Data__

__OS / Chamado__

__Descrição__

__Responsável__

28/04/2025

MFS772704

Geração do Anexo I\-M para produtos com tributação monofásica\.

Liliane Assaf

Sumário

[1\.	Introdução	1](#_Toc199928223)

[2\.	Pré\-Requisitos:	1](#_Toc199928224)

[3\.	Regras de Negócio Gerais	1](#_Toc199928225)

[RN00 – Consolidação dos Grupos Combustíveis para Geração do Anexo I\-M	1](#_Toc199928226)

[RN00\.a – Anexo I\-M Sem Movimento	1](#_Toc199928227)

[RN00\.b – Regra de Consistências	1](#_Toc199928228)

[RN00\.c – Regra para Conversão de Unidades de Medidas	1](#_Toc199928229)

[RN00\.d – Regra para Cálculo da Quantidade de Óleo Diesel A \(Base de Cálculo\)	1](#_Toc199928230)

[RN00\.e – Regra para Cálculo da Quantidade de B100 na Mistura a Ser Comercializada a Consumidor Final \(Base de Cálculo Retenção\)	1](#_Toc199928231)

[RN00\.f – Regra para Cálculo do Valor do ICMS sobre o Óleo Diesel A	1](#_Toc199928232)

[RN00\.g – Regra para Cálculo do Valor do ICMS sobre o B100	1](#_Toc199928233)

[4\.	Regras de Negócio Específicas dos Quadros	1](#_Toc199928234)

[RN01 \- Geração do Quadro 1 \- Apuração da Alíquota Ad Rem Média Ponderada	1](#_Toc199928235)

[Linha 1: Estoque Inicial:	1](#_Toc199928236)

[Linha 2: Recebimentos \(Entradas\):	1](#_Toc199928237)

[Linha 3: Correção Volumétrica	1](#_Toc199928238)

[Linha 4: Total Disponível no Período	1](#_Toc199928239)

[Linha 5: Alíquota AD REM Média Ponderada	1](#_Toc199928240)

[Linha 6: Recebimentos \(Devoluções\)	1](#_Toc199928241)

[Linha 7: Total das Entradas \(Disponível \+ Devoluções\)	1](#_Toc199928242)

[Linha 8: Remessas \(Saídas\)	1](#_Toc199928243)

[Linha 9: Remessas \(Devoluções\)	1](#_Toc199928244)

[Linha 10: Total das Saídas	1](#_Toc199928245)

[Linha 11: Perdas	1](#_Toc199928246)

[Linha 12: Ganhos	1](#_Toc199928247)

[Linha 13: Estoque Final	1](#_Toc199928248)

[RN02 \- Geração do Quadro 2 \- Apuração da Proporcionalidade por Fornecedor	1](#_Toc199928249)

[RN03 \- Geração do Quadro 3 \- Relação dos Recebimentos no Período \(Notas Fiscais de Entrada\)	1](#_Toc199928250)

[RN04 \- Geração do Quadro 4 \- Resumo das Remessas Realizadas no Período \(Saídas\)	1](#_Toc199928251)

[5\.	Regras para Emissão do Anexo I\-M	1](#_Toc199928252)

# <a id="_Toc199928223"></a>Introdução 

Esse documento tem como objetivo definir as regras de geração do Anexo I\-M em conformidade com a base legal:

Ato Cotepe ICMS nº 22/23 para Diesel

Ato Cotepe ICMS n° 44/23 para Gasolina

# <a id="_Toc197515405"></a><a id="_Toc199928224"></a>Pré\-Requisitos:

Considerar os pré\-requisitos descritos no “MTZ\_Geracao\_Anexos da Tributação Monofásica\.docx” e os listados a seguir:

1. Registro do __Estoque Inicial__ por Grupo Combustível

Localização: Módulo Específicos > Combustíveis e Derivados de Petróleo, menu Movimento de Distribuidora > Estoque Inicial por Grupos de Combustíveis e Derivados

Informar o estoque inicial de todos os grupos combustíveis relacionados ao combustível selecionado para geração do Anexo I\-M

Exemplo Cadastro para Grupo de combustível e Derivados

Grupo Combustível

Descrição

Produto SEF

I\-M

II\-M

III\-M

01

Diesel A

DSL

Sim

Sim

Sim

02

Diesel B

BXD

Sim

Sim

Sim

03

Gasolina A

GSL

Sim

Sim

Sim

04

Gasolina C

GSC

Sim

Sim

Sim

05

Diesel A S10

S10

Sim

Sim

Sim

06

Diesel B S10

BXS

Sim

Sim

Sim

07

Gasolina A Premium

GSP

Sim

Sim

Sim

08

Gasolina C Premiun

GCP

Sim

Sim

Sim

Se na tela de geração foi escolhido gerar o Anexo I\-M para o combustível DSL, deve\-se informar o estoque inicial para os grupos de combustíveis 01, 02, 05 e 06\.  

Isso porque o Anexo I\-M gerado em nome de UM combustível e agrupa informações de vários grupos combustíveis\. 

Veja a TACES114 \- Grupamento dos Combustíveis para Composição dos Anexos Monofásicos \(tabela CBT\_PROD\_SEF\_CENTR\), que contém a relação dos combustíveis \(COD\_PROD\_SEF\) que são consolidados e geram UM anexo em nome de um combustível \(COD\_PROD\_SEF\_CENTR\):

COD\_ANEXO

COD\_PROD\_SEF

COD\_PROD\_SEF\_CENTR

1M

DSL

DSL

1M

BXD

DSL

1M

S10

DSL

1M

BXS

DSL

Estoque Inicial \(tabela CBT\_GRP\_ESTOQ\):

Grupo Combustível

Data

Estabelecimento

01

31/01/2025

001

02

31/01/2025

001

05

31/01/2025

001

06

31/01/2025

001

1. Registro do Estoque Inicial por Grupo Combustível/Fornecedor

Localização: Módulo Específicos > Combustíveis e Derivados de Petróleo, menu Movimento de Distribuidora > Estoque Inicial por Grupos de Combustíveis e Derivados/Fornecedor

Registre o Estoque Inicial do período segregado por fornecedor, para cada grupo de combustível para geração do Quadro 2 do Anexo I\-M

1. Registro de Perdas e Ganhos\.

Localização: Módulo Específicos > Combustíveis e Derivados de Petróleo, menu Movimento de Distribuidora > Perdas e Ganhos por Grupos de Combustíveis e Derivados

Registre as quantidades de perdas e ganhos do período para cada grupo de combustível para geração do Quadro 1 do Anexo I\-M\.

# <a id="_Toc199928225"></a>Regras de Negócio Gerais

## <a id="_RN00_–_Regra"></a><a id="_Toc199928226"></a>RN00 – Consolidação dos Grupos Combustíveis para Geração do Anexo I\-M

Gerar um Anexo I\-M para cada opção de Combustível e estabelecimento selecionado na tela de geração, com as informações de estoque e movimentação de notas fiscais do período\.

Vejas as definições no Ato Cotepe 22/23 e 44/23:

Ato Cotepe/ICMS nº 22/2023 para Diesel:

*“1\.7\. Todos os produtos deverão ser informados de forma consolidada, por Grupo de Produto, quais sejam:*

*óleo diesel, óleo diesel marítimo \(DMA/MGO, DMB/MDO\), biodiesel B100, GLP/GLGN\. As quantidades de*

*produtos deverão ser informadas em LITROS para óleo diesel, óleo diesel marítimo e biodiesel B100, e em*

*quilogramas \(KG\) para o GLP/GLGN\.”*

Ato Cotepe ICMS n° 44/2023 para Gasolina:

*“1\.7\. Todos os produtos deverão ser informados de forma consolidada, por Grupo de*

*Produto, quais sejam: gasolina, gasolina de aviação, etanol anidro combustível \(EAC\)\. As quantidades de*

*produtos deverão ser informadas em LITROS\.”*

Para atender a essa definição, os movimentos de notas ficais, as informações de estoque inicial e perdas e ganhos são recuperados para os Grupos Combustíveis do Cadastro de “Grupo de Combustível e Derivados” e consolidados em nome do COD\_PROD\_SEF\_CENTR \(Taces 114\) para geração do Anexo I\-M\.

As seguintes opções estão disponíveis na tela de Geração:

\[ \] Diesel \- DSL, BXD, S10 e BXS

\[ \] Diesel Marítimo \- DSM 

\[ \] Gasolina \- GSL e GSC 

\[ \] Gasolina Premium \- GSP e GCP

\[ \] Gasolina de Aviação \- GSV

Cada uma das opções da tela está relacionada a um COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\)\. 

- Diesel \- DSL, BXD, S10 e BXS       🡪 COD\_PROD\_SEF\_CENTR = DSL
- Diesel Marítimo \- DSM                    🡪 COD\_PROD\_SEF\_CENTR = DSM
- Gasolina \- GSL e GSC                      🡪 COD\_PROD\_SEF\_CENTR = GSL
- Gasolina Premium \- GSP e GCP      🡪 COD\_PROD\_SEF\_CENTR= GSP
- Gasolina de Aviação \- GSV             🡪 COD\_PROD\_SEF\_CENTR = GSV

Na recuperação das informações de notas e estoque, serão considerados todos os Grupos Combustíveis do Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB\) cujo Produto SEF está relacionado ao COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\)\.

Taces114:

COD\_ANEXO

COD\_PROD\_SEF

COD\_PROD\_SEF\_CENTR

DSL\_PROD\_SEF\_CENTR

1M

DSL

DSL

Diesel

1M

BXD

DSL

Diesel

1M

DSM

DSM

Diesel Marítimo

1M

S10

DSL

Diesel

1M

BXS

DSL

Diesel

1M

GSL

GSL

Gasolina

1M

GSC

GSL

Gasolina

1M

GSP

GSP

Gasolina Premium

1M

GCP

GSP

Gasolina Premium

1M

GSV

GSV

Gasolina de Aviação

Selecionando a opção da tela “Diesel \- DSL, BXD, S10 e BXS” referente ao COD\_PROD\_SEF\_CENTR = DSL, os Grupos Combustíveis que serão considerados serão os cadastrados com Produto SEF “DSL”, “BXD”, “S10” e “BXS”\.

## <a id="_Toc199928227"></a>RN00\.a – Anexo I\-M Sem Movimento

Mesmo que não haja movimento para opção de Combustível e estabelecimento selecionados na tela de geração, para o período informado, deve ser gerado o Anexo I\-M indicando “__SEM MOVIMENTO__”\.

## <a id="_Toc199928228"></a>RN00\.b – Regra de Consistências

Realizar as seguintes validações e prosseguir com a geração do Anexo I\-M\.

1. Validar Estoque Inicial por Grupo de Combustível e por Grupo de Combustível/Fornecedores

Para a opção de Combustível selecionada na tela de geração \(ex: “Diesel \- DSL, BXD, S10 e BXS”, “Gasolina \- GSL e GSC”\), recuperar na __TACES114__ – “Grupamento dos Combustíveis para Composição dos Anexos Monofásicos”, os Códigos de Produto SEF relacionados, que são considerados na geração do Anexo I\-M\.

Para isso realizar consulta na tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) com os seguintes critérios:

- COD\_ANEXO = ‘1M’                   
- COD\_PROD\_SEF\_CENTR = ‘DSL’, p/ opção de Combustível selecionada na tela de geração for “Diesel \- DSL, BXD, S10 e BXS”

                                              = ‘DSM’, p/ opção de Combustível selecionada na tela de geração for “Diesel Marítimo \- DSM”

                                              = ‘GSL’, p/ opção de Combustível selecionada na tela de geração for “Gasolina \- GSL e GSC”

                                              = ‘GSP’, p/ opção de Combustível selecionada na tela de geração for “Gasolina Premium \- GSP e GCP”

                                              = ‘GSV’, p/ opção de Combustível selecionada na tela de geração for “Gasolina de Aviação \- GSV”

Recuperar Código de Produto SEF \(COD\_PROD\_SEF\)\. 

Obs: essa consulta pode recuperar mais de um registro\. Exemplo: se selecionado para geração o combustível “DSL”, o resultado da consulta são dois registros “DSL” e “BXD”\.

Para cada Código de Produto SEF recuperado na consulta acima, consultar o Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB\) para recuperar o Grupo Combustível\.

Para isso realizar a consulta na tabela CBT\_GRP\_COMB com os seguintes critérios:

- COD\_PROD\_SEF = COD\_PROD\_SEF recuperado

Recuperar o Identificador do Grupo Combustível \(IDENT\_GRP\_COMB\)\.

Com o Grupo Combustível recuperado acima, verificar se existe Estoque Inicial por Grupo de Combustível para o período da geração\.

Para isso consultar o “Movimento de Estoque Inicial por Grupo de Combustível” \(tabela CBT\_GRP\_ESTOQ\) com os seguintes critérios:

- Empresa de login
- Estabelecimento selecionado na tela de geração
- Mês/Ano Referencia: informado na tela de geração
- Grupo de combustível recuperado acima

Caso não exista registro, exibir a seguinte mensagem de aviso no log da geração:

Não foi encontrada informação de “Estoque Inicial por Grupo de Combustível” para o Grupo de Combustível *COD\_GRP\_COMB* referente ao *COD\_PROD\_SEF*\.  Acesse a opção Estoque Inicial por Grupo de Combustível e Derivados disponível no menu Movimento de Distribuidora, e informe para o estabelecimento e período da geração, o estoque inicial do combustível\.

Caso exista registro, verificar se existe Estoque Inicial por Grupo de Combustível/Fornecedores para o período da geração\.

Para isso consultar o “Movimento de Estoque Inicial por Grupo de Combustível/Fornecedores” \(tabela CBT\_GRP\_PFJ\_ESTOQ\) com os seguintes critérios:

- Empresa de login
- Estabelecimento selecionado na tela de geração
- Mês/Ano Referencia: informado na tela de geração
- Grupo de combustível recuperado acima

Caso não exista registro, exibir a seguinte mensagem de aviso no log da geração:

Não foi encontrada informação de “Estoque Inicial por Grupo de Combustível/Fornecedor” para o Grupo de Combustível *COD\_GRP\_COMB* referente ao *COD\_PROD\_SEF*\.  Acesse a opção Estoque Inicial por Grupo de Combustível e Derivados/Fornecedor disponível no menu Movimento de Distribuidora, e informe para o estabelecimento e período da geração, o estoque inicial do combustível segregado por fornecedor\.

## <a id="_RN00.c_–_Regra"></a><a id="_Toc199928229"></a>RN00\.c – Regra para Conversão de Unidades de Medidas

Regra aplicada aos quadros [1](#_RN01_-_Geração), [3](#_RN03_-_Geração) e [4](#_RN04_-_Geração)\.

Deve\-se aplicar o fator de conversão de unidades de medidas, quando a medida do item \(campo 25\-COD\_MEDIDA da SAFX08\) for diferente da medida parametrizada no menu: Parâmetros > Produtos x Grupos de Combustíveis e Derivados \(campo 09\-COD\_MEDIDA da SAFX96\)\.

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção >> Cadastros >> Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas será gravada a seguinte mensagem de aviso no log:

Fator de conversão de medida de XXX para XXX não encontrado\. 

Acesse o Módulo Data Warehouse, menu Manutenção >> Cadastros >> Conversão de Unidades de Medida e registre o fator de conversão para as medidas numa das opções: Padrão ou Por Produto\.

\(O primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

## <a id="_RN00.d_–_Regra"></a><a id="_Toc199928230"></a>RN00\.d – Regra para Cálculo da Quantidade de Óleo Diesel A \(Base de Cálculo\)

Regra aplicada ao campo Quantidade de Óleo Diesel A presente nos quadros [1](#_RN01_-_Geração), [3](#_RN03_-_Geração) e [4](#_RN04_-_Geração)\.

Considerar o Produto SEF do Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB campo COD\_PROD\_SEF\), para verificar se o Diesel é Puro ou é Mistura\.

__Para os produtos do grupo Diesel Puro \(DSL, DSM, S10\) ou Gasolina Pura \(GSL, GSP, GSV\):__

Preencher com o campo 24\-QUANTIDADE da SAFX08\.

Deve\-se aplicar o fator de conversão de unidades de medidas, quando a medida do item for diferente da medida parametrizada no menu: Parâmetros > Produtos x Grupos de Combustíveis e Derivados \(SAFX96\)\. Vide [RN00\.c](#_RN00.c_–_Regra)\.

__Para os produtos do grupo Diesel Mistura \(BXD, BXS\) ou Gasolina Mistura \(GSC, GCP\):__

Preencher com o cálculo:

\(campo 24\-QUANTIDADE da SAFX08\) __– __\(campo 24\-QUANTIDADE da SAFX08 __x__ campo 16\-PERC\_B100 da SAFX325/100\)

Deve\-se aplicar o fator de conversão de unidades de medidas, quando a medida do item for diferente da medida parametrizada no menu: Parâmetros > Produtos x Grupos de Combustíveis e Derivados \(SAFX96\)\. Vide [RN00\.c](#_RN00.c_–_Regra)\.

Obs regra baseada no registro 45 do SCANC Distribuidora

## <a id="_RN00.e_–_Regra"></a><a id="_Toc199928231"></a>RN00\.e – Regra para Cálculo da Quantidade de B100 na Mistura a Ser Comercializada a Consumidor Final \(Base de Cálculo Retenção\)

Regra aplicada ao campo Quantidade de B100 presente nos quadros [1](#_RN01_-_Geração), [3](#_RN03_-_Geração)\.

Considerar o Produto SEF do Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB campo COD\_PROD\_SEF\), para verificar se o Diesel é Puro ou é Mistura\.

__Para os produtos do grupo Diesel Puro \(DSL, DSM, S10\) ou Gasolina Pura \(GSL, GSP, GSV\):__

 Preencher com o cálculo:

 \(QtdA __x__ pBio\) / \(100 \- pBio\)

 Onde: 

 \- QtdA = campo 24\-QUANTIDADE da SAFX08

 \- pBio = campo 16\-PERC\_B100 da SAFX325

Deve\-se aplicar o fator de conversão de unidades de medidas, quando a medida do item for diferente da medida parametrizada no menu: Parâmetros > Produtos x Grupos de Combustíveis e Derivados \(SAFX96\)\. Vide [RN00\.c](#_RN00.c_–_Regra)\.

Se o campo pBio for preenchido com 100, no log deve ser exibida a seguinte mensagem, juntamente com as informações da nota fiscal e do produto:

“Não foi possível calcular a quantidade de B100 para a nota fiscal, pois o Percentual do Biodiesel na Composição informado, está incorreto, igual a 100%\. Reveja o preenchimento do percentual no campo 16\- PERC\_B100 da SAFX325\.”

__Para os produtos do grupo Diesel Mistura \(BXD, BXS\) ou Gasolina Mistura \(GSC, GCP\):__

 Preencher com o cálculo:

\(campo 24\-QUANTIDADE da SAFX08\) __x __\(campo 16\-PERC\_B100 da SAFX325/100\)

Deve\-se aplicar o fator de conversão de unidades de medidas, quando a medida do item for diferente da medida parametrizada no menu: Parâmetros > Produtos x Grupos de Combustíveis e Derivados \(SAFX96\)\. Vide [RN00\.c](#_RN00.c_–_Regra)\.

Obs regra baseada no registro 45 do SCANC Distribuidora

## <a id="_RN00.f_–_Regra"></a><a id="_Toc199928232"></a>RN00\.f – Regra para Cálculo do Valor do ICMS sobre o Óleo Diesel A

Regra aplicada ao campo Valor do ICMS sobre o Óleo Diesel A de B100 presente nos quadros [1](#_RN01_-_Geração), [3](#_RN03_-_Geração)\.

Considerar o Produto SEF do Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB campo COD\_PROD\_SEF\), para verificar se o Diesel é Puro ou é Mistura\.

__Para os produtos do grupo Diesel Puro \(DSL, DSM, S10\) ou Gasolina Pura \(GSL, GSP, GSV\):__

\- Se Código da Situação Estadual “B” \(campo 31 da SAFX08\) estiver preenchido com ‘02’ ou ‘15’:

     Preencher com o campo 23\-VLR\_ICMS\_MONO da SAFX325\.

\- Se Código da Situação Estadual “B” \(campo 31 da SAFX08\) estiver preenchido com ‘53’:

           Preencher com o campo 29\-VLR\_ICMS\_MONO\_OP da SAFX325\.

\- Se Código da Situação Estadual “B” \(campo 31 da SAFX08\) estiver preenchido com ‘61’:

     Preencher com o cálculo: 

\(Quantidade de Óleo Diesel A do quadro 3\) __x__ \(campo 33\-ALIQ\_AD\_REM\_ICMS\_RET da SAFX325\)

Deve\-se aplicar o fator de conversão de unidades de medidas, quando a medida do item for diferente da medida parametrizada no menu: Parâmetros > Produtos x Grupos de Combustíveis e Derivados \(SAFX96\)\. Vide [RN00\.c](#_RN00.c_–_Regra)\.

__Para os produtos do grupo Diesel Mistura \(BXD, BXS\) ou Gasolina Mistura \(GSC, GCP\):__

\- Se Código da Situação Estadual “B” \(campo 31 da SAFX08\) estiver preenchido com ‘02’ ou ‘15’:

   Preencher com o cálculo: 

\(campo 23\-VLR\_ICMS\_MONO da SAFX325\) __– __\(campo 23\- VLR\_ICMS\_MONO da SAFX325 __x__ campo 16\-PERC\_B100 da SAFX325 __/__100\)

\- Se Código da Situação Estadual “B” \(campo 31 da SAFX08\) estiver preenchido com ‘53’:

   Preencher com o cálculo:

\(campo 29\-VLR\_ICMS\_MONO\_OP da SAFX325\) __– __\(campo 29\-VLR\_ICMS\_MONO\_OP da SAFX325 __x__ campo 16\-PERC\_B100 da SAFX325 __/__100\)

\- Se Código da Situação Estadual “B” \(campo 31 da SAFX08\) estiver preenchido com ‘61’:

   Preencher com o cálculo:

 \(campo 34\-VLR\_ICMS\_MONO\_RET da SAFX325\) __–__ \(campo 34\-VLR\_ICMS\_MONO\_RET da SAFX325 __x__ campo 16\-PERC\_B100 da SAFX325 __/__100\)

Obs regra baseada no registro 45 do SCANC Distribuidora

## <a id="_RN00.g_–_Regra"></a><a id="_Toc199928233"></a>RN00\.g – Regra para Cálculo do Valor do ICMS sobre o B100

Regra aplicada ao campo Valor do ICMS sobre B100 presente nos quadros [1](#_RN01_-_Geração), [3](#_RN03_-_Geração) considerando as informações da nota fiscal

Considerar o Produto SEF do Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB campo COD\_PROD\_SEF\), para verificar se o Diesel é Puro ou é Mistura\.

__Para os produtos do grupo Diesel Puro \(DSL, DSM, S10\) ou Gasolina Pura \(GSL, GSP, GSV\):__

\- Se Código da Situação Estadual “B” \(campo 31 da SAFX08\) estiver preenchido com ‘15’:

      Preencher com o campo 26\-VLR\_ICMS\_MONO\_RETEN da SAFX325\.

\- Se Código da Situação Estadual “B” \(campo 31 da SAFX08\) estiver preenchido com ‘02’ ou ‘53’:

     Se for Gasolina Pura \(GLS, GSP, GSV\):

                Preencher com o cálculo:

                        \(Quantidade de B100 do quadro 3\) __x__ \(campo 22\-ALIQ\_AD\_REM\_ICMS da SAFX325\)

     Se for Diesel Puro \(DSL, DSM, S10\):

                Preencher com o cálculo:

                        \(Quantidade de B100 do quadro 3\) __x __\(campo 22\- ALIQ\_AD\_REM\_ICMS da SAFX325\) __x 0,3333__

\- Se Código da Situação Estadual “B” \(campo 31 da SAFX08\) estiver preenchido com ‘61’:

     Se for Gasolina Pura \(GLS, GSP, GSV\):

                 Preencher com o cálculo:

                         \(Quantidade de B100 do quadro 3\) __x__ \(campo 33\-ALIQ\_AD\_REM\_ICMS\_RET da SAFX325\)

     Se for Diesel Puro \(DSL, DSM, S10\):

                 Preencher com o cálculo:

                        \(Quantidade de B100 do quadro 3\) __x__ \(campo 33\-ALIQ\_AD\_REM\_ICMS\_RET da SAFX325\) __x 0,3333__

Obs: 0,3333 referente a 33,33% que é o percentual de redução do valor da alíquota ad rem do ICMS\.

__Para os produtos do grupo Diesel Mistura \(BXD, BXS\) ou Gasolina Mistura \(GSC, GCP\):__

\- Se Código da Situação Estadual “B” \(campo 31 da SAFX08\) estiver preenchido com ‘02’ ou ‘15’:

     Preencher com o cálculo:

                    \(campo 23\-VLR\_ICMS\_MONO da SAFX325\) __x__ \(campo 16\-PERC\_B100 da SAFX325 __/__100\)

 

\- Se Código da Situação Estadual “B” \(campo 31 da SAFX08\) estiver preenchido com ‘53’:

      Preencher com o cálculo:

                   \(campo 29\-VLR\_ICMS\_MONO\_OP da SAFX325\) __x__ \(campo 16\-PERC\_B100 da SAFX325 __/__100\)

\- Se Código da Situação Estadual “B” \(campo 31 da SAFX08\) estiver preenchido com ‘61’:

       Preencher com o cálculo:

                     \(campo 34\-VLR\_ICMS\_MONO\_RET da SAFX325\) __x__ \(campo 16\-PERC\_B100 da SAFX325 __/__100\)

Obs regra baseada no registro 45 do SCANC Distribuidora

# <a id="_Toc199928234"></a>Regras de Negócio Específicas dos Quadros

## <a id="_RN01_-_Geração"></a><a id="_Toc199928235"></a>RN01 \- Geração do Quadro 1 \- Apuração da Alíquota Ad Rem Média Ponderada

Quadro formado pelas seguintes informações:

### <a id="_Toc199928236"></a>Linha 1: Estoque Inicial:

Linha gerada a partir do Estoque inicial informado no menu Movimento de Distribuidora 🡪 Estoque Inicial por Grupo de Combustíveis e Derivados\.

__Critério de Recuperação__:

Consultar o “Movimento de Estoque Inicial por Grupo de Combustível” \(tabela CBT\_GRP\_ESTOQ\) com os seguintes critérios:

- Empresa de login
- Estabelecimento informado na tela de geração
- Mês/Ano Referencia: informado na tela de geração
- Grupo Combustível: considerar todos os grupos combustíveis do Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB\) recuperados a partir dos critérios:
	- Produto SEF do Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB campo COD\_PROD\_SEF\) = COD\_PROD\_SEF da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\)
	- COD\_ANEXO da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) = ‘1M’ 
	- COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) = 

= ‘DSL’, p/ opção de Combustível selecionada na tela de geração for “Diesel \- DSL, BXD, S10 e BXS”

                                              = ‘DSM’, p/ opção de Combustível selecionada na tela de geração for “Diesel Marítimo \- DSM”

                                              = ‘GSL’, p/ opção de Combustível selecionada na tela de geração for “Gasolina \- GSL e GSC”

                                              = ‘GSP’, p/ opção de Combustível selecionada na tela de geração for “Gasolina Premium \- GSP e GCP”

                                              = ‘GSV’, p/ opção de Combustível selecionada na tela de geração for “Gasolina de Aviação \- GSV”

O Estoque Inicial lido para cada Grupo de Combustível deve ser totalizado e gravado em nome do COD\_PROD\_SEF\_CENTR, relacionado ao Combustível selecionado na tela de Geração\. Vide [RN00](#_RN00_–_Regra)\.

Exemplo: Estoque Inicial de dois Grupos Combustíveis \(Produto SEF “DSL” e “BXD”\) são consolidados e gravados na linha 1 para o Combustível “DSL” \(COD\_PROD\_SEF\_CENTR da TACES114\)\.

__Regra de Preenchimento dos Campos:__

- Empresa; preencher com a empresa de login
- Estabelecimento informado na tela de geração
- Mês/Ano Referencia: informado na tela de geração
- Combustível:  COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) referente ao Combustível selecionado na tela de Geração\.
- Quantidade de Combustível: não preencher
- Quantidade de Óleo Diesel A \(Base de Cálculo\): preencher com campo Qtde Gasolina A/Diesel A do Estoque Inicial
- Quantidade de B100 na Mistura a Ser Comercializada a Consumidor Final \(Base de Cálculo Retenção\): preencher com campo Qtde EAC/B100 do Estoque Inicial
- Alíquota Ad Rem Média Ponderada: não preencher
- Valor do ICMS sobre o Óleo Diesel A: preencher com campo Vlr ICMS Gasolina A/Diesel A do Estoque Inicial
- Valor do ICMS sobre o B100: preencher com campo Vlr ICMS EAC/B100 do Estoque Inicial

Obs: as quantidades do estoque inicial já estão na unidade de medida que deve ser apresentado o anexo, por isso a conversão de unidade de medida não é aplicada\.

### <a id="_Toc199928237"></a>Linha 2: Recebimentos \(Entradas\):

Linha gerada a partir da totalização do [__Quadro 3__](#_RN03_-_Geração) do Anexo I\-M\.

__Regra de Preenchimento dos Campos:__

- Empresa; preencher com a empresa de login
- Estabelecimento informado na tela de geração
- Mês/Ano Referencia: informado na tela de geração
- Combustível:  COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) referente ao Combustível selecionado na tela de Geração\.
- Quantidade de Combustível: preencher com o total do campo “Quantidade de Combustível” do Quadro 3 do período\.
- Quantidade de Óleo Diesel A \(Base de Cálculo\): preencher com o total do campo “Quantidade de Óleo Diesel A \(Base de Cálculo\)” do Quadro 3 do período\.
- Quantidade de B100 na Mistura a Ser Comercializada a Consumidor Final \(Base de Cálculo Retenção\): preencher com o total do campo “Quantidade de B100 na Mistura a Ser Comercializada a Consumidor Final \(Base de Cálculo Retenção\)”do Quadro 3 do período\.
- Alíquota Ad Rem Média Ponderada: não preencher\.
- Valor do ICMS sobre o Óleo Diesel A: preencher com o total do campo “Valor do ICMS sobre o Óleo Diesel A” do Quadro 3 do período\.
- Valor do ICMS sobre o B100: preencher com o total do campo “Valor do ICMS sobre o B100” do Quadro 3 do período

### <a id="_Toc199928238"></a>Linha 3: Correção Volumétrica

Critério de Recuperação: \*\* PENDENTE DE DEFINIÇÃO \*\*

__Regra de Preenchimento dos Campos:__

- Empresa; preencher com a empresa de login
- Estabelecimento informado na tela de geração
- Mês/Ano Referencia: informado na tela de geração
- Combustível:  COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) referente ao Combustível selecionado na tela de Geração\.
- Quantidade de Combustível
- Quantidade de Óleo Diesel A \(Base de Cálculo\)
- Quantidade de B100 na Mistura a Ser Comercializada a Consumidor Final \(Base de Cálculo Retenção\)
- Alíquota Ad Rem Média Ponderada
- Valor do ICMS sobre o Óleo Diesel A
- Valor do ICMS sobre o B100

### <a id="_Toc199928239"></a>Linha 4: Total Disponível no Período

Linha gerada a partir da totalização das linhas 1, 2 e 3 do __Quadro 1__ do Anexo I\-M\.

__Regra de Preenchimento dos Campos:__

- Empresa; preencher com a empresa de login
- Estabelecimento informado na tela de geração
- Mês/Ano Referencia: informado na tela de geração
- Combustível:  COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) referente ao Combustível selecionado na tela de Geração\.
- Quantidade de Combustível: somatório do campo “Quantidade de Combustível” das linhas 1, 2 e 3\.
- Quantidade de Óleo Diesel A \(Base de Cálculo\): somatório do campo “Quantidade de Óleo Diesel A \(Base de Cálculo\)” das linhas 1, 2 e 3\.
- Quantidade de B100 na Mistura a Ser Comercializada a Consumidor Final \(Base de Cálculo Retenção\): somatório do campo “Quantidade de B100 na Mistura a Ser Comercializada a Consumidor Final \(Base de Cálculo Retenção\)” das linhas 1, 2 e 3\.
- Alíquota Ad Rem Média Ponderada: não preencher\.
- Valor do ICMS sobre o Óleo Diesel A: somatório do campo “Valor do ICMS sobre o Óleo Diesel A” das linhas 1, 2 e 3\.
- Valor do ICMS sobre o B100: somatório do campo “Valor do ICMS sobre o B100” das linhas 1, 2 e 3\.

### <a id="_Toc199928240"></a>Linha 5: Alíquota AD REM Média Ponderada

Linha gerada a partir da linha 4 do quadro 1\.

Recuperar os campos “Valor do ICMS sobre o Óleo Diesel A” e “Quantidade de Óleo Diesel A \(Base de Cálculo\)” da linha 4 do Quadro 1 do Anexo I\-M\.

__Regra de Preenchimento dos Campos:__

- Empresa; preencher com a empresa de login
- Estabelecimento informado na tela de geração
- Mês/Ano Referencia: informado na tela de geração
- Combustível:  COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) referente ao Combustível selecionado na tela de Geração\.
- Quantidade de Combustível: não preencher
- Quantidade de Óleo Diesel A \(Base de Cálculo\): não preencher
- Quantidade de B100 na Mistura a Ser Comercializada a Consumidor Final \(Base de Cálculo Retenção\): não preencher
- Alíquota Ad Rem Média Ponderada: preencher com o resultado da divisão do “Valor do ICMS sobre o Óleo Diesel A” pela “Quantidade de Óleo Diesel A \(Base de Cálculo\)”
- Valor do ICMS sobre o Óleo Diesel A: não preencher
- Valor do ICMS sobre o B100: não preencher

### <a id="_Toc199928241"></a>Linha 6: Recebimentos \(Devoluções\)

Linha gerada a partir das Notas de Entrada por Devolução de Produtos sujeitos à tributação monofásica\.

__Critério de Recuperação__:

Para geração desse quadro recuperar os documentos fiscais a partir das tabelas SAFX07, SAFX08, SAFX325, considerando os seguintes critérios:

- Código da empresa = código da empresa da geração; 
- Estabelecimento informado na tela de geração
- Data Fiscal compreendida no mês/ano Referência informado na geração;
- __Notas fiscais de Entrada \(MOVTO\_E\_S <> ‘9’\)__
- __Notas fiscais de Devolução \(NORM\_DEV = ‘2’\)__
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Somente notas com item de mercadoria \(SAFX08\);
-  Somente itens com CFOP ou CFOP/NAT parametrizados no menu: Parâmetros > Anexos I, II, III, IV, V, VI e VIII para o tipo:

__   90 – Devolução de Venda de Combustíveis e Derivados__

__   93 – Devolução de Venda a Consumidor Final__

__   687 – Remessa em Bonificação, Doação ou Brinde__

__   688 \- Empréstimos__

- Somente notas com Informações de Tributação do ICMS Monofásico \(SAFX325\);
- Código da Sit\. Estadual “B” \(campo 1 da SAFX08\) = ‘02’, ‘15’, ‘53’ ou ‘61’;
- Considerar a Parametrização da Regras p/ Geração dos Anexos feita para o estabelecimento no item de menu: Parâmetros > Regras p/ Geração dos Anexos\. 
- Se o Campo “Considerar somente as Notas Fiscais com movimentação física de mercadoria” estiver marcado, recuperar apenas itens com Ind\. Movim\. Física da Merc\. \(campo 115\-IND\_MOV\_FIS da SAFX08\) = ‘S’;
- Se desmarcado, recuperar independente do Ind\. Movim\. Física da Merc\. \(campo 115\-IND\_MOV\_FIS da SAFX08\) ser S ou N\.
- Produto do item da nota deve ser parametrizado no item de menu: Parâmetros > Produtos x Grupos de Combustíveis e Derivados, com o seu respectivo grupo de combustíveis \(SAFX96\)
- Quanto ao Grupo de Combustível parametrizado para o Produto: considerar todos os grupos combustíveis do Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB\) recuperados a partir dos critérios:
	- Produto SEF do Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB campo COD\_PROD\_SEF\) = COD\_PROD\_SEF da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\)
	- COD\_ANEXO da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) = ‘1M’ 
	- COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) = 

= ‘DSL’, p/ opção de Combustível selecionada na tela de geração for “Diesel \- DSL, BXD, S10 e BXS”

                                              = ‘DSM’, p/ opção de Combustível selecionada na tela de geração for “Diesel Marítimo \- DSM”

                                              = ‘GSL’, p/ opção de Combustível selecionada na tela de geração for “Gasolina \- GSL e GSC”

                                              = ‘GSP’, p/ opção de Combustível selecionada na tela de geração for “Gasolina Premium \- GSP e GCP”

                                              = ‘GSV’, p/ opção de Combustível selecionada na tela de geração for “Gasolina de Aviação \- GSV”

   Localização: Parâmetros >> Grupos de Combustíveis e Derivados

As notas fiscais recuperadas de cada Grupo de Combustível devem ser totalizadas e gravadas em nome do COD\_PROD\_SEF\_CENTR, relacionado ao Combustível selecionado na tela de Geração\. Vide [RN00](#_RN00_–_Regra)\.

Exemplo: Notas de dois Grupos Combustíveis \(Produto SEF “DSL” e “BXD”\) são consolidadas e gravadas na linha 6 para o Combustível “DSL” \(COD\_PROD\_SEF\_CENTR da TACES114\)\.

__Regra de Preenchimento dos Campos:__

- Empresa; preencher com a empresa de login
- Estabelecimento informado na tela de geração
- Mês/Ano Referencia: informado na tela de geração
- Combustível:  COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) referente ao Combustível selecionado na tela de Geração\.
- Quantidade de Combustível: Preencher com o campo 24\-QUANTIDADE da SAFX08\.
- Deve\-se aplicar o fator de conversão de unidades de medidas, quando a medida do item for diferente da medida parametrizada no menu: Parâmetros > Produtos x Grupos de Combustíveis e Derivados \(SAFX96\)\. Vide [RN00\.c](#_RN00.c_–_Regra)\.
- Quantidade de Óleo Diesel A \(Base de Cálculo\): Aplicar a regra [RN00\.d](#_RN00.d_–_Regra)
- Quantidade de B100 na Mistura a Ser Comercializada a Consumidor Final \(Base de Cálculo Retenção\): Aplicar a regra [RN00\.e](#_RN00.e_–_Regra)\.
- Alíquota Ad Rem Média Ponderada: Não preencher
- Valor do ICMS sobre o Óleo Diesel A: Aplicar a regra [RN00\.f](#_RN00.f_–_Regra)
- Valor do ICMS sobre o B100: Aplicar a regra [RN00\.g](#_RN00.g_–_Regra)

### <a id="_Toc199928242"></a>Linha 7: Total das Entradas \(Disponível \+ Devoluções\)

Linha gerada a partir da totalização das linhas 4 e 6 do __Quadro 1__ do Anexo I\-M\.

__Regra de Preenchimento dos Campos:__

- Empresa; preencher com a empresa de login
- Estabelecimento informado na tela de geração
- Mês/Ano Referencia: informado na tela de geração
- Combustível:  COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) referente ao Combustível selecionado na tela de Geração\.
- Quantidade de Combustível: somatório do campo “Quantidade de Combustível” das linhas 4 e 6\.
- Quantidade de Óleo Diesel A \(Base de Cálculo\): somatório do campo “Quantidade de Óleo Diesel A \(Base de Cálculo\)” das linhas 4 e 6\.
- Quantidade de B100 na Mistura a Ser Comercializada a Consumidor Final \(Base de Cálculo Retenção\): somatório do campo “Quantidade de B100 na Mistura a Ser Comercializada a Consumidor Final \(Base de Cálculo Retenção\)” das linhas 4 e 6\.
- Alíquota Ad Rem Média Ponderada: não preencher\.
- Valor do ICMS sobre o Óleo Diesel A: somatório do campo “Valor do ICMS sobre o Óleo Diesel A” das linhas 4 e 6\.
- Valor do ICMS sobre o B100: somatório do campo “Valor do ICMS sobre o B100” das linhas 4 e 6\.

### <a id="_Toc199928243"></a>Linha 8: Remessas \(Saídas\)

Linha gerada a partir das Notas de Saída Normal de Produtos sujeitos à tributação monofásica\.

__Critério de Recuperação__:

Para geração desse quadro recuperar os documentos fiscais a partir das tabelas SAFX07, SAFX08, SAFX325, considerando os seguintes critérios:

- Código da empresa = código da empresa da geração; 
- Estabelecimento informado na tela de geração
- Data Fiscal compreendida no mês/ano Referência informado na geração;
- __Notas fiscais de Entrada \(MOVTO\_E\_S = ‘9’\)__
- __Notas fiscais de Devolução \(NORM\_DEV = ‘1’\)__
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Somente notas com item de mercadoria \(SAFX08\);
-  Somente itens com CFOP ou CFOP/NAT parametrizados no menu: Parâmetros > Anexos I, II, III, IV, V, VI e VIII para o tipo:

   __88 – Saída de Combustíveis e Derivados__

__   92 – Saída a Consumidor Final__

__   687 – Remessa em Bonificação, Doação ou Brinde__

__   688 \- Empréstimos__

- Somente notas com Informações de Tributação do ICMS Monofásico \(SAFX325\);
- Código da Sit\. Estadual “B” \(campo 1 da SAFX08\) = ‘02’, ‘15’, ‘53’ ou ‘61’;
- Considerar a Parametrização da Regras p/ Geração dos Anexos feita para o estabelecimento no item de menu: Parâmetros > Regras p/ Geração dos Anexos\. 
- Se o Campo “Considerar somente as Notas Fiscais com movimentação física de mercadoria” estiver marcado, recuperar apenas itens com Ind\. Movim\. Física da Merc\. \(campo 115\-IND\_MOV\_FIS da SAFX08\) = ‘S’;
- Se desmarcado, recuperar independente do Ind\. Movim\. Física da Merc\. \(campo 115\-IND\_MOV\_FIS da SAFX08\) ser S ou N\.
- Produto do item da nota deve ser parametrizado no item de menu: Parâmetros > Produtos x Grupos de Combustíveis e Derivados, com o seu respectivo grupo de combustíveis \(SAFX96\)
- Quanto ao Grupo de Combustível parametrizado para o Produto: considerar todos os grupos combustíveis do Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB\) recuperados a partir dos critérios:
	- Produto SEF do Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB campo COD\_PROD\_SEF\) = COD\_PROD\_SEF da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\)
	- COD\_ANEXO da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) = ‘1M’ 
	- COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) = 

= ‘DSL’, p/ opção de Combustível selecionada na tela de geração for “Diesel \- DSL, BXD, S10 e BXS”

                                              = ‘DSM’, p/ opção de Combustível selecionada na tela de geração for “Diesel Marítimo \- DSM”

                                              = ‘GSL’, p/ opção de Combustível selecionada na tela de geração for “Gasolina \- GSL e GSC”

                                              = ‘GSP’, p/ opção de Combustível selecionada na tela de geração for “Gasolina Premium \- GSP e GCP”

                                              = ‘GSV’, p/ opção de Combustível selecionada na tela de geração for “Gasolina de Aviação \- GSV”

   Localização: Parâmetros >> Grupos de Combustíveis e Derivados

As notas fiscais recuperadas de cada Grupo de Combustível devem ser totalizadas e gravadas em nome do COD\_PROD\_SEF\_CENTR, relacionado ao Combustível selecionado na tela de Geração\. Vide [RN00](#_RN00_–_Regra)\.

Exemplo: Notas de dois Grupos Combustíveis \(Produto SEF “DSL” e “BXD”\) são consolidadas e gravadas na linha 6 para o Combustível “DSL” \(COD\_PROD\_SEF\_CENTR da TACES114\)\.

__Regra de Preenchimento dos Campos:__

- Empresa; preencher com a empresa de login
- Estabelecimento informado na tela de geração
- Mês/Ano Referencia: informado na tela de geração
- Combustível:  COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) referente ao Combustível selecionado na tela de Geração\.
- Quantidade de Combustível: Preencher com o campo 24\-QUANTIDADE da SAFX08\.
- Deve\-se aplicar o fator de conversão de unidades de medidas, quando a medida do item for diferente da medida parametrizada no menu: Parâmetros > Produtos x Grupos de Combustíveis e Derivados \(SAFX96\)\. Vide [RN00\.c](#_RN00.c_–_Regra)\.
- Quantidade de Óleo Diesel A \(Base de Cálculo\): Aplicar a regra [RN00\.d](#_RN00.d_–_Regra)
- Quantidade de B100 na Mistura a Ser Comercializada a Consumidor Final \(Base de Cálculo Retenção\): Aplicar a regra [RN00\.e](#_RN00.e_–_Regra)\.
- Alíquota Ad Rem Média Ponderada: Não preencher
- Valor do ICMS sobre o Óleo Diesel A: Aplicar a regra [RN00\.f](#_RN00.f_–_Regra)
- Valor do ICMS sobre o B100: Aplicar a regra [RN00\.g](#_RN00.g_–_Regra)

### <a id="_Toc199928244"></a>Linha 9: Remessas \(Devoluções\)

Linha gerada a partir das Notas de Saída por Devolução de Produtos sujeitos à tributação monofásica\.

__Critério de Recuperação__:

Para geração desse quadro recuperar os documentos fiscais a partir das tabelas SAFX07, SAFX08, SAFX325, considerando os seguintes critérios:

- Código da empresa = código da empresa da geração; 
- Estabelecimento informado na tela de geração
- Data Fiscal compreendida no mês/ano Referência informado na geração;
- __Notas fiscais de Entrada \(MOVTO\_E\_S = ‘9’\)__
- __Notas fiscais de Devolução \(NORM\_DEV = ‘2’\)__
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Somente notas com item de mercadoria \(SAFX08\);
-  Somente itens com CFOP ou CFOP/NAT parametrizados no menu: Parâmetros > Anexos I, II, III, IV, V, VI e VIII para o tipo:

__   91 – Devolução de Compras de Combustíveis e Derivados__

__   687 – Remessa em Bonificação, Doação ou Brinde__

__   688 \- Empréstimos__

- Somente notas com Informações de Tributação do ICMS Monofásico \(SAFX325\);
- Código da Sit\. Estadual “B” \(campo 1 da SAFX08\) = ‘02’, ‘15’, ‘53’ ou ‘61’;
- Considerar a Parametrização da Regras p/ Geração dos Anexos feita para o estabelecimento no item de menu: Parâmetros > Regras p/ Geração dos Anexos\. 
- Se o Campo “Considerar somente as Notas Fiscais com movimentação física de mercadoria” estiver marcado, recuperar apenas itens com Ind\. Movim\. Física da Merc\. \(campo 115\-IND\_MOV\_FIS da SAFX08\) = ‘S’;
- Se desmarcado, recuperar independente do Ind\. Movim\. Física da Merc\. \(campo 115\-IND\_MOV\_FIS da SAFX08\) ser S ou N\.
- Produto do item da nota deve ser parametrizado no item de menu: Parâmetros > Produtos x Grupos de Combustíveis e Derivados, com o seu respectivo grupo de combustíveis \(SAFX96\)
- Quanto ao Grupo de Combustível parametrizado para o Produto: considerar todos os grupos combustíveis do Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB\) recuperados a partir dos critérios:
	- Produto SEF do Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB campo COD\_PROD\_SEF\) = COD\_PROD\_SEF da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\)
	- COD\_ANEXO da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) = ‘1M’ 
	- COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) = 

= ‘DSL’, p/ opção de Combustível selecionada na tela de geração for “Diesel \- DSL, BXD, S10 e BXS”

                                              = ‘DSM’, p/ opção de Combustível selecionada na tela de geração for “Diesel Marítimo \- DSM”

                                              = ‘GSL’, p/ opção de Combustível selecionada na tela de geração for “Gasolina \- GSL e GSC”

                                              = ‘GSP’, p/ opção de Combustível selecionada na tela de geração for “Gasolina Premium \- GSP e GCP”

                                              = ‘GSV’, p/ opção de Combustível selecionada na tela de geração for “Gasolina de Aviação \- GSV”

   Localização: Parâmetros >> Grupos de Combustíveis e Derivados

As notas fiscais recuperadas de cada Grupo de Combustível devem ser totalizadas e gravadas em nome do COD\_PROD\_SEF\_CENTR, relacionado ao Combustível selecionado na tela de Geração\. Vide [RN00](#_RN00_–_Regra)\.

Exemplo: Notas de dois Grupos Combustíveis \(Produto SEF “DSL” e “BXD”\) são consolidadas e gravadas na linha 6 para o Combustível “DSL” \(COD\_PROD\_SEF\_CENTR da TACES114\)\.

__Regra de Preenchimento dos Campos:__

- Empresa; preencher com a empresa de login
- Estabelecimento informado na tela de geração
- Mês/Ano Referencia: informado na tela de geração
- Combustível:  COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) referente ao Combustível selecionado na tela de Geração\.
- Quantidade de Combustível: Preencher com o campo 24\-QUANTIDADE da SAFX08\.

Deve\-se aplicar o fator de conversão de unidades de medidas, quando a medida do item for diferente da medida parametrizada no menu: Parâmetros > Produtos x Grupos de Combustíveis e Derivados \(SAFX96\)\. Vide [RN00\.c](#_RN00.c_–_Regra)\.

- Quantidade de Óleo Diesel A \(Base de Cálculo\): Aplicar a regra [RN00\.d](#_RN00.d_–_Regra)
- Quantidade de B100 na Mistura a Ser Comercializada a Consumidor Final \(Base de Cálculo Retenção\): Aplicar a regra [RN00\.e](#_RN00.e_–_Regra)\.
- Alíquota Ad Rem Média Ponderada: Não preencher
- Valor do ICMS sobre o Óleo Diesel A: Aplicar a regra [RN00\.f](#_RN00.f_–_Regra)
- Valor do ICMS sobre o B100: Aplicar a regra [RN00\.g](#_RN00.g_–_Regra)

### <a id="_Toc199928245"></a>Linha 10: Total das Saídas

Linha gerada a partir da totalização das linhas 8 e 9 do __Quadro 1__ do Anexo I\-M\.

__Regra de Preenchimento dos Campos:__

- Empresa; preencher com a empresa de login
- Estabelecimento informado na tela de geração
- Mês/Ano Referencia: informado na tela de geração
- Combustível:  COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) referente ao Combustível selecionado na tela de Geração\.
- Quantidade de Combustível: somatório do campo “Quantidade de Combustível” das linhas 8 e 9\.
- Quantidade de Óleo Diesel A \(Base de Cálculo\): somatório do campo “Quantidade de Óleo Diesel A \(Base de Cálculo\)” das linhas 8 e 9\.
- Quantidade de B100 na Mistura a Ser Comercializada a Consumidor Final \(Base de Cálculo Retenção\): somatório do campo “Quantidade de B100 na Mistura a Ser Comercializada a Consumidor Final \(Base de Cálculo Retenção\)” das linhas 8 e 9\.
- Alíquota Ad Rem Média Ponderada: não preencher\.
- Valor do ICMS sobre o Óleo Diesel A: somatório do campo “Valor do ICMS sobre o Óleo Diesel A” das linhas 8 e 9\.
- Valor do ICMS sobre o B100: somatório do campo “Valor do ICMS sobre o B100” das linhas 8 e 9\.

### <a id="_Toc199928246"></a>Linha 11: Perdas

Linha gerada a partir das Perdas do combustível informadas manualmente na opção do menu Movimento de Distribuidora 🡪 Perdas e Ganhos por Grupo de Combustíveis e Derivados\.  Também é possível importar essas informações através da SAFX06\.

__Critério de Recuperação__:

Consultar o “Movimento de Perdas e Ganhos por Grupo de Combustível” \(tabela X06\_PERDA\_GANHO\) com os seguintes critérios:

- Empresa de login
- Estabelecimento informado na tela de geração
- Mês/Ano Referencia: informado na tela de geração
- Tipo = __Perda__
- Grupo Combustível: considerar todos os grupos combustíveis do Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB\) recuperados a partir dos critérios:
	- Produto SEF do Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB campo COD\_PROD\_SEF\) = COD\_PROD\_SEF da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\)
	- COD\_ANEXO da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) = ‘1M’ 
	- COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) = 

= ‘DSL’, p/ opção de Combustível selecionada na tela de geração for “Diesel \- DSL, BXD, S10 e BXS”

                                              = ‘DSM’, p/ opção de Combustível selecionada na tela de geração for “Diesel Marítimo \- DSM”

                                              = ‘GSL’, p/ opção de Combustível selecionada na tela de geração for “Gasolina \- GSL e GSC”

                                              = ‘GSP’, p/ opção de Combustível selecionada na tela de geração for “Gasolina Premium \- GSP e GCP”

                                              = ‘GSV’, p/ opção de Combustível selecionada na tela de geração for “Gasolina de Aviação \- GSV”

As quantidades de perda recuperadas para cada Grupo de Combustível devem ser totalizadas e gravadas em nome do COD\_PROD\_SEF\_CENTR, relacionado ao Combustível selecionado na tela de Geração\. Vide [RN00](#_RN00_–_Regra)\.

Exemplo: Registro de Perda de dois Grupos Combustíveis \(Produto SEF “DSL” e “BXD”\) são consolidados e gravados na linha 11 para o Combustível “DSL” \(COD\_PROD\_SEF\_CENTR da TACES114\)\.

__Regra de Preenchimento dos Campos:__

- Empresa; preencher com a empresa de login
- Estabelecimento informado na tela de geração
- Mês/Ano Referencia: informado na tela de geração
- Combustível:  COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) referente ao Combustível selecionado na tela de Geração\.
- Quantidade de Combustível: preencher com campo Qtde de Combustível das Perdas \(tabela X06\_PERDA\_GANHO\)\.
- Quantidade de Óleo Diesel A \(Base de Cálculo\): preencher com campo Qtde Gasolina A/Diesel A das Perdas \(tabela X06\_PERDA\_GANHO\)\.
- Quantidade de B100 na Mistura a Ser Comercializada a Consumidor Final \(Base de Cálculo Retenção\): preencher com campo Qtde EAC/B100 das Perdas \(tabela X06\_PERDA\_GANHO\)\.
- Alíquota Ad Rem Média Ponderada: não preencher
- Valor do ICMS sobre o Óleo Diesel A: não preencher
- Valor do ICMS sobre o B100: não preencher

Obs:

1. As quantidades das perdas e ganhos já estão na unidade de medida que deve ser apresentado o anexo, por isso a conversão de unidade de medida não é aplicada\. Linha gerada a partir das Perdas do combustível informadas manualmente na opção do menu Movimento de Distribuidora 🡪 Perdas e Ganhos por Grupo de Combustíveis e Derivados\.  Também é possível importar essas informações através da SAFX06\.
2. Os Ato Cotepe 22/23 e 44/23 orientam preencher apenas as quantidades, por isso os campos de Valor do ICMS não foram preenchidos\. Veja:

“*2\.5\.2\.9\. PERDAS \- Informar quantidades de perdas, até o percentual permitido na legislação da ANP, para ajustar às quantidades existentes de fato em estoque\.”*

### <a id="_Toc199928247"></a>Linha 12: Ganhos

Linha gerada a partir dos Ganhos do combustível informados manualmente na opção do menu Movimento de Distribuidora 🡪 Perdas e Ganhos por Grupo de Combustíveis e Derivados\.  Também é possível importar essas informações através da SAFX06\.

__Critério de Recuperação__:

Consultar o “Movimento de Perdas e Ganhos por Grupo de Combustível” \(tabela X06\_PERDA\_GANHO\) com os seguintes critérios:

- Empresa de login
- Estabelecimento informado na tela de geração
- Mês/Ano Referencia: informado na tela de geração
- Tipo = __Ganho__
- Grupo Combustível: considerar todos os grupos combustíveis do Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB\) recuperados a partir dos critérios:
	- Produto SEF do Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB campo COD\_PROD\_SEF\) = COD\_PROD\_SEF da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\)
	- COD\_ANEXO da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) = ‘1M’ 
	- COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) = 

= ‘DSL’, p/ opção de Combustível selecionada na tela de geração for “Diesel \- DSL, BXD, S10 e BXS”

                                              = ‘DSM’, p/ opção de Combustível selecionada na tela de geração for “Diesel Marítimo \- DSM”

                                              = ‘GSL’, p/ opção de Combustível selecionada na tela de geração for “Gasolina \- GSL e GSC”

                                              = ‘GSP’, p/ opção de Combustível selecionada na tela de geração for “Gasolina Premium \- GSP e GCP”

                                              = ‘GSV’, p/ opção de Combustível selecionada na tela de geração for “Gasolina de Aviação \- GSV”

As quantidades de ganho recuperadas para cada Grupo de Combustível devem ser totalizadas e gravadas em nome do COD\_PROD\_SEF\_CENTR, relacionado ao Combustível selecionado na tela de Geração\. Vide [RN00](#_RN00_–_Regra)\.

Exemplo: Registro de Ganho de dois Grupos Combustíveis \(Produto SEF “DSL” e “BXD”\) são consolidados e gravados na linha 12 para o Combustível “DSL” \(COD\_PROD\_SEF\_CENTR da TACES114\)\.

__Regra de Preenchimento dos Campos:__

- Empresa; preencher com a empresa de login
- Estabelecimento informado na tela de geração
- Mês/Ano Referencia: informado na tela de geração
- Combustível:  COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) referente ao Combustível selecionado na tela de Geração\.
- Quantidade de Combustível: preencher com campo Qtde de Combustível dos Ganhos \(tabela X06\_PERDA\_GANHO\)\.
- Quantidade de Óleo Diesel A \(Base de Cálculo\): preencher com campo Qtde Gasolina A/Diesel A dos Ganhos \(tabela X06\_PERDA\_GANHO\)\.
- Quantidade de B100 na Mistura a Ser Comercializada a Consumidor Final \(Base de Cálculo Retenção\): preencher com campo Qtde EAC/B100 dos Ganhos \(tabela X06\_PERDA\_GANHO\)\.
- Alíquota Ad Rem Média Ponderada: não preencher
- Valor do ICMS sobre o Óleo Diesel A: não preencher
- Valor do ICMS sobre o B100: não preencher

Obs:

1. As quantidades das perdas e ganhos já estão na unidade de medida que deve ser apresentado o anexo, por isso a conversão de unidade de medida não é aplicada\. Linha gerada a partir das Perdas do combustível informadas manualmente na opção do menu Movimento de Distribuidora 🡪 Perdas e Ganhos por Grupo de Combustíveis e Derivados\.  Também é possível importar essas informações através da SAFX06\.
2. Os Ato Cotepe 22/23 e 44/23 orientam preencher apenas as quantidades, por isso os campos de Valor do ICMS não foram preenchidos\. Veja:

*“2\.5\.2\.10\. GANHOS \- Informar quantidades de ganhos, até o percentual permitido na legislação da ANP, para ajustar às quantidades existentes de fato em estoque\.”*

### <a id="_Linha_13:_Estoque"></a><a id="_Toc199928248"></a>Linha 13: Estoque Final

Linha gerada a partir da totalização das linhas 7 \- Total das Entradas \(Disponível \+ Devolução\), 10 \- Total das Saídas, 11 \- Perdas e 12 \- Ganhos do __Quadro 1__ do Anexo I\-M:

__Regra de Preenchimento dos Campos:__

- Empresa; preencher com a empresa de login
- Estabelecimento informado na tela de geração
- Mês/Ano Referencia: informado na tela de geração
- Combustível:  COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) referente ao Combustível selecionado na tela de Geração\.
- Quantidade de Combustível: preencher com o resultado do cálculo abaixo, considerar o campo “Quantidade de Combustível”:

                                 linha 7 \(Total das Entradas\) menos linha 10 \(Total das Saídas\) menos linha 11 \(Perdas\) mais linha 12 \(Ganhos\)

- Quantidade de Óleo Diesel A \(Base de Cálculo\): preencher com o resultado do cálculo abaixo, considerar o campo “Quantidade de Óleo Diesel A \(Base de Cálculo\)”:

                                 linha 7 \(Total das Entradas\) menos linha 10 \(Total das Saídas\) menos linha 11 \(Perdas\) mais linha 12 \(Ganhos\)

- Quantidade de B100 na Mistura a Ser Comercializada a Consumidor Final \(Base de Cálculo Retenção\): preencher com o resultado do cálculo abaixo, considerar o campo “Quantidade de B100 na Mistura a Ser Comercializada a Consumidor Final \(Base de Cálculo Retenção\)”

                                 linha 7 \(Total das Entradas\) menos linha 10 \(Total das Saídas\) menos linha 11 \(Perdas\) mais linha 12 \(Ganhos\)

- Alíquota Ad Rem Média Ponderada: preencher com o campo “Alíquota Ad Rem Média Ponderada” da linha 5\.
- Valor do ICMS sobre o Óleo Diesel A: preencher com o resultado do cálculo considerando os campos da linha 13:

                                  Quantidade de Óleo Diesel A \(Base de Cálculo\) \* Alíquota Ad Rem Média Ponderada

- Valor do ICMS sobre o B100: preencher com o resultado do cálculo considerando os campos da linha 13:

Considerar o COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) referente ao Combustível selecionado na tela de Geração, para saber se o Anexo é do Diesel ou Gasolina, pois para Diesel, aplica a proporção de 33,33% definida na cláusula décima primeira do Convênio ICMS nº 199/22 correspondente à parcela devida à UF de destino\.

Se COD\_PROD\_SEF\_CENTR = DSL ou DSM \(Diesel\) então:

                                  Quantidade de B100 na Mistura a Ser Comercializada a Consumidor Final \(Base de Cálculo Retenção\) \* Alíquota Ad Rem Média Ponderada \* __0,3333__

Se COD\_PROD\_SEF\_CENTR = GSL ou GSP ou GSV \(Gasolina\) então:

                                  Quantidade de B100 na Mistura a Ser Comercializada a Consumidor Final \(Base de Cálculo Retenção\) \* Alíquota Ad Rem Média Ponderada

__Observação sobre Transporte do Estoque Final do Período para o Período Seguinte:__

O estoque final calculado na linha 13 não poderá ser gravado como Estoque Inicial do período seguinte na opção “Movimento de Estoque Inicial por Grupo de Combustível” \(tabela CBT\_GRP\_ESTOQ\) pois o estoque final foi calculado considerando mais de um Grupo Combustível, consolidando no COD\_PROD\_SEF\_CENTR\.

## <a id="_Toc199928249"></a>RN02 \- Geração do Quadro 2 \- Apuração da Proporcionalidade por Fornecedor

Quadro gerado a partir de duas origens:

\- Estoque inicial por Grupo Combustível e Derivados/Fornecedor informado no menu Movimento de Distribuidora\.

\- Notas fiscais de Entradas Normais, totalizadas do [__Quadro 3__](#_RN03_-_Geração) do Anexo I\-M\.

__Critério de Recuperação do Estoque Inicial por Grupo Combustível e Derivados/Fornecedor:__

Consultar o “Movimento de Estoque Inicial por Grupo de Combustível e Derivados/Fornecedor” \(tabela CBT\_GRP\_PFJ\_ESTOQ\) com os seguintes critérios:

- Empresa de login
- Estabelecimento informado na tela de geração
- Mês/Ano Referencia: informado na tela de geração
- Grupo Combustível: considerar todos os grupos combustíveis do Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB\) recuperados a partir dos critérios:
	- Produto SEF do Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB campo COD\_PROD\_SEF\) = COD\_PROD\_SEF da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\)
	- COD\_ANEXO da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) = ‘1M’ 
	- COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) = 

= ‘DSL’, p/ opção de Combustível selecionada na tela de geração for “Diesel \- DSL, BXD, S10 e BXS”

                                              = ‘DSM’, p/ opção de Combustível selecionada na tela de geração for “Diesel Marítimo \- DSM”

                                              = ‘GSL’, p/ opção de Combustível selecionada na tela de geração for “Gasolina \- GSL e GSC”

                                              = ‘GSP’, p/ opção de Combustível selecionada na tela de geração for “Gasolina Premium \- GSP e GCP”

                                              = ‘GSV’, p/ opção de Combustível selecionada na tela de geração for “Gasolina de Aviação \- GSV”

O Estoque Inicial lido para cada Grupo de Combustível deve ser totalizado e gravado em nome do COD\_PROD\_SEF\_CENTR, relacionado ao Combustível selecionado na tela de Geração\. Vide [RN00](#_RN00_–_Regra)\.

Exemplo: Estoque Inicial de dois Grupos Combustíveis \(Produto SEF “DSL” e “BXD”\) são consolidados e gravados na linha 1 para o Combustível “DSL” \(COD\_PROD\_SEF\_CENTR da TACES114\)\.

Totalizar o Estoque Inicial por COD\_PROD\_SEF\_CENTR e CNPJ do Fornecedor \(campo 06\-CPF\_CGC da SAFX04\)\.

__Critério de Recuperação das Notas fiscais de Entradas Normais, totalizadas do Quadro 3 do Anexo I\-M:__

Mesmos critérios aplicados na recuperação das notas fiscais de entrada do [Quadro 3](#_RN03_-_Geração):

__Regra de Preenchimento dos Campos:__

- Empresa; preencher com a empresa de login
- Estabelecimento informado na tela de geração
- Mês/Ano Referencia: informado na tela de geração
- Combustível:  COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) referente ao Combustível selecionado na tela de Geração\.
- CNPJ: preencher com o campo 06\-CPF\_CGC da SAFX04 do Fornecedor das duas origens: 
	- Movimento de Estoque Inicial por Grupo de Combustível e Derivados/Fornecedor,
	- Notas Fiscais de Entrada apresentadas no Quadro 3\.

      Caso o campo 06\-CPF\_CGC da SAFX04 não esteja preenchido, informar Zeros\.

- Tipo: Preencher de acordo com o Cadastro de Pessoa Física Jurídica por Ramo de Atividade, disponível no Módulo: BÁSICOS > DATAWAREHOUSE > Manutenção > Cadastros Parâmetros > Pessoa Física/Jurídica por Ramo de Atividade\. Esse cadastro também pode ser importado via SAFX45\. Tabela: PRT\_PFJ\_MSAF
	- Preencher com “COM” para Classificação de Atividade igual a:
		- 94 – Refinaria
		- 95 – Formulador
		- 96 – CPQ
		- 97 \- Importador
	- Preencher com “SEM” para as demais Classificações de Atividade\.

Caso a Pessoa Fis/Jur não possua cadastro, gravar mensagem de aviso no log:

Pessoa Fisica/Juridica sem parametrização de Categoria no cadastro de Ramo de Atividade\.

Acesse o Módulo Data Warehouse, menu Manutenção >> Cadastros Parâmetros >> Pessoa Física/Jurídica por Ramo de Atividade, e inclua a classificação da atividade para o fornecedor\. O cadastro também pode ser importado via SAFX45\.

Gr\./Ind\./Cod\./CNPJ/Razão Social: xx/x/xxxx/xxxxxxx/xxxxxxxxxxxxxxxxxxx

- Estoque Inicial: preencher com campo “Qtde Gasolina A/Diesel A” do Movimento de Estoque Inicial por Grupo de Combustível e Derivados/Fornecedor \(tabela CBT\_GRP\_PFJ\_ESTOQ\)\.
- Recebimentos: preencher com o somatório do campo “Quantidade de Óleo Diesel A \(Base de Cálculo\)” das notas fiscais do fornecedor, apresentadas no [Quadro 3](#_RN03_-_Geração), ajustada com a aplicação do FCV \(???\)\.

\*\* PENDENTE DE DEFINIÇÃO \*\*

Quando o fornecedor for a refinaria de petróleo ou suas bases, a CPQ, o Formulador ou o Importador, com faturamento do produto convertido a 20o C, as quantidades deverão ser ajustadas com a aplicação do FCV \(Fator de Correção do Volume\) para a UF do emitente do relatório\.

- Total Disponível: Somatório dos campos anteriores “Estoque Inicial” e “Recebimentos”
- Proporção: preencher com o resultado da divisão: 

                                              \(“Total Disponível” do Fornecedor / Somatório do “Total Disponível” de todos os fornecedores\) \* 100

Informar o percentual com seis casas decimais

- Estoque Final: preencher com o resultado da multiplicação do campo “Quantidade de Óleo Diesel A \(Base de Cálculo\)” da [linha 13 – Estoque Final](#_Linha_13:_Estoque) do Quadro 1 pela Proporção calculada para o Fornecedor

                                  \[ “Quantidade de Óleo Diesel A \(Base de Cálculo\)” \* Proporção \]/100

Quando a participação percentual de determinado fornecedor for inferior a 1%, as quantidades relativas a este fornecedor deverão ser incorporadas ao fornecedor com maior percentual de participação no estoque\. No caso de operações de transferências entre estabelecimentos do mesmo núcleo de CNPJ, este percentual será de 10%\.

Ao final do cálculo do quadro 2, para todos os fornecedores aplicar o ajuste descrito acima\. Verificar se o CNPJ do fornecedor está no cadastro dos Estabelecimentos da Empresa de login\. Caso seja um CNPJ de algum estabelecimento, considerar 10% senão considerar 1% na aplicação da regra acima\.

## <a id="_RN03_-_Geração"></a><a id="_Toc199928250"></a>RN03 \- Geração do Quadro 3 \- Relação dos Recebimentos no Período \(Notas Fiscais de Entrada\)

Quadro gerado a partir das Notas de Entrada normal \(não considerar devoluções\) de Produtos sujeitos à tributação monofásica\.

__Critério de Recuperação__:

Para geração desse quadro recuperar os documentos fiscais a partir das tabelas SAFX07, SAFX08, SAFX325, considerando os seguintes critérios:

- Código da empresa = código da empresa da geração; 
- Estabelecimento informado na tela de geração
- Data Fiscal compreendida no mês/ano Referência informado na geração;
- __Notas fiscais de Entrada \(MOVTO\_E\_S <> ‘9’\)__
- __Notas fiscais Normais \(NORM\_DEV = ‘1’\)__
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Somente notas com item de mercadoria \(SAFX08\);
-  Somente itens com CFOP ou CFOP/NAT parametrizados no menu: Parâmetros > Anexos I, II, III, IV, V, VI e VIII para o tipo:

__  89 – Entrada de Combustíveis e Derivados__

__  687 – Remessa em Bonificação, Doação ou Brinde__

__  688 \- Empréstimos__

- Somente notas com Informações de Tributação do ICMS Monofásico \(SAFX325\);
- Código da Sit\. Estadual “B” \(campo 1 da SAFX08\) = ‘02’, ‘15’, ‘53’ ou ‘61’;
- Considerar a Parametrização da Regras p/ Geração dos Anexos feita para o estabelecimento no item de menu: Parâmetros > Regras p/ Geração dos Anexos\. 
- Se o Campo “Considerar somente as Notas Fiscais com movimentação física de mercadoria” estiver marcado, recuperar apenas itens com Ind\. Movim\. Física da Merc\. \(campo 115\-IND\_MOV\_FIS da SAFX08\) = ‘S’;
- Se desmarcado, recuperar independente do Ind\. Movim\. Física da Merc\. \(campo 115\-IND\_MOV\_FIS da SAFX08\) ser S ou N\.
- Produto do item da nota deve ser parametrizado no item de menu: Parâmetros > Produtos x Grupos de Combustíveis e Derivados, com o seu respectivo grupo de combustíveis \(SAFX96\)
- Quanto ao Grupo de Combustível parametrizado para o Produto: considerar todos os grupos combustíveis do Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB\) recuperados a partir dos critérios:
	- Produto SEF do Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB campo COD\_PROD\_SEF\) = COD\_PROD\_SEF da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\)
	- COD\_ANEXO da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) = ‘1M’ 
	- COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) = 

= ‘DSL’, p/ opção de Combustível selecionada na tela de geração for “Diesel \- DSL, BXD, S10 e BXS”

                                              = ‘DSM’, p/ opção de Combustível selecionada na tela de geração for “Diesel Marítimo \- DSM”

                                              = ‘GSL’, p/ opção de Combustível selecionada na tela de geração for “Gasolina \- GSL e GSC”

                                              = ‘GSP’, p/ opção de Combustível selecionada na tela de geração for “Gasolina Premium \- GSP e GCP”

                                              = ‘GSV’, p/ opção de Combustível selecionada na tela de geração for “Gasolina de Aviação \- GSV”

   Localização: Parâmetros >> Grupos de Combustíveis e Derivados

__Regra de Preenchimento dos Campos:__

- Empresa; preencher com a empresa de login
- Estabelecimento informado na tela de geração
- Mês/Ano Referencia: informado na tela de geração
- Combustível:  COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) referente ao Combustível selecionado na tela de Geração\.
- Dados do Fornecedor: 

Preencher com informações do Cadastro da Pessoa Física Jurídica \(SAFX04\), referente à Pessoa Fis/Jur da Nota Fiscal \(campos 06 e 07 – Ind\_fis\_jur e Cod\_fis\_jur da SAFX07\)

- 
	- CNPJ: Preencher com o campo 06\-CPF\_CGC da SAFX04\.
	- Inscrição Estadual Preencher com o campo 08\-INSC\_ESTADUAL da SAFX04\.
	- Razão Social Preencher com o campo 05\- RAZAO\_SOCIAL da SAFX04\.
	- Endereço: Preencher com os campos 12\- ENDERECO \+ 13\- NUM\_ENDERECO \+ 14\- COMPL\_ENDERECO \+ 15\- BAIRRO da SAFX04 \+ Descrição do Município referente ao campo 25\-COD\_MUNICIPIO da SAFX04\.
	- UF: Preencher com o campo 19\-UF da SAFX04\.
- Número da Nota Fiscal: Preencher com o campo 08\-NUM\_DOCFIS da SAFX07\.
- Modelo: Preencher com o campo 13\-COD\_MODELO da SAFX07
- Série: Preencher com o campo 09\-SERIE\_DOCFIS da SAFX07\.
- Data: Preencher com 11 – DATA\_EMISSAO da SAFX07
- CFOP: Preencher com o campo 08\-COD\_CFO da SAFX08\.
- Quantidade de Combustível:  Preencher com o campo 24\-QUANTIDADE da SAFX08\.

Deve\-se aplicar o fator de conversão de unidades de medidas, quando a medida do item for diferente da medida parametrizada no menu: Parâmetros > Produtos x Grupos de Combustíveis e Derivados \(SAFX96\)\. Vide [RN00\.c](#_RN00.c_–_Regra)\.

- Quantidade de Óleo Diesel A \(Base de Cálculo\): Aplicar a regra [RN00\.d](#_RN00.d_–_Regra)
- Quantidade de B100 na Mistura a Ser Comercializada a Consumidor Final \(Base de Cálculo Retenção\): Aplicar a regra [RN00\.e](#_RN00.e_–_Regra)\.
- Alíquota Ad Rem

Se o Código da Situação Estadual “B” \(campo 31 da SAFX08\) estiver preenchido com ‘02’, ‘15’ ou ‘53’, então:

   Preencher com o campo 22\- ALIQ\_AD\_REM\_ICMS da SAFX325\. 

Se o Código da Situação Estadual “B” \(campo 31 da SAFX08\) estiver preenchido com ‘61’, então:

   Preencher com o campo 33\- ALIQ\_AD\_REM\_ICMS\_RET da SAFX325\. 

Obs regra baseada no registro 45 do SCANC Distribuidora

- Valor do ICMS sobre o Óleo Diesel A: Aplicar a regra [RN00\.f](#_RN00.f_–_Regra)
- Valor do ICMS sobre o B100: Aplicar a regra [RN00\.g](#_RN00.g_–_Regra)

## <a id="_RN04_-_Geração"></a><a id="_Toc199928251"></a>RN04 \- Geração do Quadro 4 \- Resumo das Remessas Realizadas no Período \(Saídas\)

Quadro gerado a partir do somatório as Notas de Saída Normais subtraindo as entradas por devolução\.

__Critério de Recuperação__:

Para geração desse quadro recuperar os documentos fiscais a partir das tabelas SAFX07, SAFX08, SAFX325, considerando os seguintes critérios:

- Código da empresa = código da empresa da geração; 
- Estabelecimento informado na tela de geração
- Data Fiscal compreendida no mês/ano Referência informado na geração;
- __Notas fiscais de Saída Normal \(MOVTO\_E\_S = ‘9’ e NORM\_DEV = ‘1’\)__

Ou

__Notas fiscais de Entrada por Devolução \(MOVTO\_E\_S <> ‘9’ e NORM\_DEV = ‘2’\)__

- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Somente notas com item de mercadoria \(SAFX08\);
-  Somente itens com CFOP ou CFOP/NAT parametrizados no menu: Parâmetros > Anexos I, II, III, IV, V, VI e VIII para o tipo:

  __88 – Saída de Combustíveis e Derivados__

__  90 – Devolução de Venda de Combustíveis e Derivados__

__  92 – Saída a Consumidor Final__

__  93 – Devolução de Venda a Consumidor Final__

__  687 – Remessa em Bonificação, Doação ou Brinde__

__  688 \- Empréstimos__

- Somente notas com Informações de Tributação do ICMS Monofásico \(SAFX325\);
- Código da Sit\. Estadual “B” \(campo 1 da SAFX08\) = ‘02’, ‘15’, ‘53’ ou ‘61’;
- Considerar a Parametrização da Regras p/ Geração dos Anexos feita para o estabelecimento no item de menu: Parâmetros > Regras p/ Geração dos Anexos\. 
- Se o Campo “Considerar somente as Notas Fiscais com movimentação física de mercadoria” estiver marcado, recuperar apenas itens com Ind\. Movim\. Física da Merc\. \(campo 115\-IND\_MOV\_FIS da SAFX08\) = ‘S’;
- Se desmarcado, recuperar independente do Ind\. Movim\. Física da Merc\. \(campo 115\-IND\_MOV\_FIS da SAFX08\) ser S ou N\.
- Produto do item da nota deve ser parametrizado no item de menu: Parâmetros > Produtos x Grupos de Combustíveis e Derivados, com o seu respectivo grupo de combustíveis \(SAFX96\)
- Quanto ao Grupo de Combustível parametrizado para o Produto: considerar todos os grupos combustíveis do Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB\) recuperados a partir dos critérios:
	- Produto SEF do Cadastro de “Grupo de Combustível e Derivados” \(tabela CBT\_GRP\_COMB campo COD\_PROD\_SEF\) = COD\_PROD\_SEF da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\)
	- COD\_ANEXO da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) = ‘1M’ 
	- COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) = 

= ‘DSL’, p/ opção de Combustível selecionada na tela de geração for “Diesel \- DSL, BXD, S10 e BXS”

                                              = ‘DSM’, p/ opção de Combustível selecionada na tela de geração for “Diesel Marítimo \- DSM”

                                              = ‘GSL’, p/ opção de Combustível selecionada na tela de geração for “Gasolina \- GSL e GSC”

                                              = ‘GSP’, p/ opção de Combustível selecionada na tela de geração for “Gasolina Premium \- GSP e GCP”

                                              = ‘GSV’, p/ opção de Combustível selecionada na tela de geração for “Gasolina de Aviação \- GSV”

   Localização: Parâmetros >> Grupos de Combustíveis e Derivados

__Regra de Preenchimento dos Campos:__

- Empresa; preencher com a empresa de login
- Estabelecimento informado na tela de geração
- Mês/Ano Referencia: informado na tela de geração
- Combustível:  COD\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\) referente ao Combustível selecionado na tela de Geração\.
- Unidade Federada: UF da Pessoa Física Jurídica \(SAFX04\)\.  \(\*\)

Preencher com o campo 122\-UF\_DESTINO da SAFX07\. Caso não esteja preenchida, considerar a UF da Pessoa Física Jurídica \(SAFX04\)\.

Obs regra baseada no registro 45 do SCANC Distribuidora\.

- Quantidade de Combustível: Preencher com o campo 24\-QUANTIDADE da SAFX08, somando as saídas e subtraindo as devoluções\.

Deve\-se aplicar o fator de conversão de unidades de medidas, quando a medida do item for diferente da medida parametrizada no menu: Parâmetros > Produtos x Grupos de Combustíveis e Derivados \(SAFX96\)\. Vide [RN00\.c](#_RN00.c_–_Regra)\.

- Quantidade de Óleo Diesel A: Aplicar a regra [RN00\.d](#_RN00.d_–_Regra)

\(\*\) A definição de UF Federada não está considerando a UF de Destino \(campo 122 da SAFX07 como é a regra do SCANC\) por conta da orientação de preenchimento do Anexo II\-M – Operações interestaduais dos clientes, presente nos Ato Cotepe ICMS nº 22/23 \(diesel\) tópico 3\.5\.2\.15 e Ato Cotepe ICMS n° 44/23 \(Gasolina\) tópico 3\.5\.2\.17\.

Ato Cotepe ICMS nº 22/23 \(diesel\):

![](data:image/png;base64,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)

# <a id="_Toc199928252"></a>Regras para Emissão do Anexo I\-M

O anexo I\-M é gerado consolidado por Empresa, Estabelecimento, Período e Combustível\.

Layout com diferenças entre Diesel e Gasolina quantos aos títulos dos campos\. No Anexo do Diesel há referências para Óleo Diesel A e B100\. Já no Anexo da Gasolina, muda para Gasolina A e EAC\.

As definições do layout de todos os Anexos da Tributação Monofásica, estão nos Atos Cotepe ICMS nº 22/23 para Diesel e n° 44/23 para Gasolina\.

Exemplo de títulos:

Anexo I\-M para Diesel

Anexo I\-M para Gasolina

Colunas do Quadro 1: 

\- QUANTIDADE DE __ÓLEO DIESEL A__ \(BASE DE CÁLCULO\)

\- QUANTIDADE DE __B100__ NA MISTURA A SER COMERCIALIZADA A CONSUMIDOR FINAL \(BASE DE CÁLCULO RETENÇÃO\)

Colunas do Quadro 1: 

\- QUANTIDADE DE __GASOLINA A__ \(BASE DE CÁLCULO\)

\- QUANTIDADE DE __EAC__ NA MISTURA A SER COMERCIALIZADA A CONSUMIDOR FINAL \(BASE DE CÁLCULO RETENÇÃO\)

__Nome do Arquivo:__

CNPJ do Estabelecimento\_Ano\_Mes\_Anexo\_1M\_Combustível\.PDF ou XLS

__Cabeçalho__:

\- CNPJ:

  Preencher com o CNPJ do Cadastro do Estabelecimento\.

  Máscara do CNPJ: já considerar alfanumérico\.

  Máscara: XX\.XXX\.XXX/XXXX\-XX

\- Razão Social:

  Preencher com a Razão Social do Cadastro do Estabelecimento\.

\- Endereço:

  Preencher com as seguintes informações do Cadastro do Estabelecimento:

  Endereço \+ Número \+ Complemento \+ Bairro \+ Descrição do Município \+ Cep

\- UF

  Preencher com a UF do Cadastro do Estabelecimento:

\- Inscrição Estadual

  Preencher com a Inscrição Estadual cadastrada na tabela de Registro Estadual para a UF do Estabelecimento\.

  Localização: Módulo Parâmetros, menu: Preliminares 🡪 Inscrições Estaduais

  Máscara: XXX\.XXX\.XX\-X

\- Combustível: 

 Preencher com os campos COD\_PROD\_SEF\_CENTR \+ DSC\_PROD\_SEF\_CENTR da tabela CBT\_PROD\_SEF\_CENTR \(TACES114\)

\- Categoria: 

  Essa regra utilizará dois cadastros:

    \- Cadastros de Estabelecimentos x Pessoas Física/Jurídica, disponível no Módulo: Básicos > Data Warehouse, menu: Manutenção > Cadastros > Cadastros de Estabelecimentos x Pessoas Física/Jurídica; Tabela: DWT\_PFJ\_ESTAB

    \- Cadastro de Pessoa Física Jurídica por Ramo de Atividade, disponível no Módulo: Básicos > Data Warehouse, menu: Manutenção > Cadastros Parâmetros > Pessoa Física/Jurídica por Ramo de Atividade\. Esse cadastro também pode ser importado via SAFX45\. Tabela: PRT\_PFJ\_MSAF;

  O campo categoria deve ser preenchido com o Ramo de Atividade cadastrado para a Pessoa Fis/Jur que está associada ao estabelecimento \(campo DSC\_PARAM da PRT\_PAR2\_MSAF\)\.

__Anexo SEM MOVIMENTO__:

\- Texto “SEM MOVIMENTO” abaixo do cabeçalho\.

\- Os quadros 1, 2, 3, e 4 não serão apresentados

\- Considerar a coluna “PERIODO\_COM\_MOVIMENTO” na tabela do quadro 1\.

__Quadro 1__:

\- Ordenação: por Linha

\- Mesmo que a linha não esteja gravada na tabela, ela deve ser demonstrada no quadro 1\.

\- Quadro 1 completo com as 13 linhas, exceto quando o anexo é SEM MOVIMENTO\.

\- Alguns campos não são preenchidos para algumas linhas\. Esses campos são os marcados com ////////////////////////// na figura abaixo\.

![](data:image/png;base64,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)

__Quadro 2__:

\- Ordenação: por CNPJ do fornecedor

\- Quadro só é demonstrado se e houver registro na tabela\.

__Quadro 3:__

\- Ordenação: por CNPJ do fornecedor e número da nota fiscal\.

\- Quadro só é demonstrado se e houver registro na tabela\.

__Quadro 4__

\- Ordenação: por UF\.

\- Quadro só é demonstrado se e houver registro na tabela\.

