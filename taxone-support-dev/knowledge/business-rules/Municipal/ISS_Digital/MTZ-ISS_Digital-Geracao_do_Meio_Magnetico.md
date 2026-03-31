# MTZ-ISS_Digital-Geracao_do_Meio_Magnetico

- **Fonte:** MTZ-ISS_Digital-Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2026-03-11
- **Tamanho:** 89 KB

---

#                                               ISS DIGITAL \- Geração do Meio Magnético

__Atenção: Regras ajustadas da OS3470\-I1A estão no novo documento de regras dos módulos municipais – DE\-PARA – Municipal\.xls\.__

__Documento disponível no diretório do CVS: documentação funcional\\Documento Matriz\\Municipal\\Regras Gerais\.__

##### DOCUMENTO DE REQUISITO 

###### DR

###### Nome

__Descrição__

OS3470\-E

Geração do Meio Magnético ISS DIGITAL

Este documento tem como objetivo criar a geração para os municípios que são atendidos pelo ISS DIGITAL\. Dessa forma usaremos o módulo de Parâmetros por Município que servirá para o usuário realizar a parametrização de todos os municípios atendidos pelo ISS DIGITAL em um único lugar\. Além disso, também realizaremos a geração dos municípios através de uma única geração, ou seja, quando o cliente clicar em um município da ISS DIGITAL será exibido a mesma tela de geração do Meio Magnético\. 

Com essa OS também criaremos as obrigações para os municípios de Corumbá e atualizaremos a geração dos municípios de Teresina, Sorocaba, Campinas, entre outros\.

OS3553\-B

DW\-MUNICIPAL\-NOVO PRODUTO \- ISS\+FACIL NOVA IGUAÇU

Este documento tem como objetivo atribuir às funcionalidades do Validador ISS Digital criado pela OS3470\-E os municípios aderentes a esta ferramenta\.

Incluir no Manager os municípios que não foram contemplados pela OS3470\-E quando foi criado o módulo ISS Digital\.

CH5563

Ajuste nos campos valor bruto da nota fiscal, código SIAFI do município e Modelo do documento\.

Este documento tem como objetivo alterar as regras de negócio para o campo valor bruto da nota fiscal do registro tipo E, alterar a forma de verificar o código SIAFI do município e alterar a regra para modelo de documento do registro tipo R\.

CH8473\_2012

DW \- MUNICIPAL \- ISS DIGITAL \- Ajuste na regra para gerar notas fiscais serviços tomados dentro município de Campinas\.

Esse chamado tem o objetivo de alterar a geração de registros de serviços tomados para que apenas carregue no arquivo notas fiscais eletrônicas \(modelo 55\) em que o município da Pessoa fis/jur cadastrada na nota fiscal seja diferente do município do estabelecimento escolhido na tela de geração

OS3470\-I1A

Ajuste nas regras gerais de recuperação Municipais – Local da prestação do Serviço

Este documento tem como objetivo ajustar a regras de tipo de recolhimento e migrar essa regra para um novo documento DE\-PARA de regras\.

CH10801

BELÉM \- Geração do Campo Motivo da Retenção/Não Retenção do Registro R incorreto\.

Este documento tem como objetivo ajustar a geração Registro R – Motivo da Retenção/Não retenção\.__ __

CH10741\_2012

CAMPO GRANDE \- Ajuste na regra para que as Notas Eletrônicas de Serviço não sejam geradas no arquivo magnético

Este documento tem como objetivo ajustar a geração do Registro R, para que recupere as notas eletrônicas somente quando o prestador for de município diferente do município da geração\.

CH21624\-A

ISS SOROCADA \- Geração do Motivo de Retenção T somente se for dentro do município

Este documento tem como objetivo ajustar a regra de geração do campo Motivo da Retenção/Não retenção do registro R\.

OS3729

DW \- MUNICIPAL \- CAMPINAS \- Geração do campo 5 \- Série / Modelo da nota fiscal do Registro Tipo ¿R¿ ¿ Notas Fiscais Recebidas da ISS Digital de Campinas incorreta\.

Este documento tem como objetivo permitir que o campo 05 – Série/Modelo da nota fiscal do registro R – Notas Fiscais Recebidas seja preenchido corretamente\.

OS3828

Geração do Meio Magnético ISS DIGITAL \- Sorocaba

CH32888/2012

DW \- MUNICIPAL \- ISS SOROCABA \- Alteração na geração do código de serviço

Permitir que o campo 19 – Código do serviço prestado do registro R seja preenchido corretamente\.

CH32888\-A/2012

DW \- MUNICIPAL \- Sorocaba \- Definição da Regra para a geração do Campo 19 \(Código de Serviço\) do ISS Digital

O objetivo deste chamado é permitir que o campo 19 – Código do Serviço do Registro R seja preenchido através da parametrização realizada na tela Municipal – Parâmetros para Município – Parâmetros – Serviços Msaf x Serviços para todos os municípios que pertencem ao validador ISS Digital\.

CH32888\-B/2012

DW \- MUNICIPAL \- Sorocaba \- Complemento da Regra para a geração do Campo 19 \(Código de Serviço\) do ISS Digital

Complementação da regra criada para o campo 19 – Código do Serviço do registro R, para que o mesmo seja demonstrado sem os separadores\.

CH25273\_2013

DW \- MUNICIPAL \- Sorocaba \- Complemento da Regra para a geração de Situação Especial

Complemento na RN10 para considerar número da inscrição municipal de

 Situação Especial para campo 02 do Registro H

CH15640\-B\_2013

DW \- MUNICIPAL \- Campinas – Complemento regra geral registro R e alteração do campo de valor bruto

Complemento na Regra p/ Registro Tipo R \(RN48\) para considerar agrupamento e alteração no campo 08 do Registro R \(RN56\)

CH30394\_2013

DW \- MUNICIPAL \- Campo Grande \- Inclusão do campo 22 no Registro Tipo R

Para o município de Campo Grande será necessário gerar o campo 22 \- CPF/CNPJ do cliente no Registro Tipo R\.

OS4331

Novo Parâmetro – Quebra do Arquivo por Data de Emissão

Implementar novo parâmetro para que seja possível realizar a quebra do arquivo por data de emissão\.

CH964\_2014

DW – MUNICIPAL – Campo Grande – Tratamento do campo 06 do Registro Tipo R

Tratamento específico para o município de Campo Grande Registro Tipo R campo Motivo da Não Retenção\.

CH10297\_2014

DW – MUNICIPAL – Campo Grande – Tratamento do campo 21 do Registro Tipo R

Tratamento específico para o município de Campo Grande Registro Tipo R campo Operação da nota fiscal recebida\.

CH12731\_2014

DW – MUNICIPAL – CAMPINAS – Tratamento do campo Data de Retenção do ISS do Registro Tipo R

Tratamento específico para o município de Campinas – Registro Tipo R, campo Data de Retenção do ISS\.

CH17654\-A\_2014

DW – MUNICIPAL – Sorocaba – Alteração do campo Motivo da Retenção/Não retenção do Registro Tipo R  

Este documento tem como objetivo alterar a geração do campo Motivo da Retenção/Não retenção do Registro Tipo R para Não incidência no município\.

CH18848\_2014

DW – MUNICIPAL – São Luis – Inclusão do município São Luis na regra de Modelo da nota fiscal / Série/Modelo da nota fiscal do Registro Tipo R

Este documento tem como objetivo alterar a geração do campo Modelo da nota fiscal / Série/Modelo da nota fiscal do Registro Tipo R, incluindo o município de São Luis\.

CH14867\-A/2014

DW \- MUNICIPAL \- CAMPINAS \- Erro na apresentação da numeração das nas fiscais no relatório de conferência

Ajuste na regra de geração do campo Número da NF incluindo regra para considerar posições à direita\.

CH15421\_2014

DW – MUNICIPAL – SOROCABA – Alteração do campo <a id="OLE_LINK47"></a><a id="OLE_LINK48"></a><a id="OLE_LINK49"></a>Série da nota fiscal/Documento da nota fiscal do Registro R

<a id="OLE_LINK50"></a><a id="OLE_LINK51"></a><a id="OLE_LINK52"></a>Este documento tem como objetivo alterar a geração do campo Série da nota fiscal/Documento da nota fiscal do Registro R para o município de Sorocaba, incluindo tratamento para NF de outro Município\.

CH22152\_2014

DW – MUNICIPAL – Teresina – Inclusão do município Teresina na regra de Modelo da nota fiscal / Série/Modelo da nota fiscal do Registro Tipo R

Este documento tem como objetivo alterar a geração do campo Modelo da nota fiscal / Série/Modelo da nota fiscal do Registro Tipo R, incluindo o município de Teresina\.

CH14865\_2014

DW – MUNICIPAL – CAMPINAS – Alteração do campo Série da nota fiscal/Documento da nota fiscal do Registro R

