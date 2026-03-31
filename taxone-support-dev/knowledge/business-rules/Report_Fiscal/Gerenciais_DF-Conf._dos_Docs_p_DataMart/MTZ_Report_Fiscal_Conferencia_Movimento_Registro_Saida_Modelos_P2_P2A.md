---
source: "MTZ_Report_Fiscal_Conferencia_Movimento_Registro_Saida_Modelos_P2_P2A.docx"
category: Report_Fiscal
converted: auto
---





THOMSON REUTERS

Report Fiscal
Relatório de Conferencia do Movimento do Registro de Saídas Modelos P2/P2A

Localização da tela: Básicos >> Report Fiscal

Menu: Gerenciais >> Documentos Fiscais >> Conferencia dos Documentos p/ DataMart >> Movimentos de Saídas >> Ajuste SINIEF >> Geração.
Gerenciais >> Documentos Fiscais >> Conferencia dos Documentos p/ DataMart >> Movimentos de Saídas >> Ajuste SINIEF >> Emissão.

DOCUMENTO DE REQUISITO


Sumário

**1.	Regras Gerais	1**
2.	Regras dos Campos da Tela de Geração	1
3.	Regras dos Campos da Tela de Emissão	1
4.	Recuperação dos dados:	1
5.	Itens do Relatório	1
4.1 – Principal	1
3.2 – Resumo por Decendio	1
3.3 – Resumo por Quinzena	1
3.4 – Resumo da Observação	1
3.5 – Resumo por UF	1
3.6 – Resumo por Alíquota	1
3.7 – Resumo por CFO	1
6.	Tratamento dos Parâmetros p/ UF	1
7.	Tramentos de Situações especiais	1

# Regras Gerais

O relatório de conferência do movimento de saída passa a ser gerado via processamento assíncrono, por isso está sendo dividido em duas etapas: geração e emissão do relatório.
No Tax One o relatório é armazenado em arquivos CSV e PDF.
No DW o relatório é disponibilizado em tela, em arquivo PSR e PDF.

# Regras dos Campos da Tela de Geração

Localização da tela: Básicos >> Report Fiscal

Título da tela: Gerenciais >> Documentos Fiscais >> Conferencia dos Documentos p/ DataMart Movimentos de Saídas >> Ajuste SINIEF >> Geração.



# Regras dos Campos da Tela de Emissão

Localização da tela: Básicos >> Report Fiscal

Título da tela: Gerenciais >> Documentos Fiscais >> Conferencia dos Documentos p/ DataMart Movimentos de Saídas >> Ajuste SINIEF >> Emissão.



Funcionamento da Tela:
Usuário preenche os campos Período, Obrigação Fiscal e  UF.
O sistema apresenta os Estabelecimentos que possuem relatórios gerados para o período e obrigação fiscal informados.
Usuário aciona a execução da emissão.
O sistema disponibiliza os relatórios que já foram gerados através da opção (Gerenciais >> Documentos Fiscais >> Conferencia dos Documentos p/ DataMart Movimentos de Saídas >> Ajuste SINIEF >> Geração) que atendam aos critérios informados na tela.


# Recuperação dos dados para Relatório:

Origem dos Dados: Tabelas de Documento Fiscal (SAFX07, SAFX08, SAFX09).
Critérios de Seleção:
- Codigo da Empresa de login
- Estabelecimento informado na tela
- Data fiscal compreendida no período da geração
- Classificação do Documento Fiscal = 1, 2, 3, 4

São recuperada notas fiscais com e sem itens.

Origem dos Dados: Tabelas de Documento Fiscal Utilities (SAFX42, SAFX43).
Critérios de Seleção:
- Codigo da Empresa de login
- Estabelecimento informado na tela
- Data fiscal compreendida no período da geração

Origem dos Dados: Tabelas do Convênio 115 (ICT_MM_CONV115).
Critérios de Seleção:
- Codigo da Empresa de login
- Estabelecimento informado na tela
- Data fiscal compreendida no período da geração

