# MTZ_EFD_Pre_Geracao_Registro_1400_MG

- **Fonte:** MTZ_EFD_Pre_Geracao_Registro_1400_MG.docx
- **Modificado:** 2026-01-19
- **Tamanho:** 92 KB

---

THOMSON REUTERS

                                                                                     __Módulo Sped Fiscal__

__  __

__Pré\-Geração do Registro 1400 \(MG – Minas Gerais\)__

__Localização__: Menu Sped, EFD \- Escrituração Fiscal Digital, item Pré\-Geração à Registro 1400 – Periodicidade Anual/Específico por UF – __\(Campo UF = MG – Minas Gerais\)__

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS4728\-A

Atendimento à Resolução 4\.730, de 17/12/14, SEF\-MG

Criação do processo de pré\-geração para o registro 1400 de MG para os códigos referentes às operações de todo exercício\. 

27/03/2015

\(criação do docto\)

MFS3248

Lara Aline

Ajuste na tela de pré\-geração para que possa atender todas as UF que possuem geração específica anual para o Registro 1400\.

09/11/2016

MFS24921

Andréa Rocha

Inclusão do modelo 67\.

28/02/2019

MFS25904

Tratamento dos Itens de Desconto da SAFX43

 Alteração na totalização das notas para efetuar a dedução do valor do Desconto dos itens de dedução \(ver __RN04__, totalização das notas da SAFX42/SAFX43\)\.

30/06/2020

MFS60170

Tratamento – Inclução de filtro de geração e mensagem\.

Alteração na geração do registro __1400__ – Geração Específica para UF = MG

Tratamento na geração do registro 1400, item “__3\.5 \- __<a id="_Hlk68106826"></a>__Prestação de Serviço de Transporte Rodoviário”__

05/04/2021

MFS73848

Aline Melo

Inclusão de subitem no processo de pré\-geração do código 3\.6 Outras Entradas a Detalhar por Município, para a geração automática do 1400\.

04/11/2021

MFS80785

Andréa Rocha

Inclusão do modelo 55 na pré\-geração do item 3\.6\.9 \(Saídas de mercadorias de estabelecimento de mesmo titular\)\.

14/02/2022

MFS86206

Aline Melo

Inclusão de subitem 3\.6\.8 no processo de pré\-geração do código 3\.6 Outras Entradas a Detalhar por Município, para a geração automática do 1400\.

17/06/2022

MFS699904

Andréa Rocha

Inclusão do modelo 66 na pré\-geração do código 3\.6 \- Outras Entradas a Detalhar por Município, para a geração automática do 1400\.

30/10/2024

MFS672643

Liliane Assaf

__RN04__:Alteração na geração do código 3\.6 – “Outras Entradas a Detalhar por Município”::

1. Incluir recuperação das notas de modelo 62 \(NFCOM\) referentes ao subtópico __3\.6\.7 –__ Atividades de Prestação de Serviços de Comunicação/Telecomunicação \(__RN04\.02__\)\.
2. Passar a gerar o subtópico “__3\.6\.14__ \- Outras Hipóteses em que Haja Necessidade de Atribuição de VAF a mais de um Município” \(__RN04\.03__\)

17/01/2025

	

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

Esta geração foi criada na OS4728\-A, com objetivo de fazer a geração dos dados de registro 1400 para MG\. Essa geração é especifica para os itens da Resolução 4\.730/2014 \(SEF\-MG\) cuja entrega é apenas no arquivo de DEZ, e os valores são referentes às operações de todo exercício\.

__\[MFS73848\]__ Conforme Resolução Nº 5\.369 DE 22 DE MAIO DE 2020 \(SEF\-MG\), incluir o tratamento do item __3\.6\.9__ no processo de geração automática, em atendimento ao código “Outras Entradas a Detalhar por Município”\.

\[__MFS672643\]: __Inclusão do tratamento para o item__ 3\.6\.14\.__

Os itens gerados são os seguintes:

     \- Prestação de Serviço de Transporte Rodoviário  \(item __3\.5__ da Resolução\) – *Válido neste menu de Pré\-Geração até 31/12/2020\.*

     \- Outras Entradas a Detalhar por Município            \(item __3\.6__ da Resolução\)

Quanto ao item “__Outras Entradas a Detalhar por Município__” a geração automática irá considerar apenas as operações referentes aos subitens descritos abaixo\. Os demais subitens do item 3\.6 não terão geração automática, e para informar seus valores, o usuário poderá utilizar a tela manutenção do registro 1400 \(campo “Valores Informados”\)\.   

- 3\.6\.2 \- Atividades de Prestação de Transporte Aéreo de Carga                                                                                                                                           \(vide RN04\.01\)
- 3\.6\.3 \- Atividades de Prestação de Serviço de Transporte Ferroviário/Aquaviário                                                                                                               \(vide RN04\.01\)
- 3\.6\.7 \- Atividades de Prestação de Serviços de Comunicação/Telecomunicação                                                                                                                \(vide RN04\.02\)
- 3\.6\.8 \- Atividade de fornecimento de refeição industrial para município distinto ao da localização do contribuinte                                                              \(vide RN04\.03\) \[__MFS86206__\]
- 3\.6\.9 \- Saídas de mercadorias de estabelecimento de mesmo titular localizado em município diverso daquele onde ocorreu a efetiva comercialização \(vide RN04\.03\) \[__MFS73848__\]
- 3\.6\.11 \- Atividades de Geração de Energia                                                                                                                                                                            \(vide RN04\.02\)
- 3\.6\.12 \- Atividades de Distribuição de Energia Elétrica                                                                                                                                                          \(vide RN04\.02\)
- 3\.6\.13 \- Atividades de Transmissão de Energia Elétrica                                                                                                                                                        \(vide RN04\.02\)
- 3\.6\.14 \- Outras Hipóteses em que Haja Necessidade de Atribuição de VAF a mais de um Município                                                                                  \(vide RN04\.03\) \[__MFS672643\]__

Os dados apurados serão armazenados e utilizados posteriormente para gravação do registro 1400 na geração do Sped Fiscal\.

__RN01__

__                                                        Parâmetros da Geração__

__Ano Base__ – Neste campo o usuário informará o ano base das operações a serem totalizadas\.

__Geração p/Inscrição Estadual Única – __Este campo apresenta duas opções: “Sim” e “Não” \(seguindo o padrão da tela de geração do Sped\)\.

Default: opção “Não”

__Estabelecimentos__ – Neste campo serão disponibilizados os estabelecimentos para seleção do usuário, de acordo com os seguintes critérios:

     \- Somente estabelecimentos da empresa do login;

     \- Somente estabelecimentos da UF de MG;

     \- Se parâmetro “Geração por inscrição estadual única” = “Sim”:

        Nesse caso, serão demonstrados *apenas* os estabelecimentos centralizadores de I\.E\.U\., de acordo com a parametrização do

        módulo de Controle das Obrigações Estaduais \(menu “*Obrigações à Empresas/Estabelecimentos com Inscrição Estadual Única*”\);

     \- Se parâmetro “Geração por inscrição estadual única” = “Não”

        Nesse caso, serão demonstrados *todos* os estabelecimentos que atendam aos demais critérios;

__\[ALTERAÇÃO MFS3248\]__

Regras de tela verificar novo documento matriz: MTZ\_EFD\_Tela\_Pre\-Geracao\_Registro\_1400\_UF\.docx

__RN02__

__                                                    Recuperação dos Dados__

A geração é feita separadamente para cada um dos dois itens a serem apurados \(conforme __RN00__\), da seguinte forma:

__Prestação de Serviço de Transporte Rodoviário__:

Neste caso a apuração é feita a partir dos documentos de transporte rodoviário da SAFX07\.

__Obs\.:__ A partir do período de 2021 o cálculo para este item deverá ser gerado __mensalmente__, \(de acordo com a Resolução 5\.369 de 22 de maio de 2020 – Subitem 3\.4\.2\), e será gerado no registro 1400 diretamente pelo menu de Geração > Meio Magnético\.

__Outras Entradas a Detalhar por Município:__

Neste caso, a apuração envolve vários segmentos: 

\- Outros tipos de Transportes \(Aéreo, Ferroviário e Aquaviário\);

\- Energia Elétrica;

\- Comunicação / Telecomunicação; 

Desta forma, a apuração é feita a partir dos documentos de transporte da SAFX07, e para os demais casos, da SAFX42/SAFX43\. Nos dois casos, também serão consideradas as operações de entrada \(deduções\) parametrizadas\. 

\- Comercialização Produto/Mercadoria \[MFS73848\]

\- Fornecimento de Refeição Industrial \[MFS86206\]

Para os dois itens acima, a apuração é feita a partir dos documentos de produto/mercadoria da SAFX07 e SAFX08\. Também serão consideradas as operações de entrada \(deduções\) parametrizadas\.

O total geral para o item “*Outras Entradas a Detalhar por Município*” será o total apurado para os segmentos: transportes, energia elétrica, comunicação/telecomunicação, comercialização produto/mercadoria e fornecimento de refeições\.

Os detalhes do processamento referente a cada um destes dois itens, e também sobre a gravação dos dados apurados, foram descritos separadamente, nas seguintes regras:

__RN03__

__Prestação de Serviço de Transporte Rodoviário__

__RN04__

__Outras Entradas a Detalhar por Município__

__RN05__

__Gravação dos Dados__

__RN03__

__                                       Prestação de Serviço de Transporte Rodoviário__

O cálculo para este item é feito de acordo com o “Manual de Orientação para Preenchimento e Entrega da Declaração Anual do Movimento Econômico e Fiscal \(DAMEF\)”, conforme orientação que consta no item 3\.5\.1 da Resolução 4\.730/2013, SEF\-MG \(ver detalhes no help do programa da VAF\-MG, vrs 7\.07\.06, opção “Documentos”, help da aba VAF\)\.

Será totalizado o valor das saídas por município de origem, e aplicada a forma de cálculo descrita no programa DAMEF/VAF, conforme as regras descritas a seguir\.

__Obs\.:__ À partir do período de 2021 o cálculo para este item deverá ser gerado no registro 1400 __mensalmente__, \(de acordo com a Resolução 5\.369 de 22 de maio de 2020 – Subitem 3\.4\.2\), e será gerado diretamente pelo menu de Geração do Meio Magnético\.

__Origem dos dados__ àTabelas dos Documentos Fiscais – Capa e Itens de Mercadoria  \(SAFX07 e SAFX08\)

__Critérios para recuperação dos documentos de transporte na SAFX07/SAFX08:__

\- Empresa – empresa do login

\- Estabelecimento – estabelecimento da geração

  No caso de geração por I\.E\.U\. serão considerados os documentos de todos os estabelecimentos envolvidos na centralização,

  \(centralizador e centralizados\), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle

  das Obrigações Estaduais;

\- Classificação = 1 ou 4 \(a NF de modelo 07 usa classificação 1 e os CTRC’s usam classificação 4\)	

                                      \(modelo 07 é nota fiscal de transporte rodoviário de carga\)

\- Data Fiscal \(ou data extemporânea\) – deve ser uma data cujo ano seja = ano base informado em tela

\- Modelo \(campo 13\) – somente modelos de transporte rodoviário ou multimodal \(07, 08, 8B, 26, 57, 67\) 

Observar que no caso do modelo do CTe \(57\), não é possível identificar qual é o tipo de transporte, pois esse modelo de conhecimento eletrônico pode ser utilizado para qualquer tipo de transporte\. Outro detalhe é que o CFOP não serve para identificar o tipo de transporte, pois são os mesmos para todos os tipos \(aéreo, rodoviário, etc\.\.\.\)\. Assim, a geração considera o modelo 57 para os dois códigos de MG, e caberá ao cliente que utilizar modelo 57, identificar o tipo de transporte através da natureza de operação\.

\- Somente notas de saída \(MOVTO\_E\_S = ‘9’\)

\- Situação \- somente as notas não canceladas

\- O campo “117\-UF de Origem” da SAFX07 deve ser “MG”;

\- O campo “182\-Município de Origem” da SAFX07 deve estar preenchido;

\- Somente notas com  CFOP ou CFOP/Natureza parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à CFOP

   ou CFOP/Natureza de Operação”, para a operação = “__Prestacao\_de\_Servico\_de\_Transporte\_Rodoviario__” da UF = MG;

\- Notas com ou sem itens na SAFX08; 

\- No caso das notas com itens, será utilizado o CFOP ou CFOP/Natureza do item, e para as notas sem itens, utiliza os da capa;

\- Valor a ser totalizado à valor contábil do item \(SAFX08\), ou valor total da nota \(SAFX07\) para as notas sem itens;

__Processamento das notas:__

As notas serão agrupadas __*por município de origem*__, e __*para cada município*__ será apurado o total das saídas\. O resultado final será calculado da seguinte forma:

  

     A =  Total das notas de saída

     B =  20% do valor de A

     C = A – B

  

Para cada município apurado, será gravado o resultado final, que corresponde ao valor “C” representado no quadro acima\.

As regras para gravação dos dados estão descritas na __RN05__\.

\[__MFS60170__\] Incluir bloqueio para gerar somente até 31/12/2020, e Incluir Mensagem no Log de geração\.

 

A partir do período de 2021 o cálculo para este item deverá ser gerado __mensalmente__, \(de acordo com a Resolução 5\.369 de 22 de maio de 2020 – Subitem 3\.4\.2\), e será gerado no registro 1400 diretamente pelo menu de Geração > Meio Magnético\.

\- Data Fiscal \(ou data extemporânea\) – deve ser uma data cujo ano seja = ano base informado em tela

      \-Bloquear a data em 31/12/2020\.

Caso a data de Geração seja após 31/12/2020 gravar mensagem no Log de Geração:

Item 3\.5 – Transporte Rodoviário à será gravada uma mensagem no log com a seguinte descrição: “A partir de 2021 esse item deverá ser gerado mensalmente na geração do arquivo Meio Magnético, de acordo com a Resolução 5\.369 de 22 de maio de 2020\.

__RN04__

__                                           Outras Entradas a Detalhar por Município__

Para este item será feita a totalização das saídas e também das entradas \(parametrizadas como dedução\), __por município de origem ou do ponto de consumo/terminal faturado \(no caso das utilities\)__, conforme as regras descritas a seguir\.

__  __

__Origem dos dados__ àComo este item engloba tanto o segmento de transportes \(exceto rodoviário\), como energia elétrica e telecom, a totalização das operações tem duas origens:

      \- Tabelas dos Documentos Fiscais – Capa e Itens de Mercadoria  \(SAFX07, SAFX08 e SAFX09\)

      \- Tabelas dos Documentos Fiscais de Utilities – Capa e Itens \(SAFX42 e SAFX43\)

*\(a SAFX09 é utilizada apenas na totalização das entradas a serem deduzidas, quando for o caso\)*

__RN04\.01 Critérios para recuperação dos documentos de transporte na SAFX07/SAFX08:__

Atendimento aos subtópicos:

- 3\.6\.2 \- Atividades de Prestação de Transporte Aéreo de Carga
- 3\.6\.3 \- Atividades de Prestação de Serviço de Transporte Ferroviário/Aquaviário

__Critérios de Recuperação:__

\- Empresa – empresa do login

\- Estabelecimento – estabelecimento da geração

  No caso de geração por I\.E\.U\. serão considerados os documentos de todos os estabelecimentos envolvidos na centralização,

  \(centralizador e centralizados\), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle

  das Obrigações Estaduais;

\- Classificação = 1 ou 4 \(a NF de modelo 27 usa classificação 1 e os CTRC’s usam classificação 4\)	

                                      \(modelo 27 é nota fiscal de transporte ferroviário de carga\)

\- Data Fiscal \(ou data extemporânea\) – deve ser uma data cujo ano seja = ano base informado em tela

\- Modelo \(campo 13\) – somente modelos de transporte rodoviário ou multimodal \(09, 10, 11, 26, 27, 57, 67\) 

Observar que no caso do modelo do CTe \(57\), não é possível identificar qual é o tipo de transporte, pois esse modelo de conhecimento eletrônico pode ser utilizado para qualquer tipo de transporte\. Outro detalhe é que o CFOP não serve para identificar o tipo de transporte, pois são os mesmos para todos os tipos \(aéreo, rodoviário, etc\.\.\.\)\. Assim, a geração considera o modelo 57 para os dois códigos de MG, e caberá ao cliente que utilizar modelo 57, identificar o tipo de transporte através da natureza de operação\.

\- Somente notas de saída \(MOVTO\_E\_S = ‘9’\)

\- Situação \- somente as notas não canceladas

\- O campo “117\-UF de Origem” da SAFX07 deve ser “MG”;

\- O campo “182\-Município de Origem” da SAFX07 deve estar preenchido;

\- Somente notas com  CFOP ou CFOP/Natureza parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à CFOP

   ou CFOP/Natureza de Operação”, para a operação = “__Outras\_Entradas\_a\_Detalhar\_Por\_Municipio__” da UF = MG;

\- Notas com ou sem itens na SAFX08; 

\- No caso das notas com itens, será utilizado o CFOP ou CFOP/Natureza do item, e para as notas sem itens, utiliza os da capa;

\- Valor a ser totalizado à valor contábil do item \(SAFX08\), ou valor total da nota \(SAFX07\) para as notas sem itens;

__RN04\.02 Critérios para recuperação dos documentos de utilities na SAFX42/SAFX43:__

Atendimento aos subtópicos:

- 3\.6\.7 \- Atividades de Prestação de Serviços de Comunicação/Telecomunicação
- 3\.6\.11 \- Atividades de Geração de Energia
- 3\.6\.12 \- Atividades de Distribuição de Energia Elétrica
- 3\.6\.13 \- Atividades de Transmissão de Energia Elétrica

__\[MFS699904\] __Inclusão do modelo 66 na pré\-geração do código 3\.6 \- Outras Entradas a Detalhar

__\[MFS67643\] __Inclusão da recuperação da notas fiscais de modelo 62

__Critérios de Recuperação:__

\- Empresa – empresa do login

\- Estabelecimento – estabelecimento da geração

  No caso de geração por I\.E\.U\. serão considerados os documentos de todos os estabelecimentos envolvidos na centralização,

  \(centralizador e centralizados\), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle

  das Obrigações Estaduais;

\- Data Fiscal \(ou data extemporânea\) – deve ser uma data cujo ano seja = ano base informado em tela

\- Modelo \(campo 13\) – somente 06, 21, 22,__ 62__ e 66 \(EE e Telecom\) 

\- Situação \- somente as notas não canceladas

\- O campo “75\-UF do Ponto de Consumo/Terminal Faturado” da SAFX42 deve ser “MG”;

\- O campo “76\-Município do Ponto de Consumo” da SAFX42 deve estar preenchido;

\- Os itens informativos *não* serão considerados \(campo “10\-Tipo de Item” da SAFX43 = “1”\);

\- Somente notas com  CFOP ou CFOP/Natureza parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à CFOP

   ou CFOP/Natureza de Operação”, para a operação = “__Outras\_Entradas\_a\_Detalhar\_Por\_Municipio__” da UF = MG;

\- Como os documentos da 42/43 sempre têm itens, será utilizado o CFOP ou CFOP/Natureza do item;

\- Valor a ser totalizado à campo “19\-Valor do Serviço” do item \(SAFX43\);

\- Valor a ser totalizado = Se item de adição, soma o __valor do serviço__ \(campo 19 SAFX43\),

                                        Se item de dedução, subtrai o __valor do desconto__ \(campo 18 da SAFX43\); 

                                        *\(ao subtrair o valor do desconto, considerar sempre o valor absoluto\)*

\(Itens de __adição__ são os itens com o campo “20\-Adição/Desconto” __nulo__ ou = “__A__”\);

\(Itens de __dedução__ são os itens com o campo “20\-Adição/Desconto” = “__D__”\);

__MFS25904__: A totalização das notas recuperadas passou a ser feita da seguinte forma: deve somar o Valor do Serviço dos itens de adição, e subtrair o Valor do Desconto dos itens de dedução, conforme a regra acima\.

Exemplo: supondo as notas abaixo para um mesmo município do ponto de Consumo:

   Nota 101: Item 1, Adição/ Desc\. = “__A__”, Valor do Serviço = 1\.000,00

                    Item 2, Adição/ Desc\. = “__A__”, Valor do Serviço = 500,00

   Nota 102: Item 1, Adição/ Desc\. = “__A__”, Valor do Serviço = 2\.000,00

                    Item 2, Adição/ Desc\. = “__D__”, Valor do Desconto = 300,00

   Valor totalizado = __3\.200,00__ \(1\.000,00 \+ 500,00 \+ 2\.000,00 – 300,00\)

__\[__<a id="_Hlk106354130"></a>__MFS73848\]__

<a id="_Hlk106353453"></a>__RN04\.03 Critérios para recuperação dos documentos de entrada e saída de mercadorias na SAFX07/SAFX08:__

Atendimento aos subtópicos:

- 3\.6\.8 \- Atividade de fornecimento de refeição industrial para município distinto ao da localização do contribuinte
- 3\.6\.9 \- Saídas de mercadorias de estabelecimento de mesmo titular localizado em município diverso daquele onde ocorreu a efetiva comercialização
- 3\.6\.14 \- Outras Hipóteses em que Haja Necessidade de Atribuição de VAF a mais de um Município \[__MFS672643\]__

__\[MFS80785\] __Inclusão da recuperação da notas fiscais de modelo 55

__\[MFS67643\]__ incluir a recuperação das notas fiscais em atendimento ao subtópico __3\.6\.14__\. Para isso considerar notas com CFOP ou CFOP/Natureza parametrizados para a operação “Outras Entradas a Detalhar por Municipio \(especifico para 3\.6\.14\)” \(COD\_PARAM 895\) e com município origem preenchido \(igual ou diferente do município do estabelecimento\)\.

As notas fiscais recuperadas para atendimento aos subtópicos __3\.6\.8 __e__ 3\.6\.9 __possuem CFOP ou CFOP/Natureza parametrizados para a operação “Outras Entradas a Detalhar por Municipio” \(COD\_PARAM = 635\) e com município origem preenchido e diferente do município do estabelecimento\)\. 

__Orientações: __

As notas de saída devem ser recuperadas nessa regra\.

As notas de entrada devem ser recuperadas na regra de dedução\.

__Critérios de Recuperação:__

\- Empresa – empresa do login

\- Estabelecimento – estabelecimento da geração

\- Data Fiscal \(ou data extemporânea\) – deve ser uma data cujo ano seja = ano base informado em tela

\- Somente notas de saída \(MOVTO\_E\_S = ‘9’\)

\- Modelo \(campo13\-MODELO da SAFX07\) igual a 01, 1B, 04, 55 ou 65;

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3;

\- Situação \- somente as notas não canceladas;

\- O campo “117\-UF de Origem” da SAFX07 deve ser “MG”;

\- O campo “182\-Município de Origem” da SAFX07 deve estar preenchido;

\- Para os subtópicos __3\.6\.8__ e __3\.6\.9__ devem ser aplicados os dois critérios a seguir:

  \- CFOP ou CFOP/Natureza da nota parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à CFOP ou CFOP/Natureza de Operação“ para a operação = “__Outras\_Entradas\_a\_Detalhar\_Por\_Municipio__” da UF = MG \(COD\_PARAM = 635\); e

  \- Campo “182\-Município de Origem” da SAFX07 <> campo COD\_MUNICIPIO da tabela ESTABELECIMENTO 

Para o subtópico __3\.6\.14__ devem ser aplicados os dois critérios a seguir:

\- CFOP ou CFOP/Natureza da nota parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à CFOP ou CFOP/Natureza de Operação”, para a operação = “__Outras\_Entradas\_a\_Detalhar\_Por\_Municipio \(especifico para 3\.6\.14\)__” da UF = MG \(COD\_PARAM 895\); e

\- Campo “182\-Município de Origem” da SAFX07 preenchido

\- Notas com ou sem itens na SAFX08; 

\- No caso das notas com itens, será utilizado o CFOP ou CFOP/Natureza do item, e para as notas sem itens, utiliza os da capa;

\- Valor a ser totalizado à valor contábil do item \(SAFX08\), ou valor total da nota \(SAFX07\) para as notas sem itens;

<a id="_Hlk106353501"></a>__RN04\.04 Critérios para recuperação das entradas \(deduções\) na SAFX07/SAFX08/SAFX09:__

__\[MFS67643\]__ incluir a recuperação das notas fiscais de dedução em atendimento ao subtópico __3\.6\.14__\. Para isso considerar notas com CFOP ou CFOP/Natureza parametrizados para a operação “Outras Entradas a Detalhar por Municipio \(especifico para 3\.6\.14\)” \(COD\_PARAM 896\) e com município origem preenchido \(igual ou diferente do município do estabelecimento\)\.

As notas fiscais de dedução recuperadas para atendimento aos subtópicos __3\.6\.8 __e__ 3\.6\.9 __possuem CFOP ou CFOP/Natureza parametrizados para a operação “Outras Entradas a Detalhar por Municipio” \(COD\_PARAM = 636\) e com município origem preenchido e diferente do município do estabelecimento\)\. 

\- Empresa – empresa do login

\- Estabelecimento – estabelecimento da geração

  No caso de geração por I\.E\.U\. serão considerados os documentos de todos os estabelecimentos envolvidos na centralização,

  \(centralizador e centralizados\), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle

  das Obrigações Estaduais;

\- Classificação = 1 ou 3

\- Data Fiscal \(ou data extemporânea\) – deve ser uma data cujo ano seja = ano base informado em tela

\- Somente notas de entrada \(MOVTO\_E\_S <> ‘9’\)

\- Situação \- somente as notas não canceladas

\- O campo “117\-UF de Origem” da SAFX07 deve ser “MG”;

\- O campo “182\-Município de Origem” da SAFX07 deve estar preenchido;

\- Para os subtópicos __3\.6\.8__ e __3\.6\.9__ devem ser aplicados os dois critérios a seguir:

  \- CFOP ou CFOP/Natureza da nota parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à *Deduções* à CFOP ou CFOP/Natureza de Operação“ para a operação = “__Outras\_Entradas\_a\_Detalhar\_Por\_Municipio__” da UF = MG \(COD\_PARAM = 636\); e

  \- Campo “182\-Município de Origem” da SAFX07 <> campo COD\_MUNICIPIO da tabela ESTABELECIMENTO 

Para o subtópico __3\.6\.14__ devem ser aplicados os dois critérios a seguir:

\- CFOP ou CFOP/Natureza da nota parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à *Deduções* à CFOP ou CFOP/Natureza de Operação”, para a operação = “__Outras\_Entradas\_a\_Detalhar\_Por\_Municipio \(especifico para 3\.6\.14\)__” da UF = MG \(COD\_PARAM 896\); e

\- Campo “182\-Município de Origem” da SAFX07 preenchido

\- Notas com *ou* sem itens na SAFX08/SAFX09; 

\- No caso das notas com itens, será utilizado o CFOP ou CFOP/Natureza do item, e para as notas sem itens, utiliza os da capa;

\- Valor a ser totalizado:

             \-valor contábil do item \(se item da SAFX08\);

             \-valor total do serviço \(se tem da SAFX09\);

             \-valor total da nota \(SAFX07\), se nota sem item;

__Processamento das notas:__

As notas serão agrupadas __*por município de origem *ou do ponto de consumo/terminal faturado \(no caso das utilities\)__, e para cada município será apurado o total das saídas e o total das entradas\.

O resultado final de cada município será =  \[ Total das notas de saída – Total das notas de entrada \]

Para cada município apurado, será gravado o resultado final, de acordo com as regras descritas na __RN05__\.

__RN05__

__                                                        Gravação dos Dados__

O resultado apurado __*para cada município*__ será gravado na tabela da manutenção do registro 1400, correspondente ao menu “Geração à Manutenção à Registro 1400”, com as informações abaixo\.

Caso já exista o registro para o *estabelecimento*, *período*, *município* e *código da tabela de itens p/o índice de participação dos municípios*, os valores calculados serão atualizados, mas, os valores informados \(campos “Outros Valores” e “Outras Deduções”\) que possam já ter sido cadastrados serão mantidos\.

Estabelecimento

Estabelecimento da geração

Período

As datas inicial e final do período serão preenchidas com:

Data Inicial à 01/12/nnnn

Data Final à 31/12/nnnn

Sendo “nnnn” o ano base informado em tela\.

Esses valores serão gerados apenas no arquivo da EFD do mês de dezembro, e por isso, a tabela será gerada com a data inicial e final do mês de dezembro do ano informado em tela\.

Indicador do Produto

*Os campos referentes ao produto serão preenchidos com um caracter branco \(pois fazem parte da chave da tabela\)\.*

Código do Produto

*Os campos referentes ao produto serão preenchidos com um caracter branco \(pois fazem parte da chave da tabela\)\.*

Município

UF = MG

Município = código do município apurado 

Código da Tabela de Itens p/o Índice de Participação dos Municípios

Para o item da prestação de serviço de transporte rodoviário \(conforme __RN03__\):

     Será gravado o conteúdo “__Prestação\_de\_Serviço\_de\_Transporte\_Rodoviário__”;

Para o item denominado “Outras entradas a detalhar por município” \(conforme __RN04__\):

     Será gravado o conteúdo “__Outras\_Entradas\_a\_Detalhar\_por\_Municipio__”; 

Valores Calculados – Valor Apurado

Valor das saídas apurado para o município 

Valores Calculados – Deduções

Valor das deduções apurado para o município \(será o total das notas de entrada parametrizadas como dedução, que é utilizado no item “Outras\_Entradas\_a\_Detalhar\_por\_Municipio”\)\.

Valores Informados – Outros Valores

*\(campo não atualizado na geração, pois corresponde a valor inserido manualmente\)   *

Valores Informados – Outras Deduções

*\(campo não atualizado na geração, pois corresponde a valor inserido manualmente\)*

Valor Total

O valor deste campo é gerado a partir dos seguintes campos da tabela:

        \[ Valor Apurado – Deduções \+ Outros Valores – Outras Deduções \]

= = = = = 

