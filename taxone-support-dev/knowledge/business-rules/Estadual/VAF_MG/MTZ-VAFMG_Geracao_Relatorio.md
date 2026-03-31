# MTZ-VAFMG_Geracao_Relatorio

- **Fonte:** MTZ-VAFMG_Geracao_Relatorio.docx
- **Modificado:** 2023-07-27
- **Tamanho:** 42 KB

---

							VAF\-MG – Geração do Relatório

__Localização__: Menu Estadual, Módulo VAF\-MG, item de menu Obrigações à Geração do Relatório

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS2621

VAF\-MG

O relatório da VAF\-MG deverá demonstrar os valores obtidos na linha de Outras entradas detalhadas por município, quando o contribuinte for do tipo Transportador\.

OS 3022

Geração da VAF\-MG com Inscrição Estadual Única

O objetivo desta OS é alterar a geração do relatório VAF\-MG para atender as empresas que realizam a apuração de forma centralizada por Inscrição Estadual Única\. Nestes casos, deve ser gerado um único relatório para a VAF\-MG, com a totalidade das operações de todos os estabelecimentos envolvidos da centralização\.

OS3202

Atendimento ao Contribuinte Tipo Transportador

Atender por Completo ao Transportador, efetuando o rateio do valor de Outras Entradas\.

CH104167

Inclusão do CNPJ contribuinte no Quadro Cadastro do Contribuinte

Inclusão do CNPJ contribuinte no Quadro Cadastro do Contribuinte

OS3202

Automatizar Cálculo do Detalhamento de Outras Entradas para Contribuintes do Tipo Transportador

Automatizar Cálculo do Detalhamento de Outras Entradas para Contribuintes do Tipo Transportador \(alterada a RN19\)

MFS\-20715

Alteração no Módulo: Estadual > VAF\-MG\.

Essa alteração de produto tem como objetivo a inclusão de um parâmetro nas telas do CFOP/CFOP por Natureza\. Quando marcado apresenta como exclusão o somatório dos valores de Isentas e Outras \(ICMS\) das notas de energia elétrica/comunicação e transporte na geração do relatório no título de “Exclusão VAF”\.

MFS\-44425

DAMEF – Portaria SRE 175/2020

RN00: A geração do relatório da DAMEF com ano\-exercício A PARTIR DE 2020, devem ser executada pela funcionalidade disponível no menu DAMEF\-EFD FISCAL >> Geração do Relatório \(Portaria SRE 175/2020\)\. 

RN01: Inclusão de Críticas na Geração do Relatorio\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Para ano\-exercício A PARTIR DE 2020, então:

    Utilizar a Geração do Relatório disponivel no <a id="_Hlk53752782"></a>menu DAMEF\-EFD FISCAL >> Geração do Relatório \(Portaria SRE 175/2020\)\.

Para ano\-exercício ANTERIOR A 2020, então:

    Utilizar a Geração do Relatório disponivel no menu Obrigações à Geração do Relatório\.

MFS\-44425

__RN01__

__Críticas da Geração:__

1. Caso não exista registro na tabela de Dados Iniciais da VAF, para o estabelecimento e ano exercício informado na tela de geração, exbir mensagem no log:

ATENCAO: Dados Iniciais Não preenchidos para a empresa XXX e estabelecimento YYYYYY\. As Informações do VAF não serão calculadas\. Favor informar na Manutenção dos Dados Iniciais\.

1. Caso exista registro na tabela de Dados Iniciais da VAF, para o estabelecimento e ano exercício informado na tela de geração, mas o campo “Tipo de Contribuinte” estiver sem preenchimento, exbir mensagem no log:

ATENCAO: Campo Tipo de Contribuinte Não preenchido para a empresa XXX e estabelecimento YYYYYY\. As Informações do VAF não serão calculadas\. Favor informar na Manutenção dos Dados Iniciais\.

\[MFS\-44425\]

Caso exista registro na tabela de Dados Iniciais da VAF, para o estabelecimento e ano exercício informado na tela de geração, mas o campo “Tipo de Contribuinte” estiver preenchimento com a opção *Regular*, exbir mensagem no log e abortar o processo:

ATENCAO: Campo Tipo de Contribuinte preenchido com opção Regular para a empresa XXX e estabelecimento YYYYYY\.  Esta opção é válida para a DAMEF a partir da Portaria 175/2020\. Favor acessar o menu Preliminares à Manutenção de Dados Iniciais e corrigir a informação solicitada\.

Caso o ano exercício informado na tela seja maior ou igual a 2020, exibir a seguinte mensagem no log e continuar o processamento:

ATENCAO: Para geração dos relatórios da DAMEF de exercícios a partir de 2020, utilizar a geração disponível no menu DAMEF\-EFD FISCAL à Geração do Relatório \(Portaria SRE 175/2020\)\.

MFS\-44425

__RN01A__

O sistema irá verificar se na parametrização dos dados iniciais está preenchido o tipo de contribuinte igual a Transportador e irá demonstrar o detalhamento de entradas por município\.

OS2621

__RN01B__

O detalhamento de entradas por município deverá considerar os Documentos fiscais que foram utilizados para compor o valor da linha “Outras entradas”\.

OS2621

__RN02__

O sistema deverá agrupar os municípios que estão preenchidos no campo Município Origem \(campo 182 da Safx07\)\.

OS2621

__RN03__

O valor a ser demonstrado no relatório da VAF será o mesmo valor recuperado para calcular a linha outras entradas\.

OS2621

__RN04__

Geração do Relatório

Módulo: Estadual à VAF\-MG, Menu: Obrigações Geração do Relatório

Parâmetro “__Geração centralizada por Inscrição Estadual Única__”\. A partir da criação deste parâmetro, a regra para demonstrar os estabelecimentos no quadro “Estabelecimentos” deve ser:

         \-     Trazer “desmarcado” o parâmetro de Geração centralizada por Inscrição Estadual Única\.

          \-     Se parâmetro Geração centralizada por Inscrição Estadual Única desmarcado:

Mostrar todos os Estabelecimentos da Empresa, cuja UF = “MG”\.

          \-     Se parâmetro Geração centralizada por Inscrição Estadual Única marcado:

Mostrar apenas os Estabelecimentos parametrizados como centralizadores na parametrização dos Estabelecimentos com Inscrição Estadual Única do módulo de Controle das Obrigações Estaduais, cuja UF = “MG

A geração do relatório da VAF\-MG deve ser alterada para considerar o novo parâmetro incluído na tela de Geração do Relatório do módulo VAF\-MG\. O tratamento da inscrição estadual única será o mesmo já existente no Mastersaf para a emissão dos livros fiscais, da seguinte forma:

- Os registros de identificação do contribuinte devem ser gerados com os dados do estabelecimento centralizador;
- Ao utilizar qualquer parametrização cujo cadastro seja por estabelecimento, deve\-se utilizar a parametrização feita em nome do estabelecimento centralizador;
- Além dos documentos fiscais do estabelecimento da geração, que é o estabelecimento centralizador, deverão ser recuperados também os documentos dos estabelecimentos centralizados\. Assim, a regra é considerar os documentos fiscais de todos os estabelecimentos envolvidos na centralização, lembrando que a parametrização dos estabelecimentos Centralizador x Centralizados fica no módulo Controle das Obrigações Estaduais, no item “Obrigações à Empresas/Estabelecimentos com Inscrição Estadual Única”; 
- Os registros gerados a partir dos dados dos livros fiscais \(P1, P2 e P9\) deverão considerar as gerações feitas p/o estabelecimento centralizador, utilizando sempre os livros das obrigações fiscais 161, 162, 163, 164 e 165, que são os códigos dos livros fiscais utilizados por quem trabalha com inscrição estadual única\. 

Segue detalhes de cada quadro apresentados no relatório nas regras __RN05 __a __RN19\.__

OS 3022

__RN05__

Cadastrado do Responsável\.

As regras na geração desse quadro não serão modificadas na utilização da geração do relatório por I\.E\.U\.

OS 3022

__RN06__

Cadastro do Contribuinte:

Considerar os dados do Estabelecimento Centralizador\. 

OS 3022

__RN07__

Totalização do Inventário Inicial e Final:

Neste quadro é gerado com as totalizações dos valores dos campos: Tributados, Isentos ou Não Incidência, Outros e Sujeitos à Substituição Tributária, de acordo com a empresa e estabelecimento selecionados, nas datas informadas através dos parâmetros Data de Inventário Inicial e Data de Inventário Final na tela de Geração do Relatório\.

