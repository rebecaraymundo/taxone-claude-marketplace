# MTZ-Job-Servidor-Importacao_SAFX42

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX42.docx
- **Modificado:** 2026-02-22
- **Tamanho:** 73 KB

---

__         __

# Módulo Job Servidor – Importação SAFX42 \(Documento Fiscal Utilities\)

                      Localização: Menu Básicos, Módulo: Job Servidor, item Importação à Execução

*Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX42, conforme o Manual de Layout,  o que facilita a consulta\. Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00\.*

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS 3132

DW \- ESTADUAL \- SEF\-PE \- Atendimento a TELECOM \- Revisão da OS2867

Revisão geral da geração dos registros 76 e 77 para o SEF\-PE

OS3295

Atendimento a Portaria CAT 187/2010

Alterações do Mastersaf p/ atendimento a Portaria CAT 187/2010  \(esta OS criou os campos 88 ao 96\)

OS2890

Criação de campos para atendimento do Ato Cotepe 24/2010

Criação de campos referente as notas de fiscais modelo 21 e 22 de  Ressarcimento ao Cliente\.

OS3065\-dw

Novos campos p/ atendimento ao SEF II\-PE

Novos campos p/ atendimento ao SEF II\-PE

OS3065\-A

Geração do arquivo LA\-ICMS do SEFII

Geração do arquivo LA\-ICMS do SEFII \(parte 1\)

OS3424

Criação de campos para atendimento Portaria CAT Nº 115/11, que altera a Portaria CAT Nº 187/10

Criação de campos para atendimento Portaria CAT Nº 115/11, que altera a Portaria CAT Nº 187/10

OS3135

Alteração no campo 14 \(Tipo de Receita\)

Novo código de Tipo de Receita

OS3564

Novo código de modelo – 58\.

Novo código de modelo de Documento Fiscal \- Manifesto Eletrônico de Documentos Fiscais \- MDF\-e\.

OS3557

Crítica no campo de classe de consumo

Crítica no campo de classe de consumo para atendimento do SPED FISCAL

OS3743

Inclusão de campos

Identificador do  Documento Fiscal de Utilities e Código do Sistema de Origem

OS3931

Tratamento na Importação da SAFX42

Incluir um tratamento para recuperar o IDENT correto do cadastro da Pessoa Fis/Jur, na atualização dos dados da SAFX42/SAFX43\.

OS4214

Inclusão de campo

Inclusão de campo p/atendimento ao Módulo Arquivo de Injeção de Energia Elétrica

OS4316

Criação de Campos

Criação dos campos Código e Descrição da SCP

OS4579

Alteração no tamanho do campo 

Alteração no tamanho do campo NUM\_LANCTO\_CONTABIL para 40 posições\.

MFS\-1079

Criação e ajuste de campos

Criação e atualização do conteúdo padrão de campos para atender ao Convênio ICMS 60/2015\.

MFS\-7160

Inclusão de campos

Este documento tem como objetivo incluir os campos “Chave de Acesso \(CV115\-e\)” e “Data Autorização de Emissão \(CV115\-e\)”, em atendimento ao Convênio ICMS 94/2016\.

CH23207\_2017

MFS15833

Inclusão de opção válida para o campo 121 \- COD\_MODELO\_SUBST

Esse documento tem como objetivo incluir o modelo de documento “01” no campo 121 \- Modelo do Documento Fiscal Substituído/Complementado\.

__MFS31251__

Criação de campos

Criação dos campos “Finalidade Emissão do Documento” e “Chave de Acesso da NFe Substituída”, p/geração dos novos campos do registro C500 do Sped Fiscal \(novo layout vrs\. 1\.13, vigência Jan/2020\)\. 

MFS\-34503

Modelo de Documento

__RN13: __Passar a considerar os modelos 28 e 29, no campo 13 \- Modelo de Documento

MFS62273

Andréa Rocha

Inclusão do modelo 66 para o campo 78 \- Código Modelo NF

MFS74305

Liliane V\. Assaf

Sped Fiscal Atualização 2022 :

__RN121__ Passar a considerar o modelo 66 no campo 121 – COD\_MODELO\_SUBST,

__RN128__: Inclusão do campo Código de Autenticação Digital \(Convênio 115/2003\)

__RN129__: Inclusão do campo Outras Deduções

MFS432820

Liliane V\. Assaf

Tratamento do modelo 62 – NFCom:

__RN13, RN78, RN121, RN126:__ Passar a considerar o modelo 62

__RN128__: Passar a considerar os modelos 21 e 22

__RN130__: Inclusão do campo Tipo Faturamento \(NFe\)

MFS591907

Graciela Soares

Criação de Novos Campos – Tabela SAFX42

MFS\-851680

Alessandra Cristina Navatta

Aumento do campo 54 \- Canal de Distribuição/ Código da Obra \(RN54\)

MFS891513

Andréa Rocha

Alteração da regra de preenchimento do campo 139 \- Motivo da substituição, para corrigir o valor aceito, conforme informado no manual layout\.

MFS981990

Liliane Assaf

Novos campos \(itens 169 a 171\) para atendimento ao Ato Cotepe ICMS 52/15\.

#### Cód\.

### DR

__RN00__

__Regras gerais__

*\(espaço reservado para regras genéricas, que não dizem respeito a campos específicos\)*

__RN02__

__Campo Código da SCP__

Alterar a rotina de importação para que seja considerado o novo campo:

Tabela: SAFX42

Item: A ser reservado pelo A&D

Nome do Campo: Código da SCP

Tipo: A

Tamanho: 014

Comentário: Código da Sociedade em Conta de Participação

Deverá existir um cadastro correspondente na SAFX2057 para o código informado\. Caso não exista, retornar a mensagem: “Cadastro da SCP não encontrado”\.

__OS4316__

__RN03__

