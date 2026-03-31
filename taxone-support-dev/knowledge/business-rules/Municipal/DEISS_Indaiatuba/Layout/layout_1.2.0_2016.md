# layout_1.2.0_2016

- **Fonte:** layout_1.2.0_2016.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 59 KB

---

__            Prefeitura Municipal de Indaiatuba__

__Secretaria da Fazenda   
Departamento de Rendas Mobiliárias   
Departamento de Informática__ 

__Leiaute de Importação de Escrituração para o Sistema DEISS__

__Versão 1\.2\.0 \- 01/03/2016__

O leiaute deverá ser apresentado em dois arquivos no formato texto \- TXT, contendo apenas caracteres da tabela ASCII, com no máximo 50 \(cinquenta\) registros por arquivo\. Um arquivo deverá conter as informações sobre os serviços prestados, e o outro arquivo sobre os serviços tomados\. As notas emitidas para pessoas físicas que estiverem em sequência e possuírem o mesmo valor, podem ser informadas em lote, utilizando o número da nota inicial e da nota final, o CPF deverá ser informado da seguinte forma: 00099999999999\. As notas emitidas para pessoa jurídica devem ser lançadas uma a uma e o campo “Nota fiscal final” deverá conter o mesmo número que o campo “Nota fiscal inicial”\.

Para empresas quem emitem a Nota Fiscal Eletrônica de Serviços \(NFS\-E\) o sistema faz a escrituração automática tanto para o prestador quanto para o tomador do serviço, portanto, __as Notas Fiscais Eletrônicas emitidas por prestadores do Município de Indaiatuba não devem ser escrituradas__\.

