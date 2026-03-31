# MTZ-PIM-Relatorio_Detalhamento_Subapuracoes

- **Fonte:** MTZ-PIM-Relatorio_Detalhamento_Subapuracoes.docx
- **Modificado:** 2021-06-21
- **Tamanho:** 90 KB

---

THOMSON REUTERS

__                            Módulo PIM – Relatório de Detalhamento das Subapurações__

__  __

__Localização__: Menu Específicos, Módulo PIM, item Apuração 🡪 Subapurações do Sped Fiscal 🡪 Relatórios 🡪 Detalhamento das Subapurações

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS4593\-C

Relatório de Detalhamento das Subapurações

Criação de relatório para demonstrar o detalhamento da operações referentes às subapurações

19/09/2014

\(criação do docto\)

	

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

Este relatório foi criado na OS4593\-C com o objetivo de detalhar as operações que compõem cada subapuração\.

Na prática, o relatório demonstra as notas fiscais, lançamentos, e débitos especiais associados a cada uma das subapurações utilizadas\.

É um detalhamento de cada uma das linhas de total da subapuração que aparece na listagem dos totais apurados \(item de menu “Relatórios 🡪 Listagem dos Totais Apurados”\)\.

As diferenças entre esses dois relatórios é a seguinte:

     \- A listagem dos totais apurados utiliza os valores calculados pela rotina da apuração dos resultados das subapurações\. Assim, para

       sua emissão, é pré\-requisito que a apuração dos resultados já tenha sido executada;

     \- A listagem dos totais mostra apenas os totais gerais, que serão gravados no registro 1920 do Sped Fiscal;

     \- O relatório do detalhamento das subapurações mostra as operações que compõem cada subapuração, notas e lançamentos, para

       permitir uma conferência\. Ele pode ser emitido mesmo antes de executar a apuração, assim, neste caso *não* existe o pré\-requisito

       do outro relatório;

  

__RN01__

__                                                      Parâmetros da Tela __

__Parâmetros da Geração:__

__Subapuração__ – Este campo é uma lista das subapurações do Sped Fiscal \+ opção “Todas”

Todas

 Subapuração 1

 Subapuração 2

 Subapuração 3

 Subapuração 4

 Subapuração 5

 Subapuração 6

 Não Incentivado

Default   🡪 opção “Todas”  

__Período __– Neste campo serão informadas as datas inicial e final para emissão do relatório\.

As datas serão utilizadas para filtro das notas fiscais nas opções “Débitos de Notas Fiscais” e “Créditos de Notas Fiscais” do campo 

“Dados para Conferência”, e na opção “Lançamentos Complementares e Débitos Especiais” será utilizada apenas a data final\.

__Dados para Conferência __– Este campo apresenta as seguintes opções para seleção do usuário:

                                                        \[   \] Débitos de Notas Fiscais

                                                        \[   \] Créditos de Notas Fiscais 

                                                        \[   \] Lançamentos Complementares

                                                        \[   \] Débitos Especiais

O usuário poderá selecionar as opções desejadas, devendo escolher ao menos uma delas obrigatoriamente\.

 

__Estabelecimentos/Inscrições Estaduais__ – Este quadro exibe a lista dos estabelecimentos / inscrições estaduais que atendam aos seguintes critérios: 

     \- Somente os estabelecimentos da Empresa do login;

     \- Somente os estabelecimentos e inscrições estaduais parametrizados no Módulo PIM \(menu “Cadastros 🡪 Inscrição Estadual por

       Estabelecimento”\);

__RN02__

__                                                   Recuperação dos Dados__

__Recuperação dos Dados:__

Os dados deste relatório são tratados separadamente, de acordo com as opções escolhidas no campo “*Dados para Conferência*”, da seguinte forma:

\(ver layout na planilha anexa “Layout\_do\_Detalhamento\_das\_Subapurações”\)

Débitos de Notas Fiscais

São as notas fiscais de saída com informações de ajustes na SAFX113 referentes às subapurações\. 

Corresponde às notas fiscais que compõe o total do campo “Débitos de Notas Fiscais”, apurado na rotina “Apuração dos Resultados” e demonstrado no relatório “Listagem dos Totais Apurados”, que pode ser emitido após executar a apuração\.

