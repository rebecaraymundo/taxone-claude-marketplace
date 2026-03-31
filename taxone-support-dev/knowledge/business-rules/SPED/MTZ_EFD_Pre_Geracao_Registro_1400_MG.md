# MTZ_EFD_Pre_Geracao_Registro_1400_MG

> Fonte: MTZ_EFD_Pre_Geracao_Registro_1400_MG.docx




THOMSON REUTERS

Módulo Sped Fiscal

Pré-Geração do Registro 1400 (MG – Minas Gerais)


Localização: Menu Sped, EFD - Escrituração Fiscal Digital, item Pré-Geração à Registro 1400 – Periodicidade Anual/Específico por UF – (Campo UF = MG – Minas Gerais)



DOCUMENTO DE REQUISITO




REGRAS DE NEGÓCIO



Esta geração foi criada na OS4728-A, com objetivo de fazer a geração dos dados de registro 1400 para MG. Essa geração é especifica para os itens da Resolução 4.730/2014 (SEF-MG) cuja entrega é apenas no arquivo de DEZ, e os valores são referentes às operações de todo exercício.

[MFS73848] Conforme Resolução Nº 5.369 DE 22 DE MAIO DE 2020 (SEF-MG), incluir o tratamento do item 3.6.9 no processo de geração automática, em atendimento ao código “Outras Entradas a Detalhar por Município”.
[MFS672643]: Inclusão do tratamento para o item 3.6.14.

Os itens gerados são os seguintes:

- Prestação de Serviço de Transporte Rodoviário  (item 3.5 da Resolução) – Válido neste menu de Pré-Geração até 31/12/2020.
- Outras Entradas a Detalhar por Município            (item 3.6 da Resolução)

Quanto ao item “Outras Entradas a Detalhar por Município” a geração automática irá considerar apenas as operações referentes aos subitens descritos abaixo. Os demais subitens do item 3.6 não terão geração automática, e para informar seus valores, o usuário poderá utilizar a tela manutenção do registro 1400 (campo “Valores Informados”).

3.6.2 - Atividades de Prestação de Transporte Aéreo de Carga                                                                                                                                           (vide RN04.01)
3.6.3 - Atividades de Prestação de Serviço de Transporte Ferroviário/Aquaviário                                                                                                               (vide RN04.01)
3.6.7 - Atividades de Prestação de Serviços de Comunicação/Telecomunicação                                                                                                                (vide RN04.02)
3.6.8 - Atividade de fornecimento de refeição industrial para município distinto ao da localização do contribuinte                                                              (vide RN04.03) [MFS86206]
3.6.9 - Saídas de mercadorias de estabelecimento de mesmo titular localizado em município diverso daquele onde ocorreu a efetiva comercialização (vide RN04.03) [MFS73848]
3.6.11 - Atividades de Geração de Energia                                                                                                                                                                            (vide RN04.02)
3.6.12 - Atividades de Distribuição de Energia Elétrica                                                                                                                                                          (vide RN04.02)
3.6.13 - Atividades de Transmissão de Energia Elétrica                                                                                                                                                        (vide RN04.02)
3.6.14 - Outras Hipóteses em que Haja Necessidade de Atribuição de VAF a mais de um Município                                                                                  (vide RN04.03) [MFS672643]


Os dados apurados serão armazenados e utilizados posteriormente para gravação do registro 1400 na geração do Sped Fiscal.



Ano Base – Neste campo o usuário informará o ano base das operações a serem totalizadas.

Geração p/Inscrição Estadual Única – Este campo apresenta duas opções: “Sim” e “Não” (seguindo o padrão da tela de geração do Sped).

Default: opção “Não”

Estabelecimentos – Neste campo serão disponibilizados os estabelecimentos para seleção do usuário, de acordo com os seguintes critérios:

- Somente estabelecimentos da empresa do login;

- Somente estabelecimentos da UF de MG;

- Se parâmetro “Geração por inscrição estadual única” = “Sim”:
Nesse caso, serão demonstrados apenas os estabelecimentos centralizadores de I.E.U., de acordo com a parametrização do
módulo de Controle das Obrigações Estaduais (menu “Obrigações à Empresas/Estabelecimentos com Inscrição Estadual Única”);

