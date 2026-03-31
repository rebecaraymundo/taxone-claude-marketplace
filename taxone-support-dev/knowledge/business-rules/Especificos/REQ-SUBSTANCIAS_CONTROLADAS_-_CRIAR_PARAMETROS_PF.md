# REQ-SUBSTANCIAS CONTROLADAS - CRIAR PARÂMETROS PF

> Fonte: REQ-SUBSTANCIAS CONTROLADAS - CRIAR PARÂMETROS PF.doc

SUBSTÂNCIAS CONTROLADAS

PARAMETRIZAÇÃO PARA GERAÇÃO DE PRODUTOS CONTROLADOS


Revisões

Data	OS/Chamado	Descrição	Autor		

Índice
 TOC \o "1-3" \h \z \u \t "Título 4;4;Título 5;5"  HYPERLINK \l "_Toc202264732" 1.	Introdução	 PAGEREF _Toc202264732 \h 3
 HYPERLINK \l "_Toc202264733" 1.1	Visão Geral / Objetivo	 PAGEREF _Toc202264733 \h 3
 HYPERLINK \l "_Toc202264734" 1.2	Documentos e Base Legal para a Solução	 PAGEREF _Toc202264734 \h 3
 HYPERLINK \l "_Toc202264735" 2.	Solução Funcional	 PAGEREF _Toc202264735 \h 3
 HYPERLINK \l "_Toc202264736" 2.1	Procedimentos para Fábrica	 PAGEREF _Toc202264736 \h 3
 HYPERLINK \l "_Toc202264737" 2.1.1	Interface com Usuário	 PAGEREF _Toc202264737 \h 3
 HYPERLINK \l "_Toc202264738" 2.1.1.1	Telas	 PAGEREF _Toc202264738 \h 3
 HYPERLINK \l "_Toc202264739" 2.1.1.1.1	Tela x	 PAGEREF _Toc202264739 \h 3
 HYPERLINK \l "_Toc202264740" ·ð	Criação	 PAGEREF _Toc202264740 \h 3
 HYPERLINK \l "_Toc202264741" ·ð	Alteração	 PAGEREF _Toc202264741 \h 3
 HYPERLINK \l "_Toc202264742" 2.1.1.1.2	Tela y	 PAGEREF _Toc202264742 \h 3
 HYPERLINK \l "_Toc202264743" ·ð	Criação	 PAGEREF _Toc202264743 \h 3
 HYPERLINK \l "_Toc202264744" ·ð	Alteração	 PAGEREF _Toc202264744 \h 3
 HYPERLINK \l "_Toc202264745" 2.1.1.2	Relatórios	 PAGEREF _Toc202264745 \h 3
 HYPERLINK \l "_Toc202264746" 2.1.1.2.1	Relatório W	 PAGEREF _Toc202264746 \h 3
 HYPERLINK \l "_Toc202264747" ·ð	Criação	 PAGEREF _Toc202264747 \h 3
 HYPERLINK \l "_Toc202264748" ·ð	Alteração	 PAGEREF _Toc202264748 \h 3
 HYPERLINK \l "_Toc202264749" 2.1.1.2.2	Relatório Z	 PAGEREF _Toc202264749 \h 3
 HYPERLINK \l "_Toc202264750" ·ð	Criação	 PAGEREF _Toc202264750 \h 3
 HYPERLINK \l "_Toc202264751" ·ð	Alteração	 PAGEREF _Toc202264751 \h 3
 HYPERLINK \l "_Toc202264752" 2.1.2	Procedimentos para Processamento.	 PAGEREF _Toc202264752 \h 3
 HYPERLINK \l "_Toc202264753" 2.2	Procedimentos para Interface	 PAGEREF _Toc202264753 \h 3
 HYPERLINK \l "_Toc202264754" 3.	Pontos de Atenção	 PAGEREF _Toc202264754 \h 3
 HYPERLINK \l "_Toc202264755" 3.1	Impactos em outros módulos	 PAGEREF _Toc202264755 \h 3
 HYPERLINK \l "_Toc202264756" 3.2	Implementação nas versões	 PAGEREF _Toc202264756 \h 3
 HYPERLINK \l "_Toc202264757" 4.	Informações para Conteúdo	 PAGEREF _Toc202264757 \h 3
 HYPERLINK \l "_Toc202264758" 4.1	Criação / Alteração – Tabelas SAFX  (Manual de Layout)	 PAGEREF _Toc202264758 \h 3
 HYPERLINK \l "_Toc202264759" 4.2	Criação / Alteração em telas e relatórios (manual operacional, roteiro e help)	 PAGEREF _Toc202264759 \h 3
 HYPERLINK \l "_Toc202264760" 4.3	Criação / Alteração de Tabelas (Fixas, Acessórias, Básicas)	 PAGEREF _Toc202264760 \h 3
 HYPERLINK \l "_Toc202264761" 4.4	Criação / Alteração de Roteiro Operacional	 PAGEREF _Toc202264761 \h 3
 HYPERLINK \l "_Toc202264762" 4.5	Outras informações que necessitarão ser atualizadas (help, manual operacional, etc)	 PAGEREF _Toc202264762 \h 3
 HYPERLINK \l "_Toc202264763" 5.	Testes	 PAGEREF _Toc202264763 \h 3
 HYPERLINK \l "_Toc202264764" 5.1	Cenário de Teste	 PAGEREF _Toc202264764 \h 3



 DOCPROPERTY  Title  \* MERGEFORMAT Título do Requisito
 DOCPROPERTY  Comments  \* MERGEFORMAT 
