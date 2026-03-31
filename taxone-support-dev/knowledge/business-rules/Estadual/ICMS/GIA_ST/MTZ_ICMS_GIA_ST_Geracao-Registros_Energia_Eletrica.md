# MTZ_ICMS_GIA_ST_Geracao-Registros_Energia_Eletrica

- **Fonte:** MTZ_ICMS_GIA_ST_Geracao-Registros_Energia_Eletrica.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 76 KB

---

THOMSON REUTERS

GIA\-ST

Geração dos Registros de Energia Elétrica

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS3854

Julyana Perrucini

Inclusão de regra específica para recuperação das informações de empresas no segmento de energia elétrica\.

__MFS10606__

Alteração na geração dos vencimentos

Preenchimento do Valor a Recolher p/ Vencimento Único

REGRAS DE NEGÓCIO

__SAFX42, SAFX43 e Apuração do ICMS\-ST\.__

__Saída para aba Registro Principal__

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN00

__Regra Geral Registro Principal__:

__Seleção dos registros__

Se o parâmetro “Informações para Empresas de Energia Elétrica” estiver *marcado* na tela de Geração:

Considerar a seleção dos registros da SAFX42 e SAFX43, com as seguintes condições:

Modelo de Documento \(campo 13\-COD\_MODELO da tabela SAFX42\) = 01, 06;

Situação da Nota \(campo 21\-SITUACAO da tabela SAFX42\) <> S

Classificação do Documento Fiscal \(campo 50\-COD\_CLASS\_DOC\_FIS da tabela SAFX42\) = 1, 3;

Código Fiscal \(campo 13\-COD\_CFO da tabela SAFX43\) parametrizado em Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por CFOP >> Energia Elétrica, do módulo Estadual – ICMS;

Valor Substituição Tributária \(campo 39\- VLR\_SUBST\_TRIB da tabela SAFX43\) > 0;

A UF do Ponto de Consumo/Terminal faturado \(campo 75\-UF\_CONSUMO da SAFX42\) deve ser considerada para geração das Guias por UF Favorecida, desde que esteja parametrizada em Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida, do módulo Estadual – ICMS\. *Observação:* nesse caso não será considerado parâmetro 67 do livro da apuração, conforme feito no procedimento das SAFX07 e SAFX08\.

__Vencimentos__

Para recuperar os Vencimentos e Valores do ICMS\-ST, existem dois processos na rotina de geração da GIA\-ST:

- Através das GNRE’s, preenchendo automaticamente os campos de Vencimentos e Valores associados aos vencimentos das GNRE’s do período, que deverá ser habilitado conforme o vencimento do ICMS\-ST, mas preenchido manualmente;

Nesse caso é verificado se existe conteúdo na tabela ICT\_GUIA\_GNRE\_CON, que contém as guias recolhidas no período, então se houver, a rotina de geração realiza o tratamento abaixo:

1. Verifica a inscrição estadual do estabelecimento para a UF em questão \(módulo Básicos \- Parâmetros, menu Preliminares >> Inscrições Estaduais\);
2. Caso a inscrição não esteja cadastrada, ou esteja suspensa, soma todas as guias da UF em questão, o valor recuperado será gravado na GIA\-ST no campo do 1º vencimento \(módulo Estadual \- ICMS, menu Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Manutenção\), e a data do vencimento será a maior data das GNRE’s existentes no período;
3. Caso a inscrição exista e seja válida, totaliza as GNRE’s por data de vencimento, e grava um registro para cada vencimento, com o valor totalizado do vencimento\.

*Observações:*

- A GIA\-ST é sempre gerada por UF, portanto, ao ler as GNRE’s na tabela ICT\_GUIA\_GNRE\_CON, sempre considera a UF da GIA\-ST, tratando cada caso separadamente\.
- Ao fazer o cálculo das GNRE’s considera as GNRE’s com Data de Apuração dentro do período informado na GIA\-ST\.
- Ou; Através da parametrização por UF Favorecida \(módulo Estadual \- ICMS, menu Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\) caso não localize guias no período\. Nesse caso o usuário precisa colocar os dias de Vencimento e quando efetuar a geração dos dados, esses dias serão preenchidos na Manutenção no item Vencimentos da Aba Principal, mas seu valor deverá ser preenchido manualmente\. Alteração da __MFS10606__: O Valor do ICMS\-ST referente ao primeiro dia de vencimento passou a ser preenchido de forma automática, mas *apenas* quando existir apenas um dia de vencimento na parametrização\. Neste caso, o Valor do ICMS\-ST será preenchido com o valor total do ICMS\-ST apurado para a UF\.  Quando for parametrizado mais de um dia de vencimento, nenhum valor será preenchido de forma automática, e os valores referentes a cada um dos vencimentos deverão ser informados manualmente através da tela de manutenção\.

