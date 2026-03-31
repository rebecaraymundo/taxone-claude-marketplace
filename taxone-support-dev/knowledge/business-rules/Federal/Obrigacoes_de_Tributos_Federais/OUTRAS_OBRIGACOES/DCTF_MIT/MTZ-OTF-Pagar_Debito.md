# MTZ-OTF-Pagar_Debito

- **Fonte:** MTZ-OTF-Pagar_Debito.docx
- **Modificado:** 2026-03-04
- **Tamanho:** 49 KB

---

# Obrigações de Tributos Federais \- Pagar Débito

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3267\-B1

Obrigações de Tributos Federais \- Gerar DCTF

Será desenvolvida uma rotina para que a Sul América informe automaticamente na DCTF o respectivo valor dos créditos que estão sendo compensados na obrigação acessória\.

OS3267\-B2

Obrigações de Tributos Federais \- Geração da DCTF a partir das Retenções e Retificações das Retenções – Registros de Compensação R12 e R13

Será desenvolvida uma rotina para que a Sul América informe automaticamente na DCTF o respectivo valor dos créditos que estão sendo compensados na obrigação acessória\.

OS3699

Obrigações de Tributos Federais \- Atualização Legal da DCTF para a versão 2\.4

Trata\-se da atualização legal da DCTF para a versão 2\.4\.

CH8853\_2013

Obrigações de Tributos Federais

Alteração da tela ‘‘Pagamento de Débitos’

OS4620

Obrigações de Tributos Federais \- Atualização Legal da DCTF para a versão 3\.1

Trata\-se da atualização legal da DCTF para a versão 3\.1\.

#### Cód\.

### Descrição

### DR

# RN01

Após a DCTF ser gerada, o Pagamento de Débitos deverá ser preenchido automaticamente através do menu Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Pagamento de Débitos ou Outras Obrigações >> DCTF >> DCTF Mensal \(a partir de 01/01/2006\) >> Pagamento de Débitos\. As informações que poderão ser alteradas serão descritas nas regras a seguir\.

OS3267\-B1

# RN02

Serão disponibilizados os seguintes campos:

- __Empresa:__ será disponibilizada nesse campo a Empresa em que foram gerados os Pagamentos do Débito\. O usuário poderá selecionar outras Empresas – caso as mesmas já tenham sido geradas anteriormente\.
- __Declaração:__ nessa parte serão informados os detalhes da geração da DCTF em relação aos Dados Iniciais da Empresa ou Estabelecimento\.
	- __Ano: __será informado o Ano da Declaração\. Essa informação deve ser recuperada do campo “Ano” da parametrização de Dados Iniciais \(ver menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Estabelecimento\.
	- __Periodicidade:__ será informada a Periodicidade da Declaração\. Essa informação deve ser recuperada do campo “Periodicidade” da parametrização de Dados Iniciais \(ver menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Estabelecimento\.
	- __Mês:__ será informado o Mês da Declaração\. Essa informação deve ser recuperada do campo “Mês” da parametrização de Dados Iniciais \(ver menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Estabelecimento\.
	- __Tipo Declaração:__ será informado o Tipo Declaração da Declaração\. Essa informação deve ser recuperada do campo “Tipo Declaração” da parametrização de Dados Iniciais \(ver menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Estabelecimento\.
	- __Retificadora:__ será informado se a Declaração é Retificadora ou não\. Essa informação deve ser recuperada do campo “Retificadora” da parametrização de Dados Iniciais \(ver menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Estabelecimento\.
	- __Estabelecimento:__ será informado o Estabelecimento da Declaração\. Essa informação deve ser recuperada do campo “Estabelecimento” da parametrização de Dados Iniciais \(ver menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Estabelecimento\. Sempre será recuperado o Estabelecimento parametrizado como Matriz\.
	- __Dia:__ será informado o Dia do Débito\. O usuário não poderá editar essa informação\.
	- __Mês: __será informado o Mês do Débito\. Essa informação será recuperada de acordo com o Mês dos Débitos que compõem a Ficha de Débito\. O usuário não poderá editar essa informação\.
	- __Ano: __será informado o Ano do Débito\. Essa informação será recuperada de acordo com o Ano dos Débitos que compõem a Ficha de Débito\. O usuário não poderá editar essa informação\.
	- __Status Operação: __será informado o Status da Operação da Ficha de Débito\. Essa informação será recuperada da Digitação da Ficha de Débito localizada no menu Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Pagamento de Débitos\. Poderão ser exibidos 3 \(três\) status diferentes:
		- 1 – Pendente
		- 2 – Em andamento
		- 3 – Liquidado
	- __Saldo Dividido:__ será informado se o Saldo do Débito foi dividido ou não\. Essa informação deve ser recuperada do campo “Saldo Dividido” da rotina de Geração da DCTF \(menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Geração DCTF >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Geração DCTF >> Por Estabelecimento\. O usuário não poderá editar essa informação\.
- __Saldo Dividido: __será informado se o Saldo do Débito foi dividido ou não\. Essa informação deve ser recuperada do campo “Saldo Dividido” da rotina de Geração da DCTF \(menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Geração DCTF >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Geração DCTF >> Por Estabelecimento\. O usuário não poderá editar essa informação\.
- __Grupo Tributo:__ será informado o Grupo do Tributo de acordo com o critério de consolidação para a DCTF\. Essa informação será recuperada do campo COD\_TRIBUTO da tabela X53\_RETENCAO\_IRRF quando as retenções não possuírem retificações ou do campo COD\_TRIBUTO da tabela X530\_RETIFICACAO\_IRRF mais atual quando a retenção possuir uma ou mais retificações\. O usuário não poderá editar essa informação\.
- __Código Receita:__ será informado o Código de Receita de acordo com o critério de consolidação para a DCTF\. Essa informação será recuperada do campo COD\_RECEITA da tabela X53\_RETENCAO\_IRRF quando as retenções não possuírem retificações ou do campo COD\_RECEITA da tabela X530\_RETIFICACAO\_IRRF mais atual quando a retenção possuir uma ou mais retificações\. O usuário não poderá editar essa informação\.
- __Estabelecimento do Débito:__ será informado o Estabelecimento do Débito\. Essa informação deve ser recuperada do campo “Estabelecimento do débito da Digitação da Ficha de Débito \(ver menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Digitação da Ficha de Débito\)\.

OS3267\-B1

# RN03

As fichas “Pagamento do Débito Parcial”, “Parcelamento do Débito” e “Suspensão do Débito” não serão alteradas\.

OS3267\-B1

# RN04

A forma como são gravadas as informações nas tabelas que são referentes ao Pagamento de Débitos, estão descritas no documento de Matriz da Geração da DCTF a partir das Retificações\. 

OS3267\-B1

# RN05

Caso o cliente tenha um Débito que tenha tido um DARF compensado totalmente, ou seja, o valor total do DARF para pagamento tenha sido compensado em sua totalidade por um Crédito – Crédito da X751\_DCTF\_COMPL ou Crédito de Saldo Credor – o usuário ao abrir a tela de Pagamento de Débitos, verá o valor da Compensação nos seguintes campos:

- Compensação via Crédito de DARF – Compensação de Pagamento Indevido ou a Maior
	- Compensação Darf
	- Principal Darf
	- Total Pago
	- Valor Débito
- Compensação via Saldo Credor – Outras Compensações
	- Compensação
	- Total Pago
	- Valor Débito

Nesse caso, não será exibida mensagem de erro informando que o Valor Total Pago do Débito é Maior do que o próprio Débito\.

OBS: além disso, a DCTF será gerada com o registro do Débito \(R10\) e o registro da compensação \(R12 e/ou R13\)\.

OS3267\-B2

# RN06

Caso o cliente selecione um Débito na tela de Pagamento de Débitos e no campo “Selecionar Pagamento” seja selecionada a opção “Outras Compensações”, deverá ser criado uma nova opção chamada “Reintegra” no campo “Tipo de Crédito”\.

Essa opção deverá ser disponibilizada como última opção do campo\.

OS3699

# RN07

Quando o tipo do pagamento for ‘Suspensão do Débito’, o campo ‘Cód\. Processo’ da tela ‘Pagamento de Débitos’ deve aceitar 24 posições \(esta alteração será necessária apenas na tela, pois na tabela ‘dct\_susp\_deb’ este campo já aceita 24 posições\)\.

CH8853\_2013

# RN08

Quando o Mês e Ano da Declaração for maior ou igual a Agosto de 2014 e for selecionado o tipo do pagamento “Suspensão do Débito”, deverá ser atualizado o conteúdo do campo “Motivo Suspensão”, exibindo as seguintes opções:

“01” – Liminar em Mandado de Segurança 

“02” – Depósito Judicial do Montante Integral 

“03” – Antecipação de Tutela 

“04” – Liminar em Medida Cautelar 

“07” – Medida Judicial em que o declarante não é o autor 

“08” – Sentença em Mandado de Segurança favorável ao contribuinte 

“09” – Sentença em Ação Ordinária favorável ao contribuinte e confirmada pelo TRF 

“10” – Acórdão do TRF favorável ao contribuinte 

“11” – Acórdão do STJ em Recurso Especial favorável ao contribuinte 

“12” – Acórdão do STF em Recurso Extraordinário favorável ao contribuinte

Para versões anteriores à 3\.1 da DCTF este campo tinha apenas uma posição\. A partir da versão 3\.1 passa a ter duas posições\.

As opções “5” – Depósito Administrativo do Montante Integral e “6” – Outros foram removidas a partir da versão 3\.1 e não devem ser demonstradas quando o Mês e Ano da Declaração for maior ou igual a Agosto de 2014\.

Por default, quando selecionado o tipo de pagamento "Suspensão de Débito" todos os campos estão habilitados em tela e devem ser aplicados os seguintes tratamentos:

Se for selecionado como "Motivo da Suspensão" as opções: “01” – Liminar em Mandado de Segurança __ou__ “02” – Depósito Judicial do Montante Integral __ou__ “03” – Antecipação de Tutela __ou__ “04” – Liminar em Medida Cautelar __ou__ “08” – Sentença em Mandado de Segurança favorável ao contribuinte __ou__ “09” – Sentença em Ação Ordinária favorável ao contribuinte e confirmada pelo TRF __ou__ “10” – Acórdão do TRF favorável ao contribuinte __ou__ “11” – Acórdão do STJ em Recurso Especial favorável ao contribuinte __ou__ “12” – Acórdão do STF em Recurso Extraordinário favorável ao contribuinte, devem ser habilitados para digitação os campos:

- Número do Processo
- Vlr Suspensão
- Cód\. Vara
- Estado
- Município

O dropdown "Depósito" deve estar preenchido por default com a opção "Com Depósito", exibindo os campos:

- Identificação do Depósito
- Período de Apuração
- CPF/CNPJ
- Código da Receita
- Data de Vencimento
- Valor do Principal
- Valor da Multa
- Valor dos Juros

Se o status do dropdown "Depósito" for alterado para "Sem Depósito", os campos relacionados ao depósito serão inibidos\.

Para o Motivo “02” – Depósito Judicial do Montante Integral a opção de Depósito será sempre "Com Depósito", não permitindo alteração\.

Se for selecionado como "Motivo da Suspensão" a opção: “07” – Medida Judicial em que o declarante não é o autor, deve ser habilitado para digitação o campo: Vlr Suspensão\. Neste caso, o dropdown "Depósito" deve estar preenchido por default com a opção "Sem Depósito" e os campos relacionados ao depósito serão inibidos\.

Para o dropdown "Depósito", geraremos no arquivo o código “0” quando for selecionada a opção “Sem Depósito e “1” quando for selecionada a opção “Com Depósito”\. Esta alteração também é valida para período maior ou igual a agosto de 2014\.

OS4620

# RN09

Quando o Mês e Ano da Declaração for maior ou igual a Agosto de 2014, o tipo de pagamento “Outras Compensações” não deve ser mais exibido\.

OS4620

# RN10

Quando o Mês e Ano da Declaração for maior ou igual a Agosto de 2014, o tipo de pagamento “Compensação de Pagamento Indevido ou a Maior” deve ser exibido com o nome “Compensações”

OS4620

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

