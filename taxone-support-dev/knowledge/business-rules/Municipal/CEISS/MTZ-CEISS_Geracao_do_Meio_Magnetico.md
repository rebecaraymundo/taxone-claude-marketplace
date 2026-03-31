# MTZ-CEISS_Geracao_do_Meio_Magnetico

- **Fonte:** MTZ-CEISS_Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2025-11-24
- **Tamanho:** 132 KB

---

<a id="_Hlk46918134"></a>

THOMSON REUTERS

Municipal

CEISS \- Geração do Meio Magnético

 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS40550

Andréa Rocha

Criação do novo módulo que permita a geração do meio magnético CEISS em que serão informados os documentos fiscais de serviço prestados \(emitidos\) e tomados \(recebidos\)\.

MFS75591

Rogério Ohashi

Inclusão dos Campos “Cód\. IBGE do Local de Prestação”, “Cód\. IBGE do Local de Incidência” e Retido no arquivo meio magnético de serviço prestados \(emitidos\) RN42, RN43 e RN44 e tomados \(recebidos\) RN69, RN70 e RN71\.

MFS\-797057

Alessandra Cristina Navatta

Inclusão do município de Barretos/SP no validador CEISS

MFS860767

Andréa Rocha

Alteração da regra de preenchimento dos campos de “Cód\. IBGE do Local de Prestação” e “Cód\. IBGE do Local de Incidência” na geração de serviço prestados \(emitidos\) e tomados \(recebidos\)\. Para tratar a situação do campo código do município preenchido com 7 caracteres, que já está concatenado com o código da UF\.

MFS829438

Graciela Soares

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

MFS\-926148

Rafael Fabiano

Inclusão do município de Catanduva/SP no validador CEISS

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN01

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Votuporanga” deve ficar localizado no grupo “Municipal”\.

MFS40550

RN02

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “57105” \(Votuporanga\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Votuporanga, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

MFS40550

RN03

__Estrutura de menus do módulo Votuporanga:__

Deverão ser criados os seguintes menus e sub\-menus no módulo Votuporanga:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
- Janela
- Ajuda

MFS40550

MFS\-797057

__MFS\-926148__

RN04

__Regra de criação do nome do arquivo__

Deverá ser gerado apenas um arquivo para serviços prestados e tomados\.

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.TXT__, onde:

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.TXT

__CEISS\_MUNICIPIO\_DDMMAAAA\.txt__, onde:

__       CEISS__: representa a obrigação que está sendo gerada\.       

__       MUNICIPIO__: representa o município que está sendo gerado\. Deve ser preenchido com o nome do município selecionado no manager\.

__       DDMMAAAA__: representa a data inicial da geração

       __\.txt__: extensão do arquivo\.

__Ex:__ CEISS\_VOTUPORANGA\_01012010\.txt

Quando o parâmetro Quebrar Arquivos por Data de Emissão estiver marcado deve ser realizado a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente a data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. As nomenclaturas desses arquivos deverão ser:

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\_MMAAAA\.TXT__, onde:

       __DDMMAAAA__: representa a data inicial da geração\.   

__       MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\_012010\.TXT

__CEISS\_MUNICIPIO\_DDMMAAAA\_MMAAAA\.txt__, onde:

__       CEISS__: representa a obrigação que está sendo gerada\.       

__       MUNICIPIO__: representa o município que está sendo gerado\. Deve ser preenchido com o nome do município selecionado no                manager\.

__       DDMMAAAA__: representa a data inicial da geração

         __MMAAAA__: representa a data do período de geração, mês e ano\.

       __\.txt__: extensão do arquivo\.

__Ex:__ CEISS\_VOTUPORANGA\_01022014\_012014\.txt

MFS40550

MFS\-797057

__MFS\-926148__

RN05

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial__: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final__: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Contador__: deve ser exibido através de um ListBox\. Serão listados apenas registros da tabela RESP\_INFORMACAO, cujo o campo IND\_CATEGORIA = 2, 4 ou 6\.

__Gerar Serviços Prestados:__ deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)\.

__Gerar Serviços Tomados:__ deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)\.

__Quebrar arquivo por Data de Emissão__: deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\.

