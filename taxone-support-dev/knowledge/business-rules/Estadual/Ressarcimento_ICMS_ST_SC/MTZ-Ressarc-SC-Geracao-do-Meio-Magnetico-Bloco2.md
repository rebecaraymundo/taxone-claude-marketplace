# MTZ-Ressarc-SC-Geracao-do-Meio-Magnetico-Bloco2

- **Fonte:** MTZ-Ressarc-SC-Geracao-do-Meio-Magnetico-Bloco2.docx
- **Modificado:** 2022-09-12
- **Tamanho:** 149 KB

---

THOMSON REUTERS

Módulo Ressarcimento e Complemento ICMS\-ST – SC \(Portaria SEF 378/2018\)

Geração do Meio Magnético 

Bloco 2

__Localização__: Menu Estadual, módulo Ressarcimento de ICMS\-ST – SC \(Port\.SEF 378/2018\), menu Geração à Geração do Meio Magnético

Este documento é específico das regras de geração do Bloco 2\.

Para as regras gerais da geração do arquivo, consultar o doc “__MTZ\-Ressarc\-SC\-Geracao\-do\-Meio\-Magnetico__”

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS25525__

Geração do Meio Magnético 

Criação da geração do meio magnético da Portaria SEF 378/2018 \- SC

11/04/2019

\(criação do documento\)

__MFS25526__

Geração do Meio Magnético

Geração dos registros 2114 e 2132

22/05/2019

__MFS30131__

Geração do campo 16 do 2113 

Geração do campo 16 do registro 2113

30/08/2019

__MFS29416__

Geração do novo registro 2115

Geração do novo registro 2115, conforme Portaria SEF 208/2019

02/09/2019

__MFS30185__

Geração do novo registro 2133

Geração do novo registro 2133, conforme Portaria SEF 208/2019

05/09/2019

__MFS33079__

Geração do novo registro 2131

Geração do novo registro 2131, conforme Portarias SEF 378/2018 e SEF 208/2019 

23/12/2019

__MFS32267__

Alteração na geração do registro 2130

Tratamento de erro dado no validador para o campo 15 do registro 2130

26/12/2019

__MFS32575__

Alteração na geração do registro 2110

Tratamento de erro dado no validador para os campos 6,7 e 10 do registro 2110

06/01/2020

__MFS32070__

Geração do novo registro 2134

Geração do novo registro 2134, conforme Portaria SEF 343/2019 

04/03/2020

__MFS34795__

Geração do novo registro 2131

Geração do novo registro 2121 e alteração do registro 2120, conforme Portaria SEF 343/2019

12/03/2020

__MFS36656__

Alteração na geração do registro 2130

Tratamento de erro dado no validador para o campo 16 do registro 2130

19/05/2020

__MFS37144__

Alteração na geração do registro 2113

Tratamento de erro dado no validador para o campo 16 do registro 2113

22/05/2020

__MFS40583__

Alteração na geração do registro 2113

Alterada a geração do campo 06\-DT\_E do 2113, nos casos de notas de devolução

14/07/2020

__MFS46100__

Atualização legal Port\. SEF 262/20

Revogação do registro 2131, pela Portaria SEF 262/2020, de 02/10/2020 \(ver item 13\)\.

27/10/2020

__MFS46103__

Atualização legal Port\. SEF 262/20

Alteração do registro 2112 para inclusão do campo 07\-CNPJ \(ver item 6\)\.

28/10/2020

__MFS46143__

Atualização legal Port\. SEF 262/20

Alteração dos registros 2113, para inclusão do campo 17\-CNPJ e 2130, para inclusão do campo 27\-CNPJ \(ver itens 7 e 12\)\.

29/10/2020

__MFS64687__

Atualização Legal Port\. SEF N° 159/2021

Registro 2113 – campo 16 \- Tratamento das novas operações:

40 \- Venda óleo diesel para transporte coletivo de passageiros \(e Devoluções\)

50 \- Venda de óleo diesel para embarcação pesqueira, com benefício de isenção \(e Devoluções\)

24/06/2021

__MFS58553__

Atualização Legal da Port\. SEF 013/2021

Geração do novo registro de Nota Fiscal Eletrônica de Ajuste \(2135\)

Tratamento bastante semelhante ao aplicado às notas complementares \(MFS30185\)\.

04/08/2021

__MFS46838__

Tratamento do Perfil D

Alteração no registro 2112 – campo 07 – CNPJ\.

Alteração no registro 2113 – campo 17 – CNPJ\.

Alteração no registro 2130 – campo 27 – CNPJ\.

Alteração na recuperação da movimentação para geração dos registros 2114 e 2115 \(filhos do 2113\)\.

Alteração na recuperação da movimentação para geração dos registros 2131, 2132, 2133 e 2135 \(filhos do 2130\)\.

21/09/2021

Sumário

