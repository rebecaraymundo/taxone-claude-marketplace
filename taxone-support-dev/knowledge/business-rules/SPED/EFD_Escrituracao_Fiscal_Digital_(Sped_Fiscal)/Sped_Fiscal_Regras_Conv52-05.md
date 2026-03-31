# Sped_Fiscal_Regras_Conv52-05

- **Fonte:** Sped_Fiscal_Regras_Conv52-05.docx
- **Modificado:** 2024-08-06
- **Tamanho:** 52 KB

---

__         Regras de Geração do Sped Fiscal, opção “Convênio ICMS 52/2005”__

__Localização__: Menu SPED, módulo EFD – Escrituração Fiscal Digital, menu Geração – Conv\. ICMS 52/05 🡪 Meio Magnético

Este documento é específico da geração efetuada no menu “Geração – Conv\. ICMS 52/05 🡪 Meio Magnético”, onde para um determinado estabelecimento, serão gerados os arquivos da EFD a serem entregues para as UF’s nas quais o estabelecimento tenha prestado serviços de TV por assinatura via satélite, conforme solicitação do Convênio ICMS 52/2005 \(para maiores informações consultar help deste menu\)   

__                                                                    R e v i s õ e s__

__Data__

__OS / Chamado__

__Descrição __

__Responsável__

27/06/2011

OS3335\-A

\(criação do docto\)

Telecom – Geração da EFD p/as UF’s dos tomadores do serviço de TV por assinatura via satélite, conforme Convênio ICMS 52/2005\. 

Vânia Dias Mattos

07/03/2014

OS4342

Geração do Bloco K \(ver RN0001\)

Vânia Dias Mattos

25/05/2015

OS4786

Alteração na geração do Convênio 115 p/tratamento do modelo \(ver regras do registro D695 e D696\)

Vânia Dias Mattos

27/12/2016

MFS6391 \(ch16897/16\)

Correção na geração do campo 05\-COD\_REC de registro E116 

Vânia Dias Mattos

05/04/2017

MFS8681

\(ch 15814/16\)

Ajustes na geração dos registros do Bloco E devido à alteração na manutenção dos lançamentos complementares\.

Vânia Dias Mattos

14/02/2018

MFS\-16364

Inclusão da geração dos Registros 0190, 0200, 1010 e 1400\. 

Julyana Perrucini

07/12/2018

MFS22062

Alteração na geração dos arquivos do Conv\. ICMS 52/05 para armazenar o saldo credor resultante do período, quando for o caso, e transportá\-lo para o período seguinte\.\.

Vânia Dias Mattos

01/07/2024

MFS656015

Inclusão da geração dos registros 0002, E500 e E520\.  Alteração na regra de geração dos registros E100 e E110, para os arquivos sem movimento\.

Andréa Rocha

 

RN0000

__Parâmetros da tela de geração__:

Campo __Estabelecimento__ 🡪 Este campo é uma lista com a relação de todos os estabelecimentos parametrizados no menu “Dados Iniciais” que tenham o parâmetro “*Obrigado ao Convênio ICMS 52/2005”* = “S”*\.*

Campo __Data Inicial__ 🡪 data inicial do período da geração

Campo __Data Final __🡪 data final do período da geração

Campo__ Leiaute__ 🡪 Este campo é uma lista com a relação de todos os leiautes do Sped Fiscal atendidos pelo Mastersaf\.  A lista deve exibir a descrição completa do leiaute\.

Campo __Finalidade__ 🡪 Este campo é uma lista com as seguintes opções:

- Remessa do Arquivo Original
- Remessa do Arquivo Substituto

Quadro __UF’s a serem geradas__ 🡪 Neste quadro são exibidas todas as UF’s e respectivas inscrições estaduais cadastradas p/o estabelecimento no menu “Geração – Conv\. ICMS 52/05 🡪Inscrições Estaduais”, e o usuário poderá selecionar as UF’s para as quais deseja efetuar a geração do arquivo\.

Obs: Esta geração *não* trabalha com a informação do perfil, porque os registros a serem gerados são fixos\.

RN0001

__Regras da Geração__:

Para cada UF / Inscrição Estadual selecionada em tela deverá ser gerado um arquivo do Sped Fiscal\.

São arquivos um tanto fora do padrão, pois na realidade são apenas parte do arquivo “oficial” do Estabelecimento, que conterão apenas os valores referentes aos serviços prestados de TV por assinatura para outras UF’s nos registros D695 e D696\.

Esses arquivos representam a apuração do imposto feita para cada UF onde o estabelecimento mantenha a prestação deste serviço\.

Alteração da __MFS8681__: A geração dos arquivos do Conv\. ICMS 52/05 foi alterada para mudança do conceito em relação aos lançamentos complementares\. Originalmente, só era previsto lançamentos do tipo “estorno de débito”\. Com a alteração para permitir que qualquer tipo de lançamento possa ser associado aos arquivos do Convênio\.52, foram realizados alguns ajustes na geração do Bloco E\.

Os débitos e créditos desta apuração se resumem no seguinte:

__Débito__ 🡪 Total dos valores declarados no registro D696 e débitos de lançamentos complementares que possam existir \(__MFS8681__\);

__Crédito__ 🡪 Valor do lançamento complementar a ser feito manualmente pelo usuário\. Este lançamento representa o rateio do ICMS das notas fiscais entre a UF do prestador e a UF do tomador\. Além deste lançamento, também serão considerados demais créditos de lançamentos complementares que possam existir \(__MFS8681__\);

Como não existe esta apuração no Mastersaf, a geração do Bloco E será feita a partir de regras diferenciadas\.

Alteração da __MFS\-16364__: A geração dos arquivos do Conv\. ICMS 52/05 foi alterada para contemplar o registro 1400\. O conceito permanece o mesmo, porém o recolhimento do ICMS para UF diversa\. Consequentemente foram acrescentados os Registros 0190, 0200 e 1010 \(este último para declaração da obrigatoriedade do Bloco 1\)\.

__O conteúdo destes arquivos será o seguinte__:

__Bloco 0__

Os registros do Bloco 0 serão gerados normalmente, sendo que a inscrição estadual do registro de identificação \(“0000”\) será a UF do tomador do serviço\. A maioria dos registros deste bloco não será gerada, uma vez que nestes arquivos não constarão documentos fiscais\. Assim, não existirão dados cadastrais a serem informados\. 

__Bloco C__

Este bloco será gerado *sem informação*\.

__Bloco D__

Serão gerados somente os registros D695 e D696, com os valores referentes às operações realizadas com a UF em questão\.

__Bloco E__

Serão gerados apenas os registros E100, E110, E111, E112 e E116: 

No E110 constará o débito do total das operações com a UF em questão, e o crédito referente ao lançamento complementar de rateio do ICMS, e demais débitos e créditos de lançamentos complementares que possam existir \(__MFS8681__\);

No E111 constará o lançamento complementar do rateio do ICMS entre as duas UF’s, e demais lançamentos complementares que possam existir \(__MFS8681__\);

No E112 constarão as informações de processos e documentos de arrecadação vinculados aos lançamentos, caso existam; \(a geração do registro E112 foi incluída na __MFS8681__\); 

No E116 constarão os dados do recolhimento feito para a UF em questão;

__Blooc G__

Este bloco será gerado *sem informação*\.

__Bloco H __

Este bloco será gerado *sem informação*\.

__Bloco K __

Este bloco será gerado *sem informação*\.                 *\(bloco inserido no layout pela OS4342\)*

__Bloco 1__

Este bloco será gerado *sem informação*\.

Serão gerados os registros 1010 e 1400:

No 1010, constará a obrigatoriedade de registro do Bloco 1;

No 1400 constarão os dados dos municípios com os valores referentes às operações realizadas com a UF em questão\.

A seguir serão descritas as regras de cada um dos registros a serem gerados\.

 

#### Bloco 0 – Abertura, Identificação e Referências

Registro 0000

As regras de geração são as mesmas do arquivo “normal”, exceto para os campos descritos abaixo, que deverão ser gerados com o seguinte conteúdo:

Campo __09\-UF__ 🡪 gravar a UF selecionada em tela

Campo __10\-IE__ 🡪 gravar a inscrição estadual da UF selecionada em tela 

Campo __11\-COD\_MUN__ 🡪 gravar o código do município da capital da UF gravada no campo 09\-UF

Campo __12\-IM 🡪 __este campo deve ser gravado sem informação \(“||”\)

Campo __13\-SUFRAMA 🡪 __este campo deve ser gravado sem informação \(“||”\)

Campo __14\-IND\_PERFIL__ 🡪 gravar “A”

