# MTZ_Monitor_Tributos_Pagar_Tela_Layout_XML

- **Fonte:** MTZ_Monitor_Tributos_Pagar_Tela_Layout_XML.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 156 KB

---

THOMSON REUTERS

 Parametrização do Layout XML

 XML

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS3962\-D 

Elenilson Coutinho 

Parametrização de Layout XML

MFS\-1685

Elenilson Coutinho

Atualização da tela Parametrização do Layout XML para que demonstre o imposto IPI

MFS\-1683

Elenilson Coutinho

Atualização da tela Parametrização do Layout XML para que demonstre o imposto ICMS

MFS\-1686

Elenilson Coutinho

Atualização da tela Parametrização do Layout XML para que demonstre os impostos PIS/PASEP e COFINS

MFS\-1684

Elenilson Coutinho

Atualização da tela Parametrização do Layout XML para que demonstre o imposto ICMS\-ST

MFS\-1687

Elenilson Coutinho

Inclusão do Botão “Definir Layout Retorno” e Painel, dos Labels “Layout de Envio” e Layout de Retorno\. e do campo Autent\. Bancaria\.

MFS\-3268

Elenilson Coutinho

Alteração no campo “Declaração XML” e “Tag XML”

MFS\-4069

Elenilson Coutinho

Desabilitar os campos Conteúdo Fixo e Variável quando Tipo Tag selecionada a opção “Grupo”

MFS\-5052

Ajuste na tela

Bloqueio do campo “Casas Decimais” quando selecionado o conteúdo variável “Agência”

MFS\-5047

Ajuste na tela

Inclusão de campos ao definir layout de retorno\.

MFS\-6310

Geração do Arquivo de Impostos Apurados

Retirar os impostos ICMS e ICMS\-ST 

Sumário

