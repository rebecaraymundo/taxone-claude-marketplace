# MTZ-Relacao_Mensal_Compra_Venda

- **Fonte:** MTZ-Relacao_Mensal_Compra_Venda.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 34 KB

---

# Atendimento – Polícia Federal – Relação Mensal de Compras/Vendas por Classificação de Produto

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data de Alteração__

OS3976\-G

DW \- ESPECÍFICOS \- SUBSTÂNCIAS CONTROLADAS \- Correção na geração do Polícia Federal onde registro MR que deve ser considerada pela Data Emissão

Este documento tem como objetivo permitir a geração para atendimento à Polícia Federal através da Data de Emissão da nota fiscal\.

04/04/2013

CH27589\-A\_2013

DW \- ESPECÍFICOS \- SUBSTÂNCIAS CONTROLADAS – Gravação do CAMPO DIA

Tratamento na gravação do campo DIA\.

11/11/2013

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

__Regra para tela Relação Mensal de Compras/Vendas por Classificação de Produto__

Ao clicar no menu Atendimento > Polícia Federal > Relação Mensal de Compras/Vendas por Classificação de Produto, o sistema deve exibir a tela de seleção conforme abaixo, com o seguinte campo, além dos campos já existentes: 

Recuperar informações por: 

Exibir campo no formato radio Button com as seguinte opções: Data Movimento e Data Emissão\. A opção Data Movimento deve estar marcada por default\.

OS3976\-G

__RG00__

__Regra Geral para recuperação dos dados:__

A geração deve recuperar as informações da tabela X70\_MOV\_SUBST\_CONT através da seguintes informações:

- Se o campo Recuperar informações por estiver marcado como Data Movimento:

        O campo DATA\_MOVTO deve estar dentro do mês/ano referencia informado na tela de geração\.

Se o campo Recuperar informações por estiver marcado como Data Emissão:

        O campo DATA\_EMISSAO deve estar dentro do mês/ano referencia informado na tela de geração\.

- Empresa igual a selecionado na Manager
- Estabelecimento igual ao escolhido na tela de geração

OS3976\-G

__RN02__

__CAMPO DIA__

Gravar a informação do campo DATA\_MOVTO de acordo com a parametrização prevista na RG00, ou seja, se o parâmetro estiver marcado como Data Movimento\.

OU

Gravar a informação do campo DATA\_EMISSAO de acordo com a parametrização prevista na RG00, ou seja, se o parâmetro estiver marcado como Data Emissão\.

CH27589\-A\_2013

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

