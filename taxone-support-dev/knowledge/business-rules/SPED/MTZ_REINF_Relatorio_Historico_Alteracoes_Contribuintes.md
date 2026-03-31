# MTZ_REINF_Relatorio_Historico_Alteracoes_Contribuintes

> Fonte: MTZ_REINF_Relatorio_Historico_Alteracoes_Contribuintes.docx






THOMSON REUTERS

Módulo EFD - REINF
Relatório de Histórico das Alterações - Contribuintes

Localização: Menu SPED, Módulo: EFD - REINF, item de menu Relatórios  Relatório de Histórico das Alterações  Contribuintes



DOCUMENTO DE REQUISITO


Sumário

1.	REGRAS DOS CAMPOS	4
2.	REGRAS DE GERAÇÃO DO RELATÓRIO	5
2.1.	Layout do Relatório	10

## REGRAS DOS CAMPOS


Localização da tela: Menu: SPED, Módulo: EFD - REINF, item de menu Relatórios/ Relatório de Histórico das Alterações / Contribuinte
Título da tela: Relatório de Histórico das Alterações – Contribuintes





















## REGRAS DE GERAÇÃO DO RELATÓRIO


Regra Geral:
Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.

Origem das informações para geração:
Para geração deste relatório, serão consideradas as informações da seguinte origem:

Cadastro de Informações do Contribuinte

Regra de seleção:
A geração do relatório será de acordo com os critérios de filtro informados na tela de geração.

-Empresa = empresa do login
-Estabelecimento = estabelecimento informado em tela
-Validade Inicial = A partir da Validade Inicial informada em tela


Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a mensagem “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no relatório.


Regra de processamento:

Para cada estabelecimento selecionado em tela será gerado um relatório.

Serão recuperadas as informações dos da Tela de Informações do Contribuinte de acordo com a regra de seleção, todas as informações para a Empresa e Estabelecimento a partir da Validade Inicial caso informada, se não serão recuperadas todas as informações para a Empresa e Estabelecimento de todas as validades.


Ordenação:
Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

- Empresa (cod_empresa)
- Validade Inicial (valid_ini)
- Data de Ocorrência (dat_ocorrencia)

Segue regras do preenchimento dos dados no relatório:






### Layout do Relatório




| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS12175 | Lara Aline | Alteração do Modulo REINF para criação de um relatório de histórico de alterações dos Dados Iniciais. Novo relatório  “Relatório de Histórico das Alterações - Contribuintes”. | 28/07/2017 (criação do documento) |
| MFS79878 | Alessandra Cristina Navatta | - Inclusão do campo referente a versão 2.1 do REINF; - Ajuste nas regras para referenciar a tela de Informações do Contribuinte ao invés de Dados Iniciais; - Ajuste no caminho do relatório que anteriormente apontava para o menu Parâmetros e não Relatórios.   Atenção: Os dois últimos pontos citados acima, são apenas ajustes na documentação funcional, que estava desatualizada. | 15/02/2022 |
| MFS-523052 | Alessandra Cristina Navatta | Inclusão do campo Indicativo de Entidade Vinculada a União | 22/03/2023 |
| MFS-840399 | Alessandra Cristina Navatta | Inclusão do campo Indicador de Pertencimento do IRRF, para atendimento do evento R-1000 (campo indPertIRRF), versão 2.1.2 (Nota Técnica 02/2025) | 20/06/2025 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | S | Default: estabelecimento do login, quando for o caso. | Lista dos estabelecimentos da empresa do login. | MFS12175 |
| Validade Inicial | Data | N | S | Formato: DD/MM/AAAA  Default: Habilitado | Validade Inicial a ser considerada na geração, caso informada. | MFS12175 |


| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Empresa | Texto |  | Razão social da empresa. | MFS12175 |
| Página | Numérico |  | Número da página sequencial do relatório | MFS12175 |
| Filial | Texto |  | Código e a razão social do estabelecimento em questão (estabelecimento informado em tela). | MFS12175 |
| Data | Data | DD/MM/AAAA às HH:MM:SS hs | Data de emissão e hora do relatório | MFS12175 |
| CNPJ | Alfanumérico |  | Deverá ser exibido o CNPJ do Estabelecimento. | MFS12175 |
| Título | Texto |  | Título do relatório: “Relatório de Histórico das Alterações - Contribuinte” | MFS12175 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Inicio Validade | Data | DD/MM/AAAA | Data Inicio da Validade (Valid_ini) tabela REINF_DADOS_INI_HIST | MFS12175 |
| Fim Validade | Data | DD/MM/AAAA | Data Fim da Validade (Valid_fim) tabela REINF_DADOS_INI_HIST | MFS12175 |
| Data Ocorrência | Data | DD/MM/AAAA HH:MM:SS hs | Data da Ocorrência (Dat_ocorrencia) tabela REINF_DADOS_INI_HIST | MFS12175 |
| Status | Alfanumérico |  | Status do Evento (Ind_status) tabela REINF_STATUS_DADOS_INI_HIST_V | MFS12175 |
| Corpo do Relatório – Registro de Informações de Cadastro do Contribuinte | Corpo do Relatório – Registro de Informações de Cadastro do Contribuinte | Corpo do Relatório – Registro de Informações de Cadastro do Contribuinte | Corpo do Relatório – Registro de Informações de Cadastro do Contribuinte | Corpo do Relatório – Registro de Informações de Cadastro do Contribuinte |
| Classificação Tributária | Alfanumérico |  | Classificação Tributária (cod_classif_trib) do cadastro da tela Informações do Contribuinte. | MFS12175 MFS-81450 |
| Escrituração Contábil na ECD | Alfanumérico |  | Escrituração Contábil ECD (ind_escritura_ecd) do cadastro da tela Informações do Contribuinte. | MFS12175 MFS-81450 |
| Desoneração da Folha | Alfanumérico |  | Desoneração da Folha (ind_desonera_folha) do cadastro da tela Informações do Contribuinte. | MFS12175 MFS-81450 |
| Acordo de Isenção de Multa | Alfanumérico |  | Acordo de Isenção (ind_acordo_isencao) do cadastro da tela Informações do Contribuinte. | MFS12175 MFS-81450 |
| Situação Pessoa Jurídica | Alfanumérico |  | Situação (ind_situacao_pj) do cadastro da tela Informações do Contribuinte. | MFS12175 MFS-81450 |
| Indicativo de Entidade Vinculada a União | Alfanumérico |  | Informação do campo ‘Indicativo de Entidade Vinculada a União’ da tela Informações do Contribuinte. | MFS-523052 |
| Data da Transformação de Entidade Beneficente de Assistência Social Isenta de Contribuições Sociais em Sociedade com Fins Lucrativos - Art. 13 - Lei 11096/2005 | Data |  | Informação do campo Data da Transformação de Entidade Beneficente de Assistência Social Isenta de Contribuições Sociais em Sociedade com Fins Lucrativos - Art. 13 - Lei 11096/2005 do cadastro da tela Informações do Contribuinte. | MFS-81450 |
| Indicador de Pertencimento do IRRF | Texto |  | Só deve ser exibida informação, se o parâmetro Pertencimento do IRRF, a tela de Informações do Contribuinte estiver marcado.Neste caso, apresentar Sim | MFS-840399 |
| Corpo do Relatório – Registro de Informações de Contato do Contribuinte | Corpo do Relatório – Registro de Informações de Contato do Contribuinte | Corpo do Relatório – Registro de Informações de Contato do Contribuinte | Corpo do Relatório – Registro de Informações de Contato do Contribuinte | Corpo do Relatório – Registro de Informações de Contato do Contribuinte |
| Nome | Alfanumérico |  | Nome do Contribuinte (Nome_contato) do cadastro da tela Informações do Contribuinte. | MFS12175 MFS-81450 |
| CPF | Numérico |  | CPF (Num_CPF) do cadastro da tela Informações do Contribuinte. | MFS12175 MFS-81450 |
| Telefone | Alfanumérico |  | Telefone (Num_tel_fixo) do cadastro da tela Informações do Contribuinte. | MFS12175 MFS-81450 |
| Celular | Alfanumérico |  | Celular (Num_tel_cel) do cadastro da tela Informações do Contribuinte. | MFS12175 MFS-81450 |
| E-mail | Alfanumérico |  | Email (Email) do cadastro da tela Informações do Contribuinte. | MFS12175 MFS-81450 |
| Corpo do Relatório – Registro de Informação de Software House | Corpo do Relatório – Registro de Informação de Software House | Corpo do Relatório – Registro de Informação de Software House | Corpo do Relatório – Registro de Informação de Software House | Corpo do Relatório – Registro de Informação de Software House |
| CNPJ | Alfanumérico |  | Situação (num_cnpj) do cadastro da tela Informações do Contribuinte – Registro de Informações da Software House. | MFS12175 MFS-81450 |
| Razão Social | Alfanumérico |  | Razão Social (razao_social) do cadastro da tela Informações do Contribuinte – Registro de Informações da Software House. | MFS12175 MFS-81450 |
| Nome do Contato | Alfanumérico |  | Nome do Contato (nome_contato) do cadastro da tela Informações do Contribuinte – Registro de Informações da Software House. | MFS12175 MFS-81450 |
| Telefone | Alfanumérico |  | Telefone (num_tel) do cadastro da tela Informações do Contribuinte – Registro de Informações da Software House. | MFS12175 MFS-81450 |
| Email | Alfanumérico |  | Email (email) do cadastro dos da tela Informações do Contribuinte – Registro de Informações da Software House. | MFS12175 MFS-81450 |
