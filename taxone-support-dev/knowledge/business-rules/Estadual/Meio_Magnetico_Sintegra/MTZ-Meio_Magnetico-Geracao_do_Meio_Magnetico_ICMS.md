# MTZ-Meio_Magnetico-Geracao_do_Meio_Magnetico_ICMS

- **Fonte:** MTZ-Meio_Magnetico-Geracao_do_Meio_Magnetico_ICMS.docx
- **Modificado:** 2023-11-08
- **Tamanho:** 327 KB

---

# Meio Magnético – Geração do Meio Magnético ICMS

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__OS2600/ CH6875\_2012__

Gerar Registros Tipo SME e SMS para Minas Gerais

Correção na geração dos Registros Tipo SME e SMS para contemplar o Registro 70 \(CTRC\)

Gerar os Registros 88\-SME e 88\-SMS para períodos sem movimentação de Estabelecimentos de Minas Gerais\.

Correção na geração dos Registros Tipo SME e SMS para contemplar o Registro 70 \(CTRC\) 

__OS2708__

Meio Magnético – Geração do Meio Magnético

Criação de um parâmetro chamado “Gerar Número de Item com base no Número de Item dos documentos fiscais”\.

__OS2811__

Meio Magnético – Geração do Meio Magnético

Tratamento específico do Registro 88STES para o Estado de Minas Gerais\.

__OS2850__

Meio Magnético – Geração do Meio Magnético

Tratamento específico do Registro 88STES e 88STITNF para o Estado de Minas Gerais\.

__OS2864__

Meio Magnético – Geração do Meio Magnético

Geração do Registro 54 para as NFs de Entrada Modelo “06”

__CH69942__

Geração do Meio Magnético

Alterar a geração do Meio Magnético para que os CFOP’s de anulação gerem apenas o registro 50\.

__CH74417__

Não gerar Registro 54 para Documentos Fiscais de Entrada cujo código do modelo = 21

Permitir que o SINTEGRA não gere o registro 54 cujo Documentos Fiscais de Entrada possuam código do modelo = 21

__OS30002__

Geração dos registros 88STES e 88STITNF

Revisão nas regras de geração\.

__CH78184__

Geração do registro 54, itens 991\(Frete\) e 992 \(Seguro\)\.

Geração dos itens 991 \(Frete\) e 992 \(Seguro\) do registro 54 a partir dos valores informados na capa da nota\.

__CH77317__

Não gerar o registro 54 para as notas de entrada modelo = 22

Permitir que o SINTEGRA não gere o registro 54 cujo Documentos Fiscais de Entrada possuam código do modelo = 21 ou 22

__CH64607\-A__

DW \- ESTADUAL \- MEIO MAGNETICO \- Erro na recuperação das notas para composição do registro 88STITNF

Alteração na rotina de geração dos registros 88STITNF para que seja limitado o período de pesquisa das notas de entrada dos produtos para composição do estoque inicial\. \(RN29\)

__CH82260__

Alteração no preenchimento dos registros tipo 10 e tipo 11\.

Alteração para gravar o DDD \+ número do telefone no campo FAX do registro tipo 10 e no campo TELEFONE do registro tipo 11\.

__CH82459__

Alteração na geração do registro tipo 54\.

Ajuste na geração do registro tipo 54 para atendimento a CAT32/96\.

__OS3097\-C__

Creditar Valor de ICMS\-ST para a UF da Concessionárias nas operações de veículos novos \(Convênio ICMS 51/00\)

- Creditar valor de ICMS\-ST para a UF da Concessionária no registro do tipo 53 – Substituição Tributária para a seguinte obrigação:
	- SINTEGRA \(módulo: Meio Magnético\)
- Exclusão das funcionalidades para efeitos de crédito do ICMS\-ST para a UF de Destino, presentes no parâmetro “67 – Lançar Campo UF Origem/Destino do Documento Fiscal nos Livros Fiscais \(Movimentos/Resumos por UF\)” na tela de Parâmetros por UF do módulo ICMS\.
	- SINTEGRA \(módulo: Meio Magnético\)

__CH64607\-B__

Ajuste na geração do Registro STITNF

Ajuste na geração do Registro STITNF

__CH82194__

Ajuste na geração do Registro 54

Ajuste na geração do Registro 54 em relação as notas complementares\.

__CH85409__

Ajuste na geração das NF’s Modelo 06

Parametrizar geração das NF’s modelo 06 no registro 54 e demais filhos\.

__CH79588\-A__

Ajuste Registro 85

Ajustar Registro 85, quando o registro de exportação for DS ou IS

__OS2937__

Pepsico \- Parametrização de CFOP x UF

Este documento tem como objetivo criar o novo módulo que permita a parametrização de CFOP’s por UF especificamente para o cliente Pepsico para tratamento de regime especial nas Ufs\. \(ver __RN35__, __RN44\-A__, __RN45\-A__ e __RN46\-A__\) 

__CH88198__

Ajustar geração do Registro 54 especial para seqüencial 999

Ajustar geração do Registro 54 especial para seqüencial 999

__CH92305\-A/ CH118186__

Ajuste na geração do Registro 50

Ajuste na geração do Registro 50 em relação às notas de transferência de saldo ICMS

Ajuste da regra para SP e RJ

__OS3038__

Ajuste Registro 53

Considerar o campo UF origem/destino do documento fiscal na geração do Meio Magnético – Registro 53

__OS3229__

Alteração no critério de seleção dos registros do Tipo 56 – Veículos Novos

Alteração no parâmetro dos registros do Tipo 56 e criado um novo parâmetro por Extensão de CFOP\.

__CH110164\-A__

Ajuste na geração do Registro 70

Ajuste na geração do Registro 70

__CH111796__

Ajuste na geração do Registro Tipo 60A

Ajuste na geração do Registro Tipo 60A

__CH112538__

Ajuste Registro 53 – ICMS\-S não apropriado

Considerar o valor do ICMS\-S para quando o documento fiscal possuir o código de antecipação igual á “4 \- Antecipação tributária com MVA \(Margem de Valor Agregado\), efetuada pelo destinatário encerrando a fase de tributação”\.

__OS3531__

Novo Código de Tipo de Receita

Novo código de Tipo de Receita para os Registros 76 e 77\.

__CH109989__

Considerar o Parâmetro 67 na geração do registro 50

Considerar o Parâmetro 67 na geração do registro 50

__CH5271\_2012__

Considerar CNPJ da concessionária para geração do registro tipo 56

Considerar CNPJ da concessionária para geração do registro tipo 56

__OS3690__

Geração do Registro 88\-11da DIC\-SE

Geração do Registro 88\-11da DIC\-SE \(ver __RN55__\)

__CH17462__

IE Amazonas

Ajuste na geração do Registro 74

__CH21224\_2012__

Geração do Registro 88\-02 MS

Geração do Registro 88\-02 MS	

__OS3520__

Alteração na geração do registro tipo 55

Alteração na geração do registro tipo 55 para considerar as guias da opção “GNRE Online”  __\(vide RN58\)__

__CH35852\-A/2012__

Alteração na geração do registro tipo 54

Ajuste na RN44 para geração do item 999 do registro 54\.

__CH13910\_2013__

Alteração na geração do registro tipo 50

Ajuste na geração do registro tipo 50 para gerar de acordo com a combinação CFOP/Alíquota dos itens do documento fiscal\.

__OS3774__

Utilização do parâmetro para a geração do Registro 54, quando estabelecimento for RJ

Utilização do parâmetro para a geração do Registro 54, quando estabelecimento for RJ

__CH8984\_2013__

Utilização do parâmetro para a geração do Registro 54, quando estabelecimento for RJ

Complemento da OS3774 com a inclusão dos CFOP’s de importação\.

__CH10037\_2013__

Tratamento nos registros 61 e 61R

Ajuste no agrupamento dos registros 61 e 61R\.

__CH19583\-A\_2013__

Alteração pelo Convênio ICMS 73/2013

Alteração campo Número Inicial de Ordem registro 61\.

__CH28466\_2013__

Tratamento campo 09 do Registro Tipo 55

Tratamento no campo 09 \(Número GNRE\) do Registro 55 para considerar sempre 20 posições tanto pela GNRE normal quanto pela GNRE ONLINE\.

__OS4195__

Tratamento campo 09 do Registro Tipo 55

Ajuste no tratamento no campo 09 \(Número GNRE\) do Registro 55 para considerar sempre 20 posições na GNRE normal, por Grupo/Convênio e Online\.

__CH1063\_2014__

Tratamento Registro Tipo 88E e Tipo 75

<a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>Ajuste no tratamento para geração do Registro Tipo 75 quando houver a geração do Registro Tipo 88E\.

__OS4635__

Meio Magnético – Geração do Meio Magnético

Geração do registro 88 L36451 – RJ

__OS4666__

Atendimento regime especial Pepsico

Possibilitar a geração do arquivo apenas c/as notas *não* escrituradas\.

\(ver __RN35__, __RN44\-A__, __RN45\-A__ e __RN46\-A__\)

__CH23172\_2014__

Tratamento Registro Tipo 51

Este documento tem como objetivo tratar a geração do Registro Tipo 51 para desconsiderar notas fiscais de modelo 55 com a natureza de operação de Anulação de Valores não tributados pelo IPI\.

__CH10664\_2015__

Tratamento Registro Tipo 61 E 61R

Este documento tem como objetivo especificar todos os modelos de documentos fiscais que deverão compor a geração os Registros Tipo 61 E 61R\.

__CH18474\_2015__

Alteração Registro Tipo 50 e Registro Tipo 61

Este documento tem como objetivo atender o “Comunicado n° 003/2015 de 10 de agosto de 2015” da SEFAZ/PI para modelo de documento 65\-NFC\-e\.

__CH12009\_2016__

Atendimento Decreto nº 46\.614

Este documento tem como objetivo alterar a geração do tamanho do campo “05\-Código do Produto” do Registro Tipo “88STES” e do tamanho dos campos “06\-Número” e “05\-Código do Produto” do Registro Tipo “88STITNF”, em atendimento ao Decreto nº 46\.614 referente ao arquivo magnético SINTEGRA do estado de Minas Gerais\.

__MFS8012\(CH23671\)__

Tratamento registro 55

Somente considerar registro com valor GNRE maior do que zero

MFS9038

\(ch 222/17\)

Alteração registro 88STITNF \(MG\)

Alteração registro 88STITNF \(MG\)\. Ver __RN29__\.

__CH1674\_2017/__

__MFS9404__

Alteração Registro 88STITNF

Considerar NF sem saldo anterior para o registro 88STITNF

__CH27464\_2016__

Alteração registro 88STITNF \(MG\)

Alteração registro 88STITNF \(MG\), campo 15 \- Base Cálculo do ICMS OP\. Ver RN29\.

__CH7865\_2017 \(MFS\-10879\)__

Alteração Registro Tipo 61

Este documento tem como objetivo alterar o preenchimento do campo de valores para desconsiderar documento fiscal cancelado\.

__MFS11800__

Alteração Registro Tipo 50

Este documento tem como objetivo alterar o preenchimento do campo CNPJ do Registro Tipo 50 para considerar CPF/CNPJ do consumidor \(NF modelo 65\)\.

__MFS15533__

Alteração Registro Tipo 61 e Tipo 70

Inclusão de novos modelos de documento nos registros Tipo 61 e Tipo 70\.

__CH10233\_2018 \(MFS\-18513\)__

Alteração do Registro Tipo 88STES

Este documento tem como objetivo alterar a geração do Registro Tipo 88STES ajustando o cálculo multiplicador dos campos 7 e 8 com o campo 6\. 

