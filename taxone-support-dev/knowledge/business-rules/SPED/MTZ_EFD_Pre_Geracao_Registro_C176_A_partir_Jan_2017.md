# MTZ_EFD_Pre_Geracao_Registro_C176_A_partir_Jan_2017

> Fonte: MTZ_EFD_Pre_Geracao_Registro_C176_A_partir_Jan_2017.docx






THOMSON REUTERS

Módulo Sped Fiscal – Pré-Geração do Registro C176 – A partir de Janeiro de 2017

(Ressarcimento de ICMS em Operações com ST)


Localização: Menu Sped, Módulo EFD - Escrituração Fiscal Digital, item Pré-Geração à Registro C176


DOCUMENTO DE REQUISITO







Sumário

1.	Parâmetros da Tela	4
2.	Recuperação dos Dados e Processamento (C176)	7
3.	Recuperação dos Dados e Processamento (Ajustes – C195/C197)	18
4.	Recuperação dos Dados e Processamento (Devoluções)	25
5.	Recuperação dos Dados e Processamento (Ajustes de Estorno das Devoluções)	28
6.	Recuperação dos Dados e Processamento (Lançamento na Apuração do ICMS)	33
7.	Gravação dos Dados	35
8.	Emissão do Relatório	56
9.	Emissão do Relatório das Devoluções	63














## Parâmetros da Tela


Esta geração foi criada na OS2388-N1-A (item 2.5), em Maio/2009, com objetivo de gerar os dados do registro C176 de um determinado período. Os dados apurados são armazenados em tabelas auxiliares, e posteriormente utilizados na geração do arquivo do Sped Fiscal.

A partir da MFS2772 (Maio/16), esta geração passou a gerar também as informações dos registros C195/C197, referentes a ajustes relacionados aos valores do C176. Além disso, passou a gerar também lançamentos complementares na Apuração do ICMS.

A partir da MFS6677 (Set/16), esta geração passou a gerar mais 16 campos com informações para o registro C176, Além disso, foi criado um novo relatório para conferência das novas informações. Esses ajustes são válidos APENAS para gerações a partir de Jan/2017, ou seja, o período de geração deve ser igual ou maior que Jan/2017 para que as alterações dessa MFS sejam consideradas.
Para períodos anteriores a Jan/2017 a geração continuará sendo possível com a pré-geração anterior às alterações dessa MFS (MFS6677).

A partir da MFS9749 (Mar/17), esta geração passou a tratar as notas de devolução de mercadorias cuja saída tenha gerado ressarcimento/crédito de ICMS-ST. A partir destas devoluções, são gerados ajustes de estorno deste ressarcimento/crédito, e também lançamentos na Apuração do ICMS registrando os totais de ressarcimento e crédito estornados.

Alteração MFS9986 (Mar/17): Correção no cálculo da média dos valores das notas de entrada para a geração dos ajustes (problema identificado apenas nos casos de existir mais de uma entrada). Ver detalhes no item 3.

Alteração MFS11639 (Jun/17): Incluído o novo parâmetro “Tratamento das saídas com notas de entrada sem valor de ICMS-ST” (consultar os detalhes sobre a criação deste novo parâmetro no help).

Alteração MFS-20986 (Jan/19): Inclusão do campo 27 para informar o valor unitário destacado no documento fiscal de entrada a título de FCP ST ou valor unitário do FCP ST informado a título de reembolso.

Parâmetros da geração:




## Recuperação dos Dados e Processamento (C176)






Este processo será realizado apenas para os itens de documento fiscal que atendam aos seguintes critérios:

- Nota fiscal de saída;

- A data fiscal da nota deve ser referente ao período informado em tela (>= data inicial e <= data final);

- Modelo 01 ou 55;

- O item da nota deve ser um item de venda de produto sujeito a ST, cuja operação gera direito a ressarcimento. Esta condição é
identificada a partir da parametrização de CFOP, CFOP/NAT, Produtos e NCM’s, da seguinte forma:

(a partir da MFS2772 (Maio/26), a geração passou a utilizar também parametrização de CFOP, Produtos e NCM’s, além da parametrização de Natureza de Operação, já usada na versão original).





Obs:

- Além dos critérios descritos acima, a recuperação das notas e itens a serem processados segue as mesmas regras da recuperação das notas do C100 e C170. Observar que os documentos eletrônicos (modelo 55) normalmente, não terão os seus itens gravados no C170, mas, no caso dos itens com direito a ressarcimento de ST, eles serão gerados sim, para que o registro C176 possa ser gravado também (esta regra de exceção esta descrita no documento “Notas _Especiais_C100”).

- Quando o parâmetro “Geração p/Inscrição Estadual Única” for = “Sim”, a recuperação dos documentos fiscais será realizada para todos os estabelecimentos envolvidos na centralização, ou seja, o centralizador e os centralizados, de acordo com a parametrização de Inscrição Estadual Única do Módulo de Controle das Obrigações Estaduais.


Para cada item que atenda aos critérios acima, serão executados os seguintes passos:

Os passos a seguir descrevem como será feita a recuperação das notas de entrada referentes ao produto da nota de saída, e a utilização dos dados de cada entrada para gravar no C176. A informação chave para o tratamento das entradas é a quantidade, pois a busca será feita até que a quantidade da(s) entrada(s) atinja a quantidade da saída.

= = = = = = = =

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

Recuperar o documento de referência da base de dados e gravar as informações desta nota conforme descrito no item “7-Gravação
dos Dados” (item “Gravação dos Dados referentes ao registro C176”). Para a recuperação desta nota na base de dados, serão
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


Passo 3à Neste passo será feita a pesquisa na base de dados para recuperar a(s) última(s) nota(s) de entrada(s) do produto em questão, até que o total da quantidade de todas as notas de entrada atinjam a quantidade vendida do produto (quantidade da nota da venda, que aparecerá no C170). Para cada uma das notas recuperadas neste processo será gravado um registro na tabela auxiliar com as informações da nota, conforme descrito no item “7-Gravação dos Dados” (item “Gravação dos Dados referentes ao registro C176”).
[MFS-34480]: Particularmente para a UF = RS, a quantidade total das entradas gravadas na tabela auxiliar não pode exceder a quantidade da saída. O objetivo é que a soma das quantidades informadas no campo 07 do C176 seja igual à quantidade informada no campo 05 do C170 (pai dos C176). Sendo assim, a última nota de entrada recuperada que faz atingir a quantidade de saída, pode ter a quantidade gravada na tabela auxiliar reduzida. Por exemplo: Qtde NF Saída = 100. Já foram gravadas na tabela auxiliar notas de entrada cujo total da qtde = 60. A próxima nota de Entrada recuperada possui Qtde = 200.  Essa nota será gravada na tabela auxiliar com quantidade = 40 e não 200.
Para recuperar as notas da base de dados serão utilizados os critérios de pesquisa descritos no quadro abaixo “Critérios para recuperação das notas de entrada (Passo 3)”.








[MFS505030] Alteração da recuperação das notas fiscais de entrada para tratar a situação de incorporação de empresa.



Críticas a serem realizadas durante o processamento:

Para cada uma das situações descritas no quadro abaixo, será gerada a mensagem de aviso no log de erros:



Observações importantes:

Gravação do C176:

Ao gravar os dados de cada nota de entrada na tabela auxiliar, seguir as regras descritas no item “7-Gravação  dos Dados” (item “Gravação dos Dados referentes ao registro C176”).

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

Alteração da MFS11639: (passa a verificar o parâmetro “Tratamento das saídas com notas de entrada sem valor de ICMS-ST”)

Além da condição acima, quando o parâmetro “Tratamento das saídas com notas de entrada sem valor de ICMS-ST” estiver marcado, os ajustes serão gerados apenas se todas as entradas geradas para o item da saída em questão, tiverem o valor do ICMS-ST preenchido (ou seja, têm o campo “09-VL_UNIT_BC_ST” do C176 com um valor > zeros). Quando uma ou mais entradas não atenderem a esta condição, os ajustes não serão gerados.

Combinando os dois parâmetros, teremos:




Para cada item de nota fiscal de saída processado serão gerados um ou dois ajustes, um de ressarcimento, e outro de crédito, exceto quando se tratar de antecipação (quando o campo 18-COD_RESP_RET = 3), nesse caso os ajustes não serão gerados de acordo com as orientações do setor de informação.
Alteração da MFS8824 (Dez/2016): Conforme entendimento da Informação baseado na Portaria CAT 113/2016, os ajustes passarão a ser gerados normalmente para os casos de antecipação.

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





As informações a serem armazenadas para cada ajuste estão descritas no item “7-Gravação dos Dados” (no item “Gravação dos Dados referentes aos Ajustes (C195/C197)”);

Tratamento de erro: caso não exista o registro da parametrização a ser utilizada, os lançamentos não serão gerados, e no log será gravada a seguinte mensagem de erro: “Não existem dados da parametrização dos ajustes a lançamentos da Apuração do ICMS. Os ajustes não foram gerados”.



## Recuperação dos Dados e Processamento (Devoluções)


O tratamento das devoluções na pré-geração do C176 foi desenvolvido pela MFS9749.

Após o processamento das notas de saída, e a geração de seus respectivos ajustes de ressarcimento/crédito (conforme definido nos itens 2 e 3) , será feito o tratamento das devoluções. O objetivo é identificar as entradas por devolução de mercadorias que na saída geraram ajustes de ressarcimento / crédito, e gerar ajustes de estorno referentes às quantidades devolvidas.

OBS: A geração dos dados para ajustes de estorno (C195/C197) será executada apenas quando o parâmetro “Gerar os ajustes (C197) e os lançamentos complementares na Apuração do ICMS” estiver marcado. Mesmo procedimento adotado para os ajustes de ressarcimento/crédito.

Critérios para recuperação das notas de devolução e seus itens:

- Nota fiscal de entrada (campo Movimento E/S <> 9);

- Notas de devolução (campo Normal/Devolução = 2);

- A data fiscal da nota deve ser referente ao período informado em tela (>= data inicial e <= data final);

- O CFOP ou CFOP/Nat do item da nota deve constar na seguinte parametrização:



- O produto do item da nota deve ser um produto sujeito a ST, cuja operação gera direito a ressarcimento. Para isso, o produto
deve constar em uma das parametrizações disponíveis no módulo (Produtos e NCM’s):



Critérios para recuperação das saídas associadas a cada devolução:

Para cada item de devolução recuperado (conforme os critérios descritos acima), será feita a identificação das notas de saída que originaram a devolução.

Esta associação entre o item da devolução e as saídas é feita através da SAFX192. Nesta tabela, para cada item da devolução, são informadas as notas de saída de origem da mercadoria devolvida.

Critérios para identificar as saídas referentes ao item da devolução:

- Campos 01 a 15 da SAFX192 – considerar os campos chave do item da nota de devolução;
- Campo “16-Tipo de Referência” = 1 (“Port.CAT 158/15 - Devolução (E) x Documentos de Origem (S)”);

Com base nesses critérios de busca, poderão existir várias notas (itens) de saída associadas ao item da devolução.

Cada item de nota de saída referenciada será identificado pelos campos 17 ao 23.

Críticas em relação ao item da devolução x saídas referenciadas na SAFX192:


Após a recuperação dos dados dos itens de devolução, das notas de saída referenciadas na SAFX192, o cálculo e geração dos ajustes de estorno serão feitos conforme descrito no item a seguir.


## Recuperação dos Dados e Processamento (Ajustes de Estorno das Devoluções)


Para cada item de devolução:

O cálculo dos estornos é feito por item de devolução, a partir das respectivas saídas referenciadas (SAFX192), da seguinte forma:

Para cada saída referenciada será calculado um valor de estorno (para ressarcimento e para crédito), e ao final do cálculo de todas as saídas, o valor dos ajustes de estorno do item de devolução, será o total de todas as saídas.

Estes estornos são calculados com base nos ajustes originais gerados para as saídas.

(verificar exemplos na planilha “MTZ-EFD-Pre_Geracao_Registro_C176_Exemplo_Devolucoes”)

Para cada item de saída referenciado:

Como identificar os ajustes de ressarcimento/crédito da saída:

Como dito acima, os estornos serão calculados saída a saída, baseado nos ajustes originais de ressarcimento e crédito.

Para recuperar estes ajustes na SAFX113, deve-se considerar:



OBS: Quando os ajustes de ressarcimento e/ou crédito de uma determinada saída (SAFX192) não forem identificados na SAFX113, o procedimento será o seguinte:
- Os valores de estorno referentes a esta saída não serão calculados;
- A saída será considerada normalmente no processo, apesar de não gerar valores para estorno. A intenção é que esta saída seja
demonstrada normamente no relatório de conferência das devoluções. Assim, o usuário poderá visualizar que ela foi associada à uma
devolução, mas como não existem os ajustes originais do ressarcimento/crédito, os valores de estorno não foram calculados;

Como calcular os valores de estorno:

Verificar se a quantidade de devolução informada na nota referenciada (SAFX192, campo 24-Quantidade da Devolução) é igual a quantidade da saída (X08).

Caso sim à Nesse caso, o valor do estorno do ressarcimento e crédito será exatamente igual ao valor do ajuste gerado na saída. O mesmo se aplica ao valor da base de cálculo e da alíquota do ajuste.

Ver planilha de exemplos, aba “Exemplo 1”: Este é o exemplo do item 1 da nota de devolução 888. Observar que na saída referenciada (SAFX192) a quantidade de devolução informada (40) é a mesma quantidade que consta no item da nota fiscal da saída (SAFX08). Por isso, o valor do estorno deste item de devolução serão exatamente os mesmos dos ajustes originais gerados para a saída (Ressarcimento de 500,00 e Crédito de 140,00).

Caso não à Nesse caso, o valor do estorno será calculado de forma proporcional à quantidade da devolução, e o mesmo procedimento também se aplica ao valor da base de cálculo. Já a alíquota será sempre a mesma do ajuste original.

Neste caso, será necessário calcular qual é o valor unitário do ajuste gerado para a saída, e depois aplicar este valor unitário sobre a quantidade de devolução do item referenciado (SAFX192).

Como exemplo, vide o item 2 da nota de devolução abaixo:




A quantidade da devolução foi = 5,

Já a quantidade do item da saída foi = 10,

Desta forma, teremos:

Cálculo do valor unitário dos ajustes, com base no valor do ajuste da saída:

Valor Unitário do Ajuste de Ressarcimento: ICMS = 1200,00 / 10 = 120,0000
Base = 24000 / 10 = 2400,0000

Valor Unitário do Ajuste de Crédito: ICMS = 800,00 / 10 = 80,0000
Base = 8000 / 10 = 800,0000


(para obter maior precisão, o cálculo do valor unitário pode ser feito com 4 casas decimais)

Para calcular qual será o valor a ser estornado, basta multiplicar o valor unitário pela quantidade de devolução do item de referência (ou seja, da SAFX192):

Valor do estorno do ajuste de ressarcimento: ICMS = 120,0000 * 5 = 600,00
Base =  2400,0000 * 5 = 12.000,00

Valor do estorno do ajuste de crédito: ICMS = 80,0000 * 5 = 400,00
Base = 800,0000 * 5 = 4.000,00

