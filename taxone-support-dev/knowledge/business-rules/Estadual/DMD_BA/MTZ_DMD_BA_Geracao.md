# MTZ_DMD_BA_Geracao

- **Fonte:** MTZ_DMD_BA_Geracao.docx
- **Modificado:** 2022-06-06
- **Tamanho:** 55 KB

---

__MÓDULO DMD\-BA – Geração do meio Magnético\.__

__Localização__: Módulo Estadual > DMD – BA > Geração > Geração do Meio Magnético

###### DR

###### Nome

__Descrição__

OS3805\-A

Jefferson Mota  

Geração do Meio magnético e definições de regras\.

MFS\-29457

Alessandra Cristina Navatta

Ajuste no meio magnético do registro 02 \- Entrada, nos campos Valor Comercial Cont\. Inscrito e Valor Comercial Cont\. Não Inscrito \(regras RN02\-09 e RN02\-11\), para considerar o campo 64 \- VLR\_CONTAB\_ITEM da SAFX08\.

MFS41467

Vânia Mattos

Alterada regra de identificação dos contribuintes inscritos/não inscritos no caso dos Produtores Rurais 

MFS44435

Vânia Mattos

A geração da DMD foi alterada para utilizar a nova parametrização de Grupo DMD x CFOP \(ver __RN02\-00__,__ RN02\-01__,__ RN03\-00__ e __RN03\-01__\) 

Registro 00: Registro Mestre da DMD\-BA

RN00\-00

__Origens das Informações: __Tela de Responsável por Informações

__Regra de Seleção: __O registro “00” é o registro com todas as informações iniciais do arquivo\. Ele será gerado com os dados do cadastro do responsável pela obrigação, que foi indicado na tela de dados inciais da DMD\. 

__Campos\-chave do registro__: 04 \- CPF/CNPJ\.

OS3805\-A

RN00\-04

__Registro 00: Número do CPF do Responsável__

Preencher com o conteúdo do campo “CPF/CNPJ” da tabela dos Responsáveis por Informação \(NUM\_CPF\)\. De acordo com o cadastro realizado na tela dos Dados Iniciais da obrigação\.

*OBS: Na verdade este campo contém sempre o CPF, e nunca o CNPJ, pois tem apenas 11 posições\. Quando o responsável é da categoria “Empresa”, e portanto tem um CNPJ, esta informação fica apenas na tabela dos responsáveis contadores \(RESP\_CONTADOR\)\. *

OS3805\-A

RN00\-05

__Registro 00: Nome do responsável pela Declaração__

Recuperar a informação do__ Nome do Responsável __informado na tela Parâmetros > Dados Iniciais do módulo DMD – BA, considerando as 35 posições primeiras do nome\.

OS3805\-A

Registro 01: Identificação da Empresa do DMD

RN01\-00

__Origens das Informações:  __Tabelas SAFX04, SAFX08 e Tela de Parâmetros por Produto\.

__Regra de seleção: __O registro 01 será utilizado para demonstrar o produto diferido por estabelecimento\. Ele será gerado, considerando as informações de período e estabelecimento parametrizadas na tela de geração, produto parametrizado na tela de Parâmetros por Produto\.

Para a seleção das informações serão considerados os registros da SAFX08, que tenham no campo 13\-Indicador do Produto e 14\-Produto, os produtos parametrizados na tela de Parâmetros por Produtos, considerando apenas os produtos cujo o campo Status do Produto seja igual a “Normal”, ou os produtos com status “Motivo de Baixa”, desde que o campo Referência da Baixa seja maior ou igual ao período inicial e menor ou igual ao período final, cujo o estabelecimento e data fiscal correspondam aos critérios parametrizados na tela de geração, desconsiderando os itens de notas fiscais canceladas e considerando somente itens diferidos, ou seja, que tenha o campo 31\- Tabela Situação Estadual “B” com conteúdo igual a “51”\. As notas devem ser recuperadas de acordo com a parametrização de CFOP ou CFOP Natureza\.  Se na tela de geração for informado um código de produto diferido, considerar na seleção somente o produto indicado\.

Não devem ser geradas informações de produtos baixados após o período de referência da baixa\. Ex\.:

Produto 001, baixado em 05/2013

Período de geração: 01/2013 a 07/2013

