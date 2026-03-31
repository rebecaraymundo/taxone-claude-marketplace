# MTZ-Importacao_SAFX70

- **Fonte:** MTZ-Importacao_SAFX70.docx
- **Modificado:** 2024-04-11
- **Tamanho:** 37 KB

---

# Job Servidor \- Importação da SAFX70

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3948

DW \- ESPECIFICOS \- SUBSTANCIAS CONTROLADAS \- Criação de campo CR na SAFX04

Este documento tem como objetivo incluir o campo número de certificado do registro na SAFX04 bem como na sua tabela oficial\. Assim como incluir o campo data de emissão na SAFX70, bem como na sua tabela original\.

MFS604387

Liliane Assaf

Criação de campos para atendimento ao SIPROQUIM2

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Regra p/ importação on line e bacth da SAFX70__

Realizar as seguintes validações:

- 
	- Conversão de campo do tipo data
	- Conversão de campo do tipo numérico
	- Conversão de @ em nulo

OS3948

__RN33__

__Campo 33 \- Data Restrição Embarque__

Campo de Preenchimento não obrigatório\.

Deve ser uma data válida\.

Quando preenchido com uma data inválida, o registro não será importado, e no log de erros será gravada uma mensagem:

*93638 \- O Campo Data Restrição de Embarque com formato invalido\.*

MFS604387

__RN34__

__Campo 34 \- Data Conhecimento Embarque__

Campo de Preenchimento não obrigatório\.

Deve ser uma data válida\.

Quando preenchido com uma data inválida, o registro não será importado, e no log de erros será gravada uma mensagem: 

 

*93639 \- O Campo Data Conhecimento de Embarque com formato invalido\.*

MFS604387

__RN35__

__Campo 35 \- Indicador da Pessoa Física/Jurídica Entrega__

Campo de preenchimento não obrigatório\.

Valores válidos: '1', '2', ‘3’, ‘4’, ‘5’\.

Quando preenchido com valor inválido, o registro não será importado, e no log de erros será gravada uma mensagem: 

*93634 \- O indicador de Pessoa Fisica/Juridica de Entrega deve ser preenchido de acordo com: <1>, <2>, <3>, <4> ou <5>\.*

MFS604387

__RN36__

__Campo 36 \- Código da Pessoa Física/Jurídica Entrega__

Campo de preenchimento não obrigatório\.

A partir do conteúdo dos campos 35 e 36 \(indicador e código da pessoa fis/jur\) será verificada a existência da pessoa informada na Tabela de Pessoas Fis/Jur \(SAFX04\)\. Quando não encontrada, o registro não será importado, e no log de erros será gravada uma mensagem informando que a pessoa não existe na tabela:

*93635 \- O Codigo da Pessoa Fisica/Juridica de Entrega nao esta cadastrado*\.

MFS604387

__RN37__

__Campo 37 \- Indicador da Pessoa Física/Jurídica Adquirente__

Campo de preenchimento não obrigatório\.

Valores válidos: '1', '2', ‘3’, ‘4’, ‘5’\.

Quando preenchido com valor inválido, o registro não será importado, e no log de erros será gravada uma mensagem: 

*93636 \- O indicador de Pessoa Fisica/Juridica do Adquirente deve ser preenchido de acordo com: <1>, <2>, <3>, <4> ou <5>\.*

MFS604387

__RN38__

__Campo 38 \- Código da Pessoa Física/Jurídica Adquirente__

Campo de preenchimento não obrigatório\.

A partir do conteúdo dos campos 37 e 38 \(indicador e código da pessoa fis/jur\) será verificada a existência da pessoa informada na Tabela de Pessoas Fis/Jur \(SAFX04\)\. Quando não encontrada, o registro não será importado, e no log de erros será gravada uma mensagem informando que a pessoa não existe na tabela:

*93637 \- O Codigo da Pessoa Fisica/Juridica do Adquirente nao esta cadastrado*\.

MFS604387

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

