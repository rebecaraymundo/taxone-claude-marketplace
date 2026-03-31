# MTZ-ESPECIFICOS-i-SIMP-Tela_Dados_Iniciais

- **Fonte:** MTZ-ESPECIFICOS-i-SIMP-Tela_Dados_Iniciais.docx
- **Modificado:** 2025-04-15
- **Tamanho:** 72 KB

---

THOMSON REUTERS

i\-SIMP

Parametrização dos Dados Iniciais

__Localização__: Módulo Específicos, módulo i\-SIMP, menu Parâmetros 🡪 Dados Iniciais

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MF619031__

Liliane Videira Assaf

Criação da Tela 

27/05/2024

__MFS682504__

Andréa Rocha

Inclusão de um parâmetro para tratar a geração de produtos com  quantidade zerada

06/09/2024

__MFS777536__

Andréa Rocha

Inclusão de parâmetro para desconsiderar as notas de venda e de devolução, quando ambas forem emitidas no mesmo mês

15/04/2024

Sumário

[1\.	Regras Gerais	2](#_Toc524527071)

[2\.	Layout da Tela	2](#_Toc524527072)

[3\.	Regras de Funcionamento dos Campos	4](#_Toc524527073)

# <a id="_Toc524527071"></a>Regras Gerais

Esta é uma parametrização com informações do estabelecimento para ser utilizada na geração do meio magnético DPMP\.

# <a id="_Toc524527072"></a>Layout da Tela

Tela do tipo formulário simples\.

Estabelecimento  \[ xxxxxx \- xxxxxxxxxxxxxxxxxxxx   \\/\]

Parametrização da Operação ANP utilizada:

\(o\) Por Tipo de Operação

\(  \) Por Tipo de Operação/Estabelecimento

\[ \] Gerar Somente Operações com Quantidades Movimentadas

\[ \] Desconsiderar a NF de Venda e de devolução emitidas no mesmo mês

Replicar para os Estabelecimento \[ \]                                          

\[\] xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  \[\] Selecionar Todos

\[\] xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  \[\] Desmarcar Todos

\[\] xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

\[\] xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

\[\] xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Tabela: EST\_ISIMP\_DADOS\_INI

__Botões da barra de menu__:

NOVO

Ao clicar nesta opção os dados da tela serão limpos, e o usuário poderá cadastrar a parametrização para um novo estabelecimento\. 

ABRE

Exibe janela de pesquisa dos dados já parametrizados, para que o usuário selecione a parametrização <a id="OLE_LINK4"></a>desejada a ser exibida em tela\.

EXCLUI

Opção para excluir a parametrização de um estabelecimento

CONFIRMA

Opção para salvar os dados da parametrização incluída / alterada\.

RELATÓRIO

Esta opção permite imprimir os dados da parametrização\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

  

# <a id="_Toc524527073"></a>Regras de Funcionamento dos Campos

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/__

__Default__

__Regra__

<a id="_Hlk517437550"></a>Estabelecimento

Alfanumérico 

S

S

Listbox

Este campo é uma lista dos estabelecimentos da empresa para seleção do usuário\.

Caso o estabelecimento seja informado no login do Manager, este campo deve ser apresentado bloqueado\. 

Caso contrário, apresentar uma lista contendo todos os estabelecimentos da empresa de login\.

Ao salvar o registro fazer as seguintes validações:

1\) Caso o campo “Estabelecimento” não esteja preenchido, então exibir a seguinte mensagem e não salvar registro:

*   “Campo "Estabelecimento" deve ser preenchido\.”*

Parametrização da Operação ANP utilizada

Alfanumérico 

S

S

Radium Button

Defaul = “Por Tipo de Operação”

Campo composto com as seguintes opções:

- Por Tipo de Operação
- Por Tipo de Operação/Estabelecimento

Gerar Somente Operações com Quantidades Movimentadas

Alfanumérico 

N

S

Checkbox

Default: desmarcado

__\[MFS682504\]__

Opção para permitir que sejam gerados somente os produtos em que as quantidades sejam maior que zero, para as operações de entrada e saída\.

Desconsiderar a NF de Venda e de Devolução emitidas no mesmo mês

Alfanumérico 

N

S

Checkbox

Default: desmarcado

__\[MFS777536\]__

Opção para permitir que sejam desconsideradas as notas fiscais de venda e sua respectiva devolução, quando ambas forem emitidas no mesmo mês\.

Replicar para os Estabelecimentos

Checkbox

Default: desmarcado

Opção para permitir que a parametrização seja replicada para outros estabelecimentos no momento de salvar a operação\.

A lista dos estabelecimentos para replicação só será habilitada para seleção do usuário, quando esta opção estiver marcada\. Caso contrário, a lista permanece desabilitada, e não será possível selecionar nenhum estabelecimento\. 

Estabelecimentos

Alfanumérico 

N

N

Este campo exibe a lista dos estabelecimentos da empresa para seleção do usuário \(exceto o estabelecimento informado no campo “Estabelecimento”\)\.

Selecionar todos

Alfanumérico 

N

N

Opção para marcar / desmarcar todos os estabelecimentos simultaneamente\.

= = = = = =

