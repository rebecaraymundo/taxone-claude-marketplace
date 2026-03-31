# T1_RT - NFCom Requisitos de negocios_v1

- **Fonte:** T1_RT - NFCom Requisitos de negocios_v1.docx
- **Modificado:** 2025-07-02
- **Tamanho:** 266 KB

---

<a id="_Toc485386230"></a><a id="_Toc485386520"></a><a id="_Toc503342450"></a><a id="_Toc509770174"></a><a id="_Toc513523690"></a>Projeto Reforma Tributária | Tax One

__Criado por:__

Érika Borges

__Data __

15/05/2025

__Produto: Automation__

__ ADO__

__768949__

__Framework | Estadual > Gia SP > Geração dos Registros__

__Histórico de revisão__

__Data da Revisão__

__Responsável pela atualização__

__Descrição da atualização__

15/05/2025

Erika Borges

Adequações NFCOM v1\.4

18/06/2025

Érika Borges

Adequações NFCOM v1\.5 e CTE v1\.5

30/06/2025

Érika Borges

Criação das tabelas SAFX3042 e SAFX3043 para os processos da NFCOM \- Saídas\.

Sumário

[1\.	Introdução	3](#_Toc202175056)

[2\.	Requisitos de negócios – RT & NFCOM	4](#_Toc202175057)

[2\.1\.	NFSC\-e & NFCom	4](#_Toc202175058)

[2\.1\.1\.	Nota Fiscal Fatura de Serviço de Comunicação eletrônica	4](#_Toc202175059)

[2\.1\.2\.	Nota Fiscal Fatura de Serviço de Comunicação eletrônica	5](#_Toc202175060)

[__2\.1\.3\.__	__NFCOM | Layout SAFX__	6](#_Toc202175061)

[3\.	Regras de negócios \- RT|NFCOM	8](#_Toc202175062)

[__3\.1\. RT|NFCOM – Alterações Técnicas__	8](#_Toc202175063)

[__3\.1\.1\. Inclusão de Squema para IBS/CBS\[Nova SAFX\]__	8](#_Toc202175064)

[3\.1\.2\. Grupo de Impostos IBS/CBS  \[Conciliação\]	8](#_Toc202175065)

[3\.1\.3\. Grupo de informações da Tributação Regular	8](#_Toc202175066)

[3\.1\.4\.	Grupo de totais da NFCom \[Conciliação\]	8](#_Toc202175067)

[__3\.1\.5\.__	__Código de Classificação Tributária do IBS e da CBS \[TACES\]__	8](#_Toc202175068)

[3\.1\.6\.	Grupo de__ Compras Governamentais \[Conciliação\]__	9](#_Toc202175069)

[3\.1\.7\.	Nova Regra de Validação Cofaturamento \[Conciliação\]	9](#_Toc202175070)

[3\.1\.8\.	CNPJ Alfanumérico \[Estadual\]	9](#_Toc202175071)

[4\.	Premissas	10](#_Toc202175072)

[5\.	Conceitos	11](#_Toc202175073)

[6\.	Referências RT & NFcom	12](#_Toc202175074)

[__6\.1\.__	__NFCom \- Referências__	12](#_Toc202175075)

[__61\.1\.__	__NFCom  – Obrigatoriedade de emissão da NFCom__	12](#_Toc202175076)

[__61\.2\.__	__NFCom – Alteração SAFX e tabelas Internas__	12](#_Toc202175077)

[__61\.3\.__	__RT – Mudanças na RT para NFCom__	12](#_Toc202175078)

[7\.	Proposta de solução \- NFCom & CTE	13](#_Toc202175079)

[__7\.1\.__	__NFCom – Modelo 62 | RT – SAFX3042__	13](#_Toc202175080)

[__7\.1\.1\.__	__NFCom  | Total DFE__	13](#_Toc202175081)

[__7\.1\.2\.__	__NFCom  | Grupo de Totais__	13](#_Toc202175082)

[__7\.1\.3\.__	__NFCom | Compras Governamentais__	14](#_Toc202175083)

[__7\.2\.__	__NFCom – Modelo 62 | RT – SAFX3043__	15](#_Toc202175084)

[__7\.3\.__	__NFCom – Modelo 62 | RT – SAFX3007__	18](#_Toc202175085)

[__7\.3\.1\.__	__NFCom  | Total DFE__	18](#_Toc202175086)

[__7\.3\.2\.__	__NFCom  | Grupo de Totais__	18](#_Toc202175087)

[__7\.3\.3\.__	__NFCom | Compras Governamentais__	18](#_Toc202175088)

[__7\.4\.__	__NFCom – Modelo 62 | RT – SAFX3008__	20](#_Toc202175089)

[8\.	Termo de Aceite – Aprovação	23](#_Toc202175090)

1. <a id="_Toc202175056"></a>__Introdução__

Este documento de requisitos de negócios tem por objetivo descrever as necessidades e proposta de solução para o __DEMANDA REFORMA TRIBUTÁRIA – NFCOM – Modelo 62__\.

O __ONESOURCE Tax One __é um software tributário integrado acessível, seguro e confiável que une o melhor da tecnologia com os melhores padrões de segurança da Thomson Reuters para garantir compliance fiscal às empresas\. Com o aumento da complexidade da legislação tributária brasileira, empresas precisam cada vez mais de soluções eficazes na gestão do departamento tributário\.

No contexto da Reforma tributária, o repositório de dados fiscais do Tax One terá sua estrutura atualizada para suportar os novos impostos com base na versão da publicação na presente data\. Nesse documento abordaremos a proposta de solução para os processos fiscais da __Nota Fiscal Fatura de Serviço de Comunicação Eletrônica __suportados pela estrutura de arquivos __SAFX08 – Itens de mercadorias para nota fiscal de entrada – Modelo 62 __ e __SAFX43 \- Itens de Documentos Fiscais de Utilities – Modelo 62__, com base na versão NFCom\_Nota\_Tecnica\_2025\_001\_RTC\_v1\.02 da NFCom\. 

 

1. <a id="_Toc202175057"></a>__Requisitos de negócios – RT & NFCOM__

## <a id="_Toc202175058"></a>NFSC\-e & NFCom

### <a id="_Toc202175059"></a>Nota Fiscal Fatura de Serviço de Comunicação eletrônica 

A Nota Fiscal de Serviço de Comunicação modelo 21 e a Nota Fiscal de Serviço de Telecomunicação modelo 22 são documentos fiscais utilizados para registrar a prestação de serviços de comunicação e telecomunicação, respetivamente\. São emitidos pelas empresas que prestam esses serviços e servem para comprovar a realização da prestação e a cobrança dos impostos aplicáveis\. 

- __Modelo 21:__Destina\-se à prestação de serviços de comunicação, como telefonia fixa e móvel, TV por assinatura, internet, rádio, entre outros\. 
- __Modelo 22:__Destina\-se à prestação de serviços de telecomunicação, abrangendo telefonia fixa e móvel, VoIP, entre outros\. 

__Caracterização:__ São notas fiscais sem a necessidade de DANFE \(Documento Auxiliar da Nota Fiscal Eletrônica\), ou seja, não possuem uma versão impressa para o cliente\. A emissão e transmissão da nota fiscal são feitas de forma eletrónica, através de arquivos TXT\. 

- __Utilização: __São emitidas pelas empresas prestadoras de serviços e destinadas aos consumidores, que podem consultar a nota fiscal em meio eletrônico\. 
- __Principais diferenças em relação a outras notas fiscais:__
	- Não requer certificado digital para emissão\.
	- Não há necessidade de geração de XML\. 
	- A transmissão para a SEFAZ \(Secretaria Estadual de Fazenda\) é feita através de arquivos TXT\. 
	- Não existe DANFE para impressão\. 

Lista de CNAE – Utilities

__Código__

__Descrição__

 6010\-1 

Atividades de rádio

 6021\-7 

Atividades de televisão aberta

6022\-5

Programadoras e atividades relacionadas à TV por assinatura

6110\-8

Telecomunicações por fio

6120\-5

Telecomunicações sem fio

6130\-2

Telecomunicações por satélite

6141\-8

Operadoras de televisão por assinatura por cabo

6142\-6

Operadoras de televisão por assinatura por micro ondas

6143\-4

Operadoras de televisão por assinatura por satélite

6190\-6

Outras atividades de telecomunicações

6319\-4

Portais, provedores de conteúdo e outros serviços de informação na internet

### <a id="_Toc202175060"></a>Nota Fiscal Fatura de Serviço de Comunicação eletrônica 

A __NFCom__, ou __Nota Fiscal Fatura de Serviço de Comunicação Eletrônica__ – __modelo 62,__ é um documento emitido e armazenado eletronicamente, com existência exclusivamente digital, cuja validade jurídica é garantida pela assinatura digital do emitente e pela autorização de uso pela administração tributária da unidade federada do contribuinte\. Ela simplifica as obrigações acessórias dos contribuintes, permitindo ao Fisco acompanhar a emissão em tempo real\.

O principal objetivo da __NFCom__ é substituir: 

- Nota Fiscal de Serviço de Comunicação – modelo 21, 
- Nota Fiscal de Serviço de Telecomunicações – modelo 22\. 

Todos os Estados e o Distrito Federal adotaram a __NFCom__, ficando a critério de cada unidade federativa – UF determinar sua obrigatoriedade\.

Lista de CFOps válidos para emissão da NFCom

Código

Descrição

         1\.205 

__Anulação __de valor relativo à prestação de serviço de comunicação

         5\.301 

Prestação de serviço de comunicação para __execução de serviço da mesma natureza__

         5\.302 

Prestação de serviço de comunicação a __estabelecimento industrial__

         5\.303 

Prestação de serviço de comunicação a __estabelecimento comercial__

         5\.304 

Prestação de serviço de comunicação a estabelecimento de prestador de __serviço de transporte__

         5\.305 

Prestação de serviço de comunicação a estabelecimento de geradora de distribuidora de __energia elétrica__

         5\.306 

Prestação de serviço de comunicação a estabelecimento de __produtor rural__

         5\.307 

Prestação de serviço de comunicação a __não contribuinte__

         5\.933 

Prestação de serviço __tributado pelo ISSQN__

         6\.301 

Prestação de serviço de comunicação para __execução de serviço da mesma natureza__

         6\.302 

Prestação de serviço de comunicação a __estabelecimento industrial__

         6\.303 

Prestação de serviço de comunicação a __estabelecimento comercial__

         6\.304 

Prestação de serviço de comunicação a estabelecimento de prestador de __serviço de transporte__

         6\.305 

Prestação de serviço de comunicação a estabelecimento de geradora de distribuidora de __energia elétrica__

         6\.306 

Prestação de serviço de comunicação a estabelecimento de __produtor rural__

         6\.307 

Prestação de serviço de comunicação a __não contribuinte__

         7\.301 

Prestação de serviço de comunicação para __execução de serviço da mesma natureza__

Estão previstos no MOC os seguintes eventos para a NFCom:

__110111 __–__ Cancelamento__: a empresa emitente da NFCom é responsável por registrar o evento\. O prazo para o cancelamento é de até 120 \(cento e vinte\) horas após o último dia do mês da sua autorização, devendo atender às demais particularidades especificadas na cláusula décima quinta do [Ajuste SINIEF 7/2022](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2022/AJ007_22)\. 

__240140 __– __Autorizada NFCom de Substituição__: registra que a NFCom foi referenciada por uma outra com a finalidade substituição\. O Fisco é responsável por registrar esse evento\. 

__240150 __– __Autorizada NFCom de Ajuste__: registra que a NFCom foi referenciada por uma outra com a finalidade ajuste\. O Fisco é responsável por registrar esse evento\. 

__240151 __– __Cancelada NFCom de Ajuste__: registra no documento que recebeu o registro do evento 240150, o cancelamento da NFCom de finalidade ajuste\. O Fisco é responsável por registrar esse evento\. 

__240160 __– __Autorizada NFCom de Cofaturamento__: registra que a NFCom foi referenciada por outra com o tipo de faturamento cofaturamento\. O Fisco é responsável por registrar esse evento\. 

__240161 __– __Cancelada NFCom de Cofaturamento__: registra no documento que recebeu o registro do evento 240160, o cancelamento da NFCom de tipo de faturamento cofaturamento\. O Fisco é responsável por registrar esse evento\. 

__240162 __– __Substituída NFCom de Cofaturamento__: registra no documento que recebeu o registro do evento 240160, que este foi referenciado por uma NFCom de substituição, cujo tipo de faturamento é cofaturamento\. O Fisco é responsável por registrar esse evento\. 

__240170 __– __Liberação Prazo Cancelamento__: registra no documento que o mesmo recebeu liberação para cancelamento maior que o prazo determinado\. O Fisco é responsável por registrar esse evento\. 

- 
	- 
		1. <a id="_Toc202175061"></a>__NFCOM | Layout SAFX__

Os processos SAFX da NFCom que processam informações dos impostos que serão substituídos pela CBS e IBS\. 

A partir de um documento emitido após a implantação da Reforma tributária, os tributos populados nos campos de impostos dessas tabelas passam a ser desconsiderados e novos campos de impostos passam a ser populados\. 

O tratamento dos impostos IBS e CBS nesses processos precisam compreender características dos controles estipulados pela RT, tais como: diferentes alíquotas, tributação regular \(ZFM e ALC\), compras governamentais e cofaturamento\. 

Lista de impostos x Processos SAFX

PIS/COFINS

ISS

ICMS

SAFX04

SAFX04

SAFX04

SAFX42

SAFX42

SAFX42

SAFX43

SAFX43

SAFX43

SAFX332

 

SAFX332

SAFX334

SAFX333

SAFX333

SAFX431

SAFX431

SAFX431

 

SAFX432

 

Obs\.: Nessa versão da RT – NFCom, apenas PIS, COFINS e ICMS\. 

Os processos SAFX suportarão a implementação da NFCom prevista para 11/2025 e RT em 01/2026 e a entrega dos SPED Fiscal e SPED Contribuições em período de transição para o RT\. 

Arquivos SAFX para integração das __Nota Fiscal Fatura de Serviço de Comunicação eletrônica__\.

 

NOME

LEGISLAÇÃO

OBJETIVO

SAFX42

Capa de Documentos Fiscais de Utilities

IN 68 \- Arquivos 3\.8 – Telecomunicações

Módulo: BÁSICOS > DATAWAREHOUSE > Manutenção > Documento Fiscal > Novo Documento Fiscal > Documento Fiscal Utilities /Aba: "Capa"

SAFX43

Itens de Documentos Fiscais de Utilities

IN 68 \- Arquivos 3\.9

Módulo: BÁSICOS > DATAWAREHOUSE > Manutenção > Documento Fiscal > Novo Documento Fiscal > Documento Fiscal Utilities /Aba: "Itens"

SAFX254

Term\. Telefônicos dos Planos de Prestações de Serviços Telefônicos Corporativos, Familiares ou Similares

Atendimento NFCom

O objetivo desta tabela é adequar as informações para atendimento à NFCom , referente às informações de Entrada\.  
Essa tabela tem vinculação com a SAFX07 \(Capa do Documento Fiscal\)\.

SAFX331

Informação de Programa de Fidelidade e Fatura da Nota fiscal Eletrônica

Atendimento NFCom

O objetivo desta tabela é adequar as informações para atendimento à NFCom , referente às informações de Entrada\.  
Essa tabela tem vinculação com a SAFX07 \(Capa do Documento Fiscal\)\.

SAFX332

Informações de Processos em Nota Fiscal Eletrônica \- Valores alterados e Processos de Ressarcimento 

Atendimento NFCom

"O objetivo desta tabela é adequar as informações para atendimento à NFCom , referente às informações de Entrada\.

SAFX333

Informações de Partilha com UF Destinatária em Nota Fiscal Eletrônica

Atendimento NFCom

"O objetivo desta tabela é adequar as informações para atendimento à NFCom , referente às informações de Entrada\.

SAFX334

Infomações de Fundos de Desenvolvimento e Retenções de Tributos Federais em Nota Fiscal Eletrônica

Atendimento NFCom

"O objetivo desta tabela é adequar as informações para atendimento à NFCom , referente às informações de Entrada\.

SAFX431 e SAFX432

Itens Negativos de Documentos Fiscais de Utilities

Convênio ICMS 115

Convênio ICMS 60/2015

 Esta tabela é utilizada para a carga dos itens negativos do documento fiscal \(Utilities\), com todas as informações necessárias para a geração do Convênio ICMS 115\. Além dos itens negativos, deverão ser carregados também, quando for o caso, os itens normais \(não negativos\) que foram consolidados a outros itens da nota original\. As informações desta tabela serão utilizadas apenas para o Convênio ICMS 115, com objetivo de gerar os itens exatamente no mesmo formato do documento original, com seus itens negativos, quando for o caso\. Esta tabela deve ser utilizada somente nos casos em que a carga dos dados para a SAFX43 for realizada já com os valores dos itens consolidados deduzidos ou somados, conforme o caso, aos itens principais da nota\. Além disso, é necessário o preenchimento do campo “N\. Item Real” da SAFX43\. Para notas que não possuem itens com valores negativos e os dados tenham sido importados para a SAFX43 com todos os itens da nota original, não é necessário utilizar esta tabela\. A partir da vigência do Convênio ICMS 60/2015 esta tabela passou a ser considerada como padrão para geração do meio magnético do Convênio 115, pois esta legislação passou a tratar a demonstração das informações de desconto como item negativo demonstrado no meio magnético\. 

Arquivos SAFX de cadastros que envolvem a movimentação da NFCom

 

NOME

LEGISLAÇÃO

OBJETIVO

SAFX04

Arquivo de Cadastro de Pessoas Físicas/Jurídicas

IN 68/95 \- Arquivo 8\.1  
IN 86/01 \- Arquivo 4\.9\.1  
IN 89/03 \- Arquivo 4\.9\.2

Módulo: BÁSICOS > DATAWAREHOUSE > Manutenção > Cadastros > Pessoas Físicas/Jurídicas

1. <a id="_Toc202175062"></a>__Regras de negócios \- RT|NFCOM__

<a id="_Toc202175063"></a>__3\.1\. RT|NFCOM – Alterações Técnicas __

A Nota Técnica Reforma Tributária NFCom 2025\.001 tem como propósito implementar as mudanças necessárias nos layouts da __Nota Fiscal Fatura de Serviço de Comunicação Eletrônica__, __modelo 62,__ adequando\-os aos novos tributos: __IBS__ e __CBS__\.

__Principais mudanças__

<a id="_Toc202175064"></a>__3\.1\.1\. Inclusão de Squema para IBS/CBS\[Nova SAFX\]__

Incluso no pacote de schemas de cada documento fiscal eletrônico o arquivo __*DFeTiposBasicos\_v1\.00\.xsd*__\.

Esse arquivo define, de forma estruturada, os campos obrigatórios para registrar as informações relacionadas à tributação do IBS \(Imposto sobre Bens e Serviços\) e da CBS \(Contribuição sobre Bens e Serviços\), na Nota Fiscal Fatura de Serviço de Comunicação Eletrônica — padrão que também será aplicado aos demais documentos fiscais eletrônicos\.

Obs\.: Esquema disponível na seção 3, página 5 da NFCom\_Nota\_Tecnica\_2025\_001\_RTC\_v1\.02\. 

### <a id="_Toc202175065"></a>3\.1\.2\. Grupo de Impostos IBS/CBS  \[Conciliação\]

O grupo será utilizado para envio das informações do Imposto de Bens e Serviços – IBS, Contribuição de Bens e Serviços – CBS e deve ser adicionado ao final do grupo imposto \(em cada item do grupo det/imposto/IBSCBS\)\.

Neste grupo são informados, o __CST, o cClassTrib e a base de cálculo serão idênticas e por item da nota fiscal\.__ Com isso, foi criado o __Grupo de informações específicas do IBS/CBS\.__

Para o__ IBS__, como as alíquotas podem variar entre Estados e Municípios, dentro do grupo de informações do IBS/CBS de competência das Unidades Federadas foram criados dois campos distintos:

- __IBSUF__: informações referentes à alíquota estadual, e 
- __IBSMun__: informações referentes à alíquota municipal\. Ambos os subgrupos incluem, além da alíquota, campos para detalhar diferimento, devolução de tributos e redução de alíquota\.

Para a __CBS__, foi implementado o __Grupo de Informações da CBS__ contendo um subgrupo específico com os mesmos tipos de informações, regulamentadas pela União: alíquota, diferimento, devolução de tributos e redução de alíquota\.

### <a id="_Toc202175066"></a>3\.1\.3\. Grupo de informações da Tributação Regular 

Também foi implementado o __Grupo de informações da Tributação Regular__ que traz campos adicionais para o envio de dados relacionados à tributação regular \(ZFM e ALC\) para detalhar saldos de crédito presumido informando como seria a tributação caso não cumprida a condição resolutória/suspensiva\. 

### <a id="_Toc202175067"></a>Grupo de totais da NFCom \[Conciliação\]

Por fim, foi adicionado ao __grupo de totais da NFCom__, um grupo de__ totalização do IBS/CBS__ em relação ao declarado nos itens que conta com subgrupos para cada tributo e deve ser preenchido com o somatório dos valores correspondentes aos itens da nota\.

__Importante__: como o IBS e a CBS são tributos “por fora”, seus valores devem ser adicionados ao valor total da NFCom\. e junto a esse grupo deverá ser criada a tag Valor Total do DFe, onde o total geral do DFe deverá ser a soma do valor total da NFCom = vNF \+ vTotIBS \+ vTotCBS com a seguinte exceção:__* Em 2026 não somar vTotIBS e vTotCBS*__\.

Junto a esse grupo e campos, __novas regras de validação foram implementadas ao grupo de totais IBS e CBS__\. Essas validações exigem que a soma dos valores nos totalizadores corresponda exatamente à soma dos valores dos itens\.

- 
	- 
		1. <a id="_Toc202175068"></a>__Código de Classificação Tributária do IBS e da CBS \[TACES\]__

As informações dos tributos __IBS e CBS__ associadas aos itens dos documentos fiscais eletrônicos deverão ser classificadas com base no __Código de Situação Tributária – *CST*__ e no __Código de Classificação Tributária – *cClassTrib*__\.

A tabela contento os códigos foi publicada por meio do Informe Técnico RT 2024\.001 e está disponível para download nos Portais Nacionais dos DF\-es\. Cada código de CST e cClassTrib está vinculado a um artigo específico da LC 214/2025, facilitando a correta interpretação e aplicação dos novos tributos por item da nota fiscal, além de orientar o cumprimento das regras de validação\. 

O Fisco ressalta que essa tabela será atualizada periodicamente para refletir melhorias, alterações legais e demandas da __Apuração Assistida__ do IBS e da CBS — especialmente durante o período de transição da Reforma Tributária, de 2026 a 2032\.

Os Códigos de Situação Tributária \(CST\) também foram atualizados para atender às disposições da Lei Complementar nº 214/2025 e à implementação dos novos tributos\. Confira abaixo como ficou a nova estrutura:

- __000__ – Tributação integral;
- __010__ – Tributação com alíquotas uniformes – operações setor financeiro; 
- __011__ – Tributação com alíquotas uniformes reduzidas em 60%;
- __011__ – Tributação com alíquotas uniformes reduzidas em 30%;
- __200__ – Alíquota zero;
- __200__ – Alíquota zero apenas CBS e reduzida em 60% para IBS;
- __200__ – Alíquota reduzida em 80%;
- __200__ – Alíquota reduzida em 70%;
- __200__ – Alíquota reduzida em 60%;
- __200__ – Alíquota reduzida em 50%; 
- __200 __– Alíquota reduzida em 40%;
- __200__ – Alíquota reduzida em 30%;
- __210__ – Alíquota reduzida em 50% com redutor de base de cálculo;
- __210__ – Alíquota reduzida em 70% com redutor de base de cálculo; 
- __220__ – Alíquota fixa;
- __221__ – Alíquota fixa proporcional; 
- __400__ – Isenção;
- __410__ – Imunidade e não incidência;
- __510__ – Diferimento;
- __550__ – Suspensão;
- __620__ – Tributação monofásica;
- __800__ – Transferência de crédito;
- __810__ – Ajustes;
- __820__ – Tributação em declaração de regime específico\.
	- 
		1. <a id="_Toc202175069"></a>Grupo de__ Compras Governamentais __<a id="_Hlk198631564"></a>__\[Conciliação\]__

Esse grupo de__ Compras Governamentais__, dentro de __ide__, identifica se a nota fiscal se refere a uma compra feita por um ente público União, Estado, DF ou Município\. Conforme o ente informado, __algumas alíquotas devem ser zeradas obrigatoriamente__:

- União: IBS UF e IBS Mun ~ alíquotas zero 
- Estado: IBS Mun e CBS ~ alíquotas zero
- DF: CBS ~ alíquotas zero
- Município: IBS UF e CBS ~ alíquotas zero

Se essas alíquotas não forem zeradas corretamente, a nota fiscal será rejeitada no sistema de mensageria\. 

Inclusos os campos para __tipo de aquisição e percentual de redução de alíquota__\. 

### <a id="_Toc202175070"></a>Nova Regra de Validação Cofaturamento \[Conciliação\]

Implementada a regra de validação: __G70a\_223__ – *Rejeição: NFCom Local informada deve ser da mesma UF da NFCom\. *Essa regra garante que a NFCom de prestação local e de longa distância, nos casos de cofaturamento, estejam vinculadas à mesma unidade federada\.

### <a id="_Toc202175071"></a>CNPJ Alfanumérico \[Estadual\]

Todos os campos do tipo CNPJ e Chave de Acesso nos schemas do projeto NFCom passarão por alterações futuras para aceitar o novo formato de __CNPJ Alfanumérico__, que incluirá letras nas primeiras posições, além dos números\.

As novas estruturas serão:

- CNPJ: de \[0\-9\]\{14\} para __\[A\-Z0\-9\]\{12\}\[0\-9\]\{2\}__
- Chave de acesso: de \[0\-9\]\{44\} para__ \[0\-9\]\{6\}\[A\-Z0\-9\]\{12\}\[0\-9\]\{26\}__

1. <a id="_Toc202175072"></a>__Premissas__

Homologação das alterações dos processos da SAFX42 e SAFX43 para a NFCOM conforme às demandas: 

SAFX04 \- MFS591904 – Adição de campos para atende a NFCom

SAFX42 \- MFS591907 e MFS779390 – Alterações da estrutura para atender a NFCom\. 

SAFX43 \- MFS591910 e MFS779390  – Alterações da estrutura para atender a NFCom\. 

SAFX254 – MFS61353 – Criação da  estrutura para NFCom\.

SAFX331 – MFS652069 \- Criação da  estrutura para NFCom\.

SAFX332 – MFS65207 \- Criação da  estrutura para NFCom\.

SAFX333 – MFS652075 \- Criação da  estrutura para NFCom\.

SAFX334 – MFS652078 – Criação da  estrutura para NFCom\.

*SAFX431 \- OS441 – Criação da estrutura e MFS\-1079 – sem alterações para NFCom\.*

*SAFX432 – OS de criação  = MFS591913 – sem alterações para NFCom\.*

TBD – Validar com a Graci se as alterações para atender a NFCom foram finalizadas\.

TBD – Validar se as SAFX431 e 432 não tem alterações por conta da NFCOM\. 

Obrigatoriedade de emissão da Nota Fiscal de Fatura de Serviço de Comunicação \(NFCom\)  prevista conforme [Ajuste SINIEF 34/2024](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2024/ajuste-sinief-34-24) a partir de__ 1º de novembro de 2025__, ou conforme nova publicação do governo\. 

1. <a id="_Toc202175073"></a>__Conceitos__
2. <a id="_Toc202175074"></a>__Referências RT & NFcom__
	1. <a id="_Toc202175075"></a>__NFCom \- Referências__
	2. <a id="_Toc202175076"></a>__NFCom  – Obrigatoriedade de emissão da NFCom__

[Ajuste SINIEF Nº 49/2023](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2023/ajuste-sinief-49-23) obrigatoriedade de emissão da Nota Fiscal de Fatura de Serviço de Comunicação \(NFCom\) prevista para 1º de abril de 2025\.

[Ajuste SINIEF 34/2024](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2024/ajuste-sinief-34-24) prorrogou essa data, estabelecendo que a obrigatoriedade da NFCom será a partir de__ 1º de novembro de 2025\. __

- 
	1. <a id="_Toc202175077"></a>__NFCom – Alteração SAFX e tabelas Internas __

SAFX04 \- MFS591904 – [MTZ\-DW\-Manutencao\_SAFX04\.docx](https://trten.sharepoint.com/:w:/r/sites/REQ_MTZ/Mastersaf%20DW%20TaxOne/Documento_Matriz/Basicos/MasterSAF_DW/MTZ-DW-Manutencao_SAFX04.docx?d=wf4d24ab268dd40f09ead4c73d31bbfdb&csf=1&web=1&e=W3b77o)

SAFX42 \- MFS591907 e MFS779390 \- [MTZ\-DW\-Manutencao\_SAFX42\.doc](https://trten.sharepoint.com/:w:/r/sites/REQ_MTZ/Mastersaf%20DW%20TaxOne/Documento_Matriz/Basicos/MasterSAF_DW/MTZ-DW-Manutencao_SAFX42.doc?d=w24989f6b94694d11830115c0d425aac4&csf=1&web=1&e=4cP6As)

SAFX43 \- MFS591910 e MFS779390 \- [MTZ\-DW\-Manutencao\_SAFX43\.doc](https://trten.sharepoint.com/:w:/r/sites/REQ_MTZ/Mastersaf%20DW%20TaxOne/Documento_Matriz/Basicos/MasterSAF_DW/MTZ-DW-Manutencao_SAFX43.doc?d=w5ed349a8b7cf452daaac3d4cb75f563e&csf=1&web=1&e=pOBr16)

SAFX254 – MFS61353 \- [MTZ\-DW\-Manutencao\_SAFX254\.docx](https://trten.sharepoint.com/:w:/r/sites/REQ_MTZ/Mastersaf%20DW%20TaxOne/Documento_Matriz/Basicos/MasterSAF_DW/MTZ-DW-Manutencao_SAFX254.docx?d=wa92bc7fbce42426185a0aab998b891a5&csf=1&web=1&e=guHoWy)

SAFX331 – MFS652069 \- [MTZ\-DW\-Manutenção\_SAFX331\.doc](https://trten.sharepoint.com/:w:/r/sites/REQ_MTZ/Mastersaf%20DW%20TaxOne/Documento_Matriz/Basicos/MasterSAF_DW/MTZ-DW-Manuten%C3%A7%C3%A3o_SAFX331.doc?d=webf83f2b1bb4427cb042604c859929a2&csf=1&web=1&e=cJvTWE)

SAFX332 – MFS65207 \- [MTZ\-DW\-Manutencao\_SAFX332\.docx](https://trten.sharepoint.com/:w:/r/sites/REQ_MTZ/Mastersaf%20DW%20TaxOne/Documento_Matriz/Basicos/MasterSAF_DW/MTZ-DW-Manutencao_SAFX332.docx?d=wbfecfea1ece84ee790b4a5d7cf4c4429&csf=1&web=1&e=qNo9co)

SAFX333 – MFS652075 \- [MTZ\-DW\-Manutenção\_SAFX333\.doc](https://trten.sharepoint.com/:w:/r/sites/REQ_MTZ/Mastersaf%20DW%20TaxOne/Documento_Matriz/Basicos/MasterSAF_DW/MTZ-DW-Manuten%C3%A7%C3%A3o_SAFX333.doc?d=w15d49ff922e944a69fa9867675c571cd&csf=1&web=1&e=w0DWRK)

SAFX334 – MFS652078 \- [MTZ\-DW\-Manutenção\_SAFX334\.doc](https://trten.sharepoint.com/:w:/r/sites/REQ_MTZ/Mastersaf%20DW%20TaxOne/Documento_Matriz/Basicos/MasterSAF_DW/MTZ-DW-Manuten%C3%A7%C3%A3o_SAFX334.doc?d=wf529130eb0504d7a9be26cb92f5675a8&csf=1&web=1&e=3KcxMW)

*SAFX431 \- OS441 e MFS\-1079 \- *[*MTZ\-DW\-Manutencao\_SAFX431\.docx*](https://trten.sharepoint.com/:w:/r/sites/REQ_MTZ/Mastersaf%20DW%20TaxOne/Documento_Matriz/Basicos/MasterSAF_DW/MTZ-DW-Manutencao_SAFX431.docx?d=w670fba50203840edb88e66021530af8b&csf=1&web=1&e=YNZtfL)* \**

*SAFX432 – MFS591913 \- *[*MTZ\-DW\-Manutencao\_SAFX432\.docx*](https://trten.sharepoint.com/:w:/r/sites/REQ_MTZ/Mastersaf%20DW%20TaxOne/Documento_Matriz/Basicos/MasterSAF_DW/MTZ-DW-Manutencao_SAFX432.docx?d=wbc4d43d79e7343ee864b3c1253453e16&csf=1&web=1&e=67HC9L)* \**

*\*sem alterações para atender a NFCom\. *

- 
	1. <a id="_Toc202175078"></a>__RT – Mudanças na RT para NFCom__

[Nota técnica 2025\.001\-RTC v1\.04](https://dfe-portal.svrs.rs.gov.br/Nfcom/Documentos)  atender a essas exigências, substituindo a Nota Técnica DFe – 2024\.001 IBS/CBS v1\.10\. 

A nova versão traz grupos, campos e regras de validações voltados ao IBS e CBS, sempre alinhados à legislação vigente\.

__Tabela de Código de Classificação Tributária do IBS e da CBS__

[cClassTrib \- 05052025\.xlsx](https://trten.sharepoint.com/:x:/r/sites/MarcosTeam/Shared%20Documents/General/Projetos/Solu%C3%A7%C3%B5es/Tax%20One/Reforma%20Tributaria/NFCOM%20-%20Mod%2062/Doctos%20Ref%20RT%20-%20NFCom%20-%20Mod%2062/cClassTrib%20-%2005052025.xlsx?d=w98a6acc58a0042d8af2c82ec5a9df01b&csf=1&web=1&e=DeVFiO) \- Em dezembro de 2024, foi publicada no [Portal Nacional da NF\-e](https://www.nfe.fazenda.gov.br/portal/principal.aspx) a versão 1\.00 do Informe Técnico RT 2024\.001, que apresenta a __Tabela de Código de Classificação Tributária do IBS e da CBS — a cClassTrib__\.\.

__Prazo de implantação da Nota Técnica Reforma Tributária NFCom 2025\.001__

Em razão das mudanças exigidas nas infraestruturas das Secretarias de Fazenda de Estado, dos Municípios, bem como nos sistemas dos contribuintes, os prazos definidos para implementação da Nota Técnica Reforma Tributária NFCom 2025\.001 versão 1\.01 são:

- 
	- Ambiente de homologação: a partir de __01/07/2025__
	- Ambiente de produção *– grupos, campos e eventos*: a partir de __01/10/2025__
	- Ambiente de produção *– regras de validação*: a partir de __janeiro de 2026__

__IMPORTANTE__: as mudanças entram em operação efetiva a partir de __1º de janeiro de 2026__\.

1. <a id="_Toc202175079"></a>__Proposta de solução \- NFCom & CTE__

Para atender a Reforma tributária, as atualizações se fazem necessárias aos processos do Tax One\. 

<a id="_Toc186457526"></a>

- 
	1. <a id="_Toc202175080"></a>__NFCom – Modelo 62 | RT – SAFX3042 __

Criar a SAFX3042 \- Capa de Documentos Fiscais de Utilities para suportar as informações da NFCom\_Nota\_Tecnica\_2025\_001\_RTC\_v1\.05a para a operação de Serviço de Comunicação – Modelo 62\.

__Regra __

- Entrada/Saída \(MOVTO\_E\_S\) = 9 e Modelo de Documento \(COD\_MODELO\) = 62\. 

A nova SAFX suportará apenas as operações de saídas \(prestação de serviço de comunicação\)\. As informações de entradas do serviço de comunicação, serão mantidas nos arquivos SAFX3007 e SAFX3008 conforme os itens 7\.3 e 7\.4\.

- SAFX3043 \- Itens de Documentos Fiscais de Utilities:  a SAFX deverá ser atribuída a Capa de Documentos Fiscais de Utilities, ou seja, como filha da tabela SAFX3042\. 

Adicionar os campos dos grupos: 

- Total DFe;
- Compras Governamentais;
- Totais IBS e CBS\.
	- 
		1. <a id="_Toc202175081"></a>__NFCom  | Total DFE__

__vTotDFe__ – Total Geral do DFe: Valor total do documento fiscal\. \(vNF \+ total do IBS \+ total da CBS\)

Para carregar as informações da tag vTotDFe, utilizar o campo 15 \- Valor dos serviços da SAFX3042\.

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA2YAAABJCAYAAABWxzWAAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAACjESURBVHhe7Z3NixzXtcDPvL8gct7GSRCM1G2CmJVlOY/uVZBwmBEWQxgN5BGjlbojCExvJDCe5ZiAvOkBgzOj1ZCQwMgYRUHdxJKW0zzHz14No+Bue8Dk2ZvY0j6Lfufcj6p7b31Xf1V1n59dmq6qW/fj3HNv3VN176mlk5OTIQK0PXv2DBimjNz5n3vq1/xz979uql8MwzAMwzDMvLD04sWLofoNjx8/hjt/+U7tTZbTP/4Gln/9e7XHlJWi1OOi6FOZy8l5Lx6L0m4YZtHgts0w5eQ/1F+GYRiGYRiGYRhmRrBhxjAMwzAMwzAMM2PYMGMYhmEYhmEYhpkxbJgxDMMwDMMwDMPMGDbMGIZhGKYQvAQrNdzU7w38nZeVszoeJsj45MwwDDNORvLKuHJ9Ex5eewF33voYoNWEuxdPxe8P1fk4iuMxCDvl1hW4dfEMLKsjp9+ewgfvYzm+VgeYSKLr8SV4++51uPmy2rV4DvfeOYTffX0e7v3hClz29tXpHIxXn8Lzfvrt56gXn6bUCx3H6GUzSS5nnNwRLMO1O1/CmxPIWxLxecd8Yzu8UtB2mE6/0sj+UzhWu0VgvO1mGkTJ+Dk8ffgZ7N7/siDyzdf+N8R9VO0Qnz2Bc+0v1U4Gam/AV7eW4fThfbh8/3t1ME0by5fvsjE2OReY8rXtMjOP40gs0/XX4Na1ZVWm53D62Wewhe2kSPeweWSkN2Y//fEZHGw8h39gBVZ/hAfE7zJBhsF17KBlYzrF/BPLLy/D3Xc34e2zYpcZGWzQKFt/e6GOlwGZZ2L55VdRL96ADbFXYL7Rclb7hJb9N2q/UMh2eHMe2mHpZF9mlFzF7zNw+doVeHj3UonfEuF9FD6HO+/swbl37sOdD57AtZzGwsbr1JKew5NPtFE2R21sZMYnZ4aZ13HkRgvL5BllBJbvIvaxrfNqn5kU+Qyzs/Tq/xL8gowxrKyf1s7DOXECjTU8VxboCcdl+kFPst/ag8t3DuHcW9hRf0YHz8DN35b5Jl8cTh8+EbL1t49L8yT26Qcyz+feegJPxZFl+EVN/Ejge/jdHbzxvzXtp86YblvJ+f3P1aD1FO5o2bfpjc2s8hbO/LTDNLJnxoXXr6DOnHtHyfvlV2H3ehHuQXnaGOmPeiP/9ffwYS/vk+nz8At6G/TtKfxVpc33OpNxyZlh5rVtqT4E6M059WNGH3vxIr+0mDD5DLOfvAZ3b70Kl2k6CT0V8H6/Cnd/eUYEKT5a8XDw/cAcMGFH/dHn8PSzU3hqPeE+D2/f3YSv/tCU2903DOWk6R90fBPeRiP1nvgt9+/RIP6scSzqOifMhqX49Ep5E57qtDH80+vn5/hGStMCDFkLOc56sPUcvlJvQc79WOclpU4UrhNz8zZLPYxvh3KwvQxvGnJ1deNpy8xDUh7NtnpJlPXp1Afyk+hLFpyvP4XLH0hTePnaa8Zb7RR9yVmpB16YML2P1LkofXLbGJGku3F6QSTptgL1hgaKp59qgyNrG1P8JKYvyCEzW+5hcqPyy/BC1xU07dA+lkJO05AzwyS0rdKOI8++JF+2GA936CHGV+onM1nyGWa9jz3r+ekHviUtfpdlSoBWPBpw/1P88MGb/M32x7j5DY2eitx8+Qw8ffgE7jzE0uKNLPgk5AzcvHUF48XGKAbxZ+DyLVT+d/HYN6dyehNd90v3VTBe9+5FEUZcR8auEbd8pXwGlr99Lhr66bf4m6btlOSVMuX1KXZG3paQb1Hei2fg9LPP4c4H2LlheS/fum7drKfPGTin1rV89X9yelA6nSgTM9DD2HaobwQo+5+IH55u0PRALw8Xr3hvSdLnkdrqqziAxXTVkWkx2b5kgfmnntb4A6iqAUlyX4IDmXfpwSKtUaP6eB6u9zE6J0nWp2TdjdeLtLodmMaYsY1JqDxRfUF6mSX34abcnsNfP5XTwMyHX3Lgewp/64kD6eQ0BTkzzNyOI+lBF70lM9dE1+QDH4AX0E89C4DJQ/41Zj/BSlU/5e8QxSwF6ZTsw4/uw7V37sPN+1/Ch7iJaW3YwH4qzmpQ4dE4pal6N72pTABP3sFj2EC96U0/cr1lyYXWFObmHTVlDhuVfIKpb0wY5v1D0dC9eC6eL/56JwHqB8rK29TRUM5eAhwP4E31c9ii6SY97NxUeS+vux3Y5BEdonjCpaYrYE70ACGdTpSJWephWDvEPkXcmBRaNzBVmh4o8iCmi2H7Eg4OsuVRPEiieDznCNNhsn3JAuMZGYo0fYk3sHoBX31C9UHTkIwBSaLO+cTqU4p44vUirW6rcOaTbo8Ubcwjpi9IK7OUfbgpt+NPcMCIx5YvqSf5Oq3PMB36i8TKaWpyZhiTeR9Hnod7t+TI7fTh/6Zy8MfkJ5dhJqYWqEq6fEv/JmvdnoJQDvynq/GcgTd/+Zp666MH6UE849QbJGR9uqBvlOoJpr4xWa+Uv4QnIkzavM8W8gwmbtx6S/NW9eVX4aF+5f7uq/HG3ESRxiRBXpbuvGN6HU2nE+Vk2noYFof/ltLi2wgnQ5nyOMsHSdPqSxYMz2BwiOtLUD8+EGtBlsX9S0zvaYVM74nSOY+U+hQbT4xepNVt9VTbn8ZokqGNWTh9QVqZperDHbnpMqkB5crPpPOBp3837xkp2s+k5cwwFml1Y1p9/xjv32J6pMyr7eWVmRS5DLN/fPQE7omOGa3vD/C3qFz5e3dmg52MeAqvFNek9oZqOJfUkwSaunEFbl78ATx5/xAu66cRzORQC2ktg24GrsbF01yVPj3B8l3fsk6Mhbh26A20Z2lEjRvWm4nhzeJwBjGxfcn38GF7D669Q/c0mgqJcZDnsal7dxyPXshpjP50a8HY21hKmeXqw79X0xkpry/Bm5fooZiZt1HlxO2PGSPzPo48e0lMoSQfEmyUTY9chtkxWtp9+kHWd0/OCRc3Q/JulMmqnyVfwt+EcelOr3gJ3l5fllPuvsEbEB3Sc2vNpw0TAxu4eIKpbka64XuvpAkdZo6foJuv98+ehw2sg0J9BHSqOjELpqWH0e1w45fqKbsrY1M36HtN9ESe5smPmMeV6/JG+vYk3/pPUG+mkv+iQk91o6baJPQl9CFmenosPGpq76uWDiFROpeVqHiS9CKVbqvP1qCppKdbS3K0MQunL0AyyyxDH66nM15+/TWZrpm3tO1nonJmGM38jiNXyLAUb7ppaiUbZdMk5xozfQMwSJzqUTw+bOsbipxyQYOar+hbL0qh732kpk/oReWo1FvYuN6OeQWdD5oGugn3Wm94r4z9xqsbPob5rQzjvQI35t0XGVpgKp8c6U17FMJOQ71uv/JbdezrT71pMncp3HX5xOburStw68d0vCBMXCdmwWz0MKodyg/A0px49ZTd0g2VBzUYl1OdRsnjediib7bgjfTm6zkG3GmZmN5MKf8FwutXaNBNT3XpIK1r0gOINH3J2Uuw++511DvpCW3juho86cFKos6lJCmeRL1Iodto/Fyhe1eIrqduYx6YDvYFTzGdQF+QSWY5+nA9xerisojXmpaZJKdpyJlhDOZxHElG2UNsN7LloAG3bo/h7lmOj5hxk9MwU5b2N99jh6mt7jLyJdwU35uQDcZeS2R8f0Z09nJ6xeVbF+Hcp5/Lhjg2aBoo5uBHeCMiWVL6xpSPD9uYx4eYR8zfZbxZLb+Mvx+W6aOYZ+STI2/7gTr+PfzugVrsjZ2VngogykvyxmM3r8knNlReb8BVBCauE7NgVnoo26GcFhXTDhFfN1QeMM/0NO+mdsiSO49046L6xPiyDLizMjG9mVL+C4XqT8RvLDfVszNVLrEvwfrYQp0nD2XkCY0+qCr03lhLmqRzaYmNJ4VeJOl2+HosTfo2JpF9wVdhfUEmmeXpw/V0RsL8SDaSVk4TlDPD2MzhOPLHeowmkeM2f5PTn5lJsfTixYuh+g2PHz+GO3/5Tu1NltM//gaWf/17tbeo0Pcn6MkKNqjQm2PxKUo9Loo+Taac09HDMtfRvOrXorSbQkFT69YB7rxvrlllxs6Cy5nb9qJQ/nEkY5PzjRnDMAzDMJnpfQzXPv2B9Y0hZgKwnBmGKSFsmDEMwzDMNBCOKDbh4bUzES7tmbHAcmYYpqSwYTZTvoffiY9f8utnZpawHjLMVOh9LNoZuY5nL2cThOXMLAx8/5432DBjGIZhGIZhGIaZMUsnJydDBGh79uwZ/Pvsz9WpyfLfP/tP+NMn/1J7TFkpSj0uij6VuZyc9+KxKO2GYRYNbtsMU04CXhk3NuQ3yifNn//+Hfzq9R+qPaasFKUeF0WfylxOznvxWJR2wzCLBrdthiknPJWRYRiGYRiGYRhmxrBhxjAMwzAMwzAMM2PYMGMYhmEYhmEYhpkxbJgxDMMwDMMwDMPMGDbMGIZhGIZhGIZhZgwbZgzDMAwygN36Eiw1u2rfptvEc/VdDJVEfDzFJ3v+hWzGXN5JxLkIdJt1WFoyZDfYhd1ustaOhxLofreJ8mlCWA5Z56aN0peQfnWwq/TY3fLUT0ydy3N12E3RRESeUt0DRoTyNI10CgobZgzDMAxSgaubNYD9ByE38C482AeobV7FULNhsNuEejP7zTrvdcx0GUs9oRG2g3ra7g9huLcqDnXfa0Fr5xHXv6IrGvIFqKp9H9XGLwTPMONmAAM0PupLVWj1cHflFadfHcCjwx402n3o951N6XV2juGLQCNAw5AaTGMbtlJ07P0TzGwgr+NH6OgU0ikqbJgxDMMwgsrVTajBPjxwLbPuAzxag82rs7xVHkPvWP3MRN7rmOkyhnrqn0APVuAVQ01X99BIO9pa2EGezQC+IBmHDXoHX2AN0CmW1GSht2RVqO4AbPc70MAjjXXX2OrDSa8GF7C/rVScTYXIRPUC9t4hdN9Dw7AG7dtpjD2pO5M33KeVTnFhw4xhGIaRVK6CfGlmW2byKfsm+HYZDi70lDHa6k2Iny02gC69EfGm5NShac2dkVN66rtdGa8zXYemWFXp0XKvBVVrOk98vHHXZcu/iXmtWw5NUnldxhUnhjHLRWGMgoVNVbOP6Xqw46F9GHShSdOu6BjKy07aSdeRp05DvBUzwxjn89SviZhmtYZ6CvuwZsQh0janRQ12/XLgVqd8qVOSeBnS+fy6M2towB8x6BVGLRoD3qlgOV3Ry7c+6jxu9htP1Bc8RrKLmq6XXBcOCeFT5Uf3MSKMmsJnxmvopXWNl27ItL9M5ajA1hE9LNiDVSBj2JS5gh6E6f52MKD/R6PyCqxg7Z701b4Ay4btpdY+8N6Wxcpv8AgO0YizHs4lljujDggdk0ZptnSSdbVUvHjxYqi3+/fvD6fFnz75l/rFlJmi1OOi6FOZy8l5Lx5h5eq3a0OAxrCj9of4qwEwrLX7ah+PNGAIjc5QHukP2zXcr7XtfTyv8eLUUfTdONU1UMNjOl4bEYeXhiQ53vDrsubfRFzrpdkfdtqNIdqyGctrM6447XgoSAP3a0MdRJfbxD7m1EO/r9LFYzWKF/dxc+Uj4jBk7OVV7ct8YV7xGhEn5d2JI6yessoRE7LSJey8OderfOSRodzNpjvTJLTP6rdRr/yymLjyT9on2bUbbb9uSLamLEVauI9608ZAXjCNPm/WRWLdwrDhV0ygLtPkR+sxHvB1XV8XiNO8Rhxw9AnJWg6TEH0lpKwxX5S23kiOKaIMJ5gnr22p/UT5uXlNU24dJkEHqE7pXL+D+6JOsqWTqKslgw0zZiSKUo+Lok9lLifnvXiElsu7WZr74YM5jT1YcQen4QMVe2Agr3HDmARvtmniDbsuSHz+TWSa7ik9WFd7qfLlM644w+MxseOU2MdCyh5S/7ZMKV1XP+y8hKXr1kuwntKU2SGlYdZw4vRJlqGLHX+c7kyXsLYdLbtgvu1ySYQ9E4nThiOMDk0anfCJkmvIYN8jOT8yD2Z6KcrgHMtWDpswGYs8NAxjURBiEGbCKRfmPqxt2djXuGVKVe5YHZDxJ8WRJp0w2cTrarHhqYwMwzCMj5rOeKxWig8eHULPmsZI0OL1XWg2m1Cv10HMIItCrF0Jrk+rvLKC/4YtSE/JSPFmyL+JSjN2+UPWfI0rzjTxTAKRbg9aVX+q0dLSGpBItQ7lIqscU7EKt9sNOG5VMY91rP9dexpiKhnm1J0CIJw3hDr+CE5xXN2j9U80tZSmj8qpYxWzKgZySiDJQG7kyMKvLzH9ubGOEg9DOhoJrq2KQk5vC66FMtZcZc6PXstkOjSSctDr7OLLQGQth4lKP+BQqQJbe0dwtLcFq96JCqzebkOtdwiPXL0f7NrTD0Pn8FWAmk1PzWUc7O5g+2zAtunxI1Z+0hmJvzYxXbnj5Sdl7cZhOxhJl06irpYMNswYhmEYA+mdsXdInuzkDdkePNB6Abl4ff32bTg6OoJOQ50qBWXPfxHBQTN5Qhza21EaV29TprK1B0eYt35nGy7AIayhQdn0FxUlUGbdiXH8EercZxX2jlBO/W2AwzUc9Bprr8gYqK7ByfqBkIHYtkkQ2vFKggOHCAM40uufCG87dbHIlR/bCBMIOTRA2gHhZRjIg9K4zVoOi5D04xBrAEOobMGB4bUxuc114b1WDxodWuOmSJSfY0SlKneCDliy1jiGWGr5xuhqCWHDjGEYhrEQ3hnp6Ww3bMG3PNY+oCe6SYMAJHThOd1z8a4dN9hKIm+8WfNvEpGmRdZ8jSvONPFMgqh0R/VYkFWOKdHZqqyuijcTZFjt7yinBEkyHEV3Zo58awLHX8iyGrjOfQaDLnSVoCoVGvTSGwnfW6t4i97owJ7/SkfFod/GZTQ6BElvR4JvSXVd5spPiGEgdMu6xjVWwx5UuaR8ixZhdIQ56CHcOjIxvTZGUb0gpkFAl96W1dpgvnxMlF9EXm3ccufQgRzpJOlqKeE1ZswoFKUeF0WfylxOznvxiC6Xmv8Pwbn7Q2cNGjlHoP3gugB/X6wJoLUG3gF3jYO7BiIEtV7BDJIcL+JelyP/JuKcl2a5nH/oONrCAUdYOiHrPhLXmCWnK+VpxIm4cWAglTe1j2SVo47DTEmkrdPx6t6LMFDe2LKMqDvTJLRti7Kg/LAA0gkLrV0iGdvr6mTd2DIwdcCuOz8Or15C6sHGl7uOQ+yb+mCh+wcnvMp0nvwE9A+x9FTJisJIOeh4zXiylgNRcvd1m/bVOULXkXa+g1tHhLXrKDO6PCHxpJOf2QekKHeIzG3stkyOP4RDoIzylXknOap9TDdpTXTRYcOMGYmi1OOi6FOZy8l5Lx5x5ZIDB+PmbKDP0c2aHClYg19CDWD9mywNLtQg1rjOR95ww9LyUTdlut4bWSTFSwSvy55/E4xPDVys663RTpp8mYwrTrpOx6PCeEYIYchCXS9kYchTnDfTTWGYJaUbLEt4HPnq1yBkMOjWre/5TW7kZMGOMb4so+nO9Ihq254xqTbhMS8g0iQ9wkG1lqHwuCcH2bragnUbAhnZVj3owXcEgfBm/NnzE9TJiGtMeRkGgEemcsg0dFhvc/Im0jTilGWKjjUVom1gXFaZNfHyo/OybRo6nVDuNDpgypauFwaom79E+SbpavkYg2GmOtOkRuiQfqBj3kicLWOaLqJhBuKkzjbYsELD4hY/kJh/8g5Yo+RJjSqPSMsxcA4Z9GRkEuUcd11EMUre7cFE1o43Xx9lMprc49KXNxWzbFHu4n0wPutGlDQYiKYc7YZhmKxw2x4Nui8u+viOmQ0jrTEjz0T1JfLcog5MhApsHeiFjR3AAQ6Obzpy/yD91/zFhy2tjw0qam3oGAsnO5srcNxag2rYh/CcsLQdFHBxc2kIkWe/73/scFpE6kYCea8rJAWpi1C6Taiu7cNKR+WrswL7a9VUC/an00dFk5R+t1kVXt02vbJtAlD/E1k46XygdbwCbe+aNqBAYq5hGIZh0iPXMWVbI8cw4yG3YUZf2a+uHcJKG42Zhjo4KbyFjXpFYFXtq91UHEOP1gyHUPXir8AqeWzqk1vSFtwIcTtqhhWbOs7kIyBP3KZPtG7Ek/e6YlKMunBBQ2SHVvrKhckiX6t79oL9CKbaR4WQnL5axNw5gi2vbFtwQE+f9h/g2RCE8wG8Znsv/TUMwzBMelI5oWCYyZDbMKtsHcFweAR7Y3mkTk+Bg99foIHNUtibqwAD6NLbC+9bDvQtA/8q8nJTpUfWaGxV6XzSk+XKFpCnUOkuOi2YhybmV+eh3rS/j8IUkmjdyKtTqMusB2PEcdOrWF2nBnqCZ6MZbx+VneT0V2FvOESDU+2aeJ7BHLBvIlff7jXy204MwzDMyIh+9qgYM0aYhaMg7vLN7+Zo0rgllQx2b8BaC2Bbf0eFvmXQqnqG3ureEPpyDiT06XzoSMhGDvyCH/PrDwYw8DZ1EBFTko43Zfy49TePYa1a7m8pTANbnrZMp0GUbuTVKdKDFmwrPehDG/Zh7UY5pjvOui5CEU8uo8j7kdliImTebcINNPgb2+mnaRO2a2iGYRiGYcpIYb5j5n03Rw+01PdC7G9IhCE/lldr3/a/kl6hr/ujodd6b7yGUa+FxlYVqt6mDS+akiS/beJlYWu7/N9SmDQBeeJWCCMmv06RwUZGmrxMfTemDBS2LhYEWkdHMqcFZ42O9Y2ZJMiYW3P6H4ZhGIZhykdhDDO0zGCz1oNDZZmJD95FfEzPQs0Fdg04ObVnzE/U9dsRb1NfThd56EGrqqe90baGZhnmYJ4e6Y+bgDxxOyrA4HIknaK3HrvQbDahXq8Lxw6loKh1kQY0TPx2F5wSXQpW95Tc+7AN5Hwo3dt2uY7tWK5TK0VlMQzDMAwTRXEMMxwC+tMZ009jnBRyalAKw9CjBm097c3Yjni0tEBIj3nVHYD127fh6OhoJk4n5orKKxD90nEFhNMsNGqkF0m5ldtTagWL04FGL/ltO61prbYA+52j8HVqDMMwDMOUigIZZjgkoel/YjojLfhPM40REQO3Hpw4XgAGX9DKFDVwy8pgF8gRXGrDMCIPxVikw2Qmr06p6bc0pWy1EB4N54EqXBAOB20rxV1Tpb1Iik0dKzziTV/Im7HYdXWEdJa0drwCHTTK+NkPwzAMw8wHoxlmykmARjoPUDu5WIX1Rg8Ob+zAfuq3VXLtz/6a4f1uYKwRUofENLTeScCZB2E6PRCe+Kot6NXaGZ68U77pU0J+Hmjdx1L1BpRxVtU0CTqcmL7Agroxik75Bh3pABn4PnrN2Rc4tC4eRaiLIBXYIhep+2vQxMoQ+RJrqshlfIqplk45Ru+jMhKX/uq6WIe6Jjx3ynAD1LPmDex/8Ix2REkeQH0DDs/Td8ygDZ2D22iY6uvkxjAMwzBMiXnx4sVQb/fv3x+mpz/EsesQo3C2xrCjQsQR+VX6TkPEE/7FdZlm8Fx/2Gk3hjUvD7VhIySMl9+GzGGnocMbW42u7WBoGxG21g4c98E8NGpGXBhPJzr0vBBZjwmEyl7JLc/H9vPmQxLUjbw61W9rHZDhA3rTb6s407UTl9HKGc646yKKUfLex37BqotUbWu0PsokX95TpN/vDNtWv4H9W6M9NIsn+xVVF6p/jNo89U3JJPSJYZjZw22bYcrJEhlkeEMXPH78GDY2NtTeZPnz37+DX73+Q7XHlJWi1OOi6FOZy8l5z0sXmksPYF07Gxoji9JuGGbR4LbNMOWkUGvMGIZhGBNaT7YD0Bm/UZYHOa2yHjpFW5wzPt4vwwa3cnnNlOv5zHIl4cohK+L6uv+pijA51pvupyycD9tjHdUxD+Wb3Dp9eVOa5Einbsh3qd6EXW8eu2Sx6mGMDHZht2htnpaaGG0sN4Nu+voWa4plOFddybuuH4e50RR2ejAn983r/Gv0NPd0ukdLAXxdr4slAtGo9ohh7X472GbctELLVMd7h5FedLlp0+VaPNgwYxiGKSwV2DoqmtfFHrTSfuOu1oaO4TGTtnF4zRzQWuDAoDiZvNfNHFOOnTbAfguq3sCSBk9VaAlnMDrMpliXWXVHgDmZX3lL2dGa1c2Okh1unZVjaK1Vgw8RZlwPZaT7Xgta4/6m7IgI51Err4zoKAoNpuoatPZ7+LsGtVoN//agF1rfqBvGgnP3M0r9E4qDkPH4Gzm4kj4MCM8JFhq7N1oy3XafHtop3UvIi/y8yj6ewVAUBH/tr0X7Qug2MU6VtRXD6xkdX8O0/HgwJietQJnoZw/vHUZ6tBxfllPuC8Q+bo31QjyMnAVsmDEMwzDpoZtmrwXvpRxpVU2PmUleM3HAUU/1pPQYevGuKyPIe93s8eS4ugUHbRzJ9E7EwEZ6gyVnOHvCG6wZpnb8IF6WCy7vwe4NHHjS4PYItlaV7HBb3TuCPsqvF2JQTKQe5pjVPfp0EMpE7c+eAZCD5doF7dM3J90H4lu1ZKz3h0fi8zi0YFuw79R39z1h4NQaDWmgWMj8EPQ9SorH36SDq1VtmR2T4zAyCMlBlAwvnnOp+PFAMC/iGsQy5oYYZqg+5+N/P9ik2zS/w1oDT1zK+RYmBh0VT7DcIWUa9oGai5ne6pY6Rw6+CJKlLvsCfwOGDTOGYRgGoaeuwamGYrqJOe1nZVsMNoXXUnVomtCUsioNMNA4rNKUF+8prfKq602FqUPTKEvcddYUIOElU51KxLzWTs8nPl8jo7715z6Fr4hBz+gD4jLKO1388nupaEmFfnKicvUAOp1175MciUy4HsZDUDYBEeIAvqmmrwVlLKfV0fQ3McWtLqezGS9KBGLapziow8vjAiv+4BS4xPNpymBixifCBj/HZE/vozQzvOUlw1wHXt1T37A16xvzK96WNWD79gVxpGd9i4fyQ399T7wBhAdfpHcIN+prwiCstfv+TIrV2/INLR7QpZKf90HUm8HBo0NhzJn6XqVv0SB2fkhkZJSRF+q2TNf4TBDFK95okYdqX4QOukyGQWdgvn0j3LwuPPm9Mo4GewyaD4pSj4uiT2UuJ+e9eLjlEl5FLe+z0rOk9oQrPHgK14/K46ThBtI/JxH7GFen3x/ioEFt6qSDd75DXksb1jVhBPOpjolr9YHOEAcVlhffsOt0vuUxVS4vTLCcJuJaL03Dk6sRPk2+TLTc9NmAHIWMQspF6dYaw3aIV2GXeZZ3fPwmMr8RSQWYRD1MkrA+y62PQP0Ir8GG11u17xVReRWuUfkwDP1H8rV02bzGvV55lfXjd3RGx+/tJ+tUmI55qPgoPTov6oz0gXRIhhBptC1PuJimW6ZQZN5EfWMZa57OOZiexlV+rPyannZrGI/eHMX0dMu93kSUBduEKCOmieWS4VQ7wGNmtF6c5kGdHzpm/o7Ej9uTmVcmX87kWdk9ppHtOo3MFwM2zJiRKEo9Loo+lbmcnPfiESiXO5By9vWgV+3gzTTiHKJvtvYWvCl7g5XQzciLQXAwFhzAEXLgYQwO4gZxCj0Al2HiDAWZpnvKlkO6fJnY6at9Tx5qUwNjCzEowwGdEcYNIphreQdx5emh5BBzqcXY62HChPVZYbLwbfEQI8s9Jtq8qbfuNXHho+pWGk1EWF26OhRfBpPw9JJ10i1THBg28JkkdUogddaXgdo30pdtRl/vb276frjwNirwjB/cSDe9cDof9rVap720dN+g8qfTjJaF+iSQcY04GlWm0Lag85a+Lc47PJWRYRiGkVSuwmbNXwMgpr9Efex/dQ86jQRHIGL9BU3t0VvIlK7KFhzp8/021GjtghderaFIYvAFHOOV5vQkQnwEHs84s8scBjDo7kKz2YR63VxXkYBKM3apykj5MnDk2N8G4ZzCmiJWWYWtvSMpy34HpbgPa9WQ6abzLG9BzvjTMM56mAGre5QfmlpKUxTlFMGKV4Vy+lmvdUPITW60Bk+dRoTTDMspQwWoyr2pcGKtUwO2lRLZ4eUUwvZttweoqOlrXZDBAz2ERXwZTGR53PiEUwpzypzyrOiXmRxeBHU7nIqoa1HPaNGgJKwp3oPdHbkODf/dEXHLaYjeukREO8lA48fTK9qOzIbYbcppwYLwNWECNZWyj9YS9PahpfVOtB3Cn5JI7cSfQYgHB7tQp7VrYp2XXNum8+ZOPRSg3JrKcU6N1rapa4hQxx/ECuqCG5WXt5ipnAsGG2YMwzCMogJXN2vQO3xEw1uxBqe2edUfxDiIQVKvBTdiF3kUGVorU4XqDsD67dti0TmNaYpOZfW2WEivvbQNXPGjcbB3QEbXPmhHbsVg0vLOEL94CGF4unOhtUnN3dj1b+WrB8zPEQ7cyaI8XEPjxjAYleHb7h/AwYG/9ft9ZSSEO83Q65SE7Hf2oeF92sMJL+I3DQOHCMM7YEjFlcFEOOdwB/uO8SeMkTU4WT8QuiI24YgiJp8EGiXdLm66wqmej8hgJPSDiS68Z1i1vV6PnBIq/DCUHzJgog1BNIDU04VGWzoPMZ3SkOdTeghhdsEVvSbNSycE5axGGkRYdzekQxG5jk0aqfqhxv4OGsGGkMWaPJTbPhqwjQ7qh7G2zS8Txqwdf4gHQGQr7gTXA/ZPZLrCAyVDsGHGMAzDeFS2ttHYOoRHIYvkg+CABEe+9JR9Rz19nQnC8UIPnDXsONajTMUNBmlwgoPRgy3hSS8TEWla5M1XFuhpejX823ITo6jyzhS/fAjhe5KzobfF+/snFCwds6iHDAzImFCGRMUzJMIMRuVRUm2+AOQbKPftiXhLSp7/6G0ZtMF7IaYG/nb4oKEQMGYtbEMqfRkicIw/MSOg0YE94zWOeMuXYCQMHu3A2toarN2gB1gK782PRL8ts9+Eac+ECu+aqDZDDxoMZx9b6xiS8MvcP9lHPd2336Jpj5E6XtF2CC3/gfiMgbTL6I2mrFsJGZBy88CfUmZ4XVO53K+RV0b6lIuTca9MhlHspR9EyJtwHX8Ipy1oIO6mrdw5gteYMaNQlHpcFH0qczk578Ujqlxoa4kF6Dga8NYNEHTcXbNB6wzEWg5aJ2CcE2Fj13KEE+F/wkatXTGXPsh1DcYahhDHAYHrnHVGtECd9s18yzKHl0Oc89KckvMP3DpqXYtMRq9boTR0GDwm6gSPiViiweDJlEXeKeK30bpbk84sHPmaZZl0PYwbt22L+jLW+EjZmGuO9Noqw3GKqAuVc1WXgXLQcXJWYchdEAgfEj/JxrvI37fOG3WXXAYTWx/J8YdbFzI+HX94vYei12KJTTrrkL9xE+VRuhCQlyoTnpPBSEa4H6GfUt/t894xLTcdhwhHeVG/cQvorzhurH+M00sdr1s/+lqRlrmpPIaWySm3R9RxM78xeZxT2DBjRqIo9bgo+lTmcnLei0dkudTN1R2giJulewcl9EDFOCfCRgw4RscYJBgDB2+gLrbasBEYYAWvkwaGHz6Qb28QFjZAwPi8xf/G9ZaM0uTLx01f7HvXqg0HQp5nOwINANsJAdad5WluVMoj78T4A7jloPBoTDrCK0Y9pCfYtkkWZt6cvBOeIennXYewjRiDkLZPhIaPiV8QOO96OkxRBgPPMFdxdShPVj6N9ESdS4PKKUo4WG4zr1LfZH49XQlE5LcHOuXpakiCvh477cAzxPzjopxmXly9FJhtJ1kvdfrePcBrlxGbKkN4mexy+0h5k+wCXYeqO9c75SKwRAYZCkvw+PFj2NjYUHuT5c9//w5+9foP1R5TVopSj4uiT2UuJ+e9eCxKu2GYRaO4bZu+bbYDF+ij3qHT9xhmseE1ZgzDMAzDMMwUoHWpK3AY582VYRYYNswYhmEYhmGYyUJeEMmhw9oxrMR4e2WYRYYNM4ZhGIZhGGay0Df0yH368Aj2eB4jw4TChhnDMAzDMAzDMMyMWTo5OSEnIOIbC8+ePYN/n/25OsUwDMMwDMMwDMNMg5l5ZWQYhmEYhmEYhmEkPJWRYRiGYRiGYRhmxrBhxjAMwzAMwzAMM1MA/h++WNnveJd9pgAAAABJRU5ErkJggg==)

- 
	- 
		1. <a id="_Toc202175082"></a>__NFCom  | Grupo de Totais__

Atribuir  a SAFX3042 \- Capa de Documentos Fiscais de Utilities, as informações referente ao Grupo de Totais\. 

![](data:image/png;base64,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)

- 
	- 
		1. <a id="_Toc202175083"></a>__NFCom | Compras Governamentais__

Atribuir SAFX3042 \- Capa de Documentos Fiscais de Utilities as informações referente às operações de Compras Governamentais\. 

![](data:image/png;base64,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)

- 
	1. <a id="_Toc202175084"></a>__NFCom – Modelo 62 | RT – SAFX3043 __

Criar a SAFX3043 \- Itens de Documentos Fiscais de Utilities para suportar o CBS e IBS para a Prestação de Comunicação – Modelo 62 nas operações de Saídas\. 

__Regras__

- Entrada/Saída \(MOVTO\_E\_S\) = 9 e Modelo de Documento \(COD\_MODELO\) = 62\. 

A nova safx suportará apenas as operações de saídas \(prestação de serviço de comunicação\)\. As informações de entradas do serviço de comunicação, serão mantidas nos arquivos SAFX3007 e SAFX3008 conforme os itens 7\.3 e 7\.4\.

- SAFX3042 \- Capa de Documentos Fiscais de Utilities, ou seja, como filha da tabela SAFX3042\. 

Campos a serem adicionados ao arquivo SAFX3043 referente  ao modelo 62: 

__\#__

__Campo__

__Ele__

__Pai__

__Tipo__

__Ocor\.__

__Tam\.__

__Descrição/Observação__

\#

IBSCBS

G

imposto

\-

0\-1

\-

Grupo de informações da Tributação IBS/CBS

1

CST

E

IBSCBS

N

1\-1

3

Código da Situação Tributária do IBS/CBS

2

cClassTrib

E

IBSCBS

N

1\-1

6

Código da Classificação Tributária do IBS/CBS

3

gIBSCBS

G

IBSCBS

\-

0\-1

\-

Grupo de informações específicas do IBS/CBS

4

vBC

E

gIBSCBS

N

1\-1

13,2

Valor da Base de cálculo comum a IBS/CBS

5

gIBSUF

G

gIBSCBS

\-

1\-1

\-

Grupo de informações do IBS/CBS de competência  
das Unidades Federadas

6

pIBSUF

E

gIBSUF

N

1\-1

3,2/3,4

Alíquota do IBS Estadual

7

gDif

G

gIBSUF

\-

0\-1

\-

Grupo de campos do diferimento

8

pDif

E

gDif

N

1\-1

3,2/3,4

Percentual de diferimento

9

vDif

E

gDif

N

1\-1

13,2

Valor do diferimento

10

gDevTrib

G

gIBSUF

\-

0\-1

\-

Grupo de informações da devolução de tributos

11

vDevTrib

E

gDevTrib

N

1\-1

13,2

Valor do tributo devolvido\.  
No fornecimento de energia elétrica, água, esgoto e  
gás natural e em outras hipóteses definidas no  
regulamento

12

gRed

G

gIBSUF

\-

0\-1

\-

Grupo de informações da redução de Alíquota

13

pRedAliq

E

gRed

N

1\-1

3,2/3,4

Percentual da redução de Alíquota do cClassTrib

14

pAliqEfet

E

gRed

N

1\-1

3,2/3,4

Alíquota efetiva do IBS de competência das UF que será aplicada a base de cálculo, incluindo o gCompraGov/pRedutor, se houver\. pAliqEfet = pIBSUF\*\(1 – pRedAliq\)\*\(1 \- gCompraGov/pRedutor\)

15

vIBSUF

E

gIBSUF

N

1\-1

13,2

Valor do IBS de competência da UF

16

gIBSMun

G

gIBSCBS

\-

1\-1

\-

Grupo de informações do IBS/CBS de competência  
do municipio

17

pIBSMun

E

gIBSMun

N

1\-1

3,2/3,4

Alíquota do IBS Municipal

18

gDif

G

gIBSMun

\-

0\-1

\-

Grupo de campos do diferimento

19

pDif

E

gDif

N

1\-1

3,2/3,4

Percentual de diferimento

20

vDif

E

gDif

N

1\-1

13,2

Valor do diferimento

21

gDevTrib

G

gIBSMun

\-

0\-1

\-

Grupo de informações da devolução do tributo

22

vDevTrib

E

gDevTrib

N

1\-1

13,2

Valor do tributo devolvido\. No fornecimento de energia elétrica, água, esgoto e gás natural e em outras hipóteses definidas no regulamento

23

gRed

G

gIBSMun

\-

0\-1

\-

Grupo de informações da redução de Alíquota

24

pRedAliq

E

gRed

N

1\-1

3,2/3,4

Percentual da redução de Alíquota do cClassTrib

25

pAliqEfet

E

gRed

N

1\-1

3,2/3,4

Alíquota efetiva do IBS de competência das UF que será aplicada a base de cálculo, incluindo o gCompraGov/pRedutor, se houver\. pAliqEfet = pIBSUF\*\(1 – pRedAliq\)\*\(1 \- gCompraGov/pRedutor\)

26

vIBSMun

E

gIBSMun

N

1\-1

13,2

Valor do IBS de competência do município

27

gCBS

G

gIBSCBS

\-

1\-1

\-

Grupo de informações da CBS

28

pCBS

E

gCBS

N

1\-1

3,2/3,4

Alíquota da CBS

29

gDif

G

gCBS

\-

0\-1

\-

Grupo de campos do diferimento

30

pDif

E

gDif

N

1\-1

3,2/3,4

Percentual de diferimento

31

vDif

E

gDif

N

1\-1

13,2

Valor do diferimento

32

gDevTrib

G

gCBS

\-

0\-1

\-

Grupo de informações da devolução do tributo

33

vDevTrib

E

gDevTrib

N

1\-1

13,2

Valor da CBS devolvida\. No fornecimento de energia elétrica, água, esgoto e gás natural e em outras hipóteses definidas no regulamento

34

gRed

G

gCBS

\-

0\-1

\-

Grupo de informações da redução de Alíquota

35

pRedAliq

E

gRed

N

1\-1

3,2/3,4

Percentual da redução de Alíquota do cClassTrib

36

pAliqEfet

E

gRed

N

1\-1

3,2/3,4

Alíquota efetiva da CBS que será aplicada a base de cálculo, incluindo o gCompraGov/pRedutor, se houver\. pAliqEfet = pIBSUF\*\(1 – pRedAliq\)\*\(1 \- gCompraGov/pRedutor\)

37

vCBS

E

gCBS

N

1\-1

13,2

Valor da CBS

38

gTribRegular

G

gIBSCBS

\-

0\-1

\-

Grupo de informações da Tributação Regular\.  
Informar como seria a tributação caso não cumprida  
a condição resolutória/suspensiva\. Exemplo 1: Art\.  
442, §4\. Operações com ZFM e ALC\. Exemplo 2:  
Operações com suspensão do tributo\.\.

39

CSTReg

E

gTribRegular

N

1\-1

3

Código da Situação Tributária  
Informado como seria o CST caso não cumprida a  
condição resolutória/suspensiva

40

cClassTribReg

E

gTribRegular

N

1\-1

6

Código de Classificação Tributária  
Informado como seria o cClassTrib caso não  
cumprida a condição resolutória/suspensiva

41

pAliqEfetRegIBSUF

E

gTribRegular

N

1\-1

3,2/3,4

Alíquota efetiva da UF  
Informado a Alíquota caso não cumprida a condição  
resolutória/suspensiva

42

vTribRegIBSUF

E

gTribRegular

N

1\-1

13,2

Informado como seria o valor do Tributo da UF caso  
não cumprida a condição resolutória/suspensiva

43

pAliqEfetRegIBSMun

E

gTribRegular

N

1\-1

3,2/3,4

Alíquota efetiva do Município  
Informado a Alíquota caso não cumprida a condição  
resolutória/suspensiva

44

vTribRegIBSMun

E

gTribRegular

N

1\-1

13,2

Informado como seria o valor do Tributo do  
Município caso não cumprida a condição  
resolutória/suspensiva

45

pAliqEfetRegCBS

E

gTribRegular

N

1\-1

3,2/3,4

Alíquota efetiva da CBS  
Informado a Alíquota caso não cumprida a condição  
resolutória/suspensiva

46

vTribRegCBS

E

gTribRegular

N

1\-1

13,2

Informado como seria o valor do Tributo CBS caso  
não cumprida a condição resolutória/suspensiva

47

gIBSCredPres

G

gIBSCBS

\-

0\-1

\-

Grupo de Informações do Crédito Presumido,  
quando aproveitado pelo emitente do documento\.

48

cCredPres

E

gIBSCredPres

N

1\-1

 

Código do Crédito Presumido \(ver Tabela\)

49

pCredPres

E

gIBSCredPres

N

1\-1

3,2/3,4

Percentual

50

vCredPres

CE

gIBSCredPres

N

1\-1

13,2

Valor do crédito presumido

51

vCredPresCondSus

CE

gIBSCredPres

N

1\-1

13,2

Valor do Crédito Presumido Condição Suspensiva Preencher apenas para cCredPres com indicação de Condição Suspensiva

52

gCBSCredPres

G

gIBSCBS

\-

0\-1

\-

Grupo de Informações do Crédito Presumido,  
quando aproveitado pelo emitente do documento\.

53

cCredPres

E

gCBSCredPres

N

1\-1

 

Código do Crédito Presumido \(ver Tabela\)

54

pCredPres

E

gCBSCredPres

N

1\-1

3,2/3,4

Percentual

55

vCredPres

CE

gCBSCredPres

N

1\-1

13,2

Valor do crédito presumido

56

vCredPresCondSus

CE

gCBSCredPres

N

1\-1

13,2

Valor do Crédito Presumido Condição Suspensiva Preencher apenas para cCredPres com indicação de Condição Suspensiva

57

gTribCompraGov

G

gIBSCBS

\-

0\-1

\-

Grupo de informações da composição do valor do IBS e da CBS em compras governamenta

58

pAliqIBSUF

E

gTribCompraGov

N

1\-1

3,2/3,4

Alíquota IBS da UF utilizada

59

vTribBSUF

E

gTribCompraGov

N

1\-1

13,2

Valor do Tributo do IBS da UF Valor que seria devido a UF, sem aplicação do Art\. 473\. da LC 214/20025

60

pAliqIBSMun

E

gTribCompraGov

N

1\-1

3,2/3,4

Alíquota IBS do Município utilizada

61

vTribIBSMun

E

gTribCompraGov

N

1\-1

13,2

Valor do Tributo do Município da UF Valor que seria devido ao Município, sem aplicação do Art\. 473\. da LC 214/20025

62

pAliqCBS

E

gTribCompraGov

N

1\-1

3,2/3,4

Alíquota IBS do CBS utilizada

63

vTribCBS

E

gTribCompraGov

N

1\-1

13,2

Valor do Tributo da CBS Valor que seria devido a CBS, sem aplicação do Art\. 473\. da LC 214/20025

- 
	1. <a id="_Toc202175085"></a>__NFCom – Modelo 62 | RT – SAFX3007 __

Adicionar ao arquivo SAFX3007 \- Arquivo de Notas Fiscais, os campos para suportar as informações da NFCom\_Nota\_Tecnica\_2025\_001\_RTC\_v1\.05a para o Serviço de Comunicação – Modelo 62 – operações de entradas\.

__Regras__

- Entrada/Saída \(MOVTO\_E\_S\) = 9 e Modelo de Documento \(COD\_MODELO\) = 62\. 

A SAFX3007 suportará apenas as operações de entradas \(prestação de serviço de comunicação\)\. As informações de saídas do serviço de comunicação, serão suportadas nos arquivos SAFX3042 e SAFX3043 conforme os itens 7\.1 e 7\.2\.

- SAFX3008 \- Itens Notas Fiscais Mercadorias e Produtos: adicionar os campos para as informações da NFCom\_Nota\_Tecnica\_2025\_001\_RTC\_v1\.05a para a operação de Serviço de Comunicação – Modelo 62\.
	- 
		1. <a id="_Toc202175086"></a>__NFCom  | Total DFE__

__vTotDFe__ – Total Geral do DFe: Valor total do documento fiscal\. \(vNF \+ total do IBS \+ total da CBS\)

Para carregar as informações da tag vTotDFe, utilizar o campo ?????? da SAFX3007\.

- 
	- 
		1. <a id="_Toc202175087"></a>__NFCom  | Grupo de Totais__

Atribuir  a SAFX3007 \- Arquivo de Notas Fiscais, as informações referente ao Grupo de Totais\. 

![](data:image/png;base64,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)

- 
	- 
		1. <a id="_Toc202175088"></a>__NFCom | Compras Governamentais__

Atribuir SAFX3007 \- Arquivo de Notas Fiscais, as informações referente às operações de Compras Governamentais\. 

![](data:image/png;base64,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)

- 
	1. <a id="_Toc202175089"></a>__NFCom – Modelo 62 | RT – SAFX3008 __

Adicionar ao arquivo SAFX3008 \- Itens Notas Fiscais Mercadorias e Produtos, os campos para suportar as informações da NFCom\_Nota\_Tecnica\_2025\_001\_RTC\_v1\.05a para o Serviço de Comunicação – Modelo 62 – operações de entradas\.

__Regras__

- Entrada/Saída \(MOVTO\_E\_S\) = 9 e Modelo de Documento \(COD\_MODELO\) = 62\. 

A SAFX3007 suportará apenas as operações de entradas \(prestação de serviço de comunicação\)\. As informações de saídas do serviço de comunicação, serão suportadas nos arquivos SAFX3042 e SAFX3043 conforme os itens 7\.1 e 7\.2\.

- SAFX3007 \- Arquivo de Notas Fiscais: a SAFX deverá ser atribuída a Capa de Documentos Fiscais de Utilities, ou seja, como filha da tabela SAFX3007\. 

Campos a serem adicionados ao arquivo SAFX3008 referente  ao modelo 62: 

__\#__

__Campo__

__Ele__

__Pai__

__Tipo__

__Ocor\.__

__Tam\.__

__Descrição/Observação__

\#

IBSCBS

G

imposto

\-

0\-1

\-

Grupo de informações da Tributação IBS/CBS

1

CST

E

IBSCBS

N

1\-1

3

Código da Situação Tributária do IBS/CBS

2

cClassTrib

E

IBSCBS

N

1\-1

6

Código da Classificação Tributária do IBS/CBS

3

gIBSCBS

G

IBSCBS

\-

0\-1

\-

Grupo de informações específicas do IBS/CBS

4

vBC

E

gIBSCBS

N

1\-1

13,2

Valor da Base de cálculo comum a IBS/CBS

5

gIBSUF

G

gIBSCBS

\-

1\-1

\-

Grupo de informações do IBS/CBS de competência  
das Unidades Federadas

6

pIBSUF

E

gIBSUF

N

1\-1

3,2/3,4

Alíquota do IBS Estadual

7

gDif

G

gIBSUF

\-

0\-1

\-

Grupo de campos do diferimento

8

pDif

E

gDif

N

1\-1

3,2/3,4

Percentual de diferimento

9

vDif

E

gDif

N

1\-1

13,2

Valor do diferimento

10

gDevTrib

G

gIBSUF

\-

0\-1

\-

Grupo de informações da devolução de tributos

11

vDevTrib

E

gDevTrib

N

1\-1

13,2

Valor do tributo devolvido\.  
No fornecimento de energia elétrica, água, esgoto e  
gás natural e em outras hipóteses definidas no  
regulamento

12

gRed

G

gIBSUF

\-

0\-1

\-

Grupo de informações da redução de Alíquota

13

pRedAliq

E

gRed

N

1\-1

3,2/3,4

Percentual da redução de Alíquota do cClassTrib

14

pAliqEfet

E

gRed

N

1\-1

3,2/3,4

Alíquota efetiva do IBS de competência das UF que será aplicada a base de cálculo, incluindo o gCompraGov/pRedutor, se houver\. pAliqEfet = pIBSUF\*\(1 – pRedAliq\)\*\(1 \- gCompraGov/pRedutor\)

15

vIBSUF

E

gIBSUF

N

1\-1

13,2

Valor do IBS de competência da UF

16

gIBSMun

G

gIBSCBS

\-

1\-1

\-

Grupo de informações do IBS/CBS de competência  
do municipio

17

pIBSMun

E

gIBSMun

N

1\-1

3,2/3,4

Alíquota do IBS Municipal

18

gDif

G

gIBSMun

\-

0\-1

\-

Grupo de campos do diferimento

19

pDif

E

gDif

N

1\-1

3,2/3,4

Percentual de diferimento

20

vDif

E

gDif

N

1\-1

13,2

Valor do diferimento

21

gDevTrib

G

gIBSMun

\-

0\-1

\-

Grupo de informações da devolução do tributo

22

vDevTrib

E

gDevTrib

N

1\-1

13,2

Valor do tributo devolvido\. No fornecimento de energia elétrica, água, esgoto e gás natural e em outras hipóteses definidas no regulamento

23

gRed

G

gIBSMun

\-

0\-1

\-

Grupo de informações da redução de Alíquota

24

pRedAliq

E

gRed

N

1\-1

3,2/3,4

Percentual da redução de Alíquota do cClassTrib

25

pAliqEfet

E

gRed

N

1\-1

3,2/3,4

Alíquota efetiva do IBS de competência das UF que será aplicada a base de cálculo, incluindo o gCompraGov/pRedutor, se houver\. pAliqEfet = pIBSUF\*\(1 – pRedAliq\)\*\(1 \- gCompraGov/pRedutor\)

26

vIBSMun

E

gIBSMun

N

1\-1

13,2

Valor do IBS de competência do município

27

gCBS

G

gIBSCBS

\-

1\-1

\-

Grupo de informações da CBS

28

pCBS

E

gCBS

N

1\-1

3,2/3,4

Alíquota da CBS

29

gDif

G

gCBS

\-

0\-1

\-

Grupo de campos do diferimento

30

pDif

E

gDif

N

1\-1

3,2/3,4

Percentual de diferimento

31

vDif

E

gDif

N

1\-1

13,2

Valor do diferimento

32

gDevTrib

G

gCBS

\-

0\-1

\-

Grupo de informações da devolução do tributo

33

vDevTrib

E

gDevTrib

N

1\-1

13,2

Valor da CBS devolvida\. No fornecimento de energia elétrica, água, esgoto e gás natural e em outras hipóteses definidas no regulamento

34

gRed

G

gCBS

\-

0\-1

\-

Grupo de informações da redução de Alíquota

35

pRedAliq

E

gRed

N

1\-1

3,2/3,4

Percentual da redução de Alíquota do cClassTrib

36

pAliqEfet

E

gRed

N

1\-1

3,2/3,4

Alíquota efetiva da CBS que será aplicada a base de cálculo, incluindo o gCompraGov/pRedutor, se houver\. pAliqEfet = pIBSUF\*\(1 – pRedAliq\)\*\(1 \- gCompraGov/pRedutor\)

37

vCBS

E

gCBS

N

1\-1

13,2

Valor da CBS

38

gTribRegular

G

gIBSCBS

\-

0\-1

\-

Grupo de informações da Tributação Regular\.  
Informar como seria a tributação caso não cumprida  
a condição resolutória/suspensiva\. Exemplo 1: Art\.  
442, §4\. Operações com ZFM e ALC\. Exemplo 2:  
Operações com suspensão do tributo\.\.

39

CSTReg

E

gTribRegular

N

1\-1

3

Código da Situação Tributária  
Informado como seria o CST caso não cumprida a  
condição resolutória/suspensiva

40

cClassTribReg

E

gTribRegular

N

1\-1

6

Código de Classificação Tributária  
Informado como seria o cClassTrib caso não  
cumprida a condição resolutória/suspensiva

41

pAliqEfetRegIBSUF

E

gTribRegular

N

1\-1

3,2/3,4

Alíquota efetiva da UF  
Informado a Alíquota caso não cumprida a condição  
resolutória/suspensiva

42

vTribRegIBSUF

E

gTribRegular

N

1\-1

13,2

Informado como seria o valor do Tributo da UF caso  
não cumprida a condição resolutória/suspensiva

43

pAliqEfetRegIBSMun

E

gTribRegular

N

1\-1

3,2/3,4

Alíquota efetiva do Município  
Informado a Alíquota caso não cumprida a condição  
resolutória/suspensiva

44

vTribRegIBSMun

E

gTribRegular

N

1\-1

13,2

Informado como seria o valor do Tributo do  
Município caso não cumprida a condição  
resolutória/suspensiva

45

pAliqEfetRegCBS

E

gTribRegular

N

1\-1

3,2/3,4

Alíquota efetiva da CBS  
Informado a Alíquota caso não cumprida a condição  
resolutória/suspensiva

46

vTribRegCBS

E

gTribRegular

N

1\-1

13,2

Informado como seria o valor do Tributo CBS caso  
não cumprida a condição resolutória/suspensiva

47

gIBSCredPres

G

gIBSCBS

\-

0\-1

\-

Grupo de Informações do Crédito Presumido,  
quando aproveitado pelo emitente do documento\.

48

cCredPres

E

gIBSCredPres

N

1\-1

 

Código do Crédito Presumido \(ver Tabela\)

49

pCredPres

E

gIBSCredPres

N

1\-1

3,2/3,4

Percentual

50

vCredPres

CE

gIBSCredPres

N

1\-1

13,2

Valor do crédito presumido

51

vCredPresCondSus

CE

gIBSCredPres

N

1\-1

13,2

Valor do Crédito Presumido Condição Suspensiva Preencher apenas para cCredPres com indicação de Condição Suspensiva

52

gCBSCredPres

G

gIBSCBS

\-

0\-1

\-

Grupo de Informações do Crédito Presumido,  
quando aproveitado pelo emitente do documento\.

53

cCredPres

E

gCBSCredPres

N

1\-1

 

Código do Crédito Presumido \(ver Tabela\)

54

pCredPres

E

gCBSCredPres

N

1\-1

3,2/3,4

Percentual

55

vCredPres

CE

gCBSCredPres

N

1\-1

13,2

Valor do crédito presumido

56

vCredPresCondSus

CE

gCBSCredPres

N

1\-1

13,2

Valor do Crédito Presumido Condição Suspensiva Preencher apenas para cCredPres com indicação de Condição Suspensiva

57

gTribCompraGov

G

gIBSCBS

\-

0\-1

\-

Grupo de informações da composição do valor do IBS e da CBS em compras governamenta

58

pAliqIBSUF

E

gTribCompraGov

N

1\-1

3,2/3,4

Alíquota IBS da UF utilizada

59

vTribBSUF

E

gTribCompraGov

N

1\-1

13,2

Valor do Tributo do IBS da UF Valor que seria devido a UF, sem aplicação do Art\. 473\. da LC 214/20025

60

pAliqIBSMun

E

gTribCompraGov

N

1\-1

3,2/3,4

Alíquota IBS do Município utilizada

61

vTribIBSMun

E

gTribCompraGov

N

1\-1

13,2

Valor do Tributo do Município da UF Valor que seria devido ao Município, sem aplicação do Art\. 473\. da LC 214/20025

62

pAliqCBS

E

gTribCompraGov

N

1\-1

3,2/3,4

Alíquota IBS do CBS utilizada

63

vTribCBS

E

gTribCompraGov

N

1\-1

13,2

Valor do Tributo da CBS Valor que seria devido a CBS, sem aplicação do Art\. 473\. da LC 214/20025

1. <a id="_Toc202175090"></a>__Termo de Aceite – Aprovação__

Aprovações / Responsáveis – cliente

Responsável

Nome

Data

Assinatura

Usuário\-Chave

Aprovações / Responsáveis – Thomson Reuters TAX 

Responsável

Nome

Data

Assinatura

Responsável

Gerente de Projetos

