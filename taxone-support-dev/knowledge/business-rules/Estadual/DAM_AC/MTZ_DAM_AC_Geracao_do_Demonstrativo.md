# MTZ_DAM_AC_Geracao_do_Demonstrativo

- **Fonte:** MTZ_DAM_AC_Geracao_do_Demonstrativo.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 92 KB

---

THOMSON REUTERS

Demonstrativo da Apuração Mensal 

DAM\-AC

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS1680

Julyana Perrucini

Este documento tem como objetivo criar o módulo DAM\-AC\.

Sumário

[1\.	REGRAS DOS CAMPOS	3](#_Toc452710607)

[2\.	REGRAS DE GERAÇÃO DO RELATÓRIO	3](#_Toc452710608)

[2\.1\.	Layout do Relatório	32](#_Toc452710609)

# <a id="_Toc350763252"></a><a id="_Toc452710607"></a>REGRAS DOS CAMPOS 

Verificar documento Matriz: MTZ\_DAM\_AC\_Tela\_Geracao\_do\_Demonstrativo\.docx\.

# <a id="_Toc452710608"></a>REGRAS DE GERAÇÃO DO RELATÓRIO 

__Origem das informações para geração:__ 

- Tabelas de Discriminação das Entradas/ Saídas e Apuração da Geração dos Registros\.

__Regra de seleção: __

- <a id="OLE_LINK8"></a><a id="OLE_LINK9"></a>Considerar os campos necessários das tabelas de Discriminação das Entradas/ Saídas e Apuração para utilização no Demonstrativo, seguindo os seguintes critérios:
	- A empresa e o estabelecimento devem compreender a empresa e o estabelecimento preenchidos na tela de geração do demonstrativo;
	- A data da apuração dos registros devem compreender o mês e ano de referência preenchido na tela de geração do demonstrativo;

__Regra de gravação: __Os dados cadastrais a ser considerados são do estabelecimento em questão, exceto se a geração for por Inscrição Estadual Única, pois nesse caso de geração, os dados cadastrais a ser considerados são do estabelecimento centralizador\.

__Regra de agrupamento: __Não se aplica\.

__Ordenação: __Não se aplica\.

__Campo/Coluna__

__Tipo__

__Formato/Default__

__Regra__

__MFS/CH__

__Dados do Cabeçalho__

Demonstrativo da Apuração Mensal – DAM

Texto

Formato: 

Text Area

Default:

Fixo

Conteúdo fixo “DEMONSTRATIVO DA APURAÇÃO MENSAL \- DAM”\.

MFS1680

Firma ou Razão Social

Texto

Formato: 

Text Area

Default:

Não se aplica

Preencher com o conteúdo do campo Razão Social da tela de Empresa/Estabelecimento do estabelecimento selecionado na geração do demonstrativo\.

MFS1680

Inscrição Estadual

Texto

Formato: 

Text Area

Default:

Não se aplica

Preencher com o conteúdo do campo Inscrição Estadual quando o campo U\.F for igual a AC da tela de Inscrições Estaduais do estabelecimento selecionado na geração do demonstrativo\.

MFS1680

CGC/MF

Texto

Formato: 

99\.999\.999/9999\-99

Default:

Não se aplica

Preencher com o conteúdo do campo CNPJ da tela de Empresa/Estabelecimento do estabelecimento selecionado na geração do demonstrativo\.

MFS1680

Período de Referência

Texto

Formato: 

MM/AAAA

Default:

Não se aplica

Preencher com o conteúdo Mês/ Ano Referência da tela de geração do demonstrativo\.

MFS1680

Endereço \(Logradouro, rua, av\. etc\)

Texto

Formato: 

Text Area

Default:

Não se aplica

Preencher com o conteúdo dos campos Tipo Logradouro e Endereço da tela de Empresa/Estabelecimento do estabelecimento selecionado na geração do demonstrativo\.

MFS1680

Nº

Texto

Formato: 

Text Area

Default:

Não se aplica

Preencher com o conteúdo do campo Número da tela de Empresa/Estabelecimento do estabelecimento selecionado na geração do demonstrativo\.

MFS1680

Complemento

Texto

Formato: 

Text Area

Default:

Não se aplica

Preencher com o conteúdo do campo Complemento da tela de Empresa/Estabelecimento do estabelecimento selecionado na geração do demonstrativo\.

MFS1680

UF

Texto

Formato: 

Text Area

Default:

Não se aplica

Preencher com o conteúdo do campo U\.F\. da tela de Empresa/Estabelecimento do estabelecimento selecionado na geração do demonstrativo\.

MFS1680

Bairro ou Distrito

Texto

Formato: 

Text Area

Default:

Não se aplica

Preencher com o conteúdo do campo Bairro da tela de Empresa/Estabelecimento do estabelecimento selecionado na geração do demonstrativo\.

__Tratamento:__

- Se o campo Bairro não estiver preenchido, considerar o conteúdo do campo Distrito\.

MFS1680

Município

Texto

Formato: 

Text Area

Default:

Não se aplica

Preencher com a descrição do conteúdo do campo Município da tela de Empresa/Estabelecimento do estabelecimento selecionado na geração do demonstrativo\.

MFS1680

CEP

Texto

Formato: 

Text Area

Default:

Não se aplica

Preencher com o conteúdo do Cep da tela de Empresa/Estabelecimento do estabelecimento selecionado na geração do demonstrativo\.

MFS1680

__Corpo do Relatório \- ENTRADAS__

Entradas de Mercadorias, Bens e/ ou Aquisições de Serviços

Texto

Formato: 

Text Area

Default:

Fixo

Conteúdo fixo “ENTRADAS”\.

Esse quadro de entradas receberá as informações da tabela de entradas e saídas da geração dos registros quando o campo CFOP for iniciado com 1, 2 e 3\.

MFS1680

Natureza da Operação

Texto

Formato: 

Text Area

Default:

Fixo

Essa coluna deve vir com o conteúdo fixo “Natureza da Operação”\.

Tem como objetivo listar todas as operações utilizadas no DAM\.

__Campos fixos da coluna:__

Do Estado

17%

25%

Subst\. Trib\.

Outras

De Outros Estados

7%

12%

Subst\. Trib\.

7%

12%

Outras

Do Exterior

Totais

	

MFS1680

Valor Contábil

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “Valor Contábil”\.

Tem como objetivo somar o valor contábil para cada linha da coluna Natureza da Operação de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

__Preenchimento para linha “Do Estado”, considerar CFOP iniciado com 1:__

Linha 17% \- Do Estado, preencher com o conteúdo do campo Valor Contábil da tabela de discriminação das entradas da geração dos registros \(campo VLR\_CONTABIL\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 17,00;

Linha 25% \- Do Estado, preencher com o conteúdo do campo Valor Contábil da tabela de discriminação das entradas da geração dos registros \(campo VLR\_CONTABIL\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 25,00;

Linha Subst\. Trib\. \- Do Estado, preencher com o conteúdo do campo Valor Contábil da tabela de discriminação das entradas da geração dos registros \(campo VLR\_CONTABIL\) quando o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha Outras \- Do Estado, preencher com o conteúdo do campo Valor Contábil da tabela de discriminação das entradas da geração dos registros \(campo VLR\_CONTABIL\) quando o campo de Valor Isenta ou Valor Outras \(campo VLR\_BASE\_ISENTA ou VLR\_BASE\_OUTRAS\) for maior que zero\.

__Preenchimento para linha “De Outros Estados”, considerar CFOP iniciado com 2:__

Linha 7% \- De Outros Estados, preencher com o conteúdo do campo Valor Contábil da tabela de discriminação das entradas da geração dos registros \(campo VLR\_CONTABIL\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 7,00;

Linha 12% \- De Outros Estados, preencher com o conteúdo do campo Valor Contábil da tabela de discriminação das entradas da geração dos registros \(campo VLR\_CONTABIL\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 12,00;

Linha 7% \- Subst\. Trib\. \- De Outros Estados, preencher com o conteúdo do campo Valor Contábil da tabela de discriminação das entradas da geração dos registros \(campo VLR\_CONTABIL\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 7,00 e o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha 12% \- Subst\. Trib\. \- De Outros Estados, preencher com o conteúdo do campo Valor Contábil da tabela de discriminação das entradas da geração dos registros \(campo VLR\_CONTABIL\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 12,00 e o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha Outras \- De Outros Estados, preencher com o conteúdo do campo Valor Contábil da tabela de discriminação das entradas da geração dos registros \(campo VLR\_CONTABIL\) quando o campo de Valor Isenta ou Valor Outras \(campo VLR\_BASE\_ISENTA ou VLR\_BASE\_OUTRAS\) for maior que zero\.

__Preenchimento para linha “Do Exterior”, considerar CFOP iniciado com 3:__

Linha Do Exterior, preencher com o conteúdo do campo Valor Contábil da tabela de discriminação das entradas da geração dos registros \(campo VLR\_CONTABIL\)\.

MFS1680

Base de Cálculo

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “Base de Cálculo”\.

Tem como objetivo somar o valor da base de cálculo para cada linha da coluna Natureza da Operação de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

__Preenchimento para linha “Do Estado”, considerar CFOP iniciado com 1:__

Linha 17% \- Do Estado, preencher com o conteúdo do campo Base de Cálculo da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_ICMS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 17,00;

Linha 25% \- Do Estado, preencher com o conteúdo do campo Base de Cálculo da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_ICMS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 25,00;

Linha Subst\. Trib\. \- Do Estado, preencher com o conteúdo do campo Base de Cálculo da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_ICMS\) quando o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha Outras \- Do Estado, preencher com o conteúdo do campo Base de Cálculo da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_ICMS\) quando o campo de Valor Isenta ou Valor Outras \(campo VLR\_BASE\_ISENTA ou VLR\_BASE\_OUTRAS\) for maior que zero\.

__Preenchimento para linha “De Outros Estados”, considerar CFOP iniciado com 2:__

Linha 7% \- De Outros Estados, preencher com o conteúdo do campo Base de Cálculo da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_ICMS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 7,00;

Linha 12% \- De Outros Estados, preencher com o conteúdo do campo Base de Cálculo da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_ICMS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 12,00;

Linha 7% \- Subst\. Trib\. \- De Outros Estados, preencher com o conteúdo do campo Base de Cálculo da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_ICMS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 7,00 e o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha 12% \- Subst\. Trib\. \- De Outros Estados, preencher com o conteúdo do campo Base de Cálculo da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_ICMS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 12,00 e o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha Outras \- De Outros Estados, preencher com o conteúdo do campo Base de Cálculo da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_ICMS\) quando o campo de Valor Isenta ou Valor Outras \(campo VLR\_BASE\_ISENTA ou VLR\_BASE\_OUTRAS\) for maior que zero\.

__Preenchimento para linha “Do Exterior”, considerar CFOP iniciado com 3:__

Linha Do Exterior, preencher com o conteúdo do campo Base de Cálculo da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_ICMS\)\.

MFS1680

Isentas ou Não Tributadas

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “Isentas ou Não Tributadas”\.

Tem como objetivo somar o valor da base de isentas ou não tributadas para cada linha da coluna Natureza da Operação de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

__Preenchimento para linha “Do Estado”, considerar CFOP iniciado com 1:__

Linha 17% \- Do Estado, preencher com o conteúdo do campo Isentas ou Não Tributadas da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_ISENTA\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 17,00;

Linha 25% \- Do Estado, preencher com o conteúdo do campo Isentas ou Não Tributadas da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_ISENTA\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 25,00;

Linha Subst\. Trib\. \- Do Estado, preencher com o conteúdo do campo Isentas ou Não Tributadas da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_ISENTA\) quando o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha Outras \- Do Estado, preencher com o conteúdo do campo Isentas ou Não Tributadas da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_ISENTA\) quando o campo de Valor Isenta ou Valor Outras \(campo VLR\_BASE\_ISENTA ou VLR\_BASE\_OUTRAS\) for maior que zero\.

__Preenchimento para linha “De Outros Estados”, considerar CFOP iniciado com 2:__

Linha 7% \- De Outros Estados, preencher com o conteúdo do campo Isentas ou Não Tributadas da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_ISENTA\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 7,00;

Linha 12% \- De Outros Estados, preencher com o conteúdo do campo Isentas ou Não Tributadas da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_ISENTA\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 12,00;

Linha 7% \- Subst\. Trib\. \- De Outros Estados, preencher com o conteúdo do campo Isenta ou Não Tributadas da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_ISENTA\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 7,00 e o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha 12% \- Subst\. Trib\. \- De Outros Estados, preencher com o conteúdo do campo Isentas ou Não Tributadas da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_ISENTA\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 12,00 e o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha Outras \- De Outros Estados, preencher com o conteúdo do campo Isentas ou Não Tributadas da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_ISENTA\) quando o campo de Valor Isenta ou Valor Outras \(campo VLR\_BASE\_ISENTA ou VLR\_BASE\_OUTRAS\) for maior que zero\.

__Preenchimento para linha “Do Exterior”, considerar CFOP iniciado com 3:__

Linha Do Exterior, preencher com o conteúdo do campo Isentas ou Não Tributadas da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_ISENTA\)\.

MFS1680

Outras

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “Outras”\.

Tem como objetivo somar o valor da base outras para cada linha da coluna Natureza da Operação de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

__Preenchimento para linha “Do Estado”, considerar CFOP iniciado com 1:__

Linha 17% \- Do Estado, preencher com o conteúdo do campo Outras da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_OUTRAS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 17,00;

Linha 25% \- Do Estado, preencher com o conteúdo do campo Outras da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_OUTRAS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 25,00;

Linha Subst\. Trib\. \- Do Estado, preencher com o conteúdo do campo Outras da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_OUTRAS\) quando o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha Outras \- Do Estado, preencher com o conteúdo do campo Outras da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_OUTRAS\) quando o campo de Valor Isenta ou Valor Outras \(campo VLR\_BASE\_ISENTA ou VLR\_BASE\_OUTRAS\) for maior que zero\.

