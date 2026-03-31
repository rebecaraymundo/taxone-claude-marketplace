# MTZ-ICMS-Livro_de_Saidas

- **Fonte:** MTZ-ICMS-Livro_de_Saidas.docx
- **Modificado:** 2026-01-30
- **Tamanho:** 63 KB

---

# Módulo – ICMS \- Livros de saídas Normais

__Módulo:__ Estadual → ICMS

__Menu:__ Datamart → Emissão Livro de Saída P2 → Ajuste Sinief

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__CH53090/__

__OS 2715__

Item 77 e 78 

Corrigir a parte principal dos livros fiscais de entrada e saídas quando os parâmetros 77 e 78 em Parâmetros por UF __não__ estiverem selecionados\.

__OS 2715/ __

__CH54397__

Alteração OBS Livros Entrada e Saídas

Alterar as observações nos livros de ICMS de entradas e saídas geradas pelos parâmetros por UF 23 e 25, que geram observações de ICMS\-S, quando a NF é tributada\. Atualmente gera apenas o valor do imposto, mas conforme RICMS\-SP, arts 275 \(LS\) e 276 \(LE\), também é necessário incluir o valor da base de cálculo\.

__CH82580/ OS3165__

Ajuste Sinief para identificar as NF\-e denegadas ou inutilizadas 

Ajustar a apresentação das NF\-e inutilizadas ou denegadas nas observações do livro fiscal\.

__CH101651__

Alterar a regra de demonstração de NF cancelada no livro de saída – P2

Alterar a regra de demonstração de NF cancelada no livro de saída – P2

__OS3227__

Alterar o tratamento para Notas Fiscais extemporâneas

Apresentar no livro apenas os dados para identificação do documento quando se tratar de NF extemporânea de saída\.

__OS3384__

Alteração na Observação dos Livros

Considerar a regra do parâmetro “87” de parâmetros por UF\.

__OS3165__

Identificar as NF\-e denegadas ou inutilizadas

Ajustar a apresentação das NF\-e inutilizadas ou denegadas nas observações do livro fiscal \(P2, P2A\)

__OS3375__

Correção P1 e P1A

Correção do lançamento dos valores das bases isenta/redução e base outras\.  

__OS3526__

Alterar o tratamento para Notas Fiscais especiais = “D”

Apresentar no livro apenas os dados para identificação do documento quando se tratar de NF especial “D – Operação de Compra/Venda para entrega Futura\.”\.

__OS3046__

Alteração do Livro de Saídas

Alteração da observação “Faturamento Direto ao Consumidor”, que passará a utilizar dois formatos distintos \(vide __RN09__\)\.

__OS4786__

__\(22/05/15\)__

Alteração na geração do Convênio 115 p/tratamento do modelo 

Separar os documentos fiscais de modelos diferentes em arquivos distintos \(ver __RN10__\)\. 

__MFS9139 \(CH188\_2017\)__

Alterar o tratamento para Notas Fiscais extemporâneas

Apresentar no livro apenas os dados para identificação e valor Contabil do documento quando se tratar de NF extemporânea de saída\.

__CH14989\_2017 \(MFS12955\)__

Alterar o tratamento para Notas Fiscais especiais = “D” para a UF do CE

Quando se tratar de estabelecido na UF do CE apresentar no livro os dados para identificação do documento, valor contábil e observações ao se tratar de NF especial “D – Operação de Compra/Venda para entrega Futura\.” Com CFOP 5922 e 6922\.

__CH20938\_2017__

__\(MFS\-14403\)__

Alterar o tratamento para Notas Fiscais especiais = “D” para a UF do RS também\.

Quando se tratar de estabelecido na UF do RS apresentar no livro os dados para identificação do documento, valor contábil e observações ao se tratar de NF especial “D – Operação de Compra/Venda para entrega Futura\.” Com CFOP 5922 e 6922\.

__CH20938\_2017__

__\(MFS\-14944\)__

Inclusão de CFOPs 

Quando se tratar de estabelecidos nas localidades da UF do CE e RS apresentar no livro os dados para identificação do documento e observações\. Porém, não apresentar os valores contábeis ao se tratar de NF especial “D – Operação de Compra/Venda para entrega Futura\.” Com CFOP 5117 e 6117\.

__CH6363\_2018__

__\(MFS\-17310\)__

Revisão da Regra RN08\.

Conforme verificado a legislação do RS determina que, no caso de operação de venda para entrega futura: nota Fiscal para simples faturamento \(CFOPs 5\.922 e 6\.922\) será registrada com indicação apenas na coluna "VALOR CONTÁBIL" e sem indicação dos valores na coluna "ICMS VALORES FISCAIS"\. Nota Fiscal relativa à efetiva saída das mercadorias \(CFOPs 5\.116/ 6\.116 e 5\.117/6\.117\) será registrada sem indicação na coluna "VALOR CONTÁBIL" e com indicação dos valores na coluna "ICMS VALORES FISCAIS"\. 

__MFS1033222__

Esclarecimento sobre a regra de documentos de Utilities

No caso de documentos de Utilities, há duas formas de gerar o livro P2: através da rotina de consolidação \(antigo mapa resumo\) ou por incrição estadual única\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Para os livros fiscais de Saídas para empresas com Inscrição Estadual Única:__

è Em Parâmetros por UF, quando o item 78 \( Modelo de Livro P2/P2A\)   estiver desmarcado, para documentos fiscais mistas \( mercadorias e serviços \), tabela SAFX07, item 12 COD\_CLASS\_DOC\_FIS= 3, deverá ser exibida um único Valor Contábil  de forma sumarizada na parte principal dos livros fiscais, contabilizando o valor contábil do item de  mercadoria com o  valor contábil do item de serviço\.

A coluna do CFOP, base de Cálculo, Alíquota, Imposto Debitado/não\-tributadas e Outras continuam sendo exibidas por item em linhas diferentes\.

Caso item 12, da tabela SAFX07,  COD\_CLASS\_DOC\_FIS <> 3, os livros não sofrerão alterações\.

Os livros que sofrerão esta correção são:

èModelo P2

	è Ajuste SINIEF

	èConvênio ICMS

	èConvênio ICMS RS

  èDecreto 27\.427/00 \- RJ

èModelo P2A

	è Ajuste SINIEF

	èConvênio ICMS

  èDecreto 27\.427/00 \- RJ

CH53090

__RN01__

__Para os livros fiscais de Saídas normais__

è Em Parâmetros por UF, quando os itens 23 \(Lançar ICMS\-S com crédito nas Observações \(P1/P1A\) e 25 \(Lançar ICMS\-S com crédito nas Observações \(P2/P2A\)\) estiverem marcados, deve\-se para documentos fiscais com itens de mercadorias e ICMS\-S tributado, gerar uma observação contendo o Valor do Imposto e a sua respectiva Base de Cálculo\.

Os Livros de que sofrerão correção são:

èModelo P2/P2A

     èAjuste SINIEF

     èConvênio ICMS

				

èModelo P2A

     èAjuste SINIEF

     èConvênio ICMS

__RN02__

Na geração do livro fiscal através do menu: __Datamart > Emissão Livro de Saídas > Modelo P2 e P2A >__ __Ajuste SINIEF e Convênio ICMS__, quando uma __NF cancelada for gerada nas observações do livro__, o sistema deve verificar:

\- Se o documento fiscal for um documento denegado \(campo IND\_NFE\_DENEG\_INUT = ‘1’ da SAFX07\), gravar a informação ‘Nota Fiscal Denegada Número: <NUM\_NF>’;

\- Se o documento fiscal for um documento inutilizado \(campo IND\_NFE\_DENEG\_INUT = ‘2’ da SAFX07\), gravar a informação ‘Nota Fiscal Inutilizada Número: <NUM\_NF>’;

\- Senão, gravar a informação ‘Nota Fiscal Cancelada Número: <NUM\_NF>’\.

__\[ALTERADA – OS3165\]__

__Módulo: __Estadual → ICMS

__Menu:__ DATAMART → Emissão Livros de Saída 

Sendo: 

__P2 → Ajuste Sinief, Convênio ICMS, Convênio ICMS RS e Outros Atos Legais__

__P2A → Ajuste Sinief, Convênio ICMS e Outros Atos Legais__

__P2 Consolidado → Ajuste Sinief, Convênio ICMS e Convênio ICMS MG__

__P2A → Ajuste Sinief, Convênio ICMS e Convênio ICMS MG__

O sistema deve recuperar as informações da SAFX130 \- Documentos Fiscais Eletrônicos Denegados ou Inutilizados, e gravar a informação, no campo Observações, dos Livros de Saída conforme abaixo:

\- Campo 08 \- DATA\_REF \(SAFX130\) for pertinente ao período de geração\.

Na emissão do Livro de Saídas, quando uma __NF cancelada for gerada nas observações do livro__, o sistema deve verificar:

\- Se o documento fiscal for um documento denegado \(Campo 10 \- IND\_SITUACAO = ‘1’ – SAFX130\), gravar a informação ‘__Nota Fiscal Eletrônica Denegada Número: <NUM\_NF>’__ ;

\- Se o documento fiscal for um documento inutilizado \(Campo 10 \- IND\_SITUACAO = ‘2’ – SAFX130\), gravar a informação __‘Nota Fiscal Eletrônica Inutilizada Número: <NUM\_NF>’__;

Na coluna Observações, campo Código do Destinatário, deverá ser gerado em branco\.

Somente gravar o número da nota fiscal \(individualmente\) e valor monetário, que deve estar zerado\.

Além de recuperar as NF’s Denegadas da SAFX07, deve recuperar também da SAFX130, conforme regra acima\.

No caso de NF’s Inutilizadas deve recuperar pela SAFX130, uma vez que a NF não chegou a ser emitida\.

__CH82580/__

__OS3165__

__RN03__

__Regra para alterar a visualização de NF cancelada no livro de saída P2:__

__Módulo:__ Estadual → ICMS

__Menu:__ Datamart → Emissão Livro de Saída P2 → Ajuste Sinief

 Na emissão do Livro de Saída P2 \(102\), quando se tratar de __NOTA FISCAL CANCELADA__ \(Safx07 \- campo 30 – Situação = ‘S’, ou seja, regularmente cancelada\), o campo Valor Contábil \(Livro de Saída P2\) deve ser preenchido por 0,00\.

__CH101651__

__RN04__

__Regra para notas fiscais extemporâneas__

__Módulo: __Estadual à ICMS

1. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2 à Ajuste SINIEF
2. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2 à Convênio ICMS
3. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2 à Convênio ICMS RS
4. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2 à Outros ATOS Legais
5. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2 Consolidado à Ajuste SINIEF
6. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2 Consolidado à Convênio ICMS
7. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2 Consolidado à Convênio ICMS MG
8. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2A à Ajuste SINIEF
9. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2A à Convênio ICMS
10. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2A à Outros ATOS Legais
11. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2A Consolidado à Ajuste SINIEF
12. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2A Consolidado à Convênio ICMS
13. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2A Consolidado à Convênio ICMS MG

Quando se tratar de Nota fiscal extemporânea de saída, ou seja, se o campo DAT\_ESCR\_EXTEMP \(Item 77 da SAFX07\) > 0, então:

Apresentar no livro apenas os dados de identificação do documento, ou seja, os campos de valores devem ser zerados\. A nota extemporânea de saída também deve ser desconsiderada em todos os resumos deste livro, seja por UF, Alíquota, CFOP, ICMS\-ST, etc\. Os campos que devem ser zerados são os que estão listados abaixo:

*Item de relatório* à Principal

__Campos:__ Valor Contábil, __MFS9139\(CH188\_2017\)__

Contábil, __MFS9139\(CH188\_2017\)__

Base Cálculo,  

Alíquota, 

Imposto debitado\.

Isentas ou não tributadas \(Operações sem débido do imposto\),

Outras \(Operações sem débido do imposto\)\.

Codificação – Fiscal,

ICMS / IPI\.

*Item de relatório à  RESUMO POR UF*

__Campos: __Valor contábil \(Não contribuinte e Contribuinte\), __MFS9139\(CH188\_2017\)__

Base de Cálculo\(Não contribuinte e Contribuinte\),

Outras,

ICMS Cobrado por Substituição tributária\.

*Item de relatório à RESUMO POR ALÍQUOTA*

__Campos:__ Base de Cálculo,

Alíquota,

Valor ICMS\.

*Item de relatório: RESUMO CFO*

__Campos:__ Valor Contábil \(Sub Total por CFOP e Totais gerais\), __MFS9139\(CH188\_2017\)__

Base de cálculo \(Sub Total por CFOP e Totais gerais\),

Imposto debitado \(Sub Total por CFOP e Totais gerais\)\.

Isentas ou não tributadas \(Operações sem débido do imposto\),

Outras \(Operações sem débido do imposto\)\.

Código Fiscal,

ICMS / IPI\.

Para os demais *itens de relatório*, não sumarizar os valores\.

__OS3277__

__MFS9139\(CH188\_2017\)__

__RN05__

__Considerar o Parâmetro “87” de parâmetros por UF:__

Considerar a configuração do parâmetro “87 \- Considerar Observações de Informações Complementares da Nota \(SAFX112\) para livros \(P2 e P2A\)” que altera a regra de geração para as OBSERVAÇÕES:

Para informação sobre o funcionamento do parâmetro, consultar o documento matriz “Mtz \- ICMS \- Parâmetros por UF\.doc”

__Módulo: __Estadual à ICMS

__Localização Livro P2 – Código 102:__

1. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2 à Ajuste SINIEF
2. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2 à Convênio ICMS
3. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2 à Convênio ICMS RS
4. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2 à Outros ATOS Legais
5. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2 Consolidado à Ajuste SINIEF
6. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2 Consolidado à Convênio ICMS
7. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2 Consolidado à Convênio ICMS MG

__Localização Livro P2A – Código 104:__

1. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2A à Ajuste SINIEF
2. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2A à Convênio ICMS
3. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2A à Outros ATOS Legais
4. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2A Consolidado à Ajuste SINIEF
5. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2A Consolidado à Convênio ICMS
6. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2A Consolidado à Convênio ICMS MG

__Localização Livro P2 de Inscrição estadual única \- Código 163__

1. __Menu__: DataMart à Livros Fiscais p/ Empresas c/ Insc\. Estadual Única à Emissão Livro de Saídas à Modelo P2 – Convênio ICMS

__Localização Livro P2A de Inscrição estadual única \- Código 164__

1. __ Menu__: DataMart à Livros Fiscais p/ Empresas c/ Insc\. Estadual Única à Emissão Livro de Saídas à Modelo P2A – Convênio ICMS

Se o parâmetro 87 estiver selecionado e o tipo da observação for informação complementar da nota, ou seja, campo 13 da SAFX112 = “I”, gerar no resumo “OBSERVAÇÔES” dos livros \(P1 e P2\) as observações cadastradas nos campos abaixo:

1. Campo 03 \(DESCRICAO\) da SAFX2009 correspondente ao código cadastrado no campo 12 \(COD\_OBS\_LANCTO\_FISCAL\) da SAFX112\.
2. Campo 14 \(DSC\_COMPLEMENTAR\) da SAFX112\.

Quando houver informação complementar na SAFX112 então devem ser apresentadas as duas observações apenas com a separação de um traço \(Item 1 e 2\)\.

__OS3384__

__RN07__

Os livros de saída do modelo Ajuste SINIEF \(P2 e P2A\), que apresentam os valores das bases \(tributada, isenta/redução e outras\) em linhas distintas, devem fazer o lançamento das bases da seguinte forma:

Consolidação dos valores por documento fiscal:

As bases tributadas devem ser totalizadas por Imposto \(ICMS, IPI ou ST\), CFOP e Alíquota

As demais bases \(isenta/redução e outras\) devem ser totalizadas por Imposto \(ICMS, IPI ou ST\) e CFOP\. Neste caso, a alíquota não precisa ser considerada, uma vez que ela não aparece nas linhas referentes a estes valores\.

__ __

__Exemplo__: Supondo uma nota com os seguintes itens:

__   Aliq ICMS__

__      ICMS__

__      BASE 1 __

__      BASE 2__

__       BASE 3__

__      BASE 4__

Item 1 \(cfop 5101\)

0,00

0,00

0,00

100,00

0,00

0,00

Item 2 \(cfop 5101\)

10,00

8,00

80,00

20,00

0,00

0,00

Item 3 \(cfop 5101\)

12,00

48,00

400,00

0,00

0,00

0,00

A demonstração das bases no livro deve será feita da seguinte forma:

__CFOP__

__ICMS / IPI__

__Cod__

__Base de Cálculo__

__Alíquota__

__Imposto Creditado__

5101

ICMS

1

80,00

10,00

8,00

5101

ICMS

1

400,00

12,00

48,00

5101

ICMS

2

120,00

__OS3375__

__RN08__

__Regra para Notas Fiscais Especiais = “D \- Operação de Compra/Venda para entrega Futura”__

__Módulo: __Estadual à ICMS

1. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2 à Ajuste SINIEF
2. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2 à Convênio ICMS
3. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2 à Convênio ICMS RS
4. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2 à Outros ATOS Legais
5. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2 Consolidado à Ajuste SINIEF
6. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2 Consolidado à Convênio ICMS
7. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2 Consolidado à Convênio ICMS MG
8. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2A à Ajuste SINIEF
9. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2A à Convênio ICMS
10. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2A à Outros ATOS Legais
11. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2A Consolidado à Ajuste SINIEF
12. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2A Consolidado à Convênio ICMS
13. __Menu: __DataMart à Emissão do livro de Saídas à Modelo P2A Consolidado à Convênio ICMS MG

__\[ALTERADA \- CH14989\_2017 \(MFS12955\)\]__

__\[ALTERADA – CH20938\_2017 \(MFS14403\)\]__

__\[ALTERADA – CH20938\_2017 \(MFS14944\)\]__

__\[ALTERADA – CH6363\_2018 \(MFS17310\)\]__

SE nos Parâmetros p/ UF do módulo ICMS, item de menu Manutenção, estiver com o campo UF diferente de “CE” e “RS”

      SE for Nota Fiscal com operação de compra/venda para entrega futura campo IND\_SITUACAO\_ESP \(item 125 da SAFX07\) igual a “D“;

            SE for CFOP campo COD\_CFO \(item 14 da SAFX07, 22 da SAFX08 ou 17 da SAFX09\) igual a “5922, 6922”, então:

Demonstrar nos Livros P2 apenas os dados de identificação do documento e “VALOR CONTÁBIL”, acrescentar uma observação automática com a descrição “Simples Faturamento”, os demais campos \(de valores\) deverão aparecer zerados, isso serve para todos os itens desse Livro, seja por UF, Alíquota, CFOP, ICMS\-ST, etc\. Os campos que devem ser zerados são os listados conforme segue:

*Item de relatório à Principal*

__Campos: __Base Cálculo, 

Alíquota, 

Imposto debitado\.

Isentas ou não tributadas \(Operações sem débito do imposto\),

Outras \(Operações sem débito do imposto\)\.

Codificação – Fiscal,

ICMS / IPI\.

*Item de relatório à RESUMO POR UF*

__Campos: __Base de Cálculo\(Não contribuinte e Contribuinte\),

Outras,

ICMS Cobrado por Substituição tributária\.

*Item de relatório à RESUMO POR ALÍQUOTA*

__Campos:__ Base de Cálculo,

Alíquota,

Valor ICMS\.

*Item de relatório à RESUMO CFO*

__Campos:__ Base de cálculo \(Sub Total por CFOP e Totais gerais\),

Imposto debitado \(Sub Total por CFOP e Totais gerais\)\.

Isentas ou não tributadas \(Operações sem débido do imposto\),

Outras \(Operações sem débido do imposto\)\.

Código Fiscal,

ICMS / IPI\.

Para os demais *itens de relatório*, não sumarizar os valores\.

OU

SE nos Parâmetros p/ UF do módulo ICMS, item de menu Manutenção, estiver com o campo UF igual a “CE” e “RS”

      SE for Nota Fiscal com operação de compra/venda para entrega futura campo IND\_SITUACAO\_ESP \(item 125 da SAFX07\) igual a “D“;

            SE for CFOP campo COD\_CFO \(item 14 da SAFX07, 22 da SAFX08 ou 17 da SAFX09\) igual a

“5116”, “5117”, “6116”, ”6117” ou “7116”, então: Demonstrar nos Livros P2 a __coluna “VALOR CONTÁBIL” sem valor__ preenchido\. Os demais campos \(de valores\) deverão aparecer com preenchimento, isso serve para todos os itens desse Livro, seja por UF, Alíquota, CFOP, ICMS\-ST, etc\. 

__OS3526__

__CH14989\_2017 \(MFS12955\)__

__       CH20938\_2017__

__\(MFS\-14403\)__

__CH20938\_2017__

__\(MFS\-14944\)__

__CH6363\_2018__

__\(MFS\-17310\)__

__RN09__

Observação automática do “__FATURAMENTO DIRETO AO CONSUMIDOR__”:

Esta observação é gerada de forma automática nos livros de saída, a partir das seguintes condições:

\(condições verificadas em testes realizados em Jul/2012\) 

- 
	- 
		- 
			- 
				1. Quando o parâmetro “43\-Obs p/ Faturamento Direto ao Consumidor”  \(Parâmetros por UF\) estiver marcado p/a UF do Estabelecimento; 
				2. Quando na __*capa*__ da nota \(__SAFX07__\), o campo “106\-Base ICMS Origem/Destino” __*ou*__ o campo “107\-Valor ICMS Origem/Destino” tiver preenchido com um valor > 0;

__Alteração da OS3046:__

Todos os livros de saídas gerados nos menus descritos abaixo, exceto a opção do “Convênio ICMS RS”, foram alterados quanto ao tratamento do parâmetro “43\-Observação p/Faturamento Direto ao Consumidor” da parametrização por UF\. 

Datamart à Emissão Livro de Saídas à Modelo P2                               \(todas as opções __*exceto*__ a “Convênio ICMS RS”\)

Datamart à Emissão Livro de Saídas à Modelo P2A                             \(todas as opções\)

Datamart à Emissão Livro de Saídas à Modelo P2 Consolidado        \(todas as opções\)

Datamart à Emissão Livro de Saídas à Modelo P2A Consolidado     \(todas as opções\)

Originalmente, a observação gerada continha apenas o conteúdo “Faturamento Direto ao Consumidor”\.

Nesta OS foram criadas duas alternativas para geração desta observação:

Opção 1 à __Demonstrar apenas “Faturamento Direto ao Consumidor”__: 

 \(esta opção também será utilizada como default, no caso dos parâmetros cadastrados antes desta alteração, em que a coluna da tabela esteja sem preenchimento\)

  

     Neste caso,  será gerado apenas o conteúdo “Faturamento Direto ao Consumidor” \(conforme o funcionamento original\)\. 

Opção 2 à __Demonstrar também os valores do ICMS referente às outras UF’s__:

     Neste caso, será demonstrado também o valor da base de cálculo e do ICMS Origem/Destino, como exemplificado a seguir:

   *Faturamento Direto ao Consumidor \- Conv  51/00 \- Base ICMS Destino R$ 999\.999\.999,99, Valor ICMS Destino R$ 999\.999\.999,99*

Obs: No caso dos livros em que o resumo das observações tem limitação no tamanho das observações demonstradas \(têm apenas 3 colunas de 50 caracteres\), a observação poderá ser dividida em três partes: 

Parte 1 à *Faturamento Direto ao Consumidor*

Parte 2 à *Conv 51/00 \- Base ICMS Destino R$ 999\.999\.999,99*

Parte 3 à *Valor ICMS Destino R$ 999\.999\.999,99*

Os valores citados *são os mesmos valores utilizados como critério para impressão ou não da observação*\. Trata\-se dos seguintes campos da SAFX07:

- Campo “106\-Base ICMS Origem/Destino” da SAFX07
- Campo “107\-Valor ICMS Origem/Destino” da SAFX07

__OS3046__

__RN10__

*\(Módulo ICMS, menu “Parâmetros por UF”\)*

Utilização do parâmetro:

__Parâmetro 51__: __*Emissão do Livro de Saídas \(P2/P2A\) conforme Convênio ICMS 115*__*”:*

Este parâmetro é utilizado nas opções do Livro de Saídas P2/P2A do Ajuste SINIEF, e também nos livros por Inscrição Estadual Única\.

  

Sempre que os livros de saídas são gerados com este parâmetro ativado, é gerada uma linha na parte principal do livro para cada volume de arquivo Mestre do Conv\. 115 existente para o período\. 

Esta linha mostra o número do primeiro e do último documento fiscal contido no arquivo, e os valores totais de todos os documentos\. As colunas “UF Dest”, “Contábil” e “Fiscal” __não são preenchidas\.__

Além da parte principal do livro, também é gerada uma linha na parte das observações, para cada linha que foi gerada na parte principal\. Nesta linha aparece o nome do arquivo e sua chave de codificação digital \(hash code\)\. E abaixo das informações de cada arquivo Mestre, são demonstradas as seguintes informações referentes ao arquivo:

\- Resumo dos valores de ST por UF;

\- Resumo das deduções por espécie \(Classificação do Item\);

Todas as informações demonstradas na parte principal e nas observações do livro são recuperadas das tabelas: __ICT\_MM\_CONV115__  e  __ICT\_MM\_CONV115\_UF\_ST__\.

Alteração da __OS4786__: A partir desta OS, os arquivos do Conv\.115 passaram a ser gerados por Série e Modelo\. Como o modelo *não* faz parte do nome do arquivo, poderão existir arquivos de mesmo nome, mas conteúdo diferente, sendo um para cada modelo \(modelo 21 e 22 por exemplo\)\. Na prática, os procedimentos realizados na emissão do livro *não* tiveram alterações em seu funcionamento, apenas os ajustes internos, necessários p/o tratamento das tabelas que contém os dados do Convênio utilizados no livro \(ICT\_MM\_CONV115 e ICT\_MM\_CONV115\_UF\_ST\)\.

__RN11__

__Tratamento do Parâmetro “44” de parâmetros por UF:__

Zera valores de base e tributo do ICMS e ICMSS\.

__RN12__

__Regra para documentos de Utilities__

__ __

Há duas formas de gerar o livro P2 para documentos de Utilities \(SAFX42 E SAFX43\)\.

 

1. Realizar a rotina de consolidação \(antigo mapa resumo\):

Estadual > ICMS > DataMart > Consolidação de documentos de utilities\. Esse processo é responsável por alimentar as tabelas de documentos fiscais \(SAFX07, SAFX08 E SAFX09\)\.

 

1. Caso seja necessário recuperar os documentos de utilities sem a utilização do processo de consolidação, a geração do livro deve ser realizada através do caminho: Estadual > ICMS > DataMart > Livro Fiscal p/ empresa c/ inscrição estadual única > Emissão Livro de Saídas > Modelo P2 \- Convênio ICMS, com a marcação do item 51 nos parâmetros por UF\.

__MFS1033222__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