Registro 0002

__\[MFS656015\]__  Inclusão do registro

Idem arquivo “normal”\. 

Esse registro deve ser informado quando o campo IND\_ATIV do registro 0000 for igual a “0”\. 

Registro 0005

Idem arquivo “normal”\.

Registro 0015

Não será gerado\.

Registro 0100

Idem arquivo “normal”\.

Registro 0150

Não será gerado, uma vez que o arquivo não conterá nenhum documento fiscal, portanto, não existirá nenhuma pessoa fis/jur a ser referenciada neste registro\.

Registro 0175

Não será gerado, uma vez que não existirão pessoas fis/jur no registro 0150\.

Registro 0190

Idem arquivo “normal”\.

Registro 0200

Idem arquivo “normal”\.

Registro 0205

Não será gerado, uma vez que não existirão produtos no registro 0200\.

Registro 0206

Não será gerado, uma vez que não existirão produtos no registro 0200\.

Registro 0220

Não será gerado, uma vez que não existirão produtos no registro 0200\.

Registro 0300

Não será gerado, uma vez que o arquivo não conterá nenhum documento fiscal, e o Bloco G será gerado sem informação\. Assim, não existirão Bens a serem referenciados neste registro\.

Registro 0305

Não será gerado, uma vez que não existirão Bens no registro 0300\.

Registro 0400

Não será gerado, uma vez que o arquivo não conterá nenhum documento fiscal, portanto, não existirão naturezas de operação a serem referenciadas neste registro\.

Registro 0450

Não será gerado, uma vez que o arquivo não conterá nenhum documento fiscal, portanto, não existirão informações complementares a serem referenciadas neste registro\.

Registro 0460

Não será gerado, uma vez que o arquivo não conterá nenhum documento fiscal, portanto, não existirão observações a serem referenciadas neste registro\.

Registro 0500

Não será gerado, uma vez que o arquivo não conterá nenhum documento fiscal, portanto, não existirão contas contábeis a serem referenciadas neste registro\.

Registro 0600

Não será gerado, uma vez que o arquivo não conterá nenhum documento fiscal, portanto, não existirão centros de custos a serem referenciados neste registro\.

#### Bloco D – Documentos Fiscais II – Serviços \(ICMS\)

Registro D695

As regras de geração são as mesmas do arquivo “normal”, exceto os campos do nome e da chave de autenticação digital do arquivo mestre, que serão gerados com o seguinte conteúdo:

Campo __08\-NOM\_MESTRE__ 🡪 Será o mesmo nome do arquivo mestre utilizado no arquivo “normal”, trocando\-se apenas as duas primeiras posições pela sigla da UF em questão \(UF informada em tela para a geração do arquivo\)\.

Exemplo, supondo que a UF informada em tela seja = MG:

Se o conteúdo a ser gravado no arquivo “normal” for “__SP__0011106NM\.001”, gravar “__MG__0011106NM\.001”\.

Campo __09\-CHV\_COD\_DIG__ 🡪 Ao invés de gravar o código de autenticação que consta na ICT\_MM\_CONV115, como é feito no arquivo “normal”, será gravado o código de autenticação do arquivo mestre da UF em questão, gerado pelo programa “extrator”\. Esta informação é recuperada a partir dos dados que são armazenados na geração do Convênio 115\. Para isso, considerar os dados que compõe a chave da ICT\_MM\_CONV115 \+ a UF em questão, e a partir do registro encontrado, utilizar a informação do código de autenticação digital do arquivo da UF em questão\.

Alteração da __OS4786__: A partir desta OS, os arquivos do Conv\.115 passaram a ser gerados por Série e Modelo\. Como o modelo *não* faz parte do nome do arquivo, poderão existir arquivos de mesmo nome, mas conteúdo diferente, sendo um para cada modelo \(modelo 21 e 22 por exemplo\)\. Na prática, os procedimentos realizados na geração do Sped *não* tiveram alterações em seu funcionamento, apenas os ajustes internos, necessários p/o tratamento das tabelas que contém os dados do Convênio \(são as tabelas “ICT\_MM\_CONV115”\)\.

__Importante__: Para a geração “normal” do Sped Fiscal  é pré\-requisito gerar o arquivo do Convênio 115 e depois executar a rotina de importação dos hash code\. Da mesma forma que para a geração destes arquivos “especiais” será pré\-requisito gerar os arquivos das respectivas UF’s através do programa “extrator”, e depois, executar a rotina de importação dos hash code destes arquivos\.

