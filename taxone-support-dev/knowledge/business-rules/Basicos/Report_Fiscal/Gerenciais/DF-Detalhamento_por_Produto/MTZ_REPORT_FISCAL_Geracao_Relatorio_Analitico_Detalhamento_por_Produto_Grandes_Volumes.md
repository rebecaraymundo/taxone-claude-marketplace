# MTZ_REPORT_FISCAL_Geracao_Relatorio_Analitico_Detalhamento_por_Produto_Grandes_Volumes

- **Fonte:** MTZ_REPORT_FISCAL_Geracao_Relatorio_Analitico_Detalhamento_por_Produto_Grandes_Volumes.docx
- **Modificado:** 2023-11-09
- **Tamanho:** 68 KB

---

THOMSON REUTERS

Relatório Analítico – Detalhamento por Produto \(Grandes Volumes\)

Geração do Detalhamento por Produto

Localização: Básicos > Report Fiscal

Menu: Gerenciais > Documento Fiscais > Analíticos > Detalhamento por Produto \(Grandes Volumes\)

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS4310

Lara Aline

Este documento tem o objetivo de incluir os campos: IPI Isentas, IPI Outras, Base ICMSS e alterar a regra do campo Base IPI\.

MFS14922

João Henrique

Inclusão do campo de Código de Tributação IPI no relatório\.

MFS\-71662

Rogério Ohashi

Inclusão dos campos Valor Base INSS, Valor Alíquota INSS e Valor de INSS Retido no relatório\.

MFS\-70186

Andréa Rocha

Inclusão do campo Inscrição Estadual Substituto Tributário no relatório\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral de Seleção__

A geração do relatório será de acordo com os critérios de filtro informados na tela de geração\.

__Origem das informações__: Manter o mesmo tratamento atual do relatório normal e de via servidor, ou seja, recuperação de nota fiscal de entrada e saída pela SAFX07/08 e parametrizações comuns e obrigatórias para NF, sendo classificação fiscal 1, 3  e documento não cancelado\.

*Observação:* Os três relatórios de Detalhamento por Produto são idênticos, mudando apenas a forma de salvar o arquivo\.

MFS4310

RN01

__Informações padrão do cabeçalho__

As informações do cabeçalho do relatório serão geradas da seguinte forma:

- Na parte superior do relatório, serão geradas as informações da Empresa selecionada, Data e Hora de emissão do relatório e Página do mesmo\.
	- No canto superior esquerdo do relatório, serão informados os dados do estabelecimento\. O estabelecimento será informado de acordo com o Estabelecimento selecionado na tela geração e será informado através do Código e Descrição separados por um “\-“, além disso, deverá apresentar o CNPJ e Inscrição Estadual \(caso este esteja parametrizado\)\.
	- Na parte central superior será informada a “Data” do relatório\. Essa informação irá exibir a data e hora que o relatório foi gerado\.
	- No canto direito será exibido o número da página do relatório, que deverá ser sequencial\. 
- Na parte central do relatório, deverá ser exibido o título do mesmo\. O título do relatório é “RELATÓRIO ANALÍTICO  \- DETALHAMENTO POR PRODUTO”\.
- Abaixo do título do relatório, deverá ser exibido no formato dd/mm/aaaa, o período de geração do relatório\. Essa informação será recuperada do campo “Período”\.

OS4774

RN02

__Informações do corpo do relatório__

O Relatório Analítico será exibido através dos seguintes campos:

Nº NF – Campo 08 da SAFX07\.

Movto E/S – Campo 03 da SAFX07\.

Tipo Docto – Campo 05 da SAFX07\.

Série / Subsérie – Campo 09 da SAFX07\.

Data Fiscal – Campo 20 da SAFX07\.

Data Emissão – Campo 11 da SAFX07\.

Nº de Controle – Campo 16 da SAFX07\.

Mod\.Documento – Campo 13 da SAFX07 de acordo com o cadastrado na SAFX2024\.

Chave de Acesso da NF\-e – Campo 226 da SAFX07\.

Código FIS/JUR – Campo 07 da SAFX07 de acordo com o cadastrado na SAFX04\.

Razão Social – Campo 07 da SAFX07 de acordo com o cadastrado na SAFX04\.

CPF/CNPJ – Campo 07 da SAFX07 de acordo com o cadastrado na SAFX04\.

Insc\.Estadual – Campo 07 da SAFX07 de acordo com o cadastrado na SAFX04\.

UF – Campo 07 da SAFX07 de acordo com o cadastrado na SAFX04\.

Nº do Item – Campo 18 da SAFX08\.

Código do Produto – Campo 14 da SAFX08 de acordo com o cadastrado na SAFX2013\.

Descrição – Campo 14 da SAFX08 de acordo com o cadastrado na SAFX2013\.

Descrição Complementar – Campo 21 da SAFX08\.

NCM – Campo 26 da SAFX08 de acordo com o cadastrado na SAFX2043\.

CFOP – Campo 22 da SAFX08 de acordo com o cadastrado na SAFX2012\.

Nat\. Operação – Campo 23 da SAFX08 de acordo com o cadastrado na SAFX2006\.

CST A/B – Campo 30 \+ campo 31 \(separado por barra “/”\) de acordo com o cadastrado na SAFX2025 e SAFX2026\.

Valor Unitário – Campo 27 da SAFX08\.

Quantidade – Campo 24 da SAFX08\.

Valor Total – Campo \.

Valor Contábil – Campo 64 da SAFX08\.

Valor Desconto – Campo 29 da SAFX08\.

Base ICMS – Campo 56 da SAFX08\.

Aliq\. Trib\. ICMS – Campo 42 da SAFX08\.

Vlr\. Trib\. ICMS – Campo 43 da SAFX08\.

Base Red\. ICMS – Campo 57 da SAFX08\.

Base ICMSS – Campo 61 da SAFX08\.

Vlr\. ICMS NDESTAC – Campo 80 da SAFX08\.

Vlr\. IPI NDESTAC – Campo 81 da SAFX08\.

Vlr\. Tributo ICMSS – Campo 94 da SAFX08\.

Valor Isentas – <a id="OLE_LINK198"></a><a id="OLE_LINK199"></a><a id="OLE_LINK200"></a>Campo 56 quando o campo 57 = 2 da SAFX08\.

Valor Outras – Campo 56 quando o campo 57 = 3 da SAFX08\.

Código de Tributação IPI – Campo 146 da SAFX08\.

Base IPI – Campo 59 quando o campo 58 = 1 da SAFX08\.

IPI Isentas – Campo 59 quando o campo 58 = 2 da SAFX08\.

IPI Outras – Campo 59 quando o campo 58 =3 da SAFX08\.

Alíquota IPI – Campo 47 da SAFX08\.	

Valor IPI – Campo 48 da SAFX08\.

Alíq\. Diferença – Campo 44 da SAFX08\.

Valor DIFAL – Campo 68 da SAFX08\.

Valor FCP UF Destino – Campo 221 da SAFX08\.

Valor ICMS UF Destino – Campo 222 da SAFX08\.

Valor ICMS UF Origem – Campo 223 da SAFX08\.

Campo Observação LF E/S – Campo 45 da SAFX08\.

Campo Valor do FCP UF Destino

Campo Valor ICMS UF Destino

Campo Valor ICMS UF Origem

Campo CST PIS

Campo CST COFINS

Campo Alíquota PIS

Campo Alíquota COFINS

Campo Base de Cálculo PIS

Campo Base de Cálculo COFINS

Campo Valor PIS

Campo Valor COFINS

Campo Base de Cálculo PIS\-ST

Campo Alíquota do PIS\-ST

Campo Valor Tributo PIS\-ST

Campo Base de Calculo COFINS\-ST

Campo Alíquota da COFINS\-ST

Campo Valor Tributo COFINS\-ST

Campo Quantidade \- Base de Cálculo PIS

Campo Alíquota do PIS \- Em Reais

Campo Quantidade \- Base de Cálculo COFINS

Campo Alíquota do COFINS \- Em Reais

Campo cod\_und\_padrao

Campo dsc\_und\_padrao\_1

Campo vlr\_icms\_ndestac

Campo vlr\_base\_icmss\_n\_escrit

Campo vlr\_icmss\_ndestac

Campo vlr\_aliq\_sub\_icms

Campo vlr\_outras

Campo vlr\_fecp\_icms

Campo vlr\_fecp\_difaliq

Campo vlr\_fecp\_icms\_st

Campo vlr\_fecp\_fonte

Campo cod\_conta

Campo cod\_custo

Campo num\_docfis\_ref

Campo serie\_docfis\_ref

Campo desc\_municipio

Campo cod\_beneficio

Campo vlr\_base\_inss – Campo 85 da SAFX07\.

Campo vlr\_aliq\_inss – Campo 86 da SAFX07\.

Campo vlr\_inss\_retido – Campo 87 da SAFX07\.

Campo insc\_estad\_substit – Campo 21 da SAFX07

Observação: Esses campos deverão ser demonstrados no relatório de acordo com a nomenclatura a seguir, é a mesma regra e composição do relatório padrão, porém com a distribuição diferente:

movto\_e\_s/ norm\_dev/ ident\_docto/ ident\_fis\_jur/ num\_docfis/ serie\_docfis/ sub\_serie\_docfis/ num\_item / ind\_produto/ cod\_produto/ dsc\_produto/ num\_controle\_docto/ data\_emissao/ cod\_modelo/ num\_autentic\_nfe/ descricao\_compl/ cod\_nbm/ cod\_cfo/ cod\_natureza\_op/ cod\_situacao\_a/ cod\_situacao\_b/ vlr\_unit/ quantidade/ vlr\_tot\_nota/ vlr\_contab\_item/ vlr\_base\_icms/ vlr\_aliq\_icms/ vlr\_icms/ vlr\_icms\_ndestac/ vlr\_ipi\_ndestac/ vlr\_subst\_icms/ vlr\_base\_isentas/ vlr\_base\_outras/ dif\_aliq\_tributo/ vlr\_difal/ dsc\_observacao/ cod\_docto/ descricao/ ind\_fis\_jur/ cod\_fis\_jur/ cpf\_cgc/ razao\_social/ insc\_estadual/ vlr\_base\_red/ cod\_estado/ cod\_empresa/ vlr\_desconto/ cod\_trib\_ipi/ vlr\_base\_ipi/ vlr\_aliq\_ipi/ vlr\_ipi\./ vlr\_fcp\_uf\_dest/ vlr\_icms\_uf\_dest/ vlr\_icms\_uf\_orig/ base\_ipi/  trib\_ipi/  base\_sub\_trib\_icms /  vlr\_base\_inss /  vlr\_aliq\_inss /  vlr\_inss\_retido /  insc\_estad\_substit 

OS4774

CH13715\_2015

MFS\_3582

MFS4310

MFS14922

MFS70186

  


Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

