# MTZ-OTF-Geracao-Emissao_Informe_de_Rendimentos_IN_698-2006

- **Fonte:** MTZ-OTF-Geracao-Emissao_Informe_de_Rendimentos_IN_698-2006.docx
- **Modificado:** 2026-02-05
- **Tamanho:** 65 KB

---

# Geração / Emissão Informe de Rendimentos Financeiros – IN 698/2006

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3752

Obrigações de Tributos Federais \- Nomenclatura IN 698/2006

Trata\-se da criação do Informe de Rendimentos Financeiros, de acordo com a IN 698/2006\.

OS3752\-A

Obrigações de Tributos Federais \- Nomenclatura IN 698/2006

Implementa a geração dos quadros 4 – Rendimentos Isentos, 5 – Rendimentos Sujeitos à Tributação Exclusiva, 6 – Saldos em Contas Correntes e em VGBL e 7 – Créditos em Transito do Informe de Rendimentos Financeiros\.

OS3752\-B

Obrigações de Tributos Federais \- Geração dos Rendimentos dos Quadros 4 e 5 a partir da SAFX53

Trata\-se do ajuste para o cliente Caixa Seguradora para que as colunas “Rendimentos” e “Rendimentos Líquidos” sejam geradas a partir da SAFX53 e não mais da SAFX195 conforme implementação da OS3752\-A\.

A OS3752\-A foi desenvolvida criando uma tabela SAFX em que as informações de Saldos e Rendimentos fossem informadas em um único lugar\. Ocorre que o cliente Caixa Seguradora não possui os meios de extrair essa informação e montar a tabela SAFX195 para importação no produto, logo o cliente gostaria que o produto realizasse o somatório a partir da SAFX53 que já estaria carregada no produto\.

O cliente irá utilizar apenas as seguintes linhas:

- Rendimentos Isentos
	- 3 – Demais
- Rendimentos Sujeitos à Tributação Exclusiva
	- 3 – Títulos de Capitalização
	- 6 – Previdência Complementar, Fapi, PGBL e VGBL

Nesse caso, essas linhas serão recuperadas da SAFX53, enquanto que as demais linhas dos quadros 4 – Rendimentos Isentos e 5 – Rendimentos Sujeitos à Tributação Exclusiva, continuarão sendo geradas a partir da carga e importação da SAFX195\.

OS3996

Obrigações de Tributos Federais – Alteração da cor de fundo dos Informes de Rendimento

Essa OS tem por objetivo, alterar a cor de fundo dos Informes de Rendimento\. Conforme documento de visão da OS3996, foram solicitados os seguintes itens, porém conforme alinhamento com o Sr\. Marcos Paula em 08/10/2013, só será desenvolvido na OS\-3996 a alteração da cor de fundo\.

Os itens solicitados no documento de visão foram:

__Item__

__Descrição__

__Solução__

1

Criação de uma tabela auxiliar no cadastro de pessoas onde será informado para cada CPF ou CNPJ a suas respectivas classificações\. Exemplo:1 – corretor, 2\- prestador, 3 \- beneficiário\), lembrando que o CPF/CNPJ poderá ter mais de uma classificação\. Tratar e disponibilizar ao usuário a seleção das classificações em tempo de geração dos informes\.

O cliente poderá tratar pelo Código de Operação, conforme informações do Marcos Paula\.

2

PDF Individual: Necessidade de que os informes sejam gerados em PDF individualmente  por CPF/CNPJ, e que o nome do arquivo seja parametrizável\.

Será tratado na OS\-4000\.

3

Logotipo nos informes: Ter funcionalidade de inserir a imagem do logotipo de cada empresa nos informes de forma parametrizável

Será tratado na OS\-3997\.

__4__

__Configuração do Envelope: Ter funcionalidade de definir a cor do fundo do envelope, de forma a não deixar transparecer nenhuma informação sigilosa e também possibilitar a configuração das dobras do envelope, pois dependendo a impressora, a dobra poderá sofrer ajustes\.__

__Será tratado na OS\-3996\.__

5

Informação de Isenção: Alguns beneficiários possuem Isenção em parte da tributação do IRRF a ser apresentado no Informe e Dirf, para composição do valor a ser demonstrado, é preciso ter campos específicos nas retenções para que o tratamento seja feito\.

Tipos de Isenção: Aposentado maior de 65 anos, beneficiário associado a cooperativa de transporte \(Taxi\) e beneficiário portador de moléstia grave\. Este item aplica\-se somente ao Informe de Rendimentos de terceiros \(Pessoa Física\) e aos Registros da Dirf especificos para estas informações\.

Será tratado na OS\-3999\.

Vale salientar que o controle de margem solicitado no item 4, já foi solicitado por outros clientes \(vide OS\-3956\) e há dificuldade técnica para implementação dessa demanda\. Logo esse item não será desenvolvido nessa OS\-3996 \(ver e\-mail sobre a margem anexo junto à demanda\)\.

OS4000

Obrigações de Tributos Federais \- Geração dos Informes de Rendimento Individualizados

Essa OS tem por objetivo, permitir a geração dos informes de rendimento individualizados, ou seja, que para cada informe de rendimento seja gerado um arquivo PDF diferente\. Além disso, será permitido que o usuário parametrize a forma como o nome do informe será disponibilizado\. Para essa OS foram solicitados diversos itens nos documentos de visão, que por sua vez foram segregados em diversas OS’s\. Abaixo seguem essas divisões:

Os itens solicitados no documento de visão foram:

__Item__

__Descrição__

__Solução__

1

