# MTZ_Importacao_SAFX_detalhe_safx158

- **Fonte:** MTZ_Importacao_SAFX_detalhe_safx158.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 47 KB

---

    

# Módulo Job Servidor – Importação – Detalhe do Crédito/Contribuição Extemporânea – Itens Notas Fiscais Mercadorias e Produtos 

#  \(SAFX158\) 

*\(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX158, conforme o Manual de Layout, o que facilita a consulta\)*

*\(Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00\)*

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3169\-DW11

Criação da SAFX158

Criação da tabela de Detalhe de Crédito/Contribuição Extemporânea dos itens das notas fiscais de mercadoria extemporânea ‘’filha’’ da SAFX08 para atendimento dos registros 1101, 1102, 1501, 1502, 1200, 1210, 1600 e 1610 do Bloco 1 do Anexo Único do Ato Declaratório Executivo COFINS Nº 31, de 08 de julho de 2010

09/02/2011

CH110004

Alteração

Ao importar a SAFX158 , o campo \(IND\_PIS\_COFINS\_EXTEMP\) da SAFX08, deve ser alterado para S automaticamente\. 

22/08/2011

OS3513

Data Fiscal para as Notas Fiscais de Saídas de Mercadorias 

Quando parametrizado, então a data do fato gerador \(Data Fiscal\) na saída de documentos fiscais de mercadoria deve ser a “Data E/S”, ou seja, data de saída da mercadoria\.

06/12/2011

CH118904\-A

DW \- BASICOS \- JOB SERVIDOR \- Importação da SAFX158 \- Não é possível flegar a opção limita período

O objetivo dessa demanda é permitir que a importação da SAFX158 possa ser feita por período, através do campo Limita Período\.

20/12/2011

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN00__

__Regras gerais__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alterados para contemplar os campos descritos abaixo na tabela SAFX158\.

__*Limita Período:*__

Quando o campo Limita Período da tela de programação da importação estiver marcado, a importação deve importar apenas os registros que estiverem dentro do período informado nos campos Início Período e Fim Período\. 

Quando este campo não estiver marcado, a importação deve importar os registros independente do período informado\.

Na importação deve conter a seguinte regra de importação:

__Validação:__

Não existe registro na X08 com a mesma chave \(Empresa, Estabelecimento, Data da Escrita Fiscal, Movimento Entrada/Saída, Normal ou Devolução, Tipo do Documento, Indicador da Pessoa Física/Jurídica, Código do Destinatário/Emitente, Número do Documento Fiscal, Série, Sub Série, Indicador do Produto, Produto, código do bem, código do incorporador, unidade padrão, item de nota fiscal, data de lançamento do crédito/débito, crédito/débito extemporâneo, Código da Situação Tributária do PIS/PASEP e Código da Situação Tributária da COFINS\) do registro que está sendo importado na SAFX158\.

__Mensagem:__

Não existe item do documento fiscal de mercadoria para esse detalhe de crédito/débito extemporâneo\.

__Solução: __

Importar a SAFX08 para esse item da nota fiscal de mercadoria e produto, com competência menor à competência informada na SAFX158\.

OS3169\-DW14

/

CH118904\-A

__RN01__

__Campo 01 \- Código da empresa__

 

__Item: __01

__Nome do Campo: __COD\_EMPRESA

__Descrição: __Código da empresa

__Tipo:__ A

__Tamanho: __003

__Comentário: __Campo destinado ao código da Empresa\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN02__

__Campo 02 \- Código do estabelecimento__

__Item: __02

__Nome do Campo: __COD\_ESTAB

__Descrição: __Código do estabelecimento

__Tipo:__ A

__Tamanho: __006

__Comentário: __Campo destinado ao código do Estabelecimento\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN03__

__Campo 03 \- Data da Escrita Fiscal__

__Item: 03__

__Nome do Campo: __DATA\_FISCAL

__Descrição:__ Data da Escrita Fiscal

__Tipo__: N

__Tamanho:__ 008

C__omentário__:

Este campo deve corresponder à data fiscal contida na SAFX08, que está definida da seguinte maneira:        

 \-Notas de entrada = data de saída/recebimento \(campo 20 da SAFX07\);                                                                         

 \-Notas de saída = data da emissão do documento\.              

\[Alteração – OS 3513\]

Se o campo 03 \(MOVTO\_E\_S\) da SAFX07 = ‘9’

E campo 12 \(COD\_CLASS\_DOC\_FIS\) da SAFX07 = ‘1’ ou ‘3’ ou ‘7’, então

Campo 03 \(DATA\_FISCAL\) da SAFX158 = campo 20 da SAFX07 \(DATA\_SAIDA\_REC\)\.

Esta regra __somente__ será valida se campo 01 \(COD\_EMPRESA\) OU campo 02 \(COD\_ESTAB\) corretamente parametrizado em "Módulo: Básicos > Parâmetros, Menu: Preliminares > Parametrização para Data Fiscal"

Caso não exista a parametrização, o documento seja de entrada ou não seja de mercadoria, então continuar escriturando da forma como é feita originalmente\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14 / OS\-3513

__RN04__

__Campo 04 \- Movimento Entrada/Saída__

__Item: 04__

__Nome do Campo: __MOVTO\_E\_S

__Descrição: __Movimento Entrada/Saída

__Tipo:__ A

__Tamanho: __001

__Comentário: __

Informar de acordo com:

1 \- Documento de Entrada, Documento de Terceiros;

2 \- Documento de Entrada emitida pelo Estabelecimento, acolhendo Notas de Produtores Agropecuários;

3 \- Documento de Entrada emitida pelo Estabelecimento, por retorno de mercadorias não entregues ao destinatário;                                                                                                                                        4 \- Documento de Entrada emitida pelo Estabelecimento, outros motivos legais;

5 \- Documento de Entrada emitida pelo Estabelecimento, globalizando Conhecimento de Frete ou Material Uso/Consumo;

9 \- Documento de Saída\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN05__

__Campo 05 \- Normal ou Devolução__

__Item: 05__

__Nome do Campo: __NORM\_DEV

__Descrição: __Normal ou Devolução 

__Tipo:__ A

__Tamanho: __001

__Comentário: __

Qualifica o motivo da Entrada / Saída, de acordo com:

1 \- Normal;

2 \- Devolução \(Quando se tratar de Devolução de Mercadorias\- Produtos, Insumos, Materiais Uso/Consumo, Ativo, etc\., previstos em legislação\)\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN06__

__Campo 06 – Tipo do Documento__

__Item: 06__

__Nome do Campo: __COD\_DOCTO

__Descrição: __Tipo do Documento

__Tipo:__ A

__Tamanho: __005

__Comentário:__

__ __Tipo de Documento de acordo com a Tabela de Tipo de Documentos \(SAFX2005\) \-  \(Duplicata,  Fatura,  Nota  Fiscal  Fatura,  Recibo  e  etc\. \.\.\. \)\. Quando se trata de Documentos Fiscais Modelos 2B, 2C ou 2D informar “MRC”\. O MasterSAF definiu um Tipo de Documento “CIAP” para atender a escrituração dos Créditos de 1/48 avos para o Estado de MG, que exige que estes créditos sejam listados no Livro Registro de Entradas\. De acordo com as alterações nas Legislações de ECF, é necessário que o Código a ser utilizado para a Escrituração do Resumo Diário de ECF no Livro Registro de Saídas seja informado “CF”, a Partir do Convênio ICMS No 50/00 \(15/09/00\)\. Para os Resumos Diários ou por Ciclo de Faturamento referentes a Telecomunicações, Energia Elétrica e Contas de Fornecimento de Gás Canalizado, o Usuário poderá criar uma Codificação que deve ser registrada na “Tabela de Tipos de Documentos Fiscais”\. É importante salientar que este dado não mais é requerido para a IN SRF 86/01, mas é obrigatório para a Escrituração dos Livros Fiscais do Convênio ICMS 57/95 e suas alterações\.

__Chave Primária__

__Obrigatório__ 

OS3169\-DW14

__RN07__

__Campo 07 – Indicador da Pessoa Fis/Jur Adquirente__

__Item: 07__

__Nome do Campo: __IND\_FIS\_JUR 

__Descrição: __Indicador da Pessoa Física/Jurídica 

__Tipo:__ A

__Tamanho: __001

__Comentário: __

Campo que deverá ser preenchido com o Indicador de Pessoa Física/Jurídica relacionada, conforme segue:

1 \- Fornecedor;

2 \- Cliente;

3 \- Estabelecimento;

4 \- Transportadora;

5 \- Cliente/Fornecedor/Transportadora\.