__Estabelecimento__: o sistema deve exibir os estabelecimentos pertencentes ao município de Votuporanga em questão, que estejam licenciados e que o usuário possua acesso no PowerLock\.

MFS40550

MFS\-797057

__MFS\-926148__

RN06

__Regra p/ geração do arquivo magnético__

__Tipos de Registros__

__Registro Tipo 0 – Header:__ O primeiro registro do arquivo contém informações de identificação da empresa\. Deverá existir apenas 1 registro do tipo 0 por arquivo\. 

__Registro Tipo 1 – Serviços Prestados ou Notas Emitidas:__ Registro de detalhamento de nota fiscal emitida, sem limite de ocorrência\.

__Registro Tipo 2\- Serviços Tomados ou Notas Recebidas:__ Registro de detalhamento de nota fiscal recebida, sem limite de ocorrência\. 

__Registro Tipo 3 – Plano de Conta Bancário:__ Registro de detalhamento do plano de contas, sem limite de ocorrência \(Não será gerado\)\.

__Registro Tipo 9 – Trailer:__ O último registro do arquivo contém a quantidade de registros do arquivo\. Deverá existir apenas 1 registro do tipo 9 por arquivo\. 

MFS40550

MFS\-797057

__MFS\-926148__

RN07

__Regra p/ preenchimento dos campos do arquivo magnético__

\- Campos do tipo Data devem estar no formato: AAAAMMDD

\- Campos de valores podem ter um dos formatos: Ex: 1\.20 ou 1,20 ou 120

MFS40550

MFS\-797057

__MFS\-926148__

__Regras para o Registro 0 – Header __

RN08

__Regras p/ campo Código do Registro:__

Preencher com o texto fixo __“0”__\.

Tipo: Numérico

Tamanho: 01 caractere

Campo obrigatório\.

MFS40550

RN09

__Regras p/ campo Quantidade de Registros:__

Preencher com o texto fixo __“00001”__

Tipo: Numérico 

Tamanho: 05 caracteres

Campo obrigatório\.

MFS40550

RN10

__Regras p/ campo Ano Competência:__

Preencher com o ano informado na tela de Geração do Meio Magnético\.

Tipo: Numérico 

Tamanho: 04 caracteres

Campo obrigatório\.

MFS40550

RN11

__Regras p/ campo Mês Competência:__

Preencher com o mês informado na tela de Geração do Meio Magnético\. 

Tipo: Numérico 

Tamanho: 02 caracteres

Campo obrigatório\.

MFS40550

RN12

__Regras p/ campo Inscrição Municipal:__

Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO\.

 

Tipo: Numérico 

Tamanho: 20 caracteres

Campo obrigatório\.

Obs\.: Sem zeros à esquerda\.

MFS40550

RN13

__Regras p/ campo CPF/CNPJ do Contribuinte:__

Preencher com o campo CGC da tabela ESTABELECIMENTO\.

 

Tipo: Numérico 

Tamanho: 14 caracteres

Campo obrigatório\.

Obs\.: Sem máscara, preencher com zeros à esquerda se for CNPJ\.

MFS40550

RN14

__Regras p/ campo Nome do Contribuinte:__

Preencher com o campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO\.

Tipo: Alfanumérico 

Tamanho: 80 caracteres

Campo obrigatório\.

MFS40550

RN15

__Regras p/ campo Simples Nacional:__

Se o campo IND\_ISS da tabela ESTABELECIMENTO = ‘07’

     Preencher com “S”

Senão 

     Preencher com “N”\. 

Tipo: Alfanumérico

Tamanho: 01 caracter

Campo obrigatório\.

MFS40550

RN16

__Regras p/ campo Data da Geração:__

Preencher com a data atual no formato “AAAMMDD”\. 

Tipo: Data 

Tamanho: 8 caracteres

Campo obrigatório\.

MFS40550

RN17

__Regras p/ campo CPF/CNPJ do Contador:__

Preencher com o campo NUM\_CPF da tabela RESP\_INFORMACAO referente ao contador selecionado na tela de geração do meio magnético\.

Se o contador não for informado na tela, preencher com a mesma informação campo CPF/CNPJ do Contribuinte\.

 

Tipo: Numérico 

Tamanho: 14 caracteres

Campo obrigatório\.

Obs\.: Sem máscara, preencher com zeros à esquerda se for CNPJ

MFS40550

RN18

__Regras p/ campo Campo Livre:__

Preencher com o campo espaços\.

Tipo: Alfanumérico 

Tamanho: 361 caracteres

Campo não obrigatório\.

MFS40550

__Regras para o Registro 1 – ESCRITURAÇÃO DE SERVICOS PRESTADOS __

RN19

__Regra geral p/ Registro de Serviços Prestados__

Este registro deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\);
- Classificação do Documento fiscal = 2 ou 3;
- Empresa e estabelecimentos escolhidos na tela de geração;
- Data fiscal dentro do período de referência\.

MFS40550

RN20

__Regras p/ campo Código do Registro:__

Preencher com o texto fixo __“1”__\.

Tipo: Numérico

Tamanho: 01 caractere

Campo obrigatório\.

MFS40550

RN21

__Regras p/ campo Quantidade de Registros:__

Preencher com a sequência da linha gerada para o Registro 1\.

Tipo: Numérico 

Tamanho: 05 caracteres

Campo obrigatório\.

MFS40550

RN22

__Regras p/ campo Modelo Nota:__

Preencher com o campo “DESCRICAO” da tabela X2005\_TIPO\_DOCTO, referente ao campo COD\_DOCTO cadastrado na nota fiscal\.

Tipo: Alfanumérico

Tamanho: 10 caracteres

Campo obrigatório\.

MFS40550

RN23

__Regras p/ campo Série Nota:__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Alfanumérico

Tamanho: 5 caracteres

Campo Obrigatório

MFS40550

RN24

__Regras p/ campo Número Nota:__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Numérico

Tamanho: 07 caracteres

Campo Obrigatório

MFS40550

RN25

__Regras p/ campo Data Emissão Nota:__

Preencher apenas com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Numérico

Tamanho: 08 caracteres

Campo Obrigatório

MFS40550

RN26

__Regras p/ campo Valor da Nota:__

Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

Tipo: Numérico  

Tamanho: 18 caracteres \(2 decimais\)

Campo Obrigatório

MFS40550

RN27

__Regras p/ campo Valor da Dedução:__

Preencher com o campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV\.

Tipo: Numérico  

Tamanho: 18 caracteres \(2 decimais\)

Campo Obrigatório

MFS40550

RN28

__Regras p/ campo Situação da Nota:__

Preencher com:

C – Cancelada, se campo SITUACAO = “S” da SAFX07\.

E – Emitida, se campo SITUACAO = “N” da SAFX07\.

Tipo: Alfanumérico

Tamanho: 01 caracter

Campo Obrigatório

MFS40550

RN29

__Regras p/ campo Código do Serviço:__

__ __

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao campo COD\_SERVICO do serviço cadastrado na nota fiscal\.

Tipo: Alfanumérico  

Tamanho: 05 caracteres

Campo Obrigatório

MFS40550

RN30

__Regras p/ campo Alíquota Simples:__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

Tipo: Numérico

Tamanho: 5 caracteres \(2 decimais\)

Campo Obrigatório 

MFS40550

RN31

__Regras p/ campo CEP Local do Serviço:__

Preencher com o campo COD\_CEP da TACES12 \(DWT\_CEP\) referente ao campo COD\_MUNICIPIO do município cadastrado na nota fiscal\.  O campo deve ser completado com zeros à direita\.

Tipo: Numérico

Tamanho: 8 caracteres 

Campo Obrigatório 

MFS40550

RN32

__Regras p/ campo CPF/CNPJ do Tomador:__

Preencher com o campo CPF\_CGC da SAFX04\.

 

Tipo: Numérico 

Tamanho: 14 caracteres

Campo não obrigatório\.

Obs\.: Sem máscara, preencher com zeros à esquerda se for CNPJ\.

MFS40550

RN33

__Regras p/ campo Inscrição Municipal Tomador:__

Preencher com o campo INSC\_MUNICIPAL da SAFX04\.

Tipo: Numérico