Criação de uma tabela auxiliar no cadastro de pessoas onde será informado para cada CPF ou CNPJ a suas respectivas classificações\. Exemplo:1 – corretor, 2\- prestador, 3 \- beneficiário\), lembrando que o CPF/CNPJ poderá ter mais de uma classificação\. Tratar e disponibilizar ao usuário a seleção das classificações em tempo de geração dos informes\.

O cliente poderá tratar pelo Código de Operação, conforme informações do Marcos Paula\.

__2__

__PDF Individual: Necessidade de que os informes sejam gerados em PDF individualmente  por CPF/CNPJ, e que o nome do arquivo seja parametrizável\.__

__Será tratado na OS\-4000\.__

3

Logotipo nos informes: Ter funcionalidade de inserir a imagem do logotipo de cada empresa nos informes de forma parametrizável

Será tratado na OS\-3997\.

4

Configuração do Envelope: Ter funcionalidade de definir a cor do fundo do envelope, de forma a não deixar transparecer nenhuma informação sigilosa e também possibilitar a configuração das dobras do envelope, pois dependendo a impressora, a dobra poderá sofrer ajustes\.

Será tratado na OS\-3996\.

5

Informação de Isenção: Alguns beneficiários possuem Isenção em parte da tributação do IRRF a ser apresentado no Informe e Dirf, para composição do valor a ser demonstrado, é preciso ter campos específicos nas retenções para que o tratamento seja feito\.

Tipos de Isenção: Aposentado maior de 65 anos, beneficiário associado a cooperativa de transporte \(Taxi\) e beneficiário portador de moléstia grave\. Este item aplica\-se somente ao Informe de Rendimentos de terceiros \(Pessoa Física\) e aos Registros da Dirf especificos para estas informações\.

Será tratado na OS\-3999\.

OS3997

Obrigações de Tributos Federais – Inclusão de logotipo nos Informes de Rendimento

Essa OS tem por objetivo, permitir a inclusão do logotipo da empresa nos Informes de Rendimento\. Conforme documento de visão da OS3996, foram solicitados os seguintes itens, porém conforme alinhamento com o Sr\. Marcos Paula em 08/10/2013, só será desenvolvido na OS\-3997 a inclusão do logotipo nos informes de rendimento\.

Os itens solicitados no documento de visão foram:

__Item__

__Descrição__

__Solução__

1

Criação de uma tabela auxiliar no cadastro de pessoas onde será informado para cada CPF ou CNPJ a suas respectivas classificações\. Exemplo:1 – corretor, 2\- prestador, 3 \- beneficiário\), lembrando que o CPF/CNPJ poderá ter mais de uma classificação\. Tratar e disponibilizar ao usuário a seleção das classificações em tempo de geração dos informes\.

O cliente poderá tratar pelo Código de Operação, conforme informações do Marcos Paula\.

2

PDF Individual: Necessidade de que os informes sejam gerados em PDF individualmente  por CPF/CNPJ, e que o nome do arquivo seja parametrizável\.

Será tratado na OS\-4000\.

__3__

__Logotipo nos informes: Ter funcionalidade de inserir a imagem do logotipo de cada empresa nos informes de forma parametrizável__

__Será tratado na OS\-3997\.__

4

Configuração do Envelope: Ter funcionalidade de definir a cor do fundo do envelope, de forma a não deixar transparecer nenhuma informação sigilosa e também possibilitar a configuração das dobras do envelope, pois dependendo a impressora, a dobra poderá sofrer ajustes\.

Será tratado na OS\-3996\.

5

Informação de Isenção: Alguns beneficiários possuem Isenção em parte da tributação do IRRF a ser apresentado no Informe e Dirf, para composição do valor a ser demonstrado, é preciso ter campos específicos nas retenções para que o tratamento seja feito\.

Tipos de Isenção: Aposentado maior de 65 anos, beneficiário associado a cooperativa de transporte \(Taxi\) e beneficiário portador de moléstia grave\. Este item aplica\-se somente ao Informe de Rendimentos de terceiros \(Pessoa Física\) e aos Registros da Dirf especificos para estas informações\.

Será tratado na OS\-3999\.

Vale salientar que o controle de margem solicitado no item 4, já foi solicitado por outros clientes \(vide OS\-3956\) e há dificuldade técnica para implementação dessa demanda\. Logo esse item não será desenvolvido nessa OS\-3996 \(ver e\-mail sobre a margem anexo junto à demanda\)\.

#### Cód\.

### Descrição

###     DR

# RN01

Deverá ser criada no módulo Obrigações de Tributos Federais, a tela “<a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>Geração / Emissão Informe de Rendimentos Financeiros – IN 698/2006”\. Essa tela irá permitir que o usuário gere as informações que irão compor o Informe de Rendimentos e emita o mesmo\. 

Essa tela será disponibilizada no menu: Rendimentos >> Rendimentos Financeiros >> Informe de Rendimentos Financeiros – IN 698/2006\. Esse menu deverá ser disponibilizado abaixo do menu “Juros Remuneratórios do Capital Próprio”\.

OS3752

# RN02

Nessa tela deverão ser exibidos os seguintes campos:

- __Empresa: __nesse campo o usuário poderá selecionar a Empresa para a geração do relatório\. Essa informação será recuperada da tabela EMPRESA e será exibida através do “Código Empresa” \+ “Descrição Empresa” separada por hífen \(\-\)\. *Exemplo: 001 – Empresa 001*\. Campo obrigatório de preenchimento\.
- __Estabelecimento:__ nesse campo o usuário poderá selecionar o Estabelecimento para a geração do relatório\. Essa informação será recuperada da tabela ESTABELECIMENTO e será exibida através do “Código Estabelecimento” \+ “Descrição Estabelecimento” separada por hífen \(\-\)\. *Exemplo: 001 – Estabelecimento 001*\. Campo obrigatório de preenchimento\.
- __Ano Calendário: __nesse campo o usuário irá informar o Ano Calendário para a geração do Informe de Rendimentos\. Esse campo deverá ser Numérico de 4 \(quatro\) posições\. Campo obrigatório de preenchimento\.
- __Pessoa Física:__ nesse campo o usuário poderá pesquisar uma Pessoa Física para filtrar os Informes de Rendimento por esse beneficiário\. As informações serão recuperadas da tabela X04\_PESSOA\_FIS\_JUR de beneficiários que sejam pessoas físicas\. Campo não obrigatório de preenchimento\.
- __Informações Complementares:__ nesse campo o usuário poderá informar as Informações Complementares que irão ser exibidas no Informe de Rendimentos\. Esse campo deverá ser Alfanumérico de 70 \(setenta\) posições\. Campo não obrigatório de preenchimento\.
- __Gerar informações de Rendimentos/Rendimentos Líquidos a partir da SAFX53:__ caso esse parâmetro seja selecionado parte da coluna “Rendimentos” do quadro 4 – Rendimentos Isentos e parte da coluna “Rendimentos Líquidos” do quadro 5 – Rendimentos Sujeitos à Tributação Exclusiva serão geradas a partir da SAFX53 e não da SAFX195\. A regra para recuperação das informações a partir da seleção desse parâmetro encontra\-se mais adiante nesse mesmo documento\.

Serão recuperados os registros do Controle de Tributos \(tabela: X53\_RETENCAO\_IRRF\) de Pessoas Físicas e cujos Códigos de Receita \(DARF\) estejam parametrizados no menu: Parâmetros >> Parâmetros por Código de Receita – IN 698/2006 do módulo Obrigações de Tributos Federais\. Além disso, os registros serão recuperados de acordo com o Ano Calendário informado para a Data de Movimento existente na tabela de Controle de Tributos, ou seja, caso o Ano Calendário seja “2011” serão recuperados os registros do Controle de Tributos cuja Data de Movimento seja do ano de 2011\.

Serão recuperados também os registros da tabela de Informações Complementares de Informe de Rendimentos Financeiros \(SAFX195\) considerando os critérios de empresa, estabelecimento e ano calendário informados, considerando como critério de comparação para seleção das informações os campos de empresa, estabelecimento e data do movimento, onde a data de movimento deve compreender o ano calendário parametrizado\.

O informe deve ser gerado mesmo que só exista informações em uma das tabelas origem \(SAFX53 ou SAFX195\)\.

Ao gerar o Informe de Rendimentos, vale salientar que embora para uma mesma Empresa, Estabelecimento e Grupo existam mais de um Código Receita \(DARF\) com datas de validade distintas, o sistema irá gerar os Informes de Rendimento para todos os códigos cadastrados na parametrização independente da data de validade do mesmo, ou seja, o Informe de Rendimentos será composto por todos os Códigos DARF informados no Controle de Tributos e que estejam parametrizados\.

OS3752

OS3752\-A

OS3752\-B

# RN03

A geração do cabeçalho do Informe de Rendimentos Financeiros deverá exibir no campo “Ano\-Calendário de” o ano de acordo com o campo “Ano Calendário” informado na tela Parâmetros Rendimentos >> Rendimentos Financeiros >> Informe de Rendimentos Financeiros – IN 698/2006\.

OS3752

# RN04

No quadro __1 – Identificação da Fonte Pagadora__, o sistema deverá exibir as seguintes informações:

- __Nome Empresarial:__ deverá ser exibida a Razão Social do Estabelecimento de acordo com a tabela ESTABELECIMENTO\.
- __CNPJ:__ deverá ser exibido o CNPJ do Estabelecimento de acordo com a tabela ESTABELECIMENTO\.

OS3752

# RN05

No quadro __2 – Pessoa Física Beneficiária dos Rendimentos__, o sistema deverá exibir as seguintes informações:

- __CPF:__ deverá ser exibido o CPF do Beneficiário, de acordo com a Pessoa Física/Jurídica informada no Controle de Tributos \(tabela: X53\_RETENCAO\_IRRF\)\.
- __Nome Completo:__ deverá ser exibido o Nome Completo do Beneficiário, de acordo com a Pessoa Física/Jurídica informada no Controle de Tributos \(tabela: X53\_RETENCAO\_IRRF\)\.

OS3752

# RN06

A geração do quadro __3 – Rendimentos Tributáveis na Declaração de Ajuste Anual \(Valores em Reais\)__ será realizada da seguinte maneira:

- __01 – Previdência Complementar__
	- Na coluna “Rendimentos” deverão ser recuperados os Rendimentos Tributáveis do Beneficiário de acordo com o Código de Receita parametrizado na tela Parâmetros >> Parâmetros por Código de Receita – IN 698/2006\. Os rendimentos tributáveis será o somatório dos campos “Valor Bruto” e “Valor Outros de Tributação Exclusiva” do Controle de Tributos\.
	- Na coluna “Imposto Retido na Fonte” deverá ser recuperado o Imposto de Renda Retido na Fonte do Beneficiário de acordo com o Código de Receita parametrizado na tela Parâmetros >> Parâmetros por Código de Receita – IN 698/2006\. O Imposto de Renda Retido na Fonte é o campo “Valor Tributo” do Controle de Tributos\.
- __02 – Fundo de Aposentadoria Programada Individual \(Fapi\)__
	- Na coluna “Rendimentos” deverão ser recuperados os Rendimentos Tributáveis do Beneficiário de acordo com o Código de Receita parametrizado na tela Parâmetros >> Parâmetros por Código de Receita – IN 698/2006\. Os rendimentos tributáveis será o somatório dos campos “Valor Bruto” e “Valor Outros de Tributação Exclusiva” do Controle de Tributos\.
	- Na coluna “Imposto Retido na Fonte” deverá ser recuperado o Imposto de Renda Retido na Fonte do Beneficiário de acordo com o Código de Receita parametrizado na tela Parâmetros >> Parâmetros por Código de Receita – IN 698/2006\. O Imposto de Renda Retido na Fonte é o campo “Valor Tributo” do Controle de Tributos\.
- __03 \- Plano Gerador de Benefício Livre \(PGBL\)__
	- Na coluna “Rendimentos” deverão ser recuperados os Rendimentos Tributáveis do Beneficiário de acordo com o Código de Receita parametrizado na tela Parâmetros >> Parâmetros por Código de Receita – IN 698/2006\. Os rendimentos tributáveis será o somatório dos campos “Valor Bruto” e “Valor Outros de Tributação Exclusiva” do Controle de Tributos\.
	- Na coluna “Imposto Retido na Fonte” deverá ser recuperado o Imposto de Renda Retido na Fonte do Beneficiário de acordo com o Código de Receita parametrizado na tela Parâmetros >> Parâmetros por Código de Receita – IN 698/2006\. O Imposto de Renda Retido na Fonte é o campo “Valor Tributo” do Controle de Tributos\.
- __04 – Vida Gerador de Benefício Livre \(VGBL\)__
	- Na coluna “Rendimentos” deverão ser recuperados os Rendimentos Tributáveis do Beneficiário de acordo com o Código de Receita parametrizado na tela Parâmetros >> Parâmetros por Código de Receita – IN 698/2006\. Os rendimentos tributáveis será o somatório dos campos “Valor Bruto” e “Valor Outros de Tributação Exclusiva” do Controle de Tributos\.
	- Na coluna “Imposto Retido na Fonte” deverá ser recuperado o Imposto de Renda Retido na Fonte do Beneficiário de acordo com o Código de Receita parametrizado na tela Parâmetros >> Parâmetros por Código de Receita – IN 698/2006\. O Imposto de Renda Retido na Fonte é o campo “Valor Tributo” do Controle de Tributos\.
- __05 – Demais \(especificar\)__
	- Na coluna “Rendimentos” deverão ser recuperados os Rendimentos Tributáveis do Beneficiário de acordo com o Código de Receita parametrizado na tela Parâmetros >> Parâmetros por Código de Receita – IN 698/2006\. Os rendimentos tributáveis será o somatório dos campos “Valor Bruto” e “Valor Outros de Tributação Exclusiva” do Controle de Tributos\.
	- Na coluna “Imposto Retido na Fonte” deverá ser recuperado o Imposto de Renda Retido na Fonte do Beneficiário de acordo com o Código de Receita parametrizado na tela Parâmetros >> Parâmetros por Código de Receita – IN 698/2006\. O Imposto de Renda Retido na Fonte é o campo “Valor Tributo” do Controle de Tributos\.
- __06 – TOTAL__
	- Na coluna “Rendimentos” o sistema deverá realizar uma totalização de todos os valores\.
	- Na coluna “Imposto Retido na Fonte” o sistema deverá realizar uma totalização de todos os valores\.
	- A linha “TOTAL” não é parametrizada pelo usuário na tela de Nomenclatura, a mesma deve ser gerada automaticamente pelo sistema\. Nesse exemplo, a mesma é descrita como “06” porque a última linha anterior é a “05”, porém esse valor deverá ser alterado, conforme a quantidade de parametrizações do usu

Vale salientar que na coluna “Especificação” onde constam as linhas que irão compor o Informe de Rendimentos, o conteúdo das mesmas é recuperado do campo “Descrição” da tela Nomenclatura – IN 698/2006, desde que o campo “Classe” = “3 – Rendimentos Tributáveis”\.

As nomenclaturas do quadro 3 irão ser exibidas de acordo com a parametrização de nomenclatura, independente se a mesma possuir valores para serem recuperados na tabela de Controle de Tributos OU se essas nomenclaturas estão associadas a algum Código DARF\.

OS3752

# RN07

Caso alguma das linhas do quadro 3 não possuam valor superior a 0,00 \(zero\) ou o mesmo não seja informado, a linha deverá ser gerada em branco\.

OS3752

# RN08

Os quadros 4, 5, 6 e 7 não serão gerados de forma automática assim como o quadro 3 nesse momento e deverão ser gerados em branco as suas colunas, exceto as colunas de Saldos em 31/12 da linha 02 do quadro 4 e das linhas 05 e 06 do quadro 5 que deverão ser exibidas em uma cor mais escura\.

A coluna “Especificação” dos quadros 4, 5, 6 e 7 deverão ser geradas com as seguintes descrições:

__4\. RENDIMENTOS ISENTOS \(Valores em reais\)__

01\. Contas de Poupança e Letras Hipotecárias

02\. Lucros e Dividendo apurados a partir de 1996 e distribuídos no ano\-calendário

03\. Demais \(especificar\)

__5\. RENDIMENTOS SUJEITOS À TRIBUTAÇÃO EXCLUSIVA \(Valores em reais\)__

01\. Fundos de Investimento

02\. Aplicações de Renda Fixa

03\. Títulos de Capitalização

04\. Juros sobre o Capital Próprio

05\. Operações de Swap

