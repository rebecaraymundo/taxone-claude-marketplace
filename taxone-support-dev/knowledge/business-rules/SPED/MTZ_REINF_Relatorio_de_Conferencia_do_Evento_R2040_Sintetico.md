# MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2040_Sintetico

> Fonte: MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2040_Sintetico.docx






THOMSON REUTERS

Módulo EFD - REINF
Relatório de Conferência do Evento R-2040 - Sintético

Localização: Menu SPED, Módulo: EFD - REINF, item de menu Relatórios  Conferência dos Eventos  R-2040



DOCUMENTO DE REQUISITO


Sumário

1.	REGRAS DOS CAMPOS	3
2.	REGRAS DE GERAÇÃO DO RELATÓRIO	6
2.1.	Layout do Relatório	12

## REGRAS DOS CAMPOS


Localização da tela: Menu: SPED, Módulo: EFD - REINF, item de menu Relatórios > Conferência dos Eventos > R-2040
Título da tela: Relatório de Conferência do Evento R-2040




















## REGRAS DE GERAÇÃO DO RELATÓRIO


Regra Geral:
Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.

Origem das informações para geração:
Para geração deste relatório, serão consideradas as informações da seguinte origem:

Evento R-2040 (SAFX03, SAFX04, SAFX09 e Cadastro do Estabelecimento).

Regra de seleção:
A geração do relatório será de acordo com os critérios de filtro informados na tela de geração.

-Empresa = empresa do login
-Período = período informado em tela
- Versão = versão informada em tela
-Tipo = tipo de relatório informado em tela
-Tipo de Ambiente = tipo de ambiente informado em tela
-Estabelecimento = estabelecimento informado em tela


Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a mensagem “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no relatório.


Regra de processamento:

Para cada estabelecimento selecionado em tela será gerado um relatório.

Serão recuperadas as informações do evento R-2040 de acordo com a regra de seleção, todas as informações para a Empresa e Estabelecimento de acordo com o período informado. Relatório demonstrará as informações consolidadas por Estabelecimento, CNPJ Associação Desportiva. Será recuperado sempre a ultima ocorrência do evento R-2040 por Tipo e Número de Inscrição do contribuinte. Relatório demostrará as informações consolidadas.




Ordenação:
Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

- Empresa
- Estabelecimento

Segue regras do preenchimento dos dados no relatório:






















### Layout do Relatório




| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS17630 | Lara Aline | Alteração do Modulo REINF para criação de um relatório de conferência do evento R-2040. Novo relatório  “Relatório de Conferência do Evento R-2040”. | 25/06/2018 (criação do documento) |
|  |  |  |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período | Data | S | S | Formato: MM/AAAA  Default: Habilitado | Local para digitação do período inicial e final de referencia da geração do relatório, no formato de DD/MM/AAAA.  Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para a criação do relatório. | MFS17630 |
| Versão | Texto | S | S | Default: Versão atual | Este campo exibe todas as versões de layout do Reinf:  - 1.3.02 | MFS17630 |
| Tipo do Relatório | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções:  - Analítico - Sintético | MFS17630 |
| Tipo de Ambiente | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de ambiente entre as opções:  - Produção Restrita - Produção | MFS17630 |
| Geração Multiempresa | CheckBox | S | S | Default: não selecionado | Quando o usuário selecionar esta opção, será exibido no campo Estabelecimento, todas as empresas, contendo o código da empresa, código e a razão social de cada estabelecimento. | MFS17630 |
| Estabelecimentos | CheckBox | S | S | Default: não selecionado | Este campo exibe todos os estabelecimentos da empresa que acessou o módulo do EFD-Reinf.   A partir do parâmetro “Geração Multiempresa”, a lista passou a funcionar da seguinte forma:  - Caso o parâmetro “Geração Multiempresa” estiver desmarcado: Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento, somente da empresa que acessou o módulo. XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento).       - Caso o parâmetro “Geração Multiempresa” estiver marcado: Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento, mas neste caso serão mostradas todas as empresas: XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento)         Obs: No caso da geração multiempresa, as regras da geração do relatório não se modificam. A diferença é apenas na chamada, já que na lista de estabelecimentos para geração do relatório existirão estabelecimentos de empresas distintas.  O usuário deverá escolher obrigatoriamente ao menos um estabelecimento para a geração do relatório.  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento deve ser Selecionado”  Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”. | MFS17630 |


| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Empresa | Texto |  | Razão social da empresa. | MFS17630 |
| Data | Data | DD/MM/AAAA às HH:MM:SS hs | Data de emissão e hora do relatório | MFS17630 |
| Página | Numérico |  | Número da página sequencial do relatório | MFS17630 |
| Título | Texto |  | Título do relatório: “Relatório de Conferência do Evento R-2040 - Sintético” | MFS17630 |
| Período | Data | Formato: MM/AAAA | Deverá ser exibido o período informado em tela. | MFS17630 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Estabelecimento | Texto |  | Estabelecimento informado em tela | MFS17630 |
| Corpo do Relatório – Informação de Identificação do Evento/Contribuinte | Corpo do Relatório – Informação de Identificação do Evento/Contribuinte | Corpo do Relatório – Informação de Identificação do Evento/Contribuinte | Corpo do Relatório – Informação de Identificação do Evento/Contribuinte | Corpo do Relatório – Informação de Identificação do Evento/Contribuinte |
| Tipo de Arquivo | Numérico |  | Tipo de Arquivo, gerado no campo indRetif do evento R-2040. | MFS17630 |
| Número Recibo | Alfanumérico |  | Número Recibo, gerado no campo nrRecibo do evento R-2040. | MFS17630 |
| Tipo Ambiente | Alfanumérico |  | Tipo Ambiente, gerado no campo tpAmb do evento R-2040. | MFS17630 |
| Processo de Emissão | Alfanumérico |  | Processo de Emissão, gerado no campo procEmi do evento R-2040. | MFS17630 |
| Versão do Processo de Emissão | Alfanumérico |  | Versão do Processo de Emissão, gerado no campo procEmi do evento R-2040. | MFS17630 |
| Tipo de Inscrição Contribuinte | Alfanumérico |  | Tipo de Inscrição Contribuinte, gerado no campo tpInsc do evento R-2040. | MFS17630 |
| Número de Inscrição Contribuinte | Data | DD/MM/AAAA | Número de Inscrição Contribuinte, gerado no campo nrInsc do evento R-2040. | MFS17630 |
| Corpo do Relatório –  Identificação do estabelecimento que efetou o repasse de recursos a Associação Desportiva que mantém equipe de futebol profissional | Corpo do Relatório –  Identificação do estabelecimento que efetou o repasse de recursos a Associação Desportiva que mantém equipe de futebol profissional | Corpo do Relatório –  Identificação do estabelecimento que efetou o repasse de recursos a Associação Desportiva que mantém equipe de futebol profissional | Corpo do Relatório –  Identificação do estabelecimento que efetou o repasse de recursos a Associação Desportiva que mantém equipe de futebol profissional | Corpo do Relatório –  Identificação do estabelecimento que efetou o repasse de recursos a Associação Desportiva que mantém equipe de futebol profissional |
| Tipo Inscrição Estabelecimento | Alfanumérico |  | Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R-2040. | MFS17630 |
| Número Inscrição Estabelecimento | Alfanumérico |  | Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R-2040. | MFS17630 |
| Corpo do Relatório –  DETALHAMENTO DOS REPASSES EFETUADOS PELO ESTABELECIMENTO | Corpo do Relatório –  DETALHAMENTO DOS REPASSES EFETUADOS PELO ESTABELECIMENTO | Corpo do Relatório –  DETALHAMENTO DOS REPASSES EFETUADOS PELO ESTABELECIMENTO | Corpo do Relatório –  DETALHAMENTO DOS REPASSES EFETUADOS PELO ESTABELECIMENTO | Corpo do Relatório –  DETALHAMENTO DOS REPASSES EFETUADOS PELO ESTABELECIMENTO |
| CNPJ Associação Desportiva | Alfanumérico |  | CNPJ Associação Desportiva, gerado no campo cnpjAssocDesp do evento R-2040. | MFS17630 |
| Valor Total Bruto Recursos Repassados | Numérico | Default: 0,000 | Valor Total Bruto Recursos Repassados (VLR_TOT da SAFX09 ou VLR_BRUTO da SAFX03), gerado no campo vlrTotalRep do evento R-2040. | MFS17630 |
| Valor Total Retenção Recursos Recebidos | Numérico | Default: 0,000 | Valor Total Retenção Recursos Recebidos (VLR_INSS_RETIDO da SAFX09 ou VLR_RET da SAFX03), gerado no campo vlrTotalRet do evento R-2040. | MFS17630 |
| Valor Total Não Retenção | Numérico | Default: 0,000 | Valor Total Não Retenção (VLR_N_RET_PRINC da SAFX09 ou VLR_N_RET” da SAFX03), gerado no campo vlrTotalNRet do evento R-2040. | MFS17630 |