Tamanho: 20 caracteres

Campo não obrigatório\.

Obs\.: Sem zeros à esquerda

MFS40550

RN34

__Regras p/ campo Indefinido:__

Preencher com um espaço em branco\. 

Tipo: Alfanumérico

Tamanho: 01 caracter

MFS40550

RN35

__Regras p/ campo Nome Tomador:__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Alfanumérico

Tamanho: 80 caracteres

Campo não obrigatório\.

MFS40550

RN36

__Regras p/ campo Nome Fantasia do Tomador:__

Preencher com o campo NOME\_FANTASIA da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Alfanumérico

Tamanho: 40 caracteres

Campo não obrigatório\.

MFS40550

RN37

__Regras p/ campo Rua Endereço Tomador:__

Preencher com o campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Alfanumérico

Tamanho: 40 caracteres

Campo não obrigatório\.

MFS40550

RN38

__Regras p/ campo Número Predial Tomador:__

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Numérico

Tamanho: 5 caracteres

Campo não obrigatório\.

MFS40550

RN39

__Regras p/ campo Complemento Tomador:__

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Alfanumérico

Tamanho: 20 caracteres

Campo não obrigatório\.

MFS40550

RN40

__Regras p/ campo Bairro Tomador:__

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Alfanumérico

Tamanho: 40 caracteres

Campo não obrigatório\.

MFS40550

RN41

__Regras p/ campo CEP Tomador:__

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Numérico

Tamanho: 8 caracteres

Campo não obrigatório\.

MFS40550

RN42

__Regra p/ o campo Cód\. IBGE do Local da Prestação__

Se o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for maior que 5 caracteres

     Preencher com o campo COD\_MUNICIPIO da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da tabela 

     DWT\_DOCTO\_FISCAL \(campo 73 \- Código do Município do ISS DA SFX07\)

Senão 

     Preencher com os campos COD\_UF \+ COD\_MUNICIPIO da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da 

     tabela DWT\_DOCTO\_FISCAL \(campo 73 \- Código do Município do ISS DA SFX07\)\. 

  Caso esse campo não esteja preenchido considerar o campo COD\_MUNICIPIO da tabela SAFX04 \(X04\_PESSOA\_FIS\_JUR\)\.

Tipo: Alfanumérico

Tamanho: 7 caracteres

MFS75591/

MFS860767

RN43

__Regra p/ o campo Cód\. IBGE do Local de Incidência__

Se o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for maior que 5 caracteres

     Preencher com o campo COD\_MUNICIPIO da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da tabela 

     DWT\_DOCTO\_FISCAL \(campo 73 \- Código do Município do ISS DA SFX07\)

Senão 

     Preencher com os campos COD\_UF \+ COD\_MUNICIPIO da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da 

     tabela DWT\_DOCTO\_FISCAL \(campo 73 \- Código do Município do ISS DA SFX07\)\. 

  Caso esse campo não esteja preenchido considerar o campo COD\_MUNICIPIO da tabela SAFX04 \(X04\_PESSOA\_FIS\_JUR\)\.

Tipo: Alfanumérico

Tamanho: 7 caracteres

MFS75591/

MFS860767

RN44

__Regra p/ o campo Retido__

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido\.

__    __Preencher com ‘S’\.

__Senão__

    Preencher com ‘N’\.

Tipo: Alfanumérico

Tamanho: 1 caracter

MFS75591

RN45

__Regras p/ campo Livre:__

Preencher com espaços em branco\. 

Tipo: Alfanumérico

Tamanho: 151 caracteres

MFS40550

OS4592

__Regras para o Registro Detalhe – Registro Tipo 2 – ESCRITURAÇÃO DE SERVICOS TOMADOS__

RN46

__Regra geral p/ Registro de Serviços Tomados__

Este registro deve conter todas as notas com as seguintes características:

- Nota de Entrada \(movto\_e\_s <> ‘9’\);
- Classificação do Documento fiscal = 2 ou 3;
- Empresa e estabelecimentos escolhidos na tela de geração;
- Data fiscal dentro do período de referência\.

MFS40550

RN47

__Regras p/ campo Código do Registro:__