Esta regra não está completa, o objetivo é apenas dar uma noção das informações tratadas pelo relatório.


# Itens do Relatório


## 4.1 – Principal

O relatório apresenta os valores das bases (tributada, isenta/redução e outras) em linhas distintas, fazendo o lançamento das bases da seguinte forma:

Consolidação dos valores por documento fiscal:

As bases tributadas devem ser totalizadas por Imposto (ICMS, IPI ou ST), CFOP e Alíquota

As demais bases (isenta/redução e outras) devem ser totalizadas por Imposto (ICMS, IPI ou ST) e CFOP. Neste caso, a alíquota não precisa ser considerada, uma vez que ela não aparece nas linhas referentes a estes valores.

Exemplo: Supondo uma nota com os seguintes itens:


A demonstração das bases no livro deve será feita da seguinte forma:


Campos que compões o relatório:
- Espécie: preenchido com o Tipo do Documento (campo 05 da SAFX07)
- Serie/Subserie
- Numero Documento Fiscal
- Dia: dia correspondente a Data Fiscal da nota
- UF Destino: UF da Pessoa Física Jurídica da Nota Fiscal
- Valor Contábil: valor total da nota (safx07) para notas sem item. Para notas com itens somatório do valor contábil item.
- Codificação – Contábil: Conta Contábil da capa da nota fiscal. Foi retirada a opção de escolha na tela de emissão, para exibir a conta contábil ou o código de controle.
- Codificação – Fiscal: CFOP dos itens da nota fiscal
- ICMS/IPI
- Cod (a): preenchido com:
- 1 – para base tributada de ICMS oU IPI
- 2 – para base isenta + reduzida de ICMS ou IPI
- 3 – para base outras de ICMS ou IPI
- Base de Cálculo: base de cálculo do ICMS ou IPI (tributada, isenta + reduzida, outras)
- Imposto Debitado: Valor do ICMS ou IPI
- Código do Destinatário: CPF/CGC da Pessoa Fis/Jur da nota fiscal. Foi retirada a opção de escolha na tela de emissão, para exibir o CPF/CGC ou o Código da Pessoa Fis/Jur.
- Número da OBS: sequencial que identifica uma observação apresentada no Resumo da Observação



## 3.2 – Resumo por Decendio
Este resumo é demonstrado quando o parâmetro 14 da tela de Parâmetros p/ UF do módulo ICMS estiver marcado.
Totalização das notas fiscais apresentadas na parte principal do livro por decêndio (1º , 2º e 3º decêndio do mês).
Cada decêndio agrupa os valores das notas por Tributo (ICMS ou IPI) e Código de Tributação (1 – base tributada, 2 – para base isenta + reduzida, 3 – base outras). Valores totalizados são os apresentados na parte principal:
- Valor Contábil
- Base de Cálculo
- Imposto Debitado



## 3.3 – Resumo por Quinzena
Este resumo é demonstrado quando o parâmetro 15 da tela de Parâmetros p/ UF do módulo ICMS estiver marcado.
Totalização das notas fiscais apresentadas na parte principal do livro por quinzena (1ª e 2ª quinzena do mês).
Cada decêndio agrupa os valores das notas por Tributo (ICMS ou IPI) e Código de Tributação (1 – base tributada, 2 – para base isenta + reduzida, 3 – base outras).  Valores totalizados são os apresentados na parte principal:
- Valor Contábil
- Base de Cálculo
- Imposto Debitado



## 3.4 – Resumo da Observação
Relação das observações das notas demonstradas na parte principal.


## 3.5 – Resumo por UF
Este resumo é demonstrado quando o parâmetro 3 da tela de Parâmetros p/ UF do módulo ICMS estiver marcado.
Totalização das notas fiscais apresentadas na parte principal do livro por UF da Pessoa Física Jurídica da nota.
Valores totalizados são os apresentados na parte principal:
- Valor Contábil: segregado em dois campos
- Valor Contábil Contribuinte:
- Valor Contábil Não Contribuinte:
- Base de Cálculo: base tributada de ICMS segregada em dois campos:
- Base de Cálculo Contribuinte
- Base de Cálculo Não Contribuinte
- Base Outras
- ICMS Cobrado p/ Substituição Tributária

Na tela de Parâmetros por UF do módulo ICMS, escolhendo o parâmetro 3 – Resumo por UF, são apresentadas três opções:
- Layout Resumido Contribuinte pelo CFOP;
- Layout Resumido Contribuinte pelo Indicador;
- Layout Completo.
Se for selecionada a opção Layout Resumido Contribuinte pelo CFOP, considera-se os seguintes CFOPs como não contribuinte: '618','619','645','653','663','5258','5307','5357','6107','6108','6258','6307','6357') Ou seja, se o CFOP da nota fiscal estiver nessa relação, os valores contábil e base de ICMS são apresentados na coluna NÃO CONTRIBUINTE.
Se for selecionada a opção "Layout Resumido Contribuinte pelo Indicador", será utilizado o campo "29 - Contribuinte Final" da tabela SAFX07. Se o campo 29 for igual "S", os valores contábil e base de ICMS são apresentados na coluna CONTRIBUINTE; quanto o indicador não estiver preenchido, ou for igual "N", os valores contábil e base de ICMS são apresentados na coluna NÃO CONTRIBUINTE.

IF ValorParam ('TP_GI') = '1' THEN  -- Contribuinte/Não Contribuinte decidido pelo CFOP
IF SUBSTR(pItem.COD_CFO,1) IN ('618','619','645','653','663','5258','5307','5357','6107','6108','6258','6307','6357') THEN
pItem.VLR_CONT_NAO_CONTR      := pItem.VLR_CONTAB_ITEM;
pItem.VLR_BASE_ICMS_NAO_CONTR := pItem.VLR_BASE_ICMS_1;
ELSE
pItem.VLR_CONT_CONTR          := pItem.VLR_CONTAB_ITEM;
pItem.VLR_BASE_ICMS_CONTR     := pItem.VLR_BASE_ICMS_1;
END IF;
ELSE        -- C/ CONTRIB. PELO INDICADOR ('2') OU LAYOUT COMPLETO ('3')
IF NVL(pCapaNF.CONTRIB_FINAL,'N') = 'N' THEN
pItem.VLR_CONT_NAO_CONTR      := pItem.VLR_CONTAB_ITEM;
pItem.VLR_BASE_ICMS_NAO_CONTR := pItem.VLR_BASE_ICMS_1;
ELSE
pItem.VLR_CONT_CONTR          := pItem.VLR_CONTAB_ITEM;
pItem.VLR_BASE_ICMS_CONTR     := pItem.VLR_BASE_ICMS_1;
END IF;
END IF;


## 3.6 – Resumo por Alíquota
Este resumo é demonstrado quando o parâmetro 4 da tela de Parâmetros p/ UF do módulo ICMS estiver marcado.
Totalização das notas fiscais apresentadas na parte principal do livro por Alíquota de ICMS. São consideradas apenas as notas com Base Tributada de ICMS, ou seja, Tributo ICMS e Código de Tributação (1 – base tributada).
Campos apresentados:
- Base de Cálculo: total da base tributada de ICMS das notas apresentadas na parte principal, agrupadas por Alíquota
- Alíquota: Alíquota de ICMS das notas apresentadas na parte principal.
- Valor do ICMS: total do ICMS das notas apresentadas na parte principal, agrupadas por Alíquota.



## 3.7 – Resumo por CFO
Este resumo é demonstrado quando o parâmetro 2 da tela de Parâmetros p/ UF do módulo ICMS estiver marcado.
Totalização das notas fiscais apresentadas na parte principal do livro por CFOP da nota.
Cada CFOP agrupa os valores das notas por Tributo (ICMS ou IPI) e Código de Tributação (1 – base tributada, 2 – para base isenta + reduzida, 3 – base outras).  Valores totalizados são os apresentados na parte principal:
- Valor Contábil
- Base de Cálculo
- Imposto Debitado


