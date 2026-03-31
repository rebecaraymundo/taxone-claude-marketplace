# MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R4040_Analitico

> Fonte: MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R4040_Analitico.docx






THOMSON REUTERS

Módulo EFD - REINF
Relatório de Conferência do Evento Família 4000 (R-4040 – Analítico)

Localização: Menu SPED, Módulo: EFD - REINF, item de menu Relatórios à Conferência dos Eventos à Família 4000



DOCUMENTO DE REQUISITO

Sumário

1.	REGRAS DOS CAMPOS	3
2.	REGRAS DE GERAÇÃO DO RELATÓRIO	6
2.1.	Layout do Relatório	14

## REGRAS DOS CAMPOS


Localização da tela: Menu: SPED, Módulo: EFD - REINF, item de menu Relatórios > Conferência dos Eventos > Família 4000
Título da tela: Relatório de Conferência dos Eventos – Família 4000

As regras da tela, estão disponíveis no documento MTZ_REINF_Tela_Relatorio_de_Conferencia_do_Evento_Familia4000.docx, link:

https://trten.sharepoint.com/sites/REQ_MTZ/Mastersaf%20DW%20TaxOne/Documento_Matriz/SPED/EFD-Reinf/Relatorios/Conferencia_dos_Eventos/Familia_4000/MTZ_REINF_Tela_Relatorio_de_Conferencia_do_Evento_Familia4000.docx?web=1












## REGRAS DE GERAÇÃO DO RELATÓRIO


Regra Geral:

[MFS626907] Retirar a opção de “salvar como”.  O relatório passará a ter as opções de salvar em excel ou em PDF

Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.

Origem das informações para geração:

Para geração deste relatório, serão consideradas as informações da seguinte origem:

Evento R-4040 (Cadastro do Estabelecimento, SAFX279, SAFX282).

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
Serão recuperadas as informações do evento R-4040 de acordo com a regra de seleção, todas as informações para a Empresa e Estabelecimento de acordo com o período informado. Relatório demonstrará as informações por Estabelecimento, Natureza de Rendimento, Data do Movimento e Processos.


Ordenação:
Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

- Empresa
- Estabelecimento
- Natureza do Rendimento
- Data do Movimento

Segue regras do preenchimento dos dados no relatório:













### Layout do Relatório



A partir da Versão 2.1.2 do REINF


= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ===============================
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                           							   Pág.: 999999
Data: 99/99/9999 às HH:MM:SS  hs

Relatório de Conferência do Evento R-4040 – Analítico
Período: 99/9999
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ================================
Estabelecimento: XXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
_____________________________________________________________________________________________________________________________
Informação de Identificação do Evento
_____________________________________________________________________________________________________________________________

Tipo Arquivo: XXXXXXXXXXXXXXX 	   		Status: X-XXXXX   			              N. Recibo: XXXXXXXXXXXXXXXXXXX
Tipo Amb. : XXXXXXXXX        				Processo de Emissão: X-XXXXXX                      Versão do Processo de Emissão: XXXXXXXX
Tipo Inscrição Estabelecimento: X-XXXXXXXXXXXX       Número Inscrição Estabelecimento: XXXXX	  Identificador Evento Adicional: XXXXX



| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-79893 | Alessandra Cristina Navatta | Criação de um relatório de conferência do evento R-4040 (analítico). Relatórios à “Conferência dos Eventos àR-4040”. | 11/04/2022 |
| MFS-537211 | Alessandra Cristina Navatta | Adequação do relatório, atendendo o layout 2.1.2 do REINF:  Inclusão dos campos:  Identificador do evento Adicional, no agrupamento Identificação do Evento/Contribuinte  Data Escr. Cont., no agrupamento – Informações de Pagamentos a Beneficiários não Identificados  Inclusão de opção válida no campo Natureza de Rendimento (agrupamento Natureza de Rendimento) | 13/07/2023 |
| MFS-594003 | Alessandra Cristina Navatta | Criada tela única, para a geração dos relatórios de conferência da família 4000.  Excluído o layout da versão 2.1.1 da documentação | 14/02/2024 |
| MFS-627086 | Rosemeire Santos | Inclusão da coluna de status no relatório. Foi necessário incluir essa coluna no relatório, que não está prevista no layout do evento, para evitar duplicidade de dados na conferência dos dados (formato Excel). | 03/04/2024 |
| MFS626907 | Andréa Rocha | Retirada a opção de “salvar como” da geração do relatório. | 20/05/2024 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período | Data | S | S | Formato: MM/AAAA  Default: Habilitado | Local para digitação do período inicial e final de referência da geração do relatório, no formato de DD/MM/AAAA.  Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para a criação do relatório. | MFS-79893 |
| Versão | Texto | S | S | Default: Versão atual | Este campo exibe as versões de layout do Reinf. A partir da versão 2.1.1 | MFS-79893 |
| Tipo do Relatório | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções:  - Analítico - Sintético | MFS-79893 |
| Tipo de Ambiente | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de ambiente entre as opções:  - Produção Restrita - Produção | MFS-798939136 |
| Geração Multiempresa | CheckBox | S | S | Default: não selecionado | Quando o usuário selecionar esta opção, será exibido no campo Estabelecimento, os estabelecimentos de todas as empresas que o usuário tem acesso e que geraram o evento. Se o parâmetro estiver desmarcado, apenas os estabelecimentos da empresa logada que geraram o evento serão demonstrados. | MFS-79893 |
| Estabelecimentos | CheckBox | S | S | Default: não selecionado | - Caso o parâmetro “Geração Multiempresa” estiver desmarcado: Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento, somente da empresa que acessou o módulo. XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento).       - Caso o parâmetro “Geração Multiempresa” estiver marcado: Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento, mas neste caso serão mostradas todas as empresas: XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento)         Obs: No caso da geração multiempresa, as regras da geração do relatório não se modificam. A diferença é apenas na chamada, já que na lista de estabelecimentos para geração do relatório existirão estabelecimentos de empresas distintas.  O usuário deverá escolher obrigatoriamente ao menos um estabelecimento para a geração do relatório.  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento deve ser Selecionado”  Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”. | MFS-79893 |


