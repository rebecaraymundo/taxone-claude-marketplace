# Layout - Bento_Goncalves

- **Fonte:** Layout - Bento_Goncalves.docx
- **Modificado:** 2021-05-03
- **Tamanho:** 59 KB

---

__[Layout do Registro Tipo 10 – Identificação do Documento Fiscal](https://www.nfs-e.net/datacenter/help/registro10.txt" \t "_blank)__  


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

Tipo do Documento \( 01 – Nota Fiscal Eletrônica de Serviços; 02 – Nota Fiscal Eletrônica Migrada; 03 – Nota em Bloco; 04 – Nota Fiscal de Serviços Eletrônica; 05 – Nota Fiscal de Serviços \(bloco\); 06 – Recibo \)

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

  
  
[__Layout do Registro Tipo 20 – Identificação dos serviços relacionados ao Documentos Fiscal__](https://www.nfs-e.net/datacenter/help/registro20.txt)  


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

Tipo do Documento \( 01 – Nota Fiscal Eletrônica de Serviços; 02 – Nota Fiscal Eletrônica Migrada; 03 – Nota em Bloco; 04 – Nota Fiscal de Serviços Eletrônica; 05 – Nota Fiscal de Serviços \(bloco\); 06 – Recibo \)

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

  
  
[__Layout do Registro Tipo 30 – Identificação da pessoa relacionada ao Documento Fiscal \*__](https://www.nfs-e.net/datacenter/help/registro30.txt)  


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

  
  
[__Layout do Registro Tipo 40 – Informações sobre o plano de contas da empresa__](https://www.nfs-e.net/datacenter/help/registro40.txt)  


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

__UNIDADES DE SERVIÇOS DISPONÍVEIS__:

__Código__

__Sigla__

__Descrição__

1

UND

Unidade

2

HR

Hora

3

M²

M2

__LISTA DE SERVIÇOS DISPONÍVEIS __:

__Código__

__Alíquota__

__Permite Sub\. Tributária__

__Padrão Trib\. Prestador__

__Permite Alterar Trib\. Prestador__

__Descrição__

101

3\.0000

NÃO

SIM

NÃO

Análise e desenvolvimento de sistemas\.

102

3\.0000

NÃO

SIM

NÃO

Programação\.

103

3\.0000

NÃO

SIM

NÃO

Processamento, armazenamento ou hospedagem de dados, textos, imagens, vídeos, páginas eletrônicas, aplicativos e sistemas de informação, entre outros formatos, e congêneres\.

104

3\.0000

NÃO

SIM

NÃO

Elaboração de programas de computadores, inclusive de jogos eletrônicos, independentemente da arquitetura construtiva da máquina em que o programa será executado, incluindo tablets, smartphones e congêneres\.

105

3\.0000

NÃO

SIM

NÃO

Licenciamento ou cessão de direito de uso de programas de computação\.

106

3\.0000

NÃO

SIM

NÃO

Assessoria e consultoria em informática\.

107

3\.0000

NÃO

SIM

NÃO

Suporte técnico em informática, inclusive instalação, configuração e manutenção de programas de computação e bancos de dados\.

108

3\.0000

NÃO

SIM

NÃO

Planejamento, confecção, manutenção e atualização de páginas eletrônicas\.

109

3\.0000

NÃO

SIM

NÃO

Disponibilização, sem cessão definitiva, de conteúdos de áudio, vídeo, imagem e texto por meio da internet, respeitada a imunidade de livros, jornais e periódicos \(exceto a distribuição de conteúdos pelas prestadoras de Serviço de Acesso Condicionado , de que trata a Lei no 12\.485, de 12 de setembro de 2011, sujeita ao ICMS\)\.

201

3\.0000

NÃO

SIM

NÃO

Serviços de pesquisas e desenvolvimento de qualquer natureza\.

301

0\.0000

NÃO

SIM

NÃO

\(VETADO\) \- Locação de bens móveis\.

302

3\.0000

NÃO

SIM

NÃO

Cessão de direito de uso de marcas e de sinais de propaganda\.

303

3\.0000

NÃO

SIM

NÃO

Exploração de salões de festas, centro de convenções, escritórios virtuais, stands, quadras esportivas, estádios, ginásios, auditórios, casas de espetáculos, parques de diversões, canchas e congêneres, para realização de eventos ou negócios de qualqu er natureza\.

304

3\.0000

NÃO

SIM

NÃO

Locação, sublocação, arrendamento, direito de passagem ou permissão de uso, compartilhado ou não, de ferrovia, rodovia, postes, cabos, dutos e condutos de qualquer natureza\.

305

3\.0000

SIM

SIM

SIM

Cessão de andaimes, palcos, coberturas e outras estruturas de uso temporário\.

401

3\.0000

NÃO

SIM

NÃO

Medicina e biomedicina\.

402

3\.0000

NÃO

SIM

NÃO

Análises clínicas, patologia, eletricidade médica, radioterapia, quimioterapia, ultra\-sonografia, ressonância magnética, radiologia, tomografia e congêneres\.

403

3\.0000

NÃO

SIM

NÃO

Hospitais, clínicas, laboratórios, sanatórios, manicômios, casas de saúde, prontos\-socorros, ambulatórios e congêneres\.

404

3\.0000

NÃO

SIM

NÃO

Instrumentação cirúrgica\.

405

3\.0000

NÃO

SIM

NÃO

Acupuntura\.

406

3\.0000

NÃO

SIM

NÃO

Enfermagem, inclusive serviços auxiliares\.

407

3\.0000

NÃO

SIM

NÃO

Serviços farmacêuticos\.

408

3\.0000

NÃO

SIM

NÃO

Terapia ocupacional, fisioterapia e fonoaudiologia\.

409

3\.0000

NÃO

SIM

NÃO

Terapias de qualquer espécie destinadas ao tratamento físico, orgânico e mental\.

410

3\.0000

NÃO

SIM

NÃO

Nutrição\.

411

3\.0000

NÃO

SIM

NÃO

Obstetrícia\.

412

3\.0000

NÃO

SIM

NÃO

Odontologia\.

413

3\.0000

NÃO

SIM

NÃO

Ortóptica\.

414

3\.0000

NÃO

SIM

NÃO

Próteses sob encomenda\.

415

3\.0000

NÃO

SIM

NÃO

Psicanálise\.

416

3\.0000

NÃO

SIM

NÃO

Psicologia\.

417

3\.0000

NÃO

SIM

NÃO

Casas de repouso e de recuperação, creches, asilos e congêneres\.

418

3\.0000

NÃO

SIM

NÃO

Inseminação artificial, fertilização in vitro e congêneres\.

419

3\.0000

NÃO

SIM

NÃO

Bancos de sangue, leite, pele, olhos, óvulos, sêmen e congêneres\.

420

3\.0000

NÃO

SIM

NÃO

Coleta de sangue, leite, tecidos, sêmen, órgãos e materiais biológicos de qualquer espécie\.

421

3\.0000

NÃO

SIM

NÃO

Unidade de atendimento, assistência ou tratamento móvel e congêneres\.

422

3\.0000

SIM

SIM

SIM

Planos de medicina de grupo ou individual e convênios para prestação de assistência médica, hospitalar, odontológica e congêneres\.

423

3\.0000

SIM

SIM

SIM

Outros planos de saúde que se cumpram através de serviços de terceiros contratados, credenciados, cooperados ou apenas pagos pelo operador do plano mediante indicação do beneficiário\.

501

3\.0000

NÃO

SIM

NÃO

Medicina veterinária e zootecnia\.

502

3\.0000

NÃO

SIM

NÃO

Hospitais, clínicas, ambulatórios, prontos\-socorros e congêneres, na área veterinária\.

503

3\.0000

NÃO

SIM

NÃO

Laboratórios de análise na área veterinária\.

504

3\.0000

NÃO

SIM

NÃO

Inseminação artificial, fertilização in vitro e congêneres\.

505

3\.0000

NÃO

SIM

NÃO

Bancos de sangue e de órgãos e congêneres\.

506

3\.0000

NÃO

SIM

NÃO

Coleta de sangue, leite, tecidos, sêmen, órgãos e materiais biológicos de qualquer espécie\.

507

3\.0000

NÃO

SIM

NÃO

Unidade de atendimento, assistência ou tratamento móvel e congêneres\.

508

3\.0000

NÃO

SIM

NÃO

Guarda, tratamento, amestramento, embelezamento, alojamento e congêneres\.

509

3\.0000

SIM

SIM

SIM

Planos de atendimento e assistência médico\-veterinária\.

601

3\.0000

NÃO

SIM

NÃO

Barbearia, cabeleireiros, manicuros, pedicuros e congêneres\.

602

3\.0000

NÃO

SIM

NÃO

Esteticistas, tratamento de pele, depilação e congêneres\.

603

3\.0000

NÃO

SIM

NÃO

Banhos, duchas, sauna, massagens e congêneres\.

604

3\.0000

NÃO

SIM

NÃO

Ginástica, dança, esportes, natação, artes marciais e demais atividades físicas\.

605

3\.0000

NÃO

SIM

NÃO

Centros de emagrecimento, spa e congêneres\.

606

3\.0000

NÃO

SIM

NÃO

Aplicação de tatuagens, piercings e congêneres\.

701

3\.0000

NÃO

SIM

NÃO

Engenharia, agronomia, agrimensura, arquitetura, geologia, urbanismo, paisagismo e congêneres\.

702

3\.0000

SIM

SIM

SIM

Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concr etagem e a instalação e montagem de produtos, peças e equipamentos \(exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS\)\.

703

3\.0000

NÃO

SIM

NÃO

Elaboração de planos diretores, estudos de viabilidade, estudos organizacionais e outros, relacionados com obras e serviços de engenharia

704

3\.0000

SIM

SIM

SIM

Demolição\.

705

3\.0000

SIM

SIM

SIM

Reparação, conservação e reforma de edifícios, estradas, pontes, portos e congêneres \(exceto o fornecimento de mercadorias produzidas pelo prestador dos serviços, fora do local da prestação dos serviços, que fica sujeito ao ICMS\)\.

706

3\.0000

NÃO

SIM

NÃO

Colocação e instalação de tapetes, carpetes, assoalhos, cortinas, revestimentos de parede, vidros, divisórias, placas de gesso e congêneres, com material fornecido pelo tomador do serviço\.

707

3\.0000

NÃO

SIM

NÃO

Recuperação, raspagem, polimento e lustração de pisos e congêneres\.

708

3\.0000

NÃO

SIM

NÃO

Calafetação\.

709

3\.0000

SIM

SIM

SIM

Varrição, coleta, remoção, incineração, tratamento, reciclagem, separação e destinação final de lixo, rejeitos e outros resíduos quaisquer\.

710

3\.0000

SIM

SIM

SIM

Limpeza, manutenção e conservação de vias e logradouros públicos, imóveis, chaminés, piscinas, parques, jardins e congêneres\.

711

3\.0000

SIM

SIM

SIM

Decoração e jardinagem, inclusive corte e poda de árvores\.

712

3\.0000

SIM

SIM

SIM

Controle e tratamento de efluentes de qualquer natureza e de agentes físicos, químicos e biológicos\.

713

3\.0000

NÃO

SIM

NÃO

Dedetização, desinfecção, desinsetização, imunização, higienização, desratização, pulverização e congêneres\.

714

0\.0000

NÃO

SIM

NÃO

\(VETADO\) \- Saneamento ambiental, inclusive purificação, tratamento, esgotamento sanitário e congêneres\.

715

0\.0000

NÃO

SIM

NÃO

\(VETADO\) \- Tratamento e purificação de água\.

716

3\.0000

SIM

SIM

SIM

Florestamento, reflorestamento, semeadura, adubação, reparação de solo, plantio, silagem, colheita, corte e descascamento de árvores, silvicultura, exploração florestal e dos serviços congêneres indissociáveis da formação, manutenção e colheita de fl orestas, para quaisquer fins e por quaisquer meios\.

717

3\.0000

SIM

SIM

SIM

Escoramento, contenção de encostas e serviços congêneres\.

718

3\.0000

SIM

SIM

SIM

Limpeza e dragagem de rios, portos, canais, baías, lagos, lagoas, represas, açudes e congêneres\.

719

3\.0000

SIM

SIM

SIM

Acompanhamento e fiscalização da execução de obras de engenharia, arquitetura e urbanismo\.

720

3\.0000

NÃO

SIM

NÃO

Aerofotogrametria \(inclusive interpretação\), cartografia, mapeamento, levantamentos topográficos, batimétricos, geográficos, geodésicos, geológicos, geofísicos e congêneres\.

721

3\.0000

NÃO

SIM

NÃO

Pesquisa, perfuração, cimentação, mergulho, perfilagem, concretação, testemunhagem, pescaria, estimulação e outros serviços relacionados com a exploração e explotação de petróleo, gás natural e de outros recursos minerais\.

722

3\.0000

NÃO

SIM

NÃO

Nucleação e bombardeamento de nuvens e congêneres\.

801

3\.0000

NÃO

SIM

NÃO

Ensino regular pré\-escolar, fundamental, médio e superior\.

802

3\.0000

NÃO

SIM

NÃO

Instrução, treinamento, orientação pedagógica e educacional, avaliação de conhecimentos de qualquer natureza\.

901

3\.0000

NÃO

SIM

NÃO

Hospedagem de qualquer natureza em hotéis, apart\-service condominiais, flat, apart\-hotéis, hotéis residência, residence\-service, suite service, hotelaria marítima, motéis, pensões e congêneres

902

3\.0000

NÃO

SIM

NÃO

Agenciamento, organização, promoção, intermediação e execução de programas de turismo, passeios, viagens, excursões, hospedagens e congêneres\.

903

3\.0000

NÃO

SIM

NÃO

Guias de turismo\.

1001

2\.0000

NÃO

SIM

NÃO

Agenciamento, corretagem ou intermediação de câmbio, de seguros, de cartões de crédito, de planos de saúde e de planos de previdência privada\.

1002

3\.0000

NÃO

SIM

NÃO

Agenciamento, corretagem ou intermediação de títulos em geral, valores mobiliários e contratos quaisquer\.

1003

3\.0000

NÃO

SIM

NÃO

Agenciamento, corretagem ou intermediação de direitos de propriedade industrial, artística ou literária\.

1004

3\.0000

SIM

SIM

SIM

Agenciamento, corretagem ou intermediação de contratos de arrendamento mercantil \(leasing\), de franquia \(franchising\) e de faturização \(factoring\)\.

1005

3\.0000

NÃO

SIM

NÃO

Agenciamento, corretagem ou intermediação de bens móveis ou imóveis, não abrangidos em outros itens ou subitens, inclusive aqueles realizados no âmbito de Bolsas de Mercadorias e Futuros, por quaisquer meios\.

1006

3\.0000

NÃO

SIM

NÃO

Agenciamento marítimo\.

1007

3\.0000

NÃO

SIM

NÃO

Agenciamento de notícias\.

1008

3\.0000

NÃO

SIM

NÃO

Agenciamento de publicidade e propaganda, inclusive o agenciamento de veiculação por quaisquer meios\.

1009

2\.0000

NÃO

SIM

NÃO

Representação de qualquer natureza, inclusive comercial\.

1010

3\.0000

NÃO

SIM

NÃO

Distribuição de bens de terceiros\.

1101

3\.0000

SIM

SIM

SIM

Guarda e estacionamento de veículos terrestres automotores, de aeronaves e de embarcações\.

1102

3\.0000

SIM

SIM

SIM

Vigilância, segurança ou monitoramento de bens, pessoas e semoventes\.

1103

3\.0000

NÃO

SIM

NÃO

Escolta, inclusive de veículos e cargas\.

1104

3\.0000

SIM

SIM

SIM

Armazenamento, depósito, carga, descarga, arrumação e guarda de bens de qualquer espécie\.

1201

3\.0000

SIM

SIM

SIM

Espetáculos teatrais\.

1202

3\.0000

SIM

SIM

SIM

Exibições cinematográficas\.

1203

3\.0000

SIM

SIM

SIM

Espetáculos circenses\.

1204

3\.0000

SIM

SIM

SIM

Programas de auditório\.

1205

3\.0000

SIM

SIM

SIM

Parques de diversões, centros de lazer e congêneres\.

1206

3\.0000

SIM

SIM

SIM

Boates, taxi\-dancing e congêneres\.

1207

3\.0000

SIM

SIM

SIM

Shows, ballet, danças, desfiles, bailes, óperas, concertos, recitais, festivais e congêneres\.

1208

3\.0000

SIM

SIM

SIM

Feiras, exposições, congressos e congêneres\.

1209

5\.0000

SIM

SIM

SIM

Bilhares, boliches e diversões eletrônicas ou não\.

1210

5\.0000

SIM

SIM

SIM

Corridas e competições de animais\.

1211

3\.0000

SIM

SIM

SIM

Competições esportivas ou de destreza física ou intelectual, com ou sem a participação do espectador\.

1212

3\.0000

SIM

SIM

SIM

Execução de música\.

1213

3\.0000

NÃO

SIM

NÃO

Produção, mediante ou sem encomenda prévia, de eventos, espetáculos, entrevistas, shows, ballet, danças, desfiles, bailes, teatros, óperas, concertos, recitais, festivais e congêneres\.

1214

3\.0000

SIM

SIM

SIM

Fornecimento de música para ambientes fechados ou não, mediante transmissão por qualquer processo\.

1215

3\.0000

SIM

SIM

SIM

Desfiles de blocos carnavalescos ou folclóricos, trios elétricos e congêneres\.

1216

3\.0000

SIM

SIM

SIM

Exibição de filmes, entrevistas, musicais, espetáculos, shows, concertos, desfiles, óperas, competições esportivas, de destreza intelectual ou congêneres\.

1217

3\.0000

SIM

SIM

SIM

Recreação e animação, inclusive em festas e eventos de qualquer natureza\.

1301

0\.0000

NÃO

SIM

NÃO

\(VETADO\) \- Produção, gravação, edição, legendagem e distribuição de filmes, video\-tapes, discos, fitas cassete, compact disc, digital video disc e congêneres\.

1302

3\.0000

NÃO

SIM

NÃO

Fonografia ou gravação de sons, inclusive trucagem, dublagem, mixagem e congêneres\.

1303

3\.0000

NÃO

SIM

NÃO

Fotografia e cinematografia, inclusive revelação, ampliação, cópia, reprodução, trucagem e congêneres\.

1304

3\.0000

NÃO

SIM

NÃO

Reprografia, microfilmagem e digitalização\.

1305

3\.0000

NÃO

SIM

NÃO

Composição gráfica, inclusive confecção de impressos gráficos, fotocomposição, clicheria, zincografia, litografia e fotolitografia, exceto se destinados a posterior operação de comercialização ou industrialização, ainda que incorporados, de qualquer forma, a outra mercadoria que deva ser objeto de posterior circulação, tais como bulas, rótulos, etiquetas, caixas, cartuchos, embalagens e manuais técnicos e de instrução, quando ficarão sujeitos ao ICMS\.

1401

3\.0000

NÃO

SIM

NÃO

Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto \(exceto peças e partes empregadas, que fi cam sujeitas ao ICMS\)\.

1402

3\.0000

NÃO

SIM

NÃO

Assistência técnica\.

1403

3\.0000

NÃO

SIM

NÃO

Recondicionamento de motores \(exceto peças e partes empregadas, que ficam sujeitas ao ICMS\)\.

1404

3\.0000

NÃO

SIM

NÃO

Recauchutagem ou regeneração de pneus\.

1405

3\.0000

NÃO

SIM

NÃO

Restauração, recondicionamento, acondicionamento, pintura, beneficiamento, lavagem, secagem, tingimento, galvanoplastia, anodização, corte, recorte, plastificação, costura, acabamento, polimento e congêneres de objetos quaisquer\.

1406

3\.0000

NÃO

SIM

NÃO

Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido\.

1407

3\.0000

NÃO

SIM

NÃO

Colocação de molduras e congêneres\.

1408

3\.0000

NÃO

SIM

NÃO

Encadernação, gravação e douração de livros, revistas e congêneres\.

1409

3\.0000

NÃO

SIM

NÃO

Alfaiataria e costura, quando o material for fornecido pelo usuário final, exceto aviamento\.

1410

3\.0000

NÃO

SIM

NÃO

Tinturaria e lavanderia\.

1411

3\.0000

NÃO

SIM

NÃO

Tapeçaria e reforma de estofamentos em geral\.

1412

3\.0000

NÃO

SIM

NÃO

Funilaria e lanternagem\.

1413

3\.0000

NÃO

SIM

NÃO

Carpintaria e serralheria\.

1414

3\.0000

NÃO

SIM

NÃO

Guincho intramunicipal, guindaste e içamento\.

1501

5\.0000

SIM

SIM

SIM

Administração de fundos quaisquer, de consórcio, de cartão de crédito ou débito e congêneres, de carteira de clientes, de cheques pré\-datados e congêneres\.

1502

5\.0000

NÃO

SIM

NÃO

Abertura de contas em geral, inclusive conta\-corrente, conta de investimentos e aplicação e caderneta de poupança, no País e no exterior, bem como a manutenção das referidas contas ativas e inativas\.

1503

5\.0000

NÃO

SIM

NÃO

Locação e manutenção de cofres particulares, de terminais eletrônicos, de terminais de atendimento e de bens e equipamentos em geral\.

1504

5\.0000

NÃO

SIM

NÃO

Fornecimento ou emissão de atestados em geral, inclusive atestado de idoneidade, atestado de capacidade financeira e congêneres\.

1505

5\.0000

NÃO

SIM

NÃO

Cadastro, elaboração de ficha cadastral, renovação cadastral e congêneres, inclusão ou exclusão no Cadastro de Emitentes de Cheques sem Fundos

1506

5\.0000

NÃO

SIM

NÃO

Emissão, reemissão e fornecimento de avisos, comprovantes e documentos em geral

1507

5\.0000

NÃO

SIM

NÃO

Acesso, movimentação, atendimento e consulta a contas em geral, por qualquer meio ou processo, inclusive por telefone, fac\-símile, internet e telex, acesso a terminais de atendimento, inclusive vinte e quatro horas

1508

5\.0000

NÃO

SIM

NÃO

Emissão, reemissão, alteração, cessão, substituição, cancelamento e registro de contrato de crédito

1509

5\.0000

SIM

SIM

SIM

Arrendamento mercantil \(leasing\) de quaisquer bens, inclusive cessão de direitos e obrigações, substituição de garantia, alteração, cancelamento e registro de contrato, e demais serviços relacionados ao arrendamento mercantil \(leasing\)\.

1510

5\.0000

NÃO

SIM

NÃO

Serviços relacionados a cobranças, recebimentos ou pagamentos em geral, de títulos quaisquer, de contas ou carnês, de câmbio, de tributos e por conta de terceiros, inclusive os efetuados por meio eletrônico, automático ou por máquinas de atendimento

1511

5\.0000

NÃO

SIM

NÃO

Devolução de títulos, protesto de títulos, sustação de protesto, manutenção de títulos, reapresentação de títulos, e demais serviços a eles relacionados\.

1512

5\.0000

NÃO

SIM

NÃO

Custódia em geral, inclusive de títulos e valores mobiliários\.

1513

5\.0000

NÃO

SIM

NÃO

Serviços relacionados a operações de câmbio em geral, edição, alteração, prorrogação, cancelamento e baixa de contrato de câmbio

1514

5\.0000

NÃO

SIM

NÃO

Fornecimento, emissão, reemissão, renovação e manutenção de cartão magnético, cartão de crédito, cartão de débito, cartão salário e congêneres\.

1515

5\.0000

NÃO

SIM

NÃO

Compensação de cheques e títulos quaisquer

1516

5\.0000

NÃO

SIM

NÃO

Emissão, reemissão, liquidação, alteração, cancelamento e baixa de ordens de pagamento, ordens de crédito e similares, por qualquer meio ou processo

1517

5\.0000

NÃO

SIM

NÃO

Emissão, fornecimento, devolução, sustação, cancelamento e oposição de cheques quaisquer, avulso ou por talão\.

1518

5\.0000

NÃO

SIM

NÃO

Serviços relacionados a crédito imobiliário, avaliação e vistoria de imóvel ou obra, análise técnica e jurídica, emissão, reemissão, alteração, transferência e renegociação de contrato, emissão e reemissão do termo de quitação e demais serviços relac ionados a crédito imobiliário\.

1601

3\.0000

SIM

SIM

SIM

Serviços de transporte coletivo municipal rodoviário, metroviário, ferroviário e aquaviário de passageiros\.

1602

3\.0000

SIM

SIM

SIM

Outros serviços de transporte de natureza municipal\.

1701

3\.0000

NÃO

SIM

NÃO

Assessoria ou consultoria de qualquer natureza, não contida em outros itens desta lista

1702

3\.0000

NÃO

SIM

NÃO

Datilografia, digitação, estenografia, expediente, secretaria em geral, resposta audível, redação, edição, interpretação, revisão, tradução, apoio e infra\-estrutura administrativa e congêneres\.

1703

3\.0000

NÃO

SIM

NÃO

Planejamento, coordenação, programação ou organização técnica, financeira ou administrativa\.

1704

3\.0000

NÃO

SIM

NÃO

Recrutamento, agenciamento, seleção e colocação de mão\-de\-obra\.

1705

3\.0000

SIM

SIM

SIM

Fornecimento de mão\-de\-obra, mesmo em caráter temporário, inclusive de empregados ou trabalhadores, avulsos ou temporários, contratados pelo prestador de serviço\.

1706

3\.0000

NÃO

SIM

NÃO

Propaganda e publicidade, inclusive promoção de vendas, planejamento de campanhas ou sistemas de publicidade, elaboração de desenhos, textos e demais materiais publicitários\.

1707

0\.0000

NÃO

SIM

NÃO

\(VETADO\) \- Veiculação e divulgação de textos, desenhos e outros materiais de propaganda e publicidade, por qualquer meio\.

1708

3\.0000

NÃO

SIM

NÃO

Franquia \(franchising\)\.

1709

3\.0000

NÃO

SIM

NÃO

Perícias, laudos, exames técnicos e análises técnicas\.

1710

3\.0000

SIM

SIM

SIM

Planejamento, organização e administração de feiras, exposições, congressos e congêneres\.

1711

3\.0000

NÃO

SIM

NÃO

Organização de festas e recepções

1712

3\.0000

NÃO

SIM

NÃO

Administração em geral, inclusive de bens e negócios de terceiros\.

1713

3\.0000

NÃO

SIM

NÃO

Leilão e congêneres\.

1714

3\.0000

NÃO

SIM

NÃO

Advocacia\.

1715

3\.0000

NÃO

SIM

NÃO

Arbitragem de qualquer espécie, inclusive jurídica\.

1716

3\.0000

NÃO

SIM

NÃO

Auditoria\.

1717

3\.0000

NÃO

SIM

NÃO

Análise de Organização e Métodos\.

1718

3\.0000

NÃO

SIM

NÃO

Atuária e cálculos técnicos de qualquer natureza\.

1719

3\.0000

NÃO

SIM

NÃO

Contabilidade, inclusive serviços técnicos e auxiliares\.

1720

3\.0000

NÃO

SIM

NÃO

Consultoria e assessoria econômica ou financeira\.

1721

3\.0000

NÃO

SIM

NÃO

Estatística\.

1722

3\.0000

NÃO

SIM

NÃO

Cobrança em geral\.

1723

3\.0000

NÃO

SIM

NÃO

Assessoria, análise, avaliação, atendimento, consulta, cadastro, seleção, gerenciamento de informações, administração de contas a receber ou a pagar e em geral, relacionados a operações de faturização \(factoring\)\.

1724

3\.0000

NÃO

SIM

NÃO

Apresentação de palestras, conferências, seminários e congêneres\.

1725

3\.0000

NÃO

SIM

NÃO

Inserção de textos, desenhos e outros materiais de propaganda e publicidade, em qualquer meio \(exceto em livros, jornais, periódicos e nas modalidades de serviços de radiodifusão sonora e de sons e imagens de recepção livre e gratuita\)\.

1801

3\.0000

NÃO

SIM

NÃO

Serviços de regulação de sinistros vinculados a contratos de seguros

1901

3\.0000

NÃO

SIM

NÃO

Serviços de distribuição e venda de bilhetes e demais produtos de loteria, bingos, cartões, pules ou cupons de apostas, sorteios, prêmios, inclusive os decorrentes de títulos de capitalização e congêneres\.

2001

3\.0000

SIM

SIM

SIM

Serviços portuários, ferroportuários, utilização de porto, movimentação de passageiros, reboque de embarcações, rebocador escoteiro, atracação, desatracação, serviços de praticagem, capatazia, armazenagem de qualquer natureza, serviços acessórios, mo vimentação de mercadorias, serviços de apoio marítimo, de movimentação ao largo, serviços de armadores, estiva, conferência, logística e congêneres\.

2002

3\.0000

SIM

SIM

SIM

Serviços aeroportuários, utilização de aeroporto, movimentação de passageiros, armazenagem de qualquer natureza, capatazia, movimentação de aeronaves, serviços de apoio aeroportuários, serviços acessórios, movimentação de mercadorias, logística e con gêneres\.

2003

3\.0000

SIM

SIM

SIM

Serviços de terminais rodoviários, ferroviários, metroviários, movimentação de passageiros, mercadorias, inclusive suas operações, logística e congêneres\.

2101

5\.0000

NÃO

SIM

NÃO

Serviços de registros públicos, cartorários e notariais\.

2201

5\.0000

NÃO

SIM

NÃO

Serviços de exploração de rodovia mediante cobrança de preço ou pedágio dos usuários, envolvendo execução de serviços de conservação, manutenção, melhoramentos para adequação de capacidade e segurança de trânsito, operação, monitoração, assistência a os usuários e outros serviços definidos em contratos, atos de concessão ou de permissão ou em normas oficiais\.

2301

3\.0000

NÃO

SIM

NÃO

Serviços de programação e comunicação visual, desenho industrial e congêneres\.

2401

3\.0000

NÃO

SIM

NÃO

Serviços de chaveiros, confecção de carimbos, placas, sinalização visual, banners, adesivos e congêneres\.

2501

3\.0000

NÃO

SIM

NÃO

Funerais, inclusive fornecimento de caixão, urna ou esquifes

2502

3\.0000

NÃO

SIM

NÃO

Translado intramunicipal e cremação de corpos e partes de corpos cadavéricos\.

2503

3\.0000

NÃO

SIM

NÃO

Planos ou convênio funerários\.

2504

3\.0000

NÃO

SIM

NÃO

Manutenção e conservação de jazigos e cemitérios\.

2505

3\.0000

NÃO

SIM

NÃO

Cessão de uso de espaços em cemitérios para sepultamento\.

2601

3\.0000

NÃO

SIM

NÃO

Serviços de coleta, remessa ou entrega de correspondências, documentos, objetos, bens ou valores, inclusive pelos correios e suas agências franqueadas

2701

3\.0000

NÃO

SIM

NÃO

Serviços de assistência social\.

2801

3\.0000

NÃO

SIM

NÃO

Serviços de avaliação de bens e serviços de qualquer natureza\.

2901

3\.0000

NÃO

SIM

NÃO

Serviços de biblioteconomia\.

3001

3\.0000

NÃO

SIM

NÃO

Serviços de biologia, biotecnologia e química\.

3101

5\.0000

NÃO

SIM

NÃO

Serviços técnicos em edificações, eletrônica, eletrotécnica, mecânica, telecomunicações e congêneres\.

3201

3\.0000

NÃO

SIM

NÃO

Serviços de desenhos técnicos\.

3301

3\.0000

NÃO

SIM

NÃO

Serviços de desembaraço aduaneiro, comissários, despachantes e congêneres\.

3401

3\.0000

NÃO

SIM

NÃO

Serviços de investigações particulares, detetives e congêneres\.

3501

3\.0000

NÃO

SIM

NÃO

Serviços de reportagem, assessoria de imprensa, jornalismo e relações públicas\.

3601

3\.0000

NÃO

SIM

NÃO

Serviços de meteorologia\.

3701

3\.0000

NÃO

SIM

NÃO

Serviços de artistas, atletas, modelos e manequins\.

3801

3\.0000

NÃO

SIM

NÃO

Serviços de museologia\.

3901

3\.0000

NÃO

SIM

NÃO

Serviços de ourivesaria e lapidação \(quando o material for fornecido pelo tomador do serviço\)\.

4001

3\.0000

NÃO

SIM

NÃO

Obras de arte sob encomenda\.

9999

3\.0000

NÃO

SIM

NÃO

Outros Serviços