__Campo Descrição da SCP__

Alterar a rotina de importação para que seja considerado o novo campo:

Tabela: SAFX42

Item: A ser reservado pelo A&D

Nome do Campo: Descrição da SCP

Tipo: A

Tamanho: 100

Comentário: Descrição da Sociedade em Conta de Participação 

__OS4316__

__RN13__

__Campo 13 – Modelo de Documento__

Tabela de Origem: SAFX2024

Códigos de Modelos aceitos são: 01, 06, 21, 22, 28, 29, 62 e 66\.

Se o código informado não foi um dos acima mencionados, exibir a seguinte mensagem e não importar o registro:

*“91068 \- Modelo invalido para este tipo de documento \(codigo validos: 01, 06, 21, 22, 28, 29, 62 ou 66\)”*

O modelo 66 \(NF3e\-Nota Fiscal de Energia Elétrica Eletrônica\) passou a ser tratado na SAFX42 na __MFS31252__, para atender a nova versão 1\.13 do Sped Fiscal \(vigência 01/01/2020\)\.

__MFS31252__

MFS\-34503

MFS432820

__RN54__

__Campo Código da Obra__

A rotina de Importação do módulo JOB Servidor deve ser ajustada para que contemple a alteração de aumento do campo COD\_CANAL\_DISTRIB da tabela SAFX42\-Capa de Documentos Fiscais de Utilities\. 

__![](data:image/png;base64,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)__

__Item__: 54

__Nome__: COD\_CANAL\_DISTRIB

__Descrição__: Canal de Distribuição/ Código da Obra

__Tamanho__: 15

__Tipo__: A

__Obrigatoriedade__: N

MFS\-851680

__RN78__

__Campo 78 – Código Modelo NF__

__\[MFS62273\] __Inclusão do modelo 66

__ __

Campo não obrigatório\. 

Quando este campo estiver preenchido, será verificado se o código é um destes códigos abaixo:

'01','1B','02','2D','2E','3A','3B','03','04','06','07','08','8B','09','10','11','13','14','15','16','17','18','20','21','22','23','24','25','26','27','28','29','30','58', 62 e ‘66’

Se o código informado não foi um dos acima mencionados, exibir a seguinte mensagem e não importar o registro:

*“91604\- Nao existe relacao do Codigo do Modelo da NF\(Cotepe\) informado com a tabela do ATO COTEPE 70/05 \- 4\.1\.1”*

__MFS62273__

MFS432820

__RN87__

__Campo 87 – Código da Classe de Consumo para o SEF\-PE__

O campo de código da classe de consumo não será obrigatório\.

Caso o código informado não esteja contido na lista de valores previstos para o SEF\-PE, apresentar a mensagem no log:

Crítica: Código da classe de consumo inválido para o SEF\-PE\.

Solução: Consulte o manual de orientação do SEF\-PE para verificar a lista dos códigos permitidos\.

Alteração da OS3065\-A: Alterada a regra de validação do campo, para atender as duas versões do SEF \(SEF e SEF II\):

__Validação atual__ \(antes da OS3065\-A\) è o código informado é validado na Tabela de Classes de Consumo, buscando pelos critérios:  modelo = modelo da nota  e  indicador = “2”

*\(o indicador serve para identificar a qual obrigação se refere os códigos da tabela, e 2 indica SEF\-PE\)*

__Nova validação__ \(a partir da OS3065\-A\) è devido à nova versão do SEF, \(SEF II\), foi incluída uma nova lista de códigos nesta tabela, que receberam o indicador = “3”, indicando tratar\-se da obrigação SEF II\.

Com isso, a validação passou a ser feita a partir de uma data parametrizada no Módulo SEF II, da seguinte forma:

Parâmetros que serão utilizados na validação:

 

- Parâmetro “*Mês/Ano inicial da entrega do SEF II*” \(Módulo SEF II – PE, menu “Dados Iniciais”\)
- Data fiscal do documento

Validação:

__Se__ mês/ano do parâmetro não existente __ou__ nulo:

      Valida se o código da classe de consumo existe na tabela nas seguintes condições: 

- Modelo = modelo do documento \(campo “13\-Modelo do Documento”\);
- Indicador de Uso  = __“2”__ \(indicando que a obrigação é o  __SEF\-PE__\);

__Senão__

      __Se__ o mês/ano da data fiscal do documento for igual ou superior ao mês/ano do parâmetro 

            Valida se o código da classe de consumo existe na tabela nas seguintes condições: 

- Modelo = modelo do documento \(campo “13\-Modelo do Documento”\);
- Indicador de Uso  = __“3”__ \(indicando que a obrigação é o  __SEF II\-PE__\);

      __Senão __

            Valida se o código da classe de consumo existe na tabela nas seguintes condições: 

- Modelo = modelo do documento \(campo “13\-Modelo do Documento”\);
- Indicador de Uso  = __“2”__ \(indicando que a obrigação é o  __SEF\-PE__\);

Quando o código informado não for encontrado na tabela nas condições estabelecidas, será gravada a seguinte mensagem no log, e o registro não será importado: “Código da classe de consumo inexistente ou inválido para a data da nota fiscal”\.

Obs: Para obter o parâmetro da data do SEF II, será feita a pesquisa pela parametrização do Estabelecimento\. Caso não exista, será verificada a parametrização a partir do Estabelecimento Centralizador, caso o estabelecimento em questão conste como componente de alguma centralização \(centralização dos estabelecimentos por inscrição estadual única que consta no módulo de controle das obrigações estaduais\)\.

__OS3132__

__OS3065\-A__

__RN88__

__Campo 88 – Autor da Ação Judicial: __

Campo não obrigatório criado pela OS3295\. 

__OS3295__

__RN89__

__Campo 89 – Número do Processo da Ação Judicial:__

