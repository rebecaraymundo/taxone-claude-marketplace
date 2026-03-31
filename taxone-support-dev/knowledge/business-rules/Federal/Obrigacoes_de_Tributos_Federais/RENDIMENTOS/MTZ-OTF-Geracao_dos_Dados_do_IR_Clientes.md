# MTZ-OTF-Geracao_dos_Dados_do_IR_Clientes

- **Fonte:** MTZ-OTF-Geracao_dos_Dados_do_IR_Clientes.docx
- **Modificado:** 2024-02-27
- **Tamanho:** 34 KB

---

# Módulo – Obrigações de Tributos Federais

# Geração dos Dados do Informe de Rendimentos Clientes

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3753\-C

Obrigações de Tributos Federais – Desconsiderar Retenções com Estorno dos Informes de Rendimento

O cliente Caixa Seguradora possui um processo interno de estorno de retenções\. O conceito de estorno de retenções é quando o cliente deseja reaver o valor de uma retenção indevida\. Isso pode ocorrer em três momentos distintos no produto:

- __Retenção sem DARF Gerado:__ esse é o caso mais simples, o cliente importou uma retenção no produto, porém antes mesmo de gerar o DARF referente a essa retenção, o cliente percebeu o erro\. 
- __Retenção com DARF Gerado e Não Pago:__ esse caso é o cenário principal do cliente, pois ele envia o DARF para pagamento e por motivos de erro no sistema bancário – exemplo: conta inválida ou encerrada, CPF inválido, entre outros – o pagamento não é processado\. Nesse caso o cliente tem que estornar o valor no ERP \(SAP\) para que essa retenção não seja considerada em nenhuma obrigação acessória\.
- __Retenção com DARF Gerado e Pago: __esse cenário já está resolvido dentro do sistema, pois se o cliente pagou um DARF indevidamente – a maior ou a menor – o cliente pode resolver essa situação através da funcionalidade de Tributos Ajustados já disponibilizada no produto\.

A solução proposta foi a criação de dois campos de identificação na tabela de Controle de Tributos: “Estorno” e “Data do Estorno”\. Esses campos identificam a retenção estornada e não permitem que a mesma seja considerada nas obrigações acessórias federais e relatórios de conferência do sistema\. Vale salientar que esses campos citados anteriormente foram criados na OS3753\. As rotinas do sistema que deverão ser alteradas são:

- Obrigações Acessórias
	- DARF
	- DCTF
	- DIRF
	- __Informe de Rendimentos – OS3753\-C__
- Relatórios Gerenciais
	- Relatório de Tributos Federais
	- Relatório de Rastreabilidade

Hoje a rotina de importação do produto não permite a importação de uma retenção que tenha um DARF vinculado à mesma e que esteja Gerado/Não Pago ou Pago\. Isso é um controle do sistema para garantir que um DARF fique diferente da retenção, ocasionando erros críticos para o cliente\. Esse controle funciona assim de longa data e no passado já foram dados NO GO para que isso fosse permitido\.

Com esse cenário do cliente, o sistema deverá permitir que na rotina de importação da tabela de Controle de Tributos – SAFX53 – o sistema ao identificar os campos “Estorno” e “Data do Estorno” preenchidos, o sistema deverá fazer a seguinte identificação:

- __Retenção sem DARF Gerado:__ nesse caso a retenção será atualizada sem maiores ônus\. 
- __Retenção com DARF Gerado e Não Pago:__ nesse caso, o sistema irá identificar o DARF dessa retenção e irá à tabela X75\_DCTF apagar esse DARF\. Essa retenção e as outras associadas ao DARF que foi deletado, terão seu status alterado para “Não Gerado”\. Essas retenções terão o campo “Estorno” e “Data do Estorno” informados\.
- __Retenção com DARF Pago:__ nesse caso o cliente deverá utilizar o sistema de acordo com a funcionalidade de Tributos Ajustados já existente no sistema\. 

É importante que no segundo ponto o DARF seja deletado, porque as retenções com Estorno não serão consideradas nas obrigações federais\. Se isso não for desenvolvido ao gerar a DCTF o cliente irá ter uma Ficha de Pagamento \(R11\) sem uma Ficha de Débito vinculada\.

O escopo da OS3753\-C é permitir que os Informes de Rendimento desconsidere as retenções da tabela de Controle de Tributos que estejam estornadas\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

Ao gerar o Informe de Rendimentos Outros Clientes, o sistema ao recuperar os registros de retenção do Controle de Tributos \(tabela: X53\_RETENCAO\_IRRF\), deve ignorar os registros estornados, ou seja, os registros cujo campo “Estorno” e “Data do Estorno” estejam preenchidos\.

__OS3753\-C__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