Se o parâmetro “Informações para Empresas de Energia Elétrica” estiver *desmarcado* na tela de Geração:

Considerar a geração normal pela SAFX07, SAFX08 e outros: MTZ \- ICMS \- GIA\-ST Geracao \(Registros\)\.doc\.

MFS3854

__MFS10606__

RN01

Campo __Estabelecimento:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com o estabelecimento parametrizado de acordo com a UF Favorecida e escolhido na tela de geração dos registros\.

MFS3854

RN02

Campo __Data Apuração:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Geração\.

Preencher com o último dia do mês preenchido no campo Período, se houver mais de um mês no range do período, serão consideradas duas apurações\.

MFS3854

RN03

Campo __UF Favorecida:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária Geração >> Parâmetros por UF Favorecida\.

Preencher com a UF Favorecida parametrizada e de acordo com as notas fiscais recuperadas no período da apuração\.

__Tratamento:__

- Se não houver UF Favorecida parametrizada, será gerada pelo menos a UF do estabelecimento como GIA Sem Movimento, pois se existir Inscrição Estadual, gravará registro zerado, inclusive em casos em que houver inscrição de substituto tributário\.

MFS3854

RN04

Campo __Vlr\. dos Produtos:__

__Origem: __Básicos >> MasterSAF DW >> Manutenção >> Documento Fiscal >> Novo Documento Fiscal >> Documento Fiscal Utilities \- Capa\.

Preencher com o conteúdo do campo Valor Total do Documento Fiscal \(campo 17\-VLR\_TOT\_NOTA da tabela SAFX42\)\.

__Tratamento:__

Considerar o parâmetro Valor dos Produtos da tela de geração dos registros, da seguinte forma:

- Não irá considerar valor de seguro e frete por não existirem essas situações em casos de nota fiscal de energia elétrica, então mesmo se selecionados não surtirá efeitos no cálculo, porém serão considerados os campos Outras Despesas e Desconto: Valor Total do Documento Fiscal \(campo 17\-VLR\_TOT\_NOTA da tabela SAFX42\) \+ Valor Outras Despesas \(campo 18\-VLR\_OUTRAS\_DESP da tabela SAFX42\) \- Valor do Desconto \(campo 18\-VLR\_DESCONTO da tabela SAFX43\); o cálculo será feito de acordo com o item que for selecionado\.

MFS3854

RN05

Campo __Vlr\. do IPI:__

Não se aplica em casos de energia elétrica\.

MFS3854

RN06

Campo __Base de Cálculo ICMS Próprio:__

__Origem: __Básicos >> MasterSAF DW >> Manutenção >> Documento Fiscal >> Novo Documento Fiscal >> Documento Fiscal Utilities \- Item\.

Preencher com o conteúdo do campo Base Tributada \(campo 23\-VLR\_BASE\_ICMS\_1 da tabela SAFX43\)\.

MFS3854

RN07

Campo __ICMS Próprio:__

__Origem: __Básicos >> MasterSAF DW >> Manutenção >> Documento Fiscal >> Novo Documento Fiscal >> Documento Fiscal Utilities \- Item\.

Preencher com o conteúdo do campo Valor ICMS \(campo 22\-VLR\_TRIB\_ICMS da tabela SAFX43\)\.

MFS3854

RN08

Campo __Base de Cálculo ICMS\-ST:__

__Origem: __Básicos >> MasterSAF DW >> Manutenção >> Documento Fiscal >> Novo Documento Fiscal >> Documento Fiscal Utilities \- Item\.

Preencher com o conteúdo do campo Base Substituição Tributária \(campo 40\- VLR\_BASE\_SUB\_TRIB da tabela SAFX43\)\.

MFS3854

RN09

Campo __ICMS\-ST:__

__Origem: __Básicos >> MasterSAF DW >> Manutenção >> Documento Fiscal >> Novo Documento Fiscal >> Documento Fiscal Utilities \- Item\.

Preencher com o conteúdo do campo Valor Substituição Tributária \(campo 39\- VLR\_SUBST\_TRIB da tabela SAFX43\)\.

MFS3854

RN10

Campo __ICMS\-ST Devoluções:__

Não se aplica em casos de energia elétrica\.

MFS3854

RN11

Campo __ICMS\-ST Ressarcimento:__

Não se aplica em casos de energia elétrica\.

MFS3854

RN12

Campo __Crédito ICMS\-ST Período Anterior:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária Geração >> Manutenção\.