06\. Previdência Complementar, Fapi, PGBL e VGBL

07\. Demais \(especificar\)

08\. TOTAL

__6\. SALDO EM CONTAS CORRENTES EM VGBL \(Valores em reais\)__

01\. Depósito em conta corrente de depósito à vista ou de investimento

02\. Prêmios acumulados em VGBL

__7\. CRÉDITOS EM TRÂNSITO \(Valores em reais\)__

01\. Fundos e clubes de investimento

02\. Demais

Isso se deve ao fato de que o cliente Caixa Seguros não gera as informações desses quadros pelo produto, porém será gerada outra OS para que essas colunas sejam geradas\. 

*OBS: Esses quadros – 4, 5, 6 e 7 – serão gerados a partir da OS3752\-A\. vale salientar que a descrição das linhas dos quadros 4, 5, 6 e 7 será alterada a partir dessa OS, respeitando a parametrização do usuário, assim como no quadro 3\.*

OS3752

# RN09

A geração do quadro __8 – Informações Complementares__ do Informe de Rendimentos será feita a partir do preenchimento do campo “Informações Complementares” do menu: Parâmetros Rendimentos >> Rendimentos Financeiros >> Informe de Rendimentos Financeiros – IN 698/2006 do módulo Obrigações de Tributos Federais\.

Caso o campo não seja preenchido, esse quadro do Informe de Rendimentos também não o será\.

OS3752

# RN10

A geração dos quadros 4 – Rendimentos Isentos, 5 – Rendimentos Sujeitos à Tributação Exclusiva, 6 – Saldos em Contas Correntes e em VGBL e 7 – Créditos em Transito será realizada com base nas informações carregadas na tabela de Informações Complementares de Informe de Rendimentos Financeiros \(SAFX195\), exceto nas seguintes condições:

- Caso o parâmetro “Gerar informações de Rendimentos/Rendimentos Líquidos a partir da SAFX53” esteja selecionado:
	- Recuperar da X53\_RETENCAO\_IRRF
		- Coluna “Rendimentos” da Linha 03 – Demais do quadro 4 – Rendimentos Isentos, de acordo com os cálculos informados na OS3752\-B para os Códigos DARF “0561” ou “6891” desde que o campo “Valor Aposentadoria Isenta” > 0\.
		- Coluna “Rendimentos Líquidos” da Linha 03 – Títulos de Capitalização do quadro 5 – Rendimentos Sujeitos à Tributação Exclusiva, de acordo com os cálculos informados na OS3752\-B para o Código DARF “0916” desde que um dos campos – Valor Bruto, Valor Tributo ou Valor Outros Tributação Exclusiva – esteja preenchido\.
		- Coluna “Rendimentos Líquidos” da Linha 06 – Previdência Complementar, Fapi, PGBL e VGBL – Demais do quadro 5 – Rendimentos Sujeitos à Tributação Exclusiva, de acordo com os cálculos informados na OS3752\-B para o Código DARF “5565” desde que um dos campos – Valor Bruto, Valor Tributo ou Valor Outros Tributação Exclusiva – esteja preenchido\.

Como a geração do Informe acontece agrupando as informações por CNPJ da Fonte Pagadora e CPF do Beneficiário, no momento da geração as informações que estão em tabelas distintas deverão ser consolidadas para que seja gerado apenas um informe por CNPJ da Fonte Pagadora e CPF do Beneficiário\.

Exemplo: se tenho na SAFX53 informações que atendam a regra de seleção para gerar o quadro 3 e na SAFX195 informações que atendam a regra de seleção para gerar o quadro 4 e nestas tabelas distintas as informações são referentes ao mesmo CNPJ da Fonte Pagadora e CPF do Beneficiário deverá ser gerado apenas um informe demonstrando valores nos quadros 3 e 4, sendo cada valor de sua respectiva origem\.

OS3752\-A

OS3752\-B

# RN11

A geração do quadro 4\. RENDIMENTOS ISENTOS \(Valores em reais\) será realizada considerando informações da SAFX195 e respeitando as seguintes regras:

- 01\. Contas de Poupança e Letras Hipotecárias \(linha\):
	- Coluna “Saldos em 31/12 Ano\-Calendário Anterior”: Somatório dos valores informados no campo “Contas de Poupança e Letras Hipotecárias – Saldo Ano Anterior” considerando a regra de agrupamento\.
	- Coluna “Saldos em 31/12 Ano\-Calendário”: Somatório dos valores informados no campo “Contas de Poupança e Letras Hipotecárias – Saldo Ano Calendário” considerando a regra de agrupamento\.
	- Coluna “Rendimentos”: Somatório dos valores informados no campo “Contas de Poupança e Letras Hipotecárias – Rendimentos” considerando a regra de agrupamento\.
- 02\. Lucros e Dividendo apurados a partir de 1996 e distribuídos no ano\-calendário \(linha\):
	- Coluna “Saldos em 31/12 Ano\-Calendário Anterior”: Não se aplica\. Mostrar informação em cinza\.
	- Coluna “Saldos em 31/12 Ano\-Calendário”: Não se aplica\. Mostrar informação em cinza\.
	- Coluna “Rendimentos”: Somatório dos valores informados no campo “Lucros e Dividendos apurados a partir de 1996 e distribuídos no ano\-calendário – Rendimentos” considerando a regra de agrupamento\.
