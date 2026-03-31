# MTZ_DOT-ES_Geracao_dos_Dados

- **Fonte:** MTZ_DOT-ES_Geracao_dos_Dados.docx
- **Modificado:** 2024-12-19
- **Tamanho:** 37 KB

---

                                   Geração dos Dados da DOT\-ES 

__Localização__: Menu Estadual, Módulo DOT\-ES 🡪 Obrigações 🡪 Geração dos Dados

##                                            Documento de Requisito

__Doc__

__Alteração__

__Data__

__Resp__

OS3712\-A

Geração dos Dados da DOT\-ES

27/02/2013

CH2897\-A\_2015

Definição Campo Destino da Nota do Parâmetro de Dados Acessórios\.

05/05/2015

Julyana Perrucini

MFS31580

Alteração das regras do Quadro A para CFOP com final “949”

08/11/2019

Andréa Rocha

MFS48816

Inclusão de parâmetro para não gerar o Quadro A, conforme  informações da portaria N\.º 35 \-R, DE 06 DE OUTUBRO DE 2014

15/12/2020

Andréa Rocha

### RN00

Regras Gerais

Os dados da DOT\-ES serão obtidos com base no Resumo por Município/Extensão de CFOP, SAFX52 e Detalhamento dos Valores p/ Município da própria DOT, onde serão consideradas somente as informações de Energia Elétrica, Extração de Petróleo e Outras Atividades, que não têm opção de parametrização\.

A partir desta geração serão alimentadas as telas de consulta das informações dos Quadros A e B e também a tela de Detalhamento dos Valores p/ Município\. As telas consulta demonstrarão as informações consolidadas, porém, a geração deve prever o armazenamento de informações conforme CFOPs / Naturezas parametrizadas, pois isso será utilizado na geração de relatórios de conferência\.

__Parâmetros de Tela:__

Período 🡪Neste campo o usuário informará as datas inicial e final para a geração dos dados \(DD/MM/AAAA\)

__\[MFS48816\] __Inclusão do parâmetro para ter a opção de não gerar o quadro A, conforme definição da portaria N\.º 35 \-R, de 06 de outubro de 2014

Gerar informações do Quadro A 🡪 campo do tipo S/N, default = marcado

    

Data p/ Apuração do Estoque Inicial \(SAFX52\) 🡪 Neste campo o usuário informará a data base para seleção da informação do inventário para apuração do estoque inicial\. Quando o campo “Gerar informações do Quadro A” estiver desmarcado, o preenchimento desta data não é obrigatório\.

Data p/ Apuração do Estoque Final \(SAFX52\) 🡪 Neste campo o usuário informará a data base para seleção da informação do inventário para apuração do estoque final\.   Quando o campo “Gerar informações do Quadro A” estiver desmarcado, o preenchimento desta data não é obrigatório\.

Geração por Inscrição Estadual Única 🡪 campo do tipo S/N, default = desmarcado

Gerar Dados Acessórios 🡪 campo do tipo S/N, default = marcado

Estabelecimentos 🡪 Neste quadro serão exibidos todos os estabelecimentos da Empresa que sejam do ES\.

	

__Origem dos Dados__: Resumo por Município/Extensão CFOP \(\*\)

                               SAFX52

                               Detalhamento dos Valores p/ Município \(\*\*\)

\(\*\) opção “*Resumo por Município/Extensão CFOP*” da rotina de geração das Obrigações Acessórias

\(\*\*\) opção de manutenção da própria DOT\-ES\. Nela o usuário informará os valores referentes ao detalhamento de Energia Elétrica, Extração de Petróleo e Outras Atividades, que não serão gerados automaticamente

__Para cada Estabelecimento selecionado pelo usuário, serão realizados os seguintes procedimentos__:

\- Geração dos dados do __Quadro A__, todos os campos \(ver regras __RN01__ a __RN13__\)

__    Obs\.:__ Quando o parâmetro “Gerar informações do Quadro A” estiver desmarcado, o quadro deve ser gerado com todos os seus valores zerados\.

\- Geração dos dados do __Quadro B__, campos 15, 16 e 17 \(ver regras __RN14__ a __RN21__\)

\- Geração dos valores detalhados por município do quadro “Detalhamento” \(ver regras __RN22__ a __RN26__\)

### RN01

### Campo Estoque Inicial:

O valor do estoque inicial será obtido na SAFX52 através da totalização do campo “14\-Custo Total”, de todos os registros de inventário na data do estoque inicial informada em tela\.