[1\.	TELA A SER DESENVOLVIDA	3](#_Toc391035964)

[1\.1\.	Diagrama de Casos de Uso	3](#_Toc391035965)

[1\.1\.1\.	UC001 – Manutenção da Estrutura Padrão	3](#_Toc391035966)

[1\.1\.1\.1\.1\.	Fluxo Principal	4](#_Toc391035967)

[1\.1\.1\.1\.2\.	Fluxo Alternativo 1 – Localizar registros \(Exemplo\)	4](#_Toc391035968)

[2\.	Regras dos Campos	4](#_Toc391035969)

# <a id="_Toc391035964"></a>TELA A SER DESENVOLVIDA

\[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir\]

## <a id="_Toc350763243"></a><a id="_Toc391035965"></a>Diagrama de Casos de Uso 

__ __

__UC Estrutura Padrão__

__Usuário __

__UC001 – Manutenção da   __

__Estrutura Padrão__

Manutenção Padrão

## <a id="_Toc350763244"></a><a id="_Toc391035966"></a>UC001 – Manutenção da Estrutura Padrão

\[Descrever a ação deste caso de uso\. 

Ex\.: Este caso de uso descreve o processo de Cadastro de Estrutura Padrão\.\]

__Documentação do Caso de Uso__

__Ator Principal__

Usuário do Sistema

__Pré\- Condições__

Estar logado no produto MasterSAF DW\.

__Pós\-Condições__

Não se aplica\.

### <a id="_Toc332809652"></a><a id="_Toc332888915"></a><a id="_Toc350763245"></a><a id="_Toc391035967"></a>Fluxo Principal 

__Ações do Ator__

__Ações do Sistema__

### <a id="_Toc332809666"></a><a id="_Toc332888929"></a><a id="_Toc350763246"></a>

### <a id="_Toc391035968"></a>Fluxo Alternativo 1 – Localizar registros \(Exemplo\)

__Ações do Ator__

__Ações do Sistema__

# <a id="_Toc350763252"></a><a id="_Toc391035969"></a>Regras dos Campos 

__Localização da tela:__ Módulo: Gestão Estratégica🡪 Monitor de Tributos a Pagar

__                                   __Menu: Parâmetros🡪Layout do Arquivo XML

__   __

__Título da tela: __Parametrização de Layout XML

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Status do Layout

Radio Button

S

S

Default: Ativo

Exibir as opções:

- Ativo
- Inativo

OS3962\-D

Código/Descrição do Tipo do Arquivo

Editbox

S

S

Deverá recuperar os códigos de tipo de arquivo cadastrados no menu: Parâmetros >> Tipo de Arquivo do módulo Monitor de Tributos a Pagar

Obs: Deverá existir tratamento para não exibir a opção “Arquivo TXT”\.

OS3962\-D

Tipo do Arquivo

Editbox

S

N

Esse campo será preenchido de acordo com o campo “Código/Descrição do Tipo do Arquivo”\.

OS3962\-D

Código do Layout

Editbox

S

S

OS3962\-D

Descrição do Layout

Editbox

S

S

OS3962\-D

Grupo Tributo/Tributo

Dropdown

S

S

Lista com as opções \(default: não preenchido\)

Preencher conforme abaixo:

1 – Federal

2 – Estadual 

3 – Municipal 

4 – Previdenciário

Caso o campo “Grupo Tributo” não esteja preenchido, deve ser exibida a seguinte mensagem de erro: “Informe Grupo Tributo“\.O campo Tributo deverá aparecer vazio\. A lista de layout\(s\) deverá estar vazia\.

Obs: Não serão apresentados os respectivos “números” dos tributos, apenas a descrição\. Estes números serão a referencia para o campo “grupo\_tributo” da TFIX140\.

OS3962\-D

MFS\-1683

Lista de Tributos\*

Lista

S

S

Lista com as opções \(default: desabilitado e não preenchido\)

Será habilitado quando for informado o Grupo Tributo, demonstrando apenas os Tributos relacionados ao Grupo indicado, conforme regras abaixo:

Para o Grupo Federal, demonstrar as opções:

- IRPJ
- IRRF
- CSLL
- PIS/PASEP
- COFINS 
- IPI
- PIS/PASEP \(PRÓPRIO\)
- COFINS \(PRÓPRIO\)

\[MFS\-6310\]

Para o Grupo Municipal, demonstrar as opções:

- ISS

Para o Grupo Previdenciário, demonstrar a opção:

- INSS

Caso o campo “Lista de Tributos” não esteja preenchido, deve ser exibida a seguinte mensagem de erro: “Informe Tributo“\. A lista de layout\(s\) deverá estar vazia\.

OS3962\-D

MFS\-1685

MFS\-1683

MFS\-1686

MFS\-1684

MFS\-6310

Declaração XML

Editbox

S

S

Esta é uma instrução padrão, que sempre deve ser inserida no começo de um documento XML\.

Serão apresentadas as seguintes opções:

<?xml version="1\.0"?>

<?xml version="1\.0" encoding="UTF\-16"?>

<?xml version="1\.0" encoding="ISO\-8859\-1"?>

Caso não preenchido deverá exibir a seguinte mensagem: “Declaração XML não informada\.”

OS3962\-D

MFS\-3268

Duplicar Layout

Botão

N

N

Ao clicar nesse botão, o sistema irá copiar para um novo registro todas as informações do layout que estiver sendo visualizado, com exceção do Código e a Descrição do Layout, que deverá ser informado pelo usuário\.

Caso o usuário tente salvar o registro sem fazer alterações em ao menos um dos campos: Grupo Tributo, Tributo, Parametrização do Layout ou Parâmetros de Seleção, mesmo que tenha código de layout distinto, não permitir a gravação e retornar a mensagem: “Registro já possui as informações Grupo Tributo, Tributo, Layout e Parâmetros de Seleção cadastradas\. Por gentileza alterar” e não deve incluir o novo registro\.

Obs: Quando acionado o botão “Definir Layout de Retorno” este deverá ser desabilitado\. Funcionalidade deste botão ativa apenas para o layout de envio\.

OS3962\-D

MFS\-1687

Definir Layout de Retorno

Botão

N

N

Default: Desabilitado

Ao clicar nesse botão o sistema deverá criar um layout de retorno igual ao layout de envio parametrizado pelo usuário, porém, desabilitado, ou seja, não será possível qualquer edição, inclusão ou exclusão de campo\.

Os campos “Conteúdo Fixo”, “Conteúdo Variável” e “Parâmetros de Seleção” não farão parte do layout\.

Este layout terá novos campos \(fixos\) serão eles:

Valor Total: Numérico, 17,2

Valor de Juros: \(Numérico\), 17,2,

Valor de Multa: \(Numérico\), 17,2

Data de Pagamento: \(Data\), 8, decimal não será preenchido\.

Estes campos serão desabilitados para edição, posição inicial seguirá o sequencial do campo anterior, Tipo da Tag default = “Atributo”, campos Num\. Tag Pai Para elementos e Atributos os números da tag devem utilizar a sequência do campo “Ordem do Campo”\.

Terá também o campo, \(último campo do layout\) com descrição “Autent\. Bancaria”, também desabilitado para qualquer edição,

Tipo default = Alfanumérico, Tag XML default = AUTENT\_BANCARIA, Tipo da Tag default = “Atributo” e os campos Num\. Tag Pai, Tamanho e Decimais não preenchidos\.

Botão dinâmico, quando acionado será alterado para “Verificar Layout de Envio”\.

Obs: Este botão só será habilitado após utilização do layout de envio\.

MFS\-1687

MFS\-5047

Layout de Envio 

Texto

N

N

Quando acionado o botão “Definir Layout Retorno”, este label deverá ser alterado para “Layout de Retorno”, ou seja, campo dinâmico\.

MFS\-1687

Ordem do Campo

Editbox

S

N

Campo autoincremental\. Irá gerar uma sequência numérica, iniciando em 1\.

OS3962\-D

Descrição do Campo

Editbox

S

S

OS3962\-D

Tag XML

Editbox

S

S

Informar o nome da tag XML, nomes de tags não podem conter espaços em branco nem os caracteres \!"\#$%&'\(\)\*\+,/;<=>?@\[\\\]^\`\{|\}~\. Além disso, não podem começar com um número, “ \. ” \(ponto\) ou “ \- " \(traço\)\.  


Caso a regra acima não seja respeitada, exibir a seguinte mensagem: “Nome de tag inválido”\.

Obs: Não poderá existir nome de tag XML iguais na parametrização, caso contrário exibir a seguinte mensagem: O nome da Tag XML XXXXX está repetido\. Favor corrigir\.

OS3962\-D

MFS\-3268

Tipo da Tag

Dropdown

S

S

Este campo terá as seguintes opções:

1 \- Raiz

2 \- Grupo

3 \- Atributo

4 \- Elemento

As opções poderão ser selecionadas da seguinte forma:

O primeiro campo do layout parametrizável, a coluna “Tipo da Tag” deverá ser o Raiz\. O sistema irá exibir automaticamente\. Ao selecionar a opção “Raiz” os seguintes campos ficarão desabilitados para serem informados:

Número Tag Pai 

Tipo do campo 

Máscara/Data

Tamanho

Decimal

Conteúdo fixo

Conteúdo variável

Agrupado

Quando o primeiro campo possui a coluna “Tipo Tag” – Raiz, o campo seguinte só poderá ser parametrizável com a opção, “Grupo”\. Quando a opção selecionada for “Grupo” os seguintes campos ficarão desabilitados para serem informados:

Tipo do campo 

Máscara/Data

Tamanho

Decimal

Conteúdo Fixo

Conteúdo Variável

Agrupado

Quando o campo possuir a coluna “Tipo Tag” – Grupo, o campo seguinte só poderá ser parametrizável com as opções Atributo e Elemento respeitando o Número Tag Pai\.

Quando a opção selecionada for “Atributo” ou “Elemento”, os campos ficarão habilitados\.

Número Tag Pai 

Tipo do campo 

Máscara/Data

Tamanho

Decimal

Conteúdo fixo

Conteúdo variável

Agrupado

Quando o campo possuir a coluna “Tipo Tag” – "Elemento" é necessário haver um campo anterior com tipo tag "Grupo" respeitando o Número Tag Pai\.

OS3962\-D

MFS\-3268

MFS\-4069

Número Tag Pai

Editbox

S

S

Nesse campo o usuário irá definir a ordem da hierarquia ou seja a sequência das tags na estrutura XML\.

Obs:

Seguir a seguinte regra referente ao campo Tipo da Tag\.

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>Raiz 🡪 Sempre zero

Grupo\-\->  Um Grupo deve apontar para Raiz 

Atributo 🡪 Deve apontar para um Grupo

Elemento 🡪 Deve apontar para um Grupo

\[Alteração MFS\-3268\]

Obs: Para elementos e Atributos os números da tag devem utilizar a sequência do campo “Ordem do Campo” Exemplo:Se o tipo da tag Grupo estiver na linha de ordem do campo = 5 os elementos e atributos que estão dentro da hierarquia deste grupo, terá o número da tag pai = 5

OS3962\-D

MFS\-3268

Tipo do Campo

Dropdown

S

S

Lista com as opções \(default: não preenchido\)

Preencher conforme abaixo:

       \- Alfanumérico

       \- Data

       \- Numérico

OS3962D

Mascara/Data

Editbox

N

S

Este campo será parametrizado pelo usuário onde poderá preencher a mascara/data a critério\.

Exemplos: DD/MM/AAAA, DD\-MM\-AAAA, etc\.

Obs: Este campo só será habilitado e obrigatório se o campo “Tipo do Campo” for “Data”\.

OS3962D

Tamanho

Editbox

S

S

Caso o campo “Tipo do Campo” seja do tipo “Data”, esse campo deverá ficar desabilitado\.

OS3962D

Decimal

Editbox

N

S

Esse campo irá definir se o campo terá casas decimais ou não\. Esse campo só ficará habilitado caso o campo “Tipo do Campo” seja “Numérico”\.

Obs: Caso o campo Dec\_Col\_Bd da TFIX140 estiver preenchido com conteúdo maior que zero o campo decimal deverá ser habilitado, caso contrário o campo deverá ficar desabilitado\.

OS3962D/

MFS\-5052

Conteúdo Fixo

Editbox

S

S

O campo deverá possuir a mesma quantidade de caracteres informada no campo “Tamanho”\.

O sistema não deverá aceitar que o conteúdo desse campo, seja diferente do definido no campo “Tipo de Campo”\. Exemplo: caso o “Tipo de Campo” seja “Numérico” o sistema deverá exibir mensagem de erro padrão informando essa situação\.

OS3962D

Conteúdo Variável

Editbox

S

S

As informações dos campos a serem selecionados serão recuperadas das seguintes tabelas de acordo com o Tributo selecionado:

- ISS = GPE\_FECHAMENTO\_ISS
- INSS = IRT\_GPS
- IPI = ITEM\_APURAC\_CALC

MFS\-6310

- PIS/PASEP \(PRÓPRIO\) = EPC\_REG\_AJT\_M200\_M600
- COFINS \(PRÓPRIO\) = EPC\_REG\_AJT\_M200\_M600
- Ao exibir os campos para seleção, o sistema só deverá exibir os campos de acordo com o formato definido no campo “Tipo do Campo”, conforme definição abaixo:
- Data
- Este campo será parametrizado pelo usuário onde poderá preencher a mascara/data a critério\. Exemplos: DD/MM/AAAA, DD\-MM\-AAAA, etc\.

                    

- Alfanumérico
	- Só serão exibidos os campos da TFIX140 que sejam do tipo Alfanumérico para o Tributo escolhido\.
- Numérico
	- Só serão exibidos os campos da TFIX140 que sejam do tipo Numérico para o Tributo escolhido\.

OS3962D

MFS\-1685

MFS\-1683

MFS\-1686

MFS\-1684

MFS\-6310

\*Limpar

Botão

N

N

Esse botão tem a função de limpar o campo “Conteúdo Variável”\.

Agrupado

Checkbox

N

S

Default: não habilitado e não selecionado

Este campo deve ser habilitado para seleção quando o formato do campo indicado em conteúdo variável for do tipo “Numérico”\. Quando selecionado, indica que o campo apontado como “Agrupado” será somado e as informações serão consolidadas na geração do arquivo\.

OS3962D

Mostra Rel

Checkbox

Default: não selecionado

Quando selecionado indica quais campo deverão sair no relatório de conferência de geração do arquivo\.

OS3962D

__Parâmetros de Seleção__

Conteúdo Variável

Editbox

N

S

Nesse campo, o usuário irá escolher os campos como parâmetros de seleção\. Obrigatoriamente deve existir ao menos um conteúdo variável do tipo Data e que tenha Condição igual a "Utilizado na tela"\. Caso o usuário não informe nenhum, não permitir a gravação do layout e retornar a mensagem: "É necessário haver ao menos 1 Conteúdo Variável do tipo Data e com a Condição igual a Utilizado na Tela\. Favor corrigir"\.

OS3962D

Condição

Dropdown

N

S

Lista com as opções \(default: não preenchido\)

Preencher conforme abaixo:

- É igual a
- É maior que
- É maior e igual a
- É menor que
- É menor e igual a
- É diferente que
- Utilizado na tela

Se a opção “Utilizado na tela” for selecionada, o sistema não irá permitir o preenchimento da coluna “Conteúdo Fixo”\.

OS3962D

Grupo

Editbox

S

N

Default: não preenchido

Nesse campo, o usuário irá selecionar o Grupo ao qual pertence o campo informado no campo “Conteúdo Variável”\.

OS3962D

Conteúdo Fixo

Editbox

S

S

Caso o campo seja preenchido com um conteúdo acima do valor máximo de caracteres, será exibida mensagem de erro informando o cliente e esse registro não será gravado\.

OS3962D

Grupo

Dropdown

N

S

Lista com as opções \(default: não preenchido\)

Preencher conforme abaixo:

- E
- Ou

OS3962D

*\* Descrição não disponível em tela*

![](data:image/png;base64,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BBBAIEsB+8+IZNkq6kIAAQQQQAABBBBAAAEE8iPgswKaAHR+homWIIAAAggggAACCCCAAAIIIIAAAggggAACxRMo2BYcxQOmxQgggAACCCCAAAIIIIAAAggggAACCCCAAAIugTzuAc0wIYAAAggggAACCCCAAAIIIIAAAggggAACCJRAgAB0CQaRLiCAAAIIIIAAAggggAACCCCAAAIIIIAAAnkUIACdx1GhTQgggAACCCCAAAIIIIAAAggggAACCCCAQAkECECXYBDpAgIIIIAAAggggAACCCCAAAIIIIAAAgggkEcBAtB5HBXahAACCCCAAAIIIIAAAggggAACCCCAAAIIlECAAHQJBpEuIIAAAggggAACCCCAAAIIIIAAAggggAACeRQgAJ3HUaFNCCCAAAIIIIAAAggggAACCCCAAAIIIIBACQQIQJdgEOkCAggggAACCCCAAAIIIIAAAggggAACCCCQRwEC0HkcFdqEAAIIIIAAAggggAACCCCAAAIIIIAAAgiUQKAufWg0GvuOHH/+8IMTExMjIyMl6BVdCCVw/MSZUOlJXFyBq1YsK27jaTkCCCCAAAIIIIAAAggggAACCCCAQD4FBgcHBwYGJMi8e6Z/bN3yqakp+VE1lQB0Pocs01ZJAJq4ZKbiHaqMge4QPNUigAACCCCAAAIIIIAAAggggAACJRfwCUCXfAuOYdehhlqdTmTYwxYVNn27RiZVTiIIFIIAAggggAACCCCAAAIIIIAAAggggAACCLgFSh6AHm0dqtvt7hd0WpjdSbALw8NzXBHKDJvXnV6daXfe86EI7SQLAggggAACCCCAAAIIIIAAAggggAACCGQjUPIAdDaI9rXoZddJrb+2rzqDlKOjwxnUQhUIIIAAAggggAACCCCAAAIIIIAAAgggUBSBigag9f4Vji069LCZ5z3HUicwHw3MZVOUu0nmbhuOlkuBno/q8+0ebdMSWVctOUazmb6OuqReHcI225BZe7LpNbUggAACCCCAAAIIIIAAAggggAACCCBQHYGKBqAdA6y3s1ALk9W/jpOOQLOZQD0UNpdjEbTaKsRRSOSJ6NmYCLt2SPBXx3/VfX3GHSN2b6DhzuuSn4t3m9HnyL0mIwIIIIAAAggggAACCCCAAAIIIIAAAgjkSoAAdK6GI0pjdORaB52jlNLaeVktQHYsTFYn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AQQQQAABBBBIRYAAdCqsFIoAAggggAACCCCAAAIIIIAAAggggAACCCBAAJo5gAACCCCAAAIIIIAAAggggAACCCCAAAIIIJCKAAHoVFgpFAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQIAANHMAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAIBUBAtCpsFIoAggggAACCCCAAAIIIIAAAggggAACCCCAAAFo5gACCCCAAAIIIIAAAggggAACCCCAAAIIIPD/b+/+XeRIzj6Ao0usxEqMs802e+GCU2rMLSh1ZAwb3t8gUHTJy5so0p9ijAKjQNFuuJE4HTg+2EAYYTswOJPn7ffaFPVW93T39PTTv+aziLvd2e6nqj5V07PzVW+JQIiAADqEVVECBAgQIECAAAECBAgQIECAAAECBAgQEEBbAwQIECBAgAABAgQIECBAgAABAgQIECAQIiCADmFVlAABAgQIECBAgAABAgQIECBAgAABAgQE0NYAAQIECBAgQIAAAQIECBAgQIAAAQIECIQICKBDWBUlQIAAAQIECBAgQIAAAQIECBAgQIAAAQG0NUCAAAECBAgQIECAAAECBAgQIECAAAECIQIC6BBWRQkQIECAAAECBAgQIECAAAECBAgQIEBAAG0NECBAgAABAgQIECBAgAABAgQIECBAgECIgAA6hFVRAgQIECBAgAABAgQIECBAgAABAgQIEBBAWwMECBAgQIAAAQIECBAgQIAAAQIECBAgECIggA5hVZQAAQIECBAgQIAAAQIECBAgQIAAAQIEBNDWAAECBAgQIECAAAECBAgQIECAAAECBAiECAigQ1gVJUCAAAECBAgQIECAAAECBAgQIECAAAEBtDVAgAABAgQIECBAgAABAgQIECBAgAABAiECAugQVkUJECBAgAABAgQIECBAgAABAgQIECBAQABtDRAgQIAAAQIECBAgQIAAAQIECBAgQIBAiIAAOoRVUQIECBAgQIAAAQIECBAgQIAAAQIECBAQQFsDBAgQIECAAAECBAgQIECAAAECBAgQIBAiIIAOYVWUAAECBAgQIECAAAECBAgQIECAAAECBATQ1gABAgQIECBAgAABAgQIECBAgAABAgQIhAgIoENYFSVAgAABAgQIECBAgAABAgQIECBAgAABAbQ1QIAAAQIECBAgQIAAAQIECBAgQIAAAQIhAgLoEFZFCRAgQIAAAQIECBAgQIAAAQIECBAgQEAAbQ0QIECAAAECBAgQIECAAAECBAgQIECAQIiAADqEVVECBAgQIECAAAECBAgQIECAAAECBAgQEEBbAwQIECBAgAABAgQIECBAgAABAgQIECAQIiCADmFVlAABAgQIECBAgAABAgQIECBAgAABAgQE0NYAAQIECBAgQIAAAQIECBAgQIAAAQIECIQICKBDWBUlQIAAAQIECBAgQIAAAQIECBAgQIAAAQG0NUCAAAECBAgQIECAAAECBAgQIECAAAECIQIC6BBWRQkQIECAAAECBAgQIECAAAECBAgQIEBAAG0NECBAgAABAgQIECBAgAABAgQIECBAgECIgAA6hFVRAgQIECBAgAABAgQIECBAgAABAgQIEBBAWwMECBAgQIAAAQIECBAgQIAAAQIECBAgECIggA5hVZQAAQIECBAgQIAAAQIECBAgQIAAAQIEBNDWAAECBAgQIECAAAECBAgQIECAAAECBAiECAigQ1gVJUCAAAECBAgQIECAAAECBAgQIECAAAEBtDVAgAABAgQIECBAgAABAgQIECBAgAABAiECAugQVkUJECBAgAABAgQIECBAgAABAgQIECBAQABtDRAgQIAAAQIECBAgQIAAAQIECBAgQIBAiIAAOoRVUQIECBAgQIAAAQIECBAgQIAAAQIECBAQQFsDBAgQIECAAAECBAgQIECAAAECBAgQIBAiIIAOYVWUAAECBAgQIECAAAECBAgQIECAAAECBATQ1gABAgQIECBAgAABAgQIECBAgAABAgQIhAgIoENYFSVAgAABAgQIECBAgAABAgQIECBAgAABAbQ1QIAAAQIECBAgQIAAAQIECBAgQIAAAQIhAgLoEFZFCRAgQIAAAQIECBAgQIAAAQIECBAgQEAAbQ0QIECAAAECBAgQIECAAAECBAgQIECAQIiAADqEVVECBAgQIECAAAECBAgQIECAAAECBAgQEEBbAwQIECBAgAABAgQIECBAgAABAgQIECAQIiCADmFVlAABAgQIECBAgAABAgQIECBAgAABAgQE0NYAAQIECBAgQIAAAQIECBAgQIAAAQIECIQICKBDWBUlQIAAAQIECBAgQIAAAQIECBAgQIAAAQG0NUCAAAECBAgQIECAAAECBAgQIECAAAECIQIC6BBWRQkQIECAAAECBAgQIECAAAECBAgQIEBAAG0NECBAgAABAgQIECBAgAABAgQIECBAgECIgAA6hFVRAgQIECBAgAABAgQIECBAgAABAgQIEBBAWwMECBAgQIAAAQIECBAgQIAAAQIECBAgECIggA5hVZQAAQIECBAgQIAAAQIECBAgQIAAAQIEBNDWAAECBAgQIECAAAECBAgQIECAAAECBAiECAigQ1gVJUCAAAECBAgQIECAAAECBAgQIECAAAEBtDVAgAABAgQIECBAgAABAgQIECBAgAABAiECAugQVkUJECBAgAABAgQIECBAgAABAgQIECBAQABtDRAgQIAAAQIECBAgQIAAAQIECBAgQIBAiIAAOoRVUQIECBAgQIAAAQIECBAgQIAAAQIECBAQQFsDBAgQIECAAAECBAgQIECAAAECBAgQIBAiIIAOYVWUAAECBAgQIECAAAECBAgQIECAAAECBATQ1gABAgQIECBAgAABAgQIECBAgAABAgQIhAgIoENYFSVAgAABAgQIECBAgAABAgQIECBAgAABAbQ1QIAAAQIECBAgQIAAAQIECBAgQIAAAQIhAgLoEFZFCRAgQIAAAQIECBAgQIAAAQIECBAgQEAAbQ0QIECAAAECBAgQIECAAAECBAgQIECAQIiAADqEVVECBAgQIECAAAECBAgQIECAAAECBAgQEEBbAwQIECBAgAABAgQIECBAgAABAgQIECAQIiCADmFVlAABAgQIECBAgAABAgQIECBAgAABAgQE0NYAAQIECBAgQIAAAQIECBAgQIAAAQIECIQICKBDWBUlQIAAAQIECBAgQIAAAQIECBAgQIAAAQG0NUCAAAECBAgQIECAAAECBAgQIECAAAECIQIC6BBWRQkQIECAAAECBAgQIECAAAECBAgQIEBAAG0NECBAgAABAgQIECBAgAABAgQIECBAgECIgAA6hFVRAgQIECBAgAABAgQIECBAgAABAgQIEBBAWwMECBAgQIAAAQIECBAgQIAAAQIECBAgECIggA5hVZQAAQIECBAgQIAAAQIECBAgQIAAAQIEBNDWAAECBAgQIECAAAECBAgQIECAAAECBAiECAigQ1gVJUCAAAECBAgQIECAAAECBAgQIECAAAEBtDVAgAABAgQIECBAgAABAgQIECBAgAABAiECAugQVkUJECBAgAABAgQIECBAgAABAgQIECBAQABtDRAgQIAAAQIECBAgQIAAAQIECBAgQIBAiIAAOoRVUQIECBAgQIAAAQIECBAgQIAAAQIECBAQQFsDBAgQIECAAAECBAgQIECAAAECBAgQIBAiIIAOYVWUAAECBAgQIECAAAECBAgQIECAAAECBATQ1gABAgQIECBAgAABAgQIECBAgAABAgQIhAgIoENYFSVAgAABAgQIECBAgAABAgQIECBAgAABAbQ1QIAAAQIECBAgQIAAAQIECBAgQIAAAQIhAgLoEFZFCRAgQIAAAQIECBAgQIAAAQIECBAgQEAAbQ0QIECAAAECBAgQIECAAAECBAgQIECAQIiAADqEVVECBAgQIECAAAECBAgQIECAAAECBAgQEEBbAwQIECBAgAABAgQIECBAgAABAgQIECAQIiCADmFVlAABAgQIECBAgAABAgQIECBAgAABAgQE0NYAAQIECBAgQIAAAQIECBAgQIAAAQIECIQICKBDWBUlQIAAAQIECBAgQIAAAQIECBAgQIAAAQG0NUCAAAECBAgQIECAAAECBAgQIECAAAECIQIC6BBWRQkQIECAAAECBAgQIECAAAECBAgQIEBAAG0NECBAgAABAgQIECBAgAABAgQIECBAgECIgAA6hFVRAgQIECBAgAABAgQIECBAgAABAgQIEBBAWwMECBAgQIAAAQIECBAgQIAAAQIECBAgECIggA5hVZQAAQIECBAgQIAAAQIECBAgQIAAAQIEBNDWAAECBAgQIECAAAECBAgQIECAAAECBAiECAigQ1gVJUCAAAECBAgQIECAAAECBAgQIECAAAEBtDVAgAABAgQIECBAgAABAgQIECBAgAABAiECAugQVkUJECBAgAABAgQIECBAgAABAgQIECBAQABtDRAgQIAAAQIECBAgQIAAAQIECBAgQIBAiIAAOoRVUQIECBAgQIAAAQIECBAgQIAAAQIECBAQQFsDBAgQIECAAAECBAgQIECAAAECBAgQIBAiIIAOYVWUAAECBAgQIECAAAECBAgQIECAAAECBATQ1gABAgQIECBAgAABAgQIECBAgAABAgQIhAgIoENYFSVAgAABAgQIECBAgAABAgQIECBAgAABAbQ1QIAAAQIECBAgQIAAAQIECBAgQIAAAQIhAgLoEFZFCRAgQIAAAQIECBAgQIAAAQIECBAgQEAAbQ0QIECAAAECBAgQIECAAAECBAgQIECAQIiAADqEVVECBAgQIECAAAECBAgQIECAAAECBAgQEEBbAwQIECBAgAABAgQIECBAgAABAgQIECAQIiCADmFVlAABAgQIECBAgAABAgQIECBAgAABAgQE0NYAAQIECBAgQIAAAQIECBAgQIAAAQIECIQICKBDWBUlQIAAAQIECBAgQIAAAQIECBAgQIAAAQG0NUCAAAECBAgQIECAAAECBAgQIECAAAECIQIC6BBWRQkQIECAAAECBAgQIECAAAECBAgQIEBAAG0NECBAgAABAgQIECBAgAABAgQIECBAgECIgAA6hFVRAgQIECBAgAABAgQIECBAgAABAgQIEBBAWwMECBAgQIAAAQIECBAgQIAAAQIECBAgECIggA5hVZQAAQIECBAgQIAAAQIECBAgQIAAAQIEBNDWAAECBAgQIECAAAECBAgQIECAAAECBAiECAigQ1gVJUCAAAECBAgQIECAAAECBAgQIECAAAEBtDVAgAABAgQIECBAgAABAgQIECBAgAABAiECAugQVkUJECBAgAABAgQIECBAgAABAgQIECBAQABtDRAgQIAAAQIECBAgQIAAAQIECBAgQIBAiIAAOoRVUQIECBAgQIAAAQIECBAgQIAAAQIECBAQQFsDBAgQIECAAAECBAgQIECAAAECBAgQIBAiIIAOYVWUAAECBAgQIECAAAECBAgQIECAAAECBATQ1gABAgQIECBAgAABAgQIECBAgAABAgQIhAgIoENYFSVAgAABAgQIECBAgAABAgQIECBAgAABAbQ1QIAAAQIECBAgQIAAAQIECBAgQIAAAQIhAgLoEFZFCRAgQIAAAQIECBAgQIAAAQIECBAgQEAAbQ0QIECAAAECBAgQIECAAAECBAgQIECAQIiAADqEVVECBAgQIECAAAECBAgQIECAAAECBAgQEEBbAwQIECBAgAABAgQIECBAgAABAgQIECAQIvCkqno4HN5//PyLf/zlp59+evHiRUg7ihIgQIAAAQIECBAgQIAAAQIECBAgQIDAfgX+8vdfvP7y9P75s8fHx6urq3qg/y+A/vbbb/c7fCMjQIAAAQIECBAgQIAAAQIECBAgQIAAgSiB6i7nrgD604d3US2rS4AAAQIECBAgQIAAAQIECBAgQIAAAQL7Ffjuu+/6A+iHh4f9ChgZAQIECBAgQIAAAQIECBAgQIAAAQIECEwv8P3331d7bgwKoG9vb6dvX0UCBAgQIECAAAECBAgQIECAAAECBAgQ2KnA9fX1sQD6q50O2bAIECBAgAABAgQIECBAgAABAgQIECBAYGEBAfTCE6B5AgQIECBAgAABAgQIECBAgAABAgQI7FVAAL3XmTUuAgQIECBAgAABAgQIECBAgAABAgQILCwggF54AjRPgAABAgQIECBAgAABAgQIECBAgACBvQoIoPc6s8ZFgAABAgQIECBAgAABAgQIECBAgACBhQUE0AtPgOYJECBAgAABAgQIECBAgAABAgQIECCwVwEB9F5n1rgIECBAgAABAgQIECBAgAABAgQIECCwsIAAeuEJ0DwBAgQIECBAgAABAgQIECBAgAABAgT2KvCkGtjhcHj/8fOnD+8eHh5ub28nHOrNzU1R7e7ubnj9+vSTThlefPSRJ/UqF+geyEllU+cL4bVZjUZ2IgECBAgQIECAAAECBAgQIECAAAECWxG4vr6+urqqQubXX57eP3/2+PhYfVl3fo47oKtUtP6o2mtG0scQ05HDTylKVSeOPneSqU2Z8qljH9i69HkglMMIECBAgAABAgQIECBAgAABAgQIEFhEYI4AetzAUmy9j7t6UwQ/TqP1rJxoH0oT4ihFgAABAgQIECBAgAABAgQIECBAgMDiAnNswZGy0XyXiebeFOmR5v3CHXcQF8Vr0OL46sve4tVZxTHF3LTebty9w0bHrhrHhn9s7Hn30gBPenDxpaYDBAgQIECAAAECBAgQIECAAAECBAjsUmDhLTjqrTCKNPbYvhwpUB5yQEpgOza7yG8NzuPdYleQY+F4vSCK+q0PNrf7SM0Vm4F0b83R+t1jpzSVovf92OUzxKAIECBAgAABAgQIECBAgAABAgQIEIgQmGMLjtbNNPJUunVgvQc0zypy3pO8Ulh86l4Z3Y127H/dfWLHd/MejlA6icXBBAgQIECAAAECBAgQIECAAAECBAgQGC3QswVH867e4S2ljS+a2xM3bzcuDu4+IH23+UnevdYi1QHHHi++1VuquKe7W6aj0frE4WNJDZ3EWJw1fB4dSYAAAQIECBAgsLiAf/Bj8SnQAQIECBAgQIAAgQ6Bji04+gPoc37YPRbRnpScdsTNraFt94PHAujh+W9v/e6A+KQOjBhgb9LtqUKAAAECBAgQILA5gepnvHN+LN/ceHWYAAECBAgQIEBgWwIL7wHdxMo3R26l7D2gOKs4vv7y2D9d2Htw84f71v601sk7duyA7hO7u5fny+N6ta21q7cECBAgQIAAAQIECBAgQIAAAQIECGxXIPYO6O26rLPnJ236sc4h6BUBAgQIECBAgMAIAXdAj0BzCgECBAgQIECAwGwCq7sDeraR76mhc/bj3pODsRAgQIAAAQIECBAgQIAAAQIECBAgsBWBr7bSUf2sNtyoP1AQIECAAAECBAgQIECAAAECBAgQIEBgEwIC6E1Mk04SIECAAAECBAgQIECAAAECBAgQIEBgewIC6O3NmR4TIECAAAECBAgQIECAAAECBAgQIEBgEwIC6E1Mk04SIECAAAECBAgQIECAAAECBAgQIEBgewIC6O3NmR4TIECAAAECBAgQIECAAAECBAgQIEBgEwIC6E1Mk04SIECAAAECBAgQIECAAAECBAgQIEBgewIC6O3NmR4TIECAAAECBAgQIECAAAECBAgQIEBgEwIC6E1Mk04SIECAAAECBAgQIECAAAECBAgQIEBgewIC6O3NmR4TIECAAAECBAgQIECAAAECBAgQIEBgEwIC6E1Mk04SIECAAAECBAgQIECAAAECBAgQIEBgewIC6O3NmR4TIECAAAECBAgQIECAAAECBAgQIEBgEwIC6E1Mk04SIECAAAECBAgQIECAAAECBAgQIEBgewJPqi4fDof3Hz9/+vDu4eHh9vY2H8TNzc3d3V3rsKpv5Y8fO+x8krqhZv1jjxctNg8beGJV55xzC8bWIZyPowKBixWY8BKUnum9F4cJG73YiVv2BWVt7LOtqDNfSdMLYvG63/uUWRu4/hAYITDb87S3bx0/lvee6wACBAgQIECAAAEC0QLX19dXV1dVyPz6y9P7588eHx+rL+tGR94Bnd5zVrlwHYEhhesAAAv7SURBVA0XP533Dqk6fsgpy765TaOrh7NsZ3pJHUDgcgTOvwS1WhVP+eKY9WQQO5vooNlcv9L5A5//lbR+jqRnSvdTZv1ToIcEegXOf572NuEAAgQIECBAgAABArsXGBlAFy5xb0HPr1zk4+eEyOd3ZvfryQAJLCIwz3Mzj97ifudjEcBVNTrPbK5qyHVn4gYeV3mFjLpEIFTAsymUV3ECBAgQIECAAIG9CozcgqMjxs1vEmy9Obp4sHlM/sixz9N8HDs9n7C8t0XPO3pbVW6emGKC6pNjZY/VLArudUkZF4EZBM6/BKWncH4x6X7KF6ekDLrjKT8DxQ6aGDKbrRfk9GDxitA6U+f87WMQ8pCB18F063LNH5z5lTSBpCE0P9nKLARNrrK7ERjyPJ3tAlV1xl9/7mZpGQgBAgQIECBAYH8C02/Bccwo/0XF3jfMxfvqdFNJx9YcRf26G92Ndk9nuqWx9a1yfu6xI4v6vQLeOezvCWZE6xHofQKmZ3rrxaQZqzX/wqy4UrW26Ba5cUui3lCi/iguv0Ou5Mcmt3uux3U19Kzhy7juRvE3ta2Bdd7hc15JWyeoVcNTI3SRKD6/gAvU/OZaJECAAAECBAgQ2I3ANFtwDOHoDV6bocOQskOOSe/Gm7exnPReuuhhb9khfXMMAQLzCPRego51I0+Th18x5hnUzloR3PdOaO8yjnslTWF36zQ1f12pdywOILAtAReobc2X3hIgQIAAAQIECKxKYL4AunfY6Rbj3jfYvaUGHjD8trjhRxZv0Wcby8AhO4wAgdECp14HRjfkRAKjBeZ/JR3dVScSIECAAAECBAgQIECAwIUITBNAT3jLVbNU8bvY4yYmBcHTJsLdZSdkGTdqZxG4EIHQ51po8QuZoOHDHHLBH3LM8BbXc+SEKy3olbTDKv8Fo71O0HqWip4sJTBkbQ85Zqn+a5cAAQIECBAgQIDAUgIjA+h894n8bWfHrhTFCJu/rpveMNffat3Fsqhf1xze6LE+9L5baG23dc66OzNhvrDUitEugTUITHgJan36tz6Rh19/PNNPWiQDL7CtLwp1Q8dePopUtPdSf1K3zz94wmV87KVwhlfSYw6tTyJPjfOXjQozC1zsBWpmZ80RIECAAAECBAjsW+BJNbzD4fD+4+dPH949PDzc3t7mA67eK057y/C+NY2OAIE9CeTx5Z7GtaexmKM9zaaxENiZwOQXKD+W72yFGA4BAgQIECBAYGcC19fXV1dXVcj8+svT++fPHh8fqy/rMY68A3pnQIZDgACBQmBtd8uaIAIECBAgQIAAAQIECBAgQIDAFgUE0FucNX0mQCBcIP1jbuEtaeAMgXqazijgVAIECEQJuEBFyapLgAABAgQIECCwNQEB9NZmTH8JECBAgAABAgQIECBAgAABAgQIECCwEYHl94D+/Ld/bsRKNwkQWEbg17/6ZWrYFWOZOfi51XwiFuyGpgkQIDCDwEpebvILrz2gZ5h3TRAgQIAAAQIECIwW6NgDehUBtFBj9NQ6kcDuBaoIoAig//D73+1+1KEDvL+/f/v27alN/Oa3Lya/Vq8k3+mmuMxRn7o8HE9gBwLFk726QE37cvPy5ctTlYoLrwD6VEDHEyBAgAABAgQIzCkggJ5TW1sECEwpIICeUvPnWnUA/ebNm+GVX716FRRATx7vDh/UkCOL5TfklN5jJk+1elt0AAECvQJ//NOfZwigz7zwCqB759EBBAgQIECAAAECCwp0BNBr2QP65uYu/TlfKq9WfV4VrP874mP0iSPacgoBAicJPHnyP/nxxZfVt+pH8v+eU/+kc5sHV93I/xyr1hzFme12nP6vYR9xHVCZAAEClyYw7Lr7r0tjMV4CBAgQIECAAIF9C6wlgK6U7+5u6j/dme/ARDhVqz6pi+97Io2OAIEkkDLcw+G/04P554tYVR2o+5A+WaQbeaOHYR+L91MHCBDYrkD6i7f8El0/WAwqPRJ0yvCyodrDrruH0D4oToAAAQIECBAgQGBmgRUF0GnkvRn0zEaaI0CAwC4F5CC7nFaDIrAegSrzrf/KrfqTfhmleKQZQ0ecMqInQYwuvEGwyhIgQIAAAQIECKxZYI0BdOHV3Joj3QQ9fNeO4pTURGvx+sE1T5u+ESDQLdDcdiM9UtwEN+SeuOYxdet5zdSfYwcf63BH8dabBCecejnIhJhKESBAYIiAC+8QJccQIECAAAECBAjsTGADAXRza460n0bHrh2t2XT1YL7LR/oyv+d64E4gO1sHhkNgZwLHNtxIN9al8XbcapdS5o779dJddfm+H/ntfr1B+bHi3TcJTjJffx32MUlbihAgQKBDoL6WnkQ04pST6gcdPOy6+9eg1pUlQIAAAQIECBAgsIjABgLojtucO76VcuScNQXNzS2h0yPD76peZMI0SoDA+QJ5bHHqDctF683E5NSCC94B/e9hH+eDq0CAAAECtcCw6+6/cREgQIAAAQIECBDYk8DaA+j8JuXCveNbHTPUvcH0uJp7WhDGQmD3AkX63Lwn+hyBfJvRgXVSB/Ise0Sdgc3lh6Uc5L/aPtJ3R1R2CgECBIYLjLiXecQpw/sTeqQLbyiv4gQIECBAgAABAusUWGMAXafAEV71zs6tGbRNnyPA1SSwNoE1ZxZpE4/Z0FIO8vHjx6LR6hEB9GwToSECBC5HwIX3cubaSAkQIECAAAECBJLAigLotPdFnj7XYXH+rwLm22icul1GqlY3kRdvPmKVECCwcoHqluG0f0WeLNePH+t8vuVFXqE+vvuR3i1Km6d3G+bH58VPrTNupvJ/C+uHH35IRarP82+NK+4sAgQIDBEY8feCI04Z0pN5jnHhncdZKwQIECBAgAABAqsSePJz4HJ4//Hzpw/vHh4ebm9v8/79X/p7dxfa489/++evf/XL0CYUJ0BguwLFJaL68g+//912h7OGnt/f3799+/bNmzc//vhj0Z9vvvnmw4cPxYNff/31q1evfvPbF5Nfq9d//Y/ooTW8hmeBPswmkP8DrXWjxSPNNDnilGa7xSN//NOfi0vc5E/Vly9fnnnhneHH8tkWhoYIECBAgAABAgT2J3B9fX11dVWFzK+/PL1//uzx8bH68j/vAqr/CaD3N+VGRGA3AgLoyacyBdDDKwugh1v1Hjl5qtXbogMIEOgVmC2A7u1JOqB54RVAD9dzJAECBAgQIECAwPwCAuj5zbVIgMA0AgLoaRyzKnUAfWpZd0CfKnbseAH0VJLqEJhQYJ4A+tQOFxdeAfSpgI4nQIAAAQIECBCYU2DtAfScFtoiQGBzAvmvRVfh3eb6v5sOR2zBsX6cyxz1+udFDwlMLtDcgmPyJkYUzHslgB4B6BQCBAgQIECAAIHZBFYdQM+moCECBAgQIECAAAECGxUQQG904nSbAAECBAgQIHAhAh0B9FcXQmCYBAgQIECAAAECBAgQIECAAAECBAgQIDCzwJOqve5/hHDmDmmOAAECBAgQIECAAIFC4O7ujgkBAgQIECBAgACB1QqM34JjtUPSMQIECBAgQIAAAQIECBAgQIAAAQIECBBYg4AtONYwC/pAgAABAgQIECBAgAABAgQIECBAgACByxKwB/RlzbfREiBAgAABAgQIECBAgAABAgQIECBAYDYBAfRs1BoiQIAAAQIECBAgQIAAAQIECBAgQIDAZQkIoC9rvo2WAAECBAgQIECAAAECBAgQIECAAAECswkIoGej1hABAgQIECBAgAABAgQIECBAgAABAgQuS0AAfVnzbbQECBAgQIAAAQIECBAgQIAAAQIECBCYTUAAPRu1hggQIECAAAECBAgQIECAAAECBAgQIHBZAgLoy5pvoyVAgAABAgQIECBAgAABAgQIECBAgMBsAgLo2ag1RIAAAQIECBAgQIAAAQIECBAgQIAAgcsSEEBf1nwbLQECBAgQIECAAAECBAgQIECAAAECBGYTEEDPRq0hAgQIECBAgAABAgQIECBAgAABAgQIXJaAAPqy5ttoCRAgQIAAAQIECBAgQIAAAQIECBAgMJuAAHo2ag0RIECAAAECBAgQIECAAAECBAgQIEDgsgT+F/iSrCIT1M7aAAAAAElFTkSuQmCC)

