# MTZ-EFD_Contribuicoes_Financeiras_Assemelhadas-Geracao_dos_Registros

- **Fonte:** MTZ-EFD_Contribuicoes_Financeiras_Assemelhadas-Geracao_dos_Registros.docx
- **Modificado:** 2026-02-02
- **Tamanho:** 98 KB

---

# EFD \- Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas \- Geração dos Registros 

##### DOCUMENTO DE REQUISITO 

###### DR

###### Nome

__Descrição__

OS3810\-B

EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas – Geração dos Registros

Essa OS tem por objetivo a geração dos registros e da apuração do módulo EFD–Contribuições Financeira/Assemelhada\. Trata\-se da escrituração digital dos tributos PIS e COFINS para as instituições financeiras, seguradoras, entidades de previdência privada, operadoras de planos de assistência à saúde e assemelhadas, conforme Ato Declaratório Executivo nº\. 65 de 20/12/12\.

OS3810\-D

EFD \- Contribuições Financeira/Assemelhada \- Geração do Meio Magnético

Essa OS tem por objetivo permitir a geração do meio magnético do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas e permitir a geração dos Demonstrativos por Contribuição e Natureza da Receita\.

OS3732

EFD \- Contribuições Financeira/Assemelhada \- Geração do Meio Magnético

Inclusão da opção de Geração Multiempresa

OS3810\-E

EFD \- Contribuições Financeira/Assemelhada \- Geração do Meio Magnético

Definição das regras de geração dos registros: F001 – Abertura do Bloco F, F600 – Contribuição Retida na Fonte, F700 – Deduções Diversas, F990 – Encerramento do Bloco F, 1001 – Abertura do Bloco 1, 1300 – Controle dos Valores Retidos na Fonte – PIS/PASEP, 1700 – Controle dos Valores Retidos na Fonte – COFINS e 1990 – Encerramento do Bloco 1\.

CH29448/2013

EFD\-Contribuições Financeira/Assemelhada – Geração do Meio Magnétivo

Ajuste na regra de exibição dos estabelecimentos e empresa na tela de geração para que demonstre a informação em ordem crescente\.

CH5184\_2014

EFD\-Contribuições Financeira/Assemelhada – Geração do Meio Magnétivo

Ajuste na regra de geração dos registros I200 e I300 para que deixem de demonstrar registros com valor zero\.

OS4322

EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas – Geração dos Registros

Automatização do processo para geração do Registro M350\.

CH23215\_2015

EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas – Geração dos Registros

Ajuste na regra de geração dos registros M410 e M810 para desconsiderá\-los quando não houver valor de receita\.

MFS33127

Andréa Rocha

Inclusão de regra para definição do layout de acordo com o período informado\.

MFS33912

Aline Melo

Inclusão do registro 0900 em atendimento ao novo layout versão 1\.32, válido a partir de Janeiro de 2020\.

MFS\-761087

Bruna Ribeiro

O objetivo desta solicitação é incluir um parâmetro na tela de dados iniciais referente ao Registro 0110 \(Regimes de Apuração da Contribuição Social e de Apropriação de Crédito\) para a apuração da contribuição com base na alíquota específica\.

#### Cód\.

### Descrição

### DR

# RN01

Deverá ser criada uma tela chamada “Geração dos Registros – EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas”\. 

Essa tela será responsável pela geração dos registros para posterior geração do meio magnético \(arquivo TXT\) do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas\.

OS3810\-B

# RN02

Serão disponibilizados na tela os seguintes campos:

- __Data Inicial:__ nesse campo, o usuário irá informar a Data Inicial para a geração dos registros\. A partir da Data Inicial informada nesse campo, o sistema irá recuperar as informações das Operações do Período\.
- __Data Final:__ nesse campo, o usuário irá informar a Data Final para a geração dos registros\. A partir da Data Final informada nesse campo, o sistema irá recuperar as informações das Operações do Período\. OBS: caso a Data Final seja menor que a Data Inicial, o sistema não deverá permitir a geração e deverá exibir uma mensagem de erro padrão para essa situação\.
- __Leiaute:__ será exibido o leiaute de acordo com a TFIX67 importada\.

 Se a data inicial e a final for a partir de julho/2012 \(deverá ser visualizado na tela, apenas o leiaute: Escrituração Fiscal Digital das    

                 Contribuições Financeiras e Assemelhadas – Versão 2\.0\.1A\)

                 Se a data inicial e a final for a partir de janeiro/2019 \(deverá ser visualizado na tela, apenas o leiaute: Escrituração Fiscal Digital das   

                 Contribuições Financeiras e Assemelhadas \-  Versão 3\.1\.0A\)

__                 \[MFS33127\]__ Inclusão do leiaute 2020

                 Se a data inicial e a final for a partir de janeiro/2020 \(deverá ser visualizado na tela, apenas o leiaute: Escrituração Fiscal Digital das   

 Contribuições Financeiras e Assemelhadas \-  Versão 3\.2\.0A\) 

- __Perfil:__ nesse campo, o usuário irá selecionar o Perfil parametrizado no menu: Parâmetros >> Perfil do módulo EFD\-Contribuições Financeira/Assemelhada\. Só será permitida a seleção de um perfil que esteja vinculado nessa mesma parametrização ao leiaute selecionado\. OBS: no momento só temos um leiaute, mas caso no futuro sejam criados novos leiautes, o sistema já estará em parte preparado para essa situação\.
- __Tipo de Escrituração:__ deve ser um campo do tipo lista que exiba às opções “Original” e “Retificadora”\. Por padrão, deve ser demonstrado sempre a opção “Original”\.
- __Núm\. Recibo Última Declaração:__ campo do tipo texto\. Por padrão deve estar desabilitado em tela para edição, sendo habilitado somente quando no campo Tipo de Escrituração for selecionada a opção “Retificadora”\.
- __Multiempresa:__ Quando o parâmetro Geração Multiempresa estiver marcado, no campo Empresa/Estabelecimento, serão exibidas todas as empresas que o usuário logado possui acesso e que possuam estabelecimentos com parametrização em Dados Iniciais\. Para as empresas selecionadas será gerado um arquivo \(processo\) para cada estabelecimento centralizador, com os dados dos respectivos estabelecimentos centralizados \(de acordo com a parametrização realizada no Módulo: Mastersaf DW/ Básicos / Parâmetros, Menu: Preliminares >> Centralização da Escrituração das Obrigações Federais\) e caso existam estabelecimentos descentralizados para esta empresa, será gerado um arquivo \(processo\) para cada estabelecimento descentralizado\. Se o parâmetro estiver desmarcado, serão apresentados no campo Empresa/Estabelecimento os estabelecimentos centralizados e descentralizados \(considerando o perfil de acesso do usuário e os estabelecimentos que possuam parametrização em Dados Iniciais\), para o usuário selecionar para qual  estabelecimento serão gerados os arquivos\.
- __Demonstrativo da Apuração por Tipo de Contribuição:__ nesse flag, caso o usuário selecione o mesmo será gerado o Demonstrativo da Apuração por Tipo de Contribuição\.
- __Demonstrativo da Apuração por Tipo de Natureza da Receita:__ nesse flag, caso o usuário selecione o mesmo será gerado o Demonstrativo da Apuração por Tipo de Natureza da Receita\.
- __Empresa/Estabelecimento:__ nesse campo, o usuário deverá selecionar quais empresas ou estabelecimentos \(dependendo do parâmetro Multi\-Empresa\) deverão ser selecionados para geração do meio magnético da EFD\-Contribuições Financeira/Assemelhada\. Serão, exibidos em ordem crescente, os estabelecimentos ou empresas que o usuário possui permissão de acesso\. Campo não obrigatório de preenchimento\.

OS3810\-B

OS3810\-D

OS3732

CH29448/ 2013

MFS33127

__Relação de Registros que serão gerados__

__Bloco 0 \- Abertura, Identificação e Referências__

- __Registro 0000 – Abertura do Arquivo Digital e Identificação da Pessoa Jurídica__

__RNG\-0000__

Deve ser gerado um registro 0000 por arquivo, com os dados de identificação do estabelecimento\.

