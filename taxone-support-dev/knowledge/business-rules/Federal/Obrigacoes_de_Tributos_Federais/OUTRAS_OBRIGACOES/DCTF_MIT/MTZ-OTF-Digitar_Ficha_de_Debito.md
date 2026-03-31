# MTZ-OTF-Digitar_Ficha_de_Debito

- **Fonte:** MTZ-OTF-Digitar_Ficha_de_Debito.docx
- **Modificado:** 2026-02-25
- **Tamanho:** 49 KB

---

# Obrigações de Tributos Federais \- Digitar Ficha de Débito

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3267\-B1

Obrigações de Tributos Federais \- Gerar DCTF

Será desenvolvida uma rotina para que a Sul América informe automaticamente na DCTF o respectivo valor dos créditos que estão sendo compensados na obrigação acessória\.

OS3124\-B

<a id="OLE_LINK3"></a><a id="OLE_LINK4"></a><a id="OLE_LINK1"></a><a id="OLE_LINK2"></a>Obrigações de Tributos Federais \- Ajuste do Grupo de Tributo da Digitação da Ficha de Débito da DCTF

Através do chamado interno 76654, foi solicitada a reavaliação da TACES15, pois os Códigos de Tributo dessa tabela não estão iguais com a forma que os Códigos de Tributo são gerados na DCTF\. Abaixo segue o exemplo:

De acordo com a análise desse chamado seria necessário uma alteração completa da TACES15 e de outras tabelas que leem essa informação\. Além disso, seria necessária a adequação de funcionalidades do sistema, tais como, DCTF, DIRF, Informes de Rendimento do PIS/COFINS/CSLL, Relatório de Tributos Federais, entre outros\.

Após uma nova análise por parte do Requisito, foram realizados diversos testes na DCTF, onde foi constatado que existe um DE\-PARA interno que converte os Tributos para os códigos corretos dentro da obrigação\. Além disso, os outros pontos de alteração informados na análise não se aplicam mais no cenário atual\. Além disso, é importante salientar que alteração em base histórica de clientes em produção é de grande complexidade\.

Em virtude desse cenário, foi optado por não alterar nenhuma tabela acessória e outras funcionalidades do produto\. Como nessa análise inicial feita em 2010, não foi provado nenhum problema no produto foi decidido que essa OS3124\-B será utilizada para que no campo “Grupo Tributo” da tela de Digitação da Ficha de Débito da DCTF tenha os códigos omitidos\. A funcionalidade permanecerá a mesma\.

MFS\-543009

Alessandra Cristina Navatta

Inclusão da regra do campo DAT\_PERIOD\_APUR\. Este campo não é exibido em tela e será gerado pelo sistema – RN04

#### Cód\.

### Descrição

### DR

# RN01

Após a DCTF ser gerada, a Ficha de Débito deverá ser preenchida automaticamente através do menu Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Digitação da Ficha de Débito\. As informações serão preenchidas pelo sistema e o usuário poderá ter acesso à alteração de algumas informações\.

OS3267\-B1

# RN02

Serão disponibilizados os seguintes campos:

- __Empresa:__ será disponibilizada nesse campo a Empresa em que foram geradas as Fichas de Débito\. O usuário poderá selecionar outras Empresas e o cadastro de Dados Iniciais da Empresa será alterado conforme a Empresa selecionada\.
- __Declaração:__ nessa parte serão informados os detalhes da geração da DCTF em relação aos Dados Iniciais da Empresa ou Estabelecimento\.
	- __Ano: __será informado o Ano da Declaração\. Essa informação deve ser recuperada do campo “Ano” da parametrização de Dados Iniciais \(ver menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Estabelecimento\.
	- __Periodicidade:__ será informada a Periodicidade da Declaração\. Essa informação deve ser recuperada do campo “Periodicidade” da parametrização de Dados Iniciais \(ver menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Estabelecimento\.
	- __Mês:__ será informado o Mês da Declaração\. Essa informação deve ser recuperada do campo “Mês” da parametrização de Dados Iniciais \(ver menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Estabelecimento\.
	- __Tipo Declaração:__ será informado o Tipo Declaração da Declaração\. Essa informação deve ser recuperada do campo “Tipo Declaração” da parametrização de Dados Iniciais \(ver menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Estabelecimento\.
	- __Estabelecimento:__ será informado o Estabelecimento da Declaração\. Essa informação deve ser recuperada do campo “Estabelecimento” da parametrização de Dados Iniciais \(ver menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Estabelecimento\. Sempre será recuperado o Estabelecimento parametrizado como Matriz\.
	- __Retificadora:__ será informado se a Declaração é Retificadora ou não\. Essa informação deve ser recuperada do campo “Retificadora” da parametrização de Dados Iniciais \(ver menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Estabelecimento\.
- __Grupo Tributo:__ será informado o Grupo do Tributo de acordo com o critério de consolidação para a DCTF\. Essa informação será recuperada do campo DSC\_ABREV da tabela DWT\_TRIBUTO de acordo com o campo COD\_TRIBUTO da tabela X53\_RETENCAO\_IRRF quando as retenções não possuírem retificações ou do campo COD\_TRIBUTO da tabela X530\_RETIFICACAO\_IRRF mais atual quando a retenção possuir uma ou mais retificações\. O usuário não poderá editar essa informação\. Caso a ficha de Débito esteja sendo consultada, será exibida no campo a descrição do Grupo Tributo – campo DSC\_ABREV\. O Código do Tributo – campo COD\_TRIBUTO da tabela DWT\_TRIBUTO – não será mais exibido\.
- __Estabelecimento Débito:__ será informado o Estabelecimento do Débito\.
- __Código Receita:__ será informado o Código de Receita de acordo com o critério de consolidação para a DCTF\. Essa informação será recuperada do campo COD\_RECEITA da tabela X53\_RETENCAO\_IRRF quando as retenções não possuírem retificações ou do campo COD\_RECEITA da tabela X530\_RETIFICACAO\_IRRF mais atual quando a retenção possuir uma ou mais retificações\. O usuário não poderá editar essa informação\.

*\(CONTINUA \.\.\.\)*

OS3267\-B1

OS3124\-B

# RN03

*\(\.\.\. CONTINUA\)*

- __Periodicidade Receita:__ será informado a Periodicidade da Receita\. Essa informação deve ser recuperada do campo “Periodicidade” da parametrização de Dados Iniciais \(ver menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Estabelecimento\. O usuário não poderá editar essa informação\.
- __Dia:__ será informado o Dia do Débito\. O usuário não poderá editar essa informação\.
- __Mês: __será informado o Mês do Débito\. Essa informação será recuperada de acordo com o Mês dos Débitos que compõem a Ficha de Débito\. O usuário não poderá editar essa informação\.
- __Ano: __será informado o Ano do Débito\. Essa informação será recuperada de acordo com o Ano dos Débitos que compõem a Ficha de Débito\. O usuário não poderá editar essa informação\.
- __Balanço Redução: __será informado o Balanço de Redução da Ficha de Débito\. Essa informação será recuperada de acordo com o campo “Balanço de Redução” da rotina de Geração da DCTF \(menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Geração DCTF >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Geração DCTF >> Por Estabelecimento\. O usuário não poderá editar essa informação\.
- __Valor Débito: __será informado o Valor do Débito\. Essa informação deve ser o somatório do campo VLR\_IR\_RETIDO da tabela X53\_RETENCAO\_IRRF para as retenções sem retificação ou do campo VLR\_IR\_RETIDO da tabela X530\_RETIFICACAO\_IRRF mais recente para as retenções que possuem uma retificação ou mais\. Esse valor poderá ser editado pelo usuário\. Vale salientar que o agrupamento das informações será pelo Código de Receita\.
- __Status Operação: __será informado o Status da Operação da Ficha de Débito\. Poderão ser exibidos 3 \(três\) status diferentes:
	- 1 – Pendente
	- 2 – Em andamento
	- 3 – Liquidado

O Status da Operação será informado de acordo com algumas comparações:	

- Caso o Valor do Pagamento do Débito for 0 \(zero\), é gerado o indicador 1 – Pendente\.
- Caso o Valor do Pagamento seja diferente do Valor do Débito, significa que deve ser gerado o indicador 2 – Em andamento\.
- Se o Valor do Pagamento for igual ao Valor do Débito, é gerado o indicador 3 \- Liquidado
- __Saldo Dividido: __será informado se o Saldo do Débito foi dividido ou não\. Essa informação deve ser recuperada do campo “Saldo Dividido” da rotina de Geração da DCTF \(menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Geração DCTF >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Geração DCTF >> Por Estabelecimento\. O usuário não poderá editar essa informação\.

OS3267\-B1

# RN04

__Campo DAT\_PERIOD\_APUR __

Este campo não será exibido em tela e será gerado pelo sistema, de acordo com as informações dos campos: Dia Período Apuração, Mês Período Apuração e Ano Período Apuração, seguindo as regras:

__Se os campos Dia Período Apuração, Mês Período Apuração estiverem preenchidos com valores diferentes de ‘00’, gravar o campo com as informações dos campos: __

‘Informação do Dia Período Apuração’‘Informação do Mês Período Apuração’‘Informação do Ano Período Apuração’

__Se o campo Dia Período Apuração estiver preenchido com ‘00’ e os campos Mês Período Apuração e Ano Período estiverem preenchidos com informação diferente de ‘00’ e ‘0000’, respectivamente, gravar o campo com:__

‘01’‘Informação do Mês Período Apuração’‘Informação do Ano Período Apuração’

__Se os campos Dia Período Apuração e Mês Período Apuração estiverem preenchidos com ‘00’, gravar o campo com:__

‘01‘01‘Informação do Ano Período Apuração’

MFS\-543009

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

