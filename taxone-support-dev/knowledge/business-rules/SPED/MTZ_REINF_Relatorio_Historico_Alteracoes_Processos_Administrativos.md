# MTZ_REINF_Relatorio_Historico_Alteracoes_Processos_Administrativos

> Fonte: MTZ_REINF_Relatorio_Historico_Alteracoes_Processos_Administrativos.docx






THOMSON REUTERS

Módulo EFD - REINF
Relatório de Histórico das Alterações – Processos Administrativos

Localização: Menu SPED, Módulo: EFD - REINF, item de menu Parâmetros  Dados Iniciais  Relatório de Histórico das Alterações  Processos Administrativos



DOCUMENTO DE REQUISITO


Sumário

1.	REGRAS DOS CAMPOS	3
2.	REGRAS DE GERAÇÃO DO RELATÓRIO	4
2.1.	Layout do Relatório	9

## REGRAS DOS CAMPOS


Localização da tela: Menu: SPED, Módulo: EFD - REINF, item de menu Parâmetros Dados Iniciais  Relatório de Histórico das Alterações  Processos Administrativos
Título da tela: Relatório de Histórico das Alterações dos Processos Administrativos





















## REGRAS DE GERAÇÃO DO RELATÓRIO


Regra Geral:
Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.

Origem das informações para geração:
Para geração deste relatório, serão consideradas as informações da seguinte origem:

SAFX2058 - Cadastro de Processos Administrativos / Judiciais
SAFX2059 - Informação de Suspensão de Exigibilidade de Tributos


Regra de seleção:
A geração do relatório será de acordo com os critérios de filtro informados na tela de geração.

-Grupo = Grupo de Processos Administrativos informado em tela
-Tipo de Processo = Tipo de Processo informado em tela
-Número de Processo = Número de Processo informado em tela


Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a mensagem “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no relatório.


Regra de processamento:

Para cada grupo selecionado em tela será gerado um relatório.

Serão recuperadas as informações dos Processos Administrativos / Judiciais de acordo com a regra de seleção, todas as informações para o Grupo, Tipo de Processo e Número de Processo caso informado, se não serão recuperadas todas as informações para o Grupo de Tipo do Processo encontrado.


Ordenação:
Para o relatório de cada Grupo selecionado em tela, os dados serão ordenados da seguinte forma:

- Grupo
- Tipo de Processo
- Número de Processo

Segue regras do preenchimento dos dados no relatório:





### Layout do Relatório




| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS10356 | Lara Aline | Alteração do Modulo REINF para criação de um relatório de histórico de alterações dos Dados Iniciais. Novo relatório  “Relatório de Histórico das Alterações - Processos Administrativos”. | 21/11/2017 (criação do documento) |
|  |  |  |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Grupo | Alfanumérico | S | S | Default: não selecionado | Lista dos grupos do estabelecimento | MFS10356 |
| Tipo do Processo | Alfanumérico | S | S | Default: Todos | Tipo do Processo a ser considerado na geração, caso informado. | MFS10356 |
| Número do Processo | Alfanumérico | N | S | Default: não informado | Número do Processo a ser considerado na geração, caso informado. | MFS10356 |


| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Empresa | Texto |  | Razão social da empresa. | MFS10356 |
| Página | Numérico |  | Número da página sequencial do relatório. | MFS10356 |
| Data | Data | DD/MM/AAAA às HH:MM:SS hs | Data de emissão e hora do relatório | MFS10356 |
| Título | Texto |  | Título do relatório: “Relatório de Histórico das Alterações dos Processos Administrativos” | MFS12175 |
| Corpo do Relatório – Informações do Processo | Corpo do Relatório – Informações do Processo | Corpo do Relatório – Informações do Processo | Corpo do Relatório – Informações do Processo | Corpo do Relatório – Informações do Processo |
| Grupo | Alfanumérico |  | Grupo do estabelecimento (grupo_estab) da tabela GRUPO_ESTAB. | MFS10356 |
| Tipo do Processo | Alfanumérico |  | Tipo do Processo (IND_TP_PROC_ADJ) do cadastro Processo Administrativo/Judiciais. | MFS10356 |
| Número do Processo | Alfanumérico |  | Tipo do Processo (NUM_PROC_ADJ) do cadastro Processo Administrativo/Judiciais. | MFS10356 |
| Validade Inicial | Alfanumérico |  | Data Início/Inclusão/Alteração da Validade (VALID_PROC_ADJ_INI) do cadastro Processo Administrativo/Judiciais. | MFS10356 |
| Validade Final | Alfanumérico |  | Data de Término da Validade (VALID_PROC_ADJ_FIM) do cadastro Processo Administrativo/Judiciais. | MFS10356 |
| UF Seção Jurídica | Alfanumérico |  | UF (COD_ESTADO) do cadastro Processo Administrativo/Judiciais. | MFS10356 |
| Município | Alfanumérico |  | Município (COD_MUNICIPIO) do cadastro Processo Administrativo/Judiciais. | MFS10356 |
| Identificação da Vara | Alfanumérico |  | Código da Vara (COD_VARA) do cadastro Processo Administrativo/Judiciais. | MFS10356 |
| Autoria da Ação Judicial | Alfanumérico |  | Indicador de Autoria (IND_AUTORIA) do cadastro Processo Administrativo/Judiciais. | MFS10356 |
| Nº Processo | Alfanumérico |  | Número do Processo de Importação (NUM_PROCESSO) do cadastro Processo Administrativo/Judiciais. | MFS10356 |
| Corpo do Relatório – Informação de Suspensão de Exigibilidade de Tributos | Corpo do Relatório – Informação de Suspensão de Exigibilidade de Tributos | Corpo do Relatório – Informação de Suspensão de Exigibilidade de Tributos | Corpo do Relatório – Informação de Suspensão de Exigibilidade de Tributos | Corpo do Relatório – Informação de Suspensão de Exigibilidade de Tributos |
| Código de Suspensão | Alfanumérico |  | Código do Indicativo da Suspensão de Exigibilidade de Tributos (COD_SUSP) do cadastro Processo Administrativo/Judiciais, aba Informação de Suspensão de Exigibilidade de Tributos. | MFS10356 |
| Indicador Suspensão | Alfanumérico |  | Indicador da Suspensão de Exigibilidade de Tributos (IND_SUSP) do cadastro Processo Administrativo/Judiciais, aba Informação de Suspensão de Exigibilidade de Tributos. | MFS10356 |
| Data Decisão | Alfanumérico |  | Data da Decisão (DAT_DECISAO) do cadastro Processo Administrativo/Judiciais, aba Informação de Suspensão de Exigibilidade de Tributos. | MFS10356 |
| Indicador de Depósito | Alfanumérico |  | Indicador de Depósito (IND_DEPOSITO) do cadastro Processo Administrativo/Judiciais, aba Informação de Suspensão de Exigibilidade de Tributos. | MFS10356 |
| Nº Processo | Alfanumérico |  | Número do Processo de Importação (NUM_PROCESSO) do cadastro Processo Administrativo/Judiciais, aba Informação de Suspensão de Exigibilidade de Tributos. | MFS10356 |