<a id="OLE_LINK23"></a><a id="OLE_LINK24"></a><a id="OLE_LINK25"></a>Este documento tem como objetivo alterar a geração do campo Série da nota fiscal/Documento da nota fiscal do Registro R para o município de Campinas, incluindo tratamento para NF de outro Município\.

CH26113\_2014

DW – MUNICIPAL – SOROCABA – Alteração do <a id="OLE_LINK53"></a><a id="OLE_LINK54"></a><a id="OLE_LINK55"></a>campo Modelo da nota fiscal / Série/Modelo da nota fiscal

<a id="OLE_LINK56"></a><a id="OLE_LINK57"></a><a id="OLE_LINK58"></a>Este documento tem como objetivo alterar a geração do campo Modelo da nota fiscal / Série/Modelo da nota fiscal do Registro R para o município de Sorocaba, incluindo tratamento para NF de outro Município\.

MFS1218

Novo Parâmetro – Gerar Arquivos por Data de Emissão

Implementar novo parâmetro para que seja possível gerar o arquivo por data de emissão\.

MFS1699

DW – MUNICIPAL – SOROCABA – Inclusão dos registros faltantes\.

Inclusão dos Registros E e D, faltantes no arquivo de registros do município de Sorocaba\. 

CH15374\_2015

DW \- MUNICIPAL – ISS DIGITAL – Retirada do range da data inicial e final

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

CH24395\_2015

DW – MUNICIPAL – SOROCABA – Inclusão do campo 22 Matrícula CEI/Processo Administrativo no Registro R

Este documento tem como objetivo incluir na geração o campo 22 Matrícula CEI/Processo Administrativo no Registro R para o município de Sorocaba\.

CH26692\_2015

DW – MUNICIPAL – UBERLANDIA – Alteração do campo Série da nota fiscal/Documento da nota fiscal do Registro R

Este documento tem como objetivo alterar a geração do campo Série da nota fiscal/Documento da nota fiscal do Registro R para o município de Uberlândia, incluindo tratamento para Outros Municípios\.

CH28829\_2015

DW – MUNICIPAL – UBERLANDIA – Inclusão do campo Cliente do Registro R

Este documento tem como objetivo incluir o campo Ciente para o município de Uberlândia com preenchimento zerado conforme estabelece a Prefeitura\.

CH7230\_2016

DW – MUNICIPAL – CAMPINAS – Alteração do campo Modelo da nota fiscal / Série/Modelo da nota fiscal do Registro R

Este documento tem como objetivo alterar o preenchimento do campo Modelo da nota fiscal / Série/Modelo da nota fiscal do Registro Tipo R para o município de Campinas\.

CH9821\_2016

DW – MUNICIPAL – BELÉM – Inclusão do campo Cliente do Registro R

Este documento tem como objetivo incluir o campo Cliente para o município de Belém com preenchimento zerado por não tratarmos o preenchimento da Operação como J\. *Obs\.:* Algumas Prefeituras estão solicitando que o campo seja preenchido com zeros, mesmo existindo a informação no layout\.

CH7320\_2016

DW – MUNICIPAL – TERESINA – Inclusão do campo Cliente do Registro R

Este documento tem como objetivo incluir o campo Cliente para o município de Teresina com preenchimento zerado por não tratarmos o preenchimento da Operação como J\. *Obs\.:* Algumas Prefeituras estão solicitando que o campo seja preenchido com zeros, mesmo existindo a informação no layout\.

CH25417\_2016

DW – MUNICIPAL – CAMPINAS – Alteração do campo __Código do Serviço Prestado__ do Registro R\.

Este documento tem como objetivo alterar a regra de negócio do Código do Serviço Prestado \- Registro R para o município de __CAMPINAS__ considerar o preenchimento do campo na geração quando o prestador for de outro município E do mesmo município\.

MFS\-31470 e 31480

DW – MUNICIPAL – Alteração da regra dos campos de código SIAFI do Registro R, para o município de São Luis\.

Ajuste na regra dos campos Código SIAFI do município do prestador do serviço \(RN65\) e Código SIAFI do município do local da prestação do serviço \(RN69\), para inserir zeros a esquerda ao código do município até atingir o tamanho máximo do campo \(10 posições\), para o município de São Luis\.

MFS82097

DW – MUNICIPAL – Campinas – Tratamento do campo 21 do Registro Tipo R

Tratamento específico para o município de Campinas Registro Tipo R campo Operação da nota fiscal recebida\.

MFS\-562118

Alteração nome do validador ISS\_DIGITAL para NFSe Campinas

Este documento tem como objetivo tratar a geração do meio magnético em TXT dos Registro tipo “R” \- Notas Recebidas e Registro tipo “D” \- Dedução de Materiais da NF Emitidas de Const\. Civil, no novo validador NFSe Campinas\.

MFS\-643430

Denílson André Santos

Este documento, tem o objetivo de readequar o tratamento de regras, para as situações tributáveis e, de não incidência no município \(RN54\.a e RN54\.c\), destinada a cidade de Campo Grande \- MS\.

MFS\-659278

Denílson André Santos

Este documento, tem o objetivo de readequar o tratamento da regra RN54\.c que, trata dos detalhes de não incidência/não incidente no município, destinada a cidade de Campo Grande \- MS\.

MFS 682807

Bruna Mariel Ribeiro

Este documento, tem o objetivo de readequar o tratamento da regra RN54\.c que, trata dos detalhes do motivo da retenção no município, destinada a cidade de Campo Grande \- MS\.

MFS869438

Rogério Ohashi

Este documento tem por objetivo corrigir a regra de geração dos Campo 03\-Versão do sistema dá ISSO e do Campo 05\-Modelo específico para o Município de Uberlândia\.

MFS\-839828

Rosemeire Santos

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

MFS\-895669

Rosemeire Santos

Este documento tem o objetivo, incluir o município de Nova Iguaçu/RJ, ao grupo de municípios atendidos pelo validador ISS Digital\.

MFS\-912835

Rafael Fabiano

Este documento tem o objetivo, incluir o município de Triunfo/RS, ao grupo de municípios atendidos pelo validador ISS Digital\.

MFS\-917355

Andréa Rocha

Alteração da regra de preenchimento do campo “18\-Enquadramento no Simples Nacional do tomador de serviços” do Registro Tipo “R”, para preencher com “N” quando não tiver valor, para o município de Uberlândia\.

MFS\-926968

Rafael Fabiano

Este documento tem o objetivo, incluir o município de Montes Claros/MG, ao grupo de municípios atendidos pelo validador ISS Digital\.

MFS\-1000560

Alessandra Navatta

Este documento tem o objetivo incluir/alterar para o município de Uberlândia:

- Registro tipo H, o campo versão do sistema da ISS Digital \(RN11\),
- Registro R – Modelo da nota fiscal / Série/Modelo da nota fiscal, para as notas recebidas \(RN53\.a\)

MFS\-1053904

Rosemeire Santos

Este documento tem o objetivo alterar Registro tipo H, o campo versão 400 do sistema da ISS Digital \(RN11\)

para o município de Uberlândia\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

__Regra p/ inclusão do novo módulo no Manager – Corumbá:__

O novo módulo “Corumbá” deve ficar localizado no grupo “Municipal” 

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados do município de Corumbá”\.

OS3470\-E

__RN02__

