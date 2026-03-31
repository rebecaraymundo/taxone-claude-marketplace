# MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Tratamento Novo Produto sem Inventário

- **Fonte:** MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Tratamento Novo Produto sem Inventário.docx
- **Modificado:** 2023-12-27
- **Tamanho:** 97 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS 

\(IN\-RE 087/2020\) 

Tratamento para Novos Produtos sem Inventários 

__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS\-ST \- RS \(IN\-RE 048/2018\), itens:

Geração 🡪 IN\-RE 087/20 🡪 Geração dos Movimentos

	

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS72958__

Liliane Videira Assaf

Tratamento de produtos novos sem inventário\.

21/09/2021 

__MFS81749__

Liliane Assaf

Tratamento para Notas de Produtos Farmacêuticos de Distribuidores criada pela MFS66473

15/03/2022

__MFS518178__

Liliane Assaf

Limpeza da Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\), dos registros com IND\_GRAVACAO = B foi transferida para o início da Geração dos Movimentos

27/12/2023

Sumário

[1\.	Introdução	1](#_Toc83124124)

[2\.	Recuperação dos Dados e Processamento	1](#_Toc83124125)

[1º passo Limpeza	1](#_Toc83124126)

[2º Passo – Recuperar os Produtos Sujeitos a ST Movimentados no período de geração e sem registro Inventário	1](#_Toc83124127)

[3º Passo – Gravação da Tabela de Médias Ponderadas	1](#_Toc83124128)

#  

# <a id="_Toc83124124"></a>Introdução

Essa rotina faz o tratamento para produtos novos\. Ou seja, produtos que iniciaram sua movimentação no período da geração, não existia movimentação em período anterior e o cliente não carrega o inventário do último dia do mês anterior pois este registro não existe no sistema ERP de origem\.

Exemplo: geração do mês de setembro de 2021\. Primeira movimentação do produto \(nota de entrada\) em 15/09/2021\. Produto sem inventário na X52 para 31/08/2021\.

 

Esta rotina irá identificar tais produtos e carregar a tabela de médias ponderadas \(EST\_ST\_RS\_MEDIA\_POND\), para o produto e dia imediatamente anterior ao mês da geração com quantidades e valores zerados\.  A rotina de Transferência dos Movimentos para EFD Fiscal irá ler esse registro da tabela de médias ponderadas \(EST\_ST\_RS\_MEDIA\_POND\), e gerar um registro na X52 com quantidade e valores zerados\.

Essa rotina deve ser executada após o cálculo da média ponderada\.

Observação: Originalmente a rotina de Geração do Movimento exigia que todos os Produto sujeito a ICMS\-ST tivessem inventário carregados na SAFX52 para o dia imediatamente anterior ao mês da geração\.  Mas o cliente Magazine Luiza possui na faixa de 2000 produtos novos no mês e não carrega inventário para esses novos produtos\.

# <a id="_Toc350763252"></a><a id="_Toc59988568"></a><a id="_Toc83124125"></a>Recuperação dos Dados e Processamento 

## <a id="_1º_Passo_–"></a><a id="_Toc83124127"></a>1º Passo – Recuperar os Produtos Sujeitos a ST Movimentados no período de geração e sem registro Inventário 

Vamos recuperar os produtos sujeitos a ST, que exista movimento no período da geração e que não possua registro de inventário para o último dia do mês anterior\.

Para isso vamos fazer duas consultas: 

1. Consulta recuperando os produtos com movimento de entrada, devolução de entrada e devolução de saída no período, através da leitura da tabela de Média Ponderada \(com pelo menos um dia com quantidade >0\) e que não possua registro de inventário para o último dia do mês anterior\. 
2. Consulta recuperando os produtos com movimentação de saída no período, através da leitura da Tabela da Movimentação de Saída \(EST\_ST\_RS\_NF\_SAI\) e que não possua registro de inventário para o último dia do mês anterior\.

Veja o detalhamento das consultas a seguir:

a\) Consulta da tabela de Média Ponderada:

__Origem dos dados__:  \- Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\)\.

                                  

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data – pertencente ao período que está sendo processado;

\- Qtde total Convertida Inicial \(QTD\_CONV\_INI\) >0 __OU__ Quantidade de Devolução de Saída \(QTD\_CONV\_DEV\_SAI\_MP\) > 0 __OU__ 

   Quantidade Entrada Convertida \(QTD\_CONV\_ENT\_MP\)>0 __OU__ Quantidade Devolução de Entrada \(QTD\_CONV\_DEV\_ENT\_MP\) >0 __OU__ 

   Qtde total Convertida Final \(QTD\_CONV\_FIM\)> 0

\- __NÃO EXISTE__ registro de Inventário para o produto na Tabela do Inventário \(X52\_INVENT\_PRODUTO\), com os critérios:

- Data do Inventário \(campo 03 \- DATA\_INVENTARIO\) último dia do mês anterior que está sendo processado;
- Motivo do Inventário \(campo 40 \- IND\_MOT\_INV\) = “06” \- controle das mercadorias sujeitas ao regime de substituição tributária;
- Grupo Contagem \(campo 04 \- GRUPO\_CONTAGEM\) 🡪 1, 2, 3 e 5;
- IND\_GRAVACAO \(X52\)  <> 9 \-\- significa que o cliente não carregou a x52

\[__MFS518178__\]: Limpeza da Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\), dos registros com IND\_GRAVACAO = B foi incluída no início da Geração dos Movimentos\. Dessa forma esse critério se tornou desnecessário:

 __Ou __

  __EXISTE__ registro de Inventário para o produto na Tabela do Inventário \(X52\_INVENT\_PRODUTO\), com os critérios:

- Data do Inventário \(campo 03 \- DATA\_INVENTARIO\) último dia do mês anterior que está sendo processado;
- Motivo do Inventário \(campo 40 \- IND\_MOT\_INV\) = “06” \- controle das mercadorias sujeitas ao regime de substituição tributária;
- Grupo Contagem \(campo 04 \- GRUPO\_CONTAGEM\) 🡪 1, 2, 3 e 5;
- IND\_GRAVACAO \(X52\) = 9 \-\- reprocessamento da geração do movimento qdo já ocorreu a Transferência dos Movimentos p/ EFD
- Existe registro na Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\), com os critérios abaixo atendidos:

   \- Empresa – código da empresa do login;

   \- Estabelecimento – código do estabelecimento selecionado para geração;

   \- Data = último dia do mês anterior que está sendo processado;  

   \- Produto = Produto da Parametrização de Produtos \(por Código, por NCM e por CEST\);

   \- IND\_GRAVACAO = ‘__B’__ – significa que o os valores unitários foram calculados por essa rotina

\- Só recuperar os Produtos estão no __primeiro período__ de geração\. 

  Ou seja, o Produto que __não__ possua registro na Tabela de Média Ponderada para algum dia do mês anterior, com quantidade maior que zero:

        __Origem dos dados__: \- Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\)\.

        __Critérios:__

   \- Empresa – código da empresa do login;

   \- Estabelecimento – código do estabelecimento selecionado para geração;

   \- Data pertencente ao mês anterior que está sendo processado;

        \- Produto = Produto da Parametrização de Produtos \(por Código, por NCM e por CEST\);

  \- Qtde total Convertida Inicial \(QTD\_CONV\_INI\) >0 __OU__ Quantidade de Devolução de Saída \(QTD\_CONV\_DEV\_SAI\_MP\) > 0 __OU__ 

    Quantidade Entrada Convertida \(QTD\_CONV\_ENT\_MP\)>0 __OU__ Quantidade Devolução de Entrada \(QTD\_CONV\_DEV\_ENT\_MP\) >0 __OU__ 

    Qtde total Convertida Final \(QTD\_CONV\_FIM\)> 0

__\[[MFS81749](https://jira.thomsonreuters.com/browse/MFS-81749" \o "TICKET 35007 - DW - ESTADUAL - Ressarcimento ICMS-ST RS - Produtos Farmacêuticos  - Não devem ser gerados os registros C180, C181, C185, C186, H030, nem cálculo de média de inventário para produtos parametrizados como farmacêuticos (parte 3))\]__

__Tratamento para Produtos Farmacêuticos de Distribuidores:__

\- Não recuperar os Produtos Farmaceuticos de Estabelecimentos Distribuidores\. Ou seja, se os dois critérios a seguir forem atendidos, não recuperar o produto da Média Ponderada:

- Estabelecimento é um __Distribuidor__ \(atacadista\), ou seja, na Tela de Dados Iniciais estiver com o campo “Contribuinte Varejista?” = Não; 
- __Produto__ estiver cadastrado, na tela de Parametrização de Produtos Farmacêuticos por Código, no menu: Parametros >  \(IN\-RE 087/20\) > Produtos Farmacêuticos > Código

b\) Consulta da tabela de Movimentação de Saída:

Vamos recuperar os produtos sujeitos a ST, que exista movimento de __saída__ no período e que não possua registro de inventário para o último dia do mês anterior\. Para isso fazer a consulta a seguir:

__Origem dos dados__:  \- Tabela da Movimentação de Saída do Ressarcimento \(EST\_ST\_RS\_NF\_SAI\)

__Critérios:__

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data Fiscal – pertencente ao período que está sendo processado;

\- __NÃO EXISTE__ registro de Inventário para o produto na Tabela do Inventário \(X52\_INVENT\_PRODUTO\), com os critérios:

- Data do Inventário \(campo 03 \- DATA\_INVENTARIO\) último dia do mês anterior que está sendo processado;
- Motivo do Inventário \(campo 40 \- IND\_MOT\_INV\) = “06” \- controle das mercadorias sujeitas ao regime de substituição tributária;
- Grupo Contagem \(campo 04 \- GRUPO\_CONTAGEM\) 🡪 1, 2, 3 e 5;
- IND\_GRAVACAO \(X52\)  <> 9 \-\- significa que o cliente não carregou a x52

\[__MFS518178__\]: Limpeza da Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\), dos registros com IND\_GRAVACAO = B foi incluída no início da Geração dos Movimentos\. Dessa forma esse critério se tornou desnecessário:

 __Ou__

  __EXISTE__ registro de Inventário para o produto na Tabela do Inventário \(X52\_INVENT\_PRODUTO\), com os critérios:

- Data do Inventário \(campo 03 \- DATA\_INVENTARIO\) último dia do mês anterior que está sendo processado;
- Motivo do Inventário \(campo 40 \- IND\_MOT\_INV\) = “06” \- controle das mercadorias sujeitas ao regime de substituição tributária;
- Grupo Contagem \(campo 04 \- GRUPO\_CONTAGEM\) 🡪 1, 2, 3 e 5;
- IND\_GRAVACAO \(X52\) = 9 \-\- reprocessamento da geração do movimento qdo já ocorreu a Transferência dos Movimentos p/ EFD
- Existe registro na Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\), com os critérios abaixo atendidos:

   \- Empresa – código da empresa do login;

   \- Estabelecimento – código do estabelecimento selecionado para geração;

   \- Data = último dia do mês anterior que está sendo processado;  

   \- Produto = Produto da Parametrização de Produtos \(por Código, por NCM e por CEST\);

   \- IND\_GRAVACAO = ‘__B’__ – significa que o os valores unitários foram calculados por essa rotina

\- Só recuperar os Produtos estão no __primeiro período__ de geração\. 

  Ou seja, o Produto que __não__ possua registro na Tabela de Média Ponderada para algum dia do mês anterior, com quantidade maior que zero:

        __Origem dos dados__: \- Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\)\.

        __Critérios:__

   \- Empresa – código da empresa do login;

   \- Estabelecimento – código do estabelecimento selecionado para geração;

   \- Data pertencente ao mês anterior que está sendo processado;

        \- Produto = Produto da Parametrização de Produtos \(por Código, por NCM e por CEST\);

  \- Qtde total Convertida Inicial \(QTD\_CONV\_INI\) >0 __OU__ Quantidade de Devolução de Saída \(QTD\_CONV\_DEV\_SAI\_MP\) > 0 __OU__ 

    Quantidade Entrada Convertida \(QTD\_CONV\_ENT\_MP\)>0 __OU__ Quantidade Devolução de Entrada \(QTD\_CONV\_DEV\_ENT\_MP\) >0 __OU__ 

    Qtde total Convertida Final \(QTD\_CONV\_FIM\)> 0

__\[[MFS81749](https://jira.thomsonreuters.com/browse/MFS-81749" \o "TICKET 35007 - DW - ESTADUAL - Ressarcimento ICMS-ST RS - Produtos Farmacêuticos  - Não devem ser gerados os registros C180, C181, C185, C186, H030, nem cálculo de média de inventário para produtos parametrizados como farmacêuticos (parte 3))\]__

__Tratamento para Produtos Farmacêuticos de Distribuidores:__

\- Não recuperar os Produtos Farmaceuticos de Estabelecimentos Distribuidores\. Ou seja, se os dois critérios a seguir forem atendidos, não recuperar o produto do movimento de saída:

- Estabelecimento é um __Distribuidor__ \(atacadista\), ou seja, na Tela de Dados Iniciais estiver com o campo “Contribuinte Varejista?” = Não; 
- __Produto__ estiver cadastrado, na tela de Parametrização de Produtos Farmacêuticos por Código, no menu: Parametros >  \(IN\-RE 087/20\) > Produtos Farmacêuticos > Código

## <a id="_Toc83124128"></a>2º Passo – Gravação da Tabela de Médias Ponderadas

Para cada __Produto__ sujeito ao ICMS\-ST\(\*\), gravar um registro na tabela __EST\_ST\_RS\_MEDIA\_POND__ com os valores zerados, para o último dia do mês anterior\.

__Tabela EST\_ST\_RS\_MEDIA\_POND__

Os campos sinalizados com asterisco compõem a chave da tabela\.

__PK__

__Campo__

__Regra de Preenchimento__

\(\*\)

Código do Estabelecimento

COD\_ESTAB

Código do estabelecimento SELECIONADO na tela de geração

\(\*\)

Código da Empresa 

COD\_EMPRESA

Código da empresa de login 

\(\*\)

Código do Estabelecimento

COD\_ESTAB\_ORIG

Código do estabelecimento SELECIONADO na tela de geração

\(\*\)

Data 

DATA

Último dia do mês anterior\.

\(\*\)

Produto

Grupo\_Produto, Ind\_Produto,

Cod\_Produto

Produto sujeito ao ICMS\-ST foco do processamento\.

__Saldo Inicial do Dia__

Qtde total Convetida Inicial

QTD\_CONV\_INI

Preencher com zero\.

Valor do ICMS Calculado Inicial

VLR\_ICMS\_INI\_MP

Preencher com zero\.

Valor do ICMS\-ST Calculado Inicial

VLR\_ICMS\_ST\_INI\_MP

Preencher com zero\.

Valor Base de Cálculo do ICMS\-ST Calculado Inicial

VLR\_BC\_ST\_INI\_MP

Preencher com zero\.

Valor FECEP\-ST Calculado Inicial

VLR\_FECEP\_ST\_INI\_MP

Preencher com zero\.

__Devoluções das Saídas do Dia__

Quantidade Devolvida Convertida

QTD\_CONV\_DEV\_SAI\_MP

Preencher com zero\.

Valor do ICMS Calculado para Devolução

VLR\_ICMS\_DEV\_SAI\_MP

Preencher com zero\.

Valor do ICMS\-ST Calculado para Devolução

VLR\_ICMS\_ST\_DEV\_SAI\_MP

Preencher com zero\.

Valor Base de Cálculo do ICMS\-ST Calculado para Devolução

VLR\_BC\_ST\_DEV\_SAI\_MP

Preencher com zero\.

Valor FECEP\-ST Calculado para Devolução

VLR\_FECEP\_ST\_DEV\_SAI\_MP

Preencher com zero\.

__Entradas do Dia__

Quantidade Entrada Convertida

QTD\_CONV\_ENT\_MP

Preencher com zero\.

Valor do ICMS Calculado para Entrada

VLR\_ICMS\_ENT\_MP

Preencher com zero\.

Valor do ICMS\-ST Calculado para Entrada

VLR\_ICMS\_ST\_ENT\_MP

Preencher com zero\.

Valor Base de Cálculo do ICMS\-ST Calculado para Entrada

VLR\_BC\_ST\_ENT\_MP

Preencher com zero\.

Valor FECEP\-ST Calculado para Entrada

VLR\_FECEP\_ST\_ENT\_MP

Preencher com zero\.

__Devoluções das Entradas do Dia__

Quantidade Devolvida Convertida

QTD\_CONV\_DEV\_ENT\_MP

Preencher com zero\.

Valor do ICMS Calculado para Devolução

VLR\_ICMS\_DEV\_ENT\_MP

Preencher com zero\.

Valor do ICMS\-ST Calculado para Devolução

VLR\_ICMS\_ST\_DEV\_ENT\_MP

Preencher com zero\.

Valor Base de Cálculo do ICMS\-ST Calculado para Devolução

VLR\_BC\_ST\_DEV\_ENT\_MP

Preencher com zero\.

Valor FECEP\-ST Calculado para Devolução

VLR\_FECEP\_ST\_DEV\_ENT\_MP

Preencher com zero\.

__Saldo Final do Dia__

Qtde total Convetida Final

QTD\_CONV\_FIM

Preencher com zero\.

Valor do ICMS Calculado Final

VLR\_ICMS\_FIM\_MP

Preencher com zero\.

Valor do ICMS\-ST Calculado Final

VLR\_ICMS\_ST\_FIM\_MP

Preencher com zero\.

Valor Base de Cálculo do ICMS\-ST Calculado Final

VLR\_BC\_ST\_FIM\_MP

Preencher com zero\.

Valor FECEP\-ST Calculado Final

VLR\_FECEP\_ST\_FIM\_MP

Preencher com zero\.

__Valores Médios Unitários Calculados do Dia__

Valor Médio Unitário do ICMS

VLR\_UNIT\_ICMS\_FIM\_MP

Preencher com zero\.

Valor Médio Unitário do ICMS\-ST s/ FECEP 

VLR\_UNIT\_ICMS\_ST\_FIM\_MP

Preencher com zero\.

Valor Médio Unitário do ICMS\-ST c/ FECEP 

VLR\_UNIT\_ICMS\_ST\_FECEP\_FIM\_MP

Preencher com zero\.

Valor Médio Unitário da Base de Cálculo do ICMS\-ST

VLR\_UNIT\_BC\_ST\_FIM\_MP

Preencher com zero\.

Valor Médio Unitário do FECEP\-ST

VLR\_UNIT\_FECEP\_ST\_FIM\_MP

Preencher com zero\.

Indicador de Gravação

IND\_GRAVACAO

‘B’ – significa que o os valores unitários foram calculados por essa rotina

Número do Processo

PROC\_ID

Número do Processo da geração do movimento

\[__MFS518178__\]: Limpeza da Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\), dos registros com IND\_GRAVACAO = B foi transferida para o início da Geração dos Movimentos:

Obs: Limpar os registros de processos anteriores da tabela __EST\_ST\_RS\_MEDIA\_POND__ com IND\_GRAVACAO = B com os seguintes critérios:

- Empresa = Código da empresa de login
- Estabelecimento = Código do estabelecimento SELECIONADO na tela de geração
- Data = último dia do mês anterior que está sendo processado\.
- IND\_GRAVACAO = ‘B’ – significa que o os valores unitários foram calculados por essa rotina
- Número do Processo diferente do número do processo da geração em execução

  Limpar os registros de processos anteriores na Tabela do Inventário \(X52\_INVENT\_PRODUTO\), com os seguintes critérios:

- Data do Inventário \(campo 03 \- DATA\_INVENTARIO\) último dia do mês anterior que está sendo processado;
- Motivo do Inventário \(campo 40 \- IND\_MOT\_INV\) = “06” \- controle das mercadorias sujeitas ao regime de substituição tributária;
- Grupo Contagem \(campo 04 \- GRUPO\_CONTAGEM\) 🡪 1, 2, 3 e 5;
- Existe registro na Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\), com os critérios abaixo atendidos:

   \- Empresa – código da empresa do login;

   \- Estabelecimento – código do estabelecimento selecionado para geração;

   \- Data = último dia do mês anterior que está sendo processado;  

   \- Produto = Produto do inventário

   \- IND\_GRAVACAO = ‘__B’__ – significa que o os valores unitários foram calculados por essa rotina

   \- Numero do Processo diferente do número do processo da geração em execução

= = = = = =

 

