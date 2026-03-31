# MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2060_Sintetico

> Fonte: MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2060_Sintetico.docx






THOMSON REUTERS

Módulo EFD - REINF
Relatório de Conferência do Evento R-2060 - Sintético

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

Serão recuperadas as informações do evento R-2060 de acordo com a regra de seleção, todas as informações para a Empresa e Estabelecimento de acordo com o período informado. Relatório demonstrará as informações consolidadas por Estabelecimento, Código de Atividade. Será recuperado sempre a ultima ocorrência do evento R-2060 por Tipo e Número de Inscrição do contribuinte. Relatório demostrará as informações consolidadas.


Ordenação:
Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

- Empresa
- Estabelecimento

Segue regras do preenchimento dos dados no relatório:






### Layout do Relatório




| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS15342 | Lara Aline | Alteração do Modulo REINF para criação de um relatório de conferência do evento R-2060. Novo relatório  “Relatório de Conferência do Evento R-2060”. | 24/01/2018 (criação do documento) |
| MFS18226 | Lara Aline | Inclusão do campo Tipo de Ambiente | 04/06/2018 |
|  |  |  |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período | Data | S | S | Formato: MM/AAAA  Default: Habilitado | Local para digitação do período inicial e final de referencia da geração do relatório, no formato de DD/MM/AAAA.  Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para a criação do relatório. | MFS15342 |
| Versão | Texto | S | S | Default: Versão atual | Este campo exibe todas as versões de layout do Reinf:  - 1.2 - 1.3 | MFS15342 |
| Tipo do Relatório | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções:  - Analítico - Sintético | MFS15342 |
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
| Corpo do Relatório – Informação de Identificação do Evento/Contribuinte | Corpo do Relatório – Informação de Identificação do Evento/Contribuinte | Corpo do Relatório – Informação de Identificação do Evento/Contribuinte | Corpo do Relatório – Informação de Identificação do Evento/Contribuinte | Corpo do Relatório – Informação de Identificação do Evento/Contribuinte |
| Tipo de Arquivo | Numérico |  | Tipo de Arquivo, gerado no campo indRetif do evento R-2060. | MFS15342 |
| Número Recibo | Alfanumérico |  | Número Recibo, gerado no campo nrRecibo do evento R-2060. | MFS15342 |
| Tipo Ambiente | Alfanumérico |  | Tipo Ambiente, gerado no campo tpAmb do evento R-2060. | MFS15342 |
| Processo de Emissão | Alfanumérico |  | Processo de Emissão, gerado no campo procEmi do evento R-2060. | MFS15342 |
| Versão do Processo de Emissão | Alfanumérico |  | Versão do Processo de Emissão, gerado no campo procEmi do evento R-2060. | MFS15342 |
| Tipo de Inscrição Contribuinte | Alfanumérico |  | Tipo de Inscrição Contribuinte, gerado no campo tpInsc do evento R-2060. | MFS15342 |
| Número de Inscrição Contribuinte | Data | DD/MM/AAAA | Número de Inscrição Contribuinte, gerado no campo nrInsc do evento R-2060. | MFS15342 |
| Corpo do Relatório – INFORMAÇÃO DA CONTRIBUIÇÃO PREVIDENCIÁRIA SOBRE A RECEITA BRUTA /  Identificação do estabelecimento que auferiu a receita bruta | Corpo do Relatório – INFORMAÇÃO DA CONTRIBUIÇÃO PREVIDENCIÁRIA SOBRE A RECEITA BRUTA /  Identificação do estabelecimento que auferiu a receita bruta | Corpo do Relatório – INFORMAÇÃO DA CONTRIBUIÇÃO PREVIDENCIÁRIA SOBRE A RECEITA BRUTA /  Identificação do estabelecimento que auferiu a receita bruta | Corpo do Relatório – INFORMAÇÃO DA CONTRIBUIÇÃO PREVIDENCIÁRIA SOBRE A RECEITA BRUTA /  Identificação do estabelecimento que auferiu a receita bruta | Corpo do Relatório – INFORMAÇÃO DA CONTRIBUIÇÃO PREVIDENCIÁRIA SOBRE A RECEITA BRUTA /  Identificação do estabelecimento que auferiu a receita bruta |
| Tipo Inscrição Estabelecimento | Alfanumérico |  | Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R-2060. | MFS15342 |
| Número Inscrição Estabelecimento | Alfanumérico |  | Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R-2060. | MFS15342 |
| Valor Total Receita Bruta Estabelecimento | Numérico | Default: 0,000 | Valor Total Receita Bruta Estabelecimento (VLR_REC_BRT da SAFX185), gerado no campo VlrRecBrutaTotal do evento R-2060. | MFS15342 |
| Valor Total da Contribuição Previdenciária Apurada Estabelecimento | Numérico | Default: 0,000 | Valor Total da Contribuição Previdenciária Apurada Estabelecimento (VLR_CONT_PREV_REINF da SAFX185), gerado no campo VlrCPApurTotal do evento R-2060. | MFS15342 |
| Valor Total da Contribuição Previdenciária com exigibilidade suspensa | Numérico | Default: 0,000 | Valor Total da Contribuição Previdenciária com exigibilidade suspensa (VLR_PREV_EXIG_SUSP da SAFX2113), gerado no campo VlrCPRBSuspTotal do evento R-2060. | MFS15342 |
| Corpo do Relatório – VALOR TOTAL DA RECEITA POR TIPO DE CÓDIGO DE ATIVIDADE ECONÔMICA | Corpo do Relatório – VALOR TOTAL DA RECEITA POR TIPO DE CÓDIGO DE ATIVIDADE ECONÔMICA | Corpo do Relatório – VALOR TOTAL DA RECEITA POR TIPO DE CÓDIGO DE ATIVIDADE ECONÔMICA | Corpo do Relatório – VALOR TOTAL DA RECEITA POR TIPO DE CÓDIGO DE ATIVIDADE ECONÔMICA | Corpo do Relatório – VALOR TOTAL DA RECEITA POR TIPO DE CÓDIGO DE ATIVIDADE ECONÔMICA |
| Código Atividade Econômica | Alfanumérico |  | Código Atividade Econômica (COD_ATIV_CONT_PREV da SAFX185), gerado no campo codAtivEcon do evento R-2060. | MFS15342 |
| Valor Total Receita Bruta Atividade | Numérico | Default: 0,000 | Valor Total Receita Bruta Atividade (VLR_REC_BRT_ATIV da SAFX185), gerado no campo vlrRecBrutaAtiv do evento R-2060. | MFS15342 |
| Valor Total Exclusões Receita Bruta | Numérico | Default: 0,000 | Valor Total Exclusões Receita Bruta (VLR_AJUSTE_EXCLUSAO da SAFX185), gerado no campo vlrExcRecBruta do evento R-2060. | MFS15342 |
| Valor Total Adições Receita Bruta | Numérico | Default: 0,000 | Valor Total Adições Receita Bruta (VLR_AJUSTE_ADICAO da SAFX185) da SAFX08 ou SAFX09, gerado no campo vlrAdicRecBruta do evento R-2060. | MFS15342 |
| Valor Base Cálculo CPRB | Numérico | Default: 0,000 | Valor Base Cálculo CPRB (VLR_BASE_CONT_PREV_REINF da SAFX185), gerado no campo vlrBcCPRB do evento R-2060. | MFS15342 |
| Valor CPRB | Numérico | Default: 0,000 | Valor CPRB (VLR_CONT_PREV_REINF da SAFX185), gerado no campo vlrCPRBapur do evento R-2060. | MFS15342 |
