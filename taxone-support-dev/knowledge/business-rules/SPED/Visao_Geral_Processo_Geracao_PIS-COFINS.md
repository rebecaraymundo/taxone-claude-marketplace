# Visao_Geral_Processo_Geracao_PIS-COFINS

> Fonte: Visao_Geral_Processo_Geracao_PIS-COFINS.doc

Revisões

Data	Descrição	Autor		24/01/2011	Criação.	Pedro Nascimento		

Controle de Alterações  
 TITLE  \* MERGEFORMAT Documentação Técnica - PIS/COFINS –  SUBJECT  \* MERGEFORMAT Visão Geral dos Objetos de Geração PIS/COFINS
  COMMENTS  \* MERGEFORMAT SPED - EFD-PISPASEP-COFINS

Desenvolvimento nas Releases:  KEYWORDS  \* MERGEFORMAT 2.01.0
 TOC \o "1-4" \h \z  HYPERLINK \l "_Toc315793425" 1.	Modelagem de Dados	 PAGEREF _Toc315793425 \h 2
 HYPERLINK \l "_Toc315793426" 2.	Parametrizações Utilizadas no PIS/COFINS	 PAGEREF _Toc315793426 \h 3
 HYPERLINK \l "_Toc315793427" 2.1	Dados Iniciais	 PAGEREF _Toc315793427 \h 3
 HYPERLINK \l "_Toc315793428" 2.2	Identificador do Tipo de Operação	 PAGEREF _Toc315793428 \h 6
 HYPERLINK \l "_Toc315793429" 2.3	Identificador da Natureza da Base do Crédito	 PAGEREF _Toc315793429 \h 6
 HYPERLINK \l "_Toc315793430" 2.4	Registros C500	 PAGEREF _Toc315793430 \h 7
 HYPERLINK \l "_Toc315793431" 2.5	Registros F100	 PAGEREF _Toc315793431 \h 8
 HYPERLINK \l "_Toc315793432" 2.6	Identificador da Natureza da Receita	 PAGEREF _Toc315793432 \h 8
 HYPERLINK \l "_Toc315793433" 2.7	Identificador dos Tipos de Crédito	 PAGEREF _Toc315793433 \h 9
 HYPERLINK \l "_Toc315793434" 2.8	Identificador dos Tipos de Contribuição	 PAGEREF _Toc315793434 \h 12


Modelagem de Dados
O PIS/COFINS faz uso de algumas tabelas específicas para gravação de dados da apuração, conforme modelo abaixo:


Parametrizações Utilizadas no PIS/COFINS
Dados Iniciais
Localização
Módulo: SPED – EFD-PIS/PASEP-COFINS
Menu: Parâmetros ( Dados Iniciais

Definição:
Parametrização que contém uma série de itens que determinam o comportamento do processo de geração e da apuração nos vários registros. Esta parametrização será feita para os estabelecimentos centralizador da geração apenas, não cabendo parametrizar os demais. Abaixo segue a lista de parâmetros disponíveis e suas finalidades:

Registro 0110
Os itens deste quadro determinam informações a respeito do conjunto de operações que a empresa pratica, e seu preenchimento influencia diretamente na apuração. Os parâmetros indicam se a empresa possui operações com incidência de PIS/COFINS Cumulativo e/ou Não Cumulativo, se o método de apropriação é direto ou proporcional à receita bruta da empresa.

Dicas
Hoje não atendemos o método de apropriação direta, apenas o método proporcional à receita bruta;
O método através da receita bruta realiza o cálculo de um percentual utilizado para segregar os créditos em operações Cumulativas e Não Cumulativas, conforme regras RNM105-04, RNM105-05, RNM505-04 e RNM505-05 (regras dos registros M105/M505). Hoje este cálculo é feito no método EpcAP_RegraDicionario.calcularPercentualReceitaBruta.

Registro 0200
Determina os valores a serem gravados para produtos e serviços.

Dicas
Quando o campo código da natureza do serviço está em branco o código do serviço sai no registro assim “|S-|”.

Registro A100, C100...
Determina se para geração destes registros consideraremos as notas com data de emissão ou data de lançamento dentro do período, note que na recuperação (cursor) lemos todas as notas que possuam qualquer uma das datas dentro do período.

Dicas
O tratamento desta regra encontra-se nas packages EpcXX_RegraDicionario.valInclusaoRegistro_XXXX.

Registro C010
Indica se os registros de notas fiscais eletrônicas e cupons fiscais serão gerados de forma consolidada ou aberta. Para notas fiscais a geração será feita nos registros C100 ou C180/C190 e filhos, para cupons os registros gerados serão C400 ou C490 e seus filhos. Observe que esta regra afeta apenas NF eletrônica, modelo 55, desta forma o comportamento da aplicada desta regra é o seguinte:

1 – Apuração com base nos registros de consolidações C180 e C190:
Ao utilizar esta opção o arquivo será gerado da seguinte forma:
Registros C100/C170 contendo notas fiscais com modelos 01, 1B e 04;
Registros C180/C190 contendo notas fiscais com modelo 55.

2 – Apuração com base no registro individualizado:
Quando utilizada esta opção os registros C100/C170 irão conter notas de classificação 01, 1B, 04 e 55. O registros C180 e C190 não serão gerados.

Dicas
O tratamento para os modelos a serem gerados nos registros C100/C170 está contida na função EpcDF_RegraDicionario.valTipoApuracao_C100_C170;
Existem rotinas específicas para gerarmos cada um dos tipos de registros, EpcDF ou EpcNE para notas fiscais, e EpcEI e EpcEC para cupons;
A decisão de qual destas rotinas será chamada está inserida na package Epc_Dicionario, através das funções avaliarCondicoesEspecGrp_EPCNE, avaliarCondicoesEspecGrp_EPCEI e avaliarCondicoesEspecGrp_EPCEC;
Não existe uma rotina de decisão para a EPCDF visto que esta sempre será chamada, a rotina EpcNE diz respeito apenas as notas eletrônicas, as demais notas são geradas pela EpcDF.

Registro C600, C601 e C605
Indica se estes registros serão gerados a partir da SAFX42/SAFX43 ou SAFX190/SAFX191.

Dicas
Existem rotinas específicas para gerarmos cada um dos tipos de registros, EpcUT para SAFX42/SAFX43 e EpcUE para SAFX190/SAFX191;
A decisão de qual destas rotinas será chamada está inserida na package Epc_Dicionario, através das funções avaliarCondicoesEspecGrp_EPCUT, avaliarCondicoesEspecGrp_EPCUE.

Registro D600, D601 e D605
Indica se estes registros serão gerados a partir da SAFX42/SAFX43 ou SAFX161/SAFX162.

Dicas
Existem rotinas específicas para gerarmos cada um dos tipos de registros, EpcUT para SAFX42/SAFX43 e EpcUC para SAFX161/SAFX162;
A decisão de qual destas rotinas será chamada está inserida na package Epc_Dicionario, através das funções avaliarCondicoesEspecGrp_EPCUT, avaliarCondicoesEspecGrp_EPCUC.

Registro F100
Indica se para a geração dos registros F100 será utilizada a parametrização por Tipo de Documento ou por Conta Contábil e Centro de Custo.

Dicas
Estas parametrizações são utilizadas para determinação do CST, alíquota entre outras informações;
No caso das alíquotas, caso a alíquota esteja informada na SAFX147, será então utilizadas esta alíquota, e não a da parametrização;
A geração destes registros é feita pelas package EpcDD.

Registro F120/F130
Estes registros possuem a mesma origem, esta parametrização indica a forma com a qual estes registros será gerada, se agrupada ou detalhada.

Dicas
A geração destes registros é feita pelas package EpcDD.

Registro da Natureza da Base do Crédito
A natureza da base de crédito é utilizada para o detalhamento das bases de cálculo dos créditos, totalizadas nos registros M105 e M505. Esta natureza em alguns dos registros do PIS/COFINS é informada de maneira explícita, ou seja, está contida em um campo do registro, em outros é deduzida através de parametrização por Código do Serviço ou Por CFOP/Natureza. Este campo indica se a natureza da base do crédito será obtida das notas fiscais e outras origens ou se será determinada com base nestas parametrizações.

Dicas
A rotina que trata esta parametrização está na package Epc_Parametros, funções getParamCFOPBaseCredito e getParamServBaseCredito, estas rotinas são chamadas pelas package EpcXX_Dados para que seja determinado código da natureza da receita.

Registro M410 e M810
Este parâmetro é muito parecido com o anterior, ou seja, indicará se o código da Natureza da Receita, contido nos registros M410 e M810 serão obtidos a partir das notas fiscais e demais documentos e operações ou através da parametrização do Identificador da Natureza da Receita.

Dicas
A rotina que trata esta parametrização está na package Epc_Parametros, método setParamNaturezaReceita, que chamado a partir da package EpcAP_Dados, no método processarApuracaoRegistro, onde temos um para cada tipo de dicionário de dados (EPCXX) previsto no PIS/COFINS.

Obs.: Vide o item correspondente a parametrização da natureza da receita, esta parametrização é complexa e merece estudo.

Registro 0450, A110, C110, ..., D500
Este parâmetro indica se o código da observação (SAFX2009), que possui tamanho 8, será justificado à direita ou esquerda na gravação dos registros do PIS/COFINS, com tamanho 6.

Registro M200 e M600
Este parâmetro indica o comportamento para o cálculo dos descontos dos créditos e deduções das retenções que são realizados na apuração dos registros M200/M600. Estes registros possuem o resultado final da apuração, apurado a partir do confrontado das Contribuições (Débitos) com os créditos do período, créditos de períodos anteriores e deduções.
O cálculo da apuração realizado pelo mastersaf foi concebido com base no entendimento inicial da ordem de aplicação dos descontos dos créditos e das deduções, num segundo momento foi verificado que esta ordem não é pré-determinada, e que as empresas podem estabelecer estratégias diferentes de aplicação destes descontos e deduções.
A criação deste parâmetro viabiliza ao cliente optar entre realizar o cálculo automático determinado pela regra RNG-M200 ou não. O cálculo automático realiza descontos de créditos do período e deduções sem que haja interferência do usuário, restando a este apenas lançar descontos de créditos de períodos anteriores quando estes existirem e quando houver saldo de contribuições para serem descontadas, caso o usuário utilize-se deste parâmetro, os descontos e deduções do período não serão realizados, e o usuário terá como realizá-los um a um manualmente, na ordem que lhe convier, e o sistema irá apenas calcular o resultado final com base nestes lançamentos individualizados.

Dicas
O cálculo da apuração é realizado pela package Epc_Calculo_Apuracao, esta package contém os métodos recalcularPIS_Geracao e recalcularCOFINS_Geracao para o cálculo realizado durante a geração dos registros, e outros dois métodos chamados recalcularPIS_Manutencao e recalcularCOFINS_Manutencao que são acionados através da tela de manutenção da apuração do PIS e da COFINS, no menu Obrigações ( Manutenção ( Apuração COFINS e Apuração PIS/PASEP;
A diferença entre os métodos Geração e Manutenção encontra-se na forma de apresentação das mensagens de erro, que na geração são gravadas no log e processo, e na manutenção são retornadas em forma de texto para que a tela as exiba ao usuário;
Outro detalhe importante é que o controle de COMMIT e ROLLBACK é realizado por esta rotina, ou seja, na tela de manutenção o salvamento só é efetivado quando o resultado do recálculo for efetuado sem erros.

Identificador do Tipo de Operação
Localização
Módulo: SPED – EFD-PIS/PASEP-COFINS
Menu: Parâmetros ( Identificador do Tipo de Operação ( Por CFOP ou Por Extensão/CFOP

Definição:
Esta parametrização é responsável por definir o tipo de operação como devolução de venda, devolução de compra ou geradora de receita, e sua finalidade será determinar as notas a serem geradas nos registros C100, C180, C190 e C380 e seus filhos.

Dicas
A função que retorna os valores das operações através deste parâmetro está contida na package Epc_Parametros, no método getParamCFOPTipoOperacao;
A chamada deste método é feita nas rotinas que determinam e classificam as notas para geração nos registros citados acima, ou seja, estão contidas nas packages EpcDF_RegraDicionario (C100 e C380) e EpcNE_RegraDicionario (C180 e C190), nos métodos valInclusaoRegistro_XXXX correspondentes aos registros.

Obs.: Atentar para a forma como estas parametrizações são obtidas, o comentário contido na package nos ajuda a entedê-la. Este comentário está contido na procedure setParaCFOPTipoOperacao:

-- Carrega um vetor com os parâmetros por CFOP e Natureza para o COD_PARAM = 475
-- O vetor é indexado pelo próprio código do CFOP, sendo guardadas as naturezas caso for necessário, exemplo:
-- parâmetros por CFOP:
--    paramCFOPTipoOperacao(5303) = |3| (onde 3 é o conteúdo do campo IND_DESTINACAO)
--    paramCFOPTipoOperacao(5307) = |1| (onde 1 é o conteúdo do campo IND_DESTINACAO)
-- parâmetros por CFOP/Natureza:
--    paramCFOPTipoOperacao(5303) = |002,VCF,3|002,VFD,1|
--    paramCFOPTipoOperacao(5307) = |002,VCF,1|002,VFD,3|
--
--    No exmplo acima a sequência |002,VCF,1| representa:
--    - 002 = GRUPO_NATUREZA_OP
--    - VCF = COD_NATUREZA_OP
--    - 1   = IND_DESTINACAO

Identificador da Natureza da Base do Crédito
Localização
Módulo: SPED – EFD-PIS/PASEP-COFINS
Menu: Parâmetros ( Identificador do Tipo de Operação ( Por CFOP, Por Extensão/CFOP ou Por Serviço

Definição:
Esta parametrização é responsável por definir a natureza da base do crédito, e sua finalidade é a de gerar o detalhamento das bases de cálculo do crédito contidas nos registros M105 e M505. 

Dicas
A lista dos CFOPs para determinação das naturezas é prevista na legislação, e o validador já trata tais casos, ocorre que pode ser gerada diferença caso a parametrização do cliente não reflita as regras do PVA;
Esta parametrização é opcional, ou seja, o cliente pode carregar a natureza diretamente na nota, vide dados iniciais;
A função que retorna os valores das naturezas através deste parâmetro está contida na package Epc_Parametros, nos métodos getParamCFOPBaseCredito e getParamServBaseCredito;
A chamada deste método é feita nas rotinas que tratam dos dados dos registros, ou seja, estão contidas nas packages EpcXX_Dados, nos métodos setDadosItem correspondentes aos registros, e também na package EpcAP_Dados que realiza a apuração convertendo os formatos EPCXX para EPCAP;
O sistema tem por padrão verificar inicialmente a parametrização por serviço, e caso nada seja encontrado, verificar a parametrização por CFOP.

Obs.: Atentar para a forma como estas parametrizações são obtidas, o comentário contido na package nos ajuda a entedê-la. Este comentário está contido na procedure setParaCFOPTipoOperacao.

-- Carrega um vetor com os parâmetros por CFOP e Natureza para o COD_PARAM = 475
-- O vetor é indexado pelo próprio código do CFOP, sendo guardadas as naturezas caso for necessário, exemplo:
-- parâmetros por CFOP:
--    paramCFOPTipoOperacao(5303) = |3| (onde 3 é o conteúdo do campo IND_DESTINACAO)
--    paramCFOPTipoOperacao(5307) = |1| (onde 1 é o conteúdo do campo IND_DESTINACAO)
-- parâmetros por CFOP/Natureza:
--    paramCFOPTipoOperacao(5303) = |002,VCF,3|002,VFD,1|
--    paramCFOPTipoOperacao(5307) = |002,VCF,1|002,VFD,3|
--
--    No exmplo acima a sequência |002,VCF,1| representa:
--    - 002 = GRUPO_NATUREZA_OP
--    - VCF = COD_NATUREZA_OP
--    - 1   = IND_DESTINACAO

Registros C500
Localização
Módulo: SPED – EFD-PIS/PASEP-COFINS
Menu: Parâmetros ( Registros C500 ( Por CFOP e Por Extensão CFOP

Definição:
O objetivo deste item será identificar as notas com modelo 55 que devam ser geradas nos registros C500. Normalmente os modelos 55 são gerados nos registros C100, porém ao selecionar um CFOP nesta opção, este deixará de ser gerado nos demais registros para compor o C500.

Dicas
A função que retorna os valores das operações através deste parâmetro está contida na package Epc_Parametros, no método getParamCFOPRegistroC500;
A chamada deste método é feita na package EpcDF_RegraDicionario, na função valTipoApuracao_C100_C170.

Obs.: Atentar para a forma como estas parametrizações são obtidas, o comentário contido na package nos ajuda a entedê-la. Este comentário está contido na procedure setParaCFOPTipoOperacao:

-- Carrega um vetor com os parâmetros por CFOP e Natureza para o COD_PARAM = 475
-- O vetor é indexado pelo próprio código do CFOP, sendo guardadas as naturezas caso for necessário, exemplo:
-- parâmetros por CFOP:
--    paramCFOPTipoOperacao(5303) = |3| (onde 3 é o conteúdo do campo IND_DESTINACAO)
--    paramCFOPTipoOperacao(5307) = |1| (onde 1 é o conteúdo do campo IND_DESTINACAO)
-- parâmetros por CFOP/Natureza:
--    paramCFOPTipoOperacao(5303) = |002,VCF,3|002,VFD,1|
--    paramCFOPTipoOperacao(5307) = |002,VCF,1|002,VFD,3|
--
--    No exmplo acima a sequência |002,VCF,1| representa:
--    - 002 = GRUPO_NATUREZA_OP
--    - VCF = COD_NATUREZA_OP
--    - 1   = IND_DESTINACAO

Registros F100
Localização
Módulo: SPED – EFD-PIS/PASEP-COFINS
Menu: Parâmetros ( Registros F100 ( Por Tipo de Docto. ou Por Conta Contábil e Centro de Custo

Definição:
Estas parametrizações servem para determinar o CST, alíquota e a natureza da base de crédito dos registros F100, e pode ser feita destas duas formas, ou seja, por tipo de documento ou conta e centro de custos. Na parametrização por tipo de documento podemos ter um único parâmetro por tipo de documento, para a conta contábil poderemos ter um registro para cada conta e centro de custo, não sendo obrigatório o centro de custos.

Dicas
Esta parametrização está sendo tratada na package EpcDD_Dados, nas funções getParamTipoDocto e getParamContaContabil.

Identificador da Natureza da Receita
Localização
Módulo: SPED – EFD-PIS/PASEP-COFINS
Menu: Parâmetros ( Apuração ( Identificador da Natureza da Receita

Definição:
Esta parametrização é utilizada na determinação dos códigos de natureza da receita informados nos registros M410 e M810, e possui uma série de possíveis combinações que podem ser utilizadas na determinação destes códigos, conforme segue:

Por Produto/NBM: Esta opção permite ao usuário criar regras a partir dos códigos de produto e/ou NBM, juntamente com as combinações de CST e alíquotas, as possibilidades são:
CST + Produto + NBM + Alíquotas (em percentual ou reais);
CST + Produto + Alíquotas (em percentual ou reais);
CST + NBM + Alíquotas (em percentual ou reais).
Por Serviço: Esta opção permite ao usuário criar regras a partir dos códigos de serviço, juntamente com as combinações de CST e alíquotas, as possibilidades são:
CST + Serviço + Alíquotas (em percentual ou reais).
Por CST/Alíquota: Esta opção permite ao usuário criar regras a partir dos CST’s, juntamente com as combinações CFOP e alíquotas, as possibilidades são:
CST + CFOP + Alíquotas (em percentual ou reais);
CST + Alíquotas (em percentual ou reais);
CST.

É importante notarmos que, ao utilizar-se desta parametrização para a definição dos códigos de natureza da receita, o sistema obedece expressamente à ordem na qual as combinações foram apresentadas, ou seja:
CST + Produto + NBM + Alíquotas (em percentual ou reais);
CST + Produto + Alíquotas (em percentual ou reais);
CST + NBM + Alíquotas (em percentual ou reais);
CST + Serviço + Alíquotas (em percentual ou reais).
CST + CFOP + Alíquotas (em percentual ou reais);
CST + Alíquotas (em percentual ou reais);
CST.

Cada grupo de combinações é testado, avaliando se o registro gerado enquadra-se em alguma destas combinações ou até que todas tenham sido avaliadas sem sucesso.

Dicas
Esta parametrização tem uma característica de distinguir alíquotas iguais a ZERO como valores válidos, já que existem situações onde a alíquota igual a zero representa uma operação válida para geração nos registros M410 e M810, portanto, há uma distinção entre a alíquota sem preenchimento (NULA) e preenchida com ZERO;
Como foi observado acima, o preenchimento das alíquotas é feito de forma exclusiva, ou seja, ao preencher a alíquota em percentual, a alíquota em reais não poderá ser preenchida e vice-versa. Além disto elas não são obrigatórias, e portanto, podem não ser preenchidas no caso da última combinação, onde apenas o CST será preenchido, ficando todas as alíquotas sem informação;
O preenchimento de uma das alíquotas, seja PIS ou COFINS, obriga que a outra equivalente também seja preenchida;
 O CFOP só tem uso na combinação expressa acima, não sendo válido para nenhuma das demais;
O NBM está definido como um range de valores, possuindo um valor inicial e um final;
O tratamento desta parametrização está contido no método setParamNaturezaReceita da package Epc_Parametros, onde seguimos uma ordem para a avaliação das possíveis combinações. A sua chamada é feita através dos métodos processarApuracaoRegistro da package EpcAP_Dados.

Identificador dos Tipos de Crédito
Localização
Módulo: SPED – EFD-PIS/PASEP-COFINS
Menu: Parâmetros ( Apuração ( Identificador dos Tipos de Crédito

Definição:
Os tipos de créditos são códigos definidos para identificar as origens de créditos apurados pelo PIS/COFINS e consolidados através dos registros M100 e seus filhos, para o PIS, e M500 e seus filhos, para a COFINS. Os tipos de crédito são determinados através de um conjunto de campos contidos nos registros e nas origens dos dados gerados no EFD, a saber:
CST;
Tipo de Alíquota (Em Percentual ou Em Reais);
Alíquota do PIS e da COFINS;
O Indicador da Origem do Crédito (Se no Mercado Interno ou Mercado Externo – Importação);
Código da Base de Crédito;
Tipo do Participante (Pessoa Jurídica ou Pessoa Física); e
CFOP.

Cada registro om crédito a ser gerado será avaliado com base nos colunas acima, identificando os códigos de crédito a partir de regras aplicáveis a cada campo, exemplo:

Coluna	Valor/Critério		Código do Tipo de Crédito	201		CST PIS/COFINS	51		Tipo de Alíquota PIS/COFINS	P		Operador da Alíquota PIS/COFINS		Alíquota do PIS	1,6500		Alíquota da COFINS	7,6000		Operador do Indicador de Origem do Crédito	DIFERENTE DE		Indicador de Origem do Crédito	1		Operador do Código da Base de Crédito	IGUAL A		Código da Base de Crédito	12		Operador do Participante		Participante		Operador do CFOP		CFOP		
Acima temos uma regra para classificação de registros no código de crédito 201, definida a partir das informações contidas nos vários registros do PIS/COFINS, o sistema avalia os registros enquadrando-os nas condições de cada regra, como esta, e identificando aqueles que atendam a todas as condições.

O primeiro critério será sempre o CST, e partir deste, cada valor será comparado. Nesta comparação algumas situações precisam ser esclarecidas:
Na regra, os itens que não possuam valor, permitem a classificação de qualquer informação, no exemplo acima, os itens participante e CFOP, aceitam quaisquer tipos de pessoa, física ou jurídica, e CFOP;
De acordo com o tipo de registro avaliado, certos campos podem ou não serem avaliados, conforme o conjunto de informações que este disponha em sua formação (vide dicas ao final);
Grande parte dos campos possui um “Operador” que define o critério de comparação, ou seja, se o valor deverá ser igual a ou diferente de etc.;
Dependendo do CST, um mesmo registro do EFD poderá ser classificado em um ou mais códigos de tipo de crédito, os CSTs que permitem a classificação em mais de um código são 53, 54, 55, 56, 63, 64, 65 e 66;
Quando um registro for classificado em mais de um código de crédito, isto significa dizer que o mesmo será lançado em mais de um registro M100 e M500, agrupados por código de crédito e alíquotas. Note-se que, na ocorrência desta classificação, haverá a aplicação de um percentual de rateio que irá particionar o valor do crédito nos códigos de crédito apurados, este percentual é calcula com base na proporção das operações tributadas e não tributadas no mercado interno e externo, informadas no registro 0111, e seu cálculo está contido nas regras de geração dos registros M100/M105 e M500/M505, para tal vide regras RNM100-08/RNM105-07 e RNM500-08/RNM505-07;
A parametrização das regras é prevista pelas regras do PVA e está prevista no Mastersaf através da TACES71, e estão disponíveis para alteração através desta opção. A alteração será permitida apenas clicando no botão “Personalizar Parametrização” na tela, e a qualquer momento o usuário poderá retornar ao padrão clicando no mesmo botão, que torna-se “Retornar Parametrização Padrão Mastersaf”;
Hoje o Mastersaf não possui tratamento que considere os NCM’s previstos na tabela 4.3.11 do EFD, o tratamento está feito através das alíquotas previstas para os NCM’s da lista.

Dicas
A permissão para alterações desta parametrização não foi algo bom para a solução nossa, ocorrem problemas em função desta parametrização ser muito complexa, e os clientes acabam inserindo alterações e deturpando os dados da apuração, o que causa erros de validação. Devemos ficar sempre atentos para alterações desta parametrização, quando forem encontrados problemas na validação dos dados da apuração;
O conjunto de regras está contido na tabela EPC_PARAM_TP_CRED;
A parametrização é de uso geral, portanto, o campo de empresa é preenchido com espaços. O campo IND_PARAM nos indica se a parametrização é “Padrão” ou “Personalizada”, e possui três possíveis valores: 0, 1 ou 2. O padrão desta parametrização será indicado por IND_PARAM = 0, quando é acionado o botão para personalização dos parâmetros, o sistema faz uma cópia dos parâmetros padrão, preenchendo nos dados copiados o código da empresa e o IND_PARAM = 1, caso o usuário venha a retornar para a parametrização padrão, os sistema altera os registros da empresa, modificando o IND_PARAM para 2. A partir das condições dos dados na tabela, é possível então para o sistema determinar se será utilizada a parametrização padrão ou personalizada, conforme exemplos:

Cenário 1 - Parametrização Padrão Inicial do Sistema

Empresa	IND_PARAM	Comentários		0	Linhas da parametrização padrão, todas as linhas da tabela estarão sem a Empresa informada e com IND_PARAM = 0.		
Cenário 2 - Parametrização Personalizada para a Empresa 001


Empresa	IND_PARAM	Comentários		0	Linhas da parametrização padrão.		001	1	Se existir ao menos uma linha para a Empresa da geração e IND_PARAM = 1, então significa que a parametrização foi personalizada, e que as linhas com IND_PARAM = 0 devem ser ignoradas.		
Cenário 3 - Parametrização Retornada para o Padrão

Empresa	IND_PARAM	Comentários		0	Linhas da parametrização padrão.		001	2	Se existir ao menos uma linha para a Empresa da geração e IND_PARAM = 2, então significa que a parametrização foi personalizada, mas que foi retornada a parametrização padrão. Nesta situação a parametrização válida será a padrão, com IND_PARAM = 0, e as linhas com IND_PARAM = 2 ignoradas.		
Cenário 4 - Parametrização Padrão para Empresa 001 e Personalizada para a Empresa 002

Empresa	IND_PARAM	Comentários		0	Linhas da parametrização padrão.		001	2	A empresa 001 possui linhas com IND_PARAM = 2, portanto, a parametrização válida para esta será a Padrão (IND_PARAM = 0).		002	1	A empresa 002 possui linhas com IND_PARAM = 1, portanto, a parametrização válida para esta será a Personalizada (IND_PARAM = 1).		
O tratamento das parametrizações de tipo de crédito encontra-se na package Epc_Parametros, através dos métodos:
setTipoCredApur: responsável por carregar as parametrizações no início da geração e armazená-las em um vetor;
setEstrutClassTpCred: esta procedure é chamada no processo de apuração (EpcAP_Dados) para setar os elementos do registro de origem (A170, C170, C181 etc.) para classificação;
getTipoCredApur: esta rotina efetua a classificação a partir das informações fornecidas e grava o resultado no vetor retTpCredApur (o resultado é dado em um vetor pelo fato da possibilidade de classificação em mais de um código.
Durante a classificação, é normal que um registro seja classificado em vários códigos de crédito, mesmo que seja um registro com CST que não permita tal situação, ocorre que existe um PESO que é calculado com base na quantidade de elementos que a regra possui e que são válidos para classificação. No método setTipoCredApur existe o tratamento que calcula o peso de cada regra e armazena este peso em um dos campos da estrutura de dados, no momento da classificação (getTipoCredApur) este peso é avaliado e a regra com maios peso é que a prevalecerá na classificação.


Identificador dos Tipos de Contribuição
Localização
Módulo: SPED – EFD-PIS/PASEP-COFINS
Menu: Parâmetros ( Apuração ( Identificador dos Tipos de Contribuição

Definição:
Os tipos de contribuição são códigos definidos para identificar as origens das contribuições apuradas pelo PIS/COFINS e consolidadas através dos registros M210, para o PIS, e M610, para a COFINS. Os tipos de contribuição são determinados através de um conjunto de campos contidos nos registros e nas origens dos dados gerados no EFD, a saber:
CST;
Tipo de Alíquota (Em Percentual ou Em Reais);
Alíquota do PIS e da COFINS;
O Indicador da Origem do Crédito (Se no Mercado Interno ou Mercado Externo – Importação);
Código da Base de Crédito;
Tipo do Participante (Pessoa Jurídica ou Pessoa Física); e
CFOP.

Cada registro om crédito a ser gerado será avaliado com base nos colunas acima, identificando os códigos de crédito a partir de regras aplicáveis a cada campo, exemplo: