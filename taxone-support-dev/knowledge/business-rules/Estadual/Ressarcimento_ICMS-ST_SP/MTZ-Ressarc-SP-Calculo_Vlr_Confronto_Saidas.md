# MTZ-Ressarc-SP-Calculo_Vlr_Confronto_Saidas

- **Fonte:** MTZ-Ressarc-SP-Calculo_Vlr_Confronto_Saidas.docx
- **Modificado:** 2024-01-04
- **Tamanho:** 119 KB

---

THOMSON REUTERS

Módulo Ressarcimento e Complemento de ICMS\-ST – SP 

\(Portaria CAT 42/2018\) 

Cálculo do Valor de Confronto das Saídas

__Localização__: Menu Estadual, módulo Ressarcimento e Complemento de ICMS\-ST – SP, menu Geração à Geração dos Movimentos

Este processo é realizado após a geração dos movimentos na tabela EST\_ST\_SP\_NOTA\_ECF, sempre que o parâmetro “*Opção de processamento*” da tela da geração dos movimentos for = 2 ou 3\.

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS28382__

Cálculo do Valor de Confronto

Criação do cálculo do Valor de Confronto

19/06/2019 

\(criação do documento\)

__MFS28384__

Cálculo do Valor de Confronto

Inclusão do cálculo do Valor de Confronto das devoluções de saída

16/07/2019

__MFS42663__

Alteração do parâmetro “*Pesquisar as últimas entradas até*”

Alteração do parâmetro “*Pesquisar as últimas entradas até*” de lista para data\.

29/09/2020

__MFS48348__

Cálculo do Valor do Confronto das Devoluções para considerar situação onde as notas de saídas referenciadas não possuem Ficha 3\.

Cliente possui uma situação onde as notas de devolução referenciam notas de saídas de períodos anteriores à vigência da CAT42/2018\. Logo essas notas de saídas não constam na ficha3, e o Valor do Confronto das notas de devolução fica zerado, pois seu cálculo faz uso do campo 21 da Ficha 3 das notas de saídas referenciadas pela devolução\.

Essa situação já era prevista, e no manual do roteiro existe a seguinte orientação:

__Observação sobre devolução de saídas de períodos antigos__: Se a saída que originou a devolução for de um período antigo, em que o usuário ainda não utilizava o módulo, o seu valor de confronto não poderá ser recuperado da Ficha 3, e consequentemente, o valor de confronto da nota de devolução não será calculado\. Nesse caso, será gerada uma mensagem de erro no log\. Uma alternativa para resolver esta situação seria:

1 \- Lançar o valor de confronto da nota de saída no campo “107\-Valor Carga Tributária Origem” da SAFX08;

2 \- Executar a geração dos movimentos para o período da nota de saída alterada\. Nesse caso, a geração deve ser executada com o parâmetro do cálculo do Valor de Confronto desmarcado, para que o valor de confronto desta saída seja o valor lançado no campo 107 da SAFX08\. Com este procedimento, esta nota de saída passará a constar na tabela da Ficha 3, apesar de se tratar de um período antigo, em que o módulo ainda não era utilizado;

2 \- Reexecutar o cálculo do valor de confronto do período atual, para que o valor de confronto da devolução em questão possa ser gerado;

Esse procedimento é custoso pro cliente\. Por isso estamos realizando uma alteração no Cálculo do Valor do Confronto, para considerar o valor do confronto carregado no campo 107 da X08 da nota de saída referenciada pela devolução, caso não encontre ficha 3 dessa nota\. Isso elimina a necessidade do cliente reprocessar períodos anteriores\.

03/12/2020

__MFS67469__

Atendimento ao tópico 3\.3\.6\.1\.3

Atendimento ao tópico 3\.3\.6\.1\.3 do Manual do Sistema, para Enquadramento Legal = 1 – Saída a Consumidor Final\.

12/08/2021

__MFS525055__

Andréa Rocha

Alteração da regra de recuperação das notas fiscais para passar a verificar a parametrização de CFOP/Natureza por estabelecimento, caso a parametrização tenha sido cadastrada\.

24/04/2023

__MFS591070__

Liliane Assaf

Tratamento das Incorporações de Empresas/Estabelecimentos no cálculo do valor de confronto das saídas\.

21/12/2023

Sumário

[1\.	Parâmetros da Tela	2](#_Toc12375454)

[2\.	Recuperação dos Dados e Processamento	3](#_Toc12375455)

[3\.	Cálculo do Valor de Confronto na Saída	5](#_Toc12375456)

[4\.	Cálculo do Valor de Confronto na Devolução de Saída	13](#_Toc12375457)

# <a id="_Toc12375454"></a>Parâmetros da Tela 

Este processo é chamado do menu “__Geração dos Movimentos__”, através do parâmetro de tela “*Opção de processamento*”, da seguinte forma:

__Opção de Processamento__

__Processos a serem realizados__

Geração dos Movimentos

Nesse caso será realizada apenas a geração dos movimentos para a Ficha 3, que consiste na carga dos documentos para a tabela específica do módulo \(EST\_ST\_SP\_NOTA\_ECF\)\.

Geração dos Movimentos 

__\+ __

Cálculo do Valor de Confronto \(col 21 da Ficha 3\)

Nesse caso será realizada a geração dos movimentos para a Ficha 3, e ao final deste processo, será realizado o processo de cálculo do Valor de Confronto\.

Cálculo do Valor de Confronto \(col 21 da Ficha 3\)

Nesse caso será realizada apenas o processo de cálculo do Valor de Confronto dos movimentos de saída \(Fato Gerador não Realizado e Saída p/Outros Estados\)\. 

Para realizar esta opção isoladamente é pré\-requisito que os movimentos do período solicitado já tenham sido gerados\.

Para verificar os parâmetros da tela, e as regras da geração dos movimentos, consultar o seguinte documento:__ __

__                                                                                          MTZ\-Ressarc\-SP\-Geracao\_Movimentos\_Ficha3__

__\[MFS525055\]__ Inclusão da utilização da parametrização de CFOP/Natureza por Estabelecimento quando estiver cadastrada para o estabelecimento da geração

# <a id="_Toc350763252"></a><a id="_Toc12375455"></a>Recuperação dos Dados e Processamento

   

__Origem dos dados__: \- Tabela dos Movimentos da Ficha 3 \(__EST\_ST\_SP\_NOTA\_ECF__\);

                                  \- Parametrização de CFOP / Natureza de Operação \(Por UF ou por Estabelecimento\);

                                  \- SAFX07 / SAFX08 \- Tabelas dos Documentos Fiscais;

                                  \- SAFX192 – Documentos Referenciados;

O objetivo desta geração é filtrar os movimentos de saídas, e devoluções de saída, dos tipos “Fato Gerador não Realizado” e “Saídas p/ Outros Estados” na <a id="OLE_LINK27"></a>tabela dos movimentos \(__EST\_ST\_SP\_NOTA\_ECF__\), calcular o valor de confronto da saída ou devolução, e atualizar o valor calculado na tabela\. 

__\[MFS67469\] Atendimento ao tópico 3\.3\.6\.1\.3 do Manual do Sistema, p/ Enquadramento Legal 1:__

Com o atendimento ao tópico 3\.3\.6\.1\.3, o valor do confronto passa a ser calculado para o tipo “Saída a Consumidor ou usuário final”, sendo que o valor calculado é armazenado num campo separado \(Valor Confronto – ICMS Efetivo Entrada Origem \(VLR\_CONF\_ENT\_ORIG\)\), já que a coluna 21 da Ficha 3 se mantém não preenchida para esse tipo de enquadramento legal \(1\)\.

Ou seja, somente para os tipos “Fato Gerador não Realizado” e “Saídas p/ Outros Estados” o Valor Confronto – ICMS Efetivo Entrada calculado por essa rotina é demonstrado na coluna 21 da ficha 3\.

No caso da saída, o valor de confronto é calculado com base nas últimas entradas do produto, e no caso das devoluções, o cálculo é feito com base nas operações de venda que originaram a devolução\.

__Resumo do Processo:__

Para cada item recuperado na tabela dos movimentos, seja saída ou devolução de saída, do tipo “Fato Gerador não Realizado”, “Saídas p/ Outros Estados” e “Saída a Consumidor ou usuário final” \[__MFS67469\]__, serão executados os seguintes procedimentos:

- No caso das saídas, pesquisar as últimas entradas do produto\. Estas entradas poderão ser informadas pelo usuário \(via SAFX192\), ou não\. Caso sim, serão utilizadas apenas as entradas informadas na SAFX192, caso não, será feita a pesquisa das últimas entradas na SAFX07/SAFX08, até atingir a quantidade da saída;
- No caso das devoluções de saída, pesquisar as notas da saída que originaram a devolução do produto\. Neste caso, o usuário deverá, obrigatoriamente, informar estas notas de saída na SAFX192;
- Calcular o valor de confronto da saída ou devolução de saída;
- Para os tipos “Fato Gerador não Realizado”, “Saídas p/ Outros Estados” gravar o resultado apurado na coluna “__Valor Confronto \- ICMS Efetivo Entrada \(VLR\_CONF\_ENT\)”__ da tabela do movimento \(EST\_ST\_SP\_NOTA\_ECF\)\. Este valor corresponde à coluna 21 da Ficha 3;
- \[__MFS67469\] __Para o tipo “Saída a Consumidor ou usuário final” gravar o resultado apurado na coluna “__Valor Confronto \- ICMS Efetivo Entrada Origem \(VLR\_CONF\_ENT\_ORIG\)”__ da tabela do movimento \(EST\_ST\_SP\_NOTA\_ECF\)\. Este valor __não__ será demonstrado na coluna 21 da Ficha 3;
- Gravar numa tabela os dados do cálculo realizado, informando as notas fiscais envolvidas e o resultado final;

A seguir serão descritas as regras que detalham os passos descritos acima\.

 

__Critérios da recuperação das saídas e devoluções na tabela dos movimentos \(EST\_ST\_SP\_NOTA\_ECF\): __

- Empresa – código da empresa do login;
- Estabelecimento – código do estabelecimento selecionado para geração;

*             \(Observar que no caso de geração por I\.E\.U\. \(parâmetro “Geração por Inscrição Estadual Única” = marcado\), os movimentos de todos os*

*              Estabelecimentos envolvidos na centralização, estarão gravados na tabela EST\_ST\_SP\_NOTA\_ECF já em nome do centralizador\)*

- Data Fiscal – data enquadrada no período informado em tela;

             \[__MFS67469\]__

- Código de Enquadramento = “1” \(“Saída a Consumidor ou usuário final”\) ou “__2__” \(Fato Gerador não Realizado\) ou “__4__” \(Saída p/ Outros Estados\);

Para executar este processo é pré\-requisito que os movimentos do período já tenham sido gerados\.  Por isso, caso não retorne nenhum movimento nas condições acima, será gravada a seguinte mensagem no log da geração:

*“Cálculo do valor de confronto não realizado para o Estabelecimento, pois não existem movimentos de saída ou devolução \(Cód\. Enquadramento = 2 ou 4\) gerados para o período”*

O log deve exibir a identificação do estabelecimento em questão para a conferência do usuário\. 

__Procedimento a ser realizado para cada item recuperado na tabela dos movimentos \(EST\_ST\_SP\_NOTA\_ECF\)__:

As regras do cálculo do valor de confronto são diferentes dependendo do tipo de item \(saída ou devolução de saída\)\. Por isso, os procedimentos a serem realizados foram definidos separadamente, da seguinte forma:

<a id="OLE_LINK28"></a>

- __Se for um movimento de saída__ \(Movimento E/S\) = “9”

<a id="OLE_LINK31"></a>             Será executado o procedimento descrito no item “__3\-Cálculo do Valor de Confronto na Saída__”;

- __Se for um movimento de devolução de saída__ \(Movimento E/S\) <> “9”

             Será executado o procedimento descrito no item “__4\-Cálculo do Valor de Confronto na Devolução de Saída__”;

	 

# <a id="_Toc12375456"></a>Cálculo do Valor de Confronto na Saída

 

O cálculo do valor de confronto na saída, consiste em pesquisar as últimas entradas do produto, até atingir a quantidade da saída, <a id="OLE_LINK26"></a>e calcular a média ponderada do valor do ICMS de todas as entradas identificadas\.

O usuário poderá *opcionalmente*, informar as notas de entrada a serem utilizadas no cálculo\. Este procedimento é feito via SAFX192 \(opção “Documentos Referenciados” da tela de manutenção dos itens de mercadoria\), e poderá ser feito apenas para determinadas notas ou todas, conforme a escolha do usuário\.

Quando as entradas não forem referenciadas na SAFX192, a rotina do cálculo fará a busca\.

__Recuperação das últimas entradas do produto:__

Será verificado na SAFX192 a existência de notas referenciadas para o item da saída em questão\. 

A SAFX192 é uma tabela “filha” da SAFX08, e a referência é feita da seguinte forma:

\- Os campos 1 ao 15 identificam o item da de saída;

\- O campo “16\-Tipo de Referência” indica o tipo de associação\. Nessa pesquisa, serão consideradas apenas as linhas com tipo = “__2__”;

\- Os campos 17 ao 23 identificam o item da nota de entrada referenciado;

__Se__ existirem itens referenciados na SAFX192,      

     Nesse caso a média das entradas será calculada utilizando as notas referenciadas indicadas na SAFX192;

__Senão __

     Nesse caso será feita a recuperação das últimas entradas do produto na SAFX07/SAFX08, __da nota mais recente para as mais antigas__,

     considerando os critérios a seguir:

- Notas da mesma Empresa <a id="OLE_LINK35"></a><a id="OLE_LINK39"></a>da saída em questão;
- <a id="OLE_LINK34"></a>Notas do mesmo Estabelecimento da saída em questão, se “*Geração por Inscrição Estadual Única*” = “__N__” \(parâmetro da tela da geração\), __ou__, notas do mesmo Estabelecimento da saída em questão, e também dos estabelecimentos centralizados, se “*Geração por Inscrição Estadual Única*” = “__S__”\. Lembrando que, para as empresas que trabalham com I\.E\.U\., todos os movimentos na EST\_ST\_SP\_NOTA\_ECF estão sempre em nome do estabelecimento centralizador; 

  

- Apenas notas de entrada \(MOVTO\_E\_S <> 9\);
- Apenas notas que não sejam devolução \(somente notas com NORM\_DEV = 1\);
- Apenas notas com itens na SAFX08;
- O CFOP ou CFOP/Natureza do item deve estar parametrizado \(menu “*Parâmetros à CFOP/Natureza para a Ficha 3*”\) para a operação “Entradas \(e Devoluções\)”\. Primeiro deve\-se verificar se existe parametrização cadastrada na opção Por Estabelecimento, para o estabelecimento da geração \(tratar I\.E\.U\.\)\.  Se houver parametrização, deve\-se considerar os CFOP/Naturezas cadastrados na parametrização por Estabelecimento \(Parâmetros 🡪 CFOP/Natureza para a Ficha 3 🡪 CFOP \(Por Estabelecimento\) ou Natureza de Operação \(Por Estabelecimento\)\)\.  Se não houver parametrização cadastrada para o estabelecimento, deve\-se utilizar os CFOP/Naturezas cadastrados por UF \(Parâmetros 🡪 CFOP/Natureza para a Ficha 3 🡪 CFOP ou Natureza de Operação\)\.
- O produto do item deve ser o mesmo produto da saída em questão, __ou__, um dos produtos associados à ele \(associação de produtos do menu “Parâmetros > Produtos > Por Código”\)\. Lembrando que para as empresas que trabalham com associação de produtos, todos os movimentos na EST\_ST\_SP\_NOTA\_ECF estão sempre em nome do produto principal;

  

- Serão recuperadas as notas de entrada suficientes para cobrir a quantidade da saída <a id="OLE_LINK45"></a><a id="OLE_LINK46"></a><a id="OLE_LINK47"></a>*\(ver item abaixo que detalha sobre como totalizar a quantidade das entradas\)*__;__
- A pesquisa das notas será feita até atingir a quantidade da saída, __ou__, até que a Data Limite informada para a pesquisa seja atingida\. Este limite é identificado através do parâmetro “*Pesquisar as últimas entradas até*” da tela da geração\. Isso significa que, quando for o caso de utilizar notas de meses anteriores, deve\-se considerar apenas as notas com a DATA\_FISCAL que não exceda a data limite estabelecida no parâmetro;

           \[__MFS42663\]__ O parâmetro “*Pesquisar as últimas entradas até*” da tela da geração, que antes funcionava com um campo lista,

          apresentando as opções \[1 mês, 2 meses, 3 meses \.\.\.\.\. 18 meses\], foi alterado para funcionar com um campo data\. Assim, o

          usuário passou a informar direto uma data limite, ao invés de informar um número de meses\.

<a id="OLE_LINK49"></a><a id="OLE_LINK50"></a><a id="OLE_LINK51"></a><a id="OLE_LINK52"></a><a id="OLE_LINK53"></a><a id="OLE_LINK54"></a>           Exemplo :

\-Período da geração: 01/01/2019 a 31/01/2019;

* \(Lembrando que as datas inicial e final do período da geração informadas em tela são sempre do mesmo mês\) *           

\- Parâmetro “Pesquisar as últimas entradas até” = 01/10/2018;

\- Neste caso, a pesquisa só será feita nos meses de Jan/2019, Dez/2018, Nov/2018 e Out/2018\. Notas de meses anteriores à

   Out/2018 não serão consideradas\.

- __\[MFS591070\] Tratamento das Incorporações de Empresas/Estabelecimentos:__

Se o total da quantidade das notas de entrada recuperadas da SAFX07/SAFX08 com os critérios acima, não for suficiente para cobrir a quantidade da saída em questão, verificar se o parâmetro para buscar as notas nas empresas incorporadas está marcado na tela da geração\. 

     Se o parâmetro “Considerar as notas fiscais da empresa incorporada” estiver marcado:

           Considerar as notas das empresas/estabelecimentos cadastradas como incorporadas na tela de Relação de Empresa 

           Incorporadora x Incorporada\*\* para a empresa/estabelecimento da geração \(incorporadora\), para recuperar as notas de  

           entrada afim de atingir a quantidade da saída do produto\.

    Senão

          Considerar somente as notas fiscais da empresa e estabelecimento selecionados para a geração se “*Geração por Inscrição Estadual Única*” = “__N__” 

          \(parâmetro da tela da geração\), __ou__ também dos estabelecimentos centralizados, se “*Geração por Inscrição Estadual Única*” = “__S__”\.

\*\* Módulo Parâmetros, item Preliminares 🡪 Relação de Empresa Incorporadora x Incorporada

OBS: Não estamos tratando o cenário de Cadastros de Produtos distintos entre as empresas incorporadora e incorporadas\. Ou seja, os produtos entre essas empresas devem ser identificados pelo mesmo grupo, indicador e código do produto\.  A Lasa que foi o cliente que abriu essa demanda, poissui cadastros iguais entre as empresas participantes da incorporação\. Se os cadastros fossem diferentes, teríamos que criar uma espécie de dexpara entre os cadastros dos produtos da empresa incorporadora para com os das empresas incorporadas\.

Caso contrário, será gravada a seguinte mensagem no log, e o cálculo do Valor de Confronto não será realizado para esta saída:

__Mensagem de aviso quando não identificar entradas p/uma determinada saída:__

Se nenhuma entrada for identificada para a nota de saída em questão, seja entrada referenciada na SAFX192, ou recuperada da SAFX08, o cálculo do Valor de Confronto *não* será realizado para esta saída, e no log de erro será gravada a seguinte mensagem: *“O cálculo do VC não foi realizado para este item de saída, pois não foram encontradas notas de entrada do produto\. Consultar os detalhes e pré\-requisitos do cálculo no help e roteiro operacional do módulo”\.*

* *

O log deve exibir as informações de identificação do item da saída \(ao menos o número, série, data e item\) para conferência do usuário:

__Como totalizar a quantidade das notas de entrada e comparar com a QTD da saída em questão:__

A quantidade das notas de entrada, quando necessário, serão convertidas para a unidade de medida do cadastro do produto \(SAFX2013\)\. 

*Observação importante: O cadastro a ser considerado é sempre o cadastro do produto da nota de saída\. Isso porque quando a entrada for de um produto associado, o produto será diferente do produto da nota de saída, e neste caso, para efeito de conversão de medida, deve\-se considerar sempre a unidade de medida do produto principal\. Assim, a comparação entre as unidades de medida, será feita entre a unidade da nota de entrada e a unidade de cadastro do produto da saída \(produto “principal” da associação\)\.*

Este procedimento é feito antes de utilizar a informação do campo, já que todas as quantidades devem estar na mesma unidade de medida\. 

*\(Lembrando que a unidade da saída recuperada da EST\_ST\_SP\_NOTA\_ECF já estará convertida, quando for o caso\)*

 

__Se__ a unidade de medida do item da entrada = unidade de medida do cadastro do produto: *\(ver OBS acima sobre produtos associados\)*

      \(campo “25\-Unidade de Medida” da SAFX08 = campo “14\-Código de Medida” da SAFX2013\)

       Nesse caso, não é necessário efetuar a conversão;

__Senão __

     __Se__ existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\)

         Nesse caso, será utilizada a informação da quantidade já convertida do campo “137\-Quantidade Convertida”;

     __Senão         __

         Nesse caso a quantidade da entrada item \(SAFX08\) será convertida para a unidade de medida do cadastro do produto;

__Para efetuar a conversão de medida__:

A conversão é feita conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da mesma forma que é feita na rotina de geração dos movimentos:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o cálculo do Valor de Confronto *não* será realizado para esta saída, e no log de erro será gravada a seguinte mensagem: *“O cálculo do VC não foi realizado para este item de saída, pois não foi possível converter a quantidade de nota de entrada para a medida do cadastro do produto \(fator de conversão de XXX para XXX não identificado\)\. *

*\(o primeiro “XXX” é a unidade do item da entrada, e o segundo “XXX”, a unidade do cadastro do produto\)\.*

O log deve exibir as seguintes informações para conferência do usuário:

\- Identificação do item da saída \(ao menos o número, série, data e item\);

\- Identificação do item da entrada \(ao menos o número, série, data e item\);

<a id="OLE_LINK41"></a><a id="OLE_LINK42"></a><a id="OLE_LINK43"></a><a id="OLE_LINK44"></a>  

__Crítica da Quantidade das Entradas x QTD da Saída:__

__Se__ existirem itens referenciados na SAFX192,      

     Nesse caso, o total da quantidade das notas de entrada referenciadas na SAFX192 deve ser >= a quantidade da saída em questão\.    

     Caso contrário, será gravada a mensagem abaixo no log, e o cálculo do Valor de Confronto *não* será realizado para esta saída:

    *“O cálculo do VC não foi realizado para este item de saída, pois as entradas referenciadas na SAFX192 não atingem a quantidade da*

*     saída” *\(o log deve exibir a identificação do item da saída para conferência do usuário\)

__Senão __

     Nesse caso, o total da quantidade das notas de entrada recuperadas da SAFX07/SAFX08 deve ser >= a quantidade da saída em

     questão\. Caso contrário, será gravada a seguinte mensagem no log, e o cálculo do Valor de Confronto *não* será realizado para esta

     saída: *“O cálculo do VC não foi realizado para este item de saída, pois as entradas recuperadas da SAFX07/SAFX08 não foram*

*    suficientes para cobrir a quantidade da saída” *\(o log deve exibir a identificação do item da saída para conferência do usuário\)\. 

     Este problema poderá ocorrer quando a pesquisa das entradas na SAFX07/SAFX08 for realizada até a data limite 

     especificada, mas a quantidade total das notas recuperadas não for suficiente para cobrir a quantidade da saída em questão;

*\(Conforme já citado acima, para totalizar a quantidade das entradas, será utilizada a informação da quantidade já convertida, quando for o caso\) *

__Cálculo do Valor de Confronto com base nas entradas a serem utilizadas:__

As entradas recuperadas para cada saída serão processadas em ordem de data, __sempre da mais recente para mais antiga__\.

Para cada entrada a ser processada será calculado um valor de ICMS, conforme a regra abaixo\. 

- Se quantidade da saída __=__ quantidade da entrada, considerar __*Valor ICMS*__ = Valor ICMS da entrada \(vide “__Considerações__”\);
- Se quantidade da saída __>__ quantidade da entrada, considerar __*Valor ICMS*__ = Valor ICMS da entrada \(vide__ __“__Considerações__”\);
- Se quantidade da saída __<__ quantidade da entrada, calcular o valor do ICMS proporcional à quantidade restante para cobrir a saída, da seguinte forma: 

                                          \[ __*Valor ICMS*__ = \(Valor ICMS da entrada \(\*\*\*\) / quantidade da entrada\) \* quantidade da saída \]

Após o processamento de todas as entradas, o resultado do Valor de Confronto da saída será o total dos valores calculados \(“__*Valor ICMS*__”\) de todas as entradas\.

__Considerações:__

- A “*quantidade da entrada*” utilizada no cálculo é a quantidade da nota de entrada já convertida \(conforme a regra de conversão já descrita acima\);

  

- O “*Valor ICMS da entrada*” utilizado no cálculo será o valor do ICMS do item \(campo “43\-Valor ICMS”, se preenchido, ou campo “80\-ICMS não Escriturado”, se preenchido, ou campo "225\-Valor ICMS Não Destacado"\);
- A “*quantidade da saída*” utilizada no cálculo é a quantidade que consta no movimento da saída \(EST\_ST\_SP\_NOTA\_ECF\)\. Ao processar a primeira nota de entrada, é utilizada a quantidade integral da saída\. Para as próximas entradas, a “quantidade da saída” será a quantidade integral da saída, menos a quantidade das entradas processadas anteriormente \(ver o exemplo abaixo\);
- O cálculo será encerrado assim que a quantidade integral da saída for atingida na última entrada processada \(quando as entradas são recuperadas da SAFX07/SAFX08, a pesquisa é encerrada quando isso acontece, mas no caso das entradas referenciadas na SAFX192 isso poderia acontecer, ou seja, podem existir entradas a mais do que o necessário\);

Exemplo:

O exemplo a seguir é básico, mostra apenas o conceito do cálculo descrito acima\. 

Para exemplos mais completos, com conversão de medida, produtos associados, etc\., consultar a planilha “*Exemplo\_Calculo\_Valor\_Confronto*” \(ver abas “*Vlr Confronto da Saída \(II\)*” e “*Vlr Confronto da Saída \(III\)*”\)\.

__Notas de Entrada__:

__   Data               NF           QTD       Valor        ICMS__

25/04/2019      __450__       10,0000      50,00        6,00

08/05/2019      __511__         2,0000      13,50        1,62

__Notas de Saída__:

__   Data               NF           QTD       Valor        ICMS       Vlr Confronto Calculado__

05/05/2019      __001__         5,0000      30,00         3,60                     __3,00__

10/05/2019      __002__         5,0000      40,00         4,80                     __3,42__

__Cálculo do Valor de Confronto da Nota 001 \(de 05/05\):__

Nota de Entrada: __450__ \(de 25/04\) 

A Quantidade da saída \(5,0000\) é __<__ Quantidade da entrada \(10,0000\), logo, __*Valor ICMS*__ = \(6,00 / 10,0000\) \* 5,0000 = __3,00__

__Cálculo do Valor de Confronto da Nota 002 \(de 10/05\):__

  

Nota de entrada: __511__ \(de 08/05\)

A Quantidade da saída \(5,0000\) é __>__ Quantidade da entrada \(2,0000\), logo, __*Valor ICMS*__ = 1,62

Saldo quantidade da saída a ser considerada no cálculo da próxima entrada: 5,0000 – 2,0000 = __3,0000__

Nota de entrada: __450 __\(de 25/04\)

A Quantidade da saída \(__3,0000__\) é __<__ Quantidade da entrada \(10,0000\), logo, __*Valor ICMS*__ = \(6,00 / 10,0000\) \* __3,0000__ = 1,80

                                                                                                                  Valor de Confronto da__ Nota 002__ = 1,62 \+ 1,80 = __3,42__

__Gravação do Valor de Confronto calculado na Tabela dos Movimentos:__

Para os movimentos de saída/devolução dos tipos “__2__” \(Fato Gerador não Realizado\) e “__4__” \(Saída p/ Outros Estados\):

O resultado obtido será atualizado na coluna “__Valor Confronto \- ICMS Efetivo Entrada \(VLR\_CONF\_ENT\)”__ da tabela dos movimentos da Ficha 3\. Este valor corresponde à coluna “*21\-ICMS Efetivo da Entrada, nas demais Hipóteses*” da Ficha 3\.

__\[MFS67469\] Atendimento ao tópico 3\.3\.6\.1\.3 do Manual do Sistema, p/ Enquadramento Legal 1:__

Para o tipo “Saída a Consumidor ou usuário final”:

O resultado obtido será atualizado na coluna “__Valor Confronto \- ICMS Efetivo Entrada Origem \(VLR\_CONF\_ENT\_ORIG\)”__ da tabela dos movimentos da Ficha 3\. 

Este valor não é demonstrado na Ficha 3\!

Quando se tratar de um movimento de saída/devolução para outros estados \(campo “Código Enquadramento” da tabela do movimento = “4”\), o valor atualizado no campo “Valor Confronto – ICMS Efetivo Entrada”, será gravado também no campo “__ICMS – Crédito Op\. Própria__” da tabela\.

Todas as notas de entrada utilizadas no cálculo do valor de confronto para um determinado item de saída, serão gravadas numa tabela auxiliar\. As regras de gravação destas informações estão descritas no item a seguir \(item “*Gravação dos Dados utilizados no Cálculo*”\)\. 

__Gravação dos Dados utilizados no Cálculo do VC das Saídas:__

<a id="_Hlk508706613"></a>Cada nota de entrada utilizada no cálculo do valor de confronto será gravada numa tabela auxiliar\. Estas entradas serão vinculadas à nota da saída em questão\. 

Estas informações serão utilizadas posteriormente num relatório de conferência, para que o usuário possa conferir os cálculos efetuados para chegar ao resultado final\.

*\(ver layout do relatório na planilha “Layout\_Relatorio\_Conferencia\_Valor\_Confronto”, aba “Conferencia VC – Saidas”\)*

 

Informações a serem armazenadas:

Sobre a nomenclatura dos campos descrita a seguir: No caso do cálculo do Valor de Confronto das saídas, a nota “principal” é a nota de saída, e as notas de referência são as notas de entrada pesquisadas ou referenciadas na SAFX192\. 

__\*\*\*__

__Código da empresa__

                                       __Informações de identificação da nota de saída__

 

                                                \(conforme a EST\_ST\_SP\_NOTA\_ECF\)

__\*\*\*__

__Código do estabelecimento__

__\*\*\*__

__Período \(mês e ano\)__

__\*\*\*__

__Produto__

__\*\*\*__

__Data Fiscal __

__\*\*\*__

__Tipo do Documento__

__\*\*\*__

__Série do Documento__

__\*\*\*__

__Número do Documento__

__\*\*\*__

__Pessoa Fis/Jur__

__\*\*\*__

__Número do Item__

__\*\*\*__

__Movimento E/S__

__\*\*\*__

__Número do Documento __<a id="OLE_LINK10"></a><a id="OLE_LINK11"></a>__da NF de referência__

                                      __Informações de identificação da nota de entrada__

 

                                                

__\*\*\*__

__Série do Documento da NF de referência__

__\*\*\*__

__Subsérie do Documento da NF de referência__

__\*\*\*__

__Data Fiscal da NF de referência__

__\*\*\*__

__Tipo do Documento da NF de referência __

__\*\*\*__

__Pessoa Fis/Jur da NF de referência__

__\*\*\*__

__Número do Item da NF de referência__

Quantidade da nota principal

Quantidade da nota de saída \(conforme a EST\_ST\_SP\_NOTA\_ECF\)

Código de enquadramento da nota principal

Código de enquadramento legal da nota de saída \(conforme a EST\_ST\_SP\_NOTA\_ECF\)

Produto da NF de referência 

Identificação do produto da nota de entrada

\(será sempre o mesmo da nota de saída, exceto quando se tratar de um produto associado\)

Código da Empresa de Origem da NF de referência

__\[MFS591070\] Tratamento das Incorporações de Empresas/Estabelecimentos__

Empresa da nota de entrada

\(será sempre o mesmo da nota de saída, exceto quando se tratar de Incorporação\)

Código do Estabelecimento de Origem da NF de referência

Estabelecimento da nota de entrada

\(será sempre o mesmo da nota de saída, exceto quando se tratar de geração por I\.E\.U\. ou Incorporação\)

Quantidade da NF de referência \(quantidade original\)

Quantidade original da entrada \(sem conversão\)

Quantidade convertida da NF de referência 

Quantidade da entrada convertida\. 

Quando não houver necessidade de conversão, será gravada a quantidade original da entrada \(mesmo conteúdo do campo anterior\)\.

Valor ICMS da NF de referência

Valor ICMS da Entrada 

Será gravado o valor do ICMS utilizado no cálculo, ou seja, campo “43\-Valor ICMS”, se preenchido, ou campo “80\-ICMS não Escriturado”, se preenchido, ou campo "225\-Valor ICMS Não Destacado"\.

Quantidade utilizada da NF de referência

Quantidade da entrada utilizada para “cobrir” a saída  

Valor Médio Calculado

Valor Médio do ICMS calculado para a nota de entrada \(conforme descrito no exemplo\)

Valor de Confronto da nota de referência

*Este campo da tabela do relatório é preenchido apenas no cálculo VC das devoluções \(conforme item 4\)*

Quantidade Devolvida da NF de referência

*Este campo da tabela do relatório é preenchido apenas no cálculo VC das devoluções \(conforme item 4\)*

  


# <a id="_Toc12375457"></a>Cálculo do Valor de Confronto na Devolução de Saída

O cálculo do valor de confronto nas devoluções, consiste em identificar a\(s\) nota\(s\) de saída que originaram a devolução, e calcular o valor de confronto da devolução com base no valor de confronto gerado nas operações originais\.

Para o cálculo do valor de confronto das devoluções, é __obrigatório__ que sejam informadas na SAFX192 __\(\*\)__ as notas de saída que originaram a devolução\.

__\(\*\)__* Opção “Documentos Referenciados” da tela de manutenção dos itens de mercadoria\)*

No caso das devoluções em que não existir a\(s\) saída\(s\) referenciadas na SAFX192, o valor de confronto não será calculado, e será gerada mensagem de erro no log \(conforme descrito a seguir\)\.

__Recuperação das saídas referenciadas na SAFX192:__

A SAFX192 é uma tabela “filha” da SAFX08, e a referência é feita da seguinte forma:

\- Os campos 1 ao 15 identificam o item da nota de devolução em questão;

\- O campo “16\-Tipo de Referência” indica o tipo de associação\. Nessa pesquisa, serão consideradas apenas as linhas com tipo = “__1__”;

\- Os campos 17 ao 23 identificam o item da nota de saída referenciado;

Caso *não* existam itens referenciados na SAFX192 para a nota de devolução, o valor de confronto *não* será calculado, e no log será gravada a seguinte mensagem: 

*         “O cálculo do VC não foi realizado para este item de devolução, pois não existe a referência das saídas originais na SAFX192”*

                                \(o log deve exibir a identificação do item da devolução para conferência do usuário\)

__Sobre a SAFX192__:

Na SAX192, ao informar as saídas que originaram a devolução, o usuário também informa, obrigatoriamente, a quantidade devolvida que corresponde a cada nota de saída \(campo 24\-Quantidade da Devolução\)\. Ou seja, ele informa o quanto da quantidade da nota de devolução, que é originada desta saída\. Este “quanto” pode ser a quantidade integral da devolução, ou apenas parte dela\. Lembrando que, de acordo com as orientações do manual de layout, esta quantidade deve ser informada na mesma unidade de medida da nota da devolução\.  

__Crítica da Quantidade da nota de devolução x Quantidades devolvidas informadas na SAFX192:__

O total da quantidade devolvida de todas as saídas referenciadas na SAFX192, deve ser = quantidade da nota de devolução\. 

Esta crítica é realizada na manutenção da SAFX192\. No entanto, como os dados também podem ser importados \(e nesse caso não há como fazer esta validação\), será feita a verificação antes de efetuar o cálculo do confronto\.

__Se__ Quantidade da Nota de Devolução \(Qtd da SAFX08\) <> Total das Quantidades Devolvidas informadas na SAFX192:

     Nesse caso, será gravada a mensagem abaixo no log, e o cálculo do valor de confronto *não* será realizado para esta devolução:

    *“O cálculo do VC não foi realizado para este item de devolução, pois o total das quantidades devolvidas informadas na SAFX192 difere da*

*     quantidade da nota de devolução” *\(o log deve exibir a identificação do item da nota de devolução para conferência do usuário\)

Observação importante: A comparação entre a quantidade da nota de devolução e o total das quantidades devolvidas \(SAFX192\) pode ser feita de duas formas:

\- Comparando a quantidade da SAFX08 da nota de devolução __x__ total das quantidades devolvidas informadas na SAFX192;

  __Ou__

\- Comparando a quantidade da EST\_ST\_SP\_NOTA\_ECF da nota de devolução __x__ total das quantidades devolvidas informadas na SAFX192, sendo

   que nesse caso, é necessário converter as quantidades da SAFX192, quando necessário;

*\(ver exemplo na planilha anexa, aba “Vlr Confronto na Devolução \- II”\)*

 

__Cálculo do Valor de Confronto com base nas saídas referenciadas na SAFX192:__

Para cada saída referenciada na SAFX192, será recuperado o seu valor de confronto da Ficha 3, ou do campo 107 \- Valor Carga Tributária Origem ICMS da SAFX08, caso não encontre na Ficha 3, e em seguida calcular o valor de confronto proporcional, conforme descrito a seguir:

- Será recuperada a informação do Valor de Confronto que foi lançado na Ficha 3 \(coluna 21\), pois o cálculo do valor de confronto da devolução é feito com base no valor de confronto das notas originais da saída\. Este valor será recuperado do registro da saída na Tabela da Ficha3 \(EST\_ST\_SP\_NOTA\_ECF\), considerando o período da nota, pois as saídas que originam devoluções podem ser saídas do mesmo período, ou de períodos anteriores\. 
- __\[MFS48348\] __Caso o registro da saída *não* seja identificado na Tabela da Ficha, __*ou*__, não exista valor para a coluna 21 \(campo “*Valor Confronto – ICMS Efetivo Entrada* “ da tabela\), então recuperar o Valor do Confronto carregado no campo 107 \- Valor Carga Tributária Origem ICMS da SAFX08 no item da nota de saída\.
- Se o Valor do Confronto da nota de saída não for obtido de nenhuma das origens acima \(campo 21 da Ficha 3 ou campo 107 da SAFX08\), então o valor de confronto da devolução *não* será calculado, e será gravada a seguinte mensagem de erro no log:

*            “O cálculo do VC não foi realizado para este item de devolução, pois existem saídas referenciadas \(SAFX192\) que não constam nem*

*             na Ficha 3, ou, na Ficha 3 não tem o Valor de Confronto da saída \(col 21\), nem estão com o campo 107 \- Valor Carga Tributária *

*            Origem ICMS do item \(SAFX08\) carregado\. Assim, o valor de confronto da operação original não pode ser recuperado\.*

*             Consultar informações do Help e Roteiro Operacional”*

*            \(o log deve exibir a identificação do item da devolução para conferência do usuário\)*

- Cálculo do valor de confronto correspondente à saída:

\- Se a quantidade devolvida que consta na SAFX192 for __=__ quantidade da nota de saída, significa que a devolução desta saída foi integral\.  

  Neste caso, será considerado __*Valor Confronto*__ = Valor Confronto da saída;

           \- Se a quantidade devolvida que consta na SAFX192 for __<__ quantidade da nota de saída, significa que a devolução desta saída foi parcial\.   

              Neste caso, será calculado um valor proporcional à quantidade devolvida, da seguinte forma: calcula o valor unitário do valor de confronto

              que consta na FICHA 3 da nota de saída, e multiplica\-se o resultado pela quantidade devolvida \(SAFX192\):

                                __*Valor Confronto*__ = \(Valor confronto da NF de saída / quantidade da NF de saída\) \* quantidade devolvida \(SAFX192\) 

Considerações sobre as quantidades a serem utilizadas no cálculo: Existem de duas formas de fazer o cálculo descrito acima:

- Utilizar o campo da quantidade devolvida da SAFX192, e para a quantidade da saída, utilizar o campo de quantidade da SAFX08\. Neste caso, não é necessário fazer conversão de medida;
- Utilizar o campo da quantidade devolvida da SAFX192, e para a quantidade da saída, utilizar o campo de quantidade da própria tabela da FICHA 3 \(EST\_ST\_SP\_NOTA\_ECF\), de onde foi recuperado o valor de confronto da saída\. Neste caso, deve\-se  verificar a necessidade de efetuar conversão de medida da quantidade devolvida indicada na SAFX192\. Isso porque todas as quantidades da Ficha 3 são sempre referentes à unidade de medida do cadastro do produto, e podem existir operações com o produto realizadas em outras unidades\.

Independente da forma de cálculo utilizada, o resultado é sempre o mesmo, já que ou se usa as duas quantidades originais \(sem conversão\), ou se usa as duas convertidas\. 

                Exemplos do cálculo:

Ver exemplos do cálculo do VC das devoluções na planilha “__*Exemplo\_Calculo\_Valor\_Confronto*__”\.

Na aba “*Vlr Confronto na Devolução*” tem um exemplo simples, que mostra o conceito do cálculo;

Na aba “*Vlr Confronto na Devolução \(II\)*” tem um exemplo que mostra conversão de medida, onde as operações de saída são realizadas numa unidade de medida diferente da medida do cadastro do produto\. Neste caso, os movimentos são gerados na Ficha 3 com as quantidades convertidas para a unidade de medida do cadastro\. *Este segundo exemplo mostra as duas formas de cálculo* citadas na observação acima sobre as quantidades a serem utilizadas; 

    

Após o processamento de todas as saídas referenciadas na SAFX192, o resultado do Valor de Confronto da devolução será o total dos valores calculados \(“__*Valor Confronto*__”\) de todas as saídas\.

__Gravação do Valor de Confronto calculado na Tabela dos Movimentos:__

Para os movimentos de saída/devolução dos tipos “__2__” \(Fato Gerador não Realizado\) e “__4__” \(Saída p/ Outros Estados\):

O resultado obtido será atualizado na coluna “__Valor Confronto \- ICMS Efetivo Entrada \(VLR\_CONF\_ENT\)”__ da tabela dos movimentos da Ficha 3\. Este valor corresponde à coluna “*21\-ICMS Efetivo da Entrada, nas demais Hipóteses*” da Ficha 3\.

__\[MFS67469\] Atendimento ao tópico 3\.3\.6\.1\.3 do Manual do Sistema, p/ Enquadramento Legal 1:__

Para o tipo “Saída a Consumidor ou usuário final”:

O resultado obtido será atualizado na coluna “__Valor Confronto \- ICMS Efetivo Entrada Origem \(VLR\_CONF\_ENT\_ORIG\)”__ da tabela dos movimentos da Ficha 3\. 

Este valor não é demonstrado na Ficha 3\!

Como se trata de um movimento de devolução de saída, o resultado será gravado com sinal negativo \(assim como é feito na geração dos movimentos\)\.

Quando se tratar de um movimento de saída/devolução para outros estados \(campo “Código Enquadramento” da tabela do movimento = “4”\), o valor atualizado no campo “__Valor Confronto – ICMS Efetivo Entrada__”, será gravado também no campo “__ICMS – Crédito Op\. Própria__” da tabela\.

Todas as notas de saída utilizadas no cálculo do valor de confronto para um determinado item de devolução, serão gravadas numa tabela auxiliar\. As regras de gravação destas informações estão descritas no item a seguir \(item “*Gravação dos Dados utilizados no Cálculo*”\)\. 

__Gravação dos Dados utilizados no Cálculo do VC das devoluções:__

Cada nota de saída utilizada no cálculo do valor de confronto será gravada numa tabela auxiliar\. Estas saídas serão vinculadas à nota da devolução em questão\. 

Estas informações serão utilizadas posteriormente num relatório de conferência, para que o usuário possa conferir os cálculos efetuados para chegar ao resultado final\.

*\(ver layout do relatório na planilha “Layout\_Relatorio\_Conferencia\_Valor\_Confronto”, aba “Conferencia VC  Devoluções”\)*

__Informações a serem armazenadas:__

Sobre a nomenclatura dos campos descrita a seguir: No caso do cálculo do Valor de Confronto das devoluções, a nota “principal” é a nota de devolução, e as notas de referência são as notas de saída referenciada na SAFX192\.

__\*\*\*__

__Código da empresa__

                                       __Informações de identificação da nota de devolução__

 

                                                \(conforme a EST\_ST\_SP\_NOTA\_ECF\)

__\*\*\*__

__Código do estabelecimento__

__\*\*\*__

__Período \(mês e ano\)__

__\*\*\*__

__Produto__

__\*\*\*__

__Data Fiscal __

__\*\*\*__

__Tipo do Documento__

__\*\*\*__

__Série do Documento__

__\*\*\*__

__Número do Documento__

__\*\*\*__

__Pessoa Fis/Jur__

__\*\*\*__

__Número do Item__

__\*\*\*__

__Movimento E/S__

__\*\*\*__

__Número do Documento da NF de referência__

                                      __Informações de identificação da nota de saída__

 

                                                

__\*\*\*__

__Série do Documento da NF de referência__

__\*\*\*__

__Subsérie do Documento da NF de referência__

__\*\*\*__

__Data Fiscal da NF de referência__

__\*\*\*__

__Tipo do Documento da NF de referência __

__\*\*\*__

__Pessoa Fis/Jur da NF de referência__

__\*\*\*__

__Número do Item da NF de referência__

Quantidade da nota principal

Quantidade da nota de devolução \(conforme a EST\_ST\_SP\_NOTA\_ECF\)

Código de enquadramento da nota principal

Código de enquadramento legal da nota de saída \(conforme a EST\_ST\_SP\_NOTA\_ECF\)

Produto da NF de referência 

Identificação do produto da nota de saída

\(será sempre o mesmo da nota de devolução, exceto quando se tratar de um produto associado\)

Código do Estabelecimento de Origem da NF de referência

Estabelecimento da nota de saída

\(será sempre o mesmo da nota de devolução, exceto quando se tratar de geração por I\.E\.U\.\)

Quantidade da NF de referência \(quantidade original\)

Quantidade original da nota de saída \(sem conversão\)

Quantidade convertida da NF de referência 

Quantidade da nota de saída convertida \(é a quantidade da saída que consta da Ficha 3\) 

Quando não houver necessidade de conversão, será a mesma quantidade do campo anterior\.

Valor ICMS da NF de referência

*Este campo da tabela do relatório é preenchido apenas no cálculo VC das saídas \(conforme item 3\) *

Quantidade utilizada da NF de referência

*Este campo da tabela do relatório é preenchido apenas no cálculo VC das saídas \(conforme item 3\)*

Valor Médio Calculado

Valor de confronto proporcional calculado para a nota de saída\.	

Valor de Confronto da nota de referência

Valor de confronto da nota de saída \(valor de confronto recuperado da tabela da Ficha 3\)

Quantidade Devolvida da NF de referência

Quantidade devolvida que consta na SAFX192 \(sem conversão\)

  


= = = = = 

