# MTZ_GIA_RS_Tela_Manutencao_Anexo_XV

- **Fonte:** MTZ_GIA_RS_Tela_Manutencao_Anexo_XV.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 60 KB

---

THOMSON REUTERS

Anexo XV – Detalhamento de Outros Débitos

GIA\-RS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4636

Julyana Perrucini

Alteração da funcionalidade da tela de manutenção do Anexo XV\.

Sumário

[1\.	Regras dos Campos	3](#_Toc372114539)

# <a id="_Toc350763252"></a><a id="_Toc372114539"></a>Regras dos Campos 

__Localização da tela:__ Estadual\\GIA\-RS\\Obrigações\\IN DRP45/98 GIA\\Manutenção

__Título da tela: __Anexo XV – Detalhamento de Outros Débitos

__Regra Geral:__ Quando houver o preenchimento do campo Amparo/Texto/Ocorrência igual a “8099” o sistema deve permitir N registros para Especificação diferentes, caso o usuário tente inserir o código de outros débitos “8099” com a mesma Especificação, enviar mensagem na tela “Já existe registro com a chave informada”\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Amparo/Texto/Ocorrência

A

S

N

Default:

Habilitado

Neste campo o usuário deverá informar o código de Amparo Legal/Texto/Ocorrência da operação a débito, de acordo com a tabela correspondente \(DWT\_AMPARO\_LEGAL\)\.

__Tratamento:__

\- Não será permitida a repetição dos códigos, exceto para o código de outros débitos “8099”\.

__Obs:__ Para correta seleção deste código, o usuário deverá ter [importado](file:///G:/Tecnologia2/QA/UNITARIO/V2R010_UNIT/Executaveis/Help_on_line/basicos/ferramentas/oper_saffr.htm#menu_IMPORTAR_TFA) a tabela TACES21\.txt ou [cadastrado](file:///G:/Tecnologia2/QA/UNITARIO/V2R010_UNIT/Executaveis/Help_on_line/basicos/mastersaf_dw/oper_safdw01.htm#manut_codigo_amparo) manualmente através do Módulo DataWarehouse\.

__Origem:__

- Código de Amparo Legal/Texto/Ocorrência 

__Localização: __

- Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Ajuste SINIEF \(aba Lançamento de Valores\)\.

OU

- Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Empresas c/ Insc\. Estadual Única \(aba Lançamento de Valores\)\.

OS4636

Especificação

A

S

N

Default:

Habilitado

Permite que o usuário informe uma descrição detalhada dos outros débitos para efeito ao uso do código 99 – Outros da GIA\.

__Tratamento:__

- Para que não haja problema de duplicidade de registros, desabilitar o campo na tela para código de outros débitos diferente de 8099, pois os mesmos já receberão brancos\.

OS4636