Créditos de Notas Fiscais

São as notas fiscais de entradas com informações de ajustes na SAFX113 referentes às subapurações\.

 Corresponde às notas fiscais que compõe o total do campo “Créditos de Notas Fiscais”, apurado na rotina “Apuração dos Resultados”e demonstrado no relatório “Listagem dos Totais Apurados”, que pode ser emitido após executar a apuração\.

Lançamentos Complementares 

Detalhamento dos lançamentos complementares associados às subapurações através do campo “*Subapuração do Sped Fiscal*” das telas de manutenção dos lançamentos complementares da Apuração do ICMS\. 

Corresponde aos lançamentos que compõem o total dos campos abaixo, apurados na rotina “Apuração dos Resultados” e demonstrados no relatório “Listagem dos Totais Apurados”, que pode ser emitido após executar a apuração:

\-Outros Débitos

\-Estorno de Créditos

\-Outros Créditos

\-Estorno de Débitos

\-Deduções

Débitos Especiais

Detalhamento dos débitos especiais associados às subapurações através do campo “*Subapuração do Sped Fiscal*” das telas de manutenção dos lançamentos complementares da Apuração do ICMS, e também, os débitos especiais carregados via SAFX113, e associados às subapurações através do código do ajuste\. 

Corresponde aos valores que compõem o total do campo “Débitos Especiais”, apurados na rotina “Apuração dos Resultados” e demonstrados no relatório “Listagem dos Totais Apurados”, que pode ser emitido após executar a apuração\.

__Geração do Relatório:__

__O relatório será gerado por Estabelecimento /Inscrição Estadual e Subapuração\. __

__Assim, para cada Estabelecimento/Inscrição Estadual selecionada em tela, o relatório mostrará as informações de cada subapuração selecionada em tela, separadamente, e de acordo com os dados escolhidos no campo “Dados para Conferência”\.__

Os estabelecimentos/inscrições estaduais serão ordenados pelo código do estabelecimento, e para cada estabelecimento, as inscrições serão ordenadas pelo número\. 

Para cada estabelecimento / inscrição estadual, as subapurações serão apresentadas em ordem \(01, 02, 03, 04, 05, 06\)\.

Na linha do cabeçalho referente a cada subapuração *\(linha que aparece em azul na planilha do layout\)*, será demonstrado o código e a descrição da subapuração\. A descrição será recuperada da tela de cadastro das subapurações no Modulo PIM \(menu Apuração 🡪 Subapurações do Sped Fiscal  🡪 Subapurações por Inscrição Estadual\)\.

__Obs__: O campo “Inscrição Estadual” do cabeçalho apresenta a inscrição estadual em processamento \(inscrição estadual selecionada em tela\)\. 

__A emissão do relatório será feita da seguinte forma:__

Este relatório trabalha com dados de diferentes origens, portanto, os layout’s são diferentes\. Por isso, o relatório será gerado em partes distintas, semelhante ao funcionamento dos livros fiscais  \(Módulo ICMS\), e vários outros relatórios existentes no Mastersaf\.

Após a geração, cada Estabelecimento / Inscrição Estadual / Subapuração gerado será mostrada uma linha na tela\.

   \- Para visualizar cada relatório o usuário deverá clicar sobre a linha correspondente\.

   \- Será mostrada em tela a primeira parte do relatório;

   \- Na barra de menu terá a opção “*Selecionar Item de Relatório*”;

   \- Para visualizar as demais partes, o usuário deverá clicar na opção “*Selecionar Item de Relatório*” e selecionar a opção desejada;

   \- Para impressão do relatório, também existirão as opções padrão na barra de menu, e ao solicitar a impressão, sempre serão

      impressas todas as partes do relatório;

As *diferentes partes do relatório* são exatamente as abas descritas na planilha anexa “Layout\_do\_Detalhamento\_das\_Subapuracoes”\.

Na prática, serão as diferentes opções escolhidas em tela, com as seguintes diferenças:

     \- A opção “Débitos Especiais” __originará duas partes distintas__, uma para cada origem de débito especial;

     \- Existirá também a parte “Total”;

Na opção “*Selecionar Item de Relatório*” da barra de menu, as descrições das diferentes partes do relatório serão as seguintes:

Débitos de Notas Fiscais

Créditos de Notas Fiscais

Lançamentos Complementares

Débitos Especiais \- Lançamentos

Débitos Especiais – SAFX113

Totais

__Recuperação dos Dados__

As regras referentes a cada conjunto de dados estão definidas a seguir, da seguinte forma:

__     \- RN03 – Débitos de Notas Fiscais__

__     \- RN04 – Créditos de Notas Fiscais__

__     \- RN05 – Lançamentos Complementares__

__     \- RN06 – Débitos Especiais \(originados dos lançamentos complementares\) __

__     \- RN07 – Débitos Especiais \(originados da SAFX113\)__

__     \- RN08 – Totais__

__RN03__

__                                                  Débitos de Notas Fiscais__

__Débitos de Notas Fiscais__

Os dados a serem demonstrados sob este título são informações das notas fiscais de saída com ajustes na SAFX113 referentes a subapuração em processamento\.

Importante: Na prática, os critérios para a recuperação destas notas são os mesmos critérios utilizados para apuração do valor total do campo “Débitos de Notas Fiscais” da Tabela das Subapurações gerada no item de menu “Apuração 🡪 Subapurações do Sped Fiscal 🡪 Apuração dos Resultados”:

__Origem dos dados__ 🡪 SAFX07, SAFX08 e SAFX113

A SAFX08 será utilizada apenas quando o item de referência do ajuste estiver preenchido na SAFX113 \(campo 15\), caso contrário, as seguintes colunas do relatório ficarão em branco: “Item de Referência”, “CFOP”, “Tipo Produto” e “Produto”\.

 

\- Notas fiscais de saída

\- Somente as notas não canceladas

\- Data fiscal referente ao período informado em tela

\- Se nota extemporânea, a data extemporânea que deve ser referente ao período informado em tela

\- Inscrição estadual \(campo 126\) da nota = inscrição estadual em processamento

\- Modelo \(campo 13\) = 01, 1A, 1B, 04, 55, 65, 07, 08, 8B, 09, 10, 11, 26, 27 ou 57 

*  \(são os modelos tratados nos registros C100 e D100 do Sped Fiscal, pois apenas estas notas geram os registros C197 ou D197\)*

*  \(lembrando que estes registros C197 e D197 são a origem do tratamento das subapurações\) *

\- Classificação \(campo 12\) = 1 ou 3 \(mercadoria ou mista\)  

\- Somente notas com registros na SAFX113 cujo código de ajuste tenha as seguintes características:

  🡪o terceiro caracter = __2__ \(indicando um __estorno de débito__\)

     🡪o quarto caracter deve ser referente a subapuração em processamento, da seguinte forma:

           Se subapuração em processamento = 1 🡪 considerar o conteúdo “3”

           Se subapuração em processamento = 2 🡪 considerar o conteúdo “4”

           Se subapuração em processamento = 3 🡪 considerar o conteúdo “5”

           Se subapuração em processamento = 4 🡪 considerar o conteúdo “6”

           Se subapuração em processamento = 5 🡪 considerar o conteúdo “7”

           Se subapuração em processamento = 6 🡪 considerar o conteúdo “8”

Cada linha da SAFX113 recuperada de acordo com estes critérios será demonstrada no relatório, conforme o layout anexo\.

\(layout na planilha anexa “Layout\_do\_Detalhamento\_das\_Subapuracoes”, aba “*Débitos de NFs*”\)

__Preenchimentos dos dados no relatório__:

Ordenação das linhas: Data fiscal, número da nota fiscal, série da nota fiscal\.

Dt\. Fiscal

Data fiscal da nota \(campo 03 da SAFX113\)

Nota Fiscal

Número e série da nota fiscal \(campos 09 e 10 da SAFX113\)

Dt\. Emissão

Data de emissão da nota \(campo 11 da SAFX07\)

Cód\. Ajuste

Código de ajuste \(campo 13 da SAFX113\)

Base ICMS

Base de cálculo do ajuste \(campo 16 da SAFX113\)

Alíquota ICMS

Alíquota do ajuste \(campo 17 da SAFX113\)

Valor Ajuste ICMS