- Se parâmetro “Geração por inscrição estadual única” = “Não”
Nesse caso, serão demonstrados todos os estabelecimentos que atendam aos demais critérios;

[ALTERAÇÃO MFS3248]
Regras de tela verificar novo documento matriz: MTZ_EFD_Tela_Pre-Geracao_Registro_1400_UF.docx



A geração é feita separadamente para cada um dos dois itens a serem apurados (conforme RN00), da seguinte forma:

Prestação de Serviço de Transporte Rodoviário:

Neste caso a apuração é feita a partir dos documentos de transporte rodoviário da SAFX07.

Obs.: A partir do período de 2021 o cálculo para este item deverá ser gerado mensalmente, (de acordo com a Resolução 5.369 de 22 de maio de 2020 – Subitem 3.4.2), e será gerado no registro 1400 diretamente pelo menu de Geração > Meio Magnético.

Outras Entradas a Detalhar por Município:

Neste caso, a apuração envolve vários segmentos:

- Outros tipos de Transportes (Aéreo, Ferroviário e Aquaviário);
- Energia Elétrica;
- Comunicação / Telecomunicação;

Desta forma, a apuração é feita a partir dos documentos de transporte da SAFX07, e para os demais casos, da SAFX42/SAFX43. Nos dois casos, também serão consideradas as operações de entrada (deduções) parametrizadas.

- Comercialização Produto/Mercadoria [MFS73848]
- Fornecimento de Refeição Industrial [MFS86206]

Para os dois itens acima, a apuração é feita a partir dos documentos de produto/mercadoria da SAFX07 e SAFX08. Também serão consideradas as operações de entrada (deduções) parametrizadas.

O total geral para o item “Outras Entradas a Detalhar por Município” será o total apurado para os segmentos: transportes, energia elétrica, comunicação/telecomunicação, comercialização produto/mercadoria e fornecimento de refeições.

Os detalhes do processamento referente a cada um destes dois itens, e também sobre a gravação dos dados apurados, foram descritos separadamente, nas seguintes regras:





O cálculo para este item é feito de acordo com o “Manual de Orientação para Preenchimento e Entrega da Declaração Anual do Movimento Econômico e Fiscal (DAMEF)”, conforme orientação que consta no item 3.5.1 da Resolução 4.730/2013, SEF-MG (ver detalhes no help do programa da VAF-MG, vrs 7.07.06, opção “Documentos”, help da aba VAF).

Será totalizado o valor das saídas por município de origem, e aplicada a forma de cálculo descrita no programa DAMEF/VAF, conforme as regras descritas a seguir.

Obs.: À partir do período de 2021 o cálculo para este item deverá ser gerado no registro 1400 mensalmente, (de acordo com a Resolução 5.369 de 22 de maio de 2020 – Subitem 3.4.2), e será gerado diretamente pelo menu de Geração do Meio Magnético.


Origem dos dados àTabelas dos Documentos Fiscais – Capa e Itens de Mercadoria  (SAFX07 e SAFX08)


Critérios para recuperação dos documentos de transporte na SAFX07/SAFX08:

- Empresa – empresa do login

- Estabelecimento – estabelecimento da geração
No caso de geração por I.E.U. serão considerados os documentos de todos os estabelecimentos envolvidos na centralização,
(centralizador e centralizados), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle
das Obrigações Estaduais;

- Classificação = 1 ou 4 (a NF de modelo 07 usa classificação 1 e os CTRC’s usam classificação 4)

(modelo 07 é nota fiscal de transporte rodoviário de carga)

- Data Fiscal (ou data extemporânea) – deve ser uma data cujo ano seja = ano base informado em tela

- Modelo (campo 13) – somente modelos de transporte rodoviário ou multimodal (07, 08, 8B, 26, 57, 67)


- Somente notas de saída (MOVTO_E_S = ‘9’)

- Situação - somente as notas não canceladas

- O campo “117-UF de Origem” da SAFX07 deve ser “MG”;

