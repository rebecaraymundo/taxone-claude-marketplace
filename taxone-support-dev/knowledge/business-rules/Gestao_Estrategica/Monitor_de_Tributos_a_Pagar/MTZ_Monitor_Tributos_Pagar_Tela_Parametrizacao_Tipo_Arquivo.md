# MTZ_Monitor_Tributos_Pagar_Tela_Parametrizacao_Tipo_Arquivo

- **Fonte:** MTZ_Monitor_Tributos_Pagar_Tela_Parametrizacao_Tipo_Arquivo.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 155 KB

---

THOMSON REUTERS

Parametrização do Tipo de Arquivo

<>

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS3962

Parametrização do Tipo de Arquivo

Essa tela tem por objetivo permitir que o usuário defina as condições padrões de estrutura do arquivo que será gerado pelo módulo Monitor de Tributos a Pagar\.

OS3962\-D

Parametrização do Tipo de Arquivo

O objetivo deste documento de requisito é definir a solução funcional para a geração dos arquivos de retorno ao ERP realizados pelo módulo Monitor de Tributos, no formato XML\. Atualmente, essa geração ocorre somente no formato texto\.

A geração deverá abranger os tributos especificados nas OS’s da família 3962, especificamente das autarquias Federal, Previdenciário e Municipal\. Os tributos relacionados ao fisco Estadual não fazem parte do escopo dessa OS\.

MFS\-2900

Parametrização do tipo de Arquivo

Definição do separador para o tipo do arquivo texto com delimitador

Sumário

