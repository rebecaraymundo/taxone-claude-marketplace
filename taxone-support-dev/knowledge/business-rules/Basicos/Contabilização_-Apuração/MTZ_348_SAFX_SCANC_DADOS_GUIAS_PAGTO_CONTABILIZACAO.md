# MTZ_348_SAFX_SCANC_DADOS_GUIAS_PAGTO_CONTABILIZACAO

- **Fonte:** MTZ_348_SAFX_SCANC_DADOS_GUIAS_PAGTO_CONTABILIZACAO.docx
- **Modificado:** 2026-03-23
- **Tamanho:** 97 KB

---

THOMSON REUTERS

 TAX PAYMENTS –  IMPORTAÇÃO \- SAFX 348 \(Importação de Dados SCANC – Tax Automation\) 

Tax One > Básico > Data Warehouse > Manutenção > Guias de Pagamentos > Parâmetros > Geração

Tax One > Básico > Data Warehouse > Manutenção > Contabilização da Apuração > Parâmetros > Geração

 

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

ADO\- 1008069

Beatriz Tie Terada, Millys Lopes

Definição das regras de importação da SAFX 348

__Introdução __

 

A SAFX 348 irá receber os dados fornecidos pelo sistema Tax Automation, a partir da estrutura dos arquivos \.FDB gerados pelo SCANC da SEFAZ e importados na base do sistema Tax Automation\.

O sistema __Tax Automation__ consumirá esses dados por meio do arquivo FDB, processará as informações e, através da nova SAFX, enviará os resultados ao __Tax One__, onde serão utilizados nos módulos __Guias de Pagamentos__ e __Contabilização da Apuração__\.

O objetivo é consolidar os dados fiscais necessários para o módulo de contabilização, integrando informações das operações monofásicas e não monofásicas presentes nos anexos 3 \(Resumo das operações interestaduais com combustíveis e derivados de petróleo – produtos não monofásicos\) e 3M \(Resumo das operações interestaduais com combustíveis derivados de petróleo – produtos monofásicos\), para alimentar uma tabela interna do sistema Tax Automation\."

 

__ __

__Localização:__ 

- __Módulo__: Básicos > Guias de Pagamentos ou Contabilização da Apuração
- __Menu__: Guias de Pagamentos ou Contabilização da Apuração

 

__\(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX348 conforme o Manual de Layout, o que facilita a consulta\. Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00\)\.__ 

 

__Procedimentos para a Importação da SAFX: __

 __A importação da SAFX deve atender às seguintes premissas de negócio e comportamentos:__

- Os campos obrigatórios e chaves devem estar devidamente preenchidos\.
	- Ao gerar uma contabilização da apuração ou guia de pagamento, sinalizar através dos dois campos
		- ICMS\_DESTINOL
		- ICMS\_RESSARC

__Resultado da Importação:__  
Se a importação for realizada com sucesso, os dados serão registrados nas seguintes telas:

- __Tax One > Básico > Data Warehouse > Manutenção > Guias de Pagamentos > Parâmetros > Geração__
- __Tax One > Básico > Data Warehouse > Manutenção > Contabilização da Apuração > Parâmetros > Geração__

 

__                 __ 

 

 

Regra Geral para validação 

 

1º \) Consistências Básicas: 

 

- Campos Data inválidos 
- Campos Obrigatórios 
- Campos Numéricos inválidos 
- Campo Código da Empresa – Vide regra RN01 
- Campo Código do Estabelecimento – Vide regra RN02
- Campo Período – Vide regra RN03
- Campo CNPJ H – Vide regra RN04
- Campo Código do Produto SCANC – Vide regra RN05
- Campo ID – Vide regra RN06
- Campo Quadro – Vide regra RN07
	- Campo CNPJ – Vide regra RN08
	- Campo Volume – Vide regra RN10 
	- Campo Base de Cálculo do ICMS – Vide regra RN10 
	- Campo ICMS de Origem – Vide regra RN14
	- Campo ICMS de Destino \(Guia Complementar\) – Vide regra RN15
	- Campo ICMS de Destino \(Ressarcimento\) – Vide regra RN16
	- Campo ICMS Complementar – Vide regra RN17

 

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS__

