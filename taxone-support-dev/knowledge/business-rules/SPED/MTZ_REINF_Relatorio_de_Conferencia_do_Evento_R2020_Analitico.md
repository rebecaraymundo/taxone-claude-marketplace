# MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2020_Analitico

> Fonte: MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2020_Analitico.docx






THOMSON REUTERS

Módulo EFD - REINF
Relatório de Conferência do Evento R-2020 - Analítico

Localização: Menu SPED, Módulo: EFD - REINF, item de menu Relatórios  Conferência dos Eventos  R-2020



DOCUMENTO DE REQUISITO


Sumário

1.	REGRAS DOS CAMPOS	3
2.	REGRAS DE GERAÇÃO DO RELATÓRIO	4
2.1.	Layout do Relatório	9

## REGRAS DOS CAMPOS


Localização da tela: Menu: SPED, Módulo: EFD - REINF, item de menu Relatórios  Conferência dos Eventos  R-2020
Título da tela: Relatório de Conferência do Evento R-2020




## REGRAS DE GERAÇÃO DO RELATÓRIO


Regra Geral:
Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.

Origem das informações para geração:
Para geração deste relatório, serão consideradas as informações da seguinte origem:

Evento R-2020 (SAFX04, SAFX07, SAFX09 e Cadastro do Estabelecimento).

Regra de seleção:
A geração do relatório será de acordo com os critérios de filtro informados na tela de geração.

-Empresa = empresa do login
-Período = período informado em tela
-Versão = versão informada em tela
-Tipo = tipo de relatório informado em tela
-Estabelecimento = estabelecimento informado em tela


Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a mensagem “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no relatório.


Regra de processamento:

Para cada estabelecimento selecionado em tela será gerado um relatório.

Serão recuperadas as informações do evento R-2020 de acordo com a regra de seleção, todas as informações para a Empresa e Estabelecimento de acordo com o período informado. Relatório demonstrará as informações por Estabelecimento, Tomador, NFs e Tipo de Serviço. Será recuperado sempre a ultima ocorrência do evento R-2020.

[MFS18432]
Obs.: Ao final do relatório nos campos de valores deve ser realizada uma totalização dos valores gerados no relatório.

Ordenação:
Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

- Empresa
- Estabelecimento
- Nota Fiscal

Segue regras do preenchimento dos dados no relatório:






### Layout do Relatório





| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS15341 | Lara Aline | Alteração do Modulo REINF para criação de um relatório de conferência do evento R-2020. Novo relatório  “Relatório de Conferência do Evento R-2020”. | 07/02/2018 (criação do documento) |
| MFS18226 | Lara Aline | Inclusão do campo Tipo de Ambiente | 04/06/2018 |
| MFS18964 | Lara Aline | Ajuste no campo Número Inscrição Tomador para recuperar a razão social mais atual. | 06/06/2018 |
| MFS18432 | Lara Aline | Inclusão filtro por Tomadores e inclusão de totalização dos valores | 03/07/2018 |
| MFS21968 | Eduardo Cruz | Inclusão dos campos: ID Evento, Data Evento, Nº Recibo, Tipo Arquivo | 20/02/2019 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Tipo | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções:  - Analítico - Sintético | MFS15341 |
| Período | Data | S | S | Formato: MM/AAAA  Default: Habilitado | Local para digitação do período inicial e final de referencia da geração do relatório, no formato de DD/MM/AAAA.  Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para a criação do relatório. | MFS15341 |
| Tipo de Ambiente | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de ambiente entre as opções:  - Produção Restrita - Produção | MFS18226 |
| Tomador do Serviço – Todos | Alfanumérico | N | S | Default: Opção “Todos” marcada | Na abertura da tela a opção “Todos” aparecerá sempre marcada, e o campo “CNPJ/CEI” fica desabilitado;   Caso o usuário desmarque a opção “Todos”, o campo “CNPJ/CEI” será habilitado, e o usuário poderá informar o CNPJ ou CEI do tomador. | MFS18432 |
| Tomador do Serviço – CNPJ/CEI | Alfanumérico | N | S |  | Na abertura da tela este campo aparecerá sempre desabilitado;  Será habilitado apenas quando o usuário desmarcar a opção “Todos”.  Sempre que a opção “Todos” estiver desmarcada, será obrigatório informar o CNPJ ou CEI do tomador antes de solicitar a emissão do relatório. Caso contrário, será exibida uma mensagem (ex: “Informar o CNPJ/CEI do Tomador do Serviço”). | MFS18432 |
| Geração Multiempresa | CheckBox | S | S | Default: não selecionado | Quando o usuário selecionar esta opção, será exibido no campo Estabelecimento, todas as empresas, contendo o código da empresa, código e a razão social de cada estabelecimento. | MFS15341 |
| Estabelecimentos | CheckBox | S | S | Default: não selecionado | Este campo exibe todos os estabelecimentos da empresa que acessou o módulo do EFD-Reinf.   A partir do parâmetro “Geração Multiempresa”, a lista passou a funcionar da seguinte forma:  - Caso o parâmetro “Geração Multiempresa” estiver desmarcado: Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento, somente da empresa que acessou o módulo. XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento).       - Caso o parâmetro “Geração Multiempresa” estiver marcado: Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento, mas neste caso serão mostradas todas as empresas: XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento)         Obs: No caso da geração multiempresa, as regras da geração do relatório não se modificam. A diferença é apenas na chamada, já que na lista de estabelecimentos para geração do relatório existirão estabelecimentos de empresas distintas.  O usuário deverá escolher obrigatoriamente ao menos um estabelecimento para a geração do relatório.  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento deve ser Selecionado”  Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”. | MFS15341 |
|  |  |  |  |  |  |  |


| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Empresa | Texto |  | Razão social da empresa. | MFS15341 |
| Data | Data | DD/MM/AAAA às HH:MM:SS hs | Data de emissão e hora do relatório | MFS15341 |
| Página | Numérico |  | Número da página sequencial do relatório | MFS15341 |
| Título | Texto |  | Título do relatório: “Relatório de Conferência R-2020”. | MFS15341 |
| Período | Data | Formato: MM/AAAA | Deverá ser exibido o período informado em tela. | MFS15341 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Estabelecimento | Texto |  | Estabelecimento informado em tela | MFS15341 |
| ID Evento | Texto |  | Campo ID_EVENTO gravado na tabela REINF_PGER_R2020_OC | MFS21968 |
| Data Evento | Data | Formato: DD/MM/YYYY HH:MM:SS | Campo DAT_OCORRENCIA gravado na tabela REINF_PGER_R2020_OC | MFS21968 |
| Nº Recibo | Texto |  | Campo Num_recibo gravado na tabela REINF_PGER_R2020_OC | MFS21968 |
| Tipo Arquivo | Texto |  | Campo IND_OPER gravado na tabela REINF_PGER_R2020_OC | MFS21968 |
| Tipo Inscrição Estabelecimento Tomador | Alfanumérico |  | Tipo Inscrição Estabelecimento Tomador, gerado no campo tpInscEstabPrest do evento R-2020. | MFS15341 |
| Número  Inscrição Estabelecimento Tomador | Alfanumérico |  | Número Inscrição Estabelecimento Tomador, gerado no campo nrInscEstabPrest do evento R-2020. | MFS15341 |
| Tipo Inscrição Tomador | Alfanumérico |  | Tipo Inscrição Tomador, gerado no campo tplnscTomador do evento R-2020. | MFS15341 |
| Número Inscrição Tomador | Alfanumérico |  | Número Inscrição Tomador, gerado no campo nrInscTomador do evento R-2020  Se Tipo de Inscrição Tomador = 1 - CNPJ: Demostrar o CNPJ + Razão Social do Tomador gerado no evento R-2020 (CPF_CGC da SAFX04).  A razão social será buscada da tabela SAFX04 conforme o CNPJ do Tomador do evento R-2020. Será recuperada a Razão Social de validade mais atual do Tomador. | MFS15341 MFS18964 |
| Corpo do Relatório – Notas Fiscais do Prestador de Serviços | Corpo do Relatório – Notas Fiscais do Prestador de Serviços | Corpo do Relatório – Notas Fiscais do Prestador de Serviços | Corpo do Relatório – Notas Fiscais do Prestador de Serviços | Corpo do Relatório – Notas Fiscais do Prestador de Serviços |
| N° Nota Fiscal | Alfanumérico |  | Número da Nota Fiscal (NUM_DOCFIS) SAFX09, gerado no campo numDocto do evento R-2020. | MFS15341 |
| Série | Alfanumérico |  | Série da Nota Fiscal (SERIE_DOCFIS) SAFX09, gerado no campo serie do evento R-2020. | MFS15341 |
| Data de Emissão | Data | DD/MM/AAAA | Data de Emissão da Nota Fiscal (DATA_EMISSAO) SAFX07, gerado no campo dtEmissaoNF do evento R-2020. | MFS15341 |
| Valor Bruto | Numérico | Default: 0,000 | Valor Bruto (VLR_TOT da SAFX09), gerado no campo vlrBruto do evento R-2020. | MFS15341 |
| Observações | Alfanumérico |  | Observação (OBS_REINF) SAFX07, gerado no campo obs do evento R-2020. | MFS15341 |
| Corpo do Relatório – Informações sobre os tipos de Serviços constantes da Nota Fiscal | Corpo do Relatório – Informações sobre os tipos de Serviços constantes da Nota Fiscal | Corpo do Relatório – Informações sobre os tipos de Serviços constantes da Nota Fiscal | Corpo do Relatório – Informações sobre os tipos de Serviços constantes da Nota Fiscal | Corpo do Relatório – Informações sobre os tipos de Serviços constantes da Nota Fiscal |
| Tipo Serviço | Alfanumérico |  | Tipo de serviço correspondente gerado no campo tpServico do evento R-2020.  Tipo de Serviço vinculado ao código do serviço prestado parametrizado na tela de “Identificador do Tipo de Serviço” Menu: Retenções Previdenciárias>> Parâmetros | MFS15341 |
| Valor Base Retenção | Numérico | Default: 0,000 | Valor Base Retenção (VLR_BASE_INSS) SAFX09, gerado no campo vlrBaseRet do evento R-2020. | MFS15341 |
| Valor Retenção | Numérico | Default: 0,000 | Valor Retenção (VLR _INSS_RETIDO)  SAFX09, gerado no campo vlrRetencao do evento R-2020. | MFS15341 |
| Valor Retenção Subcontratados | Numérico | Default: 0,000 | Valor Retenção Subcontratados (VLR_RET_SERV) SAFX09, gerado no campo vlrRetSub do evento R-2020. | MFS15341 |
| Valor Não Retenção Principal | Numérico | Default: 0,000 | Valor Não Retenção Principal (VLR_N_RET_PRINC) SAFX09, gerado no campo vlrNRetPrinc  do evento R-2020. | MFS15341 |
| Valor Serviços 15 anos | Numérico | Default: 0,000 | Valor Serviços 15 anos (VLR_SERV_15) SAFX09, gerado no campo vlrServicos15 do evento R-2020. | MFS15341 |
| Valor Serviços 20 anos | Numérico | Default: 0,000 | Valor Serviços 20 anos (VLR_SERV_20) SAFX09, gerado no campo vlrServicos20 do evento R-2020. | MFS15341 |
| Valor Serviços 25 anos | Numérico | Default: 0,000 | Valor Serviços 25 anos (VLR_SERV_25) SAFX09, gerado no campo vlrServicos25 do evento R-2020. | MFS15341 |
| Valor Adicional | Numérico | Default: 0,000 | Valor Adicional (VLR_TOT_ADIC) SAFX09, gerado no campo vlrAdicional do evento R-2020. | MFS15341 |
| Valor Não Retenção Adicional | Numérico | Default: 0,000 | Valor Não Retenção Adicional (VLR_N_RET_ADIC) SAFX09, gerado no campo lrNRetAdic do evento R-2020. | MFS15341 |
| Corpo do Relatório – Informações de processos relacionados a não retenção de contribuição previdenciária | Corpo do Relatório – Informações de processos relacionados a não retenção de contribuição previdenciária | Corpo do Relatório – Informações de processos relacionados a não retenção de contribuição previdenciária | Corpo do Relatório – Informações de processos relacionados a não retenção de contribuição previdenciária | Corpo do Relatório – Informações de processos relacionados a não retenção de contribuição previdenciária |
| Tipo Processo Retenção Principal | Alfanumérico |  | Tipo Processo Retenção Principal (IND_TP_PROC_ADJ_PRINC) SAFX09 correspondente gerado no campo tpProcRetPrinc do evento R-2020. | MFS15341 |
| Número Processo Retenção Principal | Alfanumérico |  | Número Processo Retenção Principal (NUM_PROC_ADJ_PRINC) SAFX09 correspondente gerado no campo nrProcRetPrinc do evento R-2020. | MFS15341 |
| Código Suspenção Principal | Alfanumérico |  | Código Suspenção Principal (COD_SUSP_PRINC) SAFX09 correspondente gerado no campo codSuspPrinc do evento R-2020. | MFS15341 |
| Valor Principal | Numérico | Default: 0,000 | Valor Principal (VLR_N_RET_PRINC) SAFX09, gerado no campo valorPrinc do  evento R-2020. | MFS15341 |
| Corpo do Relatório – Informações de processos relacionados a não retenção de contribuição previdenciária adicional | Corpo do Relatório – Informações de processos relacionados a não retenção de contribuição previdenciária adicional | Corpo do Relatório – Informações de processos relacionados a não retenção de contribuição previdenciária adicional | Corpo do Relatório – Informações de processos relacionados a não retenção de contribuição previdenciária adicional | Corpo do Relatório – Informações de processos relacionados a não retenção de contribuição previdenciária adicional |
| Tipo Processo Retenção Adicional | Alfanumérico |  | Tipo Processo Retenção Principal (IND_TP_PROC_ADJ_ADIC) SAFX09 correspondente gerado no campo pProcRetAdic do evento R-2020. | MFS15341 |
| Número Processo Retenção Adicional | Alfanumérico |  | Número Processo Retenção Principal (NUM_PROC_ADJ_ADIC) SAFX09 correspondente gerado no campo nrProcRetAdic do evento R-2020. | MFS15341 |
| Código Suspenção Adicional | Alfanumérico |  | Código Suspenção Principal (COD_SUSP_ADIC) SAFX09 correspondente gerado no campo codSuspAdic do evento R-2020. | MFS15341 |
| Valor Adicional | Numérico | Default: 0,000 | Valor Principal (VLR_N_RET_ADIC) SAFX09, gerado no campo valorAdic do evento R-2020. | MFS15341 |
