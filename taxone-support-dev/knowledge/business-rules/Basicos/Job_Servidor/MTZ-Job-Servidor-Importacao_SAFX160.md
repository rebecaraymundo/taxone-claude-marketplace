# MTZ-Job-Servidor-Importacao_SAFX160

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX160.docx
- **Modificado:** 2022-09-19
- **Tamanho:** 83 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX160

__Tabela Processo Referenciado – F111__

__                                                           \(SPED Contribuições F111\)__

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS\-62826

Alessandra Cristina Navatta

Criação da SAFX160, para carregar as informações de processos referenciados – F111 \(SPED Contribuições\)

15/04/2021

MFS83787

Alteração p/ Campo Não Obrigatório 

Alteração do Campo 03 – Tipo de Documento para Campo não obrigatório\.

18/05/2022

## REGRAS DE NEGÓCIO

#### Cód\.

### MFS

__RN00__

__Regras gerais__

__Estrutura da tabela SAFX160__ 🡪 vide manual de layout

A SAFX160 é uma tabela complementar da SAFX147 \(Demais documentos e Operações Geradoras de crédito\)\.

__Campos que compõe a chave da tabela: __Os campos chave são os mesmos campos que compõem a chave da X147, por se tratar de uma tabela complementar\.

A manutenção da tabela é feita na tela de manutenção Demais Documentos e Operações Geradoras de Crédito F100 \(módulo SPED Contribuições\), através da opção “F111 – Processos Referenciado__*\)*__”\.

As informações da SAFX160 são utilizadas na geração do Sped Contribuições, registro F111\.

__Crítica da existência do Registro Pai:__

Por se tratar de uma tabela complementar à SAFX147, só é permitida a inclusão de informações dos processos referenciados na SAFX260 quando os demais documentos e operações geradoras de crédito do registro F100 já existir\. Assim, após a validação dos campos de identificação dos demais documentos \(campo 01 ao 14\) conforme as regras descritas abaixo, será verificado se o item em questão existe na SAFX147\. Caso não exista, o registro *não* será importado, e no log de erros será gravada uma mensagem de erro *\(“Nao existe o registro correspondente na SAFX147 para o processo referenciado informado\.”\)\. *

__Sobre as mensagens de erro:__

Todas as mensagens gravadas no log de erros da importação, devem mostrar os dados de identificação do registro pai, para permitir ao usuário a identificação do registro com erro\.

MFS\-62826

__RN01__

__Campo 01 \- Código da empresa__

 

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Código da empresa na tabela SAFX160\.

__Tabela: __SAFX160

__Item: __01

__Nome do Campo: __COD\_EMPRESA

__Descrição: __Código da empresa

__Tipo:__ A

__Tamanho: __003

__Comentário: __Campo destinado ao código da Empresa\.

__Chave Primária__

MFS\-62826

__RN02__

__Campo 02 \- Código do estabelecimento__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Código do estabelecimento na tabela SAFX160\.

__Tabela: __SAFX160

__Item: __02

__Nome do Campo: __COD\_ESTAB

__Descrição: __Código do estabelecimento

__Tipo:__ A

__Tamanho: __006

__Comentário: __Campo destinado ao código do Estabelecimento\.

__ Chave Primária__

MFS\-62826

__RN03__

__Campo 03 \- Tipo de documento__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Tipo de documento na tabela SAFX160\.

__Tabela: __SAFX160

__Item: __03

__Nome do Campo: __COD\_DOCTO

__Descrição: __Código do documento

__Tipo:__ A

__Tamanho: __005

__Conteúdo do Campo: __Campo destinado ao código do documento da SAFX2005\.__ __

__Chave Primária__

MFS\-62826

__RN04__

__Campo 04 \- Indicador da Pessoa física/Jurídica__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Indicador da Pessoa física/Jurídica na tabela SAFX160\.

__Tabela: __SAFX160

__Item: __04

__Nome do Campo: __IND\_FIS\_JUR

__Descrição:__ Indicador de Pessoa Física/Jurídica

__Tipo:__ A

__Tamanho: __1

__Comentário: __Campo que deverá ser preenchido com o Indicador de Pessoa Física/Jurídica

 relacionada na Tabela de Pessoa Física/Jurídica \(SAFX04\), conforme segue:

1 \- Fornecedor;

2 \- Cliente;

3 \- Estabelecimento;

4 \- Transportadora;

5 \- Cliente/Fornecedor/Transportadora\.

__Chave Primária__

__Não Obrigatório__

MFS\-62826

__RN05__

__Campo 05 \- Código/Destinatário/Emitente/ Remetente__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Código/Destinatário/Emitente/ Remetente na tabela SAFX160\.