__Regra p/ abertura do novo módulo no Manager – Corumbá:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “MS” e ao código de município do IBGE igual a “3207” \(Corumbá\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Corumbá, Mato Grosso do Sul\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS3470\-E__

__RN03__

__Estrutura de menus do módulo ISS DIGITAL:__

__\[MFS\-562118\] \-__ __Regra Campinas: Estrutura de menus do módulo NFSe Campinas:__

Deverão ser criados os seguintes menus e sub\-menus no módulo ISS DIGITAL:

- Arquivo
- Manutenção
	- Deduções
- Obrigações
	- Geração Meio Magnético
	- Geração Meio Magnético Bancos
	- Arquivo de Entradas de Serviços \(Const\. Civil/ Utilities/ Telecom\)
- Janela
- Ajuda 

*Observação para desenvolvimento:* Os packages da geração normal e da geração de situação especial \(Arquivo de Entradas de Serviços\) estão separados, porém a estrutura do arquivo magnético dos dois deve ser a mesma estabelecida por esse documento matriz, em que a diferença entre eles é a recuperação dos documentos fiscais e será gerado para o arquivo de situação especial apenas documentos fiscais de entrada\.

__OS3470\-E__

__MFS\-562118__

__RN04__

__Regra de criação do nome do arquivo__

Quando o parâmetro Quebrar Arquivos por Data de Emissão estiver desmarcado será gerado apenas um arquivo com a nomenclatura do arquivo normal indicado abaixo\.

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ MMAAAA\.TXT__, onde:

__       MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

       __\.TXT__: extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\.XML

__ISSDIGITAL\_MUNICIPIO\_DDMMAAAA\.txt__, onde:

- __ISSDIGITAL__: representa a obrigação que está sendo gerada\.
- __MUNICIPIO__: representa o município que está sendo gerado\.
- __DDMMAAAA__: representa a data inicial da geração\.
- __\.txt__: extensão do arquivo\.

Ex: ISSDIGITAL\_CAMPINAS\_01012010\.txt

__\[MFS\-562118\]__ __Regra Campinas; __Nome do arquivo

NFSE\_CAMPINAS\_01012010\.txt

Caso o parâmetro Gerar Arquivos por Data de Emissão estiver marcado, não será possível marcar o parâmetro Quebrar Arquivos por Data de Emissão e deverá ser realizada a seguinte verificação: 

Este arquivo deverá conter __todas__ as notas fiscais com data de emissão dentro do período de referência\.

Caso o parâmetro Quebrar Arquivos por Data de Emissão estiver marcado, não será possível marcar o parâmetro Gerar Arquivos por Data de Emissão e deverá ser realizado a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente a data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverão ser:

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\_MMAAAA\.TXT__, onde:

       __DDMMAAAA__: representa a data inicial da geração\.   

__       MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__      __ __\.TXT__: extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\_012010\.TXT

__ISSDIGITAL\_MUNICIPIO\_DDMMAAAA\_MMAAAA\.txt__, onde:

- __ISSDIGITAL__: representa a obrigação que está sendo gerada\.       
- __MUNICIPIO__: representa o município que está sendo gerado\.
- __DDMMAAAA__: representa a data inicial da geração\.
- __MMAAAA: __mês da competência referente à nota gerada\.
- __\.txt__: extensão do arquivo\.

Ex: ISSDIGITAL\_CAMPINAS\_01122013\_122009\.txt

Obs: Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__\[MFS\-562118\]__ __Regra Campinas; __Nome do arquivo

NFSE\_CAMPINAS\_01122013\_122009\.txt

__OS3470\-E__

__OS4331__

__MFS1218__

__MFS\-562118__

__MFS\-839828__

__RN05__

__Regra p/ tela da Geração do Meio Magnético \(Demais Municípios\)__

A tela de geração do meio magnético deve exibir os seguintes campos:

Data Inicial: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

Data Final: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__\[ALTERADA \- CH15374\_2015\]__

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

__\[MFS\-562118\]__ __Regra Campinas; __O Registro Tipo “E”, está desabilitado\.

Gerar Registro Tipo “E” – Notas Emitidas: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Gerar Registro Tipo “D” – Dedução de Materiais da NF Emitidas de Constr\. Civil: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Gerar Registro Tipo “R” – Notas Recebidas: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Quebrar arquivo por Data de Emissão: deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Estabelecimento: o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__OS3470\-E__

__OS3828__

__OS4331__

__MFS1218__

__MFS1699__

__CH15374\_2015__

__MFS\-562118__

__RN06__

__Regra p/ geração do arquivo magnético__

Cada registro especificado abaixo corresponde a uma linha de arquivo texto\. 

O registro do tipo “H”\. Este registro deverá ser único no arquivo\.

Todos os registros deverão ser finalizados pelos caracteres especiais de carriage return e line feed \(asc 13 \+ asc 10\)\.

Após o último registro, deve existir o caractere de fim de arquivo \(asc 26\)\.

__OS3470\-E__

__RN07__

__Regra p/ preenchimento dos campos do arquivo magnético__

A forma de preenchimento dos campos no arquivo deve ser realizada da seguinte maneira:

Campos do tipo N \(Numéricos\) Ex\. Inscrição Municipal, CNPJ, Valor da Nota Fiscal deverão ser preenchidos com zeros à esquerda até atingir o tamanho exato do campo\.

Campos do tipo A \(Alfanuméricos\) Ex\. Nome do Tomador/Prestador, Código do SIAFI da Prestação do Serviço, deverão ser preenchidos com espaços à direita\.

Campos do tipo D \(Data\) deverão ser preenchidos no formato dd/mm/aaaa\.

Todos os campos deverão obedecer ao tamanho e a formatação definido neste layout\.

__OS3470\-E__

__RN08__

__Regra p/ Registro Tipo H__

Primeiro registro do arquivo, contém a Inscrição Municipal da empresa e a versão do sistema\.

Deve existir apenas um registro tipo “H” por arquivo\.

__OS3470\-E__

__RN09__

__Registro H – Identificação do Registro: __

Preencher com o texto fixo “H”\.

__OS3470\-E__

__RN10__

__Registro H –  CMC pra indicar empresa: __

Preencher com o campo INSCR\_MUNICIPAL da tabela ESTABELECIMENTO\.

__\[ALTERADO – CH25273\_2013\]__

Na geração por Situação Especial Obrigações >> Arquivo de Entradas de Serviços \(Const\. Civil/ Utilities/ Telecom\) recuperar informação de acordo com a parametrização da __RN03__ do documento MTZ \- MUNICIPAL \- ISS Digital \- Geração meio magnético – sit\. especial\.doc\.

__OS3470\-E__

__CH25273\_2013__

__RN11__

__Registro H –  Versão do sistema da ISS Digital: __

Preencher com:

400, quando a obrigação for de Belém e Uberlândia\.

200, quando a obrigação for de Teresina ou Nova Iguaçu

300, quando a obrigação for de Sorocaba, Corumbá, Nova Iguaçu e Triunfo, e Uberlândia\.

600, quando a obrigação for de São Luis

100, quando a obrigação for de Campinas

500, quando a obrigação for de Campo Grande

__OS3470\-E__

__/__

__OS3553\-B__

__MFS869438__

__MFS\-895669__

__MFS\-912835__

__MFS\-926968__

__MFS\-1000560__

__MFS\-1053904__

__RN12__

__Regra p/ Registro Tipo E__

__\[MFS\-562118\]__ __Regra Campinas; __O Registro Tipo E, não será gerado\.

Este registro deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência __exceto__ quando o parâmetro “Gerar Arquivos por Data de Emissão” na tela de geração estiver marcado, caso o parâmetro estiver marcado deverá ser considerado a Data de Emissão dentro do período de referência\.

__OS3470\-E__

__MFS1218__

__MFS\-562118__

__RN13__

__Registro E – Identificação do Registro: __

Preencher com o texto fixo “E”\.

__OS3470\-E__

__RN14__

__Registro E – Data de Emissão:__ 

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. \(campo 11 da SAFX07\)\. Formato: 99/99/9999\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher como campo DAT\_CANCELAMENTO da DWT\_DOCTO\_FISCAL\. \(campo 94 da SAFX07\)

__OS3470\-E__

__RN15__

__Registro E – Série da nota fiscal: __

Preencher com o campo Série ISS Digital da tela Municipal – Parâmetros por Município – Modelo Msaf x Série ISS Digital referente ao modelo cadastrado na nota\.

__OS3470\-E__

__RN16__

__Registro E – Modelo da nota fiscal: __

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. \(campo 09 da SAFX07\)

__OS3470\-E__

__RN17__

__Registro E – Tributação da nota fiscal emitida : __

Preencher com:

H, verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “07”\.

C, verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “04”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\.

E, verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “06”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “432”\.

F, verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “01”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420”\.

K, verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “03”, s se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “427”\.

N, verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “09”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “444”\.

T, verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “10”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “445”\.

G, verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “02”, s se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “421”\.

P, quando o campo “Série da nota fiscal” = ‘AV’

__OS3470\-E__

__RN18__

__Registro E – Número da nota fiscal: __

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. \(campo 08 da SAFX07\)\.

\[__CH14867\-A/2014__\]

Na geração deste campo, deve ser consideradas 9 posições da direita para a esquerda do número da NF, considerando que os caracteres que serão suprimidos à esquerda \(da posição 10 a 12\) devem ser zeros\. Se o conteúdo do campo NUM\_DOCFIS tiver mais de 9 posições significativas \(sem zeros à esquerda\), gerar o número truncado, mas retornar no log a seguinte mensagem: “O campo Número do Documento \(NUM\_DOCFIS\) ultrapassou o tamanho máximo permitido \(9 posições\)\.”

\(Ex para esta situação: Nº de NF 12345678900 será gerado 345678900\)\.

Para a obrigação de Campinas, quando o campo Modelo da Nota Fiscal = “G”, esse campo deve ser preenchido com zeros\.

__OS3470\-E__

__CH14867\-A/2014__

__RN19__

__Registro E – Valor bruto da nota fiscal: __

Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV\. \(campo da SAFX09\)

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\) , preencher com zeros\.

Alterado CH5563

Se o campo COD\_CLASS\_DOC\_FIS da tabela DWT\_DOCTO\_FISCAL = ‘3’