Qualquer dúvida referente ao código e ao enquadramento da atividade ou serviço, verifique a lista de serviços ISSQN no site da Prefeitura Municipal de Indaiatuba: [http://www\.indaiatuba\.sp\.gov\.br/fazenda/rendas\-mobiliarias/listas/lista\-de\-servicos\-issqn/](http://www.indaiatuba.sp.gov.br/fazenda/rendas-mobiliarias/listas/lista-de-servicos-issqn/)

__Arquivo com as informações de serviços prestados\.__

__Col ini__

__Col fin__

__Tam__

__Tp__

__Ob__

__Descrição__

01

09

09

N

S

CCM \(Inscrição Municipal\) do __Prestador__, exemplo: 001214113

10

15

06

N

S

Competência \(aaaamm\), exemplo: 200806

16

21

06

N

S

Código da atividade ou serviço, exemplos: 001405, 000702, 000705

22

23

02

N

S

Dia da emissão da nota, exemplos: 01, 09, 12, 31

24

32

09

N

S

Nota fiscal inicial, exemplos: 123456789, 000000114, 000000009

33

41

09

N

S

Nota final inicial, exemplos: 123456789, 000000114, 000000009

42

46

05

C

S

Série da nota fiscal \(espaços em branco são permitidos, desde que se respeite o tamanho do campo\), exemplos: A, A1, U, NFE

47

47

01

C

N

Tipo de lançamento de Nota Fiscal: 

C = Cancelada  
F = Fixo  
I = Isento  
O = Retenção em outro município  
S = Simples Nacional  
U = Imune  
V = Variável

48

59

12

N

S

Valor da nota fiscal sem pontuação \(no caso de nota conjugada informar apenas o valor do serviço\), exemplos: 000000045323 = R$ 453,23; 000000000100 = R$ 1,00

60

63

04

N

S

Alíquota \(%\) de imposto, exemplos: 0250 = 2,50%; 0200 = 2% \(se a empresa estiver inscrita no Simples Nacional a alíquota informada deve ser igual à do enquadramento no Simples Nacional\)

64

74

11

N

S

Valor do imposto exemplo: 00000008011 = R$ 80,11; 00000000010 = R$ 0,10

75

88

14

N

S

CPF ou CNPJ do Tomador \(Informar sempre em quatorze casas preenchendo com zeros à esquerda\), exemplos: 44733608000109, 00733608000109, 00012345678910, utilizar 00099999999999 para identificar pessoa física no caso de regime especial de tributação, ou 99999999999999 para empresas no exterior\. 

89

188

100

C

N

Nome ou Razão Social do Tomador, colocar o nome completo da empresa em letras maiúsculas, os nomes com mais de 100 caracteres poderão ser abreviados

189

200

12

N

N

Valor do desconto de materiais\. Conforme a Instrução Normativa n\. 003/10 e art\. 54 §4º da Lei n\. 4\.447/2003, deverá apresentar junto ao fisco municipal até o dia 10 do mês subsequente da emissão da nota fiscal de prestação de serviços, os documentos comprobatórios especificados no art\. 1º da presente Instrução Normativa\. Exemplos: 00000000811 = R$ 8,11; 00000008110 = R$ 81,10 

201

215

14

N

S

CPF ou CNPJ do __Prestador__ \(Informar sempre em quatorze casas preenchendo com zeros à esquerda\), exemplos: 44733608000109, 00733608000109, 00012345678910\. O preenchimento desse campo é obrigatório apenas para empresas que não possuem CCM \(Cadastro Municipal\) em Indaiatuba\.

__Arquivo com as informações de serviços tomados__ 

__Col ini__

__Col fin__

__Tam__

__Tp__

__Ob__

__Descrição__

01

09

09

N

S

CCM \(Inscrição Municipal\) do __Tomador__, exemplo: 001214113

10

15

06

N

S

Competência \(aaaamm\), exemplo: 200806

16

21

06

N

S

Código da atividade ou serviço, exemplos: 001405, 000702, 000705

22

23

02

N

S

Dia da emissão da nota, exemplos: 01, 09, 12, 31

24

32

09

N

S

Nota fiscal inicial, exemplos: 123456789, 000000114, 000000009

33

41

09

N

S

Nota final inicial, exemplos: 123456789, 000000114, 000000009

42

46

05

C

S

Série da nota fiscal \(espaços em branco são permitidos, desde que se respeite o tamanho do campo\), exemplos: A, A1, U, NFE 

47

47

01

C

N

Tipo de lançamento de Nota Fiscal: 

C = Cancelada  
O = Retenção em outro município  
S = Simples Nacional  
V = Variável  
U = Imune

48

59

12

N

S

Valor da nota fiscal sem pontuação \(no caso de nota conjugada informar apenas o valor do serviço\), exemplos: 000000045323 = R$ 453,23; 000000000100 = R$ 1,00

60

63

04

N

S

Alíquota \(%\) de imposto, exemplos: 0250 = 2,50%; 0200 = 2% \(se a empresa estiver inscrita no Simples Nacional a alíquota informada, para os itens de exceção, deve ser igual ao enquadramento no Simples Nacional\)

64

74

11

N

S

Valor do imposto exemplo: 00000008011 = R$ 80,11; 00000000010 = R$ 0,10

75

88

14

N

S

CPF ou CNPJ do Prestador \(Informar sempre em quatorze casas preenchendo com zeros à esquerda\), exemplos: 44733608000109, 00733608000109, 00012345678910, utilizar 99999999999999 para empresas no exterior\. 

89

188

100

C

N

Nome ou Razão Social do Prestador, colocar o nome completo da empresa em letras maiúsculas, os nomes com mais de 100 caracteres poderão ser abreviados

189

200

12

N

N

Valor do desconto de materiais\. Conforme a Instrução Normativa n\. 003/10 e art\. 54 §4º da Lei n\. 4\.447/2003, deverá apresentar junto ao fisco municipal até o dia 10 do mês subsequente da emissão da nota fiscal de prestação de serviços, os documentos comprobatórios especificados no art\. 1º da presente Instrução Normativa\. Exemplos: 00000000811 = R$ 8,11; 00000008110 = R$ 81,10 

201

215

14

N

S

CPF ou CNPJ do __Tomador__ \(Informar sempre em quatorze casas preenchendo com zeros à esquerda\), exemplos: 44733608000109, 00733608000109, 00012345678910\. O preenchimento desse campo é obrigatório apenas para empresas que não possuem CCM \(Cadastro Municipal\) em Indaiatuba\.

__Leiaute do Arquivo de Retorno Gerado pelo Sistema DEISS__

__Col ini__

__Col fin__

__Tam__

__Tp__

__Ob__

__Descrição__

01

09

09

N

S

CCM \(Inscrição Municipal\) do __Contribuinte__, exemplo: 001214113

10

11

01

C

S

Tipo de escrituração: 'P' para serviços Prestados e 'T' para serviços Tomados\.

12

17

06

N

S

Competência da emissão da nota fiscal \(aaaamm\), exemplo: 200901

18

26

09

N

S

Número da Nota Fiscal inicial\.

27

35

09

N

S

Número da Nota Fiscal final\.

36

43

08

D

S

Data de emissão \(aaaammdd\)\. Exemplo: 20090301

44

49

06

N

S

Código do serviço prestado exemplos: 001405, 000702, 000705

50

53

04

N

S

Alíquota

54

67

14

N

S

Valor total do serviço, sem pontuação \(no caso de nota conjugada informar apenas o valor do serviço\)\. Exemplos: 00000000005323 = R$ 53,23; 00000000000100 = R$ 1,00\.

68

81

14

N

N

Valor total de deduções

82

95

14

N

S

Valor Imposto \(valor do ISSQN em Indaiatuba\)\.

96

97

01

C

S

Retenção:

E = Suspensão de exigibilidade  
F = Fixo  
I = Isento  
M = Micro Empreendedor Individual  
N = Não Incidente  
O = Retenção em outro município  
S = Simples Nacional  
U = Imune  
V = Variável

98

99

01

C

S

Situação:

C = Cancelada  
N = Normal  
S = Substituída  
U = Substituta

100

113

14

N

S

CPF ou CNPJ do Tomador/ Prestador \(sempre em quatorze casas preenchendo com zeros à esquerda\)\. Exemplos: 44733608000109, 00733608000109, 00012345678910, __99999999999999 __para empresas no exterior e__ 00099999999999__ para identificar pessoa física no caso de regime especial de tributação\. 

114

213

100

C

N

Razão Social do Tomador/ Prestador\.

__Legenda__

__Informação__

__Identificação da Informação__

__Col ini__

Coluna inicial

Número da coluna do primeiro caractere do campo

__Col fin__

Coluna final

Número da coluna do último caractere do campo

__Tam__

Tamanho

Quantidade de caracteres fixa

__Tp__

Tipo

C – caracteres \(preencher com espaços em branco a direita até completar o tamanho do campo\), em campos não obrigatórios preencher com espaços\.

D – Data \(as datas deverão ser informadas no formato aaaammdd ano, mês e dia\)

N – numérico \(preencher com zeros a esquerda até completar o tamanho do campo, os dois últimos campos serão considerados como casas decimais\), em campos não obrigatórios preencher com zeros\. Os caracteres de formatação \(máscaras\) devem ser removidos\. 

T – texto \(não serão aceitos caracteres de quebra de linha ou de tabulação\), tamanho mínimo 01 \(um\) caractere, tamanho máximo 2000 \(dois mil\) caracteres

__Ob__

Obrigatório

Obrigatoriedade de preenchimento \(Quando o tomador é estrangeiro não é obrigatório informar o endereço\)

__Descrição__

Breve descrição da informação que deverá conter o campo

__Prefeitura Municipal de Indaiatuba__

__Secretaria da Fazenda   
Departamento de Rendas Mobiliárias   
Departamento de Informática__ 

__Nota Fiscal de Serviços Eletrônica NFS\-e \- DEISS__

__Leiaute de Importação de Dados para Emissão de NFS\-e__

__Versão 1\.2\.0 \- 01/03/2016__

Os arquivos devem ser gerados no formato texto – TXT, contendo apenas caracteres da tabela ASCII, contendo as informações sobre os serviços prestados, com no máximo 50 \(cinquenta\) registros por arquivo, cada linha do arquivo de conter um registro, uma quebra de linha deve ser inserida no final de cada registro\. Os registros devem estrar ordenados pelo campo __Data do RPS__, por ordem crescente, será aceita apenas uma atividade por Nota Fiscal, é obrigatório indicar o número do Recibo Provisório de serviços \(RPS\) para gerar as Notas Fiscais Eletrônicas\. Qualquer dúvida referente ao código e ao enquadramento da atividade ou serviço verifique a lista de serviços ISSQN no site da Prefeitura Municipal de Indaiatuba: [http://www\.indaiatuba\.sp\.gov\.br/fazenda/rendas\-mobiliarias/listas/lista\-de\-servicos\-issqn/](http://www.indaiatuba.sp.gov.br/fazenda/rendas-mobiliarias/listas/lista-de-servicos-issqn/)

__Antes do arquivo ser convertido em Notas Fiscais Eletrônicas, verifique as seguintes regras: __

1\) A data do Recibo Provisório de Serviços \- RPS não pode ser menor do que a data de autorização para emissão de NFS\-e requerida junto a Prefeitura\.

2\) A substituição do RPS pela NFS\-e deverá ser efetuada no prazo máximo de 5 \(cinco\) dias corridos após a data de sua emissão\.

