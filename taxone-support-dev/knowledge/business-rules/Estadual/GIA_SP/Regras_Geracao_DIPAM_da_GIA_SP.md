# Regras_Geracao_DIPAM_da_GIA_SP

- **Fonte:** Regras_Geracao_DIPAM_da_GIA_SP.docx
- **Modificado:** 2024-02-01
- **Tamanho:** 57 KB

---

\(no requisito citar que as regras da geração foram descritas a partir do funcionamento da DIPAM\-B no módulo GIA\-SP\) 

Na geração dos dados as informações da DIPAM B são gravadas na tabela __EST\_SP\_GIA\_REG30__

	

__Código DIPAM 11__

__\[MFS92120\] __Inclusão da regra para considerar somente notas de pessoa física

	

Compras *escrituradas* de mercadorias de produtores rurais por município de origem\.

\-NF’s com CFOP ou *CFOP*/Nat parametrizado

\-Trata I\.E\.U\.;

\-Data fiscal enquadrada no período informado em tela 

\-Classificação fiscal = 1 ou 3 

\- Somente notas em que a pessoa fis/jur seja de SP __\(\*\*\*\)__	

\-Não diferencia MOVTO\_E\_S \(deveria tratar *apenas* entradas\)

\-Usa parametrização de produtos *opcionalmente*, e quando utilizada, serão consideradas apenas as notas com itens na SAFX08, para que o produto seja validado;

\-*Não* usa o parâmetro 67 do Módulo ICMS \(trabalha só com a UF da pessoa fis/jur\) 

\-Somente notas com itens	

          AND A\.SITUACAO <> 'S' 

          AND NVL\(A\.IND\_TRANSF\_CRED, '0'\) = '0' 

          AND NVL\(A\.IND\_SITUACAO\_ESP, '0'\) NOT IN \('1', '2', '8'\)

\- Somente notas fiscais em que a Pessoa Física/Jurídica seja Pessoa Física, verificando se atende a uma das condições abaixo:

  a\) Se o campo CPF/CNPJ \(campo 6 da SAFX04\) tem 11 caracteres OU

  b\) Se o campo Classe de Pessoa Física Jurídica \(campo 26 da SAFX04\) igual a 01 \(Pessoa Física\) e o campo Produtor Rural \(campo 80 da SAFX04\) igual a “S”\.

\-Valor totalizado: valor contábil do item  

\(\*\*\*\) O município utilizado no agrupamento é o município da X04\.

__Código DIPAM 12__

Compras *não escrituradas* de mercadorias de produtores rurais por município de origem\.

Não geramos este código, mas podemos apurar seguindo os mesmos critérios do código 11, mas tratando apenas a Classificação fiscal = 7 \(apenas notas não escrituradas\);

*\(criar parametrização para este código, e recuperar apenas as notas com classif=7\)*

__Código DIPAM 13__

Recebimentos, por cooperativas, de mercadorias remetidas por produtores rurais deste Estado, desde que ocorra a efetiva transmissão da propriedade para a cooperativa\.

\-NF’s com CFOP ou CFOP/Nat parametrizado

\-Trata I\.E\.U\.;

\-Data fiscal enquadrada no período informado em tela 

\-Classificação fiscal = 1 ou 3 

\- Somente notas em que a pessoa fis/jur seja de SP __\(\*\*\*\)__	

\-Não diferencia MOVTO\_E\_S \(*deveria tratar apenas entradas*\)

\-Usa parametrização de produtos *opcionalmente*, e quando utilizada, serão consideradas apenas as notas com itens na SAFX08, para que o produto seja validado;

*Não* usa o parâmetro 67 do Módulo ICMS \(trabalha só com a UF da pessoa fis/jur\) 

\-Somente notas com itens

          AND A\.SITUACAO <> 'S' 

          AND NVL\(A\.IND\_TRANSF\_CRED, '0'\) = '0' 

          AND NVL\(A\.IND\_SITUACAO\_ESP, '0'\) NOT IN \('1', '2', '8'\)

\-Valor totalizado: valor contábil do item  

\(\*\*\*\) O município utilizado no agrupamento é o município da X04\.

Observações sobre a RN06 do documento “MTZ – GIA – SP \- Geração dos Registros”:

\- Segundo esta regra serão recuperadas apenas notas com MOVTO\_E\_S = “2”, mas conforme testes realizados a geração recupera todos os CFOP’s parametrizados\. Na verdade, este procedimento não faria sentido no caso do código 23;

