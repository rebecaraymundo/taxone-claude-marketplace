# MTZ-Ressarc-PR-Parametrizacao_MVA

- **Fonte:** MTZ-Ressarc-PR-Parametrizacao_MVA.docx
- **Modificado:** 2020-04-17
- **Tamanho:** 73 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – PR

Parametrização CEST x MVA

__Localização__: Menu Estadual, módulo Ressarcimento de ICMS\-ST \- PR, menu Parâmetros 🡪 MVA

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS34473__

Criação da parametrização MVA

Criação da parametrização dos valores de MVA \(Margem de Valor Agregado\)\. 

17/03/2020

Sumário

[1\.	Regras Gerais	2](#_Toc451940535)

[2\.	Layout da Tela	2](#_Toc451940536)

[3\.	Regras de Funcionamento dos Campos	4](#_Toc451940537)

# <a id="_Toc451940535"></a>Regras Gerais

Parametrização criada na __MFS34473__ para a atualização legal do módulo Ressarcimento ICMS\-ST – PR\.

Esta é uma parametrização de MVA \(Margem de Valor Agregado\) por CEST \(Código Especificador da Substituição Tributária\)\.

Para cada CEST \(TACES94\), o usuário poderá informar uma margem de valor agregado\. E em caso de alteração legal,  poderá informar um novo MVA com nova data de validade\.

*Obs\.: A criação desta parametriação foi muito discutida entre REQ/PO/Informação, e acabamos entendendo ser a melhor alternativa para obter a informação do MVA\. Foram pensadas várias outras alternativas, mas por diversos motivos, a decisão foi criar no próprio módulo do PR uma parametrização dos MVA’s por CEST \(conforme lista de MVA’s da Resolução SEFA N\. 020, de 20/01/2017\)\. *

Os valores da MVA são utilizados no cálculo dos totais do registro 1500 \(campo L03\)\.

# <a id="_Toc451940536"></a>Layout da Tela

	

Parâmetros MVA

CEST

\(Código Especificador da Substituição Tributária\)

MVA

Data Início Validade

XXXXXXX \- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

9\.999,99

99/99/9999

XXXXXXX \- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

9\.999,99

99/99/9999

XXXXXXX \- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

9\.999,99

99/99/9999

XXXXXXX \- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

9\.999,99

99/99/9999

XXXXXXX \- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

9\.999,99

99/99/9999

XXXXXXX \- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

9\.999,99

99/99/9999

XXXXXXX \- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

9\.999,99

99/99/9999

XXXXXXX \- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

9\.999,99

99/99/9999

__Botões da barra de menu__:

NOVO

Ao clicar nesta opção será aberta uma nova linha para que o usuário insira um novo registro\. 

CONFIRMA

Opção para salvar os dados alterados ou incluídos\.

EXCLUI

Permite a exclusão da linha em foco

ORDENA

Oferece ao usuário diferentes formas de ordenar os dados, por Código CEST, MVA ou Data de Validade\.

\(Opção padrão deste tipo de tela\) 

RELATÓRIO

Esta opção permite imprimir os dados da parametrização\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

  

Esta tela não apresenta a opção <ABRE>, já que na abertura da tela já são apresentados todos os registros existentes\. 

Para visualizar todos os registros, o usuário pode utilizar a barra de rolagem vertical\.

# <a id="_Toc451940537"></a>Regras de Funcionamento dos Campos

Na abertura da tela, são demonstradas todas as linhas da tabela, na seguinte ordenação:

   \- Código CEST

   \- MVA

   \- Data Inicio Validade

A chave da tabela é composta pelas informações: CEST \+ DATA INICIO VALIDADE

Segue detalhamento do funcionamento dos campos:

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/__

__Default__

__Regra__

CEST

Alfanumérico

__    S__

S

Este campo trabalha com janela de seleção da TACES94 \(Código Especificador da Substituição Tributária\)\.

Após o usuário selecionar o CEST desejado, será exibido o código e a sua descrição \(conforme o layout acima\)\.

MVA

Numérico

__    S__

S

Neste campo será informado um valor para a margem de valor agregado \(MVA\)\. Deve ser um valor > zeros\.

Tamanho: 9999,99 \(4 inteiros e 2 decimais\)2

\(seguindo o exemplo dos MVA’s da Resolução SEFA  020, 20/01/17\)

Data Inicio Validade

Data

__    S__

S

Data da validade inicial do MVA para o CEST informado\.

Deve ser uma data válida\.

= = = = = =

