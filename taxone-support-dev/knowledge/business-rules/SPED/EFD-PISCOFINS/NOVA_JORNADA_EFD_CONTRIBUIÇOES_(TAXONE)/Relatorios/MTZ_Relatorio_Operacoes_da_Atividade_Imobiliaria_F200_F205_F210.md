# MTZ_Relatorio_Operacoes_da_Atividade_Imobiliaria_F200_F205_F210

- **Fonte:** MTZ_Relatorio_Operacoes_da_Atividade_Imobiliaria_F200_F205_F210.docx
- **Modificado:** 2026-03-05
- **Tamanho:** 94 KB

---

THOMSON REUTERS

Módulo EFD \- 

__Relatório de Operações da Atividade Imobiliária \(F200, F205 e F210\)__

__Localização__: Produto: TAXONE, Menu SPED, Módulo: EFD \- EFD\-Escrituração Fiscal Digital das Contribuições, item de menu Relatórios à 

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

__Data __

MFS\-978929

Alessandra Cristina Navatta

Criação do relatório de Operações da Atividade Imobiliária \(F200, F205 e F210\), apenas no produto TAXONE

19/02/2026

Sumário

[OBJETIVO	3](#_Toc222739928)

[REGRAS DOS CAMPOS	3](#_Toc222739929)

[1\.	REGRAS DE GERAÇÃO DO RELATÓRIO	5](#_Toc222739930)

[1\.1\.	Layout do Relatório	15](#_Toc222739931)

# <a id="_Toc350763252"></a><a id="_Toc427766285"></a><a id="_Toc222739928"></a>OBJETIVO

Desenvolver um relatório no TAXONE que permita realizar a conferência, validação e análise das informações relacionadas às operações da atividade imobiliária, contemplando os registros F200, F205 e F210 do SPED Contribuições\.

# <a id="_Toc222739929"></a>REGRAS DOS CAMPOS 

__Localização da tela:__ Menu: SPED, Módulo: EFD \- Escrituração Fiscal Digital das Contribuições, item de menu Relatórios

__Título da tela: __Operações da Atividade Imobiliária \(F200, F205 e F210\)

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS__

Período

Data 

S

S

Formato: MM/AAAA 

Default: Habilitado

Este campo servirá para informar a a competência  \(mês/ano\) da Operação de Venda que o sistema deverá considerar para seleção das informações para a criação do relatório\.

MFS\-978929

Tipo do Arquivo

Listbox

S

S

Default: Arquivo PDF

Permitir que o usuário informe qual o tipo de arquivo será gerado entre as opções:

\- Arquivo PDF

\- Excel \(XLSX\)

MFS\-978929

Estabelecimentos

CheckBox

S

S

XXX / XXXXX\-XXXXXXXXXXXXXXXXX

\(cód\. empresa \+ cód\. e razão social do estabelecimento centralizador\) ou

XXX / XXXXX\-XXXXXXXXXXXXXXXXX

\(cód\. empresa \+ cód\. e razão social do estabelecimento descentralizado\) 

Default: não selecionado

Na lista será demonstrado os estabelecimentos da empresa logada e que o usuário tenha acesso\.

Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”\.

MFS\-978929

Executar

__Campos de preenchimento obrigatório não preenchido:__

Se um campo obrigatório não for preenchido, exibir a mensagem: “<<Nome do campo que é exibido em tela>> deve ser preenchido\!”

MFS\-978929

# <a id="_Toc427766287"></a><a id="_Toc222739930"></a>REGRAS DE GERAÇÃO DO RELATÓRIO 

__Regra Geral: __

 O relatório terá as opções de salvar em Excel e em PDF

__Origem das informações para geração:__ 

Para geração deste relatório, serão consideradas as informações da seguinte origem:

-  As informações das tabelas SAFX150, SAFX151 e SAFX152 respectivamente, que são utilizadas para a geração dos Registros F200, F205 e F210 do SPED das Contribuições, conforme a data de competência

__Regra de seleção: __

A geração do relatório será de acordo com os critérios de filtro informados na tela de geração\.

      \-Empresa = empresa do login      

      \-Período = mês/ano da competência da operação de venda indicada em tela

      \-Estabelecimento = estabelecimento informado em tela

    

Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a mensagem “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no relatório\. 

__Regra de processamento: __

__ __

Para cada estabelecimento selecionado em tela será gerado um relatório\. 

Serão recuperadas as informações das SAFX150, SAFX151 e SAFX152, de acordo com a regra de seleção e os dados do cadastro da unidade imobiliária deve ser recuperada na SAFX149\.L

__Ordenação: __

Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

          \- Empresa 

          \- Estabelecimento

          \- Indicador do Tipo da Operação

                                      \- Indicador do tipo de unidade imobiliária vendida

                                     \- Identificação/nome do empreendimento

                                     \- Número do contrato 

                                     \- Identificação da PF ou da PJ Adquirente da Unidade Imobiliária

                                     \- Indicador da Natureza do Empreendimento

                                     \- Data da Operação 

__Nomenclatura: __

Relatorio\_Operacoes\_da\_Atividade\_Imobiliaria\_F200\_F205\_F210\_Cod\.Empresa\_Cod\_Estab\_PERIODO\.xls

  


Segue regras do preenchimento dos dados no relatório:

__Campo/Coluna__

__Tipo__

__Formato/Default__

__Regra__

__MFS/CH__

__Dados do Cabeçalho__

Empresa

Texto

Razão social da empresa\.

MFS\-978929

Página

Numérico

Número da página sequencial do relatório

MFS\-978929

Data

Data

DD/MM/AAAA às HH:MM:SS hs

Data de emissão e hora do relatório

MFS\-978929

Título

Texto

Título do relatório: “Relatório de Operações da Atividade Imobiliária \(F200, F205 e F210\)”

MFS\-978929

Período

Data

Formato: MM/AAAA

Deverá ser exibido o período da competência da operação de venda, informadas em tela\.

MFS\-978929

__Corpo do Relatório__

Estabelecimento

Texto 

Estabelecimento informado em tela

MFS\-978929

<a id="_Toc74655896"></a>__Corpo do Relatório__

__Registro F200: Operações da Atividade Imobiliária \- Unidade Imobiliária Vendida__

Indicador do Tipo de Operação

Texto

Código\-Descrição

Gravar o contéudo do campo “05\- Indicador do Tipo de operação ” da tabela SAFX149  que está relacionada ao movimento na tabela SAFX150\.

MFS\-978929

Indicador do Tipo de unidade imobiliária Vendida

Texto

Código\-Descrição

Neste campo deve gravar o conteúdo do campo 05\- Indicador do Tipo da Unidade Imobiliária da tabela SAFX2054 referente ao código da unidade imobiliária \(campo 03\) informada na tabela SAFX150\.

MFS\-978929

Identificação/Nome do Empreendimento

Texto

Descrição

Neste campo deve gravar o conteúdo do campo 06\- Identificação/Nome do Empreendimento da tabela SAFX2054 referente ao código da unidade imobiliária \(campo 03\) informada na tabela SAFX150\.

MFS\-978929

Número do Contrato/Documento que Formaliza a Venda da Unidade Imobiliária

Texto

Gravar o contéudo do campo “06\- Número de Contrato ” da tabela SAFX149  que está relacionada ao movimento na tabela SAFX150\.

MFS\-978929

Identificação da PF \(CPF\) ou da PJ \(CNPJ\) Adquirente da Unidade Imobiliária

Texto

999\.999\.999/99 ou

99\.999\.999\\9999\-99

Esta informação deve ser gerada a partir do campo 07“__ __Indicador da Pessoa Fis/Jur Adquirente” e o campo __ __08 ‘’Código da Pessoa Fis/Jur Adquirente’’ na SAFX149\.

Buscar o CNPJ na SAFX04 a partir da pessoa fis/jur\. informada\. 

MFS\-978929

Indicador da Natureza do Empreendimento

Texto

Código\-Descrição

Neste campo deve gravar o conteúdo do campo 08\- Indicador da natureza específica do empreendimento da tabela SAFX2054 referente ao código da unidade imobiliária \(campo 03\) informada na tabela SAFX150\.

MFS\-978929

Data da Operação

Texto

DD/MM/AAAA

Gravar o conteúdo do campo 04\- Data da Operação da venda da unidade imobiliária da tabela SAFX149 que está relacionada ao movimento na tabela SAFX150\.

MFS\-978929

Valor Total Unidade Vendida

Texto

999\.999\.999\.999,99

Campo 06 \- VLR\_TOT\_VENDA\_UNID\_IMOB da SAFX150

MFS\-978929

Valor Recebido Acumulado \(Até Mês Anterior\)

Texto

999\.999\.999\.999,99

Campo 07 \- VLR\_REC\_ACUM\_MES\_ANT da SAFX150 

MFS\-978929

Valor Total Recebido \(Mês\)

Texto

999\.999\.999\.999,99

Campo 08 \- VLR\_TOT\_REC\_MES\_ESCRIT da SAFX150

MFS\-978929

Percentual Receita Total Recebida até o Mês

Texto

99,9999

Resultado da expressão \(\(Campo 07 \-Campo 08\)/Campo 06\) da SAFX150

MFS\-978929

Agrupamento PIS 

CST

Texto

999

Campo 09 \- COD\_SIT\_PIS da SAFX150

MFS\-978929

Valor Base

Texto

999\.999\.999\.999,99

Campo 10 – VLR\_BASE\_PIS da SAFX150

MFS\-978929

Alíquota

Texto

99,9999

Campo 11 – VLR\_ALIQ\_PIS da SAFX150

MFS\-978929

Imposto

Texto

999\.999\.999\.999,99

Campo 12 – VLR\_PIS da SAFX150

MFS\-978929

Agrupamento COFINS

CST

Texto

999

Campo 13 \- COD\_SIT\_COFINS da SAFX150

MFS\-978929

Valor Base

Texto

999\.999\.999\.999,99

Campo 14 – VLR\_BASE\_COFINS da SAFX150

MFS\-978929

Alíquota

Texto

99,9999

Campo 15 – VLR\_ALIQ\_COFINS da SAFX150

MFS\-978929

Imposto

Texto

999\.999\.999\.999,99

Campo 16 – VLR\_COFINS da SAFX150

MFS\-978929

<a id="_Toc74655897"></a>__Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária__

Valor Total Custo Acumulado até o Mês Anterior Escrituração

Texto

999\.999\.999\.999,99

Campo 06 – VLR\_TOT\_CUSTO\_MES\_ANT da SAFX151

 

MFS\-978929

Valor Total Custo no Mês da Escrituração

Texto

999\.999\.999\.999,99

Campo 07 – VLR\_TOT\_CUSTO\_MES da SAFX151

MFS\-978929

Valor Total Custo Acumulado até o Mês Escrituração

Texto

999\.999\.999\.999,99

Resultado da expressão \(Campo 06 \+ Campo 07 da SAFX151\)

MFS\-978929

Parcela Custo sem Direito ao Crédito Acumulado até o Período

Texto

999\.999\.999\.999,99

Campo 08 – VLR\_PARC\_S\_CRED\_ACUM da SAFX151

MFS\-978929

Valor Base Cálculo Crédito sobre o Custo, Acumulado até o Período Escrituração

Texto

999\.999\.999\.999,99

Campo 09 – VLR\_BASE\_CRED\_CUSTO da SAFX151

MFS\-978929

Agrupamento PIS 

CST

Texto

999

Campo 10 – COD\_SIT\_PIS da SAFX151

MFS\-978929

Alíquota

Texto

99,9999

Campo 12 – VLR\_ALIQ\_PIS da SAFX151

MFS\-978929

Valor Total Crédito Acumulado sobre Custo

Texto

999\.999\.999\.999,99

Campo 11 – VLR\_TOT\_CRED\_ACUM\_PIS da SAFX151

MFS\-978929

Parcela Crédito Descontada até o Período Anterior Escrituração

Texto

999\.999\.999\.999,99

Campo 13 – VLR\_PARC\_CRED\_DESC\_PIS da SAFX151

MFS\-978929

Parcela a Descontar no Período Escrituração

Texto

999\.999\.999\.999,99

Campo 14 – VLR\_PARC\_ADESC\_PIS da SAFX151

MFS\-978929

Parcela a Descontar em Períodos Futuros

Texto

999\.999\.999\.999,99

Resultado da expressão \(Campo 11 – 13 – 14\) da SAFX151

MFS\-978929

Agrupamento COFINS

CST

Texto

999

Campo 15 – COD\_SIT\_COFINS da SAFX151

MFS\-978929

Alíquota

Texto

99,9999

Campo 17 – VLR\_ALIQ\_COFINS da SAFX151

MFS\-978929

Valor Total Crédito Acumulado sobre Custo

Texto

999\.999\.999\.999,99

Campo 16 – VLR\_TOT\_CRED\_ACUM\_COFINS da SAFX151

MFS\-978929

Parcela Crédito Descontada até o Período Anterior Escrituração

Texto

999\.999\.999\.999,99

Campo 18 – VLR\_PARC\_CRED\_DESC\_COFINS da SAFX151

MFS\-978929

Parcela a Descontar no Período Escrituração

Texto

999\.999\.999\.999,99

Campo 19 – VLR\_PARC\_ADESC\_COFINS da SAFX151

MFS\-978929

Parcela a Descontar em Períodos Futuros

Texto

999\.999\.999\.999,99

Resultado da expressão \(Campo 16 – 18 – 19\) da SAFX151

MFS\-978929

<a id="_Toc74655898"></a>__Registro F210: Operações da Atividade Imobiliária \- Custo Orçado da Unidade Imobiliária Vendida__

Valor Total Custo Orçado para Conclusão da Unidade Vendida

Texto

999\.999\.999\.999,99

Campo 06 – VLR\_TOT\_CUSTO\_ORC da SAFX152

 

MFS\-978929

Valores Ref\. a Pagtos a PF, Encargos Trabalhistas, Sociais e Previdenc\. e à Aquisição de Bens e Serviços não Sujeitos ao Pagto Contribuições

Texto

999\.999\.999\.999,99

Campo 07 – VLR\_AQ\_SERV\_NPAG\_CONTRIB da SAFX152

MFS\-978929

Valor Base Cálculo Crédito sobre o Custo Orçado Ajustado

Texto

999\.999\.999\.999,99

Campo 08 – VLR\_BASE\_CRED\_ORC da SAFX152

MFS\-978929

Valor Base Cálculo Crédito sobre o Custo Orçado Ref\. ao Mês Escrituração

Texto

999\.999\.999\.999,99

Campo 09 – VLR\_BASE\_CRED\_ORC\_PROP da SAFX152

MFS\-978929

Agrupamento PIS 

CST

Texto

999

Campo 10 – COD\_SIT\_PIS da SAFX152

MFS\-978929

Alíquota \(%\)

Texto

99,9999

Campo 11 – VLR\_ALIQ\_PIS da SAFX152

MFS\-978929

Valor Crédito sobre o Custo Orçado a ser Utilizado no Período Escrituração

Texto

999\.999\.999\.999,99

Campo 12 – VLR\_CRED\_UTIL\_PIS da SAFX152

MFS\-978929

Agrupamento COFINS

CST

Texto

999

Campo 13 – COD\_SIT\_COFINS da SAFX152

MFS\-978929

Alíquota \(%\)

Texto

99,9999

Campo 14 – VLR\_ALIQ\_COFINS da SAFX152

MFS\-978929

Valor Crédito sobre o Custo Orçado a ser Utilizado no Período Escrituração

Texto

999\.999\.999\.999,99

Campo 15 – VLR\_CRED\_UTIL\_COFINS da SAFX152

MFS\-978929

## <a id="_Toc427766288"></a><a id="_Toc222739931"></a>Layout do Relatório

Formato: PDF:

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ===============================

__Empresa:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                           						   Página\.: 999999__

__Data: 99/99/9999 às HH:MM:SS  hs__

__                                                        			 Relatório de Operações da Atividade Imobiliária \(F200, F205 e F210\)__

__                                                                                      		Período: 99/9999 __

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ================================

__Estabelecimento__: XXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

__Registro F200: Operações da Atividade Imobiliária \- Unidade Imobiliária Vendida__

__Indicador do Tipo de Operação:__ 99 – Xxxxxxxx

__Indicador do Tipo de Unidade Imobiliária Vendida__: 99 – Xxxxxxxx

__Identificação/Nome do Empreendimento : __XXXXXXXXXX

__Número do Contrato/Documento que Formaliza a Venda da Unidade Imobiliária:__ XXXXXXXXXXXXXXX

__Identificação da PF \(CPF\) ou da PJ\(CNPJ\) Adquirente da Unidade Imobiliária: __999\.999\.999/99

__Indicador da Natureza do Empreendimento: __99 \- Xxxxxxxx

__Data da Operação: __DD/MM/AAAA

__Valor Total Unidade Vendida__

__Valor Recebido Acumulado \(Até Mês Anterior\)__

__Valor Total Recebido \(Mês\) __

__Percentual Receita Total Recebida até o Mês__

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

99,9999

__PIS__

__COFINS__

__CST__

__Valor Base__

__Alíquota__

__Imposto__

__CST__

__Valor Base__

__Alíquota__

__Imposto__

999

999\.999\.999\.999,99

99,9999

999\.999\.999\.999,99

999

999\.999\.999\.999,99

99,9999

999\.999\.999\.999,99

__Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária__

__Valor Total Custo Acumulado até o Mês Anterior Escrituração__

__Valor Total Custo no Mês da Escrituração__

__Valor Total Custo Acumulado até o Mês Escrituração __

__Parcela Custo sem Direito ao Crédito Acumulado até o Período__

__Valor Base Cálculo Crédito sobre o Custo, Acumulado até o Período Escrituração __

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

__PIS__

__CST __

__Alíquota__

__Valor Total Crédito Acumulado sobre Custo __

__Parcela Crédito Descontada até o Período Anterior Escrituração__

__Parcela a Descontar no Período Escrituração __

__Parcela a Descontar em Períodos Futuros __

999

99,9999

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

__COFINS__

__CST __

__Alíquota__

__Valor Total Crédito Acumulado sobre Custo __

__Parcela Crédito Descontada até o Período Anterior Escrituração__

__Parcela a Descontar no Período Escrituração __

__Parcela a Descontar em Períodos Futuros __

999

99,9999

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

__Registro F210: Operações da Atividade Imobiliária \- Custo Orçado da Unidade Imobiliária Vendida__

__Valor Total Custo Orçado para Conclusão da Unidade Vendida__

__Valores Ref\. a Pagtos a PF, Encargos Trabalhistas, Sociais e Previdenc\. e à Aquisição de Bens e Serviços não Sujeitos ao Pagto Contribuições__

__Valor Base Cálculo Crédito sobre o Custo Orçado Ajustado__

__Valor Base Cálculo Crédito sobre o Custo Orçado Ref\. ao Mês Escrituração__

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

__PIS__

__COFINS__

__CST__

__Alíquota \(%\)__

__Valor Crédito sobre o Custo Orçado a ser Utilizado no Período Escrituração__

__CST__

__Alíquota \(%\)__

__Valor Crédito sobre o Custo Orçado a ser Utilizado no Período Escrituração__

999

99,9999

9\.999\.999\.999,99

999

99,9999

999\.999\.999\.999,99

Formato Excel:

Considerar as colunas indicadas no arquivo:__ Layout\_Relatorio\_Operacoes\_da\_Atividade\_Imobiliaria\_F200\_F205\_F210\.xlsx__

