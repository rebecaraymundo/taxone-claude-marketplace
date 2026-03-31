---
source: "MTZ-Report-Conferencia-Observacoes-da-NF.docx"
category: Report_Fiscal
converted: auto
---



THOMSON REUTERS

**Módulo Report Fiscal**

**Relatório de Conferência das Observações das Notas Fiscais**


Localização: Menu Básicos, Módulo Report Fiscal, item Operacionais  Conferência das Observações das Notas Fiscais



DOCUMENTO DE REQUISITO



















Sumário

**1.	Tela da Emissão do Relatório	3**
1.1	Layout	3
1.2	Regras	3
2.	Geração do Relatório	4
2.1	Origem dos Dados	4
2.2	Critérios de Seleção	5
2.3	Processamento	5
2.4	Ordenação	6
2.5	Preenchimento dos Dados	6
2.6	Layout do Relatório	6


# Tela da Emissão do Relatório

## Layout



## Regras



# Geração do Relatório

## Origem dos Dados

- Tabela da Capa dos Documentos Fiscais (SAFX07)
- Tabela das Observações do Documento Fiscal (SAFX112)
- Tabela dos Ajustes do Lançamento Fiscal (SAFX113)
- Tabela de Cadastro das Observações (SAFX2009)

## Critérios de Seleção

Critérios de recuperação dos documentos na SAFX07:

- COD_EMPRESA – Código da empresa do login

- COD_ESTAB – Estabelecimentos selecionados em tela, considerando:

No caso de geração por inscrição estadual única, serão considerados os documentos de
todos os estabelecimentos envolvidos na centralização (centralizador e centralizados);

No caso de geração por inscrição estadual do PIM-AM, serão considerados apenas os
documentos cujo campo “126-Inscrição Estadual” = inscrição seleciona em tela;

- DATA_FISCAL – Data fiscal que se enquadre no período informado em tela

- MOVTO_E_S – Dependendo do parâmetro “Tipo de Movimento” informado em tela:

Se = Entradas  apenas notas de entrada (MOVTO_E_S <> 9);
Se = Saídas apenas notas de saída (MOVTO_E_S = 9);
Se = Ambos  tanto entradas como saídas;

- SITUACAO – Dependendo do parâmetro “Considerar notas canceladas” informado em tela:

Se parâmetro desmarcado  as notas canceladas não serão consideradas;
Se parâmetro marcado  as notas canceladas também serão consideradas;

- Somente os documentos que tenham dados na SAFX112, considerando o parâmetro “Tipo de
Observação” informado em tela, da seguinte forma:

Se parâmetro = “Informações Complementares”  serão consideradas apenas as
observações da SAFX112 do tipo “I” (coluna IND_ICOMPL_LANCTO = “I”);

Se parâmetro = “Observações do Lançamento Fiscal”  serão consideradas apenas as
observações da SAFX112 do tipo “L” (coluna IND_ICOMPL_LANCTO = “L”).

Se parâmetro = “Ambos”  serão considerados os dois tipos de observação;

## Processamento

Para cada estabelecimento (ou estabelecimento/inscrição estadual do PIM, se for o caso) será gerado um relatório.

Para cada nota fiscal, poderão existir “n” observações na SAFX112, para qualquer um dos tipos (“I” ou “L”).

As observações do tipo “L” (Observação do Lançamento Fiscal) podem ter valores de ajustes associados na tabela SAFX113. Nesse caso, para cada observação da SAFX112 (do tipo “L”), poderão existir “n” ajustes na SAFX113.

Para cada documento recuperado de acordo com os critérios acima, serão recuperadas as observações da SAFX112 (conforme o parâmetro “Tipo de Observação”, como citado acima), e os ajustes que possam existir na SAFX113, quando for o caso.

O relatório será gerado por estabelecimento (ou Estab./Inscrição Estadual PIM, conforme o caso), seguindo a ordenação e as regras de preenchimento dos dados descritos a seguir.

Sobre os totais dos ajustes:

Durante o processamento das notas e emissão do relatório de cada estabelecimento, os valores dos ajustes apresentados serão totalizados por código do ajuste, e ao final do relatório será demonstrado o resultado desta totalização.