3\) O campo “descrição do serviço” pode conter até 2000 caracteres, o sistema não vai considerar tabulações ou caracteres de quebra de linha\. Quebras de linha devem ser indicadas pelo caractere | \(*pipe* ou barra vertical, ASCII 124\)\.

4\) Caso o e\-mail do tomador seja informado e esteja correto, o sistema enviará automaticamente um e\-mail informando o link para a visualização da Nota Fiscal emitida, tanto para o prestador como para o tomador do serviço, se o e\-mail do tomador não for informado, o prestador e o tomador não receberão o e\-mail\.

5\) Os campos devem possuir número fixo de colunas, com exceção do campo Descrição do serviço, os campos do tipo numérico devem ser completados com zeros a esquerda e os campos do tipo caractere devem ser completados com espaços em branco até atingirem o número de colunas determinadas\. Todos os caracteres de formatação \(mascaras\) devem ser removidos\.

7\) Os arquivos serão validados pelo sistema DEISS antes de serem convertidos em Notas Fiscais, caso haja alguma inconsistência, o sistema vai informar a linha e o campo com problema, o arquivo só será convertido em NFS\-e se todos os campos de todos os registros estiverem corretos\.

__Leiaute de Importação de Dados para Emissão de NFS\-e__

__Col ini__

__Col fin__

__Tam__

__Tp__

__Ob__

__Descrição__

01

09

09

N

S

CCM \(Inscrição Municipal\) do Prestador, exemplo: 001214113

10

15

06

N

S

Competência da data do RPS \(aaaamm\), exemplo: 201001

16

23

08

D

S

Data do RPS \(aaaammdd\), exemplo: 20090301

24

29

06

N

S

Código do serviço prestado, conforme lista de serviços sujeitos ao ISSQN, exemplos: 001405, 000702, 000705

30

43

14

N

S

Valor total do serviço, sem pontuação \(no caso de nota conjugada informar apenas o valor do serviço\)\. Exemplos: 00000000005323 = R$ 53,23; 00000000000100 = R$ 1,00\.

44

57

14

N

N

Valor total de deduções \(apenas para as atividades previstas no Art\. 11 do Decreto N\.º 10\.502 de 04 de dezembro de 2009\)\. Para as atividades 702 e 705, a empresa deverá obrigatoriamente, no prazo de 30 dias, apresentar ao Fisco Municipal, as 1ªs vias das notas fiscais de materiais abatidos\.

58

58

01

C

S

Tipo de lançamento da Nota Fiscal \('T' para Tributado, 'I' para Isento ou Imune e 'R' não tributado no município de Indaiatuba\)\.

