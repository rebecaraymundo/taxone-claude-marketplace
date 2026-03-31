# MTZ_EFD_Pre_Geracao_Registro_1400_Convenio_52

- **Fonte:** MTZ_EFD_Pre_Geracao_Registro_1400_Convenio_52.docx
- **Modificado:** 2022-03-29
- **Tamanho:** 95 KB

---

THOMSON REUTERS

Pré\-Geração do Registro 1400 – Convênio ICMS 52/05

EFD\-Escrituração Fiscal Digital

__Localização__: Menu Sped, Módulo EFD \- Escrituração Fiscal Digital, item Pré\-Geração à Registro 1400 – Conv\. ICMS 52/05

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

__Data__

MFS\-16364

Julyana Perrucini

Essa MFS tem como objetivo realizar a geração do “Registro 1400 – Valores Sobre Valores Agregados” da obrigação acessória EFD\-ICMS/IPI para todas as unidades federadas as quais a empresa possua inscrição estadual "virtual" em linha com o Convênio ICMS 52/05\.

MFS\-22066

Julyana Perrucini

Essa MFS tem como objetivo alterar o valor a ser apurado, retirando a obrigatoriedade de informar o valor devido em outra UF em pelo menos um dos itens\.

MFS20218

Vânia Mattos

Alteração na geração do registro 1400, nos códigos de periodicidade anual de MG e RN; 

24/01/2019

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN1400

__Regra Geral__

As regras de geração do registro 1400 para as empresas com inscrição estadual “virtual” dependem do parâmetro “__Tipo de Geração__” da parametrização das Inscrições Estaduais do Convênio ICMS 52/05 da EFD \(menu “Geração – Conv\. ICMS 52/05 à Inscrições Estaduais”\), então para cada UF/ Inscrição Estadual cadastrada serão recuperados e agrupados todos os municípios ou municípios \+ produtos \(este último no caso do usuário optar da parametrização para gerar por produto e se aplica apenas à geração Padrão\)\.

Para gerar os documentos fiscais utilities serão consideradas as informações geradas no Bloco D \(Registro D695 e Registro D696\) da regra do Convênio ICMS 52/05, que contém o detalhamento dos valores totalizados por CST/ CFOP/ ALIQ/ UF\.

No Registro 1400 será considerada a UF/Município de consumo que é onde de fato o serviço foi prestado, pois o cadastro do destinatário nem sempre representa a prestação do serviço, porque podem existir clientes em um estado, mas que tem serviços contratados em outro estado\. Apesar do Bloco D considerar apenas os itens que contenham Base de Cálculo e ICMS devido a outra UF, aqui será sumarizado todo o valor de serviço de todos os itens pela UF/Município de consumo que está sendo gerado, pois o valor repassado do município é o valor total prestado, independente se houve tributação ou não do ICMS no serviço\.

Existem dois tipos de geração:

- Padrão à É a geração original, feita na época da criação do registro 1400\. Não segue a regra específica de nenhuma UF, apenas as orientações do Guia Prático;
- Específica por UF à Modalidade de geração que atende as UF que possuem regras próprias para geração do registro 1400\. São as UF que divulgaram a tabela “*Tabela de Itens UF Índice de Participação dos Municípios*” no site da EFD\.

De acordo com o parâmetro “__Tipo de Geração__”, o registro 1400 será gerado \(quando marcado no perfil\) da seguinte forma:

__Parâmetro__

__Regras da Geração__

Opção “Padrão”

Neste caso a geração será feita dependendo da UF/ Inscrição Estadual virtual usando a geração original da criação do registro 1400\.

Consultar a seguinte regra: “__RN1400\-XX__”

Opção “Específica por UF”

Neste caso a geração será feita dependendo da UF/ Inscrição Estadual virtual usando a tabela de índice da geração específica de cada UF:

Se UF da Inscrição Virtual = “__MG__”:

     O registro 1400 será gerado de acordo com as regras específicas de MG \(Resolução 4317, Dez/2014\)\. Consultar as regras denominadas “__RN1400\-MG__”

Se UF da Inscrição Virtual = “__SP__”:

     O registro 1400 será gerado de acordo com as regras específicas de SP \(Portaria CAT 137, Dez/2014\)\. Consultar as regras denominadas “__RN1400\-SP__”

Se UF da Inscrição Virtual = “__ES__”:

     O registro 1400 será geração de acordo com as regras específicas do ES \(Portaria N\. 34\-R, Ago/2015\)\. Consultar as regras denominadas “__RN1400\-ES__”

Se UF da Inscrição Virtual = “__RN__”:

O registro 1400 será gerado de acordo com as regras específicas do RN \(Orientação Técnica EFD nº 011/2016, Jan/2016\)\. Consultar as regras denominadas “__RN1400\-RN__”

Se UF da Inscrição Virtual = “__RS__”:

     O registro 1400 será gerado de acordo com as regras específicas do RS \(Sem publicação de Ato Legal\)\. Consultar as regras denominadas “__RN1400\-RS__”

Se UF da Inscrição Virtual = “__BA__”:

     O registro 1400 será gerado de acordo com as regras específicas da BA \(Sem publicação de Ato Legal\)\. Consultar as regras denominadas “__RN1400\-BA__”

Se UF da Inscrição Virtual <> “__MG__” e <> “__SP__” e <> “__ES__” e <> “__RN__” e <>__ “RS”__ e <>__ “BA”__

     Nesse caso, o registro 1400 *não* será gerado, já que ainda *não* existem regras específicas para nenhuma outra UF, além destas\.

Os registros serão processados e gravados na tabela de Manutenção do Registro 1400 \(menu “Geração à Manutenção à Registro 1400”\) para posteriormente serem gerados no arquivo magnético da EFD de acordo com o Convênio ICMS 52/05\.

MFS\-16364

RN1400\-XX

__Regra p/ gerar as UF que utilizam a opção “Padrão”:__

A geração do 1400 para a modalidade “XX” é feita de acordo com os dados solicitados no Guia Prático da EFD\-ICMS/IPI\.

Os valores a serem gerados nessa rotina são referentes ao seguinte segmento: Telecom\.

Estes valores servirão para gerar o índice de participação dos municípios\.

As notas fiscais *sem* o ponto de consumo da SAFX42 preenchido não serão processadas, e, portanto, não irão compor o valor adicionado do município em questão\.

Na prática, todas as __notas fiscais de saída__ gravadas no registro específico de Telecom \(D695\) deverão ser totalizadas para geração dos valores do registro 1400\.

__Processamento 1 \- Totalização do Valor das Operações do Período:__

<a id="_Hlk505945354"></a>Totalizar o valor do serviço das notas fiscais da SAFX42/SAFX43 que atendam aos seguintes critérios: 

- Selecionar os documentos fiscais utilities do estabelecimento igual informado na tela de geração;
- UF da Inscrição Estadual virtual deve ser a mesma UF do ponto de consumo \(campo 75\-UF\_CONSUMO da SAFX42\), se a UF não estiver preenchida o registro será desconsiderado;
- Município deve ser do ponto de consumo \(campo 76\-COD\_MUNIC\_CONSUMO da SAFX42\), se o município não estiver preenchido o registro será desconsiderado;
- <a id="_Hlk505945341"></a>Modelo de comunicação/telecomunicação \(campo 13\-COD\_MODELO da SAFX42 = 21, 22\);
- Data Fiscal \(campo 03\-DAT\_FISCAL da SAFX42\) dentro do período da geração *ou* data extemporânea dentro do período de geração;
- Itens de Mercadoria/ Mercadoria e Serviço \(campo 50\-COD\_CLASS\_DOC\_FIS da SAFX42 = 1, 3\)\. *Atenção:* no caso das notas mistas, totalizar o valor dos itens de mercadoria e serviço;
- Situação não cancelada \(campo 21\-SITUACAO da SAFX42 <> S\);
- Não considerar os itens informativos \(campo 10\-IND\_TP\_REGISTRO da SAFX43 <> 1\);
- Somente operações interestaduais \(campo 13\-COD\_CFO da SAFX43 iniciados com “6” e “7”\)\.

OBS: Como as regras são as mesmas do registro específico \(D696 para Telecom\), além destes critérios de filtro, devem\-se considerar também as notas fiscais com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR dos registros analíticos\.

__\[ALTERADA \- MFS\-22066\]__

__Valor a ser totalizado =__ Valor do serviço do item \(campo 19\-VLR\_SERVICO da SAFX43\)\., considerando que serão sumarizados os valores de todos os itens se pelo menos um dos itens estiver com os valores da BC e do ICMS devido à outra UF maiores que “0” \(zero\) \(campos 103\-VLR\_BC\_ICMS\_UF e 104\-VLR\_ICMS\_UF da SAFX43 > 0,00\), ou seja, se no documento fiscal utilities não houver nenhum item que tenha esses campos preenchidos o registro não será considerado na totalização dos valores\.

__Se__ parâmetro “Calcular Valores por Produto” = S 

     Totalizar por Produto \(campo 12\-COD\_PRODUTO da SAFX43\) e Município \(campo 76\-COD\_MUNIC\_CONSUMO da SAFX42\);

__Senão__

     Totalizar por Município \(campo 76\-COD\_MUNIC\_CONSUMO da SAFX42\)\.

OBS: a totalização das operações de Utilities não pode ser pela SAFX07/SAFX08, pois não há a informação do Terminal Faturado, pois este dado não é tratado na geração do Mapa Resumo\. A informação de terminal faturado que existe na SAFX07 foi incluída recentemente para atender ao AC 70, e é utilizado apenas para as notas de entrada\.

__Processamento 2 – Gravar dados na tabela:__

Gravar os valores apurados, devendo verificar se existem valores informados manualmente para o período e município apurado, através do item de menu “Geração à Manutenção à Registro 1400”\.

__Campo Tabela:__

__Gravar:__

Estabelecimento

Estabelecimento selecionado na tela de geração\.

Período

Período inicial e final de acordo com mês/ ano preenchido na tela de geração*\. Exemplo: 01/2018 gravar 01/01/2018 a 31/01/2018*\.

Produto

Produto agrupado na seleção dos dados se a opção de geração for para calcular por produto\. *Observação: Os campos referentes ao produto serão preenchidos com um caractere branco, pois fazem parte da chave da tabela*\.

Município

UF = UF do município apurado\.

Código do município apurado agrupado na seleção dos dados\.

Código da Tabela de Itens p/o Índice de Participação dos municípios

Não se aplica\.

__*Valores Calculados*__

Valor Apurado

Não se aplica\.

Deduções

Não se aplica\.

__*Valores Conv\. ICMS 52/05*__

Valor Apurado

Soma dos valores calculados por Município ou Município \+ Produto

Deduções

Não se aplica no momento\.

__*Valores Informados*__

Outros Valores

Não se aplica\.

Outras Deduções

Não se aplica\.

Valor Total

Não se aplica\.

MFS\-16364

RN1400\-MG

__Regra p/ gerar as UF que utilizam a opção “Específica por UF” = MG:__

A geração do 1400 para a modalidade “MG” é feita de acordo com os dados solicitados na Resolução 4\.730, de 17/12/2014, SEF\-MG\.

Nesse Convênio iremos tratar o item a seguir descrito na Resolução:

- Outros \(item __3\.6__\)\.

Apesar desse item ser anual na Resolução a entrega será feita de forma mensal da EFD para esse Convênio\.

__Alteração MFS20218__: A apuração do código 3\.6 para MG foi desenvolvida originalmente para filtrar as notas apenas do mês informado\. No entanto, este código é para informar as operações do ano todo, e sua entrega é apenas no arquivo da escrituração de dezembro\.  

A geração deste código 3\.6 de MG será feita apenas quando o mês informado for = dezembro\. Caso contrário, não será gerado\.

As notas fiscais *sem* o ponto de consumo da SAFX42 preenchido não serão processadas, e, portanto, não irão compor o valor adicionado do município em questão\.

__Outras Entradas a Detalhar por Município__

__  __

__Processamento 1 \- Totalização do Valor das Operações do Período:__

Totalizar o valor do serviço das notas fiscais da SAFX42/SAFX43 que atendam aos seguintes critérios: 

- Selecionar os documentos fiscais utilities do estabelecimento igual informado na tela de geração;
- UF da Inscrição Estadual virtual deve ser a mesma UF do ponto de consumo \(campo 75\-UF\_CONSUMO da SAFX42\), se a UF não estiver preenchida o registro será desconsiderado;
- Município deve ser do ponto de consumo \(campo 76\-COD\_MUNIC\_CONSUMO da SAFX42\), se o município não estiver preenchido o registro será desconsiderado;
- Modelo de comunicação/telecomunicação \(campo 13\-COD\_MODELO da SAFX42 = 21, 22\);
- Data Fiscal \(campo 03\-DAT\_FISCAL da SAFX42\) dentro do período da geração *ou* data extemporânea dentro do período de geração; __\(MFS20218\)__
- Data Fiscal \(campo 03\-DAT\_FISCAL da SAFX42\) deve ser uma data cujo ano seja = ano do período informado em tela;
- Somente notas com  CFOP ou CFOP/Natureza parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à CFOP ou CFOP/Natureza de Operação”, para a operação = “__Outras\_Entradas\_a\_Detalhar\_Por\_Municipio__” da UF = MG;
- Como os documentos da SAFX42/43 sempre têm itens, será utilizado o CFOP ou CFOP/Natureza do item;
- Situação não cancelada \(campo 21\-SITUACAO da SAFX42 <> S\);
- Não considerar os itens informativos \(campo 10\-IND\_TP\_REGISTRO da SAFX43 <> 1\);
- Somente operações interestaduais \(campo 13\-COD\_CFO da SAFX43 iniciados com “6” e “7”\)\.

__\[ALTERADA \- MFS\-22066\]__

__Valor a ser totalizado =__ Valor do serviço do item \(campo 19\-VLR\_SERVICO da SAFX43\)\., considerando que serão sumarizados os valores de todos os itens se pelo menos um dos itens estiver com os valores da BC e do ICMS devido à outra UF maiores que “0” \(zero\) \(campos 103\-VLR\_BC\_ICMS\_UF e 104\-VLR\_ICMS\_UF da SAFX43 > 0,00\), ou seja, se no documento fiscal utilities não houver nenhum item que tenha esses campos preenchidos o registro não será considerado na totalização dos valores\.

__Processamento 2 – Gravar dados na tabela:__

Gravar os valores apurados, devendo verificar se existem valores informados manualmente para o período e município apurado, através do item de menu “Geração à Manutenção à Registro 1400”\.

__Campo Tabela:__

__Gravar:__

Estabelecimento

Estabelecimento selecionado na tela de geração\.

Período

Período inicial e final de acordo com mês/ ano preenchido na tela de geração*\. Exemplo: 01/2018 gravar 01/01/2018 a 31/01/2018*\.

Produto

Os campos referentes ao produto serão preenchidos com um caractere branco, pois fazem parte da chave da tabela\.

Município

UF = MG

Código do município apurado agrupado na seleção dos dados\.

Código da Tabela de Itens p/o Índice de Participação dos municípios

Outras\_Entradas\_a\_Detalhar\_por\_Municipio\.

__*Valores Calculados*__

Valor Apurado

Não se aplica\.

Deduções

Não se aplica\.

__*Valores Conv\. ICMS 52/05*__

Valor Apurado

Soma dos valores apurados por Município\.

Deduções

Não se aplica no momento\.

__*Valores Informados*__

Outros Valores

Não se aplica\.

Outras Deduções

Não se aplica\.

Valor Total

Não se aplica\.

MFS\-16364

MFS20218

RN1400\-SP

__Regra p/ gerar as UF que utilizam a opção “Específica por UF” = SP:__

A geração do 1400 para a modalidade “SP” foi desenvolvida de acordo com as mesmas regras utilizadas na geração da DIPAM\-B \(registro 30\) da GIA\-SP\.

Nesse Convênio iremos tratar o item a seguir descrito na DIPAM\-B:

- Comunicação \(item __SPDIPAM24__\)\.

As notas fiscais *sem* o ponto de consumo da SAFX42 preenchido não serão processadas, e, portanto, não irão compor o valor adicionado do município em questão\.

__Código SPDIPAM 24__ 

__Processamento 1 \- Totalização do Valor das Operações do Período:__

Totalizar o valor do serviço das notas fiscais da SAFX42/SAFX43 que atendam aos seguintes critérios: 

- Selecionar os documentos fiscais utilities do estabelecimento igual informado na tela de geração;
- UF da Inscrição Estadual virtual deve ser a mesma UF do ponto de consumo \(campo 75\-UF\_CONSUMO da SAFX42\), se a UF não estiver preenchida o registro será desconsiderado;
- Município deve ser do ponto de consumo \(campo 76\-COD\_MUNIC\_CONSUMO da SAFX42\), se o município não estiver preenchido o registro será desconsiderado;
- Modelo de comunicação/telecomunicação \(campo 13\-COD\_MODELO da SAFX42 = 21, 22\);
- Data Fiscal \(campo 03\-DAT\_FISCAL da SAFX42\) dentro do período da geração *ou* data extemporânea dentro do período de geração;
- Itens de Mercadoria/ Mercadoria e Serviço \(campo 50\-COD\_CLASS\_DOC\_FIS da SAFX42 = 1, 3\)\. *Atenção:* no caso das notas mistas, totalizar o valor dos itens de mercadoria e serviço;
- Somente notas com  CFOP ou CFOP/Natureza parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à CFOP ou CFOP/Natureza de Operação”, para a operação = “__SPDIPAM24__” da UF = SP;
- Como os documentos da SAFX42/43 sempre têm itens, será utilizado o CFOP ou CFOP/Natureza do item;
- Situação não cancelada \(campo 21\-SITUACAO da SAFX42 <> S\);
- Não considerar os itens informativos \(campo 10\-IND\_TP\_REGISTRO da SAFX43 <> 1\);
- Somente operações interestaduais \(campo 13\-COD\_CFO da SAFX43 iniciados com “6” e “7”\)\.

__\[ALTERADA \- MFS\-22066\]__

