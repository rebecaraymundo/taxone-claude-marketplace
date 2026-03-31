# MTZ_EFD_Pre_Geracao_Registro_C176

> Fonte: MTZ_EFD_Pre_Geracao_Registro_C176.docx






THOMSON REUTERS

Módulo Sped Fiscal – Pré-Geração do Registro C176

(Ressarcimento de ICMS em Operações com ST)


Localização: Menu Sped, Módulo EFD - Escrituração Fiscal Digital, item Pré-Geração à Registro C176


DOCUMENTO DE REQUISITO






Sumário

1.	Parâmetros da Tela	2
2.	Recuperação dos Dados e Processamento (C176)	4
3.	Recuperação dos Dados e Processamento (Ajustes – C195/C197)	13
4.	Recuperação dos Dados e Processamento (Lançamento na Apuração do ICMS)	16
5.	Gravação dos Dados na Tabela Auxiliar	17
6.	Emissão do Relatório	24









## Parâmetros da Tela


Esta geração foi criada na OS2388-N1-A (item 2.5), em Maio/2009, com objetivo de gerar os dados do registro C176 de um determinado período. Os dados apurados são armazenados em tabelas auxiliares, e posteriormente utilizados na geração do arquivo do Sped Fiscal.

A partir da MFS2772 (Maio/26), esta geração passou a gerar também as informações dos registros C195/C197, refrentes a ajustes relacionados aos valores do C176. Além disso, passou a gerar também lançamentos complementares na Apuração do ICMS.

Parâmetros da geração:




## Recuperação dos Dados e Processamento (C176)






Este processo será realizado apenas para os itens de documento fiscal que atendam aos seguintes critérios:

- Nota fiscal de saída;

- A data fiscal da nota deve ser referente ao período informado em tela (>= data inicial e <= data final);

- Modelo 01 ou 55;

- O item da nota deve ser um item de venda de produto sujeito a ST, cuja operação gera direito a ressarcimento. Esta condição é
identificada a partir da parametrização de CFOP, CFOP/NAT, Produtos e NCM’s, da seguinte forma:

(a partir da MFS2772 (Maio/26), a geração passou a utilizar também parametrização de CFOP, Produtos e NCM’s, além da parametrização de Natureza de Operação, já usada na versão original)




Obs:

- Além dos critérios descritos acima, a recuperação das notas e itens a serem processados segue as mesmas regras da recuperação das notas do C100 e C170. Observar que os documentos eletrônicos (modelo 55) normamente, não terão os seus itens gravados no C170, mas, no caso dos itens com direito a ressarcimento de ST, eles serão gerados sim, para que o registro C176 possa ser gravado também (esta regra de exceção esta descrita no documento “Notas _Especiais_C100”).

- Quando o parâmetro “Geração p/Inscrição Estadual Única” for = “Sim”, a recuperação dos documentos fiscais será realizada para todos os estabelecimentos envolvidos na centralização, ou seja, o centralizador e os centralizados, de acordo com a parametrização de Inscrição Estadual Única do Módulo de Controle das Obrigações Estaduais.


Para cada item que atenda aos critérios acima, serão executados os seguintes passos:

Os passos a seguir descrevem como será feita a recuperação das notas de entrada referentes ao produto da nota de saída, e a utilização dos dados de cada entrada para gravar no C176. A informação chave para o tratamento das entradas é a quantidade, pois a busca será feita até que a quantidade da(s) entrada(s) atinja a quantidade da saída.

= = = = = = = =0                   00

Sobre conversão da unidade de medida: (Alteração da MFS6746):

Originalmente, todo este processo foi feito sem considerar se a unidade de medida da entrada é a mesma da saída ou não. A partir da MFS6746, antes de usar a quantidade e o preço unitário da entrada, o processo passou a efetuar conversão de medida, sempre que necessário. Os procedimentos para conversão serão descritos a seguir:

Antes de utilizar a quantidade ou o preço unitário da nota de entrada, será verificado se a unidade de medida da entrada é a mesma unidade do item da nota de saída. A unidade verificada em ambas as notas é o campo “25-Unidade de Medida” da SAFX08 (mesmo campo utilizado na gravação da QTD do item da saída no registro C170 na geração do arquivo da EFD).

Quando a unidade não for a mesma, a quantidade e o preço unitário da entrada serão convertidos para a unidade da saída. A lógica é a seguinte:

(trata-se dos campos “24-Quantidade” e “27-Preço Unitário” da SAFX08, que são utilizados no preenchimento dos campos 07 e 08 do registro C176, além de serem utilizados também para composição de outros campos)


Se a unidade da entrada = unidade da saída:
Neste caso, o processo segue normalmente, não havendo necessidade de efetuar a conversão;
Senão
Neste caso, a quantidade e o preço unitário da entrada serão convertidos para a unidade da saída. A conversão será feita conforme
o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW (menu “Manutenção à Cadastros à
Conversão de Unidades de Medida”), da seguinte forma:
- Em primeiro lugar, é pesquisada a existência do fator de conversão na tabela de conversão por produto;
- Caso não exista, é feita a pesquisa na tabela de conversão padrão;
Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o item da nota de entrada em questão será
desconsiderado, e será gravada a seguinte mensagem de erro no log:

“Fator de conversão de medida de XXX para XXX não encontrado. A nota de entrada não será considerada na geração dos dados”

(o primeiro “XXX” será a unidade da entrada, e o segundo “XXX”, a unidade da saída)
(na coluna do log que mostra a chave do registro, serão demonstradas as informações necessárias para permitir a identificação do
item da nota de entrada em questão, mostrando inclusive o número do item da nota)

Importante à A partir deste procedimento de conversão de medida, sempre que as regras adiante citarem a utilização da quantidade ou do preço unitário da nota de entrada, o conteúdo a ser utilizado será sempre o resultado dos valores convertidos (quando for o caso), inclusive no relatório de conferência do processo.


(ver exemplos de conversão de medida no documento anexo “Exemplo-Conversao-de-Medida-C176”)


= = = = = = = = fim conversão de medida


Passo 1 à Neste passo será verificado se no item da nota existe a informação do documento fiscal de referência (campos 102, 117, 118 e 119 da SAFX08). No mínimo os campos do número e da data de emissão do documento de referência (campo 102 e 117) precisam estar preenchidos. Se um destes dois não estiver preenchido, será considerado que o documento fiscal de referência não foi informado.

Caso sim,

