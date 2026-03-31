# MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2060_Analitico

> Fonte: MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2060_Analitico.docx






THOMSON REUTERS

Módulo EFD - REINF
Relatório de Conferência do Evento R-2060 - Analítico

Localização: Menu SPED, Módulo: EFD - REINF, item de menu Relatórios  Conferência dos Eventos  R-2060



DOCUMENTO DE REQUISITO


Sumário

1.	REGRAS DOS CAMPOS	3
2.	REGRAS DE GERAÇÃO DO RELATÓRIO	4
2.1.	Layout do Relatório	9

## REGRAS DOS CAMPOS


Localização da tela: Menu: SPED, Módulo: EFD - REINF, item de menu Relatórios  Conferência dos Eventos  R-2060
Título da tela: Relatório de Conferência do Evento R-2060




























## REGRAS DE GERAÇÃO DO RELATÓRIO


Regra Geral:
Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.

Origem das informações para geração:
Para geração deste relatório, serão consideradas as informações da seguinte origem:

Evento R-2060 (SAFX185 e SAFX2113).

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

Serão recuperadas as informações do evento R-2060 de acordo com a regra de seleção, todas as informações para a Empresa e Estabelecimento de acordo com o período informado. Relatório demonstrará as informações por Estabelecimento, Código de Atividade, NFs e Ajustes. Será recuperado sempre a ultima ocorrência do evento R-2060 por tipo de número de inscrição do contribuinte.


Ordenação:
Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

- Empresa
- Estabelecimento
- Nota Fiscal

Segue regras do preenchimento dos dados no relatório:



























### Layout do Relatório






| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS15342 | Lara Aline | Alteração do Modulo REINF para criação de um relatório de conferência do evento R-2060. Novo relatório  “Relatório de Conferência do Evento R-2010”. | 29/01/2018 (criação do documento) |
| MFS18226 | Lara Aline | Inclusão do campo Tipo de Ambiente | 04/06/2018 |
| MFS21968 | Eduardo Cruz | Inclusão dos campos: ID Evento, Data Evento, Nº Recibo, Tipo Arquivo | 20/02/2019 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Tipo | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções:  - Analítico - Sintético | MFS15342 |
| Período | Data | S | S | Formato: MM/AAAA  Default: Habilitado | Local para digitação do período inicial e final de referencia da geração do relatório, no formato de DD/MM/AAAA.  Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para a criação do relatório. | MFS15342 |
| Tipo de Ambiente | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de ambiente entre as opções:  - Produção Restrita - Produção | MFS18226 |
| Geração Multiempresa | CheckBox | S | S | Default: não selecionado | Quando o usuário selecionar esta opção, será exibido no campo Estabelecimento, todas as empresas, contendo o código da empresa, código e a razão social de cada estabelecimento. | MFS15342 |
| Estabelecimentos | CheckBox | S | S | Default: não selecionado | Este campo exibe todos os estabelecimentos da empresa que acessou o módulo do EFD-Reinf.   A partir do parâmetro “Geração Multiempresa”, a lista passou a funcionar da seguinte forma:  - Caso o parâmetro “Geração Multiempresa” estiver desmarcado: Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento, somente da empresa que acessou o módulo. XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento).       - Caso o parâmetro “Geração Multiempresa” estiver marcado: Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento, mas neste caso serão mostradas todas as empresas: XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento)         Obs: No caso da geração multiempresa, as regras da geração do relatório não se modificam. A diferença é apenas na chamada, já que na lista de estabelecimentos para geração do relatório existirão estabelecimentos de empresas distintas.  O usuário deverá escolher obrigatoriamente ao menos um estabelecimento para a geração do relatório.  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento deve ser Selecionado”  Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”. | MFS15342 |


| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Empresa | Texto |  | Razão social da empresa. | MFS15342 |
| Data | Data | DD/MM/AAAA às HH:MM:SS hs | Data de emissão e hora do relatório | MFS15342 |
| Página | Numérico |  | Número da página sequencial do relatório | MFS15342 |
| Título | Texto |  | Título do relatório: “Relatório de Histórico das Alterações - Dados Iniciais” | MFS15342 |
| Período | Data | Formato: MM/AAAA | Deverá ser exibido o período informado em tela. | MFS15342 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Estabelecimento | Texto |  | Estabelecimento informado em tela | MFS15342 |
| ID Evento | Texto |  | Campo ID_EVENTO gravado na tabela REINF_PGER_R2060_OC | MFS21968 |
| Data Evento | Data | Formato: DD/MM/YYYY HH:MM:SS | Campo DAT_OCORRENCIA gravado na tabela REINF_PGER_R2060_OC | MFS21968 |
| Nº Recibo | Texto |  | Campo Num_recibo gravado na tabela REINF_PGER_R2060_OC | MFS21968 |
| Tipo Arquivo | Texto |  | Campo IND_OPER gravado na tabela REINF_PGER_R2060_OC | MFS21968 |
| Tipo Inscrição Estabelecimento | Alfanumérico |  | Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R-2060. | MFS15342 |
| Número Inscrição Estabelecimento | Alfanumérico |  | Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R-2060. | MFS15342 |
| Código Atividade Econômica | Alfanumérico |  | Código Atividade Econômica (COD_ATIV_CONT_PREV da SAFX185), gerado no campo codAtivEcon do evento R-2060. | MFS15342 |
| Corpo do Relatório – Preenchido caso a pessoa jurídica tenha de proceder a ajustes da contribuição apurada no período | Corpo do Relatório – Preenchido caso a pessoa jurídica tenha de proceder a ajustes da contribuição apurada no período | Corpo do Relatório – Preenchido caso a pessoa jurídica tenha de proceder a ajustes da contribuição apurada no período | Corpo do Relatório – Preenchido caso a pessoa jurídica tenha de proceder a ajustes da contribuição apurada no período | Corpo do Relatório – Preenchido caso a pessoa jurídica tenha de proceder a ajustes da contribuição apurada no período |
| Tipo de Ajuste | Alfanumérico |  | Tipo de Ajuste (Tipo de Ajuste) SAFX252 correspondente gerado no campo tpAjuste do evento R-2060. | MFS15342 |
| Código de Ajuste | Alfanumérico |  | Código de Ajuste (Código de Ajuste) SAFX252 correspondente gerado no campo codAjuste do evento R-2060. | MFS15342 |
| Valor Ajuste | Numérico | Default: 0,000 | Valor Ajuste (Valor do Ajuste) SAFX252 gerado no campo vlrAjuste do evento R-2060. | MFS15342 |
| Descrição Ajuste | Alfanumérico |  | Descrição Ajuste (Descrição do Ajuste) SAFX252, gerado no campo descAjuste do evento R-2060. | MFS15342 |
| Data Ajuste | Data | DD/MM/AAAA | Data Ajuste (Data do Ajuste) SAFX252, gerado no campo dtAjuste do evento R-2060. | MFS15342 |
| Corpo do Relatório – Informações de processos relacionados a Suspensão da CPRB | Corpo do Relatório – Informações de processos relacionados a Suspensão da CPRB | Corpo do Relatório – Informações de processos relacionados a Suspensão da CPRB | Corpo do Relatório – Informações de processos relacionados a Suspensão da CPRB | Corpo do Relatório – Informações de processos relacionados a Suspensão da CPRB |
| Tipo de Processo | Alfanumérico |  | Tipo de Processo (IND_TIP_PROC) SAFX2113 correspondente gerado no campo tpProc do evento R-2060. | MFS15342 |
| Número Processo | Alfanumérico |  | Número Processo (NUM_PROC) SAFX2113 correspondente gerado no campo nrProc do evento R-2060. | MFS15342 |
| Código Suspenção | Alfanumérico |  | Código Suspenção (COD_SUSP) SAFX2113 correspondente gerado no campo codSusp do evento R-2060. | MFS15342 |
| Valor CPRB Exigibilidade Suspensa | Numérico | Default: 0,000 | Valor CPRB Exigibilidade Suspensa (VLR_PREV_EXIG_SUSP) SAFX2113, gerado no campo vlrCPRBSusp do  evento R-2060. | MFS15342 |
| Corpo do Relatório – Detalhamento de Nota Fiscal por Atividade | Corpo do Relatório – Detalhamento de Nota Fiscal por Atividade | Corpo do Relatório – Detalhamento de Nota Fiscal por Atividade | Corpo do Relatório – Detalhamento de Nota Fiscal por Atividade | Corpo do Relatório – Detalhamento de Nota Fiscal por Atividade |
| N° Nota Fiscal | Alfanumérico |  | N° Nota Fiscal (NUM_DOCFIS) SAFX07/SAFX09 gerado no campo numDocto vinculado ao evento R-2060. | MFS15342 |
| Série | Alfanumérico |  | Série da Nota Fiscal (SERIE_DOCFIS) SAFX07/SAFX09, gerado no campo serie vinculado ao evento R-2060. | MFS15342 |
| Data de Emissão | Data | DD/MM/AAAA | Data de Emissão da Nota Fiscal (DATA_EMISSAO) SAFX07/SAFX09 vinculado ao evento R-2060. | MFS15342 |
| Valor Bruto | Numérico | Default: 0,000 | Valor Bruto (VLR_BRUTO da SAFX07), gerado no campo vlrBruto vinculado ao evento R-2060. | MFS15342 |