\- Segundo esta regra serão recuperadas apenas as notas cuja pessoa fis/jur tenha o campo “Classe de Pessoa Fis/Jur” = “2\-Cooperativa” MOVTO\_E\_S = “2”\.  Mas conforme os testes realizados, esta regra *não* esta sendo aplicada\.

__Código DIPAM 22__

Ratear o Valor Adicionado por município de origem nas operações abaixo: 

a\) vendas efetuadas por revendedores ambulantes autônomos em outros municípios paulistas; 

b\) refeições preparadas fora do município do declarante, em operações autorizadas por Regime Especial; 

c\) operações realizadas por empresas devidamente autorizadas a declarar por meio de uma única Inscrição Estadual; 

d\) outros ajustes determinados pela Secretaria da Fazenda mediante instrução expressa e específica\. 

O contribuinte deve apurar o valor adicionado e depois rateá\-lo entre os municípios deste Estado, proporcionalmente às operações ali realizadas, indicando a parcela correspondente a cada município\.

__= = = = = __

\-NF’s com CFOP ou CFOP/Nat parametrizado

\-Trata I\.E\.U\.;

\-Data fiscal enquadrada no período informado em tela 

\-Classificação fiscal = 1 ou 3 

\- Somente notas em que a pessoa fis/jur seja de SP __\(\*\*\*\)__	

\- Entradas e Saídas

\-Usa parametrização de produtos *opcionalmente*, e quando utilizada, serão consideradas apenas as notas com itens na SAFX08, para que o produto seja validado;

\-*Não* usa o parâmetro 67 do Módulo ICMS \(trabalha só com a UF da pessoa fis/jur\) 

\-Notas com ou sem itens

          AND A\.SITUACAO <> 'S' 

          AND NVL\(A\.IND\_TRANSF\_CRED, '0'\) = '0' 

          AND NVL\(A\.IND\_SITUACAO\_ESP, '0'\) NOT IN \('1', '2', '8'\)

\-Valor totalizado: depende do parâmetro “Forma de Cálculo”, usado no código 22;

\(\*\*\*\) O município utilizado no agrupamento é o município da X04\.

Este código trabalha com o parâmetro “Forma de Cálculo”, da seguinte forma:

__= = = = = __

Segue explicação que consta no help da parametrização:

__Se parâmetro = Base de Cálculo ICMS Normal:__

    Neste caso, das colunas “Base de Cálculo”, “Isentas/Não Tributadas”, “Outras” e “Redução”

    do ICMS normal das Saídas menos \(\-\) “Base de Cálculo”, “Isentas/Não Tributadas”, “Outras”

    e “Redução” do ICMS Normal das Entradas\.

  
__Se parâmetro = Base de Cálculo ICMS Substituição Tributaria:__

   Neste caso, das colunas “Base de Cálculo” do ICMS\-ST das Saídas menos \(\-\) “Base de

  Cálculo” ICMS\-ST das Entradas\.

  
__Se parâmetro = Valor Total NF – Revendedor Autônomo:__

     Neste caso, o cálculo é Valor Total NF de Saída \(Campo 23 \- VLR\_TOT\_NOTA – SAFX07\) \*

     Percentual IVA – RPA\.

    

	

Pelos testes, verifica\-se:

= = = = =

__Se parâmetro = Base de Cálculo ICMS Normal:__

   Usa os campos referentes ao ICMS Próprio:

    \[ \(Base de Cálculo \+ Isentas/Não Tributadas \+ Outras \+ Redução\) das saídas \]

    \-

    \[ \(Base de Cálculo \+ Isentas/Não Tributadas \+ Outras \+ Redução\) das entradas \]

__Se parâmetro = Base de Cálculo ICMS Substituição Tributária:__

    Usa os campos referentes ao ICMS\-ST:

    \[ Base de Cálculo das Saídas \] \-  \[ Base de Cálculo das Entradas \]

*    \(não sei o porque, mas nesse caso só usa o valor da base, diferente do tratamento do ICMS*

*     próprio\)*

__Se parâmetro = Valor Total NF \- Revendedor Autônomo:__

     Neste caso, o cálculo é feito somente a partir das notas de saída:

     \[  Valor total das notas de saída \*  Percentual IVA\-RPA \]

     \(este percentual é informado na tela da geração\)

= = = = =

Trata os valores dependendo se a nota tem ou não itens 

= = = = =

  
Não faz sentido ter a opção “*Valor Total – Revend Autônomo*” para os CFOP’s de entrada \!