Recuperar o documento de referência da base de dados e gravar as informações desta nota conforme descrito no item “5-Gravação
dos Dados” (item “Gravação dos Dados referentes ao registro C176)”. Para a recuperação desta nota na base de dados, serão
utilizados os critérios de pesquisa e a mensagem de erro descritos no quadro abaixo “Critérios para obter o documento de
referência (Passo 1)”. Se acontecer da nota não ser encontrada, os demais passos não serão ser executados, o processo de
gravação dos dados também não será executado, e será gravada mensagem de  erro no log (conforme descrito no quadro citado
acima).  Se o documento de referência for identificado, o processo segue normalmente para o próximo passo (passo 2).

Caso não,

Neste caso, o processo parte para o passo 3.


Passo 2 à Neste passo será verificado se a quantidade da nota de referência já “cobre” a quantidade da venda do produto:

Se quantidade da nota da entrada >= quantidade da venda (quantidade da nota da venda, que aparecerá no C170)
Neste caso o processo se encerra, ou seja, o C176 referente ao item em questão será gerado apenas com as informações da
nota de entrada informada nos campos do documento fiscal de referência da nota de saída;
Senão
Neste caso, o processo parte para o passo 3.


Passo 3à Neste passo será feita a pesquisa na base de dados para recuperar a(s) última(s) nota(s) de entrada(s) do produto em questão, até que o total da quantidade de todas as notas de entrada atinjam a quantidade vendida do produto (quantidade da nota da venda, que aparecerá no C170). Para cada uma das notas recuperadas neste processo será gravado um registro na tabela auxiliar com as informações da nota, conforme descrito no item “5-Gravação  dos Dados” (item “Gravação dos Dados referentes ao registro C176”). Para recuperar as notas da base de dados serão utilizados os critérios de pesquisa descritos no quadro abaixo “Critérios para recuperação das notas de entrada (Passo 3)”.






Críticas a serem realizadas durante o processamento:

Para cada uma das situações descritas no quadro abaixo, será gerada a mensagem de aviso no log de erros:



Observações importantes:

Gravação do C176:

Ao gravar os dados de cada nota de entrada na tabela auxiliar, seguir as regras descritas no item “5-Gravação  dos Dados” (item “Gravação dos Dados referentes ao registro C176”).

Campos obrigatórios:

Na gravação dos dados, observar as mensagens criadas para crítica dos campos obrigatórios (mensagens 50, 51, 52 e 53 da planilha “Sped_Fiscal_Log_Erros”).

Sobre as NF’e:

Observar que no caso das NF’e de emissão própria (saídas) em que o item atenda aos critérios de geração do C176, serão gerados no arquivo da EFD os registros do item (C170) e o C176, mas somente os itens da nota que geram ressarcimento (ver “Exceção 6” do registro C100 no Guia Prático a partir da versão 1.0.4).

Sobre performance:

Conforme descrito no help deste processo, a vantagem de carregar os campos da SAFX08 referentes ao documento fiscal de referência é melhorar a performance do processo, já que neste caso não será necessário executar a busca da(s) nota(s) na base de dados, considerando que muitas vezes a quantidade da nota da última entrada já poderá cobrir a quantidade vendida do produto.

Sobre a pessoa fis/jur das notas de entrada:

Foi questionado se não deveríamos considerar o fornecedor para recuperar as notas de entrada, para não trabalharmos com notas de fornecedores diferentes. Mas segundo a Informação, neste momento não devemos ter esta preocupação, já que o Guia Prático não cita nada sobre fornecedor, e deixa claro que devemos apenas demonstrar as últimas notas fiscais de entrada do produto em questão.

Sobre a base de cálculo do ST:

A base de cálculo a ser considerada para o campo 09-VL_UNIT_BC_ST seguirá o conceito aplicado em duas outras obrigações que tratam este mesmo tipo de informação:



## Recuperação dos Dados e Processamento (Ajustes – C195/C197)


A geração dos dados para os ajustes (C195/C197) será executada apenas quando o parâmetro “Gerar os ajustes (C197) e os lançamentos complementares na Apuração do ICMS” estiver marcado.

Para cada item de nota fiscal de saída processado serão gerados um ou dois ajustes, um de ressarcimento, e outro de crédito.

Assim, após o processamento de cada item de nota fiscal de saída sujeito ao ressarcimento (conforme definido no item 2), este processo será executado para a gravação dos dados dos ajustes, que será realizada da seguinte forma:

Os parâmetros para gravação dos ajustes serão recuperados do item de menu “Parâmetros à Registro C176 à Parâmetros p/Geração dos Ajustes e Lançamentos”, considerando o estabelecimento da geração. No caso de geração por inscrição estadual única, será sempre utilizada a parametrização do estabelecimento centralizador (estabelecimento selecionado na tela da geração);

Para cada item processado, poderão ser gerados até dois ajustes:
- (lembrando que no ajuste (SAFX113) existe a indicação do item da nota, ou seja, do produto)

- Um ajuste de ressarcimento, caso o campo 09 gerado p/o C176 (Valor Unitário da BC do ICMS-ST da Entrada) seja <> zeros;
- Um ajuste de crédito, caso o campo 08 gerado p/o C176 (Valor Unitário da Entrada) seja <> zeros;

Os ajustes do Sped Fiscal (C197) requerem a informação de uma observação no registro “pai” C195. A informação da observação a ser utilizada para estes ajustes é informada pelo usuário na parametrização citada acima, e também será armazenada na tabela auxiliar para posterior utilização na geração do Sped Fiscal;

O valor de cada um destes ajustes é calculado da seguinte forma:

Valor do ajuste de ressarcimento:




Valor do ajuste de crédito:

As diferenças entre o ajuste de ressarcimento e o ajuste de crédito, são as seguintes:

- Para a base de cálculo do ajuste de crédito, é utilizado o campo 08 do C176, ao invés do campo 09;

Alteração MFS7174 (alterada a alíquota utilizada no cálculo do ajuste)
- Para o ajuste de crédito é utilizada a alíquota interna do produto, ao invés da alíquota do ICMS-ST;
- Para o ajuste de crédito é utilizada a alíquota do ICMS, ao invés da alíquota interna do produto;




As informações a serem armazenadas para cada ajuste estão descritas no item “5-Gravação dos Dados” (no item “Gravação dos Dados referentes aos Ajustes”);

Tratamento de erro: caso não exista o registro da parametrização a ser utilizada, os lançamentos não serão gerados, e no log será gravada a seguinte mensagem de erro: “Não existem dados da parametrização dos ajustes a lançamentos da Apuração do ICMS. Os ajustes não foram gerados”.


## Recuperação dos Dados e Processamento (Lançamento na Apuração do ICMS)