Introdução
O Cliente Bunge solicitou que o MasteSAF enquadrasse o módulo Substâncias Controladas na Portaria Nº 1.274 MJ, de 25/08/2003 (DO-U, DE 26/08/2003) definindo algumas regras para geração de produtos controlados entregues à Polícia Federal. O MasterSAF atualmente não possui esse tipo de regras parametrizáveis no sistema, por esse motivo foi emitido o INFOLEGIS_029_09_A visando a criação das mesmas.

Visão Geral / Objetivo
O objetivo deste documento é criar uma nova tela no módulo Substâncias Controladas que permitirá a parametrização de produtos que se enquadrem nas normas previstas em Lei, definidas por quantidade e país, definindo quais produtos deve ser gerados no Maio Magnético e Relatórios Auxiliares.

Documentos e Base Legal para a Solução
INFOLEGIS_029_09_A que tem por base legal a Portaria Nº 1.274 MJ, de 25/08/2003 (DO-U, DE 26/08/2003)
Solução Funcional
Criação da tela “Parâmetros Classificação de Produtos (Polícia Federal)” que ficará no menu: Cadastro

Procedimentos para Fábrica

Interface com Usuário
 Telas

 Classificação de Produtos (Polícia Federal)
Módulo: Substâncias Controladas
Menu: Cadastro => Parâmetros Classificação de Produtos (Polícia Federal)

Criação 
Deverá ser criada uma nova tela no menu Cadastro => Parâmetros Classificação de Produtos (Polícia Federal) no módulo Substâncias Controladas com o objetivo de permitir parametrizar critérios para a geração de produtos controlados para entrega à Receita Federal.


Alteração
Não se aplica.

Procedimentos para Processamento.
MTZ-SUBSTANCIAS CONTROLADAS - CRIAR PARÂMETROS PF (RN0 a RN09).


Relatórios
Produtos por quantidade e país
Módulo: Substâncias Controladas
Menu: Cadastro => Parâmetros Classificação de Produtos (Polícia Federal)

Criação 

Deverá ser criado um relatório de conferência para os itens cadastrados como Parâmetros Classificação de Produtos.

Alteração 
Não se aplica.

Procedimentos para Processamento.
MTZ-SUBSTANCIAS CONTROLADAS - CRIAR PARÂMETROS PF (RN10).

Procedimentos para Interface
Não se aplica.

Pontos de Atenção

Impactos em outros módulos

Não se aplica.
Implementação nas versões

Essa OS deverá ser implementada a partir da Release 31.0

Informações para Conteúdo

Criação / Alteração – Tabelas SAFX  (Manual de Layout)
[Não se aplica.


Criação / Alteração em telas e relatórios (manual operacional, roteiro e help)

Módulo: Substâncias Controladas
Menu: Cadastro => Parâmetros Classificação de Produtos (Polícia Federal):
Nessa tela deverão ser cadastrados os parâmetros para atendimento à Portaria Nº 1.274 MJ, de 25/08/2003 (DO-U, DE 26/08/2003) conforme a lista (Deverá ser criado um link com as informações abaixo:)
LISTA I
1. ÁCIDO N-ACETILANTRANÍLICO (1)
2. ÁCIDO ANTRANÍLICO (1)
3. ÁCIDO FENILACÉTICO (1)
4. ÁCIDO LISÉRGICO
5. ANIDRIDO PROPIÔNICO
6. CLORETO DE ETILA
7. EFEDRINA (1)
8. ERGOMETRINA (1)
9. ERGOTAMINA (1)
10. ETAEFEDRINA (1)
11. 1-FENIL-2-PROPANONA
12. GAMA-BUTIROLACTONA (GBL)
13. ISOSAFROL
14. N-METILEFEDRINA (1)
15. 3,4-METILENODIOXIFENIL-2-PROPANONA
16. METILERGOMETRINA (1)
17. N-METILPSEUDOEFEDRINA (1)
18. ÓLEO DE SASSAFRÁS (2)
19. PIPERIDINA (1)
20. PIPERONAL
21. PSEUDOEFEDRINA (1)
22. SAFROL
ADENDO:
I – estão sujeitos a controle e fiscalização os produtos químicos acima relacionados, suas respectivas soluções e misturas, independentemente da concentração, a partir das quantidades a seguir especificadas:
a) acima de dez gramas por mês, quando se tratar dos seguintes produtos: ácido N-Acetilantranílico,
Ácido Antranílico, Efedrina, Ergometrina, Ergotamina, Metilergometrina e Pseudoefedrina; (O Cliente Aguarda essa implementação.)
b) em qualquer quantidade para os demais produtos químicos da lista; e (Atualmente o Módulo efetua tal geração)
c) quanto aos produtos químicos da lista sobrescritos com os números entre parênteses, abaixo reproduzidos, também se aplica o controle a:
(1) seus sais;
(2) óleos essenciais similares contendo safrol;
II – a fabricação, o comércio e uso do cloreto de etila somente são permitidos para fins de produção de plásticos e de outros produtos de interesse da indústria nacional, estando classificado no rol das substâncias psicotrópicas, de acordo com a legislação sanitária em vigor; e 
III – os produtos farmacêuticos e as formulações diluídas de fragrâncias estão isentas de controle, de acordo com art. 20 desta Portaria.


LISTA II
1. ACETONA
2. ÁCIDO CLORÍDRICO
3. ÁCIDO CLORÍDRICO (estado gasoso)
4. ÁCIDO CLOROSSULFÔNICO
5. ÁCIDO HIPOFOSFOROSO
6. ÁCIDO IODÍDRICO
7. ÁCIDO SULFÚRICO
8. ÁCIDO SULFÚRICO FUMEGANTE
9. AMINOPIRINA (1)
10. ANIDRIDO ACÉTICO
11. BENZOCAÍNA (1)
12. BICARBONATO DE POTÁSSIO
13. BUTILAMINA (1)
14. CAFEÍNA (1)
15. CARBONATO DE POTÁSSIO
16. CARBONATO DE SÓDIO
17. CIANETO DE BENZILA
18. CIANETO DE BROMOBENZILA
19. CLORETO DE ACETILA
20. CLORETO DE BENZILA
21. CLORETO DE METILENO
22. CLORETO DE TIONILA
23. CLOROFÓRMIO
24. DIACETATO DE ETILIDENO
25. DIETILAMINA (1)
26. 2,5-DIMETOXIFENETILAMINA (1)
27. DIPIRONA
28. ÉTER ETÍLICO
29. ETILAMINA (1)
30. FENACETINA
31. FENILETANOLAMINA (1)
32. FÓSFORO VERMELHO
33. FORMAMIDA
34. FORMIATO DE AMÔNIO
35. HIDRÓXIDO DE POTÁSSIO
36. HIDRÓXIDO DE SÓDIO
37. IODO (sublimado)
38. LIDOCAÍNA (1)
39. MAGNÉSIO (metálico)
40. MANITOL
41. METILAMINA (1)
42. METILETILCETONA
43. N-METILFORMAMIDA
44. NITROETANO
45. PENTACLORETO DE FÓSFORO
46. PERMANGANATO DE POTÁSSIO
47. PROCAÍNA (1)
48. TOLUENO
ADENDO:
I – estão sujeitos a controle e fiscalização os produtos químicos acima relacionados, quando puros ou considerados quimicamente puros ou, ainda, com grau técnico de pureza, a partir das seguintes quantidades:
a) acima de um quilograma ou um litro por mês, quando se tratar de produto sólido ou líquido, respectivamente, no caso do permanganato de potássio, anidrido acético, cloreto de acetila, diacetato de etilideno, metilamina, etilamina e butilamina; 
b) acima de dois quilogramas ou dois litros por mês, quando se tratar de produto sólido ou líquido, respectivamente, quanto aos demais produtos químicos relacionados na lista, exceto hidróxido de sódio; (O Cliente Aguarda essa implementação.)

