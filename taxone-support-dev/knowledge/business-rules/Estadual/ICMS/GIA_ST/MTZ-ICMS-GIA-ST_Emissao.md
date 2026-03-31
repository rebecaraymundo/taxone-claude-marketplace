# MTZ-ICMS-GIA-ST_Emissao

- **Fonte:** MTZ-ICMS-GIA-ST_Emissao.docx
- **Modificado:** 2026-03-05
- **Tamanho:** 40 KB

---

# 0Módulo Estadual – ICMS – GIA\-ST – Emissão

__Localização__: Menu Estadual, Módulo ICMS, item de menu Apuração à Guias de Recolhimento à Guia de Informação de Substituição Tributária à Emissão

Obs: As regras deste documento estão numeradas de acordo com a numeração dos campos no layout da GIA\-ST\. Regras gerais poderão ser incluídas na RN00\.

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3298

Alteração da GIA\-ST e GNRE para considerar o valor dos lançamentos complementares\.

A geração da GIA\-ST e da GNRE foi alterada para possibilitar que o valor dos lançamentos complementares sejam utilizados, a partir de um novo parâmetro definido pelo usuário

CH15922\_2014

Alteração do campo 6\-Inscrição Estadual na UF Favorecida

Este documento tem como objetivo alterar a geração do campo 6\-Inscrição Estadual na UF Favorecida para o estado do Paraná, quando houver Inscrição Estadual Especial\.

CH14637\_2015

Alteração Versão do Cabeçalho da Guia em Papel

Este documento tem como objetivo alterar a versão demonstrada na emissão da guia de ST em papel para o estado do Rio Grande do Sul a partir da apuração ref\. Maio/2015\.

MFS5082

Alteração no layout

Alteração na emissão da GIA\-ST para trabalhar com duas versões de layout \(2 e 3\) 

Ver __RN00__,__ RN35 __e regras específicas da versao3 \(__RN\-Versão3__\)__\.__

## REGRAS DE NEGÓCIO

__Cód\.__

__Descrição__

__DR__

__RN00__

__Regras Gerais__:

__\[ALTERADA – CH14637\_2015\]__

No cabeçalho da emissão da GIA\-ST deverá apresentar o título “GUIA NACIONAL DE INFORMAÇÃO E APURAÇÃO DO ICMS SUBSTITUIÇÃO TRIBUTÁRIA \(GIA \- ST\)” e abaixo a versão do validador de acordo com a regra a seguir:

- Apresentar “Versão 2\.0” para todas as UFs, com exceção a UF igual a “RS” que deve gerar com essa versão até a data de de apuração de “30/04/2015”;
- Apresentar “Versão 3\.0” apenas para UF igual a “RS” com data de apuração a partir de “01/05/2015”\.

__Alteração da MFS5082: __

A versão a ser exibida no cabeçalho será a versão selecionada na tela de emissão \(vide abaixo o parâmetro “__Formato__”\), ou seja, quando opção = versão 2, será impresso “Versão 2\.0”, caso contrário, “Versão 3\.0”\. 

__Alteração da OS3298__:

A emissão da GIA\-ST foi alterada para utilizar o valor dos lançamentos complementares\. Estes lançamentos podem ser  gerados automaticamente na rotina de geração da GIA, ou inseridos manualmente pelo usuário na manutenção\. Para maiores detalhes sobre  o tratamento dos lançamentos na GIA, consultar os documentos de regra específicos de cada etapa da GIA\-ST \(parametrização, geração e manutenção\)\.

No layout da GIA\-ST *não* existem campos para nenhum tipo de ajuste da apuração \(lançamentos\), e por isso, estes valores são totalizados nos campos “oficiais” da GIA\.  Os campos que tiveram o seu preenchimento alterado foram: 13, 17, 18, 20 e 21 \(consultar as regras específicas de cada campo\)\.

__Alteração da MFS5082__: *\(criação do parâmetro “Formato” e separação dos parâmetros “Local e Data”\)*

“__Formato__” – este parâmetro apresenta duas opções:       \[  \] Versão 2   \[  \] Versão 3

Opção default: 3

