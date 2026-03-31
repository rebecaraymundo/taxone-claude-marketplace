---
source: "MTZ_Relatorio_Vendas_SAT.docx"
category: Report_Fiscal
converted: auto
---






THOMSON REUTERS


Report Fiscal
Relatório Analítico Vendas Cupom SAT (Formato Padrão)




DOCUMENTO DE REQUISITO


Sumário

**1.	REGRAS DE GERAÇÃO DO RELATÓRIO	3**
1.1.	Layout do Relatório	7

# REGRAS DE GERAÇÃO DO RELATÓRIO

**Origem das informações para geração:**


Regra de seleção: Este relatório será gerado com base nas informações das tabelas SAFX201, SAFX202 e cadastro do Estabelecimento, considerando os parâmetros de período, estabelecimento e número do equipamento parametrizados na tela de geração do relatório. O usuário pode visualizar apenas documentos cancelados utilizando o checkbox “Somente Lançamentos Cancelados”.

Serão considerados os registros das tabelas SAFX201 e SAFX202, cuja data de emissão do cupom fiscal, compreenda o período parametrizado, considerando apenas os registros do estabelecimento indicado.

Alteração da MFS11117: Inclusão do parâmetro “Número do Equipamento SAT”:

Alteração da MFS17603: Inclusão do parâmetro “Somente Lançamentos Cancelados”. O campo não faz parte do corpo ou cabeçalho do relatório, mas ao marcar este novo parâmetro, o sistema apresenta na geração os documentos onde o campo: 07-Situação do Documento for igual a “02 – Documento Cancelado” da SAFX201.




Quando o parâmetro “Número do Equipamento SAT” for preenchido na tela de emissão do relatório (este parâmetro é de preenchimento não obrigatório), serão considerados apenas os movimentos em que o número do equipamento seja = equipamento informado (corresponde ao campo “03-Número do Equipamento” da SAFX201).

Ordenação do relatório: Número do Equipamento, Número do Cupom e Data de Emissão.
















## Layout do Relatório






---

| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS1932 | Jefferson Mota | Definição das regras do Relatório Analítico de Vendas Cupom SAT |  |
| MFS11117 | Vânia Mattos | Alteração do relatório das vendas com Cupom Fiscal SAT para inclusão de filtro por Número do Equipamento. | 10/08/2017 |
| MFS17603 | João Henrique | Alteração do relatório das vendas com Cupom Fiscal SAT para inclusão de filtro de documentos cancelados. | 26/11/2018 |
| MFS28723 | Aline Melo | Inclusão da coluna Item Produto/Serviço | 12/07/2019 |
|  |  |  |  |


---

| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Data | Data | Formato:  DD/MM/AA | Definições do campo.   Informar a Data atual, referente ao momento da geração do relatório. | MFS1932 |
| Página | Numérico |  | Este campo deve demonstrar o número da página atual. | MFS1932 |
| Empresa | Texto |  | Exibir o nome da empresa que acessou o módulo do Report Fiscal. | MFS1932 |
| Filial | Texto |  | Corresponde ao campo RAZAO_SOCIAL da tabela ESTABELECIMENTO, da empresa credenciada. | MFS1932 |
|  |  |  |  |  |
| CNPJ | Numérico |  | Exibir o CNPJ da tabela ESTABELECIMENTO, da empresa Credenciada que foi selecionada na tela de Critérios de Seleção. | MFS1932 |
|  |  |  |  |  |
| Período | Data | Formato:  DD/MM/AA | Corresponde ao período incial e ao período final, informados na tela de critérios da geração do relátório. | MFS1932 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Número Equipamento | Numérico |  | - Deverá exibir a informação do campo “NUM_EQUIP” da tabela SAFX201.   Obs.: Quando não houver a informação, deverá ficar em branco | MFS1932 |
| Número Cupom | Numérico |  | Nesta coluna deve exibir o valor do campo “NUM_CUPOM” da tabela SAFX201.   Obs.: Quando não houver a informação, deverá ficar em branco | MFS1932 |
| Data Emissão | Data | DD/MM/AAAA | Nesta coluna deve exibir a data de emissão do cupom fiscal, que é referente ao valor do campo “DATA_EMISSAO” da tabela SAFX201. | MFS1932 |
| CPF/CNPJ Cliente | Numérico |  | Neste campo, devemos exibir a informação do campo “CPF_CNPJ_CLIENTE” da tabela SAFX201. | MFS1932 |
| Item Produto/Serviço | Texto |  | Neste campo, devemos exibir a informação de acordo com a seguinte regra:  Preencher com o campo “COD_PRODUTO” da tabela SAFX202, caso esteja preenchido.  Senão, preencher com o campo “COD_SERVICO” da tabela SAFX202. | MFS28723 |
|  |  |  |  |  |
| CFOP | Numérico |  | Neste campo, devemos exibir a informação do campo “IDENT_CFO” da tabela SAFX202. | MFS1932 |
|  |  |  |  |  |
| Desconto | Numérico |  | Nesta coluna deve exibir o Valor do Desconto sobre o Item do campo “VLR_DESC” da tabela SAFX202. | MFS1932 |
| Acréscimos | Numérico |  | Nesta coluna deve exibir o Valor  de Acréscimo sobre o item do campo “VLR_ACRES” da tabela SAFX202. | MFS1932 |
| Líquido | Numérico |  | Nesta coluna deve exibir o valor final do item do campo “VLR_TOT_LIQ” da tabela SAFX202. | MFS1932 |
|  |  |  |  |  |
| Base | Numérico |  | Nesta coluna deve exibir os valores do campo “VLR_BASE_ICMS” da tabela SAFX202. | MFS1932 |
| Valor | Numérico |  | Nesta coluna deve exibir os valores do campo “VLR_ICMS” da tabela SAFX202. | MFS1932 |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
| Total do Dia dd/mm/aaaa | Numérico |  | Nesta linha, deve exibir o Total dos campos de Valores, por dia. | MFS1932 |
| Total Geral do Estabelecimento | Numérico |  | Nesta linha, deverá exibir o Total geral do Estabelecimento, dos campos de valores. | MFS1932 |
