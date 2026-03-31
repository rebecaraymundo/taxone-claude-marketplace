# MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Cálculo Médio Unitario Inventário

- **Fonte:** MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Cálculo Médio Unitario Inventário.docx
- **Modificado:** 2024-01-22
- **Tamanho:** 183 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS 

\(IN\-RE 087/2020\) 

Cálculo dos Valores Unitários Médios do Inventário 

__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS\-ST \- RS \(IN\-RE 048/2018\), itens:

Geração à IN\-RE 087/20 à Geração dos Movimentos

	

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS72212__

Liliane Videira Assaf

Criação do Cálculo dos Valores Unitários Médios do Inventário

09/09/2021 

__MFS72429__

Andréa Rocha

Inclusão do arredondamento dos valores calculados, ou seja, os valores calculados não serão mais truncados\.  Conforme informação passada pela SEFAZ/RS\.

01/10/2021

__MFS81749__

Liliane Assaf

Tratamento para Notas de Produtos Farmacêuticos de Distribuidores criada pela MFS66473

15/03/2022

__MFS90131__

Liliane Assaf

Chamado Lasa/Magalu: Tratamento na diferença de 0,000001 do valor médio unitário do último dia do mês para o do primeiro dia do mês seguinte\. 

01/08/2022

__MFS591083__

Liliane Assaf

Tratamento das Incorporações de Empresas/Estabelecimentos

22/01/2024

Sumário

