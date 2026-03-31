# MTZ_EFD_Parametros_Registro_1400_EspecificoUF_Deducoes_CFOP

- **Fonte:** MTZ_EFD_Parametros_Registro_1400_EspecificoUF_Deducoes_CFOP.docx
- **Modificado:** 2025-11-19
- **Tamanho:** 80 KB

---

THOMSON REUTERS

                                        __Módulo Sped Fiscal__

__Parametrização por CFOP das Operações a serem Deduzidas__

__   na Geração do Registro 1400 \(regras específicas por UF\) __

__Localização__: Menu Sped, Módulo EFD \- Escrituração Fiscal Digital, item Parâmetros 🡪 Registro 1400 🡪 Específico por UF 🡪 Deduções 🡪 CFOP

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS4728\-A

Atendimento à Resolução 4\.730, de 17/12/14, SEF\-MG

Criação de parametrização das operações a serem deduzidas no cálculo do Valor Adicionado \(Reg 1400\) p/a opção de geração do tipo “Específico por UF”\.

27/03/2015

\(criação do docto\)

MFS1566

Portaria N\. 34\-R, Sefaz\-ES

Inclusão dos códigos 05 e 10 para o estado do ES \(ver __RN02__ e __RN03__\)

14/09/20915

MFS3248

Orientação Técnica EFD nº 011/2016 – Versão 1\.10

Inclusão dos códigos para o estado do RN \(ver __RN02__ e __RN03__\)

11/11/2016

MFS7449

Alteração do 1400 p/ SP

Inclusão dos códigos 23 e 24 de SP na parametrização das deduções\.

24/01/2017

CH13531\_2017 \(MFS12315\)

Alteração do 1400 p/ RS

Inclusão do código 01 de RS na parametrização das deduções\.

04/08/2017

\(MFS14605\)

Alteração do 1400 p/ MG

Inclusão do código “Produtos Agropecuários” na parametrização das deduções\.

23/02/2018

MFS16811

Alteração do 1400 p/ BA

Inclusão de códigos p/ BA na parametrização das deduções\.

07/03/2018

MFS17764

Alteração do 1400 p/ TO

Inclusão de códigos p/ TO na parametrização das deduções\.

25/04/2018

MFS30891

Inclusão da observação

Inclusão da observação para o campo Operação\.

09/10/2019

MFS31044

Alteração do 1400 p/ TO

Inclusão de um código para o estado de TO

29/10/2019

MFS43147

Inclusão de código

Inclusão do código ACIPMS04 para o estado do Acre\.

10/08/2021

MFS35318

Inclusão de código

Inclusão do código TOIPMS10 para o estado de Tocantins\.

19/08/2021

MFS94497

Inclusão de código

Inclusão do código 1201 para o estado de Alagoas\.

25/10/2022

MFS663539

Inclusão de códigos

Inclusão de códigos BAE21\.\.\. BAE24, BAS21\.\.\.BAS24

30/07/2024

MFS651592

Inclusão de códigos

Inclusão do código PI003

27/08/2024

MFS672643

Inclusão de códigos

Inclusão do código Outras Entradas a Detalhar por Municipio \(especifico para 3\.6\.14\)

17/01/2025

	

REGRAS DE NEGÓCIO

__RN00__

__                                          Regras Gerais__

Esta parametrização foi criada na __OS4728\-A__ com objetivo de atender a geração do registro 1400 de acordo com as regras específicas das UF’s que criaram tabelas específicas para a geração do registro 1400 \(“Tabela de Itens UF Índice de Participação dos Municípios“\)\.

A princípio, ela será utilizada apenas para um dos códigos da tabela do estado de MG, e também para dois códigos do ES: ESIPM05 e ESIPM10 \(ver __RN02__\)\.

Na __MFS1566__ \(Set/2015\) foram incluídos os itens 05 e 10 do estado do ES \(Portaria n\. 34\-R, de Ago/2015\)\. 

Na __MFS3248__ \(Nov/2016\) foram incluídos os itens 4\.1, 4\.2, 4\.3, 4\.5, 4\.6 e 5\.1 do estado do RN \(Orientação Técnica EFD nº 011/2016 – Versão 1\.10\)\. 

<a id="OLE_LINK11"></a><a id="OLE_LINK12"></a><a id="OLE_LINK13"></a>Na __MFS7449__ \(Jan/2017\) foram incluídos os itens 23 e 24 \(Transportes e Comunicação\) do estado de SP \(DIPAM\-SP\)\. 

Na __MFS12315__ \(Ago/2017\) foi incluído o item 01 \(Transportes\) do estado do RS\.

Na __MFS14605__ \(Fev/2018\) foi incluído o item Produtos Agropecuários do estado de MG\.

