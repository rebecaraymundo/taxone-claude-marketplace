# MTZ-GISS_ONLINE

- **Fonte:** MTZ-GISS_ONLINE.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 150 KB

---

__Módulo GISS ON LINE__

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3143

OS3143\-C

Geração do Meio Magnético GISS\-Maceió

Complemento do layout para atender Construção Civil

Este documento especifica os registros para compor o arquivo texto do módulo GISS ON LINE a ser adequado aos municípios aderentes a esta obrigação\.

CH104403

- Alteração parâmetro de layout por Município

Alteração parâmetro de layout por Município

CH108506

Erro na geração do arquivo, não está gerando a informação"PRESTADOR OPTANTE PELO SIMPLES", o sistema está usando a alíquota da lista de serviços e não a alíquota diferenciada\.

Considerar na geração a informação de Optante pelo simples

OS3143\-O

Criação de tela de parametrização de Serviços

Parametrização de serviços, criação de flag e adequação da tela Definição de Layout\.

OS3585

Regra para alterar o campo tipo da nota

Regra para alterar o campo tipo da nota

__OBS Gerais: __

__\-Todos os registros estarão inclusos em um único arquivo texto exceto os registros de Abatimento de Construção Civil e SubEmpreitada que serão feitos em formato XML__

__\- Caso a nota fiscal possua mais de um item:__

__   Quando possuir mais de um item com códigos de serviço IGUAIS: neste caso, levar somente uma linha sumarizando os valores de  cada item, pois como se trata de somente uma natureza de serviço não há a necessidade de desmembrar os valores\.__

__  Quando possuir mais de um item com códigos de serviço DIFERENTES: neste caso, desmembrar uma linha para cada código de serviço, levando o valor do serviço de cada item e não o valor total da nota\. O campo que deverá ser utilizado é “valor total” do item de serviço__

__\- O número final de nota fiscal solicitado pelos registros será o mesmo número do inicial\.__

__\- A regra de recuperação para a data das notas fiscais será sempre pela data\_fiscal da tabela safx07, apenas demonstrando no arquivo o campo de data de emissão\.__

__LAYOUT GISS On Line Registro Serviço Prestado para Pessoa Física__

__RN00__

Gravar no campo “Identificação de Registro” o caracter fixo “C”\.

OS3143

__RN01__

Recuperar a informação do campo NUM\_DOCFIS da tabela SAFX07\. Caso o campo a nota fiscal tenha o campo movto\_e\_s = ‘9’ da tabela safx07 e o campo CPF\_CGC da tabela safx04 atrelada à nota tenha menos de 14 dígitos\.

Não carregar para este tipo de registro quando o campo ind\_tp\_servico = 1 da tabela x2018\_servicos

OS3143

__RN02__

Recuperar a informação do campo SERIE\_DOCFIS da tabela SAFX07\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN03__

Recuperar a informação do campo DATA\_EMISSAO da tabela SAFX07\. A data deve ser informada no meio magnético no formato dd/mm/aaaa\.

OS3143

__RN04\-S__

Deve ser informado o tipo da nota fiscal\.

__\[EXCLUIDA\]__

6 – Pagto pelo Prestador: se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 455 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Prestador

__ALTERADA OS3585__

__6__ – Pagto pelo Prestador: gravar “6” 

__SE__ a UF \(COD\_ESTADO da tabela SAFX2097\) = ‘SP’ 

__E__ o código do município \(COD\_MUNIC\_MSAF da tabela SAFX2097\) = ‘48500’ 

__       E __o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação 

       de serviços – Município com o cód\_param = 455 

       __OU ENTÃO__ o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido 

       Pelo prestador\.

__Obs:__ Caso o campo “Município ISS” do documento fiscal de serviço estiver vazio, considerar o município da tabela ESTABELECIMENTO

__\*Para verficar o código do município da SAFX2097: __

O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS, deve se utilizar o código do município IBGE \(campo COD\_MUNIC\_MSAF\) correspondente\.

__1__ – Tributada: gravar “1” se não forem atendidas as condições abaixo \(de 2 a 8 – Excluindo a 6\)\.

__2__ – Cancelada: gravar “2” no meio magnético, quando o campo SITUACAO da tabela SAFX07 estiver preenchido com “S” \(na tela o flag “Sit\. Cancelado” estiver marcado\)\.

__5 –__ Retida: gravar “5” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 454 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Tomador

__4 –__ Isenta: gravar “4” no meio magnético, quando o campo 38 \(tributação ISS\) da tabela safx09 estiver preenchido com 2\- isento ou o campo ind\_iss da tabela ESTABELECIMENTO estiver preenchido com 04\. Se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 433\.

__7 –__ Imune: gravar “7” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 420 ou o campo ind\_iss da tabela ESTABELECIMENTO estiver preenchido com 01\.

__8 –__ S\.Judicial: gravar “8” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 427 ou  o campo ind\_iss da tabela ESTABELECIMENTO estiver preenchido com 03\.

__3 –__ Anulada: não será tratada nessa OS\.

OS3143

OS3585

__RN05__

Recuperar a informação do campo VLR\_TOT da tabela SAFX09\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\. Não devem ser utilizados pontos ou vírgulas\. Exemplo: o valor 12,34 fica representado como:

000000001234

OS3143

__RN06__

\[ALTERADA – OS3143\-O\]

__Campo Código do Serviço/Atividade__

Verificar opção selecionada no menu Parâmetros > Definição de Layout:

__Se__ a opção Recuperar Código de Serviço – Lei Complementar 116/03 estiver selecionada, recuperar a informação do campo cod\_serv\_lei\_116 da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Se__ a opção Recuperar Código Natureza de Serviço estiver selecionada, recuperar a informação do campo COD\_NAT\_SERV da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Senão__ recuperar a informação do campo Serviços, através da tela Serviços Msaf x Serviços Municipais\. Para os casos em que tiver mais de 1 parametrização com o mesmo Código do  Serviço Msaf e Código do Serviço Municipal, deverá ser recuperado a parametrização com a data mais atual\. 

__Tamanho do campo:__

Se a informação do campo ultrapassar de 10 caracteres, sistema deverá exibir a seguinte mensagem no log:  “Informação do campo Atividade ou Serviço Prestado ultrapassa 

o tamanho permitido\. Tamanho permitido para o campo é de até 10 caracteres\.”

OS3143

OS3143

OS3143\-O

__RN07__

Gravar no campo “Tomador” o número “1”\.

OS3143

__RN08\-S__

\[ALTERADA – OS3143\]  

__OBS:Regra para notas de saída:__

D – Dentro do Município: Gravar “D” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for o mesmo município cadastrado para o estabelecimento emissor do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. 

F – Fora do Município: Gravar “F” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for diferente do município cadastrado para o estabelecimento emissor do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. 

Caso o campo “Município ISS” do documento fiscal de serviço estiver vazio, considerar o município da tabela ESTABELECIMENTO, portanto do emitente e considerar = D e criar log de geração com a seguinte mensagem:

“Município com local de prestação de serviço não localizado na capa do documento fiscal\. Neste caso, para as saídas foi considerado o município do emitente da nota fiscal para definir o Local de Prestação de Serviço\.”

OS3143

__LAYOUT GISS On Line Registro Serviço Prestado para Pessoa Jurídica__

__RN00__

Gravar no campo “Identificação de Registro” o caracter fixo “C”\.

OS3143

__RN01\-A__

Recuperar a informação do campo NUM\_DOCFIS da tabela SAFX07\. Caso o campo a nota fiscal tenha o campo movto\_e\_s = ‘9’ da tabela safx07 e o campo CPF\_CGC da tabela safx04 atrelada à nota tenha 14 dígitos\. 

Não carregar para este tipo de registro casos onde no cadastro de Pessoa Fis/Jur \(tabela safx04\) tiver o campo UF preenchido como  “EX” e campo ind\_tp\_servico = 1 da tabela x2018\_servicos

OS3143

__RN02__

Recuperar a informação do campo SERIE\_DOCFIS da tabela SAFX07\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN03__

Recuperar a informação do campo DATA\_EMISSAO da tabela SAFX07\. A data deve ser informada no meio magnético no formato dd/mm/aaaa\.

OS3143

__RN04\-S__

Deve ser informado o tipo da nota fiscal\.

__\[EXCLUIDA\]__

6 – Pagto pelo Prestador: se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 455 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Prestador

__ALTERADA OS3585__

__6__ – Pagto pelo Prestador: gravar “6” 

__SE__ a UF \(COD\_ESTADO da tabela SAFX2097\) = ‘SP’ 

__E__ o código do município \(COD\_MUNIC\_MSAF da tabela SAFX2097\) = ‘48500’ 

__       E __o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação 

       de serviços – Município com o cód\_param = 455 

       __OU ENTÃO__ o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido 

       Pelo prestador\.

__Obs:__ Caso o campo “Município ISS” do documento fiscal de serviço estiver vazio, considerar o município da tabela ESTABELECIMENTO

__\*Para verficar o código do município da SAFX2097: __

O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS, deve se utilizar o código do município IBGE \(campo COD\_MUNIC\_MSAF\) correspondente\.

__1__ – Tributada: gravar “1” se não forem atendidas as condições abaixo \(de 2 a 8 – Excluindo a 6\)\.

__2__ – Cancelada: gravar “2” no meio magnético, quando o campo SITUACAO da tabela SAFX07 estiver preenchido com “S” \(na tela o flag “Sit\. Cancelado” estiver marcado\)\.

__5 –__ Retida: gravar “5” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 454 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Tomador

__4 –__ Isenta: gravar “4” no meio magnético, quando o campo 38 \(tributação ISS\) da tabela safx09 estiver preenchido com 2\- isento ou o campo ind\_iss da tabela ESTABELECIMENTO estiver preenchido com 04\. Se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 433\.

__7 –__ Imune: gravar “7” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 420 ou o campo ind\_iss da tabela ESTABELECIMENTO estiver preenchido com 01\.

__8 –__ S\.Judicial: gravar “8” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 427 ou  o campo ind\_iss da tabela ESTABELECIMENTO estiver preenchido com 03\.

__3 –__ Anulada: não será tratada nessa OS\.

OS3143

OS3585

__RN05__

Recuperar a informação do campo VLR\_TOT da tabela SAFX09\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\. Não devem ser utilizados pontos ou vírgulas\. Exemplo: o valor 12,34 fica representado como:

000000001234

OS3143

__RN06__

\[ALTERADA – OS3143\-O\]

__Campo Código do Serviço/Atividade__

Verificar opção selecionada no menu Parâmetros > Definição de Layout:

__Se__ a opção Recuperar Código de Serviço – Lei Complementar 116/03 estiver selecionada, recuperar a informação do campo cod\_serv\_lei\_116 da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Se__ a opção Recuperar Código Natureza de Serviço estiver selecionada, recuperar a informação do campo COD\_NAT\_SERV da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Senão__ recuperar a informação do campo Serviços, através da tela Serviços Msaf x Serviços Municipais\. Para os casos em que tiver mais de 1 parametrização com o mesmo Código do  Serviço Msaf e Código do Serviço Municipal, deverá ser recuperado a parametrização com a data mais atual\. 

__Tamanho do campo:__

Se a informação do campo ultrapassar de 10 caracteres, sistema deverá exibir a seguinte mensagem no log:  “Informação do campo Atividade ou Serviço Prestado ultrapassa 

o tamanho permitido\. Tamanho permitido para o campo é de até 10 caracteres\.”

OS3143

OS3143\-O

__RN09__

Gravar o número “2”\.

OS3143

__RN10__

S – Estabelecido: Gravar “S” quando o cod\_municipio da tabela safx04 correspondente à Pessoa Fis/Jur da nota fiscal for igual ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

N – Não Estabelecido: Gravar “N” quando o cod\_municipio da tabela safx04 correspondente à Pessoa Fis/Jur da nota fiscal for diferente ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

OS3143

__RN11__

Recuperar a informação do campo RAZAO\_SOCIAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN12__

Recuperar a informação do campo INSC\_MUNICIPAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado \(10 posições\)\.

OS3143

__RN13__

Recuperar os dois últimos dígitos da informação do campo INSC\_MUNICIPAL da tabela SAFX04 caso o campo possua mais de 10 dígitos\. Caso o campo não preencha todas as posições preencher o mesmo com espaços\.

OS3143

__RN14__

Recuperar a informação do campo CPF\_CGC da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN15__

S – Isento: gravar “S” quando no cadastro da Safx04 o campo “Inscrição Estadual” estiver escrito “ISENT%”\.

N – Não Isento: gravar “N” quando no cadastro da Safx04 o campo “Inscrição Estadual” estiver preenchido com números\.

OS3143

__RN16__

Recuperar a informação do campo INSC\_ESTADUAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.Tratar esta regra somente se RN15 for N\.

OS3143

__RN17__

Recuperar a informação do campo CEP da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN18__

Recuperar a informação do campo TP\_LOGRADOURO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN13__

Inserir espaços em branco até completar o campo\. 

OS3143

__RN20__

Recuperar a informação do campo ENDERECO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN21__

Recuperar a informação do campo COMPL\_ENDERECO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN22__

Recuperar a informação do campo NUM\_ENDERECO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN23__

Recuperar a informação do campo BAIRRO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN24__

Recuperar a informação do campo UF da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN25__

Recuperar a informação da descrição do município da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN08\-S__

\[ALTERADA – OS3143\]

__OBS:Regra para notas de saída:__

D – Dentro do Município: Gravar “D” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for o mesmo município cadastrado para o estabelecimento emissor do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. 

F – Fora do Município: Gravar “F” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for diferente do município cadastrado para o estabelecimento emissor do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. 

Caso o campo “Município ISS” do documento fiscal de serviço estiver vazio, considerar o município da tabela ESTABELECIMENTO, portanto do emitente e considerar = D e criar log de geração com a seguinte mensagem:

“Município com local de prestação de serviço não localizado na capa do documento fiscal\. Neste caso, para as saídas foi considerado o município do emitente da nota fiscal para definir o Local de Prestação de Serviço\.”

OS3143

__LAYOUT GISS On Line Registro Serviço Tomado de Prestador Residente no Pais com Nota Fiscal__

__RN26__

Gravar no campo “Identificação de Registro” o caracter fixo “T”\.

OS3143

__RN01\-B__

Recuperar somente notas fiscais utilizando o campo NUM\_DOCFIS da tabela SAFX07 para casos onde no cadastro de Pessoa Fis/Jur \(tabela safx04\) tiver o campo UF preenchido diferente de  “EX” e campo indicador de entrada ou saída deverá constar = “1”\. O Tipo de documento fiscal deverá ser diferente de RPA\. Campo ind\_tp\_servico <> 1 da tabela x2018\_servicos\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN02__

Recuperar a informação do campo SERIE\_DOCFIS da tabela SAFX07\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN03__

Recuperar a informação do campo DATA\_EMISSAO da tabela SAFX07\. A data deve ser informada no meio magnético no formato dd/mm/aaaa\.

OS3143

__RN04\-E__

Deve ser informado o tipo da nota fiscal\.

__\[EXCLUIDA\]__

6 – Pagto pelo Prestador: se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 455 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Prestador

__ALTERADA OS3585__

__6__ – Pagto pelo Prestador: gravar “6” 

__SE__ a UF \(COD\_ESTADO da tabela SAFX2097\) = ‘SP’ 

__E__ o código do município \(COD\_MUNIC\_MSAF da tabela SAFX2097\) = ‘48500’ 

__       E __o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação 

       de serviços – Município com o cód\_param = 455 

       __OU ENTÃO__ o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido 

       pelo prestador\.

__\*Para verficar o código do município da SAFX2097: __

O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS, deve se utilizar o código do município IBGE \(campo COD\_MUNIC\_MSAF\) correspondente\.

__1__ – Tributada: gravar “1” se não forem atendidas as condições abaixo \(de 2 a 8 – Excluindo a 6\)\.

__2__ – Cancelada: gravar “2” no meio magnético, quando o campo SITUACAO da tabela SAFX07 estiver preenchido com “S” \(na tela o flag “Sit\. Cancelado” estiver marcado\)\.

__5 –__ Retida: gravar “5” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 454 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Tomador

__4 –__ Isenta: gravar “4” no meio magnético, quando o campo 38 \(tributação ISS\) da tabela safx09 estiver preenchido com 2\- isento ou o campo IND\_CLASSE\_PFJ da SAFX04 estiver preenchido com 10 ou Se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 433\.

__7 –__ Imune: gravar “7” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 420 ou o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07\.

__8 –__ S\.Judicial: gravar “8” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 427 ou  o campo IND\_CLASSE\_PFJ da SAFX04 = “09” 

__3 –__ Anulada: não será tratada nessa OS\.

OS3143

OS3585

__RN05__

Recuperar a informação do campo VLR\_TOT da tabela SAFX09\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\. Não devem ser utilizados pontos ou vírgulas\. Exemplo: o valor 12,34 fica representado como:

000000001234

OS3143

__RN06__

\[ALTERADA – OS3143\-O\]

__Campo Código do Serviço/Atividade__

Verificar opção selecionada no menu Parâmetros > Definição de Layout:

__Se__ a opção Recuperar Código de Serviço – Lei Complementar 116/03 estiver selecionada, recuperar a informação do campo cod\_serv\_lei\_116 da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Se__ a opção Recuperar Código Natureza de Serviço estiver selecionada, recuperar a informação do campo COD\_NAT\_SERV da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Senão__ recuperar a informação do campo Serviços, através da tela Serviços Msaf x Serviços Municipais\. Para os casos em que tiver mais de 1 parametrização com o mesmo Código do  Serviço Msaf e Código do Serviço Municipal, deverá ser recuperado a parametrização com a data mais atual\. 

__Tamanho do campo:__

Se a informação do campo ultrapassar de 10 caracteres, sistema deverá exibir a seguinte mensagem no log:  “Informação do campo Atividade ou Serviço Prestado ultrapassa 

o tamanho permitido\. Tamanho permitido para o campo é de até 10 caracteres\.”

OS3143

OS3143\-O

__RN28__

Informar se a pessoa citada no documento fiscal é física ou jurídica\.

1 – Física: gravar “1” caso o campo CPF\_CGC da tabela SAFX04 esteja preenchido com 11 números\.

2 – Jurídica: gravar “2” caso o campo CPF\_CGC da tabela SAFX04 esteja preenchido com 14 números\.

OS3143

__RN10__

S – Estabelecido: Gravar “S” quando o cod\_municipio da tabela safx04 correspondente à Pessoa Fis/Jur da nota fiscal for igual ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

N – Não Estabelecido: Gravar “N” quando o cod\_municipio da tabela safx04 correspondente à Pessoa Fis/Jur da nota fiscal for diferente ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

OS3143

__RN11__

Recuperar a informação do campo RAZAO\_SOCIAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN12__

Recuperar a informação do campo INSC\_MUNICIPAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado \(10 posições\)\.

OS3143

__RN13__

Recuperar os dois últimos dígitos da informação do campo INSC\_MUNICIPAL da tabela SAFX04 caso o campo possua mais de 10 dígitos\. Caso o campo não preencha todas as posições preencher o mesmo com espaços\.

OS3143

__RN14__

Recuperar a informação do campo CPF\_CGC da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN15__

S – Isento: gravar “S” quando no cadastro da Safx04 o campo “Inscrição Estadual” estiver escrito “ISENT%”\.

N – Não Isento: gravar “N” quando no cadastro da Safx04 o campo “Inscrição Estadual” estiver preenchido com números\.

OS3143

__RN16__

Recuperar a informação do campo INSC\_ESTADUAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.Tratar esta regra somente se RN15 for N\.

OS3143

__RN17__

Recuperar a informação do campo CEP da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN18__

Recuperar a informação do campo TP\_LOGRADOURO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN13__

Inserir espaços em branco até completar o campo\. 

OS3143

__RN20__

Recuperar a informação do campo ENDERECO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN21__

Recuperar a informação do campo COMPL\_ENDERECO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN22__

Recuperar a informação do campo NUM\_ENDERECO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN23__

Recuperar a informação do campo BAIRRO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN24__

Recuperar a informação do campo UF da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN25__

Recuperar a informação da descrição do município da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN08\-E__

\[ALTERADA – OS3143\]

__OBS: Regra para notas de entrada__

D – Dentro do Município: Gravar “D” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for o mesmo município cadastrado para o estabelecimento do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)

F – Fora do Município: Gravar “F” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for diferente do município cadastrado para o estabelecimento do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)

Caso o campo “Município ISS” do documento fiscal de serviço estiver vazio criar log de erro com a seguinte mensagem: “Para a nota fiscal \.\.\.\.\.\.\. \(demonstrar o número e código de fornecedor da nota fiscal\) Informar o código de Município ISS na capa da nota fiscal para definir o local de prestação do serviço\.”

OS3143

__RN48__

Campos: Indicador e alíquota de optante pelo Simples Nacional

\[ALTERADA – CH108506\]

Para os documentos fiscais de serviço \(SAFX07\) no cadastro de de PFJ\(SAFX04\):

Se o campo Enquadrado como Simples Nacional \-  IND\_SIMPLES\_NAC \(posição 43 da SAFX04\) estiver marcado como ‘S’ deve gravar ‘S’ no campo Indicador e recuperar o campo 

Alíquota ISS \- VLR\_ALIQ\_ISS \(posição 32 da safx 09\)

Senão, se o campo Enquadrado como Simples Nacional \-  IND\_SIMPLES\_NAC \(posição 43 da SAFX04\) estiver marcado como ‘N’ ou estiver vazio, não preencher os campos indicador e alíquota do arquivo, pois este campo não é obrigatório\.

OBS: Caso a nota fiscal possua mais de um item:

   Quando possuir mais de um item com códigos de serviço IGUAIS: neste caso, levar somente uma linha sumarizando os valores de  cada item, pois como se trata de somente uma natureza de serviço não há a necessidade de desmembrar os valores\.

  Quando possuir mais de um item com códigos de serviço DIFERENTES: neste caso, desmembrar uma linha para cada código de serviço, levando o valor do serviço de cada item e não o valor total da nota\. O campo que deverá ser utilizado é “valor total” do item de serviço

__\[EXCLUIDA\]__

Não preencher este campo\. Não é de preenchimento obrigatório\.Preencher com espaços\.

OS3143

CH108506

__LAYOUT GISS On Line Registro Serviço Tomado de Prestador Residente no Pais sem Nota Fiscal__

__RN30__

Gravar no campo “Identificação de Registro” o caracter fixo “P”\.

OS3143

__RN01\-C__

Recuperar somente notas fiscais utilizando o campo NUM\_DOCFIS da tabela SAFX07 para casos onde no cadastro de Pessoa Fis/Jur \(tabela safx04\) tiver o campo UF preenchido deferente de  “EX” e campo indicador de entrada ou saída deverá constar = “1”\. COD\_CLASS\_DOC\_FIS = “9 – Outros Documentos não escriturados” __E __COD\_DOCTO = “RPA”\. Campo ind\_tp\_servico <> 1 da tabela x2018\_servicos\.

 Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN03__

Recuperar a informação do campo DATA\_EMISSAO da tabela SAFX07\. A data deve ser informada no meio magnético no formato dd/mm/aaaa\.

OS3143

__RN04\-E__

Deve ser informado o tipo da nota fiscal\.

__\[EXCLUIDA\]__

6 – Pagto pelo Prestador: se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 455 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Prestador

__ALTERADA OS3585__

__6__ – Pagto pelo Prestador: gravar “6” 

__SE__ a UF \(COD\_ESTADO da tabela SAFX2097\) = ‘SP’ 

__E__ o código do município \(COD\_MUNIC\_MSAF da tabela SAFX2097\) = ‘48500’ 

__       E __o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação 

       de serviços – Município com o cód\_param = 455 

       __OU ENTÃO__ o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido 

       pelo prestador\.

__\*Para verficar o código do município da SAFX2097: __

O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS, deve se utilizar o código do município IBGE \(campo COD\_MUNIC\_MSAF\) correspondente\.

__1__ – Tributada: gravar “1” se não forem atendidas as condições abaixo \(de 2 a 8 – Excluindo a 6\)\.

__2__ – Cancelada: gravar “2” no meio magnético, quando o campo SITUACAO da tabela SAFX07 estiver preenchido com “S” \(na tela o flag “Sit\. Cancelado” estiver marcado\)\.

__5 –__ Retida: gravar “5” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 454 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Tomador

__4 –__ Isenta: gravar “4” no meio magnético, quando o campo 38 \(tributação ISS\) da tabela safx09 estiver preenchido com 2\- isento ou o campo IND\_CLASSE\_PFJ da SAFX04 estiver preenchido com 10 ou Se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 433\.

__7 –__ Imune: gravar “7” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 420 ou o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07\.

__8 –__ S\.Judicial: gravar “8” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 427 ou  o campo IND\_CLASSE\_PFJ da SAFX04 = “09” 

__3 –__ Anulada: não será tratada nessa OS\.

OS3143

OS3585

__RN05__

Recuperar a informação do campo VLR\_TOT da tabela SAFX09\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\. Não devem ser utilizados pontos ou vírgulas\. Exemplo: o valor 12,34 fica representado como:

000000001234

OS3143

__RN06__

\[ALTERADA – OS3143\-O\]

__Campo Código do Serviço/Atividade__

Verificar opção selecionada no menu Parâmetros > Definição de Layout:

__Se__ a opção Recuperar Código de Serviço – Lei Complementar 116/03 estiver selecionada, recuperar a informação do campo cod\_serv\_lei\_116 da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Se__ a opção Recuperar Código Natureza de Serviço estiver selecionada, recuperar a informação do campo COD\_NAT\_SERV da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Senão__ recuperar a informação do campo Serviços, através da tela Serviços Msaf x Serviços Municipais\. Para os casos em que tiver mais de 1 parametrização com o mesmo Código do  Serviço Msaf e Código do Serviço Municipal, deverá ser recuperado a parametrização com a data mais atual\. 

__Tamanho do campo:__

Se a informação do campo ultrapassar de 10 caracteres, sistema deverá exibir a seguinte mensagem no log:  “Informação do campo Atividade ou Serviço Prestado ultrapassa 

o tamanho permitido\. Tamanho permitido para o campo é de até 10 caracteres\.”

OS3143

OS3143\-O

__RN28__

Informar se a pessoa citada no documento fiscal é física ou jurídica\.

1 – Física: gravar “1” caso o campo CPF\_CGC da tabela SAFX04 esteja preenchido com 11 números\.

2 – Jurídica: gravar “2” caso o campo CPF\_CGC da tabela SAFX04 esteja preenchido com 14 números\.

OS3143

__RN10__

S – Estabelecido: Gravar “S” quando o cod\_municipio da tabela safx04 correspondente à Pessoa Fis/Jur da nota fiscal for igual ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

N – Não Estabelecido: Gravar “N” quando o cod\_municipio da tabela safx04 correspondente à Pessoa Fis/Jur da nota fiscal for diferente ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

OS3143

__RN11__

Recuperar a informação do campo RAZAO\_SOCIAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN12__

Recuperar a informação do campo INSC\_MUNICIPAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado \(10 posições\)\.

OS3143

__RN13__

Recuperar os dois últimos dígitos da informação do campo INSC\_MUNICIPAL da tabela SAFX04 caso o campo possua mais de 10 dígitos\. Caso o campo não preencha todas as posições preencher o mesmo com espaços\.

OS3143

__RN14__

Recuperar a informação do campo CPF\_CGC da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN15__

S – Isento: gravar “S” quando no cadastro da tabela safx04 o campo “Inscrição Estadual” estiver escrito “ISENT%”\.

N – Não Isento: gravar “N” quando no cadastro da tabela safx04 o campo “Inscrição Estadual” estiver preenchido com números\.

OS3143

__RN16__

Recuperar a informação do campo INSC\_ESTADUAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\. Tratar esta regra somente se RN15 for N\.

OS3143

__RN17__

Recuperar a informação do campo CEP da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN18__

Recuperar a informação do campo TP\_LOGRADOURO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN13__

Inserir espaços em branco até completar o campo\. 

OS3143

__RN20__

Recuperar a informação do campo ENDERECO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN21__

Recuperar a informação do campo COMPL\_ENDERECO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN22__

Recuperar a informação do campo NUM\_ENDERECO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN23__

Recuperar a informação do campo BAIRRO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN24__

Recuperar a informação do campo UF da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN25__

Recuperar a informação do campo descrição do município da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN08\-E__

\[ALTERADA – OS3143\]

__OBS: Regra para notas de entrada__

D – Dentro do Município: Gravar “D” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for o mesmo município cadastrado para o estabelecimento do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)

F – Fora do Município: Gravar “F” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for diferente do município cadastrado para o estabelecimento do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)

Caso o campo “Município ISS” do documento fiscal de serviço estiver vazio criar log de erro com a seguinte mensagem: “Para a nota fiscal \.\.\.\.\.\.\. \(demonstrar o número e código de fornecedor da nota fiscal\) Informar o código de Município ISS na capa da nota fiscal para definir o local de prestação do serviço\.”

OS3143

__RN48__

Campos: Indicador e alíquota de optante pelo Simples Nacional

\[ALTERADA – CH108506\]

Para os documentos fiscais de serviço \(SAFX07\) no cadastro de de PFJ\(SAFX04\):

Se o campo Enquadrado como Simples Nacional \-  IND\_SIMPLES\_NAC \(posição 43 da SAFX04\) estiver marcado como ‘S’ deve gravar ‘S’ no campo Indicador e recuperar o campo 

Alíquota ISS \- VLR\_ALIQ\_ISS \(posição 32 da safx 09\)

Senão, se o campo Enquadrado como Simples Nacional \-  IND\_SIMPLES\_NAC \(posição 43 da SAFX04\) estiver marcado como ‘N’ ou estiver vazio, não preencher os campos indicador e alíquota do arquivo, pois este campo não é obrigatório\.

OBS: Caso a nota fiscal possua mais de um item:

   Quando possuir mais de um item com códigos de serviço IGUAIS: neste caso, levar somente uma linha sumarizando os valores de  cada item, pois como se trata de somente uma natureza de serviço não há a necessidade de desmembrar os valores\.

  Quando possuir mais de um item com códigos de serviço DIFERENTES: neste caso, desmembrar uma linha para cada código de serviço, levando o valor do serviço de cada item e não o valor total da nota\. O campo que deverá ser utilizado é “valor total” do item de serviço

\[EXCLUIDA\]

Não preencher este campo\. Não é de preenchimento obrigatório\.Preencher com espaços\.

OS3143

CH108506

__                 __

__LAYOUT GISS On Line Registro Serviço Prestado Tomador Fora do Pais__

__RN00__

Gravar no campo “Identificação de Registro” o caracter fixo “C”\.

OS3143

__RN35__

Campo número da nota fiscal  para os registros prestados de Pessoa/fis/jur fora do país

Recuperar somente notas fiscais utilizando o campo NUM\_DOCFIS da tabela SAFX07 para casos onde no cadastro de Pessoa Fis/Jur \(tabela safx04\) tiver o campo UF preenchido com “EX” e 

Verificar no cadastro de Pessoa Fis/Jur da tabela safx04 se campo CPC\_CGC contém preenchidos menos de 14 dígitos, neste caso não carregar para este registro\.

Campo indicador de entrada ou saída da tabela safx07 deverá constar = “9”\. 

Campo ind\_tp\_servico <> 1 da tabela x2018\_servicos\. 

Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN02__

Recuperar a informação do campo SERIE\_DOCFIS da tabela SAFX07\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN03__

Recuperar a informação do campo DATA\_EMISSAO da tabela SAFX07\. A data deve ser informada no meio magnético no formato dd/mm/aaaa\.

OS3143

__RN04\-S__

Deve ser informado o tipo da nota fiscal\.

__\[EXCLUIDA\]__

6 – Pagto pelo Prestador: se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 455 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Prestador

__ALTERADA OS3585__

__6__ – Pagto pelo Prestador: gravar “6” 

__SE__ a UF \(COD\_ESTADO da tabela SAFX2097\) = ‘SP’ 

__E__ o código do município \(COD\_MUNIC\_MSAF da tabela SAFX2097\) = ‘48500’ 

__       E __o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – 

       Classificação de serviços – Município com o cód\_param = 455 

       __OU ENTÃO__ o campo “tipo de retenção” da tabela safx07 estiver preenchido com 

       Retido pelo prestador\.

__Obs:__ Caso o campo “Município ISS” do documento fiscal de serviço estiver vazio, considerar o município da tabela ESTABELECIMENTO

__\*Para verficar o código do município da SAFX2097: __

O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS, deve se utilizar o código do município IBGE \(campo COD\_MUNIC\_MSAF\) correspondente\.

__1__ – Tributada: gravar “1” se não forem atendidas as condições abaixo \(de 2 a 8 – Excluindo a 6\)\.

__2__ – Cancelada: gravar “2” no meio magnético, quando o campo SITUACAO da tabela SAFX07 estiver preenchido com “S” \(na tela o flag “Sit\. Cancelado” estiver marcado\)\.

__5 –__ Retida: gravar “5” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 454 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Tomador

__4 –__ Isenta: gravar “4” no meio magnético, quando o campo 38 \(tributação ISS\) da tabela safx09 estiver preenchido com 2\- isento ou o campo ind\_iss da tabela ESTABELECIMENTO estiver preenchido com 04\. Se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 433\.

__7 –__ Imune: gravar “7” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 420 ou o campo ind\_iss da tabela ESTABELECIMENTO estiver preenchido com 01\.

__8 –__ S\.Judicial: gravar “8” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 427 ou  o campo ind\_iss da tabela ESTABELECIMENTO estiver preenchido com 03\.

__3 –__ Anulada: não será tratada nessa OS\.

 ind\_iss da tabela ESTABELECIMENTO estiver preenchido com 03\.

OS3143

OS3585

__RN05__

Recuperar a informação do campo VLR\_TOT da tabela SAFX09\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\. Não devem ser utilizados pontos ou vírgulas\. Exemplo: o valor 12,34 fica representado como:

000000001234

OS3143

__RN06__

\[ALTERADA – OS3143\-O\]

__Campo Código do Serviço/Atividade__

Verificar opção selecionada no menu Parâmetros > Definição de Layout:

__Se__ a opção Recuperar Código de Serviço – Lei Complementar 116/03 estiver selecionada, recuperar a informação do campo cod\_serv\_lei\_116 da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Se__ a opção Recuperar Código Natureza de Serviço estiver selecionada, recuperar a informação do campo COD\_NAT\_SERV da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Senão__ recuperar a informação do campo Serviços, através da tela Serviços Msaf x Serviços Municipais\. Para os casos em que tiver mais de 1 parametrização com o mesmo Código do  Serviço Msaf e Código do Serviço Municipal, deverá ser recuperado a parametrização com a data mais atual\. 

__Tamanho do campo:__

Se a informação do campo ultrapassar de 10 caracteres, sistema deverá exibir a seguinte mensagem no log:  “Informação do campo Atividade ou Serviço Prestado ultrapassa 

o tamanho permitido\. Tamanho permitido para o campo é de até 10 caracteres\.”

OS3143

OS3143\-O

__RN09__

Gravar o número “2”\.

OS3143

__RN36__

Campo: Tomador estabelecido no município

Campo definido com valor “P”\.

OS3143

__RN37__

Campo: Sigla do Pais

Verificar campo sigla\_pais da tabela PAIS que está relacionada à tabela x07\_docto\_fiscal\.Pode ter espaços em branco\.

OS3143

__RN11__

Recuperar a informação do campo RAZAO\_SOCIAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN38__

Campo: Informações Gerais sobre a empresa

Completar com espaços até o limite 

indicado\.

OS3143

__RN08\-S__

\[ALTERADA – OS3143\]

__OBS:Regra para notas de saída:__

D – Dentro do Município: Gravar “D” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for o mesmo município cadastrado para o estabelecimento emissor do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. 

F – Fora do Município: Gravar “F” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for diferente do município cadastrado para o estabelecimento emissor do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. 

Caso o campo “Município ISS” do documento fiscal de serviço estiver vazio, considerar o município da tabela ESTABELECIMENTO, portanto do emitente e considerar = D e criar log de geração com a seguinte mensagem:

“Município com local de prestação de serviço não localizado na capa do documento fiscal\. Neste caso, para as saídas foi considerado o município do emitente da nota fiscal para definir o Local de Prestação de Serviço\.”

OS3143

__LAYOUT GISS On Line Registro Serviço Tomado de Prestador Residente fora   
do país sem nota fiscal__

__RN39__

__Campo: Indicador de Registro __

Gravar no campo “Identificação de Registro” o caracter fixo “P”\.

OS3143

__RN44__

__Campo: número da nota fiscal para serv\.tomado de prestador fora do país sem nota fiscal__

Recuperar somente notas fiscais utilizando o campo NUM\_DOCFIS da tabela SAFX07 para casos onde no cadastro de Pessoa Fis/Jur \(tabela safx04\) tiver o campo UF preenchido com “EX”, campo indicador de entrada ou saída deverá constar = “1” ou COD\_CLASS\_DOC\_FIS = “9 e campo ind\_tp\_servico <> 1 da tabela x2018\_servicos\.

 – Outros Documentos não escriturados” ou  COD\_DOCTO = “RPA”

Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN03__

Recuperar a informação do campo DATA\_EMISSAO da tabela SAFX07\. A data deve ser informada no meio magnético no formato dd/mm/aaaa\.

OS3143

__RN04\-E__

Deve ser informado o tipo da nota fiscal\.

__\[EXCLUIDA\]__

6 – Pagto pelo Prestador: se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 455 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Prestador

__ALTERADA OS3585__

__6__ – Pagto pelo Prestador: gravar “6” 

__SE__ a UF \(COD\_ESTADO da tabela SAFX2097\) = ‘SP’ 

__E__ o código do município \(COD\_MUNIC\_MSAF da tabela SAFX2097\) = ‘48500’ 

__       E __o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação 

       de serviços – Município com o cód\_param = 455 

       __OU ENTÃO__ o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido 

       pelo prestador\.

__\*Para verficar o código do município da SAFX2097: __

O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS, deve se utilizar o código do município IBGE \(campo COD\_MUNIC\_MSAF\) correspondente\.

__1__ – Tributada: gravar “1” se não forem atendidas as condições abaixo \(de 2 a 8 – Excluindo a 6\)\.

__2__ – Cancelada: gravar “2” no meio magnético, quando o campo SITUACAO da tabela SAFX07 estiver preenchido com “S” \(na tela o flag “Sit\. Cancelado” estiver marcado\)\.

__5 –__ Retida: gravar “5” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 454 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Tomador

__4 –__ Isenta: gravar “4” no meio magnético, quando o campo 38 \(tributação ISS\) da tabela safx09 estiver preenchido com 2\- isento ou o campo IND\_CLASSE\_PFJ da SAFX04 estiver preenchido com 10 ou Se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 433\.

__7 –__ Imune: gravar “7” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 420 ou o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07\.

__8 –__ S\.Judicial: gravar “8” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 427 ou  o campo IND\_CLASSE\_PFJ da SAFX04 = “09” 

__3 –__ Anulada: não será tratada nessa OS\.

OS3143

OS3585

__RN05__

Recuperar a informação do campo VLR\_TOT da tabela SAFX09\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\. Não devem ser utilizados pontos ou vírgulas\. Exemplo: o valor 12,34 fica representado como:

000000001234

OS3143

__RN06__

\[ALTERADA – OS3143\-O\]

__Campo Código do Serviço/Atividade__

Verificar opção selecionada no menu Parâmetros > Definição de Layout:

__Se__ a opção Recuperar Código de Serviço – Lei Complementar 116/03 estiver selecionada, recuperar a informação do campo cod\_serv\_lei\_116 da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Se__ a opção Recuperar Código Natureza de Serviço estiver selecionada, recuperar a informação do campo COD\_NAT\_SERV da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Senão__ recuperar a informação do campo Serviços, através da tela Serviços Msaf x Serviços Municipais\. Para os casos em que tiver mais de 1 parametrização com o mesmo Código do  Serviço Msaf e Código do Serviço Municipal, deverá ser recuperado a parametrização com a data mais atual\. 

__Tamanho do campo:__

Se a informação do campo ultrapassar de 10 caracteres, sistema deverá exibir a seguinte mensagem no log:  “Informação do campo Atividade ou Serviço Prestado ultrapassa 

o tamanho permitido\. Tamanho permitido para o campo é de até 10 caracteres\.”

OS3143

OS3143\-O

__RN28__

Informar se a pessoa citada no documento fiscal é física ou jurídica\.

1 – Física: gravar “1” caso o campo CPF\_CGC da tabela SAFX04 esteja preenchido com 11 números\.

2 – Jurídica: gravar “2” caso o campo CPF\_CGC da tabela SAFX04 esteja preenchido com 14 números\.

OS3143

__RN38__

Campo: Informações Gerais sobre a empresa

Completar com espaços até o limite 

indicado\.

OS3143

__RN11__

Recuperar a informação do campo RAZAO\_SOCIAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__LAYOUT GISS On Line Registro Serviço Tomado de Prestador Residente fora   
do país com nota fiscal__

__RN40__

__Campo: Indicador de Registro __

Gravar no campo “Identificação de Registro” o caracter fixo “F”\.

OS3143

__RN46__

__Campo: número da nota fiscal para Tomado de Prestador Residente fora __

__do país com nota fiscal__

Recuperar somente notas fiscais utilizando o campo NUM\_DOCFIS da tabela SAFX07 somente para casos onde no cadastro de Pessoa Fis/Jur \(tabela safx04\) tiver o campo UF preenchido com “EX” e campo indicador de entrada ou saída deverá constar = “1”\. Não considerar tipo de documento igual a RPA\. Campo ind\_tp\_servico <> 1 da tabela x2018\_servicos\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN02__

Recuperar a informação do campo SERIE\_DOCFIS da tabela SAFX07\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN03__

Recuperar a informação do campo DATA\_EMISSAO da tabela SAFX07\. A data deve ser informada no meio magnético no formato dd/mm/aaaa\.

OS3143

__RN04\-E__

Deve ser informado o tipo da nota fiscal\.

__\[EXCLUIDA\]__

6 – Pagto pelo Prestador: se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 455 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Prestador

__ALTERADA OS3585__

__6__ – Pagto pelo Prestador: gravar “6” 

__SE__ a UF \(COD\_ESTADO da tabela SAFX2097\) = ‘SP’ 

__E__ o código do município \(COD\_MUNIC\_MSAF da tabela SAFX2097\) = ‘48500’ 

__       E __o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação 

       de serviços – Município com o cód\_param = 455 

       __OU ENTÃO__ o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido 

       pelo prestador\.

__\*Para verficar o código do município da SAFX2097: __

O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS, deve se utilizar o código do município IBGE \(campo COD\_MUNIC\_MSAF\) correspondente\.

__1__ – Tributada: gravar “1” se não forem atendidas as condições abaixo \(de 2 a 8 – Excluindo a 6\)\.

__2__ – Cancelada: gravar “2” no meio magnético, quando o campo SITUACAO da tabela SAFX07 estiver preenchido com “S” \(na tela o flag “Sit\. Cancelado” estiver marcado\)\.

__5 –__ Retida: gravar “5” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 454 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Tomador

__4 –__ Isenta: gravar “4” no meio magnético, quando o campo 38 \(tributação ISS\) da tabela safx09 estiver preenchido com 2\- isento ou o campo IND\_CLASSE\_PFJ da SAFX04 estiver preenchido com 10 ou Se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 433\.

__7 –__ Imune: gravar “7” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 420 ou o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07\.

__8 –__ S\.Judicial: gravar “8” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 427 ou  o campo IND\_CLASSE\_PFJ da SAFX04 = “09” 

__3 –__ Anulada: não será tratada nessa OS\.

OS3143

OS3585

__RN05__

Recuperar a informação do campo VLR\_TOT da tabela SAFX09\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\. Não devem ser utilizados pontos ou vírgulas\. Exemplo: o valor 12,34 fica representado como:

000000001234

OS3143

__RN06__

\[ALTERADA – OS3143\-O\]

__Campo Código do Serviço/Atividade__

Verificar opção selecionada no menu Parâmetros > Definição de Layout:

__Se__ a opção Recuperar Código de Serviço – Lei Complementar 116/03 estiver selecionada, recuperar a informação do campo cod\_serv\_lei\_116 da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Se__ a opção Recuperar Código Natureza de Serviço estiver selecionada, recuperar a informação do campo COD\_NAT\_SERV da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Senão__ recuperar a informação do campo Serviços, através da tela Serviços Msaf x Serviços Municipais\. Para os casos em que tiver mais de 1 parametrização com o mesmo Código do  Serviço Msaf e Código do Serviço Municipal, deverá ser recuperado a parametrização com a data mais atual\. 

__Tamanho do campo:__

Se a informação do campo ultrapassar de 10 caracteres, sistema deverá exibir a seguinte mensagem no log:  “Informação do campo Atividade ou Serviço Prestado ultrapassa 

o tamanho permitido\. Tamanho permitido para o campo é de até 10 caracteres\.”

OS3143

OS3143\-O

__RN37__

Campo: Sigla do Pais

Verificar campo sigla\_pais da tabela PAIS que está relacionada à tabela x07\_docto\_fiscal\.Pode ter espaços em branco\.

OS3143

__RN11__

Recuperar a informação do campo RAZAO\_SOCIAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN38__

Campo: Informações Gerais sobre a empresa

Completar com espaços até o limite 

indicado\.

OS3143

__RN08\-E__

\[ALTERADA – OS3143\]

__OBS: Regra para notas de entrada__

D – Dentro do Município: Gravar “D” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for o mesmo município cadastrado para o estabelecimento do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)

F – Fora do Município: Gravar “F” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for diferente do município cadastrado para o estabelecimento do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)

Caso o campo “Município ISS” do documento fiscal de serviço estiver vazio criar log de erro com a seguinte mensagem: *“Para a nota fiscal \.\.\.\.\.\.\. \(demonstrar o número e código de fornecedor da nota fiscal\) Informar o código de Município ISS na capa da nota fiscal para definir o local de prestação do serviço\.”*

OS3143

__LAYOUT GISS On Line Registro Serviço Prestado Tomador Pessoa   
Física Sem Obra__

__RN41__

__Campo: Indicador de Registro __

Gravar no campo “Identificação de Registro” o caracter fixo “G”\.

OS3143

__RN45__

__Campo: número da nota fiscal para serv\.prestado tomador PF sem obra__

1\-Recuperar somente notas fiscais utilizando o campo NUM\_DOCFIS da tabela SAFX07 para casos onde no cadastro de Pessoa Fis/Jur \(tabela safx04\) tiver o campo indicador de entrada ou saída igual a “9”

2\-Verificar na tabela x04\_pessoa\_fis\_jur se o campo cpf\_cgc possui menos de 14 dígitos

3\-Considerar somente notas fiscais quando o campo 81 da safx07 \(cod\_canal\_distrib\) __não__ estiver preenchido

4\- campo ind\_tp\_servico = 1 da tabela x2018\_servicos

Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN02__

Recuperar a informação do campo SERIE\_DOCFIS da tabela SAFX07\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN03__

Recuperar a informação do campo DATA\_EMISSAO da tabela SAFX07\. A data deve ser informada no meio magnético no formato dd/mm/aaaa\.

OS3143

__RN04\-S__

Deve ser informado o tipo da nota fiscal\.

__\[EXCLUIDA\]__

6 – Pagto pelo Prestador: se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 455 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Prestador

__ALTERADA OS3585__

__6__ – Pagto pelo Prestador: gravar “6” 

__SE__ a UF \(COD\_ESTADO da tabela SAFX2097\) = ‘SP’ 

__E__ o código do município \(COD\_MUNIC\_MSAF da tabela SAFX2097\) = ‘48500’ 

__       E __o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação 

       de serviços – Município com o cód\_param = 455 

       __OU ENTÃO__ o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido 

       Pelo prestador\.

__Obs:__ Caso o campo “Município ISS” do documento fiscal de serviço estiver vazio, considerar o município da tabela ESTABELECIMENTO

__\*Para verficar o código do município da SAFX2097: __

O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS, deve se utilizar o código do município IBGE \(campo COD\_MUNIC\_MSAF\) correspondente\.

__1__ – Tributada: gravar “1” se não forem atendidas as condições abaixo \(de 2 a 8 – Excluindo a 6\)\.

__2__ – Cancelada: gravar “2” no meio magnético, quando o campo SITUACAO da tabela SAFX07 estiver preenchido com “S” \(na tela o flag “Sit\. Cancelado” estiver marcado\)\.

__5 –__ Retida: gravar “5” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 454 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Tomador

__4 –__ Isenta: gravar “4” no meio magnético, quando o campo 38 \(tributação ISS\) da tabela safx09 estiver preenchido com 2\- isento ou o campo ind\_iss da tabela ESTABELECIMENTO estiver preenchido com 04\. Se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 433\.

__7 –__ Imune: gravar “7” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 420 ou o campo ind\_iss da tabela ESTABELECIMENTO estiver preenchido com 01\.

__8 –__ S\.Judicial: gravar “8” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 427 ou  o campo ind\_iss da tabela ESTABELECIMENTO estiver preenchido com 03\.

__3 –__ Anulada: não será tratada nessa OS\.

OS3143

OS3585

__RN05__

Recuperar a informação do campo VLR\_TOT da tabela SAFX09\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\. Não devem ser utilizados pontos ou vírgulas\. Exemplo: o valor 12,34 fica representado como:

000000001234

OS3143

__RN06__

\[ALTERADA – OS3143\-O\]

__Campo Código do Serviço/Atividade__

Verificar opção selecionada no menu Parâmetros > Definição de Layout:

__Se__ a opção Recuperar Código de Serviço – Lei Complementar 116/03 estiver selecionada, recuperar a informação do campo cod\_serv\_lei\_116 da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Se__ a opção Recuperar Código Natureza de Serviço estiver selecionada, recuperar a informação do campo COD\_NAT\_SERV da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Senão__ recuperar a informação do campo Serviços, através da tela Serviços Msaf x Serviços Municipais\. Para os casos em que tiver mais de 1 parametrização com o mesmo Código do  Serviço Msaf e Código do Serviço Municipal, deverá ser recuperado a parametrização com a data mais atual\. 

__Tamanho do campo:__

Se a informação do campo ultrapassar de 10 caracteres, sistema deverá exibir a seguinte mensagem no log:  “Informação do campo Atividade ou Serviço Prestado ultrapassa 

o tamanho permitido\. Tamanho permitido para o campo é de até 10 caracteres\.”

OS3143

OS3143\-O

__RN42__

Gravar no campo “Identificação de Registro” o valor fixo “1”\.

OS3143

__RN08\-S__

\[ALTERADA – OS3143\]

__OBS:Regra para notas de saída:__

D – Dentro do Município: Gravar “D” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for o mesmo município cadastrado para o estabelecimento emissor do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. 

F – Fora do Município: Gravar “F” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for diferente do município cadastrado para o estabelecimento emissor do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. 

Caso o campo “Município ISS” do documento fiscal de serviço estiver vazio, considerar o município da tabela ESTABELECIMENTO, portanto do emitente e considerar = D e criar log de geração com a seguinte mensagem:

“Município com local de prestação de serviço não localizado na capa do documento fiscal\. Neste caso, para as saídas foi considerado o município do emitente da nota fiscal para definir o Local de Prestação de Serviço\.”

OS3143

__RN05__

Recuperar a informação do campo VLR\_TOT da tabela SAFX09\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\. Não devem ser utilizados pontos ou vírgulas\. Exemplo: o valor 12,34 fica representado como:

000000001234

OS3143

__RN48__

Campos: Indicador e alíquota de optante pelo Simples Nacional

\[ALTERADA – CH108506\]

Para os documentos fiscais de serviço \(SAFX07\) no cadastro de de PFJ\(SAFX04\):

Se o campo Enquadrado como Simples Nacional \-  IND\_SIMPLES\_NAC \(posição 43 da SAFX04\) estiver marcado como ‘S’ deve gravar ‘S’ no campo Indicador e recuperar o campo 

Alíquota ISS \- VLR\_ALIQ\_ISS \(posição 32 da safx 09\)

Senão, se o campo Enquadrado como Simples Nacional \-  IND\_SIMPLES\_NAC \(posição 43 da SAFX04\) estiver marcado como ‘N’ ou estiver vazio, não preencher os campos indicador e alíquota do arquivo, pois este campo não é obrigatório\.

OBS: Caso a nota fiscal possua mais de um item:

   Quando possuir mais de um item com códigos de serviço IGUAIS: neste caso, levar somente uma linha sumarizando os valores de  cada item, pois como se trata de somente uma natureza de serviço não há a necessidade de desmembrar os valores\.

  Quando possuir mais de um item com códigos de serviço DIFERENTES: neste caso, desmembrar uma linha para cada código de serviço, levando o valor do serviço de cada item e não o valor total da nota\. O campo que deverá ser utilizado é “valor total” do item de serviço

\[EXCLUIDA\]

Não preencher este campo\. Não é de preenchimento obrigatório\.Preencher com espaços\.

OS3143

CH108506

__LAYOUT GISS On Line Registro Serviço Prestado Tomador Pessoa   
Jurídica Sem Obra__

__RN41__

__Campo: Indicador de Registro __

Gravar no campo “Identificação de Registro” o caracter fixo “G”\.

OS3143

__RN47__

__Campo: número da nota fiscal para serv\.prestado tomador PJ sem obra__

1\-Recuperar somente notas fiscais utilizando o campo NUM\_DOCFIS da tabela SAFX07 para casos onde no cadastro de Pessoa Fis/Jur \(tabela safx04\) tiver o campo indicador de entrada ou saída igual a “9”

2\-Verificar na tabela x04\_pessoa\_fis\_jur se o campo cpf\_cgc possui 14 dígitos

3\- Considerar somente notas fiscais quando o campo 81 da safx07 \(cod\_canal\_distrib\) __não__ estiver preenchido 4\- Campo ind\_tp\_servico = 1 da tabela x2018\_servicos

Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN02__

Recuperar a informação do campo SERIE\_DOCFIS da tabela SAFX07\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN03__

Recuperar a informação do campo DATA\_EMISSAO da tabela SAFX07\. A data deve ser informada no meio magnético no formato dd/mm/aaaa\.

OS3143

__RN04\-S__

Deve ser informado o tipo da nota fiscal\.

__\[EXCLUIDA\]__

6 – Pagto pelo Prestador: se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 455 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Prestador

__ALTERADA OS3585__

__6__ – Pagto pelo Prestador: gravar “6” 

__SE__ a UF \(COD\_ESTADO da tabela SAFX2097\) = ‘SP’ 

__E__ o código do município \(COD\_MUNIC\_MSAF da tabela SAFX2097\) = ‘48500’ 

__       E __o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação 

       de serviços – Município com o cód\_param = 455 

       __OU ENTÃO__ o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido 

       Pelo prestador\.

__Obs:__ Caso o campo “Município ISS” do documento fiscal de serviço estiver vazio, considerar o município da tabela ESTABELECIMENTO

__\*Para verficar o código do município da SAFX2097: __

O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS, deve se utilizar o código do município IBGE \(campo COD\_MUNIC\_MSAF\) correspondente\.

__1__ – Tributada: gravar “1” se não forem atendidas as condições abaixo \(de 2 a 8 – Excluindo a 6\)\.

__2__ – Cancelada: gravar “2” no meio magnético, quando o campo SITUACAO da tabela SAFX07 estiver preenchido com “S” \(na tela o flag “Sit\. Cancelado” estiver marcado\)\.

__5 –__ Retida: gravar “5” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 454 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Tomador

__4 –__ Isenta: gravar “4” no meio magnético, quando o campo 38 \(tributação ISS\) da tabela safx09 estiver preenchido com 2\- isento ou o campo ind\_iss da tabela ESTABELECIMENTO estiver preenchido com 04\. Se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 433\.

__7 –__ Imune: gravar “7” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 420 ou o campo ind\_iss da tabela ESTABELECIMENTO estiver preenchido com 01\.

__8 –__ S\.Judicial: gravar “8” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 427 ou  o campo ind\_iss da tabela ESTABELECIMENTO estiver preenchido com 03\.

__3 –__ Anulada: não será tratada nessa OS\.

OS3143

OS3585

__RN05__

Recuperar a informação do campo VLR\_TOT da tabela SAFX09\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\. Não devem ser utilizados pontos ou vírgulas\. Exemplo: o valor 12,34 fica representado como:

000000001234

OS3143

__RN06__

\[ALTERADA – OS3143\-O\]

__Campo Código do Serviço/Atividade__

Verificar opção selecionada no menu Parâmetros > Definição de Layout:

__Se__ a opção Recuperar Código de Serviço – Lei Complementar 116/03 estiver selecionada, recuperar a informação do campo cod\_serv\_lei\_116 da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Se__ a opção Recuperar Código Natureza de Serviço estiver selecionada, recuperar a informação do campo COD\_NAT\_SERV da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Senão__ recuperar a informação do campo Serviços, através da tela Serviços Msaf x Serviços Municipais\. Para os casos em que tiver mais de 1 parametrização com o mesmo Código do  Serviço Msaf e Código do Serviço Municipal, deverá ser recuperado a parametrização com a data mais atual\. 

__Tamanho do campo:__

Se a informação do campo ultrapassar de 10 caracteres, sistema deverá exibir a seguinte mensagem no log:  “Informação do campo Atividade ou Serviço Prestado ultrapassa 

o tamanho permitido\. Tamanho permitido para o campo é de até 10 caracteres\.”

OS3143

OS3143\-O

__RN42__

Gravar no campo “Identificação de Registro” o valor fixo “2”\.

OS3143

__RN10__

S – Estabelecido: Gravar “S” quando o cod\_municipio da tabela safx04 correspondente à Pessoa Fis/Jur da nota fiscal for igual ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

N – Não Estabelecido: Gravar “N” quando o cod\_municipio da tabela safx04 correspondente à Pessoa Fis/Jur da nota fiscal for diferente ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

OS3143

__RN11__

Recuperar a informação do campo RAZAO\_SOCIAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN12__

Recuperar a informação do campo INSC\_MUNICIPAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado \(10 posições\)\.

OS3143

__RN13__

Recuperar os dois últimos dígitos da informação do campo INSC\_MUNICIPAL da tabela SAFX04 caso o campo possua mais de 10 dígitos\. Caso o campo não preencha todas as posições preencher o mesmo com espaços\.

OS3143

__RN14__

Recuperar a informação do campo CPF\_CGC da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN15__

S – Isento: gravar “S” quando no cadastro da tabela safx04 o campo “Inscrição Estadual” estiver escrito “ISENT%”\.

N – Não Isento: gravar “N” quando no cadastro da tabela safx04 o campo “Inscrição Estadual” estiver preenchido com números\.

OS3143

__RN16__

Recuperar a informação do campo INSC\_ESTADUAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\. Tratar esta regra somente se RN15 for N\.

OS3143

__RN17__

Recuperar a informação do campo CEP da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN18__

Recuperar a informação do campo TP\_LOGRADOURO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN20__

Recuperar a informação do campo ENDERECO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN21__

Recuperar a informação do campo COMPL\_ENDERECO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN22__

Recuperar a informação do campo NUM\_ENDERECO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN23__

Recuperar a informação do campo BAIRRO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN24__

Recuperar a informação do campo UF da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN25__

Recuperar a informação da descrição do município da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN08\-S__

\[ALTERADA – OS3143\]

__OBS:Regra para notas de saída:__

D – Dentro do Município: Gravar “D” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for o mesmo município cadastrado para o estabelecimento emissor do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. 

F – Fora do Município: Gravar “F” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for diferente do município cadastrado para o estabelecimento emissor do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. 

Caso o campo “Município ISS” do documento fiscal de serviço estiver vazio, considerar o município da tabela ESTABELECIMENTO, portanto do emitente e considerar = D e criar log de geração com a seguinte mensagem:

“Município com local de prestação de serviço não localizado na capa do documento fiscal\. Neste caso, para as saídas foi considerado o município do emitente da nota fiscal para definir o Local de Prestação de Serviço\.”

OS3143

__RN49__

Campo: Base de Cálculo

1. Carregar o campo base\_iss \(campo 39\) da tabela x09\_itens\_serv se estiver preenchido 
2. Caso o campo anterior não estiver preenchido, carregar o campo vlr\_base para cod\_tributo = ISS da tabela x07\_base\_docfis
3. Caso nenhuma das condições anteriores sejam atendidas carregar o campo com espaços em branco

OS3143

__RN48__

Campos: Indicador e alíquota de optante pelo Simples Nacional

\[ALTERADA – CH108506\]

Para os documentos fiscais de serviço \(SAFX07\) no cadastro de de PFJ\(SAFX04\):

Se o campo Enquadrado como Simples Nacional \-  IND\_SIMPLES\_NAC \(posição 43 da SAFX04\) estiver marcado como ‘S’ deve gravar ‘S’ no campo Indicador e recuperar o campo 

Alíquota ISS \- VLR\_ALIQ\_ISS \(posição 32 da safx 09\)

Senão, se o campo Enquadrado como Simples Nacional \-  IND\_SIMPLES\_NAC \(posição 43 da SAFX04\) estiver marcado como ‘N’ ou estiver vazio, não preencher os campos indicador e alíquota do arquivo, pois este campo não é obrigatório\.

OBS: Caso a nota fiscal possua mais de um item:

   Quando possuir mais de um item com códigos de serviço IGUAIS: neste caso, levar somente uma linha sumarizando os valores de  cada item, pois como se trata de somente uma natureza de serviço não há a necessidade de desmembrar os valores\.

  Quando possuir mais de um item com códigos de serviço DIFERENTES: neste caso, desmembrar uma linha para cada código de serviço, levando o valor do serviço de cada item e não o valor total da nota\. O campo que deverá ser utilizado é “valor total” do item de serviço

\[EXCLUIDA\]

Não preencher este campo\. Não é de preenchimento obrigatório\.Preencher com espaços\.

OS3143

CH108506

__LAYOUT GISS On Line Registro Serviço Tomado de Prestador Residente no país com nota fiscal sem obra__

__RN50__

__Campo: Indicador de Registro __

Gravar no campo “Identificação de Registro” o caracter fixo “I”\.

OS3143

__RN51__

__Campo: número da nota fiscal para serv\. Tomado de Prestador Residente no país com nota fiscal sem obra__

1\-Recuperar somente notas fiscais utilizando o campo NUM\_DOCFIS da tabela SAFX07 para casos onde no cadastro de Pessoa Fis/Jur \(tabela safx04\) tiver o campo indicador de entrada ou saída igual a “1”

2\- Não considerar tipo de documento igual a RPA

3\-Verificar na tabela x04\_pessoa\_fis\_jur se o campo UF for diferente de “EX”

4\- Considerar somente notas fiscais quando o Campo 81 da safx07 \(cod\_canal\_distrib\)__ não__ estiver preenchido

5\- Campo ind\_tp\_servico = 1 da tabela x2018\_servicos

Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN02__

Recuperar a informação do campo SERIE\_DOCFIS da tabela SAFX07\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN03__

Recuperar a informação do campo DATA\_EMISSAO da tabela SAFX07\. A data deve ser informada no meio magnético no formato dd/mm/aaaa\.

OS3143

__RN04\-E__

Deve ser informado o tipo da nota fiscal\.

__\[EXCLUIDA\]__

6 – Pagto pelo Prestador: se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 455 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Prestador

__ALTERADA OS3585__

__6__ – Pagto pelo Prestador: gravar “6” 

__SE__ a UF \(COD\_ESTADO da tabela SAFX2097\) = ‘SP’ 

__E__ o código do município \(COD\_MUNIC\_MSAF da tabela SAFX2097\) = ‘48500’ 

__       E __o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação 

       de serviços – Município com o cód\_param = 455 

       __OU ENTÃO__ o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido 

       pelo prestador\.

__\*Para verficar o código do município da SAFX2097: __

O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS, deve se utilizar o código do município IBGE \(campo COD\_MUNIC\_MSAF\) correspondente\.

__1__ – Tributada: gravar “1” se não forem atendidas as condições abaixo \(de 2 a 8 – Excluindo a 6\)\.

__2__ – Cancelada: gravar “2” no meio magnético, quando o campo SITUACAO da tabela SAFX07 estiver preenchido com “S” \(na tela o flag “Sit\. Cancelado” estiver marcado\)\.

__5 –__ Retida: gravar “5” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 454 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Tomador

__4 –__ Isenta: gravar “4” no meio magnético, quando o campo 38 \(tributação ISS\) da tabela safx09 estiver preenchido com 2\- isento ou o campo IND\_CLASSE\_PFJ da SAFX04 estiver preenchido com 10 ou Se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 433\.

__7 –__ Imune: gravar “7” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 420 ou o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07\.

__8 –__ S\.Judicial: gravar “8” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 427 ou  o campo IND\_CLASSE\_PFJ da SAFX04 = “09” 

__3 –__ Anulada: não será tratada nessa OS\.

OS3143

OS3585

__RN05__

Recuperar a informação do campo VLR\_TOT da tabela SAFX09\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\. Não devem ser utilizados pontos ou vírgulas\. Exemplo: o valor 12,34 fica representado como:

000000001234

OS3143

__RN06__

\[ALTERADA – OS3143\-O\]

__Campo Código do Serviço/Atividade__

Verificar opção selecionada no menu Parâmetros > Definição de Layout:

__Se__ a opção Recuperar Código de Serviço – Lei Complementar 116/03 estiver selecionada, recuperar a informação do campo cod\_serv\_lei\_116 da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Se__ a opção Recuperar Código Natureza de Serviço estiver selecionada, recuperar a informação do campo COD\_NAT\_SERV da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Senão__ recuperar a informação do campo Serviços, através da tela Serviços Msaf x Serviços Municipais\. Para os casos em que tiver mais de 1 parametrização com o mesmo Código do  Serviço Msaf e Código do Serviço Municipal, deverá ser recuperado a parametrização com a data mais atual\. 

__Tamanho do campo:__

Se a informação do campo ultrapassar de 10 caracteres, sistema deverá exibir a seguinte mensagem no log:  “Informação do campo Atividade ou Serviço Prestado ultrapassa 

o tamanho permitido\. Tamanho permitido para o campo é de até 10 caracteres\.”

OS3143

OS3143\-O

__RN42__

Se o campo CNPJ da tabela x04\_pessoa\_fis\_jur estiver preenchido com 14 dígitos preencher com "2"\.  
Se o campo CNPJ da tabela x04\_pessoa\_fis\_jur estiver preenchido com menos de 14 dígitos preencher com "1"\.

OS3143

__RN10__

S – Estabelecido: Gravar “S” quando o cod\_municipio da tabela safx04 correspondente à Pessoa Fis/Jur da nota fiscal for igual ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

N – Não Estabelecido: Gravar “N” quando o cod\_municipio da tabela safx04 correspondente à Pessoa Fis/Jur da nota fiscal for diferente ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

OS3143

__RN11__

Recuperar a informação do campo RAZAO\_SOCIAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN12__

Recuperar a informação do campo INSC\_MUNICIPAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado \(10 posições\)\.

OS3143

__RN13__

Recuperar os dois últimos dígitos da informação do campo INSC\_MUNICIPAL da tabela SAFX04 caso o campo possua mais de 10 dígitos\. Caso o campo não preencha todas as posições preencher o mesmo com espaços\.

OS3143

__RN14__

Recuperar a informação do campo CPF\_CGC da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN15__

S – Isento: gravar “S” quando no cadastro da tabela safx04 o campo “Inscrição Estadual” estiver escrito “ISENT%”\.

N – Não Isento: gravar “N” quando no cadastro da tabela safx04 o campo “Inscrição Estadual” estiver preenchido com números\.

OS3143

__RN16__

Recuperar a informação do campo INSC\_ESTADUAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\. Tratar esta regra somente se RN15 for N\.

OS3143

__RN17__

Recuperar a informação do campo CEP da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN18__

Recuperar a informação do campo TP\_LOGRADOURO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN20__

Recuperar a informação do campo ENDERECO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN21__

Recuperar a informação do campo COMPL\_ENDERECO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN22__

Recuperar a informação do campo NUM\_ENDERECO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN23__

Recuperar a informação do campo BAIRRO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN24__

Recuperar a informação do campo UF da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN25__

Recuperar a informação da descrição do município da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN08\-E__

\[ALTERADA – OS3143\]

__OBS: Regra para notas de entrada__

D – Dentro do Município: Gravar “D” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for o mesmo município cadastrado para o estabelecimento do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)

F – Fora do Município: Gravar “F” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for diferente do município cadastrado para o estabelecimento do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)

Caso o campo “Município ISS” do documento fiscal de serviço estiver vazio criar log de erro com a seguinte mensagem: “Para a nota fiscal \.\.\.\.\.\.\. \(demonstrar o número e código de fornecedor da nota fiscal\) Informar o código de Município ISS na capa da nota fiscal para definir o local de prestação do serviço\.”

OS3143

__RN49__

Campo: Base de Cálculo

1. Carregar o campo base\_iss \(campo 39\) da tabela x09\_itens\_serv se estiver preenchido 
2. Caso o campo anterior não estiver preenchido, carregar o campo vlr\_base para cod\_tributo = ISS da tabela x07\_base\_docfis
3. Caso nenhuma das condições anteriores sejam atendidas carregar o campo com espaços em branco

OS3143

__RN48__

Campos: Indicador e alíquota de optante pelo Simples Nacional

\[ALTERADA – CH108506\]

Para os documentos fiscais de serviço \(SAFX07\) no cadastro de de PFJ\(SAFX04\):

Se o campo Enquadrado como Simples Nacional \-  IND\_SIMPLES\_NAC \(posição 43 da SAFX04\) estiver marcado como ‘S’ deve gravar ‘S’ no campo Indicador e recuperar o campo 

Alíquota ISS \- VLR\_ALIQ\_ISS \(posição 32 da safx 09\)

Senão, se o campo Enquadrado como Simples Nacional \-  IND\_SIMPLES\_NAC \(posição 43 da SAFX04\) estiver marcado como ‘N’ ou estiver vazio, não preencher os campos indicador e alíquota do arquivo, pois este campo não é obrigatório\.

OBS: Caso a nota fiscal possua mais de um item:

   Quando possuir mais de um item com códigos de serviço IGUAIS: neste caso, levar somente uma linha sumarizando os valores de  cada item, pois como se trata de somente uma natureza de serviço não há a necessidade de desmembrar os valores\.

  Quando possuir mais de um item com códigos de serviço DIFERENTES: neste caso, desmembrar uma linha para cada código de serviço, levando o valor do serviço de cada item e não o valor total da nota\. O campo que deverá ser utilizado é “valor total” do item de serviço

\[EXCLUÍDA\]

Não preencher este campo\. Não é de preenchimento obrigatório\.Preencher com espaços\.

OS3143

CH108506

__LAYOUT GISS On Line Registro Serviço Prestado para tomador Pessoa Física com Obra__

__RN62__

__Campo: Indicador de Registro __

Gravar no campo “Identificação de Registro” o caracter fixo “X”\.

OS3143

__RN02__

Recuperar a informação do campo SERIE\_DOCFIS da tabela SAFX07\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN52__

Campo: número da nota fiscal para Serviço Prestado para tomador Pessoa Física com Obra

1\-Recuperar somente notas fiscais utilizando o campo NUM\_DOCFIS da tabela SAFX07 para casos onde no cadastro de Pessoa Fis/Jur \(tabela safx04\) tiver o campo indicador de entrada ou saída igual a “9”

2\-Verificar na tabela x04\_pessoa\_fis\_jur se o campo cpf\_cgc possui menos de 14 dígitos

3\-Considerar somente notas fiscais com o Campo 81 da safx07 \(cod\_canal\_distrib\) 

4\- Considerar preenchido campo ind\_tp\_servico = 1 da tabela x2018\_servicos

Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN03__

Recuperar a informação do campo DATA\_EMISSAO da tabela SAFX07\. A data deve ser informada no meio magnético no formato dd/mm/aaaa\.

OS3143

__RN04\-S__

Deve ser informado o tipo da nota fiscal\.

__\[EXCLUIDA\]__

6 – Pagto pelo Prestador: se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 455 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Prestador

__ALTERADA OS3585__

__6__ – Pagto pelo Prestador: gravar “6” 

__SE__ a UF \(COD\_ESTADO da tabela SAFX2097\) = ‘SP’ 

__E__ o código do município \(COD\_MUNIC\_MSAF da tabela SAFX2097\) = ‘48500’ 

__       E __o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação 

       de serviços – Município com o cód\_param = 455 

       __OU ENTÃO__ o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido 

       Pelo prestador\.

__Obs:__ Caso o campo “Município ISS” do documento fiscal de serviço estiver vazio, considerar o município da tabela ESTABELECIMENTO

__\*Para verficar o código do município da SAFX2097: __

O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS, deve se utilizar o código do município IBGE \(campo COD\_MUNIC\_MSAF\) correspondente\.

__1__ – Tributada: gravar “1” se não forem atendidas as condições abaixo \(de 2 a 8 – Excluindo a 6\)\.

__2__ – Cancelada: gravar “2” no meio magnético, quando o campo SITUACAO da tabela SAFX07 estiver preenchido com “S” \(na tela o flag “Sit\. Cancelado” estiver marcado\)\.

__5 –__ Retida: gravar “5” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 454 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Tomador

__4 –__ Isenta: gravar “4” no meio magnético, quando o campo 38 \(tributação ISS\) da tabela safx09 estiver preenchido com 2\- isento ou o campo ind\_iss da tabela ESTABELECIMENTO estiver preenchido com 04\. Se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 433\.

__7 –__ Imune: gravar “7” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 420 ou o campo ind\_iss da tabela ESTABELECIMENTO estiver preenchido com 01\.

__8 –__ S\.Judicial: gravar “8” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 427 ou  o campo ind\_iss da tabela ESTABELECIMENTO estiver preenchido com 03\.

__3 –__ Anulada: não será tratada nessa OS\.

OS3143

OS3585

__RN05__

Recuperar a informação do campo VLR\_TOT da tabela SAFX09\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\. Não devem ser utilizados pontos ou vírgulas\. Exemplo: o valor 12,34 fica representado como:

000000001234

OS3143

__RN06__

\[ALTERADA – OS3143\-O\]

__Campo Código do Serviço/Atividade__

Verificar opção selecionada no menu Parâmetros > Definição de Layout:

__Se__ a opção Recuperar Código de Serviço – Lei Complementar 116/03 estiver selecionada, recuperar a informação do campo cod\_serv\_lei\_116 da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Se__ a opção Recuperar Código Natureza de Serviço estiver selecionada, recuperar a informação do campo COD\_NAT\_SERV da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Senão__ recuperar a informação do campo Serviços, através da tela Serviços Msaf x Serviços Municipais\. Para os casos em que tiver mais de 1 parametrização com o mesmo Código do  Serviço Msaf e Código do Serviço Municipal, deverá ser recuperado a parametrização com a data mais atual\. 

__Tamanho do campo:__

Se a informação do campo ultrapassar de 10 caracteres, sistema deverá exibir a seguinte mensagem no log:  “Informação do campo Atividade ou Serviço Prestado ultrapassa 

o tamanho permitido\. Tamanho permitido para o campo é de até 10 caracteres\.”

OS3143

OS3143\-O

__RN42__

Gravar no campo “Identificação de Registro” o valor fixo “1”\.

OS3143

__RN08\-S__

\[ALTERADA – OS3143\]

__OBS:Regra para notas de saída:__

D – Dentro do Município: Gravar “D” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for o mesmo município cadastrado para o estabelecimento emissor do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. 

F – Fora do Município: Gravar “F” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for diferente do município cadastrado para o estabelecimento emissor do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. 

Caso o campo “Município ISS” do documento fiscal de serviço estiver vazio, considerar o município da tabela ESTABELECIMENTO, portanto do emitente e considerar = D e criar log de geração com a seguinte mensagem:

“Município com local de prestação de serviço não localizado na capa do documento fiscal\. Neste caso, para as saídas foi considerado o município do emitente da nota fiscal para definir o Local de Prestação de Serviço\.”

OS3143

__RN49__

Campo: Base de Cálculo

1. Carregar o campo base\_iss \(campo 39\) da tabela x09\_itens\_serv se estiver preenchido 
2. Caso o campo anterior não estiver preenchido, carregar o campo vlr\_base para cod\_tributo = ISS da tabela x07\_base\_docfis
3. Caso nenhuma das condições anteriores sejam atendidas carregar o campo com espaços em branco

OS3143

__RN53__

Campo: Código da obra

Verificar Campo 81 da safx07 cod\_canal\_distrib

Alinhar o código da obra à esquerda e preencher os espaços restantes com espaços\.

OS3143

__LAYOUT GISS On Line Registro Serviço Prestado para tomador Pessoa Jurídica com Obra__

__RN62__

__Campo: Indicador de Registro __

Gravar no campo “Identificação de Registro” o caracter fixo “X”\.

OS3143

__RN54__

__Campo: número da nota fiscal para serv\.prestado Prestado para tomador Pessoa Jurídica com Obra__

1\-Recuperar somente notas fiscais utilizando o campo NUM\_DOCFIS da tabela SAFX07 para casos onde no cadastro de Pessoa Fis/Jur \(tabela safx04\) tiver o campo indicador de entrada ou saída igual a “9”

2\-Verificar na tabela x04\_pessoa\_fis\_jur se o campo cpf\_cgc possui 14 dígitos

3\- Considerar somente notas fiscais com o Campo 81 da safx07 \(cod\_canal\_distrib\) preenchido

4\- campo ind\_tp\_servico = 1 da tabela x2018\_servicos

Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN02__

Recuperar a informação do campo SERIE\_DOCFIS da tabela SAFX07\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN03__

Recuperar a informação do campo DATA\_EMISSAO da tabela SAFX07\. A data deve ser informada no meio magnético no formato dd/mm/aaaa\.

OS3143

__RN04\-S__

Deve ser informado o tipo da nota fiscal\.

__\[EXCLUIDA\]__

6 – Pagto pelo Prestador: se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 455 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Prestador

__ALTERADA OS3585__

__6__ – Pagto pelo Prestador: gravar “6” 

__SE__ a UF \(COD\_ESTADO da tabela SAFX2097\) = ‘SP’ 

__E__ o código do município \(COD\_MUNIC\_MSAF da tabela SAFX2097\) = ‘48500’ 

__       E __o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação 

       de serviços – Município com o cód\_param = 455 

       __OU ENTÃO__ o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido 

       Pelo prestador\.

__Obs:__ Caso o campo “Município ISS” do documento fiscal de serviço estiver vazio, considerar o município da tabela ESTABELECIMENTO

__\*Para verficar o código do município da SAFX2097: __

O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS, deve se utilizar o código do município IBGE \(campo COD\_MUNIC\_MSAF\) correspondente\.

__1__ – Tributada: gravar “1” se não forem atendidas as condições abaixo \(de 2 a 8 – Excluindo a 6\)\.

__2__ – Cancelada: gravar “2” no meio magnético, quando o campo SITUACAO da tabela SAFX07 estiver preenchido com “S” \(na tela o flag “Sit\. Cancelado” estiver marcado\)\.

__5 –__ Retida: gravar “5” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 454 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Tomador

__4 –__ Isenta: gravar “4” no meio magnético, quando o campo 38 \(tributação ISS\) da tabela safx09 estiver preenchido com 2\- isento ou o campo ind\_iss da tabela ESTABELECIMENTO estiver preenchido com 04\. Se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 433\.

__7 –__ Imune: gravar “7” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 420 ou o campo ind\_iss da tabela ESTABELECIMENTO estiver preenchido com 01\.

__8 –__ S\.Judicial: gravar “8” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 427 ou  o campo ind\_iss da tabela ESTABELECIMENTO estiver preenchido com 03\.

__3 –__ Anulada: não será tratada nessa OS\.

OS3143

OS3585

__RN05__

Recuperar a informação do campo VLR\_TOT da tabela SAFX09\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\. Não devem ser utilizados pontos ou vírgulas\. Exemplo: o valor 12,34 fica representado como:

000000001234

OS3143

__RN06__

\[ALTERADA – OS3143\-O\]

__Campo Código do Serviço/Atividade__

Verificar opção selecionada no menu Parâmetros > Definição de Layout:

__Se__ a opção Recuperar Código de Serviço – Lei Complementar 116/03 estiver selecionada, recuperar a informação do campo cod\_serv\_lei\_116 da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Se__ a opção Recuperar Código Natureza de Serviço estiver selecionada, recuperar a informação do campo COD\_NAT\_SERV da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Senão__ recuperar a informação do campo Serviços, através da tela Serviços Msaf x Serviços Municipais\. Para os casos em que tiver mais de 1 parametrização com o mesmo Código do  Serviço Msaf e Código do Serviço Municipal, deverá ser recuperado a parametrização com a data mais atual\. 

__Tamanho do campo:__

Se a informação do campo ultrapassar de 10 caracteres, sistema deverá exibir a seguinte mensagem no log:  “Informação do campo Atividade ou Serviço Prestado ultrapassa 

o tamanho permitido\. Tamanho permitido para o campo é de até 10 caracteres\.”

OS3143

OS3143\-O

__RN42__

Gravar no campo “Identificação de Registro” o valor fixo “2”\.

OS3143

__RN10__

S – Estabelecido: Gravar “S” quando o cod\_municipio da tabela safx04 correspondente à Pessoa Fis/Jur da nota fiscal for igual ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

N – Não Estabelecido: Gravar “N” quando o cod\_municipio da tabela safx04 correspondente à Pessoa Fis/Jur da nota fiscal for diferente ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

OS3143

__RN11__

Recuperar a informação do campo RAZAO\_SOCIAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN12__

Recuperar a informação do campo INSC\_MUNICIPAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado \(10 posições\)\.

OS3143

__RN13__

Recuperar os dois últimos dígitos da informação do campo INSC\_MUNICIPAL da tabela SAFX04 caso o campo possua mais de 10 dígitos\. Caso o campo não preencha todas as posições preencher o mesmo com espaços\.

OS3143

__RN14__

Recuperar a informação do campo CPF\_CGC da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN15__

S – Isento: gravar “S” quando no cadastro da tabela safx04 o campo “Inscrição Estadual” estiver escrito “ISENT%”\.

N – Não Isento: gravar “N” quando no cadastro da tabela safx04 o campo “Inscrição Estadual” estiver preenchido com números\.

OS3143

__RN16__

Recuperar a informação do campo INSC\_ESTADUAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\. Tratar esta regra somente se RN15 for N\.

OS3143

__RN17__

Recuperar a informação do campo CEP da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN18__

Recuperar a informação do campo TP\_LOGRADOURO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN20__

Recuperar a informação do campo ENDERECO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN21__

Recuperar a informação do campo COMPL\_ENDERECO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN22__

Recuperar a informação do campo NUM\_ENDERECO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN23__

Recuperar a informação do campo BAIRRO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN24__

Recuperar a informação do campo UF da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN25__

Recuperar a informação da descrição do município da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN08\-S__

\[ALTERADA – OS3143\]

__OBS:Regra para notas de saída:__

D – Dentro do Município: Gravar “D” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for o mesmo município cadastrado para o estabelecimento emissor do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. 

F – Fora do Município: Gravar “F” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for diferente do município cadastrado para o estabelecimento emissor do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. 

Caso o campo “Município ISS” do documento fiscal de serviço estiver vazio, considerar o município da tabela ESTABELECIMENTO, portanto do emitente e considerar = D e criar log de geração com a seguinte mensagem:

“Município com local de prestação de serviço não localizado na capa do documento fiscal\. Neste caso, para as saídas foi considerado o município do emitente da nota fiscal para definir o Local de Prestação de Serviço\.” 

OS3143

__RN49__

Campo: Base de Cálculo

1. Carregar o campo base\_iss \(campo 39\) da tabela x09\_itens\_serv se estiver preenchido 
2. Caso o campo anterior não estiver preenchido, carregar o campo vlr\_base para cod\_tributo = ISS da tabela x07\_base\_docfis
3. Caso nenhuma das condições anteriores sejam atendidas carregar o campo com espaços em branco

OS3143

__RN53__

Campo: Código da obra

Verificar Campo 81 da safx07 cod\_canal\_distrib

Alinhar o código da obra à esquerda e preencher os espaços restantes com espaços\.

OS3143

__LAYOUT GISS On Line Registro Serviço Tomado de Prestador Residente no país com nota fiscal com obra__

__RN55__

__Campo: Indicador de Registro __

Gravar no campo “Identificação de Registro” o caracter fixo “H”\.

OS3143

__RN56__

__Campo: número da nota fiscal para serv\. Tomado de Prestador Residente no país com nota fiscal com obra__

1\-Recuperar somente notas fiscais utilizando o campo NUM\_DOCFIS da tabela SAFX07 para casos onde no cadastro de Pessoa Fis/Jur \(tabela safx04\) tiver o campo indicador de entrada ou saída igual a “1”

2\- Não considerar tipo de documento igual a RPA

3\-Verificar na tabela x04\_pessoa\_fis\_jur se o campo UF for diferente de “EX”

4\- Considerar somente notas fiscais com o Campo 81 da safx07 \(cod\_canal\_distrib\) preenchido

5\- campo ind\_tp\_servico = 1 da tabela x2018\_servicos

Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN02__

Recuperar a informação do campo SERIE\_DOCFIS da tabela SAFX07\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN03__

Recuperar a informação do campo DATA\_EMISSAO da tabela SAFX07\. A data deve ser informada no meio magnético no formato dd/mm/aaaa\.

OS3143

__RN04\-E__

Deve ser informado o tipo da nota fiscal\.

__\[EXCLUIDA\]__

6 – Pagto pelo Prestador: se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 455 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Prestador

__ALTERADA OS3585__

__6__ – Pagto pelo Prestador: gravar “6” 

__SE__ a UF \(COD\_ESTADO da tabela SAFX2097\) = ‘SP’ 

__E__ o código do município \(COD\_MUNIC\_MSAF da tabela SAFX2097\) = ‘48500’ 

__       E __o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação 

       de serviços – Município com o cód\_param = 455 

       __OU ENTÃO__ o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido 

       pelo prestador\.

__\*Para verficar o código do município da SAFX2097: __

O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS, deve se utilizar o código do município IBGE \(campo COD\_MUNIC\_MSAF\) correspondente\.

__1__ – Tributada: gravar “1” se não forem atendidas as condições abaixo \(de 2 a 8 – Excluindo a 6\)\.

__2__ – Cancelada: gravar “2” no meio magnético, quando o campo SITUACAO da tabela SAFX07 estiver preenchido com “S” \(na tela o flag “Sit\. Cancelado” estiver marcado\)\.

__5 –__ Retida: gravar “5” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 454 ou o campo “tipo de retenção” da tabela safx07 estiver preenchido com Retido pelo Tomador

__4 –__ Isenta: gravar “4” no meio magnético, quando o campo 38 \(tributação ISS\) da tabela safx09 estiver preenchido com 2\- isento ou o campo IND\_CLASSE\_PFJ da SAFX04 estiver preenchido com 10 ou Se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 433\.

__7 –__ Imune: gravar “7” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 420 ou o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07\.

__8 –__ S\.Judicial: gravar “8” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços – Município com o cód\_param = 427 ou  o campo IND\_CLASSE\_PFJ da SAFX04 = “09” 

__3 –__ Anulada: não será tratada nessa OS\.

OS3143

OS3585

__RN05__

Recuperar a informação do campo VLR\_TOT da tabela SAFX09\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\. Não devem ser utilizados pontos ou vírgulas\. Exemplo: o valor 12,34 fica representado como:

000000001234

OS3143

__RN06__

 \[ALTERADA – OS3143\-O\]

__Campo Código do Serviço/Atividade__

Verificar opção selecionada no menu Parâmetros > Definição de Layout:

__Se__ a opção Recuperar Código de Serviço – Lei Complementar 116/03 estiver selecionada, recuperar a informação do campo cod\_serv\_lei\_116 da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Se__ a opção Recuperar Código Natureza de Serviço estiver selecionada, recuperar a informação do campo COD\_NAT\_SERV da tabela SAFX2018, associado ao campo COD\_SERVICO da tabela SAFX09\.

__Senão__ recuperar a informação do campo Serviços, através da tela Serviços Msaf x Serviços Municipais\. Para os casos em que tiver mais de 1 parametrização com o mesmo Código do  Serviço Msaf e Código do Serviço Municipal, deverá ser recuperado a parametrização com a data mais atual\. 

__Tamanho do campo:__

Se a informação do campo ultrapassar de 10 caracteres, sistema deverá exibir a seguinte mensagem no log:  “Informação do campo Atividade ou Serviço Prestado ultrapassa 

o tamanho permitido\. Tamanho permitido para o campo é de até 10 caracteres\.”

OS3143

OS3143\-O

__RN42__

Gravar no campo “Identificação de Registro” o valor “1” para quando na safx04 for Pessoa Física\.

Gravar no campo “Identificação de Registro” o valor “2” para quando na safx04 for Pessoa Jurídica\.

OS3143

__RN10__

S – Estabelecido: Gravar “S” quando o cod\_municipio da tabela safx04 correspondente à Pessoa Fis/Jur da nota fiscal for igual ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

N – Não Estabelecido: Gravar “N” quando o cod\_municipio da tabela safx04 correspondente à Pessoa Fis/Jur da nota fiscal for diferente ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

OS3143

__RN11__

Recuperar a informação do campo RAZAO\_SOCIAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN12__

Recuperar a informação do campo INSC\_MUNICIPAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado \(10 posições\)\.

OS3143

__RN13__

Recuperar os dois últimos dígitos da informação do campo INSC\_MUNICIPAL da tabela SAFX04 caso o campo possua mais de 10 dígitos\. Caso o campo não preencha todas as posições preencher o mesmo com espaços\.

OS3143

__RN14__

Recuperar a informação do campo CPF\_CGC da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN15__

S – Isento: gravar “S” quando no cadastro da tabela safx04 o campo “Inscrição Estadual” estiver escrito “ISENT%”\.

N – Não Isento: gravar “N” quando no cadastro da tabela safx04 o campo “Inscrição Estadual” estiver preenchido com números\.

OS3143

__RN16__

Recuperar a informação do campo INSC\_ESTADUAL da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\. Tratar esta regra somente se RN15 for N\.

OS3143

__RN17__

Recuperar a informação do campo CEP da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com zeros à esquerda até ocupar o tamanho solicitado\.

OS3143

__RN18__

Recuperar a informação do campo TP\_LOGRADOURO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN20__

Recuperar a informação do campo ENDERECO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN21__

Recuperar a informação do campo COMPL\_ENDERECO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN22__

Recuperar a informação do campo NUM\_ENDERECO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN23__

Recuperar a informação do campo BAIRRO da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN24__

Recuperar a informação do campo UF da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN25__

Recuperar a informação da descrição do município da tabela SAFX04\. Caso o campo não preencha todas as posições preencher o mesmo com espaços à direita até ocupar o tamanho solicitado\.

OS3143

__RN08\-E__

\[ALTERADA – OS3143\]

__OBS: Regra para notas de entrada__

D – Dentro do Município: Gravar “D” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for o mesmo município cadastrado para o estabelecimento do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)

F – Fora do Município: Gravar “F” quando o campo “Município ISS” do documento fiscal de serviço \(SAFX07\) for diferente do município cadastrado para o estabelecimento do documento fiscal \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)

Caso o campo “Município ISS” do documento fiscal de serviço estiver vazio criar log de erro com a seguinte mensagem: “Para a nota fiscal \.\.\.\.\.\.\. \(demonstrar o número e código de fornecedor da nota fiscal\) Informar o código de Município ISS na capa da nota fiscal para definir o local de prestação do serviço\.”

OS3143

__RN49__

Campo: Base de Cálculo

1. Carregar o campo base\_iss \(campo 39\) da tabela x09\_itens\_serv se estiver preenchido 
2. Caso o campo anterior não estiver preenchido, carregar o campo vlr\_base para cod\_tributo = ISS da tabela x07\_base\_docfis
3. Caso nenhuma das condições anteriores sejam atendidas carregar o campo com espaços em branco

OS3143

__RN53__

Campo: Código da obra

Verificar Campo 81 da safx07 cod\_canal\_distrib

Alinhar o código da obra à esquerda e preencher os espaços restantes com espaços\.

OS3143

__RN48__

Campos: Indicador e alíquota de optante pelo Simples Nacional

\[ALTERADA – CH108506\]

Para os documentos fiscais de serviço \(SAFX07\) no cadastro de de PFJ\(SAFX04\):

Se o campo Enquadrado como Simples Nacional \-  IND\_SIMPLES\_NAC \(posição 43 da SAFX04\) estiver marcado como ‘S’ deve gravar ‘S’ no campo Indicador e recuperar o campo 

Alíquota ISS \- VLR\_ALIQ\_ISS \(posição 32 da safx 09\)

Senão, se o campo Enquadrado como Simples Nacional \-  IND\_SIMPLES\_NAC \(posição 43 da SAFX04\) estiver marcado como ‘N’ ou estiver vazio, não preencher os campos indicador e alíquota do arquivo, pois este campo não é obrigatório\.

OBS: Caso a nota fiscal possua mais de um item:

   Quando possuir mais de um item com códigos de serviço IGUAIS: neste caso, levar somente uma linha sumarizando os valores de  cada item, pois como se trata de somente uma natureza de serviço não há a necessidade de desmembrar os valores\.

  Quando possuir mais de um item com códigos de serviço DIFERENTES: neste caso, desmembrar uma linha para cada código de serviço, levando o valor do serviço de cada item e não o valor total da nota\. O campo que deverá ser utilizado é “valor total” do item de serviço

\[EXCLUIDA\]

Não preencher este campo\. Não é de preenchimento obrigatório\.Preencher com espaços\.

OS3143

CH108506

__LAYOUT GISS On Line Registro Abatimento Sub\-Empreitada  
\(Notas emitidas\)__

__RN09__

Gravar o número “2”\.

OS3143

__RN57__

__Registro Abatimento Subempreitada \-  Campo: Dia da nota fiscal__

1\-Recuperar notas fiscais de saída \(campo movto\_e\_s = 9\) utilizando somente o dia do campo data\_fiscal  da tabela SAFX07 

2\- Recuperar somente as notas com o campo CONTRATO preenchido no item da nota da tabela SAFX09 

X2018\_   Ind\_tp\_servico = 1

Class 2 ou 3

Data fiscal compreendida no período

Não considerar notas fiscais canceladas

OS3143

__RN58__

Registro Abatimento Subempreitada \-  Campo: Mês da nota fiscal

1\-Recuperar notas fiscais de saída \(campo movto\_e\_s = 9\) utilizando somente o dia do campo data\_fiscal  da tabela SAFX07 

2\- Recuperar somente as notas com o campo CONTRATO preenchido no item da nota da tabela SAFX09 

X2018\_   Ind\_tp\_servico = 1

Class 2 ou 3

Data fiscal compreendida no período

Não considerar notas fiscais canceladas

OS3143

__RN59__

Registro Abatimento Subempreitada \- Campo: Ano da nota fiscal

1\-Recuperar notas fiscais de saída \(campo movto\_e\_s = 9\) utilizando somente o dia do campo data\_fiscal  da tabela SAFX07 

2\- Recuperar somente as notas com o campo CONTRATO preenchido no item da nota da tabela SAFX09 

X2018\_   Ind\_tp\_servico = 1

Class 2 ou 3

Data fiscal compreendida no período

Não considerar notas fiscais canceladas

OS3143

__RN60__

Registro Abatimento Subempreitada \- Campo: Número da nota fiscal

1\-Recuperar notas fiscais de saída \(campo movto\_e\_s = 9\) utilizando somente o dia do campo data\_fiscal  da tabela SAFX07 

2\- Recuperar somente as notas com o campo CONTRATO preenchido no item da nota da tabela SAFX09 

X2018\_   Ind\_tp\_servico = 1

Class 2 ou 3

Data fiscal compreendida no período

Não considerar notas fiscais canceladas

OS3143

__RN61__

Considerar valores do item

Registro Abatimento Subempreitada \- Campo: Valor total da nota fiscal

1\-Recuperar notas fiscais de saída \(campo movto\_e\_s = 9\) utilizando somente o dia do campo data\_fiscal  da tabela SAFX07 

2\- Recuperar somente as notas com o campo CONTRATO preenchido no item da nota da tabela SAFX09 

X2018\_   Ind\_tp\_servico = 1

Class 2 ou 3

Data fiscal compreendida no período

Não considerar notas fiscais canceladas

OS3143

__RN75__

Considerar valores do item

Campo: Valor do imposto pago

Carregar o campo vlr\_iss\(campo 33\) da tabela safx09 se estiver preenchido 

OS3143

__RN63__

Registro Abatimento Subempreitada \- Campo: Dia do pagto da nota fiscal

1\-Verificar tabela ist\_guia\_recolh campo dat\_recolh, utilizando somente o dia para o estabelecimento referente ao da nota fiscal e código do município da capa da nota safx07\.

2\- A data da nota fiscal deve estar entre as datas de início e fim de competência da tabela ist\_guia\_recolh, campos dat\_ini\_compet e dat\_fim\_compet\. 

Utilizar filtros da RN74\.

OS3143

__RN64__

Registro Abatimento Subempreitada \- Campo: Mês do pagto da nota fiscal

1\-Verificar tabela ist\_guia\_recolh campo dat\_recolh, utilizando somente o mês para o estabelecimento referente ao da nota fiscal e código do município da capa da nota safx07\.

2\- A data da nota fiscal deve estar entre as datas de início e fim de competência da tabela ist\_guia\_recolh, campos dat\_ini\_compet e dat\_fim\_compet\. 

Utilizar filtros da RN74\.

OS3143

__RN65__

__Registro Abatimento Subempreitada \- Campo: Ano do pagto da nota fiscal__

1\-Verificar tabela ist\_guia\_recolh campo dat\_recolh, utilizando somente o ano para o estabelecimento referente ao da nota fiscal e código do município da capa da nota safx07\.

2\- A data da nota fiscal deve estar entre as datas de início e fim de competência da tabela ist\_guia\_recolh, campos dat\_ini\_compet e dat\_fim\_compet\. 

Utilizar filtros da RN74\.

OS3143

__RN74__

__Registro Abatimento de Materiais \- Campo: Guia de Recolhimento__

Verificar campo num\_guia\_recolh da tabela ist\_guia\_recolh para o estabelecimento referente ao da nota fiscal e código do município referente ao município da capa da nota safx07\. Buscar município do cadastro de contratos na tabela dwt\_contratos\.

O município ISS da tabela ist\_guia\_recolh deve ser igual ao município da tabela dwt\_contratos\.

A data da nota fiscal deve estar entre as datas de início e fim de competência da tabela ist\_guia\_recolh, campos dat\_ini\_compet e dat\_fim\_compet\. 

Caso tenha mais de uma guia para o mesmo período e mesmo estabelecimento, segue critério para definição da guia por nota fiscal:

\-Se campo tipo de faturamento estiver = 1, verificar se campo cod\_conta da tabela safx07 não está  parametrizada na tabela ist\_fatur\_antecip

\-Se campo tipo de faturamento estiver = 2, verificar se campo cod\_conta da tabela safx07 está  parametrizada na tabela ist\_fatur\_antecip

Tipo de recolhimento tem q ser igual ao tipo de recolhimento cadastrado para o estabelecimento\.

OS3143

__RN66__

__Registro Abatimento Subempreitada \- Campo: Inscrição do prestador__

Verificar na tabela ESTABELECIMENTO o campo INSC\_MUNICIPAL referente ao estabelecimento emitente da nota fiscal\.

OS3143

__RN53__

Campo: Código da obra

Verificar Campo 81 da safx07 cod\_canal\_distrib

OS3143

__RN67__

__Registro Abatimento Subempreitada \- Campo: CNPJ do prestador__

Verificar na tabela ESTABELECIMENTO o campo CGC referente ao estabelecimento emitente da nota fiscal\.

OS3143

__RN68__

__Registro Abatimento Subempreitada \- Campo: I\.E\. do prestador__

Verificar na tabela registro\_estadual o campo inscrição\_estadual  referente ao estabelecimento emitente da nota fiscal\.

OS3143

__RN10__

S – Estabelecido: Gravar “S” quando o cod\_municipio da tabela safx04 correspondente à Pessoa Fis/Jur da nota fiscal for igual ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

N – Não Estabelecido: Gravar “N” quando o cod\_municipio da tabela safx04 correspondente à Pessoa Fis/Jur da nota fiscal for diferente ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

OS3143

__RN12__

Recuperar a informação do campo INSC\_MUNICIPAL da tabela SAFX04\. 

OS3143

__RN16__

Recuperar a informação do campo INSC\_ESTADUAL da tabela SAFX04\. 

OS3143

__RN11__

Recuperar a informação do campo RAZAO\_SOCIAL da tabela SAFX04\. 

OS3143

__RN69__

Registro Abatimento Subempreitada \- Campo: Natureza

Se o campo CNPJ da tabela x04\_pessoa\_fis\_jur estiver preenchido com 14 dígitos preencher com "2"\.  
Se o campo CNPJ da tabela x04\_pessoa\_fis\_jur estiver preenchido com menos de 14 dígitos preencher com "1"\.

OS3143

__RN14__

Recuperar a informação do campo CPF\_CGC da tabela SAFX04\. 

OS3143

__RN18__

Recuperar a informação do campo TP\_LOGRADOURO da tabela SAFX04\. 

OS3143

__RN20__

Recuperar a informação do campo ENDERECO da tabela SAFX04\. 

OS3143

__RN21__

Recuperar a informação do campo COMPL\_ENDERECO da tabela SAFX04\. 

OS3143

__RN22__

Recuperar a informação do campo NUM\_ENDERECO da tabela SAFX04\. 

OS3143

__RN23__

Recuperar a informação do campo BAIRRO da tabela SAFX04\.

OS3143

__RN17__

Recuperar a informação do campo CEP da tabela SAFX04\. 

OS3143

__RN25__

Recuperar a informação da descrição do município da tabela SAFX04\.

OS3143

__RN24__

Recuperar a informação do campo UF da tabela SAFX04\. 

OS3143

__LAYOUT GISS On Line Registro Abatimento de Materiais  
\(Notas Emitidas\)__

__RN42__

Gravar no campo “Identificação de Registro” o valor fixo “1”\.

OS3143

__RN70__

__Registro Abatimento de Materiais \- Campo: Dia da nota fiscal__

Recuperar notas fiscais de saída \(campo movto\_e\_s = 9\) utilizando somente o dia do campo data\_fiscal  da tabela SAFX07 

Ind\_tp\_servico = 1

Não considerar notas fiscais canceladas

Uma das regras abaixo deverá ser atendida:

Recuperar somente as notas com o campo VLR\_MAT\_APLIC\_ISS preenchido na tabela SAFX07

Verificar na safx09 se o item de serviço esta parametrizado como material na tabela x2018\_servicos 

Campos 55\(VLR\_MAT\_PROP\) ou 56\(VLR\_MAT\_TERC\) da tabela safx09 estiver preenchido

OS3143

__RN71__

__Registro Abatimento de Materiais \- Campo: Dia da nota fiscal__

Recuperar notas fiscais de saída \(campo movto\_e\_s = 9\) utilizando somente o dia do campo data\_fiscal  da tabela SAFX07 

Ind\_tp\_servico = 1

Não considerar notas fiscais canceladas

Uma das regras abaixo deverá ser atendida:

Recuperar somente as notas com o campo VLR\_MAT\_APLIC\_ISS preenchido na tabela SAFX07

Verificar na safx09 se o item de serviço esta parametrizado como material na tabela x2018\_servicos 

Campos 55\(VLR\_MAT\_PROP\) ou 56\(VLR\_MAT\_TERC\) da tabela safx09 estiver preenchido

OS3143

__RN72__

__Registro Abatimento de Materiais \- Campo: Ano da nota fiscal__

__Registro Abatimento de Materiais \- Campo: Dia da nota fiscal__

Recuperar notas fiscais de saída \(campo movto\_e\_s = 9\) utilizando somente o dia do campo data\_fiscal  da tabela SAFX07 

Ind\_tp\_servico = 1

Não considerar notas fiscais canceladas

Uma das regras abaixo deverá ser atendida:

Recuperar somente as notas com o campo VLR\_MAT\_APLIC\_ISS preenchido na tabela SAFX07

Verificar na safx09 se o item de serviço esta parametrizado como material na tabela x2018\_servicos 

Campos 55\(VLR\_MAT\_PROP\) ou 56\(VLR\_MAT\_TERC\) da tabela safx09 estiver preenchido

OS3143

__RN73__

__Registro Abatimento de Materiais \- Campo: Dia da nota fiscal__

Recuperar notas fiscais de saída \(campo movto\_e\_s = 9\) utilizando somente o dia do campo data\_fiscal  da tabela SAFX07 

Ind\_tp\_servico = 1

Não considerar notas fiscais canceladas

Uma das regras abaixo deverá ser atendida:

Recuperar somente as notas com o campo VLR\_MAT\_APLIC\_ISS preenchido na tabela SAFX07

Verificar na safx09 se o item de serviço esta parametrizado como material na tabela x2018\_servicos 

Campos 55\(VLR\_MAT\_PROP\) ou 56\(VLR\_MAT\_TERC\) da tabela safx09 estiver preenchido

OS3143

__RN05__

Recuperar a informação do campo VLR\_TOT da tabela SAFX09\. Campo Numérico, use ponto “\.” Para separar os centavos\. EX:0000\.00

OS3143

__RN49__

Campo: Base de Cálculo

1. Carregar o campo base\_iss \(campo 39\) da tabela x09\_itens\_serv se estiver preenchido 
2. Caso o campo anterior não estiver preenchido, carregar o campo vlr\_base para cod\_tributo = ISS da tabela x07\_base\_docfis

OS3143

__RN53__

Campo: Código da obra

Verificar Campo 81 da safx07 cod\_canal\_distrib

OS3143

__RN67__

Registro Abatimento Subempreitada \- Campo: CNPJ do prestador

Verificar na tabela ESTABELECIMENTO o campo CGC referente ao estabelecimento emitente da nota fiscal\.

OS3143

__RN68__

Registro Abatimento Subempreitada \- Campo: I\.E\. do prestador

Verificar na tabela registro\_estadual o campo inscrição\_estadual  referente ao estabelecimento emitente da nota fiscal\.

OS3143

__RN10__

S – Estabelecido: Gravar “S” quando o cod\_municipio da tabela safx04 correspondente à Pessoa Fis/Jur da nota fiscal for igual ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

N – Não Estabelecido: Gravar “N” quando o cod\_municipio da tabela safx04 correspondente à Pessoa Fis/Jur da nota fiscal for diferente ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

OS3143

__RN12__

Recuperar a informação do campo INSC\_MUNICIPAL da tabela SAFX04\. 

OS3143

__RN16__

Recuperar a informação do campo INSC\_ESTADUAL da tabela SAFX04\. 

OS3143

__RN11__

Recuperar a informação do campo RAZAO\_SOCIAL da tabela SAFX04\. 

OS3143

__RN69__

Registro Abatimento Subempreitada \- Campo: Natureza

Se o campo CNPJ da tabela x04\_pessoa\_fis\_jur estiver preenchido com 14 dígitos preencher com "2"\.  
Se o campo CNPJ da tabela x04\_pessoa\_fis\_jur estiver preenchido com menos de 14 dígitos preencher com "1"\.

OS3143

__RN14__

Recuperar a informação do campo CPF\_CGC da tabela SAFX04\. 

OS3143

__RN18__

Recuperar a informação do campo TP\_LOGRADOURO da tabela SAFX04\. 

OS3143

__RN20__

Recuperar a informação do campo ENDERECO da tabela SAFX04\. 

OS3143

__RN21__

Recuperar a informação do campo COMPL\_ENDERECO da tabela SAFX04\. 

OS3143

__RN22__

Recuperar a informação do campo NUM\_ENDERECO da tabela SAFX04\. 

OS3143

__RN23__

Recuperar a informação do campo BAIRRO da tabela SAFX04\. 

OS3143

__RN17__

Recuperar a informação do campo CEP da tabela SAFX04\. 

OS3143

__RN25__

Recuperar a informação da descrição do município da tabela SAFX04\. 

OS3143

__RN24__

Recuperar a informação do campo UF da tabela SAFX04\. 

OS3143

__Regras para criação das telas__

__Cód\.__

__Descrição__

__DR__

__RN76__

O novo módulo ‘GISS ONLINE’ deve ficar localizado no Manager abaixo do módulo Municipal\.

OS3143

__RN77__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF selecionada e ao código de município do IBGE igual ao município da GISS o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Maceió, Alagoas\. Alguns dados não estarão disponíveis\. Deseja continuar?”

OS3143

__RN78__

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

OS3143

__RN79__

O botão “Não” é default\.

OS3143

__RN80__

A geração do meio magnético deve ser feita no padrão Framework\.

__\(regras disponíveis no documento matriz MTZ\-GISSONLINE\-tela de geracao do meio magnetico\.doc\)__

OS3143

__RN81__

O campo “Período de Referência” deve permitir a digitação do período no formato dd/mm/aaaa a dd/mm/aaaa, permitindo gerar o mês completo ou somente um dia\. Por padrão, o sistema sempre irá exibir o mês corrente de acordo com a data do sistema\.

__\(regras disponíveis no documento matriz MTZ\-GISSONLINE\-tela de geracao do meio magnetico\.doc\)__

OS3143

__RN82__

Os estabelecimentos exibidos devem obedecer as seguintes premissas:

- Que esteja licenciado;
- Que o usuário possua direito de acesso no PowerLock;
- Que pertença à UF do município GISS selecionado

__\(regras disponíveis no documento matriz MTZ\-GISSONLINE\-tela de geracao do meio magnetico\.doc\)__

OS3143

__RN83__

Ao gerar o arquivo devem ser exibidas as abas “Log” e “Arquivo”\. 

__Se__ o arquivo for gerado com sucesso, exibir na aba “Log” a seguinte mensagem:

*“Processo concluído com sucesso”\.*

__Se__ a opção “Recuperar Código Natureza de Serviço” do menu Parâmetros > Definição de Layout estiver selecionado e o campo COD\_NAT\_SERV da SAFX2018 não estiver preenchido, exibir na aba “Log” a seguinte mensagem: 

*“Código do Serviço 999999 não foi encontrado\.  Favor informar o código do serviço no campo Código da Natureza do Serviço na menu Básicos > Mastersaf DW > Manutenção > Códigos > Serviços”*\.

__Se__ a opção “Recuperar da parametrização Serviços Msaf x Serviços Municipais” do menu Parâmetros > Definição de Layout estiver selecionado e não for localizado a parametrização, no menu Parâmetros > Serviços Msaf x Serviços Municipais, do código do serviço informado no item da nota fiscal, exibir na aba “Log” a seguinte mensagem: 

“*Para o serviço 999999 informado, de validade dd/mm/aaaa, não foi localizada a parametrização de Serviços Msaf x Serviços Municipais\. Efetuar a parametrização no menu Parâmetros > Serviços Msaf x Serviços Municipais”\.*

Na aba “Arquivo” deve ser exibido o arquivo que poderá ser salvo localmente\.

__\(regras disponíveis no documento matriz MTZ\-GISSONLINE\-tela de geracao do meio magnetico\.doc\)__

OS3143

OS3143\-O

__RN84__

O arquivo __TEXTO__ deverá ser gerado da seguinte forma:

9999\_GISS\_20080131\.txt, onde:

9999: número do processo atribuído pelo Mastersaf\.

GISS: nome da obrigação acessória 

20080131: “Período de Referência”\. Nesse caso deverá constar o último dia do período gerado no formato aaaaddmm 

Txt: extensão do arquivo\.

__\(regras disponíveis no documento matriz MTZ\-GISSONLINE\-tela de geracao do meio magnetico\.doc\)__

OS3143

__RN85__

O arquivo __XML __deverá ser gerado da seguinte forma:

O arquivo deverá possuir cabeçalho e a primeira TAG deverá ser indicada 

como segue:

<?xml version="1\.0" encoding="UTF\-8"?>

<NF\_ABATIMENTOS xmlns:xsi="http://www\.w3\.org/2001/XMLSchema\-instance">

Nome os arquivos:

Para Subempreitadas: SubEmp\_GISS\_20080131\.xml \(constar a data da geração conforme exemplo\)

Para Abatimento de Materiais: AbatMat\_GISS\_20080131\.xml \(constar a data da geração conforme exemplo\)

__\(regras disponíveis no documento matriz MTZ\-GISSONLINE\-tela de geracao do meio magnetico\.doc\)__

OS3143

__RN86__

__Criação de Tela:__

Criação de módulo no menu Utilitários por Município__ __

OS3143

__RN87__

__Criação de Tela:__

Criação de List Box no Menu utilitários para opção de seleção da UF, quando selecionada aparecerão somente as GISS referentes aos municípios daquela UF

OS3143

__RN88__

__Criação de Tela:__

Criação de opção de módulo de parâmetros no menu utilitários com opção de ser replicada por município com a denominação “Parâmetros por Município”

OS3143

__RN89__

__Criação de Tela:__

Ao abrir a GISS do Município selecionado informar o nome do módulo no local indicado com GISS \+ nome do Município

OS3143

__RN90__

__Criação de Tela:__

Criar item de menu com opção Arquivo de Entradas e Saídas de Serviços

__\(regras disponíveis no documento matriz MTZ\-GISSONLINE\-tela de geracao do meio magnetico\.doc\)__

OS3143

__RN91__

__Criação de Tela:__

Criar item de menu com opção Arquivos de Abatimento de Materiais e Sub\- Empreitada 

__\(regras disponíveis no documento matriz MTZ\-GISSONLINE\-tela de geracao do meio magnetico\.doc\)__

OS3143

__RN92__

__Criação de Tela:__

Criar flag com opção Arquivo de Serviços Bancários Prestados

__\(regras disponíveis no documento matriz MTZ\-GISSONLINE\-tela de geracao do meio magnetico\.doc\)__

OS3143

__RN93__

__Criação de Tela:__

Criar a aba seguinte “Processos” com as informações do arquivo gerado

__\(regras disponíveis no documento matriz MTZ\-GISSONLINE\-tela de geracao do meio magnetico\.doc\)__

OS3143

__RN94__

__Criação de Tela:__

Inserir o nome do módulo no cabeçalho: Parâmetros por Município

OS3143

__RN95__

__Criação de Tela:__

Criar Itens de menu um ao lado do outro com os títulos: “Parâmetros” e “Manutenção”

OS3143

__RN96__

__Criação de Tela:__

Dentro no menu Parâmetros criar o menu Guia de Recolhimento\.

Dentro desta da opção criar os subitens: Tipo de Recolhimento de ISSQN, Contas Contábeis de Faturamento Antecipado e Parâmetros de Apuração por Estabelecimento\.

Todos esses menus são cópia dos menus de parametrização dentro do módulo ISS\. 

Menu Municipal> ISS > Parâmetros\.

__\(regras disponíveis no documento matriz MTZ\-GISSONLINE\-Telas de parâmetros\.doc\)__

OS3143

__RN97__

__Criação de Tela:__

Dentro no menu Manutenção criar “Guia de Recolhimento do ISSQN”  

Neste menu deverá constar as opções de tela iguais a do menu: Módulo ISS>ISSQN Equiparado>Equiparado a Construção Civil>Manutenção da Apuração>Guias de Recolhimento do ISSQN__ – __as informações povoadas nesta tela estarão na tabela__ __IST\_GUIA\_RECOLH

__\(regras disponíveis no documento matriz MTZ\-GISSONLINE\-Telas de parâmetros\.doc\)__

OS3143

__RN98__

__Criação de Tela:__

Criar item de menu “Classificação de Serviços por Municipio” dentro do módulo de parâmetros abaixo do menu “Guia de Recolhimento”\.

__\(regras disponíveis no documento matriz MTZ\-GISSONLINE\-Telas de parâmetros\.doc\)__

OS3143

__RN99__

__Criação de Tela:__

Inserir list Box para seleção da UF 

__\(regras disponíveis no documento matriz MTZ\-GISSONLINE\-Telas de parâmetros\.doc\)__

OS3143

__RN100__

__Criação de Tela:__

Inserir opção para seleção do Município\.

__\(regras disponíveis no documento matriz MTZ\-GISSONLINE\-Telas de parâmetros\.doc\)__

OS3143

__RN101__

__Criação de Tela:__

Inserir opção de seleção dos parâmetros criados na tfix31:

Serviços Retidos – código 454

Imposto Pago pelo Prestador – código 455

Servicos Imunes de ISS perante o Fisco – código 420

Servicos sujeitos a Deposito/Decisao Judicial – código 427

Serviços Isentos – 433

__\(regras disponíveis no documento matriz MTZ\-GISSONLINE\-Telas de parâmetros\.doc\)__

OS3143

__RN102__

__Criação de Tela:__

Inserir tabela de serviços para serem relacionados aos parâmetros

__\(regras disponíveis no documento matriz MTZ\-GISSONLINE\-Telas de parâmetros\.doc\)__

OS3143

__RN103__

__Criação de Tela:__

“Nesta tela serão listados somente os estabelecimentos que possuírem a Inscrição Municipal e o Código do Estabelecimento cadastrados no arquivo de Licenciamento\.

Em caso de dúvidas, checar as informações de UF, Município e Inscrição Municipal do cadastro do estabelecimento no módulo Básicos > Parâmetros, que precisam pertencer à GISS a ser gerada\. 

No caso de novo cadastro, para solicitação de arquivo de licenciamento entrar em contato com o setor de contratos\.

Em caso de dúvidas consultar Help do módulo\.”

__\(regras disponíveis no documento matriz MTZ\-GISSONLINE\-tela de geracao do meio magnetico\.doc\)__

OS3143

__RN104__

\[ALTERADA – \[CH105098\]  

__Criação de Tela:__

Criar tela denominada “Definição de Layout” no módulo GISS OnLine > Parâmetros por Município > Parâmetros

\-Disponibilizar opção para seleção do código do Município a ser parametrizado com base na tabela de Municípios disponibilizados na GISS OnLine\.

\-Disponibilizar flags para as seguintes opções:

1. \- Utiliza pontuação no código de Serviços: Quando esta opção estiver selecionada inserir “ponto” \(\.\) para dividir decimais no código do serviço atribuído para o campo cod\_serv\_lei\_116 da tabela dwt\_serv\_lei\_116\.Exemplo: serviço 702 deverá ser 7\.02\. Sempre decimal da direita para a esquerda\.

\[ALTERADA – \[CH105098\]  

 

1. Utiliza zeros à esquerda para completar 4 dígitos: Por default, o campo cod\_serv\_lei\_116 da tabela dwt\_serv\_lei\_116 é preenchido com 0 à esquerda, portanto, se não for selecionada esta opção, excluir o 0 à esquerda\. Exemplo: Serviço 0702 deverá ser 702 se a opção 2 não estiver selecionada ou 7\.02 se a opção 1 estiver selecionada e a opção 2 não estiver selecionada\.
2. Desconsiderar Notas Fiscais Eletrônicas de Saída: Quando esta opção estiver selecionada gerar notas fiscais com campo movto\_e\_s = 9 da tabela safx07, contendo modelo de documento DIFERENTE de 55 \(que caracteriza nota fiscal eletrônica\)\. 

##### <a id="_Toc279397182"></a>4\-Desconsiderar Notas Fiscais Eletrônicas de Entrada: Quando esta opção estiver selecionada gerar notas fiscais com campo movto\_e\_s <> 9 da tabela safx07  e modelo de documento DIFERENTE de 55<a id="_Toc279397183"></a> \(que caracteriza nota fiscal eletrônica\)\.

##### 5\-Replicar para os Municípios: Incluir seleção para replicação dos parâmetros para outros municípios\. Os municípios que devem constar nesta opção são os que estão na listagem de municípios liberados para o módulo da GISS\.

\[ALTERADA – \[CH104403\]  

1. Desconsidera zero após a pontuação no código de serviços: Caso o cliente selecione a opção número 1 – Utiliza pontuação no código de serviços o campo cod\_serv\_lei\_116 da tabela dwt\_serv\_lei\_116 gerará como o exemplo citado acima: 7\.02, porém alguns municípios excluem este zero após a pontuação decimal, portanto, se esta opção for selecionada, o código anteriormente gerado como 7\.02 será gerado como 7\.2
2. Desconsidera Último Zero à direita no Código de Serviços: Quando esta opção estiver selecionada, o campo cod\_serv\_lei\_116 da tabela dwt\_serv\_lei\_116 deverá ser gerado sem o último zero à direita\.

Exemplo: 7\.10 será gerado como 7\.1

__Regra do campo Gerar somente Notas Fiscais Emitidas – Tela de Geração Meio Magnético:__

Esse campo deve ser um check Box, com as seguintes opções “S” ou “N”\. Por default, o campo deve ser exibido desmarcado \(“N”\)\.

Quando o campo estiver marcado = \(“S”\), somente os registros de Notas emitidas deve ser gerado no meio magnético para o período informado, recuperando as notas fiscais com campo movto\_e\_s na capa = 9\.

__Regra do campo Gerar somente Notas Fiscais Recebidas – Tela de Geração Meio Magnético:__

Esse campo deve ser um check Box, com as seguintes opções “S” ou “N”\. Por default, o campo deve ser exibido desmarcado \(“N”\)\.

Quando o campo estiver marcado = \(“S”\), somente os registros de Notas Recebidas deve ser gerado no meio magnético para o período informado, recuperando as notas fiscais com campo movto\_e\_s na capa <> 9\.

Ao flegar uma opção a outra opção será desconsiderada\. Para que o arquivo seja gerado com as notas de saída e entrada, as duas opções deverão estar desmarcadas\.

OBS: Esta RN deverá ser aplicada para todos os tipos de registros da GISS OnLine exceto os Arquivos de Abatimentos de SubEmpreitada e Materiais\. Ela servirá de pré\-requisito para começar a geração\.

Em caso da não parametrização emitir a seguinte mensagem na tela de geração da GISS OnLine: *“Não foi localizado parâmetro de Definição de Layout para este município\. Menu GISS OnLine > Parâmetros por Município> Parâmetros > Definição de Layout\.”*

Esta RN deverá contemplar também a geração do Arquivo de entradas e saídas de serviços \(const\.civil/Utilities/Telecom\)\.

A mensagem não torna impeditiva a geração do arquivo\.

\-Caso o cliente faça a geração sem parametrizar considerar:

    A mesma informação do campo cod\_serv\_lei\_116 da tabela dwt\_serv\_lei\_116 para compor os códigos de serviço\.

    Considerar notas fiscais de entrada e saída \(movto\_e\_s = 1 e 9\) e notas fiscais com modelo = 55\.

__\(regras disponíveis no documento matriz MTZ\-GISSONLINE\-Telas de parâmetros\.doc\)__

CH105098

OS3143\-P

OS3143\-O

__RN105__

__Criação de Tela: Serviços Msaf x Serviços Municipais__

Criar tela denominada “Serviços Msaf x Serviços Municipais” no módulo GISS OnLine > Parâmetros por Município > Parâmetros

__Estrutura da tela__

A tela deve conter as seguintes funcionalidades: 

Grupo: ao clicar nesse botão, o sistema abrirá a tela de seleção de Estabelecimento/Grupo/Validade\.

Novo: o sistema criará um novo registro\.

Abrir: o sistema abrirá todos os registros existentes\.

Excluir: o sistema excluirá um registro existente\.

Confirmar: o sistema salvará as informações cadastradas\.

Ordenar: o sistema irá ordenar as informações de acordo com o escolhido\. Deve ser possível realizar a ordenação por todos os campos da tela\.

Relatório: o sistema chamará o relatório de conferência da tela de Serviços Msaf x Serviços Municipais\.

Sair: o sistema fechará a tela\.

__Regras da tela__

Ao clicar no menu Parâmetros > Serviços Msaf x Serviços Municipais o sistema deve exibir a tela de seleção de Estabelecimento/Grupo/Validade para que o usuário possa escolher as informações referentes aos serviços que serão parametrizados\.

 Após selecionar o Estabelecimento/Grupo/Validade, sistema deve apresentar tela com os seguintes campos:

__Validade:__ Irá permitir que diferentes serviços cadastrados no MasterSAF possam ser relacionados com o mesmo código de serviço municipal para diferentes períodos\. A data de validade é do tipo “a partir de”\. Deve conter a máscara DD/MM/AAAA\.

__UF: __Campo do tipo__ __combo box e deve exibir todas as UFs cadastradas na tabela ESTADO 

__Município:__ Deve recuperar as informações da tabela relacionadas à UF selecionada\. A recuperação dos municípios deve ser realizada através da pastinha amarela\.

__Serviços MasterSAF:__ Deverá recuperar as informações do campo COD\_SERVICO da tabela X2018\_SERVICOS\. Somente serão recuperadas informações cadastradas no grupo escolhido\. A recuperação dos serviços deve ser realizada através da pastinha amarela\.

Para a geração do meio magnético, através do menu Geração > Arquivo de Entradas e Saídas de Serviços, o usuário deve selecionar o município informado no cadastro do estabelecimento \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\.

Para a geração do meio magnético, através do menu Geração > Arquivo de Entrada de Serviços \(Construção Civil/ Utilities/Telecom\), o usuário deve selecionar o município informado no campo Município ISS do documento fiscal \(campo COD\_MUNICIPIO da SAFX07\)\.

\[CH112124\-B\]

__Serviços: __Listar os serviços da tabela TFIX106, relacionadas ao município informado no campo “Município”\. Os serviços devem ser recuperados, independente da data fixada no campo “DATA DE VALIDADE” da TFIX106\. 

 O sistema não deve permitir que os mesmos serviços sejam relacionados com a mesma UF, município e data de validade\. Nessa situação o sistema deverá exibir a seguinte mensagem de erro: “Já existe registro com a chave informada”\.

__Regras do relatório da tela__

Deve existir um relatório de conferência que informe os relacionamentos existentes entres os serviços cadastrados no MasterSAF e os serviços municipais solicitados pelo município\.

__\(regras disponíveis no documento matriz MTZ\-GISSONLINE\-Telas de parâmetros\.doc\)__

OS3143\-O

CH112124\-B

