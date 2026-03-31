# MTZ_EFD_Manutencao_Registro_1255

- **Fonte:** MTZ_EFD_Manutencao_Registro_1255.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 70 KB

---

THOMSON REUTERS

Módulo EFD\- Escrituração Fiscal Digital – Manutenção da Tabela SAFX304

SAFX304 \- Saldo Consolidado da Restituição/Complemento de ICMS

__Localização__: Menu SPED, Módulo: EFD – Escrituração Fiscal Digital, item Geração 🡪 Manutenção 🡪 Registro 1255

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS31410

Andréa Rocha

Criação da tabela SAFX304 para geração do registro 1255, da nova versão do SPED \- EFD\- Escrituração Fiscal Digital \(vigência Jan/2020\)\.

23/12/2019

Sumário

[1\.	Regras Gerais	2](#_Toc475005506)

[2\.	Layout da Tela	3](#_Toc475005507)

[3\.	Regras de Funcionamento dos Campos	4](#_Toc475005508)

# <a id="_Toc475005506"></a>Regras Gerais

Esta tabela será usada para gerar o registro 1255 do SPED\-EFD, que é filho do registro 1250\.  

Estrutura das tabelas 🡪 vide manual de layout

Campos que compõe a chave das tabelas:

      \[Código da empresa \+ Código do estabelecimento \+ Data da apuração \+ Código do Motivo\]

	

# <a id="_Toc475005507"></a>Layout da Tela

__Botões da barra de menu__:

NOVO

Ao clicar nesta opção, as informações dos campos serão limpas e o usuário poderá incluir um novo registro\.

ABRE

Ao clicar nesta opção, será aberta a janela para seleção dos registros já cadastrados para consulta ou manutenção\. 	

EXCLUI

Esta opção permite a exclusão do registro\. 

CONFIRMA

Opção para salvar as informações do registro incluído ou alterado\.

RELATÓRIO

Esta opção permite imprimir os dados da tabela\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

# <a id="_Toc475005508"></a>Regras de Funcionamento dos Campos 

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Estabelecimento

Alfanumérico 

__S__

S

Listbox

Neste campo será exibida a lista dos estabelecimentos da empresa para seleção do usuário\. 

Caso tenha sido informado um estabelecimento no login, este campo exibirá fixo o estabelecimento informado, e o usuário não poderá alterá\-lo\.

MFS31410

Data Apuração

Data 

__S__

S

  \(DD/MM/AAAA\)

Neste campo será informada uma data válida\.

MFS31410

Código do Motivo

Alfanumérico 

__   S__

__   S__

Este campo trabalha com janela de seleção da tabela dos códigos de motivo de restituição / complementação de ICMS \(DWT\_COD\_MOTIVO\_SPED\)\.

Quando o Código do Motivo for digitado, será validado a sua existência na tabela\.  Caso não exista, será exibida a mensagem “*Código do Motivo não cadastrado*”\.* *

MFS31410

Valor do ICMS

Numérico

    __N __

__   S__

Neste campo será informado o valor do ICMS\.

MFS31410

Valor do ICMS ST Restituição

Numérico

__   N__

__   S__

Neste campo será informado o valor total do ICMS/ST que o

informante tem direito ao crédito, referente às hipóteses de restituição em que há previsão deste crédito\.

MFS31410

Valor do FCP ST Restituição

Numérico

__   N__

__   S__

Neste campo será informado o valor total do FCP\_ST agregado ao valor do ICMS/ST\.

MFS31410

Valor do ICMS ST Complemento

Numérico

__   N__

__   S__

Neste campo será informado o valor total do débito referente ao

complemento do imposto\.

MFS31410

Valor do FCP ST Complemento

Numérico

__   N__

__   S__

Neste campo será informado o valor total do FCP\_ST ST agregado ao valor do ICMS/ST\.

MFS31410

	

       = = = = = =

