# MTZ_ICMS_GNRE_Grupo_Convenio_Manutencao

- **Fonte:** MTZ_ICMS_GNRE_Grupo_Convenio_Manutencao.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 63 KB

---

THOMSON REUTERS

Guia de Recolhimento de Tributos Estaduais – GNRE por Grupo/Convênio

Manutenção da GNRE por Grupo e Convênio

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4195

Julyana Perrucini

Alteração no tamanho do campo de autenticação bancária da GNRE\.

OS4533

Vânia Mattos

Criação do campo “Código de Identificação do Débito \(RJ\)”

OS4578

Vânia Mattos

Criação do campo “Classe de Vencimento \(SC\)” e alteração no tratamento do campo “Código de Identificação do Débito \(RJ\)” 

Sumário

[1\.	Regras dos Campos	3](#_Toc382212408)

# <a id="_Toc350763252"></a><a id="_Toc382212408"></a>Regras dos Campos 

__Localização da tela:__ Estadual\\ ICMS\\ Apuração\\ Guia de Recolhimento\\ Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE\\ Manutenção

__Título da tela: __Guia de Recolhimento de Tributos Estaduais – GNRE por Grupo/Convênio

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Nº Autenticação

Texto

N

S

Default: Habilitado

Permitir o usuário informar o número da autenticação de retorno da guia de recolhimento\.

Tamanho: 64 caracteres\.

__Obs\.:__ alterado o tamanho do campo pela OS4195 que anteriormente correspondia a 20 caracteres\.

OS4195

Código de Identificação do Débito \(RJ\)

N

N

Este campo trabalha com janela de seleção da TACES60 \(Tabela de Identificação de Débitos de ICMS\-RJ\), e será habilitado 

apenas para os estabelecimentos do estado do RJ \(estabelecimento emissor da guia\)\. Para estabelecimentos de outras UF’s, ficará desabilitado\.

Alteração da OS4578:

*apenas* quando a UF Favorecida for = Rio de Janeiro \(campo “UF Favorecida”\)\.

Na janela de seleção serão demonstrados apenas os códigos cuja data de validade inicial seja menor ou igual à data da apuração \(campo “Data Apuração”\)\.

Caso o código seja digitado pelo usuário, será verificada a sua existência na TACES60, considerando a regra referente à data de validade inicial\. Caso inexistente, ou inválido para a data da apuração, será exibida a mensagem de erro abaixo e a operação não será salva:

 *“Código de Identificação do Débito inexistente ou inválido p/a data da apuração”*

OS4533

OS4578

Classe de Vencimento \(SC\)

N

N

Este campo trabalha com janela de seleção da TACES80 \(Tabela das Classes de Vencimento\), e será habilitado *apenas* quando a UF Favorecida for = Santa Catarina \(campo “UF Favorecida”\)\.

Na janela de seleção serão demonstrados apenas os códigos cuja validade seja compatível com a data da apuração da GNRE \(campo “Data Apuração”\)\. A data da apuração deve ser >= a data inicial e <= a data final de vigência da classe\. 

Caso o código seja digitado pelo usuário, será verificada a sua existência na TACES80, considerando a regra referente à data de validade\. Caso inexistente, ou inválido para a data da apuração, será exibida a mensagem de erro abaixo e a operação não será salva:

 *“Classe de Vencimento inexistente ou inválida p/a data da apuração”*

OS4578