= = = = =

Na prática, o resultado final do código 22 será a mistura das duas formas de calcular, da seguinte forma:

     \(1\)\-Totaliza as saídas parametrizadas com “*Valor Total – Revend Autônomo*” e aplica o

          percentual IVA\-RPA ao total encontrado; 

     \(2\)\-Totaliza as entradas e as saídas parametrizadas com as opções “Base ICMS” ou “Base ST”

         e apura o resultado calculando Saídas – Entradas;

O resultado final será a soma desses dois valores apurados \(1 \+ 2\)\.

Sendo assim, subentende\-se que:

Os CFOP’s de saída parametrizados podem ter diferentes opções no campo “Forma de Cálculo”\.

Já os CFOP’s de entrada deveriam trabalhar somente com as opções de base de cálculo, pois não faz sentido ter a opção “*Valor Total – Revend Autônomo*”\.

= = = = =

Exemplo:

NF

E/S

Item

CFOP

Vlr Contábil

Base

Isent/Out/Red

4

Entrada

1

1111

400,00

300,00

20,00

5

Saída

1

5111

2000,00

1800,00

50,00

2

5112

1000,00

600,00

50,00

Resultado conforme a parametrização:

__CFOP__

__Forma de Cálculo__

__Teste 1 \- Resultado__:

\(1850\+ 650\) – 320\) = __2180,00__

1111

Base de Cálculo Normal

5111

Base de Cálculo Normal

5112

Base de Cálculo Normal

__CFOP__

__Forma de Cálculo__

__Teste 2 \- Resultado__:

\[ \(1850 – 320\) \] \+ \[ \(1000 \* 40%\) \]

=

\[ 1530 \] \+ \[ 400 \] = __1930,00__

1111

Base de Cálculo Normal

5111

Base de Cálculo Normal

5112

Valor Total – Rever\. Autônomo

__CFOP__

__Forma de Cálculo__

__Teste 3 \- Resultado__:

\[  \(2000 \+ 1000\)  \* 40%\) \]

=

\[ 3000 \*  40% \] = __1200,00__

5111

Valor Total – Ver\. Autônomo

5112

Valor Total – Rever\. Autônomo

__CFOP__

__Forma de Cálculo__

__Teste 4 \- Resultado__:

\[ \(0 – 320\) \] \+  \[ \(2000 \+ 1000\)  \* 40%\) \]

=

\[ \-320 \] \+  \[ 3000 \*  40% \] = __880,00__

1111

Base de Cálculo Normal

5111

Valor Total – Rever\. Autônomo

5112

Valor Total – Rever\. Autônomo

Obs: Acredito que o cenário do __teste 4__ não faça sentido, porque esta sendo utilizado o método do “Valor Total – Revend\.Autônomo” para todas as saídas, e mesmo assim existe um CFOP de entrada parametrizado \(o 1111\)\. Assim, o valor da entrada será subtraído do resultado apurado pelo método “Valor Total – Revend\.Autônomo”\. Mas, na prática,  este é o resultado obtido na geração, e a geração do Sped seguirá o mesmo resultado\. 

Tratamento dos municípios:

 A apuração dos valores descritos acima é feita por município, lembrando que a GIA\-SP não usa o parâmetro 67 na geração da DIPAM\-B\.

 

__Código DIPAM 23    \(Transporte\)__

Rateio dos serviços de transporte intermunicipal e interestadual\.

Valor total dos serviços por município paulista onde se tenha iniciado o serviço de transporte\.

A geração recupera todos os documentos dos CFOP’s parametrizados, independente da classificação do documento\. Assim, serão recuperados tanto as notas fiscais de classificação 1 por exemplo, como os CTRC’s que têm a classificação = 4\.

\-NF’s com CFOP ou CFOP/Nat parametrizado

\-Trata I\.E\.U\.;

\-Data fiscal enquadrada no período informado em tela 

\-Classificação fiscal = 1, 3, 4, 5 ou 6  

\- No caso das notas de classificação 1 ou 3 à serão consideradas apenas as notas em que a

   “*UF Origem*” da nota = “SP”;

\- No caso das notas de classificação 4, 5 ou 6 à serão consideradas apenas as notas em que a

  “*UF Origem*” da nota  = “SP” __ou__, quando esta não for informada,  a “UF de Coleta” dos itens

   de frete \(X51\) for = “SP”;   __\(\*\*\*\)__

\- Somente notas de saída

