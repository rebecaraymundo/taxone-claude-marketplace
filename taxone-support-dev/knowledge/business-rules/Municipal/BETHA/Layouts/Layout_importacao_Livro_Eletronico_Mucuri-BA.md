# Layout importacao_Livro Eletronico_Mucuri-BA

- **Fonte:** Layout importacao_Livro Eletronico_Mucuri-BA.docx
- **Modificado:** 2021-07-27
- **Tamanho:** 39 KB

---

## Layout do arquivo para importação de declarações

Um arquivo\-texto para importação de declarações normalmente é gerado por sistemas comerciais de escrita fiscal\. A razão principal de se utilizar esse tipo de arquivo é evitar que documentos fiscais sejam redigidos, resguardando\-se de possíveis erros\.

Encontra\-se, abaixo, o detalhamento do arquivo\-texto que deve ser confeccionado para a importação das declarações de serviços\.

__Coluna__

__Tamanho__

__Início__

__Fim__

__Descrição__

__Tipo__

__Permite nulo__

__Validação__

__Prefeitura__

identificador

1

1

1

Identificador "0"

Numérico \(0\)

Não

0 \- CNPJ da Prefeitura\. Este registro é obrigatório apenas para arquivos que serão validados sem que o usuário efetue login\.

CNPJ

14

2

15

CNPJ da Prefeitura

Alfanumérico \(14 caracteres\)

Não

CNPJ da Prefeitura

Versão do arquivo

3

16

18

Versão do arquivo que está sendo importado\.

Numérico \(3\)

Não

Versão do arquivo que está sendo importado\. Deve ser informado '001' para este campo\.

__Declaração__

identificador

1

1

1

Identificador "1"

Numérico \(1\)

Sim

1\-Declaração

tipo

1

2

2

Deve constar "P" ou "T" \(prestador ou tomador\)\.

Alfa \(P ou T\)

Não \*

P\-Prestador e T\-Tomador

codificação de cidades

1

3

3

Deve constar "1" ou "2"\.

Numérico \(1 ou 2\)\.

Sim

1\-IBGE e 2\-SIAFI/SIPREV

inscrição

14

4

17

CPF ou CNPJ válido do prestador/tomador do serviço\.

Alfanumérico \(14 caracteres\)

Sim

CPF\-11 caracteres ou CNPJ\-14 caracteres\. Informe\-se apenas números, sem nenhum separador no caso de CPF ou CNPJ\. Caso o limite de caracteres não seja alcançado, complete com espaços em branco à direita ou à esquerda\.

nome

50

18

67

Nome do prestador/tomador do serviço\.

Alfanumérico

Sim

Nome completo do prestador/tomador do serviço\.

data inicial

8

68

75

Data inicial da competência que está sendo declarada\.

Data DDMMAAAA

Sim

Data DDMMAAAA

data final

8

76

83

Data final da competência que está sendo declarada\.

Data DDMMAAAA

Sim

Data DDMMAAAA

\* Este campo pode ser nulo caso o identificador "1" não estiver informado no arquivo\.

__Documentos__

identificador

1

1

1

Identificador "2"

Numérico \(2\)

Sim

2\-Documentos

inscrição

14

2

15

CPF ou CNPJ válido do prestador/tomador do serviço\.

Alfanumérico \(11 ou 14 caracteres\)\.

Sim

CPF\-11 caracteres, CNPJ\-14 caracteres ou Número do documento\. Informe apenas números, sem nenhum separador no caso de CPF ou CNPJ\. Caso o limite de caracteres não seja alcançado, complete\-se com espaços em branco à direita ou à esquerda\.

nome

50

16

65

Nome do prestador/tomador do serviço\.

Alfanumérico

Sim

Nome completo do prestador/tomador do serviço\.

serie

6

66

71

Nº de série do documento fiscal\.

Alfanumérico

Sim

O nº de série será validado conforme o tipo de declaração e a cidade do prestador/tomador do serviço\.

df\_inicial

9

72

80

Nº inicial do documento fiscal\.

Numérico Inteiro\.

Não \*

Nº inicial do documento fiscal\.

df\_final

9

81

89

Nº final do documento fiscal\.

Numérico Inteiro\.

Sim

Nº final do documento fiscal\.

data\_emissao

8

90

97

Data de emissão do documento fiscal\.

Data DDMMAAAA

Sim

Data DDMMAAAA

tipo

1

98

98

Espécie de documento\.

Alfa \(N, C, R, O ou J\)

Não \*

N\-Nota fiscal, C\-Cupom fiscal, R\-Recibo, O\-Outros ou J \- Nota fiscal conjugada\.

situacao

1

99

99

Situação do documento\.

Alfa \(N, C, A, I, R, S, T, E ou D\)

Não \*

N\-Normal, C\-Cancelada, A\-Anulada, I\-Isenta, R\-Retida, S\-Substituta, T\-Não tributável, E\-Regime especial ou D\-Descontado pela prefeitura\.