59

108

50

C

S

Município onde foi realizado o serviço, nome sem abreviações, conforme descrito no IBGE \(Instituto Brasileiro de Geografia e Estatística\)\.

109

110

02

C

S

Sigla da UF onde foi realizado o serviço\.

111

111

01

C

S

Pessoa Física ou Jurídica \(F ou J\)\.

112

161

50

C

N

País de origem do tomador para empresas no exterior, nome sem abreviações, conforme descrito no IBGE\. Para empresas no Brasil preencher com espaços em branco\. 

162

175

14

N

S

CPF ou CNPJ do __Tomador__ \(Informar sempre em quatorze casas preenchendo com zeros à esquerda\)\. Exemplos: 44733608000109, 00733608000109, 00012345678910, utilizar __99999999999999 __para empresas no exterior e __00099999999999__ para identificar pessoa física no caso de regime especial de tributação, campo de preenchimento obrigatório\. 

176

275

100

C

S

Razão Social do Tomador, nome completo da empresa, nomes com mais de 100 caracteres podem ser abreviados, no caso de empresas no exterior ou de regime especial de tributação, o nome não precisa ser informado\. 

276

325

50

C

S

Município \(referente ao endereço do Tomador\), nome sem abreviações, conforme descrito no IBGE \(Instituto Brasileiro de Geografia e Estatística\)\.

326

327

02

C

S

UF \(referente ao endereço do Tomador\)\.

328

329

02

C

N

Tipo do bairro \(referente ao endereço do Tomador\), conforme o sistema DEISS:

BR = Bairro  
CH = Chácara  
CR = Condomínio Residencial  
DI = Distrito Industrial  
DM = Desmembramento  
JD = Jardim  
LT = Loteamento  
NR = Núcleo Residencial   
PQ = Parque  
VL = Vila

330

379

50

C

N

Bairro \(referente ao endereço do Tomador\)\.

380

381

02

C

S

Tipo Logradouro \(referente ao endereço do Tomador\), conforme o sistema DEISS:

AL = Alameda  
AV = Avenida  
CA = Caminho  
ET = Estrada  
PC = Praça  
R = Rua  
RD = Rodovia  
TV = Travessa  
VI = Vila  
LG = Lugarejo

382

431

50

C

S

Logradouro \(referente ao endereço do Tomador\)\.

432

437

06

N

N

Número \(referente ao endereço do Tomador\), informe 000000 para sem numeração\.

438

445

08

N

N

CEP \(referente ao endereço do Tomador\)\.

446

495

50

C

N

Complemento \(referente ao endereço do Tomador\)\.

496

505

10

N

N

Telefone do Tomador, os dois primeiros números são o DDD\.

506

565

60

C

N

E\-mail do Tomador\.

566

819

254

C

N

Texto de Observações\.

820

833

14

N

N

INSS \(campo de responsabilidade do prestador, não será calculado pelo sistema\)\.

834

847

14

N

N

IR \(campo de responsabilidade do prestador, não será calculado pelo sistema\)\.

848

861

14

N

N

CSLL \(campo de responsabilidade do prestador, não será calculado pelo sistema\)\.

862

875

14

N

N

COFINS \(campo de responsabilidade do prestador, não será calculado pelo sistema\)\.

876

889

14

N

N

PIS \(campo de responsabilidade do prestador, não será calculado pelo sistema\)\.

890

903

14

N

N

Outras Retenções \(campo de responsabilidade do prestador, não será calculado pelo sistema\)\.

904

917

14

N

N

ISS retido no tomador \(campo de responsabilidade do prestador, não será calculado pelo sistema\)\.

918

925

08

N

N

Número da NFS\-e substituída, nos casos de substituição de Notas Fiscais, a nota fiscal substituída será automaticamente cancelada\. 

926

934

09

N

S