# Tratamento dos Parâmetros p/ UF
A tela de Parâmetros p/ UF do módulo ICMS possui um conjunto de parâmetros que influencia no relatório de conferência do movimento de saída.
Alguns desses parâmetros estão elencados abaixo:





# Tramentos de Situações especiais
Para algumas notas fiscais são aplicados tratamentos para escriturá-las no livro.
Aqui não estão descritas todas as situações.




---

| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-71313 | Registro de Saídas Modelos P2/P2A | Tela Conferencia do Movimento do Registro de Saída Modelos P2/P2A – Geração e Emissão |


---

| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período |  | S | S |  | MM/AAAA |  |
| Obrigação Fiscal |  | S | S | Listbox | Lista composta pelos livros: - 102 – Registro de Saídas – Modelo P2 - 104 – Registro de Saídas – Modelo P2A |  |
| UF |  | S | S | Listbox | Lista composta por todas as Ufs (Tabela Estado) mais a opção “*Todas as Ufs*” |  |
| Estabelecimentos |  | S | S | Seleção de múltiplos estabelecimentos | Apresentar os estabelecimentos que atendam aos seguintes critérios: - Empresa de login  - Estabelecimento pertencente a UF igual a selecionada na opção acima   ou   Estabelecimento pertencente a qualquer UF caso a opção *Todas as UFs* seja selecionada. |  |


---

| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período |  | S | S |  | MM/AAAA |  |
| Obrigação Fiscal |  | S | S | Listbox | Lista composta pelos livros: - 102 – Registro de Saídas – Modelo P2 - 104 – Registro de Saídas – Modelo P2A |  |
| UF |  | S | S | Listbox | Lista composta por todas as Ufs (Tabela Estado) mais a opção “*Todas as Ufs*” |  |
| Estabelecimentos |  | S | S | Seleção de múltiplos estabelecimentos | Apresentar os estabelecimentos que atendam aos seguintes critérios: - Empresa de login  - Estabelecimento pertencente a UF igual a selecionada na opção acima   ou   Estabelecimento pertencente a qualquer UF caso a opção *Todas as UFs* seja selecionada. - Estabelecimentos que possuam relatórios gerados para o período e obrigação fiscal informados em tela. |  |


---

|  | Aliq ICMS | ICMS | BASE 1 | BASE 2 | BASE 3 | BASE 4 |
| --- | --- | --- | --- | --- | --- | --- |
| Item 1 (cfop 5101) | 0,00 | 0,00 | 0,00 | 100,00 | 0,00 | 0,00 |
| Item 2 (cfop 5101) | 10,00 | 8,00 | 80,00 | 20,00 | 0,00 | 0,00 |
| Item 3 (cfop 5101) | 12,00 | 48,00 | 400,00 | 0,00 | 0,00 | 0,00 |


---

| CFOP | ICMS / IPI | Cod | Base de Cálculo | Alíquota | Imposto Creditado |
| --- | --- | --- | --- | --- | --- |
| 5101 | ICMS | 1 | 80,00 | 10,00 | 8,00 |
| 5101 | ICMS | 1 | 400,00 | 12,00 | 48,00 |
| 5101 | ICMS | 2 | 120,00 |  |  |


---

| Parâmetro | Regra |
| --- | --- |
| 5 – Emite Documento Cancelado | -- Testa notas de Serviço canceladas --  IF (Param ('UTILIZ_NF_CANC') = 'N' and Param('NF_SERVICO') = 'N') AND pCapaNF.SITUACAO = 'S' AND pCapaNF.COD_CLASS_DOC_FIS = '2' THEN       return false;     END IF; |
| 6 – Observação Redução Base Cálculo | Esse parâmetro se aplica ao Resumo da Observação.  Se marcado, é atribuída uma observação às notas fiscais que tenham Base Reduzida de ICMS, demonstrando o valor da base reduzida de ICMS. Observação: “Redução de R$9999,99 na Base do ICMS. Onde R$9999,99 é o valor da base reduzida |
| 7 – ICMS Retido compõe o valor operação outras | Este parâmetro se aplica a Base Outras de ICMS demonstrada na Parte Principal, nos Resumos p/ Decêndio, p/ Quinzena, p/ UF  e p/ CFOP.  Caso seja selecionado, o Valor do ICMS-ST será somado à Base Outras de ICMS, nas seguintes condições: - Se o campo Apropria ICMS-ST da NF estiver marcado e o parâmetro 25 dos Parâmetros p/ UF do módulo ICMS desmarcado.  - Se o campo Apropria ICMS-ST da NF estiver desmarcado e o parâmetro 26 dos Parâmetros p/ UF do módulo ICMS desmarcado.  Parâmetros p/ UF do módulo ICMS:  Quando os parâmetros 25 e 26 são marcados, o valor do ICMS-ST é demonstrado no Resumo da Observação e não irá compor a Base Outras de ICMS. |
| 8 – Observação de Diferencial de Aliquota | Este parâmetro se aplica ao Resumo da Observação. Caso o item de mercadoria tenha valor de Dif. Alíquota ICMS maior que zero, uma observação é gerada no Resumo da observação: “Dif de Aliquota - R$'|| VLR_DIF_ALIQ_W Onde  VLR_DIF_ALIQ_W := (VLR_TOT_NOTA - VLR_TRIBUTO_ICMSS) * DIF_ALIQ_TRIB_ICMS)/100; |
| 11 – Emite NF de Serviço | Se parâmetro marcado então: Nota fiscal de serviço é considerada na Parte Principal, desde que os critérios abaixo sejam atendidos: - classificação = '2' - tenha item de serviço - CFOP do item de serviço parametrizado no Módulo ICMS, Menu: Manutenção >> Parâmetros para Serviços de NFs Conjugadas >>  CFOP para itens de serviço conforme Ajuste SINIEF |
| 17 – Créditos/Débitos RN |  |
| 22 – Observações Fixas por UF/CFOP (P1/P2) |  |
| 25 - Lançar ICMS-ST com crédito nas OBS (P2/P2A) | Se parâmetro for marcado, o valor do ICMS-ST quando Apropriado, é lançado no Resumo da Observação e não na parte principal. |
| 26 - Lançar ICMS-ST sem crédito nas OBS (P2/P2A) | Se parâmetro for marcado, o valor do ICMS-ST quando Não Apropriado, é lançado no Resumo da Observação e não na parte principal. |
| 29- Observação Capa/Item (P1/P2) | Se esta opção for selecionada as observações de ICMS, ICMS-ST e IPI constantes na Capa do Documento Fiscal (SAFX07 – itens 37, 41 e 49) são apresentadas no Resumo da Observação. |
| 43 – Observações para Faturamento Direto ao Consumidor (P2/P2A) |  |
| 44 – Cálculo do ICMS c/ base na Resolução SEFCON n 4055 | Zera Alíquota do ICMS, Valor do ICMS e bases tributada, isenta e outras de ICMS. |
|  |  |
|  |  |
|  |  |
|  |  |


---

| Situação | Regra |
| --- | --- |
| Nota Cancelada | Zera valor contábil, ICMS, Alíquota       pItem.VLR_CONTAB_ITEM    := 0;         pItem.VLR_BASE_ICMS_1    := 0;         pItem.VLR_BASE_ICMS_2    := 0;         pItem.VLR_BASE_ICMS_3    := 0;         pItem.ALIQ_TRIBUTO_ICMS  := 0;         pItem.VLR_TRIBUTO_ICMS   := 0;         pItem.COD_CFO            := null; |
| Transferência de Crédito de ICMS | Zera valor contábil,     	 pItem.VLR_CONTAB_ITEM    := 0;           pItem.VLR_BASE_ICMS_1    := 0;           pItem.VLR_BASE_ICMS_2    := 0;           pItem.VLR_BASE_ICMS_3    := 0;           pItem.ALIQ_TRIBUTO_ICMS  := 0;           pItem.VLR_TRIBUTO_ICMS   := 0; |
|  |  |
