# MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2050_Sintetico

> Fonte: MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2050_Sintetico.docx






THOMSON REUTERS

Módulo EFD - REINF
Relatório de Conferência do Evento R-2050 - Sintético

Localização: Menu SPED, Módulo: EFD - REINF, item de menu Relatórios  Conferência dos Eventos  R-2050



DOCUMENTO DE REQUISITO


Sumário

1.	REGRAS DOS CAMPOS	3
2.	REGRAS DE GERAÇÃO DO RELATÓRIO	6
2.1.	Layout do Relatório	14

## REGRAS DOS CAMPOS


Localização da tela: Menu: SPED, Módulo: EFD - REINF, item de menu Relatórios > Conferência dos Eventos > R-2050
Título da tela: Relatório de Conferência do Evento R-2050
























## REGRAS DE GERAÇÃO DO RELATÓRIO


Regra Geral:
Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.

Origem das informações para geração:
Para geração deste relatório, serão consideradas as informações da seguinte origem:

Evento R-2050 (SAFX07, SAFX263, Cadastro do Estabelecimento e tela  da Comercialização da Produção por Produtor Rural PJ/Agroindústria).

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

Serão recuperadas as informações do evento R-2050 de acordo com a regra de seleção, todas as informações para a Empresa e Estabelecimento de acordo com o período informado. Relatório demonstrará as informações consolidadas por Estabelecimento, Tipo de Comercialização. Será recuperado sempre a ultima ocorrência do evento R-2050 por Tipo e Número de Inscrição do contribuinte. Relatório demostrará as informações consolidadas.




Ordenação:
Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

- Empresa
- Estabelecimento

Segue regras do preenchimento dos dados no relatório:









### Layout do Relatório




| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS17631 | Lara Aline | Alteração do Modulo REINF para criação de um relatório de conferência do evento R-2050. Novo relatório  “Relatório de Conferência do Evento R-2050”. | 21/05/2018 (criação do documento) |
| MFS18226 | Lara Aline | Inclusão do campo Tipo de Ambiente | 04/06/2018 |
|  |  |  |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período | Data | S | S | Formato: MM/AAAA  Default: Habilitado | Local para digitação do período inicial e final de referencia da geração do relatório, no formato de DD/MM/AAAA.  Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para a criação do relatório. | MFS17631 |
| Versão | Texto | S | S | Default: Versão atual | Este campo exibe todas as versões de layout do Reinf:  - 1.3.02 | MFS17631 |
| Tipo do Relatório | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções:  - Analítico - Sintético | MFS17631 |
| Tipo de Ambiente | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de ambiente entre as opções:  - Produção Restrita - Produção | MFS18226 |
| Geração Multiempresa | CheckBox | S | S | Default: não selecionado | Quando o usuário selecionar esta opção, será exibido no campo Estabelecimento, todas as empresas, contendo o código da empresa, código e a razão social de cada estabelecimento. | MFS17631 |
| Estabelecimentos | CheckBox | S | S | Default: não selecionado | Este campo exibe todos os estabelecimentos da empresa que acessou o módulo do EFD-Reinf.   A partir do parâmetro “Geração Multiempresa”, a lista passou a funcionar da seguinte forma:  - Caso o parâmetro “Geração Multiempresa” estiver desmarcado: Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento, somente da empresa que acessou o módulo. XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento).       - Caso o parâmetro “Geração Multiempresa” estiver marcado: Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento, mas neste caso serão mostradas todas as empresas: XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento)         Obs: No caso da geração multiempresa, as regras da geração do relatório não se modificam. A diferença é apenas na chamada, já que na lista de estabelecimentos para geração do relatório existirão estabelecimentos de empresas distintas.  O usuário deverá escolher obrigatoriamente ao menos um estabelecimento para a geração do relatório.  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento deve ser Selecionado”  Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”. | MFS17631 |


| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Empresa | Texto |  | Razão social da empresa. | MFS17631 |
| Data | Data | DD/MM/AAAA às HH:MM:SS hs | Data de emissão e hora do relatório | MFS17631 |
| Página | Numérico |  | Número da página sequencial do relatório | MFS17631 |
| Título | Texto |  | Título do relatório: “Relatório de Conferência do Evento R-2050 - Sintético” | MFS17631 |
| Período | Data | Formato: MM/AAAA | Deverá ser exibido o período informado em tela. | MFS17631 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Estabelecimento | Texto |  | Estabelecimento informado em tela | MFS17631 |
| Corpo do Relatório – Informação de Identificação do Evento/Contribuinte | Corpo do Relatório – Informação de Identificação do Evento/Contribuinte | Corpo do Relatório – Informação de Identificação do Evento/Contribuinte | Corpo do Relatório – Informação de Identificação do Evento/Contribuinte | Corpo do Relatório – Informação de Identificação do Evento/Contribuinte |
| Tipo de Arquivo | Numérico |  | Tipo de Arquivo, gerado no campo indRetif do evento R-2050. | MFS17631 |
| Número Recibo | Alfanumérico |  | Número Recibo, gerado no campo nrRecibo do evento R-2050. | MFS17631 |
| Tipo Ambiente | Alfanumérico |  | Tipo Ambiente, gerado no campo tpAmb do evento R-2050. | MFS17631 |
| Processo de Emissão | Alfanumérico |  | Processo de Emissão, gerado no campo procEmi do evento R-2050. | MFS17631 |
| Versão do Processo de Emissão | Alfanumérico |  | Versão do Processo de Emissão, gerado no campo procEmi do evento R-2050. | MFS17631 |
| Tipo de Inscrição Contribuinte | Alfanumérico |  | Tipo de Inscrição Contribuinte, gerado no campo tpInsc do evento R-2050. | MFS17631 |
| Número de Inscrição Contribuinte | Data | DD/MM/AAAA | Número de Inscrição Contribuinte, gerado no campo nrInsc do evento R-2050. | MFS17631 |
| Corpo do Relatório –  INFORMAÇÃO DA COMERCIALIZAÇÃO DE PRODUÇÃO /  Identificação do estabelecimento que comercializou a produção | Corpo do Relatório –  INFORMAÇÃO DA COMERCIALIZAÇÃO DE PRODUÇÃO /  Identificação do estabelecimento que comercializou a produção | Corpo do Relatório –  INFORMAÇÃO DA COMERCIALIZAÇÃO DE PRODUÇÃO /  Identificação do estabelecimento que comercializou a produção | Corpo do Relatório –  INFORMAÇÃO DA COMERCIALIZAÇÃO DE PRODUÇÃO /  Identificação do estabelecimento que comercializou a produção | Corpo do Relatório –  INFORMAÇÃO DA COMERCIALIZAÇÃO DE PRODUÇÃO /  Identificação do estabelecimento que comercializou a produção |
| Tipo Inscrição Estabelecimento | Alfanumérico |  | Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R-2050. | MFS17631 |
| Número Inscrição Estabelecimento | Alfanumérico |  | Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R-2050. | MFS17631 |
| Valor Total Receita Bruta Estabelecimento | Numérico | Default: 0,000 | Valor Total Receita Bruta Estabelecimento (VLR_PRODUTO da SAFX07, menos as deduções informadas no campo ‘Valor da Receita Bruta’ da tela Lançamento de Deduções da Comercialização da Produção por Produtor Rural PJ/Agroindústria se houver), gerado no campo vlrRecBrutaTotal do evento R-2050. | MFS17631 |
| Valor da Contribuição Previdenciária | Numérico | Default: 0,000 | Valor da Contribuição Previdenciária (VLR_CONTRIB_PREV da SAFX07, menos as deduções informadas no campo ‘Valor da Contribuição Previdenciária’ da tela Lançamento de Deduções da Comercialização da Produção por Produtor Rural PJ/Agroindústria se houver), gerado no campo vlrCPApur do evento R-2050. | MFS17631 |
| Valor da Contribuição Previdenciária GILRAT | Numérico | Default: 0,000 | Valor da Contribuição Previdenciária GILRAT (VLR_GILRAT da SAFX07, menos as deduções informadas no campo ‘Valor do GILRAT’ da tela Lançamento de Deduções da Comercialização da Produção por Produtor Rural PJ/Agroindústria se houver), gerado no campo vlrRatApur do evento R-2050. | MFS17631 |
| Valor da Contribuição para o SENAR | Numérico | Default: 0,000 | Valor da Contribuição para o SENAR  (VLR_CONTRIB_SENAR da SAFX07, menos as deduções informadas no campo ‘Valor do SENAR’ da tela Lançamento de Deduções da Comercialização da Produção por Produtor Rural PJ/Agroindústria se houver), gerado no campo vlrSenarApur do evento R-2050. | MFS17631 |
| Valor Total da Contribuição Previdenciária com exigibilidade suspensa | Numérico | Default: 0,000 | Valor Total da Contribuição Previdenciária com exigibilidade suspensa (VLR_PREV_EXIG_SUSP da SAFX263), gerado no campo vlrCPSuspTotal do evento R-2050. | MFS17631 |
| Valor Total da Contribuição Gilrat com exigibilidade suspensa | Numérico | Default: 0,000 | Valor Total da Contribuição Gilrat com exigibilidade suspensa (VLR_GILRAT_EXIG_SUSP da SAFX263), gerado no campo vlrRatSuspTotal do evento R-2050. | MFS17631 |
| Valor Total da Contribuição para o Senar com exigibilidade suspensa | Numérico | Default: 0,000 | Valor Total da Contribuição para o Senar com exigibilidade suspensa (VLR_SENAR_EXIG_SUSP da SAFX263), gerado no campo vlrSenarSuspTotal do evento R-2050. | MFS17631 |
| Corpo do Relatório – VALOR TOTAL DA RECEITA BRUTA POR TIPO DE COMERCIALIZAÇÃO | Corpo do Relatório – VALOR TOTAL DA RECEITA BRUTA POR TIPO DE COMERCIALIZAÇÃO | Corpo do Relatório – VALOR TOTAL DA RECEITA BRUTA POR TIPO DE COMERCIALIZAÇÃO | Corpo do Relatório – VALOR TOTAL DA RECEITA BRUTA POR TIPO DE COMERCIALIZAÇÃO | Corpo do Relatório – VALOR TOTAL DA RECEITA BRUTA POR TIPO DE COMERCIALIZAÇÃO |
| Indicativo de Comercialização | Alfanumérico |  | Indicativo de Comercialização (IND_TIPO_AQUIS da SAFX07 +  Descrição correspondendo conforme abaixo), gerado no campo indCom do evento R-2050.  Descrição correspondente a cada código:  1 - Aquisição da Produção de Prod. Rural PF ou segurado especial/Comercialização da Produção por Prod. Rural PJ/Agroindústria; 8 - Comercialização da Produção para Entidade inscrita no PAA; 9 - Comercialização da Produção no Mercado Externo. | MFS17631 |
| Valor Total da Comercialização | Numérico | Default: 0,000 | Valor Total da Comercialização (VLR_PRODUTO da SAFX07, menos as deduções informadas no campo ‘Valor da Receita Bruta’ da tela Lançamento de Deduções da Comercialização da Produção por Produtor Rural PJ/Agroindústria se houver), gerado no campo vlrRecBruta do evento R-2050. | MFS17631 |
