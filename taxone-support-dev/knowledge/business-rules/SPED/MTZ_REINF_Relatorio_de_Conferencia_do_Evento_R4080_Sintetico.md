# MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R4080_Sintetico

> Fonte: MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R4080_Sintetico.docx






THOMSON REUTERS

Módulo EFD - REINF
Relatório de Conferência do Evento – Família 4000 - (R-4080 Sintético)

Localização: Menu SPED, Módulo: EFD - REINF, item de menu Relatórios  Conferência dos Eventos  Família 4000



DOCUMENTO DE REQUISITO

Sumário

1.	REGRAS DOS CAMPOS	3
2.	REGRAS DE GERAÇÃO DO RELATÓRIO	6
2.1.	Layout do Relatório	11

## REGRAS DOS CAMPOS


Localização da tela: Menu: SPED, Módulo: EFD - REINF, item de menu Relatórios > Conferência dos Eventos  > Família 4000 >
Título da tela: Relatório de Conferência dos Eventos – Família 4000

As regras da tela, estão disponíveis no documento MTZ_REINF_Tela_Relatorio_de_Conferencia_do_Evento_Familia4000.docx, link:

https://trten.sharepoint.com/sites/REQ_MTZ/Mastersaf%20DW%20TaxOne/Documento_Matriz/SPED/EFD-Reinf/Relatorios/Conferencia_dos_Eventos/Familia_4000/MTZ_REINF_Tela_Relatorio_de_Conferencia_do_Evento_Familia4000.docx?web=1











## REGRAS DE GERAÇÃO DO RELATÓRIO


Regra Geral:

[MFS626907] Retirar a opção de “salvar como”.  O relatório passará a ter as opções de salvar em excel ou em PDF

Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.

Origem das informações para geração:

Para geração deste relatório, serão consideradas as informações da seguinte origem:

Evento R-4080 (Cadastro do Estabelecimento, SAFX283, SAFX284).

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
Serão recuperadas as informações do evento R-4080 de acordo com a regra de seleção, todas as informações para a Empresa e Estabelecimento de acordo com o período informado. Relatório demonstrará as informações por Estabelecimento, Natureza de Rendimento.


Ordenação:
Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

- Empresa
- Estabelecimento
- Fonte Pagadora
- Natureza do Rendimento


Segue regras do preenchimento dos dados no relatório:





### Layout do Relatório


A partir da Versão 2.1.2 do REINF


= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ===============================
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                           							   Pág.: 999999
Data: 99/99/9999 às HH:MM:SS  hs

Relatório de Conferência do Evento R-4080 – Sintético
Período: 99/9999
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ================================
Estabelecimento: XXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
_____________________________________________________________________________________________________________________________
Informação de Identificação do Evento / Contribuinte
_____________________________________________________________________________________________________________________________

Tipo Arquivo: XXXXXXXXXXXXXXX 	    N. Recibo: XXXXXXXXXXXXXXXXXXX                           Tipo Amb. : XXXXXXXXX
Processo de Emissão: X-XXXXXX                 Versão do Processo de Emissão: XXXXXXXX

Tipo Inscrição Estabelecimento: X-XXXXXXXXXXXX                  	Número Inscrição Estabelecimento: XXXXX



| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-79907 | Alessandra Cristina Navatta | Criação de um relatório de conferência do evento R-4080 (sintético). Relatórios  “Conferência dos Eventos R-4080”. | 18/04/2022 |
| MFS-594004 | Alessandra Cristina Navatta | Criada tela única, para a geração dos relatórios de conferência da família 4000.  Ajustada a informação do layout, a partir da versão 2.1.2 (apenas ajuste em documentação) | 21/12/2023 |
| MFS- 620025 e MFS- 620042 | Alessandra Cristina Navatta | Retirar a coluna ‘Observações’ do agrupamento ‘Identificação do Rendimento’ | 12/03/2024 |
| MFS-627081 | Rosemeire Santos | Inclusão da coluna de status no relatório. Foi necessário incluir essa coluna no relatório, que não está prevista no layout do evento, para evitar duplicidade de dados na conferência dos dados (formato Excel). | 03/04/2024 |
| MFS626907 | Andréa Rocha | Retirada a opção de “salvar como” da geração do relatório. | 20/05/2024 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período | Data | S | S | Formato: MM/AAAA  Default: Habilitado | Local para digitação do período inicial e final de referência da geração do relatório, no formato de DD/MM/AAAA.  Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para a criação do relatório. | MFS-79907 |
| Versão | Texto | S | S | Default: Versão atual | Este campo exibe as versões de layout do Reinf. A partir da versão 2.1.1 | MFS-79907 |
| Tipo do Relatório | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções:  - Analítico - Sintético | MFS-79907 |
| Tipo de Ambiente | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de ambiente entre as opções:  - Produção Restrita - Produção | MFS-79907 |
| Geração Multiempresa | CheckBox | S | S | Default: não selecionado | Quando o usuário selecionar esta opção, será exibido no campo Estabelecimento, os estabelecimentos de todas as empresas que o usuário tem acesso e que geraram o evento. Se o parâmetro estiver desmarcado, apenas os estabelecimentos da empresa logada que geraram o evento serão demonstrados. | MFS-79907 |
| Estabelecimentos | CheckBox | S | S | Default: não selecionado | - Caso o parâmetro “Geração Multiempresa” estiver desmarcado: Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento, somente da empresa que acessou o módulo. XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento).       - Caso o parâmetro “Geração Multiempresa” estiver marcado: Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento, mas neste caso serão mostradas todas as empresas: XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento)         Obs: No caso da geração multiempresa, as regras da geração do relatório não se modificam. A diferença é apenas na chamada, já que na lista de estabelecimentos para geração do relatório existirão estabelecimentos de empresas distintas.  O usuário deverá escolher obrigatoriamente ao menos um estabelecimento para a geração do relatório.  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento deve ser Selecionado”  Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”. | MFS-79907 |


| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Empresa | Texto |  | Razão social da empresa. | MFS-79907 |
| Página | Numérico |  | Número da página sequencial do relatório | MFS-79907 |
| Data | Data | DD/MM/AAAA às HH:MM:SS hs | Data de emissão e hora do relatório | MFS-79907 |
| Título | Texto |  | Título do relatório: “Relatório de Conferência do Evento R-4080 - Sintético” | MFS-79907 |
| Período | Data | Formato: MM/AAAA | Deverá ser exibido o período informado em tela. | MFS-79907 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Estabelecimento | Texto |  | Estabelecimento informado em tela | MFS-79907 |
| Informação de Identificação do Evento / Contribuinte | Informação de Identificação do Evento / Contribuinte | Informação de Identificação do Evento / Contribuinte | Informação de Identificação do Evento / Contribuinte | Informação de Identificação do Evento / Contribuinte |
| Tipo Arquivo | Texto |  | Campo IND_OPER gravado na tabela REINF_PGER_R4080_OC | MFS-79907 |
| Status | Texto | Código-Descrição | Campo IND_STATUS gravado na tabela REINF_PGER_R4080_OC | MFS-627081 |
| Nº Recibo | Texto |  | Campo Num_recibo gravado na tabela REINF_PGER_R4080_OC | MFS-79907 |
| Tipo do Amb. | Texto |  | Tipo do ambiente, gerado no evento R-4080. | MFS-79907 |
| Processo de Emissão | Texto |  | Processo de Emissão, gerado no evento R-4080. | MFS-79907 |
| Versão do Processo de Emissão | Texto |  | Versão do Processo de Emissão, gerado no evento R-4080. | MFS-79907 |
| Tipo de Inscrição Estabelecimento | Alfanumérico |  | Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R-4080. | MFS-79907 |
| Número Inscrição Estabelecimento | Alfanumérico |  | Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R-4080. | MFS-79907 |
| Corpo do Relatório – Identificação da Fonte Pagadora do Rendimento | Corpo do Relatório – Identificação da Fonte Pagadora do Rendimento | Corpo do Relatório – Identificação da Fonte Pagadora do Rendimento | Corpo do Relatório – Identificação da Fonte Pagadora do Rendimento | Corpo do Relatório – Identificação da Fonte Pagadora do Rendimento |
| CNPJ da Fonte Pagadora | Alfanumérico |  | CNPJ da fonte pagadora do rendimento | MFS-79907 |
| Corpo do Relatório – Identificação do Rendimento  Esta parte do relatório demonstra a natureza do rendimento | Corpo do Relatório – Identificação do Rendimento  Esta parte do relatório demonstra a natureza do rendimento | Corpo do Relatório – Identificação do Rendimento  Esta parte do relatório demonstra a natureza do rendimento | Corpo do Relatório – Identificação do Rendimento  Esta parte do relatório demonstra a natureza do rendimento | Corpo do Relatório – Identificação do Rendimento  Esta parte do relatório demonstra a natureza do rendimento |
| Natureza do Rendimento | Texto |  | Natureza do Rendimento, vinculado ao evento R-4080.  Valores Válidos: 20001; 20002; 20003; 20004; 20005; 20006; 20007; 20008; 20009; 20010 | MFS-79907 |
| [Exclusão MFS- 620025 e MFS- 620042] Observações | Texto |  | Observações | MFS-79907 MFS- 620025 e MFS- 620042 |
| Corpo do Relatório – Totais do Recebimento do Rendimento | Corpo do Relatório – Totais do Recebimento do Rendimento | Corpo do Relatório – Totais do Recebimento do Rendimento | Corpo do Relatório – Totais do Recebimento do Rendimento | Corpo do Relatório – Totais do Recebimento do Rendimento |
| Valor Bruto | Numérico | 0,00 | Neste campo deve ser considerado o somatório do valor bruto do rendimento R-4080, independente da data do recebimento e sim do período de apuração. | MFS-79907 |
| Valor Base IR | Numérico | 0,00 | Neste campo deve ser considerado o somatório do valor da base IR do rendimento do evento R-4080, independente da data do recebimento sim do período de apuração. | MFS-79907 |
| Valor do Imposto de Renda Retido na Fonte | Numérico | 0,00 | Neste campo deve ser considerado o somatório do valor do imposto de renda retido na fonte de pagamento do rendimento evento R-4080, independente da data do recebimento e sim do período de apuração. | MFS-79907 |


| Identificação da Fonte Pagadora do Rendimento | Identificação da Fonte Pagadora do Rendimento | Identificação da Fonte Pagadora do Rendimento |
| --- | --- | --- |
| CNPJ da Fonte Pagadora: XX.XXX.XXX/XXXX-XX | CNPJ da Fonte Pagadora: XX.XXX.XXX/XXXX-XX | CNPJ da Fonte Pagadora: XX.XXX.XXX/XXXX-XX |
| Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento |
| Natureza do Rendimento: XXXXX | Natureza do Rendimento: XXXXX | Natureza do Rendimento: XXXXX |
| Totais do Recebimento do Rendimento | Totais do Recebimento do Rendimento | Totais do Recebimento do Rendimento |
| Valor Bruto | Valor Base IR | Valor do Imposto de Renda Retido na Fonte |
| 999.999.999.999,99 | 999.999.999.999,99 | 999.999.999.999,99 |
