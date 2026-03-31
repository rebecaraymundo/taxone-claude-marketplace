# MTZ_Monitor_Tributos_Pagar_Tela_Layout

- **Fonte:** MTZ_Monitor_Tributos_Pagar_Tela_Layout.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 90 KB

---

THOMSON REUTERS

Parametrização do Layout

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS3962

Parametrização do Layout

Essa tela tem por objetivo permitir que o usuário defina a estrutura do arquivo TXT que irá ser gerado para o sistema ERP do cliente\.

OS3962\-A

Parametrização do Layout  

Inclusão dos campos Data Inicial e Final de Validade\.

Atualização do Grupo Tributo e Tributo para que demonstrem apenas as informações referentes ao municipal\.

Inclusão de tratamento na tela para que não permita edição do layout e dos parâmetros de seleção para layouts cujo arquivo já tenha sido gerado e que esteja com status “Pago”\.

OS3962\-B

Parametrização do Layout

Inclusão da opção “Federal” no campo “Grupo Tributo” e das opções “IRPJ”, “IRRF”, “PIS”, “COFINS” e “CSLL” no campo “Tributo da tela de parametrização de layout\.

OS3962\-C

Parametrização do Layout

Inclusão da opção “Previdenciário” no campo “Grupo Tributo” e da opção “INSS” no campo “Tributo da tela de parametrização de layout\.

OS3962\-D

Parametrização do Layout

O objetivo deste documento de requisito é definir a solução funcional para a geração dos arquivos de retorno ao ERP realizados pelo módulo Monitor de Tributos, no formato XML\. Atualmente, essa geração ocorre somente no formato texto\.

A geração deverá abranger os tributos especificados nas OS’s da família 3962, especificamente das autarquias Federal, Previdenciário e Municipal\. Os tributos relacionados ao fisco Estadual não fazem parte do escopo dessa OS\.

MFS\-1685

Parametrização de Layout

Atualização da tela Layout do Arquivo para que demonstre o imposto IPI

MFS\-1683

Parametrização de Layout

Atualização da tela Layout do Arquivo para que demonstre o imposto ICMS

MFS\-1686

Parametrização de Layout

Atualização da tela Layout do Arquivo para que demonstre os impostos PIS/PASEP e COFINS

MFS\-1684

Parametrização de Layout

Atualização da tela Layout do Arquivo para que demonstre o imposto ICMS\-ST

MFS\-1687

Ajuste na tela

Inclusão dos Botões “Definir Layout Retorno” e Painel, dos Labels “Layout de Envio” e Layout de Retorno\.

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

