# MTZ-Job-Servidor-Importacao_SAFX533

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX533.docx
- **Modificado:** 2020-08-10
- **Tamanho:** 79 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX533

Tabela de Rendimentos Imunes e Isentos art\. 4º incisos III e V – IN RFB 1\.234/2012 da DIRF  

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS41827

Liliane Assaf

Criação de nova tabela SAFX para carga dos rendimentos oriundos dos valores pagos às entidades imunes \(art\. 4º, inciso III\) ou isentas \(art\. 4º, inciso IV\) \- IN RFB 1\.234/2012\. Tais informações demonstradas nos registros VPEIM, RIMUM,  RISEN da DIRF, conforme IN RFB nº 1\.663, de 07/10/2016\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Tabela de Rendimentos Imunes e Isentos DIRF \(SAFX533\)__

__Estrutura da tabela SAFX533__ 🡪 vide manual de layout

A SAFX533 tem como objetivo carregar os rendimentos pagos às entidades imunes \(art\. 4º, inciso III\) ou isentas \(art\. 4º, inciso IV\) da IN RFB 1\.234/2012, para atendimento aos registros VPEIM, RIMUM,  RISEN da DIRF\.  

Inicialmente cogitamos carregar esses rendimentos na SAFX53, tabela de retenções que vão pra DIRF\. Mas por serem operações imunes e isentas não possuem DARF, que é um campo obrigatório na SAFX53\.  Daí partimos para a solução de criar uma tabela específica para receber esses rendimentos\.

Foi passado para o setor de informação um questionamento quanto a apresentação em outras obrigações como DCTF, REINF, ESOCIAL de tais rendimentos\.

__Campos que compõe a chave da tabela definitiva \(X533\_RIMUN\_RISEN\):__

Código da Empresa \(COD\_EMPRESA\),

Código do Estabelecimento\(COD\_ESTAB\),

Data do Movimento \(DATA\_MOVTO\)

Pessoa Física/Jurídica \(IDENT\_FIS\_JUR\)

Tipo do Documento \(IDENT\_DOCTO\)

Número do Documento \(NUM\_DOCFIS\)

Série do Documento \(SERIE\_DOCFIS\)

Subsérie do Documento \(SUB\_SERIE\_DOCFIS\)

Código de Operação \(IDENT\_OPERACAO\)

A manutenção da tabela está disponível no módulo Básicos >> Data Wharehouse, menu: Manutenção 🡪 Retenções 🡪 Rendimentos Imunes/Isentos \(art\. 4º, incisos III e IV – IN RFB 1\.234/2012\)\.

__Base Legal:__

__IN RFB nº 1\.663, de 07/10/2016\.__

__Conceito da alteração no procedimento legal:__

Por meio da publicação da Instrução Normativa nº 1\.663, de 07 de outubro de 2016, foi alterada a Instrução Normativa nº 1\.234, de 11 de janeiro de 2012, que dispõe sobre a retenção de tributos nos pagamentos efetuados pelos órgãos da administração pública federal direta, autarquias e fundações federais, empresas públicas, sociedades de economia mista e demais pessoas jurídicas que menciona a outras pessoas jurídicas pelo fornecimento de bens e serviços\. 

Nesse sentido, entre as alterações, destacamos que ficou determinado que também deverão ser informados na DIRF, relacionada aos fatos ocorridos a partir do ano\-calendário de 2017, os valores pagos às entidades imunes ou isentas a seguir indicadas, nela discriminando, mensalmente, os valores pagos a cada entidade:

- instituições de educação e de assistência social, sem fins lucrativos, a que se refere o art\. 12 da Lei nº 9\.532/1997 
- instituições de caráter filantrópico, recreativo, cultural, científico e às associações civis, a que se refere o art\. 15 da Lei nº 9\.532/1997\.

MFS41827

__RN01__

__Campo 01 \-  Código da Empresa__

Campo de preenchimento __*obrigatório*__\.

*\(registros das tabelas SAFX sem a informação da Empresa serão desconsiderados\)*

MFS41827

__RN02__

__Campo 02 \- Código do Estabelecimento__

Campo de preenchimento __*obrigatório*__\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento serão desconsiderados\)*

MFS41827

__RN03__

__Campo 03 \- Data do Movimento__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                           “90009 \- O Campo Data de Movimento nao esta preenchido ou preenchido com zeros\.”*