RN00

 

__Índice__ 

__Nome do Campo__ 

__Descrição__ 

__Tipo__ 

__Tam\.__ 

__Obrig\.__ 

__Chave__ 

1 

COD\_EMPRESA  

Código da empresa conforme o cadastro de estabelecimento elegíveis

A 

003 

SIM 

\(\*\) 

2 

COD\_ESTABELECIMENTO  

Código do estabelecimento conforme o cadastro de estabelecimento elegíveis

A 

006 

SIM 

\(\*\) 

3 

PERIODO  

Informar  data do Período de apuração 

N 

006

SIM 

\(\*\) 

4 

CNPJ\_H

Informar o CNPJ do Declarante \(Estabelecimento\)

A 

014 

SIM 

NÃO

5 

COD\_PRODUTO\_SCANC

Informar o Código do Produto relacionado ou derivado de petróleo e diesel

A 

008

SIM 

\(\*\) 

6 

ID

Informar o Código de Identificação do Registro

A 

006

SIM 

NÃO 

7 

QUADRO

Informar o Número do Quadro referente à Operação

A 

004

SIM 

NÃO 

8 

CNPJ

Informar o CNPJ do Participante \(cliente\)

A 

014 

SIM 

NÃO

9 

PROPORCAO

Informar a quantidade \(volume\) do produto, Vide RN10

N 

015V002

NÃO 

NÃO 

10 

VOLUME

Informar a quantidade \(volume\) do produto\. Vide RN09

N 

015V002

SIM 

NÃO 

11 

UNITARIO

Informar o Valor Unitário do Produto

N 

015V002

NÃO 

NÃO 

12 

BASE\_CALCULO\_ICMS

Este campo é destinado a Base de Cálculo do ICMS

N 

015V002

SIM 

NÃO 

13 

ALIQUOTA

Informar o Percentual de Alíquota referente ao ICMS

N 

015V002

NÃO 

NÃO 

14 

ICMS\_ORIGEM

Informar o valor do ICMS na Origem 

N 

015V002

SIM 

NÃO 

15 

ICMS\_DESTINO

Campo destinado a informar o valor do ICMS no destino quando for necessário gerar a API para integração com o sistema DOOTAX\.

N 

015V002

SIM 

NÃO 

16

ICMS\_RESSARC

Campo destinado a informar o valor do ICMS quando for necessário realizar a contabilização para envio ao SAP

N 

015V002

SIM 

NÃO 

17

ICMS\_COMPL

Valor de complemento ou ressarcimento do ICMS\-ST \- Calcular: ICMS Destino \- ICMS Origem\. Não gravar valores negativos\. 

N 

015V002

SIM 

NÃO 

18

UF

Informar a Unidade Federativa \(Estado\)

A 

002

SIM 

NÃO 

19

ICMS\_ST\_TIPO

Informar o tipo de ICMS\-ST, sendo eles Complementar ou Ressarcimento \(classificação\)

A 

014

SIM 

NÃO 

20

TIPO\_OPERACAO

Informar o tipo de operação com base no seguinte preenchimento: 1 – Contabilização e 2 – Guia de Pagamento  

N 

002

SIM 

NÃO 

21

DATA\_HORA\_CRIACAO

Informar preenchimento com a data que o registro foi carregado do arquivo FDB para a base do Tax Automation\.

N 

012

NÃO 

NÃO 

22

DATA\_HORA\_ATUALIZACAO

Informar o preenchimento com a data que o registro foi atualizado, somente nos casos que houver reprocessamento de leitura do arquivo FDB para a base do Tax Automation\.

N 

012

NÃO 

NÃO 

23

USUARIO

Conforme a leitura do arquivo FDB nas máquinas, informar o usuário da máquina de  origem\. 

A 

014

SIM 

NÃO 

24

NRO\_DOC\_CONTABIL

Informa o Número do Documento Contábil criado no SAP 

N

010

SIM

NÃO

ADO\- 1008069

RN00\.1

__Campos Obrigatório não preenchido__

Se algum campo de preenchimento obrigatório não estiver preenchido, exibir a mensagem “Campo <<Nome do campo>> deve ser preenchido”

ADO\- 1008069

__RN01__

__Campo 01 – Código da empresa__

 

__Tabela: __SAFX348

__Item: __01

__Nome do Campo: __COD\_EMPRESA

__Descrição: __Código da empresa conforme o cadastro de estabelecimento elegíveis__ __

__Tipo:__ A

__Tamanho: __003

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informar o Código da empresa conforme o cadastro de estabelecimento elegíveis__ __

Exibir a mensagem da TFIX 22 CÓDIGO 90001

ADO\- 1008069

__RN02__

__Campo 02 – Código do estabelecimento__

__Tabela: __SAFX348

__Item: __02

__Nome do Campo: __COD\_ESTABELECIMENTO

__Descrição: __Código do estabelecimento conforme o cadastro de estabelecimento elegíveis__ __

__Tipo:__ A

__Tamanho: __006__ __

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informar o Código do estabelecimento conforme o cadastro de estabelecimento elegíveis__ __

Exibir a mensagem da TFIX 22 CÓDIGO 90002

ADO\- 1008069

__RN03__

__Campo 03 – Período__

__Tabela: __SAFX348

__Item: __03

__Nome do Campo:__ PERIODO

__Descrição: __Período conforme o cadastro de estabelecimento elegível

__Tipo: N__

__Tamanho:__ 006

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informar o Período conforme  o cadastro de estabelecimento elegível

Exibir a mensagem da TFIX 22 CÓDIGO 913342

ADO\- 1008069

__RN04__

__Campo 04 – CNPJ do Declarante__

 

__Tabela: __SAFX348

__Item: __04

__Nome do Campo: __CNPJ\_H

__Descrição: __CNPJ do Declarante \(Estabelecimento\)

__Tipo:__ A

__Tamanho: __014

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informar o CNPJ do Declarante \(Estabelecimento\)

Exibir a mensagem da TFIX 22 CÓDIGO 913343

ADO\- 1008069

__RN05__

__Campo 05 – Código do produto \(SCANC\)__

 

__Tabela: __SAFX348

__Item: __05

__Nome do Campo: __COD\_PRODUTO\_SCANC

__Descrição: __Código da empresa

__Tipo:__ A

__Tamanho: __008

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informa o Código do Produto relacionado ou derivado de petróleo e diesel 

Exibir a mensagem da TFIX 22 CÓDIGO 913344

ADO\- 1008069

__RN06__

__Campo 06 – Identificação__

__Tabela: __SAFX348

__Item: __06

__Nome do Campo: __ID

__Descrição: __Código de Identificação do Registro

__Tipo:__ A

__Tamanho:__ 006

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informar o Código de Identificação do Registro

Exibir a mensagem da TFIX 22 CÓDIGO 913345

ADO\- 1008069

__RN07__

__Campo 07 – Quadro__

__Tabela: __SAFX348

__Item: __07

__Nome do Campo:__ QUADRO

__Descrição:__ Número do Quadro referente à Operação

__Tipo: A__

__Tamanho:__ 004

__Campo Obrigatório__

__Comentário:__

Informar o Número do Quadro referente à Operação

Exibir a mensagem da TFIX 22 CÓDIGO 913346

ADO\- 1008069

__RN08__

__Campo 08 – CNPJ__

__Tabela:__ SAFX348

__Item:__ 08

__Nome do Campo:__ CNPJ

__Descrição:__ CNPJ do Participante \(Cliente\)

__Tipo: A__

__Tamanho: __014

__Campo Obrigatório__

__Comentário:__

Informar o CNPJ do Participante \(Cliente\)

Exibir a mensagem da TFIX 22 CÓDIGO 913347

ADO\- 1008069

__RN09__

__Campo 09 – Proporção__

__Tabela:__ SAFX348

__Item:__ 09

__Nome do Campo:__ PROPORCAO

__Descrição: __Informar a quantidade \(volume\) do produto\. Vide RN10

__Tipo:__ N

__Tamanho: __015V002

__Campo Não Obrigatório__

__Comentário:__

Informar a quantidade \(volume\) do produto\. Vide RN10\. Este campo depende do campo VOLUME

ADO\- 1008069

__RN10__

__Campo 10 – Volume__

__Tabela: __SAFX348

__Item: 10__

__Nome do Campo:__ VOLUME

__Descrição:__ Informar a quantidade \(volume\) do produto\. Vide RN09

__Tipo: N__

__Tamanho:__ 015V002

__Campo Obrigatório__

__Comentário:__

Informar a quantidade \(volume\) do produto\. Vide RN09\. Este campo depende do campo PROPORCAO

Exibir a mensagem da TFIX 22 CÓDIGO 913348

ADO\- 1008069

__RN11__

__Campo 11 – Unitário__

__Tabela: __SAFX348

__Item: __111

__Nome do Campo:__ UNITARIO

__Descrição: __Valor Unitário do Produto 

__Tipo:__ N

__Tamanho: __015V002

__Campo Não Obrigatório__

__Comentário:__

Informar o Valor Unitário do Produto 

ADO\- 1008069

__RN12__

__Campo 12 – Base de Cálculo do ICMS__

__Tabela: __SAFX348

__Item: __12

__Nome do Campo:__ BASE\_CALCULO\_ICMS

__Descrição: __

Este campo é destinado a Base de Cálculo do ICMS

__Tipo: N__

__Tamanho:__ 015V002

__Campo Obrigatório__

__Comentário:__

Este campo é destinado a Base de Cálculo do ICMS

Exibir a mensagem da TFIX 22 CÓDIGO 913349

ADO\- 1008069

__RN13__

__Campo 13 – Alíquota__

__Tabela: __SAFX348

__Item: __13

__Nome do Campo:__ ALIQUOTA__ __

__Descrição: __Percentual de Alíquota referente ao ICMS 

__Tipo: N__

__Tamanho:__ 015V002

__Campo Não Obrigatório__

__Comentário:__

Informar o Percentual de Alíquota referente ao ICMS 

ADO\- 1008069

__RN14__

__Campo 14 – ICMS de Origem __

__Tabela: __SAFX348

__Item: 14__

__Nome do Campo:__ ICMS\_ORIGEM

__Descrição: __Valor do ICMS na Origem

__Tipo:__ N

__Tamanho:__ 015V002

__Campo Obrigatório__

__Comentário:__

Informa o Valor do ICMS na Origem

Exibir a mensagem da TFIX 22 CÓDIGO 913350

ADO\- 1008069

__RN15__

__Campo 15 – ICMS no Destino __

__Tabela: __SAFX348

__Item: 15__

__Nome do Campo:__ ICMS\_DESTINO

__Descrição: __Campo destinado a informar o valor do ICMS no destino quando for necessário gerar a API para integração com o sistema DOOTAX\.

__Tipo:__ N

__Tamanho:__ 015V002

__Campo Obrigatório__

__Comentário:__

Quando preenchido, indica que será necessário gerar uma guia de pagamento por meio do envio de JSON para o sistema DOOTAX\.

Exibir a mensagem da TFIX 22 CÓDIGO 913351

ADO\- 1008069

__RN16__

__Campo 16 – ICMS Ressarcimento__

__Tabela: __SAFX348

__Item: 16__

__Nome do Campo:__ ICMS\_RESSARC

__Descrição:__ Campo destinado a informar o valor do ICMS no destino quando for necessário realizar a contabilização\.

__Tipo:__ N

__Tamanho:__ 015V002

__Campo Obrigatório__

__Comentário:__

Utilizado para registros de ressarcimento, permitindo provisionar os valores na contabilidade e realizar o envio do JSON para SAP\.

Exibir a mensagem da TFIX 22 CÓDIGO 913352

ADO\- 1008069

__RN17__

__Campo 17 – ICMS Complementar__

__Tabela: __SAFX348

__Item: 17__

__Nome do Campo:__ ICMS\_COMPL

__Descrição: __Valor de complemento ou ressarcimento do ICMS\-ST \- Calcular: ICMS Destino \- ICMS Origem\. Não gravar valores negativos\. 

__Tipo:__ N

__Tamanho:__ 015V002

__Campo Obrigatório__

__Comentário:__

Informar o valor de complemento ou ressarcimento do ICMS\-ST \- Calcular: ICMS Destino \- ICMS Origem\. Não gravar valores negativos\.

Exibir a mensagem da TFIX 22 CÓDIGO 913353

ADO\- 1008069

__RN18__

__Campo 18 – Unidade Federativa__

__Tabela: __SAFX348

__Item: 18__

__Nome do Campo:__ UF

__Descrição: __Unidade Federativa \(Estado\)

__Tipo:__ A

__Tamanho: __002

__Campo Obrigatório__

__Comentário:__

Informar a Unidade Federativa \(Estado\)

Exibir a mensagem da TFIX 22 CÓDIGO 913354

ADO\- 1008069

__RN19__

__Campo 19 – Tipo de ICMS\-ST__

__Tabela: __SAFX348

__Item: 19__

__Nome do Campo:__ ICMS\_ST\_TIPO

__Descrição: __Informar o tipo de ICMS\-ST, sendo eles Complementar ou Ressarcimento \(classificação\)

__Tipo:__ A

__Tamanho: __014

__Campo Obrigatório__ 

__Comentário:__

Informar o tipo de ICMS\-ST, sendo eles Complementar ou Ressarcimento \(classificação\)

Exibir a mensagem da TFIX 22 CÓDIGO 913355

ADO\- 1008069

__RN20__

__Campo 20 – Tipo de Operação__

__Tabela: __SAFX348

__Item: 20__

__Nome do Campo:__ TIPO\_OPERACAO

__Descrição: __Informar o tipo de operação com base no seguinte preenchimento: 1 – Contabilização e 2 – Guia de Pagamento  

__Tipo:__ N

__Tamanho: 002__

__Campo Obrigatório__

__Comentário: __

Informar o tipo de operação com base no seguinte preenchimento: 1 – Contabilização e 2 – Guia de Pagamento  

Exibir a mensagem da TFIX 22 CÓDIGO 913356

ADO\- 1008069

__RN21__

__Campo 21 – Data e Hora de Criação__

__Tabela: __SAFX348

__Item: 21__

__Nome do Campo:__ DATA\_HORA\_CRIACAO

__Descrição: __Data que o registro foi carregado do arquivo FDB para a base do Tax Automation\.

__Tipo:__ N

__Tamanho: 012__

__Campo Não Obrigatório__

__Comentário:__

Informar preenchimento com a data que o registro foi carregado do arquivo FDB para a base do Tax Automation\.

Utilizar formato DD/MM/AAAA – HH:MM

ADO\- 1008069

__RN22__

__Campo 22 – Data e Hora de Atualização__

__Tabela: __SAFX348

__Item: 22__

__Nome do Campo:__ DATA\_HORA\_ATUALIZACAO

__Descrição: __Data que o registro foi atualizado

__Tipo:__ N

__Tamanho: 012__

__Campo Não Obrigatório__

__Comentário:__

Informar o preenchimento com a data que o registro foi atualizado, somente nos casos que houver reprocessamento de leitura do arquivo FDB para a base do Tax Automation\.

ADO\- 1008069

__RN23__

__Campo 23 – Usuário__

__Tabela: __SAFX348

__Item: 23__

__Nome do Campo:__ USUARIO

__Descrição: __Conforme a leitura do arquivo FDB nas máquinas, informar o usuário da máquina de  origem\. 

__Tipo:__ A

__Tamanho: __015V002

__Campo Não Obrigatório__

__Comentário:__

Conforme a leitura do arquivo FDB nas máquinas, informar o usuário da máquina de  origem\. 

Exibir a mensagem da TFIX 22 CÓDIGO 913357

Utilizar formato DD/MM/AAAA – HH:MM

ADO\- 1008069

__RN24__

__Campo 24 – Número do Documento Contábil__

__Tabela: SAFX 348__

__Item: 24__

__Nome do Campo:__ NRO\_DOC\_CONTABIL

__Descrição: __Informa o Número do Documento Contábil criado no SAP\. __ __

__Tipo:__ N

__Tamanho: 010__

__Campo Obrigatório__ 

__Comentário:__ 

Informa o Número do Documento Contábil criado no SAP\.  

Exibir a mensagem da TFIX 22 CÓDIGO 913358

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

