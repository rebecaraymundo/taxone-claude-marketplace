# MTZ_REINF_Tela_Conferencia_Previa_Cadastros

> Fonte: MTZ_REINF_Tela_Conferencia_Previa_Cadastros.docx






THOMSON REUTERS

Conferência Prévia dos Cadastros
SPED – Reinf



DOCUMENTO DE REQUISITO



Sumário

1.	Regras dos Campos	3

## Regras dos Campos


Localização da tela: Módulo: SPED >> EFD – Reinf
Menu: REINF >> Conferência Prévia >> Cadastros

Título da tela: Conferência Prévia dos Cadastros

Obs: Ao abrir a tela de conferência deverá abrir uma subtela para seleção do Estabelecimento.
Título da tela: Selecionar Estabelecimento de Conferência Prévia dos Cadastros

[MFS18226]
Obs: O evento R-1000 de Limpeza não será apresentada na tela de conferência dos cadastros, esse evento será demostrado apenas no Painel de Controles de Eventos.




| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-10757 | Elenilson Coutinho | Inclusão da Tela de Conferência Prévia dos Cadastros (R-1070) do EFD – Reinf |
| MFS-10758 | Elenilson Coutinho | Inclusão da Tela de Conferência Prévia dos Cadastros (R-1000) do EFD – Reinf... |
| MFS13810 | Lara Aline | Ajuste no layout de tela do evento R-1070 (Campo Autoria da Ação Judicial). |
| MFS14462 | Lara Aline | Inclusão do campo Versão. |
| MFS18226 | Lara Aline | Inclusão observação sobre o evento R-1000 de Limpeza. |
| MFS-58345 | Alessandra Cristina Navatta | Reestruturação do Menu |
| MFS-81450 | Alessandra Cristina Navatta | Alteração das Informação do Evento R-1000, atendendo o layout Versão 2.1 |
| MFS-79881 | Alessandra Cristina Navatta | Inclusão das Informações do Evento R-1050, atendendo o layout Versão 2.1 |
| MFS-90863 | Alessandra Cristina Navatta | Alteração da versão 2.1 para 2.1.1   Não há regras a serem ajustada neste arquivo. |
| MFS-523048 | Alessandra Cristina Navatta | Inclusão do campo Indicativo de Entidade Vinculada a União, para atendimento do evento R-1000, versão 2.1.1. |
| MFS-840399 | Alessandra Cristina Navatta | Inclusão do campo Indicador de Pertencimento do IRRF, para atendimento do evento R-1000 (campo indPertIRRF), versão 2.1.2 (Nota Técnica 02/2025) |