Registro D696

Assim como na geração “normal”, os dados deste registro são recuperados da tabela que contém os valores agrupados por UF \+ CST \+ CFOP \+ ALIQ \(ICT\_MM\_CONV115\_UF\_CFOP\), com duas diferenças:

	

Diferença 1 🡪 Serão considerados *apenas* os registros referentes à UF em questão

                        \(ou seja, considerar apenas os registros onde COD\_ESTADO = UF informada em tela\) 

Diferença 2 🡪 Os campos 08 e 09 devem ser gerados com zero:

                         Campo __08\-VL\_BC\_ICMS\_UF__ – gravar zero;

                         Campo __VL\_ICMS\_UF__ – gravar zero;

\(o Guia Prático orienta a não preencher os campos 08 e 09 nos arquivos referentes à UF dos tomadores, no entanto, não há como deixar o campo sem preenchimento \(o PVA dá erro\), pois eles são obrigatórios\)

Alteração da __OS4786__: A partir desta OS, os arquivos do Conv\.115 passaram a ser gerados por Série e Modelo\. Como o modelo *não* faz parte do nome do arquivo, poderão existir arquivos de mesmo nome, mas conteúdo diferente, sendo um para cada modelo \(modelo 21 e 22 por exemplo\)\. Na prática, os procedimentos realizados na geração do Sped *não* tiveram alterações em seu funcionamento, apenas os ajustes internos, necessários p/o tratamento das tabelas que contém os dados do Convênio \(são as tabelas “ICT\_MM\_CONV115”\)\.

#### Bloco E – Apuração do ICMS e do IPI

Registro E100

__\[MFS656015\]__  Alteração da geração do registro, que deve ser gerado mesmo que não haja movimento no registro E110\.

As regras de geração são as mesmas do arquivo “normal”\.

__Obs__\.: Esse registro deve ser gerado mesmo que não haja movimento de ICMS, só preenchendo a data inicial e final da apuração do ICMS\.

Registro E110

__\[MFS656015\]__  Alteração da geração do registro, que deve ser gerado mesmo que não haja movimento, com todos os valores zerados\.

Assim como no arquivo “normal”, para cada apuração, ou seja, para cada registro E100 gravado, existirá um único registro E110\.

A diferença é que os dados não serão obtidos na tabela do resumo da apuração do ICMS, e sim de acordo com as regras descritas a seguir:

Para os campos gerados a partir dos lançamentos complementares da Apuração do ICMS \(seja o livro 108 ou 165\), a recuperação dos dados deve considerar os seguintes critérios:

    \- Campo “Empresa” – código da empresa do login;

    \- Campo “Estabelecimento” – código do estabelecimento selecionado para a geração;

    \- Campo “Data da Apuração” – deve estar contida no período de datas do registro E100;

    \- Campo “Lançamento Complementar referente à prestação de serviços de TV por assinatura via satélite \(Conv\. 52/05\)” = “S”;

    \- Campo “UF” = UF informada em tela para a geração;

Estes critérios servem tanto para a recuperação dos lançamentos \(aba “*Lançamento de Valores*”\), como dos débitos especiais \(aba “*Débitos Especiais*”\)\.

Alteração da __MFS8681__: Ao gerar o registro E110, passaram a ser gerados todos os campos de lançamentos na apuração, inclusive os débitos especiais \(são os campos 04, 05, 08, 09, 12 e 15\)\.  Na versão original, apenas o campo 09\-VL\_ESTORNOS\_DEB era tratado, já que só era possível associar ao Conv\. ICMS 52/05 lançamentos do tipo “estorno de débito”\. Devido à alteração, os campos tachados abaixo tiveram suas regras alteradas, e vários campos não gerados passaram a ser preenchidos\.

Alteração da __MFS22062__: A geração do registro E110 foi alterada para armazenar o saldo credor resultante do período, quando for o caso, e transportá\-lo para o período seguinte\.

__Conteúdo dos campos do E110:__

Obs: Todos os campos *não* citados acima deverão ser gerados com o valor zero \(|0|\)\.

Campo __02\-VL\_TOT\_DEBITOS__ 🡪 o valor deste campo será o total do campo 07\-VL\_ICMS de todos os registros D696 gerados no arquivo, que sejam referentes ao período de apuração do registro “pai” E100 

Campo __04\-VL\_TOT\_AJ\_DEBITOS __🡪 O valor deste campo será o total dos lançamentos complementares da apuração do ICMS, do tipo “*Outros Débitos*”\. Ou seja, o campo “*Operação Apuração*” deve ser = “__002__”\.

Campo __05\-VL\_ESTORNOS\_CRED __🡪 O valor deste campo será o total dos lançamentos complementares da apuração do ICMS, do tipo “*Estorno de Créditos*”\. Ou seja, o campo “*Operação Apuração*” deve ser = “__003__”\.

Campo __08\-VL\_TOT\_AJ\_CREDITOS __🡪 O valor deste campo será o total dos lançamentos complementares da apuração do ICMS, do tipo “*Outros Créditos*”\. Ou seja, o campo “*Operação Apuração*” deve ser = “__006__”\.

Campo __09\-VL\_ESTORNOS \_DEB__ 🡪 o valor deste campo será o total dos lançamentos complementares da apuração do ICMS, do tipo “*Estorno de Debitos*”\. Ou seja, o campo “*Operação Apuração*” deve ser = “__007__”\.

Campo __10\-VL\_SLD\_CREDOR\_ANT__ 🡪 Para a geração deste campo será verificada a existência de saldo credor no período anterior\. Essa verificação é feita na “*Tabela dos Saldos Credores do Conv\. 52/05*”, a partir dos critérios a seguir:

 \(O tratamento do saldo credor anterior foi uma alteração da __MFS22062__\. Anteriormente o campo 10 era gravado com zero\)

   \- Campo “Empresa” – código da empresa do login;

   \- Campo “Estabelecimento” – código do estabelecimento selecionado para a geração;

   \- Campo “Data Apuração” – Data da apuração do período anterior ao período da geração \( último dia do período anterior\);

   \- Campo “UF” = Identificação da UF para qual o arquivo está sendo gerado;

Se não existir informação, o campo __10\-VL\_SLD\_CREDOR\_ANT__ será gravado com zero;

Se existir, o campo __10\-VL\_SLD\_CREDOR\_ANT__ será gravado com o conteúdo do campo “Valor do Saldo Credor” da tabela;

Campo __11\-VL\_SLD\_APURADO__ 🡪 O valor deste campo será o resultado da seguinte expressão \(débitos – créditos\):

\[ 02\-VL\_TOT\_DEBITOS \+ \(04\-VL\_TOT\_AJ\_DEBITOS  \+ 05\-VL\_ESTORNOS\_CRED \) – \(08\-VL\_TOT\_AJ\_CREDITOS  \+ 09\-VL\_ESTORNOS\_DEB\) \]

\(Alteração __MFS22062__: Incluído o saldo credor anterior na expressão\)

         \[ 02\-VL\_TOT\_DEBITOS __\+__ 04\-VL\_TOT\_AJ\_DEBITOS __\+__ 05\-VL\_ESTORNOS\_CRED \]   __ –__ 

      \[ 08\-VL\_TOT\_AJ\_CREDITOS __\+__ 09\-VL\_ESTORNOS\_DEB __\+ 10\-VL\_SLD\_CREDOR\_ANT__ \] 

Caso o resultado seja negativo, este campo será preenchido com zero, e o valor do resultado obtido \(valor absoluto\) será gravado no campo 14\-VL\_SLD\_CREDOR\_TRANSPORTAR\.

Campo __12\-VL\_TOT\_DED__ 🡪 o valor deste campo será o total dos lançamentos complementares da apuração do ICMS, do tipo “*Deduções*”\. Ou seja, o campo “*Operação Apuração*” deve ser = “__012__”\.

Campo __13\-VL\_ICMS\_RECOLHER__ 🡪 O preenchimento deste campo segue a regra abaixo: 

     Se o campo 11\-VL\_SLD\_APURADO__ __=__ __zero, 

          Este campo também será gravado com zero;

     Senão 

          Este campo será gravado com o seguinte resultado: \[ 11\-VL\_SLD\_APURADO – 12\-VL\_TOT\_DED \]\. Caso este resultado

          seja negativo, este campo será preenchido com zero, e o valor do resultado obtido \(valor absoluto\) será  gravado no campo 

          14\-VL\_SLD\_CREDOR\_TRANSPORTAR\.

