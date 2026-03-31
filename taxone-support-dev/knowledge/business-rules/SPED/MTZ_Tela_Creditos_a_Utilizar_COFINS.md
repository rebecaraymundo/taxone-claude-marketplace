# MTZ_Tela_Creditos_a_Utilizar_COFINS

> Fonte: MTZ_Tela_Creditos_a_Utilizar_COFINS.docx



## (EFD-PIS/PASEP – COFINS) – Créditos a Utilizar na Apuração – COFINS



DOCUMENTO DE REQUISITO



### REGRAS DE NEGÓCIO








| DR | Nome | Descrição | Data Alteração |
| --- | --- | --- | --- |
| OS3169-DW17 | Criação da tela | Criação da Tela Créditos a Utilizar na Apuração – PIS/PASEP |  |
| OS3169-GE28 | Alteração na tela Créditos a Utilizar na Apuração – COFINS | Incluir na tela Créditos a Utilizar na Apuração (COFINS) o critério de pesquisa Código do Tipo de Crédito. | 07/11/2011 |
| MFS28515 | Andréa Rocha | Alterar a tela para não mostrar os créditos disponíveis com o status de cancelado. | 15/10/2019 |
| MFS34355 | Liliane Assaf | Alteração no tratamento dos créditos prescritos com mais de 5 anos. | 28/06/2020 |
| MFS57866 | Andréa Rocha | Alteração no tratamento dos créditos prescritos com mais de 5 anos.  Criação de um parâmetro para indicar se os créditos com mais de 5 anos podem ser usados ou não.  Assim, ficam as duas opções disponíveis para o usuário escolher a forma de tratar os créditos. | 08/03/2021 |