__MFS20115__

Alteração Registros 88STES e 88STITNF

Alteração da geração do Meio Magnético dos Registros 88STES e 88STITNF para tratar a mudança na forma de tributação\.

__MFS22719__

Alteração Registro 88STITNF

Alteração da geração do registro 88STITNF para a inclusão do novo campo “20\-Chave da NF\-e” \(ver __RN29__\)\.

__MFS\-23075__

Alteração Registro Tipo 70

Este documento tem como objetivo alterar a geração do Registro Tipo 70 para considerar a subsérie com as duas últimas posições da série do documento de modelo 57 e modelo 67\.

__MFS\-24464__

Alteração no registro 88 STITNF\.

RN29: alteração no registro 88 STITNF – campo 18 \- Alíquota – ICMS Operação Própria\.

__MFS27453__

Alteração no registro 88 STITNF\.

Alteração da regra de recuperação do registro, passando a utilizar o campo Base ICMS Substituição Tributária\.

__MFS28851__

Alteração Registros 88STES e 88STITNF

Alteração nas RN28, RN29, passar a considerar a parametrização por código de produto\.

__MFS\-32219__

Alteração Registro 88STITNF

Alteração na __RN29__, passar não considerar mais a existência de notas de notas de saídas de produtos sujeitos a ST, como critério de recuperação das notas de entradas, para gerações a partir de 01/03/2019\. A partir desta data, a recuperação das entradas de produtos sujeitos a ST independente de existir notas de saídas desses produtos no período da geração\.

\[__MFS58872__\]

Alteração Registro Tipo 50, Campo 17 – Situação\. DIEF\-MA

Alteração na __RN59, __quando se tratar de uma nota fiscal cancelada, independente se for cancelada e denegada/ou inutilizada, o campo 17 – Situação deverá ser preenchido com “S”, conforme regra de preenchimento do reg\.50, em relação as __notas canceladas__, conforme manual do Sintegra disponibilizado no Portal do Maranhão: 

Deve ser informado um Registro 50 com as informações da Nota Fiscal, ou seja, o campo 06\(Modelo\), 07\(Série\), 08\(Subsérie\) e 09\(Número da NF\)\. Os demais campos devem ser preenchidos com zeros\(numéricos\) ou brancos/espaços\(alfanuméricos\) __e o campo 17 \(Situação\) com “S”\.__

__MFS32268__

Tratamento de Nota de Entrada Cancelada

Alteração na RN69 para considerar o novo parâmetro “Não Gerar Notas de Entrada Canceladas de Emissão Própria”

__MFS87116__

Alteração Registro 88STITNF

Alteração na __RN29__, passar a considerar a existência de cupom fiscal, além das notas de saídas de produtos sujeitos a ST, como critério de recuperação das notas de entradas, para gerações anteriores à 01/03/2019\. A partir desta data, será feita a recuperação das entradas de produtos sujeitos a ST, independente de existir notas de saídas desses produtos no período da geração\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Os Registros 88SME e 88SMS deverão ser gerados com o layout contido no Requisito da OS, para Estabelecimentos de Minas Gerais \(os registros 88SME e 88SMS de Mato Grosso do Sul continuam a ser gerados da forma como estão hoje\. Os mesmos possuem layout diferente\)\.

__OS2600__

__RN01__

Caso não existam dados de documentos fiscais de entrada no período utilizado para o estabelecimento de MG, deverá ser gerado automaticamente o registro “88SME”, conforme “De – Para” especificado no Documento de Requisito\.

__OS2600__

__RN02__

Será gerado apenas um registro do tipo “88SME” para o período solicitado, no qual não tenha sido constatada movimentação \(operação ou prestação\) de entrada\. 

__OS2600__

__RN03__

O registro 88SME deve ser totalizado na soma dos registros tipo 88 e no total geral dos registros \(99\), contidos no registro 90\.

__OS2600__

__RN04__

O Registro 88SME deverá ser informado __juntamente __com os registros de Nºs “10”, “11” e “90”, nos períodos em que não haja movimento de entradas\.

__OS2600__

__RN05__

Se o período de geração __tiver__ movimento de __saída__ e não tiver movimento de entrada, deverão ser gerados __os registros com os dados de saída__ e será gerado o registro SME, indicando que não houve entradas\. Ex: Considerando a situação onde o usuário realize a geração do registro 50 com movimento de saída e não tenha movimento de entrada, o sistema deve:

Gerar o registro 50 para movimentação de saída e,

Gerar o registro 88SME para indicar que não há movimento de entrada\.

__\[ALTERADA CH6875\_2012\]__

Considerar a situação onde o usuário realize a geração do Registro 70 com movimento de saída e não tenha movimento de entrada, o sistema deve:

Gerar o Registro 70 para movimentação de saída e,

Gerar o Registro Tipo 88SME para indicar que não há movimento de entrada\.

__OS2600/ CH6875\_2012__

__RN06__

Caso não existam dados de documentos fiscais de saída no período utilizado para o Estabelecimento de MG, deverá ser gerado automaticamente o registro “88 SMS”, conforme “De – Para” especificado no Documento de Requisito\.

__OS2600__

__RN07__

Será gerado apenas um registro do tipo “88SMS” para o período solicitado, no qual não tenha sido constatada movimentação \(operação ou prestação\) de saída\.

__OS2600__

__RN08__

O registro 88SMS deve ser totalizado na soma dos registros tipo 88 e no total geral dos registros \(99\), contidos no registro 90\.

__OS2600__

__RN09__

O Registro 88SMS deverá ser informado juntamente com os registros de Nºs “10”, “11” e “90”, nos períodos em que não haja movimento de saídas\. 

__OS2600__

__RN10__

Se o período __tiver__ Movimento de__ entrada__ e não tiver movimento de saída, deverão ser gerados __os registros com os dados de entrada__ e será gerado o registro SMS indicando que não houve saídas\. Ex: Considerando a situação onde o usuário realize a geração do registro 50 com entradas e não tenha movimento de saídas, o sistema deve:

Gerar o registro 50 para movimentação de entrada e,

Gerar o registro 88SMS para indicar que não há movimento de saída\.

__\[ALTERADA CH6875\_2012\]__ 

Considerar a situação onde o usuário realize a geração do Registro 70 com entradas e não tenha movimento de saídas, o sistema deve:

Gerar o Registro 70 para movimentação de entrada e,

Gerar o Registro Tipo 88SMS para indicar que não há movimento de saída\.

__OS2600/ CH6875\_2012__

__RN11__

Nos períodos em que não houver movimento de entradas e nem de saídas, devem ser informados os registros de Nºs “10”, “11”, “88SME”, “88SMS” e “90”\.

__OS2600__

__RN12__

Deverá ser criado um novo parâmetro na tela de parametrização de Perfil do módulo Meio Magnético, aba “Informações Gerais”\. Esse novo parâmetro será chamado “Gerar Número de Item com base no Número de Item dos documentos fiscais”\.

__OS2708__

__RN13__

Por default, esse parâmetro ficará desmarcado\.

__OS2708__

__RN14__

Ao ser selecionado, o sistema irá gerar os campos “Número de Item” dos registros 54, 88STITNF, 75, 56, 57 com os números de itens baseados nos documentos fiscais de acordo com a data informada e com os itens ordenados por ordem crescente \(ex: 1, 2, 3\)\.

__OS2708__

__RN15__

Os campos de Número de Item do Documento Fiscal que serão impactados com a inclusão desse novo parâmetro são \(respectivamente\) os campos 08 – Numero do Item e 09 – Numero do Item dos registros 54 e 88STITNF\.

__OS2708__

__RN16__

Caso a geração do meio magnético seja realizada sem o novo parâmetro estar selecionado, o sistema gera a ordenação dos itens conforme é realizado atualmente\.

__OS2708__

__RN17__

O relatório de conferência dessa tela deverá ser alterado para contemplar o novo parâmetro criado\.

__OS2708__

__RN18__

Na geração do meio magnético, o sistema não deverá gerar Registro 54 para Registros 88STITNF com períodos anteriores ao período da geração\. O sistema deverá recuperar os valores para estes registros respeitando a data solicitada na tela de geração, caso contrário não recuperar\.

__OS2708__

__RN19__

Quando o meio magnético for gerado somente para o registro 54 ou 88STITNF o parâmetro deve ser selecionado\.

__OS2708__

__RN20__

__\[ALTERADA – OS2850\]__ 

O registro 88STES deverá conter as informações conforme atualmente, mas sua recuperação deverá levar em consideração além das regras atuais também as movimentações de saída \(CFOP iniciando com ‘6’\) para fora do estado de MG que aconteceram dentro do período de geração constantes na tabela SAFX08, e cujos os produtos possuam os Códigos NBM devidamente parametrizados\.

Regra removida pela OS 30002, vide regra RN28\.

__OS2811, OS2850 __

__RN21__

Na geração do meio magnético, o sistema deverá gerar Registro 54 para Registros 88STITNF com períodos anteriores ao período da geração, ou seja, para o mês anterior\. O sistema deverá recuperar os valores para estes registros respeitando a data solicitada na tela de geração, caso contrário não recuperar\.

Regra removida pela OS 3002, vide regra RN29\.

__OS2850__

__RN22__

__\[ALTERADA CH85409\]__ 

Na geração do meio magnético, o sistema deverá gerar Registro 54 para as Notas Fiscais de entrada cujo modelo de documento seja igual a “06” \(Conta de Energia Elétrica\)\. A Energia Elétrica é considerada uma mercadoria no âmbito do ICMS, logo deverá ser gerado o registro 54\.

Na tela:

Meio Magnético → Parâmetros → Convênio → Perfil, aba “Informações Gerais”,

Criar o seguinte parâmetro:

__\[  \] Não gerar NF Modelo 06 no Registro 54__

__*Quando este parâmetro estiver marcado:*__

Gerar a nota fiscal de energia elétrica \(modelo 06\) *somente* no registro 50\.

Esta NF *não* deverá ser gerada em nenhum outro registro \(54, 75\)

__*Quando este parâmetro NÃO estiver marcado:*__

Gerar normalmente esta nota no registro 50 e em todos os seus filhos \(54, 75\)

Este parâmetro virá por default desmarcado\.

Esta alteração não influencia os registros específicos\.

Regra válida somente para entradas\.

__OS2864 / CH85409__

__RN23__

__\[EXCLUÍDA – OS3097\-C\] __Na geração do meio magnético, se o parâmetro 67 da tela de Parâmetros por UF do módulo ICMS estiver marcado, ao gravar o campo 05 do registro 53 deve ser utilizada a UF de destino ao invés de utilizar a UF PF/PJ da nota fiscal\. Para as notas fiscais de saída recuperar o campo “UF Destino” \(campos 122 da SAFX07\), para as demais notas fiscais recuperar o campo “UF Origem” \(campo 117 da SAFX07\)\. Se um dos campos a ser utilizado não estiver preenchido, deve se utilizar a UF PF/PJ da nota fiscal\. 

Se o parâmetro 67 não estiver marcado, utilizar a regra anterior a essa alteração, ou seja, preencher o campo 05 do registro 53 com a UF PF/PJ da nota\.

__CH72922__

__OS3097\-C__

<a id="OLE_LINK10"></a><a id="OLE_LINK11"></a><a id="OLE_LINK12"></a><a id="OLE_LINK13"></a>__RN24__

__\[ALTERADA – CH1063\_2014\]__

Sempre que na geração do Meio Magnético \(de qualquer convênio\) forem encontrados documentos fiscais com os CFOP’s 1206, 2206, 3206, 5206, 6206 e/ou 7206, estes documentos deverão gerar SOMENTE o registro 50\.