__Valor a ser totalizado =__ Valor do serviço do item \(campo 19\-VLR\_SERVICO da SAFX43\)\., considerando que serão sumarizados os valores de todos os itens se pelo menos um dos itens estiver com os valores da BC e do ICMS devido à outra UF maiores que “0” \(zero\) \(campos 103\-VLR\_BC\_ICMS\_UF e 104\-VLR\_ICMS\_UF da SAFX43 > 0,00\), ou seja, se no documento fiscal utilities não houver nenhum item que tenha esses campos preenchidos o registro não será considerado na totalização dos valores\.

__Se__ parâmetro “Utilizar a parametrização de produtos \(DIPAM\-B – SP\)” = S 

     Considerar apenas os itens com produtos parametrizados no menu “Parâmetros à  Registro 1400 à Específico por UF à DIPAM\-B x Produto”;

__Senão__

     Considerar qualquer tipo de produto\.

Da mesma forma que é feito na geração padrão e na geração de MG do registro 1400, a totalização das notas/itens para geração deste código da DIPAM, pode ser feita \(se possível\), durante a geração do registro D695 e filhos \(pois são notas de telecom\), para uma melhor performance\. Mas, observando que neste item trabalhamos com parametrização de CFOP e de produto \(opcionalmente\)\.

__Processamento 2 – Gravar dados na tabela:__

Gravar os valores apurados, devendo verificar se existem valores informados manualmente para o período e município apurado, através do item de menu “Geração à Manutenção à Registro 1400”\.

__Campo Tabela:__

__Gravar:__

Estabelecimento

Estabelecimento selecionado na tela de geração\.

Período

Período inicial e final de acordo com mês/ ano preenchido na tela de geração*\. Exemplo: 01/2018 gravar 01/01/2018 a 31/01/2018*\.

Produto

Os campos referentes ao produto serão preenchidos com um caractere branco, pois fazem parte da chave da tabela\.

Município

UF = SP

Código do município apurado agrupado na seleção dos dados\.

Código da Tabela de Itens p/o Índice de Participação dos municípios

SPDIPAM24\.

__*Valores Calculados*__

Valor Apurado

Não se aplica\.

Deduções

Não se aplica\.

__*Valores Conv\. ICMS 52/05*__

Valor Apurado

Soma dos valores apurados por Município\.

Deduções

Não se aplica no momento\.

__*Valores Informados*__

Outros Valores

Não se aplica\.

Outras Deduções

Não se aplica\.

Valor Total

Não se aplica\.

MFS\-16364

RN1400\-ES

__Regra p/ gerar as UF que utilizam a opção “Específica por UF” = ES:__

A geração do 1400 para a modalidade “ES” é feita de acordo com os dados solicitados na Portaria N\. 34\-R, de Ago/2015, SEF\-ES\.

Nesse Convênio iremos tratar o item a seguir descrito na Portaria:

- Prestação de serviços de comunicação ou telecomunicação \(item __ESIPM07__\)\.

As notas fiscais *sem* o ponto de consumo da SAFX42 preenchido não serão processadas, e, portanto, não irão compor o valor adicionado do município em questão\.

__Código ESIPM07__

__Processamento 1 \- Totalização do Valor das Operações do Período:__

Totalizar o valor do serviço das notas fiscais da SAFX42/SAFX43 que atendam aos seguintes critérios: 

- Selecionar os documentos fiscais utilities do estabelecimento igual informado na tela de geração;
- UF da Inscrição Estadual virtual deve ser a mesma UF do ponto de consumo \(campo 75\-UF\_CONSUMO da SAFX42\), se a UF não estiver preenchida o registro será desconsiderado;
- Município deve ser do ponto de consumo \(campo 76\-COD\_MUNIC\_CONSUMO da SAFX42\), se o município não estiver preenchido o registro será desconsiderado;
- Modelo de comunicação/telecomunicação \(campo 13\-COD\_MODELO da SAFX42 = 21, 22\);
- Data Fiscal \(campo 03\-DAT\_FISCAL da SAFX42\) dentro do período da geração *ou* data extemporânea dentro do período de geração;
- Situação não cancelada \(campo 21\-SITUACAO da SAFX42 <> S\);
- Não considerar os itens informativos \(campo 10\-IND\_TP\_REGISTRO da SAFX43 <> 1\);
- Somente operações interestaduais \(campo 13\-COD\_CFO da SAFX43 iniciados com “6” e “7”\)\.

__\[ALTERADA \- MFS\-22066\]__

__Valor a ser totalizado =__ Valor do serviço do item \(campo 19\-VLR\_SERVICO da SAFX43\)\., considerando que serão sumarizados os valores de todos os itens se pelo menos um dos itens estiver com os valores da BC e do ICMS devido à outra UF maiores que “0” \(zero\) \(campos 103\-VLR\_BC\_ICMS\_UF e 104\-VLR\_ICMS\_UF da SAFX43 > 0,00\), ou seja, se no documento fiscal utilities não houver nenhum item que tenha esses campos preenchidos o registro não será considerado na totalização dos valores\.

