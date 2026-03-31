# MTZ-Ressarc-SC-Geracao-do-Meio-Magnetico-Bloco0

- **Fonte:** MTZ-Ressarc-SC-Geracao-do-Meio-Magnetico-Bloco0.docx
- **Modificado:** 2025-10-30
- **Tamanho:** 116 KB

---

THOMSON REUTERS

Módulo Ressarcimento e Complemento ICMS\-ST – SC \(Portaria SEF 378/2018\)

Geração do Meio Magnético 

Bloco 0

__Localização__: Menu Estadual, módulo Ressarcimento de ICMS\-ST – SC \(Port\.SEF 378/2018\), menu Geração 🡪 Geração do Meio Magnético

Este documento é específico das regras de geração do Bloco 0\.

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

__MFS68852__

Liliane Assaf

Registro 0220: tratamento do campo 137 – Quantidade Convertida da SAFX08

12/07/2021

__MFS46838__

Tratamento do Perfil D

Alteração no registro 0000 – campo COD\_VER

Inclusão do registro 0150\.

21/09/2021

__MFS74713__

Andréa Rocha

Alteração no registro 0000 – campo COD\_VER\.

10/11/2021

__MFS76135__

Liliane Assaf

Atualização de versão EFD115:

 \- Alteração no registro 0000 – campo COD\_VER

 \- Alteração no registro 0220 – inclusão do campo 04 – COD\_BARRA

08/12/2021

__MFS78891__

Liliane Assaf

Correção do Fator de Conversão quando calculado pelo campo 137 – Quantidade Convertida da SAFX08\. Considerar que pode existir mais de um fator de conversão de uma medida origem XX para uma medida destino YY, quando relacionado a produtos distintos\. \(correção da MFS68852\)\.

Exemplo:

Med Origem | Medi Destino | Produto | Fator

UN               | PAC               | 1\-001     | 0,6

UN               | PAC               | 1\-002     | 0,12

21/03/2022

__MFS86363__

Aline Melo

Atualização da versão EFD116 no campo COD\_VER do registro 0000

24/06/2022

__MFS92152__

Andréa Rocha

Inclusão de novo layout para o campo EFD versão do período, para possibilitar a geração para o ano de 2017\. Conforme previsto em lei, deve abranger as saídas internas destinadas a consumidor final realizadas após 05/04/2017\.

19/08/2022

__MFS579429__

Liliane Assaf

Atualização da versão EFD117 no campo COD\_VER do registro 0000

20/10/2023

__MFS581026__

Andréa Rocha

Inclusão da geração do registro 0004 \- Identificação do Estabelecimento Incorporador, a partir da versão EFD116\.

29/02/2024

__MFS693938__

Liliane Assaf

Inclusão do layout EFD118\. no campo COD\_VER do registro 0000

30/10/2024

__MFS861831__

Graciela Soares

Inclusão do layout EFD119\. no campo COD\_VER do registro 0000

30/10/2025

Sumário

