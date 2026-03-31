---
source: "MTZ-Report_Fiscal-Inf-Compl-Oper-ST-SAFX296_XLS.docx"
category: Report_Fiscal
converted: auto
---

# Report Fiscal

# Relatório de Informações Complementares das Operações Sujeitas ao ST (SPED-EFD - C180, C185 e C380) – Formato XLS

**Localização:**
Módulo: Básicos  Report Fiscal
Menu: Menu: Obrigações Acessórias  ICMS por Substituição  Operações com Substituição Tributária  Inf. Compl. Operações Sujeitas ao ST (SPED-EFD - C180, C185 e C380) – Formato XLS




# DOCUMENTO DE REQUISITO



# REGRAS DE NEGÓCIO




Considerações deste modelo:

**Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**


**Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**



---

| DR | Nome | Descrição |
| --- | --- | --- |
| MFS43551 | Andréa Rocha | Criação do relatório das Informações Complementares Complementares das Operações Sujeitas ao ST (SPED-EFD - C180, C185 e C380) – Formato XLS. O objetivo é gerar um relatório para apoio à geração do Ressarcimento do ICMS-ST de MG. |
| MFS566365 | Andréa Rocha | Inclusão de um parâmetro para definir se serão geradas as colunas de valores totais no arquivo. |


---

| Cód. | Descrição | MFS |
| --- | --- | --- |
| RN00 | Parâmetros de tela:  [MFS566365] Inclusão do parâmetro para indicar se serão geradas as colunas de valores totais  - Data Inicial: campo do tipo data no formato DD/MM/AAAA.  - Data Final: campo do tipo data no formato DD/MM/AAAA.  - Gerar as Colunas de Valores Totais: campo do tipo checkbox, default desmarcado.   - UF: campo do tipo listbox que exibirá todas as UFs da tabela Estado mais a opção “Todas”.  - Estabelecimentos: Neste campo será exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário. Incluir botão “Selecionar” para seleção de estabelecimento e o botão “Marcar Todos” caso o usuário queira marcar todos os estabelecimentos. | MFS43551 MFS566365 |
| RN01 | Regra geral - Critérios para a recuperação dos dados:  Para a geração deste relatório serão filtradas as Informações Complementares Complementares das Operações Sujeitas ao ST e os documentos fiscais relacionados.  - Origem dos dados: Tabelas de Documentos Fiscais, Informações Complementares Complementares das Operações Sujeitas ao ST e Produto (SAFX07, SAFX296 e SAFX2013);  - Período para seleção, será considerada a data fiscal (campo DATA_FISCAL da SAFX296).  Serão demonstradas todas as colunas da tabela SAFX296, ordenadas por empresa, estabelecimento, data fiscal, número e série do documento fiscal, número do item.  E também serão acrescentadas as colunas da tabela de Chave de Acesso da NF-Eletrônica (SAFX07) e descrição do produto (SAFX2013). | MFS43551 |
| RN02 | Layout do Relatório    O relatório não terá opção de impressão, ele somente terá a opção de salvar em excel.  Os campos abaixo serão mostrados no excel: | MFS43551 |


---

