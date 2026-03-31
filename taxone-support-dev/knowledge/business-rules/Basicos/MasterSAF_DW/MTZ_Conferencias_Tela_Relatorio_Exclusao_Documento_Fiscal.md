# MTZ_Conferencias_Tela_Relatorio_Exclusao_Documento_Fiscal

- **Fonte:** MTZ_Conferencias_Tela_Relatorio_Exclusao_Documento_Fiscal.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 63 KB

---

THOMSON REUTERS

Relatório de Conferência – Exclusão Documento Fiscal

Mastersaf DW

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4169

Julyana Perrucini

Criação de relatório para conferência de exclusão de documento fiscal

Sumário

[1\.	Regras dos Campos	3](#_Toc377719259)

# <a id="_Toc350763252"></a><a id="_Toc377719259"></a>Regras dos Campos 

__Localização da tela:__ Básicos >> Mastersaf DW >> Relatórios >> Conferências >> Exclusão Documento Fiscal\.

__Título da tela: __Relatório de__ __Conferência – Exclusão Documento Fiscal\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Estabelecimento:

ComboBox

S

S

Default: Habilitado/ Todos

Permitir listar os Estabelecimentos cadastrados em Parâmetros\.

__Tratamento:__

Além de listar os Estabelecimentos, deverá trazer a opção de listar – Todos\.

OS4169

Tipo de Movimento:

ComboBox

N

S

Default: Habilitado

Permitir listar o tipo de movimento do documento fiscal\.

__Tratamento:__

Listar as opções – Entrada ou Saída ou Entrada/Saída, caso não seja selecionada a opção assumir Entrada/Saída como filtro default na geração do relatório\.

OS4169

Documento Fiscal:

Texto

N

S

Formato: Numérico até 12 posições\.

Default: Habilitado

Permitir o preenchimento do número do documento fiscal para consulta específica\.

OS4169

Usuário

ComboBox

N

S

Default: Habilitado/ Todos

Permitir listar os Usuários cadastrados no sistema no módulo Segurança\.

__Tratamento:__

Além de listar os Usuários, deverá trazer a opção de listar – Todos\.

OS4169

Período:

Radio Button

S

S

Opções:

Data Fiscal

Data Exclusão

Formato: 

DD/MM/AAAA

Default:

Data Fiscal selecionado

Permitir selecionar o tipo de data a ser recuperada e trazer campo para o preenchimento da data fiscal ou a data do período da exclusão dos documentos fiscais\.

__Tratamento:__

- De acordo com a seleção deve ser preenchido o campo Período “De: DD/MM/AAAA a DD/MM/AAAA”, caso não seja preenchido, então emitir a mensagem na tela *“Favor informar Período\.”*\.

OS4169

OK

Button

N

N

Default: Habilitado

Permitir gerar o relatório\.

OS4169

Cancelar

Button

N

N

Default: Habilitado

Permitir cancelar o processo de geração do relatório saindo da tela\.

OS4169

