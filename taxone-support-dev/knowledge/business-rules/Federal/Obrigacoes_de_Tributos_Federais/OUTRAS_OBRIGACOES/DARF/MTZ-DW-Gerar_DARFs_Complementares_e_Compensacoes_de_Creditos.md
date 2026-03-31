# MTZ-DW-Gerar_DARFs_Complementares_e_Compensacoes_de_Creditos

- **Fonte:** MTZ-DW-Gerar_DARFs_Complementares_e_Compensacoes_de_Creditos.docx
- **Modificado:** 2023-03-13
- **Tamanho:** 56 KB

---

# Obrigações de Tributos Federais \- Gerar DARF's Complementares e Compensações de Créditos

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3267\-A

Obrigações de Tributos Federais \- Gerar DARF's Complementares e Compensações de Créditos

Será desenvolvida uma rotina para que a Sul América após a carga e importação da SAFX53 e a importação das retificações na tabela X530\_RETIFICACAO\_IRRF, possa informar o Saldo Inicial Credor inicial de créditos passados, gerar os DARF’s, calcular os Débitos e Créditos para que sejam realizadas as comparações entre as tabelas e determinar se há geração de DARF’s Complementares ou geração de Compensação\.

OS3267\-B2

Obrigações de Tributos Federais \- Geração da DCTF a partir das Retenções e Retificações das Retenções – Registros de Compensação R12 e R13

Será desenvolvida uma rotina para que a Sul América informe automaticamente na DCTF o respectivo valor dos créditos que estão sendo compensados na obrigação acessória\.

OS3699

Obrigações de Tributos Federais \- Atualização Legal da DCTF para a versão 2\.4

Trata\-se da atualização legal da DCTF para a versão 2\.4\.

OS3913

Obrigações de Tributos Federais – Inclusão da opção “Pagamento Indevido ou a Maior” na tela de Saldo Credor Inicial

O objetivo deste documento de requisito é permitir que o cliente cadastre os saldos credores iniciais classificamos como “Pagamento Indevido ou a Maior” na tela de Saldo Credor Inicial\.

Vale salientar que essa funcionalidade foi concebida \(OS3267\-A\) para que os saldos credores iniciais que fazem parte da ficha R13 – Outras Compensações da DCTF fossem cadastrados nessa tela\. Ocorre que o cliente Sul América possui saldos credores iniciais com essa classificação que deverão fazer parte da ficha R12 – Compensação de Pagamento Indevido ou a Maior\.

OS3857

Obrigações de Tributos Federais – Exibir Empresa e Estabelecimento logados na Geração do DARF

O cliente gostaria de visualizar no momento de geração dos DARF’s somente a Empresa e o Estabelecimento que está selecionado no Manager\. Isso se deve ao fato de que no cliente MRV, para a empresa 001 existem 688 estabelecimentos cadastrados, na empresa 002 existem 31 estabelecimentos e na empresa 003 existem 23 estabelecimentos\. Atualmente são 267 empresas licenciadas no Mastersaf\. Para gerar somente os estabelecimentos da empresa 001, o cliente tem que selecionar 688 estabelecimentos um a um\. Se for marcado o parâmetro "Selecionar todos", o sistema seleciona todos os estabelecimentos de todas as empresas e faz a geração dos DARF's para todas elas \(1035 estabelecimentos no total\)\. Isso gera um tempo maior de processamento por parte do cliente\.

No caso o cliente solicita uma forma de que seja exibido somente a Empresa selecionada no Manager e seus respectivos Estabelecimentos\. Ocorre que se a solução não for parametrizável, muitos clientes que já geram para todas as Empresas e Estabelecimentos seriam onerados, pois teriam que entrar e sair do módulo várias vezes\. 

Nesse caso será criado um parâmetro para seleção da Empresa informada no Manager\.

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

CH29336\_2013

Obrigações de Tributos Federais –

O objetivo deste documento de requisitos é definir as regras de aplicação de juros de mora – ou juros – para os DARF’s pagos em atraso\.

OS4620\-A

Ajuste na tela de Saldo Credor para Compensação dos Tributos Federais

Ajustes para atender à atualização da versão 3\.1 do layout da DCTF

#### Cód\.

### Descrição

### DR

# RN00

Deverá ser criado um novo parâmetro na tela de Parâmetros por DARF/GPS\. Esse novo parâmetro deverá ser chamado “Permitir Compensações e DARF’s Complementares”\. Por default, esse parâmetro deverá ser exibido desmarcado\.

O objetivo desse novo parâmetro é que uma vez selecionado, toda a sistemática para cálculo dos DARF’s Complementares e das Compensações que estão sendo criados na família de OS’s 3267 seja utilizado\. Uma vez desmarcado, o parâmetro não utilizará essa rotina e os DARF’s serão gerados conforme a regra atual, ou seja, recuperando as informações exclusivamente da tabela X53\_RETENCAO\_IRRF com Situação = Não Gerado e gerando os DARF’s\.

Quando o parâmetro “Permitir Compensações e DARF’s Complementares” estiver selecionado, a tela de Geração dos DARF’s \(menu: Outras Obrigações >> DARF’s >> Geração a partir das Retenções\) do módulo Obrigações de Tributos Federais será alterada conforme regras da tela de Geração dos DARF’s\. Caso contrário, a tela no padrão antigo \(atual\) será mantida para visualização\.

OS3267\-A

# RN01

Deverá ser criada uma nova tela chamada “Saldo Credor para Compensação dos Tributos Federais”\. Essa tela será disponibilizada no menu Outras Obrigações >> DARF’s >> Saldo Credor para Compensação dos Tributos Federais do módulo Obrigações de Tributos Federais\.

Essa tela permitirá que através da Empresa e Estabelecimento, seja associado para cada Código DARF um valor inicial de Saldo Credor Inicial\. Esse valor irá influenciar a compensação de DARF’s a serem gerados\. As operações permitidas nessa tela serão inclusão, consulta, alteração e exclusão\.

O saldo pode ser alterado ou excluído, caso o mesmo ainda não tenha sido utilizado na rotina de Compensação de Créditos de Tributos Federais\. Caso o usuário tente alterar ou excluir um saldo que já tenha sido utilizado parcialmente ou totalmente, deverá ser exibida a seguinte mensagem de erro: “Saldo Credor não pode ser alterado/excluído, pois o mesmo já foi utilizado parcialmente ou totalmente\.”\.

Os campos chave dessa tela serão Empresa, Estabelecimento, Código DARF, Data de Pagamento e Data de Vencimento\.

O usuário poderá informar quantos saldos credores forem necessários desde que a chave da tabela seja respeitada – Código da Empresa, Código do Estabelecimento, Data de Pagamento e Data de Vencimento\.

OS3267\-A

# RN02

Deverá ser criado um relatório de conferência para essa tela\.

OS3267\-A

# RN03

__\[ALTERADA – OS3913\] __Os seguintes campos ficarão disponíveis na tela:

- __Empresa:__ deverá ser selecionada a Empresa para parametrização\. A informação será recuperada através dos campos COD\_EMPRESA e RAZAO\_SOCIAL da tabela EMPRESA\. Essas informações serão exibidas separadas por “\-“\. Por padrão, será exibida a empresa informada no Manager\.
- __Estabelecimento:__ deverá ser selecionado um Estabelecimento para parametrização\. A informação será recuperada através dos campos COD\_ESTAB e RAZAO\_SOCIAL da tabela ESTABELECIMENTO\. Essas informações serão exibidas separadas por “\-“\. Por padrão, será exibido o estabelecimento informado no Manager\. 
- __Data Pagamento:__ deverá ser informada a Data de Pagamento do DARF que deu origem ao Saldo Credor\. A Data de Pagamento deverá ser informada no formato DD/MM/AAAA\. Campo obrigatório de preenchimento\.
- __Código DARF:__ o usuário poderá selecionar os Códigos DARF’s existentes\. A informação será recuperada dos campos COD\_DARF \+ DESCRICAO da tabela X2019\_COD\_DARF\. Campo obrigatório de preenchimento\.
- __Valor Pago DARF:__ o usuário deverá informar o Valor Pago do DARF que deu origem ao Saldo Credor na época que o mesmo foi compensado\. Deverá ser um campo numérico de 17 \(dezessete\) posições, sendo 15 \(quinze\) inteiras e 2 \(duas\) casas decimais\. Campo obrigatório de preenchimento\.
- __Data Vencimento:__ deverá ser informada a Data de Vencimento do DARF que deu origem ao Saldo Credor\. A Data de Vencimento deverá ser informada no formato DD/MM/AAAA\. Campo obrigatório de preenchimento\.
- __Observação:__ deverá ser informada uma Observação relacionada ao Saldo Credor\. Deverá ser um campo alfanumérico de 50 \(cinqüenta\) posições\. Campo não obrigatório de preenchimento\.
- __Valor a Compensar:__ deverá ser informado o Saldo Credor para compensação de débitos futuros\. Deverá ser um campo numérico de 17 \(dezessete\) posições, sendo 15 \(quinze\) inteiras e 2 \(duas\) casas decimais\. Campo obrigatório de preenchimento\. Não poderá ser informado o valor 0,00, caso isso ocorra deverá ser exibida mensagem de erro informando do fato\. Além disso, caso o valor informado nesse campo seja maior que o valor informado no campo “Valor Pago DARF”, deverá ser informada mensagem de erro impossibilitando a gravação/alteração do registro\.
- __Valor Compensado:__ será informado o Valor já Compensado em relação ao campo “Valor a Compensar”\. Esse campo não poderá ser alterado e o mesmo será calculado a partir da rotina de Débitos/Créditos, para nos casos de quando o crédito informado no campo “Valor a Compensar” for utilizado, essa quantidade utilizada ser informada nesse campo\. Como esse campo é calculado pelo sistema, caso o mesmo seja maior que 0 \(zero\), esse registro não pode ser alterado, exceto os campos “Número Documento Pagamento” e “Número Processo”\. Esse campo não deve ser aberto para edição em nenhuma hipótese\.
- __Saldo:__ será informado o Saldo do crédito\. Esse campo será calculado a partir da rotina de Débitos/Créditos\. O resultado do mesmo será o valor informado na coluna “Valor a Compensar” – “Valor Compensado”\. O saldo nunca deverá ser menor que 0 \(zero\)\.
- __Número Documento Pagamento:__ deverá ser informado o Número Documento Pagamento referente ao DARF que deu origem ao Saldo Credor\. Deverá ser um campo alfanumérico de 50 \(cinqüenta\) posições\. Campo não obrigatório de preenchimento\.
- __Tipo de Crédito:__ deverá será informado o Tipo de Crédito do Saldo Credor\. Esse tipo de Crédito irá compor a Ficha R13 – Outras Compensações da obrigação acessória DCTF\. Campo não obrigatório de preenchimento\. Serão exibidas as seguintes opções para serem selecionadas\.
	- Pagamento Indevido ou a Maior \(vale salientar que essa opção pode ser gravada como “99”, visto que não será utilizada para geração do registro R13, somente do registro R12 da DCTF\.
	- Ressarcimento de IPI
	- IRPJ Saldo Negativo Per\. Anteriores \- Próprio
	- IRPJ Saldo Negativo Per\. Anteriores \- Sucedida
	- CSLL Saldo Negativo Per\. Anteriores \- Próprio
	- CSLL Saldo Negativo Per\. Anteriores \- Sucedida
	- IRRF Cooperativas de Trabalho
	- IRRF Juros sobre o Capital Próprio
	- Outros
	- PIS/PASEP Não\-Cumulativo \- Exportação
	- Cofins Não\-Cumulativa \- Exportação
	- PIS/PASEP Não\-Cumulativo \- Mercado Interno
	- Cofins Não\-Cumulativa \- Mercado Interno
	- PIS/PASEP Embalagens \(§4º do art\. 51 da Lei nº 10\.833/03\)
	- Cofins Embalagens \(§4º do art\. 51 da Lei nº 10\.833/03\)
	- Reintegra 

Como a versão 3\.1 da DCTF excluiu a Ficha R13, deve ser atribuído um novo tratamento a este campo, sendo que, se a Data do Pagamento informada for menor que 01/08/2014, devem ser exibidas as opções acima listadas\. Se for maior ou igual a 01/08/2014, exibir como opção default a expressão “Compensações” e desabilitar o campo para edição\.

- __Formalização Pedido:__ deverá ser informado a Formalização do Pedido do Crédito que está sendo utilizado\. Campo obrigatório de preenchimento\. Serão exibidas as seguintes opções para serem selecionadas:
	- Processo Administrativo
	- DComp
	- Dcomp com Direito Creditório Reconhecido em Processo – __*OBS: ver maiores detalhes do comportamento da tela na RN20*__
- __Número Processo:__ deverá ser informado o Número do Processo Administrativo ou Judicial que deu origem ao Saldo Credor\. Deverá ser um campo alfanumérico de 24 \(vinte e quatro\) posições\. Campo não obrigatório de preenchimento\.

OS3267\-A

OS3267\-B2

OS3699

OS3913

OS4620\-A

# RN04

A tela de geração dos DARF´s deverá ser mantida, porém a mesma deverá estar vinculada a uma nova aba chamada “Parâmetros de Geração”\. A tela nova com abas só deverá ser visualizada caso o parâmetro “Permitir Compensações e DARF’s Complementares” esteja selecionado\. Caso contrário será exibida a tela atual\.

OS3267\-A

# RN05

__\[ALTERADA – OS3753\-A\] __Ao gerar os DARF’s o cliente deverá clicar no botão “Gerar Prévia dos DARF’s”\. Ao clicar nesse botão os DARF’s serão gerados e gravados nas tabelas X75\_DCTF ou X751\_DCTF\_COMPL, conforme regras abaixo:

- Caso exista alguma retenção sem o campo “Data Vencimento” preenchida, deverá ser exibida mensagem de aviso com o número do log de processo na tela e não deverá impedir a geração do DARF
- Caso a retenção esteja com o flag “Cancelado” = Sim, essa retenção não deverá ser considerada no DARF que será gerado\.
- Caso a retenção da X53\_RETENCAO\_IRRF não possua retificações na tabela X530\_RETIFICACAO\_IRRF, o DARF deve ser gerado e gravado – conforme regras de consolidação preenchidas na tela – na tabela X75\_DCTF com o campo STATUS = ‘G’\.
- Caso a retenção da X53\_RETENCAO\_IRRF possua retificações na tabela X530\_RETIFICACAO\_IRRF, deverá ser comparado o Valor da Retenção da retificação com o Valor da Retenção da Retenção Original\. Caso o Valor da Retificação da Retenção seja maior que o Valor da Retenção Original, o DARF deve ser gerado e gravado  – conforme regras de consolidação preenchidas na tela – na tabela X751\_DCTF\_COMPL com o campo STATUS = ‘G’ e com o campo IND\_DEB\_CRED = ‘D’\.
- Caso a retenção da X53\_RETENCAO\_IRRF possua retificações na tabela X530\_RETIFICACAO\_IRRF, deverá ser comparado o Valor da Retenção da retificação com o Valor da Retenção da Retenção Original\. Caso o Valor da Retificação da Retenção seja menor que o Valor da Retenção Original, o DARF deve ser gerado e gravado  – conforme regras de consolidação preenchidas na tela – na tabela X751\_DCTF\_COMPL com o campo STATUS = ‘G’ e com o campo IND\_DEB\_CRED = ‘C’\.
- Caso a retenção da X53\_RETENCAO\_IRRF esteja paga \(campo STATUS = “P”\) e a mesma esteja Cancelada \(campo IND\_CANCELAMENTO = “S”\) e Data de Cancelamento \(campo DATA\_CANCELAMENTO\) preenchida, o Valor da Retenção \(campo VLR\_IR\_RETIDO\) deverá ser liberado como crédito\. Para que isso aconteça, deve ser gerado um registro na tabela X751\_DCTF\_COMPL com o campo STATUS = ‘G’ e com o campo IND\_DEB\_CRED = ‘C’\.
- Caso a retenção da X53\_RETENCAO\_IRRF esteja com os campos “Estorno” e “Data do Estorno” preenchidos, essa retenção não deverá ser considerada para composição do DARF que esteja sendo gerado\. Vale salientar que essa retenção não possuirá uma retificação \(X530\_RETIFICACAO\_IRRF\) correspondente\. O DARF será gerado sem essa retenção\.

Nesse momento estarão gravados DARF’s nas tabelas X75\_DCTF e X751\_DCTF\_COMPL, porém esses DARF’s ainda não são DARF’s reais e sim apenas prévias dos mesmos\. Esses DARF’s NÃO SERÃO ENVIADOS para o sistema bancário para pagamento\.

Caso o cliente clique no botão “Confirmar/Gerar DARF’s” da aba “Compensações de Crédito/Geração dos DARF’s” os DARF’s gerados nas tabelas X75\_DCTF e X751\_DCTF\_COMPL mudarão o campo STATUS de “G” para “A”\.

OS3267\-A

OS3753\-A

# RN06

__\[ALTERADA – OS3913\] __Após a geração da prévia dos DARF’s será disponibilizado a aba “Compensações de Crédito/Geração dos DARF’s”\. Essa aba irá disponibilizar os créditos dos DARF’s gerados na tabela X75\_DCTF com campo STATUS = “G” e os créditos dos DARF’s gerados na tabela X751\_DCTF\_COMPL com campo STATUS = “G” e com o campo IND\_DEB\_CRED = ‘C’\. Essa tela irá gerar também os créditos provenientes do Saldo Credor\.

Caso exista alguma retenção sem o campo “Data Vencimento” preenchida, deverá ser exibida mensagem de aviso com o número do log de processo na tela e não deverá impedir a geração do DARF\. Nessa tela serão disponibilizados os seguintes filtros:

- __Empresa:__ deverá ser informada a Empresa para filtro\.
- __Estabelecimento:__ deverá ser informado o Estabelecimento para filtro\.
- __Código DARF: __deverá ser informado o Código DARF de 4 dígitos para pesquisa\. Campo numérico de 4 posições\. Filtro não obrigatório de preenchimento\. Uma vez informado esse campo irá recuperar os Créditos da tabela X751\_DCTF\_COMPL através do campo “Código DARF”, porém filtrando os mesmos quando o campo IND\_DEB\_CRED = ‘C’\.

Uma vez informados os filtros serão exibidas as informações da seguinte origem:

- Créditos da tabela X751\_DCTF\_COMPL com campo IND\_DEB\_CRED = ‘C’ \(a ser desenvolvido nas OS’s 3267\-A1 e 3267\-B\)\.
- Créditos da tela de Saldo Credor cujo Saldo seja > 0\.

Serão exibidos os seguintes campos:

- __Código Empresa:__ deverá ser exibido o Código da Empresa referente ao crédito proveniente de DARF da tabela X751\_DCTF\_COMPL ou Saldo Credor\.
- __Código Estabelecimento:__ deverá ser exibido o Código do Estabelecimento referente ao crédito proveniente de DARF da tabela X751\_DCTF\_COMPL ou Saldo Credor\.
- __Código DARF:__ deverá ser exibido o Código DARF referente ao crédito proveniente de DARF da tabela X751\_DCTF\_COMPL\.
- __Número Documento Pagamento:__ deverá ser exibido o Número Documento Pagamento referente ao crédito proveniente de DARF da tabela X751\_DCTF\_COMPL ou Saldo Credor\.
- __Código Operação:__ deverá ser exibido o Código Operação referente ao crédito proveniente de DARF da tabela X751\_DCTF\_COMPL ou Saldo Credor\.
- __Valor a Compensar:__ deverá ser exibido o Valor a Compensar referente ao crédito proveniente de DARF da tabela X751\_DCTF\_COMPL ou Saldo Credor\.
- __Valor Compensado:__ deverá ser exibido o Valor já Compensado referente ao crédito proveniente de DARF da tabela X751\_DCTF\_COMPL ou Saldo Credor\.
- __Saldo:__ deverá ser exibido o Saldo referente ao crédito proveniente de DARF da tabela X751\_DCTF\_COMPL ou Saldo Credor\.
- __Origem Crédito:__ deverá ser exibida a origem do Crédito\.
	- Caso o crédito seja da X751\_DCTF\_COMPL cujo campo IND\_DEB\_CRED = ‘C’, será exibida a informação “Pagamento Indevido ou a Maior” 
	- Caso o crédito seja referente à um Saldo Credor, será exibida a opção de acordo com o informado no registro da tela de Saldo Credor:
		- Pagamento Indevido ou a Maior \(Origem Saldos\)
		- Ressarcimento de IPI
		- IRPJ Saldo Negativo Per\. Anteriores \- Próprio
		- IRPJ Saldo Negativo Per\. Anteriores \- Sucedida
		- CSLL Saldo Negativo Per\. Anteriores \- Próprio
		- CSLL Saldo Negativo Per\. Anteriores \- Sucedida
		- IRRF Cooperativas de Trabalho
		- IRRF Juros sobre o Capital Próprio
		- Outros
		- PIS/PASEP Não\-Cumulativo \- Exportação
		- Cofins Não\-Cumulativa \- Exportação
		- PIS/PASEP Não\-Cumulativo \- Mercado Interno
		- Cofins Não\-Cumulativa \- Mercado Interno
		- PIS/PASEP Embalagens \(§4º do art\. 51 da Lei nº 10\.833/03\)
		- Cofins Embalagens \(§4º do art\. 51 da Lei nº 10\.833/03\)
		- Reintegra

OS3267\-A

OS3267\-B2

OS3699

OS3913

# RN07

Na parte de baixo da tela serão exibidos os débitos, ou seja, os DARF’s gerados nas tabelas X75\_DCTF cujo campo STATUS = ‘G’ e tabela X751\_DCTF\_COMPL cujo campo STATUS = ‘G’ e campo IND\_DEB\_CRED = ‘D’

Nessa tela serão disponibilizados os seguintes filtros:

- __Código DARF: __deverá ser informado o Código DARF de 4 dígitos para pesquisa\. Campo numérico de 4 posições\. Filtro não obrigatório de preenchimento\. Uma vez informado esse campo irá recuperar os DARF’s das tabelas X75\_DCTF e X751\_DCTF\_COMPL\.
- __Código Receita:__ deverá ser informado o Código Receita de 6 dígitos para pesquisa\. Campo numérico de 4 posições\. Filtro não obrigatório de preenchimento\. Uma vez informado esse campo irá recuperar os DARF’s das tabelas X75\_DCTF e X751\_DCTF\_COMPL\.
- __Código Operação:__ deverá ser informado o Código Operação de 6 dígitos para pesquisa\. Campo alfanumérico de 6 posições\. Filtro não obrigatório de preenchimento\. Uma vez informado esse campo irá recuperar os DARF’s das tabelas X75\_DCTF e X751\_DCTF\_COMPL\.

Uma vez informados os filtros, serão exibidos os seguintes campos:

- __Código Empresa:__ deverá ser exibido o Código da Empresa referente ao débito da X75\_DCTF ou X751\_DCTF\_COMPL\.
- __Código Estabelecimento:__ deverá ser exibido o Código do Estabelecimento referente ao débito da X75\_DCTF ou X751\_DCTF\_COMPL\.
- __Código DARF:__ deverá ser exibido o Código DARF referente ao débito da X75\_DCTF ou X751\_DCTF\_COMPL\.
- __Código Operação:__ deverá ser exibido o Código Operação referente ao débito da X75\_DCTF ou X751\_DCTF\_COMPL\.
- __Código Receita:__ deverá ser exibido o Código Receita referente ao débito da X75\_DCTF ou X751\_DCTF\_COMPL\.
- __Data de Vencimento:__ deverá ser exibido a Data de Vencimento referente débito da X75\_DCTF ou X751\_DCTF\_COMPL\.
- __Valor do Crédito:__ deverá ser exibido o Valor do Crédito referente ao débito da X75\_DCTF ou X751\_DCTF\_COMPL\.
- __Origem Crédito:__ deverá ser exibida a origem do Débito\. Nesse caso por se tratar de um débito deverá ser exibido “DARF”\.

OS3267\-A

# RN08

Deverá existir um botão chamado “Confirmar/Gerar DARF’s”\. Ao clicar nesse botão, o DARF será gerado para compensação bancária\. Nesse caso a regra para que isso aconteça é a seguinte:

- DARF’s existentes na tabela X75\_DCTF com campo STATUS = “G” passam para campo STATUS = “A”
- DARF’s existentes na tabela X751\_DCTF\_COMPL com campo STATUS = “G” e campo IND\_DEB\_CRED = “D” passam para campo STATUS = “A”\.

O valor dos DARF’s gerado nos campos “Valor Principal” das tabelas X75\_DCTF e X751\_DCTF\_COMPL deverão ser acrescidos de Juros e Multa nesse momento\. Com essa regra os DARF’s já podem ser pagos no sistema bancário\.

OS3267\-A

# RN09

Caso o usuário tente realizar uma outra geração de DARF’s ou tente sair da tela durante o processo, ou seja, antes de confirmar as operações, deverá ser exibida a seguinte mensagem de erro na tela:

*“Atenção, o processo de geração dos DARF´s ainda não foi concluído\. A saída da Tela ou uma nova Geração neste estado acarretará na desconsideração das compensações realizadas e da prévia dos DARF´s, confirma?”*

Serão exibidos os botões “Sim” e “Não”\. Caso o usuário selecione o botão “Sim”, a rotina de DARF será reiniciada, ou seja, nenhuma ação realizada pelo usuário será salva\. Caso o usuário selecione o botão “Não”, o usuário irá retornar para a tela sem nenhuma ação e/ou alteração por parte do sistema\.

# RN10

Incluir nos parâmetros para pesquisa de registros já cadastrados, os campos “Data de Cancelamento”, “Cancelado” e “Número do Voucher”\. Esses campos foram criados na OS3267\.

Esses campos para pesquisa deverão ser incluídos após o campo “Mês Competência”\.

OS3267\-A

# RN11

No relatório de conferência da tela de Controle de Tributos, os campos “Data de Cancelamento”, “Cancelado” e “Número do Voucher” deverão ser disponibilizados após o campo “Dt\. Fim Competência”\.

OS3267\-A

# RN12

Na rotina de Importação Online caso o usuário tente importar uma retificação na tabela X530\_RETIFICACAO\_IRRF e já exista outra retificação anterior \(aquela com Data de Retificação anterior mais próxima em relação à Data de Retificação da Retificação que está sendo importada\) e essa retificação anterior possua no campo “Situação DARF Complementar/Compensação Crédito” = Não Gerado ou Gerado/Não Pago ou Não Gerado,  o sistema deverá impedir a importação desse registro mais atual e deverá ser exibida a seguinte mensagem no log:

*“Existe retificação anterior com SITUACAO = N ou G\. Para a importação com sucesso, exclua Retif\. com SITUACAO = N ou exclua o DARF Compl\. e/ou Crédito associados a Retif\. que esteja com a SITUACAO = G”*

Após exibir a mensagem, deverá ser exibida a chave do documento fiscal da tabela X530\_RETIFICACAO\_IRRF que já consta na base de dados\.

Essa regra só irá funcionar caso o parâmetro “Importar Retificações de Retenções” da tela de Programação de Jobs de Importação do menu Importação >> Programação do módulo Job Servidor esteja selecionado\. Caso o mesmo não esteja selecionado essa regra não será aplicada, visto que nesse caso as retificações nunca são importadas\.

OS3267\-A

# RN13

Na rotina de Importação Batch caso o usuário tente importar uma retificação na tabela X530\_RETIFICACAO\_IRRF e já exista outra retificação anterior \(aquela com Data de Retificação anterior mais próxima em relação à Data de Retificação da Retificação que está sendo importada\) e essa retificação anterior possua no campo “Situação DARF Complementar/Compensação Crédito” = Não Gerado ou Gerado/Não Pago ou Não Gerado,  o sistema deverá impedir a importação desse registro mais atual e deverá ser exibida a seguinte mensagem no log:

*“Existe retificação anterior com SITUACAO = N ou G\. Para a importação com sucesso, exclua Retif\. com SITUACAO = N ou exclua o DARF Compl\. e/ou Crédito associados a Retif\. que esteja com a SITUACAO = G”*

Após exibir a mensagem, deverá ser exibida a chave do documento fiscal da tabela X530\_RETIFICACAO\_IRRF que já consta na base de dados\.

Essa regra só irá funcionar caso o parâmetro “Importar Retificações de Retenções” da tela de Programação de Jobs de Importação do menu Importação >> Programação do módulo Job Servidor esteja selecionado\. Caso o mesmo não esteja selecionado essa regra não será aplicada, visto que nesse caso as retificações nunca são importadas\.

OS3267\-A

# RN14

Na tela de Controle de Tributos, o sistema não deverá permitir que o usuário inclua manualmente uma nova retificação na aba “Retificações”, caso a Retificação mais atual – aquela com Data de Retificação mais recente – esteja com o campo “Situação DARF Complementar/Compensação Crédito” = Não Gerado ou Gerado/Não Pago\.

OS3267\-A

# RN15

Na tela de geração do DARF \(menu: Outras Obrigações >> DARF’s >> Geração\) do módulo Obrigações de Tributos Federais, na aba “Compensações de Crédito/Geração dos DARF’s”, deverá ser criado uma barra de rolagem vertical que permita que todos os componentes da tela possam ser visualizados\.

CH122003

# RN16

Deverá ser criado um novo parâmetro na tela de Geração do DARF a partir das Retenções\. O nome do novo parâmetro será “Somente Empresa Atual” e o mesmo deverá ficar disponível abaixo do parâmetro “Parametrizar Exceções”\. Por default esse parâmetro deverá ser exibido desmarcado\.

OS3857

# RN17

Caso o cliente não selecione o parâmetro “Somente Empresa Atual” o sistema irá exibir todas as Empresas e Estabelecimentos do sistema conforme regra atual\.

Vale salientar que a Empresa e o Estabelecimento que estiverem selecionados no Manager estarão por default selecionados\.

Caso o cliente não selecione nenhum Estabelecimento no Manager e não selecione o parâmetro “Somente Empresa Atual”, o sistema irá deixar selecionado somente a Empresa pertencente ao Estabelecimento\. Nesse caso, nenhum estabelecimento estará previamente selecionado\.

OS3857

# RN18

Caso o cliente selecione o parâmetro “Somente Empresa Atual” o sistema irá exibir somente a Empresa informada no Manager e seus respectivos Estabelecimentos\. As outras Empresas e Estabelecimentos não serão exibidas\.

Vale salientar que a Empresa e o Estabelecimento que estiverem selecionados no Manager estarão por default selecionados\.

Caso o cliente não selecione nenhum Estabelecimento no Manager e selecione o parâmetro “Somente Empresa Atual”, o sistema irá deixar selecionado somente a Empresa pertencente ao\(s\) Estabelecimento\(s\)\. Nesse caso, nenhum estabelecimento estará previamente selecionado\.

OS3857

# RN19

Caso o usuário ao tentar excluir o DARF no momento da geração – desmarcando o parâmetro “Não Excluir DARF’s” – da tela de Geração de DARF’s a partir das Retenções, e o DARF que está sendo excluído possua créditos vinculados ao mesmo \(ver campo NRO\_REFERENCIA\_DEB da tabela CTRL\_COMPENSACAO\_CRED\), o sistema deverá liberar os créditos tanto da tela de Saldo Credor \(campos: Valor a Compensar e Saldo da tabela SLD\_COMPENSACAO\_CRED\), quando os créditos oriundos de DARF \(campo: Valor Utilizado da aba: Compensações da tela de Manutenção do DARF\.

OS3917

# RN20

Quando o campo “Tipo de Crédito” estiver com a opção “Pagamento Indevido ou a Maior” selecionada, o campo “Formalização Pedido” deverá exibir as seguintes opções:

- Processo Administrativo
- Dcomp 
- Dcomp com Direito Creditório Reconhecido em Processo

Quando o campo “Tipo de Crédito” estiver com a opção diferente de “Pagamento Indevido ou a Maior” – ou seja, o campo em branco ou selecionado com uma opção diferente – o campo “Formalização Pedido” deverá exibir as seguintes opções:

- Processo Administrativo
- Dcomp

OS3913

# RN21

Ao gerar os DARF’s através do menu: Outras Obrigações >> DARF’s >> Geração a partir das Retenções no módulo Obrigações de Tributos Federais, o sistema deverá calcular os juros de mora – ou juros – quando aplicável\. Vale salientar que o valor de juros será gravado no campo “Valor Juros” da tela de Manutenção de DARF’s na aba “DARF Original” ou “DARF Complementar” \(tabelas X75\_DCTF ou X751\_DCTF\_COMPL\)\.

As regras para a aplicação de juros são as seguintes:

- A regra vale para qualquer DARF independente do Código DARF gerado;
- Caso o Controle de Tributos que seja referente ao DARF gerado possua uma Data de Vencimento preenchida em um determinado mês e a Data de Pagamento do DARF \(campo: Data Prevista de Pagamento\) seja no mínimo um dia após esse vencimento mas dentro do mesmo mês, não será cobrado juros\.
- Caso o Controle de Tributos que seja referente ao DARF gerado possua uma Data de Vencimento preenchida em um determinado mês e a Data de Pagamento do DARF \(campo: Data Prevista de Pagamento\) seja no mês seguinte, será cobrado apenas 1% de juros do valor do DARF\.
- Caso o Controle de Tributos que seja referente ao DARF gerado possua uma Data de Vencimento preenchida em um determinado mês \(exemplo: 10/2013\) e a Data de Pagamento do DARF \(campo: Data Prevista de Pagamento\) seja por exemplo em 12/2013, será cobrado apenas 1% de juros do valor do DARF\.
- Caso o Controle de Tributos que seja referente ao DARF gerado possua uma Data de Vencimento preenchida em um determinado mês \(exemplo: 10/2013\) e a Data de Pagamento do DARF \(campo: Data Prevista de Pagamento\) seja por exemplo em 01/2014, será somado toda a taxa SELIC do período \(campo: “Valor” da tela de Índice de Conversão do DW – menu: Manutenção >> Cadastros >> Índices de Conversão – acrescida de 1% Essa somatória será aplicada ao valor do DARF\.

O Valor do Juros será gravado no campo “Valor Juros” da tela de Manutenção de DARF’s aba “DARF Original” ou “DARF Complementar” \(tabelas X75\_DCTF ou X751\_DCTF\_COMPL\)\.

Essas regras foram baseadas nas consultas ao Setor de Informações\.

CH29336\_2013

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

