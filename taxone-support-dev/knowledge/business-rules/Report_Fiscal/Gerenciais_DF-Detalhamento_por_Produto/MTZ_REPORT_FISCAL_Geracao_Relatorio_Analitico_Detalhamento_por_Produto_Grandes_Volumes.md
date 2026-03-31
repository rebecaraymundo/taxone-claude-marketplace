---
source: "MTZ_REPORT_FISCAL_Geracao_Relatorio_Analitico_Detalhamento_por_Produto_Grandes_Volumes.docx"
category: Report_Fiscal
converted: auto
---





THOMSON REUTERS

Relatório Analítico – Detalhamento por Produto (Grandes Volumes)
Geração do Detalhamento por Produto

Localização: Básicos > Report Fiscal
Menu: Gerenciais > Documento Fiscais > Analíticos > Detalhamento por Produto (Grandes Volumes)


DOCUMENTO DE REQUISITO



REGRAS DE NEGÓCIO




Considerações deste modelo:

**Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**




---

| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS4310 | Lara Aline | Este documento tem o objetivo de incluir os campos: IPI Isentas, IPI Outras, Base ICMSS e alterar a regra do campo Base IPI. |
| MFS14922 | João Henrique | Inclusão do campo de Código de Tributação IPI no relatório. |
| MFS-71662 | Rogério Ohashi | Inclusão dos campos Valor Base INSS, Valor Alíquota INSS e Valor de INSS Retido no relatório. |
| MFS-70186 | Andréa Rocha | Inclusão do campo Inscrição Estadual Substituto Tributário no relatório. |


---

| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN00 | Regra Geral de Seleção  A geração do relatório será de acordo com os critérios de filtro informados na tela de geração.  Origem das informações: Manter o mesmo tratamento atual do relatório normal e de via servidor, ou seja, recuperação de nota fiscal de entrada e saída pela SAFX07/08 e parametrizações comuns e obrigatórias para NF, sendo classificação fiscal 1, 3  e documento não cancelado.  Observação: Os três relatórios de Detalhamento por Produto são idênticos, mudando apenas a forma de salvar o arquivo. | MFS4310 |
| RN01 | Informações padrão do cabeçalho  As informações do cabeçalho do relatório serão geradas da seguinte forma:  Na parte superior do relatório, serão geradas as informações da Empresa selecionada, Data e Hora de emissão do relatório e Página do mesmo. No canto superior esquerdo do relatório, serão informados os dados do estabelecimento. O estabelecimento será informado de acordo com o Estabelecimento selecionado na tela geração e será informado através do Código e Descrição separados por um “-“, além disso, deverá apresentar o CNPJ e Inscrição Estadual (caso este esteja parametrizado). Na parte central superior será informada a “Data” do relatório. Essa informação irá exibir a data e hora que o relatório foi gerado. No canto direito será exibido o número da página do relatório, que deverá ser sequencial.  Na parte central do relatório, deverá ser exibido o título do mesmo. O título do relatório é “RELATÓRIO ANALÍTICO  - DETALHAMENTO POR PRODUTO”. Abaixo do título do relatório, deverá ser exibido no formato dd/mm/aaaa, o período de geração do relatório. Essa informação será recuperada do campo “Período”. | OS4774 |
| RN02 | Informações do corpo do relatório  O Relatório Analítico será exibido através dos seguintes campos: | OS4774 CH13715_2015 MFS_3582 MFS4310 MFS14922 MFS70186 |
|  |  |  |


---

| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |

