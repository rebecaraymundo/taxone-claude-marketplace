# MTZ_Tela_Manutenção_Operacoes_da_Atividade_Imobiliaria_SAFX149_SAFX150_SAFX151_SAFX152

- **Fonte:** MTZ_Tela_Manutenção_Operacoes_da_Atividade_Imobiliaria_SAFX149_SAFX150_SAFX151_SAFX152.docx
- **Modificado:** 2026-01-22
- **Tamanho:** 67 KB

---

THOMSON REUTERS

<a id="OLE_LINK23"></a><a id="OLE_LINK24"></a><a id="OLE_LINK25"></a>Operações da Atividade Imobiliária \(F200/F205/F210\)

SAFX149, SAFX150, SAFX151, SAFX152

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

OS4316

Inclusão de campo

Incluir o campo Código e Descrição da SCP

CH23678\_2015

Julyana Perrucini

<a id="OLE_LINK46"></a><a id="OLE_LINK47"></a><a id="OLE_LINK48"></a>Criação do documento\. Inclusão de validação para campo “<a id="OLE_LINK34"></a><a id="OLE_LINK35"></a><a id="OLE_LINK36"></a><a id="OLE_LINK37"></a>Percentual da receita recebida até o mês”\.

CH7615\_2015

Julyana Perrucini

<a id="OLE_LINK58"></a><a id="OLE_LINK59"></a><a id="OLE_LINK60"></a>Este documento tem como objetivo alterar o preenchimento dos campos <a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>“<a id="OLE_LINK12"></a><a id="OLE_LINK13"></a><a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>Valor total do crédito acumulado sobre o custo incorrido PIS”, “Valor total do crédito acumulado sobre o custo incorrido COFINS” e “<a id="OLE_LINK17"></a><a id="OLE_LINK18"></a><a id="OLE_LINK19"></a><a id="OLE_LINK20"></a>Parcela a descontar em períodos futuros <a id="OLE_LINK63"></a><a id="OLE_LINK64"></a>– do PIS e COFINS”\.

Sumário

[1\.	Regras dos Campos	3](#_Toc433661398)

# <a id="_Toc350763252"></a><a id="_Toc433661398"></a>Regras dos Campos 

__Localização da tela:__ SPED\\ EFD\-Escrituração Fiscal Digital das Contribuições\\ Manutenção\\ <a id="OLE_LINK26"></a><a id="OLE_LINK27"></a><a id="OLE_LINK28"></a><a id="OLE_LINK29"></a>Operações da Atividade Imobiliária \(<a id="OLE_LINK30"></a><a id="OLE_LINK31"></a><a id="OLE_LINK32"></a><a id="OLE_LINK33"></a>F200/F205/F210\)

__Título da tela: __Operações da Atividade Imobiliária \(F200/F205/F210\) 

__ABA UNIDADE IMOBILIÁRIA VENDIDA \(SAFX149\)__

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Código SCP

Texto

S

N

Formato: 

Pastinha \+ Código \+ Descrição

Default: 

Deverá ser criado o campo Código da SCP, acompanhado da pasta de seleção da informação e o campo de texto para demonstração da descrição vinculada ao código\.

Quando acionada a pasta, serão demonstrados os registros da tabela SAFX2057 – Cadastro da SCP\. Para o código selecionado, será demonstrada também a descrição da SCP\.

Nome do campo em tela: “Código da SCP:”

Caso o usuário informe um código que não tenha cadastro correspondente na SAFX2057, retornar a mensagem de erro: “Cadastro da SCP não encontrado”\.

OS4316

 __ABA VALORES RECEBIDOS \(SAFX150\)__

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Percentual da receita recebida até o mês

Numérico

S

N

Formato: 

0,00

Default: 

Desabilitado

Este campo é preenchido pelo o sistema com a somatória dos campos \(Valor recebido acumulado até o mês anterior ao da escrituração \+ Valor total recebido no mês da escrituração\) dividido pelo o valor do campo \(Valor total de venda da unidade imobiliária\)\. 

__\[ALTERADA – CH23678\_2015\]__

__Validação:__

Caso o valor inserido no campo 07 ou no campo 08 seja maior que o valor inserido no campo 06, ou ainda, a divisão resultar em zero, não importar os registros e exibir a seguinte mensagem: “A SAFX150 somente deve ser importada quando o percentual da receita total recebida até o mês da Escrituração \(campo 07 \+ campo 08 /campo 06\) for maior que zero e não maior que 100%\.”\.

CH23678\_2015

__ABA CUSTO INCORRIDO \(SAFX151\)__

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

<a id="_Hlk448927171"></a>Valor total do crédito acumulado sobre o custo incorrido PIS

<a id="OLE_LINK21"></a><a id="OLE_LINK22"></a>Numérico

S

N

Formato: 

0,00

Default: 

Desabilitado

Nesse campo será informado o valor total do crédito acumulado sobre o custo incorrido \- PIS da unidade imobiliária vendida\.

O usuário não terá opção de alterar o valor e o mesmo será informado via importação através da SAFX151 ou através do cálculo dos campos “Valor da Base de Cálculo do Crédito sobre o Custo Incorrido, acumulado até o período da escrituração” e “Alíquota PIS” quando preenchido manualmente \(campo 09 x campo 12 /100\)\.

<a id="OLE_LINK52"></a><a id="OLE_LINK53"></a><a id="OLE_LINK54"></a>__\[ALTERADA – CH7615\_2016\]__

Quando o campo for importado através da SAFX151, considerar o valor que estiver na carga sem acrescentar o cálculo, pois o mesmo já vem com o arredondamento recomendado, então o cálculo só deverá ser aplicado quando o usuário preencher manualmente em tela e deverá ser feito o arredondamento de menor a maior conforme regra padrão da Norma ABNT NBR 5891\.

__Atenção:__ O mesmo valor preenchido em tela deverá gerar no arquivo magnético, assim como, essa regra já se encontra no documento matriz de geração do Registro F200/ 205/ 210\.

CH7615\_2016

Parcela a descontar em períodos futuros – PIS

Numérico

S

N

Formato: 

0,00

Default: 

Desabilitado

Esse campo será informado automaticamente pelo o sistema com o resultado do valor do campo Valor total do crédito acumulado sobre o custo incorrido – PIS subtraído pelos valores dos campos: Parcela do crédito descontada até o período anterior da escrituração – PIS e a Parcela a descontar no período da escrituração – PIS\. 

<a id="OLE_LINK55"></a><a id="OLE_LINK56"></a><a id="OLE_LINK57"></a>__\[ALTERADA – CH7615\_2016\]__

O usuário não terá opção de alterar o valor e o mesmo será calculado em tela e deverá ser feito o arredondamento de menor a maior conforme regra padrão da Norma ABNT NBR 5891\.

__Atenção:__ O mesmo valor preenchido em tela deverá gerar no arquivo magnético, assim como, essa regra já se encontra no documento matriz de geração do Registro F200/ 205/ 210\.

CH7615\_2016

Valor total do crédito acumulado sobre o custo incorrido COFINS

Numérico

S

N

Formato: 

0,00

Default: 

Desabilitado

Nesse campo será informado o valor total do crédito acumulado sobre o custo incorrido \- COFINS da unidade imobiliária vendida\.

<a id="OLE_LINK41"></a><a id="OLE_LINK42"></a><a id="OLE_LINK43"></a>O usuário não terá opção de alterar o valor e o mesmo será informado via importação através da SAFX151 ou através do cálculo dos campos “Valor da Base de Cálculo do Crédito sobre o Custo Incorrido, acumulado até o período da escrituração” e “Alíquota COFINS” quando preenchido manualmente \(campo 09 x campo 17 /100\)\.

<a id="OLE_LINK38"></a><a id="OLE_LINK39"></a><a id="OLE_LINK40"></a>__\[ALTERADA – CH7615\_2016\]__

Quando o campo for importado através da SAFX151, considerar o valor que estiver na carga sem acrescentar o cálculo, pois o mesmo já vem com o arredondamento recomendado, então o cálculo só deverá ser aplicado quando o usuário preencher manualmente <a id="OLE_LINK49"></a><a id="OLE_LINK50"></a><a id="OLE_LINK51"></a>em tela e deverá ser feito o arredondamento de menor a maior conforme regra padrão da Norma ABNT NBR 5891\.

__Atenção:__ O mesmo valor preenchido em tela deverá gerar no arquivo magnético, assim como, essa regra já se encontra no documento matriz de geração do Registro F200/ 205/ 210\.

CH7615\_2016

<a id="_Hlk448934073"></a>Parcela a descontar em períodos futuros – COFINS

Numérico

S

N

Formato: 

0,00

Default: 

Desabilitado

Esse campo será informado automaticamente pelo o sistema com o resultado do campo Valor total do crédito acumulado sobre o custo incorrido – COFINS subtraído pelo os valores dos campos: Parcela do crédito descontada até o período anterior da escrituração – COFINS e a Parcela a descontar no período da escrituração – COFINS\.

__\[ALTERADA – CH7615\_2016\]__

O usuário não terá opção de alterar o valor e o mesmo será calculado em tela e deverá ser feito o arredondamento de menor a maior conforme regra padrão da Norma ABNT NBR 5891\.

__Atenção:__ O mesmo valor preenchido em tela deverá gerar no arquivo magnético, assim como, essa regra já se encontra no documento matriz de geração do Registro F200/ 205/ 210\.

CH7615\_2016