\-Usa parametrização de produtos *opcionalmente*, e quando utilizada, serão consideradas apenas as notas com itens na SAFX08, para que o produto seja validado;

\-*Não* usa o parâmetro 67 do Módulo ICMS \(trabalha só com a UF da pessoa fis/jur\) 

\-Notas com ou sem itens

          AND A\.SITUACAO <> 'S' 

          AND NVL\(A\.IND\_TRANSF\_CRED, '0'\) = '0' 

          AND NVL\(A\.IND\_SITUACAO\_ESP, '0'\) NOT IN \('1', '2', '8'\)

\-Valor totalizado: valor contábil do item ou valor total da nota \(qdo nota sem itens\);

= = = = =

__\(\*\*\*\)__ O município utilizado no agrupamento é o município de origem da NF __ou__ o município de coleta dos itens de frete \(X51\), quando se tratar de notas de frete \(classif 4/5/6\) em que o município origem da capa não esteja preenchido;

Quando não existir o município de origem na NF:

 

      \- Se município de origem da nota não estiver preenchido, será usado o município de coleta

        da SAFX51;

      \- Se existir na X51 mais de um item de frete, e eles tiverem municípios de coleta diferentes,

         será gravada a seguinte msg no log, e o documento *não* será considerado:

*         “Existem na base de dados itens de frete para o DF com mais de um município de coleta\. *

*         O documento não será considerado na DIPAM\-B”*

No caso dos documentos de frete \(nota com classificação 4, 5 ou 6\), o valor utilizado será sempre o valor da capa \(SAFX07\), mesmo quando o documento tiver itens de frete \(SAFX51\)\.

= = = = = 

Exemplo:

Nota fiscal: 7

Classificação: 4 \(CTRC\)

CFOP: 5106

Município origem: Buri

Valor da Nota: 1\.000,00

Itens da X51:   1\-Município coleta: Pederneiras, Valor = 800,00; 

                           2\-Município coleta: Pederneiras, Valor = 200,00;

Neste cenário seria usado o município de Buri\.

Se na capa o município de origem não estivesse preenchido, seria usado o município de Pederneiras;

VALOR ADICIONADO DA GIA 

Fichas da Nova GIA utilizadas para calcular o Valor Adicionado: 

• Lançamentos de CFOP\. 

• Informações para a DIPAM\-B\. FICHA “LANÇAMENTO DE CFOP”

 Os CFOP iniciados com 1, 2 e 3 referem\-se a Entradas e os iniciados com 5, 6 e 7 referem\-se a Saídas\. São computados só os CFOP que representem efetivamente uma circulação de mercadoria ou prestação de serviço\. Ficam excluídos do cálculo os CFOP relativos a simples faturamento, operações com Ativo Fixo ou material de uso e consumo, remessas com previsão de retorno \(armazenamento, demonstração, comodato, empréstimo, exposição, etc\)\. A relação dos CFOP que entram no cálculo do Valor Adicionado está disponível no Anexo I do Manual da DIPAM \(v\. Introdução\)\. Portanto, percebe\-se que é vital a classificação correta do CFOP\. Dos valores das operações e prestações lançados na ficha "Lançamentos de CFOP" da GIA, nas colunas “Base de Cálculo”, “Isentas/Não Tributadas” e “Outras”, é obtido o Valor 

Adicionado pela equação:

![](data:image/png;base64,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)

= = = = = 

__Código DIPAM 24    \(Comunicação\)__

Rateio dos serviços de comunicação\.

Valor adicionado de cada município paulista onde o serviço tenha sido prestado\.

Este código usa o parâmetro “__Considerar Município do Ponto de Consumo \(Utilities\)”__ da tela da geração\.

Informações da regra RN01 do documento “MTZ – GIA\-SP – DIPAM\-B” :

__Considerar Município do Ponto de Consumo \(Utilities\):__  este parâmetro determinará a origem para a geração dos serviços de comunicação na geração do registro tipo 30 Dipam\.  A origem dos dados deste registro irá contemplar tanto as notas fiscais normais oriundas das tabelas SAFX07 quanto àquelas oriundas dos documentos fiscais utilities representados através da tabela SAFX42, considerando a regra abaixo:

- __Parâmetro “Considerar Município do Ponto de Consumo \(Utilities\)” = “Desmarcado”:__ serão recuperadas as notas ficais a partir das tabelas SAFX07 e SAFX08, incluindo os registros oriundos dos mapas\-resumo gerados a partir das notas ficais utilities\. Nesta condição *não* serão lidas as tabelas SAFX42 e SAFX43;
- __Parâmetro “Considerar Município do Ponto de Consumo \(Utilities\)” = “Marcado”:__ nesta condição será feita a recuperação das notas fiscais oriundas das tabelas SAFX07 e SAFX08, *NÃO* sendo considerados os registros de mapas\-resumo gerados a partir da SAFX42 e SAFX43, em contrapartida iremos buscar na tabela SAFX42, totalizando os dados por Município de Consumo \(campo 76 da SAFX42\)\.

\-NF’s com CFOP ou CFOP/Nat parametrizado

\-Trata I\.E\.U\.;

\-Data fiscal enquadrada no período informado em tela 

\-Classificação fiscal = 1 ou 3

\- Somente notas de saída

\-Dependendo do parâmetro __“Considerar Município do Ponto de Consumo \(Utilities\)”, __ serão recuperadas as notas da X07/X08 e/ou X42/X43:

Se parâmetro desmarcado:

      Serão recuperadas apenas as notas ficais a partir das tabelas SAFX07 e SAFX08, *incluindo* os

      registros oriundos dos mapas\-resumo \(IND\_ORIGEM\_INFO = 1\),  gerados a partir das notas

      ficais de utilities\.

      \-Recupera SAFX07/08

      \-Somente notas em que a pessoa fis/jur seja de SP  

      \-Utiliza o município da SAFX04   

      \-Não lê X42/43

Se parâmetro marcado:

     Serão recuperadas tanto notas  da X07/X08, como da X42/X43, sendo que nesse caso __não__

     serão consideradas as notas da X07/X08 originadas do mapa resumo \(IND\_ORIGEM\_INFO =

      1\)\. 

      \-Recupera SAFX07/08 o que não for originado de mapa resumo;

      \-No caso das notas da X07/X08 serão consideradas apenas as notas em que a pessoa fis/jur

        tenha a uf = “SP”;

      \- No caso das notas da X07/X08 será usado o município  da SAFX04 no grupamento;

      \-Recupera SAFX42/43 \(somente notas com UF do ponto de consumo = “SP”\);

      \- No caso das notas da X42/X43 serão consideradas apenas as notas em que a UF do ponto

        de consumo seja = “SP”; 

      \- No caso das notas da X42/X43 será usado o  município do ponto de consumo no

        grupamento;

\-Usa parametrização de produtos *opcionalmente*, e quando utilizada, serão consideradas apenas as notas com itens \(tanto da X07/X08 como da X42/X43\), para que o produto seja validado;

\-*Não* usa o parâmetro 67 do Módulo ICMS; 

\-Notas com ou sem itens

          AND A\.SITUACAO <> 'S' 

          AND NVL\(A\.IND\_TRANSF\_CRED, '0'\) = '0' 

          AND NVL\(A\.IND\_SITUACAO\_ESP, '0'\) NOT IN \('1', '2', '8'\)

\-Valor totalizado: valor contábil do item ou valor total da nota \(qdo nota sem itens\);

__Código DIPAM 25    \(Energia Elétrica\)__

Rateio de energia elétrica,conforme as situações abaixo:

a\)Distribuição de energia elétrica \- informar o valor adicionado de cada município paulista onde a energia elétrica foi fornecida, inclusive o próprio município do declarante, se for o caso\. 

b\)Geração de energia elétrica \- o valor adicionado será atribuído para o município paulista onde esteja localizado o estabelecimento gerador \(usina\) que deu saída à energia elétrica\. 

Se o estabelecimento possuir Inscrição Estadual no próprio município onde se encontra, informará apenas um valor simbólico \(R$ 1,00\) a favor deste município, sem rateio para qualquer outro município, quando solicitado pelo programa da Nova GIA\. 

Por outro lado, se a empresa possuir Inscrição Estadual única para todos os seus estabelecimentos, informará o valor adicionado de cada município paulista onde a energia elétrica tenha sido gerada, inclusive o próprio município do declarante, se for o caso\. 

c\)Comercialização de energia elétrica \- informar um valor simbólico \(R$ 1,00\) para o município onde esteja inscrito o estabelecimento comercializador, quando solicitado pelo programa da Nova GIA, sem rateio para outros municípios\.

Conforme testes realizados, e de acordo com a alteração feita pelo chamado 7195\_2013, este código é gerado sempre com o valor fixo = 1\.