Número do Recibo Provisório \(RPS\), __o número deve ser sequencial e único para cada registro__\. Exemplos: 000000001, 000000002, 000000003\. Quanto ao cancelamento do RPS, a NFS\-e gerada deve ser cancelada diretamente no sistema DEISS\. Quanto à substituição de RPS, o número da NFS\-e gerada pelo RPS substituído deve ser mencionado no campo __NFS\-e substituída__ e o RPS substituto deve mencionar o número do RPS substituído no campo de observações\. 

935

2934

2000

T

S

Texto contínuo de descrição dos serviços, o tamanho desse campo pode ser variável\. Quebras de linha devem ser indicadas pelo caractere | \(*pipe* ou barra vertical, ASCII 124\), desde que não exceda o máximo de 2000 caracteres \(sem quebra de linha\) ou 20 quebras de linhas com no máximo 90 caracteres de largura cada linha\. 

__Observação__: Para empresas no exterior, indicadas com 99999999999999 no campo CPF ou CNPJ, as colunas 276 à 495 serão consideradas uma única coluna para endereço, com tamanho de 220 caracteres\.

__Leiaute do Arquivo de Retorno Gerado pelo Sistema DEISS__

__Col ini__

__Col fin__

__Tam__

__Tp__

__Ob__

__Descrição__

01

09

09

N

S

CCM \(Inscrição Municipal\) do __Contribuinte__, exemplo: 001214113

10

15

06

N

S

Competência da emissão da nota fiscal \(aaaamm\), exemplo: 200901

16

23

08

N

S

Número da Nota Fiscal\.

24

38

15

D

S

Data e hora de emissão \(aaaammdd hhmmss\)\. Exemplo: 20090301 120000 

39

47

09

C

S

Chave de verificação\.

48

55

08

D

S

Data do RPS \(aaaammdd\), exemplo: 20090101

56

61

06

N

S

Código do serviço prestado exemplos: 001405, 000702, 000705

62

75

14

N

S

Valor total do serviço, sem pontuação \(no caso de nota conjugada informar apenas o valor do serviço\)\. Exemplos: 00000000005323 = R$ 53,23; 00000000000100 = R$ 1,00\.

76

89

14

N

N

Valor total de deduções \(apenas para as atividades previstas no Art\. 11 do Decreto N\.º 10\.502 de 04 de dezembro de 2009\)\. Para as atividades 702 e 705, a empresa deverá obrigatoriamente, no prazo de 30 dias, apresentar ao Fisco Municipal, as 1ªs vias das notas fiscais de materiais abatidos\.

90

103

14

N

S

Valor Imposto \(valor do ISSQN em Indaiatuba\)\.

104

104

01

C

S