*\(Obs: pelo conceito da Apuração do ICMS, se campo 11\-VL\_SLD\_APURADO <= 0 não pode existir dedução\)*

Campo __14\-VL\_SLD\_CREDOR\_TRANSPORTAR__ 🡪 O valor deste campo depende das regras de geração dos campos 

“*11\-VL\_SLD\_APURADO*” e “*13\-VL\_ICMS\_RECOLHER*”, conforme descrito acima\. Quando não existir valor a ser gravado no campo, decorrente das regras dos campos 11 e 13, o campo será gravado com zero\.

Quando o campo 14 for gravado com valor > zero, será feita a atualização deste valor na “Tabela dos Saldos Credores do Conv\. ICMS 52/05”, para que este saldo credor seja armazenado, e recuperado para o arquivo do próximo período\.

Informações para a gravação do saldo credor na tabela:

   \- Campo “Empresa” – código da empresa do login;

   \- Campo “Estabelecimento” – código do estabelecimento selecionado para a geração;

   \- Campo “Data Apuração” – Data da apuração do período em questão \(data final informada na tela\);

   \- Campo “UF” = Identificação da UF para qual o arquivo está sendo gerado;

   \- Campo “Valor do Saldo Credor” – valor gravado no campo 14\-VL\_SLD\_CREDOR\_TRANSPORTAR; 

Campo __15\-DEB\_ESP__ 🡪 o valor deste campo será o total dos lançamentos complementares da apuração do ICMS do estabelecimento, do tipo “*Débitos Especiais*”\. Ou seja, são os lançamentos da aba “__Débitos Especiais__”\.

__Obs__\.: Esse registro deve ser gerado mesmo que não haja movimento, com todos os valores zerados\.

Registro E111

Neste registro são gravados, um a um, os lançamentos complementares da apuração do ICMS do estabelecimento, que atendam aos seguintes critérios:

    \- Campo “Empresa” – código da empresa do login;

    \- Campo “Estabelecimento” – código do estabelecimento selecionado para a geração;

    \- Campo “Data da Apuração” – deve estar contida no período de datas do registro E100;

    \- Campo “Lançamento Complementar referente à prestação de serviços de TV por assinatura via satélite \(Conv\. 52/05\)” = “S”;

    \- Campo “UF” = UF informada em tela para a geração;

\(são exatamente os lançamentos que foram totalizados no campo __09\-VL\_ESTORNOS \_DEB__ do registro E110\) 

São exatamente os lançamentos que foram totalizados nos campos 04, 05, 08, 09, 12 e 15 do registro “pai” E110\.

Estes critérios servem tanto para a recuperação dos lançamentos \(aba “*Lançamento de Valores*”\), como dos débitos especiais \(aba “*Débitos Especiais*”\)\.

Alteração da __MFS8681__: Ao gerar o registro E110, passaram a ser gerados todos os campos de lançamentos na apuração, inclusive os débitos especiais \(são os campos 04, 05, 08, 09, 12 e 15\)\.  Na versão original, só eram permitidos lançamentos de estorno de débitos \(campo 09\)\.

A gravação de cada campo deste registro é igual a da geração do arquivo “normal”, com exceção do campo 02\-COD\_AJ\_APUR, que deverá ser gravado com o conteúdo do seguinte campo do lançamento:

                                  Campo “__Código de Ajuste da UF \(Sped Fiscal \- Reg\. E111\)__”

Registro E112

\(Originalmente, a geração dos arquivos do Conv\. 52/05 não tratava o E112\. O registro só passou a ser gerado a partir da __MFS8681__\)\. 

Este registro é “filho” do E111, e da mesma forma que no arquivo “normal”, será gerado a partir dos processos ou documentos de arrecadação vinculados ao lançamento gravado no registro pai \(opção “*Processos/Doc\.Arrecadação*” da tela de manutenção dos lançamentos complementares\)\.

As regras do preenchimento dos campos são as mesmas da geração da EFD “normal”\.

Registro E116

Da mesma forma que no arquivo “normal”, este registro será gerado a partir das guias de recolhimento cadastradas no módulo ICMS \(aba GUIA da manutenção dos lançamentos complementares\) para a apuração do período \(Registro E100\)\.

A diferença é que para este arquivo devem ser consideradas apenas as guias que atendam aos seguintes critérios:

    \-Campo “Guia referente ao recolhimento do ICMS p/UF dos tomadores do serviço \(Conv\. 52/05\)” = “S” 

    \-Campo “UF” = UF informada em tela para a geração

Alteração __MFS6391__ \(Ch 16897/16\): Tratamento do campo “05\-COD\_REC”

As regras para o tratamento do código da receita são as mesmas da geração da EFD “normal”, onde existem tratamentos diferenciados para algumas UF’s\. A diferença é que para aplicar estas regras, será considerada a UF selecionada em tela, ou seja, a UF gerada no registro 0000, ao invés da UF do estabelecimento\.  

Registro E500

__\[MFS656015\]__  Inclusão do registro

As regras de geração são as mesmas do arquivo “normal”\.

__Obs__\.: Esse registro deve ser gerado mesmo que não haja movimento de IPI, só preenchendo a data inicial e final da apuração do IPI\.  Os demais registro do bloco E500 não serão gerados, com exceção do registro E520\.

Registro E520

__\[MFS656015\]__  Inclusão do registro

Esse registro deve ser gerado com todos os valores zerados, quando o registro E500 for gerado\.

#### Bloco 1 – Outras Informações

Registro 1010

Esse registro serve para apresentar a obrigatoriedade do Bloco 1 por unidade federada, porém no Convênio ICMS 52/05 será apresentada a obrigatoriedade apenas para o registro 1400, quando houver:

__01\-REG__ 🡪 este campo será preenchido c/o conteúdo fixo “1010”\.

__02\-IND\_EXP__ 🡪 este campo será preenchido c/o conteúdo fixo “N”\.

__03\-IND\_CCRF__ 🡪 este campo será preenchido c/o conteúdo fixo “N”\.

__04\-IND\_COMB__ 🡪 este campo será preenchido c/o conteúdo fixo “N”\.

0__5\-IND\_USINA __🡪 este campo será preenchido c/o conteúdo fixo “N”\.

__06\-IND\_VA__ 🡪 Se houver movimentação para o período no registro 1400, então o sistema deve gerar automaticamente este campo com o valor “S”\. Se não houver movimentação, gerar como “N”\.

__07\-IND\_EE__ 🡪 este campo será preenchido c/o conteúdo fixo “N”\.

__08\-IND\_CART__ 🡪 este campo será preenchido c/o conteúdo fixo “N”\.

__09\-IND\_FORM__ 🡪 este campo será preenchido c/o conteúdo fixo “N”\.

__10\-IND\_AER__ 🡪 este campo será preenchido c/o conteúdo fixo “N”\.

Registro 1400

As informações deverão ser recuperadas da tabela de Manutenção do Registro 1400, localizada no módulo EFD\-Escrituração Fiscal Digital, item de menu: Geração 🡪 Manutenção 🡪 Registro 1400, considerando a empresa e o estabelecimento selecionados e de acordo com a apuração preenchida:

__01\-REG__ 🡪 este campo será preenchido c/o conteúdo fixo “1400”\.

__02\-COD\_ITEM\_IPM__ 🡪 este campo será preenchido c/o conteúdo do campo “Produto” \(indicador e o código do produto\) para os municípios que não utilizam de uma regra específica, os que utilizam, o campo será preenchido c/o conteúdo do campo “Código da Tabela de Itens p/o Índice de Participação dos Municípios”\.

__Crítica:__

Geralmente quando não se utiliza uma regra específica o valor informado deve existir no campo COD\_ITEM do registro 0200, então teoricamente a geração “Padrão” precisa ser por produto, como o registro foi implementado para aceitar também por município por conta das atividades de transporte e EE e nesse Convênio só será tratado comunicação, não vamos obrigar o usuário, deixaremos ao seu critério o tipo de geração se por município ou município \+ produto, mas emitiremos a seguinte mensagem: *“Erro: O Campo COD\_ITEM é de preenchimento obrigatório, e não foi informado”\.*

__03\-MUN__ 🡪 este campo será preenchido c/o conteúdo do campo “Município”, esse campo informa o município do ponto de consumo, e será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __🡪 este campo será preenchido c/o conteúdo do campo “Valor Apurado do grupo Valores Conv\. ICMS 52/05”\.

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

- Resultado final = negativo 🡪 Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR está com conteúdo inválido \(valor negativo\)\.”\. *O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\.
- Resultado final = zero 🡪 O registro 1400 não será gravado para este município\.

