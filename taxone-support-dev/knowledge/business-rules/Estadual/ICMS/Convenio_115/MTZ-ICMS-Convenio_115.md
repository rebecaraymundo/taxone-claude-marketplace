# MTZ-ICMS-Convenio_115

- **Fonte:** MTZ-ICMS-Convenio_115.docx
- **Modificado:** 2025-09-17
- **Tamanho:** 79 KB

---

# Módulo – ICMS – Convênio ICMS 115

	

__Localização:__

__Módulo: __ICMS 

__Menu:   __DATAMART => Convênio ICMS 115

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

Correção dos Registros de Telecom do Sped Fiscal

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

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Regras Gerais da Geração do Arquivo do Convênio ICMS 115/03__:

Os arquivos do Convênio 115 são gerados por série do documento, e por quantidade de documentos\. Séries diferentes geram arquivos diferentes, e dependendo da quantidade de notas, poderão ser gerados vários volumes da mesma série\.

Ao final da geração, serão armazenadas diversas informações sobre cada volume de arquivo gerado:

Tabela __ICT\_MM\_CONV115__ à Contém os dados gerais de cada volume do arquivo \(data, número, valores totais, nome e volume do arquivo\)\. O código de autenticação digital do arquivo mestre será preenchido apenas na rotina de importação do hash\-code\. 

Tabela __ICT\_MM\_CNV115\_UF\_CFOP__ à Contém o detalhamento dos valores totalizados por CST / CFOP / ALIQ / UF \(UF do destinatário do documento\)\. Estes valores são utilizados na geração do Sped Fiscal\.

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

Quando o parâmetro for = “S”, na geração de cada volume do arquivo, serão armazenadas algumas informações sobre as UF’s com as quais existam

    operações\. Para cada uma das UF’s \(*exceto a UF do próprio estabelecimento*\), para as quais existam notas fiscais emitidas no período, serão ser

    armazenadas as seguintes informações:

- UF \(UF do destinatário\);
- Nome do arquivo mestre que será gerado pelo programa extrator do Conv\.115 \(será o mesmo nome do arquivo mestre  “normal”, trocando apenas as duas primeiras posições para a sigla da UF\);
- Volume do arquivo; 
- Código de Autenticação Digital – deixar em branco \(será preenchido somente na rotina de importação dos hash code\); 

     Estas informações serão utilizadas na rotina de importação dos hash\-code, para possibilitar que sejam importados também os códigos de autenticação dos   

      arquivos que serão gerados pelo programa “extrator” do Convênio ICMS 115\. 

__Alteração da OS3330\-A:__

    Na tela de Geração Convênio 115, foi retirado o parâmetro Estabelecimento e acrescentado o Parâmetro “UF”\. Quando o usuário optar pelo estado de sua

     escolha no parâmetro "UF”, a rotina deverá fazer um filtro na tabela ESTABELECIMENTO onde COD\_ESTADO seja igual ao COD\_ESTADO da tabela ESTADO

     e pertençam a UF selecionada\. 

Os estabelecimentos que passarem pelo critério de seleção do parâmetro, deverão ser apresentados no quadro “Estabelecimento” em forma de lista com

     o flag para o usuário selecionar apenas os que participarão da única geração\.

Os estabelecimentos selecionados serão executados todos juntos, sendo possível porque compartilham de um mesmo controle de numeração de notas

     fiscais por série distintas\.

__Alteração da OS3974 \(Abr/2013\):__

    A geração do arquivo foi alterada para gerar no arquivo dos itens, os  “itens adicionais”   referentes aos dados de cofaturamento armazenados na tabela SAFX213\. O preenchimento destes “itens adicionais” segue as orientações da Portaria CAT 24/2013, e está descrito na regra __RN16__\.

__OS3330\-A/ __

__OS3851 / __

__OS3974__

__RN01__

Recuperar o somatório do campo 18 \( valor de descontos \) da SAFX43, dentro do período e informar este somatório no campo 28 – Somatório de descontos do relatório de conferência de arquivo eletrônico da geração do meio magnético do Convênio 115\.

__OS2609\-D__

__RN02__

Excluir o label “ Desconsiderar valor de Descontos no cálculo do valor contábil” da tela de geração do mapa resumo\.

__OS2609\-D__

__RN03__

A partir desta OS, o label “Desconsiderar valor de Descontos no cálculo do valor contábil” , deverá ser excluídos conforme a regra RN02, de forma que não serão exibidos na tela de geração do meio magnético convênio 115\.

__OS2609\-D__

__\[EXCLUIDA – OS4281\]: __A regra de negócio que compõe a quebra do arquivo pela quantidade de documento fiscal está no arquivo MTZ\_ICMS\_Convenio\_115\_ Quantidade\_Documentos\_Fiscais\_por\_Volume\.docx

__RN05__

__\[Alteração da OS3424\-D\]:__

__Módulo:__ Estadual >> ICMS 

__Menu:__ DATA MART __>>__ __Convênio ICMS 115 >> Geração do Meio Magnético__

Em São Paulo ao contrário de outros estados, a apuração do ICMS dos documentos fiscais de Energia Elétrica é realizada pela Data de Vencimento das Faturas, ao contrário de outros documentos fiscais cuja apuração é realizada pela Data Fiscal ou Data de Emissão/Data de Entrada\-Saída\. Em algumas situações esses documentos fiscais de Energia Elétrica são cancelados no mês posterior ao mês de vencimento fazendo com que os mesmos sejam gerados como cancelados e não com status de documento normal, visto que essa era a situação na época do vencimento\. 

Com a publicação do Decreto 57\.177/2011, a apuração, a partir de 01/2012, passou ter como base a data de emissão/ fiscal da nota fiscal\.

Para que essa situação não ocorra novamente, os Documentos Fiscais de Energia Elétrica que estejam cancelados deverão ser recuperados e gerados no meio magnético __Convênio ICMS 115/03__ e Geração Automática dos Mapas Resumo da seguinte forma:

Quando o campo 13 \- COD\_MODELO \(SAFX42\) = ‘6’, UF Estabelecimento = SP, UF Destinatário = SP, verificar:

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

__\[EXCLUIDA – OS4281\]: __A regra de negócio que compõe a quebra do arquivo pela quantidade de documento fiscal está no arquivo MTZ\_ICMS\_Convenio\_115\_ Quantidade\_Documentos\_Fiscais\_por\_Volume\.docx

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

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