Campo não obrigatório criado pela OS3295\. 

__OS3295__

__RN90__

__Campo 90 – Número da Vara da Ação Judicial:__

Campo não obrigatório criado pela OS3295\. 

__OS3295__

__RN91__

__Campo 91 – Data da Ação Judicial:__

Campo não obrigatório criado pela OS3295\. 

__OS3295__

__RN92__

__Campo 92 – Valor do Depósito Judicial:__

Campo não obrigatório criado pela OS3295\. 

__OS3295__

__RN93__

__Campo 93 – Data do Depósito Judicial:__

Campo não obrigatório criado pela OS3295\. 

__OS3295__

__RN94__

__Campo 94 – Número do Banco do Depósito Judicial__:

Campo não obrigatório criado pela OS3295\. 

Quando este campo estiver preenchido, será verificado se o código informado existe na tabela de cadastro dos Bancos \(Módulo DW, item Manutenção à Cadastros à Bancos\)\. Caso não, será gravada a mensagem de erro no log, e o registro não será importado:

          *“O número do Banco do depósito judicial não existe na Tabela de Cadastro dos Bancos \(Módulo DW\)”*

### OS3295

__RN95__

__Campo 95 – Número da Agência do Depósito Judicial:__

Campo não obrigatório criado pela OS3295\. 

__OS3295__

__RN96__

__Campo 96 – Número da Conta do Depósito Judicial__:

Campo não obrigatório criado pela OS3295\. 

__OS3295__

__RN97__

__Campo 97 \(Sugerido\):__ Número da NF com ressarcimento ao cliente

__Item__: 97 \(Sugerido\)

__Descrição do campo__: Número da NF com ressarcimento ao cliente

__Nome do campo__: A ser definido pelo A&D

__Comentário__: Número da Nota Fiscal com ressarcimento ao cliente\. Essa informação deve ser preenchida nos casos de Documentos Fiscais de Utilities cujo modelo seja 21 – Comunicação ou 22 – Telecomunicação para geração dos arquivos digitais do módulo Estorno de Débitos – Modelos 21/22 nos layouts “Ato COTEPE 24/2010” e “Portaria CAT 06/2009”\.

__Tamanho__: 012

__Tipo__: N

__OS2890__

__RN98__

__Campo 98 \(Sugerido\):__ Série da NF com ressarcimento ao cliente

__Item__: 98 \(Sugerido\)

__Descrição do campo__: Série da NF com ressarcimento ao cliente

__Nome do campo__: A ser definido pelo A&D

__Comentário__: Série da Nota Fiscal com ressarcimento ao cliente\.\. Essa informação deve ser preenchida nos casos de Documentos Fiscais de Utilities cujo modelo seja 21 – Comunicação ou 22 – Telecomunicação para geração dos arquivos digitais do módulo Estorno de Débitos – Modelos 21/22 nos layouts “Ato COTEPE 24/2010” e “Portaria CAT 06/2009”\.

__Tamanho__: 003

__Tipo__: A

__OS2890__

__RN99__

__Campo 99 \(Sugerido\):__ Modelo da NF com ressarcimento ao cliente

__Item__: 99 \(Sugerido\)

__Descrição do campo__: Modelo da NF com ressarcimento ao cliente

__Nome do campo__: A ser definido pelo A&D

__Comentário__: Modelo da Nota Fiscal com ressarcimento ao cliente\. O Código deve estar registrado na Tabela de Modelos de Documentos Fiscais \(__SAFX2024__\)\.

Essa informação deve ser preenchida nos casos de Documentos Fiscais de Utilities cujo modelo seja 21 – Comunicação ou 22 – Telecomunicação para geração dos arquivos digitais do módulo Estorno de Débitos – Modelos 21/22 nos layouts “Ato COTEPE 24/2010” e “Portaria CAT 06/2009”\.

__Tamanho__: 002

__Tipo__: N

__OS2890__

__RN100__

__Campo 100 \(Sugerido\):__ Data de Emissão da NF com ressarcimento ao cliente

__Item__: 100 \(Sugerido\)

__Descrição do campo__: Data de Emissão da NF com ressarcimento ao cliente

__Nome do campo__: A ser definido pelo A&D

__Comentário__: Data de Emissão da Nota Fiscal com ressarcimento ao cliente\. Essa informação deve ser preenchida nos casos de Documentos Fiscais de Utilities cujo modelo seja 21 – Comunicação ou 22 – Telecomunicação para geração dos arquivos digitais do módulo Estorno de Débitos – Modelos 21/22 nos layouts “Ato COTEPE 24/2010” e “Portaria CAT 06/2009”\.

__Tamanho__: 008

__Tipo__: D

__OS2890__

### RN101

__Campo Número do Lançamento Contábil:__

Campo *não* obrigatório e sem críticas\.

__OS3065\-dw__

__RN102__

__Campo 102 \(campo reservado\): JUROS DE MORA__

__Item__: 102 \(Reservado\)

__Descrição do campo__: Juros de Mora

__Nome do campo__: A ser definido pelo A&D

__Comentário__: Valor referente a Juros de Mora

__Tamanho__: 015V002

__Tipo__: N

__OS3424__

__RN103__

__Campo 103 \(campo reservado\): MULTA DE MORA__

__Item__: 103 \(Reservado\)

__Descrição do campo__: Multa de Mora

__Nome do campo__: A ser definido pelo A&D

__Comentário__: Valor referente a Multa de Mora

__Tamanho__: 015V002

__Tipo__: N

__OS3424__

__RN104__

__Campo 104 \(campo reservado\): ACRÉSCIMOS LEGAIS__

__Item__: 104 \(Reservado\)

__Descrição do campo__: Acréscimos Legais

__Nome do campo__: A ser definido pelo A&D

__Comentário__: Valor referente a Acréscimos Legais