- 03\. Demais \(especificar\) \(linha\):
	- Coluna “Saldos em 31/12 Ano\-Calendário Anterior”: Somatório dos valores informados no campo “Demais Rendimentos Isentos – Saldo Ano Anterior” considerando a regra de agrupamento\.
	- Coluna “Saldos em 31/12 Ano\-Calendário”: Somatório dos valores informados no campo “Demais Rendimentos Isentos – Saldo Ano Calendário” considerando a regra de agrupamento\.
	- Coluna “Rendimentos”: Somatório dos valores informados no campo “Demais Rendimentos Isentos – Rendimentos” considerando a regra de agrupamento\.

OS3752\-A

# RN12

A geração do quadro 5\. RENDIMENTOS SUJEITOS À TRIBUTAÇÃO EXCLUSIVA \(Valores em reais\) será realizada considerando informações da SAFX195 e respeitando as seguintes regras:

- 01\. Fundos de Investimento \(linha\):
	- Coluna “Saldos em 31/12 Ano\-Calendário Anterior”: Somatório dos valores informados no campo “Fundos de Investimento – Saldo Ano Anterior” considerando a regra de agrupamento\.
	- Coluna “Saldos em 31/12 Ano\-Calendário”: Somatório dos valores informados no campo “Fundos de Investimento – Saldo Ano Calendário” considerando a regra de agrupamento\.
	- Coluna “Rendimentos Líquidos”: Somatório dos valores informados no campo “Fundos de Investimento – Rendimentos” considerando a regra de agrupamento\.
- 02\. Aplicações de Renda Fixa \(linha\):
	- Coluna “Saldos em 31/12 Ano\-Calendário Anterior”: Somatório dos valores informados no campo “Aplicações de Renda Fixa – Saldo Ano Anterior” considerando a regra de agrupamento\.
	- Coluna “Saldos em 31/12 Ano\-Calendário”: Somatório dos valores informados no campo “Aplicações de Renda Fixa – Saldo Ano Calendário” considerando a regra de agrupamento\.
	- Coluna “Rendimentos Líquidos”: Somatório dos valores informados no campo “Aplicações de Renda Fixa – Rendimentos” considerando a regra de agrupamento\.
- 03\. Títulos de Capitalização \(linha\):
	- Coluna “Saldos em 31/12 Ano\-Calendário Anterior”: Somatório dos valores informados no campo “Títulos de Capitalização – Saldo Ano Anterior” considerando a regra de agrupamento\.
	- Coluna “Saldos em 31/12 Ano\-Calendário”: Somatório dos valores informados no campo “Títulos de Capitalização – Saldo Ano Calendário” considerando a regra de agrupamento\.
	- Coluna “Rendimentos Líquidos”: Somatório dos valores informados no campo “Títulos de Capitalização – Rendimentos” considerando a regra de agrupamento\.
- 04\. Juros sobre o Capital Próprio \(linha\):
	- Coluna “Saldos em 31/12 Ano\-Calendário Anterior”: Somatório dos valores informados no campo “Juros sobre Capital Próprio – Saldo Ano Anterior” considerando a regra de agrupamento\.
	- Coluna “Saldos em 31/12 Ano\-Calendário”: Somatório dos valores informados no campo “Juros sobre Capital Próprio – Saldo Ano Calendário” considerando a regra de agrupamento\.
	- Coluna “Rendimentos Líquidos”: Somatório dos valores informados no campo “Juros sobre Capital Próprio – Rendimentos” considerando a regra de agrupamento\.
- 05\. Operações de Swap \(linha\):
	- Coluna “Saldos em 31/12 Ano\-Calendário Anterior”: Não se aplica\. Mostrar informação em cinza\.
	- Coluna “Saldos em 31/12 Ano\-Calendário”: Não se aplica\. Mostrar informação em cinza\.
	- Coluna “Rendimentos Líquidos”: Somatório dos valores informados no campo “Operações Swap – Rendimentos” considerando a regra de agrupamento\.

OS3752\-A

# RN13

A geração do quadro 5\. RENDIMENTOS SUJEITOS À TRIBUTAÇÃO EXCLUSIVA \(Valores em reais\) será realizada considerando informações da SAFX195 e respeitando as seguintes regras:

- 06\. Previdência Complementar, Fapi, PGBL e VGBL \(linha\):
	- Coluna “Saldos em 31/12 Ano\-Calendário Anterior”: Não se aplica\. Mostrar informação em cinza\.
	- Coluna “Saldos em 31/12 Ano\-Calendário”: Não se aplica\. Mostrar informação em cinza\.
	- Coluna “Rendimentos Líquidos”: Somatório dos valores informados no campo “Previdência Complementar, Fapi, PGBL e VGBL – Rendimentos” considerando a regra de agrupamento\.
- 07\. Demais \(especificar\) \(linha\):
	- Coluna “Saldos em 31/12 Ano\-Calendário Anterior”: Somatório dos valores informados no campo “Demais Rendimentos Sujeitos à Tributação Exclusiva – Saldo Ano Anterior” considerando a regra de agrupamento\.
	- Coluna “Saldos em 31/12 Ano\-Calendário”: Somatório dos valores informados no campo “Demais Rendimentos Sujeitos à Tributação Exclusiva – Saldo Ano Calendário” considerando a regra de agrupamento\.
	- Coluna “Rendimentos Líquidos”: Somatório dos valores informados no campo “Demais Rendimentos Sujeitos à Tributação Exclusiva – Rendimentos” considerando a regra de agrupamento\.
- 08\. TOTAL \(linha\):
	- Coluna “Saldos em 31/12 Ano\-Calendário Anterior”: Totalização dos valores lançados na coluna “Saldos em 31/12 Ano\-Calendário Anterior” das linhas 01 a 07\.
	- Coluna “Saldos em 31/12 Ano\-Calendário”: Totalização dos valores lançados na coluna “Saldos em 31/12 Ano\-Calendário” das linhas 01 a 07\.
	- Coluna “Rendimentos Líquidos”: Totalização dos valores lançados na coluna “Rendimentos Líquidos” das linhas 01 a 07\.

