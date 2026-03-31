# MTZ_DSRe_Recife_Geracao_do_Meio_Magnetico

- **Fonte:** MTZ_DSRe_Recife_Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2026-03-09
- **Tamanho:** 55 KB

---

# Recife \- DSRe

# Geração do Meio Magnético

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

O4642

Recife \- DSRe \- Geração do Meio Magnético

Este documento tem por objetivo criar o novo módulo “Recife – DSRe que irá gerar o meio magnético permitindo a importação de notas fiscais convencionais recebidas para o Sistema de Notas Fiscais de Serviço Eletrônicas\.

CH9837\_2015

Recife \- DSRe \- Geração do Meio Magnético

Este documento tem como objetivo alterar o preenchimento do campo Inscrição Municipal do Prestador do Registro Tipo 40\.

MFS\_2071

DW \- MUNICIPAL Recife \- DSRe – Retirada do range da data inicial e final\.

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

CH9089\_2016

Recife \- DSRe \- Geração do Meio Magnético

Este documento tem como objetivo alterar a geração da declaração para desconsiderar nota fiscal eletrônica de prestadores de Recife\.

CH15059\_2016

Recife \- DSRe \- Geração do Meio Magnético

Este documento tem como objetivo alterar a geração da declaração para considerar os documentos fiscais emitidos dentro do período\.

CH5647\_2017 \(MFS10226\)

CH5647\_2017 \- DW \- MUNICIPAL \- RECIFE \- Erro de geração do campo 49 \- CNAE do registro tipo 40\.

Alteração da regra RN43 para que o código da atividade passe a ser validado pela parametrização Atividade MsafxAtividade e com isso a Nota Fiscal deverá ser desconsiderada, caso a atividade não esteja na parametrização\.

CH15269\_2017 \(MFS\-12902\)

DW \- MUNICIPAL \- RECIFE \- Erro de geração do campo 49 \- CNAE do registro tipo 40\.

Este documento tem como objetivo alterar o preenchimento do campo 49\-CNAE do Registro Tipo 40 para considerar o Código de Atividade do Serviço cadastrado no item da nota fiscal\.

MFS14915

DW – MUNICIPAL – DSRe – RECIFE – Inclusão do parâmetro de Data por quebra de emissão  

Alteração da regra RN04 para a inclusão do parâmetro “Quebrar Arquivos por Data de Emissão” na geração do meio magnético\. 

CH20796\_2017 \(MFS\-16040\)

Recife \- DSRe \- Geração do Meio Magnético

Este documento tem como objetivo alterar a geração da declaração para considerar os documentos fiscais emitidos dentro do período via quebra de arquivos\.

MFS47979

DW \- MUNICIPAL \- RECIFE \- campo CNAE do registro tipo 40\.

Alteração da regra de preenchimento do campo Código de Atividade \(Serviço Municipal\)\.

MFS82881

Andréa Rocha

Alteração da regra de preenchimento dos campos Data de Início do Período e Data de Fim do Período do registro Tipo 10\.

MFS829438

Graciela Soares

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Recife” deve ficar localizado no grupo “Municipal”\.

 A descrição funcional do módulo será: “O módulo irá gerar o meio magnético permitindo a importação de notas fiscais convencionais recebidas para o Sistema de Notas Fiscais de Serviço Eletrônicas\.”

__OS4642__

__RN02__

__Regra p/ inclusão do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “PE” e ao código de município do IBGE igual a “11606” \(Recife\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Recife, Pernambuco\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS4642__

__RN03__

__Estrutura de menus do módulo DSRe:__

Deverão ser criado o seguinte menu e sub\-menus no módulo DSRe:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
	- __Arquivo de Entradas de Serviços \(Const\.Civil/Utilities/Telecom\)__

__OS4642__

__RN04__

__Regra de criação do nome do arquivo__

__Serviços Tomados:__

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_MMAAAA\.TXT__, onde:

       __ST__: Apenas registros de serviços tomados\.

__MMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\.TXT

           

Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado, deve ser realizada a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_MMAAAA\_ MMAAAA\.TXT__, onde:

       __ST__: Apenas registros de serviços tomados\.

__MMAAAA__: representa a data inicial da geração

__MMAAAA:__ mês da competência referente à nota gerada\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\_012010\.TXT

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__*Observação:* Este parâmetro \(Quebrar Arquivo por Data de Emissão\) será válido apenas para Notas de Serviços Tomados\.__

__OS4642__

__MFS\-14915__

__MFS\-829438     __

RN05

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

Data Inicial: O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE\.

Data Final: O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE\. 

Quebrar arquivo por Data de Emissão: deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

Estabelecimento: o sistema deve exibir os estabelecimentos pertencentes ao município do Recife, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__OS4642__

__MFS\_2071__

__MFS\-14915__

__RN06__

__Regra de Estrutura e Disposição de cada registro no arquivo__

Registro Tipo 10 \(Obrigatório\): Uma linha de cabeçalho\. Primeira linha do arquivo\.

Registro Tipo 40 \(Opcional\): Zero ou mais linhas de detalhe\. Cada linha corresponde a uma Nota Fiscal Convencional Recebida\.

Registro Tipo 90 \(Obrigatório\): Uma linha de rodapé\. Última linha do arquivo\.

__OS4642__

__RN07__

__Regra de formatação do arquivo__

Todos os campos numéricos deverão ser preenchidos alinhados pela direita e sem formatação \(sem ponto e sem vírgula\)\. Se necessário, preencher com zeros à esquerda até completar seu tamanho máximo\. Quando o campo for opcional, ou seja, o conteúdo do campo não seja fornecido, este deverá ser preenchido com zeros até completar seu tamanho máximo\.

Todos os campos alfanuméricos deverão ser preenchidos alinhados pela esquerda\. Se necessário, preencher com espaços em branco à direita até completar seu tamanho máximo, com exceção do campo de Discriminação dos Serviços da linha de detalhe do registro 40\. Quando o campo for opcional, ou seja, quando o conteúdo do campo não é fornecido, este deverá ser preenchido com espaços em branco até completar seu tamanho máximo\.

__OS4642__

__RN08__

__Regra do Registro Tipo 10 – Cabeçalho__

Esse registro deve conter informações referentes ao estabelecimento contribuinte escolhido na tela de geração do meio magnético\.

__OS4642__

__RN09__

__Regra do Registro Tipo 10 – Campo Tipo de Registro__

Preencher com “10”\.

Tipo: Numérico

Tam\.: 02 caracteres

__OS4642__

__RN10__

__Regra do Registro Tipo 10 – Campo Versão do Arquivo__

Preencher com “003”\.

Tipo: Numérico

Tam\.: 03 caracteres

__OS4642__

__RN11__

__Regra do Registro Tipo 10 – Campo Identificação CPF ou CNPJ do Contribuinte__

Preencher com valor “__2”\.__

Tipo: Numérico

Tam\.: 01 caractere

__OS4642__

__RN12__

__Regra do Registro Tipo 10 – Campo CPF ou CNPJ do Contribuinte__

Preencher com o campo CGC da tabela ESTABELECIMENTO referente ao estabelecimento escolhido da geração do meio magnético\.

Tipo: Numérico

Tam\.: 14 caracteres

__OS4642__

__RN13__

__Regra do Registro Tipo 10 – Campo Inscrição Municipal do Contribuinte__

Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO referente ao estabelecimento escolhido da geração do meio magnético\.

Tipo: Numérico

Tam\.: 15 caracteres

__OS4642__

__RN14__

__Regra do Registro Tipo 10 – Campo Data de Início do Período Transferido no Arquivo__

Se o parâmetro “Quebrar Arquivos por Data de Emissão” estiver desmarcado

      Preencher com o campo “Data Inicial” da tela de geração do meio magnético\. 

Senão

      Preencher com o primeiro dia do mês \+ mês/ano da data de emissão das notas fiscais geradas no arquivo\. 

Tipo: AAAAMMDD

Tam\.: 08 caracteres

__OS4642/__

__MFS82881__

__RN15__

__Regra do Registro Tipo 10 – Campo Data de Fim do Período Transferido no Arquivo__

Se o parâmetro “Quebrar Arquivos por Data de Emissão” estiver desmarcado

      Preencher com o campo “Data Final” da tela de geração do meio magnético

Senão

      Preencher com o último dia do mês \+ mês/ano da data de emissão das notas fiscais geradas no arquivo\.

Tipo: AAAAMMDD

Tam\.: 08 caracteres

__OS4642/__

__MFS82881__

__RN16__

__Regra do Registro Tipo 10 – Campo Caractere de Fim de Linha__

Preencher com caractere de fim de linha “Enter” \(Chr\(13\) \+ Chr\(10\)\)\.

__OS4642__

__RN17__

__Regra do Registro Tipo 40 – Declaração Eletrônica de Serviços Recebidos__

Recuperar notas com as seguintes características:

- Nota de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração

__\[ALTERADA – CH15059\_2016\]__

__\[ALTERADA \- CH20796\_2017 \(MFS\-16040\)\]__

- Data fiscal de emissão dentro do período de referência \[*Observação:* O chamado 15059 foi retificado pela Maíra\]

__\[ALTERADA – CH9089\_2016\]__

- Para considerar notas fiscais eletrônicas verificar: 
- Se o município do prestador \(campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\) for __DIFERENTE__ do município do módulo selecionado para geração \(COD\_MUNICIPIO da tabela ESTABELECIMENTO\), recuperar os documentos com uma das situações abaixo:
- Modelo do Documento \(campo COD\_MODELO da tabela DWT\_DOCTO\_FISCAL = ‘55’\) __OU__
- Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal\.

__OS4642__

__CH9089\_2016__

__CH15059\_2016__

__CH20796\_2017 \(MFS\-16040\)__

__RN18__

__Regra do Registro Tipo 40 – Campo Tipo de Registro__

Preencher com “40”

__OS4642__

__RN19__

__Regra do Registro Tipo 40 – Campo Tipo de Documento__

Preencher com o campo Tipo Docto DSRe da tela Tipo Docto Msaf x Tipo Docto, em Parâmetros para Município\. referente ao tipo de documento cadastrado na nota fiscal\.

Obs\.: Caso o documento não for parametrizado em Parâmetros por Município, deverá exibir a seguinte mensagem no Log:

Para o Tipo de Documento "XXX" do Documento "NNNNNN\-SSS", não foi localizada a parametrização de Tipo Docto Msaf x Tipo Docto\. Efetuar a parametrização no menu Parâmetros > Tipo Docto Msaf x Tipo Docto no módulo "Parâmetros para Município"\.

Tipo: Numérico

Tam\.: 02 caracteres

__OS4642__

__RN20__

__Regra do Registro Tipo 40 – Campo Série do Documento__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 09 da SAFX07\)