Todos os demais registros filhos \(incluindo o registro 75\) não deverão ser gerados nesta situação, exceto quando houver registro tipo 88E que precisa gerar o registro tipo 75 correspondente\.

Arrumar também os totalizadores\.

__CH69942__

__CH1063\_2014__

__RN25__

Caso o Documento Fiscal de Mercadoria cuja operação seja de Entrada \(campo E/S = “1”, “2”, “3”, “4” ou “5”\) e o Modelo de Documento \(campo Modelo Doc = 21\) não deve ser gerado registro 54 na geração do SINTEGRA\. 

__CH74417__

__RN26__

O registro 50 do Documento Fiscal citado na RN25 deve ser gerado normalmente\. O registro 75 desse arquivo será mantido como está atualmente, ou seja, não irá considerar o produto do registro 54, visto que o mesmo não foi gerado\.

__CH74417__

__RN27__

Caso o Documento Fiscal de Mercadoria cuja operação seja de Saída \(campo E/S = “9”\) e o Modelo de Documento \(campo Modelo Doc = 06, 21 ou 22\) não devem ser gerados no meio magnético SINTEGRA\.

__CH74417__

__RN28__

A geração dos __registros 88STES__ \(Informações Referentes a Estoque de Produtos Sujeitos ao Regime de Substituição Tributária\) irá considerar as regras a seguir:

o	Os produtos serão aqueles cujo NCM pertença à lista de NCM’s informada através da parametrização existente no menu “*Parâmetros >> Minas Gerais >> Estoque de Produtos ICMS\-ST\(88STEST e 88STITNF\) >> NCM dos Produtos Sujeitos ao ICMS\-ST*”;

      OU

      \[MFS\-28851\]

	Os produtos serão aqueles que pertençam a uma faixa de códigos informada através da parametrização existente no menu “*Parâmetros >> Minas Gerais >> Estoque de Produtos ICMS\-ST\(88STEST e 88STITNF\) >> Códigos dos Produtos Sujeitos ao ICMS\-ST*”;

o    \[MFS20115\] A forma de geração do registro dependerá do parâmetro “Gerar Registros 88STES e 88STITNF quando houver   mudança na forma de tributação” informado na tela de Perfil \(Parâmetros >> Convênio ICMS 58/95 e Alterações >> Perfil\)\.  Quando     o parâmetro estiver marcado, a geração irá recuperar somente os registros em que campo 40 \(Motivo do Inventário\) da SAFX52 for igual a “02” \(Na mudança de forma de tributação da mercadoria \(ICMS\)\)\.  Quando o parâmetro estiver desmarcado, a geração não se altera, irá recuperar todos os registros da SAFX52 sem verificar o campo 40\.

o	As mercadorias/produtos deverão possuir saldo de estoque inicial referente ao período anterior, conforme a data do inventário informada para a geração do Sintegra, não sendo obrigatório o estoque inicial para informação do registro 88STITNF\.      \[MFS20115\] Quando o parâmetro “Gerar Registros 88STES e 88STITNF quando houver   mudança na forma de tributação” informado na tela de Perfil \(Parâmetros >> Convênio ICMS 58/95 e Alterações >> Perfil\) estiver marcado, o registro 88STITNF somente será gerado se houver saldo de estoque inicial\.

  

o	As operações de saída a serem consideradas serão aquelas cujo CFOP ou CFOP/Natureza estejam parametrizados para a geração dos registros 88 no menu “*Parâmetros >> Minas Gerais >> Estoque de Produtos ICMS\-ST\(88STEST e 88STITNF\) >> Saídas Sujeitas à Restituição*”\.

__\[ALTERADA – CH12009\_2016/ CH10233\_2018 \(MFS\-18513\)\]__

As regras para preenchimento de cada um dos campos pertencentes ao registro estão especificadas abaixo:

__OS 3002__

__CH12009\_2016__

__CH1674\_2017/__

__MFS9404__

__CH10233\_2018 \(MFS\-18513\)__

__MFS20115__

__MFS28851__

Nº

DENOMINAÇÃO DO CAMPO

CONTEÚDO

TAMANHO

POSIÇÃO

FORMATO

1

Tipo

“88”

2

1

2

N

2

Subtipo

“STES”

4

3

6

X

3

CNPJ

CNPJ do estabelecimento dono do estoque\.

14

7

20

N

4

Data do Inventário

Será preenchido com a data do inventário do mês anterior, correspondente ao saldo inicial de estoque do produto no mês corrente da geração\. Observe que esta data deverá corresponder à data do inventário inicial informada na geração do meio magnético do sintegra\.

8

21

28

N

5

Código do Produto

Código do produto da nota fiscal, conforme registrado no registro 75 do meio magnético do sintegra, campo 02 da SAFX2013\.

60 14

29

88 42

X

6

Quantidade

Quantidade do produto registrada no inventário \(SAFX52\) na data do inventário informada no campo 4 acima\.

__Tratamento:__

- Se o campo estiver com a quantidade zerada, o registro não deverá ser ignorado, será gerado no arquivo magnético e os campos 7 e 8 deverão fazer o cálculo multiplicador normalmente\.

13

89 43

101 55

N

7

Valor do ICMS ST

O valor deste campo deverá corresponder ao Valor do ICMS\-ST Médio \(22 da SAFX52\) multiplicado pela quantidade informada no campo 6\.

12

102 56

113 67

N

8

Valor do ICMS Operações Próprias

O valor deste campo deverá corresponder ao Valor do ICMS Médio \(21 da SAFX52\) multiplicado pela quantidade informada no campo 6\.

12

114 68

125 79

N

9

Brancos

Complementação com espaços

47

126 80

126

X

__RN29__

\[ALTERADA CH64607\-B\] A geração dos __registros 88STITNF__ \(Informações sobre Itens das Notas Fiscais Relativas à Entrada de Produtos Sujeitos ao Regime de Substituição Tributária\) irá considerar as regras a seguir:

__\[MFS87116\] __Inclusão da verificação de cupom fiscal, além da nota fiscal de saída, como critério de recuperação das notas de entradas, para gerações anteriores a 01/03/2019

Para identificar os produtos a serem gerados:

- \[MFS\-32219\] Para gerações até 28/02/2019 este critério é válido:

 Caso o produto tenha sofrido uma saída com CFOP e/ou Natureza parametrizados através da opção de menu “*Parâmetros >> Minas Gerais >> Estoque de Produtos ICMS\-ST\(88STEST e 88STITNF\) >> Saídas Sujeitas à Restituição*”, então devemos gerar os registros 88STITNF das operações de entrada deste produto;

__OU__

Caso o produto tenha sofrido uma saída por Cupom Fiscal \(SAFX994\) com CFOP parametrizado através da opção de menu “*Parâmetros >> Minas Gerais >> Estoque de Produtos ICMS\-ST\(88STEST e 88STITNF\) >> Saídas Sujeitas à Restituição*”, então devemos gerar os registros 88STITNF das operações de entrada deste produto\.   Serão considerados todos os cupons fiscais cadastrados na tabela SAFX994, para a empresa, o estabelecimento \(tratar inscrição estadual única\) e data de emissão dentro do período informado para a geração, Situação do item no Cupom diferente de “2” \(Item Cancelado Totalmente\) e CFOP parametrizado\.

\[MFS\-32219\] Para gerações a partir de 01/03/2019: deveremos gerar os registros 88STITNF das operações de entrada dos produtos produtos sujeitos a ST, independente da existência de movimentação de saída\.

                 

- \[MFS\-28851\] Os produtos serão aqueles que pertençam a uma faixa de códigos informada através da parametrização existente no menu “*Parâmetros >> Minas Gerais >> Estoque de Produtos ICMS\-ST\(88STEST e 88STITNF\) >> Códigos dos Produtos Sujeitos ao ICMS\-ST*”;

OU

Os produtos serão aqueles cujo NCM pertença à lista de NCM’s informada através da parametrização existente no menu “*Parâmetros >> Minas Gerais >> Estoque de Produtos ICMS\-ST\(88STEST e 88STITNF\) >> NCM dos Produtos Sujeitos ao ICMS\-ST*”, onde iremos considerar a hierarquia dos códigos NCM, recuperando todos os NCM’s pertencentes a um mesmo grupo, exemplo:

- Caso seja fornecido um NCM de código 0307, então todos os existentes abaixo deste devem ser considerados na geração, ou seja, todos os NCM’s iniciados em 0307;
- Ao realizar esta busca, devemos também considerar a vigência dos NCM’s cadastrados, uma vez que somente os vigentes no período devem ser considerados;
- O NCM verificado será o da nota fiscal de saída, seguido do NCM do produto, caso o NCM da nota não esteja preenchido;

Para a recuperação das notas de entrada considerar as regras a seguir:

- Caso o produto possua valor de estoque inicial informado no registro 88STES, então deverão ser gerados os itens das últimas notas fiscais de entrada que componham este estoque, até a quantidade informada no estoque inicial\. Ao realizar esta pesquisa, o sistema deverá considerar o parâmetro “*Produtos Adquiridos c/ ICMS\-ST até\. *\[MFS20115\]* Como a recuperação do registro 88STITNF é baseada na recuperação dos produtos do registro 88STES, então o tratamento do parâmetro “*Gerar Registros 88STES e 88STITNF quando houver mudança na forma de tributação” já terá sido feito na geração do registro 88STES; 
- O campo quantidade do item da nota deve ser maior que zero;
- Os itens serão aqueles cujos campos “*Valor de Base ICMS\-ST Não Escriturado*” \(144 da SAFX08\) esteja preenchido com valor maior que zero ou “*Base ICMS Substituição Tributária*” \(61 da SAFX08\) esteja preenchido com valor maior que zero e o campo “*Apropria”* \(78 da SAFX08\) igual a “N”, sendo apresentado o valor do campo que possuir valor maior que zero no registro\.__ \[MFS27453\]__
- __MFS9038__ \(ch 222/2017\): Alterada geração do registro 88STITNF, conforme orientações da Informação, com base no RICMS/MG \(ver item 5 chamado\): Além das entradas de períodos anteriores que acobertam a quantidade do estoque inicial \(quando for o caso\), também serão geradas *todas* as entradas do produto que existirem no período em questão\. 

__\[ALTERADA – CH12009\_2016\]__

As regras para preenchimento de cada um dos campos estão indicadas abaixo:

Nº

DENOMINAÇÃO DO CAMPO

CONTEÚDO

TAMANHO

POSIÇÃO

FORMATO

1

Tipo

“88”

2

1

2

N

2

Subtipo

“STITNF”

6

3

8

X

3

CNPJ

CNPJ do emitente da NF de entrada, campo 06 da SAFX04\.

14

9

22

N

4

Modelo

Código do modelo do documento fiscal

2

23

24

N

5

Série

Série da nota fiscal

3

25

27

X

6

Número

Número da nota fiscal

9 6

28

36 33

N

7

CFOP

Código Fiscal de Operação e Prestação

4

37 34

40 37

N

8

CST

Código da Situação Tributária

3

41 38

43 40

N

9

Número de Item

Número de Ordem do Item na Nota Fiscal

3

44 41

46 43

N

10

Data Entrada

Data da efetiva  Entrada \(formato AAAAMMDD\)

8

47 44

54 51

N

11

Código do produto

Código do produto do informante

60 14

55 52

114 65

X

12

Quantidade

Quantidade existente no item da nota fiscal\.

11

115 66

125 76

N

13

Valor do Produto

Valor total do item da nota fiscal de entrada\.

12

126 77

137 88

N

14

Valor do Desconto

Valor do Desconto concedido no item\.

12

138 89

