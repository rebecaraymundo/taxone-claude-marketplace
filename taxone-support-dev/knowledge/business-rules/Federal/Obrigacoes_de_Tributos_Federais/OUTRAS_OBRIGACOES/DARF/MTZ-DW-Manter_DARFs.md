# MTZ-DW-Manter_DARFs

- **Fonte:** MTZ-DW-Manter_DARFs.docx
- **Modificado:** 2023-03-13
- **Tamanho:** 49 KB

---

# Obrigações de Tributos Federais \- Manter DARF's

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3267\-A1

Obrigações de Tributos Federais \- Manter DARF's

Será desenvolvida nessa OS uma rotina que permita que após os DARF’s com status “Em Aberto” e “Pago” visualizados através de telas de manutenção do DARF Original e Complementar\. Os valores dos créditos gerados por esses DARF’s, além das compensações que esses DARF’s por ventura tenham utilizado também serão objeto dessa OS\. 

Além disso, essa OS irá tratar o pagamento dos DARF’s Originais e Complementares através da alteração da rotina de Importação Online e Importação Batch para as tabelas X75\_DCTF e X751\_DCTF\_COMPL\.

#### Cód\.

### Descrição

### DR

# RN00

Os campos de identificação do DARF deverão ser englobados na aba “DARF Original”\. Nessa aba deverão constar os DARF’s Originais que constam na tabela X75\_DCTF\. Só deverão constar nessa aba os DARF’s originais que estejam com o campo STATUS = “A” \(Em aberto\) e “P” \(Pago\)\.

Os Pré\-DARF’s \(cujo campo STATUS = “G”\) não deverão constar nessa tela\. Isso se deve ao fato de que os Pré\-DARF’s deverão ser visualizados antes da rotina de Compensação dos Créditos, para que após a devida compensação os DARF’s sejam gerados com o valor definitivo \(STATUS = “A”\)\.

OS3267\-A1

# RN01

O campo “Valor Total” \(campo 12 da SAFX75\) deverá exibir o valor original do DARF que foi gerado e posteriormente pago, independente se o mesmo sofreu retificações \(X530\) e/ou cancelamentos \(X53\)\.

OS3267\-A1

# RN02

Na parte inferior da tela de manutenção, serão exibidas as retenções e devidas retificações que foram geradas a partir daquele DARF\. As informações e as regras são divididas da seguinte forma:

- __Tributos Efetivos no DARF:__ serão exibidas as retenções/retificações que fazem parte efetivamente desse DARF\.
	- Caso o DARF Original não possua retificações na X530 e/ou cancelamento na X53\_RETENCAO\_IRRF, deverão ser exibidas todas as retenções da X53\_RETENCAO\_IRRF que compuseram aquele DARF\. As informações exibidas nos campos “Fato Gerador”, “Favorecido”, “Nome”, “No\. Doc”, “Valor Tributável” e “Valor Tributo” permanecem sendo recuperadas conforme regra atual\.
	- Caso o DARF Original possua uma retenção cancelada na X53\_RETENCAO\_IRRF \(campo 52 preenchido e campo 53 = “S”\) essa retenção cancelada __NÃO IRÁ FAZER FAZER PARTE__ das retenções que compuseram o DARF\.
	- Caso o DARF Original possua uma ou mais retificações na X530\_RETIFICACAO\_IRRF essa retenção retificada __NÃO IRÁ FAZER FAZER PARTE__ das retenções que compuseram o DARF\.
- __Tributos Originais/Cancelados no DARF:__ serão exibidas as retenções originais que fizeram parte originalmente desse DARF\. Esse conjunto de informações deverá ser inibido caso o DARF não possua retificações \(isso se deve ao fato de que essas informações irão constar na parte de Tributos Efetivos no DARF\)\. Serão exibidos todas as retenções que fizeram parte desse DARF\. As informações devem ser recuperadas da tabela X53\_RETENCAO\_IRRF\. As informações exibidas nos campos “Fato Gerador”, “Favorecido”, “Nome”, “No\. Doc”, “Valor Tributável” e “Valor Tributo” permanecem sendo recuperadas conforme regra atual\. Caso no DARF original existiu uma ou mais retenções que foram canceladas \(campo 52 preenchido e campo 53 = “S”\), essas retenções deverão ser exibidas nessa parte e com o campo “Data Cancelamento” preenchido \(campo 52 da SAFX53\)\. As retenções que não estão canceladas \(campo 52 não preenchido e campo 53 = “N”\), não precisam informar esse campo\.
- __Tributos Retificados no DARF: __ serão exibidas as retenções retificadas no DARF, ou seja, caso o DARF Original possua retenções \(X53\_RETENCAO\_IRRF\) que por sua vez possuam retificações \(X530\_RETIFICACAO\_IRRF\)\. Esse conjunto de informações deverá ser inibido caso o DARF não possua retenções com retificações \(isso se deve ao fato de que essas informações irão constar na parte de Tributos Efetivos no DARF\)\. Serão exibidas somente as retificações mais recentes, ou seja, as retificações cujo campo “Data Retificação” seja o mais atual\. As informações devem ser recuperadas da tabela X530\_RETIFICACAO\_IRRF\. 

OS3267\-A1

# RN03

Deverá ser criada uma nova aba chamada “DARF Complementar”\. Nessa aba irão constar os DARF’s Complementares que constam na tabela X751\_DCTF\_COMPL\. Só deverão constar nessa aba os DARF’s Complementares que estejam com o campo STATUS = “A” \(Em aberto\) e “P” \(Pago\) e com o campo IND\_DEB\_CRED = “D” na tabela X751\_DCTF\_COMPL\.

Os Pré\-DARF’s \(cujo campo STATUS = “G”\) da tabela X751\_DCTF\_COMPL não deverão constar nessa tela\. Isso se deve ao fato de que os Pré\-DARF’s deverão ser visualizados antes da rotina de Compensação dos Créditos, para que após a devida compensação os DARF’s sejam gerados com o valor definitivo \(STATUS = “A”\)\.

OS3267\-A1

# RN04

Nas abas “DARF Original”, “DARF Complementar”, “Crédito” e “Compensação”, será possível visualizar os Tributos Efetivos, Tributos Originais e Tributos Retificados\. 

Caso um DARF não possua retificações ou cancelamentos, será disponibilizado somente os Tributos Efetivos, não sendo possível visualizar as informações nos Tributos Originais e Tributos Retificados\.

OS3267\-A1

# RN05

Deverá ser criada uma nova aba chamada “Crédito”\. Nessa aba irão constar os créditos gerados através dos DARF’s que foram pagos a maior \(X53\_RETENCAO\_IRRF\) em relação às retificações \(X530\_RETIFICACAO\_IRRF\)\. Só deverão constar nessa aba os Créditos que estejam com o campo STATUS = “A” \(Em aberto\) e “P” \(Pago\) e com o campo IND\_DEB\_CRED = “C” na tabela X751\_DCTF\_COMPL\.

Os Pré\-DARF’s \(cujo campo STATUS = “G”\) da tabela X751\_DCTF\_COMPL não deverão constar nessa tela\. Isso se deve ao fato de que os Pré\-DARF’s deverão ser visualizados antes da rotina de Compensação dos Créditos, para que após a devida compensação os DARF’s sejam gerados com o valor definitivo \(STATUS = “A”\)\.

OS3267\-A1

# RN06

Será disponibilizado na aba “Crédito” os seguintes campos:

- __Data Apuração:__ essa informação deve ser recuperada do campo 03 \(DATA\_APURACAO\) da tabela SAFX75\. Não poderá ser editável\.
- __Valor do Crédito:__ deve ser recuperado o Valor do Crédito gerado pelo DARF\. O crédito pode ser gerado das seguintes formas:
	- Caso a retenção tenha sido cancelada, o Valor da Retenção será considerado nesse campo\.
	- Caso a retenção tenha sido retificada a menor, a diferença entre o “Valor da Retenção” da X53\_RETENCAO\_IRRF e do “Valor da Retenção” da X530\_RETENCAO\_IRRF será informado nesse campo\. Caso a retenção possua mais de uma retificação, a comparação será entre as duas retificações através do mesmo campo “Valor da Retenção”\.

Os créditos dos Saldos Credores para Compensação dos Tributos Federais, não serão considerados nessa tela\.

Cada crédito gerado por um DARF será gerado em uma linha diferente\.

OS3267\-A1

# RN07

Deverá ser criada uma nova aba chamada “Compensação”\. Nessa aba irão constar as compensações que foram utilizadas no DARF gerado\.

Os Pré\-DARF’s \(cujo campo STATUS = “G”\) da tabela X751\_DCTF\_COMPL não deverão constar nessa tela\. Isso se deve ao fato de que os Pré\-DARF’s deverão ser visualizados antes da rotina de Compensação dos Créditos, para que após a devida compensação os DARF’s sejam gerados com o valor definitivo \(STATUS = “A”\)\.

OS3267\-A1

# RN08

Será disponibilizada na aba “Compensação” os seguintes campos:

- __Data Pagamento:__ deverá ser informado a Data de Pagamento que consta no campo de mesmo nome do DARF Original \(X75\_DCTF\) ou DARF Complementar \(X751\_DCTF\_COMPL\)\.
- __Código DARF do Crédito:__ deverá ser informado o Código DARF que deu origem ao Crédito\. Essa informação deve ser recuperada do campo COD\_DARF da X75\_DCTF ou do Código DARF da tabela X751\_DCTF\_COMPL de Crédito ou de Saldo Credor\.
- __Valor DARF do Crédito:__ deverá ser informado o Valor do DARF que deu origem ao Crédito\. Essa informação deve ser recuperada do campo de Valor Principal da X75\_DCTF ou da X751\_DCTF\_COMPL\.
- __Valor Crédito:__ deverá ser informado o Valor Principal da X751\_DCTF\_COMPL ou o Valor a Compensar da tela de manutenção do Saldo Credor\.
- __Valor Utilizado:__ deverá ser informado o Valor da Compensação que consta no campo 02 da tela de Compensação\.

Cada compensação associada para o DARF será gerado em uma linha diferente\.

OS3267\-A1

# RN09

Caso o parâmetro “Permitir Compensações e DARF’s Complementares” da tela de Parâmetros por DARF/GPS do módulo Obrigações de Tributos Federais \(menu: Parâmetros >> Parâmetros DARF/GPS\) esteja desmarcado, o cliente terá acesso à tela antiga de Manutenção de DARF’s, porém somente com a aba DARF Original\. 

Nesse caso as retenções que compõem o DARF serão exibidas na parte “Tributos Efetivos”\. As partes “Tributos Originais” e “Tributos Retificados” não serão exibidas para o usuário\.

OS3267\-A1

# RN10

As seguintes críticas deverão ser realizadas na tela de manutenção dos DARF’s ao tentar excluir o mesmo:

- __DARF Original__
	- Não possui o campo DATA\_APURACAO\_COMPL preenchido ou possui outras quotas pagas \(mesmo NRO\_REFERENCIA pode ter n quotas na X75\)
		- DARF com Status = Pago, ou parte da divisão em quotas dos Tributos consta como paga, e, portanto não pode ser excluído\.
	- Não possui o campo DATA\_APURACAO\_COMPL preenchido e o campo NRO\_REFERENCIA\_COMPL preenchido além de possuir registro na X751\_DCTF\_COMPL para aquele NRO\_REFERENCIA ou possui retenção na X53\_RETENCAO\_IRRF cancelada\.
		- Este DARF possui retenção\(oes\) canceladas, não é possível excluir este DARF
	- Não possui o campo DATA\_APURACAO\_COMPL preenchido assim como o campo NRO\_REFERENCIA\_COMPL, não possui registro para a tabela X751\_DCTF\_COMPL com aquele NRO\_REFERENCIA, não possui retenção na X53\_RETENCAO\_IRRF como cancelada e possui alguma retificação de alguma retenção participante do DARF\.
		- Este DARF possui retificação\(oes\) de retenção, não é possível excluir este DARF
	- Não possui o campo DATA\_APURACAO\_COMPL preenchido assim como o campo NRO\_REFERENCIA\_COMPL, não possui registro na tabela X751\_DCTF\_COMPL para aquele NRO\_REFERENCIA e o registro não foi pago e não possui quotas com STATUS = Pago\.
		- Apaga todas as referencias na X750\_REDARF \(através do campo NRO\_REFERENCIA\) 
		- Atualiza o campo SITUACAO = ‘N’, IND\_PROC\_DARF = ‘N’ e NRO\_REFERENCIA\_DARF = nulo na X53 para todas as retenções participantes no DARF excluido\. 
		- Apaga o registro e as possíveis quotas existentes para o registro da X75
	- Não possui o campo DATA\_APURACAO\_COMPL preenchido assim como o campo NRO\_REFERENCIA\_COMPL, não possui registro na X751\_DCTF\_COMPL para aquele NRO\_REFERENCIA, os campos de Data Pagamento e Autenticação Bancária estão preenchidos \(STATUS = P’\) e nos parâmetros passados os mesmos estão diferentes, além de possuir retenção na X53\_RETENCAO\_IRRF cancelada\.
		- Este DARF possui retenção\(oes\) canceladas, não e possível reabrir este DARF\.
	- Não possui o campo DATA\_APURACAO\_COMPL preenchido assim como o campo NRO\_REFERENCIA\_COMPL, não possui o registro na tabela X751\_DCTF\_COMPL para aquele NRO\_REFERENCIA, não possui retenção na X53\_RETENCAO\_IRRF cancelada e possui retificação de alguma retenção participante do DARF\. 
		- Este DARF possui retificação\(oes\) de retencao, não e possível reabrir este DARF\.
	- Não possui o campo DATA\_APURACAO\_COMPL preenchido assim como o campo NRO\_REFERENCIA\_COMPL, não possui registro na X751\_DCTF\_COMPL para aquele NRO\_REFERENCIA\_DARF, os campos de Data de Pagamento e Autenticação Bancária estão informados \(STATUS = P\), não possui retenção na X53 cancelada e não possui retificacação de alguma retenção participante do DARF\.
		- Atualiza o registro da X75 para o STATUS = ‘A’
		- Apaga todas as referencias na X750\_REDARF \(através do campo NRO\_REFERENCIA\) 
		- Atualiza o campo situacao = ‘G’ na X53 para todas as retenções participantes no DARF\.

OS3267\-A1

# RN11

\(CONTINUA\)

As seguintes críticas deverão ser realizadas na tela de manutenção dos DARF’s ao tentar excluir o mesmo:

- __DARF Complementar__
	- Possui os campos DATA\_APURACAO\_COMPL e NRO\_REFERENCIA\_COMPL preenchidos e possui outras retificações na X530\_RETIFICACAO\_IRRF posteriores às pertencentes no DARF Complementar ou Crédito
		- Este DARF Complementar ou Credito possui retificacoes mais recentes\. Nao e possivel excluir o registro
	- Possui os campos DATA\_APURACAO\_COMPL e NRO\_REFERENCIA\_COMPL preenchidos, não foi pago para o caso de DARF Complementar \(STATUS = P\) ou compensou algum DARF \(STATUS = C\) e não possui outras retificações posteriores às pertencentes no DARF Complementar ou Crédito
		- Atualiza o campo SITUACAO\_X751 = ‘N’, IND\_PROC\_X751 = ‘N’ e NRO\_REFERENCIA\_X751 = nulo na X53 para todas as retenções ou na X530 para todas as retificações participantes no registro excluido\. 
		- Apaga o registro da X751
	- Possui os campos DATA\_APURACAO\_COMPL e NRO\_REFERENCIA\_COMPL preenchidos e possui outras retificações posteriores pertencentes ao DARF Complementar\.
		- Este DARF Complementar possui retificacoes mais recentes\. Nao e possivel reabrir o registro
	- Possui os campos DATA\_APURACAO\_COMPL e NRO\_REFERENCIA\_COMPL preenchidos e não possui outras retificações posteriores pertencentes ao DARF Complementar\.
		- Atualiza o registro da X751 para o STATUS = ‘A’

OS3267\-A1

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

