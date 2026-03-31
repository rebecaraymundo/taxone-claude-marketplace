# MTZ_Relatorio_Operacoes_da_Atividade_Imobiliaria_F200_F205_F210

> Fonte: MTZ_Relatorio_Operacoes_da_Atividade_Imobiliaria_F200_F205_F210.docx






THOMSON REUTERS

Módulo EFD -
Relatório de Operações da Atividade Imobiliária (F200, F205 e F210)

Localização: Produto: TAXONE, Menu SPED, Módulo: EFD - EFD-Escrituração Fiscal Digital das Contribuições, item de menu Relatórios à



DOCUMENTO DE REQUISITO





Sumário

OBJETIVO	3
REGRAS DOS CAMPOS	3
1.	REGRAS DE GERAÇÃO DO RELATÓRIO	5
1.1.	Layout do Relatório	15
## OBJETIVO


Desenvolver um relatório no TAXONE que permita realizar a conferência, validação e análise das informações relacionadas às operações da atividade imobiliária, contemplando os registros F200, F205 e F210 do SPED Contribuições.

## REGRAS DOS CAMPOS


Localização da tela: Menu: SPED, Módulo: EFD - Escrituração Fiscal Digital das Contribuições, item de menu Relatórios
Título da tela: Operações da Atividade Imobiliária (F200, F205 e F210)










## REGRAS DE GERAÇÃO DO RELATÓRIO


Regra Geral:

O relatório terá as opções de salvar em Excel e em PDF

Origem das informações para geração:

Para geração deste relatório, serão consideradas as informações da seguinte origem:
As informações das tabelas SAFX150, SAFX151 e SAFX152 respectivamente, que são utilizadas para a geração dos Registros F200, F205 e F210 do SPED das Contribuições, conforme a data de competência


Regra de seleção:

A geração do relatório será de acordo com os critérios de filtro informados na tela de geração.

-Empresa = empresa do login
-Período = mês/ano da competência da operação de venda indicada em tela
-Estabelecimento = estabelecimento informado em tela


Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a mensagem “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no relatório.


Regra de processamento:

Para cada estabelecimento selecionado em tela será gerado um relatório.
Serão recuperadas as informações das SAFX150, SAFX151 e SAFX152, de acordo com a regra de seleção e os dados do cadastro da unidade imobiliária deve ser recuperada na SAFX149.L


Ordenação:
Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

- Empresa
- Estabelecimento
- Indicador do Tipo da Operação
- Indicador do tipo de unidade imobiliária vendida
- Identificação/nome do empreendimento
- Número do contrato
- Identificação da PF ou da PJ Adquirente da Unidade Imobiliária
- Indicador da Natureza do Empreendimento
- Data da Operação
Nomenclatura:
Relatorio_Operacoes_da_Atividade_Imobiliaria_F200_F205_F210_Cod.Empresa_Cod_Estab_PERIODO.xls


Segue regras do preenchimento dos dados no relatório:




### Layout do Relatório

Formato: PDF:


= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ===============================
Empresa:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                           						   Página.: 999999
Data: 99/99/9999 às HH:MM:SS  hs

Relatório de Operações da Atividade Imobiliária (F200, F205 e F210)
Período: 99/9999
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ================================
Estabelecimento: XXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


Formato Excel:

Considerar as colunas indicadas no arquivo: Layout_Relatorio_Operacoes_da_Atividade_Imobiliaria_F200_F205_F210.xlsx

| MFS | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-978929 | Alessandra Cristina Navatta | Criação do relatório de Operações da Atividade Imobiliária (F200, F205 e F210), apenas no produto TAXONE | 19/02/2026 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS |
| --- | --- | --- | --- | --- | --- | --- |
| Período | Data | S | S | Formato: MM/AAAA  Default: Habilitado | Este campo servirá para informar a a competência  (mês/ano) da Operação de Venda que o sistema deverá considerar para seleção das informações para a criação do relatório. | MFS-978929 |
| Tipo do Arquivo | Listbox | S | S | Default: Arquivo PDF | Permitir que o usuário informe qual o tipo de arquivo será gerado entre as opções:  - Arquivo PDF - Excel (XLSX) | MFS-978929 |
| Estabelecimentos | CheckBox | S | S | XXX / XXXXX-XXXXXXXXXXXXXXXXX  (cód. empresa + cód. e razão social do estabelecimento centralizador) ou  XXX / XXXXX-XXXXXXXXXXXXXXXXX  (cód. empresa + cód. e razão social do estabelecimento descentralizado)    Default: não selecionado | Na lista será demonstrado os estabelecimentos da empresa logada e que o usuário tenha acesso.  Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”. | MFS-978929 |
| Executar |  |  |  |  | Campos de preenchimento obrigatório não preenchido: Se um campo obrigatório não for preenchido, exibir a mensagem: “<<Nome do campo que é exibido em tela>> deve ser preenchido!” | MFS-978929 |