149 100

N

15

Base Cálculo do ICMS OP

__\[ALTERADA CH27464\_2016\]__

__Se__ o campo “Base ICMS não destacado” \(campo 226 da SAFX08\) estiver preenchido,

    O campo será preenchido com a informação existente no campo\.

__Senão__

    O campo será preenchido com a Base de Cálculo do ICMS existente na nota fiscal de entrada\.

12

150 101

161 112

N

16

Base Cálculo do ICMS ST

__\[MFS27453\]__

Campo Base ICMS Substituição Tributária ou campo  Valor de Base ICMS\-ST Não Escriturado \(campos 61 ou 144 da SAFX08\), ou seja, aquele que estiver preenchido, de acordo com a regra de recuperação do registro\.

12

162 113

173 124

N

17

Alíquota – ICMS/ST

Lançar o valor da alíquota do ICMS\-ST \(campo 51 da SAFX08\)\.

4

174 125

177 128

N

18

Alíquota – ICMS Operação Própria

__ \[ALTERADA MFS24464\]__

__Se__ o campo “Alíquota ICMS Não Destacado” \(campo 227 da SAFX08 \- VLR\_ALIQ\_ICMS\_NAO\_DEST\) estiver preenchido,

Preenchido com a alíquota existente neste campo \(VLR\_ALIQ\_ICMS\_NAO\_DEST\)\.

__Senão__

Preenchido com o Valor da Alíquota do ICMS \(campo 42 da SAFX08 \- VLR\_ALIQ\_ICMS\)\.

Lançar o Valor da Alíquota do ICMS \(campo 42 da SAFX08\)\.

4

178 129

181 132

N

19

Valor do IPI

Este campo será preenchido com o valor do Valor IPI ou IPI Não Escriturado \(campos 48 ou 81 da SAFX08\), ou seja, aquele que estiver preenchido\.

12

182 133

193 144

N

20

Chave da NF\-e

Este campo será preenchido com o conteúdo do campo “*226\-Chave de Acesso da NF\-Eletrônica*” da SAFX07, considerando as primeiras 44 posições\. Quando não existir a informação \(nulo\), o campo será preenchido com zeros\. 

\(campo incluído na __MFS22719__\)

44

194

237

N

__OS 3002 / __

__CH64607\-B__

__CH12009\_2016__

__MFS9038__

__CH27464\_2016__

__MFS20115__

__MFS22719__

__MFS24464__

__MFS28851__

__MFS\-32219__

__MFS87116__

__RN30__

Ao gerar o registro 54 para os itens 991 e 992, referentes a frete e seguro  o sistema deverá observar se os valores estão informados no item da nota, não tendo estes valores preenchidos no item \(SAFX08\) campos 39 e 40, então o sistema deverá realizar a verificação dos valores na capa da nota \(SAFX07\), campos 24 e 25\. Assim os itens 991 e 992 do registro 54, devem ser gerados a partir não só nos itens, mas também na capa, atualmente já temos este tratamento para alguns outros campos e então se faz necessário deixarmos também a regra para estes itens\.

__CH78184__

__RN31__

Caso o Documento Fiscal de Mercadoria cuja operação seja de Entrada \(campo E/S = “1”, “2”, “3”, “4” ou “5”\) e o Modelo de Documento \(campo Modelo Doc = 21 ou 22\) não deve ser gerado registro 54 na geração do SINTEGRA\.

__CH77317__

__RN32__

O registro 50 do Documento Fiscal citado na RN31 deve ser gerado normalmente\. O registro 75 desse arquivo será mantido como está atualmente, ou seja, não irá considerar o produto do registro 54, visto que o mesmo não foi gerado\.

__CH77317__

__RN33__

O campo “FAX” do registro tipo 10 será preenchido com os 2 primeiros caracteres \(excluindo\-se os espaços em branco e os zeros à esquerda\) do campo “DDD” \+ os 8 primeiros caracteres \(excluindo\-se os espaços em branco\) do campo “FAX” da tabela “ESTABELECIMENTO\. Como já acontece atualmente, caso o valor a ser gravado seja menor que 10 caracteres, o campo será completado com zeros à esquerda\.

__CH82260__

__RN34__

O campo “TELEFONE” do registro tipo 11 será preenchido com os 4 primeiros caracteres \(excluindo\-se os espaços em branco e os zeros à esquerda\) do campo “NUM\_DDD” \+ os 8 primeiros caracteres \(excluindo\-se os espaços em branco\) do campo “NUM\_TELEFONE” da tabela RESP\_INFORMACAO”\. Como já acontece atualmente, caso o valor a ser gravado seja menor que 12 caracteres, o campo será completado com zeros à esquerda\.

__CH82260__

__RN35__

Critério para Geração dos Registros 54

Caso os tipos de registros 56 ou 88C – CAT 95/SP tenham sido gerados, então o registro 54 deverá ser gerado normalmente, caso contrário, observar as condições a seguir:

__O estabelecimento pertence ao Estado de São Paulo:__

O item da nota fiscal possui um dos CFOPs indicados abaixo em suas vigências, então o registro 54 não deverá ser gerado\.

1. para fatos geradores que tiverem ocorrido até 31/12/02:

O CFOP for = 1\.73, 2\.73, 1\.74, 2\.74, 1\.91, 2\.91, 3\.91, 1\.92, 2\.92, 1\.97, 2\.97, 3\.97, 1\.98, 2\.98, 5\.91, 6\.91, 5\.92, 6\.92, 5\.95 ou 6\.95;

b\) para fatos geradores que ocorrerem a partir de 01/01/03:

O CFOP for = 1\.406, 2\.406, 1\.407, 2\.407, 1\.551, 2\.551, 3\.551, 1\.552, 2\.552, 1\.553, 2\.553, 3\.553, 1\.554, 2\.554, 1\.555, 2\.555, 1\.556, 2\.556, 3\.556, 1\.557, 2\.557, 5\.551, 6\.551, 7\.551, 5\.552, 6\.552, 5\.553, 6\.553, 7\.553, 5\.554, 6\.554, 5\.555, 6\.555, 5\.556, 6\.556, 7\.556, 5\.557, 6\.557, 1\.601, 1\.602, 1\.603, 2\.603, 1\.604 ou 1\.605\.

__O estabelecimento pertence ao Estado do Rio de Janeiro:__ o item da nota fiscal possui o CFOP 1556 ou 2556, então não iremos gerar o registro 54\.

__\[ALTERADA – OS3774\]__ __\[CH8984\_2013\] \- Para estabelecimento cuja UF seja RJ:__ quando o novo parâmetro “__Considerar notas fiscais de ativo fixo e uso/consumo para UF RJ \(Registro 54\)__” na tela de Parâmetros \-> Convênio ICMS 57/95 e Alterações \-> Perfil \-> Informações Gerais estiver “flegado”, deverá permitir a geração dos registros do Tipo 54 para notas fiscais de ativo fixo e uso/consumo, ou seja, itens da nota fiscal que possuam o CFOP 1551, 2551 e 3551 ou 1556, 2556 3556\.

__O estabelecimento pertence a outro Estado: __gerar o registro 54 normalmente\.

__Alteração OS2937:__

__A nota fiscal é classificada como não escriturada \(Pepsico\):__

Se a UF do estabelecimento que está sendo gerado está parametrizada no menu Específicos – Pepsico – Parâmetros – CFOP x UF então a geração deve:

Considerar as notas de classificação = “7” \(notas não escrituradas\), além das classificações já existentes\. 

As notas de classificação = “7” devem ter as seguintes características:

- Notas fiscais da SAFX07/SAFX08 com o campo “12\-Classificação do Documento Fiscal” da SAFX07 = “7”;
- CFOP da SAFX07 = aos CFOP’s parametrizados para a UF do estabelecimento \(Específicos – Pepsico – Parâmetros – CFOP x UF\)
- Modelo 01 ou 55;  
- Tanto notas de entrada como de saída;

Caso a UF do estabelecimento não esteja parametrizada no menu citado, a geração não deve considerar as notas de classificação = “7”\.

__Alteração OS4666:__

Se o Perfil da geração informado em tela estiver parametrizado no Módulo Pepsico __\(\*\)__, a geração dos registros 50, 51, 53 e 54 será feita __*apenas*__ considerando as notas fiscais __*não*__ escrituradas\. Estas “notas não escrituradas” são as notas descritas na regra anterior, referente à __OS2937__ \(modelo 01/55, classificação fiscal = 7, CFOP da capa parametrizado no módulo Pepsico para a UF do estabelecimento da geração\),

__\(\*\)__ Parametrização do Módulo Pepsico, menu “Parâmetros à Perfis do Sintegra”\. Esta parametrização utiliza uma coluna da tabela dos perfis do Sintegra \(ICT\_PAR\_MEIO\_MAG\), e quando o perfil for parametrizado, o conteúdo desta coluna será = “S”\. Caso contrário, será = nulo\. Este parâmetro só fica disponível para manutenção no Módulo Pepsico, pois foi criado para atendimento a regime especial deste cliente\. 

__CH82459__

__OS3178__

__OS2937__

__OS4666__

__RN36__

- Verificar os Documentos Fiscais de Saída \(campo 03 – MOVTO\_E\_S da SAFX07 = 9\);
- Verificar se o campo 118 – IND\_COMPRA\_VENDA = “FD” da tabela SAFX07;
- Verificar se os Documentos Fiscais de Saída cujos campos 237 – IND\_FIS\_CONCES e 238 – COD\_FIS\_CONCES da tabela SAFX07 estejam preenchidos\.
- Verificar se o campo “Valor ICMS\-S” está preenchido e se o campo “Apropria” da tabela SAFX08 está selecionado\.
- SE

UF do campo 238 – COD\_FIS\_CONCES da tabela SAFX07 <> UF da UF do Estabelecimento \(vide campo IDENT\_ESTADO da tabela ESTABELECIMENTO\)

ENTÃO

Creditar o Valor de ICMS\-ST para a UF informada no campo 238 – COD\_FIS\_CONCES\. Essa UF informada deverá ser informada no campo 05 – Unidade de Federação do __registro tipo 53 – Substituição Tributária__ do Meio Magnético SINTEGRA \(ver layout no documento *CONVENIO\_ICMS\_57\_95\.pdf*\)\.

O valor de ICMS\-ST deverá ser informado no campo 12 – ICMS Retido do __registro tipo 53 – Substituição Tributária__ do Meio Magnético SINTEGRA \(ver layout no documento *CONVENIO\_ICMS\_57\_95\.pdf*\)\.

SENÃO

Creditar o Valor de ICMS\-ST para a UF informada no campo IDENT\_FIS\_JUR da tabela SAFX07\. Essa UF informada deverá ser informada no campo 05 – Unidade de Federação do __registro tipo 53 – Substituição Tributária__ do Meio Magnético SINTEGRA \(ver layout no documento *CONVENIO\_ICMS\_57\_95\.pdf*\)\.

OS3097\-C

__RN37__

Caso os campos 237 – IND\_FIS\_CONCES e 238 – COD\_FIS\_CONCES da tabela SAFX07 não estejam preenchidos, o sistema deve exibir uma mensagem de alerta na aba “Log” da tela de geração do meio magnético SINTEGRA \(módulo Meio Magnético, menu Meio Magnético – Geração do Meio Magnético ICMS\)\. A mensagem é:

Campos 237 – Indicador do Código e 238 – Código Fis/Jur da Concessionária da tabela SAFX07 não foram preenchidos para efeitos de crédito do ICMS\-ST para a UF da Concessionária\.

