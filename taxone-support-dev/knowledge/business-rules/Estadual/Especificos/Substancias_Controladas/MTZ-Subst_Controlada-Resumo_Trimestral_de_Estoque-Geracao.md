# MTZ-Subst_Controlada-Resumo_Trimestral_de_Estoque-Geracao

- **Fonte:** MTZ-Subst_Controlada-Resumo_Trimestral_de_Estoque-Geracao.docx
- **Modificado:** 2021-09-21
- **Tamanho:** 38 KB

---

# Atendimento – Ministério do Exército – Resumo Trimestral de Estoque – Geração 

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data de Alteração__

OS3949

DW \- ESPECIFICOS \- SUBSTANCIAS CONTROLADAS \- Inclui CR na geração da coluna Procedência do relatório do Ministério do Exército

Este documento tem como objetivo incluir a geração do campo Número de Certificado do Registro no Resumo Trimestral de estoque para atendimento ao Ministério do Exército\.

05/04/2013

MFS1340

DW \- ESPECIFICOS \- SUBSTANCIAS CONTROLADAS \- Inclui número da Guia de Tráfego na geração da coluna “Guia de Tráfego” do relatório do Ministério do Exército

Este documento tem como objetivo alterar a rotina de geração do relatório “Resumo Trimestral de Estoque – Ministério do Exército” do módulo Específicos – Substâncias Controladas, para ajustar o preenchimento da Guia de Tráfego\.

18/11/2015

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Regra Geral__

__Agrupamento:__ produto\.

__\[ALTERADA – MFS1340\]__

Caso o produto precise da guia de tráfego, será sempre uma guia por produto, o mesmo produto não poderá ter várias guias, então se isso ocorrer na importação ou na manutenção da SAFX70, quando for feita a geração dos registros para armazenagem na tabela SCA\_ESTOQUE\_TRIM\_NF, será considerado sempre a primeira guia informada no documento fiscal\.

A geração do relatório é por produto, então primeiramente verifica as notas de entrada e depois as de saída, porém se for de mesmo produto, os registros serão agrupados\.

MFS1340

__RN01__

__Campo Nº Certificado de Registro__

Preencher o campo de acordo com as características abaixo:

__Nome da Tabela: __SCA\_ESTOQUE\_TRIM\_NF

__Nome do Campo: __NUM\_CR

__Tamanho__: 10

__Tipo__: VARCHAR2

__Regra de Negócio__: Recuperar o número do certificado de registro \(campo NUM\_CR da tabela X04\_PESSOA\_FIS\_JUR\)

OS3949

__RN02__

__Campo Guia de Tráfego__

Preencher o campo de acordo com as características abaixo:

__\[ALTERADA – MFS1340\]__

__Nome da Tabela: __SCA\_ESTOQUE\_TRIM\_NF

__Nome do Campo: __NUM\_DOCFIS__ __A ser definido pelo A&D para receber o número da Guia de Tráfego

__Tamanho__: 12 40

__Tipo__: VARCHAR2

__Regra de Negócio__: Recuperar o número da Guia de Tráfego \(campo GUIA\_TRAFEGO da tabela X70\_MOV\_SUBST\_CONT\)

MFS1340

__RN03__

__Campo Número do Documento Fiscal__

Preencher o campo de acordo com as características abaixo:

__\[ALTERADA – MFS1340\]__

__Nome da Tabela: __SCA\_ESTOQUE\_TRIM\_NF

__Nome do Campo: __NUM\_DOCFIS

__Tamanho__: 12

__Tipo__: VARCHAR2

__Regra de Negócio__: Recuperar o Número do Documento Fiscal \(campo NUM\_DOCFIS da tabela X70\_MOV\_SUBST\_CONT\)

MFS1340

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