| Campo | Campo | Tipo | Obrig | Obrig | Ed | Formato/Default | Formato/Default | Formato/Default | Regra | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Estabelecimento | TextBox | S | S | N | Formato: Código + Estabelecimento | Formato: Código + Estabelecimento | Formato: Código + Estabelecimento | Irá demonstrar o estabelecimento selecionado na chamada da subtela de seleção. | Irá demonstrar o estabelecimento selecionado na chamada da subtela de seleção. | MFS-10757 MFS-10758 |
| Versão | Versão | TextBox | S | S | N |  |  |  | Irá demostrar a versão de Leiaute da EFD-REINF | Irá demostrar a versão de Leiaute da EFD-REINF | MFS-14462 |
| Eventos-Reinf | Eventos-Reinf | Pasta | S | S | N |  |  |  | Irá demonstrar os eventos de cadastros pré-gerados (R-1000, R-1050 e R1070), conforme seleção de estabelecimento na subtela de seleção. | Irá demonstrar os eventos de cadastros pré-gerados (R-1000, R-1050 e R1070), conforme seleção de estabelecimento na subtela de seleção. | MFS-10757 MFS-10758 MFS-79881 |
| R-1000 – Informações do Contribuinte | R-1000 – Informações do Contribuinte | R-1000 – Informações do Contribuinte | R-1000 – Informações do Contribuinte | R-1000 – Informações do Contribuinte | R-1000 – Informações do Contribuinte | R-1000 – Informações do Contribuinte | R-1000 – Informações do Contribuinte | R-1000 – Informações do Contribuinte | R-1000 – Informações do Contribuinte | R-1000 – Informações do Contribuinte | R-1000 – Informações do Contribuinte |
| Identificação do Contribuinte | Identificação do Contribuinte | Identificação do Contribuinte | Identificação do Contribuinte | Identificação do Contribuinte | Identificação do Contribuinte | Identificação do Contribuinte | Identificação do Contribuinte | Identificação do Contribuinte | Identificação do Contribuinte | Identificação do Contribuinte | Identificação do Contribuinte |
| Tipo de Inscrição | Textbox | Textbox | S | N | N | N |  |  |  | MFS-10758 | MFS-10758 |
| Número de Inscrição | Textbox | Textbox | S | N | N | N |  |  |  | MFS-10758 | MFS-10758 |
| Validade Inicial | Textbox | Textbox | S | N | N | N |  |  |  | MFS-10758 | MFS-10758 |
| Validade Final | Textbox | Textbox | N | N | N | N |  |  |  | MFS-10758 | MFS-10758 |
| Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências |
| Data da Ocorrência | Data da Ocorrência | Textbox | S | S | N |  |  |  |  |  | MFS-10758 |
| Operação | Operação | Textbox | S | S | N |  |  |  |  |  | MFS-10758 |
| Classificação Tributária | Classificação Tributária | Textbox | S | S | N |  |  |  |  |  | MFS-10758 |
| Escrituração na ECD | Escrituração na ECD | Textbox | N | N | N |  |  |  |  |  | MFS-10758 |
| Desoneração Folha | Desoneração Folha | Textbox | S | S | N |  |  |  |  |  | MFS-10758 |
| Acordo de Isenção | Acordo de Isenção | Textbox | S | S | N |  |  |  |  |  | MFS-10758 |
| Situação PJ | Situação PJ | Textbox | N | N | N |  |  |  |  |  | MFS-10758 |
| Indicativo de Entidade Vinculada a União | Indicativo de Entidade Vinculada a União | Textbox | N | N | N |  |  |  |  |  | MFS-523048 |
| Data da Transformação de Entidade Beneficente de Assistência Social Isenta de Contribuições Sociais em Sociedade com Fins Lucrativos - Art. 13 - Lei 11096/2005 | Data da Transformação de Entidade Beneficente de Assistência Social Isenta de Contribuições Sociais em Sociedade com Fins Lucrativos - Art. 13 - Lei 11096/2005 | Textbox | N | N | N |  |  |  |  |  | MFS-81450 |
| Indicador de Pertencimento do IRRF | Indicador de Pertencimento do IRRF | Texto | N | N | N |  |  |  | Só deve ser exibida informação, se o parâmetro Pertencimento do IRRF, a tela de Informações do Contribuinte estiver marcado.Neste caso, apresentar Sim | Só deve ser exibida informação, se o parâmetro Pertencimento do IRRF, a tela de Informações do Contribuinte estiver marcado.Neste caso, apresentar Sim | MFS-840399 |
| Nome do Contato | Nome do Contato | Textbox | S | S | N |  |  |  |  |  | MFS-10758 |
| CPF do Contato | CPF do Contato | Textbox | S | S | N |  |  |  |  |  | MFS-10758 |
| Telefone Fixo | Telefone Fixo | Textbox | N | N | N |  |  |  |  |  | MFS-10758 |
| Celular | Celular | Textbox | N | N | N |  |  |  |  |  | MFS-10758 |
| Email | Email | Textbox | N | N | N |  |  |  |  |  | MFS-10758 |
| Validade Final | Validade Final | Textbox | S | S | N |  |  |  |  |  | MFS-10758 |
| Nova Validade Final | Nova Validade Final | Textbox | S | S | N |  |  |  |  |  | MFS-10758 |
| Situação | Situação | Textbox | S | S | N |  |  |  |  |  | MFS-10758 |
| Informação da Software House | Informação da Software House | Informação da Software House | Informação da Software House | Informação da Software House | Informação da Software House | Informação da Software House | Informação da Software House | Informação da Software House | Informação da Software House | Informação da Software House | Informação da Software House |
| CNPJ | CNPJ | Textbox | S | S | N |  |  |  |  |  | MFS-10758 |
| Razão Social | Razão Social | Textbox | S | S | N |  |  |  |  |  | MFS-10758 |
| Nome do Contato | Nome do Contato | Textbox | S | S | N |  |  |  |  |  | MFS-10758 |
| Telefone | Telefone | Textbox | N | N | N |  |  |  |  |  | MFS-10758 |
| Email | Email | Textbox | N | N | N |  |  |  |  |  | MFS-10758 |
| R-1050 – Tabela de Entidades Ligadas | R-1050 – Tabela de Entidades Ligadas | R-1050 – Tabela de Entidades Ligadas | R-1050 – Tabela de Entidades Ligadas | R-1050 – Tabela de Entidades Ligadas | R-1050 – Tabela de Entidades Ligadas | R-1050 – Tabela de Entidades Ligadas | R-1050 – Tabela de Entidades Ligadas | R-1050 – Tabela de Entidades Ligadas | R-1050 – Tabela de Entidades Ligadas | R-1050 – Tabela de Entidades Ligadas | R-1050 – Tabela de Entidades Ligadas |
| Informações Relacionadas a Entidades Ligadas | Informações Relacionadas a Entidades Ligadas | Informações Relacionadas a Entidades Ligadas | Informações Relacionadas a Entidades Ligadas | Informações Relacionadas a Entidades Ligadas | Informações Relacionadas a Entidades Ligadas | Informações Relacionadas a Entidades Ligadas | Informações Relacionadas a Entidades Ligadas | Informações Relacionadas a Entidades Ligadas | Informações Relacionadas a Entidades Ligadas | Informações Relacionadas a Entidades Ligadas | Informações Relacionadas a Entidades Ligadas |
| Classificação da Entidade Ligada | Classificação da Entidade Ligada | Textbox | S | S | N |  |  |  |  |  | MFS-79881 |
| CNPJ | CNPJ | Textbox | S | S | N |  |  |  |  |  | MFS-79881 |
| Início Validade | Início Validade | Textbox | S | S | N |  |  |  |  |  | MFS-79881 |
| Fim Validade | Fim Validade | Textbox | N | N | N |  |  |  |  |  | MFS-79881 |
| Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências |
| Data da Ocorrência | Data da Ocorrência | Textbox | S | S | N |  |  |  |  |  | MFS-79881 |
| Operação | Operação | Textbox | S | S | N |  |  |  |  |  | MFS-79881 |
| Classificação da Entidade Ligada | Classificação da Entidade Ligada | Textbox | S | S | N |  |  |  |  |  | MFS-79881 |
| Validade Final | Validade Final | Textbox | S | S | N |  |  |  |  |  | MFS-79881 |
| Nova Validade Final | Nova Validade Final | Textbox | S | S | N |  |  |  |  |  | MFS-79881 |
| Situação | Situação | Textbox | S | S | N |  |  |  |  |  | MFS-79881 |
| R-1070 – Tabela de Processos Administrativos/Judiciais | R-1070 – Tabela de Processos Administrativos/Judiciais | R-1070 – Tabela de Processos Administrativos/Judiciais | R-1070 – Tabela de Processos Administrativos/Judiciais | R-1070 – Tabela de Processos Administrativos/Judiciais | R-1070 – Tabela de Processos Administrativos/Judiciais | R-1070 – Tabela de Processos Administrativos/Judiciais | R-1070 – Tabela de Processos Administrativos/Judiciais | R-1070 – Tabela de Processos Administrativos/Judiciais | R-1070 – Tabela de Processos Administrativos/Judiciais | R-1070 – Tabela de Processos Administrativos/Judiciais | R-1070 – Tabela de Processos Administrativos/Judiciais |
| Identificação do Processo | Identificação do Processo | Identificação do Processo | Identificação do Processo | Identificação do Processo | Identificação do Processo | Identificação do Processo | Identificação do Processo | Identificação do Processo | Identificação do Processo | Identificação do Processo | Identificação do Processo |
| Tipo do Processo | Tipo do Processo | Textbox | S | S | N |  |  |  | Irá demonstrar o tipo de inscrição do estabelecimento.  1-CNPJ | Irá demonstrar o tipo de inscrição do estabelecimento.  1-CNPJ | MFS-10757 |
| Número do Processo | Número do Processo | Textbox | S | S | N |  |  |  | Irá demonstrar o número de inscrição do estabelecimento. | Irá demonstrar o número de inscrição do estabelecimento. | MFS-10757 |
| Validade Inicial | Validade Inicial | Textbox | S | S | N |  |  |  |  |  | MFS-10757 |
| Validade Final | Validade Final | Textbox | N | N | N |  |  |  |  |  | MFS-10757 |
| Autoria da Ação Judicial | Autoria da Ação Judicial | Textbox | N | N | N |  |  |  |  |  | MFS13810 |
| Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências |
| Data da Ocorrência | Data da Ocorrência | Textbox | S | S | N |  |  |  |  |  | MFS-10757 |
| Operação | Operação | Textbox | S | S | N |  |  |  |  |  | MFS-10757 |
| UF Seção Judiciária | UF Seção Judiciária | Textbox | S | S | N |  |  |  |  |  | MFS-10757 |
| Município | Município | Textbox | N | N | N |  |  |  |  |  | MFS-10757 |
| Identificação da Vara | Identificação da Vara | Textbox | S | S | N |  |  |  |  |  | MFS-10757 |
| Autoria da Ação Judicial | Autoria da Ação Judicial | Textbox | N | N | N |  |  |  |  |  | MFS-10757 MFS13810 |
| Validade Final | Validade Final | Textbox | S | S | N |  |  |  |  |  | MFS-10757 |
| Nova Validade Final | Nova Validade Final | Textbox | S | S | N |  |  |  |  |  | MFS-10757 |
| Situação | Situação | Textbox | S | S | N |  |  |  |  |  | MFS-10757 |
| Suspensão de Exigibilidade de Tributos | Suspensão de Exigibilidade de Tributos | Suspensão de Exigibilidade de Tributos | Suspensão de Exigibilidade de Tributos | Suspensão de Exigibilidade de Tributos | Suspensão de Exigibilidade de Tributos | Suspensão de Exigibilidade de Tributos | Suspensão de Exigibilidade de Tributos | Suspensão de Exigibilidade de Tributos | Suspensão de Exigibilidade de Tributos | Suspensão de Exigibilidade de Tributos | Suspensão de Exigibilidade de Tributos |
| Código da Suspensão | Código da Suspensão | Textbox | N | N | N |  |  |  |  |  | MFS-10757 |
| Indicador de Suspensão | Indicador de Suspensão | Textbox | S | S | N |  |  |  |  |  | MFS-10757 |
| Data Decisão | Data Decisão | Textbox | S | S | N |  |  |  |  |  | MFS-10757 |
| Indicador de Depósito | Indicador de Depósito | Textbox | S | S | N |  |  |  |  |  | MFS-10757 |