Ver detalhes deste exemplo na planilha de exemplos, aba “Exemplo 1”: Este é o exemplo do item 2 da nota de devolução 888. Observar que na saída referenciada (SAFX192) a quantidade de devolução informada (5) é INFERIOR a quantidade que consta no item da nota fiscal da saída (SAFX08, qtd = 10). Por isso, foi necessário calcular o valor do estorno, a partir do valor unitário do ajuste original, gerado na saída da mercadoria. Assim, o valor do estorno deste item de devolução foi inferior ao valor dos ajustes originais (Ressarcimento de 600,00 e Crédito de 400,00), gerados para a saída, já que a devolução não foi da quantidade integral.

Na aba “Exemplo 1” estão os exemplos mais simples.

Já na aba “Exemplo 2” estão os exemplos mais complexos, como por exemplo, quando um item de devolução é originado de várias notas de saída diferentes.


Sobre a alíquota do ajuste:

A alíquota do ajuste de estorno será sempre a mesma alíquota do ajuste original gerado para a operação de saída. Quando um item de devolução for originado de vários itens de saída, os valores (ICMS e Base) do estorno serão calculados para cada saída separadamente, e depois o estorno final será a somas dos valores obtidos para cada saída. Mas a alíquota será sempre a mesma, já que “teoricamente” as saídas terão a mesma alíquota.

Observação sobre conversão de medida:

Neste processo de cálculo dos estornos das devoluções não será necessário efetuar nenhum tipo de conversão de medida, pois a quantidade informada na SAFX192 (campo 24-Quantidade da Devolução) já é obrigatoriamente na unidade de medida utilizada na saída (conforme orientações do Manual de Layout).

Gravação dos Ajustes de Estornos calculados para cada item de devolução:

Os ajustes de estornos calculados para cada item da nota de devolução serão gravados (SAFX113) para posteriormente serem utilizados na geração do Sped Fiscal.

As informações a serem armazenadas para cada ajuste estão descritas no item “7-Gravação dos Dados” (no item “Gravação dos Dados referentes aos Ajustes de Estorno das Devoluções (C195/C197)”);

## Recuperação dos Dados e Processamento (Lançamento na Apuração do ICMS)


A geração dos lançamentos complementares na Apuração do ICMS será executada apenas quando o parâmetro “Gerar os ajustes (C197) e os lançamentos complementares na Apuração do ICMS” estiver marcado.

Para cada estabelecimento processado poderão ser gerados até cinco lançamentos, da seguinte forma:

- Um lançamento com o valor total de todos os ajustes de ressarcimento;
- Um lançamento com o valor total de todos os ajustes de crédito;
- Um lançamento com o valor total de todos os ajustes de estorno de ressarcimento (devoluções);     (MFS9749)
- Um lançamento com o valor total de todos os ajustes de estorno de crédito (devoluções);                 (MFS9749)
- Um lançamento estornando o ressarcimento do primeiro lançamento. Este lançamento é sobre o valor de ressarcimento total
que deve ser transferido p/o registro 1200 da EFD. Seu valor será: valor do primeiro lançamento – valor do terceiro lançamento.
(MFS8892/MFS9749)

Cada um destes lançamentos só será gerado quando o seu respectivo total for <> zeros.

Alteração da MFS8892: Se for gerado o lançamento para o total dos ajustes de ressarcimento, será gerado também um lançamento para estornar este valor, pois a orientação da Portaria CAT 113/2016 é que o total de ressarcimento seja transferido para o registro 1200 (Controle de Créditos).

Alteração da MFS9749: Quando forem gerados ajustes de estorno de ressarcimento/crédito decorrente das devoluções (conforme itens 4 e 5), serão gerados também mais dois lançamentos, um para o total dos estornos de ressarcimento, e outro para o total dos estornos de crédito.

Alteração da MFS47510: Os valores de ajuste referentes a códigos de ajustes em que o terceiro caracter igual a “9” (=Informativo) E o quarto caracater iguais a “9” (=Informativo), não devem ser considerados no cálculo dos lançamentos complementares.  Pois, conforme é informado na legislação do RS, os códigos iniciados por “RS9999”, são códigos informativos que não impactam a apuração.  Ou seja, todos os valores de ajuste referentes a estes códigos não devem compor o valor do lançamento.  Esta regra serve para qualquer ajuste (ajustes de ressarcimento, ajustes de crédito...) que será lançado na apuração do ICMS.



Assim, após o processamento de cada estabelecimento, este processo será executado para a gravação dos lançamentos, que será realizada da seguinte forma:

Os parâmetros para gravação dos lançamentos serão recuperados do item de menu “Parâmetros à Registro C176 à Parâmetros p/Geração dos Ajustes e Lançamentos”, considerando o estabelecimento da geração. No caso de geração por inscrição estadual única, será sempre utilizada a parametrização do estabelecimento centralizador (estabelecimento selecionado na tela da geração);


O valor de cada um destes lançamentos é calculado da seguinte forma:



As informações a serem armazenadas para cada lançamento estão descritas no item “7-Gravação dos Dados” (no item “Gravação dos Dados referentes aos Lançamentos Complementares da Apuração do ICMS”);

Tratamento de erro: caso não exista o registro da parametrização a ser utilizada, os lançamentos não serão gerados, e no log será gravada a seguinte mensagem de erro: “Não existem dados da parametrização dos ajustes a lançamentos da Apuração do ICMS. Os lançamentos não foram gerados”.



## Gravação dos Dados



Os dados gerados para o registro C176, C197 (ajustes) e lançamentos complementares serão armazenados e posteriormente utilizados na geração do Sped Fiscal.

As informações a serem armazenados para cada caso, serão descritas nos itens a seguir:

- Gravação dos Dados referentes ao Registro C176

- Gravação dos Dados referentes aos Ajustes (C195/C197)

- Gravação dos Dados referentes aos Ajustes de Estorno das Devoluções (C195/C197)        (MFS9749)

- Gravação dos Dados referentes aos Lançamentos Complementares da Apuração do ICMS



Gravação dos Dados referentes ao Registro C176:

Segue descrição das informações a serem armazenadas para posterior gravação do registro C176 na geração do Sped Fiscal:

Observar que além destes dados também deverão ser armazenadas todas as referências da nota fiscal de saída, e seu respectivo item a qual o C176 pertence, lembrando que o registro C176 é “filho” do registro de itens da nota (C170).





Gravação dos Dados referentes aos Ajustes (C195/C197):

Segue descrição das informações a serem armazenadas para posterior gravação dos registros C195 e C197 na geração do Sped Fiscal.

Estas informações serão gravadas nas tabelas SAFX específicas para geração destes registros do Sped Fiscal. São elas:

SAFX112 – OBSERVAÇÕES DA NOTA FISCAL (corresponde ao C195, registro “filho” do C100);
SAFX113 – AJUSTES DO LANÇAMENTO FISCAL (corresponde ao C197, registro “filho” do C195);

Observar que além dos dados descritos abaixo, a SAFX112 também possui todas as referências da nota fiscal de saída a qual a observação pertence.

Da mesma forma, além dos dados descritos abaixo, a SAFX113 também possui todas as referências da observação (SAFX112) a qual o ajuste estará vinculado, já que a SAFX113 é uma tabela “filha” da SAFX112 (assim como o registro C197 é um registro “filho” do C195).

Sobre a parametrização (item Parâmetros à Registro C176 à Parâmetros p/Geração dos Ajustes e Lançamentos):

Observar que a parametrização para geração destas informações contém os dados específicos para os ajustes de ressarcimento e os  ajustes de crédito. No entanto, é possível que o usuário informe o mesmo código de observação a ser utilizada nos dois casos. Quando isso ocorrer, obviamente que será gravado apenas um registro na SAFX112, uma vez que o código da observação é chave. Da mesma forma, nada impede que a observação parametrizada possa já existir para a nota fiscal em questão. Estas duas situações devem ser previstas na geração.

Nos ajustes de ressarcimento:


- Informações da Observação (SAFX112) p/o C195:



- Informações do Ajuste (SAFX113) p/o C197:



Nos ajustes de crédito:


- Informações da Observação (SAFX112) p/o C195:



- Informações do Ajuste (SAFX113) p/o C197:




Gravação dos Dados referentes aos Ajustes de Estorno das Devoluções (C195/C197):

A gravação dos ajustes de estorno a partir das devoluções segue as mesmas orientações sobre a SAFX112 e SAFX113 descritas para os ajustes anteriores (ajustes de ressarcimento/créditovinculados à nota de saída).

Estes ajustes de estorno ficam vinculados à nota de devolução.

Nos ajustes de estorno do ressarcimento:


- Informações da Observação (SAFX112) p/o C195:



- Informações do Ajuste (SAFX113) p/o C197:



Nos ajustes de estorno do crédito:


- Informações da Observação (SAFX112) p/o C195:



- Informações do Ajuste (SAFX113) p/o C197:





Gravação dos Dados referentes aos Lançamentos Complementares da Apuração do ICMS:

Os lançamentos serão gravados na Tabela dos Lançamentos Complementares da Apuração do ICMS.

Para cada um dos lançamentos a seguir, serão descritos as informações a serem gravadas:

- Lançamento de Ressarcimento
- Lançamento de Crédito
- Lançamento de Estorno do Ressarcimento (Devoluções)     (MFS9749)
- Lançamento de Estorno do Crédito (Devoluções)                 (MFS9749)
- Lançamento de Estorno do Ressarcimento (referente ao valor a ser transferido p/o registro 1200)  (MFS8892/MFS9749)


Informações do Lançamento de Ressarcimento:




Informações do Lançamento de Crédito:




Informações do Lançamento de Estorno do Ressarcimento (Devoluções):      (lançamento criado pela MFS9749)





Informações do Lançamento de Estorno do Crédito (Devoluções):                   (lançamento criado pela MFS9749)





Informações do Lançamento de Estorno do Ressarcimento (referente ao valor a ser transferido p/o registro 1200):

(Lançamento criado pela MFS8892)





Observações importantes sobre a gravação dos lançamentos:

Observar que para os lançamentos do tipo “1”, como é o caso dos lançamentos que serão gravados, existe uma associação entre o lançamento e os ajustes que originaram o lançamento. Para isso, existe uma tabela interna que tem este relacionamento, para que na tela de manutenção dos lançamentos sejam exibidos todos os ajustes vinculados ao lançamento. Esta tabela também será alimentada neste processo para que o lançamento a ser gerado fique corretamente associado a todos os ajustes da SAFX113 que o originaram (conforme as regras descritas nos itens anteriores). No caso, para o lançamento de ressarcimento, serão todos os ajustes de ressarcimento que foram totalizados para compor o seu valor, e a mesma coisa para o lançamento de crédito. O mesmo acontecerá para os lançamentos referentes aos ajustes decorrentes das devoluções: para o lançamento de estorno de ressarcimento (devoluções), serão todos os ajustes de estorno de ressarcimento que foram totalizados para compor o seu valor, e a mesma coisa para o lançamento de estorno de crédito.

(este procedimento é padrão para geração automática de lançamentos complementares)

Antes de gerar os lançamentos, será realizado procedimento de limpeza dos lançamentos que possam já ter sido gerados anteriormente por este mesmo processo.  Este procedimento é necessário por causa das situações de reexecução do processo em um mesmo período. Para efetuar a limpeza, considerar os campos de identificação do lançamento (empresa, estabelecimento, obrigação fiscal e data da apuração), e também o indicador próprio criado para estes lançamentos (IND_DIG_CALCULADO = “C”).



## Emissão do Relatório


Na aba “Relatório” será emitido um relatório de conferência dos dados gerados.

O usuário poderá visualizar o relatório logo após a geração, e também posteriormente, selecionando uma geração já executada na aba “Processos”.

Ver layout na planilha anexa “Layout-Conferencia-PreGeracao-do-C176_A_partir_Jan2017”.

Regras do preenchimento dos dados:

Para cada item de saída processado, serão demonstradas as entradas consideradas para geração do C176.

Para cada nota de entrada considerada, serão demonstrados os dados básicos de identificação, e ao final da linha, os dois valores calculados para geração do registro C176: campo “15-Valor Unitário do crédito de ICMS” e campo “17-Valor Unitário do ressarcimento”.

(Observar que o layout mostra o número do item da nota, e assim, caso ocorra à situação de numa mesma nota de entrada, existirem dois itens de mesmo produto recuperados, cada um deles será gerado numa linha do relatório).

Após a exibição de todas as notas de entrada referentes ao item de saída, serão demonstrados os dois ajustes (C197) gerados para o item: o ressarcimento e o crédito.

Ao final de todas as notas de saída de um determinado Estabelecimento, será demonstrado o valor total de ressarcimento e o valor total de crédito, valores estes originaram os lançamentos de forma automática na Apuração do ICMS do estabelecimento.

Várias colunas do relatório trabalham com letras para identificação da coluna. Este recurso foi utilizado para demonstrar o cálculo realizado na apuração de alguns valores importantes, como por exemplo, os valores gerados para o registro C176, e também os ajustes do C197. Desta forma, o usuário poderá verificar como os cálculos foram realizados.

Obs: Todas as informações do relatório são as informações já descritas e detalhadas nos itens deste documento referentes à recuperação e processamento dos dados, por isso, as regras de preenchimento abaixo não detalham tabelas, numeração de campos, etc.

Linha de identificação do item da nota de saída:




Linhas das notas fiscais de entrada associadas ao item da saída:




Linhas de total das entradas demonstradas:







Linhas dos ajustes gerados para o item da saída:


Alteração da MFS11639:
No quadro que demonstra os dados dos ajustes gerados (Ressarcimento e Crédito), será impressa uma observação na mesma linha do titulo do quadro (“Ajustes gerados p/o item (C197)”). Esta observação será gerada apenas quando o conteúdo da coluna “Indicador de Gravação na EFD” das linhas referentes à saída em questão, for = “N” (lembrando que todas as linhas referentes à um único item de saída, terão sempre o mesmo conteúdo nesta coluna).

Ex:











Linhas dos totais do Estabelecimento:





## Emissão do Relatório das Devoluções


Na aba “Relatório - Devoluções” será emitido um relatório de conferência dos dados gerados a partir das notas de devolução processadas no período.

Esta aba foi criada na MFS9855 para demonstrar os ajustes de estorno do ressarcimento/crédito gerados para cada nota de devolução.

O usuário poderá visualizar o relatório logo após a geração, e também posteriormente, selecionando uma geração já executada na aba “Processos”.

Ver layout na planilha anexa “Layout-PreGeracaoC176-Conf-Devolucoes”.


Regras do preenchimento dos dados:

Para cada item de DEVOLUÇÃO processado, serão demonstradas as notas fiscais de saídas referenciadas na SAFX192. Para cada saída referenciada, serão demonstrados os dados básicos de identificação do item, a quantidade devolvida informada na SAFX192, e ao final da linha, os valores dos respectivos ajustes de ressarcimento/crédito (SAFX113).

Após cada saída, será gerada uma linha demonstrando os valores de estorno calculados com base na quantidade devolvida.

Após a exibição de todos os itens de saída associados à uma devolução, serão demonstrados os dois ajustes de estorno (C197) gerados para o item da devolução: o ressarcimento e o crédito.

