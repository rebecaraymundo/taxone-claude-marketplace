# MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2050_Analitico

> Fonte: MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2050_Analitico.docx






THOMSON REUTERS

Módulo EFD - REINF
Relatório de Conferência do Evento R-2050 - Analítico

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

Evento R-2050 (SAFX07, SAFX263, Cadastro do Estabelecimento e tela “Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria”).
Tabela das Notas Fiscais que compõem os valores do R-2050 (REINF_PGER_R2050_NF);

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
Serão recuperadas as informações do evento R-2050 de acordo com a regra de seleção, todas as informações para a Empresa e Estabelecimento de acordo com o período informado. Relatório demonstrará as informações por Estabelecimento, Tipo de Comercialização, NFs e Processos. Será recuperado sempre a última ocorrência do evento R-2050 por tipo de número de inscrição do contribuinte.


Ordenação:
Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

- Empresa
- Estabelecimento
- Nota Fiscal

Segue regras do preenchimento dos dados no relatório:






















### Layout do Relatório



= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                    Data: 99/99/9999   Pág.: 999999
Relatório de Pagamento do Evento R-2050 – Analítico
Período: 99/9999
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

Estabelecimento: XXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ID Evento: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                                    Data Evento: 99/99/9999 99:99:99
N. Recibo: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                          Tipo Arquivo: XXXXXXXXXXXXXXXXXX
Tipo Inscrição Estabelecimento: X-XXXXXXXXXXXXXXXXXXX                                            Número Inscrição Estabelecimento: XXXXX






| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS17631 | Lara Aline | Alteração do Modulo REINF para criação de um relatório de conferência do evento R-2050. Novo relatório  “Relatório de Conferência do Evento R-2050”. | 21/05/2018 (criação do documento) |
| MFS18226 | Lara Aline | Inclusão do campo Tipo de Ambiente | 04/06/2018 |
| MFS21968 | Eduardo Cruz | Inclusão dos campos: ID Evento, Data Evento, Nº Recibo, Tipo Arquivo | 20/02/2019 |
| MFS20474 | Vânia Mattos | Inclusão de colunas no relatório, e linha de totalização dos valores por indicativo de comercialização | 06/06/2019 |
|  |  |  |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Tipo | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções:  - Analítico - Sintético | MFS17631 |
| Período | Data | S | S | Formato: MM/AAAA  Default: Habilitado | Local para digitação do período inicial e final de referencia da geração do relatório, no formato de DD/MM/AAAA.  Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para a criação do relatório. | MFS17631 |
| Tipo de Ambiente | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de ambiente entre as opções:  - Produção Restrita - Produção | MFS18226 |
| Geração Multiempresa | CheckBox | S | S | Default: não selecionado | Quando o usuário selecionar esta opção, será exibido no campo Estabelecimento, todas as empresas, contendo o código da empresa, código e a razão social de cada estabelecimento. | MFS17631 |
| Estabelecimentos | CheckBox | S | S | Default: não selecionado | Este campo exibe todos os estabelecimentos da empresa que acessou o módulo do EFD-Reinf.   A partir do parâmetro “Geração Multiempresa”, a lista passou a funcionar da seguinte forma:  - Caso o parâmetro “Geração Multiempresa” estiver desmarcado: Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento, somente da empresa que acessou o módulo. XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento).       - Caso o parâmetro “Geração Multiempresa” estiver marcado: Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento, mas neste caso serão mostradas todas as empresas: XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento)         Obs: No caso da geração multiempresa, as regras da geração do relatório não se modificam. A diferença é apenas na chamada, já que na lista de estabelecimentos para geração do relatório existirão estabelecimentos de empresas distintas.  O usuário deverá escolher obrigatoriamente ao menos um estabelecimento para a geração do relatório.  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento deve ser Selecionado”  Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”. | MFS17631 |