__Preenchimento para linha “De Outros Estados”, considerar CFOP iniciado com 2:__

Linha 7% \- De Outros Estados, preencher com o conteúdo do campo Outras da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_OUTRAS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 7,00;

Linha 12% \- De Outros Estados, preencher com o conteúdo do campo Outras da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_OUTRAS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 12,00;

Linha 7% \- Subst\. Trib\. \- De Outros Estados, preencher com o conteúdo do campo Outras da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_OUTRAS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 7,00 e o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha 12% \- Subst\. Trib\. \- De Outros Estados, preencher com o conteúdo do campo Outras da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_OUTRAS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 12,00 e o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha Outras \- De Outros Estados, preencher com o conteúdo do campo Outras da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_OUTRAS\) quando o campo de Valor Isenta ou Valor Outras \(campo VLR\_BASE\_ISENTA ou VLR\_BASE\_OUTRAS\) for maior que zero\.

__Preenchimento para linha “Do Exterior”, considerar CFOP iniciado com 3:__

Linha Do Exterior, preencher com o conteúdo do campo Outras da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_OUTRAS\)\.

MFS1680

__Corpo do Relatório \- SAÍDAS__

Saídas de Mercadorias e/ou Prestação de Serviços

Texto

Formato: 

Text Area

Default:

Fixo

Conteúdo fixo “SAÍDAS”\.

Esse quadro de saídas receberá as informações da tabela de entradas e saídas da geração dos registros quando o campo CFOP for iniciado com 5, 6 e 7\.

MFS1680

Natureza da Operação

Texto

Formato: 

Text Area

Default:

Fixo

Essa coluna deve vir com o conteúdo fixo “Natureza da Operação”\.

Tem como objetivo listar todas as operações utilizadas no DAM\.

__Campos fixos da coluna:__

Para o Estado

17%

25%

Subst\. Trib\.

Outras

Para Outros Estados

12%

Subst\. Trib\.

Devolução

Outras

Para o Exterior

Totais

	

MFS1680

Valor Contábil

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “Valor Contábil”\.

Tem como objetivo somar o valor contábil para cada linha da coluna Natureza da Operação de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

__Preenchimento para linha “Para o Estado”, considerar CFOP iniciado com 5:__

Linha 17% \- Para o Estado, preencher com o conteúdo do campo Valor Contábil da tabela de discriminação das saídas da geração dos registros \(campo VLR\_CONTABIL\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 17,00;

Linha 25% \- Para o Estado, preencher com o conteúdo do campo Valor Contábil da tabela de discriminação das saídas da geração dos registros \(campo VLR\_CONTABIL\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 25,00;

Linha Subst\. Trib\. – Para o Estado, preencher com o conteúdo do campo Valor Contábil da tabela de discriminação das saídas da geração dos registros \(campo VLR\_CONTABIL\) quando o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha Outras \- Para o Estado, preencher com o conteúdo do campo Valor Contábil da tabela de discriminação das saídas da geração dos registros \(campo VLR\_CONTABIL\) quando o campo de Valor Isenta ou Valor Outras \(campo VLR\_BASE\_ISENTA ou VLR\_BASE\_OUTRAS\) for maior que zero\.

__Preenchimento para linha “Para Outros Estados”, considerar CFOP iniciado com 6:__

Linha 7% \- Para Outros Estados, preencher com o conteúdo do campo Valor Contábil da tabela de discriminação das saídas da geração dos registros \(campo VLR\_CONTABIL\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 7,00;

Linha 12% \- Para Outros Estados, preencher com o conteúdo do campo Valor Contábil da tabela de discriminação das saídas da geração dos registros \(campo VLR\_CONTABIL\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 12,00;

Linha 7% \- Subst\. Trib\. \- Para Outros Estados, preencher com o conteúdo do campo Valor Contábil da tabela de discriminação das saídas da geração dos registros \(campo VLR\_CONTABIL\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 7,00 e o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha 12% \- Subst\. Trib\. \- Para Outros Estados, preencher com o conteúdo do campo Valor Contábil da tabela de discriminação das saídas da geração dos registros \(campo VLR\_CONTABIL\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 12,00 e o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha Outras – Para Outros Estados, preencher com o conteúdo do campo Valor Contábil da tabela de discriminação das saídas da geração dos registros \(campo VLR\_CONTABIL\) quando o campo de Valor Isenta ou Valor Outras \(campo VLR\_BASE\_ISENTA ou VLR\_BASE\_OUTRAS\) for maior que zero\.

__Preenchimento para linha “Para o Exterior”, considerar CFOP iniciado com 7:__

Linha Para o Exterior, preencher com o conteúdo do campo Valor Contábil da tabela de discriminação das saídas da geração dos registros \(campo VLR\_CONTABIL\)\.

MFS1680

Base de Cálculo

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “Base de Cálculo”\.

Tem como objetivo somar o valor da base de cálculo para cada linha da coluna Natureza da Operação de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

__Preenchimento para linha “Para o Estado”, considerar CFOP iniciado com 5:__

Linha 17% \- Para o Estado, preencher com o conteúdo do campo Base de Cálculo da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_ICMS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 17,00;

Linha 25% \- Para o Estado, preencher com o conteúdo do campo Base de Cálculo da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_ICMS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 25,00;

Linha Subst\. Trib\. \- Para o Estado, preencher com o conteúdo do campo Base de Cálculo da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_ICMS\) quando o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha Outras \- Para o Estado, preencher com o conteúdo do campo Base de Cálculo da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_ICMS\) quando o campo de Valor Isenta ou Valor Outras \(campo VLR\_BASE\_ISENTA ou VLR\_BASE\_OUTRAS\) for maior que zero\.

__Preenchimento para linha “Para Outros Estados”, considerar CFOP iniciado com 6:__

Linha 7% \- Para Outros Estados, preencher com o conteúdo do campo Base de Cálculo da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_ICMS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 7,00;

Linha 12% \- Para Outros Estados, preencher com o conteúdo do campo Base de Cálculo da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_ICMS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 12,00;

Linha 7% \- Subst\. Trib\. \- Para Outros Estados, preencher com o conteúdo do campo Base de Cálculo da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_ICMS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 7,00 e o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha 12% \- Subst\. Trib\. \- Para Outros Estados, preencher com o conteúdo do campo Base de Cálculo da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_ICMS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 12,00 e o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha Outras \- Para Outros Estados, preencher com o conteúdo do campo Base de Cálculo da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_ICMS\) quando o campo de Valor Isenta ou Valor Outras \(campo VLR\_BASE\_ISENTA ou VLR\_BASE\_OUTRAS\) for maior que zero\.

__Preenchimento para linha “Para o Exterior”, considerar CFOP iniciado com 7:__

Linha Do Exterior, preencher com o conteúdo do campo Base de Cálculo da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_ICMS\)\.

MFS1680

Isentas ou Não Tributadas

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “Isentas ou Não Tributadas”\.

Tem como objetivo somar o valor da base de isentas ou não tributadas para cada linha da coluna Natureza da Operação de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

__Preenchimento para linha “Para o Estado”, considerar CFOP iniciado com 5:__

Linha 17% \- Para o Estado, preencher com o conteúdo do campo Isentas ou Não Tributadas da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_ISENTA\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 17,00;

Linha 25% \- Para o Estado, preencher com o conteúdo do campo Isentas ou Não Tributadas da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_ISENTA\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 25,00;

Linha Subst\. Trib\. \- Para o Estado, preencher com o conteúdo do campo Isentas ou Não Tributadas da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_ISENTA\) quando o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha Outras \- Para o Estado, preencher com o conteúdo do campo Isentas ou Não Tributadas da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_ISENTA\) quando o campo de Valor Isenta ou Valor Outras \(campo VLR\_BASE\_ISENTA ou VLR\_BASE\_OUTRAS\) for maior que zero\.

__Preenchimento para linha “Para Outros Estados”, considerar CFOP iniciado com 6:__

Linha 7% \- Para Outros Estados, preencher com o conteúdo do campo Isentas ou Não Tributadas da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_ISENTA\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 7,00;

Linha 12% \- Para Outros Estados, preencher com o conteúdo do campo Isentas ou Não Tributadas da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_ISENTA\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 12,00;

Linha 7% \- Subst\. Trib\. \- Para Outros Estados, preencher com o conteúdo do campo Isenta ou Não Tributadas da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_ISENTA\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 7,00 e o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha 12% \- Subst\. Trib\. \- Para Outros Estados, preencher com o conteúdo do campo Isentas ou Não Tributadas da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_ISENTA\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 12,00 e o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha Outras \- Para Outros Estados, preencher com o conteúdo do campo Isentas ou Não Tributadas da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_ISENTA\) quando o campo de Valor Isenta ou Valor Outras \(campo VLR\_BASE\_ISENTA ou VLR\_BASE\_OUTRAS\) for maior que zero\.

__Preenchimento para linha “Para o Exterior”, considerar CFOP iniciado com 7:__

Linha Do Exterior, preencher com o conteúdo do campo Isentas ou Não Tributadas da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_ISENTA\)\.

MFS1680

