# MTZ-ICMS-Parametros_por_UF

- **Fonte:** MTZ-ICMS-Parametros_por_UF.docx
- **Modificado:** 2026-02-05
- **Tamanho:** 64 KB

---

# Módulo – ICMS – Parâmetros por UF 

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__OS2609\-D__

Alteração nos Livros

Para que os Livros de Saídas sejam emitidos corretamente, deverá ser criado um campo “Consumidor Final” na capa de Utilities, complementar os CFOP´s de Não Contribuintes Estaduais,corrigir os resumos de Decêndio, Quinzena e Código de Receita, excluir o Label  “Desconsiderar valor de descontos no cálculo do valor contábil” da tela do Geração do Mapa Resumo/Geração do meio magnético do convênio 115  e  criar uma parametrização para unificar as configurações nos Parâmetros por UF da tela de Geração dos Mapas Resumo  e  Livros de Saídas\.

__CH53090__

__OS 2715__

Item 77 e 78 

Corrigir a parte principal dos livros fiscais de entrada e saídas quando os parâmetros 77 e 78 em Parâmetros por UF __não__ estiverem selecionados\.

__OS 2715__

__CH54397__

Alteração OBS Livros Entrada e Saídas

Alterar as observações nos livros de ICMS de entradas e saídas geradas pelos parâmetros por UF 23 e 25, que geram observações de ICMS\-S, quando a NF é tributada\. Atualmente gera apenas o valor do imposto, mas conforme RICMS\-SP, arts 275 \(LS\) e 276 \(LE\), também é necessário incluir o valor da base de cálculo\.

__OS3008__

Entradas \- IPI não escriturado no campo de observações

O objetivo dessa OS é permitir que o valor do campo IPI não escriturado do item da nota fiscal seja informado no Livro de Entradas, na coluna observação\.

__OS3384__

Regra para observações dos livros P1 e P2

Regra para o parâmetro “87 \- Considerar Observações de Informações Complementares da Nota \(SAFX112\) para livros \(P1 e P2\)”\.

__OS3424\-A__

Alteração na regra do Parâmetro 84

Alteração na regra do Parâmetro 84, conforme alteração do Decreto 57\.177/2011

__OS3527__

Alteração da GI/ICMS

Inclusão de parâmetro para utilização na geração e emissão da GI/ICMS \(RN13\)\.

__OS3659__

Alteração no Livro de Apuração do ICMS

Criação de um novo parâmetro para que os CFOP’s zerados sejam exibidos nos resumos por CFOP do P9 \(vide __RN14__\)\.

__OS3046__

Livro de Saídas

Alteração da observação “Faturamento Direto ao Consumidor”, que passará a utilizar dois formatos distintos \(vide __RN15__\)\.

__CH21822\-A\_2012__

Parâmetro por UF \- 32 

Correção no parâmetro 32 – Descrição para cabeçalho dos Livros Fiscais \(por folha ou por página\)

__OS3972__

Parâmetro 90

Inclusão do Parâmetro 90 – Demonstrar Operações por Indicador de Produto e Situação Tributária

__MFS2131__

Nova Apuração do Ato Cotepe 44

Criação de novo parâmetro p/atendimento ao Ato Cotepe/ICMS 44/2015 \(ver __RN16__\)

__MFS6817__

Novo Cálculo de diferencial de alíquota para RS\.

Criação de novo parâmetro p/atendimento a Instrução Normativa RE Nº 39/2016 \(ver RN17\)

__MF11722__

Novo Cálculo de diferencial de alíquota para PR e GO\.

Alteração do parâmetro 92, sobre o cálculo do Diferencial de Alíquotas \(ver __RN17__\)\.

__CH14249\_2017 \(MFS\-14393\)__

Alteração Parâmetro 67

Esse documento tem como objetivo alterar o funcionamento do Parâmetro 67\-Lançar Campo UF Origem/Destino do Documento Fiscal nos Livros Fiscais \(Movimentos/Resumo por UF\) para considerar aquisição de serviços de transporte quando ocorre triangulação\. 