| Empresa | Empresa da geração |
| --- | --- |
| Estabelecimento | Estabelecimento da geração |
| CPF_CGC do estabelecimento | CPF_CGC da tabela Estabelecimento |
| Razão social do estabelecimento | Razão social da tabela Estabelecimento |
| Data Fiscal | Data fiscal (campo 03 da SAFX296) |
| Tipo de Movimento | Movimento Entrada/Saída (campo 04 da SAFX296) |
| Normal ou Devolução | Normal ou Devolução (campo 05 da SAFX296) |
| Tipo de documento | Tipo de documento (campo 06 da SAFX296) |
| Ind./Código Pessoa Fis/Jur | Indicador e Código da Pessoa Física/Jurídica (campos 01 e 02 da SAFX04) |
| CPF_CGC Pessoa Fis/Jur | CPF_CGC (campo 06 da SAFX04) |
| Razão social da Pessoa Fis/Jur | Razão Social (campo 06 da SAFX04) |
| Número da NF | Número do Documento Fiscal (campo 09 da SAFX296) |
| Série da NF | Série do Documento Fiscal (campo 10 da SAFX296) |
| Subsérie da NF | Subsérie do Documento Fiscal (campo 11 da SAFX296) |
| Chave NF-e | Chave de Acesso da NF-Eletrônica (campo 226 da SAFX07) |
| Item | Número do item (campo 15 da SAFX296) |
| Código do Produto | Indicador e Código do Produto (campos 12 e 13 da SAFX296) |
| Descrição do Produto | Descrição do Produto (campo 04 da SAFX2013) |
| Unid. Padrão | Unidade Padrão (campo 14 da SAFX296) |
| Qtde Convertida | Quantidade Convertida (campo 16 da SAFX296) |
| Unid. Medida | Unidade Medida (campo 17 da SAFX296) |
| Vlr Unit. Conv. | Valor Unitário Conv. (campo 18 da SAFX296) |
| Vlr Unit. ICMS Conv. | Valor Unitário ICMS Conv. (campo 19 da SAFX296) |
| Resp. Ret. (Ent) | Responsável Retenção (Entradas) (campo 20 da SAFX296) |
| Vlr BC ICMS-ST Conv. (Ent.) | Valor Unitário BC ICMS-ST Conv. (Entradas) (campo 21 da SAFX296) |
| Vlr ICMS-ST Conv. (Ent.) | Valor Unitário ICMS-ST Conv. (campo 22 da SAFX296) |
| Vlr FCP-ST Conv. (Ent.) | Valor Unitário FCP-ST Conv. (campo 23 da SAFX296) |
| Cód. Mot (Saída) | Código Motivo (Saídas) (campo 24 da SAFX296) |
| Vlr ICMS Oper Conv. (Saída) | Valor Unitário ICMS na Oper. Conv. (Saídas) (campo 25 da SAFX296) |
| Vlr ICMS Estq Conv. (Saída) | Valor Unitário ICMS Estoque Conv. (Saídas) (campo 26 da SAFX296) |
| Vlr ICMS-ST Estq Conv. (Saída) | Valor Unitário ICMS-ST Estoque Conv. (Saídas) (campo 27 da SAFX296) |
| Vlr FCP-ST Estq Conv. (Saída) | Valor Unitário FCP-ST Estoque Conv. (Saídas) (campo 28 da SAFX296) |
| Vlr ICMS-ST Conv. Rest. (Saída) | Valor Unitário ICMS-ST Conv. Rest. (Saídas) (campo 29 da SAFX296) |
| Vlr FCP-ST Conv. Rest. (Saída) | Valor Unitário FCP-ST Conv. Rest. (Saídas) (campo 30 da SAFX296) |
| Vlr ICMS-ST Conv. Compl. (Saída) | Valor Unitário ICMS-ST Conv. Compl. (Saídas) (campo 31 da SAFX296) |
| Vlr FCP-ST Conv. Compl. (Saída) | Valor Unitário FCP-ST Conv. Compl. (Saídas) (campo 32 da SAFX296) |
| Vlr Item | [MFS566365] Inclusão das colunas de valores totais de acordo com o parâmetro de tela  Se o parâmetro “Gerar as Colunas de Valores Totais” estiver marcado       Valor Unitário Conv. (campo 18 da SAFX296) * Quantidade Convertida (campo 16 da SAFX296) Senão         Essa coluna não deve ser gerada no arquivo. |
| Vlr ICMS Devido | [MFS566365] Inclusão das colunas de valores totais de acordo com o parâmetro de tela  Se o parâmetro “Gerar as Colunas de Valores Totais” estiver marcado      Valor Unitário ICMS Conv. (campo 19 da SAFX296) * Quantidade Convertida (campo 16 da SAFX296) Senão         Essa coluna não deve ser gerada no arquivo. |
| Vlr ICMS Pago | [MFS566365] Inclusão das colunas de valores totais de acordo com o parâmetro de tela  Se o parâmetro “Gerar as Colunas de Valores Totais” estiver marcado      (Valor Unitário ICMS Estoque Conv. (Saídas) (campo 26 da SAFX296) + Valor Unitário ICMS-ST Estoque        Conv. (Saídas) (campo 27 da SAFX296) + Vlr FCP-ST Estq Conv. (Saída) (campo 28 da        SAFX296)) * Quantidade Convertida (campo 16 da SAFX296) Senão         Essa coluna não deve ser gerada no arquivo. |
| Vlr Restituição | [MFS566365] Inclusão das colunas de valores totais de acordo com o parâmetro de tela  Se o parâmetro “Gerar as Colunas de Valores Totais” estiver marcado      (Valor Unitário ICMS-ST Conv. Rest. (Saídas) (campo 29 da SAFX296) + Valor Unitário FCP-ST Conv.        Rest. (Saídas) (campo 30 da SAFX296)) * Quantidade Convertida (campo       16 da SAFX296) Senão         Essa coluna não deve ser gerada no arquivo. |
| Vlr Complemento | [MFS566365] Inclusão das colunas de valores totais de acordo com o parâmetro de tela  Se o parâmetro “Gerar as Colunas de Valores Totais” estiver marcado      (Valor Unitário ICMS-ST Conv. Compl. (Saídas) (campo 31 da SAFX296) + Valor Unitário FCP-ST Conv.       Compl. (Saídas) (campo 32 da SAFX296)) * Quantidade Convertida (campo 16 da SAFX296) Senão         Essa coluna não deve ser gerada no arquivo. |
| Alíquota Interna | [MFS566365] Inclusão das colunas de valores totais de acordo com o parâmetro de tela  Se o parâmetro “Gerar as Colunas de Valores Totais” estiver marcado       (Coluna Vlr ICMS Devido / Coluna Vlr Item) * 100 Senão         Essa coluna não deve ser gerada no arquivo.  Obs.: Mostrar a coluna alíquota com 2 casas decimais. |


---

| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |



---

| RN01 | [ALTERADA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |

