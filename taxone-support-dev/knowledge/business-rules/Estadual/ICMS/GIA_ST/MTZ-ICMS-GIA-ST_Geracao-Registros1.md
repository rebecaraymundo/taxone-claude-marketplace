# MTZ-ICMS-GIA-ST_Geracao-Registros1

- **Fonte:** MTZ-ICMS-GIA-ST_Geracao-Registros1.docx
- **Modificado:** 2026-03-04
- **Tamanho:** 108 KB

---

# Módulo Estadual \- ICMS \- Geração da GIA\-ST

__Localização__: Menu Estadual, Módulo ICMS, item de menu Apuração à Guias de Recolhimento à Guia de Informação de Substituição Tributária à Geração

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__CH72922\-A__

Considerar parâmetro 67 na geração da GIA\-ST

Considerar parâmetro 67 na geração da GIA\-ST 

__OS3298__

Alteração da GIA\-ST e GNRE para considerar o valor dos lançamentos complementares\.

A geração da GIA\-ST e da GNRE foi alterada para possibilitar que o valor dos lançamentos complementares sejam utilizados, a partir de um novo parâmetro definido pelo usuário\. 

__MFS2283__

Alteração da GIA\-ST Versão 3\.1

Este documento tem como objetivo atualizar a GIA\-ST de acordo com Versão 3\.1 do layout disponibilizado pela SEFAZ do RS\.

__CH2215\_2016__

Tratamento para GIA\-ST Versão 3\.1 em casos de DIFAL

Este documento tem como objetivo tratar a geração dos registros quando houver apenas valores de diferencial de alíquota a declarar\.

__CH7697\_2016__

Alteração do preenchimento do campo “Valor do ICMS Devido” do A4

Este documento tem como objetivo alterar o preenchimento do campo “Valor do ICMS Devido” do Anexo IV – EC 87/15\.

__MFS3854__

Alteração da GIA\-ST em atendimento as empresas de energia elétrica

Esse documento tem como objetivo alterar a obrigação acessória Guia de Informações de Substituição Tributária \(GIA\-ST\) para contemplar a geração por Inscrição Estadual Única e atender empresas de energia elétrica\.

__CH12151\_2016__

Alteração das Devoluções ou Anulações EC 87/15

Este documento tem como objetivo alterar a recuperação das informações relativas às Devoluções ou Anulações da Emenda Constitucional 87/15 do Anexo Principal\.

__MFS4524__

Alteração para recuperação das informações relativas à EC 87/15 a partir do módulo PIM

Este documento tem como objetivo incluir a opção de gerar as informações dos Lançamentos Complementares da Apuração do ICMS Dif\. Alíquota UF Origem/Destino \(EC 87/15\) relativas à Emenda Constitucional nº 87/2015, do módulo Específicos – PIM \- Gestão do Controle de Incentivos Fiscais do Polo Industrial de Manaus\.

__CH21316\_2016__

Alteração da origem de informação no preenchimento do campo Valor ICMS Devido à UF de Destino

Este documento tem como objetivo alterar a origem de informação para o preenchimento do campo Valor ICMS Devido à UF de Destino através das operações de saídas\.

__CH8957\_2017__

__\(MFS11377\)__

Alteração na guia de informação de Substituição tributária \(Anexo I\)\.

Esse documento tem como objetivo alterar a aba Anexo I \(Devoluções\) da GIA\-ST\. Caso o campo do convênio 132/92 não esteja preenchido, o sistema deverá preencher com o campo do convênio 51/00 no campo Vlr\. ICMS\-ST Devolução\.

__MFS10606__

Alteração na geração dos vencimentos

Preenchimento do Valor a Recolher p/ Vencimento Único\.

__MFS27837__

Alteração na geração do Valor ICMS devido à UF de Destino

Este documento tem como objetivo alterar a geração do Valor ICMS devido à UF de Destino para o estado igual a “RJ”\.

__MFS28188__

Alteração na geração do Valor ICMS ST FCP

Automatização do campo Valor do ICMS\-ST FCP da GIA ST

__MFS29475__

Alteração na geração do Valor ICMS ST FCP

Inclusão do filtro do código da obrigação na geração automática do Valor do ICMS\-ST FCP

__MFS30017__

Alteração na geração do Valor de Devoluções ou Anulações

Inclusão do valor do saldo credor do mês anterior no cálculo do valor de Devoluções ou Anulações

__MFS69213__

Tratamento para considerar o parâmetro “Complemento de ICMS\-ST \(Anexo II\)

Inclusão de Regra p/ considerar as Notas Fiscais complementares com Complemento de ICMS\-ST de Terceiros e Aquisições de Simples Nacional\.

__MFS69962__

Alteração na geração do Total ICMS FCP

Alteração da geração do Total ICMS FCP da EC 87/15 para o estado igual a “RJ”\.

__MFS35443__

Preenchimento do Anexo IV da GIA ST através da GNRE Online\.

Estão sendo alterados a geração do Anexo IV e do campo “Total ICMS FCP” \(RN35\) da aba “Principal” para passar a ler a guia da GNRE Online, além da Guia dos Lançamentos Complementares já atualmente considerada\. A regra RN31 do campo “Total ICMS Devido à UF de Destino” da aba “Principal” não está sendo modificada por enquanto, pois hoje não parte da leitura das Guias do Lançamentos Complementares, e o nosso foco foi alterar apenas as regras com origem nas Guias\. Pode ser objeto de futura modificação, caso haja necessidade de compatibilizar o somatório do “Valor do ICMS Devido” do Anexo IV com o campo “Total ICMS Devido à UF de Destino” da aba “Principal”\.

__MFS91049__

Inclusão de parâmetro “Geração do Anexo IV \(EC87/15\)”

Tratamento para o sistema considerar o parâmetro “Geração do Anexo IV \(EC87/15\)” para o sistema gerar somente o Anexo IV, referente aos Registros EC87/15\.  

__MFS91970__

Inclusão de parâmetro “Retirar o valor de FECP do ICMS\-ST”

Tratamento para o sistema considerar o parâmetro “Retirar o valor de FECP do ICMS\-ST” para o sistema gravar o valor de ICMS\-ST\.

__MFS94270__

Tratamento na geração dos Registros quando utilizado o parâmetro “Geração do Anexo IV \(EC87/15\)”\.

Tratamento para o sistema considerar o parâmetro “Considerar UF p/ Geração do EC87/15 \(Anexo IV\)” na tela de “Parâmetro por UF Favorecida” para o sistema gerar somente o Anexo IV, referente aos Registros EC87/15, por UF\.

__MFS536852__

Andréa Rocha

Alteração do cálculo do valor de Devoluções ou Anulações referente ao EC 87/15, para passar a considerar o valor do FCP das notas de devoluções para calcular o valor\.

__MFS564378__

Andréa Rocha

Alteração da regra de geração dos campos Data de Vencto do ICMS Devido e Valor do ICMS Devido do Anexo IV – EC87/15\.

__MFS569593__

Andréa Rocha

Alteração da regra de geração dos campos Data de Vencimento FCP e Valor do ICMS FCP do Anexo IV – EC87/15, quando a origem da informação for oriunda da GNRE Online e  a UF=RJ\.

__MFS585303__

Andréa Rocha

Alteração da regra do campo Crédito ICMS\-ST Período Anterior da Aba Principal

__MFS585693__

Andréa Rocha

Alteração da regra de geração do campo Valor do 1º Vencimento do ICMS\-ST FCP, quando a origem da informação for oriunda da GNRE Online e a UF=RJ\.

__MFS585734__

Andréa Rocha

Alteração da regra do Anexo IV \- EC87/15 e da regra do Quadro \(EC87/15\), para que os os valores de ICMS e FECP dos dois, gerem o mesmo valor de resultado final\.

__MFS1016914__

Lyene Benvenutti

Especificar na regra que o campo “Valor do ICMS ST \- Devolução” na GIA\-ST considera apenas notas de devolução__ de entrada\.__

##### REGRAS DE NEGÓCIO

__SAFX07, SAFX08, Apuração do ICMS\-ST e outros\.__

__Saída para aba Registro Principal__

__Cód\.__

__Descrição__

__DR__

__RN00__

__Regra Geral Registro Principal__:

__Vencimentos__

__Alteração da MFS2283__:

Para recuperar os Vencimentos e Valores do ICMS\-ST e ICMS\-ST FCP, existem dois processos na rotina de geração da GIA\-ST:

- Através das GNRE’s, preenchendo automaticamente os campos de Vencimentos e Valores associados aos vencimentos das GNRE’s do período, exceto aos valores de ICMS\-ST FCP que deverá ser habilitado conforme o vencimento do ICMS\-ST, mas preenchido manualmente\[MFS28188\];

__ICMS ST FCP__

Sobre a automatização referente ao ICMS ST FCP, o valor será recuperado a partir da totalização dos valores demonstrados nas Guias de Recolhimento, as Guias de FECEP estarão tipificadas  com o campo Código de Obrigação a Recolher igual à ‘006 – ICMS resultante da alíquota  adicional dos itens incluídos  no fundo  de Combate a Pobreza\.

Nesse caso é verificado se existe conteúdo na tabela ICT\_GUIA\_GNRE\_CON, que contém as guias recolhidas no período, então se houver, a rotina de geração realiza o tratamento abaixo:

1. Verifica a inscrição estadual do estabelecimento para a UF em questão \(módulo Básicos \- Parâmetros, menu Preliminares >> Inscrições Estaduais\);
2. Caso a inscrição não esteja cadastrada, ou esteja suspensa, soma todas as guias da UF em questão, o valor recuperado será gravado na GIA\-ST no campo do 1º vencimento \(módulo Estadual \- ICMS, menu Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Manutenção\), e a data do vencimento será a maior data das GNRE’s existentes no período;
3. Caso a inscrição exista e seja válida, totaliza as GNRE’s por data de vencimento, e grava um registro para cada vencimento, com o valor totalizado do vencimento\.

- Ou; Através da parametrização por UF Favorecida \(módulo Estadual \- ICMS, menu Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\) caso não localize guias no período\. Nesse caso o usuário precisa colocar os dias de Vencimento e quando efetuar a geração dos dados, esses dias serão preenchidos na Manutenção no item Vencimentos da Aba Principal, mas seu valor deverá ser preenchido manualmente\. Alteração da __MFS10606__: O Valor do ICMS\-ST referente ao primeiro dia de vencimento passou a ser preenchido de forma automática, mas *apenas* quando existir apenas um dia de vencimento na parametrização\. Neste caso, o Valor do ICMS\-ST será preenchido com o valor total do ICMS\-ST apurado para a UF\.  Quando for parametrizado mais de um dia de vencimento, nenhum valor será preenchido de forma automática, e os valores referentes a cada um dos vencimentos deverão ser informados manualmente através da tela de manutenção\.

*Observações:*

- A GIA\-ST é sempre gerada por UF, portanto, ao ler as GNRE’s na tabela ICT\_GUIA\_GNRE\_CON, sempre considera a UF da GIA\-ST, tratando cada caso separadamente\.
- Ao fazer o cálculo das GNRE’s considera as GNRE’s com Data de Apuração dentro do período informado na GIA\-ST, nesse caso não considera a parametrizacoa por UF Favorecida \(regra abaixo\);

__Alteração da OS3298__:

__Lançamentos__

A partir da OS3298 a geração da GIA\-ST passou a considerar os lançamentos complementares da apuração do ICMS \(livro P9\), dependendo do parâmetro “__Utilizar os lançamentos da apuração do ICMS\-ST \(P9\) para complementar a GIA\-ST”__ da parametrização das UF’s da GIA\-ST\. 

\(até então a GIA\-ST era gerada com base apenas nos documentos fiscais, sem recuperar nenhuma informação do P9\)

Se “__Utilizar os lançamentos da apuração do ICMS\-ST \(P9\) para complementar a GIA\-ST”__ = N ou nulo

      Permanece a forma original da geração, sem recuperar nenhuma informação da apuração do ICMS\-ST \(P9\)\. 

Se “__Utilizar os lançamentos da apuração do ICMS\-ST \(P9\) para complementar a GIA\-ST”__ = “S”

      Neste caso a geração irá recuperar o valor dos lançamentos complementares da apuração, para cada período e

      UF, e armazená\-los em campos separados dos demais campos da GIA\-ST \(ver regras específicas de cada campo

      na RN04 a RN08\)\.

      

       Estes valores ficam armazenados em campos separados, para que o usuário possa visualizá\-los 

       separadamente\. Somente no momento da emissão da GIA\-ST \(menu “Emissão”\) ou da geração do arquivo  

       \(menu “Meio Magnético”\) é que os valores serão totalizados nos campos “oficiais” da GIA\-ST\.

__Devolução/ Ressarcimento__

Recupera Valores das Entradas

Gravação das Notas Fiscais de Devolução e Ressarcimento para Anexos 1 e 2 \(tabela ICT\_GIA\_ST\_ANEX1\_2\)

Se parâmetro Geração p/ Meio Magnético estiver marcado na tela de Geração, então recupera:

Notas fiscais de Entrada \(campo 03 da SAFX07\);

Notas fiscais não canceladas \(campo 30 da SAFX07\);

Notas fiscais com classificação 1 e 3 \(campo 12 da SAFX07\);

É necessário que o estabelecimento \(campo 02 da SAFX07\) seja igual o que for marcado na tela de Geração e a data fiscal \(campo 20 da SAFX07\) compreenda a data preenchida no campo Período, além disso, a pessoa física/jurídica \(campo 07 da SAFX07\) precisa ter cadastro na SAFX04\.

Após a verificação da capa da nota fiscal, ainda verificar se no item dessa nota o valor de tributação do ICMS\-ST é maior que zero e se o crédito é apropriado \(campos 78 e 94 da SAFX08\)\.

Definir Devolução ou Ressarcimento para gravação:

O que irá definir a nota fiscal de Devolução é o campo 04 da SAFX07 que deverá ser igual a “2” e não deve ter o CFOP parametrizado em Parâmetros por CFOP >> Ressarcimentos\.

O que irá definir a nota fiscal de Ressarcimento é o campo 04 da SAFX07 que deverá ser igual a “2” e deve ter o CFOP parametrizado em Parâmetros por CFOP >> Ressarcimentos\.

__Alteração da MFS2283/ CH12151\_2016__:

__Complemento ICMS\-ST__

__\[ALTERAÇÃO\-MFS69213\] Inclusão de Regra p/ considerar o Complemento de ICMS\-ST de Terceiros e Aquisições de Simples Nacional__

__Tratamento__

Recupera Valores das Entradas – Notas Fiscais Complementares\.

__Se__ o parâmetro Geração p/ Meio Magnético estiver marcado na tela de Geração; 

 __Então__ verificar o parâmetro “Complemento ICMS\-ST \(Anexo II\)”, conforme regras abaixo:

__Parâmetro Complemento ICMS\-ST \(Anexo II\)__

__Parâmetro Desmarcado:__ O sistema permanecerá conforme regra original, desconsiderando o parâmetro ““Complemento ICMS\-ST \(Anexo II\)”\.

__Parâmetro Marcado:__ A geração deverá considerar o parâmetro ““Complemento ICMS\-ST \(Anexo II\)”, e recuperar as Notas fiscais que atendam aos seguintes critérios:

   \- Estabelecimento igual ao estabelecimento selecionado na geração;

   \- A data fiscal da nota deve ser referente ao período informado em tela \(>= data inicial e <= data final\);

   \- Nota fiscal de entrada \(campo 03 \- MOVTO\_E\_S __<> 9__ da tabela SAFX07\);

   \- Nota fiscal Normal \(campo 04 \- NORM\_DEV __= 1__ da tabela SAFX07\);

   \- Classificação fiscal 1 e 3 \(campo 12 \- COD\_CLASS\_DOC\_FIS __= 1, 3__ da tabela SAFX07\);

   \- Não considerar notas fiscais canceladas \(campo 30 \- SITUACAO __<> S__ da tabela SAFX07\);

   \- Nota Fiscal Complementar \(campo 125 – IND\_SITUACAO\_ESP __= 5__  da tabela SAFX07\)\.

            Obs\.: Situação Especial = “5 \- NF Complementar ou CT\-e de Complemento de Valores \(modelo: 57\)”\.

Após a verificação da Capa da Nota Fiscal, ainda verificar o Item da Nota Fiscal se:

   \- Valor de ICMS Substituição Tributária maior que zero \(campo 52 – VLR\_SUBST\_ICMS __> 0__ da tabela SAFX08\) *>> Campo VLR\_TRIBUTO\_ICMSS da tabela DWT\_ITENS\_MERC*\.

   \- Se o crédito é apropriado \(campo 78 – APROPRIA __= S__ da tabela SAFX08\) *>> Campo IND\_CRED\_ICMSS da tabela DWT\_ITENS\_MERC*\.

__Então__ preencher a tabela “ICT\_GIA\_ST\_ANEX1\_2”\. 

__Obs\.:__ Para o Registro ser considerado na Aba Anexo II, o Campo IND\_DEV\_RES\_ICMSS deve ser = __2\.__

*Essa regra contempla os seguintes cenários:*

*1 \- Nas aquisições de empresas do Simples Nacional o cliente emite nota fiscal de entrada para auto lançamento a crédito dos respectivos impostos;  
   
2 – Emissão de nota de venda do Substituto Tributário com retenção do ICMS ST e o cliente emite uma nota de devolução na qual não há o ICMS ST, acompanhada de uma segunda nota fiscal para amparar o ressarcimento \(Reembolso\) do valor anteriormente retido na venda\. *

__\[MFS536852\] __Inclusão do valor do FCP no cálculo do valor de devolução ou anulação\.

__Devoluções ou Anulações EC 87/15__

1. Recupera Valores das Entradas:

             Gravação das Notas Fiscais de “Devoluções ou Anulações” Anexo IV – EC 87/15 \(campo a definir pelo A&D\)

             Se o parâmetro Geração p/ Meio Magnético estiver marcado na tela de Geração, então recupera as notas com as     

             seguintes características:

- Notas fiscais de Entrada \(campo 03 da SAFX07\);
- Que seja de devolução \(campo 04 da SAFX07\);
- Não canceladas \(campo 30 da SAFX07\);
- Com classificação 1, 3 e 4 \(campo 12 da SAFX07\);
- De operações interestaduais \(CFOP’s iniciados por “2”\);

            Para gerar em cada UF Favorecida, a identificação da UF Destino Origem será sempre a UF do estabelecimento da 

            geração \(que é o contribuinte emitente da nota da venda\) e a identificação da UF Origem Destino será a UF de 

            origem destino informada na nota fiscal \(campo 117 122 da SAFX07\)\.

            É necessário que o estabelecimento \(campo 02 da SAFX07\) seja igual o que for marcado na tela de Geração e a  

            data fiscal \(campo 20 da SAFX07\) compreenda a data preenchida no campo Período, além disso, a pessoa 

            física/jurídica \(campo 07 da SAFX07\) precisa ter cadastro na SAFX04\.

            Após a verificação da capa da nota fiscal, ainda verificar se no item dessa nota, o valor do ICMS da UF de Origem 

            \(campo 223 da SAFX08\), ou o valor do ICMS da UF de Destino \(campo 222 da SAFX08\), ou o valor FCP UF Destino 

            \(campo 221 da SAFX08\) é maior que zero\.

*           Observação: *Considerar somente notas com item\.

__\[MFS30017\]__

1. Recuperação do valor de saldo credor do período anterior da UF \(tabela da “Apuração ICMS Difal UF Orig/Dest”\):

Empresa

Código da empresa 

Estabelecimento

Código do estabelecimento 

No caso da Apuração do ICMS por Inscrição Estadual Única, será o código do estabelecimento centralizador\.

Código do Livro

= “108” \(no caso da Apuração do ICMS normal\)

= “165” \(no caso da Apuração do ICMS por Inscrição Estadual Única\)

Data da Apuração

Data da apuração do período anterior \(anterior ao mês inicial informado em tela\)

UF

UF para a qual será feita a geração

             O campo que contém o saldo credor é o “Resultado Credor”\.

              Caso o registro não exista na tabela, será considerado o valor zeros para o saldo credor anterior\. 

__\[ALTERADA – MFS3854\]__

__Geração por Inscrição Estadual Única__

Se o parâmetro __Geração p/ Empresa com IEU __estiver __*desmarcado*__ na tela de geração dos registros, gerar os dados do estabelecimento parametrizado na tela geração e em Parâmetros por UF Favorecida de forma descentralizada;

Se parâmetro __Geração p/ Empresa com IEU __estiver__ *marcado* __na tela de geração dos registros, gerar os dados considerando as informações do contribuinte do estabelecimento centralizador e consolidar os valores dos estabelecimentos centralizados, parametrizados em Controle de Obrigações Estaduais\.

__\[ALTERAÇÃO\-MFS91049\] __Inclusão de Parâmetro p/ considerar somente as informações do Anexo IV – EC87/15__ __

__\[ALTERAÇÃO\-MFS94270\] __Inclusão de tratamento para considerar informações do Anexo IV – EC87/15, conforme parâmetro “Considerar UF p/ Geração do EC87/15 \(Anexo IV\)” incluído na tela de UF Favorecido\.

__Parâmetro: Geração do EC87/15 \(Anexo IV\)__

O parâmetro “Geração do EC87/15 \(Anexo IV\)” foi incluído para permitir aos contribuintes que são obrigados a entregar apenas o __*Quadro EC 89/15*__\. \(*Solicitação do cliente ARCOM*\)\.

Para isso o sistema deverá realizar __apenas__ o preenchimento dos campos 1 e 2, 4, 5,e 6 e 22 a 36 do __Registro A0__ e do próprio quadro EC 89/15 \(Anexo IV\), considerando as Regras __RN30__ à __RN35__ e Regras de “__Saída para aba Registro Anexo IV – EC 87/15”\.__

__Tratamento__

__Se__ o parâmetro “__Geração do EC87/15 \(Anexo IV\)” __estiver __*desmarcado*__ na tela de geração dos registros, o sistema permanecerá conforme regra original, gerando todas as informações da GIA\-ST; 

__Default:__ Desmarcado\.

__Se __o parâmetro “__Geração do EC87/15 \(Anexo IV\)” __na tela de geração dos registros, estiver__ *marcado\.*__

  __Verificar __se__ __parâmetro “__Considerar UF p/ Geração do EC87/15 \(Anexo IV\)__”__ __na tela de “Parâmetros por UF Favorecida”, estiver __marcado\.__

    Parâmetro __marcado __para UF Favorecida:

         __Gerar__ somente os Registros do __Anexo IV__, referente as informações do Quadro EC 87/15 __e__ Campo 1 à 6 e 22 à 36 do Registro A0\.

    Parâmetro __desmarcado __para UF Favorecida:

          __Gerar__ todas as informações da GIA\-ST, se houver;

Caso o parâmetro “__Geração do EC87/15 \(Anexo IV\)”, __na tela de geração dos registros__ __estiver __marcado__ e não houver nenhuma__ UF, __com o parâmetro__ “Considerar UF p/ Geração do EC87/15 \(Anexo IV\)__”, __marcado, __na tela de “Parâmetros por UF Favorecida, o sistema deverá gerar todas as informações da GIA\-ST, caso houver e__ __gravar a seguinte Mensagem de Log:

__Mensagem de Log__: O parâmetro “Geração do EC87/15 \(Anexo IV\)”, está marcado, porém não identificamos nenhuma UF parametrizada na tela de UF Favorecida\. Favor consultar a tela de UF Favorecida e marcar a opção “Considerar UF p/ Geração do EC87/15 \(Anexo IV\)” para a UF que deverá gerar somente as informações do Quadro de EC87/15\.

__Obs\.:__ O objetivo desse parâmetro é permitir que o usuário possa optar em gerar somente as informações do EC87/15 por UF\.

Se parâmetro “__Geração do EC87/15 \(Anexo IV\)” __estiver__ *marcado* __na tela de geração dos registros, o sistema deverá gerar somente os Registros do __Anexo IV__, referente as informações do Quadro EC 87/15 __e__ Campo 1 à 6 e 22 à 36 do Registro A0\.

Obs¹\.: Essa alteração está alinhada com a Área de Informação, Henrique Pontes e Marcos de Paula\.

Obs²\.: Essa funcionalidade foi implementada por solicitação do cliente ARCOM, para ser executada, __Por UF__, para a UF de Distrito Federal, porém foi disponibilizado a solução de forma o usuário possa selecionar qualquer UF, conforme necessidade\.

Obs³\.: O cliente se enquadra no art\. 27\-L do Decreto nº 18\.955/97\. No Art\. 207 § 14 do RICMS/DF ele cita :  
"§ 14\. Os campos 4, 5, 6 e 22 a 36 de que trata o § 4º são comuns ao preenchimento das operações relativas à substituição tributária e às operações e prestações destinadas a consumidor final não contribuinte do imposto, devendo, na hipótese de preenchimento exclusivo do Quadro Emenda Constitucional nº 87/15, por contribuinte que não seja substituto tributário, ser desconsideradas as partes das regras de preenchimento que se referem ao substituto\."

__OS2289__

__OS3298__

__MFS2283__

__MFS3854__

__CH12151\_2016__

__MFS10606__

__MFS28188__

__MFS30017__

__MFS91049__

__MFS536852__

__RN01__

__Regra Geral Parâmetro 67 por UF__:

No momento da geração da GIA\-ST, verificar se está selecionado o parâmetro 67 nos parâmetros por UF, para o estabelecimento em questão\.

*Impacto:*

ICMS → Apuração → Guias de Recolhimento → Guia de Informação de Substituição Tributária → Geração 

ICMS → Apuração → Guias de Recolhimento → Guia de Informação de Substituição Tributária → Manutenção

ICMS → Apuração → Guias de Recolhimento → Guia de Informação de Substituição Tributária → Emissão

ICMS → Apuração → Guias de Recolhimento → Guia de Informação de Substituição Tributária → Geração para o meio magnético

__CH72922\-A__

__RN02__

__Parâmetro 67 por UF desmarcado__:

Caso o parâmetro 67 não esteja marcado, o sistema deverá buscar a UF do cadastro da pessoa física/jurídica informada no documento fiscal \(safx04\)\.

__CH72922\-A__

__RN03__

__Parâmetro 67 por UF marcado__:

Caso o parâmetro 67 esteja marcado, a GIA\-ST deverá recuperar a UF de acordo com o campo “UF Destino”, da capa do documento fiscal \(campo 122 da safx07\)\. 

No caso de existir documentos sem a UF preenchida na capa do documento fiscal, o sistema irá recuperar da pessoa fis/jur do documento fiscal, procedimento este que já é feito para o livro de saídas\.

__CH72922\-A__

__RN03a__

Campo__ Base de Cálculo ICMS ST__

Esse campo deverá ser preenchido com o somatório da Base de Cálculo ICMS ST das notas fiscais\.

   

__Tratamento:__

Se o campo BASE\_SUB\_TRIB\_ICMS da SAFX08 não estiver preenchido, preencher com o campo BASE\_ICMS\_ORIGDEST da SAFX08 de acordo com a UF de Origem/Destino para considerar corretamente a respectiva UF parametrizada na GIA\-ST\.  