__MFS93637__

Andréa Rocha

Inclusão do parâmetro 93 para ser utilizado na geração do resumo da apuração do ICMS\.

__MFS534631__

Liliane Assaf

Inclusão do parâmetro 94 para atendimento ao ICMS Monofásico sobre Combustíveis\.

__MFS520581__

Andréa Rocha

Inclusão do parâmetro 95 para ser utilizado na geração do resumo da apuração do ICMS, para atendimento à nota técnica 002/2010 do Rio Grande do Norte\.

__MFS628422__

Andréa Rocha

Inclusão do parâmetro 96 para ser utilizado na geração do resumo da apuração do ICMS, para atendimento à Instrução Normativa n° 03/2024, do Ceará\.  Esse parâmetro não vai ficar vinculado ao estado do Ceará, poderá ser usado por qualquer estado, que faça a transferência de saldo credor de ICMS para compensar saldo devedor de outro estabelecimento\.

__MFS768225__

Andréa Rocha

Inclusão do parâmetro 97 para ser utilizado para Tax Data Manager \(TDM\), para gravar as informações por nota fiscal na Apuração do ICMS, que serão utilizadas posteriormente no Tax Data Manager \(TDM\)\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Inclusão de um ox com o título “Parâmetros p/ Livros de Saídas ” no Parâmetros por UF\.

__OS2609\-D__

__RN01__

Inclusão de um campo no ox “Parâmetros p/ Mapa Resumo /  Livros de Saídas”:

🡺 item 83 – “Considerar  Itens de Crédito” \( Mapa Resumo/Livros de Saídas \),  campo tipo check ox, alfanumérico, tamanho 01\.

A funcionalidade deste label é o mesmo que utilizado na Tela de Geração do Mapa Resumo\.

Como default, o campo deverá estar desmarcado\.

__OS2609\-D__

__RN02__

A partir desta OS, o label “Considerar Itens de Crédito”  deverá ser realocado da tela de Geração de Mapas Resumo para Parâmetros por UF no item 83 com a mesma funcionalidade\.

__OS2609\-D__

__RN03__

O item 83 dos Parâmetros por UF deverá ser checado quando na Geração dos Mapas Resumo e emissão dos livros de Saídas\.

__OS2609\-D__

__RN04__

Incluir no item 51 – “Emissão do Livro de Entradas \(P1/P1A\) conforme Port\. CAT44 – SP”

__OS2609\-A__

__RN05__

Para os livros fiscais de Entradas Normais e Livros Fiscais de Entradas  para empresas com Inscrição Estadual única:

🡺 Em Parâmetros por UF, quando o item 77\( Modelo de Livro P1/P1A\)   estiver desmarcado, para documentos fiscais mistas \( mercadorias e serviços \), tabela SAFX07, item 12 COD\_CLASS\_DOC\_FIS= 3, deverá ser exibida um único Valor Contábil  de forma sumarizada na parte principal dos livros fiscais, contabilizando o valor contábil do item de  mercadoria com o  valor contábil do item de serviço\.

A coluna do CFOP, base de Cálculo, Alíquota, Imposto Debitado/não\-tributadas e Outras continuam sendo exibidas por item em linhas diferentes\.

Caso item 12 da tabela SAFX07, COD\_CLASS\_DOC\_FIS <> 3, os livros não sofrerão alterações\.

__CH53090__

__RN06__

Para os livros fiscais de Saídas normais, como também Livros Fiscais de Saídas para empresas com Inscrição Estadual única:

🡺 Em Parâmetros por UF, quando o item 78\( Modelo de Livro P2/P2A\)   estiver desmarcado, para documentos fiscais mistas \( mercadorias e serviços \), tabela SAFX07, item 12 COD\_CLASS\_DOC\_FIS= 3, deverá ser exibida um único Valor Contábil  de forma sumarizada na parte principal dos livros fiscais, contabilizando o valor contábil do item de  mercadoria com o  valor contábil do item de serviço\.

