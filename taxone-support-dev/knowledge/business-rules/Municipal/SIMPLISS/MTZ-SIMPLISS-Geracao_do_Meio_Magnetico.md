# MTZ-SIMPLISS-Geracao_do_Meio_Magnetico

- **Fonte:** MTZ-SIMPLISS-Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2026-03-20
- **Tamanho:** 103 KB

---

# SIMPLISS \- Geração do Meio Magnético

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3470\-D

Geração do Meio Magnético SIMPLISS 

 

Este documento tem como objetivo criar a geração para os municípios que são atendidos pelo SIMPLISS\. Dessa usaremos o módulo de Parâmetros por Município que servirá para o usuário realizar a parametrização de todos os municípios atendidos pelo SIMPLISS em um único lugar\. Além disso, também realizaremos a geração dos municípios através de uma única geração, ou seja, quando o cliente clicar em um município da SIMPLISS será exibido a mesma tela de geração do Meio Magnético\. 

Com essa OS também estaremos criando as obrigações para os municípios de Maracaí, Mineiros do Tietê, Dois Córregos e São João da Boa Vista\. Usaremos o módulo SIMPLISS Piracicaba para transformá\-lo em SIMPLISS e dessa forma atender ao município de Piracicaba\.

CH788\_2012

DW \- MUNICIPAL \- PIRACICABA \- Ajuste na recuperação do campo 5 ES\-MUNICIPIO para gerar com 7 caracteres

O objetivo desta demanda é alterar o campo es\_município do cabeçalho dos registros de serviços prestados para que o mesmo possa gravar o código do município do IBGE completo\.

CH14640\_2012

DW \- MUNICIPAL \- PIRACICABA \- Geração do campo COD\_SERV\_LEI\_116 incorreta\.

O objetivo deste documento é ajustar a geração do campo es\_item\_lista\_servico para que informe no arquivo os códigos de serviço no formato correto\.

CH4712\_2013

DW \- MUNICIPAL \- SIMPLISS \- TEODORO SAMPAIO \- Erro na geração do campo pre\_endereco\_es\_municipio

O objetivo desse chamado é permitir que os campos referentes ao código do município sejam preenchidos de acordo com a tabela do IBGE\. \(Código da UF \+ Código do Município\)

OS3490

DW \- MUNICIPAL \- SIMPLISS \- TEODORO SAMPAIO \- Alteração do códigos ISS para atenser o campo cd\_regime\_especial\_tributacao Código de identificação

Este documento tem como objetivo alterar a geração do campo cd\_regime\_especial\_tributacao dos registros de serviços tomados e prestados\.

CH6343\_2013

DW Municipal \- Piracicaba \- geração de notas fiscais eletrônicas de prestadores estabelecidos no municipio\.

Este documento tem como objetivo ajustar a recuperação das notas de serviços tomados \(contratados\)\.

CH17331\_2013

DW \- MUNICIPAL \- SIMPLISS –  Alteração para Geração de estabelecimento fora do município\.

Este documento tem como objetivo, ajustar a regra do campo Tomador de Serviços, para que seja possível efetuar a geração, utilizando Inscrição Estadual de estabelecimento fora do município\.

CH473\_2014

DW \- MUNICIPAL \- PIRACICABA – Ajuste da geração do campo es\_item\_lista\_servico do prestador de serviços

Este documento tem como objetivo ajustar a regra de geração do campo Código de Especificação da Atividade \(es\_item\_lista\_servico\) do prestador de serviços\.

CH7586\_2014

DW – MUNICIPAL – SIMPLISS – Ajuste da geração do campo cd\_regime\_especial\_tributacao do tomador de serviços

<a id="OLE_LINK44"></a><a id="OLE_LINK45"></a><a id="OLE_LINK46"></a>O objetivo deste documento é ajustar a geração do campo cd\_regime\_especial\_tributacao do Registro de Serviços Tomados da obrigação municipal SIMPLISS\.

__OS3341\-A1__

Geração do Meio Magnético para nota fiscais com número de documento com mais de 12 posições\.  

Ajuste para considerar o novo campo NUM\_DOCFIS\_SERV

__CH24658\_2014__

DW – MUNICIPAL – SIMPLISS – Ajuste da geração do campo Tomador de Serviços – Corpo – Optante pelo Simples Nacional

Este documento tem como objetivo ajustar a geração do campo Tomador de Serviços – Corpo – Optante pelo Simples Nacional\.

__OS4682__

DW – MUNICIPAL – SIMPLISS – Ajuste da geração do campo Tomador de Serviços – Corpo – Código da Natureza de Operação

Este documento tem como objetivo ajustar a geração do campo Tomador de Serviços – Corpo – Código da Natureza de Operação\.

__OS4840__

Inclusão do município Balneário Camboriú

Este documento tem como objetivo incluir o município Balneário Camboriú\.

__MFS2431__

DW – MUNICIPAL – SIMPLISS – Novo Parâmetro Quebra do Arquivo por Data de Emissão

Este documento tem como objetivo disponibilizar o novo parâmetro “Quebrar Arquivo por Data de Emissão” na tela de geração dos registros dos municípios atendidos pelo validador SIMPLISS, possibilitando gerar o arquivo magnético separado do mês de referência da apuração, quando houver notas fiscais de entrada anterior à data a ser apurada\.

__MFS\_2071__

DW \- MUNICIPAL \- SIMPLISS – Retirada do range da data inicial e final\.

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

__MFS\_5370__

DW \- MUNICIPAL \- IRACEMÁPOLIS

Este documento tem como objetivo incluir o município de Iracemápolis no validador SIMPLISS e incluir o campo “Indicador de Incidência do ISS”\.

__MFS\_5905__

DW \- MUNICIPAL \- CARAPICUIBA

Este documento tem como objetivo incluir o município de Carapicuiba no validador SIMPLISS\.

__MFS8131__

DW – MUNICIPAL \- TUPÃ

Este documento tem como objetivo incluir o município de Tupã no validador SIMPLISS\.

__MFS17871__

DW – MUNICIPAL – JOÃO MONLEVADE

Este documento tem como objetivo incluir o município de João Monlevade no validador SIMPLISS\.

__MFS\-21322__

DW – MUNICIPAL – VOLTA REDONDA/ PIRACICABA

Este documento tem como objetivo incluir o município de Volta Redonda no validador SIMPLISS e alterar o layout do município de Piracicaba\.

__MFS\-21322__

DW – MUNICIPAL – Espírito Santo do Pinhal / Casa Branca

Este documento tem como objetivo incluir os municípios de Espírito Santo do Pinhal e Casa Branca no validador SIMPLISS\.

__MFS31274__

DW – MUNICIPAL – Blumenau

Este documento tem como objetivo incluir o município de Blumenau no validador SIMPLISS\.

__MFS44374__

DW – MUNICIPAL – São Gonçalo

Este documento tem como objetivo incluir o município de São Gonçalo no validador SIMPLISS\.

__MFS75180__

Andréa Rocha

Inclusão do preenchimento do campo “Indicador de Incidência do ISS” para o município de Presidente Prudente\.

__MFS\-552778__

Alessandra Cristina Navatta

Este documento tem como objetivo incluir o município de Arceburgo no validador SIMPLISS\.

Alteração na escrita da RN57\.a e RN96\.a, visando melhorar a compreensão das regras\.

A opção “Gerar RPS” não será processada para o município de Arceburgo\. \(RN18\)

__MFS\- 565912__

Rosemeire Santos

Este documento tem como objetivo ajustar as regras \(RN80\) Base de cálculo ISS e \(RN81\) Alíquota de ISS para o município de Arceburgo no validador SIMPLISS\.

__MFS__[__776824__](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/776824)

Rogério Ohashi

Este documento tem como objetivo incluir regra no campo Código de Natureza de Operação específico para o município de Piracicaba, para verificar o município de PFJ <> município do estab\.

__MFS\-810921__

Bruna Ribeiro

Este documento tem como objetivo incluir regra no campo Código de Natureza de Operação específico para o município de Piracicaba\. Verificando os campos: código do município e o local do recolhimento do imposto\.

__MFS837010__

Bruna Ribeiro

Este documento tem como objetivo incluir regra no campo Código de Natureza de Operação específico para o município de Piracicaba\. 

__MFS\-839680__

Rosemeire Santos

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

__MFS\-978069__

Rosemeire Santos

Este documento tem como objetivo incluir o município de Presidente Prudente e Blumenau, na regra __RN68\.b__ específica para o campo Código de Natureza de Operação, para a geração da Construção Civil\. 

__MFS\-1015365__

Alessandra Navatta

Movido o trecho da regra RN68\.b \(da geração de Construção Civil\) para o documento MTZ\_SIMPLISS\_Geracao\_Meio\_Magnetico\_Situacao\_Especial\.docx