Neste caso, considera\-se a movimentação do período até o mês 05/2013, sendo que, neste mês ele será gerado com Motivo de Baixa “S”\.

Na geração por inscrição estadual única, serão recuperados os dados de todos os estabelecimentos envolvidos na centralização*\.*

As informações desse registro devem ser agrupadas, considerando os campos chaves informados abaixo\.

__Campos\-chave do registro__: Ano de Referência da DMD, Mês de referência da DMD, Número de inscrição estadual, Código Produto Diferimento, Número Habilitação\.

RN01\-02

__Registro 01: Ano de Referência__

Este campo deverá ser gerado com o __Ano__ informado na data fiscal do produto selecionado na SAFX08\.

OS3805\-A

RN01\-03

__Registro 01: Mês de Referência__

Este campo deverá ser gerado com o __Mês__ informado na data fiscal do produto selecionado na SAFX08\.

OS3805\-A

RN01\-04

__ Registro 01: Número de Inscrição Estadual__

Recuperar a informação da Inscrição Estadual do estado da BA do estabelecimento selecionado na geração da DMD\-BA\.

OS3805\-A

RN01\-05

__Registro 01: Retificação__

Se o campo Tipo de Declaração da tela de Geração for igual a “Retificadora” gerar S, se não gerar N\.

__\- __Informar __S__ se a declaração for retificadora

__\- __Informar __N__ se a declaração não for retificadora

OS3805\-A

RN01\-06

__Registro 01: Motivo de Baixa__

Se o campo Tipo de Declaração da tela de Geração for igual a “Baixa” gerar S para todos os produtos\.

Se o campo Status do Produto da tela de Parâmetros por Produtos, para o produto que esta sendo gerado no registro 01 for igual a motivo de baixa, e o campo referência da baixa deste mesmo produto for igual ao mês/ano de referência do registro, gerar S para o produto baixado\.

Para outras situações gerar N\.

__\- __Informar __S__ se a declaração for por motivo de baixa

__\- __Informar __N__ se a declaração não for por motivo de baixa

OS3805\-A

RN01\-07

__Registro 01: Código do Produto Diferimento__

Este campo deverá ser preenchido com as informações do código do produto da DMD, informado no campo “Grupo Produto” da tela Parâmetros por Produto\.

OS3805\-A

RN01\-09

__Registro 01: Razão Social__

Este campo deve ser gerado com a informação da __Razão Social__ da tabela ESTABELECIMENTO, que está gerando o Meio Magnético\.

OS3805\-A

RN01\-12

__Registro 01: Numero Habilitação__

Recuperar a informação do campo Nº Habilitação preenchido na tela de Parâmetros por Produto da DMD – BA\.

OS3805\-A

RN01\-15

__Registro 01: Código de Município__

Deve ser recuperada a informação do campo COD\_MUNICIPIO da tabela ESTABELECIMENTO, realizando a conversão para a demonstração do código no formato da tabela de municípios da Bahia\.

OS3805\-A

Registro 02: Entradas

RN02\-00

__Origens das Informações:__

\- SAFX04

\- SAFX07/SAFX08

\- Parâmetros por Produto

\- Parametrização das Operações

\- Parametrização das Operações por Grupo DMD \(__MFS44435__, Nov/2020\)

__Regra de Seleção:  __O registro 02 contém informações de entrada do produto\. Ele será gerado, considerando as informações de período e estabelecimento parametrizadas na tela de geração, produto parametrizado na tela de Parâmetros por Produto e código de município\.

Este registro será gerado, considerando as informações da Data fiscal da SAFX07 que deve ser compreendida dentro do mês e ano da geração do meio magnético, onde o campo de movimento Entrada/Saída seja um movimento de “Entrada” e o campo Normal/Devolução deverá estar qualificado como "Normal"\. Deve ser verificada a situação da nota devendo estar com situação "N" \(Nota Fiscal Não Cancelada\) e deverá considerar o produto da tabela SAFX08 vinculado à tabela de Parâmetros por Produto do módulo DMD\-BA, considerando apenas os produtos cujo o campo Status do Produto seja igual a “Normal”, ou os produtos com status “Motivo de Baixa”, desde que o campo Referência da Baixa seja maior ou igual ao período inicial e menor ou igual ao período final, devendo considerar o campo COD\_SITUACAO\_B da SAFX08 = “51”, ou seja, somente itens diferidos\. As notas devem ser recuperadas de acordo com a parametrização de CFOP ou CFOP Natureza\.

Não devem ser geradas informações de produtos baixados após o período de referência da baixa\. Ex\.:

Produto 001, baixado em 05/2013

Período de geração: 01/2013 a 07/2013

Neste caso, considera\-se a movimentação do período até o mês 05/2013, sendo que, neste mês ele será gerado com Motivo de Baixa “S”\.

Na geração por inscrição estadual única, serão recuperados os dados de todos os estabelecimentos envolvidos na centralização*\.*

__Campos\-chave do registro__: Ano de Referência da DMD, Mês de Referência da DMD, Número de Inscrição Estadual, Código do Produto Diferimento, Código de Entrada e Código do Município\.

\.

OS3805\-A

__MFS44435__

RN02\-01

__Processamento dos itens recuperados:__

Os Grupos da DMD, e os itens de documento fiscal \(SAFX08\), recuperados conforme as regras descritas na RN02\-00, serão processados da seguinte forma:

Os valores dos itens são consolidados por Município e Grupo Produto DMD\.

Os valores de cada item são lançados no Grupo DMD para o qual o produto esta parametrizado\. Esta associação do item ao Grupo DMD, independe do CFOP ou NAT\. Assim, basta que o produto esteja parametrizado para um Grupo DMD, que todas as suas operações serão lançadas neste Grupo DMD, seja qual for o CFOP ou NAT do item na SAFX08, desde que estejam parametrizados \(“Parametrização das Operações”\)\.

__MFS44435: __Nesta mfs foi criada uma nova parametrização de CFOP e CFOP/NAT, no menu “*Parametrização das Operações por Grupo DMD*”\. Esta nova parametrização por Grupo DMD é opcional, e tem como objetivo corrigir a duplicidade que ocorria quando um produto era parametrizado para mais de um Grupo DMD\. Com a sua criação, a geração passou a funcionar da seguinte forma:

*\(Importante: Observar que os critérios de recuperação dos itens na SAFX08 não se altera, ou seja, a parametrização das operações original, menu “Parametrização das Operações”, continua a ser obrigatória, e serve como filtro dos itens que serão considerados na geração\)  *

__Se o produto do item da nota estiver parametrizado para mais de um Grupo DMD:__

     \[ Nesta verificação, são considerados apenas os Grupos DMD da parametrização que estejam

       válidos, conforme a RN02\-00, ou seja, que tenham o \(*Status do Produto = “Normal”*\) __ou__

__       __\(Status do Produto = “Motivo de Baixa” e “Ref\. Baixa” seja um mês/ano >= ao mês/ano do 

       período final informado na tela da geração\) \]

 

     Nesse caso, o valor do item será lançado em apenas um dos Grupos DMD, o que depende do

     CFOP ou CFOP/NAT do item, da seguinte forma: para verificar qual será o grupo, é feita a

     pesquisa na parametrização do menu “*Parametrização das Operações por Grupo DMD*”, com 

     objetivo de identificar em qual dos Grupos DMD associados ao produto, que o CFOP ou 

     CFOP/NAT do item esta parametrizado\. O grupo identificado, é justamente o grupo que 

     recebe o valor do item em questão\. 

     Caso não seja identificado o CFOP ou CFOP/NAT na parametrização, para nenhum dos Grupos

     DMD relacionados ao produto \(ou mesmo nenhum dos grupos tenha sido parametrizado\), o

     item em questão *será desconsiderado da geração* e no log será gerada a seguinte mensagem

     de aviso: *“Item desconsiderado da geração, pois o Produto esta parametrizado para mais de*

*     um Grupo da DMD, e não foi possível identificar através de CFOP ou NAT, a qual grupo DMD o*

*     item se refere\. Consultar o help das parametrizações do módulo”  *

     O log deve demonstrar os dados de identificação do item da nota, para que o usuário possa

     identificar o problema\.