Quando nenhuma das notas listadas tiver valor de ajuste, as linhas de cabeçalho referentes a estes totais não serão geradas (não faz sentido demonstrá-las sem nenhum valor).

## Ordenação

Para cada Estabelecimento ou Estabelecimento/Inscrição Estadual PIM, conforme o caso, serão listadas em primeiro lugar as operações de entrada, depois as operações de saída, e por último os totais por código de ajuste, conforme exemplificado no layout.

- Tanto para as operações de entrada, como para as saídas, os documentos serão ordenados por data fiscal.

- Para uma mesma data fiscal, os documentos serão ordenados por número.

- Para cada nota fiscal, as observações serão apresentadas ordenadas pelo tipo (“I” ou “L”), e
para cada tipo, ordenadas pelo código da observação.

## Preenchimento dos Dados

As cinco primeiras colunas do relatório são referentes às informações da capa do documento (SAFX07).

As colunas sob o título “Observação” são referentes às observações da SAFX112 vinculadas ao documento.

As colunas sob o título “Ajuste” são referentes aos ajustes da SAFX113 vinculados a uma observação do tipo “L”.

Quando uma nota tiver mais de uma observação, os dados de identificação da nota, não se repetem, a não ser quando houver uma quebra de página.

A descrição de uma observação (coluna “Descrição / Descrição Complementar”) poderá ocupar ‘n’ linhas, pois o tamanho de cada observação é variável.

Quando a descrição de uma determinada observação ocupar mais de uma linha, as colunas que identificam a observação (Tipo, Vínculo e Código) não se repetem.

Seguindo a mesma lógica, quando uma observação (tipo”L”) tiver mais de um ajuste vinculado,
e portanto ocupar mais de uma linha de ajuste, as colunas que identificam a observação, e também a sua descrição, também não se repetem.

Segue regras de preenchimento dos campos:

Cabeçalho:


Linhas de Detalhe:


Totais dos Ajustes por Código:





## Layout do Relatório

Vide documento “Layout-Conferencia-Observacoes-e-Ajustes.xlsx”.


= = = = =

---

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| OS4712 | Novo relatório | Novo relatório para conferência das observações e ajustes (SAFX112/SAFX113) vinculados às notas fiscais. | 13/03/2015 |
| MFS32722 | Inclusão de campo | Inclusão do campo VLR_OUTROS  da SAFX 113. | 12/08/2021 |
|  |  |  |  |
|  |  |  |  |


---

| Campo | Tipo | Obrig | Ed | Formato/Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Período | Data | S | S | DD/MM/AAAA | Neste campo o usuário informará uma data inicial e uma data final, a serem utilizadas como filtro dos documentos fiscais. A data inicial deve ser < = data final. |
| Tipo de Movimento | Lista | S | S | Default: nenhum | Este campo é uma lista com as seguintes opções: - Entradas - Saídas - Ambos |
| Tipo de Observação | Lista | S | S | Default: nenhum | Este campo é uma lista com as seguintes opções: - Informações Complementares - Observações do Lançamento Fiscal - Ambos |
| Considerar notas canceladas | Checkbox | N | S | Default: desmarcado | Opção para considerar ou não as notas canceladas na emissão do relatório. |
| Geração por Inscrição Estadual Única | Checkbox | N | S | Default: desmarcado | Opção para geração do relatório por inscrição estadual única. Esta opção interfere na montagem da lista dos estabelecimentos (ver regra do campo “Estabelecimentos”). |
| Geração por Inscrição Estadual do PIM-AM | Checkbox | N | S | Default: desmarcado | Opção para geração do relatório por inscrição estadual do Amazonas (Módulo PIM). Esta opção interfere na montagem da lista dos estabelecimentos (ver regra do campo “Estabelecimentos”). |
| UF | Lista | N | S | Default: branco | Este campo é uma lista com a sigla das UF’s da tabela ESTADOS + opção “brancos”. Se preenchido, o campo “Estabelecimentos” exibirá apenas os estabelecimentos da UF selecionada. |
| Estabelecimentos |  |  |  |  | Na abertura da tela este campo exibirá a lista de todos os estabelecimentos da empresa do login.   Posteriormente, caso o usuário selecione os campos “Geração por I.E.U.”, “Geração por IE do PIM-AM”, ou preencha o campo “UF”, esta lista será refeita, conforme regras a seguir:  Se o campo “UF” for preenchido, a lista será refeita, considerando apenas os estabelecimentos da UF informada.  Se a opção “Geração por Inscrição Estadual Única” for marcada, a lista passará a exibir apenas os estabelecimentos centralizadores, de acordo com a centralização dos estabelecimentos de mesma I.E.U. (Módulo de Controle das Obrigações Estaduais).  Se a opção “Geração por Inscrição Estadual do PIM-AM” for marcada, a lista passará a exibir apenas os estabelecimentos do AM com suas respectivas inscrições estaduais, a partir do cadastro das IE’s do Módulo PIM (MENU “Cadastros  Inscrição Estadual por Estabelecimento”). Nesse caso, ao lado da razão social do estabelecimento será exibida a sua IE, no formato:  “XXXXXX – XXXXXXXXXXXXXXXXXXX – XXXXXXXXXXXXX”  Obs: Para montar a lista, as diferentes modalidades de geração são tratadas junto com a UF selecionada, quando for o caso, e considerando  sempre apenas os estabelecimentos da empresa do login. |
| Marcar Todos | Button | N | S |  | Ao clicar nesta opção serão marcados para seleção todos os estabelecimentos exibidos da lista. |
| Desmarcar Todos | Button | N | S |  | Ao clicar nesta opção serão desmarcados todos os estabelecimentos exibidos da lista. |