c) acima de trezentos quilogramas por mês, para pessoa jurídica, e cinco quilogramas por mês, para pessoa física, no caso de hidróxido de sódio e carbonato de sódio sólidos; e (O Cliente Aguarda essa implementação.)
d) os sais dos produtos químicos da lista sobrescritos com o número (1), nas mesmas quantidades prescritas nas alíneas anteriores;
II – também estão sujeitas a controle e fiscalização, exceto quando se tratar de produtos que se enquadram no art. 20 desta Portaria as soluções específicas e misturas dos produtos químicos acima relacionados, associados ou não a outros produtos químicos controlados, nos seguintes casos:
1) para quantidades acima de cinco quilogramas ou cinco litros por mês, quando se tratar de produto sólido ou líquido respectivamente: 
a) ácidos orgânicos e inorgânicos com concentração individual superior a dez por cento;
b) hidróxidos, bicarbonatos e carbonatos com concentração individual superior a dez por cento;
c) solventes orgânicos com concentração individual superior a sessenta por cento; e
d) demais substâncias com concentração superior a vinte por cento; 
1) Para quantidades acima de um quilograma ou de um litro por mês:
a) permanganato de potássio com qualquer concentração;
III – com relação aos produtos comerciais a que se refere o art. 20 desta Portaria deverão ser atendidas as seguintes exigências específicas:
a) no caso das soluções à base de solventes orgânicos, fabricadas para uso como removedor de esmalte de unhas, o teor total de substâncias químicas controladas não deverá ultrapassar a sessenta por cento, conterão corantes e somente poderão ser comercializadas no varejo em embalagens de até quinhentos mililitros;
b) quanto às soluções de éter etílico, fabricadas para uso médico-hospitalar, o teor total de substâncias químicas controladas não deverá ultrapassar a sessenta por cento e somente poderá ser comercializada no varejo em embalagens de até quinhentos mililitros; e
c) qualquer que seja a categoria do produto, a isenção de controle não se aplica ao permanganato de potássio, suas soluções e misturas com outras substâncias químicas;
IV - no caso da soda cáustica (hidróxido de sódio) em escamas, comercializada em supermercados e em outras lojas do ramo, e da soda barrilha (carbonato de sódio), aplicar-se-á o disposto na alínea c do inciso I deste Adendo, quanto aos limites de isenção de controle para pessoas jurídicas e pessoas físicas;
V - com relação as soluções eletrolíticas de bateria, formuladas à base de ácido sulfúrico, o limite de isenção para pessoa jurídica é de duzentos litros por mês e para pessoa física é de cinco litros por mês; e
VI – a norma estabelecida no art. 19 desta Portaria aplica-se aos produtos químicos relacionados nos itens 1, 21, 23, 28, 42 e 48 da Lista II.