__MFS\-1019978__

Rosemeire Santos

Este documento tem como objetivo ajustar a regra __RN68__ para o campo Código de Natureza de Operação, para a geração da Construção Civil\.

__MFS\-1012082__

Rosemeire Santos

Este documento tem como objetivo ajustar a regra __RN96\.a__, campo Indicador de incidência do ISS, para o Municípios de Presidente Prudente, para geração Construção Civil, Eventual, Telecom e Utilities\.

__MFS\-1048310__

Rosemeire Santos

Este documento tem como objetivo incluir os municípios de Itobi\-SP, Paraguacu Paulista\-SP, Pirapora Do Bom Jesus\-SP, Santa Cruz Do Rio Pardo\-SP, Santo Antonio Do Jardim\-SP, Taciba\-SP e Taruma\-SP, no validador SIMPLISS\.

__MFS\-1047132__

Rosemeire Santos

Este documento tem como objetivos, ajustar a regra __RN76__, para correto preenchimento do campo __Retenção na fonte__, para todos os municípios\.

##   

## REGRAS DE NEGÓCIO  

#### \.

### Descrição

### DR

__RN01__

__Regra p/ inclusão do novo módulo no Manager – Dois Córregos:__

O novo módulo “Dois Córregos” deve ficar localizado no grupo “Municipal” 

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de Dois Córregos”\.

OS3470\-D

__RN02__

__Regra p/ abertura do novo módulo no Manager – Dois Córregos:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “14106” \(Dois Córregos\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Dois Córregos, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS3470\-D__

__RN03__

__Regra p/ inclusão do novo módulo no Manager – Maracaí:__

O novo módulo “Maracaí” deve ficar localizado no grupo “Municipal” 

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de Maracaí”\.

__OS3470\-D__

__RN04__

__Regra p/ abertura do novo módulo no Manager – Maracaí:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “28809” \(Maracaí\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Maracaí, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS3470\-D__

__RN05__

__Regra p/ inclusão do novo módulo no Manager – Mineiros do Tietê:__

O novo módulo “Mineiros do Tietê” deve ficar localizado no grupo “Municipal” 

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de Mineiros do Tietê”\.

__OS3470\-D__

__RN06__

__Regra p/ abertura do novo módulo no Manager – Mineiros do Tietê:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “29807” \(Mineiros do Tietê\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Mineiros do Tietê, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS3470\-D__

__RN07__

__Regra p/ inclusão do novo módulo no Manager – São João da Boa Vista:__

O novo módulo “São João da Boa Vista” deve ficar localizado no grupo “Municipal” 

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de São João da Boa Vista”\.

__OS3470\-D__

__RN08__

__Regra p/ abertura do novo módulo no Manager – São João da Boa Vista:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “49102” \(São João da Boa Vista\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de São João da Boa Vista, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS3470\-D__

__RN09__

__Regra p/ inclusão do novo módulo no Manager – Piracicaba:__

O novo módulo “Piracicaba” deve ficar localizado no grupo “Municipal” 

__OS3470\-D__

__RN10__

__Estrutura de menus do módulo SIMPLISS Piracicaba:__

Deverão ser criados os seguintes menus e sub\-menus no módulo SIMPLISS:

- Arquivo
- Obrigações
	- Meio Magnético
	- Arquivo de Entradas de Serviços \(Const\. Civil/Utilities /Telecom\)
- Janela
- Ajuda 

__OS3470\-D__

__RN11__

__Regra p/ campo Parâmetro da tela Parâmetros por Município – Parâmetros – Classificação de Serviços:__

Deve exibir as seguintes opções:

- Serviços Isentos – cod\_param = 433
- Servicos Imunes de ISS perante o Fisco – cod\_param = 420
- Serviços sujeitos a procedimento administrativo – cod\_param = 485
- ISSQN Regime Tributação Fixa – cod\_param = 487
- Servicos Sujeitos a Regime de Estimativa – cod\_param = 421
- Servicos Tributáveis – cod\_param = 445
- Servicos sujeitos a Deposito/Decisao Judicial – cod\_param = 427

__OS3470\-D__

__RN12__

__Regra de criação do nome do arquivo__

__\[ALTERADA – MFS2431\]__

__Arquivos em Geral:__

__CNPJ do contribuinte \+ anoatual \+ mesatual \+ diaatual \+ horaatual \+ minutoatual \+ segundoatual\.txt__, onde:

Ex: 0000000000000020110401102040\.txt

__Serviços Tomados__

- Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver desmarcado será gerado apenas um arquivo com a nomenclatura do arquivo normal indicado abaixo\.

__CNPJ do contribuinte \+ anoatual \+ mesatual \+ diaatual \+ horaatual \+ minutoatual \+ segundoatual\.txt__, onde:

Ex: 0000000000000020110401102040\.txt

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_MMAAAA\.TXT__, onde:

      \.__TXT__: extensão do arquivo\.

       __MMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       ST__: representa o arquivo é de serviço tomado\.

Ex: SP\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\.TXT

- Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado deve ser realizada a seguinte verificação:

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter todas as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser:

__CNPJ do contribuinte \+ anoatual \+ mesatual \+ diaatual \+ horaatual \+ minutoatual \+ segundoatual \+ \_MMAAAA\.txt__, onde:

Ex: 0000000000000020110401102040__\_032011__\.txt

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_MMAAAA\_MMAAAA\.TXT__, onde:

__       \.TXT__: extensão do arquivo\.

       __MMAAAA__: representa a data inicial da geração\.   

__       MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       ST__: representa o arquivo é de serviço tomado\.

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\_012010\.TXT

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__OBS\.: Este novo parâmetro \(Quebrar Arquivo por Data de Emissão\) será válido, apenas para Notas de Serviços Tomados__

__OS3470\-D__

__MFS2431__

__MFS\-839680__

__RN13__

__Regra p/ tela da Geração do Meio Magnético__

__\[ALTERADA – MFS2431\]__

A tela de geração do meio magnético deve exibir os seguintes campos:

Data Inicial: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

Data Final: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

Gerar Serviços Prestados: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Gerar Serviços Contratados: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Gerar RPS: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Quebrar Arquivo por Data de Emissão: Deverá ser exibido através de um checkbox\. Deve ser exibido e desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)\.

Número do Lote: deve ser exibido através de um textbox\. Deve permitir a digitação do número do lote a ser gerado\.

Estabelecimento: o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__OS3470\-D__

__MFS2431__

__MFS\_2071__

__RN14__

__Regras referentes à formatação dos registros gerados no meio magnético:__

- Os campos deverão ser separados pelo caracter  “| “;
- O separador decimal será o caracter “\.”;
- Os campos do tipo  texto não precisam ser completados por caracteres de espaço;
- Os campos dos tipos inteiro ou decimal não precisam ser completados com zero;
- Campos do tipo Data \(date\): Formato: AAAA\-MM\-DD

                                                           Onde: AAAA = Ano com 4 caracteres

                                                                      MM = Mês com 2 caracteres

                                                                      DD = Dia com 2 caracteres

- Campos de Valores Decimais \(decimal\): Formato: 0\.00

Não deve ser utilizado separador de milhar\. O ponto \(\.\) deve ser utilizado para separar a parte inteira da fracionária\.

Exemplo:

48\.562,25 = 48562\.25

1,00 = 1\.00 ou 1

0,50 = 0\.50 ou 0\.5

- Valores Percentuais \(decimal\): Formato: 0\.0000

O formato em percentual presume o valor percentual em sua forma fracionária, contendo 5 dígitos\. O ponto \(\.\) separa a parte inteira da fracionária\.

Exemplo:

62% = 0\.62

150% = 1\.5

25,32% = 0\.2532

Obs: Quando um campo não estiver preenchido deve\-se apenas colocar o próximo “|” \(pipe\)\.

__OS3470\-D__

__RN15__

__Regras referentes à estrutura do meio magnético:__

1 – Cabeçalho

2 – Corpo do arquivo

Ex:

1|cnpj|inscrição\_municipal|tiponota|es\_município

2|serie|numero|\.\.\.

2|serie|numero|\.\.\.

Obs: Deve\-se gerar um arquivo para cada opção marcada na tela de geração\.

__OS3470\-D__

__RN16__

__Regra p/ Recuperar notas fiscais de serviços prestados__

Esse arquivo apenas deve ser gerado quando o campo “Gerar serviços prestados” estiver marcado e deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência

Quando a nota não tiver itens não deve ser recuperada\.

__OS3470\-D__

__RN17__

__Regra p/ Recuperar notas fiscais de serviços contratados__

Esse arquivo apenas deve ser gerado quando o campo “Gerar serviços contratados” estiver marcado e deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Não considerar notas eletrônicas conforme detalhamento abaixo:

As notas fiscais eletrônicas cujo prestador \(SAFX04\) é do município da obrigação \(Estabelecimento\), não devem ser geradas no arquivo\. 

Para identificar notas fiscais eletrônicas, existem duas formas:

1. Através do modelo 55
2. Através o campo NF\-e \(Nota Fiscal Eletrônica\) da tela de cadastro de tipos de documentos marcado

Dessa forma deve\-se primeiro identificar se a nota é uma nota fiscal eletrônica e depois verificar se o prestador é ou não do município da obrigação \(Estabelecimento\) e assim gerar ou não a nota no arquivo\. Conforme regra abaixo:

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

Quando a nota não tiver itens não deve ser recuperada\.

__OS3470\-D__

__CH6343\_2013__

__RN18__

__Regra p/ Recuperar notas fiscais de serviços prestados \- RPS__

Esse arquivo apenas deve ser gerado quando o campo “Gerar RPS” estiver marcado e deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\)
- Classificação do Documento fiscal = ‘9’
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Código do documento = ‘RPS’

Quando a nota não tiver itens não deve ser recuperada\.

__\[ALTERAÇÃO MFS\-552778\]__ Para o município de Arceburgo:

Não será processado arquivo separado, quando a opção “Gerar RPS”, na tela de geração do meio magnético, estiver marcada e o município for Arceburgo\. Considerando este cenário, exibir a mensagem no log: “A opção “Gerar RPS” não será processada para o município de Arceburgo”\.

__OS3470\-D__

__MFS\-552778__

__RN19__

__Regra p/ o campo Prestador de Serviços – Cabeçalho – Identificador __

Preencher com “1”\.

__OS3470\-D__

__RN20__

__Regra p/ o campo Prestador de Serviços – Cabeçalho – CPF/CNPJ do Prestador__

Preencher com o campo CGC da tabela ESTABELECIMENTO\.

__OS3470\-D__

__RN21__

__Regra p/ o campo Prestador de Serviços – Cabeçalho – Inscrição Municipal do Prestador__

Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO\.

__OS3470\-D__

__RN22__

__Regra p/ o campo Prestador de Serviços – Cabeçalho – Tipo da Nota__

Preencher com “P”\.

__OS3470\-D__

__RN23__

__Regra p/ o campo Prestador de Serviços – Cabeçalho – Código do município do prestador conforme a tabela do IBGE__

Preencher com o campo COD\_UF \+ COD\_MUNICIPIO \(preencher com 0 a esquerda até completar 5 posições\) da tabela MUNICIPIO referente ao município do estabelecimento que está sendo gerado\. \(COD\_MUNICIPIO da tabela ESTABELECIMENTO\)

__OS3470\-D__

__/__

__CH788\_2012__

__RN24__

__Regra p/ o campo Prestador de Serviços – Corpo – Identificador__

Preencher com “2”\.

__OS3470\-D__

__RN25__

__Regra p/ o campo Prestador de Serviços – Corpo – Número da Nota Fiscal__

__Tela\-A__ ç__  Modulo: __Básicos >> Parâmetros__ Menu:__ Preliminares >> __Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)__

Se o campo __COD\_ESTAB__ selecionado na geração for __=__ o campo __COD\_ESTAB__ da __Tela\-A__

  __E__

Campo __Data\_fiscal __for maior ou igual o campo __Data Inicio__ da __Tela\-A__ __ __  

  __E__

Campo __NUM\_DOCFIS\_SERV __da tabela __DWT\_DOCTO\_FISCAL__ estiver preenchido

__ __ 

Então, Preencher com o campo __NUM\_DOCFIS\_SERV__ da tabela __DWT\_DOCTO\_FISCAL__

Se não,

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__OS3470\-D__

__OS3341\-A1__

__RN26__

__Regra p/ o campo Prestador de Serviços – Corpo – Série da Nota Fiscal__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Campo obrigatório\.

__OS3470\-D__

__RN27__

__Regra p/ o campo Prestador de Serviços – Corpo – Tipo da Nota Fiscal__

Preencher com o campo Tipo Docto da tela Parâmetros por Município \- Tipo Docto\. Msaf x Tipo Docto referente ao tipo de documento cadastrado na capa da nota fiscal\.

__OS3470\-D__

__RN28__

__Regra p/ o campo Prestador de Serviços – Corpo – Data de Emissão da Nota Fiscal__

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

__OS3470\-D__

__RN29__

__Regra p/ o campo Prestador de Serviços – Corpo – Código da Natureza de Operação__

Preencher com:

1, Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “10”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “445”__ E__

campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL = ao município em questão*\.Se o campo *COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL não estiver preenchido, verificar o município cadastrado no estabelecimento\.

2, Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “10”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “445” __E__

campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL <> ao município em questão*\.Se o campo *COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL não estiver preenchido, verificar o município cadastrado na tabela X04\_PESSOA\_FIS\_JUR\.

 

3, Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “04”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\.

4, Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “01”, s se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420”\.

5, Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “03”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “427”\.

6, Verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “485”\.

__OS3470\-D__

__MFS\-1048310__

__RN29a__

__Regra p/ o campo Prestador de Serviços – Corpo – Código da Natureza de Operação\. Especifico para o Município de Piracicaba__

Preencher com:

1, Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “10”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “445”__ E__

campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL = ao município em questão*\.Se o campo *COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL não estiver preenchido, verificar o município cadastrado no estabelecimento\.

2, Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “10”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “445” __E__

campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL <> ao município em questão*\.Se o campo *COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL não estiver preenchido, verificar o município cadastrado na tabela X04\_PESSOA\_FIS\_JUR\. 

3, Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “04”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\.

4, Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “01”, s se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420”\.

5, Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “03”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “427”\.

6, Verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “485”\.

__RN30__

__Regra p/ o campo Prestador de Serviços – Corpo – Código de Identificação do Regime Especial de Tributação__

Preencher com:

4, quando o campo NAT\_PESSOA\_JUR da tabela ESTABELECIMENTO = ‘01’

1,quando o campo IND\_ISS do ESTABELECIMENTO = 11

3, Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “08”

2, verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “02”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “421”\.

9, Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “04”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\.

10, Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “01”, s se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420”\.

11, Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “03”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “427”\.

5, Verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão  parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “452”\.

6, não será tratado

7, Verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão  parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “589”\.

8, Verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão  parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “495”\.

12, Verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão  parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “485”

__OS3470\-D__

__/__

__OS3940__

__RN31__

__Regra p/ o campo Prestador de Serviços – Corpo – Optante pelo Simples Nacional__

Preencher com:

1, Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “07”\.

2, quando o campo acima for <> “07

__OS3470\-D__

__RN32__

__Regra p/ o campo Prestador de Serviços – Corpo – Status da Nota Fiscal__

Preencher com:

1, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> ‘S

2, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = ‘S’

__OS3470\-D__

RN33

__Regra p/ o campo Prestador de Serviços – Corpo – Informações Adicionais ao documento__

Preencher com brancos\.

__OS3470\-D__

RN34

__Regra p/ o campo Prestador de Serviços – Corpo – Código de Especificação da Atividade__

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao código de serviço cadastrado no item da nota fiscal\.

__\[ALTERADA – CH473\_2014\]__

Formato: com ponto “\.” e sem o primeiro zero “0” à esquerda\.

Exemplos: Para o código 1401, informar no arquivo 14\.01

                  Para o código 0701, informar no arquivo 7\.01

     Para o código 0026, informar no arquivo 0\.26

__OS3470\-D__

__CH473\_2014__

RN35

__Regra p/ o campo Prestador de Serviços – Corpo – Valor total do serviço__

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\.

__OS3470\-D__

RN36

__Regra p/ o campo Prestador de Serviços – Corpo – Valor da Dedução__

Preencher com o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV\.

__OS3470\-D__

__RN37__

__Regra p/ o campo Prestador de Serviços – Corpo – Retenção na fonte__

Para que esse campo seja preenchido com “1”, é necessário que pelo menos umas das seguintes opções seja verdadeira:

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se estiver preenchido, verificar se está preenchido com “1”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV não está preenchido\. 

Caso nenhuma das opões seja verdadeira, preencher com “2”\.

__OS3470\-D__

__RN38__

__Regra p/ o campo Prestador de Serviços – Corpo – Valor do ISS – Imposto __

Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

__OS3470\-D__

__RN39__

__Regra p/ o campo Prestador de Serviços – Corpo – Valor do ISS retido__

Preencher com o somatório do campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\. Caso o mesmo não esteja preenchido e se caracterizar retenção pelo prestador, preencher com o campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

__OS3470\-D__

__RN40__

__Regra p/ o campo Prestador de Serviços – Corpo – Valor de outras retenções__

Preencher com o somatório do campo VLR\_BASE\_ISS\_3 da tabela DWT\_ITENS\_SERV

__OS3470\-D__

__RN41__

__Regra p/ o campo Prestador de Serviços – Corpo – Valor da base de cálculo__

Preencher com o somatório do campo VLR\_BASE\_ISS\_1 da tabela DWT\_ITENS\_SERV\.

__OS3470\-D__

__RN42__

__Regra p/ o campo Prestador de Serviços – Corpo – Valor da alíquota do serviço__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. 

__OS3470\-D__

__RN43__

__Regra p/ o campo Prestador de Serviços – Corpo – Tipo do CPF/CNPJ do Tomador do Serviço__

Preencher com:

3, quando o campo IDENT\_ESTADO da tabela X04\_PESSOA\_FIS\_JUR  for correspondente ao COD\_ESTADO = ‘EX’

2, quando o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR tiver 14 posições\.

1, quando o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR tiver 11 posições\.

__OS3470\-D__

__RN44__

__Regra p/ o campo Prestador de Serviços – Corpo – CPF/CNPJ do Tomador do Serviço__

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN45__

__Regra p/ o campo Prestador de Serviços – Corpo – Inscrição Municipal do Tomador do Serviço__

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN46__

__Regra p/ o campo Prestador de Serviços – Corpo – Razão Social do Tomador de Serviços__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN47__

__Regra p/ o campo Prestador de Serviços – Corpo – Endereço do Tomador de Serviços__

Preencher com o campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN48__

__Regra p/ o campo Prestador de Serviços – Corpo – Número do endereço do Tomador de Serviços__

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN49__

__Regra p/ o campo Prestador de Serviços – Corpo – Complemento do endereço do Tomador de Serviços__

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN50__

__Regra p/ o campo Prestador de Serviços – Corpo – Bairro do endereço do Tomador de Serviços__

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__ RN51__

__Regra p/ o campo Prestador de Serviços – Corpo – Estado do endereço do Tomador de Serviços__

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao campo IDENT\_ESTADO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__ RN52__

__Regra p/ o campo Prestador de Serviços – Corpo – CEP do endereço do Tomador de Serviços__

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__ RN53__

__Regra p/ o campo Prestador de Serviços – Corpo – Código do Município do Tomador de Serviço conforme tabela do IBGE__

Preencher com os campos COD\_UF \+ COD\_MUNICIPIO \(preencher com 0 a esquerda até completar 5 posições\) da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__/__

__CH4712\_2013__

__ RN54__

__Regra p/ o campo Prestador de Serviços – Corpo – Telefone do Tomador de Serviços__

Preencher com o campo TELEFONE da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__ RN55__

__Regra p/ o campo Prestador de Serviços – Corpo – Email do Tomador de Serviços__

Preencher com o campo EMAIL da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__ RN56__

__Regra p/ o campo Prestador de Serviços – Corpo – Código do município conforme a tabela do IBGE\. Informa o local do recolhimento do imposto__

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota e COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL estiver preenchido, recuperar campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\. 

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota e COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL não estiver preenchido:

Exibir a mensagem no log: “O campo Cod Munic ISS não está preenchido para a nota”  concatenada com o numero da nota fiscal\.

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS <> ‘1’ referente ao serviço cadastrado na nota:

Se COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL estiver preenchido, recuperar campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\. 

Senão recuperar o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\. 

Depois de recuperado o código do município de acordo com a regra acima, esse campo deve ser preenchido com os campos COD\_UF \+ COD\_MUNICIPIO \(preencher com 0 a esquerda até completar 5 posições\) da tabela MUNICIPIO para o município correspondente\.

*Obs: O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS\.*

__OS3470\-D __

__/__

__CH4712\_2013__

__ RN57__

__Regra p/ o campo Prestador de Serviços – Corpo – Estado do município do recolhimento__

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota e COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL estiver preenchido, recuperar o campo COD\_ESTADO referente ao COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\. 

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota e COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL não estiver preenchido:

Exibir a mensagem no log: “O campo Cod Munic ISS não está preenchido para a nota” concatenada com o número da nota fiscal\.

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS <> ‘1’ referente ao serviço cadastrado na nota:

Se COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL estiver preenchido, recuperar o campo COD\_ESTADO referente ao campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\. 

Senão recuperar o campo COD\_ESTADO referente ao COD\_MUNICIPIO da tabela ESTABELECIMENTO\. 

*Obs: O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS\.*

__OS3470\-D__

__MFS\-1048310__

__  RN57a__

__Regra p/ o campo Prestador de Serviços – Corpo – Indicador de incidência do ISS__

__Este campo deverá ser tratado apenas para o Município Iracemápolis, Tupã, João Monlevade, Piracicaba, Volta Redonda, Espírito Santo do Pinhal, Casa Branca, Blumenau, São Gonçalo, Presidente Prudente, __Arceburgo__, Itobi\-SP, Paraguacu Paulista\-SP, Pirapora Do Bom Jesus\-SP, Santa Cruz Do Rio Pardo\-SP, Santo Antonio Do Jardim\-SP, Taciba\-SP e Taruma\-SP\. __

Se o campo CD\_NATUREZA\_OPERACAO \(do layout\), estiver sendo gerado com os valores ‘1’ ou ‘2’, preencher com 

 ‘1’ – Sim – ISS Tributável na Nota\. Caso contrário, ou seja, o campo CD\_NATUREZA\_OPERACAO preenchido com informação diferente de ‘1’ ou ‘2’, preencher com ‘2’ – Não – ISS Não Tributável na Nota

Tipo: Numérico 

1 Posição

Campo Obrigatório

Valores Válidos: 1, 2 

__MFS5370__

__MFS8131__

__MFS17871__

__MFS\-21322__

__MFS\-23600__

__MFS31274__

__MFS44374__

__MFS75180__

__MFS\-552778__

__MFS\-1048310__

__RN58__

__Regra p/ o campo Tomador de Serviços – Cabeçalho – Identificador __

Preencher com 1“

__OS3470\-D__

__RN59__

__Regra p/ o campo Tomador de Serviços – Cabeçalho – CPF/CNPJ do Tomador__

Preencher com o campo CGC da tabela ESTABELECIMENTO referente ao estabelecimento escolhido na tela de geração do meio magnético\.

__OS3470\-D__

__RN60__

__Regra p/ o campo Tomador de Serviços – Cabeçalho – Inscrição Municipal do Tomador__

Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO referente ao estabelecimento escolhido na tela de geração do meio magnético\.

Para construção civil, Utilities e Telecom, deverá respeitar a seguinte regra:

Se o estabelecimento possuir duas inscrições municipais, uma em seu município e outra em município onde possui uma inscrição municipal eventual, essa inscrição deverá estar parametrizada conforme tela de Cadastro de Inscrição Municipal\.

Neste caso deverá preencher com a informação do campo 05 \- INSC\_MUNICIPAL da tabela SAFX156 referente a Inscrição Municipal inserida na tela de “Cadastro de Inscrição Municipal”\.

__OS3470\-D__

__CH17331\_2013__

__RN61__

__Regra p/ o campo Tomador de Serviços – Cabeçalho – Tipo da Nota__

Preencher com “A”

__OS3470\-D__

__RN62__

__Regra p/ o campo Tomador de Serviços – Cabeçalho – Código do município do prestador conforme a tabela do IBGE__

Preencher com o campo COD\_UF \+ COD\_MUNICIPIO \(preencher com 0 a esquerda até completar 5 posições\) da tabela MUNICIPIO referente ao município do estabelecimento que está sendo gerado\. \(COD\_MUNICIPIO da tabela ESTABELECIMENTO\)

__OS3470\-D__

__/__

__CH788\_2012__

__RN63__

__Regra p/ o campo Tomador de Serviços – Corpo – Identificador__

Preencher com “2”

__OS3470\-D__

__RN64__

__Regra p/ o campo Tomador de Serviços – Corpo – Número da Nota Fiscal__

__Tela\-A__ ç__  Modulo: __Básicos >> Parâmetros__ Menu:__ Preliminares >> __Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)__

Se o campo __COD\_ESTAB__ selecionado na geração for __=__ o campo __COD\_ESTAB__ da __Tela\-A__

  __E__

Campo __Data\_fiscal __for maior ou igual o campo __Data Inicio__ da __Tela\-A__ __ __  

  __E__

Campo __NUM\_DOCFIS\_SERV __da tabela __DWT\_DOCTO\_FISCAL__ estiver preenchido

__ __ 

Então, Preencher com o campo __NUM\_DOCFIS\_SERV__ da tabela __DWT\_DOCTO\_FISCAL__

Se não,

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__OS3470\-D__

__OS3341\-A1__

__RN65__

__Regra p/ o campo Tomador de Serviços – Corpo – Série da Nota Fiscal__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__OS3470\-D__

__RN66__

__Regra p/ o campo Tomador de Serviços – Corpo – Tipo da Nota Fiscal__

Preencher com o campo Tipo Docto da tela Parâmetros por Município \- Tipo Docto\. Msaf x Tipo Docto referente ao tipo de documento cadastrado na capa da nota fiscal\.

__OS3470\-D__

__RN67__

__Regra p/ o campo Tomador de Serviços – Corpo – Data de Emissão da Nota Fiscal__

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

__OS3470\-D__

__RN68__

__Regra p/ o campo Tomador de Serviços – Corpo – Código da Natureza de Operação__

__\[ALTERADA – OS4682\]__

Preencher com:

3, Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”\.

4, Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07”\.

5, Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “09”\.

6, Verificar se o  campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “11”\.

1, Verificar se o campo COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL = ao município em questão*\. Se o campo *COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL não estiver preenchido, verificar o município cadastrado no estabelecimento\.

2, Verificar se o campo COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL <> ao município em questão\. 

__\[ALTERAÇÃO \- MFS1019978\] A comparação dos municípios deve ser pelo campo COD\_MUNIC\_MSAF da SAFX2097 e não pelo COD\_MUNIC\_ISS__

__Atenção:__ A regra de verificação das naturezas 1 e 2 para SITUAÇÃO ESPECIAL, geração do arquivo magnético pelo menu “Arquivo de Entradas de Serviços \(Consti\. Civil/Utilities/Telecom\)”, deve preencher da seguinte forma:

1, Verificar se o campo COD\_MUNIC\_MSAF da SAFX2097 \(atrelado ao COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL = ao município do prestador na X04\_PESSOA\_FIS\_JUR*\.* 

2, Verificar se o campo COD\_MUNIC\_MSAF da SAFX2097 \(atrelado ao COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL <> ao município do prestador na X04\_PESSOA\_FIS\_JUR*\.*

*Observação: *O campo COD\_MUNIC\_MSAF da SAFX2097 \(atrelado ao COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL para esse caso sempre estará preenchido, pois para seleção da situação especial o campo é obrigatório\. 

Se nenhuma das regras acima forem atendidas gravar “vazio” \(Null\)\.

__OS3470\-D__

__OS4682__

__MFS\-1019978__

__MFS\-1048310__

__RN68\.a__

__Regra p/ o campo Tomador de Serviços – Corpo – Código da Natureza de Operação – Específico para o município de Piracicaba\.__

__\[ALTERADA – \]__

Preencher com:

3, Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”\.

4, Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07”\.

5, Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “09”\.

6, Verificar se o  campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “11”\.

2, Verificar se o campo COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL <> ao município em questão\. 

__Ou __

Verificar se o__ __cod\_municipio\_pfj <> cod\_municipio\_estab __E__ ind\_tp\_ret = 2

1, Verificar se o campo COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL = ao município em questão*\. Se o campo *COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL não estiver preenchido, verificar o município cadastrado no estabelecimento\. 

__Atenção:__ A regra de verificação das naturezas 1 e 2 para SITUAÇÃO ESPECIAL, geração do arquivo magnético pelo menu “Arquivo de Entradas de Serviços \(Consti\. Civil/Utilities/Telecom\)”, deve preencher da seguinte forma:

1, Verificar se o campo COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL = ao município do prestador na X04\_PESSOA\_FIS\_JUR*\.* 

2, Verificar se o campo COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL <> ao município do prestador na X04\_PESSOA\_FIS\_JUR*\.*

*Observação: *O campo COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL para esse caso sempre estará preenchido, pois para seleção da situação especial o campo é obrigatório\. 

__MFS__[__776824__](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/776824)

__MFS837010__

__RN68\.b__

__Regra p/ o campo Tomador de Serviços – Corpo – Código da Natureza de Operação – Específico para o município de Blumenau e Presidente Prudente\.__

Preencher com:

3, Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”\.

4, Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07”\.

5, Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “09”\.

6, Verificar se o  campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “11”\.

2, Verificar se o campo COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL <> ao município em questão\. 

__Ou __

Verificar se o__ __cod\_municipio\_pfj <> cod\_municipio\_estab __E__ ind\_tp\_ret = 2

1, Verificar se o campo COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL = ao município em questão*\. Se o campo *COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL não estiver preenchido, verificar o município cadastrado no estabelecimento\. 

__\[Exclusão MFS\-1015365\]__ Trecho da regra, movido para o documento MTZ\_SIMPLISS\_Geracao\_Meio\_Magnetico\_Situacao\_Especial\.docx\. 

__Atenção:__ A regra de verificação das naturezas 1 e 2 para SITUAÇÃO ESPECIAL, geração do arquivo magnético pelo menu “Arquivo de Entradas de Serviços \(Consti\. Civil/Utilities/Telecom\)”, deve preencher da seguinte forma:

2, Verificar se o campo COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL <> ao município em questão \(município do módulo\)

__Ou __

Verificar se o__ __cod\_municipio\_pfj <> cod\_municipio\_estab __E__ ind\_tp\_ret = 2

1, Verificar se o campo COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL = ao município em questão \(município do módulo\)\.

*Observação: *O campo COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL para esse caso sempre estará preenchido, pois para seleção da situação especial o campo é obrigatório\. 

__MFS\-978069__

__MFS\-1015365__

__RN69__

__Regra p/ o campo Tomador de Serviços – Corpo – Código de Identificação do Regime Especial de Tributação__

__\[ALTERADA – CH7586\_2014\]__

Preencher com:

6,__ __Quando o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR = 01\.

1, Quando o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR = 04\.

3, Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “06”\.

4,__ __Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “02”\.

2, <a id="OLE_LINK34"></a><a id="OLE_LINK35"></a><a id="OLE_LINK36"></a>Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “08”, se não estiver preenchido <a id="OLE_LINK30"></a><a id="OLE_LINK31"></a><a id="OLE_LINK32"></a><a id="OLE_LINK33"></a>verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “421”\.

9, <a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK7"></a>Verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na <a id="OLE_LINK8"></a><a id="OLE_LINK9"></a><a id="OLE_LINK10"></a><a id="OLE_LINK11"></a><a id="OLE_LINK12"></a>tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”, se não estiver parametrizado verificar se o <a id="OLE_LINK13"></a><a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a><a id="OLE_LINK17"></a>campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”\.

10, Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420”\.__ __

11, Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “09”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “427”\.

5, Verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão  parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “452”\.

7, Verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão  parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “589”\.

8, Verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão  parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “495”\.

12, Verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = ”485” \.

__OS3470\-D__

__/__

__OS3940__

__/__

__CH7586\_2014__

__RN70__

__Regra p/ o campo Tomador de Serviços – Corpo – Optante por Simples Nacional__

__\[ALTERADA \- CH24658\_2014\]__

Preencher com:

1, quando o campo 43\-IND\_SIMPLES\_NAC da SAFX04 do prestador cadastrado na nota fiscal for igual a “S”;

2, quando o campo 43\-IND\_SIMPLES\_NAC da SAFX04 do prestador cadastrado na nota fiscal for igual a “N”;

__OS3470\-D__

__CH24658\_2014__

__RN71__

__Regra p/ o campo Tomador de Serviços – Corpo – Status da Nota Fiscal__

Preencher com:

1, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> ‘S

2, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = ‘S’

__OS3470\-D__

__RN72__

__Regra p/ o campo Tomador de Serviços – Corpo – Informações Adicionais ao Documento__

Preencher com brancos\.

__OS3470\-D__

__RN73__

__Regra p/ o campo Tomador de Serviços – Corpo – Código de Especificação da Atividade__

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao código de serviço cadastrado no item da nota fiscal\.

Formato: com ponto “\.” e sem o primeiro zero “0” à esquerda\.

Exemplos: Para o código 1401, informar no arquivo 14\.01

                 Para o código 0701, informar no arquivo 7\.01

     Para o código 0026, informar no arquivo 0\.26

__OS3470\-D__

__CH14640\_2012__

__RN74__

__Regra p/ o campo Tomador de Serviços – Corpo – Valor total do serviço__

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\.

__OS3470\-D__

__RN75__

__Regra p/ o campo Tomador de Serviços – Corpo – Valor de dedução__

Preencher com o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV\.

__OS3470\-D__

__RN76__

__Regra p/ o campo Tomador de Serviços – Corpo – Retenção na fonte__

Para que esse campo seja preenchido com “1”, é necessário que pelo menos umas das seguintes opções seja verdadeira:

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL está preenchido\. Se estiver preenchido, verificar se está preenchido com “2” “1”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “N” “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV não está preenchido\. 

Caso nenhuma das opões seja verdadeira, preencher com “2”\.

__OS3470\-D__

__MFS\-1047132__

__RN77__

__Regra p/ o campo Tomador de Serviços – Corpo – Valor do ISS – Imposto __

Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

__OS3470\-D__

__RN78__

__Regra p/ o campo Tomador de Serviços – Corpo – Valor do ISS Retido__

Preencher com o somatório do campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\. Caso o mesmo não esteja preenchido e se caracterizar retenção pelo prestador, preencher com o campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

__OS3470\-D__

__RN79__

__Regra p/ o campo Tomador de Serviços – Corpo – Valor de outras retenções__

Preencher com o somatório do campo VLR\_BASE\_ISS\_3 da tabela DWT\_ITENS\_SERV

__OS3470\-D__

__RN80__

__Regra p/ o campo Tomador de Serviços – Corpo – Valor da base de cálculo__

Preencher com o somatório do campo VLR\_BASE\_ISS\_1 da tabela DWT\_ITENS\_SERV\.

\[__MFS\-565912__\] __Regra específica para município de Arceburgo__

Se o campo VLR\_BASE\_ISS\_1 da tabela DWT\_ITENS\_SERV, não esteja preenchido, preencher com o somatório do campo VLR\_BASE\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\. Ou Se o campo VLR\_BASE\_ISS\_RETIDO não estiver preenchido ou preenchido com zeros, preencher com o somatório dos campos VLR\_BASE\_ISS\_2, e ou VLR\_BASE\_ISS\_3 da tabela DWT\_ITENS\_SERV\.

__OS3470\-D__

__MFS\-565912__

__RN81__

__Regra p/ o campo Tomador de Serviços – Corpo – Valor da alíquota do serviço__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

__\[MFS\-565912\] Regra específica para município de Arceburgo__

Se o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV, não tiver preenchido, preencher com o campo VLR\_ALIQ\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\. 

__OS3470\-D__

__MFS\-565912__

__RN82__

__Regra p/ o campo Tomador de Serviços – Corpo – Tipo do CPF/CNPJ do Prestador__

Preencher com:

3, quando o campo IDENT\_ESTADO da tabela X04\_PESSOA\_FIS\_JUR for correspondente ao COD\_ESTADO = ‘EX’

2, quando o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR tiver 14 posições\.

1, quando o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR tiver 11 posições\.

__OS3470\-D__

__RN83__

__Regra p/ o campo Tomador de Serviços – Corpo – CPF/CNPJ do Prestador__

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN84__

__Regra p/ o campo Tomador de Serviços – Corpo – Inscrição Municipal do Prestador__

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN85__

__Regra p/ o campo Tomador de Serviços – Corpo – Razão Social do Prestador__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN86__

__Regra p/ o campo Tomador de Serviços – Corpo – Endereço do Prestador__

Preencher com o campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN87__

__Regra p/ o campo Tomador de Serviços – Corpo – Número do Endereço do Prestador__

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN88__

__Regra p/ o campo Tomador de Serviços – Corpo – Complemento do Endereço do Prestador__

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN89__

__Regra p/ o campo Tomador de Serviços – Corpo – Bairro do Endereço do Prestador__

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN90__

__Regra p/ o campo Tomador de Serviços – Corpo – Estado do Endereço do Prestador__

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao campo IDENT\_ESTADO da tabela X04\_PESSOA\_FIS\_JUR\. 

__OS3470\-D__

__RN91__

__Regra p/ o campo Tomador de Serviços – Corpo – CEP do Endereço do Prestador__

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN92__

__Regra p/ o campo Tomador de Serviços – Corpo – Código do Município do Prestador conforme a tabela do IBGE__

Preencher com o campo COD\_UF \+ COD\_MUNICIPIO \(preencher com 0 a esquerda até completar 5 posições\) da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__/__

__CH4712\_2013__

__RN93__

__Regra p/ o campo Tomador de Serviços – Corpo – Telefone do Prestador__

Preencher com o campo TELEFONE da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN94__

__Regra p/ o campo Tomador de Serviços – Corpo – E\-mail do Prestador__

Preencher com o campo EMAIL da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN95__

__Regra p/ o campo Tomador de Serviços – Corpo – Código do Município conforme a tabela do IBGE\. Informa o local do recolhimento do imposto__

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota e COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL estiver preenchido, recuperar campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\. 

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota e COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL não estiver preenchido:

Exibir a mensagem no log: “O campo Cod Munic ISS não está preenchido para a nota”  concatenada com o número da nota fiscal\.

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS <> ‘1’ referente ao serviço cadastrado na nota:

Se COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL estiver preenchido, recuperar campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\. 

Senão recuperar o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\. 

Depois de recuperado o código do município de acordo com a regra acima, esse campo deve ser preenchido com os campos COD\_UF \+ COD\_MUNICIPIO \(preencher com 0 a esquerda até completar 5 posições\) da tabela MUNICIPIO para o município correspondente\.

*Obs: O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS\.*

__OS3470\-D__

__/__

__CH4712\_2013__

__MFS\-1048310__

__RN95\.a__

__Regra p/ o campo Tomador de Serviços – Corpo – Código do Município conforme a tabela do IBGE\. Informa o local do recolhimento do imposto\.__

__Este campo deverá ser tratado apenas para o município de Piracicaba __

Se IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL = ‘1’ recuperar o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\. 

Caso o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL não esteja preenchido exibir a seguinte mensagem no log: “O campo Cod Munic ISS não está preenchido para a nota” concatenar o número da nota fiscal na mensagem\.

__Ou__

Se IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL = ‘2’ recuperar o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \. 

Caso o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR não esteja preenchido exibir a seguinte mensagem no log: “O campo Cod Munic ISS não está preenchido para o fornecedor” concatenar com o código do fornecedor\. 

__MFS\-810921 __

__RN96__

__Regra p/ o campo Tomador de Serviços – Corpo – Estado do Município do recolhimento__

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota e COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL estiver preenchido, recuperar o campo COD\_ESTADO referente ao COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\. 

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota e COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL não estiver preenchido:

Exibir a mensagem no log: “O campo Cod Munic ISS não está preenchido para a nota”  concatenada com o número da nota fiscal\.

Se IND\_TP\_SERVICO da tabela X2018\_SERVICOS <> ‘1’ referente ao serviço cadastrado na nota:

Se COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL estiver preenchido, recuperar o campo COD\_ESTADO referente ao campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\. 

Senão recuperar o campo COD\_ESTADO referente ao COD\_MUNICIPIO da tabela ESTABELECIMENTO\. 

*Obs: O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS\.*

__OS3470\-D__

__  RN96\.a__

__Regra p/ o campo Tomador de Serviços – Corpo – Indicador de incidência do ISS__

__Este campo deverá ser tratado apenas para o Município Iracemápolis, Tupã, João Monlevade, Piracicaba, Volta Redonda, Espírito Santo do Pinhal, Casa Branca, Blumenau, São Gonçalo e Presidente Prudente, Arceburgo, Itobi\-SP, Paraguacu Paulista\-SP, Pirapora Do Bom Jesus\-SP, Santa Cruz Do Rio Pardo\-SP, Santo Antonio Do Jardim\-SP, Taciba\-SP e Taruma\-SP\. __

Se o campo CD\_NATUREZA\_OPERACAO \(do layout\), estiver sendo gerado com os valores ‘1’ ou ‘2’, preencher com 

 ‘1’ – Sim – ISS Tributável na Nota\. Caso contrário, ou seja, o campo CD\_NATUREZA\_OPERACAO preenchido com informação diferente de ‘1’ ou ‘2’, preencher com ‘2’ – Não – ISS Não Tributável na Nota\.

__\[ALTERAÇÃO\-MFS1012082\]__ \- Específica para município de Presidente Prudente \- Arquivo de Entradas de Serviços \(Consti\. Civil/Utilities/Telecom\)”,

Se o campo CD\_NATUREZA\_OPERACAO \(do layout\), estiver sendo gerado com o valor ‘1’ \(Tributação no município\), e o campo IND\_TP\_RET da tabela SAFX07 for = 1, então preencher com ‘1’ – Sim – ISS Tributável na Nota\. 

Se o campo CD\_NATUREZA\_OPERACAO \(do layout\), estiver preenchido com ‘2’ \(Tributação fora do município\), e o campo IND\_TP\_RET da tabela SAFX07 for = 2, então preencher com ‘2’ – Não – ISS Não Tributável na Nota\.

Caso nenhuma condição dessa for verdadeira, permanece regra atual

Tipo: Numérico 

1 Posição

Campo Obrigatório

Valores Válidos: 1, 2 

__MFS5370__

__MFS8131__

__MFS17871  
MFS\-21322__

__MFS\-23600__

__MFS31274__

__MFS44374__

__MFS75180__

__MFS\-552778__

__MFS\-1012082__

__MFS\-1048310__

__RN96b__

__Regra p/ o campo Tomador de Serviços – Corpo – Estado do Município do recolhimento__

__Este campo deverá ser tratado apenas para o município de Piracicaba __

Se IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL = ‘1’ recuperar o campo COD\_ESTADO\_NF da tabela DWT\_DOCTO\_FISCAL\. 

__Ou__

Se IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL = ‘2’ recuperar o campo COD\_ESTADO da tabela X04\_PESSOA\_FIS\_JUR \. 

__MFS\-810921__

__RN97__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Identificador__

Preencher com “1”

__OS3470\-D__

__RN98__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Número do Lote enviado__

Preencher com número seqüencial e único\. Deverá ser iniciado no número 1 e continuar a seqüência nos demais arquivos enviados posteriormente\. Cada arquivo deverá ser composto por um único lote\.

__OS3470\-D__

__RN99__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – CPF/CNPJ do Prestador__

Preencher com o campo CGC da tabela ESTABELECIMENTO referente ao estabelecimento escolhido na tela de geração do meio magnético\.

__OS3470\-D__

__RN100__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Inscrição Municipal do Prestador__

Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO referente ao estabelecimento escolhido na tela de geração do meio magnético\.

__OS3470\-D__

__RN101__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Código do Município do Prestador conforme a tabela do IBGE__

Preencher com os campos COD\_UF \+ COD\_MUNICIPIO \(preencher com 0 a esquerda até completar 5 posições\) da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO referente ao estabelecimento escolhido na tela de geração do meio magnético\.

__OS3470\-D__

__/__

__CH4712\_2013__

__RN102__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Número do RPS__

__Tela\-A__ ç__  Modulo: __Básicos >> Parâmetros__ Menu:__ Preliminares >> __Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)__

Se o campo __COD\_ESTAB__ selecionado na geração for __=__ o campo __COD\_ESTAB__ da __Tela\-A__

  __E__

Campo __Data\_fiscal __for maior ou igual o campo __Data Inicio__ da __Tela\-A__ __ __  

  __E__

Campo __NUM\_DOCFIS\_SERV __da tabela __DWT\_DOCTO\_FISCAL__ estiver preenchido

__ __ 

Então, Preencher com o campo __NUM\_DOCFIS\_SERV__ da tabela __DWT\_DOCTO\_FISCAL__

Se não, 

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL  

__OS3470\-D__

__OS3341\-A1__

__RN103__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Série do RPS__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__OS3470\-D__

__RN104__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Data de Emissão do RPS__

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

__OS3470\-D__

__RN105__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Código da Natureza da Operação__

Preencher com:

1, Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “10”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “445” e campo COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL = ao município em questão*\.Se o campo *COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL não estiver preenchido, verificar o município cadastrado no estabelecimento\.

2, Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “10”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “445” e campo COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL <> ao município em questão*\.Se o campo *COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL não estiver preenchido, verificar o município cadastrado na tabela X04\_PESSOA\_FIS\_JUR\.

3, Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “04”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\.

4, Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “01”, s se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420”\.

5, Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “03”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “427”\.

6, Verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “485”\.

__OS3470\-D__

__RN106__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Código de Identificação do Regime Especial de Tributação__

Preencher com o campo IND\_ISS da tabela ESTABELECIMENTO

__OS3470\-D__

__RN107__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Optante pelo Simples Nacional__

Preencher com:

1, Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “07”\.

2, quando o campo acima for <> “07

__OS3470\-D__

__RN108__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Status do RPS__

Preencher com:

1, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> ‘S

2, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = ‘S’

__OS3470\-D__

__RN109__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Código de especificação da Atividade Federal__

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao código de serviço cadastrado no item da nota fiscal\.

__OS3470\-D__

__RN110__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Código de especificação da Atividade Municipal__

Preencher com brancos\.

__OS3470\-D__

__RN111__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Código CNAE__

Preencher com campo COD\_ATIVIDADE da tabela ESTABELECIMENTO\.

__OS3470\-D__

__RN112__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Descrição do Serviço__

Preencher com o campo DSC\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao código de serviço cadastrado no item da nota fiscal\.

__OS3470\-D__

__RN113__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Valor total do Serviço__

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\.

__OS3470\-D__

__RN114__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Valor de dedução__

Preencher com o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV\.

__OS3470\-D__

__RN115__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Valor do PIS__

Preencher com o somatório do campo VLR\_PIS da tabela DWT\_ITENS\_SERV

__OS3470\-D__

__RN116__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Valor do COFINS__ 

Preencher com o somatório do campo VLR\_COFINS da tabela DWT\_ITENS\_SERV

__OS3470\-D__

__RN117__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Valor do INSS__

Preencher com o somatório do campo VLR\_BASE\_INSS da tabela DWT\_ITENS\_SERV

__OS3470\-D__

__RN118__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Valor do Imposto de Renda__

Preencher com o somatório do campo VLR\_TRIBUTO\_IR da tabela DWT\_ITENS\_SERV

__OS3470\-D__

__RN119__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Valor da Contribuição Social__

Preencher com o somatório do campo VLR\_CSLL da tabela DWT\_ITENS\_SERV

__OS3470\-D__

__RN120__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Retenção da Fonte__

Para que esse campo seja preenchido com “1”, é necessário que pelo menos umas das seguintes opções seja verdadeira:

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se estiver preenchido, verificar se está preenchido com “1”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV não está preenchido\.

Caso nenhuma das opões seja verdadeira, preencher com “2”\.

__OS3470\-D__

__OS3470\-I1__

__RN121__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Valor do ISS – Imposto __

Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

__OS3470\-D__

__RN122__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Valor do ISS Retido__

Preencher com o somatório do campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\. Caso o mesmo não esteja preenchido e se caracterizar retenção pelo prestador, preencher com o campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

__OS3470\-D__

__RN123__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Valor das outras retenções__

Preencher com o somatório do campo VLR\_BASE\_ISS\_3 da tabela DWT\_ITENS\_SERV

__OS3470\-D__

__RN124__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Valor da base de cálculo__

Preencher com o somatório do campo VLR\_BASE\_ISS\_1 da tabela DWT\_ITENS\_SERV

__OS3470\-D__

__RN125__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Valor da alíquota do serviço__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

__OS3470\-D__

__RN126__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Valor líquido da Nota Fiscal__

Preencher com o somatório do campo VLR\_TOT da tabela DWT\_ITENS\_SERV

__OS3470\-D__

__RN127__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Valor de desconto incondicionado__

Preencher com  zeros\.

__OS3470\-D__

__RN128__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Valor de desconto condicionado__

Preencher com o somatório do campo VLR\_DESCONTO da tabela DWT\_ITENS\_SERV

__OS3470\-D__

__RN129__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Tipo do CPF/CNPJ do Tomador do Serviço__

Preencher com:

3, quando o campo IDENT\_ESTADO da tabela X04\_PESSOA\_FIS\_JUR  for correspondente ao COD\_ESTADO = ‘EX’

2, quando o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR tiver 11 posições\.

1, quando o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR tiver 11 posições\.

__OS3470\-D__

__RN130__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – CPF/CNPJ do Tomador do Serviço__

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN131__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Inscrição Municipal do Tomador do Serviço__

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN132__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Razão Social do Tomador do Serviço__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN133__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Endereço do Tomador do Serviço__

Preencher com o campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN134__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Número do endereço do Tomador do Serviço__

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN135__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Complemento do endereço do Tomador do Serviço__

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN136__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Bairro do endereço do Tomador do Serviço__

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN137__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Estado do endereço do Tomador do Serviço__

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao campo IDENT\_ESTADO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN138__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – CEP do endereço do Tomador do Serviço__

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN139__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Código do município do tomador do serviço conforme tabela do IBGE__

Preencher com os campos COD\_UF \+ COD\_MUNICIPIO \(preencher com 0 a esquerda até completar 5 posições\) da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__/__

__CH4712\_2013__

__RN140__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Telefone do Tomador do Serviço__

Preencher com o campo TELEFONE da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN141__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – E\-mail do Tomador do Serviço__

Preencher com o campo EMAIL da tabela X04\_PESSOA\_FIS\_JUR\.

__OS3470\-D__

__RN142__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Razão Social do Intermediário do Serviço__

Preencher com brancos\.

__OS3470\-D__

__RN143__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – CPF/CNPJ do Intermediário do Serviço__

Preencher com brancos\.

__OS3470\-D__

__RN144__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Tipo do CPF/CNPJ do Intermediário do Serviço__

Preencher com brancos\.

__OS3470\-D__

__RN145__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Inscrição Municipal do Intermediário do Serviço__

Preencher com brancos\.

__OS3470\-D__

__RN146__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Código Obra Construção Civil__

Preencher com brancos\.

__OS3470\-D__

__RN147__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Código Art Construção Civil__

Preencher com brancos\.

__OS3470\-D__

__RN148__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Número do RPS substituta__

Preencher com brancos\.

__OS3470\-D__

__RN149__

__Regra p/ o campo Prestador de Serviços – RPS – Corpo – Série do RPS Substituta__

Preencher com brancos\.

__OS3470\-D__

__RN150__

__Regra p/ o campo Lista de Itens de Serviço – Identificador __

Preencher com “2”

__OS3470\-D__

__RN151__

__Regra p/ o campo Lista de Itens de Serviço – Descrição do Item de serviço __

Preencher com o campo DSC\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao código de serviço cadastrado no item da nota fiscal\.

__OS3470\-D__

__RN152__

__Regra p/ o campo Lista de Itens de Serviço – Quantidade itens __

Preencher com o campo QUANTIDADE da tabela DWT\_ITENS\_SERV referente ao código do serviço mencionado anteriormente\.

__OS3470\-D__

__RN153__

__Regra p/ o campo Lista de Itens de Serviço – Valor de cada unidade__

Preencher com o campo VLR\_UNIT da tabela DWT\_ITENS\_SERV referente ao código do serviço mencionado anteriormente\.

__OS3470\-D__

__RN154__

__Regra p/ inclusão do novo módulo no Manager – Embú:__

O novo módulo “Embú” deve ficar localizado no grupo “Municipal” 

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de Embú”\.

OS3470\-D

__RN155__

__Regra p/ abertura do novo módulo no Manager – Embú:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “15004” \(Embú\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Embú, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS3470\-D__

__RN156__

__Regra p/ inclusão do novo módulo no Manager – Presidente Prudente:__

O novo módulo “Presidente Prudente” deve ficar localizado no grupo “Municipal” 

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de Presidente Prudente”\.

OS3470\-D

__RN157__

__Regra p/ abertura do novo módulo no Manager – Presidente Prudente:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “41406” \(Presidente Prudente\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Presidente Prudente, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS3470\-D__

__RN158__

__Regra p/ inclusão do novo módulo no Manager – São José do Rio Pardo:__

O novo módulo “São José do Rio Pardo” deve ficar localizado no grupo “Municipal” 

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de São José do Rio Pardo”\.

OS3470\-D

__RN159__

__Regra p/ abertura do novo módulo no Manager – São José do Rio Pardo:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “49706” \(São José do Rio Pardo\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de São José do Rio Pardo, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS3470\-D__

__RN160__

__Regra p/ inclusão do módulo no Manager – Balneário Camboriú:__

Manter o módulo “Balneário Camboriú” no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de Balneário Camboriú”\.

OS4840

__RN161__

__Regra p/ abertura do módulo no Manager – Balneário Camboriú:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SC” e ao código de município do IBGE igual a “2008” \(Balneário Camboriú\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Balneário Camboriú, Santa Catarina\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS4840__

__RN162__

__Regra p/ inclusão do módulo no Manager – Iracemápolis:__

Manter o módulo __“Iracemápolis”__ no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de Iracemápolis”\.

__MFS5370__

__RN163__

__Regra p/ abertura do módulo no Manager – Iracemápolis:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “21408” \(Iracemápolis\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Iracemápolis, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS5370__

__RN164__

__Regra p/ inclusão do módulo no Manager – Carapicuíba:__

Manter o módulo __“Carapicuíba”__ no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de Carapicuíba”\.

__MFS\_5905__

__RN165__

__Regra p/ abertura do módulo no Manager – Carapicuíba:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “10609” \(Carapicuíba\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Carapicuíba, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\_5905__

__RN166__

__Regra p/ inclusão do módulo no Manager – Tupã:__

Manter o módulo __“Tupã”__ no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de Tupã”\.

__MFS8131__

__RN167__

__Regra p/ abertura do módulo no Manager – Tupã:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “55000” \(Tupã\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Tupã, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS8131__

__RN168__

__Regra p/ inclusão do módulo no Manager – João Monlevade:__

Manter o módulo __“João Monlevade”__ no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de João Monlevade”\.

__MFS17871__

__RN169__

__Regra p/ abertura do módulo no Manager – João Monlevade:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “MG” e ao código de município do IBGE igual a “36207” \(João Monlevade\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de João Monlevade, Minas Gerais\. Alguns dados não estarão disponíveis\. Deseja continuar? ”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS17871__

__RN170__

__Regra p/ inclusão do módulo no Manager – Volta Redonda:__

Incluir o módulo __“Volta Redonda”__ no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de Volta Redonda”\.

__MFS\-21322__

__RN171__

__Regra p/ abertura do módulo no Manager – Volta Redonda:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “RJ” e ao código de município do IBGE igual a “6305” \(Volta Redonda\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Volta Redonda, Rio de Janeiro\. Alguns dados não estarão disponíveis\. Deseja continuar? ”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-21322__

__RN172__

__Regra p/ inclusão do módulo no Manager – __Espírito Santo do Pinhal__:__

Incluir o módulo __“__Espírito Santo do Pinhal__”__ no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de Espírito Santo do Pinhal”\.

__MFS\-23600__

__RN173__

__Regra p/ abertura do módulo no Manager – __Espírito Santo do Pinhal__:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “15186” \(Espírito Santo do Pinhal\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Espírito Santo do Pinhal, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar? ”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-23600__

__RN174__

__Regra p/ inclusão do módulo no Manager – __Casa Branca__:__

Incluir o módulo __“__Casa Branca__”__ no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de Casa Branca”\.

__MFS\-23600__

__RN175__

__Regra p/ abertura do módulo no Manager – __Casa Branca__:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “10807” \(Casa Branca\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Casa Branca, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar? ”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-23600__

__RN176__

__Regra p/ inclusão do módulo no Manager – __Blumenau__:__

Incluir o módulo __“__Blumenau__”__ no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de Blumenau”\.

__MFS31274__

__RN177__

__Regra p/ abertura do módulo no Manager – __Blumenau__:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SC” e ao código de município do IBGE igual a “2404” \(Blumenau\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Blumenau, Santa Catarina\. Alguns dados não estarão disponíveis\. Deseja continuar? ”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS31274__

__RN178__

__Regra p/ inclusão do módulo no Manager – São Gonçalo:__

Incluir o módulo __“__São Gonçalo__”__ no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de São Gonçalo”\.

__MFS44374__

__RN179__

__Regra p/ abertura do módulo no Manager – São Gonçalo:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “RJ” e ao código de município do IBGE igual a “4904” \(São Gonçalo\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de São Gonçalo, Rio de Janeiro\. Alguns dados não estarão disponíveis\. Deseja continuar? ”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS44374__

__RN180__

__Regra p/ inclusão do novo módulo no Manager – Arceburgo:__

O novo módulo “Arceburgo” deve ficar localizado no grupo “Municipal” 

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de Arceburgo”\.

__MFS\-552778__

__RN181__

__Regra p/ abertura do novo módulo no Manager – Arceburgo:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “MG” e ao código de município do IBGE igual a “4106” \(Arceburgo\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Arceburgo, Minas Gerais\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-552778__

__RN182__

__Regra p/ inclusão do novo módulo no Manager – Nome dos Municípios:__

__MUNICÍPIO__

__ESTADO__

__CÓDIGO MUNICÍPIO__

__ITOBI__

__SP__

23800

__PARAGUACU PAULISTA__

__SP__

35507

__PIRAPORA DO BOM JESUS__

__SP__

39103

__SANTA CRUZ DO RIO PARDO__

__SP__

46405

__SANTO ANTONIO DO JARDIM__

__SP__

48104

__TACIBA__

__SP__

52908

__TARUMA__

__SP__

53955

O novo módulo “Nome do Município” deve ficar localizado no grupo “Municipal” 

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados, inclusive os de profissionais autônomos do município de Nome do município”\.

__MFS\-1048310__

__RN183__

__Regra p/ abertura do novo módulo no Manager – Nome dos Municípios:__

__MUNICÍPIO__

__ESTADO__

__CÓDIGO MUNICÍPIO__

__ITOBI__

__SP__

23800

__PARAGUACU PAULISTA__

__SP__

35507

__PIRAPORA DO BOM JESUS__

__SP__

39103

__SANTA CRUZ DO RIO PARDO__

__SP__

46405

__SANTO ANTONIO DO JARDIM__

__SP__

48104

__TACIBA__

__SP__

52908

__TARUMA__

__SP__

53955

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “XX” e ao código de município do IBGE igual a “XXXX” \(Nome do município\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de “Nome do município”, UF\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-1048310__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

