# MTZ-EISS_Barueri-Geracao_do_Meio_Magnetico

- **Fonte:** MTZ-EISS_Barueri-Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2025-10-07
- **Tamanho:** 96 KB

---

THOMSON REUTERS

Municipal

EISS Barueri \- Geração do Meio Magnético

 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4019

Geração do Meio Magnético EISS \- Barueri

Deverá ser criado um novo módulo que permita a geração do meio magnético EISS Barueri em que serão informados os documentos fiscais de serviço prestados \(emitidos\) e tomados \(recebidos\)\.

OS4592

Geração do Meio Magnético EISS \- Barueri

Este documento tem como objetivo alterar a geração do campo Código do Serviço Prestado do Detalhe do Registro Tipo 1 e do campo Código do Serviço Tomado do Detalhe do Registro Tipo 2\.

MFS\-2071

DW \- MUNICIPAL – EISS Barueri – Retirada do range da data inicial e final\.

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

CH8833\_2017 \(MFS\-11046\)

DW \- MUNICIPAL – EISS Barueri – Retirada do Registro Tipo 2 de Serviços Tomados\.

Este documento tem como objetivo alterar a obrigação para não considerar o Registro Tipo 2 de Serviços Tomados, pois conforme contato com a Prefeitura essa informação é feita manualmente no sistema e com opção de importação apenas para Serviços Prestados\.

MFS\-95776

Andréa Rocha

Alteração para considerar somente a geração do Registro Tipo 2 de Serviços Tomados, e não gerar mais as notas de serviços prestados \(Registro Tipo 1\)\. Uma vez que a escrituração das notas fiscais eletrônicas será processada automaticamente com a emissão das respectivas notas fiscais\.

MFS\-829438     

Graciela Soares

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN01

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Barueri” deve ficar localizado no grupo “Municipal”\.

OS4019

RN02

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “5708” \(Barueri\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Barueri, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

OS4019

RN03

__Estrutura de menus do módulo Barueri:__

Deverão ser criados os seguintes menus e sub\-menus no módulo Barueri:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
- Janela
- Ajuda

OS4019

RN04

__Regra de criação do nome do arquivo__

__\[ALTERADA \- CH8833\_2017 \(MFS\-11046\)\]__

__\[MFS95776\] __Alteração para gerar somente notas fiscais de serviços tomados

Deverá ser gerado apenas um arquivo para serviços prestados e__ __tomados\.

O arquivo deverá ser gerado da seguinte forma:

   

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.TXT__, onde:

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.TXT

     __BARUERI\_DDMMAAAA\.txt__, onde:

__     BARUERI: __indica que  é um arquivo do EISS Barueri\.

     __DDMMAAAA__: data inicial da geração\.

     \.__txt__: extensão do arquivo\.

OS4019

CH8833\_2017 \(MFS\-11046\)

MFS95776

MFS829438

RN05

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

Data Inicial: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

Data Final: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

Tipo de Operação:__ __O campo deve ser tipo combo com as seguintes opções: “Inclusão”, “Alteração” e “Exclusão”\. Valor default: Inclusão\. Campo de preenchimento obrigatório, caso o usuário não informe valor para este campo, exibir mensagem de preenchimento obrigatório\.

Identificação da Remessa:__ __O campo deve ser um text Box\.__ __O campo deve permitir que o usuário digite o sequencial desejado, com no máximo 11 posições\. Campo de preenchimento obrigatório, caso o usuário não informe valor para este campo, exibir mensagem de preenchimento obrigatório\.

Estabelecimento: o sistema deve exibir os estabelecimentos pertencentes ao município de Barueri, que estejam licenciados e que o usuário possua acesso no PowerLock\.

OS4019

MFS\_2071

__Regras para o Registro Cabeçalho – Registro Tipo 0 – Segmento 00 – Identificação do Contribuinte__

RN06

__Regras p/ campo Tipo do Registro:__

Preencher com o texto fixo __“000”__\.

Tipo: Numérico

Tamanho: 03 caracteres

OS4019

RN07

__Regras p/ campo Inscrição do Contribuinte:__

Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO\.

Tipo: Numérico 

Tamanho: 07 caracteres

OS4019

RN08

__Regras p/ campo Ano Competência:__

Preencher com o ano informado na tela de Geração do Meio Magnético\.

Tipo: Numérico 

Tamanho: 04 caracteres

RN09

__Regras p/ campo Mês Competência:__

Preencher com o mês informado na tela de Geração do Meio Magnético\. 

Tipo: Numérico 

Tamanho: 02 caracteres

RN10

__Regras p/ campo Identificação da Remessa do Contribuinte:__

Identificação do arquivo por Contribuinte\. A identificação da Remessa é livre desde que seja exclusiva e única\. É um número de controle informado pelo contribuinte\.

Sugestão de preenchimento:

aaaammddxxx sendo:

aaaammdd = ano\+mês\+dia 

xxx = número da Remessa 

Exemplo:  20131125123

__OBS: __O exemplo de preenchimento acima é apenas sugestão\. Lembrando que a identificação da Remessa é livre desde que seja exclusiva/única\.

\- Preencher com o campo “Identificação da Remessa” da tela de geração do meio magnético\.

Será um sequencial numérico por arquivo gerado\. 

 

Tipo: Numérico 

Tamanho: 11 caracteres

RN11

__Regras p/ campo Versão do Lay\-Out:__

Preencher com o texto fixo __“V100”__\.

Tipo: Texto 

Tamanho: 04 caracteres

RN12

__Regras p/ campo Fim de Linha:__

Caractere de fim de linha\. Preencher com ASC13 __/__ ASC10\.

Tipo: ASCII\(13\)\+ASCII\(10\)

Tamanho: 01 caracter

__Regras para o Registro Cabeçalho – Registro Tipo 1 – Segmento 00 – Identificação de Declaração de Serviços Prestados__

RN13

__Regra geral p/ Registro de Serviços Prestados__

Este registro deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\);
- Classificação do Documento fiscal = 2 ou 3;
- Empresa e estabelecimentos escolhidos na tela de geração;
- Data fiscal dentro do período de referência\.