LISTA III
1. ACETALDEÍDO
2. ACETATO DE ETILA
3. ACETATO DE ISOAMILA
4. ACETATO DE ISOBUTILA
5. ACETATO DE ISOPROPILA
6. ACETATO DE n-BUTILA
7. ACETATO DE n-PROPILA
8. ACETATO DE sec-BUTILA
9. ACETONITRILA
10. ÁCIDO ACÉTICO
11. ÁCIDO BENZÓICO
12. ÁCIDO BROMÍDRICO
13. ÁCIDO FÓRMICO
14. ÁLCOOL n-BUTÍLICO
15. ÁLCOOL ISOBUTÍLICO
16. ÁLCOOL sec-BUTÍLICO
17. ÁLCOOL n-PROPÍLICO
18. ALILBENZENO
19. AMÔNIA
20. ANIDRIDO BENZÓICO
21. ANIDRIDO ISATÓICO
22. BENZALDEÍDO
23. BENZENO
24. BOROHIDRETO DE SÓDIO
25. BROMOBENZENO
26. 1,1-CARBONILDIIMIDAZOLE
27. CICLOEXANO
28. CICLOEXANONA
29. CLORETO DE BENZOÍLA
30. CLORETO MERCÚRICO
31. DIACETONA ÁLCOOL
32. 1,2-DICLOROETANO
33. DISSULFETO DE CARBONO
34. HIDRETO DE ALUMÍNIO E LÍTIO
35. HIDRÓXIDO DE AMÔNIO
36. HIDROXILAMINA (1)
37. LÍTIO (metálico)
38. METILISOBUTILCETONA
39. ORTO-TOLUIDINA
40. PIRIDINA (1)
41. PROPIOFENONA
42. SÓDIO (metálico)
43. TETRACLORETO DE CARBONO
44. TETRAHIDROFURAN
ADENDO:
I – estão sujeitos a controle e fiscalização os produtos químicos acima relacionados, quando puros ou considerados quimicamente puros ou ainda com grau técnico de pureza, a partir das seguintes quantidades:
a) acima de dois quilogramas ou dois litros por mês, quando se tratar de produto químico sólido ou líquido, respectivamente, no caso do acetato de etila, ácido acético, ácido fórmico, amônia, benzeno, cicloexanona, hidróxido de amônio e metilisobutilcetona; (O Cliente Aguarda essa implementação.)
b) acima de cinco quilogramas ou cinco litros por mês, quando se tratar de produto químico sólido ou líquido, respectivamente, no caso dos demais produtos químicos relacionados na lista; e (O Cliente Aguarda essa implementação.)
c) quanto aos produtos químicos da lista sobrescritos com o número 1 entre parênteses, abaixo reproduzido, também aplica-se o controle para as mesmas quantidades prescritas na alínea b:
(1) seus sais;
II – também estão sujeitas a controle e fiscalização, exceto quando se tratar de produtos que se enquadram no art. 20 desta Portaria as soluções específicas e misturas dos produtos químicos acima relacionados, associados ou não a outros produtos químicos controlados, nos seguintes casos, para quantidades acima de cinco quilogramas ou cinco litros, conforme o estado físico do produto envolvido:
a) ácidos orgânicos e inorgânicos com concentração individual superior a dez por cento;
b) hidróxido de amônio, com concentração individual superior a dez por cento;
c) solventes orgânicos com concentração individual superior a sessenta por cento; e
d) demais substâncias com concentração superior a vinte por cento;
III – com relação aos produtos comerciais a que se refere o art. 20 desta Portaria deverão ser atendidas as seguintes exigências específicas:
a) no caso das soluções à base de solventes orgânicos, fabricadas para uso como removedor de esmalte de unhas, o teor total de substâncias químicas controladas não deverá ultrapassar a sessenta por cento, conterão corantes e somente poderão ser comercializadas no varejo em embalagens de até quinhentos mililitros; e b) as soluções específicas de hidróxido de amônio não poderão ter concentração superior a dez por cento.
III – a norma estabelecida no art.19 desta Portaria, aplica-se aos produtos químicos relacionados nos itens 2, 3, 4, 5, 6, 7, 8, 14, 15, 16, 17, 23, 27, 28, 31, 32, 34, 38 e 43 da Lista III.


