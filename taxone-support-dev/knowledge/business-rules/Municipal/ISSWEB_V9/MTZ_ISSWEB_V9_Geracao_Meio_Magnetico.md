# MTZ_ISSWEB_V9_Geracao_Meio_Magnetico

- **Fonte:** MTZ_ISSWEB_V9_Geracao_Meio_Magnetico.docx
- **Modificado:** 2025-10-27
- **Tamanho:** 103 KB

---

THOMSON REUTERS

Municipal \- ISSWeb V9

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-14969

Julyana Perrucini

Este documento tem como objetivo incluir o novo validador ISSWeb V9\.

MFS24791

Andréa Rocha

Inclusão do município de Mogi das Cruzes/SP\.

MFS28612

Andréa Rocha

Exclusão do município de Mogi das Cruzes/SP e Itaquaquecetuba/SP do validador\.

MFS\-68547

Elisabete Costa

Inclusão do município de Alumínio/SP\.

__MFS\-829438     __

Graciela Soares

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN01

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo __“Itaquaquecetuba”__ deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: *“Consiste na entrega das informações sobre os serviços prestados e serviços tomados do município de Itaquaquecetuba\.”*\.

O novo módulo __“Mairinque”__ deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: *“Consiste na entrega das informações sobre os serviços prestados e serviços tomados do município de *Mairinque*\.”*\.

O módulo __“Mogi das Cruzes”__ deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: <a id="_Hlk2266596"></a>*“Consiste na entrega das informações sobre os serviços prestados e serviços tomados do município de *Mogi das Cruzes*\.”*\.

O novo módulo __“Alumínio”__ deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: *“Consiste na entrega das informações sobre os serviços prestados e serviços tomados do município de Alumínio\.”*\.

MFS\-14969

MFS24791

MFS28612

MFS\-68547

RN02

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “23107” \(__Itaquaquecetuba__\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Itaquaquecetuba, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “28403” \(__Mairinque__\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Mairinque, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “30607” \(__Mogi das Cruzes__\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Mogi das Cruzes, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “1152” \(__Alumínio__\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Alumínio, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

MFS\-14969

MFS24791

MFS28612

MFS\-68547

RN03

__Estrutura de menus do módulo ISS WEB V9:__

Deverão ser criados os seguintes menu e sub\-menus no módulo ISS WEB V9:

- Arquivo
- Obrigações
	- Geração do Meio Magnético
	- Arquivo de Entradas de Serviços \(Const\. Civil/Utilities /Telecom\)
- Janela
- Ajuda 

MFS\-14969

RN04

__Regra de criação do nome do arquivo:__

__Serviços Prestados:__

__SP\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.TXT__, onde:

       __SP__: Apenas registros de serviços prestados\.

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: SP\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.TXT

__SP\_ISSWEBV9\_MUNICIPIO\_DDMMAAAA\.TXT__, onde:

__       SP\_ISSWEBV9__: representa a obrigação que está sendo gerada\.

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __DDMMAAAA__: representa a data inicial da geração\.

       __\.TXT__: extensão do arquivo\.

*Exemplo:* SP\_ISSWEBV9\_MAIRINQUE\_01012010\.TXT

                SP\_ISSWEBV9\_ALUMÍNIO\_01012010\.TXT

__Serviços Tomados:__

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.TXT__, onde:

       __ST__: Apenas registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.TXT

__ST\_ISSWEBV9\_MUNICIPIO\_DDMMAAAA\.TXT__, onde:

__       ST\_ISSWEBV9__: representa a obrigação que está sendo gerada\.

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __DDMMAAAA__: representa a data inicial da geração\.

       __\.TXT__: extensão do arquivo\.

*Exemplo:* ST\_ISSWEBV9\_MAIRINQUE\_01012010\.TXT

ST\_ISSWEBV9\_ALUMÍNIO\_01012010\.TXT

Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado, deve ser realizada a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\_ MMAAAA\.TXT__, onde:

       __ST__: Apenas registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial da geração

__MMAAAA:__ mês da competência referente à nota gerada\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\_012010\.TXT

__ST\_ISSWEBV9\_MUNICIPIO\_DDMMAAAA\_MMAAAA\.TXT__, onde:

__               ST\_ISSWEBV9__: representa a obrigação que está sendo gerada\.    

__               MUNICIPIO__: representa o município que está sendo gerado\.   

               __DDMMAAAA__: representa a data inicial da geração\.   

__               MMAAAA:__ mês da competência referente à nota gerada

               __\.TXT__: extensão do arquivo\.

*Exemplo:* ST\_ISSWEBV9\_MAIRINQUE\_01012014\_122013\.TXT

                ST\_ISSWEBV9\_ALUMÍNIO\_01012014\_122013\.TXT

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__*Observação:* Este parâmetro \(Quebrar Arquivo por Data de Emissão\) será válido apenas para Notas de Serviços Tomados\.__

MFS\-14969

MFS\-68547

MFS829438

RN05

__Regra p/ tela da Geração do Meio Magnético:__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Gerar Serviços Prestados:__ deve ser exibido através de um CheckBox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Gerar Serviços Tomados:__ deve ser exibido através de um CheckBox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um CheckBox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Enviar NF por E\-mail__: deve ser exibido através de um CheckBox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

*Observação:* Cada campo deverá exibir mensagem padrão caso de não preenchimento\.

MFS\-14969

RN06

__Regra p/ Geração do Arquivo Magnético__

- Para ser importado o arquivo deve estar na codificação “ANSI”;
- Tipo de dado Numérico \- preenchido com zeros, alinhados à direita;
- Tipo de dado Char \- preenchido com espaços, alinhados á esquerda;
- Tipo de dado Financeiro \- preenchidos com zeros considerando 2 \(duas\) casas decimais, alinhado à direita;
- Tipo de dado Finaneiro4 \- preenchidos com zeros considerando 4 \(quatro\) casas decimais, alinhado à direita;
- Tipo de dado Financeiro9 \- preenchidos com zeros considerando 9 \(nove\) casas decimais, alinhado à direita\.

MFS\-14969

RN07

__Regra p/ Recuperar Notas Fiscais de Serviços Prestados:__

Esse arquivo deve ser gerado apenas quando o campo “Gerar Serviços Prestados” estiver marcado e deve conter todas as notas fiscais com as seguintes características:

- Nota de Saída \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL = 9\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência

Quando a nota não tiver itens não deve ser recuperada\.

O agrupamento das notas fiscais deverá ser realizado pelos campos __CodAtividade, ImpRetido e Aliquota__\.

MFS\-14969

RN08

__Regra p/ Recuperar Notas Fiscais de Serviços Tomados:__

Esse arquivo deve ser gerado apenas quando o campo “Gerar serviços tomados” estiver marcado e deve conter todas as notas fiscais com as seguintes características:

- Nota de Entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência
- Não deve recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> S\)

Quando a nota não tiver itens não deve ser recuperada\.

O agrupamento das notas fiscais deverá ser realizado pelos campos __CodAtividade, ImpRetido e Aliquota__\.

MFS\-14969

RN09

__Regra p/ o campo Header – TipodeRegistro__

Preencher com fixo “0”\.

Campo obrigatório

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-14969

RN10

__Regra p/ o campo Header – TpIdentificação__

Preencher com fixo “1”\.

Campo obrigatório

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-14969

RN11

__Regra p/ o campo Header – CnpjCpf__

Preencher com o conteúdo do campo CGC da tabela ESTABELECIMENTO\.

Campo obrigatório

Formato: 99999999999999

Tipo: Numérico

Tamanho: 14

MFS\-14969

RN12

__Regra p/ o campo Header – Ccm__

Preencher com o conteúdo do campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO\.

Campo obrigatório

Formato: 9999999

Tipo: Numérico

Tamanho: 8

MFS\-14969

RN13

__Regra p/ o campo Header – VersaoLayout__

Preencher com fixo “09”\.

Campo obrigatório

Formato: 99

Tipo: Numérico

Tamanho: 2

MFS\-14969

RN14

__Regra p/ o campo Header – Filler__

Campo livre para futuras informações, preencher com brancos\.

Campo não obrigatório

Formato: XXX\.\.\.

Tipo: Char

Tamanho: 124

MFS\-14969

RN15

__Regra p/ o campo Detalhe – Tipo de Registro__

Preencher com fixo “1”\.

Campo obrigatório

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-14969

RN16

__Regra p/ o campo Detalhe – SequencialNf__

Sequencial de Registro de NF devendo iniciar com 1 para cada arquivo\.

Campo obrigatório

Formato: 99999999

Tipo: Numérico

Tamanho: 8

MFS\-14969

RN17

__Regra p/ o campo Detalhe – NF__

Preencher com fixo “00000000”\.

*Observação:* o campo NF deverá ser preenchido com zeros \(0\), este número é fornecido pela Prefeitura\.

Campo obrigatório

Formato: 99999999

Tipo: Numérico

Tamanho: 8

MFS\-14969

RN18

__Regra p/ o campo Detalhe – SituacaoNF__

Preencher com:

1, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> ‘S’;

2, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = ‘S’\.

*Observação:* Serviço Tomado será sempre igual a “1”\.

Campo obrigatório

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-14969

RN19

__Regra p/ o campo Detalhe – Dt Emissão__

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

Campo obrigatório

Formato: 99999999 \(DDMMAAAA\)

Tipo: Numérico

Tamanho: 8

MFS\-14969

RN20

__Regra p/ o campo Detalhe – CodAtividade__

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na nota fiscal\.

__Tratamento:__

- Se o código de serviço da lei 116 não estiver cadastrado na SAFX2018, deverá ser gravado com 0 \(zeros\) e emitida a mensagem de log: *“Erro: Favor preencher o código da Lei 116 no cadastro do serviço para o serviço informado na nota fiscal <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”*;
- Se o código de serviço da lei 116 estiver diferente para os serviços cadastrados na NF, deverá ser gravado com 0 \(zeros\) e emitida a mensagem de log: *“Erro: O código da Lei 116 cadastrado no serviço informado na nota fiscal difere com os demais serviços, favor verificar\! <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”\.*

Campo obrigatório

Formato: 999999

Tipo: Numérico

Tamanho: 6

MFS\-14969

RN21

__Regra p/ o campo Detalhe – CFPS__

Preencher com o conteúdo do campo COD\_CFPS da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Se o campo do código fiscal de prestação de serviço não estiver preenchido, deverá ser gravado com 0 \(zeros\) e emitida a mensagem de log: *“Erro: Favor preencher o CFPS da nota fiscal <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”\.*

Campo obrigatório

Formato: 999

Tipo: Numérico

Tamanho: 3

MFS\-14969

RN22

__Regra p/ o campo Detalhe – Série__

Preencher com fixo “17”\.

Campo obrigatório

Formato: 99

Tipo: Numérico

Tamanho: 2

MFS\-14969

RN23

__Regra p/ o campo Detalhe – CNPJ/CPF__

Preencher com o conteúdo do campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR referente à pessoa fis/jur cadastrada na nota fiscal\.

Campo obrigatório

Formato: 99999999999999

Tipo: Numérico

Tamanho: até 14

MFS\-14969

RN24

__Regra p/ o campo Detalhe – Nome__

Preencher com o conteúdo do campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR referente à pessoa fis/jur cadastrada na nota fiscal\.

Campo obrigatório

Formato: XXX\.\.\.

Tipo: Char

Tamanho: 100

MFS\-14969

RN25

__Regra p/ o campo Detalhe – CEP__

Preencher com o conteúdo do campo CEP da tabela X04\_PESSOA\_FIS\_JUR referente à pessoa fis/jur cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo do CEP não estiver preenchido no cadastro da pessoa física/ jurídica, deverá ser gravado com brancos e emitida a mensagem de log: *“Erro: Favor preencher o CEP da PFJ <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”\.*

Campo obrigatório

Formato: XXXXXXXX

Tipo: Char

Tamanho: 8

MFS\-14969

RN26

__Regra p/ o campo Detalhe – Endereço__

Preencher com o conteúdo do campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente à pessoa fis/jur cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo do Endereço não estiver preenchido no cadastro da pessoa física/ jurídica, deverá ser gravado com brancos e emitida a mensagem de log: *“Erro: Favor preencher o Endereço da PFJ <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”\.*

Campo obrigatório

Formato: XXX\.\.\.

Tipo: Char

Tamanho: 100

MFS\-14969

RN27

__Regra p/ o campo Detalhe – Bairro__

Preencher com o conteúdo do campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR referente à pessoa fis/jur cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo do Bairro não estiver preenchido no cadastro da pessoa física/ jurídica, deverá ser gravado com brancos e emitida a mensagem de log: *“Erro: Favor preencher o Bairro da PFJ <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”\.*

Campo obrigatório

Formato: XXX\.\.\.

Tipo: Char

Tamanho: 50

MFS\-14969

RN28

__Regra p/ o campo Detalhe – Cidade__

Preencher com o conteúdo do campo CIDADE da tabela X04\_PESSOA\_FIS\_JUR referente à pessoa fis/jur cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo da Cidade não estiver preenchido no cadastro da pessoa física/ jurídica, deverá ser gravado com brancos e emitida a mensagem de log: *“Erro: Favor preencher a Cidade da PFJ <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”\.*

Campo obrigatório

Formato: XXX\.\.\.

Tipo: Char

Tamanho: 60

MFS\-14969

RN29

__Regra p/ o campo Detalhe – Estado__

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao IDENT\_ESTADO da pessoa fis/jur cadastrada na nota fiscal\.

__Tratamento:__

- Se o campo da UF não estiver preenchido no cadastro da pessoa física/ jurídica, deverá ser gravado com brancos e emitida a mensagem de log: *“Erro: Favor preencher a UF da PFJ <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”\.*

Campo obrigatório

Formato: XX

Tipo: Char

Tamanho: 2

MFS\-14969

RN30

__Regra p/ o campo Detalhe – Endereçocobrança__

Preencher com brancos\.

Campo não obrigatório

Formato: XXX\.\.\.

Tipo: Char

Tamanho: 100

MFS\-14969

RN31

__Regra p/ o campo Detalhe – Email__

Preencher com o conteúdo do campo E\_MAIL da tabela X04\_PESSOA\_FIS\_JUR referente à pessoa fis/jur cadastrada na nota fiscal\.

Campo não obrigatório

Formato: XXX\.\.\.

Tipo: Char

Tamanho: 80

MFS\-14969

RN32

__Regra p/ o campo Detalhe – EnviarNFporemail__

Preencher com:

S, se o campo Enviar NF por E\-mail estiver marcado na tela de geração do arquivo magnético;

N, se o campo Enviar NF por E\-mail estiver marcado na tela de geração do arquivo magnético\.

*Observação:* não haverá escolha por NF, então se selecionado o usuário receberá da Prefeitura todas as NF do período\.

Campo obrigatório

Formato: X

Tipo: Char

Tamanho: 1

MFS\-14969

RN33

__Regra p/ o campo Detalhe – ImpRetido__

__Para notas Emitidas:__

Verificar o local da prestação do serviço \(campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\.

Preencher com “S” quando pelo menos uma das seguintes opções for verdadeira:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “2" e se o local da prestação do serviço = município do módulo selecionado; OU 
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO E se o local da prestação do serviço = município do módulo selecionado; OU
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido E se o local da prestação do serviço = município do módulo selecionado\.

Caso nenhuma das opões seja verdadeira, preencher com “N”\.

__Para notas Recebidas:__

Verificar o local da prestação do serviço \(campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\.

Preencher com “S” quando pelo menos uma das seguintes opções for verdadeira:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado; OU 
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado; OU
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

Caso nenhuma das opões seja verdadeira, preencher com “N”\.

__Tratamento:__

- Nas duas situações, ou seja, nas notas emitidas e recebidas, se o imposto retido divergir entre os itens, deverá ser gravado com “N” e emitida à mensagem de log: *“Erro: O imposto retido está divergindo entre os itens, favor verificar se foi utilizada a SAFX2098 e se suas alíquotas estão diferentes para o serviço cadastrado ou se o valor retido foi preenchido corretamente nos itens do documento fiscal\. <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”\.*

Campo obrigatório

Formato: X

Tipo: Char

Tamanho: 1

MFS\-14969

RN34

__Regra p/ o campo Detalhe NF – VlrServiço__

Preencher com o somatório do campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 4 para ser preenchido de acordo com o tamanho exigido no layout;
- Não considerar pontos ou vírgulas;
- Preencher com zeros à esquerda se o tamanho do campo não for atingido\.

*Exemplo:* 999999999999999,99

Campo obrigatório

Formato: 99999999999999

Tipo: Financeiro

Tamanho: 14

MFS\-14969

RN35

__Regra p/ o campo Detalhe NF – VlrDeduções__

Preencher com o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 4 para ser preenchido de acordo com o tamanho exigido no layout;
- Não considerar pontos ou vírgulas;
- Preencher com zeros à esquerda se o tamanho do campo não for atingido\.

*Exemplo:* 999999999999999,99

Campo não obrigatório

Formato: 99999999999999

Tipo: Financeiro

Tamanho: 14

MFS\-14969

RN36

__Regra p/ o campo Detalhe NF – VlrImposto__

Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 4 para ser preenchido de acordo com o tamanho exigido no layout;
- Não considerar pontos ou vírgulas;
- Preencher com zeros à esquerda se o tamanho do campo não for atingido\.

*Exemplo:* 999999999999999,99

Campo obrigatório

Formato: 99999999999999

Tipo: Financeiro

Tamanho: 14

MFS\-14969

RN37

__Regra p/ o campo Detalhe NF – Alíquota__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Se na NF a alíquota divergir entre os itens, deverá ser gravado com 0 \(zeros\) e emitida à mensagem de log: *“Erro: A alíquota está divergente entre os itens da nota fiscal e pode não corresponder com a atividade informada, favor verificar\! <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”\.*

Campo obrigatório

Formato: 99999

Tipo: Financeiro

Tamanho: 5

MFS\-14969

RN38

__Regra p/ o campo Detalhe NF – VlrTotalNota__

Preencher com o somatório do campo VLR\_TOT\_NOTA da tabela DWT\_DOCTO\_FISCAL\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 4 para ser preenchido de acordo com o tamanho exigido no layout;
- Não considerar pontos ou vírgulas;
- Preencher com zeros à esquerda se o tamanho do campo não for atingido\.

*Exemplo:* 999999999999999,99

Campo obrigatório

Formato: 99999999999999

Tipo: Financeiro

Tamanho: 14

MFS\-14969

RN39

__Regra p/ o campo Detalhe NF – VlrCofins__

Preencher com o somatório do campo VLR\_COFINS da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 4 para ser preenchido de acordo com o tamanho exigido no layout;
- Não considerar pontos ou vírgulas;
- Preencher com zeros à esquerda se o tamanho do campo não for atingido\.

*Exemplo:* 999999999999999,99

Campo não obrigatório

Formato: 99999999999999

Tipo: Financeiro

Tamanho: 14

MFS\-14969

RN40

__Regra p/ o campo Detalhe NF – VlrPIS__

Preencher com o somatório do campo VLR\_PIS da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 4 para ser preenchido de acordo com o tamanho exigido no layout;
- Não considerar pontos ou vírgulas;
- Preencher com zeros à esquerda se o tamanho do campo não for atingido\.

*Exemplo:* 999999999999999,99

Campo não obrigatório

Formato: 99999999999999

Tipo: Financeiro

Tamanho: 14

MFS\-14969

RN41

__Regra p/ o campo Detalhe NF – VlrIRRF__

Preencher com o conteúdo do campo VLR\_TRIBUTO\_IR da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 4 para ser preenchido de acordo com o tamanho exigido no layout;
- Não considerar pontos ou vírgulas;
- Preencher com zeros à esquerda se o tamanho do campo não for atingido\.

*Exemplo:* 999999999999999,99

Campo não obrigatório

Formato: 99999999999999

Tipo: Financeiro

Tamanho: 14

MFS\-14969

RN42

__Regra p/ o campo Detalhe NF – VlrINSS__

Preencher com o somatório do campo VLR\_INSS\_RETIDO da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 4 para ser preenchido de acordo com o tamanho exigido no layout;
- Não considerar pontos ou vírgulas;
- Preencher com zeros à esquerda se o tamanho do campo não for atingido\.

*Exemplo:* 999999999999999,99

Campo não obrigatório

Formato: 99999999999999

Tipo: Financeiro

Tamanho: 14

MFS\-14969

RN43

__Regra p/ o campo Detalhe NF – VlrCSLL__

Preencher com o somatório do campo VLR\_CSLL da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 4 para ser preenchido de acordo com o tamanho exigido no layout;
- Não considerar pontos ou vírgulas;
- Preencher com zeros à esquerda se o tamanho do campo não for atingido\.

*Exemplo:* 999999999999999,99

Campo não obrigatório

Formato: 99999999999999

Tipo: Financeiro

Tamanho: 14

MFS\-14969

RN44

__Regra p/ o campo Detalhe NF – RPS__

Preencher com o conteúdo do campo NUM\_RPS\_NFE da tabela DWT\_DOCTO\_FISCAL\.

__Tratamento:__

- Se o campo do RPS não estiver preenchido no documento fiscal, deverá ser gravado com 0 \(zeros\) e emitida a mensagem de log: *“Erro: Favor preencher o número de RPS referente ao documento fiscal <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”\.*

Campo obrigatório

Formato: 99999999

Tipo: Numérico

Tamanho: 8

MFS\-14969

RN45

__Regra p/ o campo Detalhe NF – Modelo__

Preencher com:

F, quando o campo MODELO\_NF\_DMS = “SF”, “VF”, “1F” ou “TF”;

S, quando o campo MODELO\_NF\_DMS <> “SF”, “VF”, “1F” ou “TF”;

__Tratamento:__

- Se o campo do Modelo NF – Atend\. Municipal não estiver preenchido no documento fiscal, deverá ser gravado com branco e emitida a mensagem de log: *“Erro: Favor preencher o Modelo NF – Atend\. Municipal <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”\.*

Campo obrigatório

Formato: X

Tipo: Char

Tamanho: 1

MFS\-14969

RN46

__Regra p/ o campo Detalhe NF – Observação__

Preencher com o conteúdo do campo OBS\_INF\_ADIC\_NF da tabela DWT\_DOCTO\_FISCAL\.

Campo não obrigatório

Formato: XXX\.\.\.

Tipo: Char

Tamanho: 255

MFS\-14969

RN47

__Regra p/ o campo Detalhe NF – DtEmissãoRPS__

Preencher com o conteúdo do campo DAT\_EMISSAO\_RPS\_NFE da tabela DWT\_DOCTO\_FISCAL\.

__Tratamento:__

- Se o campo da data de emissão do RPS não estiver preenchido no documento fiscal, deverá ser gravado com 0 \(zeros\) e emitida a mensagem de log: *“Erro: Favor preencher a data de emissão do RPS referente ao documento fiscal <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”\.*

Campo obrigatório

Formato: 99999999 \(DDMMAAAA\)

Tipo: Numérico

Tamanho: 8

MFS\-14969

RN48

__Regra p/ o campo Detalhe NF – TipoTomador__

Preencher com:

J, se o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR tiver mais que 11 posições;

F, se o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR tiver até 11 posições;

O, se o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR não estiver preenchido \(casos de situação especial\)\.

Campo obrigatório

Formato: X

Tipo: Char

Tamanho: 1

MFS\-14969

RN49

__Regra p/ o campo Detalhe NF – RGInscriçãoEstadual__

Preencher com o conteúdo do campo INSC\_ESTADUAL da tabela X04\_PESSOA\_FIS\_JUR quando o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR tiver mais que 11 posições, caso contrário preencher com brancos\.

*Observação:* Não trataremos pessoa física porque não possuímos campo para preenchimento de RG\.

Campo não obrigatório

Formato: XXX\.\.\.

Tipo: Char

Tamanho: 20

MFS\-14969

RN50

__Regra p/ o campo Detalhe NF – TranspNome__

Preencher com brancos\.

Campo não obrigatório

Formato: XXX\.\.\.

Tipo: Char

Tamanho: 150

MFS\-14969

RN51

__Regra p/ o campo Detalhe NF – TranspCNPJ__

Preencher com brancos\.

Campo não obrigatório

Formato: XXX\.\.\.

Tipo: Char

Tamanho: 20

MFS\-14969

RN52

__Regra p/ o campo Detalhe NF – TranspEndereço__

Preencher com brancos\.

Campo não obrigatório

Formato: XXX\.\.\.

Tipo: Char

Tamanho: 255

MFS\-14969

RN53

__Regra p/ o campo Detalhe NF – TranspFrete__

Preencher com brancos\.

Campo não obrigatório

Formato: XXX\.\.\.

Tipo: Char

Tamanho: 100

MFS\-14969

RN54

__Regra p/ o campo Detalhe NF – TranspQtd__

Preencher com zeros\.

Campo não obrigatório

Formato: 99999999999999

Tipo: Financeiro

Tamanho: 14

MFS\-14969

RN55

__Regra p/ o campo Detalhe NF – TranspEspécie__

Preencher com brancos\.

Campo não obrigatório

Formato: XXX\.\.\.

Tipo: Char

Tamanho: 50

MFS\-14969

RN56

__Regra p/ o campo Detalhe NF – TranspPLíquido__

Preencher com zeros\.

Campo não obrigatório

Formato: 99999999999999

Tipo: Financeiro

Tamanho: 14

MFS\-14969

RN57

__Regra p/ o campo Detalhe NF – TranspPBruto__

Preencher com zeros\.

Campo não obrigatório

Formato: 99999999999999

Tipo: Financeiro

Tamanho: 14

MFS\-14969

RN58

__Regra p/ o campo Detalhe NF – CasasDecVlrUnitário__

Preencher com fixo “2”\.

Campo obrigatório

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-14969

RN59

__Regra p/ o campo Detalhe NF – CasasDecVlrTotal__

Preencher com fixo “2”\.

Campo obrigatório

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-14969

RN60

__Regra p/ o campo Detalhe NF – OutrosDescontos__

Preencher com o somatório do campo VLR\_DESCONTO da tabela DWT\_ITENS\_SERV\.

Campo não obrigatório

Formato: 99999999999999

Tipo: Financeiro

Tamanho: 14

MFS\-14969

RN61

__Regra p/ o campo Detalhe NF – CcmTomador__

Preencher com o conteúdo do campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR\.

Campo não obrigatório

Formato: 999\.\.\.

Tipo: Numérico

Tamanho: 20

MFS\-14969

RN62

__Regra p/ o campo Detalhe NF – ServicoCidade__

Preencher com o conteúdo do campo DSC\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS referente ao campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\.

Campo não obrigatório

Formato: XXX\.\.\.

Tipo: Char

Tamanho: 100

MFS\-14969

RN63

__Regra p/ o campo Detalhe NF – ServicoEstado__

Preencher com o conteúdo do campo COD\_ESTADO da tabela ESTADO de acordo com o IDENT\_ESTADO da tabela X2097\_MUNIC\_ISS referente ao campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\.

Campo não obrigatório

Formato: XX

Tipo: Char

Tamanho: 2

MFS\-14969

RN64

__Regra p/ o campo Detalhe NF – VlrAproxImposto__

Preencher com zeros\.

*Observação:* Não existe no manual de layout e de orientação informando sobre esse campo\.

Campo não obrigatório

Formato: 99999999999999

Tipo: Financeiro

Tamanho: 14

MFS\-14969

RN65

__Regra p/ o campo Detalhe NF – AliquotaImpostoAprox__

Preencher com zeros\.

Campo não obrigatório

Formato: 99999

Tipo: Financeiro

Tamanho: 5

MFS\-14969

RN66

__Regra p/ o campo Detalhe NF – FonteImpostoAprox__

Preencher com zeros\.

*Observação:* Não existe no manual de layout e de orientação informando sobre esse campo\.

Campo não obrigatório

Formato: 99999999999999

Tipo: Financeiro

Tamanho: 11

MFS\-14969

RN66\.a

__\[EXCLUÍDA – MFS28612\]__

__Regra p/ o campo Detalhe NF – FonteImpostoAprox para o município de Mogi das Cruzes__

Preencher com zeros\.

*Observação:* Não existe no manual de layout e de orientação informando sobre esse campo\.

Campo não obrigatório

Formato: 9999999999

Tipo: Financeiro

Tamanho: 10

MFS24791

MFS28612

RN67

__Regra p/ o campo Detalhe NF – Filler__

Campo livre para futuras informações, preencher com brancos\.

Campo não obrigatório

Formato: XXX\.\.\.

Tipo: Char

Tamanho: 38

MFS\-14969

RN68

__Regra p/ o campo Detalhe Item NF – Tipo de Registro__

Preencher com fixo “2”\.

Campo obrigatório

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-14969

RN69

__Regra p/ o campo Detalhe Item NF – SequenciaNFe__

Preencher com o mesmo sequencial gerado para o Detalhe NF em SequencialNf\.

Campo obrigatório

Formato: 99999999

Tipo: Numérico

Tamanho: 8

MFS\-14969

RN70

__Regra p/ o campo Detalhe Item NF – Item__

Preencher com o conteúdo do campo NUM\_ITEM da tabela DWT\_ITENS\_SERV\.

Campo obrigatório

Formato: 99999999

Tipo: Numérico

Tamanho: 8

MFS\-14969

RN71

__Regra p/ o campo Detalhe Item NF – Qtd__

Preencher com o conteúdo do campo QUANTIDADE da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 2 para ser preenchido de acordo com o tamanho exigido no layout, as 2 últimas posições das casas decimais devem ser desconsideradas;
- Não considerar pontos ou vírgulas;
- Preencher com zeros à esquerda se o tamanho do campo não for atingido\.

*Exemplo:* 99999999999,999999

Campo obrigatório

Formato: 99999999999999

Tipo: Financeiro4

Tamanho: 14

MFS\-14969

RN72

__Regra p/ o campo Detalhe Item NF – Unidade__

Preencher com fixo “UN”\.

Campo obrigatório

Formato: XX

Tipo: Char

Tamanho: 2

MFS\-14969

RN73

__Regra p/ o campo Detalhe Item NF – VlrUnitário__

Preencher com o somatório do campo VLR\_UNIT da tabela DWT\_ITENS\_SERV\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 6 para ser preenchido de acordo com o tamanho exigido no layout;
- Não considerar pontos ou vírgulas;
- Preencher com zeros à esquerda se o tamanho do campo não for atingido\.

*Exemplo:* 999999999999999,99\. Como esse campo é exigido com 9 \(nove\) casas decimais deverá ser gravado o que recuperar do campo \+ 7 \(sete\) casas decimais para completar o seu tamanho, ou seja, 9999999999,99\+9999999\.

Campo obrigatório

Formato: 999\.\.\.

Tipo: Financeiro9

Tamanho: 19

MFS\-14969

RN74

__Regra p/ o campo Detalhe Item NF – VlrTotal__

Preencher com o somatório do campo VLR\_TOT\_NOTA da tabela DWT\_DOCTO\_FISCAL\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 6 para ser preenchido de acordo com o tamanho exigido no layout;
- Não considerar pontos ou vírgulas;
- Preencher com zeros à esquerda se o tamanho do campo não for atingido\.

*Exemplo:* 999999999999999,99\. Como esse campo é exigido com 9 \(nove\) casas decimais deverá ser gravado o que recuperar do campo \+ 7 \(sete\) casas decimais para completar o seu tamanho, ou seja, 9999999999,99\+9999999\.

Campo obrigatório

Formato: 999\.\.\.

Tipo: Financeiro9

Tamanho: 19

MFS\-14969

RN75

__Regra p/ o campo Detalhe Item NF – Descritem__

Preencher com o campo DSC\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na nota fiscal\.

*Observação:* Não é necessário colocar mensagem para esse campo porque como o código da lei 116 também é obrigatório e já irá emitir mensagem, consequentemente ajustando o erro do código ajustará esse campo\.

Campo obrigatório

Formato: XXX\.\.\.

Tipo: Char

Tamanho: 911

MFS\-14969

RN76

__Regra p/ o campo Detalhe Item NF – Filler__

Campo livre para futuras informações, preencher com brancos\.

Campo não obrigatório

Formato: XXX\.\.\.

Tipo: Char

Tamanho: 118

MFS\-14969

RN77

__Regra p/ Recuperar Detalhe Parcela NF__

Esse registro será gerado a partir dos documentos de contas a pagar e contas a receber \(SAXF03, SAFX301, SAFX05 e SAFX501\), referentes às notas fiscais geradas no registro Detalhe NF quando o campo Modelo for igual a “F” e a fatura não for à vista \(campo IND\_FATURA da tabela DWT\_DOCTO\_FISCAL = “2\-A Prazo”\), caso contrário o mesmo não deverá ser considerado, pois só é obrigatório para fatura\.

A identificação dos títulos/ faturas referentes às notas fiscais da SAFX07 é feita da seguinte forma: 

Para as notas de entrada 🡪 pesquisar Contas a Pagar \(SAFX03\)

Para as notas de saída 🡪 pesquisar Contas a Receber \(SAFX05\)

Obter os títulos/ faturas na SAFX03/SAFX05 utilizando a identificação da nota fiscal, através dos seguintes critérios:

- Número, série e subsérie do documento = Número, série e subsérie da NF
- Tipo de documento                                   = Tipo de Documento da NF
- Pessoa Física/Jurídica                              = Pessoa Fis/Jur da NF
- Data de Emissão \(campo 11\) 🡪 a emissão da fatura deve ser >= data emissão da NF
- Data de Movimento \(campo 03\) 🡪 havendo mais de um registro nas condições anteriores deve\-se considerar o registro de < data de movimento; assim, se um mesmo documento for importado mais de uma vez em datas diferentes, iremos considerar apenas o original;
- Código de Operação \(campo 10\) 🡪 considerar apenas os registros em que a operação seja do tipo “C” \(campo 04 da SAXF2001\), que significa “Cadastramento Inicial do Título”\.

MFS\-14969

RN78

__Regra p/ o campo Detalhe Parcela NF – Tipo de Registro__

Preencher com fixo “3”\.

Campo obrigatório se houver

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-14969

RN79

__Regra p/ o campo Detalhe Item NF – SequenciaNFe__

Preencher com o mesmo sequencial gerado para o Detalhe Item NF em SequencialNf\.

Campo obrigatório se houver

Formato: 99999999

Tipo: Numérico

Tamanho: 8

MFS\-14969

RN80

__Regra p/ o campo Detalhe Item NF – NroParcela__

Preencher com o conteúdo do campo NUM\_PARCELA da tabela X301\_TIT\_PAGAR\_PARC nas entradas e X501\_TIT\_RECEBER\_PARC nas saídas\.

Campo obrigatório se houver

Formato: 99

Tipo: Numérico

Tamanho: 2

MFS\-14969

RN81

__Regra p/ o campo Detalhe Item NF – DtVencimento__

Preencher com o conteúdo do campo DATA\_VENCTO da tabela X301\_TIT\_PAGAR\_PARC nas entradas e X501\_TIT\_RECEBER\_PARC nas saídas\.

__Tratamento:__

- Se o campo da data de vencimento da fatura não estiver preenchido em contas a pagar ou a receber, deverá ser gravado com 0 \(zeros\) e emitida a mensagem de log: *“Erro: Favor preencher a data de vencimento referente a fatura <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”\.*

Campo obrigatório se houver

Formato: 99999999 \(DDMMAAAA\)

Tipo: Numérico

Tamanho: 8

MFS\-14969

RN82

__Regra p/ o campo Detalhe Item NF – Valor__

Preencher com o conteúdo do campo VLR\_PARCELA da tabela X301\_TIT\_PAGAR\_PARC nas entradas e X501\_TIT\_RECEBER\_PARC nas saídas\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 4 para ser preenchido de acordo com o tamanho exigido no layout;
- Não considerar pontos ou vírgulas;
- Preencher com zeros à esquerda se o tamanho do campo não for atingido\.

*Exemplo:* 999999999999999,99

Campo obrigatório se houver

Formato: 99999999999999

Tipo: Numérico

Tamanho: 14

MFS\-14969

RN83

__Regra p/ o campo Trailer – Tipo de Registro__

Preencher com fixo “9”\.

Campo obrigatório

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-14969

RN84

__Regra p/ o campo Trailer – QtdNFs__

Totalizar a quantidade de registro “1” gerado no arquivo magnético\.

Campo obrigatório

Formato: 9999

Tipo: Numérico

Tamanho: 4

MFS\-14969

RN85

__Regra p/ o campo Trailer – VlrTotalNfs__

Totalizar com a soma do campo VlrTotalNota de cada registro “1” gerado no arquivo magnético\.

Campo obrigatório

Formato: 99999999999999

Tipo: Financeiro

Tamanho: 14

MFS\-14969

RN86

__Regra p/ o campo Trailer – TotalDeduções__

Totalizar com a soma do campo VlrDeduções de cada registro “1” gerado no arquivo magnético\.

Campo obrigatório

Formato: 99999999999999

Tipo: Financeiro

Tamanho: 14

MFS\-14969

RN87

__Regra p/ o campo Trailer – TotalImpostos__

Totalizar com a soma do campo VlrImposto de cada registro “1” gerado no arquivo magnético\.

Campo obrigatório

Formato: 99999999999999

Tipo: Financeiro

Tamanho: 14

MFS\-14969

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

