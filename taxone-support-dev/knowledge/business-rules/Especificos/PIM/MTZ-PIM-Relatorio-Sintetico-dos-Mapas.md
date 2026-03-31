# MTZ-PIM-Relatorio-Sintetico-dos-Mapas

- **Fonte:** MTZ-PIM-Relatorio-Sintetico-dos-Mapas.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 71 KB

---

THOMSON REUTERS

PIM – Gestão do Controle de Incentivos Fiscais de Manaus

Relatório Sintético dos Mapas

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4789

Julyana Perrucini

<a id="OLE_LINK30"></a><a id="OLE_LINK31"></a><a id="OLE_LINK32"></a><a id="OLE_LINK132"></a><a id="OLE_LINK133"></a>Este documento tem como objetivo incluir o componente 22\-Diferimentos na geração do relatório\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral__

__Regra de Cabeçalho__

- Demonstrar apenas título Relatório Sintético dos Mapas e incluir numeração de página \(exemplo: 1 de 5\)\.

Formato definido em documento Layout\_PIM\_Relatorio\_Sintetico\_dos\_Mapas\.xls\.

OS4789

<a id="_Hlk418252166"></a>RN01

<a id="OLE_LINK92"></a><a id="OLE_LINK93"></a><a id="OLE_LINK94"></a>__Componente 22\-Diferimentos – Regra Geral__

Para geração do relatório sintético dos mapas para este componente, é necessário efetuar a geração da rotina de cálculo através da <a id="OLE_LINK83"></a>Apuração >> Geração dos Mapas >> Acessórios\.

Nesta rotina do cálculo são inicialmente contabilizados os valores totais das saídas \(valor contábil\) com as seguintes características:

- Notas de saídas tributadas, ou seja, cujo campo de ICMS esteja preenchido com valor maior que zero, e cujos CFOP’s/Naturezas estejam parametrizados para o componente 22 \(a partir destes dados, é criado um vetor contendo a totalização dos valores contábeis por linha de incentivo\)\. 

Em seguida são lidos os documentos de entrada com valor de ICMS não\-destacado, cujos CFOP’s/Naturezas estejam parametrizados para o componente 22, para cada nota recuperada será buscado o código de estrutura e item para o componente 22\. Para cada linha contida no vetor de totais das saídas tributadas, será efetuado o seguinte cálculo:

- O valor do ICMS não\-destacado é multiplicado pelo resultado da divisão do valor contábil pelo total das saídas;
- Caso o valor resultante seja maior que zero, a nota fiscal será gravada na <a id="OLE_LINK95"></a><a id="OLE_LINK96"></a><a id="OLE_LINK97"></a><a id="OLE_LINK98"></a>tabela ICT\_AM\_AP\_NF, e o valor resultante gravado no campo VLR\_TRIBUTO da nota fiscal\.

Observação: Cada nota de entrada recuperada nesta rotina será duplicada, quantas vezes existirem linhas de incentivo com valores de saídas tributadas\.

Não existe tela de manutenção para esse componente\.

Após a gravação dos dados na tabela <a id="OLE_LINK99"></a><a id="OLE_LINK100"></a><a id="OLE_LINK101"></a>ICT\_AM\_AP\_NF de acordo com o cálculo efetuado conforme esclarecido anteriormente, considerar para recuperação dos registros a serem demonstrados no relatório o Estabelecimento, a Inscrição Estadual a Data de Apuração e o Componente deve ser igual a 22\-Diferimentos\.

OS4789

RN02

<a id="OLE_LINK102"></a><a id="OLE_LINK103"></a>__Componente 22\-Diferimentos – CAMPO LINHA DE PRODUÇÃO__

Preencher concatenando e separando por hífen \(\-\) o código de linha de produto \+ descrição, cadastrados na linha de produtos incentivados referentes à informação utilizada para o cálculo<a id="OLE_LINK107"></a><a id="OLE_LINK108"></a><a id="OLE_LINK109"></a><a id="OLE_LINK110"></a>, de acordo com o código gravado no campo COD\_LINHA\_PRD da tabela ICT\_AM\_AP\_NF\.

OS4789

RN03

__Componente 22\-Diferimentos – CAMPO COMPONENTE__

Preencher concatenando e separando por hífen \(\-\) o conteúdo do campo Componente \+ descrição, da parametrização feita em Parâmetros dos Mapas >> Itens para o campo Componente igual a 22\-Diferimento, de acordo com o item gravado no campo COD\_COMP\_APUR da tabela ICT\_AM\_AP\_NF\.

OS4789

RN04

<a id="OLE_LINK111"></a><a id="OLE_LINK112"></a><a id="OLE_LINK113"></a>__Componente 22\-Diferimentos – CAMPO ESTRUTURA__

<a id="OLE_LINK114"></a><a id="OLE_LINK115"></a><a id="OLE_LINK116"></a>Preencher concatenando e separando por hífen \(\-\) o conteúdo do campo Estrutura \+ Cod/Dsc\., da parametrização feita em Parâmetros dos Mapas >> Estrutura para o campo Componente igual a 22\-Diferimento, de acordo com a estrutura gravada no campo COD\_ESTRUT da tabela ICT\_AM\_AP\_NF\.

OS4789

RN05

<a id="OLE_LINK117"></a><a id="OLE_LINK118"></a>__Componente 22\-Diferimentos – CAMPO ITEM__

Preencher concatenando e separando por hífen \(\-\) o conteúdo do campo Item \+ descrição, da parametrização feita em Parâmetros dos Mapas >> Itens para o campo Componente igual a 22\-Diferimento, de acordo <a id="OLE_LINK119"></a><a id="OLE_LINK120"></a><a id="OLE_LINK121"></a><a id="OLE_LINK122"></a>com o item gravado no campo COD\_ITEM\_APUR da tabela ICT\_AM\_AP\_NF\.

OS4789

RN06

<a id="OLE_LINK123"></a><a id="OLE_LINK124"></a>__Componente 22\-Diferimentos – CAMPO VALOR__

Preencher com o valor calculado através do mapa acessório \(verificar RN01\) gravado no campo VLR\_TRIBUTO da tabela ICT\_AM\_AP\_NF\.

OS4789

RN07

<a id="OLE_LINK125"></a><a id="OLE_LINK126"></a><a id="OLE_LINK127"></a>__Componente 22\-Diferimentos – CAMPO TOTAL DO COMPONENTE__

<a id="OLE_LINK128"></a><a id="OLE_LINK129"></a><a id="OLE_LINK130"></a><a id="OLE_LINK131"></a>Preencher a totalização dos valores por componente\.

OS4789

RN08

__Componente 22\-Diferimentos – CAMPO TOTAL DA ESTRUTURA__

Preencher a totalização dos valores por estrutura\.

OS4789

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