Tipo: Texto

Tam\.: 05 caracteres

__OS4642__

__RN21__

__Regra do Registro Tipo 40 – Campo Número do Documento__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 08 da SAFX07\)

Tipo: Numérico

Tam\.: 15 caracteres

__OS4642__

__RN22__

__Regra do Registro Tipo 40 – Campo Data de Emissão __

 Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(campo 11 da SAFX07\)\. Formato AAAAMMDD\.

Tipo: AAAAMMDD\.

Tam\.: 08 caracteres

__OS4642__

__RN23__

__Regra do Registro Tipo 40 – Campo Status do Documento__

Status do Documento Recebido\. Deverá Preencher com:

1 – Normal\.  Quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> ‘S’

2 \- Cancelado\. Quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = ‘S’

Tipo: Numérico

Tam\.: 01 caracter

__OS4642__

__RN24__

__Regra do Registro Tipo 40 – Campo Identificação de CPF ou CNPJ do Prestador__

Preencher com:

1, quando o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal tiver 11 posições\. \(campo 06 da SAFX04\)

2, quando o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal tiver 14 posições\. \(campo 06 da SAFX04\)

Tipo: Numérico

Tam\.: 01 caracter

__OS4642__

__RN25__

__Regra do Registro Tipo 40 – Campo CPF ou CNPJ do Prestador__

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 06 da SAFX04\)\. 

Sem formatação \(ponto, traço, barra, \.\.\.\)

Tipo: Numérico

Tam\.: 14 caracteres

__OS4642__

__RN26__

__Regra do Registro Tipo 40 – Campo Inscrição Municipal do Prestador__

__\[ALTERADA – CH9837\_2015\]__

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR referente à pessoa fis/jur cadastrada na nota fiscal \(campo 09 da SAFX04\) quando o campo COD\_MUNICIPIO \(campo 25 da SAFX04\) for igual a Recife, caso contrário preencher com zeros\.

Tipo: Numérico

Tam\.: 15 caracteres

__OS4642__

__CH9837\_2015__

__RN27__

__Regra do Registro Tipo 40 – Campo Inscrição Estadual do Prestador__

Preencher com o campo INSC\_ESTADUAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 08 da SAFX04\)

Tipo: Numérico

Tam\.: 15 caracteres

__OS4642__

__RN28__

__Regra do Registro Tipo 40 – Campo Nome ou Razão Social do Prestador__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 05 da SAFX04\)

Tipo: Texto

Tam\.: 115 caracteres

__OS4642__

__RN29__

__Regra do Registro Tipo 40 – Campo Tipo do Endereço do Prestador \(Rua, Av, \.\.\.\)__

Preencher com o campo TP\_LOGRADOURO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 42 da SAFX04\)

Tipo: Texto

Tam\.: 03 caracteres

__OS4642__

__RN30__

__Regra do Registro Tipo 40 – Campo Endereço do Prestador__

Preencher com o campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 12 da SAFX04\)

Tipo: Texto

Tam\.: 125 caracteres

__OS4642__

__RN31__

__Regra do Registro Tipo 40 – Campo Número do Endereço do Prestador__

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 13 da SAFX04\)

Tipo: Texto

Tam\.: 10 caracteres

__OS4642__

__RN32__

__Regra do Registro Tipo 40 – Campo Complemento do Endereço do Prestador__

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 14 da SAFX04\)

Tipo: Texto

Tam\.: 60 caracteres

__OS4642__

__RN33__

__Regra do Registro Tipo 40 – Campo Bairro do Prestador__

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 15 da SAFX04\)

Tipo: Texto

Tam\.: 72 caracteres

__OS4642__

__RN34__

__Regra do Registro Tipo 40 – Campo Cidade do Prestador__

Preencher com o campo DESCRICAO da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 25 da SAFX04\)

Tipo: Texto

Tam\.: 50 caracteres

__OS4642__

__RN35__

__Regra do Registro Tipo 40 – Campo UF do Prestador__

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao campo IDENT\_ESTADO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 19 da SAFX04\)

Tipo: Texto

Tam\.: 02 caracteres

__OS4642__

__RN36__

__Regra do Registro Tipo 40 – Campo CEP do Prestador__

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 20 da SAFX04\)

Tipo: Numérico

Tam\.: 08 caracteres

__OS4642__

__RN37__

__Regra do Registro Tipo 40 – Campo Telefone de Contato do Prestador__

Preencher com o campo TELEFONE da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 23 da SAFX04\)

Tipo: Texto

Tam\.: 11 caracteres

__OS4642__

__RN38__

__Regra do Registro Tipo 40 – Campo E\-mail do Prestador__

Preencher com o campo E\_MAIL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 40 da SAFX04\)

Tipo: Texto

Tam\.: 80 caracteres

__OS4642__

__RN39__

__Regra do Registro Tipo 40 – Campo Tipo de Tributação de Serviços__

Preencher com:

__“03”__ \- Isenta, quando o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\.

__“01” \- __Tributado no município, se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1” e se o local da prestação do serviço = município do módulo selecionado __OU__ 

se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado __OU__

se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado__ OU__

__“02”__ \- Tributado fora do município, quando o campo IND\_TP\_RET = “2” e COD\_MUNICIPIO da capa do documento fiscal \(safx07\) for diferente ao município de geração da obrigação \(Recife\), __OU__

se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “472”\.__OU__

__“04”__ \- Imune, quando o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420”\.

__“05”__ \- Operação Suspensa por Decisão Judicial, quando o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “09”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “427”\.

Obs\.: Caso nenhum dos itens acima seja válido, preencher com zeros\.

Tipo: Numérico

Tam\.: 02 caracteres

__OS4642__

__RN40__

__Regra do Registro Tipo 40 – Campo Reservado__

Preencher com brancos\.

Tipo: Texto

Tam\.: 54 caracteres

__OS4642__

__RN41__

__Regra do Registro Tipo 40 – Campo Opção pelo Simples__

 Preencher com:

0, quando o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR <> “S”

1, quando o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR = “S”

Tipo: Numérico 

Tam\.: 01 caracteres

__OS4642__

__RN42__

__Regra do Registro Tipo 40 – Campo Código do Serviço Federal__

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao campo IDENT\_SERV\_LEI\_116 relacionado ao serviço cadastrado na nota fiscal\.

O campo deve ser preenchido sem formatação\. Ex: “07\.20” será “0720”\.

Caso o campo não possuir informação, deverá ser preenchido com zeros até completar seu tamanho máximo\. 

Tipo: Numérico

Tam\.: 04 caracteres

__OS4642__

__RN43__

__Regra do Registro Tipo 40 – Campo Código CNAE __

Preencher com o campo COD\_ATIVIDADE da tabela X04\_PESSOA\_FIS\_JUR referente ao Código da Atividade Econômica\.

Preencher com o conteúdo do campo Atividade da parametrização no módulo Municipal – Parâmetros para Município, item de menu Parâmetros >> Atividade Msaf x Atividade, referente a atividade da pessoa fis/jur cadastrada na nota\. 

Quando o campo COD\_ATIVIDADE estiver vazio, Se a atividade não estiver parametrizada, a nota fiscal deverá ser desconsiderada na geração do arquivo e deverá preencher com zeros e exibir a seguinte mensagem no Log: “Para o Código de Atividade Econômica – CNAE "XXXXXXX", não foi localizada a parametrização de Atividade Msaf x Atividade\. Efetuar a parametrização no menu Parâmetros > Atividade Msaf x Atividade no módulo "Parâmetros para Município"\. Por isso, a Nota Fiscal foi desconsiderada na geração do arquivo\.

O Código de Atividade Econômica – CNAE não está cadastrado , no cadastro de Pessoa Física/Jurídica\.”

__\[ALTERADA \- CH15269\_2017 \(MFS\-12902\)\]__

Preencher com o conteúdo do campo COD\_ATIVIDADE da tabela ATIV\_ECONOMICA relacionado ao campo COD\_ATIVIDADE da tabela X2018\_SERVICOS relacionado ao serviço cadastrado no item da nota fiscal de serviço\.

__\[MFS47979\] __Inclusão da utilização da parametrização de Serviço Msaf x Atividade

Se o campo COD\_ATIVIDADE da tabela X2018\_SERVICOS não estiver preenchido

     Preencher com o conteúdo do campo Atividade da parametrização no módulo Municipal – Parâmetros para Município, item de menu Parâmetros >> Serviço Msaf x Atividade, referente ao serviço cadastrada na nota\. 

O campo deve ser preenchido sem formatação\. Ex: “6209100” será “00000000000006209100”\.

Tipo: Numérico

Tam\.: 20 caracteres

__OS4642__

__MFS10226__

__CH15269\_2017 \(MFS\-12902\)__

__MFS47979__

__RN44__

__Regra do Registro Tipo 40 – Campo Alíquota__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. \(campo 32 da SAFX09\)

Incluindo duas casas decimais \(sem ponto decimal e sem %\)\. Exemplo: 105,00% = 10500

Tipo: Numérico

Tam\.:05 caracteres

__OS4642__

__RN45__

__Regra do Registro Tipo 40 – Campo Valor dos Serviços__

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\. \(campo 14 da SAFX09\)

Incluindo os centavos \(sem ponto decimal e sem R$\)\.

Exemplo:

R$ 500,85 = 000000000050085

R$ 500,00 = 000000000050000

Tipo: Numérico

Tam\.:15 caracteres

__OS4642__

__RN46__

__Regra do Registro Tipo 40 – Campo Valor das Deduções__

Preencher com o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV\. \(campo 59 da SAFX09\)

Incluindo os centavos \(sem ponto decimal e sem R$\)\.

Exemplo:

R$ 500,85 = 000000000050085

R$ 500,00 = 000000000050000

Tipo: Numérico

Tam\.:15 caracteres

__OS4642__

__RN47__

__Regra do Registro Tipo 40 – Campo Reservado__

Preencher com brancos\.

Tipo: Texto

Tam\.:30 caracteres

__OS4642__

__RN48__

__Regra do Registro Tipo 40 – Campo Valor do ISS__

Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. \(campo 33 da SAFX09\)

Incluindo os centavos \(sem ponto decimal e sem R$\)\.

Exemplo:

R$ 500,85 = 000000000050085

R$ 500,00 = 000000000050000

Tipo: Numérico

Tam\.:15 caracteres

__OS4642__

__RN49__

__Regra do Registro Tipo 40 – Campo ISS Retido__

Preencher com __“1”__, quando pelo menos umas das seguintes opções seja verdadeira:

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado __OU__  
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo  COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado __OU__
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

Caso nenhuma das opões seja verdadeira, preencher com __“0”__\.

Tipo: Numérico

Tam\.:01 caracteres

__OS4642__

__RN50__

__Regra do Registro Tipo 40 – Campo Data de Competência__

Preencher com o campo DT\_PAGTO\_NF da tabela DWT\_DOCTO\_FISCAL \(campo da SAFX07\), quando pelo menos umas das seguintes opções seja verdadeira:

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL está preenchido\. Se estiver preenchido, verificar se está preenchido com “1”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

Caso nenhuma das opões seja verdadeira, preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. \(campo da SAFX07\)\.

Tipo: AAAAMMDD

Tam\.:08 caracteres

__OS4642__

__RN51__

__Regra do Registro Tipo 40 – Campo Código da Obra__

Preencher com o campo COD\_CEI da tabela DWT\_DOCTO\_FISCAL\. Caso o campo COD\_CEI não esteja informado na nota, esse campo deve ser preenchido com o campo COD\_CANAL\_DISTRIB da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Texto

Tam\.:15 caracteres

__OS4642__

__RN52__

__Regra do Registro Tipo 40 – Anotação de Responsabilidade Técnica__

Preencher com brancos\. 

Tipo: Texto

Tam\.:15 caracteres

__OS4642__

__RN53__

__Regra do Registro Tipo 40 – Campo Caractere de Fim de Linha__

Preencher com caractere de fim de linha “Enter” \(Chr\(13\) \+ Chr\(10\)\)\.

__OS4642__

__RN54__

__Regra do Registro Tipo 90 – Rodapé__

Preencher com o total dos valores informados no registro tipo 40\.

__OS4642__

__RN55__

__Regra do Registro Tipo 90 – Campo Tipo de Registro__

Preencher com “90”\.

Tipo: Numérico

Tam\.:02 caracteres

__OS4642__

__RN56__

__Regra do Registro Tipo 90 – Campo Número de linhas do detalhe do arquivo__

Preencher com a quantidade de registros do tipo 40 gerados no arquivo\.

Tipo: Numérico

Tam\.:08 caracteres

__OS4642__

__RN57__

__Regra do Registro Tipo 90 – Campo Valor total dos serviços contidos no arquivo__

Preencher com o somatório dos valores dos serviços dos registros do tipo 40\.

Tipo: Numérico

Tam\.:15 caracteres

__OS4642__

__RN58__

__Regra do Registro Tipo 90 – Campo Valor total das deduções contidas no arquivo__

Preencher com o somatório dos valores das deduções dos registros do tipo 40\.

Tipo: Numérico

Tam\.:15 caracteres

__OS4642__

__RN59__

__Regra do Registro Tipo 90 – Campo Valor total dos descontos condicionados contidos no arquivo__

 Preencher com zeros\.

Tipo: Numérico

Tam\.:15 caracteres

__OS4642__

__RN60__

__Regra do Registro Tipo 90 – Campo Valor total dos descontos incondicionados contidos no arquivo__

Preencher com zeros\.

Tipo: Numérico

Tam\.:15 caracteres

__OS4642__

__RN61__

__Regra do Registro Tipo 90 – Campo Caractere de Fim de Linha__

Preencher com caractere de fim de linha “Enter” \(Chr\(13\) \+ Chr\(10\)\)\.

__OS4642__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