Junto à mensagem deve ser exibidas as informações chave do documento fiscal para que o cliente possa identificar qual documento fiscal não possui a informação\. *Exemplo:* 076\-01\-001\-01012000, onde:

076 – empresa

01 – estabelecimento

001 – número do documento fiscal

01012000 – data de emissão do documento fiscal

OS3097\-C

__RN38__

Excluir a regra que credita o valor de ICMS através da UF Destino utilizando o parâmetro 67 da tela de Parâmetros por UF do módulo ICMS para o SINTEGRA\.

OS3097\-C

__RN39__

Para que a geração do SINTEGRA seja realizada de maneira correta, o usuário deverá selecionar no campo “UF” a opção “Todas as UF’s”\. 

OS3097\-C

__RN40__

Ao gravar a UF da Concessionária no campo 05 – Unidade de Federação do __registro tipo 53 – Substituição Tributária__ de acordo com a RN01, o campo 03 – Inscrição Estadual deve ter seu conteúdo gravado com a Inscrição Estadual da Concessionária \(vide campo 08 – INSC\_ESTADUAL da tabela X04\_PESSOA\_FIS\_JUR\)\. É importante que essa regra seja feita, em virtude da crítica existente no validador\.

OS3097\-C

__RN41__

Quando existe uma nota fiscal complementar no sistema \(situação especial = 5 na capa da NF\), é gerado no Sintegra um registro 50 normal e um registro 54 com o item especial 997 e os dados principais da NF\.

Este procedimento está correto visto que essas notas geralmente não possuem item no sistema, porém quando os demais valores estiverem preenchidos na NF, deverão ser preenchidos no arquivo também\.

__Nº__

__Denominação do Campo__

__Preenchimento Msaf__

01

Tipo 

__Fixo “54”__

02 

CNPJ 

CNPJ do remetente nas entradas e do destinatário nas saídas

03 

Modelo 

Modelo da NF na capa

04 

Série 

Série da NF na capa

05 

Número 

Número da NF na capa

06 

CFOP 

CFOP

*Do item, se tiver item*

*Da capa, se não tiver item*

*Sem preenchimento, se não houver informação capa/item*

07 

CST 

CST

*Do item, se tiver item*

*Da capa, se não tiver item*

*Sem preenchimento, se não houver informação capa/item*

08 

Número do Item 

__Fixo “997”__

09 

Código do Produto ou Serviço

Código do produto

*Do item, se tiver item*

*Sem preenchimento, se não houver item*

10 

Quantidade 

Quantidade

*Do item, se tiver item*

*Fixo “1”, se não houver item*

11 

Valor do Produto 

Valor Produto 

*Campo 22/safx07*

12 

Valor do Desconto / Despesa Acessória 

Valor ICMS \(x07\)

*Campo 35/safx07 ou campo 43/safx08, se houver item*

13 

Base de Cálculo do ICMS 

Base ICMS \(x07\)

*Campo 51/safx07 ou campo 56/safx08, se houver item*

14 

Base de Cálculo do ICMS ST

Base ICMS\-S \(x07\)

*Campo 64/safx07 ou campo 61/safx08, se houver item*

15 

Valor do IPI 

Valor do IPI \(x07\)

*Campo 40/safx07 ou campo 48/safx08, se houver item*

16 

Alíquota do ICMS 

Alíquota ICMS \(x07\)

*Campo 34/safx07 ou campo 42/safx08, se houver item*

CH82194

__RN42__

__Registro 85 – Campo 05 \(Registro de Exportação\)__

Para Declaração Simplificada de Exportação \(campo 71/safx48 = DS ou IS\), o campo 5 deve ser preenchido com Zeros, independente de, na safx48, o campo *Número do RE* estar preenchido ou não\.

OS3230

__RN43__

__Registro 85 – Campo 06 \(Data do Registro\)__

Para Declaração Simplificada de Exportação \(campo 71/safx48 = DS ou IS\), o campo 6 deve ser preenchido com Zeros\.

Mesmo que o campo 03 da safx48 esteja preenchido, gravar com zeros\.

OS3230

__RN44__

__Registro 54 Especial – Sequencial 999__

Alterar geração do Meio Magnético para o registro 54, quando é gerado o item seqüencial 999 no campo 08\. 

Existe no módulo uma parametrização em:

Meio Magnético → Parâmetros → Parâmetros por UF

CH35852\-A/2012

__Quando o parâmetro está desmarcado:__

É Deverá ser gerado somente um registro 999, com para cada um dos CFOP’s do item, e não grava alíquota\.

__Quando o parâmetro está marcado:__

Deverá ser gerado um registro 999 para cada CFOP e alíquota\.

\*\*\* O nome do parâmetro não deverá mudar: será colocado no HELP uma informação para indicar ao usuário que este seqüencial em específico terá um comportamento diferente\.

CH88198

CH35852\-A/2012

__RN44\-A__

Critério para Geração dos Registros 50

__Alteração os2937:__

__A nota fiscal é classificada como não escriturada \(Pepsico\):__

Se a UF do estabelecimento que está sendo gerado está parametrizada no menu Específicos – Pepsico – Parâmetros – CFOP x UF então a geração deve:

Considerar as notas de classificação = “7” \(notas não escrituradas\), além das classificações já existentes\. 

As notas de classificação = “7” devem ter as seguintes características:

- Notas fiscais da SAFX07/SAFX08 com o campo “12\-Classificação do Documento Fiscal” da SAFX07 = “7”;
- CFOP da SAFX07 = aos CFOP’s parametrizados para a UF do estabelecimento \(Específicos – Pepsico – Parâmetros – CFOP x UF\)
- Modelo 01 ou 55;  
- Tanto notas de entrada como de saída;

Caso a UF do estabelecimento não esteja parametrizada no menu citado, a geração não deve considerar as notas de classificação = “7”\.

__Alteração OS4666:__

Se o Perfil da geração informado em tela estiver parametrizado no Módulo Pepsico __\(\*\)__, a geração dos registros 50, 51, 53 e 54 será feita __*apenas*__ considerando as notas fiscais __*não*__ escrituradas\. Estas “notas não escrituradas” são as notas descritas na regra anterior, referente à __OS2937__ \(modelo 01/55, classificação fiscal = 7, CFOP da capa parametrizado no módulo Pepsico para a UF do estabelecimento da geração\),

__\(\*\)__ Parametrização do Módulo Pepsico, menu “Parâmetros à Perfis do Sintegra”\. Esta parametrização utiliza uma coluna da tabela dos perfis do Sintegra \(ICT\_PAR\_MEIO\_MAG\), e quando o perfil for parametrizado, o conteúdo desta coluna será = “S”\. Caso contrário, será = nulo\. Este parâmetro só fica disponível para manutenção no Módulo Pepsico, pois foi criado para atendimento a regime especial deste cliente\. 

__OS2937__

__OS4666__

__RN45__

__Regra para NF de transferência do ICMS – Registro 50:__

Quando se tratar de Nota Fiscal de transferência do ICMS, a gravação de __valores \(campos 11, 12, 13, 14, 15 – Meio Magnético\)__ no Registro 50 deverá ser zerada\.

A identificação da Nota Fiscal de transferência do ICMS será pela tabela SAFX07 quando:

__\- Campo 23 – VLR\_TOT\_NOTA = 0,00;__

__\- Campo 74 – IND\_TRANS\_CRED <> ‘0’\.__

A gravação de valores no Registro 50 deve ocorrer zerada mesmo que o __Campo 35 – VLR\_ICMS <> 0,00__\.

__Obs\.:__ O filtro pelo Campo 03 – MOVTO\_E\_S __não__ foi informado em virtude da possibilidade de haver nota fiscal de saída e entrada\.

__\[ALTERADA – CH118186\]__

Essa regra deve ser válida quando a UF do estabelecimento for igual a SP e RJ\.

__CH92305\-A/ CH118186__

__RN45\-A__

Critério para Geração dos Registros 51

__Alteração os2937:__

__A nota fiscal é classificada como não escriturada \(Pepsico\):__

Se a UF do estabelecimento que está sendo gerado está parametrizada no menu Específicos – Pepsico – Parâmetros – CFOP x UF então a geração deve:

Considerar as notas de classificação = “7” \(notas não escrituradas\), além das classificações já existentes\. 

As notas de classificação = “7” devem ter as seguintes características:

- Notas fiscais da SAFX07/SAFX08 com o campo “12\-Classificação do Documento Fiscal” da SAFX07 = “7”;
- CFOP da SAFX07 = aos CFOP’s parametrizados para a UF do estabelecimento \(Específicos – Pepsico – Parâmetros – CFOP x UF\)
- Modelo 01 ou 55;  
- Tanto notas de entrada como de saída;

Caso a UF do estabelecimento não esteja parametrizada no menu citado, a geração não deve considerar as notas de classificação = “7”\.

__Alteração OS4666:__

Se o Perfil da geração informado em tela estiver parametrizado no Módulo Pepsico __\(\*\)__, a geração dos registros 50, 51, 53 e 54 será feita __*apenas*__ considerando as notas fiscais __*não*__ escrituradas\. Estas “notas não escrituradas” são as notas descritas na regra anterior, referente à __OS2937__ \(modelo 01/55, classificação fiscal = 7, CFOP da capa parametrizado no módulo Pepsico para a UF do estabelecimento da geração\),

__\(\*\)__ Parametrização do Módulo Pepsico, menu “Parâmetros à Perfis do Sintegra”\. Esta parametrização utiliza uma coluna da tabela dos perfis do Sintegra \(ICT\_PAR\_MEIO\_MAG\), e quando o perfil for parametrizado, o conteúdo desta coluna será = “S”\. Caso contrário, será = nulo\. Este parâmetro só fica disponível para manutenção no Módulo Pepsico, pois foi criado para atendimento a regime especial deste cliente\. 

__Alteração Chamado 23172\_2014:__

Desconsiderar na geração do Registro Tipo 51 nota fiscal de entrada e saída correspondente à totalização quanto ao IPI de acordo com o período e estabelecimento de geração quando o campo 229\-Código Modelo NF da SAFX07 for igual a “55” e o campo 22\-Código Fiscal da SAFX08 ou 07 \(em caso de nota fiscal sem item\) for igual a: “1200, 1205, 1206, 1207, <a id="DEVOL_2200"></a>2200, 2205, 2206, 2207, 3200, 3205, 3206, 3207, 5200, 5205, 5206, 5207, 6200, 6205, 6206, 6207, 7200, 7205, 7206 e 7207”; para os demais manter tratamento atual da geração\.

__OS2937__

__OS4666__

__CH23172\_2014__

__RN46__

__Regra para considerar Parâmetro 67 \( módulo ICMS\):__

__Módulo:__ Estadual → Meio Magnético

__Menu:__ Meio Magnético → Geração do Meio Magnético ICMS

No momento da geração do Meio Magnético, o sistema deverá verificar se o __Parâmetro 67__ – __Lançar Campo UF Origem/Destino do Documento Fiscal nos Livros Fiscais \(Movimentos/Resumo por UF\) __em __Módulo:__ ICMS – __Menu:__ Manutenção → Parâmetros por UF, está selecionado\. 

Se o __Parâmetro 67__ – __Lançar Campo UF Origem/Destino do Documento Fiscal nos Livros Fiscais \(Movimentos/Resumo por UF\)__ estiver selecionado, o sistema deverá considerá\-lo para a geração do Registro 53 do Meio Magnético, ou seja, considerar as informações dos campos abaixo documentos fiscais que tiverem os campos abaixo devidamente preenchidos:

__Campo 117 – UF\_ORIG\_DEST \(SAFX07\)__

__Campo 122 – UF\_DESTINO \(SAFX07\)__

quando:

\- Campo 03 – MOVTO\_E\_S = ‘9’ \(SAFX07\);

\- Campo 11 – DATA\_EMISSAO for pertinente ao período de geração da obrigação \(SAFX07\);

\- Campo 12 – COD\_CLASS\_DOC\_FIS = ‘1’ \(SAFX07\); 

__\- __Campo 118 – IND\_COMPRA\_VENDA = ‘FD’ \(SAFX07\)

Se o __Parâmetro 67__ – __Lançar Campo UF Origem/Destino do Documento Fiscal nos Livros Fiscais \(Movimentos/Resumo por UF\)__ não estiver selecionado, a geração do Meio Magnético deverá ocorrer normalmente\. 

__OS3038__

__RN46\-A__

Critério para Geração dos Registros 53

__Alteração os2937:__

__A nota fiscal é classificada como não escriturada \(Pepsico\):__

Se a UF do estabelecimento que está sendo gerado está parametrizada no menu Específicos – Pepsico – Parâmetros – CFOP x UF então a geração deve:

Considerar as notas de classificação = “7” \(notas não escrituradas\), além das classificações já existentes\. 

As notas de classificação = “7” devem ter as seguintes características:

- Notas fiscais da SAFX07/SAFX08 com o campo “12\-Classificação do Documento Fiscal” da SAFX07 = “7”;
- CFOP da SAFX07 = aos CFOP’s parametrizados para a UF do estabelecimento \(Específicos – Pepsico – Parâmetros – CFOP x UF\)
- Modelo 01 ou 55;  
- Tanto notas de entrada como de saída;

Caso a UF do estabelecimento não esteja parametrizada no menu citado, a geração não deve considerar as notas de classificação = “7”\.

__Alteração OS4666:__

Se o Perfil da geração informado em tela estiver parametrizado no Módulo Pepsico __\(\*\)__, a geração dos registros 50, 51, 53 e 54 será feita __*apenas*__ considerando as notas fiscais __*não*__ escrituradas\. Estas “notas não escrituradas” são as notas descritas na regra anterior, referente à __OS2937__ \(modelo 01/55, classificação fiscal = 7, CFOP da capa parametrizado no módulo Pepsico para a UF do estabelecimento da geração\),

__\(\*\)__ Parametrização do Módulo Pepsico, menu “Parâmetros à Perfis do Sintegra”\. Esta parametrização utiliza uma coluna da tabela dos perfis do Sintegra \(ICT\_PAR\_MEIO\_MAG\), e quando o perfil for parametrizado, o conteúdo desta coluna será = “S”\. Caso contrário, será = nulo\. Este parâmetro só fica disponível para manutenção no Módulo Pepsico, pois foi criado para atendimento a regime especial deste cliente\. 

__OS2937__

__OS4666__

__RN47__

__\[ALTERADA – OS3229\]__ __Geração do Registro Tipo 56 – Operações com Veículos Automotores Novos__

Para a geração do Registro Tipo 56 foi alterado o parâmetro anterior “__NCM/NBM p/ Op\. Veículos Automotores Novos – Tipo 56”, __incluindo uma nova opção que é o “__CFOP” __e por __Extensão de CFOP,__ para compor o critério de busca do registro\. 

Além do critério de busca já existente por NCM/NBM, a rotina de geração deverá selecionar os registros quando o parâmetro __Operação com Veículos Automotores Novos – Tipo 56 – Por CFOP__, estiver preenchido com CFOP \(tabela SAFX2012\) juntamente com o Estabelecimento\. 

Ou então, a rotina de geração deverá selecionar os registros quando o parâmetro __Operação com Veículos Automotores Novos – Tipo 56 – Por Extensão de CFOP\. __Recuperar o campo 01 \(COD\_CFO\) da tabela SAFX2012 e o campo COD\_NATUREZA\_OP da tabela X2006\_NATUREZA\_OP\. Os campos IDENT\_CFO e IDENT\_NATUREZA\_OP devem estar relacionados na tabela X2081\_EXTENSAO\_CFO\. Deverá estar preenchido a Natureza de CFOP juntamente com o Estabelecimento\.

Estes novos parâmetros “CFOP” e “CFOP/Natureza” não serão obrigatórios\. Serão verificados somente quando existirem informações parametrizadas\.

Obs\.: O critério de seleção do registro deverá ser alterado quando é verificado o conteúdo do parâmetro do registro 56, os demais critérios não foram alterados\.

__OS3229__

__RN48__

__Regra para criar campo NF REFERENCIADA OUTRAS UF’S:__

__Módulo: __Estadual → Meio Magnético

__Menu: __Meio Magnético → Geração do Meio Magnético

Criar um fleg __NF REFERENCIADA OUTRAS UF’S \( Registro 70\)__\.

Deve ficar abaixo do campo UF\.

Este campo deve estar desabilitado, e somente habilitar quando o usuário selecionar uma UF específica\.

Caso selecionado, este campo deverá gerar para o Registro 70 Nota, Nota Fiscal referenciada de outras UF’s\.

__CH110164\-A__

__RN49__

__RN49__

__\[EXCLUÍDA – CH117555\]__ __Regra para geração MM – Registro Tipo 60ª: __

__Módulo:__ Estadual → Meio Magnético Sintegra

__Menu__: 

Na geração do Meio Magnético, para o __REGISTRO TIPO 60ª__, preenchimento do __CAMPO Nº 06__, a informação deve ser recuperada da __SAFX28 – Equiparado Emissor de Cupom Fiscal, Campo 24 – VLR\_GT\_FINAL__, quando:

Campo 10 – DATA\_EMISSÃO \(SAFX28\) for pertinente ao período da geração do Meio Magnético\.

![](data:image/png;base64,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)

__Alteração – CH117555:__

Na geração do Meio Magnético, para o __REGISTRO TIPO 60ª__, preenchimento do __CAMPO Nº 06__, deve ser um total parcial por situação tributária/ alíquota, ou seja, deve ser gerado um registro \(tipo 60ª\) para cada situação tributária/ alíquota por dia e por equipamento, possuindo um valor acumulado no final do dia\.

Para o campo 05 – Situação Tributária/ Alíquota \(layout registro tipo 60ª\) deve ser recuperada o campo 09 – VLR\_ALIQ\_OPER \(SAFX29\), que deve ser correspondente ao campo 17 – COD\_TRIB\_INT \(SAFX29\)\.

Para o campo 06 – Valor Acumulado no totalizador parcial \(layout registro tipo 60ª\) deve ser recuperada o campo 10 – COD\_TRIB\_INT \(SAFX29\), e que deve corresponder ao campo 05 Situação Tributária/ Alíquota e também ao campo 17 – COD\_TRIB\_INT \(SAFX29\)\.

__CH111796/ CH117555__

__CH111796/ CH117555__

__RN50__

__Registro Tipo 53 – Campo 12 \(ICMS Retido\)__

Se o campo 82 \(IND\_CRED\_ICMSS\) for igual á “N”

	E o campo 143 \(COD\_ANTEC\_ST\) da SAFX07 for igual á “4”, então:

Levar o valor do campo 48 \(VLR\_SUBST\_ICMS\) para este campo no Meio Magnético \(Campo 12 do registro Tipo 53\)\.

__CH112538__

__RN51__

__Registro Tipo 53 – Campo 15 \(Código da Antecipação\)__

Se o campo 82 \(IND\_CRED\_ICMSS\) for igual á “N”

	E o campo 143 \(COD\_ANTEC\_ST\) da SAFX07 for igual á “4”, então:

Informar o valor “4” no campo 15 do registro Tipo 53\.

__CH112538__

__RN52__

__Tipo de Receita – Registros Tipo 76 e 77__

Se o campo 14 da SAFX42 = “4”, então:

Gerar o valor = “3” para os seguintes campos do Sintegra:

Para o registro Tipo 76, campo 09 e para o Registro Tipo 77, campo 08\.

__OS3531__

__RN53__

Na geração do meio magnético – Registro 50, verificar se o parâmetro 67 \- Lançar Campo UF Origem/Destino do Documento Fiscal nos Livros Fiscais \(Movimentos/Resumo por UF\) \- \(Módulo: ICMS > Menu: Manutenção > Parâmetros por UF\) está selecionado, caso positivo, considerar os campos abaixo, para recuperação das notas, quando o campo 13 \- COD\_MODELO = ‘55’ e campo 03 \- MOVTO\_E\_S = ‘9’ da SAFX07:

122 – UF\_DESTINO \(SAFX07\)\. A informação desse campo deve ser levada para o campo 05 – Unidade de Federação \(Sigla da unidade da Federação do remetente nas entradas e do destinatário nas saídas\)\.

Quando o parâmetro 67 – Lançar Campo UF Origem/Destino do Documento Fiscal nos Livros Fiscais \(Movimentos/Resumo por UF\)

não estiver selecionado, o sistema deve recuperar a informação do campo 19 – UF \(SAFX04\) referente à pessoa fis/ jur\.

__CH109989__

__RN54__

__Registro Tipo 56 – Campo 11 \(CNPJ/ MF da Concessionária\):__

Se campo 118 – IND\_COMPRA\_VEND \(SAFX07\) = ‘FD’, então:

Levar a informação do campo 06 – CPF\_CGC \(SAFX04\) correspondente ao campo 238 – COD\_FIS\_CONCES \(SAFX07\) para o campo 11 do Registro Tipo 56\.

__CH5271\_2012__

__RN55__

__Geração do Registro 88\-11 da DIC\-SE:__   \(Alteração da __OS3690__ – Ago/2012\)

A geração do meio magnético foi alterada para passar a gerar o registro especial 88\-11 da DIC\-SE, mas somente quando o parâmetro “*Registros 88 – SE*” estiver selecionado no perfil escolhido para a geração \(menu Parâmetros à Convênio ICMS 57/95 e alterações à Perfil\)\.

__Se__ o parâmetro “Registro 88 – SE” = “S” 

     O registro 88\-11 será gerado a partir dos dados apurados no Módulo DIC\-SE, ou digitados pelo usuário na rotina de manutenção

     do registro 88\-11, também do módulo DIC\-SE\.

     \(mesmo procedimento adotado pelos demais registros específicos do SE gerados no Sintegra\)

__Senão__

     O registro 88\-11 *não* será gerado\.

__Obs__: Para gerar o campo “04\-Município”, o código do município utilizado na DIC\-SE é obtido através da parametrização do item de menu “Parâmetros à Município IBGE x Sergipe” do módulo DIC\-SE\.

__OS3690__

__RN56__

__Geração do registro 74 quando a UF do Estabelecimento = AM__

A geração do arquivo magnético do Sintegra AMAZONAS, no caminho Módulo Meio Magnético à Meio Magnético à Geração do meio magnético ICMS \- AM, deve ser filtrado por estabelecimento e Inscrição estadual, conforme a parametrização de geração utilizada pelo usuário\.

Gerar um arquivo por IE

__CH17462\_2012__

__RN57__

__Geração do Registro 8802 quando a UF do Estabelecimento = MS:__

O Registro Tipo 8802 deve ser gerado quando o campo 71 \- IND\_NF\_ESPECIAL \(SAFX07\) for = ‘I”, levando\-se o critério abaixo:

Campo 11 \- DATA\_EMISSAO for pertinente ao período de geração;

Campo 12 \- COD\_CLASS\_DOC\_FIS = ‘4’;

Campo 30 – SITUACAO = ‘N’

__CH21224\_2012__

__RN58__

__Registro Tipo 55__

A geração deste registro foi alterada para passar a considerar as novas guias da opção “GNRE Online”, além das opções da GNRE “normal” e GNRE por Grupo/Convênio já tratadas originalmente\.

