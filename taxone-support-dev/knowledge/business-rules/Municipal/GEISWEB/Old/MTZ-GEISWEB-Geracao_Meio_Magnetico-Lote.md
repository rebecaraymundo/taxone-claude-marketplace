# MTZ-GEISWEB-Geracao_Meio_Magnetico-Lote

- **Fonte:** MTZ-GEISWEB-Geracao_Meio_Magnetico-Lote.docx
- **Modificado:** 2026-01-30
- **Tamanho:** 59 KB

---

Municipal

GEISWEB \- Geração do Meio Magnético   

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3470\-S

GEISWEB – Geração do meio magnético 

Este documento tem como objetivo criar a geração para os municípios que são atendidos pelo Meuiss dentro do grupo de obrigações “Municipal”, que permitirá a geração de um meio magnético onde serão informados documentos fiscais de serviço em lote para o período e estabelecimento escolhidos, onde apenas estabelecimentos sediados no município em questão poderão ser selecionados\.

OS3926\-N

DW \- MUNICIPAL \- GEISWEB \- Atendimento a constução civil/telecomunicações/utilities

Este documento tem como objetivo criar a geração do meio magnético para os segmentos de Construção Civil, Utilities e Telecom para os municípios atendidos pelo validador GEISWEB\. 

OS3926\-N

DW \- MUNICIPAL \- GEISWEB \- Atendimento a constução civil/telecomunicações/utilities

Este documento tem como objetivo acrescentar a nomenclatura \(RN14\) na geração do meio magnético para os segmentos de Construção Civil, Utilities e Telecom para os municípios atendidos pelo validador GEISWEB\.

OS4429

DW \- MUNICIPAL \- GEISWEB – Inclusão de Município

Este documento tem como objetivo incluir o município de Mogi Mirim, que anteriormente era atendido pelo SIGISS e passará a ser atendido pelo validador GEISWEB\. 

__MFS2105__

DW \- MUNICIPAL \- GEISWEB – Inclusão de Município

Este documento tem como objetivo incluir o município de Votorantim\-SP, para ser atendido pelo validador GEISWEB\. 

MFS\_2071

DW \- MUNICIPAL \- GEISWEB – Retirada do range da data inicial e final\.

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

CH10330\_2017

Lara Aline

Ajuste no campo Valor da Base de Cálculo para verificar também a base de cálculo isenta\.

MFS31941

DW \- MUNICIPAL \- GEISWEB – Inclusão de Município

Este documento tem como objetivo incluir o município de Itatinga\-SP, para ser atendido pelo validador GEISWEB\. 

MFS37837

Andréa Rocha

Alteração da regra de recuperação dos dados para o município de Itatinga

MFS43270

Andréa Rocha

Alteração da regra do campo 11 \- Município da nota fiscal\.

MFS43854

Andréa Rocha

Alteração da regra de recuperação dos dados para o município de Itatinga, de acordo com o prestador de serviço, para as notas fiscais de serviços tomados esta alteração está sendo feita de acordo com a consulta feita pelo cliente à prefeitura de Itatinga\.

MFS829438

Graciela Soares

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

MFS935738

Andréa Rocha

Inclusão do parâmetro ‘Quebrar Arquivos por Data de Emissão’ na tela de geração

__MFS\-1023835__

Rosemeire Santos

Inclusão da regra RN19\.a de preenchimento do campo Número da nota fiscal, para município de Cajamar/SP 

##### REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

RN00

__Regra p/ inclusão do novo módulo no Manager – Boituva:__

O novo módulo “Boituva” deve ficar localizado no grupo “Municipal” 

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de Boituva”\.

__OS3470\-S__

RN01

__Regra p/ abertura do novo módulo no Manager – Boituva:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “7001” \(Boituva\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Boituva, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS3470\-S__

RN02

__Regra p/ inclusão do novo módulo no Manager – Cajamar:__

O novo módulo “Cajamar” deve ficar localizado no grupo “Municipal” 

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de Cajamar”\.

__OS3470\-S__

RN03

__Regra p/ abertura do novo módulo no Manager – Cajamar:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “9205” \(Cajamar\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Cajamar, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS3470\-S__

RN04

__Regra p/ inclusão do novo módulo no Manager – Laranjal Paulista:__

O novo módulo “Laranjal Paulista” deve ficar localizado no grupo “Municipal” 

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de Laranjal Paulista”\.

__OS3470\-S__

RN05

__Regra p/ abertura do novo módulo no Manager – Laranjal Paulista:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “26407” \(Laranjal Paulista\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Laranjal Paulista, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS3470\-S__

RN06

__Regra p/ inclusão do novo módulo no Manager – Tietê:__

O novo módulo “Tietê” deve ficar localizado no grupo “Municipal” 

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de Tietê”\.

__OS3470\-S__

RN07

__Regra p/ abertura do novo módulo no Manager – Tietê:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “54508” \(Tietê\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Tietê, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS3470\-S__

RN08

__Regra p/ hierarquia de menus:__

Deverão ser criados os seguintes menus e sub\-menus:

- Arquivo
- Obrigações
	- Geração do Meio Magnético
	- Arquivo de Entradas de Serviços \(Const\. Civil/Utilities/Telecom\)
- Janela

Ajuda

__OS3470\-S__

__/__

__OS3926\-N__

__MFS31941__

RN09

__Regra para geração do Meio Magnético:__

A geração do meio magnético deve ser feita no padrão Framework\. Caso o usuário selecione mais de um estabelecimento na geração, o sistema irá gerar um arquivo para cada estabelecimento\.

__OS3470\-S__

RN10

__Regra do campo Data Inicial da tela Obrigações – Geração Meio Magnético:__

O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE\.

__OS3470\-S__

RN11

__Regra do campo Data Final da tela Obrigações – Geração Meio Magnético:__

O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE\. 

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.”

__OS3470\-S__

__MFS\_2071__

RN12

__Regra do flag Gerar Movimento a Partir – Geração Meio Magnético:__

O campo “Gerar Movimento a partir” tem duas opções:

\( x\) Data de Emissão

\(   \) Data do Fato Gerador

O sistema deve permitir que apenas uma das opções seja marcada pelo usuário\. 

Por padrão deve estar marcada a opção ‘Data de Emissão’ e desmarcada a opção ‘Data do Fato gerador’\.

__OS3470\-S__

RN12A

__Regra do flag Gerar Serviços Prestados/Gerar serviços Tomados– Geração Meio Magnético:__

Existem duas opções disponíveis:

Gerar Serviços Prestados: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Gerar Serviços Contratados: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__OS3470\-S__

RN12B

__Regra do flag Quebrar Arquivos por Data de Emissão__ __– Geração Meio Magnético:__

O campo deve ser um Checkbox\. Esse campo terá as seguintes opções “S” ou “N”\. Por default, o campo deve ser exibido desmarcado \(“N”\)\.

<a id="_Hlk212566618"></a>Obs\.:  Esse parâmetro só vai ficar habilitado, se o parâmetro “Gerar Movimento a partir” for igual a “Data de Emissão”\.

__MFS935738__

RN13

__Regra para abas existentes na geração do meio magnético:__

Ao gerar o meio magnético devem ser exibidas as abas “Log”, “Arquivo”, “Processos” e “Relatório”\. A aba “Arquivo” deve exibir o arquivo que poderá ser salvo localmente\. A aba “Log” deve exibir a mensagem “Processo concluído com sucesso” quando o arquivo for gerado corretamente, caso contrário exibir a mensagem “Processo concluído com erros”\.

__OS3470\-S__

RN14

__Regra p/ nomenclatura do arquivo magnético:__

O nome do arquivo deve seguir a seguinte regra:

__STP\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.TXT__, onde:

       __STP__: significa que é um arquivo de serviços tomados e prestados\.

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.TXT

Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado, deve ser realizado a seguinte verificação: 

- Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. 
- Esse arquivo deve conter todas as notas fiscais que tenham a mesma competência \(mesmo mês referente a data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverão ser:

__STP\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\_MMAAAA\.TXT__, onde:

       __STP__: significa que é um arquivo de serviços tomados e prestados\.

__DDMMAAAA__: representa a data inicial da geração\.   

__       MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\_012010\.TXT

Obs: Neste caso o arquivo normal também deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

Observação: Este parâmetro \(Quebrar Arquivo por Data de Emissão\) será válido apenas para Notas de Serviços Tomados\.

    __STP\_GEISWEB\_MUNICIPIO\_DDMMAAAA\.txt__, em que:

     __STP__: significa que é um arquivo de serviços tomados e prestados

__     GEISWEB: __indica que é um arquivo do validador GEISWEB

__     MUNICIPIO: __representa a obrigação que está sendo gerada\. Dependendo da obrigação deve ser preenchido com o município  correspondente

     __DDMMAAAA__: data inicial da geração

    \.__txt__: extensão do arquivo

Na geração do meio magnético para utilities\\cc\\telecom, o nome do arquivo deve ser:

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.TXT__, onde:

       __ST__: Apenas registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.TXT

__    ST__\___GEISWEB\_MUNICIPIO\_DDMMAAAA\.txt__, em que:

__    ST__: significa que é um arquivo de serviços tomados 

__     GEISWEB: __indica que é um arquivo do validador GEISWEB

__     MUNICIPIO: __representa a obrigação que está sendo gerada\. Dependendo da obrigação deve ser preenchido com o município  correspondente

     __DDMMAAAA__: data inicial da geração

    \.__txt__: extensão do arquivo

__OS3470\-S__

__OS3926\-N__

__MFS31941__

__MFS\-829438__

__MFS935738      __

RG00

__Regras Gerais para geração do Meio Magnético:__

O arquivo deverá ser gerado no formato texto \(ASCII\)

__Tratamento dos campos numéricos: __

\- Devem ser preenchidos alinhados a direita e sem pontuação;

\- Devem ser preenchidos com zeros à esquerda até completar a quantidade de posições determinada no __layout__\. 

__Tratamento dos campos alfanuméricos:__

\- Devem ser preenchidos alinhados a esquerda\.

\- Devem ser preenchidos com espaços em branco à direita até completar a quantidade de posições determinada no layout\. 

__Obs: Todos os campos deste layout são obrigatórios\.__

__OS3470\-S__

RG01

__Regra geral para Recuperação dos dados:__

Serão listados todos os registros de documentos fiscais de entrada campo __MOVTO\_E\_S__ da tabela __DWT\_DOCTO\_FISCAL__ <> 9 com código de classificação campo __COD\_CLASS\_DOC\_FIS__ da tabela __DWT\_DOCTO\_FISCAL__ = ‘2’ ou ‘3’, não cancelados Campo __SITUACAO__ da tabela __DWT\_DOCTO\_FISCAL__ = ‘N’ para o período e estabelecimento escolhidos, recuperando o movimento pela data fiscal \(campo DATA\_FISCAL da tabela DWT\_DOCTO\_FISCAL\) 

Serão gerados arquivos para estabelecimentos pertencentes a UF/município do módulo que está sendo executado\.

Os movimentos de documentos fiscais serão gerados somente para códigos de município do prestador campo __COD\_MUNICIPIO__ da tabela __X04\_PESSOA\_FIS\_JUR__ que seja diferente dos estabelecimentos pertencentes a UF/município do módulo que está sendo executado\)

__E__

Para códigos de município do prestador campo __COD\_MUNICIPIO__ da tabela __X04\_PESSOA\_FIS\_JUR__ que sejam iguais a UF/município do módulo que está sendo executado\.

__Se__ o campo __COD\_CLASS\_DOC\_FIS__ da tabela __DWT\_DOCTO\_FISCAL __for igual a ‘9’ __E__ o campo __COD\_DOCTO__ da tabela __DWT\_DOCTO\_FISCAL__ = ‘RPA’ 

__Ou__

__SE __o campo__ COD\_CLASS\_DOC\_FIS__ da tabela __DWT\_DOCTO\_FISCAL__ for igual a “2 – Serviços” ou “3 \- Mercadorias e Serviços”

__E __o campo IND\_MAT\_SERV da tabela __X2018\_SERVICOS__ = “2 – Serviço“E \- IND\_SERVICO\_TERC da tabela X2018\_SERVICOS = “S \- Tipo de Serviço prestado por terceiros, pessoa física”

__Regra para recuperação de notas eletrônicas:__

- Notas com Modelo = 55 apenas quando o município da pessoa fis/jur \(COD\_MUNICIPIO da SAFX04\) <> município do estabelecimento \(COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. Quando o município da pessoa fis/jur \(COD\_MUNICIPIO da SAFX04\) for igual ao município do estabelecimento \(COD\_MUNICIPIO da tabela ESTABELECIMENTO\) essa nota não deve ser considerada no arquivo\.
- Notas cujo campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’ referente ao tipo de documento da nota, apenas quando o município da pessoa fis/jur \(COD\_MUNICIPIO da SAFX04\) <> município do estabelecimento \(COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. Quando o município da pessoa fis/jur \(COD\_MUNICIPIO da SAFX04\) for igual ao município do estabelecimento \(COD\_MUNICIPIO da tabela ESTABELECIMENTO\) essa nota não deve ser considerada no arquivo\.

__\[MFS37837\] / \[MFS43854\] – Para o município de Itatinga – Serviços Tomados:__

- Desconsiderar os itens das notas que não possuírem Valor de Base ISS, deve\-se verificar as 2 bases de ISS \(quando a tributação for igual a 1 – Normal ou 2 – Isento\), quando o município da pessoa fis/jur \(COD\_MUNICIPIO da SAFX04\) for igual município do estabelecimento \(COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\.

__OS3470\-S__

__MFS37837__

__MFS43854__

RG02

__Regra geral para Agrupamento dos itens:__

Deve se consolidar em uma única linha, valores dos itens de um mesmo documento fiscal, há quebra em mais linhas quando os campos 

Tipo de Lançamento, Código de serviço possuírem valores diferentes dentre os itens\.

__Se houver quebra de linha, __gerar mensagens de log, informando ao usuário que nesta obrigação não são permitidos documentos com mais de um item\.

__OS3470\-S__

RN15

__Regra para geração dos dados:__

As tabelas de Capas de Documentos Fiscais e Itens de Serviço \(DATAMART\), assim como a tabela de Cadastro de Pessoas Físicas/Jurídicas devem estar devidamente povoadas\.

__OS3470\-S__

RN16

__Regra para o preenchimento do campo 01 \-‘CNPJ ou CPF do declarante’:__

Recuperar a informação do campo __CGC__ da tabela __ESTABELECIMENTO __

__Obs: __Campo Obrigatório

Campo do tipo numérico

__OS3470\-S__

RN17

__Regra para preenchimento do campo 02 –‘Tipo da Nota Fiscal’:__

Preencher com o tipo de documento parametrizado na tela Parâmetros por Município – Parâmetros – Tipo Docto Msaf x Tipo Docto referente ao tipo de documento preenchido na nota fiscal\.

__Obs:__ Se não existir parametrização para o tipo informado na nota, log do sistema deve exibir mensagem para o usuário informando que para o tipo de documento não foi localizada a parametrização de Tipo Docto\. Msaf x Tipo Docto

__Obs: __ Campo obrigatório\.

Campo do tipo alfanumérico\.

__OS3470\-S__

RN18

__Regra para preenchimento do campo 03 – ‘Série da nota fiscal’:__

Recuperar a informação do campo __SERIE\_DOCFIS__ \(campo 09\) da tabela __DWT\_DOCTO\_FISCAL __

__Obs: __ Campo obrigatório\.

Campo do tipo alfanumérico\.

__OS3470\-S__

RN19

__Regra para preenchimento do campo 04 – ‘Número da nota fiscal’:__

Recuperar a informação do campo __NUM\_DOCFIS__ __\(campo 08\) __da tabela __DWT\_DOCTO\_FISCAL__\. 

__Obs: __ Campo obrigatório\.

Campo do tipo numérico\.

__OS3470\-S__

RN19\.a

__Regra para preenchimento do campo 04 – ‘Número da nota fiscal’: \- Específica para o município de Cajamar__

Recuperar a informação do campo __NUM\_DOCFIS__ __\(campo 08\) __da tabela __DWT\_DOCTO\_FISCAL__\. \- Preencher com zeros a esquerda para completar as 10 posições\.

__Tamanho: __10 posição

__Campo do tipo numérico\.__

__Obs:  Campo obrigatório\.__

__MFS\-1023835__

RN20

__Regra para preenchimento do campo 05 – ‘Código do serviço prestado’:__

Preencher com o campo __COD\_SERV\_LEI\_116__ da tabela __DWT\_SERVICO\_LEI\_116__ referente ao serviço cadastrado na nota fiscal\.

__Obs: __ Campo obrigatório\.

Campo do tipo numérico\.

__OS3470\-S__

RN21

__Regra para preenchimento do campo 06 – ‘Tipo de Lançamento da nota fiscal’__

__O campo deve ser preenchido com:__

  
__Para notas emitidas:__

__P __– \(Simples Nacional ou MEI e retido pelo tomador\)

Preencher com ‘P’ __SE__ ao menos uma das condições abaixo forem atendidas

\- Se__ __o campo__ IND\_ISS __da tabela __ESTABELECIMENTO__ for igual a:

‘09’ – Não Tributável

__OU__

‘07’ – Simples Nacional

__N__ – \(Devido no município pelo prestador\)__ __

Preencher com ‘N’ caso nenhuma das opções da regra para gerar como ‘P’ seja atendida

__Para notas recebidas: __

__T – __\(Devido no município pelo tomador\) 

Preencher com ‘T’__ SE__ ao menos uma das condições abaixo forem atendidas

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido ,  
recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.  
  
\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se  
o local da prestação do serviço = município do módulo selecionado OU   
\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo   
COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU  
\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado \.

__OBS:__ Regra atualizada no documento DE\-PARA – Municipal\.xls \(__R1\-RN0001\)__

  
__R__ \- \(Nota fiscal recebida dentro ou fora do município\)__ __

Preencher com ‘R’ caso nenhuma das opções da regra para gerar como ‘T’ seja atendida

__Obs: __ Campo obrigatório\.

Campo do tipo alfanumérico\.

__OS3470\-S__

RN22

__Regra para preenchimento do campo 07 – ‘Data de emissão da nota fiscal’__ 

__Se__ o flag ‘Gerar movimento a partir da data de emissão’ estiver __marcado__:

    Recuperar o campo __DATA\_EMISSAO \(campo 11\) __da tabela __DWT\_DOCTO\_FISCAL__\.

__Se __o flag ‘Gerar movimento a partir da data do fato gerador’ estiver __marcado__: 

     Recuperar o campo DAT\_FATO\_GERADOR __\(campo 93\) __da tabela __DWT\_DOCTO\_FISCAL\.__

__Se__ o flag ‘Gerar movimento a partir da data do fato gerador’ estiver __marcado, e __campo __DAT\_FATO\_GERADOR \(campo 93\)__ da tabela __DWT\_DOCTO\_FISCAL __não estiver preenchido, preencher o campo com zeros e gerar mensagem de log, informando ao usuário que o campo data do fato gerador não está preenchido\.

__Obs: __ Campo obrigatório\.

Campo do tipo numérico\.

__OS3470\-S__

RN23

__Regra para preenchimento do campo 08 – ‘Valor da nota fiscal’__

Recuperar a informação do campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

__Incluir os centavos, sem ponto decimal Ex: 500,85 deves se informar 50085__

__Obs: __ Campo obrigatório\.

Campo do tipo numérico\.

__OS3470\-S__

RN24

__Regra para preenchimento do campo 09 – ‘Valor da base de cálculo’__

__\[ALTERADO CH10330\_2017\]__

Verificar se o campo __VLR\_BASE\_ISS\_2__ está preenchido:

Se estiver preenchido, recuperar a informação do campo __VLR\_BASE\_ISS\_2__ da tabela __DWT\_ITENS\_SERV\.__

Se não, recuperar a informação do campo __VLR\_BASE\_ISS\_1__ da tabela __DWT\_ITENS\_SERV\.__

__\[MFS43854\] Para o município de Itatinga – Serviços Tomados \(notas fiscais de entrada\)__

Se VLR\_BASE\_ISS\_2 não estiver preenchido __e__ VLR\_BASE\_ISS\_1 não estiver preenchido __e__ município da pessoa fis/jur    

     \(COD\_MUNICIPIO da SAFX04\) <> município do estabelecimento \(COD\_MUNICIPIO da tabela ESTABELECIMENTO\)

     Recuperar a informação do campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

     

Recuperar a informação do campo __BASE\_ISS \(campo 39\)__ da tabela __DWT\_ITENS\_SERV\.__

__Incluir os centavos, sem ponto decimal Ex: 500,85 deve se informar 50085\. __

__Obs\. Campo obrigatório\.__

Campo do tipo numérico

__OS3470\-S__

__CH10330\_2017__

__MFS43854__

RN25

__Regra para preenchimento do campo 10 – ‘CNPJ/CPF do prestador ou tomador’__

__Para notas recebidas:__

Recuperar a informação do campo __CPF\_CGC \(campo 06\)__ da tabela __X04\_PESSOA\_FIS\_JUR __

__Para notas emitidas:__

Recuperar a informação do campo __CGC__ da tabela __ESTABELECIMENTO __

Deve conter 11 posições \(para CPF\) ou 14 posições \(para CNPJ\)

No caso de serviço prestado no exterior campo __UF \(campo19\)__ da tabela __X04\_PESSOA\_FIS\_JUR __preenchido com ‘EX’, informe ‘99999999999999’\.

No caso de serviço prestado no Brasil sem identificação, campo __CPF\_CGC \(campo 06\)__ da tabela __X04\_PESSOA\_FIS\_JUR __sem preenchimento __E__ __UF \(campo19\)__ da tabela __X04\_PESSOA\_FIS\_JUR __<>‘EX’ informe “11111111111111”\.

__Obs\. __Campo obrigatório

Campo do tipo numérico

__OS3470\-S__

RN26

__Regra para preenchimento do campo 11 – ‘Município da nota fiscal’__

__Para notas recebidas:__

Recuperar o campo __CIDADE \(campo 16\)__ da tabela __X04\_PESSOA\_FIS\_JUR\.__

__Para notas emitidas:__

Recuperar o campo __CIDADE __da tabela __ESTABELECIMENTO\.__

__Para notas recebidas:__

Recuperar o campo __CIDADE __da tabela __ESTABELECIMENTO\.__

__Para notas emitidas:__

Recuperar o campo __CIDADE \(campo 16\)__ da tabela __X04\_PESSOA\_FIS\_JUR\.__

__Obs: __Campo obrigatório\. 

Campo do tipo alfanumérico\.

__OS3470\-S__

__MFS43270__

RN27

__Regra para preenchimento do campo 12 –‘Data de lançamento’:__

Recuperar o campo __DATA\_FISCAL__ da tabela __DWT\_DOCTO\_FISCAL__\.

__Obs: __ Campo obrigatório\.

Campo do tipo numérico\.

__OS3470\-S__

RN28

__Regra p/ inclusão do novo módulo no Manager – Mogi Mirim:__

O novo módulo “Mogi Mirim” deve ficar localizado no grupo “Municipal” 

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de Mogi Mirim”\.

__OS4429__

RN29

__Regra p/ abertura do novo módulo no Manager – Mogi Mirim:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “30805” \(Mogi Mirim\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Mogi Mirim, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS4429__

RN30

__Regra p/ inclusão do novo módulo no Manager – Votorantim:__

O novo módulo “Votorantim” deve ficar localizado no grupo “Municipal” 

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de Votorantim”\.

__MFS2105__

RN31

__Regra p/ abertura do novo módulo no Manager – Votorantim:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “57006” \(Votorantim\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Votorantim, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS2105__

RN32

__Regra p/ inclusão do novo módulo no Manager – Itatinga:__

O novo módulo “Itatinga” deve ficar localizado no grupo “Municipal” 

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de Itatinga”\.

MFS31941

RN33

__Regra p/ abertura do novo módulo no Manager – Itatinga:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “23503” \(Itatinga\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Itatinga, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

MFS31941

