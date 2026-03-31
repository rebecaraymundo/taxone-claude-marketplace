# MTZ_COPIA_DAS_PARAMETRIZACOES_EXPORTACAO

- **Fonte:** MTZ_COPIA_DAS_PARAMETRIZACOES_EXPORTACAO.docx
- **Modificado:** 2022-12-20
- **Tamanho:** 69 KB

---

THOMSON REUTERS

Cópia de Parametrizações Exportação

__MTZ\_COPIA\_DAS\_PARAMETRIZACOES\_EXPORTACAO __

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-2464

Eric Celestrino

Inclusão do módulo EFD Contribuições na funcionalidade cópia de parâmetros\.

MFS\-2465

Eric Celestrino

Inclusão do módulo EFD Fiscal na funcionalidade cópia de parâmetros\.

MFS\-2466

Eric Celestrino

Inclusão do módulo ECD Contábil na funcionalidade cópia de parâmetros\.

MFS\-2467

Eric Celestrino

Inclusão do módulo EFD Contribuições Financeiras na funcionalidade cópia de parâmetros\.

 

Sumário

[1\.	Regras dos Campos	3](#_Toc445131859)

[2\.	Regras da Exportação	6](#_Toc445131860)

# <a id="_Toc350763252"></a><a id="_Toc445131859"></a>Regras dos Campos 

__Localização da tela: __Básicos >> Ferramentas >> Rotinas Acessórias >> Cópia das Parametrizações >> Exportação

__Título da tela: __Cópia das Parametrizações – Exportação

__Regra Geral:__ Ao final do processo será exibido um relatório com a quantidade de registros gravados para cada parametrização exportada, e a aba Arquivo será habilitada\. Nessa aba o usuário deverá selecionar os arquivos a serem gravados e escolher o diretório onde será feita a gravação\. Para a correta importação dos arquivos posteriormente, o campo "Nome do Arquivo com Nº do Processo" deverá ser desmarcado\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Estabelecimento Origem

Texto

S

Formato:

Combo Box

Default:

Habilitado

Nesse campo o usuário deverá selecionar o estabelecimento que servirá de base para a origem das parametrizações a serem copiadas\.

__Tratamento:__

- Quando o estabelecimento origem não for selecionado, emitir a mensagem de aviso na tela: “Informe Estabelecimento origem\.”;

Filtro por Módulo

Texto

S

S

Formato:

Combo Box

Default:

\*Todos\*

Esse campo lista para o usuário todos os módulos disponíveis para cópia das parametrizações\.

__Conteúdo:__

- \*Todos\*
- CONTROLE OBRIGACOES ESTADUAIS;
- CONTROLE OBRIGACOES FEDERAIS;
- FERRAMENTAS;
- ICMS;
- IPI;
- MEIO MAGNETICO – ICMS;
- OBRIGACOES ACESSRIAS SP;
- OBRIGACOES TRIBUTOS FEDERAIS;
- PARAMETROS;
- EFD CONTRIBUIÇÕES;
- EFD ESCRITURACAO FISCAL DIGITAL;
- ECD ESCRITURACAO CONTABIL DIGITAL;
- EFD CONTRIBUIÇÕES FINANCEIRAS / ASSEMELHADAS;

MFS\-2464

MFS\-2465

MFS\-2466

MFS\-2467

Parâmetros

S

S

Todos não selecionados

Neste quadro estarão listadas todas as parametrizações disponíveis para cópia, onde o usuário deverá selecionar as parametrizações que serão exportadas nessa operação\. 

Para visualizar essa lista, o usuário deverá ter importado a TFIX65 \("Catálogo de Parametrizações para Cópia"\)\.

__Regra:__ Quando no campo <<filtro por módulo>> estiver marcado \*Todos\* deve ser apresentados todas as informações dos módulos disponíveis, quando no campo <<filtro por módulo>> estiver marcando algum módulo específico, as informações apresentadas para a seleção deve ser relacionadas ao módulo selecionado no campo <<filtro por módulo>>\.

__Tratamento:__

- Quando não for selecionado nenhum parâmetro, emitir a mensagem de aviso na tela: “Selecione pelo menos uma opção em Parâmetros\.”;

# <a id="_Toc445131082"></a><a id="_Toc445131860"></a>Regras da Exportação

- 
	- 
		- __Origem das informações para geração:__ TFIX65\.
	- Lista dos módulos a serem considerados na exportação:

__\[ALTERADA – MFS2464/ MFS2465/ MFS2466/ MFS2467/\]__

CONTROLE OBRIGACOES ESTADUAIS;

CONTROLE OBRIGACOES FEDERAIS;

FERRAMENTAS;

ICMS;

IPI;

MEIO MAGNETICO – ICMS;

OBRIGACOES ACESSRIAS SP;

OBRIGACOES TRIBUTOS FEDERAIS;

PARAMETROS;

EFD CONTRIBUIÇÕES;

EFD ESCRITURACAO FISCAL DIGITAL;

ECD ESCRITURACAO CONTABIL DIGITAL;

       EFD CONTRIBUIÇÕES FINANCEIRAS / ASSEMELHADAS;

- __Regra de seleção:__ Para o arquivo SAFPXXXX será recuperada a parametrização do caminho informado na descrição do item de menu da TFIX65 de acordo com cada arquivo e estabelecimento de origem selecionado pelo usuário na tela de geração\.
	- 
		- __Regra de agrupamento:__ Não se aplica\.
		- __Ordenação: __Não se aplica\.

__Campo/Coluna__

__Tipo__

__Formato/Default__

__Regra__

__MFS/CH__

__Dados do Cabeçalho__

Estabelecimento de Origem dos Dados:

Texto

Demonstrar o código e a razão social da empresa de origem selecionada na tela de geração\.

Pág:

Texto

Demonstrar a paginação do relatório, que será demonstrado por estabelecimento\.

__Corpo do Relatório__

Módulo

Texto

Demonstrar o nome do módulo que foi selecionado para exportação\.

Arquivo

Texto

Demonstrar o nome do arquivo que foi selecionado para exportação\.

Parametrização

Texto

Demonstrar o nome da parametrização que foi selecionada para exportação de acordo com o módulo\.

Qtd registros exportados

Texto

Demonstrar a quantidade de registros que foram exportados para cada parametrização\.

__Como realizar a exportação:__

A exportação das parametrizações deve ser feita da seguinte forma:

- Parametrizações por Empresa 🡪 exportar *todos* os registros
- Parametrizações por Estabelecimento 🡪 exportar *apenas* os registros do Estabelecimento de origem informado em tela;  

As parametrizações que trabalham com identificadores internos do Mastersaf deverão ser tratadas internamente para que no arquivo sejam gravados apenas os códigos, assim como ocorre nos arquivos SAFX de importação/exportação\.   

Criação dos Arquivos:

 

A exportação deve ser feita através da criação de arquivos, obedecendo as regras pré\-existentes de framework\.

 

Os arquivos gerados devem ter as iniciais “__SAFP__” seguido da numeração que consta na TFIX\. A coluna “Número do Arquivo” da TFIX servirá para identificar o arquivo que corresponde a cada parametrização\.

Ex:

__SAFP001 \- __Módulo Ferramentas, Parâmetros do Sistema 🡪 Preferências

__SAFP004 \- __Módulo Ferramentas, Parâmetros do Sistema 🡪 Vendas sob Regimes Especiais 🡪 Parâmetros por CFOP