Para a IN SRF 86/01 a Identificação se é fornecedor, cliente, transportadora não tem significado, apenas deve ser informado o cadastro e as respectivas alterações referentes ao período de abrangência de dados solicitados na Intimação\. Esta discriminação foi introduzida pelo MasterSAF para atender as necessidades de estrutura de dados de nossos clientes e que não interferem nos dados a serem fornecidos ao Fisco\. Esta definição é a mesma já definida na Capa do Documento Fiscal\.

Observação: Para o Convênio 51/00, este campo deve ser preenchido da seguinte forma:

\- Faturamento Direto para Leasing \- preencher com o Destinatário da Nota Fiscal de Leasing, no caso a Financeira do Veículo;

\- Faturamento Direto \- preencher com o Dealer de Entrega do Veículo \(Concessionária\);

__Chave Primária__

__Obrigatório__ 

OS3169\-DW14

__RN08__

__Campo 08 – Código da Pessoa Fis/Jur Adquirente__

__Item: 08__

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Código do Destinatário/Emitente

__Tipo:__ A

__Tamanho: __014

__Comentário: __

Preencher com Indicador da Pessoa Fis/Jur do documento fiscal da SAFX07\. Preencher de acordo com a Tabela de Pessoas Física/Jurídicas \(SAFX04\)\.

Quando se tratar de Outros Documentos Fiscais, tais como Resumo de ECF, Resumo Diário ou por Ciclo de Faturamento de Telecomunicações, Energia Elétrica e Gás Canalizado pode\-se informar o Código do Estabelecimento\. Esta definição é a mesma já definida na Capa do Documento Fiscal\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN09__

__Campo  09 – Número do Documento Fiscal__

__Item: 09__

__Nome do Campo: __NUM\_DOCFIS

__Descrição: __Número do Documento Fiscal

__Tipo:__ A

__Tamanho: __012

__Comentário: __

Neste Campo deve ser informado o Número do Documento Fiscal\. Quando se tratar de Tipo de Documento Fiscal Modelo 2B, 2C ou 2D informar o Número do Mapa de Resumo\. Da mesma forma, quando se tratar de Resumos Diários referentes a Escrituração de Documentos Fiscais de Telecomunicações, Energia Elétrica ou Gás Canalizado, pode\-se informar o Número do Resumo, ou um Número Sequencial para o Campo – Número do Documento\. Esta definição é a mesma já definida na Capa do Documento Fiscal\. O Número do Documento Fiscal deve ter tamanho de 6 \(seis\) dígitos, que podem ser alinhados a esquerda ou a direita, porém com os 6 \(seis\) dígitos completos\. Para o Setor de Telecomunicações já estão previstos Números com 9 \(nove\) Dígitos, que também devem ser alinhados a esquerda ou a direita, uma vez que o MasterSAF define este campo com 12 \(doze\) dígitos\. As instruções do Convênio ICMS No 57/95 determina que números de Documentos Fiscais com Números acima de 6 \(seis\) dígitos, sejam truncados nos dígitos mais significativos\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN10__

__Campo 10 \- Série do Documento Fiscal__

__Item: 10__

__Nome do Campo: __SERIE\_DOCFIS 

__Descrição: Série do Documento Fiscal__

__Tipo:__ A

__Tamanho: __003

__Comentário: __

A ausência deste dado deve ser representada com espaços ou nulo\. Quando se trata de Documentos Fiscais Modelos 2B, 2C ou 2D informar “CMR”\. Com as alterações introduzidas na Legislação os Campos de Séries para ECF devem conter a informação “ECF”, a Partir do Convênio ICMS No 50/00 \(15/09/00\)\. Quando se Tratar da Escrituração dos Mapas Resumos de Telecomunicações, Energia Elétrica e Gás Canalizado os campos devem vir Nulos, a não ser que haja uma AIDF que contemple este resumo como Uma Obrigação Acessória, tal como os Resumos Diários de ECF\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN11__

__Campo 11 \- Subsérie do Documento Fiscal__

__Item: __11

__Nome do Campo: __SUB\_SERIE\_DOCFIS

__Descrição: __Subsérie do Documento Fiscal

__Tipo:__ A

__Tamanho: __002

__Comentário: __

