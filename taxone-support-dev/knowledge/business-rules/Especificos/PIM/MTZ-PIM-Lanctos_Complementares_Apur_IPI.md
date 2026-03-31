# MTZ-PIM-Lanctos_Complementares_Apur_IPI

- **Fonte:** MTZ-PIM-Lanctos_Complementares_Apur_IPI.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 74 KB

---

THOMSON REUTERS

Módulo PIM \(Incentivos Ficais do Polo Industrial de Manaus\)

Manutenção dos Lançamentos Complementares da Apuração do IPI

__Localização__: Menu Específicos, Módulo PIM, item Apuração 🡪 Apuração do IPI 🡪 Lançamentos Complementares 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS13326

Ato Cotepe 48/2017

\-Inclusão da opção “3\-Documento Fiscal” no campo “Origem”;

\-Retirada obrigatoriedade do “Número”, se informada a “Origem”;

\-Criação da opção “Documentos Fiscais Vinculados \(Sped Fiscal, E531\)”; 

21/09/2017

\(criação do documento\)

Sumário

[1\.	Regras Gerais	3](#_Toc493771865)

[2\.	Aba APURAÇÃO	3](#_Toc493771866)

[3\.	Aba LANÇAMENTO DE VALORES	3](#_Toc493771867)

[4\.	Aba GUIA	4](#_Toc493771868)

[5\.	Aba GUIA \-RIPI	4](#_Toc493771869)

# <a id="_Toc493771865"></a>Regras Gerais

# <a id="_Toc350763252"></a><a id="_Toc493771866"></a>Aba APURAÇÃO

# <a id="_Toc493771867"></a>Aba LANÇAMENTO DE VALORES

__MFS13627__ – Alterações para atendimento ao Ato Cotepe 48/2017:

\- O título ”*Documento Vinculado ao Ajuste*” foi renomeado para *“*<a id="OLE_LINK10"></a><a id="OLE_LINK11"></a>*Documento Vinculado ao Ajuste \(Sped Fiscal \- Reg E530\)”;*

\- Retirada obrigatoriedade de preenchimento do campo “Número” quando o campo “Origem” for preenchido;

\- Incluída a opção “3” na lista de valores do campo “Origem”;

<a id="OLE_LINK8"></a><a id="OLE_LINK9"></a>

\- Incluída a opção “<a id="OLE_LINK13"></a><a id="OLE_LINK14"></a><a id="OLE_LINK15"></a>*Documentos Fiscais Vinculados \(Sped Fiscal – Reg\. E531\)*”;

__Regras do funcionamento dos campos:__

<a id="OLE_LINK46"></a><a id="OLE_LINK47"></a><a id="OLE_LINK48"></a>__Regras do funcionamento dos campos:__

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

*Documento Vinculado ao Ajuste \(Sped Fiscal \- Reg E530\) – *

Origem

Alfanumérico

N

S

Listbox

Este campo é uma lista com as seguintes opções:

0 \- Processo Judicial

1 \- Processo Administrativo

2 – PER/DCOMP

3 – Documento Fiscal     \(incluída na __MFS13326__\)

9 \- Outros

Ao salvar a operação, se o campo “Origem” for preenchido e o campo “Número” não tiver sido informado, será exibida a mensagem “*Favor informar o Número do Documento Vinculado ao Ajuste*”, e a operação não será salva\. \(crítica retirada pela __MFS13326\)\.__

Ver crítica referente à Origem = 3 na __RN01 __abaixo\.

MFS13326

<a id="OLE_LINK38"></a><a id="OLE_LINK39"></a><a id="OLE_LINK21"></a><a id="OLE_LINK22"></a><a id="OLE_LINK23"></a>Documentos Fiscais Vinculados \(Sped Fiscal – Reg\. E531\)

\(opção criada na MFS13326\)

Button

Esta opção ficará disponível *apenas* quando o campo “Origem” for preenchido com a opção “3\-Documento Fiscal”\.

Caso contrário, ficará desabilitada\.

Ao clicar nesta opção será aberta uma janela para o usuário informar os documentos fiscais vinculados ao lançamento em questão\.

Verificar abaixo as regras específicas desta janela\.

OBS: Ao passar o mouse sobre este botão, aparecerá a mensagem *“Opção válida apenas para os lançamentos de Origem = 3”*\. \(semelhante à tela da apuração do ICMS\)

__RN01__

Ao salvar a operação, será realizada a seguinte crítica:

Caso o usuário tenha alterado a origem do lançamento de “3” para outra opção qualquer, será exibida a seguinte mensagem:

                        “Ao alterar a origem do lançamento de “3” p/outra origem qualquer, os documentos

                            fiscais vinculados que já tenham sido informados serão apagados\. Confirma?”

      

                                                                  <<OK>>      <<Cancela>>

Caso o usuário confirme, a operação será salva normalmente e os documentos fiscais vinculados já existentes serão excluídos\. Quando se tratar de um lançamento novo \(a ser incluído\), os documentos fiscais informados serão simplesmente desconsiderados\.

__Documentos Fiscais Vinculados \(Sped Fiscal – Reg\. E531\):__

Para cada lançamento, o usuário poderá associar um ou vários documentos fiscais\.

Para informar um documento, o usuário deverá obrigatoriamente clicar na pastinha amarela \(vide layout da tela\), que exibirá os dados da tabela de documentos fiscais\. 

Serão disponibilizados para seleção apenas os documentos fiscais que atendam aos seguintes critérios:

\- documentos fiscais do estabelecimento __e inscrição estadual__ da apuração;

\- data de emissão <= a data da apuração \(data da aba “Apuração”\);

\- <a id="OLE_LINK43"></a><a id="OLE_LINK44"></a><a id="OLE_LINK45"></a>modelo = “01” ou “55” \(conforme regra do Guia Prático vrs 2\.0\.21\);

__Regras do funcionamento dos campos:__

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Dt\. Fiscal

Data

S

N

Neste campo será exibida a data fiscal do documento fiscal selecionado pelo usuário\.

\(o campo fica desabilitado\)

E/S

Alfanumérico

S

N

Neste campo será exibido o tipo de movimento do documento fiscal selecionado pelo usuário, no seguinte formato:

“E” – quando se tratar de nota fiscal de entrada

“S” – quando se tratar de nota fiscal de saída

\(o campo fica desabilitado\)

NF/Série/Sub

Alfanumérico

S

N

Neste campo será exibido o número, a série e a subsérie do documento fiscal selecionado pelo usuário\. 

\(os campos ficam desabilitados\)

Pessoa Fis/Jur \(Ind/Cód\.\)

Alfanumérico 

S

N

Neste campo será exibido o indicador e o código da pessoa fis/jur do documento fiscal selecionado pelo usuário\.

\(os campos ficam desabilitados\)

Item da NF

Numérico

N

S

Lista/Nenhum

Neste campo o usuário poderá, opcionalmente, informar o item do documento fiscal informado ao qual se refere o ajuste\. 

O campo exibe uma lista com a numeração dos tens do documento fiscal \+ opção em branco\. 

Vlr Ajuste

Numérico

S

S

Neste campo o usuário informará o valor do ajuste referente ao documento ou item do documento informado\.

Ao salvar os dados desta janela, será realizada uma crítica, conforme __RN01__ abaixo\.

<a id="_Hlk493855023"></a>__RN01__

Ao salvar os documentos informados nesta janela, será realizada a comparação entre o valor do lançamento e o total do valor informado no campo “Vlr Ajuste” de todos os documentos/itens informados\.

Caso o total do ajuste não seja igual ao valor do lançamento, será exibida a mensagem abaixo e a operação não será salva\.

*           “O total geral dos ajustes informados não confere com o valor informado no lançamento\. Favor verificar”*

# <a id="_Toc493771868"></a>Aba GUIA

# <a id="_Toc493771869"></a>Aba GUIA \-RIPI

= = = = = =