Ao final de todas as notas de DEVOLUÇÃO de um determinado Estabelecimento, será demonstrado o valor total de estorno do ressarcimento e o valor total de estorno do crédito (estes valores que originaram os lançamentos na Apuração do ICMS do estabelecimento).

OBS: Todas as informações do relatório são as informações já descritas e detalhadas nos itens deste documento referentes à recuperação dos dados e processamento das devoluções (itens 4 e 5) , por isso, as regras de preenchimento abaixo não detalham tabelas, numeração de campos, etc.

Linha de identificação do item da nota de DEVOLUÇÃO:





Linha de identificação das notas fiscais de SAÍDA associadas ao item da DEVOLUÇÃO:




Linha dos valores de estorno calculados p/cada saída:     (“Valores a serem estornados referentes à quantidade devolvida”)

Esta linha demonstra os valores de estorno do ressarcimento e do crédito calculados para a saída demonstrada na linha anterior. Estes valores são calculados conforme descrito no item “5-Recuperação dos Dados e Processamento (Ajustes de Estorno das Devoluções)”.





Linha dos ajustes de estorno gerados p/a devolução:      (“Ajustes de estorno gerados p/o item da devolução”)

Nas linhas “Ressarcimento” e “Crédito” serão demonstrados os valores dos ajustes de estorno gerados para a nota de devolução. Estes valores são o resultado total dos estornos calculados para todas as saídas associadas à nota de devolução. Estes resultados são calculados conforme descrito no item “5-Recuperação dos Dados e Processamento (Ajustes de Estorno das Devoluções)”.





Linhas dos totais do Estabelecimento:                (“Total dos Ajustes de Estorno do Estabelecimento”)

Nestas linhas serão demonstrados os valores totais de estorno de ressarcimento e de crédito gerados para o estabelecimento.




= = = = = =



| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| OS2388-N1-A | Reformulação do C176 - GP Vrs 1.0.4 (Maio/2009) | Criação de uma rotina preliminar para gerar os dados do registro C176, conforme as alterações divulgadas pelo Guia Prático vrs 1.0.4 (Maio/2009) . (este documento é a transcrição das regras especificadas na época, na OS2388-N1-A) | 19/04/2016 (criação do documento) |
| MFS2772 | Atendimento a Portaria CAT 158 | Para atendimento a Port. CAT 158 esta geração passou a gerar também os ajustes (C195/C197) e lançamentos complementares na Apuração do ICMS, referentes aos valores apurados para o registro C176, e também a emitir um relatório de conferência dos valores apurados. | 30/05/2016 |
| MFS6677 | Atendimento ao Ato Cotepe 07/2016 | Para atendimento a Ato Cotepe 07/2016 foram incluídos mais 16 campos referentes aos valores apurados e informações das notas para o registro C176, e também emitir um novo relatório de conferência dos valores apurados para as novas informações do registro. | 26/09/2016 |
| MFS6746 | Conversão de Medida | Alteração na geração do C176 p/tratar conversão de medida entre entrada x saída | 07/11/2016 |
| MFS8795 | Portaria CAT 112/2016 | Dispensa dos campos 20 ao 24 do C176 (ver item 5) | 26/12/2016 |
| MFS8824 | Alteração p/os casos de antecipação (Portaria CAT 112/2016) | Alteração para gerar os ajustes (C197) também nos casos de antecipação | 28/12/2016 |
| MFS8892 | Novos parâmetros | Portaria CAT 113/16: criação de parâmetros p/o lançamento de estorno de ressarcimento | 30/12/2016 |
| MFS9068 (ch345/17) | Alteração na geração do campo 19 | Alteração na geração do campo 19-COD_MOT_RES | 09/01/2017 |
| MFS8968 (ch27247) | Alteração na geração do campo 12 | Alteração na geração do campo 12 | 11/01/2017 |
| MFS9275 (CH766) | Alteração no campo 14 | Alteração na descrição da mensagem de erro do campo 14 | 25/01/2017 |
| MFS9753 (CH26567-A) | Alteração na geração do campo 14 | Alteração na geração do campo 14 | 21/02/2016 |
| MFS9749 | Tratamento das Devoluções | Portaria CAT 112/16: Tratamento das devoluções (geração dos ajustes de estorno e dos lançamentos referentes às devoluções de mercadorias). | 21/02/2017 |
| MFS9855 | Tratamento das Devoluções | Criação da aba “Relatório – Devoluções” para a conferência das notas de devolução processadas no período. | 03/03/2017 |
| MFS9986 (Ch 2107/17) | Correção na geração dos ajustes | Correção no cálculo da média dos valores das notas de entrada para a geração dos ajustes (problema identificado apenas nos casos de existir mais de uma entrada). | 15/03/2017 |
| MFS10355 (ch 5505/17) | Alteração na geração do campo 14 | Alteração na geração do campo 14 p/os casos de antecipação. | 07/04/2017 |
| MFS11639 | Criação de um novo parâmetro | Alteração na geração do C176 p/a utilização do novo parâmetro “Tratamento das saídas com notas de entrada sem valor de ICMS-ST”. | 13/06/2017 |
| MFS12341 (CH13076_2017) | Criação de tratamento do campo 15 | Criação de tratamento para gerar vazio no campo 15 - VL_UNIT_ICMS_ULT_E quando o valor for igual a ‘0’. | 19/07/2017 |
| CH1720_2018 (MFS-16346) | Tratamento no campo 17 | Tratamento no campo 17 do Registro C176 para valores calculados com resultado negativo. | 01/02/2018 |
| MFS18752 | Alteração na recuperação das notas fiscais de entrada | Alteração para que as entradas sejam identificadas não apenas pelo código do produto da nota de saída, como também pelo código anterior registrado na SAFX2013, quando for o caso. | 07/08/2018 |
| MFS-20986 | Ato Cotepe n° 44/2018 | Criação do campo 27- VL_UNIT_RES_FCP_ST. | 01/01/2018 |
| MFS32699 | Tratamento no campo 09 | Alteração no campo 09 do Registro C176 para tratar crítica dada no validador do SPED-EFD, quanto ao campo 14: Validação: o valor informado no campo 14 deve corresponder ao menor valor entre os campos 09 - VL_UNIT_BC_ST e 12 - VL_UNIT_BC_ICMS_ULT_E. | 12/2019 |
| MFS-34128 | Tratamento no campo 12 | Alteração no campo 12 do Registro C176 para tratar crítica dada no validador do SPED-EFD, quanto ao campo 14: Validação: o valor informado no campo 14 deve corresponder ao menor valor entre os campos 09 - VL_UNIT_BC_ST e 12 - VL_UNIT_BC_ICMS_ULT_E. | 19/06/2020 |
| MFS-34480 | Tratamento na Qtde Entrada | Tópico 2 – Recuperação dos Dados e Processamento (C176) – PASSO3: Tratamento para UF = RS: Na busca das últimas notas de entrada a fim de atingir a quantidade da NF de Saida, realizar um tratamento para que o total da quantidade das notas de entradas não supere a quantidade da saída. | 21/09/2020 |
| MFS47427 | Andréa Rocha | Alteração da descrição de uma opção do campo Código do motivo do ressarcimento | 11/12/2020 |
| MFS47510 | Andréa Rocha | Alteração na forma de gerar os lançamentos complementares na apuração do ICMS para não considerar os códigos de ajuste em que o terceiro e o quarto caracter do código forem iguais a 9.  Alteração feita baseada na legislação do RS, que determina que estes códigos devem ir para o registro C197 e não devem impactar a apuração do ICMS, pois são códigos informativos. | 08/01/2021 |
| MFS47166 | Rogério Ohashi | Alteração no campo “06- COD_PART_ULT_E” do registro C176 para tratamento dos cenários de Notas Fiscais Emitidas pelo próprio Estabelecimento, acolhendo Notas de Produtores Rurais (Campo Movimento de Entradas /ou Saídas igual a “2”). Solicitação do Cliente Zaffira devido erro no validador PVA. | 25/01/2021 |
| MFS60490 | Rogério Ohashi | Alteração no campo “16- ALIQ_ST_ULT_E” do registro C176, para recuperar a Alíquota Interna parametrizada na Tela de “Parâmetros > Registro C176 > Produto ou NCM´s”, conforme a data da Nota Fiscal de Entrada. | 18/03/2021 |
| MFS71627 | Andréa Rocha | Alteração no tratamento do campo 14-VL_UNIT_LIMITE_BC_ICMS_ULT_E, quando o campo 18-COD_RESP_RET for igual a “1”.  A alteração é necessária devido ao erro dado no validador, o valor do campo 14 deve ser o menor valor entre os campos VL_UNIT_BC_ST e VL_UNIT_BC_ICMS_ULT_E. | 20/09/2021 |
| MFS-73699 | Liliane Assaf | Ato Cotepe 62/2021, novo leiaute EFD115 (versão 1.15, Jan/2022): - Alteração na regra de preenchimento do campo 18- COD_RESP_RET para tratamento do novo código “4” – Remetente Direto Simples Nacional. | 27/10/2021 |
| MFS-85388 | Aline Melo | Ato Cotepe 21/2022, novo leiaute EFD116 (versão 1.16, Jan/2023): Alteração na regra do campo 14, inclusão da exigência do campo COD_RESP_RET igual a “2 – Remetente Indireto”. | 11/05/2021 |
| MFS523539 | Andréa Rocha | Alteração no tratamento do campo 27-VL_UNIT_RES_FCP_ST,  quando a UF do estabelecimento for igual a “RS”.  A alteração é necessária devido ao erro dado no validador, que diz que deve ser preenchido com zeros. | 31/03/2023 |
| MFS528854 | Andréa Rocha | Alteração na regra de recuperação da parametrização por produto/NCM para verificar a data da nota fiscal de entrada | 18/04/2023 |
| MFS505030 | Andréa Rocha | Alteração na regra de recuperação das notas fiscais de entrada para tratar a situação  de incorporação de empresa. | 26/09/2023 |
| MFS637814 | Graciela Soares | Alteração na regra de recuperação das notas fiscais para tratar os campos CHAVE_NFE_RET, COD_PART_NFE_R ET, SER_NFE_RET, NUM_NFE_RET, ITEM_NFE_RET para atendimento ao Rio de Janeiro. | 09/05/2024 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Data Inicial | Data | S | S |  | Neste campo o usuário informará a data inicial do período da geração. Válidos a partir de Jan/2017 para nova geração. |  |
| Data Final | Data | S | S |  | Neste campo o usuário informará a data final do período da geração. |  |
| Pesquisar últimas entradas até | Data | S | S |  | Neste campo é informada a data limite até onde será feita a pesquisa das últimas notas de entrada do produto.  Obs: Esta pesquisa é feita desde a data da venda (data da NF da venda) até a data limite informada, sendo que ao atingir a quantidade da venda a pesquisa é interrompida. Assim, esta data é apenas um limite “genérico” para os casos em que as entradas não sejam encontradas (para evitar que a pesquisa seja feita indeterminadamente). |  |
| Gerar os ajustes (C197) e os lançamentos complementares na Apuração do ICMS | Alfanumérico | N | S | Default:   Desmarcado | Este campo é um checkbox onde o usuário poderá optar em gerar ou não os dados para os ajustes do C197 e os lançamentos da Apuração do ICMS. | (parâmetro criado na MFS2772) |
| Tratamento das saídas com notas de entrada sem valor de ICMS-ST | Alfanumérico | N | S | Default:   Desmarcado | Este campo é um checkbox onde o usuário informa se as saídas com entrada(s) sem valor de ICMS-ST, terão ou não os ajustes do C197 gerados. (ver help do parâmetro) | (parâmetro criado na MFS11639) |
| Considerar as notas fiscais da empresa incorporada | Alfanumérico | N | S | Default:   Desmarcado | Este campo é um checkbox onde o usuário informa se vai considerar as notas fiscais de entrada da empresa incorporada, além das notas fiscais da empresa/estabelecimento da geração. | (parâmetro criado na MFS505030) |
| Geração p/Inscrição Estadual Única | Alfanumérico | N | S | Default:   Opção “Não” | Este campo apresenta duas opções:   - Sim - Não  As opções são alternativas.  A opção informada interfere no campo “Estabelecimentos”, conforme descrito na regra específica. |  |
| Estabelecimentos | Alfanumérico | S | Ver regra |  | Neste campo será exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário.  A exibição dos estabelecimentos depende da opção informada no campo “Geração p/Inscrição Estadual Única”, da seguinte forma:  Se = “Sim” à Neste caso, serão exibidos apenas os estabelecimentos centralizadores, conforme a parametrização da Inscrição Estadual Única no módulo de Controle das Obrigações Estaduais;   Se = “Não” à Neste caso serão exibidos todos os estabelecimentos da empresa;  Sempre que a opção do campo “Geração p/Inscrição Estadual Única” for alterada, esta lista será refeita dinamicamente, considerando a nova opção. |  |


| Visão resumida do processo:  O processo identifica as notas fiscais de saída do período, com direito à ressarcimento de ICMS-ST. Para cada item identificado, será realizada a busca das últimas entradas do produto até atingir a quantidade da saída. O processo é complexo, e se resumo na seguinte lógica:  Se o item da saída tiver a informação do documento fiscal de referência preenchido:       Neste caso, a busca da última entrada será feita acessando diretamente o documento informado como referência.       Se a quantidade deste documento de entrada já cobrir a quantidade da nota da saída,           Neste caso a pesquisa já estará concluída, e os dados serão gerados apenas com base nesta entrada;      Senão,           A pesquisa prossegue na busca das outras entradas anteriores até que a quantidade da saída seja atingida; (*)  Senão (não existe a informação do documento fiscal de referência)       Neste caso, será realizada a pesquisa das últimas entradas do produto, desde a data da venda (data da NF da venda) até a data limite informada em tela, até que a quantidade da saída seja atingida; (*)  Os dados de cada nota de entrada identificada serão gravados numa tabela auxiliar, com todas as informações solicitadas no registro C176, estas informações serão utilizadas posteriormente na gravação do arquivo do Sped Fiscal.  (*) Para UF = RS, a quantidade total das entradas recuperadas não pode exceder a quantidade da saída. A soma das quantidades informadas no campo 07 do C176 deve ser igual à quantidade informada no campo 05 do C170 (pai dos C176). |
| --- |


| O CFOP ou o CFOP/NAT do item deve estar parametrizado:       O CFOP do item deve constar da parametrização do menu “Parâmetros à Registro C176 à NF’s Saída c/direito a        Ressarcimentoà CFOP” do módulo EFD”;       ou       O CFOP/Natureza de Operação do item deve constar da parametrização do menu “Parâmetros à Registro C176 à NF’s      Saída c/direito a Ressarcimentoà CFOP / Natureza de Operação” do módulo EFD”;  [MFS528854] Alteração da regra para identificar a data de validade da parametrização de produto  O Produto ou o seu NCM deve estar parametrizado:        O produto do item deve constar da parametrização do menu “Parâmetros à Registro C176 à Produtos” do módulo       EFD”;        ou        O NCM do produto do item deve constar da parametrização do menu “Parâmetros à Registro C176 à NCM’s” do       módulo EFD”;  Na pesquisa da parametrização dos Produtos / NCM’s, poderão existir várias parametrizações válidas para o Estabelecimento e período em questão, pois esta parametrização é por Estab/Grupo/Aliq/Validade.  Serão pesquisadas as parametrizações existentes para o Estabelecimento em questão, Grupo válido para o período da geração, e cuja validade atenda ao período da geração, ou seja:  - tenha validade inicial <= ao último primeiro dia do período da geração; - se a validade final estiver preenchida, ela deve ser uma data >= ao último dia do período da geração;  Observação sobre a data de validade da parametrização:  Para identificar a data de validade da parametrização, deve-se verificar a regra do preenchimento do campo Alíquota do ICMS ST relativa à última entrada da mercadoria, que tem maiores detalhes sobre a verificação das datas de validade em relação às datas das notas.  Basta que o Produto, ou o seu NCM, conste em qualquer uma das parametrizações válidas para o período.  Obs: A alíquota interna da parametrização onde o produto, ou seu NCM foi identificado, será utilizada posteriormente para o cálculo do ajuste de crédito (cálculo definido no item “3-Recuperação dos Dados e Processamento (Ajustes C195/C197)”). |
| --- |


| Critérios para obter o documento de referência (Passo 1) |
| --- |
| O documento de referência deve ser recuperado na base de dados a partir dos critérios descritos abaixo:   - nota fiscal de entrada (MOVTO_E_S  <> ‘9’); - número da nota = conteúdo do campo 117 da SAFX08; - série da nota      = conteúdo do campo 118 da SAFX08; - subsérie da nota = conteúdo do campo 119 da SAFX08; - data de emissão da nota = conteúdo do campo 102 da SAFX08;  - produto = produto do item da nota de venda (ver OBS abaixo);    OU    (produto = indicador e código anterior do produto do item da nota de venda e data de emissão da nota de referência < data da     alteração do código do produto do item da nota de venda)  Alteração MFS18752 (Ago/2018): a busca do item da nota de entrada passou a ser feita considerando o código do produto da nota de venda, ou, o código anterior do produto registrado na SAFX2013, quando for o caso. Mas, o código anterior só será considerado nos casos em que a nota de entrada for de uma data anterior a data da alteração do código registrada na SAFX2013.Desta forma, essa nova condição se baseia nos seguintes campos do cadastro do produto da saída: campos “42-Indicador Anterior”, “43-Código Anterior” e “44-Data da Alteração” da SAFX2013 (observar que o campo do código anterior do produto poderá estar nulo, e assim, só deve ser utilizado quando preenchido).  Considerar a necessidade de pesquisar esta nota nas tabelas normais (X07/X08), já que a nota fiscal poderá estar num período anterior ao período da movimentação gerada no Datamart;  OBS: Caso no documento encontrado exista mais de um item do mesmo produto, deve-se totalizar as quantidades e as bases de cálculo de todos os itens, e o campo VL_UNIT_BC_ST deve ser calculado a partir das bases e quantidades já totalizadas, conforme descrito no item “7-Gravação  dos Dados” (item “Gravação dos Dados referentes ao registro C176”).   Crítica a ser realizada:  Caso a nota de referência não seja encontrada na base de dados, será gravada a seguinte mensagem no log:      “O documento de referência indicado no item da nota não foi encontrado na base de dados. O registro C176 não foi gerado”.   Na planilha de erros “Sped_Fiscal_Log_Erros” esta é a mensagem de número 61. Na linha “Dados do Registro” deve ser exibida a identificação da nota de ressarcimento, o item da nota em questão, e também os dados do documento fiscal de referência (Num/Ser/Sub/Dt Emis). |


| Critérios para recuperação das notas de entrada (Passo 3)”. |
| --- |
| - nota fiscal de entrada (MOVTO_E_S  <> ‘9’); - data fiscal da nota = considerar as notas com data <= a data da nota fiscal de venda do produto (data da nota de saída);   Atendido este primeiro critério, as notas deverão ser recuperadas em ordem decrescente de data, até que o total da quantidade de todas as notas recuperadas atinja a quantidade vendida do produto (quantidade da venda).   Se o total da quantidade não for atingido na busca pelas notas de entrada para a empresa e o estabelecimento da geração, deve ser verificado se o parâmetro para buscar as notas na empresa incorporada está marcado:       Se o parâmetro “Considerar as notas fiscais da empresa incorporada” estiver marcado em tela            Considerar as notas da empresa/estabelecimento cadastradas como incorporadas na tela de Relação de Empresa             Incorporadora x Incorporada** para a empresa/estabelecimento da geração (incorporadora), para recuperar as notas de              entrada para atingir a quantidade vendida do produto     Senão           Considerar somente as notas fiscais da empresa e estabelecimento selecionados para a geração.  ** Módulo Parâmetros, item Preliminares à Relação de Empresa Incorporadora x Incorporada  - desconsiderar as notas canceladas - desconsiderar as notas de devolução - considerar apenas os itens com CFOP ou CFOP/Natureza parametrizados no menu “Parâmetros à Registro C176 à NF’s    Entrada”;   - produto = produto do item da nota de venda (ver OBS abaixo);    OU    (produto = indicador e código anterior do produto do item da nota de venda e data de emissão da nota de entrada < data da     alteração do código do produto do item da nota de venda)  Alteração MFS18752 (Ago/2018): a busca do item da nota de entrada passou a ser feita considerando o código do produto da nota de venda, ou, o código anterior do produto registrado na SAFX2013, quando for o caso. Mas, o código anterior só será considerado nos casos em que a nota de entrada for de uma data anterior a data da alteração do código registrada na SAFX2013. Desta forma, essa nova condição se baseia nos seguintes campos do cadastro do produto da saída: campos “42-Indicador Anterior”, “43-Código Anterior” e “44-Data da Alteração” da SAFX2013 (observar que o campo do código anterior do produto poderá estar nulo, e assim, só deve ser utilizado quando preenchido).   Considerar a necessidade de pesquisar esta nota nas tabelas normais (X07/X08), já que a nota fiscal poderá estar num período anterior ao período da movimentação gerada no Datamart.  Atentar para o detalhe de não considerar a mesma nota já recuperada através do documento de referência informado na SAFX08.  OBS: Quando no documento encontrado existir mais de um item do mesmo produto, deve-se totalizar as quantidades e as bases de cálculo de todos os itens, e o campo VL_UNIT_BC_ST deve ser calculado a partir das bases e quantidades já totalizadas, conforme descrito no item “7-Gravação  dos Dados” (item “Gravação dos Dados referentes ao registro C176”). |


| Situação de erro | Mensagem de aviso |
| --- | --- |
| Quando no item da nota de saída os campos do documento de referência estiverem preenchidos, mas ao tentar recuperar a nota na base de dados, ela não for encontrada. Neste caso, deverá ser gerada mensagem de aviso, e a rotina deve interromper o processamento deste item (ou seja, não precisa fazer a pesquisa de outras notas de entrada na base de dados, pois diante do erro encontrado, o usuário terá que verificar se o documento de referência informado está errado). | O documento de referência indicado no item da nota não foi encontrado na base de dados. O registro C176 não será gerado. |
| Quando o total da quantidade de todas as notas de entrada recuperadas, não for o suficiente para “cobrir” a quantidade do item da nota de saída. | A quantidade do Item de Saída não foi atingida pelas quantidades das últimas NF de Entradas recuperadas |
| Quando o item da nota de saída não tiver a informação do documento de referência, e ao realizar a pesquisa das notas de entrada na base de dados, não for encontrada nenhuma nota até a data limite informada em tela. | Não foram identificadas NF de Entradas para o Item de Saída. O registro  C176 não será gerado. |
| Quando na nota de entrada, a quantidade do item ou os três campos da base de cálculo do ST não estiverem preenchidos no item, será exibida mensagem de erro no log. | Para calcular a BC unitária é necessário que os campos da QTD (campo 24) e da BC do ICMS-ST estejam preenchidos no item da nota (campo 61, 144 ou 106). |


| Registro 88-STITNF do Sintegra à Tem um procedimento que grava as últimas entradas do produto até atingir a quantidade do produto em estoque. Para recuperar as entradas não há filtro de CFOP (vale qq nota). Nas operações interestaduais usa a BC normal do ST (campo 61 da SAFX08), já nas internas usa a não escriturada (campo 144 da SAFX08). A razão desta lógica é obter a BC no caso das operações em que o ST não é lançado na entrada (o emitente não é o responsável pelo recolhimento). Este tratamento foi feito para clientes de MG, com base no Decreto 44.541 (Jun/2007) – SEF-MG (OS2437).  CAT 17 (Apur Compl/Ressarcimento de ST) àTambém trata as operações de entrada dos produtos que geraram solicitação de Ressarcimento. Neste caso existe uma parametrização por CFOP/Nat. Para recuperar as notas (coluna “Valor Total da Base de Cálculo da Retenção” do Modelo III da CAT 17). Utiliza a BC normal do ST (campo 61 da SAFX08) ou o campo 106, para os casos em que a retenção for feita na origem. Neste caso, os campos normais da BC e do valor do ST não estarão preenchidos, e a BC estará no campo “106-Base Cálculo Carga Tributária Origem ICMS” (da mesma forma que o campo 144, também se trata de ST que não será escriturada no livro, e por isso, os valores do ST não estão nos campos normais).  (OS1165, v1r8.0) |
| --- |


| Se “Gerar os ajustes (C197) e os lançamentos complementares na Apuração do ICMS” desmarcado             Neste caso o procedimento de geração dos ajustes não será executado;     Senão  (“Gerar os ajustes (C197) e os lançamentos complementares na Apuração do ICMS” marcado )               Se “Tratamento das saídas com notas de entrada sem valor de ICMS-ST” desmarcado                     Neste caso o procedimento de geração dos ajustes será executado normalmente;              Senão  (“Tratamento das saídas com notas de entrada sem valor de ICMS-ST” marcado)                       Neste caso o procedimento de geração dos ajustes será executado apenas se todas as entradas geradas p/a                    saída em questão, tiverem valor do ICMS-ST (conforme explicado acima). Caso contrário, o procedimento de                     geração dos ajustes não será executado; |
| --- |


| VL_BC_ICMS | A base de cálculo a ser utilizada para o ajuste é calculada da seguinte forma:  Valor do campo 09 (Valor unitário da base de cálculo do imposto pago por substituição) gerado p/o C176 x Quantidade do item da nota de saída  Quando existir mais de uma nota de entrada:  Caso exista mais de uma nota fiscal de entrada para o item em questão, ou seja, caso tenha sido gerado mais de um registro C176 para o item, o valor a ser utilizado será a média do campo 09 de todas as entradas (de todos os C176 gerados), e só depois, multiplicar a quantidade do item da saída sobre os valores médios calculados.  Exemplo:  Registro 1: Valor do campo 09= 250,00 Registro 2: Valor do campo 09 = 78,00 Registro 3: Valor do campo 09 = 1.480,00  Valor médio a ser utilizado = (250,00 + 78,00 + 1.480,00) / 3 = 602,66  Alteração MFS9986: Alterada a forma de cálculo para fazer a média ponderada, utilizando como peso a quantidade de cada nota de entrada, ao invés de considerar apenas a quantidade de notas de entrada geradas para a saída. Com a alteração, a média passou a ser calculada da seguinte forma:      [ (valor nf 1 * qtd nf 1) + (valor nf 2 * qtd nf 2) + (valor nf 3 * qtd nf 3) ...... ]  /  [ qtd nf 1 + qtd nf 2 + qtd nf 3 ..........]  Exemplo:  Registro 1: Valor do campo 09 = 50,00       Qtd da entrada (campo 07): 10 Registro 2: Valor do campo 09 = 48,00       Qtd da entrada (campo 07): 25 Registro 3: Valor do campo 09 = 42,50       Qtd da entrada (campo 07): 40  Valor médio a ser utilizado =   [ (50,00 * 10) + (48,00 * 25) + (42,50 * 40) ] / [ 10 + 25 + 40 ] = [ 500,00 + 1.200,00 + 1.700,00) / [ 75 ] = 3.400,00  / 75 = 45,33  (pela regra original o resultado seria = 46,83, pois seria = (50,00 + 48,00 + 42,50) / 3 )  Após calcular a média do campo 09 de todas as entradas, é só multiplicar o valor obtido pela quantidade do item da saída.  Exemplo: supondo que no exemplo acima a quantidade da saída fosse = 10,00, teríamos:                                                 45,33 (valor médio apurado) * 10, 00 = 453,30 |
| --- | --- |
| ALIQ_ICMS | Alíquota do ICMS-ST da nota fiscal de entrada:  Alíquota do campo 16 (Alíquota do ICMS ST relativa à última entrada da mercadoria) gerado p/ o C176    Caso exista mais de uma nota fiscal de entrada para o item em questão, as alíquotas entre as notas de entrada sempre serão iguais, pois de acordo com a regra definida, será utilizada a alíquota interna da parametrização dos produtos para preencher o campo 16-ALIQ_ST_ULT_E.  Obs.: Para o Registro C197 não será aplicado a regra de considerar a Alíquota Interna do parâmetro: EFD Escrituração Fiscal Digital >> Parâmetros >> Registro C176 >> Produtos ou NCM's, por Data de Validade de Inicio e Fim, conforme Nota Fiscal de Entrada, uma vez que o PVA não permite registros com a mesma informação do “COD_AJ” e “COD_ITEM”. |
| VL_ICMS | O valor do ajuste é calculado da seguinte forma:                       (17-VL-UNIT_RES * Quantidade do item da nota de saída)  Quando existir mais de uma nota de entrada:  Caso exista mais de uma nota fiscal de entrada para o item em questão, ou seja, caso tenha sido gerado mais de um registro C176 para o item, o valor a ser utilizado será a média do campo 17 de todas as entradas (de todos os C176 gerados), e só depois, multiplicar a quantidade do item da saída sobre os valores médios calculados.  Exemplo:  Registro 1: Valor do campo 17= 50,00 Registro 2: Valor do campo 17 = 125,00 Registro 3: Valor do campo 17 = 3,200,00  Valor médio a ser utilizado = (50,00 + 125,00 + 3.200,00) / 3 = 1.125,00  Alteração MFS9986: Alterada a forma de cálculo para fazer a média ponderada, utilizando como peso a quantidade de cada nota de entrada, ao invés de considerar apenas a quantidade de notas de entrada geradas para a saída. Com a alteração, a média passou a ser calculada da seguinte forma:      [ (valor nf 1 * qtd nf 1) + (valor nf 2 * qtd nf 2) + (valor nf 3 * qtd nf 3) ...... ]  /  [ qtd nf 1 + qtd nf 2 + qtd nf 3 ..........]  Após calcular a média do campo 17 de todas as entradas, é só multiplicar o valor obtido pela quantidade do item da saída.  (a lógica é a mesma descrita no exemplo do campo VL_BC_ICMS) |


