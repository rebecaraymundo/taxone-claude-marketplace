# MTZ_EFD_Pre_Geracao_Registro_E115-Específico RS

- **Fonte:** MTZ_EFD_Pre_Geracao_Registro_E115-Específico RS.docx
- **Modificado:** 2026-03-17
- **Tamanho:** 88 KB

---

THOMSON REUTERS

Pré\-Geração do Registro E115

EFD\-Escrituração Fiscal Digital

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-13074

Julyana Perrucini

Essa MFS tem como objetivo criar a rotina de geração do Registro E115 para alimentar a tabela de Valores Declaratórios\.

CH5484\_2018

\(MFS\-17456\)

João Henrique

Essa MFS tem como objetivo gerar o registro E115 quebrando por CFOP\.

CH16505\_2018 \(MFS\-19588\)

Julyana Perrucini

Essa MFS tem como objetivo ajustar a geração do Anexo V\.A para considerar a redução de base de cálculo à soma dos valores\.

MFS\-23315

Julyana Perrucini

Essa MFS tem como objetivo alterar a geração dos Anexos V\.A e V\.B\.

MFS\-24916

Liliane Assaf

Reestruturação de Menu \(Específico RS\)

MFS\-40746

Liliane Assaf

Inclusão das notas de classificação = 4 \- Conhecimentos Fretes \- SAFX 51, nos Anexos V\.A, V\.B e V\.C

MFS\-57858

Rogério Ohashi

Regra para bloquear pré\-geração de um CFOP para mais de um Código de Informação Adicional, para evitar duplicidade na geração dos Registros E115\.E criar Log de Erro de Geração\.