__Processamento 2 – Gravar dados na tabela:__

Gravar os valores apurados, devendo verificar se existem valores informados manualmente para o período e município apurado, através do item de menu “Geração à Manutenção à Registro 1400”\.

__Campo Tabela:__

__Gravar:__

Estabelecimento

Estabelecimento selecionado na tela de geração\.

Período

Período inicial e final de acordo com mês/ ano preenchido na tela de geração*\. Exemplo: 01/2018 gravar 01/01/2018 a 31/01/2018*\.

Produto

Os campos referentes ao produto serão preenchidos com um caractere branco, pois fazem parte da chave da tabela\.

Município

UF = ES

Código do município apurado agrupado na seleção dos dados\.

Código da Tabela de Itens p/o Índice de Participação dos municípios

ESIPM07\.

__*Valores Calculados*__

Valor Apurado

Não se aplica\.

Deduções

Não se aplica\.

__*Valores Conv\. ICMS 52/05*__

Valor Apurado

Soma dos valores apurados por Município\.

Deduções

Não se aplica no momento\.

__*Valores Informados*__

Outros Valores

Não se aplica\.

Outras Deduções

Não se aplica\.

Valor Total

Não se aplica\.

MFS\-16364

RN1400\-RN

__Regra p/ gerar as UF que utilizam a opção “Específica por UF” = RN:__

A geração do 1400 para a modalidade “RN” é feita de acordo com os dados solicitados na Orientação Técnica EFD nº 011/2016, SET\-RN\.

Nesse Convênio iremos tratar o item a seguir descrito na Orientação Técnica:

- Atividades de Prestação de Serviços de Comunicação/Telecomunicação \(item __4\.6__\)\.

Apesar desse item ser anual na Orientação Técnica a entrega será feita de forma mensal da EFD para esse Convênio\.

__Alteração MFS20218__: A apuração do código 4\.6 para o RN foi desenvolvida originalmente para filtrar as notas apenas do mês informado\. No entanto, este código é para informar as operações do ano todo, e sua entrega é apenas no arquivo da escrituração de dezembro\.  

A geração deste código 4\.6 do RN será feita apenas quando o mês informado for = dezembro\. Caso contrário, não será gerado\.

As notas fiscais *sem* o ponto de consumo da SAFX42 preenchido não serão processadas, e, portanto, não irão compor o valor adicionado do município em questão\.

__Código IPM 4\.6__

__Processamento 1 \- Totalização do Valor das Operações do Período:__

Totalizar o valor do serviço das notas fiscais da SAFX42/SAFX43 que atendam aos seguintes critérios: 

- Selecionar os documentos fiscais utilities do estabelecimento igual informado na tela de geração;
- UF da Inscrição Estadual virtual deve ser a mesma UF do ponto de consumo \(campo 75\-UF\_CONSUMO da SAFX42\), se a UF não estiver preenchida o registro será desconsiderado;
- Município deve ser do ponto de consumo \(campo 76\-COD\_MUNIC\_CONSUMO da SAFX42\), se o município não estiver preenchido o registro será desconsiderado;
- Modelo de comunicação/telecomunicação \(campo 13\-COD\_MODELO da SAFX42 = 21, 22\);
- Data Fiscal \(campo 03\-DAT\_FISCAL da SAFX42\) dentro do período da geração *ou* data extemporânea dentro do período de geração; __\(MFS20218\)__
- Data Fiscal \(campo 03\-DAT\_FISCAL da SAFX42\) deve ser uma data cujo ano seja = ano do período informado em tela;
- Somente notas com  CFOP ou CFOP/Natureza parametrizado no menu “Parâmetros à Registro 1400 à Específico por UF à CFOP ou CFOP/Natureza de Operação”, para a operação = “__IPM 4\.6__” da UF = RN;
- Como os documentos da SAFX42/43 sempre têm itens, será utilizado o CFOP ou CFOP/Natureza do item;
- Situação não cancelada \(campo 21\-SITUACAO da SAFX42 <> S\);
- Não considerar os itens informativos \(campo 10\-IND\_TP\_REGISTRO da SAFX43 <> 1\);
- Somente operações interestaduais \(campo 13\-COD\_CFO da SAFX43 iniciados com “6” e “7”\)\.

__\[ALTERADA \- MFS\-22066\]__

