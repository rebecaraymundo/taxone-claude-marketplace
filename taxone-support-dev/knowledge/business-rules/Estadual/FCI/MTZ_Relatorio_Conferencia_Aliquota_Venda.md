# MTZ_Relatorio_Conferencia_Aliquota_Venda

- **Fonte:** MTZ_Relatorio_Conferencia_Aliquota_Venda.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 35 KB

---

# Regras de Relatório

# Conferência da Alíquota de Venda

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3874\-B

Criação do documento

Definição das regras para o relatório Conferência da Alíquota de Venda\.

OS4395

Criação do documento

Melhoria no Relatório Conferência da Alíquota de Venda com inclusão de campos 

REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Origem da Informação__: Cadastro do Estabelecimento, SAX214 – Movimentação de Produtos Sujeitos ao FCI, SAFX08 – Itens Notas Fiscais Mercadorias e Produtos\.

__Regra de seleção__: este relatório será gerado quando, na tela de emissão dos relatórios de apoio do FCI for selecionada a opção “Conferência da Alíquota de Venda”\. Serão selecionados os registros da tabela SAX214 – Movimentação de Produtos Sujeitos ao FCI cuja Data de Referência compreenda o período informado na tela de emissão do relatório, que tenham a mesma parametrização de empresa e estabelecimento\.

Para cada produto selecionado da SAFX214 que atenda aos critérios de seleção, deve haver uma seleção na tabela de Documentos Fiscais \(SAFX07 e 08\) em busca de Documentos que registrem movimentação do produto indicado na SAFX214\. Esta seleção deve considerar: NFs cuja data fiscal compreenda o período informado na tela de emissão do relatório e que tenham a mesma parametrização de empresa e estabelecimento, que tenha movimento de Entrada/Saída igual a 9 \- Documento de Saída, que tenha o campo Modelo de Documento igual a 55 e que o produto indicado na SAFX214 tenha sido indicado também na SAFX08, considerando os campos de Indicador e Código do Produto para identificação\.

__Campos\-chave__: Estabelecimento, Nº da NF, Série, Emissão, Cód\. Produto e Alíq\. de Venda

__Ordenação__: Emissão, Nº da NF, Série, Cód\. Produto e Alíq\. de Venda

__Agrupamento__: Estabelecimento, Nº da NF, Série, Emissão, Cód\. Produto e Alíq\. de Venda

OS3874\-B

__Cabeçalho__

__RN01__

__Empresa__

Descrição do nome da empresa que está emitindo o relatório\.

OS3874\-B

__RN02__

__Estabelecimento__

Campo Razão Social da tabela de Estabelecimento\.

OS3874\-B

__RN03__

__Inscrição Estadual__

Código da Inscrição Estadual cadastrada para a UF do Estabelecimento\.

OS3874\-B

__RN04__

__CNPJ__

Campo CNPJ do Estabelecimento\.

OS3874\-B

__Dados dos Documentos Fiscais__

__RN05__

__Nº da NF__

Será gerado com base no campo Número do Documento Fiscal \(campo 09 da SAFX08\)\.

OS3874\-B

__RN06__

__Série__

Será gerado com base no campo Série do Documento Fiscal \(campo 10 da SAFX08\)\.

OS3874\-B

__RN07__

__Emissão__

Será gerado com base no campo Data da Escrita Fiscal do Documento Fiscal \(campo 03 da SAFX08\)\.

OS3874\-B

__RN08__

__Cód\. Produto__

Será composto pelo Indicador de Produto \+ Código do Produto informado na tabela de Movimentação de Produtos Sujeitos ao FCI \(SAFX214\), assumindo a seguinte formatação: *Ind\. Produto–Cód\. Produto*\.

OS3874\-B

__RN09__

__% do C\.I\.__

Será gerado com base no campo Percentual do Conteúdo de Importação informado na tabela SAFX214\.

OS3874\-B

__RN10__

__Alíq\. de Venda__

Será gerado com base no campo Alíquota ICMS \(campo 42 da SAFX08\)\.

OS3874\-B

__RN11__

__BC do ICMS__

Será gerado com base no campo Base ICMS \(campo 56 da SAFX08\)\.

OS3874\-B

__RN12__

__Valor do ICMS__

Será gerado com base no campo Valor ICMS \(campo 43 da SAFX08\)\.

OS3874\-B

__RN13__

__Ident\. Pessoa Fis / Jur__

Será composto pelo Indicador Pessoa Física / Jurídica \+ Código de Destinatário / Emitente \(campo 7 e 8 da SAFX08\)\.

__ __

OS4395

__RN14__

__CFOP__

Será gerado com base no campo código fiscal \(campo 22 da SAFX08\)\.

OS4395

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