[1\.	Regras Gerais do Bloco 2	1](#_Toc78989878)

[2\.	Registro 2001 – Abertura do Bloco 2	1](#_Toc78989879)

[3\.	Registro 2100 – Demonstrativo da Apuração Mensal do Ressarcimento / Complemento	1](#_Toc78989880)

[4\.	Registro 2110 \- Demonstrativo da Apuração Mensal do Ressarcimento / Complemento por Produto	1](#_Toc78989881)

[5\.	Registro 2111 – Complemento de Identificação do Item	1](#_Toc78989882)

[6\.	Registro 2112 – Totais dos Documentos Fiscais de Vendas a Consumidor Final \(ECF\)	1](#_Toc78989883)

[7\.	Registro 2113 – Documentos Fiscais de Vendas	1](#_Toc78989884)

[8\.	Registro 2114 – Complemento de Documento Fiscal Referenciado na Devolução de Vendas	1](#_Toc78989885)

[9\.	Registro 2115 – Nota Fiscal Complementar que Referenciou a Nota de Saída Informada no Registro 2113	1](#_Toc78989886)

[10\.	Registro 2120: Valor Médio Mensal Unitário das Entradas da Base de Cálculo da Substituição Tributária para Apuração de Entrada de Mercadoria identificada no Registro 2110, incluindo NF\-e de Remetente Indireto com tag específica informada no XML	1](#_Toc78989887)

[11\.	Registro 2121: Valor Médio Mensal Unitário da Base de Cálculo da Substituição Tributária para Apuração de Entrada de Mercadoria identificada no Registro 2110 \- todas NF\-e informadas no Registro 2130	1](#_Toc78989888)

[12\.	Registro 2130: Documentos Fiscais de Entradas	1](#_Toc78989889)

[13\.	Registro 2131: Documento Fiscal Referenciado, emitido pelo Substituto Tributário, referente a Entrada de Mercadoria Adquirida de Remetente Indireto	1](#_Toc78989890)

[14\.	Registro 2132: Complemento de Documento Fiscal Referenciado na Devolução de Aquisição	1](#_Toc78989891)

[15\.	Registro 2133 – Nota Fiscal Complementar que Referenciou a Aquisição Informada no Registro 2130	1](#_Toc78989892)

[16\.	Registro 2134 – Complemento para NF\-E de Aquisição de Remetente Indireto	1](#_Toc78989893)

[17\.	Registro 2135 – Nota Fiscal Eletrônica de Ajuste que Referenciou a Aquisição Informada no Registro 2130	1](#_Toc78989894)

[18\.	Registro 2990: Encerramento do Bloco 2	1](#_Toc78989895)

# <a id="_Toc78989878"></a>Regras Gerais do Bloco 2

Os registros do Bloco 2 são gerados a partir das tabelas específicas do módulo \(movimentos e cálculos\), e em algumas situações, a partir das tabelas que contém informações de documentos de referência relacionados aos documentos fiscais\.

A seguir serão definidas as regras da geração de cada registro do Bloco 2\. 

# <a id="_Toc78989879"></a><a id="OLE_LINK30"></a>Registro 2001 – Abertura do Bloco 2

REG

Conteúdo fixo = “__2001__”

IND\_MOV

“0” à Bloco com dados informados \(quando existir dados para a geração do registro 2100 do estabelecimento\)

“1” à Bloco sem dados informados \(quando não existir dados para a geração do registro 2100 do estabelecimento\)

# <a id="_Toc78989880"></a>Registro 2100 – Demonstrativo da Apuração Mensal do Ressarcimento / Complemento

Registro único no arquivo, gerado a partir dos totais de ressarcimento/complemento apurados para o Estabelecimento\.

<a id="OLE_LINK24"></a>__Origem dos dados__: Tabela da Apuração do Ressarcimento / Complemento por Estabelecimento \(__EST\_ST\_SC\_APUR\_ESTAB__\)

Esta tabela é gerada numa etapa preliminar, no menu “*Geração > Cálculo do Ressarcimento/Complemento*”\. Ver regras desta geração no documento de regras ”*MTZ\-Ressar\-SC\-Calculo\_Ressarcimento”\.*

__Critérios de recuperação__:

    \- Empresa à código da Empresa;

    \- Estabelecimento à código do Estabelecimento em questão;

    \- Período à período informado em tela para geração do arquivo; 

01\-REG

Conteúdo fixo = “__2100__”

02\-S\_VL\_ICMS\_ST\_REST

Campo __Total Valor ICMS\-ST à Restituir __da tabela da apuração do Ressarc/Compl por Estabelecimento

03\-S\_VL\_ICMS\_ST\_COMPL

Campo __Total Valor ICMS\-ST à Complementar __da tabela da apuração do Ressarc/Compl por Estabelecimento

04\-SD\_ICMS\_ST\_REST

Campo __Saldo ICMS\-ST Restituição__ da tabela da apuração do Ressarc/Compl por Estabelecimento

05\-SD\_ICMS\_ST\_RESS

Campo __Saldo ICMS\-ST Ressarcimento__ da tabela da apuração do Ressarc/Compl por Estabelecimento

06\-SD\_ICMS\_ST\_COMPL

Campo __Saldo ICMS\-ST Complemento__ da tabela da apuração do Ressarc/Compl por Estabelecimento

07\-SD\_ICMS\_OP

Campo __Saldo ICMS Operações Próprias__ da tabela da apuração do Ressarc/Compl por Estabelecimento

08\-V\_APUR\_CRED\_ICMS

Campo __Valor Crédito Apurado __da tabela da apuração do Ressarc/Compl por Estabelecimento

09\- V\_APUR\_ICMS\_COMP

Campo __Valor Complemento Apurado __da tabela da apuração do Ressarc/Compl por Estabelecimento

# <a id="_Toc78989881"></a>Registro 2110 \- Demonstrativo da Apuração Mensal do Ressarcimento / Complemento por Produto

Registro <a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>“filho” do 2100\.

Este registro demonstra os valores de ressarcimento/complemento apurados para cada produto\.

__Origem dos dados__: Tabela da Apuração do Ressarcimento / Complemento por Produto \(__EST\_ST\_SC\_APUR\_PROD__\)

<a id="OLE_LINK18"></a><a id="OLE_LINK19"></a><a id="OLE_LINK20"></a>Esta tabela é gerada numa etapa preliminar, no menu “*Geração > Cálculo do Ressarcimento/Complemento*”\. Ver regras desta geração no documento de regras ”*MTZ\-Ressar\-SC\-Calculo\_Ressarcimento”\.*

__Critérios de recuperação__:

    \- Empresa à código da Empresa;

    \- Estabelecimento à código do Estabelecimento em questão;

    \- Período à período informado em tela para geração do arquivo; 

Para cada linha recuperada será gerado um registro 2110 com as informações abaixo: 

01\-REG

Conteúdo fixo = “__2110__”

02\-COD\_ITEM

Identificação do produto da tabela da apuração do Ressarc/Compl por Produto\.

A geração deste campo depende da parametrização dos dados inicias do estabelecimento em questão \(menu “*Parâmetrosà Dados Iniciais”\)*, da seguinte forma:

Se parâmetro “*Considerar o indicador no código do produto*” marcado,

     O campo será gerado com a concatenação do indicador \+ código do produto, no formato: X\-XXXXXXXXXXXXXX;

Senão

      O campo será gerado apenas com o código do produto;

	

<a id="OLE_LINK8"></a><a id="OLE_LINK9"></a>Todos os produtos gravados neste registro, serão registrados no Bloco 0, registro 0200, e registros “filhos” 0205 e 0206, quando for o caso\.  

03\-QTDE\_T\_V\_CF

Campo __Quantidade Total das Saídas para Consumidor Final __da tabela da apuração do Ressarc/Compl por Produto\.

04\-VL\_T\_V\_CF

Campo __Valor Total das Saídas para Consumidor Final __da tabela da apuração do Ressarc/Compl por Produto\.

05\-VLM\_UNIT\_V\_CF

Campo __Valor Médio Unitário das Saídas para Consumidor Final __da tabela da apuração do Ressarc/Compl por Produto\.

06\-VL\_T\_BCST\_V\_CF

Campo __Valor Total Base de Cálculo do ICMS\-ST Proporcional __da tabela da apuração do Ressarc/Compl por Produto\.

\[MFS32575\] – Tratamento de erro dado no validador

Quando o campo estive nulo, preencher com 0,00\.

07\-VL\_DIF\_MAIOR\_BCST

Campo __Valor da Diferença a Maior __da tabela da apuração do Ressarc/Compl por Produto\.

\[MFS32575\] – Tratamento de erro dado no validador

Quando o campo estive nulo, preencher com 0,00\.

08\-VL\_DIF\_MENOR\_BCST

Campo __Valor da Diferença a Menor __da tabela da apuração do Ressarc/Compl por Produto\.

09\-ALIQ\_EF

Campo __Alíquota ICMS Efetiva __da tabela da apuração do Ressarc/Compl por Produto\.

10\-VL\_ICMS\_ST\_REST

Campo __Valor ICMS\-ST à Restituir __da tabela da apuração do Ressarc/Compl por Produto\.

\[MFS32575\] – Tratamento de erro dado no validador

Quando o campo estive nulo, preencher com 0,00\.

11\-VL\_ICMS\_ST\_COMPL

Campo __Valor ICMS\-ST à Complementar __da tabela da apuração do Ressarc/Compl por Produto\.

12\-QTDE\_T\_IND\_S\_OE

Campo __Quantidade Total das Saídas para Outros Estados __da tabela da apuração dpeo Ressarc/Compl por Produto\.

13\-VL\_ICMS\_ IND\_S\_OE

Campo __Valor Total ICMS das Saídas para Outros Estados __da tabela da apuração do Ressarc/Compl por Produto\.

14\-VL\_ICMS\_ ST\_IND\_S\_OE

Campo __Valor Total ICMS\-ST das Saídas para Outros Estados __da tabela da apuração do Ressarc/Compl por Produto\.

__MFS64687__

15\-QTDE\_T\_IND\_S\_SN

15\- QTDE\_T\_IND\_S\_ICMSST\_DES

__MFS64687: __

Port\. SEF N° 159/2021, altera o campo 15 do registro 2110\.

De:

 Quantidade Total das Saídas para  Simples Nacional \(QTDE\_T\_IND\_S\_SN\)\.

Para:Quantidade Total das Saídas com  Desoneração ICMS\-ST \(QTDE\_T\_IND\_S\_ICMSST\_DES\)\.

__MFS64687: __Só alteração de nomenclatura\.

Nomenclatura do campo “__Quantidade Total das Saídas para Simples Nacional”__ na *Tabela da Apuração do* Ressarc/Compl por* Produto* alterada para __“Quantidade Total das Saídas c/ Desoneração ICMS\-ST”\.__

Campo __Quantidade Total das Saídas para Simples Nacional “Quantidade Total das Saídas c/ Desoneração ICMS\-ST” __da Tabela da Apuração do Ressarc/Compl por Produto\.

__MFS64687__

16\-VL\_T\_CREDITO\_MVA\_SN

16\-VL\_T\_CREDITO\_ICMSST\_DES

__MFS64687: __

Port\. SEF N° 159/2021, altera o campo 16 do registro 2110\.

 De:

 Valor Total Créditos Simples Nacional \(VL\_T\_CREDITO\_MVA\_SN\)\.

Para:Valor Total Créditos por Desoneração ICMS\-ST \(VL\_T\_CREDITO\_ICMSST\_DES\)\.

__MFS64687:__ Só alteração de nomenclatura\.

Nomenclatura do campo “__Valor Total Créditos Simples Nacional” __na *Tabela da Apuração do* Ressarc/Compl por* Produto* alterada para __“Valor Total Créditos Desoneração ICMS\-ST”\.__

Campo __Valor Total Créditos Simples Nacional “Valor Total Créditos Desoneração ICMS\-ST” __da tabela da apuração do Ressarc/Compl por Produto\.

# <a id="_Toc78989882"></a>Registro 2111 – Complemento de Identificação do Item

__A definir__

# <a id="_Toc78989883"></a>Registro 2112 – Totais dos Documentos Fiscais de Vendas a Consumidor Final \(ECF\)

<a id="OLE_LINK25"></a><a id="OLE_LINK26"></a><a id="OLE_LINK27"></a>Registro “filho” do 2110\.

Este registro demonstra os totais das vendas originadas de ECF para o produto apresentado no registro 2110\.

__Origem dos dados__: Tabela dos Totais de ECF \(__EST\_ST\_SC\_ECF__\)

<a id="OLE_LINK12"></a><a id="OLE_LINK13"></a>Esta tabela é gerada numa etapa preliminar, no menu “*Geração > Geração dos Movimentos > Saídas \- ECF*”\. Ver regras desta geração no documento de regras ”*MTZ\-Ressar\-SC\-Geracao\_Movimentos\_Saidas\_ECF”\.*

<a id="OLE_LINK32"></a><a id="OLE_LINK33"></a>__Critérios da recuperação dos dados__:

    \- Empresa à código da Empresa;

    \- Estabelecimento à código do Estabelecimento em questão;

    \- Período <a id="OLE_LINK4"></a>à período informado em tela para geração do arquivo; 

    \- Produtoà produto do registro “pai” 2110;

Para cada linha recuperada será gerado um registro 2112 com as informações abaixo: 

01\-REG

Conteúdo fixo = “__2112__”

02\-QTDE\_V\_CF	

<a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK7"></a>Campo __Quantidade do Cupom __da tabela dos totais de ECF\.

03\-UNID

Campo __Unidade de Medida __da tabela dos totais de ECF\.

Todos as unidades de medida gravadas neste registro, serão registradas no Bloco 0, registro 0190\.  

04\-FAT\_CONV

Campo __Fator de Conversão __da tabela dos totais de ECF\.

Sempre que o fator de conversão for diferente de 1, ele será gravado no Bloco 0, registro 0220\. Trata\-se de um registro “filho” do 0200, que informa as diferentes unidades de comercialização do produto, com os respectivos fatores de conversão\.

05\-QTDE\_V\_CF\_C

Campo __Quantidade Convertida __da tabela dos totais de ECF\.

06\-VL\_V\_CF

<a id="OLE_LINK40"></a><a id="OLE_LINK41"></a><a id="OLE_LINK42"></a>Campo __Valor da Venda __da tabela dos totais de ECF\.

07\-CNPJ

Este campo é preenchido com o CNPJ que consta no cadastro do estabelecimento emissor dos cupons, que é próprio estabelecimento da geração é o __estabelecimento de origem__\. 

__MFS46103__: campo incluído pela Portaria SEF 262/2020, de 02/10/2020

Obs\.: Este novo campo terá o objetivo de informar o estabelecimento emissor dos cupons fiscais, quando a geração do arquivo for realizada de forma consolidada, que é o novo Perfil D\. No entanto, a geração do Ressarc ICMS\-ST de SC ainda *não* trata este Perfil D, que será desenvolvido em demandas futuras\. Por isso, neste momento o campo será sempre preenchido com o CNPJ do estabelecimento da geração\.

__MFS46838: Tratamento do Perfil D:__

MFS que passa a gerar o Perfil D\. Com isso, esse campo passa a ser preenchido com o CNPJ do estabelecimento de __origem__\.

# <a id="_Toc78989884"></a>Registro 2113 – Documentos Fiscais de Vendas

<a id="OLE_LINK47"></a><a id="OLE_LINK48"></a>Registro “filho” do 2110\.

Este registro demonstra os totais das vendas, e suas devoluções, originados de notas fiscais, para o produto apresentado no registro 2110\.

__Origem dos dados__: Tabela dos Movimentos \(__EST\_ST\_SC\_NF__\)

<a id="OLE_LINK75"></a>Esta tabela é gerada numa etapa preliminar, no menu “*Geração > Geração dos Movimentos > Saídas*”\. Ver regras desta geração no documento de regras “*MTZ\-Ressar\-SC\-Geracao\_Movimentos\_Saidas”\.*

<a id="OLE_LINK74"></a>__Critérios da recuperação dos dados__:

    \- Empresa à código da Empresa;

    \- Estabelecimento à código do Estabelecimento em questão;

    \- Período à período informado em tela para geração do arquivo;

    \- Indicador do Tipo de Registro à = “__2113__” \(apenas os movimentos de saída ou devolução de saída a serem gravados no registro 2113\);

    \- Produtoà produto do registro “pai” 2110;

<a id="OLE_LINK54"></a><a id="OLE_LINK55"></a>Para cada linha recuperada será gerado um registro 2113 com as informações abaixo: 

<a id="OLE_LINK78"></a><a id="OLE_LINK79"></a>

01\-REG

Conteúdo fixo = “__2113__”

<a id="OLE_LINK34"></a><a id="OLE_LINK35"></a><a id="OLE_LINK36"></a><a id="OLE_LINK37"></a><a id="OLE_LINK38"></a><a id="OLE_LINK39"></a><a id="_Hlk9260470"></a>02\-IND\_OPER

Campo __Nota de Devolução __da tabela dos movimentos \(0=Saída, 1=Devolução\)\.

03\-IND\_S

Campo __Indicador do Tipo de Saída __da tabela dos movimentos \(será = 10, 20 ou 30\)\.

04\-CHV\_NFE

Campo __Chave Documento Fiscal Eletrônico __da tabela dos movimentos\.

05\-DT\_NFE

Campo __Data Emissão __da tabela dos movimentos\.

06\-DT\_E

Campo __Data Entrada __da tabela dos movimentos\.

Alteração __MFS40583__:

Este campo será preenchido no arquivo *apenas* quando se tratar de notas de devolução de vendas \(ou seja, quando for uma nota de entrada = campo 02\-IND\_OPER = “1”\)\.   

07\-CNPJ

Este campo é gerado com a informação do CNPJ da pessoa fis/jur emitente do documento \(campo __Pessoa Fis/Jur__ da tabela dos movimentos\)\. Para tal será verificado se a informação que consta no campo 06\-CPF\_CGC da SAFX04 é um CNPJ ou um CPF:

Se o conteúdo for um CNPJ à a informação será gerada neste campo, e o campo 08\-CPF será gerado sem informação \(“||”\);

Se o conteúdo for um CPF à a informação será gerada no campo 08\-CPF, e este campo será gerado sem informação \(“||”\);    

 

08\-CPF

Este campo é gerado com a informação do CPF da pessoa física do documento \(campo __Pessoa Fis/Jur__ da tabela dos movimentos\), seguindo a mesma regra descrita para o campo 07\-CNPJ\.

<a id="_Hlk9261200"></a>09\-NUM\_ITEM	

<a id="OLE_LINK43"></a><a id="OLE_LINK44"></a><a id="OLE_LINK45"></a><a id="OLE_LINK46"></a>Campo __Número do Item __da tabela dos movimentos\.

10\-QTDE\_IND\_S	

Campo __Quantidade da Nota __da tabela dos movimentos\.

11\-UNID

Unidade de medida do item da nota \(Campo 25\-Unidade de Medida do item\)

\(Na tabela dos movimentos, é a coluna COD\_MEDIDA\_ITEM\)

Todos as unidades de medida gravadas neste registro, serão registradas no Bloco 0, registro 0190\.  

12\-FAT\_CONV

Campo __Fator de Conversão __da tabela dos movimentos\.

Sempre que o fator de conversão for diferente de 1, ele será gravado no Bloco 0, registro 0220\. Trata\-se de um registro “filho” do 0200, que informa as diferentes unidades de comercialização do produto, com os respectivos fatores de conversão\.

13\-QTDE\_IND\_S\_C

Campo __Quantidade Convertida __da tabela dos movimentos\.

14\-VL\_V\_IND\_S

Campo __Valor da Venda __da tabela dos movimentos\.

15\-CFOP

Campo __CFOP __da tabela dos movimentos\.

__MFS64687__

16\-VL\_CREDITO\_MVA\_SN

16\-VL\_CREDITO\_ICMSST\_DES

__MFS64687: __

Port\. SEF N° 159/2021, altera o campo 16 do registro 2113\.

De:

 Valor do Crédito Simples Nacional \(VL\_CREDITO\_MVA\_SN\), que considerava o tipo de saída = 30\.

Para:Valor do Crédito por Desoneração ICMS\-ST \(VL\_CREDITO\_ICMSST\_DES\), que passa a considerar os tipos de saídas 30, 40 e 50\.

__MFS64687:__ alteração de regra de preenchimento e nomenclatura\.

Nomenclatura do campo “__Valor Crédito Simples Nacional” __na *Tabela dos Movimentos* alterada para __“Valor Crédito Desoneração ICMS\-ST”\.__

MFS30131:

O preenchimento deste campo depende do campo __Indicador do Tipo de Saída__ da tabela dos movimentos \(corresponde ao campo 03\-IND\_S do registro 2113\), da seguinte forma:

__MFS64687__

Se __Indicador do Tipo de Saída__ = “30” ou “40” ou “50”

     O campo será preenchido com o conteúdo do campo __Valor Crédito Simples Nacional__ __Valor Crédito Desoneração__

__     ICMS\-ST __da tabela dos movimentos; 

Senão

    __\[MFS37144\]__ – Tratamento de erro dado no validador

     O campo será gerado com zero\.

17\-CNPJ

Este campo é preenchido com o CNPJ que consta no cadastro do estabelecimento emissor dos documentos, que é próprio estabelecimento da geração é o __estabelecimento de origem__\. 

__MFS46143__: campo incluído pela Portaria SEF 262/2020, de 02/10/2020

Obs\.: Este novo campo terá o objetivo de informar o estabelecimento emissor dos documentos, quando a geração do arquivo for realizada de forma consolidada, que é o novo Perfil D\. No entanto, a geração do Ressarc ICMS\-ST de SC ainda *não* trata este Perfil D, que será desenvolvido em demandas futuras\. Por isso, neste momento o campo será sempre preenchido com o CNPJ do estabelecimento da geração\.

__MFS46838: Tratamento do Perfil D:__

MFS que passa a gerar o Perfil D\. Com isso, esse campo passa a ser preenchido com o CNPJ do estabelecimento de __origem__

# <a id="_Toc78989885"></a>Registro 2114 – Complemento de Documento Fiscal Referenciado na Devolução de Vendas

Registro “filho” do 2113\.

Este registro é gerado apenas quando o documento do registro “pai” 2113 for uma nota de devolução, ou seja, quando o campo __Nota de Devolução __da tabela dos movimentos = __1__ \(Devolução\)\.

O objetivo é demonstrar os documentos fiscais referenciados nas informações complementares da nota de devolução, que têm a finalidade de indicar os documentos da operação original da venda\. Estes documentos referenciados podem ser tanto notas fiscais \(SAFX07/08\), como cupons fiscais \(SAFX993/994\)\.

__MFS46838: Tratamento do Perfil D:__

Considerar que a nota fiscal do registro 2113 pode ser do estabelecimento Centralizador \(informado na tela de geração\) ou dos seus estabelecimentos Centralizados\. Com isso a busca dos documentos referenciados e cupons referenciados deve considerar o estabelecimento de origem do registro 2113 da tabela de Movimento\.

__Origem dos dados__: Tabela dos Documentos Fiscais Referenciados \(__SAFX116__\)

                                  Tabela dos Cupons Fiscais Referenciados \(__SAFX117__\)

*\(Serão utilizadas as mesmas tabelas das informações complementares utilizadas no Sped Fiscal, para geração dos registros C113 e C114\) *

Estas tabelas são vinculadas à capa da nota \(SAFX07\), e assim, não têm a informação do produto\. Elas têm apenas as informações de identificação do documento referenciado \(nota ou cupom\)\.

Para a geração do registro 2114, serão considerados somente os documentos referenciados recuperados da SAFX116/SAFX117, que tenham pelo menos um item do produto em questão \(produto do registro “avô” 2110\)\.

Desta forma, o procedimento é o seguinte:

  

- Pesquisa todos os registros da SAFX116/SAFX117 vinculados a nota fiscal de devolução do registro “pai” 2113;
- Dentre os documentos referenciados recuperados nestas tabelas, serão considerados apenas aqueles que tenham entre os seus itens o produto em questão \(produto do registro “avô” 2110\)\. A pesquisa dos itens é feita dependendo do tipo de documento referenciado, da seguinte forma:

\- Documentos referenciados originados da SAFX116 à como se trata de notas fiscais, os itens são pesquisados na SAFX08;

             \- Cupons referenciados originados da SAFX117 à como se trata de cupons fiscais, a pesquisa dos itens é feita na SAFX994;

__Exemplo__:

__Dados da X07 / X08 / X116__

__Dados dos registros no arquivo__

__Notas de Venda__:

__NF: 85__

Item 1 – Produto A4

__NF: 120                               __

Item 1 – Produto A1            

Item 2 – Produto A5            

                                            

__NF: 350__

Item 1 – Produto A3

Item 2 – Produto A4

Item 3 – Produto A9

__Nota de Devolução__:

__NF: 522__

Item 1 – Produto A1

Item 2 – Produto A4

Documentos referenciados \(X116\): NF 120 e NF 350

__2110 Produto A1__

     __2113__ NF 120

     __2113__ NF 522

           __2114__ NF 120 

           *\(Observar que existem 2 documentos referenciados na SAFX116 para a nota de *

*            devolução *__*522*__*\. Mas apenas o documento *__*120*__* seria gerado aqui, pois só ele tem*

*            itens do *__*Produto A1*__*\)* 

__2110 __Produto A3

     __2113__ NF 350

__2110 Produto A4__

     __2113__ NF 85

     __2113__ NF 350

     __2113__ NF 522

           __2114__ NF 350 

           *\(Observar que existem 2 documentos referenciados na SAFX116 para a nota de*

*           devolução *__*522*__*\. Mas apenas o documento *__*350*__* seria gerado aqui, pois só ele tem *

*           itens do *__*Produto A4*__*\)* 

__2110 __Produto A5

     __2113__ NF 120

__2110 __Produto A9

     __2113__ NF 350

__Critérios da recuperação dos documentos referenciados da SAFX116 e SAFX117:__

     \- Campos 01 ao 11 = Campos de identificação da nota da Tabela de Movimentos \(nota de devolução gerada no registro “pai” 2113\); 

__     MFS46838: Tratamento do Perfil D:__

    \- Estabelecimento \(campo 02\) à Estabelecimento origem da nota do registro “pai” 2113;

Poderão ser recuperados ‘n’ registros de documentos referenciados \(notas e cupons\)\.

Na __SAFX116__ as informações do documento referenciado constam nos campos 13 ao 21;

Na __SAFX117__ as informações do cupom referenciado constam nos campos 13 ao 18;

Para cada documento de referência recuperado \(nota ou cupom\), será feita a pesquisa para verificar se a nota/cupom tem itens do produto em questão ou não \(pesquisa dos itens descrita acima\)\.

No caso da __SAFX116__, a pesquisa dos itens na __SAFX08__ é feita a partir dos campos que identificam a nota de referência \(campo 13 ao campo 19\), e da identificação do produto em questão, da seguinte forma:

__Campos da SAFX08__

__Campos da SAFX116__

01\-Código da Empresa

01\-Código da Empresa

02\-Código do Estabelecimento

02\-Código do Estabelecimento

03\-Data Fiscal

19\-Data de Emissão

*Obs\.: Como o doc de referência nesse caso será sempre uma venda \(uma saída\), então a data de emissão é a própria data fiscal\) *

04\-Movimento E/S 

16\-Movimento E/S

07\-Indicador da Pessoa Fis/Jur

17\-Indicador da Pessoa Fis/Jur

08\-Código da Pessoa Fis/Jur

18\-Código da Pessoa Fis/Jur

09\-Número do Documento Fiscal

13\-Número do Documento Fiscal

10\-Série do Documento Fiscal

14\-Série do Documento Fiscal

11\-Subsérie do Documento Fiscal

15\-Subsérie do Documento Fiscal

13\-Indicador do Produto

__Indicador do Produto em questão \(produto do registro “avô” 2110\)__

14\-Produto

__Código do Produto em questão \(produto do registro “avô” 2110\)__

         Obs\.: O Tipo de Documento não é usado na busca, pois a SAFX116 não tem campo do tipo de documento do documento de referência;

No caso da __SAFX117__, a pesquisa dos itens na __SAFX994__ é feita a partir dos campos que identificam o cupom de referência \(campo 13 ao campo 16\), e da identificação do produto em questão, da seguinte forma:

__Campos da SAFX994__

__Campos da SAFX117__

01\-Código da Empresa

01\-Código da Empresa

02\-Código do Estabelecimento

02\-Código do Estabelecimento

03\-Modelo Documento 

04\-Número do Caixa

\(ID da X2087\_EQUIPAMENTO\_ECF\)

16\-Modelo de Documento

13\-Número do Caixa \(ECF\)

05\-COO \(Contador de Ordem de Operação\) 

14\-Número do Documento

06\-Data da Emissão

15\-Data de Emissão

08\-Indicador do Produto

__Indicador do Produto em questão \(produto do registro “avô” 2110\)__

09\-Código do Produto

__Código do Produto em questão \(produto do registro “avô” 2110\)__

O objetivo desta pesquisa é apenas verificar se o documento referenciado tem ou não itens do produto em questão, sem importar quais são estes itens, já que as informações do item não serão utilizadas\.

__Gravação dos dados no registro 2114:__

Serão gravados no registro 2114 *apenas* aqueles documentos referenciados \(notas e cupons\) para os quais exista item do produto em questão \(conforme o exemplo descrito acima\)\. Assim, os documentos referenciados que *não* tiverem item do produto em questão, *serão desconsiderados*\.

Para cada documento referenciado \(nota ou cupom\) a ser considerado, será gravado um registro 2114\. 

Os campos a serem utilizados depende da origem do documento de referência \(SAFX116 ou SAFX117\), conforme descrito a seguir:

01\-REG

Conteúdo fixo = “__2114__”

02\-CNPJ

Este campo é gerado com a informação do CNPJ da pessoa fis/jur do documento de referência\.

__Documento referenciado originado da SAFX116:__

    A partir dos campos __17\-Indicador Pessoa Fis/Jur__ e __18\-Código Pessoa Fis/Jur__ da SAFX116, será verificado o conteúdo da

    informação que consta no campo 06\-CPF\_CGC da SAFX04:

     Se for um CNPJ à a informação será gerada neste campo, e o campo 03\-CPF será gerado sem informação \(“||”\);

     Se for um CPF à a informação será gerada no campo 03\-CPF, e este campo será gerado sem informação \(“||”\);    

__Documento referenciado originado da SAFX117:__

    No caso dos cupons referenciados, a SAFX117 não tem esta informação\. Assim, será recuperada a informação do campo 

    “08\-CNPJ/CPF do Adquirente” da capa do cupom \(SAFX993\)\. Da mesma forma descrita acima, será verificado se o conteúdo da

    informação é um CNPJ ou um CPF:

     Se for um CNPJ à a informação será gerada neste campo, e o campo 03\-CPF será gerado sem informação \(“||”\);

     Se for um CPF à a informação será gerada no campo 03\-CPF, e este campo será gerado sem informação \(“||”\);  

     Para acessar a capa do cupom na SAFX993 a partir da SAFX117:

    SAFX993                                                             SAFX117

    01\-Código da Empresa                                    = 01\-Código da Empresa

    02\-Código do Estabelecimento                        = 02\-Código do Estabelecimento

    03\-Modelo Documento / 04\-Número do Caixa = 16\-Modelo Documento / 13\-Número do Caixa \(ECF\)

    05\-COO                                                            = 14\-Número do Documento

    06\-Data de Emissão                                         = 15\-Data de Emissão

03\-CPF

Este campo é gerado com a informação do CPF da pessoa física do documento de referência, seguindo a mesma regra descrita para o campo 02\-CNPJ\.

04\-CHV\_NFE\_REF

__Documento referenciado originado da SAFX116:__

   Campo __21\-Chave de Acesso da NF\-Eletrônica__ da SAFX116;

__Cupom referenciado originado da SAFX117:__

   Campo __18\-Chave do CF\-e__ da SAFX117;

05\-ECF\_CX\_REF

__Documento referenciado originado da SAFX116:__

   Este campo será gerado sem informação \(“||”\);

__Cupom referenciado originado da SAFX117:__

   Campo __13\-Número do Caixa \(ECF\)__ da SAFX117;

Obs\.: Na SAFX117 o campo tem 9 posições porque trata tanto os cupons da SAFX993/994, como os cupons SAT CF\-e da SAFX201/202\. Mas para esta obrigação tratamos apenas os cupons da SAFX993/994, onde o tamanho é de 3 posições\. Por isso, o campo 13\-Número do Caixa \(ECF\) nunca ultrapassará o tamanho do layout\.

06\-NUM\_DOC\_REF

__Documento referenciado originado da SAFX116:__

   Campo __13\-Número do Documento Fiscal __da SAFX116;

__Cupom referenciado originado da SAFX117:__

   Campo __14\-Número do Documento__ da SAFX117;

07\-DT\_DOC\_REF

__Documento referenciado originado da SAFX116:__

   Campo __19\-Data de Emissão__ da SAFX116;

__Cupom referenciado originado da SAFX117:__

   Campo __15\-Data de Emissão__ da SAFX117;

# <a id="_Toc78989886"></a>Registro 2115 – Nota Fiscal Complementar que Referenciou a Nota de Saída Informada no Registro 2113

Registro “filho” do 2113\.

Este registro demonstra as notas fiscais complementares associadas à nota de saída informada no registro 2113\.

__MFS46838: Tratamento do Perfil D:__

Considerar que a nota fiscal do registro 2113 pode ser do estabelecimento Centralizador \(informado na tela de geração\) ou dos seus estabelecimentos Centralizados\. Com isso a busca das Notas Complementares deve considerar o estabelecimento de origem do registro 2113 da tabela de Movimento\.

__Origem dos dados__: Tabela das Notas Complementares \(__EST\_ST\_SC\_NF\_COMPL__\)

Esta tabela é gerada numa etapa preliminar, no menu “*Geração > Geração dos Movimentos > Saídas*”\.  As notas complementares são identificadas durante o processo, e seus valores e quantidades são totalizados na nota original \(2113\)\.   

Ver regras desta geração no documento de regras “*MTZ\-Ressar\-SC\-Geracao\_Movimentos\_Saidas”\.*

__Critérios da recuperação dos dados__:

    \- Empresa à código da Empresa;

    \- Estabelecimento à código do Estabelecimento em questão;

__     MFS46838: Tratamento do Perfil D:__

    \- Estabelecimento à Estabelecimento origem da nota do registro “pai” 2113;

    \- Período à período informado em tela para geração do arquivo;

    \- Indicador do Tipo de Registro à = “__2115__”;

    \- Produtoà produto do registro “pai” 2110;

    \- Data Fiscal                    à dados da identificação da nota do registro “pai” 2113;

    \- Tipo do Documento       à dados da identificação da nota do registro “pai” 2113;

    \- Série do Documento      à dados da identificação da nota do registro “pai” 2113;

    \- Número do Documento  à dados da identificação da nota do registro “pai” 2113;

    \- Pessoa Fis/Jur                à dados da identificação da nota do registro “pai” 2113;

    \- Número do Item              à dados da identificação da nota do registro “pai” 2113;

    \- Movimento E/S                à dados da identificação da nota do registro “pai” 2113;111

Para cada linha recuperada será gerado um registro 2115 com as informações abaixo: 

01\-REG

Conteúdo fixo = “__2115__”

02\-CHV\_NFE\_COMP

Campo __Chave Documento Fiscal Eletrônico da Nota Complementar __da tabela das notas complementares\.

03\-NUM\_ITEM\_NFE\_COMP

Campo __Número do Item da Nota Complementar __da tabela das notas complementares\.

# <a id="_Toc78989887"></a>Registro 2120: Valor Médio Mensal Unitário das Entradas da Base de Cálculo da Substituição Tributária para Apuração de Entrada de Mercadoria identificada no Registro 2110, incluindo NF\-e de Remetente Indireto com tag específica informada no XML

<a id="OLE_LINK72"></a><a id="OLE_LINK73"></a>Registro “filho” do 2110\.

Este registro demonstra o valor médio unitário do produto, calculado a partir das notas de entrada\.

<a id="OLE_LINK56"></a><a id="OLE_LINK57"></a><a id="OLE_LINK58"></a>Para cada produto \(cada registro 2110\), poderá existir apenas um registro 2120\.

__\[MFS34795\] Alteração válida somente a partir de novembro de 2019__

__Obs\.:__ Este registro não será informado quando no Registro 2130 estejam relacionados __somente__ os documentos fiscais de aquisição classificada como de Remetente Indireto \(COD\_RESP\_RET = 2\), em que no XML da NF\-e __não__ tenha preenchida a *tag *especifica das informações relativas ao ICMS cobrado anteriormente por substituição tributária \(COD\_IND\_XML = 1, Registro 2134\)\.  Este tratamento está sendo feito no cálculo do valor médio das entradas, que não irá calcular os valores do registro 2120 quando se tratar desta situação\.

__Origem dos dados__: Tabela do Valor Médio das Entradas \(__EST\_ST\_SC\_VLR\_UNIT__\)

Esta tabela é gerada numa etapa preliminar, no menu “*Geração > Cálculo do Valor Médio das Entradas*”\. Ver regras desta geração no documento de regras “*MTZ\-Ressar\-SC\-Calculo\_Valor\_Medio\_Entradas”\.*

__Critérios da recuperação dos dados__:

    \- Empresa à código da Empresa;

    \- Estabelecimento à código do Estabelecimento em questão;

    \- Período à período informado em tela para geração do arquivo; 

    \- Produtoà produto do registro “pai” 2110;

     __\[MFS34795\]__ Alteração da geração do registro 2120: somente se os valores do registro 2120 estiverem preenchidos, conforme o cálculo do valor médio das entradas 

    \- Quantidade Total \(registro 2120\) maior que zero  

Para cada produto \(cada registro 2110\), existirá apenas um registro na tabela EST\_ST\_SC\_VLR\_UNIT, e portanto, existirá apenas um único registro 2120\.

O registro 2120 será gerado com as seguintes informações: 

01\-REG

Conteúdo fixo = “__2120__”

02\-S\_QTDE\_C

<a id="OLE_LINK59"></a><a id="OLE_LINK60"></a><a id="OLE_LINK61"></a>Campo __Quantidade Total __da tabela do valor médio das entradas\.

03\-S\_VL\_BCST\_INT

Campo __Total da BC Integral do ICMS\-ST __da tabela do valor médio das entradas\.

04\-VLM\_UNIT\_BCST

Campo __Valor Médio Unitário da BC do ICMS\-ST __da tabela do valor médio das entradas\.

05\-S\_VL\_ICMS

Campo __Total do Valor do ICMS __da tabela do valor médio das entradas\.

06\-VLM\_UNIT\_ICMS

Campo __Valor Médio Unitário do ICMS __da tabela do valor médio das entradas\.

07\-S\_VL\_ICMS\_ST

Campo __Total do Valor do ICMS\-ST __da tabela do valor médio das entradas\.

08\-VLM\_UNIT\_ICMS\_ST

Campo <a id="OLE_LINK70"></a>__Valor Médio Unitário do ICMS\-ST__ da tabela do valor médio das entradas\.

# <a id="_Toc78989888"></a>Registro 2121: Valor Médio Mensal Unitário da Base de Cálculo da Substituição Tributária para Apuração de Entrada de Mercadoria identificada no Registro 2110 \- todas NF\-e informadas no Registro 2130

__\[MFS34795\]__

Registro “filho” do 2110, somente deve ser gerado a partir de novembro de 2019\.

Este registro demonstra o valor médio unitário do produto, calculado a partir das notas de entrada\.

Para cada produto \(cada registro 2110\), poderá existir apenas um registro 2121\.

__Obs\.: __Este registro não será informado quando no Registro 2130 estejam relacionados __exclusivamente __documentos fiscais de aquisição, classificada como de Remetente Indireto \(COD\_RESP\_RET = 2\), em que no XML da NF\-e foi preenchida a *tag *especifica com informações relativas ao ICMS cobrado anteriormente por substituição tributária\.  Este tratamento está sendo feito no cálculo do valor médio das entradas, que não irá calcular os valores do registro 2121 quando se tratar desta situação\.

__Origem dos dados__: Tabela do Valor Médio das Entradas \(__EST\_ST\_SC\_VLR\_UNIT__\)

Esta tabela é gerada numa etapa preliminar, no menu “*Geração > Cálculo do Valor Médio das Entradas*”\. Ver regras desta geração no documento de regras “*MTZ\-Ressar\-SC\-Calculo\_Valor\_Medio\_Entradas”\.*

__Critérios da recuperação dos dados__:

    \- Empresa à código da Empresa;

    \- Estabelecimento à código do Estabelecimento em questão;

    \- Período à período informado em tela para geração do arquivo; 

    \- Produtoà produto do registro “pai” 2110;

    \- Quantidade Total \(registro 2121\) maior que zero  

Para cada produto \(cada registro 2110\), existirá apenas um registro na tabela EST\_ST\_SC\_VLR\_UNIT, e portanto, existirá apenas um único registro 2121\.

O registro 2121 será gerado com as seguintes informações: 

01\-REG

Conteúdo fixo = “__2121__”

02\-S\_QTDE\_C\_T

Campo __Quantidade Total __do registro 2121 da tabela do valor médio das entradas\.

03\-S\_QTDE\_C\_VLM

Campo __Quantidade Total da Mercadoria__ do registro 2121 da tabela do valor médio das entradas\.

04\-S\_VL\_BCST\_INT\_ VLM

Campo __Total da BC Integral do ICMS\-ST VLM__ do registro 2121 da tabela do valor médio das entradas\.

05\- VLM\_UNIT\_BCST\_G

Campo __Valor Médio Unitário do ICMS\-ST__ do registro 2121 da tabela do valor médio das entradas\.

# <a id="_Toc78989889"></a>Registro 2130: Documentos Fiscais de Entradas 

Registro “filho” do 2120 \(Valor Médio Unitário das Entradas\)\.

Neste registro serão demonstradas todas as notas fiscais de entrada utilizadas no cálculo do valor médio unitário do produto\.

__Origem dos dados__: Tabela dos Movimentos \(__EST\_ST\_SC\_NF__\)

Esta tabela é gerada numa etapa preliminar, no menu “*Geração > Geração dos Movimentos > Entradas*”\. Ver regras desta geração no documento de regras “*MTZ\-Ressar\-SC\-Geracao\_Movimentos\_Entradas”\.*

__Critérios da recuperação dos dados__:

    \- Empresa à código da Empresa;

    \- Estabelecimento à código do Estabelecimento em questão;

    \- Período à período informado em tela para geração do arquivo;

    \- Indicador do Tipo de Registro à = “__2130__” \(apenas os movimentos de entrada ou devolução de entrada a serem gravados no registro 2130\);

    \- Produtoà produto do registro “avô” 2110;

Para cada linha recuperada será gerado um registro 2130 com as informações abaixo: 

01\-REG

Conteúdo fixo = “__2130__”

02\-IND\_OPER

Campo __Nota de Devolução __da tabela dos movimentos \(0=Entrada, 1=Devolução\)\.

03\-CHV\_NFE

Campo __Chave Documento Fiscal Eletrônico __da tabela dos movimentos\.

04\-DT\_E

Campo __Data Entrada __da tabela dos movimentos\. Quando nulo, o campo será gerado sem informação \(“||”\)\.

Alteração MFS30185: Este campo passou a ser gerado de acordo com as orientações do layout de SC \(Essas regras eram tratadas na pré\-geração do registro 2130, mas foram transferidas para a geração do arquivo\)

A geração deste campo segue a regra abaixo:

Se nota de entrada \(MOVTO\_E\_S <> 9\), então:

      Preencher com a informação do campo __Data Entrada __da tabela dos movimentos;

Senão \(são as notas de saída das devoluções de entrada\)

     O campo será gerado sem informação \(“||”\);

05\-DT\_NFE

Campo __Data Emissão __da tabela dos movimentos\. Quando nulo, o campo será gerado sem informação \(“||”\)\.

Alteração MFS30185: Este campo passou a ser gerado de acordo com as orientações do layout de SC \(Essas regras eram tratadas na pré\-geração do registro 2130, mas foram transferidas para a geração do arquivo\)

A geração deste campo segue a regra abaixo:

Se nota de entrada \(MOVTO\_E\_S <> 9\), então:

      O campo será gerado sem informação \(“||”\);

Senão \(são as notas de saída das devoluções de entrada\)

      Preencher com a informação do campo __Data Emissão __da tabela dos movimentos\.

06\-CNPJ

Este campo é gerado com a informação do CNPJ da pessoa fis/jur emitente do documento \(campo __Pessoa Fis/Jur__ da tabela dos movimentos\)\. Para tal será verificado se a informação que consta no campo 06\-CPF\_CGC da SAFX04 é um CNPJ ou um CPF:

Se o conteúdo for um CNPJ à a informação será gerada neste campo;

Se o conteúdo for um CPF à este campo será gerado sem informação \(“||”\);:::

*\(Pendente: nesse caso deve\-se gravar mensagem de erro, já que o campo é obrigatório?*

*\(Observar que o registro 2113 tem os dois campos, CNPJ e CPF\) *

07\-NUM\_ITEM

Campo __Número do Item __da tabela dos movimentos\.

08\-COD\_RESP\_RET

Campo __Código Responsável Retenção __da tabela dos movimentos\.

Quando nulo, o campo será gerado sem informação \(“||”\)\.

09\-QTDE

Campo __Quantidade da Nota __da tabela dos movimentos\.

10\-UNID

Unidade de medida do item da nota \(Campo 25\-Unidade de Medida do item\)

\(Na tabela dos movimentos, é a coluna COD\_MEDIDA\_ITEM\)

Todos as unidades de medida gravadas neste registro, serão registradas no Bloco 0, registro 0190\.  

11\-FAT\_CONV

Campo __Fator de Conversão __da tabela dos movimentos\.

Sempre que o fator de conversão for diferente de 1, ele será gravado no Bloco 0, registro 0220\. Trata\-se de um registro “filho” do 0200, que informa as diferentes unidades de comercialização do produto, com os respectivos fatores de conversão\.

12\-QTDE\_C

Campo __Quantidade Convertida __da tabela dos movimentos\.

13\-VL\_E

Campo __Valor da Entrada __da tabela dos movimentos\.

14\-CFOP

Campo __CFOP __da tabela dos movimentos\.

15\-VL\_BC\_ICMS

Campo __Base de Cálculo do ICMS __da tabela dos movimentos\.

\[MFS32267\] – Tratamento de erro dado no validador

Quando o campo estive nulo, preencher com 0,00\.

16\-ALIQ\_ICMS

<a id="OLE_LINK110"></a>Campo __Alíquota ICMS __da tabela dos movimentos\.

\[MFS36656\] – Tratamento de erro dado no validador

Quando o campo estive nulo, preencher com 0,00\.

17\-VL\_ICMS

<a id="OLE_LINK111"></a><a id="OLE_LINK112"></a>Campo __Valor ICMS __da tabela dos movimentos\.

18\-VL\_BC\_ST

<a id="OLE_LINK108"></a><a id="OLE_LINK109"></a>Campo __Base de Cálculo ICMS\-ST Pago __da tabela dos movimentos\.

19\-VL\_BC\_ST\_INT

Campo __Base de Cálculo ICMS\-ST Integral __da tabela dos movimentos\.

20\-ALIQ\_ST\_E

Campo __Alíquota ICMS\-ST Pago __da tabela dos movimentos\.

21\-ALIQ\_ST\_EF

Campo __Alíquota ICMS\-ST Efetiva __da tabela dos movimentos\.

22\-CAL\_ICMS\_ST

<a id="OLE_LINK113"></a><a id="OLE_LINK114"></a><a id="OLE_LINK115"></a>Campo __Valor ICMS\-ST Calculado __da tabela dos movimentos\.

23\-VL\_ICMS\_ST

Campo __Valor ICMS\-ST __da tabela dos movimentos\.

24\-COD\_DA

<a id="OLE_LINK116"></a><a id="OLE_LINK117"></a><a id="OLE_LINK118"></a>Campo __Modelo do Documento de Arrecadação __da tabela dos movimentos\.

<a id="OLE_LINK119"></a><a id="OLE_LINK120"></a><a id="OLE_LINK121"></a>Quando nulo, o campo será gerado sem informação \(“||”\)\.

25\-NUM\_DARE

Campo __Número do Documento de Arrecadação __da tabela dos movimentos\.

Quando nulo, o campo será gerado sem informação \(“||”\)\.

26\-COD\_AJ

Campo __Código de Ajuste do Sped Fiscal \(C197\) __da tabela dos movimentos\.

Quando nulo, o campo será gerado sem informação \(“||”\)\.

27\-CNPJ

Este campo é preenchido com o CNPJ que consta no cadastro do estabelecimento emissor dos documentos, que é próprio estabelecimento da geração é o __estabelecimento de origem__\. 

__MFS46143__: campo incluído pela Portaria SEF 262/2020, de 02/10/2020

Obs\.: Este novo campo terá o objetivo de informar o estabelecimento emissor dos documentos, quando a geração do arquivo for realizada de forma consolidada, que é o novo Perfil D\. No entanto, a geração do Ressarc ICMS\-ST de SC ainda *não* trata este Perfil D, que será desenvolvido em demandas futuras\. Por isso, neste momento o campo será sempre preenchido com o CNPJ do estabelecimento da geração\.

__MFS46838: Tratamento do Perfil D:__

MFS que passa a gerar o Perfil D\. Com isso, esse campo passa a ser preenchido com o CNPJ do estabelecimento de __origem__\.

# <a id="_Toc78989890"></a>Registro 2131: Documento Fiscal Referenciado, emitido pelo Substituto Tributário, referente a Entrada de Mercadoria Adquirida de Remetente Indireto 

__\(MFS33079\) __\- Inclusão do registro 2131;

__\(MFS46100\) __\- O registro 2131 foi revogado pela Portaria SEF 262/2020, de 02/10/2020, e portanto, não será mais gerado\.

Registro “filho” do 2130\.

Este registro demonstra as notas fiscais emitidas por Substitutos Tributários, associadas à nota de entrada adquirida de Remetente Indireto \(COD\_RESP\_RET = 2\) informada no registro 2130\.

 

Conforme a __Portaria SEF 208/2019__ \(Art\. 6º\), este registro __não__ será informado sempre que:

1 \- Apurado complementação do imposto retido, na saída destinada a consumidor final para cada item de mercadoria informado no registro 2110, ou

2 \- Apurado ressarcimento em decorrência de saída em operação interna destinada a empresa optante pelo Simples Nacional para cada item de mercadoria informado no registro 2110;

3 \- o item de mercadoria informado no registro 2110 tenha sua base de cálculo definida por PMPF, conforme divulgado em Ato COTEPE/PMPF, enquadrado nos seguintes NCM/SH:

<a id="_Hlk28357528"></a>  2207\.10\.90 \- Etanol Hidratado Combustível;

  2710\.12\.59 \- Gasolina Automotiva;

  2710\.19\.21 \- Óleo Diesel;

  2711\.19\.10 \- Gás Liquefeito de Petróleo;

  2711\.21\.00 \- Gás Natural Veicular\.

Com base na resposta a pergunta 22 do “Perguntas\_e\_Respostas\_DRCST2\.docx”, as situações 1 e 2 podem ser identificadas pelo preenchimento dos campos VL\_ICMS\_ST\_COMPL e VL\_T\_CREDITO\_MVA\-SN do 2110 respectivamente\. Veja disposição hierárquica entre o 2110 e 2131:

Hierarquia:

2110

    2120

        2130

            2131

__MFS46838: Tratamento do Perfil D:__

Considerar que a nota fiscal do registro 2130 pode ser do estabelecimento Centralizador \(informado na tela de geração\) ou dos seus estabelecimentos Centralizados\. Com isso a busca dos Documentos Referenciados deve considerar o estabelecimento de origem do registro 2130 da tabela de Movimento\.

__Origem dos dados__: Tabela das Documentos Referenciados \(__SAFX192__\)

Esta tabela armazena o relacionamento de um documento fiscal com vários documentos de referência\. Três tipos de referência são possíveis:

1 \- Devolução \(Entrada\) x Documentos de Origem \(SaÍdas\)

2 \- Saída x Entradas \(Cálculo do Valor de Confronto da Port\. CAT 42/2018\)

3 \- Entrada de mercadoria adquirida de remetente indireto \(substituído\) x NF’s Emitidas pelos Substitutos Tributários

Na geração do registro 2131, são recuperadas apenas os registros com tipo de referência = 3\.

__Critérios da recuperação dos dados__:

1\) Registro superior \(__2110__\), deve obedecer às restrições especificadas na Portaria 208/2019\. Sendo assim, considerar os seguintes critérios:

     \- Campo VL\_ICMS\_ST\_COMPL igual a zero ou não preenchido;

     \- Campo VL\_T\_CREDITO\_MVA\-SN igual a zero ou não preenchido;

     \- NCM do Produto informado no campo COD\_ITEM do registro 2110 diferente de:  

  22071090 \- Etanol Hidratado Combustível;

  27101259 \- Gasolina Automotiva;

  27101921 \- Óleo Diesel;

  27111910 \- Gás Liquefeito de Petróleo;

  27112100 \- Gás Natural Veicular\.

      Obs: NCM do produto é apresentado no registro 0200 campo COD\_NCM\.

2\) Registro “pai” \(__2130__\) deve ser __Entrada \(Aquisição\)__ de __Remetente Indireto__\. Sendo assim, considerar os critérios:

     \- Campo “Nota de Devolução” \(ind\_nota\_devol\) da Tabela dos Movimentos \(__EST\_ST\_SC\_NF__\) = __“0” \- Entrada \(Aquisição\)__;

     \- Campo “Código Responsável Retenção” \(cod\_resp\_ret\) da Tabela dos Movimentos \(__EST\_ST\_SC\_NF__\) = __“2” – Remetente Indireto__;

          

3\) Recuperar os Documentos Referenciados \(SAFX192\), relacionados à nota do registro “pai” 2130\. Sendo assim, considerar aos critérios:

    \- Empresa \(campo 01 \- SAFX192\)                             à dados da identificação da nota do registro “pai” 2130, na Tabela dos Movimentos \(__EST\_ST\_SC\_NF__\);

__     MFS46838: Tratamento do Perfil D:__

    \- Estabelecimento \(campo 02 \- SAFX192\)                 à dados da identificação da nota do registro “pai” 2130, na Tabela dos Movimentos \(__EST\_ST\_SC\_NF__\);

    \- Estabelecimento \(campo 02 \- SAFX192\)                  à Estabelecimento origem da nota do registro “pai” 2130, na Tabela dos Movimentos \(__EST\_ST\_SC\_NF__\);

    \- Estabelecimento \(campo 02 \- SAFX192\)                 à dados da identificação da nota do registro “pai” 2130, na Tabela dos Movimentos \(__EST\_ST\_SC\_NF__\);

    \- Data Fiscal \(campo 03 \- SAFX192\)                          à dados da identificação da nota do registro “pai” 2130, na Tabela dos Movimentos \(__EST\_ST\_SC\_NF__\);

    \- Movimento Entrada/Saída \(campo 04 \- SAFX192\)   à dados da identificação da nota do registro “pai” 2130, na Tabela dos Movimentos \(__EST\_ST\_SC\_NF__\);

    \- Normal ou Devolução \(campo 05 \- SAFX192\)          à dados da identificação da nota do registro “pai” 2130, na Tabela dos Movimentos \(__EST\_ST\_SC\_NF__\);

    \- Tipo do Documento \(campo 06 \- SAFX192\)             à dados da identificação da nota do registro “pai” 2130, na Tabela dos Movimentos \(__EST\_ST\_SC\_NF__\);

    \- Pessoa Fis/Jur \(campo 07 e 8 \- SAFX192\)              à dados da identificação da nota do registro “pai” 2130, na Tabela dos Movimentos \(__EST\_ST\_SC\_NF__\);

    \- Número do Documento \(campo 09 \- SAFX192\)       à dados da identificação da nota do registro “pai” 2130, na Tabela dos Movimentos \(__EST\_ST\_SC\_NF__\);

    \- Série do Documento \(campo 10 \- SAFX192\)           à dados da identificação da nota do registro “pai” 2130, na Tabela dos Movimentos \(__EST\_ST\_SC\_NF__\);

    \- Subsérie do Documento \(campo 11 \- SAFX192\)     à dados da identificação da nota do registro “pai” 2130, na Tabela dos Movimentos \(__EST\_ST\_SC\_NF__\);

    \- Produto \(campos 12 e 13 – SAFX192\)                    à dados da identificação da nota do registro “pai” 2130, na Tabela dos Movimentos \(__EST\_ST\_SC\_NF__\);

    \- Número do Item                                                       à dados da identificação da nota do registro “pai” 2130, na Tabela dos Movimentos \(__EST\_ST\_SC\_NF__\);

    __\- Tipo de Referência \(campo 16 – SAFX192\) = 3__

Caso todos os critérios acima sejam atendidos, para cada linha recuperada será gerado um registro 2131 com as informações abaixo: 

01\-REG

Conteúdo fixo = “__2131__”

02\-CHV\_NFE\_RET

Campo __25 \- Chave de Acesso da Nfe Emitida pelo Substituto Tributário__ da tabela de Documentos Referenciados \(SAFX192\)\.

03\- CNPJ\_NFE\_RET

Campo __26 \- CNPJ do Substituto Tributário__ da tabela de Documentos Referenciados \(SAFX192\)\.

04 \- NUM\_ITEM\_NFE\_RET

Campo __23 – Item da Nota Fiscal de Referência__ da tabela de Documentos Referenciados \(SAFX192\)\.

05 \- QTDE\_NFE\_RET

Campo __24 \- Quantidade da Devolução ou Proporcional a Aquisição de Remetente Indireto__ da tabela de Documentos Referenciados \(SAFX192\)\.

__Críticas do 2131 relacionadas ao registro 2110:__

Caso os critérios 2 e 3 descritos acima sejam atendidos, mas um os critérios 1 não sejam atendidos, então gerar mensagem no Relatório do Log de Erros e __não__ gravar o registro 2131: 

Se o campo VL\_ICMS\_ST\_COMPL do Registro superior \(__2110__\) for diferente de zero, então:

Aviso: Registro 2131 não será gerado para a aquisição de remetente indireto, pois foi apurado complementação do imposto retido, na saída destinada a consumidor final, para o produto informado no registro 2110 \(VL\_ICMS\_ST\_COMPL maior que zero\)\.

Se o campo VL\_T\_CREDITO\_MVA\-SN do Registro superior \(__2110__\) for diferente de zero, então:

Aviso: Registro 2131 não será gerado para a aquisição de remetente indireto, pois foi apurado ressarcimento em decorrência de saída em operação interna destinada a empresa optante pelo Simples Nacional, para o produto informado no registro 2110 \(VL\_T\_CREDITO\_MVA\-SN maior que zero\)\.

Se o NCM do Produto informado no campo COD\_ITEM do registro superior __2110__ igual a 22071090 \- Etanol Hidratado Combustível, ou 27101259 \- Gasolina Automotiva, ou 27101921 \- Óleo Diesel, ou 27111910 \- Gás Liquefeito de Petróleo, ou 27112100 \- Gás Natural Veicular, então:

Aviso: Registro 2131 não será gerado para a aquisição de remetente indireto, pois o produto informado no registro 2110 possui NCM 2207\.10\.90, ou 2710\.12\.59, ou 2710\.19\.21, ou 2711\.19\.10, ou 2711\.21\.00, que é calculado por PMPF\.

Para todas essas críticas, acrescentar a chave de identificação do registro:

Registro 2130 \(Aquisição\): Nr\./Serie/Subsérie: xxxxxxxxxxx/xxx/xx, \- Chave NFe: xxxxxxxxxxxxxxxxx \- CNPJ Emitente: xxxxxxxxxxxxx \-  Nr\. Item:xxxxx\. NFe Emitida pelo Substituto: Chave NFe: xxxxxxxxxxxxxxxxxxxxxxxx – CNPJ: xxxxxxxxxxxxx \- Nr\. Item:xxxxx – Ind\-Cód Produto: x\-xxxxxxx\.

__Críticas do 2131 relacionadas ao registro 2130:__

Para cada registro pai __2130__, efetuar a seguinte consistência:

Totalizar as quantidades gravadas no campo 05 \- QTDE\_NFE\_RET dos registros filhos 2131\. 

Recuperar a quantidade do item de mercadoria da nota principal gravada no registro pai 2130, campo 09 \- QTDE\.

Caso sejam diferentes, então gerar mensagem no Relatório do Log de Erros e gravar normalmente o registro 2131: 

Aviso: Somatório das quantidades informadas nos registros 2131 diverge da quantidade da aquisição informada no registro pai 2130\.

Chave de identificação do registro \(dados apenas do registro pai 2130\):

Registro 2130 \(Aquisição\): Nr\./Serie/Subsérie: xxxxxxxxxxx/xxx/xx, \- Chave NFe: xxxxxxxxxxxxxxxxx \- CNPJ Emitente: xxxxxxxxxxxxx \-  Nr\. Item:xxxxx\.

# <a id="_Toc78989891"></a>Registro 2132: Complemento de Documento Fiscal Referenciado na Devolução de Aquisição

Registro “filho” do 2130\.

Este registro é gerado apenas quando o documento do registro “pai” 2130 for uma nota de devolução, ou seja, quando o campo __Nota de Devolução __da tabela dos movimentos = __1__ \(Devolução\)\.

O objetivo é demonstrar os documentos fiscais referenciados nas informações complementares da nota de devolução, que têm a finalidade de indicar os documentos da operação original da aquisição\. 

__MFS46838: Tratamento do Perfil D:__

Considerar que a nota fiscal do registro 2130 pode ser do estabelecimento Centralizador \(informado na tela de geração\) ou dos seus estabelecimentos Centralizados\. Com isso a busca dos documentos referenciados deve considerar o estabelecimento de origem do registro 2130 da tabela de Movimento\.

__Origem dos dados__: Tabela dos Documentos Fiscais Referenciados \(__SAFX116__\)

*\(Será utilizada a mesma tabela das informações complementares utilizada no Sped Fiscal, para geração do registro C113\) *

*Obs\.: Para a geração do registro 2132 é utilizada apenas a SAFX116, porque nesse caso, os documentos referenciados são sempre notas fiscais \(e nunca cupons fiscais\), já que se trata das entradas de aquisição do produto devolvido \(no registro 2114 a situação é diferente, pois as referências podem ser tanto notas como cupons, por isso a geração do 2114 utiliza também a SAFX117\)\.*

*\(Serão utilizadas as mesmas tabelas das informações complementares utilizadas no Sped Fiscal, para geração dos registros C113 e C114\) *

Esta tabela é vinculada à capa da nota \(SAFX07\), e assim, não têm a informação do produto\. Ela têm apenas as informações de identificação do documento referenciado\.

Para a geração do registro 2132, serão considerados somente os documentos referenciados recuperados da SAFX116 que tenham pelo menos um item do produto em questão \(produto do registro “avô” 2110\)\.

Desta forma, o procedimento é o seguinte:

  

- Pesquisa todos os registros da SAFX116 vinculados a nota fiscal de devolução do registro “pai” 2130;
- Dentre os documentos referenciados recuperados, serão considerados apenas aqueles que tenham entre os seus itens \(SAFX08\) o produto em questão \(produto do registro “avô” 2110\);

__Exemplo__:

__Dados da X07 / X08 / X116__

__Dados dos registros no arquivo__

__Notas de Aquisição__:

__NF: 85__

Item 1 – Produto A4

__NF: 120                               __

Item 1 – Produto A1            

Item 2 – Produto A5            

                                            

__NF: 350__

Item 1 – Produto A3

Item 2 – Produto A4

Item 3 – Produto A9

__Nota de Devolução__:

__NF: 522__

Item 1 – Produto A1

Item 2 – Produto A4

Documentos referenciados \(X116\): NF 120 e NF 350

__2110 Produto A1__

__     2120 __Valor Médio Unitário

            __2130 __NF 120

            __2130 __NF 522

                    __2132__ NF 120

           *\(Observar que existem 2 documentos referenciados na SAFX116 para a nota de *

*            devolução *__*522*__*\. Mas apenas o documento *__*120*__* seria gerado aqui, pois só ele tem*

*            itens do *__*Produto A1*__*\)*

__2110 __Produto A3

__     2120 __Valor Médio Unitário

            __2130 __NF 350

__2110 Produto A4__

__     2120 __Valor Médio Unitário

            __2130__ NF 85

            __2130__ NF 350

            __2130__ NF 522

                    __2132__ NF 350 

           *\(Observar que existem 2 documentos referenciados na SAFX116 para a nota de*

*           devolução *__*522*__*\. Mas apenas o documento *__*350*__* seria gerado aqui, pois só ele tem *

*           itens do *__*Produto A4*__*\)* 

__2110 __Produto A5

__     2120 __Valor Médio Unitário

            __2130__ NF 120

__2110 __Produto A9

__     2120 __Valor Médio Unitário

            __2130__ NF 350

__Critérios da recuperação dos documentos referenciados da SAFX116:__

     \- Campos 01 ao 11 = Campos de identificação da nota da Tabela de Movimentos \(nota de devolução gerada no registro “pai” 2130\);

__     MFS46838: Tratamento do Perfil D:__

    \- Estabelecimento \(campo 02\) à Estabelecimento origem da nota do registro “pai” 2130;

As informações do documento referenciado constam nos campos 13 ao 21 da SAFX116\.

Poderão ser recuperados ‘n’ registros de documentos referenciados\.

Para cada documento de referência recuperado, será feita a pesquisa para verificar se a nota tem itens do produto em questão ou não \(pesquisa dos itens descrita acima\)\.

Para a pesquisa dos itens 

A pesquisa dos itens na __SAFX08__ é feita a partir dos campos que identificam a nota de referência \(campo 13 ao campo 19\), e da identificação do produto em questão, da seguinte forma:

__Campos da SAFX08__

__Campos da SAFX116__

01\-Código da Empresa

01\-Código da Empresa

02\-Código do Estabelecimento

02\-Código do Estabelecimento

03\-Data Fiscal

Nesse caso o documento referenciado será sempre uma entrada\. Nas notas de entrada a DATA\_FISCAL equivale a data da entrada da mercadoria, diferente das saídas em que equivale à data de emissão da nota\. Por isso, na geração do 2114, é utilizada a data de emissão do documento de referência \(campo “19\-Data de Emissão” da SAFX116\), mas para geração do 2132 não é possível\. Observar que a SAFX116 não tem nem a data fiscal, nem a data da entrada da mercadoria\.

Por isso, para pesquisar os itens do documento na SAFX08, é necessário primeiro obter na capa da nota de referência, a informação da Data Fiscal da nota\. Para recuperar a capa:

 

 SAFX07                                              SAFX116

 01\-Código da Empresa                    = 01\-Código da Empresa

 02\-Código do Estabelecimento        = 02\-Código do Estabelecimento

 03\-Movimento E/S                           = 16\-Movimento Entrada/Saída

 06\-Indicador Pessoa Fis/Jur            = 17\-Indicador da Pessoa Fis/Jur

 07\-Código Pessoa Fis/Jur                = 18\-Código da Pessoa Fis/Jur

 08\-Número do Documento               = 13\-Número do Documento

 09\-Série do Documento                   = 14\-Sérire do Documento

 10\-Subsérie do Documento             = 15\-Subsérie do Documento

 11\-Data de Emissão                        = 19\-Data de Emissão

04\-Movimento E/S 

16\-Movimento E/S

07\-Indicador da Pessoa Fis/Jur

17\-Indicador da Pessoa Fis/Jur

08\-Código da Pessoa Fis/Jur

18\-Código da Pessoa Fis/Jur

09\-Número do Documento Fiscal

13\-Número do Documento Fiscal

10\-Série do Documento Fiscal

14\-Série do Documento Fiscal

11\-Subsérie do Documento Fiscal

15\-Subsérie do Documento Fiscal

13\-Indicador do Produto

__Indicador do Produto em questão \(produto do registro “avô” 2110\)__

14\-Produto

__Código do Produto em questão \(produto do registro “avô” 2110\)__

Obs\.: O Tipo de Documento não é usado na busca, pois a SAFX116 não tem campo do tipo de documento do documento de referência;

O objetivo desta pesquisa é apenas verificar se o documento referenciado tem ou não itens do produto em questão, sem importar quais são estes itens, já que as informações do item não serão utilizadas\.

__Gravação dos dados no registro 2132:__

Serão gravados no registro 2132 *apenas* aqueles documentos referenciados para os quais exista item do produto em questão \(conforme o exemplo descrito acima\)\. Assim, os documentos referenciados que *não* tiverem item do produto em questão, *serão desconsiderados*\.

Para cada documento referenciado a ser considerado, será gravado um registro 2132 com as seguintes informações:

01\-REG

Conteúdo fixo = “__2132__”

02\-CNPJ

Este campo é gerado com a informação do CNPJ da pessoa fis/jur do documento de referência \(campos __17\-Indicador Pessoa Fis/Jur__ e __18\-Código Pessoa Fis/Jur__ da SAFX116\), verificando o conteúdo da informação que consta no campo “06\-CPF\_CGC” da SAFX04:

  Se for um CNPJ à a informação será gerada neste campo;

  Se for um CPF à este campo será gerado sem informação \(“||”\); __\(\*\)__

__*\(\*\)*__* Este campo é de preenchimento obrigatório, mas não iremos gerar mensagem de erro nesse momento, pois é esperado que na  nota de entrada a pessoa fis/jur seja sempre uma pessoa jurídica\. *

03\-CHV\_NFE\_REF

Campo __21\-Chave de Acesso da NF\-Eletrônica__ da SAFX116\.

04\-DT\_E\_REF

Este campo é gerado com a informação da data da entrada da nota fiscal de referência, obtida na capa do documento de referência, conforme os critérios descritos acima\.

Campo __“20\-Data de Saída/Recebimento”__ da capa da nota de referência \(__SAFX07__\) 

*\(Lembrando que a SAFX116 tem apenas a informação da data de emissão do documento de referência, por isso, esta informação precisa ser recuperada do documento\)*

 

# <a id="_Toc78989892"></a>Registro 2133 – Nota Fiscal Complementar que Referenciou a Aquisição Informada no Registro 2130

Registro “filho” do 2130\.

Este registro demonstra as notas fiscais complementares associadas à nota de entrada informada no registro 2130\.

__MFS46838: Tratamento do Perfil D:__

Considerar que a nota fiscal do registro 2130 pode ser do estabelecimento Centralizador \(informado na tela de geração\) ou dos seus estabelecimentos Centralizados\. Com isso a busca das Notas Complementares deve considerar o estabelecimento de origem do registro 2130 da tabela de Movimento\.

__Origem dos dados__: Tabela das Notas Complementares \(__EST\_ST\_SC\_NF\_COMPL__\)

Esta tabela é gerada numa etapa preliminar, no menu “*Geração > Geração dos Movimentos > Entradas*”\.  As notas complementares são identificadas durante o processo, e seus valores e quantidades são totalizados na nota original \(2130\)\.   

Ver regras desta geração no documento de regras “*MTZ\-Ressar\-SC\-Geracao\_Movimentos\_Entradas”\.*

__Critérios da recuperação dos dados__:

    \- Empresa à código da Empresa;

    \- Estabelecimento à código do Estabelecimento em questão;

__     MFS46838: Tratamento do Perfil D:__

    \- Estabelecimento à Estabelecimento origem da nota do registro “pai” 2130;

    \- Período à período informado em tela para geração do arquivo;

    \- Indicador do Tipo de Registro à = “__2133__”;

    \- Produtoà produto do registro “pai” 2110;

    \- Data Fiscal                    à dados da identificação da nota do registro “pai” 2130;

    \- Tipo do Documento       à dados da identificação da nota do registro “pai” 2130;

    \- Série do Documento      à dados da identificação da nota do registro “pai” 2130;

    \- Número do Documento  à dados da identificação da nota do registro “pai” 2130;

    \- Pessoa Fis/Jur                à dados da identificação da nota do registro “pai” 2130;

    \- Número do Item              à dados da identificação da nota do registro “pai” 2130;

    \- Movimento E/S                à dados da identificação da nota do registro “pai” 2130;

Para cada linha recuperada será gerado um registro 2133 com as informações abaixo: 

01\-REG

Conteúdo fixo = “__2133__”

02\-CHV\_NFE\_COMP

Campo __Chave Documento Fiscal Eletrônico da Nota Complementar __da tabela das notas complementares\.

03\-NUM\_ITEM\_NFE\_COMP

Campo __Número do Item da Nota Complementar __da tabela das notas complementares\.

# <a id="_Toc78989893"></a>Registro 2134 – Complemento para NF\-E de Aquisição de Remetente Indireto

__\[MFS32070\] __Inclusão do registro

Registro “filho” do 2130, somente deve ser gerado a partir de novembro de 2019

	

Este registro deve ser apresentado sempre que o documento fiscal identificado no Registro 2130 se referir a uma entrada de mercadoria adquirida de Remetente Indireto \(COD\_RESP\_RET = 2\), que no XML da NF\-e não tenha preenchido a *tag *especifica para o Grupo Tributação do ICMS = 60\.  Ou seja, se a *tag *especifica do XML estiver preenchida, o registro não será gerado\.

Tabela dos Movimentos \(__EST\_ST\_SC\_NF__\)

Esta tabela é gerada numa etapa preliminar, no menu “*Geração > Geração dos Movimentos > Entradas*”\. Ver regras desta geração no documento de regras “*MTZ\-Ressar\-SC\-Geracao\_Movimentos\_Entradas”\.*

__Critérios da recuperação dos dados__:

    \- Empresa à código da Empresa;

    \- Estabelecimento à código do Estabelecimento em questão;

    \- Período à período informado em tela para geração do arquivo;

    \- Indicador do Tipo de Registro à = “__2130__” \(apenas os movimentos de entrada ou devolução de entrada a serem gravados no registro 2130\);

    \- Produtoà produto do registro “avô” 2110;

    \- Código Responsável Retenção à = “2” \(apenas Remetente Indireto\);

    \- Indicador de preenchimento dos Valores de ICMS cobrados anteriormente por ST à = “N” \(apenas os movimentos de entrada ou devolução de entrada que não tenham a tag do XML preenchida\);

Para cada linha recuperada será gerado um registro 2134 com as informações abaixo: 

01\-REG

Conteúdo fixo = “__2134__”

02\-COD\_IND\_XML

Campo __Indicador de preenchimento dos Valores de ICMS cobrados anteriormente por ST __da tabela dos movimentos\.

Se __Indicador de preenchimento dos Valores de ICMS cobrados anteriormente por ST __igual a “N”

   Gravar “1”\.

# <a id="_Toc78901904"></a><a id="_Toc78989894"></a>Registro 2135 – Nota Fiscal Eletrônica de Ajuste que Referenciou a Aquisição Informada no Registro 2130

__\[MFS58553\]__

Registro “filho” do 2130\.

Este registro demonstra as notas fiscais eletrônicas de ajuste associadas à nota de entrada informada no registro 2130\.

__MFS46838: Tratamento do Perfil D:__

Considerar que a nota fiscal do registro 2130 pode ser do estabelecimento Centralizador \(informado na tela de geração\) ou dos seus estabelecimentos Centralizados\. Com isso a busca das Notas Eletrônicas de ajuste deve considerar o estabelecimento de origem do registro 2130 da tabela de Movimento\.

__Origem dos dados__: <a id="_Hlk78989788"></a>Tabela das Notas Eletrônicas de Ajuste \(__EST\_ST\_SC\_NF\_AJ__\)

Esta tabela é gerada numa etapa preliminar, no menu “*Geração > Geração dos Movimentos > Entradas*”\.  As notas de ajuste são identificadas durante o processo, e seus valores são totalizados na nota original \(2130\)\.   

Ver regras desta geração no documento de regras “*MTZ\-Ressar\-SC\-Geracao\_Movimentos\_Entradas”\.*

__Critérios da recuperação dos dados__:

    \- Empresa à código da Empresa;

    \- Estabelecimento à código do Estabelecimento em questão;

__     MFS46838: Tratamento do Perfil D:__

    \- Estabelecimento à Estabelecimento origem da nota do registro “pai” 2130;

    \- Período à período informado em tela para geração do arquivo;

    \- Produtoà produto do registro “pai” 2110;

    \- Data Fiscal                    à dados da identificação da nota do registro “pai” 2130;

    \- Tipo do Documento       à dados da identificação da nota do registro “pai” 2130;

    \- Série do Documento      à dados da identificação da nota do registro “pai” 2130;

    \- Número do Documento  à dados da identificação da nota do registro “pai” 2130;

    \- Pessoa Fis/Jur                à dados da identificação da nota do registro “pai” 2130;

    \- Número do Item              à dados da identificação da nota do registro “pai” 2130;

    \- Movimento E/S                à dados da identificação da nota do registro “pai” 2130;

Para cada linha recuperada será gerado um registro 2133 com as informações abaixo: 

01\-REG

Conteúdo fixo = “__2135__”

02\-CHV\_NFE\_COMP

Campo __Chave Documento Fiscal Eletrônico da Nota de Ajuste __da tabela das Notas Eletrônicas de Ajuste\.

03\-NUM\_ITEM\_NFE\_COMP

Campo __Número do Item da Nota de Ajuste __da tabela das Notas Eletrônicas de Ajuste\.

# <a id="_Toc78989895"></a>Registro 2990: Encerramento do Bloco 2

REG

Conteúdo fixo = “__2990__”

QTD\_LIN\_2

Quantidade total de linhas informadas no Bloco 2, incluindo os registros de abertura e fechamento do Bloco\.

= = = = = =

 

