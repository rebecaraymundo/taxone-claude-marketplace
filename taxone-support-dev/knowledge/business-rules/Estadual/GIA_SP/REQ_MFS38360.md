# REQ_MFS38360

- **Fonte:** REQ_MFS38360.docx
- **Modificado:** 2025-10-09
- **Tamanho:** 114 KB

---

THOMSON REUTERS

__MFS38360 __

__Módulo GIA SP – Geração Automática da DIPAM Código 12__

Revisões

__Data__

__OS/Chamado__

__Descrição__

__Autor__

26/06/2020

MFS38360

<a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK8"></a><a id="OLE_LINK10"></a>Alterar a geração dos dados da DIPAM, para gerar de forma automática o código 12\.

Vânia Mattos

Sumário

[1\.	INTRODUÇÃO	3](#_Toc44326881)

[1\.1	Documentos e Base Legal para a Solução	3](#_Toc44326882)

[2\.	SOLUÇÃO FUNCIONAL / ESCOPO	3](#_Toc44326883)

[2\.1	Procedimentos para Fábrica	3](#_Toc44326884)

[2\.1\.1	Geração dos Registros da GIA SP	3](#_Toc44326885)

[3\.	ROCEDIMENTOS PARA CONTEÚDO	3](#_Toc44326886)

[3\.1	Criação / Alteração – Tabelas \(Manual de Layout\)	3](#_Toc44326887)

[3\.2	Criação / Alteração em telas e relatórios \(manual operacional, roteiro e help\)	4](#_Toc44326888)

[3\.2\.1	Geração dos Registros da GIA SP	4](#_Toc44326889)

[3\.3	Criação / Alteração de Tabelas \(Fixas, Acessórias, Básicas\)	5](#_Toc44326890)

[3\.4	Criação / Alteração de Roteiro Operacional	5](#_Toc44326891)

[3\.5	Outras informações que necessitarão ser atualizadas \(help, manual operacional etc\)	5](#_Toc44326892)

[3\.6	Informações p/ Carta do Patch	5](#_Toc44326893)

[4\.	TESTES	6](#_Toc44326894)

[4\.1	Dicas para montagem do cenário de testes	6](#_Toc44326895)

# <a id="_Toc200962059"></a><a id="_Toc200996459"></a><a id="_Toc200996577"></a><a id="_Toc200998055"></a><a id="_Toc354574223"></a><a id="_Ref354574309"></a><a id="_Ref354574320"></a><a id="_Toc354574398"></a><a id="_Toc354574442"></a><a id="_Toc354574527"></a><a id="_Toc354578073"></a><a id="_Toc354578300"></a><a id="_Toc354578991"></a><a id="_Toc354579132"></a><a id="_Toc44326881"></a>INTRODUÇÃO

O objetivo desta MFS é implementar a geração automática do Código 12 da DIPAM \(reg\.30\), na GIA\-SP\.

A DIPAM é o registro 30 da GIA\-SP, e tem vários tipos de códigos, sendo que o 12 ainda não tem geração automática\. 

A geração seguirá as mesmas regras do registro 1400 do Sped Fiscal para o código DIPAM12, a diferença é que serão utilizadas as parametrizações de CFOP e Produto do módulo da GIA SP, ao invés do Sped\. 

	

## <a id="_Toc44326882"></a>Documentos e Base Legal para a Solução

# <a id="Premissas"></a><a id="_Toc200962060"></a><a id="_Toc200996460"></a><a id="_Toc200996578"></a><a id="_Toc200998056"></a><a id="_Toc354574225"></a><a id="_Toc354574400"></a><a id="_Toc354574444"></a><a id="_Toc354574529"></a><a id="_Toc354578075"></a><a id="_Toc354578302"></a><a id="_Toc354578993"></a><a id="_Toc354579134"></a><a id="_Toc44326883"></a>SOLUÇÃO FUNCIONAL / ESCOPO

  

## <a id="_Toc200962061"></a><a id="_Toc200996461"></a><a id="_Toc200996579"></a><a id="_Toc200998057"></a><a id="_Toc354574226"></a><a id="_Toc354574401"></a><a id="_Toc354574445"></a><a id="_Toc354574530"></a><a id="_Toc354578076"></a><a id="_Toc354578303"></a><a id="_Toc354578994"></a><a id="_Toc354579135"></a><a id="_Toc44326884"></a>Procedimentos para Fábrica

### <a id="_Toc44326885"></a>Geração dos Registros da GIA SP

__Localização__: Menu Estadual, módulo GIA\-SP, menu Obrigações à Nova GIA \- V8\.0 \(V0210\) à Geração à Geração dos Registros 

A geração da GIA será alterada para passar a gerar de forma automática o registro da DIPAM \(reg\. 30\), para o seguinte código: 

                 “12\- Compras *não* escrituradas de mercadorias de produtores agropecuários”  

A alteração esta descrita no seguinte documento de regras:

                                            __MTZ\-GIA\-SP\-Geracao\_dos\_Registros__

                                                       \(ver regra __RN18__\)

	

__Obs__: Na MFS33992 o código 12 foi incluído na lista de códigos do módulo, para permitir ao usuário inserir os valores deste código via manutenção\. E agora, nesta demanda, vamos gerar o código 12 de forma automática\. 

# <a id="_Toc200962071"></a><a id="_Toc200996470"></a><a id="_Toc200996588"></a><a id="_Toc200998068"></a><a id="_Toc354574229"></a><a id="_Toc354574404"></a><a id="_Toc354574448"></a><a id="_Toc354574533"></a><a id="_Toc354578079"></a><a id="_Toc354578306"></a><a id="_Toc354578997"></a><a id="_Toc354579138"></a><a id="_Toc44326886"></a>ROCEDIMENTOS PARA CONTEÚDO

<a id="_Toc199304378"></a><a id="_Toc200962072"></a><a id="_Toc200996471"></a><a id="_Toc200996589"></a><a id="_Toc200998069"></a>

## <a id="_Toc354574230"></a><a id="_Toc354574405"></a><a id="_Toc354574449"></a><a id="_Toc354574534"></a><a id="_Toc354578080"></a><a id="_Toc354578307"></a><a id="_Toc354578998"></a><a id="_Toc354579139"></a><a id="_Toc44326887"></a>Criação / Alteração – Tabelas \(Manual de Layout\)

*\(sem alterações\)*

## <a id="_Toc200996472"></a><a id="_Toc200996590"></a><a id="_Toc200998070"></a><a id="_Toc354574231"></a><a id="_Toc354574406"></a><a id="_Toc354574450"></a><a id="_Toc354574535"></a><a id="_Toc354578081"></a><a id="_Toc354578308"></a><a id="_Toc354578999"></a><a id="_Toc354579140"></a><a id="_Toc44326888"></a>Criação / Alteração em telas e relatórios \(manual operacional, roteiro e help\)

<a id="OLE_LINK3"></a><a id="OLE_LINK4"></a><a id="OLE_LINK7"></a>

### <a id="_Toc44326889"></a>Geração dos Registros da GIA SP

__Localização__: Menu Estadual, módulo GIA\-SP, menu Obrigações à Nova GIA \- V8\.0 \(V0210\) à Geração à Geração dos Registros 

Alterar o help deste item de menu, na parte que descreve os parâmetros do registro 30 \(“__*Parametrização p/ Registro 30 \- DIPAM\-B*__”\)\.

Alterações:

- O campo “__*Período*__”, que no help aparece abaixo do quadrinho que cita os campos de município da SAFX07 e SAFX51, deve ser __reposicionado__ para ficar logo abaixo do campo “Gera DIPAM\-B”, conforme aparece em destaque no trecho a seguir:
- Incluir uma nova observação, conforme destacado no trecho abaixo, como “__*Obs1*__”;

 

<a id="geracao_registros"></a>__Geração dos Registros__

Nesta opção o usuário poderá fazer a geração dos registros, apurando os valores para os tipos de registros 05, 10, 14, 18, 20, 25 e 30\. 

Descrição dos campos:

__\.\.\.\.\.__

__\.\.\.\.\.__

__\.\.\.\.\.__

__\.\.\.\.\.__

__Parametrização p/ Registro 30 – DIPAM\-B: __

__Produto:__ Caso o usuário deseje fazer a geração utilizando a [parametrização](file:///C:/@CVS/MsafDW/conteudo/Conteudo/Help_on_line/Estadual/GIA_SP/oper_safousp.htm#codigo_dipam_b_produto) por produto referente a DIPAM\-B, deverá habilitar este campo\. 

__Gera DIPAM\-B:__ Caso o usuário deseja gerar o registro de DIPAM\-B, basta selecionar este campo\. 

__Período:__ Informar o período para a apuração do registro DIPAM\-B\. 

Este campo somente ficará disponível para o usuário, caso este tenha informado que deseja Gerar DIPAM\-B\. 

__Obs1: __Para a geração dos códigos DIPAM 11 e 12 \(Compras escrituradas e não escrituradas de mercadorias de produtores agropecuários\), será utilizado o Município da pessoa física/jurídica \(SAFX04\) indicada no documento\. Serão consideradas apenas as notas fiscais com CFOP ou CFOP/Natureza parametrizados, e a parametrização de Produtos é opcional \(conforme indicado no campo “Produto”\)\. No caso das compras não escrituradas \(código 12\), serão utilizados os documentos fiscais de classificação = “7” \(campo 12\-Classificação do Documento Fiscal\); 

__Obs2:__ Para a geração dos dados de transporte da DIPAM \(código "23"\) será utilizado sempre a UF e o município de origem da capa da Nota Fiscal\. Casos esses campos não estejam preenchidos e a Nota tenha classificação de conhecimento de frete\(4,5 ou 6\), será recuperado o município de coleta dos itens de frete \(SAFX51\)\. Os campos em questão são os seguintes:

 

__Tabela__

__Campo__

SAFX07

117 \- UF Origem

182 \- Município Origem

SAFX51

42 \- Município Coleta

__\.\.\.\.\.__

__\.\.\.\.\.__

__\.\.\.\.\.__

__\.\.\.\.\.__

__\.\.\.\.\.__

__\.\.\.\.\.__

## <a id="_Toc44326890"></a>Criação / Alteração de Tabelas \(Fixas, Acessórias, Básicas\)

<a id="OLE_LINK13"></a>*\(sem alterações\)*

## <a id="_Toc354574233"></a><a id="_Toc354574408"></a><a id="_Toc354574452"></a><a id="_Toc354574537"></a><a id="_Toc354578083"></a><a id="_Toc354578310"></a><a id="_Toc354579001"></a><a id="_Toc354579142"></a><a id="_Toc44326891"></a>Criação / Alteração de Roteiro Operacional

*\(sem alterações\)*

## <a id="_Toc354574234"></a><a id="_Toc354574409"></a><a id="_Toc354574453"></a><a id="_Toc354574538"></a><a id="_Toc354578084"></a><a id="_Toc354578311"></a><a id="_Toc354579002"></a><a id="_Toc354579143"></a><a id="_Toc44326892"></a>Outras informações que necessitarão ser atualizadas \(help, manual operacional etc\)

*\(sem alterações\)*

## <a id="_Toc426992014"></a><a id="_Toc428981618"></a><a id="_Toc44326893"></a>Informações p/ Carta do Patch

<a id="OLE_LINK49"></a><a id="OLE_LINK16"></a><a id="OLE_LINK42"></a><a id="OLE_LINK46"></a>__*Módulo*__*: GIA\-SP*

__*Resumo da Alteração:*__* Geração do código 12 da DIPAM\-B \(registro 30\)\. *

__*Descritivo das Alterações*__*: A geração da GIA SP foi alterada para gerar de forma automática, o código 12 da DIPAM\-B \(registro 30\): *

*              “12\- Compras não escrituradas de mercadorias de produtores agropecuários”  *

*Para a geração do código 12 serão utilizadas as mesmas regras da geração do registro 1400 do Sped Fiscal, uma vez que o código DIPAM12 já tem geração automática para a EFD\. A geração é feita a partir dos documentos fiscais de classificação = “7” \(campo 12\-Classificação do Documento Fiscal\)\.*

*Para mais detalhes sobre a geração do código 12, consultar o help do menu “Obrigações > Nova GIA \- V8\.0 \(V0210\) > Geração > Geração dos Registros” do Módulo GIA SP\.*

*\- Módulos Impactados:* GIA\-SP

# <a id="_Toc200962062"></a><a id="_Toc200996464"></a><a id="_Toc200996582"></a><a id="_Toc200998062"></a><a id="_Toc354574235"></a><a id="_Toc354574410"></a><a id="_Toc354574454"></a><a id="_Toc354574539"></a><a id="_Toc354578085"></a><a id="_Toc354578312"></a><a id="_Toc354579003"></a><a id="_Toc354579144"></a><a id="_Toc44326894"></a>TESTES

## <a id="_Toc44326895"></a>Dicas para montagem do cenário de testes

- Verificar se todos os filtros da recuperação das notas, conforme definido em regra,  estão funcionando corretamente;

 

- Utilizar parametrização das notas por CFOP;
- Utilizar parametrização das notas por CFOP/Natureza de Operação;
- Utilizar a parametrização de Produtos, lembrando que, como esta parametrização é opcional, deve\-se validar a geração utilizando, e não utilizando a parametrização; 
- Utilizar notas fiscais de diferentes pessoas fis/jur, de municípios de SP diferentes;
- Utilizar também, notas fiscais de pessoas fis/jur que *não* sejam de SP, para verificar se de fato estas notas não serão consideradas;
- Verificar se o município gravado na tabela, conforme os dados demonstrados na tela da manutenção, é realmente o município da Tabela de Municípios de SP \(DE\-PARA Município IBGE x Município SP\); 
- Testar a geração “normal” e geração por Inscrição Estadual Única;

__*\(verificar demais regras a serem validadas no documentos de regras\)*__

= = = = =