Somente considerar registros com Valor GNRE maior do que Zero

 O preenchimento do registro TIPO 55 a partir das guias da GNRE Online será feito da seguinte forma:

Campo

Conteúdo a ser gravado a partir da tabela das guias da GNRE Online 

Tipo 

Gravar “55”

CNPJ

CNPJ do estabelecimento

Inscrição Estadual

Este campo demonstra a IE do contribuinte na UF Favorecida, e será gerado da seguinte forma:

Se o Estabelecimento tiver registro de uma IE na UF Favorecida

      \(IE cadastrada  no menu “Cadastros à Inscrições Estaduais” do Módulo

       Parâmetros, o Estabelecimento e a UF Favorecida\)

      Neste caso o campo é preenchido com a IE recuperada no módulo

       Parâmetros;

Senão

      O campo é preenchido com o conteúdo “INEXISTENTE”;

Data da GNRE

Campo “Data do Pagamento” 

UF do substituto

Sigla da UF do estabelecimento

UF Favorecida

Campo “UF Favorecida”

Banco GNRE

Campo “Banco Recolhimento”

Agencia GNRE

Campo “Agência Recolhimento”

Número GNRE

Campo “N\. Autenticação Bancária”

__\[ALTERAÇÃO – CH28466\_2013\]__

__\[ALTERAÇÃO – OS4195\]__

__Tratamento:__

\- Se o campo for preenchido com mais de 20 posições, deve considerar na geração ignorando as primeiras posições, ou seja, considerar as 20 últimas\. É necessário gerar a mensagem em Log “Autenticação Bancária da Guia de Recolhimento \- GNRE Online está com mais de 20 posições\. Favor verificar, pois será considerado as 20 últimas posições”\.

\- Se o campo for preenchido com menos de 20 posições, deve considerar na geração espaços em branco à esquerda do número, por ser um campo alfanumérico\.

Valor GNRE

Campo “Valor Principal”, se preenchido\. Caso contrário, será utilizado o campo “Valor Total”\.

Data Vencimento

Campo “Data do Vencimento”

Mês e Ano de Referência

Campo “Mês e Ano de referência”

Número do Convênio/Protocolo

Campo “Convênio”

__\[ALTERAÇÃO – 28466\_2013\]__

O preenchimento do registro TIPO 55 a partir das guias da GNRE normal será feito da seguinte forma:

Número GNRE

Campo “Nº Autenticação”

__Tratamento:__

__\[ALTERAÇÃO – OS4195\]__

\- Se o campo for preenchido com mais de 20 posições, deve considerar na geração ignorando as primeiras posições, ou seja, considerar as 20 últimas\. É necessário gerar a mensagem em Log “Autenticação Bancária da Guia de Recolhimento \- GNRE Online está com mais de 20 posições\. Favor verificar, pois será considerado as 20 últimas posições”\.

__\[ALTERAÇÃO – CH28466\_2013\]__

\- Se o campo for preenchido com menos de 20 posições, deve considerar na geração espaços em branco à esquerda do número, por ser um campo alfanumérico\.

__\[ALTERAÇÃO – OS4195\]__

O preenchimento do registro TIPO 55 a partir das guias por Grupo/Convênio GNRE será feito da seguinte forma:

Número GNRE

Campo “Nº Autenticação”

__Tratamento:__

\- Se o campo for preenchido com mais de 20 posições, deve considerar na geração ignorando as primeiras posições, ou seja, considerar as 20 últimas\. É necessário gerar a mensagem em Log “Autenticação Bancária da Guia de Recolhimento \- GNRE Online está com mais de 20 posições\. Favor verificar, pois será considerado as 20 últimas posições”\.

\- Se o campo for preenchido com menos de 20 posições, deve considerar na geração espaços em branco à esquerda do número, por ser um campo alfanumérico\.

__OS3520\-D__

__CH28466\_2013__

__OS4195__

__MFS8012\(CH23671\)__

__RN59__

__Registro Tipo 50:__

__Regra Geral:__

Deve ser gerado para os documentos fiscais descritos a seguir:

__\[ALTERADA – CH18474\_2015\]__

- Nota Fiscal, modelo 1 ou 1\-A \(código 01\), quanto ao ICMS, a critério de cada UF, Nota Fiscal do Produtor, modelo 4 \(código 04\),
- Nota Fiscal/Conta de Energia Elétrica, modelo 6 \(código 06\),
- Nota Fiscal de Serviço de Comunicação, modelo 21 \(código 21\),
- Nota Fiscal de Serviços de Telecomunicações, modelo 22 \(código 22\)’
- Nota Fiscal Eletrônica, modelo 55 \(código 55\)\.
- Nota Fiscal de Consumidor Eletrônica \(modelo 65\), __SOMENTE__ quando a UF do Estabelecimento for igual a PI\. *Observação:* Retirado do Registro 61 para gerar no Registro 50 conforme “Comunicado n° 003/2015 de 10 de agosto de 2015” da SEFAZ/PI\. Aos demais estados mantém a mesma geração\.

Deve ser gerado um registro tipo 50 para cada registro 54 de acordo com a concatenação das informações relativos a “CFOP” e “Alíquota”\. Em suma, na hipótese de haver uma nota fiscal com 2 ou mais itens deve ser criado um registro 50 para tantas quantas forem as combinações entre CFOP e Alíquota existentes na SAFX08\.

__\[ALTERADA – MFS11800 / MFS58872\]__

__Regra dos Campos:__

Nº 

Denominação do Campo 

Conteúdo 

Tamanho 

Posição 

Formato 

Preenchimento MSAF

01 

Tipo 

"50" 

02 

1 

2 

N 

02 

CNPJ 

CNPJ do remetente nas entradas e do destinatário nas saídas 

14 

3 

16 

N 

Se a NF for modelo igual a “65” \(princípio estabelecido para Piauí conforme regra geral\), esse campo será preenchido com a informação do CPF/CNPJ do Consumidor da SAFX07\.

Senão, se o campo CPF/CNPJ do Consumidor da SAFX07 não estiver informado será preenchido com a informação do campo CPF\-CGC da SAFX04\. Caso não houver cadastro na SAFX04 preencher com zeros\.

Os demais modelos de NF serão preenchidos com base na informação do campo CPF\-CGC da SAFX04\.

03 

Inscrição Estadual 

Inscrição Estadual do remetente nas entradas e do destinatário nas saídas 

14 

17 

30 

X 

As pessoas não obrigadas \(pessoas não inscritas ou estrangeiras\) e que estão cadastradas na SAFX04 já vem com o preenchimento da informação de “ISENTO” conforme orientação do Manual de Layout de Importação do Mastersaf DW\.

04 

Data de emissão ou recebimento 

Data de emissão na saída ou de recebimento na entrada 

8 

31 

38 

N 

05 

Unidade da Federação 

Sigla da unidade da Federação do remetente nas entradas e do destinatário nas saídas 

2 

39 

40 

X 

06 

Modelo 

Código do modelo da nota fiscal 

2 

41 

42 

N 

07 

Série 

Série da nota fiscal 

3 

43 

45 

X 

08 

Número 

Número da nota fiscal 

6 

46 

51 

N 

09 

CFOP 

Código Fiscal de Operação e Prestação 

4 

52 

55 

N 

10 

Emitente 

Emitente da Nota Fiscal \(P\-próprio/T\-terceiros\) 

1 

56 

56 

X 

11 

Valor Total 

Valor total da nota fiscal \(com 2 decimais\) 

13 

57 

69 

N 

12 

Base de Cálculo do ICMS 

Base de Cálculo do ICMS \(com 2 decimais\) 

13 

70 

82 

N 

13 

Valor do ICMS 

Montante do imposto \(com 2 decimais\) 

13 

83 

95 

N 

14 

Isenta ou não\-tributada 

Valor amparado por isenção ou não incidência \(com 2 decimais\) 

13 

96 

108 

N 

15 

Outras 

Valor que não confira débito ou crédito do ICMS \(com 2 decimais\) 

13 

109 

121 

N 

16 

Alíquota 

Alíquota do ICMS \(com 2 decimais\) 

4 

122 

125 

N 

17 

Situação 

Situação da Nota Fiscal 

1 

126 

126 

X 

__\[MFS58872\] __Alteração de regra de Notas Fiscais Canceladas – DIEF\-MA

__Tratamento:__

Se a situação do documento fiscal \(campo 30 da x07\_docto\_fiscal\) = ‘__S’__

     E se a UF do Estabelecimento for igual a __‘MA’__

O campo Situação deve ser preenchido com ‘__S__’

__CH13910\_2013__

__CH18474\_2015__

__MFS11800__

\[__MFS58872__\]

__RN60__

__Registro Tipo 61 \(Bilhetes e passagens\):__

Origem: SAFX07/08

__\[ALTERADA CH10664\_2015\]__

__Regra Geral:__

Deve ser gerado para os documentos fiscais descritos a seguir:

__\[ALTERADA – CH18474\_2015\]__

- Bilhete de Passagem Aquaviário \(modelo 14\)
- Bilhete de Passagem e Nota de Bagagem \(modelo 15\)
- Bilhete de Passagem Ferroviário \(modelo 16\)
- Bilhete de Passagem Rodoviário \(modelo 13\)
- Nota Fiscal de Venda a Consumidor \(modelo 2\)
- Nota Fiscal de Produtor \(modelo 4\)
- Nota Fiscal de Consumidor Eletrônica \(modelo 65\), __EXCETO__ quando a UF do Estabelecimento for igual a PI\. *Observação:* Retirado do Registro 61 para gerar no Registro 50 conforme “Comunicado n° 003/2015 de 10 de agosto de 2015” da SEFAZ/PI\. Aos demais estados mantém a mesma geração\.
- Bilhete de Passagem Eletrônico, \(modelo 63\)

__\[ALTERADA – CH7865\_2017 \(MFS\-10879\)\]__

Desconsiderar os valores dos documentos fiscais CANCELADOS \(campo SITUACAO = S da tabela SAFX07\) nas somatórias de valores: campo 10\-Valor Total, 11\-Base de Cálculo ICMS, 12\-Valor do ICMS, 13\-Isenta ou Não Tributada, 14\-Outras e 15\-Alíquota\.

__CH10664\_2015__

__CH18474\_2015__

__CH7865\_2017 \(MFS\-10879\)__

__MFS15533__

__RN61__

__Registro Tipo 61 – Campo 08 \(Número Inicial de Ordem\):__

Origem: SAFX07/08

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 08 da SAFX07\) que deve corresponder ao número do primeiro documento fiscal emitido no dia do mesmo modelo, série e subsérie\.

__Tratamento:__

Buscar informação mínima do campo Nº NF das Notas de Saída\. Quando o documento fiscal tiver o campo Número maior que 6, deve ser preenchido com os últimos 6 dígitos\.

__CH19583\-A\_2013__

__RN62__

__Registro Tipo 61 – Campo 09 \(Número Final de Ordem\):__

<a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a><a id="OLE_LINK9"></a>Origem: SAFX07/08

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 08 da SAFX07\) que deve corresponder ao número do último documento fiscal emitido no dia do mesmo modelo, série e subsérie\.

__Tratamento:__

Buscar informação máxima do campo Nº NF das Notas de Saída\. Quando o documento fiscal tiver o campo Número maior que 6, deve ser preenchido com os últimos 6 dígitos e se for emitido apenas um documento fiscal na data, deve ser preenchido com o mesmo número indicado no campo 08 \(Número final de ordem\)\.

__CH19583\-A\_2013__

__RN63__

__Registro Tipo 61R \(Resumo Mensal por Item\):__

