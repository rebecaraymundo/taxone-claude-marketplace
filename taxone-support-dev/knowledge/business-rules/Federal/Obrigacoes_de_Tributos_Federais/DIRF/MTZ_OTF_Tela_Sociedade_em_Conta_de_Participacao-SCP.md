# MTZ_OTF_Tela_Sociedade_em_Conta_de_Participacao-SCP

- **Fonte:** MTZ_OTF_Tela_Sociedade_em_Conta_de_Participacao-SCP.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 71 KB

---

THOMSON REUTERS

Sociedade em Conta de Participação \(SCP\)

DIRF \- 2017

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-8291

Tela Sociedade em Conta de Participação \(SCP\)

Criação da Tela “Sociedade em Conta de Participação \(SCP\)”

Sumário

[1\.	Regras dos Campos	2](#_Toc471741294)

# <a id="_Toc350763252"></a><a id="_Toc471741294"></a>Regras dos Campos 

__Localização da tela:__ Módulo: Federal >> Obrigações de Tributos Federais

__                                   __Menu: DIRF >> Sociedade em Conta de Participação \(SCP\)

__Título da tela: __Sociedade em Conta de Participação \(SCP\)

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Estabelecimento

Text Box

S

S

Default: Habilitado

Ao Acessar a tela, este campo será preenchido com o estabelecimento que fora logado no sistema, caso contrário o usuário deverá selecionar o estabelecimento desejado\.

Obs: deverá ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS8291

Ano Calendário

Text Box

S

S

Default: Habilitado

Valor default = 2016

Esse campo poderá ser alterado\.

Caso não preenchido exibir a seguinte mensagem: “Ano calendário não preenchido”\. 

MFS8291

Ano Referência – DIRF

Text Box

S

S

Default: Habilitado

Valor default = 2017

Esse campo poderá ser alterado\.

Caso não preenchido exibir a seguinte mensagem: “Ano Referência \- DIRF não preenchido”\. 

MFS8291

CNPJ da SCP

Pasta

S

S

Default: Habilitado

Ao selecionar a pasta deverão ser listados os SCP´s cadastrados \(SAFX2057\) em que o campo Incide DIRF esteja preenchido com ‘S’ e que estejam dentro do período de validade d acordo com o campo Ano Calendário\.

Caso não preenchido exibir a seguinte mensagem: “CNPJ da SCP não preenchido”

MFS8291

Nome Empresarial da SCP

Text Box

S

N

Default: Desabilitado

Selecionar o conteúdo do campo Descrição da SCP \(SAFX2057\) correspondente ao SCP recuperado no campo acima CNPJ da SPC\.

MFS8291

Tipo de beneficiário 

S

S

Default: Habilitado

Identifica o tipo de beneficiário\.

Tipos: 

1 \- Pessoa Física; 

2 \- Pessoa Jurídica; 

Demostrar apenas as descrições\.

MFS8291

CPF / CNPJ do beneficiário da SCP

Text Box

S

S

Default: Habilitado

CPF/CNPJ do beneficiário\. Deverá validar se o CPF/CNPJ é válido, de acordo com o campo Tipo de beneficiário\. 

Caso não preenchido exibir a seguinte mensagem:

“CPF/CNPJ do beneficiário não preenchido”\.

Será validado também no caso do tipo de beneficiário = ‘2 – Pessoa Física’ se o CNPJ informado é o mesmo que o CNPJ informado no campo CNPJ da SCP, caso positivo exibir a seguinte mensagem:

“CNPJ do beneficiário não pode ser igual ao CNPJ da SCP”\.

MFS8291

Nome do beneficiário da SCP

Text Box

S

S

Default: Habilitado

Caso não preenchido exibir a seguinte mensagem: “Nome do Prestador de Serviço não preenchido”\.

MFS8291

Percentual de participação na SCP

Text Box

N

S

Default: Habilitado

Campo não obrigatório

MFS8291

Lucros e dividendos pagos ao sócio da SCP \(Janeiro – 13°\)

Text Box

N

S

Default: Habilitado

Campo não obrigatório

MFS8291

Totais

Text Box

N

S

Default: Habilitado

Somatório de todos os meses do quadro Lucros e dividendos pagos ao sócio da SCP

MFS8291

Sugestão de Tela

