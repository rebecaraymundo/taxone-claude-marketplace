# MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2010_Sintetico

> Fonte: MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2010_Sintetico.docx






THOMSON REUTERS

Módulo EFD - REINF
Relatório de Conferência do Evento R-2010 - Sintético

Localização: Menu SPED, Módulo: EFD - REINF, item de menu Relatórios  Conferência dos Eventos  R-2010

DOCUMENTO DE REQUISITO


Sumário

1.	REGRAS DOS CAMPOS	3
2.	REGRAS DE GERAÇÃO DO RELATÓRIO	4
2.1.	Layout do Relatório	9

## REGRAS DOS CAMPOS


Localização da tela: Menu: SPED, Módulo: EFD - REINF, item de menu Relatórios  Conferência dos Eventos  R-2010
Título da tela: Relatório de Conferência do Evento R-2010



## REGRAS DE GERAÇÃO DO RELATÓRIO


Regra Geral:
Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.

Origem das informações para geração:
Para geração deste relatório, serão consideradas as informações da seguinte origem:

Evento R-2010 (SAFX04, SAFX07, SAFX08, SAFX09 e Cadastro do Estabelecimento).

Regra de seleção:
A geração do relatório será de acordo com os critérios de filtro informados na tela de geração.

-Empresa = empresa do login
-Período = período informado em tela
- Versão = versão informada em tela
-Tipo = tipo de relatório informado em tela
-Estabelecimento = estabelecimento informado em tela

Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a mensagem “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no relatório.


Regra de processamento:

[MFS533595] Tratamento p/ desconsiderar os eventos com status de exclusão.

Para cada estabelecimento selecionado em tela será gerado um relatório.

Serão recuperadas as informações do evento R-2010 de acordo com a regra de seleção, todas as informações para a Empresa e Estabelecimento de acordo com o período informado. Relatório demonstrará as informações consolidadas por Estabelecimento/Obra, Prestador. Será recuperado sempre a última ocorrência do evento R-2010, exceto para os eventos com status de exclusão (Evento Excluído na Mensageria), pois não devem ser considerados no Relatório.

[MFS572946] Complemento da regra da [MFS533595], para considerar o envio do novo evento R-2010, após evento de exclusão.
Para o evento que teve exclusão e está com status de exclusão (Evento Excluído na Mensageria), SE o evento tiver uma nova geração, o mesmo deverá ser demonstrado no relatório, por Estabelecimento/Obra, Prestador, NFs e Tipo de Serviço. Será recuperado sempre a última ocorrência do evento


[MFS18433]
Obs.: Ao final do relatório nos campos de valores deve ser realizada uma totalização dos valores gerados no relatório.


Ordenação:
Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

- Empresa
- Estabelecimento

Segue regras do preenchimento dos dados no relatório:






### Layout do Relatório




| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS15340 | Lara Aline | Alteração do Modulo REINF para criação de um relatório de conferência do evento R-2010. Novo relatório  “Relatório de Conferência do Evento R-2010”. | 04/01/2018 (criação do documento) |
| MFS18226 | Lara Aline | Inclusão do campo Tipo de Ambiente | 04/06/2018 |
| MFS18964 | Lara Aline | Ajuste no campo CNPJ Prestador para recuperar a razão social mais atual. | 06/06/2018 |
| MFS18433 | Lara Aline | Inclusão filtro por Prestador e inclusão de totalização dos valores | 29/06/2018 |
| MFS533595 | Rogério Ohashi | Alteração da regra de recuperação dos registros para desconsiderar os eventos com Status de Exclusão (Evento Excluído na Mensageria). | 29/05/2023 |
| MFS572946 | Rosemeire Santos | Alteração da regra de para considerar o envio do novo evento após o evento de Exclusão (Evento Excluído na Mensageria). | MFS572946 |
| MFS938875 | Rogério Ohashi | Inclusão do parâmetro “Razão Social”, se desmarcado não será gerado a informação de Razão Social na coluna “CNPJ Prestador” melhorando consideravelmente o tempo de geração. | 15/10/2025 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período | Data | S | S | Formato: MM/AAAA  Default: Habilitado | Local para digitação do período inicial e final de referencia da geração do relatório, no formato de DD/MM/AAAA.  Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para a criação do relatório. | MFS15340 |
| Versão | Texto | S | S | Default: Versão atual | Este campo exibe todas as versões de layout do Reinf:  - 1.2 - 1.3 | MFS15340 |
| Tipo do Relatório | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções:  - Analítico - Sintético | MFS15340 |
| Tipo de Ambiente | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de ambiente entre as opções:  - Produção Restrita - Produção | MFS18226 |
| Prestador do Serviço – Todos | Alfanumérico | N | S | Default: Opção “Todos” marcada | Na abertura da tela a opção “Todos” aparecerá sempre marcada, e o campo “CNPJ” fica desabilitado;  Caso o usuário desmarque a opção “Todos”, o campo “CNPJ” será habilitado, e o usuário poderá informar o CNPJ do prestador. | MFS18433 |
| Prestador do Serviço – CNPJ | Alfanumérico | N | S |  | Na abertura da tela este campo aparecerá sempre desabilitado;  Será habilitado apenas quando o usuário desmarcar a opção “Todos”.  Quando preenchido, deve ser um CNPJ válido, caso contrário, será exibida uma mensagem (ex: “CNPJ inválido”).  Sempre que a opção “Todos” estiver desmarcada, será obrigatório informar o CNPJ do prestador antes de solicitar a emissão do relatório. Caso contrário, será exibida uma mensagem (ex: “Informar o CNPJ do Prestador do Serviço”). | MFS18433 |
| Razão Social | CheckBox | N | S | Default: Selecionado | Caso o usuário desmarque essa opção o Relatório será gerado sem a informação da Razão Social do Prestador de Serviço, na coluna CNPJ do Prestador, e passará a ser informado somente a informação de CNPJ | MFS938875 |
| Geração Multiempresa | CheckBox | S | S | Default: não selecionado | Quando o usuário selecionar esta opção, será exibido no campo Estabelecimento, todas as empresas, contendo o código da empresa, código e a razão social de cada estabelecimento. | MFS15340 |
| Estabelecimentos | CheckBox | S | S | Default: não selecionado | Este campo exibe todos os estabelecimentos da empresa que acessou o módulo do EFD-Reinf.   A partir do parâmetro “Geração Multiempresa”, a lista passou a funcionar da seguinte forma:  - Caso o parâmetro “Geração Multiempresa” estiver desmarcado: Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento, somente da empresa que acessou o módulo. XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento).       - Caso o parâmetro “Geração Multiempresa” estiver marcado: Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento, mas neste caso serão mostradas todas as empresas: XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento)         Obs: No caso da geração multiempresa, as regras da geração do relatório não se modificam. A diferença é apenas na chamada, já que na lista de estabelecimentos para geração do relatório existirão estabelecimentos de empresas distintas.  O usuário deverá escolher obrigatoriamente ao menos um estabelecimento para a geração do relatório.  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento deve ser Selecionado”  Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”. | MFS15340 |


| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Empresa | Texto |  | Razão social da empresa. | MFS15340 |
| Data | Data | DD/MM/AAAA às HH:MM:SS hs | Data de emissão e hora do relatório | MFS15340 |
| Página | Numérico |  | Número da página sequencial do relatório | MFS15340 |
| Título | Texto |  | Título do relatório: “Relatório de Histórico das Alterações - Dados Iniciais” | MFS15340 |
| Período | Data | Formato: MM/AAAA | Deverá ser exibido o período informado em tela. | MFS15340 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Estabelecimento | Texto |  | Estabelecimento informado em tela | MFS15340 |
| Corpo do Relatório – Informação de Identificação do Evento/Contribuinte | Corpo do Relatório – Informação de Identificação do Evento/Contribuinte | Corpo do Relatório – Informação de Identificação do Evento/Contribuinte | Corpo do Relatório – Informação de Identificação do Evento/Contribuinte | Corpo do Relatório – Informação de Identificação do Evento/Contribuinte |
| Tipo de Arquivo | Numérico |  | Tipo de Arquivo, gerado no campo indRetif do evento R-2010. | MFS15340 |
| Número Recibo | Alfanumérico |  | Número Recibo, gerado no campo nrRecibo do evento R-2010. | MFS15340 |
| Tipo Ambiente | Alfanumérico |  | Tipo Ambiente, gerado no campo tpAmb do evento R-2010. | MFS15340 |
| Processo de Emissão | Alfanumérico |  | Processo de Emissão, gerado no campo procEmi do evento R-2010. | MFS15340 |
| Versão do Processo de Emissão | Alfanumérico |  | Versão do Processo de Emissão, gerado no campo procEmi do evento R-2010. | MFS15340 |
| Tipo de Inscrição Contribuinte | Alfanumérico |  | Tipo de Inscrição Contribuinte, gerado no campo tpInsc do evento R-2010. | MFS15340 |
| Número de Inscrição Contribuinte | Data | DD/MM/AAAA | Número de Inscrição Contribuinte, gerado no campo nrInsc do evento R-2010. | MFS15340 |
| Corpo do Relatório – SERVIÇOS TOMADOS - CESSÃO DE MÃO DE OBRA OU EMPREITADA / Identificação do Estabelecimento/obra contratante dos Serviços | Corpo do Relatório – SERVIÇOS TOMADOS - CESSÃO DE MÃO DE OBRA OU EMPREITADA / Identificação do Estabelecimento/obra contratante dos Serviços | Corpo do Relatório – SERVIÇOS TOMADOS - CESSÃO DE MÃO DE OBRA OU EMPREITADA / Identificação do Estabelecimento/obra contratante dos Serviços | Corpo do Relatório – SERVIÇOS TOMADOS - CESSÃO DE MÃO DE OBRA OU EMPREITADA / Identificação do Estabelecimento/obra contratante dos Serviços | Corpo do Relatório – SERVIÇOS TOMADOS - CESSÃO DE MÃO DE OBRA OU EMPREITADA / Identificação do Estabelecimento/obra contratante dos Serviços |
| Tipo Inscrição Estabelecimento | Alfanumérico |  | Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R-2010. | MFS15340 |
| Número Inscrição Estabelecimento | Alfanumérico |  | Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R-2010. | MFS15340 |
| Indicativo Obra | Alfanumérico |  | Indicativo Obra, gerado no campo indObra do evento R-2010. | MFS15340 |
| Corpo do Relatório – Identificação do Prestador de Serviços mediante cessão de mão de obra ou empreitada | Corpo do Relatório – Identificação do Prestador de Serviços mediante cessão de mão de obra ou empreitada | Corpo do Relatório – Identificação do Prestador de Serviços mediante cessão de mão de obra ou empreitada | Corpo do Relatório – Identificação do Prestador de Serviços mediante cessão de mão de obra ou empreitada | Corpo do Relatório – Identificação do Prestador de Serviços mediante cessão de mão de obra ou empreitada |
| CNPJ Prestador | Alfanumérico |  | Demostrar o CNPJ (cnpjPrestador) + Razão Social do Prestador gerado no evento R-2010 (CPF_CGC da SAFX04).  A razão social será buscada da tabela SAFX04 conforme o CNPJ do Prestador do evento R-2010. Será recuperada a Razão Social de validade mais atual do Prestador. | MFS15340 MFS18964 |
| Valor Total Bruto | Numérico | Default: 0,000 | Valor Total Bruto (VLR_ITEM da SAFX08 ou VLR_TOT da SAFX09), gerado no campo vlrTotalBruto do evento R-2010. | MFS15340 |
| Valor Total Base Retenção | Numérico | Default: 0,000 | Valor Total Base Retenção (VLR_BASE_INSS) da SAFX08 ou SAFX09, gerado no campo vlrTotalBaseRet do evento R-2010. | MFS15340 |
| Valor Total Retenção Principal | Numérico | Default: 0,000 | Valor Total Retenção Principal (VLR_INSS_RETIDO – VLR_RET_SERV) da SAFX08 ou SAFX09, gerado no campo vlrTotalRetPrinc do evento R-2010. | MFS15340 |
| Valor Total Retenção Adicional | Numérico | Default: 0,000 | Valor Total Retenção Adicional (VLR_TOT_ADIC) da SAFX08 ou SAFX09, gerado no campo vlrTotalRetAdic do evento R-2010. | MFS15340 |
| Valor Total Não Retenção Principal | Numérico | Default: 0,000 | Valor Total Não Retenção Principal (VLR_N_RET_PRINC) da SAFX08 ou SAFX09, gerado no campo vlrTotalNRetPrinc do evento R-2010. | MFS15340 |
| Valor Total Não Retenção Adicional | Numérico | Default: 0,000 | Valor Total Não Retenção Adicional (VLR_N_RET_ADIC) da SAFX08 ou SAFX09, gerado no campo vlrTotalINRetAdic do evento R-2010. | MFS15340 |
| Indicativo CPRB | Alfanumérico |  | Indicativo CPRB, gerado no campo indCPRB do evento R-2010. | MFS15340 |