Senão preencher com zero\.

__MFS11377__

__RN03b__

Campo__ ICMS ST__

__\[MFS91970\] Tratamento para subtrair o valor de FECP somado ao valor de ICMS\-ST, no processo de Data Mart\.__

Esse campo deverá ser preenchido com o somatório do ICMS ST das notas fiscais\. 

__Tratamento:__

Se o parâmetro “__*Retirar o valor de FECP do ICMS\-ST*” __estiver __*desmarcado*__ na tela de geração dos registros, a de preenchimento desse campo permanecerá conforme regra original, conforme abaixo:

Se o campo VLR\_TRIBUTO\_ICMSS da DWT\_ITENS\_MERC \(SAFX08\) não estiver preenchido, preencher com o campo VLR\_ICMS\_ORIGDEST da DWT\_ITENS\_MERC \(SAFX08\) de acordo com a UF de Origem/Destino para considerar corretamente a respectiva UF parametrizada na GIA\-ST\. 

Senão preencher com zero\.

__Default:__ Desmarcado\.

Se parâmetro “__*Retirar o valor de FECP do ICMS\-ST*” __estiver__ *marcado* __na tela de geração dos registros, o sistema deverá preencher campo de ICMS\-ST, efetuando o cálculo do valor de FECP \(\-\) ICMS\-ST, que passará a preencher o valor de ICMS\-ST sem o Valor de FECP que está embutido na DWT\_ITENS\_MERC Campo VLR\_TRIBUTO\_ICMSS, conforme execução do processo de Data Mart, e deverá seguir conforme a regra abaixo:

      __Se__ o campo VLR\_TRIBUTO\_ICMSS da DWT\_ITENS\_MERC \(SAFX08\) estiver preenchido;

        __Preencher__ o Campo de ICMS\-ST com o resultado do cálculo abaixo:

            Campos VLR\_TRIBUTO\_ICMSS \(\-\) VLR\_FECP\_ICMS\_ST da tabela \(DWT\_ITENS\_MERC\) 

__Ou__

        Se o campo VLR\_TRIBUTO\_ICMSS da DWT\_ITENS\_MERC \(SAFX08\) não estiver preenchido;

           __Preencher__ com o campo VLR\_ICMS\_ORIGDEST da DWT\_ITENS\_MERC \(SAFX08\) de acordo com a UF de Origem/Destino para considerar corretamente a respectiva UF parametrizada na GIA\-ST\.

Senão preencher com zero\.

__MFS11377__

__MFS91970__

__RN03c__

Campo__ __<a id="_Hlk150781589"></a>__Crédito ICMS\-ST Período Anterior__

__\[MFS585303\] __Alteração da regra do campo Crédito ICMS\-ST Período Anterior

Recuperação do valor de saldo credor do período anterior da UF \(Tabela da “Apuração ICMS\-ST”\):

Empresa

Código da empresa 

Estabelecimento

Código do estabelecimento 

No caso da Apuração do ICMS por Inscrição Estadual Única, será o código do estabelecimento centralizador\.

Código do Livro

= “108” \(no caso da Apuração do ICMS normal\)

= “165” \(no caso da Apuração do ICMS por Inscrição Estadual Única\)

Data da Apuração

Data da apuração do período anterior \(anterior ao mês inicial informado em tela\)

UF

UF para a qual será feita a geração

Código Operação

014 \(Saldo Credor a transportar\)

             O campo que contém o saldo credor é o VAL\_ITEM\_DISCRIM\.

              Caso o registro não exista na tabela, será considerado o valor zeros para o saldo credor anterior\. 

__MFS585303__

__RN04__

Campo __Outros Débitos__:

Se parâmetro __“Utilizar os lançamentos da apuração do ICMS\-ST \(P9\) para complementar a GIA\-ST”__ = “S”

      O campo será gravado com o total dos lançamentos complementares da Apuração do ICMS\-ST \(P9\) referentes ao

       período e UF em questão, e classificados como “outros débitos” \(lançamentos com código de operação = “__002__”\)\.

Senão

      O campo será gravado com o valor zero\.  

__\[ALTERADA – MFS3854\]__

Se o parâmetro “Geração p/ Empresas com IEU” estiver marcado na tela de Geração \(geração dos registros da GIA\-ST\), as informações acima serão recuperadas da tabela de apuração de Empresas c/ Insc\. Estadual Única\.

__OS3298__

__MFS3854__

__RN05__

Campo __Estorno de Crédito__:

Se parâmetro __“Utilizar os lançamentos da apuração do ICMS\-ST \(P9\) para complementar a GIA\-ST”__ = “S”

      O campo será gravado com o total dos lançamentos complementares da Apuração do ICMS\-ST \(P9\) referentes ao

       período e UF em questão, e classificados como “estorno de crédito” \(lançamentos com código de operação = “__003__”\)\.

Senão

      O campo será gravado com o valor zero\.  

__\[ALTERADA – MFS3854\]__

Se o parâmetro “Geração p/ Empresas com IEU” estiver marcado na tela de Geração \(geração dos registros da GIA\-ST\), as informações acima serão recuperadas da tabela de apuração de Empresas c/ Insc\. Estadual Única\.

__OS3298__

__MFS3854__

__RN06__

Campo __Outros Créditos__:

Se parâmetro __“Utilizar os lançamentos da apuração do ICMS\-ST \(P9\) para complementar a GIA\-ST”__ = “S”

      O campo será gravado com o total dos lançamentos complementares da Apuração do ICMS\-ST \(P9\) referentes ao

       período e UF em questão, e classificados como “outros créditos” \(lançamentos com código de operação = “__006__”\)\.

Senão

      O campo será gravado com o valor zero\.  

__\[ALTERADA – MFS3854\]__

Se o parâmetro “Geração p/ Empresas com IEU” estiver marcado na tela de Geração \(geração dos registros da GIA\-ST\), as informações acima serão recuperadas da tabela de apuração de Empresas c/ Insc\. Estadual Única\.

__OS3298__

__MFS3854__

__RN07__

Campo __Estorno de Débito:__

Se parâmetro __“Utilizar os lançamentos da apuração do ICMS\-ST \(P9\) para complementar a GIA\-ST”__ = “S”

      O campo será gravado com o total dos lançamentos complementares da Apuração do ICMS\-ST \(P9\) referentes ao

       período e UF em questão, e classificados como “estorno de débito” \(lançamentos com código de operação = “__007__”\)\.

Senão

      O campo será gravado com o valor zero\.  

__\[ALTERADA – MFS3854\]__

Se o parâmetro “Geração p/ Empresas com IEU” estiver marcado na tela de Geração \(geração dos registros da GIA\-ST\), as informações acima serão recuperadas da tabela de apuração de Empresas c/ Insc\. Estadual Única\.

__OS3298__

__MFS3854__

__RN08__

Campo __Deduções__:

Se parâmetro __“Utilizar os lançamentos da apuração do ICMS\-ST \(P9\) para complementar a GIA\-ST”__ = “S”

      O campo será gravado com o total dos lançamentos complementares da Apuração do ICMS\-ST \(P9\) referentes ao

       período e UF em questão, e classificados como “deduções” \(lançamentos com código de operação = “__012__”\)\.

Senão

      O campo será gravado com o valor zero\.

__\[ALTERADA – MFS3854\]__

Se o parâmetro “Geração p/ Empresas com IEU” estiver marcado na tela de Geração \(geração dos registros da GIA\-ST\), as informações acima serão recuperadas da tabela de apuração de Empresas c/ Insc\. Estadual Única\.

__OS3298__

__MFS3854__

__RN09__

Campo __ICMS\-ST Devido__: \(VLR\_ICMSS\_DEVIDO\)

Neste campo será gravado o resultado abaixo, caso positivo:     \(caso negativo, gravar zero\)

\(ICMS\-ST Retido \+ Outros Débitos \+ Estorno de Créditos\) – \(Devoluções \+ Ressarcimento \+ Crédito do Per\. Anterior \+ Outros Créditos \+ Estorno de Débitos \+ Deduções\)

Observar que na totalização dos valores não é necessário utilizar o parâmetro de utilização dos lançamentos complementares, pois caso os mesmos não sejam utilizados, os respectivos campos estarão com valor zero\.

__OS3298__

__RN10__

Campo __Crédito p/o Período Seguinte__: \(VLR\_ICMSS\_CRED\)

Se o resultado abaixo for positivo, gravar o resultado no campo “__Crédito p/o Período Seguinte__”, caso contrário,__ __o resultado deverá ser gravado no campo “__ICMS\-ST a Recolher__”: 

\(Devoluções \+ Ressarcimento \+ Crédito do Per\. Anterior \+ Outros Créditos \+ Estorno de Débitos \+ Deduções\) – 

\(ICMS\-ST Retido \+ Outros Débitos \+ Estorno de Créditos \+ Repasse ICMS\-ST Combustível\) 

Obs: Este valor é o resultado do total dos créditos – total dos débitos \(incluindo o repasse do ICMS\-ST de combustível\)\.

__OS3298__

__RN11__

Campo __ICMS\-ST a Recolher__: \(VLR\_ICMSS\_RECOLHIM\)

\(ver __RN10__\)

__OS3298__

__RN12__

Campo__ Vencimentos – Data do 1º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com a data do 1º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

__OS2289__

__RN13__

Campo__ Vencimentos – Data do 2º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com a data do 2º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

__OS2289__

__RN14__

Campo__ Vencimentos – Data do 3º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com a data do 3º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

__OS2289__

__RN15__

Campo__ Vencimentos – Data do 4º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com a data do 4º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

__OS2289__

__RN16__

Campo__ Vencimentos – Data do 5º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com a data do 5º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

__OS2289__

__RN17__

Campo__ Vencimentos – Data do 6º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com a data do 6º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

__OS2289__

__RN18__

Campo__ Vencimentos – Valor do 1º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com o valor a recolher referente o 1º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

Alteração da __MFS10606__: 

O Valor do ICMS\-ST referente ao primeiro dia de vencimento passou a ser preenchido de forma automática, mas *apenas* quando existir apenas um dia de vencimento na parametrização \(menu “Parâmetros por UF Favorecida”\)\. Neste caso, o Valor do ICMS\-ST será preenchido com o valor total do ICMS\-ST apurado para a UF \(este valor corresponde ao campo “21\-Total do ICMS\-ST a Recolher” da GIA\-ST, que na tela de manutenção é o campo “ICMS\-ST a Recolher”\)\. 

Quando for parametrizado mais de um dia de vencimento, nenhum valor será preenchido de forma automática, e todos os valores referentes a cada vencimento deverão ser informados manualmente através da tela de manutenção\.

__OS2289__

__MFS10606__

__RN19__

Campo__ Vencimentos – Valor do 2º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com o valor a recolher referente o 2º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

__OS2289__

__RN20__

Campo__ Vencimentos – Valor do 3º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com o valor a recolher referente o 3º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

__OS2289__

__RN21__

Campo__ Vencimentos – Valor do 4º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com o valor a recolher referente o 4º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

__OS2289__

__RN22__

Campo__ Vencimentos – Valor do 5º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com o valor a recolher referente o 5º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

__OS2289__

__RN23__

Campo__ Vencimentos – Valor do 6º Vencimento do ICMS\-ST:__

__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção ou Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\.

Preencher com o valor a recolher referente o 6º vencimento do ICMS\-ST, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

__OS2289__

__RN24__

Campo__ Vencimentos – Valor do 1º Vencimento do ICMS\-ST FCP:__

Este campo não terá processamento automático no momento, então preencher com o valor a recolher manualmente referente o 1º vencimento do ICMS\-ST FCP, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

\[__MFS585693__\] Alteração da regra de geração dos dados a partir da GNRE Online, para UF=RJ, para passar a usar o valor de FECP\.  Manter a regra original para RJ, para gerar para períodos anteriores\.

O Valor do ICMS\-ST FCP referente ao primeiro dia de vencimento passou a ser preenchido de forma automática, mas *apenas* quando existir apenas um dia de vencimento na parametrização \(menu “Parâmetros por UF Favorecida”\) OU quando a tabela ICT\_GUIA\_GNRE\_CON  tenha informações de GNRE, neste caso a data de vencimento dessa tabela será considerada na geração\.

Composição dos Cálculo do campo:

O Valor do ICMS\-ST FCP será preenchido com o somatório do __Valor Principal__ da Guia Recolhimento Tributos Estaduais \(GNRE\), quando__ __o código de obrigação for igual a “006\-ICMS resultante da alíquota adicional dos itens incluídos no FCP” \(__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais \(GNRE\)  >> Manutenção \) 

\+ __Valor Principal__ da Guia Recolhimento Tributos Estaduais Grupo/Convênio GNRE, quando__ __o código de obrigação for igual a “006\-ICMS resultante da alíquota adicional dos itens incluídos no FCP” \(__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais por Grupo/Convênio GNRE >> Manutenção\) 

