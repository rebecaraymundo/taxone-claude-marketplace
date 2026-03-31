# Sped_Fiscal_Bloco G_Especial

- **Fonte:** Sped_Fiscal_Bloco G_Especial.docx
- **Modificado:** 2023-04-13
- **Tamanho:** 36 KB

---

                                             Sped Fiscal – Bloco G – Geração Especial do Bloco G

__Localização:__  Menu Sped, Módulo EFD\-Escrituração Fiscal Digital, item Geração 🡪 Meio Magnético __\(Especial\)__

__Data__

__OS / Chamado__

__Descrição __

__Responsável__

17/08/2011

OS3400\-A

Geração especial do Bloco G p/as Empresas atrasadas na entrega

Vânia Dias Mattos

21/10/2011

OS3400\-B

Alteração na geração especial do Bloco G para incluir os Bens já baixados em períodos anteriores, mas que tenham créditos calculados durante o período da “não entrega” do Bloco G  

\(foi incluída a regra diferenciada para a geração do G125, pois quando foi criada a “geração especial” só existia diferença em relação a geração do G126\)\. 

Vânia Dias Mattos

__A geração “especial” do Bloco G difere da normal em relação a geração dos registros G125 e G126\. Neste documento constam __

__apenas as diferenças que existirão nestes registros quando efetuada a geração especial \(a geração “especial” é feita através do__

__item de menu descrito acima\)\.__

__Esta geração serve apenas para a primeira entrega do Bloco G, e somente nos casos em que houver atraso na entrega,__

__quando a apropriação dos créditos do CIAP fica proibida de ser feita enquanto durar a inadimplência\.__

__O objetivo é lançar todas as parcelas calculadas no período da inadimplência do Bloco G como crédito extemporâneo, para __

__que a empresa possa se apropriar de todos os créditos referentes ao período da proibição de uma única vez, que será o __

__período da primeira entrega do Bloco G\.__

__   __

__\(consultar detalhes sobre a utilização deste tipo de geração no Help e no requisito das OS’s 3400\-A e OS3400\-B\)__

# Registro G125 – Outros  Créditos do CIAP

RNG125

A alteração na geração do G125 foi implementada na OS3400\-B:

*\(originalmente, a geração “especial” tinha diferença apenas na geração do G126\)*

Na geração “especial” o G125 será gerado da seguinte forma:

1. Serão gerados os dados do G125 da mesma forma que é feita para a geração normal;
2. Além dos Bens gerados de acordo com as regras da geração normal, serão gerados também os Bens que tenham sido baixados \(BAIXA TOTAL\) no período entre o mês da interrupção dos créditos \(parâmetro informado em tela\) e o mês anterior ao mês da geração\. O objetivo de levar para o arquivo também os Bens já baixados, é fazer com que as suas parcelas de créditos calculadas durante este intervalo de tempo, também possam ser lançadas como créditos extemporâneos no arquivo;

__Conclusão__: Na verdade, a diferença da geração normal para a geração especial do G125, é que na geração normal são gerados apenas os Bens que ainda se encontram ativos no período da geração, enquanto na geração especial, poderão existir também Bens já baixados \(BAIXA TOTAL\) em períodos anteriores ao período da geração do arquivo\.

Para exemplificar, vamos supor o seguinte cenário:

__     __

__    Bem __

__NOV/2010__

__ DEZ/2010__

__   __

__\(Mês  da__

__Interrupção\) __

__JAN/2011__

__FEV/2011__

__MAR/2011__

__ABR/2011__

__MAIO/2011__

__JUN/2011__

__JULHO/2011__

__\(Mês da__

__Geração\)__

B00 \*

48

\-\-\-

\-\-\-

\-\-\-

\-\-\-

\-\-\-

\-\-\-

\-\-\-

\-\-\-

__B01__

19

__20__

__21__

__22__

__23__

__24__

__25__

__26__

__27__

__B02__

\-\-\-

\-\-\-

\-\-\-

\-\-\-

__1__

__2__

__3__

__4__

__5__

B03 \*

45

46

47

48

\-\-\-

\-\-\-

\-\-\-

\-\-\-

\-\-\-

B04 \*

41

42

43

44

45

46

47

48

\-\-\-

__B05__

40

__41__

__42__

__43__

__44__

__45__

__46__

__47__

__48__

B06 \*

47

48

\-\-\-

\-\-\-

\-\-\-

\-\-\-

\-\-\-

\-\-\-

\-\-\-

__B07__

14

__15__

__16__

__17__

__18__

__19__

__20__

__21__

__22__

B08 \*

23

24

25

26

27

\-\-\-

\-\-\-

\-\-\-

\-\-\-