| Campo/Coluna | Tipo | Tipo | Formato/Default | Regra | Regra | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Empresa | Texto | Texto |  | Razão social da empresa. | Razão social da empresa. | Razão social da empresa. | MFS-79893 |
| Página | Numérico | Numérico |  | Número da página sequencial do relatório | Número da página sequencial do relatório | Número da página sequencial do relatório | MFS-79893 |
| Data | Data | Data | DD/MM/AAAA às HH:MM:SS hs | Data de emissão e hora do relatório | Data de emissão e hora do relatório | Data de emissão e hora do relatório | MFS-79893 |
| Título | Texto | Texto |  | Título do relatório: “Relatório de Conferência do Evento R-4040 - Analítico” | Título do relatório: “Relatório de Conferência do Evento R-4040 - Analítico” | Título do relatório: “Relatório de Conferência do Evento R-4040 - Analítico” | MFS-79893 |
| Período | Data | Data | Formato: MM/AAAA | Deverá ser exibido o período informado em tela. | Deverá ser exibido o período informado em tela. | Deverá ser exibido o período informado em tela. | MFS-79893 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Estabelecimento | Texto | Texto |  | Estabelecimento informado em tela | Estabelecimento informado em tela | Estabelecimento informado em tela | MFS-79893 |
| Informação de Identificação do Evento | Informação de Identificação do Evento | Informação de Identificação do Evento | Informação de Identificação do Evento | Informação de Identificação do Evento | Informação de Identificação do Evento | Informação de Identificação do Evento | Informação de Identificação do Evento |
| Tipo Arquivo | Texto | Texto |  | Campo IND_OPER gravado na tabela REINF_PGER_R4040_OC | Campo IND_OPER gravado na tabela REINF_PGER_R4040_OC | Campo IND_OPER gravado na tabela REINF_PGER_R4040_OC | MFS-79893 |
| Status | Texto | Texto | Código-Descrição | Campo IND_STATUS gravado na tabela REINF_PGER_R4040_OC | Campo IND_STATUS gravado na tabela REINF_PGER_R4040_OC | Campo IND_STATUS gravado na tabela REINF_PGER_R4040_OC | MFS-627086 |
| Nº Recibo | Texto | Texto |  | Campo Num_recibo gravado na tabela REINF_PGER_R4040_OC | Campo Num_recibo gravado na tabela REINF_PGER_R4040_OC | Campo Num_recibo gravado na tabela REINF_PGER_R4040_OC | MFS-79893 |
| Tipo do Amb. | Texto | Texto |  | Tipo do ambiente, gerado no evento R-4040. | Tipo do ambiente, gerado no evento R-4040. | Tipo do ambiente, gerado no evento R-4040. | MFS-79893 |
| Processo de Emissão | Texto | Texto |  | Processo de Emissão, gerado no evento R-4040. | Processo de Emissão, gerado no evento R-4040. | Processo de Emissão, gerado no evento R-4040. | MFS-79893 |
| Versão do Processo de Emissão | Texto | Texto |  | Versão do Processo de Emissão, gerado no evento R-4040. | Versão do Processo de Emissão, gerado no evento R-4040. | Versão do Processo de Emissão, gerado no evento R-4040. | MFS-79893 |
| Tipo de Inscrição Estabelecimento | Alfanumérico | Alfanumérico |  | Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R-4040. | Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R-4040. | Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R-4040. | MFS-79893 |
| Número Inscrição Estabelecimento | Alfanumérico | Alfanumérico |  | Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R-4040. | Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R-4040. | Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R-4040. | MFS-79893 |
| Identificador Evento Adicional | Texto | Texto |  | Identificador de evento adicional por beneficiário, a critério do declarante.  Este campo deve ser apresentado a partir da versão 2.1.2 | Identificador de evento adicional por beneficiário, a critério do declarante.  Este campo deve ser apresentado a partir da versão 2.1.2 | Identificador de evento adicional por beneficiário, a critério do declarante.  Este campo deve ser apresentado a partir da versão 2.1.2 | MFS-537211 |
| Corpo do Relatório – Natureza do Rendimento  Esta parte do relatório demonstra a natureza do rendimento | Corpo do Relatório – Natureza do Rendimento  Esta parte do relatório demonstra a natureza do rendimento | Corpo do Relatório – Natureza do Rendimento  Esta parte do relatório demonstra a natureza do rendimento | Corpo do Relatório – Natureza do Rendimento  Esta parte do relatório demonstra a natureza do rendimento | Corpo do Relatório – Natureza do Rendimento  Esta parte do relatório demonstra a natureza do rendimento | Corpo do Relatório – Natureza do Rendimento  Esta parte do relatório demonstra a natureza do rendimento | Corpo do Relatório – Natureza do Rendimento  Esta parte do relatório demonstra a natureza do rendimento | Corpo do Relatório – Natureza do Rendimento  Esta parte do relatório demonstra a natureza do rendimento |
| Natureza do Rendimento | Natureza do Rendimento | Texto | Código: Descrição | Código: Descrição | Natureza do Rendimento, vinculado ao evento R-4040.  [ALTERAÇÃO MFS-537211] Inclusão de natureza de rendimento 12052: Valores Válidos: 12052; 19001; 19009 | MFS-79893 MFS-537211 | MFS-79893 MFS-537211 |
| Corpo do Relatório – Informações de Pagamentos a Beneficiários não Identificados | Corpo do Relatório – Informações de Pagamentos a Beneficiários não Identificados | Corpo do Relatório – Informações de Pagamentos a Beneficiários não Identificados | Corpo do Relatório – Informações de Pagamentos a Beneficiários não Identificados | Corpo do Relatório – Informações de Pagamentos a Beneficiários não Identificados | Corpo do Relatório – Informações de Pagamentos a Beneficiários não Identificados | Corpo do Relatório – Informações de Pagamentos a Beneficiários não Identificados | Corpo do Relatório – Informações de Pagamentos a Beneficiários não Identificados |
| Data do Fato Gerador | Data do Fato Gerador | Data | DD/MM/AAA | DD/MM/AAA | Data do movimento vinculado ao evento R4040 | MFS-79893 | MFS-79893 |
| Valor Líquido | Valor Líquido | Numérico | 0,00 | 0,00 | Valor Líquido vinculado ao evento R-4040. | MFS-79893 | MFS-79893 |
| Valor Reajustado | Valor Reajustado | Numérico | 0,00 | 0,00 | Valor Reajustado vinculado ao evento R-4040. | MFS-79893 | MFS-79893 |
| Valor do Imposto de Renda Retido na Fonte | Valor do Imposto de Renda Retido na Fonte | Numérico | 0,00 | 0,00 | Valor do Imposto de Renda Retido na Fonte vinculado ao evento R-4040. | MFS-79893 | MFS-79893 |
| Data Escr. Cont. | Data Escr. Cont. | Data | DD/MM/AAAA | DD/MM/AAAA | Data da escrituração contábil.  Apresentar este campo a partir da versão 2.1.2 | MFS-537211 | MFS-537211 |
| Descrição | Descrição | Texto |  |  | Descrição vinculada ao evento R-4040. | MFS-79893 | MFS-79893 |
| Corpo do Relatório – Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais | Corpo do Relatório – Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais | Corpo do Relatório – Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais | Corpo do Relatório – Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais | Corpo do Relatório – Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais | Corpo do Relatório – Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais | Corpo do Relatório – Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais | Corpo do Relatório – Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais |
| Tipo do Processo | Alfanumérico | Alfanumérico |  | Tipo de Processo , correspondente o evento R-4040  Valores Válidos  1-Administrativo 2-Judicial | Tipo de Processo , correspondente o evento R-4040  Valores Válidos  1-Administrativo 2-Judicial | Tipo de Processo , correspondente o evento R-4040  Valores Válidos  1-Administrativo 2-Judicial | MFS-79893 |
| Número do Processo | Alfanumérico | Alfanumérico |  | Número Processo (NUM_PROC) correspondente gerado no campo nrProc do evento R-4040. | Número Processo (NUM_PROC) correspondente gerado no campo nrProc do evento R-4040. | Número Processo (NUM_PROC) correspondente gerado no campo nrProc do evento R-4040. | MFS-79893 |
| Código de Suspenção | Alfaumérico | Alfaumérico |  | Código Suspenção (COD_SUSP) correspondente gerado no campo codSusp do evento R-4040. | Código Suspenção (COD_SUSP) correspondente gerado no campo codSusp do evento R-4040. | Código Suspenção (COD_SUSP) correspondente gerado no campo codSusp do evento R-4040. | MFS-79893 |
| Valor da Base com Exigibilidade Suspensa | Numérico | Numérico | 0,00 | Valor da Base com Exigibilidade Suspensa gerado no evento R-4040 | Valor da Base com Exigibilidade Suspensa gerado no evento R-4040 | Valor da Base com Exigibilidade Suspensa gerado no evento R-4040 | MFS-79893 |
| Valor da Retenção que Deixou de ser Efetuada | Numérico | Numérico | 0,00 | Valor da Retenção que Deixou de ser Efetuada gerado no evento R-4040 | Valor da Retenção que Deixou de ser Efetuada gerado no evento R-4040 | Valor da Retenção que Deixou de ser Efetuada gerado no evento R-4040 | MFS-79893 |
| Valor do Depósito Judicial | Numérico | Numérico | 0,00 | Valor do Depósito Judicial gerado no evento R-4040 | Valor do Depósito Judicial gerado no evento R-4040 | Valor do Depósito Judicial gerado no evento R-4040 | MFS-79893 |