- O campo “182-Município de Origem” da SAFX07 deve estar preenchido;

- Somente notas com  CFOP ou CFOP/Natureza parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à CFOP
ou CFOP/Natureza de Operação”, para a operação = “Prestacao_de_Servico_de_Transporte_Rodoviario” da UF = MG;

- Notas com ou sem itens na SAFX08;

- No caso das notas com itens, será utilizado o CFOP ou CFOP/Natureza do item, e para as notas sem itens, utiliza os da capa;

- Valor a ser totalizado à valor contábil do item (SAFX08), ou valor total da nota (SAFX07) para as notas sem itens;


Processamento das notas:

As notas serão agrupadas por município de origem, e para cada município será apurado o total das saídas. O resultado final será calculado da seguinte forma:



Para cada município apurado, será gravado o resultado final, que corresponde ao valor “C” representado no quadro acima.

As regras para gravação dos dados estão descritas na RN05.

[MFS60170] Incluir bloqueio para gerar somente até 31/12/2020, e Incluir Mensagem no Log de geração.

A partir do período de 2021 o cálculo para este item deverá ser gerado mensalmente, (de acordo com a Resolução 5.369 de 22 de maio de 2020 – Subitem 3.4.2), e será gerado no registro 1400 diretamente pelo menu de Geração > Meio Magnético.

- Data Fiscal (ou data extemporânea) – deve ser uma data cujo ano seja = ano base informado em tela
-Bloquear a data em 31/12/2020.

Caso a data de Geração seja após 31/12/2020 gravar mensagem no Log de Geração:

Item 3.5 – Transporte Rodoviário à será gravada uma mensagem no log com a seguinte descrição: “A partir de 2021 esse item deverá ser gerado mensalmente na geração do arquivo Meio Magnético, de acordo com a Resolução 5.369 de 22 de maio de 2020.



Para este item será feita a totalização das saídas e também das entradas (parametrizadas como dedução), por município de origem ou do ponto de consumo/terminal faturado (no caso das utilities), conforme as regras descritas a seguir.

Origem dos dados àComo este item engloba tanto o segmento de transportes (exceto rodoviário), como energia elétrica e telecom, a totalização das operações tem duas origens:

- Tabelas dos Documentos Fiscais – Capa e Itens de Mercadoria  (SAFX07, SAFX08 e SAFX09)

- Tabelas dos Documentos Fiscais de Utilities – Capa e Itens (SAFX42 e SAFX43)

(a SAFX09 é utilizada apenas na totalização das entradas a serem deduzidas, quando for o caso)

RN04.01 Critérios para recuperação dos documentos de transporte na SAFX07/SAFX08:
Atendimento aos subtópicos:
3.6.2 - Atividades de Prestação de Transporte Aéreo de Carga
3.6.3 - Atividades de Prestação de Serviço de Transporte Ferroviário/Aquaviário

Critérios de Recuperação:
- Empresa – empresa do login

- Estabelecimento – estabelecimento da geração
No caso de geração por I.E.U. serão considerados os documentos de todos os estabelecimentos envolvidos na centralização,
(centralizador e centralizados), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle
das Obrigações Estaduais;

- Classificação = 1 ou 4 (a NF de modelo 27 usa classificação 1 e os CTRC’s usam classificação 4)

(modelo 27 é nota fiscal de transporte ferroviário de carga)

- Data Fiscal (ou data extemporânea) – deve ser uma data cujo ano seja = ano base informado em tela

- Modelo (campo 13) – somente modelos de transporte rodoviário ou multimodal (09, 10, 11, 26, 27, 57, 67)


- Somente notas de saída (MOVTO_E_S = ‘9’)

- Situação - somente as notas não canceladas

- O campo “117-UF de Origem” da SAFX07 deve ser “MG”;

- O campo “182-Município de Origem” da SAFX07 deve estar preenchido;

- Somente notas com  CFOP ou CFOP/Natureza parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à CFOP
ou CFOP/Natureza de Operação”, para a operação = “Outras_Entradas_a_Detalhar_Por_Municipio” da UF = MG;

- Notas com ou sem itens na SAFX08;

