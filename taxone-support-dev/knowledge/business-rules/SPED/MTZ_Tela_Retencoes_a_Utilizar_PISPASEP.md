# MTZ_Tela_Retencoes_a_Utilizar_PISPASEP

> Fonte: MTZ_Tela_Retencoes_a_Utilizar_PISPASEP.docx



## (EFD-PIS/PASEP – COFINS) – Retenções a Utilizar na Apuração – PIS/PASEP



DOCUMENTO DE REQUISITO


### REGRAS DE NEGÓCIO








| DR | Nome | Descrição | Data Alteração |
| --- | --- | --- | --- |
| OS3169-DW17 | Criação da tela Retenções a Utilizar na Apuração – PIS/PASEP | Criação da tela de Retenções a Utilizar na Apuração – PIS/PASEP |  |
| OS3169-GE28 | Alteração na tela Retenções a Utilizar na Apuração – PIS/PASEP | Incluir na tela Retenções a Utilizar na Apuração (PIS/PASEP) o campo Retenção Disponível. | 07/11/2011 |


| Cód. |  | DR |
| --- | --- | --- |
| RN00 | Renomear os campos “Valor Limite da Dedução do Valor Retido na Fonte na Contribuição Não Cumulativa” para “Valor Limite da Contribuição Não Cumulativa a Descontar” e o campo “Valor Limite da Dedução do Valor Retido na Fonte na Contribuição Cumulativa” para “Valor Limite da Contribuição Cumulativa a Descontar”. | OS3169-GE28 |
| RN01 | Inclusão da coluna Retenção Disponível na terceira parte da tela (Este campo terá a mesma informação que está sendo informado na segunda parte da tela). | OS3169-GE28 |
| RN02 | Após pesquisar os registros o usuário poderá selecionar os dados para a terceira parte da tela de acordo com a utilização das retenções. | OS3169-DW17 |
| RN03 | O campo “Valor Limite da Contribuição Não Cumulativa a Descontar’’ é apenas informativo, devendo apresentar o Valor da Contribuição Não Cumulativa a Recolher/Pagar (campo 08) do registro M200. | OS3169-DW17 OS3169-GE28 |
| RN04 | O campo “Valor Limite da Contribuição Cumulativa a Descontar’’ é apenas informativo, devendo apresentar o Valor da Contribuição Cumulativa a Recolher/Pagar (campo 12) do registro M200. | OS3169-DW17 OS3169-GE28 |
| RN05 | Parte – Retenção(s) (Disponível(s)  Após o usuário informar na pesquisa o período na tela de Retenções Disponíveis, o sistema de apresentar dos todos os saldos de valores retidos na fonte das escriturações de períodos anteriores que o campo Retenção Disponível esteja com o valor maior que zero.   Listar registros com as informações a seguir:  Retenção Disponível maior que ZERO; Natureza da Receita igual a ZERO ou 1; Condição da Pessoa Jurídica Declarante igual a 0 e 1  Caso o cliente queira utilizar a retenção com a condição PFJ = 1  Exibir a seguinte msg:  Retenção na Fonte não pode ser utilizada pois a Condição da Pessoa Jurídica Declarante é 1- Responsável pela Retenção/Recolhimento. | OS3169-DW17 |
| RN06 | O sistema deve permitir que usuário selecione um ou mais tipos de saldos dos valores retidos na fonte. Após o usuário clicar na funcionalidade >>, o sistema de apresentar os valores retidos na fonte selecionados na parte de Dedução(s) a ser Utilizada(s) no Período. | OS3169-DW17 |
| RN07 | Parte – Retenção(s) a ser Utilizada(s) no Período Permitir alterar o valor do campo abaixo, até zerar o valor informado no campo ‘’Valor Limite da Contribuição Não Cumulativa a Descontar’’, se o campo natureza da receita esteja igual ‘’0 – Receita de Natureza Não Cumulativa’’ e o campo Condição da PJ Declarante estiver igual ‘’ 0 – Beneficiária da Retenção / Recolhimento’’  Retenção Deduzida da Contribuição | OS3169-DW17 |
| RN08 | Permitir alterar os valores dos campos abaixo, até zerar o valor informado no campo ‘‘Retenção Disponíveis’’, se o campo natureza da receita esteja igual ‘’0 – Receita de Natureza Não Cumulativa’’ e o campo Condição da PJ Declarante estiver igual ‘’ 0 – Beneficiária da Retenção / Recolhimento’’  Retenção Utilizada por Pedido de Restituição; e Retenção Utilizada por Declaração da Compensação. | OS3169-DW17 |
| RN09 | Após o usuário clicar no botão Confirmar, as retenções a utilizar na dedução da contribuição, o sistema deve efetuar as seguintes validações:  Situação A Somatório de valores informado no campo ‘’Retenção Deduzida da Contribuição’’ de todos os registros apresentados na parte de retenção a utilizar, considerando o seguinte critério. Campo Natureza da Receita estiver igual a ‘’ 0  Campo Condição da PJ Declarante estiver igual ‘’ 0 – Beneficiária da Retenção / Recolhimento’’ Compara o Valor Limite da Contribuição Não Cumulativa a Descontar.  Se o resultado descrito no item 1, for maior que o valor apresentado no campo Valor Limite da  Contribuição Não Cumulativa a Descontar, o sistema de exibir a seguinte mensagem:  Valor Retido na Fonte de Períodos Anteriores, superou o valor da contribuição Não Cumulativa em ''|| 999999,00.  Situação B  Somatório de valores informado no campo ‘’Retenção Deduzida da Contribuição’’ de todos os registros apresentados na parte de retenção a utilizar, considerando o seguinte critério. Campo Natureza da Receita estiver igual a ‘’1”  Campo Condição da Pessoa Jurídica Declarante estiver igual ‘’ 0 – Beneficiária da Retenção / Recolhimento’’ Compara o Valor Limite da Contribuição Cumulativa a Descontar.  Se o resultado descrito no item 1, for maior que o valor apresentado no campo Valor Limite da Contribuição Cumulativa a Descontar, o sistema de exibir a seguinte mensagem:  Valor Retido na Fonte de Períodos Anteriores, superou o valor da contribuição Cumulativa  em ''|| 999999,00. | OS3169-DW17 OS3169-GE28 |
|  | Situação C  Somatório de valores informado no campo ‘’Retenção Deduzida da Contribuição’’ de todos os registros apresentados na parte de retenção a utilizar, considerando o seguinte critério. Se a empresa tem regime misto (campo Incidência Tributária no Período = 3 da tela de Dados Iniciais, menu Parâmetros > Dados Iniciais)  Campo Natureza da Receita estiver igual a ‘’1”  Campo Condição da PJ Declarante estiver igual ‘’ 0 – Beneficiária da Retenção / Recolhimento’’ 2)	Compara o Valor Limite da Contribuição Não Cumulativa a Descontar, somente se o Valor Limite da Contribuição Cumulativa a Descontar for igual a zeros.  3)	Se o resultado descrito no item 1, for maior que o valor apresentado no campo Valor Limite da Contribuição Não Cumulativa a Descontar, o sistema de exibir a seguinte mensagem: Valor Retido na Fonte de Períodos Anteriores, superou o valor da contribuição não Cumulativa  em ''|| 999999,00. |  |
|  | Situação D  Somatório de valores informado no campo ‘’Retenção Deduzida da Contribuição’’ de todos os registros apresentados na parte de retenção a utilizar, considerando o seguinte critério. Se a empresa tem regime misto (campo Incidência Tributária no Período = 3 da tela de Dados Iniciais, menu Parâmetros > Dados Iniciais)  Campo Natureza da Receita estiver igual a ‘’ 0  Campo Condição da Pessoa Jurídica Declarante estiver igual ‘’ 0 – Beneficiária da Retenção / Recolhimento’’ 2)	Compara o Valor Limite da Contribuição Cumulativa a Descontar, somente se o Valor Limite da Contribuição Não Cumulativa a Descontar for igual a zeros.  3)	Se o resultado descrito no item 1, for maior que o valor apresentado no campo Valor Limite da Contribuição Cumulativa a Descontar, o sistema de exibir a seguinte mensagem: Valor Retido na Fonte de Períodos Anteriores, superou o valor da contribuição Cumulativa  em ''|| 999999,00. |  |
| RN10 | : Caso a somatória dos campos: Retenção Deduzida da Contribuição; Retenção Utilizada por Pedido de Restituição; e Retenção Utilizada por Declaração da Compensação for maior que o valor da Retenção Disponível, o sistema deve exibir a seguinte mensagem:    Somatório dos Valores de Retenção Deduzida da Contribuição maior que o Valor da Retenção Disponível | OS3169-DW17 |
