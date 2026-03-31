# MTZ-ICMS-Geracao_Convenio115

- **Fonte:** MTZ-ICMS-Geracao_Convenio115.docx
- **Modificado:** 2024-07-11
- **Tamanho:** 118 KB

---

# Módulo – ICMS – Convênio ICMS 115

__Localização__ à Menu: Estadual, Módulo: ICMS, menu DATAMART à Convênio ICMS 115 à Geração do Meio Magnético

	

##### DOCUMENTO DE REQUISITO\.

###### DR

###### Nome

__Descrição__

__OS2609\-D__

Alteração nos Livros de Saídas

Para que os Livros de Saídas sejam emitidos corretamente, deverá ser criado um campo “Consumidor Final” na capa de Utilities, complementar os CFOP´s de Não Contribuintes Estaduais,corrigir os resumos de Decêndio, Quinzena e Código de Receita, excluir o Label  “Desconsiderar valor de descontos no cálculo do valor contábil” da tela do Geração do Mapa Resumo/Geração do meio magnético do convênio 115  e  criar uma parametrização para unificar as configurações nos Parâmetros por UF da tela de Geração dos Mapas Resumo  e  Livros de Saídas\.

__CH76590__

Quebra do arquivo em volumes

Correção na quebra do arquivo em volumes para considerar a regra inserida pela OS2768

__OS2768\-M/ 3424\-D__

ICMS \- Geração de Documentos Fiscais de Utilities Cancelados no Convênio ICMS 115/03 para empresas de Energia Elétrica

Ajuste conforme Decreto 57\.177/11

Gerar Documentos Fiscais de Utilities no meio magnético Convênio ICMS 115/03 que estejam com status “Cancelado”, cujo modelo seja “06 – Nota Fiscal/Conta de Energia Elétrica modelo 06” e cuja Data de Cancelamento seja maior que a Data de Vencimento\. Esses documentos fiscais deverão ficar com status “Normal”\.

Ajuste conforme Decreto 57\.177/11

__OS3295__

Atendimento a Portaria CAT 187/2010

Alterações do Mastersaf p/ atendimento a Portaria CAT 187/2010 

__OS3335\-A__

Telecom\-Geração da EFD p/as UF’s dos tomadores do serviço\.

Telecom \- Geração da EFD p/as UF’s dos Tomadores dos Serviços de TV por Assinatura via Satélite \(atendimento ao Convênio ICMS 52/2005\)\.  

__OS3330\-A__

Geração Única\.

O objetivo é especificar as alterações necessárias para gerar o meio magnético Convênio 115 de forma única, ou seja, selecionar um ou mais estabelecimentos e efetuar uma única geração\.

__CH111412__

Ajuste na geração do meio magnético 

Ajuste na geração do meio magnético, pois a regra de quebra dos registros não está sendo respeitada conforme legislação\.

__OS3597__

Atualização legal do Convênio ICMS 07 13/03/2012

Alteração de tamanho de campos do Mestre de Documentos Fiscal e Dados do Destinatário do Documento Fiscal

__OS3851__

Correção dos Registros de Telecom do Sped Fiscal;

A totalização dos valores p/geração da tabela auxiliar ICT\_MM\_CONV115\_UF\_CFOP passará a considerar os novos campos 103 e 104 da SAFX43 \(vide RN00\)\. 

__CH7733\_2012__

Alteração na regra\.

Alteração da regra para gerações anteriores a 01/07/2012, onde passa a vigorar o Convênio ICMS 07/2012

__OS3330\-A1__

Conv\. 115  por IEU

Permitir que o Conv\. ICMS também seja gerado por IEU\.

__CH29604\_2012__

Ajuste na geração do meio magnético

Ajuste na regra do Cálculo da quantidade de documentos fiscais por volume \(arquivo\)

__OS3974__

Portaria CAT 24/2013 

Alteração na geração do arquivo do Conv\. 155/03, de acordo com a Portaria CAT 24/2013 \(ver __RN00__ e __RN16__\)\.

__OS3694\-A1__

Ajuste na regra de quebra do arquivo

Ajuste na regra de quebra do arquivo\.

__OS4144__

Novo parâmetro na geração do Convênio 115

Novo parâmetro na geração do Convênio 115 p/o preenchimento da descrição do arquivo dos itens \(ver __RN17__\)\.

__OS4281__

Exclusão RN04 e RN09

As regras referentes à quebra do arquivo por volume serão transferidas para o arquivo MTZ\_ICMS\_Convenio\_115\_ Quantidade\_Documentos\_Fiscais\_por\_Volume\.docx

__OS4413\-A__

Tratamento dos itens negativos da nova tabela SAFX431

Alteração da geração para considerar os itens da nova tabela SAFX431 \(Itens Negativos de Utilities\) \(ver__ RN18__\)

__OS4786__

Alteração na geração do Convênio 115 p/tratamento do modelo 

Separar os documentos fiscais de modelos diferentes em arquivos distintos \(ver __RN00__, __RN19__ e __RN20__\)\. 

__MFS4969__

Atendimento ao Convênio ICMS 60

Atendimento ao Convênio ICMS 60\.

__CH15005\_2016__

Tratamento para notas fiscais canceladas de estabelecidos no estado do Rio Grande do Sul

Este documento tem como objetivo alterar a geração do Convênio 115 para tratar as notas fiscais de estabelecidos no estado do Rio Grande do Sul\.

__MFS7160__

Atendimento ao Convênio ICMS 94

Atendimento ao Convênio ICMS 94/2016 e Convênio ICMS 160/2015\.

__MFS6572__

Atendimento ao Convênio ICMS 60

Atendimento ao Convênio ICMS 60

__MFS7783__

Alteração na geração do campo “Tipo de Utilização” dos itens

Alteração na geração do campo “Tipo de Utilização” dos itens \(ver __RN24__\)

__CH24596\_2016__

Ajuste na geração do meio magnético

Ajuste nas regras dos campos que contém informações de telefone, 22 e 26 arquivo mestre e 11 e 13 arquivo de dados destinatários\. Para alterar a tipo para alfanuméricos conforme retorno da secretaria da fazendo\.

__MFS\-15387__

Alteração no preenchimento do campo 26 do Arquivo Mestre

A geração do registro mestre de notas fiscais de serviços de telecom referente ao campo 26 do item 5\.2\.5\.2 do Convênio 115/03 deverá ser gerado sem informações \(nulo\) com a publicação do Ato COTEPE 74/17\. 

__CH17064\_2018 \(MFS\-19361\)__

Alteração no preenchimento do campo 24 do Arquivo de Itens

A geração do campo 24\-Outros Valores do Arquivo de Itens foi tratado para o cliente Nextel que não utiliza da SAFX431\.

__MFS20889__

Alteração no preenchimento do campo 09 do Arquivo dos Dados Cadastrais\.

Alteração no Arquivo dos Dados Cadastrais considerando parâmetro da tela de geração do convênio 115 para apresentar o campo 09 – Município conforme determinação do IBGE\.

__MFS24491__

Criação do parâmetro para desconsiderar os itens de desconto

Alterar a geração para tratar o parâmetro que desconsidera os itens de desconto da SAFX43\.

__MFS31749__

Geração da tabela auxiliar ICT\_MM\_CONV115\_UF\_CFOP

Inclusão da gravação de 2 novos campos na tabela ICT\_MM\_CONV115\_UF\_CFOP\.

__MFS67557__

Geração da tabela auxiliar ICT\_MM\_CONV115\_UF\_CFOP

Alteração da gravação dos campos Valor Outras e Valor Isentas, para utilizar as regras da Portaria CAT 66/2019 para preenchimento dos campos\.

__MFS91802__

Tratamento dos itens de desconto da SAFX431 p/ Arquivo Mestre

Readequação da Regra para considerar o parâmetro “Desconsiderar Itens de Desconto \(SAFX431\) p/ Arquivo Mestre” para desconsiderar os itens de desconto na geração do Arquivo Mestre\.

__MFS524611__

Andréa Rocha

Alteração nas regras de geração da tabela ICT\_MM\_CONV115\_UF\_CFOP para não considerar os documentos escriturados com o CFOP 0000\.

__MFS657377__

Andréa Rocha

Alteração das regras de geração do campo município no arquivo de Dados Cadastrais, quando a UF for do exterior\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Regras Gerais da Geração do Arquivo do Convênio ICMS 115/03__:

Os arquivos do Convênio 115 são gerados por série do documento, e por quantidade de documentos\. Séries e Modelos __\(\*\)__ diferentes geram arquivos diferentes, e dependendo da quantidade de notas, poderão ser gerados vários volumes da mesma série e modelo __\(\*\)__\.

Ao final da geração, serão armazenadas diversas informações sobre cada volume de arquivo gerado:

Tabela __ICT\_MM\_CONV115__ à Contém os dados gerais de cada volume do arquivo \(data, número, valores totais, nome e volume do arquivo\)\. O código de autenticação digital do arquivo mestre será preenchido apenas na rotina de importação do hash\-code\. 

Tabela __ICT\_MM\_CNV115\_UF\_CFOP__ à Contém o detalhamento dos valores totalizados por CST / CFOP / ALIQ / UF \(UF do destinatário do documento\)\. Estes valores são utilizados na geração do Sped Fiscal\.

__\(\*\) Alteração da OS4786 \(Maio/2015\): Separação dos documentos de modelos diferentes em arquivos diferentes__

Originalmente, os arquivos do Conv115 eram gerados por Série\. Assim, documentos de séries diferentes, eram gerados em arquivos diferentes\.

A partir da OS4786 além da Série, o Modelo dos documentos também passou a ser utilizado como critério para a separação dos arquivos\. Assim, os arquivos não terão mais modelos diferentes no mesmo arquivo\. Sempre que existir no período documentos de modelos diferentes, serão gerados arquivos diferentes, um para cada modelo\. Para maiores detalhes, ver as regras __RN19__ e __RN20__\.

__Alteração da OS3851:__

    A geração do Convênio 115 foi alterada para durante a totalização dos valores que geram a tabela auxiliar ICT\_MM\_CONV115\_UF\_CFOP, sejam

    considerados também os valores dos novos campos 103 e 104 da SAFX43 \(Valor da BC e do ICMS devido a outra UF\)\. O valor destes campos será

    considerado na totalização somente no caso das operações interestaduais, ou seja, apenas quando o CFOP do item for iniciado por “6” ou “7”\.

     Obs: A condição do CFOP interestadual é apenas por uma questão de segurança, pois na verdade estes novos campos  da SAFX43 foram criados

               especificamente para a carga dos valores da base de cálculo e ICMS devido a outra UF nos termos do Convênio 52/2005, e assim, só deverão

              ser carregados nas prestações de serviço não\-medido de TV por assinatura via satélite para outra UF\.

__Alteração da OS3335\-A__:

    A geração passou a verificar se  o estabelecimento em questão é obrigado ao Convênio ICMS 52/2005 \(parâmetro “Obrigado ao Convênio ICMS 52/2005”

    do módulo Sped Fiscal, menu “Parâmetros à Dados Iniciais”\)\.

Quando o parâmetro for = “S”, na geração de cada volume do arquivo, serão armazenadas algumas informações sobre as UF’s com as quais existam operações\. Para cada uma das UF’s \(*exceto a UF do próprio estabelecimento*\), para as quais existam notas fiscais emitidas no período, serão ser armazenadas as seguintes informações:

- UF \(UF do destinatário\);
- Nome do arquivo mestre que será gerado pelo programa extrator do Conv\.115 \(será o mesmo nome do arquivo mestre  “normal”, trocando apenas as duas primeiras posições para a sigla da UF\);
- Volume do arquivo; 
- Código de Autenticação Digital – deixar em branco \(será preenchido somente na rotina de importação dos hash code\); 

     Estas informações serão utilizadas na rotina de importação dos hash\-code, para possibilitar que sejam importados também os códigos de autenticação dos   

      arquivos que serão gerados pelo programa “extrator” do Convênio ICMS 115\. 

__Alteração da OS3330\-A:__

    Na tela de Geração Convênio 115, foi retirado o parâmetro Estabelecimento e acrescentado o Parâmetro “UF”\. Quando o usuário optar pelo estado de sua escolha no parâmetro "UF”, a rotina deverá fazer um filtro na tabela ESTABELECIMENTO onde COD\_ESTADO seja igual ao COD\_ESTADO da tabela ESTADO e pertençam a UF selecionada\. 

Os estabelecimentos que passarem pelo critério de seleção do parâmetro, deverão ser apresentados no quadro “Estabelecimento” em forma de lista com o flag para o usuário selecionar apenas os que participarão da única geração\.

Os estabelecimentos selecionados serão executados todos juntos, sendo possível porque compartilham de um mesmo controle de numeração de notas fiscais por série distintas\.

__Alteração da OS3974 \(Abr/2013\):__

    A geração do arquivo foi alterada para gerar no arquivo dos itens, os  “itens adicionais”   referentes aos dados de cofaturamento armazenados na tabela SAFX213\. O preenchimento destes “itens adicionais” segue as orientações da Portaria CAT 24/2013, e está descrito na regra __RN16__\.

__OS3330\-A/ __

__OS3851 / __

__OS3974__

__RN01__

Recuperar o somatório do campo 18 \(valor de descontos \) da SAFX43, dentro do período e informar este somatório no campo 28 – Somatório de descontos do relatório de conferência de arquivo eletrônico da geração do meio magnético do Convênio 115\.

__OS2609\-D__

__RN02__

Excluir o label “ Desconsiderar valor de Descontos no cálculo do valor contábil” da tela de geração do mapa resumo\.

__OS2609\-D__

__RN03__

A partir desta OS, o label “Desconsiderar valor de Descontos no cálculo do valor contábil” , deverá ser excluídos conforme a regra RN02, de forma que não serão exibidos na tela de geração do meio magnético convênio 115\.

__OS2609\-D__

__RN04__

__\[EXCLUIDA – OS4281\]: __A regra de negócio que compõe a quebra do arquivo pela quantidade de documento fiscal está no arquivo MTZ\_ICMS\_Convenio\_115\_ Quantidade\_Documentos\_Fiscais\_por\_Volume\.docx

__Cálculo da quantidade de documentos fiscais por volume \(arquivo\)__:

a\-\) Contar o total de notas existentes na x42 para aquela empresa, estabelecimento e período \(__filtrando pela data fiscal__\) onde o __\[modelo da NF for__ __diferente de__ __‘06’\]__ __OU__ __\[o modelo for__ __igual a__ __‘06’__ __E__ __a UF do estabelecimento for diferente de ‘SP’\]__;

b\-\) Contar o total de notas existentes na x42 para aquela empresa, estabelecimento e período \(__filtrando pela data de vencimento__\) onde o __\[modelo da NF for igual a ‘06’ E o código do estado do estabelecimento for igual a ‘SP’\]__\.

O total de NF’s do período \(t\) será = \(a\+b\), então, o arquivo será quebrado em volumes de até cem mil notas caso o total de NF’s \(t\) seja de até 1 milhão de registros, ou, será quebrado em volumes de até 1 milhão de notas caso o total de NF’s \(t\) seja maior que 1 milhão de registros\.

__\[Alteração da OS3694\-A1\]:__

Ou seja, Quando a quantidade de NFs do período for menor que um milhão, quebra\-se em arquivos de cem mil\. Quando for maior ou igual a um milhão, serão realizadas quebras de um em um milhão, sendo que se houver um saldo de NFs menores que um milhão, este saldo será gerado em um único arquivo\.

Exemplo: se tenho uma quantidade de 5\.344\.000 NFs, serão gerados 6 arquivos:

\- 5 arquivos contendo um milhão de NFs

\- 1 arquivo contendo 344\.000 mil notas

\[__Alterada – CH29604\_2012__\]

Quando a UF do estabelecimento for igual a MG, o total de NF’s do período \(t\) será = \(a\+b\), então, o arquivo será quebrado em volumes de até 1 milhão de notas caso o total de NF’s \(t\)\.

__\[Alteração da OS3330\-A\]__:

Quando o usuário optar pela geração única, ou seja, escolhendo um ou mais estabelecimentos o processo de geração, o cálculo não será afetado\. A rotina deve continuar com as regras atuais\.

__CH76590 /__

__OS3330\-A__

__CH29604/2012__

__OS3694\-A1__

__RN05__

__\[Alteração da OS3424\-D\]:__

__Módulo:__ Estadual >> ICMS 

__Menu:__ DATA MART __>>__ __Convênio ICMS 115 >> Geração do Meio Magnético__

Em São Paulo ao contrário de outros estados, a apuração do ICMS dos documentos fiscais de Energia Elétrica é realizada pela Data de Vencimento das Faturas, ao contrário de outros documentos fiscais cuja apuração é realizada pela Data Fiscal ou Data de Emissão/Data de Entrada\-Saída\. Em algumas situações esses documentos fiscais de Energia Elétrica são cancelados no mês posterior ao mês de vencimento fazendo com que os mesmos sejam gerados como cancelados e não com status de documento normal, visto que essa era a situação na época do vencimento\. 

Com a publicação do Decreto 57\.177/2011, a apuração, a partir de 01/2012, passou ter como base a data de emissão/ fiscal da nota fiscal\.

Para que essa situação não ocorra novamente, os Documentos Fiscais de Energia Elétrica que estejam cancelados deverão ser recuperados e gerados no meio magnético __Convênio ICMS 115/03__ e Geração Automática dos Mapas Resumo da seguinte forma:

__\[ALTERADA – CH15005\_2016\]__

Quando o campo 13 \- COD\_MODELO \(SAFX42\) = ‘6’, UF Estabelecimento = SP e RS, UF Destinatário = SP e RS, verificar:

\- Se campo 21 – SITUACAO \(SAFX42\) = ‘S’;

\- Se campo 03 \- DAT\_FISCAL \(SAFX42\) tiver data até 31\.12\.2011, a escrituração deve ser pela data de vencimento, ou seja, pelo campo 32 da SAFX42;

\- Se campo 03 – DAT\_FISCAL \(SAFX42\) tiver data a partir de 01\.01\.2012, a escrituração deve ser pelo campo 03 \(SAFX42\);

\- Mês/Ano de Cancelamento é maior que o Mês/Ano de Emissão \(campo 56 > 03 da SAFX42\)\.

__Obs\.:__  A UF Destinatário deve = SP em virtude de negócios, pois o estabelecimento é situado em SP, porém comercializa energia elétrica para outra UF, como por exemplo as cidades que se localizam em divisas\.

__Obs\.:__ A regra acima deve ser válida para reprocessamento\.

- Estabelecimento do estado de SP – São Paulo
- NF cujo modelo seja 06 – Energia Elétrica \(campo 13 da SAFX42\)
- NF com situação Cancelada \(campo 30 da SAFX42\)
- Mês/Ano de Cancelamento é maior que o Mês/Ano de Vencimento \(campo 56 > 32 da SAFX42\)

Caso essas premissas sejam atendidas, as informações deverão ser gravadas da seguinte forma:

- Gravar “N” no campo 19 – Situação do Documento \(posições 196\-196\) do arquivo tipo MESTRE DE DOCUMENTO FISCAL\.
- Gravar “N” no campo 26 – Situação do Documento \(posições 213\-213\) do arquivo tipo ITEM DE DOCUMENTO FISCAL\.

__\[Alteração da OS3330\-A\]__:

Quando o usuário optar pela geração única, ou seja, escolhendo um ou mais estabelecimentos o processo de geração, o cálculo não será afetado\. A rotina deve continuar com as regras atuais\.

__OS2768\-M/ OS3330\-A/ OS3424\-D__

__CH15005\_2016__

__RN06__

Como esses documentos fiscais que outrora eram gerados com o status “Cancelado” e agora são gerados com status “Normal”, os mesmos deverão fazer parte dos totalizadores dos documentos normais do arquivo tipo CONTROLE E IDENTIFICAÇÃO do Convênio ICMS 115/03\. Para tal efeito, os seguintes campos deverão considerar esses documentos:

- Campo 13 – Quantidade de registros do arquivo Mestre do Documento Fiscal \(posições 307\-313\) do arquivo tipo CONTROLE E IDENTIFICAÇÃO\.
- Campo 27 \- Quantidade de registros do arquivo Item de Documento Fiscal \(posições 473\-481\) do arquivo tipo CONTROLE E IDENTIFICAÇÃO\.

__OS2768\-M__

__RN07__

Os valores dos documentos com situação “Normal” deverão ser sumarizados no arquivo CONTROLE E IDENTIFICAÇÃO\. Os campos a serem considerados são:

- Campo 19 – Valor Total
- Campo 20 – BC ICMS
- Campo 21 – ICMS
- Campo 22 – Operações Isentas ou Não Tributadas
- Campo 23 – Outros valores que não compõe a BC do ICMS
- Campo 33 – Total
- Campo 34 – Descontos
- Campo 35 – Acréscimos e Despesas Acessórias
- Campo 36 – BC ICMS
- Campo 37 – ICMS
- Campo 38 – Operações Isentas ou Não Tributadas
- Campo 39 – Outros valores que não compõe a BC do ICMS

__OS2768\-M__

__RN08__

Campo “__23 \- Brancos – Reservado para uso futuro__” \(Arquivo Mestre de Documentos Fiscais\):

A partir da OS3295 este campo passou a ser preenchido da seguinte forma, conforme as orientações do Art\. 2 da Portaria CAT 187/2010:

\(até então o campo não era utilizado, e conforme manual do Convênio 115 era preenchido com brancos\)

__Se__ modelo do documento fiscal  = 06 \(Prestação de Serviços de Energia Elétrica\):

   Quando o documento fiscal tiver item ou itens c/o novo campo “96\-Tipo de Decisão Judicial” = “1”; à gravar “__ES__”

   Quando o documento fiscal tiver item ou itens c/o novo campo “96\-Tipo de Decisão Judicial” = “2” à gravar “__BC__”

   Quando o documento fiscal tiver item ou itens c/o novo campo “96\-Tipo de Decisão Judicial” = “3” à gravar “__NI__”

   Não ocorrendo nenhuma das situações acima à gravar brancos

Senão

   Preencher o campo com brancos\.

Obs: O modelo da nota fiscal deve ser verificado através do campo “13 \- Modelo de Documento” da SAFX42\.

__OS3295__

__RN09__

__\[EXCLUIDA – OS4281\]: __A regra de negócio que compõe a quebra do arquivo pela quantidade de documento fiscal está no arquivo MTZ\_ICMS\_Convenio\_115\_ Quantidade\_Documentos\_Fiscais\_por\_Volume\.docx

__Regra para Geração do Meio Magnético:__

__Módulo:__ Estadual → ICMS

__Menu:__ Datamart → Geração ICMS 115 → Geração do Meio Magnético

Na geração do arquivo de meio magnético deve ser respeitada a seguinte regra:

\- Deve ser um conjunto de arquivos, distinto para cada modelo e série do documento fiscal;

\- O conjunto de arquivo deve ser dividido em volumes, sempre que a quantidade de documentos fiscais alcançar a regra abaixo:

- Para 100 mil documentos fiscais, quando for contribuinte com volume mensal de emissão até 1 milhão de documentos fiscais;
- Para 1 milhão de documentos fiscais, quando o contribuinte tiver volume mensal de emissão superior a 1 milhão de documentos fiscais\.

__CH111412__

__RN10__

__Regra para Geração do Meio Magnético:__

As inclusões a seguir, deverão ser efetuadas quando o campo Mês/Ano de Apuração da tela de Geração Meio Magnético do Convênio 115 esteja preenchido com o período a partir de __07/2012__\.

__Registro MESTRE DE DOCUMENTO FISCAL__

Campo 22 \- Número do terminal telefônico ou Número da conta de consumo

__Nome: __Número do terminal telefônico ou Número da conta de consumo

__Tamanho: 12__

__Posição: __210 \- 221

__Tipo: __Alfanumérico

__Regra de Negócio:__ Informar a localidade de registro e o número do telefone no formato “LLNNNNNNNN”, quando:

\- Nota Fiscal de Serviço de Comunicação/Telecom \(modelo 21 e 22\)

- “LL” são os 2 dígitos do DDD \(recuperar o campo 22 da SAFX04\) concatenado com “NNNNNNNN” são os 8 dígitos do terminal/aparelho telefônico \(recuperar o campo 23 da SAFX04\)\. Quando o número de identificação do terminal com 9 \(nove\) dígitos, utilizar o formato “LLNNNNNNNNN” e utilizar a mesma recuperação\.
- Quando o campo 22 DDD, for maior que 2 dígitos deverá ser desprezado os zeros a esquerda e caso o conteúdo do campo for maior 2 dígitos , emitir a mensagem de erro no log: “*O conteúdo da localidade \(DDD\) ultrapassa o valor permitido no registro\. Deverá ser revisado*”\. 
- O campo 23 Telefone, deverá ser aceito com 8 dígitos ou 9 dígitos, desprezar o restante do campo caso ultrapasse esta quantidade\. Caractere especial \(traço\), também deverá ser desprezado no campo\.

\- Nota Fiscal/Conta de Energia Elétrica \(modelo 06\) e \(modelo 01\)

- Recuperar o número da conta de consumo, conteúdo do campo 59 da SAFX42\.

__Orientações de Preenchimento do campo, conforme Portaria CAT 79/12 – a partir do Convênio ICMS 07/2012:__

- Quando não houver informação no campo correspondente:

\(Completar as posições com espaços\.\)

- Quando houver telefone com Localidade \+ 8 dígitos \(10 posições\):

D

D

1

2

3

4

5

6

7

8

__OS3597/ CH7733\_2012__

- Quando houver telefone com Localidade \+ 9 dígitos \(11 posições\) :

D

D

1

2

3

4

5

6

7

8

9

\(o preenchimento dos campos deve ser iniciado da esquerda para a direita, e preenchido com espaços para os caracteres não preenchidos na tabela\)

__Tratamento para as versões anteriores ao Convênio  ICMS 07 de 2012:__

Informar a localidade de registro e o número do telefone no formato “LLNNNNNNNN”, quando:

\- Nota Fiscal de Serviço de Comunicação/Telecom \(modelo 21 e 22\)

- “LL” são os 2 dígitos do DDD \(recuperar o campo 22 da SAFX04\) concatenado com “NNNNNNNN” são os 8 dígitos do terminal/aparelho telefônico \(recuperar o campo 23 da SAFX04\)\. 
- Quando o campo 22 DDD, for maior que 2 dígitos deverá ser desprezado os zeros a esquerda e caso o conteúdo do campo for maior 2 dígitos , emitir a mensagem de erro no log: “*O conteúdo da localidade \(DDD\) ultrapassa o valor permitido no registro\. Deverá ser revisado*”\. 
- O campo 23 Telefone, deverá ser aceito com 8 dígitos, desprezar o restante do campo a esquerda caso ultrapasse esta quantidade\. Caractere especial \(traço\), também deverá ser desprezado no campo\.

\- Nota Fiscal/Conta de Energia Elétrica \(modelo 06\) e \(modelo 01\)

- Recuperar o número da conta de consumo, conteúdo do campo 59 da SAFX42\.

__Exemplo da Formatação:__

Quando não houver informação no campo correspondente:

\(Completar as posições com espaços\.\)

Quando houver telefone com Localidade \+ 8 dígitos \(10 posições\):

D

D

1

2

3

4

5

6

7

8

__RN11__

__Regra para Geração do Meio Magnético:__

__Registro MESTRE DE DOCUMENTO FISCAL__

Campo 23 – Brancos – reservado para uso futuro

__Nome: __Brancos

__Tamanho: 05__

__Posição: __222 \- 226

__Tipo: __Alfanumérico

__Regra de Negócio: __Preencher com brancos o conteúdo deste campo\.

__OS3597__

__RN12__

__Regra para Geração do Meio Magnético:__

__Registro DADOS CADASTRAIS DO DESTINATÁRIO DO DOCUMENTO FISCAL__

Campo 11 – Telefone de Contato

__Nome: __Número do telefone de contato

__Tamanho: 12__

__Posição: __184 \- 195

__Tipo: __Numérico

__Regra de Negócio:__ Informar o “LL” são os 2 dígitos do DDD \(recuperar o campo 22 da SAFX04\) concatenado com “NNNNNNNN” são os 8 dígitos do terminal/aparelho telefônico \(recuperar o campo 23 da SAFX04\)\. Quando o número de identificação do terminal com 9 \(nove\) dígitos, utilizar o formato “LLNNNNNNNNN” e utilizar a mesma recuperação\. 

- Quando o campo 22 DDD, for maior que 2 dígitos deverá ser desprezado os zeros a esquerda e caso o conteúdo do campo for maior 2 dígitos , emitir a mensagem de erro no log: “*O conteúdo da localidade \(DDD\) ultrapassa o valor permitido no registro\. Deverá ser revisado*”\. 
- O campo 23 Telefone, deverá ser aceito com 8 dígitos ou 9 dígitos, desprezar o restante do campo caso ultrapasse esta quantidade\. Caractere especial \(traço\), também deverá ser desprezado no campo\.

__Orientações de Preenchimento do campo, conforme Portaria CAT 79/12 – a partir do Convênio ICMS 07/2012:__

- Quando não houver informação no campo correspondente:

0

0

0

0

0

0

0

0

0

0

0

0

\(Completar as posições com zeros\.\)

- Quando houver telefone com Localidade \+ 8 dígitos \(10 posições\):

0

0

D

D

1

2

3

4

5

6

7

8

- Quando houver telefone com Localidade \+ 9 dígitos \(11 posições\) :

0

D

D

1

2

3

4

5

6

7

8

9

\(o preenchimento dos campos deve ser iniciado da direita para a esquerda, e preenchido com zeros para os caracteres não preenchidos na tabela\)

__OS3597/ CH7733\_2012__

__Tratamento para as versões anteriores ao Convênio  ICMS 07 de 2012:__

Informar o “LL” são os 2 dígitos do DDD \(recuperar o campo 22 da SAFX04\) concatenado com “NNNNNNNN” são os 8 dígitos do terminal/aparelho telefônico \(recuperar o campo 23 da SAFX04\)\. 

- Quando o campo 22 DDD, for maior que 2 dígitos deverá ser desprezado os zeros a esquerda e caso o conteúdo do campo for maior 2 dígitos , emitir a mensagem de erro no log: “*O conteúdo da localidade \(DDD\) ultrapassa o valor permitido no registro\. Deverá ser revisado*”\. 
- O campo 23 Telefone, deverá ser aceito com 8 dígitos, desprezar o restante do campo a esquerda caso ultrapasse esta quantidade\. Caractere especial \(traço\), também deverá ser desprezado no campo\.

__Exemplo da Formatação:__

Quando não houver informação no campo correspondente:

0

0

0

0

0

0

0

0

0

0

\(Completar as posições com zeros\.\)

Quando houver telefone com Localidade \+ 8 dígitos \(10 posições\):

D

D

1

2

3

4

5

6

7

8

__RN13__

__Regra para Geração do Meio Magnético:__

__Registro DADOS CADASTRAIS DO DESTINATÁRIO DO DOCUMENTO FISCAL__

Campo 13 \- Número do terminal telefônico ou Número da conta de consumo

__Nome: __Número do terminal telefônico ou Número da conta de consumo

__Tamanho: 12__

__Posição: __208 \- 219

__Tipo: __Alfanumérico

__Regra de Negócio:__ Informar a localidade de registro e o número do telefone no formato “LLNNNNNNNN”, quando:

\- Nota Fiscal de Serviço de Comunicação/Telecom \(modelo 21 e 22\)

