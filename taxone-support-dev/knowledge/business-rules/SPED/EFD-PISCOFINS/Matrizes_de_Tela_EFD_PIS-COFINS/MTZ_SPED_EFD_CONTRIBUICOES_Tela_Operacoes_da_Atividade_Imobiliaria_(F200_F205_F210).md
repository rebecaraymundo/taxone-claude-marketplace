# MTZ_SPED_EFD_CONTRIBUICOES_Tela_Operacoes_da_Atividade_Imobiliaria_(F200_F205_F210)

- **Fonte:** MTZ_SPED_EFD_CONTRIBUICOES_Tela_Operacoes_da_Atividade_Imobiliaria_(F200_F205_F210).docx
- **Modificado:** 2022-11-22
- **Tamanho:** 69 KB

---

THOMSON REUTERS

Operações da Atividade Imobiliária \(F200/ F205/ F210\)

EFD\-Contribuições

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

CH7615\_2015

Julyana Perrucini

<a id="OLE_LINK58"></a><a id="OLE_LINK59"></a><a id="OLE_LINK60"></a>Este documento tem como objetivo alterar o preenchimento dos campos <a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>“<a id="OLE_LINK12"></a><a id="OLE_LINK13"></a><a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>Valor total do crédito acumulado sobre o custo incorrido PIS”, “Valor total do crédito acumulado sobre o custo incorrido COFINS” e “<a id="OLE_LINK17"></a><a id="OLE_LINK18"></a><a id="OLE_LINK19"></a><a id="OLE_LINK20"></a>Parcela a descontar em períodos futuros <a id="OLE_LINK63"></a><a id="OLE_LINK64"></a>– do PIS e COFINS”\.

Sumário

[1\.	TELA A SER DESENVOLVIDA	3](#_Toc355275051)

[1\.1\.	Diagrama de Casos de Uso	3](#_Toc355275052)

[1\.1\.1\.	UC001 – Manutenção da Estrutura Padrão	3](#_Toc355275053)

[1\.1\.1\.1\.1\.	Fluxo Principal	4](#_Toc355275054)

[1\.1\.1\.1\.2\.	Fluxo Alternativo 1 – Localizar registros \(Exemplo\)	4](#_Toc355275055)

[2\.	Regras dos Campos	5](#_Toc355275056)

# <a id="_Toc350763252"></a><a id="_Toc355275056"></a>Regras dos Campos 

__Localização da tela:__ SPED\\ EFD – Escrituração Fiscal Digital das Contribuições\\ Manutenção<a id="OLE_LINK9"></a><a id="OLE_LINK10"></a><a id="OLE_LINK11"></a>\\ Operações das Atividades Imobiliárias \(F200/F205/F210\)

__Título da tela: __Operações das Atividades Imobiliárias \(F200/F205/F210\)

__ABA Custo Incorrido__

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

<a id="_Hlk448927171"></a>Valor total do crédito acumulado sobre o custo incorrido PIS

<a id="OLE_LINK21"></a><a id="OLE_LINK22"></a><a id="OLE_LINK23"></a><a id="OLE_LINK24"></a>Numérico

S

N

Formato: 

0,00

Default: 

Desabilitado

<a id="OLE_LINK33"></a><a id="OLE_LINK34"></a><a id="OLE_LINK35"></a><a id="OLE_LINK36"></a>Nesse campo será informado o valor total do crédito acumulado sobre o custo incorrido \- PIS da unidade imobiliária vendida\.

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

<a id="OLE_LINK37"></a><a id="OLE_LINK38"></a><a id="OLE_LINK39"></a><a id="OLE_LINK40"></a>__\[ALTERADA – CH7615\_2016\]__

Quando o campo for importado através da SAFX151, considerar o valor que estiver na carga sem acrescentar o cálculo, pois o mesmo já vem com o arredondamento recomendado, então o cálculo só deverá ser aplicado quando o usuário preencher manualmente <a id="OLE_LINK48"></a><a id="OLE_LINK49"></a><a id="OLE_LINK50"></a><a id="OLE_LINK51"></a>em tela e deverá ser feito o arredondamento de menor a maior conforme regra padrão da Norma ABNT NBR 5891\.

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