Retenção \(I' para Isento, 'O' para não tributado no município de Indaiatuba, 'S' para Simples nacional e 'T' para Tributado\)\.

105

105

01

C

S

Situação \('C' de Cancelada e' N' Normal\.

106

155

50

C

S

Município onde foi realizado o serviço, nome sem abreviações, conforme descrito no IBGE\. 

156

157

02

C

S

UF onde realizado o serviço\.

158

158

01

C

S

Pessoa Física ou Jurídica \(F ou J\)\.

159

208

50

C

N

País de origem do tomador\. 

209

222

14

N

S

CPF ou CNPJ do __Tomador__ \(sempre em quatorze casas preenchendo com zeros à esquerda\)\. Exemplos: 44733608000109, 00733608000109, 00012345678910, __99999999999999 __para empresas no exterior e__ 00099999999999__ para identificar pessoa física no caso de regime especial de tributação\. 

223

322

100

C

S

Razão Social do Tomador, nome completo da empresa, nomes com mais de 100 caracteres poderão ser abreviados\.

323

372

50

C

S

Município \(referente ao endereço do Tomador\), nome sem abreviações, conforme descrito no IBGE\.

373

374

02

C

S

UF \(referente ao endereço do Tomador\)\.

375

376

02

C

N

Tipo do bairro \(referente ao endereço do Tomador\), conforme o sistema DEISS:

BR = Bairro  
CH = Chácara  
CR = Condomínio Residencial  
DI = Distrito Industrial  
DM = Desmembramento  
JD = Jardim  
LT = Loteamento  
NR = Núcleo Residencial   
PQ = Parque  
VL = Vila

377

426

50

C

N

Bairro \(referente ao endereço do Tomador\)\.

427

428

02

C

S

Tipo Logradouro \(referente ao endereço do Tomador\), conforme o sistema DEISS:

AL = Alameda  
AV = Avenida  
CA = Caminho  
ET = Estrada  
PC = Praça  
R = Rua  
RD = Rodovia  
TV = Travessa  
VI = Vila  
LG = Lugarejo

429

478

50

C

S

Logradouro \(referente ao endereço do Tomador\)

479

484

06

N

N

Número \(referente ao endereço do Tomador\), 000000 para sem numeração\.

485

492

08

N

N

CEP \(referente ao endereço do Tomador\)\.

493

542

50

C

N

Complemento \(referente ao endereço do Tomador\)\.

543

552

10

N

N

Telefone do Tomador, os dois primeiros números são o DDD\.

553

612

60

C

N

E\-mail do Tomador\.

613

866

254

C

N

Texto de Observações\.

867

880

14

N

N

INSS \(campo de responsabilidade do prestador, não será calculado pelo sistema\)

881

894

14

N

N

IR \(campo de responsabilidade do prestador, não será calculado pelo sistema\)\.

895

908

14

N

N

CSLL \(campo de responsabilidade do prestador, não será calculado pelo sistema\)\.

909

922

14

N

N

COFINS \(campo de responsabilidade do prestador, não será calculado pelo sistema\)\.

923

936

14

N

N

PIS \(campo de responsabilidade do prestador, não será calculado pelo sistema\)\.

937

950

14

N

N

Outras Retenções \(campo de responsabilidade do prestador, não será calculado pelo sistema\)\.

951

964

14

N

N

ISS retido no tomador \(campo de responsabilidade do prestador, não será calculado pelo sistema\)\.

965

972

08

N

N

Número da NFS\-e substituída\.

973

981

09

N

N

Número do Recibo Provisório \(RPS\)\.

982

2981

2000

T

S

Descrição do serviço, o tamanho desse campo será variável se a descrição for menor que 2000 caracteres\. Quebras de linha serão indicadas pelo caractere | \(*pipe* ou barra vertical, ASCII 124\)\.

__Observação__: Para empresas no exterior, indicadas com 99999999999999 no campo CPF ou CNPJ, as colunas 323 à 542 serão consideradas uma única coluna para endereço, com tamanho de 220 caracteres\.

__Legenda__

__Informação__

__Identificação da Informação__

__Col ini__

Coluna inicial

Número da coluna do primeiro caractere do campo

__Col fin__

Coluna final

Número da coluna do último caractere do campo

__Tam__

Tamanho

Quantidade de caracteres fixa

__Tp__

Tipo

C – caracteres \(preencher com espaços em branco a direita até completar o tamanho do campo\), em campos não obrigatórios preencher com espaços\.

D – Data \(as datas deverão ser informadas no formato aaaammdd ano, mês e dia\)

N – numérico \(preencher com zeros a esquerda até completar o tamanho do campo, os dois últimos campos serão considerados como casas decimais\), em campos não obrigatórios preencher com zeros\. Os caracteres de formatação \(máscaras\) devem ser removidos\. 

T – texto \(não serão aceitos caracteres de quebra de linha ou de tabulação\), tamanho mínimo 01 \(um\) caractere, tamanho máximo 2000 \(dois mil\) caracteres

__Ob__

Obrigatório

Obrigatoriedade de preenchimento \(Quando o tomador é estrangeiro não é obrigatório informar o endereço\)

__Descrição__

Breve descrição da informação que deverá conter o campo