__Valor a ser totalizado =__ Valor do serviço do item \(campo 19\-VLR\_SERVICO da SAFX43\)\., considerando que serão sumarizados os valores de todos os itens se pelo menos um dos itens estiver com os valores da BC e do ICMS devido à outra UF maiores que “0” \(zero\) \(campos 103\-VLR\_BC\_ICMS\_UF e 104\-VLR\_ICMS\_UF da SAFX43 > 0,00\), ou seja, se no documento fiscal utilities não houver nenhum item que tenha esses campos preenchidos o registro não será considerado na totalização dos valores\.

__Processamento 2 – Gravar dados na tabela:__

Gravar os valores apurados, devendo verificar se existem valores informados manualmente para o período e município apurado, através do item de menu “Geração à Manutenção à Registro 1400”\.

__Campo Tabela:__

__Gravar:__

Estabelecimento

Estabelecimento selecionado na tela de geração\.

Período

Período inicial e final de acordo com mês/ ano preenchido na tela de geração*\. Exemplo: 01/2018 gravar 01/01/2018 a 31/01/2018*\.

Produto

Os campos referentes ao produto serão preenchidos com um caractere branco, pois fazem parte da chave da tabela\.

Município

UF = RN

Código do município apurado agrupado na seleção dos dados\.

Código da Tabela de Itens p/o Índice de Participação dos municípios

IPM 4\.6\.

__*Valores Calculados*__

Valor Apurado

Não se aplica\.

Deduções

Não se aplica\.

__*Valores Conv\. ICMS 52/05*__

Valor Apurado

Soma dos valores apurados por Município\.

Deduções

Não se aplica no momento\.

__*Valores Informados*__

Outros Valores

Não se aplica\.

Outras Deduções

Não se aplica\.

Valor Total

Não se aplica\.

MFS\-16364

MFS20218

RN1400\-RS

__Regra p/ gerar as UF que utilizam a opção “Específica por UF” = RS:__

A geração do 1400 para a modalidade “RS” é feita de acordo com os códigos específicos da tabela do RS \(Tabela de Itens UF Índice de Participação dos Municípios\)\.

Nesse Convênio iremos tratar o item a seguir descrito na tabela do RS:

- Comunicação \(item __03__\)\.

As notas fiscais *sem* o ponto de consumo da SAFX42 preenchido não serão processadas, e, portanto, não irão compor o valor adicionado do município em questão\.

__Código 03__

__Processamento 1 \- Totalização do Valor das Operações do Período:__

Totalizar o valor do serviço das notas fiscais da SAFX42/SAFX43 que atendam aos seguintes critérios: 

- Selecionar os documentos fiscais utilities do estabelecimento igual informado na tela de geração;
- UF da Inscrição Estadual virtual deve ser a mesma UF do ponto de consumo \(campo 75\-UF\_CONSUMO da SAFX42\), se a UF não estiver preenchida o registro será desconsiderado;
- Município deve ser do ponto de consumo \(campo 76\-COD\_MUNIC\_CONSUMO da SAFX42\), se o município não estiver preenchido o registro será desconsiderado;
- Modelo de comunicação/telecomunicação \(campo 13\-COD\_MODELO da SAFX42 = 21, 22\);
- Data Fiscal \(campo 03\-DAT\_FISCAL da SAFX42\) dentro do período da geração *ou* data extemporânea dentro do período de geração;
- Situação não cancelada \(campo 21\-SITUACAO da SAFX42 <> S\);
- Não considerar os itens informativos \(campo 10\-IND\_TP\_REGISTRO da SAFX43 <> 1\);
- Somente operações interestaduais \(campo 13\-COD\_CFO da SAFX43 iniciados com “6” e “7”\)\.

__\[ALTERADA \- MFS\-22066\]__

__Valor a ser totalizado =__ Valor do serviço do item \(campo 19\-VLR\_SERVICO da SAFX43\)\., considerando que serão sumarizados os valores de todos os itens se pelo menos um dos itens estiver com os valores da BC e do ICMS devido à outra UF maiores que “0” \(zero\) \(campos 103\-VLR\_BC\_ICMS\_UF e 104\-VLR\_ICMS\_UF da SAFX43 > 0,00\), ou seja, se no documento fiscal utilities não houver nenhum item que tenha esses campos preenchidos o registro não será considerado na totalização dos valores\.

__Processamento 2 – Gravar dados na tabela:__

Gravar os valores apurados, devendo verificar se existem valores informados manualmente para o período e município apurado, através do item de menu “Geração à Manutenção à Registro 1400”\.

__Campo Tabela:__

__Gravar:__

Estabelecimento

Estabelecimento selecionado na tela de geração\.

Período

