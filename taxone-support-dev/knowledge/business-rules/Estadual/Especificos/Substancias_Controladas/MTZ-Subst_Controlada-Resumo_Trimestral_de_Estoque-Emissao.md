# MTZ-Subst_Controlada-Resumo_Trimestral_de_Estoque-Emissao

- **Fonte:** MTZ-Subst_Controlada-Resumo_Trimestral_de_Estoque-Emissao.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 35 KB

---

# Atendimento – Ministério do Exército – Resumo Trimestral de Estoque – Emissão 

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data de Alteração__

OS3949

W \- ESPECIFICOS \- SUBSTANCIAS CONTROLADAS \- Inclui CR na geração da coluna Procedência do relatório do Ministério do Exército

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

__RN01__

__Campo Nº Certificado de Registro__

Esse campo deve ser concatenado juntamente com os demais campos do campo Procedência\. Para isso deve\-se recuperar o campo NUM\_CR da tabela SCA\_ESTOQUE\_TRIM\_NF\.

OS3949

__RN02__

__Campo Guia de Tráfego__

__\[ALTERADO – MFS1340\]__

Recuperar a informação do campo NUM\_DOCFIS Guia de Tráfego \(a ser definido pelo A&D\) da tabela SCA\_ESTOQUE\_TRIM\_NF\.

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

