# MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Cálculo Média Ponderada

- **Fonte:** MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Cálculo Média Ponderada.docx
- **Modificado:** 2024-04-22
- **Tamanho:** 147 KB

---

	

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS 

\(IN\-RE 087/2020\) 

Cálculo da Média Ponderada Móvel dos Valores Unitários 

__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS\-ST \- RS \(IN\-RE 048/2018\), itens:

Geração à IN\-RE 087/20 à Geração dos Movimentos

	

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS48753__

Liliane Videira Assaf

Criação da funcionalidade\.

Esta entrega não estão sendo contemplados:

\- Parametrização com Produtos Associados

22/12/2020 

__MFS66171__

Liliane Videira Assaf

Hoje calculamos o campo “Valor Médio Unitário do ICMS\-ST” sem FECEP\. 

Precisamos criar um outro campo para o “Valor Médio Unitário ICMS\-ST __c/__ FECEP”\. E renomear o campo “Valor Médio Unitário do ICMS\-ST” para “Valor Médio Unitário ICMS\-ST __s/__ FECEP”\.

07/06/2021

__MFS69798__

Liliane Videira Assaf

Correção no cálculo do Saldo Inicial do primeiro dia do Mês, para sempre considerar a quantidade do inventário do último dia do mês anterior\. Erradamente estava sendo considerada a quantidade da tabela de média ponderada do último dia do mês anterior\.

03/08/2021

__MFS72212__

Liliane Videira Assaf

Criação do Cálculo dos Valores Unitários Médios do Inventário\.

09/09/2021 

__MFS72429__

Andréa Rocha

Inclusão do arredondamento dos valores calculados, ou seja, os valores calculados não serão mais truncados\.  Conforme informação passada pela SEFAZ/RS\.

30/09/2021

__MFS81749__

Liliane Assaf

Tratamento para Notas de Produtos Farmacêuticos de Distribuidores criada pela MFS66473

15/03/2022

__MFS84145__

Andréa Rocha

Alteração no cálculo do Saldo Inicial para o campo Valor de ICMS\-ST Médio, para abater o valor do FECEP Médio incluído no valor do ICMS\-ST Médio, quando a origem dos dados for da tabela do Inventário por Produto

11/04/2022

__MFS90131__

Liliane Assaf

Chamado Lasa/Magalu: Tratamento na diferença de 0,000001 do valor médio unitário do último dia do mês para o do primeiro dia do mês seguinte\. 

01/08/2022

__MFS89648__

Liliane Assaf

Atualização legal IN55/22:

Alteração no Saldo Inicial para tratar dois cenários:

\- Valor Médio Ponderado Móvel calculado ao final do dia anterior negativo \(19\.3\-A\.2\.2\.2\)

\- Quantidade final do dia anterior zerada \(19\.3\-A\.2\.2\.3 da IN\-045/98\)

10/08/2022

__MFS92151__

Liliane Assaf

Tratamento do Saldo Inicial para deduzir a quantidade das saídas do dia anterior \(tópico 19\.3\-A\.2\.2 – “a”\)

17/08/2022

__MFS94561__

Liliane Assaf

Devoluções de saídas no mesmo dia da saída não entram na composição o Valor Unitário Médio Ponderado\.

Pendência \(MFS\-97582\): Melhorar a conferência dos valores no relatório da média ponderada\.

01/11/2021

__MFS99147__

Liliane Assaf

Ajuste na regra do Saldo Inicial do Dia que deduz a quantidade de saídas do dia anterior, para tratar o cenário de saídas sem estoque \(Quantidade das Saídas > quantidade saldo final do dia anterior\)\. Correção da regra criada pela MFS92151\.

Para isso foi criado o Parâmetro na tela de Dados Iniciais “Tratamento p/ saídas com quantidades não acobertadas pelo saldo \(Cálculo da Média Ponderada\)”

Se o parâmetro estiver marcado, só deduzir a quantidade de saídas suportada pela quantidade que está no saldo final do dia anterior\.

19/12/2022

Sumário

[1\.	Introdução	1](#_Toc63699477)

[2\.	Recuperação dos Dados e Processamento	1](#_Toc63699478)

[1º Passo – Calcular o Saldo Inicial do Dia	1](#_Toc63699479)

[2º Passo – Calcular o Total das Devoluções de Saídas do Dia	1](#_Toc63699480)

[3º Passo: Calcular o Total das Entradas do Dia	1](#_Toc63699481)

[4º Passo: Calcular o Total das Devoluções de Entradas do Dia	1](#_Toc63699482)

[5º Passo: Calcular o Saldo Final do Dia e Gravar a tabela EST\_ST\_RS\_MEDIA\_POND	1](#_Toc63699483)

[3\.	Relatório de Conferência	1](#_Toc63699484)

[4\.	Tratamento para Produtos não Movimentados:	1](#_Toc63699485)

#  

# <a id="_Toc63699477"></a>Introdução

O Cálculo da Média Pondera Móvel dos Valores Unitários do ICMS, ICMS\-ST, Base de Cálculo do ICMS\-ST e FECEP\-ST, tem como base na __IN\-RE 087/20__ tópicos __19\.3\-A\.2\.2__, __19\.3\-A\.2\.2\.2 e 19\.3\-A\.2\.2\.3 __e é executado por __DIA__, para todos os produtos sujeitos ao ICMS\-ST vigentes no período da geração\.

O cálculo é feito com quatro valores conforme estabelece o tópico 19\.3\-A\.2\.2:

\(alínea “a”\) no saldo inicial do primeiro dia do período, que corresponde ao saldo final do dia anterior;

\(alínea “b”\): movimento de devolução de saídas do período;

\(alínea “c”\): movimento de entradas do período;

\(alínea “d”\): movimento de devolução de entradas do período;

Os valores das alíneas “b”, “c” e “d” foram calculados em etapas anteriores\.

O resultado do cálculo é armazenado numa tabela para uso na Geração dos Movimentos de Saídas e em gerações de períodos posteriores: EST\_ST\_RS\_MEDIA\_POND\.

__Pré\-requisito__:

É necessário que todos os produtos sujeitos a ICMS\-ST possuam um registro de inventário \(SAFX52\) com IND\_MOT\_INV = 06 no dia imediatamente anterior ao período de geração\.

__MFS72212: Criação do Cálculo dos Valores Unitários Médios do Inventário:__

Para o primeiro período da geração de um Produto sujeito a ICMS\-ST, os Valores Unitários do ICMS, ICMS\-ST, Base de Cálculo do ICMS\-ST e FECEP\-ST devem estar carregados na SAFX52 para o dia imediatamente anterior ao mês da geração\. 

Antes da __MFS72212__, para o __primeiro período__ da geração era necessário que os valores médios unitários fossem carregados na SAFX52 \(campos 21\-VLR\_ICMS\_MEDIO, 22\-VLR\_ICMSS\_MEDIO, 43\-VLR\_BASE\_ICMSS\_MEDIO e 44\-VLR\_FCP\_MEDIO\) no último dia do mês anterior ao período da geração, com IND\_MOT\_INV = 06\. A partir da __MFS72212__, a geração do movimento passou a calcular os valores médios unitários do inventário com base nas últimas notas de entradas do produto\.  Sendo assim, o preenchimento dos valores unitários na SAFX52 para o primeiro período de geração tornou\-se opcional\. Caso valores unitários venham carregados na SAFX52 estes serão utilizados para o cálculo da Média Ponderada, caso contrário a rotina irá calculá\-los\.

O saldo inicial do primeiro dia do mês da geração será calculado com base nesses valores\. Os demais dias, o saldo inicial será o saldo final do dia anterior\. 

A partir do segundo período de geração, os Valores Unitários do ICMS, ICMS\-ST, Base de Cálculo do ICMS\-ST e FECEP\-ST não precisam mais ser carregados na SAFX52 para o último dia do mês anterior, pois tais valores já estarão calculados pela geração do mês anterior\. 

Além disso a rotina atualizará os campos 21\-VLR\_ICMS\_MEDIO, 22\-VLR\_ICMSS\_MEDIO, 43\-VLR\_BASE\_ICMSS\_MEDIO e 44\-VLR\_FCP\_MEDIO da Tabela do Inventário \(X52\_INVENT\_PRODUTO\) do último dia do mês anterior, com os valores unitários médios calculados\. Para isso o cliente deve carregar um registro na SAFX52 do último dia do mês anterior, com IND\_MOT\_INV = 06, sem os valores unitários médios\.

O Sped Fiscal exige que exista um registro H030 com MOTIVO INVENTÁRIO = “06” no arquivo que apresentar pelo menos um registro C180, C181, C185, C186, C330, C380, C430, C480, C815\.  Por esse motivo é necessário que todo mês exista um registro na SAFX52 dos produtos sujeitos ao ICMS\-ST com IND\_MOT\_INV = 06, do último dia do mês anterior\. Sendo que, no primeiro mês os valores unitários médios devem ser carregados, e nos demais meses não\.

__Sobre Produtos Associados__:

Para identificar os produtos sujeitos a ICMS\-ST utilizamos as opções de parametrização do menu Parâmetros à Produtos:* “Por Código*”, ou “Por NCM” ou *“CEST”*\.  A parametrização Por Código aceita trabalharmos com o conceito de Produtos Associados\. Parametriza\-se um produto “principal” e *N* produtos associados\. O produto “principal” é gravado na tabela \(__ESP\_SP\_PROD\_ST__\), e os associados ao produto principal na tabela __ESP\_SP\_PROD\_ST\_ASS__\.  Os produtos associados servem para recuperação dos movimentos de entradas, saídas e devoluções \(x07/x08/x993/x994\)\.  Mas todo o controle de inventário \(x52\) é em nome do Produto Principal\.  __O Cálculo da Média Ponderada Móvel é gravado em nome do Produto Principal__\.

__Sobre a Tabela EST\_ST\_RS\_MEDIA\_POND:__

Para um estabelecimento e mês informados na tela geração, a tabela EST\_ST\_RS\_MEDIA\_POND deve ser gravada com um registro para cada dia do mês e produto sujeito a ICMS\-ST\.  

Caso exista apenas parametrização do Produto, mas não exista inventário do Produto \(x52\), nem movimentação do período \(x07, x08\) o produto não deve ser gravado na tabela EST\_ST\_RS\_MEDIA\_POND\.

Por exemplo:

Geração do Estabelecimento 001, de janeiro do 2021\.

Os produtos sujeitos ao ICMS\-ST, parametrizados numa das opções do menu Parâmetros à Produtos, são: PROD01, PROD02\.

Ao final da geração a tabela EST\_ST\_RS\_MEDIA\_POND conterá 31 registros pra cada produto, um para cada dia do mês:

ESTAB	PRODUTO	DIA		VALORES CALCULADOS

001		PROD01	01/01/2021	\.\.\.\.

001		PROD01	02/01/2021	\.\.\.\.

001		PROD01	03/01/2021	\.\.\.\.

\.\.\.

001		PROD01	31/01/2021	\.\.\.\.

001		PROD02	01/01/2021	\.\.\.\.

001		PROD02	02/01/2021	\.\.\.\.

001		PROD02	03/01/2021	\.\.\.\.

\.\.\.

001		PROD02	31/01/2021	\.\.\.\.

__Texto da IN\-RE 087/20, Tópico 19\.3\-A\.2\.2 que define Cálculo da Média Pondera Móvel dos Valores Unitários:__

__“19\.3\-A\.2\.2__ \- Para definir, em relação a cada mercadoria, o valor médio ponderado móvel do dia, definido no subitem 19\.3\-

A\.2\.1, ao fim de cada dia, o contribuinte deverá seguir as etapas que seguem:

a\) identificar o saldo total do estoque inicial do dia de cada mercadoria, por meio da multiplicação da quantidade total

existente em estoque no fim do dia anterior pelo valor médio ponderado móvel apurado no fim do dia anterior;

b\) acrescentar ao valor apurado na alínea "a" as informações referentes a todas as devoluções de saídas da mercadoria e

retornos de mercadorias não entregues, de que trata a alínea "c" do subitem 19\.3\-A\.1, ocorridos durante o dia, que corresponderá à soma

das multiplicações da quantidade de mercadorias de cada devolução e retorno pelo valor unitário médio móvel calculado ao fim do dia em que

ocorreu a saída objeto de devolução ou retorno;

c\) acrescentar ao valor apurado na alínea "b" as informações referentes a todas as entradas de mercadorias, de que trata

a alínea "b" do subitem 19\.3\-A\.1, ocorridas durante o dia, que corresponderá à soma das multiplicações da quantidade de cada entrada pelo

valor unitário que serviu de base de cálculo do imposto retido por substituição tributária;

d\) subtrair do valor apurado na alínea "c" as informações referentes a todas as devoluções de entradas de que trata a

alínea "d" do subitem 19\.3\-A\.1, que corresponderá à soma das multiplicações da quantidade de cada saída em devolução pelo valor unitário

que serviu de base de cálculo do imposto retido por substituição tributária para a mercadoria objeto de devolução;

e\) quantificar o total da mercadoria no fim do dia, desconsideradas as saídas de que trata a alínea "a" do subitem 19\.3\-A\.1

registradas durante o dia, que corresponderá à soma da quantidade existente em estoque no fim do dia anterior com a quantidade das

saídas devolvidas ou retornadas durante o dia, bem como da quantidade que entrou no dia, subtraída da quantidade que saiu em devolução

no dia;

f\) obter o resultado, que corresponderá à divisão do total dos valores apurados conforme alíneas "a" a "d" pela

quantidade apurada na alínea "e"\.”

# <a id="_Toc350763252"></a><a id="_Toc59988568"></a><a id="_Toc63699478"></a>Recuperação dos Dados e Processamento 

__Visão resumida do Processamento__

O Cálculo deve ser executado dia por dia, em __ordem cronológica__\.

Para cada __dia__ do mês da geração, executar:

  1º: Geração os Movimentos de Devolução das Saídas do dia;

  2º: Cálculo da Média Ponderada Móvel dos Valores Unitários do dia\.

__Geração os Movimentos de Devolução das Saídas do dia:__

Veja documento *“MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Devolução de Saidas\.docx”\.*

__Cálculo da Média Ponderada Móvel dos Valores Unitários do dia__:

1º Passo: Calcular o Saldo Inicial do dia 

2º Passo: Calcular o Total das Devoluções de Saídas do dia

3º Passo: Calcular o Total das Entradas do dia

4º Passo: Calcular o Total das Devoluções de Entradas do dia

5º Passo: Calcular o Saldo Final do dia e gravando a tabela EST\_ST\_RS\_MEDIA\_POND\.

## <a id="_1º_Passo_–"></a><a id="_Toc63699479"></a>1º Passo – Calcular o Saldo Inicial do Dia

Segundo a IN087/20, para calcular o saldo inicial do dia recupera\-se o saldo final do dia anterior\. Para isso, vamos adotar dois procedimentos, um aplicado ao primeiro dia do mês da geração, e outro para os demais dias do mês:

- __Segundo Dia do mês da geração em diante:__

Para o __segundo ao último dia__ do mês da geração, recuperar o saldo final do dia anterior da tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\)\. 

__Recuperação do Saldo Final do Dia Anterior da Tabela do Cálculo da Média Ponderada \(EST\_ST\_RS\_MEDIA\_POND\) __

__Origem dos dados__: \- Parametrização de Produtos \(por Código, por NCM e por CEST\);

                                  \- Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\)\.

__Critérios:__

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data __*imediatamente anterior*__ ao DIA que está sendo processado;

\- O produto deve constar na parametrização do menu “*Parâmetros à Produtos à Por Código*”, __ou__, seu NCM deve estar parametrizado no menu “*Parâmetros à Produtos à Por NCM*”, __ou__, seu CEST deve estar parametrizado no menu “*Parâmetros à Produtos à Por CEST*”\. 

 Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração\.

No caso da parametrização dos produtos, primeiro é verificado se o produto consta na parametrização da opção “Por Código”\. Ao verificar a parametrização por código, basta considerar o produto “principal”\. Pois conforme já explicado, o cálculo é gravado em nome do produto “principal” \(__ESP\_SP\_PROD\_ST__\)\. 

A prioridade na pesquisa da parametrização dos produtos é: por Código, por NCM, e por último, por CEST, da seguinte forma:

 

        \-Caso o produto conste na parametrização por código, a parametrização por NCM não precisa ser verificada\.

        \-Caso não, é verificado se o NCM do produto \(NCM do cadastro do produto\) consta na parametrização da opção “Por NCM”\.

        \-Caso o produto conste na parametrização por NCM, a parametrização por CEST não precisa ser verificada\.

        \-Caso não, é verificado se o CEST do produto \(CEST do cadastro do produto\) consta na parametrização da opção “Por CEST”\.

Recuperar as seguintes informações:

- Qtde total Convetida Final \(QTD\_CONV\_FIM\)
- Valor do ICMS Calculado Final \(VLR\_ICMS\_FIM\_MP\)
- Valor do ICMS\-ST Calculado Final \(VLR\_ICMS\_ST\_FIM\_MP\)
- Valor Base de Cálculo do ICMS\-ST Calculado Final \(VLR\_BC\_ST\_FIM\_MP\)
- Valor FECEP\-ST Calculado Final \(VLR\_FECEP\_ST\_FIM\_MP\)
- Qtde Saídas a deduzir p/ próximo dia c/ movimento \(QTD\_CONV\_SAF\_MP\)

      Os campos que compõe o __Saldo Inicial__ do Dia serão preenchidos com os valores do Saldo Final do dia anterior:

- Qtde Total Convertida Inicial \(QTD\_CONV\_INI\) = Qtde total Convetida Final \(QTD\_CONV\_FIM\)
- Valor do ICMS Calculado Inicial \(VLR\_ICMS\_INI\_MP\) = Valor do ICMS Calculado Final \(VLR\_ICMS\_FIM\_MP\)
- Valor do ICMS\-ST Calculado Inicial \(VLR\_ICMS\_ST\_INI\_MP\) = Valor do ICMS\-ST Calculado Final \(VLR\_ICMS\_ST\_FIM\_MP\)
- Valor Base de Cálculo do ICMS\-ST Calculado Inicial \(VLR\_BC\_ST\_INI\_MP\) = Valor Base de Cálculo do ICMS\-ST Calculado Final \(VLR\_BC\_ST\_FIM\_MP\)
- Valor FECEP\-ST Calculado Inicial \(VLR\_FECEP\_ST\_INI\_MP\) = Valor FECEP\-ST Calculado Final \(VLR\_FECEP\_ST\_FIM\_MP\)

O Saldo Inicial do segundo dia em diante depende a Quantidade Final do dia imediatamente anterior\.

__1 \- Para Quantidade Final \(QTD\_CONV\_FIM\) do dia imediatamente anterior IGUAL a Zero__:

__1\.1__ \- Se o dia corrente possui pelo menos uma Movimentação de Entrada, ou Devolução de Entrada ou Devolução de Saída \(QTD\_CONV\_ENT\_MP <>0 ou QTD\_CONV\_DEV\_SAI\_MP <> 0 ou 

QTD\_CONV\_DEV\_ENT\_MP <>0\), então:

__MFS92151: Subtrair a Quantidade das Saídas do Dia anterior do Saldo Final, para compor o Saldo Inicial \(19\.3\-A\.2\.2 – “a”\)__

__MFS99147:Só deduzir a quantidade de saídas suportada pela quantidade que está no saldo final do dia anterior \(continuação da MFS92151\):__

__            	      Quando Parâmetro “Tratamento p/ saídas com quantidades não acobertadas pelo saldo \(Cálculo da Média Ponderada\)” = ‘N’:__

Compor a Quantidade Inicial com a Quantidade Final menos quantidade de saídas do dia anterior\.

- 
	- 
		- 
			- Qtde Total Convertida Inicial \(QTD\_CONV\_INI\) = Qtde total Convetida Final \(QTD\_CONV\_FIM\) \- 

                                                              		   Qtde Saídas a deduzir p/ próximo dia c/ movimento \(QTD\_CONV\_SAI\_MP\)

Se Quantidade Inicial calculada ficar negativa, exibir a seguinte mensagem de aviso no log da geração:

*Cálculo da Média Ponderada Móvel: Valor do Saldo Inicial calculado a partir da movimentacao de saidas, resultou em negativo\. Veja os campos <Qtde \(Saida do Dia\)> e <Qtde Final> do dia anterior no Relatorio de Calculo de Media Ponderada\. *Dados de Identificação: Empresa: xxx \- Estab: xx – Período: 99/99/9999 \- Produto\(ind/cód\) x\-xxx – Dia DD/MM/AAAA

Zera a quantidade de saídas anteriores pois foram utilizadas \(Qtde Saída a deduzir p/ próximo dia c/ movimento \(QTD\_CONV\_SAI\_MP\)\)\.

__                  Quando Parâmetro “Tratamento p/ saídas com quantidades não acobertadas pelo saldo \(Cálculo da Média Ponderada\)” = ‘S’:__

Compor a Quantidade Inicial com a Quantidade Final do dia anterior\.

- 
	- 
		- 
			- Qtde Total Convertida Inicial \(QTD\_CONV\_INI\) = Qtde total Convetida Final \(QTD\_CONV\_FIM\) 

Qtde Saída a deduzir p/ próximo dia c/ movimento \(QTD\_CONV\_SAI\_MP\) mantém pois não foram utilizadas\.

__\[MFS89648\] \(19\.3\-A\.2\.2\.3 da IN\-045/98\) \- Tratamento para Quantidade Final do dia anterior zero:__

	Verificar se a Quantidade Final foi zerada por conta de ocorrência de devolução de entrada em dias anteriores\. Cenário tratado conforme tópico 19\.3\-A\.2\.2\.3\.

Para isso realizar uma busca na tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\) com aos critérios:

\- Estabelecimento, empresa e produto em questão;

\- Data igual ao dia__* imediatamente anterior*__ ao DIA que está sendo processado;