<a id="_Hlk508204463"></a>Na __MFS16811__ \(Mar/2018\) foram incluídos os itens BAE01, BAS01, BAE02, BAS02, BAE03, BAS03, BAE04 e BAS04 do estado da BA\.

<a id="_Hlk512447603"></a>Na __MFS17764__ \(Abr/2018\) foram incluídos os itens TOIPME04, TOIPMS04, TOIPME06, TOIPMS06, TOIPME07, TOIPMS07, TOIPME08 e TOIPMS08 do estado de TO \(Portaria nº 265, de 23 de março de 2018\)\.

Na __MFS31044__ \(Out/2019\) foi incluída a operação TOIPME10 para TO\.

Na __MFS43147__ \(Agosto/2021\) foi incluída a operação ACIPMS04 para AC\.

Na __MFS35318__ \(Agosto/2021\) foi incluída a operação TOIPMS10 para TO\.

Na __MFS94497__ \(Outubro/2022\) foi incluída a operação 1201 para AL\.

<a id="_Hlk173262680"></a>Na __MFS663539 __\(Julho/2024\) foram incluídas as operações BAE21, BAE22, BAE23, BAE24, BAS21, BAS22, BAS23,BAS24 para BA\.

<a id="_Hlk175658375"></a>Na __MFS651592__ \(Ago/2024\) foi incluída a operação PI003 para Piauí\.

Na __MFS672643 __\(Janeiro/2025\) foi incluída a operação “Outras\_Entradas\_a\_Detalhar\_por\_Municipio \(especifico para 3\.6\.14\)”, para MG\.

Opções da barra de menu:

__Confirma__ 🡪 salva os dados incluídos ou alterados para o estabelecimento e operação em questão; 

__Relatório__ 🡪 Esta opção permite a emissão de relatório de conferência dos dados parametrizados, conforme padrão das telas de manutenção\. Os critérios para emissão do relatório são Estabelecimento e Operação\. O usuário deverá obrigatoriamente selecionar um estabelecimento, e opcionalmente escolher uma operação específica, se desejar\. Serão listados todos os dados parametrizados para os critérios selecionados;

__Fecha__ 🡪 fecha a janela da parametrização;

__RN01__

__                                          Campo Estabelecimento:__

__Estabelecimento__ 🡪 Este campo é uma lista dos estabelecimentos da empresa do login para seleção do usuário\. Quando for informado um estabelecimento no login, o campo mostrará fixo este estabelecimento, e usuário não poderá alterá\-lo\.

__RN02__

__                                          Campo Operação:__

__Operação__ 🡪 Este campo é uma lista, que a princípio exibirá apenas a seguinte operação de MG:

MG – Outras Entradas a Detalhar por Município

O campo fica desabilitado, já que a princípio somente serão tratadas deduções para este tipo de operação\. 

Alteração da __MFS1566__: Incluídos os códigos ESIPM05 e ESIPM10 p/o estado do ES\. Com a inclusão destes códigos, este campo passa a funcionar da seguinte forma: 

<a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>Alteração da __MFS7449__: Incluídos os códigos SPDIPAM23 e SPDIPAM24 p/o estado de SP\. Com a inclusão destes códigos, este campo passa a funcionar da seguinte forma: 

__Operação__ 🡪 Este campo é uma lista que exibirá as seguintes operações:

MG – Outras Entradas a Detalhar por Município

MG – Produtos Agropecuários

MG \- Outras\_Entradas\_a\_Detalhar\_por\_Municipio \(especifico para 3\.6\.14\)

ES – ESIPM05 \(Distribuição de Energia Elétrica\) 

ES – ESIPM10 \(Distribuição de Gás Canalizado\)

RN – IPM 4\.1 \(Prestação de Serviço de Transporte Rodoviário de Cargas\)

RN – IPM 4\.2 \(Prestação de Serviço de Transporte Aéreo de Cargas\)

RN – IPM 4\.3 \(Prestação de Serviço de Transporte Aquaviário de Cargas\)

RN – IPM 4\.5 \(Atividades de Distribuição de Energia Elétrica\)

RN – IPM 4\.6 \(Atividades de Prestação de Serviços de Comunicação/Telecomunicação\)

RN – IPM 5\.1 \(Atividades de Prestação de Serviço de Transporte Dutoviário/Ferroviário\)

SPDIPAM23

SPDIPAM24

RS – 01 \(Transportes\)

BAE01

BAS01

BAE02

BAS02

BAE03

BAS03

BAE04

BAS04

BAE21

BAS21

BAE22

BAS22

BAE23

BAS23

BAE24

BAS24

TOIPME04

TOIPMS04

TOIPME06

TOIPMS06

TOIPME07

TOIPMS07

TOIPME08

TOIPMS08

TOIPME10