__Senão  \(o produto do item da nota esta parametrizado para um único Grupo DMD\)__

     Nesse caso, será verificado se o Grupo DMD para qual o produto esta parametrizado, consta

     na parametrização do menu “*Parametrização das Operações por Grupo DMD*”: 

     Caso sim: será verificado se o CFOP ou CFOP/NAT do item esta parametrizado para o grupo, e

     se sim, o valor do item será lançado normalmente para o Grupo DMD em questão\. Mas, se o 

     grupo constar na parametrização, mas o CFOP ou CFOP/NAT não estiver parametrizado para

     este grupo, o item *será desconsiderado da geração* e no log será gerada uma mensagem de

     aviso: *“Item desconsiderado da geração, pois o Grupo DMD do produto consta na*

*     parametrizado das operações por Grupo DMD, mas a operação do item não esta *

*    parametrizada \(CFOP ou Nat\)\. Consultar o help desta parametrização”  *

     Caso não: o valor do item será lançado normalmente para o Grupo DMD em questão *\(nesse* 

*     caso, como o produto esta associado a apenas um Grupo DMD, e o grupo não consta*

*     na parametrização das operações por Grupo DMD, signifca que o grupo pode receber *

*     qualquer tipo de operação\) *

__Exemplo:__ Ver o exemplo que consta no final deste documento\. Neste exemplo foi descrito um cenário que mostra a aplicação das regras descritas acima, referentes ao funcionamento da geração da DMD após a criação da Parametrização das Operações por Grupo DMD __\(MFS44435\)__\.

__MFS44435__

RN02\-02

__Registro 02: Ano de Referência__

Este campo deverá ser gerado com o __Ano__ informado na data fiscal do produto selecionado na SAFX08\. Deve ser o mesmo ano informado na linha 01\.

OS3805\-A

RN02\-03

__Registro 02: Mês de Referência__

Este campo deverá ser gerado com o __Mês__ informado na data fiscal do produto selecionado na SAFX08\. Deve ser o mesmo mês informado na linha 01\.

OS3805\-A

RN02\-04

__Registro 02: Número de Inscrição Estadual__

Recuperar a informação da Inscrição Estadual do estado da BA do estabelecimento selecionado na geração da DMD\-BA\.

OS3805\-A

RN02\-05

__Registro 02: Código do Produto Diferimento__

Este campo deverá ser preenchido com as informações do código do produto da DMD, informado no campo “Grupo Produto” da tela Parâmetros por Produto\.

OS3805\-A

RN02\-07

__Registro 02: Código do Município__

Recuperar a informação do Município da SAFX04 da Pessoa Fis/Jur da nota fiscal, realizando a conversão para a demonstração do código no formato da tabela de municípios da Bahia\.

Se a pessoa Fis/Jur for de FORA do estado da BA, deverá ser gerada a informação padrão “99994”\.

Se a pessoa Fis/Jur for do EXTERIOR deverá ser gerada a informação padrão “88888”\.

OS3805\-A

RN02\-08

__Registro 02: Quantidade Cont\. Inscrito__

Deverá ser recuperada a informação do campo QUANTIDADE da SAFX08, quando a pessoa FIS/JUR da referida nota fiscal possuir no campo inscrição estadual o conteúdo diferente de “ISENTO” __e__ o campo “Produtor Rural” for = “__N__”\.

__MFS41467:__ Conforme o item “Considerações Gerais” do manual da DMD\-BA, *todos* os produtores rurais, sejam eles inscritos ou não inscritos, no Cadastro do ICMS da BA, devem ser considerados como “não inscritos”\. Esta regra vale para os 4 campos \(RN02\-08, RN02\-09, RN02\-10 e RN02\-11\)\.

OS3805\-A

__MFS41467__

RN02\-09

__Registro 02: Valor Comercial Cont\. Inscrito__

Deverá ser recuperada a informação do campo  VLR\_CONTAB\_ITEM da SAFX08, quando a pessoa FIS/JUR da referida nota fiscal possuir no campo inscrição estadual o conteúdo diferente de “ISENTO” __e__ o campo “Produtor Rural” for = “__N__”\.

OS3805\-A

MFS29457

__MFS41467__

RN02\-10

__Registro 02: Quantidade Cont\. Não Inscrito__

Deverá ser recuperada a informação do campo QUANTIDADE da SAFX08, quando a pessoa FIS/JUR da referida nota fiscal possuir no campo inscrição estadual o conteúdo igual a “ISENTO”

__*ou*__ o campo “Produtor Rural” for = “__S__”\.

OS3805\-A

__MFS41467__

RN02\-11

__Registro 02: Valor Comercial Cont\. Não Inscrito__

Deverá ser recuperada a informação do campo VLR\_CONTAB\_ITEM da SAFX08, quando a pessoa FIS/JUR da referida nota fiscal possuir no campo inscrição estadual o conteúdo igual a “ISENTO”

__*ou*__ o campo “Produtor Rural” for = “__S__”\.

OS3805\-A

MFS29457

__MFS41467__

	

Registro 03: Saídas

RN03\-00

__Origens das Informações:__

\- SAFX04

\- SAFX07/SAFX08

\- Parâmetros por Produto

\- Parametrização das Operações

\- Parametrização das Operações por Grupo DMD \(__MFS44435__, Nov/2020\)

__Regra de Seleção: __O registro 03 contém informações de saída do produto\. Ele será gerado, considerando as informações de período e estabelecimento parametrizadas na tela de geração, produto parametrizado na tela de Parâmetros por Produto e código de município\.

Este registro será gerado, considerando as informações da Data fiscal da SAFX07 que deve ser compreendida dentro do mês e ano da geração do meio magnético, onde o campo de movimento Entrada/Saída seja um movimento de “Saída” e o campo Normal/Devolução deverá estar qualificado como "Normal"\. Deve ser verificada a situação da nota devendo estar com situação "N" \(Nota Fiscal Não Cancelada\) e deverá considerar o produto da tabela SAFX08 vinculado à tabela de Parâmetros por Produto do módulo DMD\-BA, considerando apenas os produtos cujo o campo Status do Produto seja igual a “Normal”, ou os produtos com status “Motivo de Baixa”, desde que o campo Referência da Baixa seja maior ou igual ao período inicial e menor ou igual ao período final, devendo considerar o campo COD\_SITUACAO\_B da SAFX08 = “51”, ou seja, somente itens diferidos\. As notas devem ser recuperadas de acordo com a parametrização de CFOP ou CFOP Natureza\.

Não devem ser geradas informações de produtos baixados após o período de referência da baixa\. Ex\.:

Produto 001, baixado em 05/2013

Período de geração: 01/2013 a 07/2013

Neste caso, considera\-se a movimentação do período até o mês 05/2013, sendo que, neste mês ele será gerado com Motivo de Baixa “S”\.

Na geração por inscrição estadual única, serão recuperados os dados de todos os estabelecimentos envolvidos na centralização*\.*

__Campos\-chave do registro__: Ano de Referência da DMD, Mês de Referência da DMD, Número de Inscrição Estadual, Código do Produto Diferimento, Código Entrada/Saída e Código do Município\.

OS3805\-A

__MFS44435__

RN03\-01

__Processamento dos itens recuperados:__

Os Grupos da DMD, e os itens de documento fiscal \(SAFX08\), recuperados conforme as regras descritas na RN03\-00, serão processados da seguinte forma:

Os valores dos itens são consolidados por Município e Grupo Produto DMD\.

Os valores de cada item são lançados no Grupo DMD para o qual o produto esta parametrizado\. Esta associação do item ao Grupo DMD, independe do CFOP ou NAT\. Assim, basta que o produto esteja parametrizado para um Grupo DMD, que todas as suas operações serão lançadas neste Grupo DMD, seja qual for o CFOP ou NAT do item na SAFX08, desde que estejam parametrizados \(“Parametrização das Operações”\)\.

__MFS44435: __Nesta mfs foi criada uma nova parametrização de CFOP e CFOP/NAT, no menu “*Parametrização das Operações por Grupo DMD*”\. Esta nova parametrização por Grupo DMD é opcional, e tem como objetivo corrigir a duplicidade que ocorria quando um produto era parametrizado para mais de um Grupo DMD\. Com a sua criação, a geração passou a funcionar da seguinte forma:

*\(Importante: Observar que os critérios de recuperação dos itens na SAFX08 não se altera, ou seja, a parametrização das operações original, menu “Parametrização das Operações”, continua a ser obrigatória, e serve como filtro dos itens que serão considerados na geração\)  *

__Se o produto do item da nota estiver parametrizado para mais de um Grupo DMD:__

     \[ Nesta verificação, são considerados apenas os Grupos DMD da parametrização que estejam

       válidos, conforme a RN02\-00, ou seja, que tenham o \(*Status do Produto = “Normal”*\) __ou__

__       __\(Status do Produto = “Motivo de Baixa” e “Ref\. Baixa” seja um mês/ano >= ao mês/ano do 

       período final informado na tela da geração\) \]

 

     Nesse caso, o valor do item será lançado em apenas um dos Grupos DMD, o que depende do

     CFOP ou CFOP/NAT do item, da seguinte forma: para verificar qual será o grupo, é feita a

     pesquisa na parametrização do menu “*Parametrização das Operações por Grupo DMD*”, com 

     objetivo de identificar em qual dos Grupos DMD associados ao produto, que o CFOP ou 

     CFOP/NAT do item esta parametrizado\. O grupo identificado, é justamente o grupo que 

     recebe o valor do item em questão\. 

     Caso não seja identificado o CFOP ou CFOP/NAT na parametrização, para nenhum dos Grupos

     DMD relacionados ao produto \(ou mesmo nenhum dos grupos tenha sido parametrizado\), o

     item em questão *será desconsiderado da geração* e no log será gerada a seguinte mensagem

     de aviso: *“Item desconsiderado da geração, pois o Produto esta parametrizado para mais de*

*     um Grupo da DMD, e não foi possível identificar através de CFOP ou NAT, a qual grupo DMD o*

*     item se refere\. Consultar o help das parametrizações do módulo”  *

     O log deve demonstrar os dados de identificação do item da nota, para que o usuário possa

     identificar o problema\.

__Senão  \(o produto do item da nota esta parametrizado para um único Grupo DMD\)__

     Nesse caso, será verificado se o Grupo DMD para qual o produto esta parametrizado, consta

     na parametrização do menu “*Parametrização das Operações por Grupo DMD*”: 

     Caso sim: será verificado se o CFOP ou CFOP/NAT do item esta parametrizado para o grupo, e

     se sim, o valor do item será lançado normalmente para o Grupo DMD em questão\. Mas, se o 

     grupo constar na parametrização, mas o CFOP ou CFOP/NAT não estiver parametrizado para

     este grupo, o item *será desconsiderado da geração* e no log será gerada uma mensagem de

     aviso: *“Item desconsiderado da geração, pois o Grupo DMD do produto consta na*

*     parametrizado das operações por Grupo DMD, mas a operação do item não esta *

*    parametrizada \(CFOP ou Nat\)\. Consultar o help desta parametrização”  *

     Caso não: o valor do item será lançado normalmente para o Grupo DMD em questão *\(nesse* 

*     caso, como o produto esta associado a apenas um Grupo DMD, e o grupo não consta*

*     na parametrização das operações por Grupo DMD, signifca que o grupo pode receber *

*     qualquer tipo de operação\) *

__Exemplo:__ Ver o exemplo que consta no final deste documento\. Neste exemplo foi descrito um cenário que mostra a aplicação das regras descritas acima, referentes ao funcionamento da geração da DMD após a criação da Parametrização das Operações por Grupo DMD __\(MFS44435\)__\.

__MFS44435__

RN03\-02

__Registro 03: Ano de Referência__

Este campo deverá ser gerado com o __Ano__ informado na data fiscal do produto selecionado na SAFX08\. Deve ser o mesmo ano informado na linha 01\.

OS3805\-A

RN03\-03

__Registro 03: Mês de Referência__

Este campo deverá ser gerado com o __Mês__ informado na data fiscal do produto selecionado na SAFX08\. Deve ser o mesmo mês informado na linha 01\.

OS3805\-A

RN03\-04

__Registro 03: Número de Inscrição Estadual__

Recuperar a informação da Inscrição Estadual do estado da BA do estabelecimento selecionado na geração da DMD\-BA

OS3805\-A

RN03\-05

__Registro 03: Código do Produto Diferimento__

Este campo deverá ser preenchido com as informações do código do produto da DMD, informado no campo “Grupo Produto” da tela Parâmetros por Produto\.

OS3805\-A

RN03\-07

__Registro 03: Código do Município__

Recuperar a informação do Município da SAFX04 da Pessoa Fis/Jur da nota fiscal, realizando a conversão para a demonstração do código no formato da tabela de municípios da Bahia\.