---

| Primeira linha do cabeçalho | A primeira linha do cabeçalho demonstra a razão social da empresa, a data de emissão do relatório e o número da página. |
| --- | --- |
| Segunda linha do cabeçalho | O campo “Filial” será preenchido com o código e a razão social do estabelecimento em questão. No campo “Período” será exibido o período solicitado em tela (data inicial e data final), e ao lado aparecerá o tipo de movimento solicitado em tela, no seguinte formato:  - Se opção = Entradas  o conteúdo será = (Entradas) - Se opção = Saídas    o conteúdo será = (Saídas) - Se opção = Ambos   o conteúdo será = (Entradas e Saídas)  O campo “Insc.Estadual” será preenchido da seguinte forma:  Geração “Normal”  será a IE do estabelecimento na sua própria UF; Geração por I.E.U  será a IE do estabelecimento centralizador na sua UF; Geração por IE-PIM  será a IE selecionada em tela (IE do PIM)  O campo “CNPJ” será preenchido com o CNPJ do estabelecimento. |


---

| Data Fiscal | Data fiscal do documento (SAFX07) |
| --- | --- |
| Nota Fiscal | Número do documento (SAFX07) |
| Série/Sub | Série e subsérie do documento (SAFX07) |
| Dt. Emissão | Data da emissão do documento (SAFX07) |
| Pessoa Fis/Jur | Pessoa fis/jur do documento (indicador + código) |
| Tipo | Tipo da observação (campo “13-Tipo de Observação” da SAFX112) |
| Vínculo | Dependendo do campo “15-Vinculação” da SAFX112:  Se = “1”  o campo será preenchido com “EFD – ICMS/IPI” Se = “2”  o campo será preenchido com “EFD – PIS/COFINS” |
| Código | Código da observação (campo “12-Código da Observação” da SAFX112). |
| Descrição/Descrição Complementar | Este campo será preenchido com a concatenação da descrição da SAFX2009 + descrição complementar da SAFX112, no formato:  [ SAFX2009.DESCRICAO + “-“ + SAFX112.DSC_COMPLEMENTAR ]  Como estes dois campos têm o tamanho de 500 caracteres, a descrição de uma única observação poderá ocupar ‘n’ linhas. |
| Cód. Ajuste | Código do ajuste vinculado à observação (campo “13-Código do Ajuste” da SAFX113). |
| Valor Ajuste | Valor do ajuste vinculado à observação (campo “18-Valor do ICMS” da SAFX113). |
| Valor Outros Ajustes | Valor de outros ajustes vinculados à observação (campo “19-Outros Valores” da SAFX113). |


---

| Código do Ajuste | Código do ajuste totalizado. |
| --- | --- |
| Total | Valor total do ajuste. |
| Total Outros Ajustes | Valor total de outros ajustes. |
