# MTZ-OTF-Geracao_Consolidacao_das_Retencoes

- **Fonte:** MTZ-OTF-Geracao_Consolidacao_das_Retencoes.docx
- **Modificado:** 2020-08-29
- **Tamanho:** 27 KB

---

# Módulo – Obrigações de Tributos Federais – Geração da Consolidação das Retenções

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

CH54719

Alteração na procedure o dia de vencimento

Para que  a geração da consolidação gera corretamente os valores de multas de juros deverá alterar o dia de vencimento para o dia 20\.

OS2839

Inclusão para tratamento do campo Valor Outras Entidades\.

Para os casos em que as Bases de INSS não estiverem preenchidas, recuperar o valor correto de Valor Outras Entidades\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Alterar em FED\_CALC\_TAXAS, na função “calcula\_juros\_multa\_INSS”, o dia  de vencimento para o dia 20\.

CH54719

__RN01__

__Valor Outras Entidades __

Se os campos Base INSS \(campo 85\-VLR\_BASE\_INSS\) e/ou 2º Base INSS \(campo 151\-VLR\_BASE\_INSS\_2\) da SAFX07 não estiverem preenchidos, deverá se recuperado o valor do campo Valor Outras Entidades \(campo 214\-VLR\_OUTRAS\_ENTID\) da SAFX07\.

OS2839

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