Valor do Ajuste \(campo 18 da SAFX113\)

Item de Referência

Número do item de referência do ajuste \(campo 15 da SAFX113\)

\(quando não preenchido, a coluna ficará em branco\)

CFOP

Esta coluna será preenchida apenas quando o item de referência estiver preenchido na SAFX113\. Neste caso, será informado o CFOP indicado no item da nota \(campo 22 da SAFX08\)\.

\(quando o item de referência não estiver preenchido na SAFX113, a coluna ficará em branco\)

Tipo Produto

Esta coluna será preenchida apenas quando o item de referência estiver preenchido na SAFX113\.

Neste caso, será informado o tipo do produto indicado no item da nota\. Trata\-se do campo “15\-Tipo do Produto” do cadastro do produto \(SAFX2013\)\.

\(quando o item de referência não estiver preenchido na SAFX113, a coluna ficará em branco\)

Produto

Esta coluna será preenchida apenas quando o item de referência estiver preenchido na SAFX113\. Neste caso, será informada a identificação do produto indicado no item da nota \(campos 13 e 14 da SAFX08\)\.

Será demonstrada a concatenação das informações do indicador, código e descrição do produto \(descrição do cadastro do produto na SAFX2013\), como aparece no layout\. 

Se necessário, a descrição poderá ser truncada, se houver limitação do número de colunas a serem exibidas\.

 \(quando o item de referência não estiver preenchido na SAFX113, a coluna ficará em branco\)

Ao final, a coluna “Valor Ajuste ICMS” será totalizada na linha “Total do débito das notas fiscais de saída”\.

__RN04__

__                                                  Créditos de Notas Fiscais__

__Créditos de Notas Fiscais__

Os dados a serem demonstrados sob este título são informações das notas fiscais de entrada com ajustes na SAFX113 referentes a subapuração em processamento\.

Importante: Na prática, os critérios para a recuperação destas notas são os mesmos critérios utilizados para apuração do valor total do campo “Créditos de Notas Fiscais” da Tabela das Subapurações gerada no item de menu “Apuração 🡪 Subapurações do Sped Fiscal 🡪 Apuração dos Resultados”:

__Origem dos dados__ 🡪 SAFX07, SAFX08 e SAFX113

A SAFX08 será utilizada apenas quando o item de referência do ajuste estiver preenchido na SAFX113 \(campo 15\), caso contrário, as seguintes colunas do relatório ficarão em branco: “Item de Referência”, “CFOP”, “Tipo Produto” e “Produto”\.

\- Notas fiscais de entrada

\- Somente as notas não canceladas

\- Data fiscal referente ao período informado em tela

\- Se nota extemporânea, a data extemporânea que deve ser referente ao período informado em tela

\- Inscrição estadual \(campo 126\) da nota = inscrição estadual em processamento

\- Modelo \(campo 13\) = 01, 1A, 1B, 04, 55, 65, 07, 08, 8B, 09, 10, 11, 26, 27 ou 57 

*  \(são os modelos tratados nos registros C100 e D100 do Sped Fiscal, pois apenas estas notas geram os registros C197 ou D197\)*

*  \(lembrando que estes registros C197 e D197 são a origem do tratamento das subapurações\) *

\- Classificação \(campo 12\) = 1 ou 3 \(mercadoria ou mista\)  

\- Somente notas com registros na SAFX113 cujo código de ajuste tenha as seguintes características:

  🡪o terceiro caracter = __5__ \(indicando um __estorno de crédito__\)

     🡪o quarto caracter deve ser referente a subapuração em processamento, da seguinte forma:

           Se subapuração em processamento = 1 🡪 considerar o conteúdo “3”

           Se subapuração em processamento = 2 🡪 considerar o conteúdo “4”

           Se subapuração em processamento = 3 🡪 considerar o conteúdo “5”

           Se subapuração em processamento = 4 🡪 considerar o conteúdo “6”

           Se subapuração em processamento = 5 🡪 considerar o conteúdo “7”

           Se subapuração em processamento = 6 🡪 considerar o conteúdo “8”

Cada linha da SAFX113 recuperada de acordo com estes critérios será demonstrada no relatório, conforme o layout anexo\.

\(layout na planilha anexa “Layout\_do\_Detalhamento\_das\_Subapuracoes”, aba “*Créditos de NFs*”\)

__Preenchimentos dos dados no relatório:__

Ordenação das linhas: Data fiscal, número da nota fiscal, série da nota fiscal\.

Dt\. Fiscal

Data fiscal da nota \(campo 03 da SAFX113\)

Nota Fiscal

Número e série da nota fiscal \(campos 09 e 10 da SAFX113\)

Dt\. Emissão

Data de emissão da nota \(campo 11 da SAFX07\)

Cód\. Ajuste

Código de ajuste \(campo 13 da SAFX113\)

Base ICMS

Base de cálculo do ajuste \(campo 16 da SAFX113\)

Alíquota ICMS

Alíquota do ajuste \(campo 17 da SAFX113\)

Valor Ajuste ICMS

Valor do Ajuste \(campo 18 da SAFX113\)

Item de Referência

Número do item de referência do ajuste \(campo 15 da SAFX113\)

\(quando não preenchido, a coluna ficará em branco\)

CFOP

Esta coluna será preenchida apenas quando o item de referência estiver preenchido na SAFX113\. Neste caso, será informado o CFOP indicado no item da nota \(campo 22 da SAFX08\)\.

\(quando o item de referência não estiver preenchido na SAFX113, a coluna ficará em branco\)

Tipo Produto

Esta coluna será preenchida apenas quando o item de referência estiver preenchido na SAFX113\.

Neste caso, será informado o tipo do produto indicado no item da nota\. Trata\-se do campo “15\-Tipo do Produto” do cadastro do produto \(SAFX2013\)\.

\(quando o item de referência não estiver preenchido na SAFX113, a coluna ficará em branco\)

Produto

Esta coluna será preenchida apenas quando o item de referência estiver preenchido na SAFX113\. Neste caso, será informada a identificação do produto indicado no item da nota \(campos 13 e 14 da SAFX08\)\.

Será demonstrada a concatenação das informações do indicador, código e descrição do produto \(descrição do cadastro do produto na SAFX2013\), como aparece no layout\. 

Se necessário, a descrição poderá ser truncada, se houver limitação do número de colunas a serem exibidas\.

 \(quando o item de referência não estiver preenchido na SAFX113, a coluna ficará em branco\)

Ao final, a coluna “Valor Ajuste ICMS” será totalizada na linha “Total do crédito das notas fiscais de entrada”\.

__RN05__

__                                        Lançamentos Complementares __

As informações dos lançamentos complementares serão demonstradas de acordo com o tipo do lançamento, da seguinte forma:

\- Outros Débitos

\- Estorno de Créditos

\- Outros Créditos

\- Estorno de Débitos

\- Deduções

\(ver layout na planilha “Layout\_do\_Detalhamento\_das\_Subapuracoes”, aba “*Lançamentos”*\)

__Origem dos dados: __Tabela dos Lançamentos Complementares da Apuração do ICMS

\(módulo PIM, item Apuração 🡪 Apuração dos Saldos de Impostos e Taxas 🡪 Lançamentos Complementares 🡪 Apuração do ICMS\)

Segue regras da geração de cada um dos tipos de lançamento:

Importante: Os critérios para a recuperação dos dados são os mesmos critérios utilizados para apuração do valor total de cada um destes campos da Tabela das Subapurações, gerada no item de menu “Apuração 🡪 Subapurações do Sped Fiscal 🡪 Apuração dos Resultados”:

__Outros Débitos:__

Sob este título serão demonstrados todos os lançamentos complementares da Apuração do ICMS do Estabelecimento / Inscrição Estadual em processamento, que atendam aos seguintes critérios:

- Lançamentos referentes à apuração do ICMS do período solicitado para a geração \(Data Apuração = Data final informada\);

 

- Lançamentos com o campo “*Operação Apuração*” = __002__ \(Outros Débitos\);
- Lançamentos com o campo “*Tipo de Lançamento*” = 2 ou 3 \(“Lançamento associado a outros documentos fiscais” ou “Outros Lançamentos”\);  
- Lançamentos com o campo “*Subapuração do Sped Fiscal*” = Subapuração em processamento;

__Estorno de Créditos:__

Sob este título serão demonstrados todos os lançamentos complementares da Apuração do ICMS do Estabelecimento / Inscrição Estadual em processamento, que atendam aos seguintes critérios:

- Lançamentos referentes à apuração do ICMS do período solicitado para a geração \(Data Apuração = Data final informada\);

 

- Lançamentos com o campo “*Operação Apuração*” = __003__ \(Estorno de Crédito\);
- Lançamentos com o campo “*Tipo de Lançamento*” = 2 ou 3 \(“Lançamento associado a outros documentos fiscais” ou “Outros Lançamentos”\);  
- Lançamentos com o campo “*Subapuração do Sped Fiscal*” = Subapuração em processamento;

__Outros Créditos:__

Sob este título serão demonstrados todos os lançamentos complementares da Apuração do ICMS do Estabelecimento / Inscrição Estadual em processamento, que atendam aos seguintes critérios:

- Lançamentos referentes à apuração do ICMS do período solicitado para a geração \(Data Apuração = Data final informada\);

 

- Lançamentos com o campo “*Operação Apuração*” = __006__ \(Outros Créditos\);
- Lançamentos com o campo “*Tipo de Lançamento*” = 2 ou 3 \(“Lançamento associado a outros documentos fiscais” ou “Outros Lançamentos”\);  
- Lançamentos com o campo “*Subapuração do Sped Fiscal*” = Subapuração em processamento;

__Estorno de Débitos:__

Sob este título serão demonstrados todos os lançamentos complementares da Apuração do ICMS do Estabelecimento / Inscrição Estadual em processamento, que atendam aos seguintes critérios:

- Lançamentos referentes à apuração do ICMS do período solicitado para a geração \(Data Apuração = Data final informada\);

 

- Lançamentos com o campo “*Operação Apuração*” = __007__ \(Estorno de Débitos\);
- Lançamentos com o campo “*Tipo de Lançamento*” = 2 ou 3 \(“Lançamento associado a outros documentos fiscais” ou “Outros Lançamentos”\);  
- Lançamentos com o campo “*Subapuração do Sped Fiscal*” = Subapuração em processamento;

__Deduções:__

Sob este título serão demonstrados todos os lançamentos complementares da Apuração do ICMS do Estabelecimento / Inscrição Estadual em processamento, que atendam aos seguintes critérios:

- Lançamentos referentes à apuração do ICMS do período solicitado para a geração \(Data Apuração = Data final informada\);

 

- Lançamentos com o campo “*Operação Apuração*” = __012__ \(Deduções\);
- Lançamentos com o campo “*Tipo de Lançamento*” = 2 ou 3 \(“Lançamento associado a outros documentos fiscais” ou “Outros Lançamentos”\);  
- Lançamentos com o campo “*Subapuração do Sped Fiscal*” = Subapuração em processamento;

__Preenchimentos dos dados no relatório:__

Lançamento

Descrição do Lançamento \(campo “Descrição”\)

N\. Discrim\.

Sequencial do lançamento \(campo “N\. Discriminação”\)

Classe

Código da classe do lançamento \(campo “Classe Lançamento”\)

Cód\. Ajuste

Código de ajuste do lançamento \(campo “Código de Ajuste \(Sped Fiscal – Reg E111/E220\)”\)

Valor

Valor do lançamento \(campo “Valor”\)

Ao final de cada item, a coluna “Valor” será totalizada nas linhas de total respectivas, conforme layout anexo\.

 \(planilha “Layout\_do\_Detalhamento\_das\_Subapuracoes”, aba “*Lançamentos”*\)

__RN06__

__                              Débitos Especiais \(originados dos lançamentos complementares\)__

__Débitos Especiais \(originados dos lançamentos complementares\):__

Sob este título serão demonstrados os débitos especiais cadastrados para a apuração do período na manutenção dos lançamentos complementares de ICMS \(aba “Débitos Especiais”\)\.

\(ver layout na planilha “Layout\_do\_Detalhamento\_das\_Subapuracoes”, aba “Débitos Especiais – Lançamentos”\)

__Origem dos dados: __ Tabela dos Débitos Especiais da Apuração do ICMS – PIM

\(Módulo PIM, item Apuração 🡪 Apuração dos Saldos de Impostos e Taxas 🡪 Lançamentos Complementares 🡪 Apuração do ICMS\)

\(aba “Débitos Especiais”\)

Importante: Os critérios para a recuperação dos dados são os mesmos critérios utilizados para apuração do valor total do campo “Débitos Especiais” da Tabela das Subapurações, gerada no item de menu “Apuração 🡪 Subapurações do Sped Fiscal 🡪 Apuração dos Resultados”:

Os dados a serem demonstrados são todos os débitos especiais da Apuração do ICMS do Estabelecimento / Inscrição Estadual em processamento, que atendam aos seguintes critérios:

- Débitos especiais referentes à apuração do ICMS do período solicitado para a geração \(Data Apuração = Data final informada\);

 

- Débitos especiais com o campo “*Subapuração do Sped Fiscal*” = Subapuração em processamento;

Preenchimentos dos dados no relatório:

Descrição

Descrição do débito \(campo “Descrição”\)

Cód\. Ajuste

Código de ajuste do débito \(campo “Código de Ajuste”\)

Valor

Valor do débito \(campo “Valor do Débito”\)

Ao final, a coluna “Valor” será totalizada na linha “Total”\.

__RN07__

__                                     Débitos Especiais \(originados da SAFX113\)__

__Débitos Especiais \(originados da SAFX113\):__

Sob este título serão demonstrados os débitos especiais originados dos débitos especiais declarados nos ajustes das notas fiscais \(SAFX113\)\.

\(ver layout na planilha “Layout\_do\_Detalhamento\_das\_Subapuracoes”, aba “Débitos Especiais – SAFX113”\)

OBS: Atualmente \(Set/2014\) a tabela dos códigos de ajustes provenientes de documentos fiscais \(SAFX113\) divulgada pela Sefaz\-AM na Resolução 16/2014, não tem nenhum código referente à débito especial a ser utilizado nos registros C197/D197 p/as subapurações\. No entanto, como o Guia Prático prevê esta situação \(conforme as orientações de preenchimento do campo 13\-DEB\_ESP\_OA do registro 1920\), o cálculo das subapurações já trata esta situação, caso a Sefaz\-AM altere a tabela incluindo novos códigos\.

Isso significa que de acordo c/a Resolução 16/2014 não há como gerar um débito especial para uma subapuração na SAFX113 \(C197/D197\), pois não existe código de ajuste com o terceiro caracter = “7” e o quarto caracter = 3, 4, 5, 6, 7 ou 8\)\.

__Origem dos dados: __ Tabela dos Documentos Fiscais \(SAFX07/SAFX08/SAFX113\)

Importante: Os critérios para a recuperação dos dados são os mesmos critérios utilizados para apuração do valor total do campo “Débitos Especiais” da Tabela das Subapurações, gerada no item de menu “Apuração 🡪 Subapurações do Sped Fiscal 🡪 Apuração dos Resultados”:

Os dados a serem demonstrados são informações das notas fiscais de entrada *ou* saída com ajustes na SAFX113 referentes a subapuração em processamento\.

Os critérios para a recuperação das notas são exatamente os mesmos citados nas regras RN03 e RN04, exceto quanto ao tipo de movimento \(neste caso são consideradas entradas como saídas\), e também as características do código de ajuste, que deverão ser as seguintes:

                     🡪 o terceiro caracter do código deve ser = __7__ \(*débitos especiais*\)

                     🡪 o quarto caracter deve ser referente a subapuração em processamento, da seguinte forma: 

                           Se subapuração em processamento = 1 🡪 considerar o conteúdo “3”

                           Se subapuração em processamento = 2 🡪 considerar o conteúdo “4”

                           Se subapuração em processamento = 3 🡪 considerar o conteúdo “5”

                           Se subapuração em processamento = 4 🡪 considerar o conteúdo “6”

                           Se subapuração em processamento = 5 🡪 considerar o conteúdo “7”

                           Se subapuração em processamento = 6 🡪 considerar o conteúdo “8”

Preenchimentos dos dados no relatório:

Dt\. Fiscal

Data fiscal da nota \(campo 03 da SAFX113\)

Nota Fiscal