Como a geração da DIPAM\-B no Sped seguirá as regras que temos hoje na geração da GIA\-SP, o procedimento será o mesmo, exceto na questão do município, já que a geração da GIA\-SP *não esta obedecendo a regra definida*, pois esta lançando o valor 1 para o município da pessoa fis/jur das notas parametrizadas, ao invés de usar o município definido na regra do chamado 7195:

__RN03__

Alteração realizada pelo chamado __7195\_2013__ \(Maio/2013\):

Ao gerar a DIPAM B para o códDIP 2\.5, NÃO realizar o rateio por município\. Este código é gerado mediante parametrização dos CFOP’s que irão compor o valor pertinente a comercialização de Energia Elétrica\.

Deve\-se gerar somente uma linha do registro 30 \(DIPAM \- B\) com a informação do município correspondente ao município do estabelecimento responsável pela geração \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\) e o valor “simbólico” de R$1,00\. Esta alteração visa atender a exigência do validador, uma vez que a posição da SEFAZ de SP é de que comerciantes de Energia Elétrica não devem apresentar rateio algum\.

O valor deve ser alinhado a direita e completados com zeros à esquerda\.

CH7195\_2013

Na verdade, não é preciso ler nenhuma nota, basta lançar o valor 1,00 para o município do estabelecimento\. O problema é quando gravar o código 25, e quanto a isso o comportamento da GIA\-SP é o seguinte: a geração grava o código 25 sempre que existir algum CFOP parametrizado\. Caso contrário, o registro Tipo 30 do código 25 não é gravado\. Como neste momento utilizaremos o mesmo conceito da GIA\-SP, o funcionamento no SPED será o mesmo\.

*\(o correto mesmo seria ter uma outra condição para gravar o código 25, que fosse independente da parametrização por CFOP, já que não há necessidades de ler nenhuma nota\!\)*

= = = = = 

__Código DIPAM 26__

Rateio da produção agropecuária

Valor da produção agropecuária \(inclusive de hortifrutigranjeiros\) própria ou em propriedades arrendadas em estabelecimentos que não possuam Inscrições Estaduais \(IE\) inscritas, ou que, mesmo possuindo Inscrições Estaduais, haja regime especial dispensando a escrituração nestes estabelecimentos\. 

Só gera para as notas de entrada\.

Totaliza o valor contábil \(e não o somatório das bases do ICMS, como descreve a RN07 do documento de regras “MTZ – GIA\-SP  \- Geração dos Registros”\)\.

\-NF’s com CFOP ou *CFOP*/Nat parametrizado

\-Trata I\.E\.U\.;

\-Data fiscal enquadrada no período informado em tela 

\-Classificação fiscal = 1 ou 3 

\-Somente notas em que a pessoa fis/jur seja de SP __\(\*\*\*\)__	

\-A parametrização não diferencia MOVTO\_E\_S, mas trata apenas as entradas 

\-Usa parametrização de produtos *opcionalmente*, e quando utilizada, serão consideradas apenas as notas com itens na SAFX08, para que o produto seja validado;

\-*Não* usa o parâmetro 67 do Módulo ICMS \(trabalha só com a UF da pessoa fis/jur\) 

\-Somente notas com itens	

          AND A\.SITUACAO <> 'S' 

          AND NVL\(A\.IND\_TRANSF\_CRED, '0'\) = '0' 

          AND NVL\(A\.IND\_SITUACAO\_ESP, '0'\) NOT IN \('1', '2', '8'\)

\-Valor totalizado: valor contábil do item 

\(\*\*\*\) O município utilizado no agrupamento é o município da X04\.

__Código DIPAM 27__

Vendas presenciais com saídas/vendas efetuadas em estabelecimento diverso de onde ocorreu a transação/negociação inicial\.

O estabelecimento que promover saídas de mercadorias por estabelecimento diverso daquele no qual as transações comerciais são realizadas, excluídas as transações comerciais não presenciais, deve informar neste código o valor das operações informando os respectivos municípios onde as transações foram realizadas\. Válido apenas para casos em que ambos os estabelecimentos estejam localizados neste Estado\.

Só gera para as notas de saída\.

Totaliza o somatório das bases do ICMS\.

\-NF’s com *CFOP* ou *CFOP/Nat* parametrizado

\-Trata I\.E\.U\.;

\-Data fiscal enquadrada no período informado em tela 

\-Classificação fiscal = 1 ou 3 

\-Somente notas em que a pessoa fis/jur seja de SP __\(\*\*\*\)__	

