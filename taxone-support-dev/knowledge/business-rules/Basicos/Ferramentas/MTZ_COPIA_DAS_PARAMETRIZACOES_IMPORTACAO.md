# MTZ_COPIA_DAS_PARAMETRIZACOES_IMPORTACAO

- **Fonte:** MTZ_COPIA_DAS_PARAMETRIZACOES_IMPORTACAO.docx
- **Modificado:** 2024-06-26
- **Tamanho:** 71 KB

---

6

THOMSON REUTERS

Cópia de Parametrizações Importação

__MTZ\_COPIA\_DAS\_PARAMETRIZACOES\_IMPORTACAO__

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

MFS36444

Andréa Rochca

Retirada do campo “Diretório Oracle de origem” da tela para o TAX ONE\.

Sumário

[1\.	Regras dos Campos	3](#_Toc445131081)

[2\.	Regras da Importação	5](#_Toc445131082)

# <a id="_Toc350763252"></a><a id="_Toc445131081"></a>Regras dos Campos 

__Localização da tela: __Básicos >> Ferramentas >> Rotinas Acessórias >> Cópia das Parametrizações >> Importação

__Título da tela: __Cópia das Parametrizações – Importação

__Regra Geral:__ Ao final do processo será exibido um relatório com a quantidade de registros lidos, importados, rejeitados e ignorados para cada parametrização importada\. *Obs\.:* Os registros rejeitados \(erros\) não serão gravados, as mensagens de erro podem ser consultadas após o término do processo através da aba Log\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Diretório Oracle de origem

Texto

S

S

Formato:

Text Input

Default:

Habilitado

Nesse campo o usuário informará o diretório onde foram gravados os arquivos gerados na exportação de parametrizações\.

__Tratamento:__

- Quando o campo não for preenchido, emitir a mensagem de aviso na tela: “Informe Diretório Oracle de origem\.”;

__\[MFS36444\] __Retirada do campo

Este campo não deve ser mostrado quando esta rotina for utlizada pelo TAX ONE\.  

Para importar os arquivos do TAX ONE, o usuário deve cadastrar o directory no módulo ferramentas, menu Parâmetros do Sistema > Cadastro de Diretório do Servidor\.

MFS36444

Limpar parametrizações já existentes? \(somente p/ grp\.2\-Estabelecimento Origem\)

Texto

N

S

Formato:

Check Box

Default:

Habilitado e Desmarcado

O usuário deve utilizar essa opção caso queira que antes de iniciar a importação dos dados, o sistema limpe todos os dados das parametrizações em questão que eventualmente já tenham sido parametrizados no\(s\) estabelecimento\(s\) de destino\. 

Essa funcionalidade está disponível para os parâmetros cujo tipo de exportação seja "2\-Estabelecimento Origem", exceto para o item de parametrização Obrigações >> Central de Escrituração \(SAFP0027\)\.

Estabelecimentos de Destino

Texto

S

S

Formato:

Check Box

Default:

Habilitado e Desmarcado

Nesse quadro, o usuário deverá selecionar os estabelecimentos de destino das parametrizações a serem importadas\.

Tratamento:

- Quando nenhum estabelecimento for marcado, emitir a mensagem de aviso na tela: “Selecione pelo menos uma opção em Estabelecimentos de Destino\.”;

Parâmetros

Texto

S

S

Formato:

Check Box

Default:

Habilitado e Desmarcado

Nesse quadro serão exibidos todos os menus disponíveis para importação \(de acordo com a TFIX65\), assim como o nome dos arquivos e suas características\. 

__Tratamento:__

- Quando nenhum parâmetro for marcado, emitir a mensagem de aviso na tela: “Selecione pelo menos uma opção em Parâmetros\.”;

# <a id="_Toc445131082"></a>Regras da Importação

- 
	- 
		- __Origem das informações para geração:__ TFIX65, arquivos extraídos de Cópia das Parametrizações – Exportação\.
	- Lista dos módulos a serem considerados na importação:

__\[ALTERADA – MFS2464/ MFS2465/ MFS2466/ MFS2467\]__

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

- 
	- 
		- __Regra de seleção:__ 
			- Para o arquivo SAFPXXXX será recuperada a parametrização do caminho informado na descrição do item de menu da TFIX65 de acordo com cada arquivo e estabelecimento de origem selecionado pelo usuário na tela de geração;
		- __Regra de agrupamento:__ Não se aplica\.
		- __Ordenação: __Não se aplica\.
		- __Regra Geral:__
			- Ao final do processo, a importação deve gerar um relatório com informações básicas sobre os dados importados\. Para cada parametrização importada, mostrar a quantidade de registros lidos, gravados, rejeitados, atualizados e ignorados\.
			- O relatório deve demonstrar os dados por Estabelecimento \(estabelecimento a estabelecimento de destino que recebeu a cópia das parametrizações\);
			- No caso das parametrizações que são por Empresa, as informações aparecerá somente uma única vez, associadas à Empresa;

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

Qtd registros lidos

Texto

Demonstrar a quantidade de registros lidos no arquivo texto \(da parametrização em questão\)\.

Qtd registros importados

Texto

Demonstrar a quantidade de registros gravados\.

Qtd registros rejeitados \(erro\)

Texto

Demonstrar a quantidade de registros que não foram importados porque ocorreu algum erro na crítica dos seus dados\.

Qtd registros atualizados

Texto

Demonstrar a quantidade de registros que já existiam na base de destino, mas tiveram alguma informação atualizada\.

Qtd registros ignorados

Texto

Demonstrar a quantidade de registros que foram ignorados, pois já existiam na base de destino e estavam idênticos\.

Status

Texto

Demonstrar o status da importação da parametrização em questão \(“Ok” ou “Erro”\)\.

__Como realizar a importação:__

A importação das parametrizações deve ser feita da seguinte forma:

 

- Parametrizações por Empresa à importar todos os registros
- Parametrizações por Estabelecimento à importar os dados da parametrização *para todos os estabelecimentos selecionados em tela* 

__Atualização dos Dados:__

No caso dos registros a serem importados que já existam na base de destino, deverá ser feita a atualização dos dados sempre que houver alguma diferença, ou então, o registro será ignorado se for idêntico ao já existente\.

__Críticas a serem realizadas na importação:__

Os registros que tiverem problemas na validação __*não serão gravados*__ e no log será gravada uma mensagem de erro\.

Sobre a validação dos grupos, datas de validade e códigos:

Grupo de Relacionamento:

Nas parametrizações que têm somente o grupo de relacionamento \(sem data de validade\), deve ser verificado:

\-Verificar se existe o grupo e o relacionamento entre o Grupo e o  Estabelecimento para o qual esta sendo realizada a importação

Msg à  “Grupo de Relacionamento \[xxxxxxxxx\] não cadastrado”

Ou

Msg à   “Não existe relacionamento entre o Grupo e o Estabelecimento \[xxxxxxxxx/xxxxxx\]”

Datas de Validade:

Nas parametrizações que têm grupo de relacionamento e data de validade, deve ser verificado:

\-Fazer a mesma validação descrita acima, só que considerando a data de validade, ou seja: verificar se existe relacionamento entre o Grupo x Estabelecimento x Tabela  \(estabelecimento *para o qual esta sendo feita a cópia\.\)* com uma data de validade que seja < = a data de validade do registro\. 

O objetivo desta verificação é evitar a inclusão de um registro com uma determinada data de validade, sem que na época existisse o relacionamento entre o Grupo x Estabelecimento x Tabela\. 

Msg à “Não existe relacionamento Grupo x Estabelecimento x Tabela válido para esta data de validade \[xxxxxxxxx/xxxxxx/99/99/9999\]”

Códigos:

As parametrizações que trabalham com códigos \(fornecedores, clientes, produtos, unidade de medida, NBM, CFOP etc\.\.\. \), devem verificar se o código em questão já existe na tabela correspondente\. Quando não existir, o registro não poderá ser importado para não causar uma inconsistência na base de dados\. Neste caso o log deve mostrar uma mensagem de erro conforme os exemplos abaixo:

Exemplos:

  

Indicador/Código do Produto \[X / XXXXXXXXXXXXXXXXXXXXX\] não cadastrado\. 

Indicador/Pessoa física/jurídica \[X / XXXXXXXXXXXXXXXXXXXXXX\] não cadastrada\. 

Código da unidade de medida \[XXXXXXX\] não cadastrado\. 

__Sobre a descrição das mensagens de erro:__

Como a quantidade da parametrizações a serem tratadas é muito grande, o requisito não cita a descrição exata de cada mensagem de erro, pois seria uma relação muito grande\.

O importante é que sejam implementadas todas as críticas solicitadas e que o log mostre claramente *as seguintes informações* para cada mensagem de erro:

\-Módulo e parametrização em questão

\-Descrição do erro

\-Identificação do registro onde ocorreu o erro\.