Preencher com o conteúdo do campo Crédito p/ o Período Seguinte \(campo VLR\_GIA\_ST\_MES\_ANT da tabela ICT\_GIA\_ST\)\.

MFS3854

RN13

Campo __Pagto ICMS\-ST Antecipado:__

Preenchimento manual por parte do contribuinte\.

MFS3854

RN14

Campo __Lançamentos Complementares – Outros Débitos:__

__Origem: __Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS Subst\. Tributária >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única\.

Se o parâmetro “Geração p/ Empresas com IEU” estiver marcado na tela de Geração \(geração dos registros da GIA\-ST\), as informações serão recuperadas da tabela de apuração de Empresas c/ Insc\. Estadual Única, caso contrário, as informações serão recuperadas da tabela de apuração Ajuste SINIEF\.

Se o parâmetro “Utilizar os lançamentos da apuração do ICMS\-ST \(P9\) para complementar a GIA\-ST” estiver marcado, o campo será gravado com o total dos lançamentos complementares da Apuração do ICMS\-ST \(P9\) referentes ao período e UF em questão, e classificados como “outros débitos” \(lançamentos com código de operação = “__002__”\)\.

Senão

      O campo será gravado com o valor zero\.  

MFS3854

RN15

Campo __Lançamentos Complementares – Estorno de Crédito:__

__Origem: __Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS Subst\. Tributária >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única\.

Se o parâmetro “Geração p/ Empresas com IEU” estiver marcado na tela de Geração \(geração dos registros da GIA\-ST\), as informações serão recuperadas da tabela de apuração de Empresas c/ Insc\. Estadual Única, caso contrário, as informações serão recuperadas da tabela de apuração Ajuste SINIEF\.

Se o parâmetro “Utilizar os lançamentos da apuração do ICMS\-ST \(P9\) para complementar a GIA\-ST” estiver marcado, o campo será gravado com o total dos lançamentos complementares da Apuração do ICMS\-ST \(P9\) referentes ao período e UF em questão, e classificados como “estorno de crédito” \(lançamentos com código de operação = “__003__”\)\.

Senão

      O campo será gravado com o valor zero\.  

MFS3854

RN16

Campo __Lançamentos Complementares – Outros Créditos:__

__Origem: __Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS Subst\. Tributária >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única\.

Se o parâmetro “Geração p/ Empresas com IEU” estiver marcado na tela de Geração \(geração dos registros da GIA\-ST\), as informações serão recuperadas da tabela de apuração de Empresas c/ Insc\. Estadual Única, caso contrário, as informações serão recuperadas da tabela de apuração Ajuste SINIEF\.

Se o parâmetro “Utilizar os lançamentos da apuração do ICMS\-ST \(P9\) para complementar a GIA\-ST” estiver marcado, o campo será gravado com o total dos lançamentos complementares da Apuração do ICMS\-ST \(P9\) referentes ao período e UF em questão, e classificados como “outros créditos” \(lançamentos com código de operação = “__006__”\)\.

Senão

      O campo será gravado com o valor zero\.  

MFS3854

RN17

Campo __Lançamentos Complementares – Estorno de Débito:__

__Origem: __Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS Subst\. Tributária >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única\.

Se o parâmetro “Geração p/ Empresas com IEU” estiver marcado na tela de Geração \(geração dos registros da GIA\-ST\), as informações serão recuperadas da tabela de apuração de Empresas c/ Insc\. Estadual Única, caso contrário, as informações serão recuperadas da tabela de apuração Ajuste SINIEF\.

Se o parâmetro “Utilizar os lançamentos da apuração do ICMS\-ST \(P9\) para complementar a GIA\-ST” estiver marcado, o campo será gravado com o total dos lançamentos complementares da Apuração do ICMS\-ST \(P9\) referentes ao período e UF em questão, e classificados como “estorno de débito” \(lançamentos com código de operação = “__007__”\)\.

Senão

      O campo será gravado com o valor zero

MFS3854

RN18

Campo __Lançamentos Complementares – Deduções:__

__Origem: __Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS Subst\. Tributária >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única\.

Se o parâmetro “Geração p/ Empresas com IEU” estiver marcado na tela de Geração \(geração dos registros da GIA\-ST\), as informações serão recuperadas da tabela de apuração de Empresas c/ Insc\. Estadual Única, caso contrário, as informações serão recuperadas da tabela de apuração Ajuste SINIEF\.

Se o parâmetro “Utilizar os lançamentos da apuração do ICMS\-ST \(P9\) para complementar a GIA\-ST” estiver marcado, o campo será gravado com o total dos lançamentos complementares da Apuração do ICMS\-ST \(P9\) referentes ao período e UF em questão, e classificados como “deduções” \(lançamentos com código de operação = “__012__”\)\.

Senão

      O campo será gravado com o valor zero\.

MFS3854

RN19

Campo __ICMS\-ST Devido:__

Preencher com o seguinte cálculo se positivo, caso negativo gravar zero:

\(ICMS\-ST \+ Outros Débitos \+ Estorno de Crédito\) \- \(ICMS\-ST Devoluções \+ Crédito ICMS\-ST Período Anterior \+ Outros Créditos \+ Estorno de Débito \+ Deduções\)\.

Observar que na totalização dos valores não é necessário utilizar o parâmetro de utilização dos lançamentos complementares, pois caso os mesmos não sejam utilizados, os respectivos campos estarão com valor zero\.

MFS3854

RN20

Campo __Crédito p/ o Período Seguinte:__

Preencher com o seguinte cálculo e se positivo gravar o resultado no campo "Crédito p/o Período Seguinte", caso negativo, gravar o resultado no campo "ICMS\-ST a Recolher" \(sem o sinal de negativo\):

\(ICMS\-ST Devoluções \+ Crédito ICMS\-ST Período Anterior \+ Outros Créditos \+ Estorno de Débito \+ Deduções\) \- \(ICMS\-ST \+ Outros Débitos \+ Estorno de Crédito\)\.

Observar que este valor é o resultado do total dos créditos \- total dos débitos\.

MFS3854

RN21

Campo __Despesas Acessórias:__

__Origem: __Básicos >> MasterSAF DW >> Manutenção >> Documento Fiscal >> Novo Documento Fiscal >> Documento Fiscal Utilities \- Item\.

Preencher com o conteúdo do campo Valor Outras Despesas \(campo 46\-VLR\_OUTRAS\_DESP da tabela SAFX43\)\.

MFS3854

RN22

Campo __Repasse ICMS\-ST Combustível:__

Não se aplica em casos de energia elétrica\.

MFS3854

RN23

Campo __ICMS\-ST a Recolher:__

Preencher de acordo com o resultado da RN20\.

MFS3854

RN24

Campo __GIA Sem Movimento:__

Se não houver valores a serem gravados na GIA\-ST, gravar como sem movimento, será considerado sem movimento se apenas os campos Crédito ICMS\-ST Período Anterior e Crédito p/ o Período Seguinte tiverem valor\.

MFS3854

RN25

Campo __GIA Substitutiva:__

Preenchimento manual por parte do contribuinte\.

MFS3854

RN26

Campo __Oper\. Repasse de Combustível:__

Não se aplica em casos de energia elétrica\.

MFS3854

RN27

Campo__ Vencimentos – Data do 1º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com a data do 1º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

MFS3854

RN28

Campo__ Vencimentos – Data do 2º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com a data do 2º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

MFS3854

RN29

Campo__ Vencimentos – Data do 3º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com a data do 3º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

MFS3854

RN30

Campo__ Vencimentos – Data do 4º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com a data do 4º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

MFS3854

RN31

Campo__ Vencimentos – Data do 5º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com a data do 5º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

MFS3854

RN32

Campo__ Vencimentos – Data do 6º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com a data do 6º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

MFS3854

RN33

Campo__ Vencimentos – Valor do 1º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com o valor a recolher referente o 1º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

Alteração da __MFS10606__: 

O Valor do ICMS\-ST referente ao primeiro dia de vencimento passou a ser preenchido de forma automática, mas *apenas* quando existir apenas um dia de vencimento na parametrização \(menu “Parâmetros por UF Favorecida”\)\. Neste caso, o Valor do ICMS\-ST será preenchido com o valor total do ICMS\-ST apurado para a UF \(este valor corresponde ao campo “21\-Total do ICMS\-ST a Recolher” da GIA\-ST, que na tela de manutenção é o campo “ICMS\-ST a Recolher”\)\. 

Quando for parametrizado mais de um dia de vencimento, nenhum valor será preenchido de forma automática, e todos os valores referentes a cada vencimento deverão ser informados manualmente através da tela de manutenção\.

__OS2289__

__MFS10606__

RN34

Campo__ Vencimentos – Valor do 2º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com o valor a recolher referente o 2º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

__OS2289__

RN35

Campo__ Vencimentos – Valor do 3º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com o valor a recolher referente o 3º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

__OS2289__

RN36

Campo__ Vencimentos – Valor do 4º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com o valor a recolher referente o 4º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

__OS2289__

RN37

Campo__ Vencimentos – Valor do 5º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com o valor a recolher referente o 5º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

__OS2289__

RN38

Campo__ Vencimentos – Valor do 6º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com o valor a recolher referente o 6º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

__OS2289__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

