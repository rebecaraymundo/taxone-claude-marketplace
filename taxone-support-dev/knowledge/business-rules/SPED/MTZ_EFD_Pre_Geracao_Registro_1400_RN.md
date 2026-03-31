# MTZ_EFD_Pre_Geracao_Registro_1400_RN

> Fonte: MTZ_EFD_Pre_Geracao_Registro_1400_RN.docx




THOMSON REUTERS

Módulo Sped Fiscal

Pré-Geração do Registro 1400 (RN – Rio Grande do Norte)


Localização: Menu Sped, Módulo EFD - Escrituração Fiscal Digital, item Pré-Geração à Registro 1400 – Periodicidade Anual/Específico por UF – (UF = RN – Rio Grande do Norte


DOCUMENTO DE REQUISITO


REGRAS DE NEGÓCIO



Esta geração foi criada na MFS3248, com objetivo de fazer a geração dos dados de registro 1400 para RN. Essa geração é especifica para os itens da Orientação Técnica EFD nº 011/2016 (SET-RN) cuja entrega é apenas no arquivo de DEZ, e os valores são referentes às operações de todo exercício.

Os itens gerados são os seguintes:

- Prestação de Serviço de Transporte Rodoviário de Cargas (item 4.1 da OT) – (válido neste menu de Pré-Geração até 31/12/2020)
- Prestação de Serviço de Transporte Aéreo de Cargas (item 4.2 da OT)
- Prestação de Serviço de Transporte Aquaviário de Cargas (item 4.3 da OT)
- Extração de Substâncias Minerais - Na Hipótese da Jazida se Estender por Mais de um Município (item 4.4 da OT)
- Atividades de Distribuição de Energia Elétrica (item 4.5 da OT)
- Atividades de Prestação de Serviços de Comunicação/Telecomunicação (item 4.6 da OT)
- Produção de Petróleo e Gás Natural - Na Hipótese da Produção se Estender por Mais de um Município (item 4.7 da OT)
- Distribuição de Água Canalizada (item 4.8 da OT)
- Distribuição de Gás Natural Canalizado (item 4.9 da OT)
OUTRAS ENTRADAS A DETALHAR POR MUNICÍPIO:
- Atividades de Prestação de Serviço de Transporte Dutoviário/Ferroviário (item 5.1 da OT)
- Sistemas de Integração entre Empresário, Sociedade Empresária ou Empresa Individual de Responsabilidade Limitada e Produtores Rurais (item 5.2 da OT)
- Atividades do Estabelecimento do Contribuinte que se estenderem pelos Territórios de mais de um Município (item 5.3 da OT)
- Atividades de Geração/Transmissão de Energia Elétrica (item 5.4 da OT)
- Atividade de Fornecimento de Refeição Industrial para Município Distinto daquele da Circunscrição do Contribuinte (item 5.5 da OT)
- Mudança do Estabelecimento do Contribuinte para Outro Município (item 5.6 da OT)
- Outras Hipóteses em que Haja Necessidade de Atribuição de Valor Adicionado Fiscal (VAF) a mais de um Município (item 5.7 da OT)

A geração automática irá considerar apenas as operações referentes aos itens descritos abaixo. Os demais itens não terão geração automática, e para informar seus valores, o usuário poderá utilizar a tela manutenção do registro 1400 (campo “Valores Informados”).

- 4.1-Prestação de Serviço de Transporte Rodoviário de Cargas
- 4.2-Prestação de Serviço de Transporte Aéreo de Cargas
- 4.3-Prestação de Serviço de Transporte Aquaviário de Cargas
- 4.5-Atividades de Distribuição de Energia Elétrica
- 4.6-Atividades de Prestação de Serviços de Comunicação/Telecomunicação
- 5.1-Atividades de Prestação de Serviço de Transporte Dutoviário/Ferroviário

Os dados apurados serão armazenados e utilizados posteriormente para gravação do registro 1400 na geração do Sped Fiscal.



A geração é feita separadamente para cada um dos itens a serem apurados (conforme RN00), da seguinte forma:

Prestação de Serviço de Transporte Rodoviário de Cargas,

Obs.:Para o item acima, a partir de 01/01/2021 o cálculo deverá ser gerado mensalmente, e será gerado no registro 1400 diretamente pelo menu de Geração > Meio Magnético.

Prestação de Serviço de Transporte Aéreo de Cargas,
Prestação de Serviço de Transporte Aquaviário de Cargas,
Atividades de Prestação de Serviço de Transporte Dutoviário/Ferroviário:

Nestes casos a apuração é feita a partir dos documentos de transporte da SAFX07.

Atividades de Distribuição de Energia Elétrica,
Atividades de Prestação de Serviços de Comunicação/Telecomunicação,

Nestes casos, a apuração envolve outros segmentos:

- Energia Elétrica;
- Comunicação / Telecomunicação;

Desta forma, a apuração é feita a partir dos documentos de transporte da SAFX07, e para os demais casos, da SAFX42/SAFX43. Em todos os casos também serão consideradas as operações de entrada (deduções) parametrizadas.

Os detalhes do processamento referente a cada um destes itens, e também sobre a gravação dos dados apurados, foram descritos separadamente, nas seguintes regras:




O cálculo para este item é feito de acordo com o “Valor Adicionado Fiscal (VAF)”, conforme orientação que consta no item 4.1.1 da Orientação Técnica EFD nº 011/2016 (SET-RN).

Para este item será feita a totalização das saídas e também das entradas (parametrizadas como dedução), por município de origem, conforme as regras descritas a seguir.

Obs.: À partir do período de 01/01/2021 o cálculo deverá ser gerado mensalmente, e será gerado no registro 1400 diretamente pelo menu de Geração > Meio Magnético. As regras abaixo constam no documento Sped_Fiscal_Regras_Bloco_1.docxs


Origem dos dados à Tabelas dos Documentos Fiscais – Capa e Itens de Mercadoria (SAFX07, SAFX08 e SAFX09).

(a SAFX09 é utilizada apenas na totalização das entradas a serem deduzidas, quando for o caso).

Critérios para recuperação dos documentos de transporte na SAFX07/SAFX08:

- Empresa – empresa do login

- Estabelecimento – estabelecimento da geração
No caso de geração por I.E.U. serão considerados os documentos de todos os estabelecimentos envolvidos na centralização,
(centralizador e centralizados), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle
das Obrigações Estaduais;

- Classificação = 1 ou 4 (a NF de modelo 07/08 usa classificação 1 e os CTRC’s usam classificação 4)

- Data Fiscal (ou data extemporânea) – deve ser uma data cujo ano seja = ano base informado em tela

- Modelo (campo 13) – somente modelos de transporte rodoviário ou multimodal (07, 08, 57)


- Somente notas de saída (MOVTO_E_S = ‘9’)

- Situação - somente as notas não canceladas

- O campo “117-UF de Origem” da SAFX07 deve ser “RN”;

- O campo “182-Município de Origem” da SAFX07 deve estar preenchido;

- Somente notas com CFOP ou CFOP/Natureza parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à CFOP
ou CFOP/Natureza de Operação”, para a operação = “IPM 4.1” da UF = RN;

- Notas com ou sem itens na SAFX08;

- No caso das notas com itens, será utilizado o CFOP ou CFOP/Natureza do item, e para as notas sem itens, utiliza os da capa;

- Valor a ser totalizado à valor contábil do item (SAFX08), ou valor total da nota (SAFX07) para as notas sem itens;


Critérios para recuperação das entradas (deduções) na SAFX07/SAFX08/SAFX09:

- Empresa – empresa do login

- Estabelecimento – estabelecimento da geração
No caso de geração por I.E.U. serão considerados os documentos de todos os estabelecimentos envolvidos na centralização,
(centralizador e centralizados), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle
das Obrigações Estaduais;

- Classificação = 1 ou 3

- Data Fiscal (ou data extemporânea) – deve ser uma data cujo ano seja = ano base informado em tela

- Somente notas de entrada (MOVTO_E_S <> ‘9’)

- Situação - somente as notas não canceladas

- O campo “117-UF de Origem” da SAFX07 deve ser “RN”;

- O campo “182-Município de Origem” da SAFX07 deve estar preenchido;

- Somente notas com  CFOP ou CFOP/Natureza parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à Deduções à CFOP ou CFOP/Natureza de Operação”, para a operação = “IPM 4.1” da UF = RN;

- Notas com ou sem itens na SAFX08/SAFX09;

- No caso das notas com itens, será utilizado o CFOP ou CFOP/Natureza do item, e para as notas sem itens, utiliza os da capa;

- Valor a ser totalizado:
-valor contábil do item (se item da SAFX08);
-valor total do serviço (se item da SAFX09);
-valor total da nota (SAFX07), se nota sem item;

Processamento das notas:

As notas serão agrupadas por município de origem, e para cada município será apurado o total das saídas e o total das entradas.

O resultado final de cada município será = [Total das notas de saída – Total das notas de entrada]

Para cada município apurado, será gravado o resultado final, de acordo com as regras descritas na RN08.

[MFS64253] Tratamento para gerar somente até 31/12/2020

- Data Fiscal (ou data extemporânea) – deve ser uma data cujo ano seja = ano base informado em tela
-Bloquear a data em 31/12/2020.

Caso a data de geração seja após 31/12/2020 informar a seguinte mensagem no Log de Geração:

Item 4.1 – Prestação de Serviço de Transporte Rodoviário de Cargas : A partir de 2021 esse item deverá ser gerado mensalmente na geração do arquivo Meio Magnético, de acordo com a Instrução Normativa nº 001_2020.



O cálculo para este item é feito de acordo com o “Valor Adicionado Fiscal (VAF)”, conforme orientação que consta no item 4.2.2 da Orientação Técnica EFD nº 011/2016 (SET-RN).

Para este item será feita a totalização das saídas e também das entradas (parametrizadas como dedução), por município de origem, conforme as regras descritas a seguir.

Origem dos dados à Tabelas dos Documentos Fiscais – Capa e Itens de Mercadoria (SAFX07, SAFX08 e SAFX09).

(a SAFX09 é utilizada apenas na totalização das entradas a serem deduzidas, quando for o caso).

Critérios para recuperação dos documentos de transporte na SAFX07/SAFX08:

- Empresa – empresa do login

- Estabelecimento – estabelecimento da geração
No caso de geração por I.E.U. serão considerados os documentos de todos os estabelecimentos envolvidos na centralização,
(centralizador e centralizados), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle
das Obrigações Estaduais;

- Classificação = 1 ou 4 (a NF de modelo 07/10 usa classificação 1 e os CTRC’s usam classificação 4)

- Data Fiscal (ou data extemporânea) – deve ser uma data cujo ano seja = ano base informado em tela

- Modelo (campo 13) – somente modelos de transporte (07,10, 57).


- Somente notas de saída (MOVTO_E_S = ‘9’)

- Situação - somente as notas não canceladas

- O campo “117-UF de Origem” da SAFX07 deve ser “RN”;

- O campo “182-Município de Origem” da SAFX07 deve estar preenchido;

- Somente notas com CFOP ou CFOP/Natureza parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à CFOP
ou CFOP/Natureza de Operação”, para a operação = “IPM 4.2” da UF = RN;

- Notas com ou sem itens na SAFX08;

- No caso das notas com itens, será utilizado o CFOP ou CFOP/Natureza do item, e para as notas sem itens, utiliza os da capa;

- Valor a ser totalizado à valor contábil do item (SAFX08), ou valor total da nota (SAFX07) para as notas sem itens;


Critérios para recuperação das entradas (deduções) na SAFX07/SAFX08/SAFX09:

- Empresa – empresa do login

- Estabelecimento – estabelecimento da geração
No caso de geração por I.E.U. serão considerados os documentos de todos os estabelecimentos envolvidos na centralização,
(centralizador e centralizados), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle
das Obrigações Estaduais;

- Classificação = 1 ou 3

- Data Fiscal (ou data extemporânea) – deve ser uma data cujo ano seja = ano base informado em tela

- Somente notas de entrada (MOVTO_E_S <> ‘9’)

- Situação - somente as notas não canceladas

- O campo “117-UF de Origem” da SAFX07 deve ser “RN”;

- O campo “182-Município de Origem” da SAFX07 deve estar preenchido;

- Somente notas com  CFOP ou CFOP/Natureza parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à Deduções à CFOP ou CFOP/Natureza de Operação”, para a operação = “IPM 4.2” da UF = RN;

- Notas com ou sem itens na SAFX08/SAFX09;

- No caso das notas com itens, será utilizado o CFOP ou CFOP/Natureza do item, e para as notas sem itens, utiliza os da capa;

- Valor a ser totalizado:
-valor contábil do item (se item da SAFX08);
-valor total do serviço (se item da SAFX09);
-valor total da nota (SAFX07), se nota sem item;

Processamento das notas:

As notas serão agrupadas por município de origem, e para cada município será apurado o total das saídas e o total das entradas.

O resultado final de cada município será = [Total das notas de saída – Total das notas de entrada]

Para cada município apurado, será gravado o resultado final, de acordo com as regras descritas na RN08.



O cálculo para este item é feito de acordo com o “Valor Adicionado Fiscal (VAF)”, conforme orientação que consta no item 4.3.2 da Orientação Técnica EFD nº 011/2016 (SET-RN).

Para este item será feita a totalização das saídas e também das entradas (parametrizadas como dedução), por município de origem, conforme as regras descritas a seguir.

Origem dos dados à Tabelas dos Documentos Fiscais – Capa e Itens de Mercadoria (SAFX07, SAFX08 e SAFX09).

(a SAFX09 é utilizada apenas na totalização das entradas a serem deduzidas, quando for o caso).

Critérios para recuperação dos documentos de transporte na SAFX07/SAFX08:

- Empresa – empresa do login

- Estabelecimento – estabelecimento da geração
No caso de geração por I.E.U. serão considerados os documentos de todos os estabelecimentos envolvidos na centralização,
(centralizador e centralizados), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle
das Obrigações Estaduais;

- Classificação = 1 ou 4 (a NF de modelo 07/09 usa classificação 1 e os CTRC’s usam classificação 4)

- Data Fiscal (ou data extemporânea) – deve ser uma data cujo ano seja = ano base informado em tela

- Modelo (campo 13) – somente modelos de transporte (07, 09, 57).


- Somente notas de saída (MOVTO_E_S = ‘9’)

- Situação - somente as notas não canceladas

- O campo “117-UF de Origem” da SAFX07 deve ser “RN”;

- O campo “182-Município de Origem” da SAFX07 deve estar preenchido;

- Somente notas com CFOP ou CFOP/Natureza parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à CFOP
ou CFOP/Natureza de Operação”, para a operação = “IPM 4.3” da UF = RN;

- Notas com ou sem itens na SAFX08;

- No caso das notas com itens, será utilizado o CFOP ou CFOP/Natureza do item, e para as notas sem itens, utiliza os da capa;

- Valor a ser totalizado à valor contábil do item (SAFX08), ou valor total da nota (SAFX07) para as notas sem itens;


Critérios para recuperação das entradas (deduções) na SAFX07/SAFX08/SAFX09:

- Empresa – empresa do login

- Estabelecimento – estabelecimento da geração
No caso de geração por I.E.U. serão considerados os documentos de todos os estabelecimentos envolvidos na centralização,
(centralizador e centralizados), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle
das Obrigações Estaduais;

- Classificação = 1 ou 3

- Data Fiscal (ou data extemporânea) – deve ser uma data cujo ano seja = ano base informado em tela

- Somente notas de entrada (MOVTO_E_S <> ‘9’)

- Situação - somente as notas não canceladas

- O campo “117-UF de Origem” da SAFX07 deve ser “RN”;

- O campo “182-Município de Origem” da SAFX07 deve estar preenchido;

- Somente notas com  CFOP ou CFOP/Natureza parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à Deduções à CFOP ou CFOP/Natureza de Operação”, para a operação = “IPM 4.3” da UF = RN;

- Notas com ou sem itens na SAFX08/SAFX09;

- No caso das notas com itens, será utilizado o CFOP ou CFOP/Natureza do item, e para as notas sem itens, utiliza os da capa;

- Valor a ser totalizado:
-valor contábil do item (se item da SAFX08);
-valor total do serviço (se item da SAFX09);
-valor total da nota (SAFX07), se nota sem item;

Processamento das notas:

As notas serão agrupadas por município de origem, e para cada município será apurado o total das saídas e o total das entradas.

O resultado final de cada município será = [Total das notas de saída – Total das notas de entrada]

Para cada município apurado, será gravado o resultado final, de acordo com as regras descritas na RN08.


O cálculo para este item é feito de acordo com o “Valor Adicionado Fiscal (VAF)”, conforme orientação que consta no item 4.5.2 da Orientação Técnica EFD nº 011/2016 (SET-RN).

Para este item será feita a totalização das saídas e também das entradas (parametrizadas como dedução), por ponto de consumo/terminal faturado (no caso das utilities), conforme as regras descritas a seguir.

Origem dos dados à Tabelas dos Documentos Fiscais de Utilities – Capa e Itens (SAFX42 e SAFX43)

Tabelas dos Documentos Fiscais – Capa e Itens de Mercadoria (SAFX07, SAFX08 e SAFX09).

(a SAFX09 é utilizada apenas na totalização das entradas a serem deduzidas, quando for o caso)

[MFS710674] Inclusão do modelo de nota “66”

Critérios para recuperação dos documentos de utilities na SAFX42/SAFX43:

- Empresa – empresa do login

- Estabelecimento – estabelecimento da geração
No caso de geração por I.E.U. serão considerados os documentos de todos os estabelecimentos envolvidos na centralização,
(centralizador e centralizados), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle
das Obrigações Estaduais;

- Data Fiscal – deve ser uma data cujo ano seja = ano base informado em tela

- Modelo (campo 13) – somente 06 ou 66 (Energia Elétrica)

- Situação - somente as notas não canceladas

- O campo “75-UF do Ponto de Consumo/Terminal Faturado” da SAFX42 deve ser “RN”;

- O campo “76-Município do Ponto de Consumo” da SAFX42 deve estar preenchido;

- Os itens informativos não serão considerados (campo “10-Tipo de Item” da SAFX43 = “1”);

- Somente notas com  CFOP parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à CFOP”, para a operação = “IPM 4.5” da UF = RN;

- Como os documentos da 42/43 sempre têm itens, será utilizado o CFOP;

- Valor a ser totalizado à campo “19-Valor do Serviço” do item (SAFX43);


Critérios para recuperação das entradas (deduções) na SAFX07/SAFX08/SAFX09:

- Empresa – empresa do login

- Estabelecimento – estabelecimento da geração
No caso de geração por I.E.U. serão considerados os documentos de todos os estabelecimentos envolvidos na centralização,
(centralizador e centralizados), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle
das Obrigações Estaduais;

- Classificação = 1 ou 3

- Data Fiscal (ou data extemporânea) – deve ser uma data cujo ano seja = ano base informado em tela

- Somente notas de entrada (MOVTO_E_S <> ‘9’)

- Situação - somente as notas não canceladas

- O campo “117-UF de Origem” da SAFX07 deve ser “RN”;

- O campo “182-Município de Origem” da SAFX07 deve estar preenchido;

- Somente notas com  CFOP ou CFOP/Natureza parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à Deduções à CFOP ou CFOP/Natureza de Operação”, para a operação = “IPM 4.5” da UF = RN;

- Notas com ou sem itens na SAFX08/SAFX09;

- No caso das notas com itens, será utilizado o CFOP ou CFOP/Natureza do item, e para as notas sem itens, utiliza os da capa;

- Valor a ser totalizado:
-valor contábil do item (se item da SAFX08);
-valor total do serviço (se tem da SAFX09);
-valor total da nota (SAFX07), se nota sem item;


Processamento das notas:

As notas serão agrupadas por ponto de consumo/terminal faturado (no caso das utilities), e para cada município será apurado o total das saídas e o total das entradas.

O resultado final de cada município será = [Total das notas de saída – Total das notas de entrada]

Para cada município apurado, será gravado o resultado final, de acordo com as regras descritas na RN08.


O cálculo para este item é feito de acordo com o “Valor Adicionado Fiscal (VAF)”, conforme orientação que consta no item 4.6.2 da Orientação Técnica EFD nº 011/2016 (SET-RN).

Para este item será feita a totalização das saídas e também das entradas (parametrizadas como dedução), por ponto de consumo/terminal faturado (no caso das utilities), conforme as regras descritas a seguir.

Origem dos dados à Tabelas dos Documentos Fiscais de Utilities – Capa e Itens (SAFX42 e SAFX43)

Tabelas dos Documentos Fiscais – Capa e Itens de Mercadoria (SAFX07, SAFX08 e SAFX09).

(a SAFX09 é utilizada apenas na totalização das entradas a serem deduzidas, quando for o caso)


Critérios para recuperação dos documentos de utilities na SAFX42/SAFX43:

- Empresa – empresa do login

- Estabelecimento – estabelecimento da geração
No caso de geração por I.E.U. serão considerados os documentos de todos os estabelecimentos envolvidos na centralização,
(centralizador e centralizados), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle
das Obrigações Estaduais;

- Data Fiscal – deve ser uma data cujo ano seja = ano base informado em tela

- Modelo (campo 13) – somente 21 e 22 (Telecom)

- Situação - somente as notas não canceladas

- O campo “75-UF do Ponto de Consumo/Terminal Faturado” da SAFX42 deve ser “RN”;

- O campo “76-Município do Ponto de Consumo” da SAFX42 deve estar preenchido;

- Os itens informativos não serão considerados (campo “10-Tipo de Item” da SAFX43 = “1”);

- Somente notas com CFOP parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à CFOP”, para a operação = “IPM 4.6” da UF = RN;

- Como os documentos da 42/43 sempre têm itens, será utilizado o CFOP;

- Valor a ser totalizado à campo “19-Valor do Serviço” do item (SAFX43);


Critérios para recuperação das entradas (deduções) na SAFX07/SAFX08/SAFX09:

- Empresa – empresa do login

- Estabelecimento – estabelecimento da geração
No caso de geração por I.E.U. serão considerados os documentos de todos os estabelecimentos envolvidos na centralização,
(centralizador e centralizados), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle
das Obrigações Estaduais;

- Classificação = 1 ou 3

- Data Fiscal (ou data extemporânea) – deve ser uma data cujo ano seja = ano base informado em tela

- Somente notas de entrada (MOVTO_E_S <> ‘9’)

- Situação - somente as notas não canceladas

- O campo “117-UF de Origem” da SAFX07 deve ser “RN”;

- O campo “182-Município de Origem” da SAFX07 deve estar preenchido;

- Somente notas com  CFOP ou CFOP/Natureza parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à Deduções à CFOP ou CFOP/Natureza de Operação”, para a operação = “IPM 4.6” da UF = RN;

- Notas com ou sem itens na SAFX08/SAFX09;

- No caso das notas com itens, será utilizado o CFOP ou CFOP/Natureza do item, e para as notas sem itens, utiliza os da capa;

- Valor a ser totalizado:
-valor contábil do item (se item da SAFX08);
-valor total do serviço (se tem da SAFX09);
-valor total da nota (SAFX07), se nota sem item;


Processamento das notas:

As notas serão agrupadas por ponto de consumo/terminal faturado (no caso das utilities), e para cada município será apurado o total das saídas e o total das entradas.

O resultado final de cada município será = [Total das notas de saída – Total das notas de entrada]

Para cada município apurado, será gravado o resultado final, de acordo com as regras descritas na RN08.



O cálculo para este item é feito de acordo com o “Valor Adicionado Fiscal (VAF)”, conforme orientação que consta no item 5.8 da Orientação Técnica EFD nº 011/2016 (SET-RN).

Para este item será feita a totalização das saídas e também das entradas (parametrizadas como dedução), por município de origem, conforme as regras descritas a seguir.

Origem dos dados à Tabelas dos Documentos Fiscais – Capa e Itens de Mercadoria (SAFX07, SAFX08 e SAFX09)

(a SAFX09 é utilizada apenas na totalização das entradas a serem deduzidas, quando for o caso)

Critérios para recuperação dos documentos de transporte na SAFX07/SAFX08:

- Empresa – empresa do login

- Estabelecimento – estabelecimento da geração
No caso de geração por I.E.U. serão considerados os documentos de todos os estabelecimentos envolvidos na centralização,
(centralizador e centralizados), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle
das Obrigações Estaduais;

- Classificação = 1 ou 4

- Data Fiscal (ou data extemporânea) – deve ser uma data cujo ano seja = ano base informado em tela

- Modelo (campo 13) – somente modelos de transporte (07, 11, 16)

- Somente notas de saída (MOVTO_E_S = ‘9’)

- Situação - somente as notas não canceladas

- O campo “117-UF de Origem” da SAFX07 deve ser “RN”;

- O campo “182-Município de Origem” da SAFX07 deve estar preenchido;

- Somente notas com  CFOP ou CFOP/Natureza parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à CFOP
ou CFOP/Natureza de Operação”, para a operação = “IPM 5.1” da UF = RN;

- Notas com ou sem itens na SAFX08;

- No caso das notas com itens, será utilizado o CFOP ou CFOP/Natureza do item, e para as notas sem itens, utiliza os da capa;

- Valor a ser totalizado à valor contábil do item (SAFX08), ou valor total da nota (SAFX07) para as notas sem itens;


Critérios para recuperação das entradas (deduções) na SAFX07/SAFX08/SAFX09:

- Empresa – empresa do login

- Estabelecimento – estabelecimento da geração
No caso de geração por I.E.U. serão considerados os documentos de todos os estabelecimentos envolvidos na centralização,
(centralizador e centralizados), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle
das Obrigações Estaduais;

- Classificação = 1 ou 3

- Data Fiscal (ou data extemporânea) – deve ser uma data cujo ano seja = ano base informado em tela

- Somente notas de entrada (MOVTO_E_S <> ‘9’)

- Situação - somente as notas não canceladas

- O campo “117-UF de Origem” da SAFX07 deve ser “RN”;

- O campo “182-Município de Origem” da SAFX07 deve estar preenchido;

- Somente notas com  CFOP ou CFOP/Natureza parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à Deduções à CFOP ou CFOP/Natureza de Operação”, para a operação = “IPM 5.1” da UF = RN;

- Notas com ou sem itens na SAFX08/SAFX09;

- No caso das notas com itens, será utilizado o CFOP ou CFOP/Natureza do item, e para as notas sem itens, utiliza os da capa;

- Valor a ser totalizado:
-valor contábil do item (se item da SAFX08);
-valor total do serviço (se tem da SAFX09);
-valor total da nota (SAFX07), se nota sem item;


Processamento das notas:

As notas serão agrupadas por município de origem, e para cada município será apurado o total das saídas e o total das entradas.

O resultado final de cada município será = [Total das notas de saída – Total das notas de entrada]

Para cada município apurado, será gravado o resultado final, de acordo com as regras descritas na RN08.



O resultado apurado para cada município será gravado na tabela da manutenção do registro 1400, correspondente ao menu “Geração à Manutenção à Registro 1400”, com as informações abaixo.

Caso já exista o registro para o estabelecimento, período, município e código da tabela de itens p/o índice de participação dos municípios, os valores calculados serão atualizados, mas, os valores informados (campos “Outros Valores” e “Outras Deduções”) que possam já ter sido cadastrados serão mantidos.



= = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS3248 | Atendimento à Orientação Técnica EFD nº 011/2016 – SET-RN | Processo de pré-geração para o registro 1400 de RN para os códigos referentes às operações de todo exercício. | 10/11/2016 (criação do docto) |
| MFS64253 | Ajuste na geração do código 4.1 | Ajuste na regra de geração do código 4.1, para que seja gerado mensalmente a partir de 01/01/2021. | 02/06/2021 |
| MFS710674 | Inclusão do código 66 | Inclusão do modelo de nota “66” na regra do código Atividades de Distribuição de Energia Elétrica IPM 4.5 | 03/02/2025 |


| RN00 | Regras Gerais |
| --- | --- |


| RN01 | Recuperação dos Dados |
| --- | --- |


| RN02 | Prestação de Serviço de Transporte Rodoviário de Cargas |
| --- | --- |
| RN03 | Prestação de Serviço de Transporte Aéreo de Cargas |
| RN04 | Prestação de Serviço de Transporte Aquaviário de Cargas |
| RN05 | Atividades de Distribuição de Energia Elétrica |
| RN06 | Atividades de Prestação de Serviços de Comunicação/Telecomunicação |
| RN07 | Atividades de Prestação de Serviço de Transporte Dutoviário/Ferroviário |
| RN08 | Gravação dos Dados |


| RN02 | Prestação de Serviço de Transporte Rodoviário de Cargas |
| --- | --- |


| Observar que no caso do modelo do CTe (57), não é possível identificar qual é o tipo de transporte, pois esse modelo de conhecimento eletrônico pode ser utilizado para qualquer tipo de transporte. Outro detalhe é que o CFOP não serve para identificar o tipo de transporte, pois são os mesmos para todos os tipos (aéreo, rodoviário, etc...). Assim, a geração considera o modelo 57 para os dois códigos de MG, e caberá ao cliente que utilizar modelo 57, identificar o tipo de transporte através da natureza de operação. |
| --- |


| RN03 | Prestação de Serviço de Transporte Aéreo de Cargas |
| --- | --- |


| Observar que no caso do modelo do CTe (57), não é possível identificar qual é o tipo de transporte, pois esse modelo de conhecimento eletrônico pode ser utilizado para qualquer tipo de transporte. Outro detalhe é que o CFOP não serve para identificar o tipo de transporte, pois são os mesmos para todos os tipos (aéreo, rodoviário, etc...). Assim, a geração considera o modelo 57 para os dois códigos de MG, e caberá ao cliente que utilizar modelo 57, identificar o tipo de transporte através da natureza de operação. |
| --- |


| RN04 | Prestação de Serviço de Transporte Aquaviário de Cargas |
| --- | --- |


| Observar que no caso do modelo do CTe (57), não é possível identificar qual é o tipo de transporte, pois esse modelo de conhecimento eletrônico pode ser utilizado para qualquer tipo de transporte. Outro detalhe é que o CFOP não serve para identificar o tipo de transporte, pois são os mesmos para todos os tipos (aéreo, rodoviário, etc...). Assim, a geração considera o modelo 57 para os dois códigos de MG, e caberá ao cliente que utilizar modelo 57, identificar o tipo de transporte através da natureza de operação. |
| --- |


| RN05 | Atividades de Distribuição de Energia Elétrica |
| --- | --- |


| RN06 | Atividades de Prestação de Serviços de Comunicação/Telecomunicação |
| --- | --- |


| RN07 | Atividades de Prestação de Serviço de Transporte Dutoviário/Ferroviário |
| --- | --- |


| RN08 | Gravação dos Dados |
| --- | --- |


| Estabelecimento | Estabelecimento da geração |
| --- | --- |
| Período | As datas inicial e final do período serão preenchidas com:  Data Inicial à 01/12/nnnn Data Final à 31/12/nnnn  Sendo “nnnn” o ano base informado em tela.  Esses valores serão gerados apenas no arquivo da EFD do mês de dezembro, e por isso, a tabela será gerada com a data inicial e final do mês de dezembro do ano informado em tela. |
| Indicador do Produto | Os campos referentes ao produto serão preenchidos com um caracter branco (pois fazem parte da chave da tabela). |
| Código do Produto | Os campos referentes ao produto serão preenchidos com um caracter branco (pois fazem parte da chave da tabela). |
| Município | UF = RN Município = código do município apurado |
| Código da Tabela de Itens p/o Índice de Participação dos Municípios | Para o item “Prestação de Serviço de Transporte Rodoviário de Cargas” (conforme RN02):      Será gravado o conteúdo “IPM 4.1”;  Para o item “Prestação de Serviço de Transporte Aéreo de Cargas” (conforme RN03):      Será gravado o conteúdo “IPM 4.2”;   Para o item “Prestação de Serviço de Transporte Aquaviário de Cargas” (conforme RN04):      Será gravado o conteúdo “IPM 4.3”;  Para o item “Atividades de Distribuição de Energia Elétrica” (conforme RN05):      Será gravado o conteúdo “IPM 4.5”;  Para o item “Atividades de Prestação de Serviços de Comunicação/Telecomunicação” (conforme RN06):      Será gravado o conteúdo “IPM 4.6”;   Para o item “Atividades de Prestação de Serviço de Transporte Dutoviário/Ferroviário” (conforme RN07):      Será gravado o conteúdo “IPM 5.1”; |
| Valores Calculados – Valor Apurado | Valor das saídas apurado para o município |
| Valores Calculados – Deduções | Valor das deduções apurado para o município.  Será o total das notas de entrada parametrizadas como dedução, que são utilizadas nos itens:  - 4.1- Prestação de Serviço de Transporte Rodoviário de Cargas - 4.2- Prestação de Serviço de Transporte Aéreo de Cargas - 4.3- Prestação de Serviço de Transporte Aquaviário de Cargas - 4.5- Atividades de Distribuição de Energia Elétrica - 4.6- Atividades de Prestação de Serviços de Comunicação/Telecomunicação - 5.1- Atividades de Prestação de Serviço de Transporte Dutoviário/Ferroviário |
| Valores Informados – Outros Valores | (campo não atualizado na geração, pois corresponde a valor inserido manualmente) |
| Valores Informados – Outras Deduções | (campo não atualizado na geração, pois corresponde a valor inserido manualmente) |
| Valor Total | O valor deste campo é gerado a partir dos seguintes campos da tabela:          [Valor Apurado – Deduções + Outros Valores – Outras Deduções] |
