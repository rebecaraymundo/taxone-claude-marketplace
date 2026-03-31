# MTZ_ReportFiscal_Relatorio_Diario_Exportacao_Dados

- **Fonte:** MTZ_ReportFiscal_Relatorio_Diario_Exportacao_Dados.docx
- **Modificado:** 2020-12-02
- **Tamanho:** 71 KB

---

<a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>

THOMSON REUTERS

Módulo Report Fiscal e SPED/ECD – Escrituração Contábil Fiscal

Relatório Diário \(Exportação dos Dados\)

__Localização__: Menu Básicos à Report Fiscal, item de menu Gerenciais à Contábil à Geral à Diário \(Exportação dos Dados 

__Localização__: Menu Sped à ECD – Escrituração Contábil Digital, item de menu Relatórios à  Diário \(Exportação dos Dados 

__    Obs\.: Este item de menu só está disponível no TAX ONE\.__

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS39406

Andréa Rocha

Inclusão de 6 colunas novas no relatório diário\.

MFS\-43760

Alessandra Cristina Navatta

Disponibilizar este relatório também no Menu Relatórios do Sped Contábil

Sumário

[1\.	REGRAS DE GERAÇÃO DO RELATÓRIO	3](#_Toc48818693)

# <a id="_Toc427766287"></a><a id="_Toc453687763"></a><a id="_Toc48818693"></a>REGRAS DE GERAÇÃO DO RELATÓRIO 

__Origem das informações para geração:__ 

Para geração deste relatório, serão consideradas informações da seguinte tabela:

- __SAFX01 __\- Tabela de Arquivo Contábil; 

Obs\.: O relatório não será gerado em formato para impressão, será gerado um arquivo no formato CSV\.

__Campo/Coluna__

__Tipo__

__Formato/Default__

__Regra__

__MFS/CH__

Número do Lançamento

Texto

Campo 16\-Número do Lançamento da SAFX01\.

MFS39406

Tipo de Lançamento

Texto

Campo 17\-Tipo de Lançamento da SAFX01\.

MFS39406

Data de Lançamento Extemporâneo

Data

Formato: DD/MM/AAAA

Campo 32\-Data de Lançamento Extemporâneo da SAFX01\.

MFS39406

Operação com Participante Vinculado \- Indicador e Código da Pessoa Física/Jurídica

Texto

Campo 18\- Indicador da Pessoa Física/Jurídica e Código da Pessoa Física/Jurídica \- Operação com Participante Vinculado da SAFX01\.

MFS39406

Razão Social

Texto

Campo 05\- Razão Social da SAFX04 referente a PFJ \- Operação com Participante Vinculado da SAFX01\.

MFS39406

Data \- Operação com Participante Vinculado

Data

Formato: DD/MM/AAAA

Campo 04\-Início Validade da SAFX39 referente a PFJ \- Operação com Participante Vinculado da SAFX01\.

MFS39406