| Cód. |  | DR |
| --- | --- | --- |
| RN00 | Renomear o campo ‘Valor Limite para o Crédito Descontado, Apurado em Período de Apuração Anterior’, para ‘Valor Limite da Contribuição Não Cumulativa a Descontar’. | OS3169-GE28 |
| RN01 | Na segunda parte da  tela, incluir a pesquisa por  Cód. Tipo Crédito, que deve ter as seguintes opções: TFIX93 (101,102,103,104,105,106,108,109,199,201,202,203,204,205,206,208,209,299,301,302,303,304,305,306,308,309,399) e Em Branco.  Se o usuário escolher a opção em branco, todos os códigos deverão ser apresentados. | OS3169-GE28 |
| RN02 | O campo ‘’Valor Limite da Contribuição Não Cumulativa a Descontar’’ é apenas informativo, devendo apresentar o Valor da Contribuição Não Cumulativa a Recolher/Pagar (campo 5) do registro M600 que foi gerado através da funcionalidade Geração dos Registros. | OS3169-DW17 OS3169-GE28 |
| RN03 | Parte – Crédito(s) a ser Utilizado(s) no Período Inclusão da coluna Crédito Disponível na terceira parte da tela (Este campo terá a mesma informação que está sendo informado na segunda parte da tela). | OS3169-GE28 |
| RN04 | Após pesquisar os registros o usuário poderá selecionar os dados para a terceira parte da tela de acordo com a utilização dos créditos. | OS3169-DW17 |
| RN05 | Permitir alterar o valor do campo descrito abaixo, até zerar o valor informado no campo ‘’Valor Limite da Contribuição Não Cumulativa a Descontar”  na parte Contribuição para COFINS  no Período . | OS3169-DW17 |
| RN06 | Crédito Utilizado para Desconto Após o usuário clicar no botão Confirmar, o sistema deve fazer as seguintes validações, antes de gravar o resultado da somatória dos valores do ‘’Crédito utilizado para Desconto’’ de todos os registros apresentados nessa parte, no campo ‘’Valor do Crédito Descontado, Apurado em Período Anterior da Escrituração’’ na parte Contribuição para PIS/PASEP no período.   Somar o valor crédito utilizado para Desconto de TODOS os tipos de créditos na parte Crédito(s) a ser Utilizado(s);    Compara o somatório descrito no item 1 com o valor do campo ‘’Valor Limite da Contribuição Não Cumulativa a Descontar’’ informado na parte ‘’Contribuição para PIS/PASEP no Período ’’.   Se o resultado descrito no item 1, for maior que o valor apresentado no campo “Valor Limite da Contribuição Não Cumulativa a Descontar”, o sistema de exibir a seguinte mensagem:  Valor do Crédito Descontado, Apurado em Período de Apuração Anterior, superou o valor da contribuição Não Cumulativa em '||999999,00. | OS3169-DW17 OS3169-GE28 |
| RN07 | Permitir alterar os valores dos campos descritos abaixo, até zerar o valor informado no campo ‘’Crédito Disponível’’ correspondente o registro selecionado.  Crédito Utilizado por Pedido de Ressarcimento; Crédito Utilizado por Compensação intermediária; Crédito Utilizado por Transferência (Cisão, Fusão e Incorporação); e Outros Créditos Utilizados. | OS3169-DW17 |
| RN08 | Caso a somatória dos campos: ‘’Crédito Utilizado para Desconto’’, ‘’Crédito Utilizado por Pedido de Ressarcimento’’, ‘’Crédito Utilizado por Compensação intermediária’’, ‘’Crédito Utilizado por Transferência (Cisão, Fusão e Incorporação)’’ e ‘’Outros Créditos Utilizados’’ for maior que o valor informado no campo Crédito a utilizar, o sistema deve exibir a seguinte mensagem:    Somatório dos Valores dos Créditos a Utilizar maior que o Valor do Crédito Disponível | OS3169-DW17 |
| RN09 | Parte – Crédito(s) Disponível(s)  Regras para o Quadro de Crédito Disponível:  [MFS57866] Criação de um parâmetro para indicar se os créditos com mais de 5 anos podem ser usados ou não.  Se o parâmetro “Utilizar os créditos superiores a 60 meses” estiver desmarcado       Os créditos que tiverem um período maior que 5 anos, ou seja, a diferença entre o mês/ano do          crédito e a data da apuração for maior que 5 anos, serão demonstrados com o campo        "Cancelado por Prazo de Prescrição" marcado.       Caso o usuário tente utilizar um crédito que esteja com "Cancelado por Prazo de Prescrição"         marcado, ou seja, com mais de 5 anos, o sistema exibirá a mensagem abaixo e impedirá a        utilização do crédito:      “Atenção, o crédito selecionado está com Status Cancelado por Prazo de Prescrição pois possui           mais de 5 anos e por isso não poderá ser utilizado.”  Se o parâmetro “Utilizar os créditos superiores a 60 meses” estiver marcado       O campo "Cancelado por Prazo de Prescrição" vai ficar habilitado para o usuário marcar ou          Desmarcar, ou seja, o usuário escolhe se o crédito está cancelado ou não.         Caso o usuário tente utilizar um crédito que esteja com "Cancelado por Prazo de Prescrição"         marcado, ou seja, com mais de 5 anos, o sistema exibirá a mensagem abaixo e impedirá a        utilização do crédito:      “Atenção, o crédito selecionado está com Status Cancelado por Prazo de Prescrição pois possui           mais de 5 anos e por isso não poderá ser utilizado.”       Se o campo "Cancelado por Prazo de Prescrição" estiver desmarcado, os créditos que tiverem um        período maior que 5 anos, ou seja, a diferença entre o mês/ano do crédito e a data da apuração       for maior que 5 anos, quando for selecionado para a utilização, deve-se dar uma mensagem:     “Atenção, o crédito selecionado possui mais de 5 anos. Favor verificar se o mesmo está prescrito.”.           A mensagem será para informar o usuário, mas não impedirá a utilização do crédito.  Obs.: O parâmetro “Utilizar os créditos superiores a 60 meses” está disponível na tela de Dados Iniciais (Parâmetros  Dados Iniciais). | MFS28515 MFS34355 MFS57866 |
