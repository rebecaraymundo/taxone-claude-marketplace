# MTZ_Tela_Lancamento_Contabil_Moeda_Funcional

- **Fonte:** MTZ_Tela_Lancamento_Contabil_Moeda_Funcional.docx
- **Modificado:** 2020-12-28
- **Tamanho:** 69 KB

---

THOMSON REUTERS

Lançamento Contábil em Moeda Funcional

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-2631

Criação de Tela

Criação da Tela Lançamento Contábil em Moeda Funcional

MFS11427

Melhoria na janela de pesquisa 

Melhoria na janela de pesquisa p/ exibir outros campos 

Sumário

[1\.	TELA A SER DESENVOLVIDA	3](#_Toc355275051)

[1\.1\.	Diagrama de Casos de Uso	3](#_Toc355275052)

[1\.1\.1\.	UC001 – Manutenção da Estrutura Padrão	3](#_Toc355275053)

[1\.1\.1\.1\.1\.	Fluxo Principal	4](#_Toc355275054)

[1\.1\.1\.1\.2\.	Fluxo Alternativo 1 – Localizar registros \(Exemplo\)	4](#_Toc355275055)

[2\.	Regras dos Campos	5](#_Toc355275056)

# <a id="_Toc350763252"></a><a id="_Toc355275056"></a>Regras dos Campos 

__Localização da tela:__ Módulo: Básicos >> MastersafDW

__                                   __Menu: Manutenção >> Contabilidade >> Movimentos em Moeda Funcional >> Diário Geral

__Título da tela: __Lançamento Contábil em Moeda Funcional

__      MFS11427__: Alterado o funcionamento da janela de pesquisa \(opção <Abre>\) para ficar de acordo com o padrão utilizado na manutenção da

                               respectiva tabela de lançamentos do menu original, em moeda nacional \(SAFX01\)\. 

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

Data Lançamento

Texto

S

S

Formato: DD/MM/AAAA

Informar a data do lançamento contábil\.

Obs: Caso não preenchido exibir a seguinte mensagem: “O Campo de Data do Lancamento Contabil deve ser preenchido”\.

MFS\-2631

Tipo de Lançamento 

Dropdown

N

S

Default: Não preenchido

Tipo de lançamento contábil:

\- Normal

\- Encerramento

MFS\-2631

Conta\(Gr\./Cod\./Val\.\)

Pasta

S

S

Ao selecionar a pasta serão apresentadas os códigos das contas  contábil conforme cadastro na SAFX2002\.

Obs: Caso não preenchido exibir a seguinte mensagem: “O Codigo da Conta Contabil deve ser preenchido”\.

MFS\-2631

Débito/Crédito do Lançamento

Radio Button

N

S

Default: Selecionado na opção “Crédito”

Tipo da conta contábil: 

\- Débito

\- Crédito

MFS\-2631

Arquivamento

Texto

S

S

Informação necessária para localização do documento que originou o lançamento\.

Obs: Caso não preenchido exibir a seguinte mensagem: “O Campo Arquivamento deve ser preenchido”\.

MFS\-2631

Contra Part\. \(Gr\./Cód\./Val\.\)

Pasta

N

S

Serão apresentados os códigos das contas de contra partida do lançamento contábil conforme cadastro SAFX2002\.

MFS\-2631

Custo \(Gr\./Cód\./Val\.\)

Pasta

N

S

Serão apresentados os códigos do centro de custo conforme cadastro SAFX2003\.

MFS\-2631

Hist\. Padrão \(Gr\./Cód\./Val\.\)

Pasta

N

S

Serão apresentados os códigos de histórico padrão conforme cadastro SAFX2020\.

Obs: Este campo está relacionado ao campo “Histórico Complementar” ao menos um deles deve estar preenchido\. Se nenhum deles for preenchido, retornar mensagem de erro: “Os Campos Codigo do Historico e Historico Complementar sao relacionados, pelo menos um deve ser informado”\.

MFS\-2631

Operação com Participante Vinculado \(SPED Contábil\)

Pasta

N

S

Quando informado, verificar a existência do cadastro da PFJ na tabela SAFX04\.

MFS\-2631

Histórico Complementar

Texto

N

S

Este campo está relacionado ao campo “Histórico Padrão” ao menos um deles deve estar preenchido\. Se nenhum deles for preenchido, retornar mensagem de erro: “Os Campos Codigo do Historico e Historico Complementar sao relacionados, pelo menos um deve ser informado”\.

MFS\-2631

Valor Lançamento

Texto

S

S

Indicar valor do lançamento contábil\.

Obs: Caso não preenchido exibir a seguinte mensagem: “O Campo Valor do Lancamento Contabil deve ser preenchido”\.

MFS\-2631

Número do lançamento

Texto

N

S

Indicar número do lançamento contábil\.

MFS\-2631

