# MTZ_Tela_Programacao_do_Livro_Batch

- **Fonte:** MTZ_Tela_Programacao_do_Livro_Batch.docx
- **Modificado:** 2025-08-18
- **Tamanho:** 85 KB

---

THOMSON REUTERS

ICMS

Programação do Livro Batch

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4804

Julyana Perrucini

Este documento tem como objetivo incluir a programação do livro 165 \- Registro de apuração do ICMS \- P9 \- Insc Est Única no processo\.

MFS62601

Liliane Assaf

__Trocar__ o label __Data Inicial__ para __Programação Válida a partir de__

__Trocar__ o label __Dias Específicos__ por __Gerar nos dias__

__Trocar__ o label __Eventual__ por __Executar Programação em Qualquer Dia__

__Remover__ o campo __Período__\. Atualmente usando a opção Eventual, o período informado é considerado como período para apuração do Livro, independente do calendário aberto\. Isso pode gerar problemas para o SPED Fiscal, por isso estamos removendo esse campo, para que o livro seja sempre gerado com o período do calendário fiscal\.

Sumário

[1\.	Regras Gerais	1](#_Toc68642808)

[2\.	Layout da Tela	1](#_Toc68642809)

[3\.	Regras dos Campos	1](#_Toc68642810)

# <a id="_Toc451940535"></a><a id="_Toc68642808"></a>Regras Gerais

Parametrização da programação dos livros fiscais de entrada, saída, apuração, estoque, inventário\.

Numa programação define\-se os estabelecimentos, livros e dias do mês em a programação será executada\.

A apuração dos livros será realizada de acordo com o calendário fiscal, ou seja, o período de apuração a ser executado, será o período que está em aberto, conforme pode ser consultado na tela de Status da Obrigação\. 

Uma única programação pode conter vários estabelecimentos e livros fiscais\.

A execução da programação pode ser feita de duas maneiras:

\- Através da tela de Execução disponível no módulo ICMS, menu Livros Batch >> Execução;

\- Através do schedule de um job criado no banco de dados Oracle\.

# <a id="_Toc451940536"></a><a id="_Toc68642809"></a>Layout da Tela

Programação \[                \]

Descrição      \[                                                 \]

Data Inicial   \[dd/mm/aaaa\]

Periodicidade:

\( \) Eventual

\( \) Dias Específicos

Período \[dd/mm/aaaa\] a \[dd/mm/aaaa\]

Prog Dias Específicos:

01 \[ \] 02 \[ \] 03 \[ \]  \.\.\.\.   14 \[ \] 15 \[ \]    16 \[ \]

17 \[ \] 18 \[ \] 19 \[ \]  \.\.\.\.   30 \[ \] 31 \[ \]  UD \[ \]

Estabelecimentos:

\[ \] xxx \- xxxxxxxxxxxxxxxxxxxxx

\[ \] xxx \- xxxxxxxxxxxxxxxxxxxxx

\[ \] xxx \- xxxxxxxxxxxxxxxxxxxxx

\[ \] xxx \- xxxxxxxxxxxxxxxxxxxxx

Tipos de Livro

\[ \] xxx – xxxxxxxxxxxxxxxxxxxxx

\[ \] xxx \- xxxxxxxxxxxxxxxxxxxxx

\[ \] xxx \- xxxxxxxxxxxxxxxxxxxxx

__Botões da barra de menu__:

NOVO

Permite a criação de uma nova programação

ABRE

Permite a seleção de uma programação já gravada para possíveis manutenções\.

CONFIRMA

Opção para salvar os dados alterados ou incluídos\.

EXCLUI

Permite a exclusão dos dados parametrizados\.

FECHA

Fecha a tela da manutenção\.

  

# <a id="_Toc350763252"></a><a id="_Toc68642810"></a>Regras dos Campos 

__Localização da tela:__ Estadual\\ ICMS\\ Livros Batch\\ Programação 

__Título da tela: __Programação do Livro Batch

Tabela gravada: ICT\_PROG, ICT\_CONTROLE

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__Tabela/Campo__

__OS/CH__

Programação

Texto

S

N

Número sequencial atribuído pelo sistema ao salvar uma programação\.

ICT\_PROG / COD\_PROG

Descrição

Texto

S

S

Descrição da programação que deve ser atribuída pelo usuário\.

ICT\_PROG / DSC\_PROG

\[MFS62601\]

Data Inicial

Programação Válida a partir de

Data

S

S

\[MFS62601\]: Mudança de label

Preencher com a data de início validade da programação\. A execução da programação só é permitida a partir dessa data\.

ICT\_PROG / DAT\_INI\_EVENT

MFS62601

Periodicidade

S

S

Radium button

\[MFS62601\]: Mudança de label 

Opções disponíveis:

2 – Eventual “Executar a Programação em Qualquer Dia”

7 \- Dias Específicos “Gerar nos Dias”

Se for escolhida a opção Eventual, então o campo a seguir, Período, deve ser preenchido\.

Se for escolhida a opção Dias Específicos “Gerar nos Dias”, então pelo menos um dia deve ser selecionado no campo “Prog Dias Específicos”\.

ICT\_PROG / IND\_PERIOD

MFS62601

Período

Data

dd/mm/aaaa

\[MFS62601\]: campo excluído

Campo só deve ficar habilidado se a Periodicidade escolhida for 2 – Eventual\.

Período composto pela Data Inicial e Data Final\.

ICT\_PROG / DAT\_INI\_PERIODO

DAT\_FIM\_PERIODO

MFS62601

Prog Dias Específicos

\[MFS62601\]: alteração na de

Campo só deve ficar habilidado se a Periodicidade escolhida for 7 \- “Gerar nos Dias”\.

Opções para seleção de cada dia do mês: 01 a 31, mais a opção UD, que significa último dia do mês\.

ICT\_PROG / COD\_PROG\_MENSAL

MFS62601

Estabelecimento

Texto

S

S

Formato: 

Check Box

Default: 

Habilitado

Permite a seleção de um ou mais estabelecimentos

ICT\_CONTROLE / COD\_ESTAB

Tipos de Livro

Texto

S

S

Formato: 

Check Box

Default: 

Habilitado

Permitir usuário informar os tipos de livros que deseja fazer a programação, tendo a opção de selecionar o modelo de livro \(Ajuste SINIEF, Convênio ICMS, Decreto 27\.427/00 RJ, Consolidado ou Produto\)\.

__\[ALTERADA – OS4804\]__

__Conteúdo:__

- 101 \- Registro de Entradas \- Modelo P1; 
- 102 \- Registro de Saídas \- Modelo P2; 
- 103 \- Registro de Entradas \- Modelo P1A; 
- 104 \- Registro de Saídas \- Modelo P2A; 
- 105 \- Registro de Controle da Produção de Estoque \- P3; 
- 107 \- Registro de Inventário por Produto \- P7 
- 108 \- Registro de Apuração do ICMS \- P9; 
- 131 \- Registro de Entradas \- Modelo P1 Incentivados; 
- 132 \- Registro de Entradas \- Modelo P1A Incentivados; 
- 133 \- Registro de Entradas \- Modelo P1 N/Incentivados; 
- 134 \- Registro de Entradas \- Modelo P1A N/Incentivados; 
- 135 \- Registro de Saídas \- Modelo P2 Incentivados; 
- 136 \- Registro de Saídas \- Modelo P2A Incentivados; 
- 137 \- Registro de Saídas \- Modelo P2 N/Incentivados; 
- 138 \- Registro de Saídas \- Modelo P2A N/Incentivados; 
- 161 \- Registro de Entradas \- Modelo P1; 
- 162 \- Registro de Entradas \- Modelo P1A; 
- 163 \- Registro de Saídas \- Modelo P2; ou 
- 164 \- Registro de Saídas \- Modelo P2A\.
- 165 \- Registro de apuração do ICMS \- P9 \- Insc Est Única\.

ICT\_CONTROLE / COD\_TIPO\_LIVRO

OS4804

