# MTZ-DW-Manutencao_SAFX431

- **Fonte:** MTZ-DW-Manutencao_SAFX431.docx
- **Modificado:** 2025-05-19
- **Tamanho:** 70 KB

---

THOMSON REUTERS

                                                                  __Módulo DW – Manutenção da SAFX431__

__ __

__                          Tabela dos Itens Negativos dos Documentos Fiscais de Utilities__

__                                       __

__Localização__: Menu Básicos, Módulo: DW, menu Manutenção à Documento Fiscal à Novo Documento Fiscal à Documento Fiscal Utilities

__Aba__: Itens Consolidados \(Conv\. 115/03\)

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS441

Criação da tabela dos itens negativos de Utilities 

Criação da tabela dos itens negativos de Utilities para possibilitar a geração correta do arquivo do Convênio ICMS 115\.

18/01/2014

\(criação do docto\)

MFS\-1079

Atualização da estrutura da tabela

Inclusão de novos campos na tela de manutenção para atendimento ao Convênio 60/2015

08/06/2016

REGRAS DE NEGÓCIO

__RN00__

__Regras gerais__

A tabela SAFX431, assim como a SAFX43, é uma tabela “filha” da SAFX42 \(Capa\-Utilities\), criada na OS4413, para a carga dos itens de dedução \(itens negativos\) dos documentos fiscais de Utilities\. O objetivo é permitir a geração do arquivo do Convênio 115 com todos os itens e valores da nota fiscal “original”, uma vez que esta obrigação é a segunda via do documento, e assim, deve refletir exatamente os dados da nota \(ver detalhes no item “1\-Introdução” da OS4413\)\.

Chave de identificação à Empresa \+ Estabelecimento \+ Data \+ Pessoa Fis/Jur \+ Núm/Sér/Sub Documento \+ Núm do Item 

*\(é a mesma chave da SAFX43\)*

Estrutura da Tabela à vide Manual de Layout 

A seguir estão descritas as regras de funcionamento dos campos tratados na aba “__*Itens Consolidados \(Conv,115/03\)*__”, que correspondem aos campos 09 ao 28 da tabela SAFX431,

Os demais campos \(01 ao 08\) não constam deste documento, pois são os campos de relacionamento com a tabela “mãe” SAFX42, cuja manutenção é feita na aba “Capa”\.

__RN01__

Campo “__Número do Item__”:                     

\(corresponde ao campo “09\-Número do Item” do Manual de Layout\)

Campo obrigatório\.

Sem críticas\.

__RN02__

Campo “__Classificação do Item \(Mercadoria/Serviço\)__”:

\(corresponde ao campo “12\-Classificação do Item \(Mercadoria/Serviço\)” do Manual de Layout\)

Campo obrigatório\.

Este campo é uma lista com as opções:

Mercadoria

Serviço

O default do campo depende do tipo da nota fiscal \(campo “*Class Doc Fiscal*” da capa\), da seguinte forma:

   \- Se classificação da capa = Mercadoria à o campo será inicializado com “Mercadoria” e *não* será habilitado para alteração;

   \- Se classificação da capa = Serviço à  o campo será inicializado com “Serviço” e *não* será habilitado para alteração;

   \- Se classificação da capa = Mercadoria/Serviço à o campo será inicializado com “Mercadoria”, e ficará disponível para alteração;

Os campos do produto e serviço dependerão do conteúdo deste campo, da seguinte forma:

Se conteúdo = ‘1’:

      Neste caso, serão habilitados os campos do Produto \(Indicador e Código\), e desabilitado o campo do Serviço\.

Se conteúdo = ‘2’:

      Neste caso, será habilitado o campo do Serviço, e desabilitados os campos do Produto \(Indicador e Código\)\.

Ao salvar a operação \(botão <Confirma>\), será realizada a seguinte crítica:

 

Se conteúdo = ‘1’ e o produto não estiver preenchido:

      Será exibida a seguinte mensagem de erro, e a operação não será salva: *“O Produto deve ser preenchido”*

Se conteúdo = ‘2’ e o serviço não estiver preenchido:

      Será exibida a seguinte mensagem de erro, e a operação não será salva: *“O Serviço deve ser preenchido”*

__RN03__

Campo “__Número do Item da Consolidação__”:

\(corresponde ao campo “11\-Número do Item da Consolidação” do Manual de Layout\)

Campo obrigatório\.

Ao salvar a operação \(botão <Confirma>\), será realizada a seguinte crítica:

O número do item informado neste campo deve constar do campo “*Número do Item Real*” de algum item da nota \(aba “Item”\)\.

Caso não exista, será exibida a mensagem abaixo e a operação não será salva:

  *“O Número do Item da Consolidação deve constar no campo “Número do Item Real” de algum dos itens da aba Item”*

__RN04__

Campo “__Item de Dedução__”:

\(corresponde ao campo “10\-Indicador de Item de Dedução” do Manual de Layout\)

Campo obrigatório\.

Este campo é uma lista com as opções:

Sim

Não

Opção default = Sim

__RN05__

Campo “__Serviço__”:

\(corresponde ao campo “15\-Código do Serviço” do Manual de Layout\)

Obrigatório apenas quando o campo “Classificação do Item \(Mercadoria/Serviço\)” for = 2 \(vide __RN02__\)\.

Este campo trabalha com janela de seleção dos serviços da tabela SAFX2018, considerando apenas os serviços com validade <= data de emissão da nota\.

Obs: para obter o grupo da SAFX2018 será utilizada a data do campo “Data Emissão/Escr\.Fiscal””\.

Se digitado, será verificada a existência do código informado na SAFX2018, considerando as regras referentes ao grupo e a data de validade\. Se não encontrado, será exibida a mensagem de erro abaixo e a operação não será salva:

*                                                          “Código do Serviço não cadastrado”*

__RN06__

Campo “__Produto__”:

\(corresponde aos campos “13\-Indicador do Produto” e “14\-Código do Produto” do Manual de Layout\)

Obrigatório apenas quando o campo “Classificação do Item \(Mercadoria/Serviço\)” for = 1 \(vide __RN02__\)

Este campo trabalha com janela de seleção dos produtos da tabela SAFX2013, considerando apenas os produtos com validade <= data de emissão da nota\.

Obs: para obter o grupo da SAFX2013 será utilizada a data do campo “Data Emissão/Escr\.Fiscal””\.

Se digitado, será verificada a existência do produto informado na SAFX2013, considerando as regras referentes ao grupo e a data de validade\. Se não encontrado, será exibida a mensagem de erro abaixo e a operação não será salva:

*                                                                       “Produto não cadastrado”*

__RN07__

Campo “__CFOP__”:

\(corresponde ao campo “16\-Código Fiscal” do Manual de Layout\)

Campo não obrigatório\.

Este campo trabalha com janela de seleção dos CFOP’s da tabela SAFX2012, considerando apenas os códigos com validade <= data de emissão da nota\.

Se digitado, será verificada a existência do código informado na SAFX2012, considerando a regra referente à data de validade\. Se não encontrado, será exibida a mensagem de erro abaixo e a operação não será salva:

*                                                                       “CFOP não cadastrado”*

__RN08__

Campo “__Medida__”:

\(corresponde aos campos “17\-Unidade de Medida” do Manual de Layout\)

Campo não obrigatório\.

Este campo trabalha com janela de seleção das unidades de medida da tabela SAFX2007, considerando apenas as unidades com validade <= data de emissão da nota\.

Obs: para obter o grupo da SAFX2007 será utilizada a data do campo “Data Emissão/Escr\.Fiscal””\.

Se digitado, será verificada a existência do código informado na SAFX2007, considerando as regras referentes ao grupo e a data de validade\. Se não encontrado, será exibida a mensagem de erro abaixo e a operação não será salva:

*                                                            “Unidade de Medida não cadastrada”*

__RN09__

Campo “__Valor Serviço”__:

\(corresponde ao campo “21\-Valor do Serviço” do Manual de Layout\)

Campo *não* obrigatório e *sem* críticas\.

__RN10__

Campo “__Valor Outras Despesas”__:

\(corresponde ao campo “22\-Valor Outras Despesas” do Manual de Layout\)

Campo *não* obrigatório e *sem* críticas\.

__RN11__

Campo “__Base ICMS”__:

\(corresponde ao campo “25\-Base Tributada” do Manual de Layout\)

Campo *não* obrigatório e *sem* críticas\.

__RN12__

Campo “__Valor ICMS”__:

\(corresponde ao campo “24\-Valor ICMS” do Manual de Layout\)

Campo *não* obrigatório e *sem* críticas\.

__RN13__

Campo “__Alíquota ICMS”__:

\(corresponde ao campo “23\-Alíquota ICMS” do Manual de Layout\)

Campo *não* obrigatório e *sem* críticas\.

__RN14__

Campo “__B\.Isentas ICMS”__:

\(corresponde ao campo “26\-Base Isenta/Não Tributada” do Manual de Layout\)

Campo *não* obrigatório e *sem* críticas\.

__RN15__

Campo “__B\.Outras ICMS”__:

\(corresponde ao campo “27\-Base Outras” do Manual de Layout\)

Campo *não* obrigatório e *sem* críticas\.

__RN16__

Campo “__B\.Redução ICMS”__:

\(corresponde ao campo “28\-Base de Redução” do Manual de Layout\)

Campo *não* obrigatório e *sem* críticas\.

__RN17__

Campo “__Qtd\. Contratada__”:

\(corresponde ao campo “19\-Quantidade Contratada” do Manual de Layout\)

Campo *não* obrigatório e *sem* críticas\.

__RN18__

Campo “__Qtd\. Fornecida__”:

\(corresponde ao campo “20\-Quantidade Fornecida” do Manual de Layout\)

Campo *não* obrigatório e *sem* críticas\.

__RN19__

Campo “__Classificação do Item \(Conv\.115/03\)__”:

\(corresponde ao campo “18\-Classificação do Item \(Conv\.115/03\)” do Manual de Layout\)

Campo *não* obrigatório e *sem* críticas\.

__RN20__

Campo “__Descrição do Produto/Serviço__”:

\(corresponde ao campo “29\-Descrição do Produto/Serviço” do Manual de Layout\)

Campo *não* obrigatório e *sem* críticas\.

__RN30__

Campo__ “Alíquota PIS”__

__Formato__: Editbox

__Tamanho__: 003V004

__Tipo__: N

Não chave e não obrigatório\.

__RN31__

Campo__ “Vlr\. PIS”__

__Formato__: Editbox

__Tamanho__: 015V002

__Tipo__: N

Não chave e não obrigatório\.

__RN32__

Campo__ “Alíquota COFINS”__

__Formato__: Editbox

__Tamanho__: 003V004

__Tipo__: N

Não chave e não obrigatório\.

__RN33__

Campo__ “Vlr\. COFINS”__

__Formato__: Editbox

__Tamanho__: 015V002

__Tipo__: N

Não chave e não obrigatório\.

__RN34__

Campo__ “Ind\. de Desconto Judicial”__

__Formato__: Radio button

__Tamanho__: 001

__Tipo__: A

Não chave e não obrigatório\.

Conteúdos válidos: S – Sim ou N – Não

Default: N – Não\.

