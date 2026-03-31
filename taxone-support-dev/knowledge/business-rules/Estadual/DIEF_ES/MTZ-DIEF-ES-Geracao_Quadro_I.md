# MTZ-DIEF-ES-Geracao_Quadro_I

- **Fonte:** MTZ-DIEF-ES-Geracao_Quadro_I.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 33 KB

---

1. DIEF\-ES \- Geração do Quadro I \- TRANSPORTES

##### DOCUMENTO DE REQUISITO

###### OS

###### Nome

__Descrição__

OS3568

Este documento tem por objetivo de permitir que o Quadro I – Transporte, contemple os documentos de Resumo de Movimento Voo\.

CH101551\-A

DIEF\-ES – Correção da geração do Quadro I\.

Alterada a regra de geração do Quadro I para trazer os documentos fiscais RMD\.

## REGRAS DE NEGÓCIO

#### Cód

### Descrição

### OS

__RG01__

__Regra de seleção do Quadro I – Transporte__

Tabelas a serem recuperadas para documento fiscal de conhecimento de transporte:

SAFX07,

SAFX51, 

PRT\_CFO\_MSAF, 

PRT\_EXTCFO\_MSAF,

SAFX2006,

SAFX2012, 

ESTADO

Campos a serem recuperados: COD\_MUNICIPIO, COD\_MUNICIPIO\_DEST, COD\_MUNIC\_COLETA, IDENT\_ESTADO e somatório VLR\_TOT\_NOTA

Agrupamento: COD\_MUNICIPIO, IDENT\_ESTADO

CRITÉRIOS A SEREM CONSIDERADOS:

- Data Fiscal entre Período Inicial e Período final recebidos como parâmetro\.
- Empresa e Estabelecimento recebidos como parâmetro\.
- Considerar apenas notas não canceladas\.
- Considerar notas que não sejam de transferência\.
-  Notas com movimento de saída\.
- A classificação do documento fiscal deve ser 4, 5 ou 6
- COD\_PARAM = 158
- Município e UF da Capa da Nota e do Estado de Espírito Santo\.
- Recuperar as notas fiscais com itens ou sem itens
- Recuperar as notas fiscais com CFOP e com CFOP/Extensão \(parâmetro de Prestação de Serviços do ICMS\)

Demais regras:

Estas condições deverão ser aplicadas tanto na geração normal quanto à Geração por Inscrição Estadual Única\.

Quando o parâmetro “Geração Centralizada por Inscrição Estadual Única” da Geração dos Registros estiver marcado, o somatório deverá considerar todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no modulo controle das obrigações estaduais\. \(Inventário e Documentário Fiscal\)\.  As informações deverão ser cadastradas sempre em nome do estabelecimento centralizador\.

__OS3568/__

__101551\-A__

Tabelas a serem recuperadas para documento fiscal de Resumo de Movimento Diário:

SAFX07,

PRT\_CFO\_MSAF, 

PRT\_EXTCFO\_MSAF,

SAFX2006,

SAFX2012, 

ESTADO

Campos a serem recuperados: COD\_MUNICIPIO, COD\_MUNICIPIO\_DEST, COD\_MUNIC\_COLETA, IDENT\_ESTADO e somatório VLR\_TOT\_NOTA

Agrupamento: COD\_MUNICIPIO, IDENT\_ESTADO

CRITÉRIOS A SEREM CONSIDERADOS:

- Data de Emissão entre Período Inicial e Período final recebidos como parâmetro\.
- Empresa e Estabelecimento recebidos como parâmetro\.
- Considerar apenas notas não canceladas\.
- Considerar notas que não sejam de transferência\.
-  Notas com movimento de saída\.
- A classificação do documento fiscal deve ser 1 e 3
- Modelo de documento = 15 e 18 
- COD\_PARAM = 158
- Município e UF da Capa da Nota e do Estado de Espírito Santo\.
- Recuperar as notas fiscais sem itens
- Recuperar as notas fiscais com CFOP e com CFOP/Extensão \(parâmetro de Prestação de Serviços do ICMS\)

__RN01__

__Campo 01 – Tipo de Registro__

Deverá ser gravado o conteúdo fixo “I”

__Posição:__ 001 a 001

__Conteúdo: __“I”

__OS3568__

__RN02__

__Campo 02 – Código do Município__

Deverá ser gravado o código do município

__Posição:__ 002 a 006

__Conteúdo__: Utilizar o critério de seleção da regra __RG01__ para obter o filtro dos campos e totalizar o movimento de notas fiscais do período, buscando pelo município origem “Município Remet\. \(Cód\./Desc\.\)” da SAFX07\.

De acordo com este município, verificar correspondência na tabela “Municípios IBGE x Municípios ES” \(TACES24\) e gravar o código do município válido para o estado do Espírito Santo\.

O cadastro “Municípios IBGE x Municípios ES”, em menu \(Estadual – DIEF\-ES – Parâmetros – Municípios IBGE x Municípios ES\)\.

__OS3568__

__RN03__

__Campo 03 – Valor da Geração__

Deverá ser gravado o código do município

__Posição:__ 007 a 016

__Conteúdo:__ Utilizar o critério de seleção da regra __RG01__ para efetuar o somatório, pelo campo “Valor Total do Doc\. Fiscal ” da SAFX07\.

__OS3568__