- “LL” são os 2 dígitos do DDD \(recuperar o campo 22 da SAFX04\) concatenado com “NNNNNNNN” são os 8 dígitos do terminal/aparelho telefônico \(recuperar o campo 23 da SAFX04\)\. Quando o número de identificação do terminal com 9 \(nove\) dígitos, utilizar o formato “LLNNNNNNNNN” e utilizar a mesma recuperação\.
- Quando o campo 22 DDD, for maior que 2 dígitos deverá ser desprezado os zeros a esquerda e caso o conteúdo do campo for maior 2 dígitos , emitir a mensagem de erro no log: “*O conteúdo da localidade \(DDD\) ultrapassa o valor permitido no registro\. Deverá ser revisado*”\. 
- O campo 23 Telefone, deverá ser aceito com 8 dígitos ou 9 dígitos, desprezar o restante do campo caso ultrapasse esta quantidade\. Caractere especial \(traço\), também deverá ser desprezado no campo\.

\- Nota Fiscal/Conta de Energia Elétrica \(modelo 06\) e \(modelo 01\)

- Recuperar o número da conta de consumo, conteúdo do campo 59 da SAFX42\.

__Orientações de Preenchimento do campo, conforme Portaria CAT 79/12 – a partir do Convênio ICMS 07/2012:__

- Quando não houver informação no campo correspondente:

\(Completar as posições com espaços\.\)

- Quando houver telefone com Localidade \+ 8 dígitos \(10 posições\):

D

D

1

2

3

4

5

6

7

8

- Quando houver telefone com Localidade \+ 9 dígitos \(11 posições\) :

D

D

1

2

3

4

5

6

7

8

9

\(o preenchimento dos campos deve ser iniciado da esquerda para a direita, e preenchido com espaços para os caracteres não preenchidos na tabela\)

\- Demais modelos, deixar em branco\.

\- Completar o campo com brancos a direita\.

__OS3597/ CH7733\-2012__

__Tratamento para as versões anteriores ao Convênio  ICMS 07 de 2012:__

Informar a localidade de registro e o número do telefone no formato “LLNNNNNNNN”, quando:

\- Nota Fiscal de Serviço de Comunicação/Telecom \(modelo 21 e 22\)

- “LL” são os 2 dígitos do DDD \(recuperar o campo 22 da SAFX04\) concatenado com “NNNNNNNN” são os 8 dígitos do terminal/aparelho telefônico \(recuperar o campo 23 da SAFX04\)\. 
- Quando o campo 22 DDD, for maior que 2 dígitos deverá ser desprezado os zeros a esquerda e caso o conteúdo do campo for maior 2 dígitos , emitir a mensagem de erro no log: “*O conteúdo da localidade \(DDD\) ultrapassa o valor permitido no registro\. Deverá ser revisado*”\. 
- O campo 23 Telefone, deverá ser aceito com 8 dígitos, desprezar o restante do campo a esquerda caso ultrapasse esta quantidade\. Caractere especial \(traço\), também deverá ser desprezado no campo\.

\- Nota Fiscal/Conta de Energia Elétrica \(modelo 06\) e \(modelo 01\)

- Recuperar o número da conta de consumo, conteúdo do campo 59 da SAFX42\.

__Exemplo da Formatação:__

Quando não houver informação no campo correspondente:

\(Completar as posições com espaços\.\)

Quando houver telefone com Localidade \+ 8 dígitos \(10 posições\):

D

D

1

2

3

4

5

6

7

8

__RN14__

__Regra para inclusão do novo parâmetro Geração p/ Empresa com Insc\. Estadual Única:__

Neste item o usuário poderá os arquivos magnéticos para o Convênio 115 por Inscrição estadual Única\. 

Se o novo parâmetro __Geração p/ Empresa com Insc\. Estadual Única__ estiver __*desmarcado*:__

Neste caso, mostrar todos os Estabelecimentos da Empresa \(conforme funcionamento atual\);

Se o novo parâmetro __Geração p/ Empresa com Insc\. Estadual Única __estiver__ *marcado*:__

Neste caso, mostrar apenas os Estabelecimentos parametrizados como *centralizadores* na parametrização dos Estabelecimentos com Inscrição Estadual Única do módulo de Controle das Obrigações Estaduais\.

__OS3330\-A1__

__RN15__

__Regra para o novo parâmetro Geração p/ Empresa com Insc\. Estadual Única:__

A geração do arquivo foi alterada para considerar o novo parâmetro incluído na tela\. O tratamento da inscrição estadual única será o mesmo já existente no Mastersaf para a emissão dos livros fiscais, da seguinte forma:

- Ao utilizar qualquer parametrização cujo cadastro seja por estabelecimento, deve\-se utilizar a parametrização feita em nome do estabelecimento centralizador;
- Além dos documentos fiscais do estabelecimento da geração, que é o estabelecimento centralizador, deverão ser recuperados também os documentos dos estabelecimentos centralizados\. Assim, a regra é considerar os documentos fiscais de todos os estabelecimentos envolvidos na centralização, lembrando que a parametrização dos estabelecimentos Centralizadores x Centralizados fica no módulo Controle das Obrigações Estaduais, no item “Obrigações à Empresas/Estabelecimentos com Inscrição Estadual Única”;
- Na falta do preenchimento de campo obrigatório, deve ser informado no log a seguinte mensagem:

“NOME DO CAMPO” deve ser preenchido\. Empresa XXX  Estabelecimento XXXX Data Fiscal XXXXXXXX Número / Série XXXXXXXX\.

Sendo que o estabelecimento deve ser o centralizado, caso a nota pertença a ele\.

__OS3330\-A1__

__RN16__

__Regra para geração dos itens adicionais no arquivo dos itens:__

Após a gravação dos itens do documento fiscal no arquivo dos itens, serão gerados os “itens adicionais” de acordo com as regras definidas a seguir:

Origem dos dados à SAFX213

Para cada documento fiscal \(SAFX42\) gravado no arquivo, os dados da SAFX213 serão obtidos através dos campos chave do documento fiscal, da seguinte forma:

          SAFX213                                        SAFX42

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-              \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

Código da Empresa                          = Código da Empresa

Código do Estabelecimento               = Código do Estabelecimento

Data da Emissão/Escrita Fiscal         = Data da Emissão/Escrita Fiscal

Indicador e Código da Pessoa Fis/Jur = Indicador e Código da Pessoa Fis/Jur

Número do Documento Fiscal             = Número do Documento Fiscal

Série do Documento Fiscal                = Série do Documento Fiscal

Subsérie do Documento Fiscal           = Subsérie do Documento Fiscal

Caso existam dados na SAFX213 para o documento fiscal em questão, será gravado um item adicional para cada registro recuperado da SAFX213\.

Os dados a serem gravados nestes itens segue a especificação do documento “DEPARA\_Convenio115” \(ver “Itens Adicionais”\)\.

Observar que o campo “13\-Descrição do Serviço ou Fornecimento” será gravado com a concatenação das informações da SAFX213 \(como consta no De\-Para\)\. Ao concatenar as informações, os campos serão alinhados da seguinte forma:

__Posição 01 a 02__ à código CSP                                                      \(alinhar a direita e preencher as posições não significativas com brancos\)

__Posição 03 __à branco

__Posição 04 a 13__ à nome da prestadora                                         \(alinhar a esquerda e preencher as posições não significativas com brancos\)

__Posição 14__ à branco 

__Posição 15 a 17__ à série do documento do cofaturamento             \(alinhar a esquerda e preencher as posições não significativas com brancos\)

__Posição 18__ à branco 

__Posição 19 a 27__ à número do documento do cofaturamento          \(alinhar a direita e preencher as posições não significativas com brancos\)

*\(Observar que o campo “10\-Número do Documento Fiscal do Cofaturamento” da SAFX213 foi criado como A/012 apenas por uma questão de padrão, mas na verdade a informação deve ser tratada como um campo numérico de 9 posições, que ocupará da posição 19 a 27\) *

__Posição 28__ à branco 

__Posição 29 a 40__ à valor total do documento do cofaturamento     \(alinhar a direita e preencher as posições não significativas com brancos\)

__OS3974__

__RN17__

Campo__ “13\-Descrição do serviço ou fornecimento”__ do Arquivo dos Itens:

__Alteração da OS4144 \(Ago/2013\):__

Na OS4144 foi criado o seguinte parâmetro na tela da geração:

Preenchimento da descrição do arquivo dos itens: \( x \) Descrição da Tabela de Produtos \(SAFX2013\)

                                                                      \(   \) Descrição da Tabela dos Itens de Utilities \(SAFX43\)

As opções são alternativas, assim, o usuário só poderá optar por uma delas\.

Na abertura da tela a opção “*Descrição da Tabela de Produtos \(SAFX2013\)*” aparecerá sempre marcada por default, mantendo assim o funcionamento original da geração\. 

De acordo com a opção do usuário, o preenchimento do campo “13\-Descrição do serviço ou fornecimento” do arquivo dos itens será feito da seguinte forma:

\- Opção “__Descrição da Tabela de Produtos \(SAFX2013\)__” à Neste caso o campo será preenchido com a descrição do produto da SAFX2013,

   conforme o procedimento original;

\- Opção “__Descrição da Tabela dos Itens de Utilities \(SAFX43\)__“ à Neste caso o campo será preenchido com o conteúdo do campo “*30\-Descrição*

*   do serviço ou fornecimento*” do item \(SAFX43\), mas *apenas* quando este campo estiver preenchido\. Caso contrário, será utilizada a descrição do

   produto da SAFX2013;

Quando o conteúdo a ser gravado ultrapassar o tamanho do campo no layout, a informação será truncada \(conforme já era feito antes da criação do parâmetro\)\.

__ Importante__ à __Esta regra não se aplica às seguintes situações__:

     \- Geração dos itens denominados “Itens Adicionais” \. Trata\-se de itens gerados a partir dos dados de cofaturamento da SAFX213, ou seja, estes

       itens __não__ são gerados a partir da SAFX43 \(conforme definido na RN16\);

     \- Geração dos itens das NF’s de serviços pré\-pagos, identificados pelo campo “59\-Indicador de Serviço Pré\-Pago” da SAFX43\. Neste caso, a

       descrição é sempre gerada com informações sobre a ativação do crédito \(campos 60, 61 e 62 da SAFX43\);

__OS4144__

__RN18 \- Utilização do parâmetro “Gravar os itens negativos no arquivo \(itens da SAFX431\)”__

__\(parâmetro criado na OS4413\-A\) __

Este parâmetro é utilizado na gravação do Arquivo dos Itens, da seguinte forma:

__Parâmetro desmarcado__:     \(apenas itens da __SAFX43__\)

     Neste caso, o Arquivo dos Itens será gerado apenas com os itens da SAFX43, conforme o funcionamento original da geração;

 

__Parâmetro marcado__:           \(itens da __SAFX43__ e __SAFX431__\)

     Neste caso, o Arquivo dos Itens será gerado com os itens da __SAFX43__, e também os itens da __SAFX431__\. Além de considerar os itens da SAFX431, também existem algumas regras diferentes no tratamento dos itens da SAFX43\.

\[__MFS\-4969__\] Quando for selecionada a opção de Formato do Convênio ICMS igual a “Convênio ICMS 60” na tela de Geração do Meio Magnético, assumir na geração a regra do parâmetro “Gravar os itens negativos no arquivo \(itens da SAFX431\)” marcado\. Para este Convênio esta opção será padrão\.

    

     A seguir serão descritas as regras de gravação dos itens considerando as duas tabelas \(__SAFX43__ e __SAFX431__\):	

	

            __Em relação à gravação dos itens da SAFX43__

         \[__MFS24491\] Tratamento do parâmetro “Desconsiderar Itens de Desconto \(SAFX43\)” \(regra criada para atender a CPFL\)__

          Quando o parâmetro estiver marcado, os itens da SAFX43 que tenham o campo Adição/Desconto \(campo 20\) igual a “D” \(Desconto\) não devem ser considerados na geração do arquivo\.

- O campo “11\-Item” é gravado com a informação do campo “110\-Número do Item Real”, da seguinte forma:

                   Se campo “110\-Número do Item Real” não preenchido à grava o conteúdo do campo “09\-Item Nota Fiscal”;

                   Senão à grava o conteúdo do campo “110\-Número do Item Real”;

- Para cada item da SAFX43 a ser gravado, será verificado se ele é o resultado de uma consolidação de itens da nota original\. Para isso, será verificada a existência de dados na SAFX431 para o documento fiscal em questão\. Caso exista, será verificado se algum dos itens da SAFX431 “aponta” para o item da SAFX43 em questão, através do campo “11\-Número do Item da Consolidação”\. Este campo indica que o item da SAFX431 está associado ao item da SAFX43\.    

                    Observar que poderão existir ‘n’ registros da SAFX431 associados a um item da SAFX43;

                    Caso não exista nenhum item associado à então o item da SAFX43 será gravado no arquivo normalmente, conforme o DE\-PARA e regras já existentes;

                    Caso existam itens associados à neste caso, o item da SAFX43 terá alteração no conteúdo de alguns valores a serem gravados\. O objetivo é estornar o valor dos itens associados do valor do item principal \(item da SAFX43\)\. Este procedimento é necessário, uma vez que os itens da SAFX431 também serão gravados no arquivo\.

                    Os valores a serem calculados são os seguintes:

                    \(observar que os itens da SAFX431 que entram neste cálculo são apenas os itens associados ao item em questão da SAFX43, conforme a verificação descrita acima\!\!\!\)

__Campo do Arquivo de Itens:__

__Valor a ser gravado:__

18\-Total 

Valor do Serviço da SAFX43 – Valor Serviço dos itens da SAFX431 com campo “10\-Ind Dedução” = “N”

\(para o valor do serviço será “estornado” apenas os itens da SAFX431 que não são itens negativos\)

 \(isso porque o valor dos negativos não é deduzido do valor do serviço na carga da SAFX43, pois ele é carregado p/o campo do Desconto\) 

19\-Desconto

Neste caso este campo será preenchido com zeros

 \(como os itens negativos da SAFX431 serão gravados no arquivo, o campo desconto não será utilizado\)

21\-BC ICMS

Base Tributada da SAFX43 \+ Base Tributada dos itens da SAFX431 com campo “10\-Ind Dedução” = “S”

                                             \- Base Tributada dos itens da SAFX431 com campo “10\-Ind Dedução” = “N”     

22\-ICMS

Valor ICMS da SAFX43 \+ Valor ICMS dos itens da SAFX431 com campo “10\-Ind Dedução” = “S”

                                       \- Valor ICMS dos itens da SAFX431 com campo “10\-Ind Dedução” = “N”  

23\-Oper\.Isentas/Não Trib

\(Base Isenta \+ Base Redução\) da SAFX43 \+ \(Base Isenta \+ Base Redução\) dos itens da SAFX431 com campo “10\-Ind Dedução” = “S”

                                                                      \- \(Base Isenta \+ Base Redução\) dos itens da SAFX431 com campo “10\-Ind Dedução” = “N”

24\-Outros Valores

Base Outras da SAFX43 \+ Base Outras dos itens da SAFX431 com campo “10\-Ind Dedução” = “S”

                                         \- Base Outras dos itens da SAFX431 com campo “10\-Ind Dedução” = “N”

__\[ALTERADA – MFS\-19361 \(regra criada para atender a Nextel\)\]__

Base Outras da SAFX43 \+ Base Outras dos itens da SAFX43 com campo “Adição/Desconto” = “D” e sinal negativo

                                         \- Base Outras dos itens da SAFX43 com campo “Adição/Desconto” = “A” ou “D” sem sinal negativo

32\-PIS/PASEP

\(MFS\-4969\)

Este campo será gerado somente quando, na tela de geração, for selecionado o Formato “Convênio ICMS 60”\.

Valor do PIS da SAFX43 \+ Valor do PIS dos itens da SAFX431 com campo “10\-Ind Dedução” = “S”

                                         \- Valor do PIS dos itens da SAFX431 com campo “10\-Ind Dedução” = “N”

34\-COFINS

\(MFS\-4969\)

Este campo será gerado somente quando, na tela de geração, for selecionado o Formato “Convênio ICMS 60”\.

Valor da COFINS da SAFX43 \+ Valor da COFINS dos itens da SAFX431 com campo “10\-Ind Dedução” = “S”

                                                 \- Valor da COFINS dos itens da SAFX431 com campo “10\-Ind Dedução” = “N”

                          __OBS__: O cálculo descrito acima considera o valor absoluto dos campos \(sem o sinal\)\. Observar que quando o tem da SAFX431 for um item de dedução \(Indicador de dedução = “S”\), estes valores estarão negativos\.

            Sobre a totalização dos valores no Arquivo Mestre à No caso destes itens que terão seus valores calculados, observar que os valores referentes ao item a serem totalizados no Arquivo Mestre \(campos 15, 16, 17 e 18\), serão os valores que de fato forma gravados no arquivo dos itens, ou seja, os valores que foram calculados\.

__            Em relação à gravação dos itens da SAFX431:__

            Além de gravar os itens da SAFX43, a geração também irá verificar se existem itens na SAFX431 referentes ao documento fiscal em questão\. Caso existam, todos os itens recuperados serão gravados no

            Arquivo de Itens do Convênio 115\.

            Para verificar o preenchimento dos campos, verificar o documento “__*DEPARA\_Convenio115*__”, no item “__*Arquivo de Itens de Documento Fiscal \(itens originados da SAFX431\)*__”\.

            Importante: os valores de serviço, ICMS, base ICMS, base isenta e base outras dos itens de dedução \(campo “10\-Ind Dedução” = “S”\) serão gravados com sinal negativo, como consta no DEPARA\.

__\[ALTERAÇÃO\- MFS91802\]__ Readequação na geração para considerar o parâmetro “Desconsiderar Itens de Desconto \(SAFX431\) p/ Arquivo Mestre”

Este parâmetro será utilizado na gravação do Arquivo Mestre, da seguinte forma:

__Parâmetro desmarcado:__ Se o parâmetro “Desconsiderar Itens de Desconto \(SAFX431\) p/ Arquivo Mestre” estiver *desmarcado* o sistema deverá seguir a regra original e gerar as informações, conforme regra abaixo:  

Sobre a totalização dos valores no Arquivo Mestre à Ao gravar cada item da SAFX431, os seus valores também deverão ser totalizados para os campos 15, 16, 17 e 18  do Arquivo Mestre, da seguinte forma:

                            \- Para os itens de dedução \(campo 10\-Indicador de Dedução = ”S”\) à o valor será subtraído para compor os totais do documento;

                            \- Para os itens que não são dedução \(campo 10\-Indicador de Dedução = “N”\) à o valor será somado para compor os totais do documento;

__OBS__: A regra descrita acima considera o valor absoluto dos campos \(sem o sinal\)\. Observar que quando o tem da SAFX431 for um item de dedução \(Indicador de dedução = “S”\), os valores estarão negativos\.

__Parâmetro marcado:__ Se o parâmetro “Desconsiderar Itens de Desconto \(SAFX431\) p/ Arquivo Mestre” estiver *marcado* o sistema deverá desconsiderar os *itens de desconto* da SAFX431, seguindo a regra abaixo:

            Sobre a totalização dos valores no Arquivo Mestre à Ao gravar cada item da SAFX431, os seus valores deverão ser totalizados para os campos 15, 16, 17 e 18  do Arquivo Mestre, da seguinte forma:

                            \- Para os itens de dedução \(campo 10\-Indicador de Dedução = ”S”\) à o valor deverá ser __*desconsiderado*__ para compor os totais do documento;

                            \- Para os itens que não são dedução \(campo 10\-Indicador de Dedução = “N”\) à o valor será somado para compor os totais do documento;

__                           OBS__: A regra descrita acima considera o valor absoluto dos campos \(sem o sinal\)\. 

__= = = fim RN18 = = = = = = = = = = = = = = = = = = = = = __

__RN19 \- Utilização do parâmetro “Modelo de documento para geração”__

__\(parâmetro criado na OS4786\)__

Este parâmetro é utilizado da seguinte forma:

Opção “Todos”

Neste caso serão considerados todos os modelos de documentos existentes na SAFX42, e os arquivos serão gerados separadamente por Série e Modelo\. 

Assim, os arquivos serão gerados por: Empresa, Estabelecimento, Mês/Ano, Série e Modelo\.

*\(na versão original do Conv\. 115 \(antes da OS4786\), o modelo não era critério para separação dos arquivos\)*

O nome dos arquivos *não* será alterado, pois segue o formato descrito na legislação\. Desta forma, *poderão existir arquivos de mesmo nome*, onde apenas o conteúdo será diferente, podendo cada um deles tratar um modelo diferente\. Na __RN20__ está descrito o procedimento adotado na gravação dos arquivos para permitir a gravação dos arquivos de mesmo nome\.   

Opção “01”

Neste caso serão considerados apenas os documentos fiscais da SAFX42 do Modelo escolhido \(01, 06, 21 ou 22\)\.

Opção “06”

Opção “21”

Opção “22”

__= = = fim RN19 = = = = = = = = = = = = = = = = = = = = = __