| Campo/Coluna | Tipo | Tipo | Tipo | Formato/Default | Regra | Regra | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Empresa | Texto | Texto | Texto |  | Razão social da empresa. | Razão social da empresa. | Razão social da empresa. | MFS17631 |
| Data | Data | Data | Data | DD/MM/AAAA às HH:MM:SS hs | Data de emissão e hora do relatório | Data de emissão e hora do relatório | Data de emissão e hora do relatório | MFS17631 |
| Página | Numérico | Numérico | Numérico |  | Número da página sequencial do relatório | Número da página sequencial do relatório | Número da página sequencial do relatório | MFS17631 |
| Título | Texto | Texto | Texto |  | Título do relatório: “Relatório de Conferência do Evento R-2050 - Analítico” | Título do relatório: “Relatório de Conferência do Evento R-2050 - Analítico” | Título do relatório: “Relatório de Conferência do Evento R-2050 - Analítico” | MFS17631 |
| Período | Data | Data | Data | Formato: MM/AAAA | Deverá ser exibido o período informado em tela. | Deverá ser exibido o período informado em tela. | Deverá ser exibido o período informado em tela. | MFS17631 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Estabelecimento | Texto | Texto | Texto |  | Estabelecimento informado em tela | Estabelecimento informado em tela | Estabelecimento informado em tela | MFS17631 |
| ID Evento | Texto | Texto | Texto |  | Campo ID_EVENTO gravado na tabela REINF_PGER_R2050_OC | Campo ID_EVENTO gravado na tabela REINF_PGER_R2050_OC | Campo ID_EVENTO gravado na tabela REINF_PGER_R2050_OC | MFS21968 |
| Data Evento | Data | Data | Data | Formato: DD/MM/YYYY HH:MM:SS | Campo DAT_OCORRENCIA gravado na tabela REINF_PGER_R2050_OC | Campo DAT_OCORRENCIA gravado na tabela REINF_PGER_R2050_OC | Campo DAT_OCORRENCIA gravado na tabela REINF_PGER_R2050_OC | MFS21968 |
| Nº Recibo | Texto | Texto | Texto |  | Campo Num_recibo gravado na tabela REINF_PGER_R2050_OC | Campo Num_recibo gravado na tabela REINF_PGER_R2050_OC | Campo Num_recibo gravado na tabela REINF_PGER_R2050_OC | MFS21968 |
| Tipo Arquivo | Texto | Texto | Texto |  | Campo IND_OPER gravado na tabela REINF_PGER_R2050_OC | Campo IND_OPER gravado na tabela REINF_PGER_R2050_OC | Campo IND_OPER gravado na tabela REINF_PGER_R2050_OC | MFS21968 |
| Tipo Inscrição Estabelecimento | Alfanumérico | Alfanumérico | Alfanumérico |  | Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R-2050. | Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R-2050. | Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R-2050. | MFS17631 |
| Número Inscrição Estabelecimento | Alfanumérico | Alfanumérico | Alfanumérico |  | Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R-2050. | Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R-2050. | Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R-2050. | MFS17631 |
| Corpo do Relatório – Detalhamento de Nota Fiscal por Tipo de Comercialização  Esta parte do relatório demonstra as notas fiscais utilizadas na geração do evento R-2050, agrupadas por Indicativo de Comercialização.  As informações são recuperadas da tabela REINF_PGER_R2050_NF, tabela alimentada durante a geração do evento R-2050. | Corpo do Relatório – Detalhamento de Nota Fiscal por Tipo de Comercialização  Esta parte do relatório demonstra as notas fiscais utilizadas na geração do evento R-2050, agrupadas por Indicativo de Comercialização.  As informações são recuperadas da tabela REINF_PGER_R2050_NF, tabela alimentada durante a geração do evento R-2050. | Corpo do Relatório – Detalhamento de Nota Fiscal por Tipo de Comercialização  Esta parte do relatório demonstra as notas fiscais utilizadas na geração do evento R-2050, agrupadas por Indicativo de Comercialização.  As informações são recuperadas da tabela REINF_PGER_R2050_NF, tabela alimentada durante a geração do evento R-2050. | Corpo do Relatório – Detalhamento de Nota Fiscal por Tipo de Comercialização  Esta parte do relatório demonstra as notas fiscais utilizadas na geração do evento R-2050, agrupadas por Indicativo de Comercialização.  As informações são recuperadas da tabela REINF_PGER_R2050_NF, tabela alimentada durante a geração do evento R-2050. | Corpo do Relatório – Detalhamento de Nota Fiscal por Tipo de Comercialização  Esta parte do relatório demonstra as notas fiscais utilizadas na geração do evento R-2050, agrupadas por Indicativo de Comercialização.  As informações são recuperadas da tabela REINF_PGER_R2050_NF, tabela alimentada durante a geração do evento R-2050. | Corpo do Relatório – Detalhamento de Nota Fiscal por Tipo de Comercialização  Esta parte do relatório demonstra as notas fiscais utilizadas na geração do evento R-2050, agrupadas por Indicativo de Comercialização.  As informações são recuperadas da tabela REINF_PGER_R2050_NF, tabela alimentada durante a geração do evento R-2050. | Corpo do Relatório – Detalhamento de Nota Fiscal por Tipo de Comercialização  Esta parte do relatório demonstra as notas fiscais utilizadas na geração do evento R-2050, agrupadas por Indicativo de Comercialização.  As informações são recuperadas da tabela REINF_PGER_R2050_NF, tabela alimentada durante a geração do evento R-2050. | Corpo do Relatório – Detalhamento de Nota Fiscal por Tipo de Comercialização  Esta parte do relatório demonstra as notas fiscais utilizadas na geração do evento R-2050, agrupadas por Indicativo de Comercialização.  As informações são recuperadas da tabela REINF_PGER_R2050_NF, tabela alimentada durante a geração do evento R-2050. | Corpo do Relatório – Detalhamento de Nota Fiscal por Tipo de Comercialização  Esta parte do relatório demonstra as notas fiscais utilizadas na geração do evento R-2050, agrupadas por Indicativo de Comercialização.  As informações são recuperadas da tabela REINF_PGER_R2050_NF, tabela alimentada durante a geração do evento R-2050. |
| Indicativo de Comercialização | Alfanumérico | Alfanumérico | Alfanumérico |  | Indicativo de Comercialização (IND_TIPO_AQUIS da SAFX07 +  Descrição correspondendo conforme abaixo), gerado no campo indCom do evento R-2050.  Descrição correspondente a cada código:  1 - Aquisição da Produção de Prod. Rural PF ou segurado especial/Comercialização da Produção por Prod. Rural PJ/Agroindústria; 8 - Comercialização da Produção para Entidade inscrita no PAA; 9 - Comercialização da Produção no Mercado Externo. | Indicativo de Comercialização (IND_TIPO_AQUIS da SAFX07 +  Descrição correspondendo conforme abaixo), gerado no campo indCom do evento R-2050.  Descrição correspondente a cada código:  1 - Aquisição da Produção de Prod. Rural PF ou segurado especial/Comercialização da Produção por Prod. Rural PJ/Agroindústria; 8 - Comercialização da Produção para Entidade inscrita no PAA; 9 - Comercialização da Produção no Mercado Externo. | Indicativo de Comercialização (IND_TIPO_AQUIS da SAFX07 +  Descrição correspondendo conforme abaixo), gerado no campo indCom do evento R-2050.  Descrição correspondente a cada código:  1 - Aquisição da Produção de Prod. Rural PF ou segurado especial/Comercialização da Produção por Prod. Rural PJ/Agroindústria; 8 - Comercialização da Produção para Entidade inscrita no PAA; 9 - Comercialização da Produção no Mercado Externo. | MFS17631 |
| N° Nota Fiscal | Alfanumérico | Alfanumérico | Alfanumérico |  | N° Nota Fiscal (NUM_DOCFIS) SAFX07 gerado no campo numDocto vinculado ao evento R-2050. | N° Nota Fiscal (NUM_DOCFIS) SAFX07 gerado no campo numDocto vinculado ao evento R-2050. | N° Nota Fiscal (NUM_DOCFIS) SAFX07 gerado no campo numDocto vinculado ao evento R-2050. | MFS17631 |
| Série | Alfanumérico | Alfanumérico | Alfanumérico |  | Série da Nota Fiscal (SERIE_DOCFIS) SAFX07, gerado no campo serie vinculado ao evento R-2050. | Série da Nota Fiscal (SERIE_DOCFIS) SAFX07, gerado no campo serie vinculado ao evento R-2050. | Série da Nota Fiscal (SERIE_DOCFIS) SAFX07, gerado no campo serie vinculado ao evento R-2050. | MFS17631 |
| Data de Emissão | Data | Data | Data | DD/MM/AAAA | Data de Emissão da Nota Fiscal (DATA_EMISSAO) SAFX07 vinculado ao evento R-2050. | Data de Emissão da Nota Fiscal (DATA_EMISSAO) SAFX07 vinculado ao evento R-2050. | Data de Emissão da Nota Fiscal (DATA_EMISSAO) SAFX07 vinculado ao evento R-2050. | MFS17631 |
| Valor Bruto | Numérico | Numérico | Numérico | Default: 0,000 | Valor Bruto (VLR_BRUTO da SAFX07), gerado no campo vlrBruto vinculado ao evento R-2050.  Obs: Nesse campo deverá gerar o valor bruto da nota, ou seja, será recuperada o valor de todos os itens da nota, mesmo se o usuário estiver com o parâmetro “Desconsiderar NFs sem Valor de Retenção informado” selecionado nos Dados Iniciais. Será considerado o valor bruto de todos os itens da nota, mesmo os itens que foram desconsiderados na geração com o parâmetro “Desconsiderar NFs sem Valor de Retenção informado”. | Valor Bruto (VLR_BRUTO da SAFX07), gerado no campo vlrBruto vinculado ao evento R-2050.  Obs: Nesse campo deverá gerar o valor bruto da nota, ou seja, será recuperada o valor de todos os itens da nota, mesmo se o usuário estiver com o parâmetro “Desconsiderar NFs sem Valor de Retenção informado” selecionado nos Dados Iniciais. Será considerado o valor bruto de todos os itens da nota, mesmo os itens que foram desconsiderados na geração com o parâmetro “Desconsiderar NFs sem Valor de Retenção informado”. | Valor Bruto (VLR_BRUTO da SAFX07), gerado no campo vlrBruto vinculado ao evento R-2050.  Obs: Nesse campo deverá gerar o valor bruto da nota, ou seja, será recuperada o valor de todos os itens da nota, mesmo se o usuário estiver com o parâmetro “Desconsiderar NFs sem Valor de Retenção informado” selecionado nos Dados Iniciais. Será considerado o valor bruto de todos os itens da nota, mesmo os itens que foram desconsiderados na geração com o parâmetro “Desconsiderar NFs sem Valor de Retenção informado”. | MFS17631 |
| Contrib. Previdenciária  (Coluna incluída na MFS20474) | Numérico | Numérico | Numérico |  | Campo “Valor da Contribuição Previdenciária” da nota fiscal (VLR_CONTRIB_PREV da SAFX07). | Campo “Valor da Contribuição Previdenciária” da nota fiscal (VLR_CONTRIB_PREV da SAFX07). | Campo “Valor da Contribuição Previdenciária” da nota fiscal (VLR_CONTRIB_PREV da SAFX07). | MFS20474 |
| GILRAT  (Coluna incluída na MFS20474) | Numérico | Numérico | Numérico |  | Campo “Valor da GILRAT” da nota fiscal (VLR_GILRAT da SAFX07). | Campo “Valor da GILRAT” da nota fiscal (VLR_GILRAT da SAFX07). | Campo “Valor da GILRAT” da nota fiscal (VLR_GILRAT da SAFX07). | MFS20474 |
| SENAR  (Coluna incluída na MFS20474) | Numérico | Numérico | Numérico |  | Campo “Valor da Contribuição destinada ao SENAR” da nota fiscal (VLR_CONTRIB_SENAR da SAFX07). | Campo “Valor da Contribuição destinada ao SENAR” da nota fiscal (VLR_CONTRIB_SENAR da SAFX07). | Campo “Valor da Contribuição destinada ao SENAR” da nota fiscal (VLR_CONTRIB_SENAR da SAFX07). | MFS20474 |
| Corpo do Relatório – Linha de total das notas fiscais por Indicativo de Comercialização | Corpo do Relatório – Linha de total das notas fiscais por Indicativo de Comercialização | Corpo do Relatório – Linha de total das notas fiscais por Indicativo de Comercialização | Corpo do Relatório – Linha de total das notas fiscais por Indicativo de Comercialização | Corpo do Relatório – Linha de total das notas fiscais por Indicativo de Comercialização | Corpo do Relatório – Linha de total das notas fiscais por Indicativo de Comercialização | Corpo do Relatório – Linha de total das notas fiscais por Indicativo de Comercialização | Corpo do Relatório – Linha de total das notas fiscais por Indicativo de Comercialização | Corpo do Relatório – Linha de total das notas fiscais por Indicativo de Comercialização |
| Totais Comercialização  (Linha incluída na MFS20474) | Totais Comercialização  (Linha incluída na MFS20474) | Numérico |  |  |  | Totalização das colunas de valor para cada indicativo de comercialização:  - Valor Bruto - Contrib. Previdenciária - GILRAT - SENAR | MFS20474 | MFS20474 |
| Corpo do Relatório – Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte | Corpo do Relatório – Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte | Corpo do Relatório – Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte | Corpo do Relatório – Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte | Corpo do Relatório – Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte | Corpo do Relatório – Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte | Corpo do Relatório – Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte | Corpo do Relatório – Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte | Corpo do Relatório – Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte |
| Tipo de Processo | Alfanumérico | Alfanumérico | Alfanumérico |  | Tipo de Processo (IND_TIP_PROC) SAFX263 correspondente gerado no campo tpProc do evento R-2050. | Tipo de Processo (IND_TIP_PROC) SAFX263 correspondente gerado no campo tpProc do evento R-2050. | Tipo de Processo (IND_TIP_PROC) SAFX263 correspondente gerado no campo tpProc do evento R-2050. | MFS17631 |
| Número Processo | Alfanumérico | Alfanumérico | Alfanumérico |  | Número Processo (NUM_PROC) SAFX263 correspondente gerado no campo nrProc do evento R-2050. | Número Processo (NUM_PROC) SAFX263 correspondente gerado no campo nrProc do evento R-2050. | Número Processo (NUM_PROC) SAFX263 correspondente gerado no campo nrProc do evento R-2050. | MFS17631 |
| Código Suspenção | Alfanumérico | Alfanumérico | Alfanumérico |  | Código Suspenção (COD_SUSP) SAFX263 correspondente gerado no campo codSusp do evento R-2050. | Código Suspenção (COD_SUSP) SAFX263 correspondente gerado no campo codSusp do evento R-2050. | Código Suspenção (COD_SUSP) SAFX263 correspondente gerado no campo codSusp do evento R-2050. | MFS17631 |
| Valor CPRB Exigibilidade Suspensa | Numérico | Numérico | Numérico | Default: 0,000 | Valor CPRB Exigibilidade Suspensa (VLR_PREV_EXIG_SUSP) SAFX263, gerado no campo vlrCPSusp do  evento R-2050. | Valor CPRB Exigibilidade Suspensa (VLR_PREV_EXIG_SUSP) SAFX263, gerado no campo vlrCPSusp do  evento R-2050. | Valor CPRB Exigibilidade Suspensa (VLR_PREV_EXIG_SUSP) SAFX263, gerado no campo vlrCPSusp do  evento R-2050. | MFS17631 |
| Valor Contribuição Gilrat Exigibilidade Suspensa | Numérico | Numérico | Numérico | Default: 0,000 | Valor CPRB Exigibilidade Suspensa (VLR_GILRAT_EXIG_SUSP) SAFX263, gerado no campo vlrRatSusp do  evento R-2050. | Valor CPRB Exigibilidade Suspensa (VLR_GILRAT_EXIG_SUSP) SAFX263, gerado no campo vlrRatSusp do  evento R-2050. | Valor CPRB Exigibilidade Suspensa (VLR_GILRAT_EXIG_SUSP) SAFX263, gerado no campo vlrRatSusp do  evento R-2050. | MFS17631 |
| Valor Contribuição Senar Exigibilidade Suspensa | Numérico | Numérico | Numérico | Default: 0,000 | Valor CPRB Exigibilidade Suspensa (VLR_SENAR_EXIG_SUSP) SAFX263, gerado no campo vlrSenarSusp do  evento R-2050. | Valor CPRB Exigibilidade Suspensa (VLR_SENAR_EXIG_SUSP) SAFX263, gerado no campo vlrSenarSusp do  evento R-2050. | Valor CPRB Exigibilidade Suspensa (VLR_SENAR_EXIG_SUSP) SAFX263, gerado no campo vlrSenarSusp do  evento R-2050. | MFS17631 |


