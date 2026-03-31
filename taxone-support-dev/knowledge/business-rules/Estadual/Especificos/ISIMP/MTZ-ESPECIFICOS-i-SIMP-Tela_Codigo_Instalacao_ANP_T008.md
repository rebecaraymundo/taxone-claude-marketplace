# MTZ-ESPECIFICOS-i-SIMP-Tela_Codigo_Instalacao_ANP_T008

- **Fonte:** MTZ-ESPECIFICOS-i-SIMP-Tela_Codigo_Instalacao_ANP_T008.docx
- **Modificado:** 2021-11-25
- **Tamanho:** 77 KB

---

THOMSON REUTERS

I\-SIMP

Manutenção Tabela de Código Instalação ANP T008

__Localização__: Menu Específicos, módulo i\-SIMP, menu Parâmetros 🡪 Tabela de Códigos Instalação ANP T008

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS66217__

Liliane Assaf

Criação da tela de manutenção 

25/11/2021

Sumário

[1\.	Regras Gerais	1](#_Toc37236796)

[2\.	Layout da Tela	1](#_Toc37236797)

[3\.	Regras de Funcionamento dos Campos	1](#_Toc37236798)

# <a id="_Toc37236796"></a>Regras Gerais

Esta funcionalidade tem como objetivo permitir a manutenção dos Códigos de instalação ANP – T008, que são importados via TACES98\.

No módulo Ferramentas já existe uma tela de manutenção para esta tabela em “Tabelas Internas >> Manter >> Tabelas > Tabela de Códigos de instalação ANP – T008”\. O problema que no TaxOne esta tela é de difícil operação por ser do tipo múltiplos registros e a tabela possuir um alto volume de registros\. Por isso estamos criando uma tela, no módulo i\-SIMP, que permita dar manutenção em um único registro por vez evitando assim problemas de performance no TAX ONE\.

# <a id="_Toc37236797"></a>Layout da Tela

Cód\. Instalação:           \[                                 \]

Validade Inicial:            \[ DD/MM/AAAA\]   

Validade Final              \[ DD/MM/AAAA\]  

Dsc\. Tipo Instalação    \[                                                                                            \]

Nome da Tabela Física: PRT\_INSTALACAO\_OBRIG

__Botões da barra de menu__:

NOVO

Ao clicar nesta opção os dados da tela serão limpos, e o usuário poderá cadastrar um novo registro de Código de instalação ANP – T008\.

ABRE

Exibe janela de pesquisa dos registros de Código de instalação ANP – T008 já gravados, para que o usuário selecione <a id="OLE_LINK4"></a>o que desejar exibir em tela\.

EXCLUI

Opção para excluir o registro de Código de instalação ANP – T008\.

CONFIRMA

Opção para salvar os dados do registro de Código de instalação ANP – T008 incluída / alterada\.

RELATÓRIO

Esta opção permite imprimir os dados do registro de Código de instalação ANP – T008\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

  

# <a id="_Toc37236798"></a>Regras de Funcionamento dos Campos

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/__

__Default__

__Regra__

<a id="_Hlk517437550"></a>Cód\. Instalação

Alfanumérico 

__S__

S

Texto

Campo texto de livre digitação\.

Obrigatório\.

Ao salvar o registro, caso o campo não esteja preenchido, exibir a seguinte mensagem:

 “Cód\. Instalação é de preenchimento obrigatório e não foi informado\.”

Validade Inicial

Data 

__S__

S

DD/MM/AAAA

Campo texto no formato DD/MM/AAAA\.

Obrigatório\.

Ao salvar o registro, caso o campo não esteja preenchido, exibir a seguinte mensagem:

 “Validade Inicial é de preenchimento obrigatório e não foi informado\.”

Validade Final

Data 

N

S

DD/MM/AAAA

Campo texto no formato DD/MM/AAAA\.

Não Obrigatório\.

Dsc\. Tipo Instalação    

Alfanumérico

N

S

Texto

Campo texto para livro digitação\.

Não Obrigatório

= = = = = =

