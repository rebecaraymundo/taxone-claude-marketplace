# MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2040_Analitico

> Fonte: MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2040_Analitico.docx






THOMSON REUTERS

Módulo EFD - REINF
Relatório de Conferência do Evento R-2040 - Analítico

Localização: Menu SPED, Módulo: EFD - REINF, item de menu Relatórios  Conferência dos Eventos  R-2040



DOCUMENTO DE REQUISITO


Sumário

1.	REGRAS DOS CAMPOS	3
2.	REGRAS DE GERAÇÃO DO RELATÓRIO	4
2.1.	Layout do Relatório	9

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
-Estabelecimento = estabelecimento informado em tela


Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a mensagem “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no relatório.

Regra de processamento:

Para cada estabelecimento selecionado em tela será gerado um relatório.

Serão recuperadas as informações do evento R-2050 de acordo com a regra de seleção, todas as informações para a Empresa e Estabelecimento de acordo com o período informado. Relatório demonstrará as informações por Estabelecimento, CNPJ Associação Desportiva. Será recuperado sempre a última ocorrência do evento R-2050 por tipo de número de inscrição do contribuinte.



Ordenação:
Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

- Empresa
- Estabelecimento

Segue regras do preenchimento dos dados no relatório:









### Layout do Relatório






| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS17630 | Lara Aline | Alteração do Modulo REINF para criação de um relatório de conferência do evento R-2040. Novo relatório  “Relatório de Conferência do Evento R-2040”. | 26/06/2018 (criação do documento) |
| MFS21968 | Eduardo Cruz | Inclusão dos campos: ID Evento, Data Evento, Nº Recibo, Tipo Arquivo | 20/02/2019 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Tipo | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções:  - Analítico - Sintético | MFS17630 |
| Período | Data | S | S | Formato: MM/AAAA  Default: Habilitado | Local para digitação do período inicial e final de referência da geração do relatório, no formato de DD/MM/AAAA.  Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para a criação do relatório. | MFS17630 |
| Tipo de Ambiente | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de ambiente entre as opções:  - Produção Restrita - Produção | MFS17630 |
| Geração Multiempresa | CheckBox | S | S | Default: não selecionado | Quando o usuário selecionar esta opção, será exibido no campo Estabelecimento, todas as empresas, contendo o código da empresa, código e a razão social de cada estabelecimento. | MFS17630 |
| Estabelecimentos | CheckBox | S | S | Default: não selecionado | Este campo exibe todos os estabelecimentos da empresa que acessou o módulo do EFD-Reinf.   A partir do parâmetro “Geração Multiempresa”, a lista passou a funcionar da seguinte forma:  - Caso o parâmetro “Geração Multiempresa” estiver desmarcado: Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento, somente da empresa que acessou o módulo. XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento).       - Caso o parâmetro “Geração Multiempresa” estiver marcado: Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento, mas neste caso serão mostradas todas as empresas: XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento)         Obs: No caso da geração multiempresa, as regras da geração do relatório não se modificam. A diferença é apenas na chamada, já que na lista de estabelecimentos para geração do relatório existirão estabelecimentos de empresas distintas.  O usuário deverá escolher obrigatoriamente ao menos um estabelecimento para a geração do relatório.  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento deve ser Selecionado”  Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”. | MFS17630 |


| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Empresa | Texto |  | Razão social da empresa. | MFS17630 |
| Data | Data | DD/MM/AAAA às HH:MM:SS hs | Data de emissão e hora do relatório | MFS17630 |
| Página | Numérico |  | Número da página sequencial do relatório | MFS17630 |
| Título | Texto |  | Título do relatório: “Relatório de Conferência do Evento R-2040 - Analítico” | MFS17630 |
| Período | Data | Formato: MM/AAAA | Deverá ser exibido o período informado em tela. | MFS17630 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Estabelecimento | Texto |  | Estabelecimento informado em tela | MFS17630 |
| ID Evento | Texto |  | Campo ID_EVENTO gravado na tabela REINF_PGER_R2040_OC | MFS21968 |
| Data Evento | Data | Formato: DD/MM/YYYY HH:MM:SS | Campo DAT_OCORRENCIA gravado na tabela REINF_PGER_R2040_OC | MFS21968 |
| Nº Recibo | Texto |  | Campo Num_recibo gravado na tabela REINF_PGER_R2040_OC | MFS21968 |
| Tipo Arquivo | Texto |  | Campo IND_OPER gravado na tabela REINF_PGER_R2040_OC | MFS21968 |
| Tipo Inscrição Estabelecimento | Alfanumérico |  | Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R-2040. | MFS17630 |
| Número Inscrição Estabelecimento | Alfanumérico |  | Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R-2040. | MFS17630 |
| CNPJ Associação Desportiva | Alfanumérico |  | CNPJ Associação Desportiva, gerado no campo cnpjAssocDesp do evento R-2040. | MFS17630 |
| Corpo do Relatório – DETALHAMENTO DOS RECURSOS REPASSADOS A ASSOCIAÇÃO DESPORTIVA | Corpo do Relatório – DETALHAMENTO DOS RECURSOS REPASSADOS A ASSOCIAÇÃO DESPORTIVA | Corpo do Relatório – DETALHAMENTO DOS RECURSOS REPASSADOS A ASSOCIAÇÃO DESPORTIVA | Corpo do Relatório – DETALHAMENTO DOS RECURSOS REPASSADOS A ASSOCIAÇÃO DESPORTIVA | Corpo do Relatório – DETALHAMENTO DOS RECURSOS REPASSADOS A ASSOCIAÇÃO DESPORTIVA |
| Tipo de Repasse | Alfanumérico |  | Tipo de Repasse (campo “Tipo de Repasse” da Tela de Identificador do Tipo de Repasse por Código de Serviço ou da tela Identificador do Tipo de Repasse por Código de Operação), gerado no campo tpRepasse do evento R-2040 | MFS17630 |
| Descrição Recurso | Alfanumérico |  | Descrição Recurso (descrição conforme campo “Tipo de Repasse” da Tela de Identificador do Tipo de Repasse por Código de Serviço ou da tela Identificador do Tipo de Repasse por Código de Operação), gerado no campo descRecurso do evento R-2040.  Conforme abaixo:  1 - 'Patrocínio'; 2 - 'Lic. marcas símbolos'; 3 - ‘Publicidade'; 4 - 'Propaganda'; 5 - 'Transmite espetáculo'; | MFS17630 |
| Valor Bruto Repasse Efetuado | Numérico | Default: 0,000 | Valor Bruto Repasse Efetuado (VLR_TOT da SAFX09 ou VLR_BRUTO da SAFX03), gerado no campo vlrBruto do evento R-2040. | MFS17630 |
| Valor Retenção Contribuição Previdenciária | Numérico | Default: 0,000 | Valor Retenção Contribuição Previdenciária (VLR_INSS_RETIDO SAFX09 ou VLR_RET da SAFX03), gerado no campo vlrRetApur do evento R-2040. | MFS17630 |
| Corpo do Relatório – Informações de processos relacionados a não retenção de contribuição previdenciária | Corpo do Relatório – Informações de processos relacionados a não retenção de contribuição previdenciária | Corpo do Relatório – Informações de processos relacionados a não retenção de contribuição previdenciária | Corpo do Relatório – Informações de processos relacionados a não retenção de contribuição previdenciária | Corpo do Relatório – Informações de processos relacionados a não retenção de contribuição previdenciária |
| Tipo de Processo | Alfanumérico |  | Tipo de Processo (IND_TP_PROC_ADJ_PRINC da SAFX09 ou IND_TP_PROC_ADJ_PRINC da SAFX03) gerado no campo tpProc do evento R-2040. | MFS17630 |
| Número Processo | Alfanumérico |  | Número Processo (NUM_PROC_ADJ_PRINC da SAFX09 ou NUM_PROC_ADJ_PRINC da SAFX03) gerado no campo nrProc do evento R-2040. | MFS17630 |
| Código Suspenção | Alfanumérico |  | Código Suspenção (COD_SUSP_PRINC da SAFX09 ou COD_SUSP da SAFX03) gerado no campo codSusp do evento R-2040. | MFS17630 |
| Valor Não Contribuição Previdenciária Principal | Numérico | Default: 0,000 | Valor Não Contribuição Previdenciária Principal (VLR_N_RET_PRINC da SAFX09 ou VLR_N_RET da SAFX03), gerado no campo vlrNRet do evento R-2040. | MFS17630 |