| VL_BC_ICMS | A base de cálculo a ser utilizada para o ajuste é calculada da seguinte forma:  Valor do campo 14 (Valor unitário da base de cálculo do ICMS relativo à última entrada da mercadoria) gerado p/o C176 x Quantidade do item da nota de saída  Quando existir mais de uma nota de entrada:  Caso exista mais de uma nota fiscal de entrada para o item em questão, ou seja, caso tenha sido gerado mais de um registro C176 para o item, o valor a ser utilizado será a média do campo 14 de todas as entradas (de todos os C176 gerados), e só depois, multiplicar a quantidade do item da saída sobre os valores médios calculados.  Alteração MFS9986: Alterada a forma de cálculo para fazer a média ponderada, utilizando como peso a quantidade de cada nota de entrada, ao invés de considerar apenas a quantidade de notas de entrada geradas para a saída. Com a alteração, a média passou a ser calculada da seguinte forma:      [ (valor nf 1 * qtd nf 1) + (valor nf 2 * qtd nf 2) + (valor nf 3 * qtd nf 3) ...... ]  /  [ qtd nf 1 + qtd nf 2 + qtd nf 3 ..........]  Após calcular a média do campo 14 de todas as entradas, é só multiplicar o valor obtido pela quantidade do item da saída.  (a lógica é a mesma descrita no exemplo do campo VL_BC_ICMS do ajuste de ressarcimento) |
| --- | --- |
| ALIQ_ICMS | Alíquota do ICMS da nota fiscal de entrada:  Alíquota do campo 13 (Alíquota do ICMS aplicável à última entrada da mercadoria) gerado p/ o C176  Caso exista mais de uma nota fiscal de entrada para o item em questão, observar:   No caso deste ajuste, as alíquotas das diferentes notas de entrada poderão ser diferentes (o que não é o esperado). Neste caso, o Setor de Informação recomenda que seja informada a alíquota (o campo 13) da nota de entrada mais recente. Sabemos que neste caso a conta do C197 também não irá fechar (valor = base * aliq /100), mas nesse início o procedimento será este. Ou seja, caso exista mais de uma nota fiscal de entrada para o item em questão, a alíquota a ser utilizada será a alíquota do ICMS (campo 13) da nota de entrada mais recente.   Obs* Campo 13 - ALIQ_ICMS_ULT_E - Alíquota do ICMS aplicável à última entrada da mercadoria |
| VL_ICMS | O valor do ajuste é calculado da seguinte forma:                       (15- VL_UNIT_ICMS_ULT_E * Quantidade do item da nota de saída)  Quando existir mais de uma nota de entrada:  Caso exista mais de uma nota fiscal de entrada para o item em questão, ou seja, caso tenha sido gerado mais de um registro C176 para o item, o valor a ser utilizado será a média do campo 15 de todas as entradas (de todos os C176 gerados), e só depois, multiplicar a quantidade do item da saída sobre os valores médios calculados.  Alteração MFS9986: Alterada a forma de cálculo para fazer a média ponderada, utilizando como peso a quantidade de cada nota de entrada, ao invés de considerar apenas a quantidade de notas de entrada geradas para a saída. Com a alteração, a média passou a ser calculada da seguinte forma:      [ (valor nf 1 * qtd nf 1) + (valor nf 2 * qtd nf 2) + (valor nf 3 * qtd nf 3) ...... ]  /  [ qtd nf 1 + qtd nf 2 + qtd nf 3 ..........]  Após calcular a média do campo 15 de todas as entradas, é só multiplicar o valor obtido pela quantidade do item da saída.  (a lógica é a mesma descrita no exemplo do campo VL_BC_ICMS do ajuste de ressarcimento) |


| O CFOP do item deve constar da parametrização do menu “Parâmetros à Registro C176 à NF’s Saída c/direito a        Ressarcimento (e Devoluções)à CFOP” do módulo EFD”;       ou       O CFOP/Natureza de Operação do item deve constar da parametrização do menu “Parâmetros à Registro C176 à NF’s      Saída c/direito a Ressarcimento (e Devoluções)à CFOP / Natureza de Operação” do módulo EFD”; |
| --- |


| O produto do item deve constar da parametrização do menu “Parâmetros à Registro C176 à Produtos” do módulo       EFD”;        ou        O NCM do produto do item deve constar da parametrização do menu “Parâmetros à Registro C176 à NCM’s” do       módulo EFD”;  Na pesquisa da parametrização dos Produtos / NCM’s, poderão existir várias parametrizações válidas para o Estabelecimento e período em questão, pois esta parametrização é por Estab/Grupo/Aliq/Validade.  Serão pesquisadas as parametrizações existentes para o Estabelecimento em questão, Grupo válido para o período da geração, e cuja validade atenda ao período da geração, ou seja:  - tenha validade inicial <= ao primeiro dia do período da geração; - se a validade final estiver preenchida, ela deve ser uma data >= ao último dia do período da geração;  Basta que o Produto, ou o seu NCM, conste em qualquer uma das parametrizações válidas para o período. |
| --- |


| Devoluções sem referências das saídas na SAFX192:   Para os itens de devolução que não tiverem dados na SAFX192, será gerada uma mensagem de erro no log, e a devolução não será considerada no processo: “Item de devolução não processado, pois não foram identificadas as referências das saídas (SAFX192)”. O log deve demonstrar os dados básicos de identificação do item da devolução, para que o usuário possa verificar o problema.  Quantidade da Devoluções x Quantidades Referenciadas na SAFX192:  O total das quantidades informadas para todas as saídas referenciadas na SAFX192 (campo “24-Quantidade Devolução”), deve ser igual à quantidade do item da devolução (quantidade da SAFX08). Caso esta igualdade não ocorra, será gerada uma mensagem de erro no log, e a devolução não será considerada no processo: “O total das quantidades de devolução informadas nas referências, não confere com a quantidade da devolução”. O log deve demonstrar os dados básicos de identificação do item da devolução, para que o usuário possa verificar o problema. |
| --- |


| SAFX113 | SAFX192 |
| --- | --- |
| Campos 01 ao 11 (campos de identificação da capa) | = campos chave da capa (campo 01 ao 11) |
| Campo 15 (campo de identificação do item) | = campo de identificação do item (campo 15) |
| Campo 13 (Código do Ajuste) | Os códigos de ajustes serão identificados a partir da parametrização (menu “Parâmetros > Registro C176 > Parâmetros p/Geração dos Ajustes e Lançamentos”), da seguinte forma:  Para o ajuste de ressarcimento: 	 = deve ser o código parametrizado no campo “Ajuste de Ressarcimento”   Para o ajuste de crédito:  = deve ser o código parametrizado no campo “Ajuste de Crédito” |


| SAFX08 / SAFX113 | SAFX192 (Referências) |
| --- | --- |
| Nota de Venda:100                                                                                            ICMS        Base      Aliq                                                                                           ----------    ------------  ------ Item 1 - Produto 01  QTD: 40   Ajuste Ressarcimento:    500,00     10.000,00   5%                                                      Ajuste Crédito:                140,00     1.400,00   10%  Item 2 - Produto 02  QTD: 10   Ajuste Ressarcimento: 1.200,00     24.000,00   5%                                                    Ajuste Crédito:               800,00      8.000,00   10%  Nota de Devolução: 888  Item 1 - Produto 01  QTD: 40 Item 2 - Produto 02  QTD: 5 | Nota de Devolução: 888  Item 1: Nota de saída 100, Item 1, QTD: 40 Item 2: Nota de saída 100, Item 2, QTD: 5 |


| OBS: No caso de geração por inscrição estadual única, os lançamentos serão gerados sempre para o estabelecimento                centralizador (estabelecimento selecionado na tela da geração), considerando o valor total dos ajustes referentes a todos os estabelecimentos envolvidos na centralização (centralizador e centralizados). Além disso, será utilizado o livro fsical “165”, ao invés da livro “108”; |
| --- |


| Lançamento de ressarcimento: | Total do valor de todos os ajustes de ressarcimento (total do campo VL_ICMS, conforme o cálculo definido no item “3-Recuperação dos Dados e Processamento – Ajustes (C195/C197)”).  Alteração da MFS47510: Desconsiderar os valores de ajustes referentes a códigos de ajuste em que o terceiro caracter igual a “9” (=Informativo) E o quarto caracater igual a “9” (=Informativo). |
| --- | --- |
| Lançamento de crédito: | Total do valor de todos os ajustes de crédito (total do campo VL_ICMS, conforme o cálculo definido no item “3-Recuperação dos Dados e Processamento – Ajustes (C195/C197)”).  Alteração da MFS47510: Desconsiderar os valores de ajustes referentes a códigos de ajuste em que o terceiro caracter igual a “9” (=Informativo) E o quarto caracater igual a “9” (=Informativo). |
| Lançamento de estorno de ressarcimento (devoluções):  (criado na MFS9749) | Total do valor de todos os ajustes de estorno de ressarcimento gerados a partir das notas de devolução, confome cálculo definido no item “5-Recuperação dos Dados e Processamento – Ajustes de Estorno das Devoluções”.  Alteração da MFS47510: Desconsiderar os valores de ajustes referentes a códigos de ajuste em que o terceiro caracter igual a “9” (=Informativo) E o quarto caracater igual a “9” (=Informativo). |
| Lançamento de estorno de crédito (devoluções):  (criado na MFS9749) | Total do valor de todos os ajustes de estorno de crédito gerados a partir das notas de devolução, confome cálculo definido no item “5-Recuperação dos Dados e Processamento – Ajustes de Estorno das Devoluções”.  Alteração da MFS47510: Desconsiderar os valores de ajustes referentes a códigos de ajuste em que o terceiro caracter igual a “9” (=Informativo) E o quarto caracater igual a “9” (=Informativo). |
| Lançamento de estorno do  ressarcimento (valor que será transferido p/o registro 1200):  (criado na MFS8892) (alterado na MFS9749) | O valor deste lançamento é exatamente igual ao valor do lançamento de ressarcimento – lançamento de estorno do ressarcimento (Devoluções), já que seu objetivo é estornar o ressarcimento total.  (naturalmente este lançamento só será realizado se existir valor de ressarcimento, ou seja, se o primeiro lançamento tiver sido realizado) |


