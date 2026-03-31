# MTZ_Tela_Saldo_Contabil_Centro_Custo_Moeda_Funcional

- **Fonte:** MTZ_Tela_Saldo_Contabil_Centro_Custo_Moeda_Funcional.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 75 KB

---

THOMSON REUTERS

Saldo Contábil por Centro de Custo em Moeda Funcional

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-2631

Criação de Tela

Criação da Tela Saldo Contábil por Centro de Custo em Moeda Funcional

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

__Localização da tela:__ Módulo: Básicos >> MastersafDW

__                                   __Menu: Manutenção >> Contabilidade >> Movimentos em Moeda Funcional >> Diário Geral

__Título da tela: __Saldo Contábil por Centro de Custo em Moeda Funcional

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Estabelecimento

Texto

S

N

Ao Acessar a tela, este campo será preenchido com o estabelecimento que fora logado no sistema, caso contrário o usuário deverá selecionar o estabelecimento desejado\.

Obs: deverá ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-2631

Data do Saldo

Texto

S

S

Formato: DD/MM/AAAA

Informar a data do saldo contábil\.

Obs: Caso não preenchido exibir a seguinte mensagem: “O Campo de Data do Saldo Contábil deve ser preenchido”\.

MFS\-2631

Conta\(Gr\./Cod\./Val\.\)

Pasta

S

S

Ao selecionar a pasta serão apresentadas os códigos das contas contábeis conforme cadastro na SAFX2002\.

Obs: Caso não preenchido exibir a seguinte mensagem: “O Codigo da Conta Contabil deve ser preenchido”\.

MFS\-2631

Centro Custo \(Gr\./Cód\./Data Val\.\)

Pasta

S

S

Serão apresentados os códigos do centro de custo conforme cadastro SAFX2003\.

MFS\-2631

Saldo Contábil Anterior

Texto

N

S

Formato: ,00

MFS\-2631

Débito/Crédito

Radio Button

N

S

Default: Selecionado a opção Débito

MFS\-2631

Total Débitos

Texto

N

S

Formato: ,00

MFS\-2631

Total Créditos 

Texto

N

S

Formato: ,00

MFS\-2631

Saldo Final

Texto

N

N

Default: Desabilitado

Formato: ,00

O valor informado na coluna de Saldo Final deve ser igual ao resultado do seguinte cálculo:

Se Campo Débito/Crédito do Saldo Inicial for igual a “C”, o valor do Saldo Final deve ser igual a:

Saldo Inicial \+ Total Crédito – Total Débito \(considerar sempre valor positivo\)\.

Se Campo Débito/Crédito do Saldo Inicial for igual a “D”, o valor do Saldo Final deve ser igual a:

Saldo Inicial \+ Total Débito – Total Crédito \(considerar sempre valor positivo\)\.

MFS\-☱

\*Débito/Crédito do Saldo Final

Texto

N

N

Default: Desabilitado

Se Campo Débito/Crédito do Saldo Inicial for igual a “C”, o valor do Saldo Final deve ser igual a:

Saldo Inicial \+ Total Crédito – Total Débito\.

Se o resultado do cálculo for positivo, o campo Débito/Crédito do Saldo Final deve ser igual a “C”\. Se for negativo, deve ser igual a “D”\.

Se Campo Débito/Crédito do Saldo Inicial for igual a “D”, o valor do Saldo Final deve ser igual a:

Saldo Inicial \+ Total Débito – Total Crédito\.

Se o resultado do cálculo for positivo, o campo Débito/Crédito do Saldo Final deve ser igual a “D”\. Se for negativo, deve ser igual a “C”\.

MFS\-2631

*\* Descrição não existente em tela\.*

