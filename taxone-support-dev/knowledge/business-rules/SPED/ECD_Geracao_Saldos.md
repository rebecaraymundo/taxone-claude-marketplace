# ECD_Geracao_Saldos

> Fonte: ECD_Geracao_Saldos.docx


ECD - Geração de Saldos
Localização: TAXONE >> SPED >> ECD – Escrituração Contábil Digital >> Geração >> SALDOS


DOCUMENTO DE REQUISITO











Sumário

1.	Objetivo	3
2.	TELA	3
3.	Regras dos Campos	3
4.	Processo	5























REGRAS DE NEGÓCIO


## Objetivo


A funcionalidade de Geração de Saldos foi criada, para não precisar importar a SAFX02- Arquivos de Saldos Mensais. Os saldos serão criados, considerando o saldo final do período anterior (tabela de saldos X02), e a movimentação do período (lançamentos contábeis da X01). O pré-requisito é que seja informado o saldo final do período anterior ao período que está sendo indicado na tela.

Obs.: Devido necessidade de geração de ECD de Situação Especial, a tela foi alterada, sendo incluído os Campo de Data Inicial e Data Final, que permitirá ao usuário definir as datas dos Campos de Saldo Inicial e Saldo final, conforme necessidade do cliente.


## TELA




## Regras dos Campos


Localização da tela:  TAXONE> SPED > ECD-Escrituração Contábil Digital > Geração > Saldos

Título da tela: Geração de Saldos Contábeis




## Processo





| MFS | Nome | Descrição |
| --- | --- | --- |
| MFS-581991 | Alessandra Cristina Navatta | Internalização de customização: Criada a reversa, porém, o customizado foi ajustado para gravar na tabela definitiva do saldo (X02 e não na SAFX02), alterado o período de geração do relatório (apenas o mês será solicitado, originalmente, estava sendo solicitado data inicial e data final). Ajustado o processo para sempre deletar os registros da X02, quando o tipo de execução for “GERAR - X02”  A funcionalidade será disponibilizada apenas no Tax One. Será permitida a geração de registros de saldos a partir dos saldos final do período anterior (safx02) e do movimento do período (safx01).  Para o correto funcionamento, é necessário a carga inicial do saldo, os períodos seguintes passam a ser processados por essa nova funcionalidade. |
| MFS-621819 | Denilson André Santos | Este documento, tem como objetivo, descrever a recuperação do saldo final do período anterior que, será o saldo inicial do período vigente/informado em tela |
| MFS-898505 | Rogério Ohashi | Este documento tem por objetivo de alterar o campo de Período, que agora possibilita o usuário inserir as informações dos campos de Data Inicial e Data Final do da tabela X02_SALDOS, caso o parâmetro de Situação Especial estiver marcado. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS |
| --- | --- | --- | --- | --- | --- | --- |
| Empresa | Lista | S | S |  | Apresenta todas as empresas que usuário tem acesso. | MFS-581991 |
| Estabelecimento | Lista | S | S |  | Apresenta os estabelecimentos que o usuário tem acesso, da empresa que foi selecionada. | MFS-581991 |
| Data Inicial | Data | S | S | DD/MM/AAAA | Informar o período para a geração/consulta dos saldos.  O sistema deve apresentar o dia/mês/ano da data do campo de Saldo Inicial. | MFS-581991 MFS-898505 |
| Data Final | Data | S | S | DD/MM/AAAA | O sistema deve apresentar o dia/mês/ano da data do campo de Saldo Final. | MFS-898505 |
| Situação Especial | Checkbox | N | S | Default: Desmarcado | Caso a entrega se referir a uma Entrega de Situação Especial, a geração respeitará a data inicial e data final conforme preenchido na tela | MFS-898505 |
| Tipo de Execução | Lista | S | S | CONSULTAR - X02 | Lista de valores válidos:  GERAR - X02 CONSULTAR - X02 | MFS-581991 |
| Executar |  |  |  |  | Mensagem de Campos Obrigatórios:  Se não for informado a Empresa, exibir a mensagem: “Informe a Empresa) Se não for informado o Estabelecimento, exibir a mensagem: “Informe o Estabelecimento) Se não for informado o Período, exibir a mensagem: “Informe o Período) Ao gerar, se não existir no período movimentação (lançamentos contábeis) e no período imediatamente anterior não existir saldos contábeis, mas, se existir saldos, anteriores ao período imediatamente anterior, exibir a mensagem no log: “Não há saldos gerados para o período anterior e movimento para o período atual.” | MFS-581991 |