__Tamanho__: 015V002

__Tipo__: N

__OS3424__

__RN105__

__Campo 105 \(campo reservado\): DATA FIM AÇÃO JUDICIAL:__

__Item:__ 105 \(Reservado\)

__Descrição do campo:__ Data Fim Ação Judicial

__Nome do campo:__ A ser definido pelo A&D

__Comentário:__ Referente a Data Fim da Ação Judicial

__Tamanho:__ 008

__Tipo:__ N

__OS3424__

__RN14__

__Tipo de Receita – Campo 14__

Novo código de Tipo de Receita, conforme abaixo:

Código: 4

Descrição: Ressarcimento

__OS3531__

__RN78__

__Campo 78 \- COD\_MODELO\_COTEPE__

Aceitar a importação do novo código de modelo “58”\.

__OS3564__

__RN63__

__Campo 63 – Classe de Consumo – SPED FISCAL \(COD\_CLASSE\_CONSUMO\)__

O código da classe de consumo informado para o campo 63 da SAFX42 é validado na Tabela de Classes de Consumo \(DWT\_CLASSE\_CONSUMO\), verificando se ele existe na tabela com modelo = modelo da nota, e indicador = “1”\. 

O indicador serve para identificar a qual obrigação se refere os códigos da tabela, onde neste caso será sempre “1”, pois trata\-se de SPED FISCAL\.

Este tratamento já existe atualmente, porém deve ser validado com a equipe de Qualidade se a importação está atendendo os novos códigos\.

Quando o código informado não for encontrado na tabela nas condições estabelecidas, gravar a mensagem abaixo no log, e não importar o registro:

   “Código da classe de consumo do SPED FISCAL inexistente ou inválido para o modelo do documento fiscal”

Obs\.: Esta mensagem pode ser alterada por A&D ou Conteúdo, caso julguem necessário\. Não encontrei mensagem semelhante na TFIX22\.

__OS3557__

__RN64__

__Campo – Identificador do  Documento Fiscal de Utilities__

__Tabela: __SAFX42

__Item: __A ser definido pelo A&D

__Nome do Campo:__ Será definido pelo A&D

__Descrição:__ Identificador do  Documento Fiscal de Utilities

__Tipo:__ A

__Tamanho: __128

__Não Obrigatório__

__Comentário: __Informar o Identificador do Documento Fiscal de Utilities

__OS3743__

__RN65__

__Campo – Código do  Sistema de Origem__

__Tabela: __SAFX42

__Item: __A ser definido pelo A&D

__Nome do Campo:__ Será definido pelo A&D

__Descrição:__ Código do Sistema de Origem

__Tipo:__ A

__Tamanho: __004

__Não Obrigatório__

__Comentário: __Informar o código do Sistema de Origem

__OS3743__

__RN66__

Deve ser recuperado o IDENT do registro de maior validade que seja menor ou igual a data da escrituração fiscal da nota \(SAFX42, campo 03\-DAT\_FISCAL\), no momento da atualização de dados na SAFX42/SAFX43, evitando assim, a duplicidade de registros nessas tabelas\.

__OS3931__

__RN110__

Campo __Quantidade de energia elétrica injetada__:

Campo *não* obrigatório criado pela OS4214\.

__OS4214__

__RN111__

Campo __Valor da energia elétrica injetada__:

Campo *não* obrigatório criado pela OS4214\.

__OS4214__

__RN69__

Campo Número do Lançamento

A rotina de Importação do módulo JOB Servidor deve ser ajustada para que contemple a alteração no campo NUM\_LANCTO\_CONTAIL da tabela SAFX42 – Arquivo de Notas Fiscais para Hotéis, que deve ser criada com a seguinte estrutura:

__ __

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

NUM\_LANCTO\_CONTABIL

A

40

NAO

NAO

__OS4579__

__RN21__

__Item__:__ __21

__Nome do Campo__: SITUACAO

__Descrição__: Situação da Nota

__Tamanho__:__ __001

__Tipo__: A

Não chave e não obrigatório

A regra de validação deste campo deve ser ajustada para permitir também a importação do conteúdo C \- Nota Fiscal complementar\. Hoje, o sistema aceita as opções S \- Nota Fiscal regularmente cancelada, N \- Nota Fiscal não cancelada ou R \- Refaturamento/ Substituto\.

__MFS\-1079__

__RN113__

__Item__:__ __A ser definido pelo A&D

__Nome do Campo__: Será definido pelo A&D

__Descrição__: Tipo de Cliente

__Tamanho__:__ __002

__Tipo__: A

Não chave e não obrigatório

O conteúdo deste campo deve ser nulo ou pertencer à TACES92, campo código, considerando o registro da TACES que tenha o Modelo de Documento da NF \(campo 13 – COD\_MODELO\) igual ao campo Modelo de Documento da TACES\.

Caso não exista registro com conteúdo cadastrado na TACES, retornar mensagem de erro: “Tipo de Cliente Inválido ou não cadastrado na TACES92”\.

__MFS\-1079__

__RN114__

__Item__:__ __A ser definido pelo A&D

__Nome do Campo__: Será definido pelo A&D

__Descrição__: Subclasse de Consumo

__Tamanho__:__ __002

__Tipo__: A

Não chave e não obrigatório

O conteúdo deste campo deve ser nulo ou pertencer à TACES93, campo código, considerando o registro da TACES que tenha o Modelo de Documento da NF \(campo 13 – COD\_MODELO\) igual ao campo Modelo de Documento da TACES\.

Caso não exista registro com conteúdo cadastrado na TACES, retornar mensagem de erro: “Subclasse de Consumo Inválida ou não cadastrado na TACES93”\.

__MFS\-1079__

__RN115__

__Item__:__ __A ser definido pelo A&D

__Nome do Campo__: Será definido pelo A&D