__Tabela: __SAFX160

__Item: __05

__Nome do Campo: __COD\_FIS\_JUR

__Descrição:__ Código/Destinatário/Emitente/ Remetente

__Tipo:__ A

__Tamanho: __060

__Comentário: __

Deve estar registrado na Tabela de Pessoa Física/Jurídica \(SAFX04\)\. Quando se tratar de Outros Documentos Fiscais, tais como Resumo de ECF ou por Ciclo de Faturamento de Telecomunicações, Energia Elétrica e Gás Canalizado pode\-se informar o Código do Estabelecimento\. Outra questão a ser levantada, é que o Cliente MasterSAF, pode tratar este Código seja ele Um Código Interno, ou sejam os Códigos de Cadastros na SRF se for CPF ou MF se for um CNPJ\. Ou seja, se o Sistema transacional trabalhar com CFP e CNPJ, estes códigos também poderão ser os CFP e CNPJ\. É recomendável que o tratamento seja o mesmo do Sistema transacional para evitar transtornos, embora qualquer solução atenderá ao Fisco, seja código Interno ou Códigos de Cadastros na SRF e MF\.  
Observação: Para o Convênio 51/00, este campo deve ser preenchido da seguinte forma:  
• Faturamento Direto para Leasing \- preencher com o Destinatário da Nota Fiscal de Leasing, no caso a Financeira do Veículo;  
• Faturamento Direto \- preencher com o Dealer de Entrega do Veículo \(Concessionária\)\.

__   Chave Primária__

__   Não Obrigatório__

MFS\-62826

__RN06__

__Campo 06 \- Indicador do Produto__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Indicador do Produto na tabela SAFX160\.

__Tabela: __SAFX160

__Item: __06

__Nome do Campo: __IND\_PRODUTO

__Descrição: __Indicador do Produto

__Tipo:__ A

__Tamanho: __001

__Comentário: __

Identificadores:  
1 \- Produto Acabado;  
2 \- Insumos;  
3 \- Embalagem;  
4 \- Consumo;  
5 \- Outros;  
6 \- Em Elaboração;  
7 \- Intermediário;  
8 \- Miscelâneas\.  
Esta Discriminação para Identificar a Mercadoria se é Produto Acabado, Insumo, Produto em Elaboração, não é mais solicitada pela IN SRF 86/01, porém é obrigatória para outras obrigações da RIPI, tal como o Inventário, por isso, deve continuar a atender a SRF\. Obs: O preenchimento dos campos 13 e 14 exclui o preenchimento dos campos 15 e 16, e vice\-versa\.

__Chave Primária__

__Não Obrigatório__

MFS\-62826

__RN07__

__Campo 07 \- Produto__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Produto na tabela na tabela SAFX160\.

__Tabela: __SAFX160

__Item: __07

__Nome do campo: __COD\_PRODUTO

__Descrição: __Produto

__Tipo:__ A

__Tamanho: __035

__Conteúdo do Campo: __

Informar o Código do Produto/Mercadoria, de acordo com  as solicitações da dos Convênios ICMS, RIPI e IN SRF, devidamente registradas na Tabela de Produto \(SAFX2013\)\. Esta codificação de mercadorias/produtos deve representar os códigos dos registrados nos sistemas corporativos e nos sistemas de faturamento \(Billing\)\. Assim, para simples ilustração podemos citar que para empresas industriais e comerciais, devem ser informados os códigos internos, para telecomunicações, os serviços que especificam os tipos de ligações, etc\. Para o registro do “Resumo Diário” e Outros Resumos referentes a outros Modelos de Documentos Fiscais, não existe a exigência de Códigos específicos, bem como para registrar aquisições de Bens do Ativo e/ou as Alienações\. Por isso, para cada Tipo de Modelo de Documento Fiscal, deve ser definido os critérios  e os códigos a serem utilizados e analisar se as Legislações requerem ou não Códigos para o Atendimento a Escrituração, Meios Magnéticos e Obrigações Acessórias\. Obs: O preenchimento dos campos 13 e 14 exclui o preenchimento dos campos 15 e 16, e vice\-versa\.

__Chave Primária__

__Não Obrigatório__

MFS\-62826

__RN08__

__Campo 08 – Data da Operação__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Data da Operação na tabela SAFX160\.

__Tabela: __SAFX160

__Item: __08

__Nome do campo: __DATA\_OPER

__Descrição: __Data da Operação

__Tipo:__ N

__Tamanho: __008

__Formato:__ DDMMAAAA

__Comentário: __Data da operação \(data do lançamento da nota, ou data contábil, ou data da operação de acordo com os registros contábeis\)\.

__ Chave Primária__

MFS\-62826