B09 \*

12

\-\-\-

\-\-\-

\-\-\-

\-\-\-

\-\-\-

\-\-\-

\-\-\-

\-\-\-

Com estes dados, ao gerar o arquivo para __JULHO/2011__, tendo interrompido a apropriação em __DEZ/2010__, o Bloco G “especial” será gerado da seguinte forma:

*\(os Bens que aparecem com asterisco são os Bens baixados, seja antes de atingir a última parcela \(48\), como os exemplos B08 E B09, ou uma baixa por término do período de apropriação, como os exemplos B00, B03, B04, B05 e B06\)\.   *

__Bem 01:__

G125– 1 registro “SI” com a parcela 27

G126– 7 registros com as parcelas 20, 21, 22, 23, 24, 25 e 26

__Bem 02__:

G125– 1 registro “SI” com a parcela 5

G126– 4 registros com as parcelas 1, 2, 3 e 4

__Bem 03:__

G125– 1 registro “SI”  \(ver OBS I\);

            1 registro “BA”,  para a baixa automática realizada em Fev/2011\(já que pelo exemplo, o mês de fevereiro é o

            último mês da apropriação, e portanto, será gerada a baixa automática\);

G126– 3 registros com as parcelas  46, 47 e 48

__Bem 04:__

G125– 1 registro “SI”  \(ver OBS I\);

            1 registro “BA”,  para a baixa automática realizada em Jun/2011\(já que pelo exemplo, o mês de junho é o

            último mês da apropriação, e portanto, será gerada a baixa automática\);

G126– 7 registros com as parcelas 42, 43, 44, 45, 46, 47 e 48;

__Bem 05__:

G125– 1 registro “SI” com a parcela 48;

            1 registro “BA” para a baixa automática realizada \(já que pelo exemplo, o mês de Julho é o último mês da

            apropriação, e portanto, será gerada a baixa automática\);

G126– 7 registros com as parcelas 41, 42, 43, 44, 46 e 47

__Bem 06:__

G125– 1 registro “SI”  \(ver OBS I\);

            1 registro “BA”,  para a baixa automática realizada em Dez/2011\(já que pelo exemplo, o mês de dezembro é o

            último mês da apropriação, e portanto, será gerada a baixa automática\);

G126– 1 registro com a parcela  48;

__Bem 07__:

G125– 1 registro “SI” com a parcela 22

G126– 7 registros com as parcelas 15, 16, 17, 18, 19, 20 e 21

__Bem 08:__

G125– 1 registro “SI”  \(ver OBS I\);

            1 registro “AT”, “PE” ou “OT” \(dependendo do tipo da baixa\) para a baixa realizada em Março/2011\(já que pelo

            exemplo é o mês em que o Bem foi baixado\);

G126– 3 __ou__ 4 registros, referentes às parcelas 24, 25, 26 __ou__ 24, 25, 26 e 27  \(ver OBS II\);

__OBS__: Observar que antes da OS3400\-B seriam gerados apenas os Bens 01, 02, 05 e 07, pois apenas estes se encontram ainda ativos no mês da geração \(Julho/2011\)\. Mas após o desenvolvimento da OS3400\-B, todos os Bens com créditos calculados durante o período da inadimplência serão gerados no arquivo\. Ou seja, com a alteração, passam a aparecer no arquivo os Bens 03, 04, 06 e 08\. Observar também que os Bens B00 e B09 não aparecem no Bloco G, pois têm baixa em períodos anteriores ao período da geração, no entanto, a baixa é fora do intervalo de tempo a ser considerado \(mês da interrupção <\-> mês da geração\)\. 

Observações sobre a geração do G125 dos Bens baixados em períodos anteriores:

O registro G125 “SI” dos Bens já baixados em períodos anteriores, deve ser gerado da seguinte forma:

- No campo DT\_MOV deve ser informada a data inicial do mês da geração \(conforme todos os registros “SI” são gerados\);
- Os valores de ICMS \(campos 05, 06, 07 e 08\) devem ser gerados normalmente, conforme a regra atual \(ou seja, são os valores originais do cadastro do CIAP menos as baixas *parciais* que possam existir para o Bem\);
-  Os campos do número da parcela e do valor passível de apropriação \(campos 09 e 10\) devam ser gerados sem informação;

O registro G125 referente à baixa, deve ser gerado normalmente, com a data real da baixa, seguindo as mesmas regras da geração normal para os registros G125 referentes às saídas\.

# Registro G126 – Outros  Créditos do CIAP

RNG126

Este registro é “filho” do G125, e nele serão gravadas todas as parcelas de crédito existentes para o Bem, no período referente ao seguinte intervalo de datas:

Data inicial do intervalo 🡪 último dia do mês/ano a partir do qual a apropriação foi interrompida \(\*\)

Data final do intervalo 🡪 último dia do mês anterior ao mês da “Data Inicial” informada em tela 

\(\*\) Parâmetro “*Interrupção dos créditos a partir de*” da tela da geração do arquivo\.

A idéia é lançar no G126 tudo que houver de crédito calculado durante este intervalo para o Bem gravado no G125 \(sejam parcelas normais, e também as parcelas extemporâneas\)\.

__Origem dos dados__: 

Tabelas dos cálculos do CIAP \(se Modelo = “C”🡪 APT\_DEM\_BASE\_CR e APT\_DEM\_CR\_MENSAL\)

                                                 \(se Modelo = “D”🡪 APT\_EST\_SAIDA e APT\_EST\_MENS\_ANO\)

Tabela do cálculo dos créditos extemporâneos \(APT\_CALC\_CRED\_EXT\)

__Critérios para recuperação dos dados a partir do Bem gravado no G125__:

__Nas tabelas dos cálculos “normais” do CIAP__:

Empresa                   = código da empresa informante

Estabelecimento       = código do Estabelecimento informante

Data de Apuração     = deve se enquadrar no intervalo de datas a ser tratado

                                      \(>= data inicial do intervalo e <= data final do intervalo\)

Identificador do CIAP = identificador do Bem gravado no G125 \(NUM\_CIAP\)

Indicador E/S             = E \(esta regra se aplica apenas ao Modelo C, ou seja, a APT\_DEM\_BASE\_CR\)

Valor da Parcela \(\*\)   <> 0 \(considerar apenas os registros onde existir valor de parcela calculado\) 

\(\*\) Se Modelo = C é o campo VLR\_CRED\_MENSAL da APT\_DEM\_BASE\_CR

      Se Modelo = D é o campo VLR\_TOT\_EST\_MENSAL da APT\_EST\_SAIDA

__Na tabela dos créditos extemporâneos__:

Empresa                    = código da empresa informante

Estabelecimento        = código do Estabelecimento informante

Data de Apuração      deve ser >= data inicial do intervalo e <= data da apuração __ \(\*\)__

Identificador do CIAP  = identificador do Bem gravado no G125 \(NUM\_CIAP\)

__*\(\*\)*__* Neste caso serão considerados também os créditos extemporâneos que possam ter sido calculados no período da geração, diferente da recuperação dos dados dos cálculos “normais”, que considera apenas as parcelas calculadas até o mês anterior ao mês da geração\. *

Cada linha recuperada de acordo com os critérios acima, representa uma parcela de crédito a ser gravada no G126\. 

Para a gravação dos campos, observar as regras específicas descritas a seguir, observando que as regras são diferentes, dependendo da origem dos dados \(se for uma parcela “comum”, ou se for uma parcela extemporânea\)\.

OBS: Quando o registro “pai” G125 for o resultado de uma consolidação de várias aquisições, as parcelas destas aquisições também serão consolidadas, conforme o conceito da geração do Bloco G \(ver regras da consolidação na RNG125 do documento de regras do Sped Fiscal\)\. 

  

RNG126\-02

Campo DT\_INI:

Se parcela “comum”   \(originada das tabelas do cálculo do CIAP\)

      Preencher com a data do primeiro dia do mês e ano do campo “Data de Apuração” das tabelas de

      cálculo do CIAP  __\(\*\*\*\)__

Se parcela “extemporânea”    \(originada da tabela dos créditos extemporâneos\)

      Campo “Data inicial” da tabela dos créditos extemporâneos \(é a data inicial do período a que se

      refere à parcela extemporânea\)\.

__\(\*\*\*\) __A regra correta para obter a data do primeiro dia do período seria verificar a periodicidade da apuração do ICMS, e dependendo se mensal, quinzenal ou decendial, calcular a data inicial\. No entanto, como se trata de uma geração muito específica, que será utilizada por alguns poucos clientes apenas para a primeira geração do Bloco G, não precisamos aplicar esta regra, considerando que a periodicidade da apuração do ICMS é mensal há mais de dez anos\.\.\. 

RNG126\-03

Campo DT\_FIN:	

Se parcela “comum”   \(originada das tabelas do cálculo do CIAP\)

      Campo “Data de Apuração” das tabelas de cálculo do CIAP 

Se parcela “extemporânea”    \(originada da tabela dos créditos extemporâneos\)

      Campo “Data final” da tabela dos créditos extemporâneos \(é a data final do período a que se refere

      à parcela extemporânea\)\.

RNG126\-04

Campo NUM\_PARC:

Se parcela “comum”   \(originada das tabelas do cálculo do CIAP\)

      Preencher com o número da parcela\. As tabelas do cálculo do CIAP não têm esta informação, 

      por isso, este valor deve ser calculado da forma padrão\. A regra geral para o cálculo do número

     da parcela esta descrita na RNG125\-09 do documento de regras do Sped Fiscal\.

Se parcela “extemporânea”    \(originada da tabela dos créditos extemporâneos\)

      Campo “Número da parcela” da tabela dos créditos extemporâneos

RNG126\-05

Campo VL\_PARC\_PASS:

Se parcela “comum”   \(originada das tabelas do cálculo do CIAP\)

       Campo “Valor da Parcela Passível de Apropriação” \(VLR\_PASS\_APROP\) das tabelas do cálculo 

Se parcela “extemporânea”    \(originada da tabela dos créditos extemporâneos\)

      Campo “Valor da Parcela Passível de Apropriação” \(VLR\_PARC\_APROP\) da tabela dos créditos

      extemporâneos

RNG126\-06

Campo VL\_TRIB\_OC:

Se parcela “comum”   \(originada das tabelas do cálculo do CIAP\)

       Campo “Valor das Saídas Tributadas” das tabelas do cálculo do período

Se parcela “extemporânea”    \(originada da tabela dos créditos extemporâneos\)

      Campo “Valor das Saídas Tributadas do Período” da tabela dos créditos extemporâneos

__Obs: __No caso da tabelas dos créditos extemporâneos, esta informação consta na própria tabela que contém as informações sobre a parcela calculada para cada Bem\. Já nas tabelas do cálculo “normal” do CIAP, esta informação *não* esta na tabela que contém as informações das parcelas calculadas \(APT\_DEM\_BASE\_CR e APT\_EST\_SAIDA\), e sim nas tabelas que contém os valores totais do período \(APT\_DEM\_CR\_MENSAL e APT\_EST\_MENS\_ANO\), nas quais existe apenas um registro por período\. Para recuperar as informações destas tabelas a partir das tabelas das parcelas, basta utilizar como critério COD\_EMPRESA \+ COD\_ESTAB \+ DAT\_APURACAO\.

RNG126\-07

Campo VL\_TOTAL:

Se parcela “comum”   \(originada das tabelas do cálculo do CIAP\)

       Campo “Valor Total das Saídas” das tabelas do cálculo do período

Se parcela “extemporânea”    \(originada da tabela dos créditos extemporâneos\)

      Campo “Valor Total das Saídas do Período” da tabela dos créditos extemporâneos

__Obs: __No caso da tabelas dos créditos extemporâneos, esta informação consta na própria tabela que contém as informações sobre a parcela calculada para cada Bem\. Já nas tabelas do cálculo “normal” do CIAP, esta informação *não* esta na tabela que contém as informações das parcelas calculadas \(APT\_DEM\_BASE\_CR e APT\_EST\_SAIDA\), e sim nas tabelas que contém os valores totais do período \(APT\_DEM\_CR\_MENSAL e APT\_EST\_MENS\_ANO\), nas quais existe apenas um registro por período\. Para recuperar as informações destas tabelas a partir das tabelas das parcelas, basta utilizar como critério COD\_EMPRESA \+ COD\_ESTAB \+ DAT\_APURACAO\.

RNG126\-08

Campo IND\_PER\_SAI:

Este valor representa o índice de participação das saídas tributadas/exportação sobre o valor total das saídas do período, e deve ser preenchido com o seguinte conteúdo: 

	

Se parcela “comum”   \(originada das tabelas do cálculo do CIAP\)

       Saídas Tributadas / Total das Saídas do período \(campo 06\-VL\_TRIB\_OC / campo 07\-VL\_TOTAL\)

Se parcela “extemporânea”    \(originada da tabela dos créditos extemporâneos\)

       Saídas Tributadas / Total das Saídas do período \(campo 06\-VL\_TRIB\_OC / campo 07\-VL\_TOTAL\)

Obs: Ao efetuar este cálculo, considerar 8 casas decimais\. 

RNG126\-09

VL\_PARC\_APROP:

Se parcela “comum”   \(originada das tabelas do cálculo do CIAP\)

      Valor da parcela calculada

      \(Se Modelo = C é o campo VLR\_CRED\_MENSAL da APT\_DEM\_BASE\_CR\)

      \(Se Modelo = D é o campo VLR\_TOT\_EST\_MENSAL da APT\_EST\_SAIDA\)

Se parcela “extemporânea”    \(originada da tabela dos créditos extemporâneos\)

      Campo “Valor da Parcela” da tabela dos créditos extemporâneos