\+ __Valor Principal ou Valor Total \(caso o valor Principal esteja sem valor\)__ da Guia Recolhimento Tributos Estaduais \(GNRE Online\), quando UF <>  ‘RJ’ e o código de obrigação for igual a “006\-ICMS resultante da alíquota adicional dos itens incluídos no FCP” \(__Origem__: Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais \(GNRE Online >> Manutenção \) 

\+ __Valor Principal FECP ou Valor Total FECP \(caso o valor Principal FECP esteja sem valor\)__ da Guia Recolhimento Tributos Estaduais \(GNRE Online\), quando UF =  ‘RJ’ OU __Valor Principal ou Valor Total \(caso o valor Principal esteja sem valor\)__ da Guia Recolhimento Tributos Estaduais \(GNRE Online\) quando UF =  ‘RJ’ e o código de obrigação for igual a “006\-ICMS resultante da alíquota adicional dos itens incluídos no FCP” \(__Origem: __Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia Recolhimento Tributos Estaduais \(GNRE Online >> Manutenção \)

\+ __Valor Recolhimento da Apuração do P9 __quando__ __o código de obrigação for igual a “006\-ICMS resultante da alíquota adicional dos itens incluídos no FCP” \( __Origem: __Estadual >> ICMS >> Apuração >> Apuração ICMS >> Lançamentos Complementares >> Apuração do ICMS à Ajuste SINIEF – Opção da Aba \- Guia \)\.

__\[MFS29475\]__

Obs\.: Somente serão recuperadas as guias em que o código de obrigação for igual a “006\-ICMS resultante da alíquota adicional dos itens incluídos no FCP”\.

Resumo: 

Valor do ICMS\-ST FCP = __ict\_guia\_gnre\.vlr\_principal \+ ict\_guia\_gnre\_con\.vlr\_principal \+ ict\_gnre\_ol\_guia\.vlr\_principal ou ict\_gnre\_ol\_guia\.vlr\_total\) \+ guia\_rec\_subst\.vlr\_guia\_recol__

- Observação: Quando for parametrizado mais de um dia de vencimento na parametrização por UF Favorecida \(módulo Estadual \- ICMS, menu Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Parâmetros por UF Favorecida\), nenhum valor será preenchido de forma automática, e todos os valores referentes a cada vencimento deverão ser informados manualmente através da tela de manutenção\. 
- Esssa regra só será aplicada se não houver GNRE’s na tabela ICT\_GUIA\_GNRE\_CON, caso tenha informações de GNRE sempre será considera a a data de vencimento na geração\. 

\[MFS28188\]

*Importante *

As guias de ST cadastradas na aba “Guia” \(manutenção dos Lançamentos Complementares\) são referentes ao ICMS\-ST interno, pois as guias interestaduais são geradas na rotina das GNRE’s\. Na aba “Guia” não existe a possibilidade de informar a UF, como acontece na aba “Lançamentos”, por isso, as guias aqui informadas na aba “Guia” \(manutenção dos Lançamentos Complementares\) são referentes sempre a UF do Estabelecimento\. Assim, só é necessário recuperar as guias desta tabela quando se tratar da apuração da UF do Estabelecimento\. Para as demais UF’s, são utilizadas as GNRE’s\.

__O cálculo deste campo foi definido baseado no registro E250 do Sped Fiscal\.__

__MFS2283__

__MFS28188__

__MFS29475__

__MFS585693__

__RN25__

Campo__ Vencimentos – Valor do 2º Vencimento do ICMS\-ST FCP:__

Este campo não terá processamento automático no momento, então preencher com o valor a recolher manualmente referente o 2º vencimento do ICMS\-ST FCP, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

__MFS2283__

__RN26__

Campo__ Vencimentos – Valor do 3º Vencimento do ICMS\-ST FCP:__

Este campo não terá processamento automático no momento, então preencher com o valor a recolher manualmente referente o 3º vencimento do ICMS\-ST FCP, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

__MFS2283__

__RN27__

Campo__ Vencimentos – Valor do 4º Vencimento do ICMS\-ST FCP:__

Este campo não terá processamento automático no momento, então preencher com o valor a recolher manualmente referente o 4º vencimento do ICMS\-ST FCP, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

__MFS2283__

__RN28__

Campo__ Vencimentos – Valor do 5º Vencimento do ICMS\-ST FCP:__

Este campo não terá processamento automático no momento, então preencher com o valor a recolher manualmente referente o 5º vencimento do ICMS\-ST FCP, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

__MFS2283__

__RN29__

Campo__ Vencimentos – Valor do 6º Vencimento do ICMS\-ST FCP:__

Este campo não terá processamento automático no momento, então preencher com o valor a recolher manualmente referente o 6º vencimento do ICMS\-ST FCP, conforme prazos constantes de Convênios e Protocolos ICMS de acordo com a RN00\.

__MFS2283__

__RN30__

Campo __EC N° 87/15 com Movimento:__

__\[ALTERADA – CH2215\_2016\]__

A geração relativa a EC 87/2015 no registro principal independe se existem valores de ICMS\-ST a serem declarados na GIA, então quando o campo GIA Sem Movimento estiver marcado ou não deve ser considerados os valores de diferencial de alíquota que competem a EC 87/2015\.

Este campo virá marcado quando via processamento \(geração dos registros\) gerar valores para diferencial de alíquota à UF de Destino e FCP, mas também será possível o usuário efetuar a parametrização manualmente\.

Irá considerar o flag quando os campos Valor ICMS Devido à UF de Destino ou Total ICMS FCP forem preenchidos\.

__MFS2283__

__CH2215\_2015__

__RN31__

Campo __Informações EC 87/15 – Valor ICMS Devido à UF de Destino:__

__\[ALTERADA – MFS4524/ CH21316\_2016/MFS27837\]__

__Origem:__ 

Estadual >> ICMS >> DATA MART >> Apuração do ICMS >> Ajuste SINIEF \(quando o parâmetro “91 \- Apuração ICMS Dif\.Alíquota UF Orig/Dest \- EC 87/15” da parametrização por UF do Módulo ICMS estiver selecionada para a UF favorecida a ser gerada\);

Específicos >> PIM \- Gestão do Controle de Incentivos Fiscais do Polo Industrial de Manaus >> Apuração >> Apuração dos Saldos de Impostos e Taxas >> Lançamentos Complementares >> Apuração do ICMS Dif\. Aliq\. UF Origem/Destino \(EC 87/15\) \(quando o parâmetro “91 \- Apuração ICMS Dif\.Alíquota UF Orig/Dest \- EC 87/15” da parametrização por UF do Módulo ICMS estiver selecionada para a UF favorecida a ser gerada\)\.

Se a UF favorecida = “RJ”

    Preencher com o conteúdo do campo gerado para o diferencial de alíquota do Total dos Débitos por Saídas e Prestações     

    da UF favorecida, de acordo com o período preenchido na tela de Geração e Estabelecimento selecionado __mais__ o campo 

    Total ICMS FCP \(vide regra de geração – RN35\)\.

Senão

    Preencher com o conteúdo do campo gerado para o diferencial de alíquota do Total dos Débitos por Saídas e Prestações     

    da UF favorecida, de acordo com o período preenchido na tela de Geração e Estabelecimento selecionado\.

Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração do ICMS Dif\. Aliq\. UF Origem/Destino \(EC 87/15\), aba Guias de Recolhimento;

Específicos >> PIM \- Gestão do Controle de Incentivos Fiscais do Polo Industrial de Manaus >> Apuração >> Apuração dos Saldos de Impostos e Taxas >> Lançamentos Complementares >> Apuração do ICMS Dif\. Aliq\. UF Origem/Destino \(EC 87/15\), aba Guias de Recolhimento\.

Preencher com a soma dos valores informados no campo “Valor” para cada UF Favorecida processada, quando o campo “Código Obrigação” for igual a 000, de acordo com o período preenchido na tela de Geração e Estabelecimento selecionado\.

*Observações: *

- Considerar a soma dos valores informados o valor informado de uma das tabelas da guia de recolhimento Apuração do ICMS Dif\. Aliq\. UF Origem/Destino \(EC 87/15\): do módulo ICMS ou do módulo PIM; conforme determina a origem da informação;
- Só serão consideradas as informações do módulo PIM quando o campo “Tipo de Apuração do ICMS utilizada no Mastersaf” da tela Empresa/ Estabelecimento, localizada no módulo Básicos – Parâmetros >> Preliminares >> Empresa/ Estabelecimento \(aba Informações Específicas\), for igual a 4;
- No módulo PIM, mesmo os lançamentos sendo feitos por Inscrição Estadual, ou seja, um estabelecimento pode ter mais de uma Inscrição Estadual por incentivo, a recuperação na GIA\-ST será por UF favorecida, então os valores serão consolidados mesmo se tiverem cadastrados com Inscrições Estaduais diferentes\.

Origem Campo: 221 \- Valor FCP UF Destino\-VLR\_FCP\_UF\_DEST da tabela SAFX08

__MFS2283__

__MFS4524__

__CH21316\_2016__

__MFS27837__

__RN32__

Campo __Informações EC 87/15 – Devoluções ou Anulações:__

__\[MFS536852\] __Inclusão do valor do FCP no cálculo do valor de devolução ou anulação\.

__\[MFS585734\] __Alteração da regra para considerar o valor do FCP no cálculo do valor de devolução somente para a UF=RJ, conforme alinhamento com a área de informação

__Origem:__ SAFX04/07/08 e tabela da “Apuração ICMS Difal UF Orig/Dest”

Se a UF favorecida = “RJ”

     Preencher com a soma dos valores informados no campo “Valor ICMS UF Origem”, no campo “Valor ICMS UF Destino” e 

     no campo “Valor FCP UF Destino”, mais o valor do saldo credor do período anterior, de acordo com a RN00 para 

     Devoluções ou Anulações EC 87/15 de acordo com a UF Favorecida ao período estipulado

Senão

     Preencher com a soma dos valores informados no campo “Valor ICMS UF Origem” e no campo “Valor ICMS UF Destino”,   

    mais o valor do saldo credor do período anterior, de acordo com a RN00 para Devoluções ou Anulações EC 87/15 de     

    acordo com a UF Favorecida ao período estipulado\.

Este campo corresponde ao “retorno de mercadoria”, que seria uma operação de devolução, só que, como o destinatário seria no caso um não contribuinte, ele não emite nota, e assim, a nota para a devolução da mercadoria seria emitida pelo próprio vendedor\.

__MFS2283__

__MFS30017__

__MFS536852__

__RN33__

Campo __Informações EC 87/15 – Pagamentos Antecipados:__

Esse campo será preenchido manualmente pelo usuário\.

__MFS2283__

__RN34__

Campo __Informações EC 87/15 – Total ICMS Devido à UF de Destino:__

Preencher com o resultado do campo Valor ICMS Devido à UF de Destino deduzidos os valores de Devoluções ou Anulações e Pagamentos Antecipados\.

__\[ALTERADA – CH7697\_2016\]__

__Tratamento:__

Quando o valor for negativo, zerar o preenchimento\.

__Atenção:__ 

O campo Pagamentos Antecipados será deduzido no resultado apenas na manutenção quando for preenchido\.

Este campo corresponde ao Valor do ICMS Devido informado no Anexo IV – EC 87/15\.

__MFS2283__

__CH7697\_2016__

__RN35__

Campo __Informações EC 87/15 – Total ICMS FCP:__

__\[ALTERADA – MFS4524\]__

__\[MFS69962\] Alteração de regra para preenchimento para a UF=RJ__

\[MFS35443\]: Preenchimento do Anexo IV da GIA ST através da GNRE Online\.

__\[MFS585734\] __Alteração da regra para UF=RJ, para considerar o valor a recolher do FECP do resultado da apuração do EC87/15\.

__Origem – UF <> ”RJ”:__ 

Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração do ICMS Dif\. Aliq\. UF Origem/Destino \(EC 87/15\), aba Guias de Recolhimento;

__MFS35443__

GNRE Online:

Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Recolhimento Tributos Estaduais \(GNRE Online\)  >> Manutenção;

Específicos >> PIM \- Gestão do Controle de Incentivos Fiscais do Polo Industrial de Manaus >> Apuração >> Apuração dos Saldos de Impostos e Taxas >> Lançamentos Complementares >> Apuração do ICMS Dif\. Aliq\. UF Origem/Destino \(EC 87/15\), aba Guias de Recolhimento\.

__Origem – UF = ”RJ”:__ 

Estadual >> ICMS >> DATA MART >> Apuração do ICMS >> Ajuste SINIEF \(quando o parâmetro “91 \- Apuração ICMS Dif\.Alíquota UF Orig/Dest \- EC 87/15” da parametrização por UF do Módulo ICMS estiver selecionada para a UF favorecida a ser gerada\);

Específicos >> PIM \- Gestão do Controle de Incentivos Fiscais do Polo Industrial de Manaus >> Apuração >> Apuração dos Saldos de Impostos e Taxas >> Lançamentos Complementares >> Apuração do ICMS Dif\. Aliq\. UF Origem/Destino \(EC 87/15\) \(quando o parâmetro “91 \- Apuração ICMS Dif\.Alíquota UF Orig/Dest \- EC 87/15” da parametrização por UF do Módulo ICMS estiver selecionada para a UF favorecida a ser gerada\)\.

Se a UF favorecida = “RJ”

     Preencher com o conteúdo do campo gerado para o valor a Recolher do FCP da UF favorecida, de acordo com o período    

     preenchido na tela de Geração e Estabelecimento selecionado

Senão

    Considerar a Guias de Recolhimento dos Lançamentos Complementares: 

Preencher com a soma dos valores informados no campo “Valor” para cada UF Favorecida processada, quando o campo “Código Obrigação” for igual a 006, de acordo com o período preenchido na tela de Geração e Estabelecimento selecionado\.

    Considerar as Guias da GNRE Online, caso não exista Guia dos Lançamentos Complementares:

Preencher com a soma dos valores informados no campo “Valor Total”, se preenchido \(se não preenchido considerar o campo “Valor Principal”\), para cada UF Favorecida processada, quando o “Código de Receita” for __100129 ou 100137 __e o campo “Apuração Ref\.” = “2”, de acordo com o período preenchido na tela de Geração e Estabelecimento selecionado\.

*Observações: *

- Considerar a soma dos valores informados na guia de recolhimento: do módulo ICMS ou do módulo PIM; conforme determina a origem da informação;
- Só serão consideradas as informações do módulo PIM quando o campo “Tipo de Apuração do ICMS utilizada no Mastersaf” da tela Empresa/ Estabelecimento, localizada no módulo Básicos – Parâmetros >> Preliminares >> Empresa/ Estabelecimento \(aba Informações Específicas\), for igual a 4;
- No módulo PIM, mesmo os lançamentos sendo feitos por Inscrição Estadual, ou seja, um estabelecimento pode ter mais de uma Inscrição Estadual por incentivo, a recuperação na GIA\-ST será por UF favorecida, então os valores serão consolidados mesmo se tiverem cadastrados com Inscrições Estaduais diferentes\.

__MFS2283__

__MFS4524__

__CH22963\_2017 \(MFS\-15149\)__

__MFS69962__

__Saída para aba Anexo I – Devolução__

	

__Cód\.__

__Descrição__

__DR__

__RN01__

Campo__ Vlr\. ICMS – ST Devolução:__

Esse campo deverá ser preenchido pelo Substituto Tributário com o somatório do ICMS ST das notas fiscais de Devolução de Entrada \(Quando o campo NORM\_DEV da SAFX07 for igual a ‘2’\)\.

__Tratamento:__

Se o campo VLR\_SUBST\_ICMS da SAFX08 não estiver preenchido, preencher com o campo VLR\_ICMS\_ORIGDEST da SAFX08 de acordo com a UF de Origem/Destino para considerar corretamente a respectiva UF parametrizada na GIA\-ST\. 

Senão preencher com zero\.

__MFS11377__

__MFS 1016914__

__Saída para aba Registro Anexo IV – EC 87/15__

__Cód\.__

__Descrição__

__DR__

__RN00__

__Regra Geral Anexo IV – EC 87/15__:

__\[ALTERADA – CH2215\_2016\]__

A geração desse anexo independe se existem valores de ICMS\-ST a serem declarados na GIA, então quando o campo GIA Sem Movimento estiver marcado ou não devem ser considerados os valores de diferencial de alíquota que competem a EC 87/2015\.

Esse Anexo deverá ser agrupado por UF e pelas datas de vencimento do ICMS Devido e do ICMS FCP\.

__MFS2283__

__CH2215\_2016__

__RN01__

Campo __Data de Vencto do ICMS Devido à UF de Destino:__

__\[MFS35443\]__: Preenchimento do Anexo IV da GIA ST através da GNRE Online\.

__\[MFS564378\]__ Inclusão do código da obrigação 020 \(ICMS – Diferença de Aliquota EC87/2015\)

__\[ALTERADA – MFS4524\]__

__Origem:__ 

Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração do ICMS Dif\. Aliq\. UF Origem/Destino \(EC 87/15\), aba Guias de Recolhimento;

__MFS35443__

GNRE Online:

Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Recolhimento Tributos Estaduais \(GNRE Online\)  >> Manutenção;

Específicos >> PIM \- Gestão do Controle de Incentivos Fiscais do Polo Industrial de Manaus >> Apuração >> Apuração dos Saldos de Impostos e Taxas >> Lançamentos Complementares >> Apuração do ICMS Dif\. Aliq\. UF Origem/Destino \(EC 87/15\), aba Guias de Recolhimento\.

Considerar a Guias de Recolhimento dos Lançamentos Complementares:

Preencher com o conteúdo do campo “Data Vencimento” para cada UF Favorecida processada, quando o campo “Código Obrigação” for igual a “000” ou “020”, de acordo com o período preenchido na tela de Geração e Estabelecimento selecionado\.

Considerar as Guias da GNRE Online, caso não exista Guia dos Lançamentos Complementares:

Preencher com o conteúdo do campo “Data Vencimento” para cada UF Favorecida processada, quando o “Código de Receita” for __100102 ou 100110__, de acordo com o período preenchido na tela de Geração e Estabelecimento selecionado\.

*Observações: *

- Considerar a soma dos valores informados de uma das tabelas da guia de recolhimento: do módulo ICMS ou do módulo PIM; conforme determina a origem da informação;
- Só serão consideradas as informações do módulo PIM quando o campo “Tipo de Apuração do ICMS utilizada no Mastersaf” da tela Empresa/ Estabelecimento, localizada no módulo Básicos – Parâmetros >> Preliminares >> Empresa/ Estabelecimento \(aba Informações Específicas\), for igual a 4;
- No módulo PIM, mesmo os lançamentos sendo feitos por Inscrição Estadual, ou seja, um estabelecimento pode ter mais de uma Inscrição Estadual por incentivo, a recuperação na GIA\-ST será por UF favorecida, então os valores serão consolidados mesmo se tiverem cadastrados com Inscrições Estaduais diferentes\.

__MFS2283__

__MFS4524__

__MFS564378__

__RN02__

Campo __Valor do ICMS Devido:__

\[MFS35443\]: Preenchimento do Anexo IV da GIA ST através da GNRE Online\.

__\[MFS564378\]__ Inclusão do código da obrigação 020 \(ICMS – Diferença de Aliquota EC87/2015\)

__\[MFS585734\] __Alteração da regra de geração dos dados a partir da GNRE Online, para UF=RJ, para considerar o valor  FECP\.  Alteração necessária para igualar a regra desse campo com o campo “Total ICMS Devido à UF de Destino” do Registro Principal\.

__\[ALTERADA – MFS4524\]__

__Origem:__ 

Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração do ICMS Dif\. Aliq\. UF Origem/Destino \(EC 87/15\), aba Guias de Recolhimento;

__MFS35443__

GNRE Online:

Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Recolhimento Tributos Estaduais \(GNRE Online\)  >> Manutenção;

Específicos >> PIM \- Gestão do Controle de Incentivos Fiscais do Polo Industrial de Manaus >> Apuração >> Apuração dos Saldos de Impostos e Taxas >> Lançamentos Complementares >> Apuração do ICMS Dif\. Aliq\. UF Origem/Destino \(EC 87/15\), aba Guias de Recolhimento\.

Se a UF favorecida <> “RJ”

         Considerar a Guias de Recolhimento dos Lançamentos Complementares:

Preencher com a soma dos valores informados no campo “Valor” para cada UF Favorecida processada, quando o campo “Código Obrigação” for igual a “000” ou “020”, de acordo com o período preenchido na tela de Geração e Estabelecimento selecionado

        Considerar as Guias da GNRE Online, caso não exista Guia dos Lançamentos Complementares:

Preencher com a soma dos valores informados no campo “Valor Total”, se preenchido \(se não preenchido considerar o campo “Valor Principal”\), para cada UF Favorecida processada, quando o “Código de Receita” for __100102 ou 100110__, de acordo com o período preenchido na tela de Geração e Estabelecimento selecionado\.

Senão \(UF=RJ\)

         Considerar a Guias de Recolhimento dos Lançamentos Complementares do ICMS e do FECP:

Preencher com a soma dos valores informados no campo “Valor” para cada UF Favorecida processada, quando o campo “Código Obrigação” for igual a “000” ou “020” ou “006” \(FECP\), de acordo com o período preenchido na tela de Geração e Estabelecimento selecionado

         Considerar as Guias da GNRE Online, caso não exista Guia dos Lançamentos Complementares:

 Preencher com a soma dos valores informados no campo “Valor GNRE” \(Valor GNRE = Valor Total FECP \+ Valor Total\), para a UF Favorecida processada, quando o “Código de  Receita” for __100102 ou 100110__ e o campo “Apuração Ref\.” = “2”, de acordo com o período preenchido na tela de Geração e Estabelecimento selecionado\.

*Observações: *

- Considerar a soma dos valores informados de uma das tabelas da guia de recolhimento: do módulo ICMS ou do módulo PIM; conforme determina a origem da informação;
- Só serão consideradas as informações do módulo PIM quando o campo “Tipo de Apuração do ICMS utilizada no Mastersaf” da tela Empresa/ Estabelecimento, localizada no módulo Básicos – Parâmetros >> Preliminares >> Empresa/ Estabelecimento \(aba Informações Específicas\), for igual a 4;
- No módulo PIM, mesmo os lançamentos sendo feitos por Inscrição Estadual, ou seja, um estabelecimento pode ter mais de uma Inscrição Estadual por incentivo, a recuperação na GIA\-ST será por UF favorecida, então os valores serão consolidados mesmo se tiverem cadastrados com Inscrições Estaduais diferentes\.

Este campo corresponde ao Total ICMS Devido à UF de Destino informado no Registro Principal\.

__\[EXCLUIDA \- CH21316\_2016\]__

__\[ALTERADA – CH7697\_2016\]__

__Tratamento Dedução Notas de Devolução:__

Na validação da GIA\-ST só é considerada uma Data de Vencto do ICMS Devido à UF de Destino, então mesmo quando existem vários registros com datas diferentes, ele totaliza o valor desses registros considerando a primeira data, do primeiro registro inserido no Anexo IV\. Com isso, a soma deve corresponder ao Total ICMS Devido à UF de Destino do Anexo Principal\. 

Então, no nosso sistema, que reflete exatamente o validador, deverá seguir a seguinte condição:

- Quando há notas fiscais de devolução no período da apuração que está sendo processada, o valor é totalizado para a aba principal, esse valor deverá ser deduzido do valor do ICMS devido referente à menor data de vencimento do ICMS devido: \(valor do ICMS devido \- valor de devolução\), se o valor da devolução for maior que o valor do ICMS devido, ele deverá zerar o valor para aquele vencimento e partir para deduzir o restante do próximo vencimento\.

*Exemplo 1:*

__Anexo 4__

Data de Vencto do ICMS Devido à UF de Destino: 15/05/2016 Valor do ICMS Devido = R$100 \- R$56 __= R$44__

Data de Vencto do ICMS Devido à UF de Destino: 16/05/2016 Valor do ICMS Devido __= R$100__

__Anexo Principal__

Valor do ICMS Devido = R$200

Devoluções ou Anulações = R$56

Total ICMS Devido à UF de Destino __= R$144__

*Exemplo 2:*

__Anexo 4__

Data de Vencto do ICMS Devido à UF de Destino: 15/05/2016 Valor do ICMS Devido = R$100 \- R$100 __= R$0__

Data de Vencto do ICMS Devido à UF de Destino: 16/05/2016 Valor do ICMS Devido = R$100 \- R$20 __= R$80__

Data de Vencto do ICMS Devido à UF de Destino: 16/05/2016 Valor do ICMS Devido __= R$100__

__Anexo Principal__

Valor do ICMS Devido = R$300

Devoluções ou Anulações = R$120

Total ICMS Devido à UF de Destino __= R$180__

*Ponto de atenção:* Está previsto no validador que a devolução quando for maior que o Valor do ICMS Devido à UF de Destino deverá gravar zero

__MFS2283__

__CH7697\_2016__

__MFS4524__

__CH21316\_2016__

__MFS564378__

__MFS585734__

__RN03__

Campo __Data de Vencimento FCP:__

\[MFS35443\]: Preenchimento do Anexo IV da GIA ST através da GNRE Online\.

\[__MFS569593__\] Alteração da regra de geração dos dados a partir da GNRE Online, para UF=RJ, para passar a considerar as receitas __100102 ou 100110, __que vão ser utilizadas para gerar o valor de FECP

__\[ALTERADA – MFS4524\]__

__Origem:__ 

Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração do ICMS Dif\. Aliq\. UF Origem/Destino \(EC 87/15\), aba Guias de Recolhimento;

__MFS35443__

GNRE Online:

Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Recolhimento Tributos Estaduais \(GNRE Online\)  >> Manutenção;

Específicos >> PIM \- Gestão do Controle de Incentivos Fiscais do Polo Industrial de Manaus >> Apuração >> Apuração dos Saldos de Impostos e Taxas >> Lançamentos Complementares >> Apuração do ICMS Dif\. Aliq\. UF Origem/Destino \(EC 87/15\), aba Guias de Recolhimento\.

Considerar a Guias de Recolhimento dos Lançamentos Complementares:

Preencher com o conteúdo do campo “Data Vencimento” para cada UF Favorecida processada, quando o campo “Código Obrigação” for igual a 006, de acordo com o período preenchido na tela de Geração e Estabelecimento selecionado\.

Considerar as Guias da GNRE Online, caso não exista Guia dos Lançamentos Complementares:

Se a UF favorecida <> “RJ”

Preencher com o conteúdo do campo “Data Vencimento” para cada UF Favorecida processada, quando o “Código de Receita” for __100129 ou 100137 __e o campo “Apuração Ref\.” = “2”, de acordo com o período preenchido na tela de Geração e Estabelecimento selecionado\.

Senão \(UF=RJ\)

             Se houver guias com “Código de Receita” for __100129 ou 100137 __e o campo “Apuração Ref\.” = “2”

      Preencher com o conteúdo do campo “Data Vencimento” para cada UF Favorecida processada, quando o 

     “Código de Receita” for __100129 ou 100137 __e o campo “Apuração Ref\.” = “2”, de acordo com o período preenchido 

      na tela de Geração e__ __Estabelecimento selecionado

Senão

      Preencher com o conteúdo do campo “Data Vencimento” para a UF Favorecida processada, quando o “Código 

     de Receita” for __100102 ou 100110__ e o campo “Apuração Ref\.” = “2”, de acordo com o período preenchido na tela 

     de Geração e Estabelecimento selecionado\.

*Observações: *

- Considerar a soma dos valores informados de uma das tabelas da guia de recolhimento: do módulo ICMS ou do módulo PIM; conforme determina a origem da informação;
- Só serão consideradas as informações do módulo PIM quando o campo “Tipo de Apuração do ICMS utilizada no Mastersaf” da tela Empresa/ Estabelecimento, localizada no módulo Básicos – Parâmetros >> Preliminares >> Empresa/ Estabelecimento \(aba Informações Específicas\), for igual a 4;
- No módulo PIM, mesmo os lançamentos sendo feitos por Inscrição Estadual, ou seja, um estabelecimento pode ter mais de uma Inscrição Estadual por incentivo, a recuperação na GIA\-ST será por UF favorecida, então os valores serão consolidados mesmo se tiverem cadastrados com Inscrições Estaduais diferentes\.

__MFS2283__

__MFS4524__

__MFS569593__

__RN04__

Campo __Valor do ICMS FCP:__

\[MFS35443\]: Preenchimento do Anexo IV da GIA ST através da GNRE Online\.

\[__MFS569593__\] Alteração da regra de geração dos dados a partir da GNRE Online, para UF=RJ, para passar a considerar as receitas __100102 ou 100110, __que vão ser utilizadas para gerar o valor de FECP

__\[ALTERADA – MFS4524\]__

__Origem:__

Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração do ICMS Dif\. Aliq\. UF Origem/Destino \(EC 87/15\), aba Guias de Recolhimento;

__MFS35443__

GNRE Online:

Estadual >> ICMS >> Apuração >> Guias de Recolhimento >> Guia de Recolhimento Tributos Estaduais \(GNRE Online\)  >> Manutenção;

Específicos >> PIM \- Gestão do Controle de Incentivos Fiscais do Polo Industrial de Manaus >> Apuração >> Apuração dos Saldos de Impostos e Taxas >> Lançamentos Complementares >> Apuração do ICMS Dif\. Aliq\. UF Origem/Destino \(EC 87/15\), aba Guias de Recolhimento\.

Considerar a Guias de Recolhimento dos Lançamentos Complementares:

Preencher com a soma dos valores informados no campo “Valor” para cada UF Favorecida processada, quando o campo “Código Obrigação” for igual a 006, de acordo com o período preenchido na tela de Geração e Estabelecimento selecionado\.

Considerar as Guias da GNRE Online, caso não exista Guia dos Lançamentos Complementares:

      Se a UF favorecida <> “RJ”

Preencher com a soma dos valores informados no campo “Valor Total”, se preenchido \(se não preenchido considerar o campo “Valor Principal”\), para cada UF Favorecida processada, quando o “Código de Receita” for __100129 ou 100137 __e o campo “Apuração Ref\.” = “2”, de acordo com o período preenchido na tela de Geração e Estabelecimento selecionado

      Senão \(UF=RJ\)

             Se houver guias com “Código de Receita” for __100129 ou 100137 __e o campo “Apuração Ref\.” = “2”

      Preencher com a soma dos valores informados no campo “Valor Total”, se preenchido \(se não preenchido    

      considerar o campo “Valor Principal”\), para cada UF Favorecida processada, quando o “Código de Receita” for 

__      100129 ou 100137 __e o campo “Apuração Ref\.” = “2”, de acordo com o período preenchido na tela de Geração e         

__      __Estabelecimento selecionado

Senão

      Preencher com a soma dos valores informados no campo “Valor Total FECP”, se preenchido \(se não preenchido    

      considerar o campo “Valor Principal FECP”\), para a UF Favorecida processada, quando o “Código de 

      Receita” for __100102 ou 100110__ e o campo “Apuração Ref\.” = “2”, de acordo com o período preenchido na tela de 

      Geração e Estabelecimento selecionado\.

*Observações: *

- Considerar a soma dos valores informados de uma das tabelas da guia de recolhimento: do módulo ICMS ou do módulo PIM; conforme determina a origem da informação;
- Só serão consideradas as informações do módulo PIM quando o campo “Tipo de Apuração do ICMS utilizada no Mastersaf” da tela Empresa/ Estabelecimento, localizada no módulo Básicos – Parâmetros >> Preliminares >> Empresa/ Estabelecimento \(aba Informações Específicas\), for igual a 4;
- No módulo PIM, mesmo os lançamentos sendo feitos por Inscrição Estadual, ou seja, um estabelecimento pode ter mais de uma Inscrição Estadual por incentivo, a recuperação na GIA\-ST será por UF favorecida, então os valores serão consolidados mesmo se tiverem cadastrados com Inscrições Estaduais diferentes\.

Este campo corresponde ao Total ICMS FCP de Destino informado no Registro Principal\.

__MFS2283__

__MFS4524__

__MFS69962__

__MFS569593__