A geração dos lançamentos complementares na Apuração do ICMS será executada apenas quando o parâmetro “Gerar os ajustes (C197) e os lançamentos complementares na Apuração do ICMS” estiver marcado.

Para cada estabelecimento processado serão gerados um ou dois lançamentos, um para o total dos ajustes de ressarcimento, e outro para o total dos ajustes de crédito.


Assim, após o processamento de cada estabelecimento, este processo será executado para a gravação dos lançamentos, que será realizada da seguinte forma:

Os parâmetros para gravação dos lançamentos serão recuperados do item de menu “Parâmetros à Registro C176 à Parâmetros p/Geração dos Ajustes e Lançamentos”, considerando o estabelecimento da geração. No caso de geração por inscrição estadual única, será sempre utilizada a parametrização do estabelecimento centralizador (estabelecimento selecionado na tela da geração);

Para cada estabelecimento processado, poderão ser gerados até dois lançamentos:

- Um lançamento com o valor total de todos os ajustes de ressarcimento gerados para o estabelecimento;
- Um lançamento com o valor total de todos os ajustes de crédito gerados para o estabelecimento;

Cada um destes lançamentos só será gerado quando o seu respectivo total for <> zeros.


O valor de cada um destes lançamentos é calculado da seguinte forma:



As informações a serem armazenadas para cada lançamento estão descritas no item “5-Gravação dos Dados” (no item “Gravação dos Dados referentes aos Lançamentos Complementares da Apuração do ICMS”);

Tratamento de erro: caso não exista o registro da parametrização a ser utilizada, os lançamentos não serão gerados, e no log será gravada a seguinte mensagem de erro: “Não existem dados da parametrização dos ajustes a lançamentos da Apuração do ICMS. Os lançamentos não foram gerados”.


## Gravação dos Dados na Tabela Auxiliar



Gravação dos Dados referentes ao Registro C176:

Segue descrição das informações a serem armazenadas para posterior gravação do registro C176 na geração do Sped Fiscal:

Observar que além destes dados também deverão ser armazenadas todas as referências da nota fiscal de saída, e seu respectivo item a qual o C176 pertence, lembrando que o registro C176 é “filho” do registro de itens da nota (C170).




Gravação dos Dados referentes aos Ajustes (C195/C197):

Segue descrição das informações a serem armazenadas para posterior gravação dos registros C195 e C197 na geração do Sped Fiscal.

Estas informações serão gravadas nas tabelas SAFX específicas para geração destes registros do Sped Fiscal. São elas:

SAFX112 – OBSERVAÇÕES DA NOTA FISCAL       (corresponde ao C195, registro “filho” do C100);
SAFX113 – AJUSTES DO LANÇAMENTO FISCAL    (corresponde ao C197, registro “filho” do C195);

Observar que além dos dados descritos abaixo, a SAFX112 também possui todas as referências da nota fiscal de saída a qual a observação pertence.

Da mesma forma, além dos dados descritos abaixo, a SAFX113 também possui todas as referências da observação (SAFX112) a qual o ajuste estará vinculado,  já que a SAFX113 é uma tabela “filha” da SAFX112 (assim como o registro C197 é um registro “filho” do C195).

Sobre a parametrização (item Parâmetros à Registro C176 à Parâmetros p/Geração dos Ajustes e Lançamentos):

Observar que a parametrização para geração destas informações contém os dados específicos para os ajustes de ressarcimento e os  ajustes de crédito. No entanto, é possível que o usuário informe o mesmo código de observação a ser utilizada nos dois casos. Quando isso ocorrer, obviamente que será gravado apenas um registro na SAFX112, uma vez que o código da observação é chave. Da mesma forma, nada impede que a observação parametrizada possa já existir para a nota fiscal em questão. Estas duas situações devem ser previstas na geração.

Nos ajustes de ressarcimento:


- Informações da Observação (SAFX112) p/o C195:



- Informações do Ajuste (SAFX113) p/o C197:



Nos ajustes de crédito:


- Informações da Observação (SAFX112) p/o C195:



- Informações do Ajuste (SAFX113) p/o C197:




Gravação dos Dados referentes aos Lançamentos Complementares da Apuração do ICMS:

Os lançamentos serão gravados na Tabela dos Lançamentos Complementares da Apuração do ICMS.


Informações do Lançamento de Ressarcimento:




Informações do Lançamento de Crédito:





Observações importantes sobre a gravação dos lançamentos:

Observar que para os lançamentos do tipo “1”, como é o caso dos lançamentos que serão gravados, existe uma associação entre o lançamento e os ajustes que originaram o lançamento. Para isso, existe uma tabela interna que tem este relacionamento, para que na tela de manutenção dos lançamentos sejam exibidos todos os ajustes vinculados ao lançamento. Esta tabela também será alimentada neste processo para que o lançamento a ser gerado fique corretamente associado a todos os ajustes da SAFX113 que o originaram (conforme as regras descritas no item 4). No caso, para o lançamento de ressarcimento, serão todos os ajustes de ressarcimento que foram totalizados para compor o seu valor, e a mesma coisa para o lançamento de crédito.

(este procedimento é padrão para geração automática de lançamentos complementares)

Antes de gerar os lançamentos, será realizado procedimento de limpeza dos lançamentos que possam já ter sido gerados anteriormente por este mesmo processo.  Este procedimento é necessário por causa das situações de reexecução do processo em um mesmo período. Para efetuar a limpeza, considerar os campos de identificação do lançamento (empresa, estabelecimento, obrigação fiscal e data da apuração), e também o indicador próprio criado para estes lançamentos (IND_DIG_CALCULADO = “C”).


## Emissão do Relatório


Na aba “Relatório” será emitido um relatório de conferência dos dados gerados.

O usuário poderá visualizar o relatório logo após a geração, e também posteriormente, selecionando uma geração já executada na aba “Processos”.

Ver layout na planilha anexa “Layout-Conferencia-PreGeracao-do-C176”.

Regras do preenchimento dos dados:

Para cada item de saída processado, serão demonstradas as entradas consideradas para geração do C176.

Para cada nota de entrada considerada, serão demonstrados os dados básicos de identificação, e ao final da linha, os dois valores calculados para geração do registro C176: campo “08-Valor Unitário da Mercadoria” e campo “09-Valor Unitário da BC do ICMS-ST”.

(Observar que o layout mostra o número do item da nota, e assim, caso ocorra a situação de numa mesma nota de entrada, existirem dois itens de mesmo produto recuperados, cada um deles será gerado numa linha do relatório. Apesar da geração do C176 ser por nota fiscal (ou seja, nesse caso estes dois itens de mesma nota iriam gerar um único C176), o objetivo é demonstrar ao usuário todo o detalhamento do processo realizado)

