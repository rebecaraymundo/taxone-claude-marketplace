# MTZ-Ressarc-SC-Geracao_Movimentos_Entradas

- **Fonte:** MTZ-Ressarc-SC-Geracao_Movimentos_Entradas.docx
- **Modificado:** 2026-03-01
- **Tamanho:** 264 KB

---

THOMSON REUTERS

Módulo Ressarcimento e Complemento de ICMS\-ST – SC 

\(Portaria SEF 378/2018\) 

Geração dos Movimentos – Entradas 

__Localização__: Menu Estadual, módulo Ressarcimento de ICMS\-ST – SC \(Port\.SEF 378/2018\), menu Geração à Geração dos Movimentos à Entradas 

                                           DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS25917

Liliane V\. Assaf

Geração dos movimentos de Entrada e devoluções de Entrada \(parte 1\)

22/03/2019 

MFS25519

Liliane V\. Assaf

Geração dos movimentos de Entrada e devoluções de Entrada \(parte 2\)

17/04/2019 

MFS29913

Andréa Rocha

Alteração do preenchimento do campo 17\-VL\_ICMS

26/08/2019

__MFS30185__

Vânia Mattos

Atualização legal da Port\. SEF 208/2019:

\- Alteração na geração dos movimentos \(2130\);

\- Geração das informações do novo registro das notas complementares \(2133\);

03/09/2019

MFS30949

Andréa Rocha

Inclusão de um novo parâmetro em tela

07/10/2019

MFS31736

Andréa Rocha

Alteração do preenchimento do campo 15 – VL\_BC\_ICMS e 16 – ALIQ\_ICMS

01/11/2019

MFS32070

Andréa Rocha

Inclusão de um novo campo para a geração

02/03/2020

MFS34798

Andréa Rocha

Alteração do preenchimento do campo 17\-VL\_ICMS conforme Portaria 343/2019 

17/03/2020

MFS35374

Andréa Rocha

Alteração das regras para recuperar as notas fiscais de entrada, incluindo a quantidade final do inventário para limitar a busca das notas de entrada

20/05/2020

MFS68852

Liliane Assaf

Tratamento do campo 137 – Quantidade Convertida da SAFX08

12/07/2021

MFS58553

Liliane Assaf

Atualização Legal da Port\. SEF 013/2021

Tratamento da Nota Fiscal Eletrônica de Ajuste \(Entrada para Estorno\)

\- Alteração na Geração do movimento de entrada \(2130\);

\- Geração das informações do novo registro de notas de ajuste \(2135\)

Tratamento bastante semelhante ao aplicado às notas complementares \(MFS30185\)\.

02/08/2021

__MFS46838__

Tratamento do Perfil D

Alteração na lista de Estabelecimentos para considerar a Parametrização da “Centralização de Estabelecimentos p/ Perfil D”, demonstrando os estabelecimentos Centralizadores e Não Centralizados\.

Alteração na leitura dos movimentos de entrada e inventário para considerar o estabelecimento selecionado para geração e, caso este seja um estabelecimento centralizador, recuperar também os movimentos de entrada e inventário dos seus estabelecimentos centralizados\.

21/09/2021

__MFS78891__

Liliane Assaf

Correção do Fator de Conversão quando calculado pelo campo 137 – Quantidade Convertida da SAFX08\. Considerar que pode existir mais de um fator de conversão de uma medida origem XX para uma medida destino YY, quando relacionado a produtos distintos\. \(correção da MFS68852\)\.

Exemplo:

Med Origem | Medi Destino | Produto | Fator

UN               | PAC               | 1\-001     | 0,6

UN               | PAC               | 1\-002     | 0,12

21/03/2022

__MFS95515__

Andréa Rocha

Inclusão de um parâmetro na tela para definir se serão recuperadas as notas de devolução de meses anteriores ao período da geração, e tratamento do parâmetro na geração dos movimentos de entrada\. 

26/10/2022

__MFS591077__

Andréa Rocha

Inclusão do tratamento das Incorporações de Empresas/Estabelecimentos na geração dos movimentos de entrada\.

08/02/2024

__MFS684912__

Liliane Assaf

Atendimento a Portaria SEF nº 195/2024 que altera a Portaria SEF nº 378, de 2018\.

Tratamento do ingresso das mercadorias no regime de substituição tributária conforme Portaria SEF n° 195/2024, estabelecendo inclusão das seguintes informações no registro 2130:

\- Estoque no ingresso das mercadorias no regime de substituição tributária; \(NOTA 8 da Portaria SEF nº 378/2018\);

\- Notas de entrada por devolução de mercadoria cuja saída tenha ocorrido antes da data do seu ingresso no regime de substituição tributária\. \(NOTA 9 da Portaria SEF nº 378/2018\)\.

13/08/2025

Sumário

