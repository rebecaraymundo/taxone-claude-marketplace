# MTZ-PIM-Relatorio_Valores_ICMS_Difal_EC87_por_IE

- **Fonte:** MTZ-PIM-Relatorio_Valores_ICMS_Difal_EC87_por_IE.docx
- **Modificado:** 2022-05-12
- **Tamanho:** 77 KB

---

THOMSON REUTERS

Módulo Report Fiscal – Relatório dos Valores do ICMS Dif\. Aliq\. da EC 87/2015 

__Localização__: Menu Específicos, Módulo: PIM – Gestão do Controle de Incentivos Fiscais do Polo Industrial de Manaus, menu Relatórios 🡪 Relatório dos Valores do ICMS Dif Aliq da EC 87/2015

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS4423

Eric Celestrino

Criação de Relatório dos Valores do ICMS Dif Aliq da EC 87/2015 

Sumário

[1\.	REGRAS DE GERAÇÃO DO RELATÓRIO	3](#_Toc451861191)

[1\.1\.	Layout do Relatório	6](#_Toc451861192)

# <a id="_Toc451861191"></a>REGRAS DE GERAÇÃO DO RELATÓRIO 

__Origem das Informações para Geração__: Tabela dos Documentos Fiscais de Mercadoria – Capa \(SAFX07\)

                                			    Tabela dos Documentos Fiscais de Mercadoria – Itens \(SAFX08\)

  

Para cada estabelecimento/ inscrição estadual selecionado em tela será gerado um relatório\. 

As regras descritas a seguir se referem ao processamento de cada estabelecimento/ inscrição estadual:

Serão recuperadas todas as notas fiscais das operações interestaduais, tanto entradas como saídas, que tenham ao menos algum destes campos preenchidos\.

__Nas notas sem itens \(SAFX07\)__

__Nas notas com itens \(SAFX08\)__

   283\-Valor FCP UF Destino

   221\-Valor FCP UF Destino

   284\-Valor ICMS UF Destino

   222\-Valor ICMS UF Destino

   285\-Valor ICMS UF Origem

   223\-Valor ICMS UF Origem

__Regra de Seleção__:

   \- Empresa – empresa do login;

   \- Estabelecimento – estabelecimento/ inscrição estadual selecionado para emissão do relatório;

   \- Data da nota – notas com data fiscal enquadrada no período informado, *ou*, notas com data extemporânea enquadrada no período;

   \- Classificação – notas de classificação 1, 3 ou 4 \(nota de mercadoria, nota mista, ou transporte\);

   \- CFOP – apenas as operações interestaduais \(CFOP’s iniciados por “2” ou “6”\);

__   \- Inscrição Estadual \(campo 126 da SAFX07\) – inscrição estadual da apuração;__

   \- Somente notas *não* canceladas;

   \- Serão consideradas apenas as notas / itens que tenham ao menos um dos campos acima preenchidos;

   \- De acordo com o parâmetro de tela “__Tipo de Movimento__”:

  

        \- Se “Tipo de Movimento” = “Entrada” 🡪 serão consideradas apenas as notas de entrada;

        \- Se “Tipo de Movimento” = “Saídas” 🡪 serão consideradas apenas as notas de saída;

        \- Se “Tipo de Movimento” = “Entradas e Saídas” 🡪 serão consideradas tanto as notas de entrada como de saída;

   \- De acordo com o parâmetro de tela “__UF Origem/Destino__”:

         Se “UF Origem/Destino” = “Todas”

               Nesse caso serão consideradas todas as notas de acordo com os critérios acima;

               \(mesmo quando os campos de UF Origem e UF Destino da nota *não* estiverem preenchidos\)

*                Obs: Na geração da Apuração do Difal estas notas sem UF não são consideradas, mas no relatório elas serão demonstradas,*

*                justamente para que o usuário possa visualizá\-las e verificar o problema\. *

         Senão 

               Nesse caso serão consideradas apenas as notas cuja UF origem/destino da capa seja igual a UF informada em tela 

               \(parâmetro “__UF Origem/Destino__”\), da seguinte forma:

               \- Nas *entradas*, a nota será considerada apenas se o campo *UF Origem* for = “UF Origem/Destino” informada em tela; 

               \- Nas *saídas*, a nota será considerada apenas se o campo *UF Destino* for = “UF Origem/Destino” informada em tela; 

__\(a UF de origem da nota é o campo “117\-UF Origem” e a UF de destino é o campo “122\-UF Destino” da SAFX07\)__

__Regra de agrupamento / Ordenação:__

As notas recuperadas para cada estabelecimento serão agrupadas separadamente por entradas e saídas, pois de acordo com o layout, primeiro serão demonstradas as operações de entrada, e depois as saídas\.

Cada grupo de notas \(entradas / saídas\) será ordenado por:

     \- Conteúdo da coluna “Data fiscal” \(data fiscal ou data extemporânea da nota, conforme o caso\);

     \- Conteúdo da coluna “Nota Fiscal” \(número e série da nota\);

     \- Conteúdo da coluna “Pessoa Fis/Jur” \(indicador e código da pessoa fis/jur\);

O relatório irá demonstrar primeiro as notas de entradas, da seguinte forma:

     \- Relação de todas as notas de entrada na ordenação descrita acima, sendo uma linha para cada item;

     \- Ao final de todas as notas de entrada, será demonstrada a linha do total geral das entradas \(totalização das colunas\);

     \- Após a linha do total geral das entradas, será exibido um resumo com a totalização das entradas por UF de origem e destino da operação __\(\*\)__; 

A seguir, será feito o mesmo processo para as notas de saída:

     \- Relação de todas as notas de saída na ordenação descrita acima, sendo uma linha para cada item;

     \- Ao final de todas as notas de saída, será demonstrada a linha do total geral das saídas \(totalização das colunas\);

     \- Após a linha do total geral das saídas, será exibido um resumo com a totalização das saídas por UF de origem e destino da operação __\(\*\)__; 

__\(\*\)__ A totalização das notas para os resumos *não* é simplesmente a totalização das colunas do relatório\. A regra para geração destes resumos será descrita no item 4\.

Caso o usuário tenha optado por listar apenas as entradas ou apenas as saídas \(parâmetro “Tipo de Movimento”\), *um destes processos não será executado*, e o relatório irá demonstrar apenas as notas de entrada, ou apenas as notas de saída, conforme o caso\. 

## <a id="_Toc451861192"></a>Layout do Relatório

__Linhas de cabeçalho:__

Primeira linha do cabeçalho

A primeira linha do cabeçalho demonstra a razão social da empresa, a data de emissão do relatório e o número da página\.

Segunda linha do cabeçalho

Campo “Filial” = será preenchido com o código e a razão social do estabelecimento em questão\.

Campo “Inscrição Estadual” = será preenchido com a inscrição estadual do estabelecimento em questão \(inscrição na sua própria UF\)\.

Campo “CNPJ” = será preenchido com o CNPJ do estabelecimento em questão\.

Terceira linha do cabeçalho

Nesta linha será exibido o título do relatório, e o período solicitado em tela para a sua emissão:

                  “Relatório dos Valores do ICMS Dif Aliq da EC 87/2015 – Período: 99/99/9999 a 99/99/9999”

__Linha de subtítulo das notas fiscais de entrada e das notas fiscais de saída:__

Linha do subtítulo das Entradas

Esta linha é um subtítulo que identifica que serão exibidas a seguir as notas fiscais de entrada\. Conforme mostrado na planilha de layout, o seu conteúdo é apenas: 

                                                         “Documentos de Entrada”

Linha do subtítulo das Saídas

Esta linha é um subtítulo que identifica que serão exibidas a seguir as notas fiscais de saída\. Conforme mostrado na planilha de layout, o seu conteúdo é apenas: 

                                                         “Documentos de Saída”

__Linhas do detalhamento das notas fiscais:__

OBS: As linhas do detalhamento das notas são iguais para as entradas e saídas, exceto pelo titulo e conteúdo da coluna UF \(conforme detalhado a seguir\)\. 

Data Fiscal

Data fiscal da nota

Emissão

Data de emissão da nota

Nota Fiscal

Número e série da nota fiscal, no formato: XXXXXXXXXXXX / XXX

Pessoa Fis/Jur

Indicador e código da pessoa fis/jur da nota fiscal, no formato: X\-XXXXXXXXXXXX 

N\. Item

Número do item da nota fiscal

No caso das notas sem item, esta coluna ficará em branco

CFOP

CFOP do item da nota fiscal

No caso das notas sem item, será utilizado o CFOP da capa

Produto

Indicador e código do produto do item da nota fiscal, no formato: X\-XXXXXXXXXXXXXXXXXXXXXXXX

No caso das notas sem item, esta coluna ficará em branco

Valor do Item

Valor do item da nota fiscal \(campo “Valor do Item”\)

 No caso das notas sem item, esta coluna ficará em branco

Qtd

Quantidade do item da nota fiscal \(campo “Quantidade”\)

 No caso das notas sem item, esta coluna ficará em branco

Valor Contábil

Valor contábil do item da nota fiscal \(campo “Valor Contábil”\)

No caso das notas sem item, será utilizado o valor total da capa da  nota 

UF Origem \(NF\) 

__ou__

UF Destino \(NF\)

No cabeçalho referente às notas fiscais de __entrada__, esta coluna tem o título: “__UF Origem \(NF\)__”\.

No cabeçalho referente às notas fiscais de __saída__, esta coluna tem o título: “__UF Destino \(NF\)__”\.

Conteúdo da coluna:

Se nota de entrada 🡪 sigla da UF informada no campo “117\-UF Origem” da SAFX07;

Se nota de saída 🡪 sigla da UF informada no campo “122\-UF Destino” da SAFX07;

ICMS Origem

Valor do campo “223\-Valor ICMS UF Origem” do item da nota

No caso das notas sem itens, será utilizado o valor da capa \(campo “285\-Valor ICMS UF Origem”\)

 

Quando o conteúdo do campo for zeros ou nulo, a coluna do relatório ficará em branco\. 

ICMS Destino

Valor do campo “222\-Valor ICMS UF Destino”

No caso das notas sem itens, será utilizado o valor da capa \(campo “284\-Valor ICMS UF Destino”\)

Quando o conteúdo do campo for zeros ou nulo, a coluna do relatório ficará em branco\.

FCP Destino

Valor do campo “221\-Valor FCP UF Destino”

No caso das notas sem itens, será utilizado o valor da capa \(campo “283\-Valor FCP UF Destino”\)

Quando o conteúdo do campo for zeros ou nulo, a coluna do relatório ficará em branco\.

__Linha do total geral das entradas:__

Total Geral das Entradas

Esta linha será demonstrada ao final de todas as notas de __entrada__ do estabelecimento em questão\.

Seu conteúdo será a totalização das três colunas dos valores do diferencial de alíquota:

 \- ICMS Origem

 \- ICMS Destino

 \- FCP Origem

  

__Linha do total geral das saídas:__

Total Geral das Saídas

Esta linha será demonstrada ao final de todas as notas de __saída__ do estabelecimento em questão\.

Seu conteúdo será a totalização das três colunas dos valores do diferencial de alíquota:

 \- ICMS Origem

 \- ICMS Destino

 \- FCP Origem

__Linhas do resumo “Total das Entradas por UF Origem/Destino”:	__

Este resumo será gerado ao final da listagem de todas as notas de entrada, conforme demonstra a planilha do layout\.

Será gerada uma linha para cada UF de origem demonstrada na coluna “UF Origem \(NF\)”, e uma linha para a UF do próprio estabelecimento da emissão do relatório\.

*\(no caso das entradas, a UF do estabelecimento é a UF de destino da operação\)*

Caso existam notas *sem* a informação da UF de origem no relatório, será gerada uma linha com a coluna UF = “??”\. Nestes casos, os valores referentes a estas notas serão totalizados nesta linha\.

Segue regra de preenchimento dos valores para cada UF demonstrada:

UF

Sigla da UF de origem / destino da operação, para a qual o crédito será totalizado\.

O quadro mostrará uma linha __para cada UF__, considerando:

\- Uma linha para cada UF de origem demonstrada na coluna “UF Origem \(NF\)”;

\- Uma linha para a UF do próprio Estabelecimento da emissão do relatório;

Quando existir alguma nota *sem* a informação da UF Origem \(coluna “UF Origem” = brancos\), os valores destas notas serão totalizados, e para que eles sejam demonstrados no resumo, será gerada uma linha com a coluna UF = “??”\.

*\(ver exemplos na planilha de layout do relatório, aba “Exemplo” e “Exemplo com nf sem UF preenchida”\)*

Crédito

O valor desta coluna representa o crédito a ser lançado para a UF na Apuração do ICMS do Difal \(EC87/15\)\.

O seu conteúdo dependerá da UF demonstrada, da seguinte forma:

Na linha da UF do Estabelecimento:

     \- O conteúdo desta coluna será o total geral da coluna “__ICMS Destino__” de todas as notas de entrada exibidas;

       \(corresponde ao total da coluna “ICMS Destino” da linha “Total Geral das Entradas”\);

     \- Se este total for = zeros, a coluna ficará em branco;

Nas linhas das UF’s de Origem:

     \- O conteúdo desta coluna será o total dos valores da coluna “__ICMS Origem__” de todas as linhas da UF;

     \- Se o total apurado for = zeros, a coluna ficará em branco;

Na linha de UF = “??”:

     \- O conteúdo desta coluna será o total dos valores da coluna “__ICMS Origem__” de todas as linhas SEM a informação da UF

       de Origem;

Conforme descrito na regra da coluna “UF”, *esta linha só existirá caso existam notas sem a informação da UF *na coluna “UF Origem \(NF\)”\. Neste caso os valores serão totalizados numa única linha, representada como UF = “??”\.

Crédito FCP

O valor desta coluna representa o crédito do FCP a ser lançado para a UF na Apuração do ICMS do Difal \(EC87/15\)\.

O seu conteúdo dependerá da UF demonstrada, da seguinte forma:

Na linha da UF do Estabelecimento:

     \- O conteúdo desta coluna não será preenchido \(a coluna ficará em branco\);

Nas linhas das UF’s de Origem:

     \- O conteúdo desta coluna será o total dos valores da coluna “__FCP Destino__” de todas as linhas da UF;

     \- Se o total apurado for = zeros, a coluna ficará em branco;

Na linha de UF = “??”:

     \- O conteúdo desta coluna será o total dos valores da coluna “__FCP Destino__” de todas as linhas SEM a informação da UF

       de Origem;

Conforme descrito na regra da coluna “UF”, *esta linha só existirá caso existam notas sem a informação da UF *na coluna “UF Origem \(NF\)”\. Neste caso os valores serão totalizados numa única linha, representada como UF = “??”\.

__Linhas do resumo “Total das Saídas por UF Origem/Destino”:__

Este resumo será gerado ao final da listagem de todas as notas de saída, conforme demonstra a planilha do layout\.

Será gerada uma linha para cada UF de destino demonstrada na coluna “UF Destino \(NF\)”, e uma linha para a UF do próprio estabelecimento da emissão do relatório\.

*\(no caso das saídas, a UF do estabelecimento é a UF de origem da operação\)*

Caso existam notas *sem* a informação da UF de destino no relatório, será gerada uma linha com a coluna UF = “??”\. Nestes casos, os valores referentes à estas notas serão totalizados nesta linha\.

Segue regra de preenchimento dos valores para cada UF demonstrada:

UF

Sigla da UF de origem / destino da operação, para a qual o débito será totalizado\.

O quadro mostrará uma linha __para cada UF__, considerando:

\- Uma linha para cada UF de destino demonstrada na coluna “UF Destino \(NF\)”;

\- Uma linha para a UF do próprio Estabelecimento da emissão do relatório;

Quando existir alguma nota *sem* a informação da UF Destino \(coluna “UF Destino” = brancos\), os valores destas notas serão totalizados, e para que eles sejam demonstrados no resumo, será gerada uma linha com a coluna UF = “??”\.

*\(ver exemplos na planilha de layout do relatório, aba “Exemplo” e “Exemplo com nf sem UF preenchida”\)*

Débito

O valor desta coluna representa o débito a ser lançado para a UF na Apuração do ICMS do Difal \(EC87/15\)\.

O seu conteúdo dependerá da UF demonstrada, da seguinte forma:

Na linha da UF do Estabelecimento:

     \- O conteúdo desta coluna será o total geral da coluna “__ICMS Origem__” de todas as notas de saída exibidas;

       \(corresponde ao total da coluna “ICMS Origem” da linha “Total Geral das Saídas”\);

     \- Se este total for = zeros, a coluna ficará em branco;

Nas linhas das UF’s de Destino:

     \- O conteúdo desta coluna será o total dos valores da coluna “__ICMS Destino__” de todas as linhas da UF;

     \- Se o total apurado for = zeros, a coluna ficará em branco;

Na linha de UF = “??”:

     \- O conteúdo desta coluna será o total dos valores da coluna “__ICMS Destino__” de todas as linhas SEM a informação da UF

       de destino;

Conforme descrito na regra da coluna “UF”, *esta linha só existirá caso existam notas sem a informação da UF *na coluna “UF Destino \(NF\)”\. Neste caso os valores serão totalizados numa única linha, representada como UF = “??”\.

Débito FCP

O valor desta coluna representa o débito do FCP a ser lançado para a UF na Apuração do ICMS do Difal \(EC87/15\)\.

O seu conteúdo dependerá da UF demonstrada, da seguinte forma:

Na linha da UF do Estabelecimento:

     \- O conteúdo desta coluna não será preenchido \(a coluna ficará em branco\);

Nas linhas das UF’s de Destino:

     \- O conteúdo desta coluna será o total dos valores da coluna “__FCP Destino__” de todas as linhas da UF;

     \- Se o total apurado for = zeros, a coluna ficará em branco;

Na linha de UF = “??”:

     \- O conteúdo desta coluna será o total dos valores da coluna “__FCP Destino__” de todas as linhas SEM a informação da UF

       de destino;

Conforme descrito na regra da coluna “UF”, *esta linha só existirá caso existam notas sem a informação da UF *na coluna “UF Destino \(NF\)”\. Neste caso os valores serão totalizados numa única linha, representada como UF = “??”\.

Sugestão de leiaute:

Vide Layout\_Relatorio\_dos\_Valores\_do\_Difal\_EC87\_por\_IE\.xlsx

