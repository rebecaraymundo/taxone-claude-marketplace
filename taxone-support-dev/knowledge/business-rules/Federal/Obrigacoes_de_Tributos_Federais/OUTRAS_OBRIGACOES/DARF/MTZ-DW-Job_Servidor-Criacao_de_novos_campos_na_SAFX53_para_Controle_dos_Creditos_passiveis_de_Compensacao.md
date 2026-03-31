# MTZ-DW-Job_Servidor-Criacao_de_novos_campos_na_SAFX53_para_Controle_dos_Creditos_passiveis_de_Compensacao

- **Fonte:** MTZ-DW-Job_Servidor-Criacao_de_novos_campos_na_SAFX53_para_Controle_dos_Creditos_passiveis_de_Compensacao.docx
- **Modificado:** 2020-08-29
- **Tamanho:** 41 KB

---

# DW e Job Servidor \- Criação de novos campos na SAFX53 para Controle dos Créditos passíveis de Compensação

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3267

DW e Job Servidor \- Criação de novos campos na SAFX53 para Controle dos Créditos passíveis de Compensação

Será desenvolvida uma rotina para que a Sul América carregue e importe as informações das retenções a partir da tabela SAFX53 e possa retificar as vindouras retenções erradas\.

#### Cód\.

### Descrição

### DR

# RN00

Deverão ser criados na tabela SAFX53 os seguintes campos:

- __Data de Cancelamento:__ trata\-se da Data de Cancelamento da Retenção que irá controlar os Tributos retidos incorretamente e que devem ser cancelados\. Esse campo deverá ser do tipo numérico de 8 posições\. A data deverá ser informada no formato AAAAMMDD\. Campo não obrigatório de preenchimento\. 
- __Cancelado:__ trata\-se do campo que irá identificar se a retenção é Cancelada ou não\. Esse campo deverá ser do tipo alfanumérico de 1 posição\. Campo não obrigatório de preenchimento\. O campo deverá possuir apenas duas opções válidas:
	- S – retenção cancelada
	- N – retenção não cancelada
- __Número do Voucher:__ trata\-se do campo que irá identificar o Número do Lançamento Financeiro\. Esse campo deverá ser do tipo alfanumérico de 50 posições\. Campo não obrigatório de preenchimento\.
- __Data de Retificação:__ trata\-se da Data de Retificação da Retenção que irá controlar as os tributos retidos incorretamente a maior ou a menor\. Esse campo deverá ser do tipo numérico com 8 posições\. A data deverá ser informada no formato AAAAMMDD\. Campo não obrigatório de preenchimento\. Esse campo só deverá ser obrigatório no processo de Importação Online ou Importação Batch caso o parâmetro “Importar Retificações de Retenções” esteja marcado\.

OS3267

# RN01

Deverão ser criados na tabela X53\_RETENCAO\_IRRF os seguintes campos:

- __Data de Cancelamento:__ Trata\-se da Data de Cancelamento da Retenção que irá controlar os Tributos retidos incorretamente e que devem ser cancelados\. Esse campo deverá ser do tipo numérico de 8 posições\. A data deverá ser informada no formato dd/mm/aaaa\. Campo não obrigatório de preenchimento\. Esse campo só será obrigatório de preenchimento caso o campo “Cancelado” esteja informado como “S”\. Caso o campo “Cancelado” esteja informado como “N” esse campo não deverá ser informado\. 
- __Cancelado:__ Trata\-se do campo que irá identificar se a retenção é Cancelada ou não\. Esse campo deverá ser do tipo alfanumérico de 1 posição\. Campo não obrigatório de preenchimento\. O campo deverá possuir apenas duas opções válidas:
	- S – retenção cancelada
	- N – retenção não cancelada
- __Número do Voucher:__ Trata\-se do campo que irá identificar o Número do Lançamento Financeiro\. Esse campo deverá ser do tipo alfanumérico de 50 posições\. Campo não obrigatório de preenchimento\.

OS3267

# RN02