Preencher com o campo VLR\_TOT\_NOTA da tabela DWT\_DOCTO\_FISCAL

__OS3470\-E__

__CH5563__

__RN20__

__Registro E – Valor do serviço: __

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\. \(campo 14 da SAFX09\)

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\) , preencher com zeros\.

__OS3470\-E__

__RN21__

__Registro E – Tipo de recolhimento do ISS: __

Para que esse campo seja preenchido com “A”, é necessário que pelo menos umas das seguintes opções seja verdadeira:

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se estiver preenchido, verificar se está preenchido com “2”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota utilizando o município cadastrado no estabelecimento\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

Caso nenhuma das opões seja verdadeira, preencher com “R”\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\) , preencher com brancos\.

__Obs\.: Regra ajustada no documento DE\-PARA – Municipal\.xls \(E1\-RN0001\)__

__OS3470\-E__

__OS3470\-I1A__

__RN22__

__Registro E – Alíquota de ISS: __

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. \(campo 32 da SAFX09\)\. Formato: 99\.99

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher com zeros\.

Se o declarante for optante pelo simples nacional, preencher com zeros\.

__OS3470\-E__

__RN23__

__Registro E – CNPJ do tomador de serviços: __

Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota quando o tamanho do campo for igual a 14\. \(campo 06 da SAFX04\)

Se o tomador for estrangeiro, preencher com zeros\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher com zeros\.

__OS3470\-E__

__CH5563__

RN24

__Registro E – CPF do tomador de serviços: __

Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota quando o tamanho do campo for igual a 11\. \(campo 06 da SAFX04\)

Se o campo tiver 14 posições ou o tomador for estrangeiro, preencher com zeros\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\) , preencher com zeros\.

__OS3470\-E__

RN25

__Registro E – Nome do tomador de serviços: __

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota \(campo 05 da SAFX04\)

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\) , preencher com brancos\.

__OS3470\-E__

RN26

__Registro E – Código SIAFI do município do tomador de serviços: __

Preencher com o campo COD\_MUNIC\_SIAFI da tabela PRT\_MUNIC\_SIAFI referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\. \(campo 25 da safx04\)\. O campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR deve ser igual ao campo COD\_MUNIC\_MSAF da tabela PRT\_MUNIC\_SIAFI\. 

Para tomador de serviços estrangeiro, usar “9999” e não informar CPF ou CNPJ\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\) , preencher com brancos\.

__\[ALTERAÇÃO\-MFS\-895669\] – Desconsiderar este campo na geração do arquivo para o município de Nova Iguaçu/RJ\.__

__OS3470\-E__

__MFS\-895669__

RN27

__Registro E – Código da atividade CNAE relacionada ao serviço: __

Preencher com o campo COD\_ATIVIDADE da tabela ESTABELECIMENTO referente estabelecimento escolhido na tela de parâmetros da geração do meio magnético\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher com brancos\.

__\[ALTERAÇÃO\-MFS\-895669\] – Desconsiderar este campo na geração do arquivo para o município de Nova Iguaçu/RJ\.__

__OS3470\-E__

__MFS\-895669__

__RN28__

__Registro E – Código SIAFI do município do local da prestação do serviço: __

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota e COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL estiver preenchido:

Esse campo será preenchido com o campo COD\_MUNIC\_SIAFI da tabela PRT\_MUNIC\_SIAFI referente ao campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\. 

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota e COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL não estiver preenchido:

Exibir a mensagem no log: “O campo Cod Munic ISS não está preenchido para a nota” concatenada com o número da nota fiscal\.

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS <> ‘1’ referente ao serviço cadastrado na nota:

Esse campo será preenchido com o campo COD\_MUNIC\_SIAFI da tabela PRT\_MUNIC\_SIAFI referente ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\. 

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher com brancos\.

*Obs: O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS\.*

__*Alterado CH5563*__

*Para verificar o código do município a ser recuperado:*

*O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS*

*Deve se utilizar o código do município IBGE \(campo COD\_MUNIC\_MSAF\) correspondente na tabela X2097\_MUNIC\_ISS para recuperar o *campo COD\_MUNIC\_SIAFI da tabela PRT\_MUNIC\_SIAFI

__\[ALTERAÇÃO\-MFS\-895669\] – Desconsiderar este campo na geração do arquivo para o município de Nova Iguaçu/RJ\.__

__OS3470\-E__

__CH5563__

__MFS\-895669__

__RN29__

__Registro E – Número final do intervalo: __

Preencher com zeros\.

__OS3470\-E__

__RN30__

__Registro E – Situação da Nota: __

Preencher com:

E, quando o campo IND\_NOTA\_SERVICO da tabela DWT\_DOCTO\_FISCAL = ‘E’  \(campo 137 da SAFX07\)

C, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = ‘S’   \(campo 30 da SAFX07\)

N, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> ‘S’ \(campo 30 da SAFX07\)

__OS3470\-E__

__RN31__

__Registro E – Enquadramento no Simples Nacional do Tomador de Serviços: __

Preencher com o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR\. \(campo 43 da SAFX04\)

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\) , preencher com brancos\.

__OS3470\-E__

__RN32__

__Registro E – Operação da nota fiscal emitida: __

Preencher com:

D, quando o campo NORM\_DEV da tabela DWT\_DOCTO\_FISCAL = ‘2’ \(campo 04 da SAFX07\)

G, quando o campo IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota\.

I, quando campo IND\_ISS da tabela ESTABELECIMENTO = ‘08’

C, verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “01” ou “04”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros por Município – Classificação de Serviços – Município com o COD\_PARAM = “420” ou “433”\.

H, verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “02”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros por Município – Classificação de Serviços – Município com o COD\_PARAM = “421”\.

B, o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV > 0\. 

A, o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV = 0 ou quando não estiver preenchido\. 

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher com brancos\.

__OS3470\-E__

__RN33__

__Regra p/ Registro Tipo D – Dedução de Materiais e Subempreitadas das NF Emitidas de Const\. Civil__

Para que esse registro seja gerado a nota fiscal emitida deverá ser de construção civil \(IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota\)\.

Para cada dedução de uma nota deverá ser informado um registro D\. Não há limites de registro D por arquivo, desde que haja um registro E relacionado\.

Quando a nota for de construção civil, a geração deve verificar se existe dedução de material ou subempreitada para essa nota no menu Manutenção – Deduções\. Se houver a geração deve apresentar um registro para a nota emitida \(tipo E\) e tantos quantos forem os registros de dedução \(tipo D\)\.

__MFS\-562118 \- Regra para Campinas:__

Quando a nota for de construção civil, a geração deve verificar se existe dedução de material ou subempreitada para essa nota no menu Manutenção – Deduções\. A geração desses registros deve ser independente da geração dos registros \(tipo E\) 

__OS3470\-E__

__MFS\-562118__

__RN34__

__Registro D – Identificação do registro__

Preencher com texto fixo “D”

__OS3470\-E__

__RN35__

__Registro D – Data da emissão da NF emitida \(de qual deve deduzir\)__

Preencher com o campo Data Emissão da nota fiscal que será deduzida na tela Manutenção – Deduções\. \(mestre\) Formato: 99/99/9999\.

__OS3470\-E__

__RN36__

__Registro D – Serie da NF emitida \(De qual deve deduzir\)__

Preencher com o campo Série DMS da tela Parâmetros – Modelo Msaf x Série DMS referente ao tipo de documentos cadastrado na nota\. \(mestre\)

__OS3470\-E__

__RN37__

__Registro D – Modelo da NF Emitida \(de qual deve deduzir\)__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL da nota fiscal que será deduzida na tela Manutenção – Deduções\. \(mestre\)

__OS3470\-E__

__RN38__

__Registro D – Numero de identificação da NF emitida \(de qual deve deduzir\)__

Preencher com o campo Numero Doc\. Fiscal da nota fiscal que será deduzida na tela Manutenção – Deduções\. \(mestre\)

\[__CH14867\-A/2014__\]

Na geração deste campo, deve ser consideradas 9 posições da direita para a esquerda do número da NF, considerando que os caracteres que serão suprimidos à esquerda \(da posição 10 a 12\) devem ser zeros\. Se o conteúdo do campo NUM\_DOCFIS tiver mais de 9 posições significativas \(sem zeros à esquerda\), gerar o número truncado, mas retornar no log a seguinte mensagem: “O campo Número do Documento \(NUM\_DOCFIS\) ultrapassou o tamanho máximo permitido \(9 posições\)\.”

\(Ex para esta situação: Nº de NF 12345678900 será gerado 345678900\)\.

__OS3470\-E__

__CH14867\-A/2014__

__RN39__

__Registro D – Valor bruto da NF emitida \(de qual deve deduzir\)__

Preencher com o campo Valor Total da Nota da nota fiscal que será deduzida na tela Manutenção – Deduções\. \(mestre\)

__OS3470\-E__

__RN40__

__Registro D – Tipo da Dedução__

Preencher com o campo Tipo de Dedução da tela Manutenção – Deduções\.

__OS3470\-E__

__RN41__

__Registro D – Numero de Identificação da NF \(a deduzir\)__

Preencher com o campo Nº Nota Fiscal da nota fiscal que será deduzida na tela Manutenção – Deduções\. \(detalhe\)

__OS3470\-E__

__RN42__

__Registro D – Valor bruto da NF \(a deduzir\)__

Preencher com o campo Valor da Nota da nota fiscal que será deduzida na tela Manutenção – Deduções \(detalhe\)

__OS3470\-E__

__RN43__

__Registro D – Valor do material a deduzir__

Preencher com o campo Valor Dedução da nota fiscal que será deduzida na tela Manutenção – Deduções\. \(detalhe\)

__OS3470\-E__

__RN44__

__Registro D – CNPJ do prestador do serviço__

Preencher com o campo CGC da tabela ESTABELECIMENTO quando tiver 14 posições\.

Quando for pessoa física ou estrangeiro, preencher com zeros\.

__OS3470\-E__

__RN45__

__Registro D – CPF do prestador do serviço__

Preencher com o campo CGC da tabela ESTABELECIMENTO quando tiver 11 posições\.

Quando for pessoa jurídica ou estrangeiro, preencher com zeros\.

__OS3470\-E__

__RN46__

__Registro D – Nome do prestador do serviço__

Preencher com o campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO 

__OS3470\-E__

__RN47__

__Registro D – Código SIAFI do município do tomador de serviços__

Preencher com o campo COD\_MUNIC\_SIAFI da tabela PRT\_MUNIC\_SIAFI referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR referente ao campo Pessoa Fis/Jur da nota fiscal a ser deduzida\. \(campo 25 da safx04\)\. O campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR deve ser igual ao campo COD\_MUNIC\_MSAF da tabela PRT\_MUNIC\_SIAFI\. 

Gravar '9999' se a PFJ for estrangeira\.

__\[ALTERAÇÃO\-MFS\-895669\] – Desconsiderar este campo na geração do arquivo para o município de Nova Iguaçu/RJ\.__

__OS3470\-E__

__MFS\-895669__

__RN48__

__Regra p/ Registro Tipo R__

Este registro deve conter todas as notas com as seguintes características:

- Nota de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência __exceto__ quando o parâmetro “Gerar Arquivos por Data de Emissão” na tela de geração estiver marcado, caso o parâmetro estiver marcado deverá ser considerado a Data de Emissão dentro do período de referência\.
- Nota não cancelada \(situacao <> ‘S’\)

\-     Para considerar notas fiscais eletrônicas verificar: 

Se o município do prestador \(campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\) for __DIFERENTE__ do município do módulo selecionado para geração \(COD\_MUNICIPIO da tabela ESTABELECIMENTO\), recuperar os documentos com uma das situações abaixo:

\- Modelo do Documento \(campo COD\_MODELO da tabela DWT\_DOCTO\_FISCAL = ‘55’\) __OU__

\- Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal\.

O campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR está relacionado com o campo COD\_MUNIC\_ISS da tabela X2097\.

__NÃO__ gerar as Notas Fiscais de Serviço no arquivo Meio Magnético\.

__Considerações importantes:__

- __ \(CAMPINAS\) __Os registros devem ser agrupados pelos campos Código do Serviço \(verificar condições de geração deste campo na RN68\) e Valor da Alíquota ISS \(verificar condições de geração deste campo na RN58\)\.

__OS3470\-E__

__/__

__CH8473\_2012__

__CH10741__

__CH15640\-B\_2013__

__MFS1218__

__RN49__

__Registro R – Identificação do Registro: __

Preencher com o texto fixo “R”\.

__OS3470\-E__

__RN50__

__Registro R – Data de retenção do ISS: __

Preencher com o campo DT\_PAGTO\_NF da tabela DWT\_DOCTO\_FISCAL\. \(campo 175 da SAFX07\), quando pelo menos uma das opções abaixo seja verdadeira:

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL está preenchido\. Se estiver preenchido, verificar se está preenchido com “1”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota utilizando o município cadastrado no estabelecimento\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

*Obs: Se o campo DT\_PAGTO não estiver preenchido, deve\-se preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. Essa informação será incluída no manual operacional para conhecimento do cliente\.*

Caso nenhuma das opões seja verdadeira, preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. \(campo 11 da SAFX07\) Formato: 99/99/9999\.

__\[ALTERADA – CH12731\_2014\] __

- __\(CAMPINAS\) __Apenas para o município de Campinas, Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. \(campo 11 da SAFX07\) Formato: __99/99/9999__\.

__OS3470\-E__

__CH12731\_2014__

__RN51__

__Registro R – Data de emissão da nota fiscal: __

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. \(campo 11 da SAFX07\) Formato: 99/99/9999\.

__OS3470\-E__

__RN52__

<a id="OLE_LINK26"></a><a id="OLE_LINK27"></a><a id="OLE_LINK28"></a>__Registro R – Série da nota fiscal / Documento da nota fiscal: __

Preencher com o campo Série para o ISS Digital da tela Municipal – Parâmetros por Município – Modelo Msaf x Série referente ao modelo cadastrado na nota\.

__OS3470\-E__

__MFS\-895669__

__MFS\-912835__

__MFS\-926968__

__RN52\.a__

__Registro R – __<a id="OLE_LINK15"></a><a id="OLE_LINK16"></a><a id="OLE_LINK17"></a><a id="OLE_LINK18"></a><a id="OLE_LINK43"></a><a id="OLE_LINK44"></a><a id="OLE_LINK45"></a><a id="OLE_LINK46"></a>__Série da nota fiscal / Documento da nota fiscal \(Sorocaba\): __

Preencher com o campo Série para o ISS Digital da tela Municipal – <a id="OLE_LINK29"></a><a id="OLE_LINK30"></a><a id="OLE_LINK31"></a><a id="OLE_LINK32"></a>Parâmetros <a id="OLE_LINK40"></a><a id="OLE_LINK41"></a><a id="OLE_LINK42"></a>por Município – Modelo Msaf x Série referente ao modelo cadastrado na nota\.

<a id="OLE_LINK37"></a><a id="OLE_LINK38"></a><a id="OLE_LINK39"></a>Tratamento para Série <a id="OLE_LINK33"></a><a id="OLE_LINK34"></a><a id="OLE_LINK35"></a><a id="OLE_LINK36"></a>OM \(NF de outro município\):

- Uma NF com a pessoa PFJ vinculada que esteja estabelecida em um município diferente de Sorocaba, será sempre preenchida com “OM \- NF de outro município”;
- Terão casos em que o contribuinte pode ter um mesmo modelo de documento cadastrado em notas fiscais diferentes e que precisam ser cadastradas com séries diferentes dependendo da operação, porém não tem como vincular séries diferentes para o mesmo modelo de documento;
- O parâmetro então só será considerado quando o município do prestador cadastrado na nota fiscal for igual ao município de Sorocaba\.

__CH15421\_2014__

__RN52\.b__

__Registro R – Série da nota fiscal / Documento da nota fiscal \(Campinas\): __

Preencher com o campo Série para o ISS Digital da tela Municipal – Parâmetros por Município – Modelo Msaf x Série referente ao modelo cadastrado na nota\.

Tratamento para Série OM \(NF de outro município\):

- Uma NF com a pessoa PFJ vinculada que esteja estabelecida em um município diferente de Campinas, será sempre preenchida com “OM \- NF de outro município”;
- Terão casos em que o contribuinte pode ter um mesmo modelo de documento cadastrado em notas fiscais diferentes e que precisam ser cadastradas com séries diferentes dependendo da operação, porém não tem como vincular séries diferentes para o mesmo modelo de documento;
- O parâmetro então só será considerado quando o município do prestador cadastrado na nota fiscal for igual ao município de Campinas\.

__CH14865\_2014__

__RN52\.c__

__Registro R – Série da nota fiscal / Documento da nota fiscal \(Uberlândia\): __

Preencher com o campo Série para o ISS Digital da tela Municipal – Parâmetros por Município – Modelo Msaf x Série referente ao modelo cadastrado na nota\.

Tratamento para Série OM \(Outros Municípios\):

- Uma NF com a pessoa PFJ vinculada que esteja estabelecida em um município diferente de Uberlândia, será sempre preenchida com “OM \- Outros Municípios”;
- Terão casos em que o contribuinte pode ter um mesmo modelo de documento cadastrado em notas fiscais diferentes e que precisam ser cadastradas com séries diferentes dependendo da operação, porém não tem como vincular séries diferentes para o mesmo modelo de documento;
- O parâmetro então só será considerado quando o município do prestador cadastrado na nota fiscal for igual ao município de Uberlândia\.

__CH26692\_2015__

__RN53__

__Registro R – Modelo da nota fiscal / Série/Modelo da nota fiscal:__

<a id="OLE_LINK12"></a><a id="OLE_LINK13"></a><a id="OLE_LINK14"></a>Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. \(campo 09 da SAFX07\)\.

__OS3470\-E__

__CH5563__

__OS3729__

__MFS\-895669__

__MFS\-912835__

__MFS\-926968__

__RN53\.a__

<a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>__Registro R – Modelo da nota fiscal / Série/Modelo da nota fiscal \(Belém/São Luis/Teresina/Uberlândia\): \[ALTERADA – CH18848\_2014/CH22152\_2014/MFS869438\]__

<a id="OLE_LINK9"></a><a id="OLE_LINK10"></a><a id="OLE_LINK11"></a>Preencher com espaços em branco\.

__CH5563__

__CH18848\_2014__

__CH22152\_2014__

__MFS869438__

__MFS\-1000560__

__RN53\.b__

__Registro R – __<a id="OLE_LINK19"></a><a id="OLE_LINK20"></a><a id="OLE_LINK21"></a><a id="OLE_LINK22"></a>__Modelo da nota fiscal / Série/Modelo da nota fiscal \(Sorocaba\):__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 09 da SAFX07\), porém se o campo Série da nota fiscal / Documento da nota fiscal \(RN52\.a\) gerar igual a “OM” preencher com espaços em branco\.

__CH26113\_2014__

__RN53\.c__

__Registro R – Modelo da nota fiscal / Série/Modelo da nota fiscal \(Campinas\):__

Esse campo usará para preenchimento da série o que for parametrizado em Municipal – Parâmetros por Município – Modelo Msaf x Série de acordo com a regra a seguir, essa é a mesma parametrização utilizada na RN52\.b, pois os campos 04\-Documento da nota fiscal e 05\-Série / Modelo da nota fiscal são vinculados para validação no ISS, de acordo com o documento da nota é que será definida a série/ modelo porque na nota fiscal física não é obrigatório o preenchimento da série/ subsérie em alguns casos, porém o validador espera dependendo do tipo do documento\.

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 09 da SAFX07\), quando o campo série da parametrização da tela Municipal – Parâmetros por Município – Modelo Msaf x Série referente ao modelo cadastrado na nota estiver gravado com as seguintes opções:

10 \- NF Servico M01, Serie A/Bloco

11 \- NF Servico M01, Serie A/ Jogo Solto

12 \- NF Servico M01, Serie A/ Formulario Continuo

40 \- NF Simplificada de Servicos M02, Serie B/Bloco

42 \- NF Simplificada de Servicos M02, Serie B/Formulario Continuo

50 \- NF Fatura de Servico M01, Serie A/Bloco

51 \- NF Fatura de Servico M01, Serie A/ Jogo Solto

52 \- NF Fatura de Servico M01, Serie A/ Formulario Continuo

55 \- NF Conjugada Eletronico \(ESTADO\)M55

70 \- NF Conjugada M01/Bloco

71 \- NF Conjugada M01/Jogo Solto

72 \- NF Conjugada M01/Formulario Continuo

73 \- NF Conjugada M07/Bloco

74 \- NF Conjugada M07/Formulario Continuo

75 \- NF Conjugada M07/Jogo Solto

90 \- NF Fatura Conjugada M01/Bloco

91 \- NF Fatura Conjugada M01/ Jogo Solto

92 \- NF Fatura Conjugada M01/ Formulario Continuo

93 \- NF Conjugada M07/Bloco

94 \- NF Conjugada M07/Formulario Continuo

95 \- NF Conjugada M07/Jogo Solto

RJ \- Recibo em geral de Pessoa Juridica

RN \- Recibo em geral de Pessoa Natural

Preencher com espaço em branco, quando o campo série da parametrização da tela Municipal – Parâmetros por Município – Modelo Msaf x Série referente ao modelo cadastrado na nota estiver gravado com a opção: R \- 	RPA \- Recibo de Profissional Autonomo \(Pessoa Natural\)\.

Preencher com “R”, quando o campo série da parametrização da tela Municipal – Parâmetros por Município – Modelo Msaf x Série referente ao modelo cadastrado na nota estiver gravado com as opções: OT \- Outros Documentos \(Pessoa Jurídica\) e OM \- Nota Fiscal de outro município\.

Preencher com “G”, quando o campo série da parametrização da tela Municipal – Parâmetros por Município – Modelo Msaf x Série referente ao modelo cadastrado na nota estiver gravado com a opção: G	 \- Dispensado da Emissão de NF de Serviço\.

__CH7230\_2016__

__MFS\-100560__

__RN54__

__Registro R – Motivo da Retenção/Não retenção: __

Preencher com “T” se:

\- O código do serviço da Lei Complementar 116/03 associado ao código informado na nota fiscal estiver parametrizado na tela de Classificação de Serviços – ST __OU__

\- Quando pelo menos uma das opções abaixo seja verdadeira:

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se

o local da prestação do serviço = município do módulo selecionado __OU __

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado __OU__

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

__Obs\.: Regra ajustada no documento DE\-PARA – Municipal\.xls \(R1\-RN0001\)__

Caso nenhuma das opões seja verdadeira, preencher com:

__Pago pelo prestador/Não Incidente  __

C, quando o campo  IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL = ‘2’ \(campo 141 da SAFX07\)

__Valor de serviços menor que o mínimo \(Somente para o município de Teresina\)__

V, se campo CIDADE da tabela X04\_PESSOA\_FIS\_JUR = “11001” e UF = “PI” e campo valor do serviço lançado na nota fiscal recebida for <= 100,00

__Profissional autônomo inscrito__

G, quando o campo COD\_CBO da tabela X04\_PESSOA\_FIS\_JUR estiver preenchido para a pessoa fis/jur cadastrada na nota\.

__Sociedade de profissional__

F, verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “06”\.

__\[ALTERADA – CH17654\-A\_2014\]__

__Não incidência no município__

__\[EXCLUIDO\]__

A, verificar se o serviço e o município do prestador cadastrados na nota está parametrizado na tela Parâmetros por Município – Classificação de Serviços – Município com o COD\_PARAM = “432” e o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR não estiver preenchido\.

Se o serviço e o município do prestador cadastrados na nota está parametrizado na tela Parâmetros por Município – Classificação de Serviços – Município com o COD\_PARAM = “432” e o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR não estiver preenchido\.

__OBS: Para verificar o municipio e uf correspondente a DWT\_DOCTO\_FISCAL corretamente:__

1\-Localizar COD\_MUNIC\_ISS da tabela SAFX2097 referente ao COD\_MUNICIPIO da DWT\_DOCTO\_FISCAL 

2\-Localizar COD\_MUNIC\_MSAF da SAFX2097 correspondente 

Se o COD\_MUNIC\_MSAF for diferente do município em questão e UF for diferente da UF em questão\.

__Não Tributável__

B, verificar se o serviço e o município do prestador cadastrados na nota está parametrizado na tela Parâmetros por Município – Classificação de Serviços – Município com o COD\_PARAM = “444” e o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR não estiver preenchido\.__ \[EXCLUÍDO\]__

__Imune__

D, verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07”, se não estiver preenchido verificar se o serviço e o município do prestador cadastrados na nota está parametrizado na tela Parâmetros por Município – Classificação de Serviços – Município com o COD\_PARAM = “420”\.

__Isento__

E, verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”, se não estiver preenchido verificar se o serviço e o município do prestador cadastrados na nota está parametrizado na tela Parâmetros por Município – Classificação de Serviços – Município com o COD\_PARAM = “433”\.

__Estimativa__

H, verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “08”, se não estiver preenchido verificar se o serviço e o município do prestador cadastrados na nota está parametrizado na tela Parâmetros – por Município – Classificação de Serviços – Município com o COD\_PARAM = “421”\.

__Deposito em Juízo__

I, verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “09”, se não estiver preenchido verificar se o serviço e o município do prestador cadastrados na nota está parametrizado na tela Parâmetros – por Município – Classificação de Serviços – Município com o COD\_PARAM = “427”\.

__Medida Liminar/Cautelar__

J, verificar se o serviço e o município do prestador cadastrados na nota está parametrizado na tela Parâmetros – por Município – Classificação de Serviços – Município com o COD\_PARAM = “449” e e o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR não estiver preenchido\.

__OS3470\-E__

__OS3470\-I1A__

__CH10801__

__CH21624\-A__

__17654\-A\_2014__

__MFS\-895669__

__MFS\-912835__

__MFS\-926968__

__RN54\.a__

__Registro R – Motivo de Retenção \(Campo Grande\-MS\)__

__Se__ DWT\_DOCTO\_FISCAL\-__MOVTO\_E\_S__ = ‘1’ __e__ \(DWT\_DOCTO\_FISCAL\-__COD\_CLASS\_DOC\_FIS__ = ‘2’ ou ‘3’\) __e__ DWT\_DOCTO\_FISCAL\-__SITUACAO__ <> ‘S’ __e __DWT\_DOCTO\_FISCAL\-__IND\_TP\_RET __= 1 __e __

\(\(DWT\_ITENS\_SERV\-__VLR\_BASE\_ISS __> 0,00 __e__ DWT\_ITENS\_SERV\-__ VLR\_ISS__ > 0,00\) __ou __\(DWT\_ITENS\_SERV\-__VLR\_BASE\_ISS\_RETIDO __>__ __0,00 __e __DWT\_ITENS\_SERV\-__ VLR\_ISS\_RETIDO__ > 0,00\)\) __e __

\(DWT\_ITENS\_SERV\-__ALIQ\_TRIBUTO\_ISS__ > 0 __ou __DWT\_ITENS\_SERV\-__VLR\_ALIQ\_ISS\_RETIDO__ > 0\) __e__ DWT\_DOCTO\_FISCAL\-__COD\_MUNICIPIO__ = Município do módulo selecionado __então__

    Informar o motivo __T__, que significa, “Tributável no município”

__\[MFS682807\] Alteração do Layout \- Campo não será preenchido\.__

- No campo: Motivo da Retenção = Deixar Vazio\.

__MFS\-643430__

__MFS\-682807__

__RN54\.b__

__Registro R – Motivo da Não Retenção \(Campinas\): __

Preencher com brancos, quando pelo menos uma das opções forem verdadeiras:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado __OU __
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado __OU__
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

Caso nenhuma das opões seja verdadeira, preencher com:

A, verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “03”, se não estiver preenchido verificar se o serviço cadastrado na nota está parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “427”\.

B, essa OS não tratará essa opção\.

C, verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “01”, se não estiver preenchido verificar se o serviço cadastrado na nota está parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420”\.

D, verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “04”, se não estiver preenchido verificar se o serviço cadastrado na nota está parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\.

E, verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “08”\.

R, essa OS não tratará essa opção\.

__Obs\.: Regra ajustada no documento DE\-PARA – Municipal\.xls \(R1\-RN0001\)__

__OS3470\-E__

__OS3470\-I1A__

__RN54\.c__

__Registro R – Motivo da Não Retenção \(Campo Grande\-MS\): __

__Tratamento específico para não incidência da retenção do ISS, no município de Campo Grande \- MS__

Se DWT\_DOCTO\_FISCAL\-MOVTO\_E\_S = ‘1’ e \(DWT\_DOCTO\_FISCAL\-COD\_CLASS\_DOC\_FIS = ‘2’ ou ‘3’\) e DWT\_DOCTO\_FISCAL\-SITUACAO <> ‘S’ e DWT\_ITENS\_SERV\- VLR\_ISS = 0,00 e DWT\_ITENS\_SERV\- VLR\_ISS\_RETIDO = 0,00 e DWT\_DOCTO\_FISCAL\-COD\_MUNICIPIO <> Município do módulo selecionado Então

      Se PRT\_SERVICO\_MUNIC\_MSAF\-COD\_MUNICIPIO = Município do módulo selecionado e PRT\_SERVICO\_MUNIC\_MSAF\-COD\_PARAM = 432 e 

      PRT\_SERVICO\_MUNIC\_MSAF\-COD\_SERVICO = COD\_SERVICO, utilizado na tabela DWT\_ITENS\_SERV Então

           Informar o motivo A, que significa, “Não incidência no município”

Se DWT\_DOCTO\_FISCAL\-MOVTO\_E\_S = ‘1’ e \(DWT\_DOCTO\_FISCAL\-COD\_CLASS\_DOC\_FIS = ‘2’ ou ‘3’\) e DWT\_DOCTO\_FISCAL\-SITUACAO <> ‘S’ e DWT\_DOCTO\_FISCAL\-IND\_TP\_RET = 2 DWT\_ITENS\_SERV\- VLR\_ISS = 0,00 e DWT\_ITENS\_SERV\- VLR\_ISS\_RETIDO = 0,00 Então

      Informar o motivo C, que significa, “Pago pelo prestador/Não incidente”

__CH964\_2014__

__MFS\-643430__

__MFS\-659278__

__RN55__

__Registro R – Numero de identificação da Nota Fiscal: __

Se o campo “Série da Nota Fiscal” = “F”, preencher com o campo NUM\_MÁQUINA da tabela DWT\_DOCTO\_FISCAL \(campo 65 da SAFX07\) concatenado com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. \(campo 08 da SAFX07\)\. No formato mmmcccccc, onde mmm é o número da máquina e cccccc é o número do documento fiscal\.

Caso contrário, preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. \(campo 08 da SAFX07\)\.

\[__CH14867\-A/2014__\]

Na geração deste campo, quando for atendida a situação de concatenação do NUM\_MAQUINA \+ NUM\_DOCFIS deve ser considerado as 3 primeiras posições do campo NUM\_MAQUINA \(pois este é um campo numérico\) e as 6 últimas posições do campo NUM\_DOCFIS \(tipo varchar\)\.

Se for gerado apenas o NUM\_DOCFIS, deve ser consideradas 9 posições da direita para a esquerda do número da NF, considerando que os caracteres que serão suprimidos à esquerda \(da posição 10 a 12\) devem ser zeros\. Se o conteúdo do campo NUM\_DOCFIS tiver mais de 9 posições significativas \(sem zeros à esquerda\), gerar o número truncado, mas retornar no log a seguinte mensagem: “O campo Número do Documento \(NUM\_DOCFIS\) ultrapassou o tamanho máximo permitido \(9 posições\)\.”

\(Ex para esta situação: Nº de NF 12345678900 será gerado 345678900\)\.

__OS3470\-E__

__CH14867\-A/2014__

__RN56__

__Registro R – Valor bruto da nota fiscal: __

__\[ALTERADA \- CH15640\-B\_2013\] __

Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV\. 

Alterado CH5563

Se o campo COD\_CLASS\_DOC\_FIS da tabela DWT\_DOCTO\_FISCAL = ‘3’

Preencher com o campo VLR\_TOT\_NOTA da tabela DWT\_DOCTO\_FISCAL

__\[EXCLUIDA \- CH15640\-B\_2013\] __

__OS3470\-E__

__CH15640\-B\_2013__

__RN57__

__Registro R – Valor do serviço lançado na nota fiscal recebida: __

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\. \(campo 14 da SAFX09\)

__OS3470\-E__

__RN58__

__Registro R – Alíquota de ISS: __

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. \(campo 32 da SAFX09\), quando pelo menos uma das opções abaixo seja verdadeira:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado __OU __
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado __OU__
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

Caso nenhumas das opções acima sejam verdadeiras, preencher com zeros\.

__Obs\.: Regra ajustada no documento DE\-PARA – Municipal\.xls \(Referência ISS Digital verificar R1\-RN0001 do Detalhamento\)__

__OS3470\-E__

__RN59__

__Registro R – Numero da parcela de pagamento da NF: __

Preencher com zeros\.

__OS3470\-E__

__RN60__

__Registro R – Quantidade de parcelas de pagamento da NF: __

Preencher com zeros\.

__OS3470\-E__

__RN61__

__Registro R – Descrição do motivo da não retenção: __

Preencher com brancos\.

__OS3470\-E__

__RN62__

__Registro R – CNPJ do prestador do serviço: __

Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR quando o tamanho do campo for igual a 14\. \(campo 06 da SAFX04\)

Se o campo tiver 11 posições ou o tomador for estrangeiro, preencher com zeros\.

__OS3470\-E__

__RN63__

__Registro R – CPF do prestador do serviço:__ 

Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR quando o tamanho do campo for igual a 11\. \(campo 06 da SAFX04\)

Se o campo tiver 14 posições ou o tomador for estrangeiro, preencher com zeros\.

__OS3470\-E__

__RN64__

__Registro R – Nome do prestador do serviço: __

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR\. \(campo 05 da SAFX04\)

__OS3470\-E__

__RN65__

__Registro R – Código SIAFI do município do prestador do serviço: __

Preencher com o campo COD\_MUNIC\_SIAFI da tabela PRT\_MUNIC\_SIAFI referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\. \(campo 25 da safx04\)\. O campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR deve ser igual ao campo COD\_MUNIC\_MSAF da tabela PRT\_MUNIC\_SIAFI\. 

Se prestador for estrangeiro usar “9999” e não informar CPF ou CNPJ\.

__*Para o município de São Luis, considerar também a validação abaixo:*__

Deve ser inserido zeros a esquerda ao código do município, até atingir o tamanho máximo do campo \(10 posições\)