\-A parametrização não diferencia MOVTO\_E\_S, mas trata apenas as saídas 

\-Usa parametrização de produtos *opcionalmente*, e quando utilizada, serão consideradas apenas as notas com itens na SAFX08, para que o produto seja validado;

\-*Não* usa o parâmetro 67 do Módulo ICMS \(trabalha só com a UF da pessoa fis/jur\) 

\-Somente notas com itens	

          AND A\.SITUACAO <> 'S' 

          AND A\.NORM\_DEV <> 2	

          AND NVL\(A\.IND\_TRANSF\_CRED, '0'\) = '0' 

          AND NVL\(A\.IND\_SITUACAO\_ESP, '0'\) NOT IN \('1', '2', '8'\)

\-Valor totalizado: valor da Base de Cálculo ICMS, Base ICMS Isenta ou Base ICMS Outras\.

\(\*\*\*\) O município utilizado no agrupamento é o município da X04\. 

__Código DIPAM 31__

Total de __saídas __de mercadorias e prestações de serviços __não escrituradas__:

a\) relativas a Autos de Infração e Imposição de Multa \- AIIM pagos ou inscritos na Dívida Ativa no período

b\) autodenunciadas;

c\) valor adicionado resultante da venda de ativo imobilizado ou de material de uso e consumo\.

d\) mercadorias que vierem a perecer, deteriorar\-se ou ser objeto de roubo, furto ou extravio durante o ano base

Conforme __RN13__ do documento “MTZ – GIA\-SP – Geracao dos Registros”:

\(feito na OS3407\)

Se parâmetro FORMA DE CÁLCULO selecionado for VALOR TOTAL DAS NOTAS FISCAIS \(Campo 23 \- VLR\_TOT\_NOTA,SAFX07\):

para este campo deverá ser gravado o resultado do cálculo VALOR TOTAL DAS NOTAS FISCAIS \(Campo 23 \- VLR\_TOT\_NOTA,SAFX07\) \* PERCENTUAL IVA – RPA \(RN10 \- definido pelo usuário\)

Regra para gravação do Registro 30 – Código DIPAM 3\.1:

NF saida e entrada

Classif __1, 2, 3__ \(apesar do título deste código 31 ser “não escrituradas, a geração da GIA\-SP não considera as notas parametrizadas com classificação “7”\)

Valor totalizado:

Classif 1 e 3 à valor contábil dos itens ou valor total da nota quando nota sem itens

Classif 2à valor total da nota 

Trabalha com o parâmetro “Forma de Cálculo”, da mesma forma que o código “22”, com a diferença que usa apenas as opções “Base de Cálculo – ICMS” e “Valor Total NF – Revendedor Autônomo”:

__Se parâmetro = Base de Cálculo ICMS Normal:__

   Usa os campos referentes ao ICMS Próprio:

    \[ \(Base de Cálculo \+ Isentas/Não Tributadas \+ Outras \+ Redução\) das saídas \]

    \-

    \[ \(Base de Cálculo \+ Isentas/Não Tributadas \+ Outras \+ Redução\) das entradas \]

__Se parâmetro = Valor Total NF \- Revendedor Autônomo:__

     Neste caso, o cálculo é feito somente a partir das notas de saída:

     \[  Valor total das notas de saída \*  Percentual IVA\-RPA \]

     \(este percentual é informado na tela da geração\)

= = = = =

  
Não faz sentido ter a opção “*Valor Total – Revend Autônomo*” para os CFOP’s de entrada \!

= = = = =

Na prática, o resultado final do código 31 será a mistura das duas formas de calcular, da seguinte forma:

     \(1\)\-Totaliza as saídas parametrizadas com “*Valor Total – Revend Autônomo*” e aplica o

          percentual IVA\-RPA ao total encontrado; 

     \(2\)\-Totaliza as entradas e as saídas parametrizadas com as opções “Base ICMS” ou “Base ST”

         e apura o resultado calculando Saídas – Entradas;

O resultado final será a soma desses dois valores apurados \(1 \+ 2\)\.

Sendo assim, subentende\-se que:

Os CFOP’s de saída parametrizados podem ter diferentes opções no campo “Forma de Cálculo”\.

\(cabe o mesmo exemplo descrito para o código 22\)

A apuração não é por município\!

O resultado final, é gravado num único registro 30 c/o município = zeros, assim como os outros códigos “3n”\.

