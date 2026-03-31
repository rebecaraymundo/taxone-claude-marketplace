# MTZ-ICMS-GNREOnline_Geracao_do_ArquivoXML

- **Fonte:** MTZ-ICMS-GNREOnline_Geracao_do_ArquivoXML.docx
- **Modificado:** 2025-04-02
- **Tamanho:** 74 KB

---

                           __Geração do Arquivo de Lotes de Guias __

__Localização__: Menu Estadual, Módulo ICMS, menu Apuração 🡪 Guias de Recolhimento 🡪 Recolhimento Tributos Estaduais \(GNRE Online\) 🡪 Geração do Arquivo XML

##                                            <a id="_Toc24450060"></a><a id="_Toc24450452"></a><a id="_Toc24451351"></a><a id="_Toc24451817"></a>Documento de Requisito

__Doc__

__Alteração__

__Data__

__Resp__

__OS3520\-B__

Geração do Arquivo XML da GNRE Online

19/03/2013

\(Criação do doc\)

Vânia Mattos

__CH26354\_2013__

Tratamento dos campos c19\_municipioEmitente e c22\_telefoneEmitente da identificação do emitente

22/10/2013

Julyana Perrucini

__CH26354\-B\_2013__

Tratamento dos campos 

c06\_valorPrincipal e 

c10\_valorTotal 

19/11/2013

Julyana Perrucini

__MFS27985__

Novo parâmetro “Versão” para possibilitar a geração nos dois layout’s: 1\.00 e 2\.00

12/11/2019

Vânia Mattos

__MFS34140__

<a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK8"></a><a id="OLE_LINK10"></a>Novo parâmetro para não gravar no arquivo, as guias em que a UF Favorecida for a própria UF do estabelecimento da geração\.

29/06/2020

Vânia Mattos

__MFS64168__

Tratamento das tag’s ‘*contribuinteEmitente*”, ”*contribuinteDestinatario*” e das tag’s de preenchimento não obrigatórios: layout: 2\.00\.

01/06/2021

Rogério Ohashi

__MFS74539__

Tratamento dos Campos Detalhamento da Receita, Detalhamento de Produto e Tipo de Documento Origem para serem preenchidos ou não, ou __se nulo__, conforme Parâmetro por UF\.

26/10/2021

Rogério Ohashi

__MFS78478__

Tratamento dos Campos Período e Mês e Ano, para serem preenchidos ou não, conforme Parâmetro por UF\.

29/12/2021

Rogério Ohashi

__MFS534151__

Alteração da regra de preenchimento da tag IdentificadorGuia, quando a UF favorecida for igual a SP\.  Essa alteração está sendo feita para possibilitar a importação do arquivo XML para gerar a DARE SP, qua não importa o arquivo se possuir essa tag\.

08/05/2023

Andréa Rocha

__MFS544156__

Inclusão dos novos campos Valor Principal FECP e Valor Total FECP na geração do arquivo XML\.  Esses campos são necessários para tratar a geração de uma guia única e e com um único código de receita 10011\-0 \(Apuração\) ou 10010\-2 \(Operação\), para os valores do ICMS e o FECP, para a UF favorecida igual a ‘RJ’ ou ‘RS’ ou ‘SE’ ou ‘RO’\.   A alteração será feita para a versão 2\.00\.

22/06/2023

Andréa Rocha

__MFS585714__

Inclusão do tratamento para gerar a guia por Apuração, informando o produto \(Classificação do Produto da GNRE\)\.

15/12/2023

Andréa Rocha

__MFS602689__

Passar a gerar um único número de processo para todas as UF’s de um determinado estabelecimento\.

Atendimento requisitado pelo TAX AUTOMATION

01/03/2024

Liliane Assaf

__MFS792095__

Alteração da regra de preenchimento do campo Inscrição Estadual \(IE\) do contribuinte emitente para UF=PR\.

02/04/2025

Andréa Rocha

Sumário

__RN00 – Regras Gerais 	2__

__RN01 – Parâmetros de Tela 	3__

__RN02 – Recuperação dos Dados 	4__

__RN03 – Gravação os Dados na Versão 1\.00 	5 __

__RN04 – Gravação os Dados na Versão 2\.00 	10__

__                                            RN00 \- Regras Gerais                                                          __

Esta geração lê a tabela das    guias de recolhimento da GNRE Online e gera um arquivo XML a ser transmitido para as UF’s através do portal da GNRE Online\.

__Estrutura do arquivo:__

