# MTZ-OTF-Demonstrativo_INSS_por_Estabelecimento-Avulso-Analitico

- **Fonte:** MTZ-OTF-Demonstrativo_INSS_por_Estabelecimento-Avulso-Analitico.docx
- **Modificado:** 2020-08-29
- **Tamanho:** 29 KB

---

# Obrigações de Tributos Federais 

# Relatório Demonstrativo de INSS por Estabelecimento \(Avulso\) \- Analítico

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS2839

# OTF\- Relatório Demonstrativo de INSS por Estabelecimento \(Avulso\) \- Analitico

Ajustes da apresentação das informações no relatório\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Regra para tela de critério de seleção do relatório__

__RN01__

__Regra para geração do relatório__

Os campos __Cedente__, __CNPJ/CPF__, __Razão Social__, __Data Emissão NF__, __Data Lacto NF__, __Nº Doc Fiscal__ e __Série/Subsérie__ devem ser apresentadas somente na 1ª linha, quando as informações forem idênticas para as Bases INSS e 2ª Base INSS\. 

A ordenação das linhas deve ser ascendente, através do campo __Valor Aliq__\. __INSS__ \(campo VLR\_ALIQ\_INSS da tabela IRT\_RET\_INSS\_DF\)\.

Os campos abaixo devem ser recuperados do menu: OTF > Outras Obrigações > Retenção de INSS – Serviços Prestados > Manutenção de Dados de Retenção:

__\- Valor Bruto: __campo__ Valor Total da Nota __\(campo VLR\_TOT\_NOTA da tabela IRT\_RET\_INSS\_DF\) somente na 1ª linha e não apresentar somatório na coluna

__\- Bases Cálculo:__ 

1ª linha \- campo __Valor dos Serv\./Base__ __INSS__ \(campo VLR\_SERVICOS da tabela IRT\_RET\_INSS\_DF\) relacionado à menor alíquota\.

2ª linha  \- campo __Valor dos Serv\./Base__ __INSS__ \(campo VLR\_SERVICOS da tabela IRT\_RET\_INSS\_DF\) relacionado à menor 

alíquota\.

3 ª linha – __Valor dos Serv\./Base__ __INSS__ \(campo VLR\_SERVICOS da tabela IRT\_RET\_INSS\_DF\) relacionado à maior

alíquota\. Não apresentar somatório na coluna\.

__\- Valor Apuração: __

1ª linha – campo __Valor do INSS Retido__ \(campo VLR\_INSS\_RETIDO da tabela IRT\_RET\_INSS\_DF\) relacionado à menor alíquota\.

2ª linha – campo __Valor do INSS Retido __\(campo VLR\_INSS\_RETIDO da tabela IRT\_RET\_INSS\_DF\) relacionado à menor alíquota\.

3ª linha – campo __Valor do INSS Retido __\(campo VLR\_INSS\_RETIDO da tabela IRT\_RET\_INSS\_DF\) relacionado à maior alíquota\. Deve apresentar somatório na coluna\.

__OS2839__

__CH16039\_2014__

__RN02__

__Totalizadores – Lançamentos do Mês de Janeiro e Emissões do Mês de Janeiro__

Apresentar o somatório do campo __Valor Apuração__\.

__OS2839__

__RN03__

No final do relatório deverá existir a linha “\*\* \- Sem Alíquota – Valor de Outras Entidades”\. Essa linha deverá apresentar o somatório do campo “Valor Outras Entidades” da capa do Documento Fiscal\.

__CH116174__