[1\.	TELA A SER DESENVOLVIDA	4](#_Toc373746056)

[1\.1\.	Diagrama de Casos de Uso	4](#_Toc373746057)

[1\.1\.1\.	UC001 – Manutenção da Estrutura Padrão	4](#_Toc373746058)

[1\.1\.1\.1\.1\.	Fluxo Principal	5](#_Toc373746059)

[1\.1\.1\.1\.2\.	Fluxo Alternativo 1 – Novo Registro	5](#_Toc373746060)

[2\.	Regras dos Campos	5](#_Toc373746061)

# <a id="_Toc373746056"></a>TELA A SER DESENVOLVIDA

\[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir\]

## <a id="_Toc350763243"></a><a id="_Toc373746057"></a>Diagrama de Casos de Uso 

__ __

__UC Estrutura Padrão__

__Usuário __

__UC001 – Manutenção da   __

__Estrutura Padrão__

Manutenção Padrão

## <a id="_Toc350763244"></a><a id="_Toc373746058"></a>UC001 – Manutenção da Estrutura Padrão

\[Descrever a ação deste caso de uso\. 

Ex\.: Este caso de uso descreve o processo de Cadastro de Estrutura Padrão\.\]

__Documentação do Caso de Uso__

__Ator Principal__

Usuário do Sistema\.

__Pré\- Condições__

Estar logado no produto MasterSAF DW\.

__Pós\-Condições__

Não se aplica\.

<a id="_Toc332809652"></a><a id="_Toc332888915"></a><a id="_Toc350763245"></a>

### <a id="_Toc373746059"></a>Fluxo Principal 

__Ações do Ator__

__Ações do Sistema__

### <a id="_Toc373746060"></a><a id="_Toc332809666"></a><a id="_Toc332888929"></a><a id="_Toc350763246"></a>Fluxo Alternativo 1 – Novo Registro

__Ações do Ator__

__Ações do Sistema__

__Fim do fluxo Alternativo__

<a id="_Toc350763252"></a>

# <a id="regras_campos"></a><a id="_Toc373746061"></a>Regras dos Campos 

__Localização da tela:__ Parâmetros >> Layout do Arquivo

__Título da tela: __Parametrização de Layout

__Regra geral de funcionamento da tela__:

- Através desta tela será possível definir o formato em que os arquivos de retorno para o ERP serão gerados\. Ela é pré\-requisito para extração dos dados da base;
- Na primeira parametrização todos os campos estarão disponíveis para edição, porém, a partir do momento que o arquivo for gerado e pago não será possível editar as informações aqui incluídas\. Isso para garantir o vínculo do que foi gerado e já pago e será possível de controlar através da tela de Status dos Arquivos Gerados\. Se no Status do layout parametrizado houver pelo menos um registro com status diferente de “Cancelado”, os campos relacionados à Parametrização do Layout e aos Parâmetros de Seleção devem ficar desabilitados para edição\.
- As informações da tela serão armazenadas considerando os campos "Status do Layout", "Código do Layout", "Grupo Tributo/Tributo" e "Lista de Tributos", não podendo existir duplicidade destas informações\. Caso exista tentativa de inserção de registros com estes mesmos critérios, retornar a mensagem ao usuário: "Não é possível cadastrar layouts com os mesmos critérios de Status do Layout, Código do Layout e Grupo Tributo/Tributo"\.
- O cliente poderá inserir arquivos no formato TXT \(texto\) ou XML\.

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

OS3962\-A

Código/Descrição do Tipo do Arquivo

Pasta

S

S

Deverá recuperar os códigos de tipo de arquivo cadastrados no menu: Parâmetros >> Tipo de Arquivo do módulo Monitor de Tributos a Pagar

Obs: Deverá existir tratamento para não exibir a opção “Arquivo XML”\.

OS3962

OS3962D

Tipo do Arquivo

Lista

S

N

Esse campo será preenchido de acordo com o campo “Código/Descrição do Tipo do Arquivo”\. Caso o arquivo seja do tipo “TXT” e com o código selecionado, será exibida uma das opções abaixo:

- Texto com Largura Fixa
- Texto com Delimitador

OS3962

Código do Layout

Texto

S

S

Alfanumérico \(3\)

OS3962

Descrição do Layout

Texto 

S

S

Alfanumérico \(50\)

OS3962

Grupo Tributo/Tributo

Lista

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

OS3962

OS3962\-B

OS3962\-C

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

Caso o campo “Lista de Tributos” não esteja preenchido, deve ser exibida a seguinte mensagem de erro: “Informe Tributo“\.A lista de layout\(s\) deverá estar vazia\.

OS3962

OS3962\-B

MFS\-1685

MFS\-1683

MFS\-1686

MFS\-1684

MFS\-6310

Duplicar Layout

Botão

N

N

Ao clicar nesse botão, o sistema irá copiar para um novo registro todas as informações do layout que estiver sendo visualizado, com exceção do Código e a Descrição do Layout, que deverá ser informado pelo usuário\.

Caso o usuário tente salvar o registro sem fazer alterações em ao menos um dos campos: Grupo Tributo, Tributo, Parametrização do Layout ou Parâmetros de Seleção, mesmo que tenha código de layout distinto, não permitir a gravação e retornar a mensagem: “Registro já possui as informações Grupo Tributo, Tributo, Layout e Parâmetros de Seleção cadastradas\. Por gentileza alterar” e não deve incluir o novo registro\.

Obs: Quando acionado o botão “Definir Layout de Retorno” este deverá ser desabilitado\. Funcionalidade deste botão ativa apenas para o layout de envio\.

OS3962

MFS\-1687

Definir Layout de Retorno

Botão

N

N

Default: Desabilitado

Ao clicar nesse botão o sistema deverá criar um layout de retorno igual ao layout de envio parametrizado pelo usuário, porém, desabilitado, ou seja, não será possível qualquer edição, inclusão ou exclusão de campo\.

Os campos “Conteúdo Fixo”, “Conteúdo Variável” e “Parâmetros de Seleção” não farão parte do layout\. Este layout terá novos campos \(fixos\) serão eles: 

Valor Total: Numérico, 17,2

Valor de Juros: \(Numérico\), 17,2,

Valor de Multa: \(Numérico\), 17,2  

Data de Pagamento: \(Data\), 8, decimal não será preenchido\.

Estes campos serão desabilitados para edição, posição inicial seguirá o sequencial do campo anterior\.

Terá também o campo, \(último campo do layout\) com descrição “Autent\. Bancaria”, também desabilitado para qualquer edição, alfanumérico, posição inicial seguirá o sequencial do campo anterior e posição final não será preenchido, assim como tamanho e decimais\.

Obs: Este botão só será habilitado após utilização do layout de envio\.

Botão dinâmico, quando acionado será alterado para “Verificar Layout de Envio”\.

MFS\-1687

MFS\-5047

Layout de Envio 

Texto

N

N

Quando acionado o botão “Definir Layout Retorno”, este label deverá ser alterado para “Layout de Retorno”, ou seja, campo dinâmico\.

MFS\-1687

__Parametrização do Layout__

Ordem do Campo

Texto

S

N

Alfanumérico \(3\)

Campo autoincremental\. Irá gerar uma sequência numérica, iniciando em 1\.

OS3962

Descrição do Campo

Texto

S

S

Alfanumérico \(100\)

OS3962

Tipo do Campo

Lista

S

S

Lista com as opções \(default: não preenchido\)

Preencher conforme abaixo:

- Alfanumérico
- Data \(DDMMAAAA\)
- Data \(MMDDAAAA\)
- Data \(AAAADDMM\)
- Data \(AAAAMMDD\)
- Data \(MMAAAADD\)
- Numérico

OS3962

Posição Inicial

Texto

S

N

Alfanumérico

O primeiro registro incluído, o valor inicial desse campo é “1”\.

Esse campo não poderá ser alterado, pois seu conteúdo irá variar de acordo com o campo “Tamanho”\.

OS3962

Posição Final

Texto

S

N

Alfanumérico

Esse campo não poderá ser alterado, pois seu conteúdo irá variar de acordo com o campo “Tamanho”\.

Caso o campo “Tipo do Campo” seja do tipo Data, esse campo deverá ficar desabilitado e não poderá ser preenchido\.

OS3962

Tamanho

Texto

S

S

Numérico \(5\)

Ao informar o tamanho, o conteúdo dos campos “Posição Inicial” e “Posição Final” será alterado\.

Caso o campo “Tipo do Campo” seja do tipo Data, esse campo deverá ficar desabilitado e não poderá ser preenchido\.

OS3962

Decimal

Numérico

N

S

Numérico \(1\)

Esse campo irá definir se o campo terá casas decimais ou não\. Esse campo só ficará habilitado caso o campo “Tipo do Campo” seja “Numérico”\.

Obs: Caso o campo Dec\_Col\_Bd da TFIX140 estiver preenchido com conteúdo maior que zero o campo decimal deverá ser habilitado, caso contrário o campo deverá ficar desabilitado\.

OS3962/

MFS\-5052

Conteúdo Fixo

Texto

S

S

Alfanumérico \(50\)

O campo deverá possuir a mesma quantidade de caracteres informada no campo “Tamanho”\.

O sistema não deverá aceitar que o conteúdo desse campo, seja diferente do definido no campo “Tipo de Campo”\. Exemplo: caso o “Tipo de Campo” seja “Numérico” o sistema deverá exibir mensagem de erro padrão informando essa situação\.

OS3962

OS3962\-A

OS3962\-C

Conteúdo Variável

Pasta

S

S

As informações dos campos a serem selecionados serão recuperadas das seguintes tabelas de acordo com o Tributo selecionado:

- ISS = GPE\_FECHAMENTO\_ISS
- INSS = IRT\_GPS
- IPI = ITEM\_APURAC\_CALC
- PIS/PASEP \(PRÓPRIO\) = EPC\_REG\_AJT\_M200\_M600\(Registro M200\)
- COFINS \(PRÓPRIO\) = EPC\_REG\_AJT\_M200\_M600\(\(Registro M600\)
- Ao exibir os campos para seleção, o sistema só deverá exibir os campos de acordo com o formato definido no campo “Tipo do Campo”, conforme definição abaixo:
- Alfanumérico
	- Só serão exibidos os campos da TFIX140 que sejam do tipo Alfanumérico para o Tributo escolhido\.
- Data \(DDMMAAAA\)
	- Só serão exibidos os campos da TFIX140 que sejam do tipo Data para o Tributo escolhido\.
- Data \(MMDDAAAA\)
	- Só serão exibidos os campos da TFIX140 que sejam do tipo Data para o Tributo escolhido\.
- Data \(AAAADDMM\)
	- Só serão exibidos os campos da TFIX140 que sejam do tipo Data para o Tributo escolhido\.
- Data \(AAAAMMDD\)
	- Só serão exibidos os campos da TFIX140 que sejam do tipo Data para o Tributo escolhido\.
- Data \(MMAAAADD\)
	- Só serão exibidos os campos da TFIX140 que sejam do tipo Data para o Tributo escolhido\.
- Numérico
	- Só serão exibidos os campos da TFIX140 que sejam do tipo Numérico para o Tributo escolhido\.

OS3962

OS3962\-C

MFS\-1685

MFS\-1683

MFS\-1686

MFS\-1684

MFS\-6310

\* Limpar

Botão

N

N

Função de limpar o campo “Conteúdo Variável”\.

OS3962\-D

Agrupado

Checkbox

N

S

Default: não habilitado e não selecionado

Este campo deve ser habilitado para seleção quando o formato do campo indicado em conteúdo variável for do tipo “Numérico”\. Quando selecionado, indica que o campo apontado como “Agrupado” será somado e as informações serão consolidadas na geração do arquivo\.

OS3962\-A

__Parâmetros de Seleção__

Conteúdo Variável

Pasta

N

S

Alfanumérico \(100\)

Nesse campo, o usuário irá escolher os campos como parâmetros de seleção\. Obrigatoriamente deve existir ao menos um conteúdo variável do tipo Data e que tenha Condição igual a "Utilizado na tela"\. Caso o usuário não informe nenhum, não permitir a gravação do layout e retornar a mensagem: "É necessário haver ao menos 1 Conteúdo Variável do tipo Data e com a Condição igual a Utilizado na Tela\. Favor corrigir"\.

OS3962

Condição

Lista

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

OS3962

Grupo

Pasta

S

N

Default: não preenchido

Nesse campo, o usuário irá selecionar o Grupo ao qual pertence o campo informado no campo “Conteúdo Variável”\.

OS3962\-A

Conteúdo Fixo

Texto

S

S

Alfanumérico \(50\)

Caso o campo seja preenchido com um conteúdo acima do valor máximo de caracteres, será exibida mensagem de erro informando o cliente e esse registro não será gravado\.

OS3962

Grupo

Lista

N

S

Lista com as opções \(default: não preenchido\)

Preencher conforme abaixo:

- E
- Ou

OS3962

*\* Descrição não disponível em tela*

 

