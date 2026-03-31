# MTZ-OTF-Manutencao_de_DARFs

- **Fonte:** MTZ-OTF-Manutencao_de_DARFs.docx
- **Modificado:** 2020-08-29
- **Tamanho:** 30 KB

---

# Obrigações de Tributos Federais – Manutenção de DARF’s

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3212

Obrigações de Tributos Federais – Gerar DARF’s por Código Retenção/Código Operação/Data Vencimento/Código Receita

O objetivo dessa OS é gerar os DARF’s consolidando os mesmos por Código Retenção/Código Operação/Data de Vencimento/Código Receita\.

OS3917

Obrigações de Tributos Federais – Liberar Crédito Utilizado caso o DARF vinculado ao mesmo seja excluído

O cliente Sul América observou o seguinte comportamento no sistema: ao gerar os DARF’s de um determinado período em que pelo menos um deles possui um crédito oriundo de DARF ou Saldo Credor, ao excluir o mesmo pela tela de manutenção dos DARF’s ou através do parâmetro “Não Excluir DARF’s” no momento da geração, o sistema exclui o DARF, porém não libera o crédito utilizado no DARF excluído\. Isso gera um problema porque embora os DARF’s fiquem com os valores gerados corretamente, os créditos são considerados como utilizados no sistema e o cliente não consegue utilizar esse crédito novamente\. Abaixo segue um exemplo do problema do cliente:

__Cadastro de Saldo Credor__

__Valor a Compensar__

__Valor Compensado__

__Saldo__

R$ 3\.000,00

R$ 700,00

R$ 2\.300,00

__DARF Gerado__

__Data Apuração__

__Código DARF__

__Valor DARF antes da utilização de Crédito__

__Valor final do DARF após a utilização do Crédito__

__Crédito Utilizado__

31/03/2013

1708

R$ 10\.500,00

R$ 9\.800,00

R$ 700,00

Nesse caso, caso o cliente exclua o DARF gerado ou gere novamente os DARF’s desmarcando a opção “Não Excluir DARF’s”, o crédito de R$ 700,00 oriundo de Saldo Credor já utilizado, não poderá mais ser utilizado para compensação dos DARF’s\. O correto seria que os R$ 700\.00 de crédito já utilizado seja liberado, aumentando o saldo de R$ 2\.300,00 para R$ 3\.000,00\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Será disponibilizado o seguinte campo na tela:

- __Cód\. Operação:__ deverá ser informado o Código de Operação\. O código será informado a partir do código da retenção existente na tabela X53\_RETENCAO\_IRRF\. Esse campo deverá ser do tipo alfanumérico de 6 posições\. Campo não obrigatório de preenchimento\.

Esse campo será disponibilizado abaixo do campo “Cód\. Receita” que já existe na tela\.

OS3212

__RN01__

O relatório de conferência dessa tela deverá ser alterado\.

OS3212

# RN02

Caso o usuário ao tentar excluir o DARF na tela de Manutenção de DARF’s \(o mesmo precisa estar Em Aberto\) e o mesmo possua créditos vinculados ao mesmo \(ver campo NRO\_REFERENCIA\_DEB da tabela CTRL\_COMPENSACAO\_CRED\), o sistema deverá liberar os créditos tanto da tela de Saldo Credor \(campos: Valor a Compensar e Saldo da tabela SLD\_COMPENSACAO\_CRED\), quando os créditos oriundos de DARF \(campo: Valor Utilizado da aba: Compensações da tela de Manutenção do DARF\. 

OS3917

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