Origem: SAFX07/08

__\[ALTERADA CH10664\_2015\] __

Considerar todos os modelos de documentos fiscais descritos no Registro Tipo 61 \(RN60\)\.

__\[ALTERADA CH10037\_2013\]__

__Regra Geral:__

Deve ser gerado um registro para cada combinação de código de produto e alíquota, ou seja, se determinado produto saiu do estabelecimento com alíquotas distintas no período informado, deve ser gerado um registro para cada ocorrência desse tipo, além disso, os campos de valores devem ser somados de acordo com esse agrupamento\.

Considerar esse tratamento para geração por Estabelecimento e também por Inscrição Estadual Única, este último considerando quando o parâmetro “Geração para Empresa c/ Insc\. Estadual Única” estiver marcado\.

__CH10037\_2013__

__CH10664\_2015__

__RN64__

__Registro Tipo 88E – Tratamento Geral:__

Este registro estabelece a correspondência entre os códigos definidos pela Secretaria da Fazenda de São Paulo e a codificação utilizada pelo contribuinte informante, conforme registro do tipo 75 \(Portaria CAT 32/96\)\. 

Deverá ser gerado um registro do tipo "88E" correspondente a cada registro do tipo 75 da Portaria CAT 32/96 \(referentes a combustíveis / solventes\)\.

__Tratamento:__

Deve ser ignorado a RN24, com relação aos CFOPs descritos para exclusão do registro tipo 75, quando o usuário selecionar a geração do registro 88E no Perfil, em Parâmetros >> Convênio ICMS 57/95 e Alterações\.

Com isso, todo o registro tipo 75 gerado no arquivo magnético terá que gerar um registro tipo 88E\.

Utilizar a parametrização “Correspondência de Produtos”, em Parâmetros >> Parâmetros p/ CAT 95/03 – SP para identificação dos registros aqui pré\-estabelecidos\.

__CH1063\_2014__

__RN65__

__Registro Especial Tipo 88 L36451 – RJ__

Para geração do registro as informações serão recuperadas a partir dos valores salvos na tela Registro Especial \(Registro 88 L36451 \- RJ\), Manutenção >> Registro Especial \(Registro 88 L36451 – RJ\)\.

O registro __88 L36451 __deverá ser contabilizado com os demais registros no registro tipo 90\.

__A geração do registro 88 L36451\-RJ ficará condicionado á seguinte regra:__

- Quando estiver habilitado o parâmetro geração do Registro 88 L36451 – RJ, em Parâmetros >> Convênio ICMS 57/95 e Alterações >> perfil\.

 

__As regras para criação e preenchimento dos campos pertencentes ao registro estão especificadas abaixo:__

No primeiro arquivo entregue pelo estabelecimento com o registro 88, além das informações do mês de apuração o estabelecimento deverá informar os registros múltiplos referentes aos 12 meses anteriores ao mês de apuração\.

__Tela\-A__ ç tela menu Manutenção >> Registro Especial \( Registro 88 L36451 – RJ\)

- O sistema deverá gerar registro onde a coluna __<<Mês/Ano Apuração>>__ da __Tela\-A __estiver dentro da __Data inicial__ e __Data Final__ da __“__Geração do Meio Magnético ICMS, e o Estabelecimento da __Tela\-A __for igual ao Estabelecimento escolhido na __“Geração do Meio Magnético”__\.

__Leiaute do Registro:__

![](data:image/png;base64,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)

Campo 01 – Preencher com texto fixo com "88";

 

Campo 02 \- Preencher com texto fixo "L36451";

Campo 03 – Preencher com o valor da coluna __<<Mês/Ano Referência>> __da __Tela\-A__,__ __utilizar o formato AAMM\.

Campo 04 \- Preencher com o valor da coluna __<<Valor ICMS Normal>> __da __Tela\-A__\.

Campo 05 \- Preencher com o valor da coluna __<<Valor ICMS Importação>> __da __Tela\-A__\. 

Campo 06 \- Preencher com o valor da coluna __<< Valor ICMS Total>> __da __Tela\-A__\.

Campo 07 \- Preencher com o valor da coluna __<<Valor da UFIR Mês de Referência>> __da __Tela\-A\.__

Campo 08 \- Preencher com o valor do resultado entre a divisão do campo __06 \-__ __<< Valor ICMS Total>> __pelo campo __07 \-__ __<<Valor da UFIR Mês de Referência>> __da __Tela\-A__\.

Campo 09 \- Preencher com o valor da coluna __<< Valor ICMS Total UFIR mesmo mês ano anterior >> __da __Tela\-A\.__

Campo 10 \- Preencher com o valor da coluna __<<Valor de Recolhimento UFIR dia 05>> __da __Tela\-A\.__

 

Campo 11 \- Preencher com o valor da coluna __<<Valor de Recolhimento UFIR dia 20>> __da __Tela\-A__\.

Campo 12 \- Preencher com o valor da coluna __<<Valor de Recolhimento UFIR dia 10>> __da __Tela\-A\.__

15 \- CAMPO 13 \- Preencher com espaços em branco\.

__ __

__OS4635__

__RN66__

__Registro Tipo 54:__

__Regra Geral:__

- Deve ser gerado um registro para cada produto ou serviço constante da nota fiscal e/ou romaneio\.
- Deve ser gerado um registro tipo 50 para cada registro 54 de acordo com a concatenação das informações relativos a “CFOP” e “Alíquota”\. Em suma, na hipótese de haver uma nota fiscal com 2 ou mais itens deve ser criado um registro 50 para tantas quantas forem as combinações entre CFOP e Alíquota existentes na SAFX08\.

__Regra dos Campos:__

Nº 

Denominação do Campo 

Conteúdo 

Tamanho 

Posição 

Formato 

Preenchimento MSAF

01 

Tipo 

"54" 

2 

1 

2 

N 

02 

CNPJ 

CNPJ do remetente nas entradas e do destinatário nas saídas 

14 

3 

16 

N 

Se a NF for modelo igual a “65” \(princípio estabelecido para Piauí conforme regra geral\), esse campo será preenchido com a informação do CPF/CNPJ do Consumidor da SAFX07\.

Senão, se o campo CPF/CNPJ do Consumidor da SAFX07 não estiver informado será preenchido com a informação do campo CPF\-CGC da SAFX04\. Caso não houver cadastro na SAFX04 preencher com zeros\.

Os demais modelos de NF serão preenchidos com base na informação do campo CPF\-CGC da SAFX04\.

03 

Modelo 

Código do modelo da nota fiscal 

2 

17 

18 

N 

04 

Série 

Série da nota fiscal 

3 

19 

21 

X 

05 

Número 

Número da nota fiscal 

6 

22 

27 

N 

06 

CFOP 

Código Fiscal de Operação e Prestação 

4 

28 

31 

N 

07 

CST 

Código da Situação Tributária 

3 

32 

34 

X 

08 

Número do Item 

Número de ordem do item na nota fiscal 

3 

35 

37 

N 

09 

Código do Produto ou Serviço 

Código do produto ou serviço do informante 

14 

38 

51 

X 

10 

Quantidade 

Quantidade do produto \(com 3 decimais\) 

11 

52 

62 

N 

11 

Valor do Produto 

Valor bruto do produto \(valor unitário multiplicado por quantidade\) \- com 2 decimais 

12 

63 

74 

N 

12 

Valor do Desconto / Despesa Acessória 

Valor do Desconto Concedido no item \(com 2 decimais\)\. 

12 

75 

86 

N 

13 

Base de Cálculo do ICMS 

Base de cálculo do ICMS \(com 2 decimais\) 

12 

87 

98 

N 

14 

Base de Cálculo do ICMS para Substituição Tributária 

Base de cálculo do ICMS de retenção na Substituição Tributária \(com 2 decimais\) 

12 

99 

110 

N 

15 

Valor do IPI 

Valor do IPI \(com 2 decimais\) 

12 

111 

122 

N 

16 

Alíquota do ICMS 

Alíquota Utilizada no Cálculo do ICMS \(com 2 decimais\) 

4 

123 

126 

N 

__MFS11800__

__RN67__

__Registro Tipo 70:__

Origem: SAFX07/08

__Regra Geral:__

Deve ser gerado para os documentos fiscais descritos a seguir:

- Registro de total de Nota Fiscal de Serviço de Transporte \(modelo 7\)
- Conhecimento de Transporte Rodoviário de Cargas \(modelo 8\)
- Conhecimento de Transporte Aquaviário de Cargas \(modelo 9\)
- Conhecimento Aéreo \(modelo 10\)
- Conhecimento de Transporte Ferroviário de Cargas \(modelo 11\)
- Conhecimento de Transporte Eletrônico \(modelo 57\)
- Conhecimento de Transporte Eletrônico para Outros Serviços \(modelo 67\)

__\[ALTERADA \- MFS\-23075\]__

Notas fiscais de modelo \(campo 13\-COD\_MODELO da tabela SAFX07\) igual a "57" e “67” em que a Série \(campo 09\-SERIE\_DOCFIS da tabela SAFX07\) possuir mais que uma posição: 

Se a Subsérie \(campo 10\-SUB\_SERIE\_DOCFIS da tabela SAFX07\) igual a “Vazio/Nulo”:

Preencher no campo Subsérie do Registro Tipo 70 \(posição 44 a 45\) com os dois últimos caracteres do campo 09\-SERIE\_DOCFIS da tabela SAFX07 

Senão campo Subsérie do Registro 70 deverá ser igual ao campo 10\-SUB\_SERIE\_DOCFIS da tabela SAFX07\.

__MFS15533__

__MFS\-23075__

__RN68__

__Registro Tipo 70 – Campo 17 \(Situação\):__

Origem: SAFX07/08

Preencher com o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL \(campo 30 da SAFX07\)\.

__Tratamento:__

Se o modelo documento \(campo 13 da SAFX07\) = 57 ou 67

     Se o Indicador de Nfe denegada/inutilizada  \(campo 231 da SAFX07\) = 1 \(Nota Fiscal Eletrônica denegada\)

          O campo Situação deve ser preenchido com 2

     Senão Se o Indicador de Nfe denegada/inutilizada  \(campo 231 da SAFX07\) = 2 \(Nota Fiscal Eletrônica inutilizada\)

          O campo Situação deve ser preenchido com 4

__MFS15533__

__RN69__

__Tratamento para Nota de Entrada Cancelada__

Para tratamento do Documento Fiscal \(SAFX07\) de entrada \(MOVTO\_E\_S\) <> ‘9’ cancelado, temos os parâmetros na Tela de Perfil \(vide Parâmetros >> Convênio ICMS 57/95 e Alterações >> Perfil\):

\- “Não Gerar Notas de Entrada Canceladas Emitidas por Terceiros”

\- “Não Gerar Notas de Entrada Canceladas de Emissão Própria” \[parâmetro criado pela MFS32268\]

Caso o parâmetro “Não Gerar Notas de Entrada Canceladas Emitidas por Terceiros” esteja marcado, as notas com MOVTO\_E\_S = ‘1’ CANCELADAS, não são geradas no meio magnético SINTEGRA\.

\[MFS32268\]

Caso o parâmetro “Não Gerar Notas de Entrada Canceladas de Emissão Própria” esteja marcado, as notas com MOVTO\_E\_S = ‘2’, ‘3’, ‘4’ e ‘5’ CANCELADAS, não são geradas no meio magnético SINTEGRA\.

MOVTO\_E\_S : campo 03 \- Movimento Entrada/Saída da SAFX07\.

Registros do Sintegra afetados: 50, 51, 53, 54, 56, 57, 61, 70, 71, 77\.

__MFS32268__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

