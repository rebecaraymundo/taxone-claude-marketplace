# MTZ-DW-Manutencao_SAFX432

- **Fonte:** MTZ-DW-Manutencao_SAFX432.docx
- **Modificado:** 2024-03-11
- **Tamanho:** 71 KB

---

THOMSON REUTERS

Módulo DW

Manutenção dos Processos Referenciados pelos Itens de Documentos Fiscais de Utilities \(SAFX432\)

__Localização:__ Menu Básicos, módulo DW, menu Manutenção > Documento Fiscal > Documento Fiscal Utilities

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS591913

Liliane Assaf

Criação da tela de Processos Refereciados pelos Itens de Documentos Fiscais de Utilities

10/03/2024

Sumário

[1\.	Regras Gerais	2](#_Toc451260495)

[2\.	Layout da Tela	2](#_Toc451260496)

[3\.	Regras de Funcionamento dos Campos	3](#_Toc451260497)

# <a id="_Toc451260495"></a>Regras Gerais

Tabela SAFX432 \- Tabela de Processos Referenciados pelos Itens de Documentos Fiscais de Utilities

O objetivo dessa tabela é armazenar os processos referenciados pelos itens do Documento Fiscal de Utilities, que são carregados através da SAFX43\. Um item do Documento Fiscal de Utilities pode conter vários processos referenciados\.

Essas informações fazem parte do layout da NFCom\. O Mapeamento completo dos campos da NFCom para as SAFX’s \(SAFX42, SAFX43, SAFX432,\.\.\., SAFX07,SAFX08\) está disponível no Share Point \(Requisitos \- Mastersaf DW TaxOne\\Manuais\-de\-layout\\Layout\_DEXPARA\\ TR\_NFCOM\_DEXPARA\.xlsx\)\.

Estrutura da tabela: Consultar o Manual Layout\.

Informações gravadas na tabela: X432\_ITEM\_TELECOM\_PROC

# <a id="_Toc451260496"></a>Layout da Tela

 

 

 

Processos Referenciados pelo Item

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Tipo do Processo: 

\\/

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Número do Processo: 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Novo 

Exclui

 

<<

<

>

>>

 

Confirma

Fecha

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

  

# <a id="_Toc451260497"></a>Regras de Funcionamento dos Campos

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Tipo do Processo

Alfanumérico

S

__N__

Neste campo deve ser disponibilizada uma lista com as opções abaixo:

0 \- SEFAZ;

1 \- Justiça Federal;

2 \- Justiça Estadual

Ao salvar o registro o Tipo de Processo não tiver sido informado o sistema deve apresentar mensagem padrão e não salvar o registro\.

MFS591913

Número do Processo

Alfanumérico

S

__N__

Texto para livre digitação do número do processo\.

Ao salvar o registro o Número de Processo não tiver sido informado o sistema deve apresentar mensagem padrão e não salvar o registro\.

MFS591913

       = = = = = =