[1\.	Introdução	1](#_Toc82095692)

[2\.	Recuperação dos Dados e Processamento	1](#_Toc82095693)

[1º Passo – Recuperar os Produtos Sujeitos a ST que estão no primeiro período de geração e sem valores unitários no Inventário	1](#_Toc82095694)

[2º Passo – Recuperar as Notas de Entrada até cobrir a Quantidade do Estoque	1](#_Toc82095695)

[3º Passo: Calcular os Valores Unitários Médios	1](#_Toc82095696)

[4º Passo: Gravar os Valores Unitários Médios	1](#_Toc82095697)

[3\.	Relatório de Conferência	1](#_Toc82095698)

#  

# <a id="_Toc82095692"></a>Introdução

O Cálculo dos Valores Unitários Médios do ICMS, ICMS\-ST, Base de Cálculo do ICMS\-ST e FECEP\-ST do inventário do produto, para o primeiro período de geração\.

Originalmente a rotina de Geração do Movimento exigia que, para o primeiro período da geração de um Produto sujeito a ICMS\-ST, os Valores Unitários do ICMS, ICMS\-ST, Base de Cálculo do ICMS\-ST e FECEP\-ST viessem carregados na SAFX52 para o dia imediatamente anterior ao mês da geração\. Essa exigência se dava apenas para o primeiro mês, pois a partir do segundo período de geração, os Valores Unitários do ICMS, ICMS\-ST, Base de Cálculo do ICMS\-ST e FECEP\-ST são recuperados do cálculo da média ponderada realizada na geração do movimento do mês anterior\.

Mas alguns clientes tiveram dificuldade em calcular esses valores unitários para o primeiro período\. Sendo assim, criamos essa rotina para realizar o cálculo dos valores unitários, bastando para isso existir o registro de inventário na SAFX52 com quantidade maior que zero e IND\_MOT\_INV = 06, para o dia imediatamente anterior ao mês da geração\.

Os valores unitários calculados serão armazenados na tabela onde são armazenas as médias ponderadas dos períodos \(EST\_ST\_RS\_MEDIA\_POND\), para o produto e dia imediatamente anterior ao mês da geração\.

__Sobre Produtos Associados__:

Para identificar os produtos sujeitos a ICMS\-ST utilizamos as opções de parametrização do menu Parâmetros à Produtos:* “Por Código*”, ou “Por NCM” ou *“CEST”*\.  A parametrização Por Código aceita trabalharmos com o conceito de Produtos Associados\. Parametriza\-se um produto “principal” e *N* produtos associados\. O produto “principal” é gravado na tabela \(__ESP\_SP\_PROD\_ST__\), e os associados ao produto principal na tabela __ESP\_SP\_PROD\_ST\_ASS__\.  Os produtos associados servem para recuperação dos movimentos de entradas, saídas e devoluções \(x07/x08/x993/x994\)\.  Mas todo o controle de inventário \(x52\) é em nome do Produto Principal\.  __O Cálculo dos Valores Unitários Médios do Inventário é gravado em nome do Produto Principal__\.

__Texto da IN\-RE 087/20, Tópico 19\.3\-A\.3 que define Cálculo da Média Pondera Móvel dos Valores Unitários do Inventário:__

__19\.3\-A\.2\.1\.2\.1 \-__

__No primeiro dia de aplicação da sistemática, deverá ser utilizado o valor calculado no inventário das mercadorias previsto no subitem 19\.3\-A\.3\.__

__19\.3\-A\.3 \-__

__Conforme disposto no RICMS, Livro III, art\. 25\-B, parágrafo único, I, o contribuinte deverá apresentar o registro H005, com o campo MOT\_INV igual a "06" e DT\_INV igual ao dia imediatamente anterior ao campo DT\_INI informado no registro 0000, com informações do inventário das mercadorias recebidas com substituição tributária existentes em estoque no fim do dia 31 de dezembro de 2020 ou do dia anterior àquele em que passar a apurar o ajuste, se posterior a 1º de janeiro de 2021\. \(Acrescentado pela __[__IN RE 087/20__](http://www.legislacao.sefaz.rs.gov.br/Site/Document.aspx?inpKey=275375)__, de 03/11/20\. \(DOE 04/11/20\) \- Efeitos a partir de 04/11/20\.\)__

__19\.3\-A\.3\.1 \-__

__O inventário deverá ser apresentado no arquivo da EFD\-ICMS/IPI do mês subsequente ao evento\. \(Acrescentado pela __[__IN RE 087/20__](http://www.legislacao.sefaz.rs.gov.br/Site/Document.aspx?inpKey=275375)__, de 03/11/20\. \(DOE 04/11/20\) \- Efeitos a partir de 04/11/20\.\)__

__19\.3\-A\.3\.2 \-__

__Na hipótese em que não for possível determinar a correspondência entre a base de cálculo do débito de substituição tributária e a respectiva mercadoria, deverá ser utilizado o valor unitário da base de cálculo do débito de substituição tributária registrado no documento fiscal do último recebimento, proporcional à quantidade existente em estoque, desde que a quantidade constante desse documento fiscal seja maior ou igual ao somatório do estoque inventariado\. \(Acrescentado pela __[__IN RE 087/20__](http://www.legislacao.sefaz.rs.gov.br/Site/Document.aspx?inpKey=275375)__, de 03/11/20\. \(DOE 04/11/20\) \- Efeitos a partir de 04/11/20\.\)__

__19\.3\-A\.3\.2\.1 \-__

__Na hipótese em que a quantidade das mercadorias registradas no documento fiscal do último recebimento for menor que o somatório do estoque inventariado, serão adicionados os recebimentos registrados em documentos fiscais imediatamente anteriores, até que se complete a quantidade existente em estoque, hipótese em que deverá ser utilizado o valor médio ponderado unitário da base de cálculo do débito de substituição tributária\. \(Acrescentado pela __[__IN RE 087/20__](http://www.legislacao.sefaz.rs.gov.br/Site/Document.aspx?inpKey=275375)__, de 03/11/20\. \(DOE 04/11/20\) \- Efeitos a partir de 04/11/20\.\)__

Obs: texto bastante semelhante ao da CAT42 \(Ressarcimento SP\) do “MANUAL Sistema Ressarcimento\_ICMS\_ST\.pdf”:

__3\.3\.8 Para efeito de determinação do valor de confronto, e na impossibilidade de identificação da operação de entrada da mercadoria, o contribuinte substituí\-do considerará o valor correspondente às entradas mais recentes, suficientes para comportar a quantidade envolvida\. Caso o documento fiscal referente à entrada mais recente do item não seja suficiente para comportar a quantidade indicada no documento fiscal de saída, e se faça necessário utilizar documen\-to\(s\) fiscal\(ais\) anterior\(es\) ao último, o valor a ser lançado a título de valor de confronto corresponderá à média ponderada dos dados obtidos em todas as notas fiscais utilizadas para comportar a quantidade saída, conforme exemplo a seguir\. __

__Exemplo: Último documento de entrada: 10 unidades, a R$15,00 cada\. __

__Penúltimo documento de entrada: 20 unidades, a R$10,00 cada\. __

__Saída: 12 unidades\. __

__Valor de Confronto: 10 unidades a R$ 15,00 = R$ 150,00 \+ 2 unidades a R$ 10,00 = R$ 20,00\. __

__Valor total: R$ 170,00, que divididos por 12 = R$ 14,17 \(valor unitário a ser informado\)\. __

# <a id="_Toc350763252"></a><a id="_Toc59988568"></a><a id="_Toc82095693"></a>Recuperação dos Dados e Processamento 

__Visão resumida do Processamento__

Esse cálculo considera os __Produtos Sujeitos a ST__, no __primeiro período__ de geração do movimento da IN\-087, cujo Inventário está com __Valores Unitários zerados__\. 

Para esses produtos, o cálculo vai varrer as últimas entradas até que a quantidade das entradas atinja a quantidade o inventário, e calcular o valor unitário do ICMS, ICMS\-ST, Base ICMS\-ST e FECEP\-ST\.

## <a id="_1º_Passo_–"></a><a id="_Toc82095694"></a>1º Passo – Recuperar os Produtos Sujeitos a ST que estão no primeiro período de geração e sem valores unitários no Inventário 

Vamos recuperar os produtos sujeitos a ST cujo cálculo será realizado nos próximos passos\.

__Origem dos dados__: \- Parametrização de Produtos \(por Código, por NCM e por CEST\);

                                  \- Tabela do Inventário \(X52\_INVENT\_PRODUTO\)\.

__Critérios:__

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data do Inventário \(campo 03 \- DATA\_INVENTARIO\) último dia do mês anterior ao que está sendo processado;

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

\- Quantidade de Inventário \(X52\) > 0

\- Valores Unitários do Inventário \(X52\) zerados e IND\_GRAVACAO \(X52\) <> ‘9’:   \-\- significa que o cliente não carregou os valores unitários 

- 21 \- Valor de ICMS Médio \(VLR\_ICMS\_MEDIO\) = 0
- 22 \- Valor de ICMS\-ST Médio \(VLR\_ICMSS\_MEDIO\) = 0
- 43 \- Valor Base ICMS\-ST Médio \(VLR\_BASE\_ICMSS\_MEDIO\) = 0
- 44 \- Valor FECEP Médio \(VLR\_FCP\_MEDIO\) = 0
- IND\_GRAVACAO \(X52\)  <> 9

  OU                  \-\- reprocessamento da geração do movimento qdo já ocorreu a Transferência dos Movimentos p/ EFD

  Algum Valor Unitário \(X52\) diferente de zero __e__ IND\_GRAVACAO \(X52\) = ‘9’ __e__ existe Valor Unitário Calculado por essa rotina:    

- 21 \- Valor de ICMS Médio \(VLR\_ICMS\_MEDIO\) <>  0 OU 22 \- Valor de ICMS\-ST Médio \(VLR\_ICMSS\_MEDIO\) <> 0 OU 43 \- Valor Base ICMS\-ST Médio \(VLR\_BASE\_ICMSS\_MEDIO\) <> 0 OU 44 \- Valor FECEP Médio \(VLR\_FCP\_MEDIO\) <> 0
- IND\_GRAVACAO \(X52\) = 9
- Existe registro na Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\), com os critérios abaixo atendidos:

   \- Empresa – código da empresa do login;

   \- Estabelecimento – código do estabelecimento selecionado para geração;

   \- Data = último dia do mês anterior que está sendo processado;  

   \- Produto = Produto da Parametrização de Produtos \(por Código, por NCM e por CEST\);

   \- IND\_GRAVACAO = ‘__A’__ – significa que o os valores unitários foram calculados por essa rotina

\- Só recuperar os Produtos estão no __primeiro período__ de geração\. 

  Ou seja, o Produto que __não__ possua registro na Tabela de Média Ponderada para algum dia do mês anterior, com quantidade maior que zero:

        __Origem dos dados__: \- Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\)\.

        __Critérios:__

   \- Empresa – código da empresa do login;

   \- Estabelecimento – código do estabelecimento selecionado para geração;

   \- Data pertencente ao mês anterior que está sendo processado;

        \- Produto = Produto da Parametrização de Produtos \(por Código, por NCM e por CEST\);

  \- Qtde total Convertida Inicial \(QTD\_CONV\_INI\) >0 __OU__ Quantidade de Devolução de Saída \(QTD\_CONV\_DEV\_SAI\_MP\) > 0 __OU__ 

    Quantidade Entrada Convertida \(QTD\_CONV\_ENT\_MP\)>0 __OU__ Quantidade Devolução de Entrada \(QTD\_CONV\_DEV\_ENT\_MP\) >0 __OU__ 

    Qtde total Convertida Final \(QTD\_CONV\_FIM\)> 0

__\[__[__MFS81749__](https://jira.thomsonreuters.com/browse/MFS-81749)__\]__

__Tratamento para Produtos Farmacêuticos de Distribuidores:__

<a id="_Hlk75258358"></a>\- Não recuperar o inventário de Produtos Farmaceuticos de Estabelecimentos Distribuidores\. Ou seja, se os dois critérios a seguir forem atendidos, não recuperar o inventário:

- Estabelecimento é um __Distribuidor__ \(atacadista\), ou seja, na Tela de Dados Iniciais estiver com o campo “Contribuinte Varejista?” = Não; 
- <a id="_Hlk78292438"></a>__Produto__ do inventário estiver cadastrado, na tela de Parametrização de Produtos Farmacêuticos por Código, no menu: Parametros >  \(IN\-RE 087/20\) > Produtos Farmacêuticos > Código

__Recuperação da Quantidade da Tabela de Inventário \(X52\_INVENT\_PRODUTO\) __

Os critérios acima podem retornar mais de um registro de inventário para o mesmo produto\. Caso isso ocorra, recuperar registro a registro, individualmente\. Considerar as seguintes informações:

- 12 \- Unidade de Medida \(COD\_MEDIDA\)
- 13 \- Quantidade de Inventário \(QUANTIDADE\)

Calcular a quantidade convertida:

- Qtde total Convetida Final:

Campo 13\-Quantidade de Inventário, aplicando a conversão, quando necessário\. Veja:

__Se__ unidade do inventário __\(\*\)__ = unidade do cadastro do produto __\(\*\*\) __

      __\(\*\)__ unidade do inventário = campo “12\-Unidade de Medida” da SAFX52

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será a própria quantidade do inventário;

__Senão __

         Nesse caso a quantidade do inventário \(SAFX52\) será convertida para a unidade de medida do cadastro do produto;

         \[Quantidade de Inventário \(SAFX52\) \* Fator de Conversão\]

__Sobre a conversão de medida:__

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas será gravada a seguinte mensagem de erro no log:

“C*álculo dos Valores Unitários do Inventário: O cálculo dos Valores Unitários do Inventário não foi realizado para o produto x\-yyyyy, pois não foi possível converter a quantidade do inventário para a medida do cadastro do produto \(fator de conversão de XXX para XXX não identificado\)\.”*

Onde x\-yyyyy são o indicador e código do produto\.

O primeiro “XXX” é a unidade do inventário, e o segundo “XXX”, a unidade do cadastro do produto\.

## <a id="_Toc82095695"></a>2º Passo – Recuperar as Notas de Entrada até cobrir a Quantidade do Estoque

Para cada produto sujeito a ST recuperado no passo anterior com a quantidade do estoque convertida, recuperar as últimas notas de entradas de períodos anteriores, até atingir a quantidade de estoque, e calcular o valor unitário médio a partir dos valores \[__ICMS__ \], \[ __BC ICMS\-ST__ \], \[ __ICMS\-ST__ \] e \[__FECEP\-ST__ \] com base em todas as entradas identificadas\. 

Neste passo será feita a recuperação das últimas entradas do produto na SAFX07/SAFX08, __da nota mais recente para as mais antigas__, considerando os critérios a seguir:

__Origem dos dados__: \- SAFX07 / SAFX08 – Tabelas dos Documentos Fiscais \(DATAMART ou X07/X08\)

                                    

__Critérios:__

\- Empresa                  = Código da empresa do login

\- Estabelecimento      = Código do estabelecimento selecionado para geração

\- Data Fiscal das notas de entradas >= a data informada em “*Pesquisar as últimas entradas até*” \(parâmetro da tela de geração\)

\- Data Fiscal das notas de entradas <= último dia do mês anterior ao que está sendo processado

\- Movimento E/S        = deve ser uma nota de entrada \(MOVTO\_E\_S <> “9”\) 

\- Normal/Devolução   = deve ser uma nota normal \(NORM\_DEV = ‘1’\)

\- Somente notas *não canceladas*;

\- Quantidade > 0

\- Produto                    = produto sujeito a ST

\- O CFOP ou CFOP/Natureza do item deve constar na parametrização do menu “*Parâmetros à \(IN\-RE 087/20\) à Operações*” para a seguinte operação:

- Entradas \(e Devoluções\)” \(código parâmetro 771\)

\- Serão recuperadas as notas de entrada suficientes para cobrir a quantidade do __Estoque__ <a id="OLE_LINK45"></a><a id="OLE_LINK46"></a><a id="OLE_LINK47"></a>*\(ver item abaixo que detalha sobre como totalizar a quantidade das entradas\)*__;__

\- A pesquisa das notas será feita até atingir a quantidade do estoque, __ou__, até que a Data Limite informada para a pesquisa seja atingida\. Este limite é identificado através do parâmetro “__*Pesquisar as últimas entradas até*__” da tela da geração\. Isso significa que devem ser consideradas apenas as notas com a DATA\_FISCAL que não exceda a data limite estabelecida no parâmetro;

__\[MFS591083\] Tratamento das Incorporações de Empresas/Estabelecimentos:__

\- Se o total da quantidade das notas de entrada recuperadas com os critérios acima, não for suficiente para cobrir a quantidade do estoque em questão, verificar se o parâmetro para buscar as notas nas empresas incorporadas está marcado na tela da geração\. 

     Se o parâmetro “Considerar as notas fiscais da empresa incorporada” estiver marcado:

           Considerar as notas das empresas/estabelecimentos cadastradas como incorporadas na tela de Relação de Empresa 

           Incorporadora x Incorporada\*\* para a empresa/estabelecimento da geração \(incorporadora\), para recuperar as notas de  

           entrada afim de atingir a quantidade de estoque do produto\.

    Senão

          Considerar somente as notas fiscais da empresa e estabelecimento selecionados para a geração\.

\*\* Módulo Parâmetros, item Preliminares 🡪 Relação de Empresa Incorporadora x Incorporada

O parâmetro “__*Utilizar DATA MART para períodos anteriores*__” determinará se a nota fiscal de entrada será recuperada das Tabelas Normais \(X07/X08\), ou das Tabelas DATAMART \(dwt\)\. Caso o parâmetro esteja selecionado, as tabelas DATAMART serão consideradas, caso contrário utilizar as tabelas Normais \(X07/X08\)\.

__Mensagem de aviso quando não identificar entradas p/ o produto:__

Se nenhuma entrada for identificada para o produto em questão, o cálculo do Valor Unitário *não* será realizado, e no log de erro será gravada a seguinte mensagem: *“*C*álculo dos Valores Unitários do Inventário: O cálculo dos Valores Unitários do Inventário não foi realizado para o produto x\-yyyyy, pois não foram encontradas notas de entrada do produto\. Consultar os detalhes e pré\-requisitos do cálculo no help e roteiro operacional do módulo”\.*

* *

Onde x\-yyyyy são o indicador e código do produto\.

__Como totalizar a quantidade das notas de entrada e comparar com a QTD do estoque do produto em questão:__

A quantidade das notas de entrada, quando necessário, será convertida para a unidade de medida do cadastro do produto \(SAFX2013\)\. 

Este procedimento é feito antes de utilizar a informação do campo, já que todas as quantidades devem estar na mesma unidade de medida\. 

__Se__ a unidade de medida do item da entrada = unidade de medida do cadastro do produto: 

      \(campo “25\-Unidade de Medida” da SAFX08 = campo “14\-Código de Medida” da SAFX2013\)

       Nesse caso, não é necessário efetuar a conversão;

__Senão __

     __Se__ existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\)

         Nesse caso, será utilizada a informação da quantidade já convertida do campo “137\-Quantidade Convertida”;

     __Senão         __

         Nesse caso a quantidade da entrada item \(SAFX08\) será convertida para a unidade de medida do cadastro do produto;

__Para efetuar a conversão de medida__:

A conversão é feita conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da mesma forma que é feita na rotina de geração dos movimentos:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o cálculo do Valor Unitário *não* será realizado para o produto, e no log de erro será gravada a seguinte mensagem: *“*C*álculo dos Valores Unitários do Inventário: O cálculo dos Valores Unitários do Inventário não foi realizado para o produto x\-yyyyy, pois não foi possível converter a quantidade de nota de entrada para a medida do cadastro do produto \(fator de conversão de XXX para XXX não identificado\)\.” *

Onde x\-yyyyy são o indicador e código do produto\. O* primeiro “XXX” é a unidade do item da entrada, e o segundo “XXX”, a unidade do cadastro do produto\.*

O log deve exibir as seguintes informações para conferência do usuário:

\- Identificação do item da nota de __entrada__ \(ao menos o número, série, data e item\);

<a id="OLE_LINK41"></a><a id="OLE_LINK42"></a><a id="OLE_LINK43"></a><a id="OLE_LINK44"></a>  

__Crítica da Quantidade das Entradas x QTD do Estoque:__

O total da quantidade das notas de entrada recuperadas da SAFX07/SAFX08 deve ser >= a quantidade do __Estoque__ em questão\. Caso contrário, será gravada a seguinte mensagem no log, e o cálculo do Valor Unitário *não* será realizado para o produto em questão: *“*C*álculo dos Valores Unitários do Inventário: O cálculo dos Valores Unitários do Inventário não foi realizado para o produto x\-yyyyy, pois as entradas recuperadas da SAFX07/SAFX08 não foram suficientes para cobrir a quantidade em estoque” *

Este problema poderá ocorrer quando a pesquisa das entradas na SAFX07/SAFX08 for realizada até a data limite especificada, mas a quantidade total das notas recuperadas não for suficiente para cobrir a quantidade do estoque em questão;

*\(Conforme já citado acima, para totalizar a quantidade das entradas, será utilizada a informação da quantidade já convertida, quando for o caso\) *

## <a id="_3º_Passo:_Calcular"></a><a id="_Toc82095696"></a>3º Passo: Calcular os Valores Unitários Médios 

As entradas recuperadas para o produto em questão serão processadas em ordem de data, __sempre da mais recente para mais antiga__\.

Para cada entrada a ser processada será calculado um valor de __ICMS__, um de __ICMS\-ST__, um de __Base ICMS\-ST__ e um de __FECEP\-ST__, conforme a regra abaixo\. 

- Se quantidade do Estoque __=__ quantidade da entrada, considerar __*Valor ICMS *__= Valor ICMS da entrada \(vide “__Considerações__”\);

                                                                                                                  __*Valor ICMS\-ST *__= Valor ICMS\-ST da entrada \(vide “__Considerações__”\);

                                                                                                                  __*Valor Base ICMS\-ST *__= Valor Base ICMS\-ST da entrada \(vide “__Considerações__”\);

                                                                                                                  __*Valor FECEP\-ST *__= Valor FECEP\-ST da entrada \(vide “__Considerações__”\);

- Se quantidade do Estoque __>__ quantidade da entrada, considerar __*Valor ICMS*__ = Valor ICMS da entrada \(vide__ __“__Considerações__”\);

                                                                                                       __*Valor ICMS\-ST *__= Valor ICMS\-ST da entrada \(vide “__Considerações__”\);

                                                                                                                   __*Valor Base ICMS\-ST *__= Valor Base ICMS\-ST da entrada \(vide “__Considerações__”\);

                                                                                                                   __*Valor FECEP\-ST *__= Valor FECEP\-ST da entrada \(vide “__Considerações__”\);

- Se quantidade do Estoque __<__ quantidade da entrada, calcular os valores do ICMS, ICMS\-ST, Base\-ST e FECEP\-ST proporcional à quantidade restante para cobrir o estoque, da seguinte forma: 

                                          \[ __*Valor ICMS*__ = \(Valor ICMS da entrada  / quantidade da entrada\) \* quantidade do estoque \]

                                          \[ __*Valor ICMS\-ST*__ = \(Valor ICMS\-ST da entrada  / quantidade da entrada\) \* quantidade do estoque\]

                                          \[__*Valor Base ICMS\-ST *__= Valor Base ICMS\-ST da entrada / quantidade da entrada\) \* quantidade do estoque\]  

                                          \[ __*Valor FECEP\-ST*__ = \(Valor FECEP\-ST da entrada  / quantidade da entrada\) \* quantidade do estoque\]

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

__Obs\.: Todos os valores calculados acima devem ser arredondados, não devem ser truncados\.__

           __\[MFS90131\] __Arredondar para 8 casas decimais o resultado dos cáculos acima \( \(valor / qtde\) \* qtde\)

Após o processamento de todas as entradas, calcular os __Valores Unitários Médios do ICMS, ICMS\-ST \(sem e com FECEP\), Base\-ST e do FECEP\-ST__:

Valor Médio Unitário do ICMS

Somatório do “Valor ICMS” de todas as entradas dividido pela Quantidade do Estoque\.

Valor Médio Unitário do ICMS\-ST s/ FECEP 

Somatório do “Valor ICMS\-ST” de todas as entradas dividido pela Quantidade do Estoque\.

Valor Médio Unitário do ICMS\-ST c/ FECEP 

Somatório dos \(“Valor ICMS\-ST” \+ “Valor FECEP\-ST”\) de todas as entradas dividido pela Quantidade do Estoque\.

Valor Médio Unitário da Base de Cálculo do ICMS\-ST

Somatório do “Valor Base ICMS\-ST” de todas as entradas dividido pela Quantidade do Estoque\.

Valor Médio Unitário do FECEP\-ST

Somatório do “Valor FECEP\-ST” de todas as entradas dividido pela Quantidade do Estoque\.

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

__Obs\.: Todos os valores unitários calculados acima devem ser arredondados, não devem ser truncados\.__

__\[MFS90131\] __Arredondar para 8 casas decimais o resultado dos cáculos \(valor / qtde\)

__Considerações:__

- A “*quantidade da entrada*” utilizada no cálculo é a quantidade da nota de entrada já convertida \(conforme a regra de conversão já descrita acima\);

  

- O “*Valor ICMS da entrada*” utilizado no cálculo será o valor do ICMS do item \(campo “43\-Valor ICMS”, se preenchido, ou campo “80\-ICMS não Escriturado”, se preenchido, ou campo "225\-Valor ICMS Não Destacado"\);
- O “*Valor ICMS\-ST da entrada*” utilizado no cálculo será os valores \(“52\-Valor ICMS Substituição Tributária”, ou “145\-Valor de ICMS\-ST não \.Escriturado”, ou "133\-ICMS\-ST Não Escriturado", ou “107\-Valor Carga Tributária Origem”\), aplicando o tratamento do Fecep embutido, conforme descrito a seguir:

__Tratamento do FECEP\-ST quando embutido no ICMS\-ST__

Tratamento do FECEP embutido nos vlrs de ICMS/ICMS\-ST \(aplicado às Entradas e Devoluções de Entradas\):

Se o item de mercadoria foi recuperado das tabelas “normais” \(X07/X08\), então:

      Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” da Parametrização dos Dados Iniciais foi marcado, então:

             Se for considerado o “52\-Valor ICMS Substituição Tributária” p/ o __Valor do ICMS\-ST__ :

    Preencher com: \(Valor do ICMS\-ST\- Valor do FECEP\-ST\) 

Senão:

                  Preencher com: \(Valor do ICMS\-ST\) 

      Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” da Parametrização dos Dados Iniciais não foi marcado, então:

           Preencher com: \(Valor do ICMS\-ST\) 

Se o item de mercadoria foi recuperado das tabelas do DATAMART, então:

     Se for considerado o “52\-Valor ICMS Substituição Tributária” para o__ Valor do ICMS\-ST__ :

           Preencher com:  \(Valor do ICMS\-ST \- Valor do FECEP\-ST\) 

     Senão

           Preencher com: \(Valor do ICMS\-ST\) 

Onde:

__\- Valor do ICMS\-ST__ \(\*\): Valor do ICMS\-ST é oriundo de um dos quatro campos do item da nota fiscal de Entrada \(SAFX08\), dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor do ICMS\-ST = 52\-VLR\_SUBST\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

         Valor do ICMS\-ST = 145\- VLR\_ICMSS\_N\_ESCRIT\.

    Senão:

        Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                         “133\- VLR\_ICMSS\_NDESTAC” preenchidos, então:

             Valor do ICMS\-ST = 133\- VLR\_ICMSS\_NDESTAC\.

        Senão:

            Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e 

                             “107\- VLR\_TRIB\_ICMS\_ORIG” preenchidos, então:

                 Valor do ICMS\-ST = 107\- VLR\_TRIB\_ICMS\_ORIG

- O “*Valor Base ICMS\-ST da entrada*” utilizado no cálculo será um dos valores \(61\-BASE\_SUB\_TRIB\_ICMS ou 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT ou 106\-VLR\_BASE\_ICMS\_ORIG\) conforme descrito abaixo:

Preencher com: 61\-BASE\_SUB\_TRIB\_ICMS ou 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT ou 106\-VLR\_BASE\_ICMS\_ORIG \(conforme regras abaixo\):

                       Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

Considerar os campos “61\-BASE\_SUB\_TRIB\_ICMS” da SAFX08\.

                      Senão

                          Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

Considerar os campos “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT da SAFX08\.

                         Senão

                             Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e “133\- VLR\_ICMSS\_NDESTAC” estiverem preenchidos, então: 

Considerar os campos “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” da SAFX08 

                            Senão

Se campo “106\-VLR\_BASE\_ICMS\_ORIG” e “107\-VLR\_TRIB\_ICMS\_ORIG” estiverem preenchidos, então: 

Considerar o campo “106\-VLR\_BASE\_ICMS\_ORIG” da SAFX08\.

- O “*Valor FECEP\-ST da entrada*” utilizado no cálculo será o valor do FECEP ICMST\-ST do item \(campo “140\-Valor FECEP ICMS\-ST"\);
- A “*quantidade do estoque*” utilizado no cálculo é a quantidade que consta na X52\_INVENT\_PRODUTO\. Ao processar a primeira nota de entrada, é utilizada a quantidade integral do estoque\. Para as próximas entradas, a “quantidade do estoque” será a quantidade integral do estoque, menos a quantidade das entradas processadas anteriormente \(ver o exemplo abaixo\);

Observação: As notas de entrada com os valores considerados no cálculo serão demonstradas num relatório gravado em arquivo excel\. Ver tópico 3 – [Relatório de Conferência](#_Relatório_de_Conferência)\.

Exemplo:

O exemplo a seguir é básico, mostra apenas o conceito do cálculo descrito acima e foi feito com base no exemplo dado para o cálculo do valor do confronto na “*MTZ\-Ressarc\-SP\-Calculo\_Vlr\_Confronto\_Saidas*”\.  

__EXEMPLO 1: PRODUTO XXX – inventário em 30/04__

__Notas de Entrada__:

__   Data               NF           QTD       Valor        ICMS   ICMS\-ST   BASE\-ST   FECEP\-ST__

25/04/2019      __450__       10,0000      50,00        6,00       5,00         8,00            4,00

08/05/2019      __511__         2,0000      13,50        1,62       3,62         5,00            2,62

__Inventário__:

__   Data              QTD       __

30/04/2019       5,0000      

__Cálculo do Valor Unitário do Inventário de 30/04:__

Nota de Entrada: __450__ \(de 25/04\) 

A Quantidade do Estoque \(5,0000\) é __<__ Quantidade da entrada \(10,0000\), logo:

__* Valor ICMS*__ = \(6,00 / 10,0000\) \* 5,0000 = __3,00__

__* Valor ICMS\-ST*__ = \(5,00 / 10,0000\) \* 5,0000 = __2,50* *__

__* Valor Base\-ST*__ = \(8,00 / 10,0000\) \* 5,0000 = __4,00__

__*  *__

                                                                                              Valor Unitário ICMS = \(3,00\)/5,00 = 0,6

                                                                                              Valor Unitário ICMS\-ST = \(2,50\)/5,00 = 0,5

                                                                                              Valor Unitário Base ICMS\-ST = \(4,00\)/5,00 = 0,8

                                                                                              Valor Unitário FECEP\-ST = \(2,00\)/5,00 = 0,4

__EXEMPLO 2: PRODUTO XXX – inventário em 31/05__

__Notas de Entrada__:

__   Data               NF           QTD       Valor        ICMS   ICMS\-ST   BASE\-ST   FECEP\-ST__

25/04/2019      __450__       10,0000      50,00        6,00       5,00         8,00            4,00

08/05/2019      __511__         2,0000      13,50        1,62       3,62         5,00            2,62

__Inventário__:

__   Data              QTD       __

31/05/2019       5,0000      

__Cálculo do Valor Unitário do Inventário de 31/05\):__

  

Nota de entrada: __511__ \(de 08/05\)

A Quantidade do Estoque \(5,0000\) é __>__ Quantidade da entrada \(2,0000\), logo:

__* Valor ICMS*__ = 1,62 

__* Valor ICMS\-ST*__ = 3,62

__*Valor Base\-ST*__ = 5,00

__* Valor FECEP\-ST*__ = 2,62

Saldo quantidade do Estoque a ser considerada no cálculo da próxima entrada: 5,0000 – 2,0000 = __3,0000__

Nota de entrada: __450 __\(de 25/04\)

A Quantidade da Dev\. Saída \(__3,0000__\) é __<__ Quantidade da entrada \(10,0000\), logo:

 __*Valor ICMS*__ = \(6,00 / 10,0000\) \* __3,0000__ = __1,80__

__* Valor ICMS\-ST*__ = \(5,00 / 10,0000\) \* __3,0000__ = __1,50* *__

__*Valor Base\-ST*__ = \(8,00 / 10,0000\) \* __3,0000__ = __2,4__

__* Valor FECEP\-ST*__ = \(4,00 / 10,0000\) \* __3,0000__ = __1,20__

                                                                                              Valor Unitário ICMS = \(1,62 \+ 1,80\)/5,00 = 0,68

                                                                                              Valor Unitário ICMS\-ST = \(3,62 \+ 1,50\)/5,00 = 1,02

                                                                                              Valor Unitário Base ICMS\-ST = \(5,00 \+ 2,40\)/5,00 = 1,48

                                                                                              Valor Unitário FECEP\-ST = \(2,62 \+ 1,20\)/5,00 = 0,76

## <a id="_4º_Passo:_Gravar"></a><a id="_Toc82095697"></a>4º Passo: Gravar os Valores Unitários Médios

Para cada __Produto__ sujeito ao ICMS\-ST\(\*\), gravar um registro na tabela __EST\_ST\_RS\_MEDIA\_POND__ com os valores unitários calculados no [Passo 3](#_3º_Passo:_Calcular), para o último dia do mês anterior\.

__Tabela EST\_ST\_RS\_MEDIA\_POND__

Os campos sinalizados com asterisco compõem a chave da tabela\.

__PK__

__Campo__

__Regra de Preenchimento__

\(\*\)

Código do Estabelecimento

COD\_ESTAB

Código do estabelecimento SELECIONADO na tela de geração

\(\*\)

Código da Empresa 

COD\_EMPRESA

Código da empresa de login 

\(\*\)

Código do Estabelecimento

COD\_ESTAB\_ORIG

Código do estabelecimento SELECIONADO na tela de geração

\(\*\)

Data 

DATA

Último dia do mês anterior\.

\(\*\)

Produto

Grupo\_Produto, Ind\_Produto,

Cod\_Produto

Produto sujeito ao ICMS\-ST foco do processamento\.

__Saldo Inicial do Dia__

Qtde total Convetida Inicial

QTD\_CONV\_INI

Preencher com zero\.

Valor do ICMS Calculado Inicial

VLR\_ICMS\_INI\_MP

Preencher com zero\.

Valor do ICMS\-ST Calculado Inicial

VLR\_ICMS\_ST\_INI\_MP

Preencher com zero\.

Valor Base de Cálculo do ICMS\-ST Calculado Inicial

VLR\_BC\_ST\_INI\_MP

Preencher com zero\.

Valor FECEP\-ST Calculado Inicial

VLR\_FECEP\_ST\_INI\_MP

Preencher com zero\.

__Devoluções das Saídas do Dia__

Quantidade Devolvida Convertida

QTD\_CONV\_DEV\_SAI\_MP

Preencher com zero\.

Valor do ICMS Calculado para Devolução

VLR\_ICMS\_DEV\_SAI\_MP

Preencher com zero\.

Valor do ICMS\-ST Calculado para Devolução

VLR\_ICMS\_ST\_DEV\_SAI\_MP

Preencher com zero\.

Valor Base de Cálculo do ICMS\-ST Calculado para Devolução

VLR\_BC\_ST\_DEV\_SAI\_MP

Preencher com zero\.

Valor FECEP\-ST Calculado para Devolução

VLR\_FECEP\_ST\_DEV\_SAI\_MP

Preencher com zero\.

__Entradas do Dia__

Quantidade Entrada Convertida

QTD\_CONV\_ENT\_MP

Preencher com zero\.

Valor do ICMS Calculado para Entrada

VLR\_ICMS\_ENT\_MP

Preencher com zero\.

Valor do ICMS\-ST Calculado para Entrada

VLR\_ICMS\_ST\_ENT\_MP

Preencher com zero\.

Valor Base de Cálculo do ICMS\-ST Calculado para Entrada

VLR\_BC\_ST\_ENT\_MP

Preencher com zero\.

Valor FECEP\-ST Calculado para Entrada

VLR\_FECEP\_ST\_ENT\_MP

Preencher com zero\.

__Devoluções das Entradas do Dia__

Quantidade Devolvida Convertida

QTD\_CONV\_DEV\_ENT\_MP

Preencher com zero\.

Valor do ICMS Calculado para Devolução

VLR\_ICMS\_DEV\_ENT\_MP

Preencher com zero\.

Valor do ICMS\-ST Calculado para Devolução

VLR\_ICMS\_ST\_DEV\_ENT\_MP

Preencher com zero\.

Valor Base de Cálculo do ICMS\-ST Calculado para Devolução

VLR\_BC\_ST\_DEV\_ENT\_MP

Preencher com zero\.

Valor FECEP\-ST Calculado para Devolução

VLR\_FECEP\_ST\_DEV\_ENT\_MP

Preencher com zero\.

__Saldo Final do Dia__

Qtde total Convetida Final

QTD\_CONV\_FIM

Preencher com zero\.

Valor do ICMS Calculado Final

VLR\_ICMS\_FIM\_MP

Preencher com zero\.

Valor do ICMS\-ST Calculado Final

VLR\_ICMS\_ST\_FIM\_MP

Preencher com zero\.

Valor Base de Cálculo do ICMS\-ST Calculado Final

VLR\_BC\_ST\_FIM\_MP

Preencher com zero\.

Valor FECEP\-ST Calculado Final

VLR\_FECEP\_ST\_FIM\_MP

Preencher com zero\.

__Valores Médios Unitários Calculados do Dia__

Valor Médio Unitário do ICMS

VLR\_UNIT\_ICMS\_FIM\_MP

Valor Médio Unitário do ICMS calculado no [passo 3](#_3º_Passo:_Calcular)\.

__\[MFS90131\]__ Arredondar para 8 casas decimais o resultado do cáculo \(vide passo 3\)\.

Valor Médio Unitário do ICMS\-ST s/ FECEP 

VLR\_UNIT\_ICMS\_ST\_FIM\_MP

Valor Médio Unitário do ICMS\-ST s/ FECEP calculado no [passo 3](#_3º_Passo:_Calcular)\.

__\[MFS90131\]__ Arredondar para 8 casas decimais o resultado do cáculo \(vide passo 3\)\.

Valor Médio Unitário do ICMS\-ST c/ FECEP 

VLR\_UNIT\_ICMS\_ST\_FECEP\_FIM\_MP

Valor Médio Unitário do ICMS\-ST c/ FECEP calculado no [passo 3](#_3º_Passo:_Calcular)\.

__\[MFS90131\]__ Arredondar para 8 casas decimais o resultado do cáculo \(vide passo 3\)\.

Valor Médio Unitário da Base de Cálculo do ICMS\-ST

VLR\_UNIT\_BC\_ST\_FIM\_MP

Valor Médio Unitário da Base de Cálculo do ICMS\-ST calculado no [passo 3](#_3º_Passo:_Calcular)\.

__\[MFS90131\]__ Arredondar para 8 casas decimais o resultado do cáculo \(vide passo 3\)\.

Valor Médio Unitário do FECEP\-ST

VLR\_UNIT\_FECEP\_ST\_FIM\_MP

Valor Médio Unitário do FECEP\-ST calculado no [passo 3](#_3º_Passo:_Calcular)\.

__\[MFS90131\]__ Arredondar para 8 casas decimais o resultado do cáculo \(vide passo 3\)\.

Indicador de Gravação

IND\_GRAVACAO

‘A’ – significa que o os valores unitários foram calculados por essa rotina

Número do Processo

PROC\_ID

Número do Processo da geração do movimento

Obs: Limpar os registros de processos anteriores da tabela __EST\_ST\_RS\_MEDIA\_POND__  com IND\_GRAVACAO = A\.

# <a id="_Relatório_de_Conferência"></a><a id="_Toc82095698"></a>Relatório de Conferência

Gravar num arquivo excel com o seguinte conteúdo:

Para cada produto sujeito a ST considerado no cálculo:

\- um ou mais registros correspondentes às notas de entrada consideradas no cálculo\.

\- UM registro demonstrando a quantidade do inventário e os valores unitários médios calculados, que foram gravados na tabela __EST\_ST\_RS\_MEDIA\_POND__\.

Nome do arquivo: Relatório\_Conferencia\_Calculo\_Media\_Inventário\_mm\_aaaa\_cod\_estab\.xlsx

Abaixo estão discriminados por cores, os campos que serão gravados para as notas e para o inventário:

\- Em azul: campos que devem ser preenchidos apenas para os registros de notas de entrada

\- Em verde: campos que devem ser preenchidos para o registro de inventário 

\- Em preto: campos que devem ser preenchidos para todos os registros \(notas e inventário\)\.

__MFS591083: __Tratamento das Incorporações de Empresas/Estabelecimentos

__Código da empresa__

Empresa de login

__Código do estabelecimento__

Estabelecimento informado na tela de geração\.

__Período \(mês e ano\)__

Período informado na tela de geração\.

__Produto \(ind\-cod\)__

Indicador \+ \- \+ Código do produto da Nota de entrada recuperada no passo 3 \(campo 13 e 14 \- SAFX08\)\.

__Data Inventário__

Data do Inventario recuperado no [passo 1](#_1º_Passo_–) \(último dia do mês anterior ao que está sendo processado\)

__Cod Empresa do Doc Fiscal__

Codigo da Empresa da Nota de Entrada \(campo 01 \- SAFX08\)

__Cod Estab do Doc Fiscal__

Codigo do Estabelecimento da Nota de Entrada \(campo 01 \- SAFX08\)

__Data Fiscal __

Data Fiscal da Nota de entrada considerada no cálculo no [passo 3](#_3º_Passo:_Calcular) \(campo 03 \- SAFX08\)\.

__Tipo do Documento__

Tipo Documento da Nota de entrada considerada no cálculo no passo 3 \(campo 06 \- SAFX08\)\.

__Número do Documento__

Número da Nota de entrada considerada no cálculo no passo 3 \(campo 09 \-SAFX08\)\.

__Série do Documento__

Série da Nota de entrada considerada no cálculo no passo 3 \(campo 10 \-SAFX08\)\.

__Subsérie do Documento__

Subsérie da Nota de entrada considerada no cálculo no passo 3 \(campo 11 \-SAFX08\)\.

__Pessoa Fis/Jur \(ind\-cod\)__

Indicador \+ \- \+ Código da Pessoa Fis/Jur da Nota de entrada considerada no cálculo no passo 3 \(campo 07 e 08 \-SAFX08\)\.

__Número do Item__

Número do item da Nota de entrada considerada no cálculo no passo 3 \(campo 18 \-SAFX08\)\.

__Medida do Produto__

Unidade de Medida do Cadastro do Produto \(campo 14 – SAFX2013\)

__Medida da Nota__

Unidade de Medida da Nota de entrada considerada no cálculo no passo 3 \(campo 25 \-SAFX08\)\.

__Quantidade Estoque__

Quantidade recuperada do inventário já convertida \(vide passo 1\)

__Quantidade da nota__

Quantidade da Nota de entrada recuperada no passo 3 \(campo 24 \-SAFX08\)\.

__Quantidade da nota Convertida \(1\)__

Quantidade da Nota de entrada recuperada no passo 3, convertida para unidade de medida do produto\.

__Quantidade da nota Utilizada \(2\)__

Quantidade da Nota de entrada utilizada para atingir a quantidade do estoque, conforme explicado no passo 3\.

__Valor do ICMS da nota \(3\)__

“*Valor ICMS da entrada*” conforme explicado no passo 3 em “__Considerações__”\.

__Valor do ICMS\-ST da nota \(sem fecep\) \(4\)__

*“Valor ICMS\-ST da entrada*” conforme explicado no passo 3 em “__Considerações__”\.

__Valor da Base ICMS\-ST da nota \(5\)__

*“Valor Base ICMS\-ST da entrada*” conforme explicado no passo 3 em “__Considerações__”\.

__Valor do FECEP\-ST da nota \(6\)__

“*Valor FECEP\-ST da entrada*” conforme explicado no passo 3 em “__Considerações__”\.

__Valor do ICMS Proporcional \(\(3\)/\(1\) \*\(2\)\)__

Conforme explicado no passo 3, é o valor do ICMS utilizado para cobrir a quantidade de estoque\.

__Valor do ICMS\-ST Proporcional \(\(4\)/\(1\) \*\(2\)\)__

Conforme explicado no passo 3, é o valor do ICMS\-ST utilizado para cobrir a quantidade de estoque\.

__Valor da Base ICMS\-ST Proporcional \(\(5\)/\(1\) \*\(2\)\)__

Conforme explicado no passo 3, é o valor da Base ICMS\-ST utilizado para cobrir a quantidade de estoque\.

__Valor da FECEP\-ST Proporcional \(\(6\)/\(1\) \*\(2\)\)__

Conforme explicado no passo 3, é o valor do FECEP\-ST utilizado para cobrir a quantidade de estoque\.

__Valor Médio Unitário do ICMS__

Valor Unitário Médio do ICMS calculado para o produto e gravado na __EST\_ST\_RS\_MEDIA\_POND__ com \(vide passo 4\)\.

__Valor Médio Unitário do ICMS\-ST s/ FECEP __

Valor Unitário Médio do ICMS\-ST sem Fecep calculado para o produto e gravado na __EST\_ST\_RS\_MEDIA\_POND__ com \(vide [passo 4](#_4º_Passo:_Gravar)\)\.

__Valor Médio Unitário do ICMS\-ST c/ FECEP __

Valor Unitário Médio do ICMS\-ST com Fecep calculado para o produto e gravado na __EST\_ST\_RS\_MEDIA\_POND__ com \(vide passo 4\)\.

__Valor Médio Unitário da Base de Cálculo do ICMS\-ST__

Valor Unitário Médio da Base do ICMS\-ST calculado para o produto e gravado na __EST\_ST\_RS\_MEDIA\_POND__ com \(vide passo 4\)\.

__Valor Médio Unitário do FECEP\-ST__

Valor Unitário Médio do FECEP\-ST calculado para o produto e gravado na __EST\_ST\_RS\_MEDIA\_POND__ com \(vide passo 4\)\.

![](data:image/x-emf;base64,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)

= = = = = =

 