A tabela X530\_RETIFICACAO\_IRRF deverá ser criada contendo todos os campos da SAFX53 com os mesmos domínios e tamanhos já estabelecidos \(ver Manual de Layout\)\.

Além desses campos na nova tabela X530\_RETIFICACAO\_IRRF, deverão ser incluídos os seguintes campos:

- __Data de Retificação:__ deverá ser um campo do tipo numérico com 8 posições\. A data deverá ser informada no formato dd/mm/aaaa\. Campo obrigatório de preenchimento\.
- __Número do Voucher:__ deverá ser um campo do tipo alfanumérico de 50 posições\. Será informado nesse campo o Número do Lançamento Financeiro referente à retenção\. Campo não obrigatório de preenchimento\.

Os campos “Data Cancelamento” e “Cancelado” que estão sendo criados nessa OS na tabela SAFX53, __não deverão constar__ na tabela X530\_RETIFICACAO\_IRRF\.

Uma retenção irá possuir varias retificações\. A Data de Retificação irá diferenciar uma retenção da outra\.

OS3267

# RN03

A rotina de Carga do Job Servidor deverá prever a inclusão dos campos “Data de Cancelamento”, “Cancelado“, “Número do Voucher” e “Data de Retificação” na tabela SAFX53\.

As rotinas de Importação Online e Importação Batch deverão prever a inclusão dos campos “Data de Cancelamento”, “Cancelado“, “Número do Voucher” na tabela X53\_RETENCAO\_IRRF\. Essas mesmas rotinas deverão prever a inclusão dos campos “Data de Retificação” e “Número do Voucher” na tabela X530\_RETIFICACAO\_IRRF\.

A rotina de Exportação do módulo Job Servidor deverá prever a inclusão dos campos “Data de Cancelamento”, “Cancelado“, “Número do Voucher” e “Data de Retificação” para a tabela SAFX53\. A rotina de Exportação da SAFX53 irá conter as retenções da X53\_RETENCAO\_IRRF e as retificações das retenções da X530\_RETIFICACAO\_IRRF\.

OS3267

# RN04

Será disponibilizado o seguinte campo na tela:

- __Data de Cancelamento:__ deverá ser um campo do tipo numérico com 8 posições\. A data deverá ser informada no formato dd/mm/aaaa\. Campo não obrigatório de preenchimento\.
- __Cancelado:__ deverá ser um campo do tipo alfanumérico de 1 posição\. Caso o documento seja cancelado o flag deverá estar marcado, caso contrário não deverá estar marcado\. Campo não obrigatório de preenchimento\.
- __Número do Voucher:__ deverá ser um campo do tipo alfanumérico de 50 posições\. Será informado nesse campo o Número do Lançamento Financeiro referente à retenção\. O campo só pode ser alterado caso o campo Situação DARF = N\.

Os campos “Data de Cancelamento” e “Cancelado” só podem ficar habilitados caso a retenção já esteja paga e caso o campo SITUACAO\_X751 = N\.

Caso o campo “Cancelado” esteja selecionado, e o usuário tente salvar a retenção sem a “Data de Cancelamento” preenchida, deverá ser exibida uma mensagem de erro informando do fato e impedir a gravação\. Essa regra para o caso contrário, ou seja, caso a “Data de Cancelamento” seja informada sem o flag do campo “Cancelado”\.

OS3267

# RN05

O relatório de conferência dessa tela deverá ser alterado\.

OS3267

# RN06

Na tela de pesquisa das retenções cadastradas na manutenção de controle de tributos – tabela: X53\_DCTF – os campos “Data de Cancelamento”, “Cancelado” e “Número do Voucher” deverão ser informados para que a pesquisa possa ser realizada por esses campos também\.

OS3267

# RN07

Deverá ser criado o parâmetro “Importar Retificações de Retenções”\. Esse parâmetro será disponibilizado na tela de programação da Importação Online\. Serão exibidas duas opções: “Sim” e “Não”\. Caso seja selecionada a opção “Sim”, todas as retificações das retenções que estiverem sendo importadas e já existirem com status “Pago” na X53\_RETENCAO\_IRRF, serão importadas para a tabela X530\_RETIFICACAO\_IRRF\. Caso seja selecionada a opção “Não”, as retificações não serão importadas para a tabela X530\_RETIFICACAO\_IRRF\. Esse parâmetro só será disponibilizado para a tabela SAFX53\.

A regra da utilização do parâmetro no processo de importação é o seguinte:

- Caso a retenção que será importada esteja com status = Pago na tabela X53\_RETENCAO\_IRRF, e a mesma possua a Data de Retificação preenchida, deverá ser gravado o registro na tabela X530\_RETIFICACAO\_IRRF, assim como a Data de Retificação no campo “Data de Retificação” desse registro na tabela X530\_RETIFICACAO\_IRRF\. Esse registro gravado na X530\_RETIFICACAO\_IRRF será considerado a retificação\.

O parâmetro “Importar Retificações de Retenções” será criado após o campo “Data Averb\. X48”\.

OS3267

# RN08

Deverá ser criado o parâmetro “Importar Retificações de Retenções”\. Esse parâmetro será disponibilizado na tela de programação da Importação Batch\. Serão exibidas duas opções: “Sim” e “Não”\. Caso seja selecionada a opção “Sim”, todas as retificações das retenções que estiverem sendo importadas e já existirem com status “Pago” na X53\_RETENCAO\_IRRF, serão importadas para a tabela X530\_RETIFICACAO\_IRRF\. Caso seja selecionada a opção “Não”, as retificações não serão importadas para a tabela X530\_RETIFICACAO\_IRRF\. Esse parâmetro só será disponibilizado para a tabela SAFX53\.

A regra da utilização do parâmetro no processo de importação é o seguinte:

- Caso a retenção que será importada esteja com status = Pago na tabela X53\_RETENCAO\_IRRF, e a mesma possua a Data de Retificação preenchida, deverá ser gravado o registro na tabela X530\_RETIFICACAO\_IRRF, assim como a Data de Retificação no campo “Data de Retificação” desse registro na tabela X530\_RETIFICACAO\_IRRF\. Esse registro gravado na X530\_RETIFICACAO\_IRRF será considerado a retificação\.

O parâmetro “Importar Retificações de Retenções” será criado após o campo “Data Averb\. X48”\.

OS3267

# RN09

Caso a retenção que será importada esteja com status = Pago e SITUACAO\_X751 = N na tabela X53\_RETENCAO\_IRRF, e a mesma esteja com Indicador de Cancelamento = Cancelada, deverá ser alterado o registro já pago na tabela X53\_RETENCAO\_IRRF e gravada a Data de Cancelamento no campo “Data de Cancelamento” desse mesmo registro na tabela X53\_RETENCAO\_IRRF\.

Nesse caso o flag “Cancelado” deverá ser alterado de acordo com a informação a ser importada\.

Nos casos das retenções canceladas, o parâmetro “Importar Retificações de Retenções” não será determinante para o cancelamento da retenção\.

OS3267

# RN10

Durante a rotina de processamento da Importação Online ou Batch, deverão ser exibidas mensagens de erro impedindo a importação nos seguintes casos de cancelamento:

__Cancelamento da Retenção__

- Campo “Cancelado” = Sim e campo “Data Cancelamento” não preenchido
	- Mensagem: “Retenção inválida, pois possui indicação de cancelamento, mas está sem Data de Cancelamento preenchida\.”
- Campo “Cancelado” = Não e campo “Data Cancelamento” preenchido
	- Mensagem: “Retenção inválida, pois possui indicação de cancelamento, mas está sem Data de Cancelamento preenchida\.”
- Campo “Data Retificação” preenchido, assim como os campos “Cancelado” = Sim e/ou “Data Cancelamento” preenchido\.
	- Mensagem: “Retenção inválida, pois possui informações de cancelamento e retificação simultaneamente\.”
- Campo “Cancelado” = Sim e não existe retenção com a mesma chave na X53\_RETENCAO\_IRRF\.
	- Mensagem: “Retenção inválida, pois possui indicação de cancelamento e a mesma não se encontra na base\. Somente Retenções já existentes na base na situação de Darf pago podem ser canceladas\.”
- Campo “Cancelado” = Sim e retenção na X53\_RETENCAO\_IRRF com campo SITUACAO = ‘N’
	- Mensagem: “Retenção inválida, pois possui indicação de cancelamento e a mesma se encontra na base na situação de Darf não gerado\. Somente Retenções existentes na base na situação de Darf Pago podem ser canceladas\.”
- Campo “Cancelado” = Sim e retenção na X53\_RETENCAO\_IRRF com campo SITUACAO = ‘G’
	- Mensagem: “14080 – Retenção inválida, pois já se encontra na base referenciada a um DARF gerado\.”
- Campo “Cancelado” = @ e retenção na X53\_RETENCAO\_IRRF com campo SITUACAO = ‘P’
	- Mensagem: “Retenção inválida, pois já se encontra na base referenciada a um DARF pago\.”
- Campo “Cancelado” = Sim ou Não e retenção na X53\_RETENCAO\_IRRF com campo SITUACAO = ‘P’ e campo SITUACAO\_X751 <> ‘N’
	- Mensagem: “Retenção inválida pois já se encontra referenciada a um Darf Complementar ou a uma Compensação de Crédito\.”

OS3267

# RN11

Deverá ser criada a tela de manutenção “Controle de Tributos Retificados”\. Essa tela irá conter as informações da  tabela X530\_RETIFICACAO\_IRRF que nada mais são do que as retificações das retenções já pagas cujos valores foram alterados\. 

O processo de importação da tabela X530\_RETIFICACAO\_IRRF será através da importação da tabela SAFX53\.

OS3267

# RN12

A tela Controle de Tributos Retificados será disponibiliza no módulo DW, através do menu Manutenção >> Controle de Tributos Retificados\. Esse menu ficará disponível abaixo do menu Manutenção >> Controle de Tributos\. A tela de manutenção das Retenções e a tela de manutenção das Retificações, serão disponibilizadas através do mesmo menu, porém em abas distintas: Retenção e Retificações\.

OS3267

# RN13

Os campos que irão compor essa tela são os mesmos campos da tela de Controle de Tributos, exceto os campos “Data de Cancelamento” e “Cancelado”\. Essa tela irá possuir também os seguintes campos:

- __Data de Retificação:__ deverá ser um campo do tipo data no formato dd/mm/aaaa\. Campo obrigatório de preenchimento\.
- __Número do Voucher:__ deverá ser um campo do tipo alfanumérico de 50 posições\. Campo não obrigatório de preenchimento\.
- __Situação DARF Complementar/Compensação Crédito:__ deverá ser um campo que irá exibir as opções “Não Gerado”, “Gerado/Não Pago” e “Pago”\. Essas opções variam conforme a geração da rotina de DARF’s nas retificações:
	- *Não Gerado:* deverá ser exibida essa opção, caso a retificação ainda não tenha sido considerada na rotina de geração dos DARF’s\.
	- *Gerado/Não Pago:* deverá ser exibida essa opção, caso a retificação tenha sido gerada através dos DARF’s, porém ainda não tenha sido paga\.
	- *Pago:* deverá ser exibida essa opção, caso o DARF gerado a partir da retificação tenha sido pago\.

Caso o campo SITUACAO\_X751 <>  N irá bloquear todos os campos para edição\.

Todas as críticas/validações da tela de Controle de Tributos deverão existir nessa tela, exceto a crítica da alteração de campos na tela para inclusão de justificativa\.

OS3267

# RN14

Deverá ser criado um relatório de conferência dessa tela\.

OS3267

# RN15

Deverá ser criado o parâmetro “Exportar Retificações de Retenções”\. Esse parâmetro será disponibilizado na tela de programação da Exportação de Dados, após a coluna “Tabela Temp\.”\. Serão exibidas duas opções: “Sim” e “Não”\.

OS3267

# RN16

Deverá ser criado o parâmetro “Exportar Retificações de Retenções”\. Esse parâmetro será disponibilizado na tela de execução da Exportação de Dados, após a coluna “Tabela Temp\.”\. Serão exibidas as opções “Sim” ou “Não” de acordo com a programação parametrizada\.

A regra da utilização do parâmetro no processo de importação é o seguinte:

- Caso o parâmetro “Exportar Retificações de Retenções” esteja selecionado com a opção “Sim” na tela de Programação para a Exportação de Dados da tabela SAFX53, a exportação irá considerar as retenções existentes na X53\_RETENCAO\_IRRF e as retificações das retenções existentes na X530\_RETIFICACAO\_IRRF no arquivo exportado\.
- Caso o parâmetro “Exportar Retificações de Retenções” esteja selecionado com a opção “Não” na tela de Programação para a Exportação de Dados da tabela SAFX53, a exportação irá considerar apenas as retenções existentes na X53\_RETENCAO\_IRRF e __NÃO IRÁ CONSIDERAR__ as retificações das retenções existentes na X530\_RETIFICACAO\_IRRF no arquivo exportado\.

OS3267

# RN17

Deverá ser criado o parâmetro “Importar Retificações de Retenções” como um novo campo na tela de Execução da Importação Online\. Esse parâmetro irá exibir a opção selecionada de acordo com a programação selecionada no campo “Job de Importação”\.

O parâmetro “Importar Retificações de Retenções” será criado após o campo “Data Averb\. X48”\.

OS3267

# RN18

Durante a rotina de processamento da Importação Online ou Batch, deverão ser exibidas mensagens de erro impedindo a importação nos seguintes casos de retificação da retenção:

__Retificação da Retenção__

- Retenção com campo “Data Retificação” informado, porém parâmetro “Importar Retificações de Retenções” das rotinas Importação Online OU Importação Batch não está selecionado\.
	- Mensagem: “Não foi possível importar a Retificação da Retenção, pois a opção Importar Retificações de Retenções não foi selecionada”\.
- Retenção com campo “Data Retificação” informado, porém não existe retenção existente com mesma chave na tabela X53\_RETENCAO\_IRRF\.
	- Mensagem: “Retificação inválida, pois não existe na base retenção referente a retificação, ou a retenção não está com situação de Darf pago”\.
- Retenção com campo “Data Retificação” informado, porém a retenção existente com mesma chave na tabela X53\_RETENCAO\_IRRF está com o campo SITUACAO = ‘N’ ou nulo
	- Mensagem: “Retificação inválida, pois não existe na base retenção referente a retificação, ou a retenção não está com situação de Darf pago”\.
- Retenção com campo “Data Retificação” informado, porém a retenção existente com mesma chave na tabela X53\_RETENCAO\_IRRF está com o campo SITUACAO = ‘G’
	- Mensagem: “Retificação inválida, pois não existe na base retenção referente a retificação, ou a retenção não está com situação de Darf pago”\.
- Retenção com campo “Data Retificação” informado \(B\), e a retenção existente na X53\_RETENCAO\_IRRF está com o campo SITUACAO = ‘P’ E não existe retificação da retenção dessa mesma chave na X530\_RETIFICACAO\_IRRF \(B\) E existe uma outra retificação da retenção na X530\_RETIFICACAO\_IRRF \(A\), porém a “Data da Retificação” da retificação \(B\) < “Data Retificação” da retificação \(A\) e o campo SITUACAO\_X751 <> ‘N’\.
	- Mensagem: “Retificação inválida, pois a retenção referenciada possui uma Retificação com data anterior que já está referenciada a um Darf Complementar ou a uma Compensação de Crédito\.”
- Retenção com campo “Data Retificação” informado, e a retenção da X53\_RETENCAO\_IRRF está com o campo SITUACAO = ‘P’ e existe na X530\_RETIFICACAO\_IRRF registro com campo SITUACAO\_X751 <> ‘N’
	- Mensagem: “Retificação inválida, pois a mesma já se encontra referenciada a um Darf Complementar ou a uma Compensação de Crédito\.

OS3267

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