A coluna do CFOP, base de Cálculo, Alíquota, Imposto Debitado/não\-tributadas e Outras continuam sendo exibidas por item em linhas diferentes\.

Caso item 12, da tabela SAFX07,  COD\_CLASS\_DOC\_FIS <> 3, os livros não sofrerão alterações\.

__CH53090__

__RN07__

Para os livros fiscais de Entradas e Saídas normais

🡺 Em Parâmetros por UF, quando os itens 23 \(Lançar ICMS\-S com crédito nas Observações \(P1/P1A\) e 25 \(Lançar ICMS\-S com crédito nas Observações \(P2/P2A\)\) estiverem marcados, deve\-se para documentos fiscais com itens de mercadorias e ICMS\-S tributado, gerar uma observação contendo o Valor do Imposto e a sua respectiva Base de Cálculo\.

__OS 2715__

__RN08__

Regra p/ Inclusão do novo parâmetro “86 – Observação de IPI não escriturado”

Incluir na tela ICMS – Manutenção – Parâmetros p/UF, o novo parâmetro “86 – Observação de IPI não Escriturado“\. Esse campo deve ser um checkbox onde deve gravar “S” – quando o campo estiver marcado e “N” – quando o campo estiver desmarcado\. Por default, esse campo deve ser exibido desmarcado\.

__OS3008__

__RN09__

__Regra para o parâmetro “87 \- Considerar Observações de Informações Complementares da Nota \(SAFX112\) para livros \(P1 e P2\)”\.__

- Se selecionado deve emitir a mensagem abaixo:

“Por Default o Mastersaf gera sempre as observações informadas nos itens de Documento Fiscal\. 

Escolhendo esta opção, você estará desabilitando os parâmetros 29 e 81 e considerando apenas as observações informadas em “Informações complementares” do documento fiscal \(SAFX112\)\. 

Deseja continuar?”

\*SIM      \*CANCELAR\.

Escolhendo a opção SIM, o sistema habilita o parâmetro 87 e desabilita os parâmetros 29 e 81\. 

Escolhendo a opção CANCELAR, a ação deve ser desconsiderada\.

- Quando o parâmetro for “Desabilitado” então deve ser emitida a seguinte mensagem para o usuário:

“Por Default o Mastersaf gera sempre as observações informadas nos itens de Documento Fiscal\. Desmarcando esta opção, você estará habilitando o parâmetro 29 e considerando a parametrização Default do Sistema\.

Deseja continuar?”

\*SIM    \*CANCELAR

Escolhendo a opção SIM, o sistema habilita o parâmetro 29 e desabilita o parâmetro 87\.

Escolhendo a opção CANCELAR, a ação deve ser desconsiderada\.

Se o parâmetro 87 estiver selecionado e o tipo da observação for informação complementar da nota, ou seja, campo 13 da SAFX112 = “I”, gerar no resumo “OBSERVAÇÔES” dos livros \(P1 e P2\) as observações cadastradas nos campos abaixo:

1. Campo 03 \(DESCRICAO\) da SAFX2009 correspondente ao código cadastrado no campo 12 \(COD\_OBS\_LANCTO\_FISCAL\) da SAFX112\.
2. Campo 14 \(DSC\_COMPLEMENTAR\) da SAFX112\.

Quando houver informação complementar na SAFX112 então devem ser apresentadas as duas observações apenas com a separação de um traço \(Item 1 e 2\)\.

__OS3384__

__RN10__

__Parâmetro 29__

Alterar a mensagem que é apresentada quando o parâmetro 29 é habilitado, conforme destacado em verde:

__Mensagem atual:__ O Parâmetro 81 será desabilitado\. Deseja continuar?

__Alterar a mensagem para: __Os Parâmetros 81 e 87 serão desabilitados\. Deseja continuar?

Escolhendo a opção SIM, o sistema habilita o parâmetro 29 e desabilita os parâmetros 81 e 87\.

Escolhendo a opção CANCELAR, a ação deve ser desconsiderada\.

__OS3384__

__RN11__

__Parâmetro 81__

Alterar a mensagem que é apresentada quando o parâmetro 81 é habilitado, conforme destacado em verde:

__Mensagem atual:__ “Por Default o Mastersaf gera sempre as observações informadas nos itens de Documento Fiscal\. Escolhendo esta opção, você estará desabilitando o parâmetro 29 e considerando apenas as observações informadas na capa do Documento Fiscal\.

Deseja continuar?”

__Alterar a mensagem para: __“Por Default o Mastersaf gera sempre as observações informadas nos itens de Documento Fiscal\. Escolhendo esta opção, você estará desabilitando os parâmetros 29 e 87 e considerando apenas as observações informadas na capa do Documento Fiscal\.

Deseja continuar?”

Escolhendo a opção SIM, o sistema habilita o parâmetro 81 e desabilita os parâmetros 29 e 87\.

Escolhendo a opção CANCELAR, a ação deve ser desconsiderada\.

__OS3384__

__RN12__

__Regra para parâmetro 84 \- Escritura NF’s EE \(Modelo 06\) pela Data de Vencimento:__

Este parâmetro foi criado para atender às empresas de Energia Elétrica, que devem escriturar as notas fiscais de serviço de energia elétrica \(modelo 06\) pela data de vencimento, ao invés de escrituração pela data de emissão do documento, e para a UF SP\. Esse parâmetro foi criado pela OS2768\-F\.

Quando o campo 13 \- COD\_MODELO \(SAFX42\) = ‘6’, UF Estabelecimento = SP, UF Destinatário = SP, verificar:

SE campo 03 \- DAT\_FISCAL \(SAFX42\) tiver data até 31\.12\.2011 e o campo 32 \- DAT\_VENCTO \(SAFX 42\) tiver data a partir de 01\.02\.2012, a escrituração deve ser pela data de vencimento, ou seja, pelo campo 32 da SAFX42\.

SE campo 03 \- DAT\_FISCAL \(SAFX42\) tiver data a partir de 01\.01\.2012, a escrituração deve ser pelo campo 11 \(SAFX42\)\.

__Obs\.:__ A UF Destinatário deve ser qualquer em virtude de negócios, pois o estabelecimento é situado em SP, porém comercializa energia elétrica para outra UF, como por exemplo, as cidades que se localizam em divisas entre estados\.

__OS3424\-A__

__RN13__

__Parâmetro “*GI/ICMS c/detalhamento dos Bens de Uso/Consumo e Ativo Imobilizado”:*__

*Parâmetro criado na OS3527, utilizado na geração e emissão da GI/ICMS do Módulo ICMS\.*

*Para consultar as regras de utilização deste parâmetro, verificar os documentos de regras referentes a geração e emissão da GI/ICMS: “*MTZ \- ICMS – Geração da GI/ICMS” *e  “*MTZ \- ICMS – Emissão da GI/ICMS”\.

__OS3527__

__RN14__

Parâmetro __Exibir CFOP’s zerados no Livro de Apuração do ICMS \(P9\)__:

Parâmetro criado pela OS3659 para utilização na geração do Livro de Apuração do ICMS:

Com a criação deste parâmetro os resumos das entradas e saídas totalizadas por CFOP no Livro P9 passarão a exibir também os CFOP’s com todos os valores zerados, da seguinte forma:

- Se parâmetro desmarcado 🡪 neste caso os CFOP’s zerados *não* serão exibidos nos resumos
- Se parâmetro marcado 🡪 neste caso os CFOP’s zerados serão exibidos nos resumos

\(ver detalhes no documento de regras da geração do livro P9\)

OS3659

__RN15__

Parâmetro __43\-Observação p/Faturamento Direto ao Consumidor \(P2/P2A\):__

__Alteração da OS3046:__

Alterada a forma de funcionamento deste parâmetro, que passou a utilizar dois formatos de observação distintos\. Para escolher o formato desejado, foram criadas as seguintes opções relacionadas ao parâmetro 43:

Opção \[__Demonstrar apenas “Faturamento Direto ao Consumidor”__\] 🡪 Neste caso será impresso apenas o conteúdo “Faturamento Direto ao Consumidor”\.

Opção \[__Demonstrar também os valores do ICMS referente às outras UF’s__\] 🡪 Neste caso, além deste conteúdo, será demonstrado também o valor da base de cálculo e do ICMS referente à UF de destino \(campos 106 e 107 da SAFX07\)\.

O default será a primeira opção, seguindo o funcionamento original\.

 

Estas duas opções serão habilitadas para seleção do usuário apenas quando o parâmetro \[43\] for selecionado\. Caso contrário, deverão ficar desablitadas\. 

 \(ver detalhes da utilização do parâmetro no documento de regras da geração do livro P2\)

__OS3046__

__RN16__

Parâmetro __91\-Apuração ICMS Dif Alíquota UF Orig/Dest \- EC 87/15 \(P9\)__:

Parâmetro criado pela MFS2131 para utilização na geração do Livro de Apuração do ICMS\.

O objetivo deste parâmetro é permitir ao usuário que o processo de geração da “Apuração do ICMS Dif Aliq UF Orig/Dest” \(criada pelo Ato Cotepe 44/2015\) seja executado durante a geração da Apuração do ICMS \(P9\)\. Ver detalhes nos documentos de regras do P9\.

__MFS2131__

__RN17__

__Parâmetro 92 – Cálculo do Diferencial de Alíquota c/ base na IN RE Nº 39/2016 para RS\.__

Parâmetro criado pela MFS6817 para utilização no cálculo do diferencial de alíquota efetuado na Apuração do ICMS para RS\.

Esse parâmetro ficará habilitado apenas para UF = ‘RS’\.

O objetivo deste parâmetro é permitir ao usuário que o processo de cálculo do diferencial de alíquota seja alterado de acordo com a Instrução Normativa RE Nº 39/2016 durante a geração da Apuração do ICMS \(P9\)\. Ver detalhes nos documentos de regras no MTZ\_Calculo\_Diferencial\_Aliquota\_Lançamento\_Automatico\_RS\.doc\.

Alteração __MFS11722__:

__92 – Cálculo do Diferencial de Alíquota c/base nas Regras Específicas das UF’s__

Este parâmetro foi renomeado com objetivo de atender a todas as UF’s, e passou a apresentar duas opções do valor a ser utilizado nos cálculos, ficando da seguinte forma: 

![](data:image/png;base64,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)

O parâmetro passou a ficar habilitado para todas as UF’s\. 

As opções de valor são alternativas, e só ficarão habilitadas quando o parâmetro estiver marcado\.

Sempre que o parâmetro *for marcado*, a opção de valor default será marcada automaticamente \(default = “Valor Contábil do Item”\)\.

Sempre que o parâmetro *for desmarcado*, a opção de valor selecionada será limpa, e ficarão as duas desmarcadas\.

A opção de valor escolhida é gravada na coluna IND\_TP\_PAR com o conteúdo: “1” para “Valor Contábil do Item”, e “2” para “Valor parametrizado \(Módulo Ferramentas\)”\.

__MFS6817__

__MFS11722__

__RN18__

__Parâmetro 32 \- Descrição para cabeçalho dos Livros Fiscais:__

Este parâmetro deve ser utilizado na emissão dos livros fiscais e tem duas opções:

__Folha:__ caso o usuário selecione está, no livro deverá aparecer Folha e os números das folhas\.

__Página:__ caso o usuário selecione está, no livro deverá aparecer Página e os números das páginas\.

Este parâmetro deve atender todos os livros fiscais: P1, P1A, P2, P2A, P7, P9, inclusive os livros gerados por Inscrição Estadual Única\.

__CH21822\-A\_2012__

__RN19__

__Parâmetro 90 – Demonstrar Operações por Indicador de Produto e Situação Tributária__

Este parâmetro será utilizado na emissão dos Livros P7 que têm como origem para geração a tabela SAFX52 \(Convênio 57/95 \- Layout Oficial, Produto e Decreto 43\.080/02 – MG\)\. Quando selecionado, possibilitará a emissão do livro quebrando por Indicador de Produto e Situação Tributária\.

__OS3972__

__RN20__

__Parâmetro 67 – Lançar Campo UF Origem/Destino do Documento Fiscal nos Livros Fiscais \(Movimentos/Resumo por UF\)__

Este parâmetro define a busca da informação a ser lançada na coluna "UF" do Livro Registro de Entradas \(P1/P1A\) e Livro Registro de Saídas \(P2/P2A\) e Convênio ICMS 51/00, bem como para o Resumo por UF destes livros\. Caso não seja selecionado, será considerada a UF constante no Cadastro de Pessoas Físicas/Jurídicas do Fornecedor ou do Cliente do Documento Fiscal\. Caso seja selecionado, o sistema buscará a UF informada no campo "UF Origem" ou "UF Destino" dos Documentos Fiscais \(capa\)\. 

__Exemplo:__ 

- Operações interestaduais entre Contribuintes da mesma UF \- Este parâmetro atende as UFs que interpretam que para o lançamento fiscal dos Contribuintes de Transporte deve\-se considerar a UF do Remetente ou o Destinatário do Documento Fiscal\. Para as UFs que interpretam que se deve considerar o Emitente do Conhecimento de Transporte, o sistema pode gerar a UF através do Cadastro do Fornecedor ou Cliente\.
- Caso o documento fiscal possua no campo Classificação Fiscal diferente de “4 – Conhecimento de Transporte” o sistema irá verificar se a UF de Origem e UF de Destino estão preenchidas\. Caso positivo essa UF de Origem será informada para o documento fiscal no Livro de Registro de Entradas e a UF de Destino para o Livro de Registro de Saídas\. Caso negativo será considerado a UF da Pessoa Física/Jurídica do documento fiscal\. Caso nenhuma das duas informações esteja preenchida, o sistema irá exibir uma mensagem na geração do livro informando que essas informações não estão preenchidas\.

__MFS\-14393:__ Inclui tratamento específico para operações de aquisição de serviços de transporte com triangulação \(__*Exemplo:*__ Serviço de transporte tomado na mesma UF do estabelecimento, em que a origem do serviço será na mesma UF do estabelecimento, mas seu destino será numa UF diferente da UF do estabelecimento\. Envolvendo, nesse caso, o expedidor e o recebedor estabelecido na mesma UF, tomando serviço de uma empresa também da mesma UF, mas remetendo para uma UF diferente sendo do mesmo grupo da empresa expedidora e recebedora\)\.

Esse tratamento também é utilizado na apuração do diferencial de alíquota, tanto a apuração do DIFAL feita no livro P9, como os 4 relatórios do DIFAL do Report Fiscal foram atualizados para usar o parâmetro 67, então serão recuperadas apenas as notas em que e UF da pessoa fis/jur *ou a UF Origem da nota, dependendo do conteúdo do parâmetro 67* for diferente da UF do Estabelecimento, exceto em casos de triangulação do serviço de conhecimento de transporte\.

A comparação das UF’s a serem utilizadas será feita da seguinte forma:

__Se__ parâmetro 67 marcado

      Neste caso, a comparação entre as UFs é feita utilizando a UF Origem informada no documento fiscal \(campo 117 da SAFX07\), *mas* apenas nos casos em que ela estiver preenchida, ou seja:

        __Se__ UF Origem da SAFX07 preenchida:

             \[UF Origem da SAFX07 <> UF do cadastro do Estabelecimento\] __OU__

             \[CFOP da SAFX08 OU SAFX07 \(se não houver item\) iniciada com “235” E UF Origem da SAFX07 = UF do cadastro do Estabelecimento E UF Destino da SAFX07 <> UF do cadastro do Estabelecimento\]

        __Senão__

             \[UF do cadastro da SAFX04 <> UF do cadastro do Estabelecimento\] 

__Senão__

       Neste caso, a comparação das UFs é feita sempre a partir da UF da pessoa fis/jur:

                \[UF do cadastro da SAFX04 <> UF do cadastro do Estabelecimento\]

__CH14249\_2017 \(MFS\-14393\)__

__RN21__

__Parâmetro 93 – Considerar Lançamentos Complementares vinculados à Subapuração no livro de Apuração ICMS \(P9\)__

Este parâmetro será utilizado na emissão do Livro de Apuração do ICMS \(P9\), na parte do Resumo da Apuração para demonstrar os lançamentos complementares que estão vinculados a uma Subapuração\.

Quando selecionado, os lançamentos complementares que estão vinculados a uma Subapuração, serão demonstrados na parte do Resumo da Apuração\.

__MFS93637__

__RN22__

__Parâmetro 94 – Escritura o ICMS Monofásico sobre combustível junto ao ICMS/ICMS\-ST \(P9/P9\-ST\)__

Esse parâmetro será utilizado na geração da Apuração do ICMS e do ICMS\-ST \(P9 e P9\-ST\), para sumarizar o ICMS Monofásico das notas de saídas de Combustíveis carregados através da SAFX325, ao valor total das saídas, da seguinte forma:

\- Para os CST = 02, 15, totalizar o Valor do ICMS Próprio Devido \(item 23 da SAFX325 \- VLR\_ICMS\_MONO\) \+ Valor do ICMS com retenção \(item 26 da SAFX325 \- VLR\_ICMS\_MONO\_RETEN\) no item 001 do Resumo da Apuração do ICMS\-ST\.

\- Para o CST = 53 do B100 \(Biodiesel\), totalizar o Valor do ICMS Próprio Devido \(item 23 da SAFX325 \- VLR\_ICMS\_MONO\) no item 001 do Resumo da Apuração do ICMS\.

__MFS534631__

__RN23__

__Parâmetro 95 – Tratamento da Nota Técnica 002/2010 \- RN \(P9\)__

Esse parâmetro será utilizado na geração da Apuração do ICMS\(P9\), para atendimento à nota técnica 002/2010 do Rio Grande do Norte\.  Para as notas fiscais de transferência de crédito/débito, será feito um tratamento nos itens 001 e 005 na geração do resumo da apuração, que irá impactar na geração dos itens 02\-VL\_TOT\_DEBITOS e 06\-VL\_TOT\_CREDITOS do registro E110 do SPED\-EFD\. 

__MFS520581__

__RN24__

__Parâmetro 96 – Tratamento da Transferência de Crédito \- Compensação \(P9\)__

Esse parâmetro será utilizado na geração da Apuração do ICMS \(P9\), para atendimento à Instrução Normativa n° 03/2024, do Ceará\.  Esse parâmetro não vai ficar vinculado ao estado do Ceará, poderá ser usado por qualquer estado, que faça a transferência de saldo credor de ICMS para compensar saldo devedor de outro estabelecimento\. Para as notas fiscais de transferência de crédito, será feito um tratamento nos itens 001 e 005 na geração do resumo da apuração, que irá impactar na geração dos itens 02\-VL\_TOT\_DEBITOS e 06\-VL\_TOT\_CREDITOS do registro E110 do SPED\-EFD\. 

__MFS628422__

__RN25__

__Parâmetro 97 – Disponibilizar Notas Fiscais da Apuração do ICMS p/ Tax Data Manager \(TDM\) \(P9\)__

Esse parâmetro será utilizado na geração da Apuração do ICMS \(P9\), para gravar as informações por nota fiscal na Apuração do ICMS, que serão utilizadas posteriormente no Tax Data Manager\.  A geração da apuração gera os valores para o livro já somados, não grava a informação por nota fiscal\.  Esse parâmetro está sendo criado para não deixar a geração mais lenta, para os clientes que não vão usar o TDM\.

__MFS768225__

__Considerações deste modelo:__

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