| Pessoa Fis/Jur | Indicador e Código do emitente da nota fiscal da entrada   (a informação deste campo irá gerar o campo “06- COD_PART_ULT_E” do registro C176).  Alteração MFS47166: Regra para Notas Fiscais de Entradas Emitidas pelo Próprio Estabelecimento (acolhendo Notas de Produtores Agropecuários) - Cliente Zaffira.         Se Nota Fiscal de Entradas campo MOVTO_E_S = 2         Preencher com Indicador e Código do emitente da nota fiscal de saída.  Senão      Preencher com o Indicador e Código do emitente da nota fiscal da entrada |
| --- | --- |
| Valor unitário da entrada | Alteração MFS2772: Na geração deste campo foram acrescidas as despesas acessórias do item. Originalmante, o campo era preenchido apenas com o preço unitário do item.   Este campo será preenchido com o valor unitário (campo 27-Preço Unit) + despesas acessórias (campos 39-Frete, 40-Seguro e campo 41-Outras Despesas) do item da nota fiscal de entrada  A informação do campo “27-Preço Unitário” já é o valor unitário, como descreve o próprio nome. Já o valor dos campos “Frete”, “Seguro” e “Outras Despesas” precisa ser dividido pela quantidade do item, para que seja utilizado o valor unitário destas despesas.  Assim, o valor será apurado da seguinte forma:                               [Preço Unitário + ((Frete + Seguro + Outras Despesas) / Qtd do item)]  Obs à no caso da nota de entrada ter mais de um item de mesmo produto, recuperados no processo, será calculado o preço unitário por item (valor unitário para cada item separadamente).  (a informação deste campo irá gerar o campo “08- VL_UNIT_ULT_E” do registro C176) |
| Valor unitário da base de cálculo do ICMS-ST da entrada | Este campo será preenchido com a base de cálculo do ST do item da nota de entrada, dividida pela quantidade do item (quantidade também da entrada). Este procedimento é feito para se calcular o valor unitário, como pede o registro C176.   A base de cálculo a ser utilizada dependerá do campo que estiver preenchido na SAFX08, já que devemos considerar que a operação pode ter o ICMS-ST escriturado ou não escriturado, e em qualquer um dos casos a base de cálculo precisa ser demonstrada no C176.  Para isso, será aplicada a seguinte lógica no preenchimento deste campo:  Se campo “61-Base ICMS-ST” preenchido:      O campo será preenchido com o seguinte valor à (61-Base ICMS-ST / 24-Quantidade) Senão      Se campo “144-Base ICMS-ST não Escriturada” preenchido:          O campo será preenchido com o seguinte valor à (144-Base ICMS-ST não Escriturada / 24-Quantidade)      Senão           Se campo “106-Base Cálculo Carga Tribut Origem” preenchido:                O campo será preenchido com o seguinte valor à (106-Base Cálculo Carga Tribut Origem / 24-Quantidade)           Senão                O campo não será preenchido.  Desta forma, qualquer que seja a situação tributária da nota de entrada do produto, a informação será demonstrada. O usuários da CAT17 e os clientes obrigados a geração dos registros 88STES e 88STITNF do Sintegra (Decreto 44.541 de Junho/07, SEF-MG) já estão cientes da necessidade de carregar a informação nos campo 144 ou 106 no caso do ST não escriturado na entrada (conforme descrito RNC176).    Obs à no caso da nota de entrada ter mais de um item de mesmo produto, recuperados no processo, será calculado o valor por item (valor unitário para cada item separadamente).  [MFS32699] Tratamento de crítica dada no validador quando compara o campo 9 com o campo 12: Quando o valor do campo 09 (VL_UNIT_BC_ST)  for menor que o valor do campo 12 (VL_UNIT_BC_ICMS_ULT_E), o campo 09 deve ser gravado com a última posição decimal igual a 0 e o valor deve ser truncado. Ex.: 8,035 à 8,030 Esse tratamento é necessário pois no validador do SPED-EFD, o campo 14 possui a seguinte consistência: Validação: o valor informado no campo 14 deve corresponder ao menor valor entre os campos 09 - VL_UNIT_BC_ST e 12 - VL_UNIT_BC_ICMS_ULT_E.  [MFS85388] Em atendimento ao layout  versão 1.16 (Janeiro/2023)   Tratamento de crítica dada no validador quando compara o campo 9 com o campo 12:  Para o período de geração a partir de 01/01/2023:  Quando o valor do campo 09 (VL_UNIT_BC_ST)  for menor que o valor do campo 12 (VL_UNIT_BC_ICMS_ULT_E) E o campo 18 (COD_RESP_RET) for igual a “2”, o campo 09 deve ser gravado com a última posição decimal igual a 0 e o valor deve ser truncado. Ex.: 8,035 à 8,030  Esse tratamento é necessário pois no validador do SPED-EFD, o campo 14 possui a seguinte consistência: Validação: deve corresponder ao menor valor entre os campos VL_UNIT_BC_ST e VL_UNIT_BC_ICMS_ULT_E, quando o campo COD_RESP_RET for igual a “2 – Remetente Indireto”   (a informação deste campo irá gerar o campo “09- VL_UNIT_BC_ST” do registro C176) |
| Chave de Acesso da NF-Eletrônica | Chave de Acesso da NF-e da nota fiscal da entrada   (a informação deste campo irá gerar o campo “10- CHAVE_NFE_ULT_E” do registro C176) |
| Valor unitário da base de cálculo da operação própria do remetente sob o regime comum de tributação. | Este campo será preenchido com a base de cálculo do ICMS Próprio do item da nota de entrada, dividida pela quantidade do item (quantidade também da entrada). Este procedimento é feito para se calcular o valor unitário, como pede o registro C176.   Para isso, será aplicada a seguinte lógica no preenchimento deste campo:  Se campo da base de cálculo do ICMS preenchido:      O campo será preenchido com o seguinte valor  (56 - Base ICMS / 24-Quantidade) Senão           Se campo da base outras ICMS preenchido:               O campo será preenchido com o seguinte valor  (56 - Base ICMS para 55 -Tributação = 3 / 24-Quantidade)          Senão               O campo será preenchido com o seguinte valor  (Base ICMS não destacado / 24-Quantidade)  Alteração da MFS8968 (CH 27247):  Este campo será preenchido com o valor do campo da base do ICMS não destacado (novo campo 226) do item da nota de entrada, dividido pela quantidade do item (quantidade também da entrada). Este procedimento é feito para se calcular o valor unitário, como pede o registro C176.   Quando o campo “Base ICMS Não Destacado” não estiver preenchido, então será utilizado o valor do campo “Base Outras ICMS”.  Desta forma, a lógica é a seguinte:  Se o campo “Base ICMS Não Destacado” estiver preenchido,       O campo será preenchido com o seguinte valor: (Base ICMS Não Destacado / 24-Quantidade); Senão       O campo será preenchido com o seguinte valor: (Base Outras ICMS / 24-Quantidade);  Se nenhuma das duas bases estiver preenchida, então o campo 12 será gerado com zeros.     Obs à no caso da nota de entrada ter mais de um item de mesmo produto, recuperados no processo, será calculado o valor por item (valor unitário para cada item separadamente).  [MFS34128] Tratamento de crítica dada no validador quando compara o campo 9 com o campo 12: Truncar o valor do campo 12 com duas decimais.  Esse tratamento é necessário pois no validador do SPED-EFD, o campo 14 possui a seguinte consistência: Validação: o valor informado no campo 14 deve corresponder ao menor valor entre os campos 09 - VL_UNIT_BC_ST e 12 - VL_UNIT_BC_ICMS_ULT_E.. (a informação deste campo irá gerar o campo “12- VL_UNIT_BC_ICMS_ULT_E” do registro C176) |
| Alíquota do ICMS aplicável à última entrada da mercadoria. | Este campo será a Alíquota do ICMS próprio que consta na nota da entrada.  No caso descrito para o campo anterior (compra de substituído), provavelmente a alíquota do ICMS também não estará preenchida na nota.   Para isso, será aplicada a seguinte lógica no preenchimento deste campo:  Se campo da Alíquota do ICMS preenchido:      O campo será preenchido com a Alíquota do ICMS; Senão      O campo será preenchido com a “Aliq ICMS não destacado”;  (a informação deste campo irá gerar o campo “13- ALIQ_ICMS_ULT_E” do registro C176) |
| Valor unitário da base de cálculo do ICMS relativo à última entrada da mercadoria, limitado ao valor da BC da retenção. | Este campo será preenchido com a base de cálculo do ICMS relativo à última entrada da mercadoria, limitado ao valor da BC da retenção que corresponderá ao menor valor entre os campos 09-VL_UNIT_BC_ST e 12-VL_UNIT_BC_ICMS_ULT_E.  Para isso, será aplicada a seguinte lógica no preenchimento deste campo:  [MFS71627] Alteração da regra de preenchimento do campo, quando o emitente for o substituto  Se emitente = Substituto, ou seja, se o campo 18 - COD_RESP_RET for igual a ‘1’ - Remetente Direto ou “4” - Remetente Direto Simples Nacional [MFS-73699]      Será Informado o valor do campo 12 - VL_UNIT_BC_ICMS_ULT_E;      Será informado o menor valor entre os campos 09 - VL_UNIT_BC_ST e 12 - VL_UNIT_BC_ICMS_ULT_E;  Se emitente = Substituído, ou seja, se o campo 18 - COD_RESP_RET for igual a ‘2’ - Remetente Indireto.     Será informado o menor valor entre os campos 09 - VL_UNIT_BC_ST e 12 - VL_UNIT_BC_ICMS_ULT_E;  Se for antecipação, ou seja, se o campo 18 - COD_RESP_RET for igual a ‘3’ - Próprio declarante.       Neste caso este campo não será preenchido;      Alteração da MFS8824 (Dez/2016): Será Informado o valor do campo 09;       Alteração da MFS9753 (Fev/2017): Será Informado o valor do campo 12 - VL_UNIT_BC_ICMS_ULT_E;       Alteração da MFS10355 (Abr/2017):       Será informado o menor valor entre os campos 09 - VL_UNIT_BC_ST e 12 - VL_UNIT_BC_ICMS_ULT_E;  Caso não seja encontrada informação no campo 18 – COD_RESP_REST, deverá ser apresentada uma mensagem de aviso no log conforme abaixo:  “Erro: Para calcular a BC unitária relativa à última entrada (campo 14) é necessário que o campo Indicador de ICMS-ST (campo 131) ou o campo Situação Especial - Substituição Tributária (campo 132)  esteja preenchido no item da nota.”  Obs à no caso da nota de entrada ter mais de um item de mesmo produto, recuperados no processo, será calculado o valor por item (valor unitário para cada item separadamente).  (a informação deste campo irá gerar o campo “14- VL_UNIT_LIMITE_BC_ICMS_ULT_E” do registro C176) |
| Valor unitário do crédito de ICMS sobre operações próprias do remetente, relativo à última entrada da mercadoria, decorrente da quebra da ST. | Este campo será preenchido com o crédito de ICMS sobre operações próprias do remetente, relativo à última entrada da mercadoria, decorrente da quebra da ST – equivalente à multiplicação entre os campos 13 - ALIQ_ICMS_ULT_E e 14- VL_UNIT_LIMITE_BC_ICMS_ULT_E.  Para isso o preenchimento deste campo será:  [(14- VL_UNIT_LIMITE_BC_ICMS_ULT_E * 13- ALIQ_ICMS_ULT_E) / 100]  No caso de antecipação, este campo não será preenchido, uma vez que não existirá informação no campo 14.  Tratamento:       - Se no preenchimento do campo o valor for igual a ‘0’, na geração este campo deverá ser preenchido com vazio.  Obs à no caso da nota de entrada ter mais de um item de mesmo produto, recuperados no processo, será calculado o valor por item (valor unitário para cada item separadamente).  (a informação deste campo irá gerar o campo “15- VL_UNIT_ICMS_ULT_E” do registro C176) |
| Alíquota do ICMS ST relativa à última entrada da mercadoria. | Este campo será a Alíquota do ICMS-ST que consta na nota da entrada.  Na geração deste campo será utilizada a alíquota interna do produto. Esta alíquota é informada na parametrização dos produtos para geração do C176 (parametrização já existente). Menu: Parâmetros > Registro C176 > Produto ou NCM´s.  [ALTERAÇÃO – MFS60490] Regra para considerar a validade da Alíquota interna parametrizada, de acordo com a data da Nota Fiscal de Entrada, considerado os parâmetros por Produto e NCM’s.  - Utilizar a alíquota interna dos produtos ou NCM’s, considerando a Data de Validade da aliquota interna parametrizada, de acordo com a Data da Nota Fiscal de entrada, para preencher o campo 16-ALIQ_ST_ULT_E, abaixo exemplo para facilitar o entendimento:  Parametrização Por Produto – C176   Caso exista mais de uma nota fiscal de entrada para o item em questão, o programa deverá considerar a Data de Entrada x Validade da aliquota interna parametrizada, conforme quadro de exemplo acima, o cálculo já é efetuado e demonstrado por Nota Fiscal e ao final no quadro “Totais C176” será demonstrado a somatório dos valores das Notas Fiscais. Conforme regra  (*Linhas de total das entradas demonstradas*).  (a informação deste campo irá gerar o campo “16- ALIQ_ST_ULT_E” do registro C176) |
| Valor unitário do ressarcimento (parcial ou completo) de ICMS decorrente da quebra da ST | Este campo será preenchido com o valor do ressarcimento (parcial ou completo) de ICMS, relativo à última entrada da mercadoria, decorrente da quebra da ST.  Para isso o preenchimento deste campo será:  [(09- VL_UNIT_BC_ST * 16- ALIQ_ST_ULT_E) / 100] - 15-VL_UNIT_ICMS_ULT_E  Obs1 à no caso da nota de entrada ter mais de um item de mesmo produto, recuperados no processo, será calculado o valor por item (valor unitário para cada item separadamente).  [ALTERADA - CH1151_2018 (MFS-16129)] Obs2 à o valor informado nesse campo deve ser maior ou igual a “0” (zero), então se o valor calculado gerar negativo, gravar “0” (zero). Essa situação ocorre por exceção em que a base de cálculo do ICMS próprio é maior do que a base de cálculo do ICMS-ST, então não há recolhimento/ ressarcimento do ICMS-ST, nessa circunstância o Registro C197 não deverá ser gerado e pode ter impacto no bloco E.  (a informação deste campo irá gerar o campo “17- VL_UNIT_RES” do registro C176) |
| Código do responsável pela retenção do ICMS-ST | Responsável pela retenção da nota fiscal da entrada.  A informação ser utilizada dependerá do campo 131- Indicador de ICMS-ST e 132 - Situação Especial - Substituição Tributária que estiver preenchido na SAFX08.  Para isso, será aplicada a seguinte lógica no preenchimento deste campo:  Se campo “132 - Situação Especial - Substituição Tributária” igual a ‘1’:      O campo será preenchido com o seguinte valor à “3” - Próprio Declarante Senão      Se campo “131- Indicador de ICMS-ST” igual a ‘1’:          [MFS-73699]          Se Data Inicial da Geração for anterior a Janeiro de 2022, então:              O campo será preenchido com o seguinte valor à “1” - Remetente Direto;          Senão:              Se Pessoa Fis/Jur gravada no campo “06- COD_PART_ULT_E”  for do Simples Nacional (IND_SIMPLES_NAC = ‘S’)                  (SAFX04 - campo 43- Enquadrado como Simples Nacional) então:                 O campo será preenchido com o seguinte valor à “4” - Remetente Direto Simples Nacional              Senão                 O campo será preenchido com o seguinte valor à “1” - Remetente Direto Regime Comum       Se campo “131- Indicador de ICMS-ST” igual a ‘2’:          O campo será preenchido com o seguinte valor à “2” - Remetente Indireto   (a informação deste campo irá gerar o campo “18- COD_RESP_RET” do registro C176) |
| Código do motivo do ressarcimento | Motivo do Ressarcimento   [ALTERADA – MFS-20986] [MFS-47427] Alteração da descrição da opção 1, conforme atualização do guia prático  Opções: 1–Saída para outra UF;   1–Venda para outra UF; 2 – Saída amparada por isenção ou não incidência; 3 – Perda ou deterioração; 4 – Furto ou roubo; 5 – Exportação; 6 – Venda interna para Simples Nacional; 9 – Outros.  A informação a ser utilizada dependerá do campo ‘Motivo do Ressarcimento’ do Quadro Sped Fiscal (Registro C176) que estiver preenchido na SAFX08. Alteração da MFS9068: Este campo será preenchido com a informação do campo “228-Motivo do Ressarcimento” (SAFX08) do item da nota fiscal de saída (C170) que originou o registro C176.  (a informação deste campo irá gerar o campo “19- COD_MOT_RES” do registro C176) |
| Chave de Acesso da NF-E com retenção ICMS-ST | Chave de Acesso da NF-e emitida pelo substituto, na qual consta o valor do ICMS-ST retido.  Alteração MFS637814, ativação do campo em atendimento a atualização legal e ticket 97289:  Para o Rio de Janeiro – RJ:  Este campo é preenchido com a informação do campo ‘Chave de Acesso da NF-E com retenção ICMS-ST’ da nota fiscal de entrada(campo 231 da SAFX08, na tela de manutenção, fica no quadro “Sped Fiscal -  Registro C176”).  (a informação deste campo irá gerar o campo “20- CHAVE_NFE_RET” do registro C176)  Para as demais UF´s:  Alteração MFS8795: campo dispensado pela Port. CAT 112/2016  Este campo não será preenchido. |
| Código do participante do emitente da NF-e em que houve a retenção do ICMS-ST | Indicador e código do participante do emitente da NF-e em que houve a retenção do ICMS-ST.  Alteração MFS637814, ativação do campo em atendimento a atualização legal e ticket 97289:  Para o Rio de Janeiro – RJ:  Este campo é preenchido com a informação dos campos ‘Indicador da Pessoa Fis/Jur do emitente da NF-E com retenção ICMS-ST’ e ‘Código da Pessoa Fis/Jur do emitente da NF-E com retenção ICMS-ST’ (campos 233 e 234 da SAFX08, na tela de manutenção ficam no quadro “Sped Fiscal - Registro C176”).  (a informação deste campo irá gerar o campo “21- COD_PART_NFE_RET” do registro C176)  Para as demais UF´s:  Alteração MFS8795: campo dispensado pela Port. CAT 112/2016  Este campo não será preenchido. |
| Série da NF-e em que houve a retenção do ICMS-ST | Série da NF-e em que houve a retenção do ICMS-ST.  Alteração MFS637814, ativação do campo em atendimento a atualização legal e ticket 97289:  Para o Rio de Janeiro – RJ:   Este campo é preenchido com a informação do campo ‘Série do Docto. Fiscal com retenção ICMS-ST’ (campo 230 da SAFX08, na tela de manutenção fica no quadro “Sped Fiscal - Registro C176”).   (a informação deste campo irá gerar o campo “22- SER_NFE_RET” do registro C176)  Para as demais UF´s:  Alteração MFS8795: campo dispensado pela Port. CAT 112/2016  Este campo não será preenchido. |
| Número da NF-e em que houve a retenção do ICMS-ST | Número da NF-e em que houve a retenção do ICMS-ST  Alteração MFS637814, ativação do campo em atendimento a atualização legal e ticket 97289:  Para o Rio de Janeiro – RJ:  Este campo é preenchido com a informação do campo ‘Número do Docto. Fiscal com retenção ICMS-ST’ (campo 229 da SAFX08, na tela de manutenção fica no quadro “Sped Fiscal - Registro C176”).  (a informação deste campo irá gerar o campo “23- NUM_NFE_RET” do registro C176)  Para as demais UF´s:  Alteração MFS8795: campo dispensado pela Port. CAT 112/2016  Este campo não será preenchido. |
| Número sequencial do item na NF-e em que houve a retenção do ICMS-ST | Número sequencial do item na NF-e em que houve a retenção do ICMS-ST, que corresponde à mercadoria objeto de pedido de ressarcimento.  Alteração MFS637814, ativação do campo em atendimento a atualização legal e ticket 97289:  Para o Rio de Janeiro – RJ:  Este campo é preenchido com a informação do campo ‘Item do Docto. Fiscal com retenção ICMS-ST’ (campo 232 da SAFX08, na tela de manutenção fica no quadro “Sped Fiscal - Registro C176”).  (a informação deste campo irá gerar o campo “24- ITEM_NFE_RET” do registro C176)  Para as demais UF´s:  Alteração MFS8795: campo dispensado pela Port. CAT 112/2016  Este campo não será preenchido. |
| Código do modelo do documento de arrecadação | Código do modelo do documento de arrecadação.  0 - Documento estadual de arrecadação 1 – GNRE  A informação a ser utilizada dependerá dos campos ‘Código do modelo do documento de arrecadação’ do Quadro Sped Fiscal (Registro C176) que estiver preenchido na SAFX08.  (a informação deste campo irá gerar o campo “25- COD_DA” do registro C176) |
| Número do documento de arrecadação estadual | Número do documento de arrecadação estadual, se houver.  A informação a ser utilizada dependerá dos campos ‘Número do documento de arrecadação’ do Quadro Sped Fiscal (Registro C176) que estiver preenchido na SAFX08.  (a informação deste campo irá gerar o campo “26- NUM_DA” do registro C176) |
| Valor Unitário do Ressarcimento (parcial ou completo) de FCP decorrente da quebra da ST | [ALTERADA – MFS-20986] [ALTERADA – MFS523539]   Valor Unitário do Ressarcimento (parcial ou completo) de FCP decorrente da quebra da ST.  Se a UF do estabelecimento da geração for igual a “RS”      Preencher com zeros Senão      Este campo é preenchido com a informação preenchida no campo 140-ICMS-ST do Quadro FECEP dividido pela informação       preenchida no campo 24-Quantidade da SAFX08 (140-ICMS-ST do Quadro FECEP / 24-Quantidade da tabela SAFX08).  (a informação deste campo irá gerar o campo “27- VL_UNIT_RES_FCP_ST” do registro C176) |
| Indicador de Gravação na EFD   (MFS11639) | Esta coluna foi criada na tabela auxiliar pela MFS11639 (Jun/2017). O objetivo é indicar se as entradas de uma determinada saída deverão ou não ser gravadas no C176 no momento da geração do arquivo da EFD.  Para o preenchimento deste campo, é utilizada a seguinte regra:  Se parâmetro “Tratamento das saídas com notas de entrada sem valor de ICMS-ST” desmarcado:        Neste caso o campo ficará sempre com o valor default “S”  Senão     (parâmetro “Tratamento das saídas com notas de entrada sem valor de ICMS-ST” marcado)        Neste caso o conteúdo a ser gravado dependerá da seguinte condição:       - Se todas as entradas geradas para o item da saída em questão, tiverem o valor do ICMS-ST preenchido (ou seja, têm o campo          “09-VL_UNIT_BC_ST” do C176 com um valor > zeros), nesse caso o conteúdo será “S”.        - Se uma ou mais entradas referentes à saída em questão não atenderem a esta condição, nesse caso o conteúdo será “N”.    OBS: Este indicador se refere na verdade ao item da saída, e indica se as suas entradas deverão ou não ser gravados no meio magnético do Sped Fiscal (C176). Assim, independente de quantas entradas existirem para uma determinada saída, todas as linhas da tabela referentes à mesma nota de saída, terão o mesmo conteúdo no indicador (ou todos = “S” ou todos = “N”). |


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


