# MTZ-Ressarc-PR-Meio_Magnetico_ADRC_ST_CD

- **Fonte:** MTZ-Ressarc-PR-Meio_Magnetico_ADRC_ST_CD.docx
- **Modificado:** 2021-12-09
- **Tamanho:** 98 KB

---

THOMSON REUTERS

Módulo Ressarcimento e Complemento de ICMS\-ST – Paraná 

Geração do Arquivo Magnético da Central de Distribuição – ADRC\-ST CD 

__Localização__: Menu Estadual, módulo Ressarcimento de ICMS\-ST – PR, menu Geração 🡪 NPF 003/20 🡪 Central de Distribuição 🡪 Meio Magnético ADRC\-ST \(CD\) 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS34476__

Geração do Meio Magnético da CD

Geração do Meio Magnético da Central de Distribuição \(ADRC\-ST CD\)

03/04/2020 

\(criação do documento\)

__MFS61729__

Andréa Rocha 

Alteração da regra do campo N\_NF, incluir tratamento para o campo o número do documento fiscal com tamanho maior que 9 posições\.

17/03/2021

__MFS76535__

Andréa Rocha

Inclusão de mensagem de erro para os produtos que não tem o campo CEST preenchido\.

09/12/2021

Sumário

[1\.	Regras Gerais	2](#_Toc36811485)

[2\.	Parâmetros de Tela	3](#_Toc36811486)

[3\.	Processamento	5](#_Toc36811487)

[4\.	Registro 0001 – Abertura e Identificação do Contribuinte	6](#_Toc36811488)

[5\.	Registro 1001 – Registro Analítico do Produto	7](#_Toc36811489)

[6\.	Registro 1101 \- Totalizador das Entradas do Produto	9](#_Toc36811490)

[7\.	Registro 1111 – Notas Fiscais de Entrada	10](#_Toc36811491)

# <a id="_Toc36811485"></a>Regras Gerais

A geração do meio magnético da Central de Distribuição \(ADRC\-ST CD\) segue os padrões do módulo Sped Fiscal \(Framework\), com as seguintes abas:

Parâmetros

Aba dos parâmetros para a geração do arquivo\.

Processos

Esta aba mostra as gerações já efetuadas, e o usuário pode selecionar uma geração para consulta\. 

Log

Nesta aba é exibido o relatório do log de erros da geração\. 

Arquivos

Nesta aba o usuário pode salvar o arquivo referente às gerações já efetuadas\.

Quantidade de Registros Gerados

Nesta aba será mostrado um resumo com a quantidade total de registros gerados para cada tipo de registro, no seguinte formato:

Registro 0001 \- Abertura e Identificação do Contribuinte 

999999

Registro 1001 \- Registro Analitico do Produto 

999999

Registro 1101 \- Totalizador das Entradas 

999999

Registro 1111 – Notas Fiscais de Entrada 

999999

Registro 9999 \- Encerramento

999999

__Layout do Arquivo__: Ver layout e informações técnicas para geração do arquivo no manual da Sefaz PR: “Manual\_ADRC\_ST – PR\.pdf” \(Vrs 1\.0\)

__Nome do arquivo__:  “__999999\_XXXXXX\_MM\_AAAA\_ADRC\_ST\_CD\_PR__”

Sendo:

__999999__ – Número do processo \(o default é usar o processo no nome do arquivo, mas o usuário pode solicitar não utilizá\-lo, conforme o parâmetro “*Gerar arquivo sem número do processo*” da aba “Arquivo” do Framework\);__ __

__XXXXXX __– Código do estabelecimento;

__MM__ – Mês da geração;

__AAAA__ – Ano da geração;

__“ADRC\_ST\_CD\_PR”__ – Conteúdo fixo que indica a obrigação;

# <a id="_Toc36811486"></a>Parâmetros de Tela

Meio Magnético ADRC\-ST \(CD\)

  Estabelecimento Central Distribuição: \[ XXXXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX \]

  Período:     \[99/9999\]

  Versão:       \[    \]

  Finalidade: \[                                             \]

        

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/__

__Default__

__Regra__

Estabelecimento Central  Distribuição

Alfanumérico 

__S__

S

Este campo é uma lista de todos os estabelecimentos cadastrados como “Central de Distribuição” na parametrização dos Dados Iniciais\.

Trata\-se dos estabelecimentos informados no campo “*Estabelecimento da Central de Distribição*” da parametrização dos dados iniciais de todos os estabelecimentos\.

O usuário deverá selecionar a central de distribuição desejada\.

Caso a lista não tenha informação \(o que acontecerá se nenhum dos estabelecimentos tiver o campo da Central de Distribuição preenchido\), então será exibida a seguinte mensagem logo após a abertura da tela:

*“Não existem estabelecimentos cadastrados como Central de Distribuição na parametrização dos dados iniciais de nenhum estabelecimento \(campo “Estabelecimento da Central de Distribição”\)”*

<a id="_Hlk517437550"></a>Período

Data

\(mês e ano\) 

S

S

MM/AAAA

Neste campo o usuário informa o período \(mês e ano\) para a geração do arquivo\.

Versão

Alfanumérico 

S

N

Lista

Este campo é uma lista, que a princípio terá apenas uma opção:

“1\.0”

Finalidade

Alfanumérico 

S

N

Lista

Default = “Arquivo original”

Este campo é uma lista com as seguintes opções:

\- Arquivo original

\- Arquivo substituto

# <a id="_Toc36811487"></a>Processamento

Origem dos dados:  \- Tabelas de Cadastro dos Estabelecimentos;

                                \- Tabela de Cadastro dos Produtos \(SAFX2013\);

                                \- Tabela de Cadastro das Pessoas Fis/Jur \(SAFX04\);

                                \- Tabela dos Movimentos de Entradas; 

                                \- Tabela dos Totais por Produto;

A geração do meio magnético da CD é feita a partir da movimentação do período, e tem como pré\-requisito a execução da Geração dos Dados da Central de Distribuição\.

Para o estabelecimento Central de Distribuição informado em tela, será gerado um arquivo com as seguintes informações:

__Bloco__

__Registro__

__Descrição / Hierarquia__

__Nível__

__0__

__0001__

Abertura e Identificação do Contribuinte

0

__1__

__1001__

   Registro Analitico do Produto

1

__1__

__1101__

       Registro Totalizador das Entradas

2

__1__

__1111__

            Notas Fiscais de Entrada

3

__9__

__9999__

Registro de Encerramento

0

A seguir serão descritas as regras sobre a recuperação dos dados e preenchimento dos campos para cada um dos registros citados acima\.

# <a id="_Toc36811488"></a>Registro 0001 – Abertura e Identificação do Contribuinte

Este registro é único no arquivo, e será gerado a partir das informações de cadastro do estabelecimento central de distribuição, e de alguns parâmetros informados em tela\.

Preenchimento dos campos:

01A

REG

Conteúdo fixo = “__0001__”

02A

COD\_VERSAO

Conteúdo fixo = “100”

\(A geração deste campo depende da versão informada em tela, mas a princípio, a lista do campo “Versão” tem apenas uma opção\)

03A

MES\_ANO

Mês e ano do período informado em tela

04A

CNPJ

CNPJ do estabelecimento Central de Distribuição informado em tela \(cadastro do estabelecimento\)

05A

IE

Inscrição estadual do estabelecimento Central de Distribuição informado em tela, na sua UF\.

Campo “*Inscrição Estadual*” da Tabela de Cadastro das Inscrições Estaduais \(módulo Parâmetros, item Preliminares > Inscrições Estaduais\), a partir do código do estabelecimento \+ UF do estabelecimento\. 

06A

NOME

Razão social do estabelecimento Central de Distribuição informado em tela \(cadastro do estabelecimento\)

07A

CD\_FIN

A geração deste campo depende da opção informada em tela para o campo “Finalidade”, da seguinte forma:

Se Finalidade = “Arquivo original”

      O campo será gerado com “0”;

 

Se Finalidade = “Arquivo substituto”

      O campo será gerado com “1”; 

# <a id="_Toc36811489"></a>Registro 1001 – Registro Analítico do Produto

Será gerado um registro 1001 para cada produto referenciado nos movimentos gravados no registro das notas fiscais \(registros 1111\)\.

*\(Haverá apenas um registro 1001 para cada produto, independente da quantidade de movimentos\)*

As informações para geração deste registro são obtidas a partir das seguintes tabelas:

- Tabela de Cadastro dos Produtos \(SAFX2013\)\. Para recuperar o registro do produto será considerado o registro de maior data de validade, que seja < = a data final do período \(data do último dia do período da geração\);
- Tabelas da Parametrização dos Produtos \(Por Código e Por NCM\)\. Estas tabelas são utilizadas para obter as alíquotas e o indicador de FECOP;

Preenchimento dos campos:

01B

REG

Conteúdo fixo = “__1001__”

02B

IND\_FECOP

Neste campo é informado se o produto é sujeito ao Fundo de Combate a Pobreza \(FECOP\), informação que consta na parametrização de produtos do módulo \(menu “*Parâmetros 🡪 Produtos 🡪 Por Código*” __ou__ “*Parâmetros 🡪 Produtos 🡪 Por NCM*”\)\. 

Se campo “*Sujeito ao FCP*” da parametrização nulo ou = “N”

     O campo será gravado com “0”; 

Senão

     O campo será gravado com “1”; 

*Obs\.: Para acessar esta parametrização, primeiro é verificado se o produto consta na parametrização por código, e caso não, será verificado se o NCM do produto consta na parametrização por NCM\. É o mesmo procedimento feito na geração dos movimentos de entradas e saídas\)*

03B

COD\_ITEM

A geração deste campo depende da parametrização dos dados inicias \(menu “*Parâmetros🡪 Dados Iniciais”\)\.*

Como a Central de Distribuição não precisa ter um cadastro nos Dados Iniciais, será utilizado o registro de qualquer uma das filiais \(qualquer outro estabelecimento\), cuja parametrização tenha o campo “*Estabelecimento da Central de Distribuição*” = central de distribuição informada para a geração:

Se parâmetro “*Considerar o indicador no código do produto*” marcado,

     O campo será gerado com a concatenação do indicador \+ código do produto \(X\-XXXXXXXXXXXXXX\);

Senão

      O campo será gerado apenas com o código do produto;

04B

COD\_BARRAS

Campo “40\-Código de Barras” da SAFX2013\.

Conforme a legislação, os códigos GTIN/EAN podem ter o tamanho de 8, 12, 13 ou 14 dígitos\. Como na SAFX2013 o tamanho do campo tem 60 posições, caso o conteúdo do campo ultrapasse o permitido no layout do PR \(14 posições\), o que pode acontecer em casos de erro, o campo será gerado sem informação “\(||”\), e no log será gravada a seguinte mensagem de erro: *“O tamanho do campo Código de Barras do cadastro do Produto ultrapassa o tamanho máximo permitido no layout \(14\)\. O campo B04\-COD\_BARRAS será gerado sem informação”*\.

O log deve demonstrar o códido do produto para que o usuário possa identificar o problema\.

 

05B

COD\_ANP

Campo “41\-Código ANP” da SAFX2013\.

Conforme a legislação, os códigos ANP têm o tamanho de 9 dígitos\. Como na SAFX2013 o tamanho do campo tem 12 posições, caso o conteúdo do campo ultrapasse o permitido no layout do PR \(9 posições\), o que pode acontecer em casos de erro, o campo será gerado sem informação \(“||”\), e no log será gravada a seguinte mensagem de erro: *“O tamanho do campo Código ANP do cadastro do Produto ultrapassa o tamanho máximo permitido no layout \(9\)\. O campo B05\-COD\_ANP será gerado sem informação”*\.

O log deve demonstrar o códido do produto para que o usuário possa identificar o problema\.

06B

NCM

Campo “05\-Código NBM” da SAFX2013 \(*considerando apenas as 8 primeiras posições*\)\.

07B

CEST

Campo “54\- Código Especificador da Substituição Tributária” da SAFX2013\.

__\[MFS76535\]__ Inclusão da mensagem de erro para o campo CEST

Como o campo CEST é obrigatório no layout, quando o Código Especificador da Substituição Tributária não estiver preenchido na SAFX2013, o campo será gerado sem informação \(“||”\), e no log será gravada a seguinte mensagem de erro: *“O campo CEST deve ser preenchido”*\.

O log deve demonstrar o códido do produto para que o usuário possa identificar o problema\.

08B

DESCR\_ITEM

Campo “04\-Descrição do Produto” da SAFX2013\.

09B

UNID\_ITEM	

Campo “14\-Código de Medida” da SAFX2013 \(unidade da SAFX2007\)

10B

ALIQ\_ICMS\_ITEM

Neste campo será informada a alíquota interna do produto, informação que consta na parametrização de produtos do módulo \(menu “*Parâmetros 🡪 Produtos 🡪 Por Código*” __ou__ “*Parâmetros 🡪 Produtos 🡪 Por NCM*”\)\. 

Campo “Alíquota Interna dos Produtos”

*Obs\.: Para acessar esta parametrização, primeiro é verificado se o produto consta na parametrização por código, e caso não, será verificado se o NCM do produto consta na parametrização por NCM\. É o mesmo procedimento feito na geração dos movimentos de entradas e saídas\)*

11B

ALIQ\_FECOP

Este campo será preenchido apenas quando o campo B02\-IND\_FECOP = “1” \(ver regra B02\)\.

Se campo B02\-IND\_FECOP = “1”

      O campo será gravado com a alíquota do FECOP que consta na parametrização do produto \(campo “Alíquota FCP”\)

Senão

      O campo será gravado sem informação \(“||”\);

# <a id="_Toc36811490"></a>Registro 1101 \- Totalizador das Entradas do Produto

<a id="OLE_LINK52"></a>

Registro “filho” do registro 1001\-Registro Analítico do Produto\.

Origem dos dados: Tabela dos Totais por Produto

Para cada produto gravado no registro 1001, será gravado um único registro 1101, cujos valores são recuperados da __Tabela dos Totais por Produto__, a partir dos seguintes critérios:

\- Empresa                   = Código da empresa do login

\- Estabelecimento       = Código do estabelecimento Central Distribuição informado em tela

\- Período \(mês e ano\) = Período \(mês a ano\) informado na tela da geração

\- Produto                     = Produto em questão \(indicador e código\)

\- Tipo de Registro       = “__1101__”

Preenchimento dos campos:

01C

REG

Conteúdo fixo = “__1101__”

02C

QTD\_TOT\_ENTRADA

Campo __QTD\_TOT\_ENTRADA\_E__ da Tabela dos Totais do Produto

03C

VL\_BC\_ICMSST\_UNIT\_MED 

Campo __VL\_BC\_ICMSST\_UNIT\_MED\_E__ da Tabela dos Totais do Produto 

04C

VL\_TOT\_ICMS\_SUPORT\_ENTR 

Campo __VL\_TOT\_ICMS\_SUPORT\_E__ da Tabela dos Totais do Produto

05C

VL\_UNIT\_MED\_ICMS\_SUPORT\_ENTR 

Campo __VL\_UNIT\_MED\_ICMS\_SUPORT\_E__ da Tabela dos Totais do Produto

06C

QTD\_TRANSF

Campo __QTD\_TRANSF\_E__ da Tabela dos Totais do Produto

# <a id="_Toc36811491"></a>Registro 1111 – Notas Fiscais de Entrada

Este registro é filho do “1101\-Totalizador das Entradas do Produto”, e demonstra as notas fiscais de entrada do produto\.

Origem dos dados: Tabela dos movimentos do período

\- Empresa                   = Código da empresa do login

\- Estabelecimento       = Código do estabelecimento Central de Distribuição informado em tela 

\- Período \(mês e ano\) = Período \(mês a ano\) informado na tela da geração

\- Produto                     = Produto em questão \(indicador e código\)

\- Tipo de Registro       = “__1111__”

Para cada linha recuperada da tabela, conforme os critérios acima, será gravado um registro 1111\.

 

Preenchimento dos campos:

01D

REG

Conteúdo fixo = “__1111__”

02D

DT\_DOC

Campo “__Data Emissão__” da Tabela dos Movimentos

03D

COD\_RESP\_RET

Campo “__Código Responsável Retenção__” da Tabela dos Movimentos

04D

CST\_CSOSN 

Campo “__CST\_ICMS__” da Tabela dos Movimentos

05D

CHAVE

Campo “__Chave Documento Fiscal Eletrônico”__ da Tabela dos Movimentos

06D

N\_NF

Campo “__Número do Documento__” da Tabela dos Movimentos\.

__\[MFS61729\]__ Inclusão do tratamento para o Número do Documento com tamanho maior que 9 posições para desconsiderar os zeros à esquerda

Se o conteúdo do campo ultrapassar o tamanho do layout \(9 posições\)

     Se essas posições à esquerda estiverem preenchidas com zeros \(considerando 12, 11 ou 10 posições preenchidas\)

          Os zeros devem ser desconsiderados e o campo deve ser gerado com as 9 posições restantes

     Senão \(se essas posições à esquerda __não__ estiverem preenchidas com zeros\)

          Será gerada a seguinte mensagem de erro no log: *“O campo N\_NF ultrapassou o tamanho máximo permitido no   *

*          layout do registro 1110 \(9 posições\)”*

          O log deve exibir os dados de identificação da nota para permitir a conferência do usuário\.

07D

CNPJ\_EMIT

Neste campo será informado o CNPJ da Pessoa Fis/Jur do documento fiscal \(campo 06 da SAFX04\)\. Trata\-se da __Pessoa Fis/Jur__ que consta da Tabela dos Movimentos\.  

08D

UF\_EMIT

Neste campo será informada a sigla da UF da Pessoa Fis/Jur do documento fiscal \(campo 19\-UF da SAFX04\)\. Trata\-se da __Pessoa Fis/Jur__ que consta da Tabela dos Movimentos\.  

09D

CNPJ\_DEST

Neste campo será informado o CNPJ do Estabelecimento informante do arquivo \(= campo __04A\-CNPJ__ do registro 0000\)\.

10D

UF\_DEST

Neste campo será informada a sigla da UF do Estabelecimento informante do arquivo \(UF do cadastro do Estabelecimento Central de Distribuição\)\.  

11D

CFOP

Campo “__CFOP__” da Tabela dos Movimentos\.

12D

N\_ITEM

Campo “__Número do Item__” da Tabela dos Movimentos;

13D

UNID\_ITEM

Campo “__Unidade de Medida__” da Tabela dos Movimentos;

14D

QTD\_ENTRADA

Campo “__Quantidade da Entrada__” da Tabela dos Movimentos\.

15D

VL\_UNIT\_ITEM

Campo “__Valor Unitário__” da Tabela dos Movimentos\.

16D

VL\_BC\_ICMS\_ST

Campo “__Valor Base ICMS\-ST__” da Tabela dos Movimentos\.

17D

VL\_ICMS\_SUPORT\_ENTR

Campo “__Valor ICMS Suportado__” da Tabela dos Movimentos\.

= = = = = =

 

