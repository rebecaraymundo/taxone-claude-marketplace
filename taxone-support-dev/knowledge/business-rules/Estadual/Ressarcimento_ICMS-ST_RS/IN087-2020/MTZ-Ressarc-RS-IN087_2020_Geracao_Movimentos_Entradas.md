# MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Entradas

- **Fonte:** MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Entradas.docx
- **Modificado:** 2026-03-01
- **Tamanho:** 130 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS 

\(IN\-RE 087/2020\) 

Geração dos Movimentos – Entradas 

__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS\-ST \- RS \(IN\-RE 048/2018\),

 itens: Geração 🡪 IN\-RE 087/20 🡪 Geração dos Movimentos 

	

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS48753__

Liliane Videira Assaf

Criação da funcionalidade\.

Não estamos trabalhando com Produtos Associados, apesar do documento mencionar tal parametrização em algumas regras\.

22/12/2020 

__MFS65137__

Liliane Videira Assaf

Retirada dos parâmetros da tela de geração, pois foram para a Tela de Dados Iniciais:

\- Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)

\- Tratamento p/ Entrada objeto da Devolução de períodos anteriores à adoção da sistemática da IN\-RE 087/20:

Valores Unitários Médios recuperados:

\( \) do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)

\( \) da própria Nota de Entrada referenciada pela Devolução

Dt anterior à adoção IN\-RE087/20: \[31/12/2020\]

13/05/2021

__MFS72429__

Andréa Rocha

Inclusão do arredondamento dos valores calculados, ou seja, os valores calculados não serão mais truncados\.  Conforme informação passada pela SEFAZ/RS\.

05/10/2021

__MFS81749__

Liliane Assaf

Tratamento para Notas de Produtos Farmacêuticos de Distribuidores criada pela MFS66473

15/03/2022

__MFS84243__

Andréa Rocha

Inclusão da verificação da data fiscal da nota fiscal para recuperar a parametrização por Produto/NCM/CEST\. 

12/04/2022

__MFS90131__

Liliane Assaf

Chamado Lasa/Magalu: Tratamento na diferença de 0,000001 do valor médio unitário do último dia do mês para o do primeiro dia do mês seguinte\. 

01/08/2022

__MFS92521__

Andréa Rocha

Alteração do preenchimento do campo 18\-VL\_UNIT\_CONV do registro C180, para passar a verificar o campo Responsável Retenção para fazer o cálculo do valor\.  Passar a utilizar a mesma regra já adotada para o Ressarcimento ICMS\-ST – MG\.

24/08/2022

__MFS93537__

Liliane Assaf

Criação do campo DATA EMISSÃO na tabela de movimentos de entrada \(EST\_ST\_RS\_NF\_ENT\)

19/10/2022

__MFS543860__

Andréa Rocha

Tratamento do parâmetro para definir se o valor do FECEP está embutido nos valores de ICMS não destacado e não escriturado

19/06/2023

Sumário

[1\.	Introdução	1](#_Toc59988567)

[2\.	Recuperação dos Dados e Processamento	1](#_Toc59988568)

[3\.	Gravação dos Dados na Tabela dos Movimentos	1](#_Toc59988569)

[4\.	RELATORIO DE CONFERÊNCIA	1](#_Toc59988570)

# <a id="_Toc59988567"></a>Introdução 

Esse documento tem como objetivo definir a geração das __Entradas__ que consiste em:

- Recuperar as notas fiscais entradas do período;
- Calcular os valores untários médios ponderados com base nos valores da nota de entrada;
- Gravar as notas de entradas na tabela específica dessa geração \(EST\_ST\_RS\_NF\_ENT\);
- Gerar o Relatório de Conferência a partir da tabela EST\_ST\_RS\_NF\_ENT, demonstrando o detalhamento do cálculo dos valores que serão apresentados no __C180__ do Sped Fiscal\.

Esse processamento é base para a geração do registro __C180__\. Todos os registros gravados na tabela EST\_ST\_RS\_NF\_ENT numa próxima etapa serão copiados para a tabela X296\_INFO\_COMPL\_ST\_ITENS\_MERC de onde parte a geração do registro C180 no módulo SPED FISCAL\.  Ou seja, as regras que definem o C180 são realizadas nessa fase\.

__Nota__: A parametrização dos Produtos Associados se aplica apenas na geração da IN048/18\. Não se aplica a IN087/20\!

# <a id="_Toc350763252"></a><a id="_Toc59988568"></a>Recuperação dos Dados e Processamento

<a id="_2.1_–_Recuperação"></a>__Origem dos dados__: \- Parametrização de Produtos \(por Código, por NCM e por CEST\);

                                  \- Parametrização de CFOP / Natureza de Operação;

                                  \- SAFX07 / SAFX08 – Tabelas dos Documentos Fiscais \(DATAMART\)

__Critérios da recuperação das Notas Fiscais de Entrada: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data Fiscal – data enquadrada no período informado em tela;

\- Nota fiscal normal \(NORM\_DEV = “1”\);

\- Nota de Entrada \(MOVTO\_E\_S <> “9”\);

\- Modelo = 01, 1B, 04, 55 \(\*\)

\- Somente notas *não canceladas*;

\- Somente notas *com itens*;

__\[MFS84243\] __Inclusão da verificação da data fiscal da nota fiscal para recuperar a parametrização por Produto/NCM/CEST\.

\- O produto do item deve constar na parametrização do menu “*Parâmetros 🡪 Produtos 🡪 Por Código*”, __ou__, seu NCM deve estar parametrizado no menu “*Parâmetros 🡪 Produtos 🡪 Por NCM*”, __ou__, seu CEST deve estar parametrizado no menu “*Parâmetros 🡪 Produtos 🡪 Por CEST*”\. 

  Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração\.  Somente devem ser considerados os produtos em que a data fiscal da nota fiscal esteja compreendida entre a data inicial de vigência e a data final de vingência da parametrização\.  Quando a data final de vigência não estiver preenchida, a parametrização ainda está válida, ou seja, o produto será considerado\.

   No caso da parametrização dos produtos, primeiro é verificado se o produto consta na parametrização da opção “Por Código”\. Ao verificar a parametrização por código, deve\-se considerar também os produtos associados\. Ou seja, o produto da nota deve constar como o produto “principal” da parametrização \(__ESP\_SP\_PROD\_ST__\), ou ser um produto “associado” ao produto principal \(__ESP\_SP\_PROD\_ST\_ASS__\)\.  Módulos de ressarcimento de SC e SP trabalham com produto associado\.

   Os produtos “associados” são produtos cuja movimentação será demonstrada na Ficha 3 em nome do produto principal parametrizado\. 

  A prioridade na pesquisa da parametrização dos produtos é: por Código, por NCM, e por último, por CEST, da seguinte forma:

 

        \-Caso o produto conste na parametrização por código, a parametrização por NCM não precisa ser verificada\.

        \-Caso não, é verificado se o NCM do produto \(NCM do cadastro do produto\) consta na parametrização da opção “Por NCM”\.

        \-Caso o produto conste na parametrização por NCM, a parametrização por CEST não precisa ser verificada\.

        \-Caso não, é verificado se o CEST do produto \(CEST do cadastro do produto\) consta na parametrização da opção “Por CEST”\.

 \- O CFOP ou CFOP/Natureza do item deve constar na parametrização do menu “*Parâmetros 🡪 \(IN\-RE 087/20\) 🡪 Operações*” para a seguinte operação:

- Entradas \(e Devoluções\)” \(código parâmetro 771\)

Recuperar as seguintes informações da nota de entrada \(SAFX07/SAFX08\):

\- Campos de Identificação da Capa e do Item da nota;

\- 13,14 \- Produto – GRUPO\_PRODUTO, IND\_PRODUTO, COD\_PRODUTO \(SAFX08\)

\- Unidade de Medida do Produto \(SAFX2013\)

__\- Caso o produto do item da nota de entrada tenha sido parametrizado por Código \(menu “Parâmetros 🡪 Produtos 🡪 Por Código”\) recuperar o Produto Principal \(grupo, indicador e código\) e a Unidade de Medida do Produto Principal \(SAFX2013 – campo 14 – COD\_MEDIDA\)\.__

\- 24 \- Quantidade \- QUANTIDADE \(SAFX08\)

\-137\-Quantidade Convertida \(SAFX08\)

\- 25 \- Unidade de Medida \- COD\_MEDIDA \(SAFX08\)

\- 64 \- Valor Contábil do Item \- VLR\_CONTAB\_ITEM \(SAFX08\) 

__\[__[__MFS81749__](https://jira.thomsonreuters.com/browse/MFS-81749)__\]__

__Tratamento para Notas de Produtos Farmacêuticos emitidas por Distribuidores:__

<a id="_Hlk75258358"></a>Verificar os critérios a seguir:

- Estabelecimento é um __Distribuidor__ \(atacadista\), ou seja, na Tela de Dados Iniciais estiver com o campo “Contribuinte Varejista?” = Não; 
- <a id="_Hlk78292438"></a>__Produto__ do Item da Nota de Entrada estiver cadastrado, na tela de Parametrização de Produtos Farmacêuticos por Código, no menu: Parametros >  \(IN\-RE 087/20\) > Produtos Farmacêuticos > Código

<a id="_Hlk75258481"></a>Se os dois critérios forem atendidos, então:

            O item de mercadoria dessa nota de entrada não será gravado na tabela EST\_ST\_RS\_NF\_ENT, e a seguinte mensagem será exibida no log:

“*Registro C180: Nota de Entrada de produto farmacêutico amparada pelo art 103/104 do Livro III do RICMS não será gerada no C180”\.*

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Entrada exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

Segundo a IN\-RE 087/20, Tópico 19\.3\-A\.2\.2, alínea “c” os valores unitários médios são os calculados a partir dos valores da entrada\. Veja: 

”*c\) acrescentar ao valor apurado na alínea "b" as informações referentes a todas as entradas de mercadorias, de que trata a alínea "b" do subitem 19\.3\-A\.1, ocorridas durante o dia, que corresponderá à soma das multiplicações da quantidade de cada entrada pelo valor unitário que serviu de base de cálculo do imposto retido por substituição tributária;*”

\(\*\) Segundo o Guia Prático do Sped Fiscal, não se gera nota de modelo 65 de entrada no C100:

* “Este registro deve ser gerado para cada documento fiscal código 01, 1B, 04, 55 e 65 \(saída\), conforme item 4\.1\.1 da Nota Técnica \(Ato COTEPE/ICMS nº 44/2018 e alterações\), registrando a entrada ou saída de produtos ou outras situações que envolvam a emissão dos documentos fiscais mencionados\. As NFC\-e \(código 65\) não devem ser escrituradas nas entradas\.”*

# <a id="_Toc59988569"></a>Gravação dos Dados na Tabela dos Movimentos

Os documentos fiscais de recuperados serão gravados__ item a item__, conforme definido a seguir\.

__Tabela EST\_ST\_RS\_NF\_ENT__

Os campos sinalizados com asterisco compõem a chave da tabela\.

A estrutura da tabela __EST\_ST\_RS\_NF\_ENT__ é baseada na SAFX296\. Contém todos os campos da SAFX296 e campos a mais usados no relatorio de conferência\.

PK

Item

SAFX296

Campo

Regra de Preenchimento

Campos para relatório

\(\*\)

Código do Estabelecimento

COD\_ESTAB\_GER

Código do estabelecimento SELECIONADO na tela de geração\.

Esse campo foi criado, pois no futuro poderemos ter a geração por Inscrição Estadual Única, e nessa opção o estabelecimento selecionado na tela de geração é o centralizador, e as notas fiscais são dos estabelecimentos centralizador e centralizados\.

Não apresentar

__*Campos do layout da SAFX296 \(Item da nota de entrada\)*__

\(\*\)

01

Código da Empresa 

COD\_EMPRESA

Código da empresa da nota de Entrada \(SAFX07\) 

Cod Empresa

\(\*\)

02

Código do Estabelecimento

COD\_ESTAB

Código do estabelecimento da nota de Entrada \(SAFX07\)

Cod Estab

\(\*\)

03

Data Escrita Fiscal

DATA\_FISCAL

Data fiscal da nota de Entrada \(SAFX07\)

Dt Fiscal

\(\*\)

04

Movimento Entrada / Saída

MOVTO\_E\_S

Indicador do movimento da nota de Entrada \(SAFX07\)

E/S

\(\*\)

05

Normal ou Devolução

NORM\_DEV

Indicando de Normal/Devolução da nota de Entrada \(SAFX07\)

Norm/Dev

\(\*\)

06

Tipo do Documento

COD\_DOCTO 

\(IDENT\_DOCTO\)

Tipo do documento da nota de Entrada\.

Cod Docto

\(\*\)

07

08

Pessoa Física/Jurídica

IND\_FIS\_JUR/ COD\_FIS\_JUR

\(IDENT\_FIS\_JUR\)

Pessoa física/jurídica da nota de Entrada \(SAFX07\)

Ind Fis/Jur

Cod Fis/Jur

\(\*\)

09

Número do Documento Fiscal

NUM\_DOCFIS

Número do documento fiscal de Entrada\.

Num Docfis

 

10

Série do Documento Fiscal

SERIE\_DOCFIS

Série do documento fiscal de Entrada\.

Serie

 

11

Subsérie do Documento Fiscal

SUB\_SERIE\_DOCFIS

Subsérie do documento fiscal de Entrada

SubSerie

12 13 14 15

Identificador do Item

DISCRI\_ITEM

Campo identificador do item de mercadoria de Entrada 

\(DISCR\_ITEM da X08\_ITENS\_MERC\)\.

Num Item

16

Quantidade Convertida

Campos da EFD correspondentes: 03 do C180 e 07 do C185\.

QTD\_CONV

Preencher com:

“Qtde Convertida Calculada para o Item da NF de Entrada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  [__*Detalhamento da Nota de Entrada*__](#Detalha_NF_SAI)\.

Qtde Conv \(C180\-03\)

17

Unidade de Medida

Campos da EFD correspondentes:  04 do C180 e 08 do C185\.

COD\_MEDIDA

Campo 14 – Unidade de Medida do Cadastro do Produto \(SAFX2013\), do produto pertencente ao item da nota de Entrada\. *\(ver OBS abaixo sobre os produtos associados\)*

__Sobre os produtos associados:__ Quando se tratar de uma nota fiscal de produto “associado”, a unidade de medida apresentada será a __unidade do produto principal__\.

Medida

\(C180\-04\)

18

Valor Unitário Conv\.

Campos da EFD correspondes: 05 \(C180\), 09 \(C185\) e 05 \(C380\)\.

VLR\_UNIT\_CONV

__\[MFS92521\] __O campo deve ser o valor líquido, não incluindo o ICMS\-ST, mas somente quando o campo IND\_RESP\_RET\_ENT \(COD\_RESP\_RET\) igual a “1” \(Remetente Direto\)\. Quando o responsável é o próprio declarante \(COD\_RESP\_RET=3\) ou remetente indireto \(COD\_RESP\_RET=2\), o valor do ICMS\-ST não compõe o valor contábil, portanto não deve ser deduzido\.

  Se  IND\_RESP\_RET\_ENT = “1” 

      \(VLR\_CONTAB\_ITEM \- Valor do ICMS\-ST\) / QTD\_CONV\_NF\_ENT

  Senão \(COD\_RESP\_RET = “2 ou “3”\)

      VLR\_CONTAB\_ITEM / QTD\_CONV\_NF\_ENT

Onde os valores são oriundos do item da nota de Entrada:

- IND\_RESP\_RET\_ENT é o campo 20\-Responsável Retenção \(SAFX296\);
- VLR\_CONTAB\_ITEM é o campo 64\-Valor Contabil \(SAFX08\) do Item da nota de Entrada;
- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF de Entrada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”
- Valor do ICMS\-ST é oriundo de um dos quatro campos SAFX08, dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor do ICMS\-ST = 52\-VLR\_SUBST\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

         Valor do ICMS\-ST = 145\- VLR\_ICMSS\_N\_ESCRIT\.

    Senão:

        Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                          “133\- VLR\_ICMSS\_NDESTAC” estiverem preenchidos, então:

             Valor do ICMS\-ST = 133\- VLR\_ICMSS\_NDESTAC\.

        Senão:

            Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e 

                             “107\- VLR\_TRIB\_ICMS\_ORIG” estiverem preenchidos, então:

                 Valor do ICMS\-ST = 107\- VLR\_TRIB\_ICMS\_ORIG

Ver  [__*Detalhamento da Nota de Entrada*__](#Detalha_NF_SAI)\.

__Obs__: O valor do ICMS\-ST está sendo subtraído do valor contábil com base na orientação do Guia Prático do Sped Fiscal: 

*“Campo 05 \(VL\_UNIT\_CONV\) – *__*Preenchimento*__*: informar o valor unitário líquido do item/produto \(considerando descontos e acréscimos incondicionais aplicados sobre o valor bruto\)\. O valor unitário do campo 05 não inclui o ICMS ST na aquisição de participante substituto ou nas hipóteses em que o informante é responsável pela substituição\.”*

Essa interpretação foi confirmada com nossa Área de Informação \(CAN\) juntamente com o Carrefour\.

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

Vlr Unit Conv \(C180\-05\)

19

Valor Unitário ICMS Conv\.

Campos da EFD correspondes: 06 \(C180\), 10 \(C185\) e 06 \(C380\)\.

VLR\_ICMS\_CONV

Preencher com:

 Valor do ICMS / QTD\_CONV\_NF\_ENT 

Onde os valores são oriundos do item da nota de Entrada:

- Valor do ICMS é oriundo de um dos três campos SAFX08, dependendo de qual esteja preenchido:

Campo “43\-Valor ICMS”, se preenchido, ou

   Campo “80\-ICMS não Escriturado”, se preenchido, ou

       Campo “225\-Valor ICMS Não Destacado”  

- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF de Entrada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  [__*Detalhamento da Nota de Entrada*__](#Detalha_NF_SAI)\.

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ Arredondar para 6 casas decimais o valor, pois compõe o layout do C180\.

Vlr Unit ICMS Conv \(C180\-06\)

20

Responsável Retenção \(Entradas\)

Campo da EFD corresponde: 02 \(C180\)

IND\_RESP\_RET\_ENT

Este campo será preenchido de acordo com os campos 131\- Indicador de ICMS\-ST e 132 – Situação Especial – Substituição Tributária que estiver preenchido na SAFX08 \(referente ao item de entrada recuperado\)\. De acordo com as regras abaixo:

Se campo “132 – Situação Especial – Substituição Tributária” igual a ‘1’, então:

   O campo será preenchido com o valor igual a “3” – Próprio Declarante

Senão

     Se campo “131\- Indicador de ICMS\-ST” igual a ‘1’, então:

         O campo será preenchido com o valor igual a “1” – Remetente Direto

     Se campo “131\- Indicador de ICMS\-ST” igual a ‘2’, então:

         O campo será preenchido com o valor igual a “2” – Remetente Indireto

Cod Resp \(C180\-02\)

21

Valor Unitário BC ICMS\-ST Conv\. \(Entradas\)

Campo da EFD corresponde: 07 \(C180\)

VLR\_UNIT\_BC\_ICMSS\_ENT

Preencher com:

 Valor da BC\-ST / QTD\_CONV\_NF\_ENT

Onde os valores são oriundos do item da nota de Entrada:

- Valor da BC\-ST é oriundo de um dos quatro campos SAFX08, dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor da BC\-ST = 61\-BASE\_SUB\_TRIB\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

       Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

    Senão:

       Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                        “133\- VLR\_ICMSS\_NDESTAC” preenchidos, então:

          Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

       Senão:

           Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e 

                            “107\- VLR\_TRIB\_ICMS\_ORIG” preenchidos, então:

               Valor da BC\-ST = 106 \- VLR\_BASE\_ICMS\_ORIG

- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF de Entrada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  [__*Detalhamento da Nota de Entrada*__](#Detalha_NF_SAI)\.

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ Arredondar para 6 casas decimais o valor, pois compõe o layout do C180\.

Vlr Unit BC ICMS\-ST Conv \(C180\-07\)

22

Valor Unitário ICMS\-ST Conv\.  \(Entradas\)

Campo da EFD corresponde: 08 \(C180\)\.

VLR\_UNIT\_ICMSS\_CONV\_ENT

O preenchimento do campo seria:

 \(Valor do ICMS\-ST \+ Valor do FECEP\-ST\) / QTD\_CONV\_NF\_ENT

Mas deve\-se tratar o caso do Valor do ICMS\-ST já conter o FECEP\-ST, para que este não seja somado duas vezes\. 

Como premissa, a tabela DATAMART já contém o FECEP\-ST embutido no campo 52\-ICMS\-ST, pois na equalização do DATA MART, os clientes são orientados a marcar o parâmetro para Somar FECEP ao ICMS/ICMS\-ST, quando o FECEP não “nasce” embutido ao ICMS/ICMS\-ST nas tabelas “normais” X07/X08\. 

Quanto às tabelas “normais”, o FECEP pode ou não estar embutido campo 52\-ICMS\-ST via importação da SAFX08, por isso existe o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” da tela de Dados Iniciais \(menu Parâmetros 🡪 IN\-RE 087/2020 🡪 Dados Iniciais\)\.__ \[MFS65137\]__\.

Tratamento do FECEP embutido nos vlrs de ICMS/ICMS\-ST \(aplicado às Entradas e Devoluções de Entradas\):

  Se o item de mercadoria foi recuperado das tabelas “normais” \(X07/X08\), então:

        Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST 

        nos itens \(SAFX08\)” foi marcado na tela de Dados Iniciais, então:

             Se for considerado o “52\-Valor ICMS Substituição Tributária” p/ o

             __Valor do ICMS\-ST__ \(\*\):

    Preencher com: \(Valor do ICMS\-ST\) / QTD\_CONV\_NF\_ENT 

Senão:

                  Preencher com:

                  \(Valor do ICMS\-ST \+ Valor do ICMS\-ST FECEP\) / 

                  QTD\_CONV\_NF\_ENT

        Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST

        nos itens \(SAFX08\)” não foi marcado, então:

             Preencher com:  

             \(Valor do ICMS\-ST \+ Valor do ICMS\-ST FECEP\) /

             QTD\_CONV\_NF\_ENT

  Se o item de mercadoria foi recuperado das tabelas do DATAMART, então:

       Se for considerado o “52\-Valor ICMS Substituição Tributária” para o  

__       Valor do ICMS\-ST__ \(\*\):

           Preencher com: \(Valor do ICMS\-ST\) / QTD\_CONV\_NF\_ENT

       Senão

           Preencher com:

          \(Valor do ICMS\-ST \+ Valor do ICMS\-ST FECEP\) /

          QTD\_CONV\_NF\_ENT

__\[MFS543860\]__ Tratamento do parâmetro para identificar se o valor do FECP está embutido nos valores de ICMS não destacado/não escriturado

Tratamento do FECEP embutido nos valores de ICMS\-ST não escriturado e não destacado \(aplicado às Entradas e Devoluções de Entradas\):

    Se o parâmetro “Valores de FECEP estão embutidos nos valores de ICMS\-ST não destacado/não escriturado” for marcado na tela de Dados Iniciais, então:

             Se for considerado o campo “145\- VLR\_ICMSS\_N\_ESCRIT” p/ o

             __Valor do ICMS\-ST__ \(\*\):

    Preencher com: \(VLR\_ICMSS\_N\_ESCRIT\) / QTD\_CONV\_NF\_ENT 

Senão:

                  Preencher com:

                  \(VLR\_ICMSS\_N\_ESCRIT \+ Valor do ICMS\-ST FECEP\) / 

                  QTD\_CONV\_NF\_ENT

            Se for considerado o campo “133\- VLR\_ICMSS\_NDESTAC” p/ o

             __Valor do ICMS\-ST__ \(\*\):

    Preencher com: \(VLR\_ICMSS\_NDESTAC\) / QTD\_CONV\_NF\_ENT 

Senão:

                  Preencher com:

                  \(VLR\_ICMSS\_NDESTAC \+ Valor do ICMS\-ST FECEP\) / 

                  QTD\_CONV\_NF\_ENT

        Se o parâmetro “Valores de FECEP estão embutidos nos valores de ICMS\-ST não destacado/não escriturado” não for marcado, então:

             Preencher com:  

             \(VLR\_ICMSS\_N\_ESCRIT \+ Valor do ICMS\-ST FECEP\) / QTD\_CONV\_NF\_ENT

              OU

             \(VLR\_ICMSS\_NDESTAC \+ Valor do ICMS\-ST FECEP\) / QTD\_CONV\_NF\_ENT

             

Onde os valores são oriundos do item da nota de Entrada:

- \(\*\)__Valor do ICMS\-ST__ é oriundo de um dos quatro campos SAFX08, dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor do ICMS\-ST = 52\-VLR\_SUBST\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

         Valor do ICMS\-ST = 145\- VLR\_ICMSS\_N\_ESCRIT\.

    Senão:

        Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                         “133\- VLR\_ICMSS\_NDESTAC” preenchidos, então:

             Valor do ICMS\-ST = 133\- VLR\_ICMSS\_NDESTAC\.

        Senão:

            Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e 

                             “107\- VLR\_TRIB\_ICMS\_ORIG” preenchidos, então:

                 Valor do ICMS\-ST = 107\- VLR\_TRIB\_ICMS\_ORIG

- Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08\.
- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF de Entrada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  [__*Detalhamento da Nota de Entrada*__](#Detalha_NF_SAI)\.

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ Arredondar para 6 casas decimais o valor, pois compõe o layout do C180\.

Vlr Unit ICMS\-ST Conv \(C180\-08\)

23

Valor Unitário FCP\-ST Conv\.  \(Entradas\)

Campo da EFD corresponde: 09 \(C180\)\.

VLR\_UNIT\_FCP\_CONV\_ENT

Preencher com:

Valor do FECEP\-ST/ QTD\_CONV\_NF\_ENT

Onde os valores são oriundos do item da nota de Entrada:

- Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08\.
- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF de Entrada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  [__*Detalhamento da Nota de Entrada*__](#Detalha_NF_SAI)\.

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ Arredondar para 6 casas decimais o valor, pois compõe o layout do C180\.

Vlr Unit FCP\-ST Conv \(C180\-09\)

 

24

Código Motivo \(Saídas\)

Campos da EFD correspondes: 06 \(C185\) e 02 \(C380\)\.

COD\_MOTIVO\_SAI

Não Preencher\. Esse campo da SAFX296 é utilizado nas notas de saídas\.

Não Apresentar

 

25

Valor Unitário ICMS na Oper\. Conv\. \(Saídas\)

Campos da EFD correspondes: 11 \(C185\) e 07 \(C380\)\.

VLR\_UNIT\_ICMS\_OPER\_SAI

Não Preencher\. Esse campo da SAFX296 é utilizado nas notas de saídas\.

Não Apresentar

26

Valor Unitário ICMS Estoque Conv\. \(Saídas\)

Campos da EFD correspondes: 12 \(C185\) e 08 \(C380\)\.

VLR\_UNIT\_ICMS\_ESTQ\_SAI

Não Preencher\. Esse campo da SAFX296 é utilizado nas notas de saídas\.

Não Apresentar

27

Valor Unitário ICMS\-ST Estoque Conv\. \(Saídas\)

Campos da EFD correspondes: 13 \(C185\) e 09 \(C380\)\.

VLR\_UNIT\_ICMSS\_ESTQ\_SAI

Não Preencher\. Esse campo da SAFX296 é utilizado nas notas de saídas\.

Não Apresentar

28

Valor Unitário FCP\-ST Estoque Conv\. \(Saídas\)

Campos da EFD correspondes: 14 \(C185\) e 10 \(C380\)\.

VLR\_UNIT\_FCP\_ESTQ\_SAI

Não Preencher\. Esse campo da SAFX296 é utilizado nas notas de saídas\.

Não Apresentar

29

Valor Unitário ICMS\-ST Conv\. Rest\. \(Saídas\)

Campos da EFD correspondes: 15 \(C185\) e 11 \(C380\)\.

VLR\_UNIT\_ICMSS\_REST\_SAI

Não Preencher\. Esse campo da SAFX296 é utilizado nas notas de saídas\.

Não Apresentar

30

Valor Unitário FCP\-ST Conv\. Rest\. \(Saídas\)

Campos da EFD correspondes: 16 \(C185\) e 12 \(C380\)\.

VLR\_UNIT\_FCP\_REST\_SAI

Não Preencher\. Esse campo da SAFX296 é utilizado nas notas de saídas\.

Não Apresentar

31

Valor Unitário ICMS\-ST Conv\. Compl\. \(Saídas\)

Campos da EFD correspondes: 17 \(C185\) e 13 \(C380\)\.

VLR\_UNIT\_ICMSS\_COMPL\_SAI

Não Preencher\. Esse campo da SAFX296 é utilizado nas notas de saídas\.

Não Apresentar

32

Valor Unitário FCP\-ST Conv\. Compl\. \(Saídas\)

Campos da EFD correspondes: 18 \(C185\) e 14 \(C380\)\.

VLR\_UNIT\_FCP\_COMPL\_SAI

Não Preencher\. Esse campo da SAFX296 é utilizado nas notas de saídas\.

Não Apresentar

__*Parametrização do Produto \(por Código, NCM ou CEST\)*__

Produto da NF 

GRUPO\_PROD\_NF

IND\_PROD\_NF

COD\_PROD\_NF

Produto do item da nota de entrada\.

Ind Produto

\(SAFX2013\-01\)

Cod Produto \(SAFX2013\-02\)

Unidade de Medida do Produto NF

COD\_MEDIDA\_PROD\_NF

Unidade de Medida do Produto da nota de entrada \(SAFX2013 – campo 14 – COD\_MEDIDA\)

Medida Produto \(SAFX2013\-14\)

NCM do Produto NF

COD\_NBM\_PROD\_NF

Código NBM do Produto da nota de entrada \(SAFX2013 – campo 05 – Código NBM\)

NCM Produto \(SAFX2013\-05\)

CEST do Produto NF

COD\_CEST\_PROD\_NF

Código CEST do Produto da nota de entrada \(SAFX2013 – campo 54 – Código Especificador da Substituição Tributária\)

CEST Produto \(SAFX2013\-54\)

Produto Principal

GRUPO\_PROD\_PRINC

IND\_PROD\_PRINC

COD\_PROD\_PRINC

Caso o produto do item da nota de entrada tenha sido parametrizado por Código \(menu “Parâmetros 🡪 Produtos 🡪 Por Código”\) apresentar o Produto Principal \(grupo, indicador e código\)\.

Não Apresentar

Unidade de Medida do Produto Principal

COD\_MEDIDA\_PROD\_PRINC

Caso o produto do item da nota de entrada tenha sido parametrizado por Código \(menu “Parâmetros 🡪 Produtos 🡪 Por Código”\) apresentar a Unidade de Medida do Produto Principal \(SAFX2013 – campo 14 – COD\_MEDIDA\)\.

Não Apresentar

<a id="Detalha_NF_SAI"></a>__*Detalhamento da Nota de Entrada *__

Quantidade do Item da NF de Entrada \(safx08 – item 24\)

QTD\_NF\_ENT

Campo 24\-Quantidade \(SAFX08\) do item da nota fiscal de Entrada\.

Qtde Item \(SAFX08\-24\)

Quantidade Convertida do Item da NF de Entrada \(safx08 – item137\)

QTD\_CONV\_X08\_NF\_ENT

Campo 137 – Quantidade Convertida \(SAFX08\) do item da nota fiscal de Entrada

Qtde Conv Item \(SAFX08\-137\)

Unidade de Medida do Item da NF de Entrada 

\(safx08 \- item 25\)

COD\_MEDIDA\_NF\_ENT

Campo 25 – Unidade de Medida \(SAFX08\) do item da nota fiscal de Entrada\.

Medida Item \(SAFX08\-25\)

Fator Conversão

FAT\_CONV\_NF\_ENT

Preecher com o Fator de Conversão utilizado na regra do campo “Qtde Convertida Calculada para o Item da Nota de Entrada \(QTD\_CONV\_NF\_ENT\)” a seguir\.

__Se__ unidade da nota = unidade do cadastro do produto, então:__  __

__    __Campo será preenchido com 1;

__Senão __

     Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\), então:

         Campo não será preenchido;

     Senão         

           Se não encontrado Fator de Conversão nos Cadastros de Conversão de 

           Unidades de Medidas, então:

                Campo será preenchido com \-1;

           Senão

                 Campo será preenchido com o Fator de Conversão encontrado\.

Fator Conv \(Cadastro Conversão Medida\)

Qtde Convertida Calculada para o Item da NF de Entrada

\(<a id="QTD_CONV_NF_ENT"></a>QTD\_CONV\_NF\_ENT\)

QTD\_CONV\_NF\_ENT

Campo 24\-Quantidade \(SAFX08\) do Item da nota de Entrada, aplicando a conversão, quando necessário\. Veja:

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\)  __*\(ver OBS abaixo sobre os produtos associados\)*

      __\(\*\)__ unidade da nota = campo “25\-Unidade de Medida” da SAFX08 do Item da NF de Entrada

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será gerado a própria quantidade do item da nota;

__Senão __

     Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\)

         Nesse caso, será utilizada a informação da quantidade já convertida do campo “137\-Quantidade Convertida”;

     Senão         

         Nesse caso a quantidade do item \(SAFX08\) será convertida para a unidade de medida do cadastro do produto;

         \[ Quantidade do item da nota \(SAFX08\) \* Fator de Conversão \]

__Sobre os produtos associados:__ Quando se tratar de uma nota fiscal de produto “associado”, a comparação será feita da unidade de medida da nota, com a __unidade do produto principal__\.

Exemplo:

__Produto principal__: COCA\-COLA PET                 \(unidade de medida do estoque – SAFX2013 = UN\) 

__Produtos associados__: COCA\-COLA PET–1      \(unidade de medida do estoque – SAFX2013 = PAC \(6 unidades\)\)

Nota de venda do produto associado: __COCA\-COLA PET\-1__, unidade da nota = PAC, Quantidade = __5__

Compara a unidade de medida da nota do produto associado com a unidade de estoque do produto principal: PAC x UN

Como é diferente, deve\-se converter a quantidade da nota de PAC para UN\. 

Para acessar a tabela de conversão por produto, será utilizado o código do produto principal:

__DWT\_CONV\_MEDIDA\-2: __Produto = __COCA\-COLA PET__

                                          Unidade Origem = PAC

                                          Unidade Destino = UN

                                          Fator de conversão = 6,0000

Conversão da quantidade da nota do associado:  QTD da nota x Fator de Conversão   =  5 x 6,0000 = 30,0000 

Lembrando que, quando não existe fator na tabela de conversão por produto \(DWT\_CONV\_MEDIDA\_2\), será utilizada a tabela padrão \(DWT\_CONV\_MEDIDA\)\.  

__= = = = =__

__Sobre a conversão de medida:__

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas será gravada a seguinte mensagem de erro no log:

“*Registro C180: Fator de conversão de medida de XXX para XXX não encontrado\. Nota de Entrada será gerada no C180 sem Quantidade Convertida e valores unitários da Mercadoria, do ICMS, BC\-ST, ICMS\-ST e FCP \(campos 3 e 5 a 9\)”\.*

\(O primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Entrada exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

Não Apresentar pois já é o campo Qtde Conv \(C180\-03\)

Valor Contabil do Item da NF de Entrada 

\(safx08 – item 64\)

VLR\_CONTAB\_ENT

Campo 64\-“Vlr Contabil do Item”\(SAFX08\) do item da nota fiscal de Entrada\.

Vlr Contabil Item \(SAFX08\-64\)

Valor do ICMS do Item da NF de Entrada 

VLR\_ICMS\_ENT

Valor do ICMS é oriundo de um dos três campos do item da nota fiscal de Entrada \(SAFX08\), dependendo de qual esteja preenchido:

Campo “43\-Valor ICMS”, se preenchido, ou

   Campo “80\-ICMS não Escriturado”, se preenchido, ou

       Campo “225\-Valor ICMS Não Destacado”  

Vlr ICMS Item \(SAFX08\-43,80,225\)

Valor da BC\-ST do Item da NF de Entrada 

VLR\_BC\_ST\_ENT

Valor da Base de Cálculo do ICMS\-ST é oriundo de um dos quatro campos do item da nota fiscal de Entrada \(SAFX08\), dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor da BC\-ST = 61\-BASE\_SUB\_TRIB\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

       Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

    Senão:

       Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                        “133\- VLR\_ICMSS\_NDESTAC” preenchidos, então:

          Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

       Senão:

           Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e 

                             “107\- VLR\_TRIB\_ICMS\_ORIG” preenchidos, então:

               Valor da BC\-ST = 106 \- VLR\_BASE\_ICMS\_ORIG

Vlr BC ICMS\-ST Item \(SAFX08\-61,144,106\)

Valor do ICMS\-ST do Item da NF de Entrada 

VLR\_ICMS\_ST\_ENT

Valor do ICMS\-ST é oriundo de um dos quatro campos do item da nota fiscal de Entrada \(SAFX08\), dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor do ICMS\-ST = 52\-VLR\_SUBST\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

         Valor do ICMS\-ST = 145\- VLR\_ICMSS\_N\_ESCRIT\.

    Senão:

        Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                         “133\- VLR\_ICMSS\_NDESTAC” preenchidos, então:

             Valor do ICMS\-ST = 133\- VLR\_ICMSS\_NDESTAC\.

        Senão:

            Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e 

                             “107\- VLR\_TRIB\_ICMS\_ORIG” preenchidos, então:

                 Valor do ICMS\-ST = 107\- VLR\_TRIB\_ICMS\_ORIG

Vlr ICMS\-ST Item \(SAFX08\-52,145,133,107\)

Valor do FECEP\-ST do Item da NF de Entrada 

VLR\_FECEP\_ST\_ENT

Valor do FECEP\-ST é oriundo do item da nota fiscal de Entrada \(SAFX08\):

- Campo 140\-FECEP ICMS\-ST da SAFX08\.

Vlr FECEP\-ST Item \(SAFX08\-144\)

Data Emissão

DATA\_EMISSAO

Data Emissão da SAFX07 \(campo 11 da SAFX07\)

__*Dados para o “Cálculo da Média Pondera Móvel dos Valores Unitários” alínea “c” do 19\.3\-A\.2\.2 da IN\-RE 087/20*__

Quantidade Entrada Convertida \(a\)

QTD\_CONV\_ENT\_MP

__Igual ao campo 16 – Quantidade Convertida \(QTD\_CONV\)__

Preencher com:

“Qtde Convertida Calculada para o Item da NF de Entrada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  [__*Detalhamento da Nota de Entrada*__](#Detalha_NF_SAI)\.

Não Apresentar pois já é o campo Qtde Conv \(C180\-03\)

Valor Médio Unitário do ICMS  \(b\)

VLR\_UNIT\_ICMS\_ENT\_MP

__Igual ao campo 19 \- Valor Unitário ICMS Conv\. \(VLR\_ICMS\_CONV\)__

Preencher com:

 Valor do ICMS / QTD\_CONV\_NF\_ENT 

Onde os valores são oriundos do item da nota de Entrada:

- Valor do ICMS é oriundo de um dos três campos SAFX08, dependendo de qual esteja preenchido:

Campo “43\-Valor ICMS”, se preenchido, ou

   Campo “80\-ICMS não Escriturado”, se preenchido, ou

       Campo “225\-Valor ICMS Não Destacado”  

- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF de Entrada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  [__*Detalhamento da Nota de Entrada*__](#Detalha_NF_SAI)\.

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ Arredonda para 8 casas decimais, pois o campo é utilizado no Cálculo da Média Ponderada\.

Vlr Unit ICMS \(p/ Cálculo da Média Ponderada\)

Valor Médio Unitário do ICMS\-ST \(c\)

VLR\_UNIT\_ICMS\_ST\_ENT\_MP

__Não é igual ao campo 22 \- Valor Unitário ICMS\-ST Conv\. \(Entradas\)  \(VLR\_UNIT\_ICMSS\_CONV\_ENT\)__

O preenchimento do campo seria:

 Valor do ICMS\-ST/ QTD\_CONV\_NF\_ENT

Mas para cálculo da Média Ponderada, precisamos separar o FECEP\-ST do ICMS\-ST\. O motivo é que na geração da Saída e Devolução de Saída o campo VLR\_UNIT\_ICMSS\_ESTQ\_SAI \(13 \(C185\) e 09 \(C380\)\) é resultante da soma do ICMS\-ST e FECEP\-ST oriundos do Cálculo da Média Ponderada \(EST\_ST\_RS\_MEDIA\_POND\)\. Se não calcularmos e gravá\-los separadamente na tabela EST\_ST\_RS\_MEDIA\_POND, o FECEP\-ST pode sair duplicado no campo VLR\_UNIT\_ICMSS\_ESTQ\_SAI\.

Tratamento do FECEP embutido nos vlrs de ICMS/ICMS\-ST \(aplicado às Entradas e Devoluções de Entradas\):

Se o item de mercadoria foi recuperado das tabelas “normais” \(X07/X08\), então:

      Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST 

      nos itens \(SAFX08\)” foi marcado da tela de Dados Iniciais \(menu 

      Parâmetros 🡪 IN\-RE 087/2020 🡪 Dados Iniciais\)\.__ \[MFS65137\]__, então:

             Se for considerado o “52\-Valor ICMS Substituição Tributária” p/ o

             __Valor do ICMS\-ST__ \(\*\):

    Preencher com: 

    \(Valor do ICMS\-ST\- Valor do ICMS\-ST FECEP\) /

    QTD\_CONV\_NF\_ENT 

Senão:

                  Preencher com:

                  \(Valor do ICMS\-ST\) / QTD\_CONV\_NF\_ENT

      Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST

      nos itens \(SAFX08\)” não foi marcado, então:

           Preencher com:  

             \(Valor do ICMS\-ST\) / QTD\_CONV\_NF\_ENT

Se o item de mercadoria foi recuperado das tabelas do DATAMART, então:

     Se for considerado o “52\-Valor ICMS Substituição Tributária” para o  

__     Valor do ICMS\-ST__ \(\*\):

           Preencher com:  

            \(Valor do ICMS\-ST \- Valor do ICMS\-ST FECEP\) 

             / QTD\_CONV\_NF\_ENT

     Senão

           Preencher com:

          \(Valor do ICMS\-ST\) / QTD\_CONV\_NF\_ENT

__\[MFS543860\]__ Tratamento do parâmetro para identificar se o valor do FECP está embutido nos valores de ICMS não destacado/não escriturado

Tratamento do FECEP embutido nos valores de ICMS\-ST não escriturado e não destacado \(aplicado às Entradas e Devoluções de Entradas\):

    Se o parâmetro “Valores de FECEP estão embutidos nos valores de ICMS\-ST não destacado/não escriturado” for marcado na tela de Dados Iniciais, então:

             Se for considerado o campo “145\- VLR\_ICMSS\_N\_ESCRIT” p/ o

             __Valor do ICMS\-ST__ \(\*\):

    Preencher com: \(VLR\_ICMSS\_N\_ESCRIT \- Valor do ICMS\-ST FECEP\) / QTD\_CONV\_NF\_ENT 

Senão:

                  Preencher com: VLR\_ICMSS\_N\_ESCRIT / QTD\_CONV\_NF\_ENT

            Se for considerado o campo “133\- VLR\_ICMSS\_NDESTAC” p/ o

             __Valor do ICMS\-ST__ \(\*\):

    Preencher com: \(VLR\_ICMSS\_NDESTAC\- Valor do ICMS\-ST FECEP\) / QTD\_CONV\_NF\_ENT 

Senão:

                  Preencher com: VLR\_ICMSS\_NDESTAC / QTD\_CONV\_NF\_ENT

        Se o parâmetro “Valores de FECEP estão embutidos nos valores de ICMS\-ST não destacado/não escriturado” não for marcado, então:

             Preencher com:  

             \(VLR\_ICMSS\_N\_ESCRIT \+ Valor do ICMS\-ST FECEP\) / QTD\_CONV\_NF\_ENT

              OU

             \(VLR\_ICMSS\_NDESTAC \+ Valor do ICMS\-ST FECEP\) / QTD\_CONV\_NF\_ENT

             

Onde os valores são oriundos do item da nota de Entrada:

- \(\*\)__Valor do ICMS\-ST__ é oriundo de um dos quatro campos SAFX08, dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor do ICMS\-ST = 52\-VLR\_SUBST\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

         Valor do ICMS\-ST = 145\- VLR\_ICMSS\_N\_ESCRIT\.

    Senão:

        Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                         “133\- VLR\_ICMSS\_NDESTAC” preenchidos, então:

             Valor do ICMS\-ST = 133\- VLR\_ICMSS\_NDESTAC\.

        Senão:

            Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e 

                             “107\- VLR\_TRIB\_ICMS\_ORIG” preenchidos, então:

                 Valor do ICMS\-ST = 107\- VLR\_TRIB\_ICMS\_ORIG

- Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08\.
- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF de Entrada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  [__*Detalhamento da Nota de Entrada*__](#Detalha_NF_SAI)\.

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ Arredonda para 8 casas decimais, pois o campo é utilizado no Cálculo da Média Ponderada\.

Vlr Unit ICMS\-ST\(s/ FECEP\-ST\) \(p/ Cálculo da Média Ponderada\)

Valor Médio Unitário da Base de Cálculo do ICMS\-ST \(d\)

VLR\_UNIT\_BC\_ST\_ENT\_MP

__Igual ao campo 21 \- Valor Unitário BC ICMS\-ST Conv\. \(Entradas\) \(VLR\_UNIT\_BC\_ICMSS\_ENT\)__

Preencher com:

 Valor da BC\-ST / QTD\_CONV\_NF\_ENT

Onde os valores são oriundos do item da nota de Entrada:

- Valor da BC\-ST é oriundo de um dos quatro campos SAFX08, dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor da BC\-ST = 61\-BASE\_SUB\_TRIB\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

       Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

    Senão:

       Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e

                        “133\- VLR\_ICMSS\_NDESTAC” preenchidos, então:

          Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

       Senão:

           Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e 

                            “107\- VLR\_TRIB\_ICMS\_ORIG” preenchidos, então:

               Valor da BC\-ST = 106 \- VLR\_BASE\_ICMS\_ORIG

- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF de Entrada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  [__*Detalhamento da Nota de Entrada*__](#Detalha_NF_SAI)\.

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ Arredonda para 8 casas decimais, pois o campo é utilizado no Cálculo da Média Ponderada\.

Vlr Unit BC ICMS\-ST \(p/ Cálculo da Média Ponderada\)

Valor Médio Unitário do FECEP\-ST \(e\)

VLR\_UNIT\_FECEP\_ST\_ENT\_MP

__Igual ao campo 23 \- Valor Unitário FCP\-ST Conv\.  \(Entradas\) \(VLR\_UNIT\_FCP\_CONV\_ENT\)__

Preencher com:

Valor do FECEP\-ST/ QTD\_CONV\_NF\_ENT

Onde os valores são oriundos do item da nota de Entrada:

- Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08\.
- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF de Entrada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  [__*Detalhamento da Nota de Entrada*__](#Detalha_NF_SAI)\.

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ Arredonda para 8 casas decimais, pois o campo é utilizado no Cálculo da Média Ponderada\.

Vlr Unit FECEP\-ST \(p/ Cálculo da Média Ponderada\)

Valor do ICMS Calculado para Entrada \(f\) = \(a \* b\)

VLR\_ICMS\_ENT\_MP

Preencher com:

\[Quantidade Entrada Convertida \(a\) \* Valor Médio Unitário do ICMS  \(b\)\]

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ Arredonda para 8 casas decimais, pois o campo é utilizado no Cálculo da Média Ponderada\.

Vlr ICMS \(p/ Cálculo da Média Ponderada\)

Valor do ICMS\-ST Calculado para Entrada \(g\) = \(a \* c\)

VLR\_ICMS\_ST\_ENT\_MP

Preencher com:

\[Quantidade Entrada Convertida \(a\) \* Valor Médio Unitário do ICMS\-ST \(c\)\]

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ Arredonda para 8 casas decimais, pois o campo é utilizado no Cálculo da Média Ponderada\.

Vlr ICMS\-ST\(s/ FECEP\-ST\) \(p/ Cálculo da Média Ponderada\)

Valor Base de Cálculo do ICMS\-ST Calculado para Entrada \(h\) = \(a \* d\)

VLR\_BC\_ST\_ENT\_MP

Preencher com:

\[Quantidade Entrada Convertida \(a\) \* Valor Médio Unitário da Base de Cálculo do ICMS\-ST \(d\)\]

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ Arredonda para 8 casas decimais, pois o campo é utilizado no Cálculo da Média Ponderada\.

Vlr BC ICMS\-ST \(p/ Cálculo da Média Ponderada\)

Valor FECEP\-ST Calculado para Entrada \(i\) = \(a \* e\)

VLR\_FECEP\_ST\_ENT\_MP

Preencher com:

\[Quantidade Entrada Convertida \(a\) \* Valor Médio Unitário do FECEP\-ST \(e\)\]

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ Arredonda para 8 casas decimais, pois o campo é utilizado no Cálculo da Média Ponderada\.

Vlr FECEP\-ST \(p/ Cálculo da Média Ponderada\)

# <a id="_Toc59988570"></a>RELATORIO DE CONFERÊNCIA

Gerar um arquivo excel a partir da leitura da tabela __EST\_ST\_RS\_NF\_ENT__

Nome do arquivo: Relatório\_Conferencia\_C180\_mm\_aaaa\_cod\_estab\.xlsx

= = = = = =

 

