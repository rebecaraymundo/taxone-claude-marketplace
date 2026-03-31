# MTZ_Monitor_Tributos_Pagar_Tela_Geracao_Arquivo_Tributos_Apurados

- **Fonte:** MTZ_Monitor_Tributos_Pagar_Tela_Geracao_Arquivo_Tributos_Apurados.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 81 KB

---

    

THOMSON REUTERS

Geração do Arquivo de Tributos Apurados

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS3962\-A

Geração do Arquivo de Impostos Apurados

O objetivo deste documento de requisito é especificar a geração do arquivo de impostos apurados, com base no layout especificado na OS3962\.

OS3962\-B

Geração do Arquivo de Impostos Apurados 

Inclusão da opção “Federal” no campo “Grupo Tributo” e das opções “IRPJ”, “IRRF”, “PIS”, “COFINS” e “CSLL” no campo “Tributo da tela de parametrização de layout\.

OS3962\-C

Geração do Arquivo de Impostos Apurados

Inclusão da opção “Previdenciário” no campo “Grupo Tributo” e da opção “INSS” no campo “Tributo” da tela de parametrização de layout\.

OS3888\-B1

Municipal \- Gerenciador ISS \- Retorno dos Impostos Apurados para o SAP

Ajuste do campo Grupo Tributo para que demonstre somente a opção Municipal, no módulo Gerenciador de ISS\.

MFS\-1685

Geração do Arquivo de Impostos Apurados

Atualização da Tela Arquivos de Tributos Apurados para que demonstre o imposto IPI

MFS\-1683

Geração do Arquivo de Impostos Apurados

Atualização da Tela Arquivos de Tributos Apurados para que demonstre o imposto ICMS

MFS\-1686

Geração do Arquivo de Impostos Apurados

Atualização da Tela Arquivos de Tributos Apurados para que demonstre os impostos PIS/PASEP  e COFINS

MFS\-1684

Geração do Arquivo de Impostos Apurados

Atualização da Tela Arquivos de Tributos Apurados para que demonstre o imposto ICMS\-ST

MFS\-2830

Geração do Arquivo de Impostos Apurados

Inclusão do Campo “Cód\./ Desc\. Tipo de Arquivo”\.

MFS\-3267

Geração do Arquivo de Impostos Apurados

Alteração do campo Layout, este passará a ser do tipo dropdown\.

MFS\-3273

Geração do Arquivo de Impostos Apurados

Inclusão dos campos: “Tipo de Geração” e “Perfil”

MFS\-6310

Geração do Arquivo de Impostos Apurados

Retirar os impostos ICMS e ICMS\-ST 

Sumário