Como é possível obter duas formas de gerações desse quadro, através do parâmetro ‘’Tipo de Inventário’’ na tela de geração do relatório, segue abaixo o detalhamento de cada um deles:

- Caso esteja marcado o parâmetro Produto, as informações geradas neste quadro serão recuperadas da tabela X52\_INVENT\_PRODUTO;
- Caso esteja desmarcado o parâmetro NBM, as informações geradas neste quadro serão recuperadas da tabela X62\_INVENTARIO\_NBM\.

__Regras para Geração por I\.E\. U:__

Na geração desse quadro, deverão ser considerados os itens de Inventário de todos os estabelecimentos \(centralizador e centralizados\), mantendo a mesma regra totalização dos valores do produto com a mesma combinação de dados\.

OS 3022

__RN08__

Demonstrativo do Resultado Operacional:

Esse quadro é gerado, demonstrando a totalização dos valores dos lançamentos efetuados no balanço de encerramento em cada campo, que são recuperados através da tabela DWT\_BALANCO, para as classes do balanço que estiverem relacionadas aos códigos de parâmetro \(COD\_PARAM\) da tabela PRT\_BALANCO\_MSAF\.

“Como é possível obter duas formas de gerações deste quadro, através do parâmetro ‘‘Balanço de Encerramento Centralizado \(por empresa\)” da tela de geração do relatório, segue abaixo o detalhamento de cada um deles:

- Caso estiver marcado o parâmetro “Balanço de Encerramento Centralizado \(por empresa\)”, na totalização dos valores, serão considerados os lançamentos que estejam com o campo Tipo de Balanço \(IND\_TP\_BALANCO\) da tabela DWT\_BALANÇO igual 1 \(Empresarial\)\.
-   Caso estiver desmarcado o parâmetro “Balanço de Encerramento Centralizado \(por empresa\)”, na totalização dos valores, serão considerados os lançamentos que estejam com o campo Tipo de Balanço \(IND\_TP\_BALANCO\) da tabela DWT\_BALANÇO igual 2 \(Estabelecimento\)\.

__Regras para Geração por I\.E\. U:__

- Na geração desse quadro, caso estiver desmarcado o parâmetro “Balanço de Encerramento Centralizado \(por empresa\)”, devem ser considerados os lançamentos que estejam com o campo Tipo de Balanço \(IND\_TP\_BALANCO\) da tabela DWT\_BALANÇO igual 2 \(Estabelecimento\) dos estabelecimentos \(centralizador e centralizados\)\. 

OS 3022

__RN09__

Resumo das Operações e Prestações de Entradas \(Entradas do Estado\):

Esse quadro é gerado, com os dados que são recuperados do Resumo por UF, através das tabelas EST\_RES\_UF\_01\.  A leitura dessa tabela não será alterada, pois é gerada no passo anterior, considerando todas as notas fiscais dos estabelecimentos \(centralizador e centralizados\)\.

Com exceção dos campos:

\- Produto Agropecuário, que os dados são recuperados do Resumo por Município Agro, através da tabela EST\_RES\_MUN\_AGRO\. A leitura dessa tabela não será alterada, pois é gerada no passo anterior, considerando todas as notas fiscais dos estabelecimentos \(centralizador e centralizados\)\.

\- Geração de Energia Elétrica, que é preenchido com informação digitada pelo usuário na tela de Manutenção dos Dados Iniciais, localizada no módulo: Estaduais à Menu: VAF\-MG à Preliminares à Manutenção dos Dados Iniciais\.

OS 3022

__RN10__

Entradas de Outros Estados

Esse quadro é gerado com os dados que são recuperados do Resumo por UF, através da tabela EST\_RES\_UF\_01\.  A leitura dessa tabela não será alterada, pois é gerada no passo anterior, considerando todas as notas fiscais dos estabelecimentos \(centralizador e centralizados\)\.

OS 3022

__RN11__

Entradas do Exterior

Esse quadro é gerado com dados que são recuperados do Resumo por UF, através da tabela EST\_RES\_UF\_01\. A leitura dessa tabela não será alterada, pois é gerada no passo anterior, considerando todas as notas fiscais dos estabelecimentos \(centralizador e centralizados\)\.