As opções são alternativas, e dependendo da escolha, serão utilizados diferentes layout’s na emissão da GIA\-ST, da seguinte forma:

     Opção “*Versão 2*” à layout original utilizado na versão 2 do programa da GIA\-ST; 

     Opção “*Versão 3*” à layout da versão 3 do programa GIA\-ST da Sefaz\-RS, onde aparecem os campos referentes à

                                    EC 87/2015\. Para o formato da versão 3, ver regras específicas \(__RN\-Versao3\)__”\. 

__"Local"__ \- neste campo será informado o local para preenchimento do campo “Local e Data”, no formato da versão 2, ou do campo “Local”, no formato da versão 3;

“__Data__” \- neste campo será informada uma data para preenchimento do campo " Local e Data", no formato da versão 2, ou do campo "Data", no formato da versão 3;

__OS3298__

__CH14637\_2015__

__MFS5082__

__RN06__

Campo __6\-Inscrição Estadual na UF Favorecida__:

__Alteração do CH15922\_2014__: Se a “*UF Favorecida”* do estabelecimento for = “PR” então, ao invés de gerar o campo 06 \(Inscrição estadual\) com a inscrição normal do PR \(como já é feito hoje\), deverá ser considerado o campo “Inscrição Estadual Especial” do cadastro de inscrições estaduais do módulo Parâmetro em Preliminares >> Inscrições Estaduais\.

Esta regra apenas deve ser considerada para as operações internas, ou seja, venda para o próprio estado do PARANA, quando o CFOP se inicia com 5\.

No caso de operações interestaduais, continuar considerando o campo de inscrição estadual normal do PR\.

__Atenção: __

Essa regra foi aplicada para geração do arquivo magnético através da OS3401 e deve ser tratada também na emissão, porém nós não iremos aplicar a regra da mensagem de tela avisando sobre a IE como é feito na geração do arquivo magnético, a mensagem para emissão será colocada no manual operacional para que o usuário tome atenção ao dado informado, o motivo de não incluir é por não ser obrigatória a IE Especial\.

__CH15922\_2014__

__RN13__

Campo __13\-ICMS Retido por ST__:

__Alteração da OS3298__: Com a criação dos campos para os lançamentos complementares na GIA\-ST, a geração deste campo passou a considerar o valor dos lançamentos, uma vez que a GIA\-ST *não* tem campos específicos para nenhum tipo de ajuste da apuração\.

O preenchimento deste campo depende do parâmetro “Totalizar os lançamentos de dedução no campo 17\-Pagamentos Antecipados” \(menu “GIA\-ST à Parâmetros por UF Favorecida”\), da seguinte forma:

__Se__ parâmetro “Totalizar os lançamentos de dedução no campo 17\-Pagamentos Antecipados” = N \(ou nulo\)

      Será gravada a totalização dos seguintes campos: \(ICMS\-ST Retido \+ Outros Débitos \+ Estorno de Créditos\) – 

                                                                                       \(Outros Créditos \+ Estorno de Débitos \+ Deduções\);

__Senão __

      Será gravada a totalização dos seguintes campos: \(ICMS\-ST Retido \+ Outros Débitos \+ Estorno de Créditos\) – 

                                                                                        \(Outros Créditos \+ Estorno de Débitos\);

__OS3298__

__RN17__

Campo __17\-Pagamentos Antecipados__:

__Alteração da OS3298__: Com a criação dos campos para os lançamentos complementares na GIA\-ST, a geração deste campo passou a considerar o valor dos lançamentos, uma vez que a GIA\-ST *não* tem campo específicos para nenhum tipo de ajuste da apuração\.

O preenchimento deste campo depende do parâmetro “Totalizar os lançamentos de dedução no campo 17\-Pagamentos Antecipados” \(menu “GIA\-ST à Parâmetros por UF Favorecida”\), da seguinte forma:

__Se__ parâmetro “Totalizar os lançamentos de dedução no campo 17\-Pagamentos Antecipados” = N \(ou nulo\)

      Será gravado o conteúdo do campo “Pagto ICMS\-ST Antecipado”;

__Senão __

      Será gravada a totalização dos seguintes campos: “Pagto ICMS\-ST Antecipado” \+ “Deduções”;

__OS3298__

__RN18__

Campo __18\-ICMS\-ST Devido__:

Este campo será o resultado abaixo, caso positivo:    \(se negativo, gravar zero\)

\(ICMS\-ST Retido \+ Outros Débitos \+ Estorno de Créditos\) – \(Devoluções \+ Ressarcimento \+ Crédito do Per\. Anterior \+ Pagamentos Antecipados \+ Outros Créditos \+ Estorno de Débitos \+ Deduções\)