OS4019

RN14

__Regras p/ campo Tipo do Registro:__

Preencher com o texto fixo __“100”__\.

Tipo: Numérico

Tamanho: 03 caracteres

OS4019

RN15

__Regras p/ campo Identificação do Tipo de Serviço:__

Preencher com o texto fixo __“__SERVICO PRESTADO__”__\.

Tipo: Texto

Tamanho: 16 caracteres

OS4019

RN16

__Regras p/ campo Fim de Linha:__

Caractere de fim de linha\. Preencher com ASC13 __/__ ASC10\.

Tipo: ASCII\(13\)\+ASCII\(10\)

Tamanho: 01 caracter

OS4019

__Regras para o Registro Detalhe – Registro Tipo 1 – Segmento 01 – Informações de Serviços Prestados__

RN17

__Regras p/ campo Tipo do Registro:__

Preencher com o texto fixo __“101”__\.

Tipo: Numérico

Tamanho: 03 caracteres

OS4019

RN18

__Regras p/ campo Tipo de Operação:__

Preencher com a opção escolhida no campo “Tipo de Operação” da tela de geração do meio magnético\.

Opção Inclusão, preencher com “__1__”\.   

Opção Alteração, preencher com “__2__”\.

Opção Exclusão, preencher com “__3__”\.

Tipo: Numérico

Tamanho: 01 caracter

OS4019

RN19

__Regras p/ campo Código do Tipo do Documento:__

Preencher com o campo “Modelo EISS Barueri” da tela Parâmetros por Município / Parâmetros / Modelo Msaf x Modelo, referente ao modelo cadastrado na nota fiscal\.

Tipo: Numérico

Tamanho: 03 caracteres

OS4019

RN20

__Regras p/ campo Série Documento:__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. Caso não houver série na nota, deixar em branco\.

Tipo: Texto

Tamanho: 10 caracteres

Campo Não Obrigatório

OS4019

RN21

__Regras p/ campo Número Documento:__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Numérico

Tamanho: 09 caracteres

OS4019

RN22

__Regras p/ campo Dia Emissão Documento:__

Indica o dia da emissão do documento\. Preencher apenas com o dia do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Numérico

Tamanho: 02 caracteres

OS4019

RN23

__Regras p/ campo Documento Cancelado:__

Preencher com:

__1__ – Sim, se campo SITUACAO = “S” da SAFX07\.

__2__ – Não, se campo SITUACAO = “N” da SAFX07\.

Tipo: Numérico

Tamanho: 01 caracter

OS4019

RN24

__Regras p/ campo Tomador do Serviço Estrangeiro:__

Preencher com:

__1__ – Sim\. Quando o campo UF da tabela x04\_PESSOA\_FIS\_JUR estiver preenchido com “EX”\.

Senão, preencher com  __2__ – Não\.  

Tipo: Numérico

Tamanho: 01 caracter

OS4019

RN25

__Regras p/ campo Indicador do CPF/CNPJ do Tomador:__

__1__ – CPF\. Preencher quando o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR, tiver 11 posições\. 

__2__ – CNPJ\. Preencher quando o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR, tiver 14 posições\. 

Tipo: Numérico

Tamanho: 01 caracter

OS4019

RN26

__Regras p/ campo CPF/CNPJ Tomador do Serviço:__

Preencher com campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR\. 

Obs\.: Não preencher quando tomador for estrangeiro\.

Tipo: Numérico

Tamanho: 14 caracteres

OS4019

RN27

__Regras p/ campo Razão Social/Nome Tomador:__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Texto

Tamanho: 100 caracteres

OS4019

RN28

__Regras p/ campo UF Logradouro Tomador:__

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao IDENT\_ESTADO da tabela X04\_PESSOA\_FIS\_JUR\.

Tipo: Texto  Tamanho: 02 caracteres

OS4019

RN29

__Regras p/ campo Cidade Logradouro Tomador:__

Preencher com o campo CIDADE da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Texto  

Tamanho: 40 caracteres

OS4019

RN30

__Regras p/ campo Código do Serviço Prestado:__

__\[ALTERADA – OS4592\]__

Preencher com o campo Serviço da tela Municipal – Parametros por Município – Parâmetros – Serviço Msaf x Serviço referente ao serviço cadastrado na nota fiscal\.

Obrigatório somente para documentos Não cancelados ou Cancelados com Motivo de Cancelamento 001 \- Cancelamento do Serviço / 002 \- Dados Incorretos, caso contrário poderá gerar com o código do serviço ou com zeros\.

Se não houver parametrização para o serviço cadastrado na nota fiscal, deve ser exibida a seguinte mensagem de log: “O serviço não foi parametrizado na tela Parâmetros por Município – Parâmetros – Serviço Msaf x Serviço\. Favor verificar\.”\.

__Tratamentos:__

- Desconsiderar pontuação \(\.\) e hífen \(\-\) do código do serviço gerado\. __Exemplo:__ Serviço 01\.01\.01\.1\.1\-5 gerar 010101115\.
- Se não houver parametrização para o serviço cadastrado na nota fiscal gerar o campo com “000000000”\.

__*Obs\.: *__*O controle dos serviços é inteiramente responsabilidade do usuário fiscal\.*

Tipo: Numérico  

Tamanho: 09 caracteres

OS4019

OS4592

RN31

__Regras p/ campo Exportação:__

Preencher com:

__1__ – Sim\. Quando o campo “Tomador do Serviço Estrangeiro” existente neste arquivo, estiver preenchido com “EX”\.

Senão, preencher com __2__ – Não\.

Tipo: Numérico  

Tamanho: 01 caracter

OS4019

RN32

__Regras p/ campo Valor do Documento:__

Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

Tipo: Numérico  

Tamanho: Valor com 15 posições com zeros a esquerda, sem vírgula e sem ponto\.

Exemplo: R$10,25 = 000000000001025

OS4019

RN33

__Regras p/ campo Valor Não Incluso na Base de Cálculo:__

Não será tratado, informa zeros\.

Tipo: Numérico  

Tamanho: Valor com 15 posições\.

OS4019

RN34

__Regras p/ campo Imposto Retido:__

__Retido__

Para que esse campo seja preenchido com __“1”\- __SIM__,__ é necessário que pelo menos umas das seguintes opções seja verdadeira:

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido , recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “2" e se

o local da prestação do serviço = município do módulo selecionado OU; 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU;

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado \. 

__Não Retido__

Caso nenhuma das opões seja verdadeira, preencher com __“2”\- __NÂO__\.__

Tipo: Numérico  

Tamanho: 01 caracter 

OS4019

RN35

__Regras p/ campo Fim de Linha:__

Caractere de fim de linha\. Preencher com ASC13 __/__ ASC10\.

Tipo: ASCII\(13\)\+ASCII\(10\)

Tamanho: 01 caracter

OS4019

__Regras para o Registro Detalhe – Registro Tipo 1 – Segmento 02 – Informações do Cancelamento__

RN36

__Regras p/ campo Tipo do Registro:__

Preencher com o texto fixo __“102”__\.

Tipo: Numérico

Tamanho: 03 caracteres

OS4019

RN37

__Regras p/ campo Código Motivo do Cancelamento:__

Preencher com o código do campo  138 \-“COD\_MOTIVO” da tabela SAFX07\. 

Os códigos são cadastrados manualmente pelo usuário na tela “DW / Manutenção / Cadastros /  Motivo de Cancelamento e Extravio de NF\. É Preenchido de acordo com a tabela de Motivos de Cancelamento estipulada por cada Município\.

Códigos do Município de Barueri:

001 – Cancelamento do Serviço

002 – Dados Incorretos

003 – Substituição

004 – Documento Rejeitado pelo Tomador

005 – Documento Inutilizado

Tipo: Numérico

Tamanho: 03 caracteres

OS4019

RN38

__Regras p/ campo Descrição do Cancelamento:__

Preencher com a informação do campo  140 \-“ OBS\_COMPL\_MOTIVO” da tabela SAFX07\. 

Tipo: Texto

Tamanho: 200 caracteres

OS4019

RN39

__Regras p/ campo Fim de Linha:__

Caractere de fim de linha\. Preencher com ASC13 __/__ ASC10\.

Tipo: ASCII\(13\)\+ASCII\(10\)

Tamanho: 01 caracter

OS4019

__Regras para o Registro Detalhe – Registro Tipo 1 – Segmento 03 – Somente para atividades relacionadas nas exceções__

RN40

__Regras p/ campo Tipo do Registro:__

Preencher com o texto fixo __“103”__\.

Tipo: Numérico

Tamanho: 03 caracteres

OS4019

RN41

__Regras p/ campo Local da Prestação do Serviço:__

Preencher com:

__1 __\- Para serviço prestado no Município\. Verificar se o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é igual ao município informado no campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\. 

Senão, preencher com:

__2__ \- para serviço prestado fora do Município\.

Tipo: Numérico

Tamanho: 01 caracteres

OS4019

RN42

__Regras p/ campo Local da Prestação do Serviço diferente do Endereço do Tomador:__

Preencher com:

__1 – __Sim\. Deve verificar se o municipio informado na capa da nota, COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é <> do municipio do tomador CIDADE da tabela X04\_PESSOA\_FIS\_JUR\. 

Senão, preencher com:

__2__ – Não\. 

Tipo: Numérico

Tamanho: 01 caracteres

OS4019

RN43

__Regras p/ campo Serviço Prestado em Vias Publicas:__

Preencher com:

__1 – __Sim\. Quando o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 for referente ao código 702 ou 705\.

Senão preencher com:

__2__ – Não\. 

Tipo: Numérico

Tamanho: 01 caracteres

OS4019

RN44

__Regras p/ campo Fim de Linha:__

Caractere de fim de linha\. Preencher com ASC13 __/__ ASC10\.

Tipo: ASCII\(13\)\+ASCII\(10\)

Tamanho: 01 caracter

OS4019

__Regras para o Registro Detalhe – Registro Tipo 1 – Segmento 04 __

RN45

__Regras p/ o Registro Tipo 1 – Segmento 4:__

As informações deste registro, deverão ser informadas apenas quando o tipo de Serviço do campo “Código do Serviço Prestado”, for igual a 702 e 705\.__ __

Caso contrário não informar o Segmento 04\.

OS4019

RN46

__Regras p/ campo Tipo do Registro:__

Preencher com o texto fixo __“104”__\.

Tipo: Numérico

Tamanho: 03 caracteres

OS4019

RN47

__Regras p/ campo Endereço Logradouro do local do Serviço Prestado:__

Preencher com o campo TP\_LOGRADOURO da tabela X04\_PESSOA\_FIS\_JUR \+ o campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\.

Tipo: Texto

Tamanho: 100 caracteres

OS4019

RN48

__Regras p/ campo Numero Logradouro do local do Serviço Prestado:__

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\.

Tipo: Texto

Tamanho: 10 caracteres

OS4019

RN49

__Regras p/ campo Complemento Logradouro do local do Serviço Prestado:__

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\.

Tipo: Texto

Tamanho: 20 caracteres

OS4019

RN50

__Regras p/ campo Bairro Logradouro do local do Serviço Prestado:__

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR\.

Tipo: Texto

Tamanho: 60 caracteres

OS4019

RN51

__Regras p/ campo Cidade Logradouro do local do Serviço Prestado:__

Preencher com o campo CIDADE da tabela X04\_PESSOA\_FIS\_JUR\.

Tipo: Texto

Tamanho: 40 caracteres

OS4019

RN52

__Regras p/ campo UF Logradouro do local do Serviço Prestado:__

Preencher com o campo COD\_ESTADO da tabela ESTADO, referente ao IDENT\_ESTADO da tabela X04\_PESSOA\_FIS\_JUR\.

Tipo: Texto

Tamanho: 02 caracteres

OS4019

RN53

__Regras p/ campo CEP Logradouro do local do Serviço Prestado:__

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR\.

Obs\.: Deverá considerar “zeros significativos” a esquerda\. 

Tipo: Numérico

Tamanho: 08 caracteres

OS4019

RN54

__Regras p/ campo Fim de Linha:__

Caractere de fim de linha\. Preencher com ASC13 __/__ ASC10\.

Tipo: ASCII\(13\)\+ASCII\(10\)

Tamanho: 01 caracter

OS4019

__Regras para o Registro Rodapé – Registro Tipo 1 – Segmento 99 – Totalização Declaração de Serviços Prestados __

RN55

__Regras p/ campo Tipo do Registro:__

Preencher com o texto fixo __“199”__\.

Tipo: Numérico

Tamanho: 03 caracteres

OS4019

RN56

__Regras p/ campo Total dos Serviços Prestados contido nos Registros Tipo 1:__

Preencher com o Total dos Serviços Prestados contido nos Registros Tipo 1 \- Segmento 01\. Preencher com a informação do campo “Valor do Documento”, do segmento 01\.

Valor com 15 posições com zeros a esquerda, sem vírgula e sem ponto\.

Exemplo: R$10,25 = 000000000001025

Tipo: Numérico

Tamanho: 15 caracteres

OS4019

RN57

__Regras p/ campo Total dos Valores Não Incluso na Base de Calculo contido nos Registros Tipo 1:__

Não será tratado, informar zeros\.

Tipo: Numérico

Tamanho: 15 caracteres

OS4019

RN58

__Regras p/ campo Fim de Linha:__

Caractere de fim de linha\. Preencher com ASC13 __/__ ASC10\.

Tipo: ASCII\(13\)\+ASCII\(10\)

Tamanho: 01 caracter

OS4019

__\[ALTERADA \- CH8833\_2017 \(MFS\-11046\): Exclusão do Registro Tipo 2 – Serviços Tomados, pois o mesmo é preenchido de forma manual no validador\]__

__\[MFS95776\] __Alteração para gerar somente notas fiscais de serviços tomados

__Regras para o Registro Cabeçalho – Registro Tipo 2 – Segmento 00 – Identificação de Declaração de Serviços Tomados__

RN59

__Regra geral p/ Registro de Serviços Tomados__

Este registro deve conter todas as notas com as seguintes características:

- Documentos de Entradas: \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Não deve recuperar notas canceladas\.

 Quando a nota não tiver itens não deve ser recuperada\. 

OS4019

RN60

__Regras p/ campo Tipo do Registro:__

Preencher com o texto fixo __“200”__\.

Tipo: Numérico

Tamanho: 03 caracteres

OS4019

RN61

__Regras p/ campo Idedntificação do Tipo de Serviço:__

Preencher com o texto fixo __“__SERVICO TOMADO__”__\.

Tipo: Texto

Tamanho: 14 caracteres

OS4019

RN62

__Regras p/ campo Fim de Linha:__

Caractere de fim de linha\. Preencher com ASC13 __/__ ASC10\.

Tipo: ASCII\(13\)\+ASCII\(10\)

Tamanho: 01 caracter

OS4019

__Regras para o Registro Detalhe – Registro Tipo 2 – Segmento 01 – Informações de Serviços Tomados__

RN63

__Regras p/ campo Tipo do Registro:__

Preencher com o texto fixo __“201”__\.

Tipo: Numérico

Tamanho: 03 caracteres

OS4019

RN64

__Regras p/ campo Tipo de Operação:__

Preencher com a opção escolhida no campo “Tipo de Operação” da tela de geração do meio magnético\.

Opção Inclusão, preencher com “__1__”\.

Opção Alteração, preencher com “__2__”\.

Opção Exclusão, preencher com “__3__”\.

Tipo: Numérico

Tamanho: 01 caracter

OS4019

RN65

__Regras p/ campo Código do Tipo do Documento:__

Preencher com o campo “Modelo EISS Barueri” da tela Parâmetros por Município / Parâmetros / Modelo Msaf x Modelo, referente ao modelo cadastrado na nota fiscal\.

Tipo: Numérico

Tamanho: 03 caracteres

OS4019

RN66

__Regras p/ campo Série Documento:__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. Caso não houver série na nota, deixar em branco\.

Tipo: Texto

Tamanho: 10 caracteres

Campo Não Obrigatório

OS4019

RN67

__Regras p/ campo Número Documento:__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Numérico

Tamanho: 09 caracteres

OS4019

RN68

__Regras p/ campo Dia Emissão Documento:__

Indica o dia da emissão do documento\. Preencher apenas com o dia do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Numérico

Tamanho: 02 caracteres

OS4019

RN69

__Regras p/ campo Reservado:__

Deverá preencher com o texto fixo “__0__”\.

Tipo: Numérico

Tamanho: 01 caracter

OS4019

RN70

__Regras p/ campo Prestador do Serviço Estrangeiro:__

Preencher com:

__1__ – Sim\. Quando o campo UF da tabela x04\_PESSOA\_FIS\_JUR estiver preenchido com “EX”\.

Senão, preencher com  __2__ – Não\.  

Tipo: Numérico

Tamanho: 01 caracter

OS4019

RN71

__Regras p/ campo Indicador do CPF/CNPJ do Prestador:__

__1__ – CPF\. Preencher quando o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR, tiver 11 posições\. 

__2__ – CNPJ\. Preencher quando o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR, tiver 14 posições\. 

Tipo: Numérico

Tamanho: 01 caracter

OS4019

RN72

__Regras p/ campo CPF/CNPJ Prestador do Serviço:__

Preencher com campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Numérico

Tamanho: 14 caracteres

OS4019

RN73

__Regras p/ campo Razão Social/Nome Prestador:__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Texto

Tamanho: 100 caracteres

OS4019

RN74

__Regras p/ campo UF Logradouro Prestador:__

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao IDENT\_ESTADO da tabela X04\_PESSOA\_FIS\_JUR\.

Tipo: Texto  Tamanho: 02 caracteres

OS4019

RN75

__Regras p/ campo Cidade Logradouro Prestador:__

Preencher com o campo CIDADE da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Texto  

Tamanho: 40 caracteres

OS4019

RN76

__Regras p/ campo Código do Serviço Tomado:__

__\[ALTERADA – OS4592\]__

Preencher com o campo Serviço da tela Municipal – Parametros por Município – Parâmetros – Serviço Msaf x Serviço referente ao serviço cadastrado na nota fiscal\.

Se não houver parametrização para o serviço cadastrado na nota fiscal, deve ser exibida a seguinte mensagem de log: “O serviço não foi parametrizado na tela Parâmetros por Município – Parâmetros – Serviço Msaf x Serviço\. Favor verificar\.”\.

__Tratamentos:__

- Desconsiderar pontuação \(\.\) e hífen \(\-\) do código do serviço gerado\. __Exemplo:__ Serviço 01\.01\.01\.1\.1\-5 gerar 010101115\.
- Se não houver parametrização para o serviço cadastrado na nota fiscal gerar o campo com “000000000”\.

Tipo: Numérico  

Tamanho: 09 caracteres

OS4019

OS4592

RN77

__Regras p/ campo Importação:__

Preencher com:

__1__ – Sim\. Quando o campo “Prestador do Serviço Estrangeiro” existente neste arquivo, estiver preenchido com “EX”\.

Senão, preencher com __2__ – Não\.

Tipo: Numérico  

Tamanho: 01 caracter

OS4019

RN78

__Regras p/ campo Valor do Documento:__

Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

Tipo: Numérico  

Tamanho: Valor com 15 posições com zeros a esquerda, sem vírgula e sem ponto\.

Exemplo: R$10,25 = 000000000001025

OS4019

RN79

__Regras p/ campo Valor Não Incluso na Base de Cálculo:__

Não será tratado, informa zeros\.

Tipo: Numérico  

Tamanho: Valor com 15 posições\.

OS4019

RN80

__Regras p/ campo Imposto Retido:__

__Retido__

Para que esse campo seja preenchido com __“1”\- __SIM__,__ é necessário que pelo menos umas das seguintes opções seja verdadeira:

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido , recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se

o local da prestação do serviço = município do módulo selecionado OU; 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU;

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado \. 

__Não Retido__

Caso nenhuma das opões seja verdadeira, preencher com __“2”\- __NÃO__\.__

Tipo: Numérico  

Tamanho: 01 caracter

OS4019

RN81

__Regras p/ campo Fim de Linha:__

Caractere de fim de linha\. Preencher com ASC13 __/__ ASC10\.

Tipo: ASCII\(13\)\+ASCII\(10\)

Tamanho: 01 caracter

OS4019

__Regras para o Registro Detalhe – Registro Tipo 2 – Segmento 02 – Atividades Relacionadas Simples Nacional__

RN82

__Regras p/ campo Tipo do Registro:__

Preencher com o texto fixo __“202”__\.

Tipo: Numérico

Tamanho: 03 caracteres

OS4019

RN83

__Regras p/ campo Prestador é optante do Simples Nacional:__

Preencher com:

__1 __–__ __Sim\. Se o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR = “__S__”

Senão preencher com__:__

__2 __– Não\.

Tipo: Numérico

Tamanho: 01 caracteres

OS4019

RN84

__Regras p/ campo Alíquota Simples Nacional:__

Se o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR estiver marcado como  “__S__”, recuperar a informação do campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

Alíquotas validas para optantes do simples Nacional:

Se  alíquota inserida for 2,79%, deverá preencher o campo com 0279;

Se  alíquota inserida for 3,50%, deverá preencher o campo com 0350;

Se  alíquota inserida for 3,84%, deverá preencher o campo com 0384;

Se  alíquota inserida for 3,87%, deverá preencher o campo com 0387;

Se  alíquota inserida for 4,23%, deverá preencher o campo com 0423;

Se  alíquota inserida for 4,26%, deverá preencher o campo com 0426;

Se  alíquota inserida for 4,31%, deverá preencher o campo com 0431;

Se  alíquota inserida for 4,61%, deverá preencher o campo com 0461;

Se  alíquota inserida for 4,65%, deverá preencher o campo com 0465;

Se  alíquota inserida for 5,00%, deverá preencher o campo com 0500\.

Caso a alíquota inserida não for uma alíquota válida para o optante do Simples Nacional, deverá exibir a seguinte mensagem no Log: "Valor da alíquota, não é válida para optantes do Simples Nacional\.”

Senão, caso o prestador não for do Simples Nacional, preencher com zeros\.

Tipo: Numérico

Tamanho: 04 caracteres, com zeros a esquerda e sem vírgula\.

OS4019

RN85

__Regras p/ campo Fim de Linha:__

Caractere de fim de linha\. Preencher com ASC13 __/__ ASC10\.

Tipo: ASCII\(13\)\+ASCII\(10\)

Tamanho: 01 caracter

OS4019

__Regras para o Registro Detalhe – Registro Tipo 2 – Segmento 03 – Somente para atividades relacionadas nas exceções__

RN86

__Regras p/ campo Tipo do Registro:__

Preencher com o texto fixo __“203”__\.

Tipo: Numérico

Tamanho: 03 caracteres

OS4019

RN87

__Regras p/ campo Local da Prestação do Serviço:__

Preencher com:

__1 __\- Para serviço prestado no Município\. Verificar se o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é igual ao município informado no campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\. 

Senão, preencher com:

__2__ \- para serviço prestado fora do Município\.

Tipo: Numérico

Tamanho: 01 caracteres

OS4019

RN88

__Regras p/ campo Local da Prestação do Serviço diferente do Endereço do Tomador:__

Preencher com:

__1 – __Sim\. Deve verificar se o municipio informado na capa da nota, COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é <> do municipio do tomador CIDADE da tabela ESTABELECIMENTO\. 

Senão, preencher com:

__2__ – Não\. 

Tipo: Numérico

Tamanho: 01 caracteres

OS4019

RN89

__Regras p/ campo Serviço Prestado em Vias Publicas:__

Preencher com:

__1 – __Sim\. Quando o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 for referente ao código 702 ou 705\.

Senão preencher com:

__2__ – Não\. 

Tipo: Numérico

Tamanho: 01 caracteres

OS4019

RN90

__Regras p/ campo Fim de Linha:__

Caractere de fim de linha\. Preencher com ASC13 __/__ ASC10\.

Tipo: ASCII\(13\)\+ASCII\(10\)

Tamanho: 01 caracter

OS4019

__Regras para o Registro Detalhe – Registro Tipo 2 – Segmento 04 __

RN91

__Regras p/ o Registro Tipo 2 – Segmento 4:__

As informações deste registro, deverão ser informadas apenas quando o tipo de Serviço do campo “Código do Serviço Prestado”, for igual a 702 e 705\.__ __

Caso contrário não informar o Segmento 04\.

OS4019

RN92

__Regras p/ campo Tipo do Registro:__

Preencher com o texto fixo __“204”__\.

Tipo: Numérico

Tamanho: 03 caracteres

OS4019

RN93

__Regras p/ campo Endereço Logradouro do local do Serviço:__

Preencher com o campo TP\_LOGRADOURO da tabela ESTABELECIMENTO \+ o campo ENDERECO da tabela ESTABELECIMENTO\.

Tipo: Texto

Tamanho: 100 caracteres

OS4019

RN94

