# MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2055_Sintetico

> Fonte: MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2055_Sintetico.docx






THOMSON REUTERS

Módulo EFD - REINF
Relatório de Conferência do Evento R-2055 - Sintético

Localização: Menu SPED, Módulo: EFD - REINF, item de menu Relatórios  Conferência dos Eventos  R-2055



DOCUMENTO DE REQUISITO


Sumário

1.	REGRAS DOS CAMPOS	3
2.	REGRAS DE GERAÇÃO DO RELATÓRIO	6
2.1.	Layout do Relatório	11

## REGRAS DOS CAMPOS


Localização da tela: Menu: SPED, Módulo: EFD - REINF, item de menu Relatórios > Conferência dos Eventos > R-2055
Título da tela: Relatório de Conferência do Evento R-2055
























## REGRAS DE GERAÇÃO DO RELATÓRIO


Regra Geral:
Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.

Origem das informações para geração:
Para geração deste relatório, serão consideradas as informações da seguinte origem:

Evento R-2055 (SAFX07, SAFX63, Cadastro do Estabelecimento e tela Devoluções de Aquisição de Produtor Rural (R-2055)

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

Serão recuperadas as informações do evento R-2055 de acordo com a regra de seleção, todas as informações para a Empresa e Estabelecimento de acordo com o período informado. Relatório demonstrará as informações consolidadas por Estabelecimento, Produtor Rural, Tipo de Aquisição. Será recuperado sempre a última ocorrência do evento R-2055 por Tipo e Número de Inscrição do contribuinte. Relatório demostrará as informações consolidadas.




Ordenação:
Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

- Empresa
- Estabelecimento
- Produtor Rural

Segue regras do preenchimento dos dados no relatório:















### Layout do Relatório



= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ===================
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                              				Pág.: 999999
Data: 99/99/9999 às HH:MM:SS  hs

Relatório de Conferência do Evento R-2055 – Sintético
Período: 99/9999
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ===================


Estabelecimento: XXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
_______________________________________________________________________________________________________________
Informação de Identificação do Evento / Contribuinte
_______________________________________________________________________________________________________________

Tipo Arquivo: XXXXXXXXXXXXXXX N. Recibo: XXXXXXXXXXXXXXXXXXX                Tipo Amb. : XXXXXXXXX
Processo de Emissão: X-XXXXXX    Versão do Processo de Emissão: XXXXXXXX    Indicativo de Retificação do Evento S-1250: Não
Tipo Inscrição Estabelecimento: X-XXXXXXXXXXXX                  Número Inscrição Estabelecimento: XXXXX


































| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS58386 | Alessandra Cristina Navatta | Criação de um relatório de conferência do evento R-2055 (sintético). Relatórios  “Conferência dos Eventos R-2055”. | 17/03/2021 |
|  |  |  |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período | Data | S | S | Formato: MM/AAAA  Default: Habilitado | Local para digitação do período inicial e final de referência da geração do relatório, no formato de DD/MM/AAAA.  Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para a criação do relatório. | MFS58386 |
| Versão | Texto | S | S | Default: Versão atual | Este campo exibe as versões de layout do Reinf. A partir da versão 1.5.1 | MFS58386 |
| Tipo do Relatório | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções:  - Analítico - Sintético | MFS58386 |
| Tipo de Ambiente | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de ambiente entre as opções:  - Produção Restrita - Produção | MFS58386 |
| Geração Multiempresa | CheckBox | S | S | Default: não selecionado | Quando o usuário selecionar esta opção, será exibido no campo Estabelecimento, todas as empresas, contendo o código da empresa, código e a razão social de cada estabelecimento. | MFS58386 |
| Estabelecimentos | CheckBox | S | S | Default: não selecionado | Este campo exibe todos os estabelecimentos da empresa que acessou o módulo do EFD-Reinf.   A partir do parâmetro “Geração Multiempresa”, a lista passou a funcionar da seguinte forma:  - Caso o parâmetro “Geração Multiempresa” estiver desmarcado: Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento, somente da empresa que acessou o módulo. XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento).       - Caso o parâmetro “Geração Multiempresa” estiver marcado: Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento, mas neste caso serão mostradas todas as empresas: XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento)         Obs: No caso da geração multiempresa, as regras da geração do relatório não se modificam. A diferença é apenas na chamada, já que na lista de estabelecimentos para geração do relatório existirão estabelecimentos de empresas distintas.  O usuário deverá escolher obrigatoriamente ao menos um estabelecimento para a geração do relatório.  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento deve ser Selecionado”  Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”. | MFS58386 |


| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Empresa | Texto |  | Razão social da empresa. | MFS58386 |
| Página | Numérico |  | Número da página sequencial do relatório | MFS58386 |
| Data | Data | DD/MM/AAAA às HH:MM:SS hs | Data de emissão e hora do relatório | MFS58386 |
| Título | Texto |  | Título do relatório: “Relatório de Conferência do Evento R-2055 - Sintético” | MFS58386 |
| Período | Data | Formato: MM/AAAA | Deverá ser exibido o período informado em tela. | MFS58386 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Estabelecimento | Texto |  | Estabelecimento informado em tela | MFS58386 |
| Informação de Identificação do Evento / Contribuinte | Informação de Identificação do Evento / Contribuinte | Informação de Identificação do Evento / Contribuinte | Informação de Identificação do Evento / Contribuinte | Informação de Identificação do Evento / Contribuinte |
| Tipo Arquivo | Texto |  | Campo IND_OPER gravado na tabela REINF_PGER_R2055_OC | MFS58386 |
| Nº Recibo | Texto |  | Campo Num_recibo gravado na tabela REINF_PGER_R2055_OC | MFS58386 |
| Tipo do Amb. | Texto |  | Tipo do ambiente, gerado no evento R-2055. | MFS58386 |
| Processo de Emissão | Texto |  | Processo de Emissão, gerado no evento R-2055. | MFS58386 |
| Versão do Processo de Emissão | Texto |  | Versão do Processo de Emissão, gerado no evento R-2055. | MFS58386 |
| Indicativo de Retificação do Evento S-1250 | Texto |  | Indicativo de Retificação, gerado no evento R-2055. | MFS58386 |
| Tipo de Inscrição Estabelecimento | Alfanumérico |  | Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R-2055. | MFS58386 |
| Número Inscrição Estabelecimento | Alfanumérico |  | Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R-2055. | MFS58386 |
| Corpo do Relatório – Identificação do Produtor Rural | Corpo do Relatório – Identificação do Produtor Rural | Corpo do Relatório – Identificação do Produtor Rural | Corpo do Relatório – Identificação do Produtor Rural | Corpo do Relatório – Identificação do Produtor Rural |
| Tipo de Inscrição | Texto |  | Tipo de Inscrição:  Opções Válidas: 1 - CNPJ 2 - CPF | MFS58386 |
| Número de Inscrição | Texto |  | Número de Inscrição vinculado ao evento R-2055. | MFS58386 |
| Forma de Tributação da Contribuição Previdenciária | Texto |  | Indicador OpcCP vinculado ao evento R-2055 | MFS58386 |
| Corpo do Relatório – Total das Aquisições por Produtor Rural | Corpo do Relatório – Total das Aquisições por Produtor Rural | Corpo do Relatório – Total das Aquisições por Produtor Rural | Corpo do Relatório – Total das Aquisições por Produtor Rural | Corpo do Relatório – Total das Aquisições por Produtor Rural |
| Valor da Receita Bruta Total | Numérico | 0,00 | Valor vinculado ao evento R-2055.  Neste campo, deve ser constar o somatório do valor total das receitas do produtor (campo vlrBruto do evento R-2055), independente do indicador da aquisição. | MFS58386 |
| Valor da Contribuição Previdenciária | Numérico | 0,00 | Valor vinculado ao evento R-2055. Neste campo, deve ser constar o somatório do valor total da Contribuição Previdenciária do produtor (campo vlrCPDescPR do evento R-2055), independente do indicador da aquisição. | MFS58386 |
| Valor da Contribuição Previdenciária GILRAT | Numérico | 0,00 | Valor vinculado ao evento R-2055. Neste campo, deve ser constar o somatório do valor total da Contribuição Previdenciária GILRAT do produtor (campo vlrRatDescPR do evento R-2055)., independente do indicador da aquisição. | MFS58386 |
| Valor da Contribuição Previdenciária SENAR | Numérico | 0,00 | Valor vinculado ao evento R-2055. Neste campo, deve ser constar o somatório do valor total da Contribuição Previdenciária SENAR do produtor (campo vlrSenarDesc do evento R-2055), independente do indicador da aquisição. | MFS58386 |


| Identificação do Produtor Rural | Identificação do Produtor Rural | Identificação do Produtor Rural |
| --- | --- | --- |
| Tipo de Inscrição | Número de Inscrição | Forma de Tributação da Contribuição Previdenciária |
| X-XXXX | xxxxxxxxxxxx | xxx |


| Total das Aquisições por Produtor Rural | Total das Aquisições por Produtor Rural | Total das Aquisições por Produtor Rural | Total das Aquisições por Produtor Rural |
| --- | --- | --- | --- |
|  |  |  |  |
| Valor da Receita Bruta Total | Valor da Contribuição Previdenciária | Valor da Contribuição Previdenciária GILRAT | Valor da Contribuição Previdenciária SENAR |
| 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 |


|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |


|  |  |  |  |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