Preencher com o texto fixo __“2”__\.

Tipo: Numérico

Tamanho: 01 caractere

Campo obrigatório\.

MFS40550

RN48

__Regras p/ campo Quantidade de Registros:__

Preencher com a sequência da linha gerada para o Registro 2\.

Tipo: Numérico 

Tamanho: 05 caracteres

Campo obrigatório\.

MFS40550

RN49

__Regras p/ campo Modelo Nota:__

Preencher com o campo “DESCRICAO” da tabela X2005\_TIPO\_DOCTO, referente ao campo COD\_DOCTO cadastrado na nota fiscal\.

Tipo: Alfanumérico

Tamanho: 10 caracteres

Campo obrigatório\.

MFS40550

RN50

__Regras p/ campo Série Nota:__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Alfanumérico

Tamanho: 5 caracteres

Campo Obrigatório

MFS40550

RN51

__Regras p/ campo Número Nota:__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Numérico

Tamanho: 07 caracteres

Campo Obrigatório

MFS40550

RN52

__Regras p/ campo Data Emissão Nota:__

Preencher apenas com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Numérico

Tamanho: 08 caracteres

Campo Obrigatório

MFS40550

RN53

__Regras p/ campo Valor da Nota:__

Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

Tipo: Numérico  

Tamanho: 18 caracteres \(2 decimais\)

Campo Obrigatório

MFS40550

RN54

__Regras p/ campo Valor da Dedução:__

Preencher com o campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV\.

Tipo: Numérico  

Tamanho: 18 caracteres \(2 decimais\)

Campo Obrigatório

MFS40550

RN55

__Regras p/ campo Situação da Nota:__

Preencher com:

C \- Cancelada, se campo SITUACAO = “S” da SAFX07\.

E – Emitida, se campo SITUACAO = “N” da SAFX07\.

Tipo: Alfanumérico

Tamanho: 01 caracter

Campo Obrigatório

MFS40550

RN56

__Regras p/ campo Código do Serviço:__

__ __

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao campo COD\_SERVICO do serviço cadastrado na nota fiscal\.

Tipo: Alfanumérico  

Tamanho: 05 caracteres

Campo Obrigatório

MFS40550

RN57

__Regras p/ campo Alíquota Simples:__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

Tipo: Numérico

Tamanho: 5 caracteres \(2 decimais\)

Campo Obrigatório 

MFS40550

RN58

__Regras p/ campo CEP Local do Serviço:__

Preencher com o campo COD\_CEP da TACES12 \(DWT\_CEP\) referente ao campo COD\_MUNICIPIO do município cadastrado na nota fiscal\.  O campo deve ser completado com zeros à direita\.

Tipo: Numérico

Tamanho: 8 caracteres 

Campo Obrigatório 

MFS40550

RN59

__Regras p/ campo CPF/CNPJ do Prestador:__

Preencher com o campo CPF\_CGC da SAFX04\.

 

Tipo: Numérico 

Tamanho: 14 caracteres

Campo obrigatório\.

Obs\.: Sem máscara, preencher com zeros à esquerda se for CNPJ\.

MFS40550

RN60

__Regras p/ campo Inscrição Municipal Prestador:__

Preencher com o campo INSC\_MUNICIPAL da SAFX04\.

Tipo: Numérico

Tamanho: 20 caracteres

Campo obrigatório\.

Obs\.: Sem zeros à esquerda

MFS40550

RN61

__Regras p/ campo Simples Nacional:__

Prestador é optante do Simples Nacional:

Preencher com:

S – Sim\. Se o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR = “S”

Senão preencher com:

N – Não\.

Tipo: Alfanumérico

Tamanho: 01 caracter

Campo obrigatório\.

MFS40550

RN62

__Regras p/ campo Nome Prestador:__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Alfanumérico

Tamanho: 80 caracteres

Campo obrigatório\.

MFS40550

RN63

__Regras p/ campo Nome Fantasia do Prestador:__

Preencher com o campo NOME\_FANTASIA da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Alfanumérico

Tamanho: 40 caracteres

Campo obrigatório\.

MFS40550

RN64

__Regras p/ campo Rua Endereço Prestador:__

Preencher com o campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Alfanumérico

Tamanho: 40 caracteres

Campo obrigatório\.

MFS40550

RN65

__Regras p/ campo Número Predial Prestador:__

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Numérico

Tamanho: 5 caracteres

Campo obrigatório\.

MFS40550

RN66

__Regras p/ campo Complemento Prestador:__

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Alfanumérico

Tamanho: 20 caracteres

Campo não obrigatório\.

MFS40550

RN67

__Regras p/ campo Bairro Prestador:__

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Alfanumérico

Tamanho: 40 caracteres

Campo obrigatório\.

MFS40550

RN68

__Regras p/ campo CEP Prestador:__

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR\. 

Tipo: Numérico

Tamanho: 8 caracteres

Campo obrigatório\.

MFS40550

RN69

__Regra p/ o campo Cód\. IBGE do Local da Prestação__

Se o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for maior que 5 caracteres

     Preencher com o campo COD\_MUNICIPIO da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da tabela 

     DWT\_DOCTO\_FISCAL \(campo 73 \- Código do Município do ISS DA SFX07\)

Senão 

     Preencher com os campos COD\_UF \+ COD\_MUNICIPIO da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da 

     tabela DWT\_DOCTO\_FISCAL \(campo 73 \- Código do Município do ISS DA SFX07\)\. 

  Caso esse campo não esteja preenchido considerar o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

Tipo: Alfanumérico

Tamanho: 7 caracteres

MFS75591/

MFS860767

RN70

__Regra p/ o campo Cód\. IBGE do Local de Incidência__

Se o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for maior que 5 caracteres

     Preencher com o campo COD\_MUNICIPIO da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da tabela 

     DWT\_DOCTO\_FISCAL \(campo 73 \- Código do Município do ISS DA SFX07\)

Senão 

     Preencher com os campos COD\_UF \+ COD\_MUNICIPIO da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da 

     tabela DWT\_DOCTO\_FISCAL \(campo 73 \- Código do Município do ISS DA SFX07\)\. 

  Caso esse campo não esteja preenchido considerar o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

Tipo: Alfanumérico

Tamanho: 7 caracteres

MFS75591/

MFS860767

RN71

__Regra p/ o campo Retido__

Para que esse campo seja preenchido com “S”, será necessário que pelo menos umas das seguintes opções seja verdadeira:

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se

o local da prestação do serviço = município do módulo selecionado;

__OU __

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado;

__OU__

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

__    __Preencher com ‘S’\.

__Senão__

    Preencher com ‘N’\.

Tipo: Alfanumérico

Tamanho: 1 caracter

MFS75591

RN72

__Regras p/ campo Livre:__

Preencher com espaços em branco\. 

Tipo: Alfanumérico

Tamanho: 151 caracteres

MFS40550

OS4592

__Regras para o Registro Detalhe – Registro Tipo 3 – ESCRITURAÇÃO PLANO DE CONTA BANCÁRIO __

RN73

__Regra geral p/ Registro de Escrituração Plano de Conta Bancário__

Este registro não será gerado\.

MFS40550

__Regras para o Registro Detalhe – Registro Tipo 9 – Trailer __

RN74

__Regras p/ campo Código do Registro:__

Preencher com o texto fixo __“9”__\.

Tipo: Numérico

Tamanho: 01 caractere

Campo obrigatório\.

MFS40550

RN75

__Regras p/ campo Quantidade de Registros \(Quantidade de registros constantes do campo 1\.02 e 2\.02\):__

Preencher com o somatório das quantidades de registros dos tipos de registros igual a 1 \(RN21\) e 2 \(RN45\)\.

Tipo: Numérico 

Tamanho: 05 caracteres

Campo obrigatório\.

MFS40550

RN76

__Regras p/ campo Livre:__

Preencher com espaços em branco\. 

Tipo: Alfanumérico

Tamanho: 504 caracteres

MFS40550

RN77

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “5500” \(Barretos\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Barretos, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

MFS\-797057

RN78

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Catanduva” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados e prestados do município de Catanduva”\.

__MFS\-926148__

RN79

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “11102” \(Catanduva\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Catanduva, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-926148__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