Na tabela da manutenção aparece com o município em branco, mas na geração do arquivo  o campo do município é gravado com zeros \(‘00000’\)\.

Conforme o Manual da GIA\-SP \(arquivo “pre\-formatado\_ngia\_v0210\.pdf”\):

Município

Código de um Município Paulista

 Ver __Tabela 15 __para valores válidos\.

 Alinhar à direita com ZEROS à esquerda

 Não pode haver Município duplicado para o mesmo CódDIP

 Classificação ascendente

 __Se CódDIP = 3\.X, o Município deve ser = ZEROS__

__Código DIPAM 35__

Total das entradas de mercadorias ou prestação de serviços não escrituradas, ou outros ajustes:

a\) autodenunciadas

b\) relativas a AIIM pagos ou inscritos na Dívida Ativa no período;

Conforme __RN09__ do documento “MTZ – GIA\-SP – Geracao dos Registros”:

\(feito no CH90400\)

__\[ALTERADA – CH9368\_2018 \(MFS\-18062\)\]__

__\[Alterada – MFS28440\] – Inclusão da classificação igual a “1”__

__\[Alterada – MFS37408 \- CH9601/2020 \- Cliente Yamaha\] – Inclusão do MOVTO\_E\_S  igual a “1”__

 

→ Notas fiscais de entrada com MOVTO\_E\_S = 1, __3, 4 ou 5__;

→ Classificação 1 ou 7 ou 8 \(campo 12/safx07 = 1, 7, 8\)

→ CFOP parametrizados na tela Código de DIPAM\-B x CFOP’s – Reg\.30 ou Código de DIPAM\-B x CFOP’s/ Natureza de Operação – Reg\.30

__OU__

→ Notas fiscais de saída com MOVTO\_E\_S = __9__;

→ Classificação 1 \(campo 12/safx07 = 1\)

→ CFOP 5927

\-Notas com ou sem itens

\-Valor totalizado: Valor contábil do item ou valor total da nota, se nota sem itens

Totaliza todas as notas e grava num único registro 30 c/o município = zeros

\(assim como os outros códigos “3n”\)

Na tabela da manutenção aparece com o município em branco, mas na geração do arquivo  o campo do município é gravado com zeros \(‘00000’\)\.

Conforme o Manual da GIA\-SP \(arquivo “pre\-formatado\_ngia\_v0210\.pdf”\):

Município

Código de um Município Paulista

 Ver __Tabela 15 __para valores válidos\.

 Alinhar à direita com ZEROS à esquerda

 Não pode haver Município duplicado para o mesmo CódDIP

 Classificação ascendente

 __Se CódDIP = 3\.X, o Município deve ser = ZEROS__

__Código DIPAM 36__

Total das entradas de mercadorias não escrituradas de produtores não equiparados:

Valor das entradas de mercadorias ou aquisições de serviços não escrituradas, provenientes de produtores rurais deste Estado não equiparados a comerciantes ou a industriais\.

Conforme __RN09__ do documento “MTZ – GIA\-SP – Geracao dos Registros”:

\(feito no CH90400\)

\(as regras são as mesmas do código 35, *exceto* pelo MOVTO\_E\_S e pela regra da classe da pessoa fis/jur\)

→ Notas fiscais de entrada com MOVTO\_E\_S = __2__;

→ Classificação 7 ou 8 \(campo 12/safx07 = 7, 8\)

→ CFOP iniciado por 1

→ Pessoa fis/jur desta NF deve estar com o campo Classe da Pessoa Fis/Jur <> Cooperativa \(campo 26/safx04 <> 02\)

\-Notas com ou sem itens

\-Valor totalizado: Valor contábil do item ou valor total da nota, se nota sem itens

Totaliza todas as notas e grava num único registro 30 c/o município = zeros

\(assim como os outros códigos “3n”\)

Na tabela da manutenção aparece com o município em branco, mas na geração do arquivo  o campo do município é gravado com zeros \(‘00000’\)\.

Conforme o Manual da GIA\-SP \(arquivo “pre\-formatado\_ngia\_v0210\.pdf”\):

Município

Código de um Município Paulista

 Ver __Tabela 15 __para valores válidos\.

 Alinhar à direita com ZEROS à esquerda

 Não pode haver Município duplicado para o mesmo CódDIP

 Classificação ascendente

 __Se CódDIP = 3\.X, o Município deve ser = ZEROS__

\(orientação para a validação verificar se o PVA irá aceitar munic = 0\)

= = = = = =

