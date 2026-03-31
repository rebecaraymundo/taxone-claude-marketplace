# MTZ-OTF-Parametros_DARF_GPS

- **Fonte:** MTZ-OTF-Parametros_DARF_GPS.docx
- **Modificado:** 2020-08-29
- **Tamanho:** 29 KB

---

# Módulo – Obrigações de Tributos Federais – Parâmetros DARF/GPS

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

CH54719

Alteração do dia Limite de Recebimento

Para que o sistema atenda a legislação, deverá ser alterada o dia de vencimento aceitando o dia até o dia 20\.

OS3753\-F

DW e Job Servidor \- Ajustes na Rotina de Estorno de Retenções

O cliente Caixa Seguradora possui um processo interno de estorno de retenções\. O conceito de estorno de retenções é quando o cliente deseja reaver o valor de uma retenção indevida\. Isso pode ocorrer em três momentos distintos no produto:

- __Retenção sem DARF Gerado:__ esse é o caso mais simples, o cliente importou uma retenção no produto, porém antes mesmo de gerar o DARF referente a essa retenção, o cliente percebeu o erro\. 
- __Retenção com DARF Gerado e Não Pago:__ esse caso é o cenário principal do cliente, pois ele envia o DARF para pagamento e por motivos de erro no sistema bancário – exemplo: conta inválida ou encerrada, CPF inválido, entre outros – o pagamento não é processado\. Nesse caso o cliente tem que estornar o valor no ERP \(SAP\) para que essa retenção não seja considerada em nenhuma obrigação acessória\.
- __Retenção com DARF Gerado e Pago: __esse cenário já está resolvido dentro do sistema, pois se o cliente pagou um DARF indevidamente – a maior ou a menor – o cliente pode resolver essa situação através da funcionalidade de Tributos Ajustados já disponibilizada no produto\.

Inicialmente na OS3753, foi realizado o tratamento nos módulos DW e Job Servidor, porém o cliente não tem como identificar no SAP se a retenção está paga ou não\. Logo, o cliente só deveria informar a “Data de Retificação” e no momento da importação o sistema deve identificar os status da retenção e a partir daí realizar a atualização da mesma\. Vale ressaltar que a principal alteração dessa OS será que a data a ser considerada será a “Data de Retificação” e não mais a “Data do Estorno” conforme solução anterior\.

É importante frisar também que os campos “Estorno” e “Data do Estorno” que deveriam ser informados para realizar o processo de estorno serão retirados da tabela SAFX e consequentemente do Manual de Layout\. Segundo acordado com a Fábrica isso é possível de ser feito e irá facilitar a montagem das interfaces por parte dos clientes\. Esses campos só existirão na tabela definitiva \(X53\_RETENCAO\_IRRF\)\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

No box “Parâmetro GPS”, alterar o campo “dia limite para recebimento” para aceitar o dia até dia 20\.

CH54719

__RN01__

Alterar a mensagem quando o usuário incluir a dia  maior que dia 20 na confirmação devera exibir a mensagem: “ Dia limite para recebimento somente deve ser preenchido com dia menor ou igual a 20 \.”

CH54719

__RN02__

Deverá ser criado na tela de Parâmetros DARF/GPS o flag “Considerar Estorno a partir da Data de Retificação”\. Esse parâmetro deverá ficar localizado abaixo do campo “Retenção Mínima de DARF” e por default deverá ficar desmarcado\.

OS3753\-F

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