- No caso das notas com itens, será utilizado o CFOP ou CFOP/Natureza do item, e para as notas sem itens, utiliza os da capa;

- Valor a ser totalizado à valor contábil do item (SAFX08), ou valor total da nota (SAFX07) para as notas sem itens;


RN04.02 Critérios para recuperação dos documentos de utilities na SAFX42/SAFX43:
Atendimento aos subtópicos:
3.6.7 - Atividades de Prestação de Serviços de Comunicação/Telecomunicação
3.6.11 - Atividades de Geração de Energia
3.6.12 - Atividades de Distribuição de Energia Elétrica
3.6.13 - Atividades de Transmissão de Energia Elétrica

[MFS699904] Inclusão do modelo 66 na pré-geração do código 3.6 - Outras Entradas a Detalhar
[MFS67643] Inclusão da recuperação da notas fiscais de modelo 62

Critérios de Recuperação:
- Empresa – empresa do login

- Estabelecimento – estabelecimento da geração
No caso de geração por I.E.U. serão considerados os documentos de todos os estabelecimentos envolvidos na centralização,
(centralizador e centralizados), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle
das Obrigações Estaduais;

- Data Fiscal (ou data extemporânea) – deve ser uma data cujo ano seja = ano base informado em tela

- Modelo (campo 13) – somente 06, 21, 22, 62 e 66 (EE e Telecom)

- Situação - somente as notas não canceladas

- O campo “75-UF do Ponto de Consumo/Terminal Faturado” da SAFX42 deve ser “MG”;

- O campo “76-Município do Ponto de Consumo” da SAFX42 deve estar preenchido;

- Os itens informativos não serão considerados (campo “10-Tipo de Item” da SAFX43 = “1”);

- Somente notas com  CFOP ou CFOP/Natureza parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à CFOP
ou CFOP/Natureza de Operação”, para a operação = “Outras_Entradas_a_Detalhar_Por_Municipio” da UF = MG;

- Como os documentos da 42/43 sempre têm itens, será utilizado o CFOP ou CFOP/Natureza do item;

- Valor a ser totalizado à campo “19-Valor do Serviço” do item (SAFX43);

- Valor a ser totalizado = Se item de adição, soma o valor do serviço (campo 19 SAFX43),
Se item de dedução, subtrai o valor do desconto (campo 18 da SAFX43);
(ao subtrair o valor do desconto, considerar sempre o valor absoluto)

(Itens de adição são os itens com o campo “20-Adição/Desconto” nulo ou = “A”);
(Itens de dedução são os itens com o campo “20-Adição/Desconto” = “D”);

MFS25904: A totalização das notas recuperadas passou a ser feita da seguinte forma: deve somar o Valor do Serviço dos itens de adição, e subtrair o Valor do Desconto dos itens de dedução, conforme a regra acima.

Exemplo: supondo as notas abaixo para um mesmo município do ponto de Consumo:

Nota 101: Item 1, Adição/ Desc. = “A”, Valor do Serviço = 1.000,00
Item 2, Adição/ Desc. = “A”, Valor do Serviço = 500,00

Nota 102: Item 1, Adição/ Desc. = “A”, Valor do Serviço = 2.000,00
Item 2, Adição/ Desc. = “D”, Valor do Desconto = 300,00

Valor totalizado = 3.200,00 (1.000,00 + 500,00 + 2.000,00 – 300,00)

[MFS73848]
RN04.03 Critérios para recuperação dos documentos de entrada e saída de mercadorias na SAFX07/SAFX08:

Atendimento aos subtópicos:
3.6.8 - Atividade de fornecimento de refeição industrial para município distinto ao da localização do contribuinte
3.6.9 - Saídas de mercadorias de estabelecimento de mesmo titular localizado em município diverso daquele onde ocorreu a efetiva comercialização
3.6.14 - Outras Hipóteses em que Haja Necessidade de Atribuição de VAF a mais de um Município [MFS672643]