__Descrição__: Número do Terminal Telefônico Principal

__Tamanho__:__ __015

__Tipo__: A

Não chave e não obrigatório

__MFS\-1079__

__RN116__

__Item__:__ __A ser definido pelo A&D

__Nome do Campo__: Será definido pelo A&D

__Descrição__: Número da Fatura Comercial

__Tamanho__:__ __020

__Tipo__: A

Não chave e não obrigatório

__MFS\-1079__

__RN117__

__Item__:__ __A ser definido pelo A&D

__Nome do Campo__: Será definido pelo A&D

__Descrição__: Valor Total da Fatura

__Tamanho__:__ __015V002

__Tipo__: N

Não chave e não obrigatório

__MFS\-1079__

__RN118__

__Item__:__ __A ser definido pelo A&D

__Nome do Campo__: Será definido pelo A&D

__Descrição__: Data de Leitura Anterior

__Tamanho__:__ __008

__Tipo__: N

Não chave e não obrigatório

__MFS\-1079__

__RN119__

__Item__:__ __A ser definido pelo A&D

__Nome do Campo__: Será definido pelo A&D

__Descrição__: Número do Documento Fiscal Substituído / Complementado

__Tamanho__:__ __012

__Tipo__: A

Não chave e não obrigatório

__MFS\-1079__

__RN120__

__Item__:__ __A ser definido pelo A&D

__Nome do Campo__: Será definido pelo A&D

__Descrição__: Série do Documento Fiscal Substituído / Complementado

__Tamanho__:__ __003

__Tipo__: A

Não chave e não obrigatório

__MFS\-1079__

__RN121__

__Item__:__ __121

__Nome do Campo__: COD\_MODELO\_SUBST

__Descrição__: Modelo do Documento Fiscal Substituído/Complementado

__Tamanho__:__ __002

__Tipo__: A

Não chave e não obrigatório

\[__MFS74305__\]: Sped Fiscal Atualização 2022 \- Inclusão do código modelo 66

Os conteúdos válidos para este campo são “01”, “06”, “21” ,“22”, “62” OU “66” e devem estar cadastrados na SAFX2024\. 

Se for diferente deste conteúdo, gerar a mensagem de erro no log: 

*“913185 \- Modelo invalido para este tipo de documento \(codigo validos: 01, 06, 21, 22, 62 ou 66\)”*

__MFS\-1079__

__CH23207\_2017__

__\(MFS15833\)__

MFS74305

MFS432820

__RN122__

__Item__:__ __122

__Nome do Campo__: DAT\_EMIS\_SUBST

__Descrição__: Data Emissão do Documento Fiscal Substituído / Complementado

__Tamanho__:__ __008

__Tipo__: N

Não chave e não obrigatório

__MFS\-1079__

__RN123__

__Item__:__ __123

__Nome do Campo__: PERIOD\_APUR\_SUBST

__Descrição__: Período de Apuração do Documento Fiscal \(MMAAAA\) Substituído / Complementado

__Tamanho__:__ __006

__Tipo__: N

Não chave e não obrigatório

__MFS\-1079__

__RN124__

__Item__:__ __124

__Nome do Campo__: NUM\_AUTENTIC\_NFE

__Descrição__: Chave de Acesso \(CV115\-e\)

__Tamanho__:__ __080

__Tipo__: A

Não chave e não obrigatório

__MFS\-7160__

__RN125__

__Item__:__ __125

__Nome do Campo__: DAT\_EMISSAO\_NFE

__Descrição__: Data Autorização de Emissão \(CV115\-e\)

__Tamanho__:__ __008

__Tipo__: N

Não chave e não obrigatório

__MFS\-7160__

__RN126__

Campo __Finalidade Emissão da NFe__:               \(Campo criado na __MFS31252__\)

Campo *não* obrigatório\.

Poderá ser preenchido apenas quando o campo 13 \- Modelo do Documento = 62 \(NFCom\) ou 66 \(NF3e\)\. Se preenchimento para qualquer outro modelo de documento, o registro não será importado e será gravada uma mensagem de erro no log\. \(“*93274 \- O campo Finalidade Emissão NFe deve ser informado apenas quando se tratar de modelo de documento = 62 ou 66*”\)\.

Quando preenchido, seu conteúdo deve ser = 1 \(Normal\), 2 \(Substituição\) ou 3 \(Normal com Ajuste\)\. Caso contrário, o registro não será importado e será gravada uma mensagem de erro no log \(“*93275 \- Campo Finalidade Emissão NFe inválido\. Preencher com 1, 2 ou 3*”\)\.

__MFS31252__

MFS432820

__RN127__

Campo __Chave de Acesso da NFe Substituída__:                         \(Campo criado na __MFS31252__\)

__     __

Campo *não* obrigatório\.

Este campo só poderá ser informado quando o campo anterior \(campo “__Finalidade Emissão da NFe”__\) for válido e = “2” \(Substituição\)\. Caso contrário, o registro não será importado e será gravada uma mensagem de erro no log \(“*O* *campo Chave de Acesso da NFe Substituída deve ser informado apenas quando a Finalidade da Emissão da NFe for = 2\-Substituição*\)\.

__MFS31252__

__RN128__

\[__MFS74305__\]: Sped Fiscal Atualização 2022 \- Inclusão do Campo

Campo __Código de Autenticação Digital \(Convênio 115/2003\) NF Substituída__:

Campo *não* obrigatório\.

Este campo só poderá ser informado quando o campo “__Finalidade Emissão da NFe”__\) for válido e = “2” \(Substituição\) e o campo 121\- “__Modelo do Documento Fiscal Substituído/Complementado”__ for = “06” ou “21” ou “22” \. Caso contrário, o registro não será importado e será gravada uma mensagem de erro no log \(“*O* *campo Código de Autenticação Digital \(Convênio 115/2003\) NF Substituída deve ser informado apenas quando a Finalidade da Emissão da NFe for = 2\-Substituição e Modelo Doc\. Fiscal Substituído/Complementado for = 06, 21 ou 22*\)\. CÓDIGO 913179

MFS74305

MFS432820

__RN129__

\[__MFS74305__\]: Sped Fiscal Atualização 2022 \- Inclusão do Campo

Campo Valor Outras Deduções

Campo *não* obrigatório\.

MFS74305

RN130

Campo Tipo Faturamento NFe:      

Campo não obrigatório\.

Poderá ser preenchido apenas quando o campo 13 \- Modelo do Documento = 62 \(NFCom\)\. Se preenchimento para qualquer outro modelo de documento, o registro não será importado e será gravada uma mensagem de erro no log\. <a id="_Hlk118835084"></a>\(“O campo Tipo Faturamento NFe deve ser informado apenas quando se tratar de modelo de documento = 62” – código 913220\)\.

Quando preenchido, seu conteúdo deve ser = 0 \- Faturamento Normal, 1 \- Faturamento centralizado, 2 \- Cofaturamento\. Caso contrário, o registro não será importado e será gravada uma mensagem de erro no log \(“<a id="_Hlk118835114"></a>Campo Tipo Faturamento NFe inválido\. Preencher com 0 \(Normal\), 1 \(Centralizado\) ou 2 \(Cofaturamento\)” – código 913221\)\.

MFS432820

__RN131__

__Campo 131 – Tipo do Ambiente__

__Obrigatoriedade: Não obrigatório__

__Descrição: Tipo do Ambiente__

__Nome do Campo: IND\_TP\_AMB\_NFE__

__Tamanho: 001__

__Tipo: A__

__Edita: Não__

__Lista Fixa apresentanto os itens abaixo \+ Um item na lista em Branco:__

__1 \- Produção__

__2 – Homologação__

Se o campo for preenchido com algum valor diferente, será gravada mensagem de erro padrão  \(Verificar mensagem padrão\) e o registro não será importado\.

Validação do campo: o conteúdo informado deve ser igual a < Nulo >, <1> ou <2>\. Caso seja informado um código diferente, retornar a mensagem: “Indicador do Tipo do Ambiente inválido\. Informe <1> , <2> ou deixar em branco\.

Reserva TFIX22: 913241

__MFS591907__

__RN132__

__Campo 132 – Código numérico que compõe a Chave de Acesso__

__Obrigatoriedade: Não obrigatório__

__Descrição: Código Chave de Acesso__

__Nome do Campo: COD\_NF\_NFE__

__Tamanho: 007__

__Tipo: A__

__Edita: Sim__

__MFS591907__

__RN133__

__Campo 133 – Digito verificador da chave de acesso__

__Obrigatoriedade: Não obrigatório__

__Descrição: DV Chave de Acesso__

__Nome do Campo: COD\_DV\_NFE__

__Tamanho: 001__

__Tipo: A__

__Edita: Sim__

__MFS591907__

__RN134__

__Campo 134 – Indicador de serviço pré\-pago__

Obrigatoriedade: Não obrigatório

Descrição: Serviço pré\-pago

Nome do Campo: IND\_PRE\_PAGO

Tamanho: 001

Tipo: A

Edita: Sim

__Check\-Box com a descrição “Serviço Pré\-Pago”, marcando a opção inserir o valor “1” na base de dados atendendo à regra da NFCom \(__1 – Serviço pré\-pago \(informar a tag somente se a nota for referente a um serviço exclusivamente pré\-pago\)__ \)__

Se o campo for preenchido com algum valor diferente, será gravada mensagem de erro padrão  \(Verificar mensagem padrão\) e o registro não será importado\.

Validação do campo: o conteúdo informado deve ser igual a < Nulo > ou <1>\. Caso seja informado um código diferente, retornar a mensagem: “Indicador de Serviço Pré\-Pago inválido\. Informe <1> ou deixar em branco\.

Reserva TFIX22: 913242

__MFS591907__

__RN135__

__Campo 135 – Indicador de Sessão de Meios de Rede__

Obrigatoriedade: Não obrigatório

Descrição: Sessão de Meios de Rede

Nome do Campo: IND\_SESSAO\_REDE

Tamanho: 001

Tipo: A

Edita: Sim

Check\-Box com a descrição “Sessão de Meios de Rede”, marcando a opção inserir o valor “1” na base de dados atendendo à regra da NFCom \(\(valor = 1\), essa tag dispensa geração do grupo Fatura\.  
Apenas para notas dos tipos Normal e Substituição com tipo de faturamento normal\)

Validação do campo: o conteúdo informado deve ser igual a < Nulo > ou <1>\. Caso seja informado um código diferente, retornar a mensagem: “Indicador de Sessão de Meios de Rede inválido\. Informe <1> ou deixar em branco\.

Reserva TFIX22: 913243

__MFS591907__

__RN136__

__Campo 136 – Data de início do contrato__

Obrigatoriedade: Não obrigatório

Descrição: Data Início do contrato

Nome do Campo: DAT\_INI\_CONTRATO

Tamanho: 008

Tipo: N \(Campo de Data\)

Edita: Sim

__MFS591907__

__RN137__

__Campo 137 – Data de término do contrato__

Obrigatoriedade: Não obrigatório

Descrição: Data término do contrato

Nome do Campo: DAT\_FIM\_CONTRATO

Tamanho: 008

Tipo: N \(Campo de Data\)

Edita: Sim

__MFS591907__

__RN138__

__Campo 138 – Código da UF de habilitação do terminal__

Obrigatoriedade: Não obrigatório

Descrição: UF de habilitação do terminal

Nome do Campo: UF\_TERMINAL\_TEL

Tamanho: 002

Tipo: A

Edita: Sim

Validação do campo: Caso o campo esteja preenchido no arquivo, validar seu conteúdo na tabela ESTADO\. Se o código não existir na tabela Campo “COD\_ESTADO”, gravar a seguinte mensagem no log de importação e não gravar o registro:  “O Codigo da Unidade da Federacao de habilitação do Terminal é invalido\.”

Reserva TFIX22: 913244

__MFS591907__

__RN139__

__Campo 139 – Motivo da Substituição__

Obrigatoriedade: Não obrigatório

Descrição: Motivo da Substituição

Nome do Campo: COD\_MOTIVO\_SUBST

Tamanho: 002

Tipo: A

Edita: Sim

__Lista Fixa apresentanto os itens abaixo \+ Um item na lista em Branco:__

01 – Erro de Preço  
02 – Erro Cadastral  
03 – Decisão Judicial  
04 \- Erro de Tributação  
05 \- Descontinuidade do Serviço

Se o campo for preenchido com algum valor diferente, será gravada mensagem de erro padrão  \(Verificar mensagem padrão\) e o registro não será importado\.

Validação do campo: o conteúdo informado deve ser igual a < Nulo >, <1> , <2>, <3>, <4> ou <5>\. Caso seja informado um código diferente, retornar a mensagem: “Motivo da Substituição inválido\. Informe <1> , <2>, <3>, <4>, <5> ou deixar em branco\.

__\[MFS891513\]__ Alteração do conteúdo aceito na importação

__Obs__\.:  A importação deve aceitar o campo preenchido com o conteúdo 01 ou 1\.  A informação que consta no manual layout é que o campo deve ser informado com 01, 02, 03, 04, 05, mas na importação estava exigindo 1, 2, 3, 4 ou 5\.  Como hoje já existem linhas gravadas com 1, 2, 3, 4 ou 5 na SAFX42, será aceito importar com os dois conteúdos \(01 ou 1\), mas o conteúdo gravado no banco permanece com 1, 2, 3, 4 ou 5\.

Reserva TFIX22: 913245

__MFS591907__

__MFS891513__

__RN140__

__Campo 140 – Valor Total do ICMS desonerado__

Obrigatoriedade: Não obrigatório

Descrição: Valor ICMS Desonerado

Nome do Campo: VLR\_ICMS\_DESONERADO

Tamanho: 015V002

Tipo: N

Edita: Sim

__MFS591907__

__RN141__

__Campo 141 – Valor Total do FCP \(Fundo de Combate à Pobreza\)__

Obrigatoriedade: Não obrigatório

Descrição: Valor FCP \(Fundo de Combate à Pobreza\)

Nome do Campo: VLR\_FCP

Tamanho: 015V002

Tipo: N

Edita: Sim

__MFS591907__

__RN142__

__Campo 142 – Valor do COFINS__

Obrigatoriedade: Não obrigatório

Descrição: Valor COFINS

Nome do Campo: VLR\_COFINS

Tamanho: 015V002

Tipo: N

Edita: Sim

__MFS591907__

__RN143__

__Campo 143 – Valor do PIS__

Obrigatoriedade: Não obrigatório

Descrição: Valor PIS

Nome do Campo: VLR\_PIS

Tamanho: 015V002

Tipo: N

Edita: Sim

__MFS591907__

__RN144__

__Campo 144 – Valor do FUNTTEL__

Obrigatoriedade: Não obrigatório

Descrição: Valor FUNTTEL

Nome do Campo: VLR\_FUNTTEL

Tamanho: 015V002

Tipo: N

Edita: Sim

__MFS591907__

__RN145__

__Campo 145 – Valor do FUST__

Obrigatoriedade: Não obrigatório

Descrição: Valor FUST

Nome do Campo: VLR\_FUST

Tamanho: 015V002

Tipo: N

Edita: Sim

__MFS591907__

__RN146__

__Campo 146 – Valor do PIS retido__

Obrigatoriedade: Não obrigatório

Descrição: Valor PIS Retido

Nome do Campo: VLR\_PIS\_RETIDO

Tamanho: 015V002

Tipo: N

Edita: Sim

__MFS591907__

__RN147__

__Campo 147 – Valor do COFNS retido__

Obrigatoriedade: Não obrigatório

Descrição: Valor COFNS Retido

Nome do Campo: VLR\_COFINS\_RETIDO

Tamanho: 015V002

Tipo: N

Edita: Sim

__MFS591907__

__RN148__

__Campo 148 – Valor da CSLL retida__

Obrigatoriedade: Não obrigatório

Descrição: Valor CSLL Retida

Nome do Campo: VLR\_CSLL\_RETIDO

Tamanho: 015V002

Tipo: N

Edita: Sim

__MFS591907__

__RN149__

__Campo 149– Valor do IRRF retido__

Obrigatoriedade: Não obrigatório

Descrição: Valor IRRF Retido

Nome do Campo: VLR\_IRRF\_RETIDO

Tamanho: 015V002

Tipo: N

Edita: Sim

__MFS591907__

__RN150__

__Campo 150 – Saldo de pontos do cliente na data de referência__

Obrigatoriedade: Não obrigatório

Descrição: Saldo de Pontos do Cliente 

Nome do Campo: QTD\_PTS\_PROG\_FIDEL

Tamanho: 020

Tipo: N

Edita: Sim

__MFS591907__

__RN151__

__Campo 151 – Data de aferição do saldo de pontos__

Obrigatoriedade: Não obrigatório

Descrição: Data Aferição do Saldo de Pontos

Nome do Campo: DAT\_AFER\_PROG\_FIDEL

Tamanho: 008

Tipo: N \(Campo de Data\)

Edita: Sim

__MFS591907__

__RN152__

__Campo 152 – Qtd de pontos resgatados na data de referência__