| Campo/Coluna | Tipo | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Empresa | Texto | Texto |  | Razão social da empresa. | MFS-978929 |
| Página | Numérico | Numérico |  | Número da página sequencial do relatório | MFS-978929 |
| Data | Data | Data | DD/MM/AAAA às HH:MM:SS hs | Data de emissão e hora do relatório | MFS-978929 |
| Título | Texto | Texto |  | Título do relatório: “Relatório de Operações da Atividade Imobiliária (F200, F205 e F210)” | MFS-978929 |
| Período | Data | Data | Formato: MM/AAAA | Deverá ser exibido o período da competência da operação de venda, informadas em tela. | MFS-978929 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Estabelecimento | Texto | Texto |  | Estabelecimento informado em tela | MFS-978929 |
| Corpo do Relatório Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Corpo do Relatório Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Corpo do Relatório Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Corpo do Relatório Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Corpo do Relatório Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Corpo do Relatório Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida |
| Indicador do Tipo de Operação | Texto | Texto | Código-Descrição | Gravar o contéudo do campo “05- Indicador do Tipo de operação ” da tabela SAFX149  que está relacionada ao movimento na tabela SAFX150. | MFS-978929 |
| Indicador do Tipo de unidade imobiliária Vendida | Texto | Texto | Código-Descrição | Neste campo deve gravar o conteúdo do campo 05- Indicador do Tipo da Unidade Imobiliária da tabela SAFX2054 referente ao código da unidade imobiliária (campo 03) informada na tabela SAFX150. | MFS-978929 |
| Identificação/Nome do Empreendimento | Texto | Texto | Descrição | Neste campo deve gravar o conteúdo do campo 06- Identificação/Nome do Empreendimento da tabela SAFX2054 referente ao código da unidade imobiliária (campo 03) informada na tabela SAFX150. | MFS-978929 |
| Número do Contrato/Documento que Formaliza a Venda da Unidade Imobiliária | Texto | Texto |  | Gravar o contéudo do campo “06- Número de Contrato ” da tabela SAFX149  que está relacionada ao movimento na tabela SAFX150. | MFS-978929 |
| Identificação da PF (CPF) ou da PJ (CNPJ) Adquirente da Unidade Imobiliária | Texto | Texto | 999.999.999/99 ou 99.999.999\9999-99 | Esta informação deve ser gerada a partir do campo 07“ Indicador da Pessoa Fis/Jur Adquirente” e o campo  08 ‘’Código da Pessoa Fis/Jur Adquirente’’ na SAFX149. Buscar o CNPJ na SAFX04 a partir da pessoa fis/jur. informada. | MFS-978929 |
| Indicador da Natureza do Empreendimento | Texto | Texto | Código-Descrição | Neste campo deve gravar o conteúdo do campo 08- Indicador da natureza específica do empreendimento da tabela SAFX2054 referente ao código da unidade imobiliária (campo 03) informada na tabela SAFX150. | MFS-978929 |
| Data da Operação | Texto | Texto | DD/MM/AAAA | Gravar o conteúdo do campo 04- Data da Operação da venda da unidade imobiliária da tabela SAFX149 que está relacionada ao movimento na tabela SAFX150. | MFS-978929 |
| Valor Total Unidade Vendida | Texto | Texto | 999.999.999.999,99 | Campo 06 - VLR_TOT_VENDA_UNID_IMOB da SAFX150 | MFS-978929 |
| Valor Recebido Acumulado (Até Mês Anterior) | Texto | Texto | 999.999.999.999,99 | Campo 07 - VLR_REC_ACUM_MES_ANT da SAFX150 | MFS-978929 |
| Valor Total Recebido (Mês) | Texto | Texto | 999.999.999.999,99 | Campo 08 - VLR_TOT_REC_MES_ESCRIT da SAFX150 | MFS-978929 |
| Percentual Receita Total Recebida até o Mês | Texto | Texto | 99,9999 | Resultado da expressão ((Campo 07 -Campo 08)/Campo 06) da SAFX150 | MFS-978929 |
| Agrupamento PIS | Agrupamento PIS | Agrupamento PIS | Agrupamento PIS | Agrupamento PIS | Agrupamento PIS |
| CST | Texto | Texto | 999 | Campo 09 - COD_SIT_PIS da SAFX150 | MFS-978929 |
| Valor Base | Texto | Texto | 999.999.999.999,99 | Campo 10 – VLR_BASE_PIS da SAFX150 | MFS-978929 |
| Alíquota | Texto | Texto | 99,9999 | Campo 11 – VLR_ALIQ_PIS da SAFX150 | MFS-978929 |
| Imposto | Texto | Texto | 999.999.999.999,99 | Campo 12 – VLR_PIS da SAFX150 | MFS-978929 |
| Agrupamento COFINS | Agrupamento COFINS | Agrupamento COFINS | Agrupamento COFINS | Agrupamento COFINS | Agrupamento COFINS |
| CST | Texto | Texto | 999 | Campo 13 - COD_SIT_COFINS da SAFX150 | MFS-978929 |
| Valor Base | Texto | Texto | 999.999.999.999,99 | Campo 14 – VLR_BASE_COFINS da SAFX150 | MFS-978929 |
| Alíquota | Texto | Texto | 99,9999 | Campo 15 – VLR_ALIQ_COFINS da SAFX150 | MFS-978929 |
| Imposto | Texto | Texto | 999.999.999.999,99 | Campo 16 – VLR_COFINS da SAFX150 | MFS-978929 |
| Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária |
| Valor Total Custo Acumulado até o Mês Anterior Escrituração | Valor Total Custo Acumulado até o Mês Anterior Escrituração | Texto | 999.999.999.999,99 | Campo 06 – VLR_TOT_CUSTO_MES_ANT da SAFX151 | MFS-978929 |
| Valor Total Custo no Mês da Escrituração | Valor Total Custo no Mês da Escrituração | Texto | 999.999.999.999,99 | Campo 07 – VLR_TOT_CUSTO_MES da SAFX151 | MFS-978929 |
| Valor Total Custo Acumulado até o Mês Escrituração | Valor Total Custo Acumulado até o Mês Escrituração | Texto | 999.999.999.999,99 | Resultado da expressão (Campo 06 + Campo 07 da SAFX151) | MFS-978929 |
| Parcela Custo sem Direito ao Crédito Acumulado até o Período | Parcela Custo sem Direito ao Crédito Acumulado até o Período | Texto | 999.999.999.999,99 | Campo 08 – VLR_PARC_S_CRED_ACUM da SAFX151 | MFS-978929 |
| Valor Base Cálculo Crédito sobre o Custo, Acumulado até o Período Escrituração | Valor Base Cálculo Crédito sobre o Custo, Acumulado até o Período Escrituração | Texto | 999.999.999.999,99 | Campo 09 – VLR_BASE_CRED_CUSTO da SAFX151 | MFS-978929 |
| Agrupamento PIS | Agrupamento PIS | Agrupamento PIS | Agrupamento PIS | Agrupamento PIS | Agrupamento PIS |
| CST | CST | Texto | 999 | Campo 10 – COD_SIT_PIS da SAFX151 | MFS-978929 |
| Alíquota | Alíquota | Texto | 99,9999 | Campo 12 – VLR_ALIQ_PIS da SAFX151 | MFS-978929 |
| Valor Total Crédito Acumulado sobre Custo | Valor Total Crédito Acumulado sobre Custo | Texto | 999.999.999.999,99 | Campo 11 – VLR_TOT_CRED_ACUM_PIS da SAFX151 | MFS-978929 |
| Parcela Crédito Descontada até o Período Anterior Escrituração | Parcela Crédito Descontada até o Período Anterior Escrituração | Texto | 999.999.999.999,99 | Campo 13 – VLR_PARC_CRED_DESC_PIS da SAFX151 | MFS-978929 |
| Parcela a Descontar no Período Escrituração | Parcela a Descontar no Período Escrituração | Texto | 999.999.999.999,99 | Campo 14 – VLR_PARC_ADESC_PIS da SAFX151 | MFS-978929 |
| Parcela a Descontar em Períodos Futuros | Parcela a Descontar em Períodos Futuros | Texto | 999.999.999.999,99 | Resultado da expressão (Campo 11 – 13 – 14) da SAFX151 | MFS-978929 |
| Agrupamento COFINS | Agrupamento COFINS | Agrupamento COFINS | Agrupamento COFINS | Agrupamento COFINS | Agrupamento COFINS |
| CST | CST | Texto | 999 | Campo 15 – COD_SIT_COFINS da SAFX151 | MFS-978929 |
| Alíquota | Alíquota | Texto | 99,9999 | Campo 17 – VLR_ALIQ_COFINS da SAFX151 | MFS-978929 |
| Valor Total Crédito Acumulado sobre Custo | Valor Total Crédito Acumulado sobre Custo | Texto | 999.999.999.999,99 | Campo 16 – VLR_TOT_CRED_ACUM_COFINS da SAFX151 | MFS-978929 |
| Parcela Crédito Descontada até o Período Anterior Escrituração | Parcela Crédito Descontada até o Período Anterior Escrituração | Texto | 999.999.999.999,99 | Campo 18 – VLR_PARC_CRED_DESC_COFINS da SAFX151 | MFS-978929 |
| Parcela a Descontar no Período Escrituração | Parcela a Descontar no Período Escrituração | Texto | 999.999.999.999,99 | Campo 19 – VLR_PARC_ADESC_COFINS da SAFX151 | MFS-978929 |
| Parcela a Descontar em Períodos Futuros | Parcela a Descontar em Períodos Futuros | Texto | 999.999.999.999,99 | Resultado da expressão (Campo 16 – 18 – 19) da SAFX151 | MFS-978929 |
| Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida |
| Valor Total Custo Orçado para Conclusão da Unidade Vendida | Valor Total Custo Orçado para Conclusão da Unidade Vendida | Texto | 999.999.999.999,99 | Campo 06 – VLR_TOT_CUSTO_ORC da SAFX152 | MFS-978929 |
| Valores Ref. a Pagtos a PF, Encargos Trabalhistas, Sociais e Previdenc. e à Aquisição de Bens e Serviços não Sujeitos ao Pagto Contribuições | Valores Ref. a Pagtos a PF, Encargos Trabalhistas, Sociais e Previdenc. e à Aquisição de Bens e Serviços não Sujeitos ao Pagto Contribuições | Texto | 999.999.999.999,99 | Campo 07 – VLR_AQ_SERV_NPAG_CONTRIB da SAFX152 | MFS-978929 |
| Valor Base Cálculo Crédito sobre o Custo Orçado Ajustado | Valor Base Cálculo Crédito sobre o Custo Orçado Ajustado | Texto | 999.999.999.999,99 | Campo 08 – VLR_BASE_CRED_ORC da SAFX152 | MFS-978929 |
| Valor Base Cálculo Crédito sobre o Custo Orçado Ref. ao Mês Escrituração | Valor Base Cálculo Crédito sobre o Custo Orçado Ref. ao Mês Escrituração | Texto | 999.999.999.999,99 | Campo 09 – VLR_BASE_CRED_ORC_PROP da SAFX152 | MFS-978929 |
| Agrupamento PIS | Agrupamento PIS | Agrupamento PIS | Agrupamento PIS | Agrupamento PIS | Agrupamento PIS |
| CST | CST | Texto | 999 | Campo 10 – COD_SIT_PIS da SAFX152 | MFS-978929 |
| Alíquota (%) | Alíquota (%) | Texto | 99,9999 | Campo 11 – VLR_ALIQ_PIS da SAFX152 | MFS-978929 |
| Valor Crédito sobre o Custo Orçado a ser Utilizado no Período Escrituração | Valor Crédito sobre o Custo Orçado a ser Utilizado no Período Escrituração | Texto | 999.999.999.999,99 | Campo 12 – VLR_CRED_UTIL_PIS da SAFX152 | MFS-978929 |
| Agrupamento COFINS | Agrupamento COFINS | Agrupamento COFINS | Agrupamento COFINS | Agrupamento COFINS | Agrupamento COFINS |
| CST | CST | Texto | 999 | Campo 13 – COD_SIT_COFINS da SAFX152 | MFS-978929 |
| Alíquota (%) | Alíquota (%) | Texto | 99,9999 | Campo 14 – VLR_ALIQ_COFINS da SAFX152 | MFS-978929 |
| Valor Crédito sobre o Custo Orçado a ser Utilizado no Período Escrituração | Valor Crédito sobre o Custo Orçado a ser Utilizado no Período Escrituração | Texto | 999.999.999.999,99 | Campo 15 – VLR_CRED_UTIL_COFINS da SAFX152 | MFS-978929 |


| Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida | Registro F200: Operações da Atividade Imobiliária - Unidade Imobiliária Vendida |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Indicador do Tipo de Operação: 99 – Xxxxxxxx | Indicador do Tipo de Operação: 99 – Xxxxxxxx | Indicador do Tipo de Operação: 99 – Xxxxxxxx | Indicador do Tipo de Operação: 99 – Xxxxxxxx | Indicador do Tipo de Operação: 99 – Xxxxxxxx | Indicador do Tipo de Operação: 99 – Xxxxxxxx | Indicador do Tipo de Operação: 99 – Xxxxxxxx | Indicador do Tipo de Operação: 99 – Xxxxxxxx | Indicador do Tipo de Operação: 99 – Xxxxxxxx | Indicador do Tipo de Operação: 99 – Xxxxxxxx | Indicador do Tipo de Operação: 99 – Xxxxxxxx | Indicador do Tipo de Operação: 99 – Xxxxxxxx | Indicador do Tipo de Operação: 99 – Xxxxxxxx | Indicador do Tipo de Operação: 99 – Xxxxxxxx | Indicador do Tipo de Unidade Imobiliária Vendida: 99 – Xxxxxxxx | Indicador do Tipo de Unidade Imobiliária Vendida: 99 – Xxxxxxxx | Indicador do Tipo de Unidade Imobiliária Vendida: 99 – Xxxxxxxx | Indicador do Tipo de Unidade Imobiliária Vendida: 99 – Xxxxxxxx | Indicador do Tipo de Unidade Imobiliária Vendida: 99 – Xxxxxxxx | Indicador do Tipo de Unidade Imobiliária Vendida: 99 – Xxxxxxxx | Indicador do Tipo de Unidade Imobiliária Vendida: 99 – Xxxxxxxx | Indicador do Tipo de Unidade Imobiliária Vendida: 99 – Xxxxxxxx | Indicador do Tipo de Unidade Imobiliária Vendida: 99 – Xxxxxxxx | Indicador do Tipo de Unidade Imobiliária Vendida: 99 – Xxxxxxxx |
| Identificação/Nome do Empreendimento : XXXXXXXXXX | Identificação/Nome do Empreendimento : XXXXXXXXXX | Identificação/Nome do Empreendimento : XXXXXXXXXX | Identificação/Nome do Empreendimento : XXXXXXXXXX | Identificação/Nome do Empreendimento : XXXXXXXXXX | Identificação/Nome do Empreendimento : XXXXXXXXXX | Identificação/Nome do Empreendimento : XXXXXXXXXX | Identificação/Nome do Empreendimento : XXXXXXXXXX | Identificação/Nome do Empreendimento : XXXXXXXXXX | Identificação/Nome do Empreendimento : XXXXXXXXXX | Identificação/Nome do Empreendimento : XXXXXXXXXX | Identificação/Nome do Empreendimento : XXXXXXXXXX | Identificação/Nome do Empreendimento : XXXXXXXXXX | Identificação/Nome do Empreendimento : XXXXXXXXXX | Número do Contrato/Documento que Formaliza a Venda da Unidade Imobiliária: XXXXXXXXXXXXXXX | Número do Contrato/Documento que Formaliza a Venda da Unidade Imobiliária: XXXXXXXXXXXXXXX | Número do Contrato/Documento que Formaliza a Venda da Unidade Imobiliária: XXXXXXXXXXXXXXX | Número do Contrato/Documento que Formaliza a Venda da Unidade Imobiliária: XXXXXXXXXXXXXXX | Número do Contrato/Documento que Formaliza a Venda da Unidade Imobiliária: XXXXXXXXXXXXXXX | Número do Contrato/Documento que Formaliza a Venda da Unidade Imobiliária: XXXXXXXXXXXXXXX | Número do Contrato/Documento que Formaliza a Venda da Unidade Imobiliária: XXXXXXXXXXXXXXX | Número do Contrato/Documento que Formaliza a Venda da Unidade Imobiliária: XXXXXXXXXXXXXXX | Número do Contrato/Documento que Formaliza a Venda da Unidade Imobiliária: XXXXXXXXXXXXXXX | Número do Contrato/Documento que Formaliza a Venda da Unidade Imobiliária: XXXXXXXXXXXXXXX |
| Identificação da PF (CPF) ou da PJ(CNPJ) Adquirente da Unidade Imobiliária: 999.999.999/99 | Identificação da PF (CPF) ou da PJ(CNPJ) Adquirente da Unidade Imobiliária: 999.999.999/99 | Identificação da PF (CPF) ou da PJ(CNPJ) Adquirente da Unidade Imobiliária: 999.999.999/99 | Identificação da PF (CPF) ou da PJ(CNPJ) Adquirente da Unidade Imobiliária: 999.999.999/99 | Identificação da PF (CPF) ou da PJ(CNPJ) Adquirente da Unidade Imobiliária: 999.999.999/99 | Identificação da PF (CPF) ou da PJ(CNPJ) Adquirente da Unidade Imobiliária: 999.999.999/99 | Identificação da PF (CPF) ou da PJ(CNPJ) Adquirente da Unidade Imobiliária: 999.999.999/99 | Identificação da PF (CPF) ou da PJ(CNPJ) Adquirente da Unidade Imobiliária: 999.999.999/99 | Identificação da PF (CPF) ou da PJ(CNPJ) Adquirente da Unidade Imobiliária: 999.999.999/99 | Identificação da PF (CPF) ou da PJ(CNPJ) Adquirente da Unidade Imobiliária: 999.999.999/99 | Identificação da PF (CPF) ou da PJ(CNPJ) Adquirente da Unidade Imobiliária: 999.999.999/99 | Identificação da PF (CPF) ou da PJ(CNPJ) Adquirente da Unidade Imobiliária: 999.999.999/99 | Identificação da PF (CPF) ou da PJ(CNPJ) Adquirente da Unidade Imobiliária: 999.999.999/99 | Identificação da PF (CPF) ou da PJ(CNPJ) Adquirente da Unidade Imobiliária: 999.999.999/99 | Indicador da Natureza do Empreendimento: 99 - Xxxxxxxx | Indicador da Natureza do Empreendimento: 99 - Xxxxxxxx | Indicador da Natureza do Empreendimento: 99 - Xxxxxxxx | Indicador da Natureza do Empreendimento: 99 - Xxxxxxxx | Indicador da Natureza do Empreendimento: 99 - Xxxxxxxx | Indicador da Natureza do Empreendimento: 99 - Xxxxxxxx | Indicador da Natureza do Empreendimento: 99 - Xxxxxxxx | Indicador da Natureza do Empreendimento: 99 - Xxxxxxxx | Indicador da Natureza do Empreendimento: 99 - Xxxxxxxx | Indicador da Natureza do Empreendimento: 99 - Xxxxxxxx |
| Data da Operação: DD/MM/AAAA | Data da Operação: DD/MM/AAAA | Data da Operação: DD/MM/AAAA | Data da Operação: DD/MM/AAAA | Data da Operação: DD/MM/AAAA | Data da Operação: DD/MM/AAAA | Data da Operação: DD/MM/AAAA | Data da Operação: DD/MM/AAAA | Data da Operação: DD/MM/AAAA | Data da Operação: DD/MM/AAAA | Data da Operação: DD/MM/AAAA | Data da Operação: DD/MM/AAAA | Data da Operação: DD/MM/AAAA | Data da Operação: DD/MM/AAAA | Data da Operação: DD/MM/AAAA | Data da Operação: DD/MM/AAAA | Data da Operação: DD/MM/AAAA | Data da Operação: DD/MM/AAAA | Data da Operação: DD/MM/AAAA | Data da Operação: DD/MM/AAAA | Data da Operação: DD/MM/AAAA | Data da Operação: DD/MM/AAAA | Data da Operação: DD/MM/AAAA | Data da Operação: DD/MM/AAAA |
| Valor Total Unidade Vendida | Valor Total Unidade Vendida | Valor Total Unidade Vendida | Valor Total Unidade Vendida | Valor Total Unidade Vendida | Valor Total Unidade Vendida | Valor Total Unidade Vendida | Valor Recebido Acumulado (Até Mês Anterior) | Valor Recebido Acumulado (Até Mês Anterior) | Valor Recebido Acumulado (Até Mês Anterior) | Valor Recebido Acumulado (Até Mês Anterior) | Valor Recebido Acumulado (Até Mês Anterior) | Valor Recebido Acumulado (Até Mês Anterior) | Valor Recebido Acumulado (Até Mês Anterior) | Valor Recebido Acumulado (Até Mês Anterior) | Valor Total Recebido (Mês) | Valor Total Recebido (Mês) | Valor Total Recebido (Mês) | Valor Total Recebido (Mês) | Valor Total Recebido (Mês) | Percentual Receita Total Recebida até o Mês | Percentual Receita Total Recebida até o Mês | Percentual Receita Total Recebida até o Mês | Percentual Receita Total Recebida até o Mês |
| 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 99,9999 | 99,9999 | 99,9999 | 99,9999 |
| PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS |
| CST | CST | CST | Valor Base | Valor Base | Valor Base | Valor Base | Valor Base | Alíquota | Alíquota | Imposto | Imposto | Imposto | Imposto | Imposto | CST | CST | CST | Valor Base | Valor Base | Valor Base | Valor Base | Alíquota | Imposto |
| 999 | 999 | 999 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 99,9999 | 99,9999 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999 | 999 | 999 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 99,9999 | 999.999.999.999,99 |
| Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária | Registro F205: Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária |
| Valor Total Custo Acumulado até o Mês Anterior Escrituração | Valor Total Custo Acumulado até o Mês Anterior Escrituração | Valor Total Custo Acumulado até o Mês Anterior Escrituração | Valor Total Custo Acumulado até o Mês Anterior Escrituração | Valor Total Custo no Mês da Escrituração | Valor Total Custo no Mês da Escrituração | Valor Total Custo no Mês da Escrituração | Valor Total Custo no Mês da Escrituração | Valor Total Custo no Mês da Escrituração | Valor Total Custo no Mês da Escrituração | Valor Total Custo no Mês da Escrituração | Valor Total Custo Acumulado até o Mês Escrituração | Valor Total Custo Acumulado até o Mês Escrituração | Valor Total Custo Acumulado até o Mês Escrituração | Valor Total Custo Acumulado até o Mês Escrituração | Valor Total Custo Acumulado até o Mês Escrituração | Valor Total Custo Acumulado até o Mês Escrituração | Parcela Custo sem Direito ao Crédito Acumulado até o Período | Parcela Custo sem Direito ao Crédito Acumulado até o Período | Parcela Custo sem Direito ao Crédito Acumulado até o Período | Parcela Custo sem Direito ao Crédito Acumulado até o Período | Valor Base Cálculo Crédito sobre o Custo, Acumulado até o Período Escrituração | Valor Base Cálculo Crédito sobre o Custo, Acumulado até o Período Escrituração | Valor Base Cálculo Crédito sobre o Custo, Acumulado até o Período Escrituração | Valor Base Cálculo Crédito sobre o Custo, Acumulado até o Período Escrituração |
| 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 |
| PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS |
| CST | Alíquota | Alíquota | Alíquota | Alíquota | Valor Total Crédito Acumulado sobre Custo | Valor Total Crédito Acumulado sobre Custo | Valor Total Crédito Acumulado sobre Custo | Valor Total Crédito Acumulado sobre Custo | Parcela Crédito Descontada até o Período Anterior Escrituração | Parcela Crédito Descontada até o Período Anterior Escrituração | Parcela Crédito Descontada até o Período Anterior Escrituração | Parcela Crédito Descontada até o Período Anterior Escrituração | Parcela Crédito Descontada até o Período Anterior Escrituração | Parcela Crédito Descontada até o Período Anterior Escrituração | Parcela Crédito Descontada até o Período Anterior Escrituração | Parcela Crédito Descontada até o Período Anterior Escrituração | Parcela a Descontar no Período Escrituração | Parcela a Descontar no Período Escrituração | Parcela a Descontar no Período Escrituração | Parcela a Descontar no Período Escrituração | Parcela a Descontar em Períodos Futuros | Parcela a Descontar em Períodos Futuros | Parcela a Descontar em Períodos Futuros | Parcela a Descontar em Períodos Futuros |
| 999 | 99,9999 | 99,9999 | 99,9999 | 99,9999 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 |
| COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS |
| CST | Alíquota | Alíquota | Alíquota | Alíquota | Valor Total Crédito Acumulado sobre Custo | Valor Total Crédito Acumulado sobre Custo | Valor Total Crédito Acumulado sobre Custo | Valor Total Crédito Acumulado sobre Custo | Parcela Crédito Descontada até o Período Anterior Escrituração | Parcela Crédito Descontada até o Período Anterior Escrituração | Parcela Crédito Descontada até o Período Anterior Escrituração | Parcela Crédito Descontada até o Período Anterior Escrituração | Parcela Crédito Descontada até o Período Anterior Escrituração | Parcela Crédito Descontada até o Período Anterior Escrituração | Parcela Crédito Descontada até o Período Anterior Escrituração | Parcela Crédito Descontada até o Período Anterior Escrituração | Parcela a Descontar no Período Escrituração | Parcela a Descontar no Período Escrituração | Parcela a Descontar no Período Escrituração | Parcela a Descontar no Período Escrituração | Parcela a Descontar em Períodos Futuros | Parcela a Descontar em Períodos Futuros | Parcela a Descontar em Períodos Futuros | Parcela a Descontar em Períodos Futuros |
| 999 | 99,9999 | 99,9999 | 99,9999 | 99,9999 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 |
| Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida | Registro F210: Operações da Atividade Imobiliária - Custo Orçado da Unidade Imobiliária Vendida |
| Valor Total Custo Orçado para Conclusão da Unidade Vendida | Valor Total Custo Orçado para Conclusão da Unidade Vendida | Valor Total Custo Orçado para Conclusão da Unidade Vendida | Valor Total Custo Orçado para Conclusão da Unidade Vendida | Valor Total Custo Orçado para Conclusão da Unidade Vendida | Valor Total Custo Orçado para Conclusão da Unidade Vendida | Valores Ref. a Pagtos a PF, Encargos Trabalhistas, Sociais e Previdenc. e à Aquisição de Bens e Serviços não Sujeitos ao Pagto Contribuições | Valores Ref. a Pagtos a PF, Encargos Trabalhistas, Sociais e Previdenc. e à Aquisição de Bens e Serviços não Sujeitos ao Pagto Contribuições | Valores Ref. a Pagtos a PF, Encargos Trabalhistas, Sociais e Previdenc. e à Aquisição de Bens e Serviços não Sujeitos ao Pagto Contribuições | Valores Ref. a Pagtos a PF, Encargos Trabalhistas, Sociais e Previdenc. e à Aquisição de Bens e Serviços não Sujeitos ao Pagto Contribuições | Valores Ref. a Pagtos a PF, Encargos Trabalhistas, Sociais e Previdenc. e à Aquisição de Bens e Serviços não Sujeitos ao Pagto Contribuições | Valores Ref. a Pagtos a PF, Encargos Trabalhistas, Sociais e Previdenc. e à Aquisição de Bens e Serviços não Sujeitos ao Pagto Contribuições | Valor Base Cálculo Crédito sobre o Custo Orçado Ajustado | Valor Base Cálculo Crédito sobre o Custo Orçado Ajustado | Valor Base Cálculo Crédito sobre o Custo Orçado Ajustado | Valor Base Cálculo Crédito sobre o Custo Orçado Ajustado | Valor Base Cálculo Crédito sobre o Custo Orçado Ajustado | Valor Base Cálculo Crédito sobre o Custo Orçado Ajustado | Valor Base Cálculo Crédito sobre o Custo Orçado Ajustado | Valor Base Cálculo Crédito sobre o Custo Orçado Ajustado | Valor Base Cálculo Crédito sobre o Custo Orçado Ajustado | Valor Base Cálculo Crédito sobre o Custo Orçado Ref. ao Mês Escrituração | Valor Base Cálculo Crédito sobre o Custo Orçado Ref. ao Mês Escrituração | Valor Base Cálculo Crédito sobre o Custo Orçado Ref. ao Mês Escrituração | Valor Base Cálculo Crédito sobre o Custo Orçado Ref. ao Mês Escrituração |
| 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 |
| PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | PIS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS | COFINS |
| CST | CST | Alíquota (%) | Alíquota (%) | Alíquota (%) | Alíquota (%) | Alíquota (%) | Valor Crédito sobre o Custo Orçado a ser Utilizado no Período Escrituração | Valor Crédito sobre o Custo Orçado a ser Utilizado no Período Escrituração | Valor Crédito sobre o Custo Orçado a ser Utilizado no Período Escrituração | Valor Crédito sobre o Custo Orçado a ser Utilizado no Período Escrituração | Valor Crédito sobre o Custo Orçado a ser Utilizado no Período Escrituração | Valor Crédito sobre o Custo Orçado a ser Utilizado no Período Escrituração | CST | CST | CST | Alíquota (%) | Alíquota (%) | Alíquota (%) | Valor Crédito sobre o Custo Orçado a ser Utilizado no Período Escrituração | Valor Crédito sobre o Custo Orçado a ser Utilizado no Período Escrituração | Valor Crédito sobre o Custo Orçado a ser Utilizado no Período Escrituração | Valor Crédito sobre o Custo Orçado a ser Utilizado no Período Escrituração | Valor Crédito sobre o Custo Orçado a ser Utilizado no Período Escrituração | Valor Crédito sobre o Custo Orçado a ser Utilizado no Período Escrituração |
| 999 | 999 | 99,9999 | 99,9999 | 99,9999 | 99,9999 | 99,9999 | 9.999.999.999,99 | 9.999.999.999,99 | 9.999.999.999,99 | 9.999.999.999,99 | 9.999.999.999,99 | 9.999.999.999,99 | 999 | 999 | 999 | 99,9999 | 99,9999 | 99,9999 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 |