Outras

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “Outras”\.

Tem como objetivo somar o valor da base outras para cada linha da coluna Natureza da Operação de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

__Preenchimento para linha “Para o Estado”, considerar CFOP iniciado com 5:__

Linha 17% \- Para o Estado, preencher com o conteúdo do campo Outras da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_OUTRAS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 17,00;

Linha 25% \- Para o Estado, preencher com o conteúdo do campo Outras da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_OUTRAS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 25,00;

Linha Subst\. Trib\. \- Para o Estado, preencher com o conteúdo do campo Outras da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_OUTRAS\) quando o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha Outras \- Para o Estado, preencher com o conteúdo do campo Outras da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_OUTRAS\) quando o campo de Valor Isenta ou Valor Outras \(campo VLR\_BASE\_ISENTA ou VLR\_BASE\_OUTRAS\) for maior que zero\.

__Preenchimento para linha “Para Outros Estados”, considerar CFOP iniciado com 6:__

Linha 7% \- Para Outros Estados, preencher com o conteúdo do campo Outras da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_OUTRAS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 7,00;

Linha 12% \- Para Outros Estados, preencher com o conteúdo do campo Outras da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_OUTRAS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 12,00;

Linha 7% \- Subst\. Trib\. \- Para Outros Estados, preencher com o conteúdo do campo Outras da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_OUTRAS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 7,00 e o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha 12% \- Subst\. Trib\. \- Para Outros Estados, preencher com o conteúdo do campo Outras da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_OUTRAS\) quando o campo de Valor Alíquota \(campo VLR\_ALIQ\) for igual a 12,00 e o campo de Valor ICMSS \(campo VLR\_ICMS\_S\) for maior que zero;

Linha Outras \- Para Outros Estados, preencher com o conteúdo do campo Outras da tabela de discriminação das saídas da geração dos registros \(campo VLR\_BASE\_OUTRAS\) quando o campo de Valor Isenta ou Valor Outras \(campo VLR\_BASE\_ISENTA ou VLR\_BASE\_OUTRAS\) for maior que zero\.

__Preenchimento para linha “Do Exterior”, considerar CFOP iniciado com 3:__

Linha Do Exterior, preencher com o conteúdo do campo Outras da tabela de discriminação das entradas da geração dos registros \(campo VLR\_BASE\_OUTRAS\)\.

MFS1680

__Corpo do Relatório \- Apuração__

Crédito do Imposto

Texto

Formato: 

Text Area

Default:

Fixo

Conteúdo fixo “Crédito do Imposto”\.

Esse quadro receberá as informações da tabela de crédito do imposto da geração dos registros\.

MFS1680

Entrada c/ Créditos

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “Entrada c/ Créditos”, devendo ser preenchida com a soma do conteúdo do campo Entradas com Crédito da tabela Crédito do Imposto de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

MFS1680

Outros Créditos

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “Outros Créditos”, devendo ser preenchida com a soma do conteúdo do campo Outros Créditos da tabela Crédito do Imposto de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

