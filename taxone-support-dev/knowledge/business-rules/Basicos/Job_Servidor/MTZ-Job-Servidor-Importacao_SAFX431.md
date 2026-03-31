# MTZ-Job-Servidor-Importacao_SAFX431

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX431.docx
- **Modificado:** 2025-07-15
- **Tamanho:** 86 KB

---

THOMSON REUTERS

           __Módulo Job Servidor – Tabela dos Itens Negativos dos Documentos Fiscais de Utilities__

__                                                                   __

__                                                                       \(SAFX431\)__

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS4413

Criação da tabela dos itens negativos de Utilities 

Criação da tabela dos itens negativos de Utilities para possibilitar a geração correta do arquivo do Convênio ICMS 115\.

18/01/2014

\(criação do docto\)

MFS\-1079

Atualização da tabela

Criação de campos para atender ao Convênio ICMS 60/2015\.

08/06/2016

REGRAS DE NEGÓCIO

__RN00__

__Regras gerais__

A tabela SAFX431, assim como a SAFX43, é uma tabela “filha” da SAFX42 \(Capa\-Utilities\), criada na OS4413, para a carga dos itens de dedução \(itens negativos\) dos documentos fiscais de Utilities\. O objetivo é permitir a geração do arquivo do Convênio 115 com todos os itens e valores da nota fiscal “original”, uma vez que esta obrigação é a segunda via do documento, e assim, deve refletir exatamente os dados da nota \(ver detalhes no item “1\-Introdução” da OS4413\)\.

Chave de identificação à Empresa \+ Estabelecimento \+ Data \+ Pessoa Fis/Jur \+ Núm/Sér/Sub Documento \+ Núm do Item 

*\(é a mesma chave da SAFX43\)*

Estrutura da Tabela à vide Manual de Layout 

__RN01__

Campo “__Código da Empresa__”:

Campo obrigatório\.

Verifica o preenchimento do campo\. Caso não preenchido, será gravada a mensagem de erro padrão no log da importação \(mensagem 90001 da TFIX22\)\.

__RN02__

Campo “__Código do Estabelecimento__”:

Campo obrigatório\.

Verifica o preenchimento do campo\. Caso não preenchido, será gravada a mensagem de erro padrão no log da importação \(mensagem 90002 da TFIX22\)\.

__RN03__

Campo “__Data da Emissão/Escrita Fiscal__”:

Campo obrigatório\.

Verifica o preenchimento do campo\. Caso não preenchido, será gravada a mensagem de erro padrão no log da importação \(mensagem 90131 da TFIX22\)\.

Verifica a validade da data\. Se inválida, será gravada a mensagem de erro padrão no log da importação \(mensagem 90209 da TFIX22\)\.

__RN04__

Campo “__Indicador da Pessoa Fis/Jur__”:

Campo obrigatório\.

Verifica o preenchimento do campo e a validade dos indicadores conforme os indicadores da SAFX04\. Caso não preenchido ou inválido, será gravada a mensagem de erro padrão no log da importação \(mensagem 90088 da TFIX22\)\.

__RN05__

Campo “__Código da Pessoa Fis/Jur__”:

Campo obrigatório\.

Verifica o preenchimento do campo, e se não preenchido, será gravada a mensagem de erro padrão no log da importação \(mensagem 90089 da TFIX22\)\.

Verifica a existência da pessoa na SAFX04, com validade <= a data de emissão do documento \(campo “Data Emissão/Escr\.Fiscal”\)\. Caso não exista, será gravada a mensagem de erro padrão no log da importação \(mensagem 90124 da TFIX22\)\.

Obs: para obter o grupo da pessoa fis/jur será utilizada a data do campo “Data de Emissão/Escr\.Fiscal”

__RN06__

Campo “__Número do Documento Fiscal__”:

Campo obrigatório\.

Verifica o preenchimento do campo, e se não preenchido, será gravada a mensagem de erro padrão no log da importação \(mensagem 90112 da TFIX22\)\.

__RN07__

Campo “__Série do Documento Fiscal__”:

Campo não obrigatório\.

Quando não preenchido, será gravado um caracter branco, procedimento padrão das tabelas de documentos fiscais\.  

__RN08__

Campo “__Subsérie do Documento Fiscal__”:

Campo não obrigatório\.

Quando não preenchido, será gravado um caracter branco, procedimento padrão das tabelas de documentos fiscais\. 

Após a validação dos campos 01 ao 08, será verificada a existência da capa do documento informado na tabela SAFX42, a partir dos campos chave da tabela\. Se não identificado, será gravada a mensagem de erro padrão no log da importação \(mensagem 92496 da TFIX22\)\.