Recuperação dos dados na SAFX52:

COD\_EMPRESA        = código da Empresa

COD\_ESTAB              = código do Estabelecimento \(ver OBS\)

DATA\_INVENTARIO   = data do parâmetro “Data p/ Apuração do Estoque Inicial” informado na tela da geração\)

GRUPO\_CONTAGEM = 1, 2, 3 ou 5 \(o grupo “4\-Estoque de terceiros em poder de terceiros” não será considerado\)

OBS 1 \- Na geração por inscrição estadual única, serão recuperados os dados de todos os estabelecimentos envolvidos na centralização\.

__RN02__

### Campo 02\-Compras, Transf\. e Devoluções do Estado:

__\[ALTERADA – CH2897\-A\_2015\]__

Este valor será obtido no Resumo por Município/Extensão de CFOP das obrigações acessórias, a partir das operações parametrizadas para o Quadro A, considerando os dados do estabelecimento em questão e do período selecionado em tela\.

__Atenção:__ Para casos em que o usuário selecionou a opção de seleção dos documentos fiscais por Origem/Destino da NF ou PFJ da Nota na parametrização de dados acessórios em Parâmetros >> “Parâmetros p/ Geração de Dados Acessórios”, será necessário isolar a seleção para geração dos registros 06 e 10, pois atualmente esse resumo não grava a informação de UF/Município se não houver município e para UF EX não é obrigatório cadastro de município\.

__Definição “Parâmetros p/ Geração de Dados Acessórios”:__

A seleção dos dados do resumo para a geração dos registros deve considerar a parametrização quando o campo Gerar Dados Acessórios estiver selecionado na tela de geração do arquivo magnético \(localizado no item de menu Obrigações >> Geração dos Dados\)\. Então quando o item acima for verdadeiro verificar:

- Se o campo PFJ da Nota estiver selecionado considerar o campo 25\-COD\_MUNICIPIO da SAFX04 de acordo com a Pessoa Física/ Jurídica cadastrada na nota fiscal;
- Se o campo Origem/Destino da Nota estiver selecionado considerar o campo 182\-COD\_MUNICIPIO\_ORIG da SAFX07 no caso das notas de entrada e o campo 183\-COD\_MUNICIPIO\_DEST da SAFX07 no caso das notas de saída\.

__Tratamento para geração dos Registros 06 e 10:__

- Se o campo PFJ da Nota estiver selecionado considerar o campo 25\-COD\_MUNICIPIO da SAFX04 de acordo com a Pessoa Física/ Jurídica cadastrada na nota fiscal, caso o campo esteja nulo, considerar o campo19\-UF da SAFX04 quando for igual a “EX”;
- Se o campo Origem/Destino da Nota estiver selecionado considerar o campo 182\-COD\_MUNICIPIO\_ORIG da SAFX07 no caso das notas de entrada e o campo 183\-COD\_MUNICIPIO\_DEST da SAFX07 no caso das notas de saída, caso os campos estejam nulos, considerar o campo 117\- UF\_ORIG\_DEST da SAFX07 quando for igual a “EX” no caso das notas de entrada e o campo 122\- UF\_DESTINO da SAFX07 quando for igual a “EX” no caso das notas de saída\.

*Observação:* Somente os Registros 06 e 10 que irão considerar dados de Exterior, ou seja, UF igual a “EX”\.

	

Totalizar o valor das operações de todos os CFOP’s parametrizados __\(\*\)__ \+ o valor das operações de todos os CFOP/Naturezas parametrizados __\(\*\)__\.

__\(\*\)__ Parametrização do menu “Parâmetros 🡪 Parametrização das Operações 🡪 __Quadro A__” 

Apesar de existirem parametrizações distintas por CFOP e CFOP/Natureza, será considerada a mesma origem, a tabela de Resumo de Município/Extensão de CFOP, pois permite ambos os tipos de agrupamento\.

		

*Vide detalhes sobre estes resumos na *__*RN00*__*\. *

__\[MFS31580\]__

Se CFOP finalizado com “949” \(3 últimos dígitos\) e o valor do ICMS \(VLR\_TRIB\_ICMS\) igual a zeros

     A nota não deve ser considerada

Senão

     O valor a ser totalizado é o valor contábil \(VLR\_CONTABIL\)\.

 

Recuperação dos dados dos resumos:

EMPRESA                   = código da Empresa

ESTABELECIMENTO   = código do Estabelecimento *\(ver OBS\)*

DATA DA APURAÇÃO  = considerar todos os registros cuja data se enquadre no período informado em tela 

CFOP ou CFOP/Natureza = dependendo do resumo, buscar o CFOP ou CFOP/Natureza da parametrização

*OBS: na geração por inscrição estadual única, serão recuperados os dados de todos os estabelecimentos envolvidos na centralização\. *

Observar que a DOT é uma obrigação anual\. Por isso, o esperado é que o usuário informe um período envolvendo vários meses, e assim, retornarão os dados de vários meses, onde existirão linhas repetidas para um mesmo CFOP ou CFOP/NAT\.

__RN03__

### Campo 03\-Entrada de Produção Rural Própria:

Idem RN02, considerando o parâmetro específico para esta operação\.

__\[MFS31580\]__

Se CFOP finalizado com “949” \(3 últimos dígitos\) e o valor do ICMS \(VLR\_TRIB\_ICMS\) igual a zeros

     A nota não deve ser considerada

Senão

     O valor a ser totalizado é o valor contábil \(VLR\_CONTABIL\)\.

__RN04__

### Campo 04\-Compras de Pessoa Física ou Não Contribuintes do ICMS no Estado

Idem RN02, considerando o parâmetro específico para esta operação\.

__\[MFS31580\]__

Se CFOP finalizado com “949” \(3 últimos dígitos\) e o valor do ICMS \(VLR\_TRIB\_ICMS\) igual a zeros

     A nota não deve ser considerada

Senão

     O valor a ser totalizado é o valor contábil \(VLR\_CONTABIL\)\.

### RN05

	

### Campo 05\-Compras, Transf\. e Devoluções de Outros Estados:

Idem RN02, considerando o parâmetro específico para esta operação\.

__\[MFS31580\]__

Se CFOP finalizado com “949” \(3 últimos dígitos\) e o valor do ICMS \(VLR\_TRIB\_ICMS\) igual a zeros

     A nota não deve ser considerada

Senão

     O valor a ser totalizado é o valor contábil \(VLR\_CONTABIL\)\.

### RN06

### Campo 06\-Compras, Transf\. e Devoluções do Exterior:

Idem RN02, considerando o parâmetro específico para esta operação\.

__\[MFS31580\]__

Se CFOP finalizado com “949” \(3 últimos dígitos\) e o valor do ICMS \(VLR\_TRIB\_ICMS\) igual a zeros

     A nota não deve ser considerada

Senão

     O valor a ser totalizado é o valor contábil \(VLR\_CONTABIL\)\.

### RN07

__Campo Total de Entradas:__

Este valor será a totalização dos campos 01 ao 06\.

	

### RN08

__Campo Vendas, Transferências e Devoluções Internas:__

Idem RN02, considerando o parâmetro específico para esta operação\.

__\[MFS31580\]__

Se CFOP finalizado com “949” \(3 últimos dígitos\) e o valor do ICMS \(VLR\_TRIB\_ICMS\) igual a zeros

     A nota não deve ser considerada

Senão

     O valor a ser totalizado é o valor contábil \(VLR\_CONTABIL\)\.

### RN09

__Campo Vendas, Transferências e Devoluções para outros estados:__

Idem RN02, considerando o parâmetro específico para esta operação\.

__\[MFS31580\]__

Se CFOP finalizado com “949” \(3 últimos dígitos\) e o valor do ICMS \(VLR\_TRIB\_ICMS\) igual a zeros

     A nota não deve ser considerada

Senão

     O valor a ser totalizado é o valor contábil \(VLR\_CONTABIL\)\.

### RN10

__Campo Vendas, Transferências e Devoluções para o exterior:__

Idem RN02, considerando o parâmetro específico para esta operação\.

__\[MFS31580\]__

Se CFOP finalizado com “949” \(3 últimos dígitos\) e o valor do ICMS \(VLR\_TRIB\_ICMS\) igual a zeros

     A nota não deve ser considerada

Senão

     O valor a ser totalizado é o valor contábil \(VLR\_CONTABIL\)\.

RN11

### Campo Estoque Final:

O valor do estoque final será obtido na SAFX52 através da totalização do campo “14\-Custo Total”, de todos os registros de inventário na data do estoque final informada em tela\.

Recuperação dos dados na SAFX52:

COD\_EMPRESA        = código da Empresa 

COD\_ESTAB              = código do Estabelecimento \(ver OBS\)

DATA\_INVENTARIO   = data do parâmetro “Data p/ Apuração do Estoque Final” informado na tela da geração\)

GRUPO\_CONTAGEM = 1, 2, 3 ou 5 \(o grupo “4\-Estoque de terceiros em poder de terceiros” não será considerado\)

OBS 1 \- Na geração por inscrição estadual única, serão recuperados os dados de todos os estabelecimentos envolvidos na centralização\.

__RN12__

__Campo Total de Saídas:__

Este valor será a totalização dos campos 08 ao 11\.

__RN13__

__Campo Resultado com Mercadorias \(Saídas – Entradas\):__

Este valor será o resultado da seguinte diferença: Total das Saídas \(campo 12\) – Total das Entradas \(campo 07\)

*\(se o resultado for < 0, o valor será demonstrado normalmente com o sinal negativo\)*

 

__RN14__

__Campo Energia Elétrica:__

Este valor será obtido no Detalhamento de Valores por Município, considerando que tenha sido parametrizado a opção de detalhamento correspondente à Energia Elétrica\.

Será a totalização dos valores lançados na coluna Valor \+ a totalização dos valores lançados na coluna Valor de Distribuição\.

Este valor será informado pelo usuário\.

Recuperação dos dados do detalhamento:

EMPRESA                   = código da Empresa

ESTABELECIMENTO   = código do Estabelecimento *\(ver OBS\)*

DATA DA OPERAÇÃO  = considerar todos os registros cuja data se enquadre no período informado em tela 

*OBS: na geração por inscrição estadual única, serão recuperados os dados de todos os estabelecimentos envolvidos na centralização\. *

__RN15__

__Campo Transporte:__

Este valor será obtido no Resumo por Município/Extensão de CFOP das obrigações acessórias, a partir das operações parametrizadas para o Quadro B, considerando os dados do estabelecimento em questão e do período selecionado em tela\.

	

Totalizar o valor das operações de todos os CFOP’s parametrizados __\(\*\)__ \+ o valor das operações de todos os CFOP/Naturezas parametrizados __\(\*\)__\.

 __\(\*\)__ Parametrização do menu “Parâmetros 🡪 Parametrização das Operações 🡪 __Quadro B__” 

Apesar de existirem parametrizações distintas por CFOP e CFOP/Natureza, será considerada a mesma origem, a tabela de Resumo de Município/Extensão de CFOP, pois permite ambos os tipos de agrupamento\.

*Vide detalhes sobre estes resumos na *__*RN00*__*\. O valor a ser totalizado é o valor contábil \(VLR\_CONTABIL\)\.*

 

Recuperação dos dados dos resumos:

EMPRESA                   = código da Empresa

ESTABELECIMENTO   = código do Estabelecimento *\(ver OBS\)*

DATA DA APURAÇÃO  = considerar todos os registros cuja data se enquadre no período informado em tela 

CFOP ou CFOP/Natureza = dependendo do resumo, buscar o CFOP ou CFOP/Natureza da parametrização

*OBS: na geração por inscrição estadual única, serão recuperados os dados de todos os estabelecimentos envolvidos na centralização\. *

Observar que a DOT é uma obrigação anual\. Por isso, o esperado é que o usuário informe um período envolvendo vários meses, e assim, retornarão os dados de vários meses, onde existirão linhas repetidas para um mesmo CFOP ou CFOP/NAT\.

__RN16__

__Campo Comunicação:__

Idem RN15, considerando o parâmetro específico para esta operação\.

__RN18__

__Campo Extração de Petróleo:__

Este valor será obtido no Detalhamento de Valores por Município, considerando que tenha sido parametrizado a opção de detalhamento correspondente à Extração de Petróleo\.

Será a totalização dos valores lançados na coluna Valor\.

Este valor será informado pelo usuário\.

Recuperação dos dados do detalhamento:

EMPRESA                   = código da Empresa

ESTABELECIMENTO   = código do Estabelecimento *\(ver OBS\)*

DATA DA OPERAÇÃO  = considerar todos os registros cuja data se enquadre no período informado em tela 

*OBS: na geração por inscrição estadual única, serão recuperados os dados de todos os estabelecimentos envolvidos na centralização\. *

__RN20__

__Campo Distribuição de Água Canalizada:__

Idem RN15, considerando o parâmetro específico para esta operação\.

__RN21__

__Campo Outras Atividades:__

Este valor será obtido no Detalhamento de Valores por Município, considerando que tenha sido parametrizado a opção de detalhamento correspondente à Outras Atividades\.

Será a totalização dos valores lançados na coluna Valor\.

Este valor será informado pelo usuário\.

