# MTZ-Ferramentas-Importacao_TFIX_TACES

- **Fonte:** MTZ-Ferramentas-Importacao_TFIX_TACES.docx
- **Modificado:** 2026-03-17
- **Tamanho:** 850 KB

---

    

# Módulo Ferramentas – Importação das Tabelas Fixas e Acessórias 

# \(TFIX e TACES\)

Menu Básicos, Módulo: Ferramentas, Menu Tabelas Internas à Importar à Tabelas Fixas/Acessórias

*\(Obs: As regras descritas neste documento estão numeradas de acordo com a numeração das tabelas internas \(TFIX e TACES\), para facilitar a consulta\) *

*\(As regras gerais, que não dizem respeito a nenhuma das tabelas especificamente, podem ser incluídas na regra numerada como RN00\)*

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3146\_A

Criação de novos campos p/atendimento à Resolução 3884/2007 – MG\.

O objetivo desta OS é a criação de novos campos em tabelas SAFX para atender às informações solicitadas na Resolução 3\.884 – MG\.

CH88685

Criação de nova TACES para alimentar a tabela DWT\_COD\_FISCAL\_SERV

Este documento tem o objetivo de criar a TACES69 para que a mesma possa alimentar a tabela DWT\_COD\_FISCAL\_SERV\.

OS3065\-DW

Alterações Mastersaf p/ atendimento ao SEF II \- PE 

Alterações Mastersaf p/ atendimento ao SEF II – PE

OS3720

DW \- FEDERAL \- INTERFACE GID \- alteração da geração do campo 04 arquivo ESTIMADO

O cliente BNDES abriu um chamado de número 405\_2012 solicitando a inclusão de sinal negativo para o resultado do cálculo “Total Créditos – Total Débitos” ao gerar o arquivo ESTIMADO\.TXT\. Essa alteração é necessária, visto que o cliente possui situações de contas contábeis com variação cambial e o produto LALUR aceita o sinal negativo no campo\. Para esse chamado foi aberta a OS3595\.

Ocorre que a principal situação do cliente que deveria ser considerada – Indicador de Natureza da Conta Contábil por Receita ou Despesa – não foi considerada na OS\. Para que esse problema fosse contornado, foi entregue para o cliente um chamado desvinculado – CH405\-A\_2012 – que passou a considerar o Indicador de Natureza da Conta Contábil para determinar o sinal do valor informado no arquivo ESTIMADO\.TXT\. 

Embora o cliente BNDES possua uma parametrização de Conta Lalur X Conta Mastersaf “estável”, ou seja, as contas contábeis de Receita ou Despesa não são misturadas entre si nessa parametrização, assim como as contas contábeis de outros tipos – ex: Ativo e/ou Compensação verificamos em um call realizado com o Sr\. Carlos Nascimento \(Informação\) e Sr\. Juliano Felix \(Lalur\), e os mesmos nos confirmaram que a contabilidade pode ser realizada dessa forma e não estaria incorreto\. A solução conforme foi estruturada no CH405\-A\_2012 não atenderia toda a carteira de clientes\. Nessa mesma reunião foi pensada na possibilidade de que a definição se a conta é de Receita ou Despesa fosse realizada na Conta Lalur, independente das Contas Contábeis parametrizadas\.

Após outra conversa com a Eliane Barcelos \(BNDES\) em 28/09/2012, a mesma não criou impeditivos para que a solução fosse estruturada dessa maneira\. 

Com base nessas assertivas, iremos considerar o sinal negativo no arquivo ESTIMADO\.TXT por Conta Lalur e não mais por Conta Contábil\.

OS3663

\(14/09/2012\)

Criação do Módulo DIA\-AM

Criação da TACES76

OS3520

\(Mar/2013\)

GNRE Online

Criação de duas tabelas acessórias:

TACES77\-Classificação de Produtos da GNRE Online \(vide RN\-TACES77\)

TACES78\-Unidades da Federação da GNRE Online    \(vide RN\-TACES78\)

CH 18048/13

\(Jul/2013\)

Importação TACES21 \(Amparo Legal\)

Alteração da importação da TACES21 para não sobrepor os campos que não são disponibilizados no arquivo texto \(vide __RN\-TACES21__\)

OS4533

\(04/06/2014\)

Criação da TACES60

Criação da TACES60 \(vide __RN\-TACES60__\)

OS4514\-V

\(21/06/2014\)

Criação da TACES85

Criação da TACES85 \(vide __RN\-TACES85__\)

OS4547

Criação da coluna na TFIX115

Criar a coluna indicação de serie para a tela Municipal do ISS Digital\.

OS4486

\(11/09/2014\)

Criação da TACES86 e da TACES87

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>Criação da TACES86 e da TACES87 \(vide __RN\-TACES86 __e __RN\-TACES87__\)

OS4667

\(14/11/2014\)

Criação da TACES88

Criação da TACES88 \(vide __RN\-TACES88__\)

OS4735

\(27/02/2014\)

Criação da TACES89

Criação da TACES89 \(ver __RN\-TACES89__\)

OS4667

\(03/03/2015\)

Criação da TACES90

Criação da TACES90 \(vide __RN\-TACES90__\)

MFS622 \(11/08/2015\)

Criação da TACES91

Criação da TACES91 \(vide __RN\-TACES91__\)

MFS\-2926 \(13/01/2016\)

Criação da TFIX78

Criação da TFIX78 \(vide __RN\-TFIX78__\)

MFS\-4033 \(12/04/2016\)

Ajustes na estrutura da TFIX116

Ajustes na estrutura da TFIX116 \(vide __RN\-TFIX116__\)

MFS\-1079

\(07/06/2016\)

Criação das TACES92 e TACES93

Criação da TACES92 \(vide __RN\-TACES92__\) e TACES93 \(vide __RN\-TACES93__\)

MFS\-4880

\(12/07/2016\)

Criação das TACES94

Criação da TACES94 \(vide __RN\-TACES94__\)

MFS\-11100

\(28/06/2017\)

Criação das TACES95, TACES96 e TACES97

Criação das TACES95, TACES96 e TACES97 \(vide __RN\-TACES95, RN\-TACES96 e RN\-TACES97__\)

MFS13362

Lara Aline

Ajuste no tamanho do campo Código do tipo de serviço\. \(vide __RN\-TACES85__\)

MFS14409

\(05/12/2017\)

Criação de novas TACES p/o eSocial 

Criação das TACES 62, 64 e 66 \(vide __RN\-TACES62__, __RN\-TACES64__ e __RN\-TACES66__\)\. 

MFS17016

\(24/05/2017\)

Criação da TACES98

Criação da TACES 98 \(vide __RN\-TACES98__\)

MFS19230

Lara Aline

Criação da TACES75 \(ver __RN\-TACES75__\)

MFS20889

João Henrique

Criação da TACES75 \(ver __RN\-TACES06__\)

MFS26178

Isabel Gayer

Criação da TACES101 \(Vide RN\-TACES101\) Sprint 220

MFS27738

Isabel Gayer

Criação de 2 tabelas fixas \(Vide __RN\-TFIX96 e RN\-TFIX97__\) \- Sprint 223 

MFS28198

Isabel Gayer

Alteração de TFIX11 \(Vide RN\-TFIX11\) e 2 tabelas fixas \(Vide RN\-TFIX96 e RN\-TFIX97\) \- Sprint 224\. __Obs\.: A TFIX96 está sendo utilizada no processo de carga de tabelas SAFX para o produto Tax One\.__

MFS30790

Isabel Gayer

Mudanças no processo de importação de tabelas acessórias \(__RN\-TFIX/TACES__\) e criação da TFIX101 para receber o layout da tabela ICT\_COD\_GNRE \(__RN\-TFIX101__\) devido ao processo automatizado de tabelas fixas e acessórias\.

Ao final do arquivo foi incluída as regras Técnicas para Manutenção da Funcionalidade de importação automatizada de tabelas fixas e taces\.

MFS29352

Luciana Moreira

Criação da TFIX142 para a tabela já existente ICT\_PAR\_MODELO\_LIVRO

MFS32572

Liliane Assaf

Criação das TACES102 e 103 \(DESIF\) Ver __RN\-TACES102__ e __RN\-TACES103__\.

MFS\-33130

Liliane Assaf

Criação TACES104 \(DES\-IF\)

MFS\-36719

Liliane Assaf

Criação TACES105 \(DES\-IF\)

MFS43745

Andréa Rocha

Retirar a TACES99 da lista de tabelas de importação, uma vez que a tabela não é mais utilizada\. 

MFS61949

Andréa Rocha

Ajuste da documentação para ficar de acordo com o funcionamento atual da importação das TACES70 e TACES71\.  Não foi feita alteração na rotina de importação, somente atualização da regra\.

MFS\-73138

Rogério Ohashi

Atualização TACES98/TACES70 Manual Operacional \(__*Somente atualização da regra*__\)

MFS\-74425

Rogério Ohashi

Atualização Manual Operacional – Tabelas Acessórias \(__*Somente atualização da regra*__\)

MFS\-79904

Alessandra Cristina Navatta

Atualização da TACES101 \(Vide RN\-TACES101\), para atendimento do layout 2\.1 do REINF

MFS\-91937

Liliane Assaf

Criação TACES107 \(DIME\-SC\) RN\-TACES107

MFS\-91937

Liliane Assaf

Criação TACES108 \(DIME\-SC\) RN\-TACES108

MFS\-79890

Alessandra Cristina Navatta

Criação da TACES109 \(Vide RN\-TACES109\), para atendimento do layout 2\.1\.1 do REINF

MFS\-90034

Liliane Assaf

Criação TACES110 RN\-TACES110

MFS\-98748

Andréa Rocha

Alteração do tamanho dos campos extras da TACES78

MFS\-99558

Alessandra Cristina Navatta

Alteração da TACES101 

- inclusão dos campos DED, Rend\. Isento e Tributo na chave da tabela, 
- Alteração de lista de valores dos campos DED, Rend\. Isento, País Exterior PF, País Exterior PJ, Declar
- Aumento dos campos FCI, 13º e RRA, além de alteração da lista de valores válidos\.
- Inclusão das colunas Descrição Dedução e Descrição Rendimentos Isentos

MFS\-515567

Rogério Ohashi

Criação TACES111 RN\-TACES111

MFS540746

Liliane Assaf

Criação TACES112 RN\-TACES112

MFS577274

Liliane Assaf

Inclusão do campo Tabela IPM na TACES89\.\(ver __RN\-TACES89__\)

MFS591910

Graciela Soares

Criação da TACES113 \- Código de Classificação cClass da NFCOM \. \(ver RN\-TACES113\) 

MFS\-624154

Alessandra Navatta

Permitir a importação da TACES12 no processo padrão \(via ferramenta\)

MFS\-627307

Andréa Rocha

Permitir a importação da TACES14 no processo padrão \(via ferramenta\)

MFS651592

Liliane Assaf

Criação da TFIX143 \- RN\-TFIX143

MFS\-717349

Alessandra Navatta

Inclusão de colunas na TACES75

MFS772704

Liliane Assaf

Criação da TACES114

MFS\-822287

Alessandra Navatta

Criação da TACES115, TACES116 e TACES117

__Atenção\!\!\! Devido as mudanças e prioridades do projeto, as TACES serão criadas na MFS\-848570__

MFS\-848570

Alessandra Navatta

Criação da TACES118, Criação/Atualização dos Campos da TACES115, TACES116 e TACES117

MFS\- 877552

Beatriz Terada

Criação da TACES 119

MFS\-890705

Alessandra Navatta

Criação da TACES120 

MFS\-951994

Alessandra Navatta

Atendendo a nota Técnica RTC 2025\.001 v\.1\.10:

Alteração TACES115:

- Exclusão das colunas: indNFe, indNFCe, indCTe, indCteOS, indBPe, indBPeTM, indNF3e, indNFCom e indNFSe
- Inclusão das colunas: ind\_gRedBC, ind\_gCredPres\_IBS\_ZFM e ind\_gAjusCred
- Alteração da coluna: ind\_gRed para ind\_gRedAliq
- Os campos Ind\_gIBSCBS, Ind\_gIBSCBSMono, Ind\_gRedAliq, Ind\_gDif, Ind\_gTransfCred passam a ser de preenchimento obrigatório\.
- Ajustes no conteúdo

Alteração TACES116

- Ajustes no conte

Alteração TACES117:

- Inclusão das colunas \(ind\_gEstornoCred, indNFeABI, indNFe, indNFCe, indCTe, indCTeOS, indBPe, indBPeTA, indBPeTM, indNF3e, indNFSe, indNFSe Via, indNFCom, indNFAg, indNFGas, indDERE, ANEXO, Link\), 
- Renomeada as colunas, ajustado o domínio dos campos e os campos passam a ser obrigatórios: 
	- de: ind\_CredPres, Para: ind\_gCredPresOper
	- de: indMono, para: ind\_gMonoPadrao
	- de: indMonoReten, para: ind\_gMonoReten	
	- de: indMonoRet, para: ind\_gMonoRet
	- de: indMonoDif, para: ind\_gMonoDif
- Campos pRedIBS , pRedCBS e dIniVig passam ser obrigatório\.
- Ajustes no conteúdo\.

Alteração TACES118\. 

- Inclusão da coluna pAliqCredPresCBS e 
- Ajustes no conteúdo\.

MFS\-987950

Alessandra Navatta

Ajustes realizados nas tabelas listadas abaixo, com base nas informações do __Informe Técnico 2025\.002 v\.1\.30 – RTC__, contemplando:

- __TACES115__:  
Alteração da estrutura, com renomeação das colunas destacadas em amarelo, e atualização do conteúdo das informações;
- __TACES116__:  
Atualização do conteúdo das informações;
- __TACES117__:  
Alteração da estrutura, com exclusão das colunas *ind\_RedutorBC* e *Crédito para*, além da atualização do conteúdo das informações\.

Todos os ajustes realizados consideram os dados publicados no __Portal da NF\-e__, referentes à __Tabela de Código de Classificação Tributária do IBS/CBS__, publicada em __28/01/2026__, com data de alteração em __23/01/2026__\.

## ATENÇÃO: 

## \- Ao final do arquivo foi incluída as regras Técnicas para Manutenção da Funcionalidade de importação automatizada de tabelas fixas e acessórias\.

__\- Sempre que houver atualização nas tabelas Acessórias e/ou Básicas da lista realizar os seguintes procedimentos:__

__1\) Atualizar as Pastas do GIT \(\\taxone\_dw\_conteudo\\TaxOne\_tab\_Acessorias e  \\taxone\_dw\_conteudo\\TaxOne\_Tab\_Basicas\)__

__2\) Atualizar a pasta \\taxone\_dw\_conteudo\\TXT\. __

__3\) Gerar os zips \(TaxOne\_tab\_Basicas\.zip e TaxOne\_TAB\_Acessorias\.zip\)__

__4\) Abrir uma MDOC para Equipe de documentação solicitando que disponibilize os zips no Help do TAX ONE, Aba Downloads\.__