[MFS80785] Inclusão da recuperação da notas fiscais de modelo 55
[MFS67643] incluir a recuperação das notas fiscais em atendimento ao subtópico 3.6.14. Para isso considerar notas com CFOP ou CFOP/Natureza parametrizados para a operação “Outras Entradas a Detalhar por Municipio (especifico para 3.6.14)” (COD_PARAM 895) e com município origem preenchido (igual ou diferente do município do estabelecimento).
As notas fiscais recuperadas para atendimento aos subtópicos 3.6.8 e 3.6.9 possuem CFOP ou CFOP/Natureza parametrizados para a operação “Outras Entradas a Detalhar por Municipio” (COD_PARAM = 635) e com município origem preenchido e diferente do município do estabelecimento).


Orientações:
As notas de saída devem ser recuperadas nessa regra.
As notas de entrada devem ser recuperadas na regra de dedução.

Critérios de Recuperação:

- Empresa – empresa do login

- Estabelecimento – estabelecimento da geração

- Data Fiscal (ou data extemporânea) – deve ser uma data cujo ano seja = ano base informado em tela

- Somente notas de saída (MOVTO_E_S = ‘9’)

- Modelo (campo13-MODELO da SAFX07) igual a 01, 1B, 04, 55 ou 65;

- Classificação fiscal (campo 12-COD_CLASS_DOC_FIS da SAFX07) igual a 1 ou 3;

- Situação - somente as notas não canceladas;

- O campo “117-UF de Origem” da SAFX07 deve ser “MG”;

- O campo “182-Município de Origem” da SAFX07 deve estar preenchido;

- Para os subtópicos 3.6.8 e 3.6.9 devem ser aplicados os dois critérios a seguir:
- CFOP ou CFOP/Natureza da nota parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à CFOP ou CFOP/Natureza de Operação“ para a operação = “Outras_Entradas_a_Detalhar_Por_Municipio” da UF = MG (COD_PARAM = 635); e
- Campo “182-Município de Origem” da SAFX07 <> campo COD_MUNICIPIO da tabela ESTABELECIMENTO

Para o subtópico 3.6.14 devem ser aplicados os dois critérios a seguir:
- CFOP ou CFOP/Natureza da nota parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à CFOP ou CFOP/Natureza de Operação”, para a operação = “Outras_Entradas_a_Detalhar_Por_Municipio (especifico para 3.6.14)” da UF = MG (COD_PARAM 895); e
- Campo “182-Município de Origem” da SAFX07 preenchido

- Notas com ou sem itens na SAFX08;

- No caso das notas com itens, será utilizado o CFOP ou CFOP/Natureza do item, e para as notas sem itens, utiliza os da capa;

- Valor a ser totalizado à valor contábil do item (SAFX08), ou valor total da nota (SAFX07) para as notas sem itens;


RN04.04 Critérios para recuperação das entradas (deduções) na SAFX07/SAFX08/SAFX09:
[MFS67643] incluir a recuperação das notas fiscais de dedução em atendimento ao subtópico 3.6.14. Para isso considerar notas com CFOP ou CFOP/Natureza parametrizados para a operação “Outras Entradas a Detalhar por Municipio (especifico para 3.6.14)” (COD_PARAM 896) e com município origem preenchido (igual ou diferente do município do estabelecimento).
As notas fiscais de dedução recuperadas para atendimento aos subtópicos 3.6.8 e 3.6.9 possuem CFOP ou CFOP/Natureza parametrizados para a operação “Outras Entradas a Detalhar por Municipio” (COD_PARAM = 636) e com município origem preenchido e diferente do município do estabelecimento).

- Empresa – empresa do login

- Estabelecimento – estabelecimento da geração
No caso de geração por I.E.U. serão considerados os documentos de todos os estabelecimentos envolvidos na centralização,
(centralizador e centralizados), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle
das Obrigações Estaduais;

- Classificação = 1 ou 3

- Data Fiscal (ou data extemporânea) – deve ser uma data cujo ano seja = ano base informado em tela

- Somente notas de entrada (MOVTO_E_S <> ‘9’)

- Situação - somente as notas não canceladas

- O campo “117-UF de Origem” da SAFX07 deve ser “MG”;

- O campo “182-Município de Origem” da SAFX07 deve estar preenchido;