__Regras p/ campo Numero Logradouro do local do Serviço:__

Preencher com o campo NUM\_ENDERECO da tabela ESTABELECIMENTO\.

Tipo: Texto

Tamanho: 10 caracteres

OS4019

RN95

__Regras p/ campo Complemento Logradouro do local do Serviço:__

Preencher com o campo COMPL\_ENDERECO da tabela ESTABELECIMENTO\.

Tipo: Texto

Tamanho: 20 caracteres

OS4019

RN96

__Regras p/ campo Bairro Logradouro do local do Serviço:__

Preencher com o campo BAIRRO da tabela ESTABELECIMENTO\.

Tipo: Texto

Tamanho: 60 caracteres

OS4019

RN97

__Regras p/ campo Cidade Logradouro do local do Serviço:__

Preencher com o campo CIDADE da tabela ESTABELECIMENTO\.

Tipo: Texto

Tamanho: 40 caracteres

OS4019

RN98

__Regras p/ campo UF Logradouro do local do Serviço Prestado:__

Preencher com o campo COD\_ESTADO da tabela ESTADO, referente ao IDENT\_ESTADO da tabela ESTABELECIMENTO\.

Tipo: Texto

Tamanho: 02 caracteres

OS4019

RN99

__Regras p/ campo CEP Logradouro do local do Serviço:__

Preencher com o campo CEP da tabela ESTABELECIMENTO\.

Obs\.: Deverá considerar “zeros significativos” a esquerda\. 

Tipo: Numérico

Tamanho: 08 caracteres

OS4019

RN100

__Regras p/ campo Fim de Linha:__

Caractere de fim de linha\. Preencher com ASC13 __/__ ASC10\.

Tipo: ASCII\(13\)\+ASCII\(10\)

Tamanho: 01 caracter

OS4019

__Regras para o Registro Rodapé – Registro Tipo 2 – Segmento 99 – Totalização Declaração de Serviços Tomados __

RN101

__Regras p/ campo Tipo do Registro:__

Preencher com o texto fixo __“299”__\.

Tipo: Numérico

Tamanho: 03 caracteres

OS4019

RN102

__Regras p/ campo Total dos Serviços Tomados contido nos Registros Tipo 2:__

Preencher com o Total dos Serviços Prestados contido nos Registros Tipo 2 \- Segmento 01\. Preencher com a informação do campo “Valor do Documento”, do segmento 01\.

Valor com 15 posições com zeros a esquerda, sem vírgula e sem ponto\.

Exemplo: R$10,25 = 000000000001025

Tipo: Numérico

Tamanho: 15 caracteres

OS4019

RN103

__Regras p/ campo Total dos Valores Não Incluso na Base de Calculo contido nos Registros Tipo 2:__

Não será tratado, informa zeros\. 

Tipo: Numérico  

Tamanho: Valor com 15 posições\.

OS4019

RN104

__Regras p/ campo Fim de Linha:__

Caractere de fim de linha\. Preencher com ASC13 __/__ ASC10\.

Tipo: ASCII\(13\)\+ASCII\(10\)

Tamanho: 01 caracter

OS4019

__Regras para o Registro Rodapé – Registro Tipo 9 – Segmento 00 – Encerramento do Arquivo__

RN105

__Regras p/ campo Tipo do Registro:__

Preencher com o texto fixo __“900”__\.

Tipo: Numérico

Tamanho: 03 caracteres

OS4019

RN106

__Regras p/ campo Número Total de Linhas do Arquivo:__

Preencher com o total de número de linhas do arquivo\.

Tipo: Numérico

Tamanho: 07 caracteres

OS4019

RN107

__Regras p/ campo Valor Total dos Serviços contidos no Arquivo:__

Recuperar a soma dos valores dos serviços \(campo Valor do Documento\) das linhas do registro Detalhe contidas no arquivo\.

Valor com 15 posições com zeros à esquerda, sem vírgula e sem ponto\.

Exemplo: R$10,25 = 000000000001025

Tipo: Numérico

Tamanho: 15 caracteres

OS4019

RN108

__Regras p/ campo Valor Total dos Valores não Incluso na Base de Cálculo contidos no Arquivo:__

Não será tratado, informa zeros\.

Tipo: Numérico  

Tamanho: Valor com 15 posições\.

OS4019

RN109

__Regras p/ campo Fim de Linha:__

Caractere de fim de linha\. Preencher com ASC13 __/__ ASC10\.

Tipo: ASCII\(13\)\+ASCII\(10\)

Tamanho: 01 caracter

OS4019

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

