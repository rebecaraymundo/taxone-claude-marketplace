# MTZ_Tela_Relatorio_analitico_Item_Documento_Telecom

- **Fonte:** MTZ_Tela_Relatorio_analitico_Item_Documento_Telecom.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 72 KB

---

THOMSON REUTERS

Tela de Relatório Analítico de Itens de Documentos Fiscais de Telecom

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS\_4496

Marcelo Souza

Inclusão dos critérios de geração por ciclo de faturamento e série da nota fiscal, e redirecionamento dos componentes em tela\.  

Sumário

[1\.	Regras dos Campos	3](#_Toc388950622)

# <a id="regras_campos"></a><a id="_Toc350763252"></a><a id="_Toc388950622"></a>Regras dos Campos 

__Localização da tela:__ 

Módulo: Estadual > ICMS

		Menu: Operacional > Analítico > Telecom

	        __Título da tela: __Relatório Analítico de Itens de Documentos Fiscais Telecom\.

	        

        		     	

__Funcionamento da tela:__ <a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a><a id="OLE_LINK4"></a>permite emitir relatório, com o intuito de listar os Documentos fiscais de Telecom no formato analítico\.

Para que o usuário possa obter este relatório, deverá preencher o estabelecimento do qual deseja gerar as informações, o usuário poderá escolher emitir o relatório analítico através de critérios, irão existir quatro critérios de seleção, podendo ser selecionado somente um por geração\.  

	__ 	__

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Estabelecimento

DropDown

S

S

\-

Neste campo o usuário deverá informar o estabelecimento que deseja emitir o relatório, tendo a opção de emitir por todos\.

Número do Processo

DropDown

N

S

Habilitado 

Neste caso, o usuário deverá informar o Número do Processo de Importação\.

Período Ciclo Faturamento

RadioButton

N

S

Desabilitado 

Este RadioButton serve para habilitar  o critério Ciclo Faturamento, na abertura da tela o mesmo deverá vir desabilitado\.

Habilitando este RadioButton o usuário habilita os *TextField Período e Ciclo para geração do relatório por ciclo de faturamento\.*

__*Filtro: *__*Período *

__*Componente:*__* TextField para o usuário informar a data inicial e data final\.*

__*Validação: *__*A data final deverá ser maior que a data inicial\.*

__*Filtro:*__* Ciclo Faturamento*

__*Componente: *__*TextField para o usuário informar o *número ou o código do Ciclo de Faturamento\.

__Validação: __Alfanumérico com 007 caracteres\.

__Local de Origem: __coluna \(__NUM\_CICLO__\) da tabela SAFX42\.

__ __

OS\_4496

Período Série/Sub Série NF

RadioButton

N

S

Desabilitado

Este RadioButton serve para habilitar o critério Série/Sub Série NF, na abertura da tela o mesmo deverá vir desabilitado\.

Habilitando este RadioButton o usuário habilita os TextField Série e Sub Série NF para o relatório ser gerado por número do documento fiscal\.

__Regras de Seleção: __

__Série __

__Sub Série__

__Geração do Relatório__

__PREENCHIDO__

__PREENCHIDO__

Todos os documentos com série e sub série preenchida

__NÃO PREENCHIDO__

__PREENCHIDO__

Não gerar o relatório, não existem documento somente com sub série\. exibir a mensagem padrão de erro\.

__PREENCHIDO__

__NÃO PREENCHIDO__

Todos os documentos com a série preenchida

__NÃO PREENCHIDO__

__NÃO PREENCHIDO__

Todos os documentos com série e sub série vazio

__ __

__*Filtro: *__*Período *

__*Componente:*__* TextField para o usuário informar a data inicial e data final\.*

__*Validação: *__*A data final deverá ser maior que a data inicial\.*

__Filtro:__ Série 

__Componente:__ TextField para o usuário informar o número de série do Documento Fiscal\.

__Validação Série:__ Alfanumérico com 3 caracteres  

__Local de Origem:__ coluna \(SERIE\_DOCFIS\) da tabela SAFX42\.

__Filtro:__ Sub Série NF  

__Componente:__ TextField para o usuário informar o número de sub série do Documento Fiscal\.

__Validação Sub Série:__ Alfanumérico com 2 caracteres\.

__Local de Origem:__ coluna \(SUB\_SERIE\_DOCFIS\) da tabela SAFX42\.

 

OS\_4496

Pessoa Física/Jurídica

RadioButton

N

S

Desabilitado

Neste campo o usuário deverá informar o código da pessoa física/jurídica que deseja emitir relatório, de acordo com a tabela correspondente

*\* Descrição não disponível em tela*

