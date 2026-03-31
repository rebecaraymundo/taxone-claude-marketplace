# OTF-GPS_Matriz

- **Fonte:** OTF-GPS_Matriz.docx
- **Modificado:** 2020-08-29
- **Tamanho:** 35 KB

---

# Obrigações de Tributos Federais – GPS

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS2494

GPS – Cooperativa de Trabalho de Transporte \.

Durante a geração das retenções do INSS os dados deverão ser gravados considerando o campo 26 da SAFX04, onde o sistema deverá verificar se a informação é referente à Cooperativa de transporte, caso seja, a nota gerada referente a essa Pessoa Fis/Jur deve ser levada para a tela de manutenção com a data do fato gerador preenchida conforme a data fiscal\.

Durante a geração da Guia a data de competência apresentada na GPS deve ser a mesma da data fiscal\.

OS2613

GPS – Retenção 2º Base INSS

*Conforme especificado no documento de requisitos o sistema realmente não gera a informações completas para apuração da GPS, por isso o objetivo desse documento é de alterar a sistemática atual fazendo com que a guia dessas operações sejam gravadas considerando os valores informados nos campos referentes à 2ºBase de INSS\.*

CH50401

# Demonstrativo de INSS – OTF

Atualmente os demonstrativos das retenções de INSS são tirados sem um separador de totais identificando os meses e as pessoas fis/jur\. Esse chamado trata da inclusão desses totais nos demonstrativos\.

CH81520

# Rotinas de Geração da GPS

Considerar notas fiscais classificação fiscal = 8 e 9 na geração

OS3232

# Rotinas de Geração da GPS

Permitir consolidação da GPS por CNPJ

OS3128

# Recuperação da Tela de Manutenção das Consolidações das Retenções de INSS

Conforme especificado no documento de requisitos o sistema realmente não traz todas as retenções para manutenção das consolidações, portanto, o objetivo desse documento é de alterar a regra de recuperação atual fazendo com que todas as operações sejam recuperadas comparando somente o mês/ano do cadastro da PFJ com o mês/ano da data fiscal da tela de consolidação das retenções\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

No campo 26 da SAFX04 “Classe de Pessoa Fís/Jur” deverá ser incluída a opção “05\-Cooperativa de transporte”\.

OS2494

__RN01__

O nome desse campo será somente “Data do Fato gerador”

OS2494

__RN02__

Quando da geração da retenção de INSS, se identificado que no campo 26 da SAFX 04 a informação colocada é “Cooperativa de transporte”, o campo “Data do fato gerador” dessa tela \(Manutenção de Dados de Retenção\) será igual a informação colocada no campo “Data Fiscal”\.

OS2494

__RN03__

Quando da geração das retenções de INSS o sistema deverá quando estiver lendo as informações da tabela SAFX07 deverá considerar também durante a gravação das informações, os dados colocados nos campos 151 \- Segunda Base de Cálculo para INSS, 152 \- Segunda Alíquota de INSS, 153 \- Segundo Valor de Tributo INSS e 154 \- Segundo Código de Pagamento INSS\. Da mesma forma que era feito na release 27\.

OS2613

__RN04__

Quando da geração da consolidação das retenções de INSS o sistema deverá quando estiver lendo as informações da tabela SAFX07 deverá considerar também durante a gravação das informações, os dados colocados nos campos 151 \- Segunda Base de Cálculo para INSS, 152 \- Segunda Alíquota de INSS, 153 \- Segundo Valor de Tributo INSS e 154 \- Segundo Código de Pagamento INSS\. Da mesma forma que era feito na release 27\.

OS2613

__RN05__

Verificar se para a alteração conforme RN00 e RN01 deve – se somente retirar o comentário feito na procedure__* saf\_inss\_df\.*__

OS2613

__RN06__

Após a alteração conforme RN00 e RN01, o sistema terá de gerar guias separadas para os dados colocados nos campos 151, 152, 153 e 154 da SAFX07\.

OS2613

__RN07__

Após a demonstração de cada pessoa jurídica terá um totalizador da “PJ”\. Porém, essas quebras do relatório deverão ser conforme o critério utilizado pelo usuário no momento da seleção das informações\.

Ex: O = Empresa \+ Estabelecimento \+ Pessoa Fis/Jur\.

Logo se o critério de geração do demonstrativo for \(competência\) o demonstrativo será organizado por ordem de Data emissão:

Por data Competência = O \+ Data de Emissão \+ Data Fiscal\.

Ou seja, o demonstrativo será organizado pela data de emissão\. Dentro das datas de emissão terá uma quebra a cada pessoa Fis/Jur diferente e quando o mês de emissão mudar, será apresentada outra quebra com o valor total daquele mês\.

CH50401

__RN08__

Após a demonstração de cada pessoa jurídica terá um totalizador da “PJ”\. Porém, essas quebras do relatório deverão ser conforme o critério utilizado pelo usuário no momento da seleção das informações\.

Ex: O = Empresa \+ Estabelecimento \+ Pessoa Fis/Jur\.

Logo se o critério de geração do demonstrativo for \(competência \+ Extemporâneo\) o demonstrativo será organizado por ordem de Data emissão:

Por data Competência \+ Extemporâneo = O \+ Data de Emissão \+ Data Fiscal\.

Ou seja, o relatório traz as notas cujo período de emissão seja diferente do período de lançamento e que ultrapasse a data limite parametrizada no sistema\. Com a alteração solicitada nesse chamado, esse mesmo resultado deverá ser organizado da seguinte forma:

O demonstrativo será organizado pela data de emissão\. Dentro das datas de emissão terá uma quebra a cada pessoa Fis/Jur diferente e quando o mês de emissão mudar, será apresentada outra quebra com o valor total daquele mês\.

CH50401

__RN09__

Após a demonstração de cada pessoa jurídica terá um totalizador da “PJ”\. Porém, essas quebras do relatório deverão ser conforme o critério utilizado pelo usuário no momento da seleção das informações\.

Ex: O = Empresa \+ Estabelecimento \+ Pessoa Fis/Jur\.

Logo se o critério de geração do demonstrativo for \(Data Fiscal\) o demonstrativo será organizado por ordem de Data de lançamento:

Por Data Fiscal = O \+ Data Fiscal \+ Data de Emissão\.

Ou seja, o relatório traz as notas cujo período de lançamento seja diferente do período de emissão, trazendo inclusive as notas que passaram da data limite parametrizada no sistema\. Com a alteração solicitada nesse chamado, esse mesmo resultado deverá ser organizado da seguinte forma:

O demonstrativo será organizado pela data de lançamento\. Dentro das datas fiscais terá uma quebra a cada pessoa Fis/Jur diferente e quando o mês de lançamento mudar, será apresentada outra quebra com o valor total daquele mês\.

CH50401

__RN10__

Após a demonstração de cada pessoa jurídica terá um totalizador da “PJ”\. Porém, essas quebras do relatório deverão ser conforme o critério utilizado pelo usuário no momento da seleção das informações\.

Ex: O = Empresa \+ Estabelecimento \+ Pessoa Fis/Jur\.

Logo se o critério de geração do demonstrativo for \(Data Fiscal \+ Extemporâneo\) o demonstrativo será organizado por ordem de Data de lançamento:

Por Data Fiscal \+ Extemporâneo = O \+ Data Fiscal \+ Data de Emissão\.

Ou seja, o relatório traz as notas cujo período de lançamento seja diferente do período de emissão e que ultrapasse a data limite parametrizada no sistema\. Com a alteração solicitada nesse chamado, esse mesmo resultado deverá ser organizado da seguinte forma:

O demonstrativo será organizado pela data de lançamento\. Dentro das datas fiscais terá uma quebra a cada pessoa Fis/Jur diferente e quando o mês de lançamento mudar, será apresentada outra quebra com o valor total daquele mês\.

CH50401

__RN11__

Ao final do relatório, independente do critério utilizado para geração do mesmo, terá um totalizador geral\. Que deverá se igual a soma dos meses apresentados no relatório\.

Obs: Essa regra será aplicada para os demonstrativos que apresentarem os totalizadores “geral e por estabelecimento”, caso exista demonstrativos que não apresentem esses totais, este não deverá ser inserido, permanecendo assim como esta\.

CH50401

__RN12__

Quando o prestador do serviço for uma pessoa física, na GPS as informações devem ser do contratante, e não do prestador\.

Nos campos NOME/RAZAO SOCIAL/FONE ENDEREÇO e no campo IDENTIFICADOR devem ser demonstradas as informações não do prestador do serviço e sim do contratante do serviço, pois neste tipo de operação é ele quem efetua o pagamento dos 20% do INSS\. 

Neste caso, o sistema deverá:

1. Identificar a PF/PJ do documento fiscal de serviço\.
2. Caso a PF/PJ seja uma Pessoa Física gerar os dados do estabelecimento na GPS\.

CH59907\-A

__RN13__

A regra RN12 só se aplica quando a pessoa da nota fiscal for __física__ \(para pessoa jurídica a regra não deve ser alterada\!\)\.

Para poder distinguir isso, o sistema deve se valer de um dos critérios abaixo\. Os dois critérios deverão ser incorporados, porém não deverá ser obrigatório o preenchimento dos dois, apenas um deles preenchido é suficiente:

1. Caso o campo CPF/CNPJ \(06 da safx04\) possua 11 posições;

*    ou*

1. O campo “Classe de Pessoa Fis\./Jur\.” \(26 da safx04\) esteja preenchido com a opção “01 – Pessoa Física”\.

CH59907\-A

__RN14__

Nas parametrizações do cliente, as notas de pessoa física têm uma parametrização própria por cedente ou por estabelecimento\.

Esta parametrização já determina que as guias de pessoa física ou de pessoa jurídica sejam geradas separadamente, por isso não será necessário nenhum tratamento para este ponto\.

CH59907\-A

__RN15__

__Geração da GPS__

Alterar a geração da GPS para considerar também as notas fiscais cuja classificação sejam 8 ou 9 \(cod\_clas\_doc\_fis = 8, 9\), quando a parametrização do INSS for qualquer uma das relacionadas abaixo:

→ Por Pessoa Física Jurídica x Alíquota

→ Código de Pagamento

→ Código de Pagamento x Alíquota

Esta alteração deverá impactar todas as rotinas da GPS:

- Geração das Retenções de INSS
- Geração da Consolidação das Retenções
- Relatório de Conferência para as Retenções
- GPS → Digitação/Emissão

CH81520

__RN16__

__Emissão do Demonstrativo de INSS__

Considerar também as notas fiscais cuja classificação sejam 8 ou 9 \(cod\_clas\_doc\_fis = 8, 9\) nos seguintes Demonstrativos:

OTF → Outras Obrigações → Retenção de INSS – Serviços Prestados → Emissão do Demonstrativo de INSS →

- INSS por Cedente \(Fonte\) → Analítico
- INSS por Cedente \(Fonte\) → Sintético
- INSS por Estabelecimento \(Avulso\) → Analítico
- INSS por Estabelecimento \(Avulso\) → Sintético
- Geral → Analítico
- Geral → Sintético

CH81520

__RN17__

__Geração das Retenções de INSS__

__Parâmetro “Processar”:__

__Opções:__

\(  \) Retenções do INSS a partir das notas fiscais

\(  \) Consolidação das retenções para emissão da GPS

\(  \) Ambas

Quando for escolhida a segunda ou a terceira opção, habilitar o parâmetro abaixo\.

Se for escolhida a primeira opção, o parâmetro abaixo deverá ficar desabilitado:

*Consolidar GPS por:*

*         \(  \) Código da Pessoa Fis/Jur*

*         \(  \) CNPJ/CPF*

SE ao clicar em “Execução”, não for escolhida nenhuma das duas opções, exibir a seguinte mensagem:

__MasterSAF \- IR__

__X__

 

 

 

 

 

 

 

 

__Informe "Consolidar GPS por:"__

 

 

 

 

 

 

 

 

OS3232

__RN18__

__Parâmetro “Consolidar GPS por:”__

Este parâmetro será habilitado na tela somente quando as opções do parâmetro “Processar”, forem:

2 \- Consolidação das retenções para emissão da GPS

3 \- Ambas

__→ Quando a opção de consolidação for “*Código da Pessoa Fis/Jur*”:__

Deverá ser mantida a forma de consolidação atual, ou seja:

__Estabelecimento Avulso__

__Cedente/Fonte__

Código da Empresa

Código do Estabelecimento

Código da Retenção

Indicador GFIP

Código CEI

Mês/Ano

Código Pessoa Fis/Jur

CNPJ/CPF

Código da Retenção

Indicador GFIP

Código CEI

Mês/Ano

__→ Quando a opção de consolidação for “*CNPJ/CPF*”:__

Consolidar conforme indicação abaixo:

__Estabelecimento Avulso__

__Cedente/Fonte__

Código da Empresa

Código do Estabelecimento

Código da Retenção

Indicador GFIP

Código CEI

Mês/Ano

CNPJ/CPF

Código da Retenção

Indicador GFIP

Código CEI

Mês/Ano

Neste caso, acumular o código/razão social de uma das quaisquer pessoas fis/jur para a emissão da GPS\.

 

OS3232

__RN19__

__Regra para recuperação da tela de manutenção das consolidações das retenções de INSS__

Deverá ser mantida a recuperação atual, somente alterando a seguinte regra:

Recuperar os dados referente ao período informado da tabela IRT\_RET\_INSS\_CED 

__SE__

O campo VALID\_FIS\_JUR da tabela X04 \(Validade\) deve ter mês/ano <= ao mês/ano do campo DAT\_FISCAL da tabela IRT\_RET\_INSS\_CED 

OBS: Não considerar o dia informado nos dois campos\.

OS3128

