# MTZ_DUB_RJ_Calculo_Beneficios

- **Fonte:** MTZ_DUB_RJ_Calculo_Beneficios.docx
- **Modificado:** 2021-06-04
- **Tamanho:** 123 KB

---

THOMSON REUTERS

Módulo DUB\-RJ

__Cálculo dos Benefícios__

__Localização__: Menu Estadual, Módulo: DUB\-RJ, item de menu Obrigações à Cálculo dos Benefícios

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS622

Criação do Módulo da DUB\-RJ

Criação do Módulo da DUB\-RJ

MFS3484

Inclusão da Espécie de Benefício

Inclusão da Espécie de Benefício – Diferimento do Pagamento

MFS31771

Benefício Suspensão

Alteração do Módulo DUB para inclusão do benefício do tipo “Suspensão”

MFS31697

Alteração na geração dos benefícios do tipo Isenção, Redução da BC e Suspensão 

Alteração na geração dos benefícios do tipo Isenção, Redução da BC e Suspensão, para trabalhar com a observação da SAFX08 ou da SAFX112, através de parâmetro\.

MFS41507

Alteração na geração do benefício do tipo Diferimento 

Alteração na geração do benefício do tipo Diferimento, para trabalhar com a observação da SAFX08 ou da SAFX112, através de parâmetro\.

MFS45596

Alteração no Cálculo do benefício do CP 

Alteração no cálculo do benefício do Crédito Presumido, para aplicar a alíquota sobre o valor da operação \(ao invés do Valor do ICMS, conforme a regra original\)\. Ver __RN12__ e __RN13__\. 

[MFS46075](https://jira.thomsonreuters.com/browse/MFS-46075)

Alteração Regra na geração Crédito Presumido\.

Alteração da Regra para considerar a SAFX07 na geração do Crédito Presumido, nos cenários que o cliente utiliza SAFX51 \- __RN15\.__

MFS46111

Andréa Rocha

Alteração na geração do benefício “Redução da Base de Cálculo”, tipo “03 \- Redução de base de cálculo para reduzir alíquota final” para tratar mais de uma alíquota de percentual de redução de ICMS\.

Rogério Ohashi

Alteração do cálculo do benefício tipo “02 \- Crédito presumido, específico para as operações de serviços de transporte, para coluna Valor da Operação \(Cálculo do Valor do ICMS Não debitado\), deve ser calculado considerando o campo de “Valor de ICMS”, conforme “CONVÊNIO ICMS 106/96”\. \(__RN15\)\.__

MFS46427

Liliane Assaf

Alteração no cálculo do benefício de __Isenção__ – tipo __01 __\- Isenção nas saídas e prestações para considerar a nova Parametrização de Alíquota por Benefício/UF/CST\.

Primeiro buscar a alíquota na Parametrização de Alíquota por Benefício/UF/CST, com Código da Observação, UF e CST da nota\.  Caso encontre parametrização, considera essa alíquota para o cálculo\.  

Caso não encontre, considera a alíquota da Parametrização do Benefício\. \(__RN02\)\.__

MFS62528

Liliane Assaf

Alteração no cálculo do benefício de __Isenção__ – tipo __03 __\- Isenção nas entradas e aquisições de serviço \(Importação\), para considerar a nova Parametrização de Alíquota por Benefício/UF/CST\.

Primeiro buscar a alíquota na Parametrização de Alíquota por Benefício/UF/CST, com Código da Observação, UF e CST da nota\.  Caso encontre parametrização, considera essa alíquota para o cálculo\.  

Caso não encontre, considera a alíquota da Parametrização do Benefício\. \(__RN04\)\.__

MFS62529

Liliane Assaf

Alteração no cálculo do benefício de __Redução da Base de Cálculo__ – tipo __03 __– Redução a Base de Cálculo para reduzir a alíquota final, para considerar a nova Parametrização de Alíquota por Benefício/UF/CST\.

Primeiro buscar a alíquota na Parametrização de Alíquota por Benefício/UF/CST, com Código da Observação, UF e CST da nota\.  Caso encontre parametrização, considera essa alíquota para o cálculo\.  

Caso não encontre, considera a alíquota da Parametrização do Benefício\. \(__RN07\)\.__

MFS62531

Liliane Assaf

Alteração no cálculo do benefício de __Diferimento do Pagamento__ – tipo __01 __– Diferimento do ICMS nas aquisições de ativo permanente \(Importação\), para considerar a nova Parametrização de Alíquota por Benefício/UF/CST\.

Primeiro buscar a alíquota na Parametrização de Alíquota por Benefício/UF/CST, com Código da Observação, UF e CST da nota\.  Caso encontre parametrização, considera essa alíquota para o cálculo\.  

Caso não encontre, considera a alíquota da Parametrização do Benefício\. \(__RN08\)\.__

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN00

__Regras Gerais__

\- Todos os valores resultantes dos cálculos deverão ser arredondados\.

\- Considerar apenas os documentos fiscais que possuam itens \(SAFX08\)\.

\- Deverão ser consideradas todas as validações abaixo para compor o Log do Processo:

__1 –__ Caso a diferença da alíquota resultar em um valor negativo ou igual a zero, será gravada a seguinte mensagem de erro no log do processo:

*“A diferença da alíquota calculada resultou em um valor negativo ou igual à zero, favor verificar o percentual de redução informado nos itens com a alíquota parametrizada”\. *Seguido do num\. docto fiscal, série, subsérie e data fiscal\.* *

O log exibirá os dados de identificação da nota fiscal em questão \(Número de nota fiscal/Série/SubSérie e Data fiscal\), para que o usuário possa conferir os dados\.

__2 –__ Caso existir mais de um diferencial de alíquota para mesma nota fiscal, será gravada a seguinte mensagem de erro no log do processo:

*“Existe mais de um diferencial de alíquota para a nota fiscal \(XXXX/XX/XX\)”\. *

O log exibirá os dados de identificação da nota fiscal em questão \(Número de nota fiscal/Série e SubSérie\), para que o usuário possa conferir os dados\.

__Alteração da MFS31697 \(alterou Isenção, Redução da BC e Suspensão\) e MFS41507 \(alterou o Diferimento\)__:

Alguns clientes relataram problemas na DUB, pois quando tinham numa mesma nota itens de um mesmo benefício, mas de atos legais diferentes \(situação permitida no Cadastro dos Benefícios da DUB\), a geração não processa corretamente, e considera tudo para um único ato legal\. Isso ocorria porque, apesar de cada Benefício/Ato Legal ter a sua observação própria, e as duas observações estarem na SAFX112 da nota, não havia como a geração identificar a qual observação cada item se referia, já que a SAFX112 é uma tabela “filha” da capa \(SAFX07\), e não do item \(SAFX08\)\.

Para resolver este problema, foi criado um parâmetro na tela dos Dados Iniciais da DUB \(menu “Parâmetros à Dados Iniciais”\), onde o usuário informa se deseja que o cálculo utilize a observação da SAFX112, conforme a versão original do módulo, ou a observação do item da nota \(campo 155 da SAFX08\)\. 

O Crédito Presumido não necessita de alteração, pois não trabalha com observações, e sim com uma parametrização própria de CFOP/NAT\. 

Verificar a utilização do parâmetro em todas as regras abaixo referentes aos benefícios alterados \(Isenção, Redução BC e Suspensão\)\.

__14/01/2021: Alteração MFS46075, do chamado 20896/2020 \- Bunge Alimentos S\.A, solicita que o a obrigação considere também os itens da SAFX51, uma vez que eles não possuem os itens na SAFX08\. \(conforme Resolução SEFAZ 180/08 e conforme embasamento do convênio 106/1996\) – RN15, porém como a SAFX51 não possuem as informações de CFOP/NAT para determinar qual a operação, foi alinhado com a equipe da Bunge, que vamos utilizar somente as informações da SAFX07\.__

__ __

__\- Criação de Regra para considerar no arquivo as informações oriundas da safx07 para os clientes que utilizam da SAFX51\.__

MFS622

MFS31697

MFS41507

[MFS46075](https://jira.thomsonreuters.com/browse/MFS-46075)

RN01

__Processamento dos Dados__

__Origem dos Dados:__ Tabela dos Documentos Fiscais \(SAFX07/SAFX08\)

                                  Parametrização dos Benefícios \(menu: Parâmetros > Benefícios\) __\(\*\)__ 

                                  Parametrização do Benefício – Crédito Presumido \(menu Parâmetros > Benefícios – Credito Presumido  > 

                                  Parâmetros Gerais de Cálculo por CFOP ou CFOP/Natureza\) __\(\*\*\)__

__Destino:__ Tabela do valor do ICMS não debitado por benefício__\.__

\- Tabela auxiliar que armazena os valores e informações do documento fiscal por espécie de benefícios\.

__O processamento é por Estabelecimento\.__

Para cada Estabelecimento, será calculado o valor médio de cada produto identificado nas notas\. 

O Processamento é de acordo com as notas do período de referência informado em tela\.

A seguir serão definidas as regras desse processamento\.

MFS622

RN02

__Critérios para a recuperação dos documentos__

__Espécie de Benefício: Isenção __

__Tipo de Cálculo do Benefício = 01 \- Isenção nas saídas e prestações:__

    \- Empresa = código da empresa do login;

    \- Estabelecimento = código do estabelecimento da geração; 

    \- Data Fiscal = deve ser uma data referente ao período informado em tela;

    \- Movto\_E\_S = “9” \(somente saídas\)

    \- Somente notas não canceladas;

      A observação que será utilizada como filtro, depende da opção escolhida pelo usuário nos Dados Iniciais da DUB: __\(MFS31697\)__

     __Se parâmetro "Obs complementar da nota \(SAFX112\)” marcado__

           \(Nesse caso, permanece o funcionamento original do módulo\)

         \- Considerar todos os itens presentes nas notas que:

- Estejam preenchidos o código de observação \(campo 12 \- COD\_OBS\_LANCTO\_FISCAL\) cujo tipo de observação \(campo 13 \- IND\_ICOMPL\_LANCTO\) for igual a ‘I’ e a vinculação \(campo 15 \- VINCULACAO\) for igual a ‘1 – EFD ICMS/IPI’ da SAFX112
- Estejam cadastrados na Parametrização dos Benefícios para a Espécie de Benefício = ‘Isenção’ e Cálculo do Benefício = ‘1 \- Isenção nas saídas e prestações’; 

     __Senão \(parâmetro "Obs do item \(SAFX08\)” marcado\)__

          Nesse caso, serão considerados apenas os itens que:

- A observação do campo “*155\-Código Observação*” da SAFX08 esteja preenchida e pertença a Parametrização dos Benefícios, para a Espécie de Benefício = ‘Isenção’ e Cálculo do Benefício = “1 \- Isenção nas saídas e prestações”\. 

                  

    \- Não serão considerados os itens cujo Produto esteja cadastrado na parametrização dos produtos excluídos do benefício \(menu:

      “Parâmetros > Produtos Excluídos dos Benefícios”\) para a Espécie de Benefício = ‘Isenção’;

    \- Considerar todos os itens com Código de Situação Tributária B igual a isenta \(COD\_SITUACAO\_B = ‘40’\) e o valor de base de 

       ICMS seja isenta, ou seja, campo 56 \- BASE\_ICMS preenchido da SAFX08\.

    

    \- Considerar a alíquota cadastrada na Parametrização dos Benefícios ou na Parametrização de Alíquota por Benefício/UF/CST __\(\*\)__

      conforme regra a seguir:

      \[MFS46427\] 

      Primeiro verificar se existe alíquota cadastrada na Parametrização de Alíquota por Benefício/UF/CST considerando:

- Espécie Benefício = Isenção
- Tipo de Cálculo do Benefício = 01 \- Isenção nas saídas e prestações
- Código da Observação \(da SAFX112\), caso parâmetro __"Obs complementar da nota \(SAFX112\)”__ esteja marcado;

Ou

Código da Observação \(da SAFX08\), conforme parâmetro __"Obs do item \(SAFX08\)”__ esteja__ __marcado;

- UF da Pessoa Fís/Jur da Capa do Documento fiscal \(SAFX07\);
- Sit Tributária A \(SAFX08\);
- Sit\. Tributária B \(SAFX08\);

Se a busca acima retornar registro, considerar a alíquota da Parametrização de Alíquota por Benefício/UF/CST \(EST\_DUB\_PAR\_ALIQ\)\.

Se não houver, considerar a alíquota da Parametrização do Benefício \(EST\_DUB\_CALC\_BENEF\)\.

    \- Os itens recuperados serão agrupados por nota fiscal, Tipo/Instrumento Legal da Parametrização dos Benefícios e Alíquota e gravados na tabela EST\_DUB\_CALC\_BENEF\.

__Totalização do valor:__

      O valor de cada item a ser totalizado será buscado do campo 56 \- BASE\_ICMS da SAFX08 cujo campo 55 \- TRIB\_ICMS seja igual a 2\.

     

__Cálculo do Valor do ICMS Não debitado:__

     

Para cada produto processado, calcular o valor do ICMS Não debitado da seguinte forma:

       Valor de ICMS Não debitado = Valor Total Base \(BASE\_ICMS – SAFX08\) x Alíquota parametrizada % __\(\*\)__

MFS622

MFS31697

MFS46427

RN03

__Critérios para a recuperação dos documentos__

__Espécie de Benefício: Isenção __

__Tipo de Cálculo do Benefício = 02 \- Isenção nas entradas ou aquisições de serviço \(Diferencial de Alíquota\):__

    \- Empresa = código da empresa do login;

    \- Estabelecimento = código do estabelecimento da geração; 

    \- Data Fiscal = deve ser uma data referente ao período informado em tela de cálculo do benefício;

    \- Movto\_E\_S <> “9” \(somente entradas\)

    \- Somente notas não canceladas;

      A observação que será utilizada como filtro, depende da opção escolhida pelo usuário nos Dados Iniciais da DUB: __\(MFS31697\)__

     __Se parâmetro "Obs complementar da nota \(SAFX112\)” marcado__

           \(Nesse caso, permanece o funcionamento original do módulo\)

       \- Considerar todos os itens presentes nas notas que:

- Estejam preenchidos o código de observação \(campo 12 \- COD\_OBS\_LANCTO\_FISCAL\) cujo tipo de observação \(campo 13 \- IND\_ICOMPL\_LANCTO\) for igual a ‘I’ e a vinculação \(campo 15 \- VINCULACAO\) for igual a ‘1 – EFD ICMS/IPI’ da SAFX112
- Estejam cadastrados na Parametrização dos Benefícios __\(\*\)__ para a Espécie de Benefício = ‘Isenção’ e Cálculo do Benefício = ‘2 \- Isenção nas entradas ou aquisições de serviço \(Diferencial de Alíquota\)’ ;

     __Senão    \(parâmetro "Obs do item \(SAFX08\)” marcado\)__

          Nesse caso, serão considerados apenas os itens em que a observação do campo “*155\-Código Observação*” da SAFX08 esteja 

          preenchida, e seja uma observação parametrizada no cadastro de Benefícios da DUB, para a Espécie de Benefício = ‘Isenção’ e

          Cálculo do Benefício = “2 \- Isenção nas entradas ou aquisições de serviço \(Diferencial de Alíquota\)”\. __Os itens recuperados __

__          serão agrupados por nota fiscal e  observação, e para cada agrupamento, os valores serão totalizados, e será gravada __

__          uma linha na tabela EST\_DUB\_CALC\_BENEF;__ 

    \- Não serão considerados os itens cujo Produto esteja cadastrado na parametrização dos produtos excluídos do benefício \(menu:

      “Parâmetros > Produtos Excluídos dos Benefícios”\) para a Espécie de Benefício = ‘Isenção’;

    \- Considerar todos os itens com Código de Situação Tributária B igual a isenta \(COD\_SITUACAO\_B = ‘40’\) e o valor de base de ICMS seja isenta, ou seja, campo 56 \- BASE\_ICMS preenchido da SAFX08\.

    \- Não deve considerar a alíquota parametrizada, deverá sempre buscar o diferencial de alíquota do item \(campo 44 \- DIF\_ALIQ\_ICMS da safx08\)\. 

__Totalização do valor:__

O valor de cada item a ser totalizado será buscado do campo 56 \- BASE\_ICMS da SAFX08 cujo campo 55 \- TRIB\_ICMS seja igual a 2\.

     

__Cálculo do Valor do ICMS Não debitado:__

     

Para cada produto processado, calcular o valor do ICMS Não debitado da seguinte forma:

       Valor de ICMS Não debitado = Valor Total Base \(BASE\_ICMS – SAFX08\) x Diferencial de alíquota do item % \(campo 44 \- DIF\_ALIQ\_ICMS da safx08\)\. Considerar o log de processo descrito na Regra Geral \(RN00\) opção 2\.

MFS622

__MFS31697__

RN04

__Critérios para a recuperação dos documentos__

__Espécie de Benefício: Isenção __

__Tipo de Cálculo do Benefício = 03 \- Isenção nas entradas ou aquisições de serviço \(Importação\):__

    \- Empresa = código da empresa do login;

    \- Estabelecimento = código do estabelecimento da geração; 

    \- Data Fiscal = deve ser uma data referente ao período informado em tela de cálculo do benefício;

    \- Movto\_E\_S <> “9” \(somente entradas\)

    \- Somente notas não canceladas;

    \- Considerar todos os itens com CFOP = “3”,

      A observação que será utilizada como filtro, depende da opção escolhida pelo usuário nos Dados Iniciais da DUB: __\(MFS31697\)__

     __Se parâmetro "Obs complementar da nota \(SAFX112\)” marcado__

           \(Nesse caso, permanece o funcionamento original do módulo\)

       \- Considerar todos os itens presentes nas notas que:

- Estejam preenchidos o código de observação \(campo 12 \- COD\_OBS\_LANCTO\_FISCAL\) cujo tipo de observação \(campo 13 \- IND\_ICOMPL\_LANCTO\) for igual a ‘I’ e a vinculação \(campo 15 \- VINCULACAO\) for igual a ‘1 – EFD ICMS/IPI’ da SAFX112
- Estejam cadastrados na Parametrização dos Benefícios para a Espécie de Benefício = ‘Isenção’ e Cálculo do Benefício = ‘3 \- Isenção nas entradas ou aquisições de serviço \(Importação\)’\.

     __Senão \(parâmetro "Obs do item \(SAFX08\)” marcado\)__

          Nesse caso, serão considerados apenas os itens em que:

- A observação do campo “*155\-Código Observação*” da SAFX08 esteja preenchida e pertença a Parametrização dos Benefícios, para a Espécie de Benefício = ‘Isenção’ e Cálculo do Benefício = “3 \- Isenção nas entradas ou aquisições de serviço \(Importação\)”\. 

    \- Não serão considerados os itens cujo Produto esteja cadastrado na parametrização dos produtos excluídos do benefício \(menu:

      “Parâmetros > Produtos Excluídos dos Benefícios”\) para a Espécie de Benefício = ‘Isenção’;

    \- Considerar todos os itens com Código de Situação Tributária B igual a isenta \(COD\_SITUACAO\_B = ‘40’\) e o valor de base de ICMS seja isenta, ou seja, campo 56 \- BASE\_ICMS preenchido da SAFX08\.

    \- Considerar a alíquota cadastrada na Parametrização dos Benefícios ou na Parametrização de Alíquota por Benefício/UF/CST __\(\*\) __

      conforme regra a seguir:

      \[MFS62528\] 

      Primeiro verificar se existe alíquota cadastrada na Parametrização de Alíquota por Benefício/UF/CST considerando:

- Espécie Benefício = Isenção
- Tipo de Cálculo do Benefício = 03 \- Isenção nas entradas ou aquisições de serviço \(Importação\)
- Código da Observação \(da SAFX112\), caso parâmetro __"Obs complementar da nota \(SAFX112\)”__ esteja marcado;

Ou

Código da Observação \(da SAFX08\), conforme parâmetro __"Obs do item \(SAFX08\)”__ esteja__ __marcado;

- UF da Pessoa Fís/Jur da Capa do Documento fiscal \(SAFX07\);
- Sit Tributária A \(SAFX08\);
- Sit\. Tributária B \(SAFX08\);

Se a busca acima retornar registro, considerar a alíquota da Parametrização de Alíquota por Benefício/UF/CST \(EST\_DUB\_PAR\_ALIQ\)\.

       Se não houver, considerar a alíquota da Parametrização do Benefício \(EST\_DUB\_CALC\_BENEF\)\.

    \- Os itens recuperados serão agrupados por nota fiscal, Tipo/Instrumento Legal da Parametrização dos Benefícios e Alíquota e gravados na tabela EST\_DUB\_CALC\_BENEF\.

__Totalização do valor:__

      O valor de cada item a ser totalizado será buscado do campo 56 \- BASE\_ICMS da SAFX08 cujo campo 55 \- TRIB\_ICMS seja igual a 2\.

     

__Cálculo do Valor do ICMS Não debitado:__

     

Para cada produto processado, calcular o valor do ICMS Não debitado da seguinte forma:

       Valor de ICMS Não debitado = Valor Total Base \(BASE\_ICMS – SAFX08\) x Alíquota parametrizada % __\(\*\)__

MFS622

MFS31697

MFS62528

RN05

__Critérios para a recuperação dos documentos__

__Espécie de Benefício: Redução da Base de Cálculo__

__Tipo de Cálculo do Benefício = 01 \- Redução de base de cálculo proporcional ao valor da operação/prestação \(Saída\):__

    \- Empresa = código da empresa do login;

    \- Estabelecimento = código do estabelecimento da geração; 

    \- Data Fiscal = deve ser uma data referente ao período informado em tela;

    \- Movto\_E\_S = “9” \(somente saídas\)

    \- Considerar todos os itens cujo campo 57 \- BASE\_REDU\_ICMS da SAFX08 estejam preenchidos\.

    \- Somente notas não canceladas;

      A observação que será utilizada como filtro, depende da opção escolhida pelo usuário nos Dados Iniciais da DUB: __\(MFS31697\)__

     __Se parâmetro "Obs complementar da nota \(SAFX112\)” marcado__

           \(Nesse caso, permanece o funcionamento original do módulo\)

       \- Considerar todos os itens presentes nas notas que:

- Estejam preenchidos o código de observação \(campo 12 \- COD\_OBS\_LANCTO\_FISCAL\) cujo tipo de observação \(campo 13 \- IND\_ICOMPL\_LANCTO\) for igual a ‘I’ e a vinculação \(campo 15 \- VINCULACAO\) for igual a ‘1 – EFD ICMS/IPI’ da SAFX112
- Estejam cadastrados na Parametrização dos Benefícios __\(\*\)__ para a Espécie de Benefício = ‘Redução da base de cálculo’ e Cálculo do Benefício = ‘1 \- Redução de base de cálculo proporcional ao valor da operação/prestação \(Saída\)’\. 

   

     __Senão    \(parâmetro "Obs do item \(SAFX08\)” marcado\)__

          Nesse caso, serão considerados apenas os itens em que a observação do campo “*155\-Código Observação*” da SAFX08 esteja 

          preenchida, e seja uma observação parametrizada no cadastro de Benefícios da DUB, para a Espécie de Benefício = ‘Redução 

          da base de cálculo’ e Cálculo do Benefício = “1 \- Redução de base de cálculo proporcional ao valor da operação/prestação 

         \(Saída\)”\. __Os itens recuperados serão agrupados por nota fiscal e observação, e para cada agrupamento, os valores serão totalizados, e será gravada uma linha na tabela EST\_DUB\_CALC\_BENEF;__ 

    \- Não serão considerados os itens cujo Produto esteja cadastrado na parametrização dos produtos excluídos do benefício \(menu:

      “Parâmetros > Produtos Excluídos dos Benefícios”\) para a Espécie de Benefício = ‘Redução da base de cálculo;

    \- Considerar a alíquota cadastrada na Parametrização dos Benefícios __\(\*\)__

__Totalização do valor:__

      O valor de cada item a ser totalizado será buscado do campo 64 \- VLR\_CONTAB\_ITEM da SAFX08\.

     

__Cálculo do Valor do ICMS Não debitado:__

     

Para cada produto processado, calcular o valor do ICMS Não debitado da seguinte forma:

      Valor das operações = Valor Total Contábil \(VLR\_CONTAB\_ITEM – SAFX08\)

      Valor da redução = Valor total da redução ICMS \(BASE\_REDU\_ICMS – SAFX08\)

      Valor de ICMS Não debitado = Valor da redução x Alíquota parametrizada % __\(\*\)__

MFS622

__MFS31697__

RN06

__Critérios para a recuperação dos documentos__

__Espécie de Benefício: Redução da Base de Cálculo__

__Tipo de Cálculo do Benefício = 02 \- Redução de base de cálculo proporcional ao valor da operação/prestação \(Entrada\):__

    \- Empresa = código da empresa do login;

    \- Estabelecimento = código do estabelecimento da geração; 

    \- Data Fiscal = deve ser uma data referente ao período informado em tela;

    \- Movto\_E\_S <> “9” \(somente entradas\)

    \- Somente notas não canceladas;

    \- Considerar todos os itens que o campo 57 \- BASE\_REDU\_ICMS da SAFX08 estejam preenchidos\.

      A observação que será utilizada como filtro, depende da opção escolhida pelo usuário nos Dados Iniciais da DUB: __\(MFS31697\)__

     __Se parâmetro "Obs complementar da nota \(SAFX112\)” marcado__

           \(Nesse caso, permanece o funcionamento original do módulo\)

       \- Considerar todos os itens presentes nas notas que:

- Estejam preenchidos o código de observação \(campo 12 \- COD\_OBS\_LANCTO\_FISCAL\) cujo tipo de observação \(campo 13 \- IND\_ICOMPL\_LANCTO\) for igual a ‘I’ e a vinculação \(campo 15 \- VINCULACAO\) for igual a ‘1 – EFD ICMS/IPI’ da SAFX112
- Estejam cadastrados na Parametrização dos Benefícios __\(\*\) __para a Espécie de Benefício = ‘Redução da base de cálculo’ e Cálculo do Benefício = ‘2 \- Redução de base de cálculo proporcional ao valor da operação/prestação \(Entrada\)’\.

  

     __Senão    \(parâmetro "Obs do item \(SAFX08\)” marcado\)__

          Nesse caso, serão considerados apenas os itens em que a observação do campo “*155\-Código Observação*” da SAFX08 esteja 

          preenchida, e seja uma observação parametrizada no cadastro de Benefícios da DUB, para a Espécie de Benefício = ‘Redução 

          da base de cálculo’ e Cálculo do Benefício = “2 \- Redução de base de cálculo proporcional ao valor da operação/prestação 

         \(Entrada\)”\. __Os itens recuperados serão agrupados por nota fiscal e observação, e para cada agrupamento, os valores __

__          serão totalizados, e será gravada uma linha na tabela EST\_DUB\_CALC\_BENEF;__ 

 

    \- Não serão considerados os itens cujo Produto esteja cadastrado na parametrização dos produtos excluídos do benefício \(menu:

      “Parâmetros > Produtos Excluídos dos Benefícios”\) para a Espécie de Benefício = ‘Redução da base de cálculo;

    \- Considerar a alíquota cadastrada na Parametrização dos Benefícios __\(\*\)__

__Totalização do valor:__

      O valor de cada item a ser totalizado será buscado do campo 64 \- VLR\_CONTAB\_ITEM da SAFX08\.

     

__Cálculo do Valor do ICMS Não debitado:__

     

Para cada produto processado, calcular o valor do ICMS Não debitado da seguinte forma:

      Valor das operações = Valor Total Contábil \(VLR\_CONTAB\_ITEM – SAFX08\)

      Valor da redução = Valor total da redução ICMS \(BASE\_REDU\_ICMS – SAFX08\)

      Valor de ICMS Não debitado = Valor da redução x Alíquota parametrizada % __\(\*\)__

MFS622

__MFS31697__

RN07

__Critérios para a recuperação dos documentos__

__Espécie de Benefício: Redução da Base de Cálculo__

__Tipo de Cálculo do Benefício = 03 \- Redução de base de cálculo para reduzir alíquota final:__

    \- Empresa = código da empresa do login;

    \- Estabelecimento = código do estabelecimento da geração; 

    \- Data Fiscal = deve ser uma data referente ao período informado em tela;

    \- Movto\_E\_S = “1, 2, 3, 4, 5 e 9” \(entradas e saídas\);

    \- Somente notas não canceladas;

    \- Considerar todos os itens que o campo 97 \- PERC\_RED\_BASE\_ICMS da SAFX08 estejam preenchidos\.

      A observação que será utilizada como filtro, depende da opção escolhida pelo usuário nos Dados Iniciais da DUB: __\(MFS31697\)__

     __Se parâmetro "Obs complementar da nota \(SAFX112\)” marcado__

           \(Nesse caso, permanece o funcionamento original do módulo\)

    \- Considerar todos os itens presentes nas notas que:

- Estejam preenchidos o código de observação \(campo 12 \- COD\_OBS\_LANCTO\_FISCAL\) cujo tipo de observação \(campo 13 \- IND\_ICOMPL\_LANCTO\) for igual a ‘I’ e a vinculação \(campo 15 \- VINCULACAO\) for igual a ‘1 – EFD ICMS/IPI’ da SAFX112
- Estejam cadastrados na Parametrização dos Benefícios para a Espécie de Benefício = ‘Redução da base de cálculo’ e Cálculo do Benefício = ‘3 \- Redução de base de cálculo para reduzir alíquota final’\.

     __Senão \(parâmetro "Obs do item \(SAFX08\)” marcado\)__

          Nesse caso, serão considerados apenas os itens em que:

- A observação do campo “*155\-Código Observação*” da SAFX08 esteja preenchida e pertença a Parametrização dos Benefícios, para a Espécie de Benefício = ‘Redução da base de cálculo’ e Cálculo do Benefício = “3 \- Redução de base de cálculo para reduzir alíquota final”\. 

   

    \- Não serão considerados os itens cujo Produto esteja cadastrado na parametrização dos produtos excluídos do benefício \(menu:

      “Parâmetros > Produtos Excluídos dos Benefícios”\) para a Espécie de Benefício = ‘Redução da base de cálculo;

    \- Considerar a alíquota cadastrada na Parametrização dos Benefícios ou na Parametrização de Alíquota por Benefício/UF/CST __\(\*\) __

      conforme regra a seguir:

      \[MFS62529\] 

      Primeiro verificar se existe alíquota cadastrada na Parametrização de Alíquota por Benefício/UF/CST considerando:

- Espécie Benefício = Redução da Base de Cálculo
- Tipo de Cálculo do Benefício = 03 \- Redução de base de cálculo para reduzir alíquota final
- Código da Observação \(da SAFX112\), caso parâmetro __"Obs complementar da nota \(SAFX112\)”__ esteja marcado;

Ou

Código da Observação \(da SAFX08\), conforme parâmetro __"Obs do item \(SAFX08\)”__ esteja__ __marcado;

- UF da Pessoa Fís/Jur da Capa do Documento fiscal \(SAFX07\);
- Sit Tributária A \(SAFX08\);
- Sit\. Tributária B \(SAFX08\);

Se a busca acima retornar registro, considerar a alíquota da Parametrização de Alíquota por Benefício/UF/CST \(EST\_DUB\_PAR\_ALIQ\)\.

       Se não houver, considerar a alíquota da Parametrização do Benefício \(EST\_DUB\_CALC\_BENEF\)\.

    \- Os itens recuperados serão agrupados por nota fiscal, Tipo/Instrumento Legal da Parametrização dos Benefícios e Alíquota e gravados na tabela EST\_DUB\_CALC\_BENEF\.

__Totalização do valor:__

      O valor de cada item a ser totalizado será buscado do campo 64 \- VLR\_CONTAB\_ITEM da SAFX08\.

     

__Cálculo do Valor do ICMS Não debitado:__

     

Para cada produto processado, calcular o valor do ICMS Não debitado da seguinte forma:

      Valor das operações = Valor Total Contábil \(VLR\_CONTAB\_ITEM – SAFX08\)

__\[MFS46111\] __Tratar a situação de mais uma alíquota de percentual de redução de ICMS em uma mesma nota fiscal

      Valor de ICMS Não debitado = Valor das operações x Diferença entre a Alíquota parametrizada % __\(\*\) __e o percentual de redução de ICMS presente no campo__ __97 \- PERC\_RED\_BASE\_ICMS da SAFX08\. Considerar o log de processo descrito na Regra Geral \(RN00\) opção 1 e opção 2\.  

__Obs__\.: Considerar que uma nota fiscal pode ter mais de uma alíquota percentual de redução de ICMS, ou seja, cada item da nota pode possuir uma alíquota diferente\. Portanto, para uma mesma nota fiscal poderão existir 2 linhas calculadas para o benefício tratado nesta regra\. 

Exemplo:

Alíquota parametrizada = __19 %__

Percentual de Redução do ICMS do Item: = __7%__

Diferença de Alíquota = __12 %__ que será a alíquota utilizada\.

MFS622

__MFS31697__

MFS46111

MFS62529

RN08

__Critérios para a recuperação dos documentos__

__Espécie de Benefício: Diferimento __

__Tipo de Cálculo do Benefício = 01 \- Diferimento do ICMS nas aquisições de ativo permanente \(Importação\):__

    \- Empresa = código da empresa do login;

    \- Estabelecimento = código do estabelecimento da geração; 

    \- Data Fiscal = deve ser uma data referente ao período informado em tela de cálculo do benefício;

    \- Movto\_E\_S <> “9” \(somente entradas\)

    \- Somente notas não canceladas;

    \- Considerar todos os itens com CFOP = “3”,

    \- Considerar todos os itens com Código de Situação Tributária B igual à diferimento \(COD\_SITUACAO\_B = ‘51’\) e o campo Valor

      Diferimento \(DUB\-RJ\) da SAFX08 esteja preenchido\. 

      A observação que será utilizada como filtro, depende da opção escolhida pelo usuário nos Dados Iniciais da DUB: __\(MFS41507\)__

     __Se parâmetro "Obs complementar da nota \(SAFX112\)” marcado__

           \(Nesse caso, permanece o funcionamento original do módulo\)

       \- Considerar todos os itens presentes nas notas que:

- Estejam preenchidos o código de observação \(campo 12 \- COD\_OBS\_LANCTO\_FISCAL\) cujo tipo de observação \(campo 13 \- IND\_ICOMPL\_LANCTO\) for igual a ‘I’ e a vinculação \(campo 15 \- VINCULACAO\) for igual a ‘1 – EFD ICMS/IPI’ da SAFX112\.
- Estejam cadastrados na Parametrização dos Benefícios para a Espécie de Benefício = ‘Diferimento do Pagamento’ e Cálculo do Benefício = ‘1 \- Diferimento do ICMS nas aquisições de ativo permanente \(Importação\)’\.

 

    __Senão \(parâmetro "Obs do item \(SAFX08\)” marcado\)__

          Nesse caso, serão considerados apenas os itens que:

- A observação do campo “*155\-Código Observação*” da SAFX08 esteja preenchida, e pertença a Parametrização dos Benefícios, para a Espécie de Benefício = ‘Diferimento do Pagamento’ e Cálculo do Benefício = “1 \- Diferimento do ICMS nas aquisições de ativo permanente \(Importação\)”\.  

 

     \- Não serão considerados os itens cujo Produto esteja cadastrado na parametrização dos produtos excluídos do benefício \(menu:

      “Parâmetros > Produtos Excluídos dos Benefícios”\) para a Espécie de Benefício = ‘Diferimento do Pagamento’;

    \- Considerar a alíquota cadastrada na Parametrização dos Benefícios ou na Parametrização de Alíquota por Benefício/UF/CST __\(\*\)__

      conforme regra a seguir:

      \[MFS62531\] 

      Primeiro verificar se existe alíquota cadastrada na Parametrização de Alíquota por Benefício/UF/CST considerando:

- Espécie Benefício = Diferimento do pagamento
- Tipo de Cálculo do Benefício = 01 \- Diferimento do ICMS nas aquisições de ativo permanente \(Importação\)
- Código da Observação \(da SAFX112\), caso parâmetro __"Obs complementar da nota \(SAFX112\)”__ esteja marcado;

Ou

Código da Observação \(da SAFX08\), conforme parâmetro __"Obs do item \(SAFX08\)”__ esteja__ __marcado;

- UF da Pessoa Fís/Jur da Capa do Documento fiscal \(SAFX07\);
- Sit Tributária A \(SAFX08\);
- Sit\. Tributária B \(SAFX08\);

Se a busca acima retornar registro, considerar a alíquota da Parametrização de Alíquota por Benefício/UF/CST \(EST\_DUB\_PAR\_ALIQ\)\.

Se não houver, considerar a alíquota da Parametrização do Benefício \(EST\_DUB\_CALC\_BENEF\)\.

    \- Os itens recuperados serão agrupados por nota fiscal e Tipo/Instrumento Legal da Parametrização dos Benefícios e gravados na tabela EST\_DUB\_CALC\_BENEF\_DIF\.

__Totalização do valor:__

      O valor de cada item a ser totalizado será buscado do campo Valor Diferimento \(DUB\-RJ\) da SAFX08\.

     

__Cálculo do Valor do ICMS Não debitado:__

     

Para cada produto processado, calcular o valor do ICMS Não debitado da seguinte forma:

      Valor do bem adquirido = Valor do bem adquirido \(campo Valor Diferimento \(DUB\-RJ\) da SAFX08\)

      Valor da base de cálculo na importação = Valor do bem importado / \(1 – 0__, __Alíquota parametrizada % __\(\*\)__\)\.

      Valor de ICMS Não debitado = Valor da base de cálculo na importação x Alíquota parametrizada % __\(\*\)__

Obs: O *Valor da base de cálculo na importação* é o *Valor do bem importado* dividido por um \[\(1\) menos \(\-\) zero \(0\) vírgula \(,\) alíquota parametrizada %\]\.

__Exemplo:__

Alíquota parametrizada = __16__ %

Valor do bem adquirido = 10\.000

Valor da base de cálculo na importação = 10\.000 / \(1\-0,__16__\), ou seja, 10\.000 / 0,84 = 11\.904761 

Valor de ICMS Não debitado = 11\. 904761 x __16__ % = __1\.9047617__

__Importante:__ O valor resultante sempre deve ser arredondado para número inteiro, ou seja, nesse caso o resultado do Valor de ICMS Não debitado é igual a __1\.905,00\.__

MFS3484

__MFS41507__

MFS62531

RN09

__Critérios para a recuperação dos documentos__

__Espécie de Benefício: Diferimento __

__Tipo de Cálculo do Benefício = 02 \- Diferimento do ICMS nas aquisições de ativo permanente \(Operação Interestadual\):__

    \- Empresa = código da empresa do login;

    \- Estabelecimento = código do estabelecimento da geração; 

    \- Data Fiscal = deve ser uma data referente ao período informado em tela de cálculo do benefício;

    \- Movto\_E\_S <> “9” \(somente entradas\)

    \- Somente notas não canceladas;

    \- Considerar todos os itens com CFOP = “2”,

    \- Considerar todos os itens com Código de Situação Tributária B igual à diferimento \(COD\_SITUACAO\_B = ‘51’\) e o campo Valor Diferimento \(DUB\-RJ\) da SAFX08 esteja preenchido\. 

      A observação que será utilizada como filtro, depende da opção escolhida pelo usuário nos Dados Iniciais da DUB: __\(MFS41507\)__

     __Se parâmetro "Obs complementar da nota \(SAFX112\)” marcado__

           \(Nesse caso, permanece o funcionamento original do módulo\)

       \- Considerar todos os itens presentes nas notas que:

- Estejam preenchidos o código de observação \(campo 12 \- COD\_OBS\_LANCTO\_FISCAL\) cujo tipo de observação \(campo 13 \- IND\_ICOMPL\_LANCTO\) for igual a ‘I’ e a vinculação \(campo 15 \- VINCULACAO\) for igual a ‘1 – EFD ICMS/IPI’ da SAFX112\.
- Estejam cadastrados na Parametrização dos Benefícios \(\*\) para a Espécie de Benefício = ‘Diferimento do Pagamento’ e Cálculo do Benefício = ‘2 \- Diferimento do ICMS nas aquisições de ativo permanente \(Operação Interestadual\)’\.

    __Senão \(parâmetro "Obs do item \(SAFX08\)” marcado\)__

          Nesse caso, serão considerados apenas os itens em que a observação do campo “*155\-Código Observação*” da SAFX08 esteja 

          preenchida, e seja uma observação parametrizada no cadastro de Benefícios da DUB, para a Espécie de Benefício =

          ‘Diferimento do Pagamento’ e Cálculo do Benefício = “2 \- Diferimento do ICMS nas aquisições de ativo permanente \(Operação 

          Interestadual\)”\. __Os itens recuperados serão agrupados por nota fiscal e observação, e para cada agrupamento, os __

__          valores serão totalizados, e será gravada uma linha na tabela EST\_DUB\_CALC\_BENEF\_DIF;__ 

    \- Não serão considerados os itens cujo Produto esteja cadastrado na parametrização dos produtos excluídos do benefício \(menu:

      “Parâmetros > Produtos Excluídos dos Benefícios”\) para a Espécie de Benefício = ‘Diferimento do Pagamento’;

    \- Não deve considerar a alíquota parametrizada, deverá sempre buscar o diferencial de alíquota do item \(campo 44 \- Diferença Alíquota ICMS da safx08\)\. Considerar o log de processo descrito na Regra Geral \(RN00\) opção 2\.

__Totalização do valor:__

      O valor de cada item a ser totalizado será buscado do campo Valor Diferimento \(DUB\-RJ\) da SAFX08\.

     

__Cálculo do Valor do ICMS Não debitado:__

     

Para cada produto processado, calcular o valor do ICMS Não debitado da seguinte forma:

      Valor do bem adquirido = Valor do bem adquirido \(campo Valor Diferimento \(DUB\-RJ\) da SAFX08\)

     Valor de ICMS Não debitado = Valor do bem adquirido x Diferencial de alíquota do item % \(campo 44 \- Diferença Alíquota ICMS da safx08\)\.  Considerar o log de processo descrito na Regra Geral \(RN00\) opção 1 e opção 2

MFS3484

__MFS41507__

RN10

__Critérios para a recuperação dos documentos__

__Espécie de Benefício: Diferimento __

__Tipo de Cálculo do Benefício = 03 \- Diferimento do ICMS nas aquisições de ativo permanente \(Operação Interna\):__

    \- Empresa = código da empresa do login;

    \- Estabelecimento = código do estabelecimento da geração; 

    \- Data Fiscal = deve ser uma data referente ao período informado em tela de cálculo do benefício;

    \- Movto\_E\_S <> “9” \(somente entradas\)

    \- Somente notas não canceladas;

    \- Considerar todos os itens com CFOP = “1”,

    \- Considerar todos os itens com Código de Situação Tributária B igual à diferimento \(COD\_SITUACAO\_B = ‘51’\) e o campo Valor Diferimento \(DUB\-RJ\) da SAFX08 esteja preenchido\. 

      A observação que será utilizada como filtro, depende da opção escolhida pelo usuário nos Dados Iniciais da DUB: __\(MFS41507\)__

     __Se parâmetro "Obs complementar da nota \(SAFX112\)” marcado__

           \(Nesse caso, permanece o funcionamento original do módulo\)

       \- Considerar todos os itens presentes nas notas que:

- Estejam preenchidos o código de observação \(campo 12 \- COD\_OBS\_LANCTO\_FISCAL\) cujo tipo de observação \(campo 13 \- IND\_ICOMPL\_LANCTO\) for igual a ‘I’ e a vinculação \(campo 15 \- VINCULACAO\) for igual a ‘1 – EFD ICMS/IPI’ da SAFX112\.
- Estejam cadastrados na Parametrização dos Benefícios __\(\*\)__ para a Espécie de Benefício = ‘Diferimento do Pagamento’ e Cálculo do Benefício = ‘3 \- Diferimento do ICMS nas aquisições de ativo permanente \(Operação Interna\)’\. 

    __Senão    \(parâmetro "Obs do item \(SAFX08\)” marcado\)__

          Nesse caso, serão considerados apenas os itens em que a observação do campo “*155\-Código Observação*” da SAFX08 esteja 

          preenchida, e seja uma observação parametrizada no cadastro de Benefícios da DUB, para a Espécie de Benefício =

          ‘Diferimento de Pagamento’ e Cálculo do Benefício = “3 \- Diferimento do ICMS nas aquisições de ativo permanente \(Operação 

          Interna\)”\. __Os itens recuperados serão agrupados por nota fiscal e observação, e para cada agrupamento, os valores __

__          serão totalizados, e será gravada uma linha na tabela EST\_DUB\_CALC\_BENEF\_DIF;__ 

    \- Não serão considerados os itens cujo Produto esteja cadastrado na parametrização dos produtos excluídos do benefício \(menu:

      “Parâmetros > Produtos Excluídos dos Benefícios”\) para a Espécie de Benefício = ‘Diferimento do Pagamento’;

    \- Considerar a alíquota cadastrada na Parametrização dos Benefícios __\(\*\)__

__Totalização do valor:__

      O valor de cada item a ser totalizado será buscado do campo Valor Diferimento \(DUB\-RJ\) da SAFX08\.

     

__Cálculo do Valor do ICMS Não debitado:__

     

Para cada produto processado, calcular o valor do ICMS Não debitado da seguinte forma:

      Valor do bem adquirido = Valor do bem adquirido \(campo Valor Diferimento \(DUB\-RJ\) da SAFX08\)

      Valor de ICMS Não debitado = Valor do bem adquirido x Alíquota parametrizada % __\(\*\)__

MFS3484

__MFS41507__

RN11

__Critérios para a recuperação dos documentos__

__Espécie de Benefício: Diferimento __

__Tipo de Cálculo do Benefício = 04\- Saídas com ICMS diferido para contribuintes enquadrados nos regimes de pagamento por estimativa e simples nacional:__

    \- Empresa = código da empresa do login;

    \- Estabelecimento = código do estabelecimento da geração; 

    \- Data Fiscal = deve ser uma data referente ao período informado em tela de cálculo do benefício;

    \- Movto\_E\_S = “9” \(somente saídas\)

    \- Somente notas não canceladas;

    \- Considerar todos os itens com Código de Situação Tributária B igual à diferimento \(COD\_SITUACAO\_B = ‘51’\) e o campo Valor Diferimento \(DUB\-RJ\) da SAFX08 esteja preenchido\. 

    \- Considerar todos os itens cujo Pessoa física/jurídica seja enquadrada em 08 \- Regime de Estimativa \(campo 26 \- IND\_CLASSE\_PFJ da SAFX04\) OU Simples Nacional \(campo 43 \- IND\_SIMPLES\_NAC da SAFX04\) esteja preenchido com ‘S’\.

      A observação que será utilizada como filtro, depende da opção escolhida pelo usuário nos Dados Iniciais da DUB: __\(MFS41507\)__

     __Se parâmetro "Obs complementar da nota \(SAFX112\)” marcado__

           \(Nesse caso, permanece o funcionamento original do módulo\)

      \- Considerar todos os itens presentes nas notas que:

- Estejam preenchidos o código de observação \(campo 12 \- COD\_OBS\_LANCTO\_FISCAL\) cujo tipo de observação \(campo 13 \- IND\_ICOMPL\_LANCTO\) for igual a ‘I’ e a vinculação \(campo 15 \- VINCULACAO\) for igual a ‘1 – EFD ICMS/IPI’ da SAFX112\.
- Estejam cadastrados na Parametrização dos Benefícios __\(\*\)__ para a Espécie de Benefício = ‘Diferimento do Pagamento’ e Cálculo do Benefício = ‘4\- Saídas com ICMS diferido para contribuintes enquadrados nos regimes de pagamento por estimativa e simples nacional’\. 

    __Senão    \(parâmetro "Obs do item \(SAFX08\)” marcado\)__

          Nesse caso, serão considerados apenas os itens em que a observação do campo “*155\-Código Observação*” da SAFX08 esteja 

          preenchida, e seja uma observação parametrizada no cadastro de Benefícios da DUB, para a Espécie de Benefício =

          ‘Diferimento de Pagamento’ e Cálculo do Benefício = “4 \- Saídas com ICMS diferido para contribuintes enquadrados nos regimes de pagamento por estimativa e simples nacional”\. __Os itens recuperados serão agrupados por nota fiscal e observação, e para cada agrupamento, os valores serão totalizados, e será gravada uma linha na tabela EST\_DUB\_CALC\_BENEF\_DIF;__ 

    \- Não serão considerados os itens cujo Produto esteja cadastrado na parametrização dos produtos excluídos do benefício \(menu:

      “Parâmetros > Produtos Excluídos dos Benefícios”\) para a Espécie de Benefício = ‘Diferimento do Pagamento’;

    \- Considerar a alíquota cadastrada na Parametrização dos Benefícios __\(\*\)__

__Totalização do valor:__

      O valor de cada item a ser totalizado será buscado do campo Valor Diferimento \(DUB\-RJ\) da SAFX08\.

     

__Cálculo do Valor do ICMS Não debitado:__

     

Para cada produto processado, calcular o valor do ICMS Não debitado da seguinte forma:

      Valor das saídas com diferimento = Valor do saída diferimento \(campo Valor Diferimento \(DUB\-RJ\) da SAFX08\)

      Valor de ICMS Não debitado = Valor das saídas com diferimento x Alíquota parametrizada % __\(\*\)__

MFS3484

__MFS41507__

RN12

__Critérios para a recuperação dos documentos__

__Espécie de Benefício: Crédito Presumido __

__Tipo de Cálculo do Benefício = 01 \- Crédito presumido sobre entradas:__

    \- Empresa = código da empresa do login;

    \- Estabelecimento = código do estabelecimento da geração; 

    \- Data Fiscal = deve ser uma data referente ao período informado em tela de cálculo do benefício;

    \- Movto\_E\_S <> “9” \(somente entradas\)

    \- Somente notas não canceladas;

    \- Considerar todos os itens com CFOP ou CFOP/Natureza parametrizados na Parametrização do Benefício – Crédito Presumido __\(\*\*\)__ \(menu Parâmetros  Benefícios – Credito Presumido   Parâmetros Gerais de Cálculo por CFOP ou CFOP/Natureza\) para a Espécie de Benefício = ‘Crédito Presumido’ e Cálculo do Benefício = ‘1\-Crédito presumido sobre entradas’ __exceto__ os produtos que estejam parametrizados na Parametrização dos Produtos Excluídos – Crédito Presumido  \(menu Parâmetros  Benefício – Credito Presumido  Produtos Excluídos – Crédito Presumido\) para o mesmo CFOP ou CFOP/Natureza\. 

    \- Considerar a alíquota cadastrada na Parametrização do Benefício – Crédito Presumido __\(\*\*\)__

__Totalização do valor:__

Alteração __MFS45596__: O cálculo do Crédito Presumido foi alterado para aplicar a alíquota sobre o valor da operação, ao invés do Valor do ICMS, conforme regra original\. A alteração foi baseada em parecer da Informação, no chamado 20612/20 \(Profarma\), no item 8\.

      O valor de cada item a ser totalizado será buscado do campo 43 \- VLR\_ICMS da SAFX08\.

      O valor de cada item a ser totalizado será buscado do campo 64 \- VLR\_CONTAB\_ITEM da SAFX08\.

   

__Cálculo do Valor do ICMS Não debitado:__

     

Para cada produto processado, calcular o valor do ICMS Não debitado da seguinte forma:

      Valor do crédito = Valor Total ICMS \(VLR\_ICMS – SAFX08\)

      Valor de ICMS Não debitado = Valor do crédito x Alíquota parametrizada % __\(\*\)__

      Valor da Operação = Valor Total da Operação \(VLR\_CONTAB\_ITEM – SAFX08\)

      Valor de ICMS Não debitado = Valor da Operação x Alíquota parametrizada % __\(\*\)__

MFS622

MFS45596

RN13

__Critérios para a recuperação dos documentos__

__Espécie de Benefício: Crédito Presumido __

__Tipo de Cálculo do Benefício = 02 \- Crédito presumido sobre saídas:__

    \- Empresa = código da empresa do login;

    \- Estabelecimento = código do estabelecimento da geração; 

    \- Data Fiscal = deve ser uma data referente ao período informado em tela de cálculo do benefício;

    \- Movto\_E\_S = “9” \(somente saídas\)

    \- Somente notas não canceladas;

    \- Considerar todos os itens com CFOP ou CFOP/Natureza parametrizados na Parametrização do Benefício – Crédito Presumido __\(\*\*\)__ \(menu Parâmetros  Benefícios – Credito Presumido   Parâmetros Gerais de Cálculo por CFOP ou CFOP/Natureza\) para a Espécie de Benefício = ‘Crédito Presumido’ e Cálculo do Benefício = ‘2 \- Crédito presumido sobre saídas’ __exceto__ os produtos que estejam parametrizados na Parametrização dos Produtos Excluídos – Crédito Presumido  \(menu Parâmetros  Benefício – Credito Presumido  Produtos Excluídos – Crédito Presumido\) para o mesmo CFOP ou CFOP/Natureza\. 

    \- Considerar a alíquota cadastrada na Parametrização do Benefício – Crédito Presumido __\(\*\*\)__

__Totalização do valor:__

Alteração __MFS45596__: O cálculo do Crédito Presumido foi alterado para aplicar a alíquota sobre o valor da operação, ao invés do Valor do ICMS, conforme regra original\. A alteração foi baseada em parecer da Informação, no chamado 20612/20 \(Profarma\), no item 8\.

      O valor de cada item a ser totalizado será buscado do campo 43 \- VLR\_ICMS da SAFX08\.

      O valor de cada item a ser totalizado será buscado do campo 64 \- VLR\_CONTAB\_ITEM da SAFX08\.

    

__Cálculo do Valor do ICMS Não debitado:__

     

Para cada produto processado, calcular o valor do ICMS Não debitado da seguinte forma:

      Valor do crédito = Valor Total ICMS \(VLR\_ICMS – SAFX08\)

      Valor de ICMS Não debitado = Valor do crédito x Alíquota parametrizada % __\(\*\)__

      Valor da Operação = Valor Total da Operação \(VLR\_CONTAB\_ITEM – SAFX08\)

      Valor de ICMS Não debitado = Valor da Operação x Alíquota parametrizada % __\(\*\)__

MFS622

MFS45596

RN14

__Critérios para a recuperação dos documentos__

__Espécie de Benefício: Suspensão __

O benefício do tipo Suspensão não tem diferentes opções de cálculo, como acontece nos demais tipos\. Na verdade, não haverá nenhum cálculo a ser executado, o processo irá apenas recuperar as notas enquadradas no benefício, e gravá\-las na tabela \(EST\_DUB\_CALC\_BENEF\), para posterior emissão de relatório\.

    \- Empresa = código da empresa do login;

    \- Estabelecimento = código do estabelecimento da geração; 

    \- Data Fiscal = deve ser uma data referente ao período informado em tela;

    \- Movto\_E\_S = “9” \(somente saídas\)

    \- Somente notas não canceladas;

    \- *Não* considerar os itens cujo Produto esteja cadastrado na parametrização “*Parâmetros > Produtos Excluídos dos Benefícios*”

      para o Benefício = “Suspensão”;

 

    \- Considerar apenas os itens com Código de Situação Tributária B igual a suspensão \(COD\_SITUACAO\_B = ‘__50__’\);

   \-  A observação que será utilizada como filtro, depende da opção escolhida pelo usuário nos Dados Iniciais da DUB: __\(MFS31697\)__

      __Se parâmetro "Obs complementar da nota \(SAFX112\)” marcado__

           \(Nesse caso, permanece o funcionamento original do módulo\)

           A nota deve ter uma observação cadastrada na SAFX112, com as seguintes características:

           O campo 13 \- IND\_ICOMPL\_LANCTO =  “I” \(__I__nformações Complementares da Nota\);

           O campo 15 – VINCULACAO = “1” \(EFD ICMS/IPI\);

           A observação do campo “12 \- COD\_OBS\_LANCTO\_FISCAL” deve estar cadastrada para o benefício de Suspensão, na 

           parametrização do menu “Parâmetros > Benefícios” \(campo “Código de Observação”\)\. Para pesquisar a observação na 

           parametrização dos benefícios \(EST\_DUB\_CAD\_BENEF\), serão considerados os seguintes dados:

\- Código da Empresa \- código da empresa do login;

             \- Código do Estabeecimento \- código do estabelecimento da geração;

             \- Espécie do Benefício \(COD\_ESPECIE\) = “05” \(Suspensão\);

             \- Tipo de Cálculo \(IND\_TIPO\_CALC\) = “ “ \(um caracter branco\);

      __Senão    \(parâmetro "Obs do item \(SAFX08\)” marcado\)__

           Nesse caso, serão considerados apenas os itens em que a observação do campo “*155\-Código Observação*” da SAFX08 esteja 

           preenchida, e seja uma observação parametrizada no cadastro de Benefícios da DUB, para o benefício de Suspensão \(menu 

           “Parâmetros > Benefícios”\)\. __Os itens recuperados serão agrupados por nota fiscal e observação, e para cada __

__           agrupamento, os valores serão totalizados, e será gravada  uma linha na tabela EST\_DUB\_CALC\_BENEF;__ 

 __Totalização do valor: __*Para cada agrupamento de nota fiscal e observação*, será totalizado o Valor Contábil dos itens \(campo 64\-VLR\_CONTAB\_ITEM da SAFX08\);

*Para cada nota fiscal / observação processada*, será gravada uma única linha na tabela EST\_DUB\_CALC\_BENEF, com as seguintes informações:

   \- COD\_EMPRESA – Código da empresa do login;

   \- COD\_ESTAB – Código do estabelecimento da geração;   

   \- COD\_ESPECIE – “05” \(Código do benefício da Suspensão\); 

   \- DATA\_FISCAL – Data fiscal da nota fiscal;

   \- MOVTO\_E\_S – “9”;

   \- NORM\_DEV – Indicador de nota de devolução da nota fiscal;

   \- IDENT\_DOCTO – Identificador do tipo de documento da nota fiscal;

   \- IDENT\_FIS\_JUR – Identificador da pessoa fis/jur da nota fiscal; 

   \- NUM\_DOCFIS – Número da nota fiscal;

   \- SERIE\_DOCFIS – Série da nota fiscal;

   \- SUB\_SERIE\_DOC\_FIS – Sub\-série da nota fiscal; 

   \- COD\_ATO\_LEGAL – COD\_ATO\_LEGAL da Parametrização dos Benefícios;

   \- NUMERO\_ANO – NUMERO\_ANO da Parametrização dos Benefícios;

   \- DATA\_INI – DATA\_INI da Parametrização dos Benefícios;

   \- IND\_TIPO\_CALC – IND\_TIPO\_CALC da Parametrização dos Benefícios;

   

   \- VLR\_CONTABIL \- Totalização do Valor Contábil de todos os itens da nota, conforme a regra acima;

   \- VLR\_BASE          \- Este campo será gravado com zeros;

   \- VLR\_PERC          \- Este campo será gravado com zeros;

   \- VLR\_ICMS\_DEB \- Este campo será gravado com zeros;

__Obs\.__: Apesar do benefício Suspensão *não* ter diferentes opções de cálculo, pode existir na parametrização do benefício mais de um código de obervação cadastrada \(a observação compõe  chave da EST\_DUB\_CAD\_BENEF\)\. Desta forma, poderão existir notas com observações diferentes, referentes à diferentes atos legais\. Assim, o relatório irá demonstrar as notas por Ato Legal, da mesma forma feita para os demais benefícios\.

MFS31771

__MFS31697__

RN15

__Critérios para a recuperação dos documentos da X07\_DOCTO\_FISCAL para cliente que utilizam X51\_ITENS\_FRETE__

__ __

__Espécie de Benefício: Crédito Presumido__

__ __

__Tipo de Cálculo do Benefício = 02 \- Crédito presumido sobre saídas:__

 

    \- Empresa = código da empresa do login;

 

    \- Estabelecimento = código do estabelecimento da geração; 

 

    \- Data Fiscal = deve ser uma data referente ao período informado em tela de cálculo do benefício;

    \- Movto\_E\_S = “9” \(somente saídas\)

 

    \- Somente notas não canceladas;

 

    \- Considerar todos os itens com CFOP ou CFOP/Natureza parametrizados na Parametrização do Benefício – Crédito Presumido __\(\*\*\): __ \(menu Parâmetros  Benefícios – Credito Presumido   Parâmetros Gerais de Cálculo por CFOP ou CFOP/Natureza\) para a Espécie de Benefício = ‘Crédito Presumido’ e Cálculo do Benefício = ‘2 \- Crédito presumido sobre saídas’ __exceto__ os produtos que estejam parametrizados na Parametrização dos Produtos Excluídos – Crédito Presumido  \(menu Parâmetros  Benefício – Credito Presumido  Produtos Excluídos – Crédito Presumido\) para o mesmo CFOP ou CFOP/Natureza\. 

 

    \- Considerar a alíquota cadastrada na Parametrização do Benefício – Crédito Presumido __\(\*\*\)\]__

__\[ALTERAÇÃO\-MFS\] __Alteração da regra de cálculo específico para as operações de Serviços de Transportes, \(COD\_CLASS\_DOC\_FIS = ‘4'

 

__Totalização do valor:__

 

     

O valor de cada item a ser totalizado será recuperado do campo VLR\_TOT\_NOTA da X07\_DOCTO\_FISCAL, ou do campo VLR\_TRIBUTO\_ICMS \(Valor de ICMS\) da X07\_DOCTO\_FISCAL, caso seja uma operação de serviço de Transporte\.

    

__Cálculo do Valor do ICMS Não debitado:__

     

Para cada item processado, calcular o valor do ICMS Não debitado da seguinte forma:

Valor Documento Fiscal = Valor Total do Documento Fiscal \(Campo __VLR\_TOT\_NOTA__ – __X07\_DOCTO\_FISCAL__\) __OU__

__SE __o campo __*COD\_CLASS\_DOC\_FIS*__ da tabela __*DWT\_DOCTO\_FISCAL*__ for igual a ‘__4__’ \(Conhecimentos Fretes \- SAFX 51\)

  __PREENCHER__ o campo “Valor da Operação” com o valor do campo __*VLR\_TRIBUTO\_ICMS*__ da tabela __*DWT\_DOCTO\_FISCAL*__ \(Valor do ICMS\)\.

 

Valor de ICMS Não debitado = Valor da Operação x Alíquota parametrizada % __\(\*\) __

MFS46075

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

