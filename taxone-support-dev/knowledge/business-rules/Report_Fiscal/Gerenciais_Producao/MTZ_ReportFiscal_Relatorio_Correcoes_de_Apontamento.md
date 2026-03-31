---
source: "MTZ_ReportFiscal_Relatorio_Correcoes_de_Apontamento.docx"
category: Report_Fiscal
converted: auto
---





THOMSON REUTERS

Módulo Report Fiscal – Relatório das Correções de Apontamento


Localização  Menu: Básicos, Módulo: Report Fiscal, menu Gerenciais  Produção  Correções de Apontamento


DOCUMENTO DE REQUISITO








Sumário

**1.	Parâmetros da Tela	2**
2.	Origem e Recuperação dos Dados	4
3.	Processamento	5
4.	Layout e Preenchimento dos Dados no Relatório	5























# Parâmetros da Tela











# Origem e Recuperação dos Dados


Origem dos Dados: Tabela das Correções de Apontamento da EFD - Bloco K (SAFX235);
Tabela de Itens das Correções de Apontamento da EFD – Bloco K (SAFX236);

A partir dos parâmetros informados em tela, serão recuperados os dados de todas as correções de apontamento (SAFX235), e seus respectivos itens (SAFX236), que atendam aos seguintes critérios:

- Código da Empresa – Empresa do login;
- Código do Estabelecimento – Estabelecimento selecionado em tela;
- Período de Referência – Período informado em tela:
- Tipo da Correção – Tipo da correção informado em tela;
- Indicador e Código do Produto – Quando o campo “Produto” for informado na tela dos parâmetros, serão consideradas apenas as correções do
produto informado. Quando o campo não for preenchido, serão consideradas todas as correções do período
e tipo informados, independente do produto.

Observar que a existência de itens para uma correção não é obrigatória. Desta forma, poderão existir correções sem itens na tabela “filha” (SAXF236).


# Processamento

Para cada correção de apontamento recuperada (SAFX235), os dados serão impressos da seguinte forma:

- Uma linha com as informações da correção (SAFX235);
- Abaixo, serão impressos os dados de todos os itens da correção (SAFX236), quando existirem itens;

A exceção é para as correções do tipo “1” (Estoque Escriturado”), onde só existem dados na SAFX235, ou seja, este tipo de correção não tem itens.


# Layout e Preenchimento dos Dados no Relatório

Ver layout do relatório na planilha anexa “Layout_Relatorio_Correcoes_de_Apontamento”.

Este relatório trabalha com três tipos de layout, dependendo do tipo de correção escolhido, da seguinte forma:

- Tipo de correção = “1-Correção de apontamento de Estoque Escriturado (K200)”  layout da aba “Estoque Escriturado”;

- Tipo de correção = “3-Correção de apontamento de Movimentação Interna (K220)”  layout da aba “Movimentação Interna”;

- Tipos de correção = 2, 4, 5 ou 6  layout da aba “Outros Tipos”;


**Ordenação dos dados**

A ordenação dos dados para apresentação no relatório dependerá do tipo de layout:

- Para as correções do tipo “1” (layout da aba “Estoque Escriturado”), os dados serão ordenados por:

Data do Estoque Final, Indicador e Código do Produto;

(lembrando que as correções do tipo “1” não têm itens)

- Para as correções do tipo “3” (layout da aba “Movimentação Interna”), os dados serão ordenados por:

Dados da correção (SAFX235)  Data final do período de apuração do erro, Indicador e Código do Produto;
Dados dos itens (SAFX236)  Para cada registro “pai”, os itens serão ordenados por Indicador e Código do Produto;

- Para as correções do tipo “2”, “4”, “5” ou “6” (layout da aba “Outros Tipos”), os dados serão ordenados por:

Dados da correção (SAFX235)  Data final do período de apuração do erro, Código da Ordem de Produção, Código Diferenciador
da Produção, Indicador e Código do Produto;
Dados dos itens (SAFX236)  Para cada registro “pai”, os itens serão ordenados por Indicador e Código do Produto;


**Segue detalhamento sobre o preenchimento dos dados para cada tipo de layout:**


**Linhas de cabeçalho:**

(o cabeçalho é igual para todos os layout’s)




A seguir serão definidas as linhas separadamente por tipo do layout:


**Layout “Estoque Escriturado”**

**Linha de detalhe da correção:**



**Layout “Movimentação Interna”**


**Linha de detalhe da correção:**




**Linha de detalhe dos itens da correção:**


Esta linha demonstra os itens da correção em questão.

Quando não existirem itens na SAFX236, esta linha não será impressa.




**Layout “Outros Tipos”**


**Linha de detalhe da correção:**




**Linha de detalhe dos itens da correção:**


Esta linha demonstra os itens da correção em questão.

Quando não existirem itens na SAFX236, esta linha não será impressa.




**Linha de detalhe do insumo substituído:**


Esta linha será impressa apenas quando o item em questão tiver a informação do insumo substituído. Ou seja, quando não existir informação nos campos 20 e 21 da SAFX236, esta linha não será impressa.






= = = = = =