OS 3022

__RN12__

Total das Entradas

Neste quadro, é gerado com as totalizações dos valores dos campos apresentados nos quadros descritos acima\. 

Com exceção dos campos: Autuações Fiscais \(Denúncias Espontâneas\) e Ajuste de Transferência que são preenchidos com a informação digitada pelo usuário na tela de Manutenção dos Dados Iniciais, localizada no módulo: Estaduais à Menu: VAF\-MG à Preliminares à Manutenção dos Dados Iniciais\.

OS 3022

__RN13__

Resumo das Operações e Prestações de Saídas \(Saídas do Estado\)

Neste quadro o campo Transporte Tomado de Transportador Autônomo é preenchido com informação digitada pelo usuário na tela de Manutenção dos Dados Iniciais, localizada no módulo: Estaduais à Menu: VAF\-MG à Preliminares à Manutenção dos Dados Iniciais\.

Para os demais campos, os dados serão recuperados da tabela EST\_RES\_UF\_01\.  A leitura dessa tabela não será alterada, pois é gerada no passo anterior, considerando todas as notas fiscais dos estabelecimentos \(centralizador e centralizados\)\.

OS 3022

__RN14__

Saídas de Outros Estados

Esse quadro é gerado com dados que são recuperados do Resumo por UF, através da tabela EST\_RES\_UF\_01\. A leitura dessa tabela não será alterada, pois é gerada no passo anterior, considerando todas as notas fiscais dos estabelecimentos \(centralizador e centralizados\)\. 

OS 3022

__RN15__

Saídas do Exterior

Esse quadro é gerado com dados que são recuperados do Resumo por UF, através da tabela EST\_RES\_UF\_01\. A leitura dessa tabela não será alterada, pois é gerada no passo anterior, considerando todas as notas fiscais dos estabelecimentos \(centralizador e centralizados\)\.

OS 3022

__RN16__

Total de Saídas:

Esse quadro é gerado com as totalizações dos valores dos campos apresentados nos quadros: Resumo das Operações e Prestações de Saídas, Saídas de Outros Estados e Saídas do Exterior\. 

Com exceção dos campos: Autuações Fiscais \(Denúncias Espontâneas\), Cooperativas e Ajuste de Transferência que são preenchidos com a informação digitada pelo usuário na tela de Manutenção dos Dados Iniciais, localizada no módulo: Estaduais à Menu: VAF\-MG à Preliminares à Manutenção dos Dados Iniciais\.

OS 3022

__RN17__

__\[ALTERADA – CH70711\-B\]__

Exclusão do VAF:

Na geração desse quadro, nos campos: __Campo Parcela do IPI que não integre a base de cálculo ICMS__ e __Mercadorias com Suspensão de ICMS__ deve considerar todos os documentos fiscais do estabelecimento \(centralizador e centralizados\)\.

Cálculo do campo “__Campo Parcela do IPI que não integre a base de cálculo ICMS__”

     Quando o Campo 33 da SAFX08 \(__IND\_IPI\_INCLUSO__\) estiver marcado, considerado apenas o campo 81 da SAFX08 \(__VLR\_IPI\_NDESTAC__\);

     Quando o Campo 33 da SAFX08 \(__IND\_IPI\_INCLUSO__\) estiver desmarcado, considerados os campos 48 \(__VLR\_IPI__\) __\+__ 81 \(__VLR\_IPI\_NDESTAC__\) da SAFX08\.