OBS: Na geração centralizada \(Parâmetros > Preliminares > Centralização de Escrituração, deve\-se utilizar os dados do Estabelecimento centralizador\.

Registro de nível 0, ocorrência de 1 por arquivo e obrigatório\.

OS3810\-B

__RN0000\-02__

__Campo COD\_VER__

Gerar com a informação 003, se o leiaute utilizado \(na tela de Geração dos Registros\) for EPC201\.

__\[MFS33127\] __Inclusão do leiaute 2020

Gerar com a informação 006, se o leiaute utilizado \(na tela de Geração dos Registros\) for EPC320\.

OS3810\-B

MFS33127

__RN0000\-03__

__Campo TIPO\_ESCRIT__:

Verificar o parâmetro “Tipo de Escrituração” informado na tela de geração:

Se Tipo de Escrituração = “Original”

      Gravar “0”

Senão            

      Gravar “1” \(Retificadora\)

OS3810\-B

__RN0000\-04__

__Campo IND\_SIT\_ESP:__

Se a data de início de atividade \(campo DAT\_ INI\_ATIVIDADE da tabela estabelecimento\) estiver entre a data inicial e final de geração do arquivo = ‘0’

Se a data de cisão \(campo DATA\_CISAO da tabela estabelecimento\) estiver entre a data inicial e final da geração do arquivo ou se o dia inicial for diferente de “01” e a data da cisão for igual a data inicial de geração “\-1”,preencher com  ‘1’

Se a data de fusão \(campo DATA\_FUSAO da tabela estabelecimento\) estiver entre a data inicial e final da geração do arquivo ou se o dia inicial for diferente de “01” e a data da fusão for igual a data inicial de geração “\-1”, igual = ‘2’

Se a data de incorporação \(campo DATA\_INCORPORACAO da tabela estabelecimento\) estiver entre a data inicial e final da geração do arquivo ou se o dia inicial for diferente de “01” e a data da incorporação for igual a data inicial de geração “\-1”, igual = ‘3’

Se a data de encerramento \(campo DT\_ENCERRAMENTO da tabela estabelecimento\) estiver entre a data inicial e final de geração do arquivo, preencher com “4”\.

OS3810\-B

__RN0000\-05__

__Campo NUM\_REC\_ANTERIOR:__

Este campo deve ser preenchido com o conteúdo do campo Número do Recibo da Escrituração Anterior, informado na tela de geração\.

OS3810\-B

__RN0000\-06__

__Campo DT\_INI:__

Este campo deve ser preenchido com o dia, mês e ano inicial através do parâmetro Data Inicial, informado na tela de geração\.

OS3810\-B

__RN0000\-07__

__Campo DT\_FIN:__

Este campo deve ser preenchido com o dia, mês e ano final através do parâmetro Data Final, informado na tela de geração\.

OS3810\-B

__RN0000\-13__

__Campo IND\_NAT\_PJ:__

Esse campo deve ser preenchido de acordo com as opções selecionadas no campo Natureza de pessoa jurídica da tela de manutenção do Estabelecimento, localizado no módulo: Básicos 🡪 Parâmetros 🡪 Preliminares 🡪 Estabelecimento/Companhia, com o seguinte critério:

Se a opção selecionada for igual ‘’Sociedade empresária em geral’’, gravar ‘’00’’

Se a opção selecionada for igual ‘’Sociedade cooperativa’’, gravar ‘’01’’

Se a opção selecionada for igual ‘’Entidade sujeita ao PIS/Pasep exclusivamente Folha de Salários’’, gravar ‘’02’’\.

OS3810\-B

__RN0000\-14__

__Campo IND\_ATIV:__

Esse campo deve ser preenchido de acordo com as opções selecionadas no campo Tipo de Atividade de pessoa jurídica da tela de manutenção do Estabelecimento, localizado no módulo: Básicos 🡪Parâmetros 🡪 Preliminares 🡪 Estabelecimento/Companhia, com o seguinte critério:

Se a opção selecionada for igual ‘Industrial ou equiparado a industrial’’, gravar ‘’0’’

Se a opção selecionada for igual ‘’Prestador de serviços’’, gravar ‘’1’’

Se a opção selecionada for igual “’Atividade de comércio”, gravar ‘’2’’

Se a opção selecionada for igual “’Atividade financeira”, gravar “3’’

Se a opção selecionada for igual ‘”Atividade imobiliária”, gravar “4’’

Se a opção selecionada for igual “’Outros”, gravar “9’’

OS3810\-B

- __Registro 0001 – Abertura Bloco 0__

__RNG\-0001__

Deve ser gerado um registro 0001 por arquivo\.

Registro de nível 1, ocorrência de 1 por arquivo e obrigatório\.

OS3810\-B

__RN0001\-02__

__Campo IND\_MOV__

Gerar fixo “0”\.

OS3810\-B

- __Registro 0100 – Dados do Contabilista__

__RN0100__

Um registro por arquivo\. Conterá os dados do contabilista responsável, parametrizado no módulo EFD\-PIS/COFINS, menu: Sped → EFD – Escrituração Fiscal Digital \- PIS/PASEP\-COFINS → Parâmetros 🡪 Dados Iniciais\.

OBS: Na geração centralizada, deve\-se utilizar o contabilista parametrizado para o Estabelecimento centralizador\.

OS3810\-B

__RN0100\-03__

__RN0100\-05__

Quanto aos campos 03 e 05 \(CNPJ/CPF\), preencher apenas um deles, dependendo do conteúdo do campo “CPF/CNPJ” do contabilista\. Se for um CPF, gravar o campo 03, e se for um CNPJ, gravar o campo 05\.

OS3810\-B

__RN0100\-14__

__Campo COD\_MUN__:

Concatenação do Código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município do contabilista responsável \(para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\)\.

OS3810\-B

- __Registro 0110 – Regimes de Apuração da Contribuição Social__

__RNG\-0110__

Deve ser gerado um registro 0001 por arquivo\.

Registro de nível 2, ocorrência de 1 por arquivo e obrigatório\.

OS3810\-B

__RN0110\-02__

__Campo COD\_INC\_TRIB:__

Gerar com “2”\.

OS3810\-B

__RN0110\-03__

__Campo IND\_APRO\_CRED:__

Gerar nulo \(“||”\)\.

OS3810\-B

__RN0110\-04__

__Campo COD\_TIPO\_CONT:__

Código indicador do Tipo de Contribuição Apurada no Período:

1 – Apuração da Contribuição Exclusivamente a Alíquota Básica 

2 – Apuração da Contribuição a Alíquotas Específicas \(Diferenciadas e/ou por Unidade de Medida de Produto\)

OBS: Verificar o parâmetro de Dados iniciais, p/ preencher o campo\.

OS3810\-B

MFS\- 761087

__RN0110\-05__

__Campo IND\_REG\_CUM:__

Gerar nulo \(“||”\)\.

OS3810\-B

- __Registro 0140 – Tabela de Cadastro do Estabelecimento__

# Registro 0140 – Tabela de Cadastro do EstabelecimentoRN0140

Na geração centralizada, será gerado um registro para o estabelecimento centralizador, e um registro para cada estabelecimento centralizado\.

Se o estabelecimento centralizado não possuir movimento e/ou estejam encerrados \(caso o campo Data Encerramento do cadastro do Estabelecimento seja anterior à data de geração do EFD\-Contribuições Financeira/Assemelhada\) não devem ser gerados registros 0140 para esse estabelecimento\.

Para o estabelecimento centralizador que possua ou não movimento sempre deve ser gerado o registro 0140 no período de geração do EFD\-Contribuições Financeira/Assemelhada\.

Registro de nível 2, ocorrência de vários por arquivo e obrigatório\.

OS3810\-B

# RN0140\-01

__Registro 0140 – 01 – REG:__

Deverá ser gravado no campo 01 – REG o texto fixo “0140”\.

OS3810\-B

# RN0140\-02

__Registro 0140 – 02 – COD\_EST:__

Deverá ser gravado no campo 02 – COD\_EST o Código do Estabelecimento\. Essa informação deverá ser recuperada do campo “Código Estabelecimento” do cadastro de Empresa/Estabelecimento \(menu: Preliminares >> Empresa/Estabelecimento\) do módulo Parâmetros\.

OS3810\-B

# RN0140\-03

__Registro 0140 – 03 – NOME:__

Deverá ser gravado no campo 03 – NOME a Razão Social do Estabelecimento\. Essa informação deverá ser recuperada do campo “Razão Social” do cadastro de Empresa/Estabelecimento \(menu: Preliminares >> Empresa/Estabelecimento\) do módulo Parâmetros\.

OS3810\-B

# RN0140\-04

__Registro 0140 – 04 – CNPJ:__

Deverá ser gravado no campo 04 – CNPJ a Razão Social do Estabelecimento\. Essa informação deverá ser recuperada do campo “CNPJ” do cadastro de Empresa/Estabelecimento \(menu: Preliminares >> Empresa/Estabelecimento\) do módulo Parâmetros\.

OS3810\-B

# RN0140\-05

__Registro 0140 – 05 – UF:__

Deverá ser gravado no campo 05 – UF o Código do Estado \(Unidade Federativa\) do Estabelecimento\. Essa informação deverá ser recuperada do campo “UF” do cadastro de Empresa/Estabelecimento \(menu: Preliminares >> Empresa/Estabelecimento\) do módulo Parâmetros\.

OS3810\-B

# RN0140\-06

__Registro 0140 – 06 – IE:__

Deverá ser gravado no campo 06 – IE a Inscrição Estadual do Estabelecimento\. Essa informação deverá ser recuperada do campo “Inscrição Estadual” do cadastro de Inscrição Estadual \(menu: Preliminares >> Inscrições Estaduais\) do módulo Parâmetros\.

Caso a Inscrição estadual do Estabelecimento possua o conteúdo = “ISENTO”, gravar o campo sem informação “||”\.

OS3810\-B

# RN0140\-07

__Registro 0140 – 07 – COD\_MUN:__

Deverá ser gravado no campo 07 – COD\_MUN o Código do Município do Estabelecimento\. Essa informação deverá ser recuperada da concatenação dos campos Código UF \+ Código Município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros a esquerda quando necessário\. 

OS3810\-B

# RN0140\-08

__Registro 0140 – 08 – IM:__

Deverá ser gravado no campo 08 – IM a Inscrição Municipal do Estabelecimento\. Essa informação deverá ser recuperada do campo “Inscrição Municipal” do cadastro de Estabelecimento \(menu: Preliminares >> Empresa/Estabelecimento\) do módulo Parâmetros\.

OS3810\-B

# RN0140\-09

__Registro 0140 – 09 – SUFRAMA:__

Deverá ser gravado no campo 09 – SUFRAMA o Número de Inscrição do Estabelecimento na SUFRAMA\. Essa informação deverá ser recuperada do campo “Inscrição SUFRAMA” do cadastro de Estabelecimento \(menu: Preliminares >> Empresa/Estabelecimento\) do módulo Parâmetros\.

OS3810\-B

- __Registro 0500 – Plano de Contas Contábeis	__

__RNG\-0500__

Este registro deve ser gerado a partir das contas contábeis referenciadas nos diversos registros da EFD\-PIS/COFINS\.

Gravar um registro 0500 para cada conta contábil \(campo COD\_CTA constante na movimentação do período\)

O registro da SAFX2002 \(Tabela do Plano de Contas\) a ser considerado, deve ser sempre o de maior data de validade, que seja <= a data final do período\.

OBS1: Na geração centralizada, gravar as observações envolvidas nos documentos de todos os Estabelecimentos\. Nesse caso, os registros 0500 serão gerados abaixo do registro 0140 do estabelecimento centralizador\.

Registro de nível 2, ocorrência de vários por arquivo e obrigatório se houver\.

OS3810\-B

__RN0500\-02__

__Campo DT\_ALT:__

Campo Data Início/Inclusão/Alteração da SAFX2002\.

OS3810\-B

__RN0500\-03__

__Campo COD\_ NAT\_CC:__

Este campo deve ser preenchido de acordo com o conteúdo do campo “07\-Indicador de Natureza” da SAFX2002, da seguinte forma:

Se Indicador = 0 \(Compensação\)

    gravar 05 \(Contas de Compensação\);

Se Indicador = 1 \(Ativo\)

     gravar 01 \(Contas de Ativo\);

Se Indicador = 2 \(Passivo\)

     gravar 02 \(Contas de Passivo\);

Se Indicador = 3 \(Despesa\), 4 \(Receita\) ou 8 \(Custo\) 

     gravar 04 \(Contas de Resultado\);

Se Indicador = 7 \(Patrimônio Líquido\)

     gravar 03 \(Patrimônio Líquido\);

Se Indicador = 5 \(Mutações Ativas\), 6 \(Mutações  Passivas\) ou 9 \(Outros\)

     gravar 09 \(Outras\);

OS3810\-B

__RN0500\-04__

__Campo IND\_CTA:__

Campo Indicador de Conta da SAFX2002\.

OS3810\-B

__RN0500\-05__

__Campo NÍVEL:__

Campo Nível da SAFX2002\.

OS3810\-B

__RN0500\-06__

__Campo COD\_CTA:__

Campo Código da Conta da SAFX2002\.

OS3810\-B

__RN0500\-07__

__Campo NOME\_CTA:__

Campo Descrição da Conta da SAFX2002\.

OS3810\-B

__RN0500\-08__

__Campo COD\_CTA\_REF:__

Buscar na tabela SAFX2101 o código da conta referencial associada ao código da conta gerada no campo 06\. Se existir mais de uma conta referencial \(ou seja, mais de um registro na SAFX2101\) para uma mesma conta contábil, gerar um registro 0500 para cada conta referencial encontrada\.

Somente deverá ser gravada a Conta Referencial parametrizada pela Empresa \(DE/PARA\) de acordo com a entidade responsável pelo Plano, ou seja, Receita Federal, SUSEP ou COSIF, dessa forma, a rotina deverá verificar a qual Plano a Conta Referencial pertence\.

Se a Conta Referencial pertencer a determinado Plano \(Entidade\) cujo Estabelecimento centralizador não está parametrizado, o campo será em branco\.

OS3810\-B

__RN0500\-09__

__Campo CNPJ\_EST:__

Verificar se a conta contábil está relacionada a um grupo que possua somente um Estabelecimento associado, se sim, trazer o conteúdo do campo CNPJ do Estabelecimento que está associado a esse grupo\. 

Caso contrário, deixar em branco\.

OS3810\-B

- __Registro 0900 – Composição das Receitas do Período – Receita Bruta e Demais Receitas__

__RNG\-0900__

Este registro deve ser gerado a partir da somatória dos valores de Receita Bruta e Demais Receitas, dos Registros do Bloco I, Contribuições Financeiras e Assemelhadas\.

Para cada registro a ser considerado na composição da receita total por cada bloco, deve ser atendida a sua respectiva regra geral de geração\. Os demais valores de receitas não brutas, devem ser recuperados através do item de menu:

Manutenção > Registro do Bloco 0 > Demais Receitas não Brutas \(0900\)\.

Registro de nível 2, ocorrência de 1 por arquivo e obrigatório somente se a escrituração for transmitida após o prazo regular de entrega, a partir de Janeiro de 2020\.

__Observações:__ Este registro deverá ser informado sempre que a escrituração original for transmitida após o prazo regular de entrega \(após o 10º dia útil do 2º mês subsequente ao período de apuração a que se refere a escrituração\)\.

MFS33912

__RN0900\-01__

Texto fixo “0900”

MFS33912

__RN0900\-02__

__REC\_TOTAL\_BLOCO\_A__

\-Receita total referente aos registros escriturados no Bloco A\.

MFS33912

__RN0900\-03__

__REC\_NRB\_BLOCO\_A__

\-Parcela da receita total escriturada no Bloco A \(Campo 02\), não classificada como receita bruta\.

MFS33912

__RN0900\-04__

__REC\_TOTAL\_BLOCO\_C__

\-Receita total referente aos registros escriturados no Bloco C\. 

MFS33912

__RN0900\-05__

__REC\_NRB\_BLOCO\_C__

\- Parcela da receita total escriturada no Bloco C \(Campo 04\), não classificada como receita bruta\.

MFS33912

__RN0900\-06__

__REC\_TOTAL\_BLOCO\_D__\- Receita total referente aos registros escriturados no Bloco D\.

MFS33912

__RN0900\-07__

__REC\_NRB\_BLOCO\_D__

\- Parcela da receita total escriturada no Bloco D \(Campo 06\), não classificada como receita bruta

MFS33912

__RN0900\-08__

__REC\_TOTAL\_BLOCO\_F__

\- Receita total referente aos registros escriturados no Bloco F

MFS33912

__RN0900\-09__

__REC\_NRB\_BLOCO\_F__

\- Parcela da receita total escriturada no Bloco F \(Campo 08\), não classificada como receita bruta

MFS33912

__RN0900\-10__

__REC\_TOTAL\_BLOCO\_I__

\- Receita total referente aos registros escriturados no Bloco I

Deverá ser gravado no campo 02 – VL\_REC o Valor da Receita das Operações do Período\. Essa informação deverá ser recuperada do campo “Valor Receita” da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período \(menu: Manutenção >> Operações do Período\) do módulo EFD\-Contribuições Financeira/Assemelhada\.

MFS33912

__RN0900\-11__

__REC\_NRB\_BLOCO\_I__

\- Parcela da receita total escriturada no Bloco I \(Campo 10\) não classificada como receita bruta

Preencher com o campo Bloco I da tela Demais Receitas não Brutas \(0900\)\.

MFS33912

__RN0900\-12__

__REC\_TOTAL\_BLOCO\_1__

\- Receita total referente aos registros escriturados no Bloco 1 \(RET\)

MFS33912

__RN0900\-13__

__REC\_NRB\_BLOCO\_1__

\- Parcela da receita total escriturada no Bloco 1 \(Campo 12\), não classificada como receita bruta

MFS33912

__RN0900\-14__

__REC\_TOTAL\_PERIODO__

\- Receita bruta total \(Campos 02, 04, 06, 08, 10 e 12\)

Preencher com o valor informado no campo 10\.

MFS33912

__RN0900\-15__

__REC\_TOTAL\_NRB\_PERÍODO__

\- Parcela da receita total escriturada \(Campo 14\), não classificada como receita bruta \(Soma dos Campos 03, 05, 07, 09, 11 e 13\)

Preencher com o valor informado no campo 11\.

MFS33912

- __Registro 0990 – Encerramento do Bloco 0__

__RNG\-0990__

Deve ser gerado um registro 0990 por arquivo\.

Registro de nível 1, ocorrência de 1 por arquivo e obrigatório\.

OS3810\-B

__RN0990\-02__

__Campo QTD\_LIN\_0:__

Quantidade de registros do Bloco 0\.

OS3810\-B

__Bloco A \- Documentos Fiscais \- Serviços \(ISS\)__

- __Registro A001 – Abertura Bloco A__

__RNG\-A001__

Deve ser gerado um registro A001 por arquivo\.

Registro de nível 1, ocorrência de 1 por arquivo e obrigatório\.

OS3810\-B

__RNA001\-02__

__Campo IND\_MOV__

Gerar fixo “1”\.

OS3810\-B

- __Registro A990 – Encerramento do Bloco A__

__RNG\-A990__

Deve ser gerado um registro A990 por arquivo\.

Registro de nível 1, ocorrência de 1 por arquivo e obrigatório\.

OS3810\-B

__RNA990\-02__

__Campo QTD\_LIN\_A:__

Quantidade de registros do Bloco A\.

OS3810\-B

__Bloco C \- Documentos Fiscais I – Mercadorias \(ICMS/IPI\)__

- __Registro C001 – Abertura Bloco C__

__RNG\-C001__

Deve ser gerado um registro C001 por arquivo\.

Registro de nível 1, ocorrência de 1 por arquivo e obrigatório\.

OS3810\-B

__RNC001\-02__

__Campo IND\_MOV__

Gerar fixo “1”\.

OS3810\-B

- __Registro C990 – Encerramento do Bloco C__

__RNG\-C990__

Deve ser gerado um registro C990 por arquivo\.

Registro de nível 1, ocorrência de 1 por arquivo e obrigatório\.

OS3810\-B

__RNC990\-02__

__Campo QTD\_LIN\_C:__

Quantidade de registros do Bloco C\.

OS3810\-B

__Bloco D \- Documentos Fiscais II – Serviços \(ICMS\)__

- __Registro D001 – Abertura Bloco D__

__RNG\-D001__

Deve ser gerado um registro D001 por arquivo\.

Registro de nível 1, ocorrência de 1 por arquivo e obrigatório\.

OS3810\-B

__RND001\-02__

__Campo IND\_MOV__

Gerar fixo “1”\.

OS3810\-B

- __Registro D990 – Encerramento do Bloco D__

__RNG\-D990__

Deve ser gerado um registro D990 por arquivo\.

Registro de nível 1, ocorrência de 1 por arquivo e obrigatório\.

OS3810\-B

__RND990\-02__

__Campo QTD\_LIN\_D:__

Quantidade de registros do Bloco D\.

OS3810\-B

__Bloco F \- Demais Documentos e Operações__

- __Registro F001 – Abertura Bloco F__

__RNG\-F001__

Deve ser gerado um registro F001 por arquivo\.

Registro de nível 1, ocorrência de 1 por arquivo e obrigatório\.

OS3810\-B

__RNF001\-02__

__Campo IND\_MOV__

Deverá ser gravado no campo 02 – IND\_MOV se esse registro possui informações ou não\.

- Gravar “0”, caso existam informações a serem demonstradas nos registros F600 ou F700\.
- Gravar “1”, caso não existam informações a serem demonstradas nos registros F600 ou F700\.

OS3810\-B

OS3810\-E

- __Registro F600 – Contribuição Retida na Fonte__

__RNG\-F600__

Gerar um registro F600 para cada registro informado através do módulo: EFD Contribuições Financeiras e Assemelhadas, menu: Manutenção >> Registro do Bloco F >> Contribuição Retida na Fonte \(F600\), que atenda ao critério abaixo:

Data de Pagamento: 

Entre a Data Inicial e Data Final de geração do arquivo ou anterior\.

O agrupamento dos registros deve ser feito de acordo com os campos chaves deste registro:

Indicador de Natureza da Retenção na Fonte \(Campo 02\)

Data da Pagamento \(Campo 14\)

Código da Receita \(Campo 04\)

Indicador da Natureza da Receita \(Campo 07\)

CNPJ \(Campo 08\)

OBS: a partir da OS3590 o agrupamento será a partir da Data de Pagamento e não mais da Data de Retenção\. A Data de Pagamento deverá sempre ser igual ou menor que a DT\_FIM do arquivo, gerado no registro 0000\.

OS3810\-D

__RNF600\-01__

No campo REG deverá ser gravado o texto fixo “F600”\.

OS3810\-D

__RNF600\-02__

No campo IND\_NAT\_REC deverá ser gravado o indicador da Natureza da Receita, de acordo com a informação selecionada no campo “Natureza da Retenção na Fonte” da tela “Nova Contribuição na Fonte \(F600\)”\.

- Gravar “01”, caso a opção seja “01 \- Retenção por Órgãos, Autarquias e Fundações Federais;
- Gravar “02”, caso a opção seja “02 \- Retenção por outras Entidades da Administração Pública Federal”;
- Gravar “03”, caso a opção seja “03 \- Retenção por Pessoas Jurídicas de Direito Privado”;
- Gravar “04”, caso a opção seja “04 \- Recolhimento por Sociedade Cooperativa”;
- Gravar “05”, caso a opção seja “05 \- Retenção por Fabricante de Máquinas e Veículos”;
- Gravar “99”, caso a opção seja “99 \- Outras Retenções”\.	

OS3810\-D

__RNF600\-03__

A data gerada nesse campo será a “Data de Pagamento” da SAFX145\.

OS3810\-D

__RNF600\-04__

Deverá ser gravado no campo VL\_BC\_RET, a informação contida no campo “Base de Cálculo Retenção ou Recolhimento” da tela “Nova Contribuição na Fonte \(F600\)”\.

OS3810\-D

__RNF600\-05__

Deverá ser gravado no campo VL\_RET, a informação contida no campo “Valor Total na Fonte/Recolhido” da tela “Nova Contribuição na Fonte \(F600\)”\.

OS3810\-D

__RNF600\-06__

Ao gerar o campo 06 – COD\_REC do registro F600, a informação deverá ser recuperada do campo “Código da Receita” \(12/SAFX145\) da tela de manutenção do registro F600 através do menu Manutenção >> Registro do Bloco F >> Contribuição Retida na Fonte \(F600\)\.

Deverão ser recuperados e gravados no arquivo os 4 \(quatro\) primeiros dígitos do Código de Receita\.

OS3810\-D

__RNF600\-07__

Deverá ser gravado no campo IND\_NAT\_REC, a informação contida no campo “Natureza da Receita” da tela “Nova Contribuição na Fonte \(F600\)”\.

- Gravar “0”, caso a opção seja “Não Cumulativa”
- Gravar “1”, caso a opção seja “Cumulativa”;

OS3810\-D

__RNF600\-08__

Deverá ser gravado no campo CNPJ, o CNPJ com 14 posições de acordo com o campo “Responsável/Beneficiário da Retenção” da tela “Nova Contribuição na Fonte \(F600\)”\.

OS3810\-D

__RNF600\-09__

Deverá ser gravado no campo VL\_RET\_PIS, a informação que estiver contida no campo “Valor Retido na Fonte – Parcela Referente ao PIS” da tela “Nova Contribuição na Fonte \(F600\)”\.

OS3810\-D

__RNF600\-10__

Deverá ser gravado no campo VL\_RET\_COFINS, a informação que estiver contida no campo “Valor Retido na Fonte – Parcela Referente ao COFINS” da tela “Nova Contribuição na Fonte \(F600\)”\.

OS3810\-D

__RNF600\-11__

Deverá ser gravado no campo IND\_REC, a informação que estiver contida no campo “Condição da PJ Declarante \(Ind\)” da tela “Nova Contribuição na Fonte \(F600\)”\.

- Gravar “0”, caso a opção seja “Beneficiária da Retenção / Recolhimento”
- Gravar “1”, caso a opção seja “Responsável da Retenção / Recolhimento”;

OS3810\-D

- __Registro F700 – Deduções Diversas__

__RNG\-F700__

Gerar um registro F700 para cada registro informado através do módulo: EFD\-Contribuições Financeira/Assemelhada, menu: Manutenção → Registro do Bloco F → Deduções Diversas, que atenda ao critério abaixo:

Competência: Igual a competência \(mês/ano\) da geração do arquivo\.

Empresa e Estabelecimento: igual a parametrizada para geração\. No caso de geração com estabelecimento centralizador, considerar dados de todos os centralizados\.

OS3810\-E

__RNF700\-01__

__Registro F700 \- 01 \- REG__

Deverá ser gravado no campo 01 – REG o texto fixo “F700”\.

OS3810\-E

__RNF700\-02__

__Registro F700 \- 02 \- IND\_ORI\_DED__

Será gravado o conteúdo do campo “Origem da Dedução” da SAFX193\.

OS3810\-E

__RNF700\-03__

__Registro F700 \- 03 \- IND\_NAT\_DED__

Será gravado o conteúdo do campo “Natureza da Dedução” da SAFX193, realizando a seguinte conversão:

Indicador da Natureza da Dedução = “N” \- Não Cumulativa, gera “0”;

Indicador da Natureza da Dedução = “C” \- Cumulativa, gera “1”;

OS3810\-E

__RNF700\-04__

__Registro F700 \- 04 \- VL\_DED\_PIS__

Será gravado o conteúdo do campo “Valor a Deduzir \- PIS” da SAFX193\.

OS3810\-E

__RNF700\-05__

__Registro F700 \- 05 \- VL\_DED\_COFINS__

Será gravado o conteúdo do campo “Valor a Deduzir – COFINS” da SAFX193\.

OS3810\-E

__RNF700\-06__

__Registro F700 \- 06 \- VL\_BC\_OPER__

Será gravado o conteúdo do campo “Valor da Base de Cálculo a deduzir PIS/PASEP – COFINS” da SAFX193\.

OS3810\-E

__RNF700\-07__

__Registro F700 \- 07 – CNPJ__

Será gravado o conteúdo do campo “CNPJ” da SAFX193\.

OS3810\-E

__RNF700\-08__

__Registro F700 \- 08 \- INF\_COMP__

Será gravado o conteúdo do campo “Informações complementares” da SAFX193\.

OS3810\-E

- __Registro F990 – Encerramento do Bloco F__

__RNG\-F990__

Deve ser gerado um registro F990 por arquivo\.

Registro de nível 1, ocorrência de 1 por arquivo e obrigatório\.

OS3810\-B

__RNF990\-02__

__Campo QTD\_LIN\_F:__

Quantidade de registros do Bloco F\.

OS3810\-B

__Bloco 1 \- Complemento da Escrituração – Controle de Saldos de Créditos e de Retenções, Operações Extemporâneas e Outras Informações__

- __Registro I001 – Abertura Bloco I__

# RNI001

As informações serão recuperadas da tela de Operações do Período do módulo EFD\-Contribuições Financeiras/Assemelhadas\.

Registro de nível 1, ocorrência de 1 por arquivo e obrigatório\.

OS3810\-B

# RNI001\-01

__Registro I001 – 01 – REG:__

Deverá ser gravado no campo 01 – REG o texto fixo “I001”\.

OS3810\-B

# RNI001\-02

__Registro I001 – 02 – IND\_MOV:__

Deverá ser gravado no campo 02 – IND\_MOV se esse registro possui informações ou não\.

- Gravar “0”, caso existam informações a serem recuperadas na tela de Operações do Período\.
- Gravar “1”, caso não existam informações a serem recuperadas na tela de Operações do Período\.

OS3810\-B

- __Registro I010 – Identificação da Pessoa Jurídica__

# RNI010

As informações do registro I010 deverão ser recuperadas do cadastro de Empresa/Estabelecimento \(menu: Preliminares >> Empresa/Estabelecimento\) do módulo Parâmetros\. 

- Caso o parâmetro “Multiempresa” não esteja selecionado, deverá ser recuperado o Estabelecimento que está selecionado\.
- Caso o parâmetro “Multiempresa” esteja selecionado, deverá ser recuperado o Estabelecimento Centralizador – estabelecimento informado como Centralizador no menu: Preliminares >> Centralização de Escrituração de Obrigações Federais do módulo Parâmetros\. Será recuperado o Estabelecimento Centralizador de acordo com a Empresa selecionada\.

Registro de nível 2, ocorrência de vários por arquivo e obrigatório\.

OS3810\-B

# RNI010\-01

__Registro I010 – 01 – REG__

Deverá ser gravado no campo 01 – REG o texto fixo “I010”\.

OS3810\-B

# RNI010\-02

__Registro I010 – 02 – CNPJ__

Deverá ser gravado no campo 02 – CNPJ o CNPJ da Pessoa Jurídica que está declarando a informação\. Essa informação deverá ser recuperada da seguinte forma:

- Caso o parâmetro “Multi\-Empresa” não esteja selecionado, deverá ser recuperado o CNPJ do Estabelecimento que está selecionado – ver campo CNPJ do cadastro de Empresa/Estabelecimento do módulo Parâmetros \(menu: Preliminares >> Empresa/Estabelecimento\)\.
- Caso o parâmetro “Multi\-Empresa” esteja selecionado, deverá ser recuperado o CNPJ do Estabelecimento Centralizador – estabelecimento informado como Centralizador no menu: Preliminares >> Centralização de Escrituração de Obrigações Federais do módulo Parâmetros\. Será recuperado o CNPJ de acordo com a Empresa selecionada  – ver campo CNPJ do cadastro de Empresa/Estabelecimento do módulo Parâmetros \(menu: Preliminares >> Empresa/Estabelecimento\)\.

OS3810\-B

# RNI010\-03

__Registro I010 – 03 – IND\_ATIV__

Deverá ser gravado no campo 03 – IND\_ATIV o tipo de Atividade do ramo Financeiro ou Assemelhado ao qual o Estabelecimento está enquadrado\. Essa informação deverá ser recuperada do campo “Tipo de Atividade Financeira” do cadastro de Empresa/Estabelecimento \(menu: Preliminares >> Empresa/Estabelecimento\) do módulo Parâmetros\.

A informação deverá ser gravada da seguinte maneira:

- Gravar “01” caso a opção selecionada seja “1 – Operações de Instituições Financeiras e Assemelhadas”;
- Gravar “02” caso a opção selecionada seja “2 – Operações de Seguros Privados”;
- Gravar “03” caso a opção selecionada seja “3 – Operações de Previdência Complementar”;
- Gravar “04” caso a opção selecionada seja “4 – Operações de Capitalização”;
- Gravar “05” caso a opção selecionada seja “5 – Operações de Planos de Assistência à Saúde”;
- Gravar “06” caso a opção selecionada seja “6 – Operações referentes a mais de um dos indicadores acima”\.

OS3810\-B

# RNI010\-04

__Registro I010 – 04 – INFO\_COMPL__

Deverá ser gravado no campo 04 – INFO\_COMPL a Informação Complementar do Estabelecimento\. Essa informação deverá ser recuperada do campo “Informação Complementar” do cadastro de Empresa/Estabelecimento \(menu: Preliminares >> Empresa/Estabelecimento\) do módulo Parâmetros\.

OS3810\-B

- __Registro I100 – Consolidação das Operações do Período__

# RNI100\-00

As informações do registro I100 deverão ser recuperadas da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período do módulo EFD\-Contribuições Financeiras/Assemelhadas\.

Registro de nível 3, para cada ocorrência do registro I010 podem existir “N” I100 e é obrigatório se houver\.

OS3810\-B

# RNI100\-01

__Registro I100 – 01 – REG__

Deverá ser gravado no campo 01 – REG o texto fixo “I100”\.

OS3810\-B

# RNI100\-02

__Registro I100 – 02 – VL\_REC__

Deverá ser gravado no campo 02 – VL\_REC o Valor da Receita das Operações do Período\. Essa informação deverá ser recuperada do campo “Valor Receita” da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período \(menu: Manutenção >> Operações do Período\) do módulo EFD\-Contribuições Financeira/Assemelhada\.

OS3810\-B

# RNI100\-03

__Registro I100 – 03 – CST\_PIS\_COFINS__

Deverá ser gravado no campo 03 – CST\_PIS\_COFINS o Código de Situação Tributária PIS ou COFINS das Operações do Período\. Essa informação deverá ser recuperada do campo “Cód\. Sit\. Trib\. PIS/COFINS” da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período \(menu: Manutenção >> Operações do Período\) do módulo EFD\-Contribuições Financeira/Assemelhada\.

OS3810\-B

# RNI100\-04

__Registro I100 – 04 – VL\_TOT\_DED\_GER__

Deverá ser gravado no campo 04 – VL\_TOT\_DED\_GER o Valor Total das Deduções e Exclusões de Caráter Geral\. Essa informação deverá ser recuperada do campo “Valor Total Ded\./Excl\. Caráter Geral” da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período \(menu: Manutenção >> Operações do Período\) do módulo EFD\-Contribuições Financeira/Assemelhada\.

OS3810\-B

# RNI100\-05

__Registro I100 – 05 – VL\_TOT\_DED\_ESP__

Deverá ser gravado no campo 05 – VL\_TOT\_DED\_ESP o Valor Total das Deduções e Exclusões de Caráter Específico\. Essa informação deverá ser recuperada do campo “Valor Total Ded\./Excl\. Caráter Específico” da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período \(menu: Manutenção >> Operações do Período\) do módulo EFD\-Contribuições Financeira/Assemelhada\.

OS3810\-B

# RNI100\-06

__Registro I100 – 06 – VL\_BC\_PIS__

Deverá ser gravado no campo 06 – VL\_BC\_PIS o Valor da Base de Cálculo do PIS\. Essa informação deverá ser recuperada do campo “Valor Base de Cálculo PIS” da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período \(menu: Manutenção >> Operações do Período\) do módulo EFD\-Contribuições Financeira/Assemelhada\.

OS3810\-B

# RNI100\-07

__Registro I100 – 07 – ALIQ\_PIS__

Deverá ser gravado no campo 07 – ALIQ\_PIS o Valor da Alíquota do PIS\. Essa informação deverá ser recuperada do campo “Alíquota PIS” da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período \(menu: Manutenção >> Operações do Período\) do módulo EFD\-Contribuições Financeira/Assemelhada\.

OS3810\-B

# RNI100\-08

__Registro I100 – 08 – VL\_PIS__

Deverá ser gravado no campo 08 – VL\_PIS o Valor do PIS\. Essa informação deverá ser recuperada do campo “Valor PIS” da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período \(menu: Manutenção >> Operações do Período\) do módulo EFD\-Contribuições Financeira/Assemelhada\.

OS3810\-B

# RNI100\-09

__Registro I100 – 09 – VL\_BC\_COFINS__

Deverá ser gravado no campo 09 – VL\_BC\_COFINS o Valor da Base de Cálculo do COFINS\. Essa informação deverá ser recuperada do campo “Valor Base de Cálculo COFINS” da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período \(menu: Manutenção >> Operações do Período\) do módulo EFD\-Contribuições Financeira/Assemelhada\.

OS3810\-B

# RNI100\-10

__Registro I100 – 10 – ALIQ\_COFINS__

Deverá ser gravado no campo 10 – ALIQ\_COFINS o Valor da Alíquota do COFINS\. Essa informação deverá ser recuperada do campo “Alíquota COFINS” da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período \(menu: Manutenção >> Operações do Período\) do módulo EFD\-Contribuições Financeira/Assemelhada\.

OS3810\-B

# RNI100\-11

__Registro I100 – 11 – VL\_COFINS__

Deverá ser gravado no campo 11 – VL\_COFINS o Valor do COFINS\. Essa informação deverá ser recuperada do campo “Valor COFINS” da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período \(menu: Manutenção >> Operações do Período\) do módulo EFD\-Contribuições Financeira/Assemelhada\.

OS3810\-B

# RNI100\-12

__Registro I100 – 12 – INFO\_COMPL__

Deverá ser gravado no campo 12 – INFO\_COMPL a Informação Complementar\. Essa informação deverá ser recuperada do campo “Inf\. Complementar” da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período \(menu: Manutenção >> Operações do Período\) do módulo EFD\-Contribuições Financeira/Assemelhada\.

OS3810\-B

- __Registro I200 – Composição das Receitas, Deduções e/ou Exclusões do Período__

# RNI200\-00

As informações do registro I200 deverão ser recuperadas da tela “Operações do Período” – aba: I200 – Composição das Receitas/Deduções/Exclusões do módulo EFD\-Contribuições Financeiras/Assemelhadas\.

Deverá ser desconsiderado o registro que tenha o campo 04 – DET\_VALOR com conteúdo igual a zero\.

Registro de nível 4, para cada ocorrência do registro I100 podem existir “N” I200 e é obrigatório se houver\.

OS3810\-B

CH5184/2014

# RNI200\-01

__Registro I200 – 01 – REG__

Deverá ser gravado no campo 01 – REG o texto fixo “I200”\.

OS3810\-B

# RNI200\-02

__Registro I200 – 02 – NUM\_CAMPO__

Deverá ser gravado no campo 02 – NUM\_CAMPO o Número do Campo referente à Composição das Receitas/Deduções/Exclusões\. A informação deverá ser gravada da seguinte forma:

- Gravar “02”, caso a opção selecionada seja “Valor da Receita”;
- Gravar “04”, caso a opção selecionada seja “Valor Total Ded\./Excl\. Caráter Geral”;
- Gravar “05”, caso a opção selecionada seja “Valor Total Ded\./Excl\. Caráter Específico”\.

OS3810\-B

# RNI200\-03

__Registro I200 – 03 – COD\_DET__

Deverá ser gravado no campo 03 – COD\_DET o Código de Detalhamento\. Essa informação deverá ser recuperada do campo “Código Receita/Dedução/Exclusão” da tela “Operações do Período” – aba: I200 – Composição das Receitas/Deduções/Exclusões \(menu: Manutenção >> Operações do Período\) do módulo EFD\-Contribuições Financeira/Assemelhada\.

OS3810\-B

# RNI200\-04 

__Registro I200 – 04 – DET\_VALOR__

Deverá ser gravado no campo 04 – DET\_VALOR o Detalhamento do Valor\. Essa informação deverá ser recuperada do campo “Valor Detalhado” da tela “Operações do Período” – aba: I200 – Composição das Receitas/Deduções/Exclusões \(menu: Manutenção >> Operações do Período\) do módulo EFD\-Contribuições Financeira/Assemelhada\.

OS3810\-B

# RNI200\-05

__Registro I200 – 05 – COD\_CTA__

Deverá ser gravado no campo 05 – COD\_CTA o Código da Conta Contábil\. Essa informação deverá ser recuperada do campo “Código Conta Contábil” da tela “Operações do Período” – aba: I200 – Composição das Receitas/Deduções/Exclusões \(menu: Manutenção >> Operações do Período\) do módulo EFD\-Contribuições Financeira/Assemelhada\.

O cadastro desta conta contábil deverá ser informado no registro 0500\.

OS3810\-B

# RNI200\-06

__Registro I200 – 06 – INFO\_COMPL__

Deverá ser gravado no campo 06 – INFO\_COMPL a Informação Complementar\. Essa informação deverá ser recuperada do campo “Informação Complementar” da tela “Operações do Período” – aba: I200 – Composição das Receitas/Deduções/Exclusões \(menu: Manutenção >> Operações do Período\) do módulo EFD\-Contribuições Financeira/Assemelhada\.

OS3810\-B

- __Registro I300 – Complemento das Operações – Detalhamento das Receitas, Deduções e/ou Exclusões do Período__

# NI300\-00

As informações do registro I300 deverão ser recuperadas da tela “Operações do Período” – aba: I300 – Complemento das Operações do módulo EFD\-Contribuições Financeiras/Assemelhadas\.

Deverá ser desconsiderado o registro que tenha o campo 03 – DET\_VALOR com conteúdo igual a zero\.

Registro de nível 5, para cada ocorrência do registro I200 podem existir “N” I300 e é obrigatório se houver\.

OS3810\-B

CH5184/2014

# RNI300\-01

__Registro I300 – 01 – REG__

Deverá ser gravado no campo 01 – REG o texto fixo “I300”\.

OS3810\-B

# RNI300\-02

__Registro I300 – 02 – COD\_COMP__

Deverá ser gravado no campo 02 – COD\_COMP o Código de Complemento\. Essa informação deverá ser recuperada do campo “Cód\. Complemento Receita/Dedução/Exclusão” da tela “Operações do Período” – aba: I300 – Complemento das Operações \(menu: Manutenção >> Operações do Período\) do módulo EFD\-Contribuições Financeira/Assemelhada\.

OS3810\-B

# RNI300\-03

__Registro I300 – 03 – DET\_VALOR__

Deverá ser gravado no campo 03 – DET\_VALOR o Valor Detalhado\. Essa informação deverá ser recuperada do campo “Valor Detalhado” da tela “Operações do Período” – aba: I300 – Complemento das Operações \(menu: Manutenção >> Operações do Período\) do módulo EFD\-Contribuições Financeira/Assemelhada\.

OS3810\-B

# RNI300\-04

__Registro I300 – 04 – COD\_CTA__

Deverá ser gravado no campo 04 – COD\_CTA o Código da Conta Contábil\. Essa informação deverá ser recuperada do campo “Cód\. Conta Contábil” da tela “Operações do Período” – aba: I300 – Complemento das Operações \(menu: Manutenção >> Operações do Período\) do módulo EFD\-Contribuições Financeira/Assemelhada\.

O cadastro desta conta contábil deverá ser informado no registro 0500\.

OS3810\-B

# RNI300\-05

__Registro I300 – 05 – INFO\_COMPL__

Deverá ser gravado no campo 05 – INFO\_COMPL a Informação Complementar\. Essa informação deverá ser recuperada do campo “Informação Complementar” da tela “Operações do Período” – aba: I300 – Complemento das Operações \(menu: Manutenção >> Operações do Período\) do módulo EFD\-Contribuições Financeira/Assemelhada\.

OS3810\-B

- __Registro I990 – Encerramento do Bloco I__

__RNG\-I990__

Deve ser gerado um registro I990 por arquivo\.

Registro de nível 1, ocorrência de 1 por arquivo e obrigatório\.

OS3810\-B

__RNI990\-02__

__Campo QTD\_LIN\_I:__

Quantidade de registros do Bloco I\.

OS3810\-B

__Bloco M \- Apuração da Contribuição e Crédito de PIS/PASEP e da COFINS__

- __Registro M001 – Abertura Bloco M__

__RNG\-M001__

Deve ser gerado um registro M001 por arquivo\.

Registro de nível 1, ocorrência de 1 por arquivo e obrigatório\.

OS3810\-B

__RNM001\-02__

__Campo IND\_MOV__

Gerar fixo “0”\.

OS3810\-B

- __Registro M200 – Consolidação da Contribuição para o PIS/PASEP do Período__

__RNG\-M200__

Deve ser gerado um registro M200 por arquivo, demonstrando o valor da contribuição apurada no período\.

Este registro será gerado com base nos valores apurados no registro filho M210, no registro F600 e F700 do mesmo período de apuração\. Se não existir um destes registros que o originam, ele será gerado com valores zerados\.

Para utilização e seleção dos valores informados nos Registros F600 e F700, as seguintes regras devem ser seguidas:

Se o parâmetro “Informar os Descontos/Deduções manualmente, nas telas de Apuração PIS/PASEP e COFINS”, estiver __desmarcado__ \(em dados iniciais\), realizar a ordem do desconto e deduções do valor da contribuição a recolher, conforme segue:

1\. Através da totalização das informações dos registros M210, obtem\-se o valor do campo 09 do registro M200\.

2\. Desse valor descontam\-se as deduções do período \(campo 04 do registro F700 quando o campo “03\- Indicador da Natureza da Dedução” for igual a “1”\)\.

3\. Se ainda restar contribuição a pagar, desconta\-se desse valor as retenções do período \(campo 09 do registro F600 quando o campo “07 – Indicador da Natureza da Receita” for igual a 1 e o campo “11 – Indicador da Condição da PJ Declarante” for igual a “0”\)\.

Obs\.: Os descontos/deduções da contribuição apurada listados acima devem ser feitos na sequência indicada, até que não reste contribuição a pagar, ou até que não restem mais créditos/retenções/deduções a descontar/deduzir\.

Se o parâmetro “Informar os Descontos/Deduções manualmente, nas telas de Apuração PIS/PASEP e COFINS” estiver __marcado__ \(em dados iniciais\):

Considerar apenas os descontos das deduções do período \(campo 04 do registro F700 quando o campo “03\- Indicador da Natureza da Dedução” for igual a “1”\)\.

Registro de nível 2, ocorrência de 1 por arquivo e obrigatório\.

OS3810\-B

OS3810\-E

__RNM200\-02__

__Campo VL\_TOT\_CONT\_NC\_PER:__

Gerar “0,00”\.

OS3810\-B

__RNM200\-03__

__Campo VL\_TOT\_CRED\_DESC:__

Gerar “0,00”\.

OS3810\-B

__RNM200\-04__

__Campo VL\_TOT\_CRED\_DESC\_ANT:__

Gerar “0,00”\.

OS3810\-B

__RNM200\-05__

__Campo VL\_TOT\_CONT\_NC\_DEV:__

Gerar “0,00”\.

OS3810\-B

__RNM200\-06__

__Campo VL\_RET\_NC:__

Gerar “0,00”\.

OS3810\-B

__RNM200\-07__

__Campo VL\_OUT\_DED\_NC:__

Gerar “0,00”\.

OS3810\-B

__RNM200\-08__

__Campo VL\_CONT\_NC\_REC:__

Gerar “0,00”\.

OS3810\-B

__RNM200\-09__

__Campo VL\_TOT\_CONT\_CUM\_PER:__

Este campo será resultado da soma dos valores lançados no campo 13 \- VL\_CONT\_PER dos registros M210 filhos deste registro\.

OS3810\-B

__RNM200\-10__

__Campo VL\_RET\_CUM:__

Observar a ordem para realização da utilização do valor da retenção informada na RNG\-M200\. Se o parâmetro “Informar os Descontos/Deduções manualmente, nas telas de Apuração PIS/PASEP e COFINS” estiver __desmarcado__ \(em dados iniciais\)

O valor do campo deve ser igual ao somatório do campo “09 – Valor Retido na Fonte\-PIS” do registro F600 quando o campo “07 – Indicador da Natureza da Receita” for igual a 1 e o campo “11 – Indicador da Condição da PJ Declarante” for igual a “0”\.

Se o parâmetro “Informar os Descontos/Deduções manualmente, nas telas de Apuração PIS/PASEP e COFINS” estiver __marcado__ \(em dados iniciais\)

O valor do campo deve será igual a zero, pois o valor será informado pelo usuário após a geração dos registros através das telas de “Retenção na Fonte PIS/PASEP Apurada no Período” ou “Retenções a Utilizar na Apuração”\.

OS3810\-B

OS3810\-E

__RNM200\-11__

__Campo VL\_OUT\_DED\_CUM:__

Observar a ordem para realização da utilização do valor da retenção informada na RNG\-M200\. O valor do campo deve ser igual ao somatório do campo “04 – Valor a Deduzir\-PIS” do registro F700 quando o campo “03 – Indicador da Natureza da Dedução” for igual a “1”

OS3810\-B

OS3810\-E

__RNM200\-12__

__Campo VL\_CONT\_CUM\_REC:__

Este campo será resultado do cálculo: \(Campo VL\_TOT\_CONT\_CUM\_PER __menos__ Campo VL\_RET\_CUM __menos__ Campo VL\_OUT\_DED\_CUM\)\.

OS3810\-B

__RNM200\-13__

__Campo VL\_TOT\_CONT\_REC:__

Este campo será resultado do cálculo: \(Campo VL\_CONT\_NC\_REC __mais__ Campo VL\_CONT\_CUM\_REC\)\.

OS3810\-B

- __Registro M210 – Detalhamento da Contribuição para o PIS/PASEP do Período__

__RNG\-M210__

Este registro será gerado com base nos valores demonstrados nos registros I100 gerados no período, cujo conteúdo do campo 03 \- CST\_PIS\_COFINS seja igual a “01”\. Ele será uma consolidação das informações por COD\_CONT e ALIQ\_PIS\.

Registro de nível 3, para cada ocorrência do registro M200 poderão existir “N” M210 por arquivo e obrigatório quando existir o M200\.

 

OS3810\-B

__RNM210\-02__

__Campo COD\_CONT:__

Fixar “51”\.

OS3810\-B

__RNM210\-03__

__Campo VL\_REC\_BRT:__

Este campo será resultado da soma dos valores lançados no campo 02 \- VL\_REC de todos os registros I100 do arquivo, cujo conteúdo do campo 03 \- CST\_PIS\_COFINS seja igual a “01”, considerando o agrupamento deste registro que é por COD\_CONT e ALIQ\_PIS\.

OS3810\-B

__RNM210\-04__

__Campo VL\_BC\_CONT:__

Este campo será resultado da soma dos valores lançados no campo 06 \- VL\_BC\_PIS de todos os registros I100 do arquivo, cujo conteúdo do campo 03 \- CST\_PIS\_COFINS seja igual a “01”, considerando o agrupamento deste registro que é por COD\_CONT e ALIQ\_PIS\.

OS3810\-B

__RNM210\-05__

__Campo ALIQ\_PIS:__

Neste campo será demonstrada a alíquota informada no campo 07 \- ALIQ\_PIS de todos os registros I100 do arquivo, cujo conteúdo do campo 03 \- CST\_PIS\_COFINS seja igual a “01”\.

OS3810\-B

__RNM210\-06__

__Campo QUANT\_BC\_PIS:__

Gerar nulo \(“||”\)\.

OS3810\-B

__RNM210\-07__

__Campo ALIQ\_PIS\_QUANT:__

Gerar nulo \(“||”\)\.

OS3810\-B

__RNM210\-08__

__Campo VL\_CONT\_APUR:__

Este campo será resultado do seguinte cálculo: Valor informado no campo VL\_BC\_CONT __multiplicado__ pelo resultado do cálculo __\(__valor do campo ALIQ\_PIS __dividido__ por 100__\)__

OS3810\-B

__RNM210\-09__

__Campo VL\_AJUS\_ACRES:__

Gerar “0,00”\.

OS3810\-B

__RNM210\-10__

__Campo VL\_AJUS\_REDUC:__

Gerar “0,00”\.

OS3810\-B

__RNM210\-11__

__Campo VL\_CONT\_DIFER:__

Gerar “0,00”\.

OS3810\-B

__RNM210\-12__

__Campo VL\_CONT\_DIFER\_ANT:__

Gerar “0,00”\.

OS3810\-B

__RNM210\-13__

__Campo VL\_CONT\_PER:__

Este campo será resultado do cálculo: \(Valor do campo VL\_CONT\_APUR __mais__ valor do campo VL\_AJUS\_ACRES __menos__ valor do campo VL\_AJUS\_REDUC __menos__ valor do campo VL\_CONT\_DIFER __mais__ valor do campo VL\_CONT\_DIFER\_ANT\)\.

OS3810\-B

- __Registro M350 – PIS/PASEP – Folha de Salários__

__RNM350__

Este registro será gerado com base nos lançamentos de Saldo \(Tabela: X02\_SALDOS\) e \(Tabela X80\_SALDOS\_CCUSTO caso o campo “Utiliza saldo por centro de custo” selecionado\. Conforme parametrização para “GERAÇÃO AUTOMÁTICA” 

Módulo: SPED 🡪 EFD – Contribuições Financeira Assemelhada 🡪 Menu: Parâmetros 🡪 Dados Iniciais 

Registro M350 – PIS/PASEP – Folha de Salários\. 

Obs: 

Quando ”Geração Automática” deverá gerar os registros na tela Folha de Salários \(M350\)\. 

Módulo: SPED 🡪 EFD – Contribuições Financeira Assemelhada 🡪 Menu: Obrigações 🡪 Manutenção 

Folha de Salários \(M350\)\.

__Campo Estabelecimento:__ Deverá mostrar o “Código” do estabelecimento Descentralizado ou Centralizador e “Descrição“ conforme parametrização:

Módulo: Básicos 🡪 Parâmetros 🡪 Menu: Preliminares 🡪 Centralização da Escrituração de Obrigações Federais

__Campo Período de Apuração:__ Deverá mostrar a “Data Inicial” parametrizada na Geração dos Registros:

Módulo: SPED 🡪 EFD Contribuições Financeira Assemelhada 🡪 Menu: Obrigações 🡪 Geração dos Registros\.

Registro de nível 2\.

Ocorrência 1 por arquivo\.

OS4322

__RNM350\-02__

__Campo VL\_TOT\_FOL:__

Ao executar a geração do Registro M350, o sistema irá recuperar todos os Lançamentos de saldo do cliente \(tabela: X02\_SALDOS\) e \(Tabela X80\_SALDOS\_CCUSTO caso o campo “Utiliza saldo por centro de custo” selecionado\), para o período solicitado, de acordo com a Parametrização por Foha de Salário \(M350\) para as contas associados ao indicador "Valor da Folha de Salários"\.

Definida no __Módulo: __SPED🡪 EFD – Contribuições Financeiras Assemelhadas

__Menu:__    Parâmetros 🡪 Parametrização Folha de Salários \(M350\)

Se a Natureza \(IND\_NATUREZA\) da Conta na SAFX2002 for igual a “0\. Compensação”, "1\. Ativo", "3\. Despesa", "5\. Mutações Ativas", "7\. Patrimônio Líquido" ou "8\. Custo", considerar:

Valor Total de Débito menos Valor Total de Crédito \(considerar SAFX02 e SAF80, considerando parametrização em Dados Iniciais\)\.

Se a Natureza \(IND\_NATUREZA\) da Conta na SAFX2002 for igual a "2\. Passivo", "4\. Receita", "6\. Mutações Passivas" ou "9\. Outros", considerar:

Valor Total de Crédito menos Valor Total de Débito \(considerar SAFX02 e SAF80, considerando parametrização em Dados Iniciais\)\.

Se o resultado do cálculo for negativo, demonstrar o valor zerado e retornar a mensagem: “Atenção, foi encontrado valor negativo\. A situação deverá ser revisada e corrigida”\.

Se período de encerramento __“Trimestral”, “Semestral” ou “Anual”__ na totalização de crédito menos débito desconsiderar o lançamento de encerramento\. \(Tabela: X01\_CONTABIL\) campo TIPO\_LANCTO = “E”\. 

__A REGRA ACIMA__ também será válida nos caso de __“Cisão”, “Fusão” ou “Incorporação”__, __OU SEJA__, na totalização de crédito menos débito deverá desconsiderar o lançamento de encerramento para os casos citados de “Situação Especial”, conforme __DATAS PARAMETRIZADAS__ no Menu: Preliminares >> Empresa/Estabelecimento do módulo Básico >> Parâmetros\. 

Caso houver “Situação Especial”, o período de encerramento parametrizado no Módulo: SPED🡪 EFD – Contribuições Financeiras Assemelhadas Menu: Parâmetros🡪 Dados Iniciais será desconsiderado\. 

Obs: Fica de responsabilidade do usuário, definir o período de geração do arquivo conforme data de “Situação Especial” \(Cisão, Fusão, Incorporação\) parametrizada\.

OS4322

__RNM350\-03__

__Campo VL\_EXC\_BC:__

Ao executar a geração do Registro M350, o sistema irá recuperar todos os Lançamentos de saldo do cliente \(tabela: X02\_SALDOS\) e \(Tabela X80\_SALDOS\_CCUSTO caso o campo “Utiliza saldo por centro de custo” selecionado\), para o período solicitado, de acordo com a Parametrização por Foha de Salário \(M350\) para as contas associados ao indicador "Valor das Exclusões a Base de Cálculo"\.

definida no __Módulo: __SPED🡪 EFD – Contribuições Financeiras Assemelhadas

__Menu:__    Parâmetros 🡪 Parametrização Folha de Salários \(M350\)

Se a Natureza \(IND\_NATUREZA\) da Conta na SAFX2002 for igual a “0\. Compensação”, "1\. Ativo", "3\. Despesa", "5\. Mutações Ativas", "7\. Patrimônio Líquido" ou "8\. Custo", considerar:

Valor Total de Débito menos Valor Total de Crédito \(considerar SAFX02 e SAF80, considerando parametrização em Dados Iniciais\)\.

Se a Natureza \(IND\_NATUREZA\) da Conta na SAFX2002 for igual a "2\. Passivo", "4\. Receita", "6\. Mutações Passivas" ou "9\. Outros", considerar:

Valor Total de Crédito menos Valor Total de Débito \(considerar SAFX02 e SAF80, considerando parametrização em Dados Iniciais\)\.

Se o resultado do cálculo for negativo, demonstrar o valor zerado e retornar a mensagem: “Atenção, foi encontrado valor negativo\. A situação deverá ser revisada e corrigida”\.

Se período de encerramento __“Trimestral”, “Semestral” ou “Anual”__ na totalização de crédito menos débito desconsiderar o lançamento de encerramento\. \(Tabela: X01\_CONTABIL\) campo TIPO\_LANCTO = “E”\. 

__A REGRA ACIMA__ também será válida nos caso de __“Cisão”, “Fusão” ou “Incorporação”__, __OU SEJA__, na totalização de crédito menos débito deverá desconsiderar o lançamento de encerramento para os casos citados de “Situação Especial”, conforme __DATAS PARAMETRIZADAS__ no Menu: Preliminares >> Empresa/Estabelecimento do módulo Básico >> Parâmetros\. 

Caso houver “Situação Especial”, o período de encerramento parametrizado no Módulo: SPED🡪 EFD – Contribuições Financeiras Assemelhadas Menu: Parâmetros🡪 Dados Iniciais será desconsiderado\. 

Obs: Fica de responsabilidade do usuário, definir o período de geração do arquivo conforme data de “Situação Especial” \(Cisão, Fusão, Incorporação\) parametrizada\.

OS4322

__RNM350\-04__

__Campo VL\_TOT\_BC:__

Este campo será o resultado do campo 02 \(VL\_TOT\_FOL\) – campo 03 \(VL\_EXC\_BC\)\.

Obs: Caso o campo VL\_EXC\_BC > que VL\_TOT\_FOL exibir a seguinte mensagem no log de geração: 

“Valor das Exclusões a Base de Cálculo é superior ao Valor Total da Folha de Salário”\.

OS4322

__RNM350\-05__

__Campo ALIQ\_PIS\_FOL:__

Este campo receberá o valor da Alíquota PIS conforme parametrização\.

__Módulo: __SPED🡪 EFD – Contribuições Financeiras Assemelhadas

__Menu:__    Parâmetros 🡪 Parametrização Folha de Salários \(M350\)

OS4322

__RNM350\-06__

__Campo VL\_TOT\_CONT\_FOL:__

Este campo será o resultado do cálculo: Campo 04\(VL\_TOT\_BC\) \* Campo 05\(ALIQ\_PIS\_FOL\)\.

OS4322

- __Registro M400 – Consolidação da Contribuição para o PIS/PASEP do Período__

__RNG\-M400__

Este registro será gerado com base na parametrização realizada na tela de Parametrização por Conta Contábil, considerando o agrupamento das informações por Código de Situação Tributária do PIS e Conta Contábil\. Ele só existirá quando o Código de Natureza da Receita da parametrização for diferente de nulo e o Código de Situação Tributária do PIS for igual a “06” ou “07” ou “08” ou “09”\.

Este registro é pai do M410\. No M410 as informações serão detalhadas por Natureza da Receita e Conta Contábil e aqui por CST e Conta Contábil, sendo que, a conta contábil aqui informada será a sintética das contas analíticas demonstradas no M410\.

Registro de nível 2, existirão vários por arquivo e obrigatório quando o Código de Situação Tributária do PIS for igual a “06” ou “07” ou “08” ou “09”\.

OS3810\-B

__RNM400\-02__

__Campo CST\_PIS:__

Campo Situação Tributária do PIS informada na parametrização\.

OS3810\-B

__RNM400\-03__

__Campo VL\_TOT\_REC:__

Este campo será a soma dos valores lançados no campo 03 \- VL\_REC do registro M410 que são filhos deste registro\.

OS3810\-B

__RNM400\-04__

__Campo COD\_CTA:__

Será gerado com o código da Conta Contábil do tipo “Sintética” de nível anterior à conta informada no registro filho M410\.

*Exemplo – Contas:*

*1\.00 \(sintética – nível 2\)*

*1\.00\.00 \(sintética – nível 3\)*

*1\.00\.00\.01 \(analítica – nível 4\)*

*1\.00\.00\.02 \(analítica – nível 4\)*

*1\.00\.00\.00\.01 \(analítica – nível 5\)*

*No registro filho, M410, estarão as contas analíticas\. Neste registro será gerada a conta sintética de nível anterior à conta informada no registro filho\. Sendo assim, com base no exemplo, será gerada a conta “1\.00\.00”\.*

O cadastro desta conta contábil deverá ser informado no registro 0500\.

OS3810\-B

__RNM400\-05__

__Campo DESC\_COMPL:__

Gerar nulo \(“||”\)\.

OS3810\-B

- __Registro M410 – Consolidação da Contribuição para o PIS/PASEP do Período__

__RNG\-M410__

Este registro será gerado com base na parametrização realizada na tela de Parametrização por Conta Contábil, considerando o agrupamento das informações por Código de Natureza da Receita e Conta Contábil\. Ele só existirá quando o Código de Natureza da Receita da parametrização for diferente de nulo e o Código de Situação Tributária do PIS for igual a “06” ou “07” ou “08” ou “09”\.

Serão considerados registros da tabela SAFX01 – Arquivo Contábil das Contas Contábeis parametrizadas cuja Data da Operação compreenda o período de geração do arquivo\.

__\[ALTERADA – CH23215\_2015\]__

Deverá ser desconsiderado o registro que tenha o campo 03 – VL\_REC com conteúdo igual a zero\.

Registro de nível 3, para cada ocorrência do registro M400 poderão existir “N” M410 por arquivo e obrigatório quando existir o M400\.

OS3810\-B

CH23215\_2015

__RNM410\-02__

__Campo NAT\_REC:__

Informar neste campo o Código de Natureza da Receita vinculado à parametrização\.

OS3810\-B

__RNM410\-03__

__Campo VL\_REC:__

Este campo será resultado do cálculo: __\(__soma do Valor do Lançamento Contábil de todos os lançamentos existentes para o período cujo Indicador de Débito/Crédito seja igual a “C”__\)__ __menos__ __\(__soma do Valor do Lançamento Contábil de todos os lançamentos existentes para o período cujo Indicador de Débito/Crédito seja igual a “D”__\)__\.

Mesmo que o resultado apurado seja negativo, deve ser apresentado o valor absoluto \(positivo\)\.

OS3810\-B

__RNM410\-04__

__Campo COD\_CTA:__

Informar neste campo a Conta Contábil vinculada à parametrização\.

O cadastro desta conta contábil deverá ser informado no registro 0500\.

OS3810\-B

__RNM410\-05__

__Campo DESC\_COMPL:__

Gerar nulo \(“||”\)\.

OS3810\-B

- __Registro M600 – Consolidação da Contribuição para o PIS/PASEP do Período__

__RNG\-M600__

Deve ser gerado um registro M600 por arquivo, demonstrando o valor da contribuição apurada no período\.

Este registro será gerado com base nos valores apurados no registro filho M610, no registro F600 e F700 do mesmo período de apuração\. Se não existir um destes registros que o originam, ele será gerado com valores zerados\.

Para utilização e seleção dos valores informados nos Registros F600 e F700, as seguintes regras devem ser seguidas:

Se o parâmetro “Informar os Descontos/Deduções manualmente, nas telas de Apuração PIS/PASEP e COFINS”, estiver __desmarcado__ \(em dados iniciais\), realizar a ordem do desconto e deduções do valor da contribuição a recolher, conforme segue:

1\. Através da totalização das informações dos registros M610, obtem\-se o valor do campo 09 do registro M600\.

2\. Desse valor descontam\-se as deduções do período \(campo 05 do registro F700 quando o campo “03\- Indicador da Natureza da Dedução” for igual a “1”\)\.

3\. Se ainda restar contribuição a pagar, desconta\-se desse valor as retenções do período \(campo 10 do registro F600 quando o campo “07 – Indicador da Natureza da Receita” for igual a 1 e o campo “11 – Indicador da Condição da PJ Declarante” for igual a “0”\)\.

Obs\.: Os descontos/deduções da contribuição apurada listados acima devem ser feitos na sequência indicada, até que não reste contribuição a pagar, ou até que não restem mais créditos/retenções/deduções a descontar/deduzir\.

Se o parâmetro “Informar os Descontos/Deduções manualmente, nas telas de Apuração PIS/PASEP e COFINS” estiver __marcado__ \(em dados iniciais\):

Considerar apenas os descontos das deduções do período \(campo 05 do registro F700 quando o campo “03\- Indicador da Natureza da Dedução” for igual a “1”\)\.

Registro de nível 2, ocorrência de 1 por arquivo e obrigatório\.

OS3810\-B

OS3810\-E

__RNM600\-02__

__Campo VL\_TOT\_CONT\_NC\_PER:__

Gerar “0,00”\.

OS3810\-B

__RNM600\-03__

__Campo VL\_TOT\_CRED\_DESC:__

Gerar “0,00”\.

OS3810\-B

__RNM600\-04__

__Campo VL\_TOT\_CRED\_DESC\_ANT:__

Gerar “0,00”\.

OS3810\-B

__RNM600\-05__

__Campo VL\_TOT\_CONT\_NC\_DEV:__

Gerar “0,00”\.

OS3810\-B

__RNM600\-06__

__Campo VL\_RET\_NC:__

Gerar “0,00”\.

OS3810\-B

__RNM600\-07__

__Campo VL\_OUT\_DED\_NC:__

Gerar “0,00”\.

OS3810\-B

__RNM600\-08__

__Campo VL\_CONT\_NC\_REC:__

Gerar “0,00”\.

OS3810\-B

__RNM600\-09__

__Campo VL\_TOT\_CONT\_CUM\_PER:__

Este campo será resultado da soma dos valores lançados no campo 13 \- VL\_CONT\_PER dos registros M610 filhos deste registro\.

OS3810\-B

__RNM600\-10__

__Campo VL\_RET\_CUM:__

Observar a ordem para realização da utilização do valor da retenção informada na RNG\-M600\. Se o parâmetro “Informar os Descontos/Deduções manualmente, nas telas de Apuração PIS/PASEP e COFINS” estiver __desmarcado__ \(em dados iniciais\)

O valor do campo deve ser igual ao somatório do campo “10 – Valor Retido na Fonte\-COFINS” do registro F600 quando o campo “07 – Indicador da Natureza da Receita” for igual a 1 e o campo “11 – Indicador da Condição da PJ Declarante” for igual a “0”\.

Se o parâmetro “Informar os Descontos/Deduções manualmente, nas telas de Apuração PIS/PASEP e COFINS” estiver __marcado__ \(em dados iniciais\)

O valor do campo deve será igual a zero, pois o valor será informado pelo usuário após a geração dos registros através das telas de “Retenção na Fonte COFINS Apurada no Período” ou “Retenções a Utilizar na Apuração”\.

OS3810\-B

OS3810\-E

__RNM600\-11__

__Campo VL\_OUT\_DED\_CUM:__

Observar a ordem para realização da utilização do valor da retenção informada na RNG\-M600\. O valor do campo deve ser igual ao somatório do campo “05 – Valor a Deduzir\-COFINS” do registro F700 quando o campo “03 – Indicador da Natureza da Dedução” for igual a “1”

OS3810\-B

OS3810\-E

__RNM600\-12__

__Campo VL\_CONT\_CUM\_REC:__

Este campo será resultado do cálculo: \(Campo VL\_TOT\_CONT\_CUM\_PER __menos__ Campo VL\_RET\_CUM __menos__ Campo VL\_OUT\_DED\_CUM\)\.

OS3810\-B

__RNM600\-13__

__Campo VL\_TOT\_CONT\_REC:__

Este campo será resultado do cálculo: \(Campo VL\_CONT\_NC\_REC __mais__ Campo VL\_CONT\_CUM\_REC\)\.

OS3810\-B

- __Registro M610 – Detalhamento da Contribuição para o PIS/PASEP do Período__

__RNG\-M610__

Este registro será gerado com base nos valores demonstrados nos registros I100 gerados no período, cujo conteúdo do campo 03 \- CST\_PIS\_COFINS seja igual a “01”\. Ele será uma consolidação das informações por COD\_CONT e ALIQ\_COFINS\.

Registro de nível 3, para cada ocorrência do registro M600 poderão existir “N” M610 por arquivo e obrigatório quando existir o M600\.

OS3810\-B

__RNM610\-02__

__Campo COD\_CONT:__

Fixar “51”\.

OS3810\-B

__RNM610\-03__

__Campo VL\_REC\_BRT:__

Este campo será resultado da soma dos valores lançados no campo 02 \- VL\_REC de todos os registros I100 do arquivo, cujo conteúdo do campo 03 \- CST\_PIS\_COFINS seja igual a “01”, considerando o agrupamento deste registro que é por COD\_CONT e ALIQ\_COFINS\.

OS3810\-B

__RNM610\-04__

__Campo VL\_BC\_CONT:__

Este campo será resultado da soma dos valores lançados no campo 09 \- VL\_BC\_COFINS de todos os registros I100 do arquivo, cujo conteúdo do campo 03 \- CST\_PIS\_COFINS seja igual a “01”, considerando o agrupamento deste registro que é por COD\_CONT e ALIQ\_COFINS\.

OS3810\-B

__RNM610\-05__

__Campo ALIQ\_COFINS:__

Neste campo será demonstrada a alíquota informada no campo 10 \- ALIQ\_COFINS de todos os registros I100 do arquivo, cujo conteúdo do campo 03 \- CST\_PIS\_COFINS seja igual a “01”\.

OS3810\-B

__RNM610\-06__

__Campo QUANT\_BC\_COFINS:__

Gerar nulo \(“||”\)\.

OS3810\-B

__RNM610\-07__

__Campo ALIQ\_COFINS\_QUANT:__

Gerar nulo \(“||”\)\.

OS3810\-B

__RNM610\-08__

__Campo VL\_CONT\_APUR:__

Este campo será resultado do seguinte cálculo: Valor informado no campo VL\_BC\_CONT multiplicado pelo resultado do cálculo \(valor do campo ALIQ\_COFINS dividido por 100\)

OS3810\-B

__RNM610\-09__

__Campo VL\_AJUS\_ACRES:__

Gerar “0,00”\.

OS3810\-B

__RNM610\-10__

__Campo VL\_AJUS\_REDUC:__

Gerar “0,00”\.

OS3810\-B

__RNM610\-11__

__Campo VL\_CONT\_DIFER:__

Gerar “0,00”\.

OS3810\-B

__RNM610\-12__

__Campo VL\_CONT\_DIFER\_ANT:__

Gerar “0,00”\.

OS3810\-B

__RNM610\-13__

__Campo VL\_CONT\_PER:__

Este campo será resultado do cálculo: \(Valor do campo VL\_CONT\_APUR __mais__ valor do campo VL\_AJUS\_ACRES __menos__ valor do campo VL\_AJUS\_REDUC __menos__ valor do campo VL\_CONT\_DIFER __mais__ valor do campo VL\_CONT\_DIFER\_ANT\)\.

OS3810\-B

- __Registro M800 – Consolidação da Contribuição para o PIS/PASEP do Período__

__RNG\-M800__

Este registro será gerado com base na parametrização realizada na tela de Parametrização por Conta Contábil, considerando o agrupamento das informações por Código de Situação Tributária da COFINS e Conta Contábil\. Ele só existirá quando o Código de Natureza da Receita da parametrização for diferente de nulo e o Código de Situação Tributária da COFINS for igual a “06” ou “07” ou “08” ou “09”\.

Este registro é pai do M810\. No M810 as informações serão detalhadas por Natureza da Receita e Conta Contábil e aqui por CST e Conta Contábil, sendo que, a conta contábil aqui informada será a sintética das contas analíticas demonstradas no M810\.

Registro de nível 2, existirão vários por arquivo e obrigatório quando o Código de Situação Tributária da COFINS for igual a “06” ou “07” ou “08” ou “09”\.

OS3810\-B

__RNM800\-02__

__Campo CST\_COFINS:__

Campo Situação Tributária da COFINS informada na parametrização\.

OS3810\-B

__RNM800\-03__

__Campo VL\_TOT\_REC:__

Este campo será a soma dos valores lançados no campo 03 \- VL\_REC do registro M810 que são filhos deste registro\.

OS3810\-B

__RNM800\-04__

__Campo COD\_CTA:__

Será gerado com o código da Conta Contábil do tipo “Sintética” de nível anterior à conta informada no registro filho M810\.

*Exemplo – Contas:*

*1\.00 \(sintética – nível 2\)*

*1\.00\.00 \(sintética – nível 3\)*

*1\.00\.00\.01 \(analítica – nível 4\)*

*1\.00\.00\.02 \(analítica – nível 4\)*

*1\.00\.00\.00\.01 \(analítica – nível 5\)*

*No registro filho, M810, estarão as contas analíticas\. Neste registro será gerada a conta sintética de nível anterior à conta informada no registro filho\. Sendo assim, com base no exemplo, será gerada a conta “1\.00\.00”\.*

O cadastro desta conta contábil deverá ser informado no registro 0500\.

OS3810\-B

__RNM800\-05__

__Campo DESC\_COMPL:__

Gerar nulo \(“||”\)\.

OS3810\-B

- __Registro M810 – Consolidação da Contribuição para o PIS/PASEP do Período__

__RNG\-M810__

Este registro será gerado com base na parametrização realizada na tela de Parametrização por Conta Contábil, considerando o agrupamento das informações por Código de Natureza da Receita e Conta Contábil\. Ele só existirá quando o Código de Natureza da Receita da parametrização for diferente de nulo e o Código de Situação Tributária do PIS for igual a “06” ou “07” ou “08” ou “09”\.

Serão considerados registros da tabela SAFX01 – Arquivo Contábil das Contas Contábeis parametrizadas cuja Data da Operação compreenda o período de geração do arquivo\.

__\[ALTERADA – CH23215\_2015\]__

Deverá ser desconsiderado o registro que tenha o campo 03 – VL\_REC com conteúdo igual a zero\.

Registro de nível 3, para cada ocorrência do registro M800 poderão existir “N” M810 por arquivo e obrigatório quando existir o M800\.

OS3810\-B

CH23215\_2015

__RNM810\-02__

__Campo NAT\_REC:__

Informar neste campo o Código de Natureza da Receita vinculado à parametrização\.

OS3810\-B

__RNM810\-03__

__Campo VL\_REC:__

Este campo será resultado do cálculo: \(soma do Valor do Lançamento Contábil de todos os lançamentos existentes para o período cujo Indicador de Débito/Crédito seja igual a “C”\) __menos__ \(soma do Valor do Lançamento Contábil de todos os lançamentos existentes para o período cujo Indicador de Débito/Crédito seja igual a “D”\)\.

Mesmo que o resultado apurado seja negativo, deve ser apresentado o valor absoluto \(positivo\)\.

OS3810\-B

__RNM810\-04__

__Campo COD\_CTA:__

Informar neste campo a Conta Contábil vinculada à parametrização\.

O cadastro desta conta contábil deverá ser informado no registro 0500\.

OS3810\-B

__RNM810\-05__

__Campo DESC\_COMPL:__

Gerar nulo \(“||”\)\.

OS3810\-B

- __Registro M990 – Encerramento do Bloco M__

__RNG\-M990__

Deve ser gerado um registro M990 por arquivo\.

Registro de nível 1, ocorrência de 1 por arquivo e obrigatório\.

OS3810\-B

__RNM990\-02__

__Campo QTD\_LIN\_M:__

Quantidade de registros do Bloco P\.

OS3810\-B

__Bloco P \- Apuração da Contribuição Previdenciária sobre a Receita Bruta__

- __Registro P001 – Abertura Bloco P__

__RNG\-P001__

Deve ser gerado um registro P001 por arquivo\.

Registro de nível 1, ocorrência de 1 por arquivo e obrigatório\.

OS3810\-B

__RNP001\-02__

__Campo IND\_MOV__

Gerar fixo “1”\.

OS3810\-B

- __Registro P990 – Encerramento do Bloco P__

__RNG\-P990__

Deve ser gerado um registro P990 por arquivo\.

Registro de nível 1, ocorrência de 1 por arquivo e obrigatório\.

OS3810\-B

__RNP990\-02__

__Campo QTD\_LIN\_P:__

Quantidade de registros do Bloco P\.

OS3810\-B

__Bloco 1 \- Complemento da Escrituração – Controle de Saldos de Créditos e de Retenções, Operações Extemporâneas e Outras Informações__

- __Registro 1001 – Abertura Bloco I__

# RN1001

Deve ser gerado um registro 1001 por arquivo\.

Registro de nível 1, ocorrência de 1 por arquivo e obrigatório\.

OS3810\-E

# RN1001\-01

__Campo IND\_MOV__

Deverá ser gravado no campo 02 – IND\_MOV se esse registro possui informações ou não\.

- Gravar “0”, caso existam informações a serem demonstradas nos registros 1300 ou 1700\.
- Gravar “1”, caso não existam informações a serem demonstradas nos registros 1300 ou 1700\.

OS3810\-E

- __Registro 1300 – Controle dos Valores Retidos na Fonte – PIS/Pasep__

__RNG\-1300__

Este registro tem por objetivo realizar o controle dos saldos de valores retidos na fonte de períodos anteriores ao da atual escrituração, bem como totalizar os respectivos valores retidos no atual período da escrituração e que foram devidamente detalhados no registro F600, que atendam os critérios:

Se for retenção na fonte da escrituração atual:

No registro F600, o campo VL\_RET\_PIS esteja preenchido\.

Se for uma Retenção na Fonte da Escrituração Períodos Anterior:

- Somente as retenções na fonte que estejam com o __valor maior que zero__ no campo ‘’Retenção Disponível’’ apresentada na tela, localizada no módulo: SPED → EFD\-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – PIS/PASEP → Retenções Disponíveis
- Demonstrar os créditos disponíveis cujo Mês/Ano seja menor que DT\_FIN do registro 0000\.

O agrupamento desse registro deve ser feito com base das informações dos seguintes campos:

02 – Indicador de Natureza da Retenção na Fonte \(IND\_NAT\_RET\)

03 – Período do Recebimento e da Retenção \(PR\_REC\_RET\)

OS3810\-E

__RN1300\-01__

__Registro 1300 \- 01 \- REG__

Deverá ser gravado no campo 01 – REG o texto fixo “1300”\.

OS3810\-E

__RN1300\-02__

__Registro 1300 \- 02 \- IND\_NAT\_RET__

Se for retenção na fonte da escrituração atual:

Neste campo deve ser recuperado o dado do campo IND\_NAT\_RET do registro F600, considerando as restrições da regra __RNG\-1300__

Se for uma Retenção na Fonte da Escrituração de Períodos Anterior:

Neste campo deve ser recuperado o dado informado no campo ‘’Natureza da Retenção na Fonte’’ na tela, localizada no Módulo: SPED → EFD\-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – PIS/PASEP → Retenções Disponíveis, considerando as restrições da regra __RNG\-1300__\.

OS3810\-E

__RN1300\-03__

__Registro 1300 \- 03 \- PR\_REC\_RET__

Se for retenção na fonte da escrituração atual:

Esse campo deve ser preenchido com o mês/ano do campo Data do recebimento e retenção, considerando as restrições definidas na regra__ __geral__ RNG 1300\.__

Se for uma Retenção na Fonte da Escrituração de Períodos Anterior:

Neste campo deve ser recuperado o dado informado no campo ‘’Mês/Ano’’ na tela, localizada no Módulo: SPED → EFD\-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – PIS/PASEP → Retenções Disponíveis, considerando as restrições da regra __RNG\-1300__\.

OS3810\-E

__RN1300\-04__

__Registro 1300 \- 04 \- VL\_RET\_APU__

Se for retenção na fonte da escrituração atual:

Esse campo deve ser preenchido com a somatória do campo VL\_RET\_PIS do registro F600\.

Se for uma Retenção na Fonte da Escrituração de Períodos Anterior:

Esse campo deve preenchido com o resultado da somatória do campo ‘’Retenção Apurada’’ na tela, localizada: Módulo: SPED → EFD\-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – PIS/PASEP → Retenções Disponíveis, considerando as restrições da regra __RNG\-1300__\.

OS3810\-E

__RN1300\-05__

__Registro 1300 \- 05 \- VL\_RET\_DED__

Se for retenção na fonte da escrituração atual:

Esse campo deve ser preenchido com a retenção na fonte gerada no registro F600, que foi utilizada na dedução da contribuição, conforme a regra RNG do registro M200, considerando a restrição da regra __RNG 1300__\. 

Se for uma Retenção na Fonte da Escrituração de Períodos Anterior:

Esse campo deve ser preenchido com o resultado da somatória do valor dos campos ‘__’Retenção Deduzida na Contribuição’’__ apresentada na parte __Retenção\(s\) Disponível\(s\) __e na parte __Retenção\(s\) a ser Utilizada\(s\) no Período__ na tela do módulo abaixo, considerando as restrições da regra __RNG\-1300__\.

SPED → EFD\-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – PIS/PASEP → Retenções a Utilizar na Apuração\.

OS3810\-E

__RN1300\-06__

__Registro 1300 \- 06 \- VL\_RET\_PER__

Se for retenção na fonte da escrituração atual:

Deve ser preenchido com zeros “0,00’’

Se for uma Retenção na Fonte da Escrituração de Períodos Anterior:

Esse campo deve ser preenchido com a somatória do valor dos campos ‘‘Retenção Utilizada por Pedido de Restituição ’’ apresentado na parte __Retenção\(s\) Disponível\(s\) __e na parte __Retenção\(s\) a ser Utilizada\(s\) no Período __na tela do módulo abaixo, considerando as restrições da regra __RNG\-1300__\. 

SPED → EFD\-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – PIS/PASEP → Retenções a Utilizar na Apuração\. 

OS3810\-E

__RN1300\-07__

__Registro 1300 \- 07 \- VL\_RET\_DCOMP__

Se for retenção na fonte da escrituração atual:

Deve ser preenchido com zeros “0\.00’’

Se for uma Retenção na Fonte da Escrituração de Períodos Anterior:

Esse campo deve ser preenchido com o valor informado no campo ‘’Retenção Utilizada por Declaração da Compensação’’, apresentado parte __Retenção\(s\) Disponível\(s\) __e__ __na parte __Retenção\(s\) a ser Utilizada\(s\) no Período __na tela do módulo abaixo, considerando as restrições da regra __RNG\-1300__\. 

SPED → EFD\-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – PIS/PASEP → Retenções a Utilizar na Apuração, considerando as restrições da regra __RNG\-1300__\.

OS3810\-E

__RN1300\-08__

__Registro 1300 \- 08 \- SLD\_RET__

Esse campo deve ser igual 04\-VL\_RET\_APU __menos__ 05\-VL\_RET\_DED __menos __06\-VL\_RET\_PER __menos __07__\-__VL\_RET\_DCOMP\.

OS3810\-E

- __Registro 1700 – Controle dos Valores Retidos na Fonte – COFINS__

__RNG\-1700__

Este registro tem por objetivo realizar o controle dos saldos de valores retidos na fonte de períodos anteriores ao da atual escrituração, bem como totalizar os respectivos valores retidos no atual período da escrituração e que foram devidamente detalhados no registro F600, que atendam os critérios:

Se for retenção na fonte da escrituração atual:

No registro F600, o campo VL\_RET\_COFINS esteja preenchido\.

Se for uma Retenção na Fonte da Escrituração Períodos Anterior:

- Somente as retenções na fonte que estejam com o __valor maior que zero__ no campo ‘’Retenção Disponível’’ apresentada na tela, localizada no módulo: SPED → EFD\-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – COFINS → Retenções Disponíveis
- Demonstrar os créditos disponíveis cujo Mês/Ano seja menor que DT\_FIN do registro 0000\.

O agrupamento desse registro deve ser feito com base das informações dos seguintes campos:

02 – Indicador de Natureza da Retenção na Fonte \(IND\_NAT\_RET\)

03 – Período do Recebimento e da Retenção \(PR\_REC\_RET\)

OS3810\-E

__RN1700\-01__

__Registro 1700 \- 01 \- REG__

Deverá ser gravado no campo 01 – REG o texto fixo “1700”\.

OS3810\-E

__RN1700\-02__

__Registro 1700 \- 02 \- IND\_NAT\_RET__

Se for retenção na fonte da escrituração atual:

Neste campo deve ser recuperado o dado do campo IND\_NAT\_RET do registro F600, considerando as restrições da regra __RNG\-1700__

Se for uma Retenção na Fonte da Escrituração de Períodos Anterior:

Neste campo deve ser recuperado o dado informado no campo ‘’Natureza da Retenção na Fonte’’ na tela, localizada no Módulo: SPED → EFD\-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – COFINS → Retenções Disponíveis, considerando as restrições da regra __RNG\-1700__\.

OS3810\-E

__RN1700\-03__

__Registro 1700 \- 03 \- PR\_REC\_RET__

Se for retenção na fonte da escrituração atual:

Esse campo deve ser preenchido com o mês/ano do campo Data do recebimento e retenção, considerando as restrições definidas na regra__ __geral__ RNG 1700\.__

Se for uma Retenção na Fonte da Escrituração de Períodos Anterior:

Neste campo deve ser recuperado o dado informado no campo ‘’Mês/Ano’’ na tela, localizada no Módulo: SPED → EFD\-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – COFINS → Retenções Disponíveis, considerando as restrições da regra __RNG\-1700__\.

OS3810\-E

__RN1700\-04__

__Registro 1700 \- 04 \- VL\_RET\_APU__

Se for retenção na fonte da escrituração atual:

Esse campo deve ser preenchido com a somatória do campo VL\_RET\_COFINS do registro F600\.

Se for uma Retenção na Fonte da Escrituração de Períodos Anterior:

Esse campo deve preenchido com o resultado da somatória do campo ‘’Retenção Apurada’’ na tela, localizada: Módulo: SPED → EFD\-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – COFINS → Retenções Disponíveis, considerando as restrições da regra __RNG\-1700__\.

OS3810\-E

__RN1700\-05__

__Registro 1700 \- 05 \- VL\_RET\_DED__

Se for retenção na fonte da escrituração atual:

Esse campo deve ser preenchido com a retenção na fonte gerada no registro F600, que foi utilizada na dedução da contribuição, conforme a regra RNG do registro M200, considerando a restrição da regra __RNG 1700__\. 

Se for uma Retenção na Fonte da Escrituração de Períodos Anterior:

Esse campo deve ser preenchido com o resultado da somatória do valor dos campos ‘__’Retenção Deduzida na Contribuição’’__ apresentada na parte __Retenção\(s\) Disponível\(s\) __e na parte __Retenção\(s\) a ser Utilizada\(s\) no Período__ na tela do módulo abaixo, considerando as restrições da regra __RNG\-1700__\.

SPED → EFD\-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – COFINS → Retenções a Utilizar na Apuração\.

OS3810\-E

__RN1700\-06__

__Registro 1700 \- 06 \- VL\_RET\_PER__

Se for retenção na fonte da escrituração atual:

Deve ser preenchido com zeros “0,00’’

Se for uma Retenção na Fonte da Escrituração de Períodos Anterior:

Esse campo deve ser preenchido com a somatória do valor dos campos ‘‘Retenção Utilizada por Pedido de Restituição ’’ apresentado na parte __Retenção\(s\) Disponível\(s\) __e na parte __Retenção\(s\) a ser Utilizada\(s\) no Período __na tela do módulo abaixo, considerando as restrições da regra __RNG\-1700__\. 

SPED → EFD\-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – COFINS → Retenções a Utilizar na Apuração\. 

OS3810\-E

__RN1700\-07__

__Registro 1700 \- 07 \- VL\_RET\_DCOMP__

Se for retenção na fonte da escrituração atual:

Deve ser preenchido com zeros “0\.00’’

Se for uma Retenção na Fonte da Escrituração de Períodos Anterior:

Esse campo deve ser preenchido com o valor informado no campo ‘’Retenção Utilizada por Declaração da Compensação’’, apresentado parte __Retenção\(s\) Disponível\(s\) __e__ __na parte __Retenção\(s\) a ser Utilizada\(s\) no Período __na tela do módulo abaixo, considerando as restrições da regra __RNG\-1700__\. 

SPED → EFD\-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – COFINS → Retenções a Utilizar na Apuração, considerando as restrições da regra __RNG\-1700__\.

OS3810\-E

__RN1700\-08__

__Registro 1700 \- 08 \- SLD\_RET__

Esse campo deve ser igual 04\-VL\_RET\_APU __menos__ 05\-VL\_RET\_DED __menos __06\-VL\_RET\_PER __menos __07__\-__VL\_RET\_DCOMP\.

OS3810\-E

- __Registro 1990 – Encerramento do Bloco P__

__RNG\-P990__

Deve ser gerado um registro 1990 por arquivo\.

Registro de nível 1, ocorrência de 1 por arquivo e obrigatório\.

OS3810\-E

__RNP990\-02__

__Campo QTD\_LIN\_1:__

Quantidade de registros do Bloco 1\.

OS3810\-E

Bloco 9 \- Controle e Encerramento do Arquivo Digital

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

