# MTZ-Ressarc-SC-Geracao-do-Meio-Magnetico-BlocoH

- **Fonte:** MTZ-Ressarc-SC-Geracao-do-Meio-Magnetico-BlocoH.docx
- **Modificado:** 2021-09-27
- **Tamanho:** 78 KB

---

THOMSON REUTERS

Módulo Ressarcimento e Complemento ICMS\-ST – SC \(Portaria SEF 378/2018\)

Geração do Meio Magnético 

Bloco H

__Localização__: Menu Estadual, módulo Ressarcimento de ICMS\-ST – SC \(Port\.SEF 378/2018\), menu Geração 🡪 Geração do Meio Magnético

Este documento é específico das regras de geração do Bloco H\.

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

__MFS46838__

Tratamento do Perfil D

Alteração no registro H010\.

Inclusão do registro H011\.

21/09/2021

Sumário

[1\.	Regras Gerais do Bloco H	1](#_Toc83644705)

[2\.	Registro H001 – Abertura do Bloco H	1](#_Toc83644706)

[3\.	Registro H005 – Totais do Inventário	1](#_Toc83644707)

[4\.	Registro H010 – Inventário	1](#_Toc83644708)

[5\.	Registro H011 –  Identificação do Estabelecimento Detentor do Inventário	1](#_Toc83644709)

[6\.	Registro H990 – Encerramento do Bloco H	1](#_Toc83644710)

# <a id="_Toc83644705"></a>Regras Gerais do Bloco H

Os registros do Bloco H seguem o layout do Sped Fiscal, e são gerados a partir da Tabela do Inventário \(SAFX52\) para todos os produtos referenciados no arquivo \(registros 2112, 2113 e 2130\)\.

O registro H020 *não* deve ser gerado, conforme as orientações da Portaria SEF 378/2018\)

Diferente do Sped Fiscal, neste arquivo o inventário deve ser gerado todo mês, com a posição no último dia do mês\. Além disso, também serão geradas apenas as informações referentes ao indicador de propriedade “0” \(*Item de propriedade do informante e em seu poder*\), conforme orientação da Portaria SEF 378/2018:

Texto da Portaria 378:

*3\.3\. No REGISTRO H010 \- INVENTÁRIO, o preenchimento do Campo IND\_PROP \- Indicador de propriedade/posse do item: exigirá obrigatoriamente o indicador de propriedade e posse “0 \- Item de propriedade do informante e em seu poder”\. *

*\(Conforme interpretação deste item junto à Informação, deve ser informado apenas o IND\_PROP = “0”\)  *

# <a id="_Toc83644706"></a><a id="OLE_LINK30"></a>Registro H001 – Abertura do Bloco H

REG

Conteúdo fixo = “__H001__”

IND\_MOV

Este campo é preenchido sempre com “0”, pois os registros do Bloco H sempre conterão dados\.

# <a id="_Toc83644707"></a>Registro H005 – Totais do Inventário

Registro único no arquivo, com os totais do inventário\.

REG

Conteúdo fixo = “__H005__”

DT\_INV

Data do último dia do período da geração

VL\_INV

Resultado da totalização do campo __06\-VL\_ITEM__ de todos os registros __H010__\.

Quando não existir nenhum H010, será informado zero\. 

MOT\_INV

<a id="OLE_LINK39"></a>Este campo será gerado sempre com o conteúdo “05” \(Por solicitação da Fiscalização\), conforme orientação da Portaria SEF 378/2018\.

# <a id="_Toc83644708"></a>Registro H010 – Inventário

Registro “filho” do H005, que apresenta os valores do inventário de cada produto\. 

Lembrando que, conforme descrito na introdução do item “4\-Regras de Geração do Bloco H”, serão considerados apenas os dados de inventário dos produtos referenciados no arquivo \(registros 2112, 2113 e 2130\)\.

__Origem dos dados__: SAFX52

__Critérios de recuperação__:

    \- Empresa 🡪 código da Empresa;

    \- Estabelecimento 🡪 código do Estabelecimento selecionado para geração, observando o tratamento abaixo:

__    \[MFS46838\] Tratamento para Perfil D:__

__    __Caso o estabelecimento selecionado na tela de geração seja um estabelecimento __Centralizador__, recuperar os registros de inventário do estabelecimento __Centralizador__ e dos seus __    __

__    __estabelecimentos __Centralizados__, que foram a ele relacionados, na parametrização da “Centralização de Estabelecimentos p/ Perfil D”\.

__    __Caso o estabelecimento selecionado na tela de geração seja um estabelecimento “__Não centralizado”__, recuperar os registros de inventário apenas do estabelecimento selecionado para 

    geração\.

    \- Data do Inventário 🡪 data do último dia do período da geração; 

    \- Produto 🡪 indicador e código do Produto;

    \- Grupo de Contagem 🡪 será considerado apenas o grupo de contagem = “1” \(Estoque Próprio, em Poder do Estabelecimento\);

Obs\.: Conforme descrito na introdução do item “4\-Regras de Geração do Bloco H”, serão geradas apenas as informações referentes ao estoque próprio em poder do Estabelecimento, que corresponde ao indicador de propriedade \(campo IND\_PROP\) = “0” \(Item de propriedade do informante e em seu poder\)\.

__Grupamento__:

Os dados recuperados serão agrupados por:  

    \- Produto \(campos 6 e 7 da SAFX52\);

    \- Unidade de Medida \(campo 12<a id="_Hlk7010483"></a> da SAFX52\);

__Valores totalizados para cada grupamento__: 

    \- Quantidade \(campo 13 da SAFX52\);

    \- Custo Total \(campo 14 da SAFX52\);

    \- Valor Total p/o IR \(campo 42 da SAFX52\);

O grupamento é necessário pois a chave da tabela do Inventário permite a existência de várias linhas de mesmo produto e grupo de contagem\. Isso porque na chave tem o 

campo “11\-Natureza do Estoque”, que permite diversas combinações com o mesmo produto\.

*Obs\.: O Sped Fiscal tem este mesmo agrupamento de dados na geração do H010, sendo que utiliza outros campos também, como Grupo de Contagem e Pessoa Fis/Jur\. Estes campos não são necessários aqui porque a recuperação dos dados considera apenas os registros de grupo de contagem = “1”\.*

 

Para cada grupamento, conforme as regras acima, será gravado um registro H010, com as seguintes informações: 

REG

Conteúdo fixo = “__H010__”

COD\_ITEM

Identificação do produto \(campos 6 e 7 da SAFX52\), conforme o grupamento descrito acima\.

 

A geração deste campo depende da parametrização dos dados inicias do estabelecimento em questão \(menu “*Parâmetros🡪 Dados Iniciais”\)*, da seguinte forma:

Se parâmetro “*Considerar o indicador no código do produto*” marcado,

     O campo será gerado com a concatenação do indicador \+ código do produto, no formato: X\-XXXXXXXXXXXXXX;

Senão

      O campo será gerado apenas com o código do produto;

__Crítica da existência de mais de uma linha no grupamento para o mesmo produto__:

Caso o grupamento retorne mais de uma linha para o mesmo produto, será realizado o seguinte procedimento:

\(ou seja, o produto foi registrado no Inventáriuo para mais de uma unidade de medida\)

\- O registro H010 será gravado normalmente;

\- Será gravada a mensagem abaixo no log de erros, para alertar o usuário sobre a existência do problema:

*                      “Foi identificada a existência de inventário do produto em diferentes unidades de medida”*

O log deve exibir a identificação do registro \(“H010”\) com erro e a identificação do produto, no mesmo padrão do Sped Fiscal\.

<a id="OLE_LINK8"></a>Todos os produtos gravados neste registro, serão registrados no Bloco 0, registro 0200, e registros “filhos” 0205 e 0206, quando for o caso\.  

UNID

Código da unidade de medida \(campo12 da SAFX52\), conforme o grupamento descrito acima\.

Todos as unidades de medida gravadas neste registro, serão registrados no Bloco 0, registro 0190\.  

QTD

Totalização do campo “13\-Quantidade” da SAFX52, conforme o grupamento descrito acima\.

VL\_UNIT

Campo “15\-Custo Unitário” da SAFX52\.

Quando o registro H010 a ser gravado for o resultado do agrupamento de mais de um registro da SAFX52, o valor unitário será calculado, da seguinte forma:

                  Total do Custo Total gravado no campo __VL\_ITEM__ __/__ Quantidade gravada no campo __QTD__ 

VL\_ITEM

Totalização do campo “14\-Custo Total” da SAFX52, conforme o grupamento descrito acima\.

IND\_PROP

Este campo será gerado sempre com o conteúdo “0” \(Item de propriedade do informante e em seu poder\)

*\(ver esclarecimentos na introdução do item “4\-Regras de Geração do Bloco H”\)*

COD\_PART

Este campo será gerado sem informação \(“||”\), pois o indicador de propriedade \(IND\_PROP\) será sempre o informante\.

TXT\_COMPL

Campo 16\-Observação da SAFX52\.

Quando o registro H010 a ser gravado for o resultado de agrupamento de mais de um registro da SAFX52, os textos das observações deverão ser concatenados e separados com "/" ou "\-" \(mesmo procedimento realizado no Sped Fiscal\)\.

COD\_CTA

Campo 18\-Código da Conta Contábil da SAFX52\.

Quando o registro H010 a ser gravado for o resultado do agrupamento de mais de um registro da SAFX52, com diferentes códigos de conta, será considerada para geração deste campo a conta do registro da SAFX52 de maior valor de inventário \(campo 14 da SAFX52\)\. 

\(É o mesmo procedimento realizado no Sped Fiscal, por orientação do Guia Prático\)

VL\_ITEM\_IR

Totalização do campo “42\-Valor Total p/o IR” da SAFX52, conforme o grupamento descrito acima\.

# <a id="_Toc83644709"></a>Registro H011 –  Identificação do Estabelecimento Detentor do Inventário

__\[MFS46838\] Tratamento para Perfil D:__

Registro “filho” do H010, deve ser gerado apenas para o __Perfil D__\.  Apresentando os estabelecimentos detentores do inventário informado no H010\. 

Lembrando que, conforme descrito na introdução do item “4\-Regras de Geração do Bloco H”, serão considerados apenas os dados de inventário dos produtos referenciados no arquivo \(registros 2112, 2113 e 2130\)\.

__Origem dos dados__: SAFX52

__Critérios de recuperação__: \(mesmos critérios de recuperação dos registros de inventário do Registro H010\)

    \- Empresa 🡪 código da Empresa;

    \- Estabelecimento 🡪 código do Estabelecimento selecionado para geração, observando o tratamento abaixo:

__    __Caso o estabelecimento selecionado na tela de geração seja um estabelecimento __Centralizador__, recuperar os registros de inventário do estabelecimento __Centralizador__ e dos seus __    __

__    __estabelecimentos __Centralizados__, que foram a ele relacionados, na parametrização da “Centralização de Estabelecimentos p/ Perfil D”\.

__    __Caso o estabelecimento selecionado na tela de geração seja um estabelecimento “__Não centralizado”__, recuperar os registros de inventário apenas do estabelecimento selecionado para 

    geração\.

    \- Data do Inventário 🡪 data do último dia do período da geração; 

    \- Produto 🡪 indicador e código do Produto;

    \- Grupo de Contagem 🡪 será considerado apenas o grupo de contagem = “1” \(Estoque Próprio, em Poder do Estabelecimento\);

__Grupamento__:

Os dados recuperados serão agrupados por:  

    \- Estabelecimento \(capo 2 da SAFX52\)

    \- Produto \(campos 6 e 7 da SAFX52\);

    \- Unidade de Medida \(campo 12 da SAFX52\);

O Produto e a Unidade de Medida fazem parte do grupamento pois são os dados chave do registro pai H010\.

Para cada grupamento, conforme as regras acima, será gravado um registro H011, com as seguintes informações: 

REG

Conteúdo fixo = “__H011__”

CNPJ

Preencher com o CNPJ do cadastro do Estabelecimento recuperado\.

Importante: 

- Este registro deve ser gerado apenas quando o __Perfil for D__\. Ver o campo Perfil do estabelecimento informado na tela de geração, na Parametrização dos dados iniciais \(menu Parâmetros > Dados Iniciais, campo “Perfil da EFD”\)\.

# <a id="_Toc83644710"></a>Registro H990 – Encerramento do Bloco H

REG

Conteúdo fixo = “__H990__”

QTD\_LIN\_H

Quantidade total de linhas informadas no Bloco H, incluindo os registros de abertura e fechamento do Bloco\.

= = = = = =

 