- Para os subtópicos 3.6.8 e 3.6.9 devem ser aplicados os dois critérios a seguir:
- CFOP ou CFOP/Natureza da nota parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à Deduções à CFOP ou CFOP/Natureza de Operação“ para a operação = “Outras_Entradas_a_Detalhar_Por_Municipio” da UF = MG (COD_PARAM = 636); e
- Campo “182-Município de Origem” da SAFX07 <> campo COD_MUNICIPIO da tabela ESTABELECIMENTO

Para o subtópico 3.6.14 devem ser aplicados os dois critérios a seguir:
- CFOP ou CFOP/Natureza da nota parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à Deduções à CFOP ou CFOP/Natureza de Operação”, para a operação = “Outras_Entradas_a_Detalhar_Por_Municipio (especifico para 3.6.14)” da UF = MG (COD_PARAM 896); e
- Campo “182-Município de Origem” da SAFX07 preenchido


- Notas com ou sem itens na SAFX08/SAFX09;

- No caso das notas com itens, será utilizado o CFOP ou CFOP/Natureza do item, e para as notas sem itens, utiliza os da capa;

- Valor a ser totalizado:
-valor contábil do item (se item da SAFX08);
-valor total do serviço (se tem da SAFX09);
-valor total da nota (SAFX07), se nota sem item;


Processamento das notas:

As notas serão agrupadas por município de origem ou do ponto de consumo/terminal faturado (no caso das utilities), e para cada município será apurado o total das saídas e o total das entradas.

O resultado final de cada município será =  [ Total das notas de saída – Total das notas de entrada ]

Para cada município apurado, será gravado o resultado final, de acordo com as regras descritas na RN05.



O resultado apurado para cada município será gravado na tabela da manutenção do registro 1400, correspondente ao menu “Geração à Manutenção à Registro 1400”, com as informações abaixo.

Caso já exista o registro para o estabelecimento, período, município e código da tabela de itens p/o índice de participação dos municípios, os valores calculados serão atualizados, mas, os valores informados (campos “Outros Valores” e “Outras Deduções”) que possam já ter sido cadastrados serão mantidos.





= = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| OS4728-A | Atendimento à Resolução 4.730, de 17/12/14, SEF-MG | Criação do processo de pré-geração para o registro 1400 de MG para os códigos referentes às operações de todo exercício. | 27/03/2015 (criação do docto) |
| MFS3248 | Lara Aline | Ajuste na tela de pré-geração para que possa atender todas as UF que possuem geração específica anual para o Registro 1400. | 09/11/2016 |
| MFS24921 | Andréa Rocha | Inclusão do modelo 67. | 28/02/2019 |
| MFS25904 | Tratamento dos Itens de Desconto da SAFX43 | Alteração na totalização das notas para efetuar a dedução do valor do Desconto dos itens de dedução (ver RN04, totalização das notas da SAFX42/SAFX43). | 30/06/2020 |
| MFS60170 | Tratamento – Inclução de filtro de geração e mensagem. | Alteração na geração do registro 1400 – Geração Específica para UF = MG Tratamento na geração do registro 1400, item “3.5 - Prestação de Serviço de Transporte Rodoviário” | 05/04/2021 |
| MFS73848 | Aline Melo | Inclusão de subitem no processo de pré-geração do código 3.6 Outras Entradas a Detalhar por Município, para a geração automática do 1400. | 04/11/2021 |
| MFS80785 | Andréa Rocha | Inclusão do modelo 55 na pré-geração do item 3.6.9 (Saídas de mercadorias de estabelecimento de mesmo titular). | 14/02/2022 |
| MFS86206 | Aline Melo | Inclusão de subitem 3.6.8 no processo de pré-geração do código 3.6 Outras Entradas a Detalhar por Município, para a geração automática do 1400. | 17/06/2022 |
| MFS699904 | Andréa Rocha | Inclusão do modelo 66 na pré-geração do código 3.6 - Outras Entradas a Detalhar por Município, para a geração automática do 1400. | 30/10/2024 |
| MFS672643 | Liliane Assaf | RN04:Alteração na geração do código 3.6 – “Outras Entradas a Detalhar por Município”:: Incluir recuperação das notas de modelo 62 (NFCOM) referentes ao subtópico 3.6.7 – Atividades de Prestação de Serviços de Comunicação/Telecomunicação (RN04.02). Passar a gerar o subtópico “3.6.14 - Outras Hipóteses em que Haja Necessidade de Atribuição de VAF a mais de um Município” (RN04.03) | 17/01/2025 |


