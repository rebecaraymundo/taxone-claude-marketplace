# MTZ-OS3171-A1-OTF-Gerar_Registros_CJAA-CJAC-ESDJ-RPDE-BRPDE-VRPDE_da_DIRF_2011

- **Fonte:** MTZ-OS3171-A1-OTF-Gerar_Registros_CJAA-CJAC-ESDJ-RPDE-BRPDE-VRPDE_da_DIRF_2011.docx
- **Modificado:** 2020-08-29
- **Tamanho:** 53 KB

---

# OTF \- Gerar Registros CJAA\-CJAC\-ESDJ\-RPDE\-BRPDE\-VRPDE da DIRF 2011

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3171\-A1

OTF \- Gerar Registros CJAA\-CJAC\-ESDJ\-RPDE\-BRPDE\-VRPDE da DIRF 2011\.doc

## <a id="_Toc282084627"></a>Módulo: Obrigações de Tributos Federais

- Geração dos registros CJAA, CJAC, ESDJ, RPDE, BRPDE e VRPDE da DIRF 2011\.

#### Cód\.

### Descrição

### DR

# RN01

Gravar no campo 1 – Identificador do Registro o valor fixo “CJAC”\.

O registro CJAC corresponde a um registro BPFDEC e/ou BPJDEC correspondente, logo deverão ser recuperadas as Fichas Financeiras \(SAFX21\) e as Retenções do período \(SAFX53\) dos Beneficiários – pessoas físicas – cujo campo Tipo Lançamento = Beneficiários com valores de imposto compensados em virtude de decisão judicial – ano calendário\. Nos casos em que a informação for oriunda da SAFX21, verificar o código da verba \(campo 07\) e verificar se na Parametrização por Verba \(menu: Parâmetros >> Parâmetros p/ Verba \(Folha de Pagamento\) o campo “Classe DIRF” = “Imposto de Renda Retido”\.

O valor compensado em virtude da decisão judicial já vai ser informado nesse registro além do campo respectivo ao mesmo Beneficiário no registro RTIRF também já vir com a informação correta\.

*Exemplo*: caso se tenha um valor a ser compensado de R$ 1\.000,00 e o valor retido no mês foi de R$ 1\.000,00, o registro RTIRF será informado com o valor R$ 0,00 e o registro CJAC com valor R$ 1\.000,00\. Caso o valor da compensação seja maior, o valor do imposto retido RTIRF será zerado e a sobra do crédito \(a ser utilizado no CJAC\) deverá ser utilizada em outro mês\. Caso o valor da compensação seja menor, o valor do RTIRF será diminuído até o valor máximo da compensação, e o CJAC será informado com o valor creditado\.

OBS: vale salientar que as verbas informadas no campo 07 da SAFX21 deverão seguir a regra previamente existente de que as verbas classificadas como “Desconto” deverão ser subtraídas, enquanto que as verbas classificadas como “Proventos” deverão ser somadas\.

OS3171\-A1

# RN02

Gravar no campo 2 – Janeiro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Janeiro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Janeiro \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN03

Gravar no campo 3 – Fevereiro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Fevereiro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Fevereiro \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN04

Gravar no campo 4 – Março:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Março \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Março \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN05

Gravar no campo 5 – Abril:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Abril \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Abril \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN06

Gravar no campo 6 – Maio:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Maio \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Maio \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN07

Gravar no campo 7 – Junho:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Junho \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Junho \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN08

Gravar no campo 8 – Julho:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Julho \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Julho \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN09

Gravar no campo 9 – Agosto:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Agosto \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Agosto \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN10

Gravar no campo 10 – Setembro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Setembro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Setembro \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN11

Gravar no campo 11 – Outubro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Outubro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Outubro \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN12

Gravar no campo 12 – Novembro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Novembro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Novembro \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN13

Gravar no campo 13 – Dezembro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Dezembro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Dezembro \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN14

Gravar no campo 14 – Décimo Terceiro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 desde que o campo “Indicador da Folha” \(campo 06 da SAFX21\) seja “Pagamento de 13º\. Salário”\. 
- SAFX53
	- O valor contido no campo “Valor Tributo 13º\. Salário” da SAFX53\.

OS3171\-A1

# RN15

Gravar no campo 1 – Identificador do Registro o valor fixo “CJAA”\.

O registro CJAA corresponde a um registro BPFDEC e/ou BPJDEC correspondente, logo deverão ser recuperadas as Fichas Financeiras \(SAFX21\) e as Retenções do período \(SAFX53\) dos Beneficiários – pessoas físicas – cujo campo Tipo Lançamento = Beneficiários com valores de imposto compensados em virtude de decisão judicial – anos anteriores\. Nos casos em que a informação for oriunda da SAFX21, verificar o código da verba \(campo 07\) e verificar se na Parametrização por Verba \(menu: Parâmetros >> Parâmetros p/ Verba \(Folha de Pagamento\) o campo “Classe DIRF” = “Imposto de Renda Retido”\.

O valor compensado em virtude da decisão judicial já vai ser informado nesse registro além do campo respectivo ao mesmo Beneficiário no registro RTIRF também já vir com a informação correta\.

*Exemplo*: caso se tenha um valor a ser compensado de R$ 1\.000,00 e o valor retido no mês foi de R$ 1\.000,00, o registro RTIRF será informado com o valor R$ 0,00 e o registro CJAC com valor R$ 1\.000,00\. Caso o valor da compensação seja maior, o valor do imposto retido RTIRF será zerado e a sobra do crédito \(a ser utilizado no CJAC\) deverá ser utilizada em outro mês\. Caso o valor da compensação seja menor, o valor do RTIRF será diminuído até o valor máximo da compensação, e o CJAC será informado com o valor creditado\.

OBS: vale salientar que as verbas informadas no campo 07 da SAFX21 deverão seguir a regra previamente existente de que as verbas classificadas como “Desconto” deverão ser subtraídas, enquanto que as verbas classificadas como “Proventos” deverão ser somadas\.

OS3171\-A1

# RN16

Gravar no campo 2 – Janeiro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Janeiro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Janeiro \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN17

Gravar no campo 3 – Fevereiro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Fevereiro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Fevereiro \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN18

Gravar no campo 4 – Março:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Março \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Março \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN19

Gravar no campo 5 – Abril:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Abril \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Abril \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN20

Gravar no campo 6 – Maio:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Maio \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Maio \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN21

Gravar no campo 7 – Junho:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Junho \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Junho \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN22

Gravar no campo 8 – Julho:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Julho \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Julho \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN23

Gravar no campo 9 – Agosto:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Agosto \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Agosto \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN24

Gravar no campo 10 – Setembro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Setembro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Setembro \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN25

Gravar no campo 11 – Outubro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Outubro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Outubro \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN26

Gravar no campo 12 – Novembro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Novembro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Novembro \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN27

Gravar no campo 13 – Dezembro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Dezembro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo 15 da SAFX53 para a competência de Dezembro \(ver campos 12 e 13 da SAFX53\)\.

OS3171\-A1

# RN28

Gravar no campo 14 – Décimo Terceiro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 desde que o campo “Indicador da Folha” \(campo 06 da SAFX21\) seja “Pagamento de 13º\. Salário”\. 
- SAFX53
	- O valor contido no campo “Valor Tributo 13º\. Salário” da SAFX53\.

OS3171\-A1

# RN29

Gravar no campo 1 – Identificador do Registro o texto fixo “RPDE”\.

As informações a serem gravadas serão recuperadas das tabelas SAFX21 e SAFX53\. Caso não existam registros nessas tabelas, os registros RPDE, BRPDE e VRPDE não deverão ser gerados\. O critério para recuperar as informações dos beneficiários domiciliados no exterior é o seguinte:

- SAFX21
	- Campo “Declarante de rendimentos pagos a residentes ou domiciliados no exterior” = Sim no menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais;
	- Total de Rendimentos anuais igual ou superior a 1x o valor informado no campo “Valor Anual Mínimo de Rendimentos” do menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\. Deverão ser considerados como Total de Rendimentos anuais os valores do período informado nos campos “Mês/Ano da Saída do País” e “Mês/Ano do Retorno ao País” \(campos 68 e 69 da SAFX21\) __OU__ com valores de IR retido na fonte – ver campo 07 da SAFX21 cuja campo “Classe DIRF” = Imposto de Renda Retido na tela de Parâmetros por Verba \(módulo: Obrigações de Tributos Federais, menu: Parâmetros >> Parâmetros por Verba \(Folha de Pagamento\)\) – e com o campo 09 da SAFX21 preenchido para o período\. 
- SAFX53
	- Campo “Declarante de rendimentos pagos a residentes ou domiciliados no exterior” = Sim no menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais;
	- Total de Rendimentos anuais igual ou superior a 1x o valor informado no campo “Valor Anual Mínimo de Rendimentos” do menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\. Deverão ser considerados como Total de Rendimentos anuais os valores durante o período quando a Pessoa Física/Jurídica possuir a UF = EX __OU__ com valores de IR retido na fonte – ver campo 15 da SAFX53 para o período informado\.

O total de rendimentos do ano calendário que estiverem fora do período informado nos campos 68 e 69 da SAFX21 serão considerados nos registros\-filhos da família BPFDEC \(porque os mesmos serão pagos para o funcionário residente no Brasil\)\. Só serão considerados nos registros\-filhos da família RPDE os que estiverem dentro do período informado nos campos 68 e 69 da SAFX21\.

Nos casos em que o prestador de serviço \(pessoa física ou jurídica\) estiver parte do ano prestando serviço no Brasil e na outra parte do ano fora do país, o cliente deverá criar dois cadastros desse prestador \(SAFX04\) com data de validade distinta\. Só será considerada nos registros da família RPDE os que estiverem com UF = EX\. O cadastro do prestador que estiver no Brasil \(UF <> EX\) será considerado nos registros da família BPJDEC\.

Caso um mesmo funcionário \(SAFX21\) ou prestador \(SAFX53\) possuam informações para os respectivos registros dentro do país \(BPFDEC ou BPJDEC e filhos\) ou fora do país \(RPDE, BRPDE e VRPDE\) o sistema não deverá considerar o somatório de dentro e fora do país para definir se o funcionário ou prestador é elegível para ser considerado na DIRF\. As informações devem ser consideradas de forma separada\. Caso em ambas as situações os valores não sejam iguais ou superiores a 1x o valor informado no campo “Valor Anual Mínimo de Rendimentos” da tela de Geração da DIRF, o funcionário ou prestador __NÃO SERÁ INFORMADO__ no meio magnético\. Porém se em um dos casos o mesmo for elegível, __TODAS__ as informações pertinentes ao funcionário ou prestador serão geradas no arquivo\.

OS3171\-A1

# RN30

Gravar no campo 1 – Identificador de Registro o valor fixo “BRPDE”\.

OS3171\-A1

# RN31

Gravar no campo 2 – Beneficiário a informação de acordo com as regras abaixo:

- SAFX21
	- Gravar o valor “1”
- SAFX53
	- Caso o Beneficiário seja uma Pessoa Física \(campo 04 da SAFX53\), gravar “1”\.
	- Caso o Beneficiário seja uma Pessoa Jurídica \(campo 04 da SAFX53\), gravar “2”\.

No caso da SAFX53, para identificar uma Pessoa Física de uma Jurídica, verificar o identificador do campo 04 da SAFX53 e procurar o campo 06 da SAFX04\. Caso o campo 06 da SAFX04 possua 11 posições é uma Pessoa Física\. Caso possua 14 posições é uma Pessoa Jurídica\.

Caso o campo 06 da SAFX04 não esteja preenchido – o que caracteriza que o beneficiário não possui CPF ou CNPJ – verificar o campo 26 da SAFX04\. Caso o mesmo esteja preenchido com “1”, gravar “1”\. Caso esteja preenchido com qualquer outra informação, gravar “2”\.

OS3171\-A1

# RN32

Gravar no campo 3 – Código do País a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor de acordo com o campo “País”\.
- SAFX53
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo 21 da SAFX04\.

No caso em que o Código do País não for preenchido na SAFX21, deverá ser exibida a seguinte mensagem no log de geração da DIRF: “__*Retenção de Funcionário residente no exterior sem preenchimento do campo Código do País\. Por gentileza, verificar o cadastro do Funcionário\.*__”\.

No caso em que o Código do País não for preenchido na SAFX53, deverá ser exibida a seguinte mensagem no log de geração da DIRF: “__*Retenção de Terceiro residente no exterior sem preenchimento do campo Código do País\. Por gentileza, verificar o cadastro da Pessoa Física/Jurídica*__”\.

OS3171\-A1

# RN33

Gravar no campo 4 \- Número de identificação fiscal – NIF a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor contido no campo “Número de Identificação Fiscal” da SAFX15\.
- SAFX53
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo “Número de Identificação Fiscal” da SAFX04\.

OS3171\-A1

# RN34

Gravar no campo 5 – CPF/CNPJ a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor contido no campo 12 da SAFX15\.
- SAFX53
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo 06 da SAFX04\.

OS3171\-A1

# RN35

Gravar no campo 6 – Nome/Nome Empresarial a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor contido no campo 05 da SAFX15\.
- SAFX53
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo 05 da SAFX04\.

OS3171\-A1

# RN36

Gravar no campo 7 – Relação fonte pagadora pessoa jurídica e beneficiário pessoa jurídica a informação de acordo com as regras abaixo:

- SAFX21
	- Não será gravada nessa situação, visto que essa informação é pertinente somente para Pessoas Jurídicas\.
- SAFX53
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo “Relação Fonte Pagadora/Beneficiário” da SAFX04\. Essa informação só será gravada caso a Pessoa Física/Jurídica da SAFX04 seja uma __Pessoa Jurídica__\.

OS3171\-A1

# RN37

Gravar no campo 8 – Logradouro a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor contido no campo 35 da SAFX15\.
- SAFX53
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo 12 da SAFX04\.

OS3171\-A1

# RN38

Gravar no campo 9 – Número a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor contido no campo 36 da SAFX15\.
- SAFX53
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo 13 da SAFX04\.

OS3171\-A1

# RN39

Gravar no campo 10 – Complemento a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor contido no campo 37 da SAFX15\.
- SAFX53
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo 14 da SAFX04\.

OS3171\-A1

# RN40

Gravar no campo 11 – Bairro/Distrito a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor contido no campo 38 da SAFX15\.
- SAFX53
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo 15 da SAFX04\.

OS3171\-A1

# RN41

Gravar no campo 12 – Código Postal a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor contido no campo 40 da SAFX15\.
- SAFX53
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo 20 da SAFX04\.

OS3171\-A1

# RN42

Gravar no campo 13 – Cidade a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor contido no campo 39 da SAFX15\.
- SAFX53
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo 16 da SAFX04\.

OS3171\-A1

# RN43

Gravar no campo 14 – Estado/Província a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor contido no campo 76 da SAFX15\.
- SAFX53
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo 55 da SAFX04\.

OS3171\-A1

# RN44

Gravar no campo 15 – Telefone a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor contido nos campos “DDD” e “Telefone” da SAFX15\.
- SAFX53
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido nos campos 22 e 23 da SAFX04\.

OS3171\-A1

# RN45

Gravar no campo 1 – Identificador do Registro o valor fixo “VRPDE”\.

OS3171\-A1

# RN46

Gravar no campo 2 – Data do Pagamento a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação do campo 08 da SAFX21\.
- SAFX53
	- Recuperar a informação do campo “Data Pagamento” da SAFX53\. Caso o campo “Data Pagamento” não esteja preenchido, gravar a informação contida no campo 03 \(DATA\_MOVTO\) da SAFX53\.

Nesse caso em que a Data do Pagamento não esteja preenchida para a SAFX53 e seja gerada no arquivo a Data do Movimento deverá ser exibido no log de geração da DIRF a seguinte mensagem: __*“Retenção de Terceiro residente no exterior sem preenchimento de algum dos campos: Data Pagamento, Tipo Rendimento e/ou Forma Tributação\. Por gentileza, verificar a manutenção do Controle de Tributos”*__

OS3171\-A1

# RN47

Gravar no campo 3 – Código de Receita a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação a partir do campo “Residente no Exterior” da tela de geração da DIRF – módulo: Obrigações de Tributos Federais, menu: DIRF >> Geração DIRF\.
- SAFX53
	- Recuperar a informação do campo 11 da SAFX53\.

OS3171\-A1

# RN48

Gravar no campo 4 – Tipo de Rendimento a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação do campo “Tipo Rendimento” 
- SAFX53
	- Recuperar a informação do campo “Tipo Rendimento”\.

No caso em que o Tipo Rendimento não esteja preenchido na SAFX21, deverá ser exibido no log de geração da DIRF a seguinte mensagem: “__*Retenção de Funcionário residente no exterior sem preenchimento de algum dos campos: Tipo Rendimento e/ou Forma Tributação\. Por gentileza, verificar a manutenção da Ficha Financeira\.*__”

No caso em que o Tipo Rendimento não esteja preenchido na SAFX53, deverá ser exibido no log de geração da DIRF a seguinte mensagem: “__*Retenção de Terceiro residente no exterior sem preenchimento de algum dos campos: Data Pagamento, Tipo Rendimento e/ou Forma Tributação\. Por gentileza, verificar a manutenção do Controle de Tributos\.*__”

OS3171\-A1

# RN49

Gravar no campo 5 – Rendimento Pago a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação a partir do campo 09 da SAFX21, desde que a verba informada \(campo 07 da SAFX21\) esteja parametrizada no menu Parâmetros >> Parâmetros p/ Verba do módulo Obrigações de Tributos Federais com a opção “Rendimentos Tributáveis”\.
- SAFX53
	- Recuperar a informação a partir do campo 14 da SAFX53

OBS: as verbas oriundas da tabela SAFX21 que estiverem classificadas como “Proventos” devem ser somadas, enquanto que as verbas classificadas como “Descontos” devem ser subtraídas\.

OS3171\-A1

# RN50

Gravar no campo 6 – Imposto Retido a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação a partir do campo 09 da SAFX21, desde que a verba informada \(campo 07 da SAFX21\) esteja parametrizada no menu Parâmetros >> Parâmetros p/ Verba do módulo Obrigações de Tributos Federais com a opção “Imposto de Renda Retido”\.
- SAFX53
	- Recuperar a informação a partir do campo 15 da SAFX53

OBS: as verbas oriundas da tabela SAFX21 que estiverem classificadas como “Proventos” devem ser subtraídas, enquanto que as verbas classificadas como “Descontos” devem ser somadas\.

OS3171\-A1

# RN51

Gravar no campo 7 – Forma de Tributação a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação do campo “Forma Tributação” 
- SAFX53
	- Recuperar a informação do campo “Forma Tributação” 

No caso em que a Forma de Tributação não esteja preenchido na SAFX21, deverá ser exibido no log de geração da DIRF a seguinte mensagem: “__*Retenção de Funcionário residente no exterior sem preenchimento de algum dos campos: Tipo Rendimento e/ou Forma Tributação\. Por gentileza, verificar a manutenção da Ficha Financeira\.*__”

No caso em que a Forma de Tributação não esteja preenchido na SAFX53, deverá ser exibido no log de geração da DIRF a seguinte mensagem: “__*Retenção de Terceiro residente no exterior sem preenchimento de algum dos campos: Data Pagamento, Tipo Rendimento e/ou Forma Tributação\. Por gentileza, verificar a manutenção do Controle de Tributos\.*__”

OS3171\-A1

# RN52

Gravar no campo 1 – Identificador do Registro o valor fixo “ESDJ”\.

- Deverão ser recuperadas as Fichas Financeiras \(SAFX21\) e as Retenções do período \(SAFX53\) – somente para pessoas físicas – cujo campo Tipo Lançamento = Beneficiários do Imposto de Renda retido na fonte com depósito judicial\.
- Quando as informações forem recuperadas das Fichas Financeiras \(SAFX21\), o código da verba \(campo 07 da SAFX21\) deverá estar parametrizado no módulo Obrigações de Tributos Federais \(menu: Parâmetros >> Parâmetros p/ Verba\) com o campo “Classe DIRF” = “Imposto de Renda Retido”\.

OBS: as verbas oriundas da tabela SAFX21 que estiverem classificadas como “Proventos” devem ser subtraídas, enquanto que as verbas classificadas como “Descontos” devem ser somadas\.

OS3171\-A1

# RN53

Gravar no campo 2 – Janeiro de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Janeiro \(ver campos 04 e 05 da SAFX21\)
- SAFX53
	- Gravar o campo 15 da SAFX53 para a competência de Janeiro \(ver campos 04 e 05 da SAFX21\)

OS3171\-A1

# RN54

Gravar no campo 3 – Fevereiro de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Fevereiro \(ver campos 04 e 05 da SAFX21\)
- SAFX53
	- Gravar o campo 15 da SAFX53 para a competência de Fevereiro \(ver campos 04 e 05 da SAFX21\)

OS3171\-A1

# RN55

Gravar no campo 4 – Março de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Março \(ver campos 04 e 05 da SAFX21\)
- SAFX53
	- Gravar o campo 15 da SAFX53 para a competência de Março \(ver campos 04 e 05 da SAFX21\)

OS3171\-A1

# RN56

Gravar no campo 5 – Abril de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Abril \(ver campos 04 e 05 da SAFX21\)
- SAFX53
	- Gravar o campo 15 da SAFX53 para a competência de Abril \(ver campos 04 e 05 da SAFX21\)

OS3171\-A1

# RN57

Gravar no campo 6 – Maio de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Maio \(ver campos 04 e 05 da SAFX21\)
- SAFX53
	- Gravar o campo 15 da SAFX53 para a competência de Maio \(ver campos 04 e 05 da SAFX21\)

OS3171\-A1

# RN58

Gravar no campo 7 – Junho de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Junho \(ver campos 04 e 05 da SAFX21\)
- SAFX53
	- Gravar o campo 15 da SAFX53 para a competência de Junho \(ver campos 04 e 05 da SAFX21\)

OS3171\-A1

# RN59

Gravar no campo 8 – Julho de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Julho \(ver campos 04 e 05 da SAFX21\)
- SAFX53
	- Gravar o campo 15 da SAFX53 para a competência de Julho \(ver campos 04 e 05 da SAFX21\)

OS3171\-A1

# RN60

Gravar no campo 9 – Agosto de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Agosto \(ver campos 04 e 05 da SAFX21\)
- SAFX53
	- Gravar o campo 15 da SAFX53 para a competência de Agosto \(ver campos 04 e 05 da SAFX21\)

OS3171\-A1

# RN61

Gravar no campo 10 – Setembro de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Setembro \(ver campos 04 e 05 da SAFX21\)
- SAFX53
	- Gravar o campo 15 da SAFX53 para a competência de Setembro \(ver campos 04 e 05 da SAFX21\)

OS3171\-A1

# RN62

Gravar no campo 11 – Outubro de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Outubro \(ver campos 04 e 05 da SAFX21\)
- SAFX53
	- Gravar o campo 15 da SAFX53 para a competência de Outubro \(ver campos 04 e 05 da SAFX21\)

OS3171\-A1

# RN63

Gravar no campo 12 – Novembro de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Novembro \(ver campos 04 e 05 da SAFX21\)
- SAFX53
	- Gravar o campo 15 da SAFX53 para a competência de Novembro \(ver campos 04 e 05 da SAFX21\)

OS3171\-A1

# RN64

Gravar no campo 13 – Dezembro de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Dezembro \(ver campos 04 e 05 da SAFX21\)
- SAFX53
	- Gravar o campo 15 da SAFX53 para a competência de Dezembro \(ver campos 04 e 05 da SAFX21\)

OS3171\-A1

# RN65

Gravar no campo 14 – Décimo Terceiro de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21, desde que o campo 06 \(IND\_FOLHA\) da SAFX21 esteja com a opção “Pagamento de 13º\. Salário”\.
- SAFX53
	- Gravar o campo “Valor Tributo 13º\. Salário” da SAFX53

OS3171\-A1

# RN66

Caso durante a geração do arquivo o campo “Relação Fonte Pagadora/Beneficiário” do registro BRPDE seja informado para uma Pessoa Física, deve ser exibida a seguinte mensagem de erro no log de geração\.

“Não pode ser informado para uma Pessoa Física a Relação de Fonte Pagadora com o Beneficiário, pois a mesma é pertinente apenas para Pessoa Jurídica”\.

Embora seja exibida a mensagem de erro, a geração do arquivo não será impedida\.

OS3171\-A1

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