[1\.	TELA A SER DESENVOLVIDA	3](#_Toc373227401)

[1\.1\.	Diagrama de Casos de Uso	3](#_Toc373227402)

[1\.1\.1\.	UC001 – Manutenção da Estrutura Padrão	3](#_Toc373227403)

[1\.1\.1\.1\.1\.	Fluxo Principal	4](#_Toc373227404)

[1\.1\.1\.1\.2\.	Fluxo Alternativo 1 – Novo Registro	4](#_Toc373227405)

[1\.1\.1\.1\.3\.	Fluxo Alternativo 2 – Abrir Registros	4](#_Toc373227406)

[1\.1\.1\.1\.4\.	Fluxo Alternativo 3 – Excluir Registros	5](#_Toc373227407)

[1\.1\.1\.1\.5\.	Fluxo Alternativo 4 – Imprimir Registros	5](#_Toc373227408)

[1\.1\.1\.1\.6\.	Fluxo Alternativo 5 – Visualizar Relatórios de Conferência	5](#_Toc373227409)

[2\.	Regras dos Campos	6](#_Toc373227410)

# <a id="_Toc373227401"></a>TELA A SER DESENVOLVIDA

\[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir\]

## <a id="_Toc350763243"></a><a id="_Toc373227402"></a>Diagrama de Casos de Uso 

__ __

__UC Estrutura Padrão__

__Usuário __

__UC001 – Manutenção da   __

__Estrutura Padrão__

Manutenção Padrão

## <a id="_Toc350763244"></a><a id="_Toc373227403"></a>UC001 – Manutenção da Estrutura Padrão

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

### <a id="_Toc373227404"></a>Fluxo Principal 

__Ações do Ator__

__Ações do Sistema__

O Usuário do Sistema acessa a tela de Parametrização do Tipo de Arquivo\.

O sistema disponibiliza a tela de Parametrização do Tipo de Arquivo com todos os campos não preenchidos\. O usuário deverá informar os dados a serem cadastrados de acordo com as [regras dos campos](#regras_campos)\.

O Usuário do Sistema preenche os campos e solicita a gravação das informações\.

__<<Fluxo Alternativo 1>>__

__<<Fluxo Alternativo 2>>__

__<<Fluxo Alternativo 5>>__

O sistema grava as informações\.

### <a id="_Toc373227405"></a><a id="_Toc332809666"></a><a id="_Toc332888929"></a><a id="_Toc350763246"></a>Fluxo Alternativo 1 – Novo Registro

__Ações do Ator__

__Ações do Sistema__

O usuário clica no botão “Novo”\.

O sistema limpa os campos e disponobiliza um novo registro para ser incluído\. Caso existam dados digitados que ainda não foram salvos, o sistema exibe a seguinte mensagem de erro: “Deseja gravar modificações?”\. Caso o usuário selecione a opção “Sim”, o registro prévio é gravado\. Caso selecione a opção “Não”, o registro é descartado\. Caso o usuário selecione a opção “Cancelar”, a operação será desfeita\.

__Fim do fluxo Alternativo__

### <a id="_Toc373227406"></a>Fluxo Alternativo 2 – Abrir Registros

__Ações do Ator__

__Ações do Sistema__

O usuário clica no botão “Abre”\.

__<<Fluxo Alternativo 3>>__

__<<Fluxo Alternativo 4>>__

O sistema apresenta os registros cadastrados, de acordo com os parâmetros informados\.

__Fim do fluxo Alternativo__

### <a id="_Toc373227407"></a>Fluxo Alternativo 3 – Excluir Registros

__Ações do Ator__

__Ações do Sistema__

O usuário clica no botão “Exclui”\.

O sistema exclui o registro selecionado pelo Usuário do Sistema\.

__Fim do fluxo Alternativo__

### <a id="_Toc373227408"></a>Fluxo Alternativo 4 – Imprimir Registros

__Ações do Ator__

__Ações do Sistema__

O usuário clica no botão “Imprime”\.

O sistema imprime o registro selecionado pelo Usuário do Sistema\.

__Fim do fluxo Alternativo__

### <a id="_Toc373227409"></a>Fluxo Alternativo 5 – Visualizar Relatórios de Conferência

__Ações do Ator__

__Ações do Sistema__

O usuário clica no botão “Relatório”\.

O sistema exibe os registros cadastrados no sistema de acordo com o critério de pesquisa informado – se existente\.

__Fim do fluxo Alternativo__

<a id="_Toc350763252"></a>

# <a id="regras_campos"></a><a id="_Toc373227410"></a>Regras dos Campos 

__Localização da tela:__ Parâmetros >> Tipo de Arquivo

__Título da tela: __Parametrização de Tipo de Arquivo

__RN__

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

RN01

Código do Tipo do Arquivo

Texto

S

S

Alfanumérico \(5\)

OS3962

RN02

Descrição do Tipo do Arquivo

Texto

S

S

Alfanumérico \(56\)

OS3962

RN03

Tipo do Arquivo

Lista

S

S

Preencher conforme abaixo:

- Texto com Largura Fixa
- Texto com Delimitador
- Arquivo XML

Caso a opção selecionada seja “Texto com Largura Fixa”, os campos “Campo Alfanumérico” e “Campo Numérico” ficarão habilitados\.

Caso a opção selecionada seja “Texto com Delimitador”, os campos “Campo Alfanumérico” e “Campo Numérico” ficarão desabilitados\.

Caso a opção selecionada seja “Arquivo XML” os campos “Campo Alfanumérico” e “Campo Numérico” ficarão desabilitados\.

OS3962

OS3962\-A

OS3962\-D

RN04

Separador

Dropdown

S

S

Preencher conforme abaixo:

- |
- ;

Obs: Este campo será habilitado apenas quando o campo Tipo do Arquivo for selecionado na opção “Texto com Delimitador”\.

OS3962

MFS\-2900

RN05

Campo Alfanumérico

Lista

S

S

Lista com as opções \(default: não preenchido\)

Preencher conforme abaixo:

- preencher com zeros à esquerda
- preencher com zeros à direita
- preencher com espaços em branco à esquerda
- preencher com espaços em branco à direita

Esse campo só ficará habilitado, caso o campo “Tipo do Arquivo” seja “Texto com Largura Fixa”\.

OS3962

OS3962\-A

RN06

Campo Numérico

Lista

S

S

Lista com as opções \(default: não preenchido\)

Preencher conforme abaixo:

- preencher com zeros à esquerda
- preencher com zeros à direita
- preencher com espaços em branco à esquerda
- preencher com espaços em branco à direita

Esse campo só ficará habilitado, caso o campo “Tipo do Arquivo” seja “Texto com Largura Fixa”\.

OS3962

OS3962\-A

![](data:image/png;base64,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)