Após a exibição de todas as notas de entrada referentes ao item de saída, serão demonstrados os dois ajustes (C197) gerados para o item: o ressarcimento e o crédito.

Ao final de todas as notas de saída de um determinado Estabelecimento, será demonstrado o valor total de ressarcimento e o valor total de crédito, valores estes originaram os lançamentos de forma automática na Apuração do ICMS do estabelecimento.

Várias colunas do relatório trabalham com letras para identificação da coluna. Este recurso foi utilizado para demonstrar o cálculo realizado na apuração de alguns valores importantes, como por exemplo, os valores gerados para o registro C176, e também os ajustes do C197. Desta forma, o usuário poderá verificar como os cálculos foram realizados.

Obs: Todas as informações do relatório são as informações já descritas e detalhadas nos itens deste documento referentes à recuperação e processamento dos dados, por isso, as regras de preenchimento abaixo não detalham, tabelas, numeração de campos, etc ...

Linha de identificação do item da nota de saída:




Linhas das notas fiscais de entrada associadas ao item da saída:





Linhas de total das entradas demonstradas:




Linhas dos ajustes gerados para o item da saída:


Alteração MFS7174: A descrição dos campos de alíquota destas linhas foram alteradas para refletir corretamente o conteúdo da informação. Vide  planilha anexa “Layout-Conferencia-PreGeracao-do-C176”.




Linhas dos totais do Estabelecimento:




= = = = = =






| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| OS2388-N1-A | Reformulação do C176 - GP Vrs 1.0.4 (Maio/2009) | Criação de uma rotina preliminar para gerar os dados do registro C176, conforme as alterações divulgadas pelo Guia Prático vrs 1.0.4 (Maio/2009) . (este documento é a transcrição das regras especificadas na época, na OS2388-N1-A) | 19/04/2016 (criação do documento) |
| MFS2772 | Atendimento a Portaria CAT 158 | Para atendimento a Port. CAT 158 esta geração passou a gerar também os ajustes (C195/C197) e lançamentos complementares na Apuração do ICMS, referentes aos valores apurados para o registro C176, e também a emitir um relatório de conferência dos valores apurados. | 30/05/2016 |
| MFS7174 | Alteração no cálculo dos ajustes | Alteração no cálculo dos ajustes para corrigir as alíquotas utilizadas:  - Ver item “3-Recuperação dos Dados e Processamento (Ajustes – C195/C197)”, subitens “Valor do Ajuste de Ressarcimento”, e “Valor do Ajuste de Crédito”;  - Ver também o item “6-Emissão do Relatório”, subitem “Linhas dos ajustes gerados para o item da saída” (alterada a descrição dos campos que exibem as alíquotas utilizadas no cálculo dos ajustes); | 06/10/2016 |
| MFS6746 | Conversão de Medida | Alteração na geração do C176 p/tratar conversão de medida entre entrada x saída | 07/11/2016 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Data Inicial | Data | S | S |  | Neste campo o usuário informará a data inicial do período da geração. |  |
| Data Final | Data | S | S |  | Neste campo o usuário informará a data final do período da geração. |  |
| Pesquisar últimas entradas até | Data | S | S |  | Neste campo é informada a data limite até onde será feita a pesquisa das últimas notas de entrada do produto.  Obs: Esta pesquisa é feita desde a data da venda (data da NF da venda) até a data limite informada, sendo que ao atingir a quantidade da venda a pesquisa é interrompida. Assim, esta data é apenas um limite “genérico” para os casos em que as entradas não sejam encontradas (para evitar que a pesquisa seja feita indeterminadamente). |  |
| Gerar os ajustes (C197) e os lançamentos complementares na Apuração do ICMS | Alfanumérico | N | S | Default:   Desmarcado | Este campo é um checkbox onde o usuário poderá optar em gerar ou não os dados para os ajustes do C197 e os lançamentos da Apuração do ICMS. | (parâmetro criado na MFS2772) |
| Geração p/Inscrição Estadual Única | Alfanumérico | N | S | Default:   opção “Não” | Este campo apresenta duas opções:   - Sim - Não  As opções são alternativas.  A opção informada interfere no campo “Estabelecimentos”, conforme descrito na regra específica. |  |
| Estabelecimentos | Alfanumérico | S | Ver regra |  | Neste campo será exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário.  A exibição dos estabelecimentos depende da opção informada no campo “Geração p/Inscrição Estadual Única”, da seguinte forma:  Se = “Sim” à Neste caso, serão exibidos apenas os estabelecimentos centralizadores, conforme a parametrização da Inscrição Estadual Única no módulo de Controle das Obrigações Estaduais;   Se = “Não” à Neste caso serão exibidos todos os estabelecimentos da empresa;  Sempre que a opção do campo “Geração p/Inscrição Estadual Única” for alterada, esta lista será refeita dinamicamente, considerando a nova opção. |  |


| Visão resumida do processo:  O processo identifica as notas fiscais de saída do período, com direito à ressarcimento de ICMS-ST. Para cada item identificado, será realizada a busca das últimas entradas do produto até atingir a quantidade da saída. O processo é complexo, e se resumo na seguinte lógica:  Se o item da saída tiver a informação do documento fiscal de referência preenchido:       Neste caso, a busca da última entrada será feita acessando diretamente o documento informado como referência.       Se a quantidade deste documento de entrada já cobrir a quantidade da nota da saída,           Neste caso a pesquisa já estará concluída, e os dados serão gerados apenas com base nesta entrada;      Senão,           A pesquisa prossegue na busca das outras entradas anteriores até que a quantidade da saída seja atingida;  Senão (não existe a informação do documento fiscal de referência)       Neste caso, será realizada a pesquisa das últimas entradas do produto, desde a data da venda (data da NF da venda) até a data      limite informada em tela, até que a quantidade da saída seja atingida;  Os dados de cada nota de entrada identificada serão gravados numa tabela auxiliar, com todas as informações solicitadas no registro C176, estas informações serão utilizadas posteriormente na gravação do arquivo do Sped Fiscal. |
| --- |