Se a pessoa Fis/Jur for de FORA do estado da BA, deverá ser gerada a informação padrão “99994”\.

Se a pessoa Fis/Jur for do EXTERIOR deverá ser gerada a informação padrão “88888”\.

OS3805\-A

RN03\-08

__Registro 03: Quantidade Cont\. Inscrito__

Deverá ser recuperada a informação do campo QUANTIDADE da SAFX08, quando a pessoa FIS/JUR da referida nota fiscal possuir no campo inscrição estadual, o conteúdo diferente de “ISENTO” __e__ o campo “Produtor Rural” for = “__N__”\.

__MFS41467:__ Conforme o item “Considerações Gerais” do manual da DMD\-BA, *todos* os produtores rurais, sejam eles inscritos ou não inscritos, no Cadastro do ICMS da BA, devem ser considerados como “não inscritos”\. Esta regra vale para os 4 campos \(RN03\-08, RN03\-09, RN03\-10 e RN03\-11\)\.

OS3805\-A

__MFS41467__

RN03\-09

__Registro 03: Valor Comercial Cont\. Inscrito__

Deverá ser recuperada a informação do campo VLR\_ITEM da SAFX08, quando a pessoa FIS/JUR da referida nota fiscal possuir no campo inscrição estadual o conteúdo diferente de “ISENTO”

__e__ o campo “Produtor Rural” for = “__N__”\.

OS3805\-A

__MFS41467__

RN03\-10

__Registro 03: Quantidade Cont\. Não Inscrito__

Deverá ser recuperada a informação do campo QUANTIDADE da SAFX08, quando a pessoa FIS/JUR da referida nota fiscal possuir no campo inscrição estadual o conteúdo igual a “ISENTO”

__*ou*__ o campo “Produtor Rural” for = “__S__”\.

OS3805\-A

__MFS41467__

RN03\-11

__Registro 03: Valor Comercial Cont\. Não Inscrito__

Deverá ser recuperada a informação do campo VLR\_ITEM da SAFX08, quando a pessoa FIS/JUR da referida nota fiscal possuir no campo inscrição estadual o conteúdo igual a “ISENTO” __*ou*__ o campo “Produtor Rural” for = “__S__”\.

OS3805\-A

__MFS41467__

Registro 99: Encerramento

RN99\-00

__Regra de Seleção: __O registro 99 é o registro de encerramento do arquivo que foi gerado, onde deverá constar a informação padrão do tipo de registro e o total de “Registros 01” que foram gerados no arquivo\.

OS3805\-A

RN99\-02

__Registro 99: Quantidade de Registros__

Este campo deve sumarizar a quantidade de registros 01 gerados no Meio Magnético\.

OS3805\-A

RN99\-03

__Regra de criação do nome do arquivo: __

O arquivo deverá ser gerado com a seguinte nomenclatura:

__    111111\_DMD\_TR\.TXT__

Onde__:__

__111111\_ :__é o número do processo

__DMD\_TR: __nomenclatura obrigatória do arquivo DMD\-BA\.

__\.TXT:__ extensão do arquivo

__Se __o__ __parâmetro “Gera Arquivo S/ N° Processo” estiver selecionado, o sistema deverá gerar o arquivo sem o número de processo conforme exemplo abaixo:

__DMD\_TR\.TXT         __

Onde__:__

__DMD\_TR: __nomenclatura obrigatória do arquivo DMD\-BA\.

__\.TXT:__ extensão do arquivo

OBS\.: Este tratamento se aplica, apenas quando for salvar o arquivo na máquina\.__         __

OS3805\-A

__Exemplo:   __\(exemplo referenciado na __RN02\-01__ e __RN03\-01__\)

Exemplo da geração da DMD em relação às parametrizações:

__Período da Geração__: __01/2018__

__Parametrização dos Produtos:__

__Grupo DMD__

__Produtos __

__Status__

__Referência da Baixa __

ABC

001, 002

Normal

DEV\-1

999

Normal

DEV\-2

999

Normal

PRL\-1

222, 888

Normal

PRL\-2

888

Normal

STO\-1

444

Normal

STO\-2

444

Normal

CAD\-1

777

Motivo de Baixa

12/2017

CAD\-2

777

Normal

 

__Parametrização das Operações:__

__Operação__