[https://webhelp\.thomsonreuters\.com\.br/Site/HELPDW/V2R010/Conteudo/Demais\_Empresas/Onesource\_Tax\_One/Help/WebHelp/inicio/downloads\.htm](https://webhelp.thomsonreuters.com.br/Site/HELPDW/V2R010/Conteudo/Demais_Empresas/Onesource_Tax_One/Help/WebHelp/inicio/downloads.htm)

MFS de exemplo:[https://dev\.azure\.com/tr\-ggo/Mastersaf%20Fiscal%20Solutions/\_workitems/edit/595131](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/595131) que abriu a MDOC [https://dev\.azure\.com/tr\-ggo/Mastersaf%20Documentation/\_workitems/edit/656914](https://dev.azure.com/tr-ggo/Mastersaf%20Documentation/_workitems/edit/656914) solicitando atualização desse zip no Webhelp do TAXONE\.

## REGRAS DE NEGÓCIO	

#### Cód\.

### DR

__RN00__

__Regras gerais__

*\(espaço reservado para regras genéricas, que não dizem respeito a campos específicos\)*

__RN\-TACES60__

__Tabela TACES60 – Tabela de Identificação de Débitos de ICMS – RJ __

A TACES60 foi criada para atendimento à Portaria SUACIEF n° 31, de 26/05/2014\.

Esta tabela conterá os códigos de identificação de débitos de ICMS do Estado do Rio de Janeiro\. Na criação todos os códigos descritos na Portaria terão data de validade inicial = 01/05/2014, data de início da vigência dos códigos\.

Campos:

__Campo__

__Tipo/Tamanho__

Código

Campo numérico de 3 posições 

Descrição

Campo alfanumérico de 120 posições

Validade Inicial

Campo de data \(DDMMAAAA\)

Validade Final

Campo de data \(DDMMAAAA\)

As informações iniciais da tabela para carga dos dados no Mastersaf estão descritas no documento de requisito da OS4533, item “3\.3\.1\-Criação da TACES60”\. Esses códigos são utilizados na geração dos registros E116 e E250 do Sped Fiscal, mas apenas para os contribuintes do RJ\.

OS4533

__RN\-TACES62__

__TACES62 \- Tabela de Códigos de Incidência Tributária das Rubricas \(eSocial\)__   *\(criação: MFS14409\)*

Chave: campos “Tipo” \+ “Código de Incidência Tributária”

__Campo__

__Tipo__

__Tamanho__

Tipo

A

01

Código de Incidência Tributária

A

02

Descrição

A

150

Os dados desta tabela acessória correspondem às opções de preenchimento dos campos *“22\-codIncCP” *e* “23\-codIncIRRF” *do evento S\-1010 \(Tabela de Rubricas\) do eSocial \(vrs 2\.4\.01\)\.

 

A princípio, a tabela contém apenas os códigos de incidência referentes à previdência social e ao IRRF, uma vez que o escopo da geração do eSocial se restringe aos trabalhadores autônomos\.

 

O campo “Tipo” define se o código é referente Contribuição Previdenciária ou ao IRRF:

1 – Para os códigos referentes à previdência social;

2 – Para os códigos referentes ao IRRF;

MFS14409

__RN\-TACES64__

__TACES64 \- Tabela de Natureza das Rubricas da Folha de Pagamento \(eSocial\)        __*\(criação: MFS14409\)*

Chave: campo “Código da Natureza da Rubrica”

__Campo__

__Tipo__

__Tamanho__

Código da Natureza da Rubrica

A

04

Nome da Natureza da Rubrica 

A

100

Os dados desta tabela correspondem a seguinte tabela do eSocial: “*Tabela 03 – Natureza das Rubricas da Folha de Pagamento*”\.

MFS14409

__RN\-TACES66__

__TACES66 \- Tabela de Categoria de Trabalhador \(eSocial\)              __*\(criação: MFS14409\)*

Chave: campo “Código da Categoria”

__Campo__

__Tipo__

__Tamanho__

Código da Categoria

A

03

Descrição 

A

250

Os dados desta tabela acessória correspondem a seguinte tabela do eSocial: “*Tabela 01 – Categorias de Trabalhadores*”\.

MFS14409

__RN\-TACES68__

__Tabela TACES68 – Tipos de Movimentação de Estoque__

A importação das tabelas fixas e acessórias foi alterada na OS3146\_A para atendimento à Resolução 3\.884/07 – MG \(registro H200\)\. 

Esta tabela conterá os códigos de movimentação do estoque tratados no registro H200\. Na criação todos os códigos descritos na Resolução 3\.884 – MG terão data de validade inicial = 01/01/2011, data prevista para início da validade desta nova obrigação\.

As informações iniciais da tabela para carga dos dados no Mastersaf estão descritas no documento de requisito da OS3146\_A, item “4\.3\.1\-Criação da Nova TACES”\.

OS3146\_A

__RN\-TACES69__

__Tabela TACES69 – Cadastro de Códigos Fiscais de Serviço__

Alterar a rotina de importação de tabelas fixas/acessórias para que a mesma passe a considera a importação da TACES69\.

As informações iniciais da tabela estão descritas no documento de requisitos no item <a id="_Toc267563253"></a>TACES NOVA \(Cadastro de Códigos Fiscais de Serviços \- DWT\_COD\_FISCAL\_SERV\)

CH88685

__RN\-TACES74__

__Tabela TACES74 \- Classes de Operação ou Prestação – ICMS – SEF II \- PE __

Esta TACES foi criada para atendimento ao arquivo magnético do SEF II – PE \(campo “COP”\)\.

Campos:

Campos

Tipo / Tamanho

Chave

Código COP

A /  4

\*

Validade Inicial

N / 8 

\*

Validade Final

N / 8

Descrição

A / 70

CFOP

__A / 4__

\*

A carga inicial desta tabela foi realizada a partir da tabela “*4\.2\.2\.1\-Tabela Classe da Operação ou Prestação – ICMS*” da planilha de layout do arquivo “eDoc\-Extrato de Documentos” \(aba TAB\_INT\) disponível no site da Sefaz\-PE\.

Para cada código COP poderão existir várias linhas na tabela, com diferentes CFOP’s\.  

OS3065\-dw

__RN\-TFIX59\-01__

__Tabela TFIX59 – Contas Lalur \(GID\) Lucro Presumido__

Deverá ser criado o campo “Indicador de Natureza” na tabela TFIX59\. Esse campo deverá ser possuir as seguintes características:

Tipo: Alfanumérico

Tamanho: 001

Obrigatoriedade: Não

Esse campo só deverá aceitar 3 \(três\) opções:

- Receita
- Despesa
- \(vazio\)

O cliente deverá informar uma das informações acima\. Vale salientar que por definição de produto, esse campo não será preenchido a princípio\.

OS3720

__RN\-TACES76__

__Tabela TACES76 – Códigos de Tributação de Produtos \(DIA\-AM\)__

Esta TACES foi criada para atendimento aos arquivos MATRIZ\-NAC e Declaração Mensal da DIA\-Amazonas\.

Campos:

Campos

Tipo / Tamanho

Chave

Código 

A /  4

\*

Descrição

A / 100

A carga inicial desta tabela foi realizada a partir do documento “Tabela de Multiplicadores\.pdf” disponível no site da Sefaz\-AM, referentes à obrigação DIA\-AMAZONAS\.__ __

OS3663

__RN\-TACES77__

__Tabela TACES77 – Classificação de Produtos da GNRE Online__

Esta TACES foi criada para atendimento à GNRE Online, novo modelo de guia de recolhimento desenvolvido no módulo ICMS pelas OS’s3520\. 

A manutenção da tabela é feita no Módulo ICMS, menu “menu Apuração à Guias de Recolhimento à Guias Recolhimento Tributos Estaduais \(GNRE Online\) à Parâmetros à Classificação de Produtos da GNRE Online”, e ela é utilizada na geração automática das guias, no menu “menu Apuração à Guias de Recolhimento à Guias Recolhimento Tributos Estaduais \(GNRE Online\) à Geração dos Dados”\.

Campos:

Campos

Tipo / Tamanho

Chave

Código do Produto

N /  003

\*

Descrição

A / 200

A carga inicial desta tabela foi realizada a partir da tabela de produtos disponível no portal da GNRE Online \([www\.gnre\.pe\.gov\.br](http://www.gnre.pe.gov.br)\) em DEZ/2012\.__ __

OS3520

__RN\-TACES78__

__Tabela TACES78 – Unidades da Federação da GNRE Online__

__\[MFS98748\] __Aumento do tamanho dos campos extras, de 2 para 3 posições

Esta TACES foi criada para atendimento à GNRE Online, novo modelo de guia de recolhimento desenvolvido no módulo ICMS pelas OS’s3520\. 

A manutenção da tabela é feita no Módulo ICMS, menu “menu Apuração à Guias de Recolhimento à Guias Recolhimento Tributos Estaduais \(GNRE Online\) à Parâmetros à Parâmetros por UF”, e ela é utilizada na geração automática das guias, no menu “menu Apuração à Guias de Recolhimento à Guias Recolhimento Tributos Estaduais \(GNRE Online\) à Geração dos Dados”\.

 

Campos:

Campo

Tipo / Tamanho

Campos Chave

__UF__

__A / 002__

__\*__

__Receita__

__A / 007__

__\*__

Detalhamento de Receita

A / 001

Código de Detalhamento da Receita

__A / 006 __

Detalhamento de Produto 

A / 001 

Documento 

A / 001

Período

A / 001

Mês / Ano

A / 001

Destinatário

A / 001

Campos Extras

A / 001

Campo Extra1

N / 003

Campo Extra2

N / 003

Campo Extra3 

N / 003

Valores

__N / 001__

A carga inicial desta tabela foi realizada a partir das regras de preenchimento das GNRE’s, disponíveis no portal da GNRE Online \([www\.gnre\.pe\.gov\.br](http://www.gnre.pe.gov.br)\) em MAR/2013\.__ __

OS3520

MFS98748

__RN\-TACES21__

__Tabela TACES21 – Amparos Legais__

__Alteração do chamado 18048/13:__

Este chamado implementou uma melhoria na importação, para *não* sobrepor a informação dos campos que *não* são disponibilizados no arquivo texto\.

Quando o registro do amparo legal já existe na base de dados, a importação faz uma comparação para verificar se houve alteração de algum campo, e se houver, faz a atualização do registro \(ou seja, sobrepõe os dados\)\. Nesta comparação, os seguintes campos __não__ serão considerados:

\-Código de Receita

\-Campo “Tributo”

\-Campo “ICMS”

\-Campo “IPI”

\-Campo “ICMS\-S”

*Obs: A TACES21 possui algumas informações que foram incluídas na tabela \(provavelmente para atender a alguma obrigação\), mas que não são disponibilizadas no arquivo texto\. \(no arquivo texto estão com zeros ou @ para todas as UF’s\)\. Isso gera problemas, pois se o cliente preenche algum destes campos na manutenção da tabela, e depois executa a rotina de importação, os campos serão todos apagados\.*

CH18048/13

__RN\-TACES85__

__Tabela TACES85 – Tipo de Serviço – eSocial\. __

A TACES85 foi criada para atendimento ao Integrador do Onesource eSocial\.

Esta tabela conterá os códigos de Tipo de Serviço do eSocial\.

Campos:

__Campo__

__Tipo / Tamanho__

__Chave__

Data de Início de Validade

N / 8

\*

Código do Tipo de Serviço

A / 9

\*

Descrição do Tipo de Serviço

A / 100 

As informações iniciais da tabela para carga dos dados no Mastersaf estão descritas no documento de requisito da OS4514\-B\.

OS4514\-B

MFS13362

__RNTFIX115__

__Tabela TFIX115 Cadastro de Validadores\.__

Criar campo na TFIX115 para identificação do validar, essa campo fará a identificação dos validadores que deverão utilizar a  parametrização da tela “Modelo Msaf x Município Prestador x Série” localizada no módulo Municipal >> Parâmetros por Município menu Parâmetros > Modelo Msaf x Município Prestador x Série\.

   

__ __

__Campo__

__Tipo / Tamanho__

__Chave__

Indicador de validador 

A / 1

OS4547

__RN\-TACES86__

__Tabela TACES86 – CFOP – Motivo de Ajuste\. __

A TACES86 foi criada para atendimento à GIA\-RS – Anexos I\.c e V\.c\.

Esta tabela conterá os códigos do Motivo de Ajuste do valor excluído para fins de cálculo do valor adicionado\.

__Campos:__

__Campo__

__Tipo / Tamanho__

__Chave__

CFOP

A / 4

\*

Código de Ajuste

A / 3

\*

Data Início

D / 8

\*

Data Fim

D / 8

As informações iniciais da tabela para carga dos dados no Mastersaf estão descritas no documento de requisito da OS4486\.

OS4486

__RN\-TACES87__

__Tabela TACES87 – Motivo de Ajuste\. __

A TACES87 foi criada para atendimento à GIA\-RS – Anexos I\.c e V\.c\.

Esta tabela conterá os códigos do Motivo de Ajuste e os indicadores de recuperação dos dados \(discriminação das entradas e saídas\)\.

__Campos:__

__Campo__

__Tipo / Tamanho__

__Chave__

Código de Ajuste

A / 3

\*

Data Início

D / 8

\*

Descrição

A / 100

Recuperar Motivo

N / 1

Data Fim

D / 8

As informações iniciais da tabela para carga dos dados no Mastersaf estão descritas no documento de requisito da OS4486\.

OS4486

__RN\-TACES88__

__Tabela TACES88 – __Código Situação Tributária ISS__\. __

A TACES88 foi criada para atendimento a obrigações de ISS\.

Esta tabela conterá os códigos da Situação Tributária ISS\.

Campos:

__	Campo	__

__Tipo / Tamanho__

__Chave__

Código da Situação Tributária ISS

N / 2

\*

Data de Início de Validade

N / 8

\*

Descrição da Situação Tributária ISS

A / 100 

As informações iniciais da tabela para carga dos dados no Mastersaf estão descritas no documento de requisito da OS4667\.

OS4667

__RN\-TACES89__

__Tabela TACES89 – Códigos dos Itens de Participação dos Municípios – Sped Fiscal__

Esta TACES foi criada para atendimento ao Sped Fiscal, registro 1400, e corresponde às tabelas dos itens para cálculo do índice de participação dos municípios, disponibilizadas por alguns estados\.

Sua manutenção é feita no próprio módulo Ferramentas\.

Campos:

  

__Campo__

__Tipo __

__Tamanho__

__Chave__

UF 

A 

2

\*

Código

A 

60

\*

Descrição 

A 

250

Tabela IPM

A

10

A carga inicial foi realizada com os códigos referentes aos estados de MG e SP, obtidos na Resolução 4\.730/2014 \(Sefaz\-MG\) e Portaria CAT 137/2014 \(Sefaz\-SP\)\.__ __

OS4735

MFS577274

__RN\-TACES90__

__Tabela TACES90 – Natureza da Subconta Correlata __

A TACES90 foi criada para possibilitar a geração de informações na ECD, registro I053, onde será associada à uma conta contábil\.

Campos:

__	Campo	__

__Tipo / Tamanho__

__Chave__

Código da Natureza da Subconta Correlata

A / 2

\*

Data de Início de Validade

N / 8

\*

Descrição do Tipo de Serviço

A / 200 

Data de Fim de Validade

N / 8

Críticas:

Código \(campo chave\) à Campo obrigatório

Data de Início de Validade \(campo chave\) à Campo obrigatório\. Deve ser uma data válida\.

As informações iniciais da tabela para carga dos dados no Mastersaf estarão disponíveis na implementação da OS4745\.

OS4745

__RN\-TACES91__

__Tabela TACES91 –  Cadastro de Benefícios de ICMS \(DUB\-RJ\)__

A TACES91 foi criada para atendimento à DUB\-RJ\.

Esta tabela conterá os códigos dos Benefícios de ICMS do RJ para fins de cálculo do Imposto não recolhido/não debitado\.

__Campos:__

__Campo__

__Tipo / Tamanho__

__Chave__

Tipo Ato Legal

A / 2

\*

Número/Ano

A / 12

\*

Data Início

D / 8

\*

Descrição do Benefício

A / 1100

Espécie do Benefício

A / 2

\*

Data Fim

D / 8

As informações iniciais da tabela para carga dos dados no Mastersaf estão descritas no documento de requisito da MFS622\.

MFS622

__RN\-TFIX78__

__Tabela RN\-TFIX78 – Critérios de Consolidação do Razão Auxiliar das Subcontas__

A TFIX78 foi criada para atendimento à ECD, para utilização na parametrização de “Critérios de Consolidação \- Razão Auxiliar das Subcontas”\. Nela estarão disponíveis os campos que irão compor o Livro Razão Auxiliar das Subcontas para que seja atribuído para cada campo qual critério será utilizado na geração do registro I555, consolidador do I550\. Como estes critérios de consolidação podem ser definidos pelo usuário, criamos a parametrização\.

__Campos:__

__Campo__

__Tipo / Tamanho__

__Chave__

Versão do Layout ECD

A / 3

\*

Código do Item

A / 3

\*

Descrição

A / 200

Formato

A / 3

As informações iniciais da tabela para carga dos dados no Mastersaf estão descritas no documento de requisito da MFS2926\.

MFS\-2926

__RN\-TFIX116__

__Tabela TFIX116 – Cadastro de Operações das Obrigações__

Ajustar a estrutura da TFIX116, para que contemple novo campo no final da estrutura\. Será um campo utilizado para identificar o Tipo de Operação ao qual o Código ANP se refere\. Não será um campo obrigatório e deverá permitir os seguintes conteúdos: “E – Entrada”, “S – Saída” ou “O – Outros”\.

__ __

__Campo__

__Tipo / Tamanho__

__Chave__

Indicador de validador 

A / 1

O conteúdo atualizado da tabela estará disponível junto ao Requisito da MFS\-4033\.

MFS\-4033

__RN\-TACES92__

__Tabela TACES92 – Tipo de Cliente __

A TACES92 foi criada para possibilitar o cadastramento do Tipo de Cliente, conforme solicitado pelo Convênio ICMS 60/2015\.

Campos:

__	Campo	__

__Tipo / Tamanho__

__Chave__

Modelo do Documento

A / 2

\*

Código do Tipo de Cliente

A / 2

\*

Descrição

A / 200 

Críticas:

Modelo do Documento \(campo chave\) à Campo obrigatório e seu conteúdo deve constar da Tabela de Modelo de Documento Fiscal \(SAFX2024\)\.

Código do Tipo do Cliente \(campo chave\) à Campo obrigatório\.

Por ser necessária a validação do código de Modelo do Documento com os códigos cadastrados na SAFX2024, no momento da importação desta TACES será exibida a tela de “Parâmetros para Importação” para que o usuário informe um período para que o sistema saiba qual Grupo considerar para realização da validação\. A partir da indicação do período, consideraremos os registros da SAFX2024 associada ao Grupo vigente no período para o estabelecimento selecionado\.

As informações iniciais da tabela para carga dos dados no Mastersaf estarão disponíveis na implementação da MFS\-1079\.

MFS\-1079

__RN\-TACES93__

__Tabela TACES93 – Subclasse de Consumo __

A TACES93 foi criada para possibilitar o cadastramento da Subclasse de Consumo, conforme solicitado pelo Convênio ICMS 60/2015\.

Campos:

__	Campo	__

__Tipo / Tamanho__

__Chave__

Modelo do Documento

A / 2

\*

Código da Subclasse de Consumo

A / 2

\*

Descrição

A / 200 

Críticas:

Modelo do Documento \(campo chave\) à Campo obrigatório e seu conteúdo deve constar da Tabela de Modelo de Documento Fiscal \(SAFX2024\)\.

Código da Subclasse de Consumo \(campo chave\) à Campo obrigatório\.

Por ser necessária a validação do código de Modelo do Documento com os códigos cadastrados na SAFX2024, no momento da importação desta TACES será exibida a tela de “Parâmetros para Importação” para que o usuário informe um período para que o sistema saiba qual Grupo considerar para realização da validação\. A partir da indicação do período, consideraremos os registros da SAFX2024 associada ao Grupo vigente no período para o estabelecimento selecionado\.

As informações iniciais da tabela para carga dos dados no Mastersaf estarão disponíveis na implementação da MFS\-1079\.

MFS\-1079

__RN\-TACES94__

__Tabela TACES94 – Código Especificador da Substituição Tributária __

A tabela TACES94 foi criada com a finalidade de realizar o cadastramento do Código Especificador da Substituição Tributária, conforme solicitação do Convênio ICMS 92/2015\.

Campos:

__	Campo	__

__Tipo / Tamanho__

__Chave__

Data de Atualização

D/8

\*

Código Especificador da Substituição Tributária \- CEST

A/7

\*

Descrição

A/800

Críticas:

Data de Atualização \(Campo chave\) à Campo obrigatório\.

Código Especificador da Substituição Tributária \- CEST \(campo chave\) à Campo obrigatório\.

As informações iniciais da tabela para carga dos dados no Mastersaf estarão disponíveis na implementação da MFS\-4880\.

MFS4880

__RN\-TACES95__

__Tabela TACES95 – Código de Características Físico\-Químicas__

A tabela TACES95 foi criada com a finalidade de realizar o cadastramento do Código de Característica Físico\-Química, conforme tabela de código T004 \(Códigos de Características Físico\-Químicas\) do i\-SIMP\.

Campos:

__	Campo	__

__Tipo / Tamanho__

__Chave__

Código

A/3

\*

Data Início Validade

D/8

\*

Data Fim Validade

D/8

Característica

A/100

Unidade de Medida

A/15

Críticas:

Código \(campo chave\) à Campo obrigatório\.

Data Início Validade \(Campo chave\) à Campo obrigatório\.

As informações iniciais da tabela para carga dos dados no Mastersaf estarão disponíveis na implementação da MFS\-11100\.

MFS11100

__RN\-TACES96__

__Tabela TACES96 – Código de Métodos de Aferição__

A tabela TACES96 foi criada com a finalidade de realizar o cadastramento do Código do Método de Aferição, conforme tabela de código T009 \(Códigos de Métodos de Aferição\) do i\-SIMP\.

Campos:

__	Campo	__

__Tipo / Tamanho__

__Chave__

Código

A/3

\*

Data Início Validade

D/8

\*

Data Fim Validade

D/8

Método

A/50

Críticas:

Código \(campo chave\) à Campo obrigatório\.

Data Início Validade \(Campo chave\) à Campo obrigatório\.

As informações iniciais da tabela para carga dos dados no Mastersaf estarão disponíveis na implementação da MFS\-11100\.

MFS11100

__RN\-TACES97__

__Tabela TACES97 – Código de Vasilhames__

A tabela TACES97 foi criada com a finalidade de realizar o cadastramento do Código de Vasilhames, conforme tabela de código T006 \(Códigos de Vasilhames de GLP\) do i\-SIMP\.

Campos:

__	Campo	__

__Tipo / Tamanho__

__Chave__

Código

A/3

\*

Data Início Validade

D/8

\*

Data Fim Validade

D/8

Vasilhame

A/50

Críticas:

Código \(campo chave\) à Campo obrigatório\.

Data Início Validade \(Campo chave\) à Campo obrigatório\.

As informações iniciais da tabela para carga dos dados no Mastersaf estarão disponíveis na implementação da MFS\-11100\.

MFS11100

__RN\-TACES98__

__Tabela TACES98 – Tabela de Códigos de Instalação ANP T008__

A tabela TACES98 foi criada com a finalidade de importar e manutenir os códigos de instalação da ANP tabela T008 no mastersaf DW\.

Campos:

__	Campo	__

__Tipo / Tamanho__

__Chave__

Código de Instalação

N/007

\*

Validade Inicial

D/008

\*

Descrição

A/200

Validade Final

D/008

Críticas:

Código de Instalação \(campo chave\)\.

Validade Inicial \(Campo chave\) 

As informações iniciais da tabela para carga dos dados no Mastersaf estarão disponíveis na implementação da MFS\-17016\. Seguiremos a criação da tabela TACES conforme definição da tabela TFX86\. O objetivo principal é possibilitar que o usuário possa manutenir no sistema por conta própria os códigos de Instalação\.

MFS17016

__RN\-TACES75__

__Tabela TACES75 – Tabela de  Códigos de Atividades, Produtos e Serviços Sujeitos à Contribuição Previdenciária sobre a Receita Bruta__

A tabela TACES75 foi criada com a finalidade de realizar o cadastramento do Códigos de Atividades, Produtos e Serviços Sujeitos à Contribuição Previdenciária sobre a Receita Bruta, conforme tabela 5\.1\.1 – Contribuição Previdenciária sobre a Receita Bruta\. 

Campos:

__	Campo	__

__Tipo / Tamanho__

__Chave__

Identificação de Atividade

N/5

\*

Código de Atividade

A/8

\*

Data Inicio Validade

D/8

\*

Descrição Atividade

A/400

Campo NBM  

A/10

Alíquota  

N/12

Data Fim Validade

D/8

Indicativo Atividade

A/1

CNAE

A/10

Início Escrituração

D/8

Código Receita

A/6

Críticas:

Identificação de Atividade \(campo chave\) à Campo obrigatório\.

Código de Atividade \(Campo chave\) à Campo obrigatório\.

Data Inicio Validade \(Campo chave\) à Campo obrigatório\.

MFS19230

MFS\-717349

__RN\-TACES06__

__Tabela TACES06 – Tabela Municípios IBGE__

A tabela TACES06 foi criada com a finalidade de realizar o cadastramento das informações dos Municípios do Brasil conforme a tabela do IBGE\. 

Inclusão de novo campo na tabela:

__	Campo	__

__Tipo / Tamanho__

__Obrigatório__

__Chave__

Descrição de Município por Código IBGE

A/50

Não

Não

__Observação:__ A inclusão do campo se faz necessária para atender o convênio 115 \(ICMS\) e preencher com o a descrição na geração conforme IBGE\. Nossa tabela possui um preenchimento diferente atualmente para as descrições dos municípios\.

\*O nome técnico do campo  na tabela será definido pelo desenvolvimento\.

MFS\-20889

__RN\-TACES101__

__Tabela TACES101 \- Tabela de Natureza de Rendimentos \(EFD\-REINF\)__

A tabela TACES101 foi criada com a finalidade de ser utilizada no módulo EFD\-REINF, para recepcionar as informações da tabela 01 \- Natureza de Rendimentos \- Leiaute 2\.1 da EFD\-REINF utilizada na geração dos eventos R\-4010 – Pagamentos/créditos a beneficiário pessoa física, linha 37,64; R\-4020 \- Pagamentos/créditos a beneficiário pessoa jurídica, linha 30,59 e R\-4080 – Retenção no Recebimento, linha 20\.

A tabela TACES101 – Tabela de Natureza de Rendimentos \(EFD\-REINF\) deverá ser incluída na tela de importação da TACES/TFIX do módulo Ferramentas \(menu: Tabelas Internas >> Importar >> Tabelas Acessórias\)\.

__Campos:__

__Campo__

__Sugestão__

__Chave__

__Tipo__

__Tamanho__

Grupo

COD\_GRUPO\_NAT\_REND

\(\*\)

A

2

Código da Natureza do Rendimento

COD\_NAT\_REND

\(\*\)

A

9

Natureza de Rendimento

DESCRICAO

A

600

FCI

IND\_FCI

A

3

13º 

IND\_DEC\_TERC

A

3

RRA

IND\_RRA

A

3

DED

TIPO\_DEDUCAO

\(\*\)

A

50

Descrição Dedução

DESC\_ TIPO\_DEDUCAO

A

600

Rend\. Isento

TIPO\_ISENCAO

\(\*\)

A

50

Descrição Rendimentos Isentos

DESC\_ TIPO\_ISENCAO

A

600

País Exterior PF

TIPO\_PAIS\_EXT\_PF

A

50

País Exterior PJ

TIPO\_PAIS\_EXT\_PJ

A

50

Declar

TIPO\_NAT\_DECLAR

A

50

TRIBUTO

TIPO\_TRIBUTO

\(\*\)

A

50

A carga inicial desta tabela foi realizada a partir do “Leiautes da EFD\-Reinf v2\.1 \- Anexo I \- Tabelas” do site da Receita Federal do Brasil\.

Críticas:

Grupo \(campo chave\) à Campo obrigatório\. 

Código da Natureza do Rendimento \(campo chave\) à Campo obrigatório\. 

__ALTERAÇÃO MFS\-99558__\] DED \(campo chave\) àCampo não obrigatório\. 

__\[ALTERAÇÃO MFS\-99558__\] Rend\. isento: \(campo chave\) àCampo não obrigatório\. 

__\[ALTERAÇÃO MFS\-99558\] __Tributo: \(campo chave\) àCampo não obrigatório\. 

Listas de Valores Válidos, estão disponíveis nos arquivos liberados das respectivas demandas\.

As informações iniciais da tabela para carga dos dados no Mastersaf estarão disponíveis na implementação da MFS\-26178\. As atualizações da estrutura da tabela, estão disponíveis na MFS\-79904 e na MFS\-99558

MFS26178

MFS\-79904

MFS\-99558

__RN\-TACES102__

__Tabela TACES102 \- Tabela de Codigos de Tributacao DESIF \- Anexo 6__

A tabela TACES102 foi criada com a finalidade de carregar a lista estabelecida no Anexo 6 – Tabela de Códigos de Tributação da DES\-IF\.  

__Base Legal:__

Secretaria Municipal de Fazenda da Prefeitura de São Paulo:

Instrução Normativa SF/SUREM Nº 17, DE 26 DE SETEMBRO DE 2017

Portaria SF/SUREM nº 57, de 4 de outubro de 2017

A DES\-IF é um validador municipal para financeiras, que hoje atende ao município de São Paulo\. No Mastersaf atendemos a tal obrigação através do módulo São Paulo\-Financeiras\.

A primeira carga da TACES 102 está sendo feita com a versão do anexo ¨6 aqui anexada \(“anexo\_6\_\-\_tabela\_de\_codigos\_de\_tributacao\_da\_des\-if\_1507756539\.pdf”\), através da MFS\-32572 \(março/2020\)\.  A ideia é disponibilizarmos uma tela de manutenção para que possíveis modificações possam ser realizadas pelos usuários\.

__Campos:__

__Campo__

__Sugestão__

__Chave__

__Tipo__

__Tamanho__

Código de Tributação DESIF

COD\_TRIB\_DESIF

\(\*\)

A

15

Descrição

DSC\_TRIB\_DESIF

A

300

Código do Serviço da Lei 116

COD\_SERV\_L116

A

5

Críticas:

Código de Tributação DESIF \(campo chave\) à Campo obrigatório\.

![](data:image/x-emf;base64,AQAAAGwAAAAAAAAAAQAAAH0AAABLAAAAAAAAAAAAAADeCAAAxQUAACBFTUYAAAEAgB8AABEAAAACAAAAAAAAAAAAAAAAAAAAgAcAADgEAABYAQAAwgAAAAAAAAAAAAAAAAAAAMA/BQDQ9QIAGAAAAAwAAAAAAAAAGQAAAAwAAAD///8AcgAAAKAZAAArAAAAAQAAAFIAAAAoAAAAKwAAAAEAAAAoAAAAKAAAAACA/wEAAAAAAAAAAAAAgD8AAAAAAAAAAAAAgD8AAAAAAAAAAP///wAAAAAAbAAAADQAAACgAAAAABkAACgAAAAoAAAAKAAAACgAAAAoAAAAAQAgAAMAAAAAGQAAAAAAAAAAAAAAAAAAAAAAAAAA/wAA/wAA/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAw0NAwQgIAIEIiICBCIiAgQiIgIEIiICBCIiAgQiIgIEIiICBCIiAgQiIgIEIiICBCIiAgQiIgIEIiICBCIiAgQiIgIEIiICBCIiAgQiIgIEIiICBCIiAgQiIgIEIiICBCIiAgQiIgQFHBwAAAcHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAhISFh2PkRol8fMWIf//FiH//xYh//8WIf//FiH//xYh//8WIf//FiH//xYh//8WIf//FiH//xYh//8WIf//FiH//xYh//8WIf//FiH//xYh//8WIf//FiH//xYh//8WIf//FiH//xYh//8fKN/fDBFvbwABDAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg93dxYh/f0/Sf3/a3L7/4yR+v+Nkvr/jZL6/42S+v+Nkvr/jZL6/42S+v+Nkvr/jZL6/42S+v+Nkvr/jZL6/42S+v+Nkvr/jZL6/42S+v+Nkvr/jZL6/42S+v+Nkvr/jZL6/4mP+v9sc/v/MTv+/xci+/sJDnJyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQe8vJHT/3/xMf3/+rr9v/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/09PX/6+v1/6er+f8mMP7/FB7y8gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWIf//eH77//Hx9f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/Z2vb/Ljj+/xYh//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFiH//36E+v/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/29vb/+/v7//19fX/9fX1/9/f3//a2tr/4ODg/+7u7v/v7+//3d3d//T09P/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1/zQ9/v8WIf//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYh//9+hPr/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1/zMzM//IyMj/9fX1//X19f9PT0//S0tL/2pqav+np6f/u7u7/z09Pf/u7u7/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f80Pf7/FiH//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWIf//foT6//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f8zMzP/d3d3/7CwsP/o6Oj/R0dH/5ubm//Dw8P/aGho/5SUlP88PDz/0tLS/93d3f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/ND3+/xYh//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFiH//36E+v/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/MzMz/4aGhv9nZ2f/r6+v/0RERP+hoaH/5+fn/2xsbP+CgoL/PDw8/0RERP9eXl7/6enp//X19f/19fX/9fX1//X19f/19fX/9fX1/zQ9/v8WIf//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYh//9+hPr/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1/zMzM//Hx8f/lpaW/4qKiv8+Pj7/oaGh/+Pj4/9ra2v/hYWF/zw8PP/t7e3/8/Pz//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f80Pf7/FiH//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWIf//foT6//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f80NDT/n5+f/21tbf+lpaX/RERE/4aGhv+dnZ3/a2tr/6Kiov88PDz/p6en/7S0tP/q6ur/9fX1//X19f/19fX/9fX1//X19f/19fX/ND3+/xYh//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFiH//36E+v/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/dnZ2/2tra/+VlZX/4eHh/4ODg/9paWn/g4OD/83Nzf/U1NT/dXV1/2hoaP94eHj/3Nzc//X19f/19fX/9fX1//X19f/19fX/9fX1/zQ9/v8WIf//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYh//9+hPr/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f80Pf7/FiH//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWIf//foT6//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/ND3+/xYh//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFiH//36E+v/19fX/9fX1//X19f/19fX/9PT1//Dw9f/u7vX/7/D1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1/zQ9/v8WIf//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYh//9+hPr/9fX1//X19f/19fX/9fX1/93e9v9TWvz/JS/+/0ZP/f/W2Pf/9PT1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f80Pf7/FiH//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWIf//foT6//X19f/19fX/9fX1//X19f/Dxff/RU39/5KX+f9YX/z/TVX8/9fZ9v/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/ND3+/xYh//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFiH//36E+v/19fX/9fX1//X19f/19fX/3N72/2Fp/P98gvv/wcT4/1hg/P96gPv/6Oj2//X19f/19fX/9fX1//X19f/19fX/9fX1/9/g9v+/wvf/y833/+7v9f/19fX/9fX1//X19f/19fX/9fX1/zQ9/v8WIf//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYh//9+hPr/9fX1//X19f/19fX/9fX1//T09f/f4Pb/mJ35/0tT/f9GTv3/LDX+/7S3+P/z9PX/9fX1//X19f/19fX/5eX2/3l++/82P/7/KjT+/y44/v+Kj/r/7Oz1//X19f/19fX/9fX1//X19f80Pf7/FiH//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWIf//foT6//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/pKj5/z5H/f8yPP7/YWj7/5uf+f/Mzvf/ztD3/0xU/P9MVP3/yMr3/+jo9v9mbPv/PUb+/9/g9v/19fX/9fX1//X19f/19fX/ND3+/xYh//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFiH//36E+v/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f+mqvj/JjD+/ygy/v8sNv7/ICr//yAq//9HUP3/zM73/9vc9v+fo/n/Ljj+/2du/P/m5/b/9fX1//X19f/19fX/9fX1/zQ9/v8WIf//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYh//9+hPr/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/2tv2/0pS/f9+hPr/yMr3/1Ze/P9+g/r/rLD4/4WK+v9sc/v/WmL8/3R7+//O0Pf/9PT1//X19f/19fX/9fX1//X19f80Pf7/FiH//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWIf//foT6//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f+Bh/r/Ljj+/5GW+v9wd/v/4OH2//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/ND3+/xYh//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFiH//36E+v/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/ztD3/yw2/v8fKf//3N32//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1/zQ9/v8WIf//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYh//9+hPr/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1/9/g9v8zPP7/FiH//8TH+P/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f80Pf7/FiH//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWIf//foT6//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f+Vmvn/jZL6/x4o//+Hjfr/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/ND3+/xYh//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFiH//36E+v/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/v7/X/YWj7/9HT9/8/SP3/W2P8//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1/zQ9/v8WIf//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYh//9+hPr/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/3t/2/2du/P/d3vb/S1T9/ztE/f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f80Pf7/FiH//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWIf//foT6//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1/+bm9v9dZPz/vL74/yMt/v9YX/z/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/l5fb/MTr+/xYh//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFiH//36E+v/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/lpv5/ygy/v8dKP//vb/3//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/pKj5/yQv/v8VIP39AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYh//9+hPr/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/4+T2/1Ze/P8YIv//DhawsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWIf//foT6//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/6+v2/3qA+/8dKPr8ERrR0QIEJycAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFiH//36E+v/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1/5ab+f8iLPv7DhaqqgQGMzMAAAEBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYh//9+hPr/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1/4SK+v8gK/v9DRSnpwIEHh4AAAEBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVIP7+aXD7/+fo9v/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/8vP1/3l/+v8ZI/7/ERnKygECGRkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEhvb2zI8/v+4u/j/8PD1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/z8/X/4uLz/ZSZ9/4iLP39EhvY2AIDIyMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkOc3MUH/f3Rk79/5Wa+f+xtfj/srX4/7K1+P+ytfj/srX4/7K1+P+ytfj/srX4/7K1+P+ytfj/srX4/7K1+P+ytfj/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)

MFS32572

__RN\-TACES103__

__Tabela TACES103 \- Tabela de Codigos de Tributacao do Municipio DESIF \- Anexo 7__

A tabela TACES103 foi criada com a finalidade de carregar a lista estabelecida no Anexo 7 – Tabela de Códigos de Tributação do Município DES\-IF\.  

__Base Legal:__

Secretaria Municipal de Fazenda da Prefeitura de São Paulo:

Instrução Normativa SF/SUREM Nº 17, DE 26 DE SETEMBRO DE 2017

Portaria SF/SUREM nº 57, de 4 de outubro de 2017

A DES\-IF é um validador municipal para financeiras, que hoje atende ao município de São Paulo\. No Mastersaf atendemos a tal obrigação através do módulo São Paulo\-Financeiras\.

A primeira carga da TACES 103 está sendo feita com a versão do anexo ¨7 aqui anexada \(“anexo\_7\_\-\_tabela\_de\_codigos\_de\_tributacao\_do\_municipio\_1507756653”\), através da MFS\-32572 \(março/2020\)\. A ideia é disponibilizarmos uma tela de manutenção para que possíveis modificações possam ser realizadas pelos usuários\.

__Campos:__

__Campo__

__Sugestão__

__Chave__

__Tipo__

__Tamanho__

Código do Município IBGE

COD\_MUNICIPIO\_IBGE

\(\*\)

A

7

Código de Tributação do Município

COD\_TRIB\_MUNIC

\(\*\)

A

7

Código de Tributação DESIF

COD\_TRIB\_DESIF

A

15

Alíquota

ALIQ

N

5 \(3int, 2dec\)

Inicio de Vigência

VALID\_INI

\(\*\)

D

Fim de Vigência

VALID\_FIM

D

Críticas:

Código do Município IBGE \(campo chave\) à Campo obrigatório\.

Código de Tributação do Município \(campo chave\) à Campo obrigatório\.

Código de Tributação DESIF  à Campo obrigatório\.

Alíquota  à Campo obrigatório\. Numérico válido\.

Início de Vigência \(campo chave\) à Campo obrigatório\. Data válida\.

Fim de Vigência à Se preenchido deve ser uma data válida\.

__![](data:image/x-emf;base64,AQAAAGwAAAAAAAAAAQAAAH0AAABLAAAAAAAAAAAAAADeCAAAxQUAACBFTUYAAAEAmB8AABEAAAACAAAAAAAAAAAAAAAAAAAAgAcAADgEAABYAQAAwgAAAAAAAAAAAAAAAAAAAMA/BQDQ9QIAGAAAAAwAAAAAAAAAGQAAAAwAAAD///8AcgAAAKAZAAArAAAAAQAAAFIAAAAoAAAAKwAAAAEAAAAoAAAAKAAAAACA/wEAAAAAAAAAAAAAgD8AAAAAAAAAAAAAgD8AAAAAAAAAAP///wAAAAAAbAAAADQAAACgAAAAABkAACgAAAAoAAAAKAAAACgAAAAoAAAAAQAgAAMAAAAAGQAAAAAAAAAAAAAAAAAAAAAAAAAA/wAA/wAA/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAw0NAwQgIAIEIiICBCIiAgQiIgIEIiICBCIiAgQiIgIEIiICBCIiAgQiIgIEIiICBCIiAgQiIgIEIiICBCIiAgQiIgIEIiICBCIiAgQiIgIEIiICBCIiAgQiIgIEIiICBCIiAgQiIgQFHBwAAAcHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAhISFh2PkRol8fMWIf//FiH//xYh//8WIf//FiH//xYh//8WIf//FiH//xYh//8WIf//FiH//xYh//8WIf//FiH//xYh//8WIf//FiH//xYh//8WIf//FiH//xYh//8WIf//FiH//xYh//8fKN/fDBFvbwABDAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg93dxYh/f0/Sf3/a3L7/4yR+v+Nkvr/jZL6/42S+v+Nkvr/jZL6/42S+v+Nkvr/jZL6/42S+v+Nkvr/jZL6/42S+v+Nkvr/jZL6/42S+v+Nkvr/jZL6/42S+v+Nkvr/jZL6/4mP+v9sc/v/MTv+/xci+/sJDnJyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQe8vJHT/3/xMf3/+rr9v/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/09PX/6+v1/6er+f8mMP7/FB7y8gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWIf//eH77//Hx9f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/Z2vb/Ljj+/xYh//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFiH//36E+v/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/29vb/+/v7//19fX/9fX1/9/f3//a2tr/4ODg/+7u7v/v7+//3d3d//T09P/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1/zQ9/v8WIf//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYh//9+hPr/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1/zMzM//IyMj/9fX1//X19f9PT0//S0tL/2pqav+np6f/u7u7/z09Pf/u7u7/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f80Pf7/FiH//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWIf//foT6//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f8zMzP/d3d3/7CwsP/o6Oj/R0dH/5ubm//Dw8P/aGho/5SUlP88PDz/0tLS/93d3f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/ND3+/xYh//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFiH//36E+v/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/MzMz/4aGhv9nZ2f/r6+v/0RERP+hoaH/5+fn/2xsbP+CgoL/PDw8/0RERP9eXl7/6enp//X19f/19fX/9fX1//X19f/19fX/9fX1/zQ9/v8WIf//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYh//9+hPr/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1/zMzM//Hx8f/lpaW/4qKiv8+Pj7/oaGh/+Pj4/9ra2v/hYWF/zw8PP/t7e3/8/Pz//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f80Pf7/FiH//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWIf//foT6//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f80NDT/n5+f/21tbf+lpaX/RERE/4aGhv+dnZ3/a2tr/6Kiov88PDz/p6en/7S0tP/q6ur/9fX1//X19f/19fX/9fX1//X19f/19fX/ND3+/xYh//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFiH//36E+v/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/dnZ2/2tra/+VlZX/4eHh/4ODg/9paWn/g4OD/83Nzf/U1NT/dXV1/2hoaP94eHj/3Nzc//X19f/19fX/9fX1//X19f/19fX/9fX1/zQ9/v8WIf//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYh//9+hPr/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f80Pf7/FiH//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWIf//foT6//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/ND3+/xYh//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFiH//36E+v/19fX/9fX1//X19f/19fX/9PT1//Dw9f/u7vX/7/D1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1/zQ9/v8WIf//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYh//9+hPr/9fX1//X19f/19fX/9fX1/93e9v9TWvz/JS/+/0ZP/f/W2Pf/9PT1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f80Pf7/FiH//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWIf//foT6//X19f/19fX/9fX1//X19f/Dxff/RU39/5KX+f9YX/z/TVX8/9fZ9v/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/ND3+/xYh//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFiH//36E+v/19fX/9fX1//X19f/19fX/3N72/2Fp/P98gvv/wcT4/1hg/P96gPv/6Oj2//X19f/19fX/9fX1//X19f/19fX/9fX1/9/g9v+/wvf/y833/+7v9f/19fX/9fX1//X19f/19fX/9fX1/zQ9/v8WIf//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYh//9+hPr/9fX1//X19f/19fX/9fX1//T09f/f4Pb/mJ35/0tT/f9GTv3/LDX+/7S3+P/z9PX/9fX1//X19f/19fX/5eX2/3l++/82P/7/KjT+/y44/v+Kj/r/7Oz1//X19f/19fX/9fX1//X19f80Pf7/FiH//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWIf//foT6//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/pKj5/z5H/f8yPP7/YWj7/5uf+f/Mzvf/ztD3/0xU/P9MVP3/yMr3/+jo9v9mbPv/PUb+/9/g9v/19fX/9fX1//X19f/19fX/ND3+/xYh//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFiH//36E+v/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f+mqvj/JjD+/ygy/v8sNv7/ICr//yAq//9HUP3/zM73/9vc9v+fo/n/Ljj+/2du/P/m5/b/9fX1//X19f/19fX/9fX1/zQ9/v8WIf//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYh//9+hPr/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/2tv2/0pS/f9+hPr/yMr3/1Ze/P9+g/r/rLD4/4WK+v9sc/v/WmL8/3R7+//O0Pf/9PT1//X19f/19fX/9fX1//X19f80Pf7/FiH//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWIf//foT6//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f+Bh/r/Ljj+/5GW+v9wd/v/4OH2//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/ND3+/xYh//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFiH//36E+v/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/ztD3/yw2/v8fKf//3N32//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1/zQ9/v8WIf//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYh//9+hPr/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1/9/g9v8zPP7/FiH//8TH+P/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f80Pf7/FiH//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWIf//foT6//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f+Vmvn/jZL6/x4o//+Hjfr/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/ND3+/xYh//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFiH//36E+v/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/v7/X/YWj7/9HT9/8/SP3/W2P8//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1/zQ9/v8WIf//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYh//9+hPr/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/3t/2/2du/P/d3vb/S1T9/ztE/f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f80Pf7/FiH//wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWIf//foT6//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1/+bm9v9dZPz/vL74/yMt/v9YX/z/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/l5fb/MTr+/xYh//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFiH//36E+v/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/lpv5/ygy/v8dKP//vb/3//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/pKj5/yQv/v8VIP39AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYh//9+hPr/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/4+T2/1Ze/P8YIv//DhawsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWIf//foT6//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/6+v2/3qA+/8dKPr8ERrR0QIEJycAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFiH//36E+v/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1/5ab+f8iLPv7DhaqqgQGMzMAAAEBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYh//9+hPr/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1/4SK+v8gK/v9DRSnpwIEHh4AAAEBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVIP7+aXD7/+fo9v/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/8vP1/3l/+v8ZI/7/ERnKygECGRkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEhvb2zI8/v+4u/j/8PD1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/19fX/9fX1//X19f/z8/X/4uLz/ZSZ9/4iLP39EhvY2AIDIyMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkOc3MUH/f3Rk79/5Wa+f+xtfj/srX4/7K1+P+ytfj/srX4/7K1+P+ytfj/srX4/7K1+P+ytfj/srX4/7K1+P+ytfj/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)__

MFS32572

__RN\-TACES104__

__Tabela TACES104 \- Tabela de Tarifas Bancárias DESIF \- Anexo 9__

A tabela TACES104 foi criada com a finalidade de carregar a lista estabelecida no Anexo 9 – Tabela de Tarifas Bancárias da DES\-IF\.  

__Base Legal:__

Secretaria Municipal de Fazenda da Prefeitura de São Paulo:

Instrução Normativa SF/SUREM Nº 17, DE 26 DE SETEMBRO DE 2017

Portaria SF/SUREM nº 57, de 4 de outubro de 2017

A DES\-IF é um validador municipal para financeiras, que hoje atende ao município de São Paulo\. No Mastersaf atendemos a tal obrigação através do módulo São Paulo\-Financeiras\.

A primeira carga da TACES 104 está sendo feita com a versão do anexo 9 aqui anexada\.

__Campos:__

__Campo__

__Sugestão__

__Chave__

__Tipo__

__Tamanho__

Código Tarifa Bancária

COD\_TARIFA\_DESIF

\(\*\)

A

4

Grupo da Tarifa

GRUPO\_TARIFA\_DESIF

A

100

Descrição da Tarifa

DSC\_TARIFA\_DESIF

A

200

Periodicidade

DSC\_PERIODICIDADE

A

50

![](data:image/x-emf;base64,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EQDe/xEA3v8QALb/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABEAwP8TAO3/EwDs/2FV8v//////QTPu/xIA6f8SAOn/EgDo/2FV8P//////QTPr/xIA5f9xZu///////1FE6v8SAOP/0Mz5/7Cq9f8SAOH/EgDg/xIA4P8RAN//EQDe/xAAtv8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEQDA/xMA7f8TAO3/YlXy/////////////////4F38/8SAOn/YVXw//////9BM+z/EgDm/0Ez6v//////YVXt/xIA4//QzPn////////////QzPn/EgDg/xIA4P8RAN//EAC2/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARAMH/EwDu/xMA7f9iVfP//////0Ez7/9hVfL//////1FE7/9hVfD//////0Ez7f8SAOf/cWbw//////9RROz/EgDk/9DM+f+wqvb/EgDi/xIA4v8SAOH/EgDg/xIA4P8QALf/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABEAwf8TAO//EwDu/2JV8///////QjPw/2FV8v//////YVXx/2FV8P//////QTPt/yIR6v/QzPr/3938/xIA5f8SAOX/0Mz6/7Cq9v8SAOP/EgDi/xIA4v8SAOH/EgDg/xAAt/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEQDB/xMA7/8TAO//YlX0/////////////////8C7+v8SAOv/YVXx/////////////////8C7+f9BM+z/EgDm/xIA5f/QzPr////////////v7v3/EgDi/xIA4v8SAOH/EAC3/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARAML/EwDw/xMA7/8TAO//EwDu/xMA7f8TAO3/EwDs/xIA6/8SAOv/EgDq/xIA6f8SAOn/EgDo/xIA6P8SAOf/EgDm/xIA5f8SAOX/EgDk/xIA4/8SAOP/EgDi/xIA4v8QALj/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABEAwv8TAPH/EwDw/xMA7/8TAO//EwDu/xMA7f8TAO3/EwDs/xIA6/8SAOv/EgDq/xIA6f8SAOn/EgDo/xIA6P8SAOf/EgDm/xIA5f8SAOX/EgDk/xIA4/8SAOP/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)

MFS\-33130

__RN\-TACES107__

__Tabela TACES107 \- Tabela de Cadastro dos Códigos de Benefícios TTD \(DIME\-SC\)__

A tabela TACES107 foi criada com a finalidade de carregar a lista Códigos de Benefícios \(Número do TTD\) disponíveis nos Anexos I, II, IV, V, VII, IX da Portaria SEF N° 143/2022 de Santa Catarina\.  

__Base Legal:__

PORTARIA SEF N° 143/2022 de Santa Catarina\.  

__Campos:__

__Campo__

__Regra de Preenchimento__

Código Benefício \(Nr do TTD\)

Preencher com o campo “Nº do TTD” dos Anexos I, II, IV, V, VII, IX da Portaria SEF N° 143/2022

Descrição Benefício

Preencher com o campo “Dispositivo Legal” dos Anexos I, II, IV, V, VII, IX da Portaria SEF N° 143/2022

Tabela: table EST\_SC\_DIME\_BENEF

MFS\-91937

__RN\-TACES108__

__Tabela TACES108 \- Tabela de Cadastro dos Códigos Tipo 3 – Crédito Presumido \(DCIP\) \(DIME\-SC\)__

A tabela TACES108 foi criada com a finalidade de carregar a lista dos subtipos DCIP do “Tipo 3 \- Crédito Presumido” disponíveis no Manual “TABELAS DCIP PREVISTA NO ITEM 3\.4\.2\.1 DO ANEXO I DA PORTARIA SEF Nº 153/12” de Santa Catarina\.  

__Base Legal:__

<a id="_Hlk114567244"></a>Manual “TABELAS DCIP PREVISTA NO ITEM 3\.4\.2\.1 DO ANEXO I DA PORTARIA SEF Nº 153/12” 

Item 3\.4\.2\.1 da Portaria SEF Nº 153/12 de Santa Catarina\.

__Campos:__

__Campo__

__Regra de Preenchimento__

Código Tipo 3

Preencher com o campo “Nº” da lista “Tipo 3 \- Crédito Presumido” disponível no Manual “TABELAS DCIP PREVISTA NO ITEM 3\.4\.2\.1 DO ANEXO I DA PORTARIA SEF Nº 153/12”

Descrição Tipo 3

Preencher com o campo “Descrição” da lista “Tipo 3 \- Crédito Presumido” disponível no Manual “TABELAS DCIP PREVISTA NO ITEM 3\.4\.2\.1 DO ANEXO I DA PORTARIA SEF Nº 153/12”

Descrição Complementar

Preencher com o campo “Descrição Complementar” da lista “Tipo 3 \- Crédito Presumido” disponível no Manual “TABELAS DCIP PREVISTA NO ITEM 3\.4\.2\.1 DO ANEXO I DA PORTARIA SEF Nº 153/12”

Validade Inicial

Preencher com o campo “Início” da lista “Tipo 3 \- Crédito Presumido” disponível no Manual “TABELAS DCIP PREVISTA NO ITEM 3\.4\.2\.1 DO ANEXO I DA PORTARIA SEF Nº 153/12”

Validade Final

Preencher com o campo “Fim” da lista “Tipo 3 \- Crédito Presumido” disponível no Manual “TABELAS DCIP PREVISTA NO ITEM 3\.4\.2\.1 DO ANEXO I DA PORTARIA SEF Nº 153/12”

Tabela: EST\_SC\_DIME\_TIPO3

MFS\-91937

__RN\-TACES105__

__Tabela TACES105 \- Tabela de Outros Produtos e Serviços DESIF \- Anexo 10__

A tabela TACES105 foi criada com a finalidade de carregar a lista estabelecida no Anexo 10 – Tabela de Outros Produtos e Serviços da DES\-IF\.  

__Base Legal:__

Secretaria Municipal de Fazenda da Prefeitura de São Paulo:

Instrução Normativa SF/SUREM Nº 17, DE 26 DE SETEMBRO DE 2017

Portaria SF/SUREM nº 57, de 4 de outubro de 2017

A DES\-IF é um validador municipal para financeiras, que hoje atende ao município de São Paulo\. No Mastersaf atendemos a tal obrigação através do módulo São Paulo\-Financeiras\.

A primeira carga da TACES 105 está sendo feita com a versão do anexo 10 aqui anexada\.

__Campos:__

__Campo__

__Sugestão__

__Chave__

__Tipo__

__Tamanho__

Código Produto/Serviço

COD\_PSERV\_DESIF

\(\*\)

A

4

Grupo Produto/Serviço

GRUPO\_PSERV\_DESIF

A

100

Descrição Produto/Serviço

DSC\_PSERV\_DESIF

A

200

Indicador de Obrigatoriedade da Descrição Complementar

IND\_OBRIG\_COMPL

A

1

__![](data:image/x-emf;base64,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EQDe/xEA3v8QALb/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABEAwP8TAO3/EwDs/2FV8v//////QTPu/xIA6f8SAOn/EgDo/2FV8P//////QTPr/xIA5f9xZu///////1FE6v8SAOP/0Mz5/7Cq9f8SAOH/EgDg/xIA4P8RAN//EQDe/xAAtv8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEQDA/xMA7f8TAO3/YlXy/////////////////4F38/8SAOn/YVXw//////9BM+z/EgDm/0Ez6v//////YVXt/xIA4//QzPn////////////QzPn/EgDg/xIA4P8RAN//EAC2/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARAMH/EwDu/xMA7f9iVfP//////0Ez7/9hVfL//////1FE7/9hVfD//////0Ez7f8SAOf/cWbw//////9RROz/EgDk/9DM+f+wqvb/EgDi/xIA4v8SAOH/EgDg/xIA4P8QALf/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABEAwf8TAO//EwDu/2JV8///////QjPw/2FV8v//////YVXx/2FV8P//////QTPt/yIR6v/QzPr/3938/xIA5f8SAOX/0Mz6/7Cq9v8SAOP/EgDi/xIA4v8SAOH/EgDg/xAAt/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEQDB/xMA7/8TAO//YlX0/////////////////8C7+v8SAOv/YVXx/////////////////8C7+f9BM+z/EgDm/xIA5f/QzPr////////////v7v3/EgDi/xIA4v8SAOH/EAC3/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARAML/EwDw/xMA7/8TAO//EwDu/xMA7f8TAO3/EwDs/xIA6/8SAOv/EgDq/xIA6f8SAOn/EgDo/xIA6P8SAOf/EgDm/xIA5f8SAOX/EgDk/xIA4/8SAOP/EgDi/xIA4v8QALj/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABEAwv8TAPH/EwDw/xMA7/8TAO//EwDu/xMA7f8TAO3/EwDs/xIA6/8SAOv/EgDq/xIA6f8SAOn/EgDo/xIA6P8SAOf/EgDm/xIA5f8SAOX/EgDk/xIA4/8SAOP/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)__

__RN\-TACES109__

__Tabela TACES109 \- Tabela de Natureza de Rendimentos x Código de Receita__

A tabela TACES109 foi criada com a finalidade de carregar o de\_para liberado pela receita da natureza de rendimentos x código de receita  

__Base Legal:__

Manual “Manual da EFD\-Reinf versão 2\.1\.1”, Anexo I – Tabela de natureza de rendimentos x código de receita

__Campos:__

__Campo__

__Sugestão__

__Chave__

__Tipo__

__Tamanho__

Evento

EVENTO

\(\*\)

A

6

Cód\. da Natureza do Rendimento

COD\_NAT\_REND

\(\*\)

N

5

Descrição da Natureza de Rendimento

DESCRICAO

A

450

Tributação no Exterior

TRIB\_EXT

\(\*\)

A

1

Tributo

TRIBUTO

\(\*\)

A

10

Indicador de Classif\. Tibutária 85

IND\_CLASSIF\_TRIB\_85

\(\*\)

A

3

Código de Receita

COD\_RECEITA

\(\*\)

A

6

Período de Apuração

PER\_APUR

\(\*\)

A

10

__Obs\. Nem todos os campos sugeridos na chave são de preenchimento obrigatório \(exemplo: tributo,  código de receita, período de apuração\)__

__Os campos nulos devem ser gravados no banco com um espaço, para colocá\-los como PK\.__

Tabela: CAD\_NAT\_REND\_COD\_RECEITA

MFS\-79890

__RN\-TACES110__

__Tabela TACES110\- Tabela de Cadastro de Grupo cClass NFe __

A tabela TACES110 foi criada com a finalidade de carregar os códigos de Grupo cClass dos modelos de documentos fiscais eletrônicos de energia elétrica NF3e \(código 66\) e serviços de comunicação NFCom\(código 62\) disponibilizados no Portal da NF\-e \([https://dfe\-portal\.svrs\.rs\.gov\.br/](https://dfe-portal.svrs.rs.gov.br/)\)

\.  

__Base Legal:__

# NF3e \(modelo 66\): Tabela de Código de Itens da NF3e \(cClass\) \([https://dfe\-portal\.svrs\.rs\.gov\.br/NF3E/tabelacclass](https://dfe-portal.svrs.rs.gov.br/NF3E/tabelacclass)\)

NFCom \(modelo 62\): ainda não está disponível a tabela para NFCom \([https://dfe\-portal\.svrs\.rs\.gov\.br/Nfcom](https://dfe-portal.svrs.rs.gov.br/Nfcom)\)

__Campos:__

__Campo__

__Regra de Preenchimento__

Código do Modelo

Códigos dos Modelos de Documento Fiscal\.

Segundo o Portal NF\-e os modelos 62 e 66 são os únicos com a informação de grupo cClass\.

Código Grupo cClass NFe

Código do Grupo cClass conforme tabela disponibilizada no Portal NF\-e\.

Descrição Código Grupo cClass NFe

Descrição do Grupo cClass conforme tabela disponibilizada no Portal NF\-e\.

Tabela: DWT\_GRUPO\_CCLASS

MFS90034

__Tabela TFIX96 \- CAT\_LAYOUT\_IMP__

A tabela TFIX96 foi criada com a finalidade de ser utilizada no processo de carga das tabelas SAFX no produto TAX ONE e para recepcionar as informações do manual de layout aba Layout TXT, disponível no módulo Job Servidor\. Hoje também é utilizada na rotina de Limpeza de tabelas definitivas do módulo Ferramentas \(menu Rotinas Acessórias à Inicialização à Exclusão de Tabelas Definitivas\)\.

A tabela TFIX96 – Tabela com o layout da carga para tabela SAFX deverá ser incluída no arquivo Tfixes\.xml para importação através da tela de importação da TFIX do módulo Ferramentas \(menu: Tabelas Internas >> Importar >> Tabelas Fixas/Acessórias\)\. Ver orientação ao final deste documento\. Necessário atualizar junto a TFIX97\.

__Obs\.: A TFIX96 está sendo utilizada no processo de carga de tabelas SAFX para o produto Tax One\.__

Campos:

NOM\_TAB\_WORK  VARCHAR2\(8\)       N                                            

NUM\_CAMPO         NUMBER\(4\)           N                                            

IND\_OBRIG             VARCHAR2\(1\)       N Indica se o campo e de preenchimento obrigatorio: S ou N\.

DESCRICAO           VARCHAR2\(300\)   N                                          

NOME\_CAMPO      VARCHAR2\(30\)      N Nome do campo no banco de dados\.

TAMANHO              VARCHAR2\(20\)      N Tamanho do campo, conforme manual de layout\. ex: vlr 015V002, aliq 003V004 ou 001\.

TIPO                        VARCHAR2\(1\)        N Informar A – Alfanumerico ou N \- Numerico\.

VERSAO                 VARCHAR2\(10\)       Y Versao do produto\.

PATCH                    VARCHAR2\(10\)       Y Patch de criacao da tabela\.

MFS\_ORIGEM        VARCHAR2\(30\)       Y Numero da demanda do jira de criacao da tabela\.

COD\_ERRO            VARCHAR2\(100\)     Y Relacao dos códigos de erros tratados para o campo\.

NOME\_CAMPO\_DEST VARCHAR2\(30\) Y Campo que sera utilizado no processo exportação \(Informação do campo

                                                                     correspondente na tabela definitiva\. O tratamento será apenas para campos que 

                                                                     tenham nomenclaturas diferentes ou que tenham referências com Idents\. Não será 

                                                                     necessário popular os campos com mesmas nomenclaturas\. 

                                                                     Ex: SAFX01 – campo 03 \- Data da Operação \(DATA\_OPERACAO\); Na 

                                                                            X01\_CONTABIL \(DATA\_LANCTO\)

DSC\_COMENTARIO VARCHAR2\(4000\) Y Comentario com orientacoes para preenchimento do campo na importacao da tabela SAFX

A carga inicial desta tabela foi realizada a partir das informações existentes no manual de layout aba Layout TXT\.

__Esclarecimento do preenchimento de alguns campos:__

Coluna

Regra de preenchimento

NOM\_TAB\_WORK

Nome da tabela temporária SAFX

NUM\_CAMPO

Coluna ITEM do Manual de Layout\.

IND\_OBRIG

Coluna OBRIGATORIEDADE do Manual de Layout\.

DESCRICAO

Coluna DESCRIÇÃO do Manual de Layout\.

NOME\_CAMPO

Campo da tabela temporária SAFX\. Coluna NOME DO CAMO do Manual de Layout

NOME\_CAMPO\_DEST

Preenchido APENAS quando o nome do campo na tabela definitiva for diferente do nome do campo da SAFX correspondente\. Exemplo SAFX2001:

__NOME\_CAMPO    NOME\_CAMPO\_DEST__

DATA\_X2001         VALID\_OPERACAO

MFS27738 / MFS28198

__RN\-TACES111__

__Tabela TACES111\- Tabela de Código de Tributação p/ Município __

A tabela TACES111 foi criada com a finalidade de criar o DE/PARA entre o Código de Serviço da Lei Complementar 116/03 e a tabela de Código de Tributação por Município, pela Prefeitura de Juiz de Fora, alterando a regra de preenchimento da TAG <ItemListaServiço> do validador FINTELISS, para uma lista específica com 9 posições\. Essa tabela está sendo criada também para viabilizar alterações futuras de outras prefeituras\.

__Campos: Regra de Preenchimento__

__Campo__

__Regra de Preenchimento__

Código de Estado \(UF\)

O campo de Código de Estado deverá estar cadastrado na tabela de ESTADO 

Código de Município

O campo de Código de Município deverá estar cadastrado na tabela de MUNICIPIO

Código Tributação p/ Município

Sem Regra de preenchimento\. O Código de Tributação, será informado pelo usuário ou conforme tabela disponibilizada pela Prefeitura\. 

Descrição Código Tributação p/ Município

Sem Regra de preenchimento\. A Descrição do Código de Tributação, será informado pelo usuário ou conforme tabela disponibilizada pela Prefeitura\.

__Campos:__

__Campo__

__Sugestão__

__Chave__

__Tipo__

__Tamanho__

Código de Estado \(UF\)

COD\_ESTADO

\(\*\)

A

2

Código de Município

COD\_MUNICIPIO

\(\*\)

N

5

Código Tributação p/ Município

COD\_TRIBUTACAO\_MUNIC

\(\*\)

A

12

Descrição Código de Tributação p/ Munic

DSC\_TRIBUTACAO\_MUNIC

A

250

Tabela: CAD\_TRIBUTACAO\_MUNIC

MFS\-515567

__RN\-TACES112__

__Tabela TACES112\- Tabela de Produtos Sujeitos à Tributação Monofásica ICMS __

A tabela TACES112 é carregada com os códigos de combustíveis sujeitos a tributação monofásica do ICMS, partir da tabela disponibilizada no portal da Nfe\.

Base Legal:

[Portal da Nota Fiscal Eletrônica \(fazenda\.gov\.br\)](https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=/NJarYc9nus=) \- Tabela de códigos de combustíveis sujeitos à tributação monofásica de ICMS\.

![](data:image/x-emf;base64,AQAAAGwAAAAAAAAAAQAAAH0AAABLAAAAAAAAAAAAAADeCAAAxQUAACBFTUYAAAEAnCAAABUAAAACAAAAAAAAAAAAAAAAAAAAgAcAADgEAABYAQAAwgAAAAAAAAAAAAAAAAAAAMA/BQDQ9QIAGAAAAAwAAAAAAAAAGQAAAAwAAAD///8AcgAAAKAZAAArAAAAAQAAAFIAAAAoAAAAKwAAAAEAAAAoAAAAKAAAAACA/wEAAAAAAAAAAAAAgD8AAAAAAAAAAAAAgD8AAAAAAAAAAP///wAAAAAAbAAAADQAAACgAAAAABkAACgAAAAoAAAAKAAAACgAAAAoAAAAAQAgAAMAAAAAGQAAAAAAAAAAAAAAAAAAAAAAAAAA/wAA/wAA/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABaW12ydHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/WltdsgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdHd5//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHR3ef/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB0d3n/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdHd5//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHR3ef/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB0d3n/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdHd5//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHR3ef/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/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AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdHd5//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef/6+vr/+vr6//r6+v/6+vr/yMnJ/3R3ef8rLC1gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHR3ef/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/+vr6//r6+v/6+vr/yMnJ/3R3ef8rLC1gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB0d3n/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5//r6+v/6+vr/yMnJ/3R3ef8rLC1gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdHd5//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef/6+vr/yMnJ/3R3ef8rLC1gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHR3ef/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/yMnJ/3R3ef8rLC1gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB0d3n/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/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)

__Campos: Regra de Preenchimento__

__Campo__

__Regra de Preenchimento__

Código Produto Oficial

Código do produto ANP  \(cProdANP\) conforme Tabela de Combustíveis Sujeitos à Tributação Monofásica\-20230419\.xlsx\)

Descrição do Produto

Descrição do produto conforme Tabela de Combustíveis Sujeitos à Tributação Monofásica\-20230419\.xlsx

Alíquota ad Rem ICMS

Alíquota ad Rem ICMS \(adRemICMS\) conforme Tabela de Combustíveis Sujeitos à Tributação Monofásica\-20230419\.xlsx

Validade Inicial

Data Início da vigência conforme Tabela de Combustíveis Sujeitos à Tributação Monofásica\-20230419\.xlsx

Validade Final

Data Fim da vigência conforme Tabela de Combustíveis Sujeitos à Tributação Monofásica\-20230419\.xlsx

Indicador de Biocombustível

Campo não existe na Tabela de Combustíveis Sujeitos à Tributação Monofásica\-20230419\.xlsx\. Foi criado pela nossa solução para indicar com S os biocombustíveis\. No momento marcamos com S apenas o B100\.

__Campos:__

__Campo__

__Sugestão__

__Chave__

__Tipo__

__Tamanho__

Código Produto Oficial

COD\_PROD\_OFICIAL

\(\*\)

A

10

Descrição do Produto

DSC\_PROD\_OFICIAL

A

250

Alíquota ad Rem ICMS

ALIQ\_AD\_REM\_ICMS

N

7\(3int 4dec\)

Validade Inicial

DAT\_VALID\_INI

\(\*\)

D

Validade Final

DAT\_VALID\_FIM

D

Indicador de Biocombustível

IND\_BIOCOMB

A

1

Tabela: __CBT\_PRD\_ICMS\_MONO__

MFS\-540746

__RN\-TFIX97__

__Tabela TFIX97 \- CAT\_LAYOUT\_HIST__

A tabela TFIX97 foi criada com a finalidade de ser utilizada para recepcionar as informações da planilha de alterações SAFX aba Alterações no Manual de Layout\.

A tabela TFIX97 – Tabela com as alterações realizadas nas tabelas SAFX deverá ser incluída no arquivo Tfixes\.xml para importação através da tela de importação da TFIX do módulo Ferramentas \(menu: Tabelas Internas >> Importar >> Tabelas Fixas/Acessórias\)\. __Obs\.: Sempre atualizar essa tabela junto com a TFIX96\.__

Campos:

NOM\_TAB\_WORK   VARCHAR2\(8\)    N                                            

NUM\_CAMPO          NUMBER\(4\)        N                                            

PATCH                     VARCHAR2\(10\)  N  Patch de criacao da tabela\.

IND\_OBRIG             VARCHAR2\(1\)     N  Indica se o campo e de preenchimento obrigatorio: S ou N\.

DESCRICAO           VARCHAR2\(300\) N                                            

NOME\_CAMPO      VARCHAR2\(30\)   N   Nome do campo no banco de dados\.

TAMANHO              VARCHAR2\(20\)   N  Tamanho do campo, conforme manual de layout\. ex: vlr 015V002, aliq 003V004 ou 001\.

TIPO                       VARCHAR2\(1\)     N   Informar A – Alfanumerico ou N \- Numerico\.

VERSAO                VARCHAR2\(10\)    Y  Versao do produto\.

MFS\_ALTERA       VARCHAR2\(30\)    Y  Numero da demanda do jira de alteracao da tabela\.

IND\_ALT                VARCHAR2\(3\)       Y Indica o tipo de alteracao realizada na tabela, conforme abaixo\. C/S – Criação de

                                                                 SAFX; M/S – Modifica Estrutura da SAFX; I/C – Inclusao de Campo em SAFX; A/N – 

                                                                Alteracao de Nome de Campo em SAFX; A/O – Alteracao do Campo Obrigatoriedade; 

                                                                C/C – Alteracao de Comentario do Campo; A/D – Alteracao do Campo Descricao; A/T –  

                                                               Alteracao do Campo Tamanho; T/C – Alteracao do Tipo de Campo; C/E – Critica de                          

                                                                Erros

DSC\_COMENTARIO VARCHAR2\(4000\) Y Comentario com orientacoes para preenchimento do campo na importacao da tabela SAFX

A carga inicial desta tabela foi realizada a partir das informações existentes na planilha de alterações SAFX aba Alterações no Manual de Layout\.

Obs\.: Na MFS\-28198 realizar a mudança do campo DSC\_COMENTARIO para última posição da tabela\.

MFS27738 / MFS28198

__RN\-TFIX11__

__Tabela TFIX11 \- CAT\_PRIOR\_IMP \- Catálogo Prioridade de Importação__

__Esclarecimento de preenchimento de alguns campos:__

Coluna

Regra de preenchimento

NOM\_TAB\_WORK

Nome da tabela temporária SAFX

NOM\_TAB\_DEF

Nome da tabela Definitiva correspondente a SAFX

DATA\_REF\_TAB\_DEF

Campo pertencente à tabela temporária SAFX do tipo Data\.

Informação utilizada em dois processos:

\- Importação do módulo Job Servidor, na versão multi load \(ind\_multi\_load = “S’\);

\- Limpeza de tabelas definitivas do módulo Ferramentas \(menu Rotinas Acessórias à Inicialização à Exclusão de Tabelas Definitivas\)\.

IND\_MULTI\_LOAD

Indicador para processo de importação na versão multi load\.

LEGISLACAO

Legislacao a que a tabela esta vinculada \(Manual de Layout\)

OBJETIVO

Objetivo que orienta sobre a utilizacao da tabela \(Manual de Layout\)

\[MFS28198\]

Ajusta a estrutura da TFIX11, para contemplar 2 novos campos, LEGISLACAO e OBJETIVO\. Campos utilizados para incluir as informaçõe da aba índice do manual de layout, disponibilizado no módulo Job Servidor, menu Carga\.

MFS\-28198

__RN\-TFIX101__

__Tabela TFIX101 – ICT\_COD\_GNRE – Códigos para GNRE__

__Esclarecimento de preenchimento de alguns campos:__

Coluna

Regra de preenchimento

COD\_GNRE

Código da Guia Nacional de Recolhimento

DESCRICAO

Descrição do código

\[MFS30790\]

Cria a TFIX101 para a importação da tabela ICT\_COD\_GNRE que era utilizada no processo padrão de carga da tabela acessória TACES78\. 

MFS\-30790

__RN\-TFIX142__

__Tabela TFIX142 – Cadastro dos Modelos dos Livros Fiscais__

__Esclarecimento de preenchimento de alguns campos:__

Coluna

Regra de preenchimento

COD\_TIPO\_LIVRO

Código do Tipo do Livro Fiscal

ITEM\_MENU\_EMISSAO

Opção de menu de emissão do livro: pode ser um sequencial criado por livro\. No caso dos livros P3 \(105\) e P7 \(118, 107\) será gravado o conteúdo do campo MODELO da estrutura S\_PARAM\_CHAMADA que é passada como parâmetro no Open da janela de emissão\.  O campo Modelo da S\_PARAM\_CHAMADA já identifica o item de emissão do P3 e do P7

DSC\_MENU\_EMISSAO

Titulo da opção do menu de emissão do livro

DSC\_TIPO\_LIVRO

Descrição no Tipo de Livro que será apresentada na tela de Programação Batch \(deve ser preenchido com o NOM\_OFICIAL da tabela TIPO\_LIVRO\_FISCAL\)

MODELO

Modelo gravado na ICT\_CONTROLE \(que deve ser o mesmo MODELO a ser gravado na ICA\_PARAM\_GER\_APUR\)

DSC\_MODELO

Descrição do Modelo \(Ajuste Sinief, Convênio ICMS,\.\.\.\)

COD\_MODULO

COD\_MODULO da tabela PRT\_MODULOS\_MSAF: 005 \- ICMS, 010 \- IPI'

IND\_EXIBE\_PROG\_BATCH

Identifica os livros/modelos que serão apresentados na tela de  Programação dos Livros BATCH

IND\_EXIBE\_MODELO

Indica se o modelo do livro será apresentado na tela de Programação dos Livros BATCH

FORMATO\_LIVRO

Formato do Livro

IND\_TELECOM

Indicador de Telecom 

IND\_OBS\_VALOR\_ST

Indicador de observação de valor ST

IND\_RESUMO\_OBSERVACOES

Indicador de resumo de observações

IND\_TRATA\_ICMSS\_N\_ESCRIT

Indicador de tratamento de ICMSS Não Escrituário

IND\_BASE\_ST\_N\_ESCRIT\_OBS

Indicator de base ST Não Escrituário OBS

Cria a TFIX142 para a importação da tabela ICT\_PAR\_MODELO\_LIVRO que era populada no DW através de um script enviado pelo suporte aos clientes, mas para o Tax One precisamos torná\-la uma TFIX para que a mesma possa ser pupulada no banco de forma automática\.

MFS\-29352

__RN\-TFIX/TACES__

__TABELAS INTERNAS > IMPORTAR__

Adequar o menu para:

Tabelas Fixas/Acessórias

Tabelas Acessórias

Tabelas Fixas/Acessórias: Modificado para receber a importação automatizada de tabelas acessórias, juntamente com as tabelas fixas\. Este processo utiliza o arquivo tfixes\.xml\.

Tabelas Acessórias: Manter o menu para realizar a importação apenas de 17 tabelas acessórias que contém regras específicas e não foram inclusas no processo automatizado\. São elas: 

- TACES03 \- Situação Tributária Estadual \- A
- TACES04 \- Situação Tributária Estadual \- B
- TACES07 \- Nacionalidades
- TACES11 \- Observações de Livros Fiscais
- TACES31 \- Cadastro de CBC Moedas \(SPED\)
- TACES32 \- Cadastro da Consolidação de Normas Cambiais \(CNC\)
- TACES33 \- Cadastro de CBC País Acordo Jurisdição
- TACES55 \- Grupo Produtos do DACON
- TACES56 \- Produtos do DACON
- TACES57 \- Produtos SERC
- TACES66 \- Tabela de Categoria de Trabalhador \(eSocial\)
- TACES70 \- Cadastro Tipo de Documento DEREX  __\[MFS61949\-MFS73138\]__ A TACES70 é importada automaticamente
- TACES71 \- Parametrização dos Tipos de Crédito __\[MFS61949\]__ A TACES71 não é importada automaticamente
- TACES73 \- Parametrização dos Códigos de Contribuição
- TACES92 \- Tipo de Cliente
- TACES93 \- Subclasse de Consumo
- <a id="_Hlk83307326"></a>TACES98 – Cadastro de Código de Instalação de Obrigações __\[MFS73138\]__ Inclusão da TACES98 da lista de tabelas 
- TACES99 \- Catálogo de Empresas para OLSS __\[MFS43745\-MFS\-73138\]__ Retirada da TACES99 da importação
- TACES100 \- Observações por UF/Situação Especial ST

__Atenção: \(MFS\-74425\) Atualização Manual Operacional__

No processo de importação das tabelas Acessórias \(TACES\) obrigatoriamente a nomenclatura e extensão deverão ser utilizadas com a __escrita em maiúsculo__, __TACESAAA\.TXT__ \(AAA: Número TACES\), o intuito é evitar possíveis problemas identificados no momento da importação devido particularidades de sistema operacional, com isso estamos padronizando o processo para todos os clientes independente se utilizam Windows ou Linux\. 

__RN\-TFIX/TACES__

__ IMPORTANTE: Ver regras desse processo ao final deste documento\.__

__\- Sempre que houver atualização nessas tabelas Acessórias atualizar as Pastas “ZIP” \(TaxOne\_TAB\_Acessorias\.zip\) no CVS e abrir uma MDOC para Equipe de documentação disponibilizar a tabela atualizada no Help do TAX ONE, Aba Downloads\.__

__RN\-TFIX60__

__Tabela TFIX60 – Código de Serviço conforme lista Anexo I da Lei Complementar 116/03__

Esta TFIX refere\-se ao código da Lei Complementar 116/03

Campos:

Campos

Tipo / Tamanho

Chave

Código Lei 116/03

VARCHAR2\(4\)

\*

Data

DATE

Descrição

VARCHAR2 \(100\)

tipo\_serv\_lei\_116

CHAR\(1\)

__RN\-TACES113__

__Tabela TACES113 – Código de Classificação cClass da NFCOM__

__A tabela TACES113 foi criada com a finalidade de importar e manutenir os códigos de Classificação de Item da NFCom\.__

__Nome da Tabela: CAD\_CCLASS\_NFCOM__

__Campos:__

__Campo__

__Sugestão__

__Chave__

__Tipo__

__Tamanho__

Grupo / Código

COD\_CCLASS\_NFCOM

\(\*\)

A

7

Descrição

DSC\_CCLASS\_NFCOM

\(\*\)

A

200

__Campos: Regra de Preenchimento__

__Campo__

__Regra de Preenchimento__

Grupo / Código

Código de Classificação de Item da NFCom\.  
Sem Regra de preenchimento\. O Código, será informado pelo usuário ou conforme tabela disponibilizada\.

Descrição

Sem Regra de preenchimento\. A Descrição do Código de Classificação de Item da NFCom, será informada pelo usuário ou conforme tabela disponibilizada\.

__Críticas:__

Grupo / Código \(campo chave\) à Campo obrigatório\.

Descrição \(campo chave\) à Campo obrigatório\.

MFS591910

__RN\-TACES114__

Taces114 \- Grupamento dos Combustíveis para os Anexos da Monofasia

Objetivo: Tabela para armazenar a relação dos Combustível para geração dos Anexos da Tributação Monofásica, disponibilizados no módulo Combustíveis e Derivados de Petróleo\.

Tabela CBT\_PROD\_SEF\_CENTR

__Campo__

__Regra de Preenchimento__

Código do Anexo

\(COD\_ANEXO\)

Preenchido com os códigos dos anexos conforme domínio:

1M

2M

3M

Código do Produto SEF

\(COD\_PROD\_SEF\)

Preenchido com os códigos do produto SEF conforme tabela 4\.2 do manual do SCANC CTB\.

Exemplo:

DSL 

BXD

S10

BXS

Código do Produto SEF Centralizador

\(COD\_PROD\_SEF\_CENTR\)

Os anexos I\-M e II\-M, que são gerados consolidando mais de um combustível, esse campo indica o combustível para qual o anexo será gerado\.

Exemplo: DSL é centralizador dos combustíveis DSL, BXD, S10 e BXS\. É gerado um único Anexo I\-M com as informações dos quatro combustíveis em nome do DSL\.

O Anexo III\-M consolida todos os combustíveis \(diesel e gasolina\) num compõe um único Anexo III\-M\. Logo o preenchimento desse campo é indiferente\.

Descrição do Produto SEF Centralizador

\(DSC\_PROD\_SEF\_CENTR\)

Descrição do Produto SEF Centralizador, que juntamente com o código, que será apresentado no cabeçalho dos anexos I\-M e II\-M\.

MFS772704

<a id="_Hlk175674524"></a>__RN\-TFIX143__

__Tabela TFIX143\- Tabela de Parâmetros MasterSAF Nomenclatura por UF__ 

<a id="_Hlk175674422"></a>A tabela TFIX143 foi criada com a finalidade de carregar os Códigos de Parâmetros que são apresentados nas telas de Parametrização por CFOP e CFOP/Natureza Operação para geração do registro 1400 do Sped Fiscal\. As telas são:

\- Parâmetros à Registro 1400 à Específico por UF à CFOP

\- Parâmetros à Registro 1400 à Específico por UF à CFOP / Natureza de Operação

\- Parâmetros à Registro 1400 à Específico por UF à Deduções à CFOP

\- Parâmetros à Registro 1400 à Específico por UF à Deduções à CFOP / Natureza de Operação

  

__Base Legal:__

Cada UF tem sua regra para geração do registro 1400\.

__Campos:__

__Campo__

__Regra de Preenchimento__

Código do Parâmetro

Código oriundo da TFIX31 \- Parâmetros MasterSAF Nomenclatura \- PRT\_PAR2\_MSAF

Código da UF

Código do Estado da Tabela ESTADO

Tipo CFO

Campo indica se o Código do Parâmetro estará relacionado a CFOP’s de Entradas, Saídas ou os dois\. Esse campo é preenchido com:

E – apenas CFOP’s de Entrada;

S – apenas CFOP’s de Saída;

T – considera CFOP’s de Entrada e Saída\.

Tipo DED

Campo indica se o Código do Parâmetro será utilizado nas telas de Deduções ou nas telas Normais\. Campo é preenchido com:

S – Utilizado nas telas de Deduções \(Específico por UF à Deduções à CFOP e CFOP / Natureza de Operação\)

N – Utilizado nas telas Normais \(Específico por UF à CFOP e CFOP / Natureza de Operação\)\.

Tabela: PRT\_PAR\_OPER\_UF

MFS651592

__RN\-TACES115__

__Tabela TACES115 \- Tabela de Código de Situação Tributária do IBS e da CBS \- Reforma Tributária__

A tabela TACES115 foi criada com a finalidade de carregar o Cadastro dos Códigos de Situação Tributária do IBS e da CBS, para atender a Reforma Tributária\.

A tabela deverá ser incluída na tela de importação da TACES/TFIX do módulo Ferramentas \(menu: Tabelas Internas >> Importar >> Tabelas Acessórias\)\.

__Campos:__

__Campo__

__Sugestão__

__Chave__

__Obrigatório__

__Tipo__

__Tamanho__

CST – IBS/CBS

COD\_CST\_IBS\_CBS

Sim

Sim

A

3

Descrição CST\-IBS/CBS

DESCR\_IBS\_CBS

Não 

Sim

A

100

Ind\_gIBSCBS

IND\_GIBSCBS

Não

SIm

A

1

Ind\_gIBSCBSMono

IND\_GIBSCBS\_MONO

Não

Sim

A

1

Ind\_gRed

IND\_GRED

Não

Sim

A

1

Ind\_gDif

IND\_GDIF

Não

Sim

A

1

Ind\_gTransfCred

IND\_GTRANSF\_CRED

Não

Sim

A

1

Ind\_gCredPresIBSZFM

IND\_GCRED\_PRES\_IBS\_ZFM

Não

Sim

A

1

ind\_gAjusteCompet

IND\_G\_AJUSTE\_COMPET

Não

Sim

A

1

ind\_RedutorBC

IND\_REDUTOR\_BC

Não

Sim

A

1

indNFe

IND\_NFE

Não

Sim

A

3

indNFCe

IND\_NFCE

Não

Sim

A

3

indCTe

IND\_CTE

Não

Sim

A

3

indCteOS

IND\_CTE\_OS

Não

Sim

A

3

indBPe

IND\_BPE

Não

Sim

A

3

indBPeTM

IND\_BPE\_TM

Não

Sim

A

3

indNF3e

IND\_NF3E

Não

Sim

A

3

indNFCom

IND\_NFCOM

Não

Sim

A

3

indNFSe

IND\_NFSE

Não

Sim

A

3

Tabela: CAD\_CST\_IBS\_CBS

A carga inicial desta tabela foi realizada a partir do arquivo liberado no portal de Nfe\(data 18/06/2025\)\.

Críticas:

__CST – IBS/CBS __\(campo chave\) à Campo obrigatório\.

__Descrição CST – IBS/CBS __à Campo obrigatório\.

__Ind\_gIBSCBS__ à Campo obrigatório\. Lista de valores válidos:

branco

‘0’ – Não é permitido

‘1’\-Exige 

__Ind\_gIBSCBSMono __à Campo obrigatório\. Lista de valores válidos:

branco

‘0’ – Não é permitido

‘1’\-Exige 

__Ind\_gRed__à Campo obrigatório\. Lista de valores\. Validação de valores válidos:

branco

‘0’ – Não é permitido

‘1’\-Exige 

__Ind\_gDif__ à Campo obrigatório\. Lista de valores válidos:

branco

‘0’ – Não é permitido

‘1’\-Exige 

__Ind\_gTransfCred__à Campo obrigatório\.Lista de valores válidos:

branco

‘0’ – Não é permitido

‘1’\-Exige 

__Ind\_gCredPresIBSZFM __à Campo obrigatório\. Lista de valores\. Validação de valores válidos:

‘0’ – Não é permitido

‘1’\-Exige 

__Ind\_gAjusteCompet__à Campo obrigatório\. Lista de valores\. Validação de valores válidos:

‘0’ – Não é permitido

‘1’\-Exige 

__Ind\_RedutorBC__à Campo obrigatório\. Lista de valores\. Validação de valores válidos:

‘0’ – Não é permitido

‘1’\-Exige 

__indNFe, indNFCe, indCTe, indCteOS, indBPe, indBPeTM, indNF3e, indNFCom e/ou indNFSe __à Lista de valores válidos:

‘Não’

‘Sim’

MFS\-822287

MFS\-848570

MFS\-951840

MFS\-987950

__RN\-TACES116__

__Tabela TACES116 \- Tabela de Classificação Tributária do IBS e da CBS \- Reforma Tributária__

A tabela TACES116 foi criada com a finalidade de carregar o Cadastro das Classificações Tributárias do IBS e da CBS, para atender a Reforma Tributária\.

A tabela deverá ser incluída na tela de importação da TACES/TFIX do módulo Ferramentas \(menu: Tabelas Internas >> Importar >> Tabelas Acessórias\)\.

__Campos:__

__Campo__

__Sugestão__

__Chave__

__Obrigatório__

__Tipo__

__Tamanho__

cClassTrib

COD\_CCLASS\_TRIB

Sim

Sim

A

6

Nome cClassTrib

NOME\_CCLASS\_TRIB

Não 

Sim

A

200

Descrição cClassTrib

DESC\_CCLASS\_TRIB

Não

Sim

A

1200

LC Redação

LC\_REDACAO

Não

Não

A

1200

LC 214/25

LC\_214\_25

Não

Não

A

50

Tabela: CAD\_CCLASS\_TRIB

A carga inicial desta tabela foi realizada a partir do arquivo liberado no portal de Nfe \(data 18/06/2025\)\.

Críticas:

__cClassTrib__ \(campo chave\) à Campo obrigatório\.

__Nome cClassTrib__ à Campo obrigatório\.

__Descrição cClassTrib__ à Campo obrigatório\.

MFS\-822287

MFS\-848570

MFS\-951840

MFS\-987950

__RN\-TACES117__

__Tabela TACES117 \- Tabela de Código de Situação Tributária x Classificação Tributária \(do IBS e da CBS\) \-Reforma Tributária__

A tabela TACES117 foi criada com a finalidade de carregar o Código de Situação Tibutária x Classificações Tributárias do IBS e da CBS, para atender a Reforma Tributária\.

A tabela deverá ser incluída na tela de importação da TACES/TFIX do módulo Ferramentas \(menu: Tabelas Internas >> Importar >

> Tabelas Acessórias\)\.

__Campos:__

__Campo__

__Sugestão__

__Chave__

__Obrigatório__

__Tipo__

__Tamanho__

CST – IBS/CBS

COD\_CST\_IBS\_CBS

Sim

Sim

A

3

Descrição CST – IBS/CBS

DESC\_CST\_IBS\_CBS

Não

Sim

A

100

cClassTrib

COD\_CCLASS\_TRIB

Sim

Sim

A

6

Nome cClassTrib

NOME\_CCLASS\_TRIB

Não 

Sim

A

200

Descrição cClassTrib

DESC\_CCLASS\_TRIB

Não

Sim

A

1200

LC Redação

LC\_REDACAO

Não

Não

A

1200

LC 214/25

LC\_214\_25

Não

Não

A

50

Tipo de Alíquota

TIPO\_ALIQUOTA

Não

Sim

A

50

pRedIBS

PERC\_RED\_IBS

Não

Sim

A

005

pRedCBS

PERC\_RED\_CBS

Não

Sim

A

005

Ind\_RedutorBC

IND\_REDUTOR\_BC

Não

Não

A

005

Ind\_gTribRegular

IND\_G\_TRIB\_REGULAR

Não

Não

A

001

Ind\_CredPres Ind\_gCredPresOper

IND\_G\_CRED\_PRES\_OPER

Não

Sim

A

001

IndMono Ind\_gMonoPadrao

IND\_G\_MONO\_PADRAO

Não

Sim

A

001

indMonoReten Ind\_gMonoReten

IND\_G\_MONO\_RETEN

Não

Sim

A

001

indMonoRet Ind\_gMonoRet

IND\_G\_MONO\_RET

Não

Sim

A

001

indMonoDif Ind\_gMonoDif

IND\_G\_MONO\_DIF

Não

Sim

A

001

ind\_gEstornoCred

IND\_G\_ESTORNO\_CRED

Não

Sim

A

001

Crédito para

CREDITO\_PARA

Não

Não

A

500

dIniVig 

DT\_INICIAL

Sim

Sim

D

8

dFimVig 

DT\_FIM

Sim

Não

D

8

DataAtualização

DT\_ATUALIZACAO

Não

Sim

D

8

indNFeABI

IND\_NFE\_ABI

Não

Sim

A

001

indNFe

IND\_NFE

Não

Sim

A

001

indNFCe

IND\_NF\_CE

Não

Sim

A

001

indCTe

IND\_CTE

Não

Sim

A

001

indCTeOS

IND\_CTE\_OS

Não

Sim

A

001

indBPe

IND\_BPE

Não

Sim

A

001

indBPeTA

IND\_BPE\_TA

Não

Sim

A

001

indBPeTM

IND\_BPE\_TM

Não

Sim

A

001

indNF3e

IND\_NF3E

Não

Sim

A

001

indNFSe

IND\_NFSE

Não

Sim

A

001

indNFSe Via

IND\_NFSE\_VIA

Não

Sim

A

001

indNFCom

IND\_NFCOM

Não

Sim

A

001

indNFAg 

IND\_NFAG

Não

Sim

A

001

indNFGas

IND\_NFGAS

Não

Sim

A

001

indDERE

IND\_DERE

Não

Sim

A

001

ANEXO

ANEXO

Não

Não

A

002

Link

LINK

Não

Não

A

100

__Obs\. Nem todos os campos sugeridos na chave são de preenchimento obrigatório \(exemplo: dIniVig, dFimVig,\)__

__Os campos nulos devem ser gravados no banco com um espaço, para colocá\-los como PK\.__

Tabela: CAD\_CST\_IBS\_CBS\_x\_CCLASS\_TRIB

A carga inicial desta tabela foi realizada a partir do arquivo liberado no portal de Nfe\(data 18/06/2025\)\.

Críticas:

__CST – IBS/CBS__ \(campo chave\)à Campo obrigatório\.Deve estar cadastrada na tabela CAD\_CST\_IBS\_CBS

__Descrição CST – IBS/CBS__ à Campo obrigatório\.Recupera da CAD\_CST\_IBS\_CBS

__CClassTrib __\(campo chave\)à Campo obrigatório\.Deve estar cadastrada na tabela CAD\_CCLASS\_TRIB

__Nome cClassTrib__ à Campo obrigatório\.Recupera da CAD\_CCLASS\_TRIB

__Descrição cClassTrib__ à Campo obrigatório\.Recupera da CAD\_CCLASS\_TRIB

__LC Redação__ à Campo obrigatório\.Recupera da CAD\_CCLASS\_TRIB

__LC 214/25__ à Campo obrigatório\.Recupera da CAD\_CCLASS\_TRIB

__Tipo de Alíquota__ à Campo obrigatório\.

__pRedIBS__à Campo obrigatório\. Lista de valores válidos:

branco,

30, 

40, 

50,

60,

70,

80, 

100,

N/A

__pRedCBS__à Campo obrigatório\.Lista de valores válidos:

branco,

30, 

40, 

50,

60,

70,

80, 

100,

N/A

__indRedutorBC__à Lista de valores válidos:

branco, 

N,

S,

N/A

__Ind\_g\_TribRegular__à Lista de valores válidos:

branco, 

0,

1

__Ind\_gCredPresOper__à  Campo obrigatório\.Lista de valores válidos:

Branco

0, 

1

__Ind\_gMonoPadrao__àCampo obrigatório\.Lista de valores válidos:

branco, 

0,

1

__Ind\_gMonoReten__à Campo obrigatório\.Lista de valores válidos:

branco, 

0,

1

__Ind\_gMonoRet__à Campo obrigatório\.Lista de valores válidos:

branco, 

0,

1

__Ind\_gMonoDif__à Campo obrigatório\.Lista de valores válidos:

branco, 

0,

1

__Ind\_gEstornoCred__à Campo obrigatório\.Lista de valores válidos: 

0,

1

__dIniVig __\(campo chave\)\. à Campo obrigatório\.Formato: DD/MM/AAAA

__dFimVig__ \(campo chave\) àDeve ser maior que o Campo dInVig\. Formato: DD/MM/AAAA

__DataAtualização __à__ __campo obrigatório\. Formato: DD/MM/AAAA

__indNFeABI, indNFe, indNFCe, indCTe, indCTeOS, indBPe, indBPeTA, indBPeTM, indNF3e, indNFSe, indNFSe Via, indNFCom, indNFAg, indNFGas e indDERE __àCampo obrigatório\. Lista de Valores Válidos:

0,

1

__Link__ àcampo obrigatório\.

MFS\-822287

MFS\-848570

MFS\-951840

MFS\-987950

__RN\-TACES118__

__Tabela TACES118 \- Tabela de Código de Crédito Presumido do do IBS e da CBS \- Reforma Tributária__

A tabela TACES118 foi criada com a finalidade de carregar o Código de Crédito Presumido do IBS e da CBS, para atender a Reforma Tributária\.

A tabela deverá ser incluída na tela de importação da TACES/TFIX do módulo Ferramentas \(menu: Tabelas Internas >> Importar >> Tabelas Acessórias\)\.

__Campos:__

__Campo__

__Sugestão__

__Chave__

__Obrigatório__

__Tipo__

__Tamanho__

cCredPres

CCRED\_PRES

Sim

Sim

A

3

Descrição 

DESC\_ CCRED\_PRES

Não

Sim

A

300

LC 214/2025

LC\_214\_2025

Não

Sim

A

1500

Apropria via NF?

APROPRIA\_VIA\_NF

Não

Sim

A

001

Apropria via Evento?

APROPRIA\_VIA\_EVENTO

Não

Sim

A

001

IndDeduzCredPres

IND\_DEDUZ\_CRED\_PRES

Não

Não

A

001

indCredPresCBS

IND\_DEDUZ\_CRED\_PRES\_CBS

Não

Não

A

001

indCredPresIBS

IND\_DEDUZ\_CRED\_PRES\_IBS

Não

Sim

A

001

Alíquota CBS

ALIQUOTA\_CBS

Não

Não

A

50

Alíquota IBS

ALIQUOTA\_IBS

Não

Não

A

50

pAliqCredPresCBS

P\_ALIQ\_CRED\_PRES\_CBS

Não

Não

A

200

cClass nota referenciada

CCLASS\_NOTA\_REFER

Não

SIm

A

50

dIniVig 

DT\_INICIAL

Sim

Sim

D

8

dFimVig 

DT\_FIM

Sim

Não

D

8

__Obs\. Nem todos os campos sugeridos na chave são de preenchimento obrigatório \(exemplo:   dFimVig\)__

__Os campos nulos devem ser gravados no banco com um espaço, para colocá\-los como PK\.__

Tabela: CCRED\_PRES

A carga inicial desta tabela foi realizada a partir do arquivo liberado no portal de Nfe \(04/07/25\)\.

Atualizada a carga conforme tabela \(data 06/10/2025\)

Críticas:

__cCredPres __\(campo chave\)à Campo obrigatório

__Descrição __ à Campo obrigatório

__LC 214/2025 __ à Campo obrigatório

__Apropria via NF?f__à Campo obrigatório

Lista de valores válidos:

‘0’ – Não é permitido

‘1’\-Exige 

__Apropria Evento?__ à Campo obrigatório

 Lista de valores válidos:

‘0’ – Não é permitido

‘1’\-Exige 

__IndDeduzCredPres__ à 

 Lista de valores válidos:

Branco

‘1’\-Exige 

__IndCredPresCBS __à Lista de valores válidos:

Branco

‘0’ – Não é permitido

‘1’\-Exige 

__IndCredPresIBS__ à campo obrigatório

Lista de valores válidos:

‘0’ – Não é permitido

‘1’\-Exige 

__cClass nota referenciada __à campo obrigatório

__dIniVig __\(campo chave\) à campo obrigatório\. Formato: DD/MM/AAAA

__dFimVig __\(campo chave\) àDeve ser maior que o Campo dInVig\. Formato: DD/MM/AAAA

MFS\-848570

MFS\-951840

__RN\-TACES119__

__Tabela TACES 119 – Tabela de Arrecadação \- DOOTAX__

__ __

A tabela TACES119 foi criada com o intuito de alimentar dados, utilizando como base a tabela obrigatória da DOOTAX \(Tax Payments\) para manutenção dos dados\. A tabela acessória deve facilitar a manipulação e a visualização dos dados, permitindo uma gestão mais eficiente das informações relacionadas a pagamentos de impostos e manutenção pelo usuário

__ __

__Campos:__

__ __

__Campo__

__Sugestão__

__Chave__

__Obrigatório__

__Tipo__

__Tamanho__

Unidade Federativa Favorecida

UF\_FAVORECIDA

\(\*\)

Não

C

2

Código de Arrecadação

COD\_ARREDACAO

\(\*\)

Sim

C

20

Código de Receita

COD\_RECEITA

\(\*\)

Sim

N

20

Detalhamento de Receita

DET\_RECEITA

\(\*\)

Não

N

20

__ __

Campo __UF__ à Campo de preenchimento obrigatório \(campo chave\)\. Na inserção de novas linhas, será exibida a lista das UF’s da tabela ESTADO, para o usuário selecionar a UF desejada;

__Dados carregados da planilha\.__

 

[__Cópia de Planilha de Apoio \- Campos Obrigatorios JSON \(1\) \(003\)__](https://trten.sharepoint.com/sites/RaizenCustom/Shared%20Documents/Raizen%20Custom/C%C3%B3pia%20de%20Planilha%20de%20Apoio%20-%20Campos%20Obrigatorios%20JSON%20(1)%20(003).xlsx?web=1)

MFS\- 877552

__RN\-TACES120__

__Tabela TACES120 \- Tabela de Códigos de Indicadores das Operações de Consumo \- Reforma Tributária__

A tabela TACES120 foi criada com a finalidade de carregar os Códigos de Indicadores das Operações de Consumo, para atender a Reforma Tributária\.

A tabela deverá ser incluída na tela de importação da TACES/TFIX do módulo Ferramentas \(menu: Tabelas Internas >> Importar >> Tabelas Acessórias\)\.

__Campos:__

__Campo__

__Sugestão__

__Chave__

__Obrigatório__

__Tipo__

__Tamanho__

Código indOp

COD\_IND\_OP

Sim

Sim

A

010

Art\. 11

ART\_11

Não

Sim

A

20

Tipo de operação

TIPO\_OPERACAO

Não

Sim

A

200

Considera\-se local da operação

CONSIDERA\_LOCAL\_OP

Não

Sim

A

200

Característica do fornecimento

CARACTERISTICA\_FORN

Não

Sim

A

200

Local do fornecimento a ser identificado no Dfe

LOCAL\_FORN\_DFE

Não

Sim

A

200

Detalhes

DETALHES

Não

Não

A

800

Tabela: COD\_IND\_OPERACAO\_CONSUMO

A carga inicial desta tabela foi realizada a partir do arquivo liberado no portal de Nfse \(AnexoVII\-IndOp\_IBSCBS\_V1\.00\.00, publicado em 22/07/25\)\.

Críticas:

__Código indOP __\(campo chave\)à Campo obrigatório

__At\.11 __à Campo obrigatório

__Tipo de operação__ à Campo obrigatório

__Considera\-se local da operação__ à Campo obrigatório

__Característica do fornecimento__ à Campo obrigatório

__Local do fornecimento a ser identificado no Dfe __à campo obrigatório

MFS\-890705

__RN\-TFIX/TACES__

__REGRAS TÉCNICAS PARA MANUTENÇÃO DA FUNCIONALIDADE DE IMPORTAÇÃO AUTOMATIZADA DE TFIX/TACES__

Processo desenvolvido na linguagem JAVA, utilizando um arquivo xml com a estrutura das tabelas fixas:

__ARQUIVOS UTILIZADOS NO PROCESSO__

- imptfix\.properties
- ImportaTfix\.bat
- ImportaTfix\.jar
- tfixes\.xml

__imptfix\.properties:__ Arquivo para definição do número de threads\. 

Ex\.: nm\.threads = 8

__ImportaTfix\.bat:__ Arquivo que contém as informações de acesso ao banco de dados para atualização das tabelas fixas\. Este arquivo é utilizado no processamento da importação através do módulo ferramentas\. Todos os parâmetros são recuperados internamente através de: Dados do usuário logado na aplicação \+ Diretório informado na tela de importação de TFIX no Ferramentas\.

Em caso de estouro de memória em processamento de importação de alguma tabela fixa, pode haver a necessidade de ajustar os parâmetros de memória para a JVM \(\-Xms e \-Xmx\), no arquivo “ImportaTfix\.bat”, localizado junto com os executáveis, porém esse ajuste pode ocasionar baixa performance no processamento\. 

Ex\.: java \-XmsAAAM \-XmxAAAAM \-jar ImportaTfix\.jar %1 %2 %3 %4 %5

Xms \-> Alocação de memória inicial \(AAA\)\.

Xmx \-> Alocação máxima de memória \(AAAA\)\.

	%1 \-> Database

%2 \-> Username

%3 \-> Password

%4 \-> Código da Empresa

%5 \-> Diretório onde se encontram as tabelas fixas para importação\.

__ImportaTfix\.jar:__ Arquivo Java que contém as regras de importação das tabelas fixas, atendendo ao processo praticamente da mesma forma como é executado em PB\.

__tfixes\.xml:__ <a id="_Hlk89090537"></a>Arquivo que contém a estrutura de cada tabela fixa e de quase todas as tabelas acessórias atendendo ao layout dos registros montado nos arquivos: TFIXAAA\.TXT \(AAA: Número TFIX\) e TACESAAA\.TXT \(AAA: Número TACES\)\. O recomendado é, quando da criação de uma tabela fixa ou Acessória, cria\-la no banco de dados com o mesmo layout utilizado na montagem dos arquivos TXT\. Divergências nos layouts podem ocasionar erros na importação ou importar informações em campos trocados\. Observar que para algumas tabelas, na base de dados, existem mais campos que o definido no arquivo de importação para a tabela\. Em alguns casos esses campos são alimentados via tela\.

Ex\.: 

<?xml version="1\.0" encoding="ISO\-8859\-1" ?>

<a id="_Hlk533000740"></a><tabelas>

<tabela>

	<nome\_tabela>TFIX02</nome\_tabela>

	<nome\_tabela\_banco>TRIBUTO</nome\_tabela\_banco>

	<colunas>

		<coluna nome='cod\_tributo' tipo='VARCHAR2' ind\_chave='TRUE' />

		<coluna nome='descricao' tipo='VARCHAR2' ind\_chave='FALSE'/>

		<coluna nome='titulo' tipo='VARCHAR2' ind\_chave='FALSE'/>

	</colunas>

</tabela>

</tabelas>

__ATENÇÃO:__ Este arquivo deverá ser atualizado todas as vezes em que houver:

Criação ou exclusão de uma tabela fixa ou acessória;

Houver mudanças na estrutura da tabela fixa ou acessória, tais como:

Inclusão de novos campos;

Alteração de nome do campo;

Alteração de tipo de campo;

Alteração de tamanho de campos\. Ver se a tabela no arquivo tem algum controle de tamanho da coluna\.

Alteração de tamanho de campos com precisão;

Alteração de campos chaves da tabela no banco de dados;

Criação ou alteração de FK;

Criação ou alteração de campo IDENT\.

__Obs\.:__ Cuidado ao copiar os registros das tabelas fixas para o excel em caso de ordenamento ou ajustes, pois os campos alfanuméricos com zeros na frente devem retornar para o arquivo TXT da mesma forma\. Ex\.: TFIX30 – COD\_MODULO\. Ao mudarem a tabela no excel e ordenar, retiraram os zeros da frente dos módulos de 1 a 99, gerando erros na importação\.

As tabelas acessórias abaixo continuam no processo padrão, via ferramentas, e não foram incluídas no arquivo tfixes\.xml devido a regras específicas que impossibilitam o processo automatizado:

- TACES03 \- Situação Tributária Estadual \- A
- TACES04 \- Situação Tributária Estadual \- B
- TACES07 \- Nacionalidades
- TACES11 \- Observações de Livros Fiscais
- TACES12 \- CEP__ \[MFS\-624154__\] Inclusão da TACES12 na lista de tabela
- TACES14 \- Códigos da Receita __\[MFS\-627307__\] Inclusão da TACES14 na lista de tabela
- TACES31 \- Cadastro de CBC Moedas \(SPED\)
- TACES32 \- Cadastro da Consolidação de Normas Cambiais \(CNC\)
- TACES33 \- Cadastro de CBC País Acordo Jurisdição
- TACES55 \- Grupo Produtos do DACON
- TACES56 \- Produtos do DACON
- TACES57 \- Produtos SERC
- TACES66 \- Tabela de Categoria de Trabalhador \(eSocial\)
- TACES70 \- Cadastro de Tipo de Documento DEREX __\[MFS61949\- MFS\-73138\]__ A TACES70 é importada automaticamente
- TACES71 \- Parametrização dos Tipos de Crédito __\[MFS61949\]__ A TACES71 não é importada automaticamente
- TACES73 \- Parametrização dos Códigos de Contribuição
- TACES92 \- Tipo de Cliente
- TACES93 \- Subclasse de Consumo
- TACES98 – Cadastro de Código de Instalação de Obrigações \[__MFS\-73138__\] Inclusão da TACES98 da lista de tabelas 
- TACES99 \- Catálogo de Empresas para OLSS  __\[MFS43745\-__ __MFS\-73138\]__ Retirada da TACES99 da lista de tabelas a serem importadas
- TACES100 \- Observações por UF/Situação Especial ST

__TRATAMENTO ESPECIAL__

__TFIX50\.TXT \- Categoria x Tabelas de Processamento__

Este arquivo atualiza 3 tabelas no banco de dados:

- TAB\_PROC, 
- CATEGORIA, 
- CATEG\_TAB\_PROC

Para o processamento, via xml, foi montada uma estrutura em Java, onde o nome fictício da tabela passou a ser “CAD\_TAB\_PROC”\.

__ESTRUTURA DE MONTAGEM DO ARQUIVO TFIXES\.XML__

__ESTRUTURA PRINCIPAL__

__<tabelas> e </tabelas>:__ Tag de abertura e encerramento da estrutura principal;

<__tabela> e </tabela>:__ Tag de abertura e encerramento da estrutura de cada tabela fixa;

__<nome\_tabela> e </nome\_tabela>:__ Tag com a informação do nome do arquivo TFIX ou TACES;

__<nome\_tabela\_banco> e </nome\_tabela\_banco>:__ Tag com a informação do nome da tabela no banco correspondente a TFIX ou TACES;

__<reimportar> e </reimportar>:__ Tag com a informação de reprocessar a importação para a tabela devido ao processo de thread gerar problemas no insert da tabela\. Valores válidos: TRUE e FALSE;

__colunas> e </colunas>:__ Tag de abertura e encerramento para as colunas existentes no arquivo TFIX ou TACES;

__<coluna nome=:__ Tag que recebe o nome do campo da tabela no banco de dados;

__tipo=:__ Tag com a informação do tipo de campo no banco de dados \(CHAR, VARCHAR2, NUMBER, DATE\);

__tamanho=:__ Tag utilizada para definir tamanho de campos, principalmente em campos numéricos com precisão\. Para campos alfanuméricos, esta orientação é opcional, uma vez que o recomendado é preencher o campo na tabela fixa \(TFIX\.TXT\) ou tabela acessória \(TACES\.TXT\) com o tamanho definido no banco de dados\. Arquivos com informações que estourem o tamanho do campo irão gerar erros na importação\. Aconselhamos acertar o erro no arquivo TFIX\.TXT ou TACES\.TXT em vez de truncá\-lo incluindo esta opção\.

__precisao=:__ Tag para informar, para campos numéricos, o número de casas decimais definidas para o campo no banco de dados;

__ind\_chave=:__ Tag com a orientação para campo chave no banco de dados\. Valores válidos: TRUE e FALSE;

__existe\_so\_no\_txt=:__ Tag que trata a condição de um campo existir no arquivo TXT, mas não existir no banco de dados\. Valores válidos: TRUE e FALSE\. Ex\.: campo COD\_ESTADO que no arquivo TXT traz a UF e no banco de dados se recupera o IDENT\_ESTADO, para esta condição o valor válido é ‘TRUE’\.

__ind\_ident=:__ Tag que trata a condição do campo informado na “<coluna nome” ser um campo IDENT recuperado a partir de um campo do TXT e existente apenas no banco de dados\. Valores válidos: TRUE e FALSE\. Para esta condição o valor válido é ‘TRUE’; 

__existe\_so\_no\_banco=:__ Tag que trata a condição de um campo existir no banco de dados, mas não existir no TXT\. Valores válidos: TRUE e FALSE\. Ex\.: campo IDENT\_ESTADO que é recuperado no banco de dados através da UF existente no arquivo TXT, para esta condição o valor válido é ‘TRUE’\.

__ind\_trim=:__ Tag que informa sobre a retirada de espaços no campo\. Valores válidos: TRUE e FALSE\. Existem campos que a informação no banco de dados deve conter branco \(‘ ‘\), para esta condição, o valor a informar é ‘FALSE’\.

__nome\_sequence=:__ Tag utilizada para campos que utilizam sequence na geração da sequência para o identificador no banco de dados\. Ex\.: tabela TFIX131 – WCA\_REGRA \- <coluna nome='id\_regra' nome\_sequence="seq\_wca\_regra"

__VALIDAÇÕES__

__<validacoes> e </validacoes>:__ Tags de abertura e encerramento para as condições de: 

Recuperação de IDENT; 

Identificadores sequenciais \(sequence\);

Validações de campos com FK\.

__Para recuperar uma informação de um campo em outra tabela \(IDENT\)__

__<recuperar coluna=:__ Tag que recebe o número correspondente a coluna a ser utilizado para a recuperação de um campo\. A numeração das colunas distribuídas verticalmente, conforme estrutura do layout segue o padrão: 0, 1, 2 \.\.\.7\. Podemos ter mais de uma coluna a recuperar, neste caso, informar as colunas correspondentes\. Ex\.: “0,1”;

__tabela=:__ Tag que recebe o nome da tabela em que será realizada a recuperação do campo informado;

__campo\_recuperar=:__ Tag que recebe o nome do campo a recuperar a partir da tabela informada\. Podemos ter mais de uma “coluna” a recuperar, neste caso, informar as colunas correspondentes\. Ex\.: “campo 0,campo 1”;

__campo\_ref=:__ Tag que recebe o nome do campo de referência existente no arquivo TXT para recuperação de um campo existente na base de dados;

__coluna\_ref=:__ Tag que recebe o número correspondente a coluna a ser utilizada come referência para a recuperação de um campo\. A numeração das colunas distribuídas verticalmente, conforme estrutura do layout segue o padrão: 0, 1, 2 \.\.\.7 Podemos ter mais de uma coluna a recuperar, neste caso, informar as colunas correspondentes\. Ex\.: “0,1”;

__cod\_erro=:__ Tag que recebe o número do código de erro cadastrado na tabela TFIX22 \(CAT\_ERRO\) para o critério utilizado na recuperação do campo\.

__Para validar a informação de um campo em outra tabela \(FK\)__

__<validar coluna=:__ Tag que recebe o número correspondente a coluna a ser utilizado para a validação de um campo\. A numeração das colunas distribuídas verticalmente, conforme estrutura do layout segue o padrão: 0, 1, 2 \.\.\.7\. Podemos ter mais de uma coluna a validar, neste caso, informar as colunas correspondentes\. Ex\.: “0,1”;

__tabela=:__ Tag que recebe o nome da tabela em que será realizada a validação do campo informado;

__campo\_tabela=:__ Tag que recebe o nome do campo de referência existente no arquivo TXT para validação de um campo existente na base de dados \(FK\)\. Podemos ter mais de uma “coluna” a validar, neste caso, informar as colunas correspondentes\. Ex\.: “campo 0,campo 1”;

__cod\_erro=:__ Tag que recebe o número do código de erro cadastrado na tabela TFIX22 \(CAT\_ERRO\) para o critério utilizado na validação do campo\.

__\.\.\. />:__ Comando de fechamento das tags “<coluna nome=”, “<recuperar” e “<validar”\.

__LOCALIZAÇÃO DOS ARQUIVOS__

- ImportaTfix\.bat \- CVS\\MsafDW\\java\\Entregaveis
- ImportaTfix\.jar
- imptfix\.properties \- CVS\\Sistemas\_Internos\\ImportaTFIX\\Atualizacao
- tfixes\.xml \- CVS\\MsafDW\\conteudo\\Conteudo\\TXT

__ARQUIVOS ATUALIZADOS__

__CVS__

CVS\\MsafDW\\conteudo\\Conteudo\\TXT > tfixes\.xml

__ATENÇÃO: O arquivo “tfixes\.xml” válido é o existente na pasta acima\. Não utilize o da pasta CVS\\Sistemas\_Internos\\ImportaTFIX\\Atualizacao, pois este era um arquivo de testes\.__

Os arquivos fontes dos programas estão na estrutura do CVS de Sistemas\_Internos \(Mesmo nível do MsafDW\)\.

\\Sistemas\_Internos\\ImportaTFIX

O processo de geração é realizado nesta pasta\. Ao final, os arquivos gerados devem ser copiados para as pastas abaixo:

CVS\\MsafDW\\java\\Entregaveis\\ImportaTfix\.bat \(se houver mudanças\)

CVS\\MsafDW\\java\\Entregaveis\\ImportaTfix\.jar

__PACOTE PATCH__

CVS\\MsafDW\\java\\Entregaveis\\ImportaTfix\.bat \-> Copiar esse arquivo para o diretório "Executáveis"

CVS\\MsafDW\\java\\Entregaveis\\ImportaTfix\.jar \-> Copiar esse arquivo para o diretório "Executáveis"

CVS\\MsafDW\\java\\Entregaveis\\Imptfix\.properties \-> Copiar esse arquivo para o diretório "Executáveis"

CVS\\MsafDW\\conteudo\\Conteudo\\TXT\\tfixes\.xml \-> Copiar esse arquivo para o diretório "Executáveis"

CVS\\MsafDW\\conteudo\\Conteudo\\TXT\\tfixes\.xml para o diretório "Atualizacao"

CVS\\MsafDW\\java\\Entregaveis\\Imptfix\.properties para o diretório "Atualizacao"

__PACOTE ACUMULATIVO__

CVS\\MsafDW\\java\\Entregaveis\\ImportaTfix\.bat \-> Copiar esse arquivo para o diretório "Executaveis"

CVS\\MsafDW\\java\\Entregaveis\\ImportaTfix\.jar \-> Copiar esse arquivo para o diretório "Executaveis"

CVS\\MsafDW\\java\\Entregaveis\\Imptfix\.properties \-> Copiar esse arquivo para o diretório "Executaveis"

CVS\\MsafDW\\conteudo\\Conteudo\\TXT\\tfixes\.xml \-> Copiar esse arquivo para o diretório "Executaveis"

CVS\\MsafDW\\conteudo\\Conteudo\\TXT\\tfixes\.xml para o diretório "Atualizacao"

CVS\\MsafDW\\java\\Entregaveis\\Imptfix\.properties para o diretório "Atualizacao"

__SITUAÇÕES DE ERROS__

1\. Para executar a importação das tabelas fixas, caso os executáveis do Mastersaf DW estejam na rede, o diretório deverá estar mapeado para um driver local\.

2\. Em caso de estouro de memória em processamento de importação de alguma tabela fixa, pode haver a necessidade de ajustar os parâmetros de memória para a JVM \(\-Xms e \-Xmx\), no arquivo “ImportaTfix\.bat”, localizado junto com os executáveis, porém esse ajuste pode ocasionar baixa performance no processamento\. Exemplo:

		java \-XmsAAAM \-XmxAAAAM \-jar ImportaTfix\.jar %1 %2 %3 %4 %5

		Xms \-> Alocação de memória inicial \(AAA\)\.

		Xmx \-> Alocação máxima de memória \(AAAA\)\.

1. Para o erro apresentado na tela a seguir ao executar a importação no Ferramentas, verifique se os arquivos se encontram nas pastas executaveis e/ou atualização:

![](data:image/png;base64,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)