| Tipo de Observação (campo 12) | “L” (observações referentes aos lançamentos fiscais da nota) |
| --- | --- |
| COD_OBS | Código da observação parametrizada pelo usuário para os ajustes de estorno de ressarcimento (devoluções) (parametrização descrita no item 3). |
| TXT_COMPL | (sem informação) |


| COD_AJ | Código do ajuste de estorno do ressarcimento (devoluções) parametrizado pelo usuário (parametrização descrita no item 3). |
| --- | --- |
| DESCR_COMPL_AJ | Descrição complementar do ajuste de estorno do ressarcimento (devoluções) parametrizada pelo usuário (parametrização descrita no item 3). |
| COD_ITEM | Indicador e Código do produto em questão (produto do item da nota fiscal de devolução processada) |
| VL_BC_ICMS | Valor da base de cálculo do ajuste de estorno do ressarcimento (devoluções), conforme cálculo definido no item “5-Recuperação dos Dados e Processamento (Ajustes de Estorno das Devoluções)”. |
| ALIQ_ICMS | Valor da alíquota do ajuste de estorno do ressarcimento (devoluções), conforme cálculo definido no item “5-Recuperação dos Dados e Processamento (Ajustes de Estorno das Devoluções)”. |
| VL_ICMS | Valor do ICMS do ajuste de estorno do ressarcimento (devoluções), conforme cálculo definido no item “5-Recuperação dos Dados e Processamento (Ajustes de Estorno das Devoluções)”. |


| Tipo de Observação (campo 12) | “L” (observações referentes aos lançamentos fiscais da nota) |
| --- | --- |
| COD_OBS | Código da observação parametrizada pelo usuário para os ajustes de estorno do crédito (devoluções) (parametrização descrita no item 3). |
| TXT_COMPL | (sem informação) |


| COD_AJ | Código do ajuste de estorno do crédito (devoluções) parametrizado pelo usuário (parametrização descrita no item 3). |
| --- | --- |
| DESCR_COMPL_AJ | Descrição complementar do ajuste de estorno do crédito (devoluções) parametrizada pelo usuário (parametrização descrita no item 3). |
| COD_ITEM | Indicador e Código do produto em questão (produto do item da nota fiscal de devolução processada) |
| VL_BC_ICMS | Valor da base de cálculo do ajuste de estorno do crédito (devoluções), conforme cálculo definido no item “5-Recuperação dos Dados e Processamento (Ajustes de Estorno das Devoluções)”. |
| ALIQ_ICMS | Valor da alíquota do ajuste de estorno do crédito (devoluções), conforme cálculo definido no item “5-Recuperação dos Dados e Processamento (Ajustes de Estorno das Devoluções)”. |
| VL_ICMS | Valor do ICMS do ajuste de estorno do crédito (devoluções), conforme cálculo definido no item “5-Recuperação dos Dados e Processamento ( Ajustes de Estorno das Devoluções)”. |


| Código da Empresa | Código da empresa do login |
| --- | --- |
| Código do Estabelecimento | Código do estabelecimento processado  No caso de geração por inscrição estadual única, será o estabelecimento centralizador. |
| Tipo do Livro Fiscal (OBRIGACAO_FISCAL) | “108”, ou “165”, no caso de geração por Inscrição Estadual Única. |
| Data da Apuração | Data final do período informado na tela da geração |
| Item da Apuração  (ITEM_OPER_APUR) | Item da apuração parametrizado p/o lançamento de ressarcimento (parametrização descrita no item 6). |
| Descrição do Lançamento | Descrição parametrizada p/o lançamento de ressarcimento (parametrização descrita no item 6). |
| N. Discriminação (NUM_DISCRIMINAÇÃO) | Sequencial do lançamento gerado da seguinte forma: a coluna NUM_DISCRIMINACAO é um sequencial dos lançamentos feitos para um mesmo código de operação.  Para preenchê-la deve-se recuperar o maior sequencial existente na tabela dos lançamentos para o código de operação que se deseja gravar, incrementar um, e gravar o registro. |
| Classe de Lançamento | Código da classe parametrizado p/o lançamento de ressarcimento (parametrização descrita no item 6). |
| Código do Amparo Legal | Código do amparo legal parametrizado p/o lançamento de ressarcimento (parametrização descrita no item 6). |
| Subitem do Amparo | Código do sub-item do amparo legal parametrizado p/o lançamento de ressarcimento (parametrização descrita no item 6). |
| Tipo do lançamento | “1” (lançamento referente aos ajustes demonstrados no registro C197) |
| Valor do Lançamento (VLR_LANCTO) | Valor do lançamento de ressarcimento conforme cálculo descrito no item 6.  Alteração da MFS47510: Desconsiderar os valores de ajuste referentes a códigos de ajuste em que o terceiro caracter igual a “9” (=Informativo) E o quarto caracater igual a “9” (=Informativo). |
| Tipo de Informação  (IND_DIG_CALCULADO) | “C” (para diferenciar estes lançamentos, será utilizada a letra “C”, o que possibilitará efetuar o procedimento de limpeza a cada reexecução do processo) |


| Código da Empresa | Código da empresa do login |
| --- | --- |
| Código do Estabelecimento | Código do estabelecimento processado  No caso de geração por inscrição estadual única, será o estabelecimento centralizador. |
| Tipo do Livro Fiscal (OBRIGACAO_FISCAL) | “108, ou “165”, no caso de geração por Inscrição Estadual Única |
| Data da Apuração | Data final do período informado na tela da geração |
| Item da Apuração  (ITEM_OPER_APUR) | Item da apuração parametrizado p/o lançamento de crédito (parametrização descrita no item 6). |
| Descrição do Lançamento | Descrição parametrizado p/o lançamento de crédito (parametrização descrita no item 6). |
| N. Discriminação (NUM_DISCRIMINAÇÃO) | Sequencial do lançamento gerado da seguinte forma: a coluna NUM_DISCRIMINACAO é um sequencial dos lançamentos feitos para um mesmo código de operação.  Para preenchê-la deve-se recuperar o maior sequencial existente na tabela dos lançamentos para o código de operação que se deseja gravar, incrementar um, e gravar o registro. |
| Classe de Lançamento | Código da classe parametrizado p/o lançamento de crédito (parametrização descrita no item 6). |
| Código do Amparo Legal | Código do amparo legal parametrizado p/o lançamento de crédito (parametrização descrita no item 6). |
| Subitem do Amparo | Código do sub-item do amparo legal parametrizado p/o lançamento de crédito (parametrização descrita no item 6). |
| Tipo do lançamento | “1” (lançamento referente aos ajustes demonstrados no registro C197) |
| Valor do Lançamento (VLR_LANCTO) | Valor do lançamento de crédito conforme cálculo descrito no item 6.   Alteração da MFS47510: Desconsiderar os valores de ajuste referentes a códigos de ajuste em que o terceiro caracter igual a “9” (=Informativo) E o quarto caracater igual a “9” (=Informativo). |
| Tipo de Informação  (IND_DIG_CALCULADO) | “C”  (para diferenciar estes lançamentos, será utilizada a letra “C”, o que possibilitará efetuar o procedimento de limpeza a cada reexecução do processo) |


| Código da Empresa | Código da empresa do login |
| --- | --- |
| Código do Estabelecimento | Código do estabelecimento processado  No caso de geração por inscrição estadual única, será o estabelecimento centralizador. |
| Tipo do Livro Fiscal (OBRIGACAO_FISCAL) | “108”, ou “165”, no caso de geração por Inscrição Estadual Única. |
| Data da Apuração | Data final do período informado na tela da geração |
| Item da Apuração  (ITEM_OPER_APUR) | Item da apuração parametrizado p/o lançamento de Estorno de Ressarcimento (Devoluções). (parametrização descrita no item 6). |
| Descrição do Lançamento | Descrição parametrizada p/o lançamento de Estorno de Ressarcimento (Devoluções). (parametrização descrita no item 6). |
| N. Discriminação (NUM_DISCRIMINAÇÃO) | Sequencial do lançamento gerado da seguinte forma: a coluna NUM_DISCRIMINACAO é um sequencial dos lançamentos feitos para um mesmo código de operação.  Para preenchê-la deve-se recuperar o maior sequencial existente na tabela dos lançamentos para o código de operação que se deseja gravar, incrementar um, e gravar o registro. |
| Classe de Lançamento | Código da classe parametrizado p/o lançamento de Estorno de Ressarcimento (Devoluções). (parametrização descrita no item 6). |
| Código do Amparo Legal | Código do amparo legal parametrizado p/o lançamento de Estorno de Ressarcimento (Devoluções). (parametrização descrita no item 6). |
| Subitem do Amparo | Código do sub-item do amparo legal parametrizado p/o lançamento de Estorno de Ressarcimento (Devoluções).  (parametrização descrita no item 6). |
| Tipo do lançamento | “1” (lançamento referente aos ajustes demonstrados no registro C197) |
| Valor do Lançamento (VLR_LANCTO) | Valor do lançamento de Estorno de Ressarcimento (Devoluções), conforme cálculo descrito no item “6-Recuperação dos Dados e Processamento (Lançamento na Apuração do CIMS)”.  Alteração da MFS47510: Desconsiderar os valores de ajuste referentes a códigos de ajuste em que o terceiro caracter igual a “9” (=Informativo) E o quarto caracater igual a “9” (=Informativo). |
| Tipo de Informação  (IND_DIG_CALCULADO) | “C” (para diferenciar estes lançamentos, será utilizada a letra “C”, o que possibilitará efetuar o procedimento de limpeza a cada reexecução do processo) |


| Código da Empresa | Código da empresa do login |
| --- | --- |
| Código do Estabelecimento | Código do estabelecimento processado  No caso de geração por inscrição estadual única, será o estabelecimento centralizador. |
| Tipo do Livro Fiscal (OBRIGACAO_FISCAL) | “108”, ou “165”, no caso de geração por Inscrição Estadual Única. |
| Data da Apuração | Data final do período informado na tela da geração |
| Item da Apuração  (ITEM_OPER_APUR) | Item da apuração parametrizado p/o lançamento de Estorno de Crédito (Devoluções). (parametrização descrita no item 6). |
| Descrição do Lançamento | Descrição parametrizada p/o lançamento de Estorno de Crédito (Devoluções). (parametrização descrita no item 6). |
| N. Discriminação (NUM_DISCRIMINAÇÃO) | Sequencial do lançamento gerado da seguinte forma: a coluna NUM_DISCRIMINACAO é um sequencial dos lançamentos feitos para um mesmo código de operação.  Para preenchê-la deve-se recuperar o maior sequencial existente na tabela dos lançamentos para o código de operação que se deseja gravar, incrementar um, e gravar o registro. |
| Classe de Lançamento | Código da classe parametrizado p/o lançamento de Estorno de Crédito (Devoluções). (parametrização descrita no item 6). |
| Código do Amparo Legal | Código do amparo legal parametrizado p/o lançamento de Estorno de Crédito (Devoluções). (parametrização descrita no item 6). |
| Subitem do Amparo | Código do sub-item do amparo legal parametrizado p/o lançamento de Estorno de Crédito (Devoluções).  (parametrização descrita no item 6). |
| Tipo do lançamento | “1” (lançamento referente aos ajustes demonstrados no registro C197) |
| Valor do Lançamento (VLR_LANCTO) | Valor do lançamento de Estorno de Crédito (Devoluções), conforme cálculo descrito no item “6-Recuperação dos Dados e Processamento (Lançamento na Apuração do CIMS)”.  Alteração da MFS47510: Desconsiderar os valores de ajuste referentes a códigos de ajuste em que o terceiro caracter igual a “9” (=Informativo) E o quarto caracater igual a “9” (=Informativo). |
| Tipo de Informação  (IND_DIG_CALCULADO) | “C” (para diferenciar estes lançamentos, será utilizada a letra “C”, o que possibilitará efetuar o procedimento de limpeza a cada reexecução do processo) |