[1\.	Introdução:	1](#_Toc206180299)

[2\.	Parâmetros da Tela	1](#_Toc206180300)

[1\.	Recuperação dos Dados e Processamento	1](#_Toc206180301)

[2\.	Gravação dos Dados na Tabela dos Movimentos \(origem = SAFX07/SAFX08\)	1](#_Toc206180302)

[3\.	Regras de Negócio:	1](#_Toc206180303)

[5\.1 – Regra de Definição do Responsável pela Retenção:	1](#_Toc206180304)

[5\.2 – Preenchimento dos Campos Base de Cálculo do ICMS, Alíquota ICMS e Valor ICMS \(15 \- VL\_BASE\_ICMS ,16 \- ALIQ\_ICMS e 17 \- VL\_ICMS\):	1](#_Toc206180305)

[5\.3 – Preenchimento dos Campos Base de Cálculo ICMS\-ST Pago e Integral e Alíquotas ST Pago e Efetiva\(campos 18, 19, 20 e 21\)	1](#_Toc206180306)

[5\.4 – Preenchimento do Campo Valor ICMS\-ST \(23 – VL\_ICMS\_ST\)	1](#_Toc206180307)

[4\.	Gravação dos Dados das Notas Complementares	1](#_Toc206180308)

[5\.	Gravação dos Dados das Notas Fiscais Eletrônicas de Ajuste	1](#_Toc206180309)

# <a id="_Toc206180299"></a>Introdução:

__\[MFS35374\]__ Alteração da regra de recuperação das notas de entrada, anteriormente recuperava\-se as notas de entradas até que cobrisse a quantidade da saída\.  A alteração será para recuperar as entradas até cobrir o somatório da quantidade da saída e da quantidade de estoque final do inventário \(campo QTD do Registro H010\), se houver\.

\[__MFS684912__\] Inclusão de duas novas origens que precisam ser somadas à quantidade das notas de entradas recuperadas até cobrir a quantidade da saída e estoque final do inventário do produto:

1. Estoque no ingresso das mercadorias no regime de substituição tributária; \(NOTA 8 da Portaria SEF nº 378/2018\);
2. Notas de entrada por devolução de mercadoria cuja saída tenha ocorrido antes da data do seu ingresso no regime de substituição tributária\. \(NOTA 9 da Portaria SEF nº 378/2018\)\.

__Objetivo__: 

Carregar a movimentação das entradas e devoluções de entrada dos produtos sujeitos ao ICMS\-ST, do estoque no Ingresso das Mercadorias no Regime de Substituição Tributária \(NOTA 8 da Portaria SEF nº 378/2018\) e das entradas por devolução de mercadoria cuja saída tenha ocorrido antes da data do seu ingresso no regime de substituição tributária \(NOTA 9 da Portaria SEF nº 378/2018\)\. Os produtos considerados são aqueles que constam nos movimentos de Saída do período \(saídas por nota fiscal – registro 2113 e por ECF – registro 2112\)\.  

 

Para cada produto presente na movimentação das saídas do período, será realizada a busca das últimas entradas do produto mais do estoque no Ingresso das Mercadorias no Regime de Substituição Tributária, mais entradas por devolução de mercadoria cuja saída tenha ocorrido antes da data do seu ingresso no regime de substituição tributária, da maior para a menor data, que esteja dentro do período determinado pelas datas “Pesquisar últimas entradas até” e “Data Final”\. A busca finaliza quando a quantidade das entradas \(mais as quantidades do estoque no Ingresso das Mercadorias no Regime de Substituição Tributária e das entradas por devolução de mercadoria cuja saída tenha ocorrido antes da data do seu ingresso no regime de substituição tributária\), cobrir a quantidade da saída mais a quantidade final do inventário ou que a data limite informada em “*Pesquisar últimas entradas até*” seja atingida\.

__Pré\-Requisito: __

- Geração dos Movimentos de Saída \(item menu “Geração > Geração dos Movimentos > Saídas”\) 
- Geração dos Movimentos de Saída – ECF \(item menu “Geração > Geração dos Movimentos > Saídas \- ECF”\)

Como partiremos da tabela que armazena a movimentação das saídas resultantes dos processamentos da “Geração dos Movimentos de Saída” e “Geração dos Movimentos de Saída – ECF”, estes processos se tornam pré\-requisito para a Geração do Movimento das Entradas\.

Obs\.: As informações complementares sobre os documentos referenciados nas devoluções* não* são tratadas nesta geração\. Estas informações dão origem ao registro 2132 do meio magnético, e são recuperadas direto das tabelas SAFX116 e SAFX117 na própria geração do arquivo, quando se tratar de nota de devolução\. 

__Base Legal__: 

Portaria SEF 378\-2018 __\(__PeSEF de 03\.12\.18\) 

Decreto Nº 1\.024, de 11 de janeiro de 2017: conceitua alíquota interna e alíquota praticada\.

# <a id="_Toc206180300"></a>Parâmetros da Tela 

Período: MM/AAAA

Pesquisar últimas entradas até: DD/MM/AAAA

\[ \] Utilizar DATA MART

\[ \] Considerar Notas Fiscais de Devolução Somente do Período

\[ \] Considerar as notas fiscais da empresa incorporada

Estabelecimentos:         \[\\/\] Selecionar    \[ x \] Marcar Todos

\[x\] xxxxx – xxxxxxxxxxxxxxxxxxxxxxxxx

\[x\] xxxxx \- xxxxxxxxxxxxxxxxxxxxxxxxx

\[x\] xxxxx \- xxxxxxxxxxxxxxxxxxxxxxxxx

Funcionamento dos campos:

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/__

__Default__

__Regra__

<a id="_Hlk517437550"></a>Período

Data 

__S__

S

MM/AAAA

Neste campo será informado o período \(mês e ano\) para a geração do movimento\.

Deve ser um mês válido\.

Pesquisar últimas entradas até

Data

__S__

S

DD/MM/AAAA

__Default__: 01/01/XXXX, onde XXXX é o ano anterior à Data Inicial\.

Neste campo é informada a data limite até onde será feita a pesquisa das últimas notas de entrada do produto\.

Deve ser uma data válida e <= ao primeiro dia do Período informado\. Caso a Data informada neste campo seja maior que o primeiro dia do Período informado, exibir a mensagem de erro: “*Data da Pesquisa das últimas entradas deve ser anterior ao Período informado\.*

Obs: A pesquisa da movimentação das entradas é feita desde o Período informado até a data limite informada neste campo, sendo que ao atingir a quantidade da venda mais a quantidade final do inventário, a pesquisa é interrompida\. Assim, esta data é apenas um limite “*genérico”* para os casos em que as entradas não sejam encontradas \(para evitar que a pesquisa seja feita indeterminadamente\)\.

Utilizar DATA MART

\[__MFS30949__\]

Alfanumérico 

N

N

Checkbox

Default: desmarcado

Opção que permite ao usuário escolher se quer recuperar as notas fiscais das tabelas do DATA MART\.

Considerar Notas Fiscais de Devolução Somente do Período

Alfanumérico 

N

N

Checkbox

Default: desmarcado

__\[MFS95515__\] Inclusão do parâmetro para definir o tratamento das notas de devolução

Opção que permite ao usuário escolher se quer recuperar as notas fiscais de devolução somente do período da geração

Considerar as notas fiscais da empresa incorporada

Alfanumérico 

N

N

Checkbox

Default: desmarcado

__\[MFS591077__\] __Tratamento das Incorporações de Empresas/Estabelecimentos__

Este campo é um checkbox onde o usuário informa se vai considerar as notas fiscais de entrada da empresa incorporada, além das notas fiscais da empresa/estabelecimento da geração\.

Estabelecimentos

Alfanumérico 

__S__

S

Neste campo é exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário\.

Serão disponibilizados para seleção apenas os estabelecimentos de SC \(UF do estabelecimento = SC\)\.

__\[MFS46838\] Tratamento para Perfil D:__

A lista deve demonstrar os estabelecimentos que se enquadram na seguinte classificação:

\- __Centralizadores__: estabelecimentos parametrizados na “Centralização de Estabelecimentos p/ Perfil D” como Centralizador;

\- __Não centralizados__: estabelecimentos que não pertençam à “Centralização de Estabelecimentos p/ Perfil D”\. Ou seja, são os estabelecimentos da empresa de login, que não são estabelecimentos centralizadores nem centralizados\.

Selecionar

N

N

Esta opção é um facilitador que permite ao usuário selecionar um ou mais estabelecimentos através de uma janela de seleção da tabela de estabelecimentos\.

O filtro dos estabelecimentos disponibilizados para seleção segue a mesma regra descrita para o campo “Estabelecimento”:

\- Somente Estabelecimentos da empresa do login;

\- Somente Estabelecimentos da UF de SC;

\- __Centralizadores__: estabelecimentos parametrizados na “Centralização de Estabelecimentos p/ Perfil D” como Centralizador;

\- __Não centralizados__: estabelecimentos que não pertençam à “Centralização de Estabelecimentos p/ Perfil D”\. Ou seja, são os estabelecimentos da empresa de login, que não são estabelecimentos centralizadores nem centralizados\.

Quando esta opção é utilizada, após escolher os estabelecimentos e clicar no botão <OK> da janela de seleção, os estabelecimentos selecionados pelo usuário serão demonstrados no campo “Estabelecimentos” já marcados\. 

   

Marcar todos

N

N

Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados no campo “Estabelecimentos”\.

# <a id="_Recuperação_dos_Dados"></a><a id="_Toc350763252"></a><a id="_Toc206180301"></a>Recuperação dos Dados e Processamento

__Origem dos dados__: \- Parametrização de Produtos por Código / por NCM / por CEST;

                                  \- Parametrização de CFOP / Natureza de Operação;

                                  \- Se parâmetro “Utilizar DATA MART” estiver marcado    \[__MFS30949__\]

                                         SAFX07 / SAFX08 \- Tabelas dos Documentos Fiscais do DATA MART

                                    Senão

                                         SAFX07 / SAFX08 \- Tabelas dos Documentos Fiscais;

                                  \- Tabela dos Movimentos do módulo Ressarcimento e Complemento do ICMS\-ST – SC 

                                  \- Tabela dos Movimentos __de ECF__ do módulo Ressarcimento e Complemento do ICMS\-ST – SC

		          \- Tabela do Inventário de Estoque por Produto \(SAFX52\)  __\[MFS35374\]__

                                 \- Tabela da Parametrização das Mercadorias Ingressadas no Regime ST \[__MFS684912__\]

__Procedimento para Recuperação dos movimentos:__

__Passo 1: Recuperação dos Movimentos de Saída e Saída por ECF:__

\(a\) Totalizar a “Quantidade Convertida dos Movimentos de Saída” por produto:

Buscar os registros da Tabela dos Movimentos \(EST\_ST\_SC\_NF\) do módulo Ressarcimento e Complemento do ICMS\-ST – SC, para recuperar os movimentos de saída \(com devoluções das saídas\) do período\. 

Os critérios são os seguintes:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Código do estabelecimento selecionado em tela;
- Data do Período = último dia do mês/Ano do período informado em tela;
- Indicador do Tipo de Registro = ‘2113’

Recuperar o campo “Quantidade Convertida” de forma acumulada por __Produto__, somando o movimento de saída e subtraindo a devolução\.

Se campo “Nota de Devolução” \(*IND\_NOTA\_DEVOL*\) = “0” \(saída\), então:

Somar a “Quantidade Convertida” lida\.

Se campo “Nota de Devolução” \(*IND\_NOTA\_DEVOL*\) = “1” \(devolução\), então:

Subtrair a “Quantidade Convertida” lida\.

\(b\) Totalizar a “Quantidade Convertida dos Movimentos ECF” por produto:

Buscar os registros a Tabela dos Movimentos __de ECF__ \(EST\_ST\_SC\_ECF\) do módulo Ressarcimento e Complemento do ICMS\-ST – SC, para recuperar os movimentos de saída por ECF do período\. 

Os critérios são os seguintes:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Código do estabelecimento selecionado em tela;
- Data do Período = último dia do mês/Ano do período informado em tela;

Recuperar o campo “Quantidade Convertida” de forma acumulada por __Produto__\.

Obs: ECF não tem devolução, portanto o acúmulo é feito só somando a quantidade lida\.

\(c\) Calcular a “Quantidade Convertida Total Saída” por Produto:

“<a id="OLE_LINK2"></a>[Qtde Convertida Total Saída](#OLE_LINK11)” = “Quantidade Convertida dos Movimentos de Saída” \+ “Quantidade Convertida dos Movimentos ECF” 

Exemplo

Produto 

Qtde Convertida dos Movimentos de Saída

\(registro 2113\)

Qtde Convertida dos Movimentos ECF

\(registro 2112\)

Qtde Convertida Total Saída

1 – 001

1000,0000

2000,0000

3000,0000

1 – 002

4000,0000

1000,0000

5000,0000

Caso não exista movimento de Saída nem de Saída – ECF para o estabelecimento e período, ou seja, as consultas \(a\) e \(b\) acima definidas não retornem registro, gerar uma mensagem de erro no log da geração e finalizar o processo\. 

“Não é possível executar a geração do movimento de entrada, pois não há movimento de saída gerado para o estabelecimento e período informados\.

Favor executar as Gerações dos Movimentos de Saída \(item menu Geração > Geração dos Movimentos > Saídas e Saídas \- ECF\)\.”

Considerações:

\(1\) Pode existir movimento para um produto em apenas uma das consultas\. 

\(2\) Nesse cálculo não são consideradas as saídas pertinentes a devoluções das entradas, notas que compõe o registro 2130\.  \(Confirmado em reunião de 01/04/19\)

__Passo 2 \- Recuperação das Notas Fiscais de Entrada e Devolução de Entradas: __

\[__MFS95515__\] Inclusão do tratamento para o parâmetro que vai definir a forma de recuperar as notas de devolução

A partir de cada produto recuperado no __passo 1__, fazer uma consulta nas Tabelas de Documentos Fiscais, para recuperar os movimentos de entrada \(e devolução das entradas\) do período e de períodos anteriores\.

Os critérios são os seguintes:

- Código Empresa = código da empresa do login;
- Código Estabelecimento = código do estabelecimento selecionado para geração;

__\[MFS46838\] Tratamento para Perfil D:__

Caso o estabelecimento selecionado na tela de geração seja um estabelecimento __Centralizador__, recuperar os documentos fiscais do estabelecimento __Centralizador__ e dos seus estabelecimentos __Centralizados__, que foram a ele relacionados, na parametrização da “Centralização de Estabelecimentos p/ Perfil D”\.

Caso o estabelecimento selecionado na tela de geração seja um estabelecimento “__Não centralizado”__, recuperar os documentos fiscais apenas do estabelecimento selecionado para geração\.

- Quanto a Data fiscal, considerar:

Se o parâmetro “Considerar Notas Fiscais de Devolução Somente do Período” estiver desmarcado

       Data Fiscal – data compreendida entre as datas informadas em tela “__Pesquisar últimas entradas até__” a “__Data Final__”;

           Senão 

                 Se for uma nota normal \(campo NORM\_DEV= ‘1’\)

	           Data Fiscal – data compreendida entre as datas informadas em tela “__Pesquisar últimas entradas até__” a “__Data Final__”;

                 Senão \(Devolução \- campo NORM\_DEV= ‘2’\)

                      Data Fiscal – data compreendida no período da geração;

- Somente notas *não canceladas*;
- Somente notas *com itens*;
- Modelo – somente os documentos de modelo = 55 \(conforme Portaria SEF 378/2018, registro 2113\);   
- O produto do item deve constar na parametrização do menu “*Parâmetros à Produtos à Por Código*”, __ou__, seu NCM deve estar parametrizado no menu “*Parâmetros *à* Produtos *à* Por NCM*”, __ou__, seu CEST deve estar parametrizado no menu “*Parâmetros *à* Produtos *à* Por CEST*”\. 

Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração\.

No caso da parametrização dos produtos, primeiro é verificado se o produto consta na parametrização da opção “Por Código”\. Ao verificar a

parametrização por código, deve\-se considerar também os produtos associados\. Ou seja, o produto da nota deve constar como o produto

“principal” da parametrização \(__ESP\_SP\_PROD\_ST__\), ou ser um produto “associado” ao produto principal \(__ESP\_SP\_PROD\_ST\_ASS__\)\.  Lembrando que o produto recuperado no __passo 1 __é sempre produto principal\.

Os produtos “associados” são produtos cuja movimentação será demonstrada nos Registros 2112, 2113 e 2130 em nome do produto principal parametrizado\. 

A prioridade na pesquisa da parametrização dos produtos é: por Código, por NCM, e por último, por CEST, da seguinte forma:

\- Caso o produto conste na parametrização por código, a parametrização por NCM não precisa ser verificada\.

\- Caso não, é verificado se o NCM do produto \(NCM do cadastro do produto\) consta na parametrização da opção “Por NCM”\.

\- Caso o produto conste na parametrização por NCM, a parametrização por CEST não precisa ser verificada\.

\- Caso não, é verificado se o CEST do produto \(CEST do cadastro do produto\) consta na parametrização da opção “Por CEST”\.

- O CFOP ou CFOP/Natureza do item deve constar na parametrização do menu “*Parâmetros à Operações*” para alguma\(s\)  das seguintes

operações:

- 
	- Entradas \(e devoluções\) \(*parâmetro 740*\)

__Ordenação por:__

-  Produto 
- Data Fiscal em ordem decrescente

\- __Sobre as notas complementares__ \(alteração da __MFS30185 – Portaria 208/2019__\):

Durante a pesquisa das notas de entrada, quando se tratar de uma nota complementar \(campo “*125\-Situação Especial*” da capa = “5”\), o procedimento será o seguinte: 

A nota complementar *não será gerada na tabela dos movimentos*, pois *não será gravada no registro 2130 do arquivo*;

Ao invés disso, os seus valores serão somados à nota original, conforme descrito nas regras da gravação dos dados na tabela dos movimentos \(item 4\)\. A nota da operação original é a nota de referência informada no item da nota complementar, através dos campos 102, 117, 118 e 119 da

SAFX08;

Os dados de identificação da nota complementar serão armazenados em separado, sempre associados à nota da operação original, pois na geração do meio magnético darão origem aos registros 2133; 

\- __Sobre as Notas Fiscais Eletrônicas de ajuste__ \(alteração da __MFS58553 – Portaria 013/2021__\):

Durante a pesquisa das notas de entrada, quando se tratar de uma nota fiscal eletrônica de ajuste \(campo “*125\-Situação Especial*” da capa = “E”\), o procedimento será o seguinte: 

A nota fiscal eletrônica de ajuste *não será gerada na tabela dos movimentos*, pois *não será gravada no registro 2130 do arquivo*;

Ao invés disso, seus valores de Base de Cálculo ICMS\-ST e ICMS\-ST serão subtraídos da nota original \(campos 18 e 23 do 2130\), conforme descrito nas regras da gravação dos dados na tabela dos movimentos \(item 4\)\. A nota da operação original é a nota de referência informada no item da nota fiscal eletrônica de ajuste, através dos campos 102, 117, 118 e 119 da SAFX08;

Os dados de identificação da nota fiscal eletrônica de ajuste serão armazenados em separado, sempre associados à nota da operação original, pois na geração do meio magnético darão origem aos registros 2135; 

Obs: Diferentemente da Nota Complementar, a Nota Eletrônica de Ajuste não altera a quantidade da nota original, apenas os campos 18 – Base de Cálculo ICMS\-ST e 23 – Valor ICMS\-ST\.

\[__MFS684912__\] Inclusão do estoque no Ingresso das Mercadorias no Regime de Substituição Tributária, a ser somado à quantidade das notas de entradas recuperadas até cobrir a quantidade da saída e estoque final do inventário do produto\. \(NOTA 8 da Portaria SEF nº 378/2018\)\.

__Passo 2\.1 \- Recuperação do Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária: __

A partir de cada produto recuperado no __passo 1__, fazer uma consulta na Parametrização das Mercadorias Ingressadas no Regime ST, cuja manutenção está disponível no menu Parâmetros\.

Os critérios são os seguintes:

- Código Empresa = código da empresa do login;
- Código Estabelecimento = código do estabelecimento selecionado para geração;

__\[MFS46838\] Tratamento para Perfil D:__

Caso o estabelecimento selecionado na tela de geração seja um estabelecimento __Centralizador__, recuperar os documentos fiscais do estabelecimento __Centralizador__ e dos seus estabelecimentos __Centralizados__, que foram a ele relacionados, na parametrização da “Centralização de Estabelecimentos p/ Perfil D”\.

Caso o estabelecimento selecionado na tela de geração seja um estabelecimento “__Não centralizado”__, recuperar os documentos fiscais apenas do estabelecimento selecionado para geração\.

- Data do Ingresso – data compreendida entre as datas informadas em tela “__Pesquisar últimas entradas até__” a “__Data Final__”;
- Data de Recolhimento da 1ª Parcela da DISE – data compreendida entre as datas informadas em tela “__Pesquisar últimas entradas até__” a “__Data Final__”;
- Produto da Parametrização das Mercadorias Ingressadas no Regime ST deve constar na parametrização do menu “*Parâmetros à Produtos à Por Código*”, __ou__, seu NCM deve estar parametrizado no menu “*Parâmetros *à* Produtos *à* Por NCM*”, __ou__, seu CEST deve estar parametrizado no menu “*Parâmetros *à* Produtos *à* Por CEST*”\. 

Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração\.

No caso da parametrização dos produtos, primeiro é verificado se o produto consta na parametrização da opção “Por Código”\. Ao verificar a

parametrização por código, deve\-se considerar também os produtos associados\. Ou seja, o produto da Parametrização das Mercadorias Ingressadas no Regime ST deve constar como o produto “principal” da parametrização \(__ESP\_SP\_PROD\_ST__\), ou ser um produto “associado” ao produto principal \(__ESP\_SP\_PROD\_ST\_ASS__\)\.  Lembrando que o produto recuperado no __passo 1 __é sempre produto principal\.

Os produtos “associados” são produtos cuja movimentação será demonstrada nos Registros 2112, 2113 e 2130 em nome do produto principal parametrizado\. 

A prioridade na pesquisa da parametrização dos produtos é: por Código, por NCM, e por último, por CEST, da seguinte forma:

\- Caso o produto conste na parametrização por código, a parametrização por NCM não precisa ser verificada\.

\- Caso não, é verificado se o NCM do produto \(NCM do cadastro do produto\) consta na parametrização da opção “Por NCM”\.

\- Caso o produto conste na parametrização por NCM, a parametrização por CEST não precisa ser verificada\.

\- Caso não, é verificado se o CEST do produto \(CEST do cadastro do produto\) consta na parametrização da opção “Por CEST”\.

Recuperar a quantidade para ser somar com a quantidade das entradas recuperadas no __passo 2__, ordenando pela Data do Ingresso\.

\[__MFS684912__\] Notas de entrada por devolução de mercadoria cuja saída tenha ocorrido antes da data do seu ingresso no regime de substituição tributária, a ser somado à quantidade das notas de entradas recuperadas até cobrir a quantidade da saída e estoque final do inventário do produto\. \(NOTA 9 da Portaria SEF nº 378/2018\)\.

__Passo 2\.2 \- Recuperação das Notas de Entrada por Devolução de Mercadoria cuja Saída ocorreu antes da Data do Ingresso no Regime de Substituição Tributária: __

A partir de cada produto recuperado no __passo 1__, fazer uma consulta nas Tabelas de Documentos Fiscais, para recuperar os movimentos de devolução das saídas do período e de períodos anteriores\.

Os critérios são os seguintes:

- Código Empresa = código da empresa do login;
- Código Estabelecimento = código do estabelecimento selecionado para geração;

__\[MFS46838\] Tratamento para Perfil D:__

Caso o estabelecimento selecionado na tela de geração seja um estabelecimento __Centralizador__, recuperar os documentos fiscais do estabelecimento __Centralizador__ e dos seus estabelecimentos __Centralizados__, que foram a ele relacionados, na parametrização da “Centralização de Estabelecimentos p/ Perfil D”\.

Caso o estabelecimento selecionado na tela de geração seja um estabelecimento “__Não centralizado”__, recuperar os documentos fiscais apenas do estabelecimento selecionado para geração\.

- Devolução \- campo NORM\_DEV= ‘2’;
- Notas fiscais de entrada – campo MOVTO\_E\_S <> ‘9’;
- Quanto a Data fiscal, considerar:

Se o parâmetro “Considerar Notas Fiscais de Devolução Somente do Período” estiver desmarcado

       Data Fiscal – data compreendida entre as datas informadas em tela “__Pesquisar últimas entradas até__” a “__Data Final__”;

           Senão 

                  Data Fiscal – data compreendida no período da geração;

- Somente notas *não canceladas*;
- Somente notas *com itens*;
- Modelo – somente os documentos de modelo = 55 \(conforme Portaria SEF 378/2018, registro 2113\);   
- O produto do item deve constar na parametrização do menu “*Parâmetros à Produtos à Por Código*”, __ou__, seu NCM deve estar parametrizado no menu “*Parâmetros *à* Produtos *à* Por NCM*”, __ou__, seu CEST deve estar parametrizado no menu “*Parâmetros *à* Produtos *à* Por CEST*”\. 

Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração\.

No caso da parametrização dos produtos, primeiro é verificado se o produto consta na parametrização da opção “Por Código”\. Ao verificar a

parametrização por código, deve\-se considerar também os produtos associados\. Ou seja, o produto da nota deve constar como o produto

“principal” da parametrização \(__ESP\_SP\_PROD\_ST__\), ou ser um produto “associado” ao produto principal \(__ESP\_SP\_PROD\_ST\_ASS__\)\.  Lembrando que o produto recuperado no __passo 1 __é sempre produto principal\.

Os produtos “associados” são produtos cuja movimentação será demonstrada nos Registros 2112, 2113 e 2130 em nome do produto principal parametrizado\. 

A prioridade na pesquisa da parametrização dos produtos é: por Código, por NCM, e por último, por CEST, da seguinte forma:

\- Caso o produto conste na parametrização por código, a parametrização por NCM não precisa ser verificada\.

\- Caso não, é verificado se o NCM do produto \(NCM do cadastro do produto\) consta na parametrização da opção “Por NCM”\.

\- Caso o produto conste na parametrização por NCM, a parametrização por CEST não precisa ser verificada\.

\- Caso não, é verificado se o CEST do produto \(CEST do cadastro do produto\) consta na parametrização da opção “Por CEST”\.

- O CFOP ou CFOP/Natureza do item deve constar na parametrização do menu “*Parâmetros à Operações*” para alguma\(s\)  das seguintes operações:
- Venda à consumidor final
- Venda para outro estado
- Venda para optantes do Simples Nacional

__MFS64687__

- Venda óleo diesel para transporte coletivo de passageiros \(e Devoluções\)
- Venda de óleo diesel para embarcação pesqueira, com benefício de isenção \(e Devoluções\)
- Somente considerar devolução dos produtos que pertencem a Parametrização das Mercadorias Ingressadas no Regime ST
- Somente considerar a devolução se a operação de saída original ocorreu antes da Data do Ingresso da Mercadoria no Regime ST, obtida da Parametrização das Mercadorias Ingressadas no Regime ST\. Para isso é necessário obter a data fiscal da nota original da venda\. Isso é feito através das notas de referência informadas nas tabelas SAFX116 e SAFX117\.

__Sobre a Obtenção da nota original de venda:__

- As tabelas SAFX116/SAFX117 são vinculadas à capa da nota \(SAFX07\), e assim, não têm a informação do produto\. Elas têm apenas as informações de identificação do documento referenciado \(ou seja, a nota da SAFX07, ou o cupom da SAFX993\);
- Critérios para pesquisa dos documentos referenciados na SAFX116 / SAFX117 vinculados a nota fiscal de devolução:

            \- Campos 01 ao 11 = Campos de identificação da nota de devolução;

               Poderão ser recuperados ‘n’ registros de documentos referenciados \(notas e cupons\)\.

               Na __SAFX116__ as informações do documento referenciado constam nos campos 13 ao 21;

               Na __SAFX117__ as informações do cupom referenciado constam nos campos 13 ao 18;

            \- Serão considerados apenas os documentos referenciados recuperados da SAFX116/SAFX117, que tenham pelo menos um item do

              produto em questão\. Para verificar os itens do documento referenciado, é necessário pesquisar na SAFX08, ou na SAFX994, dependendo 

              se o documento referenciado é uma nota \(SAFX07\), ou um cupom \(SAFX993\); 

                            Para pesquisar os itens do documento fiscal referenciado \(SAFX116\) na SAFX08: 

__Campos da SAFX08__

__Campos da SAFX116__

01\-Código da Empresa

01\-Código da Empresa

02\-Código do Estabelecimento

02\-Código do Estabelecimento

03\-Data Fiscal

19\-Data de Emissão

*Obs\.: Como o doc de referência nesse caso será sempre uma venda \(uma saída\), então a data de emissão é a própria data fiscal\) *

04\-Movimento E/S 

16\-Movimento E/S

07\-Indicador da Pessoa Fis/Jur

17\-Indicador da Pessoa Fis/Jur

08\-Código da Pessoa Fis/Jur

18\-Código da Pessoa Fis/Jur

09\-Número do Documento Fiscal

13\-Número do Documento Fiscal

10\-Série do Documento Fiscal

14\-Série do Documento Fiscal

11\-Subsérie do Documento Fiscal

15\-Subsérie do Documento Fiscal

13\-Indicador do Produto

__Indicador do Produto em questão__

14\-Produto

__Código do Produto em questão__

                            Para pesquisar os itens do cupom fiscal referenciado \(SAFX117\) na SAFX994: 

__Campos da SAFX994__

__Campos da SAFX117__

01\-Código da Empresa

01\-Código da Empresa

02\-Código do Estabelecimento

02\-Código do Estabelecimento

03\-Modelo Documento 

04\-Número do Caixa

\(ID da X2087\_EQUIPAMENTO\_ECF\)

16\-Modelo de Documento

13\-Número do Caixa \(ECF\)

05\-COO \(Contador de Ordem de Operação\) 

14\-Número do Documento

06\-Data da Emissão

15\-Data de Emissão

08\-Indicador do Produto

__Indicador do Produto em questão__

09\-Código do Produto

__Código do Produto em questão__

Obs importante: A pesquisa dos itens do documento referenciado, é apenas para verificar se a nota ou cupom indicado na SAFX116/SAFX117 se referem, ou não, ao produto em questão\. Esta verificação é necessária pois pode existir uma nota de devolução, com vários itens diferentes, e cada um destes itens pode ter sido originado de notas de venda diferentes, de diferentes datas, e até mesmo diferentes períodos\. Como a questão aqui é identificar se a venda do produto foi realizada no antes da Data de Ingresso da Mercadoria no Regime ST, é importante acessar a nota de referência correta, ou seja, aquela referente ao produto em questão\. 

- Se a pesquisa dos documentos referenciados na SAFX116/SAFX117, conforme os critérios descritos acima, retornar apenas um documento, será verificado se a data de emissão deste documento \(campo “19\-Data de Emissão” da SAFX116, ou campo “15\-Data de Emissão” da SAFX117\) é anterior a Data do Ingresso da Mercadoria no Regime ST\. Caso sim, a nota de devolução será considerada, caso não, a nota será descartada, e assim, não será demonstrada no arquivo;

*           \(como estes documentos de referência são saídas, a data de emissão é a própria data fiscal da nota\) *

- Se a pesquisa dos documentos referenciados na SAFX116/SAFX117, conforme os critérios descritos acima, *retornar mais de um documento*, o procedimento será o seguinte: se ao menos um dos documentos de referência recuperados tiver a data de emissão anterior a Data do Ingresso da Mercadoria no Regime ST, a nota de devolução será considerada\. Caso contrário, a nota será descartada, e assim, *não* será demonstrada no arquivo;

*Obs\.: Não existe orientação na legislação em relação a este cenário, ou seja, uma devolução tendo como referência várias notas de venda do produto, realizadas em diferentes datas ou diferentes períodos\. No entanto, precisamos tratar este cenário de alguma forma, uma vez que as tabelas permitem ‘n’ documentos de referência associados a uma única nota da SAFX07\. *

- Se a pesquisa dos documentos referenciados na SAFX116/SAFX117, conforme os critérios descritos acima, *não retornar nada*, ou seja, não existir nenhuma nota de referência que atenda aos critérios, *a nota de devolução não será considerada na geração*, e será gravada a seguinte mensagem de erro no log:

*                “Nota de devolução de saída de mercadoria ingressada no Regime ST não considerada na geração, pois a nota da operação original da venda do produto não foi identificada\. Ver orientações no help sobre as devoluções”*

            No log serão demonstrados os dados de identificação da nota de devolução em questão, para que o usuário possa verificar o problema\. 

__Ordenação por:__

- Produto 
- Data Fiscal em ordem decrescente

__\[MFS35374\]__ Inclusão da recuperação do inventario 

__Passo 3 \- Recuperação do Inventário de Estoque por Produto \(SAFX52\): __

A partir de cada produto recuperado no __passo 1__, fazer uma consulta na Tabelas do Inventário por Produto, para recuperar o estoque do final do período\.

Os critérios são os seguintes:

- Código Empresa = código da empresa do login;
- Código Estabelecimento = código do estabelecimento selecionado para geração;

__\[MFS46838\] Tratamento para Perfil D:__

Caso o estabelecimento selecionado na tela de geração seja um estabelecimento __Centralizador__, recuperar os documentos fiscais do estabelecimento __Centralizador__ e dos seus estabelecimentos __Centralizados__, que foram a ele relacionados, na parametrização da “Centralização de Estabelecimentos p/ Perfil D”\.

Caso o estabelecimento selecionado na tela de geração seja um estabelecimento “__Não centralizado”__, recuperar os documentos fiscais apenas do estabelecimento selecionado para geração\.

- Data do Inventário – data do último dia do período da geração;
- Grupo de Contagem \- será considerado apenas o grupo de contagem = “1” \(Estoque Próprio, em Poder do Estabelecimento\);

Grupamento:

Os dados recuperados serão agrupados por:  

    \- Produto \(campos 6 e 7 da SAFX52\);

Campo totalizado para cada grupamento: 

    \- Quantidade \(campo 13 da SAFX52\);

O grupamento é necessário pois a chave da tabela do Inventário permite a existência de várias linhas de mesmo produto e grupo de contagem\. Isso porque na chave tem o campo “11\-Natureza do Estoque”, que permite diversas combinações com o mesmo produto\.

__Obs\.:__  Poderá não existir quantidade de estoque para um determinado produto na tabela de Inventário por Produto na data pesquisada, neste caso, a quantidade do inventário não será considerada para recuperar as notas fiscais de entrada\.

__Importante__:

A pesquisa das entradas é feita até atingir a quantidade total das saídas do período mais a quantidade final do inventário, conforme descrito nos Passos 1, 2 e 3\. Assim, a cada entrada pesquisada, verifica\-se se a quantidade total das saídas mais a quantidade final do inventário já foi ou não atingida, e se a pesquisa deve parar nessa nota, ou continuar\.  Com a nova regra sobre o tratamento das notas complementares, deve\-se observar que, ao utilizar o valor de cada entrada para fazer essa verificação, deve\-se considerar a quantidade da entrada em questão \+ suas notas complementares, caso existam\.

Assim, a pesquisa das entradas deve ser feita sempre a partir das notas “normais” \(não complementares e não eletrônicas de ajustes\), e para cada entrada a ser processada, será verificada a existência de notas complementares\. Caso existam, a quantidade a ser considerada será sempre a quantidade da entrada \+ suas notas complementares\.

__\[MFS58553\]__ Para Notas Eletrônicas de Ajuste \(campo “*125\-Situação Especial*” da capa = “E”\), tomar dois cuidados:

\- A nota de entrada original \(“normal”\) não terá sua quantidade subtraída pela quantidade da Nota Eletrônica de Ajuste que a referencia\. Isso porque, diferentemente das notas complementares, as notas de ajuste não deduzem a quantidade da nota original, apenas os campos 18 – Base de Cálculo ICMS\-ST e 23 – Valor ICMS\-ST\. 

\- A quantidade da Nota Fiscal Eletrônica de Ajuste NÃO pode ser considerada na totalização das quantidades das entradas usadas para atingir a quantidade das saídas \+ quantidade final do inventário\. Isso porque a Nota Fiscal Eletrônica de Ajuste *não será gerada na tabela dos movimentos*, ou seja, *não será gravada no registro 2130*\. 

__Exemplo__:

Supondo uma geração das entradas com o seguinte cenário:

   \- Mês da geração = __Junho__;

   \- Total da Quantidade das Saídas do Período: __1\.200,000__ 

   \- Notas fiscais de entrada do produto = ver quadro abaixo;

__Março__

__Abril__

__Maio__

__Junho__

Nota

Quantidade

Nota

Quantidade

Nota

Quantidade

Nota

Quantidade

__1__

50,000

__4 __

__\(Ajuste da nf 3\)__

45,000

__7__

10,000

__12__

100,000

__2__

__200,000__

__5__

80,000

__8__

30,000

__13__

50,000

__3__

85,000

__6__

120,000

__9__

150,000

__14__

200,000

__10__

50,000

__15 __

__\(Compl\. da nf 12\)__

30,000

__11__

__ \(Compl da nf 6\)__

100,000

__16 __

__\(Ajuste da nf 12\)__

10,00

Para atingir a quantidade total das saídas \(1\.200,000\), a pesquisa usará as entradas “*normais*”, sempre considerando a quantidade de seus complementos, caso existam\. As notas fiscais eletrônicas de ajuste serão desconsideradas\. Veja:

__                    Nota de entrada \[Registro 2130\]         QTD \[QTD nota \+ QTD notas complementares\]       QTD Acumulada__

__                    = = = = = = = = = = = = = = = = = =         = = = = = = = = = = = = = = = = = = = = = = = = =          = = = = = = = = =__

                                          NF 14                                          200,000                                                                     200,00

                                          NF 13                                            50,000                                                                    250,000       

                                          NF 12                                 130,000 \[100,000 \+ 30,000 da __NF 15__\]                              380,000

                                          NF 10                                            50,000                                                                    430,000       

                                          NF 9                                            150,000                                                                    580,000       

                                          NF 8                                              30,000                                                                    610,000       

                                          NF 7                                              10,000                                                                    620,000

                                          NF 6                                   220,000 \[120,000 \+ 100,000 da __NF 11__\]                            840,000       

                                          NF 5                                              80,000                                                                    920,000       

                                          NF 3                                              85,000                                                                 1\.005,000       

                                          NF 2                                            200,000                                                                 1\.205,000

Observar que nesse cenário a pesquisa se encerra na NF 2, exatamente quando a quantidade acumulada atingiu a quantidade total das saídas\.

Observar também que a pesquisa utiliza as notas “normais”, e para cada uma, verifica a existência de notas complementares\.

__Obs1__\.: Deve ser prevista a possibilidade de existir mais de uma nota complementar para o mesmo item de nota original\.

__Obs2__\.: A referência da nota da operação original que foi complementada é obtida no item da nota complementar \(SAFX08\), através dos campos 102 \(Data\), 117, 118 e 119 \(Número, Série e Subsérie do documento\)\. Observar que não existe campo para indicar o item da nota original a ser complementado, por isso, esta informação é obtida através do produto\. Assim, a regra é considerar o item da nota original de mesmo produto do item da nota complementar\. Observar que esta solução prevê que na nota original não existirá mais de um item de mesmo produto\. Caso este cenário venha a acontecer, a solução deverá ser revista, e uma possível solução seria utilizar a SAFX192 para fazer este cruzamento \(item da nota complementar x item da nota original\)\. Consultamos a Informação sobre isso, e a orientação é não se preocupar com isso \(a princípio\), conforme e\-mail anexo no Jira\. 

__\[MFS58553\]__ As obs1 e obs2 também se aplicam às Notas Eletrônicas de Ajuste \(campo “*125\-Situação Especial*” da capa = “E”\)\.

\[__MFS684912__\] Inclusão do estoque no Ingresso das Mercadorias no Regime de Substituição Tributária, e das notas de entrada por devolução de mercadoria cuja saída tenha ocorrido antes da data do seu ingresso no regime de substituição tributária, a serem somados à quantidade das notas de entradas recuperadas até cobrir a quantidade da saída e estoque final do inventário do produto\. Base legal: Notas 8 e 9 do registro 2130 da Portaria SEF 378\.

__\[MFS591077\] Tratamento das Incorporações de Empresas/Estabelecimentos:__

Quando acontecer da data limite ser alcançada, sem que a quantidade apurada nas entradas e nas notas complementares seja suficiente para atingir a quantidade total das saídas mais a quantidade final do inventário, verificar se o parâmetro para buscar as notas nas empresas incorporadas está marcado na tela da geração\. 

     Se o parâmetro “Considerar as notas fiscais da empresa incorporada” estiver marcado:

          Considerar as notas e Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária \(passo 2\.1\) das empresas/estabelecimentos cadastradas como incorporadas na tela de Relação 

          de Empresa Incorporadora x Incorporada\*\* para a empresa/estabelecimento da geração \(incorporadora\), para recuperar as notas de entrada afim de atingir a quantidade da saída do produto\.

    Senão

          Considerar somente as notas fiscais da empresa e estabelecimento selecionados para a geração\.         

\*\* Módulo Parâmetros, item Preliminares à Relação de Empresa Incorporadora x Incorporada

__Obs__\.: Não estamos tratando o cenário de Cadastros de Produtos distintos entre as empresas incorporadora e incorporadas\. Ou seja, os produtos entre essas empresas devem ser identificados pelo mesmo grupo, indicador e código do produto\.  A Lasa que foi o cliente que abriu essa demanda, possui cadastros iguais entre as empresas participantes da incorporação\. Se os cadastros fossem diferentes, teríamos que criar uma espécie de dexpara entre os cadastros dos produtos da empresa incorporadora para com os das empresas incorporadas\.

__\[MFS35374\]__ Inclusão da verificação da quantidade final do inventário

\[__MFS684912__\] Inclusão do estoque no Ingresso das Mercadorias no Regime de Substituição Tributária, e das notas de entrada por devolução de mercadoria cuja saída tenha ocorrido antes da Data do seu Ingresso no Regime de Substituição Tributária, a serem somados à quantidade das notas de entradas recuperadas até cobrir a quantidade da saída e estoque final do inventário do produto\. Base legal: Notas 8 e 9 do registro 2130 da Portaria SEF 378\.

__Passo 4 \- Processamento e Gravação das Notas Fiscais de Entrada e Devolução de Entradas:__

Para cada produto processar as notas fiscais de entrada \(e devoluções das entradas\) \(vide passo 2\), o Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária \(vide passo 2\.1\) e as notas de entrada por devolução de mercadoria cuja saída tenha ocorrido antes da Data do seu Ingresso no Regime de Substituição Tributária \(vide passo 2\.2\), em ordem decrescente de data, até que esta quantidade \(entradas e devoluções das entradas, mais estoque e devolução de saída\), cubra a quantidade total de saída do produto mais a quantidade final do inventário, calculada no passo 1 e no passo 3\. 

Executar os seguintes passos:

1. Converter a quantidade lida do item de mercadoria, considerando como origem a unidade de medida do item e destino a unidade de medida do Cadastro do Produto \(safx2013\)\.

Veja explicação sobre a regra de conversão da quantidade no campo “[Quantidade Convertida](#OLE_LINK22)”, no tópico

 [4 \- Gravação dos Dados na Tabela dos Movimentos \(origem = SAFX07/SAFX08\)](#_Gravação_dos_Dados),\.

1. Acumular a Quantidade Convertida do item da nota, somando o movimento de entrada e subtraindo a devolução:

Se a nota de entrada \(*MOVTO\_E\_S <> 9 da SAFX07*\), então:                                          \(recuperada no passo 2 e 2\.2\),

Somar a quantidade convertida do item à “Qtde Convertida Total Entrada”\.

Se a nota de saída \(*MOVTO\_E\_S = 9 da SAFX07*\), então:                                               \(recuperada no passo 2\)

Subtrair a quantidade convertida do item da “Qtde Convertida Total Entrada”\.

	

1. Acumular a Quantidade do Estoque no Ingresso da Mercadoria no Regime ST \(recuperada no passo 2\.1\) somando à “Qtde Convertida Total Entrada”\. \(não há conversão de unidades de medida\)\.
2. Avaliar se “Qtde Convertida Total Entrada” atingiu a “[Qtde Convertida Total Saída](#OLE_LINK2)” mais a quantidade final do inventário\.

Se “Qtde Convertida Total Entrada” __> =__ “Qtde Convertida Total Saída” \+ quantidade final do inventário então:

Interromper o processo de busca das notas de entrada \(e devolução\) para um produto\.

Gravar as notas na tabela, como descrito no tópico [4 \- Gravação dos Dados na Tabela dos Movimentos \(origem = SAFX07/SAFX08\)](#_Gravação_dos_Dados)\.

# <a id="_Gravação_dos_Dados"></a><a id="_Toc206180302"></a>Gravação dos Dados na Tabela dos Movimentos \(origem = SAFX07/SAFX08\) 

<a id="_Hlk508706613"></a>

Os documentos fiscais de entrada \(e devolução\) recuperados da SAX07 / SAFX08 __serão gravados na tabela item a item__, na Tabela dos Movimentos \(EST\_ST\_SC\_NF\) do módulo Ressarcimento e Complemento do ICMS\-ST – SC, que é utilizada posteriormente em diversas funcionalidades do módulo\. 

Os campos sinalizados com asterisco compõem a chave da tabela\.

__EST\_ST\_SC\_NF:__

__\*\*\*__

__Código da empresa__

Código da empresa \(SAFX07\)

__\*\*\*__

__Código do estabelecimento__

__\[MFS46838\] Tratamento para Perfil D:__

Código do estabelecimento \(SAFX07\) 

Preencher com o estabelecimento selecionado na tela de geração

__\*\*\*__

__Código do estabelecimento de origem__

Código do estabelecimento de origem do documento \(SAFX07\)

 

Obs\.: Este campo foi criado na tabela por causa da geração por inscrição estadual única, que será desenvolvida posteriormente\. A princípio, o módulo será desenvolvido sem esta opção, e assim, este campo será gravado com o mesmo conteúdo do anterior;

__\[MFS46838\] Tratamento para Perfil D:__

Com o tratamento do Perfil D, onde os documentos fiscais são recuperados dos estabelecimentos __Centralizador__ e __Centralizados__, este campo passa a ser gravado com o estabelecimento presente na nota fiscal\.

__\*\*\*__

__Período \(mês e ano\)__

Período da geração informado em tela

\(último dia do mês/ano informado\)

__\*\*\*__

__Produto__

Produto referente ao item da nota \(campos 13 e 14 da SAFX08\)\.

Quando se tratar de um produto “associado”, a informação gravada neste campo será o produto principal da parametrização \(lembrando que toda a movimentação dos associados é demonstrada na obrigação em nome do produto principal\)\.

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Preencher com o “Produto” da Parametrização das Mercadorias Ingressadas no Regime ST\. 

             Também se aplica o tratamento de produto associado descrito acima\. 

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

             Preencher com o “Produto” do item da nota \(campos 13 e 14 da SAFX08\)\. 

             Também se aplica o tratamento de produto associado descrito acima\. 

__\*\*\*__

__Data Fiscal 	__

Data fiscal do documento \(SAFX07\)

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Não preencher

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

             Preencher com Data Fiscal \(SAFX07\)\. 

__\*\*\*__

__Tipo do Documento__

Tipo do Documento \(campo “05\-Tipo do Documento” da SAFX07\)

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Não preencher

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

             Preencher com Tipo do Documento \(campo “05\-Tipo do Documento” SAFX07\)\. 

__\*\*\*__

__Série do Documento__

Série do documento fiscal \(campo “09\-Série do Documento” da SAFX07\)

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Não preencher

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

             Preencher com Série do documento fiscal \(campo “09\-Série do Documento” da SAFX07\)\. 

__\*\*\*__

__Número do Documento__

Número do documento fiscal \(campo “08\-Número do Documento” da SAFX07\)

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Não preencher

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

             Preencher com Número do documento fiscal \(campo “08\-Número do Documento” da SAFX07\)\. 

__\*\*\*__

__Pessoa Fis/Jur__

Pessoa fis/jur do documento fiscal \(campos 06 e 07 da SAFX07\)

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Não preencher

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

             Preencher com Pessoa fis/jur do documento fiscal \(campos 06 e 07 da SAFX07\)\. 

__\*\*\*__

__Número do Item__

*\(campo 07 – NUM\_ITEM reg 2130\)*

Número do item do documento fiscal \(campo “18\-Item Nota Fiscal” da SAFX08\)

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Não preencher

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

             Preencher com Número do item do documento fiscal \(campo “18\-Item Nota Fiscal” da SAFX08\)\. 

__\*\*\*__

__Movimento E/S__

Indicador do movimento \(campo “03\-Movimento Entrada/Saída” da SAFX07\)

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

            Preencher fixo com “0”\. 

            Deve ser preenchido com <> 9, para que no relatório de conferência, o registro ser somado às Entradas\.

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

             Preencher com Indicador do movimento \(campo “03\-Movimento Entrada/Saída” da SAFX07\) 

Modelo de Documento

Modelo do Documento fiscal \(campo “13\-Modelo de Documento” da SAFX07\)

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Não preencher

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

             Preencher com Modelo do Documento fiscal \(campo “13\-Modelo de Documento” da SAFX07\) 

Indicador do Tipo de Registro

Nesta geração das entradas e devoluções de entradas, este campo será preenchido com “__2130__”\.

Indicador do Tipo de Saída 

Não preencher\.

Chave Documento Fiscal Eletrônico 

*\(campo 03 – CHV\_NFE reg 2130\)*

Chave do documento fiscal eletrônico \(campo 226\-Chave de Acesso da NF\-Eletrônica, SAFX07\)

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Não preencher

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

             Preencher com Chave do documento fiscal eletrônico \(campo 226\-Chave de Acesso da NF\-Eletrônica, SAFX07\)

Data Emissão

*\(campo 05 – DT\_NFE reg 2130\)*

Data de emissão do documento \(campo 11\-Data de Emissão da SAFX07\)

<a id="OLE_LINK16"></a><a id="OLE_LINK19"></a>Alteração MFS30185: Este campo será sempre preenchido na tabela, independente da condição da nota\. As regras específicas do registro 2130 serão tratadas na geração do arquivo\. 

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Não preencher

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

             Preencher com Data de emissão do documento \(campo 11\-Data de Emissão da SAFX07\)\.

Data Entrada

*\(campo 04 – DT\_E reg 2130\)*

Alteração MFS30185: Este campo será sempre preenchido na tabela, independente da condição da nota\. As regras específicas do registro 2130 serão tratadas na geração do arquivo\. 

A geração deste campo segue a regra abaixo:

Se nota de entrada \(MOVTO\_E\_S <> 9 da SAFX07\), então:

Preencher com a Data de saída/recebimento \(campo 20\-Data Saída/Recebimento da SAFX07\)\.

Senão \(são as notas de saída das devoluções de entrada\)

Não preencher\.

Data de saída/recebimento \(campo 20\-Data Saída/Recebimento da SAFX07\)

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Não preencher

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

             Preencher com Data de saída/recebimento \(campo 20\-Data Saída/Recebimento da SAFX07\)\.

Nota de Devolução \(ind\_nota\_devol\)

*\(campo 02 – IND\_OPER reg 2130\)*

A geração deste campo segue a regra abaixo:

Se nota de entrada \(MOVTO\_E\_S <> 9 da SAFX07\), então:

Preencher com “0” \- Entrada \(Aquisição\);

Senão \(são as notas de saída das devoluções de entrada\)

Preencher com “1” \- Devolução de aquisições;

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Preencher fixo com “2” \- ICMS Estoque Ingresso na ST\.

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

             Preencher fixo com “0” \- Entrada

CFOP

*\(campo 14 – CFOP reg 2130\)*

CFOP do item do documento fiscal \(campo “22\-Código Fiscal” da SAFX08\)

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Não preencher

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

             Preencher com CFOP do item do documento fiscal \(campo “22\-Código Fiscal” da SAFX08\)\.

Quantidade da Nota

*\(campo 09 – QTDE reg 2130\)*

Quantidade do item \(campo “24\-Quantidade” da SAFX08\)

__\+__

Quantidade do item da nota complementar \(campo “24\-Quantidade” da SAFX08\)

__MFS30185__: Quando existir nota complementar para a nota de entrada em questão, conforme descrito na regra de recuperação dos dados \(ver nota “*Sobre as Notas Complementares*”\), a quantidade da nota complementar será somada à quantidade da nota original\.

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Preencher com ZERO\.

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

             Preencher com Quantidade do item \(campo “24\-Quantidade” da SAFX08\)\.

Unidade de Medida

Unidade de medida do item \(campo “17\-Unidade Padrão” da SAFX08\)

*Observação:*

*Esta informação é gravada na coluna *__*COD\_UND\_PADRAO\_ITEM*__* da tabela dos movimentos\.*

*Além desta coluna, a geração dos movimentos também armazena a informação de outras unidades, como a do campo 25\-Unidade de Medida, que é utilizada na conversão de medida, que é a coluna *__*COD\_MEDIDA\_ITEM*__*\.*

*\(No campo 10 do registro 2130 é gravada a unidade do campo 25 do item, que é a unidade da SAFX2007\)*

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Preencher com Campo “14\-Código de Medida” da SAFX2013\.

              Mesma regra do campo “UNID\_INV” do registro 0200 

              Ver MTZ\-Ressarc\-SC\-Geracao\-do\-Meio\-Magnetico\-Bloco0\.docx

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

             Preencher com Unidade de medida do item \(campo “17\-Unidade Padrão” da SAFX08\)\.

Fator de Conversão

*\(campo 11 – FAT\_CONV reg 2130\)*

Fator de conversão da unidade utilizada na nota para a unidade de inventário do produto\.

Para gerar este campo, é necessário verificar se na nota \(SAFX08\) foi utilizada a mesma unidade de medida do cadastro do produto \(unidade demonstrada no registro 0200\), e caso não, obter o fator de conversão\.

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\) __

      __\(\*\)__ unidade da nota = campo “25\-Unidade de Medida” da SAFX08

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso o campo será preenchido com o número 1;

__Senão __

      __\[MFS68852\] Tratamento do campo 137 – Quantidade Convertida da SAFX08__

      Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\), então:

         Nesse caso, será utilizada a informação da quantidade já convertida do campo “137\-Quantidade

         Convertida” para calcular o fator de conversão:

         Fator de Conversão = \[137 \- Quantidade Convertida / 24 \- Quantidade do Item \]

         \[__MFS78891\] Inclusão do Produto na tabela EST\_ST\_SC\_CONV\_MEDIDA:__

         Armazenar na tabela EST\_ST\_SC\_CONV\_MEDIDA __\(\*\)__, o Produto, a medida origem \(item da nota\), a

         medida destino \(produto\) e o fator de conversão calculado\.

         Só pode existir um fator de conversão para uma determinada combinação de Produto, medida origem 

         e destino\.

         Dado o Produto, a medida origem \(nota\) e destino \(produto\) em questão, caso o fator de conversão

         calculado, seja diferente de um fator calculado anteriormente, que já esteja gravado na tabela 

         EST\_ST\_SC\_CONV\_MEDIDA, então a nota será desconsiderada do resultado da geração, ou seja,

         não será gravada na tabela de movimento e no log, será gerada a seguinte mensagem de erro:

        “*Fator de conversão de medida de XXX para XXX é ZZZ\. Quantidade Convertida do item de mercadoria do*

*        documento fiscal não confere com a multiplicação da Quantidade pelo Fator de Conversão\.  Favor rever *

*        o documento, pois o mesmo foi desconsiderado pela geração”\.*

*       *\(o primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

       \(o log deve demonstrar as informações necessárias para permitir a identificação do item do documento,

       exibindo o número do documento, a data, o número do item, etc \.\.\.\)

       __\(\*\)__ Tabela utilizada na geração do registro 0220 no meio magnético, contendo todos os fatores de conversão

        de medida calculados com base no campo 137 da SAFX08\.

      Senão

Nesse caso o campo será preenchido com o fator de conversão obtido nas tabelas de conversão de

medida, conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do

Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

       \- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

       \- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o item da nota será gerado com o campo FATOR DE CONVERSÃO sem informação, e será gravada a seguinte mensagem de erro no log: “*Fator de conversão de medida de XXX para XXX não encontrado\. O item do documento será gerado sem esta informação”\. *\(o primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

 \(o log deve demonstrar as informações necessárias para permitir a identificação do item do documento,

  exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

__Observações importantes:__

__\- Sobre a comparação das unidades de medida:__

A comparação das unidades \(nota x cadastro\) é feita a partir dos campos referentes à unidade da SAFX2007, porque as tabelas de conversão de medida do Mastersaf usam esta medida\. Já na geração dos registros 0200 e do 2130, a medida utilizada é a do campo da unidade padrão \(SAFX2017\), cujo código é maior\. \(A unidade de medida da SAFX2007 tem apenas 3 posições\)\. Desta forma, a geração prevê que as duas unidades estejam sempre preenchidas, tanto no cadastro do produto como nas notas, e naturalmente, que sejam sempre as mesmas \(unidade de medida informada seja a mesma da unidade padrão\)\.

	

__\- Sobre os produtos associados:__

Quando se tratar de uma nota fiscal de produto “associado”, a comparação das unidades será feita da unidade de medida da nota, com a unidade do produto principal\.

Exemplo:

Produto principal: COCA\-COLA PET           \(unidade de medida do estoque – SAFX2013 = UN\) 

Produto associado: COCA\-COLA PET–1    \(unidade de medida do estoque – SAFX2013 = PAC \(6 unidades\)\)

Nota de compra do produto associado: COCA\-COLA PET\-1, unidade da nota = PAC, Quantidade = 5

Neste caso a comparação será feita entre a unidade de medida da nota do produto associado com a unidade de estoque do produto principal: PAC x UM

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Preencher com ZERO\.

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

            Preencher conforme regra descrita acima que trata as notas de entradas normais e devoluções\.

<a id="OLE_LINK22"></a>Quantidade Convertida

*\(campo 12– QTDE\_C reg 2130\)*

__Se__ o “Fator de Conversão” gerado no campo anterior = 1, então:

      Nesse caso este campo será preenchido com a mesma quantidade gerada no campo “Quantidade da Nota”;

__Senão __

      __\[MFS68852\] Tratamento do campo 137 – Quantidade Convertida da SAFX08__

      Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\), então:

         Nesse caso, será utilizada a informação da quantidade já convertida do campo “137\-Quantidade

         Convertida”;

      Senão

         Se o “Fator de Conversão” gerado no campo anterior não estiver preenchido:

Preencher este campo com zero\.

         Senão:

Nesse caso o campo será preenchido com a quantidade do item \(SAFX08\) convertida para a unidade de medida do cadastro do produto, utilizando o fator de conversão obtido\. Assim, será a multiplicação dos seguintes campos gerados acima:

              

                                          \[ Quantidade da Nota \* Fator de Conversão \]

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Preencher com o campo “Quantidade” da Parametrização das Mercadorias Ingressadas no Regime ST\.

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

            Preencher conforme regra descrita acima que trata as notas de entradas normais e devoluções\.

     

Valor da Entrada

*\(campo 13– VL\_E reg 2130\)*

Campo “64\-Valor Contábil do Item” da SAFX08

__\+__

Campo “64\-Valor Contábil do Item” da SAFX08 do item da nota complementar

__MFS30185__: Quando existir nota complementar para a nota de entrada em questão, conforme descrito na regra de recuperação dos dados \(ver nota “*Sobre as Notas Complementares*”\), o valor da nota complementar será somado ao valor da nota original\.

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Preencher com o campo “Valor Total” da Parametrização das Mercadorias Ingressadas no Regime ST\.

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

             Preencher com Campo “64\-Valor Contábil do Item” da SAFX08\.

<a id="OLE_LINK5"></a>Código Responsável Retenção

*\(campo 08 – COD\_RESP\_RET reg 2130\)*

Código que indica o responsável pela retenção do ICMS\-ST\.

__Orientação da Portaria SEF 378/2018 \(PeSEF de 03\.12\.18\):__

”Campo 08 \(COD\_RESP\_RET\) \- Preenchimento: campo preenchido somente 

para indicador do tipo de operação \(IND\_OPER= código 0\)\.”

A geração deste campo segue a regra abaixo:

__Se__ o campo “Nota de Devolução” gerado para este registro = “0” \- Entrada \(Aquisição\), então:

Aplicar a regra [5\.1 – Regra de Definição do Responsável pela Retenção](#OLE_LINK10)\.

__Senão__:

Não Preencher\.

__Validação:__

Caso o código resultante da regra 5\.1 seja nulo, gerar mensagem no log e continuar o processamento:

*“Responsável pela Retenção não definido no documento fiscal\. Por consequencia, valores de Base, Alíquota e imposto de ICMS e ICMS\-ST serão gerados sem preenchimento\. Favor rever campos Situação Especial ST e Indicador de ICMS\-ST do Item do Documento Fiscal\.”* 

O log deve demonstrar as informações necessárias para permitir a identificação do Item do documento fiscal: Estabelecimento, Data fiscal, Número do Documento, Pessoa fis/jur, Número do Item de Mercadoria\.

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Preencher fixo com “3” – Próprio Declarante\.

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

             Preencher fixo com “3” – Próprio Declarante

<a id="OLE_LINK3"></a>Base de Cálculo do ICMS

*\(campo 15 – VL\_BC\_ICMS reg 2130\)*

Vide regra [5\.2 \- Preenchimento dos Campos Base de Cálculo do ICMS, Alíquota ICMS e Valor ICMS \(15 \- VL\_BASE\_ICMS ,16 \- ALIQ\_ICMS e 17 \- VL\_ICMS\)](#OLE_LINK11)

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Preencher com ZERO\.

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

            Preencher conforme regra descrita acima que trata as notas de entradas normais e devoluções\.

Alíquota ICMS

*\(campo 16 – ALIQ\_ICMS reg 2130\)*

Vide regra [5\.2 \- Preenchimento dos Campos Base de Cálculo do ICMS, Alíquota ICMS e Valor ICMS \(15 \- VL\_BASE\_ICMS ,16 \- ALIQ\_ICMS e 17 \- VL\_ICMS\)](#OLE_LINK11)

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Preencher com ZERO\.

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

            Preencher conforme regra descrita acima que trata as notas de entradas normais e devoluções\.

Valor ICMS

*\(campo 17 – VL\_ICMS reg 2130\)*

Vide regra [5\.2 \- Preenchimento dos Campos Base de Cálculo do ICMS, Alíquota ICMS e Valor ICMS \(15 \- VL\_BASE\_ICMS ,16 \- ALIQ\_ICMS e 17 \- VL\_ICMS\)](#OLE_LINK11)

Ver crítica de campo no tópico [6 \- Geração de Críticas no Log da Geração](#_Geração_de_Críticas_1) – regra [6\.7](#_6.7_-_Critica)

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Preencher com ZERO\.

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

            Preencher conforme regra descrita acima que trata as notas de entradas normais e devoluções\.

<a id="OLE_LINK6"></a>Base de Cálculo ICMS\-ST Pago

*\(campo 18 – VL\_BCST reg 2130\)*

Vide regra [5\.3 \- Preenchimento dos Campos Base de Cálculo ICMS\-ST Pago e Integral e Alíquotas ST Pago e Efetiva\(campos 18, 19, 20 e 21\)](#OLE_LINK15)

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Preencher com ZERO\.

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

            Preencher conforme regra descrita acima que trata as notas de entradas normais e devoluções\.

<a id="OLE_LINK7"></a>Base de Cálculo ICMS\-ST Integral

*\(campo 19 – VL\_BCST\_INT reg 2130\)*

Vide regra [5\.3 \- Preenchimento dos Campos Base de Cálculo ICMS\-ST Pago e Integral e Alíquotas ST Pago e Efetiva\(campos 18, 19, 20 e 21\)](#OLE_LINK15)

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Preencher com o campo “Valor Base ICMS\-ST” da Parametrização das Mercadorias Ingressadas no Regime ST\.

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

            Preencher conforme regra descrita acima que trata as notas de entradas normais e devoluções\.

<a id="OLE_LINK8"></a>Alíquota ICMS\-ST Pago

*\(campo 20 – ALIQ\_ST\_E reg 2130\)*

Vide regra [5\.3 \- Preenchimento dos Campos Base de Cálculo ICMS\-ST Pago e Integral e Alíquotas ST Pago e Efetiva\(campos 18, 19, 20 e 21\)](#OLE_LINK15)

Se a “Alíquota Interna” recuperada da Parametrização do Produto, não estiver preenchida, exibir a seguinte mensagem no log e continuar o processamento:

*“Campo Alíquota ICMS\-ST Pago foi gerado sem informação\. *

*Favor informar a Alíquota Interna na Parametrização do Produto relacionado ao Item do Documento Fiscal\.”* 

O log deve demonstrar o Código do Produto e informações necessárias para permitir a identificação do Item do documento fiscal: Estabelecimento, Data fiscal, Número do Documento, Pessoa fis/jur, Número do Item de Mercadoria\.

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Preencher com ZERO\.

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

            Preencher conforme regra descrita acima que trata as notas de entradas normais e devoluções\.

<a id="OLE_LINK9"></a>Alíquota ICMS\-ST Efetiva

*\(campo 21 – ALIQ\_ST\_EF reg 2130\)*

Vide regra [5\.3 \- Preenchimento dos Campos Base de Cálculo ICMS\-ST Pago e Integral e Alíquotas ST Pago e Efetiva\(campos 18, 19, 20 e 21\)](#OLE_LINK15)

*\(mesma regra do campo “ALIQ\_ICMS” do registro 0200 do Ressarcimento SC\)*

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Preencher conforme regra do campo “ALIQ\_ICMS” do registro 0200\.

             Ver MTZ\-Ressarc\-SC\-Geracao\-do\-Meio\-Magnetico\-Bloco0\.docx

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

             Preencher conforme regra do campo “ALIQ\_ICMS” do registro 0200\.

             Ver MTZ\-Ressarc\-SC\-Geracao\-do\-Meio\-Magnetico\-Bloco0\.docx

<a id="OLE_LINK32"></a>Valor ICMS\-ST calculado

*\(campo 22 – CALC\_ICMS\_ST reg 2130\)*

Se campo “__Código Responsável pela Retenção__” \(conforme regra [5\.1](#OLE_LINK10)\) for nulo então

Não Preencher\.

Senão:

Preencher com: “[*Base de Cálculo ICMS\-ST Pago*](#OLE_LINK6)” \* “[*Alíquota ICMS\-ST Pago*](#OLE_LINK8)” /100

__Truncar o valor resultante da expressão acima, de acordo com o número de casas do campo\.__

__Validação:__

Se “[*Base de Cálculo ICMS\-ST Pago*](#OLE_LINK6)” \* “[*Alíquota ICMS\-ST Pago*](#OLE_LINK8)” <> 

      “*Base de Cálculo ICMS\-ST Integral*” \* “*Alíquota ICMS\-ST Efetiva*”, então:

Exibir a seguinte mensagem no log e continuar o processamento:

*“O resultado da multiplicação dos campos Base ICMS\-ST Pago e Alíquota ICMS\-ST Pago está diferente da multiplicação dos campos Base ICMS\-ST Integral e Alíquota ICMS\-ST Efetiva\.*

*Favor rever campos de Base ICMS\-ST do Item do Documento Fiscal e Alíquota Interna e Percentual de Redução da Base de Cálculo da Parametrização do Produto\.”* 

O log deve demonstrar as informações necessárias para permitir a identificação do Item do documento fiscal: Estabelecimento, Data fiscal, Número do Documento, Pessoa fis/jur, Número do Item de Mercadoria\.

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Preencher com ZERO\.

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

            Preencher conforme regra descrita acima que trata as notas de entradas normais e devoluções\.

<a id="OLE_LINK4"></a>Valor ICMS\-ST 

*\(campo 23 – VL\_ICMS\_ST reg 2130\)*

Vide regra [5\.4 \- Preenchimento do Campo Valor ICMS\-ST \(23 – VL\_ICMS\_ST\)](#OLE_LINK18)

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Preencher com o campo “Valor ICMS\-ST” da Parametrização das Mercadorias Ingressadas no Regime ST\.

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

            Preencher conforme regra descrita acima que trata as notas de entradas normais e devoluções\.

Modelo do Documento de Arrecadação

*\(campo 24 – COD\_DA reg 2130\)*

A geração deste campo segue a regra abaixo:

Se o campo “Nota de Devolução” gerado para este registro = “0” \- Entrada \(Aquisição\), então:

Se campo “Código Responsável Retenção” gerado para este registro __<>__ “2” \- Remetente Indireto, então

Preencher com o campo “235\-Código do Modelo do Documento de Arrecadação” da SAFX08\.

Senão

Não Preencher\.

Senão \(“1” \- Devolução de aquisições\)

Não preencher\.

__Validação:__

Se campo “Nota de Devolução” gerado para este registro = “0” \- Entrada \(Aquisição\) e 

     campo “Código Responsável Retenção” gerado para este registro __=__ “3” – Próprio Declarante, então:

     Se campo “235\-Código do Modelo do Documento de Arrecadação” da SAFX08 não estiver preenchido então:

Exibir a seguinte mensagem no log e continuar o processamento:

*“Campo Modelo do Documento de Arrecadação foi gerado sem informação\. *

*Favor rever o preenchimento deste campo no Item do Documento Fiscal\.”* 

O log deve demonstrar as informações necessárias para permitir a identificação do Item do documento fiscal: Estabelecimento, Data fiscal, Número do Documento, Pessoa fis/jur, Número do Item de Mercadoria\.

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Preencher fixo com “2” – DISE

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

             Preencher com o campo “235\-Código do Modelo do Documento de Arrecadação” da SAFX08\.

Número do Documento de Arrecadação

*\(campo 25 – NUM\_DARE reg 2130\)*

A geração deste campo segue a regra abaixo:

Se o campo “Nota de Devolução” gerado para este registro = “0” \- Entrada \(Aquisição\), então:

Se campo “Código Responsável Retenção” gerado para este registro __<>__ “2” \- Remetente Indireto então:

Se campo “Modelo do Documento de Arrecadação” gerado nesse registro = “0” – DARE, então:

Preencher com o campo “236\-Número do Documento de Arrecadação” da SAFX08\.

Senão:

Não Preencher\.

Senão

Não Preencher\.

Senão \(“1” \- Devolução de aquisições\)

Não preencher\.

__Validação:__

Se campo “Nota de Devolução” gerado para este registro = “0” \- Entrada \(Aquisição\) e 

     campo “Código Responsável Retenção” gerado para este registro __<>__ “2” \- Remetente Indireto e

     campo “Modelo do Documento de Arrecadação” gerado nesse registro = “0” – DARE, então:

     Se campo “236\-Número do Documento de Arrecadação” da SAFX08 não estiver preenchido então:

Exibir a seguinte mensagem no log e continuar o processamento:

*“Campo Número do Documento de Arrecadação foi gerado sem informação\. *

*Favor rever o preenchimento deste campo no Item do Documento Fiscal\.”* 

O log deve demonstrar as informações necessárias para permitir a identificação do Item do documento fiscal: Estabelecimento, Data fiscal, Número do Documento, Pessoa fis/jur, Número do Item de Mercadoria\.

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Preencher com o campo “Número da DISE” da Parametrização das Mercadorias Ingressadas no Regime ST

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

            Se campo “Modelo do Documento de Arrecadação” gerado nesse registro = “0” – DARE, então:

                    Preencher com o campo “236\-Número do Documento de Arrecadação” da SAFX08\.

            Senão:

                    Não Preencher\.

Código de Ajuste do Sped Fiscal \(C197\) 

*\(campo 26\- – NUM\_DARE reg 2130\)*

A geração deste campo segue a regra abaixo:

Se o campo “Nota de Devolução” gerado para este registro = “0” \- Entrada \(Aquisição\) e 

     o campo “Código Responsável Retenção” gerado para este registro __=__ “3” – Próprio Declarante, então:

Consultar a tabela “Ajuste/Outros Valores do Lançamento Fiscal” \(SAFX113\) com os critérios:

- Campos Chave de Identificação da Capa do Documento Fiscal;
- Registro do Ajuste com mesmo Número do Item que está no Item de Mercadoria, ou com o campo Número do Item nulo;
- Código do Ajuste = “SC71000001”\.

Se a consulta retornar algum registro, então:

Preencher o campo com “SC71000001”\.

Senão 

Não Preencher

Senão \(“1” \- Devolução de aquisições\)

Não preencher\.

Validação:

Se campo “Nota de Devolução” gerado para este registro = “0” \- Entrada \(Aquisição\) e 

     campo “Código Responsável Retenção” gerado para este registro __=__ “3” – Próprio Declarante, então:

     Se campo “Código de Ajuste do Sped Fiscal” gerado para este registro não estiver preenchido então:

Exigir a seguinte mensagem no log e continuar o processamento:

*“Campo Código de Ajuste do Sped Fiscal \(C197\) foi gerado sem informação\. *

*Favor adicionar registro de Ajuste/Outros Valores de Lançamento Fiscal \(SAFX113\) relacionado ao Item do Documento Fiscal, para o Código de Ajuste SC71000001\.”* 

O log deve demonstrar as informações necessárias para permitir a identificação do Item do documento fiscal: Estabelecimento, Data fiscal, Número do Documento, Pessoa fis/jur, Número do Item de Mercadoria\.

Observação:

Estamos considerando apenas o Código de Ajuste SC71000001, que é o código utilizado pelo cliente Magazine Luíza\. Nada impede que alteremos a regra para aceitar outros códigos que representem o pagamento do ICMS\-ST na entrada da mercadoria pelo declarante\.

\[__MFS684912__\]

Para o registro de Estoque das Mercadorias Ingressadas no Regime de Substituição Tributária:

             Preencher com o campo “Código de Ajuste \(Sped Fiscal – Reg C197\)” da Parametrização das Mercadorias Ingressadas no Regime ST

Para Nota de Entrada por Devolução de Mercadoria Ingressadas no Regime de Substituição Tributária:

Consultar a tabela “Ajuste/Outros Valores do Lançamento Fiscal” \(SAFX113\) com os critérios:

- Campos Chave de Identificação da Capa do Documento Fiscal;
- Registro do Ajuste com mesmo Número do Item que está no Item de Mercadoria, ou com o campo Número do Item nulo;
- Código do Ajuste = “SC71000001”\.

Se a consulta retornar algum registro, então:

Preencher o campo com “SC71000001”\.

Senão 

Não Preencher

Indicador de preenchimento dos Valores de ICMS cobrados anteriormente por ST

*\(campo 01 – COD\_IND\_XML reg 2134\)*

\[MFS32070\] Inclusão de campo

Indicador de preenchimento dos Valores de ICMS cobrados anteriormente por ST \(campo “302\- Indicador de preenchimento dos Valores de ICMS cobrados anteriormente por ST\)

# <a id="_Geração_de_Críticas"></a><a id="_Regras_de_Preenchimento:"></a><a id="_Toc206180303"></a><a id="_Toc2012764"></a>Regras de Negócio:

## <a id="OLE_LINK10"></a><a id="_Toc206180304"></a>5\.1 – Regra de Definição do Responsável pela Retenção:

__Se__ campo “132 \- Situação Especial \- Substituição Tributária” igual a ‘1’:

     Considerar o campo Código Reponsável pela Renteção = “3” – Próprio Declarante\.      

__Senão__

     __Se__ campo “131\- Indicador de ICMS\-ST” igual a ‘1’:

         Considerar o campo Código Reponsável pela Renteção = “1” – Rementente Direto\.

__     Se__ campo “131\- Indicador de ICMS\-ST” igual a ‘2’:

         Considerar o campo Código Reponsável pela Renteção = “2” – Rementente Indireto\.

Sendo: 131 \- Código Responsável pela Retenção o campo IND\_FORNEC\_ICMSS da X08\_ITENS\_MERC

            132 \-  Situação Especial \- Substituição Tributária o campo IND\_SITUACAO\_ESP\_ST da X08\_ITENS\_MERC

*\(mesma regra do preenchimento do campo “18\- COD\_RESP\_RET” do registro C176 do Sped Fiscal\)*

*Voltar para o tópico [4 \- Gravação dos Dados na Tabela dos Movimentos \(origem = SAFX07/SAFX08\)](#_Gravação_dos_Dados)*

*Voltar para o campo [Código Responsável Retenção](#OLE_LINK5)\.*

Observação: A nota de devolução deve estar com os campos 131 e 132 preenchidos conforme a nota original de entrada do produto\.

## <a id="OLE_LINK11"></a><a id="_Toc206180305"></a>5\.2 – Preenchimento dos Campos Base de Cálculo do ICMS, Alíquota ICMS e Valor ICMS \(15 \- VL\_BASE\_ICMS ,16 \- ALIQ\_ICMS e 17 \- VL\_ICMS\):

__Orientação da Portaria SEF 378/2018 \(__PeSEF de 03\.12\.18\)__:__

“__Campo 15 \(VL\_BASE\_ICMS\)__: Preenchimento: para o indicador do tipo de operação \(IND\_OPER= código 0\) e o código que indica o responsável pela retenção do ICMS\-ST \(COD\_RESP\_RET = 1\) ou \(COD\_RESP\_RET = 3\), desde que o emitente da NF\-e não seja optante pelo Simples Nacional, informar o valor base de cálculo do ICMS destacado no documento fiscal de entrada\. Não será informado valor quando o código que indica o responsável pela retenção do ICMS\-ST for \(COD\_RESP\_RET = 2\) ou nos casos de \(COD\_RESP\_RET = 1\) e \(COD\_RESP\_RET = 3\), e o emitente da NF\-e for optante pelo Simples Nacional\.

Para o indicador do tipo de operação \(IND\_OPER= código 1\) preencher proporcionalmente com o valor que foi informado neste registro na entrada do item da mercadoria devolvida, e quando a data da emissão da NF\-e de devolução e a data de entrada da NF\-e referenciada coincidirem com os mesmos períodos de referência abrangidos neste registro\.”

“__Campo 16 \(ALIQ\_ICMS\)__: Preenchimento: para o indicador do tipo de operação \(IND\_OPER= código 0\) e o código que indica o responsável pela retenção do ICMS\-ST \(COD\_RESP\_RET = 1\) ou \(COD\_RESP\_RET = 3\), desde que o emitente da NF\-e não seja optante pelo Simples Nacional, informar a alíquota do ICMS incidente na operação própria constante do documento fiscal de entrada\. Não será informado valor quando o código que indica o responsável pela retenção do ICMS\-ST for \(COD\_RESP\_RET = 2\) ou nos casos de \(COD\_RESP\_RET = 1\) e \(COD\_RESP\_RET = 3\), e o emitente da NF\-e for optante pelo Simples Nacional\.

Para o indicador do tipo de operação \(IND\_OPER= código 1\) preencher com o mesmo valor informado neste registro na entrada do item da mercadoria devolvida, e quando a data da emissão da NF\-e de devolução e a data de entrada da NF\-e referenciada coincidirem com os mesmos períodos de referência abrangidos neste registro\.”

“__Campo 17 \(VL\_ICMS\)__: Preenchimento: para indicador do tipo de operação \(IND\_OPER= código 0\) e o código que indica o responsável pela retenção do ICMS\-ST \(COD\_RESP\_RET = 1\) ou \(COD\_RESP\_RET = 3\), desde que o emitente da NF\-e não seja optante pelo Simples Nacional, informar o valor destacado no documento fiscal de entrada como Valor do ICMS\. 

Quando o emitente da NF\-e for optante pelo Simples Nacional, o valor informado deve ser o resultado da diferença do informado no campo CAL\_ICMS\_ST deduzido do valor informado no campo VL\_ICMS\_ST neste registro\. Esta condição não se aplica para o código que indica responsável pela retenção do ICMS\-ST \(COD\_RESP\_RET = 2\), sempre que no XML da NF\-e não foi preenchido a tag especifica com informações relativas ao ICMS cobrado anteriormente por substituição tributária, hipótese que este campo deve ser preenchido com “0” \(zero\)\.

Para indicador do tipo de operação \(IND\_OPER= código 1\), quando a data da NF\-e de devolução e a data de entrada da NF\-e referenciada coincidirem com os mesmos períodos de referência abrangidos neste registro preencher, proporcionalmente, com o mesmo valor para a NF\-e informado neste registro na entrada do item da mercadoria\. Este campo deve ser preenchido com zero, sempre que tenha sido preenchido com “0” \(zero\) na entrada do item da mercadoria\.

A geração deste campo segue a regra abaixo:

Se campo “__Código Responsável pela Retenção__” \(conforme regra [5\.1](#OLE_LINK10)\) for nulo então

- Campo Base de Cálculo do ICMS \(15 – VL\_BC\_ICMS\) = Não Preencher\.
- Campo Alíquota ICMS \(16 – ALIQ\_ICMS\) =  Não Preencher\.
- Campo Valor ICMS \(17 – VL\_ICMS \) = Não Preencher\.

Senão

Se campo “__Código Responsável pela Retenção__” \(conforme regra [5\.1](#OLE_LINK10)\) = \(‘1’ ou ‘3’\) e campo “43\- Enquadrado como Simples Nacional” da SAFX04 = ‘N’ ou não preenchido então:

Preencher os campos Base de Cálculo do ICMS, Alíquota ICMS e Valor ICMS, da seguinte forma:

- 
	- Campo Base de Cálculo do ICMS \(15 – VL\_BC\_ICMS\) =

   

                                 Se campo “55\-Tributação do ICMS” da SAFX08 = “1”, então:

                                       Preencher com o campo “56\-Base ICMS” da SAFX08

__                                                    \+ __campo “56\-Base ICMS” da SAFX08 do item da nota complementar;

__                                       \[MFS30185__: Quando existir nota complementar p/a entrada em questão, conforme descrito na regra de recuperação dos dados 

__                                       __ \(Ver nota “*Sobre as Notas Complementares*”\), os valores da nota complementar são somados aos valores da nota original\.

                                Senão \(Base Tributada ICMS não preenchida ou igual a zeros\)

                                                   Preencher com o campo “226\- Base ICMS Não Destacado” \(__MFS31736__\-Incluiu campo 226\)

__                                                    \+ __campo “56\-Base ICMS” da SAFX08 do item da nota complementar;

__                                       \[MFS30185__: Quando existir nota complementar p/a entrada em questão, conforme descrito na regra de recuperação dos dados 

__                                       __ \(Ver nota “*Sobre as Notas Complementares*”\), os valores da nota complementar são somados aos valores da nota original\.

- 
	- Campo Alíquota ICMS \(16 – ALIQ\_ICMS\) =  

                                        Preencher com o campo “42\-Alíquota ICMS” da SAFX08 se preenchido, ou campo “227\- Alíquota ICMS Não Destacado”\. 

                                        \(__MFS31736__\-Incluiu campo 227\)

__             __

__                                        MFS30185: __Quando existir nota complementar p/a entrada em questão, conforme descrito na regra de recuperação dos dados \(ver nota 

__                           __“*Sobre as Notas Complementares*”\), a alíquota a ser utilizada será a alíquota da nota complementar \(campo “42\-Alíquota ICMS” da 

                           SAFX08 do item da nota complementar\);

- 
	- Campo Valor ICMS \(17 – VL\_ICMS \) = 

                                         Preencher com o campo “43\-Valor ICMS” da SAFX08, se preenchido, ou campo “80\-ICMS não Escriturado”, se preenchido, ou campo 

                                         “225\-Valor ICMS Não Destacado”\. \(__MFS29913__\-Incluiu campos 80 e 225\) 

__                                         \+ __campo “43\-Valor ICMS” da SAFX08, se preenchido, ou campo “80\-ICMS não Escriturado”, se preenchido, ou campo 

                                         “225\-Valor ICMS Não Destacado”do item da nota complementar;

__                             \[MFS30185__: Quando existir nota complementar p/a entrada em questão, conforme descrito na regra de recuperação dos dados 

__                             __ \(Ver nota “*Sobre as Notas Complementares*”\), os valores da nota complementar são somados aos valores da nota original\.

Senão

     __\[MFS34798\] Alteração do cálculo do campo 17 – VL\_ICMS \(condição válida somente a partir de novembro de 2019\)__

                  Se campo “__Código Responsável pela Retenção__” \(conforme regra [5\.1](#OLE_LINK10)\) = \(‘2’\) e Indicador de preenchimento dos Valores de ICMS cobrados  

                  anteriormente por ST = “N”

- Campo Base de Cálculo do ICMS \(15 – VL\_BC\_ICMS\)  = Não Preencher\.
- Campo Alíquota ICMS \(16 – ALIQ\_ICMS\) =  Não Preencher\.
- Campo Valor ICMS \(17 – VL\_ICMS \) = Preencher com zero\.

     Senão

- Campo Base de Cálculo do ICMS \(15 – VL\_BC\_ICMS\)  = Não Preencher\.
- Campo Alíquota ICMS \(16 – ALIQ\_ICMS\) =  Não Preencher\.
- Campo Valor ICMS \(17 – VL\_ICMS \) = Preencher com o resultado da expressão:

 “[Valor ICMS\-ST calculado](#OLE_LINK32)” – “[Valor ICMS\-ST](#OLE_LINK4)” do registro gerado

	Sendo que o “Valor ICMS\-ST calculado” é o campo 22 do registro 2130 e o “Valor ICMS\-ST” é o campo 23 do registro 2130\.

__Observação Importante:__

Para obter a informação do “__Código Responsável pela Retenção__” mencionado na regra acima, __não__ utilizar o campo “Código Responsável pela Retenção” gravado no registro e sim o código resultante da aplicação da regra [5\.1 – Regra de Definição do Responsável pela Retenção](#OLE_LINK10)\.

Isso porque o campo “Código Responsável pela Retenção” só é preenchido no registro para notas de entrada, mas esta regra é válida tanto para entrada como para devolução\.

*Voltar para o tópico [4 \- Gravação dos Dados na Tabela dos Movimentos \(origem = SAFX07/SAFX08\)](#_Gravação_dos_Dados)*

*Voltar para o campo *[*Base de Cálculo do ICMS*](#OLE_LINK3)*;*

## <a id="OLE_LINK15"></a><a id="_Toc206180306"></a>5\.3 – Preenchimento dos Campos Base de Cálculo ICMS\-ST Pago e Integral e Alíquotas ST Pago e Efetiva\(campos 18, 19, 20 e 21\)

__Orientação da Portaria SEF 378/2018 \(__PeSEF de 03\.12\.18\)__:__

__Campo 18 \(VL\_BCST\)__: Preenchimento: para indicador do tipo de operação \(IND\_OPER= código 0\) e se o código que indica o responsável pela retenção do ICMS\-ST

\(COD\_RESP\_RET = 1\), informar o valor destacado no documento fiscal de entrada como Base de Cálculo da Substituição Tributária, se o código que indica o responsável pela retenção do ICMS\-ST \(COD\_RESP\_RET = 2\), preencher com o valor informado no documento fiscal de entrada, e se o código que indica o responsável pela retenção do ICMS\-ST \(COD\_RESP\_RET = 3\), informar o valor utilizada no memória de cálculo para apuração do imposto retido pelo declarante\.

Para indicador do tipo de operação \(IND\_OPER= código 1\), quando a data da NF\-e de devolução e a data de entrada da NF\-e referenciada coincidirem com os mesmos períodos de referência abrangidos neste registro, preencher, proporcionalmente, com o mesmo valor para a NF\-e informado neste registro na entrada do item da mercadoria\.

__Campo 19 \(VL\_BCST\_INT\)__: Preenchimento: para indicador do tipo de operação \(IND\_OPER= código 0\) será informado com o valor integral da base de cálculo da substituição tributária quando se utilizou a alíquota efetiva aplicável ao item da mercadoria na apuração do imposto retido, podendo ter o mesmo valor informado no campo VL\_BCST deste registro\.

Para indicador do tipo de operação \(IND\_OPER= código 1\), quando a data da NF\-e de devolução e a data de entrada da NF\-e referenciada coincidirem com os mesmos períodos de referência abrangidos neste registro, preencher, proporcionalmente, com o mesmo valor para a NF\-e informado neste registro na entrada do item da mercadoria\.

__Esclarecimentos Cliente Magazine Luiza:__

Esta regra foi elaborada utilizando como base o exemplo do cliente Magazine Luíza, já que as orientações da portaria não estavam claras\.

\- Quando há redução de Base de Cálculo, a base de calculo já vem reduzida na nota fiscal, ou seja, os campos da SAFX08 relacionados a Base de ICMS\-ST já recebem o valor da base ICMS\-ST com redução\. No exemplo abaixo, a base de Cálculo ICMS\-ST com redução \(1\.050,00\) estaria na SAFX08\.

\- A base de Cálculo ICMS\-ST com redução deve ser gravada no campo 18 – VL\_BCST \(Base de Cálculo ICMS\-ST Pago\)\.

\- A base de Cálculo do ICMS\-ST integral deve ser calculada, a partir da base de Cálculo ICMS\-ST com redução e do Percentual de Redução do ICMS\-ST\. No exemplo abaixo, o Percentual de Redução foi de 30%\. Ou seja 30% foi aplicado a Base Cálculo do ICMS\-ST integral \(1500,00\), para chegar a base de Cálculo ICMS\-ST com redução \(30% de 1500,00 = 450,00\. 1500,00 – 450,00 = 1\.050,00\)\. Nesta regra vamos fazer o inverso, pois temos a base de Cálculo ICMS\-ST com redução e do Percentual de Redução do ICMS\-ST e precisamos saber a base de Cálculo do ICMS\-ST integral\.

Vamos aplicar uma regra de 3:

 Base de Cálculo ICMS\-ST com redução  ESTÁ PARA   \(100 \- Percentual de Redução do ICMS\-ST\)

 Base de Cálculo do ICMS\-ST integral      ESTÁ PARA   \(100\)

 

Base de Cálculo do ICMS\-ST integral = Base de Cálculo ICMS\-ST com Redução \* 100 / \(100 \- Percentual de Redução do ICMS\-ST\)

   

\- A Base de Cálculo do ICMS\-ST integral deve ser gravada no campo 19 – VL\_BCST\_INT \(Base de Cálculo do ICMS\-ST Integral\)\.

![](data:image/png;base64,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)

A geração deste campo segue a regra abaixo:

__Passo 1__: Recuperar a Base de Cálculo do ICMS\-ST do item de mercadoria da nota:

Se campo “__Código Responsável pela Retenção__” \(conforme regra [5\.1](#OLE_LINK10)\) for nulo então

Base de Cálculo ICMS\-ST Pago \(18 – VL\_BCST\)\) = Não Preencher\.

Base de Cálculo do ICMS\-ST Integral \(19 \- VL\_BCST\_INT\) = Não Preencher\.

Alíquota ICMS\-ST Pago    \(20 – ALIQ\_ST\_E\)    =  Não Preencher\.

Alíquota ICMS\-ST Efetiva \(21 – ALIQ\_ST\_EF\) = Não Preencher\.

Senão

Se campo “__Código Responsável pela Retenção__” \(conforme regra [5\.1](#OLE_LINK10)\) = \(‘1’\) então:

Considerar o campo “61\-Base ICMS\-ST” da SAFX08 

__\+ __campo “61\-Base ICMS\-ST” da SAFX08 do item da nota complementar \(__MFS30185__\);

__\- __campo “61\-Base ICMS\-ST” da SAFX08 do item da nota eletrônica de ajuste \(__MFS58553__\);

Senão :

__Se__ campo “145\-Valor de ICMS – ST Não escriturado” e “144\-Base ICMS\-ST não Escriturada” estiverem preenchidos, então:

Considerar o campo “144\-Base ICMS\-ST não Escriturada” da SAFX08 

__\+ __campo “144\-Base ICMS\-ST Não Escriturada” da SAFX08 do item da nota complementar \(__MFS30185__\);

__\- __campo “144\-Base ICMS\-ST Não Escriturada” da SAFX08 do item da nota eletrônica de ajuste \(__MFS58553__\);

__Senão__

     __Se__ campo “133\-ICMS ST Não Escriturado” e “144\-Base ICMS\-ST não Escriturada” estiverem preenchidos, então:

Considerar o campo “144\-Base ICMS\-ST não Escriturada” da SAFX08

__\+ __campo “144\-Base ICMS\-ST Não Escriturada” da SAFX08 do item da nota complementar \(__MFS30185__\);

__\- __campo “144\-Base ICMS\-ST Não Escriturada” da SAFX08 do item da nota eletrônica de ajuste \(__MFS58553__\);

     __Senão__

             __Se__ campo “107\-Valor Carga Tributária Origem ICMS” e “106\-Base Cálculo Carga Tributária Origem ICMS” estiverem preenchidos, então:

Considerar o campo “106\-Base Cálculo Carga Tribut\. Origem” da SAFX08

__              \+ __campo “106\-Base Cálculo Carga Tribut\. Origem” da SAFX08 do item da nota complementar \(__MFS30185__\);

__              \- __campo “106\-Base Cálculo Carga Tribut\. Origem” da SAFX08 do item da nota eletrônica de ajuste \(__MFS58553__\);

             __Senão__

Base de Cálculo ICMS\-ST Pago \(18 – VL\_BCST\)\) = Não Preencher\.

Base de Cálculo do ICMS\-ST Integral \(19 \- VL\_BCST\_INT\) = Não Preencher\.

__MFS30185__: Quando existir nota complementar p/a entrada em questão, conforme descrito na regra de recuperação dos dados \(ver nota “*Sobre as Notas Complementares*”\), os valores da nota complementar são somados aos valores da nota original\.

__MFS58553__: Quando existir nota fiscal eletrônica de ajuste p/ a entrada em questão, conforme descrito na regra de recuperação dos dados \(ver nota “*Sobre as Notas Fiscais Eletrônicas de Ajuste*”\), os valores da nota de ajuste são subtraídos dos valores da nota original\.

__Passo 2__: Tratamento de Percentual de Redução de Base de Cálculo:

Considerar a “Alíquota Interna” e o “% de Redução da BC” da Parametrização do Produto que foi usada na recuperação do item da nota, conforme descrito no [passo 2](#OLE_LINK14) do tópico [3 \- Recuperação dos Dados e Processamento](#_Recuperação_dos_Dados) deste documento\. Lembrando que a parametrização do Produto usada, foi uma das relacionadas abaixo:

- “Parâmetros à Produtos à Por Código”
- “Parâmetros à Produtos à Por NCM” 
- “Parâmetros à Produtos à Por CEST”

Se “% de Redução da BC” estiver preenchido e for diferente de zero, então:

Base de Cálculo ICMS\-ST Pago \(18 – VL\_BCST\)\) = Base de Cálculo do ICMS\-ST recuperada da SAFX08 no __Passo 1__\.

Base de Cálculo do ICMS\-ST Integral \(19 \- VL\_BCST\_INT\) = Base de Cálculo do ICMS\-ST recuperada da SAFX08 \* 100 / \(100 \- “% de Redução da BC”\)

Alíquota ICMS\-ST Pago    \(20 – ALIQ\_ST\_E\)    =  Alíquota Interna

Alíquota ICMS\-ST Efetiva \(21 – ALIQ\_ST\_EF\) = Alíquota Interna – \(Alíquota Interna \* “% de Redução da BC”/100\)

Senão:

Base de Cálculo ICMS\-ST Pago \(18 – VL\_BCST\)\)= Base de Cálculo do ICMS\-ST recuperada da SAFX08 no __Passo 1__\.

Base de Cálculo do ICMS\-ST Integral \(19 \- VL\_BCST\_INT\)= Base de Cálculo do ICMS\-ST recuperada da SAFX08 no __Passo 1__\.

Alíquota ICMS\-ST Pago    \(20 – ALIQ\_ST\_E\)   = Alíquota Interna

Alíquota ICMS\-ST Efetiva \(21 – ALIQ\_ST\_EF\) = Alíquota Interna

__Observações Importantes:__

1. Para obter a informação do “__Código Responsável pela Retenção__” mencionado na regra acima, __não__ utilizar o campo “Código Responsável pela Retenção” gerado no registro e sim o código resultante da aplicação da regra [5\.1 – Regra de Definição do Responsável pela Retenção](#OLE_LINK10)\.

Isso porque o campo “Código Responsável pela Retenção” só é preenchido no registro para notas de entrada, mas esta regra é válida tanto para entrada como para devolução\.

1. __Truncar os valores resultantes das expressões acima, para de acordo com o número de casas do campo\.__

__Histórico:__

Esta regra foi feita baseada na regra de geração do campo 09 – VL\_UNIT\_BC\_ST do registro__ __C176__ __Sped Fiscal\.

A base de cálculo a ser utilizada dependerá do campo que estiver preenchido na SAFX08, já que devemos considerar que a operação pode ter o ICMS\-ST escriturado ou não escriturado, e em qualquer um dos casos a base de cálculo precisa ser demonstrada no registro 2130\.

Desta forma, qualquer que seja a situação tributária da nota de entrada do produto, a informação será demonstrada\. O usuários da CAT17 e os clientes obrigados a geração dos registros 88STES e 88STITNF do Sintegra \(Decreto 44\.541 de Junho/07, SEF\-MG\) e registro C176 do Sped Fiscal, já estão cientes da necessidade de carregar a informação nos campo 144 ou 106 no caso do ST não escriturado na entrada\.  

Regra do C176:

__Se__ campo “61\-Base ICMS\-ST” da SAFX08 estiver preenchido, então:

     Preencher com o campo “61\-Base ICMS\-ST”\.

__Senão__

     __Se__ campo “144\-Base ICMS\-ST não Escriturada”, estiver preenchido, então:

         Preencher com o campo “144\-Base ICMS\-ST não Escriturada”\.

     __Senão__

          __Se__ campo “106\-Base Cálculo Carga Tribut Origem”, estiver preenchido, então:

               Preencher com o campo “106\-Base Cálculo Carga Tribut Origem”\.

          __Senão__

               O campo não será preenchido\.

*Voltar para o tópico [4 \- Gravação dos Dados na Tabela dos Movimentos \(origem = SAFX07/SAFX08\)](#_Gravação_dos_Dados)*

*Voltar para o campo [Base de Cálculo ICMS\-ST Pago](#OLE_LINK6)*

*Volta para o campo [Base de Cálculo ICMS\-ST Integral](#OLE_LINK7)*

## <a id="OLE_LINK18"></a><a id="_Toc206180307"></a>5\.4 – Preenchimento do Campo Valor ICMS\-ST \(23 – VL\_ICMS\_ST\)

__Campo 23 \(VL \_ICMS\_ST\)__: Preenchimento: para indicador do tipo de operação \(IND\_OPER= código 0\) e se o código que indica o responsável pela retenção do ICMS\-ST \(COD\_RESP\_RET = 1\) informar o valor destacado no documento fiscal de entrada como Valor do ICMS Substituição Tributária, se o código que indica o responsável pela retenção do ICMS\-ST \(COD\_RESP\_RET = 2\) informar o valor que consta no documento fiscal de entrada, e se o código que indica o responsável pela retenção do ICMS\-ST \(COD\_RESP\_RET = 3\) informar o valor utilizada no memória de cálculo para apuração do imposto retido pelo declarante\.

Para indicador do tipo de operação \(IND\_OPER= código 1\), quando a data da NF\-e de devolução e a data de entrada da NF\-e referenciada coincidirem com os mesmos períodos de referência abrangidos neste registro, preencher proporcionalmente com o mesmo valor para a NF\-e informado neste registro na entrada do item da mercadoria\.

A geração deste campo segue a regra abaixo:

Se campo “__Código Responsável pela Retenção__” \(conforme regra [5\.1](#OLE_LINK10)\) for nulo então

Valor ICMS\-ST \(23 – VL\_ICMS\_ST\)\) = Não Preencher\.

Senão

Se campo “__Código Responsável pela Retenção__” \(conforme regra [5\.1](#OLE_LINK10)\) = \(‘1’\) então:

Valor ICMS\-ST \(23 – VL\_ICMS\_ST\) = 

          Campo “52\-Valor ICMS Substituição Tributária” da SAFX08

__           \+ __campo “52\-Valor ICMS Substtuição Tributária” da SAFX08 do item da nota complementar \(__MFS30185__\);

__           \- __campo “52\-Valor ICMS Substtuição Tributária” da SAFX08 do item da nota eletrônica de ajuste \(__MFS58553__\);

Senão : 

__Se__ campo “145\-Valor de ICMS – ST Não escriturado” e “144\-Base ICMS\-ST não Escriturada” estiverem preenchidos, então:

Valor ICMS\-ST \(23 – VL\_ICMS\_ST\) = 

         Campo “145\-Valor de ICMS\-ST Não escriturado” da SAFX08

__        \+ __campo “145\-Valor de ICMS\-ST Não Escriturado” da SAFX08 do item da nota complementar \(__MFS30185__\);

__        \- __campo “145\-Valor de ICMS\-ST Não Escriturado” da SAFX08 do item da nota eletrônica de ajuste \(__MFS58553__\);

__Senão__

     __Se__ campo “133\-ICMS ST Não Escriturado” e “144\-Base ICMS\-ST não Escriturada” estiverem preenchidos, então:

Valor ICMS\-ST \(23 – VL\_ICMS\_ST\) = 

          Campo “133\-ICMS ST Não Escriturado” da SAFX08

__          \+ __campo “133\-ICMS ST Não Escriturado” da SAFX08 do item da nota complementar \(__MFS30185__\);

          __\- __campo “133\-ICMS ST Não Escriturado” da SAFX08 do item da nota eletrônica de ajuste \(__MFS58553__\);

     __Senão__

             __Se__ campo “107\-Valor Carga Tributária Origem ICMS” e “106\-Base Cálculo Carga Tributária Origem ICMS” estiverem preenchidos, então:

Valor ICMS\-ST \(23 – VL\_ICMS\_ST\) =

          Campo “107\-Valor Carga Tributária Origem ICMS” da SAFX08

__          \+ __campo “107\-Valor Carga Tributária Origem ICMS” da SAFX08 do item da nota complementar \(__MFS30185__\);

__          \- __campo “107\-Valor Carga Tributária Origem ICMS” da SAFX08 do item da nota eletrônica de ajuste \(__MFS58553__\);

             __Senão__

Valor ICMS\-ST \(23 – VL\_ICMS\_ST\) = Não Preencher\.

__MFS30185__: Quando existir nota complementar p/a entrada em questão, conforme descrito na regra de recuperação dos dados \(ver nota “*Sobre as Notas Complementares*”\), os valores da nota complementar são somados aos valores da nota original\.

__MFS58553__: Quando existir nota fiscal eletrônica de ajuste p/ a entrada em questão, conforme descrito na regra de recuperação dos dados \(ver nota “*Sobre as Notas Fiscais Eletrônicas de Ajuste*”\), os valores da nota de ajuste são subtraídos dos valores da nota original\.

__Observação Importante:__

Para obter a informação do “__Código Responsável pela Retenção__” mencionado na regra acima, __não__ utilizar o campo “Código Responsável pela Retenção” gerado no registro e sim o código resultante da aplicação da regra [5\.1 – Regra de Definição do Responsável pela Retenção](#OLE_LINK10)\.

Isso porque o campo “Código Responsável pela Retenção” só é preenchido no registro para notas de entrada, mas esta regra é válida tanto para entrada como para devolução\.

__Histórico:__

Esta regra foi feita baseada na regra de geração do registro__ __C176__ __Sped Fiscal\.

O valor utilizado dependerá do campo que estiver preenchido na SAFX08\. Devemos considerar que a operação pode ter o ICMS\-ST escriturado ou não escriturado, e em qualquer um dos casos o ICMS\-ST precisa ser demonstrado no registro 2130\.

Regra do C176:

__Se__ campo “52\-Valor ICMS Substituição Tributária” da SAFX08 estiver preenchido, então:

     Preencher com o campo “52\-Valor ICMS Substituição Tributária”\.

__Senão__

     __Se__ campo “145\-Valor de ICMS – ST Não escriturado”, estiver preenchido, então:

         Preencher com o campo “145\-Valor de ICMS – ST Não escriturado”\.

     __Senão__

         __Se__ campo “133\-ICMS ST Não Escriturado”, estiver preenchido, então:

             Preencher com o campo “133\-ICMS ST Não Escriturado”\.

         __Senão__

             __Se__ campo “107\-Valor Carga Tributária Origem ICMS”, estiver preenchido, então:

                  Preencher com o campo “107\-Valor Carga Tributária Origem ICMS”\.

             __Senão__

                 O campo não será preenchido\.

*Voltar para o tópico [4 \- Gravação dos Dados na Tabela dos Movimentos \(origem = SAFX07/SAFX08\)](#_Gravação_dos_Dados)*

*Voltar para o campo [Valor ICMS\-ST](#OLE_LINK4)*

# <a id="_Geração_de_Críticas_1"></a><a id="_6.1_–_Crítica"></a><a id="_6.3_-_Critica"></a><a id="_6.6_-_Critica"></a><a id="_Toc17994807"></a><a id="_Toc206180308"></a>Gravação dos Dados das Notas Complementares 

As notas complementares que não foram gravadas na Tabela dos Movimentos, e tiveram seus valores totalizados na nota da operação original, serão armazenadas em tabela separada, sempre associadas às notas originais\.  Estas informações darão origem aos registros __2133__ na geração do arquivo magnético\.

\(ver regras sobre as notas complementares no item “3\-Recuperação dos Dados e Processamento”, item “Sobre as Notas Complementares”\)

Os campos sinalizados com asterisco compõem a chave da tabela, que são:

__ \[__ Chave da identificação do item da nota original na Tabela dos Movimentos __\+__ Chave NFe da NF Complementar __\+__ Item da Nota Complementar __\]__

 

Lembrando que a nota complementar fica sempre associada à entrada original do 2130\.

__\*\*\*__

__Código da empresa__

                              

                        Dados de identificação do item da nota original na Tabela dos Movimentos

                

__\*\*\*__

__Código do estabelecimento__

__\*\*\*__

__Código do estabelecimento de origem__

__\[MFS46838\] Tratamento para Perfil D:__

Com o tratamento do Perfil D, onde os documentos fiscais são recuperados dos estabelecimentos __Centralizador__ e __Centralizados__, este campo passa a ser gravado com o estabelecimento presente na nota fiscal original\.

__\*\*\*__

__Período \(mês e ano\)__

__\*\*\*__

__Produto__

__\*\*\*__

__Data Fiscal __

__\*\*\*__

__Tipo do Documento__

__\*\*\*__

__Série do Documento__

__\*\*\*__

__Número do Documento__

__\*\*\*__

__Pessoa Fis/Jur__

__\*\*\*__

__Número do Item__

__\*\*\*__

__Movimento E/S__

__\*\*\*__

__Chave Documento Fiscal Eletrônico da Nota Complementar__

__*\(campo 02 do registro 2133\)*__

Chave do documento fiscal eletrônico \(campo 226\-Chave de Acesso da NF\-Eletrônica, SAFX07\) da nota complementar

Número do Item da Nota Complementar

*\(campo 03 do registro 2133\)*

Número do item do documento fiscal \(campo “18\-Item Nota Fiscal” da SAFX08\) da nota complementar 

\(item que corresponde ao produto da nota original, informada no registro 2130\)

# <a id="_Toc206180309"></a>Gravação dos Dados das Notas Fiscais Eletrônicas de Ajuste 

__\[MFS58553 – Portaria 013/2021\]__

As notas fiscais eletrônicas de ajuste \(campo “125\-Situação Especial” da capa = “E”\), que não foram gravadas na Tabela dos Movimentos, e tiveram seus valores deduzidos da nota da operação original, serão armazenadas em tabela separada, sempre associadas às notas originais\.  Estas informações darão origem aos registros __2135__ na geração do arquivo magnético\.

\(ver regra sobre as notas fiscais eletrônicas de ajuste no item “3\-Recuperação dos Dados e Processamento”, item “Sobre as Notas Fiscais Eletrônicas de ajuste”\)

Os campos sinalizados com asterisco compõem a chave da tabela, que são:

__ \[__ Chave da identificação do item da nota original na Tabela dos Movimentos __\+__ Chave NFe da NF de Ajuste __\+__ Item da NF de Ajuste__\]__

 

Lembrando que a nota de ajuste fica sempre associada à entrada original do 2130\.

Tabela das Notas Eletrônicas de Ajuste \(EST\_ST\_SC\_NF\_AJ\)

__\*\*\*__

__Código da empresa__

                              

                        Dados de identificação do item da nota original na Tabela dos Movimentos

                

__\*\*\*__

__Código do estabelecimento__

__\*\*\*__

__Código do estabelecimento de origem__

__\[MFS46838\] Tratamento para Perfil D:__

Com o tratamento do Perfil D, onde os documentos fiscais são recuperados dos estabelecimentos __Centralizador__ e __Centralizados__, este campo passa a ser gravado com o estabelecimento presente na nota fiscal original\.

__\*\*\*__

__Período \(mês e ano\)__

__\*\*\*__

__Produto__

__\*\*\*__

__Data Fiscal __

__\*\*\*__

__Tipo do Documento__

__\*\*\*__

__Série do Documento__

__\*\*\*__

__Número do Documento__

__\*\*\*__

__Pessoa Fis/Jur__

__\*\*\*__

__Número do Item__

__\*\*\*__

__Movimento E/S__

__\*\*\*__

__Chave Documento Fiscal Eletrônico da Nota de Ajuste__

__*\(campo 02 do registro 2135\)*__

Chave do documento fiscal eletrônico \(campo 226\-Chave de Acesso da NF\-Eletrônica, SAFX07\) da nota de ajuste\.

Número do Item da Nota de Ajuste

*\(campo 03 do registro 2135\)*

Número do item do documento fiscal \(campo “18\-Item Nota Fiscal” da SAFX08\) da nota de ajuste\. 

\(item que corresponde ao produto da nota original, informada no registro 2130\)

<a id="_6.7_-_Critica"></a>

= = = = = =

 

 

