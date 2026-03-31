# MTZ_Monitor_tributos_Pagar_Tela_Perfil_Geracao

- **Fonte:** MTZ_Monitor_tributos_Pagar_Tela_Perfil_Geracao.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 75 KB

---

THOMSON REUTERS

Perfil de Geração

Monitor de tributos a Pagar

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-3273

Perfil de Geração 

Inclusão da tela Perfil de Geração 

MFS\-6310

Geração do Arquivo de Impostos Apurados

Retirar os impostos ICMS e ICMS\-ST 

Sumário

[1\.	TELA A SER DESENVOLVIDA	3](#_Toc355275051)

[1\.1\.	Diagrama de Casos de Uso	3](#_Toc355275052)

[1\.1\.1\.	UC001 – Manutenção da Estrutura Padrão	3](#_Toc355275053)

[1\.1\.1\.1\.1\.	Fluxo Principal	4](#_Toc355275054)

[1\.1\.1\.1\.2\.	Fluxo Alternativo 1 – Localizar registros \(Exemplo\)	4](#_Toc355275055)

[2\.	Regras dos Campos	5](#_Toc355275056)

# <a id="_Toc355275051"></a>TELA A SER DESENVOLVIDA

\[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir\]

## <a id="_Toc350763243"></a><a id="_Toc355275052"></a>Diagrama de Casos de Uso 

__ __

__UC Estrutura Padrão__

__Usuário __

__UC001 – Manutenção da   __

__Estrutura Padrão__

Manutenção Padrão

## <a id="_Toc350763244"></a><a id="_Toc355275053"></a>UC001 – Manutenção da Estrutura Padrão

\[Descrever a ação deste caso de uso\. 

Ex\.: Este caso de uso descreve o processo de Cadastro de Estrutura Padrão\.\]

__Documentação do Caso de Uso__

__Ator Principal__

__Pré\- Condições__

__Pós\-Condições__

### <a id="_Toc332809652"></a><a id="_Toc332888915"></a><a id="_Toc350763245"></a><a id="_Toc355275054"></a>Fluxo Principal 

\[Descrever a ação principal que será realizada na tela especificada\.

 Ex\.: O usuário deseja realizar o cadastro de uma estrutura padrão\.

__Ações do Ator__

__Ações do Sistema__

\[Descrever a interação do ator com o sistema\. 

Ex\.: O usuário acessa a tela de estrutura padrão\]\.

\[Descrever a ação esperada do sistema

Ex\.:O sistema apresenta a tela, conforme as regras definidas no tópico “Regras dos Campos”\.\]

\[Ex\.:O usuário preenche os campos da Manutenção de Estrutura do Produto\.

__<<Fluxo Alternativo 1>>__

\[Ex\.:O sistema apresenta os campos preenchidos\.\]

### <a id="_Toc332809666"></a><a id="_Toc332888929"></a><a id="_Toc350763246"></a>

### <a id="_Toc355275055"></a>Fluxo Alternativo 1 – Localizar registros \(Exemplo\)

__Ações do Ator__

__Ações do Sistema__

O usuário clica no botão “Localizar”\.

O sistema apresenta os registros cadastrados, de acordo com os parâmetros informados\.

__Fim do fluxo Alternativo__

# <a id="_Toc350763252"></a><a id="_Toc355275056"></a>Regras dos Campos 

__Localização da tela:__ Módulo: Solução Complementar >> Monitor de Tributos a Pagar

                           Menu: Parâmetros >> Perfil

__Título da tela: __Perfil de Geração

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Perfil \(Cód\./Desc\.\)

Texto

S

S

Permite que o usuário informe o código e descrição do perfil\.

Caso não preenchido deverá ser apresentada a seguinte mensagem:

“Código e Descrição do Perfil devem ser informados”\.

Não poderá ser incluso perfil com mesmo código, caso contrário exibir mensagem padrão\. 

MFS\-3273

Grupo Tributo 

Dropdown

S

S

Deverá listar as seguintes opções:

Todos

Federal 

Estadual

Municipal 

Previdenciário

Caso não preenchido, exibir a seguinte mensagem: “Grupo Tributo dever ser informado”\.

Este campo deverá ser bloqueado em uma eventual pesquisa de um perfil já parametrizado\.

MFS\-3273

Tributo\(s\)

Checbox

S

S

Este campo será apresentado apenas quando selecionado o “Grupo Tributo” 

Caso preenchido “Federal” deverão listar os seguintes tributos:

- IRPJ
- IRRF
- CSLL
- PIS/PASEP
- COFINS
- IPI
- PIS/PASEP \(PRÓPRIO\)
- COFINS \(PRÓPRIO\)

MFS\-6310

Caso preenchido “Municipal” deverá listar o seguinte tributo:

- ISS

Caso preenchido “Previdenciário” deverá listar o seguinte tributo:

- INSS

Caso preenchido a opção “Todos” deverá listar todos os tributos\.

Ao menos um registro deve ser selecionado, caso contrário exibir a seguinte mensagem de erro: “Tributo deve ser informado”\.

Este campo deverá ser bloqueado em uma eventual pesquisa de um perfil já parametrizado\.

MFS\-3273

MFS\-6310

Marcar Todos

Checbox 

N

N

Default selecionado quando o campo “Grupo Tributo” selecionado na opção todos\.

Quando selecionado irá selecionar todos os tributos listados, caso contrário, nenhum deverá ser selecionado\.

MFS\-3273

Cód\./Desc Tipo de Arquivo

Dropdown

S

   S

Serão exibidos os códigos conforme cadastro na tela “Tipo de Arquivo” e a opção “Todos”\.

Obs: Os códigos dos layouts deverão ser listados conforme filtro por Grupo e Tributo\. Caso não preenchido exibir a seguinte mensagem: “Cód\./Desc Tipo de Arquivo deve ser informado”\.

Este campo deverá ser bloqueado em uma eventual pesquisa de um perfil já parametrizado\.

MFS\-3273

Consultar

Botão

S

N

Quando selecionado irá consultar os layouts conforme parâmetros de seleção em tela: Grupo do Tributo, Tributo e Cód\./Desc Tipo de Arquivo\.

MFS\-3273

Layout\(s\)

Checbox

S

   S

Serão exibidos todos os layouts cadastrados no sistema, conforme filtro por Grupo Tributo, Tributo e Cód\./Desc Tipo de Arquivo\.

Caso selecionado a opção “Todos” nos campos “Grupo tributo” e “Cód\./Desc Tipo de Arquivo” o\(s\) layout\(s\) deverão ser apresentados da seguinte forma:

Cód\./Desc Layout / Grupo do Tributo / Tributo / Cód\./ Desc Tipo de Arquivo

Ex: 01\- LAYOUT / FEDERAL / IRRF / 01\- TXT

Obs: O label deverá ser dinâmico, conforme parâmetros de seleção em tela\.

Ex: Layout / Grupo do Tributo / Tributo / Tipo de Arquivo

Devem ser apresentados os layouts cujo campo “Status do Layout” esteja “ativo” no caminho: Monitor de tributos a pagar Menu: Parâmetros >> Layout do Arquivo e houver parametrização na tela de “Layout por Estabelecimento”\.

Ao menos “um” layout deve ser preenchido, caso contrário, exibir a seguinte mensagem: Selecione ao menos uma opção em Layout\(s\)\.

MFS\-3273

Selecionar Todos

Botão

S

N

Botão tem a função de selecionar todos os layouts listados

MFS\-3273

Desmarcar Todos

Botão

S

N

Botão tem a função de desmarcar todos os layouts selecionados

MFS\-3273

