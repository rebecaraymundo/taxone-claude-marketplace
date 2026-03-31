---
source: "MTZ_ReportFiscal_Relatorio_Diario_Exportacao_Dados.docx"
category: Report_Fiscal
converted: auto
---





THOMSON REUTERS

Módulo Report Fiscal e SPED/ECD – Escrituração Contábil Fiscal

Relatório Diário (Exportação dos Dados)

Localização: Menu Básicos à Report Fiscal, item de menu Gerenciais à Contábil à Geral à Diário (Exportação dos Dados

Localização: Menu Sped à ECD – Escrituração Contábil Digital, item de menu Relatórios à  Diário (Exportação dos Dados


**Obs.: Este item de menu só está disponível no TAX ONE.**

DOCUMENTO DE REQUISITO


Sumário

**1.	REGRAS DE GERAÇÃO DO RELATÓRIO	3**

# REGRAS DE GERAÇÃO DO RELATÓRIO

**Origem das informações para geração:**

Para geração deste relatório, serão consideradas informações da seguinte tabela:

SAFX01 - Tabela de Arquivo Contábil;

Obs.: O relatório não será gerado em formato para impressão, será gerado um arquivo no formato CSV.







---

| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS39406 | Andréa Rocha | Inclusão de 6 colunas novas no relatório diário. |
| MFS-43760 | Alessandra Cristina Navatta | Disponibilizar este relatório também no Menu Relatórios do Sped Contábil |


---

| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Número do Lançamento | Texto |  | Campo 16-Número do Lançamento da SAFX01. | MFS39406 |
| Tipo de Lançamento | Texto |  | Campo 17-Tipo de Lançamento da SAFX01. | MFS39406 |
| Data de Lançamento Extemporâneo | Data | Formato: DD/MM/AAAA | Campo 32-Data de Lançamento Extemporâneo da SAFX01. | MFS39406 |
| Operação com Participante Vinculado - Indicador e Código da Pessoa Física/Jurídica | Texto |  | Campo 18- Indicador da Pessoa Física/Jurídica e Código da Pessoa Física/Jurídica - Operação com Participante Vinculado da SAFX01. | MFS39406 |
| Razão Social | Texto |  | Campo 05- Razão Social da SAFX04 referente a PFJ - Operação com Participante Vinculado da SAFX01. | MFS39406 |
| Data - Operação com Participante Vinculado | Data | Formato: DD/MM/AAAA | Campo 04-Início Validade da SAFX39 referente a PFJ - Operação com Participante Vinculado da SAFX01. | MFS39406 |
