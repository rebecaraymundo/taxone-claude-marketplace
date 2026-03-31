# MTZ_EFD_PIS-COFINS_Relatorio_de_Creditos_PIS_COFINS_de_Ativo_Imobilizado_F120_F130

> Fonte: MTZ_EFD_PIS-COFINS_Relatorio_de_Creditos_PIS_COFINS_de_Ativo_Imobilizado_F120_F130.docx






THOMSON REUTERS

PRODUTO TAXONE
Módulo EFD-Escrituração Fiscal Digital das Contribuições

Localização: Produto: TAXONE: Menu SPED, Módulo: EFD-Escrituração Fiscal Digital das Contribuições, item de menu Relatórios >> Créditos PIS/COFINS de Ativo Imobilizado (F120/F130)



DOCUMENTO DE REQUISITO

Sumário


1.	TELA	3
2.	REGRAS DOS CAMPOS	3
3.	REGRAS DE GERAÇÃO DO RELATÓRIO	5
3.1.	Layout do Relatório	13

## TELA



## REGRAS DOS CAMPOS


Produto: TAXONE
Localização da tela: Menu: SPED, Módulo: EFD-Escrituração Fiscal Digital das Contribuições, item de menu Relatórios >
Título da tela: Relatório de Créditos PIS/COFINS de Ativo Imobilizado (F120/F130) > Geração


## REGRAS DE GERAÇÃO DO RELATÓRIO


Regra Geral:

Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.

Origem das informações para geração:

Para geração deste relatório, serão consideradas as informações da seguinte origem:

Cadastro do Estabelecimento, SAFX04, SAFX13, SAFX148

Regra de seleção:

A geração do relatório será de acordo com os critérios de filtro informados na tela de geração.

-Empresa = empresa do login
-Período = Data Inicial e Data Final informado em tela
-Estabelecimento = estabelecimento informado em tela


Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a mensagem “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no relatório.


Regra de processamento:

Para cada estabelecimento selecionado em tela será gerado um relatório.
Serão recuperadas as informações da tabela de Bens do Ativo Imobilizado Com Base nos Encargos de Depreciação e no valor de aquisição, (x148_bens_ativo_imob) da Empresa e Estabelecimento, conforme período e filtros informados na tela de geração do relatório, apresentando as colunas indicadas abaixo, neste mesmo tópico.

Ordenação:
Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:
Empresa
Estabelecimento
Data de Lançamento
Bem
Nota Fiscal


Segue regras do preenchimento dos dados no relatório:



### Layout do Relatório



| MFS | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-611470 | Alessandra Cristina Navatta | Criação do Relatório de Créditos PIS/COFINS de Ativo Imobilizado (F120/F130), apenas para o Produto TAXONE. | 20/02/2024 |
| MFS-621018 e MFS-620540 | Alessandra Cristina Navatta | Aumentar no relatório o campo ‘Cód.’(código do bem), contemplando o ajuste realizado na SAFX13 e SAFX148, que alterou o campo de 30 para 60 posições. Obs. Para este item, não há impacto em nenhuma regra deste documento (pois trata-se de ajuste técnico), apenas, foi formalizado o ajuste para mantermos o histórico. Inclusão da coluna Valor da Aquisição | 20/03/2024 |
| MFS-628684 | Alessandra Cristina Navatta | Ajustar a regra do filtro “Considerar Apenas os Bens Baixados”.  Ajustar a regra dos campos Baixado, Data da Baixa e Motivo da Baixa, quando Origem das Informações = IMPORTADO (SAFX148), que são apresentados no relatório. | 10/04/2024 |
| MFS-827107 | Alessandra Cristina Navatta | Ajustes nas regras dos campos (Já Creditado PIS (Períodos Anteriores), Já Creditado COFINS (Períodos Anteriores), Saldo a Creditar PIS (Restante), Saldo a Creditar COFINS (Restante), Valor Crédito PIS (Total) e Valor Crédito COFINS (Total)) do relatório de Saldo Analítico de Crédito por Bem (Tópico 5.5.7) | 04/06/2025 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período | Data | S | S | Formato: MM/AAAA  Default: Preenchido com o mês corrente. | Campo para informar o período da geração do relatório (mês/ano).  Por default, o sistema deve apresentar o mês corrente, mas, o usuário, pode alterar o período. | MFS-611470 |
| Considerar Apenas os Bens Baixados | Check-box |  |  | Desmarcado | Se marcado, exibir no relatório, apenas os registros recuperados, que possuem a data da baixa, preenchido na tabela CREDPIS_CONTROLE ou data da baixa preenchida na SAFX148 que estejam compreendidos dentro do período de gerado. | MFS-611470 MFS-628684 |
| Considerar Apenas as Aquisições do Mês | Check-box |  |  | Desmarcado | Se marcado, exibir no relatório, apenas os registros recuperados, que possuem a data de aquisição, campo 8-DATA_AQUIS da SAFX13, compreendido no período (data inicial e data final), de geração do relatório. | MFS-611470 |
| Tipo Geração | Lista | S | S | Arquivo PDF | Permite escolher a opção de geração. Lista de valores válidos: Arquivo PDF  Excel (XLSX) | MFS-611470 |
| Estabelecimentos | CheckBox | S | S | XXX / XXXXX-XXXXXXXXXXXXXXXXX  (cód. empresa + cód. e razão social do estabelecimento centralizador) ou  XXX / XXXXX-XXXXXXXXXXXXXXXXX  (cód. empresa + cód. e razão social do estabelecimento descentralizado)    Default: não selecionado | Na lista será demonstrado os estabelecimentos da empresa logada e que o usuário tenha acesso.  Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”. | MFS-611470 |
| Executar |  |  |  |  | Campos de preenchimento obrigatório não preenchido: Se um campo obrigatório não for preenchido, exibir a mensagem: “<<Nome do campo que é exibido em tela>> deve ser preenchido!”  Outras Validações: O campo data final deve ser maior que a data inicial, caso contrário, exibir a mensagem: Data Final deve ser maior que a Data Inicial! |  |


| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Empresa | Texto | Código - Descrição | Razão social da empresa. | MFS-611470 |
| Estabelecimento | Texto | Código - Descrição | Estabelecimento informado em tela | MFS-611470 |
| Página | Numérico |  | Número da página sequencial do relatório | MFS-611470 |
| Data | Data | DD/MM/AAAA às HH:MM:SS h | Data de emissão e hora do relatório | MFS-611470 |
| Título | Texto |  | Título do relatório: “Relatório de Créditos PIS/COFINS de Ativo Imobilizado (F120/F130)” | MFS-611470 |
| Período | Data | Formato: MM/AAAA | Deverá ser exibido o período informado em tela. | MFS-611470 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Nota Fiscal | Texto |  | Apresentar o Campo 21 - NUM_DOCFIS da SAFX13 | MFS-611470 |
| Fornecedor | Texto | Ind - Código – Razão Social | Apresentar o Campo 39 -IND_FIS_JUR e 40 - COD_FIS_JUR da SAFX13 | MFS-611470 |
| Código Bem | Texto | Código | Apresentar o Campo 05 - COD_BEM da SAFX148 | MFS-611470 |
| Descrição Bem | Texto | Descrição | Apresentar o Campo DESCRICAO do bem | MFS-611470 |
| Código Incorp. | Texto |  | Apresentar o Campo 06 - COD_INC_BEM DA SAFX148 | MFS-611470 |
| Data da Aquisição do Bem | Data | DD/MM/AAAA | Apresentar o Campo 8 - DATA_AQUIS da SAFX13 | MFS-611470 |
| Data do Lançamento | Data | DD/MM/AAAA | Apresentar o Campo 7 - DATA_LANCTO da SAFX148 | MFS-611470 |
| Data Início | Data | DD/MM/AAAA | Apresentar o Campo 53 - DATA_INI_CRED da SAFX13 | MFS-611470 |
| Data Término | Data | DD/MM/AAAA | Calcular a data final, considerando a data Início e a quantidade de parcelas na coluna Parcelas (Total) | MFS-611470 |
| Valor da Aquisição | Texto | 0,00 | Apresentar o Campo 09 - VLR_AQUIS da SAFX13 | MFS-620540 |
| Base PIS | Texto | 0,00 | Apresentar o Campo 19 – VLR_BASE_PIS da SAFX148 | MFS-611470 |
| Base COFINS | Texto | 0,00 | Apresentar o Campo 23 -VLR_BASE_COFINS da SAFX148 | MFS-611470 |
| CST PIS | Texto | 00 | Apresentar o Campo 18 – COD_SIT_PIS da SAFX148 | MFS-611470 |
| CST COFINS | Texto | 00 | Apresentar o Campo 22 - COD_SIT_COFINS da SAFX148 | MFS-611470 |
| Parcela (Mensal) | Texto | 00 | Calcular a quantidade de meses, entre os meses/ano da coluna data início até o mês/ano da coluna data lançamento do crédito.  Exemplo: Aquisição: jan/2023 Lançamento do crédito: jan23 = 1 parcela  Aquisição: jan/2023 Lançamento do crédito: jan24 = 13 parcelas | MFS-611470 |
| Valor Crédito PIS (Mensal) | Texto | 0,00 | Apresentar o Campo 21 - VLR_PIS da SAFX148 | MFS-611470 |
| Valor Crédito COFINS (Mensal) | Texto | 0,00 | Apresentar o Campo 25 - VLR_COFINS da SAFX148 | MFS-611470 |
| Já Creditado PIS (Períodos Anteriores) | Texto | 0,00 | Resultado da multiplicação da coluna Parcelas (Períodos Anteriores) * Valor Total do Crédito de PIS (Mensal)    [ALTERAÇÃO MFS-827107] Somatório do valor crédito PIS (mensal) das parcelas anteriores | MFS-611470 MFS-827107 |
| Já Creditado COFINS (Períodos Anteriores) | Texto | 0,00 | Resultado da multiplicação da coluna Parcelas (Períodos Anteriores) * Valor Total do Crédito de COFINS (Mensal)    [ALTERAÇÃO MFS-827107] Somatório do valor crédito COFINS (mensal) das parcelas anteriores | MFS-611470 MFS-827107 |
| Parcelas (Períodos Anteriores) | Texto | 00 | Resultado da subtração da coluna Parcela (Mensal) - 1 | MFS-611470 |
| Saldo a Creditar PIS (Restante) | Texto | 0,00 | Resultado da subtração das colunas: Resultado da multiplicação do valor do PIS * Parcela (Restante)  [ALTERAÇÃO MFS-827107] Resultado da expressão: (Valor Crédito PIS (Total) - (Somatório do valor crédito PIS (mensal) das parcelas anteriores) – (Valor crédito COFINS Mensal (atual)) | MFS-611470 MFS-827107 |
| Saldo a Creditar COFINS (Restante) | Texto | 0,00 | Resultado da subtração das colunas: Resultado da multiplicação do valor do COFINS * Parcela (Restante)  [ALTERAÇÃO MFS-827107] Resultado da expressão: (Valor Crédito COFINS (Total) - (Somatório do valor crédito COFINS (mensal) das parcelas anteriores) – (Valor crédito COFINS Mensal (atual)) | MFS-611470 MFS-827107 |
| Parcelas (Restante) | Texto | 00 | Resultado da subtração das colunas: Parcelas (Total) - Parcela (Mensal) | MFS-611470 |
| Valor Crédito PIS (Total) | Texto | 0,00 | Resultado da multiplicação das colunas:  Valor Crédito PIS (Mensal)* Parcelas (Total)  [ALTERAÇÃO MFS-827107]  Se o campo Indicador de Operações Geradoras de Crédito =(IND_OPER_CRED=’3’): Resultado da expressão: Valor da Aquisição (VLR_BEM_ATIVO_IMOB) – Parcela do Valor da Aquisição a ser excluída (VLR_PARCELA_DEP_MES)* ALIQ_PIS  Se o campo Operações Geradoras de Crédito DIFERENTE Aquisição (IND_OPER_CRED<>’3’): Resultado da expressão: Valor da Aquisição (VLR_BEM_ATIVO_IMOB) – Parcela do Valor da Aquisição a ser excluída (VLR_DEP_AMORT_EXC)* ALIQ_PIS | MFS-611470 MFS-827107 |
| Valor Crédito COFINS (Total) | Texto | 0,00 | Resultado da multiplicação das colunas:  Valor Crédito COFINS (Mensal)* Parcelas (Total)  [ALTERAÇÃO MFS-827107] Se o campo Indicador de Operações Geradoras de Crédito =(IND_OPER_CRED=’3’): Resultado da expressão: Valor da Aquisição (VLR_BEM_ATIVO_IMOB) – Parcela do Valor da Aquisição a ser excluída (VLR_PARCELA_DEP_MES)* ALIQ_COFINS  Se o campo Operações Geradoras de Crédito DIFERENTE Aquisição (IND_OPER_CRED<>’3’): Resultado da expressão: Valor da Aquisição (VLR_BEM_ATIVO_IMOB) – Parcela do Valor da Aquisição a ser excluída (VLR_DEP_AMORT_EXC)* ALIQ_COFINS | MFS-611470 MFS-827107 |
| Parcelas (Total) | Texto | 00 | Apresentar o Campo 44 - IND_PARCELA da SAFX13 | MFS-611470 |
| Baixado | Texto | Sim / Não | Origem das Informações: CREDPIS:  Se o campo ‘Origem das Informações’ estiver preenchido com ‘CREDPIS’, considerar a informação do campo DATA_BAIXA da tabela CREDPIS_CONTROLE, se preenchido gravar ‘Sim’. Caso não preenchido gravar ‘Não’   Origem das Informações: IMPORTADO: [ALTERAÇÃO MFS-628684] Caso o campo ‘Origem das Informações’ estiver preenchido com ‘IMPORTADO’ e o campo Data da Baixa da SAFX148 estiver preenchido, gravar ‘Sim’. Caso não exista informação no campo Data da Baixa da SAFX148 e não existir informação na CREDPIS_CONTROLE, gravar ‘Não’.   Caso exista a informação na CREDPIS_CONTROLE (situação dos clientes que não usam o módulo CREDPIS, para criar automaticamente a SAFX148, mas, possuem a informação dos bens baixados (informação atualmente existente apenas na tela do CREDPIS, em: Manutenção/ Controle de Parcelas), deve ser realizado o seguinte procedimento:  1. Efetuar a ‘Geração do Controle’ (no módulo CREDPIS), mas, não pode fazer a ‘Geração de Parcelas (reg. F120 e F130’, pois, a SAFX148 (importada), será deletada pelo processo de geração de parcelas); 2. Efetuar a Baixa do Bem na tela (Manutenção/ Controle de Parcelas) e o sistema deve considerar no relatório, a informação que está no campo ‘Data da Baixa’, se preenchido gravar ‘Sim’. Caso não preenchido gravar ‘Não’. | MFS-611470 MFS-628684 |
| Data da Baixa | Data | DD/MM/AAAA | Origem das Informações: CREDPIS:  Se o campo ‘Origem das Informações’ estiver preenchido com ‘CREDPIS’, considerar a informação do campo DATA_BAIXA da tabela CREDPIS_CONTROLE.   Origem das Informações: IMPORTADO: [ALTERAÇÃO MFS-628684] Caso o campo ‘Origem das Informações’ estiver preenchido com ‘IMPORTADO’, e o campo Data da Baixa da SAFX148 estiver preenchido, gravar esta informação. Caso não exista informação no campo Data da Baixa da SAFX148 e não existir informação na CREDPIS_CONTROLE, não preencher este campo. Caso exista a informação na CREDPIS_CONTROLE (situação dos clientes que não usam o módulo CREDPIS, para criar automaticamente a SAFX148, mas, possuem a informação dos bens baixados (informação atualmente existente apenas na tela do CREDPIS, em: Manutenção/ Controle de Parcelas), deve ser realizado o seguinte procedimento:  1. Efetuar a ‘Geração do Controle’ (no módulo CREDPIS), mas, não pode fazer a ‘Geração de Parcelas (reg. F120 e F130’, pois, a SAFX148 (importada), será deletada pelo processo de geração de parcelas); 2. Efetuar a Baixa do Bem na tela (Manutenção/ Controle de Parcelas) e o sistema deve considerar no relatório, a informação que está no campo ‘Data da Baixa’. | MFS-611470 MFS-628684 |
| Motivo da Baixa | Texto |  | Origem das Informações: CREDPIS:  Se o campo ‘Origem das Informações’ estiver preenchido com ‘CREDPIS’, considerar a informação do campo MOTIVO_BAIXA da tabela CREDPIS_CONTROLE.   Origem das Informações: IMPORTADO: [ALTERAÇÃO MFS-628684] Caso o campo ‘Origem das Informações’ estiver preenchido com ‘IMPORTADO’ e o campo Indicador do Motivo da Baixa da SAFX148 estiver preenchido, gravar esta informação. Caso não exista informação no campo Indicador do Motivo da Baixa da SAFX148 e não existir informação na CREDPIS_CONTROLE, não preencher este campo. Caso exista a informação na CREDPIS_CONTROLE (situação dos clientes que não usam o módulo CREDPIS, para criar automaticamente a SAFX148, mas, possuem a informação dos bens baixados (informação atualmente existente apenas na tela do CREDPIS, em: Manutenção/ Controle de Parcelas), deve ser realizado o seguinte procedimento:  1. Efetuar a ‘Geração do Controle’ (no módulo CREDPIS), mas, não pode fazer a ‘Geração de Parcelas (reg. F120 e F130’, pois, a SAFX148 (importada), será deletada pelo processo de geração de parcelas); 2. Efetuar a Baixa do Bem na tela (Manutenção/ Controle de Parcelas) e o sistema deve considerar no relatório, a informação que está no campo ‘Motivo da Baixa’. | MFS-611470 MFS-628684 |
| Origem das Informações | Texto | CREDPIS ou IMPORTADO | Se o registro na X148 foi criado pelo processo de cálculo de parcelas (módulo CREDPIS), considerar ‘CREDPIS’, caso o registro seja importado ou incluído via tela de manutenção, apresentar ‘IMPORTADO’ | MFS-611470 |
| Total do Estabelecimento: <<Código do estabelecimento>> |  | 0,00 | Apresentar um total por estabelecimento, para todos os campos de valores. | MFS-611470 |
| Total Geral |  | 0,00 | Apresentar um total independente dos estabelecimentos, para todos os campos de valores | MFS-611470 |