| RN | REGRAS | MFS |
| --- | --- | --- |
| RN00 | Fluxo deste processo:  Quando o tipo de Execução for CONSULTAR X02: Será exibida as informações da tabela de saldos contábeis (X02) que já estão na base (criadas ou não por este processo), da empresa, estabelecimento e período indicados em tela.   Quando o tipo de Execução for GERAR X02: Para a empresa/estabelecimento, indicado em tela, considerar os registros de cada conta contábil movimentada (lançamentos contábeis da X01) do mês indicado na geração. Ou se não existir movimentação (lançamentos contábeis da X01), considerar as informações da tabela de saldos (X02), do período anterior ao mês indicado na tela. Cada vez que esse processo é realizado, é feito a deleção dos registros da X02 existentes antes de criar novamente os registros. Conforme passos abaixo:  Recuperar saldo final (X02) do estabelecimento, do período anterior ao indicado na tela  Recupera a Movimentação da tabela de Lançamentos Contábeis (X01) do período, do estabelecimento (ambos indicados em tela) Soma todos os lançamentos a crédito (do estabelecimento e período indicado em tela). Soma todos os lançamentos a débito (do estabelecimento do período indicado em tela).  Calcular o Saldo Final do período para o estabelecimento. Gravar as Informações na Tabela de Saldo (X02)  O detalhe de cada passo acima será indicado nas regras abaixo: | MFS-581991 |
| RN01 | Saldo Final do período anterior:  Se existir movimentação (lançamentos contábeis na X01), no período indicado em tela: Recuperar na X02, o saldo final e o indicador, ambos, do período anterior. O saldo final na X02, obrigatoriamente, precisa estar imputado com o último dia do mês, que, pode variar entre os dias 28, 29, 30, 31. Uma vez encontrada a informação, os dados serão gravados no campo de saldo inicial e indicador do período vigente, ou seja, do período informado em tela.   Caso não encontre na X02, o saldo final do período anterior, imputado com um o último dia do mês, o saldo inicial a ser gravado para o período informado em tela, será zero (0,00).  Se NÃO existir movimentação (lançamentos contábeis X01) no período indicado em tela:   Caso não haja movimentação no período (dados na X01), mas, existir saldos anteriores (X02), o saldo inicial e final do período serão iguais ao saldo final do último mês encontrado.  Conta de Contrapartida Este processo, não gera automaticamente os saldos para a conta de contrapartida, se informado no lançamento contábil (campo 08 – CONTRA_PART da X01). | MFS-581991 MFS-621819 |
| RN02 | Total de Crédito e Total de Débito:  Recuperar a movimentação do período tabela X01 (definitiva), da empresa, estabelecimento e período indicado na tela e  Somar todos os lançamentos a crédito do mês indicado na tela de geração. Gravar no campo Total Crédito Somar todos os lançamentos a débito do mês indicado na tela de geração. Gravar no campo Total Débito | MFS-581991 |
| RN03 | Cálculo do saldo final:  Calcular o saldo atual com base no saldo final anterior e as somas dos lançamentos a débito e a crédito no período.   Efetuar o cálculo para encontrar o valor do saldo final:  Saldo Inicial (RN01) + Totais de Créditos (RN02) + Totais de Débitos (RN02)   Lembrando que se o saldo anterior, for devedor, deverá ser somado os lançamentos de débito e subtraído de crédito, e vice-versa. Faça sempre a diferença entre débito e crédito e mantenha o indicador do maior valor (débito ou crédito).  Indicador quando o saldo final for zero:  Se o saldo inicial for Crédito, considerar ‘C’. Se for Débito, considerar ‘D’ | MFS-581991 |
| RN04 | Gravação das informações na X02: | MFS-581991 |
| RN05 | ABA LOG  Quando o tipo de Execução for: GERAR - X02  Apresentar no log a quantidade de registros que foram gerados na tabela de saldos. Exibir a mensagem: “Registros gerados na tabela X02_SALDOS: << qtd de registros >>”    Quando o tipo de Execução for: CONSULTAR - X02: Apresentar no log a quantidade de registros, conforme exemplo: | MFS-581991 |
| RN06 | ABA RELATÓRIO DE CONSULTA  Apresentar relatorio com as informações da consulta dos saldos (ordenados por conta contábil), conforme exemplo abaixo: ABA RELATÓRIO  DE REGISTROS INSERIDOS:  Apresentar relatorio com as informações dos saldos criados, conforme exemplo abaixo: | MFS-581991 |
