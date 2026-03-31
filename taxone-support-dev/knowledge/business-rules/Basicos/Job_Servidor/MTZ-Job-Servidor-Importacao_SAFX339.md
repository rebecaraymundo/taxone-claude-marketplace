# MTZ-Job-Servidor-Importacao_SAFX339

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX339.docx
- **Modificado:** 2025-09-16
- **Tamanho:** 39 KB

---

# Job Servidor – SAFX339

# – Parametrização do CNAE x CNAE Obrigação

#  

__	Localização:__

__	Módulo: __Básicos 🡪 Job Servidor

__	Menu: __Carga__ __🡪 Programação 🡪 Execução

__       		__Importação 🡪 Programação 🡪 Execução     

          		Importação batch 🡪 Programação 🡪 Execução

# \(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX339 conforme o Manual de Layout, o que facilita a consulta\. Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00\)\.

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__MFS786236__

Liliane Videira Assaf

Criação da Importação da SAFX339

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__SAFX339 – Parametrização CNAE x CNAE Obrigação__

Tabela Definitiva: PRT\_CNAE\_MSAF\_OBRIG 

Estrutura da SAFX339:

OBRIG

ITEM

DESCRIÇÃO

CAMPO

TAM

TIPO

\(\*\)

01

Validade Inicial

VALID\_INICIAL

008

N

\(\*\)

02

Código de Atividade \(CNAE\)

COD\_ATIVIDADE

007

N

\(\*\)

03

Código do Módulo

COD\_MODULO

008

A

\(\*\)

04

Código de Atividade da Obrigação

COD\_CNAE\_OBRIG

010

A

__Sobre as mensagens de erro:__

Todas as mensagens gravadas no log de erros da importação, devem mostrar os dados de identificação do documento fiscal, para permitir ao usuário a identificação do registro com erro\.

__MFS786236__

__RN01__

__Campo Validade Inicial__

Campo de preenchimento obrigatório e deve ser uma data válida\.

Quando o campo não for preenchido ou preenchido com informação que não é uma data válida, o registro não será importado, e no log de erros será gravada uma mensagem de erro:

*93011 \- Validade Inicial nao preenchida ou invalida\.*

__MFS786236__

__RN02__

__Campo Código de Atividade \(CNAE\)__

O campo Código de Atividade \(CNAE\) é de preenchimento obrigatório, devendo ser informado conforme Cadastro de Atividade Econômica \(Taces01 \- Tabela ATIV\_ECONOMICA\)\. 

Quando o campo não for preenchido o registro não será importado, e no log de erros será gravada as mensagens de erro:

*90584 \- O codigo da Atividade Economica deve ser preenchido\.*

Quando o campo for preenchido com valor inválido que não conste no Cadastro de Atividade Econômica, o registro não será importado, e no log de erros será gravada as mensagens de erro:

*90384 \- O Campo Codigo de Atividade Economica nao esta cadastrado*

Quando o campo for preenchido com um código de Atividade que conste no Cadastro de Atividade Econômica, mas a data de validade inicial do cadastro é maior que a Validade Inicial da parametrização \(campo 01 da SAFX339\), o registro não será importado, e no log de erros será gravada as mensagens de erro:

*93788 \- A data de Validade Inicial da parametrização e anterior a data de Inicio de Vigencia do Codigo de Atividade Economica informado*

__MFS786236__

__RN03__

__ Campo Código do Módulo__

O campo Código do Módulo é de preenchimento obrigatório, devendo ser informado conforme Tabela de Módulos MSAF \(PRT\_MODULOS\_MSAF\)\. 

Quando o campo não for preenchido ou preenchido com valor inválido que não conste no Cadastro de Módulos MSAF, o registro não será importado, e no log de erros será gravada uma mensagem de erro:  
*93784: Código do Módulo nao esta preenchido\.*

*93785: Codigo de Módulo nao cadastrado na tabela de Módulos MSAF \(TFIX30\)*

__MFS786236__

__RN04__

__Campo Código de Atividade da Obrigação__

O campo Código de Atividade da Obrigação é de preenchimento obrigatório, devendo ser informado conforme Cadastro de Atividades Econômicas das Obrigações \(TFIX119 – Tabela PRT\_CNAE\_OBRIG\)\. 

Quando o campo não for preenchido o registro não será importado, e no log de erros será gravada as mensagens de erro:

*93789 \- O codigo da Atividade da Obrigação deve ser preenchido\.*

Quando o campo for preenchido com valor inválido que não conste no Cadastro de Atividades Econômicas das Obrigações, o registro não será importado, e no log de erros será gravada as mensagens de erro:

*93790 \- O Campo Codigo de Atividade da Obrigação nao esta cadastrado*

Quando o campo for preenchido com um Código de Atividade da Obrigação que conste no Cadastro de Atividades Econômicas das Obrigações, mas a data de validade inicial do cadastro é maior que a Validade Inicial da parametrização \(campo 01 da SAFX339\), o registro não será importado, e no log de erros será gravada as mensagens de erro:

*93791 \- A data de Validade Inicial da parametrização e anterior a data de Inicio de Vigencia do Codigo de Atividade da Obrigação informado*

Quando o campo for preenchido com um Código de Atividade da Obrigação que conste no Cadastro de Atividades Econômicas das Obrigações, mas a data de validade final do cadastro está preenchida e é menor que a Validade Inicial da parametrização \(campo 01 da SAFX339\), o registro não será importado, e no log de erros será gravada as mensagens de erro:

*93792 \- A data de Validade Inicial da parametrização e posterior a data fim de Vigencia do Codigo de Atividade da Obrigação informado*

__MFS786236__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

