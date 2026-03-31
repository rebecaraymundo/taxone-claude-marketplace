# MTZ_Transfer_Pricing_Operacao_Sujeita_ao_Arbitramento

- **Fonte:** MTZ_Transfer_Pricing_Operacao_Sujeita_ao_Arbitramento.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 30 KB

---

# Módulo \- Transfer Pricing \- Operação Sujeita ao

# Arbitramento Artigo 14 \- Método CAP

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS4404

Marcos G\. de Paula

Inclusão da linha "Comissões" no Detalhe do Cálculo da Operação Sujeita ao Arbitramento Artigo 14 IN 243\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

__Linha: \(H1\) Comissões__

O sistema deverá calcular a soma do Valor de Comissões lançado no Item de Notas Fiscais para o Produto e período no qual o cálculo está sendo realizado considerando a seguinte regra:

Coluna Mercado Interno: soma do Valor de Comissões do Item de Notas Fiscais das operações cujo CFOP inicie com conteúdo diferente de "7"\.

Coluna Mercado Externo: soma do Valor de Comissões do Item de Notas Fiscais das operações cujo CFOP inicie com conteúdo igual a "7"\.

O valor obtido para esta linha deve ser subtraído da linha "\(U\) Receita Líquida de Venda", considerando a coluna para o qual o valor foi apurado \(Mercado Interno ou Externo\)\.

OS4404

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

