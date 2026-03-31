# MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R4010_Sintetico

> Fonte: MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R4010_Sintetico.docx






THOMSON REUTERS

Módulo EFD - REINF
Relatório de Conferência do Evento – Família 4000 – (R-4010 Sintético)

Localização: Menu SPED, Módulo: EFD - REINF, item de menu Relatórios à Conferência dos Eventos à Família 4000



DOCUMENTO DE REQUISITO

Sumário

1.	REGRAS DOS CAMPOS	3
2.	REGRAS DE GERAÇÃO DO RELATÓRIO	6
2.1.	Layout do Relatório	11

## REGRAS DOS CAMPOS



Localização da tela: Menu: SPED, Módulo: EFD - REINF, item de menu Relatórios > Conferência dos Eventos > Família 4000 >
Título da tela: Relatório de Conferência dos Eventos – Família 4000

As regras da tela, estão disponíveis no documento MTZ_REINF_Tela_Relatorio_de_Conferencia_do_Evento_Familia4000.docx, link:

https://trten.sharepoint.com/sites/REQ_MTZ/Mastersaf%20DW%20TaxOne/Documento_Matriz/SPED/EFD-Reinf/Relatorios/Conferencia_dos_Eventos/Familia_4000/MTZ_REINF_Tela_Relatorio_de_Conferencia_do_Evento_Familia4000.docx?web=1

















## REGRAS DE GERAÇÃO DO RELATÓRIO


Regra Geral:

[MFS626907] Retirar a opção de “salvar como”.  O relatório passará a ter as opções de salvar em excel ou em PDF

Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.

Origem das informações para geração:

Para geração deste relatório, serão consideradas as informações da seguinte origem:

Evento R-4010 (Cadastro do Estabelecimento, SAFX04, SAFX53, SAFX536, SAFX531, SAFX532, SAFX534, SAFX535, SAFX275, SAFX276, SAFX277).

Regra de seleção:

A geração do relatório será de acordo com os critérios de filtro informados na tela de geração.

-Empresa = empresa do login
-Período = período informado em tela
- Versão = versão informada em tela
-Tipo = tipo de relatório informado em tela
-Estabelecimento = estabelecimento informado em tela


Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a mensagem “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no relatório.


Regra de processamento:

Para cada estabelecimento selecionado em tela será gerado um relatório.
Serão recuperadas as informações do evento R-4010 de acordo com a regra de seleção, todas as informações para a Empresa e Estabelecimento de acordo com o período informado. Relatório demonstrará as informações por Estabelecimento, Evento, Contribuinte, Informações Complementares do Contribuinte,  Beneficiário, Dependentes, Rendimento pago/creditado, Reembolso do titular do plano de saúde coletivo, Reembolso do dependente do plano de saúde coletivo empresarial.

[ALTERAÇÃO MFS-535745 ] Não considerar as informações de Dependentes, Reembolso do titular do plano de saúde coletivo e  Reembolso do dependente do plano de saúde coletivo empresarial. a partir da versão 2.1.2)


Ordenação:
Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

Empresa
Estabelecimento
Evento
Contribuinte
Informações Complementares do Contribuinte
Beneficiário
Dependentes [ALTERAÇÃO MFS-535745 ] Não considerar essas informações a partir da versão 2.1.2
Rendimento pago/creditado
Reembolso do titular do plano de saúde coletivo [ALTERAÇÃO MFS-535745 ] Não considerar essas informações a partir da versão 2.1.2Reembolso do dependente do plano de saúde coletivo empresarial [ALTERAÇÃO MFS-535745 ] Não considerar essas informações a partir da versão 2.1.2


Agrupamento:
Empresa
Estabelecimento
Evento
Contribuinte
Informações Complementares do Contribuinte
Beneficiário
Identificação do Rendimento
Informações de Rendimento

[ALTERAÇÂO MFS-622783] Para a exibição das informações no relatório:

Apresentar sempre a última ocorrência do evento.

Segue regras do preenchimento dos dados no relatório:




### Layout do Relatório


[ALTERAÇÃO MFS-535745 ] - A partir da Versão 2.1.2 do REINF

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ===============================
XXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                           							   Pág.: 999999
Data: 99/99/9999 às HH:MM:SS  hs

Relatório de Conferência do Evento R-4010 – Sintético
Período: MM/AAAA
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ================================
Estabelecimento: XXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
_____________________________________________________________________________________________________________________________


| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-79885 | Alessandra Cristina Navatta | Criação de um relatório de conferência do evento R-4010 (sintético). Relatórios à “Conferência dos Eventos àR-4010”. | 06/09/2022 |
| MFS- 511669 | Alessandra Cristina Navatta | Inclusão de formato para a exibição dos beneficiários do exterior. | 09/02/2023 |
| MFS-535745 | Alessandra Cristina Navatta | A partir da versão 2.1.2, no relatório Sintético só deverá ser apresentada, as informações do evento R-4010 até a tag infopgto (informações relativas ao pagamento).  Os dados das tags abaixo relacionadas, serão excluídas do relatório sintético:  Informações de Dependentes,  Reembolso do titular do plano de saúde coletivo e   Reembolso do dependente do plano de saúde coletivo empresarial Inclusão dos campos (a partir da  versão 2.1.2):  Identificador do evento Adicional, no agrupamento Identificação do Beneficiário  Data Escr. Cont. e Observ, no agrupamento – Informações Relativas ao Rendimento | 19/05/2023 |
| MFS-542897 | Alessandra Cristina Navatta | Alteração na regra de exibição dos estabelecimentos | 15/06/2023 |
| MFS-578044 | Alessandra Cristina Navatta | Criada tela única, para a geração dos relatórios de conferência da família 4000.  Excluído o layout da versão 2.1.1 da documentação | 06/11/2023 |
| MFS-622783 | Alessandra Cristina Navatta | Inclusão da coluna de status no relatório. Foi necessário incluir essa coluna no relatório, que não está prevista no layout do evento, para evitar duplicidade de dados na conferência dos dados (formato Excel). Além disso, será sempre demonstrado a última ocorrência do evento.  Exclusão do agrupamento ‘Informação de Identificação do Evento / Contribuinte’ e as informações existentes anteriormente neste agrupamento foram transferidas para o agrupamento ‘Identificação do Evento/ Beneficiário’, que anteriormente chama-se ‘Identificação do Beneficiário’. Este ponto foi ajustado, pois a tabela de ocorrência possui as informações por beneficiário, tipo Arquivo, Nº Recibo, Tipo do Amb., Versão do Processo de Emissão, etc... | 21/03/2024 |
| MFS626907 | Andréa Rocha | Retirada a opção de salvar como da geração do relatório. | 20/05/2024 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período | Data | S | S | Formato: MM/AAAA  Default: Habilitado | Local para digitação do período inicial e final de referência da geração do relatório, no formato de DD/MM/AAAA.  Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para a criação do relatório. | MFS-79885 |
| Versão | Texto | S | S | Default: Versão atual | Este campo exibe as versões de layout do Reinf. A partir da versão 2.1.1 | MFS-79885 |
| Tipo do Relatório | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções:  - Analítico - Sintético | MFS-79885 |
| Tipo de Ambiente | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de ambiente entre as opções:  - Produção Restrita - Produção | MFS-79885 |
| Geração Multiempresa | CheckBox | S | S | Default: não selecionado | Quando o usuário selecionar esta opção, será exibido no campo Estabelecimento, os estabelecimentos de todas as empresas que o usuário tem acesso e que geraram o evento. Se o parâmetro estiver desmarcado, apenas os estabelecimentos da empresa logada que geraram o evento serão demonstrados. | MFS-79885 |
| Estabelecimentos | CheckBox | S | S | XXX / XXXXX-XXXXXXXXXXXXXXXXX  (cód. empresa + cód. e razão social do estabelecimento centralizador) ou  XXX / XXXXX-XXXXXXXXXXXXXXXXX  (cód. empresa + cód. e razão social do estabelecimento descentralizado)    Default: não selecionado | - Caso o parâmetro “Geração Multiempresa” estiver desmarcado: Na lista será demonstrado os estabelecimentos que fizeram a geração do evento apenas da empresa que acessou o módulo.      - Caso o parâmetro “Geração Multiempresa” estiver marcado: Na lista será demonstrado o estabelecimento de todas as empresas que geraram o evento e que o usuário tem acesso:          O usuário deverá escolher obrigatoriamente ao menos um estabelecimento para a geração do relatório.  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento deve ser Selecionado”  Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”. | MFS-79885 MFS-542897 |


| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Empresa | Texto | Código - Descrição | Razão social da empresa. | MFS-79885 |
| Página | Numérico |  | Número da página sequencial do relatório | MFS-79885 |
| Data | Data | DD/MM/AAAA às HH:MM:SS hs | Data de emissão e hora do relatório | MFS-79885 |
| Título | Texto |  | Título do relatório: “Relatório de Conferência do Evento R-4010 - Sintético” | MFS-79885 |
| Período | Data | Formato: MM/AAAA | Deverá ser exibido o período informado em tela. | MFS-79885 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Estabelecimento | Texto | Código - Descrição | Estabelecimento informado em tela | MFS-79885 |
| [EXCLUSÃO MFS- MFS-622783] Informação de Identificação do Evento / Contribuinte | [EXCLUSÃO MFS- MFS-622783] Informação de Identificação do Evento / Contribuinte | [EXCLUSÃO MFS- MFS-622783] Informação de Identificação do Evento / Contribuinte | [EXCLUSÃO MFS- MFS-622783] Informação de Identificação do Evento / Contribuinte | [EXCLUSÃO MFS- MFS-622783] Informação de Identificação do Evento / Contribuinte |
| Tipo Arquivo | Texto |  | Campo IND_OPER gravado na tabela REINF_PGER_R4010_OC | MFS-79885 |
| Nº Recibo | Texto |  | Campo Num_recibo gravado na tabela REINF_PGER_R4010_OC | MFS-79885 |
| Tipo do Amb. | Texto |  | Tipo do ambiente, gerado no evento R-4010. | MFS-79885 |
| Processo de Emissão | Texto |  | Processo de Emissão, gerado no evento R-4010. | MFS-79885 |
| Versão do Processo de Emissão | Texto |  | Versão do Processo de Emissão, gerado no evento R-4010. | MFS-79885 |
| Tipo de Inscrição Estabelecimento | Alfanumérico |  | Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R-4010. | MFS-79885 |
| Número Inscrição Estabelecimento | Alfanumérico |  | Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R-4010. | MFS-79885 |
| Corpo do Relatório – Informações Complementares do Contribuinte | Corpo do Relatório – Informações Complementares do Contribuinte | Corpo do Relatório – Informações Complementares do Contribuinte | Corpo do Relatório – Informações Complementares do Contribuinte | Corpo do Relatório – Informações Complementares do Contribuinte |
| Natureza Jurídica | Texto |  | Natureza Jurídica | MFS-79885 |
| Corpo do Relatório – Identificação do Evento / Beneficiário  Esta parte do relatório demonstra os dados do beneficiário | Corpo do Relatório – Identificação do Evento / Beneficiário  Esta parte do relatório demonstra os dados do beneficiário | Corpo do Relatório – Identificação do Evento / Beneficiário  Esta parte do relatório demonstra os dados do beneficiário | Corpo do Relatório – Identificação do Evento / Beneficiário  Esta parte do relatório demonstra os dados do beneficiário | Corpo do Relatório – Identificação do Evento / Beneficiário  Esta parte do relatório demonstra os dados do beneficiário |
| Tipo Arquivo | Texto |  | Campo IND_OPER gravado na tabela REINF_PGER_R4010_OC | MFS-79885 |
| Status | Texto | Código-Descrição | Campo IND_STATUS gravado na tabela REINF_PGER_R4010_OC | MFS-622783 |
| Nº Recibo | Texto |  | Campo Num_recibo gravado na tabela REINF_PGER_R4010_OC | MFS-79885 |
| Tipo do Amb. | Texto |  | Tipo do ambiente, gerado no evento R-4010. | MFS-79885 |
| Processo de Emissão | Texto |  | Processo de Emissão, gerado no evento R-4010. | MFS-79885 |
| Versão do Processo de Emissão | Texto |  | Versão do Processo de Emissão, gerado no evento R-4010. | MFS-79885 |
| Tipo de Inscrição Estabelecimento | Alfanumérico |  | Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R-4010. | MFS-79885 |
| Número Inscrição Estabelecimento | Alfanumérico |  | Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R-4010. | MFS-79885 |
| CPF/Ident. Benef. Exterior | Texto | XXX.XXX.XXX-XX ou Grp/Ind/Cod do Benef. | CPF do Beneficiário.  [ALTERAÇÃO MFS-511669]  Caso beneficiário seja do exterior, apresentar o código do beneficiário, no formato: Grp/Ind/Cod do Benef. | MFS-79885 MFS- 511669 |
| Nome | Texto |  | Nome do Beneficiário. | MFS-79885 |
| Identificador Evento Adicional | Texto |  | Identificador de evento adicional por beneficiário, a critério do declarante.  Este campo deve ser apresentado a partir da versão 2.1.2 | MFS-535745 |
| Corpo do Relatório – Identificação dos Dependentes   [ALTERAÇÃO MFS-535745 ] - Não apresentar essas informações a partir da versão 2.1.2 | Corpo do Relatório – Identificação dos Dependentes   [ALTERAÇÃO MFS-535745 ] - Não apresentar essas informações a partir da versão 2.1.2 | Corpo do Relatório – Identificação dos Dependentes   [ALTERAÇÃO MFS-535745 ] - Não apresentar essas informações a partir da versão 2.1.2 | Corpo do Relatório – Identificação dos Dependentes   [ALTERAÇÃO MFS-535745 ] - Não apresentar essas informações a partir da versão 2.1.2 | Corpo do Relatório – Identificação dos Dependentes   [ALTERAÇÃO MFS-535745 ] - Não apresentar essas informações a partir da versão 2.1.2 |
| CPF | Texto | XXX.XXX.XXX-XX | Neste campo deve ser considerado o somatório do valor bruto do rendimento R-4010, independente da data do recebimento e sim do período de apuração. | MFS-79885 |
| Relação de Dependência | Texto | Código - Descrição | Informar a Relação de Dependência | MFS-79885 |
| Descrição | Texto | Descrição | Descrição da Dependência, quando o tipo de relação de dependência for igual a ‘99 – Outros’ | MFS-79885 |
| Corpo do Relatório – Identificação do Rendimento | Corpo do Relatório – Identificação do Rendimento | Corpo do Relatório – Identificação do Rendimento | Corpo do Relatório – Identificação do Rendimento | Corpo do Relatório – Identificação do Rendimento |
| Natureza do Rendimento | Texto |  | Natureza de Rendimento | MFS-79885 |
| Observação | Texto | Descrição | Observação | MFS-79885 |
| Corpo do Relatório – Informações Relativas ao Rendimento | Corpo do Relatório – Informações Relativas ao Rendimento | Corpo do Relatório – Informações Relativas ao Rendimento | Corpo do Relatório – Informações Relativas ao Rendimento | Corpo do Relatório – Informações Relativas ao Rendimento |
| Fato Gerador | Texto | DD/MM/AAAA | Data do Fato Gerador | MFS-79885 |
| Comp. | Texto | DD/AAAA | Mês e Ano da Competência | MFS-79885 |
| 13º | Texto | Código | Indicador de 13º  Lista de Valor Válido: S | MFS-79885 |
| Rend. Bruto | Texto | 0,00 | Valor do rendimento bruto | MFS-79885 |
| Rend. Tributável | Texto | 0,00 | Valor tributável | MFS-79885 |
| Valor IR | Texto | 0,00 | Valor do IR | MFS-79885 |
| RRA | Texto | Código | Indicador de Rendimento Recebido Acumuladamente.   Lista de Valor Válido: S | MFS-79885 |
| FCI_SCP | Texto | Código - Descrição | Indicador de FCI e SCP  Lista de Valores Válidos: 1-FCI;  2-SCP | MFS-79885 |
| Núm. Insc. FCI_SCP | Texto | XX.XXX.XXX/XXXX-XX | Número da Inscrição de FCI/SCP | MFS-79885 |
| % SCP | Texto | 999 | Percentual de SCP | MFS-79885 |
| IndJud | Texto | Código - Descrição | Informar o Indicativo exclusivo de rendimento de natureza diversa de RRA e que seja oriundo de decisão judicial  Lista de Valores Válidos: S; N | MFS-79885 |
| País Resid. Exterior | Texto | 999 | Informar o código do país de destino da remessa do pagamento a residente ou domiciliado no exterior. | MFS-79885 |
| Data Escr. Cont. | Texto | DD/MM/AAAA | Informar a data da escrituração contábil.  Este campo deve ser apresentado a partir da versão 2.1.2 | MFS-535745 |
| Observ. | Texto |  | Observações  Este campo deve ser apresentado a partir da versão 2.1.2 | MFS-535745 |
| Corpo do Relatório – Informação de Reembolso do Titular do Plano de Saúde Coletivo Empresarial   [ALTERAÇÃO MFS-535745 ] - Não apresentar essas informações a partir da versão 2.1.2 | Corpo do Relatório – Informação de Reembolso do Titular do Plano de Saúde Coletivo Empresarial   [ALTERAÇÃO MFS-535745 ] - Não apresentar essas informações a partir da versão 2.1.2 | Corpo do Relatório – Informação de Reembolso do Titular do Plano de Saúde Coletivo Empresarial   [ALTERAÇÃO MFS-535745 ] - Não apresentar essas informações a partir da versão 2.1.2 | Corpo do Relatório – Informação de Reembolso do Titular do Plano de Saúde Coletivo Empresarial   [ALTERAÇÃO MFS-535745 ] - Não apresentar essas informações a partir da versão 2.1.2 | Corpo do Relatório – Informação de Reembolso do Titular do Plano de Saúde Coletivo Empresarial   [ALTERAÇÃO MFS-535745 ] - Não apresentar essas informações a partir da versão 2.1.2 |
| Tipo Inscrição | Texto | Código - Descrição | Tipo de Inscrição  Lista de Valores Válidos 1 - Pessoa jurídica;  2 - Pessoa física. | MFS-79885 |
| Núm. Inscrição | Texto | XX.XXX.XXX/XXXX-XX ou XXX.XXX.XXX-XX | Número de Inscrição | MFS-79885 |
| Valor Reembolso Per. Apur. | Texto | 0,00 | Valor do Reembolso relativo ao período da apuração | MFS-79885 |
| Valor Reembolso Anos Anteriores | Texto | 0,00 | Valor do Reembolso relativo aos anos anteriores | MFS-79885 |
| Corpo do Relatório – Informações de Dependente do Plano de Saúde Coletivo Empresarial [ALTERAÇÃO MFS-535745 ] - Não apresentar essas informações a partir da versão 2.1.2 | Corpo do Relatório – Informações de Dependente do Plano de Saúde Coletivo Empresarial [ALTERAÇÃO MFS-535745 ] - Não apresentar essas informações a partir da versão 2.1.2 | Corpo do Relatório – Informações de Dependente do Plano de Saúde Coletivo Empresarial [ALTERAÇÃO MFS-535745 ] - Não apresentar essas informações a partir da versão 2.1.2 | Corpo do Relatório – Informações de Dependente do Plano de Saúde Coletivo Empresarial [ALTERAÇÃO MFS-535745 ] - Não apresentar essas informações a partir da versão 2.1.2 | Corpo do Relatório – Informações de Dependente do Plano de Saúde Coletivo Empresarial [ALTERAÇÃO MFS-535745 ] - Não apresentar essas informações a partir da versão 2.1.2 |
| CPF | Texto | XXX.XXX.XXX-XX | CPF do dependente | MFS-79885 |
| Valor Saúde | Texto | 0,00 | Valor relativo a dedução do rendimento tributável correspondente a pagamento a plano de saúde do dependente | MFS-79885 |


| Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX |
| Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário |
| Tipo Arquivo: XXXXXXXXXXXXXXX | Tipo Arquivo: XXXXXXXXXXXXXXX | Status: X-XXXXXXXXXXXX | Status: X-XXXXXXXXXXXX | Status: X-XXXXXXXXXXXX | Status: X-XXXXXXXXXXXX | Status: X-XXXXXXXXXXXX | Status: X-XXXXXXXXXXXX | Status: X-XXXXXXXXXXXX | Status: X-XXXXXXXXXXXX | N. Recibo: XXXXXXXXXXXXXXXXXXX | N. Recibo: XXXXXXXXXXXXXXXXXXX | N. Recibo: XXXXXXXXXXXXXXXXXXX | N. Recibo: XXXXXXXXXXXXXXXXXXX | N. Recibo: XXXXXXXXXXXXXXXXXXX | N. Recibo: XXXXXXXXXXXXXXXXXXX | N. Recibo: XXXXXXXXXXXXXXXXXXX |
| Tipo do Amb. : XXXXXXXXX | Tipo do Amb. : XXXXXXXXX | Processo de Emissão: X-XXXXXX | Processo de Emissão: X-XXXXXX | Processo de Emissão: X-XXXXXX | Processo de Emissão: X-XXXXXX | Processo de Emissão: X-XXXXXX | Processo de Emissão: X-XXXXXX | Processo de Emissão: X-XXXXXX | Processo de Emissão: X-XXXXXX | Versão do Processo de Emissão: XXXXXXXX | Versão do Processo de Emissão: XXXXXXXX | Versão do Processo de Emissão: XXXXXXXX | Versão do Processo de Emissão: XXXXXXXX | Versão do Processo de Emissão: XXXXXXXX | Versão do Processo de Emissão: XXXXXXXX | Versão do Processo de Emissão: XXXXXXXX |
| Tipo de Inscrição Estabelecimento: X-XXXXXXXXXXXX | Tipo de Inscrição Estabelecimento: X-XXXXXXXXXXXX | Tipo de Inscrição Estabelecimento: X-XXXXXXXXXXXX | Tipo de Inscrição Estabelecimento: X-XXXXXXXXXXXX | Tipo de Inscrição Estabelecimento: X-XXXXXXXXXXXX | Tipo de Inscrição Estabelecimento: X-XXXXXXXXXXXX | Tipo de Inscrição Estabelecimento: X-XXXXXXXXXXXX | Número Inscrição Estabelecimento: XXXXX | Número Inscrição Estabelecimento: XXXXX | Número Inscrição Estabelecimento: XXXXX | Número Inscrição Estabelecimento: XXXXX | Número Inscrição Estabelecimento: XXXXX | Número Inscrição Estabelecimento: XXXXX | Número Inscrição Estabelecimento: XXXXX | Número Inscrição Estabelecimento: XXXXX | Número Inscrição Estabelecimento: XXXXX | Número Inscrição Estabelecimento: XXXXX |
| CPF/ Ident. Benef. Exterior: XXX.XXX.XXX-XX ou  Grp/Ind/Cod do Benef. | CPF/ Ident. Benef. Exterior: XXX.XXX.XXX-XX ou  Grp/Ind/Cod do Benef. | Nome: XXXXXXXXX | Nome: XXXXXXXXX | Nome: XXXXXXXXX | Nome: XXXXXXXXX | Nome: XXXXXXXXX | Nome: XXXXXXXXX | Nome: XXXXXXXXX | Nome: XXXXXXXXX | Identificador Evento Adicional: XXXXXXXX | Identificador Evento Adicional: XXXXXXXX | Identificador Evento Adicional: XXXXXXXX | Identificador Evento Adicional: XXXXXXXX | Identificador Evento Adicional: XXXXXXXX | Identificador Evento Adicional: XXXXXXXX | Identificador Evento Adicional: XXXXXXXX |
| Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento |
| Natureza do Rendimento: XXXXXXX | Natureza do Rendimento: XXXXXXX | Natureza do Rendimento: XXXXXXX | Natureza do Rendimento: XXXXXXX | Natureza do Rendimento: XXXXXXX | Natureza do Rendimento: XXXXXXX | Natureza do Rendimento: XXXXXXX | Natureza do Rendimento: XXXXXXX | Natureza do Rendimento: XXXXXXX | Observação: Descrição | Observação: Descrição | Observação: Descrição | Observação: Descrição | Observação: Descrição | Observação: Descrição | Observação: Descrição | Observação: Descrição |
| Informações Relativas ao Rendimento | Informações Relativas ao Rendimento | Informações Relativas ao Rendimento | Informações Relativas ao Rendimento | Informações Relativas ao Rendimento | Informações Relativas ao Rendimento | Informações Relativas ao Rendimento | Informações Relativas ao Rendimento | Informações Relativas ao Rendimento | Informações Relativas ao Rendimento | Informações Relativas ao Rendimento | Informações Relativas ao Rendimento | Informações Relativas ao Rendimento | Informações Relativas ao Rendimento | Informações Relativas ao Rendimento | Informações Relativas ao Rendimento | Informações Relativas ao Rendimento |
| Fato Gerador | Comp. | 13º | Rend. Bruto | Rend. Tributável | Valor IR | RRA | RRA | FCI_SPC | FCI_SPC | FCI_SPC | Núm. Insc. FCI_SCP | %SCP | IndJud | País Resid. Exterior | Data Escr. Cont. | Observ. |
| DD/MM/AAAA | DD/AAAA | Cód. | 0,00 | 0,00 | 0,00 | Cód. | Cód. | Cód.  – Descrição | Cód.  – Descrição | Cód.  – Descrição | XX.XXX.XXX/XXXX-XX | 999 | Cód. | 999 | DD/MM/AAAA | XXXX |