A ausência deste dado deve ser representada com espaços ou nulo\. Quando se trata de Documentos Fiscais Modelos 2B, 2C ou 2D informar “CMR”\. Com as alterações introduzidas na Legislação os Campos de Séries para ECF devem conter a informação “ECF”, a Partir do Convênio ICMS No 50/00 \(15/09/00\)\.Quando se Tratar da Escrituração dos Mapas Resumos de Telecomunicações, Energia Elétrica e Gás Canalizado os campos devem vir Nulos, a não ser que haja uma AIDF que contemple este resumo como Uma Obrigação Acessória, tal como os Resumos Diários de ECF\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN12__

__ Campo 12 \- Bem Patrimonial \(Sim/Não \)__

__Item: 12__

__Nome do Campo: __IND\_BEM\_PATR

__Descrição: __Bem Patrimonial \(Sim/Não\)

__Tipo:__ A

__Tamanho: __001

__Comentário: __

Informar de acordo com:

S \- Indica associação do item do Documento Fiscal à Tabela de Cadastro de Bens \(SAFX13\);

N \- Indica associação do item do Documento Fiscal à Tabela de Produtos \(SAFX2013\)\.

O MasterSAF implementou este dado para permitir que seus Clientes já registrassem os Códigos das Plaquetas “Códigos dos Bens do Ativo” já no Registro de Aquisição dos Bens do Ativo e nas Alienações\. Porém a prática e as Estruturas de dados de nossos Clientes nos mostrou que não é a solução\. Estes Campos, hoje, não são utilizados, e assim, deve ser observado que ao se informar “N” neste campo não devem ser preenchidos os “Campos 15 e 16”\. Porém se algum Usuário MasterSAF, dispuser desta informação no Sistema Transacional tanto nas operações de Aquisições de Bens do Ativo e nas Alienações desses Bens poderá informar nestes campos, o que permitirá uma otimização dos controles dos Créditos de 1/48 avos do CIAP\. 

Para solucionar o Controle dos Créditos do CIAP, o Usuário poderá utilizar um Código de Produto/Mercadoria \(Classificado como 8\-Miscelâneas Campo –13\) e informar na descrição complementar do Produto a descrição do Bem do Ativo, ou cadastrar para cada bem do Ativo um Código de Produto/Mercadoria\.

Observação: O preenchimento dos campos 13 e 14 excluem o preenchimento dos campos 15 e 16, e vice\-versa\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN13__

__Campo 13 \- Indicador do Produto__

__Item: __13

__Nome do Campo: __IND\_PRODUTO

__Descrição: __Indicador do Produto

__Tipo:__ A

__Tamanho: __001

__Comentário: __

identificadores:

1 \- Produto Acabado;

2 \- Insumos;

3 \- Embalagem;

4 \- Consumo;

5 \- Outros;

6 \- Em Elaboração;

7 \- Intermediário;

8 \- Miscelâneas\.

Esta Discriminação para Identificar a Mercadoria se é Produto Acabado, Insumo, Produto em Elaboração, não é mais solicitada pela IN SRF 86/01, porém é obrigatória para outras obrigações da RIPI, tal como o Inventário, por isso, deve continuar a atender a SRF\. Obs: O preenchimento dos campos 13 e 14 exclui o preenchimento dos campos 15 e 16, e vice\-versa\.

__Obrigatório__

OS3169\-DW14

__RN14__

__Campo 14 \- Produto__

__Item: 14__

__Nome do Campo: __COD\_PRODUTO

__Descrição: __Produto

__Tipo:__ A

__Tamanho: __035

__Comentário: __

Informar o Código do Produto/Mercadoria, de acordo com  as solicitações da dos Convênios ICMS, RIPI e IN SRF, devidamente registradas na Tabela de Produto \(SAFX2013\)\. Esta codificação de mercadorias/produtos deve representar os códigos dos registrados nos sistemas corporativos e nos sistemas de faturamento \(Billing\)\. Assim, para simples ilustração podemos citar que para empresas industriais e comerciais, devem ser informados os códigos internos, para telecomunicações, os serviços que especificam os tipos de ligações, etc\. Para o registro do “Resumo Diário” e Outros Resumos referentes a outros Modelos de Documentos Fiscais, não existe a exigência de Códigos específicos, bem como para registrar aquisições de Bens do Ativo e/ou as Alienações\. Por isso, para cada Tipo de Modelo de Documento Fiscal, deve ser definido os critérios  e os códigos a serem utilizados e analisar se as Legislações requerem ou não Códigos para o Atendimento a Escrituração, Meios Magnéticos e Obrigações Acessórias\. Obs: O preenchimento dos campos 13 e 14 exclui o preenchimento dos campos 15 e 16, e vice\-versa\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN15__

