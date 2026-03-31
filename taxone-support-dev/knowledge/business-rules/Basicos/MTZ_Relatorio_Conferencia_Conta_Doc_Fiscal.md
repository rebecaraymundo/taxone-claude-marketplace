# MTZ_Relatorio_Conferência Conta Doc Fiscal

> Fonte: MTZ_Relatorio_Conferência Conta Doc Fiscal.docx






THOMSON REUTERS

Módulo Report Fiscal
Relatório de Conferência Conta Doc Fiscal




DOCUMENTO DE REQUISITO


Sumário

TELA A SER DESENVOLVIDA	1
1.	REGRAS DOS CAMPOS	1
1.1.	LAYOUT DA TELA:	1
2.	REGRAS DE GERAÇÃO DO RELATÓRIO	1
2.1.	Layout do Relatório	1

## TELA A SER DESENVOLVIDA


## REGRAS DOS CAMPOS


Localização: Menu Básicos / Report Fiscal, item de menu Operacionais > Conferência Conta Doc Fiscal > Relatório

- Título da tela: Relatório de Conferência Conta Doc Fiscal


### LAYOUT DA TELA:







## REGRAS DE GERAÇÃO DO RELATÓRIO


Origem das informações para geração:

Para geração deste relatório, serão consideradas informações das seguintes origens:

Fiscal:
SAFX07 - Arquivo de Notas Fiscais;
SAFX08 – Itens Notas Fiscais Mercadorias e Produtos;
SAFX2005 – Tabela de Tipo de Documento
SAFX04 – Arquivo de Cadastro de Pessoas Físicas/Jurídicas;
SAFX2012 – Tabela de Códigos Fiscais;

Contábil:
SAFX01 - Arquivo Contábil;
SAFX2002 - Tabela do Plano de Contas;


Regra de seleção dos Relatórios:

O relatório tem como objetivo listar as Notas Fiscais e comparar os valores com os lançamentos contábeis correspondentes a fim de verificar qualquer divergência nos valores.

A partir do Perfil escolhido e parametrizado em Parâmetros de Conferência Conta Doc Fiscal o sistema deve buscar as informações Fiscais e Contábeis a partir da Lista de Estabelecimentos, códigos CFOP e Contas Contábeis parametrizadas no Perfil, além disso usar os critérios de Data Inicio, Data Fim, Movimento e Impostos preenchidos na tela de execução do Relatório.

Após a listagem dos dados Contábeis o sistema executa uma limpeza do Estornos, basicamente buscando valores duplicados (um de entrada e outro de estorno) e removendo-os.

O Relatório deve ser gerado em csv e apresentar um arquivo para cada Estabelecimento parametrizado, nomeando o arquivo com o Código do Estabelecimento.

As informações de ambas as origens devem ser relacionadas pelo Código do Estabelecimento, Nota Fiscal, Data Fiscal e por (Doc. SAP ou Num. Lançamento).

Os processamentos de geração executados devem ficar armazenados e disponíveis na aba Processos.

Se de acordo com os critérios informados, caso não existam informações recuperadas, serão incluídos alertas no Log.

A partir dos dados recuperados, conforme descrito na Origem das informações para geração e Regra de Seleção, será gerado o relatório conforme layout abaixo:






| OS/CH | Nome | Descrição |
| --- | --- | --- |
| 534766 | Luiz Aguiar | Criação do Documento |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Aba Parâmetros | Aba Parâmetros | Aba Parâmetros | Aba Parâmetros | Aba Parâmetros | Aba Parâmetros | Aba Parâmetros |
| Perfil | Combobox | S | S | Default: Em Branco | Este campo é uma lista dos perfis criados na tela de Parâmetros da Conferência Conta Doc Fiscal | 534766 |
| Data Início | Data | S | S | DD/MM/AAAA | Neste campo o usuário informará uma data inicial, a ser utilizada como filtro dos registros do relatório. | 534766 |
| Data Fim | Data | S | S | DD/MM/AAAA | Neste campo o usuário informará uma data final, a ser utilizada como filtro dos registros do relatório. | 534766 |
| Movimento | Radiobutton | S | S | Default: Em Branco | Informa o Movimento com as seguintes opções: Entrada Saída Ambos | 534766 |
| Impostos | Checkbox | S | S | Default: Em Branco | Informa os Impostos para execução do relatório, podendo selecionar uma ou mais opções abaixo:  ICMS IPI ICMS-ST PIS COFINS ICMS-FCP ICMS-DESTINO ICMS-ORIGEM | 534766 |
| Executar | Botão | N | N |  | Inicia o processo de geração do relatório. | 534766 |
| Aba Processos | Aba Processos | Aba Processos | Aba Processos | Aba Processos | Aba Processos | Aba Processos |
| *Conteúdo da Aba |  |  |  |  | Exibe o componente padrão da aba de Processos | 534766 |
| Descrição | Texto | N | N |  | Exibe os parâmetros de execução do Relatório: Perfil: Descrição do Perfil Data Início: DD/MM/AAAA Data Fim: DD/MM/AAAA Movimento: aaaaaaaa | 534766 |
| Aba Log | Aba Log | Aba Log | Aba Log | Aba Log | Aba Log | Aba Log |
| *Conteúdo da Aba |  |  |  |  | Exibe o componente padrão da aba de Log | 534766 |
| Aba Arquivos | Aba Arquivos | Aba Arquivos | Aba Arquivos | Aba Arquivos | Aba Arquivos | Aba Arquivos |
| *Conteúdo da Aba |  |  |  |  | Exibe o componente padrão da aba de Arquivos | 534766 |


| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Cabeçalho do Relatório | Cabeçalho do Relatório | Cabeçalho do Relatório | Cabeçalho do Relatório | Cabeçalho do Relatório |
| Data | Data | DD/MM/AAAA às HH:MM:SS | Data de emissão e hora do relatório | 534766 |
| Filial | Texto |  | Código e a razão social do estabelecimento. | 534766 |
| Título | Texto |  | Título do relatório ‘Relatório de Conferência Conta Doc Fiscal’ | 534766 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Agrupador Movimento | Label | Entradas Saídas | Agrupador do relatório para separação de Entradas e Saídas. Campo:  MOVTO_E_S da SAFX07 (Fiscal) ou  IND_DEB_CRE da SAFX01 (Contábil) | 534766 |
| Data Fiscal | Data | Formato: DD/MM/AAAA | Nesta coluna exibir o valor da Data Fiscal. Campo:  DAT_FISCAL da SAFX07 ou  DATA_OPERACAO da SAFX01 | 534766 |
| Nota Fiscal | Alfanumérico |  | Nesta coluna exibir o número da Nota Fiscal. Campo:  NUM_DOCFIS da SAFX07 ARQUIVAMENTO da SAFX01 Aqui é necessário buscar parte da String e não todo o conteúdo do campo. | 534766 |
| CFOP | Alfanumérico |  | Nesta coluna exibir o CFOP. Campo:  COD_CFO da SAFX12 (Fiscal) ARQUIVAMENTO da SAFX01 (Contábil) Aqui é necessário buscar parte da String e não todo o conteúdo do campo. | 534766 |
| Doc. SAP | Alfanumérico |  | Nesta coluna exibir o valor da Data Fiscal. Campo:  NUM_CONTROLE_DOCTO da SAFX07 ou  HISTCOMPL da SAFX01 | 534766 |
| Num. Lançamento | Alfanumérico |  | Nesta coluna exibir o valor do Lançamento. Campo:  NUM_LANCAMENTO da SAFX07 ou  NUM_LANCAMENTO da SAFX01 | 534766 |
| Centro de Custo | Alfanumérico |  | Nesta coluna exibir o valor do Centro de Custo. Campo:  DSC_RESERVADO1 da SAFX07 (Fiscal) O valor não é exibido para contábil | 534766 |
| Doc. Contábil | Alfanumérico |  | Nesta coluna exibir o valor do Doc. Contábil. Campo:  DSC_RESERVADO2 da SAFX07 (Fiscal) O valor não é exibido para contábil | 534766 |
| Local | Texto |  | Nessa coluna exibir a origem dos dados com as seguintes opções: Fiscal Contábil Ambos  Caso o registro tenha sido localizado na SAFX07, preencher como Fiscal. Caso o registro tenha sido localizado na SAFX01, preencher como Contábil. Caso o registro tenha sido localizado em ambas as tabelas, preencher como Ambos. | 534766 |
| Fiscal | Fiscal | Fiscal | Fiscal | Fiscal |
| ICMS | Numérico |  | Nesta coluna deve exibir o valor do ICMS, campo VLR_ICMS da SAFX08. | 534766 |
| IPI | Numérico |  | Nesta coluna deve exibir o valor do IPI, campo VLR_IPI da SAFX08. | 534766 |
| ICMS-ST | Numérico |  | Nesta coluna deve exibir o valor ICMS Substituição Tributária, campo VLR_SUBST_ICMS SAFX08. | 534766 |
| PIS | Numérico |  | Nesta coluna deve exibir o valor do PIS, campo VLR_PIS da SAFX08. | 534766 |
| COFINS | Numérico |  | Nesta coluna deve exibir o valor do COFINS, campo VLR_COFINS da SAFX08. | 534766 |
| ICMS-FCP | Numérico |  | Nesta coluna deve exibir o valor do ICMS-FCP, campo VLR_FCP_UF_DEST da SAFX08. | 534766 |
| ICMS-ORIG | Numérico |  | Nesta coluna deve exibir o valor do ICMS-ORIG, campo VLR_ICMS_UF_ORIG da SAFX08. | 534766 |
| ICMS-DEST | Numérico |  | Nesta coluna deve exibir o valor do ICMS-DEST, campo VLR_ICMS_UF_DEST da SAFX08. | 534766 |
| Contábil | Contábil | Contábil | Contábil | Contábil |
| ICMS | Numérico |  | Nesta coluna deve exibir o valor do ICMS, campo VLR_LANCTO da SAFX01 para o imposto correspondente. | 534766 |
| IPI | Numérico |  | Nesta coluna deve exibir o valor do IPI, campo VLR_LANCTO da SAFX01 para o imposto correspondente. | 534766 |
| ICMS-ST | Numérico |  | Nesta coluna deve exibir o valor ICMS Substituição Tributária, campo VLR_LANCTO da SAFX01 para o imposto correspondente. | 534766 |
| PIS | Numérico |  | Nesta coluna deve exibir o valor do PIS, campo VLR_LANCTO da SAFX01 para o imposto correspondente. | 534766 |
| COFINS | Numérico |  | Nesta coluna deve exibir o valor do COFINS, campo VLR_LANCTO da SAFX01 para o imposto correspondente. | 534766 |
| ICMS-FCP | Numérico |  | Nesta coluna deve exibir o valor do ICMS-FCP, campo VLR_LANCTO da SAFX01 para o imposto correspondente. | 534766 |
| ICMS-ORIG | Numérico |  | Nesta coluna deve exibir o valor do ICMS-ORIG, campo VLR_LANCTO da SAFX01 para o imposto correspondente. | 534766 |
| ICMS-DEST | Numérico |  | Nesta coluna deve exibir o valor do ICMS-DEST, campo VLR_LANCTO da SAFX01 para o imposto correspondente. | 534766 |
| Diferença | Diferença | Diferença | Diferença | Diferença |
| ICMS | Numérico |  | Exibir a diferença ente os valores de ICMS Fiscal e Contábil | 534766 |
| IPI | Numérico |  | Exibir a diferença ente os valores de IPI Fiscal e Contábil | 534766 |
| ICMS-ST | Numérico |  | Exibir a diferença ente os valores de ICMS-ST Fiscal e Contábil | 534766 |
| PIS | Numérico |  | Exibir a diferença ente os valores de PIS Fiscal e Contábil | 534766 |
| COFINS | Numérico |  | Exibir a diferença ente os valores de COFINS Fiscal e Contábil | 534766 |
| ICMS-FCP | Numérico |  | Exibir a diferença ente os valores de ICMS-FCP Fiscal e Contábil | 534766 |
| ICMS-ORIG | Numérico |  | Exibir a diferença ente os valores de ICMS-ORIG Fiscal e Contábil | 534766 |
| ICMS-DEST | Numérico |  | Exibir a diferença ente os valores de ICMS-DEST Fiscal e Contábil | 534766 |
| Totais | Totais | Totais | Totais | Totais |
| Total de Entradas/Saídas | Numérico |  | Exibir o somatório das Entradas ou Saídas de Cada Imposto, para Fiscal, Contábil e Diferença. | 534766 |