Obrigatoriedade: Não obrigatório

Descrição: Qtd Pontos Resgatados

Nome do Campo: QTD\_REGAT\_PROG\_FIDEL

Tamanho: 020

Tipo: N

Edita: Sim

__MFS591907__

__RN153__

__Campo 153 – Data de resgate dos pontos__

Obrigatoriedade: Não obrigatório

Descrição: Data Resgate dos Pontos

Nome do Campo: DAT\_REGAT\_PROG\_FIDEL

Tamanho: 008

Tipo: N \(Campo de Data\)

Edita: Sim

__MFS591907__

__RN154__

__Campo 154 – URL do QRCode do PIX que será apresentado na fatura__

Obrigatoriedade: Não obrigatório

Descrição: URL QRCode do PIX 

Nome do Campo: COD\_QRCODE\_PIX

Tamanho: 2000

Tipo: A

Edita: Sim

__MFS591907__

__RN155__

__Campo 155 – CNPJ do Emitente centralizador do Faturamento__

Obrigatoriedade: Não obrigatório

Descrição: CNPJ do Emitente do Faturamento

Nome do Campo: CNPJ\_EMIT\_FATURAMENTO

Tamanho: 014

Tipo: A

Edita: Sim

__MFS591907__

__RN156__

__Campo 156 – UF do Emitente centralizador do Faturamento__

Obrigatoriedade: Não obrigatório

Descrição: UF do Emitente do Faturamento

Nome do Campo: UF\_EMIT\_FATURAMENTO

Tamanho: 002

Tipo: A

Edita: Sim

Validação do campo: Caso o campo esteja preenchido no arquivo, validar seu conteúdo na tabela ESTADO\. Se o código não existir na tabela Campo “COD\_ESTADO”, gravar a seguinte mensagem no log de importação e não gravar o registro: O Codigo da Unidade da Federacao do Emitente do Faturamento é invalido\.

Reserva TFIX22: 913246

__MFS591907__

__RN157__

__Campo 157 – CNPJ do autorizado para download__

Obrigatoriedade: Não obrigatório

Descrição: CNPJ Autorizado para download

Nome do Campo: CNPJ\_DOWNLOAD

Tamanho: 014

Tipo: A

Edita: Sim

__MFS591907__

__RN158__

__Campo 158 – CPF do autorizado para download__

Obrigatoriedade: Não obrigatório

Descrição: CPF Autorizado para download

Nome do Campo: CPF\_DOWNLOAD

Tamanho: 011

Tipo: A

Edita: Sim

__MFS591907__

__RN159__

__Campo 159 – Código de autorização débito em conta__

Obrigatoriedade: Não obrigatório

Descrição: Cod\. Autorização débito em conta

Nome do Campo: COD\_DEBITO\_AUTO

Tamanho: 030

Tipo: A

Edita: Sim

__MFS591907__

__RN160__

__Campo 160 – Número do banco para débito em conta__

Obrigatoriedade: Não obrigatório

Descrição: Banco Débito em Conta

Nome do Campo: COD\_BANCO\_AUTO

Tamanho: 010

Tipo: A

Edita: Sim

__MFS591907__

__RN161__

__Campo 161 – Número da agência bancária para débito em conta__

Obrigatoriedade: Não obrigatório

Descrição: Agência Débito em Conta

Nome do Campo: COD\_AGENCIA\_AUTO

Tamanho: 015

Tipo: A

Edita: Sim

__MFS591907__

__RN162__

__Campo 162– Chave de acesso da NFCom emitida pela Operadora Local__

Obrigatoriedade: Não obrigatório

Descrição: Chave de acesso da NFCom emitida pela Operadora Local

Nome do Campo: COD\_AUTENTIC\_COF

Tamanho: 044

Tipo: A

Edita: Sim

__MFS591907__

__RN169__

__Campo 169 \- Base de Cálculo do ICMS referente a Energia Injetada__

Obrigatoriedade: Não obrigatório

Descrição: Base de Cálculo do ICMS referente a Energia Injetada

Nome do Campo: VLR\_BC\_ICMS\_INJ

Tamanho: 015V002

Tipo: N

Validação do campo:

O campo VLR\_BC\_ICMS\_INJ não é obrigatório, mas quando preenchido, deve ser um valor decimal/numérico válido\.

Quando o campo for preenchido com valor inválido, o registro não será importado e será gravada no log de erros: 

__90461 – Valor Decimal ou Numerico com formato invalido\.__

MFS981990

__RN170__

__Campo 170 \- Valor do ICMS referente a Energia Injetada__

Obrigatoriedade: Não obrigatório

Descrição: Valor do ICMS referente a Energia Injetada

Nome do Campo: VLR\_ICMS\_INJ

Tamanho: 015V002

Tipo: N

Validação do campo:

O campo VLR\_ICMS\_INJ não é obrigatório, mas quando preenchido, deve ser um valor decimal/numérico válido\.

Quando o campo for preenchido com valor inválido, o registro não será importado e será gravada no log de erros: 

__90461 – Valor Decimal ou Numerico com formato invalido\.__

MFS981990

__RM171__

__Campo 171 \- Valor da Alíquota do ICMS referente a Energia Injetada__

Obrigatoriedade: Não obrigatório

Descrição: Valor da Alíquota do ICMS referente a Energia Injetada

Nome do Campo: VLR\_ALIQ\_ICMS\_INJ

Tamanho: 003V004

Tipo: N

Validação do campo:

O campo VLR\_ALIQ\_ICMS\_INJ não é obrigatório, mas quando preenchido, deve ser um valor decimal/numérico válido\.

Quando o campo for preenchido com valor inválido, o registro não será importado e será gravada no log de erros: 

__90461 – Valor Decimal ou Numerico com formato invalido\.__

MFS981990