__OS3298__

__RN20__

Campo __20\-Crédito p/o Período Seguinte__:

Se o resultado abaixo for positivo, gravar o resultado no campo “__20\-Crédito p/o Período Seguinte__”, caso contrário,__ __o resultado deverá ser gravado no campo “__21\-ICMS\-ST a Recolher__”: 

\(Devoluções \+ Ressarcimento \+ Crédito do Per\. Anterior \+ Pagamentos Antecipados \+ Outros Créditos \+ Estorno de Débitos \+ Deduções\) – 

\(ICMS\-ST Retido \+ Outros Débitos \+ Estorno de Créditos \+ Repasse ICMS\-ST Combustível\) 

Obs: Este valor é o resultado do total dos créditos – total dos débitos \(incluindo o débito do repasse de ICMS\-ST de combustível\)\.

__OS3298__

__RN21__

Campo __21\-ICMS\-ST a Recolher__:

\(ver __RN20__\)

__OS3298__

__RN35__

Campo “__35\-Local e Data__”:

Alteração da __MFS5082__: alterado o preenchimento deste campo, devido à separação dos campos Local/Data na tela de emissão:

 

Este campo é preenchido com a concatenação dos campos “Local” e “Data”, informados na tela da emissão do relatório\.

__MFS5082__

__                                          Regras da Emissão do Formato da Versão 3__

__RN__

__Versao3__

__Preenchimento dos campos no formato da versão 3:     __

O layout da versão 3 segue o formato disponível no programa GIA\-ST da Sefaz\-RS \(vide layout anexo\), considerando apenas que o campo “*Inconsistente*” não será gerado, pois depende da importação dos dados para o programa\.

Como demonstra o layout, o relatório é composto de cinco partes distintas:

\- Página Principal

\- Anexo I \- Detalhamento das Devoluções de Vendas de Mercadorias

\- Anexo II \- Detalhamento do ICMS de Ressarcimentos

\- Anexo III \- Informações sobre as Tranferências Efetuadas para a UF Favorecida

\- Anexo EC 87/15 \- Emenda constitucional N° 87/15 

A diferença entre as versões 2 e 3, são as informações referentes à Emenda Constitucional 87/15, que não existem na versão 2\. As informações do relatório são as mesmas utilizadas no formato da versão 2, exceto pela página principal, que tem um layout diferente devido a entrada dos campos da EC 87/15, e também pelo anexo “Anexo EC 87/15”, também referente aos valores da EC 87/15\.  

Informações do Cabeçalho:

__              Guia Nacional de Informação e Apuração do ICMS Substituição Tributária        Data: 99/99/9999__

__                                                         Versão 3\.0                                                                                  Página: 99__

A seguir serão descritas as regras de preenchimento de cada uma das partes separadamente\.

__MFS5082__

__RN__

__Versao3__

__Principal__

__Página Principal:     __

Data: Data da emissão do relatório\.

Página: Sequencial de paginação \(paginar pela GIA *de cada UF favorecida*\)\.

\- __Informações sobre o Estabelecimento e a UF favorecida:__

As informações dos campos a seguir são recuperadas do cadastro do Estabelecimento, do cadastro das inscrições estaduais e também da aba “Principal” da tela de manutenção da GIA\-ST:

  

CGC/TE: Inscrição estadual do estabelecimento __na UF favorecida__\. Esta informação é recuperada do cadastro de inscrições estaduais \(módulo Parâmetros > Preliminares > Inscrições Estaduais\), considerando o estabelecimento em questão e a UF favorecida\. 

OBS: No caso da UF Favorecida = “PR”, será considerada a mesma regra já descrita na RN06 \(versão 2\)\. 

Período: mês e ano do campo “Data de Apuração” da aba “Principal”

Razão Social: razão social do cadastro do estabelecimento

UF favorecida: sigla do estado do campo “UF Favorecida” da aba "Principal"

CNPJ: CNPJ do cadastro do estabelecimento

Endereço: endereço completo do cadastro do estabelecimento \(concatenação do logradouro \+ endereço \+ número \+ complemento \+ bairro\)

UF: sigla do estado do campo “UF” do cadastro do estabelecimento