\- Indicador de Utilização do Saldo \(19\.3\-A\.2\.2\.3 IN45/98\) \(IND\_UTIL\_DEV\_ZERA\) seja __‘N’__

Se existir registro \(significa que em dias anteriores a quantidade final do dia foi zerada por conta de movimentos de devolução de entrada\):

Cenário tratado conforme tópico 19\.3\-A\.2\.2\.3\.

Os campos que compõe o Saldo Inicial do Dia serão preenchidos com os campos do “[Saldo Inicial p/ próximo dia c /movimento \(caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 \- 19\.3\-A\.2\.2\.3\)](#Saldo_inicial)”\. 

- 
	- 
		- 
			- Valor do ICMS Calculado Inicial \(VLR\_ICMS\_INI\_MP\) = Valor do ICMS \(19\.3\-A\.2\.2\.3 IN45/98\) \(VLR\_ICMS\_DEV\_ZERA\)
			- Valor do ICMS\-ST Calculado Inicial \(VLR\_ICMS\_ST\_INI\_MP\) = Valor do ICMS\-ST \(19\.3\-A\.2\.2\.3 IN45/98\) \(VLR\_ICMS\_ST\_DEV\_ZERA\)
			- Valor Base de Cálculo do ICMS\-ST Calculado Inicial \(VLR\_BC\_ST\_INI\_MP\) = Valor Base de Cálculo do ICMS\-ST \(19\.3\-A\.2\.2\.3 IN45/98\) \(VLR\_BC\_ST\_DEV\_ZERA\)
			- Valor FECEP\-ST Calculado Inicial \(VLR\_FECEP\_ST\_INI\_MP\) = Valor FECEP\-ST \(19\.3\-A\.2\.2\.3 IN45/98\) \(VLR\_FECEP\_ST\_DEV\_ZERA\)

Atualizar Indicador de Utilização do Saldo \(19\.3\-A\.2\.2\.3 IN45/98\) \(IND\_UTIL\_DEV\_ZERA\) para “S”, do registro da ocorrência de devolução da entrada que zerou a quantidade final\.

Senão:

Mantém a regra atual Saldo Inicial = Saldo Final do dia anterior \(que no caso é zero\)\. 

__Cravar zero__\! 

- 
	- 
		- 
			- Valor do ICMS Calculado Inicial \(VLR\_ICMS\_INI\_MP\) = 0
			- Valor do ICMS\-ST Calculado Inicial \(VLR\_ICMS\_ST\_INI\_MP\) = 0
			- Valor Base de Cálculo do ICMS\-ST Calculado Inicial \(VLR\_BC\_ST\_INI\_MP\) = 0
			- Valor FECEP\-ST Calculado Inicial \(VLR\_FECEP\_ST\_INI\_MP\) = 0

Os valores do “[Saldo Inicial p/ próximo dia c /movimento \(caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 \- 19\.3\-A\.2\.2\.3\)](#Saldo_inicial)” do dia anterior se mantém inalterados\.

__1\.2__ \- Se o dia corrente não possui Movimentações de Entradas, Devoluções de Entradas e Devoluções de Saídas \(QTD\_CONV\_ENT\_MP = 0 e QTD\_CONV\_DEV\_SAI\_MP = 0 e QTD\_CONV\_DEV\_ENT\_MP =0\):

Mantém a regra atual Saldo Inicial = Saldo Final do dia anterior \(que no caso é zero\)\. 

__Cravar zero__\! 

- Qtde Total Convertida Inicial \(QTD\_CONV\_INI\) = 0
- Valor do ICMS Calculado Inicial \(VLR\_ICMS\_INI\_MP\) = 0
- Valor do ICMS\-ST Calculado Inicial \(VLR\_ICMS\_ST\_INI\_MP\) = 0
- Valor Base de Cálculo do ICMS\-ST Calculado Inicial \(VLR\_BC\_ST\_INI\_MP\) = 0
- Valor FECEP\-ST Calculado Inicial \(VLR\_FECEP\_ST\_INI\_MP\) = 0

__2 \- Para Quantidade Final \(QTD\_CONV\_FIM\) do dia imediatamente anterior Diferente de Zero, proceder:__

__MFS92151: Subtrair a Quantidade das Saídas do Dia anterior do Saldo Final, para compor o Saldo Inicial \(19\.3\-A\.2\.2 – “a”\) __

__MFS99147:Só deduzir a quantidade de saídas suportada pela quantidade que está no saldo final do dia anterior \(continuação da MFS92151\):__

__2\.1__ \- Se o dia corrente possui pelo menos uma Movimentação de Entrada, Devolução de Entrada ou Devolução de Saída \(QTD\_CONV\_ENT\_MP <>0 ou QTD\_CONV\_DEV\_SAI\_MP <> 0 ou QTD\_CONV\_DEV\_ENT\_MP <>0\):

	Compor a Quantidade Inicial com a Quantidade Final menos quantidade de saídas do dia anterior\. 

__            Quando Parâmetro “Tratamento p/ saídas com quantidades não acobertadas pelo saldo \(Cálculo da Média Ponderada\)” = ‘N’:__

- 
	- 
		- Qtde Total Convertida Inicial \(QTD\_CONV\_INI\) = Qtde total Convetida Final \(QTD\_CONV\_FIM\) \- 

   Qtde Saídas a deduzir p/ próximo dia c/ movimento \(QTD\_CONV\_SAI\_MP\)

Se Quantidade Inicial calculada ficar negativa, exibir a seguinte mensagem de aviso no log da geração:

*Cálculo da Média Ponderada Móvel: Valor do Saldo Inicial calculado a partir da movimentacao de saidas, resultou em negativo\. Veja os campos <Qtde \(Saida do Dia\)> e <Qtde Final> do dia anterior no Relatorio de Calculo de Media Ponderada\. *Dados de Identificação: Empresa: xxx \- Estab: xx – Período: 99/99/9999 \- Produto\(ind/cód\) x\-xxx – Dia DD/MM/AAAA

Zera a quantidade de saídas anteriores pois foram utilizadas \(Qtde Saída a deduzir p/ próximo dia c/ movimento \(QTD\_CONV\_SAI\_MP\)\)\.

__            		Quando Parâmetro “Tratamento p/ saídas com quantidades não acobertadas pelo saldo \(Cálculo da Média Ponderada\)” = ‘S’:__

- 
	- 
		- Se Qtde total Convetida Final \(QTD\_CONV\_FIM\) >= Qtde Saídas a deduzir p/ próximo dia c/ movimento \(QTD\_CONV\_SAI\_MP\) Então:

     Qtde Total Convertida Inicial \(QTD\_CONV\_INI\) = Qtde total Convetida Final \(QTD\_CONV\_FIM\) \- 

                                                                                     Qtde Saídas a deduzir p/ próximo dia c/ movimento \(QTD\_CONV\_SAI\_MP\)

     Qtde Saída a deduzir p/ próximo dia c/ movimento \(QTD\_CONV\_SAI\_MP\) = 0  à Zera a quantidade de saídas anteriores pois foi utilizada por completo\.

Se Qtde total Convetida Final \(QTD\_CONV\_FIM\) < Qtde Saídas a deduzir p/ próximo dia c/ movimento \(QTD\_CONV\_SAI\_MP\) Então:

     Qtde Total Convertida Inicial \(QTD\_CONV\_INI\) = 0 

     Qtde Saídas a deduzir p/ próximo dia c/ movimento \(QTD\_CONV\_SAI\_MP\) = Qtde Saídas a deduzir p/ próximo dia c/ movimento \(QTD\_CONV\_SAI\_MP\) \- 

                                                                                                                                  Qtde total Convetida Final \(QTD\_CONV\_FIM\)

- 
	- 
		- Valor do ICMS Calculado Inicial \(VLR\_ICMS\_INI\_MP\) = QTD\_CONV\_INI \* Valor Médio Unitário do ICMS \(VLR\_UNIT\_ICMS\_FIM\_MP\)
		- Valor do ICMS\-ST Calculado Inicial \(VLR\_ICMS\_ST\_INI\_MP\) = QTD\_CONV\_INI \* Valor Médio Unitário do ICMS\-ST s/ FECEP \(VLR\_UNIT\_ICMS\_ST\_FIM\_MP\)
		- Valor Base de Cálculo do ICMS\-ST Calculado Inicial \(VLR\_BC\_ST\_INI\_MP\) = QTD\_CONV\_INI \* Valor Médio Unitário da Base de Cálculo do ICMS\-ST \(VLR\_UNIT\_BC\_ST\_FIM\_MP
		- Valor FECEP\-ST Calculado Inicial \(VLR\_FECEP\_ST\_INI\_MP\) = QTD\_CONV\_INI \* Valor Médio Unitário do FECEP\-ST \(VLR\_UNIT\_FECEP\_ST\_FIM\_MP 

__2\.2__ \- Se o dia corrente não possui Movimentações de Entradas, Devoluções de Entradas e Devoluções de Saídas \(QTD\_CONV\_ENT\_MP = 0 e QTD\_CONV\_DEV\_SAI\_MP = 0 e QTD\_CONV\_DEV\_ENT\_MP =0\):	Mantém a regra para Saldo Inicial = Saldo Final do dia anterior

- 
	- 
		- Qtde Total Convertida Inicial \(QTD\_CONV\_INI\) = Qtde total Convetida Final \(QTD\_CONV\_FIM\)

__MFS94561: Devoluções de saídas no mesmo dia da saída não entram na composição o Valor Médio Ponderado__

- 
	- 
		- Valor do ICMS Calculado Inicial \(VLR\_ICMS\_INI\_MP\) = QTD\_CONV\_INI \* Valor Médio Unitário do ICMS \(VLR\_UNIT\_ICMS\_FIM\_MP\)
		- Valor do ICMS\-ST Calculado Inicial \(VLR\_ICMS\_ST\_INI\_MP\) = QTD\_CONV\_INI \* Valor Médio Unitário do ICMS\-ST s/ FECEP \(VLR\_UNIT\_ICMS\_ST\_FIM\_MP\)
		- Valor Base de Cálculo do ICMS\-ST Calculado Inicial \(VLR\_BC\_ST\_INI\_MP\) = QTD\_CONV\_INI \* Valor Médio Unitário da Base de Cálculo do ICMS\-ST \(VLR\_UNIT\_BC\_ST\_FIM\_MP
		- Valor FECEP\-ST Calculado Inicial \(VLR\_FECEP\_ST\_INI\_MP\) = QTD\_CONV\_INI \* Valor Médio Unitário do FECEP\-ST \(VLR\_UNIT\_FECEP\_ST\_FIM\_MP

	Mantém a quantidade de saídas anteriores pois não forem utilizadas \(Qtde Saída a deduzir p/ próximo dia c/ movimento \(QTD\_CONV\_SAI\_MP\)\)

	

-  __Primeiro Dia do mês da geração:__

Para o __Primeiro Dia__ do mês da geração, calcular o saldo inicial do dia considerando:

- Quantidade Tabela do Inventário \(X52\_INVENT\_PRODUTO\) do último dia do mês anterior;
- Os Valores Unitários Médios da Tabela do Inventário ou da tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\) do último dia do mês anterior;

__\[MFS69798\]__

A quantidade sempre deverá ser recuperada da Tabela do Inventário\. Já os valores Unitários Médios, depende se a geração do mês anterior foi realizada ou não\.  Ou seja:

Se o produto sujeito a ICMS\-ST possui registro para o último dia do mês anterior na tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” 

\(EST\_ST\_RS\_MEDIA\_POND\), então:

 	Considerar os Valores Unitários Médios do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\)\.

Senão:

Considerar os Valores Unitários Médios do Inventário \(X52\_INVENT\_PRODUTO\) do último dia do mês anterior\. 

__      __Calculando o __Saldo Inicial__ do dia:

- Qtde Total Convertida Inicial \(QTD\_CONV\_INI\) = Quantidade do Inventário Convertida \(X52\_INVENT\_PRODUTO\)
- Valor do ICMS Calculado Inicial \(VLR\_ICMS\_INI\_MP\): 

Se produto possui média calculada para o último dia do mês anterior, então:

\[Quantidade do Inventário Convertida \* Valor Médio Unitário do ICMS \(VLR\_UNIT\_ICMS\_FIM\_MP \- EST\_ST\_RS\_MEDIA\_POND\)\]

Senão

\[Quantidade do Inventário Convertida \* Valor de ICMS Médio \(VLR\_ICMS\_MEDIO \- X52\_INVENT\_PRODUTO\)\]\.

- Valor do ICMS\-ST Calculado Inicial \(VLR\_ICMS\_ST\_INI\_MP\):

Se produto possui média calculada para o último dia do mês anterior, então:

\[Quantidade do Inventário Convertida \* Valor Médio Unitário do ICMS\-ST s/ FECEP \(VLR\_UNIT\_ICMS\_ST\_FIM\_MP – 

EST\_ST\_RS\_MEDIA\_POND\)\]

Senão

\[Quantidade do Inventário Convertida \* \(Valor de ICMS\-ST Médio \(VLR\_ICMSS\_MEDIO\) \- Valor FECEP Médio \(VLR\_FCP\_MEDIO\)\)\]   

Onde VLR\_ICMSS\_MEDIO e VLR\_FCP\_MEDIO são campos oriundos da X52\_INVENT\_PRODUTO\.

__\[MFS84145\] __Alteração no cálculo do campo Valor de ICMS\-ST Médio, para abater o valor do FECEP Médio quando a origem for da SAFX52\.

Quando o resultado do cálculo do Valor do ICMS\-ST médio \- Valor FECEP Médio, resultar em um valor negativo, será gravada a seguinte mensagem de erro no log:  
 *“Cálculo da Média Ponderada Móvel: Valor do ICMS\-ST Calculado Inicial gerado a partir da subtração dos campos <Valor ICMS\-ST Médio> pelo <Valor Fecep Médio> do Inventário, resultou em valor negativo\.  Favor rever o Inventário do Produto \(SAFX52\) de forma a adicionar o Fecep ao valor do ICMS\-ST carregado no campo <Valor ICMS\-ST Médio>\.”*

Dados de Identificação: Empresa: xxx \- Estab: xx – Período: 99/99/9999 \- Produto\(ind/cód\) x\-xxx

- Valor Base de Cálculo do ICMS\-ST Calculado Inicial \(VLR\_BC\_ST\_INI\_MP\): 

Se produto possui média calculada para o último dia do mês anterior, então:

\[Quantidade do Inventário Convertida \* Valor Médio Unitário da Base de Cálculo do ICMS\-ST \(VLR\_UNIT\_BC\_ST\_FIM\_MP – 

EST\_ST\_RS\_MEDIA\_POND\)\]

Senão

\[Quantidade do Inventário Convertida \* Valor Base ICMS\-ST Médio \(VLR\_BASE\_ICMSS\_MEDIO \- X52\_INVENT\_PRODUTO\)\]\.

- Valor FECEP\-ST Calculado Inicial \(VLR\_FECEP\_ST\_INI\_MP\): 

Se produto possui média calculada para o último dia do mês anterior, então:

\[Quantidade do Inventário Convertida \* Valor Médio Unitário do FECEP\-ST \(VLR\_UNIT\_FECEP\_ST\_FIM\_MP \- EST\_ST\_RS\_MEDIA\_POND\)\]

Senão

\[Quantidade do Inventário Convertida \* Valor FECEP Médio \(VLR\_FCP\_MEDIO \- X52\_INVENT\_PRODUTO\)\]\.

__\[MFS89648\] \(19\.3\-A\.2\.2\.2 da IN\-045/98\) \- Tratamento para Valor Médio Ponderado Negativo:__

Verificar se Valor Médio Unitário da Base de Cálculo do ICMS\-ST do último dia do mês anterior é negativo\. Para isso considerar o VLR\_UNIT\_BC\_ST\_FIM\_MP da EST\_ST\_RS\_MEDIA\_POND, caso o produto possua média calculada para o último dia do mês anterior\. Caso contrário, considerar o VLR\_BASE\_ICMSS\_MEDIO da X52\_INVENT\_PRODUTO\.

Caso o “Valor Médio Unitário da Base de Cálculo do ICMS\-ST” recuperado do último dia do mês anterior for negativo, então:

    	O Saldo Inicial do primeiro dia do mês será zero\. 

- Qtde Total Convertida Inicial \(QTD\_CONV\_INI\) = Quantidade do Inventário Convertida \(X52\_INVENT\_PRODUTO\)
- Valor do ICMS Calculado Inicial \(VLR\_ICMS\_INI\_MP\) = 0
- Valor do ICMS\-ST Calculado Inicial \(VLR\_ICMS\_ST\_INI\_MP\) = 0
- Valor Base de Cálculo do ICMS\-ST Calculado Inicial \(VLR\_BC\_ST\_INI\_MP\) = 0
- Valor FECEP\-ST Calculado Inicial \(VLR\_FECEP\_ST\_INI\_MP\) = 0

            __\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

__Obs\.: Todos os valores calculados devem ser arredondados, não devem ser truncados\.__

            __\[MFS90131\] __Arredondar para 8 casas decimais o resultado dos cáculos \(qtde x valores unitários\)

__Recuperação dos Valores Unitários Médios da Tabela do Cálculo da Média Ponderada \(EST\_ST\_RS\_MEDIA\_POND\) __

__Origem dos dados__: \- Parametrização de Produtos \(por Código, por NCM e por CEST\);

                                  \- Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\)\.

__Critérios:__

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data igual ao último dia do mês anterior que está sendo processado;

\- O produto deve constar na parametrização do menu “*Parâmetros à Produtos à Por Código*”, __ou__, seu NCM deve estar parametrizado no menu “*Parâmetros à Produtos à Por NCM*”, __ou__, seu CEST deve estar parametrizado no menu “*Parâmetros à Produtos à Por CEST*”\. 

 Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração\.

No caso da parametrização dos produtos, primeiro é verificado se o produto consta na parametrização da opção “Por Código”\. Ao verificar a parametrização por código, basta considerar o produto “principal”\. Pois conforme já explicado, o cálculo é gravado em nome do produto “principal” \(__ESP\_SP\_PROD\_ST__\)\. 

A prioridade na pesquisa da parametrização dos produtos é: por Código, por NCM, e por último, por CEST, da seguinte forma:

 

        \-Caso o produto conste na parametrização por código, a parametrização por NCM não precisa ser verificada\.

        \-Caso não, é verificado se o NCM do produto \(NCM do cadastro do produto\) consta na parametrização da opção “Por NCM”\.

        \-Caso o produto conste na parametrização por NCM, a parametrização por CEST não precisa ser verificada\.

        \-Caso não, é verificado se o CEST do produto \(CEST do cadastro do produto\) consta na parametrização da opção “Por CEST”\.

__\[__[__MFS81749__](https://jira.thomsonreuters.com/browse/MFS-81749)__\]__

__Tratamento para Produtos Farmacêuticos de Distribuidores:__

\- Não recuperar a Média Ponderada de Produtos Farmaceuticos de Estabelecimentos Distribuidores\. Ou seja, se os dois critérios a seguir forem atendidos, não recuperar a Média Ponderada:

- Estabelecimento é um __Distribuidor__ \(atacadista\), ou seja, na Tela de Dados Iniciais estiver com o campo “Contribuinte Varejista?” = Não; 
- __Produto__ estiver cadastrado, na tela de Parametrização de Produtos Farmacêuticos por Código, no menu: Parametros >  \(IN\-RE 087/20\) > Produtos Farmacêuticos > Código

Recuperar as seguintes informações:

- Valor Médio Unitário do ICMS \(VLR\_UNIT\_ICMS\_FIM\_MP\)
- Valor Médio Unitário do ICMS\-ST s/ FECEP \(VLR\_UNIT\_ICMS\_ST\_FIM\_MP\)
- Valor Médio Unitário da Base de Cálculo do ICMS\-ST \(VLR\_UNIT\_BC\_ST\_FIM\_MP\)
- Valor Médio Unitário do FECEP\-ST \(VLR\_UNIT\_FECEP\_ST\_FIM\_MP\)

__Recuperação da Quantidade e Valores Unitários Médios da Tabela de Inventário \(X52\_INVENT\_PRODUTO\) __

__Origem dos dados__: \- Parametrização de Produtos \(por Código, por NCM e por CEST\);

                                  \- Tabela do Inventário \(X52\_INVENT\_PRODUTO\)\.

__Critérios:__

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data do Inventário \(campo 03 \- DATA\_INVENTARIO\) último dia do mês anterior que está sendo processado;

\- Motivo do Inventário \(campo 40 \- IND\_MOT\_INV\) = “06” \- controle das mercadorias sujeitas ao regime de substituição tributária;

\- Grupo Contagem \(campo 04 \- GRUPO\_CONTAGEM\) à 1, 2, 3 e 5;

\- O produto deve constar na parametrização do menu “*Parâmetros à Produtos à Por Código*”, __ou__, seu NCM deve estar parametrizado no menu “*Parâmetros à Produtos à Por NCM*”, __ou__, seu CEST deve estar parametrizado no menu “*Parâmetros à Produtos à Por CEST*”\. 

 Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração\.

No caso da parametrização dos produtos, primeiro é verificado se o produto consta na parametrização da opção “Por Código”\. Ao verificar a parametrização por código, basta considerar o produto “principal”\. Pois conforme já explicado, as informações do inventário estão registradas em nome do produto “principal” \(__ESP\_SP\_PROD\_ST__\)\. 

A prioridade na pesquisa da parametrização dos produtos é: por Código, por NCM, e por último, por CEST, da seguinte forma:

 

        \-Caso o produto conste na parametrização por código, a parametrização por NCM não precisa ser verificada\.

        \-Caso não, é verificado se o NCM do produto \(NCM do cadastro do produto\) consta na parametrização da opção “Por NCM”\.

        \-Caso o produto conste na parametrização por NCM, a parametrização por CEST não precisa ser verificada\.

        \-Caso não, é verificado se o CEST do produto \(CEST do cadastro do produto\) consta na parametrização da opção “Por CEST”\.

__\[__[__MFS81749__](https://jira.thomsonreuters.com/browse/MFS-81749)__\]__

__Tratamento para Produtos Farmacêuticos de Distribuidores:__

<a id="_Hlk75258358"></a>\- Não recuperar o inventário de Produtos Farmaceuticos de Estabelecimentos Distribuidores\. Ou seja, se os dois critérios a seguir forem atendidos, não recuperar o inventário:

- Estabelecimento é um __Distribuidor__ \(atacadista\), ou seja, na Tela de Dados Iniciais estiver com o campo “Contribuinte Varejista?” = Não; 
- __Produto__ do inventário estiver cadastrado, na tela de Parametrização de Produtos Farmacêuticos por Código, no menu: Parametros >  \(IN\-RE 087/20\) > Produtos Farmacêuticos > Código

Os critérios acima podem retornar mais de um registro de inventário para o mesmo produto\. Caso isso ocorra, recuperar registro a registro, individualmente\. Considerar as seguintes informações:

- 12 \- Unidade de Medida \(COD\_MEDIDA\)
- 13 \- Quantidade de Inventário \(QUANTIDADE\)
- 21 \- Valor de ICMS Médio \(VLR\_ICMS\_MEDIO\)
- 22 \- Valor de ICMS\-ST Médio \(VLR\_ICMSS\_MEDIO\)
- 43 \- Valor Base ICMS\-ST Médio \(VLR\_BASE\_ICMSS\_MEDIO\)
- 44 \- Valor FECEP Médio \(VLR\_FCP\_MEDIO\)

Calcular a quantidade convertida:

- Qtde total Convetida Final:

Campo 13\-Quantidade de Inventário, aplicando a conversão, quando necessário\. Veja:

__Se__ unidade do inventário __\(\*\)__ = unidade do cadastro do produto __\(\*\*\) __

      __\(\*\)__ unidade do inventário = campo “12\-Unidade de Medida” da SAFX52

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será a própria quantidade do inventário;

__Senão __

         Nesse caso a quantidade do inventário \(SAFX52\) será convertida para a unidade de medida do cadastro do produto;

         \[ Quantidade de Inventário \(SAFX42\) \* Fator de Conversão \]

__Sobre a conversão de medida:__

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas será gravada a seguinte mensagem de erro no log:

“*Cálculo da Média Ponderada Móvel: Fator de conversão de medida de XXX para XXX não encontrado\. Não foi possível calcular o Saldo inicial do dia “XX” para o produto\.*

\(O primeiro “XXX” é a unidade do inventário, e o segundo “XXX”, a unidade do cadastro do produto\)\.

Dados de Indentificação: Estabelecimento: xx \-  Produto\(ind/cód\) x\-xxx – Grupo Contagem: x – Natureza de Estoque: xx

## <a id="_Toc63699480"></a>2º Passo – Calcular o Total das Devoluções de Saídas do Dia

Nesse passo as devoluções de saídas do dia serão recuperadas a partir da tabela __EST\_ST\_RS\_NF\_DEV\_SAI__\.

__Origem dos dados__: \- Tabela Específica resultante da Geração do Movimento de Devolução das Saídas \(EST\_ST\_RS\_NF\_DEV\_SAI\)\.

                                    Vide *MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Devolução de Saidas\.docx*

__Critérios:__

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data Escrita Fiscal \- DIA que está sendo processado;

Recuperar as seguintes informações:

- Produto da NF de Devolução \(GRUPO\_PROD\_NF\_DEV, IND\_PROD\_NF\_DEV, COD\_PROD\_NF\_DEV\)
- Produto Principal \(GRUPO\_PROD\_PRINC, IND\_PROD\_PRINC, COD\_PROD\_PRINC\)
- Quantidade Devolvida Convertida \(QTD\_CONV\_DEV\_SAI\_MP\)
- Valor do ICMS Calculado para Devolução \(VLR\_ICMS\_DEV\_SAI\_MP\)
- Valor do ICMS\-ST Calculado para Devolução \(VLR\_ICMS\_ST\_DEV\_SAI\_MP\)
- Valor Base de Cálculo do ICMS\-ST Calculado para Devolução \(VLR\_BC\_ST\_DEV\_SAI\_MP\)
- Valor FECEP\-ST Calculado para Devolução \(VLR\_FECEP\_ST\_DEV\_SAI\_MP\)

Somarizar a quatindade e os valores recuperados acima por __Produto__: considerar o __Produto Principal__, caso este esteja preenchido, e o __Produto da NF de Devolução__ caso o Principal não esteja preenchido\.

## <a id="_Toc63699481"></a>3º Passo: Calcular o Total das Entradas do Dia

Nesse passo as entradas do dia serão recuperadas a partir da tabela __EST\_ST\_RS\_NF\_ENT__\.

__Origem dos dados__: \- Tabela Específica resultante da Geração do Movimento de Entradas \(EST\_ST\_RS\_NF\_ENT\)\. 

                                    Vide *MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Entradas\.docx*

__Critérios:__

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data Escrita Fiscal \- DIA que está sendo processado;

Recuperar as seguintes informações:

- Produto da NF \(GRUPO\_PROD\_NF, IND\_PROD\_NF, COD\_PROD\_NF\)
- Produto Principal \(GRUPO\_PROD\_PRINC, IND\_PROD\_PRINC, COD\_PROD\_PRINC\)
- Quantidade Entrada Convertida \(QTD\_CONV\_ENT\_MP\)
- Valor do ICMS Calculado para Entrada \(VLR\_ICMS\_ENT\_MP\)
- Valor do ICMS\-ST Calculado para Entrada \(VLR\_ICMS\_ST\_ENT\_MP\)
- Valor Base de Cálculo do ICMS\-ST Calculado para Entrada \(VLR\_BC\_ST\_ENT\_MP\)
- Valor FECEP\-ST Calculado para Entrada \(VLR\_FECEP\_ST\_ENT\_MP\)

Somarizar a quatindade e os valores recuperados acima por __Produto__: considerar o __Produto Principal__, caso este esteja preenchido, e o __Produto da NF __caso o Principal não esteja preenchido\.

## <a id="_Toc63699482"></a>4º Passo: Calcular o Total das Devoluções de Entradas do Dia

Nesse passo as devoluções de entradas do dia serão recuperadas a partir da tabela __EST\_ST\_RS\_NF\_DEV\_ENT__\.

__Origem dos dados__: \- Tabela Específica resultante da Geração do Movimento de Devolução das Entradas \(EST\_ST\_RS\_NF\_DEV\_ENT\)\.

                                    Vide *MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Devolução de Entradas\.docx*

__Critérios:__

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data Escrita Fiscal \- DIA que está sendo processado;

Recuperar as seguintes informações:

- Produto da NF de Devolução \(GRUPO\_PROD\_NF\_DEV, IND\_PROD\_NF\_DEV, COD\_PROD\_NF\_DEV\)
- Produto Principal \(GRUPO\_PROD\_PRINC, IND\_PROD\_PRINC, COD\_PROD\_PRINC\)
- Quantidade Devolvida Convertida \(QTD\_CONV\_DEV\_ENT\_MP\)
- Valor do ICMS Calculado para Devolução \(VLR\_ICMS\_DEV\_ENT\_MP\)
- Valor do ICMS\-ST Calculado para Devolução \(VLR\_ICMS\_ST\_DEV\_ENT\_MP\)
- Valor Base de Cálculo do ICMS\-ST Calculado para Devolução \(VLR\_BC\_ST\_DEV\_ENT\_MP\)
- Valor FECEP\-ST Calculado para Devolução \(VLR\_FECEP\_ST\_DEV\_ENT\_MP\)

Somarizar a quatindade e os valores recuperados acima por __Produto__: considerar o __Produto Principal__, caso este esteja preenchido, e o __Produto da NF de Devolução__ caso o Principal não esteja preenchido\.

## <a id="_Toc63699483"></a>5º Passo: Calcular o Saldo Final do Dia e Gravar a tabela EST\_ST\_RS\_MEDIA\_POND

Para cada __Produto__ sujeito ao ICMS\-ST\(\*\), gravar um registro na tabela com os valores calculados no __dia__: Saldo Inicial, Total das Devoluções de Saídas, Total das Entradas, Total das Devoluções de Entradas e Saldo Final\.

\(\*\) __Produto__ sujeito ao ICMS\-ST\(\*\) são os produtos cujo CÓDIGO ou NCM ou CEST esteja parametrizado numa mas opções de menu “*Parâmetros à Produtos à Por Código*”, __ou__, “*Parâmetros à Produtos à Por NCM*”, __ou__, “*Parâmetros à Produtos à Por CEST*”, com a data de validade da parametrização  acordo com o período informado na tela da geração\.

Observação: Caso as consultas descritas nos passos \(1, 2, 3, 4\) não retornarem registros para o __Produto__ sujeito ao ICMS\-ST\(\*\), gravar a tabela __EST\_ST\_RS\_MEDIA\_POND__ com os campos relacionados zerados\.  Esse passo é importante, pois o mês pode começar sem inventário e movimento, mas no meio do mês pode iniciar um movimento\. A tabela deve possuir um registro pra cada dia do mês\. \(Veja [tópico 4](#_Tratamento_para_Produtos) – que é executado ao final do processamento do período para o produto\)

__Tabela EST\_ST\_RS\_MEDIA\_POND__

Os campos sinalizados com asterisco compõem a chave da tabela\.

__PK__

__Campo__

__Regra de Preenchimento__

Campos para relatório

\(\*\)

Código do Estabelecimento

COD\_ESTAB

Código do estabelecimento SELECIONADO na tela de geração

Não apresentar

\(\*\)

Código da Empresa 

COD\_EMPRESA

Código da empresa da nota de Entrada \(SAFX07\) 

Cod Empresa

\(\*\)

Código do Estabelecimento

COD\_ESTAB\_ORIG

Código do estabelecimento do inventário/movimento recuperado nos passos anteriores\.

Cod Estab

\(\*\)

Data 

DATA

Dia que está sendo processado\.

Dia

\(\*\)

Produto

Grupo\_Produto, Ind\_Produto,

Cod\_Produto

Produto sujeito ao ICMS\-ST \(\*\)

Ind\-Cod Produto

__Saldo Inicial do Dia__

Qtde total Convetida Inicial

QTD\_CONV\_INI

“Qtde total Convetida Inicial” calculada no 1º Passo;

Qtde Inicial

Valor do ICMS Calculado Inicial

VLR\_ICMS\_INI\_MP

“Valor do ICMS Calculado Inicial” calculado no 1º Passo;

__\[MFS90131\]__ Arredondar para 8 casas decimais o resultado do cáculo \(vide 1º passo\)\.

Valor ICMS Inicial

Valor do ICMS\-ST Calculado Inicial

VLR\_ICMS\_ST\_INI\_MP

“Valor do ICMS\-ST Calculado Inicial” calculado no 1º Passo;

__\[MFS90131\]__ Arredondar para 8 casas decimais o resultado do cáculo \(vide 1º passo\)\.

Valor ICMS\-ST Inicial

Valor Base de Cálculo do ICMS\-ST Calculado Inicial

VLR\_BC\_ST\_INI\_MP

“Valor Base de Cálculo do ICMS\-ST Calculado Inicial” calculado no 1º Passo;

__\[MFS90131\]__ Arredondar para 8 casas decimais o resultado do cáculo \(vide 1º passo\)\.

Valor Base de Cálculo do ICMS\-ST Inicial

Valor FECEP\-ST Calculado Inicial

VLR\_FECEP\_ST\_INI\_MP

“Valor FECEP\-ST Calculado Inicial” calculado no 1º Passo;

__\[MFS90131\]__ Arredondar para 8 casas decimais o resultado do cáculo \(vide 1º passo\)\.

Valor FECEP\-ST Inicial

__Devoluções das Saídas do Dia__

Quantidade Devolvida Convertida

QTD\_CONV\_DEV\_SAI\_MP

“Quantidade Devolvida Convertida” recuperada no 2º Passo;

Qtde \(Devolução Saída\)

Valor do ICMS Calculado para Devolução

VLR\_ICMS\_DEV\_SAI\_MP

“Valor do ICMS Calculado para Devolução” recuperado no 2º Passo;

Valor ICMS \(Devolução Saída\)

Valor do ICMS\-ST Calculado para Devolução

VLR\_ICMS\_ST\_DEV\_SAI\_MP

“Valor do ICMS\-ST Calculado para Devolução” recuperado no 2º Passo;

Valor ICMS\-ST \(Devolução Saída\)

Valor Base de Cálculo do ICMS\-ST Calculado para Devolução

VLR\_BC\_ST\_DEV\_SAI\_MP

“Valor Base de Cálculo do ICMS\-ST Calculado para Devolução” recuperado no 2º Passo;

Valor Base de Cálculo do ICMS\-ST \(Devolução Saída\)

Valor FECEP\-ST Calculado para Devolução

VLR\_FECEP\_ST\_DEV\_SAI\_MP

“Valor FECEP\-ST Calculado para Devolução” recuperado no 2º Passo;

Valor FECEP\-ST \(Devolução Saída\)

__Entradas do Dia__

Quantidade Entrada Convertida

QTD\_CONV\_ENT\_MP

“Quantidade Entrada Convertida” recuperada no 3º Passo;

Qtde \(Entrada\)

Valor do ICMS Calculado para Entrada

VLR\_ICMS\_ENT\_MP

“Valor do ICMS Calculado para Entrada” recuperado no 3º Passo;

Valor ICMS \(Entrada\)

Valor do ICMS\-ST Calculado para Entrada

VLR\_ICMS\_ST\_ENT\_MP

“Valor do ICMS\-ST Calculado para Entrada” recuperado no 3º Passo;

Valor ICMS\-ST \(Entrada\)

Valor Base de Cálculo do ICMS\-ST Calculado para Entrada

VLR\_BC\_ST\_ENT\_MP

“Valor Base de Cálculo do ICMS\-ST Calculado para Entrada” recuperado no 3º Passo;

Valor Base de Cálculo do ICMS\-ST \(Entrada\)

Valor FECEP\-ST Calculado para Entrada

VLR\_FECEP\_ST\_ENT\_MP

“Valor FECEP\-ST Calculado para Entrada” recuperado no 3º Passo;

Valor FECEP\-ST \(Entrada\)

__Devoluções das Entradas do Dia__

Quantidade Devolvida Convertida

QTD\_CONV\_DEV\_ENT\_MP

“Quantidade Devolvida Convertida” recuperada no 4º Passo;

Qtde \(Devolução Entrada\)

Valor do ICMS Calculado para Devolução

VLR\_ICMS\_DEV\_ENT\_MP

“Valor do ICMS Calculado para Devolução” recuperado no 4º Passo;

Valor ICMS \(Devolução Entrada\)

Valor do ICMS\-ST Calculado para Devolução

VLR\_ICMS\_ST\_DEV\_ENT\_MP

“Valor do ICMS\-ST Calculado para Devolução” recuperado no 4º Passo;

Valor ICMS\-ST \(Devolução Entrada\)

Valor Base de Cálculo do ICMS\-ST Calculado para Devolução

VLR\_BC\_ST\_DEV\_ENT\_MP

“Valor Base de Cálculo do ICMS\-ST Calculado para Devolução” recuperado no 4º Passo;

Valor Base de Cálculo do ICMS\-ST \(Devolução Entrada\)

Valor FECEP\-ST Calculado para Devolução

VLR\_FECEP\_ST\_DEV\_ENT\_MP

“Valor FECEP\-ST Calculado para Devolução” recuperado no 4º Passo;

Valor FECEP\-ST \(Devolução Entrada\)

__Saldo Final do Dia__

Qtde total Convetida Final

QTD\_CONV\_FIM

QTD\_CONV\_INI \+ QTD\_CONV\_DEV\_SAI\_MP \+ QTD\_CONV\_ENT\_MP \- QTD\_CONV\_DEV\_ENT\_MP

__\[MFS89648\]__

Se Quantidade Final calculada for negativa, exibir a seguinte mensagem de aviso no log da geração:

*“Cálculo da Média Ponderada Móvel: Quantidade Final calculada negativa\. Favor rever a movimentação de devoluções das entradas, pois a quantidade de saídas superou o saldo inicial \+ entradas do dia\.*

Dados de Identificação: Empresa: xxx \- Estab: xx – Período: 99/99/9999 \- Produto\(ind/cód\) x\-xxx – Dia DD/MM/AAAA

Qtde Final

Valor do ICMS Calculado Final

VLR\_ICMS\_FIM\_MP

VLR\_ICMS\_INI\_MP \+ VLR\_ICMS\_DEV\_SAI\_MP \+ VLR\_ICMS\_ENT\_MP \- VLR\_ICMS\_DEV\_ENT\_MP

Valor ICMS Final

Valor do ICMS\-ST Calculado Final

VLR\_ICMS\_ST\_FIM\_MP

VLR\_ICMS\_ST\_INI\_MP \+ VLR\_ICMS\_ST\_DEV\_SAI\_MP \+ VLR\_ICMS\_ST\_ENT\_MP \- VLR\_ICMS\_ST\_DEV\_ENT\_MP

Valor ICMS\-ST Final

Valor Base de Cálculo do ICMS\-ST Calculado Final

VLR\_BC\_ST\_FIM\_MP

VLR\_BC\_ST\_INI\_MP \+ VLR\_BC\_ST\_DEV\_SAI\_MP \+ VLR\_BC\_ST\_ENT\_MP \- VLR\_BC\_ST\_DEV\_ENT\_MP

Valor Base de Cálculo do ICMS\-ST Final

Valor FECEP\-ST Calculado Final

VLR\_FECEP\_ST\_FIM\_MP

VLR\_FECEP\_ST\_INI\_MP \+ VLR\_FECEP\_ST\_DEV\_SAI\_MP \+ VLR\_FECEP\_ST\_ENT\_MP \- VLR\_FECEP\_ST\_DEV\_ENT\_MP

Valor FECEP\-ST Final

__Valores Médios Unitários Calculados do Dia__

Valor Médio Unitário do ICMS

VLR\_UNIT\_ICMS\_FIM\_MP

Se QTD\_CONV\_FIM\_MP = 0 então

   Preencher com zero\.

Senão: 

   Preencher com VLR\_ICMS\_FIM\_MP / QTD\_CONV\_FIM\_MP \(\*\)

\[MFS90131\] arredondar para 8 casas decimais o resultado do cálculo\.

\(\*\) \[MFS94561\]: Devoluções de saídas no mesmo dia da saída não entram na composição o Valor Médio Ponderado\.

Valor Médio Unitário ICMS

Valor Médio Unitário do ICMS\-ST s/ FECEP __\[MFS66171\]__

VLR\_UNIT\_ICMS\_ST\_FIM\_MP

Se QTD\_CONV\_FIM\_MP = 0 então

   Preencher com zero\.

Senão: 

  Preencher com VLR\_ICMS\_ST\_FIM\_MP / QTD\_CONV\_FIM\_MP \(\*\)

__\[MFS90131\]__ arredondar para 8 casas decimais o resultado do cálculo\.

\(\*\) \[MFS94561\]: Devoluções de saídas no mesmo dia da saída não entram na composição o Valor Médio Ponderado\.

Valor Médio Unitário ICMS\-ST s/ FECEP

Valor Médio Unitário do ICMS\-ST c/ FECEP __\[MFS66171\]__

VLR\_UNIT\_ICMS\_ST\_FECEP\_FIM\_MP

Se QTD\_CONV\_FIM\_MP = 0 então

   Preencher com zero\.

Senão: 

  Preencher com:

  \(VLR\_ICMS\_ST\_FIM\_MP \+ VLR\_FECEP\_ST\_FIM\_MP\) / QTD\_CONV\_FIM\_MP \(\*\)

__\[MFS90131\]__ arredondar para 8 casas decimais o resultado do cálculo\.

\(\*\) \[MFS94561\]: Devoluções de saídas no mesmo dia da saída não entram na composição o Valor Médio Ponderado\.

Valor Médio Unitário ICMS\-ST c/ FECEP

Valor Médio Unitário da Base de Cálculo do ICMS\-ST

VLR\_UNIT\_BC\_ST\_FIM\_MP

Se QTD\_CONV\_FIM\_MP = 0 então

   Preencher com zero\.

Senão: 

  Preencher com VLR\_BC\_ST\_FIM\_MP / QTD\_CONV\_FIM\_MP \(\*\)

__\[MFS90131\]__ arredondar para 8 casas decimais o resultado do cálculo\.

\[MFS89468\] os valores médios calculados podem ser negativos\.

\(\*\) \[MFS94561\]: Devoluções de saídas no mesmo dia da saída não entram na composição o Valor Médio Ponderado\.

Valor Médio Unitário Base de Cálculo do ICMS\-ST

Valor Médio Unitário do FECEP\-ST

VLR\_UNIT\_FECEP\_ST\_FIM\_MP

Se QTD\_CONV\_FIM\_MP = 0 então

   Preencher com zero\.

Senão: 

  Preencher com VLR\_FECEP\_ST\_FIM\_MP / QTD\_CONV\_FIM\_MP \(\*\)

__\[MFS90131\]__ arredondar para 8 casas decimais o resultado do cálculo\.

\(\*\) \[MFS94561\]: Devoluções de saídas no mesmo dia da saída não entram na composição o Valor Médio Ponderado\.

Valor Médio Unitário  FECEP\-ST

__Saídas__

Qtde Saída do dia

QTD\_CONV\_SAI\_DIA

MFS92151:

Quantidade de Saídas do Dia

Para recuperar as notas e cupons de saídas a partir da regra descrita no documento matriz da Geração dos Movimentos de Saída \(MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Saídas\.docx\)\.

A quantidade deve bater com as quantidades das notas e cupons demonstrados nos registros C185, C380, C480\. Lembrando de aplicar a conversão de unidades de medidas caso necessário\.

Qtde \(Saída do dia\)

Qtde Saída a deduzir p/ próximo dia c/ movimento

QTD\_CONV\_SAI\_MP

MFS92151:

Quantidade de saídas que será utilizada para deduzir o estoque do próximo dia em que houver movimentações de entradas e/ou devoluções\.

Preencher com QTD\_CONV\_SAI\_DIA do dia \+ QTD\_CONV\_SAI\_MP do dia anterior que não foi utilizada para compor o Saldo Inicial do dia corrente conforme 1º Passo\.

Qtde \(Saída a deduzir p/ próx dia c/ movimento\)

<a id="Saldo_inicial"></a>__Saldo Inicial p/ próximo dia c/ movimento \(caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 \- 19\.3\-A\.2\.2\.3\)__

Indicador de Utilização do Saldo \(19\.3\-A\.2\.2\.3 IN45/98\)

IND\_UTIL\_DEV\_ZERA

\[MFS89648\]

Se Quantidade Final \(QTD\_CONV\_FIM\_MP\) =__ 0__ e 

   Quantidade Devolução de Entrada QTD\_CONV\_DEV\_ENT\_MP <> 0 

Então:

   Preencher com “N”\.

Senão

   Não Preencher

Se o registro do dia anterior estiver com IND\_UTIL\_DEV\_ZERA = ‘N’, e o dia em foco não tiver movimentação, então propagar o IND\_UTIL\_DEV\_ZERA anterior para o dia corrente\. 

Não ter movimentação é quando as quantidades são zero: QTD\_CONV\_ENT\_MP =0, QTD\_CONV\_DEV\_SAI\_MP = 0 e QTD\_CONV\_DEV\_ENT\_MP = 0\.

Saldo utilizado p/ próximo dia c/ movimento, caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 \- 19\.3\-A\.2\.2\.3

Qtde total Convertida 

 \(19\.3\-A\.2\.2\.3 IN45/98\)

QTD\_CONV\_DEV\_ZERA

\[MFS89648\]

Se Quantidade Final \(QTD\_CONV\_FIM\_MP\) =__ 0__ e 

   Quantidade Devolução de Entrada QTD\_CONV\_DEV\_ENT\_MP <> 0

Então:

  Preencher com QTD\_CONV\_DEV\_ENT\_MP do dia\.

Senão

  Não preencher

Se o registro do dia anterior estiver com IND\_UTIL\_DEV\_ZERA = ‘N’, e o dia em foco não tiver movimentação, então propagar a QTD\_CONV\_DEV\_ZERA anterior para o dia corrente\.

Qtde \(Saldo Inicial p/ próximo dia c/ movimento, caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 \- 19\.3\-A\.2\.2\.3\)

Valor do ICMS 

 \(19\.3\-A\.2\.2\.3 IN45/98\)

VLR\_ICMS\_DEV\_ZERA

\[MFS89648\]

Se Quantidade Final \(QTD\_CONV\_FIM\_MP\) =__ 0__ e 

   Quantidade Devolução de Entrada QTD\_CONV\_DEV\_ENT\_MP <> 0

Então:

   Preencher com:

   \(Vlr Médio Unitário dia anterior – Vlr Unitário Dev Entrada\) \* qtde Dev Entrada

   Ou seja:

   \(VLR\_UNIT\_ICMS\_FIM\_MP do dia anterior – 

    \(VLR\_ICMS\_DEV\_ENT\_MP/ QTD\_CONV\_DEV\_ENT\_MP do dia\)

    \) \* QTD\_CONV\_DEV\_ENT\_MP do dia

Senão

  Não preencher

Se o registro do dia anterior estiver com IND\_UTIL\_DEV\_ZERA = ‘N’, e o dia em foco não tiver movimentação, então propagar o VLR\_ICMS\_DEV\_ZERA anterior para o dia corrente\.

Obs: Se não existir registro no dia anterior na Tabela de Média Ponderada, então considerar o VLR\_ICMS\_MEDIO da X52\_INVENT\_PRODUTO, ao invés do VLR\_UNIT\_ICMS\_FIM\_MP\.

Valor ICMS \(Saldo Inicial p/ próximo dia c/ movimento, caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 \- 19\.3\-A\.2\.2\.3\)

Valor do ICMS\-ST s/ FECEP

 \(19\.3\-A\.2\.2\.3 IN45/98\)

VLR\_ICMS\_ST\_DEV\_ZERA

\[MFS89648\]

Se Quantidade Final \(QTD\_CONV\_FIM\_MP\) =__ 0__ e 

   Quantidade Devolução de Entrada QTD\_CONV\_DEV\_ENT\_MP <> 0

Então:

   Preencher com:

   \(Vlr Médio Unitário dia anterior – Vlr Unitário Dev Entrada\) \* qtde Dev Entrada

   Ou seja:

   \(VLR\_UNIT\_ICMS\_ST\_FIM\_MP do dia anterior – 

    \(VLR\_ICMS\_ST\_DEV\_ENT\_MP/ QTD\_CONV\_DEV\_ENT\_MP do dia\)

    \) \* QTD\_CONV\_DEV\_ENT\_MP do dia

Senão

  Não preencher

Se o registro do dia anterior estiver com IND\_UTIL\_DEV\_ZERA = ‘N’, e o dia em foco não tiver movimentação, então propagar o VLR\_ICMS\_ST\_DEV\_ZERA anterior para o dia corrente\.

Obs: Se não existir registro no dia anterior na Tabela de Média Ponderada, então considerar o \(VLR\_ICMSS\_MEDIO \- VLR\_FCP\_MEDIO\) da X52\_INVENT\_PRODUTO, ao invés do VLR\_UNIT\_ICMS\_ST\_FIM\_MP\.

Valor ICMS\-ST s/ FECEP \(Saldo Inicial p/ próximo dia c/ movimento, caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 \- 19\.3\-A\.2\.2\.3\)

Valor do ICMS\-ST c/ Fecep

 \(19\.3\-A\.2\.2\.3 IN45/98\)

VLR\_ICMS\_ST\_FECEP\_DEV\_ZERA

\[MFS89648\]

Se Quantidade Final \(QTD\_CONV\_FIM\_MP\) =__ 0__ e 

   Quantidade Devolução de Entrada QTD\_CONV\_DEV\_ENT\_MP <> 0

Então:

   Preencher com:

   \(Vlr Médio Unitário dia anterior – Vlr Unitário Dev Entrada\) \* qtde Dev Entrada

   Ou seja:

   \(VLR\_UNIT\_ICMS\_ST\_FECEP\_FIM\_MP do dia anterior – 

    \(\(VLR\_ICMS\_ST\_DEV\_ENT\_MP \+ VLR\_FECEP\_ST\_DEV\_ENT\_MP\)/ 

       QTD\_CONV\_DEV\_ENT\_MP do dia\)

    \) \* QTD\_CONV\_DEV\_ENT\_MP do dia

Senão

  Não preencher

Se o registro do dia anterior estiver com IND\_UTIL\_DEV\_ZERA = ‘N’, e o dia em foco não tiver movimentação, então propagar o VLR\_ICMS\_ST\_FECEP\_DEV\_ZERA anterior para o dia corrente\.

Obs: Se não existir registro no dia anterior na Tabela de Média Ponderada, então considerar o \(VLR\_ICMSS\_MEDIO\) da X52\_INVENT\_PRODUTO, ao invés do VLR\_UNIT\_ICMS\_ST\_FECEP\_FIM\_MP\.

Valor ICMS\-ST c/ FECEP \(Saldo Inicial p/ próximo dia c/ movimento, caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 \- 19\.3\-A\.2\.2\.3\)

Valor Base de Cálculo do ICMS\-ST \(19\.3\-A\.2\.2\.3 IN45/98\)  

VLR\_BC\_ST\_DEV\_ZERA

\[MFS89648\]

Se Quantidade Final \(QTD\_CONV\_FIM\_MP\) =__ 0__ e 

   Quantidade Devolução de Entrada QTD\_CONV\_DEV\_ENT\_MP <> 0 

Então:

   Preencher com:

   \(Vlr Médio Unitário dia anterior – Vlr Unitário Dev Entrada\) \* qtde Dev Entrada

   Ou seja:

   \(VLR\_UNIT\_BC\_ST\_FIM\_MP do dia anterior – 

    \(VLR\_BC\_ST\_DEV\_ENT\_MP/ QTD\_CONV\_DEV\_ENT\_MP do dia\)

    \) \* QTD\_CONV\_DEV\_ENT\_MP do dia

Senão

  Não preencher

Se o registro do dia anterior estiver com IND\_UTIL\_DEV\_ZERA = ‘N’, e o dia em foco não tiver movimentação, então propagar a VLR\_BC\_ST\_DEV\_ZERA anterior para o dia corrente\.

Obs: Se não existir registro no dia anterior na Tabela de Média Ponderada, então considerar o VLR\_BASE\_ICMSS\_MEDIO da X52\_INVENT\_PRODUTO, ao invés do VLR\_UNIT\_BC\_ST\_FIM\_MP\.

Valor Base de Cálculo do ICMS\-ST \(Saldo Inicial p/ próximo dia c/ movimento, caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 \- 19\.3\-A\.2\.2\.3\)

Valor FECEP\-ST 

\(19\.3\-A\.2\.2\.3 IN45/98\)

VLR\_FECEP\_ST\_DEV\_ZERA

\[MFS89648\]

Se Quantidade Final \(QTD\_CONV\_FIM\_MP\) =__ 0__ e 

   Quantidade Devolução de Entrada QTD\_CONV\_DEV\_ENT\_MP <> 0 

Então:

   Preencher com:

   \(Vlr Médio Unitário dia anterior – Vlr Unitário Dev Entrada\) \* qtde Dev Entrada

   Ou seja:

   \(VLR\_UNIT\_FECEP\_ST\_FIM\_MP do dia anterior – 

    \(VLR\_FECEP\_ST\_DEV\_ENT\_MP/ QTD\_CONV\_DEV\_ENT\_MP do dia\)

    \) \* QTD\_CONV\_DEV\_ENT\_MP do dia

Senão

  Não preencher

Se o registro do dia anterior estiver com IND\_UTIL\_DEV\_ZERA = ‘N’, e o dia em foco não tiver movimentação, então propagar o VLR\_FECEP\_ST\_DEV\_ZERA anterior para o dia corrente\.

Obs: Se não existir registro no dia anterior na Tabela de Média Ponderada, então considerar VLR\_FCP\_MEDIO da X52\_INVENT\_PRODUTO, ao invés do VLR\_UNIT\_FECEP\_ST\_FIM\_MP\.

Valor FECEP\-ST \(Saldo Inicial p/ próximo dia c/ movimento, caso em que a devolução das entradas zera a quantidade final do dia, conforme IN45/98 \- 19\.3\-A\.2\.2\.3\)

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

__Obs\.: Todos os valores calculados devem ser arredondados, não devem ser truncados\.__

# <a id="_Toc63699484"></a>Relatório de Conferência

Gerar um arquivo excel a partir da leitura da tabela __EST\_ST\_RS\_MEDIA\_POND__

Nome do arquivo: Relatório\_Conferencia\_Calculo\_Media\_Ponderada\_mm\_aaaa\_cod\_estab\.xlsx

As quantidades e valores \(Saldo Inicial, Devolução, Entrada, Saldo final\.\.\.\) serão demonstrados em linhas e não por coluna\. Logo por dia/produto serão apresentadas as linhas identificadas pela descrição:

1. Saldo Inicial 
2. Devolução de Saída \(\+\)
3. Entrada \(\+\)
4. Devolução de Entrada \(\-\)
5. Saldo Final \(Total Dia\)
6. Valores Unitários Médios
7. Qtde Saída do Dia
8. Qtde Saída a deduzir p/ próximo dia c/ movimento
9. Saldo Inicial p/ próximo dia c/ movimento \(IN45/98 \- 19\.3\-A\.2\.2\.3\)

As colunas que compõe o relatório são as seguintes:

Coluna

Preenchimento

Cod Empresa

 

Cod Estab

 

Dia

 

Ind Produto \(SAFX2013\-01\) Cod Produto \(SAFX2013\-02\)

 

Descrição da Linha

1.  Saldo Inicial 
2. Devolução de Saída \(\+\)
3. Entrada \(\+\)
4. Devolução de Entrada \(\-\)
5. Saldo Final \(Total Dia\)
6. Valores Unitários Médios
7. Qtde Saída do Dia
8. Qtde Saída a deduzir p/ próximo dia c/ movimento
9. Saldo Inicial p/ próximo dia c/ movimento \(IN45/98 \- 19\.3\-A\.2\.2\.3\)

A linha \(9\) deve ser incluída apenas se IND\_UTIL\_DEV\_ZERA for diferente de nulo\! \[MFS89648\]

QTDE

Este campo é preenchido conforme a Descrição da Linha\.

Se Saldo Inicial, demonstrar a QTD\_CONV\_INI;

Se Devolução de Saída, demonstrar a QTD\_CONV\_DEV\_SAI\_MP

Se Entrada, demonstrar a QTD\_CONV\_ENT\_MP

Se Devolução de Entrada, demonstrar a QTD\_CONV\_DEV\_ENT\_MP

Se Saldo Final \(Total Dia\), demonstrar QTD\_CONV\_FIM

Se Valores Unitários Médios, não preencher esse campo;

Se Qtde Saída Dia, demonstrar a QTD\_CONV\_SAI\_DIA

Se Qtde Saída a deduzir p/ próximo dia c/ movimento, demonstrar a QTD\_CONV\_SAI\_MP

\[MFS89648\]

Se Saldo Inicial p/ próximo dia c/ movimento \(IN45/98 \- 19\.3\-A\.2\.2\.3\), __não__ demonstrar QTD\_CONV\_DEV\_ZERA;

Valor ICMS

Este campo é preenchido conforme a Descrição da Linha\.

Se Saldo Inicial, demonstrar a VLR\_ICMS\_INI\_MP;

Se Devolução de Saída, demonstrar a VLR\_ICMS\_DEV\_SAI\_MP 

Se Entrada, demonstrar a VLR\_ICMS\_ENT\_MP

Se Devolução de Entrada, demonstrar a VLR\_ICMS\_DEV\_ENT\_MP

Se Saldo Final \(Total Dia\), demonstrar VLR\_ICMS\_FIM\_MP

Se Valores Unitários Médios, demonstrar VLR\_UNIT\_ICMS\_FIM\_MP;

Se Qtde Saída Dia, demonstrar não preencher esse campo;

Se Qtde Saída a deduzir p/ próximo dia c/ movimento, não preencher esse campo;

\[MFS89648\]

Se Saldo Inicial p/ próximo dia c/ movimento \(IN45/98 \- 19\.3\-A\.2\.2\.3\), demonstrar VLR\_ICMS\_DEV\_ZERA;

Valor ICMS\-ST \(s/Fecep\)

Este campo é preenchido conforme a Descrição da Linha\.

Se Saldo Inicial, demonstrar a VLR\_ICMS\_ST\_INI\_MP;

Se Devolução de Saída, demonstrar a VLR\_ICMS\_ST\_DEV\_SAI\_MP 

Se Entrada, demonstrar a VLR\_ICMS\_ST\_ENT\_MP

Se Devolução de Entrada, demonstrar a VLR\_ICMS\_ST\_DEV\_ENT\_MP

Se Saldo Final \(Total Dia\), demonstrar VLR\_ICMS\_ST\_FIM\_MP

Se Valores Unitários Médios, demonstrar VLR\_UNIT\_ICMS\_ST\_FIM\_MP;

Se Qtde Saída Dia, demonstrar não preencher esse campo;

Se Qtde Saída a deduzir p/ próximo dia c/ movimento, não preencher esse campo;

\[MFS89648\]

Se Saldo Inicial p/ próximo dia c/ movimento \(IN45/98 \- 19\.3\-A\.2\.2\.3\), demonstrar VLR\_ICMS\_ST\_DEV\_ZERA;

Valor ICMS\-ST \(c/Fecep\)

Este campo é preenchido conforme a Descrição da Linha\.

Se Saldo Inicial, demonstrar a VLR\_ICMS\_ST\_INI\_MP \+ VLR\_FECEP\_ST\_INI\_MP;

Se Devolução de Saída, demonstrar a VLR\_ICMS\_ST\_DEV\_SAI\_MP \+ VLR\_FECEP\_ST\_DEV\_SAI\_MP

Se Entrada, demonstrar a VLR\_ICMS\_ST\_ENT\_MP \+ VLR\_FECEP\_ST\_ENT\_MP

Se Devolução de Entrada, demonstrar a VLR\_ICMS\_ST\_DEV\_ENT\_MP \+ VLR\_FECEP\_ST\_DEV\_ENT\_MP

Se Saldo Final \(Total Dia\), demonstrar VLR\_ICMS\_ST\_FIM\_MP \+ VLR\_FECEP\_ST\_FIM\_MP

Se Valores Unitários Médios, demonstrar VLR\_UNIT\_ICMS\_ST\_FECEP\_FIM\_MP;

Se Qtde Saída Dia, demonstrar não preencher esse campo;

Se Qtde Saída a deduzir p/ próximo dia c/ movimento, não preencher esse campo;

\[MFS89648\]

Se Saldo Inicial p/ próximo dia c/ movimento \(IN45/98 \- 19\.3\-A\.2\.2\.3\), demonstrar VLR\_ICMS\_ST\_FECEP\_DEV\_ZERA;

Valor Base de Cálculo do ICMS\-ST

Este campo é preenchido conforme a Descrição da Linha\.

Se Saldo Inicial, demonstrar a VLR\_BC\_ST\_INI\_MP;

Se Devolução de Saída, demonstrar a VLR\_BC\_ST\_DEV\_SAI\_MP;

Se Entrada, demonstrar a VLR\_BC\_ST\_ENT\_MP

Se Devolução de Entrada, demonstrar a VLR\_BC\_ST\_DEV\_ENT\_MP

Se Saldo Final \(Total Dia\), demonstrar VLR\_BC\_ST\_FIM\_MP 

Se Valores Unitários Médios, demonstrar VLR\_UNIT\_BC\_ST\_FIM\_MP;

Se Qtde Saída Dia, demonstrar não preencher esse campo;

Se Qtde Saída a deduzir p/ próximo dia c/ movimento, não preencher esse campo;

\[MFS89648\]

Se Saldo Inicial p/ próximo dia c/ movimento \(IN45/98 \- 19\.3\-A\.2\.2\.3\), demonstrar VLR\_BC\_ST\_DEV\_ZERA;

Valor FECEP\-ST 

Este campo é preenchido conforme a Descrição da Linha\.

Se Saldo Inicial, demonstrar a VLR\_FECEP\_ST\_INI\_MP;

Se Devolução de Saída, demonstrar a VLR\_FECEP\_ST\_DEV\_SAI\_MP 

Se Entrada, demonstrar a VLR\_FECEP\_ST\_ENT\_MP

Se Devolução de Entrada, demonstrar a VLR\_FECEP\_ST\_DEV\_ENT\_MP

Se Saldo Final \(Total Dia\), demonstrar VLR\_FECEP\_ST\_FIM\_MP

Se Valores Unitários Médios, demonstrar VLR\_UNIT\_FECEP\_ST\_FIM\_MP;

Se Qtde Saída Dia, demonstrar não preencher esse campo;

Se Qtde Saída a deduzir p/ próximo dia c/ movimento, não preencher esse campo;

\[MFS89648\]

Se Saldo Inicial p/ próximo dia c/ movimento \(IN45/98 \- 19\.3\-A\.2\.2\.3\), demonstrar VLR\_FECEP\_ST\_DEV\_ZERA;

Exemplo:

Cod Empresa

Cod Estab

Dia

Ind\-Cod Produto 

Descrição da Linha

QTDE

Valor ICMS

Valor ICMS\-ST \(s/Fecep\)

Valor ICMS\-ST \(c/Fecep\)

Valor Base de Cálculo do ICMS\-ST

Valor FECEP\-ST 

21

162148

01/02/2022

1\-001\-000000175

\(1\) Saldo Inicial

10

100

21

162148

01/02/2022

1\-001\-000000175

\(2\) Devolução de Saída \(\+\)

10

100

21

162148

01/02/2022

1\-001\-000000175

\(3\) Entrada \(\+\)

10

100

21

162148

01/02/2022

1\-001\-000000175

\(4\) Devolução de Entrada \(\-\)

10

100

21

162148

01/02/2022

1\-001\-000000175

\(5\) Saldo Final \(Total Dia\)

20

200

21

162148

01/02/2022

1\-001\-000000175

\(6\) Valores Unitarios Médios

10

21

162148

01/02/2022

1\-001\-000000175

\(7\) Qtde Saída do Dia

21

162148

01/02/2022

1\-001\-000000175

\(8\) Qtde Saída a deduzir p/ próximo dia c/ movimento

 

 

 

 

\(9\) Saldo Inicial p/ próximo dia c/ movimento \(IN45/98 \- 19\.3\-A\.2\.2\.3\)

# <a id="_Tratamento_para_Produtos"></a><a id="_Toc63699485"></a>Tratamento para Produtos não Movimentados:

Ao final do processamento do período, é necessário verificar se o produto sujeito a ST, gravado na tabela __EST\_ST\_RS\_MEDIA\_POND__, possui pelo menos um dia com um dos valores \(saldo inicial, devolução de saída, entrada, devolução de entrada\) diferente de zero\.

Se todos os valores estiverem zerados para todos os dias do período e estabelecimento da geração, esse produto não deve constar na tabela EST\_ST\_RS\_MEDIA\_POND\. Isso demonstra que o produto foi apenas parametrizado e não foi movimentado nem possui inventário para o estabelecimento e período da geração\. 

É importante excluir os produtos não movimentados da tabela EST\_ST\_RS\_MEDIA\_POND ao final do processamento, para evitar que num período subsequente ele seja movimentado e o Saldo Inicial não seja recuperado corretamente da Tabela do Inventário \(X52\_INVENT\_PRODUTO\), por existir registro na EST\_ST\_RS\_MEDIA\_POND do período anterior \(vide [1º passo](#_1º_Passo_–)\)\.

= = = = = =

 