__CFOP’s__

Entradas

1101, 1102, 2101, 2102

Saídas

5101, 5102, 6101, 6102

  


__Parametrização das Operações por Grupo DMD:__

__Grupo DMD__

__CFOP’s__

DEV\-1

1101, 1102

DEV\-2

2101, 2102

PRL\-1

5101

PRL\-2

5102, 6102

 

__Notas fiscais__ 

\(todas da Jan/2018\)

Na coluna “__OBS__” esta descrito o resultado, indicando se o item da nota foi, ou não, considerado na geração\. 

Se sim, para qual Grupo DMD\. E senão, qual foi o motivo que levou o item a ser desconsiderado\.

__Nota__

__Item__

__Produto__

__CFOP__

__OBS__

1

1

001

1101

Este item será lançado no Grupo DMD “ABC”

2

002

1102

Este item será lançado no Grupo DMD “ABC”

2

1

999

1101

Este item será lançado no Grupo DMD “DEV\-1” 

3

1

999

2101

Este item será lançado no Grupo DMD “DEV\-2”

4

1

001

6101

Este item será lançado no Grupo DMD “ABC”

4

1

002

5103

Este item __*não*__ será considerado na geração, pois seu CFOP não foi parametrizado em “*Parametrização das Operações*”

\(neste caso não é gerado log, pois esta parametrização tem por objetivo definir as operações a serem consideradas na DMD\)

5

1

999

1103

Este item __*não*__ será considerado na geração, pois seu CFOP não foi parametrizado em “*Parametrização das Operações*”

\(neste caso não é gerado log, pois esta parametrização tem por objetivo definir as operações a serem consideradas na DMD\.\)

6

1

999

5101

Este item __*não*__ será considerado na geração\. Trata\-se de um produto parametrizado para mais de um Grupo DMD, e por isso, o seu CFOP \(5101\) deveria constar na parametrização do menu “*Parametrização das Operações por Grupo DMD*”, para algum dos seus grupos \(DEV\-1 ou DEV\-2\)\. 

Msg no log: *“Item desconsiderado da geração, pois o Produto esta parametrizado para mais de um Grupo da DMD, e não foi possível identificar através de CFOP ou NAT, a qual grupo DMD o item se refere\. Consultar o help das parametrizações do módulo” *

7

1

888

5101

Este item será lançado no Grupo DMD “PRL\-1”

2

888

5102

Este item será lançado no Grupo DMD “PRL\-2”

8

1

222

5101

Este item será lançado no Grupo DMD “PRL\-1”

9

1

222

6102

Este item __*não*__ será considerado na geração\. Apesar de tratar\-se de um produto associado a apenas um Grupo DMD \(PRL\-1\), como este grupo consta na parametrização do menu “*Parametrização das Operações por Grupo DMD*”, o grupo só deve receber os CFOP’s parametrizados para ele\.E no caso, o CFOP 6102 não esta parametrizado para o grupo PRL\-1\. 

Msg no log:* “Item desconsiderado da geração, pois o Grupo DMD do*

*produto consta na parametrizado das operações por Grupo DMD, mas a operação do item não esta parametrizada \(CFOP ou Nat\)\. Consultar o help desta parametrização”*

10

1

444

1101

Este item __*não*__ será considerado na geração\. Trata\-se de um produto parametrizado para mais de um Grupo DMD, e por isso, o seu CFOP \(1101\) deveria constar na parametrização do menu “*Parametrização das Operações por Grupo DMD*”, para algum dos seus grupos \(STO\-1 ou STO\-2\)\. 

Msg no log: *“Item desconsiderado da geração, pois o Produto esta parametrizado para mais de um Grupo da DMD, e não foi possível identificar através de CFOP ou NAT, a qual grupo DMD o item se refere\. Consultar o help das parametrizações do módulo”*

11

1

777

6101

Este item será lançado no Grupo DMD “CAD\-2”

Observar que, apesar de na parametrização este produto estar parametrizado para dois Grupos DMD \(CAD\-1 e CAD\-2\), o grupo CAD\-1 consta como baixado em período anterior \(12/2017\), e por isso, não é mais válido\. Assim, a partir de Jan/2018, o produto é tratado como um produto associado a um único Gripo DMD, que no caso é o CAD\-2\.

= = = = = 