OS3752\-A

# RN14

A geração do quadro 6\. SALDO EM CONTAS CORRENTES EM VGBL \(Valores em reais\) será realizada considerando informações da SAFX195 e respeitando as seguintes regras:

- 01\. Depósito em conta corrente de depósito à vista ou de investimento \(linha\):
	- Coluna “Saldos em 31/12 Ano\-Calendário Anterior”: Somatório dos valores informados no campo “Depósito em Conta Corrente de Depósito à Vista ou de Investimento – Saldo Ano Anterior” considerando a regra de agrupamento\.
	- Coluna “Saldos em 31/12 Ano\-Calendário”: Somatório dos valores informados no campo “Depósito em Conta Corrente de Depósito à Vista ou de Investimento – Saldo Ano Calendário” considerando a regra de agrupamento\.
- 02\. Prêmios acumulados em VGBL \(linha\):
	- Coluna “Saldos em 31/12 Ano\-Calendário Anterior”: Somatório dos valores informados no campo “Prêmios Acumulados em VGBL – Saldo Ano Anterior” considerando a regra de agrupamento\.
	- Coluna “Saldos em 31/12 Ano\-Calendário”: Somatório dos valores informados no campo “Prêmios Acumulados em VGBL – Saldo Ano Calendário” considerando a regra de agrupamento\.

OS3752\-A

# RN15

A geração do quadro 7\. CRÉDITOS EM TRÂNSITO \(Valores em reais\) será realizada considerando informações da SAFX195 e respeitando as seguintes regras:

- 01\. Fundos e clubes de investimento \(linha\)
	- Coluna “Saldos em 31/12 Ano\-Calendário Anterior”: Somatório dos valores informados no campo “Fundos e Clubes de Investimento – Ano Anterior” considerando a regra de agrupamento\.
	- Coluna “Saldos em 31/12 Ano\-Calendário”: Somatório dos valores informados no campo “Fundos e Clubes de Investimento – Ano Calendário” considerando a regra de agrupamento\.
- 02\. Demais \(linha\):
	- Coluna “Saldos em 31/12 Ano\-Calendário Anterior”: Somatório dos valores informados no campo “Demais Créditos em Trânsito – Ano Anterior” considerando a regra de agrupamento\.
	- Coluna “Saldos em 31/12 Ano\-Calendário”: Somatório dos valores informados no campo “Demais Créditos em Trânsito – Ano Calendário” considerando a regra de agrupamento\.

OS3752\-A

# RN16

Permitir a geração do Informe de Rendimentos Financeiros em PDF como ocorre na geração do relatório de Rendimentos dos Empregados \(Menu Rendimentos >> Rendimentos Empregados >> Emissão Declaração de Rendimentos >> Por Nome\)

OS3752\-A

# RN17

Caso o parâmetro “Gerar informações de Rendimentos/Rendimentos Líquidos a partir da SAFX53” esteja selecionado, a geração das colunas “Rendimentos” do quadro 4 – Rendimentos Isentos e “Rendimentos Líquidos” do quadro 5 – Rendimentos Sujeitos à Tributação Exclusiva será realizada da seguinte forma:

- 4 – Rendimentos Isentos
	- 03 – Demais \(especificar\)
		- Deverá ser somada a informação contida no campo VLR\_APOSENT\_ISENTA de todos os registros da SAFX53 do Beneficiário que está sendo gerado no Informe de Rendimentos – ou da X530\_RETIFICACAO\_IRRF mais recente se houver – cujo Código DARF seja “0561” ou “6891”\. Essa informação será gravada na coluna “Rendimentos” da linha 03 – Demais \(especificar\) do quadro 4 – Rendimentos Isentos\.
- 5 – Rendimentos Sujeitos à Tributação Exclusiva
	- 03 – Títulos de Capitalização
		- Deverá ser realizado o cálculo de subtração dos campos VLR\_BRUTO \+ VLR\_OUTROS\_TRIB\_EXCL – VLR\_IR\_RETIDO de todos os registros da SAFX53 do Beneficiário que está sendo gerado no Informe de Rendimentos – ou da X530\_RETIFICACAO\_IRRF mais recente se houver – cujo Código DARF seja “0916”\. Essa informação será gravada na coluna “Rendimentos Líquidos” da linha 03 – Títulos de Capitalização do quadro 5 – Rendimentos Sujeitos à Tributação Exclusiva\.
	- 06 – Previdência Complementar, Fapi, PGBL e VGBL
		- Deverá ser realizado o cálculo de subtração dos campos VLR\_BRUTO \+ VLR\_OUTROS\_TRIB\_EXCL – VLR\_IR\_RETIDO de todos os registros da SAFX53 do Beneficiário que está sendo gerado no Informe de Rendimentos – ou da X530\_RETIFICACAO\_IRRF mais recente se houver – cujo Código DARF seja “5565”\. Essa informação será gravada na coluna “Rendimentos Líquidos” da linha 06 – Previdência Complementar, Fapi, PGBL e VGBL do quadro 5 – Rendimentos Sujeitos à Tributação Exclusiva\.

OS3752\-B

# RN18

É importante frisar que caso o parâmetro “Gerar informações de Rendimentos/Rendimentos Líquidos a partir da SAFX53” seja selecionado, somente as linhas mencionadas na RN17 serão geradas dessa forma, ou seja, recuperando as informações da SAFX53 ao invés da SAFX195\.

Caso o parâmetro “Gerar informações de Rendimentos/Rendimentos Líquidos a partir da SAFX53” não esteja selecionado, essas linhas mencionadas na RN17 serão recuperadas normalmente através da tabela SAFX195\.

OS3752\-B

# RN19

As linhas abaixo não são geradas pelo cliente Caixa Seguradora, e só serão geradas através da SAFX195, mesmo que o parâmetro “Gerar informações de Rendimentos/Rendimentos Líquidos a partir da SAFX53” esteja selecionado\.

- 4 – Rendimentos Isentos
	- 01 – Contas de Poupança e Letras Hipotecárias
	- 02 – Lucros e Dividendos apurados a partir de 1996 e distribuídos no ano\-calendário
- 5 – Rendimentos Sujeitos à Tributação Exclusiva
	- 01 – Fundos de Investimento
	- 02 – Aplicações de Renda Fixa
	- 04 – Juros sobre Capital Próprio
	- 05 – Operações de Swap
	- 07 – Demais \(especificar\)

As linhas citadas a seguir só recuperarão as informações da X53\_RETENCAO\_IRRF para as colunas “Rendimentos” do quadro 4 e “Rendimentos Líquidos” do quadro 5 caso o parâmetro “Gerar informações de Rendimentos/Rendimentos Líquidos a partir da SAFX53” esteja selecionado\.

- 4 – Rendimentos Isentos
	- 03 – Demais \(especificar\)
- 5 – Rendimentos Sujeitos à Tributação Exclusiva
	- 03 – Títulos de Capitalização
	- 06 – Previdência Complementar, Fapi, PGBL e VGBL

As demais colunas das linhas citadas acima continuarão a recuperar as informações da SAFX195, independente da seleção do parâmetro “Gerar informações de Rendimentos/Rendimentos Líquidos a partir da SAFX53”\.

OS3752\-B

# RN20

Ao emitir o Informe de Rendimentos, o fundo do Informe deverá ficar na cor preta e ao ser dobrado, o mesmo não deverá permitir que o usuário visualize nenhuma informação que conste dentro do informe\.

__OS3996__

# RN21

__\[EXCLUÍDA – OS4000\] __Ao emitir o Informe de Rendimentos e clicar no botão “Gera PDF”, o sistema irá salvar o arquivo PDF na pasta que o usuário selecionar e com o nome parametrizado de acordo com a tela “Parâmetros de Nomenclatura dos Informes de Rendimento” \(menu: Parâmetros >> Parâmetros de Nomenclatura dos Informes de Rendimento\) do módulo Obrigações de Tributos Federais\.

Para cada informe de rendimento, existirá um arquivo PDF diferente\.

__OS4000__

# RN22

Caso na emissão do Informe de Rendimentos exista parametrização para a Empresa/Estabelecimento contendo o logotipo na tela “Logotipo para Emissão do Informe de Rendimentos” – menu: Parâmetros >> Logotipo para Emissão do Informe de Rendimentos – do módulo Obrigações de Tributos Federais, o sistema deverá recuperar a imagem do logotipo no campo “Logotipo” e deverá gerar esse logotipo na parte superior do informe\.

__OS3997__

# RN23

__\[EXCLUÍDA – OS4000\] __Deverá ser criado na tela “Emissão de Rendimentos Outros – por CNPJ” o parâmetro “Gerar Informes de Rendimento em Arquivos PDF Individualizados”\. Esse parâmetro deverá ser disponibilizado abaixo do parâmetro “Imprimir Endereco do Remetente e Destinatario no verso do Informe de Rendimentos”\. Por default esse parâmetro deverá ficar desmarcado\.

A emissão dos Informes de Rendimento deverá seguir o seguinte padrão a partir desse novo parâmetro:

- __Parâmetro desmarcado e estabelecimento parametrizado para ser gerado individualizado__
	- Caso o informe seja emitido com o parâmetro desmarcado e com o estabelecimento parametrizado para ser gerado individualizado \(menu: Parâmetros >> Parâmetros de Nomenclatura dos Informes de Rendimento\), os informes serão gerados normalmente – caso existam informações para tal – e o arquivo PDF conterá vários informes de rendimento \(conforme regra atual\)\.
- __Parâmetro desmarcado e estabelecimento não parametrizado para ser gerado individualizado__
	- Caso o informe seja emitido com o parâmetro desmarcado e com o estabelecimento não parametrizado para ser gerado individualizado \(menu: Parâmetros >> Parâmetros de Nomenclatura dos Informes de Rendimento\), os informes serão gerados normalmente – caso existam informações para tal – e o arquivo PDF conterá vários informes de rendimento \(conforme regra atual\)\.
- __Parâmetro marcado e estabelecimento parametrizado para ser gerado individualizado__
	- Caso o informe seja emitido com o parâmetro marcado e com o estabelecimento parametrizado para ser gerado individualizado \(menu: Parâmetros >> Parâmetros de Nomenclatura dos Informes de Rendimento\), os informes serão gerados normalmente conforme a Nomenclatura definida – caso existam informações para tal – e o arquivo PDF conterá apenas um informe de rendimento\.
- __Parâmetro marcado e estabelecimento não parametrizado para ser gerado individualizado__
	- Caso o informe seja emitido com o parâmetro marcado e com o estabelecimento não parametrizado para ser gerado individualizado \(menu: Parâmetros >> Parâmetros de Nomenclatura dos Informes de Rendimento\), os informes serão gerados normalmente – caso existam informações para tal – e o arquivo PDF conterá vários informes de rendimento \(conforme regra atual\)\.

__OS4000__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