| Detalhamento de Nota Fiscal por Tipo de Comercialização | Detalhamento de Nota Fiscal por Tipo de Comercialização | Detalhamento de Nota Fiscal por Tipo de Comercialização | Detalhamento de Nota Fiscal por Tipo de Comercialização | Detalhamento de Nota Fiscal por Tipo de Comercialização | Detalhamento de Nota Fiscal por Tipo de Comercialização | Detalhamento de Nota Fiscal por Tipo de Comercialização |
| --- | --- | --- | --- | --- | --- | --- |
| Indicativo Comercialização: X - XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX | Indicativo Comercialização: X - XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX | Indicativo Comercialização: X - XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX | Indicativo Comercialização: X - XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX | Indicativo Comercialização: X - XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX | Indicativo Comercialização: X - XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX | Indicativo Comercialização: X - XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
| N. Nota Fiscal | Série | Data de Emissão | Valor Bruto | Contrib. Previdenciária | GILRAT | SENAR |
| xxxxxxxxxxxx | xxx | 99/99/9999 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 |
| xxxxxxxxxxxx | xxx | 99/99/9999 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 |
| xxxxxxxxxxxx | xxx | 99/99/9999 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 |
| Totais Comercialização: | Totais Comercialização: | Totais Comercialização: | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 |


| Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao usuário | Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao usuário | Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao usuário | Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao usuário | Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao usuário | Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao usuário |
| --- | --- | --- | --- | --- | --- |
| Tipo de Processo | Número Processo | Código Suspensão | Valor CPRB Exigibilidade Suspensa | Valor Contribuição Gilrat Exigibilidade Suspensa | Valor Contribuição Senar Exigibilidade Suspensa |
| x-xxxxxxxxx | xxxxxxxxxxxxx | xxxxxxxxxxxxxx | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 |
| x-xxxxxxxxx | xxxxxxxxxxxxx | xxxxxxxxxxxxx | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 |
| x-xxxxxxxxx | xxxxxxxxxxxxx | xxxxxxxxxxxxx | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 |