| RN00 | Regras Gerais |
| --- | --- |


| RN01 | Parâmetros da Geração |
| --- | --- |


| RN02 | Recuperação dos Dados |
| --- | --- |


| RN03 | Prestação de Serviço de Transporte Rodoviário |
| --- | --- |
| RN04 | Outras Entradas a Detalhar por Município |
| RN05 | Gravação dos Dados |


| RN03 | Prestação de Serviço de Transporte Rodoviário |
| --- | --- |


| Observar que no caso do modelo do CTe (57), não é possível identificar qual é o tipo de transporte, pois esse modelo de conhecimento eletrônico pode ser utilizado para qualquer tipo de transporte. Outro detalhe é que o CFOP não serve para identificar o tipo de transporte, pois são os mesmos para todos os tipos (aéreo, rodoviário, etc...). Assim, a geração considera o modelo 57 para os dois códigos de MG, e caberá ao cliente que utilizar modelo 57, identificar o tipo de transporte através da natureza de operação. |
| --- |


| A =  Total das notas de saída      B =  20% do valor de A      C = A – B |
| --- |


| RN04 | Outras Entradas a Detalhar por Município |
| --- | --- |


| Observar que no caso do modelo do CTe (57), não é possível identificar qual é o tipo de transporte, pois esse modelo de conhecimento eletrônico pode ser utilizado para qualquer tipo de transporte. Outro detalhe é que o CFOP não serve para identificar o tipo de transporte, pois são os mesmos para todos os tipos (aéreo, rodoviário, etc...). Assim, a geração considera o modelo 57 para os dois códigos de MG, e caberá ao cliente que utilizar modelo 57, identificar o tipo de transporte através da natureza de operação. |
| --- |


| RN05 | Gravação dos Dados |
| --- | --- |


| Estabelecimento | Estabelecimento da geração |
| --- | --- |
| Período | As datas inicial e final do período serão preenchidas com:  Data Inicial à 01/12/nnnn Data Final à 31/12/nnnn  Sendo “nnnn” o ano base informado em tela.  Esses valores serão gerados apenas no arquivo da EFD do mês de dezembro, e por isso, a tabela será gerada com a data inicial e final do mês de dezembro do ano informado em tela. |
| Indicador do Produto | Os campos referentes ao produto serão preenchidos com um caracter branco (pois fazem parte da chave da tabela). |
| Código do Produto | Os campos referentes ao produto serão preenchidos com um caracter branco (pois fazem parte da chave da tabela). |
| Município | UF = MG Município = código do município apurado |
| Código da Tabela de Itens p/o Índice de Participação dos Municípios | Para o item da prestação de serviço de transporte rodoviário (conforme RN03):      Será gravado o conteúdo “Prestação_de_Serviço_de_Transporte_Rodoviário”;  Para o item denominado “Outras entradas a detalhar por município” (conforme RN04):      Será gravado o conteúdo “Outras_Entradas_a_Detalhar_por_Municipio”; |
| Valores Calculados – Valor Apurado | Valor das saídas apurado para o município |
| Valores Calculados – Deduções | Valor das deduções apurado para o município (será o total das notas de entrada parametrizadas como dedução, que é utilizado no item “Outras_Entradas_a_Detalhar_por_Municipio”). |
| Valores Informados – Outros Valores | (campo não atualizado na geração, pois corresponde a valor inserido manualmente) |
| Valores Informados – Outras Deduções | (campo não atualizado na geração, pois corresponde a valor inserido manualmente) |
| Valor Total | O valor deste campo é gerado a partir dos seguintes campos da tabela:          [ Valor Apurado – Deduções + Outros Valores – Outras Deduções ] |
