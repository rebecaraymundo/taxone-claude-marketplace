# REQ_MFS564110_IEU_Meio_Magnético

- **Fonte:** REQ_MFS564110_IEU_Meio_Magnético.docx
- **Modificado:** 2023-09-14
- **Tamanho:** 115 KB

---

THOMSON REUTERS

__MFS564110__

__Scanc__

__Scanc – Refinaria – Geração Meio Magnético__

Revisões

__Data__

__OS/Chamado__

__Descrição__

__Autor__

11/09/2023

MFS 564110

Inclusão da opção IEU e Filtro de UF na parametrização da Rotina de Geração do Meio Magnético – Refinaria \- Scanc

Graciela Soares

  

Sumário

[1\.	INTRODUÇÃO	3](#_Toc145439834)

[1\.1	Documentos e Base Legal para a Solução	3](#_Toc145439835)

[2\.	SOLUÇÃO FUNCIONAL / ESCOPO	3](#_Toc145439836)

[2\.1	Procedimentos para Fábrica	3](#_Toc145439837)

[2\.1\.1	Inclusão da opção de Filtro por Inscrição Estadual Única:	3](#_Toc145439838)

[2\.1\.2	Inclusão da opção de Filtro por UF:	3](#_Toc145439839)

[2\.2	Procedimentos para Interface	4](#_Toc145439840)

[3\.	PROCEDIMENTOS PARA CONTEÚDO	4](#_Toc145439841)

[3\.1	Criação / Alteração – Tabelas \(Manual de Layout\)	4](#_Toc145439842)

[3\.1\.1	Manual de Layout	4](#_Toc145439843)

[3\.2	Criação / Alteração em telas e relatórios \(manual operacional, roteiro e help\)	4](#_Toc145439844)

[3\.2\.1	Geração dos Arquivos Magnéticos \- Scanc	4](#_Toc145439845)

[Anexos VI, VI\-M, VII e VII\-M	5](#_Toc145439846)

[3\.3	Criação / Alteração de Tabelas \(Fixas, Acessórias, Básicas\)	6](#_Toc145439847)

[3\.4	Criação / Alteração de Roteiro Operacional	6](#_Toc145439848)

[3\.5	Outras informações que necessitarão ser atualizadas \(help, manual operacional etc\)	6](#_Toc145439849)

[3\.6	Informações p/ Carta do Patch	6](#_Toc145439850)

[4\.	TESTES	7](#_Toc145439851)

# <a id="_Toc200962059"></a><a id="_Toc200996459"></a><a id="_Toc200996577"></a><a id="_Toc200998055"></a><a id="_Toc354574223"></a><a id="_Ref354574309"></a><a id="_Ref354574320"></a><a id="_Toc354574398"></a><a id="_Toc354574442"></a><a id="_Toc354574527"></a><a id="_Toc354578073"></a><a id="_Toc354578300"></a><a id="_Toc354578991"></a><a id="_Toc354579132"></a><a id="_Toc145439834"></a>INTRODUÇÃO

Ajuste no Filtro de Parametrização da Rotina de Geração dos Arquivos Magnéticos dos Movimentos de Refinaria do modulo de Combustíveis e Derivados de Petróleo:

\- Inclusão da opção de filtro por Estabelecimento com Inscrição Estadual Única

\- Inclusão de Filtro por UF

## <a id="_Toc145439835"></a>Documentos e Base Legal para a Solução

# <a id="Premissas"></a><a id="_Toc200962060"></a><a id="_Toc200996460"></a><a id="_Toc200996578"></a><a id="_Toc200998056"></a><a id="_Toc354574225"></a><a id="_Toc354574400"></a><a id="_Toc354574444"></a><a id="_Toc354574529"></a><a id="_Toc354578075"></a><a id="_Toc354578302"></a><a id="_Toc354578993"></a><a id="_Toc354579134"></a><a id="_Toc145439836"></a>SOLUÇÃO FUNCIONAL / ESCOPO

## <a id="_Toc200962061"></a><a id="_Toc200996461"></a><a id="_Toc200996579"></a><a id="_Toc200998057"></a><a id="_Toc354574226"></a><a id="_Toc354574401"></a><a id="_Toc354574445"></a><a id="_Toc354574530"></a><a id="_Toc354578076"></a><a id="_Toc354578303"></a><a id="_Toc354578994"></a><a id="_Toc354579135"></a><a id="_Toc145439837"></a>Procedimentos para Fábrica

### <a id="_Toc145439838"></a>Inclusão da opção de Filtro por Inscrição Estadual Única:

__Localização no DW__: Menu Específicos  Combustíveis e Derivados de Petróleo,

Menu \-> Movimento Refinaria \-> Geração dos Arquivos Magnéticos – Scanc \-> Anexos VI e VII 

Inclusão de um __*Check\-Box*__ com filtro de nome “Inscrição Estadual Única” que ao ser marcado filtre os estabelecimentos de centralizados por inscrição estadual única e também os descentralizados\.

Exemplo de Tela:

![](data:image/png;base64,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)

### <a id="_Toc145439839"></a>Inclusão da opção de Filtro por UF:

__Localização no DW__: Menu Específicos  Combustíveis e Derivados de Petróleo,

Menu \-> Movimento Refinaria \-> Geração dos Arquivos Magnéticos – Scanc \-> Anexos VI e VII 

Inclusão de uma __*Lista*__ com filtro de nome __“Pesquisa UF \(Estabelecimento\)”__ contendo todas as UF´s constantes na tabela __“Estado” __mais a opção __“Todos”__\.

Na seleção do estado correspondente deve\-se verificar na tabela__ “Estabelecimento”__ a UF correspondente e apresentar na lista de seleção todos os Estabelecimentos do estado selecionado\. 

Exemplo de Tela:

![](data:image/png;base64,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)

## <a id="_Toc354574228"></a><a id="_Toc354574403"></a><a id="_Toc354574447"></a><a id="_Toc354574532"></a><a id="_Toc354578078"></a><a id="_Toc354578305"></a><a id="_Toc354578996"></a><a id="_Toc354579137"></a><a id="_Toc145439840"></a>Procedimentos para Interface

<a id="_Toc200962071"></a><a id="_Toc200996470"></a><a id="_Toc200996588"></a><a id="_Toc200998068"></a>Não há

# <a id="_Toc354574229"></a><a id="_Toc354574404"></a><a id="_Toc354574448"></a><a id="_Toc354574533"></a><a id="_Toc354578079"></a><a id="_Toc354578306"></a><a id="_Toc354578997"></a><a id="_Toc354579138"></a><a id="_Toc145439841"></a>PROCEDIMENTOS PARA CONTEÚDO

<a id="_Toc199304378"></a><a id="_Toc200962072"></a><a id="_Toc200996471"></a><a id="_Toc200996589"></a><a id="_Toc200998069"></a>

## <a id="_Toc354574230"></a><a id="_Toc354574405"></a><a id="_Toc354574449"></a><a id="_Toc354574534"></a><a id="_Toc354578080"></a><a id="_Toc354578307"></a><a id="_Toc354578998"></a><a id="_Toc354579139"></a><a id="_Toc145439842"></a>Criação / Alteração – Tabelas \(Manual de Layout\)

### <a id="_Toc145439843"></a>Manual de Layout 

Não há

## <a id="_Toc200996472"></a><a id="_Toc200996590"></a><a id="_Toc200998070"></a><a id="_Toc354574231"></a><a id="_Toc354574406"></a><a id="_Toc354574450"></a><a id="_Toc354574535"></a><a id="_Toc354578081"></a><a id="_Toc354578308"></a><a id="_Toc354578999"></a><a id="_Toc354579140"></a><a id="_Toc145439844"></a>Criação / Alteração em telas e relatórios \(manual operacional, roteiro e help\)

<a id="OLE_LINK3"></a><a id="OLE_LINK4"></a><a id="OLE_LINK7"></a>

Alteração no Manual Operacional do módulo Combustíveis e Derivados de Petróleo\.

### <a id="_Toc145439845"></a>Geração dos Arquivos Magnéticos \- Scanc 

__Localização no DW__: Menu Específicos  Combustíveis e Derivados de Petróleo,

Menu \-> Movimento Refinaria \-> Geração dos Arquivos Magnéticos – Scanc \-> Anexos VI e VII 

Incluir o texto marcado em Verde:

Esta rotina possibilita a geração dos arquivos referentes aos Anexos VI, VI\-M, VII e VII\-M, e Notas Fiscais\.

### <a id="menu_mov_refscanc_anexos"></a><a id="_Toc145439846"></a>Anexos VI, VI\-M, VII e VII\-M

Nesta rotina o usuário pode fazer a [geração do arquivo magnético](https://webhelp.thomsonreuters.com.br/Site/HELPDW/V2R010/Especificos/combustiveis_e_derivados/rot_safcomb.htm#proc_scanc_ref) no layout definido pelo aplicativo SCANC \- Refinarias\. O arquivo conterá os dados dos Anexos VI, VI\-M, VII e VII\-M de um determinado período \(mês/ano\), e de um ou vários estabelecimentos\.

__Obs\.:__ Os anexos VI, VI\-M, VII e VII\-M gerados deverão ser importados pelo aplicativo SCANC \- Refinarias, acompanhado do relatório de conferência, que demonstra os dados gravados no arquivo\.

Inicialmente esta tela de geração só apresenta as opções de __Parâmetros__ e __Processos__, após a execução, são disponibilizadas as demais opções: __Log__, __Arquivos__ e __Conferência do Meio Magnético__\.

Para a correta geração, o usuário deve preencher nas respectivas abas, as seguintes informações:

__\- Parâmetros:__

__Tipo de Execução:__ Informar o tipo de execução, podendo ser: Imediata ou Programada\.

__Data/Hora de Execução:__ Informar a data e hora que deseja fazer a execução da geração do arquivo\.

__Obs\.:__ Este campo está disponível, caso o usuário tenha selecionado a opção "Programada" no campo Tipo de Execução\.

__Mês/Ano Referência:__ Informar o período \(mês/ano\) para geração\.

__Local:__ Informar o município de execução do arquivo\.

__Pesquisa UF \(Estabelecimento\):__ lista contendo todas as UF’s mais a opção “Todos”\. 

__Inscrição Estadual Única:__ caso essa opção seja selecionada, serão apresentados apenas os estabelecimentos Centralizadores e Descentralizados\.

__Estabelecimentos: __Lista todos os estabelecimentos cadastrados, para que o usuário selecione quais estabelecimentos que deseja fazer a geração\. Tendo a opção de selecionar todos e desmarcar todos automaticamente\.

## <a id="_Toc145439847"></a>Criação / Alteração de Tabelas \(Fixas, Acessórias, Básicas\)

## <a id="_Toc354574233"></a><a id="_Toc354574408"></a><a id="_Toc354574452"></a><a id="_Toc354574537"></a><a id="_Toc354578083"></a><a id="_Toc354578310"></a><a id="_Toc354579001"></a><a id="_Toc354579142"></a><a id="_Toc145439848"></a>Criação / Alteração de Roteiro Operacional

## <a id="_Toc354574234"></a><a id="_Toc354574409"></a><a id="_Toc354574453"></a><a id="_Toc354574538"></a><a id="_Toc354578084"></a><a id="_Toc354578311"></a><a id="_Toc354579002"></a><a id="_Toc354579143"></a><a id="_Toc145439849"></a>Outras informações que necessitarão ser atualizadas \(help, manual operacional etc\)

## <a id="_Toc426992014"></a><a id="_Toc428981618"></a><a id="_Toc145439850"></a>Informações p/ Carta do Patch

<a id="OLE_LINK49"></a><a id="OLE_LINK16"></a><a id="OLE_LINK42"></a><a id="OLE_LINK46"></a>__Carta do Patch – DW e TAXONE__:

* *

__Módulo__: Combustíveis e Derivados de Petróleo

  


__Resumo da alteração: __Inclusão de novas opções de filtros na tela de parametrização da Rotina de Geração dos Arquivos Magnéticos do Scanc Refinaria Anexos VI e VII\.

Foram disponibilizadas opções adicionais de Filtro na tela de Parametrização da Rotina de Geração dos Arquivos Magnéticos do Scanc Anexos VI e VII dos Movimentos de Refinaria do módulo de Combustíveis e Derivados de Petróleo:

\- Inclusão da opção de filtro por Estabelecimento com Inscrição Estadual Única

\- Inclusão de Filtro por UF

 

Funcionalidades atualizadas:  
  
Módulo Impactado: Combustíveis e Derivados de Petróleo

Menu \-> Movimento Refinaria \-> Geração dos Arquivos Magnéticos – Scanc \-> Anexos VI e VII 

# <a id="_Toc200962062"></a><a id="_Toc200996464"></a><a id="_Toc200996582"></a><a id="_Toc200998062"></a><a id="_Toc354574235"></a><a id="_Toc354574410"></a><a id="_Toc354574454"></a><a id="_Toc354574539"></a><a id="_Toc354578085"></a><a id="_Toc354578312"></a><a id="_Toc354579003"></a><a id="_Toc354579144"></a><a id="_Toc145439851"></a>TESTES

= = = = =

