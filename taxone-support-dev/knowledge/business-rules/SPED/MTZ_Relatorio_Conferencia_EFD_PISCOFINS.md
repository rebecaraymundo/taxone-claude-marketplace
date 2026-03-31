# MTZ_Relatorio_Conferencia_EFD_PISCOFINS

> Fonte: MTZ_Relatorio_Conferencia_EFD_PISCOFINS.docx






THOMSON REUTERS

Módulo EFD – Escrituração Fiscal Digital Das Contribuições
Relatório de Conferência PIS / COFINS



DOCUMENTO DE REQUISITO


Sumário

TELA A SER DESENVOLVIDA	1
1.	REGRAS DOS CAMPOS	1
1.1.	LAYOUT DA TELA:	1
2.	REGRAS DE GERAÇÃO DO RELATÓRIO	1
2.1.	Layout do Relatório	1

## TELA A SER DESENVOLVIDA


## REGRAS DOS CAMPOS


Localização: Menu SPED / EFD – Escrituração Fiscal Digital Das Contribuições, item de menu Relatórios > Conferência PIS / COFINS

- Título da tela: Relatório Conferência PIS / COFINS


### LAYOUT DA TELA:






## REGRAS DE GERAÇÃO DO RELATÓRIO


Origem das informações para geração:

Para geração deste relatório, serão consideradas informações das seguintes origens:

Fiscal:
epc_apuracao
epc_linhas_arquivo
SAFX07 - Arquivo de Notas Fiscais;
SAFX04 – Arquivo de Cadastro de Pessoas Físicas/Jurídicas;

Regra de seleção dos Relatórios:

O relatório tem como objetivo listar as Notas Fiscais e exibir os valores de PIS e COFINS.

O sistema deve buscar as informações a partir da lista de Estabelecimentos, Data Início e Data Fim preenchidos na tela de execução do Relatório.

O Relatório deve ser gerado em csv e apresentar um arquivo para cada Estabelecimento parametrizado, nomeando o arquivo com o Código do Estabelecimento.

Os processamentos de geração executados devem ficar armazenados e disponíveis na aba Processos.

Se de acordo com os critérios informados, caso não existam informações recuperadas, serão incluídos alertas no Log.

A partir dos dados recuperados, conforme descrito na Origem das informações para geração e Regra de Seleção, será gerado o relatório conforme layout abaixo:






| OS/CH | Nome | Descrição |
| --- | --- | --- |
| 538383 | Luiz Aguiar | Criação do Documento |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Aba Parâmetros | Aba Parâmetros | Aba Parâmetros | Aba Parâmetros | Aba Parâmetros | Aba Parâmetros | Aba Parâmetros |
| Estabelecimentos | Pasta | S | S |  | Neste campo o usuário os estabelecimentos, a serem utilizados como filtro dos registros do relatório. | 538383 |
| Data Início | Data | S | S | DD/MM/AAAA | Neste campo o usuário informará uma data inicial, a ser utilizada como filtro dos registros do relatório. | 538383 |
| Data Fim | Data | S | S | DD/MM/AAAA | Neste campo o usuário informará uma data final, a ser utilizada como filtro dos registros do relatório. | 538383 |
| Executar | Botão | N | N |  | Inicia o processo de geração do relatório. | 538383 |
| Aba Processos | Aba Processos | Aba Processos | Aba Processos | Aba Processos | Aba Processos | Aba Processos |
| *Conteúdo da Aba |  |  |  |  | Exibe o componente padrão da aba de Processos | 538383 |
| Descrição | Texto | N | N |  | Exibe os parâmetros de execução do Relatório: Data Início: DD/MM/AAAA Data Fim: DD/MM/AAAA Movimento: aaaaaaaa | 538383 |
| Aba Log | Aba Log | Aba Log | Aba Log | Aba Log | Aba Log | Aba Log |
| *Conteúdo da Aba |  |  |  |  | Exibe o componente padrão da aba de Log. | 538383 |
| Aba Arquivos | Aba Arquivos | Aba Arquivos | Aba Arquivos | Aba Arquivos | Aba Arquivos | Aba Arquivos |
| *Conteúdo da Aba |  |  |  |  | Exibe o componente padrão da aba de Arquivos. | 538383 |


| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Estab. | Texto |  | Código e a razão social do estabelecimento. | 538383 |
| Tipo Registro | Texto |  | Nesta coluna exibir o valor do Tipo de Registro. Campo:  Cod_registro da tabela epc_linhas_arquivo. | 538383 |
| NF | Texto |  | Nesta coluna exibir o valor da Número da Nota Fiscal. Campo:  Texto da tabela epc_linhas_arquivo. | 538383 |
| Série | Texto |  | Nesta coluna exibir o valor da Série da Nota Fiscal. Campo:  chave_ordenacao da tabela epc_linhas_arquivo. | 538383 |
| E/S | Texto |  | Nesta coluna exibir o valor do Indicador de Entrada ou Saída. Campo:  Texto da tabela epc_linhas_arquivo. | 538383 |
| Data Lançamento | Data | Formato: DD/MM/AAAA | Nesta coluna exibir o valor da Data do Lançamento. Campo:  Texto da tabela epc_linhas_arquivo. | 538383 |
| Cód. Cliente / Fornecedor | Texto |  | Nesta coluna exibir o valor do Código do Cliente / Fornecedor. Campo:  Texto da tabela epc_linhas_arquivo. | 538383 |
| CFOP | Texto |  | Nesta coluna exibir o valor do código CFOP. Campo:  Texto da tabela epc_linhas_arquivo. | 538383 |
| Valor Total (Item) | Numérico |  | Nesta coluna exibir o valor Total do Item. Campo:  Texto da tabela epc_linhas_arquivo. | 538383 |
| Base Calc. Pis | Numérico |  | Nesta coluna exibir o valor da base de cálculo do PIS. Campo:  Texto da tabela epc_linhas_arquivo. | 538383 |
| Aliquota Pis | Numérico |  | Nesta coluna exibir o valor da alíquota do PIS. Campo:  Texto da tabela epc_linhas_arquivo. | 538383 |
| Valor Pis | Numérico |  | Nesta coluna exibir o valor do PIS. Campo:  Texto da tabela epc_linhas_arquivo. | 538383 |
| CST PIS | Texto |  | Nesta coluna exibir o valor do código da situação tributária do PIS. Campo:  Texto da tabela epc_linhas_arquivo. | 538383 |
| Base Calc. Cofins | Numérico |  | Nesta coluna exibir o valor da base de cálculo da COFINS. Campo:  Texto da tabela epc_linhas_arquivo. | 538383 |
| Aliquota Cofins | Numérico |  | Nesta coluna exibir o valor da alíquota COFINS Campo:  Texto da tabela epc_linhas_arquivo. | 538383 |
| Valor Cofins | Numérico |  | Nesta coluna exibir o valor da COFINS. Campo:  Texto da tabela epc_linhas_arquivo. | 538383 |
| CST COFINS | Texto |  | Nesta coluna exibir o valor o código da situação tributária da COFINS. Campo:  Texto da tabela epc_linhas_arquivo. | 538383 |
| Núm. Lançamento | Texto |  | Nesta coluna exibir o valor do número do lançamento contábil. Campo:  Texto da tabela epc_linhas_arquivo. | 538383 |
| Dóc. Contábil | Texto |  | Nesta coluna exibir o valor da Documento Contábil. Campo:  Texto da tabela epc_linhas_arquivo. | 538383 |