Para os demais campos, os dados são recuperados dos Resumos por CFOP ou Resumos por CFOP/Natureza, através das tabelas EST\_RES\_CFO\_01 ou EST\_RES\_EXTCFO\.  A leitura dessas tabelas não será alterada, pois é gerada no passo anterior, considerando todas as notas fiscais dos estabelecimentos \(centralizador e centralizados

Com exceção dos campos: Dados da GI/ICMS Entrada e Saída, que são recuperados do Resumo por UF, através da tabela EST\_RES\_UF\_01\. A leitura dessa tabela não será alterada, pois é gerada no passo anterior, considerando todas as notas fiscais dos estabelecimentos \(centralizador e centralizados\)\.

OS 3022 / CH70711\-B

__RN18__

VAF: 

As regras na geração desse quadro não serão modificadas na utilização da geração do relatório por I\.E\.U\.

OS 3022

__RN19__

Detalhamento de Outras Entradas – VAF:

Esse quadro é gerado com os dados incluídos manualmente pelo usuário na tela de manutenção, localizado no módulo: Estadual à VAF\-MG, menu: Preliminares à Manutenção do Detalhamento de Outras Entradas\.

__Alteração da OS3202:__

A partir da OS3202, o quadro “Detalhamento de Outras Entradas” passou a ser OPCIONALMENTE gerado de forma automática, no caso dos contribuintes do tipo “Transportador”\.  Para isso, foi criado um  parâmetro na tela de geração do relatório: 

*     “\[   \] Gerar quadro ”Detalhamento de Outras Entradas” a partir dos índices de participação dos municípios \(Transportadores\)”*

Quando o parâmetro for marcado, a geração do quadro “Detalhamento de Outras Entradas” será feita unicamente através dos dados gerados no cálculo dos índices de participação\. Desta forma, mesmo que existam dados cadastrados previamente na manutenção do menu “Preliminares à Manutenção do Detalhamento de Outras Entradas”, eles *não* serão utilizados\.

Geração automática do quadro “Detalhamento de Outras Entradas”:

Os dados deste quadro serão gerados a partir dos dados armazenados no cálculo dos índices de participação\. 

Para cada município envolvido no cálculo, será gerada uma linha no quadro, da seguinte forma:

Coluna __Município__ à Código do município  \+  Descrição do Município 

__                                       __\(será usado o campo “Município Destino” do DE\-PARA entre os municípios do IBGE e municípios de MG\) 

                                      \(menu “Parâmetros à Municípios do IBGE x Municípios de MG”\)

Coluna __Valor__ à índice de participação calculado \* valor do campo “Outras Entradas” \(quadro VAF\) __\(\*\)__

__\(\*\) __Observar que para os contribuintes do tipo “Transportador”, o valor do campo “Outras Entradas”, que compõe o quadro “VAF”,  é calculado de forma automática, através da fórmula:  SAÍDAS  –  ENTRADAS\.

Importante à Pode acontecer  dos valores rateados entre os municípios não totalizarem exatamente o valor do campo “Outras Entradas”\. Pode haver diferença a maior ou a menor, devido ao arredondamento dos valores\. Quando isso ocorrer, a diferença deverá ser ajustada entre um ou mais municípios para que o total sempre seja = “Outras Entradas”\. Como critério para este ajuste, poderão ser utilizados os municípios de maior índice\.   

OS 3022

OS3202

__RN20__

__Regra para incluir CNPJ no quadro Cadastro de Contribuinte:__

No módulo Estadual → VAF – Valor Adicional Fiscal – MG,

Menu Obrigações → Geração de Relatórios, 

deverá, na geração, no quadro Cadastro do Contribuinte, incluir o campo com a informação CNPJ, que deverá ficar abaixo do campo Inscrição Estadual\.

__CH104167__

__RN21__

Inclusão do Checkbox __“Considerar Colunas de Isentas e Outras \(ICMS\) ”\. __

A seguir as telas em que o parâmetro será incluído:

Módulo Estadual → VAF\- Valor Adicionado Fiscal \- MG

Menu Parâmetros → Exclusões do Valor Adicionado __> por CFOP__

__                                                                                      > por CFOP/Natureza de Operação __

__Regras do Parâmetro:__

Por default o campo estará desmarcado\.

__Regras para Geração do Relatório:__

Se o usuário marcar este Checkbox, na geração do relatório serão apresentados no título “Exclusão do VAF” \(nas descrições de Energia Elétrica/Comunicação e Transporte \(parcela não utilizada\) apenas a somatória dos valores constantes nos campos: __B\. Isenta ICMS__ E __B\. Outras ICMS__ da __SAFX08 __referentes aos documentos fiscais de energia elétrica/comunicação e transporte\.

Se não estiver marcado manter a geração do relatório com o valor contábil na exclusão do VAF\.

__Observação:__ o relatório tem as colunas para NF’s de entradas e outra para as de saídas\.

__MFS\-20715__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