[MFS\-59693](https://jira.thomsonreuters.com/browse/MFS-59693)

Rogério Ohashi

Alteração na Regra para utilizar o Parâmetro “Considerar campo Código do Benefício” para considerar ou não o Campo 255 – Código do Benefício da Tabela SAFX08 na geração do Registro E115\. Esse ajuste se faz necessário para os clientes que utilizaram esse campo como critério de geração, conforme informação do campo no Manual Layout\.

__MFS\-67999__

Rogério Ohashi

Inclusão de Regra de tratamento para Geração de Estabelecimentos com Inscrição Estadual Única\.

__MFS\-80289__

Rogério Ohashi

Regra para desbloquear a pré\-geração de um CFOP para mais de um Código de Informação Adicional, e correção nas duplicidades na geração do Registros E115\. E criar Log de Erro de Geração\.

__Localização__: Menu Sped, Módulo EFD \- Escrituração Fiscal Digital, item Pré\-Geração à Registro E115 \(Específico RS\)

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN00

__Regra Específica p/ RS:__

__Regras Gerais__

Esta geração foi criada na MFS\-13074 com objetivo de fazer a geração dos dados do Registro E115 para a UF do Rio Grande do Sul \(RS\)\.

Essa geração é especifica para os itens da Tabela 5\.2 \- Informações Adicionais da Apuração \- Valores Declaratórios disponibilizados no site da Receita Federal no Portal do SPED – EFD ICMS/IPI\.

A UF do Rio Grande do Sul \(RS\) está obrigada a entrega deste registro desde 2016, no entanto o módulo só possuía a possibilidade de informar manualmente os registros para geração no arquivo magnético, nem todos os estados estão obrigados e nem todos possuem uma definição para declarar essas informações\.

Como o validador da GIA\-RS teve modificação para entrega do arquivo magnético, que agora é através da EFD e não mais na estrutura da GIA, foram definidos os códigos dos valores declaratórios relacionando\-os ao amparo legal de forma com quê consigamos gerar as informações necessárias via parametrização de CFOP ou CFOP/ Natureza de Operação\.

Trataremos os Anexos I\.C, V\.A, V\.B e V\.C\.

__\[ALTERAÇÃO\-MFS\-67999\]__ __Tratamento p/ Geração por Inscrição Estadual Única\.__

Não terá geração por IEU no momento\.

__*Tratamento:*__

*Foi disponibilizado o Parâmetro “*Geração p/Inscrição Estadual Única” na tela de Pré\-Geração do Registro E115 – Específico RS, para tratamento de* *__*Geração para Estabelecimentos por Inscrição Estadual Única,*__ sendo assim deverá seguir a seguinte regra:

__Se a opção selecionada for__* “*__*Sim”: *__S*erão consideradas as Notas Fiscais de todos os estabelecimentos envolvidos, o centralizador \(estabelecimento selecionado em tela\), e os centralizados \(conforme parametrização do módulo de controle das obrigações estaduais, menu  “Obrigações >  Empresas/Estabelecimentos com Ins\. Estadual Única”\), onde:*

__     __

         Selecionar todas as Notas Fiscais dos Estabelecimentos envolvidos na centralização, identificados a partir do campo “COD\_ESTAB” da tabela “ICP\_INSC\_EST\_CENTR”, do Estabelecimento Centralizador\.

Tabela ICP\_INSC\_EST\_CENTR:

Campo COD\_ESTAB: Estabelecimentos Centralizados;

Campo COD\_ESTAB\_CENTR: Estabelecimento Centralizador\.    

__Se a opção selecionada for* “Não”:  *__Será considerado somente as Notas Fiscais do estabelecimento selecionado em tela\.__                       __

__\[MFS57858\]__ Regra para Bloquear Geração de um CFOP, para códigos adicionais diferentes\.

__\[MFS80289\]__ Regra para Desbloquear Geração de um CFOP, para códigos adicionais diferentes\.

- Verificar se o CFOP está parametrizado para mais de um código adicional para os Anexos V\.A e V\.B

   __     SE __sim __criar__ log de aviso:

__Aviso__: CFOP “XXXX” parametrizado para códigos adicionais diferentes, para o Anexo V\.A ou V\.B, para evitar duplicidades preencher o Campo 255 \- COD\_BENEFICIO da Tabela SAFX08 ou utilizar o Parâmetro de CFOP/Natureza de Operação\. 

__                                 SE__ sim bloquear geração do CFOP\.

__          __Criar log de erro: 

__Aviso__: CFOP “XXXX” parametrizado para códigos adicionais diferentes, para evitar duplicidade utilizar o Parâmetro de CFOP/Natureza de Operação\. 

__Alteração __[__MFS\-59693__](https://jira.thomsonreuters.com/browse/MFS-59693): Criado o parâmetro “Considerar campo de Código do Benefício \- SAFX08 \(campo 255\)” na tela dos Dados Iniciais do Sped Fiscal:

 

    \- Parâmetro desmarcado – A geração do Registro E115 permanecerá conforme regra original, desconsiderando a regra do Campo 255 – Código do Benefício\.

    \- Parâmetro marcado – A geração do Registro E115 passará a considerar o Campo 255 – Código do Benefício da tabela SAFX08, conforme regra abaixo:

\- Campo Código do Benefício \(SAFX08, Campo 255 – COD\_BENEFICIO\):

              __SE__ o Campo 255 – COD\_BENEFICIO da tabela DWT\_ITENS\_MERC estiver preenchido;

                   __E__ o código do benefício estiver cadastrado no módulo EFD\-Escrituração Fiscal Digital >> Informações Adicionais da Apuração \(Registro E115/1925\)\. \(Tabela/Campo do Parâmetro: Tabela EFD\_INF\_ADIC\_APUR, Campo COD\_INF\_ADIC\);

                                            \(*Relacionamento entre as tabelas:  DWT\_ITENS\_MERC\.COD\_BENEFICIO *__*=*__* EFD\_INF\_ADIC\_APUR\.COD\_INF\_ADIC\);*

*                                    *__*Então *__*seguir com a sequência das próximas regras;*

*                            *__Senão __desconsiderar o item na geração do Registro E115\.

MFS\-13074

MFS\-57858

[__MFS\-59693__](https://jira.thomsonreuters.com/browse/MFS-59693)

__MFS\-67999__

RN01

__Critério p/ Recuperação dos Dados – Anexo I\.C__

Origem: SAFX07/08, SAFX2013, TACES51, TACES86, TACES87\.

 

Seleção das notas fiscais \(SAFX07/SAFX08\):

 

- Empresa – empresa do login
- Estabelecimento – estabelecimento da geração
	- No caso de geração por I\.E\.U, se o indicador da “Geração p/ Inscrição Estadual Única” estiver igual a SIM, serão considerados os documentos de todos os estabelecimentos envolvidos na centralização, \(centralizador e centralizados\), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle das Obrigações Estaduais;
- Somente notas fiscais de entrada \(campo MOVTO\_E\_S da SAFX07 <> 9\);
- Data fiscal referente ao período inicial e final preenchido na tela de geração;
- Classificação do documento = ‘1’ ou ‘3’ \(campo COD\_CLASS\_DOC\_FIS da SAFX07\);
- Situação da nota <> S \(campo SITUACAO da SAFX07\);
- Somente notas fiscais com item;
- Somente notas fiscais com CFOP ou CFOP/Natureza de Operação parametrizado no menu “Parâmetros  Registros E115 e 1925  Registro E115”, exceto os CFOP que estiverem cadastrados na TACES51 com o campo Excluída igual a “Não”, pois esses devem ser ignorado da geração;

MFS\-13074

RN02

__Processamento dos Dados – Anexo I\.C__

As informações não serão agrupadas porque o campo sequencial é campo chave na tabela, para cada código parametrizado gravar o registro na tabela\.

Por ser uma pré\-geração, as informações precisam ser alimentadas na tabela Registro E115/1925 \(Valores Declaratórios\) do menu  “Geração  Manutenção  Registro E115/1925 \(Valores Declaratórios\)”\.

__Campo__

__Preenchimento__

Estabelecimento

Será preenchido com o estabelecimento informado na pré\-geração\.

Período

Será preenchido com a Data Inicial e Final informada na pré\-geração\.

Sequencial

Para cada período será gerado uma sequencial dos códigos informados\. *Exemplo:*

RSXXXXXX apuração 01/01/2017 a 31/01/2017 – Seq 1

RSXXXXXX apuração 01/01/2017 a 31/01/2017 – Seq 2 

RSXXXXXX apuração 01/02/2017 a 28/02/2017 – Seq 1

RSXXXXXX apuração 01/02/2017 a 28/02/2017 – Seq 2

Trata\-se apenas de um número sequencial que o usuário deve utilizar para controlar os valores a serem apresentados no registro E115\. O controle deste sequencial pode ser feito por período, reiniciando a numeração a cada novo período\. Esse sequencial não é usado na geração da EFD, ele serve apenas para controle, já que este registro não possui uma chave \(\*\), podendo ser informados vários registros de mesmo código de informação adicional, que poderão ser diferenciados apenas pela descrição complementar\.

\(\*\) de acordo com regras do validador da EFD de Janeiro/2009\.

Código da Informação Adicional

Será preenchida com a informação do código adicional parametrizada por CFOP ou CFOP/ Natureza de Operação desse Anexo\.

Valor da Informação Adicional

__\[MFS80289\] __Correção na duplicidade quando parametrizado um CFOP para mais de um código de informação adicional

Será preenchido com a soma dos valores de acordo com os campos informados em Recuperar Motivo da TACES87 e CFOP relacionados na TACES86 para as notas fiscais que foram recuperadas\.

__Tratamentos:__

__Se __o código for igual à RS013001, verificar se o campo B\. Isenta ICMSS \(campo BASE\_ICMSS e TRIB\_ICMSS = 2 da SAFX08\)  __ou__ B\. Isenta ICMS \(campo BASE\_ICMS e TRIB\_ICMS = 2 da SAFX08\) é maior que zero, __se sim, __recuperar o Campo 52 \- VLR\_SUBST\_ICMS __ou__ o Campo 133 \- VLR\_ICMSS\_NDESTAC __ou __o__ __Campo 145 \- VLR\_ICMSS\_N\_ESCRIT da tabela SAFX08, caso contrário desconsiderar registros\.

__Se __o código for igual à RS013091, verificar se o campo B\. Outras ICMSS \(campo BASE\_ICMSS e TRIB\_ICMSS = 3 da SAFX08\)  __ou__ B\. Outras ICMS \(campo BASE\_ICMS e TRIB\_ICMS = 3 da SAFX08\) é maior que zero, __se sim, __recuperar o Campo 52 \- VLR\_SUBST\_ICMS __ou__ o Campo 133 \- VLR\_ICMSS\_NDESTAC __ou __o__ __Campo 145 \- VLR\_ICMSS\_N\_ESCRIT da tabela SAFX08, caso contrário desconsiderar registros\.

Códigos iguais a RS013001, RS013091 deverão recuperar os valores informados no campo Recuperar Motivo da TACES87 quando o campo Código de Ajuste for igual a 001;

__*Regra:*__

- <a id="OLE_LINK141"></a><a id="OLE_LINK142"></a>Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 1, <a id="OLE_LINK154"></a><a id="OLE_LINK155"></a><a id="OLE_LINK156"></a>verificar se o campo Vlr ICMSS <a id="OLE_LINK143"></a><a id="OLE_LINK144"></a><a id="OLE_LINK145"></a><a id="OLE_LINK146"></a>do item da nota fiscal \(campo VLR\_SUBST\_ICMS da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.
- <a id="OLE_LINK151"></a><a id="OLE_LINK152"></a><a id="OLE_LINK153"></a>Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 2, verificar se o campo Vlr ICMSS do item da nota fiscal \(campo VLR\_SUBST\_ICMS da SAFX08\), <a id="OLE_LINK157"></a><a id="OLE_LINK158"></a><a id="OLE_LINK159"></a>B\. Isenta ICMSS do item da nota fiscal \(campo <a id="OLE_LINK147"></a><a id="OLE_LINK148"></a><a id="OLE_LINK149"></a><a id="OLE_LINK150"></a>BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 2 da SAFX08\) __ou__ B<a id="OLE_LINK166"></a><a id="OLE_LINK167"></a><a id="OLE_LINK168"></a><a id="OLE_LINK169"></a>\. Outras ICMSS do item da nota fiscal \(campo BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 3 da SAFX08\) <a id="OLE_LINK160"></a><a id="OLE_LINK161"></a><a id="OLE_LINK162"></a>são maiores que zero, caso contrário desconsiderar registros\.
- <a id="OLE_LINK163"></a><a id="OLE_LINK164"></a><a id="OLE_LINK165"></a>Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 3, verificar se o campo B\. Isenta ICMSS do item da nota fiscal \(campo BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 2 da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.
- <a id="OLE_LINK170"></a><a id="OLE_LINK171"></a>Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 4, verificar se o campo B\. Outras ICMSS do item da nota fiscal \(campo BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 3 da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.

__Se __o código for igual à RS013002, verificar se o campo B\. Isenta IPI do item da nota fiscal \(campo BASE\_IPI e TRIB\_IPI = 2 da SAFX08\) é maior que zero, __se sim, __recuperar o Campo 48 \- VLR\_IPI __ou__ o Campo 81 \- VLR\_IPI\_NDESTAC da tabela SAFX08, caso contrário desconsiderar registros\.

__Se __o código for igual à RS013092, verificar se o campo B\. Outras IPI do item da nota fiscal \(campo BASE\_IPI e TRIB\_IPI = 3 da SAFX08\) é maior que zero, __se sim, __recuperar o Campo 48 \- VLR\_IPI __ou__ o Campo 81 \- VLR\_IPI\_NDESTAC da tabela SAFX08, caso contrário desconsiderar registros\.

Códigos iguais a RS013002 e RS013092 deverão recuperar os valores informados no campo Recuperar Motivo da TACES87 quando o campo Código de Ajuste for igual a 002;

__*Regra:*__

- <a id="OLE_LINK172"></a><a id="OLE_LINK173"></a><a id="OLE_LINK178"></a><a id="OLE_LINK179"></a><a id="OLE_LINK180"></a><a id="OLE_LINK181"></a>Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 1, verificar se o campo Vlr IPI do item da nota fiscal \(campo VLR\_IPI da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.
- <a id="OLE_LINK176"></a><a id="OLE_LINK177"></a>Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 2, verificar se o campo Vlr IPI do item da nota fiscal \(campo VLR\_IPI\), B\. Isenta IPI <a id="OLE_LINK174"></a><a id="OLE_LINK175"></a>\(campo BASE\_IPI e TRIB\_IPI = 2 da SAFX08\) ou B\. Outras IPI \(campo BASE\_IPI e TRIB\_IPI = 3 da SAFX08\) são maiores que zero, caso contrário desconsiderar registros\.
- Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 3, verificar se o campo B\. Isenta IPI \(campo BASE\_IPI e TRIB\_IPI = 2 da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.
- Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 4, verificar se o campo B\. Outras IPI \(campo BASE\_IPI e TRIB\_IPI = 3 da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.

Código igual a RS013003 deverão recuperar os valores informados no campo Recuperar Motivo da TACES87 quando o campo Código de Ajuste for igual a 003;

Regra:

- Se o CFOP com Código de Ajuste igual a 003 e campo Recuperar Motivo da TACES87 igual a 1, verificar se o campo <a id="OLE_LINK182"></a><a id="OLE_LINK183"></a><a id="OLE_LINK184"></a><a id="OLE_LINK185"></a><a id="OLE_LINK186"></a>Vlr Frete do item da nota fiscal \(campo VLR\_FRETE da SAFX08\) é maior que zero e o produto cadastrado no item da nota fiscal é classificado como Material \(Uso ou Consumo\) ou Ativo Imobilizado \(campo CLAS\_ITEM igual a 07 ou 08 da SAFX2013\), caso contrário desconsiderar registros\.
- <a id="OLE_LINK189"></a><a id="OLE_LINK190"></a><a id="OLE_LINK191"></a><a id="OLE_LINK187"></a><a id="OLE_LINK188"></a>Se o CFOP com Código de Ajuste igual a 003 e campo Recuperar Motivo da TACES87 igual a 2, verificar se o campo Vlr Frete do item da nota fiscal \(campo VLR\_FRETE da SAFX08\) <a id="OLE_LINK201"></a><a id="OLE_LINK202"></a>é maior que zero, caso contrário desconsiderar registros\.

*Observação:* O código RS013006 referente ao Motivo 6 não era tratado na GIA e também não será tratado na EFD, esse campo será bloqueado no momento da parametrização\.

Descrição Complementar

Será preenchida com os CFOP que foram parametrizados por CFOP ou CFOP/ Natureza de Operação sem separador ou espaços\. *Exemplo:*

110112011602

__CH\_5484\_2018 \(MFS\-17456\):__ Será preenchido com quebra por CFOP ou CFOP/Natureza de Operação no registro E115\.

Exemplo: 

E115| RS000000|0000,00|5405

E115| RS000000|0000,00|5927

E115| RS000000|0000,00|6411

Sub\-Apuração do Sped Fiscal

Não será preenchido porque a UF do RS não possui sub\-apuração\.

Usuário

Gravar o usuário que efetuou a pré\-geração desse Registro\.

Data Operação

Gravar com a data que foi efetuada a pré\-geração desse Registro\.

MFS\-13074

CH\_5484\_2018 \(MFS\-17456\)

RN03

__Critério p/ Recuperação dos Dados – Anexo V\.A__

__\[ALTERADA – MFS\-23315\]__

__\[__MFS\-40746: inclusão da classificação do documento = ‘4’\]

Origem: SAFX07/08/09, TACES51\.

 

Seleção das notas fiscais \(SAFX07/SAFX08/SAFX09\):

 

- Empresa – empresa do login
- Estabelecimento – estabelecimento da geração
	- No caso de geração por I\.E\.U, se o indicador da “Geração p/ Inscrição Estadual Única” estiver igual a SIM, serão considerados os documentos de todos os estabelecimentos envolvidos na centralização, \(centralizador e centralizados\), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle das Obrigações Estaduais;
- Somente notas fiscais de saída \(campo MOVTO\_E\_S da SAFX07 = 9\);
- Data fiscal referente ao período inicial e final preenchido na tela de geração;
- Classificação do documento = ‘1’ ou ‘3’ ou ‘4’ \(campo COD\_CLASS\_DOC\_FIS da SAFX07\);
- Situação da nota <> S \(campo SITUACAO da SAFX07\);
- Somente notas fiscais com item;
- Somente notas fiscais com CFOP ou CFOP/Natureza de Operação parametrizado no menu “Parâmetros  Registros E115 e 1925  Registro E115”, exceto os CFOP que estiverem cadastrados na TACES51 com o campo Isentas igual a “Não”, pois esses devem ser ignorados da geração;

*Atenção: *Notas fiscais sem item deverão ser considerados os conteúdos informados na capa\.

MFS\-13074

MFS\-23315

RN04

__Processamento dos Dados – Anexo V\.A__

As informações não serão agrupadas porque o campo sequencial é campo chave na tabela, para cada código parametrizado gravar o registro na tabela\.

Por ser uma pré\-geração, as informações precisam ser alimentadas na tabela Registro E115/1925 \(Valores Declaratórios\) do menu  “Geração  Manutenção  Registro E115/1925 \(Valores Declaratórios\)”\.

__Campo__

__Preenchimento__

Estabelecimento

Será preenchido com o estabelecimento informado na pré\-geração\.

Período

Será preenchido com a Data Inicial e Final informada na pré\-geração\.

Sequencial

Para cada período será gerado uma sequencial dos códigos informados\. *Exemplo:*

RSXXXXXX apuração 01/01/2017 a 31/01/2017 – Seq 1

RSXXXXXX apuração 01/01/2017 a 31/01/2017 – Seq 2 

RSXXXXXX apuração 01/02/2017 a 28/02/2017 – Seq 1

RSXXXXXX apuração 01/02/2017 a 28/02/2017 – Seq 2

Trata\-se apenas de um número sequencial que o usuário deve utilizar para controlar os valores a serem apresentados no registro E115\. O controle deste sequencial pode ser feito por período, reiniciando a numeração a cada novo período\. Esse sequencial não é usado na geração da EFD, ele serve apenas para controle, já que este registro não possui uma chave \(\*\), podendo ser informado vários registros de mesmo código de informação adicional, que poderão ser diferenciados apenas pela descrição complementar\.

\(\*\) de acordo com regras do validador da EFD de Janeiro/2009\.

Código da Informação Adicional

Será preenchida com a informação do código adicional parametrizada por CFOP ou CFOP/ Natureza de Operação desse Anexo\.

Valor da Informação Adicional

__\[ALTERADA \- CH16505\_2018 \(MFS\-19588\)\]__

__\[MFS80289\] __Correção na duplicidade quando parametrizado um CFOP para mais de um código de informação adicional

__Comparar __o “*Código Informação Adicional*” parametrizado na tela “*Parâmetros por CFOP \- Informações Adicionais de Apuração \- Registro E115 \(Específico RS\)*” com o Campo 255 \- COD\_BENEFICIO da tabela SAFX08\.

Regras de validação:

\- Campo COD\_CFO da tabela SAFX08 \(campo ident\_cfo da tabela dwt\_itens\_merc\) igual ao Campo COD\_CFO da Tabela EFD\_PAR\_CFO\_E115;

\- Campo COD\_BENEFICIO da Tabela DWT\_ITENS\_MERC igual ao Campo COD\_INF\_ADIC da Tabela EFD\_PAR\_CFO\_E115\.

__    Preencher__ com a soma do conteúdo informado no campo B\. Isenta ICMS e no campo B\. Redução ICMS do item da nota fiscal \(SAFX08\) de acordo com as notas fiscais que foram recuperadas, \(o valor da B\. Redução ICMS só será considerado se o campo Sit\. Tributária B igual a “20”\)\.

__Ou__

__Se__ o Campo 255 \- COD\_BENEFICIO da tabela SAFX08, não estiver preenchida:

__   E se__ o CFOP estiver parametrizado para um código de informação adicional

__Preencher__ com a soma do conteúdo informado no campo B\. Isenta ICMS e no campo B\. Redução ICMS do item da nota fiscal \(SAFX08/09\) de acordo com as notas fiscais que foram recuperadas, em caso de notas fiscais sem item recuperar o conteúdo informado no campo B\. Isenta ICMS e no campo B\. Redução ICMS da capa da nota fiscal \(SAFX07\)\. O valor da B\. Redução ICMS só será considerado se o campo Sit\. Tributária B igual a “20”; 

__Senão__

__Se__ o CFOP estiver parametrizado para mais de um Código Informação Adicional, bloquear a geração e criar a Mensagem de Erro abaixo:

__Mensagem de Erro:__ *O CFOPXXXX está parametrizado para mais de um Código de Informação Adicional\. O registro foi gerado com duplicidades e não será considerado no arquivo, favor preencher o Campo 255 \- COD\_BENEFICIO da tabela SAFX08 ou utilizar o Parâmetro de CFOP/Natureza de Operação\. *

* *

Será preenchido com a soma do conteúdo informado no campo B\. Isenta ICMS e no campo B\. Redução ICMS do item da nota fiscal \(SAFX08/09\) de acordo com as notas fiscais que foram recuperadas, em caso de notas fiscais sem item recuperar o conteúdo informado no campo B\. Isenta ICMS e no campo B\. Redução ICMS da capa da nota fiscal \(SAFX07\)\. O valor da B\. Redução ICMS só será considerado se o campo Sit\. Tributária B igual a “20”\.:

 

Descrição Complementar

Será preenchida com os CFOP que foram parametrizados por CFOP ou CFOP/ Natureza de Operação sem separador ou espaços\. *Exemplo:*

110112011602

__CH\_5484\_2018 \(MFS\-17456\):__ Será preenchido com quebra por CFOP ou CFOP/Natureza de Operação no registro E115\.

Exemplo: 

E115| RS000000|0000,00|5405

E115| RS000000|0000,00|5927

E115| RS000000|0000,00|6411

Sub\-Apuração do Sped Fiscal

Não será preenchido porque a UF do RS não possui sub\-apuração\.

Usuário

Gravar o usuário que efetuou a pré\-geração desse Registro\.

Data Operação

Gravar com a data que foi efetuada a pré\-geração desse Registro\.

MFS\-13074

CH\_5484\_2018 \(MFS\-17456\)

MFS\-23315

RN05

__Critério p/ Recuperação dos Dados – Anexo V\.B__

__\[ALTERADA – MFS\-23315\]__

__\[__MFS\-40746: inclusão da classificação do documento = ‘4’\]

Origem: SAFX07/08/09, TACES51\.

 

Seleção das notas fiscais \(SAFX07/SAFX08/SAFX09\):

 

- Empresa – empresa do login
- Estabelecimento – estabelecimento da geração
	- No caso de geração por I\.E\.U, se o indicador da “Geração p/ Inscrição Estadual Única” estiver igual a SIM, serão considerados os documentos de todos os estabelecimentos envolvidos na centralização, \(centralizador e centralizados\), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle das Obrigações Estaduais;
- Somente notas fiscais de saída \(campo MOVTO\_E\_S da SAFX07 = 9\);
- Data fiscal referente ao período inicial e final preenchido na tela de geração;
- Classificação do documento = ‘1’ ou ‘3’ ou ‘4’ \(campo COD\_CLASS\_DOC\_FIS da SAFX07\);
- Situação da nota <> S \(campo SITUACAO da SAFX07\);
- Somente notas fiscais com item;
- Somente notas fiscais com CFOP ou CFOP/Natureza de Operação parametrizado no menu “Parâmetros  Registros E115 e 1925  Registro E115”, exceto os CFOP que estiverem cadastrados na TACES51 com o campo Outras igual a “Não”, pois esses devem ser ignorados da geração;

*Atenção: *Notas fiscais sem item deverão ser considerados os conteúdos informados na capa\.

MFS\-13074

MFS\-23315

RN06

__Processamento dos Dados – Anexo V\.B__

As informações não serão agrupadas porque o campo sequencial é campo chave na tabela, para cada código parametrizado gravar o registro na tabela\.

Por ser uma pré\-geração, as informações precisam ser alimentadas na tabela Registro E115/1925 \(Valores Declaratórios\) do menu  “Geração  Manutenção  Registro E115/1925 \(Valores Declaratórios\)”\.

__Campo__

__Preenchimento__

Estabelecimento

Será preenchido com o estabelecimento informado na pré\-geração\.

Período

Será preenchido com a Data Inicial e Final informada na pré\-geração\.

Sequencial

Para cada período será gerado uma sequencial dos códigos informados\. *Exemplo:*

RSXXXXXX apuração 01/01/2017 a 31/01/2017 – Seq 1

RSXXXXXX apuração 01/01/2017 a 31/01/2017 – Seq 2 

RSXXXXXX apuração 01/02/2017 a 28/02/2017 – Seq 1

RSXXXXXX apuração 01/02/2017 a 28/02/2017 – Seq 2

Trata\-se apenas de um número sequencial para controlar os valores a serem apresentados Trata\-se apenas de um número sequencial que o usuário deve utilizar para controlar os valores a serem apresentados no registro E115\. O controle deste sequencial pode ser feito por período, reiniciando a numeração a cada novo período\. Esse sequencial não é usado na geração da EFD, ele serve apenas para controle, já que este registro não possui uma chave \(\*\), podendo ser informado vários registros de mesmo código de informação adicional, que poderão ser diferenciados apenas pela descrição complementar\.

\(\*\) de acordo com regras do validador da EFD de Janeiro/2009\.

Código da Informação Adicional

Será preenchida com a informação do código adicional parametrizada por CFOP ou CFOP/ Natureza de Operação desse Anexo\.

Valor da Informação Adicional

__\[ALTERADA – MFS\-23315\]__

__\[MFS80289\] __Correção na duplicidade quando parametrizado um CFOP para mais de um código de informação adicional

__Comparar __o “*Código Informação Adicional*” parametrizado na tela “*Parâmetros por CFOP \- Informações Adicionais de Apuração \- Registro E115 \(Específico RS\)*” com o Campo 255 \- COD\_BENEFICIO da tabela SAFX08\.

Regras de validação:

\- Campo COD\_CFO da Tabela EFD\_PAR\_CFO\_E115 igual ao Campo COD\_CFO da tabela SAFX08 \(campo ident\_cfo da tabela dwt\_itens\_merc\);

\- Campo COD\_BENEFICIO da Tabela DWT\_ITENS\_MERC igual ao Campo COD\_INF\_ADIC da Tabela EFD\_PAR\_CFO\_E115\.

__Preencher__ com a soma do conteúdo informado no campo B\. Outras ICMS do item da nota fiscal \(SAFX08/09\) de acordo com as notas fiscais que foram recuperadas\.

__Ou__

__Se__ o Campo 255 \- COD\_BENEFICIO da tabela SAFX08, não estiver preenchida:

  __E se__ o CFOP estiver parametrizado para um código de informação adicional

__Preencher__ com a soma do conteúdo informado no campo B\. Outras ICMS do item da nota fiscal \(SAFX08/09\) de acordo com as notas fiscais que foram recuperadas, em caso de notas fiscais sem item recuperar o conteúdo informado no campo B\. Outras ICMS da capa da nota fiscal \(SAFX07\)\.

__Senão__

__Se__ o CFOP estiver parametrizado para mais de um Código Informação Adicional, bloquear a geração e criar a Mensagem de Erro abaixo:

__Mensagem de Erro:__ *O CFOPXXXX está parametrizado para mais de um Código de Informação Adicional\. O registro foi gerado com duplicidades e não será considerado no arquivo, favor preencher o Campo 255 \- COD\_BENEFICIO da tabela SAFX08 ou utilizar o Parâmetro de CFOP/Natureza de Operação\. *

Será preenchido com a soma do conteúdo informado no campo B\. Outras ICMS do item da nota fiscal \(SAFX08/09\) de acordo com as notas fiscais que foram recuperadas, em caso de notas fiscais sem item recuperar o conteúdo informado no campo B\. Outras ICMS da capa da nota fiscal \(SAFX07\)\.

Descrição Complementar

Será preenchida com os CFOP que foram parametrizados por CFOP ou CFOP/ Natureza de Operação sem separador ou espaços\. *Exemplo:*

110112011602

__CH\_5484\_2018 \(MFS\-17456\):__ Será preenchido com quebra por CFOP ou CFOP/Natureza de Operação no registro E115\.

Exemplo: 

E115| RS000000|0000,00|5405

E115| RS000000|0000,00|5927

E115| RS000000|0000,00|6411

Sub\-Apuração do Sped Fiscal

Não será preenchido porque a UF do RS não possui sub\-apuração\.

Usuário

Gravar o usuário que efetuou a pré\-geração desse Registro\.

Data Operação

Gravar com a data que foi efetuada a pré\-geração desse Registro\.

MFS\-13074

CH\_5484\_2018 \(MFS\-17456\)

MFS\-23315

RN07

__Critério p/ Recuperação dos Dados – Anexo V\.C__

__\[__MFS\-40746: inclusão da classificação do documento = ‘4’\]

Origem: SAFX07/08, SAFX2013, TACES51, TACES86, TACES87\.

 

Seleção das notas fiscais \(SAFX07/SAFX08\):

 

- Empresa – empresa do login
- Estabelecimento – estabelecimento da geração
	- No caso de geração por I\.E\.U, se o indicador da “Geração p/ Inscrição Estadual Única” estiver igual a SIM, serão considerados os documentos de todos os estabelecimentos envolvidos na centralização, \(centralizador e centralizados\), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle das Obrigações Estaduais;
- Somente notas fiscais de saída \(campo MOVTO\_E\_S da SAFX07 = 9\);
- Data fiscal referente ao período inicial e final preenchido na tela de geração;
- Classificação do documento = ‘1’ ou ‘3’ ou ‘4’ \(campo COD\_CLASS\_DOC\_FIS da SAFX07\);
- Situação da nota <> S \(campo SITUACAO da SAFX07\);
- Somente notas fiscais com item;
- Somente notas fiscais com CFOP ou CFOP/Natureza de Operação parametrizado no menu “Parâmetros  Registros E115 e 1925  Registro E115”, exceto os CFOP que estiverem cadastrados na TACES51 com o campo Excluída igual a “Não”, pois esses devem ser ignorado da geração;

MFS\-13074

RN08

__Processamento dos Dados – Anexo V\.C__

As informações não serão agrupadas porque o campo sequencial é campo chave na tabela, para cada código parametrizado gravar o registro na tabela\.

Por ser uma pré\-geração, as informações precisam ser alimentadas na tabela Registro E115/1925 \(Valores Declaratórios\) do menu  “Geração  Manutenção  Registro E115/1925 \(Valores Declaratórios\)”\.

__Campo__

__Preenchimento__

Estabelecimento

Será preenchido com o estabelecimento informado na pré\-geração\.

Período

Será preenchido com a Data Inicial e Final informada na pré\-geração\.

Sequencial

Para cada período será gerado uma sequencial dos códigos informados\. *Exemplo:*

RSXXXXXX apuração 01/01/2017 a 31/01/2017 – Seq 1

RSXXXXXX apuração 01/01/2017 a 31/01/2017 – Seq 2 

RSXXXXXX apuração 01/02/2017 a 28/02/2017 – Seq 1

RSXXXXXX apuração 01/02/2017 a 28/02/2017 – Seq 2

Trata\-se apenas de um número sequencial que o usuário deve utilizar para controlar os valores a serem apresentados no registro E115\. O controle deste sequencial pode ser feito por período, reiniciando a numeração a cada novo período\. Esse sequencial não é usado na geração da EFD, ele serve apenas para controle, já que este registro não possui uma chave \(\*\), podendo ser informado vários registros de mesmo código de informação adicional, que poderão ser diferenciados apenas pela descrição complementar\.

\(\*\) de acordo com regras do validador da EFD de Janeiro/2009\.

Código da Informação Adicional

Será preenchida com a informação do código adicional parametrizada por CFOP ou CFOP/ Natureza de Operação desse Anexo\.

Valor da Informação Adicional

__\[MFS80289\] __Correção na duplicidade quando parametrizado um CFOP para mais de um código de informação adicional

Será preenchido com a soma dos valores de acordo com os campos informados em Recuperar Motivo da TACES87 e CFOP relacionados na TACES86 para as notas fiscais que foram recuperadas\.

__Tratamentos:__

__Se __o código for igual à RS053001, verificar se o campo B\. Isenta ICMSS \(campo BASE\_ICMSS e TRIB\_ICMSS = 2 da SAFX08\)  __ou__ B\. Isenta ICMS \(campo BASE\_ICMS e TRIB\_ICMS = 2 da SAFX08\) do item da nota fiscal é maior que zero, __se sim, __recuperar o Campo 52 \- VLR\_SUBST\_ICMS __ou__ o Campo 133 \- VLR\_ICMSS\_NDESTAC __ou o __Campo 145 \- VLR\_ICMSS\_N\_ESCRIT da tabela SAFX08, caso contrário desconsiderar registros\.

__Se __o código for igual à RS053091, verificar se o campo B\. Outras ICMSS \(campo BASE\_ICMSS e TRIB\_ICMSS = 3 da SAFX08\)  __ou __campo B\. Outras ICMS \(campo BASE\_ICMS e TRIB\_ICMS = 3 da SAFX08\) do item da nota fiscal é maior que zero, __se sim, __recuperar o Campo 52 \- VLR\_SUBST\_ICMS __ou__ o Campo 133 \- VLR\_ICMSS\_NDESTAC __ou o __Campo 145 \- VLR\_ICMSS\_N\_ESCRIT da tabela SAFX08, caso contrário desconsiderar registros\.

Códigos iguais a RS053001, RS053091 deverão recuperar os valores informados no campo Recuperar Motivo da TACES87 quando o campo Código de Ajuste for igual a 001;

__*Regra:*__

- Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 1, verificar se o campo Vlr ICMSS do item da nota fiscal \(campo VLR\_SUBST\_ICMS da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.
- Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 2, verificar se o campo Vlr ICMSS do item da nota fiscal \(campo VLR\_SUBST\_ICMS da SAFX08\), B\. Isenta ICMSS do item da nota fiscal \(campo BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 2 da SAFX08\) ou B\. Outras ICMSS do item da nota fiscal \(campo BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 3 da SAFX08\) são maiores que zero, caso contrário desconsiderar registros\.
- Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 3, verificar se o campo B\. Isenta ICMSS do item da nota fiscal \(campo BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 2 da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.
- Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 4, verificar se o campo B\. Outras ICMSS do item da nota fiscal \(campo BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 3 da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.

__Se __o código for igual à RS053002, verificar se o campo B\. Isenta IPI do item da nota fiscal \(campo BASE\_IPI e TRIB\_IPI = 2 da SAFX08\) é maior que zero, se __sim, __recuperar o Campo 48 \- VLR\_IPI __ou__ o Campo 81 \- VLR\_IPI\_NDESTAC da tabela SAFX08, caso contrário desconsiderar registros\.

__Se __o código for igual à RS053092, verificar se o campo B\. Outras IPI do item da nota fiscal \(campo BASE\_IPI e TRIB\_IPI = 3 da SAFX08\) é maior que zero, se __sim, __recuperar o Campo 48 \- VLR\_IPI __ou__ o Campo 81 \- VLR\_IPI\_NDESTAC da tabela SAFX08, caso contrário desconsiderar registros\.

Códigos iguais a RS053002 e RS053092 deverão recuperar os valores informados no campo Recuperar Motivo da TACES87 quando o campo Código de Ajuste for igual a 002;

__*Regra:*__

- Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 1, verificar se o campo Vlr IPI do item da nota fiscal \(campo VLR\_IPI da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.
- Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 2, verificar se o campo Vlr IPI do item da nota fiscal \(campo VLR\_IPI\), B\. Isenta IPI \(campo BASE\_IPI e TRIB\_IPI = 2 da SAFX08\) ou B\. Outras IPI \(campo BASE\_IPI e TRIB\_IPI = 3 da SAFX08\) são maiores que zero, caso contrário desconsiderar registros\.
- Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 3, verificar se o campo B\. Isenta IPI \(campo BASE\_IPI e TRIB\_IPI = 2 da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.
- Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 4, verificar se o campo B\. Outras IPI \(campo BASE\_IPI e TRIB\_IPI = 3 da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.

*Observação:* O código RS053006 referente ao Motivo 6 não era tratado na GIA e também não será tratado na EFD, esse campo será bloqueado no momento da parametrização\.

Descrição Complementar

Será preenchida com os CFOP que foram parametrizados por CFOP ou CFOP/ Natureza de Operação sem separador ou espaços\. *Exemplo:*

110112011602

__CH\_5484\_2018 \(MFS\-17456\):__ Será preenchido com quebra por CFOP ou CFOP/Natureza de Operação no registro E115\.

Exemplo: 

E115| RS000000|0000,00|5405

E115| RS000000|0000,00|5927

E115| RS000000|0000,00|6411

Sub\-Apuração do Sped Fiscal

Não será preenchido porque a UF do RS não possui sub\-apuração\.

Usuário

Gravar o usuário que efetuou a pré\-geração desse Registro\.

Data Operação

Gravar com a data que foi efetuada a pré\-geração desse Registro\.

MFS\-13074

__CH\_5484\_2018 \(MFS\-17456\):__

	

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