__\[ALTERAÇÃO\-MFS\-895669\] – Desconsiderar este campo na geração do arquivo para o município de Nova Iguaçu/RJ\.__

__OS3470\-E__

__MFS31470__

__MFS\-895669__

__RN66__

__Registro R – Enquadramento no Simples Nacional do prestador: __

Preencher com o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR\. \(campo 43 da SAFX04\)

__OS3470\-E__

__RN66\.a__

__Registro R – Enquadramento no Simples Nacional do prestador – Específico para Uberlândia: __

Preencher com o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR\. \(campo 43 da SAFX04\)\.

Se o campo IND\_SIMPLES\_NAC não estiver prenchido

      Preencher com “N”\.

__MFS917355__

__RN67__

__Registro R – Inscrito no município prestador \(Campinas\): __

Esse campo apenas deve ser utilizado para o município de Campinas e deve ser preenchido com brancos\. Para os demais municípios esse campo não deve existir no registro\.

__\[ALTERAÇÃO\-MFS\-895669\] – Desconsiderar este campo na geração do arquivo para o município de Nova Iguaçu/RJ\.__

__OS3470\-E__

__MFS\-895669__

__RN68__

__Registro R – Código do serviço prestado:__

Preencher com o campo Serviço da tela Municipal – Parametros por Município – Parâmetros – Serviços Msaf x Serviços referente ao serviço cadastrado na nota fiscal\.

__\[ALTERADO CH32888\-B\_2012\]__

O campo deverá ser gerado sem o separador \(ponto\) e alinhado à esquerda com os demais campos preenchidos com espaço\.

Preencher apenas se o prestador do serviço for de fora do município em questão, senão preencher com brancos\.

Preencher com brancos à direita até completar o tamanho do campo\.

__OS3470\-E__

__/__

__CH32888__

__/__

__CH32888\-A__

__/__

__CH32888\-B__

__MFS\-895669__

__MFS\-912835__

__MFS\-926968__

__RN68\.a__

__Registro R – Código do serviço prestado:__

__Para o município de Campinas:__

Preencher com o campo Serviço da tela Municipal – Parametros por Município – Parâmetros – Serviços Msaf x Serviços referente ao serviço cadastrado na nota fiscal\.

O campo deverá ser gerado sem o separador \(ponto\) e alinhado à esquerda com os demais campos preenchidos com espaço\.

Preencher o campo para prestadores de fora E do mesmo município em questão\.

Preencher com brancos à direita até completar o tamanho do campo\.

__CH25417\_2016__

__RN69__

__Registro R – Código SIAFI do município do local da prestação do serviço: __

Esse campo será preenchido com o campo COD\_MUNIC\_SIAFI da tabela PRT\_MUNIC\_SIAFI referente ao campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\. 

Caso o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL não esteja preenchido, esse campo será preenchido com o campo COD\_MUNIC\_SIAFI da tabela PRT\_MUNIC\_SIAFI referente ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\. 

*Obs: O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS\.*

__*Para o município de São Luis, considerar também a validação abaixo:*__

Deve ser inserido zeros a esquerda ao código do município, até atingir o tamanho máximo do campo \(10 posições\)

__\[ALTERAÇÃO\-MFS\-895669\] – Desconsiderar este campo na geração do arquivo para o município de Nova Iguaçu/RJ\.__

__OS3470\-E__

__/__

__OS3828__

__MFS31480__

__MFS\-895669__

__RN70__

__Registro R – Operação da nota fiscal recebida \(Demais Municípios\): __

Preencher com:

D, quando o campo NORM\_DEV da tabela DWT\_DOCTO\_FISCAL = ‘2’ \(campo 04 da SAFX07\)

G, quando o campo IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota\.

I, quando campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = ‘06’

C, verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07” ou “10”, se não estiver preenchido verificar se o serviço e o município da pessoa fis/jur cadastrados na nota está parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420” ou “433”\.

H, verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “08”, se não estiver preenchido verificar se o serviço e o município da pessoa fis/jur cadastrados na nota está parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “421”\.

B, quando o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV > 0\. 

A, quando o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV = 0 ou quando não estiver preenchido\. \(campo 190 da SAFX07\)

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher com brancos\.

__OS3470\-E__

__MFS\-895669__

__MFS\-912835__

__MFS\-926968__

__RN70\.a__

__Registro R – Operação da nota fiscal recebida \(Sorocaba\): __

Preencher com:

D, quando o campo NORM\_DEV da tabela DWT\_DOCTO\_FISCAL = ‘2’ \(campo 04 da SAFX07\)

G, quando o campo IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota\.

I, quando campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = ‘06’

B, quando o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV > 0\.

A, quando o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV = 0 ou quando não estiver preenchido\. \(campo 190 da SAFX07\)

J, não será tratado nessa OS\.

__OS3828__

__RN70\.b__

__Registro R – Operação da nota fiscal recebida \(CAMPO GRANDE\): __

Preencher com:

A, quando o campo VLR\_DEDUCAO\_ISS da tabela DWT\_DOCTO\_FISCAL = 0 ou quando não estiver preenchido\.

B, quando o campo VLR\_DEDUCAO\_ISS da tabela DWT\_DOCTO\_FISCAL > 0\.

C, verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07” ou “10”, se não estiver preenchido verificar se o serviço e o município da pessoa fis/jur cadastrados na nota está parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420” ou “433”\.

D, quando o campo NORM\_DEV da tabela DWT\_DOCTO\_FISCAL = ‘2’

J, esse chamado não tratará essa opção\.

CH10297\_2014

__RN70\.c__

__Registro R – CPF/CNPJ do Cliente \(CAMPO GRANDE\):__

Preencher com o campo CGC da tabela ESTABELECIMENTO\.

CH30394\_2013

__RN70\.d__

__Registro R – Operação da nota fiscal recebida \(CAMPINAS\): __

Preencher com:

D, quando o campo NORM\_DEV da tabela DWT\_DOCTO\_FISCAL = ‘2’ \(campo 04 da SAFX07\);

G, quando o campo IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota;

I, quando campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = ‘06’;

B, quando o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV > 0\. __Ou__ se o COD\_MUNICIPIO do  prestador for diferente do campo de COD\_MUNICIPIO do Estabelecimento;

A, quando o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV = 0 ou quando não estiver preenchido\. \(campo 190 da SAFX07\)\.

MFS82097

__RN71__

__Registro R – Matricula cei / Processo administrativo \(Sorocaba\): __

Preencher com zeros\.

__\[ALTERAÇÃO\-MFS\-895669\] – Desconsiderar este campo na geração do arquivo para o município de Nova Iguaçu/RJ\.__

CH24395/2015

__MFS\-895669__

__RN72__

__Registro R – Cliente \(Sorocaba/ Uberlândia/ Belém/ Teresina\): __

__\[ALTERADO CH28829\_2015/ CH9821\_2016/ CH7320\_2016\]__

Deverá preencher com zeros, respeitando o tamanho do campo de __14 posições\.__

__\[ALTERAÇÃO\-MFS\-895669\] – Desconsiderar este campo na geração do arquivo para o município de Nova Iguaçu/RJ\.__

__OS3828__

__CH28829\_2015__

__CH9821\_2016__

CH7320\_2016

__MFS\-895669__

__RN73__

__Regra p/ inclusão do novo módulo no Manager – Nova Iguaçu:__

O novo módulo “Nova Iguaçu” deve ficar localizado no grupo “Municipal” 

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados do município de Nova Iguaçu”\.

OS3470\-E

__RN74__

__Regra p/ abertura do novo módulo no Manager – Nova Iguaçu:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “RJ” e ao código de município do IBGE igual a “3500” \(Nova Iguaçu\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Nova Iguaçu, Rio de Janeiro\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS3470\-E__

__RN75__

__Regra p/ abertura do novo módulo no Manager – Campinas:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “9502” \(Campinas\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Campinas, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__\[MFS\-562118\]__ __Regra Campinas; __“Consiste na entrega das informações sobre os serviços tomados e deduções do município de “Campinas”\.

__MFS\-562118__

__RN76__

__Regra p/ abertura do novo módulo no Manager – Nova Iguaçu:__

Modulo de Nova Iguaçu já existente\.

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “RJ” e ao código de município do IBGE igual a “3500” \(Nova Iguaçu\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Nova Iguaçu, Rio de Janeiro\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-895669__

__RN77__

__Regra p/ abertura do novo módulo no Manager – Triunfo:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “__RS__” e ao código de município do IBGE igual a “22004” \(Triunfo\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Triunfo, Rio Grande do Sul\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-912835__

__RN78__

__Regra p/ abertura do novo módulo no Manager – Montes Carlos:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “__MG__” e ao código de município do IBGE igual a “43302” \(Montes Claros\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Montes Claros, Minas Gerais\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-926968__

Considerações deste modelo:

__Quando uma Regra de Negócio for alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