__RN20 – Gravação dos Arquivos Texto__

Ao gravar os arquivos texto, o nome dos arquivos será formado da seguinte forma, dependendo do conteúdo do parâmetro “*Formato do Convênio ICMS*” informado em tela:

__Se “Formato do Convênio ICMS” = “115”__ à o nome será formado da seguinte forma:

__Nome do Arquivo__

__Extensão__

__SÉRIE__

__ANO__

__MÊS__

__STATUS__

__TIPO__

__\.__

__VOLUME__

                 Sendo:

                 Série \- série dos documentos fiscais;

                 Ano \- ano do período de apuração dos documentos fiscais

                 Mês \- mês do período de apuração dos documentos fiscais

                 Status \- indica se o arquivo é normal \(N\) ou substituto \(S\);

                 Tipo – letra que identifica o tipo do arquivo, da seguinte forma:     M = Arquivo Mestre

                                                                                                                          I = Arquivo dos Itens

                                                                                                                          D = Arquivo dos Dados Cadastrais do Destinatário

                                                                                                                          C = Arquivo de Controle e Identificação\. 

                 Volume \(VVV\) \- número sequencial do volume\. A quantidade de registros do arquivo

__Se “Formato do Convênio ICMS” = “133”__ à o nome será formado conforme a regra acima, com a inclusão da UF, da seguinte forma:

__Nome do Arquivo__

__Extensão__

__UF__

__SÉRIE__

__ANO__

__MÊS__

__STATUS__

__TIPO__

__\.__

__VOLUME__

                 Sendo: UF \- sigla da unidade federada do emitente dos documentos fiscais;

__Alteração da OS4786: __A tela da gravação dos arquivos texto passou a exibir a identificação do modelo referente a cada arquivo demonstrado\.

Após o usuário selecionar um determinado processo, serão exibidos todos os arquivos gerados neste processo, e para cada arquivo, será demonstrado o nome do arquivo \(coluna “Título”\), e ao lado o código do modelo a qual se refere este arquivo \(Coluna “Modelo”\)\. Exemplo:

                                                            ![Convenio 115 - Grvacao dos Arquivos.png](data:image/png;base64,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)

Os arquivos serão demonstrados agrupados por modelo\.

O objetivo desta alteração é permitir que o usuário possa selecionar os arquivos por modelo, e gravá\-los em diretórios distintos, um modelo de cada vez, já que os arquivos terão o mesmo nome \(ver detalhes na __RN19__\)\. 

Este procedimento será necessário nos casos em que num mesmo processo existirem arquivos de modelos diversos, como por exemplo, modelo 21 e 22\.

\(MFS\-4969/ MFS\-6572\)

__Se “Formato do Convênio ICMS” = “Convênio ICMS 60”__ à o nome será formado da seguinte forma:

__Nome do Arquivo__

__Extensão__

__UF__

__CNPJ do Emitente__

__MODELO__

__SÉRIE__

__ANO__

__MÊS__

__STATUS__

__SEQUENCIAL__

__TIPO__

__\.__

__VOLUME__

                 Sendo:

                 UF \- sigla da unidade federada do emitente dos documentos fiscais;

                 CNPJ do Emitente \- CNPJ do Estabelecimento Emitente do Documento Fiscal \(estabelecimento da NFST\);

                 Modelo \- Modelo do Documento Fiscal;

                 Série \- série dos documentos fiscais;

                 Ano \- ano do período de apuração dos documentos fiscais

                 Mês \- mês do período de apuração dos documentos fiscais

                 Status \- indica se o arquivo é normal \(N\) ou substituto \(S\);

                 Sequencial \- Preencher com “01” quando o campo Status com a opção Normal marcada na tela de geração do arquivo magnético ou

                                      Preencher com o conteúdo informado no campo Sequencial quando for arquivo substituto, campo Status com a opção Substituta marcada na tela de

                                      geração do arquivo magnético;

                 Tipo – letra que identifica o tipo do arquivo, da seguinte forma:     M = Arquivo Mestre

                                                                                                                          I = Arquivo dos Itens

                                                                                                                          D = Arquivo dos Dados Cadastrais do Destinatário

                                                                                                                          C = Arquivo de Controle e Identificação\. 

                 Volume \(VVV\) \- número sequencial do volume\. A quantidade de registros do arquivo

Para o Convênio 60/2015 há uma mudança na quebra do arquivo, onde ele será demonstrado por estabelecimento e Modelo do Documento\. Neste contexto, desabilitaremos a opção de “Geração para Empresas c/ Inscrição Estadual Única”, uma vez que será gerado um arquivo para cada estabelecimento\. Podemos ter o cenário de seleção do campo “Modelo de Documento para geração” a opção “Todos”\. Se isso ocorrer, deverá ser gerado um arquivo para cada estabelecimento e modelo\. Sempre ocorrerá a quebra do arquivo considerando os campos que compõe a nomenclatura do mesmo\.

__= = = fim RN20 = = = = = = = = = = = = = = = = = = = = = __

__RN21 – Atualização de Layout Convênio ICMS 60/2015 – Arquivo Mestre de Documentos Fiscais__

\(MFS\-4969\)

Ao gerar o arquivo de Mestre de Documentos Fiscais, quando for selecionada na tela de geração no Formato do Convênio ICMS a opção “Convênio ICMS 60”, serão alterados/incluídos os campos abaixo destacados\.

\(MFS\-7160\)

O Convênio ICMS 94/2016 altera a descrição dos campos 32 e 33, e no momento ainda continuarão gerando da forma que foi especificado para o Convênio ICMS 60/2015, pois não existe legislação tratando documento fiscal eletrônico para os modelos de energia elétrica e comunicação/ telecomunicação\.

__N°__

__Conteúdo__

__Tam\.__

__Posição inicial__

__Posição final__

__Tipo__

__Tabela Msaf__

__Campo Msaf__

__Observações__

5

Classe de Consumo ou tipo de assinante

1

66

66

N

SAFX42

12

Este campo já existia no layout, porém, foi alterado passando a ser aplicável apenas para o segmento de Energia Elétrica\. Para atender a esta alteração, será gerado com o conteúdo do campo 12 \- Classe Usuário somente quando o Modelo do Documento \(campo 13\) for igual a “06”\. Nos demais casos, preencher com zeros\.

19

Situação do Documento

1

196

196

X

SAFX42

21

O campo 21 – Situação foi alterado para prever a possibilidade de situação igual a C \- Nota Fiscal complementar\. Esta informação, além das demais, deve ser demonstrada neste campo\.

22

Número do terminal telefônico ou Número da Conta de Consumo

12

210

221

X

SAFX42

15 / 59

O tamanho deste campo foi alterado para 12 posições\. 

__\[ALTERADO CH24596\_2016\]__

Para Telecom \(modelos 21 e 22\) utilizamos o campo 15 \- Número Telefone do Cliente e devemos alterar a geração para considerar as 12 últimas posições do campo, alinhados a esquerda, com as posições não significativas em branco\. 

Para Energia Elétrica \(modelo 06\) utilizamos o campo 59 \- Número da Conta de Consumo\. Neste caso, como o campo tem apenas 10 posições, devemos completar com zeros a esquerda\.

23

Indicação do tipo de informação contida no campo 01

01

222

222

N

Consideraremos informações do cadastro da Pessoa FIS/JUR vinculada a NFTE para geração deste campo\. Teremos a seguinte regra:

Se o campo 04 \- Indicador do Conteúdo do Código \(IND\_CONTEM\_COD\) da SAFX04 for diferente de "4 \- Se a Pessoa Física/Jurídica não tenha CPF/CGC" __E__ o campo 06 \- CPF\-CGC \(CPF\_CGC\) tiver preenchido com 14 posições, geraremos o conteúdo:

1 \- CNPJ;

Se o campo 04 \- Indicador do Conteúdo do Código \(IND\_CONTEM\_COD\) da SAFX04 for diferente de "4 \- Se a Pessoa Física/Jurídica não tenha CPF/CGC" __E__ o campo 06 \- CPF\-CGC \(CPF\_CGC\) tiver preenchido com 11 posições, geraremos o conteúdo:

2 \- CPF;

Se o campo 04 \- Indicador do Conteúdo do Código \(IND\_CONTEM\_COD\) da SAFX04 for igual a "4 \- Se a Pessoa Física/Jurídica não tenha CPF/CGC" __E__ o campo 26 \- Classe de Pessoa Física Jurídica \(IND\_CLASSE\_PFJ\) for diferente de "01 \- Pessoa Física", geraremos o conteúdo:

3 \- Pessoa Jurídica não obrigada à inscrição no CNPJ;

Se o campo 04 \- Indicador do Conteúdo do Código \(IND\_CONTEM\_COD\) da SAFX04 for igual a "4 \- Se a Pessoa Física/Jurídica não tenha CPF/CGC" __E__ o campo 26 \- Classe de Pessoa Física Jurídica \(IND\_CLASSE\_PFJ\) for igual a "01 \- Pessoa Física", geraremos o conteúdo:

4 \- Pessoa Física não obrigada ao CPF;

24

Tipo de cliente

02

223

224

N

SAFX42

113

Será gerado com o conteúdo do campo 113 \- Tipo de Cliente\.

25

Subclasse de consumo

02

225

226

N

SAFX42

114

Será gerado com o conteúdo do campo 114 \- Subclasse de Consumo\. Se não tiver conteúdo, preencher com zeros\.

26

Número do terminal telefônico principal

12

227

238

N

SAFX42

115

__\[ALTERADO CH24596\_2016\]__

Será gerado com o conteúdo do campo 115 \- Número do Terminal Telefônico Principal e devemos considerar as 12 últimas posições do campo, alinhados a esquerda, com as posições não significativas em branco\.

__\[ALTERADO MFS\-15387\]__

A partir da apuração de janeiro/2018 esse campo deverá ser preenchido com brancos \(nulo\)\.

27

CNPJ do emitente

14

239

252

N

ESTABELECIMENTO

Será gerado com o CNPJ do Estabelecimento da NF\.

28

Número ou código da fatura comercial 

20

253

272

N

SAFX42

116

Será gerado com o conteúdo do campo 116 \- Número da Fatura Comercial\.

29

Valor total da Fatura comercial

12

273

284

N

SAFX42

117

Será gerado com o conteúdo do campo 117 \- Valor Total da Fatura\.

30

Data de leitura anterior

8

285

292

N

SAFX42

118

Será gerado com o conteúdo do campo 118 \- Data de Leitura Anterior\. Se não tiver conteúdo, preencher com zeros\.

31

Data de leitura atual

8

293

300

N

SAFX42

71

