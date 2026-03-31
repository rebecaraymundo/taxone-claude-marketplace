# MTZ_ESTORNO_DE_DEBITOS_Geracao_Arquivo_Magnetico

- **Fonte:** MTZ_ESTORNO_DE_DEBITOS_Geracao_Arquivo_Magnetico.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 108 KB

---

THOMSON REUTERS

Estorno de Débitos – Modelo 21/22

Geração dos Documentos Fiscais de Estorno de Débitos para Empresas Prestadoras de Serviços de Comunicação e Telecomunicação

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

OS2890

Marcos Roberto de Oliveira

Este documento de requisito tem por objetivo permitir a criação de novos campos na tabela SAFX42, além de criar o novo módulo intitulado “Portaria CAT 06/09” para geração do arquivo eletrônico contendo o estorno do valor do imposto indevidamente debitado em Notas Fiscais de Serviço de Comunicações \(modelo 21\) ou Telecomunicações \(modelo 22\), emitidas a partir de maio de 2004\.

OS2890

Juliana Garcia

Revisão do documento\.

OS4076

Marcos Roberto de Oliveira

De acordo com o INFOLEGIS nº 288/13 – C, o CONFAZ disponibilizou o Ato Cotepe/ICMS n° 22, de 18/06/2013 alterando o item 5 do Anexo I do Ato Cotepe/ICMS nº 24/2010, que trata do registro de itens com ICMS recuperado ou a recuperar\.

O item 5 do anexo I, passa a vigorar com as seguintes alterações:

	DESCRICAO	                                                                              TAM	DE	ATE	TIPO

27	Número do item da Nota Fiscal de ressarcimento ao cliente     	3	508	511	N

28	Brancos	                                                                                                10	512	520	X

Este Ato entra em vigor na data de sua publicação no Diário Oficial da União em 24/06/2013\.

A alteração ocorrerá no Registro Tipo “2” do Anexo I do meio magnético gerado\. Essa alteração ocorrerá nesse ponto do sistema, visto que ocorreu somente a inclusão de um novo campo\.

MFS1676

Julyana Perrucini

Este documento tem como objetivo revisar a documentação desse módulo e alterar a geração do arquivo magnético contemplando a opção de gerar a partir da nova SAFX175 – Registros de Estorno de Débitos\.

MFS1828

Julyana Perrucini

Este documento tem como objetivo incluir o parâmetro “Considerar Status” na geração do arquivo magnético para seleção dos Registros de Estorno de Débitos de acordo com o Status preenchido na conciliação dos documentos fiscais\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN00

__Regra Geral e de Seleção:__

- Deverá ser criado dentro do grupo “Estadual” o módulo “Estorno de Débitos – Modelos 21/22”\. Esse módulo deverá ficar localizado entre os módulos “DPI\-GO” e “FOMENTAR/PRODUZIR/MICROPRODUZIR – GO”\.
- Incluir o texto resumo do módulo: *“O objetivo deste módulo é permitir um controle do estorno do valor do imposto indevidamente debitado em Notas Fiscais de Serviço de Comunicações \(modelo 21\) ou Telecomunicações \(modelo 22\)\. Através de parametrização os arquivos digitais poderão ser gerados no formato da Portaria CAT 06/09 ou do Ato COTEPE 24/2010\.”\.*
- Dentro do módulo Estorno de Débitos – Modelos 21/22 deverá ser criado o item de menu Meio Magnético >> Geração\. 
- Esse menu irá permitir que o cliente realize a geração do meio magnético contendo as informações de Estorno de Débitos para as empresas prestadoras de serviço de Comunicação \(modelo 21\) e Telecomunicação \(modelo 22\) utilizando o layout da Portaria CAT 06/09 ou do Ato COTEPE 24/2010\.
- A geração do meio magnético será no padrão Framework\.
- Os arquivos no formato “Portaria CAT 06/2009” só devem ser gerados arquivos cujo período seja a partir de 01/05/2004\. Caso seja gerado um arquivo anterior a esse período no campo “Período” deve ser exibida uma mensagem de log de erro “*A Portaria CAT 06/2009 deve ser gerada a partir de Maio de 2004”*\. 
- Os arquivos no formato “Ato COTEPE 24/2010” podem ser gerados de qualquer período informado\.
- Deverão ser recuperados os documentos fiscais de utilities da SAFX42 e SAFX43 na seguinte situação:
- COD\_EMPRESA = parametrizado na geração do arquivo
- COD\_ESTAB = parametrizado na geração do arquivo
- Modelo: \(campo 13 da SAFX42\)
	- 
		- Igual a “21 e 22”
- Classificação: \(campo 50 da SAFX42\)
	- 
		- Igual a “01” e “03”
- Situação: \(campo “21 – Situação da Nota” da SAFX42\)
	- 
		- Somente documentos não cancelados \(situação = “N”\)
- Data de Emissão/Escr\. Fiscal: \(campo 03 da SAFX42\)
	- 
		- Entre a Data Inicial e Data Final de geração do arquivo
- Valor do ICMS a ser estornado : \(campo novo da SAFX43\)\.
	- 
		- Campo “Valor do ICMS a ser estornado” preenchido

__\[ALTERADA – MFS1676\]/\[ALTERADA – MFS1828\]__

- Quando o parâmetro __“Geração por Registros de Estorno por Débitos – SAFX175”__ da Geração do Meio Magnético estiver marcado, deverão ser recuperados os documentos fiscais de utilities da SAFX175 na seguinte situação:
- COD\_EMPRESA = parametrizado na geração do arquivo
- COD\_ESTAB = parametrizado na geração do arquivo
	- Modelo do Documento da NF Objeto do Estorno = 21 e 22
	- Período de Declaração da Informação: dentro do período parametrizado na geração do arquivo
	- ICMS a ser estornado: campo “ICMS a ser Estornado” preenchido com valor maior que zero

Os registros serão selecionados nas condições acima e de acordo com a parametrização de __“Considerar Status” __marcado:

- Se igual a “N”, considerar os registros da SAFX175 que estiverem com o campo Status iguais a “N”;
- Se igual a “S”, considerar os registros da SAFX175 que estiverem com o campo Status iguais a “S”;
- Se igual a Ambos, considerar os registros da SAFX175 que estiverem com o campo Status iguais a “N” e “S”\.
- Não considerar os registros que o campo Status da SAFX175 esteja branco/nulo\.
- Quando o parâmetro “__Geração Centralizada por Inscrição Estadual Única__” da Geração do Meio Magnético estiver marcado, o somatório deverá considerar todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no módulo controle das obrigações estaduais\. \(Inventário e Documentário Fiscal\)\.  As informações deverão ser cadastradas sempre em nome do estabelecimento centralizador\. 

OS2890

MFS1676

MFS1828

RNR1

__Registro 1 – Registro de Controle e Identificação__

Campos comuns no layout da Portaria CAT 06/09 e Ato COTEPE 24/2010: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12,

13, 14, 15, 16, 17 e 18\.

Deverá ser gerado apenas 1 \(um\) registro do tipo “1” por arquivo\.

Formato dos campos: 

- Numérico \(N\): sem sinal, não compactado, suprimido o ponto e a vírgula\. Alinhado à direita, com zeros à esquerda até completar o campo\.
- Datas devem ser preenchidas no formato ano, mês e dia \(AAAAMMDD\)\. Na ausência de informação, o campo deverá ser preenchido com zeros até completar o campo\.
- Alfanumérico \(X\): letras, números e caracteres especiais válidos\. Alinhado à esquerda, com posições não significativas em branco\. Na ausência de informação, o campo deverá ser preenchido com brancos até completar o campo\.

OS2890

RNR1\-01

__Registro 1 – Registro de Controle e Identificação__ – Campo Tipo do Registro:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

Gravar fixo “1”\.

OS2890

RNR1\-02

__Registro 1 – Registro de Controle e Identificação__ – Campo CNPJ:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

Deverá ser gravado nesse campo, o CNPJ do estabelecimento parametrizado\. 

Essa informação deve ser recuperada do campo CGC da tabela ESTABELECIMENTO\.

OS2890

RNR1\-03

__Registro 1 – Registro de Controle e Identificação__ – Campo Inscrição Estadual/ IE:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

Deverá ser gravada nesse campo, a inscrição estadual do estabelecimento parametrizado\. 

Essa informação deve ser recuperada do campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL\.

OS2890

RNR1\-04

__Registro 1 – Registro de Controle e Identificação__ – Campo Razão Social:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

Deverá ser gravada nesse campo, a razão social do estabelecimento parametrizado\. 

Essa informação deve ser recuperada do campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO\.

OS2890

RNR1\-05

__Registro 1 – Registro de Controle e Identificação__ – Campo Endereço:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

Deverá ser gravado nesse campo, o endereço do estabelecimento parametrizado\. 

Essa informação deve ser recuperada dos campos ENDERECO, NUM\_ENDERECO e COMPL\_ENDERECO \(as informações dos campos devem ser separadas por espaço\) da tabela ESTABELECIMENTO\. 

OS2890

RNR1\-06

__Registro 1 – Registro de Controle e Identificação__ – Campo CEP:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

Deverá ser gravado nesse campo, p CEP do estabelecimento parametrizado\. 

Essa informação deve ser recuperada do campo CEP da tabela ESTABELECIMENTO\.

__Tratamento:__

- Formato 999999\-999 \(utilizar o traço\)\.

OS2890

RNR1\-07

__Registro 1 – Registro de Controle e Identificação__ – Campo Bairro:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

Deverá ser gravado nesse campo, o bairro do estabelecimento parametrizado\. 

Essa informação deve ser recuperada do campo BAIRRO da tabela ESTABELECIMENTO\.

OS2890

RNR1\-08

__Registro 1 – Registro de Controle e Identificação__ – Campo Município:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

Deverá ser gravado nesse campo, o município do estabelecimento parametrizado\. 

Essa informação deve ser recuperada do campo DESCRICAO da tabela MUNICIPIO relacionando com o COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

OS2890

RNR1\-09

__Registro 1 – Registro de Controle e Identificação__ – Campo UF:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

Deverá ser gravado nesse campo, o estado do estabelecimento parametrizado\. 

Essa informação deve ser recuperada do campo COD\_ESTADO da tabela ESTADO\.

OS2890

RNR1\-10

__Registro 1 – Registro de Controle e Identificação__ – Campo Responsável pela Apresentação:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

Deverá ser gravado nesse campo, o nome do responsável legal pelo estabelecimento\. 

Essa informação deve ser recuperada do campo NOM\_RESPONSAVEL da tabela RESP\_INFORMACAO a partir da informação contida no campo “Responsável Legal” do menu  Parâmetros >> Dados Iniciais\.

OS2890

MFS1676

RNR1\-11

__Registro 1 – Registro de Controle e Identificação__ – Campo Cargo:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

Deverá ser gravado nesse campo, o cargo do responsável legal pelo estabelecimento\. 

Essa informação deve ser recuperada do campo DSC\_CARGO da tabela RESP\_INFORMACAO a partir da informação contida no campo “Responsável Legal” do menu  Parâmetros >> Dados Iniciais\.

OS2890

MFS1676

RNR1\-12

__Registro 1 – Registro de Controle e Identificação__ – Campo Telefone:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

Deverá ser gravado nesse campo, o telefone do responsável legal pelo estabelecimento\. 

Essa informação deve ser recuperada dos campos NUM\_DDD e NUM\_TELEFONE da tabela RESP\_INFORMACAO a partir da informação contida no campo “Responsável Legal” do menu  Parâmetros >> Dados Iniciais\.

__Tratamento:__

- Por se tratar de um campo numérico, as informações devem ser gravadas juntas\. 

Exemplo: \(11\) 2159\-0500, onde 11 é o DDD e 2159\-0500 é o telefone, no arquivo, deve ser apresentado 001121590500\.

OS2890

MFS1676

RNR1\-13

__Registro 1 – Registro de Controle e Identificação__ – Campo e\-mail:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

Deverá ser gravado nesse campo, o e\-mail do responsável legal pelo estabelecimento\. 

Essa informação deve ser recuperada do campo E\_MAIL da tabela RESP\_INFORMACAO a partir da informação contida no campo “Responsável Legal” do menu  Parâmetros >> Dados Iniciais\.

OS2890

MFS1676

RNR1\-14

__Registro 1 – Registro de Controle e Identificação__ – Campo Qtde de Registros de Estorno de Débitos/ Quantidade de registros de Itens com ICMS recuperado ou a recuperar:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

Deverá ser gravada nesse campo, a quantidade de registros do tipo 2 presentes no arquivo\. 

Deverá ser somada a quantidade de registros do tipo 2 presentes no arquivo e gravada nesse campo\.

Por se tratar de um campo numérico, os zeros devem ser acrescentados à esquerda\.

OS2890

RNR1\-15

__Registro 1 – Registro de Controle e Identificação__ – Campo Valor Total:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

Quando o layout for igual a “Portaria CAT 06/2009”, deverá ser gravado nesse campo o somatório do campo 15 \- “Valor do Item a ser Estornado” da RNR2\-15\.P do Registro 2\.

Quando o layout for igual a “Ato COTEPE 24/2010”, deverá ser gravado nesse campo o somatório do campo 17 \- “Valor total do item da nota fiscal objeto do estorno” da RNR2\-17\.A do Registro 2\.

OS2890

RNR1\-16

__Registro 1 – Registro de Controle e Identificação__ – Campo BC ICMS:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175 – SAFX175” da tela de geração do arquivo estiver desmarcado:

Acumular somatório do campo 23 \(VLR\_BASE\_ICMS\_1\) da tabela SAFX43\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175 – SAFX175” da tela de geração do arquivo estiver marcado:

Acumular somatório do campo somatório do campo 18 \- “Valor base de cálculo do ICMS do item da nota fiscal objeto do estorno”\.

OS2890

MFS1676

RNR1\-17

__Registro 1 – Registro de Controle e Identificação__ – Campo ICMS:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175 – SAFX175” da tela de geração do arquivo estiver desmarcado:

Acumular somatório do campo 22 \(VLR\_TRIB\_ICMS\) da tabela SAFX43\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175 – SAFX175” da tela de geração do arquivo estiver marcado:

Acumular somatório do campo somatório do campo 19 \- “ICMS do item da nota fiscal objeto do estorno”\.

OS2890

MFS1676

RNR1\-18

__Registro 1 – Registro de Controle e Identificação__ – Campo ICMS a ser estornado/ ICMS recuperado ou a recuperar:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

Quando o layout for igual a “Portaria CAT 06/2009”, deverá ser gravado nesse campo o somatório do campo 16 \- “ICMS a ser Estornado” da RNR2\-16\.P do Registro 2\.

Quando o layout for igual a “Ato COTEPE 24/2010”, deverá ser gravado nesse campo o somatório do campo 20 \- “ICMS recuperado ou a recuperar” da RNR2\-20\.A do Registro 2\.

OS2890

RNR1\-19

__Registro 1 – Registro de Controle e Identificação__ – Campo Situação:

__Atende:__ Ato COTEPE 24/2010\.

Deverá ser gravada nesse campo do layout Ato COTEPE 24/2010, a informação que estiver contida no campo “Situação” da tela de geração do meio magnético, do módulo Estorno de Débitos – Modelos 21/22, item de menu: Meio Magnético >> Geração\.

__Tratamento:__

- Caso a opção selecionada seja “Normal” gravar “N”;
- Caso a opção selecionada seja “Substituto” gravar “S”\.

OS2890

RNR1\-20

__Registro 1 – Registro de Controle e Identificação__ – Campo Brancos:

__Atende:__ Ato COTEPE 24/2010\.

Deverá ser gravado nesse campo do arquivo do layout Ato COTEPE 24/2010 espaços em branco\.

OS2890

RNR2

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\)__

Campos comuns no layout da Portaria CAT 06/09 e Ato COTEPE 24/2010: 01, 02, 03, 04, 05, 06, 07, 08, 09, 11, 12, 13 e 14\.

__\[ALTERADA – MFS1676\]__

Identificação das regras:

- As regras com formato do CÓD RNR2\-XX\.A = Ato COTEPE;
- As regras com formato do CÓD RNR2\-XX\.P = Portaria;
- As regras com formato do CÓD RNR2\-XX = Ambas\.

Deverão ser gravados registros do tipo “2” quando for necessário para cada item do Documento Fiscal objeto de estorno\. 

Um documento fiscal que possua mais de 1 \(um\) item pode ter os seus itens gravados em duas linhas diferentes no registro tipo “2” do arquivo\. Para isso as regras contidas na RN00 devem ser respeitadas\.

Somente os itens que possuam o campo “ICMS a ser estornado” preenchido nas SAFX43 e SAFX175\.

Formato dos campos: 

- Numérico \(N\): sem sinal, não compactado, suprimido o ponto e a vírgula\. Alinhado à direita, com zeros à esquerda, de 12 \(doze\) posições\.
- Datas devem ser preenchidas no formato ano, mês e dia \(AAAAMMDD\)\. Na ausência de informação, o campo deverá ser preenchido com zeros;
- Alfanumérico \(X\): letras, números e caracteres especiais válidos\. Alinhado à esquerda, com posições não significativas em branco\. Na ausência de informação, o campo deverá ser preenchido com brancos\.

OS2890

MFS1676

RNR2\-01

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Tipo do Registro:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

Gravar fixo “2”\.

OS2890

RNR2\-02

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Modelo NFSC ou NFST estornada/ Modelo da Nota Fiscal Objeto do Estorno:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175 – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo 13 \(COD\_MODELO\) da tabela SAFX42\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175 – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Modelo do Documento da NF Objeto do Estorno da tabela SAFX175\.

OS2890

MFS1676

RNR2\-03\.A

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Série da Nota Fiscal Objeto do Estorno:

__Atende:__ Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175 – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo 07 \(SERIE\_DOCFIS\) da tabela SAFX42\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175 – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Série da NF Objeto do Estorno da tabela SAFX175\.

OS2890

MFS1676

RNR2\-03\.P

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Número da NFSC ou NFST estornada:

__Atende:__ Portaria CAT 06/2009\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175 – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo 06 \(NUM\_DOCFIS\) da tabela SAFX42\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Nº da NF Objeto do Estorno da tabela SAFX175\.

__Tratamento:__

- Alinhar à direita, com zeros à esquerda para completar ou trucar à esquerda quando não for suficiente\.

OS2890

MFS1676

RNR2\-04\.A

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Número da Nota Fiscal Objeto do Estorno:

__Atende:__ Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo 06 \(NUM\_DOCFIS\) da tabela SAFX42\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Nº da NF Objeto do Estorno da tabela SAFX175\.

__Tratamento:__

- Alinhar à direita, com zeros à esquerda para completar ou trucar à esquerda quando não for suficiente\.

OS2890

MFS1676

RNR2\-04\.P

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Série da NFSC ou NFST estornada:

__Atende:__ Portaria CAT 06/2009\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo 07 \(SERIE\_DOCFIS\) da tabela SAFX42\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Série da NF Objeto do Estorno da tabela SAFX175\.

OS2890

MFS1676

RNR2\-05

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Data de Emissão/ Data de Emissão da Nota Fiscal Objeto do Estorno:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo 03 \(DAT\_FISCAL\) da tabela SAFX42\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Data de Emissão da NF Objeto do Estorno da tabela SAFX175\.

OS2890

MFS1676

RNR2\-06

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Chave de Autenticação Digital/ Código de Autenticação Digital do Documento Fiscal:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo 48 \(COD\_AUTENTIC\) da tabela SAFX42\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Cód\. Autenticação da NF Objeto do Estorno da tabela SAFX175\.

OS2890

MFS1676

RNR2\-07

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo CNPJ ou CPF/ CNPJ ou CPF do Tomador do serviço:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo 06 \(CPF\_CGC\) da tabela SAFX04 referente ao tomador de serviço cadastrado na SAFX42\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo 06 \(CPF\_CGC\) da tabela SAFX04 referente ao tomador de serviço cadastrado na SAFX175\.

OS2890

MFS1676

RNR2\-08

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Inscrição Estadual/ IE do Tomador do serviço:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo 08 \(INSC\_ESTADUAL\) da tabela SAFX04 referente ao tomador de serviço cadastrado na SAFX42\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo 08 \(INSC\_ESTADUAL\) da tabela SAFX04 referente ao tomador de serviço cadastrado na SAFX175\.

__Tratamento:__

- Se o campo estiver preenchido como “ISENTO” gravar “ISENTO”;
- Se o campo não estiver preenchido gravar “ISENTO”\.

OS2890

MFS1676

RNR2\-09

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Razão Social/ Nome ou Razão Social do Tomador do serviço:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo 05 \(RAZAO\_SOCIAL\) da tabela SAFX04 referente ao tomador de serviço cadastrado na SAFX42\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo 05 \(RAZAO\_SOCIAL\) da tabela SAFX04 referente ao tomador de serviço cadastrado na SAFX175\.

OS2890

MFS1676

RNR2\-10\.A

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Número do Terminal Telefônico do Tomador da Nota Fiscal Objeto do Estorno:

__Atende:__ Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo do arquivo do layout Ato COTEPE 24/2010, a informação que estiver contida no campo 15 \(TEL\_CLIENTE\) da tabela SAFX42\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Nº do Terminal Faturado da NF Objeto do Estorno da tabela SAFX175\.

OS2890

MFS1676

RNR2\-10\.P

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Código de Identificação do Tomador do Serviço:

__Atende:__ Portaria CAT 06/2009\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo do arquivo do layout Portaria CAT 06/09, a informação que estiver contida no campo 02 \(COD\_FIS\_JUR\) da tabela SAFX04 referente ao tomador de serviço cadastrado na SAFX42\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo do arquivo do layout Portaria CAT 06/09, a informação que estiver contida no campo 02 \(COD\_FIS\_JUR\) da tabela SAFX04 referente ao tomador de serviço cadastrado na SAFX175\.

OS2890

MFS1676

RNR2\-11

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Valor Total/ Valor Total da Nota Fiscal Objeto do Estorno:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo 17 \(VLR\_TOT\_NOTA\) da tabela SAFX42\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Valor Total da NF Objeto do Estorno da tabela SAFX175\.

OS2890

MFS1676

RNR2\-12

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo BC ICMS/ Valor Base de Cálculo do ICMS da Nota Fiscal Objeto do Estorno:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo 22 \(VLR\_BASE\_ICMS1\) da tabela SAFX42\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo BC de ICMS da NF Objeto do Estorno da tabela SAFX175\.

OS2890

MFS1676

RNR2\-13

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo ICMS/ Valor do ICMS destacado na Nota Fiscal Objeto do Estorno:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo 26 \(VLR\_TRIB\_ICMS\) da tabela SAFX42\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Valor do ICMS da NF Objeto do Estorno da tabela SAFX175\.

OS2890

MFS1676

RNR2\-14

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Número do Item a ser Estornado/ Número do Item da Nota Fiscal Objeto do Estorno:

__Atende:__ Portaria CAT 06/2009 e Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo 09 \(NUM\_ITEM\) da tabela SAFX43\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Nº do Item da NF Objeto do Estorno da tabela SAFX175\.

OS2890

MFS1676

RNR2\-15\.A

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Código do Item de Serviço da Nota Fiscal Objeto do Estorno:

__Atende:__ Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo do arquivo do layout Ato COTEPE 24/2010, a informação que estiver contida no campo 02 \(COD\_PRODUTO\) da tabela SAFX2013 referenciado ao produto cadastrado na SAFX43\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo do arquivo do layout Ato COTEPE 24/2010, a informação que estiver contida no campo 02 \(COD\_PRODUTO\) da tabela SAFX2013 referente ao produto cadastrado na SAFX175\.

__Tratamento:__

- Alinhar à esquerda e truncar à direita\.

OS2890

MFS1676

RNR2\-15\.P

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Valor do Item a ser Estornado:

__Atende:__ Portaria CAT 06/2009\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo do layout Portaria CAT 06/09, a informação que estiver contida no campo 19 \(VLR\_SERVICO\) da tabela SAFX43\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Valor Total do Item da NF Objeto do Estorno da tabela SAFX175\.

OS2890

MFS1676

RNR2\-16\.A

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Descrição do Item da Nota Fiscal Objeto do Estorno:

__Atende:__ Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo do layout Ato COTEPE 24/2010, a informação que estiver contida no campo 04 \(DESCRICAO\) da tabela SAFX2013 referente ao produto cadastrado na SAX43\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo do layout Ato COTEPE 24/2010, a informação que estiver contida no campo 04 \(DESCRICAO\) da tabela SAFX2013 referente ao produto cadastrado na SAX175\.

OS2890

MFS1676

RNR2\-16\.P

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo ICMS a ser estornado:

__Atende:__ Portaria CAT 06/2009\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo do layout Portaria CAT 06/09, a informação que estiver contida no campo 99 \(VLR\_ICMS\_EST\_RET\) da tabela SAFX43\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo ICMS a ser Estornado da tabela SAFX175\.

OS2890

MFS1676

RNR2\-17\.A

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Valor Total do Item da Nota Fiscal Objeto do Estorno:

__Atende:__ Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo do layout do Ato COTEPE 24/2010, a informação que estiver contida no campo 19 \(VLR\_SERVICO\) da tabela SAFX43\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Valor Total do Item da NF Objeto do Estorno da tabela SAFX175\.

OS2890

MFS1676

RNR2\-17\.P

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Hipótese de Estorno:

__Atende:__ Portaria CAT 06/2009\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo do layout Portaria CAT 06/09, a informação que estiver contida no campo 100 \(HIPOTESE\_ESTORNO\) da tabela SAFX43\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Hipótese de Estorno da tabela SAFX175\.

OS2890

MFS1676

RNR2\-18\.A

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Base de Cálculo do ICMS do Item da Nota Fiscal Objeto do Estorno:

__Atende:__ Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo do layout do Ato COTEPE 24/2010, a informação que estiver contida no campo 23 \(VLR\_BASE\_ICMS\_1\) da tabela SAFX43\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo BC de ICMS do Item da NF Objeto de Estorno da tabela SAFX175\.

OS2890

MFS1676

RNR2\-18\.P

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Motivo do Estorno:

__Atende:__ Portaria CAT 06/2009\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo do layout Portaria CAT 06/09, a informação que estiver contida no campo 101 \(MOTIVO\_ESTORNO\) da tabela SAFX43\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Motivo do Estorno da tabela SAFX175\.

OS2890

MFS1676

RNR2\-19\.A

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo ICMS do Item da Nota Fiscal Objeto do Estorno:

__Atende:__ Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo do layout do Ato COTEPE 24/2010, a informação que estiver contida no campo 22 \(VLR\_TRIB\_ICMS\) da tabela SAFX43\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Valor do ICMS do Item da NF Objeto de Estorno da tabela SAFX175\.

OS2890

MFS1676

RNR2\-19\.P

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Número de Controle da Reclamação:

__Atende:__ Portaria CAT 06/2009\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo do layout Portaria CAT 06/09, a informação que estiver contida no campo 102 \(NUM\_CTRL\_RECL\) da tabela SAFX43\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Nº da Reclamação da tabela SAFX175\.

OS2890

MFS1676

RNR2\-20\.A

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo ICMS Recuperado ou a Recuperar:

__Atende:__ Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo do layout do Ato COTEPE 24/2010, a informação que estiver contida no campo 99 \(VLR\_ICMS\_EST\_RET\) da tabela SAFX43\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo ICMS a ser Estornado da tabela SAFX175\.

OS2890

MFS1676

RNR2\-21\.A

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Descrição do Motivo:

__Atende:__ Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo do layout do Ato COTEPE 24/2010, a informação que estiver contida no campo 101 \(MOTIVO\_ESTORNO\) da tabela SAFX43\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Motivo do Estorno da tabela SAFX175\.

OS2890

MFS1676

RNR2\-22\.A

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Número do Protocolo de atendimento da Reclamação:

__Atende:__ Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo do layout do Ato COTEPE 24/2010, a informação que estiver contida no campo 102 \(NUM\_CTRL\_RECL\) da tabela SAFX43\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Nº da Reclamação da tabela SAFX175\.

OS2890

MFS1676

RNR2\-23\.A

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Modelo da Nota Fiscal com Ressarcimento ao Cliente:

__Atende:__ Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo do layout do Ato COTEPE 24/2010, a informação que estiver contida no campo 100 \(COD\_MODELO\_RESSARC\) da tabela SAFX42\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Modelo do Documento da NF de Ressarcimento da tabela SAFX175\.

OS2890

MFS1676

RNR2\-24\.A

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Série da Nota Fiscal com Ressarcimento ao Cliente:

__Atende:__ Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo do layout do Ato COTEPE 24/2010, a informação que estiver contida no campo 99 \(SERIE\_DOCFIS\_RESSARC\) da tabela SAFX42\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Série da NF de Ressarcimento da tabela SAFX175\.

OS2890

MFS1676

RNR2\-25\.A

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Número da Nota Fiscal com Ressarcimento ao Cliente:

__Atende:__ Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo do layout do Ato COTEPE 24/2010, a informação que estiver contida no campo 98 \(NUM\_DOCFIS\_RESSARC\) da tabela SAFX42\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Nº da NF de Ressarcimento da tabela SAFX175\.

__Tratamento:__

- Alinhar à direita, com zeros à esquerda para completar ou trucar à esquerda quando não for suficiente\.

OS2890

MFS1676

RNR2\-26\.A

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Data de Emissão da Nota Fiscal com Ressarcimento ao Cliente:

__Atende:__ Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo do layout do Ato COTEPE 24/2010, a informação que estiver contida no campo 101 \(DAT\_EMISSAO\_RESSARC\) da tabela SAFX42\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Data de Emissão da NF de Ressarcimento da tabela SAFX175\.

OS2890

MFS1676

RNR2\-27\.A

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Número do Item da Nota Fiscal com Ressarcimento ao Cliente:

__Atende:__ Ato COTEPE 24/2010\.

__\[ALTERADA – MFS1676\]__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver desmarcado:

Deverá ser gravada nesse campo do layout do Ato COTEPE 24/2010, a informação que estiver contida no campo 109 \(NUM\_ITEM\_RESSARC\) da tabela SAFX42\.

__Senão__

__Se __parâmetro “Geração por Registros de Estorno de Débitos – SAFX175” da tela de geração do arquivo estiver marcado:

Deverá ser gravada nesse campo, a informação que estiver contida no campo Nº do Item da NF de Ressarcimento da tabela SAFX175\.

OS4076 

MFS1676

RNR2\-28\.A

__Registro 2 – Registro de Estorno de Débitos \(ICMS recupera ou a Recuperar\) __– Campo Brancos:

__Atende:__ Ato COTEPE 24/2010\.

__\[ALTERADA – OS4076\]__

Gravar nesse campo do arquivo do layout Ato COTEPE 24/2010 espaços em branco\.

OS2890

OS4076

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