__RN09__

__Campo 09 – Código da conta analítica debitada/creditada __

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Código da conta analítica debitada/creditada na tabela SAFX160\.

__Tabela: __SAFX160

__Item: __09

__Nome do Campo:__ COD\_CONTA

__Descrição: __Código da conta analítica debitada/creditada

__Tipo:__ A

__Tamanho: __070

__Comentário: __

Conta Contábil referente ao Imposto, utilizada para Contabilização, de acordo com a Tabela     de Plano de Contas \(SAFX2002\)\. 

MFS\-62826

__RN10__

__Campo 10 – Código do centro de custos__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Código do centro de custos na tabela SAFX160\.

__Tabela: __SAFX160

__Item: __10

__Nome do Campo:__ COD\_CUSTO

__Descrição: __Código do centro de custos

__Tipo:__ A

__Tamanho: __020

__Comentário: __

O Código deve estar registrado na Tabela de Centro de Custos \(SAFX2003\)\.

MFS\-62826

__RN11__

__Campo 11 – Número do documento__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Descrição complementar do Documento/Operação na tabela SAFX160\.

__Tabela: __SAFX160

__Item: __11

__Nome do Campo:__ NUM\_DOCTO

__Descrição: __Número do documento

__Tipo:__ A

__Tamanho: __012

__Comentário: __

Número de identificação do documento/Operação se houver

__Chave Primária__

__Não Obrigatório__

MFS\-62826

__RN12__

__Campo 12 – Série do documento__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Descrição complementar do Documento/Operação na tabela SAFX160\.

__Tabela: __SAFX160

__Item: __12

__Nome do Campo:__ SERIE

__Descrição: __Série do documento/Operação

__Tipo:__ A

__Tamanho: __003

__Comentário: __

Informar a série do documento/Operação se houver

__Chave Primária__

__Não Obrigatório__

MFS\-62826

__RN13__

__Campo 13 – Subsérie do Documento__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Descrição complementar do Documento/Operação na tabela SAFX160\.

__Tabela: __SAFX160

__Item: __13

__Nome do Campo:__ SUB\_SERIE

__Descrição: __Subsérie do documento/Operação

__Tipo:__ A

__Tamanho: __003

__Comentário: __

Informar a subsérie do documento/Operação se houver

__Chave Primária__

__Não Obrigatório__

MFS\-62826

__RN14__

__Campo 14 – Número do Lançamento__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Descrição complementar do Documento/Operação na tabela SAFX160\.

__Tabela: __SAFX160

__Item: __14

__Nome do Campo:__ NUM\_LANCTO

__Descrição: __Número do lançamento

__Tipo:__ A

__Tamanho: __040

__Comentário: __

Informar o número de lançamento destinado à identificação do conjunto de registros representativos do documento/operação\.

__Chave Primária__

__Não Obrigatório__

MFS\-62826

__RN15__

__Campo 15 – Número de Processo de Referência__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Número de Processo de Referência na tabela SAFX160\.

Tabela: SAFX160

Item: 15

__Nome do Campo__: NUM\_PROC\_REF

__Descrição: __Número de Processo de Referência

Tipo: N

Tamanho: 020

Comentário: Informar o número do processo judicial referenciado, conforme o Cadastro de Processos Referenciados\. Somente serão aceitos os processos cujo tipo de processo seja igual a '1 \- Justiça Federal', '3 \- Secretaria da Receita Federal do Brasil' ou '9 \- Outros'\.

__Consistência:__

Deverá existir um cadastro correspondente na SAFX2058 com o tipo de processo igual a 1 – Administrativo ou 2 – Judicial, vigente para o período informado\. Caso não exista, ou não tenha o tipo de processo esperado, exibir a mensagem: “Cadastro do processo referenciado nao encontrado ou registrado com data posterior ao movimento informado\.”

__Campo Obrigatório__

MFS\-62826

__RN16__

__Campo 16 – Indicador de Origem do Processo__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Indicador de Origem do Processo na tabela SAFX160\.

Tabela: SAFX160

Item: 16

__Nome do Campo__: ORIG\_PROCESSO

__Descrição: __Indicador da Origem do Processo

Tipo: N

Tamanho: 1

Lista de Valores Válidos: “1”, “3” ou “9”\. 

Comentário: 

Informar o tipo de Origem do Processo, os valores possíveis são '1' \- Justiça Federal, '3' \- Secretaria da Receita Federal do Brasil ou '9' \- Outros\.

__Tratamento:__ Se não for informado um valor válido, exibir a mensagem: O campo indicador da origem do processo deve ser preenchido com uma das opcoes validas: <1>, <3> ou <9>\.

MFS\-62826

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