LISTA IV
1. AGUARRÁS MINERAL e qualquer outro produto similar, à base de mistura de hidrocarbonetos alifáticos
2. ÁCIDO BÓRICO
3. ÁLCOOL ETÍLICO
4. ÁLCOOL ISOPROPÍLICO
5. ÁLCOOL METÍLICO
6. ÁCIDO ORTO-FOSFÓRICO
7. BICARBONATO DE SÓDIO
8. CARBONATO DE CÁLCIO
9. CARVÃO ATIVADO
10. CIMENTO PORTLAND ou do tipo PORTLAND
11. CLORETO DE CÁLCIO (anidro)
12. CLORETO DE ALUMÍNIO
13. CLORETO DE AMÔNIO
14. CROMATO DE POTÁSSIO
15. DICROMATO DE POTÁSSIO
16. DICROMATO DE SÓDIO
17. ÉTER DE PETRÓLEO
18. n-HEPTANO
19. n-HEXANO
20. GASOLINA
21. HIDRÓXIDO DE CÁLCIO
22. HIPOCLORITO DE SÓDIO
23. ÓLEO DIESEL
24. PERÓXIDO DE HIDROGÊNIO
25. ÓXIDO DE CÁLCIO
26. QUEROSENE
27. SULFATO DE SÓDIO (anidro)
28. TETRACLOROETILENO
29. THINNER e outras preparações à base solventes ou diluentes orgânicos compostos, concebidas para remover tintas ou vernizes
30. TRICLOROETILENO
31. XILENOS (isômeros orto, meta, para e misturas).
32. URÉIA
ADENDO:
I – estão sujeitos a controle e fiscalização os produtos acima relacionados, quando se tratar de exportação para a Argentina, Bolívia, Chile, Colômbia, Equador, Paraguai, Peru, Uruguai e Venezuela, nos seguintes casos: 
a) cimento Portland ou do tipo Portland, para quantidades superiores a um mil e duzentos quilogramas por operação;
b) gasolina, óleo diesel e querosene, para quantidades superiores a oitocentos e trinta litros por operação;
c) aguarrás mineral, thinner e outros produtos correlatos ou similares, bem como uréia, par a quantidades superiores a duzentos quilogramas ou duzentos litros por operação, respectivamente de acordo com o estado físico do produto envolvido;
d) carbonato de cálcio, cloreto de cálcio (anidro), cromato de potássio, hidróxido de cálcio, óxido de cálcio, carvão ativado, álcool etílico e hipoclorito de sódio, para quantidades superiores a cinqüenta quilogramas ou cinqüenta litros por operação, respectivamente de acordo com o estado físico do produto envolvido; e (O Cliente Aguarda essa implementação.)
e) com relação aos demais produtos químicos, quando a quantidade envolvida na operação for superior a cinco quilogramas ou cinco litros, respectivamente no caso de se tratar de produto sólido ou líquido; (O Cliente Aguarda essa implementação.)
II – a norma estabelecida no art. 19 desta Portaria aplica-se aos produtos químicos relacionados nos itens 4, 5, 17, 18, 19, 20, 26, 28, 29, 30 e 31 da Lista IV

Segue abaixo exemplo de tela


Dados a serem informados:
Código de Classificação Produto: Nesse campo o usuário deverá selecionar o Código de Classificação do Produto a ser parametrizado.
Quantidade: Nesse campo o usuário deverá informar a quantidade mínima para geração do Produto que será entregue à Polícia Federal. (Conforme Portaria Nº 1.274 MJ, de 25/08/2003 (DO-U, DE 26/08/2003). O sistema só irá gerar o produto, caso o movimento da operação seja superior à quantidade digitada nesse campo.
País Destino: Nesse campo o usuário deverá parametrizar os Países que conforme Portaria Nº 1.274 MJ, de 25/08/2003 (DO-U, DE 26/08/2003) são passíveis de análise pela Polícia Federal a partir de determinada quantidade exportada. Caso os produtos não se enquadrem na lista definida em Lei, esse campo não deverá ser habilitado.
Obs. Caso o produto não se enquadre em determinada quantidade de movimentação ou exportação para determinado país, essa tela não deve ser abastecida.  Poderá ser selecionado mais de um país por produto, entretanto deverá ser efetuado um novo cadastro para o mesmo produto, visto que é possível selecionar um país de cada vez.

Obs 1: Como critério para geração, o sistema irá somar toda a movimentação do mês e verificar se atinge a quantidade mínima exigida.
Obs 2: Nos casos de exportação, o sistema irá consolidar as quantidades exportadas, mesmo que para países distintos, e dessa forma, efetuar ou não a geração.
Criação / Alteração de Tabelas (Fixas, Acessórias, Básicas)

Não se aplica.
Criação / Alteração de Roteiro Ope