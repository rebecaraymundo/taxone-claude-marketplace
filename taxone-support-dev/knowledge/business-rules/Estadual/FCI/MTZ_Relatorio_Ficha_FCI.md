# MTZ_Relatorio_Ficha_FCI

- **Fonte:** MTZ_Relatorio_Ficha_FCI.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 34 KB

---

# Regras de Relatório

# Ficha do FCI

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3874\-B

Criação do documento

Definição das regras para o relatório Ficha do FCI\.

REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Origem da Informação__: Cadastro do Estabelecimento e SAX214 – Movimentação de Produtos Sujeitos ao FCI\.

__Regra de seleção__: este relatório será gerado quando, na tela de emissão do relatórios de apoio do FCI for selecionada a opção “Ficha do FCI”\. Serão selecionados os registros da tabela SAX214 – Movimentação de Produtos Sujeitos ao FCI cuja Data de Referência compreenda o período informado na tela de emissão do relatório e que tenham a mesma parametrização de empresa e estabelecimento\.

__Campos\-chave__: Estabelecimento, Data de Referência, Código da Mercadoria e Unidade de Medida

__Ordenação__: não se aplica

__Agrupamento__: deve ser gerada uma Ficha para cada Estabelecimento, Data de Referência, Código da Mercadoria e Unidade de Medida informado na SAFX214\.

OS3874\-B

__Cabeçalho__

__RN01__

__Razão Social__

Campo Razão Social da tabela de Estabelecimento\.

OS3874\-B

__RN02__

__Endereço__

Campo Endereço da tabela de Estabelecimento\.

OS3874\-B

__RN03__

__Município__

Descrição do Município do Estabelecimento\.

OS3874\-B

__RN04__

__UF__

Campo UF do Cadastro do Estabelecimento\.

OS3874\-B

__RN05__

__Inscrição Estadual__

Código da Inscrição Estadual cadastrada para a UF do Estabelecimento\.

OS3874\-B

__RN06__

__Data de Referência__

Campo Data de Referência informada na tabela SAFX214\.

OS3874\-B

__RN07__

__CNPJ__

Campo CNPJ do Estabelecimento\.

OS3874\-B

__DADOS DO BEM OU MERCADORIA RESULTANTE DA INDUSTRIALIZAÇÃO__

__RN08__

__Descrição da Mercadoria__

Será gerado com base no campo Descrição da Mercadoria \(04 – DESCRICAO\) da Tabela de Produtos \(SAFX2013\), considerando como base para seleção da informação o Indicador do Produto \+ Código do Produto informados na tabela de Movimentação de Produtos Sujeitos ao FCI \(SAFX214\)\.

OS3874\-B

__RN09__

__Código NCM__

Será gerado com base no campo Código NBM \(05 – COD\_NBM\) da Tabela de Produtos \(SAFX2013\), considerando como base para seleção da informação o Indicador do Produto \+ Código do Produto informados na tabela de Movimentação de Produtos Sujeitos ao FCI \(SAFX214\)\.

OS3874\-B

__RN10__

__Código da Mercadoria__

Será composto pelo Indicador de Produto \+ Código do Produto informado na tabela de Movimentação de Produtos Sujeitos ao FCI \(SAFX214\), assumindo a seguinte formatação: *Ind\. Produto–Cód\. Produto*\.

OS3874\-B

__RN11__

__Código GTIN__

Será gerado com base no campo Código de Barras \(40 – COD\_BARRAS\) da Tabela de Produtos \(SAFX2013\), considerando como base para seleção da informação o Indicador do Produto \+ Código do Produto informados na tabela de Movimentação de Produtos Sujeitos ao FCI \(SAFX214\)\.

OS3874\-B

__RN12__

__Unidade de Medida__

Será gerado com base na descrição da Unidade de Medida informada na SAFX214 e disponível na TACES81\.

OS3874\-B

__RN13__

__Valor da Parcela Importada do Exterior__

Será gerado com base no campo Parcela Importada do Exterior informado na tabela SAFX214\.

OS3874\-B

__RN14__

__Valor Total da Saída Interestadual__

Será gerado com base no campo Valor das Saídas Interestaduais informado na tabela SAFX214\.

OS3874\-B

__RN15__

__F\.C\.I\. nº__

Será gerado com base no campo Número do FCI informado na tabela SAFX214\.

OS3874\-B

__RN16__

__Conteúdo de Importação \(C\.I\.\)%__

Será gerado com base no campo Percentual do Conteúdo de Importação informado na tabela SAFX214\.

OS3874\-B

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