Será gerado com o conteúdo do campo 71 \- Data de Leitura do Consumo\. Se não tiver conteúdo, preencher com zeros\.

32

Chave de Acesso \(CV115\-e\)

50

301

350

X

\-

\-

Sequência de espaços\.

33

Data Autorização de Emissão \(CV115\-e\)

8

351

358

N

\-

\-

Sequência se zeros\.

34

Informações adicionais

30

359

388

X

SAFX42

123 \+ 121 \+ 120 \+ 119 \+ 122

Este campo deve ser resultado da concatenação dos campos 123 \- Período de Apuração do Documento Fiscal Substituído/Complementado \+ 121 \- Modelo do Documento Fiscal Substituído/Complementado \+ 120 \- Série do Documento Fiscal Substituído/Complementado \+ 119 \- Número do Documento Fiscal Substituído/Complementado \+ 122 \- Data Emissão do Documento Fiscal Substituído/Complementado\. Ele será gerado com este conteúdo somente quando o campo 21 – Situação estiver preenchido com situação igual a R \- Refaturamento/ Substituto ou C \- Nota Fiscal complementar, caso contrário, será gerado com uma sequência de espaços\.

Devem ser informados: referência de apuração \(4 algarismos\), modelo \(2 caracteres\), série \(3 caracteres\), número \(9 algarismos\) e data de emissão \(8 algarismos\), totalizando 30 caracteres, no seguinte formato: “AAMM\_MO\_SSS\_NNNNNNNNN\_AAAAMMDD”\. Exemplo: “0901\_22\_A  \_000001234\_20090131“, para o documento fiscal da referência “0901”, modelo “22”, série “A  “, número “000001234”, emitido em 31/01/2009\.

Como o nosso campo Número da NF \(campo 119\) tem 12 posições e a regra exige apenas 9, devemos considerar as 9 últimas\.

35

Brancos – reservado p/uso futuro 

5

389

393

X

\-

\-

Sequência de espaços\.

36

Código de Autenticação do registro

32

394

425

X

\-

\-

Gerado automaticamente pelo sistema, considerando algoritmo MD5\. Observar que a regra de aplicabilidade deste algoritmo foi alterada considerando a inclusão dos novos campos, ficando da seguinte forma no convênio:

*Informar o código de autenticação digital obtido por meio da aplicação do algoritmo MD5 \(Message Digest 5\) de 128 bits na cadeia de caracteres formada pelos campos *__*01 a 35*__*\.*

__= = = fim RN21 = = = = = = = = = = = = = = = = = = = = = __

__RN22 – Atualização de Layout Convênio ICMS 60/2015 – Arquivo Item de Documentos Fiscais__

\(MFS\-4969\)

O processo de geração do arquivo de Item de Documentos Fiscais do meio magnético convênio 115 foi alterado, de modo que a geração dos itens de desconto \(SAFX431\), anteriormente opcionais, se tornou padrão a partir do Convênio ICMS 60/2015\. Deste modo, as orientações definidas na RN18 \- Utilização do parâmetro “Gravar os itens negativos no arquivo \(itens da SAFX431\)”, passam a ser exigidas quando na tela de geração o Formato do Convênio ICMS for gerado com a opção “Convênio ICMS 60”\.

Neste contexto, as origens da informação, tanto da SAFX43 quanto da SAFX431 estão definidas no arquivo “__DEPARA\_Convenio115\.doc__”, com a estrutura específica do layout definido pelo Convênio 60/2015\. Nesta regra estarão detalhados os campos alterados/incluídos, no referido convênio\.

\(MFS\-7160\)

O Convênio ICMS 94/2016 altera a forma do preenchimento do campo 3 \- Classe de Consumo ou tipo de assinante\.

O Convênio ICMS 160/2015 havia alterado a forma de preenchimento dos campos 16 \- Quantidade Contratada e 17 \- Quantidade Prestada ou Fornecida, porém não havíamos previsto, então estamos incluído através dessa MFS\.

__N°__

__Conteúdo__

__Tam\.__

__Posição inicial__

__Posição final__

__Tipo__

__Tabela Msaf__

__Campo Msaf__

__Observações__

3

Classe de Consumo ou tipo de assinante

1

17

17

N

SAFX42

12

Este campo já existia no layout, porém, foi alterado passando a ser aplicável apenas para o segmento de Energia Elétrica\. Para atender a esta alteração, será gerado com o conteúdo do campo 12 \- Classe Usuário somente quando o Modelo do Documento \(campo 13\) for igual a “06”\. Nos demais casos, preencher com zeros\.

16

Quantidade Contratada

12

110

121

N

SAFX43 / SAFX431

44 / 19

Foi alterado o tamanho do campo\. Quando se tratar de nota fiscal modelo 6 \(gerado no campo 7\), informar a quantidade contratada, com 3 decimais\. Nos demais casos preencher com zeros\.

17

Quantidade Prestada ou Fornecida

12

122

133

N

SAFX43 / SAFX431

45 / 20

Foi alterado o tamanho do campo\. Quando se tratar de nota fiscal modelo 6 \(gerado no campo 7\), informar a quantidade contratada, com 3 decimais\. Nos demais casos preencher com zeros\.

18

 Total

11

134

144

N

SAFX43 / SAFX431

19 / 21

Reposicionamento do campo no layout\.

19

Desconto/Redutores

11

145

155

N

\-

\-

Para o Convênio 60/2015, deve ser gerado com zeros\.

20

Acréscimos/Desp\. Acess\.

11

156

166

N

\-

\-

Para o Convênio 60/2015, deve ser gerado com zeros\.

21

BC ICMS

11

167

177

N

SAFX43 / SAFX431

23 / 25

Reposicionamento do campo no layout\.

22

ICMS

11

178

188

N

SAFX43 / SAFX431

22 / 24

Reposicionamento do campo no layout\.

23

Operações Isentas/Não Tributadas

11

189

199

N

SAFX43 / SAFX431

\(24\+26\) / \(26\+28\)

Reposicionamento do campo no layout\.

24

Outros Valores

11

200

210

N

SAFX43 / SAFX431

25 / 27

Reposicionamento do campo no layout\.

25

Alíquota de ICMS

4

211

214

N

SAFX43 / SAFX431

21 / 23

Reposicionamento do campo no layout\.

26

Situação

1

215

215

X

SAFX42

21

Reposicionamento do campo no layout\.

27

Ano e Mês de Referência da Apuração

4

216

219

X

\-

\-

Reposicionamento do campo no layout\.

28

Número do Contrato

15

220

234

X

SAFX43

111

Campo novo\. Será gerado com o conteúdo do campo 111 \- Número do Contrato, quando modelo do documento for igual a 21 ou 22\. Nos demais casos, preencher com uma sequência de espaços\.

29

Quantidade faturada \(3 decimais\)

12

235

246

N

SAFX43

112

Campo novo\. Será gerado com o conteúdo do campo 112 \- Quantidade Faturada\.

30

Tarifa aplicada / Preço médio efetivo \(6 decimais\)

11

247

257

N

SAFX43

113

Campo novo\. Será gerado com o conteúdo do campo 113 \- Tarifa aplicada, quando modelo do documento for igual a 06\. Nos demais casos, preencher com uma sequência de zeros\.

31

Alíquota PIS/PASEP \(4 decimais\)

06

258

263

N

SAFX43 / SAFX431

79 / 30

Campo novo\. Será gerado com o conteúdo do campo 79 – Alíquota PIS\.

32

PIS/PASEP \(2 decimais\)

11

264

274

N

SAFX43 / SAFX431

77 / 31

Campo novo\. Será gerado com o conteúdo do campo 77 – Valor do PIS\.

33

Alíquota COFINS \(4 decimais\)

06

275

280

N

SAFX43 / SAFX431

82 / 32

Campo novo\. Será gerado com o conteúdo do campo 82 – Alíquota COFINS\.

34

COFINS \(2 decimais\)

11

281

291

N

SAFX43 / SAFX431

80 / 33

Campo novo\. Será gerado com o conteúdo do campo 80 – Valor COFINS\.

35

Indicador de desconto judicial

01

292

292

X

SAFX431

34

Campo novo\. Será gerado com espaço em branco quando for gerado Item da SAFX43\.

Se a origem for a SAFX431, será gerado com base no campo 34 \- Indicador de Desconto Judicial, sendo que, se for igual a S, deve gerar conteúdo “J”\. Se for diferente de S, gera um espaço em branco\.

36

Tipo de isenção/redução de base de cálculo

02

293

294

N

SAFX43

114

Campo novo\. Será gerado com o conteúdo do campo 114 \- Tipo de Isenção/Redução da BC\.

37

Brancos – reservado p/uso futuro

05

295

299

X

\-

\-

Sequência de espaços\.

38

Código de Autenticação do registro

32

300

331

X

\-

\-

Gerado automaticamente pelo sistema, considerando algoritmo MD5\. Observar que a regra de aplicabilidade deste algoritmo foi alterada considerando a inclusão dos novos campos, ficando da seguinte forma no convênio:

*Informar o código de autenticação digital obtido por meio da aplicação do algoritmo MD5 \(Message Digest 5\) de 128 bits na cadeia de caracteres formada pelos campos *__*01 a 37*__*\.*

__= = = fim RN22 = = = = = = = = = = = = = = = = = = = = = __

__RN23 – Atualização __<a id="_Hlk524964053"></a>__de Layout Convênio ICMS 60/2015 – Arquivo dos Dados Cadastrais__

\(MFS\-4969\)

Ao gerar o arquivo de Dados Cadastrais, quando for selecionada na tela de geração no Formato do Convênio ICMS a opção “Convênio ICMS 60”, serão alterados/incluídos os campos abaixo destacados:

__N°__

__Conteúdo__

__Tam\.__

__Posição inicial__

__Posição final__

__Tipo__

__Tabela Msaf__

__Campo Msaf__

__Observações__

09

Município

30

152

181

X

SAFX04

16

__MFS20889__

__\[MFS657377\] Inclusão do tratamento para UF do exterior__

Se o parâmetro __“Geração Descrição de Município por Cód\. IBGE”__ estiver marcado na tela de parametrização do convênio 115

    Se a UF = “EX” \(Exterior\)

         Recuper a informação do campo CIDADE da    

         tabela SAFX04

    Senão

         Recuperar na TACES06 a descrição do         

         município contida na coluna

         “DESCRICAO\_MUNICIPIO\_COD\_IBGE”       

          através do “Join” de Código UF\+ Código 

          Município do fornecedor \(SAFX04\) e da        

         TACES06

Senão \(parâmetro desmarcado\)

     Recuperar a informação do campo CIDADE da tabela SAFX04\.

11

Telefone de Contato

12

184

195

N

SAFX04

22 e 23