valor

15

100

114

Valor do documento\.

Numérico Decimal 2\.

Sim

Valor com duas casas decimais \(sem separadores de milhar e decimal\)\.

localizado

1

115

115

Localização do prestador/tomador\.

Alfa \(D, F ou E\)

Não \*

D\-Dentro do município, F\-Fora do município ou E\-Estrangeiro\.

i\_cidades

7

116

122

Coluna que indica o código da cidade do prestador/tomador do serviço

Numérico Inteiro\.

Não \*

Código nacional da cidade \(IBGE ou SIAFI/SIPREV, conforme identificador "1"\)\. Se a coluna "localizado" for igual a "E", a cidade será nula\.

eh\_optante

1

123

123

Optante pelo simples nacional "S" ou "N"\.

Alfa \(S ou N\)

Sim

S – Sim, optante pelo simples nacional e   
N – Não optante pelo simples nacional\.

motivo\_canc

512

124

635

Descrição do motivo do cancelamento do documento fiscal\.

Alfanumérico

Sim

O motivo do cancelamento poderá ser informado somente quando a situação do documento fiscal estiver definida como C\-Cancelada\.

natureza\_operacao

1

636

637

Código da natureza da operação

Numérico Inteiro

Sim

1 \- Tributação no município  
2 \- Tributação fora do município  
3 \- Isenção  
4 \- Imune  
5 \- Exigibilidade suspensa por decisão judicial  
6 \- Exigibilidade suspensa por procedimento administrativo  
7 \- Não incidência  
8 \- Exportação

\* Estes campos podem ser nulos caso o identificador "2" não estiver informado no arquivo\.

__Serviços__

identificador

1

1

1

Identificador "3"

Numérico \(3\)

Sim

3\-Serviços

i\_cnae/i\_lista\_servicos

7

2

8

Código da atividade CNAE ou código conforme lista de serviços \(Lei 116/2003\)\.

Alfanumérico para i\_cnae e Numérico Inteiro com Ponto Decimal \(\.\) para i\_lista\_servicos\.

Não \*

Código nacional referente ao serviço prestado/tomado \(fixo em 7 caracteres\)\. A atividade pode ser declarada mais de uma vez para um mesmo documento\.

valor\_servico

15

9

23

Valor do serviço

Numérico Decimal 2

Não \*

Valor com duas casas decimais \(sem separadores de milhar e decimal\)\.

i\_cidades

7

24

30

Local onde o serviço foi prestado\.

Numérico Inteiro

Sim

Código nacional da cidade \(IBGE ou SIAFI/SIPREV, conforme identificador "1"\)\. Se a coluna "localizado" for igual a "E", a cidade será nulo\.

aliquota

4

31

34

Valor da alíquota do serviço\.

Numérico decimal 2

Sim

Valor com duas casas decimais  
\(com separadores de decimal\)\.

i\_motivos\_alt\_aliquota

3

35

37

Código do motivo de alteração da alíquota\.

Numérico Inteiro

Sim

Número do motivo de alteração da alíquota cadastrado\. \(Sem separadores de milhar e decimal\)\.

\* Estes campos podem ser nulos caso o identificador "3" não estiver informado no arquivo\.

__Serviços bancários__

identificador

1

1

1

Identificador "4"

Numérico \(4\)

Sim

4\-Serviços

i\_bancos

9

2

10

Código do banco

Numérico Inteiro

Não \*

Código do banco ou da empresa enquadrada como declarante por contas de serviço junto à prefeitura\.

i\_nr\_contas

20

11

30

Nº da conta de serviço\.

Alfanumérico

Não \*

Número da conta de serviço prestado\. \(Caso o número da conta não possua 20 caracteres, deverá ser completado com espaços até que se alcance a quantidade de caracteres reservada para esta coluna\)\.

valor

15

31

45

Valor do serviço

Numérico Decimal 2

Não \*

Valor com duas casas decimais \(sem separadores de milhar e decimal\)\.

recolher

1

46

46

Flag indicando se o serviço deve ser recolhido\.

Alfa \(S ou N\)

Não \*

S\-Para recolher o imposto e N\-Para não recolher o imposto\.

\* Estes campos podem ser nulos caso o identificador "4" não estiver informado no arquivo\.

__Materiais__

Identificador

1

1

1

Identificador "5"

Numérico \(5\)

Sim

5\-Materiais

i\_materiais

7

2

8

Número do material

Numérico Inteiro

Não \*

Código do material cadastrado junto à prefeitura\.

descrição

50

9

58

Descrição do material

Alfanumérico

Não \*

Descrição do material

valor

15

59

73

Valor do material

Numérico Decimal 2

Não \*

Valor com duas casas decimais \(sem separadores de milhar e decimal\)\.

\* Estes campos podem ser nulos caso o identificador "5" não estiver informado no arquivo\.

### Algumas regras devem ser observadas para compor o arquivo de declarações

         O arquivo\-texto suportado pela ferramenta de importação do Livro Eletrônico deve estar conforme o padrão de codificação ANSI\.

         As informações constantes no arquivo de declaração \(1P \- Serviços Prestados e 1T \- Serviços Tomados\) são referentes aos serviços prestados e tomados pelo declarante \(empresa que está importando o arquivo\)\. Nesse caso, quando for gerado um arquivo do tipo 1P, deverão ser listadas as empresas para as quais foram prestados os serviços\. E, quando for gerado um arquivo do tipo 1T, deverão ser listadas as empresas das quais foram tomados os serviços\.

         As linhas do arquivo devem sempre iniciar com os algarismos 1, 2, 3, 4 ou 5\. Essa numeração é utilizada para identificar os tipos de registros a serem gravados, sendo eles observáveis na tabela: 1 \- Declaração, 2 \- Documentos, 3 \- Serviços, 4 \- Serviços bancários e 5 \- Materiais\.

         Os tipos de registro 1, 2 e 3 serão utilizados somente por prestadores/tomadores de serviços comuns\.

         Os tipos de registro 1 e 4 serão utilizados somente por prestadores enquadrados como declarantes por planos de contas\.

         O tipo de registro 5 será utilizado somente por prestadores enquadrados como construtoras, possibilitando a declaração dos materiais\.

         Um arquivo nunca poderá ter tipos de registro 2 e 4 simultaneamente\.

         O limite de caracteres de cada campo deve sempre ser alcançado\. Quando necessário, deve\-se completá\-lo com espaços em branco\.

         Para os campos numéricos, nenhum separador de milhar deve ser apresentado\.

         Nos casos em que somente a declaração dos documentos fiscais seja necessária, o tipo de registro 3 não deve ser apresentado\. Como exemplo, podemos citar os casos de notas fiscais canceladas e anuladas\.

         Para as notas que tiverem apenas valor referente à venda de mercadorias, sem prestação de serviços, deve ser informado apenas o registro 2\. Se existir venda de mercadorias e prestação de serviços, devem ser informados os registros "2" e "3"\.

         Todos os tipos de registros de uma nota devem constar no mesmo arquivo, ou seja, cada conteúdo do documento fiscal deve estar em um único arquivo\.

         O tamanho máximo para upload é de 512 kb\.

### Exemplo de arquivos

__Situação:__

         A EMPRESA DE SERVIÇOS SA \(declarante que está importando o arquivo para o livro\) __PRESTOU__ serviços para as empresas: EMPRESA AAAA S\.A\., EMPRESA BBBB S\.A\. e EMPRESA CCCC S\.A\.

         A EMPRESA DE SERVIÇOS SA \(declarante que está importando o arquivo para o livro\) __TOMOU__ serviços das empresas: EMPRESA XXXX S\.A\., EMPRESA YYYY e EMPRESA ZZZZ\.

Neste caso, deverão ser gerados dois arquivos:

Arquivo dos serviços __PRESTADOS__

                                                                           1P

                                                                           212345678901234EMPRESA AAAA S\.A\.                                                  S1            00000825800000825813012006NN000000000010000D0008607

                                                                           30014120000000000010000

                                                                           265487941321554EMPRESA BBBB S\.A\.                                                  S1            00000825900000825914012006NN000000000200000D0008607

                                                                           30014120000000000200000

                                                                           265324165798796EMPRESA CCCC S\.A\.                                                 S1            00000826000000826014012006NN000000000250000D0008607

                                                                           30014120000000000250000

Arquivo dos serviços __TOMADOS__

                                                                           1T

                                                                           265365426521549EMPRESA XXXX S\.A\.                                                  S1            00000001500000001502012006NN000000000020000D0008607

                                                                           30017140000000000010000

                                                                           298653245146795EMPRESA YYYY S\.A\.                                                  S1            00001234500001234510012006NN000000000025000D0008607

                                                                          30018010000000000200000

                                                                           265249876546535EMPRESA ZZZZ S\.A\.                                                  S1            00000354000000354014012006NN000000000075000D0008607

                                                                           30028010000000000250000

                                                                                          

__Situação:__

         A EMPRESA DE SERVIÇOS SA \(declarante que está importando o arquivo para o livro\) vendeu mercadoria para a empresa EMPRESA AAAA S\.A\. e, além disso, vendeu mercadoria e prestou serviço para a empresa EMPRESA BBBB S\.A\. O exemplo abaixo mostra a declaração das duas notas, ambas conjugadas\.

                                                                           1P

                                                                           212345678901234EMPRESA AAAA S\.A\.                                                                                                                S1              00000825800000825813012006JN000000000010000D0008607

                                                                           265487941321554EMPRESA BBBB S\.A\.                                                                                                                S1              00000825900000825914012006JN000000000300000D0008607

                                                                           30014120000000000200000