| Código da Empresa | Código da empresa do login |
| --- | --- |
| Código do Estabelecimento | Código do estabelecimento processado  No caso de geração por inscrição estadual única, será o estabelecimento centralizador. |
| Tipo do Livro Fiscal (OBRIGACAO_FISCAL) | “108”, ou “165”, no caso de geração por Inscrição Estadual Única. |
| Data da Apuração | Data final do período informado na tela da geração |
| Item da Apuração  (ITEM_OPER_APUR) | Item da apuração parametrizado p/o lançamento de estorno do ressarcimento (parametrização descrita no item 6). |
| Descrição do Lançamento | Descrição parametrizada p/o lançamento de estorno do ressarcimento (parametrização descrita no item 6). |
| N. Discriminação (NUM_DISCRIMINAÇÃO) | Sequencial do lançamento gerado da seguinte forma: a coluna NUM_DISCRIMINACAO é um sequencial dos lançamentos feitos para um mesmo código de operação.  Para preenchê-la deve-se recuperar o maior sequencial existente na tabela dos lançamentos para o código de operação que se deseja gravar, incrementar um, e gravar o registro. |
| Classe de Lançamento | Código da classe parametrizado p/o lançamento de estorno do ressarcimento (parametrização descrita no item 6). |
| Código do Amparo Legal | Código do amparo legal parametrizado p/o lançamento de estorno do ressarcimento (parametrização descrita no item 6). |
| Subitem do Amparo | Código do sub-item do amparo legal parametrizado p/o lançamento de estorno do ressarcimento (parametrização descrita no item 6). |
| Tipo do lançamento | “3” (diferente dos lançamentos do ressarcimento e do crédito, este lançamento terá o tipo = 3) |
| Valor do Lançamento (VLR_LANCTO) | Este lançamento terá o mesmo valor do lançamento de ressarcimento, já que seu objetivo é exatamente estornar o ressarcimento. Alteração MFS9749: O valor do lançamento passou a considerar também o estorno das devoluções, quando for o caso.  Este lançamento terá o seguinte valor:  (Valor do Lançamento de Ressarcimento)  –  (Valor do Lançamento de Estorno de Ressarcimento (Devoluções)) |
| Código de Ajuste do Sped Fiscal | Código de ajuste parametrizado p/o lançamento de estorno do ressarcimento (parametrização descrita no item 6).  Obs: Observar que este lançamento, diferente dos lançamentos do ressarcimento e do crédito, tem um código de ajuste. É porque os outros lançamentos são do tipo “1”, ou seja, vinculados a ajustes do C197, e este será do tipo “3”. |
| Tipo de Informação  (IND_DIG_CALCULADO) | “C” (para diferenciar estes lançamentos, será utilizada a letra “C”, o que possibilitará efetuar o procedimento de limpeza a cada reexecução do processo) |


| NF (saída) | Número, série e subsérie da nota fiscal de saída. |
| --- | --- |
| Dt. Emissão | Data de emissão da nota fiscal de saída |
| Pessoa Fis/Jur | Indicador e código da pessoa fis/jur da nota fiscal de saída |
| Item | Número do item da nota fiscal de saída |
| CFOP | CFOP do item da nota fiscal de saída |
| Natureza | Natureza de operação do item da nota fiscal de saída |
| Produto | Dados de identificação do produto: -Indicador -Código -Descrição |
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
| Base ICMS | Base de cálculo do ICMS do item da nota fiscal de entrada.      (campo incluído no relatório pela MFS9986)   O valor da base de cálculo do ICMS será recuperado do campo “Base ICMS não Destacado” (campo 226) ou da “Base ICMS Outras” do item da nota, de acordo com a regra definida no preenchimento dos dados para o registro C176 (ver item “7-Gravação dos Dados”, subitem “Gravação dos Dados Referentes ao Registro C176”). |
| Bse ICMS-ST | Base de cálculo do ICMS-ST do item da nota fiscal de entrada.  O valor da base de cálculo do ST será recuperado do campo 61, 144 ou 106 do item da nota, de acordo com a regra definida no preenchimento dos dados para o registro C176 (ver item “7-Gravação dos Dados”, subitem “Gravação dos Dados Referentes ao Registro C176”). |
| Aliq ICMS-ST | Alíquota de ICMS-ST interna do produto Menu: Parâmetros > Registro C176 > Produto ou NCM´s. |
| Vlr Unit BC ICMS (campo 12) | Valor calculado para o campo “12- Valor unitário da base de cálculo da operação própria do remetente sob o regime comum de tributação.” do registro C176, conforme definido na gravação dos dados do registro C176 (ver item “7-Gravação dos Dados”, subitem “Gravação dos Dados Referentes ao Registro C176”). |
| Vlr Unit Merc (campo 08) | Valor calculado para o campo “08-Valor unitário da entrada” do registro C176, conforme definido na gravação dos dados do registro C176 (ver item “7-Gravação dos Dados”, subitem “Gravação dos Dados Referentes ao Registro C176”):       [ valor da coluna “Preço Unitário” + (valor da coluna “Despesas Acess” / valor da coluna “Quantidade”) ] |
| BC ST Unit (campo 09) | Valor calculado para o campo “09-Valor unitário da base de cálculo do ICMS-ST da entrada” do registro C176, conforme definido na gravação dos dados do registro C176 (ver item “7-Gravação dos Dados”, subitem “Gravação dos Dados Referentes ao Registro C176”):                               valor da coluna “Base ICMS-ST” / valor da coluna “Quantidade” |
| Vlr Unit Limite BC ICMS (campo 14) | Valor calculado para o campo “14- Valor unitário da base de cálculo do ICMS relativo à última entrada da mercadoria” do registro C176, conforme definido na gravação dos dados do registro C176 (ver item “7-Gravação dos Dados”, subitem “Gravação dos Dados Referentes ao Registro C176”). |
| Vlr Unit Cred (campo 15) | Valor calculado para o campo “15- Valor unitário do crédito de ICMS sobre operações próprias do remetente da entrada” do registro C176, conforme definido na gravação dos dados do registro C176 (ver item “7-Gravação dos Dados”, subitem “Gravação dos Dados Referentes ao Registro C176”):                               valor da coluna [(Vlr Unit Limite BC ICMS * Aliq ICMS) / 100] |
| Vlr Unit Res. (campo 17) | Valor calculado para o campo “17- Valor unitário do ressarcimento (parcial ou completo) de ICMS decorrente da quebra da ST da entrada” do registro C176, conforme definido na gravação dos dados do registro C176 (ver item “7-Gravação dos Dados”, subitem “Gravação dos Dados Referentes ao Registro C176”):                               valor da coluna [(BC ST Unit * Aliq ICMS-ST) / 100] - valor da coluna ‘Vlr Unit Cred’ |


| Linha “Totais” | Esta linha demonstra os totais das colunas “K” e “L” por nota fiscal.  O motivo de demonstrar estes totais por nota é para que o usuário possa visualizar os valores totalizados por nota fiscal mesmo o registro C176 e o relatório serem por item. |
| --- | --- |


| Linha “Ressarcimento” | Nesta linha serão demonstradas as informações geradas para o ajuste de ressarcimento.   São os valores gravados na SAFX113 para o ajuste de ressarcimento, conforme definido no item “7-Gravação dos Dados”, subitem “Gravação dos Dados Referentes aos Ajustes”:   Campos:  - Cód. Ajuste à campo COD_AJ do ajuste de ressarcimento; - Base de Cálculo à campo VL_BC_ICMS do ajuste de ressarcimento; - Alíquota à campo ALIQ_ICMS do ajuste de ressarcimento; - Valor do Ajuste à campo VL_ICMS do ajuste de ressarcimento; |
| --- | --- |
| Linha “Crédito” | Nesta linha serão demonstradas as informações geradas para o ajuste de crédito.   São os valores gravados na SAFX113 para o ajuste de crédito, conforme definido no item “7-Gravação dos Dados”, subitem “Gravação dos Dados Referentes aos Ajustes”:   Campos:  - Cód. Ajuste à campo COD_AJ do ajuste de crédito; - Base de Cálculo à campo VL_BC_ICMS do ajuste de crédito; - Alíquota à campo ALIQ_ICMS do ajuste de crédito; - Valor do Ajuste à campo VL_ICMS do ajuste de crédito; |


| Linha “Ressarcimento” | Valor total de todos os ajustes de ressarcimento gerados para o estabelecimento.  Este valor corresponde ao lançamento complementar gerado na Apuração do ICMS, com o total dos ajustes de ressarcimento, conforme definido no item “7-Gravação dos Dados”, subitem “Gravação dos Dados Referentes aos Lançamentos Complementares da Apuração do ICMS”. |
| --- | --- |
| Linha “Crédito” | Valor total de todos os ajustes de crédito gerados para o estabelecimento.  Este valor corresponde ao lançamento complementar gerado na Apuração do ICMS, com o total dos ajustes de crédito, conforme definido no item “7-Gravação dos Dados”, subitem “Gravação dos Dados Referentes aos Lançamentos Complementares da Apuração do ICMS”. |


| NF Devolução | Número, série e subsérie da nota fiscal de devolução |
| --- | --- |
| Data Fiscal | Data fiscal da nota de devolução |
| Pessoa Fis/Jur | Indicador e código da pessoa fis/jur da nota fiscal de devolução |
| Item | Número do item da nota fiscal de devolução |
| CFOP | CFOP do item da nota fiscal de devolução |
| Natureza | Natureza de operação do item da nota fiscal de devolução |
| Produto | Dados de identificação do produto do item da nota fiscal de devolução: -Indicador -Código -Descrição |
| Quantidade | Quantidade do item da nota fiscal de devolução |
| UN | Código da unidade de medida do item da nota fiscal de devolução |


| NF (saída) | Número, série e subsérie da nota fiscal de saída |
| --- | --- |
| Data Fiscal | Data fiscal da nota fiscal de saída |
| Pessoa Fis/Jur | Indicador e código da pessoa fis/jur da nota fiscal de saída |
| Item | Número do item da nota fiscal de saída |
| CFOP | CFOP do item da nota fiscal de saída |
| Natureza | Natureza de operação do item da nota fiscal de saída |
| Quantidade da Saída | Quantidade do item da nota fiscal de saída |
| Quantidade Devolvida (SAFX192) | Quantidade da devolução referente ao item da nota fiscal de saída (esta é a quantidade informada na SAFX192, campo “24-Quantidade Devolvida”) |
| Valor | Nestas colunas serão demonstradas as informações referentes ao ajuste de ressarcimento (SAFX113) gerado para o item da nota fiscal de saída.   Conteúdo das colunas:  - Valor à campo “Valor do ICMS” do ajuste de ressarcimento;  - Base de Cálculo à campo “Base de Cálculo do ICMS” do ajuste de ressarcimento; - Alíq. à campo “Alíquota do ICMS” do ajuste de ressarcimento; |
| Base de Cálculo | Nestas colunas serão demonstradas as informações referentes ao ajuste de ressarcimento (SAFX113) gerado para o item da nota fiscal de saída.   Conteúdo das colunas:  - Valor à campo “Valor do ICMS” do ajuste de ressarcimento;  - Base de Cálculo à campo “Base de Cálculo do ICMS” do ajuste de ressarcimento; - Alíq. à campo “Alíquota do ICMS” do ajuste de ressarcimento; |
| Alíq. | Nestas colunas serão demonstradas as informações referentes ao ajuste de ressarcimento (SAFX113) gerado para o item da nota fiscal de saída.   Conteúdo das colunas:  - Valor à campo “Valor do ICMS” do ajuste de ressarcimento;  - Base de Cálculo à campo “Base de Cálculo do ICMS” do ajuste de ressarcimento; - Alíq. à campo “Alíquota do ICMS” do ajuste de ressarcimento; |
| Valor | Nestas colunas serão demonstradas as informações referentes ao ajuste de crédito (SAFX113) gerado para o item da nota fiscal de saída.   Conteúdo das colunas:  - Valor à campo “Valor do ICMS” do ajuste de crédito;  - Base de Cálculo à campo “Base de Cálculo do ICMS” do ajuste de crédito; - Alíq. à campo “Alíquota do ICMS” do ajuste de crédito; |
| Base de Cálculo | Nestas colunas serão demonstradas as informações referentes ao ajuste de crédito (SAFX113) gerado para o item da nota fiscal de saída.   Conteúdo das colunas:  - Valor à campo “Valor do ICMS” do ajuste de crédito;  - Base de Cálculo à campo “Base de Cálculo do ICMS” do ajuste de crédito; - Alíq. à campo “Alíquota do ICMS” do ajuste de crédito; |
| Alíq. | Nestas colunas serão demonstradas as informações referentes ao ajuste de crédito (SAFX113) gerado para o item da nota fiscal de saída.   Conteúdo das colunas:  - Valor à campo “Valor do ICMS” do ajuste de crédito;  - Base de Cálculo à campo “Base de Cálculo do ICMS” do ajuste de crédito; - Alíq. à campo “Alíquota do ICMS” do ajuste de crédito; |


| Valor | Valor do estorno de ressarcimento calculado para a saída |
| --- | --- |
| Base de Cálculo | Valor da base de cálculo referente ao estorno de ressarcimento calculado |
| Valor | Valor do estorno de crédito calculado para a saída |
| Base de Cálculo | Valor da base de cálculo referente ao estorno de crédito calculado |


| Linha “Ressarcimento” | Nesta linha serão demonstradas as informações geradas para o ajuste de ressarcimento.   São os valores gravados na SAFX113 para o ajuste de estorno do ressarcimento, conforme definido no item “7-Gravação dos Dados”, subitem “Gravação dos Dados referentes aos Ajustes de Estorno das Devoluções (C195/C197)”:  Campos:  - Cód. Ajuste à campo COD_AJ do ajuste de ressarcimento; - Base de Cálculo à campo VL_BC_ICMS do ajuste de ressarcimento; - Alíq. à campo ALIQ_ICMS do ajuste de ressarcimento; - Valor à campo VL_ICMS do ajuste de ressarcimento; |
| --- | --- |
| Linha “Crédito” | Nesta linha serão demonstradas as informações geradas para o ajuste de crédito.   São os valores gravados na SAFX113 para o ajuste de estorno do crédito, conforme definido no item “7-Gravação dos Dados”, subitem “Gravação dos Dados Referentes aos Ajustes de Estorno das Devoluções (C195/C197)”:   Campos:  - Cód. Ajuste à campo COD_AJ do ajuste de crédito; - Base de Cálculo à campo VL_BC_ICMS do ajuste de crédito; - Alíq. à campo ALIQ_ICMS do ajuste de crédito; - Valor à campo VL_ICMS do ajuste de crédito; |


| Linha “Ressarcimento” | Valor total de todos os ajustes de estorno de ressarcimento gerados para o estabelecimento.  Este valor corresponde ao lançamento complementar gerado na Apuração do ICMS, com o total dos ajustes de estorno de ressarcimento, conforme definido no item “7-Gravação dos Dados”, subitem “Gravação dos Dados Referentes aos Lançamentos Complementares da Apuração do ICMS”. |
| --- | --- |
| Linha “Crédito” | Valor total de todos os ajustes de estorno de crédito gerados para o estabelecimento.  Este valor corresponde ao lançamento complementar gerado na Apuração do ICMS, com o total dos ajustes de estorno de crédito, conforme definido no item “7-Gravação dos Dados”, subitem “Gravação dos Dados Referentes aos Lançamentos Complementares da Apuração do ICMS”. |