[1\.	TELA A SER DESENVOLVIDA	3](#_Toc370116862)

[1\.1\.	Diagrama de Casos de Uso	3](#_Toc370116863)

[1\.1\.1\.	UC001 – Manutenção da Estrutura Padrão	3](#_Toc370116864)

[1\.1\.1\.1\.1\.	Fluxo Principal	4](#_Toc370116865)

[1\.1\.1\.1\.2\.	Fluxo Alternativo 1 – Novo Registro	4](#_Toc370116866)

[2\.	Regras dos Campos	4](#_Toc370116867)

# <a id="_Toc370116862"></a>TELA A SER DESENVOLVIDA

\[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir\]

## <a id="_Toc350763243"></a><a id="_Toc370116863"></a>Diagrama de Casos de Uso 

__ __

__UC Estrutura Padrão__

__Usuário __

__UC001 – Manutenção da   __

__Estrutura Padrão__

Manutenção Padrão

## <a id="_Toc350763244"></a><a id="_Toc370116864"></a>UC001 – Manutenção da Estrutura Padrão

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

### <a id="_Toc370116865"></a>Fluxo Principal 

__Ações do Ator__

__Ações do Sistema__

### <a id="_Toc370116866"></a><a id="_Toc332809666"></a><a id="_Toc332888929"></a><a id="_Toc350763246"></a>Fluxo Alternativo 1 – Novo Registro

__Ações do Ator__

__Ações do Sistema__

__Fim do fluxo Alternativo__

<a id="_Toc350763252"></a>

# <a id="regras_campos"></a><a id="_Toc370116867"></a>Regras dos Campos 

__Localização da tela:__ Geração >> Arquivo de Tributos Apurados

__Título da tela: __Arquivo de Tributos Apurados

__Regra geral de funcionamento da tela__:

- Esta tela será utilizada para gerar os arquivos no formato parametrizado pelo usuário na tela de Parametrização do Layout;
- Quando o usuário clicar para gerar o arquivo, se um dos campos obrigatórios \(coluna Obrig = S\) não estiver parametrizado, retornar a mensagem: “Campo obrigatório não parametrizado” e posicionar o cursor sobre o campo que precisa ser indicado\. Se existir mais de um campo, posicionar o cursor sobre o primeiro campo não parametrizado;

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Data Inicial

Data

S

S

A data deverá ser informada no formato dd/mm/aaaa\. Por default não estará preenchida\.

Caso o campo não esteja preenchido, deve ser exibida a mensagem de erro: “Informe Data Inicial”\.

OS3962\-A

Data Final

Data

S

S

A data deverá ser informada no formato dd/mm/aaaa\. Por default não estará preenchida\.

A Data Final informada deve ser maior ou igual a Data Inicial\. Caso seja informada uma data menor, retornar a mensagem: “Data Final deve ser maior ou igual a Data Inicial”\.

Caso o campo não esteja preenchido, deve ser exibida a mensagem de erro: “Informe Data Final”\.

Caso a Data Final seja menor do que a Data Inicial deve ser exibida a seguinte mensagem de erro: “A Data Final deve ser maior ou igual a Data Inicial”\.

OS3962\-A

Tipo de Geração

Radio Button

S

S

Default selecionado: Layout

Permite ao usuário definir se a geração será por “Perfil” ou “Layout”

- Perfil

Quando selecionada esta opção, o usuário irá definir que a geração será por perfil, conforme parametrização realizada na tela de “Perfil de Geração”\. 

Obs: Os campos “Grupo Tributo”, “Tributo”,“Cód\./ Desc\. Tipo de Arquivo” e Layout deverão ser desabilitados\. 

- Layout

Quando selecionada esta opção, o usuário irá definir que a geração será por Layout, conforme parametrização realizada na tela de “Layout por Estabelecimento”\.

Obs:  O campo “Perfil” deverá ser desabilitado\.

MFS\-3273

Grupo Tributo

Lista

S

S

Lista com as opções \(default: não preenchido\)

Preencher conforme abaixo:

1 – Federal

2 – Estadual 

3 – Municipal 

4 – Previdenciário

Caso a tela seja acionada através do módulo Gerenciador de ISS, o campo deve demonstrar somente a opção: 

- Municipal

Caso o campo nao esteja preenchido, deverá ser exibida a seguinte mensagem: “Informe Grupo Tributo”\.

Obs: Não serão apresentados os respectivos “números” dos tributos, apenas a descrição\. Estes números serão a referencia para o campo “grupo\_tributo” da TFIX140\.

OS3962\-A

OS3962\-B

OS3888\-B1

MFS\-1683

Tributo

Lista

S

S

Lista com as opções \(default: desabilitado e não preenchido\)

Será habilitado quando for indicado o Grupo Tributo, demonstrando as seguintes informações:

Para o Grupo Tributo Federal:

- IRPJ
- IRRF
- CSLL
- PIS/PASEP
- COFINS
- IPI
- PIS/PASEP \(PRÓPRIO\)
- COFINS \(PRÓPRIO\)

MFS\-6310

Para o Grupo Tributo Municipal:

- ISS

Para o Grupo Tributo Previdenciário:

- INSS

Caso o campo não esteja preenchido, deve ser exibida mensagem de erro: “Informe Tributo”\.

OS3962\-A

OS3962\-B

MFS\-1685

MFS\-1683

MFS\-1686

MFS\-1684

MFS\-6310

Cód\./ Desc\. Tipo de Arquivo

Dropdown

S

S

Serão exibidos os códigos conforme cadastro na tela “Tipo de Arquivo” caminho \(Módulo: Gestão Estratégica >> Monitor de Tributos / Menu: Parâmetros\)\.

Caso não preenchido exibir a seguinte mensagem: “Cód\./Desc Tipo de Arquivo deve ser informado”\.

Obs: Os códigos dos layouts deverão ser listados conforme filtro por Grupo e Tributo\.

MFS\-2830

Layout

Dropdown

S

S

Serão exibidos todos os layouts cadastrados no sistema, de acordo com os parâmetros de seleção em tela: Grupo Tributo, Tributo, Cód\. Desc\. Tipo de Arquivo\. Caso não preenchido exibir a seguinte mensagem: “Informe o Layout”

Obs: Devem ser apresentados os layouts cujo o campo “Status do Layout” esteja “ativo” no caminho: Monitor de tributos a pagar Menu: Parâmetros >> Layout do Arquivo\.

Quando selecionada a opção “Layout”, no campo “Tipo de Geração”, serão exibidos os layouts conforme parametrização da tela de “Layout por Estabelecimento”, respeitando o filtro dos parâmetros de seleção em tela\. 

Obs:

Se não houver parametrização na tela de layout por estabelecimento, serão apresentados os layout conforme parametrização das telas de Layout respeitando o filtro dos parâmetros de seleção em tela\.

Caso não preenchido exibir a seguinte mensagem: “Layout deve ser informado”\.

MFS\-3273

Perfil

Dropdown

S

S

Deverão ser listados os perfis conforme parametrização na tela de “Perfil de Geração”\.

Obs:

Caso não preenchido deverá ser exibida a seguinte mensagem: “Perfil deve ser informado”

MFS\-3273

\-Realizar quebra do arquivo por Estabelecimento

Checkbox

N

S

\(Default: não selecionado\)

Esse parâmetro caso selecionado pelo usuário, irá definir que será gerado um arquivo por estabelecimento selecionado, caso contrário será gerado um único arquivo com as informações de todos os estabelecimentos, assim parametrizado\.

OS3962\-A

MFS\-3267

Estabelecimento\(s\)

Checkbox

S

S

O usuário deverá selecionar através dos checkbox os Estabelecimentos para geração do arquivo de impostos apurados\.

 Caso selecionado a opção “Layout” no campo “Tipo de Geração”, serão exibidos os estabelecimentos conforme parametrização na tela de “Layout por Estabelecimento”\.

Obs: 

__Geração por Perfil:__ Não serão listados estabelecimentos, neste caso, o Label “Estabelecimento\(s\)” deverá ser retirado\.

__Geração por Layout: __Se não houver parametrização na tela de “Layout por Estabelecimento” deverão ser listados todos os estabelecimentos para empresa logada e permissão do usuário\.

Se nenhum estabelecimento for selecionado, deverá ser exibida a mensagem: “Selecione ao menos uma opção em Estabelecimento\(s\)”\.

OS3962\-A

MFS\-3267

MFS\-3273