O arquivo XML será gerado de acordo com as orientações de preenchimento do portal da GNRE Online \([www\.gnre\.gov,br](http://www.gnre.gov,br)\), na seguinte opção:

__    Automação 🡪 Manual para Preenchimento do XML de Lote 🡪 aba “Formato do Arquivo”__

 

O arquivo poderá ser gerado na versão 1\.00 \(vrs\. original\) ou 2\.00 da GNRE Online, de acordo com a opção do usuário no parâmetro “Versão”\.

 

__MFS27985__: Alterada a geração do XML para considerar a nova versão 2\.00, válida a partir de Jan/2020\. 

__Atualização das guias processadas:__

Cada guia processada, ou seja, levada para o arquivo XML, terá o seguinte campo da tabela das guias atualizado:

                                      Campo “Indicador de gravação no arquivo XML” = “S”

	

__Nome dos arquivos:__

O nome dos arquivos será uma concatenação de várias informações, dependendo da forma de geração escolhida pelo usuário:

__MFS602689:__ alterou a nomenclatura do arquivo quanto as informações de versão e do volume:

Na geração dos arquivos separados por UF 🡪  ESTAB\_999999\_XX\_999999\_A\_999999\_Vnn\_VERSAO\_YY

                                                                                        \(cod estab\) \(uf\) \(data ini\)    \(data fim\) \(volume\)

Quando a geração *não* for por UF 🡪  ESTAB\_999999\_999999\_A\_999999\_Vnn\_VERSAO\_YY

                                                                       \(cod estab\) \(data ini\)   \(data fim\) \(volume\)

Na geração dos arquivos separados por UF 🡪  ESTAB\_999999\_XX\_999999\_A\_999999\_VERSAO\_YY\_V\_nnn\.XML

                                                                                        \(cod estab\) \(uf\) \(data ini\)    \(data fim\)       \(versão\)             \(volume\)

Quando a geração *não* for por UF 🡪  ESTAB\_999999\_999999\_A\_999999\_VERSAO\_YY\_V\_nnn\.XML

                                                                       \(cod estab\) \(data ini\)   \(data fim\)      \(versão\)            \(volume\)

Onde:

- “Vnn”: como a quantidade de guias no arquivo é limitada, será utilizado “Vnn” para indicar o volume \(V01, V02, V03, etc\.\.\.\)\.
- “V\_nnn”: como a quantidade de guias no arquivo é limitada, será utilizado “V\_nnn” para indicar o volume \(V\_001, V\_002, V\_003, etc\.\.\.\)\.
- “VERSAO\_YY”: igual a “VERSAO\_01” ou “VERSAO\_02”, dependendo da Versão selecionada na tela de geração\.

Exemplo:  “ESTAB\_ICMS\_MG\_010313 \_A\_310313\_VERSAO\_02\_V\_001”

                 “ESTAB\_ICMS\_010313 \_A\_310313\_VERSAO\_02\_V\_001”

__Quantidade de guias por arquivo__:

Cada arquivo terá no máximo 50 guias, conforme a orientação que consta no portal da GNRE Online\.

__MFS602689__

A execução da rotina gravará um único número de processo para todas as UF’s selecionadas para geração de um determinado estabelecimento\. Antes dessa MFS era criado um processo para cada UF\.

# <a id="_Toc24450454"></a><a id="_Toc24451353"></a><a id="_Toc24451819"></a>                                       RN01 \- Parâmetros de Tela                                                        

__Período de Apuração das Guias__

Neste campo o usuário informará uma data inicial e final, que limitará um período para a recuperação das guias a serem geradas no arquivo\.

__Receita__ 

Este campo é uma lista dos códigos de receita da GNRE \(módulo ICMS, menu Manutenção🡪 Códigos GNRE 🡪 Códigos de Receita\) \+ a opção “Todas”\. Na abertura da tela o campo deve mostrar a opção “Todas” como default\.

__Considerar as guias já geradas anteriormente__ 

Campo do tipo S/N\. Default = “N” \(desmarcado\)\. 

Se desmarcado, as guias já processadas, ou seja, já geradas em arquivo anteriormente, não serão consideradas no processamento\.

Se marcado, as guias já processadas serão consideradas normalmente\.

__Gerar arquivos separados para cada UF__ 

Campo do tipo S/N\. Default = “N” \(desmarcado\)\. 

Se desmarcado, os arquivos XML serão gerados por Estabelecimento, e poderão conter guias de diferentes UF’s favorecidas\.

Se marcado, os arquivos XML serão gerados por Estabelecimento e UF, e assim, cada arquivo conterá apenas guias de uma única UF favorecida\.

\(nos dois casos, a quantidade de guias por arquivo é limitada em 50, conforme manual da GNRE\) 

<a id="_Hlk44338749"></a>__Considerar as guias em que a UF Favorecida = UF do estabelecimento__

Campo do tipo S/N\. Default = “N” \(__*desmarcado*__\)\. 

Se desmarcado, as guias em que a UF FAVORECIDA = UF do Estabelecimento da geração, serão desconsideradas do processo\. Ou seja, *não* serão gravadas no arquivo XML\.

Se marcado, as guias em que a UF FAVORECIDA = UF do Estabelecimento da geração, serão consideradas normalmente no processo\. Ou seja, serão gravadas no arquivo XML\.

*\(Parâmetro criado na *__*MFS34140*__*\)*

__*Obs*__*: Esta solução foi escolhida porque não impacta na rotina de geração das guias, que é bastante complexa, pois trabalha com diferentes tipos de geração, dependendo das regras de cada UF, e da receita a ser gerada\. Assim, se fôssemos alterar a geração das guias, teríamos váris pontos a serem alterados e validados\. Alterando apenas a geração do arquivo XML, o impacto é infinitamente menor\. Para adotar esta solução, consideramos também que a GNRE Online foi desenvolvida em *__*2013*__*, e temos inúmeros usuários que a utilizam, sem relatar dificuldades na geração dos XML\. O detalhe esta na forma de gerar\. Se o usuário gerar de cada vez, apenas os estabelecimentos de mesma UF, e não marcar esta UF no quadro “Seleção das UF’s para Geração”, as guias referentes às operações internas não serão gravadas no arquivo\.*

__Versão__

Este campo é uma lista com as seguintes opções:

\- Versão 1\.00

\- Versão 2\.00

*\(Parâmetro criado na MFS27985\)*

__Seleção das UF’s para geração __

Neste campo será exibida a relação de todas as UF’s da TACES78 \(Unidades da Federação da GNRE Online\), e o usuário poderá selecionar as UF’s desejadas\. Como facilitador, serão disponibilizadas opções para marcar ou desmarcar todas as UF’s exibidas\.

__Estabelecimentos__

Neste campo serão demonstrados todos os estabelecimentos da empresa do login, e o usuário selecionará os estabelecimentos desejados para efetuar a geração\.

#                                        RN02 – Recuperação dos Dados                                                        

__Origem dos Dados__:  Tabela das guias de recolhimento da GNRE Online

                                   TACES78 \(Unidades da Federação da GNRE Online\)

__Processamento__:

Para cada estabelecimento selecionado em tela, será feita a geração dos arquivos XML\.

Na recuperação dos dados na tabela das guias, serão consideradas apenas as guias cuja UF favorecida seja uma das UF’s selecionadas em tela na opção “*Seleção das UF’s para geração*”\.

Critérios básicos para a recuperação dos dados na tabela das guias:

\- Empresa 🡪 empresa do login

\- Estabelecimento 🡪 estabelecimento em processamento 

\- Data Apuração 🡪 deve ser uma data que se enquadre no período de datas informado na tela

\-UF Favorecida 🡪 deve ser uma UF selecionada em tela \(alteração __MFS34140__\)

\-UF Favorecida 🡪 dependendo da opção do parâmetro “*Considerar as guias em que a UF *

*  Favorecida = UF do estabelecimento*”:

     Se parâmetro desmarcado:

          Neste caso, a UF Favorecida da guia, deve atender às seguintes condições:

         \- Deve ser uma UF selecionada em tela \(campo “*Seleção das UF’s para geração*”\);

            __e__

         \- Deve ser uma UF <> UF do estabelecimento da geração;

        \(neste caso, as guias em que a UF Favorecida = UF do Estabelecimento, *não* serão 

         consideradas para gravação no XML\)

 

      Se parâmetro marcado:

           Neste caso, basta que a UF Favorecida seja uma UF selecionada em tela \(campo “*Seleção *

*           das UF’s para geração*”\); 

\-Receita 🡪dependendo do parâmetro de tela:

      Se parâmetro “*Receita*” = “Todas”

           Neste caso serão consideradas as guias de qualquer receita;

      Senão 

          Neste caso serão consideradas apenas as guias da receita informada em tela; 

\- Indicador de gravação no arquivo XML 🡪 dependendo do parâmetro de tela:

      Se parâmetro “*Considerar as guias já geradas anteriormente*” = “S”

           Neste caso serão consideradas todas as guias, mesmo as já geradas anteriormente;

      Senão 

          Neste caso serão consideradas *apenas* as guias que ainda não foram gravadas no arquivo, 

          ou seja, as guias com o “*Indicador de Gravação no Arquivo XML*” = “N”;

__Forma de geração: __

Ao gerar os arquivos, as guias de cada estabelecimento poderão ser geradas num único arquivo, independente da UF, ou em arquivos separados por UF \(UF favorecida\), de acordo com a opção escolhida em tela no parâmetro “*Gerar arquiovos separados para cada UF*”, da seguinte forma:

Se desmarcado 🡪 os arquivos XML serão gerados por Estabelecimento, e poderão conter guias de diferentes UF’s favorecidas\.

Se marcado 🡪 os arquivos XML serão gerados por Estabelecimento e UF, e assim, cada arquivo conterá apenas guias de uma única UF favorecida\.

\(nos dois casos, a quantidade de guias por arquivo é limitada em 50, conforme manual da GNRE\) 

As guias recuperadas serão geradas no layout na versão 1\.00 ou 2\.00, de acordo com a opção informada pelo usuário no campo versão: *\(A versão 2\.00 foi implementada na MFS27985\)*

Versão 1\.00

Ver regras da geração no item __RN03__

Versão 2\.00

Ver regras da geração no item __RN04__

 

# <a id="_Toc24450456"></a><a id="_Toc24451355"></a><a id="_Toc24451821"></a>                          RN03 – Gravação dos Dados na Versão 1\.00

O layout do XML da versão __1\.00__ consta no site da GNRE Online \([www\.gnre\.gov\.br](http://www.gnre.gov.br)\), opção “Automação”, consultar o “*Manual para Preenchimento do XML de Lote*” na aba “Formato do Arquivo”\.

As guias serão gravadas no arquivo seguindo as regras específicas de cada campo, conforme descrito no quadro abaixo\.

__OBS__ 🡪A geração de alguns campos depende da parametrização da  UF/Receita \(TACES78 – UF’s da GNRE Online\)\. Para consultar a TACES78 são utilizados os campos “UF Favorecida” e “Receita” da guia\.

__Campos do Arquivo XML__

__Origem da informação __

c01\_UfFavorecida                 \(A/2\)

Campo “UF Favorecida” da tabela das guias

c02\_receita                            \(N/6\)

Campo “Receita” da tabela das guias

Campos de identificação do emitente:

c17\_inscricaoEstadualEmitente

c03\_idContribuinteEmitente

c16\_razaoSocialEmitente

c18\_enderecoEmitente

c19\_municipioEmitente

c20\_ufEnderecoEmitente

c21\_cepEmitente

c22\_telefoneEmitente

c27\_tipoIdentificacaoEmitente

O preenchimento destes campos depende se o estabelecimento possui ou não uma IE na UF favorecida, da seguinte forma:

__Se__ o Estab possui um IE na UF Favorecida 

      \(módulo Parâmetros, cadastro “Inscrições Estaduais”\)

    A IE é gravada no campo “c17\_inscricaoEstadualEmitente”; 

    Os demais campos e suas respectivas tag’s *não* são gerados 

    no arquivo;

__Senão__

    O campo “c17\_inscricaoEstadualEmitente” e sua tag *não* são

    gerados no arquivo\. Os demais campos são preenchidos

    com as informações do cadastro do estabelecimento \(módulo

    Parâmetros\), da seguinte forma:

     \-c03\_idContribuinteEmitente – este campo contém dois campos:

       <CPF> e <CNPJ>, mas apenas um será gerado, dependendo da

       informação que consta no cadastro do Estabelecimento\. Ao

       preencher um destes campos, o outro e sua respectiva tag __não__

__      __ será gerado no arquivo\.

     \-c16\_razaoSocialEmitente – razão social 

     \-c18\_enderecoEmitente – concatenação dos campos:

                              \(endereço \+ “,“ \+ numero \+ “,” \+ complemento\)

     \-c19\_municipioEmitente – código do município

              Obs: Somente os cinco dígitos do código, sem utilizar os

              dígitos da UF, como o padrão de várias obrigações\. 

__      \[ALTERADA – CH26354\_2013\]__

__              Tratamento:__

      \- Quando o código do município for menor que 5 dígitos completar com zeros a esquerda\.

     \-c20\_ufEnderecoEmitente – sigla da UF

     \-c21\_cepEmitente – número do CEP

     \-c22\_telefoneEmitente – concatenação do DDD \+ Telefone

__      \[ALTERADA – CH26354\_2013\]__

            __Tratamento:__

__    __  \- 1ª situação – Se o campo DDD estiver preenchido apenas com os 2 primeiros dígitos buscar informação concatenando com a informação do campo telefone, mas se o início do campo DDD ultrapassar os 2 primeiros dígitos pular para a 2ª situação\.

      \- 2ª situação – Caso o campo concatenado estiver preenchido com mais de 11 dígitos, buscar da seguinte forma:

          \- Para campo Telefone com 8 posições, verificar DDD, se estiver maior que 3 dígitos buscar as 3 últimas posições\.

          \- Para campo Telefone com 9 posições, verificar DDD, se estiver maior que 2 dígitos buscar as 2 últimas posições\.

__              Exemplo:__              

      \- em casos em que o campo Telefone tem 8 dígitos 1121590500, 01121590500, em casos em que o campo Telefone tem 9 dígitos 11956561010\. Esse campo deve atingir até 11 posições\. 

     \-c27\_tipoIdentificacaoEmitente – o preenchimento deste campo

            depende do conteúdo gravado no campo c03, como segue:

            Se conteúdo for um CNPJ 🡪 será gravado com “1”

            Se conteúdo for um CPF 🡪 será gravado com “2”

c04\_docOrigem

c28\_tipoDocOrigem

Se o campo “Tipo do Documento de Origem” da guia = nulo

    Estes campos e suas respectivas tag’s *não* serão gerados no

    arquivo

Senão 

     Os campos serão gravados com o conteúdo dos seguintes   

     campos da guia:

         c04\_docOrigem 🡨 campo documento de origem

         c28\_tipoDocOrigem 🡨 tipo do documento de origem

                                               \(preencher os zeros à esq quando for o 

                                               caso, exemplo 🡪 quando for “01\-Nota 

                                               Fiscal Avulsa”, deverá ser gravado “01”\)

c05\_referencia

Como pode ser visto no layout do arquivo, este campo é composto de 4 outros campos:

<período>

<mês>

<ano>

<parcela>

A geração destes campos no arquivo dependerá do conteúdo dos seguintes campos da tabela das guias:

Campo “Período de Referência”

Campo “Mês e Ano de Referência”

Campo “Parcela”

A geração será feita da seguinte forma:

Se estes três campos da tabela estiverem nulos:

      Neste caso o “__campo c05\_referencia__”, e os 4 campos que o

      compõe,  e todas as respectivas tag’s, __não__ serão gerados no 

      arquivo;

Senão

      Neste caso o campo c05\_referencia será gerado apenas com

      os campos que apresentarem conteúdo na tabela, da

      seguinte forma:

      <período> 🡨 campo “Período”

      <mês> 🡨 campo “Mês e Ano de Referência” \(2 primeiros dígitos\)

      <ano> 🡨 campo “Mês e Ano de Referência” \(4 últimos dígitos\)

      <parcela> 🡨 campo “Parcela”

c06\_valorPrincipal

Se o campo “Valor Principal” da guia = nulo

    Este campo e sua tag *não* serão gerados no arquivo

Senão 

     O campo será gravado com o conteúdo do valor principal da guia;

__\[ALTERADA – CH26354\-B\_2013\]__

__Tratamento: __O valor deve estar no seguinte formato: '\[0\.00 a 9999999999\.99\]' ou '0'\. 

c10\_valorTotal

Se o campo “Valor Total” da guia = nulo

    Este campo e sua tag *não* serão gerados no arquivo

Senão 

     O campo será gravado com o conteúdo do valor total da guia;

__\[ALTERADA – CH26354\-B\_2013\]__

__Tratamento: __O valor deve estar no seguinte formato: '\[0\.00 a 9999999999\.99\]' ou '0'\.

c14\_dataVencimento

Campo “Data Vencimento” da guia

 c15\_convenio

Se o campo “Convenio” da guia = nulo

    Este campo e sua tag *não* serão gerados no arquivo

Senão 

     O campo será gravado com o conteúdo do convenio da guia;

c25\_detalhamentoReceita

Se o campo “Detalhamento Receita” da guia = nulo  \(vide OBS\)

    Este campo e sua tag *não* serão gerados no arquivo

Senão 

     O campo será gravado com o conteúdo do campo “Detalhamento

      Receita” da guia\.

Obs: Como este campo *não* é obrigatório nas guias, muitas vezes ele estará sem informação\.

c26\_produto

Se o campo “Produto” da guia = nulo \(vide OBS\)

    Este campo e sua tag *não* serão gerados no arquivo

Senão 

     O campo será gravado com o conteúdo do produto da guia;

Obs: Como este campo *não* é obrigatório nas guias, muitas vezes ele estará sem informação\.

c33\_dataPagamento

Campo “Data Pagamento” da guia

Campos de identificação do destinatário:

c36\_inscricaoEstadualDestinatario

c35\_idContribuinteDestinatario

c37\_razaoSocialDestinatario

c38\_municipioDestinatario

c34\_tipoIdentificacaoDestinatario

\(vide OBS abaixo sobre a IE do destinatário\)

O preenchimento destes campos depende do conteúdo gravado na pessoa fis/jur destinatária da guia:

 

__Se__ o campo “Código da Pessoa Fis/Jur Destinatario” da guia = nulo

      Estes campos e suas respectivas tag’s *não* serão gerados no

      arquivo\.

__Senão__

       Neste caso serão utilizados os dados do cadastro da pessoa

       fis/jur \(SAFX04\), conforme regra a seguir:

        __Se__ campo “08\-Inscrição Estadual” da SAFX04

                                                                    = nulo ou “ISENTO”

              O campo “c36\_inscricaoEstadualDestinatário” e sua tag *não *

*             * serão gerados no arquivo\. Os demais campos serão

              preenchidos  com as informações da SAFX04:

          \-c35\_idContribuinteDestinatario – este campo contém dois

             campos: <CPF> e <CNPJ>, mas apenas um será gerado,

             dependendo da informação que consta no cadastro da

             pessoa fis/jur \(campo 06\)\. Ao preencher um destes campos,

             o outro e sua respectiva tag __não__ será gerado no arquivo\.

          \-c37\_razaoSocialDestinatario – razão social \(campo 05\)

          \-c38\_municipioDestinatario – código do município \(campo 25\)

                 Obs: Somente os cinco dígitos do código, sem utilizar os

                 dígitos da UF, como o padrão de várias obrigações\. 

          \-c34\_tipoIdentificacaoDestinatario \-  o preenchimento deste

                   campo depende do conteúdo gravado no campo c35,

                   como segue:

                   Se conteúdo for um CNPJ 🡪 será gravado c/“1”

                   Se conteúdo for um CPF 🡪 será gravado com “2”

__        Senão__

             A inscrição estadual da SAF04 será gravada no campo  

             “c36\_inscricaoEstadualDestinatário”;

             Os demais campos e suas respectivas tag’s *não* serão

             gerados no arquivo;

c39\_camposExtras

Como pode ser visto no layout do arquivo, são permitidos até 3 campos extras no XML, cada um deles com Código, Tipo e Valor:

\-<código> 🡪 é um código que identifica a informação, e segue uma

                      relação de campos extras da GNRE Online;

\-<tipo> 🡪 identifica o tipo da informação, se texto, número ou data;

\-<valor> 🡪contém a informação;

A geração destes campos no arquivo dependerá do conteúdo dos seguintes campos da tabela das guias:

\-Campo “Código do Campo Extra 1”, “2” e “3”

\-Campo “Tipo do Campo Extra 1”, “2’ e “3”

\-Campo “Conteúdo do Campo Extra 1”, “2” e “3”

A geração será feita da seguinte forma:

__SE__ “Código do Campo Extra 1” = nulo __e__

           “Código do Campo Extra 2” = nulo __e__

                “Código do Campo Extra 3” = nulo

      Neste caso o campo “__c39\_camposExtras__”, todos os campos

      que o compõe,  e todas as respectivas tag’s, __não__ serão gerados

      no arquivo;

__SENÃO__

      Neste caso o campo “__c39\_camposExtras__” será gerado apenas

      com os campos extras que apresentarem conteúdo na tabela, da

      seguinte forma:

      Se “Código do Campo Extra 1” <> nulo:

            Será gerado um campo extra no arquivo, com as  

             informações do primeiro campo extra da tabela:

            <codigo> 🡨 campo “Código do Campo Extra 1”

            <tipo> 🡨 campo “Tipo do Campo Extra 1”

            <valor> 🡨 campo “Conteúdo do Campo Extra 1” *\(ver Obs\);*

      Se “Código do Campo Extra 2” <> nulo:

            Será gerado um campo extra no arquivo, com as  

             informações do segundo campo extra da tabela:

            <codigo> 🡨 campo “Código do Campo Extra 2”

            <tipo> 🡨 campo “Tipo do Campo Extra 2”

            <valor> 🡨 campo “Conteúdo do Campo Extra 2” *\(ver Obs\);*

      Se “Código do Campo Extra 3” <> nulo:

            Será gerado um campo extra no arquivo, com as  

             informações do terceiro campo extra da tabela:

            <codigo> 🡨 campo “Código do Campo Extra 3”

            <tipo> 🡨 campo “Tipo do Campo Extra 3”

            <valor> 🡨 campo “Conteúdo do Campo Extra 3”  *\(ver Obs\);*

__Obs__: O campo <valor> é o que conterá de fato a informação\. Na sua gravação, serão observadas as seguintes regras:

\-Se tipo do campo = D 🡪 a data será gravada no formato AAAA\-MM\-DD 

\-Se tipo do campo = N 🡪 o número será gravado utilizando apenas ponto como separador das casas decimais\. Exemplo, para o valor 12\.450,95 seria gravado <valor>12450\.95</valor>\.

c42\_identificadorGuia

De acordo com o manual de preenchimento da GNRE Online, este campo é um identificador da guia no lote\. É um campo numérico e deve ser gerado pelo contribuinte\.

Para o seu preenchimento, as guias receberão um número sequencial no lote, que será de 1 a 50, já que a quantidade máxima de guias num arquivo é 50 \(como citado na RN00\-Regras Gerais\)\. 

__\[MFS534151\] __Alteração da regra de preenchimento da tag para a UF favorecida = SP\.

Se a UF favorecida for igual a “SP”

__     __Este campo e sua tag não serão gerados no arquivo\.

__Observação sobre a IE do destinatário:__ Nas situações em que o tipo de venda for = “FD”, e a UF da concessionária for diferente da UF da pessoa fis/jur destinatária, não há como identificar se o destinatário tem ou não uma IE na UF favorecida, que neste caso será a UF da concessionária\. Futuramente este detalhe poderá gerar uma demanda de alteração, já que pelas regras da GNRE Online, este campo deve ser preenchido sempre que o destinatário da nota tiver uma IE cadastrada na UF favorecida\. No momento a questão não será abordada, e no futuro, se for o caso, o assunto poderá ser estudado melhor\. 

# <a id="_Toc24450457"></a><a id="_Toc24451356"></a><a id="_Toc24451822"></a>                               RN04 – Gravação dos Dados na Versão 2\.00

*\(A versão 2\.00 foi implementada na MFS27985\)*

O layout do XML da versão __2\.00__ consta no site da GNRE Online \([www\.gnre\.gov\.br](http://www.gnre.gov.br)\), opção “Automação”, consultar o “*Manual para Preenchimento do XML de Lote*” na aba “Formato do Arquivo”\.

As guias serão gravadas no arquivo seguindo as regras específicas de cada campo, conforme descrito no quadro abaixo\.

__OBS__ 🡪Assim como na versão 1\.00, a geração de alguns campos depende da parametrização da UF/Receita \(TACES78 – UF’s da GNRE Online\)\. Para consultar a TACES78 são utilizados os campos “UF Favorecida” e “Receita” da guia\.

\[__MFS64168__\]Tratamento dos Campos de “contribuinteEmitente”, ”contribuinteDestinatario” e dos Campos não obrigatórios\.

__\[MFS74539\] __Tratamento dos Campos Detalhamento da Receita, Detalhamento de Produto e Tipo de Documento Origem para serem preenchidos ou não, ou __se nulo__, conforme Parâmetro por UF\.

__\[MFS78478\] __Tratamento dos Campos Período e Mês e Ano para serem preenchidos ou não, conforme Parâmetro por UF\.

__\[MFS544156\] __Inclusão da geração dos novos campos Valor Principal FECP e Valor Total FECP na tag Valor\.

\[__MFS792095\] __Alteração da regra de preenchimento do campo Inscrição Estadual \(IE\) do contribuinte emitente para UF=PR

__Campos do Arquivo XML__

__Origem da informação __

ufFavorecida                 \(A/2\)

Campo “UF Favorecida” da tabela das guias

tipoGnre

Este campo será gerado sempre com “0” \(zero\)

__Obs__\.: Na implementação da versão 2\.00 \(__MFS27985__\), apenas a geração do XML foi alterada para considerar o novo layout\. Por isso, o campo __tipoGnre__ é gerado sempre com “0”, que corresponde à forma como as guias são geradas na rotina da Geração dos Dados\. Conforme alinhamento feito com o PO e Informação, as modalidades “1” e “2” *não serão tratadas*\. \(1 = Guia com múltiplos documentos de origem e 2 = Guia com Múltiplas Receitas\)\.

Campos de identificação do emitente:

<contribuinteEmitente>  
   <identificacao>  
    <CPF>\.\.\.</CPF>  
    <CNPJ>\.\.\.</CNPJ>  
    <IE>\.\.\.</IE>  
   </identificacao>  
   <razaoSocial>\.\.\.</razaoSocial>  
   <endereco>\.\.\.</endereco>  
   <municipio>\.\.\.</municipio>  
   <uf>\.\.\.</uf>  
   <cep>\.\.\.</cep>  
   <telefone>\.\.\.</telefone>  
  </contribuinteEmitente>

\[MFS64188\] Correção da regra de geração das Tag’s de IE ou demais campos\.

O preenchimento destes campos depende se o estabelecimento possui ou não uma IE na UF favorecida, da seguinte forma:

Tratamento: 

__Se__ o Estabelecimento possui um IE na UF Favorecida 

      \(módulo Parâmetros, cadastro “Inscrições Estaduais”\)

     __Se__ a UF Favorecida = “PR” __E__ a inscrição estadual 

          especial – ICMS\-ST estiver preenchida

          A inscrição estadual especial será gravada no campo __<IE>__; 

          *Os demais campos*, e respectivas tag’s, *não serão   *

          *gerados*;

__     Senão__

           A inscrição estadual será gravada no campo __<IE>__; 

           *Os demais campos*, e respectivas tag’s, *não serão   *

           *gerados*

__Senão__

    *O campo da *__*IE*,__ e sua respectiva tag *não* será gerado;

    Os demais campos serão preenchidos com as informações do 

     cadastro do estabelecimento \(módulo Parâmetros\), da seguinte

     forma:

       __<CPF>__ e __<CNPJ>__ \- Apenas um destes campos será gerado, 

       dependendo da informação que constar no cadastro do

       Estabelecimento\. Ao preencher um destes campos, o outro e

       sua respectiva tag não será gerado;

      __<razão Social>__ \- Razão social do estabelecimento; 

      __<endereço>__ \- Concatenação dos campos:

                          \(endereço \+ “,“ \+ numero \+ “,” \+ complemento\);

      __<município>__ \- Código do município do estabelecimento\.

        Serão informados apenas os cinco dígitos do código, sem

        utilizar os dígitos da UF \(dois primeiros dígitos\)\. Quando o

        código do município for menor que 5 dígitos, completar com

        zeros a esquerda;

\.

      __<uf>__ \- Sigla da UF do estabelecimento;

      __<cep>__ \- Número do CEP do estabelecimento;

         Considerar 8 posições, para não desconsiderar o zero a esquerda\.

       __<telefone>__ – Concatenação do DDD \+ Telefone do

        Estabelecimento \(DDDnnnnnnnn\)\. Nos casos em que o

        número do telefone tiver 9 dígitos, utilizar no DDD apenas os

        dois últimos dígitos \(ex: ao invés de 021, informar apenas 21\);

receita                                        \(N/6\)

Campo “Receita” da tabela das guias

detalhamentoReceita

O campo será gravado com o conteúdo do campo “Detalhamento

      Receita” da guia\.

__Ou__

__ Se__ o campo “Detalhamento Receita” da guia = nulo

__E__

 __Se Marcado:__  O Parâmetro por UF \(Tabela ICT\_GNRE\_OL\_UF\),  Campo IND\_DET\_RECEITA \(Detalhamento da Receita\) estiver igual à “__S__”;

    Este campo e sua tag serão gerados no arquivo

__Ou__

__Se Desmarcado:__ O Parâmetro por UF \(Tabela ICT\_GNRE\_OL\_UF, Campo IND\_DET\_RECEITA \(Detalhamento da Receita\) estiver igual à “__N__”; 

    Este campo e sua tag *não* serão gerados no arquivo

     

\(Vide OBS\)\.

documentoOrigem

O campo será gerado a partir dos seguintes campos da guia:

     Tipo do documento – Tipo do Documento de Origem da guia;

     Documento Origem \- Documento de Origem da guia;

  

Observar que, diferente da versão 1\.00, na versão 2\.00 o tipo do documento é informado no atributo “tipo” da tag:

      <documentoOrigem tipo="\.\.\." >\.\.\.</documentoOrigem>

__Ou __

__  Se __o campo “Tipo do Documento de Origem” da guia = nulo

__E__

 __Se Marcado:__ O Parâmetro por UF \(Tabela ICT\_GNRE\_OL\_UF\), IND\_DOC \(Documento\) estiver igual à “__S__”;  

    Este campo e sua respectiva tag __será__ gerado no arquivo\.

__Ou__

 __Se Desmarcado:__ O Parâmetro por UF \(Tabela ICT\_GNRE\_OL\_UF Campo IND\_DOC \(Documento\) estiver igual à “__N__” \-; 

    Este campo e sua respectiva tag __*não*__ será gerado no arquivo\.

\(Vide OBS\)\.

produto

__\[MFS585714\] __Inclusão do tratamento para gerar a guia por Apuração, informando o produto \(Classificação do Produto da GNRE\)\.

O campo será gravado com o conteúdo do produto da guia

     \(coluna COD\_PROD\_GNRE\);

__Ou__

__Se __o campo “Tipo do Documento de Origem” da guia = nulo

__E__

__Se Marcado:__ O Parâmetro por UF \(Tabela ICT\_GNRE\_OL\_UF\), IND\_DET\_PRODUTO \(Detalhamento do Produto\) estiver igual à “__S__”

__OU__ IND\_DET\_PROD\_APUR \(Detalhamento do Produto – Por Apuração\) estiver igual à “__S__”;   

    Este campo e sua respectiva tag __será__ gerado no arquivo\.

__Ou__

__Se Desmarcado:__ O Parâmetro por UF \(Tabela ICT\_GNRE\_OL\_UF Campo IND\_DET\_PRODUTO \(Detalhamento do Produto\) estiver igual à “__N__”;  

      Este campo e sua tag __*não*__ serão gerados no arquivo

     

\(Vide OBS\)

Campos de referência da guia:

  <referencia>  
     <periodo>\.\.\.</periodo>  
     <mes>\.\.\.</mes>  
     <ano>\.\.\.</ano>  
     <parcela>\.\.\.</parcela>  
  </referencia>

Como pode ser visto no layout, a referência é composta de 4 outros campos:

<período>

<mês>

<ano>

<parcela>

A geração destes campos no arquivo depende do conteúdo dos seguintes campos da tabela das guias:

A geração será feita da seguinte forma:

__\[MFS78478\] __

\- __Campo “Período de Referência”__

__Se Marcado:__ O Parâmetro por UF \(Tabela ICT\_GNRE\_OL\_UF\), IND\_PERIODO \(Período de Referência\) estiver igual à “__S__”;   

    Este campo e sua respectiva tag __será__ gerado no arquivo\.

__Ou__

__Se __o campo “Período de Referência” da guia = nulo

      A tag deverá ser gerada no arquivo

__Ou__

__Se Desmarcado:__ O Parâmetro por UF \(Tabela ICT\_GNRE\_OL\_UF Campo IND\_PERIODO \(Período de Referência\) estiver igual à “__N__”;  

      Este campo e sua tag __*não*__ serão gerados no arquivo\.

\- __Campo “Mês e Ano de Referência”__

__Se Marcado:__ O Parâmetro por UF \(Tabela ICT\_GNRE\_OL\_UF\), IND\_MES\_ANO \(Mês e Ano\) estiver igual à “__S__”;   

    Este campo e sua respectiva tag __será__ gerado no arquivo\.

__Ou__

__Se __o campo “Mês e Ano” da guia = nulo

      A tag deverá ser gerada no arquivo

__Ou__

__Se Desmarcado:__ O Parâmetro por UF \(Tabela ICT\_GNRE\_OL\_UF Campo IND\_MES\_ANO \(Mês e Ano\) estiver igual à “__N__”;  

      Este campo e sua tag __*não*__ serão gerados no arquivo

\- __Campo “Parcela”__

Campo <Parcela> não é obrigatório, só preencher se for maior que zero\.

Preencher com os campos conforme abaixo: 

<período> \- campo “Período”;

<mês> \- campo “Mês e Ano de Referência” \(2 primeiros dígitos\);                                                                               

<ano> \- campo “Mês e Ano de Referência” \(4 últimos dígitos\);

<parcela> \- campo “Parcela”\.

Se estes três campos da tabela estiverem nulos:

      Neste caso o “__referência__”, e os 4 campos que o compõem, e

      todas as respectivas tag’s, *não* serão gerados no arquivo;

Senão

      Neste caso o campo “__referência__”__ __será gerado apenas com

      os campos que apresentarem conteúdo na tabela, da

      seguinte forma:

\(Vide OBS\)

dataVencimento

Campo “Data Vencimento” da guia

Formato: AAAA\-MM\-DD

Obs\.: Campo de preenchimento obrigatório\.

Valor

      <valor tipo="\.\.\." >\.\.\.</valor>

__Obs__\.: Os tipos 12 e 22 não serão utilizados, porque na geração dos dados as guias são geradas sempre apenas para um tipo de valor, ICMS ou FECEP\. Não é feita geração de guias destacando os dois valores na mesma guia \(ICMS e FECEP\)\. As guias de FECEP são sempre geradas individualmente, para as receitas 100137 e 100129\. E desta forma, conforme testes realizados no site, os valores são gerados sempre com 11 ou 21\.

Na versão 2\.00 o campo Valor tem um atributo: o “tipo”\. Este tipo que indica quando é o valor principal ou o valor total da guia, e também quando se trata de valor de ICMS ou FECEP\.

Desta forma, teremos a seguinte situação:

Se campo “*Valor Principal*” da guia estiver preenchido:

      Será gerada uma linha no arquivo com o conteúdo do campo 

      “Valor Principal”, e com tipo = “__11__”;

Se campo “*Valor Total*” da guia estiver preenchido:

      Será gerada uma linha no arquivo com o conteúdo do campo

      “Valor Total” da guia, e com tipo = “__21__”;

Observar que na tabela das guias, cada guia poderá ter um, ou os dois valores preenchidos \(Valor Principal e Valor Total\)\. Assim, quando os dois estiverem preenchidos, o XML terá duas linhas de valor, que será identificado pela informação do tipo\.

 

\(Para o valor, usar apenas o ponto como separador dos decimais\)

Obs\.: Campo de preenchimento obrigatório\.

Valor

      <valor tipo="\.\.\." >\.\.\.</valor>

__Obs__\.: Os tipos 12 e 22 passarão a ser utilizados, porque na geração dos dados, as guias serão geradas com os dois tipo de valor, ICMS e FECEP\. Essa geração será feita somente para os códigos de receita 10011\-0 e 10010\-2\.  

__\[MFS544156\] __Inclusão da geração dos novos campos Valor Principal FECP e Valor Total FECP na tag Valor, quando a UF favorecida = ‘RJ’ ou ‘RS’ ou ‘SE’ ou ‘RO’\.

Na versão 2\.00 o campo Valor tem um atributo: o “tipo”\. Este tipo que indica quando é o valor principal ou o valor total da guia, e também quando se trata de valor de ICMS ou FECEP\.

Desta forma, teremos a seguinte situação, quando a UF favorecida = ‘RJ’ ou ‘RS’ ou ‘SE’ ou ‘RO’:

Se campo “*Valor Principal*” da guia estiver preenchido:

      Será gerada uma linha no arquivo com o conteúdo do campo 

      “Valor Principal”, e com tipo = “__11__”;

Se campo “*Valor Principa FECP*” da guia estiver preenchido:

      Será gerada uma linha no arquivo com o conteúdo do campo 

      “Valor Principal”, e com tipo = “__12__”;

Se campo “*Valor Total*” da guia estiver preenchido:

      Será gerada uma linha no arquivo com o conteúdo do campo

      “Valor Total” da guia, e com tipo = “__21__”;

Se campo “*Valor TotaL FECP”*” da guia estiver preenchido:

      Será gerada uma linha no arquivo com o conteúdo do campo

      “Valor Total” da guia, e com tipo = “__22__”;

Observar que na tabela das guias, cada guia poderá ter um, ou os dois valores preenchidos \(Valor Principal e Valor Total\)\. Assim, quando os dois estiverem preenchidos, o XML terá duas linhas de valor, que será identificado pela informação do tipo\.

 

\(Para o valor, usar apenas o ponto como separador dos decimais\)

Obs\.: Campo de preenchimento obrigatório\.  Os tipos 12 e 22 só devem ser gerados se o valor for maior que zero\.

convenio

Se o campo “Convenio” da guia = nulo

    Este campo e sua respectiva tag, *não* será gerado no arquivo

Senão 

     O campo será gravado com o conteúdo do convenio da guia;

Obs\.: Campo não Obrigatório\.

Campos de identificação do destinatário:

<contribuinteDestinatario>  
   <identificacao>  
      <CPF>\.\.\.</CPF>  
      <CNPJ>\.\.\.</CNPJ>  
      <IE>\.\.\.</IE>  
   </identificacao>  
   <razaoSocial>\.\.\.</razaoSocial>  
   <municipio>\.\.\.</municipio>  
</contribuinteDestinatario>

O preenchimento destes campos depende do conteúdo gravado na pessoa fis/jur destinatária da guia:

 

__Se__ o campo “Código da Pessoa Fis/Jur Destinatario” da guia = nulo

      Estes campos e suas respectivas tag’s *não* serão gerados no

      arquivo\.

__Senão__

       Neste caso serão utilizados os dados do cadastro da pessoa

       fis/jur \(SAFX04\), conforme regra a seguir:

        __Se__ campo “08\-Inscrição Estadual” da SAFX04

                                                                    = nulo ou “ISENTO”

              O campo da __IE__ e sua tag *não *serão gerados no arquivo\.

              Os demais campos serão gerados com as informações da

              SAFX04, da seguinte forma:

              __<CPF>__ e __<CNPJ>__ \- Apenas um destes campos será

              gerado, dependendo da informação que constar no 

              cadastro da SAFX04 \(campo 06\)\. Ao preencher um

             destes campos, o outro e sua respectiva tag não será 

             gerado;

             __<razaoSocial> \-__ Razão Social da SAFX04 \(campo 05\);

             __<município>__ \-Código do município da SAFX04 \(campo 25\);

              Serão informados apenas os cinco dígitos do código, sem

              utilizar os dígitos da UF \(dois primeiros dígitos\)\. Quando o

              código do município for menor que 5 dígitos, completar com

              zeros a esquerda;

__        Senão__

             A inscrição estadual da SAFX04 será gravada no campo  

             da __IE__, e os demais campos e suas respectivas tag’s *não*  

             serão gerados no arquivo;

camposExtras

Como pode ser visto no layout do arquivo, são permitidos até 3 campos extras no XML, cada um deles com Código e Valor\.

 

\(diferente da versão 1\.00, onde existe também o <tipo>\)

\-<código> 🡪 É um código que identifica a informação, de acordo

                       com a lista de campos extras da GNRE Online;

\-<valor> 🡪 Contém a informação;

A geração destes campos no arquivo dependerá do conteúdo dos seguintes campos da tabela das guias:

\-Campo “Código do Campo Extra 1”, “2” e “3”

\-Campo “Tipo do Campo Extra 1”, “2’ e “3”

\-Campo “Conteúdo do Campo Extra 1”, “2” e “3”

A geração será feita da seguinte forma:

__SE__ “Código do Campo Extra 1” = nulo __e__

           “Código do Campo Extra 2” = nulo __e__

                “Código do Campo Extra 3” = nulo

      Neste caso o campo “__camposExtras__”, todos os campos

      que o compõe, e todas as respectivas tag’s, __não__ serão gerados

      no arquivo;

__SENÃO__

      Neste caso o campo “__camposExtras__” será gerado apenas

      com os campos extras que apresentarem conteúdo na tabela, 

      da seguinte forma:

      Se “Código do Campo Extra 1” <> nulo:

            Será gerado um campo extra no arquivo, com as  

             informações do primeiro campo extra da tabela:

            <codigo> 🡨 campo “Código do Campo Extra 1”

            <valor> 🡨 campo “Conteúdo do Campo Extra 1” *\(ver Obs\);*

      Se “Código do Campo Extra 2” <> nulo:

            Será gerado um campo extra no arquivo, com as  

             informações do segundo campo extra da tabela:

            <codigo> 🡨 campo “Código do Campo Extra 2”

            <valor> 🡨 campo “Conteúdo do Campo Extra 2” *\(ver Obs\);*

      Se “Código do Campo Extra 3” <> nulo:

            Será gerado um campo extra no arquivo, com as  

             informações do terceiro campo extra da tabela:

            <codigo> 🡨 campo “Código do Campo Extra 3”

            <valor> 🡨 campo “Conteúdo do Campo Extra 3”  *\(ver Obs\);*

__Obs__: O campo <valor> é o que conterá de fato a informação\. Na sua gravação, serão observadas as regras abaixo, de acordo com o tipo do campo \(campo “Tipo do Campo Extra 1”, “2” e “3” da tabela das guias\):

\-Se tipo do campo = D 🡪 a data será gravada no formato AAAA\-MM\-DD 

\-Se tipo do campo = N 🡪 o número será gravado utilizando apenas ponto como separador das casas decimais\. Exemplo, para o valor 12\.450,95 será gravado <valor>12450\.95</valor>\.

Obs\.: Campos não obrigatórios\.

valorGnre

__\[MFS544156\] __Alteração do preenchimento da tag ValorGnre para utilizar o nova campo de Valor Gnre

Este campo será gerado com o valor do campo Valor GNRE da tabela das guias\.

Se o campo Valor GNRE não estiver preenchido

      Este campo será gerado com o valor do campo Valor Total da tabela das guias\.

Caso o Valor Total não esteja preenchido, será utilizado o conteúdo do campo Valor Principal\.

O número será gravado utilizando apenas ponto como separador das casas decimais\. Exemplo, para o valor 12\.450,95 será gravado 12450\.95\.

Obs\.: Nas guias, os campos Valor Total e Valor Principal são gerados com o mesmo valor, mas nem sempre os dois estarão preenchidos, o que depende das regras específicas de cada UF\.

Obs\.: Como a versão 2\.00 será gerada somente com guias simples, ou seja, com o campo tipo Gnre = “0” \(Guia Simples\), este valor será o próprio valor da guia\. 

 

Obs\.: Campo de preenchimento obrigatório\.

dataPagamento

Campo “Data Pagamento” da guia

Formato: AAAA\-MM\-DD

Obs\.: Campo de preenchimento obrigatório\.

identificadorGuia

De acordo com o manual de preenchimento da GNRE Online, este campo é um identificador da guia no lote\. É um campo numérico e deve ser gerado pelo contribuinte\.

Para o seu preenchimento, as guias receberão um número sequencial no lote, que será de 1 a 50, já que a quantidade máxima de guias num arquivo é 50 \(como citado na RN00\-Regras Gerais\)\. 

Obs\.: Este campo não consta no exemplo do layout versão 2\.00 da aba “Formato do Arquivo” do site\. Mas consta da aba “Dicionário” para a versão 2\.00\.

Obs\.: Campo não obrigatório\.

__\[MFS534151\] __Alteração da regra de preenchimento da tag para a UF favorecida = SP\.

Se a UF favorecida for igual a “SP”

__     __Este campo e sua tag não serão gerados no arquivo\.

= = = = =