Número e série da nota fiscal \(campos 09 e 10 da SAFX113\)

Dt\. Emissão

Data de emissão da nota \(campo 11 da SAFX07\)

Cód\. Ajuste

Código de ajuste \(campo 13 da SAFX113\)

Base ICMS

Base de cálculo do ajuste \(campo 16 da SAFX113\)

Alíquota ICMS

Alíquota do ajuste \(campo 17 da SAFX113\)

Valor Ajuste ICMS

Valor do ICMS \(campo 18 da SAFX113\)

Item de Referência

Número do item de referência do ajuste \(campo 15 da SAFX113\)

\(quando não preenchido, a coluna ficará em branco\)

CFOP

Esta coluna será preenchida apenas quando o item de referência estiver preenchido na SAFX113\. Neste caso, será informado o CFOP indicado no item da nota \(campo 22 da SAFX08\)\.

\(quando o item de referência não estiver preenchido na SAFX113, a coluna ficará em branco\)

Tipo Produto

Esta coluna será preenchida apenas quando o item de referência estiver preenchido na SAFX113\.

Neste caso, será informado o tipo do produto indicado no item da nota\. Trata\-se do campo “15\-Tipo do Produto” do cadastro do produto \(SAFX2013\)\.

\(quando o item de referência não estiver preenchido na SAFX113, a coluna ficará em branco\)

Produto

Esta coluna será preenchida apenas quando o item de referência estiver preenchido na SAFX113\. Neste caso, será informada a identificação do produto indicado no item da nota \(campos 13 e 14 da SAFX08\)\.

Será demonstrada a concatenação das informações do indicador, código e descrição do produto \(descrição do cadastro do produto na SAFX2013\), como aparece no layout\. 

Se necessário, a descrição poderá ser truncada, se houver limitação do número de colunas a serem exibidas\.

 \(quando o item de referência não estiver preenchido na SAFX113, a coluna ficará em branco\)

Ao final, a coluna “Valor Ajuste ICMS” será totalizada na linha “Total”\.

__RN08__

__                                                                Totais__

Ao final do relatório, serão demonstrados os totais gerais, de acordo com os dados demonstrados no relatório:

\(ver layout na planilha “Layout\_do\_Detalhamento\_das\_Subapuracoes”, aba “Totais”\)

__Linha__

__Conteúdo__

Total dos Débitos \(NF’s\)

Valor lançado na linha “Total do débito das notas fiscais de saída” \(conforme __RN03__\)

Total dos Débitos \(Lançamentos Complementares\)

Total dos lançamentos complementares a débito:

 Será o total das linhas “Total Outros Débitos” \+ “Total Estorno de Créditos” \(conforme __RN05__\)\.

Total dos Créditos \(NF’s\)

Valor lançado na linha “Total do crédito das notas fiscais de entrada” \(conforme __RN04__\)

Total dos Créditos \(Lançamentos Complementares\)

Total dos lançamentos complementares a crédito:

 Será o total das linhas “Total Outros Créditos” \+ “Total Estorno de Débitos” \(conforme __RN05__\)\.

Saldo:

Nesta linha será demonstrado o resultado final, que poderá ser devedor ou credor, da seguinte forma:

Saldo =

\( Total dos Débitos \(NF’s\) \+ Total dos Débitos \(Lançamentos Complementares\) \)

__\-__

\( Total dos Créditos \(NF’s\) \+ Total dos Créditos \(Lançamentos Complementares\) \)

Independente do resultado obtido o valor será demonstrado *sem* sinal, e ao lado, o indicador de débito ou crédito, da seguinte forma:

Se saldo > 0 🡪 ao lado do valor será mostrado “\(DB\)”, como aparece no layout 

Se saldo < 0 🡪 ao lado do valor será mostrado “\(CR\)”, como aparece no layout

Se saldo = 0 🡪 mostrar apenas o valor zero, *sem* o indicador de “DB” ou “CR”

 

Débitos Especiais \(Lançamentos Complementares\):

Valor total dos débitos especiais originados dos lançamentos complementares \(conforme __RN06__\)\.

Débitos Especiais \(SAFX113\):

Valor total dos débitos especiais originados da SAFX113 \(conforme __RN07__\)\. 

= = = = = 