__Campo 15 \- Código do Bem__

__Item: 15__

__Nome do Campo: __COD\_BEM

__Descrição: __Código do Bem

__Tipo:__ A

__Tamanho: __030

__Comentário: __

Informar de acordo com a Tabela de Cadastro de Bens \(SAFX13\)\. Caso o Usuário venha a Utilizar o Código do bem do Ativo para Identificar a Aquisição, Transferência, Alienação ou outro tipo de operação, deve observar que este Código já deve ter sido registrado na Tabela de Bens do Ativo – SAFX13\. Com isso, o Usuário já terá outras vantagens no Módulo de Controle de Créditos de 1/48 de ICMS\. Se o Usuário utilizar este Código de bem do Ativo, que pode ser o Código da Plaqueta ou Outro Código, então não deverá utilizar os “Campos 13 e 14”\. A Referência a Código do Incorporador tem a função de definir os Bens que estão relacionados ao Bem Principal\.

Obs: O preenchimento dos campos 13 e 14 exclui o preenchimento dos campos 15 e 16, e vice\-versa\.

Observação sobre o CIAP x Sped Fiscal – Bloco G:

Os usuários que carregam os dados do CIAP a partir da geração automática que lê as notas fiscais devem observar que é uma grande vantagem o preenchimento desta informação no item da nota, pois desta forma ao gerar o CIAP a informação do código do Bem já estará também preenchida\. Lembrando que trata\-se de informação obrigatória no Bloco G do Sped Fiscal\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN16__

__Campo 16 \- Código do Incorporador__

__Item: 16__

__Nome do Campo: __COD\_INC\_BEM

__Descrição: __Código do Incorporador

__Tipo:__ A

__Tamanho: __006

__Comentário: __

Informar de acordo com a Tabela de Cadastro de Bens \(SAFX13\)\. Caso o Usuário venha a Utilizar o Código do bem do Ativo para Identificar a Aquisição, Transferência, Alienação ou outro tipo de operação, deve observar que este Código já deve ter sido registrado na Tabela de Bens do Ativo – SAFX13\. Com isso, o Usuário já terá outras vantagens no Módulo de Controle de Créditos de 1/48 de ICMS\. Se o Usuário utilizar este Código de bem do Ativo, que pode ser o Código da Plaqueta ou Outro Código, então não deverá utilizar os “Campos 13 e 14”\. A Referência a Código do Incorporador tem a função de definir os Bens que estão relacionados ao Bem Principal\.

Obs: O preenchimento dos campos 13 e 14 exclui o preenchimento dos campos 15 e 16, e vice\-versa\.

Observação sobre o CIAP x Sped Fiscal – Bloco G:

Os usuários que carregam os dados do CIAP a partir da geração automática que lê as notas fiscais, devem observar que é uma grande vantagem o preenchimento desta informação no item da nota, pois desta forma ao gerar o CIAP a informação do código do Bem já estará também preenchida\. Lembrando que trata\-se de informação obrigatória no Bloco G do Sped Fiscal\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN17__

__Campo 17 \- Unidade Padrão__

__Item: 17__

__Nome do Campo: __COD\_UND\_PADRAO

__Descrição: __Unidade Padrão

__Tipo:__ N

__Tamanho: __008

__Comentário: __

Unidade utilizada para controle de estoque da mercadoria\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN18__

__Campo 18 \- Item Nota Fiscal__

__Item: __18

__Nome do Campo: __NUM\_ITEM

__Descrição: __Item Nota Fiscal 

__Tipo:__ N

__Tamanho: __005

__Comentário: __

Informar o número do item da Nota Fiscal\. Apesar do campo possibilitar o tamanho de 05 posições, ou seja, notas fiscais com até 99\.999 itens, quanto da geração dos meios magnéticos \(Sintegra, IN86, IN89, SEF\-PE, etc\.\.\.\) o sistema irá considerar somente 03 posições, ou seja, notas fiscais com até 999 itens\. Esta consideração deve\-se ao fato dos layouts destes meios magnéticos estarem solicitando somente 03 posições\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN19__

__Campo 19 \- Data de Lançamento do Crédito/Débito__

__Item: 19__

