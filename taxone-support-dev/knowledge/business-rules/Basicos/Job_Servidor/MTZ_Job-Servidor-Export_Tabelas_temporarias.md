# MTZ_Job-Servidor-Export_Tabelas_temporarias

- **Fonte:** MTZ_Job-Servidor-Export_Tabelas_temporarias.docx
- **Modificado:** 2022-04-07
- **Tamanho:** 72 KB

---

<a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>

THOMSON REUTERS

Módulo Job Servidor

__Exportação Dados \- Tabelas Temporárias \(SAFXs\)__

__Localização__: Menu Básicos 🡪 Job Servidor, item de menu Exportação Dados 🡪 Tabelas Temporárias \(SAFXs\)

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS36777

Andréa Rocha

Criação da exportação dos dados das Tabelas Temporárias \(SAFXs\) em formato CSV\.

Sumário

[1\.	Definição:	3](#_Toc47962774)

[2\.	Regras da Tela	3](#_Toc47962775)

[3\.	Regras de Geração dos Arquivos	3](#_Toc47962776)

<a id="_Toc350763252"></a>

# <a id="regras_campos"></a><a id="_Toc47962774"></a>Definição:

O objetivo da rotina de exportação das tabelas temporárias \(SAFXs\) é gravar um arquivo no formato CSV, para cada tabela SAFX selecionada\.  O arquivo será gravado contendo todas as colunas da tabela SAFX, sendo uma linha de cabeçalho e as demais linhas com os dados da tabela\.

Esta rotina foi desenvolvida para os clientes que usam o TAX ONE, pois é uma necessidade dos usuários do produto e que não tem acesso ao banco de dados para consultar os dados carregados nas tabelas SAFX\.

 

# <a id="_Toc47962775"></a>Regras da Tela

As colunas mostradas na tela serão recuperadas da TFIX11 \(Catálogo Prioridade de Importação\), serão demonstradas em uma linha, tabela por tabela, para a seleção do usuário\.  Somente serão mostradas as tabelas \(SAFX\) que possuírem informações carregadas no banco de dados\. 

A tela terá a opção de pesquisar a tabela SAFX a ser gerada e também a opção de marcar/ desmarcar todas as tabelas para a geração\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Regra__

Grupo

Numérico

S

N

Neste campo será mostrada a coluna GRUPO\_ARQUIVO\.

Número

Numérico

S

N

Neste campo será mostrada a coluna NUMERO\_ARQUIVO\.

Descrição

Alfanumérico

S

N

Neste campo será mostrada a coluna DESCRICAO\_ARQUIVO\.

Tabela Temp\.

Alfanumérico

S

N

Neste campo será mostrada a coluna NOM\_TAB\_WORK

Núm\. de Registros

Alfanumérico

S

N

Neste campo será mostrada a quantidade total de registros carregados para cada SAFX\.  Será feita uma contagem de quantos registros existem carregados para cada tabela SAFX\.

# <a id="_Toc427766287"></a><a id="_Toc453687763"></a><a id="_Toc47962776"></a>Regras de Geração dos Arquivos

Para cada tabela SAFX selecionada para a geração, deve ser gravado um arquivo contendo todas as colunas da tabela SAFX, no formato CSV\.

A montagem das colunas de cada arquivo é feita com base na TFIX96 \(Tabela com o layout da carga para tabelas SAFX, conforme manual de layout\), que contém todas as colunas existentes na tabela SAFX\.  A montagem do arquivo segue a ordem dos campos de cada tabela SAFX, da seguinte forma:

Nome do arquivo a ser gerado: campo NOM\_TAB\_WORK

Ordem da coluna no arquivo: campo NUM\_CAMPO

Nome da coluna do arquivo: campo NOME\_CAMPO

__Obs\.:__  Os arquivos são gravados no Oracle Directory informado\.   Para utilização do Oracle Directory o usuário deve\-se cadastrar um diretório no módulo Ferramentas, Menu: Parâmetros do Sistema >> Cadastro de Diretórios do Servidor com o parâmetro Módulo = “Job Servidor”\.  Após cadastrar um diretório no Job Servidor, o usuário informa no campo “Diretório” o diretório cadastrado em Ferramentas\.

