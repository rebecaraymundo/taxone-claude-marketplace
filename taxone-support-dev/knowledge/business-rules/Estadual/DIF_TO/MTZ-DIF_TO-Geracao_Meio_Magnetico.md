# MTZ-DIF_TO-Geracao_Meio_Magnetico

- **Fonte:** MTZ-DIF_TO-Geracao_Meio_Magnetico.docx
- **Modificado:** 2026-02-24
- **Tamanho:** 119 KB

---

# DIF TO \- Geração do Meio Magnético

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__OS2761__

DIF\- TO Geração do Arquivo Magnético

Este documento de requisito tem por objetivo realizar a geração do meio magnético DIF\-TO\.

__CH268\_2013__

Atualização da versão para 2013\.1

Atualização da versão para 2013\.1

__CH170\_2014__

Atualização da versão para 2014\.1

Disponibilizar a versão 2014\.1 no arquivo magnético

__CH135\_2015__

Atualização da versão para 2015\.1

Disponibilizar a versão 2015\.1 no arquivo magnético

__MFS8525__

Atualização da versão para 2016\.1

Disponibilizar a versão 2016\.1 no arquivo magnético

__CH1960\_2017__

Atualização da versão para 2017\.1

Disponibilizar a versão 2017\.1 no arquivo magnético

__CH9620\_2017 \(MFS\-11647\)__

Alteração no Segmento F

Este documento tem como objetivo alterar o preenchimento dos campos Valor Contábil e Base de Cálculo do Contribuinte e Não Contribuinte para corrigir o problema de duplicidade\.

__MFS\-15858__

Atendimento a Portaria nº 1\.014/2017 para atualização da versão para 2018\.1

Este documento tem como objetivo atender a Portaria nº 1\.014/2017 que disponibiliza a versão DIF TO/2018\.

__MFS23835__

Atualização da versão para 2019\.1

Disponibilizar a versão 2019\.1 no arquivo magnético

__MFS33858__

Atualização da versão para 2019\.1

Disponibilizar a versão 2020\.1 no arquivo magnético

__MFS\-57993__

Correção Itens 3\.3, 3\.4 e 3\.5 do Segmento C

Correção do preenchimento dos itens 3\.4 – Outras/Isentas e não tributadas e 3\.5 – Substituição Tributário, pois conforme manual “__*Anexo 1 da DIF*__” o Item __3\.6 – SUBSTITUIÇÃO TRIBUTÁRIA:__ deverá ser preenchida com os valores contábeis das entradas de mercadorias sujeitas ao regime de substituição tributária\. Considerar somente aquelas cujas entradas foram alcançadas por esse regime\. E consequentemente não informar o valor da Coluna Outras, caso contrário ocorrerá crítica no validador\. Alteração das Regras RNC8, RNC9 e RNC10\.