Período inicial e final de acordo com mês/ ano preenchido na tela de geração*\. Exemplo: 01/2018 gravar 01/01/2018 a 31/01/2018*\.

Produto

Os campos referentes ao produto serão preenchidos com um caractere branco, pois fazem parte da chave da tabela\.

Município

UF = RS

Código do município apurado agrupado na seleção dos dados\.

Código da Tabela de Itens p/o Índice de Participação dos municípios

03

__*Valores Calculados*__

Valor Apurado

Não se aplica\.

Deduções

Não se aplica\.

__*Valores Conv\. ICMS 52/05*__

Valor Apurado

Soma dos valores apurados por Município\.

Deduções

Não se aplica no momento\.

__*Valores Informados*__

Outros Valores

Não se aplica\.

Outras Deduções

Não se aplica\.

Valor Total

Não se aplica\.

MFS\-16364

RN1400\-BA

__Regra p/ gerar as UF que utilizam a opção “Específica por UF” = BA:__

A geração do 1400 para a modalidade “BA” é feita de acordo com os códigos específicos da Orientação de Preenchimento da SEFAZ\-BA \(Registro\_1400\_Orientação\_Preenchimento\.pdf\)\.

Nesse Convênio iremos tratar o item a seguir descrito na Orientação de Preenchimento:

- Prestação de serviços de Comunicação/Telecomunicação \(item __BAS02__\)\.

As notas fiscais *sem* o ponto de consumo da SAFX42 preenchido não serão processadas, e, portanto, não irão compor o valor adicionado do município em questão\.

__Código BAS02__

__Processamento 1 \- Totalização do Valor das Operações do Período:__

Totalizar o valor do serviço das notas fiscais da SAFX42/SAFX43 que atendam aos seguintes critérios: 

- Selecionar os documentos fiscais utilities do estabelecimento igual informado na tela de geração;
- UF da Inscrição Estadual virtual deve ser a mesma UF do ponto de consumo \(campo 75\-UF\_CONSUMO da SAFX42\), se a UF não estiver preenchida o registro será desconsiderado;
- Município deve ser do ponto de consumo \(campo 76\-COD\_MUNIC\_CONSUMO da SAFX42\), se o município não estiver preenchido o registro será desconsiderado;
- Modelo de comunicação/telecomunicação \(campo 13\-COD\_MODELO da SAFX42 = 21, 22\);
- Data Fiscal \(campo 03\-DAT\_FISCAL da SAFX42\) dentro do período da geração *ou* data extemporânea dentro do período de geração;
- Situação não cancelada \(campo 21\-SITUACAO da SAFX42 <> S\);
- Não considerar os itens informativos \(campo 10\-IND\_TP\_REGISTRO da SAFX43 <> 1\);
- Somente operações interestaduais \(campo 13\-COD\_CFO da SAFX43 iniciados com “6” e “7”\)\.

__\[ALTERADA \- MFS\-22066\]__

__Valor a ser totalizado =__ Valor do serviço do item \(campo 19\-VLR\_SERVICO da SAFX43\)\., considerando que serão sumarizados os valores de todos os itens se pelo menos um dos itens estiver com os valores da BC e do ICMS devido à outra UF maiores que “0” \(zero\) \(campos 103\-VLR\_BC\_ICMS\_UF e 104\-VLR\_ICMS\_UF da SAFX43 > 0,00\), ou seja, se no documento fiscal utilities não houver nenhum item que tenha esses campos preenchidos o registro não será considerado na totalização dos valores\.

__Processamento 2 – Gravar dados na tabela:__

Gravar os valores apurados, devendo verificar se existem valores informados manualmente para o período e município apurado, através do item de menu “Geração à Manutenção à Registro 1400”\.

__Campo Tabela:__

__Gravar:__

Estabelecimento

Estabelecimento selecionado na tela de geração\.

Período

Período inicial e final de acordo com mês/ ano preenchido na tela de geração*\. Exemplo: 01/2018 gravar 01/01/2018 a 31/01/2018*\.

Produto

Os campos referentes ao produto serão preenchidos com um caractere branco, pois fazem parte da chave da tabela\.

Município

UF = BA

Código do município apurado agrupado na seleção dos dados\.

Código da Tabela de Itens p/o Índice de Participação dos municípios

BAS02

__*Valores Calculados*__

Valor Apurado

Não se aplica\.

Deduções

Não se aplica\.

__*Valores Conv\. ICMS 52/05*__

Valor Apurado

Soma dos valores apurados por Município\.

Deduções

Não se aplica no momento\.

__*Valores Informados*__

Outros Valores

Não se aplica\.

Outras Deduções

Não se aplica\.

Valor Total

Não se aplica\.

MFS\-16364

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