TOIPMS10

ACIPMS04

1201

PI003

A lista exibirá *apenas* os códigos referentes à UF do estabelecimento informado, da seguinte forma:

     \- Se estabelecimento de MG 🡪 aparecerá apenas o código de MG;

     \- Se estabelecimento do ES 🡪 aparecerão apenas os códigos do ES;

     \- Se estabelecimento do RN 🡪 aparecerão apenas os códigos do RN;

     \- Se estabelecimento de SP 🡪 aparecerão apenas os códigos de SP;

     \- Se estabelecimento do RS 🡪 aparecerão apenas os códigos do RS;

<a id="_Hlk508204729"></a>     \- Se estabelecimento da BA 🡪 aparecerão apenas os códigos da BA;

<a id="_Hlk512447635"></a>     \- Se estabelecimento de TO 🡪 aparecerão apenas os códigos da TO;

     \- Se estabelecimento de AC 🡪 aparecerão apenas os códigos da AC;  

     \- Se estabelecimento de AL 🡪 aparecerão apenas os códigos da AL;  

<a id="_Hlk175658646"></a>     \- Se estabelecimento de PI 🡪 aparecerão apenas os códigos do PI;

*\(mesma lógica utilizada na parametrização de CFOP\)*

Após a escolha do estabelecimento e da operação, o campo “CFOP’s” exibirá a lista dos cfop’s disponíveis para cada tipo de operação, onde estarão marcados os CFOP’s já selecionados anteriormente, quando for o caso\.

Observação sobre a parametrização das deduções:

MG 🡪 A parametrização é utilizada: \- na apuração do código “Outras Entradas”, seguindo as orientações da Resolução 4730/2014, SEF\-MG; \- na apuração do código “Produtos Agropecuários”, seguindo as orientações da Portaria Nº 149/2016\.

<a id="OLE_LINK20"></a><a id="OLE_LINK21"></a><a id="OLE_LINK22"></a>SP 🡪 A geração dos códigos da DIPAM\-B *não* trabalha com deduções, pois a princípio a geração foi feita seguindo as mesmas regras da GIA\-SP \(registro 30\) passou a trabalhar com deduções apenas para os códigos 23 e 24 \(MFS7449\)\.

ES 🡪 A parametrização é utilizada apenas na apuração dos códigos ESIPM05 e ESIPM10 \(EE e Gás\), conforme orientação dos itens 3\.5 e 3\.10 da Portaria 34\-R, Ago/2015, Sefaz\-ES\.

RN 🡪 A parametrização é utilizada apenas na apuração dos códigos “4\.1, 4,2, 4\.3, 4\.5, 4\.6 e 5\.1”, seguindo as orientações da OT EFD nº 011/2016, SET\-RN\.

RS 🡪 A parametrização é utilizada apenas na apuração do código “01\-Transportes” que passou a trabalhar com deduções para aquisição dos serviços\.

BA 🡪 A parametrização é utilizada apenas na apuração dos códigos “BAE01, BAS01, BAE02, BAS02, BAE03, BAS03, BAE04, BAS04”, BAE21, BAE22, BAE23, BAE24, BAS21, BAS22, BAS23 e BAS24, seguindo as orientações da EFD – Registro 1400 – Orientações de Preenchimento – Sefaz/BA\.

TO 🡪 A parametrização é utilizada apenas na apuração dos códigos “TOIPME04, TOIPMS04, TOIPME06, TOIPMS06, TOIPME07, TOIPMS07, TOIPME08, TOIPMS08 e TOIPME10”, seguindo as orientações da Portaria nº 265, de 23 de março de 2018\.

AC 🡪 A parametrização é utilizada apenas na apuração do código “ACIPMS04”\.

AL 🡪 A parametrização é utilizada apenas na apuração do código “1201”\.

PI 🡪 A parametrização é utilizada apenas na apuração do código “PI003”\.

<a id="_Hlk21512021"></a>__\[MFS30891\]__

Incluir uma observação no final da tela referente ao campo Operação:

“A exibição do conteúdo para o campo Operação dependerá da UF do Estabelecimento selecionado\. Apenas os Estabelecimentos cuja UF determina uma forma específica de geração apresentarão conteúdo para o campo\. Verifique as orientações específicas de cada UF no Manual do Produto\.”

__RN03__

__                                          Campo CFOP’s:__

__CFOP’s__ 🡪 Neste campo será demonstrada a lista dos cfop’s que poderão ser selecionados pelo usuário\. 

Serão disponibilizados apenas os CFOP’s referentes ás operações de entrada\.

Alteração da __MFS1566__: Incluídos os códigos ESIPM05 e ESIPM10 p/o estado do ES\. Com a inclusão destes códigos, este campo passa a funcionar da seguinte forma: 

Alteração da __MFS7449__: Incluídos os códigos SPDIPAM23 e SPDIPAM24 p/o estado de SP\. Com a inclusão destes códigos, este campo passa a funcionar da seguinte forma:

O tipo dos cfop’s a serem disponibilizados \(entrada ou saída\), depende do tipo da operação do campo “*Operação*”, da seguinte forma:

__Operação__

__CFOP’s a serem exibidos__

__UF__

__Código__

MG

Outras Entradas a Detalhar por Municipio

Apenas os CFOP’s de entrada

MG

Produtos Agropecuários

Apenas os CFOP’s de entrada

MG

Outras\_Entradas\_a\_Detalhar\_por\_Municipio \(especifico para 3\.6\.14\)

Apenas os CFOP’s de entrada

ES

ESIPM05 \(Distribuição de Energia Elétrica\)

Apenas os CFOP’s de entrada

ES

ESIPM10 \(Distribuição de Gás Canalizado\)

Apenas os CFOP’s de entrada

RN

IPM 4\.1 \(Prestação de Serviço de Transporte Rodoviário de Cargas\)

Apenas os CFOP’s de entrada

RN

IPM 4\.2 \(Prestação de Serviço de Transporte Aéreo de Cargas\)

Apenas os CFOP’s de entrada

RN

IPM 4\.3 \(Prestação de Serviço de Transporte Aquaviário de Cargas\)

Apenas os CFOP’s de entrada

RN

IPM 4\.5 \(Atividades de Distribuição de Energia Elétrica\)

Apenas os CFOP’s de entrada

RN

IPM 4\.6 \(Atividades de Prestação de Serviços de Comunicação/Telecomunicação\)

Apenas os CFOP’s de entrada

RN

IPM 5\.1 \(Atividades de Prestação de Serviço de Transporte Dutoviário/Ferroviário\)

Apenas os CFOP’s de entrada

SP

SPDIPAM23

Apenas os CFOP’s de entrada

SP

SPDIPAM24

Apenas os CFOP’s de entrada

RS

01 \(Transportes\)

Apenas os CFOP’s de entrada

BA

BAE01

Apenas os CFOP’s de saída

BA

BAS01

Apenas os CFOP’s de entrada

BA

BAE02

Apenas os CFOP’s de saída

BA

BAS02

Apenas os CFOP’s de entrada

BA

BAE03

Apenas os CFOP’s de saída

BA

BAS03

Apenas os CFOP’s de entrada

BA

BAE04

Apenas os CFOP’s de saída

BA

BAS04

Apenas os CFOP’s de entrada

BA

BAE21

Apenas os CFOP’s de saída

BA

BAS21

Apenas os CFOP’s de entrada

BA

BAE22

Apenas os CFOP’s de saída

BA

BAS22

Apenas os CFOP’s de entrada

BA

BAE23

Apenas os CFOP’s de saída

BA

BAS23

Apenas os CFOP’s de entrada

BA

BAE24

Apenas os CFOP’s de saída

BA

BAS24

Apenas os CFOP’s de entrada

TO

TOIPME04

Apenas os CFOP’s de saída

TO

TOIPMS04

Apenas os CFOP’s de entrada

TO

TOIPME06

Apenas os CFOP’s de saída

TO

TOIPMS06

Apenas os CFOP’s de entrada

TO

TOIPME07

Apenas os CFOP’s de saída

TO

TOIPMS07

Apenas os CFOP’s de entrada

TO

TOIPME08

Apenas os CFOP’s de saída

TO

TOIPMS08

Apenas os CFOP’s de entrada

TO

TOIPME10

Apenas os CFOP’s de saída

TO

TOIPMS10

Apenas os CFOP’s de entrada

AC

ACIPMS04

Apenas os CFOP’s de entrada

AL

1201

Apenas os CFOP’s de entrada

PI

PI003

Apenas os CFOP’s de entrada

Como facilitador, poderão ser utilizadas as opções “*Marcar todos*” e “*Desmarcar todos*”, para marcar ou desmarcar todos os cfop’s simultaneamente\.

__RN04__

__                        Campo Replicar para os estabelecimentos:__

A opção “Replicar para os estabelecimento” é um checkbox que permite ao usuário replicar a parametrização em questão para outros estabelecimentos, conforme o padrão de diversas telas de parametrização do Mastersaf\.

Como default, o campo estará desmarcado na abertura da tela\.

Para replicação estarão disponíveis todos os estabelecimentos da empresa do login, que forem da mesma UF do estabelecimento informado\. 

Como facilitador, poderão ser utilizadas as opções “*Marcar todos*” e “*Desmarcar todos*”, para marcar ou desmarcar todos os estabelecimentos\.

= = = = = 