[1\.	Regras Gerais do Bloco 0	1](#_Toc181177404)

[2\.	Registro 0000 – Abertura do Arquivo Digital e Identificação da Entidade	1](#_Toc181177405)

[3\.	Registro 0001 – Abertura do Bloco 0	1](#_Toc181177406)

[4\.	Registro 0004 – Identificação do Estabelecimento Incorporador	1](#_Toc181177407)

[5\.	Registro 0005 – Dados Complementares da Entidade	1](#_Toc181177408)

[6\.	Registro 0100 – Dados do Contabilista	1](#_Toc181177409)

[7\.	Registro 0150 – Identificação do Participante	1](#_Toc181177410)

[8\.	Registro 0190 – Identificação das Unidades de Medida	1](#_Toc181177411)

[9\.	Registro 0200 – Tabela de Identificação do Item	1](#_Toc181177412)

[10\.	Registro 0205 – Código Anterior do Item	1](#_Toc181177413)

[11\.	Registro 0206 – Código do Produto conforme Tabela ANP	1](#_Toc181177414)

[12\.	Registro 0220 – Fatores de Conversão de Unidade	1](#_Toc181177415)

[13\.	Registro 0990 – Encerramento do Bloco 0	1](#_Toc181177416)

# <a id="_Toc181177404"></a>Regras Gerais do Bloco 0

Para cada estabelecimento selecionado em tela será gerado um arquivo\.

Os registros do Bloco 0 são gerados a partir dos produtos, unidades de medida e fatores de conversão referenciados no Bloco 2;

Os registros do Bloco 0 seguem o layout do Sped Fiscal\.

\(Os registros não citados nas regras a seguir não devem ser gerados, conforme orientação da Portaria SEF 378/2018\)

# <a id="_Toc181177405"></a>Registro 0000 – Abertura do Arquivo Digital e Identificação da Entidade

Registro único no arquivo, gerado a partir das informações de cadastro do estabelecimento, e de alguns parâmetros informados em tela\.

REG

Conteúdo fixo = “__0000__”

COD\_VER

__\[MFS92152\] __Inclusão de novo layout para o campo EFD versão do período, para possibilitar a geração para o ano de 2017

Este campo é preenchido de acordo com o código da versão da EFD informado em tela, da seguinte forma:

Se código = “EFD100” 🡪 o campo será preenchido com “001”;

Se código = “EFD101” 🡪 o campo será preenchido com “002”;

Se código = “EFD102” 🡪 o campo será preenchido com “003”;

Se código = “EFD103” 🡪 o campo será preenchido com “004”;

Se código = “EFD104” 🡪 o campo será preenchido com “005”;

Se código = “EFD105” 🡪 o campo será preenchido com “006”;

Se código = “EFD106” 🡪 o campo será preenchido com “007”;

Se código = “EFD107” 🡪 o campo será preenchido com “008”;

Se código = “EFD108” 🡪 o campo será preenchido com “009”;

Se código = “EFD109” 🡪 o campo será preenchido com “010”;

Se código = “EFD110” 🡪 o campo será preenchido com “011”;

Se código = “EFD111” 🡪 o campo será preenchido com “012”;

Se código = “EFD112” 🡪 o campo será preenchido com “013”;

__MFS46838: Tratamento do Perfil D:__

Preenchimento do campo depende do Perfil do estabelecimento que consta nos dados iniciais \(menu Parâmetros > Dados Iniciais, campo “Perfil da EFD”\)\.

Caso Perfil = “__A__” ou “__B__”, então preencher o campo COD\_VER conforme código da versão da EFD informado em tela, da seguinte forma:

Se código = “EFD110” 🡪 o campo será preenchido com “011”;

Se código = “EFD111” 🡪 o campo será preenchido com “012”;

Se código = “EFD112” 🡪 o campo será preenchido com “013”;

__\[MFS74713\] __Inclusão dos layout EFD113 e EFD114

Se código = “EFD113” 🡪 o campo será preenchido com “014”;

Se código = “EFD114” 🡪 o campo será preenchido com “015”;

\[__MFS76135\] Inclusão do layout EFD115__

             Se código = “EFD115” 🡪 o campo será preenchido com “016”;

\[__MFS76135\] Inclusão do layout EFD116__

             Se código = “EFD116” 🡪 o campo será preenchido com “017”;

\[__MFS579429\] Inclusão do layout EFD117__

             Se código = “EFD117” 🡪 o campo será preenchido com “018”;

__MFS693938 Inclusão do layout EFD118__

             Se código = “EFD118” 🡪 o campo será preenchido com “019”;

__MFS693938 Inclusão do layout EFD119__

             Se código = “EFD119” 🡪 o campo será preenchido com “020”;

Caso Perfil = “__C__” ou “__D__”, então não preencher o campo COD\_VER\.

COD\_FIN

A geração deste campo depende da opção informada em tela para o campo “Finalidade”, da seguinte forma:

Se Finalidade = “Remessa do arquivo original”

      O campo será gerado com “0”;

 

Se Finalidade = “Remessa do arquivo substituto”

      O campo será gerado com “1”; 

DT\_INI

Data do primeiro dia do período informado em tela

DT\_FIM

Data do último dia do período informado em tela

NOME

Razão social do estabelecimento informado em tela \(cadastro do estabelecimento\)

CNPJ

CNPJ do estabelecimento informado em tela \(cadastro do estabelecimento\)

CPF

Este campo é gerado sem informação \(‘||’\)

UF

Código da UF do estabelecimento informado em tela

IE

Inscrição estadual do estabelecimento no estado de __SC__\.

Campo “*Inscrição Estadual*” da Tabela de Cadastro das Inscrições Estaduais \(tabela REGISTRO\_ESTADUAL\), no módulo Parâmetros, item Preliminares > Inscrições Estaduais\. 

Quando a inscrição estadual não for identificada, será gerada a seguinte mensagem de crítica no log: 

*                                               “O campo IE é de preenchimento obrigatório, e não foi informado”*

*\(O log deve exibir a identificação do registro com erro, no mesmo padrão do log de erros do Sped Fiscal\) *

COD\_MUN

A informação deste campo é gerada com a concatenação do Código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do Município do estabelecimento:

                      “UUMMMMM” \(onde “UU” é o código da UF, e “MMMMM” o código do município\)

Para obter o código da UF, acessar a tabela dos municípios do IBGE \(MUNICÍPIO\) a partir da sigla da UF \+ o código do município informados no cadastro do estabelecimento\.

Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

*\(Observar que no layout o tamanho desse campo é = 007\*, o que significa que as sete posições devem ser obrigatoriamente preenchidas, sendo 2 para o código da UF, e 5 para o código do município\)*

Quando o município do estabelecimento não estiver preenchido, será gerada a seguinte mensagem de crítica no log: 

*                                          “O campo COD\_MUN é de preenchimento obrigatório, e não foi informado”*

*\(O log deve exibir a identificação do registro com erro, no mesmo padrão do log de erros do Sped Fiscal\) *

IM

Inscrição municipal do estabelecimento informado em tela \(cadastro do estabelecimento, campo “Insc\. Municipal”\)\.

SUFRAMA

Inscrição na Suframa do estabelecimento informado em tela \(cadastro do estabelecimento, campo “Insc\. SUFRAMA”\)\.

IND\_PERFIL

Perfil do estabelecimento que consta nos dados iniciais \(menu Parâmetros > Dados Iniciais, campo “Perfil da EFD”\)\. 

IND\_ATIV

Este campo é gerado a partir do campo “Tipo de Atividade” do cadastro do Estabelecimento, da seguinte forma:

Se campo “Tipo de Atividade” \(IND\_ATIVIDADE\) = “0” \(Industrial ou equiparado a Industrial\),

      O campo será gerado com “0”;

Senão,

      O campo será gerado com “1”;

Quando o tipo de atividade não estiver preenchido, será gerada a seguinte mensagem de crítica no log: 

*                                     “O campo IND\_ATIV é de preenchimento obrigatório, e não foi informado”*

*\(O log deve exibir a identificação do registro com erro, no mesmo padrão do log de erros do Sped Fiscal\) *

# <a id="_Toc181177406"></a><a id="OLE_LINK30"></a>Registro 0001 – Abertura do Bloco 0

REG

Conteúdo fixo = “__0001__”

IND\_MOV

<a id="OLE_LINK35"></a><a id="OLE_LINK36"></a>Este campo é preenchido sempre com “0”, pois os registros do Bloco 0 sempre conterão dados\.

__\[MFS581026\] __Inclusão do Registro 0004

# <a id="_Toc181177407"></a>Registro 0004 – Identificação do Estabelecimento Incorporador

Registro único no arquivo, gerado a partir das informações de cadastro da Relação de Empresa Incorporadora x Incorporada 

\(Módulo Parâmetros, item Preliminares 🡪 Relação de Empresa Incorporadora x Incorporada\)

REG

Conteúdo fixo = “__0004__”

CNPJ

CNPJ do estabelecimento cadastrado como Incorporador para a empresa e estabelecimento da geração, cadastrados como incorporados\.

Recuperar o CNPJ do cadastro do Estabelecimento referente ao estabelecimento incorporador\.

# <a id="_Toc181177408"></a>Registro 0005 – Dados Complementares da Entidade

Registro único no arquivo, gerado a partir das informações de cadastro do estabelecimento\.

REG

Conteúdo fixo = “__0005__”

FANTASIA

Nome fantasia do estabelecimento \(NOME\_FANTASIA\)

CEP

CEP do estabelecimento \(cadastro do estabelecimento\)

Quando o CEP não estiver preenchido, será gerada a seguinte mensagem de crítica no log: 

*                                     “O campo CEP é de preenchimento obrigatório, e não foi informado”*

*\(O log deve exibir a identificação do registro com erro, no mesmo padrão do log de erros do Sped Fiscal\) *

END

Concatenação dos campos “Tipo Logradouro” e “Endereço” do cadastro do estabelecimento \(TP\_LOGRADOURO e ENDERECO\), separados por um caracter branco \(ex: XXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\)

Quando o endereço não estiver preenchido, será gerada a seguinte mensagem de crítica no log: 

*                                     “O campo END é de preenchimento obrigatório, e não foi informado”*

*\(O log deve exibir a identificação do registro com erro, no mesmo padrão do log de erros do Sped Fiscal\) *

NUM

Número do endereço do cadastro do estabelecimento \(NUM\_ENDERECO\)

COMPL

Este campo é gerado dependendo do conteúdo do campo “Complemento Endereço” do cadastro do estabelecimento \(quadro “Informações para geração as obrigações fiscais”\):

Se campo “Complemento Endereço” <> nulo

      O campo será gerado com o conteúdo do campo “Complemento Endereço” \(COMPL\_ENDERECO\_EFD\);

Senão, 

      O campo será gerado com o conteúdo do campo “Complemento” \(COMPL\_ENDERECO\);

BAIRRO

Este campo é gerado dependendo do conteúdo do campo “Bairro” do quadro “Informações para geração as obrigações fiscais” do cadastro do estabelecimento \(quadro “Informações para geração as obrigações fiscais”\):

Se campo “Bairro” do quadro “Informações para geração as obrigações fiscais” <> nulo

      O campo será gerado com o conteúdo do campo “Bairro” deste quadro \(BAIRRO\_COMPL\);

Senão, 

      O campo será gerado com o conteúdo do campo “Bairro” \(BAIRRO\);

Quando não existir a informação do bairro \(em nenhum dos dois campos\), será gerada a seguinte mensagem de crítica no log: 

*                                     “O campo BAIRRO é de preenchimento obrigatório, e não foi informado”*

*\(O log deve exibir a identificação do registro com erro, no mesmo padrão do log de erros do Sped Fiscal\) *

FONE

Concatenação dos campos DDD e Telefone do cadastro do estabelecimento \(DDD e TELEFONE\)

FAX

FAX do estabelecimento \(cadastro do estabelecimento\)

EMAIL

E\-mail do estabelecimento \(cadastro do estabelecimento\)

# <a id="_Toc181177409"></a>Registro 0100 – Dados do Contabilista

Registro único no arquivo, gerado a partir das informações do contabilista responsável parametrizado no menu “Dados Iniciais”\. O cadastro destes responsáveis é feito no módulo Parâmetros, menu “Requisitos Legais > Responsáveis por Informações” \(tabelas __RESP\_INFORMACAO__ e __RESP\_CONTADOR__\)\.

REG

Conteúdo fixo = “__0100__”

NOME

Nome do responsável \(campo Nome/Razão Social\)

CPF

Este campo é preenchido com o conteúdo do campo “CPF/CNPJ” da tabela dos Responsáveis por Informação \(NUM\_CPF\)\.

*OBS: Na verdade a coluna NUM\_CPF da tabela RESP\_INFORMACAO contém sempre o CPF, e nunca o CNPJ, pois tem apenas 11 posições\. Quando o responsável é da categoria “Empresa”, e portanto, tem um CNPJ, esta informação fica apenas na tabela dos responsáveis contadores \(RESP\_CONTADOR\)\.*

CRC

CRC do responsável\. Esta informação é recuperada da tabela dos responsáveis contadores \(RESP\_CONTADOR, campo NUM\_CRC\), a partir do código do responsável\.

Quando o CRC não estiver preenchido, será gerada a seguinte mensagem de crítica no log: 

*                                          “O campo CRC é de preenchimento obrigatório, e não foi informado”*

*\(O log deve exibir a identificação do registro com erro, no mesmo padrão do log de erros do Sped Fiscal\) *

CNPJ

Este campo é preenchido apenas quando a categoria do responsável for = “Empresa” \(campo “Categoria” do cadastro do responsável\):

Se campo “Categoria” = “Empresa”

     O campo será gerado com o CNPJ da empresa\. Esta informação é recuperada da tabela dos responsáveis contadores 

     \(RESP\_CONTADOR, campo NUM\_CPF __\(\*\)__ \), a partir do código do responsável\.

__\(\*\)__ Apesar do nome do campo NUM\_CPF da RESP\_CONTADOR, o seu conteúdo pode conter tanto um CFP como um CNPJ, dependendo da categoria do responsável\.

CEP

CEP do responsável \(NUM\_CEP da RESP\_INFORMACAO\)

END

Concatenação dos campos “Tipo Logradouro” e “Endereço” do cadastro do responsável \(TP\_LOGRADOURO e DSC\_ENDERECO da RESP\_INFORMACAO\), separados por um caracter branco \(ex: XXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\)

NUM

Número do endereço do responsável \(NUM\_ENDERECO da RESP\_INFORMACAO\)

COMPL

Complemento do endereço do responsável \(COMPL\_ENDERECO da RESP\_INFORMACAO\)

BAIRRO

Bairro do responsável \(DSC\_BAIRRO da RESP\_INFORMACAO\)

FONE

Concatenação dos campos DDD e Telefone do responsável \(NUM\_DDD e NUM\_TELEFONE da RESP\_INFORMACAO\)

FAX

FAX do responsável \(NUM\_FAX da RESP\_INFORMACAO\)

EMAIL

E\-mail do responsável \(E\_MAIL da RESP\_INFORMACAO\)

Quando o e\-mail não estiver preenchido, será gerada a seguinte mensagem de crítica no log: 

*                                           “O campo EMAIL é de preenchimento obrigatório, e não foi informado”*

*\(O log deve exibir a identificação do registro com erro, no mesmo padrão do log de erros do Sped Fiscal\)*

COD\_MUN

A informação deste campo é gerada com a concatenação do Código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do Município do responsável \(COD\_MUNICIPIO da RESP\_INFORMACAO\):

                              “UUMMMMM” \(onde “UU” é o código da UF, e “MMMMM” o código do município\)

Para obter o código da UF, acessar a tabela dos municípios do IBGE \(MUNICÍPIO\) a partir da sigla da UF \+ o código do município informados no cadastro do responsável\.

Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

*\(Observar que no layout o tamanho desse campo é = 007\*, o que significa que as sete posições devem ser obrigatoriamente preenchidas, sendo 2 para o código da UF, e 5 para o código do município\)*

Quando o município não estiver preenchido, será gerada a seguinte mensagem de crítica no log: 

*                                           “O campo COD\_MUN é de preenchimento obrigatório, e não foi informado”*

*\(O log deve exibir a identificação do registro com erro, no mesmo padrão do log de erros do Sped Fiscal\)*

# <a id="_Toc181177410"></a>Registro 0150 – Identificação do Participante

__MFS46838: Tratamento do Perfil D:__

Registro gerado a partir das informações do cadastro dos estabelecimentos centralizados, que estão parametrizados na “Centralização de Estabelecimentos p/ Perfil D” relacionados ao estabelecimento centralizador, informado na tela de geração\. Devem ser demonstrados apenas estabelecimentos centralizados movimentados o período\.

Importante: 

- Este registro deve ser gerado apenas quando o __Perfil for D__\. Ver o campo Perfil do estabelecimento informado na tela de geração, na Parametrização dos dados iniciais \(menu Parâmetros > Dados Iniciais, campo “Perfil da EFD”\)\.
- O estabelecimento centralizador não pode ser informado no registro 0150\. Observe que a parametrização da “Centralização de Estabelecimentos p/ Perfil D” sempre grava o estabelecimento centralizador fazendo parte da lista de estabelecimentos centralizados\.
- Gravar um registro 0150 por Estabelecimento

Procedimentos para Geração:

Quando o Estabelecimento informado na tela de geração tiver o Perfil igual a __“D”__, realizar os procedimentos a seguir:

Recuperar os __estabelecimentos centralizados__ relacionados ao estabelecimento centralizador informado para tela de geração do meio magnético\. Ver Parâmetros 🡪 Centralização de Estabelecimentos p/ Perfil D\. Não recuperar o estabelecimento centralizador\!

Gerar um registro __0150__ para cada estabelecimento centralizado que possuir movimento de entrada ou saída \(Tabela dos Movimentos e Tabela dos Movimentos – ECF\)\. 

Veja os detalhes da recuperação nas tabelas de movimento a seguir:

1. __Origem dos dados__: Tabela dos Movimentos \(__EST\_ST\_SC\_NF__\)

<a id="OLE_LINK75"></a>Esta tabela é gerada nas etapas preliminares, nos menus “*Geração > Geração dos Movimentos > Saídas*” e “*Geração > Geração dos Movimentos > Entradas*”\. 

__Critérios da recuperação dos dados__:

    \- Empresa à código da Empresa;

    \- Estabelecimento à código do Estabelecimento informado na tela de geração;

    \- Estabelecimento Origem diferente do Estabelecimento informado na tela de geração;

    \- Período à período informado em tela para geração do arquivo;

    \- Indicador do Tipo de Registro à = “__2113__” \(apenas os movimentos de saída ou devolução de saída a serem gravados no registro 2113\);

      Ou

     Indicador do Tipo de Registro à = “__2130__” \(apenas os movimentos de entrada ou devolução de entrada a serem gravados no registro 2130\);

Recuperar os distintos Códigos de Estabelecimento Origem\.

1. __Origem dos dados__: Tabela dos Totais de ECF \(__EST\_ST\_SC\_ECF__\)

Esta tabela é gerada numa etapa preliminar, no menu “*Geração > Geração dos Movimentos > Saídas \- ECF*”\. 

__Critérios da recuperação dos dados__:

    \- Empresa à código da Empresa;

    \- Estabelecimento à código do Estabelecimento informado na tela de geração;

    \- Estabelecimento Origem diferente do Estabelecimento informado na tela de geração; 

    \- Período à período informado em tela para geração do arquivo; 

Recuperar os distintos Códigos de Estabelecimento Origem\.

Gravar um registro __0150__ para cada Estabelecimento Origem recuperado nas consultas “a” e “b”\.

REG

Conteúdo fixo = “__0150__”

COD\_PART

Preencher com o código do estabelecimento Origem \(Centralizado\) recuperado nas consultas “a”, “b”\.

NOME

Preencher com a Razão Social do estabelecimento origem \(Centralizado\)\.

COD\_PAIS

Campo COD\_PAIS

Como a tabela de estabelecimento não possui o campo País, vamos considerar que os estabelecimentos estão localizados no Brasil, gravando o COD\_PAIS fixo com “__01058__”

O código do país é obtido da tabela de países \(TACES05, tabela PAIS\) e montado concatenando as três posições do código com o dígito verificador na tabela PAIS\. Para completar o tamanho de cinco posições do registro 0150, deve\-se preencher mais um zero à esquerda, da seguinte forma:  \[0CCCD\]

CCC – código do país

D – dígito verificador

CNPJ

Preencher com o CNPJ \(CGC\) do estabelecimento origem \(Centralizado\)\.

CPF

Este campo é gerado sem informação \(‘||’\)

IE

Inscrição estadual do estabelecimento origem \(Centralizado\) no estado de __SC__\.

Campo “*Inscrição Estadual*” da Tabela de Cadastro das Inscrições Estaduais \(tabela REGISTRO\_ESTADUAL\), no módulo Parâmetros, item Preliminares > Inscrições Estaduais\. 

Quando a inscrição estadual não for identificada, será gerada a seguinte mensagem de crítica no log: 

*                                               “O campo IE é de preenchimento obrigatório, e não foi informado”*

*\(O log deve exibir a identificação do registro com erro, no mesmo padrão do log de erros do Sped Fiscal\) *

COD\_MUN

A informação deste campo é gerada com a concatenação do Código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do Município do estabelecimento origem \(Centralizado\):

                      “UUMMMMM” \(onde “UU” é o código da UF, e “MMMMM” o código do município\)

Para obter o código da UF, acessar a tabela dos municípios do IBGE \(MUNICÍPIO\) a partir da sigla da UF \+ o código do município informados no cadastro do estabelecimento\.

Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

*\(Observar que no layout o tamanho desse campo é = 007\*, o que significa que as sete posições devem ser obrigatoriamente preenchidas, sendo 2 para o código da UF, e 5 para o código do município\)*

Quando o município do estabelecimento não estiver preenchido, será gerada a seguinte mensagem de crítica no log: 

*                                          “O campo COD\_MUN é de preenchimento obrigatório, e não foi informado”*

*\(O log deve exibir a identificação do registro com erro, no mesmo padrão do log de erros do Sped Fiscal\) *

SUFRAMA

Inscrição na Suframa do estabelecimento origem \(Centralizado\) \(cadastro do estabelecimento, campo “Insc\. SUFRAMA”\)\.

END

Concatenação dos campos “Tipo Logradouro” e “Endereço” do cadastro do estabelecimento \(TP\_LOGRADOURO e ENDERECO\), separados por um caracter branco \(ex: XXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\)

Quando o endereço não estiver preenchido, será gerada a seguinte mensagem de crítica no log: 

*                                     “O campo END é de preenchimento obrigatório, e não foi informado”*

*\(O log deve exibir a identificação do registro com erro, no mesmo padrão do log de erros do Sped Fiscal\) *

NUM

Número do endereço do cadastro do estabelecimento \(NUM\_ENDERECO\)

COMPL

Este campo é gerado dependendo do conteúdo do campo “Complemento Endereço” do cadastro do estabelecimento \(quadro “Informações para geração as obrigações fiscais”\):

Se campo “Complemento Endereço” <> nulo

      O campo será gerado com o conteúdo do campo “Complemento Endereço” \(COMPL\_ENDERECO\_EFD\);

Senão, 

      O campo será gerado com o conteúdo do campo “Complemento” \(COMPL\_ENDERECO\);

BAIRRO

Este campo é gerado dependendo do conteúdo do campo “Bairro” do quadro “Informações para geração as obrigações fiscais” do cadastro do estabelecimento \(quadro “Informações para geração as obrigações fiscais”\):

Se campo “Bairro” do quadro “Informações para geração as obrigações fiscais” <> nulo

      O campo será gerado com o conteúdo do campo “Bairro” deste quadro \(BAIRRO\_COMPL\);

Senão, 

      O campo será gerado com o conteúdo do campo “Bairro” \(BAIRRO\);

Quando não existir a informação do bairro \(em nenhum dos dois campos\), será gerada a seguinte mensagem de crítica no log: 

*                                     “O campo BAIRRO é de preenchimento obrigatório, e não foi informado”*

*\(O log deve exibir a identificação do registro com erro, no mesmo padrão do log de erros do Sped Fiscal\) *

# <a id="_Toc181177411"></a>Registro 0190 – Identificação das Unidades de Medida

O registro 0190 é gerado a partir da movimentação do período\. Desta forma, todas as unidades de medida referenciadas no arquivo \(registros 0200, 2112, 2113 e 2130\) terão seus dados de cadastro gravados no registro 0190\.

<a id="OLE_LINK27"></a>*\(Para cada unidade de medida será gravado apenas um registro 0190, independente da quantidade de movimentos\)*

REG

Conteúdo fixo = “__0190__”

UNID

Código da unidade de medida \(campo 01 da SAFX2007\) 

DESCR

Descrição da unidade de medida \(campo 03 da SAFX2007\)

*Obs\.: Todos os campos de unidade de medida do arquivo \(registros 0190, 0200, 0220, 2112, 2113 e 2130\) são gerados com a unidade da SAFX2007\. Isso porque utilizamos as tabelas de conversão de medida do DW, que utilizam este campo\. Assim, para evitar problemas de inconsistência, trabalhamos sempre com este campo, ao invés de utilizar o campo da unidade de medida padrão\.*__* *__

# <a id="_Toc181177412"></a>Registro 0200 – Tabela de Identificação do Item

O registro 0200 é gerado a partir da movimentação do período\. Desta forma, todos os produtos referenciados nos registros de movimento \(2112, 2113 e 2130\) terão seus dados de cadastro gravados no registro 0200\.

*\(para cada produto será gravado apenas um registro 0200, independente da quantidade de movimentos\)*

As informações do produto são obtidas no cadastro \(SAFX2013\)\. Para recuperar o registro do produto na tabela será considerado o registro de maior data de validade, que seja < = a data final do período \(data do último dia do período informado em tela\)\.

Preenchimento dos campos:

REG

Conteúdo fixo = “__0200__”

COD\_ITEM

A geração deste campo depende da parametrização dos dados inicias do estabelecimento em questão \(menu “*Parâmetros🡪 Dados Iniciais”\)*, da seguinte forma:

Se parâmetro “*Considerar o indicador no código do produto*” marcado,

     O campo será gerado com a concatenação do indicador \+ código do produto, no formato: X\-XXXXXXXXXXXXXX;

Senão

      O campo será gerado apenas com o código do produto;

DESCR\_ITEM

A geração deste campo depende da parametrização dos dados inicias do estabelecimento em questão \(menu “*Parâmetros🡪 Dados Iniciais”\)*, da seguinte forma:

Se parâmetro “*Utilizar a descrição detalhada do produto*” marcado,

     O campo será gerado com a descrição detalhada do produto \(campo “*22\-Descrição Detalhada*” da SAFX2013\)\. Caso o campo 

     da descrição detalhada não esteja preenchido, será utilizada a descrição do produto \(campo 04\);

Senão

      O campo será gerado com a descrição do produto \(campo “*04\-Descrição do Produto*” da SAFX2013\);

COD\_BARRA

Campo “40\-Código de Barras” da SAFX2013\.

COD\_ANT\_ITEM

Este campo é gerado sem informação \(‘||’\)

UNID\_INV

Campo “14\-Código de Medida” da SAFX2013\.

Todas as unidades registradas neste campo terão seus dados cadastrais gravados no registro “0190\-Identificação das Unidades de Medida”\.

*Obs\.: Todos os campos de unidade de medida do arquivo \(registros 0190, 0200, 0220, 2112, 2113 e 2130\) são gerados com a unidade da SAFX2007\. Isso porque utilizamos as tabelas de conversão de medida do DW, que utilizam este campo\. Assim, para evitar problemas de inconsistência, trabalhamos sempre com este campo, ao invés de utilizar o campo da unidade de medida padrão\.*

TIPO\_ITEM

Campo “39\-Classificação do Item \(Sped Fiscal\)” da SAFX2013\.

Quando a classificação do item não estiver preenchida, será gerada a seguinte mensagem de crítica no log: 

*                                         “O campo TIPOI\_ITEM é de preenchimento obrigatório, e não foi informado”*

*\(O log deve exibir a identificação do registro com erro e a identificação do produto, no mesmo padrão do Sped Fiscal\)*

COD\_NCM

Campo “05\-Código NBM” da SAFX2013 \(*considerando apenas as 8 primeiras posições*\)\.

Quando este campo não estiver preenchido no produto, o campo será gravado sem informação\.

Obs\.: Lembrando que os NCM’s são carregados para o campo 05\-COD\_NBM da tabela de produtos, pois o DW trabalha com a SAFX2043, que contém na verdade os NCM’s\.

EX\_IPI

Este campo é preenchido com os dois últimos dígitos do NCM do produto \(posições 9 e 10\)\. 

Quando o NCM do produto não estiver preenchido, ou, quando estas posições estiverem com brancos, o campo EX\_IPI não será preenchido, pois o NCM não tem exceção;

Obs\.: Esta informação é o código de exceção do NCM, que no DW é carregado para os dois últimos dígitos do NCM, conforme a tabela básica SAFX2043\.

COD\_GEN

Este campo é preenchido com os dois primeiros dígitos do NCM do produto \(posições 1 e 2\)\.

Quando o NCM do produto não estiver preenchido, o campo COD\_GEN não será preenchido\.

COD\_LST

Este campo é gerado sem informação \(‘||’\) *\(uma vez que a obrigação não considera os serviços da SAFX09\)*\.

ALIQ\_ICMS

Neste campo será informada a alíquota interna que consta na parametrização do produto, considerando a redução da base quando for o caso\.

Trata\-se das parametrizações do menu “*Parâmetros 🡪 Produtos 🡪 Por Código*” __ou__ “*Por NCM*” __ou__ “*Por CEST*”\. Lembrando que a prioridade ao buscar um produto na parametrização é, primeiro verificar pelo código, depois pelo NCM, e por último pelo CEST\.

A alíquota a ser utilizada no preenchimento deste campo segue a regra abaixo:

__Se__ *não* existir redução de base de cálculo \(campo “*% de Redução da BC*” nulo ou = 0\)

      Neste caso o campo será preenchido com a alíquota interna da parametrização \(campo “*Alíquota Interna*”\)

__Senão__ \(campo “*% de Redução da BC*” preenchido com valor > 0\)

      Neste caso será informado a alíquota interna já com o valor reduzido:

   

                  \[ Alíquota Interna – \(Alíquota Interna \* “% de Redução da BC” / 100 \) \]

Exemplo:

Alíquota interna = 18, 

% Redução da BC = 30

Valor a ser informado: \[ 18 – \(18 \* 30/100\) \] = \[ 18 – \(18 \* 0,3\) \] = \[ 18 – 5,4 \] = __12,60__

CEST	

Campo “54\- Código Especificador da Substituição Tributária” da SAFX2013\.

Este campo será preenchido apenas para os períodos a partir de Jan/2017\. Para períodos anteriores, será gerado sem informação \(‘||’\)\.

#  <a id="_Toc181177413"></a>Registro 0205 – Código Anterior do Item

Este é um registro “filho” do 0200, que informa alterações no código ou na descrição do produto\.

*Obs\.: Havendo alterações nos dois casos, código e descrição \(Situação 1 e Situação 2 descritas abaixo\), serão gerados dois registros 0205, pois para cada 0205 é apresentada apenas um tipo de alteração, ou o código, ou a descrição\. Um único registro 0205 nunca é utilizado para demonstrar os dois tipos de alteração\.*

<a id="OLE_LINK1"></a>O registro 0205 será gerado nas seguintes situações:

__Situação 1 – Alteração do Código:__

Quando o código do campo “*Código Anterior Utilizado pelo Produto*” estiver preenchido na SAFX2013, considerando o registro da SAFX2013 utilizado para gerar o registro 0200, e a data da alteração \(campo “*Data Alteração de Código*”\) for uma data enquadrada no período da geração\. Neste caso, será gerado um registro 0205 da seguinte forma:

REG

Conteúdo fixo = “__0205__”

DESCR\_ANT\_ITEM

Sem informação \(‘||’\)

DT\_INI

Neste campo deve ser informada a *menor data de validade* existente na SAFX2013 para o indicador e código anteriores do produto \(quadro “Código Anterior Utilizado pelo Produto”\),  

\(a ideia é informar a data em que o código anterior começou a ser utilizado\) 

DT\_FIM

Neste campo será informada a data do dia imediatamente anterior à data da alteração do código \(campo “*Data Alteração de Código*”\)\.

COD\_ANT\_ITEM

Este campo será gerado com o código anterior do produto informado na SAFX2013, considerando a parametrização dos dados inicias do estabelecimento \(menu “*Parâmetros🡪 Dados Iniciais”\)*, da seguinte forma:

Se parâmetro “*Considerar o indicador no código do produto*” marcado,

     O conteúdo será a concatenação dos campos indicador \+ código \(campos de quadro “Código Anterior Utilizado pelo Produto”\)

     Formato: “X\-XXXXXXXXXXXXXX”;

Senão

      O conteúdo será apenas o campo código do quadro “Código Anterior Utilizado pelo Produto”;

    Exemplo:

__      Validade__

__  Indicador__

__     Código__

__          Código Anterior Utilizado pelo Produto__

__Indicador__

__     Código__

__    Data Alteração__

01/01/2012

1

X001

01/01/2014

1

X001

01/01/2017

1

X001

15/01/2018

1

__T001__

1

X001

15/01/2018

No exemplo temos o produto X001 que mudou de código em 15/01/2018, passando a ter o código T001\. 

Supondo um geração para JAN/2018, ao gerar no arquivo uma nota fiscal com o código de produto = T001, seria feita a geração do registro 0200 para o produto T001, e consequentemente do registro “filho” 0206, uma vez que consta informação no campo “Código Anterior Utilizado pelo Produto”\. Neste caso, o 0205 seria gerado com as seguintes informações:

   DT\_INI = 01/01/2012                 = menor data de validade existente p/o produto 1\-X001

   DT\_FIM = 14/01/2018               = dia anterior à data da alteração do código \(15/01/2018\)

   COD\_ANT\_ITEM = 1\-X001       = Código anterior do produto informado na SAFX2013

__Situação 2 – Alteração da Descrição:__

Quando a descrição do produto apresentada no registro 0200 for diferente da apresentada na EFD \(Sped Fiscal\) do período anterior, será gerado um registro 0205 demonstrando a descrição anterior do produto\.

Lembrando que, o registro 0200 é gerado com base no registro da SAFX2013 de maior data de validade que seja <= a data final do período da geração\. 

Assim, será feita a comparação entre os registros da SAFX2013 utilizados para o registro 0200 da geração atual, e da geração do período anterior\. Ou seja, a comparação será entre:

               Registro da SAFX2013 com a maior data de validade que seja <= a data final do período *anterior* ao período da geração atual

                                                                                                       __X__

                               Registro da SAFX2013 com a maior data de validade que seja <= a data final do período da geração atual

Se o registro for o mesmo, significa que não houve alteração na descrição\.

Se os registros forem diferentes, será checado se houve mudança na descrição, conforme o seguinte parâmetro dos dados iniciais:

<a id="OLE_LINK10"></a>Se parâmetro “*Utilizar a Descrição Detalhada do Produto*” não marcado:

<a id="OLE_LINK2"></a>      A comparação da descrição dos dois registros será feita a partir do campo “Descrição” \(campo 4 da SAFX2013\);

Se parâmetro <a id="OLE_LINK7"></a>“*Utilizar a Descrição Detalhada do Produto*” marcado:

      A comparação da descrição dos dois registros será feita a partir do campo “Descrição Detalhada” \(campo 22 da SAFX2013\)\.

      Se a descrição detalhada \(campo 22\) estiver nula em um dos registros, ou nos dois, será utilizado o campo da descrição “normal” \(campo 4 da SAFX2013\)\.

      Nesse caso, a descrição “normal” será utilizada apenas no registro que não tiver informação na descrição detalhada;

Se for identificada alteração na descrição, será gerado um registro __0205__ com as seguintes informações:

REG

Conteúdo fixo = “__0205__”

DESCR\_ANT\_ITEM

Descrição anterior do produto, conforme a comparação descrita acima que identificou diferença entre a informação gerada na EFD do período anterior e do período atual\. 

Ou seja, será a descrição do registro utilizado na comparação das descrições, conforme descrito acima\. 

Lembrando que o campo utilizado depende do parâmetro “*Utilizar a Descrição Detalhada do Produto*” \(Dados Iniciais\):

Se parâmetro “*Utilizar a Descrição Detalhada do Produto*” não marcado:

      Campo “Descrição” \(campo 4 da SAFX2013\);

Se parâmetro “*Utilizar a Descrição Detalhada do Produto*” marcado:

      Campo “Descrição Detalhada” \(campo 22 da SAFX2013\)\.

      Se este campo estiver nulo, é utilizada a informação do campo “Descrição“\(campo 4 da SAFX2013\);

DT\_INI

Neste campo será informada a data de validade do registro da SAFX2013 que foi utilizado  na geração do registro 0200 da EFD \(Sped Fiscal\) do período anterior \(ou seja, a data de validade do registro<a id="OLE_LINK6"></a> utilizado na comparação das descrições, conforme descrito acima\)\.

 

 DT\_FIM

Neste campo será informada a data do dia imediatamente anterior à data de validade do registro da SAFX2013 que foi utilizado na geração do registro 0200 \(ou seja, a data de validade do registro que foi utilizado na comparação das descrições, conforme descrito acima\)\.

COD\_ANT\_ITEM

Sem informação \(‘||’\)

    Exemplo:

Exemplo:

Validade

Indicador 

Código

Descrição

Descrição Detalhada

01/01/2012

1

X001

<a id="OLE_LINK4"></a><a id="OLE_LINK5"></a>Mesa Redonda Marfim

<a id="OLE_LINK8"></a><a id="OLE_LINK9"></a>Mesa Redonda Marfim – Modelo X001

01/01/2014

1

X001

Mesa Redonda Marfim

Mesa Redonda Marfim – Modelo X001

01/03/2017

1

X001

Mesa Modelo X001

Mesa Redonda Marfim – Modelo X001

15/01/2018

1

X001

Mesa Modelo X001

<a id="OLE_LINK23"></a><a id="OLE_LINK24"></a><a id="OLE_LINK25"></a>Mesa Redonda Marfim – Modelo X001 – Refer: MRMX001

<a id="OLE_LINK12"></a><a id="OLE_LINK11"></a>Resultado com o parâmetro “Utilizar descrição detalhada do produto” = “N”

<a id="OLE_LINK22"></a>No exemplo temos o produto X001 que mudou a descrição em 01/03/2017, passando a ter a descrição <a id="OLE_LINK14"></a><a id="OLE_LINK13"></a>“Mesa Modelo X001”\. Supondo a geração para __Março/2017__, ao gerar no arquivo uma nota fiscal do produto X001, seria feita a geração do registro 0200 com a descrição “Mesa Modelo X001”, <a id="OLE_LINK16"></a><a id="OLE_LINK15"></a>por se tratar do registro da SAFX2013 de maior data de validade <= 31/03/2017\. 

Como o registro 0200 da EFD do período anterior \(Fev/2017\) foi gerado com a descrição “Mesa Redonda Marfim” \(por se tratar do registro da SAFX2013 de maior data de validade <= 28/02/2017\), houve alteração na descrição\. Neste caso, seria gerado um registro 0205 com as seguintes informações:

   DT\_INI = 01/01/2014  = data da validade do registro da SAFX2013 utilizado na geração do 

                                         0200 p/o período anterior \(Fev/2017\)

   DT\_FIM = 28/02/2017 = dia anterior à data de validade do registro da SAFX2013 utilizado na 

                                          geração do 0200 p/o período atual \(Março/2017\)

   DESCR\_ANT\_ITEM = Mesa Redonda Marfim

Resultado com o parâmetro “Utilizar descrição detalhada do produto” = “S”

No exemplo temos o produto X001 que mudou a descrição *detalhada* em 15/01/2018, passando a ter a descrição “Mesa Redonda Marfim – Modelo X001 – Refer: MRMX001”\. Supondo a geração para __Janeiro/2018__, ao gerar no arquivo uma nota fiscal do produto X001, seria feita a geração do registro 0200 com a descrição “Mesa Redonda Marfim – Modelo X001 – Refer: MRMX001”, por se tratar do registro da SAFX2013 de maior data de validade <= 31/01/2018\. 

Como o registro 0200 da EFD do período anterior \(Dez/2017\) foi gerado com a descrição “Mesa Redonda Marfim – Modelo X001” \(por se tratar do registro da SAFX2013 de maior data de validade <= 31/12/2017\), houve alteração na descrição\. Neste caso, seria gerado um registro 0205 com as seguintes informações:

   DT\_INI = 01/03/2017  = data da validade do registro da SAFX2013 utilizado na geração do 

                                         0200 p/o período anterior \(Dez/2017\)

   DT\_FIM = 14/01/2018 = dia anterior à data de validade do registro da SAFX2013 utilizado na 

                                          geração do 0200 p/o período atual \(Jan/2018\)

   DESCR\_ANT\_ITEM = Mesa Redonda Marfim – Modelo X001

__Situação 3__:

Esta situação é sobre o caso dos produtos que ficam sem ter movimentação em alguns períodos, e por isso, não são referenciados no arquivo\. Nesse caso, deve\-se verificar a alteração no código ou na descrição do produto ocorrida para todos os períodos sem movimentação\. A lógica é a mesma descrita acima, mas, considerando como mês de referência não apenas o período atual da geração, como também todos os períodos anteriores que não tiveram movimentação\.

__Isso significa que todos os registros 0205 que deveriam ser gerados nos períodos anteriores, mas não foram \(pois o produto não foi registrado no arquivo\), serão gerados no primeiro período em que o produto voltar a ser exibido no arquivo \(voltar a ter movimentação\)\.__

No caso desta geração do Ressarcimento de SC, a existência ou não de movimentação do produto deve ser verificada na tabela correspondente ao registro __2110__, que representa o resultado do ressarcimento/complemento de ST do produto a cada período\. Sempre que o produto não existir nesta tabela para o período anterior ao da geração, significa que ele não foi para o arquivo\. Assim, deve\-se verificar a sequencia de períodos anteriores sem movimentação, e aplicar a lógica de geração do __0205__ para todos estes períodos até o atual\. 

Obs\.: A geração do 0205 na EFD \(Sped Fiscal\) tem este mesmo procedimento, sendo que a verificação é feita nas tabelas de movimentos utilizadas na geração dos diversos Blocos \(SAFX07, SAFX08, SAFX52, etc \.\.\.\)\. 

# <a id="_Toc181177414"></a><a id="OLE_LINK26"></a>Registro 0206 – Código do Produto conforme Tabela ANP

Este é um registro “filho” do 0200, que informa o código do produto de acordo com a Tabela de Combustíveis da ANP \(Agência Nacional de Petróleo, [www\.anp\.gov\.br](http://www.anp.gov.br), opção SIMP, Tabelas de Códigos\)\.

O registro 0206 é gerado *apenas* nas seguintes condições:

     \- Quando o Estabelecimento em questão for um produtor, importador, distribuidor ou posto de combustível;

     \- Quando o código ANP do produto estiver preenchido \(campo “41\-Código ANP” da SAFX2013\), o que identifica tratar\-se de combustível;

A verificação se o estabelecimento é produtor, importador, distribuidor ou posto de combustível, é feita da seguinte forma:

\- Identifica a pessoa fis/jur associada ao estabelecimento, conforme a parametrização do módulo DW, \(*menu “Manutenção 🡪 Cadastros 🡪 Estabelecimentos X Pessoas Fisicas/Jurídicas”*\);

\- Identifica o ramo de atividade da pessoa fis/jur associada ao estabelecimento, conforme a parametrização dos ramos de atividade do módulo DW *\(menu “Manutenção 🡪 Cadastro Parâmetros 🡪 Pessoa Fis/Jur por Ramo de Atividade\)\. *O ramo de atividade \(campo “Classificação da Atividade”\) deve ser uma das seguintes \(campo “Classificação da Atividade”\):

94\-Refinaria

\(Produtor\)

95\-Formulador               

\(Produtor\)

96\-CPQ                          

\(Produtor\)

97\-Importador

104\-Distribuidor

105\-Posto Varejista         

\(Posto de Combustíveis\)

107\-Usina                        

\(Produtor\)

Concluindo, sempre que o código ANP do produto estiver preenchido, e o estabelecimento for um produtor, importador, distribuidor ou posto de combustível \(conforme a regra acima\), será gerado um registro 0206 para este produto\.

 

REG

Conteúdo fixo = “__0206__”

COD\_COMB

Código ANP do produto \(campo “41\-Código ANP” da SAFX2013\)

# <a id="_Toc181177415"></a><a id="OLE_LINK29"></a>Registro 0220 – Fatores de Conversão de Unidade

Este é um registro “filho” do 0200\. Seu objetivo é demonstrar todos os fatores de conversão utilizados nos movimentos <a id="OLE_LINK28"></a>__\(\*\)__, para converter a unidade do movimento na unidade do cadastro do produto \(unidade informada no registro 0200\)\.

__\(\*\)__ Os movimentos em que é feita a conversão de medida, quando necessário, são os movimentos de saída dos registros __2112__, __2113__, e as entradas do registro __2130__\.

Desta forma, cada produto gravado no registro 0200, poderá ter nenhum, ou vários registros 0220, o que dependerá das diferentes unidades utilizadas na comercialização do produto \(unidades identificadas nos movimentos\)\.

Quando um produto só tem movimentos com a mesma unidade do cadastro, não existirá nenhum registro “filho” 0220\.

Todos os registros de movimento \(2112, 2113 e 2130\) têm a informação da unidade do movimento \(campo UNID\) e o fator de conversão \(campo FAT\_CONV\)\. Quando o movimento tem a mesma unidade do cadastro do produto, este fator de conversão é gravado com 1\. __No registro 0220 são registradas apenas as situações em que houver conversão de medida__, ou seja, quando o campo FAT\_CONV do movimento é <> 1\.

Para cada produto, a combinação da unidade de medida do movimento \+ fator de conversão, deve ser gravada apenas uma vez no 0220, independente da quantidade de movimentos que utilizem esta mesma unidade\.

Preenchimento do registro 0220:

REG

Conteúdo fixo = “__0220__”

UNID\_CONV

Código da unidade de medida \(campo 01 da SAFX2007\) utilizada na comercialização do produto\.

<a id="OLE_LINK32"></a><a id="OLE_LINK33"></a><a id="OLE_LINK34"></a>Trata\-se do campo “UNID” dos registros de movimentos \(2112, 2113 e 2130\)\.

FAT\_CONV

Fator utilizado para converter a unidade do movimento \(campo UNID\_CONV\) na unidade de cadastro do produto\.

Trata\-se do campo “FAT\_CONV” dos registros de movimentos \(2112, 2113 e 2130\)\.

COD\_BARRA

\[__MFS76135\] Campo incluído pelo layout 1\.15 \(jan/2022\)\.__

- __Para Geração c/ leiaute anterior a EFD115 \(CAD\_LAYOUT – COD\_VERSAO<115\):__

Esse campo não deve ser gerado\.

- __Para Geração c/ leiaute a partir da EFD115 \(CAD\_LAYOUT – COD\_VERSAO>=115\):__

__Campo incluído a partir da versão de layout 1\.15 \(jan/2022\)__

Considerar o Código de Barra da tabela SAFX318 \- Cadastro de Códigos de Barras do Produto por Medida Comercializada\.

Tela de manutenção disponível no módulo BÁSICOS > DATAWAREHOUSE > Manutenção > Cadastros > Códigos de Barras do Produto por Medida Comercializada\.

 Para recuperar o Código de Barras, consultar a Tabela SAFX318 considerando os critérios:

\- Produto: produto presente no registro pai 0200;

\- Medida: unidade de medida comercializada presente no campo 02 – UNID\_CONV do registro 0220;

__\[MFS68852\] Tratamento do campo 137 – Quantidade Convertida da SAFX08__

Esta MFS alterou a geração dos movimentos de saída, saída ECF e entrada \(registros 2112, 2113 e 2130\), para calcular o fator de conversão através do campo 137 da SAFX08, quando este estiver preenchido, e não utilizar o fator cadastrado nas tabelas de Conversão de Medida por produto e padrão, cujas telas de manutenção estão localizadas no Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\)\.

Com isso, a geração do 0220 deve considerar as seguintes tabelas para encontrar a unidade do movimento \(campo UNID\) e o fator de conversão \(campo FAT\_CONV\):

\- DWT\_CONV\_MEDIDA \- Cadastros de Conversão de Medida por padrão

\- DWT\_CONV\_MEDIDA2 \- Cadastros de Conversão de Medida por produto

\- EST\_ST\_SC\_CONV\_MEDIDA \- Nova Tabela que armazena os Fatores de Conversão de Unidade de Medida calculados através do campo 137 da SAFX08\.

Obs: para evitar que a tabela EST\_ST\_SC\_CONV\_MEDIDA cresça ao longo do tempo de utilização do módulo, ao final da geração do registro 0220, vamos eliminar os registros de períodos anteriores ao da geração, considerando a empresa e estabelecimento informados na tela geração\.

\[__MFS78891\] Inclusão do Produto na tabela EST\_ST\_SC\_CONV\_MEDIDA:__

Alterou a tabela EST\_ST\_SC\_CONV\_MEDIDA, para armazenar o fator de conversão por o Produto, a medida origem \(item da nota\), a medida destino \(produto\)\.

# <a id="_Toc181177416"></a>Registro 0990 – Encerramento do Bloco 0

REG

Conteúdo fixo = “__0990__”

QTD\_LIN\_0

Quantidade total de linhas informadas no Bloco 0, incluindo os registros de abertura e fechamento do Bloco\.

= = = = = =

 