| O CFOP ou o CFOP/NAT do item deve estar parametrizado:       O CFOP do item deve constar da parametrização do menu “Parâmetros à Registro C176 à NF’s Saída c/direito a        Ressarcimentoà CFOP” do módulo EFD”;       ou       O CFOP/Natureza de Operação do item deve constar da parametrização do menu “Parâmetros à Registro C176 à NF’s      Saída c/direito a Ressarcimentoà CFOP / Natureza de Operação” do módulo EFD”;  O Produto ou o seu NCM deve estar parametrizado:        O produto do item deve constar da parametrização do menu “Parâmetros à Registro C176 à Produtos” do módulo       EFD”;        ou        O NCM do produto do item deve constar da parametrização do menu “Parâmetros à Registro C176 à NCM’s” do       módulo EFD”;  Na pesquisa da parametrização dos Produtos / NCM’s, poderão existir várias parametrizações válidas para o Estabelecimento e período em questão, pois esta parametrização é por Estab/Grupo/Aliq/Validade.  Serão pesquisadas as parametrizações existentes para o Estabelecimento em questão, Grupo válido para o período da geração, e cuja validade atenda ao período da geração, ou seja:  - tenha validade inicial <= ao primeiro dia do período da geração; - se a validade final estiver preenchida, ela deve ser uma data >= ao último dia do período da geração;  Basta que o Produto, ou o seu NCM, conste em qualquer uma das parametrizações válidas para o período.  Obs: A alíquota interna da parametrização onde o produto, ou seu NCM foi identificado, será utilizada posteriormente para o cálculo do ajuste de crédito (cálculo definido no item “3-Recuperação dos Dados e Processamento (Ajustes C195/C197)”). |
| --- |


| Critérios para obter o documento de referência (Passo 1) |
| --- |
| O documento de referência deve ser recuperado na base de dados a partir dos critérios descritos abaixo:   - nota fiscal de entrada (MOVTO_E_S  <> ‘9’); - número da nota = conteúdo do campo 117 da SAFX08; - série da nota      = conteúdo do campo 118 da SAFX08; - subsérie da nota = conteúdo do campo 119 da SAFX08; - data de emissão da nota = conteúdo do campo 102 da SAFX08; - produto = produto do item da nota de venda (ver OBS abaixo);   Considerar a necessidade de pesquisar esta nota nas tabelas normais (X07/X08), já que a nota fiscal poderá estar num período anterior ao período da movimentação gerada no Datamart;  OBS: Caso no documento encontrado exista mais de um item do mesmo produto, deve-se totalizar as quantidades e as bases de cálculo de todos os itens, e o campo VL_UNIT_BC_ST deve ser calculado a partir das bases e quantidades já totalizadas, conforme descrito no item “5-Gravação  dos Dados” (item “Gravação dos Dados referentes ao registro C176”).   Crítica a ser realizada:  Caso a nota de referência não seja encontrada na base de dados, será gravada a seguinte mensagem no log:      “O documento de referência indicado no item da nota não foi encontrado na base de dados. O registro C176 não foi gerado”.   Na planilha de erros “Sped_Fiscal_Log_Erros” esta é a mensagem de número 61. Na linha “Dados do Registro” deve ser exibida a identificação da nota de ressarcimento, o item da nota em questão, e também os dados do documento fiscal de referência (Num/Ser/Sub/Dt Emis). |


| Critérios para recuperação das notas de entrada (Passo 3)”. |
| --- |
| - nota fiscal de entrada (MOVTO_E_S  <> ‘9’); - data fiscal da nota = considerar as notas com data <= a data da nota fiscal de venda do produto (data da nota de saída);   Atendido este primeiro critério, as notas deverão ser recuperadas em ordem decrescente de data, até que o total da quantidade de todas as notas recuperadas atinja a quantidade vendida do produto (quantidade da venda).   - produto = produto do item da nota de venda (ver OBS abaixo);  - desconsiderar as notas canceladas - desconsiderar as notas de devolução - considerar apenas os itens com CFOP ou CFOP/Natureza parametrizados no menu “Parâmetros à Registro C176 à NF’s    Entrada”;   Considerar a necessidade de pesquisar esta nota nas tabelas normais (X07/X08), já que a nota fiscal poderá estar num período anterior ao período da movimentação gerada no Datamart.  Atentar para o detalhe de não considerar a mesma nota já recuperada através do documento de referência informado na SAFX08.  OBS: Quando no documento encontrado existir mais de um item do mesmo produto, deve-se totalizar as quantidades e as bases de cálculo de todos os itens, e o campo VL_UNIT_BC_ST deve ser calculado a partir das bases e quantidades já totalizadas, conforme descrito no item “5-Gravação  dos Dados” (item “Gravação dos Dados referentes ao registro C176”). |


| Situação de erro | Mensagem de aviso |
| --- | --- |
| Quando no item da nota de saída os campos do documento de referência estiverem preenchidos, mas ao tentar recuperar a nota na base de dados, ela não for encontrada. Neste caso, deverá ser gerada mensagem de aviso, e a rotina deve interromper o processamento deste item (ou seja, não precisa fazer a pesquisa de outras notas de entrada na base de dados, pois diante do erro encontrado, o usuário terá que verificar se o documento de referência informado esta errado) | O documento de referência indicado no item da nota não foi encontrado na base de dados. O registro  C176 não será gerado. |
| Quando o total da quantidade de todas as notas de entrada recuperadas, não for o suficiente para “cobrir”  a quantidade do item da nota de saída. | A quantidade do Item de Saída não foi atingida pelas quantidades das últimas NF de Entradas recuperadas |
| Quando o item da nota de saída não tiver a informação do documento de referência, e ao realizar a pesquisa das notas de entrada na base de dados, não for encontrada nenhuma nota até a data limite informada em tela. | Não foram identificadas NF de Entradas para o Item de Saída. O registro  C176 não será gerado. |
| Quando na nota de entrada, a quantidade do item ou os três campos da base de cálculo do ST não estiverem preenchidos no item, será exibida mensagem de erro no log. | Para calcular a BC unitária é necessário que os campos da QTD (campo 24) e da BC do ICMS-ST estejam preenchidos no item da nota (campo 61, 144 ou 106). |


| Registro 88-STITNF do Sintegra à Tem um procedimento que grava as últimas entradas do produto até atingir a quantidade do produto em estoque. Para recuperar as entradas não há filtro de CFOP (vale qq nota). Nas operações interestaduais usa a BC normal do ST (campo 61 da SAFX08), já nas internas usa a não escriturada (campo 144 da SAFX08). A razão desta lógica é obter a BC no caso das operações em que o ST não é lançado na entrada (o emitente não é o responsável pelo recolhimento). Este tratamento foi feito para clientes de MG, com base no Decreto 44.541 (Jun/2007) – SEF-MG (OS2437).  CAT 17 (Apur Compl/Ressarcimento de ST) àTambém trata as operações de entrada dos produtos que geraram solicitação de Ressarcimento. Neste caso existe uma parametrização por CFOP/Nat. Para recuperar as notas (coluna “Valor Total da Base de Cálculo da Retenção” do Modelo III da CAT 17). Utiliza a BC normal do ST (campo 61 da SAFX08) ou o campo 106, para os casos em que a retenção for feita na origem. Neste caso, os campos normais da BC e do valor do ST não estarão preenchidos, e a BC estará no campo “106-Base Cálculo Carga Tributária Origem ICMS” (da mesma forma que o campo 144, também se trata de ST que não será escriturada no livro, e por isso, os valores do ST não estão nos campos normais).  (OS1165, v1r8.0) |
| --- |


