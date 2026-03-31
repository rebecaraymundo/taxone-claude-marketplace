# MTZ-Job-Servidor-Importacao_SAFX340

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX340.docx
- **Modificado:** 2025-11-11
- **Tamanho:** 39 KB

---

# Job Servidor – SAFX340

# Parametrização da Operação da Obrigação por CFOP/Extensão CFOP

#  

__	Localização:__

__	Módulo: __Básicos 🡪 Job Servidor

__	Menu: __Carga__ __🡪 Programação 🡪 Execução

__       		__Importação 🡪 Programação 🡪 Execução     

          		Importação batch 🡪 Programação 🡪 Execução

# \(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX340 conforme o Manual de Layout, o que facilita a consulta\. Qualquer regra que não diga respeito a campos específicos, deve ser incluídax2006\_ na regra numerada como RN00\)\.

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__MFS786255__

Liliane Videira Assaf

Criação da Importação da SAFX340

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__SAFX340 – Parametrização da Operação da Obrigação por CFOP/Extensão CFOP__

__Tabela Definitiva:__ PRT\_OPER\_OBRIG\_CFO / PRT\_OPER\_OBRIG\_EXTCFO

 

Estrutura da SAFX340:

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

Código Fiscal

COD\_CFO

004

A

03

Natureza de Operação

COD\_NATUREZA\_OP

003

A

\(\*\)

04

Código do Módulo

COD\_MODULO

008

A

\(\*\)

05

Código da Operação da Obrigação

COD\_OPER\_OBRIG

010

A

06

Indicador de Transferência

IND\_DESTINACAO

001

A

__Sobre as mensagens de erro:__

Todas as mensagens gravadas no log de erros da importação, devem mostrar os dados de identificação da parametrização, para permitir ao usuário a identificação do registro com erro\.

__MFS786255__

__RN01__

__Campo Validade Inicial \(VALID\_INICIAL\)__

Campo de preenchimento obrigatório e deve ser uma data válida\.

Quando o campo não for preenchido ou preenchido com informação que não é uma data válida, o registro não será importado, e no log de erros será gravada uma mensagem de erro:

*93011 \- Validade Inicial nao preenchida ou invalida\.*

__MFS786255__

__RN02__

__Campo Código Fiscal \(COD\_CFO\)__

O campo COD\_CFO é de preenchimento obrigatório e deve ser informado conforme a Tabela de Códigos Fiscais \(SAFX2012\)\.

Quando o campo não for preenchido, o registro não será importado, e no log de erros será gravada uma mensagem de erro:

*         90028 – CFOP \- Código Fiscal de Operação e Prestação deve ser preenchido*\.

Quando o valor informado não estiver cadastrado na tabela, com validade inicial menor ou igual a Validade Inicial da parametrização \(campo 01 da SAFX340\), o registro não será importado, e no log de erros será gravada uma mensagem de erro:

         *90029 – CFOP \- Código Fiscal de Operação e Prestação não cadastrado*

__MFS786255__

__RN03__

__ Campo Natureza de Operação \(COD\_NATUREZA\_OP\)__

O campo COD\_NATUREZA\_OP não é de preenchimento obrigatório, mas quando preenchido, deve ser informado conforme a Tabela de Natureza de Operações \(SAFX2006\) e Tabela de Extensão de CFOP \(SAFX2081\)

Quando o valor informado não estiver cadastrado na tabela de Natureza de Operações \(SAFX2006\), com validade inicial menor ou igual a Validade Inicial da parametrização \(campo 01 da SAFX340\), o registro não será importado, e no log de erros será gravada uma mensagem de erro:

*             90041 – Código da Natureza de Operação não cadastrado\.*

Quando o valor informado não estiver cadastrado na Tabela de Extensão de CFOP \(SAFX2081\) juntamente com o Código Fiscal \(COD\_CFO\), o registro não será importado, e no log de erros será gravada uma mensagem de erro:

*             90388 – O Campo Codigo Extensao CFOP \(Codigo Fiscal \+ Natureza Operacao\) nao esta cadastrado\.*

\- Observação:

A Natureza de Operação não é obrigatória, porém, se um CFOP for parametrizado com Natureza de Operação, todas as parametrizações desse mesmo CFOP sem Natureza de Operação, são eliminadas na importação\.

O inverso também é verdade, ou seja, se um CFOP for parametrizado sem Natureza de Operação, todas as parametrizações desse mesmo CFOP com Natureza de Operação, são eliminadas\. 

__MFS786255__

__RN04__

__ Campo Código do Módulo__

O campo Código do Módulo é de preenchimento obrigatório, devendo ser informado conforme Tabela de Módulos MSAF \(PRT\_MODULOS\_MSAF\)\. 

Quando o campo não for preenchido ou preenchido com valor inválido que não conste no Cadastro de Módulos MSAF, o registro não será importado, e no log de erros será gravada uma mensagem de erro:  
*93784: Código do Módulo nao esta preenchido\.*

*93785: Codigo de Módulo nao cadastrado na tabela de Módulos MSAF \(TFIX30\)*

__MFS786255__

__RN05__

__Código da Operação da Obrigação \(COD\_OPER\_OBRIG\)__

O campo COD\_OPER\_OBRIG é de preenchimento obrigatório e deve ser informado conforme o Cadastro de Operações das Obrigações \(TFIX116 \- PRT\_OPER\_OBRIG\)\.

Quando o campo não for preenchido, o registro não será importado, e no log de erros será gravada uma mensagem de erro:

           *93793 – O Código da Operação da Obrigação deve ser preenchido\.*

Quando o valor informado não estiver cadastrado na tabela, o registro não será importado, e no log de erros será gravada uma mensagem de erro:

          *93794 – O Campo Código da Operação da Obrigação não está cadastrado\.*

Quando a data de validade inicial da parametrização \(campo 01 da SAFX340\) for anterior à data de validade inicial do Cadastro de Operações das Obrigações, o registro não será importado, e no log de erros será gravada uma mensagem de erro:

*        93795 – A data de Validade Inicial da parametrização é anterior à data de início de vigência do Código da Operação da Obrigação informado\.*

\- Quando a data de validade inicial da parametrização \(campo 01 da SAFX340\) for posterior à data de validade final do Cadastro de Operações das Obrigações, o registro não será importado, e no log de erros será gravada uma mensagem de erro:

*       93796 – A data de Validade Inicial da parametrização é posterior à data fim de vigência do Código da Operação da Obrigação informado\.*

__MFS786255__

__RN06__

__ Campo Indicador de Transferência \(IND\_DESTINACAO\)__

O campo IND\_DESTINACAO não é de preenchimento obrigatório, mas quando preenchido deve ser: S \(com transferência\) ou N \(sem transferência\)\.

Quando o valor informado for diferente de S ou N, o registro não será importado, e no log de erros será gravada uma mensagem de erro:

*       93797 – O campo Indicador de Transferência deve ser preenchido com <S> ou <N>\.*

__MFS786255__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

