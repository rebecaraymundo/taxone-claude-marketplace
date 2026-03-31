# MTZ_Tela_Saldo_Antes_Encerramento_Moeda_Funcional

- **Fonte:** MTZ_Tela_Saldo_Antes_Encerramento_Moeda_Funcional.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 70 KB

---

THOMSON REUTERS

Saldo Antes do Encerramento em Moeda Funcional

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-2631

Criação de Tela

Criação da tela Saldo Antes do Encerramento em Moeda Funcional

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

### <a id="_Toc332809666"></a><a id="_Toc332888929"></a><a id="_Toc350763246"></a>

### <a id="_Toc355275055"></a>Fluxo Alternativo 1 – Localizar registros \(Exemplo\)

__Ações do Ator__

__Ações do Sistema__

# <a id="_Toc350763252"></a><a id="_Toc355275056"></a>Regras dos Campos 

__Localização da tela:__ 

__                     Módulo__: MasterSAF\-DW >> Básicos >> MasterSAF DW

__                     Menu__: Manutenção >> Contabilidade >> Movimentos em Moeda Funcional

__Título da tela: __Saldo Antes do Encerramento em Moeda Funcional

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Estabelecimento

Textbox

S

N

Ao Acessar a tela, este campo será preenchido com o estabelecimento que fora logado no sistema, caso contrário o usuário deverá selecionar o estabelecimento desejado\.

Obs: deverá ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-2631

Data Saldo

Textbox

S

S

Formato: DD/MM/AAAA

Informar a data do saldo antes do encerramento\.

Obs: Caso não preenchido exibir a seguinte mensagem: “O Campo de Data do Saldo deve ser preenchido”\.

MFS\-2631

Conta

Pasta

S

S

Ao selecionar a pasta serão apresentadas os códigos das contas contábeis conforme cadastro na SAFX2002\.

Obs: Caso não preenchido exibir a seguinte mensagem: “O Codigo da Conta Contabil deve ser preenchido”\.

MFS\-2631

Centro de Custo \(Gr\./Cód\./Data Val\.\)

Pasta

N

S

Serão apresentados os códigos do centro de custo conforme cadastro SAFX2003\.

MFS\-2631

Saldo Final 

Textbox

S

S

Default: “,00”

Caso não preenchido exibir a seguinte mensagem: “O campo Saldo Final deve ser preenchido”

MFS\-2631

Indicador Débito/Crédito

Radio Button

N

S

Defautl: Opção débito selecionado

Indicador do Saldo Final:

\- Débito

\- Crédito

MFS\-2631