| Natureza do Rendimento | Natureza do Rendimento | Natureza do Rendimento | Natureza do Rendimento | Natureza do Rendimento | Natureza do Rendimento | Natureza do Rendimento | Natureza do Rendimento | Natureza do Rendimento | Natureza do Rendimento |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XXXXX: XXXXXXX | XXXXX: XXXXXXX | XXXXX: XXXXXXX | XXXXX: XXXXXXX | XXXXX: XXXXXXX | XXXXX: XXXXXXX | XXXXX: XXXXXXX | XXXXX: XXXXXXX | XXXXX: XXXXXXX | XXXXX: XXXXXXX |
| Informações de Pagamentos a Beneficiários não Identificados | Informações de Pagamentos a Beneficiários não Identificados | Informações de Pagamentos a Beneficiários não Identificados | Informações de Pagamentos a Beneficiários não Identificados | Informações de Pagamentos a Beneficiários não Identificados | Informações de Pagamentos a Beneficiários não Identificados | Informações de Pagamentos a Beneficiários não Identificados | Informações de Pagamentos a Beneficiários não Identificados | Informações de Pagamentos a Beneficiários não Identificados | Informações de Pagamentos a Beneficiários não Identificados |
| Data do Fato Gerador | Valor Líquido | Valor Líquido | Valor Reajustado | Valor Reajustado | Valor do Imposto de Renda Retido na Fonte | Valor do Imposto de Renda Retido na Fonte | Data Escr. Cont. | Data Escr. Cont. | Descrição |
| DD/MM/AAAA | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | DD/MM/AAAA | DD/MM/AAAA | XXXXXXXXXXX |
| Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais. | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais. | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais. | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais. | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais. | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais. | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais. | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais. | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais. | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais. |
| Tipo do Processo | Número do Processo | Código de Suspensão | Código de Suspensão | Valor da Base com Exigibilidade Suspensa | Valor da Base com Exigibilidade Suspensa | Valor da Retenção que Deixou de ser Efetuada | Valor da Retenção que Deixou de ser Efetuada | Valor do Depósito Judicial | Valor do Depósito Judicial | Valor do Depósito Judicial |
| X- XXXXXXX | xxxxxxxxxxxxxx | xxxxxxxxxxxxxx | xxxxxxxxxxxxxx | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 |
| X- XXXXXXX | xxxxxxxxxxxxxx | xxxxxxxxxxxxxx | xxxxxxxxxxxxxx | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 |
| X- XXXXXXX | xxxxxxxxxxxxxx | xxxxxxxxxxxxxx | xxxxxxxxxxxxxx | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 |
