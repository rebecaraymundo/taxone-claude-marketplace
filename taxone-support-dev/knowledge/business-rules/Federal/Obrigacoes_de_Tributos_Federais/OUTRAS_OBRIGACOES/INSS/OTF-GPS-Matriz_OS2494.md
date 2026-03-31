# OTF-GPS-Matriz_OS2494

- **Fonte:** OTF-GPS-Matriz_OS2494.docx
- **Modificado:** 2020-08-29
- **Tamanho:** 25 KB

---

# Obrigações de Tributos Federais – GPS

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS2494

GPS – Cooperativa de Trabalho de Transporte 

Durante a geração das retenções do INSS os dados deverão ser gravados considerando o campo 26 da SAFX04, onde o sistema deverá verificar se a informação é referente à Cooperativa de transporte, caso seja, a nota gerada referente a essa Pessoa Fis/Jur deve ser levada para a tela de manutenção com a data do fato gerador preenchida conforme a data fiscal\.

Durante a geração da Guia a data de competência apresentada na GPS deve ser a mesma da data fiscal\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

No campo 26 da SAFX04 “Classe de Pessoa Fís/Jur” deverá ser incluída a opção “05\-Cooperativa de transporte”\.

OS2494

__RN01__

O nome desse campo será somente “Data do Fato gerador”

OS2494

__RN02__

Quando da geração da retenção de INSS, se identificado que no campo 26 da SAFX 04 a informação colocada é “Cooperativa de transporte”, o campo “Data do fato gerador” dessa tela \(Manutenção de Dados de Retenção\) será igual a informação colocada no campo “Data Fiscal”\.

OS2494