__\[ALTERADO CH24596\_2016\]__

Foi alterado o tamanho do campo para 12 posições\. Deve ser gerado considerando a concatenação das duas últimas posições do campo 22 – DDD \+ os números significativos \(desconsiderar zeros a esquerda\) do campo 23 – Telefone\. Alinhar a esquerda, com as posições não significativas em branco\. 

Exemplo:

Campo DDD = 011

Campo Telefone = 912345678

No campo será gerado ‘11912345678 ‘ \(com 1 espaço branco no final\)

12

Código de Identificação do Consumidor ou assinante

12

196

207

X

SAFX04

02

Reposicionamento do campo no layout\.

13

Número do terminal telefônico ou número da conta de consumo

12

208

219

X

SAFX42

15 / 59

O tamanho deste campo foi alterado para 12 posições\. 

__\[ALTERADO CH24596\_2016\]__

Para Telecom \(modelos 21 e 22\) utilizamos o campo 15 \- Número Telefone do Cliente e devemos alterar a geração para considerar as 12 últimas posições do campo, alinhados a esquerda, com as posições não significativas em branco\. 

Para Energia Elétrica \(modelo 06\) utilizamos o campo 59 \- Número da Conta de Consumo\. Neste caso, como o campo tem apenas 10 posições, devemos completar com zeros a esquerda\.

14

UF de habilitação do terminal telefônico

2

220

221

X

SAFX42

60

Reposicionamento do campo no layout\.

Esse campo é gerado de acordo com a condição abaixo:

Se o modelo é 21 ou 22

   campo 14 é igual ao campo uf\_tel\_cliente da 42;

Se o modelo é 01 ou 06 

    campo 14 é vazio

15

Data de emissão

8

222

229

N

SAFX42

03

Campo novo\. Será gerado com a Data Emissão da nota que originou o registro\.

16

Modelo

2

230

231

N

SAFX42

13

Campo novo\. Será gerado com o Modelo do Documento da nota que originou o registro

17

Série

3

232

234

X

SAFX42

07

Campo novo\. Será gerado com a Série da nota que originou o registro

18

Número

9

235

243

N

SAFX42

06

Campo novo\. Será gerado com o Número da nota que originou o registro, considerando as 9 últimas posições do campo\.

19

Código do município

7

244

250

N

SAFX04

25

Campo novo\. Será gerado com Código do município informado no campo 09 \(cód\. UF \+ cód\. Munic\.\)

20

Brancos – reservado p/uso futuro

5

251

255

X

\-

\-

Sequência de espaços\.

21

Código de Autenticação do registro

32

256

287

X

\-

\-

Gerado automaticamente pelo sistema, considerando algoritmo MD5\. Observar que a regra de aplicabilidade deste algoritmo foi alterada considerando a inclusão dos novos campos, ficando da seguinte forma no convênio:

*Informar o código de autenticação digital obtido por meio da aplicação do algoritmo MD5 \(Message Digest 5\) de 128 bits na cadeia de caracteres formada pelos campos *__*01 a 20*__*\.*

Com a inclusão dos novos campos, a ordenação o registro também foi alterada\. Para o Convênio 60/2015 a ordenação será através dos campos 15 \- Data de emissão, 16 \- Modelo, 17 \- Série e 18 \- Número, em ordem crescente\.

__= = = fim RN23 = = = = = = = = = = = = = = = = = = = = = __

__RN24 – Arquivo Mestre, campo “06\-Fase ou Tipo de Utilização”__

__             Arquivo dos Itens, campo “04\-Fase ou Tipo de Utilização”__

Este campo é gerado a partir do campo “49\-Tipo de Utilização” da capa do documento fiscal \(SAFX42\), tanto no Arquivo Mestre, como no Arquivo dos Itens\.

__ \(MFS7783\)__ – Alterada a regra de geração do campo “Fase ou Tipo de Utilização” p/os documentos de modelo <> “06”\. 

__Para os documentos de energia elétrica \(modelo 06\):__

     Este campo é gerado a partir do campo “49\-Tipo de Utilização” da capa do documento fiscal \(SAFX42\), tanto no Arquivo Mestre, como no Arquivo dos Itens\.

__Para os demais documentos \(outros modelos\):__

     A geração passou a seguir a regra abaixo:

     \-__No Arquivo Mestre__ \(campo 06\):

     O campo será gravado com o conteúdo do campo “49\-Tipo de Utilização” da capa do documento fiscal \(SAFX42\);

     \-__No Arquivo de Itens__ \(campo 04\):

     A geração dependerá da parametrização *“Tipos de Utilização p/ Classificação do Item” *do Módulo ICMS \(\*\), da seguinte forma:

     \(\*\) menu “*Datamart à Convênio ICMS 115 à Parametrização dos Tipos de Utilização p/Classificação do Item”*

     Será verificado se a classificação do item \(campo “42\-Classificação do Item” da SAFX43\) consta na parametrização, a partir dos seguintes critérios:

          \- Classificação do Item = conteúdo do campo “42\-Classificação do Item” da SAFX43;

          \- Data de Validade = considerar a maior data de validade que seja igual ou inferior à data de emissão do documento \(campo 03 da SAFX42\);

     Se existirem dados à será utilizado o conteúdo do campo “Tipo de Utilização” da parametrização recuperada;

     Caso contrário à será utilizado o conteúdo do campo “49\-Tipo de Utilização” da capa do documento fiscal \(SAFX42\);

 

__= = = fim RN24 = = = = = = = = = = = = = = = = = = = = = __

__RN25 – Geração da tabela auxiliar ICT\_MM\_CONV115\_UF\_CFOP__

__\(Tabela utilizada para geração dos registros do SPED Fiscal\)__

__\[MFS524611\] Alteração da geração da tabela para não considerar os documentos escriturados com o CFOP 0000, porque essa tabela somente é utilizada para gerar alguns registros do SPED\-EFD, que não aceita CFOP com 0000\.  O CFOP 0000 é utilizado para a geração do convênio 115, conforme previsto em legislação\.__

A rotina de geração do arquivo magnético do Convênio 115 deve ser alterada para que durante o processamento sejam totalizados os valores por CST\-ICMS, CFOP, Alíquota e UF, e sejam armazenados numa tabela auxiliar\.  Devem ser desconsiderados os registros que tiverem o CFOP preenchido com 0000\.

A cada geração estes dados auxiliares devem ser limpos e regerados, juntamente com os dados principais\.

Estes dados serão utilizados para gravar os registros C790, D696 e D697 do Sped Fiscal\.

Os valores devem ser totalizados a partir dos itens gravados no arquivo “ITENS” do Convênio 115, já que é na tabela dos itens \(SAFX43\) que estão as informações do CST\_ICMS, CFOP e Alíquota do ICMS\.  

A UF a ser considerada na totalização é a UF da pessoa fis/jur do documento \(destinatário\)\.

 

__\[MFS67557\] Alteração da forma de gravar os valores Isenta e Outras, para atender as regras da Portaria CAT 66/2019\.  Esse valores são usados na geração do registro C790 do SPED Fiscal\.__

Segue definição dos valores a serem totalizados por código de tributação, CFOP, alíquota e UF:

         Sped 

                                                         SAFX43

CST\_ICMS

É a concatenação dos códigos das tabelas de situação estadual  "A" e "B" \(código A \+ código B\), que são os campos 32 e 33 da SAFX43\.

\(o código CST não consta dos arquivos do Convênio 115\) 

Importante à quando se tratar de um item de serviço \(Classificação do item = 2\), e os campos não estiverem preenchidos, deve\-se considerar o código “090”\.

CFOP

Campo 13 – Código Fiscal da SAFX43

ALIQ\_ICMS

Campo 21 \- Alíquota de ICMS da SAFX43

UF

UF da pessoa fis/jur \(campo 19 da SAFX04\)            

VL\_OPR

Totalização do valor contábil dos itens da SAFX43, que deverá ser calculado para cada item da seguinte forma:

                           Valor do serviço – Desconto \+ Outras Despesas

                                  \(campo 19 – campo 18 \+ campo 46\)

Observar que na SAFX43 não existe este valor, por isso ele terá que ser calculado \(é diferente da SAFX08, que tem os dois valores, o valor do item e o valor contábil do item\)\.

VL\_BC\_ICMS

Totalização do campo 23 – Base Tributada da SAFX43

VL\_ICMS

Totalização do campo 22 – Valor ICMS da SAFX43

VL\_BC\_ICMS\_ST

Totalização do campo 40 – Base Substituição Tributária da SAFX43

\(a base do ICMS\-ST não consta dos arquivos do Convênio 115\)

VL\_ICMS\_ST

Totalização do campo 39 – Valor Substituição Tributária da SAFX43

\(o valor do ICMS\-ST não consta dos arquivos do Convênio 115\)

VL\_RED\_BC

Totalização do campo 26 – Base de Redução da SAFX43

\(a base de redução não consta dos arquivos do Convênio 115\) 

VL\_OUTRAS

Campo criado na MFS31749 – Alterado MFS67557

Totalização do campo 25 – Base Outras da SAFX43

Totalização do valor outras, que deverá ser calculado para cada item da seguinte forma:

Se o código de situação estadual "B" <> 30 e <> 40 e <> 41

      VL\_OPR \- VL\_BC\_ICMS \- VL\_ICMS\_ST \- VL\_RED\_BC

Obs\.: Se o resultado da operação for um valor negativo, gravar zero\.

VL\_ISENTA

Campo criado na MFS31749 – Alterado MFS67557

Totalização do campo 24 – Base Isenta/Não Tributada da SAFX43

Totalização do valor Isenta, que deverá ser calculado para cada item da seguinte forma:

Se o código de situação estadual "B" = 30 ou 40 ou 41

      Resultado 1 = VL\_OPR \- VL\_BC\_ICMS \- VL\_ICMS\_ST \- VL\_RED\_BC

VL\_ISENTA = Resultado 1 \+ VL\_RED\_BC \(para qualquer código de situação estadual "B"\)

Obs\.: Se o resultado da operação for um valor negativo, gravar zero\.

Com esta totalização, para cada volume do arquivo Mestre, existirão “n” registros na nova tabela temporária, um para cada combinação CST x CFOP x ALIQ x UF \(na prática, para cada linha da ICT\_MM\_CONV115 existirão “n” linhas na nova tabela\)\. É importante observar que no desenho desta nova tabela deve\-se identificar claramente os dados do arquivo Mestre totalizado \(conforme chave da tabela ICT\_MM\_CONV\_115, desprezando apenas o tipo do arquivo, que não é necessário\)\.

__= = = fim RN25 = = = = = = = = = = = = = = = = = = = = = __

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