[__MFS58823__](https://jira.thomsonreuters.com/browse/MFS-58823)

Correção do critério de busca do Código de Município dos Segmentos E, F e G\.

Pela regra atual do produto, os Quadros de Saídas dos Segmentos E, F e G somente são gerados se o Município Origem da NF for igual ao Código Município do cadastro do Estabelecimento, desconsiderando as demais Notas Fiscais\. O objetivo dessa demanda é passar a considerar o Município Origem da Nota Fiscal, visando corrigir as operações triangulares, referente as operações de transportes\.

__MFS59161__

Atualização da versão para 2021\.1

Disponibilizar a versão 2021\.1 no arquivo magnético

[__MFS59318__](https://jira.thomsonreuters.com/browse/MFS-59318)

Correção Item 3\.5 do Segmento C, D, E e F\.

O objetivo dessa demanda é incluir no cálculo de preenchimento do Item 3\.5 – Outras/Isentas e não tributadas, o valor de Base de Redução, que conforme regra do Manual “DIF”, deve ser preenchido com os valores das entradas de mercadorias, bens e/ou aquisições de serviços isentas ou não alcançadas pela incidência do imposto, considerar valores dos campos: Base Isenta \+ Base Outras \+ Base de Redução\.\(Replicado para os Segmentos D, E e F\)\. 

[__MFS__](https://jira.thomsonreuters.com/browse/MFS-58823)__60181__

Correção UF dos Segmentos D e F para Transporte

__RND4: __Alteração no Quadro Segmento D \(Totais por UF \- Entradas\):

Para notas fiscais de serviço de transporte, deve\-se apresentar a UF de Origem da Nota, ao invés da UF da Pessoa Fis/Jur\.

__RNF4__: Alteração no Quadro Segmento FSegmentofD \(Totais por UF \- SaídasEntradas\):

Para notas fiscais de serviço de transporte, deve\-se apresentar a UF de DestinoOrigem da Nota, ao invés da UF da Pessoa Fis/Jur\.

 Esta regra está implementada nos livros fiscais, do módulo ICMS, através do parâmetro 67, da Tela de Parâmetros por UF\. Essas regras estão implementadas nos livros fiscais, do módulo ICMS, através do parâmetro 67, da Tela de Parâmetros por UF\. 

Na DIF\-TO, essa regra será implementada considerando os CFOP’s e Naturezas de Operação parametrizados para Transporte nas opções de menu:

\- Parâmetros >> Parâmetros p/ Registros de Entrada \(COD\_PARAM = 533\)

\- Parâmetros >> Parâmetros p/ Registros de Saída \(COD\_PARAM 545\)\.

__MFS79175__

Atualização da versão para 2022\.1

__Disponibilizar a versão 2022\.1 no aquivo magnético__

__MFS80343__

Andréa Rocha

Alteração da forma de preencher o campo Número da Nota do Segmento I\.

__MFS93557__

Correção do critério de busca do Código de Município do Segmento G\.

Alteração da forma de preencher o campo de Código de Município de Origem Segmento G, para as Notas Fiscais de Utilities, para considerar o COD\_MUNIC\_CONSUMO da X42\.

__MFS462525__

Atualização da versão para 2023\.1

Disponibilizar a versão 2023\.1 no arquivo magnético

__MFS604398__

Atualização da versão para 2024\.1

Disponibilizar a versão 2024\.1 no arquivo magnético

__MFS766545__

Atualização da versão para 2025\.1

Disponibilizar a versão 2025\.1 no arquivo magnético

__MFS1053863__

Atualização da versão para 2026\.1

Disponibilizar a versão 2026\.1 no arquivo magnético

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

#### RGA

### Segmento A – Identificação do Contribuinte

### Deverá trazer uma linha de registro do Segmento A, pois se trata de informações do contribuinte\.

__OS2761\-A__

#### RNA1

### Campo Segmento

Conteúdo fixo igual a “A”

__OS2761\-A__

__RNA2__

###### Inscrição Estadual

Recuperar o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para a empresa e o estabelecimento que estão sendo gerados\.

__OS2761\-A__

__RNA3__

###### Período de referência

Preencher com o valor informado no campo ”ANO” da tela de geração do meio magnético \(Estadual – DIF TO – Obrigações – Meio Magnético\)\. Gravar no formato AAAA\.

__OS2761\-A__

__RNA4__

###### Retificação

Preencher com o valor informado no campo “Retificação” da tela de geração do meio magnético \(Estadual – DIF TO – Obrigações – Meio Magnético\)\. Gravar “S”, quando marcado e “N”, quando desmarcado\.

__OS2761\-A__

__RNA5__

###### Atividade econômica principal

Recuperar o campo COD\_ATIVIDADE da tabela ESTABELECIMENTO para a empresa e o estabelecimento que estão sendo gerados\.

__OS2761\-A__

__RNA6__

###### Tipo de estabelecimento

Recuperar o campo IND\_MATRIZ\_FILIAL da tabela ESTABELECIMENTO para o estabelecimento que está sendo gerado e gravar:

- “2”, se o conteúdo do campo for Matriz\.
- “3”, se o conteúdo do campo for Filial\.

Quando o parâmetro de Inscrição Estadual Única da tela de geração do meio magnético \(Estadual – DIF TO – tela Obrigações – Meio Magnético\) estiver marcado, informar o “1” quando o conteúdo do campo for Único\.

__OS2761\-A__

__RNA7__

__Finalidade__

Preencher com o valor informado no campo “Finalidade” da tela Parâmetros – Dados Iniciais, para o estabelecimento que está sendo gerado e gravar:

- Caso o campo possua a opção “Informação anual” selecionada, gravar “1”\.
- Caso o campo possua a opção “Baixa Voluntária” selecionada, gravar “2”\.
- Caso o campo possua a opção “Suspensão Voluntária” selecionada, gravar “4”\.

__OS2761\-A__

__RNA8__

__Tipo de escrituração__

Preencher com o valor informado no campo “Tipo de Escrituração” da tela Parâmetros – Dados Iniciais\.

- Caso o campo possua a opção “Fiscal” selecionada, gravar “1”\.
- Caso o campo possua a opção “Contábil” selecionada, gravar “2”\.

__OS2761\-A__

__RNA9__

__Regime de apuração__

Verificar o parâmetro “Optante Simples Nacional” na tela Parâmetros – Dados Iniciais\. Se estiver marcado, preencher o conteúdo do campo “__4__”, caso contrário, estiver desmarcado, será considerado Normal, então, preencher o conteúdo do campo “__3__”\.

__\[ALTERADA – MFS\-15858\]__

A partir da versão 2018\.1, campo Versão selecionado na tela de geração:

Se o campo “Optante Simples Nacional” estiver selecionado na tela Parâmetros – Dados Iniciais, ignorar a geração e emitir a mensagem de log: *“A partir da versão 2018 será aceito somente o Regime “3” – Normal, pois os contribuintes enquadrados no Simples Nacional não estarão mais obrigados a entregar a DIF TO”\.*

__OS2761\-A__

__MFS\-15858__

__RNA10__

__Código do município__

Essa informação deve ser a concatenação do Código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município do estabelecimento \(para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\)\.

__OS2761\-A__

__RNA11__

__Período Fiscal de referência inicial__

Conforme valor informado no campo “Ano” da tela de geração do meio magnético \(Estadual – DIF TO – tela Obrigações – Dados da Declaração\), deverá informar o dia/mês/ano de início de seleção dos registros do ano selecionado, ou seja, primeiro dia do ano da referência fiscal\.

Gravar no formato DDMMAAAA\.

__OS2761\-A__

__RNA12__

__Período Fiscal de referência final__

Conforme valor informado no campo “Ano” da tela de geração do meio magnético \(Estadual – DIF TO – tela Obrigações – Dados da Declaração\), deverá informar o dia/mês/ano final de seleção dos registros do ano selecionado, ou seja, último dia do ano da referência fiscal\.

Gravar no formato DDMMAAAA\.

__OS2761\-A__

__RNA13__

__CPF do contador__

Recuperar o CPF correspondente ao campo NUM\_CPF da tabela RESP\_CONTADOR referente ao contabilista escolhido no campo “Contabilista” da tela Parâmetros – Dados Iniciais\.

__OS2761\-A__

__RNA14__

__Responsável__

Recuperar o campo NOM\_RESPONSAVEL da tabela RESP\_INFORMACAO referente ao conteúdo escolhido no campo “Responsável” da tela Parâmetros – Dados Iniciais\.

__OS2761\-A__

__RNA15__

__Saldo inicial de caixa__

Preencher com o valor contido no campo “Saldo Inicial de Caixa” da tela Obrigações – Dados Anuais da Declaração\.

__OS2761\-A__

__RNA16__

__Saldo final de caixa__

Preencher com o valor contido no campo “Saldo Final de Caixa” da tela Obrigações – Dados Anuais da Declaração\.

__OS2761\-A__

__RNA17__

__Valor de patrimônio líquido__

Preencher com o valor contido no campo “Valor do patrimônio líquido” da tela Obrigações – Dados Anuais da Declaração\.

__OS2761\-A__

__RNA18__

__Houve mudança de domicílio__

Preencher com o valor informado do campo “Houve Mudança de Domicílio” da tela Obrigações – Dados Anuais da Declaração\. 

Gravar “S”, quando marcado e “N”, quando desmarcado\.

__OS2761\-A__

__RNA19__

__Versão__

Preencher o valor informado no campo “Versão” da tela Obrigações – Meio Magnético\.

Preencher o campo com “2012\.1”\.

__\[ALTERADA – CH268\_2013\]__

Preencher o valor informado no campo “Versão” da tela Obrigações – Meio Magnético\.

Preencher o campo com ‘2013\.1’\.

__\[ALTERADA – CH170\_2014\]__

Preencher com o valor informado no campo “Versão” da tela Obrigações – Meio Magnético\.

Preencher o campo com ‘2014\.1’\.

__\[ALTERADA – CH135\_2015\]__

Preencher com o valor informado no campo “Versão” da tela Obrigações – Meio Magnético\.

Preencher o campo com ‘2015\.1’\.

__\[ALTERADA – MFS8525\]__

Preencher com o valor informado no campo “Versão” da tela Obrigações – Meio Magnético\.

Preencher o campo com ‘2016\.1’\.

__\[ALTERADA – CH1960\_2017\]__

Preencher com o valor informado no campo “Versão” da tela Obrigações – Meio Magnético\.

Preencher o campo com ‘2017\.1’\.

__\[ALTERADA – MFS\-15858\]__

Preencher com o valor informado no campo “Versão” da tela Obrigações – Meio Magnético\.

Preencher o campo com ‘2018\.1’\.

__\[ALTERADA – MFS23835\]__

Preencher com o valor informado no campo “Versão” da tela Obrigações – Meio Magnético\.

Preencher o campo com ‘2019\.1’\.

__\[ALTERADA – MFS33858\]__

Preencher com o valor informado no campo “Versão” da tela Obrigações – Meio Magnético\.

Preencher o campo com ‘2020\.1’\.

__\[ALTERADA – MFS59161\]__

Preencher com o valor informado no campo “Versão” da tela Obrigações – Meio Magnético\.

Preencher o campo com ‘2021\.1’\.

\[ALTERADA \- MFS79175\]

Preencher com o valor informado no campo “Versão” da tela Obrigações – Meio Magnético\.

Preencher o campo com ‘2022\.1’\.

\[ALTERADA \- MFS462525\]

Preencher com o valor informado no campo “Versão” da tela Obrigações – Meio Magnético\.

Preencher o campo com ‘2023\.1’\.

\[__ALTERADA \- MFS604398__\]

Preencher com o valor informado no campo “Versão” da tela Obrigações – Meio Magnético\.

Preencher o campo com ‘2024\.1’\.

\[__ALTERADA \- MFS766545__\]

Preencher com o valor informado no campo “Versão” da tela Obrigações – Meio Magnético\.

Preencher o campo com ‘2025\.1’\.

\[__ALTERADA \- MFS1053863__\]

Preencher com o valor informado no campo “Versão” da tela Obrigações – Meio Magnético\.

Preencher o campo com ‘2026\.1’\.

__OS2761\-A/ CH268\_2013__

__CH170\_2014__

__CH135\_2015__

__MFS8525__

__CH1960\_2017__

__MFS\-15858__

__MFS23835__

__MFS33858__

__MFS59161__

__MFS79175__

__MFS462525__

__MFS604398__

__MFS766545__

__MFS1053863__

#### RGB

### Segmento B – Identificação da Mudança de Domicílio Fiscal do Contribuinte

Deverá trazer as linhas de registro dos domicílios fiscais e o período de referência, que a empresa esteve em cada município\. Deverá ser informado o Município Atual e até 4 \(quatro\) Municípios Anteriores, que por ventura a empresa tenha realizado suas atividades, no período do Exercício Fiscal Declarado,sendo que a linha “A”, será o “MUNICÍPIO ATUAL”, e as linhas “B”, “C”, “D” e “E”, serão os “MUNICÍPIOS ANTERIORES”, estado de Tocantins\.

Município Atual igual a “A”: informar o domicílio fiscal, “Município”, e o período de referência, “Intervalo de Data”, que a empresa está realizando suas atividades atualmente\.

Município Anterior igual a “B”, “C”, “D”, “E”: informar o\(s\) domicílio\(s\) fiscal \(is\), “Município\(s\)” e o\(s\) período\(s\) de referência\(s\), “Intervalo\(s\) de Data\(s\)”, que a empresa está realizando suas atividades anteriormente\.

Ex\.: 2\-Município Anterior: B – Palmas 01/01/2008 a 18/06/2008

Ex\.: 1\-Município Anterior: A – Alvorada 19/06/2008 a 31/12/2008

 

O usuário deverá efetuar a parametrização na tela de Dados Anuais da Declaração para que o arquivo magnético seja gerado com os municípios participantes no período de referência, caso não possua município cadastrado na parametrização, ou seja, o parâmetro “Houve mudança de domicílio” desmarcado, ao gerar o Meio Magnético deverá assumir o município atual do Estabelecimento\.

__OS2761\-A__

__RNB1__

__Segmento__

Conteúdo fixo igual a “B”

__OS2761\-A__

__RNB2__

__Inscrição Estadual__

Recuperar o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para a empresa e o estabelecimento que estão sendo gerados\.

__OS2761\-A__

__RNB3__

__Período de referência__

Preencher com o valor informado no campo ”ANO” da tela de geração do meio magnético \(Estadual – DIF TO – Obrigações – Meio Magnético\)\. Gravar no formato AAAA\.

__OS2761\-A__

__RNB4__

__Município atual e/ou anterior__

Deverá receber o conteúdo dos campos dos municípios de domicílio fiscal “A” de atual, “B“, “C”, “D” e/ou “E” para municípios anteriores\. O usuário deverá informar estes municípios na tela de “Dados Anuais da Declaração”, no menu Obrigações\.

Trazer o conteúdo do campo do Município \(A\) e se houver, o conteúdo dos demais Municípios “B“, “C”, “D” e/ou “E\. Respeitando a ordem de classificação do cadastro de municípios da tela\. Sendo primeiramente o Município Atual \(A\) subseqüente os municípios anteriores \(B\), \(C\), \(D\) e \(E\)\.

O conteúdo deste campo deverá ser a concatenação do Código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município do estabelecimento \(para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\)\.

__OS2761\-A__

__RNB5__

__Data Inicial da cidade atual e/ou anterior__

Deverá receber o conteúdo dos campos a data inicial de domicílio dos municípios “A” de atual, “B“, “C”, “D” e/ou “E” para municípios anteriores\. O usuário deverá informar as datas iniciais dos municípios na tela de “Dados Anuais da Declaração”, no menu Obrigações\.

Se encontrado o município conforme a regra __RNB4__, enviar a Data Inicial de cada município cadastrado na tela\. Respeitando a classificação sendo primeiramente o Município Atual \(A\) subseqüente os municípios anteriores \(B\), \(C\), \(D\) e \(E\)\. 

Exceto, quando não houver mudança de domicílio fiscal \(parâmetro desmarcado\), a data inicial do Município \(A\), deverá ser preenchida automática com o primeiro dia do ano de referência na geração da DIF\.

__OS2761\-A__

__RNB6__

__Data Final da cidade atual e/ou anterior__

Deverá receber o conteúdo dos campos a data final de domicílio dos municípios “A” de atual, “B“, “C”, “D” e/ou “E” para municípios anteriores\. O usuário deverá informar as datas finais dos municípios na tela de “Dados Anuais da Declaração”, no menu Obrigações\.

Se encontrado o município conforme a regra __RNB4__, enviar a Data Final de cada município cadastrado na tela\. Respeitando a classificação sendo primeiramente o Município Atual \(A\) subseqüente os municípios anteriores \(B\), \(C\), \(D\) e \(E\)\.

Exceto, quando não houver mudança de domicílio fiscal \(parâmetro desmarcado\), a data final do Município \(A\), deverá ser preenchida automática com o último dia do ano de referência na geração da DIF\.

__OS2761\-A__

__RNB7__

__Tipo de domicílio fiscal atual e/ou anterior__

Preencher com “__A__”, se encontrado conteúdo no campo Município Atual \(A\)\. 

Preencher com “__B__”, se encontrado conteúdo no campo Município Anterior \(B\)\.

Preencher com “__C__”, se encontrado conteúdo no campo Município Anterior \(C\)\.

Preencher com “__D__”, se encontrado conteúdo no campo Município Anterior \(D\)\.

Preencher com “__E__”, se encontrado conteúdo no campo Município Anterior \(E\)\.

__OS2761\-A__

#### RGC

##### Segmento C – Entradas de Mercadorias, Bens e/ou Aquisição de Serviços no Estabelecimento do Contribuinte 

Recuperar documentos fiscais \(SAFX07, SAFX08\) de entrada que possuam CFOP parametrizado na tela Parâmetros – Registros de Entrada → Por CFOP ou Por Extensão CFOP no módulo da DIF\-TO 

- Código da empresa = passado como parâmetro
- Código estabelecimento = passado como parâmetro
- Data de Fiscal = compreendida entre a data inicial e final do ano passado como parâmetro
- Movimento Entrada/Saída <> “9” 
- Classificação do documento fiscal deve ser 1 e 3
- Código do Município \(município\) e UF do estabelecimento gerador pertencente a Tocantins 
- Considerar apenas notas não canceladas\.
- Não considerar notas de transferência de crédito \(IND\_TRANSF\_CRED = 0\)
- Desconsiderar notas com situação especial iguais a 1, 2 ou 8\.
- Recuperar as notas fiscais com itens e as notas fiscais sem itens\.
- Recuperar as notas fiscais com CFOP e com CFOP/Extensão\.
- Agrupar por: CFOP x Município\.
- Ordenar por: Código Tipo de Entradas, Tipo de Domicílio e Cód\. Município\.
- Deverão ser selecionados somente registros que pertençam aos Municípios de Domicílio Fiscal cadastrados na tela de “Dados da Declaração” atual e/ou anteriores, no menu Obrigações, do estabelecimento passado como parâmetro, onde o campo IDENT\_ESTADO pertencente ao COD\_MUNICIPIO da tabela MUNICIPIO seja igual ao IDENT\_ESTADO da tabela ESTADO do estado de Tocantins\. A periodicidade da obrigação é anual, porém as regras de seleção dos registros deverão ser de acordo com o movimento de cada município no ano de referência\. A data inicial e a data final indicarão o período desta busca dos registros\.
- Quando o parâmetro __“*Geração Centralizada por Inscrição Estadual Única”*__ da Geração dos Registros estiver marcado, o somatório deverá considerar todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no modulo controle das obrigações estaduais\. \(Inventário e Documentário Fiscal\)\. As parametrizações deverão ser feitas sempre em nome do estabelecimento centralizador, inclusive para a geração dos registros, utilizar os municípios de domicílio fiscal do centralizador e apenas de UF Tocantins\.

__OS2761\-A__

__RNC1__

__Segmento__

Conteúdo fixo igual a “C”

__OS2761\-A__

__RNC2__

__Inscrição Estadual__

Recuperar o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para a empresa e o estabelecimento que estão sendo gerados\.

__OS2761\-A__

__RNC3__

__Período de referência__

Preencher com o valor informado no campo ”ANO” da tela de geração do meio magnético \(Estadual – DIF TO – Obrigações – Meio Magnético\)\. Gravar no formato AAAA\.

__OS2761\-A__

__RNC4__

__Código Tipo de Entradas__

Deverá ser recuperado o COD\_CFOP referente ao campo COD\_CFO a tabela SAFX07\. Conforme o preenchimento do parâmetro do Segmento C com “CFOPs” ou “Extensão CFOPs”, trazer neste campo os códigos compreendidos da __Lista de Tipo de Entrada\.__

Ex\.: Selecionado a quantidade de CFOPs com o tipo 01 – COMPRAS deverá trazer no campo o conteúdo do código “__01__”\.

A DIF\-TO possui uma lista própria de tipo de operações de entradas\. 

__OS2761\-A__

__RNC5__

__Tipo Domicílio Fiscal__

Preencher com “__A__”, se selecionado registros conforme a regra __RGC__ para o Município Atual \(A\)\. 

Preencher com “__B__”, se selecionado registros conforme a regra __RGC__ para o Município Anterior \(B\)\.

Preencher com “__C__”, se selecionado registros conforme a regra __RGC__ para o Município Anterior \(C\)\.

Preencher com “__D__”, se selecionado registros conforme a regra __RGC__ para o Município Anterior \(D\)\.

Preencher com “__E__”, se selecionado registros conforme a regra __RGC__ para o Município Anterior \(E\)\.

__OS2761\-A__

__RNC6__

__Código do Município__

Quando identificado o tipo de Domicílio Fiscal da regra de seleção do campo anterior \(__Tipo Domicílio Fiscal\-RNC5__\), este campo deverá deve ser preenchido com a concatenação do Código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município do estabelecimento \(para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\)\.

__ __

__OS2761\-A__

__RNC7__

__Valor Contábil__

Para as notas sem itens  o campo deve ser preenchido com o valor contábil da SAFX07 \(campo 23\-Valor Total da Nota\);

Para as notas com itens  neste caso deve\-se totalizar o valor contábil de todos os itens da nota, considerando o campo “64\-Valor Contábil Item” da SAFX08\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, esse campo deve ser igual ao campo Substituição Tributária RNC10\.

__OS2761\-A__

__RNC8__

__Base de Cálculo__

Para as notas sem itens  o campo deve ser preenchido com o valor da base do ICMS da SAFX07 \(campo 51\-Base Tributada ICMS\);

Para as notas com itens  neste caso deve\-se totalizar o valor da base de cálculo de todos os itens da nota, considerando o campo “56\-Base ICMS” da SAFX08\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

Se a regra “__RNC10__” item 3\.5 Substituição Tributária for preenchido desconsiderar o Valor de Base de Cálculo da Nota Fiscal\. Gravar zero nesse campo\.

__*Obs\**__* A inclusão dessa regra é necessária para evitar crítica no validador, uma vez que o programa soma as colunas, Base de Cálculo \+ Outras/Isentas não tributadas \+ Substituição Tributário e compara com a coluna de Valor Contábil,\(A somatória das colunas tem que ser igual ao Valor Contábil\)\.*

__OS2761\-A__

__MFS\-57993__

__RNC9__

__Outras/Isentas não Tributadas:__

__\[__[__MFS59318__](https://jira.thomsonreuters.com/browse/MFS-59318)__\] Considerar o campo Base de Redução no cálculo: __

__ __

Para as notas sem itens  o campo deve fazer o somatório do Valor das bases isenta/não tributada \+ base outras da SAFX07 \[campos 52 \+ 53\]\.  

__ __

Para as notas sem itens  o campo deve fazer o somatório do Valor das bases isenta/não tributada \+ base outras \+ base de redução da SAFX07 \[campos 52 \+ 53 \+ 54\]\.  

*\(Tabela: DWT\_DOCTO\_FISCAL: Campos: VLR\_BASE\_ICMS\_2 \+ VLR\_BASE\_ICMS\_3 \+ VLR\_BASE\_ICMS\_4*\)   

 

Para as notas com itens  o campo deve fazer o somatório do Valor das bases isenta/não tributada e outras da SAFX08: campo 56 \(se campo 55 = 2 ou 3\)\.

 

Para as notas com itens  o campo deve fazer o somatório do Valor das bases isenta/não tributada \+ base outras \+ base de redução da SAFX08: campo 56 \(se campo 55 = 2 ou 3 ou 4\)\.

*\(Tabela: DWT\_ITENS\_MERC: Campos: VLR\_BASE\_ICMS\_2 \+ VLR\_BASE\_ICMS\_3 \+ VLR\_BASE\_ICMS\_4*\)   

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

Se a regra “__RNC10__” item 3\.5 Substituição Tributária for preenchido desconsiderar os Valores das bases isenta/não tributada \+ base outras da Nota Fiscal\. Gravar zero nesse campo\.

__*Obs\**__* A inclusão dessa regra é necessária para evitar crítica no validador, uma vez que o programa soma as colunas, Base de Cálculo \+ Outras/Isentas não tributadas \+ Substituição Tributário e compara com a coluna de Valor Contábil,\(A somatória das colunas tem que ser igual ao Valor Contábil\)\.*

__OS2761\-A__

__MFS57993__

[__MFS59318__](https://jira.thomsonreuters.com/browse/MFS-59318)

__RNC10__

__Substituição Tributária__

Para as notas sem itens  o campo deve fazer o somatório do Valor da base ICMS\-ST da SAFX07 \[campo 64\]\.

Para as notas com itens  o campo deve fazer o somatório do Valor da base ICMS\-ST da SAFX08 \[campo 61\]\.

Para as notas com itens  Preencher com o Valor Contábil do Item \(campo VLR\_CONTAB\_ITEM\) da tabela X08\_ITENS\_MERC\.

     Se os campos Valor da Base ICMS\-ST \(campo VLR\_BASE\_ICMSS\), ou Valor Base Isento de ICMS\-ST \(campo VLR\_BASE\_ICMSS\_2\) ou Valor Base Outras de ICMS\-ST \(campo VLR\_BASE\_ICMSS\_3\) da tabela DWT\_ITENS\_MERC, estiverem preenchidos\.

__ __

__OS2761\-A__

__MFS\-57993__

__RGD__

##### Segmento D – Entradas de Mercadorias, Bens e/ou Aquisição de Serviços, Detalhadas \(por Unidade da Federação\) 

Recuperar documentos fiscais \(SAFX07, SAFX08\) de entrada que possuam CFOP parametrizado na tela Parâmetros – Registros de Entrada → Por CFOP ou Por Extensão CFOP no módulo da DIF\-TO 

- Código da empresa = passado como parâmetro
- Código estabelecimento = passado como parâmetro
- Data de Fiscal = compreendida entre a data inicial e final do ano passado como parâmetro
- Movimento Entrada/Saída <> “9” 
- Classificação do documento fiscal deve ser 1 e 3 
- Código do Município \(município\) e UF do estabelecimento gerador pertencente a Tocantins
- Considerar apenas notas não canceladas\.
- Considerar notas que sejam de transferência\.
- Desconsiderar notas com situação especial iguais a 1, 2 ou 8\.
- Recuperar as notas fiscais com itens e as notas fiscais sem itens\.
- Recuperar as notas fiscais com CFOP e com CFOP/Extensão\.
- Agrupar por: UF x Município 
- Ordenar por: Código UF, Tipo de Domicílio e Cód\. Município
- Deverão ser selecionados somente registros que pertençam aos Municípios de Domicílio Fiscal cadastrados na tela de “Dados Anuais da Declaração”, no menu Obrigações, do estabelecimento passado como parâmetro, onde o campo IDENT\_ESTADO pertencente ao COD\_MUNICIPIO da tabela MUNICIPIO seja igual ao IDENT\_ESTADO da tabela ESTADO do estado de Tocantins\. A periodicidade da obrigação é anual, porém as regras de seleção dos registros deverão ser de acordo com o movimento de cada município no ano de referência\. A data inicial e a data final indicarão o período desta busca dos registros\.
- Quando o parâmetro __“*Geração Centralizada por Inscrição Estadual Única”*__ da Geração dos Registros estiver marcado, o somatório deverá considerar todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no modulo controle das obrigações estaduais\. \(Inventário e Documentário Fiscal\)\. As parametrizações deverão ser feitas sempre em nome do estabelecimento centralizador, inclusive para a geração dos registros, utilizar os municípios de domicílio fiscal do centralizador e apenas de UF Tocantins\.

__OS2761\-A__

__RND1__

__Segmento__

Conteúdo fixo igual a “D”

__OS2761\-A__

__RND2__

__Inscrição Estadual__

Recuperar o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para a empresa e o estabelecimento que estão sendo gerados\.

__OS2761\-A__

__RND3__

__Período de referência__

Preencher com o valor informado no campo ”ANO” da tela de geração do meio magnético \(Estadual – DIF TO – Obrigações – Meio Magnético\)\. Gravar no formato AAAA\.

__OS2761\-A__

__RND4__

__Código UF__

__\[__[__MFS__](https://jira.thomsonreuters.com/browse/MFS-58823)__60181\] Inclusão de Tratamento para Serviços de Transporte__

Considerar o “Tipo da Entrada” que o CFOP ou CFOP/Natureza da Operação da nota foi parametrizado na opção de menu Parâmetros >> Parâmetros p/ Registros de Entrada\.

__Se o “Tipo da Entrada” for diferente de Transporte \(COD\_PARAM <> 533\), então:__

Recuperar o campo COD\_UF\_OBRIG da tabela PRT\_UF\_OBRIG\_MSAF \(TACES63\) referente ao IDENT\_ESTADO cadastrado na tabela ESTADO pertencente a UF da PFJ \(campo 19 da SAFX04\) do documento fiscal\.

__Se o “Tipo da Entrada” for igual a Transporte \(COD\_PARAM = 533\), então:__

Recuperar o campo COD\_UF\_OBRIG da tabela PRT\_UF\_OBRIG\_MSAF \(TACES63\) referente ao IDENT\_ESTADO cadastrado na tabela ESTADO pertencente a UF Origem da Capa da Nota \(campo 117 \- UF\_ORIG\_DEST da SAFX07\)\.

Obs: esta regra é feita nos livros fiscais do módulo ICMS, através do tratamento do parâmetro 67\.

Utilizar o COD\_MODULO igual 265 da DIF\-TO\.

__OS2761\-A__

[__MFS__](https://jira.thomsonreuters.com/browse/MFS-58823)__60181__

__RND5__

__Tipo Domicílio Fiscal__

Preencher com “__A__”, se selecionado registros conforme a regra __RGD__ para o Município Atual \(A\)\. 

Preencher com “__B__”, se selecionado registros conforme a regra __RGD__ para o Município Anterior \(B\)\.

Preencher com “__C__”, se selecionado registros conforme a regra __RGD__ para o Município Anterior \(C\)\.

Preencher com “__D__”, se selecionado registros conforme a regra __RGD__ para o Município Anterior \(D\)\.

Preencher com “__E__”, se selecionado registros conforme a regra __RGD__ para o Município Anterior \(E\)\.

__OS2761\-A__

__RND6__

__Código do Município__

Quando identificado o tipo de Domicílio Fiscal da regra de seleção do campo anterior \(__Tipo Domicílio Fiscal\-RND5__\), este campo deverá deve ser preenchido com a concatenação do Código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município do estabelecimento \(para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\)\.

__OS2761\-A__

__RND7__

__Valor Contábil__

Para as notas sem itens  o campo deve ser preenchido com o valor contábil da SAFX07 \(campo 23\-Valor Total da Nota\);

Para as notas com itens  neste caso deve\-se totalizar o valor contábil de todos os itens da nota, considerando o campo “64\-Valor Contábil Item” da SAFX08\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, esse campo deve ser igual ao campo Substituição Tributária RND12\.

__OS2761\-A__

__RND8__

__Base de Cálculo__

Para as notas sem itens  o campo deve ser preenchido com o valor da base do ICMS da SAFX07 \(campo 51\-Base Tributada ICMS\);

Para as notas com itens  neste caso deve\-se totalizar o valor da base de cálculo de todos os itens da nota, considerando o campo “56\-Base ICMS” da SAFX08\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__OS2761\-A__

__RND9__

__Outras/Isentas não Tributadas:__

__\[__[__MFS59318__](https://jira.thomsonreuters.com/browse/MFS-59318)__\] Considerar o campo Base de Redução no cálculo: __

__ __

Para as notas sem itens  o campo deve fazer o somatório do Valor das bases isenta/não tributada \+ base outras da SAFX07 \[campos 52 \+ 53\]\.  

__ __

Para as notas sem itens  o campo deve fazer o somatório do Valor das bases isenta/não tributada \+ base outras \+ base de redução da SAFX07 \[campos 52 \+ 53 \+ 54\]\.  

*\(Tabela: DWT\_DOCTO\_FISCAL: Campos: VLR\_BASE\_ICMS\_2 \+ VLR\_BASE\_ICMS\_3 \+ VLR\_BASE\_ICMS\_4*\)   

 

Para as notas com itens  o campo deve fazer o somatório do Valor das bases isenta/não tributada e outras da SAFX08: campo 56 \(se campo 55 = 2 ou 3\)\.

 

Para as notas com itens  o campo deve fazer o somatório do Valor das bases isenta/não tributada \+ base outras \+ base de redução da SAFX08: campo 56 \(se campo 55 = 2 ou 3 ou 4\)\.

*\(Tabela: DWT\_ITENS\_MERC: Campos: VLR\_BASE\_ICMS\_2 \+ VLR\_BASE\_ICMS\_3 \+ VLR\_BASE\_ICMS\_4*\)   

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__OS2761\-A__

[__MFS59318__](https://jira.thomsonreuters.com/browse/MFS-59318)

__RND10__

__Petróleo/Energia__

Quando o produto \(campo 14 – SAFX08\) do documento fiscal tiver a classificação do produto, campo 25 \- IND\_CLASSIF\_ICMSS da SAFX2013 igual a 2 OU 3, deverá fazer o somatório do Valor do ICMS\-ST da SAFX08 \[campo 2\]\.

__OS2761\-A__

__RND11__

__Outros Produtos__

Quando o produto \(campo 14 – SAFX08\) do documento fiscal tiver a classificação do produto, campo 25 \- IND\_CLASSIF\_ICMSS da SAFX2013 diferente 2 e 3, deverá fazer o somatório do Valor do ICMS\-ST da SAFX08 \[campo 52\]\.

__OS2761\-A__

__RND12__

__Substituição Tributária__

Para as notas sem itens  o campo deve fazer o somatório do Valor da base ICMS\-ST da SAFX07 \[campo 64\]\.

Para as notas com itens  o campo deve fazer o somatório do Valor da base ICMS\-ST da SAFX08 \[campo 61\]\.

__OS2761\-A__

__RGE__

##### Segmento E – Saídas de Mercadorias, Bens e/ou Prestações de Serviços no Estabelecimento do Contribuinte 

Regra PRESTAÇÃO DE SERVIÇOS DE ENERGIA ELÉTRICA, COMUNICAÇÃO OU ÁGUA

Recuperar documentos fiscais \(SAFX42 e SAFX43\) de saída que possuam CFOP parametrizado na tela Parâmetros – Registros de Saída → Por CFOP ou Por Extensão CFOP no módulo da DIF\-TO 

- Código da empresa = passado como parâmetro
- Código estabelecimento = passado como parâmetro
- Data de Fiscal = compreendida entre a data inicial e final do ano passado como parâmetro
- Classificação do documento fiscal deve ser 1 e 3
- Estado deve ser igual ao do estabelecimento
- Considerar apenas notas não canceladas\.
- Desconsiderar notas com situação especial iguais a 1\.
- Recuperar as notas fiscais com itens e as notas fiscais sem itens\.
- Recuperar as notas fiscais com CFOP\.
- Campo “Ponto de Consumo / Terminal Faturado” preenchido com “UF” e “Município”\.
- Quando o parâmetro “__*Considerar Município do Ponto de Consumo \(Utilities\)”*__ da Geração do Meio Magnético estiver  marcado, deverão ser considerados os Documentos Fiscais de Utilities \(SAFX42/43\), com as seguintes características: 
- Modelo de Documento = 06 – Nota Fiscal/Conta de Energia Elétrica, 
- Modelo de Documento = 21 – Nota Fiscal de Serviço de Comunicação ou 22 – Nota Fiscal de Serviço de Telecomunicações
- Não considerar os documentos gerados pelo Mapa Resumo, quando o parâmetro “__*Considerar Município do Ponto de Consumo \(Utilities\)*__” estiver marcado\. 
- Quando não estiver marcado, permanece o comportamento atual\. Estas condições deverão ser aplicadas tanto na geração normal quanto à Geração por Inscrição Estadual Única\.

__OS2761\-A__

Regra DEMAIS DOCUMENTOS FISCAIS

__\[__[__MFS58823__](https://jira.thomsonreuters.com/browse/MFS-58823)__\] __

Alteração para retirar a restrição de só considerar Nota com UF/COD\_MUNICIPIO igual ao do Estabelecimento

Recuperar documentos fiscais \(SAFX07, SAFX08\) de saída que possuam CFOP parametrizado na tela Parâmetros – Registros de Saída → Por CFOP ou Por Extensão CFOP no módulo da DIF\-TO 

- Código da empresa = passado como parâmetro
- Código estabelecimento = passado como parâmetro
- Data de Fiscal = compreendida entre a data inicial e final do ano passado como parâmetro
- Movimento Entrada/Saída igual a “9” 
- Classificação do documento fiscal deve ser 1, 3 e 4
- Código do Município \(município\) e UF do estabelecimento gerador pertencente a Tocantins
- Considerar apenas notas não canceladas\.
- Considerar notas que sejam de transferência\.
- Desconsiderar notas com situação especial iguais a 1, 2 ou 8\.
- Recuperar as notas fiscais com itens e as notas fiscais sem itens\.
- Recuperar as notas fiscais com CFOP e com CFOP/Extensão\.
- Agrupar por: CFOP x Município\.  
- Ordenar por: Cód\.Tipo de Saídas, Tipo de Domicílio e Cód\. Município\.
- Deverão ser selecionados somente registros que pertençam aos Municípios de Domicílio Fiscal cadastrados na tela de “Dados Anuais da Declaração”, no menu Obrigações, do estabelecimento passado como parâmetro, onde o campo IDENT\_ESTADO pertencente ao COD\_MUNICIPIO da tabela MUNICIPIO seja igual ao IDENT\_ESTADO da tabela ESTADO do estado de Tocantins\. A periodicidade da obrigação é anual, porém as regras de seleção dos registros deverão ser de acordo com o movimento de cada município no ano de referência\. A data inicial e a data final indicarão o período desta busca dos registros\.
- Deverão ser selecionados os registros que pertençam ou não aos Municípios de Domicílio Fiscal cadastrados na tela de “Dados Anuais da Declaração”\. A periodicidade da obrigação é anual, porém as regras de seleção dos registros deverão ser de acordo com o movimento de cada município no ano de referência\. A data inicial e a data final indicarão o período desta busca dos registros\.

__Obs\* __A regra anterior desprezava a Nota Fiscal caso o campo COD\_MUNICIPIO do Estabelecimento fosse diferente do COD\_MUNICIPIO\_ORIG da Nota Fiscal\. Com a alteração o programa irá considerar quando for igual e diferente, agrupando as Notas Fiscais, utilizando a informação do COD\_MUNICIPIO do Estabelecimento\.

- Quando Prestação de Serviço de Transporte \[\(Código de Saída \(campo 4\) igual a “6”\], o Código do Município que tem que estar preenchido é o código do município origem, da capa do documento para ser recuperado\.
- Quando o parâmetro __“*Geração Centralizada por Inscrição Estadual Única”*__ da Geração dos Registros estiver marcado, o somatório deverá considerar todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no modulo controle das obrigações estaduais\. \(Inventário e Documentário Fiscal\)\. As parametrizações deverão ser feitas sempre em nome do estabelecimento centralizador, inclusive para a geração dos registros, utilizar os municípios de domicílio fiscal do centralizador e apenas de UF Tocantins\.

[__MFS\-58823__](https://jira.thomsonreuters.com/browse/MFS-58823)

__RNE1__

__Segmento__

Conteúdo fixo igual a “E”

__OS2761\-A__

__RNE2__

__Inscrição Estadual__

Recuperar o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para a empresa e o estabelecimento que estão sendo gerados\.

__OS2761\-A__

__RNE3__

__Período de referência__

Preencher com o valor informado no campo ”ANO” da tela de geração do meio magnético \(Estadual – DIF TO – Obrigações – Meio Magnético\)\. Gravar no formato AAAA\.

__OS2761\-A__

__RNE4__

__Código Tipo de Saídas__

Deverá ser recuperado o COD\_CFOP referente ao campo IDENT\_CFO a tabela SAFX07\. Conforme o preenchimento do parâmetro do Segmento E com “CFOPs” ou “Extensão CFOPs”, trazer neste campo os códigos compreendidos da Lista de Tipo de Saída\.

Ex\.: Selecionado a quantidade de CFOPs com o tipo 01 – VENDAS, deverá trazer no campo o conteúdo do código “__01__”\.

A DIF\-TO possui uma lista própria de tipo de operações de saídas\.

__OS2761\-A__

__RNE5__

__Tipo Domicílio Fiscal__

Preencher com “__A__”, se selecionado registros conforme a regra __RGE__ para o Município Atual \(A\)\. 

Preencher com “__B__”, se selecionado registros conforme a regra __RGE__ para o Município Anterior \(B\)\.

Preencher com “__C__”, se selecionado registros conforme a regra __RGE__ para o Município Anterior \(C\)\.

Preencher com “__D__”, se selecionado registros conforme a regra __RGE__ para o Município Anterior \(D\)\.

Preencher com “__E__”, se selecionado registros conforme a regra __RGE__ para o Município Anterior \(E\)\.

__OS2761\-A__

__RNE6__

__Código do Município__

Quando identificado o tipo de Domicílio Fiscal da regra de seleção do campo anterior \(__Tipo Domicílio Fiscal\-RNE5__\), este campo deverá deve ser preenchido com a concatenação do Código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município do estabelecimento \(para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\)\.

__OS2761\-A__

__RNE7__

__Valor Contábil__

Para as notas sem itens  o campo deve ser preenchido com o valor contábil da SAFX07 \(campo 23\-Valor Total da Nota\);

Para as notas com itens  neste caso deve\-se totalizar o valor contábil de todos os itens da nota, considerando o campo “64\-Valor Contábil Item” da SAFX08\.

Para as notas de utilities da SAFX43  o campo deve ser preenchido com o valor dos serviços deduzindo o valor dos descontos \(campo 19 – campo 18\)\. 

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, esse campo deve ser igual ao campo Substituição Tributária RNE10\.

__OS2761\-A__

__RNE8__

__Base de Cálculo__

Para as notas sem itens  o campo deve ser preenchido com o valor da base do ICMS da SAFX07 \(campo 51\-Base Tributada ICMS\);

Para as notas com itens  neste caso deve\-se totalizar o valor da base de cálculo de todos os itens da nota, considerando o campo “56\-Base ICMS” da SAFX08\.

Para as notas de utilities da SAFX43  o campo deve ser preenchido com a base de cálculo \(campo 23\)\. 

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__OS2761\-A__

__RNE9__

__Outras/Isentas não Tributadas:__

__\[__[__MFS59318__](https://jira.thomsonreuters.com/browse/MFS-59318)__\] Considerar o campo Base de Redução no cálculo: __

__ __

Para as notas sem itens  o campo deve fazer o somatório do Valor das bases isenta/não tributada \+ base outras da SAFX07 \[campos 52 \+ 53\]\.  

__ __

Para as notas sem itens  o campo deve fazer o somatório do Valor das bases isenta/não tributada \+ base outras \+ base de redução da SAFX07 \[campos 52 \+ 53 \+ 54\]\.  

*\(Tabela: DWT\_DOCTO\_FISCAL: Campos: VLR\_BASE\_ICMS\_2 \+ VLR\_BASE\_ICMS\_3 \+ VLR\_BASE\_ICMS\_4*\)   

 

Para as notas com itens  o campo deve fazer o somatório do Valor das bases isenta/não tributada e outras da SAFX08: campo 56 \(se campo 55 = 2 ou 3\)\.

 

Para as notas com itens  o campo deve fazer o somatório do Valor das bases isenta/não tributada \+ base outras \+ base de redução da SAFX08: campo 56 \(se campo 55 = 2 ou 3 ou 4\)\.

*\(Tabela: DWT\_ITENS\_MERC: Campos: VLR\_BASE\_ICMS\_2 \+ VLR\_BASE\_ICMS\_3 \+ VLR\_BASE\_ICMS\_4*\)   

Para as notas de utilities da SAFX43  o campo deve ser preenchido com a base de outras/isentas e não tributadas \(campo 24 \+ 25\)\. 

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__OS2761\-A__

[__MFS59318__](https://jira.thomsonreuters.com/browse/MFS-59318)

__RNE10__

__Substituição Tributária__

Para as notas sem itens  o campo deve fazer o somatório do Valor da base ICMS\-ST da SAFX07 \[campo 64\]\.

Para as notas com itens  o campo deve fazer o somatório do Valor da base ICMS\-ST da SAFX08 \[campo 61\]\.

Para as notas de utilities da SAFX43  o campo deve ser preenchido com a base de substituição tributária \(campo 40\)\. 

__OS2761\-A__

__RGF__

##### Segmento F – Saídas de Mercadorias, Bens e/ou Prestações de Serviços, Detalhadas \(por Unidade da Federação\) 

Regra PRESTAÇÃO DE SERVIÇOS DE ENERGIA ELÉTRICA, COMUNICAÇÃO OU ÁGUA

Recuperar documentos fiscais \(SAFX42 e SAFX43\) de saída que possuam CFOP parametrizado na tela Parâmetros – Registros de Saída → Por CFOP ou Por Extensão CFOP no módulo da DIF\-TO 

- Código da empresa = passado como parâmetro
- Código estabelecimento = passado como parâmetro
- Data de Fiscal = compreendida entre a data inicial e final do ano passado como parâmetro
- Classificação do documento fiscal deve ser 1 e 3
- Estado deve ser igual ao do estabelecimento
- Considerar apenas notas não canceladas\.
- Desconsiderar notas com situação especial iguais a 1\.
- Recuperar as notas fiscais com itens e as notas fiscais sem itens\.
- Recuperar as notas fiscais com CFOP\.
- Campo “Ponto de Consumo / Terminal Faturado” preenchido com “UF” e “Município”\.
- Quando o parâmetro “__*Considerar Município do Ponto de Consumo \(Utilities\)”*__ da Geração do Meio Magnético estiver  marcado, deverão ser considerados os Documentos Fiscais de Utilities \(SAFX42/43\), com as seguintes características: 
- Modelo de Documento = 06 – Nota Fiscal/Conta de Energia Elétrica, 
- Modelo de Documento = 21 – Nota Fiscal de Serviço de Comunicação ou 22 – Nota Fiscal de Serviço de Telecomunicações
- Não considerar os documentos gerados pelo Mapa Resumo, quando o parâmetro “__*Considerar Município do Ponto de Consumo \(Utilities\)*__” estiver marcado\. 
- Quando não estiver marcado, permanece o comportamento atual\. Estas condições deverão ser aplicadas tanto na geração normal quanto à Geração por Inscrição Estadual Única\.

__OS2761\-A__

Regra DEMAIS DOCUMENTOS FISCAIS

__\[__[__MFS58823__](https://jira.thomsonreuters.com/browse/MFS-58823)__\] __

Alteração para retirar a restrição de só considerar Nota com UF/COD\_MUNICIPIO igual ao do Estabelecimento\.

Recuperar documentos fiscais \(SAFX07, SAFX08\) de saída que possuam CFOP parametrizado na tela Parâmetros – Registros de Saída → Por CFOP ou Por Extensão CFOP no módulo da DIF\-TO 

- Código da empresa = passado como parâmetro
- Código estabelecimento = passado como parâmetro
- Data de Fiscal = compreendida entre a data inicial e final do ano passado como parâmetro
- Movimento Entrada/Saída igual a “9” 
- Classificação do documento fiscal deve ser 1, 3 e 4
- Código do Município \(município\) e UF do estabelecimento gerador pertencente a Tocantins
- Considerar apenas notas não canceladas\.
- Não considerar notas de transferência de crédito \(IND\_TRANSF\_CRED = 0\)
- Desconsiderar notas com situação especial iguais a 1, 2 ou 8\.
- Recuperar as notas fiscais com itens e as notas fiscais sem itens\.
- Recuperar as notas fiscais com CFOP e com CFOP/Extensão\.
- Agrupar por: UF x Município 
- Ordenar por: Código UF, Tipo de Domicílio e Cód\. Município\.
- Deverão ser selecionados somente registros que pertençam aos Municípios de Domicílio Fiscal cadastrados na tela de “Dados Anuais da Declaração”, no menu Obrigações, do estabelecimento passado como parâmetro, onde o campo IDENT\_ESTADO pertencente ao COD\_MUNICIPIO da tabela MUNICIPIO seja igual ao IDENT\_ESTADO da tabela ESTADO do estado de Tocantins\. A periodicidade da obrigação é anual, porém as regras de seleção dos registros deverão ser de acordo com o movimento de cada município no ano de referência\. A data inicial e a data final indicarão o período desta busca dos registros\.
- Deverão ser selecionados os registros que pertençam ou não aos Municípios de Domicílio Fiscal cadastrados na tela de “Dados Anuais da Declaração”\. A periodicidade da obrigação é anual, porém as regras de seleção dos registros deverão ser de acordo com o movimento de cada município no ano de referência\. A data inicial e a data final indicarão o período desta busca dos registros\.

__Obs\* __A regra anterior desprezava a Nota Fiscal caso o campo COD\_MUNICIPIO do Estabelecimento fosse diferente do COD\_MUNICIPIO\_ORIG da Nota Fiscal\. Com a alteração o programa irá considerar quando for igual e diferente, considerando as informações de UF\_ORIG\_DEST/COD\_MUNICIPIO\_ORIG da Nota Fiscal\.

- Quando Prestação de Serviço de Transporte \[\(Parâmetro CFOP/Extensão com o tipo Código de Saída igual a “6”\], o Código do Município que tem que estar preenchido é o código do município origem, da capa do documento para ser recuperado\.
- Quando o parâmetro __“*Geração Centralizada por Inscrição Estadual Única”*__ da Geração dos Registros estiver marcado, o somatório deverá considerar todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no modulo controle das obrigações estaduais\. \(Inventário e Documentário Fiscal\)\. As parametrizações deverão ser feitas sempre em nome do estabelecimento centralizador, inclusive para a geração dos registros, utilizar os municípios de domicílio fiscal do centralizador e apenas de UF Tocantins\.

[__MFS\-58823__](https://jira.thomsonreuters.com/browse/MFS-58823)

__RNF1__

__Segmento__

Conteúdo fixo igual a “F”

__OS2761\-A__

__RNF2__

__Inscrição Estadual__

Recuperar o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para a empresa e o estabelecimento que estão sendo gerados\.

__OS2761\-A__

__RNF3__

__Período de referência__

Preencher com o valor informado no campo ”ANO” da tela de geração do meio magnético \(Estadual – DIF TO – Obrigações – Meio Magnético\)\. Gravar no formato AAAA\.

__OS2761\-A__

__RNF4__

__Código UF__

\[[__MFS__](https://jira.thomsonreuters.com/browse/MFS-58823)__60181\] Inclusão de Tratamento para Serviços de Transporte__

Considerar o “Tipo de Saída” que o CFOP ou CFOP/Natureza da Operação da nota foi parametrizado na opção de menu Parâmetros >> Parâmetros p/ Registros de Saída\.

__Se o “Tipo de Saída” for diferente de Transporte \(COD\_PARAM <> 545\), então:__

Recuperar o campo COD\_UF\_OBRIG da tabela PRT\_UF\_OBRIG\_MSAF \(TACES63\) referente ao IDENT\_ESTADO cadastrado na tabela ESTADO pertencente a UF da PFJ \(campo 19 da SAFX04\) do documento fiscal\.

__Se o “Tipo de Saída” for igual a Transporte \(COD\_PARAM = 545\), então:__

Recuperar o campo COD\_UF\_OBRIG da tabela PRT\_UF\_OBRIG\_MSAF \(TACES63\) referente ao IDENT\_ESTADO cadastrado na tabela ESTADO pertencente a UF Destino da Capa da Nota \(campo 122 \- UF\_DESTINO da SAFX07\)\.

Obs: esta regra é feita nos livros fiscais do módulo ICMS, através do tratamento do parâmetro 67\.

Utilizar o COD\_MODULO igual 265 da DIF\-TO\.

__OS2761\-A__

[__MFS__](https://jira.thomsonreuters.com/browse/MFS-58823)__60181__

__RNF5__

__Tipo Domicílio Fiscal__

Preencher com “__A__”, se selecionado registros conforme a regra __RGF__ para o Município Atual \(A\)\. 

Preencher com “__B__”, se selecionado registros conforme a regra __RGF__ para o Município Anterior \(B\)\.

Preencher com “__C__”, se selecionado registros conforme a regra __RGF__ para o Município Anterior \(C\)\.

Preencher com “__D__”, se selecionado registros conforme a regra __RGF__ para o Município Anterior \(D\)\.

Preencher com “__E__”, se selecionado registros conforme a regra __RGF__ para o Município Anterior \(E\)\.

__OS2761\-A__

__RNF6__

__Código do Município__

Quando identificado o tipo de Domicílio Fiscal da regra de seleção do campo anterior \(__Tipo Domicílio Fiscal\-RNF5__\), este campo deverá deve ser preenchido com a concatenação do Código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município do estabelecimento \(para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\)\.

__OS2761\-A__

__RNF7__

__Valor Contábil Contribuinte__

__\[ALTERADA – CH9620\_2017 \(MFS\-11647\)\]__

Preencher este campo quando o parâmetro “__Identificação do Contribuinte Final__” da tela de Dados Anuais da Declaração estiver com a opção de “*pelo Indicador da Nota*” \(que considera campo 29\-CONTRIB\_FINAL igual a “__S__” da SAFX07 e campo 85\-IND\_CONS\_FINAL igual a “__S__” da SAFX42\)\. 

Para as notas sem itens  o campo deve ser preenchido com o valor contábil da SAFX07 \(campo 23\-Valor Total da Nota\);

Para as notas com itens  neste caso deve\-se totalizar o valor contábil de todos os itens da nota, considerando o campo “64\-Valor Contábil Item” da SAFX08;

Para as notas de utilities da SAFX43  o campo deve ser preenchido com o valor dos serviços deduzindo o valor dos descontos \(campo 19 – campo 18\)\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, esse campo deve ser igual ao campo Substituição Tributária RNF12\.

__OS2761\-A__

__CH9620\_2017 \(MFS\-11647\)__

__RNF8__

__Valor Contábil Não Contribuinte__

Preencher este campo quando o parâmetro “__Identificação do Contribuinte Final__” da tela de Dados Anuais da Declaração estiver com a opção de “*pelo Indicador da Nota*” \(que considera campo 29\-CONTRIB\_FINAL igual a “__N__” da SAFX07 e campo 85\-IND\_CONS\_FINAL igual a “__N__” da SAFX42\)\. 

Para as notas sem itens  o campo deve ser preenchido com o valor contábil da SAFX07 \(campo 23\-Valor Total da Nota\);

Para as notas com itens  neste caso deve\-se totalizar o valor contábil de todos os itens da nota, considerando o campo “64\-Valor Contábil Item” da SAFX08;

Para as notas de utilities  o campo deve ser preenchido com o valor dos serviços deduzindo o valor dos descontos \(campo 19 – campo 18 da SAFX43\)\.

Caso contrário, se o parâmetro estiver com “*pelo CFOP*”, totalizar o campo Valor Total da Nota \(23\-SAFX07 e 17\-SAFX42\), dos documentos fiscais selecionados através da lista considerando os CFOP’s: 618', '619', '645', '653', '663', '5258', '5307', '5357', '6107','6108', '6258','6307','6357', caso contrário, preencher com zeros\.

__OS2761\-A__

__RNF9__

__Base de Cálculo Contribuinte__

__\[ALTERADA – CH9620\_2017 \(MFS\-11647\)\]__

Preencher este campo quando o parâmetro “__Identificação do Contribuinte Final__” da tela de Dados Anuais da Declaração estiver com a opção de “*pelo Indicador da Nota*” \(que considera campo 29\-CONTRIB\_FINAL igual a “__S__” da SAFX07 e campo 85\-IND\_CONS\_FINAL igual a “__S__” da SAFX42\)\. 

Para as notas sem itens  o campo deve\-se totalizar o valor da base do ICMS da SAFX07 \(campo 51\-Base Tributada ICMS\);

Para as notas com itens  neste caso deve\-se totalizar o valor da base de cálculo de todos os itens da nota, considerando o campo “56\-Base ICMS” da SAFX08\.

Para as notas de utilities da SAFX43  o campo deve ser preenchido com a base de cálculo \(campo 23\)\. 

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__OS2761\-A__

__CH9620\_2017 \(MFS\-11647\)__

__RNF10__

__Base de Cálculo Não Contribuinte__

Preencher este campo quando o parâmetro “__Identificação do Contribuinte Final__” da tela de Dados Anuais da Declaração estiver com a opção de “*pelo Indicador da Nota*” \(que considera campo 29\-CONTRIB\_FINAL igual a “__N__” da SAFX07 e campo 85\-IND\_CONS\_FINAL igual a “__N__” da SAFX42\)\. 

Para as notas sem itens  o campo deve\-se totalizar o valor da base do ICMS da SAFX07 \(campo 51\-Base Tributada ICMS\);

Para as notas com itens  neste caso deve\-se totalizar o valor da base de cálculo de todos os itens da nota, considerando o campo “56\-Base ICMS” da SAFX08;

Para as notas de utilities  o campo deve ser preenchido com a base de cálculo \(campo 23 da SAFX43\)\. 

Caso contrário, se o parâmetro estiver com “pelo CFOP”, totalizar o campo Valor Total da Nota \(23\-SAFX07 e 22\-SAFX42\), dos documentos fiscais selecionados através do parâmetro do Segmento F de CFOP e/ou CFOP/Natureza\. Considerando os CFOP’s: ‘618', '619','645','653','663','5258','5307','5357','6107','6108', '6258','6307','6357', caso contrário, preencher com zeros\.

__OS2761\-A__

__RNF11__

__Outras/Isentas não Tributadas: __

__\[__[__MFS59318__](https://jira.thomsonreuters.com/browse/MFS-59318)__\] Considerar o campo Base de Redução no cálculo: __

__ __

Para as notas sem itens  o campo deve fazer o somatório do Valor das bases isenta/não tributada \+ base outras da SAFX07 \[campos 52 \+ 53\]\.  

__ __

Para as notas sem itens  o campo deve fazer o somatório do Valor das bases isenta/não tributada \+ base outras \+ base de redução da SAFX07 \[campos 52 \+ 53 \+ 54\]\.  

*\(Tabela: DWT\_DOCTO\_FISCAL: Campos: VLR\_BASE\_ICMS\_2 \+ VLR\_BASE\_ICMS\_3 \+ VLR\_BASE\_ICMS\_4*\)   

 

Para as notas com itens  o campo deve fazer o somatório do Valor das bases isenta/não tributada e outras da SAFX08: campo 56 \(se campo 55 = 2 ou 3\)\.

 

Para as notas com itens  o campo deve fazer o somatório do Valor das bases isenta/não tributada \+ base outras \+ base de redução da SAFX08: campo 56 \(se campo 55 = 2 ou 3 ou 4\)\.

*\(Tabela: DWT\_ITENS\_MERC: Campos: VLR\_BASE\_ICMS\_2 \+ VLR\_BASE\_ICMS\_3 \+ VLR\_BASE\_ICMS\_4*\)   

Para as notas de utilities da SAFX43  o campo deve ser preenchido com a base de outras/isentas e não tributadas \(campo 24 \+ 25\)\. 

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__OS2761\-A__

[__MFS59318__](https://jira.thomsonreuters.com/browse/MFS-59318)

__RNF12__

__Substituição Tributária__

Para as notas sem itens  o campo deve ser totalizado o valor da base do ICMS\-ST da SAFX07 \(campo 64 \- Base ICMS Substituição Tributária\);

Para as notas com itens  o campo deve ser totalizado o valor da base do ICMS\-ST da SAFX08 \(campo 61 \- Base ICMS Substituição Tributária\);

Para as notas de utilities da SAFX43  o campo deve ser preenchido com a base de substituição tributária \(campo 40\)\. 

__OS2761\-A__

__RNF13__

__ICMS Cobrado por Substituição Tributária__

Para as notas sem itens  o campo deve ser totalizado o valor do ICMS\-ST da SAFX07 \(campo 48 – Valor ICMS Substituição Tributária\);

Para as notas com itens  o campo deve ser totalizado o valor do ICMS\-ST da SAFX08 \(campo 52 \- Valor ICMS Substituição Tributária\);

Para as notas de utilities da SAFX43  o campo deve ser preenchido com a base de substituição tributária \(campo 39\)\. 

__OS2761\-A__

__RGG__

##### Segmento G – Saídas e Entradas de Mercadorias e/ou Prestações de Serviços do Estabelecimento do Contribuinte \(por Município de Origem\) 

Recuperar documentos fiscais \(SAFX07, SAFX08\) de saída e entrada que possuam CFOP parametrizado na tela Parâmetros – Segmento G → Por CFOP ou Por Extensão CFOP no módulo da DIF\-TO 

Documentos Fiscais de Saída:

#### Parâmetros de Registros de Saída → Por CFOP e Por CFOP/Natureza de Operação

- Código da empresa = passado como parâmetro
- Código estabelecimento = passado como parâmetro
- Data de Fiscal = compreendida entre a data inicial e final do ano passado como parâmetro
- Movimento Entrada/Saída igual a “9”
- Classificação do documento fiscal deve ser 1, 3 e 4
- Considerar apenas notas não canceladas\.
- Não considerar notas de transferência de crédito \(IND\_TRANSF\_CRED = 0\)
- Desconsiderar notas com situação especial iguais a 1, 2 ou 8\.
- Recuperar as notas fiscais com itens e as notas fiscais sem itens\.
- Recuperar as notas fiscais com CFOP e com CFOP/Extensão\.
- COD\_PARAM = 523 e 524 \(receber como parâmetro\)
- Quando Prestação de Serviço de Transporte \[\(COD\_PARAM = 523\], o Código do Município que tem que estar preenchido é o código do município origem, da capa do documento para recuperação\.

#### Documentos Fiscais de Entrada: 

#### Parâmetros de <a id="_Toc319078198"></a>Registros de Entrada → Por CFOP e Por CFOP/Natureza de Operação

- Código da empresa = passado como parâmetro
- Código estabelecimento = passado como parâmetro
- Data de Fiscal = compreendida entre a data inicial e final do ano passado como parâmetro
- Movimento Entrada/Saída diferente de “9”
- Classificação do documento fiscal deve ser 1 e 3
- Código do Município \(município\) e UF pertencente a Tocantins 
- Considerar apenas notas não canceladas\.
- Não considerar notas de transferência de crédito \(IND\_TRANSF\_CRED = 0\)
- Desconsiderar notas com situação especial iguais a 1, 2 ou 8\.
- Recuperar as notas fiscais com itens e as notas fiscais sem itens\.
- Recuperar as notas fiscais com CFOP e com CFOP/Extensão\.
- COD\_PARAM = 525 \(receber como parâmetro\)

__OS2761\-A__

[__MFS58823__](https://jira.thomsonreuters.com/browse/MFS-58823)

__RGG__

#### Documentos Fiscais de Energia e Comunicação: 

Recuperar documentos fiscais \(SAFX42 e SAFX43\) de saída que possuam CFOP parametrizado na tela Parâmetros – Segmento G → Por CFOP ou Por Extensão CFOP no módulo da DIF\-TO 

- Código da empresa = passado como parâmetro
- Código estabelecimento = passado como parâmetro
- Data de Fiscal = compreendida entre a data inicial e final do ano passado como parâmetro
- Classificação do documento fiscal deve ser 1 e 3
- Estado deve ser igual ao do estabelecimento
- Considerar apenas notas não canceladas\.
- Desconsiderar notas com situação especial iguais a 1\.
- Recuperar as notas fiscais com itens e as notas fiscais sem itens\.
- Recuperar as notas fiscais com CFOP e com CFOP/Extensão\.
- Campo “Ponto de Consumo / Terminal Faturado” preenchido com “UF” e “Município”\.
- Quando o parâmetro “__*Considerar Município do Ponto de Consumo \(Utilities\)”*__ da Geração do Meio Magnético estiver  marcado, deverão ser considerados os Documentos Fiscais de Utilities \(SAFX42/43\), com as seguintes características: 
- Modelo de Documento = 06 – Nota Fiscal/Conta de Energia Elétrica, 
- Modelo de Documento = 21 – Nota Fiscal de Serviço de Comunicação ou 22 – Nota Fiscal de Serviço de Telecomunicações
- Não considerar os documentos gerados pelo Mapa Resumo, quando o parâmetro “__*Considerar Município do Ponto de Consumo \(Utilities\)*__” estiver marcado\. 
- Quando não estiver marcado, permanece o comportamento atual\. Estas condições deverão ser aplicadas tanto na geração normal quanto à Geração por Inscrição Estadual Única\.

Demais considerações:

- Agrupar: Saídas e Entradas por Município de Origem\.         

                    

- Ordenar por: Município de Origem, Tipo de Domicílio e Cód\. Município\.
- Deverão ser selecionados somente registros que pertençam aos Municípios de Domicílio Fiscal cadastrados na tela de “Dados Anuais da Declaração”, no menu Obrigações, do estabelecimento passado como parâmetro, onde o campo IDENT\_ESTADO pertencente ao COD\_MUNICIPIO da tabela MUNICIPIO seja igual ao IDENT\_ESTADO da tabela ESTADO do estado de Tocantins\. A periodicidade da obrigação é anual, porém as regras de seleção dos registros deverão ser de acordo com o movimento de cada município no ano de referência\. A data inicial e a data final indicarão o período desta busca dos registros\.
- Quando o parâmetro __“*Geração Centralizada por Inscrição Estadual Única”*__ da Geração dos Registros estiver marcado, o somatório deverá considerar todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no modulo controle das obrigações estaduais\. \(Inventário e Documentário Fiscal\)\. As parametrizações deverão ser feitas sempre em nome do estabelecimento centralizador\. 

__OS2761\-A__

__RNG1__

__Segmento__

Conteúdo fixo igual a “G”

__OS2761\-A__

__RNG2__

__Inscrição Estadual__

Recuperar o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para a empresa e o estabelecimento que estão sendo gerados\.

__OS2761\-A__

__RNG3__

__Período de referência__

Preencher com o valor informado no campo ”ANO” da tela de geração do meio magnético \(Estadual – DIF TO – Obrigações – Meio Magnético\)\. Gravar no formato AAAA\.

__OS2761\-A__

__RNG4__

__Município de Origem__

Para documentos de entrada: Preencher com o campo Código da UF \(campo COD\_UF da tabela MUNICIPIO\) concatenado com COD\_MUNICIPIO\_ORIG da SAFX07, da tabela de documentos fiscais, se o mesmo estiver preenchido\. Caso o campo não esteja preenchido, preencher com o campo COD\_MUNICIPIO da PFJ \(tabela SAFX04\)\. Caso for de outras UFs diferentes de “TO”, preencher com “9999999”\.

Para documentos de prestação de transporte: Preencher com o campo Código da UF \(campo COD\_UF da tabela MUNICIPIO\) concatenado com o campo COD\_MUNICIPIO\_ORIG \(SAFX07\) da tabela de documentos fiscais, se o mesmo estiver preenchido\. Caso o campo não esteja preenchido e/ou for de outras UFs diferentes de “TO”, preencher com “9999999”\.

__\[__[__MFS58823__](https://jira.thomsonreuters.com/browse/MFS-58823)__\] __

Para documentos de prestação de transporte: \[\(COD\_PARAM = 523\] Preencher com o campo Código da UF \(campo COD\_UF da tabela MUNICIPIO\) concatenado com o campo COD\_MUNICIPIO\_DEST \(SAFX07\) da tabela de documentos fiscais, se o mesmo estiver preenchido\. Caso o campo não esteja preenchido, preencher com o campo COD\_MUNICIPIO da PFJ \(tabela SAFX04\)\. Caso for de outras UFs diferentes de “TO”, preencher com “9999999”\. \(

Para documentos de demais saídas/prestações: Preencher com o campo COD\_MUNICIPIO\_ORIG \(SAFX07\) da tabela de documentos fiscais, se o mesmo estiver preenchido\. Caso o campo não esteja preenchido, preencher com o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO e caso for de outras UFs diferentes de “TO”, preencher com “9999999”\.

Para documentos de demais saídas/prestações: Preencher com o campo COD\_MUNICIPIO\_DEST \(SAFX07\) da tabela de documentos fiscais, se o mesmo estiver preenchido\. Caso o campo não esteja preenchido, preencher com o campo COD\_MUNICIPIO da PFJ \(tabela SAFX04\)\. Caso for de outras UFs diferentes de “TO”, preencher com “9999999”\.

__\[MFS93557\]__

Para documentos de utilities: Preencher com o campo COD\_MUNIC\_CONSUMO da tabela X42\_CAPA\_TELECOM e caso for de outras UFs diferentes de “TO”, preencher com “9999999”\.

Para documentos de utilities: Preencher com o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO e caso for de outras UFs diferentes de “TO”, preencher com “9999999”\.

Em qualquer um dos casos acima, deverá ser feita a consolidação dos códigos de município, caso o mesmo código seja gerado mais de uma vez\. Os demais campos do registro deverão ser somados\.

__OS2761\-A__

[__MFS58823__](https://jira.thomsonreuters.com/browse/MFS-58823)

__MFS93557__

__RNG5__

__Tipo Domicílio Fiscal__

Preencher com “__A__”, se selecionado registros conforme a regra __RGG__ para o Município Atual \(A\)\. 

Preencher com “__B__”, se selecionado registros conforme a regra __RGG__ para o Município Anterior \(B\)\.

Preencher com “__C__”, se selecionado registros conforme a regra __RGG__ para o Município Anterior \(C\)\.

Preencher com “__D__”, se selecionado registros conforme a regra __RGG__ para o Município Anterior \(D\)\.

Preencher com “__E__”, se selecionado registros conforme a regra __RGG__ para o Município Anterior \(E\)\.

__OS2761\-A__

__RNG6__

__Código do Município__

Quando identificado o tipo de Domicílio Fiscal da regra de seleção do campo anterior \(__Tipo Domicílio Fiscal\-RNG5__\), este campo deverá deve ser preenchido com a concatenação do Código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município do estabelecimento \(para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\)\.

__OS2761\-A__

__RNG7__

__Saídas e/ou Prestações__

Recuperar o somatório do campo VLR\_TOT\_NOTA \(SAFX07\), se os CFOPs começarem com “5”, “6” ou “7” parametrizados na tela Parâmetros – Registros de Saída – por CFOP ou Por CFOP/Natureza de Operação\.

Para as notas da SAFX43, este campo deverá ser preenchido com o somatório do valor de serviço \(campo 19\)\.

Quando este campo for preenchido, o campo __G8 – Entradas e/ou Aquisições __deve ser preenchido com zeros\.

Caso haja consolidações de código de município semelhante \(__G4__\), os valores deste campo deverão ser somados\.

__OS2761\-A__

__RNG8__

__Entradas e/ou Aquisições__

Recuperar o somatório do campo VLR\_TOT\_NOTA \(SAFX07\), se os CFOPs começarem com “1”, “2” ou “3” parametrizados na tela Parâmetros – Registros de Entrada – por CFOP ou Por CFOP/Natureza de Operação\.

Para as notas da SAFX43, este campo deverá ser preenchido com o somatório do valor de serviço \(campo 19\)\.

Quando este campo for preenchido, o campo __G7 – Saídas e/ou Prestações __deve ser preenchido com zeros\.

Caso haja consolidações de código de município semelhante \(__G4__\), os valores deste campo deverão ser somados\.

__OS2761\-A__

__RGH__

##### Segmento H – Relação de Mercadorias e/ou Produtos Adquiridos de Outros Municípios com Diferimento do ICMS

Deve ser gerado um registro do tipo “H” para cada inscrição estadual de origem\.

Recuperar documentos fiscais \(SAFX07 e SAFX08\) de entrada que possuam CFOP parametrizado na tela Parâmetros – Aquisição c/ Diferimento do ICMS para NF com e sem item de mercadoria\.

- Código da empresa = passado como parâmetro
- Código estabelecimento = passado como parâmetro
- Data de Fiscal = compreendida entre a data inicial e final do ano passado como parâmetro
- Movimento Entrada/Saída diferente de “9”
- Classificação do documento fiscal deve ser 1 e 3
- Município da PFJ diferente do Município do Estabelecimento
- Município e UF da Pessoa Fis\. Jur da nota pertencente a Tocantins\.
- Considerar apenas notas não canceladas\.
- Não considerar notas de transferência de crédito \(IND\_TRANSF\_CRED = 0\)
- Desconsiderar notas com situação especial iguais a 1, 2 ou 8\.
- Recuperar as notas fiscais com itens e as notas fiscais sem itens\.
-  COD\_PARAM = 526 \(receber como parâmetro\)
- Agrupando por: IE de Origem x Código Município 
- Ordenar por: IE de Origem, Domicílio Fiscal, Código Município e Município de Origem
- Deverão ser selecionados somente registros que pertençam aos Municípios de Domicílio Fiscal cadastrados na tela de “Dados Anuais da Declaração”, no menu Obrigações, do estabelecimento passado como parâmetro, onde o campo IDENT\_ESTADO pertencente ao COD\_MUNICIPIO da tabela MUNICIPIO seja igual ao IDENT\_ESTADO da tabela ESTADO do estado de Tocantins\. A periodicidade da obrigação é anual, porém as regras de seleção dos registros deverão ser de acordo com o movimento de cada município no ano de referência\. A data inicial e a data final indicarão o período desta busca dos registros\.
- Quando o parâmetro __“*Geração Centralizada por Inscrição Estadual Única”*__ da Geração dos Registros estiver marcado, o somatório deverá considerar todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no modulo controle das obrigações estaduais\. \(Inventário e Documentário Fiscal\)\. As parametrizações deverão ser feitas sempre em nome do estabelecimento centralizador\. 

__OS2761\-B__

__RNH1__

__Segmento__

Conteúdo fixo igual a “H”

__OS2761\-B__

__RNH2__

__Inscrição Estadual__

Recuperar o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para a empresa e o estabelecimento que estão sendo gerados\.

__OS2761\-B__

__RNH3__

__Período de referência__

Preencher com o valor informado no campo ”ANO” da tela de geração do meio magnético \(Estadual – DIF TO – Obrigações – Meio Magnético\)\. Gravar no formato AAAA\.

__OS2761\-B__

__RNH4__

__Inscrição Estadual de Origem__

Recuperar o campo INSC\_ESTADUAL da tabela SAFX04 cadastrada na Nota Fiscal de Entrada, que possua CFOP/Natureza de Operação parametrizados na tela Parâmetros – Aquisição com Diferimento do ICMS, e cuja pessoa fis/jur seja de Tocantins e com município diferente do município do estabelecimento que está sendo gerado\.

__OS2761\-B__

__RNH5__

__Tipo Domicílio Fiscal__

Preencher com “__A__”, se selecionado registros conforme a regra __RGH__ para o Município Atual \(A\)\. 

Preencher com “__B__”, se selecionado registros conforme a regra __RGH__ para o Município Anterior \(B\)\.

Preencher com “__C__”, se selecionado registros conforme a regra __RGH__ para o Município Anterior \(C\)\.

Preencher com “__D__”, se selecionado registros conforme a regra __RGH__ para o Município Anterior \(D\)\.

Preencher com “__E__”, se selecionado registros conforme a regra __RGH__ para o Município Anterior \(E\)\.

__OS2761\-B__

__RNH6__

__Código do Município__

Quando identificado o tipo de Domicílio Fiscal da regra de seleção do campo anterior \(__Tipo Domicílio Fiscal\-RNH5__\), este campo deverá deve ser preenchido com a concatenação do Código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município do estabelecimento \(para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\)\.

__OS2761\-B__

__RNH7__

__Município de Origem__

Recuperar o campo COD\_MUNICIPIO da tabela SAFX04 cadastrada na Nota Fiscal de Entrada, que possua CFOP/Natureza de Operação parametrizados na tela Parâmetros – Aquisição com Diferimento do ICMS, e cuja pessoa fis/jur seja de Tocantins e com município diferente do município do estabelecimento que está sendo gerado\.

  
Deverá compor o campo o Código da UF \(campo COD\_UF da tabela MUNICIPIO\) concatenado com o Código do município da SAFX04\.

__OS2761\-B__

__RGI__

##### Segmento I – Relação de Mercadorias e/ou Produtos Adquiridos de Outros Municípios com Diferimento do ICMS \(Notas Fiscais por Inscrição Estadual\)

Deve ser gerado um registro do tipo “I” para cada nota fiscal de entrada agrupada por inscrição estadual de origem

Recuperar documentos fiscais \(SAFX07 e SAFX08\) de entrada que possuam CFOP parametrizado na tela Parâmetros – Aquisição c/ Diferimento do ICMS para NF com e sem item de mercadoria\.

- Código da empresa = passado como parâmetro
- Código estabelecimento  = passado como parâmetro
- Data de Fiscal = compreendida entre a data inicial e final do ano passado como parâmetro
- Movimento Entrada/Saída diferente de “9”
- Classificação do documento fiscal deve ser 1 e 3
- Município da PFJ diferente do Município do Estabelecimento
- Município e UF da Pessoa Fis\. Jur da nota pertencente a Tocantins\.
- Considerar apenas notas não canceladas\.
- Não considerar notas de transferência de crédito \(IND\_TRANSF\_CRED = 0\)
- Desconsiderar notas com situação especial iguais a 1, 2 ou 8\.
- Recuperar as notas fiscais com itens e as notas fiscais sem itens\.
-  COD\_PARAM = 526 \(receber como parâmetro\)
- Agrupando por: Numero Documento x IE x Código Município
- Ordenar por: IE de Origem, Tipo de Domicílio, Código Município e Numero da Nota
- Deverão ser selecionados somente registros que pertençam aos Municípios de Domicílio Fiscal cadastrados na tela de “Dados Anuais da Declaração”, no menu Obrigações, do estabelecimento passado como parâmetro, onde o campo IDENT\_ESTADO pertencente ao COD\_MUNICIPIO da tabela MUNICIPIO seja igual ao IDENT\_ESTADO da tabela ESTADO do estado de Tocantins\. A periodicidade da obrigação é anual, porém as regras de seleção dos registros deverão ser de acordo com o movimento de cada município no ano de referência\. A data inicial e a data final indicarão o período desta busca dos registros\.
- Quando o parâmetro __“*Geração Centralizada por Inscrição Estadual Única”*__ da Geração dos Registros estiver marcado, o somatório deverá considerar todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no modulo controle das obrigações estaduais\. \(Inventário e Documentário Fiscal\)\. As parametrizações deverão ser feitas sempre em nome do estabelecimento centralizador\. 

__OS2761\-B__

__RNI1__

__Segmento__

Conteúdo fixo igual a “I”

__OS2761\-B__

__RNI2__

__Inscrição Estadual__

Recuperar o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para a empresa e o estabelecimento que estão sendo gerados\.

__OS2761\-B__

__RNI3__

__Período de referência__

Preencher com o valor informado no campo ”ANO” da tela de geração do meio magnético \(Estadual – DIF TO – Obrigações – Meio Magnético\)\. Gravar no formato AAAA\.

__OS2761\-B__

__RNI4__

__Inscrição Estadual de Origem__

Recuperar o campo INSC\_ESTADUAL da tabela SAFX04 cadastrada na Nota Fiscal de Entrada, que possua CFOP/Natureza de Operação parametrizados na tela Parâmetros – Aquisição com Diferimento do ICMS, e cuja pessoa fis/jur seja de Tocantins e com município diferente do município do estabelecimento que está sendo gerado\.

__OS2761\-B__

__RNI5__

__Tipo Domicílio Fiscal__

Preencher com “__A__”, se selecionado registros conforme a regra __RGI__ para o Município Atual \(A\)\. 

Preencher com “__B__”, se selecionado registros conforme a regra __RGI__ para o Município Anterior \(B\)\.

Preencher com “__C__”, se selecionado registros conforme a regra __RGI__ para o Município Anterior \(C\)\.

Preencher com “__D__”, se selecionado registros conforme a regra __RGI__ para o Município Anterior \(D\)\.

Preencher com “__E__”, se selecionado registros conforme a regra __RGI__ para o Município Anterior \(E\)\.

__OS2761\-B__

__RNI6__

__Código do Município__

Quando identificado o tipo de Domicílio Fiscal da regra de seleção do campo anterior \(__Tipo Domicílio Fiscal\-RNI5__\), este campo deverá deve ser preenchido com a concatenação do Código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município do estabelecimento \(para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\)\.

__OS2761\-B__

__RNI7__

__Número da nota__

Recuperar o campo NUM\_DOCFIS da tabela SAFX07 para Nota Fiscal de Entrada, que possua CFOP/Natureza de Operação parametrizados na tela Parâmetros – Aquisição com Diferimento do ICMS, e cuja pessoa fis/jur seja de Tocantins e com município diferente do município do estabelecimento que está sendo gerado\.

__\[MFS80343\]__ Alteração da forma de preencher o número do documento fiscal

 O número do documento fiscal tem 12 posições na SAFX07 e como no layout da DIF\-TO tem 7 posições, considerar as 7 últimas posições do campo para preencher o número da nota\.

__OS2761\-B__

__MFS80343__

__RNI8__

__Valor da nota__

Recuperar o campo VLR\_TOT\_NOTA da tabela SAFX07, para notas sem item e o somatório do campo VLR\_CONTAB\_ITEM da tabela SAFX08, para notas com itens de Entrada, que possua CFOP/Natureza de Operação parametrizados na tela Parâmetros – Aquisição com Diferimento do ICMS, e cuja pessoa fis/jur seja de Tocantins e com município diferente do município do estabelecimento que está sendo gerado\.

__OS2761\-B__

__RGJ__

##### Segmento J – Demonstrativo do Estoque

Gerar as totalizações dos campos, conforme empresa e estabelecimento escolhido, quando o parâmetro “__Gerar livro de Inventário__“ estiver selecionado na tela de Meio Magnético e as datas informadas através dos parâmetros Data de Inventário Inicial e Data de Inventário Final\. Deverá ser gravado na tabela apenas um registro por período \(Ano\)\. 

Selecionar os registros processados da tabela de SAFX52 – Produtos ou SAFX62 NBM, com os seguintes filtros:

- Código da empresa = passado como parâmetro
- Código estabelecimento = passado como parâmetro
- Parâmetro de __“Gerar livro de Inventário”__ selecionado da tela de Meio Magnético
- Data de Inventario = compreendida entre a data inicial de Inventário passado como parâmetro
- Tipo de recuperação do Estoque: por __Produto  – Tabela SAFX52__

__                                                      __por__ NBM        – Tabela SAFX62__

- Quando o parâmetro __“*Geração Centralizada por Inscrição Estadual Única”*__ da Geração dos Registros estiver marcado, o somatório deverá considerar todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no modulo controle das obrigações estaduais\. \(Inventário e Documentário Fiscal\)\. As parametrizações deverão ser feitas sempre em nome do estabelecimento centralizador\. 

__OS2761\-C__

__RNJ1__

__Segmento__

Conteúdo fixo igual a “J”

__OS2761\-C__

__RNJ2__

__Inscrição Estadual__

Recuperar o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para a empresa e o estabelecimento que estão sendo gerados\.

__OS2761\-C__

__RNJ3__

__Período de referência__

Preencher com o valor informado no campo ”ANO” da tela de geração do meio magnético \(Estadual – DIF TO – Obrigações – Meio Magnético\)\. Gravar no formato AAAA\.

__OS2761\-C__

__RNJ4__

__A\- Valor do Estoque Inicial: Tributados__

Se o campo “Tipo de Inventário“ da tela Obrigações – Geração do Meio Magnético estiver marcado com “Produto”:

Recuperar o somatório do campo VLR\_BASE\_ICMS da tabela SAFX52 para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Inicial do Inventário” da tela de geração\.

Se o campo “Tipo de Inventário“ da tela Obrigações – Geração do Meio Magnético estiver marcado com “NBM”:

Recuperar o somatório do campo VLR\_BASE\_ICMS da tabela SAFX62 para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Inicial do Inventário” da tela de geração\.

__OS2761\-C__

__RNJ5__

__B\- Valor do Estoque Inicial: Outras, Isentas e/ou Não tributadas__

Se o campo “Tipo de Inventário“ da tela Obrigações – Geração do Meio Magnético estiver marcado com “Produto”:

Recuperar o somatório dos campos VLR\_BASE\_ISENTO \+ VLR\_BASE\_OUTRAS da tabela SAFX52 para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Inicial do Inventário” da tela de geração\.

Se o campo “Tipo de Inventário“ da tela Obrigações – Geração do Meio Magnético estiver marcado com “NBM”:

Recuperar o somatório dos campos VLR\_BASE\_ISENTO \+ VLR\_BASE\_OUTRAS da tabela SAFX62 para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Inicial do Inventário” da tela de geração\. 

__OS2761\-C__

__RNJ6__

__C\- Valor do Estoque Inicial: Substituição Tributária__

Se o campo “Tipo de Inventário“ da tela Obrigações – Geração do Meio Magnético estiver marcado com “Produto”:

Recuperar o somatório do campo VLR\_BASE\_ICMSS da tabela SAFX52 para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Inicial do Inventário” da tela de geração\.

Se o campo “Tipo de Inventário“ da tela Obrigações – Geração do Meio Magnético estiver marcado com “NBM”:

Recuperar o somatório do campo VLR\_BASE\_ICMSS da tabela SAFX62 para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Inicial do Inventário” da tela de geração\.

__OS2761\-C__

__RNJ7__

__A\- Valor do Estoque Final: Tributados__

Se o campo “Tipo de Inventário“ da tela Obrigações – Geração do Meio Magnético estiver marcado com “Produto”:

Recuperar o somatório do campo VLR\_BASE\_ICMS da tabela SAFX52 para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Final do Inventário” da tela de geração\.

Se o campo “Tipo de Inventário“ da tela Obrigações – Geração do Meio Magnético estiver marcado com “NBM”:

Recuperar o somatório do campo VLR\_BASE\_ICMS da tabela SAFX62 para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Final do Inventário” da tela de geração\.

__OS2761\-C__

__RNJ8__

__B\- Valor do Estoque Final: Outras, Isentas e/ou Não tributadas__

Se o campo “Tipo de Inventário“ da tela Obrigações – Geração do Meio Magnético estiver marcado com “Produto”:

Recuperar o somatório dos campos VLR\_BASE\_ISENTO \+ VLR\_BASE\_OUTRAS da tabela SAFX52 para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Final do Inventário” da tela de geração\.

Se o campo “Tipo de Inventário“ da tela Obrigações – Geração do Meio Magnético estiver marcado com “NBM”:

Recuperar o somatório dos campos VLR\_BASE\_ISENTO \+ VLR\_BASE\_OUTRAS da tabela SAFX62 para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Final do Inventário” da tela de geração\. 

__OS2761\-C__

__RNJ9__

__C\- Valor do Estoque Final: Substituição Tributária__

Se o campo “Tipo de Inventário“ da tela Obrigações – Geração do Meio Magnético estiver marcado com “Produto”:

Recuperar o somatório do campo VLR\_BASE\_ICMSS da tabela SAFX52 para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Final do Inventário” da tela de geração\.

Se o campo “Tipo de Inventário“ da tela Obrigações – Geração do Meio Magnético estiver marcado com “NBM”:

Recuperar o somatório do campo VLR\_BASE\_ICMSS da tabela SAFX62 para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Final do Inventário” da tela de geração\.

__OS2761\-C__

__RGK__

##### Segmento K – Outras Saídas e/ou Outras Entradas \(Campo 10 – Saídas, Campo 11 \- Entradas\) 

Recuperar documentos fiscais \(SAFX07 e SAFX08\) de saída e entrada que possuam CFOP parametrizado na tela Parâmetros – Registros de Entrada → Por CFOP ou Por Extensão CFOP e Registros de Saídas → Por CFOP ou Por Extensão CFOP do módulo da DIF\-TO

- Código da empresa = passado como parâmetro
- Código estabelecimento  = passado como parâmetro
- Data de Fiscal = compreendida entre a data inicial e final do ano passado como parâmetro
- Movimentos de saída e entrada
- Classificação do documento fiscal deve ser 1 e 3
- Código do Município \(município\) e UF do estabelecimento gerador pertencente a Tocantins
- Considerar apenas notas não canceladas\.
- Não considerar notas de transferência de crédito \(IND\_TRANSF\_CRED = 0\)
- Desconsiderar notas com situação especial iguais a 1, 2 ou 8\.
- Recuperar as notas fiscais com itens e as notas fiscais sem itens\.
- Recuperar as notas fiscais com CFOP e com CFOP/Extensão\.
- Agrupando por: tipo de entrada/saída, cfop, município
- Ordenar por: tipo de entrada/saída, cfop, Tipo de Domicílio e Código Município
- Deverão ser selecionados somente registros que pertençam aos Municípios de Domicílio Fiscal cadastrados na tela de “Dados Anuais da Declaração”, no menu Obrigações, do estabelecimento passado como parâmetro, onde o campo IDENT\_ESTADO pertencente ao COD\_MUNICIPIO da tabela MUNICIPIO seja igual ao IDENT\_ESTADO da tabela ESTADO do estado de Tocantins\. A periodicidade da obrigação é anual, porém as regras de seleção dos registros deverão ser de acordo com o movimento de cada município no ano de referência\. A data inicial e a data final indicarão o período desta busca dos registros\.
- Quando o parâmetro __“*Geração Centralizada por Inscrição Estadual Única”*__ da Geração dos Registros estiver marcado, o somatório deverá considerar todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no modulo controle das obrigações estaduais\. \(Inventário e Documentário Fiscal\)\. As parametrizações deverão ser feitas sempre em nome do estabelecimento centralizador\. 

__OS2761\-C__

__RNK1__

__Segmento__

Conteúdo fixo igual a “K”

__OS2761\-C__

__RNK2__

__Inscrição Estadual__

Recuperar o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para a empresa e o estabelecimento que estão sendo gerados\.

__OS2761\-C__

__RNK3__

__Período de referência__

Preencher com o valor informado no campo ”ANO” da tela de geração do meio magnético \(Estadual – DIF TO – Obrigações – Meio Magnético\)\. Gravar no formato AAAA\.

__OS2761\-C__

__RNK4__

__Tipo de Entrada/Saída__

Recuperar o campo MOVTO\_E\_S referente à tabela SAFX07\. Se o conteúdo igual a “9”de Saída, preencher com o “__S__”, caso contrário, o conteúdo for diferente de “9”, preencher com “__E__” de Entrada\.

__OS2761\-C__

__RNK5__

__CFOP__

Recuperar o COD\_CFOP referente ao campo IDENT\_CFO a tabela SAFX07\.

__OS2761\-C__

__RNK6__

__Tipo Domicílio Fiscal__

Preencher com “__A__”, se selecionado registros conforme a regra __RGK__ para o Município Atual \(A\)\. 

Preencher com “__B__”, se selecionado registros conforme a regra __RGK__ para o Município Anterior \(B\)\.

Preencher com “__C__”, se selecionado registros conforme a regra __RGK__ para o Município Anterior \(C\)\.

Preencher com “__D__”, se selecionado registros conforme a regra __RGK__ para o Município Anterior \(D\)\.

Preencher com “__E__”, se selecionado registros conforme a regra __RGK__ para o Município Anterior \(E\)\.

__OS2761\-C__

__RNK7__

__Código do Município__

Quando identificado o tipo de Domicílio Fiscal da regra de seleção do campo anterior \(__Tipo Domicílio Fiscal\-RNK5__\), este campo deverá deve ser preenchido com a concatenação do Código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município do estabelecimento \(para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\)\.

__OS2761\-C__

__RNK8__

__Valor Contábil__

Recuperar o campo VLR\_TOT\_NOTA referente à tabela SAFX07\. Se campo não possuir valor, buscar o conteúdo do somatório dos itens \(campo VLR\_CONTAB\_ITEM da tabela SAFX08\)\.

__OS2761\-C__

__RNK9__

__Base de Cálculo__

Recuperar o campo VLR\_BASE\_ICMS\_1 referente à tabela SAFX07\. Se campo não possuir valor, buscar o conteúdo do somatório dos itens \(campo VLR\_BASE\_ICMS\_1 referente à tabela SAFX08\)\. 

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__OS2761\-C__

__RNK10__

__Outras__

Recuperar o campo VLR\_BASE\_ICMS\_3 referente à tabela SAFX07\. Se campo não possuir valor, buscar o conteúdo do somatório dos itens \(campo VLR\_BASE\_ICMS\_3 da tabela SAFX08\)\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__OS2761\-C__

__RNK11__

__Substituição Tributária__

Recuperar o campo VLR\_TRIBUTO\_ICMSS referente à tabela SAFX07\. Se campo não possuir valor, buscar o conteúdo do somatório dos itens \(campo VLR\_TRIBUTO\_ICMSS referente a tabela SAFX08\)\. 

__OS2761\-C__

__RGZ__

##### Segmento Z – Indica o Final da Declaração

Deve ser gerado apenas um registro por arquivo\.

__OS2761\-A__

__RNZ1__

__Segmento__

Conteúdo fixo igual a “Z”

__OS2761\-A__

__RNZ2__

__Inscrição Estadual__

Recuperar o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para a empresa e o estabelecimento que estão sendo gerados\.

__OS2761\-A__

__RNZ3__

__Período de referência__

Preencher com o valor informado no campo ”ANO” da tela de geração do meio magnético \(Estadual – DIF TO – Obrigações – Meio Magnético\)\. Gravar no formato AAAA\.

__OS2761\-A__

__RNZ4__

__Total de registro que compõe a declaração__

Preencher com o total de registros gerados no arquivo, exceto o registro Z\.

__OS2761\-A__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

