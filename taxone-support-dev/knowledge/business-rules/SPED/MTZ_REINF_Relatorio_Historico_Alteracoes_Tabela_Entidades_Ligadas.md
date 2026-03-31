# MTZ_REINF_Relatorio_Historico_Alteracoes_Tabela_Entidades_Ligadas

> Fonte: MTZ_REINF_Relatorio_Historico_Alteracoes_Tabela_Entidades_Ligadas.docx






THOMSON REUTERS

Módulo EFD - REINF
Relatório de Histórico das Alterações –Entidades Ligadas

Localização: Menu SPED, Módulo: EFD - REINF, item de menu Relatórios  Relatório de Histórico das Alterações  Entidades Ligadas



DOCUMENTO DE REQUISITO


Sumário

1.	REGRAS DOS CAMPOS	3
2.	REGRAS DE GERAÇÃO DO RELATÓRIO	3
2.1.	Layout do Relatório	6

## REGRAS DOS CAMPOS


Localização da tela: Menu: SPED, Módulo: EFD - REINF, item de menu Relatórios / Relatório de Histórico das Alterações / Entidades Ligadas
Título da tela: Relatório de Histórico das Alterações de Tabela de Entidades Ligadas


## REGRAS DE GERAÇÃO DO RELATÓRIO


Regra Geral:
Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.

Origem das informações para geração:
Para geração deste relatório, serão consideradas as informações da seguinte origem:

Tela Tabela de Entidades Ligadas


Regra de seleção:
A geração do relatório será de acordo com os critérios de filtro informados na tela de geração.

-Empresa = empresa do login
-Estabelecimento = estabelecimento informado em tela
-Validade Inicial = A partir da Validade Inicial informada em tela


Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a mensagem “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no relatório.


Regra de processamento:

Para cada estabelecimento selecionado em tela será gerado um relatório.

Serão recuperadas as informações dos da Tela Tabela de Entidades Ligadas de acordo com a regra de seleção, todas as informações para a Empresa e Estabelecimento a partir da Validade Inicial (campo ‘Início Validade’ do agrupamento de Registro de Tabela de Entidades Ligadas) caso informada, se não serão recuperadas todas as informações para a Empresa e Estabelecimento de todas as validades.


Ordenação:
Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

- Empresa
- Estabelecimento
- Validade Inicial



Segue regras do preenchimento dos dados no relatório:





### Layout do Relatório






| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-79881 | Alessandra Cristina Navatta | Criação do Relatório | 17/03/2022 |
|  |  |  |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | S | Default: estabelecimento do login, quando for o caso. | Lista dos estabelecimentos da empresa do login. | MFS-79881 |
| Validade Inicial | Alfanumérico | N | S | Formato: DD/MM/AAAA  Default: Habilitado | Validade Inicial da tabela de entidade ligada, a ser considerada na geração, caso informada. | MFS-79881 |


| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Empresa | Texto |  | Razão social da empresa. | MFS-79881 |
| Página | Numérico |  | Número da página sequencial do relatório. | MFS-79881 |
| Estabelecimento | Texto | Centralizador - Cod – Razão Social  Ou   Descentralizador - Cod – Razão Social | Apresentar o estabelecimento que está sendo gerado o relatório | MFS-79881 |
| Data | Data | DD/MM/AAAA às HH:MM:SS h | Data de emissão e hora do relatório | MFS-79881 |
| Título | Texto |  | Título do relatório: “Relatório de Histórico das Alterações de Tabela de Entidades Ligadas” | MFS-79881 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Inicio Validade | Data | DD/MM/AAAA | Data Inicio da Validade (Valid_ini) tabela REINF_DADOS_INI_HIST | MFS-79881 |
| Fim Validade | Data | DD/MM/AAAA | Data Fim da Validade (Valid_fim) tabela REINF_DADOS_INI_HIST | MFS-79881 |
| Data Ocorrência | Data | DD/MM/AAAA HH:MM:SS h | Data da Ocorrência (Dat_ocorrencia) tabela REINF_DADOS_INI_HIST | MFS-79881 |
| Status | Alfanumérico |  | Status do Evento (Ind_status) tabela REINF_STATUS_DADOS_INI_HIST_V | MFS-79881 |
| Corpo do Relatório – Tabela de Entidades Ligadas | Corpo do Relatório – Tabela de Entidades Ligadas | Corpo do Relatório – Tabela de Entidades Ligadas | Corpo do Relatório – Tabela de Entidades Ligadas | Corpo do Relatório – Tabela de Entidades Ligadas |
| Classificação da Entidade Ligada | Alfanumérico |  | Campo ‘Classificação da Entidade Ligada’ da tela Tabela de Entidades Ligadas. | MFS-79881 |
| CNPJ da Entidade Ligada | Alfanumérico |  | Campo ‘CNPJ da Entidade Ligada’ da tela Tabela de Entidades Ligadas. | MFS-79881 |
