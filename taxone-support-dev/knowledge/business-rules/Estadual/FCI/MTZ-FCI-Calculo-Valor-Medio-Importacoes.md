# MTZ-FCI-Calculo-Valor-Medio-Importacoes

- **Fonte:** MTZ-FCI-Calculo-Valor-Medio-Importacoes.docx
- **Modificado:** 2026-01-20
- **Tamanho:** 50 KB

---

                        __FCI – Cálculo do Valor Médio das Importações__

__Localização__: Menu Estadual, Módulo FCI à Obrigações à Cálculo do CI à Cálculo do Valor Médio das Importações

##                                            Documento de Requisito

__Doc__

__Alteração__

__Data__

__Resp__

OS3874\-F1

Cálculo do valor médio das importações

02/09/2013	

\(Criação do doc\)

Vânia Mattos

CH26659\_2015

Este documento tem como objetivo alterar a RN03 – Etapa 1 para inclusão do ICMS Não Escriturado no cálculo e a RN04 para composição do ICMS Não Escriturado a ser gravado no relatório\.

29/12/2015

Julyana Perrucini

CH21391\_2017 \(MFS\-14873\)

Este documento tem como objetivo alterar a RN03 – Etapa 1 para tratar a quantidade de documentos fiscais complementares que não devem compor no cálculo\.

22/11/2017

Julyana Perrucini

MFS68270

Inclusão de mensagem para tratar a quantidade zerada para o cálculo do valor médio das importações

25/08/2021

Andréa Rocha

MFS682902

Considerar a SAFX49 no cálculo do FCI,quando o campo 216 \- VLR\_ADUANEIRO não estiver preenchido na SAFX08\.

08/10/2024

Liliane Assaf

MFS691969

Inclusão da recuperação dos insumos que tiveram movimento de aquisição no mercado nacional\.  Esses insumos serão utilizados no cálculo do CI\.

05/02/2025

Andréa Rocha

__RN00 – Regras Gerais__

Resumo do conceito do cálculo:

Neste processo é realizado o cálculo do valor médio das importações\.

Estes valores serão utilizados posteriormente para o cálculo do CI \(Conteúdo de Importação\) de cada produto industrializado sujeito ao FCI\.

Será feita uma pesquisa geral das notas fiscais de importação, agrupadas por produto, e totalizando para cada produto o valor e a quantidade\. Na totalização das notas, todos os produtos terão sua unidade de medida convertida para a unidade de medida do cadastro \(SAFX2013\)\.

Na primeira execução do cálculo, ou seja, na implantação do modulo, a pesquisa será realizada para o mês/ano de referência informado em tela, e também para os meses anteriores até o limite de meses informado pelo usuário\. Este procedimento é para recuperar as importações de produtos não importados no mês de referência\.

A partir do mês seguinte à implantação, ou seja, do segundo cálculo em diante, a pesquisa passará a ser feita apenas para o mês de referência\. Neste caso, se não existirem importações no mês de referência, o cálculo irá utilizar o valor médio já calculado em meses anteriores\.

__RN01 – Parâmetros de Tela__

__Período de referência p/o cálculo à __Neste campo o usuário informará um mês e ano \(MMAAAA\), que será utilizado como base para a pesquisa das importações\.

__No\. de meses anteriores p/pesquisa das importações \(apenas na implantação do módulo\) à __Este campo será inicializado com o valor zero\. Neste campo o usuário informará, apenas na implantação do módulo,  o limite de meses anteriores para realizar a pesquisa das importações\. 

__\[MFS691969\]__

__No\. de meses anteriores p/pesquisa das aquisições nacionais \(apenas na implantação do módulo\) à __Este campo será inicializado com o valor zero\. Neste campo o usuário informará, apenas na implantação do módulo,  o limite de meses anteriores para realizar a pesquisa das aquisições nacionais\. 

__\[MFS682902\]__

__Considerar Valor Aduaneiro da Tabela de Operações de Importação \(SAFX49\)__ à quando esse parâmetro for marcado, o valor aduaneiro da SAFX49 será considerado no Cálculo do Valor Médio das Importações, quando o campo 216\-Valor Aduaneiro da SAFX08 não estiver preenchido\.__ __

__Estabelecimentos__ àNeste campo será exibida a lista dos estabelecimentos da Empresa do login\. 

__RN02 – Processamento dos Dados__

__Origem dos Dados__: Tabela dos Documentos Fiscais \(SAFX07/SAFX08\)

                                   Parametrização das Operações de Entrada dos Insumos Importados

                                   Tabela de Operações de Importação \(SAFX49\) __\(\*\*\*\) \[MFS682902\]__

__Destino:__ Tabela do Valor Médio das Importações por Insumo \(\*\)

               __ __Tabela dos Documentos Fiscais de Importação do FCI __\(\*\*\)__

 

__\(\*\) __Tabela auxiliar que armazena o valor médio de importação por insumo 

__\(\*\*\) __Tabela auxiliar que armazena os documentos fiscais processados no cálculo de cada insumo\.

__\(\*\*\*\)__ Tabela não obrigatória, será utilizada quando o campo 216\- Valor Aduaneiro da SAFX08 não estiver preenchido\.

 

__O processamento é por Estabelecimento\.__

Para cada Estabelecimento, será calculado o valor médio das importações de cada produto identificado nas notas\.

O processo se divide em duas etapas:

__Etapa 1__ àProcessamento das notas do período de referência informado em tela\.

__Etapa 2__ àProcessamento das notas dos períodos anteriores, até o limite informado em tela\. A Etapa 2 será executada apenas na implantação do sistema\.

__\[MFS691969\]__ Inclusão da recuperação dos insumos que tiveram movimento de aquisição no mercado nacional

__Etapa 3__ àProcessamento das notas do período de referência informado em tela, para recuperar as notas fiscais de aquisições nacionais dos insumos\.  Posteriormente, esses produtos serão usados no cálculo do CI para identificar os insumos que passaram a ser adquiridos no mercado nacional, e não devem fazer parte do cálculo do CI\.

__Etapa 4__ àProcessamento das notas dos períodos anteriores, até o limite informado em tela, para recuperar as notas fiscais de aquisições nacionais dos insumos\.  Posteriormente, esses produtos serão usados no cálculo do CI para identificar os insumos que passaram a ser adquiridos no mercado nacional, e não devem fazer parte do cálculo do CI\.

A seguir serão definidas as regras do processamento de cada uma das etapas\.

__RN03 – Etapa 1__

__Critérios para a recuperação dos documentos \(SAFX07/SAFX08\)__:

    \- Empresa = código da empresa do login;

    \- Estabelecimento = código do estabelecimento da geração; 

    \- Data Fiscal = deve ser uma data referente ao período informado em tela;

    \- Movto\_E\_S <> “9” \(somente entradas\)

    \- Somente notas *não* canceladas;

    \- Considerar todos os itens com CFOP = “3”, __*exceto*__ quando ocorrer uma das seguintes situações:

         1\-O item tiver CFOP’s ou CFOP/NAT parametrizado na opção “Parâmetros à Operações de Entrada

             dos Insumos Importados à Aquisições do Exterior \(Exceções\)”;

         2\-O item tiver o Código de Situação Tributária A = “6” \(“Estrangeira \- Importação direta, sem similar 

             nacional, constante em lista de Resolução CAMEX”\);

        

             *\(trata\-se do campo “30\-Tabela Situação Estadual A” da SAFX08\)*

    \- Considerar os itens com CFOP ou CFOP/NAT parametrizado na opção “Parâmetros à Operações

       de Entrada dos Insumos Importados à Aquisições Internas” __e__ que tenham o Código de Situação

       Tributária A igual a uma das seguintes opções:

         “2” \(Estrangeira \- Adquirida no mercado interno, exceto a indicada no código 7\)

         “3” \(Nacional \- mercadoria ou bem com Conteúdo de Importação > 40% e <= a 70%\)

         “8” \(Nacional \- mercadoria ou bem com Conteúdo de Importação > a 70%\)

__\[MFS682902\]__

__Critérios para a recuperação das Operações de Importação \(SAFX49\)__

Recuperar os registros da tabela de Operações de Importação, quando os três critérios abaixo forem atendidos:

    \- Parâmetro “Considerar Valor Aduaneiro da Tabela de Operações de Importação \(SAFX49\)” estiver marcado;

    \- CFOP do item de mercadoria \(SAFX08\) iniciar por “3”;

    \- Campo 216 “Valor Aduaneiro” da SAFX08 não estiver preenchido

Para recuperar os registros das operações de importação, partir das seguintes informações da capa e do item de mercadoria:

__SAFX49__

__SAFX07/SAFX08__

01 – COD\_EMPRESA

01 – COD\_EMPRESA da SAX07

02 – COD\_ESTAB

02 – COD\_ESTAB da SAX07

05 \- DAT\_NF \(Data da Nota Fiscal\) Data de Emissão

11 \- DATA\_EMISSAO \(Data de Emissão da SAX07\)

06 \- Indicador de Pessoa Física/Jurídica

06 \- Indicador de Pessoa Física/Jurídica da SAX07

07 \- Código da Pessoa Física/Jurídica

07 \- Código da Pessoa Física/Jurídica da SAX07

08 \- Número da Nota Fiscal \(NUM\_NF\)

08 \- Número da Nota Fiscal da SAX07

09 \- Série da Nota Fiscal \(SERIE\_NF\)

09 \- Série da Nota Fiscal da SAX07

10 \- Subsérie da Nota Fiscal \(SUB\_SERIE\_NF\)

10 \- Subsérie da Nota Fiscal da SAX07

11 \- Indicador do Produto

13 \- Indicador do Produto da SAFX08

12 \- Código do Produto

14 \- Código do Produto da SAFX08

13 \- Número do Item da Nota Fiscal

18 \- Número do Item da Nota Fiscal da SAFX08

Para um item de mercadoria \(SAFX08\) podem existir vários registros de importação \(SAFX49\)\. Se for encontrado mais de um registro na SAFX49 para um item da SAFX08, todos devem ser considerados para totalização do Valor Aduaneiro\.  

Os itens recuperados serão agrupados e totalizados por produto\.

__Totalização do valor__:

      O valor de cada item a ser totalizado dependerá do CFOP e do “Código de Situação Tributára A” do item,

      da seguinte forma:

      Se CFOP “3” à utilizar o conteúdo do campo 216 “Valor Aduaneiro” da SAFX08\. 

__                                 \[MFS682902\]__

                                 Caso o campo 216 “Valor Aduaneiro” da SAFX08 não esteja preenchido, considerar os seguintes valores da SAFX49:

                                  29\-“Valor dos Produtos” \(VLR\_PRODUTO\) \+ 62\-“Despesas de Fretes – Moeda” \(VLR\_FRETE\_MOEDA\) \+ 64\-“Despesas de Seguros – Moeda” \(VLR\_SEGURO\_MOEDA\) 

__\[ALTERADA – CH26659\_2015\]__

      Se CFOP  <> “3” à neste caso, o valor a ser utilizado depende  do “Código de Situação Tributára A”:

           Se = “2” \- utilizar o conteúdo de \[ Valor Contábil do Item – Valor ICMS – ICMS Não Escriturado – Valor IPI \]

           Se = “3” \- utilizar o conteúdo de \[ \(Valor Contábil do Item – Valor ICMS – ICMS Não Escriturado – Valor IPI\) / 2 \]

           Se = “8” \- utilizar o conteúdo de \[ Valor Contábil do Item – Valor ICMS – ICMS Não Escriturado – Valor IPI \]

__Totalização da quantidade__:

      A quantidade das importações será totalizada sempre tendo como base a unidade de medida do cadastro

      do produto \(SAFX2013\)\. Este procedimento é adotado para tratar os casos em que existirem notas de  

      importação de um *mesmo insumo,* com unidades de medida diferentes\.

*     Obs: A unidade tratada no FCI será sempre a unidade da SAFX2007, pois as tabelas da composição dos*

*             produtos \(SFAX16/17/18\) utilizam esta unidade\. *

     Se campo “25\-Unidade de Medida” do item \(SAFX08\) <> campo “14\-Código de Medida” \(SAFX2013\)

           Fazer a conversão antes de efetuar a totalização da quantidade\.

           A conversão utilizará as tabelas de conversão de unidades do módulo DW, e seguirá o procedimento

           padrão utilizado pelo Mastersaf, da seguinte forma:

           \- Caso exista registro de conversão das unidades na tabela de conversão de unidades por produto:

              Efetuar a conversão considerando o fator da tabela de conversão por produto;

           \- Caso contrário:

              Efetuar a conversão considerando o fator da tabela de conversão “padrão”;

          Se não for encontrando fator de conversão para nenhuma das duas opções, será gravado no log a

          mensagem de erro abaixo, e o item em questão será desconsiderado do processo:

         *“Não identificado fator de conversão de XXX para XXX\. O documento foi desconsiderado do processo”*

          \(o log exibirá também os dados de identificação do item em questão na coluna correspondente do

           log, para que o usuário possa identificar o item de documento fiscal com problemas\)  

A quantidade a ser utilizada na totalização será a própria quantidade do item, caso a unidade do item seja = unidade da SAFX2013, caso contrário, será a quantidade convertida conforme a regra acima\. 

__\[ALTERADA \- CH21391\_2017 \(MFS\-14873\)\]__

Se tratando de nota fiscal complementar, campo “125\-Situação Especial” da capa \(SAFX07\) = 5, a sua quantidade deverá ser desconsiderada na totalização que irá compor o cálculo do valor médio da importação, mas o valor total permanece compondo o cálculo normalmente, com isso, a nota será grava e apresentada normalmente, mas não terá quantidade, isso porque por ser complemento de imposto à quantidade a ser considerada é o da nota principal\.

__Cálculo do Valor médio da importação:__

     

Para cada produto processado, calcular o valor médio das importações da seguinte forma:

       Valor Médio = Valor Total  / Quantidade Total 

__\[MFS\-68270\] __Tratamento para a quantidade total zerada

__Obs__\.: Antes de fazer o cálculo do Valor médio, deve\-se verificar se o campo quantidade total está zerado\.  Caso esteja zerado, dar a mensagem de erro no log e continuar o processamento\. E o cálculo do valor médio deve ser preenchido com zero\. Mostrar a mensagem abaixo e mostrar junto com a mensagem, o código do produto que está com erro:

*“Erro no cálculo do valor médio das importações, a quantidade do produto está zerada\.  Favor verificar”*

Os valores calculados para cada produto serão armazenados numa tabela auxiliar *\(Tabela do Valor Médio das Importações por Insumo\)* e posteriormente, serão utilizados no cálculo do CI \(Conteúdo de Importação\) de cada produto final fabricado \(produtos sujeitos ao FCI, cujos valores calculados ficam na SAFX214\)\.

Para cada produto processado armazenar as seguintes informações:

\*\*\* Empresa

Código da empresa do login

\*\*\* Estabelecimento

Código do estabelecimento da geração

\*\*\* Produto

Identificação do insumo

\*\*\* Período \(mês e ano\)  

Mês e ano das notas processadas

Valor Médio calculado

Valor médio das importações calculado

Unid\. de Medida 

Unidade de medida na qual foi totalizada a quantidade \(campo “14\-Código de Medida” da SAFX2013\)\.

\(lembrando que será utilizada sempre a unidade de medida do cadastro do produto, e quando na nota da importação constar outra unidade, será efetuada a conversão de medida\)

__RN03 – Etapa 2__

__Esta etapa será realizada apenas quando se tratar da implantação do módulo FCI,__ ou seja, apenas quando o parâmetro “*Número de meses anteriores p/pesquisa das importações \(apenas na implantação do módulo\)*” for <> zero\.

Caso contrário, esta etapa não será executada\.

Nesta etapa será realizada a pesquisa das operações de importação de produtos __não importados no mês de referência do cálculo__ \(mês apurado na Etapa 1\)\.

Serão processados todos os meses anteriores até o limite parametrizado no parâmetro “*Número de meses anteriores p/pesquisa das importações \(apenas na implantação do módulo\)*”\.

Será processado um mês de cada vez, e no processamento de cada mês a regra básica é a seguinte:

NÃO CONSIDERAR OS PRODUTOS JÁ REGISTRADOS NOS MESES SUBSEQUENTES, ATÉ O MÊS DE REFERÊNCIA\.

Exemplo:

Mês de referência                        =  OUT/2013

Parâmetro do número de meses = 18

Com base nesses parâmetros, será processado em primeiro lugar o mês de OUTUBRO, que seria a Etapa 1\.

A seguir, seria processado o mês de SET/2013, seguindo as mesmas regras de recuperação dos dados, mas __*não*__ considerando as importações dos produtos já registrados no mês de OUTUBRO\.

A seguir, seria processado o mês de AGO/2013, seguindo as mesmas regras de recuperação dos dados, mas __*não*__ considerando as importações dos produtos já registrados nos meses de SETEMBRO e OUTUBRO\.

A seguir, seria processado o mês de JUL/2013, seguindo as mesmas regras de recuperação dos dados, mas __*não*__ considerando as importações dos produtos já registrados nos meses de AGOSTO, SETEMBRO e OUTUBRO\.

E assim sucessivamente até o *décimo oitavo* mês anterior ao mês de OUT/2013, ou seja, o processamento  iria até o mês de ABR/2012 \(inclusive\)\.

A gravação dos dados na tabela será feita da mesma forma descrita na Etapa 1, sendo que no campo “Período”  será sempre gravado o mês/ano das notas processadas para a apuração do valor médio\.

__RN04 – Gravação dos Dados p/o Relatório de Conferência do Cálculo do Valor Médio das Importações__

Durante o processamento das notas, conforme descrito na __RN02/RN03__, a rotina irá armazenar as informações de cada item de documento fiscal utilizado no cálculo\.

Posteriormente, esses dados serão utilizados para emissão do relatório “Conferência do Cálculo do Valor Médio das Importações”\. 

A tabela que armazena estes dados é a *Tabela dos Documentos Fiscais de Importação do FCI*\. É uma tabela “filha” da *Tabela do Valor Médio das Importações por Insumo*\), consequentemente, sua chave é igual à chave da “mãe” \+ Número da Nota Fiscal \+ Série da Nota Fiscal \+ Identificação da Pessoa Fios/Jur\.

*\(como se trata de NFs de entrada, é necessário ter outros dados na chave da nota, além do número e a série\)*

__\[ALTERADA – CH26659\_2015\]__

 Informações de cada item processado a serem armazenados:

\- Número da nota fiscal

\- Série da nota fiscal

\- Identificação da pessoa fis/jur \(indicador e código\)

\- Data de emissão da nota fiscal

\- Data fiscal da nota fiscal

\- Número do item

\- CFOP do item

\- CST do item \(concatenação dos códigos de situação tributária A e B, campos 30 e 31 da SAFX08\) 

\- Unidade de medida \(campo 25\-Unidade de Medida da SAFX08\)

\- Quantidade do item \(campo 24\-Quantidade da SAFX08\)

\- Quantidade convertida \(quantidade que foi utilizada na totalização do item, de acordo com a __RN03__, item 

                                            “Totalização da Quantidade”\)

\- Valor contábil do item 

\- Valor do ICMS do item \+ ICMS Não Escriturado do item \(somar em único campo\)

\- Valor do IPI do item

\- Valor Aduaneiro \(SAFX08\)

__\[MFS682902\]__

\- Valor dos Produtos \(SAFX49\) 

\- Valor das Despesas de Fretes – Moeda \(SAFX49\)

\- Valor das Despesas de Seguros – Moeda \(SAFX49\)

\- Valor utilizado no cálculo \(valor que foi utilizado na totalização do item, de acordo com a __RN03__, item 

                                            “Totalização do Valor”\)

__\[MFS691969\]__ Inclusão da recuperação dos insumos que tiveram movimento de aquisição no mercado nacional

__RN05 – Etapa 3__

__Critérios para a recuperação dos documentos de aquisições nacionais \(SAFX07/SAFX08\)__:

    \- Empresa = código da empresa do login;

    \- Estabelecimento = código do estabelecimento da geração; 

    \- Data Fiscal = deve ser uma data referente ao período informado em tela;

    \- Movto\_E\_S <> “9” \(somente entradas\)

    \- Somente notas *não* canceladas;

    \- Produto = o produto do item deve estar cadastrado na SAFX17 \(Insumos\) ou SAFX18 \(Embalagens\), como insumo, que corresponde aos campos 06 e 07, tanto na SAFX17 como na SAFX18;

    \- Considerar todos os itens que tiver CFOP ou CFOP/NAT parametrizado na opção “Parâmetros 🡪 Operações de Entrada dos Insumos Nacionais 🡪 Aquisições Internas 🡪 CFOP ou CFOP/Natureza de Operação __e__ que __não__ tenham o Código de Situação Tributária A igual a uma das seguintes opções:

         “2” \(Estrangeira \- Adquirida no mercado interno, exceto a indicada no código 7\)

         “3” \(Nacional \- mercadoria ou bem com Conteúdo de Importação > 40% e <= a 70%\)

         “8” \(Nacional \- mercadoria ou bem com Conteúdo de Importação > a 70%\)

A geração irá armazenar as informações de cada item de documento fiscal recuperado conforme as regras acima\.  Os dados serão armazendos em 2 tabelas diferentes, uma tabela vai armazenar somente o produto que teve aquisição nacional e a outra tabela vai armazenar as informações do produto por nota fiscal\.

Posteriormente, esses dados serão utilizados para o cálculo do CI e para a emissão do relatório “Conferência das Aquisições Nacionais\.”\. 

Para cada produto processado, armazenar as seguintes informações \(Tabela por produto\):

\*\*\* Empresa

Código da empresa do login

\*\*\* Estabelecimento

Código do estabelecimento da geração

\*\*\* Produto

Identificação do insumo

\*\*\* Período \(mês e ano\)  

Mês e ano das notas processadas

Unidade de Medida

Código de medida do item 

Quantidade do item

Quantidade do item 

Valor contábil do item

Valor contábil do item

Informações de cada item processado a serem armazenados \(Tabela Por Nota\):

\- Empresa;

\- Estabelecimento;

\- Período de Referência;

\- Produto;

\- Número da nota fiscal;

\- Série da nota fiscal;

\- Identificação da pessoa fis/jur \(indicador e código\);

\- Data de emissão da nota fiscal;

\- Data fiscal da nota fiscal;

\- Número do item;

\- CFOP do item;

\- CST do item \(concatenação dos códigos de situação tributária A e B, campos 30 e 31 da SAFX08\);

\- Unidade de medida \(campo 25\-Unidade de Medida da SAFX08\);

\- Quantidade do item \(campo 24\-Quantidade da SAFX08\);

\- Valor contábil do item \(campo 64\-Valor Contábil do Item da SAFX08\);

    __RN06 – Etapa 4__

__Esta etapa será realizada apenas quando se tratar da implantação do módulo FCI,__ ou seja, apenas quando o parâmetro *“No\. de meses anteriores p/pesquisa das aquisições nacionais \(apenas na implantação do módulo\)”* for <> zero\.

Caso contrário, esta etapa não será executada\.

Nesta etapa será realizada a mesma pesquisa dos produtos aquiridos no mercado nacional no mês de referência do cálculo \(mês apurado na Etapa 3\)\.

Serão processados todos os meses anteriores até o limite parametrizado no parâmetro “*No\. de meses anteriores p/pesquisa das aquisições nacionais \(apenas na implantação do módulo\)*”\.

Será processado um mês de cada vez, e no processamento de cada mês a regra básica é a seguinte:

NÃO CONSIDERAR OS PRODUTOS JÁ REGISTRADOS NOS MESES SUBSEQUENTES, ATÉ O MÊS DE REFERÊNCIA\.

A gravação dos dados na tabela será feita da mesma forma descrita na Etapa 1, sendo que no campo “Período”  será sempre gravado o mês/ano das notas processadas para identificação do produto adquirido no mercado nacional\.

    

= = = = 

 	

