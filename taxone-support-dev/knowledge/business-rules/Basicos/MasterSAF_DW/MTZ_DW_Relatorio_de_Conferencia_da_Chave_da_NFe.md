# MTZ_DW_Relatorio_de_Conferencia_da_Chave_da_NFe

- **Fonte:** MTZ_DW_Relatorio_de_Conferencia_da_Chave_da_NFe.docx
- **Modificado:** 2024-02-02
- **Tamanho:** 41 KB

---

# MastersafDW – Relatório de conferência da Chave Eletrônica

__Localização:__ Menu Básicos, Módulo DW, menu Relatórios 🡪 Conferências 🡪  Chave dos Documentos Fiscais Eletrônicos

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3966

Criação do relatório de conferência dos documentos fiscais eletrônicos

Especificação das regras de validação do relatório de conferência dos documentos fiscais eletrônicos

CH28743\-2013

Alteração na conferência do tipo de emissão \(normal/contingência\) que compõe a chave da NFe \(ver __RN11__\)

CH3612\_2013

Alteração na conferência do tipo de emissão que compõe a chave da NF\-e \(ver __RN11__\)

Este documento tem como objetivo alterar a regra do Campo Emissão em que não deve ser considerado a validação com data menor igual a 03/2011\.

CH17528\_2016

Alteração na conferência do tipo de emissão que compõe a chave da NF\-e \(ver __RN11__\)

Alteração na RN11 \- Campo Emissão para considerar como válido o caracter 8 na 35a posição da Chave de Acesso\.

MFS\-5644

Melhoria no Relatório de Conferência da Chave Eletrônica\.

Esse documento tem como objetivo alterar a geração do relatório para considerar as notas fiscais para consumidor final, modelo ‘65’ conforme a estrutura realizada para os modelos ‘55’ e ‘57’\.

MFS\-11266

Melhoria no Relatório de Conferência da Chave Eletrônica\.

Esse documento tem como objetivo incluir cupom fiscal eletrônico na validação da chave eletrônica\.

MFS24022

Melhoria no Relatório de Conferência da Chave Eletrônica

Inclusão do modelo 67 eletrônico na validação da chave eletrônica\.

## 	

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Regra Geral__

__\[ALTERADA – MFS\-11266\]__

Na tela de geração deverão compor os seguintes campos:

Tipo de Movimento:

Entrada\\Saída \(Default\)

Entrada

Saída

__Tratamento:__ Para CF\-e só existe a emissão, então esse campo deve ser bloqueado quando o mesmo for selecionado, pois não será considerado no filtro da seleção dos cupons eletrônicos SAFX201\.

__\[ALTERADA – MFS\-24022\]__

Tipo de Docto:

NF\-e \(Default\)

NFC\-e

CT\-e

CT\-e os

NF\-e\\ NFC\-e\\ CT\-e\\ CT\-e os

CF\-e

MFS\-11266

MFS24022

__RN01__

__O cabeçalho do relatório deve ser composto  pelos seguintes campos:__

__Empresa __= Deve mostrar a empresa na qual o usuário está logado\.

__Período __= Deve mostrar o período de geração do relatório no formato DD/MM/AAAA

__Página = __Deve mostrar a numeração da página do relatório\.

__Data = __Deve mostrar a data e hora em que foi gerado o relatório no formato DD/MM/AAAA e HH:MM:SS

__Filial__ = Deve mostrar a filial que foi solicitada na tela de geração do relatório

__CNPJ__ = Deve mostrar o CNPJ do estabelecimento demonstrado\. Recuperar da tabela ESTABELECIMENTO\.

__I\.E\.__ = Deve demonstrar a Inscrição Estadual do estabelecimento selecionado\. Deve ser verificado a UF do estabelecimento selecionado e a partir daí, buscar no cadastro das Inscrições Estaduais a correspondente\.

OS3966

__RN02__

__O corpo do relatório deve ser composto pelos seguintes campos nos casos de informações vindas da NF:__

__Nº do Docto Fiscal __= Deve mostrar o número do documento fiscal que consta na SAFX07\.

__Série__ = Deve mostrar a série do documento fiscal que consta na SAFX07\.

__Data Fiscal__ = Deve mostrar a data fiscal do documento que consta na SAFX07\.

__E/S__ = Deve indicar se o documento fiscal se trata de um documento de ENTRADA \(E\) ou SAÍDA \(S\)

__Chave Eletrônica = __Deve indicar a Chave da NFe ou CT\-e ou NFC\-e existente na SAFX07\.

OS3966

MFS5644

__RN02\.a__

__O corpo do relatório deve ser composto pelos seguintes campos no casos de informações vindas do CF:__

__Nº do Docto Fiscal __= Deve mostrar o número do cupom fiscal eletrônico que consta na SAFX201\.

__Série__ = Deve mostrar o número do equipamento do cupom fiscal eletrônico que consta na SAFX201\.

__Data Fiscal__ = Deve mostrar a data de emissão do cupom fiscal eletrônico que consta na SAFX201\.

__E/S__ = Deve indicar que se trata de um documento de SAÍDA \(S\)

__Chave Eletrônica = __Deve indicar a Chave de Acesso do CF\-e existente na SAFX201\.

MFS\-11266

__RN03__

__Regra Geral:__

Serão considerados na geração os documentos fiscais que se enquadrem nos filtros utilizados na tela de Geração do Relatório\.

Devem ser verificados na SAFX07 os seguintes campos para recuperação das informações no relatório:

 \- Data Fiscal;

 \- Indicador de Entrada/Saída

 \- Modelo de documento

Após a seleção dos documentos fiscais, o sistema deverá verificar o campo 226 da SAFX07 \(NUM\_AUTENTC\_NFE\) e caso este contenha um cadastro válido de 44 caracteres, deve\-se continuar a validação dos campos da chave eletrônica\. Caso o campo contenha menos ou mais do que os 44 caracteres, não deverão ser realizadas as próximas validações sendo gerada a informação __ERRO__ em todas as colunas a partir da coluna UF, pertinentes a esta nota\.

OBS: A parametrização para apresentar os documentos fiscais sem erro ou não, se refere aos documentos fiscais cuja Chave Eletrônica tenha a quantidade correta \(44\) de caracteres\.

Os campos devem apresentar os caracteres que foram conferidos em caso de uma validação realizada com sucesso, caso o campo tenha alguma inconsistência, deverá ser apresentada a mensagem “ERRO”\. Caso o conteúdo da chave seja validado, deve ser apresentada a mensagem “OK”\.

OS3966

__RN03\.a__

__Regra Geral:__

Serão considerados na geração os documentos fiscais que se enquadrem nos filtros utilizados na tela de Geração do Relatório \(ver MTZ – Tela de Geracao\.doc\)\.

Devem ser verificados na SAFX201 os seguintes campos para recuperação das informações no relatório:

 \- Data de Emissão;

 \- Modelo de documento

Após a seleção dos documentos fiscais, o sistema deverá verificar o campo 10 da SAFX201 \(NUM\_AUTENTC\_NFE\) e caso este contenha um cadastro válido de 44 caracteres, deve\-se continuar a validação dos campos da chave eletrônica\. Caso o campo contenha menos ou mais do que os 44 caracteres, não deverão ser realizadas as próximas validações sendo gerada a informação __ERRO__ em todas as colunas a partir da coluna UF, pertinentes a esta nota\.

OBS: A parametrização para apresentar os documentos fiscais sem erro ou não, se refere aos documentos fiscais cuja Chave Eletrônica tenha a quantidade correta \(44\) de caracteres\.

Os campos devem apresentar os caracteres que foram conferidos em caso de uma validação realizada com sucesso, caso o campo tenha alguma inconsistência, deverá ser apresentada a mensagem “ERRO”\. Caso o conteúdo da chave seja validado, deve ser apresentada a mensagem “OK”\.

MFS\-11266

__RN04__

__Campo Qtde:__

Este campo deve representar a quantidade de caracteres contido no campo NUM\_AUTENTC\_NFE da SAFX07\. Quando este campo estiver preenchido com a informação valida de 44 caracteres, deverá ser realizada as demais validações do relatório\. Quando este campo for preenchido com uma informação <> de 44 caracteres, as demais validações da referida nota fiscal, devem ser canceladas e o sistema deverá prosseguir para a próxima NF\. 

O campo deverá ser preenchido com a quantidade de caracteres que houver no campo 226 da SAFX07 \(NUM\_AUTENTC\_NFE\)\.

OS3966

__RN04\.a__

__Campo Qtde:__

Este campo deve representar a quantidade de caracteres contido no campo NUM\_AUTENTC\_NFE da SAFX201\. Quando este campo estiver preenchido com a informação valida de 44 caracteres, deverão ser realizadas as demais validações do relatório\. Quando este campo for preenchido com uma informação <> de 44 caracteres, as demais validações da referida nota fiscal, devem ser canceladas e o sistema deverá prosseguir para a próxima NF\. 

O campo deverá ser preenchido com a quantidade de caracteres que houver no campo 10 da SAFX201 \(NUM\_AUTENTC\_NFE\)\.

MFS\-11266

__RN05__

__Campo UF:__

A validação deste campo deve ser feita verificando\-se os dois primeiros dígitos da Chave Eletrônica\.

Deve ser verificado na tabela de MUNICIPIO o campo COD\_UF equivalente ao que consta na chave e recuperado o IDENT\_ESTADO correspondente\. 

Em se tratando de documentos fiscais de __ENTRADA__ \(campo 03 da SAFX07 = “1”\), deverá ser validado se o IDENT\_ESTADO correspondente equivale ao do cadastro da pessoa fis/jur da SAFX04 que consta no documento fiscal\.

Em se tratando de documentos fiscais de __ENTRADA PRÓPRIA__ \(campo 03 da SAFX07 >1 e <9\) deverá ser validado se o IDENT\_ESTADO correspondente equivale ao do cadastro do estabelecimento da tabela ESTABELECIMENTO\.

Em se tratando de documentos fiscais de __SAÍDA__, deverá ser validado se o IDENT\_ESTADO correspondente equivale ao do cadastro do estabelecimento da tabela ESTABELECIMENTO\.

OS3966

__RN05\.a__

__Campo Código da UF:__

A validação deste campo deve ser feita verificando\-se os dois primeiros dígitos da Chave Eletrônica\.

Deve ser verificado na tabela de MUNICIPIO o campo COD\_UF equivalente ao que consta na chave e recuperado o IDENT\_ESTADO correspondente\. 

Como se trata de documentos fiscais de __SAÍDA__ deverá ser validado se o IDENT\_ESTADO correspondente equivale ao do cadastro do estabelecimento da tabela ESTABELECIMENTO\.

MFS\-11266

__RN06__

__Campo Data:__

A validação deste campo deverá ser realizada a partir do terceiro caractere da chave eletrônica até o sexto\.

Os dois primeiros dígitos se referem ao ANO de emissão do documento fiscal e os outros dois se referem ao MÊS, ambos devem ser os mesmos que constam no campo 11 da SAFX07 do referido documento fiscal\.

OS3966

__RN06\.a__

__Campo AAMM da Emissão:__

A validação deste campo deverá ser realizada a partir do terceiro caractere da chave eletrônica até o sexto\.

Os dois primeiros dígitos se referem ao ANO de emissão do cupom fiscal eletrônico e os outros dois se referem ao MÊS, ambos devem ser os mesmos que constam no campo 05 da SAFX201 do referido cupom fiscal eletrônico\.

MFS\-11266

__RN07__

__Campo CNPJ:__

A validação deste campo deverá ser realizada a partir do sétimo caractere da chave eletrônica até o vigésimo\.

Em se tratando de documentos fiscais de __ENTRADA DE TERCEIROS__, o valor recuperado deverá ser o mesmo que consta no campo 06 da SAFX04 da pessoa Fis/Jur que consta no referido documento fiscal\. 

Em se tratando de documentos fiscais de __ENTRADA PRÓPRIA__ e __SAÍDA __o valor recuperado deverá ser o mesmo que consta no campo CGC da tabela ESTABELECIMENTO, correspondente ao estabelecimento selecionado na geração do relatório\.

OS3966

__RN07\.a__

__Campo CNPJ do Emitente:__

A validação deste campo deverá ser realizada a partir do sétimo caractere da chave eletrônica até o vigésimo\.

Como se trata de documentos fiscais de __SAÍDA __o valor recuperado deverá ser o mesmo que consta no campo CGC da tabela ESTABELECIMENTO, correspondente ao estabelecimento selecionado na geração do relatório\.

MFS\-11266

__RN08__

__Campo Modelo:__

__Observação:__ Considerar as Notas Fiscais do modelo ‘65’ e 67

A validação deste campo deverá ser realizada a partir do vigésimo primeiro até o vigésimo segundo caractere\.

Deve ser verificado na tabela X2024\_modelo\_docto, o ident\_modelo que consta na X07 do documento fiscal referido\. A partir desta informação, recuperar o valor do campo COD\_MODELO que consta na tabela X2024\_modelo\_docto para este ident\. Este modelo deve estar de acordo com a informação que consta na chave do documento fiscal eletrônico\.

OS3966

MFS5644

MFS24022

__RN08\.a__

__Campo Modelo do Documento Fiscal:__

A validação deste campo deverá ser realizada a partir do vigésimo primeiro até o vigésimo segundo caractere\.

Deve ser verificado na tabela X2024\_modelo\_docto, o ident\_modelo que consta na SAFX201 do cupom fiscal eletrônico referido\. A partir desta informação, recuperar o valor do campo COD\_MODELO que consta na tabela X2024\_modelo\_docto para este ident\. Este modelo deve estar de acordo com a informação que consta na chave do cupom fiscal eletrônico\.

MFS\-11266

__RN09__

__Campo Série:__

A validação deste campo deverá ser realizada a partir do vigésimo terceiro até o vigésimo quinto caractere\.

Deve ser verificado o campo SERIE\_DOCFIS da X07 do referido documento fiscal\. Este valor deve ser o mesmo que o recuperado da chave eletrônica do documento fiscal\.

OS3966

__RN09\.a__

__Campo Número de Série do SAT:__

A validação deste campo deverá ser realizada a partir do vigésimo terceiro até o trigésimo primeiro caractere\.

Deve ser verificado o campo NUM\_EQUIP da SAFX201 do referido cupom fiscal eletrônico\. Este valor deve ser o mesmo que o recuperado da chave eletrônica do cupom fiscal eletrônico\.

Obs: Como se trata de campo numérico na tabela SAFX201 tratar a verificação dos zeros\.

MFS\-11266

__RN10__

__Campo Num\. Docto:__

A validação deste campo deverá ser realizada a partir do vigésimo sexto até o trigésimo quarto caractere\.

Deve ser verificado o campo NUM\_DOCFIS da X07 do referido documento fiscal\. Este valor deve ser o mesmo que o recuperado da chave eletrônica do documento fiscal\.

No momento da validação, como o campo na chave eletrônica terá obrigatoriamente 9 posições, caso o número do documento fiscal na X07 tenha menos caracteres, este deverá ser completado com zeros a esquerda até atingir o limite de nove caracteres\.

Obs: Na hipótese de os documentos fiscais eletrônicos escriturados na X07, conterem MAIS do que nove caracteres, o valor recuperado \(Número do documento fiscal\) deverá ser alinhado à direita e os caracteres que sobrepuserem o limite \(9\) deverão ser desconsiderados\.

OS3966

__RN10\.a__

__Campo Número do CF\-e:__

A validação deste campo deverá ser realizada a partir do trigésimo segundo até o trigésimo sétimo caractere\.

Deve ser verificado o campo NUM\_CUPOM da SAFX201 do referido cupom fiscal eletrônico\. Este valor deve ser o mesmo que o recuperado da chave eletrônica do cupom fiscal eletrônico\.

MFS\-11266

__RN11__

__Campo Emissão:__

A validação deste campo deverá ser realizada a partir do trigésimo quinto caractere\.

Deve ser verificado o campo 255 – IND\_NF\_CONTINGENCIA da SAFX07 do referido documento fiscal e realizada a seguinte conferência:

 \- Se o caractere da NF\-e for igual a __1, __então o campo na SAFX07 deverá constar com a informação__ N;__

__ \- __Se o caractere da NF\-e for igual a__ 2__, então o campo na SAFX07 deverá constar com a informação__ 1;__

__ \- __Se o caractere da NF\-e for igual a__ 3, __então o campo na SAFX07 deverá constar com a informação__ 2;__

__ \- __Se o caractere da NF\-e for igual a__ 4, __então o campo na SAFX07 deverá constar com a informação__ 3;__

__ \- __Se o caractere da NF\-e for igual a__ 5, __então o campo na SAFX07 deverá constar com a informação__ 4;__

__Alteração chamado 28743/20132:__

\(o campo “255\-NF Emitida em Contingência” não será mais utilizado na validação do tipo de emissão da NFe, pois trata\-se de um campo não obrigatório, e que atende apenas aos usuários do SEFII\)\.

Será verificado apenas se o conteúdo do trigésimo quinto caracter é um dos valores válidos de acordo com a lista de opções do portal da NFe:

1 \(emissão normal\)

2 \(Contingência FS\)

3 \(Contingência SCAN\)

4 \(Contingência DPEC\)

5 \(Contingência FS\-DA\)

6 \(Contingência SVC\-NA\)

7 \(Contingência SVC\-RS\)

8 \(Contingência SVC\-SP\)

__Atenção: __Esse campo não deve ser validado quando a data de emissão \(Campo Data\) for <= 03/2011, pois esse Campo Emissão foi implementado na versão 2\.00 em 04/2011\.

OS3966

CH3612\_2013

CH17528\_2016

__RN12__

__Campo Dígito Verificador:__

A validação deste campo deverá ser realizada a partir do ultimo caractere\.

Por se tratar de um cálculo demasiado grande, somente será feita a validação caso o fleg “Confere Dígito Verificador” na tela de geração do relatório estiver marcado\.

Este campo assegura a confiabilidade dos dados informados no documento fiscal eletrônico, é obtido através de um cálculo que envolve todos os caracteres da chave eletrônica e deverá ser validado da seguinte rotina:

 \- A partir da informação do ultimo caractere da chave eletrônica do referido documento fiscal, o sistema deverá realizar um cálculo de “somatória” dos valores da chave eletrônica\. Para tal, deve ser levado em consideração que cada informação da chave tem um “peso” diferente e cada qual, deverá ser calculado proporcionalmente, por exemplo:

O campo UF \(caracteres 1 e 2\) tem respectivamente pesos 4 e 3, logo para um documento fiscal emitido em São Paulo \(cod\. UF = 35 \) teríamos os valores __12__ \(4 \* 3\) e __15__ \(3 \* 5\);

\- Segue abaixo uma tabela de pesos para cada caractere da chave eletrônica\. O campo PONDERAÇÃO deverá representar o resultado dos campos CHAVE \* PESO:

Chave

UF

ANO EMISSÃO

CNPJ

MOD

SERIE

NUM\. DOC

E

COD\. NUMERICO

Peso

4

3

2

9

8

7

6

5

4

3

2

9

8

7

6

5

4

3

2

9

8

7

6

5

4

3

2

9

8

7

6

5

4

3

2

9

8

7

6

5

4

3

2

Ponderação

Obs: O campo CÓDIGO NUMÉRICO não será validado pelo relatório, por não se tratarem de informações sobre o documento fiscal\.

Obs²: Os valores dos pesos deverão ser internos, não cabendo ao cliente realizar quaisquer tipos de manutenção, uma vez que estes valores são fixos\.

\- Depois de realizado o cálculo e obtida todas as ponderações, estas deverão ser somadas\. O valor obtido, por sua vez, deverá ser DIVIDIDO por ONZE \(11\)\. Então, deverá ser realizado o cálculo seguinte em que o resto desta divisão é subtraído do número ONZE \(11\) novamente\.

Abaixo segue um exemplo prático de como deverá ser realizado o cálculo:

Chave Eletrônica: 35130335402759000185554040000020711000010047 \(o dígito verificador desta chave é 7\)\.

Jogando esta chave na tabela acima, calculando as ponderações e posteriormente somando\-as teremos um valor de 543\.

O resto da divisão de 543/11 = 4 \(já que o valor calculado é de 49\), fazendo inversamente 49\*11 = 539\.

Subtraindo o resto da divisão, pelo valor 11 teremos: 11 \- 4 = 7\.

Obs: Quando o resto da divisão for igual a 0 \(zero\) ou 1 \(hum\) o valor do dígito verificador deverá ser 0\.

OS3966

__RN12\.a__

__Campo Dígito Verificador:__

A validação deste campo deverá ser realizada a partir do ultimo caractere\.

Por se tratar de um cálculo demasiado grande, somente será feita a validação caso o fleg “Confere Dígito Verificador” na tela de geração do relatório estiver marcado\.

Este campo assegura a confiabilidade dos dados informados no cupom fiscal eletrônico, é obtido através de um cálculo que envolve todos os caracteres da chave eletrônica e deverá ser validado da seguinte rotina:

 \- A partir da informação do último caractere da chave eletrônica do referido cupom fiscal eletrônico, o sistema deverá realizar um cálculo de “somatória” dos valores da chave eletrônica\. Para tal, deve ser levado em consideração que cada informação da chave tem um “peso” diferente e cada qual, deverá ser calculado proporcionalmente, por exemplo:

O campo UF \(caracteres 1 e 2\) tem respectivamente pesos 4 e 3, logo para um cupom fiscal eletrônico emitido em São Paulo \(cod\. UF = 35 \) teríamos os valores __12__ \(4 \* 3\) e __15__ \(3 \* 5\);

\- Segue abaixo uma tabela de pesos para cada caractere da chave eletrônica\. O campo PONDERAÇÃO deverá representar o resultado dos campos CHAVE \* PESO:

Chave

UF

ANO EMISSÃO

CNPJ

MOD

SERIE

NUM\. DOC

COD\. NUMERICO

Peso

4

3

2

9

8

7

6

5

4

3

2

9

8

7

6

5

4

3

2

9

8

7

6

5

4

3

9

8

7

6

5

4

3

9

8

7

6

5

4

3

9

8

7

Ponderação

Obs: O campo CÓDIGO NUMÉRICO não será validado pelo relatório, por não se tratarem de informações sobre o documento fiscal\.

Obs²: Os valores dos pesos deverão ser internos, não cabendo ao cliente realizar quaisquer tipos de manutenção, uma vez que estes valores são fixos\.

\- Depois de realizado o cálculo e obtida todas as ponderações, estas deverão ser somadas\. O valor obtido, por sua vez, deverá ser DIVIDIDO por ONZE \(11\)\. Então, deverá ser realizado o cálculo seguinte em que o resto desta divisão é subtraído do número ONZE \(11\) novamente\.

Abaixo segue um exemplo prático de como deverá ser realizado o cálculo:

Chave Eletrônica: 35130335402759000185554040000020711000010047 \(o dígito verificador desta chave é 7\)\.

Jogando esta chave na tabela acima, calculando as ponderações e posteriormente somando\-as teremos um valor de 543\.

O resto da divisão de 543/11 = 4 \(já que o valor calculado é de 49\), fazendo inversamente 49\*11 = 539\.

Subtraindo o resto da divisão, pelo valor 11 teremos: 11 \- 4 = 7\.

Obs: Quando o resto da divisão for igual a 0 \(zero\) ou 1 \(hum\) o valor do dígito verificador deverá ser 0\.

MFS\-11266

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

