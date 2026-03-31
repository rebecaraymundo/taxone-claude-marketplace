# MTZ-Job-Servidor-Importacao_SAFX338

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX338.docx
- **Modificado:** 2025-08-10
- **Tamanho:** 36 KB

---

# Job Servidor – SAFX338

# – Parametrização do Município IBGE x Município Obrigação

#  

__	Localização:__

__	Módulo: __Básicos 🡪 Job Servidor

__	Menu: __Carga__ __🡪 Programação 🡪 Execução

__       		__Importação 🡪 Programação 🡪 Execução     

          		Importação batch 🡪 Programação 🡪 Execução

# \(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX338 conforme o Manual de Layout, o que facilita a consulta\. Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00\)\.

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__MFS786230__

Liliane Videira Assaf

Criação da Importação da SAFX338

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__SAFX338 – Parametrização do Município IBGE x Município Obrigação__

Tabela Definitiva: PRT\_CIDADE\_MSAF\_OBRIG 

Estrutura da SAFX338:

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

UF

UF

002

A

\(\*\)

03

Código do Município \(IBGE\)

COD\_MUNICIPIO

005

N

\(\*\)

04

Código do Módulo

COD\_MODULO

008

A

\(\*\)

05

Código do Município da Obrigação

COD\_CIDADE\_OBRIG

008

A

__Sobre as mensagens de erro:__

Todas as mensagens gravadas no log de erros da importação, devem mostrar os dados de identificação do documento fiscal, para permitir ao usuário a identificação do registro com erro\.

__MFS786230__

__RN01__

__Campo Validade Inicial__

Campo de preenchimento obrigatório e deve ser uma data válida\.

Quando o campo não for preenchido ou preenchido com informação que não é uma data válida, o registro não será importado, e no log de erros será gravada uma mensagem de erro:

*93011 \- Validade Inicial nao preenchida ou invalida\.*

__MFS786230__

__RN02__

__Campo UF__

O campo UF é de preenchimento obrigatório, devendo ser informado conforme Tabela de Unidades da Federação \(ESTADO\)\. 

Quando o campo não for preenchido ou preenchido com valor inválido que não conste no cadastro de Unidades da Federação, o registro não será importado, e no log de erros será gravada as mensagens de erro:

*93372 \- Campo UF nao esta preenchido\.*

*93373 \- Campo UF nao esta cadastrado*

__MFS786230__

__RN03__

__Campo Código do Município \(IBGE\)__

O campo Código do Município \(IBGE\) é de preenchimento obrigatório, devendo ser informado conforme Tabela de Município do IBGE \(MUNICIPIO\)\.

Quando o campo não for preenchido ou preenchido com valor inválido que não conste no cadastro de Município do IBGE, o registro não será importado, e no log de erros será gravada uma mensagem de erro:  
*93783 \- Código do Município \(IBGE\) nao esta preenchido\.*

*50918 \- Codigo de Municipio nao cadastrado na tabela de Municipios*

__MFS786230__

__RN04__

__ Campo Código do Módulo__

O campo Código do Módulo é de preenchimento obrigatório, devendo ser informado conforme Tabela de Módulos MSAF \(PRT\_MODULOS\_MSAF\)\. 

Quando o campo não for preenchido ou preenchido com valor inválido que não conste no cadastro de Módulos MSAF, o registro não será importado, e no log de erros será gravada uma mensagem de erro:  
*93784: Código do Módulo nao esta preenchido\.*

*93785: Codigo de Módulo nao cadastrado na tabela de Módulos MSAF \(TFIX30\)*

__MFS786230__

__RN05__

__Campo Código do Município da Obrigação__

O campo Código do Município da Obrigação é de preenchimento obrigatório, devendo ser informado conforme Tabela de Cidades \(PRT\_CIDADE\_OBRIG\)\. 

Quando o campo não for preenchido ou preenchido com valor inválido que não conste no cadastro de Cidades, o registro não será importado, e no log de erros será gravada uma mensagem de erro:  
*93786: Código do Município da Obrigação nao esta preenchido\.*

*93787: Código do Município da Obrigação cadastrado na tabela de Cidades \(TFIX113\)\.*

__MFS786230__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

