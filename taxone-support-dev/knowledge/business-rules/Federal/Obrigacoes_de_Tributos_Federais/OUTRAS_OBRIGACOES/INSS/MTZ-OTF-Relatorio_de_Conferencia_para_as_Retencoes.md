# MTZ-OTF-Relatorio_de_Conferencia_para_as_Retencoes

- **Fonte:** MTZ-OTF-Relatorio_de_Conferencia_para_as_Retencoes.docx
- **Modificado:** 2021-03-05
- **Tamanho:** 30 KB

---

# Obrigações de Tributos Federais 

# Relatório de  Conferência para as Retenções

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS2839

# OTF\- Relatório de  Conferência para as Retenções

Inclusão da coluna “Valor Outras Entidades” e ajuste da apresentação das informações no relatório\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Regra para tela de critério de seleção do relatório__

__RN01__

__Regra para geração do relatório__

Os campos __Data de Entrada__, __NF/Série/Subsérie__, __Emite Compr Pag__, __Data Emissão__, __Data Extemp e__ __Pessoa FIS/JUR__, devem ser apresentadas somente na 1ª linha, quando as informações forem idênticas para as Bases INSS e 2ª Base INSS\.

A ordenação das linhas deve ser ascendente, através do campo __Valor Aliq__\. __INSS__ \(campo VLR\_ALIQ\_INSS da tabela IRT\_RET\_INSS\_DF\)  

Os campos abaixo devem ser recuperados do menu: OTF > Outras Obrigações > Retenção de INSS – Serviços Prestados > Manutenção de Dados de Retenção:

__\- Valor contábil: __campo__ Valor Total da Nota __\(campo VLR\_TOT\_NOTA da tabela IRT\_RET\_INSS\_DF\) somente na 1ª linha e não apresentar somatório na coluna

__\- Bases de Cálculo:__ 

1ª linha \- campo __Valor dos Serv\./Base__ __INSS__ \(campo VLR\_SERVICOS da tabela IRT\_RET\_INSS\_DF\) relacionado à menor alíquota\.

2ª linha  \- campo __Valor dos Serv\./Base__ __INSS__ \(campo VLR\_SERVICOS da tabela IRT\_RET\_INSS\_DF\) relacionado à maior alíquota\.

3 ª linha – repetir a informação da 1ª linha\. Não apresentar somatório na coluna\.

__\-Alíquota:__ 

1ª linha – campo __Valor Aliq__\. __INSS__ \(campo VLR\_ALIQ\_INSS da tabela IRT\_RET\_INSS\_DF\)  

2ª linha – campo __Valor Aliq__\. __INSS__ \(campo VLR\_ALIQ\_INSS da tabela IRT\_RET\_INSS\_DF\)   

3ª linha deixar em branco\.

__\- Valor INSS Retido:__ 

1ª linha – campo __Valor do INSS Retido__ \(campo VLR\_INSS\_RETIDO da tabela IRT\_RET\_INSS\_DF\) relacionado à menor alíquota\.

2ª linha – campo __Valor do INSS Retido __\(campo VLR\_INSS\_RETIDO da tabela IRT\_RET\_INSS\_DF\) relacionado à maior alíquota\.

3ª linha – preencher com “0,00”\. Deve apresentar somatório na coluna\.

__\- Valor Outras Entidades: __

1ª linha – preencher com “0,00”

2ª linha \-  preencher com “0,00”

3ª linha – campo__ Valor Outras Entidades __\(campo VLR\_OUTRAS\_ENTID da tabela IRT\_RET\_INSS\_DF\)

__OS2839__

__RN02__

__Totalizadores \- Total por Código de Pagamento e Total Geral__

Apresentar o somatório das colunas __Valor INSS Retido__ e __Valor Outras Entidades__\.

__OS2839__

