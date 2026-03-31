# MTZ_Geracao_MM_AC_ICMS_52_15

- **Fonte:** MTZ_Geracao_MM_AC_ICMS_52_15.docx
- **Modificado:** 2026-03-24
- **Tamanho:** 107 KB

---

__THOMSON REUTERS__

__Geração do Meio Magnético AC ICMS 52/15__

__Módulo Arquivo de Injeção de Energia Elétrica __

Localização: Módulo Estadual >> Arquivo de Injeção de Energia Elétrica

Menu: Obrigações >> Ato Cotepe ICMS 52/2015 >> Geração do Meio Magnético

Quadro de Revisões

__                         __

__Data__

__OS / Chamado__

__Descrição__

__Responsável__

01/03/2026

MFS981991

Criação da geração do meio magnético, com os  Arquivos de Créditos e Compensação, para atendimento ao Ato Cotepe ICMS 52/15

Liliane Assaf

09/03/2026

MFS987271

Inclusão da geração dos Arquivos de Unidades e Identificação para atendimento ao Ato Cotepe ICMS 52/15

Liliane Assaf

[1\.	Introdução	1](#_Toc223287706)

[2\.	Base Legal:	1](#_Toc223287707)

[3\.	Pré\-Requisitos:	1](#_Toc223287708)

[4\.	Parâmetros de Tela	1](#_Toc223287709)

[5\.	Regras de Negócio	1](#_Toc223287710)

[RN01 – Regra de Montagem do nome dos Arquivos	1](#_Toc223287711)

[RN02 – Regra de Formatação dos campos nos Arquivos	1](#_Toc223287712)

[RN03 \- Geração do Arquivo de Identificação do Contribuinte	1](#_Toc223287713)

[RN04 \- Geração do Arquivo de Unidades Injetoras e Consumidoras	1](#_Toc223287714)

[RN05 \- Geração do Arquivo de Créditos	1](#_Toc223287715)

[RN06 \- Geração do Anexo de Compensações	1](#_Toc223287716)

# <a id="_Toc223287706"></a>Introdução 

Essa funcionalidade permite a geração do Meio Magnético para atendimento ao Ato Cotepe ICMS 52/15\.

# <a id="_Toc223287707"></a>Base Legal:

ATO COTEPE/ICMS 52, DE 25 DE NOVEMBRO DE 2015

# <a id="_Toc223287708"></a>Pré\-Requisitos:

1. Importação da Capa de Documento Fiscal de Utilities \(SAFX42\) com os dados de Injeção de Energia Elétrica necessários para geração do Arquivo de Unidades do Ato Cotepe ICMS 52/15\.

03\-DAT\_FISCAL

06\-NUM\_DOCFIS

07\-SERIE\_DOCFIS

67\-NUM\_CONTRATO

111\-VLR\_ENERGIA\_INJ

169\-VLR\_BC\_ICMS\_INJ

170\-VLR\_ICMS\_INJ

171\-VLR\_ALIQ\_ICMS\_INJ

27\-VLR\_ALIQ\_ICMS

74\-QTD\_CONSUMO\_TOTAL

COD\_MODELO

110\-QTD\_ENERGIA\_INJ

1. Importação do Item de Documento Fiscal de Utilities \(SAFX43\) com os dados de Injeção de Energia Elétrica necessários para geração do Arquivo de Unidades do Ato Cotepe ICMS 52/15\.

165\-QTD\_ENERGIA\_COMP

120\-VLR\_ENERGIA\_COMP

1. Importação da SAFX433 \(Controle de Crédito de Injeção de Energia Elétrica\) necessário para geração do Arquivo de Créditos do Ato Cotepe ICMS 52/15\.
2. Importação da SAFX434 \(Controle de Compensação de Injeção de Energia Elétrica\) necessário para geração do Arquivo de Compensação do Ato Cotepe ICMS 52/15\.
3. Incluir as Unidades Injetoras e Consumidoras no Cadastro de Pessoa Física/Jurídica \(SAFX04\) com os dados de Injeção de Energia Elétrica necessários para geração do Arquivo de Unidades do Ato Cotepe ICMS 52/15:

05\-RAZAO\_SOCIAL

06\-CPF\_CGC

08\-INSC\_ESTADUAL

12\-ENDERECO

13\-NUM\_ENDERECO

14\-COMPL\_ENDERECO

15\-BAIRRO

19\-UF

25\-COD\_MUNICIPIO

20\-CEP

42\-TP\_LOGRADOURO

94\-IND\_TP\_UNID\_EE

95\-COD\_GRP\_TITULAR\_EEE

96\-NUM\_ORD\_COMP\_EE

97\-DAT\_REF\_ENT\_EE

98\-DAT\_REF\_SAI\_EE

1. Cadastrar um Responsável pela Informação no Módulo Parâmetros, menu Requisitos Legais 🡪 Responsável por Informações\.
2. Cadastrar Inscrição Estadual do Estabelecimento para sua UF de domicílio, no módulo Parâmetros, menu Preliminares >> Inscrições Estaduais\.

# <a id="_Toc223287709"></a>Parâmetros de Tela

Mês/Ano Referência da Apuração:                 \[ dd/aaaa \]

Arquivos:

\[ \] Arquivo de Identificação do Contribuinte

\[ \] Arquivo de Unidades Injetoras e Consumidoras

\[ \] Arquivo de Créditos

\[ \] Arquivo de Compensações

Status:  \(o\) Normal

             \( \) Substituto  

Versão: \[01\]

Responsável \[                                \\/\]

  

Geração p/ Inscrição Estadual Única: \(o\) Sim

                                                             \( \) Não     

 

UF: \[ \*Todas \*                              \\/\]

Estabelecimentos:     \[ \] Selecionar \[ \] Marcar Todos

 \[ x \] xx \- xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx      

 \[ y \] xx \- xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx      

 \[    \] xx \- xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Funcionamento dos campos:

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/__

__Default__

__Regra__

<a id="_Hlk517437550"></a>Mês/Ano Referência da Apuração

Data

\(mês e ano\)

S

S

\(MM/AAAA\)

Neste campo o usuário informa o período \(mês e ano\) para a geração do arquivo\.

Deve ser um mês válido\.

Default: Apresentar o mês/ano anterior ao mês/ano do dia da execução\.

Crítica

Se o período não for informado exibir mensagem de erro:

    Informe o Mês/Ano Referência da Apuração

__Arquivos__

Arquivo de Identificação do Contribuinte

Check\-box

N

S

Default Desmarcado

Manter esse campo bloqueado para edição pois não faz parte do escopo da MFS981991

MFS987271: habilitar o check\-box\.

Arquivo de Unidades Injetoras e Consumidoras

Check\-box

N

S

Default Desmarcado

Manter esse campo bloqueado para edição pois não faz parte do escopo da MFS981991

MFS987271: habilitar o check\-box\.

Arquivo de Créditos

Check\-box

N

S

Default Desmarcado

Arquivo de Compensações

Check\-box

N

S

Default Desmarcado

Pelo menos um dos arquivos deve estar selecionado para geração\. Caso nenhum esteja marcado, exibir mensagem de erro:

  Selecione pelo menos um arquivo para geração\.

Status

Radio button

S

S

Default N \- Normal

Opções para status do arquivo: 'N' \- normal ou 'S' – substituto;

Versão

Texto

S

S

Default ‘01’

Default: Apresentar como default o valor ‘01’\.

Se Status = N – Normal, então:

    Preencher o campo Versão com ‘01’ e desabilitar campo\.

Se Status = S– Substituto, então:

    Habilitar o campo Versão\.

Crítica

Se o Versão não for informado exibir mensagem de erro:

    Informe a Versão para geração dos arquivos

Responsável

Lista

N

S

MFS987271

Este campo é uma lista dos responsáveis legais \(Módulo Parâmetros, menu Requisitos Legais 🡪 Responsável por Informações\)\.

Geração por Inscrição Estadual Única

Radio button

S

N

Default:

 opção “Sim”

Opção que permite o usuário escolher se a geração será feita por inscrição estadual única\.

UF \(Estabelecimento\)

Lista

S

S

Default “Todos”

Este campo é composto pelos códigos de Unidades Federativas oriundas da tabela Estado\. Adicionar à lista o item “__Todos__”\.

Servirá para filtro dos estabelecimentos apresentados para seleção\.

Estabelecimentos

Multi\-seleção

S

S

Neste campo é exibida a lista dos estabelecimentos da Empresa do login\.

Apresentar os estabelecimentos de acordo com a UF selecionada em “Pesquisa UF \(Estabelecimento\)” e a opção escolhida para Geração por Inscrição Estadual Única\.

Se parâmetro “Geração por Inscrição Estadual Única” = “Sim”

     Serão disponibilizados para seleção apenas os estabelecimentos que sejam 

     __centralizadores__ e os __descentralizados__, de acordo com a parametrização de

     I\.E\.U\. do módulo de controle das obrigações estaduais, e cuja UF do 

     Estabelecimento seja a escolhida em tela\.

Senão 

     Serão disponibilizados para seleção todos os estabelecimentos cuja UF  

     do estabelecimento seja a escolhida em tela\.

Selecionar

N

N

Esta opção é um facilitador que permite ao usuário selecionar um ou mais estabelecimentos através de uma janela de seleção da tabela de estabelecimentos\.

O filtro dos estabelecimentos disponibilizados para seleção segue a mesma regra descrita para o campo “Estabelecimento”\.

Quando esta opção é utilizada, após escolher os estabelecimentos e clicar no botão <OK> da janela de seleção, os estabelecimentos selecionados pelo usuário serão demonstrados no campo “Estabelecimentos” já marcados\. 

   

Marcar todos

N

N

Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados no campo “Estabelecimentos”\.

# <a id="_Toc223287710"></a>Regras de Negócio

## <a id="_Toc223287711"></a>__RN01 – Regra de Montagem do nome dos Arquivos__

O nome do arquivo deve ser montado no seguinte formato:

SCEE\_CCCCCCCCCCCCCC\_AAAAMM\_TStVV\.TXT

__Onde:__

- SCEE: Valor constante, referente ao Sistema de Compensação de Energia Elétrica\.
- CCCCCCCCCCCCCC: 14 algarismos do CNPJ do estabelecimento selecionado para geração, sem formatação\.
- AAAA: Ano da referência de apuração informado em tela \(campo Mês/Ano Referência da Apuração\)
- MM: Mês da referência de apuração informado em tela \(campo Mês/Ano Referência da Apuração\)
- T: Tipo do arquivo: 
	- “I” para Arquivo de identificação do Contribuinte
	- “U” para Arquivo de Unidades Injetoras e Consumidoras,
	- "E" para Arquivo de Créditos
	- "C" para Arquivo de Compensações
- St: Status do arquivo informado em tela:
	- "N" para arquivo normal
	- "S" para arquivo substituto
- VV: Versão do arquivo informado em tela\.
- \.TXT: Extensão do arquivo \(sempre "TXT"\)\.

__Exemplo:__

- Arquivo de Créditos, CNPJ 12345678000199, referência junho/2024, arquivo normal, primeira versão: 

SCEE\_12345678000199\_202406\_EN01\.TXT

- Arquivo de Compensação, CNPJ 12345678000199, referência junho/2024, arquivo substituto, segunda versão: 

SCEE\_12345678000199\_202406\_CS02\.TXT

## <a id="_Toc223287712"></a>__RN02 – Regra de Formatação dos campos nos Arquivos__

Ao acionar a geração, realizar as validações abaixo e prosseguir com a geração dos anexos\.

Os campos dos arquivos devem ser formatados conforme abaixo:

- __Numérico \(N\):__
	- Sem sinal, inteiro, apenas algarismos\.
	- Alinhado à direita\.
	- Posições não\-significativas preenchidas com zeros\.
- __Valor \(V\):__
	- Sem sinal, com a quantidade de casas decimais especificada\.
	- Apenas algarismos\.
	- Posições não\-significativas preenchidas com zeros\.
	- Sem ponto decimal e sem separador de milhar\.
- __Data \(D\):__
	- Somente algarismos\.
	- Formato: AAAAMMDD \(ano\-mês\-dia\)\.
- __Alfanumérico \(X\):__
	- Letras, números e caracteres especiais válidos\.
	- Alinhado à esquerda\.
	- Posições não\-significativas preenchidas com espaços em branco\.
	- Não pode conter caracteres não\-imprimíveis \(ASCII 00 a 31\), inclusive CR e LF\.

## <a id="_Toc223287713"></a>__RN03 \- Geração do Arquivo de Identificação do Contribuinte__

MFS987271

Gerar um arquivo para cada Estabelecimento selecionado na tela de Geração, contendo apenas 1 registro referente ao estabelecimento selecionado\.

O arquivo conterá dados do estabelecimento informante, totalizações das unidades e da energia injetada/compensada, com base nos dados do cadastro de Estabelecimento \(SAFX2064\) e nas informações das notas fiscais \(SAFX42/SAFX43\)\.

__Origem dos dados__: \- Tabela de Estabelecimento \(SAFX2064\);

__Critérios da recuperação: __

\- Empresa – código da empresa do login;

\- Estabelecimento = código do estabelecimento selecionado para geração;

__Regra de Processamento:__

1\) Só pode existir um registro no arquivo\.

2\) Aplicar a mesma a regra leitura das tabelas SAFX42, SAFX43 utilizada na geração do Arquivo de Unidades – vide [RN04](#_RN04_-_Geração), para totalização dos documentos fiscais e gravação dos campos 14 ao 20 do Arquivo de Identificação\. 

3\) Gravar o Arquivo de Identificação com as seguintes informações:

__Nº__

__Conteúdo__

__Tamanho__

__Posição Inicial__

__Posição Final__

__Formato__

__Regra de Preenchimento__

01

Referência de Apuração \(AAMM\)

4

1

4

N

Preencher com AAMM do Mês/Ano Referência da Apuração informado em tela\.

02

CNPJ

14

5

18

N

Preencher com campo 05\-CGC do ESTABELECIMENTO \(SAFX2064\)

03

IE

14

19

32

X

Preencher com a Inscrição Estadual do Estabelecimento cadastrada para a UF do Estabelecimento, no módulo Parâmetros, menu Preliminares >> Inscrições Estaduais \(tabela de REGISTRO\_ESTADUAL\)

04

Razão Social

50

33

82

X

Preencher com campo ESTABELECIMENTO \(SAFX2064\) – 09\-RAZAO\_SOCIAL

05

Endereço

50

83

132

X

Preencher com a concatenação dos campos 26\-TP\_LOGRADOURO \+ 11\-ENDERECO \+ 12\-NUM\_ENDERECO \+ 13\-COMPL\_ENDERECO do ESTABELECIMENTO \(SAFX2064\)

06

CEP

9

133

141

X

Preencher com campo 19\-CEP do ESTABELECIMENTO \(SAFX2064\), __com formatação 99999\-999__\.

07

Bairro

30

142

171

X

Preencher com campo 14\-BAIRRO do ESTABELECIMENTO \(SAFX2064\) 

08

Município

30

172

201

X

Código do Município da tabela IBGE\.

__Regra p/ Montagem do Código Município IBGE:__

Preencher com a concatenação do campo COD\_UF da tabela MUNICIPIO \+ campo 23\-COD\_MUNICIPIO do ESTABELECIMENTO \(SAFX2064\) \(para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\)\.

Para recuperar o COD\_UF da tabela MUNICIPIO considerar os campos 18\-COD\_ESTADO e 23\-COD\_MUNICIPIO do ESTABELECIMENTO \(SAFX2064\)\.

09

UF

2

202

203

X

Preencher com campo 18\-COD\_ESTADO do ESTABELECIMENTO \(SAFX2064\)

10

Responsável pela apresentação

30

204

233

X

Preencher com o Nome/Razão Social do Responsável pela Informação que foi selecionado na Tela de Geração \(Tabela RESP\_INFORMACAO – módulo Parâmetros, menu Requisitos Legais 🡪 Responsável por Informações\)\.

11

Cargo

20

234

253

X

Preencher com o Cargo do Responsável pela Informação que foi selecionado na Tela de Geração \(Tabela RESP\_INFORMACAO – módulo Parâmetros, menu Requisitos Legais 🡪 Responsável por Informações\)\.

12

Telefone

12

254

265

X

Preencher com DDD\+TELEFONE do Responsável pela Informação que foi selecionado na Tela de Geração \(Tabela RESP\_INFORMACAO – módulo Parâmetros, menu Requisitos Legais 🡪 Responsável por Informações\)\.

13

e\-Mail

40

266

305

X

Preencher com o e\-mail do Responsável pela Informação que foi selecionado na Tela de Geração \(Tabela RESP\_INFORMACAO – módulo Parâmetros, menu Requisitos Legais 🡪 Responsável por Informações\)\.

14

Qtde\. Total de Unidades \(Consumidoras \+ Injetoras\)

9

306

314

N

Contabilizar os distintos 67\-NUM\_CONTRATO da SAFX42, recuperados conforme [RN04](#_RN04_-_Geração) regra utilizada na geração do Arquivo de Unidades\.

15

Qtde\. de Unidades Injetoras

9

315

323

N

Contabilizar os distintos 67\-NUM\_CONTRATO da SAFX42, recuperados conforme [RN04](#_RN04_-_Geração) regra utilizada na geração do Arquivo de Unidades, cujo campo 94\-IND\_TP\_UNID\_EE da SAFX04 seja igual a "I"\-Injetora\.

16

Qtde\. de energia injetada \(kWh\) \(c/ 3 decimais\)

15

324

338

V

Somatório do campo 110\-QTD\_ENERGIA\_INJ da SAFX42, recuperados conforme [RN04](#_RN04_-_Geração) regra utilizada na geração do Arquivo de Unidades\.

17

Valor Total \(com 2 decimais\)

15

339

353

V

Somatório do campo 111\-VLR\_ENERGIA\_INJ da SAFX42, recuperados conforme [RN04](#_RN04_-_Geração) regra utilizada na geração do Arquivo de Unidades\.

18

BC ICMS \(com 2 decimais\)

15

354

368

V

Somatório do campo 169\-VLR\_BC\_ICMS\_INJ da SAFX42, recuperados conforme [RN04](#_RN04_-_Geração) regra utilizada na geração do Arquivo de Unidades\.

19

ICMS \(com 2 decimais\)

15

369

383

V

Somatório do campo 170\-VLR\_ICMS\_INJ da SAFX42, recuperados conforme [RN04](#_RN04_-_Geração) regra utilizada na geração do Arquivo de Unidades\.

20

Qtde\. de energia compensada \(kWh\) \(c/ 3 dec\.\)

15

384

398

V

Somatório do campo 165\-QTD\_ENERGIA\_COMP da SAFX43, recuperados conforme [RN04](#_RN04_-_Geração) regra utilizada na geração do Arquivo de Unidades\.

## <a id="_RN04_-_Geração"></a><a id="_Toc223287714"></a>__RN04 \- Geração do Arquivo de Unidades Injetoras e Consumidoras__

MFS987271

Gerar um arquivo para cada Estabelecimento selecionado na tela de Geração contendo as notas fiscais de Utilities do período\.

__Origem dos dados__: \- Tabela de Capa do Documento Fiscal de Utilities \(SAFX42\);

                                   Tabela de Item do Documento Fiscal de Utilities \(SAFX43\);

                                   Tabela de Cadastro da Pessoa Física Jurídica \(SAFX04\);

__Critérios da recuperação: __

\- Empresa – código da empresa do login;

\- Estabelecimento:

   Se parâmetro “*Geração por Inscrição Estadual Única*” = marcado

         Estabelecimento = código do estabelecimento selecionado para geração \(centralizador\), __e__, código dos estabelecimentos centralizados;

         \(conforme a parametrização de I\.E\.U\. do módulo de controle das obrigações estaduais\)

   Senão

         Estabelecimento = código do estabelecimento selecionado para geração;

\- Data Fiscal \(item 03\- DAT\_FISCAL da SAFX42\) – compreendida no Mês/Ano Referência da Apuração informado em tela;

\- Modelo de Documento \(item 13\-COD\_MODELO da SAFX42\) = 06 e 66

\- Situação da Nota \(item 21\-SITUACAO da SAFX42\) diferente de ‘S’ \- Nota Fiscal regularmente cancelada;

\- Número do Contrato/Unidade de Consumo \(item 67\- NUM\_CONTRATO da SAFX42\) preenchido\.

Para cada capa de nota fiscal recuperada \(SAFX42\) e buscar os registros de __Créditos__ na Tabela Controle de Crédito de Injeção de Energia Elétrica \(__SAFX433__\), __caso exista__, considerando os campos abaixo para correlação entre as duas tabelas:

\- Código da Empresa \(item 01 – COD\_EMPRESA da SAFX433\)  = COD\_EMPRESA da SAFX42

\- Código do Estabelecimento \(item 02\-COD\_ESTAB da SAFX433\) = COD\_ESTAB da SAFX42

\- Período de Referência da Apuração \(item 03\-DAT\_APURACAO da SAFX433\) compreendida no Mês/Ano Referência da Apuração informado em tela

\- Número da Instalação da Unidade Injetora \(item 04\- NUM\_INSTAL\_INJ da SAFX433\) = Número do Contrato/Unidade de Consumo \(item 67\- NUM\_CONTRATO da SAFX42\)\.

Caso não seja encontrado registro de __Crédito__ na Tabela Controle de Crédito de Injeção de Energia Elétrica \(SAFX433\), e o Tipo de Unidade \(item 94\- IND\_TP\_UNID\_EE da SAFX04\) for igual a “I” – Injetora, exibir mensagem

Arquivo de Unidades:

O Registro de Unidade foi gerado sem preenchimento nos campos 19, 20, 25 e 26, porque não foi encontrado registro de Crédito na Tabela de Controle de Crédito de Injeção de Energia Elétrica \(SAFX433\)\.

Dados do Registro: Núm Instal Unid Injetora/Consumidora: XXXX – Num Doc Fis: YYYYYY – Série Doc Fis: ZZZ – Data Emissão: DD/MM/AAAA

Para cada capa de nota fiscal recuperada \(SAFX42\) gravar um registro no Arquivo de Unidades, totalizando valores dos itens \(SAFX43\) e as quantidades dos registros de __Crédito__ recuperados da Tabela Controle de Crédito de Injeção de Energia Elétrica \(SAFX433\)\.

- Valores dos itens \(SAFX43\) a serem totalizados:

\- Valor da Energia elétrica injetada compensada pelo consumidor \(120\-VLR\_ENERGIA\_COMP da SAFX43\)

\-  Quantidade de Energia Elétrica Compensada em kWh \(item 165\-QTD\_ENERGIA\_COMP da SAFX43\) 

- Valores dos Créditos \(SAFX433\) a serem totalizados:

\- Quantidade Inicial de Energia em kWh \(08\- QTD\_ENERGIA\_INI da SAFX433\)

\- Quantidade de Energia Elétrica Injetada em kWh \(item 09\- QTD\_ENERGIA\_INJ da SAFX433\) 

\- Quantidade de Saída de Energia Elétrica em kWh \(item 10\- QTD\_ENERGIA\_SAI da SAFX433\)

\- Quantidade Final de Energia em kWh \(item 11\- QTD\_ENERGIA\_FIM da SAFX433\)

__Regra de Processamento:__

1\) Os registros devem gravados ordenados por: 

- 
	- Número de Instalação da Unidade Injetora/Consumidora \(Campo 02\)

2\) Só pode existir um registro por Número de Instalação da Unidade Injetora/Consumidora \(Campo 02\)

Caso seja recuperada mais de uma nota fiscal para o mesmo Número de Instalação da Unidade Injetora/Consumidora, exibir mensagem de aviso e prosseguir com a gravação dos registros no arquivo:

Arquivo de Unidades:  
Foi identificado mais de um registro para o mesmo Núm Instal Unid Injetora/Consumidora\.  
Essa duplicidade ocorreu porque foram encontradas mais de uma nota fiscal para a Unidade Injetora/Consumidora\.

Dados do Registro: Núm Instal Unid Injetora/Consumidora: XXXX

3\) Gravar o Arquivo de Unidades com as seguintes informações:

__Nº__

__Conteúdo__

__Tamanho__

__Posição Inicial__

__Posição Final__

__Formato__

__Regra de Preenchimento__

01

Referência de Apuração \(AAMM\)

4

1

4

N

Preencher com AAMM do campo 03\- DAT\_FISCAL da SAFX42

02

Número da Instalação da Unidade Cons\.

12

5

16

X

Preencher com campo 67\-NUM\_CONTRATO da SAFX42

03

Titular Pessoa Física ou Jurídica

1

17

17

X

Preencher com "F" se o campo 06\-CPF\_CGC da SAFX04 tiver 11 posições \(CPF\), ou "J" se tiver 14 posições \(CNPJ\)\. 

04

CPF ou CNPJ \(da Unidade Consumidora\)

14

18

31

N

Preencher com campo 06\-CPF\_CGC da SAFX04 sem formatação\.

Em se tratando de CPF, o número deve ser alinhado à direita, e as 3 primeiras posições devem ser preenchidas com zeros\.

Obs: já considerar CNPJ ALFANUMÉRICO\.

05

IE \(da Unidade Consumidora\)

14

32

45

X

Preencher com campo 08\-INSC\_ESTADUAL da SAFX04\.

06

Nome ou Razão Social \(da Unidade Consumidora\)

35

46

80

X

Preencher com campo 05\-RAZAO\_SOCIAL da SAFX04\.

07

Logradouro \(da Unidade Consumidora\)

45

81

125

X

Preencher com a concatenação dos campos 42\-TP\_LOGRADOURO e 12\-ENDERECO da SAFX04\.

08

Número

5

126

130

N

Preencher com campo 13\-NUM\_ENDERECO da SAFX04

09

Complemento

15

131

145

X

Preencher com campo 14\-COMPL\_ENDERECO da SAFX04

10

CEP \(da Unidade Consumidora\)

8

146

153

N

Preencher com campo 20\-CEP da SAFX04,__ sem formatação__

11

Bairro \(da Unidade Consumidora\)

15

154

168

X

Preencher com campo 15\-BAIRRO da SAFX04

12

Município \(da Unidade Consumidora\)

30

169

198

X

Código do Município da tabela IBGE\.

__Regra p/ Montagem do Código Município IBGE:__

Preencher com a concatenação do campo COD\_UF da tabela MUNICIPIO \+ campo 25\-COD\_MUNICIPIO da SAFX04 \(para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\)\.

Para recuperar o COD\_UF da tabela MUNICIPIO considerar os campos 19\-UF e 25\-COD\_MUNICIPIO da SAFX04\.

13

UF \(da Unidade Consumidora\)

2

199

200

X

Preencher com campo 19\-UF da SAFX04\.

14

Tipo de Unidade \(Injetora ou apenas Consumidora\)

1

201

201

X

Preencher com campo 94\-IND\_TP\_UNID\_EE da SAFX04\.

15

Código do Grupo do Titular

14

202

215

X

Preencher com campo 95\-COD\_GRP\_TITULAR\_EEE da SAFX04\.

16

Ordem de Prioridade de Compensação

7

216

222

N

Preencher com campo 96\-NUM\_ORD\_COMP\_EE da SAFX04\.

17

Referência de Entrada no Sistema de Compensação

4

223

226

N

Preencher com AAMM do campo 97\-DAT\_REF\_ENT\_EE da SAFX04\.

18

Referência de Saída do Sistema de Compensação

4

227

230

N

Se campo 98\-DAT\_REF\_SAI\_EE da SAFX04 estiver preenchido então:

        Preencher com AAMM do campo 98\-DAT\_REF\_SAI\_EE da SAFX04\.

Senão:

        Preencher com AAMM do Mês/Ano Referência da Apuração informado em tela

19

Crédito Inicial do Período \(kWh\) \(c/ 3 decimais\)

15

231

245

V

Preencher com campo 8\-QTD\_ENERGIA\_INI da SAFX433

20

Total de Injeção de Energia \(kWh\) \(c/ 3 decimais\)

13

246

258

V

Preencher com campo 110\-QTD\_ENERGIA\_INJ da SAFX42

21

Valor Total \(R$\) \(com 2 decimais\)

13

259

271

V

Preencher com campo 111\-VLR\_ENERGIA\_INJ da SAFX42

22

BC ICMS \(R$\) \(com 2 decimais\)

13

272

284

V

Preencher com campo 169\-VLR\_BC\_ICMS\_INJ da SAFX42

23

ICMS \(R$\) \(com 2 decimais\)

13

285

297

V

Preencher com campo 170\-VLR\_ICMS\_INJ da SAFX42

24

Alíquota ICMS da Energia Injetada \(%\) \(c/ 2 dec\.\)

4

298

301

V

Preencher com campo 171\-VLR\_ALIQ\_ICMS\_INJ da SAFX42

25

Total de Saídas de Energia \(kWh\) \(c/ 3 dec\.\)

13

302

314

V

Preencher com campo 10\-QTD\_ENERGIA\_SAI da SAFX433\.

26

Crédito Final do Período \(kWh\) \(c/ 3 decimais\)

15

315

329

V

Preencher com campo 11\-QTD\_ENERGIA\_FIM da SAFX433\.

27

Referência de emissão da Nota Fiscal \(AAMM\)

4

330

333

N

Preencher com AAMM do campo 03\- DAT\_FISCAL da SAFX42

28

Modelo da Nota Fiscal

2

334

335

N

Preencher com campo COD\_MODELO da SAFX42

29

Série da Nota Fiscal

3

336

338

X

Preencher com campo 07\-SERIE\_DOCFIS da SAFX42

30

Número da Nota Fiscal

9

339

347

N

Preencher com campo 06\-NUM\_DOCFIS da SAFX42

31

Data de emissão da Nota Fiscal \(AAAAMMDD\)

8

348

355

D

Preencher com campo 03\-DAT\_FISCAL da SAFX42 com formato AAAAMMDD\.

32

Total de Energia Consumida \(kWh\) \(c/ 3 decimais\)

13

356

368

V

Preencher com campo 74\-QTD\_CONSUMO\_TOTAL da SAFX42

33

Alíquota ICMS da Energia Consumida \(%\) \(c/ 2 decimais\)

4

369

372

V

Preencher com campo 27\-VLR\_ALIQ\_ICMS da SAFX42\.

34

Total de Energia Compensada \(kWh\) \(c/ 3 dec\.\)

13

373

385

V

Preencher com campo 165\-QTD\_ENERGIA\_COMP da SAFX43\.

35

Valor Total da Energia Compensada \(R$\) \(c/ 2 decimais\)

13

386

398

V

Preencher com campo 120\-VLR\_ENERGIA\_COMP da SAFX43\.

## <a id="_Toc223287715"></a>__RN05 \- Geração do Arquivo de Créditos __

Gerar um arquivo para cada Estabelecimento selecionado na tela de Geração, considerando os registros da tabela de <a id="_Hlk217932918"></a>Controle de Crédito de Injeção de Energia Elétrica \(SAFX433\)\.

__Origem dos dados__: \- Tabela Controle de Crédito de Injeção de Energia Elétrica \(SAFX433\);

__Critérios da recuperação: __

\- Empresa – código da empresa do login;

\- Estabelecimento:

   Se parâmetro “*Geração por Inscrição Estadual Única*” = marcado

         Estabelecimento = código do estabelecimento selecionado para geração \(centralizador\), __e__, código dos estabelecimentos centralizados;

         \(conforme a parametrização de I\.E\.U\. do módulo de controle das obrigações estaduais\)

   Senão

         Estabelecimento = código do estabelecimento selecionado para geração;

\- Data Apuração – compreendida no Mês/Ano Referência da Apuração informado em tela;

 

__Regra de Processamento:__

1\) Os registros devem gravados ordenados por: 

- 
	- Número de Instalação da Unidade Injetora \(campo 02\)
	- Período de Referência de Injeção \(campo 03\)
	- Posto Tarifário da Energia Injetada \(campo 04\)

2\) Cada registro corresponde a uma __combinação única__ de: 

- 
	- Número de Instalação da Unidade Injetora \(campo 02\)
	- Período de Referência de Injeção \(campo 03\)
	- Posto Tarifário da Energia Injetada \(campo 04\)

Logo se a geração foi feita com o parâmetro “Geração por Inscrição Estadual Única” = marcado, o Arquivo de Créditos é gerado em nome do Estabelecimento __Centralizador__ e os registros lidos devem ser consolidados pelos campos \(Número de Instalação da Unidade Injetora, Período de Referência de Injeção, Posto Tarifário da Energia Injetada e Tarifa da Energia Injetada\), somando os campos de Quantidade\. 

Caso o resultado da consolidação gere mais de um registro para o mesmo Número de Instalação da Unidade Injetora, Período de Referência de Injeção e Posto Tarifário da Energia Injetada, exibir mensagem de aviso e prosseguir com a gravação dos registros no arquivo:

__Arquivo de Crédito__  
Foi identificado mais de um registro para o mesmo Número de Instalação, Período de Referência da Injeção e Posto Tarifário\.  
Essa duplicidade ocorreu porque foi encontrada variação na Tarifa de Energia Injetada entre os estabelecimentos que fazem parte da mesma Inscrição Estadual Única\.

Dados do Registro: Núm Instal Unid Injetora: XXXX Período Ref Injeção e Posto Tarifário da Energia Injetada:AA

3\) Gravar o Arquivo de Créditos com as seguintes informações:

__n\.º__

__Conteúdo__

__Tam__

__Posição Inicial__

__Posição Final__

__Formato__

__Regra de Preenchimento__

01

Referência de Apuração \(AAMM\)

4

1

4

N

Preencher com AAMM do campo DAT\_APURACAO

02

Número de Instalação da Unidade Injetora

12

5

16

X

Campo NUM\_INSTAL\_INJ

03

Referência de Injeção

4

17

20

N

Preencher com AAMM do campo DAT\_REF\_INJ

04

Posto Tarifário

2

21

22

X

Campo COD\_POSTO\_INJ

05

Tarifa da Energia Injetada \(c/ 6 decimais\)

11

23

33

V

Campo VLR\_TARIFA\_INJ

06

Qtde\. Inicial de Energia \(kWh\) \(c/ 3 decimais\)

13

34

46

V

Campo QTD\_ENERGIA\_INI

07

Injeção de Energia \(kWh\) \(c/ 3 decimais\)

12

47

58

V

Campo QTD\_ENERGIA\_INJ

08

Saídas de Energia \(kWh\) \(c/ 3 decimais\)

12

59

70

V

Campo QTD\_ENERGIA\_SAI

09

Qtde\. Final de Energia \(kWh\) \(c/ 3 decimais\)

13

71

83

V

Campo QTD\_ENERGIA\_FIM

## <a id="_Toc223287716"></a>__RN06 \- Geração do Anexo de Compensações__

Gerar um arquivo para cada Estabelecimento selecionado na tela de Geração, considerando os registros da tabela de Controle de Compensação de Injeção de Energia Elétrica \(SAFX434\)\.

__Origem dos dados__: \- Tabela Controle de Compensação de Injeção de Energia Elétrica \(SAFX434\);

__Critérios da recuperação: __

\- Empresa – código da empresa do login;

\- Estabelecimento:

   Se parâmetro “*Geração por Inscrição Estadual Única*” = marcado

         Estabelecimento = código do estabelecimento selecionado para geração \(centralizador\), __e__, código dos estabelecimentos centralizados;

         \(conforme a parametrização de I\.E\.U\. do módulo de controle das obrigações estaduais\)

   Senão

         Estabelecimento = código do estabelecimento selecionado para geração;

\- Data Apuração – compreendida no Mês/Ano Referência da Apuração informado em tela;

Para cada registro de __Compensação__ recuperado, buscar o registro de __Crédito__ na Tabela Controle de Crédito de Injeção de Energia Elétrica \(SAFX433\), considerando os campos abaixo para correlação entre as duas tabelas:

Código da Empresa

COD\_EMPRESA

Código do Estabelecimento

COD\_ESTAB

Período de Referência da Apuração

DAT\_APURACAO

Número da Instalação da Unidade Injetora

NUM\_INSTAL\_INJ

Período de Referência da Injeção

DAT\_REF\_INJ

Posto Tarifário da Energia Injetada

COD\_POSTO\_INJ

Caso não seja encontrado registro de __Crédito__ na Tabela Controle de Crédito de Injeção de Energia Elétrica \(SAFX433\), exibir mensagem de aviso e prosseguir com a gravação dos registros no arquivo:

Arquivo de Compensação:

O Registro de Compensação foi gerado sem informação de Tarifa da Energia Injetada, Qtde\. de Energia Debitada e Fator de Ajuste, porque não foi encontrado um registro correspondente de Crédito na Tabela de Controle de Crédito de Injeção de Energia Elétrica \(SAFX433\)\.

Dados do Registro: Núm Instal Unid Injetora: XXXX Período Ref Injeção e Posto Tarifário da Energia Injetada: AA, Núm Instal Unid Consumidora: YYYY, Posto Tarifário da Energia Compensada: BB

 

__Regra de Processamento:__

1\) Os registros devem gravados ordenados por: 

- 
	- Número de Instalação da Unidade Injetora \(campo 02\)
	- Período de Referência de Injeção \(campo 03\)
	- Posto Tarifário da Energia Injetada \(campo 04\)
	- Número da Instalação da Unidade Consumidora \(campo 07\)
	- Posto Tarifário da Energia Compensada \(campo 08\)

2\) Cada registro corresponde a uma __combinação única__ de: 

- 
	- Número de Instalação da Unidade Injetora \(campo 02\)
	- Período de Referência de Injeção \(campo 03\)
	- Posto Tarifário da Energia Injetada \(campo 04\)
	- Número da Instalação da Unidade Consumidora \(campo 07\)
	- Posto Tarifário da Energia Compensada \(campo 08\)

Logo se a geração foi feita com o parâmetro “Geração por Inscrição Estadual Única” = marcado, o Arquivo de Compensação é gerado em nome do Estabelecimento __Centralizador__ e os registros lidos devem ser consolidados pelos campos \(Número de Instalação da Unidade Injetora, Período de Referência de Injeção, Posto Tarifário da Energia Injetada, Tarifa da Energia Injetada \(SAFX433\), Número da Instalação da Unidade Consumidora, Posto Tarifário da Energia Compensada e Tarifa da Energia Compensada \(SAFX434\)\), somando os campos de Quantidades\. 

Caso o resultado da consolidação gere mais de um registro para o mesmo Número de Instalação da Unidade Injetora, Período de Referência de Injeção e Posto Tarifário da Energia Injetada, Número da Instalação da Unidade Consumidora e Posto Tarifário da Energia Compensada, exibir mensagem de aviso e prosseguir com a gravação dos registros no arquivo:

Arquivo de Compensação  
Foi identificado mais de um registro para a mesmo Número de Instalação \(Injetora\), Período de Referência da Injeção, Posto Tarifário \(Injetada\), Número de Instalação \(Consumidora\) e Posto Tarifário \(Compensada\)

Essa duplicidade ocorreu porque foi encontrada variação na Tarifa da Energia Injetada e/ou na Tarifa da Energia Compensada entre os estabelecimentos que fazem parte da mesma Inscrição Estadual Única\.

3\) Gravar o Arquivo de Compensação com as seguintes informações:

n\.º

Conteúdo

Tam

Posição Inicial

Posição Final

Formato

__Regra de Preenchimento__

01

Referência de Apuração \(AAMM\)

4

1

4

N

Preencher com AAMM do campo DAT\_APURACAO da SAFX434

02

Número de Instalação da Unidade Injetora

12

5

16

X

Campo NUM\_INSTAL\_INJ da SAFX434

03

Referência de Injeção

4

17

20

N

Preencher com AAMM do campo DAT\_REF\_INJ da SAFX434

04

Posto Tarifário da Energia Injetada

2

21

22

X

Campo COD\_POSTO\_INJ da SAFX434

05

Tarifa da Energia Injetada \(c/ 6 decimais\)

11

23

33

V

Campo VLR\_TARIFA\_INJ da SAFX433

06

Qtde\. de Energia Debitada \(kWh\) \(c/ 3 decimais\)

12

34

45

V

Campo QTD\_ENERGIA\_SAI da SAFX433

07

Número de Instalação da Unidade Consumidora

12

46

57

X

Campo NUM\_INSTAL\_CONS da SAFX434

08

Posto Tarifário da Energia Compensada

2

58

59

X

Campo COD\_POSTO\_COMP da SAFX434

09

Tarifa da Energia Compensada \(c/ 6 decimais\)

11

60

70

V

Campo VLR\_TARIFA\_COMP da SAFX434

10

Qtde\. de Energia Compensada \(kWh\) \(c/ 3 decimais\)

12

71

82

V

Campo QTD\_ENERGIA\_COMP da SAFX434

11

Fator de Ajuste \(c/ 6 decimais\)

10

83

92

V

Se QTD\_ENERGIA\_SAI for igual a zero, preencher esse campo com zero\.

Se QTD\_ENERGIA\_SAI for diferente de a zero, preencher com o resultado do cálculo:

QTD\_ENERGIA\_COMP / QTD\_ENERGIA\_SAI, truncado na 6ª casa decimal

