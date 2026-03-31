# Layout - Cascavel

- **Fonte:** Layout - Cascavel.docx
- **Modificado:** 2026-01-15
- **Tamanho:** 62 KB

---

  
[__Layout do Registro Tipo 10 – Identificação do Documento Fiscal__](https://pr.nfs-e.net/datacenter/help/registro10.txt)  


Início

Tamanho

Fim

Tipo

Descrição

1

2

2

I

Descrição do registro \(10\)\.

4

1

4

I

Tipo do serviço \(1 \- Serviço prestado; 2 \- Serviço tomado\)\.

6

2

7

I

Tipo do Documento \( 01 – CF \- Conhecimento de Frete; 02 – ECF \- Cupom Fiscal; 03 – ERR; 04 – Ingresso; 05 – Modelo 1 \(M1\); 06 – Modelo 2 \(M1\-\); 07 – NFS\-e \- Nota Eletrônica de Serviços; 09 – OS \- Ordem de Serviço; 10 – Outros Documentos; 11 – Outros Municípios; 14 – Relatório; 15 – Série A; 16 – Série B; 17 – Série E; 18 – Série F; 19 – Série F\-1; 20 – Série F\-2; 21 – Série F\-3; 22 – Série F\-4; 23 – Série F\-5; 24 – Série G; 25 – Série I; 26 – Série P; 27 – Série S; 28 – U \- Único; 30 – Modelo 21; 31 – NFS\-e Sequêncial Nota Control \)

9

15

23

I

Número do documento\.

25

7

31

A

Competência \(MM/AAAA\) Ex\.: 01/2006\.

33

1

33

A

Tipo da pessoa \(F \- Física; J \- Jurídica\)\.

35

14

48

I

CPF / CNPJ do prestador do serviço\.

50

1

50

A

Tipo da pessoa \(F \- Física; J \- Jurídica\)\.

52

14

65

I

CPF / CNPJ do tomador do serviço, \(Caso o Tomador for estrangeiro, declarar como pessoa física e não informado dados\)

67

10

76

D

Data de emissão do documento DD/MM/AAAA\.

78

18

95

R

Valor contábil do documento\.

97

1

97

A

Situação de utilização do documento \(E \- Emitido; C \- Cancelado; X \- Extraviado; N \- Não utilizado\)\.

99

100

198

A

Observações para o documento\.

200

1

200

A

Documento fiscal proveniente de optantes do Simples Nacional \(S \- Sim; N \- Não\)\.

  
  
[__Layout do Registro Tipo 20 – Identificação dos serviços relacionados ao Documentos Fiscal__](https://pr.nfs-e.net/datacenter/help/registro20.txt)  


Início

Tamanho

Fim

Tipo

Descrição

1

2

2

I

Descrição do registro \(20\)\.

4

1

4

I

Tipo do serviço \(1 \- Serviço prestado; 2 \- Serviço tomado\)\.

6

2

7

I

Tipo do Documento \( 01 – CF \- Conhecimento de Frete; 02 – ECF \- Cupom Fiscal; 03 – ERR; 04 – Ingresso; 05 – Modelo 1 \(M1\); 06 – Modelo 2 \(M1\-\); 07 – NFS\-e \- Nota Eletrônica de Serviços; 09 – OS \- Ordem de Serviço; 10 – Outros Documentos; 11 – Outros Municípios; 14 – Relatório; 15 – Série A; 16 – Série B; 17 – Série E; 18 – Série F; 19 – Série F\-1; 20 – Série F\-2; 21 – Série F\-3; 22 – Série F\-4; 23 – Série F\-5; 24 – Série G; 25 – Série I; 26 – Série P; 27 – Série S; 28 – U \- Único; 30 – Modelo 21; 31 – NFS\-e Sequêncial Nota Control \)

9

15

23

I

Número do documento\.

25

7

31

A

Competência \(MM/AAAA\) Ex\.: 01/2006\.

33

1

33

A

Tipo da pessoa \(F \- Física; J \- Jurídica\)\.

35

14

48

I

CPF / CNPJ do prestador do serviço\.

50

1

50

A

Tipo da pessoa \(F \- Física; J \- Jurídica\)\.

52

14

65

I

CPF / CNPJ do tomador do serviço, \(Caso o Tomador for estrangeiro, declarar como pessoa física e não informado dados\)

67

7

73

I

Código do ítem da lista de serviços da lei complementar 116\.

75

6

80

R

Alíquota referente ao ítem da lista de serviços\.

82

18

99

R

Valor tributável \(Base de cálculo da prestação de serviços\)\.

101

18

118

R

Dedução\.

120

18

137

R

Valor retido\.

139

7

145

I

Local da prestação do serviço\.

147

2

148

I

Código da situação tributária da declaração do serviço\.

150

1

150

A

Tributa o ISS para o município do prestador do serviço \(S \- Sim; N \- Não\)\.

152

10

161

I

Redução de ISS por obras \- CEI

  
  
[__Layout do Registro Tipo 30 – Identificação da pessoa relacionada ao Documento Fiscal \*__](https://pr.nfs-e.net/datacenter/help/registro30.txt)  


Início

Tamanho

Fim

Tipo

Descrição

1

2

2

I

Descrição do registro \(30\)\.

4

1

4

A

Tipo da pessoa \(F \- Física; J \- Jurídica\)\.

6

14

19

I

CPF / CNPJ da pessoa\.

21

40

60

A

Nome / Razão Social\.

62

40

101

A

Descrição do logradouro\.

103

6

108

A

Nro\. Residência / Estabelecimento\.

110

20

129

A

Complemento do endereço\.

131

20

150

A

Descrição do bairro\.

152

30

181

A

Nome da cidade\.

183

2

184

A

Estado \(Unidade da Federação\)\.

186

8

193

I

Código de endereçamento postal\.

195

12

206

A

Fone comercial \(99 9999\-9999\)\.

208

12

219

A

Fax \(99 9999\-9999\)\.

  
  
[__Layout do Registro Tipo 40 – Informações sobre o plano de contas da empresa__](https://pr.nfs-e.net/datacenter/help/registro40.txt)  


Início

Tamanho

Fim

Tipo

Descrição

1

2

2

I

Descrição do registro \(40\)\.

4

7

10

A

Competência \(MM/AAAA\) Ex\.: 01/2006\.

12

1

12

A

Tipo da pessoa \(F \- Física; J \- Jurídica\)\.

14

14

27

I

CPF / CNPJ do declarante\.

29

50

78

A

Identificação da conta contábil\.

80

100

179

A

Descrição da conta contábil\.

181

50

230

A

Identificação da conta contábil sintética relacionada à Conta\.

232

7

238

I

Código do ítem da lista de serviços da lei complementar 116 relacionado à conta\.

240

50

289

A

Identificação da conta COSIF relacionada à conta \(Caso esteja usando plano de contas COSIF, este campo deverá ser declarado vazio\)\.

291

18

308

R

Valor contábil relacionado à conta referente à prestação dos serviços na competência\.

__Legenda__

I

Inteiro

Completar com zeros à esquerda\.

R

Real

Completar com zeros à esquerda, utilizando o "\." \(ponto\) como separador de casa decimal\.  
__Exemplo1__: o valor contábil do documento fiscal é de 1\.258,67; deve ser gerado no arquivo como "000000000001258\.67"\.  
__Exemplo2__: a Alíquota é de 3,00%; deve ser gerado no arquivo como "003\.00"\.

A

Alfa\-numérico

Completar com espaços à direita\.

D

Data

Utilizar "/" \(barra\) como separador de data\. Máscara: 99/99/9999\.

  
  
__\*__ De acordo com o tipo do serviço sendo declarado:  
  \- Se for serviço prestado, deverá conter informações sobre o tomador do serviço;  
  \- Se for serviço tomado, deverá conter informações sobre o prestador do serviço\.  
  
__OBSERVAÇÕES__  
__\- Deverá__ ser inserido __";" \(ponto e vírgula\)__ como separados de campos\.  
__\- Deverá__ ser inserido __";" \(ponto e vírgula\)__ ao final de cada linha\.  
__\- O Registro do tipo 20 deverá ser agrupado pelo item da lista de serviços\.__

__Importação De Documentos Conjugados__

\- No Campo __Código do Item da Lista de Serviços__ preencher com __9999__;

\- No Campo __Dedução__ preencher com o __Valor dos Produtos para Deduzir do documento Conjugado \+ ICMS/ST__;

\- No Campo __Cidade__ preencher normalmente com a __Cidade da Prestação__;

\- No Campo __Situação Tributária__ Preencher com __99__;

\- Nos Campos __Alíquota, Valor Tributável, e Valor Retido__ preencher com o __Valor Zerado__;

__LEGENDA__:

__Sigla__

__Descrição__

Item LS

Ítem da Lista de Serviço

Trib\. Mun\. Prest\.

Tributa no Municipio do Prestador

Local PS

Local da Prestação do Serviço

Sit\. Trib\.

Situação Tributária

Vlr\.

Valor

Vlr\. ISSRF

Valor do ISS Retido na Fonte

__SITUAÇÕES TRIBUTÁRIAS__:

__Código__

__Sigla__

__Descrição__

0

TI

Tributada Integralmente

1

TIRF

Tributada Integralmente com imposto sobre serviços retido na fonte

2

TIST

Tributada Integralmente e sujeita à Substituição Tributária

3

TRBC

Tributada com redução da base de cálculo

4

TRBCRF

Tributada com redução da base de cálculo com imposto sobre serviços retido na fonte

5

TRBCST

Tributada com redução da base de cálculo e sujeita à Substituição Tributária

6

ISE

Isenta

7

IMU

Imune

8

NTIFx

Não Tributada \- ISS regime Fixo

9

NTIEs

Não Tributada \- ISS regime Estimativa

10

NTICc

Não Tributada \- ISS Construção Civil recolhido antecipadamente

11

NTINa

Não Tributada \- ISS recolhido por Nota Avulsa

12

NTPEM

Não Tributada \- Prestador estabelecido no Município

13

NTREP

Não Tributada \- Recolhimento efetuado pelo prestador de fora do Município

14

NTRIB

Não Tributada

15

NTAC

Não Tributada \- Ato Cooperado

99

PDFC

Produtos Documento Fiscal Conjugado

100

NãoInc

Não incidência de ISSQN

__LISTA DE SERVIÇOS DISPONÍVEIS __:

__Código__

__Alíquota__

__Permite Sub\. Tributária__

__Padrão Trib\. Prestador__

__Permite Alterar Trib\. Prestador__

__Descrição__

101

3\.00

SIM

SIM

SIM

Análise e desenvolvimento de sistemas

102

3\.00

SIM

SIM

SIM

Programação

103

3\.00

SIM

SIM

SIM

Processamento, armazenamento ou hospedagem dedados, textos, imagens, vídeos, páginas eletrônicas,aplicativos e sistemas de informação, entre outros formatos, e congêneres

104

3\.00

SIM

SIM

SIM

Elaboração de programas de computadores,inclusive de jogos eletrônicos, independentemente da arquitetura construtiva da máquina em que o programa será executado,incluindotablets,smartphonesecongêneres

105

3\.00

SIM

SIM

SIM

Licenciamento ou cessão de direito de uso de programas de computação

106

3\.00

SIM

SIM

SIM

Assessoria e consultoria em informática

107

3\.00

SIM

SIM

SIM

Suporte técnico em informática, inclusive instalação, configuração, e manutenção de programas de computação e bancos de dados

108

3\.00

SIM

SIM

SIM

Suporte técnico em informática, inclusive instalação, configuração, e manutenção de programas de computação e bancos de dados

109

3\.00

SIM

SIM

SIM

Disponibilização, sem cessão definitiva, de conteúdos de áudio, vídeo, imagem e texto por meio da internet, respeitada a imunidade de livros, jornais e periódicos \(exceto a distribuição de conteúdos pelas prestadoras de Serviço de A cess

201

3\.00

SIM

SIM

SIM

Serviços de pesquisa e desenvolvimento de qualquer natureza

302

5\.00

NÃO

SIM

SIM

Cessão de direito de uso de marcas e de sinais de propaganda

303

5\.00

SIM

SIM

SIM

Exploração de salões de festas, centro de convenções, escritórios virtuais, stands, quadras esportivas, estádios, ginásios, auditórios, casas de espetáculos, parques de diversões, canchas e congêneres, para realização de eventos o u neg

304

5\.00

SIM

SIM

SIM

Locação, sublocação, arrendamento, direito de passagemou permissão de uso, compartilhado ou não, de ferrovia, rodovia, postes, cabos, dutos e condutos de qualquer natureza

305

5\.00

SIM

SIM

SIM

Cessão de andaimes, palcos, coberturas e outras estruturas de uso temporário\.

401

3\.00

SIM

SIM

SIM

Medicina e biomedicina

402

3\.00

SIM

SIM

SIM

Análises clínicas, patologia, eletricidade médica, radioterapia, quimioterapia, ultra\-sonografia, ressonância magnética, radiologia, tomografia e congêneres

403

3\.00

SIM

SIM

SIM

Hospitais, clínicas, laboratórios, sanatórios, manicômios, casas de saúde, pronto\-socorros, ambulatórios e congeneres\.

404

3\.00

SIM

SIM

SIM

Instrumentação cirúrgica

405

3\.00

SIM

SIM

SIM

Acupuntura

406

3\.00

SIM

SIM

SIM

Enfermagem, inclusive serviços auxiliares

407

3\.00

SIM

SIM

SIM

Serviços farmacêuticos

408

3\.00

SIM

SIM

SIM

Terapia ocupacional, fisioterapia fonoaudiologia

409

3\.00

SIM

SIM

SIM

Terapias de qualquer espécie destinadas ao tratamento físico, orgânico e mental

410

3\.00

SIM

SIM

SIM

Nutrição

411

3\.00

SIM

SIM

SIM

Obstetrícia

412

3\.00

SIM

SIM

SIM

Odontologia

413

3\.00

SIM

SIM

SIM

Ortóptica

414

3\.00

SIM

SIM

SIM

Próteses sob encomenda

415

3\.00

SIM

SIM

SIM

Psicanálise

416

3\.00

SIM

SIM

SIM

Psicologia

417

3\.00

SIM

SIM

SIM

Casas de repouso e de recuperação, creches, asilos e congêneres

418

3\.00

SIM

SIM

SIM

Inseminação artificial, fertilização in vitro e congêneres

419

3\.00

SIM

SIM

SIM

Bancos de sangue, leite, pele, olhos, óvulos, sêmen e congêneres\.

420

3\.00

SIM

SIM

SIM

Coleta de sangue, leite, tecidos, sêmen, órgãos e materiais biológicos de qualquer espécie

421

3\.00

SIM

SIM

SIM

Unidade de atendimento, assistência ou tratamento móvel e congêneres

422

3\.00

SIM

SIM

SIM

Planos de medicina de grupo ou individual e convênios para prestação de assistência médica, hos\-pitalar, odontológica e congêneres\.

423

3\.00

SIM

SIM

SIM

Outros planos de saúde que se cumpram por meio de serviços de terceiros contratados, creden\- ciados, cooperados ou apenas pagos pelo operador do plano mediante indicação do beneficiário\.

501

3\.00

SIM

SIM

SIM

Medicina veterinária e zootecnia

502

3\.00

SIM

SIM

SIM

Hospitais, clínicas, ambulatórios,prontos\-socorros e congêneres, na área veterinária

503

3\.00

SIM

SIM

SIM

Laboratórios de análise na área veterinária

504

3\.00

SIM

SIM

SIM

Inseminação artificial, fertilização in vitro e congêneres

505

3\.00

SIM

SIM

SIM

Bancos de sangue e de órgãos e congêneres

506

3\.00

SIM

SIM

SIM

Coleta de sangue, leite, tecidos, sêmen, órgãos e materiais biológicos de qualquer espécie

507

5\.00

SIM

SIM

SIM

Unidade de atendimento, assistência o tratamento móvel e congêneres

508

5\.00

SIM

SIM

SIM

Guarda, tratamento, amestramento, embelezamento, alojamento e congêneres

509

5\.00

SIM

SIM

SIM

Planos de atendimento e assistência médico veterinária

601

3\.00

SIM

SIM

SIM

Barbearia, cabeleireiros, manicures, pedicures e congêneres

602

3\.00

SIM

SIM

SIM

Estéticas, tratamento de pele, depilação e congêneres

603

3\.00

SIM

SIM

SIM

Banhos, duchas, sauna, massagens e congêneres

604

3\.00

SIM

SIM

SIM

Ginástica, dança, esportes, natação, artes marciais e demais atividades físicas

605

3\.00

SIM

SIM

SIM

Centros de emagrecimento, spa e congêneres

606

3\.00

SIM

SIM

SIM

Aplicação de tatuagens,piercingse congêneres

701

3\.00

SIM

SIM

SIM

Engenharia, agronomia, agrimensura, arquitetura, geologia, urbanismo, paisagismo e congêneres

702

3\.00

SIM

SIM

SIM

Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, in\- clusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, paviment ação,

703

3\.00

SIM

SIM

SIM

Elaboração de planos diretores, estudos de viabilidade, estudos organizacionais e outros relacionados com obras e serviços de engenharia; elaboração de anteprojetos, projetos básicos e projetos executivos para trabalhos de engenharia

704

3\.00

SIM

SIM

SIM

Demolição

705

3\.00

SIM

SIM

SIM

Reparação, conservação e reforma de edifícios, estradas, pontes, portos e congêneres \(exceto o fornecimento de mercadorias produzidas pelo prestador dos serviços, fora do local da prestação dos serviços, que fica sujeito ao ICMS\)\.

706

3\.00

SIM

SIM

SIM

Colocação e instalação de tapetes, carpete,assoalhos, cortinas, revestimentos de parede vidros, divisórias, placas de gesso e congêneres, com material fornecido pelo tomador do serviço

707

3\.00

SIM

SIM

SIM

Recuperação, raspagem, polimento e lustração de pisos e congêneres

708

3\.00

SIM

SIM

SIM

Calafetação

709

3\.00

SIM

SIM

SIM

Varrição, coleta, remoção, incineração, tratamento, reciclagem, separação e destinação final de lixo, rejeitos e outros resíduos quaisquer\.

710

3\.00

SIM

SIM

SIM

Limpeza, manutenção e conservação de vias e logradouros públicos, imóveis, chaminés, piscinas, parques, jardins e congêneres\.

711

3\.00

SIM

SIM

SIM

Decoração e jardinagem, inclusive corte e poda de árvores\.

712

3\.00

SIM

SIM

SIM

Controle e tratamento de efluentes de qualquer natureza e de agentes físicos, químicos e biológicos\.

713

3\.00

SIM

SIM

SIM

Dedetização, desinfecção, desinsetização, imunização, higienização, desratização, pulverização e congêneres

716

3\.00

SIM

SIM

SIM

Florestamento, reflorestamento, semeadura, a dubação, reparação de solo, plantio, silagem,colheita, corte e descascamento de árvores, silvicultura, exploração florestal e dos serviços congêneres in\- dissociáveis da formação, manutenção e colheita de flo

717

3\.00

SIM

SIM

SIM

Escoramento, contenção de encostas e serviços congêneres\.

718

3\.00

SIM

SIM

SIM

Limpeza e dragagem de rios, portos, canais, baías, lagos, lagoas, represas, açudes e congêneres\.

719

3\.00

SIM

SIM

SIM

Acompanhamento e fiscalização da execução de obras de engenharia, arquitetura e urbanismo

720

3\.00

SIM

SIM

SIM

Aerofotogrametria \(inclusive interpretação\), cartografia, mapeamento, levantamentos topográficos, batimétricos, geográficos, geodésicos, geofísicos e congênere

721

3\.00

SIM

SIM

SIM

Pesquisa, perfuração, cimentação, mergulho, perfilagem, concretação, testemunhagem, pescaria, estimulação e outros serviços relacionados com a exploração e exploração de petróleo, gás natural e de outros recursos minerais

722

3\.00

SIM

SIM

SIM

Nucleação e bombardeamento de nuvens e congêneres\.

801

3\.00

SIM

SIM

SIM

Ensino regular pré\-escolar, fundamental, médio e superior

802

3\.00

SIM

SIM

SIM

Instrução, treinamento, orientação pedagógica e educacional, avaliação de conhecimentos de qualquer natureza

901

5\.00

SIM

SIM

SIM

Hospedagem de qualquer natureza em hotéis, apart\-service condominiais, flat, apart\-hotéis, hotéis residência, residence\-service, suíte service, hotelaria marítima, motéis, pensões e congêneres; ocupação por temporada com fornecimento de serviço \(o

902

5\.00

SIM

SIM

SIM

Agenciamento, organização, promoção, intermediação e execução de programas de turismo,passeios, viagens, excursões, hospedagens e congêneres

903

5\.00

SIM

SIM

SIM

Guias de turismo

1001

3\.00

SIM

SIM

SIM

Agenciamento, corretagem ou intermediação de câmbio, de seguros, de cartões de crédito, de planos de saúde e de planos de previdência privada

1002

5\.00

SIM

SIM

SIM

Agenciamento, corretagem ou intermediação de títulos em geral, valores mobiliários e contratos quaisquer

1003

5\.00

SIM

SIM

SIM

Agenciamento, corretagem ou intermediação de direitos de propriedade industrial, artística ou literária

1004

5\.00

SIM

SIM

SIM

Agenciamento, corretagem ou intermediação de contratos de arrendamento mercantil \(leasing\), de franquia \(franchising\) e de faturização \(factoring\)

1005

3\.00

SIM

SIM

SIM

Agenciamento, corretagem ou intermediação de bens móveis ou imóveis, não abrangidos em outros itens ou subitens, inclusive aqueles realizados no âmbito de Bolsas de Mercadorias e Futuros, por quaisquer meios

1006

3\.00

SIM

SIM

SIM

Agenciamento marítimo

1007

3\.00

SIM

SIM

SIM

Agenciamento de notícias

1008

3\.00

SIM

SIM

SIM

Agenciamento de publicidade e propaganda, inclusive o agenciamento de veiculação por quaisquer meios

1009

2\.50

SIM

SIM

SIM

Representação de qualquer natureza,inclusive comercial

1010

2\.50

SIM

SIM

SIM

Distribuição de bens de terceiros

1101

5\.00

SIM

SIM

SIM

Guarda e estacionamento de veículos terrestres automotores, de aeronaves e de embarcações\.

1102

5\.00

SIM

SIM

SIM

Vigilância, segurança ou monitoramento de bens, pessoas e semoventes\.

1103

5\.00

SIM

SIM

SIM

Escolta, inclusive de veículos e cargas

1104

5\.00

SIM

SIM

SIM

Armazenamento, depósito, carga, descarga, arrumação e guarda de bens de qualquer espécie\.

1201

5\.00

SIM

SIM

SIM

Espetáculos teatrais

1202

5\.00

SIM

SIM

SIM

Exibições cinematográficas\.

1203

5\.00

SIM

SIM

SIM

Espetáculos circenses\.

1204

5\.00

SIM

SIM

SIM

Programas de auditório

1205

5\.00

SIM

SIM

SIM

Parques de diversões, centros de lazer e congêneres\.

1206

5\.00

SIM

SIM

SIM

Boates,taxi\-dancinge congêneres

1207

5\.00

SIM

SIM

SIM

Shows,balé, danças, desfiles, bailes, óperas, concertos, recitais, festivais e congêneres\.

1208

5\.00

SIM

SIM

SIM

Feiras, exposições, congressos e congêneres

1209

5\.00

SIM

SIM

SIM

Bilhares, boliches e diversões eletrônicas ou não\.

1210

5\.00

SIM

SIM

SIM

Corridas e competições de animais\.

1211

5\.00

SIM

SIM

SIM

Competições esportivas ou de destreza física ou intelectual, com ou sem a participação do espectador

1212

5\.00

SIM

SIM

SIM

Execução de música

1213

5\.00

SIM

SIM

SIM

Produção, mediante ou sem encomenda prévia, de eventos, espetáculos, entrevistas, shows, balé, danças, desfiles, bailes,teatros, óperas, concertos, recitais, festivais e congêneres\.

1214

5\.00

SIM

SIM

SIM

Fornecimento de música para ambientes fechados ou não, mediante transmissão por qualquer processo\.

1215

5\.00

SIM

SIM

SIM

Desfiles de blocos carnavalescos ou folclóricos, trios elétricos e congêneres\.

1216

5\.00

SIM

SIM

SIM

Exibição de filmes, entrevistas, musicais, espetáculos, concertos, desfiles, óperas, competições esportivas, de destreza intelectual ou congêneres\.

1217

5\.00

SIM

SIM

SIM

Recreação e animação, inclusive em festas e eventos de qualquer natureza\.

1302

3\.00

SIM

SIM

SIM

Fonografia ou gravação de sons, inclusive trucagem, dublagem, mixagem e congêneres

1303

3\.00

SIM

SIM

SIM

Fotografia e cinematografia, inclusive revelação, ampliação, cópia, reprodução, trucagem e congêneres

1304

3\.00

SIM

SIM

SIM

Reprografia, microfilmagem e digitalização

1305

3\.00

SIM

SIM

SIM

Composição gráfica, inclusive confecção de impressos gráficos, fotocomposição, clicheria, zincografia, litografia e fotolitografia, exceto se destinados a posterior operação de comercialização ou industrialização, ainda que incorporados, de

1401

3\.00

SIM

SIM

SIM

Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto \(exceto peças e partes empregadas, qu

1402

3\.00

SIM

SIM

SIM

Assistência técnica

1403

3\.00

SIM

SIM

SIM

Recondicionamento de motores \(exceto peças e partes empregadas, que ficam sujeitas ao ICMS\)

1404

3\.00

SIM

SIM

NÃO

Recauchutagem ou regeneração de pneus

1405

3\.00

SIM

SIM

SIM

Restauração, recondicionamento, acondicionamento, pintura, beneficiamento, lavagem, secagem, tingimento, galvanoplastia, anodização, corte, recorte, plastificação, costura, acabamento, polimento e congêneres de objetos quaisquer

1406

3\.00

SIM

SIM

SIM

Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido

1407

3\.00

SIM

SIM

SIM

Colocação de molduras e congêneres

1408

3\.00

SIM

SIM

SIM

Encadernação, gravação e douração de livros, revistas e congêneres

1409

3\.00

SIM

SIM

SIM

Alfaiataria e costura, quando o material for fornecido pelo usuário final, exceto aviamento

1410

3\.00

SIM

SIM

SIM

Tinturaria e lavanderia

1411

3\.00

SIM

SIM

SIM

Tapeçaria e reforma de estofados em geral

1412

3\.00

SIM

SIM

SIM

Funilaria e lanternagem

1413

3\.00

SIM

SIM

SIM

Carpintaria e serralheria

1414

3\.00

SIM

SIM

SIM

Guincho intramunicipal, guindaste e içamento\.

1501

5\.00

SIM

SIM

SIM

Administração de fundos quaisquer, de consórcio, de cartão de crédito ou débito e congêneres, de carteira de clientes, de cheques pré\-datados e congêneres\.

1502

5\.00

SIM

SIM

SIM

Aberturas de contas em geral, inclusive conta\-corrente, conta de investimento e aplicação e caderneta de poupança, no País e no exterior, bem como a manutenção das referidas contas ativas e inativas

1503

5\.00

SIM

SIM

SIM

Locação e manutenção de cofres particulares, de terminais eletrônicos, de terminais de atendimento e de bens e equipamentos em geral

1504

5\.00

SIM

SIM

SIM

Fornecimento ou emissão de atestados em geral, inclusive atestado de idoneidade atestado de capacidade financeira e congêneres

1505

5\.00

SIM

SIM

SIM

Cadastro, elaboração de ficha cadastral, renovação cadastral e congêneres, inclusão ou exclusão do Cadastro de Emitentes de Cheques e sem Fundos \- CCF ou em quaisquer outros bancos cadastrais

1506

5\.00

SIM

SIM

SIM

Emissão, reemissão e fornecimento de avisos, comprovantes e documentos em geral; abono de firmas; coleta e entrega de documentos, bens e valores; comunicação com outra agência ou com a administração central; licenciamento eletrônico de veí culos

1507

5\.00

SIM

SIM

SIM

Acesso, movimentação, atendimento e consulta a contas em geral, por qualquer meio ou processo, inclusive por telefone, fac\-símile, internet e telex, acesso a terminais de atendimento, inclusive vinte e quatro horas; acesso a outro banco e a re

1508

5\.00

SIM

SIM

SIM

Emissão, reemissão, alteração, cessão, substituição, cancelamento e registro de controle de crédito; estudo, análise, fiança, anuência e congêneres; serviços relativos a abertura de crédito, para quaisquer fins

1509

5\.00

SIM

SIM

SIM

Arrendamento mercantil \(leasing\) de quaisquer bens, inclusive cessão de direitos e obriga\- ções, substituição de garantia, alteração, cancela\-mento e registro de contrato e demais serviços rela\-cionados ao arrendamento mercantil \(leasing\)\.

1510

5\.00

SIM

SIM

SIM

Serviços relacionados a cobranças recebimentos ou pagamentos em geral, de títulos quaisquer, de contas ou carnês, de câmbio, de tributos e por conta de terceiros, inclusive os efetuados por meio eletrônico, automático ou po r má

1511

5\.00

SIM

SIM

SIM

Devolução de títulos, protesto de títulos, sustação de protesto, manutenção de títulos, reapresentação de títulos, e demais serviços a eles relacionados

1512

5\.00

SIM

SIM

SIM

Custódia em geral, inclusive de títulos e valores mobiliários\.

1513

5\.00

SIM

SIM

SIM

Serviços relacionados a operações de câmbio em geral, edição, alteração, prorrogação, cancelamento e baixa de contratos de câmbio; emissãode registro de exportação ou de crédito; cobrança ou depósito no exterior; emissão, forneciment o e

1514

5\.00

SIM

SIM

SIM

Fornecimento, emissão, reemissão, renovação e manutenção de cartão magnético, cartão de crédito, cartão de débito, cartão salário e congêneres

1515

5\.00

SIM

SIM

SIM

Compensação de cheques e de títulos quaisquer, serviços relacionados a depósito, inclusive depósito identificado, a saque de contas quaisquer, por qualquer meio ou processo, inclusive em terminais eletrônicos e de atendimento

1516

5\.00

SIM

SIM

SIM

Emissão, reemissão, liquidação, alteração, cancelamento e baixa de ordens de pagamento, ordens de crédito e similares, por qualquer meio ou processo; serviços relacionados à transferência de valores, dados, fundos, pagamentos e simila res,

1517

5\.00

SIM

SIM

SIM

Emissão, fornecimento, devolução, sustação, cancelamento e oposição de cheques quaisquer, avulso ou por talão

1518

5\.00

SIM

SIM

SIM

Serviços relacionados a crédito imobiliário, avaliação e vistoria de imóvel ou obra, análise técnica e jurídica, emissão, reemissão, alteração, transferência e renegociação de contrato, emissão e reemissão do termo de quitação e demais s erviç

1601

5\.00

SIM

SIM

SIM

Serviços de transporte coletivo municipal rodoviário, metroviário, ferroviário e aquaviário de passageiros\.

1602

5\.00

SIM

SIM

SIM

Outros serviços de transporte de natureza municipal\.

1701

3\.00

SIM

SIM

SIM

Assessoria ou consultoria de qualquer natureza, não contida em outros itens desta lista; análise, exame, pesquisa, coleta, compilação e fornecimento de dados e informações de qualquer natureza, inclusive cadastro e similares

1702

3\.00

SIM

SIM

SIM

Datilografia, digitação, estenografia, expediente, secretaria em geral, resposta audível, redação, edição, interpretação, revisão, tradução, apoio e infra\-estrutura administrativa e congêneres

1703

3\.00

SIM

SIM

SIM

Planejamento, coordenação, programação ou organização técnica, financeira ou administrativa

1704

3\.00

SIM

SIM

SIM

Recrutamento, agenciamento, seleção e colocação de mão\-de\-obra

1705

3\.00

SIM

SIM

SIM

Fornecimento de mão de obra,mesmo em caráter|temporário, inclusive de empregados ou trabalhadores, avulsos ou temporários, contratados pelo prestador de serviço\.

1706

3\.00

SIM

SIM

SIM

Propaganda e publicidade, inclusive promoção de vendas, planejamento de campanhas ou sistemas de publicidade, elaboração de desenhos, textos e demais materiais publicitários

1708

3\.00

SIM

SIM

SIM

Franquia

1709

3\.00

SIM

SIM

SIM

Perícias, laudos, exames técnicos e análises técnicas

1710

3\.00

SIM

SIM

SIM

Planejamento, organização e administração de feiras, exposições, congressos e congêneres\.

1711

3\.00

SIM

SIM

SIM

Organização de festas e recepções; bufê \(exceto o fornecimento de alimentação e bebidas, que fica sujeito ao ICMS\)

1712

3\.00

SIM

SIM

SIM

Administração em geral, inclusive de bens e negócios de terceiros

1713

3\.00

SIM

SIM

SIM

Leilão e congêneres

1714

3\.00

SIM

SIM

SIM

Advocacia

1715

3\.00

SIM

SIM

SIM

Arbitragem de qualquer espécie, inclusive jurídica

1716

3\.00

SIM

SIM

SIM

Auditoria

1717

3\.00

SIM

SIM

SIM

Análise de Organização e Métodos

1718

3\.00

SIM

SIM

SIM

Atuária e cálculos técnicos de qualquer natureza

1719

3\.00

SIM

SIM

SIM

Contabilidade, inclusive serviços técnicos e auxiliares

1720

3\.00

SIM

SIM

SIM

Consultoria e assessoria econômica ou financeira

1721

3\.00

SIM

SIM

SIM

Estatística

1722

3\.00

SIM

SIM

SIM

Cobrança em geral

1723

3\.00

SIM

SIM

SIM

Assessoria, análise, avaliação, atendimento, consulta, cadastro, seleção, gerenciamento de informações, administração de contas a receber ou a pagar e em geral, relacionados a operações de faturização \(factoring\)\.

1724

3\.00

SIM

SIM

SIM

Apresentação de palestras, conferências, seminários e congêneres

1725

3\.00

SIM

SIM

SIM

Inserção de textos, desenhos e outros materiais de propaganda e publicidade, em qualquer meio \(exceto em livros, jornais, periódicos e nas modalidades de serviços de radiodifusão sonora e de sons e imagens de recepção livre e gratuita\)

1801

5\.00

SIM

SIM

SIM

Serviços de regulação de sinistros vinculados a contratos de seguros; inspeção e avaliação de riscos para cobertura de seguros; prevenção e gerência de riscos seguráveis e congêneres

1901

5\.00

SIM

SIM

SIM

Serviços de distribuição e venda de bilhetes e demais produtos de loteria, bingos, cartões, pules ou cupons de apostas, sorteios, prêmios, inclusive os decorrentes de títulos de capitalização e congêneres

2001

3\.00

SIM

SIM

SIM

Serviços portuários, ferroportuários, utilização de porto, movimentação de passageiros, reboque de embarcações, rebocador escoteiro, atracação, de satracação, serviços de praticagem, capatazia, arma zenagem de qualquer natureza, serviços acessórios,

2002

3\.00

SIM

SIM

SIM

Serviços aeroportuários, utilização de aeroporto, movimentação de passageiros, armazenagem de qualquer natureza, capatazia, movimentação de aero\- naves, serviços de apoio aeroportuários, serviços acessórios, movimentação de mercadorias, lo gíst

2003

3\.00

SIM

SIM

SIM

Serviços de terminais rodoviários, ferroviários, metroviários, movimentação de passageiros, mercadorias,inclusive suas operações, logística e congêneres\.

2101

2\.50

SIM

SIM

SIM

Serviços de registros públicos, cartorários e notariais

2201

5\.00

SIM

SIM

SIM

Serviços de exploração de rodovia mediante cobrança de preço ou pedágio dos usuários, envolvendo execução de serviços de conservação, manutenção, melhoramentos para adequação de capacidade e segurança de trânsito, operação, monitoração, ass istên

2301

5\.00

SIM

SIM

SIM

Serviços de programação e comunicação visual, desenho industrial e congêneres

2401

3\.00

SIM

SIM

SIM

Serviços de chaveiros, confecção de carimbos, placas, sinalização visual, banners, adesivos e congêneres

2501

5\.00

SIM

SIM

SIM

Funerais, inclusive fornecimento de caixão,urna ou esquifes; aluguel de capela; transporte do corpo cadavérico; fornecimento de flores, coroas e outros paramentos; desembaraço de certidão de óbito; fornecimento de véu, essa e outros adornos; e mbal

2502

5\.00

SIM

SIM

SIM

Translado intramunicipal e cremação de corpos e partes de corpos cadavéricos

2503

5\.00

SIM

SIM

SIM

Planos ou convênio funerários

2504

5\.00

SIM

SIM

SIM

Manutenção e conservação de jazidos e cemitérios

2505

5\.00

SIM

SIM

SIM

Cessão de uso de espaços em cemitérios para sepultamento\.

2601

5\.00

SIM

SIM

SIM

Serviços de coleta, remessa ou entrega de correspondências, documentos, objetos, bens ou valores, inclusive pelos correios e suas agências franqueadas; courrier e congêneres

2701

2\.00

SIM

SIM

SIM

Serviços de assistência social

2801

5\.00

SIM

SIM

SIM

Serviços de avaliação de bens e serviços de qualquer natureza

2901

5\.00

SIM

SIM

SIM

Serviços de biblioteconomia

3001

3\.00

SIM

SIM

SIM

Serviços de biologia, biotecnologia e química

3101

5\.00

SIM

SIM

SIM

Serviços técnicos em edificações, eletrônica, eletrotécnica, mecânica, telecomunicações e congêneres

3201

5\.00

SIM

SIM

SIM

Serviços de desenhos técnicos

3301

3\.00

SIM

SIM

SIM

Serviços de desembaraço aduaneiro, comissários, despachantes e congêneres

3401

5\.00

SIM

SIM

SIM

Serviços de investigações particulares, detetives e congêneres

3501

3\.00

SIM

SIM

SIM

Serviços de reportagem, assessoria de imprensa, jornalismo e relações públicas

3601

3\.00

SIM

SIM

SIM

Serviços de meteorologia

3701

5\.00

SIM

SIM

SIM

Serviços de artistas, atletas, modelos e manequins

3801

3\.00

SIM

SIM

SIM

Serviços de museologia

3901

5\.00

SIM

SIM

SIM

Serviços de ourivesaria e lapidação

4001

3\.00

SIM

SIM

SIM

Obras de arte sob encomenda

40301

3\.00

SIM

SIM

SIM

Hospitais \(exceto para serviços prestados ao Sistema Único de Saúde, que se submetem à alíquota de 2%, de acordo com o parágrafo §5º deste artigo\)

40302

3\.00

SIM

SIM

SIM

Clínicas, laboratórios, sanatórios, manicômios, casas de saúde, prontos \- socorros, ambulatórios e congêneres

41901

3\.00

SIM

SIM

SIM

Bancos de sangue \(exceto para serviços prestados ao Sistema Único de Saúde, que se submetem à alíquota de 2%, de acordo com o parágrafo § 5º deste artigo\)

41902

3\.00

SIM

SIM

SIM

Bancos de leite, pele, olhos, óvulos, sêmen e congêneres

160101

2\.00

SIM

SIM

SIM

Concessionários de Transporte Público Coletivo Urbano de Passageiros, por ônibus

