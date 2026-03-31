# MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R4020_Sintetico

> Fonte: MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R4020_Sintetico.docx






THOMSON REUTERS

Módulo EFD - REINF
Relatório de Conferência do Evento – Família 4000 – (R-4020 Sintético)

Localização: Menu SPED, Módulo: EFD - REINF, item de menu Relatórios à Conferência dos Eventos à Família 4000



DOCUMENTO DE REQUISITO

Sumário

1.	REGRAS DOS CAMPOS	3
2.	REGRAS DE GERAÇÃO DO RELATÓRIO	6
2.1.	Layout do Relatório	12

## REGRAS DOS CAMPOS


Localização da tela: Menu: SPED, Módulo: EFD - REINF, item de menu Relatórios > Conferência dos Eventos > Família 4000 >
Título da tela: Relatório de Conferência dos Eventos – Família 4000

As regras da tela, estão disponíveis no documento MTZ_REINF_Tela_Relatorio_de_Conferencia_do_Evento_Familia4000.docx, link:

https://trten.sharepoint.com/sites/REQ_MTZ/Mastersaf%20DW%20TaxOne/Documento_Matriz/SPED/EFD-Reinf/Relatorios/Conferencia_dos_Eventos/Familia_4000/MTZ_REINF_Tela_Relatorio_de_Conferencia_do_Evento_Familia4000.docx?web=1


## REGRAS DE GERAÇÃO DO RELATÓRIO


Regra Geral:

[MFS626907] Retirar a opção de “salvar como”.  O relatório passará a ter as opções de salvar em excel ou em PDF

Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.

Origem das informações para geração:

Para geração deste relatório, serão consideradas as informações da seguinte origem:

Evento R-4020 (Cadastro do Estabelecimento, SAFX04, SAFX53, SAFX531, SAFX532).

Regra de seleção:

A geração do relatório será de acordo com os critérios de filtro informados na tela de geração.

-Empresa = empresa do login
-Período = período informado em tela
- Versão = versão informada em tela
-Tipo = tipo de relatório informado em tela
-Estabelecimento = estabelecimento informado em tela


Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a mensagem “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no relatório.



Regra de processamento:

[MFS-613110] Tratamento p/ desconsiderar os eventos com status de exclusão e para considerar o envio do novo evento R-4020, após evento de exclusão.


Para cada estabelecimento selecionado em tela será gerado um relatório.

Serão recuperadas as informações do evento R-4020 de acordo com a regra de seleção, todas as informações para a Empresa e Estabelecimento de acordo com o período informado. Relatório demonstrará as informações por Estabelecimento, Evento, Contribuinte, Informações Complementares do Contribuinte, Beneficiário, Identificação do Rendimento, Informações Relativas ao Pagamento, Informações Relativas a Retenções na Fonte, Processos Relacionados a não Retenção de Tributos, Informações Complementares Decorrentes de Decisão Judicial, Informações Complementares Relativas a Pagamentos no Exterior.

Será recuperado sempre a última ocorrência do evento R-4020, exceto para os eventos com status de exclusão (Evento Excluído na Mensageria), pois não devem ser considerados no Relatório, para o evento que teve exclusão e está com status de exclusão (Evento Excluído na Mensageria),

Se o evento tiver uma nova geração, o mesmo deverá ser demonstrado no relatório, por Estabelecimento, Evento, Contribuinte, Informações Complementares do Contribuinte, Beneficiário, Identificação do Rendimento, Informações Relativas ao Pagamento, Informações Relativas a Retenções na Fonte, Processos Relacionados a não Retenção de Tributos, Informações Complementares Decorrentes de Decisão Judicial, Despesas com Processo Judicial, Identificação do Advogado, Informações Complementares Relativas a Pagamentos no Exterior e Endereço do Beneficiário Residente ou Domiciliado no Exterior. Será recuperado sempre a última ocorrência do evento, (exceto se último status for de exclusão).



Ordenação:
Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

Empresa
Estabelecimento
Evento
Contribuinte
Informações Complementares do Contribuinte
Beneficiário
Identificação do Rendimento
- Informações Relativas ao Pagamento
[MFS-519027 – EXCLUSÃO] Remoção das informações listadas abaixo (no formato Sintético do relatório)
- Informações Relativas a Retenções na Fonte
- Processos Relacionados a não Retenção de Tributos
- Informações Complementares Decorrentes de Decisão Judicial
- Informações Complementares Relativas a Pagamentos no Exterior.



Agrupamento:
Empresa
Estabelecimento
Evento
Contribuinte
Informações Complementares do Contribuinte
Beneficiário
Identificação do Rendimento
- Informações Relativas ao Pagamento



Segue regras do preenchimento dos dados no relatório:




### Layout do Relatório





A partir da Versão 2.1.2 do REINF


= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ===============================
XXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                           							   Pág.: 999999
Data: 99/99/9999 às HH:MM:SS  hs

Relatório de Conferência do Evento R-4020 – Sintético
Período: MM/AAAA
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ================================
Estabelecimento: XXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
_____________________________________________________________________________________________________________________________




| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-79888 | Alessandra Cristina Navatta | Criação de um relatório de conferência do evento R-4020 (sintético). Relatórios à “Conferência dos Eventos àR-4020”. | 05/10/2022 |
| MFS- 511669 | Alessandra Cristina Navatta | Inclusão de formato para a exibição dos beneficiários do exterior. | 09/02/2023 |
| MFS-519027 | Alessandra Cristina Navatta | No relatório Sintético só deverá ser apresentada, as informações do evento R-4020 até a tag infopgto (informações relativas ao pagamento).  Os dados das tags abaixo relacionadas, serão excluídas do relatório sintético: Informações Relativas a Retenções na Fonte Processos Relacionados a não Retenção de Tributos Informações Complementares Decorrentes de Decisão Judicial Informações Complementares Relativas a Pagamentos no Exterior. | 23/03/2023 |
| MFS-537195 | Alessandra Cristina Navatta | A partir da versão 2.1.2, no relatório Sintético , Inclusão dos campos : Identificador do evento Adicional, no agrupamento Identificação do Beneficiário  Data Escr. Cont. e Observ, no agrupamento – Informações Relativas ao Pagamento Efetuado. | 31/05/2023 |
| MFS-543004 | Alessandra Cristina Navatta | Alteração na regra de exibição dos estabelecimentos | 15/06/2023 |
| MFS-594002 | Alessandra Cristina Navatta | Criada tela única, para a geração dos relatórios de conferência da família 4000.  Excluído o layout da versão 2.1.1 da documentação | 12/12/2023 |
| MFS-613110 | Rogério Ohashi | Alteração da regra de recuperação dos registros para desconsiderar os eventos com Status de Exclusão e para considerar o envio do novo evento após o evento de Exclusão (Evento Excluído na Mensageria). | 20/03/2024 |
| MFS-623425 | Alessandra Cristina Navatta | Inclusão da coluna de status no relatório. Foi necessário incluir essa coluna no relatório, que não está prevista no layout do evento, para evitar duplicidade de dados na conferência dos dados (formato Excel).   Exclusão do agrupamento ‘Informação de Identificação do Evento / Contribuinte’ e as informações existentes anteriormente neste agrupamento foram transferidas para o agrupamento ‘Identificação do Evento/ Beneficiário’, que anteriormente chama-se ‘Identificação do Beneficiário’. Este ponto foi ajustado, pois a tabela de ocorrência possui as informações por beneficiário, tipo Arquivo, Nº Recibo, Tipo do Amb., Versão do Processo de Emissão, etc... | 28/03/2024 |
| MFS626907 | Andréa Rocha | Retirada a opção de “salvar como” da geração do relatório. | 20/05/2024 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período | Data | S | S | Formato: MM/AAAA  Default: Habilitado | Local para digitação do período inicial e final de referência da geração do relatório, no formato de DD/MM/AAAA.  Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para a criação do relatório. | MFS-79888 |
| Versão | Texto | S | S | Default: Versão atual | Este campo exibe as versões de layout do Reinf. A partir da versão 2.1.1 | MFS-79888 |
| Tipo do Relatório | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções:  - Analítico - Sintético | MFS-79888 |
| Tipo de Ambiente | Checkbox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de ambiente entre as opções:  - Produção Restrita - Produção | MFS-79888 |
| Geração Multiempresa | CheckBox | S | S | Default: não selecionado | Quando o usuário selecionar esta opção, será exibido no campo Estabelecimento, os estabelecimentos de todas as empresas que o usuário tem acesso e que geraram o evento. Se o parâmetro estiver desmarcado, apenas os estabelecimentos da empresa logada que geraram o evento serão demonstrados. | MFS-79888 |
| Estabelecimentos | CheckBox | S | S | XXX / XXXXX-XXXXXXXXXXXXXXXXX  (cód. empresa + cód. e razão social do estabelecimento centralizador) ou  XXX / XXXXX-XXXXXXXXXXXXXXXXX  (cód. empresa + cód. e razão social do estabelecimento descentralizado)    Default: não selecionado | - Caso o parâmetro “Geração Multiempresa” estiver desmarcado: Na lista será demonstrado os estabelecimentos que fizeram a geração do evento apenas da empresa que acessou o módulo.      - Caso o parâmetro “Geração Multiempresa” estiver marcado: Na lista será demonstrado o estabelecimento de todas as empresas que geraram o evento e que o usuário tem acesso:          O usuário deverá escolher obrigatoriamente ao menos um estabelecimento para a geração do relatório.  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento deve ser Selecionado”  Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”. | MFS-79888 MF-543004 |


| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Empresa | Texto | Código - Descrição | Razão social da empresa. | MFS-79888 |
| Página | Numérico |  | Número da página sequencial do relatório | MFS-79888 |
| Data | Data | DD/MM/AAAA às HH:MM:SS hs | Data de emissão e hora do relatório | MFS-79888 |
| Título | Texto |  | Título do relatório: “Relatório de Conferência do Evento R-4020 - Sintético” | MFS-79888 |
| Período | Data | Formato: MM/AAAA | Deverá ser exibido o período informado em tela. | MFS-79888 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Estabelecimento | Texto | Código - Descrição | Estabelecimento informado em tela | MFS-79888 |
| [EXCLUSÃO MFS-623425] Informação de Identificação do Evento / Contribuinte | [EXCLUSÃO MFS-623425] Informação de Identificação do Evento / Contribuinte | [EXCLUSÃO MFS-623425] Informação de Identificação do Evento / Contribuinte | [EXCLUSÃO MFS-623425] Informação de Identificação do Evento / Contribuinte | [EXCLUSÃO MFS-623425] Informação de Identificação do Evento / Contribuinte |
| Tipo Arquivo | Texto |  | Campo IND_OPER gravado na tabela REINF_PGER_R4020_OC | MFS-79888 |
| Nº Recibo | Texto |  | Campo Num_recibo gravado na tabela REINF_PGER_R4020_OC | MFS-79888 |
| Tipo do Amb. | Texto |  | Tipo do ambiente, gerado no evento R-4020. | MFS-79888 |
| Processo de Emissão | Texto |  | Processo de Emissão, gerado no evento R-4020. | MFS-79888 |
| Versão do Processo de Emissão | Texto |  | Versão do Processo de Emissão, gerado no evento R-4020. | MFS-79888 |
| Tipo de Inscrição Estabelecimento | Alfanumérico |  | Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R-4020. | MFS-79888 |
| Número Inscrição Estabelecimento | Alfanumérico |  | Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R-4020. | MFS-79888 |
| Corpo do Relatório – Informações Complementares do Contribuinte | Corpo do Relatório – Informações Complementares do Contribuinte | Corpo do Relatório – Informações Complementares do Contribuinte | Corpo do Relatório – Informações Complementares do Contribuinte | Corpo do Relatório – Informações Complementares do Contribuinte |
| Natureza Jurídica | Texto |  | Natureza Jurídica | MFS-79888 |
| Corpo do Relatório – Identificação do Evento / Beneficiário  Esta parte do relatório demonstra os dados do beneficiário | Corpo do Relatório – Identificação do Evento / Beneficiário  Esta parte do relatório demonstra os dados do beneficiário | Corpo do Relatório – Identificação do Evento / Beneficiário  Esta parte do relatório demonstra os dados do beneficiário | Corpo do Relatório – Identificação do Evento / Beneficiário  Esta parte do relatório demonstra os dados do beneficiário | Corpo do Relatório – Identificação do Evento / Beneficiário  Esta parte do relatório demonstra os dados do beneficiário |
| Tipo Arquivo | Texto |  | Campo IND_OPER gravado na tabela REINF_PGER_R4020_OC | MFS-79888 |
| Status | Texto | Código-Descrição | Campo IND_STATUS gravado na tabela REINF_PGER_R4020_OC | MFS-623425 |
| Nº Recibo | Texto |  | Campo Num_recibo gravado na tabela REINF_PGER_R4020_OC | MFS-79888 |
| Tipo do Amb. | Texto |  | Tipo do ambiente, gerado no evento R-4020. | MFS-79888 |
| Processo de Emissão | Texto |  | Processo de Emissão, gerado no evento R-4020. | MFS-79888 |
| Versão do Processo de Emissão | Texto |  | Versão do Processo de Emissão, gerado no evento R-4020. | MFS-79888 |
| Tipo de Inscrição Estabelecimento | Alfanumérico |  | Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R-4020. | MFS-79888 |
| Número Inscrição Estabelecimento | Alfanumérico |  | Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R-4020. | MFS-79888 |
| CNPJ/Ident. Benef. Exterior | Texto | XXX.XXX.XX/XXXX-XX ou  Grp/Ind/Cod do Benef. | CNPJ do Beneficiário.    [ALTERAÇÃO MFS-511669] Caso beneficiário seja do exterior, apresentar o código do beneficiário, no formato: Grp/Ind/Cod do Benef. | MFS-79888 MFS- 511669 |
| Nome | Texto |  | Nome do Beneficiário. | MFS-79888 |
| IsenImun | Texto | Código - Descrição | Informações sobre isenção e imunidade | MFS-79888 |
| Identificador Evento Adicional | Texto |  | Identificador de evento adicional por beneficiário, a critério do declarante.  Este campo deve ser apresentado a partir da versão 2.1.2 | MFS-537195 |
| Corpo do Relatório – Identificação do Rendimento | Corpo do Relatório – Identificação do Rendimento | Corpo do Relatório – Identificação do Rendimento | Corpo do Relatório – Identificação do Rendimento | Corpo do Relatório – Identificação do Rendimento |
| Natureza do Rendimento | Texto |  | Natureza de Rendimento | MFS-79888 |
| Observação | Texto | Descrição | Observação | MFS-79888 |
| Corpo do Relatório – Informações Relativas ao Pagamento Efetuado | Corpo do Relatório – Informações Relativas ao Pagamento Efetuado | Corpo do Relatório – Informações Relativas ao Pagamento Efetuado | Corpo do Relatório – Informações Relativas ao Pagamento Efetuado | Corpo do Relatório – Informações Relativas ao Pagamento Efetuado |
| Fato Gerador | Texto | DD/MM/AAAA | Data do Fato Gerador | MFS-79888 |
| Valor Bruto | Texto | 0,00 | Valor bruto do rendimento | MFS-79888 |
| FCI_SPC | Texto | Código - Descrição | Indicativo de Fundo/Clube de Investimento ou Sociedade em Conta de Participação  Lista de Valores Válidos: 1 - FCI - Fundo ou clube de investimento;  2 - SCP - Sociedade em conta de participação | MFS-79888 |
| Núm. Insc. FCI_SCP | Texto | XX.XXX.XXX/XXXX-XX | Número de inscrição no CNPJ, de acordo com o conteúdo do campo indFciScp: | MFS-79888 |
| % SCP | Texto | 999 | Percentual de SCP | MFS-79888 |
| IndJud | Texto | Código - Descrição | Indicativo de Rendimento oriundo de decisão judicial  Lista de Valores Válidos: S-Sim; N-Não | MFS-79888 |
| País Resid. Exterior | Texto | 999 | Informar o código do país de destino da remessa do pagamento a residente ou domiciliado no exterior. | MFS-79888 |
| Data Escr. Cont. | Texto | DD/MM/AAAA | Informar a data da escrituração contábil.  Este campo deve ser apresentado a partir da versão 2.1.2 | MFS-537195 |
| Observ. | Texto |  | Observações  Este campo deve ser apresentado a partir da versão 2.1.2 | MFS-537195 |


| Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte | Informações Complementares do Contribuinte |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX | Natureza Jurídica: XXXX |
| Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário | Identificação do Evento / Beneficiário |
| Tipo Arquivo: XXXXXXXXXXXXXXX | Tipo Arquivo: XXXXXXXXXXXXXXX | Status: X-XXXXXXXXXXXX | Status: X-XXXXXXXXXXXX | N. Recibo: XXXXXXXXXXXXXXXXXXX | N. Recibo: XXXXXXXXXXXXXXXXXXX | N. Recibo: XXXXXXXXXXXXXXXXXXX | N. Recibo: XXXXXXXXXXXXXXXXXXX | N. Recibo: XXXXXXXXXXXXXXXXXXX | N. Recibo: XXXXXXXXXXXXXXXXXXX | N. Recibo: XXXXXXXXXXXXXXXXXXX |
| Tipo do Amb. : XXXXXXXXX | Tipo do Amb. : XXXXXXXXX | Processo de Emissão: X-XXXXXX | Processo de Emissão: X-XXXXXX | Versão do Processo de Emissão: XXXXXXXX | Versão do Processo de Emissão: XXXXXXXX | Versão do Processo de Emissão: XXXXXXXX | Versão do Processo de Emissão: XXXXXXXX | Versão do Processo de Emissão: XXXXXXXX | Versão do Processo de Emissão: XXXXXXXX | Versão do Processo de Emissão: XXXXXXXX |
| Tipo de Inscrição Estabelecimento: X-XXXXXXXXXXXX | Tipo de Inscrição Estabelecimento: X-XXXXXXXXXXXX | Tipo de Inscrição Estabelecimento: X-XXXXXXXXXXXX | Tipo de Inscrição Estabelecimento: X-XXXXXXXXXXXX | Número Inscrição Estabelecimento: XXXXX | Número Inscrição Estabelecimento: XXXXX | Número Inscrição Estabelecimento: XXXXX | Número Inscrição Estabelecimento: XXXXX | Número Inscrição Estabelecimento: XXXXX | Número Inscrição Estabelecimento: XXXXX | Número Inscrição Estabelecimento: XXXXX |
| CNPJ/Ident. Benef. Exterior: XXX.XXX.XX/XXXX-XX ou Grp/Ind/Cod do Benef. | CNPJ/Ident. Benef. Exterior: XXX.XXX.XX/XXXX-XX ou Grp/Ind/Cod do Benef. | Nome: XXXXXXXXX | Nome: XXXXXXXXX | IsenImun: Codigo - Descrição | IsenImun: Codigo - Descrição | IsenImun: Codigo - Descrição | IsenImun: Codigo - Descrição | Identificador Evento Adicional: XXXXXXXX | Identificador Evento Adicional: XXXXXXXX | Identificador Evento Adicional: XXXXXXXX |
| Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento |
| Natureza do Rendimento: XXXXXXX | Natureza do Rendimento: XXXXXXX | Natureza do Rendimento: XXXXXXX | Natureza do Rendimento: XXXXXXX | Natureza do Rendimento: XXXXXXX | Observação: Descrição | Observação: Descrição | Observação: Descrição | Observação: Descrição | Observação: Descrição | Observação: Descrição |
| Informações Relativas ao Pagamento Efetuado | Informações Relativas ao Pagamento Efetuado | Informações Relativas ao Pagamento Efetuado | Informações Relativas ao Pagamento Efetuado | Informações Relativas ao Pagamento Efetuado | Informações Relativas ao Pagamento Efetuado | Informações Relativas ao Pagamento Efetuado | Informações Relativas ao Pagamento Efetuado | Informações Relativas ao Pagamento Efetuado | Informações Relativas ao Pagamento Efetuado | Informações Relativas ao Pagamento Efetuado |
| Fato Gerador | Valor Bruto | FCI_SPC | Núm. Insc. FCI_SCP | % SCP | % SCP | IndJud | País Resid. Exterior | País Resid. Exterior | Data Escr. Cont | Observ |
| DD/MM/AAAA | 0,00 | Cód.  – Descrição | XX.XXX.XXX/XXXX-XX | 999 | 999 | Cód. | 999 | 999 | DD/MM/AAAA | XXXXXX |