Telefone: concatenação do DDD \+ telefone do cadastro do estabelecimento

É distribuidora de combustíveis\.\.\.\.\.\.: o preenchimento deste campo depende da informação do campo “Oper\. Repasse de Combustível” da aba “Principal”, da seguinte forma:

   \- Se marcado \- o campo será preenchido com “Sim”

   \- Se desmarcado \- o campo será preenchido com “Não”

GIA\-ST sem movimento: o preenchimento deste campo depende da informação do campo "GIA sem Movimento" da aba "Principal", da seguinte forma:

     \- Se marcado \- o campo será preenchido com "Sim"

     \- Se desmarcado \- o campo será preenchido com "Não"

EC N\.87/15 com movimento: o preenchimento deste campo depende da informação do campo "EC n\.87/15 com movimento” da aba "Principal" \(quadro "Informações EC 87/15"\), da seguinte forma:

     \- Se marcado \- o campo será preenchido com "Sim"

     \- Se desmarcado \- o campo será preenchido com "Não" 

Retificadora: o preenchimento deste campo depende da informação do campo "GIA Substitutiva " da aba "Principal", da seguinte forma:

     \- Se marcado \- o campo será preenchido com "Sim"

     \- Se desmarcado \- o campo será preenchido com "Não"

Efetuou transferências para a UF favorecida: o preenchimento deste campo depende do conteúdo do Anexo III da GIA\-ST, da seguinte forma:

     \- Se na aba “Anexo III – Transferências” existirem dados \- o campo será preenchido com "Sim"

     \- Se na aba “Anexo III – Transferências” não existirem dados \- o campo será preenchido com "Não"

__\- Quadro “Valores”__:

Os valores deste quadro são recuperados da tela de manutenção dos dados da GIA\-ST, aba “Principal” \(menu "Apuração > Guias de Recolhimento > Guia de Informação de Substituição Tributária > Emissão"\)\.

Valor dos Produtos: campo “Vlr\. dos Produtos”\.

Valor do IPI: campo “Vlr\. do IPI”\.

Despesas Acessórias: campo “Despesas Acessórias”\.

Base de Cálculo do ICMS Próprio: campo “Base de Cálculo do ICMS Próprio”\.

ICMS Próprio: campo “ICMS Próprio”\.

Base de Cálculo do ICMS\-ST: campo “Base de Cálculo do ICMS\-ST”

ICMS Retido por Substituição Tributária: Idem __RN13__ \(campo “13\-ICMS Retido por ST”\)\.

ICMS de Devoluções de Mercadorias: campo “ICMS\-ST Devoluções”

ICMS de Ressarcimentos: campo “ICMS\-ST Ressarcimento”

Crédito de Período Anterior: campo “Crédito ICMS\-ST Período Anterior”

Pagamentos Antecipados: idem __RN17__\( campo “17\-Pagamentos Antecipados”\)\.

ICMS\-ST Devido: idem __RN18__ \(campo “18\-ICMS\-ST Devido”\)\.

Repasse ICMS Retido por Refinarias/Complementos: campo “Repasse ICMS\-ST Combustível”

Repasse ICMS Retido por Outros Contribuintes: a princípio este campo ficará zerado, pois ele não é tratado pela nossa geração da GIA\-ST e nem existe na tela de manutenção\.

Crédito para Período Seguinte: idem __RN20__ \(campo “20\-Crédito p/o Período Seguinte”\)\.

Total do ICMS\-ST a Recolher: idem __RN21__ \(campo “21\-ICMS\-ST a Recolher”\)\.

Total do ICMS\-ST FCP a Recolher: campo "Total ICMS FCP"

__\- Quadro “Datas de Vencimento do ICMS\-ST”:__

As informações deste quadro são recuperados da tela de manutenção dos dados da GIA\-ST,  aba "Principal", quadro “Vencimentos” \(menu "Apuração > Guias de Recolhimento > Guia de Informação de Substituição Tributária > Emissão"\)\.

Data: campo “Data”\.

ICMS\-ST: campo “Valor do ICMS\-ST”\.

ICMS\-ST FCP: campo "Valor do ICMS\- ST FCP"

__\- Quadro “Emenda Constitucional N\. 87/15” e "Fundo de Combate a Pobreza" \(FCP\):__

As informações deste quadro são recuperados da tela de manutenção dos dados da GIA\-ST,  aba "Principal", quadro "Informações EC 87/15" \(menu "Apuração > Guias de Recolhimento > Guia de Informação de Substituição Tributária > Emissão"\)\.

Valor do ICMS Devido à UF de Destino: campo “Valor do ICMS Devido à UF de Destino”\.

Devoluções ou Anulações: campo “Devoluções ou Anulações”\.

Pagamentos Antecipados: campo “Pagamentos Antecipados”\.

Total do ICMS Devido à UF de Destino: campo “Total ICMS Devido à UF de Destino”\.

Total ICMS FCP: campo “Total ICMS FCP”\.

__\- Quadro “Declaração”:__

As informações deste quadro são recuperadas dos dados cadastrais do responsável, local, e data, informados na tela da emissão do relatório\.

Declarante: nome do responsável/declarante informado\.

CPF: CPF do responsável/declarante informado\.

Cargo: cargo do responsável/declarante informado\.

Telefone: concatenação de DDD \+ Telefone do responsável/declarante informado\.

E\-mail: e\-mail do responsável/declarante informado\.

Fax: fax do responsável/declarante informado

Local: conteúdo do campo “Local” informado na tela da emissão\. 

Data: conteúdo do campo "Data" informado na tela da emissão\.

__\- Quadro “Observações”:__

Este quadro é preenchido com o conteúdo do campo “Observação” da tela de manutenção dos dados da GIAST, aba "Principal"\. 

__MFS5082__

__RN__

__Versao3__

__Anexo I__

__Anexo I \- Detalhamento das Devoluções de Vendas de Mercadorias:__

As informações deste quadro são recuperadas da aba “Anexo I – Devolução” da tela de manutenção da GIA\-ST\.

Podem existir vários documentos fiscais informados para este anexo, e para cada um será impressa uma linha, de acordo com o layout\. A página referente a este anexo será impressa apenas quando existirem dados\.

 

Nota Fiscal: campo “Documento Fiscal n\.”\.

Série: campo "Série"\.

Inscrição Estadual: campo “Insc\. Estadual Fis/Jur” \(é a inscrição estadual da pessoa fis/jur informada\)\.

Data de Emissão: campo "Data Emissão"

Valor ICMS\-ST de Devolução: campo “Vlr\. ICMS\-ST Devolução”\.

__MFS5082__

__RN__

__Versao3__

__Anexo II__

__Anexo II \- Detalhamento do ICMS de Ressarcimentos:__

As informações deste quadro são recuperadas da aba “Anexo II – Ressarcimento” da tela de manutenção da GIA\-ST\. A página referente a este anexo será impressa apenas quando existirem dados\.

Nota Fiscal: campo "Documento Fiscal n"

Série: campo "Série"

Inscrição Estadual: campo "Insc Estadual Fis/Jur" é a inscrição estadual da pessoa fis/jur informada

Data de Emissão: campo "Data Emissão"

Valor ICMS\-ST de Ressarcimento: campo "Vlr ICMS\-ST Ressarcimento"

__MFS5082__

__RN__

__Versao3__

__Anexo III__

__Anexo III \- Informações sobre as Tranferências Efetuadas para a UF Favorecida:__

As informações deste quadro são recuperadas da aba “Anexo III – Transferência” da tela de manutenção da GIA\-ST\. A página referente a este anexo será impressa apenas quando existirem dados\.

Inscrição Estadual: campo "Insc Estadual Fis/Jur" é a inscrição estadual da pessoa fis/jur informada\.

Valor Base de Cálculo: campo "Base Cáculo ICMS"\.

Valor ICMS Destacado: campo "Vlr\. ICMS Destacado"\.

__MFS5082__

__RN__

__Versao3__

__Anexo EC 87/15__

__Anexo EC 87/15 – Emenda Constitucional N\. 87/15:__

As informações deste quadro são recuperadas da aba “Anexo IV – EC 87/15” da tela de manutenção da GIA\-ST\. A página referente a este anexo será impressa apenas quando existirem dados\.

Data Venc\. ICMS Devido: campo “Data de Vencto do ICMS Devido à UF de Destino”\.

Valor do ICMS: campo “Valor do ICMS Devido”\.  

Data Vencimento FCP: campo “Data de Vencimento FCP”\.

Valor do ICMS FCP: campo “Valor do ICMS FCP”\.

__MFS5082__