Recuperação dos dados do detalhamento:

EMPRESA                   = código da Empresa

ESTABELECIMENTO   = código do Estabelecimento *\(ver OBS\)*

DATA DA OPERAÇÃO  = considerar todos os registros cuja data se enquadre no período informado em tela 

*OBS: na geração por inscrição estadual única, serão recuperados os dados de todos os estabelecimentos envolvidos na centralização\. *

__RN22__

__Detalhamento Transportes:__

Este valor será obtido no Resumo por Município/Extensão de CFOP das obrigações acessórias, a partir das operações parametrizadas para o Quadro B, considerando os dados do estabelecimento em questão e do período selecionado em tela\.

	

Totalizar o valor das operações por Município e Período de Referência \(gravando por mês e ano enquadrados no período parametrizado\) considerando operações de todos os CFOP’s parametrizados __\(\*\)__ \+ o valor das operações de todos os CFOP/Naturezas parametrizados __\(\*\)__\.

 __\(\*\)__ Parametrização do menu “Parâmetros 🡪 Parametrização das Operações 🡪 __Quadro B__” 

Apesar de existirem parametrizações distintas por CFOP e CFOP/Natureza, será considerada a mesma origem, a tabela de Resumo de Município/Extensão de CFOP, pois permite ambos os tipos de agrupamento\.

*Vide detalhes sobre estes resumos na *__*RN00*__*\. O valor a ser totalizado é o valor contábil \(VLR\_CONTABIL\)\.*

 

Recuperação dos dados dos resumos:

EMPRESA                   = código da Empresa

ESTABELECIMENTO   = código do Estabelecimento *\(ver OBS\)*

DATA DA APURAÇÃO  = considerar todos os registros cuja data se enquadre no período informado em tela 

CFOP ou CFOP/Natureza = dependendo do resumo, buscar o CFOP ou CFOP/Natureza da parametrização

*OBS: na geração por inscrição estadual única, serão recuperados os dados de todos os estabelecimentos envolvidos na centralização\. *

Observar que a DOT é uma obrigação anual\. Por isso, o esperado é que o usuário informe um período envolvendo vários meses, e assim, retornarão os dados de vários meses, onde existirão linhas repetidas para um mesmo CFOP ou CFOP/NAT\.

__RN23__

__Detalhamento Comunicação: __

Idem RN22, considerando o parâmetro específico para esta operação\.

__RN24__

__Detalhamento Água Canalizada: __

Idem RN22, considerando o parâmetro específico para esta operação\.

__RN25__

__Detalhamento Pessoas Físicas:__

Este valor será obtido no Resumo por Município/Extensão de CFOP das obrigações acessórias, a partir das operações parametrizadas para o Quadro A, considerando os dados do estabelecimento em questão e do período selecionado em tela\.

	

Totalizar o valor das operações por Município e Período de Referência \(gravando por mês e ano enquadrados no período parametrizado\) considerando operações de todos os CFOP’s parametrizados __\(\*\)__ \+ o valor das operações de todos os CFOP/Naturezas parametrizados __\(\*\)__\.

 __\(\*\)__ Parametrização do menu “Parâmetros 🡪 Parametrização das Operações 🡪 __Quadro A__” 

Apesar de existirem parametrizações distintas por CFOP e CFOP/Natureza, será considerada a mesma origem, a tabela de Resumo de Município/Extensão de CFOP, pois permite ambos os tipos de agrupamento\.

*Vide detalhes sobre estes resumos na *__*RN00*__*\. O valor a ser totalizado é o valor contábil \(VLR\_CONTABIL\)\.*

 

Recuperação dos dados dos resumos:

EMPRESA                   = código da Empresa

ESTABELECIMENTO   = código do Estabelecimento *\(ver OBS\)*

DATA DA APURAÇÃO  = considerar todos os registros cuja data se enquadre no período informado em tela 

CFOP ou CFOP/Natureza = dependendo do resumo, buscar o CFOP ou CFOP/Natureza da parametrização

*OBS: na geração por inscrição estadual única, serão recuperados os dados de todos os estabelecimentos envolvidos na centralização\. *

Observar que a DOT é uma obrigação anual\. Por isso, o esperado é que o usuário informe um período envolvendo vários meses, e assim, retornarão os dados de vários meses, onde existirão linhas repetidas para um mesmo CFOP ou CFOP/NAT\.

__RN26__

__Detalhamento Produção Rural Própria:__

Idem RN25, considerando o parâmetro específico para esta operação\.

	

