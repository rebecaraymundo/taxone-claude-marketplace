# MTZ_Prodepe_Relat_Conferencia_NFs_Entrada

- **Fonte:** MTZ_Prodepe_Relat_Conferencia_NFs_Entrada.docx
- **Modificado:** 2022-04-18
- **Tamanho:** 74 KB

---

THOMSON REUTERS

                                                                                     __Módulo PRODEPE__

__  __

__                                    Relatório de Conferência das Notas Fiscais de Entrada__

__Localização__: Menu Estadual, Módulo Prodepe, item Relatórios 🡪 Conferência das Notas Fiscais de Entrada

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS4402

Tratamento das Devoluções

Alteração do cálculo do crédito presumido para tratamento das notas fiscais de devolução de vendas \(ver __RN03__, coluna N/D\)

23/01/2014

\(criação do docto\)

OS4257

Alteração da coluna Produto

Alteração do conteúdo da coluna “Produto” \(ver __RN03__\)\.

02/06/2014

MFS21913

Geração dos Registro do PRODEPE no Sped Fiscal

Inclusão da coluna “Código Informação Adicional” \(ver __RN03 __e__ RN04__\)

05/11/2018

MFS62923

Tratamento de CFOP – Rateio Proporcional – Livro Incentivado

O objetivo dessa demanda é incluir tratamento para os CFOP’s que obrigatoriamente necessitam serem rateados proporcionalmente entre os Livros Incentivados e Não Incentivado\. \(Processo será com base na nova tela de parâmetros\) Industria\. RN02\.a e RN02\.b\.

26/04/2021

MFS81635

Inclusão do Campo Valor do Item no relatório de Incentivado

O objetivo dessa demanda é incluir a coluna Valor do Item no relatório de Produtos Incentivados\.

18/04/2022

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

O objetivo deste relatório é auxiliar a conferência do cálculo dos incentivos, já que o ICMS das operações de entrada interfere diretamente no resultado dos cálculos\.

O relatório demonstra as notas ficais de entrada dos livros incentivados e não incentivado\. No caso dos incentivados,  a coluna “Incentivo” indica se a nota foi incentivada ou não\.   

Para a emissão do relatório, é necessário que a rotina de incentivo das notas fiscais já tenha sido executada\.	

__RN01__

__                                                        Parâmetros de Tela__

Campo “__Estabelecimento__”:

- lista com a relação de todos os Estabelecimentos que sejam de Pernambuco e que tenham sido parametrizados no módulo Prodepe \(que constem na parametrização “Parâmetros 🡪 Dados Gerais”\);
-  *não* existirá a opção “Todos”;

Campos “__Data Inicial__” e “__Data Final__”:

- o usuário deverá informar uma data inicial e final do período a ser pesquisado;
- será verificada a validade das datas e se a data inicial é <= data final;

Campo  “__Tipo de Livro__”:

- este campo apresenta duas opções: “Incentivados” e “Não Incentivado”;
- as opções são alternativas;
- a opção default na abertura da tela é = “Incentivados”;

Campo “__Grupo de Incentivo__”:

- o campo só será habilitado quando a opção escolhida for = “Incentivados”;
- lista com a relação de todos grupos de incentivo cadastrados para o estabelecimento selecionado;  
- a lista exibirá o código e a descrição dos grupos identificados;
- *não* existirá a opção “Todos”; 

__RN02__

__                                     Recuperação e Processamento dos Dados__

__Origem dos dados:__

     \- Tabela dos Documentos Fiscais \- Capa

     \- Tabela dos Documentos Fiscais \- Itens

     \- Tabela de controle das notas incentivadas do Prodepe \(ICT\_GUIA\_INCENT\)

O relatório será gerado com as notas fiscais de entrada com data fiscal compreendida no período solicitado, que atendam aos demais parâmetros informados em tela, e com as seguintes características:

- apenas as notas fiscais de classificação fiscal = 1 ou 3 \(Mercadoria ou Nota Mista\)
- apenas notas não canceladas
- notas *com ou sem* itens de mercadoria
- as notas sem CFOP preenchido também *devem ser consideradas*, para que situações de erro possam ser validadas\. 

Outros detalhes dependem do parâmetro “Tipo do Livro” selecionado em tela, da seguinte forma:

Na opção “__Livros Incentivados__”:

- Neste caso serão consideradas *apenas* as notas fiscais de entrada que estejam relacionadas ao grupo de incentivo escolhido;

\(para isso a geração utiliza a tabela de controle das notas incentivadas do Prodepe \(ICT\_GUIA\_INCENT\)\)

- Os dados serão processados por Estabelecimento e Grupo de Incentivo, conforme layout descrito na __RN04__;
- Ao final de cada Estabelecimento e Grupo de Incentivo, serão geradas três linhas de total com a soma das colunas “Valor Contábil”, “ICMS” e “ICMS FECP”, da seguinte forma: uma linha para totalizar as operações incentivadas, outra para as operações não incentivadas e outra para o total geral do Estabelecimento / Grupo de Incentivo;

Na opção “__Livros Não Incentivados__”:

- Neste caso serão consideradas *apenas* as notas fiscais de entrada que *não* estejam relacionadas a nenhum livro incentivado;
- Os dados serão processados por Estabelecimento, conforme layout descrito na __RN04__;
- Ao final de cada Estabelecimento, será gerada apenas uma linha de total com a soma das colunas “Valor Contábil”, “ICMS” e “ICMS FECP”;

__RN02\.a__

__Tratamento Cálculo de Proporcionalidade – Por CFOP – Conferência Entradas – Incentivados \- INDÚSTRIA__

\[__MFS62923__\] Cálculo de Proporcionalidade para a Conferência do livro de Entradas Incentivado – Industria

<a id="_Hlk70443933"></a><a id="_Hlk70443899"></a>Modalidade de Incentivo: Regra específica do cálculo do incentivo da Indústria\.

Inclusão de regra de tratamento para geração da Conferência das Entradas para os CFOP’s parametrizado na tela “Cálculo de Proporcionalidade – Por CFOP”, devem serem rateados proporcionalmente de acordo com o percentual das saídas, na rotina de geração dos Livros Incentivados no Módulo do Prodepe\. 

__Embasamento legal:__ De acordo com o disposto nas alíneas “c” e “e” do inciso VIII do Art\. 1º da Portaria 239/01\.

__Cálculo de Proporcionalidade – Por CFOP__:

 

O tratamento deverá ser efetuado no momento da geração da Conferência das Entradas, o programa deverá consultar se o CFOP está parametrizado na tela “Cálculo de Proporcionalidade \-Por CFOP” e se caso estiver, aplicar o fator de rateio proporcional de acordo com o percentual das saídas, que deverá ser recuperado da tabela ICT\_TOT\_SAIDA\_INCE, o percentual que será utilizado corresponde ao campo VLR\_PERC\_SAI\. 

Obs\* *Estes percentuais *da tabela *ICT\_TOT\_SAIDA\_INCE são previamente calculados no menu “Cálculo da Proporção das Saídas”\.*

__Tratamento__: 

Conferência das Entradas \- Incentivados:

__Se__ o CFOP estiver preenchido na tela “Cálculo de Proporcionalidade \- Por CFOP” 

  __E__ o campo de SERIE\_LIVRO da tabela ICT\_TOT\_SAIDA\_INC for igual à “B” 

    __E __o campo de SUB\_SERIE\_LIVRO da tabela ICT\_TOT\_SAIDA\_INCE igual ao campo SUB\_SERIE\_LIVRO da tabela ICT\_FAIXA\_INCENT;

     __E __o campo COD\_GRP\_INCENT da tabela ICT\_TOT\_SAIDA\_INCE igual ao campo COD\_GRP\_INCENT LIVRO da tabela ICT\_FAIXA\_INCENT;

__Aplicar__ o rateio proporcional com o percentual do campo VLR\_PERC\_SAI, nos campos de valores \(Valor Contábil, ICMS e ICMS FECP\), dos campos preenchidos: Vide “Preenchimento dos Dados no Relatório”\.

VALOR CONTÁBIL = VLR\_CONTABIL \* VLR\_PERC\_SAI \) / 100

ICMS = ICMS \* VLR\_PERC\_SAI \) / 100

ICMS FECP = ICMS FECP \* VLR\_PERC\_SAI \) / 100

__RN02\.b__

__Tratamento Cálculo de Proporcionalidade – Por CFOP – Conferência Entradas – Não Incentivados \- INDÚSTRIA__

\[__MFS62923__\] Cálculo de Proporcionalidade para a Conferência do livro de Entradas Não Incentivado – Industria

Modalidade de Incentivo: Regra específica do cálculo do incentivo da Indústria\.

Inclusão de regra de tratamento para geração da Conferência das Entradas para os CFOP’s parametrizado na tela “Cálculo de Proporcionalidade – Por CFOP”, devem serem rateados proporcionalmente de acordo com o percentual das saídas, na rotina de geração dos Livros Incentivados no Módulo do Prodepe\. 

__Embasamento legal:__ De acordo com o disposto nas alíneas “c” e “e” do inciso VIII do Art\. 1º da Portaria 239/01\.

__Cálculo de Proporcionalidade – Por CFOP__:

 

O tratamento deverá ser efetuado no momento da geração da Conferência das Entradas, o programa deverá consultar se o CFOP está parametrizado na tela “Cálculo de Proporcionalidade \-Por CFOP” e se caso estiver, aplicar o fator de rateio proporcional de acordo com o percentual das saídas, que deverá ser recuperado da tabela ICT\_TOT\_SAIDA\_INCE, o percentual que será utilizado corresponde ao campo VLR\_PERC\_SAI\. 

Obs\* *Estes percentuais *da tabela *ICT\_TOT\_SAIDA\_INCE são previamente calculados no menu “Cálculo da Proporção das Saídas”\.*

__Tratamento__: 

Conferência das Entradas \- Não Incentivados:

__Se__ o CFOP estiver preenchido na tela “Cálculo de Proporcionalidade \- Por CFOP” 

  __E__ o campo de SERIE\_LIVRO da tabela ICT\_TOT\_SAIDA\_INC for igual à “A” 

    __E __o campo de SUB\_SERIE\_LIVRO da tabela ICT\_TOT\_SAIDA\_INCE igual ao campo SUB\_SERIE\_LIVRO da tabela ICT\_FAIXA\_INCENT;

     __E __o campo COD\_GRP\_INCENT da tabela ICT\_TOT\_SAIDA\_INCE igual ao campo COD\_GRP\_INCENT LIVRO da tabela ICT\_FAIXA\_INCENT;

__Aplicar__ o rateio proporcional com o percentual do campo VLR\_PERC\_SAI, nos campos de valores \(Valor Contábil, ICMS e ICMS FECP\), dos campos preenchidos: Vide “Preenchimento dos Dados no Relatório”\.

VALOR CONTÁBIL = VLR\_CONTABIL \* VLR\_PERC\_SAI \) / 100

VALOR ITEM = VLR\_ITEM \* VLR\_PERC\_SAI \) / 100

ICMS = ICMS \* VLR\_PERC\_SAI \) / 100

ICMS FECP = ICMS FECP \* VLR\_PERC\_SAI \) / 100

__RN03__

__                                                   Preenchimento dos Dados no Relatório__

__Coluna / linha de total __

__Conteúdo __

Data Fiscal

Data fiscal do documento

N\. Docto

Número e Série do documento

Alteração __MFS21913__: Concatenação do número do documento com a série do documento\. Previsão do tamanho máximo de 9 dígitos para o número do documento \(ao invés de 12\)\. Desta forma, o tamanho máximo do campo “N\.Docto” é de 13 posições:  “XXXXXXXXX__/__XXX”\.

\(*9 posições para o número do documento \+ “/” \+ 3 posições para a série\)  *

Item

Número do item da nota fiscal\. Para as notas sem itens, a coluna deve ser preenchida com “s/item”, para ficar claro que é uma nota sem itens\.

Emitente

Razão Social da pessoa física/jurídica do documento

N/D

Coluna criada na __OS4402__\.

Esta coluna demonstra se a nota é normal ou uma devolução, da seguinte forma:

\- Se campo “03\-Normal ou Devolução” da NF \(SAFX07\) = “1” \(Normal\) 🡪 será impresso “N”

\- Se campo “03\-Normal ou Devolução” da NF \(SAFX07\) = “2” \(Devolução\) 🡪 será impresso “D”

CFOP

CFOP do item \(ou da capa, se for nota sem item\)

Nat Op

Natureza de operação do item \(ou da capa, se for nota sem item\)

Produto

Descrição do produto do item da nota\. 

Alteração da OS4257 \(Jun/2014\):

Indicador, código e descrição do produto do item da nota, no formato:

                           “9\-XXXXXXXXXXXXX – XXXXXXXXXXXXXXXXXXXXXX” 

Para as notas sem itens, a coluna ficará em branco\.

Vlr Contábil

Valor contábil do item da nota \(ou valor total da capa, se for nota sem item\)  

Vlr Item

Valor do item da nota \(ou valor total produto da capa, se for nota sem item\)  

ICMS 

Valor do ICMS do item da nota \(ou valor do ICMS da capa, se for nota sem item\)  

ICMS FECP

Valor do FECEP do item da nota\. Para as notas sem itens, a coluna sempre ficará em branco, pois a capa da nota \(SAFX07\) não tem esta informação\.

<a id="_Hlk529179498"></a>Cód\. Inf\. Adic\. \(C177\)

Campo incluído no layout pela __MFS21913__\.

\- Notas Fiscais dos livros incentivados:

   Esta coluna exibe o código de informação adicional do item, informação gerada pela rotina 

   “Incentivo das Notas Fiscais”, e gravada na tabela guia dos incentivos \(ICT\_GUIA\_INCENT,

    coluna ??????\)\.

\- Notas Fiscais dos livros não incentivados \(A01\):

   Nesse caso, esta coluna será preenchida sempre com o código “__PE000100__”\.

Obs\.: Este código se refere à tabela “__5\.6 \- Tabela informações adicionais dos itens do documento fiscal__” do Sped Fiscal, e é utilizado no preenchimento do campo COD\_INF\_ITEM do registro C177 \(registro “filho” do C170\)\.  No caso das notas do livro *não* incentivado, a informação do código é gerada automaticamente apenas no momento da geração do Sped Fiscal, com o conteúdo específica para os produtos não incentivados \(“PE000100”\)\.

Incentivo

Indicador de incentivo

Esta coluna existe apenas na opção “__Incentivados__” \(opção “Tipo de Livro” da tela da geração\)\.

*Trata\-se do indicador gerado na rotina do incentivo das notas fiscais, e armazenado na tabela de controle das notas incentivadas do Prodepe \(ICT\_GUIA\_INCENT\)\.*

Linha  “Total das Operações com Incentivo”

Total das colunas “Vlr\. Contábil”, “ICMS” e “ICMS FECP” somente das linhas com indicador de incentivo = “S”  \(itens *incentivados*\)

Linha “Total das Operações sem Incentivo”

Total das colunas “Vlr\. Contábil”, “ICMS” e “ICMS FECP” somente das linhas com indicador de incentivo = “N”  \(itens *não incentivados\)*

Linha “Total Geral”

Total geral das colunas “Vlr\. Contábil”, “ICMS” e “ICMS FECP” 

__RN04__

__                                                                     Layout do Relatório__

O layout do relatório depende do parâmetro “*Tipo de Livro*” da tela de emissão\.

As diferenças são as seguintes:

\- A coluna “__Incentivo__” só existe na opção “__Incentivados__”;

\- Na opção “__Incentivados__”, o relatório é gerado por estabelecimento e Grupo de Incentivo, e no título aparece o código do Grupo;

\- Na opção “__Não Incentivados__”, como não existe grupo de incentivo, o relatório é gerado por estabelecimento, e no título aparece

  apenas a descrição “Livro Não Incentivado”;

\- Na opção “__Incentivados__” existem três linhas de total por estabelecimento/Grupo de Incentivo;

\- Na opção “__Não Incentivados__” existe apenas uma linha de total por estabelecimento;

Segue layout das duas opções:

                                                                Opção Tipo de Livro = “__Incentivados__”:

__                  __

__                                        Conferência das Notas Fiscais de Entrada  \- Grupo de Incentivo: 999__

__                                                                              Estabelecimento: XXXXXX__

__                                                                       Período: 99/99/9999 a 99/99/9999__

Data Fiscal 

N\. Docto 

Item

Emitente

N/D

CFOP

Nat

Op 

Produto

  Valor Contábil

Valor Item

ICMS

ICMS FECP

Cód\. Inf\. Adic\. \(C177\)

Incentivo

Total das Operações com Incentivo:

Total das Operações sem Incentivo:

Total Geral:

                                                       

                                                                 Opção Tipo de Livro = “__Não Incentivados__”:

__                  __

__                                            Conferência das Notas Fiscais de Entrada  \- Livro não Incentivado__

__                                                                              Estabelecimento: XXXXXX__

__                                                                       Período: 99/99/9999 a 99/99/9999__

Data Fiscal 

N\. Docto 

Item

Emitente

N/D

CFOP

Nat

Op 

Produto

  Valor Contábil

ICMS

ICMS FECP

Cód\. Inf\. Adic\. \(C177\)

Total Geral:

        __Ordenação dos Dados__ 🡪 Data Fiscal / Número do Documento / Número do Item

        = = = = =