__Nome do Campo: __DAT\_LANC\_PIS\_COFINS

__Descrição: __Data de Lançamento do Crédito/Débito

__Tipo:__ N

__Tamanho: __008

__Comentário: __

Informar a data de lançamento dos valores de crédito ou débito de PIS/COFINS informados no documento fiscal

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN20__

__Campo 20 \- Crédito/Débito Extemporâneo__

__Item: 20__

__Nome do Campo: __IND\_PIS\_COFINS\_EXTEMP

__Descrição: __Crédito/Débito Extemporâneo

__Tipo:__ A

__Tamanho: __001

__Comentário: __

Campo utilizado para identificar se os valores de crédito ou débito dos valores de PIS/COFINS do documento fiscal serão considerados extemporâneos\.

__Chave Primária__

__Obrigatório__

OS3169\-DW14

__RN20\.1__

Ao importar o documento na SAFX158, o campo 197 \(IND\_PIS\_COFINS\_EXTEMP\) da SAFX08 \(referente à mesma nota\), deve ser alterado para ‘S’ automaticamente\. 

CH110004

__RN21__

__Campo 21 – Natureza da Base de Crédito__

__Item: 21__

__Nome do Campo: __Será definido pelo A&D__ __

__Descrição: __Natureza da Base de Crédito

__Tipo:__ N

__Tamanho: __002

__Comentário: __Informar o código da natureza da base de crédito, referenciada  no Manual do Leiaute do EFD PIS/PASEP\- COFINS

__Não Obrigatório__

OS3169\-DW14

__RN22__

__Campo 22 \- Quantidade:__

__Item: __22

__Nome do Campo: __QUANTIDADE

__Descrição: __Quantidade__ __

__Tipo:__ N

__Tamanho:__ 011V006

__Comentário: __

Informar a quantidade do produto que irá apropriar o crédito\.

__Obrigatório__

__Validação:__

A quantidade informada no campo 20 da X158 que está sendo importada maior que a quantidade informada no campo 24 da X08\. 

__Mensagem:__

“A soma da quantidade do detalhe do crédito/contribuição extemporâneo do item de documento fiscal de mercadoria e produto da ‘’X158’’ deve ser menor ou igual à quantidade do item informado na X08 ‘’

OS3169\-DW14

__RN23__

__Campo 23 \- Código da Situação Tributária do PIS/PASEP__

__Item: 23__

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Código da Situação Tributária do PIS/PASEP

__Tipo:__ N

__Tamanho: __002

__Comentário: __

Informar o código da situação tributária do PIS, conforme tabela da Receita Federal\.

__Chave Primária__

__Obrigatória__

OS3169\-DW14

__RN24__

__Campo 24 \- Valor da Base de cálculo do PIS__

__Item:__ __24__

__Nome do Campo:__ VLR\_BASE\_PIS

__Descrição: __Valor da Base de cálculo do PIS

__Tipo:__ N	

__Tamanho: __015V002

__Comentário:__

Valor da Base de cálculo do PIS/PASEP de acordo com a operação\.

__Não Obrigatório__

OS3169\-DW14

__RN25__

__Campo 25 \- Alíquota do PIS__

__Item: 25__

__Nome do Campo:__ VLR\_ALIQ\_PIS

__Descrição:__ Alíquota PIS

__Tipo:__ N

__Tamanho: __003V004

__Comentário: __

 Informar Alíquota do PIS/PASEP \(em percentual\) da operação

__Não Obrigatório__

OS3169\-DW14

__RN26__

__Campo 26\- Quantidade \- Base de Cálculo PIS__

__Item: 26__

__Nome do Campo:__ QTD\_BASE\_PIS

__Descrição:__ Quantidade \- Base de Cálculo PIS

__Tipo:__ N

__Tamanho: __015V003

__Comentário: __

 Informar a quantidade de base de cálculo do PIS\.

__Não Obrigatório__

OS3169\-DW14

__RN27__

__Campo 27 \- Alíquota do PIS \- em reais__

__Item: 27__

__Nome do Campo:__ VLR\_ALIQ\_PIS\_R

__Descrição:__ Alíquota PIS

__Tipo:__ N

__Tamanho: __015V004

__Comentário: __

 Informar Alíquota do PIS/PASEP \(em reais\) da operação

__Não Obrigatório__

OS3169\-DW14

__RN28__

__Campo 28 \- Valor do PIS__

__Item: 28__

__Nome do Campo:__ VLR\_PIS

__Descrição:__ Valor do PIS

__Tipo:__ N

__Tamanho: __015V002

__Comentário: __

Informar Valor do PIS/PASEP, calculado pela multiplicação dos campos \(Base de Cálculo PIS x Alíquota PIS\) ou calculado pela a multiplicação dos campos \(Quantidade de base de cálculo do PIS x Alíquota do PIS/PASEP \- em reais\)

__Não Obrigatório__

OS3169\-DW14

__RN29__

__Campo 29\- Código da Situação Tributária COFINS__

__Item: __29

__Nome do Campo:__ Será definido pelo A&D

__Descrição: __Código da Situação Tributária COFINS

__Tipo:__ N

__Tamanho: __002

__Comentário: __

Informar o código da situação tributária da COFINS, conforme tabela da Receita Federal\.

__Chave Primária__

__Obrigatória__

OS3169\-DW14

__RN30__

__Campo 30 \- Valor da Base de cálculo da COFINS__

__Item: __30

__Nome do Campo:__ VLR\_BASE\_COFINS

__Descrição: __Valor da Base de cálculo da COFINS

__Tipo:__ N	

__Tamanho: __015V002

__Comentário:__

Valor da Base de cálculo da COFINS de acordo com a operação\.

__Não Obrigatório__

OS3169\-DW14

__RN31__

__Campo 31 \- Alíquota da COFINS__

__Item: __31

__Nome do Campo:__ VLR\_ALIQ\_COFINS

__Descrição:__ Alíquota COFINS

__Tipo:__ N

__Tamanho: __003V004

__Comentário: __

 Informar Alíquota da COFINS \(em percentual\) da operação

__Não Obrigatório__

OS3169\-DW14

__RN32__

__Campo 32 \- Quantidade \- Base de Cálculo COFINS__

__Item: __32

__Nome do Campo:__ QTD\_BASE\_COFINS

__Descrição:__ Quantidade \- Base de Cálculo COFINS

__Tipo:__ N

__Tamanho: __015V003

__Comentário: __

 Informar a quantidade de base de cálculo da COFINS\.

__Não Obrigatório__

OS3169\-DW14

__RN33__

__Campo 33 \- Alíquota da COFINS \- em reais__

__Item: __33

__Nome do Campo:__ VLR\_ALIQ\_COFINS\_R

__Descrição:__ Alíquota COFINS – em reais

__Tipo:__ N

__Tamanho: __015V004

__Comentário: __

 Informar Alíquota da COFINS \(em reais\) da operação

__Não Obrigatório__

OS3169\-DW14

__RN34__

__Campo 34 \- Valor da COFINS__

__Item: 34__

__Nome do Campo:__ VLR\_PIS

__Descrição:__ Valor do PIS

__Tipo:__ N

__Tamanho: __015V002

__Comentário: __

Informar Valor da COFINS, calculado pela multiplicação dos campos \(Base de Cálculo COFINS x Alíquota COFINS\) ou calculado pela a multiplicação dos campos \(Quantidade de base de cálculo da COFINS x Alíquota da COFINS \- em reais\)

__Não Obrigatório__

OS3169\-DW14

__RN35__

__Campo 35 \- Conta Contábil:__

__Item: __35

__Nome do Campo:__ COD\_CONTA

__Descrição: __Código da conta analítica debitada/creditada

__Tipo:__ A

__Tamanho: __070

__Comentário: __

Conta Contábil referente ao Imposto, utilizada para Contabilização, de acordo com a Tabela de Plano de Contas \(SAFX2002\)\. 

__Não Obrigatório__

OS3169\-DW14

__RN36__

__Campo 36 \- Centro de Custo:__

__Item: __36 

__Nome do Campo:__ COD\_CUSTO

__Descrição: __Código do centro de custos

__Tipo:__ A

__Tamanho: __020

__Comentário: __

O Código deve estar registrado na Tabela de Centro de Custos \(SAFX2003\)\.

__Não Obrigatório__

OS3169\-DW14

__RN37__

__Campo 37 \- Descrição complementar__

__Item: 37__

__Nome do Campo:__ DESC\_COMPL

__Descrição: __Descrição complementar

__Tipo:__ A

__Tamanho: __255

__Comentário: __

Descrição complementar do Documento/Operação\.

__Não Obrigatório__

OS3169\-DW14

