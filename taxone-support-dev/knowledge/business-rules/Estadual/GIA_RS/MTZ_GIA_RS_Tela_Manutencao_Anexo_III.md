# MTZ_GIA_RS_Tela_Manutencao_Anexo_III

- **Fonte:** MTZ_GIA_RS_Tela_Manutencao_Anexo_III.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 63 KB

---

THOMSON REUTERS

Anexo III – Créditos Presumidos

GIA\-RS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4308

Julyana Perrucini

Criação do campo Carta de Habilitação de Patrocínio para projetos culturais que entrou como exigência na obrigação GIA\-RS Anexo III\.

OS4548

Julyana Perrucini

Alteração da tabela Anexo III para permitir mais de um registro com o código de crédito presumido “3020”\.

Sumário

[1\.	Regras dos Campos	3](#_Toc372114539)

# <a id="_Toc350763252"></a><a id="_Toc372114539"></a>Regras dos Campos 

__Localização da tela:__ Estadual\\GIA\-RS\\Obrigações\\IN DRP45/98 GIA\\Manutenção

__Título da tela: __Anexo III – Créditos Presumidos

__Regra Geral:__ Quando houver o preenchimento do campo Amparo/Texto/Ocorrência igual a “3020” o sistema deve permitir N registros para Carta de Habilitação do Patrocínio diferentes, caso o usuário tente inserir o código de crédito presumido “3020” com o mesmo nº de carta de habilitação, enviar mensagem na tela “Já existe registro com a chave informada”\.

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

\- Será permitido repetir o código de crédito presumido “3020”\.

__Obs:__ Para correta seleção deste código, o usuário deverá ter [importado](file:///G:/Tecnologia2/QA/UNITARIO/V2R010_UNIT/Executaveis/Help_on_line/basicos/ferramentas/oper_saffr.htm#menu_IMPORTAR_TFA) a tabela TACES21\.txt ou [cadastrado](file:///G:/Tecnologia2/QA/UNITARIO/V2R010_UNIT/Executaveis/Help_on_line/basicos/mastersaf_dw/oper_safdw01.htm#manut_codigo_amparo) manualmente através do Módulo DataWarehouse\.

OS4548

Carta de Habilitação do Patrocínio

N

S

S

Default:

Habilitado

Permite que o usuário informe o número da Carta de Habilitação do Patrocínio da Lei de Incentivo à Cultura\.

__Tratamento:__

- Ao efetuar a geração dos Anexos e Quadros esse campo deve ser preenchido com a informação do campo Carta de Habilitação do Patrocínio com até 12 posições e é obrigatório quando o código crédito presumido for igual a 3020\.
- A partir da OS4548, o campo se torna obrigatório para todos os códigos, então quando o código crédito presumido for diferente de 3020 gravar com zeros até 12 posições\.
- Para que não haja problema de duplicidade de registros, desabilitar o campo na tela para código de crédito presumido diferente de 3020, pois o mesmo já receberá zeros\.

__Origem:__

- Campo Carta de Habilitação do Patrocínio

__Localização: __

- Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Ajuste SINIEF \(aba Lançamento de Valores\)\.

OU

- Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Empresas c/ Insc\. Estadual Única \(aba Lançamento de Valores\)\.

OS4308

OS4548

