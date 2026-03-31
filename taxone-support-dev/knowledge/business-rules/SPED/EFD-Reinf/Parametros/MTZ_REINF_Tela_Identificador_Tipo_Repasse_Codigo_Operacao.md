# MTZ_REINF_Tela_Identificador_Tipo_Repasse_Codigo_Operacao

- **Fonte:** MTZ_REINF_Tela_Identificador_Tipo_Repasse_Codigo_Operacao.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 76 KB

---

THOMSON REUTERS

Identificador do Tipo de Repasse por Código de Operação

SPED – Reinf

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS12777

Elenilson Coutinho

Inclusão da Tela de Identificador do Tipo de Repasse por Código de Operação

MFS13367

Lara Aline

Inclusão da opção Patrocínio no campo Tipo de Repasse

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

\[Quem executará o evento\. Ex\.: Usuário do sistema\]\.

__Pré\- Condições__

\[Condições necessárias para execução\. Ex\.: Estabelecimento cadastrado\]

__Pós\-Condições__

\[Resultado após executar caso de uso\. Ex\.: Informação armazenada no banco de dados\]

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

__Localização da tela:__ Módulo: SPED >> EFD – Reinf

__                                   __Menu: REINF >> Parâmetros >> Identificador do Tipo de Repasse >> Por Código de Operação

__Título da tela: __Identificador do Tipo de Repasse por Código de Operação

Obs: Ao abrir a tela de conferência deverá abrir uma subtela para seleção do Grupo\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Grupo Serviço

TextBox

S

N

Default: Desabilitado

Deverá apresentar o grupo conforme apresentado no modal ao abrir a tela\.

MFS\-12777

Estabelecimento

Texto

S

N

Default: Desabilitado

Deverá apresentar o estabelecimento conforme apresentado no modal ao abrir a tela\.

MFS\-12777

Tipo de Repasse

Drop Down

S

S

Deverá listar as seguintes opções:

\[Alteração MFS13367\]

\- Patrocínio

\- Licenciamento de Marcas e Símbolos

\- Publicidades

\- Propaganda

\- Transmissão de Espetáculo

Caso não preenchido deverá apresentar a seguinte mensagem:

“Tipo de Repasse deve ser preenchido”

MFS\-12777

MFS\-13367

Informar Código/Descrição para Pesquisa por:

Código Descrição

Radio Button 

N

S

Default Selecionado: Código

MFS\-12777

Código de Operação

Checkbox

S

S

Deverá listar os códigos de Operação conforme SAFX2001\.

Caso não preenchido deverá apresentar a seguinte mensagem:

“Ao menos um código de Operação deve ser selecionado”

MFS\-12777

Selecionar Todos

Button

N

N

Se selecionado irá selecionar todos os estabelecimentos listados em tela\.

MFS\-12777

Desmarcar Todos

Button

N

N

Se selecionado irá desmarcar todos os estabelecimentos listados em tela\.

MFS\-12777

Replicar para os Estabelecimentos

Checkbox

S

S

Quando selecionado deverá permitir replicar a parametrização para outros estabelecimentos\.

MFS\-12777

Selecionar Todos

Button

N

N

Se selecionado irá selecionar todos os estabelecimentos listados em tela\.

MFS\-12777

Desmarcar Todos

Button

N

N

Se selecionado irá desmarcar todos os estabelecimentos listados em tela\.

MFS\-12777

