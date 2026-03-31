# MTZ_Ferramentas_Tela_Exclusao_Processos_Administrativos_Judiciais_REINF_eSocial

- **Fonte:** MTZ_Ferramentas_Tela_Exclusao_Processos_Administrativos_Judiciais_REINF_eSocial.docx
- **Modificado:** 2024-06-28
- **Tamanho:** 65 KB

---

THOMSON REUTERS

Exclusão Processo Administrativo Judicial \(REINF/eSocial\)

Básicos – Ferramentas

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS10287

Lara Aline

Inclusão da Tela que permita a exclusão dos registros das tabelas SAFX2058 e SAFX2059\.

Sumário

[1\.	Regras dos Campos	3](#_Toc498439367)

# <a id="_Toc350763252"></a><a id="_Toc498439367"></a>Regras dos Campos 

__Localização da tela:__ Módulo: Básicos >> Ferramentas

__                                   __Menu: Rotinas Acessórias >>Inicialização >> Exclusão Processo Administrativo Judicial \(REINF/eSocial\)

__Título da tela: __Exclusão Processo Administrativo Judicial \(REINF/eSocial\)

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Tipo de Execução

Radio Button

N

S

Default Selecionado: Imediata

Este Campo permite ao usuário programar a importação do arquivo de retorno\. Programação que pode ser:

Imediata \- Processo de importação realizado naquele exato momento\. 

Programada – Processo de importação automático programado para a data e hora desejada pelo usuário\.

MFS10287

Data/Hora de Execução

Texto

N

S

Default: Desabilitado

Este campo permite ao usuário informar a data e hora desejada para importação do arquivo \(Processo automático\)\.

Campo será habilitado apenas quanto o campo Tipo de Execução na opção “Programada” for selecionado\.

MFS10287

Executar

Botão

N

N

Quando acionado o sistema irá iniciar o processo de pré geração dos eventos\.

MFS10287

Data Inicial

Data

S

S

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a><a id="OLE_LINK4"></a>Formato: DD/MM/AAAA

Caso não preenchido exibir a seguinte mensagem: “O campo Data Inicial deve ser informado”\.

MFS10287

Data Final

Data

S

S

Formato: DD/MM/AAAA

Caso não preenchido exibir a seguinte mensagem: “O campo Data Final deve ser informado”\.

MFS10287

Selecionar

Pasta de Seleção

N

S

Pasta padrão que permite seleção de um estabelecimento específico\.

MFS10287

Marcar Todos

Checkbox

N

S

Default: não selecionado

Quando selecionado, deve mudar o status dos estabelecimentos para “selecionado”\.

MFS10287

Empresa/Estabelecimento

Checkbox

S

S

Default: não selecionado

Nesse campo deverá apresentar todos os estabelecimentos da empresa do login que possuam o cadastro nos Dados Iniciais do Módulo EFD\-REINF ou Módulo eSocial\. 

Na lista será demonstrado o código e a razão social de cada estabelecimento

XXX\-XXXXXXXXXXXXXXXXX

*\(cód\. e razão social do estabelecimento\)*

Ao menos uma Empresa/Estabelecimento deverá ser selecionada, caso contrário exibir a seguinte mensagem: Ao menos uma Empresa/Estabelecimento deve ser selecionada\.

MFS10287

