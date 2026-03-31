# MTZ-Duque_de_Caxias-Geracao_do_Meio_Magnetico

- **Fonte:** MTZ-Duque_de_Caxias-Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 53 KB

---

# Duque de Caxias \- Geração do Meio Magnético

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3767

Duque de Caxias \- Geração do Meio Magnético

Este documento tem por objetivo criar o novo módulo “Duque de Caxias – Declaração de Notas Convencionais Recebidas” que irá gerar o meio magnético permitindo a importação de notas fiscais convencionais recebidas para o Sistema de Notas Fiscais de Serviço Eletrônicas\.

__MFS\_2071__

DW \- MUNICIPAL – Duque de Caxias – Retirada do range da data inicial e final\.

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

Regra p/ criação do novo módulo

O novo módulo “Duque de Caxias” deve ficar localizado no grupo “Municipal” 

A descrição funcional do módulo será: “O módulo Duque de Caxias irá gerar o meio magnético permitindo a importação de notas fiscais convencionais recebidas para o Sistema de Notas Fiscais de Serviço Eletrônicas\.”

__OS3767__

__RN02__

__Regra p/ abertura do novo módulo__

Se o estabelecimento selecionado no Manager não pertencer ao estado do Rio de Janeiro \(UF = “RJ”\) e ao município de Duque de Caxias \(Cod Município IBGE = 1702\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Duque de Caxias, Rio de Janeiro\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Serão exibidos os botões “Sim” e “Não” \(default\)\. Se o usuário clicar no botão “Sim”, o módulo será aberto normalmente, senão o módulo será fechado\.

__OS3767__

__RN03__

__Regra p/ hierarquia de menus__

Deverão ser criados os seguintes menus e sub\-menus no módulo Duque de Caxias:

- Arquivo
- Obrigações
	- Meio Magnético
- Janela
- Ajuda

__OS3767__

__RN04__

__Regra de criação do nome do arquivo__

Cada arquivo corresponderá a apenas uma DMS e será identificado por:

Serviços Prestados:

__DUQUE\_CAXIAS\_DDMMAAAA\.txt__, onde:

       __DDMMAAAA__: representa a data inicial da geração do meio magnético

      __ DUQUE\_CAXIAS__: representa a obrigação que está sendo gerada\.

       __\.txt__: extensão do arquivo\.   

__OS3767__

RN05

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

Data Inicial: O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE\.

Data Final: O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE\. 

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

Estabelecimento: o sistema deve exibir os estabelecimentos pertencentes ao município de Duque de Caxias, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__OS3767__

__MFS\_2071__

__RN06__

__Regra de Estrutura e Disposição de cada registro no arquivo__

Registro Tipo 10 \(Obrigatório\): Uma linha de cabeçalho\. Primeira linha do arquivo\.

Registro Tipo 40 \(Opcional\): Zero ou mais linhas de detalhe\. Cada linha corresponde a uma Nota Fiscal Convencional Recebida\.

Registro Tipo 90 \(Obrigatório\): Uma linha de rodapé\. Última linha do arquivo\.

__OS3767__

__RN07__

__Regra de formatação do arquivo__

Todos os campos numéricos deverão ser preenchidos alinhados pela direita e sem formatação \(sem ponto e sem vírgula\)\. Se necessário, preencher com zeros à esquerda até completar seu tamanho máximo\. Quando o campo for opcional, ou seja, o conteúdo do campo não seja fornecido, este deverá ser preenchido com zeros até completar seu tamanho máximo\.

Todos os campos alfanuméricos  deverão ser preenchidos alinhados pela esquerda\. Se necessário, preencher com espaços em branco à direita até completar seu tamanho máximo, com exceção do campo de Discriminação dos Serviços da linha de detalhe do registro 40\. Quando o campo for opcional, ou seja, quando o conteúdo do campo não é fornecido, este deverá ser preenchido com espaços em branco até completar seu tamanho máximo\.

__OS3767__

__RN08__

__Regra do Registro Tipo 10 \- Cabeçalho__

Esse registro deve conter informações referentes ao estabelecimento contribuinte escolhido na tela de geração do meio magnético

__OS3767__

__RN09__

__Regra do Registro Tipo 10 – Campo Tipo de Registro__

Preencher com “10”\.

__OS3767__

__RN10__

__Regra do Registro Tipo 10 – Campo Versão do Arquivo__

Preencher com “003”\.

__OS3767__

	

RN11

__Regra do Registro Tipo 10 – Campo Identificação CPF ou CNPJ do Contribuinte__

Preencher com 2\.

A opção 1 não irá ocorrer pois o cadastro de Estabelecimentos não permite o cadastro de pessoa física\.

__OS3767__

__RN12__

__Regra do Registro Tipo 10 – Campo CPF ou CNPJ do Contribuinte__

Preencher com o campo CGC da tabela ESTABELECIMENTO referente ao estabelecimento escolhido da geração do meio magnético\.

__OS3767__

__RN13__

__Regra do Registro Tipo 10 – Campo Inscrição Municipal do Contribuinte__

Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO referente ao estabelecimento escolhido da geração do meio magnético\.

__OS3767__

__RN14__

__Regra do Registro Tipo 10 – Campo Data de Início do Período Transferido no Arquivo__

Preencher com o campo “Data Inicial” da tela de geração do meio magnético\. Formato AAAAMMDD\.

__OS3767__

__RN15__

__Regra do Registro Tipo 10 – Campo Data de Fim do Período Transferido no Arquivo__

Preencher com o campo “Data Final” da tela de geração do meio magnético\. Formato AAAAMMDD\.

__OS3767__

__RN16__

__Regra do Registro Tipo 10 – Campo Caractere de Fim de Linha__

Preencher com caractere de fim de linha “Enter” \(Chr\(13\) \+ Chr\(10\)\)\.

__OS3767__

__RN17__

__Regra do Registro Tipo 40 – Declaração  de Notas Convencionais Recebidas__

Recuperar notas com as seguintes características:

- Nota de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Notas não canceladas \(SITUACAO <> ‘S’\)

As notas fiscais eletrônicas cujo prestador \(SAFX04\) é de Duque de Caxias não devem ser geradas no arquivo\. Para identificar notas fiscais eletrônicas, o mastersaf possui duas formas:

1. Através do modelo 55
2. Através o campo NF\-e \(Nota Fiscal Eletrônica\) da tela de cadastro de tipos de documentos marcado

Dessa forma deve\-se primeiro identificar se a nota é uma nota fiscal eletrônica e depois verificar se o prestador é ou não de Duque de Caxias e assim gerar ou não a nota no arquivo\. Conforme regra abaixo:

Se o campo IND\_NF\_ELETRONICA da SAFX2005 = “S”, verificar \(independente do modelo da nota fiscal\):

       Se o município da pessoa fis/jur for __IGUAL__ ao município do estabelecimento

             A nota __NÃO__ deve ser gerada no arquivo magnético

       Se o município da pessoa fis/jur for __DIFERENTE__ do município do estabelecimento  

            A nota deve ser gerada no arquivo magnético

                                                       OU

Se o modelo da nota fiscal for igual a 55, verificar:

       Se o município da pessoa fis/jur for __IGUAL__ ao município do estabelecimento

             A nota __NÃO__ deve ser gerada no arquivo magnético

       Se o município da pessoa fis/jur for __DIFERENTE__ do município do estabelecimento  

            A nota deve ser gerada no arquivo magnético

__OS3767__

__RN18__

__Regra do Registro Tipo 40 – Campo Tipo de Registro__

Preencher com “40”

__OS3767__

__RN19__

__Regra do Registro Tipo 40 – Campo Tipo da Nota Convencional__

Preencher com o campo Tipo Docto da tela Parâmetros por Município – Parâmetros – Tipo Docto Msaf x Tipo Docto referente ao tipo de documento cadastrado na nota fiscal\.

__OS3767__

__RN20__

__Regra do Registro Tipo 40 – Campo Série da Nota Convencional__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 09 da SAFX07\)

__OS3767__

	

__RN21__

__Regra do Registro Tipo 40 – Campo Número da Nota Convencional__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 08 da SAFX07\)

__OS3767__

__RN22__

__Regra do Registro Tipo 40 – Campo Data de Emissão  da Nota Convencional__

 Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(campo 11 da SAFX07\)\. Formato AAAAMMDD\.

__OS3767__

__RN23__

__Regra do Registro Tipo 40 – Campo Status da Nota Convencional__

Preencher com:

1, quando campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> ‘S’ \(campo 30 da SAFX07\)

2, quando campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = ‘S’ \(campo 30 da SAFX07\)

__OS3767__

__RN24__

__Regra do Registro Tipo 40 – Campo Identificação de CPF ou CNPJ do Prestador__

Preencher com:

1, quando o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal tiver 11 posições\. \(campo 06 da SAFX04\)

2, quando o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal tiver 14 posições\. \(campo 06 da SAFX04\)

__OS3767__

__RN25__

__Regra do Registro Tipo 40 – Campo CPF ou CNPJ do Prestador__

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 06 da SAFX04\)\. 

Sem formatação \(ponto, traço, barra, \.\.\.\)

__OS3767__

__RN26__

__Regra do Registro Tipo 40 – Campo Inscrição Municipal do Prestador__

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 09 da SAFX04\)

__OS3767__

__RN27__

__Regra do Registro Tipo 40 – Campo Inscrição Estadual do Prestador__

Preencher com o campo INSC\_ESTADUAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 08 da SAFX04\)

__OS3767__

__RN28__

__Regra do Registro Tipo 40 – Campo Nome ou Razão Social do Prestador__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 05 da SAFX04\)

__OS3767__

__RN29__

__Regra do Registro Tipo 40 – Campo Tipo do Endereço do Prestador \(Rua, Av, \.\.\.\)__

Preencher com o campo TP\_LOGRADOURO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 42 da SAFX04\)

__OS3767__

__RN30__

__Regra do Registro Tipo 40 – Campo Endereço do Prestador__

Preencher com o campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 12 da SAFX04\)

__OS3767__

__RN31__

__Regra do Registro Tipo 40 – Campo Número do Endereço do Prestador__

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 13 da SAFX04\)

__OS3767__

__RN32__

__Regra do Registro Tipo 40 – Campo Complemento do Endereço do Prestador__

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 14 da SAFX04\)

__OS3767__

__RN33__

__Regra do Registro Tipo 40 – Campo Bairro do Prestador__

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 15 da SAFX04\)

__OS3767__

__RN34__

__Regra do Registro Tipo 40 – Campo Cidade do Prestador__

Preencher com o campo DESCRICAO da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 25 da SAFX04\)

__OS3767__

__RN35__

__Regra do Registro Tipo 40 – Campo UF do Prestador__

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao campo IDENT\_ESTADO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 19 da SAFX04\)

__OS3767__

__RN36__

__Regra do Registro Tipo 40 – Campo CEP do Prestador__

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 20 da SAFX04\)

__OS3767__

__RN37__

__Regra do Registro Tipo 40 – Campo Telefone de Contato do Prestador__

Preencher com o campo TELEFONE da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 23 da SAFX04\)

__OS3767__

__RN38__

__Regra do Registro Tipo 40 – Campo E\-mail do Prestador__

Preencher com o campo E\_MAIL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 40 da SAFX04\)

__OS3767__

__RN39__

__Regra do Registro Tipo 40 – Campo Tipo de Tributação de Serviços__

Preencher com:

__Isenta__

03, quando o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433” ou campo Base Isenta ISS da capa do documento fiscal \(safx07\) estiver > zero

__Tributado no município__

01, se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado __OU__ 

se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado __OU__

se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado \.

__Tributado fora do município__

02, quando o campo IND\_TP\_RET = “2” e COD\_MUNICIPIO da capa do documento fiscal \(safx07\) for diferente ao município de geração da obrigação \(Rio de Janeiro\), 

OU

se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “472”\.

__Imune__

04, quando o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420”\.

__OS3767__

__RN40__

__Operação Suspensa por Decisão Judicial__

05, quando o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “09”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “427”\.

__Operação Suspensa por Decisão Administrativa__

06, quando o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “470”\.

__OS3767__

__RN41__

__Regra do Registro Tipo 40 – Campo Reservado__

Preencher com brancos\.

__OS3767__

__RN42__

__Regra do Registro Tipo 40 – Campo Opção pelo Simples__

Preencher com:

0, quando o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR <> “S”

1, quando o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR = “S”

__OS3767__

__RN43__

__Regra do Registro Tipo 40 – Campo Código do Serviço Federal__

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao campo IDENT\_SERV\_LEI\_116 relacionado ao serviço cadastrado na nota fiscal\.

O campo deve ser preenchido sem formatação\. Ex: “07\.20” será “0720”\.

__OS3767__

__RN44__

__Regra do Registro Tipo 40 – Campo Código do Serviço Municipal__

Se o serviço cadastrado na nota fiscal está parametrizado na tela Parâmetros por Município – Parâmetros – Serviços – Serviços Msaf x Serviços Municipais\. 

	Preencher com o campo Serviços da tela Parâmetros por Município – Parâmetros – Serviços – Serviços  Msaf x Serviços Municipais

Senão

Verificar se o serviço da lei 116 relacionado ao serviço cadastrado na nota fiscal está parametrizado na tela  Parâmetros por Município – Parâmetros – Serviços – Serviços Lei 116 x Serviços Municipais

		Se sim, preencher com o campo Serviços da tela Parâmetros por Município – Parâmetros – Serviços – Serviços Lei 116 x Serviços Municipais\.

		Se não, deve\-se gerar o campo em branco e exibir a mensagem no log: “O serviço cadastrado na nota fiscal e o código do serviço da Lei 116 referente ao mesmo, não estão parametrizados no menu Parâmetros por Município – Parâmetros – Serviços”\.

Se o mesmo serviço cadastro na nota fiscal estiver parametrizado nas duas telas, deve\-se considerar o que está parametrizado na tela Serviços da tela Parâmetros por Município – Parâmetros – Serviços – Serviços Msaf x Serviços Municipais e deve\-se exibir uma mensagem no log informando ao usuário que será considerado o que está parametrizado na tela Parâmetros por Município – Parâmetros – Serviços – Serviços Msaf x Serviços Municipais\.

O campo deve ser preenchido sem formatação\. Ex: “07\.20\.10” será “00000000000000072010”\.

__OS3767__

__RN45__

__Regra do Registro Tipo 40 – Campo Alíquota__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. \(campo 32 da SAFX09\)

Incluindo duas casas decimais \(sem ponto decimal e sem %\)\.

__OS3767__

__RN46__

__Regra do Registro Tipo 40 – Campo Valor dos Serviços__

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\. \(campo 14 da SAFX09\)

Incluindo os centavos \(sem ponto decimal e sem R$\)

Caso o campo “Status da Nota” = “2” \(Cancelada\), preencher com zeros\.

__OS3767__

__RN47__

__Regra do Registro Tipo 40 – Campo Valor das Deduções__

Preencher com o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV\. \(campo 59 da SAFX09\)

Incluindo os centavos \(sem ponto decimal e sem R$\)

__OS3767__

__RN48__

__Regra do Registro Tipo 40 – Campo Reservado__

Preencher com brancos\.

__OS3767__

__RN49__

__Regra do Registro Tipo 40 – Campo Valor do ISS__

Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. \(campo 33 da SAFX09\)

Incluindo os centavos \(sem ponto decimal e sem R$\)

__OS3767__

__RN50__

__Regra do Registro Tipo 40 – Campo ISS Retido__

Preencher com “1”, quando pelo menos umas das seguintes opções seja verdadeira:

\- Município do prestador deve ser DIFERENTE do município do módulo \(campo COD\_MUNIC da tabela X04\_PESSOA\_FIS\_JUR = Duque de Caxias __E__ prestador NÃO deve possuir cadastro no CPOM \(“CPOM \- Cadastro de Prestadores de Serviços de Outros Municípios” da tabela X04\_PESSOA\_FIS\_JUR = desmarcado\)

Atendidas uma das regras acima, recuperar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. 

Com o município do local da prestação recuperado, verificar as seguintes opções:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado __OU__  
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo  COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado __OU__
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

Caso nenhuma das opões seja verdadeira, preencher com “0”\.

__OS3767__

__RN51__

__Regra do Registro Tipo 40 – Campo Data de Competência__

Preencher com o campo DT\_PAGTO\_NF da tabela DWT\_DOCTO\_FISCAL \(campo da SAFX07\), quando pelo menos umas das seguintes opções seja verdadeira:

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL está preenchido\. Se estiver preenchido, verificar se está preenchido com “1”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

Caso nenhuma das opões seja verdadeira, preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. \(campo da SAFX07\)

__OS3767__

__RN52__

__Regra do Registro Tipo 40 \- Reservado__

Preencher com brancos\.

__OS3767__

__RN53__

__Regra do Registro Tipo 40 – Campo Discriminação dos Serviços__

Preencher com brancos\.

__OS3767__

__RN54__

__Regra do Registro Tipo 40 – Campo Caractere de Fim de Linha__

Preencher com caractere de fim de linha “Enter” \(Chr\(13\) \+ Chr\(10\)\)\.

__OS3767__

__RN55__

__Regra do Registro Tipo 90 – Rodapé__

Preencher com o total dos valores informados no registro tipo 40\.

__OS3767__

__RN56__

__Regra do Registro Tipo 90 – Campo Tipo de Registro__

Preencher com “90”\.

__OS3767__

__RN57__

__Regra do Registro Tipo 90 – Campo Número de linhas do detalhe do arquivo__

Preencher com a quantidade de registros do tipo 40 gerados no arquivo\.

__OS3767__

__RN58__

__Regra do Registro Tipo 90 – Campo Valor total dos serviços contidos no arquivo__

Preencher com o somatório dos valores dos serviços dos registros do tipo 40\.

__OS3767__

__RN59__

__Regra do Registro Tipo 90 – Campo Valor total das deduções contidas no arquivo__

Preencher com o somatório dos valores das deduções dos registros do tipo 40\.

__OS3767__

__RN60__

__Regra do Registro Tipo 90 – Campo Valor total dos descontos condicionados contidos no arquivo__

 Preencher com zeros\.

__OS3767__

__RN61__

__Regra do Registro Tipo 90 – Campo Valor total dos descontos incondicionados contidos no arquivo__

Preencher com zeros\.

__OS3767__

__RN62__

__Regra do Registro Tipo 90 – Campo Caractere de Fim de Linha__

Preencher com caractere de fim de linha “Enter” \(Chr\(13\) \+ Chr\(10\)\)\.

__OS3767__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