---

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS6571 | Relatório das Correções de Apontamento | Criação do relatório para conferência dos dados da SAFX235/SAFX236 (Correções de Apontamento) | 18/11/2016 (criação do documento) |


---

| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | N | Listbox | Este campo é uma lista com a relação de todos os estabelecimentos da empresa do login, exibindo o código e a razão social dos estabelecimentos. Quando o estabelecimento for informado no login, o campo exibirá como default o estabelecimento informado. |  |
| Período (mês/ano) | Mês/Ano | S | S | (MM/AAAA) | Neste campo o usuário informará o período de referência para geração do relatório, no formato Mês/Ano (MM/AAAA).  Após o usuário informar o Estabelecimento e o Período, será feita a identificação do Grupo de Relacionamento a ser utilizado no campo “Produto”. O Grupo obtido será exibido no campo que aparece antes da “pastinha” de seleção dos produtos. |  |
| Tipo da Correção | Alfanumérico | S | N | Listbox | Este campo é uma lista com as seguintes opções:  1-Correção de apontamento de Estoque Escriturado (K200) 2-Correção de apontamento de Desmontagem (K210/K215) 3-Correção de apontamento de Movimentação Interna (K220) 4-Correção de apontamento de Produção Própria (K230/K235) 5-Correção de apontamento de Produção de Terceiros (K250/K255) 6-Correção de apontamento de Reprocessamento / Reparo (K260/K265)  São exatamente as opções do campo “04 -Tipo da Correção” da SAFX235. |  |
| Produto | Alfanumérico | N | S |  | Neste campo o usuário poderá informar um produto especifico para emissão do relatório.  O campo trabalha com janela de seleção dos produtos da SAFX2013, considerando apenas os produtos do Grupo de Relacionamento referente ao Estabelecimento e Período informados. O campo só será habilitado após o usuário informar o Estabelecimento e o Período.  Quando a informação for digitada, será validada a existência do produto na SAFX2013, considerando o Grupo a ser utilizado. |  |


---

| Primeira linha do cabeçalho | A primeira linha do cabeçalho demonstra a razão social da empresa, a data de emissão do relatório e o número da página. |
| --- | --- |
| Segunda linha do cabeçalho | Campo “Filial” = será preenchido com o código e a razão social do estabelecimento em questão. Campo “Inscrição Estadual” = será preenchido com a inscrição estadual do estabelecimento em questão (inscrição na sua própria UF) Campo “CNPJ” = será preenchido com o CNPJ do estabelecimento em questão. |
| Terceira linha do cabeçalho | Nesta linha será exibido o título do relatório, e o período solicitado em tela para a sua emissão, conforme o exemplo:   “Relatório de Conferência das Correções de Apontamento – XXXXXXXXXXXXXXXXXXXXXXXXX – Período: XXX/99”  Onde “XXXXXXXXXXXXXXXXXXXXX” depende do tipo de correção selecionado na tela da geração, conforme lista abaixo, e “XXX/99” é o mês e ano do período informado para geração.   Se tipo de correção = “1”, será impresso “Estoque Escriturado”; Se tipo de correção = “2”, será impresso “Desmontagem”; Se tipo de correção = “3”, será impresso “Movimentação Interna”; Se tipo de correção = “4”, será impresso “Produção Própria”; Se tipo de correção = “5”, será impresso “Produção de Terceiros”; Se tipo de correção = “6”, será impresso “Reprocessamento/Reparo”; |


---

| Dt. Estoque Final | Campo “11-Data do Estoque Final” da SAFX235 |
| --- | --- |
| Produto | Este campo será preenchido com a concatenação dos campos  “5-Indicador do Produto” e “06-Código do Produto” da SAFX235, e a descrição do produto na SAFX2013, no formato:  “X-XXXXXXXXXXXXXXXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX” |
| Grupo Contagem | O preenchimento deste campo depende do campo “12-Grupo de Contagem” da SAFX235, da seguinte forma:   Se campo “12-Grupo de Contagem” = “1”, será impresso “Estoque Próprio no Estab.”; Se campo “12-Grupo de Contagem” = “2”, será impresso “Estoque Próprio em Terceiros”; Se campo “12-Grupo de Contagem” = “3”, será impresso “Estoque de Terceiros no Estab.”; Se campo “12-Grupo de Contagem” = “5”, será impresso “Estoque em Depósito Fechado”; |
| Qtd. Correção | Campo “16-Quantidade da Correção” da SAFX235 |
| Pos./Neg. | O preenchimento deste campo depende do campo “17- Correção Positiva / Negativa” da SAFX235, da seguinte forma:  Se campo “17- Correção Positiva / Negativa” = “1”, será impresso “P”; Se campo “17- Correção Positiva / Negativa” = “2”, será impresso “N”;   Quando o campo “16-Quantidade da Correção” for = zeros (ou nulo), este campo ficará em branco. |
| Unidade | Este campo será preenchido com o código da unidade de medida referente ao campo “15-Unidade de Medida” da SAFX235. |
| Insc.Estadual-AM | Campo “18-Inscrição Estadual – AM” da SAFX235 |
| Pessoa Fis./Jur. | Este campo será preenchido com a concatenação dos campos “13-Indicador da Pessoa Fis/Jur” e “14-Código da Pessoa Fis/Jur” da SAFX235, no formato: “X-XXXXXXXXXXXXXXXXXXXXX” |


---

| Período Apur. do Erro | Este campo será preenchido com a informação dos campos “07-Data Inicial do Período de Apuração” e “08-Data Final do Período de Apuração” da SAFX235. |
| --- | --- |
| Produto Origem | Este campo será preenchido com a concatenação dos campos  “5-Indicador do Produto” e “06-Código do Produto” da SAFX235, e a descrição do produto na SAFX2013, no formato:  “X-XXXXXXXXXXXXXXXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX” |
| Insc.Estadual-AM | Campo “18-Inscrição Estadual – AM” da SAFX235 |
| Qtd. Correção | Campo “16-Quantidade da Correção” da SAFX235 |
| Pos./Neg. | O preenchimento deste campo depende do campo “17- Correção Positiva / Negativa” da SAFX235, da seguinte forma:  Se campo “17- Correção Positiva / Negativa” = “1”, será impresso “P”; Se campo “17- Correção Positiva / Negativa” = “2”, será impresso “N”;   Quando o campo “16-Quantidade da Correção” for = zeros (ou nulo), este campo ficará em branco. |
| UM | Este campo será preenchido com o código da unidade de medida referente ao campo “15-Unidade de Medida” da SAFX235. |


---

| Produto Destino | Este campo será preenchido com a concatenação dos campos  “15- Indicador do Produto (Componente/Insumo)” e “16- Código do Produto (Componente/Insumo)” da SAFX236, e a descrição do produto na SAFX2013, no formato:  “X-XXXXXXXXXXXXXXXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX” |
| --- | --- |
| Qtd. Correção | Campo “18-Quantidade da Correção” da SAFX236 |
| Pos./Neg. | O preenchimento deste campo depende do campo “19- Correção Positiva / Negativa” da SAFX236, da seguinte forma:  Se campo “19- Correção Positiva / Negativa” = “1”, será impresso “P”; Se campo “19- Correção Positiva / Negativa” = “2”, será impresso “N”;   Quando o campo “18-Quantidade da Correção” for = zeros (ou nulo), este campo ficará em branco. |
| UM | Este campo será preenchido com o código da unidade de medida referente ao campo “17-Unidade de Medida” da SAFX236. |


---

| Período Apur. do Erro | Este campo será preenchido com a informação dos campos “07-Data Inicial do Período de Apuração” e “08-Data Final do Período de Apuração” da SAFX235. |
| --- | --- |
| Cód. OP/OS | Campo “09- Código da Ordem de Produção/Serviço” da SAFX235. |
| Cód. Dif. Produção | Campo “10- Cód. Diferenciador de Produção” da SAFX235. |
| Produto | Este campo será preenchido com a concatenação dos campos  “5-Indicador do Produto” e “06-Código do Produto” da SAFX235, e a descrição do produto na SAFX2013, no formato:  “X-XXXXXXXXXXXXXXXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX” |
| Insc.Estadual-AM | Campo “18-Inscrição Estadual – AM” da SAFX235 |
| Qtd. Correção | Campo “16-Quantidade da Correção” da SAFX235 |
| Pos./Neg. | O preenchimento deste campo depende do campo “17- Correção Positiva / Negativa” da SAFX235, da seguinte forma:  Se campo “17- Correção Positiva / Negativa” = “1”, será impresso “P”; Se campo “17- Correção Positiva / Negativa” = “2”, será impresso “N”;   Quando o campo “16-Quantidade da Correção” for = zeros (ou nulo), este campo ficará em branco. |
| UM | Este campo será preenchido com o código da unidade de medida referente ao campo “15-Unidade de Medida” da SAFX235 . |


---

| Componente / Insumo | Este campo será preenchido com a concatenação dos campos  “15- Indicador do Produto (Componente/Insumo)” e “16- Código do Produto (Componente/Insumo)” da SAFX236, e a descrição do produto na SAFX2013, no formato:  “X-XXXXXXXXXXXXXXXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX” |
| --- | --- |
| Qtd. Correção | Campo “18-Quantidade da Correção” da SAFX236 |
| Pos./Neg. | O preenchimento deste campo depende do campo “19- Correção Positiva / Negativa” da SAFX236, da seguinte forma:  Se campo “19- Correção Positiva / Negativa” = “1”, será impresso “P”; Se campo “19- Correção Positiva / Negativa” = “2”, será impresso “N”;   Quando o campo “18-Quantidade da Correção” for = zeros (ou nulo), este campo ficará em branco. |
| UM | Este campo será preenchido com o código da unidade de medida referente ao campo “17-Unidade de Medida” da SAFX236. |


---

| Insumo Substituído | Este campo será preenchido com a concatenação dos campos “20-Indicador do Insumo Substituído” e “21-Código do Insumo Substituído” da SAFX236, e a descrição do produto na SAFX2013, no formato:  “X-XXXXXXXXXXXXXXXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX” |
| --- | --- |