__RN09__

Campo “__Número do Item__”:

Campo obrigatório\.

Verifica o preenchimento do campo, e se não preenchido, será gravada a mensagem de erro padrão no log da importação \(mensagem 90132 da TFIX22\)\.

__RN10__

Campo “__Indicador de Item de Dedução__”:

Campo obrigatório\.

Este campo deve estar preenchido com os valores ‘S’ ou ‘N’, caso contrário, será gravada a seguinte mensagem de erro no log da importação:

                          *“O campo Indicador de Item de Dedução deve ser preenchido com ‘S’ ou ‘N’”*

 

__RN11__

Campo “__Número do Item da Consolidação__”:

Campo obrigatório\.

Verifica o preenchimento do campo:

Se o campo não estiver preenchido, será gravada a seguinte mensagem de erro no log da importação:

                          *“O campo Número do Item da Consolidação é de preenchimento obrigatório’”*

Verifica se o item informado existe em algum item da SAFX43 como “Número do Item Real” \(campo 110\):

A pesquisa irá verificar se existe algum item na SAFX43 com o campo “*110\-Número do Item Real*” igual ao número de item informado neste campo\.

Caso não exista, será gravada a seguinte mensagem de erro no log da importação: “*O “Número do Item da Consolidação” informado não corresponde a nenhum número do item real \(campo 110\) da Tabela dos Itens \(SAFX43\)*”

__RN12__

Campo “__Classificação do Item \(Mercadoria/Serviço\)__”:

Campo obrigatório\.

__Crítica 1:__

Este campo deve estar preenchido com os valores ‘1’ \(Mercadoria\) ou ‘2’ \(Serviço\), caso contrário, será gravada a seguinte mensagem de erro no log da importação: *“O campo “*Classificação do Item \(Mercadoria/Serviço\)__”__* deve ser preenchido com ‘1’ ou ‘2’”*

__Crítica 2:__

A classificação informada deve estar de acordo com a classificação informada na nota fiscal \(campo 50 da SAFX42\), da seguinte forma:

Se classificação da nota = 1 \(Mercadoria\) à neste caso, a classificação dos itens só pode ser = 1 \(Mercadoria\);

Se classificação da nota = 2 \(Serviço\) à neste caso, a classificação dos itens só pode ser = 2 \(Serviço\);

Se classificação da nota = 3 \(Mista\) à neste caso, a classificação dos itens pode ser = 1 \(Mercadoria\) ou 2 \(Serviço\);

Caso a classificação do item não esteja de acordo com a regra acima, será gravada a seguinte mensagem no log da

importação: *“Atenção, documentos classificados como mercadoria, ou servico, nao podem possuir itens com classificacoes diferentes”  \(mensagem de erro código 906132, já existente na TFIX22\)*

__Crítica 3:__

Se conteúdo = ‘1’, será verificado o preenchimento dos campos “13\-Indicador do Produto” e “14\-Código do Produto”:

      Neste caso, tanto o indicador como o código do produto devem estar preenchidos\. Caso contrário, será gravada a

      seguinte mensagem no log da importação:

       *“Quando classificação do item = 1 \(Mercadoria\) é obrigatório o preenchimento do indicador e código do produto”*

Se conteúdo = ‘2’, será verificado o preenchimento do campo “15\-Código do Serviço”:

      Neste caso, o código do serviço deve estar preenchido\. Caso contrário, será gravada a seguinte mensagem no log da

      importação:

            *“Quando classificação do item = 2 \(Serviço\) é obrigatório o preenchimento do código do serviço”*

__RN13__

Campo “__Indicador do Produto__”:

Campo não obrigatório\.

Se preenchido, seu conteúdo deve estar de acordo com os indicadores de produto da SAFX2013\. Caso contrário, será gravada a seguinte mensagem de erro no log da importação:

  *“Campo Indicador do Produto inválido\. Preencher de acordo com os indicadores da Tabela de Produtos \(SAFX2013\)’”*

__RN14__

Campo “__Código do Produto__”: 

Campo não obrigatório\.

Quando informado,  será verificada a existência do produto na Tabela de Produtos \(SAFX2013\) , com validade <= a data de emissão do documento \(campo “Data Emissão/Escr\.Fiscal”\)\. Se não encontrado, será gravada mensagem de erro padrão no log da importação \(mensagem 90034 da TFIX22\)\.

Obs: para obter o grupo da SAFX2013 será utilizada a data do campo “Data de Emissão/Escr\.Fiscal”\.

__RN15__

Campo “__Código do Serviço__”:

Campo não obrigatório\.

Quando informado, será verificada a existência do serviço na Tabela dos Códigos de Serviço \(SAFX2018\) , com validade <= a data de emissão do documento \(campo “Data Emissão/Escr\.Fiscal”\)\. Se não encontrado, será gravada a seguinte mensagem de erro no log da importação:

*                         “Código do Serviço não cadastrado na Tabela de Códigos de Serviço \(SAFX2018\)”*

Obs: para obter o grupo da SAFX2018 usar a data do campo “Data de Emissão/Escr\.Fiscal”\.

__RN16__

Campo “__Código Fiscal__”:

Campo não obrigatório\.

Quando informado, será verificada a existência do código na Tabela dos CFOP’s \(SAFX2012\), com validade <= a data de emissão do documento \(campo “Data Emissão/Escr\.Fiscal”\)\. Se não encontrado, será gravada a mensagem de erro padrão no log da importação \(mensagem 90029 da TFIX22\)\.

__RN17__

Campo “__Unidade de Medida__”:

Campo não obrigatório\.

Quando informado, será verificada a existência do código na Tabela de Medidas \(SAFX2007\), com validade <= a data de emissão do documento \(campo “Data Emissão/Escr\.Fiscal”\)\. Se não encontrado, será gravada a mensagem de erro padrão no log da importação \(mensagem 50383 da TFIX22\)\.

Obs: para obter o grupo da SAFX2007 usar a data do campo “Data de Emissão/Escr\.Fiscal”\.

__RN18__

Campo “__Classificação do Item \(Conv\.115/03\)__”:

Campo *não* obrigatório e *sem* críticas\.

__RN19__

Campo “__Quantidade Contratada__”:

Campo *não* obrigatório e *sem* críticas\.

__RN20__

Campo “__Quantidade Fornecida__”:

Campo *não* obrigatório e *sem* críticas\.

__RN21__

Campo “__Valor do Serviço”__:

Campo *não* obrigatório e *sem* críticas\.

__RN22__

Campo “__Valor Outras Despesas”__:

Campo *não* obrigatório e *sem* críticas\.

__RN23__

Campo “__Alíquota ICMS”__:

Campo *não* obrigatório e *sem* críticas\.

__RN24__

Campo “__Valor ICMS”__:

Campo *não* obrigatório e *sem* críticas\.

__RN25__

Campo “__Base Tributada”__:

Campo *não* obrigatório e *sem* críticas\.

__RN26__

Campo “__Base Isenta/Não Tributada”__:

Campo *não* obrigatório e *sem* críticas\.

__RN27__

Campo “__Base Outras”__:

Campo *não* obrigatório e *sem* críticas\.

__RN28__

Campo “__Base de Redução”__:

Campo *não* obrigatório e *sem* críticas\.

__RN29__

Campo “__Descrição do Produto/Serviço”__:

Campo *não* obrigatório e *sem* críticas\.

__RN30__

__Item__:__ __A ser definido pelo A&D

__Nome do Campo__: Será definido pelo A&D

__Descrição__: Alíquota PIS

__Tamanho__: 003V004

__Tipo__: N

Não chave e não obrigatório

__RN31__

__Item__:__ __A ser definido pelo A&D

__Nome do Campo__: Será definido pelo A&D

__Descrição__: Valor do PIS

__Tamanho__: 015V002

__Tipo__: N

Não chave e não obrigatório

__RN32__

__Item__:__ __A ser definido pelo A&D

__Nome do Campo__: Será definido pelo A&D

__Descrição__: Alíquota COFINS 

__Tamanho__: 003V004

__Tipo__: N

Não chave e não obrigatório

__RN33__

__Item__:__ __A ser definido pelo A&D

__Nome do Campo__: Será definido pelo A&D

__Descrição__: Valor COFINS

__Tamanho__: 015V002

__Tipo__: N

Não chave e não obrigatório

__RN34__

__Item__:__ __A ser definido pelo A&D

__Nome do Campo__: Será definido pelo A&D

__Descrição__: Indicador de Desconto Judicial

__Tamanho__: 001

__Tipo__: A

Não chave e não obrigatório

O conteúdo do campo deve ser igual a S – Sim ou N – Não\. Se na interface estiver nulo, assumir como conteúdo padrão “N”\. Se for informado um conteúdo diferente dos válidos, retornar mensagem de erro: “Indicador de Desconto Judicial inválido\. Informe <S> ou <N>”\.