MFS1680

Estorno de Débito

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “Estorno de Débito”, devendo ser preenchida com a soma do conteúdo do campo Estorno de Débito da tabela Crédito do Imposto de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

MFS1680

SubTotal

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “SubTotal”, devendo ser preenchida com a soma do conteúdo do campo Sub \- Total da tabela Crédito do Imposto de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

MFS1680

Saldo Anterior

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “Saldo Anterior”, devendo ser preenchida com a soma do conteúdo do campo Saldo Credor do Mês Anterior da tabela Crédito do Imposto de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

MFS1680

Total de Créditos

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “Total de Créditos”, devendo ser preenchida com a soma do conteúdo do campo Total de Crédito da tabela Crédito do Imposto de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

MFS1680

Débito do Imposto

Texto

Formato: 

Text Area

Default:

Fixo

Conteúdo fixo “Débito do Imposto”\.

Esse quadro receberá as informações da tabela de débito do imposto da geração dos registros\.

MFS1680

Saída c/ Débito

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “Saída c/ Débito”, devendo ser preenchida com a soma do conteúdo do campo Saídas com Débito da tabela Débito do Imposto de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

MFS1680

Estorno de Crédito

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “Estorno de Crédito”, devendo ser preenchida com a soma do conteúdo do campo Estorno de Créditos da tabela Débito do Imposto de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

MFS1680

Incent\. Fisc\. Pag\.

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “Incent\. Fisc\. Pag\.”, devendo ser preenchida com a soma do conteúdo do campo Incentivos Fiscais Pagto da tabela Débito do Imposto de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

MFS1680

Outros Débitos

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “Outros Débitos”, devendo ser preenchida com a soma do conteúdo do campo Outros Débitos da tabela Débito do Imposto de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

MFS1680

Total dos Débitos

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “Total dos Débitos”, devendo ser preenchida com a soma do conteúdo do campo Total de Débitos da tabela Débito do Imposto de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

MFS1680

Apuração dos Saldos

Texto

Formato: 

Text Area

Default:

Fixo

Conteúdo fixo “Apuração dos Saldos”\.

Esse quadro receberá as informações da tabela de apuração dos saldos do imposto da geração dos registros\.

MFS1680

Saldo Devedor

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “Saldo Devedor”, devendo ser preenchida com a soma do conteúdo do campo Saldo Devedor da tabela Apuração dos Saldos de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

MFS1680

Deduções

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “Deduções”, devendo ser preenchida com a soma do conteúdo do campo Deduções da tabela Apuração dos Saldos de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

MFS1680

Incent\. Fiscais Financ\.

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “Incent\. Fiscais Financ\.”, devendo ser preenchida com a soma do conteúdo do campo Incentivos Fiscais Financ\. da tabela Apuração dos Saldos de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

MFS1680

Imposto a Recolher

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “Imposto a Recolher”, devendo ser preenchida com a soma do conteúdo do campo Imposto a Recolher da tabela Apuração dos Saldos de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

MFS1680

Saldo Credor

Numérico

Formato: 

0,00

Default:

Não se aplica

Essa coluna deve vir com o conteúdo fixo “Saldo Credor”, devendo ser preenchida com a soma do conteúdo do campo Saldo Credor da tabela Apuração dos Saldos de acordo com o período e estabelecimento parametrizados na tela de geração do demonstrativo\.

MFS1680

## <a id="_Toc452710609"></a>Layout do Relatório

Verificar o documento LAYOUT\_DAM\_AC\.xls\.