Caso o campo esteja preenchido, se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                           “90883 \- O Campo Data de Movimento e invalido”*

MFS41827

__RN04__

__Campo 04 – Indicador da Pessoa Física/Jurídica __

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, ou quando seu conteúdo for inválido \(diferente dos valores válidos p/o indicador da SAFX04\), o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“90088 \- O Indicador de Pessoa Fisica/Juridica nao esta preenchido ou com informacao invalida\.”*

MFS41827

__RN05__

__Campo 05 – Código da Pessoa Física/Jurídica __

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“90089  \- O Codigo da Pessoa Fisica/Juridica nao esta preenchido”*

Caso o campo esteja preenchido, mas a pessoa fis/jur informada não existir na Tabela SAFX04, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“90124 \- O Codigo da Pessoa Fisica/Juridica nao esta cadastrado\.”*

Para fazer a pesquisa na SAFX04, o grupo de relacionamento será obtido a partir da data de movimento, e serão consideradas na pesquisa apenas as pessoas fis/jur  com data de validade < = a data de movimento\.

MFS41827

__RN06__

__Campo 06 – Tipo do Documento __

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“90119  \- O Campo Codigo do Tipo de Documento nao esta preenchido\.”*

Caso o campo esteja preenchido, mas o tipo de documento informado não existir na Tabela SAFX2005, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“90125 \- O Codigo do Tipo de Documento nao esta cadastrado\.”*

Para fazer a pesquisa na SAFX2005, o grupo de relacionamento será obtido a partir da data de movimento, e serão consideradas na pesquisa apenas os tipos de documentos com data de validade < = a data de movimento\.

MFS41827

__RN07__

__Campo 07 – Número do Documento__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“90112\- O Campo Numero do Documento nao esta preenchido\.”*

MFS41827

__RN08__

__Campo 08 – Série do Documento__

Campo de preenchimento não obrigatório\.

Se o campo não estiver preenchido da SAFX533, o registro deve ser importado gravando\-o com um espaço em branco na tabela definitiva X533\_RIMUN\_RISEN\.

MFS41827

__RN09__

__Campo 09 – Subsérie do Documento__

Campo de preenchimento não obrigatório\.

Se o campo não estiver preenchido da SAFX533, o registro deve ser importado gravando\-o com um espaço em branco na tabela definitiva X533\_RIMUN\_RISEN\.

MFS41827

__RN10__

__Campo 10 – Código de Operação__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“90122  \- O Campo de Codigo de Operacao nao esta preenchido\.”*

Caso o campo esteja preenchido, mas o código da operação informado não existir na Tabela SAFX2001, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“90123 \- O Campo de Codigo de Operacao nao esta cadastrado\.”*

Para fazer a pesquisa na SAFX2001, o grupo de relacionamento será obtido a partir da data de movimento, e serão consideradas na pesquisa apenas os códigos de operação com data de validade < = a data de movimento\.

MFS41827

__RN11__

__Campo 11 – Ano Competência__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“90179 \- O Campo Ano de Competencia e obrigatorio \- deve ser preenchido\.”*

Caso o campo esteja preenchido, mas que não seja numérico, então o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“90461\- Valor Decimal ou Numerico com formato invalido\.”*

MFS41827

__RN12__

__Campo 12 – Mês Competência__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“90180 \- O Campo Mes de Competencia e obrigatorio \- deve ser preenchido\.”*

Caso o campo esteja preenchido, mas que não seja numérico, então o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“90461\- Valor Decimal ou Numerico com formato invalido\.”*

MFS41827

__RN13__

__Campo 13 – Indicador de Imunidade ou Isenção__

Campo de preenchimento __*obrigatório*__\.

Lista de valores válidos:

1 – Pagamento à Entidade Imune \(art\. 4º, inciso III\);  
2 – Pagamento à Entidade Isenta  \(art\. 4º, inciso IV\)\.

Quando não preenchido, ou preenchido com um valor diferente de “1” e “2”, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“92500\- O Campo Indicador de Imunidade ou Isencao e obrigatorio e deve ser preenchido com: <1> ou <2>\.”*

MFS41827

__RN14__

__Campo 14 – Valor do Rendimento__

Campo de preenchimento não obrigatório\.

Caso o campo esteja preenchido, mas que não seja numérico, então o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“90461\- Valor Decimal ou Numerico com formato invalido\.”*

MFS41827

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