| VL_BC_ICMS | A base de cálculo a ser utilizada para o ajuste, é calculada da seguinte forma:  Valor do campo 09 (Valor Unitário da BC do ICMS-ST da Entrada) gerado p/o C176 x Quantidade do item da nota de saída  Caso exista mais de uma nota fiscal de entrada para o item em questão, ou seja, caso tenha sido gerado mais de um registro C176 para o item, o valor a ser utilizado será a média do campo 09 de todos os registros.   Exemplo:  Registro 1: Valor do campo 09= 250,00 Registro 2: Valor do campo 09 = 78,00 Registro 3: Valor do campo 09 = 1.480,00  Valor médio a ser utilizado = (250,00 + 78,00 + 1.480,00) / 3 = 602,66 |
| --- | --- |
| ALIQ_ICMS | Alteração MFS7174 (alterada a alíquota utilizada no cálculo do ajuste)  Alíquota do ICMS-ST da nota fiscal de entrada usada para geração do registro C176  Caso exista mais de uma nota fiscal de entrada para o item em questão, ou seja, caso tenha sido gerado mais de um registro C176 para o item, a alíquota a ser utilizada será a alíquota do ICMS-ST da nota de entrada mais recente.   Alíquota Interna do produto.   Esta alíquota é recuperada da parametrização do produto ou NCM, que foi utilizada na identificação do produto.   Obs: Conforme orientaçao da Informação, quando se trata de ressarcimento de ICMS-ST a aliquota a ser utilizada será sempre a alíquota interna. |
| VL_ICMS | O valor do ajuste é calculado aplicando-se a alíquota sobre a base de cálculo, da seguinte forma:                       (VL_BC_ICMS * ALIQ_ICMS / 100) |


| VL_BC_ICMS | A base de cálculo a ser utilizada para o ajuste, é calculada da seguinte forma:  Valor do campo 08 (Valor Unitário da Entrada) gerado p/o C176 x Quantidade do item da nota de saída  Caso exista mais de uma nota fiscal de entrada para o item em questão, ou seja, caso tenha sido gerado mais de um registro C176 para o item, o valor a ser utilizado será a média do campo 08 de todos os registros.   (quando for o caso, a média será calculada seguindo o mesmo exemplo descrito p/o ajuste de ressarcimento) |
| --- | --- |
| ALIQ_ICMS | Alteração MFS7174 (alterada a alíquota utilizada no cálculo do ajuste)  Alíquota Interna do produto.   Esta alíquota é recuperada da parametrização do produto ou NCM, que foi utilizada na identificação do produto.   Alíquota do ICMS da nota fiscal de entrada usada para geração do registro C176.  Caso exista mais de uma nota fiscal de entrada para o item em questão, ou seja, caso tenha sido gerado mais de um registro C176 para o item, a alíquota a ser utilizada será a alíquota do ICMS da nota de entrada mais recente. |
| VL_ICMS | O valor do ajuste é calculado aplicando-se a alíquota sobre a base de cálculo, da seguinte forma:                       (VL_BC_ICMS * ALIQ_ICMS / 100) |


| OBS: No caso de geração por inscrição estadual única, os lançamentos serão gerados sempre para o estabelecimento                centralizador (estabelecimento selecionado na tela da geração), considerando o valor total dos ajustes referentes a todos os estabelecimentos envolvidos na centralização (centralizador e centralizados). Além disso, será utilizado o livro fsical “165”, ao invés da livro “108”; |
| --- |


| Lançamento de ressarcimento: | Total do valor de todos os ajustes de ressarcimento (total do campo VL_ICMS) |
| --- | --- |
| Lançamento de crédito: | Total do valor de todos os ajustes de crédito (total do campo VL_ICMS) |


| Pessoa Fis/Jur | Indicador e Código do emitente da nota fiscal da entrada   (a informação deste campo irá gerar o campo “06- COD_PART_ULT_E” do registro C176) |
| --- | --- |
| Valor unitário da entrada | Alteração MFS2772: Na geração deste campo foram acrescidas as despesas acessórias do item. Originalmante, o campo era preenchido apenas com o preço unitário do item.   Este campo será preenchido com o valor unitário (campo 27-Preço Unit) + despesas acessórias (campos 39-Frete, 40-Seguro e campo 41-Outras Despesas) do item da nota fiscal de entrada  A informação do campo “27-Preço Unitário” já é o valor unitário, como descreve o próprio nome. Já o valor dos campos “Frete”, “Seguro” e “Outras Despesas” precisa ser dividido pela quantidade do item, para que seja utilizado o valor unitário destas despesas.  Assim, o valor será apurado da seguinte forma:                               [  Preço Unitário  +  ( ( Frete + Seguro +  Outras Despesas ) / Qtd do item )  Obs à no caso da nota de entrada ter mais de um item de mesmo produto, recuperados no processo, será calculado o preço unitário médio (totalizar o valor unitário de todos os itens e depois dividir o valor obtido pelo número de itens) .     (a informação deste campo irá gerar o campo “08- VL_UNIT_ULT_E” do registro C176) |
| Valor unitário da base de cálculo do ICMS-ST da entrada | Este campo será preenchido com a base de cálculo do ST do item da nota de entrada, dividida pela quantidade do item (quantidade também da entrada). Este procedimento é feito para se calcuilar o valor unitário, como pede o registro C176.   A base de cálculo a ser utilizada dependerá do campo que estiver preenchido na SAFX08, já que devemos considerar que a operação pode ter o ICMS-ST escriturado ou não escriturado, e em qualquer um dos casos a base de cálculo precisa ser demonstrada no C176.  Para isso, será aplicada a seguinte lógica no preenchimento deste campo:  Se campo “61-Base ICMS-ST” preenchido:      O campo será preenchido com o seguinte valor à  (61-Base ICMS-ST / 24-Quantidade) Senão      Se campo “144-Base ICMS-ST não Escriturada” preenchido:          O campo será preenchido com o seguinte valor à  (144-Base ICMS-ST não Escriturada / 24-Quantidade)      Senão           Se campo “106-Base Cálculo Carga Tribut Origem” preenchido:                O campo será preenchido com o seguinte valor à (106-Base Cálculo Carga Tribut Origem / 24-Quantidade)           Senão                O campo não será preenchido.  Desta forma, qualquer que seja a situação tributária da nota de entrada do produto, a informação será demonstrada. O usuários da CAT17 e os clientes obrigados a geração dos registros 88STES e 88STITNF do Sintegra (Decreto 44.541 de Junho/07, SEF-MG) já estão cientes da necessidade de carregar a informação nos campo 144 ou 106 no caso do ST não escriturado na entrada (conforme descrito RNC176).    Obs à no caso da nota de entrada ter mais de um item de mesmo produto, recuperados no processo, os valores deverão ser totalizados conforme já descrito anteriormente, e o cálculo acima será feito com base nos valores de base e quantidade já totalizados.      (a informação deste campo irá gerar o campo “09- VL_UNIT_BC_ST” do registro C176) |


| Tipo de Observação (campo 12) | “L” (observações referentes aos lançamentos fiscais da nota) |
| --- | --- |
| COD_OBS | Código da observação parametrizada pelo usuário para os ajustes de ressarcimento (parametrização descrita no item 3). |
| TXT_COMPL | (sem informação) |


| COD_AJ | Código do ajuste de ressarcimento parametrizado pelo usuário (parametrização descrita no item 3). |
| --- | --- |
| DESCR_COMPL_AJ | Descrição complementar do ajuste de ressarcimento parametrizada pelo usuário (parametrização descrita no item 3). |
| COD_ITEM | Indicador e Código do produto em questão (produto do item da nota fiscal de saída processada) |
| VL_BC_ICMS | Valor da base de cálculo do ajuste de ressarcimento, conforme cálculo definido no item “3-Recuperação dos Dados e Processamento – Ajustes C195/C197”). |
| ALIQ_ICMS | Valor da alíquota utilizada no cálculo do ajuste de ressarcimento, conforme definido no item “3-Recuperação dos Dados e Processamento – Ajustes C195/C197”). |
| VL_ICMS | Valor do ICMS do ajuste de ressarcimento, conforme cálculo definido no item “3-Recuperação dos Dados e Processamento – Ajustes C195/C197”). |


| Tipo de Observação (campo 12) | “L” (observações referentes aos lançamentos fiscais da nota) |
| --- | --- |
| COD_OBS | Código da observação parametrizada pelo usuário para os ajustes de crédito (parametrização descrita no item 3). |
| TXT_COMPL | (sem informação) |


| COD_AJ | Código do ajuste de crédito parametrizado pelo usuário (parametrização descrita no item 3). |
| --- | --- |
| DESCR_COMPL_AJ | Descrição complementar do ajuste de crédito parametrizada pelo usuário (parametrização descrita no item 3). |
| COD_ITEM | Indicador e Código do produto em questão (produto do item da nota fiscal de saída processada) |
| VL_BC_ICMS | Valor da base de cálculo do ajuste de crédito, conforme cálculo definido no item “3-Recuperação dos Dados e Processamento – Ajustes C195/C197”). |
| ALIQ_ICMS | Valor da alíquota utilizada no cálculo do ajuste de crédito, conforme definido no item “3-Recuperação dos Dados e Processamento – Ajustes C195/C197”). |
| VL_ICMS | Valor do ICMS do ajuste de crédito, conforme cálculo definido no item “3-Recuperação dos Dados e Processamento – Ajustes C195/C197”). |


| Código da Empresa | Código da empresa do login |
| --- | --- |
| Código do Estabelecimento | Código do estabelecimento processado  No caso de geração por inscrição estadual única, será o estabelecimento centralizador. |
| Tipo do Livro Fiscal (OBRIGACAO_FISCAL) | “108, ou “165”, no caso de geração por Inscrição Estadual Única |
| Data da Apuração | Data final do período informado na tela da geração |
| Item da Apuração  (ITEM_OPER_APUR) | Item da apuração parametrizado p/o lançamento de ressarcimento (parametrização descrita no item 4). |
| Descrição do Lançamento | Descrição parametrizada p/o lançamento de ressarcimento (parametrização descrita no item 4). |
| N. Discriminação (NUM_DISCRIMINAÇÃO) | Sequencial do lançamento gerado da seguinte forma: a coluna NUM_DISCRIMINACAO é um sequencial dos lançamentos feitos para um mesmo código de operação.  Para preenchê-la deve-se recuperar o maior sequencial existente na tabela dos lançamentos para o código de operação que se deseja gravar, incrementar um, e gravar o registro. |
| Classe de Lançamento | Código da classe parametrizado p/o lançamento de ressarcimento (parametrização descrita no item 4). |
| Código do Amparo Legal | Código do amparo legal parametrizado p/o lançamento de ressarcimento (parametrização descrita no item 4). |
| Subitem do Amparo | Código do sub-item do amparo legal parametrizado p/o lançamento de ressarcimento (parametrização descrita no item 4). |
| Tipo do lançamento | “1” (lançamento referente aos ajustes demonstrados no registro C197) |
| Valor do Lançamento (VLR_LANCTO) | Valor do lançamento de ressarcimento conforme cálculo descrito no item 4. |
| Tipo de Informação  (IND_DIG_CALCULADO) | “C”  (para diferenciar estes lançamentos, será utilizada a letra “C”, o que possibilitará efetuar o procedimento de limpeza a cada reexecução do processo) |


| Código da Empresa | Código da empresa do login |
| --- | --- |
| Código do Estabelecimento | Código do estabelecimento processado  No caso de geração por inscrição estadual única, será o estabelecimento centralizador. |
| Tipo do Livro Fiscal (OBRIGACAO_FISCAL) | “108, ou “165”, no caso de geração por Inscrição Estadual Única |
| Data da Apuração | Data final do período informado na tela da geração |
| Item da Apuração  (ITEM_OPER_APUR) | Item da apuração parametrizado p/o lançamento de crédito (parametrização descrita no item 4). |
| Descrição do Lançamento | Descrição parametrizado p/o lançamento de crédito (parametrização descrita no item 4). |
| N. Discriminação (NUM_DISCRIMINAÇÃO) | Sequencial do lançamento gerado da seguinte forma: a coluna NUM_DISCRIMINACAO é um sequencial dos lançamentos feitos para um mesmo código de operação.  Para preenchê-la deve-se recuperar o maior sequencial existente na tabela dos lançamentos para o código de operação que se deseja gravar, incrementar um, e gravar o registro. |
| Classe de Lançamento | Código da classe parametrizado p/o lançamento de crédito (parametrização descrita no item 4). |
| Código do Amparo Legal | Código do amparo legal parametrizado p/o lançamento de crédito (parametrização descrita no item 4). |
| Subitem do Amparo | Código do sub-item do amparo legal parametrizado p/o lançamento de crédito (parametrização descrita no item 4). |
| Tipo do lançamento | “1” (lançamento referente aos ajustes demonstrados no registro C197) |
| Valor do Lançamento (VLR_LANCTO) | Valor do lançamento de crédito conforme cálculo descrito no item 4. |
| Tipo de Informação  (IND_DIG_CALCULADO) | “C”  (para diferenciar estes lançamentos, será utilizada a letra “C”, o que possibilitará efetuar o procedimento de limpeza a cada reexecução do processo) |


| NF (saída) | Número, série e subsérie da nota fiscal de saída |
| --- | --- |
| Dt. Emissão | Data de emissão da nota fiscal de saída |
| Pessoa Fis/Jur | Indicador e código da pessoa fis/jur da nota fiscal de saída |
| Item | Número do item da nota fiscal de saída |
| CFOP | CFOP do item da nota fiscal de saída |
| Natureza | Natureza de operação do item da nota fiscal de saída |
| Produto | Dados de identificação do produto : -Indicador -Código -Descrição |
| Quantidade | Quantidade do item da nota fiscal de saída |
| UN | Código da unidade de medida do item da nota fiscal de saída      (coluna incluída na MFS6746) |


| NF (entrada) | Número, série e subsérie da nota fiscal de entrada |
| --- | --- |
| Dt. Fiscal | Data fiscal da nota fiscal de entrada |
| Pessoa Fis/Jur | Indicador e código da pessoa fis/jur da nota fiscal de entrada |
| Item | Número do item da nota fiscal de entrada |
| CFOP | CFOP do item da nota fiscal de entrada |
| Natureza | Natureza de operação do item da nota fiscal de entrada |
| Quantidade | Quantidade do item da nota fiscal de entrada |
| Preço Unitário | Preço unitário da nota fiscal de entrada (campo 27-Preço Unit.) |
| Despesas Acess. (Frete, Seg, Out) | Nesta coluna será demonstrado o total das despesas acessórias do item:  (39-Frete + 40-Seguro + 41-Outras despesas) |
| Aliq ICMS | Alíquota de ICMS do item da nota fiscal de entrada |
| Base ICMS-ST | Base de cálculo do ICMS-ST do item da nota fiscal de entrada.  O valor da base de cálculo do ST será recuperado do campo 61, 144 ou 106 do item da nota, de acordo com a regra definida no preenchimento dos dados para o registro C176 (ver item “5-Gravação dos Dados na Tabela Auxiliar”, subitem “Gravação dos Dados Referentes ao Registro C176”). |
| Aliq ICMS-ST | Alíquota de ICMS-ST do item da nota fiscal de entrada |
| Vlr Unit Merc (campo 08) | Valor calculado para o campo “08-Valor unitário da entrada” do registro C176, conforme definido na gravação dos dados do registro C176 (ver item “5-Gravação dos Dados na Tabela Auxiliar”, subitem “Gravação dos Dados Referentes ao Registro C176”):       [ valor da coluna “Preço Unitário” + (valor da coluna “Despesas Acess” / valor da coluna “Quantidade”) ] |
| BC ST Unit (campo 09) | Valor calculado para o campo “09-Valor unitário da base de cálculo do ICMS-ST da entrada” do registro C176, conforme definido na gravação dos dados do registro C176 (ver item “5-Gravação dos Dados na Tabela Auxiliar”, subitem “Gravação dos Dados Referentes ao Registro C176”):                               valor da coluna “Base ICMS-ST” / valor da coluna “Quantidade” |


| Linha “Totais C176” | Esta linha demonstra os totais das colunas “H” e “I” por nota fiscal.  O motivo de demonstrar estes totais por nota, é para que o usuário possa visualizar exatamente os valores que serão gerados no registro C176, que é por nota fiscal (e não por item como é mostrado no relatório). Assim, quando esta situação ocorrer o total que aparecerá para esta nota será a média dos valores unitários calculados para todos os itens da nota. |
| --- | --- |


| Linha “Ressarcimento” | Nesta linha serão demonstradas as informações geradas para o ajuste de ressarcimento.   São os valores gravados na SAFX113 para o ajuste de ressarcimento, conforme definido no item “5-Gravação dos Dados na Tabela Auxiliar”, subitem “Gravação dos Dados Referentes aos Ajustes”:   Campos:  - Cód. Ajuste à campo COD_AJ do ajuste de ressarcimento; - Base de Cálculo à campo VL_BC_ICMS do ajuste de ressarcimento; - Alíquota à campo ALIQ_ICMS do ajuste de ressarcimento; - Valor do Ajuste à campo VL_ICMS do ajuste de ressarcimento; |
| --- | --- |
| Linha “Crédito” | Nesta linha serão demonstradas as informações geradas para o ajuste de crédito.   São os valores gravados na SAFX113 para o ajuste de crédito, conforme definido no item “5-Gravação dos Dados na Tabela Auxiliar”, subitem “Gravação dos Dados Referentes aos Ajustes”:   Campos:  - Cód. Ajuste à campo COD_AJ do ajuste de crédito; - Base de Cálculo à campo VL_BC_ICMS do ajuste de crédito; - Alíquota à campo ALIQ_ICMS do ajuste de crédito; - Valor do Ajuste à campo VL_ICMS do ajuste de crédito; |


| Linha “Ressarcimento” | Valor total de todos os ajustes de ressarcimento gerados para o estabelecimento.  Este valor corresponde ao lançamento complementar gerado na Apuração do ICMS, com o total dos ajustes de ressarcimento, conforme definido no item “5-Gravação dos Dados na Tabela Auxiliar”, subitem “Gravação dos Dados Referentes aos Lançamentos Complementares da Apuração do ICMS”. |
| --- | --- |
| Linha “Crédito” | Valor total de todos os ajustes de crédito gerados para o estabelecimento.  Este valor corresponde ao lançamento complementar gerado na Apuração do ICMS, com o total dos ajustes de crédito, conforme definido no item “5-Gravação dos Dados na Tabela Auxiliar”, subitem “Gravação dos Dados Referentes aos Lançamentos Complementares da Apuração do ICMS”. |
