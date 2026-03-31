# MTZ-Job-Servidor-Importacao_SAFX233

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX233.docx
- **Modificado:** 2021-01-08
- **Tamanho:** 77 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX233

Tabela dos Bens p/ Cálculo dos Créditos Extemporâneos \(Integral\) do CIAP

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS3615

Créditos Extemporâneos de Bens com Prazo de Apropriação “normal” já Ultrapassado

Criação de nova tabela SAFX para carga dos Bens que terão todos os seus créditos calculados de forma extemporânea\. 

MFS4805

Novos campos

Criação de novos campos para tratamento dos Bens com baixa antes do término do período de apropriação\. Ver RN13 e RN14\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

Estrutura da tabela SAFX223 🡪 vide manual de layout

Campos que compõe a chave da tabela:

__   Código da Empresa \+ Código do Estabelecimento \+ Data da Apuração  \+ Código do Bem \+ Código do Incorporador__

A manutenção desta tabela é feita no Módulo CIAP, menu “Créditos Extemporâneos \(Integral\) 🡪 Manutenção dos Bens”, na aba “Informações do Bem”\.

Sobre as mensagens de erro:

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação do Bem \(campos chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

 

__RN01__

__Campo Código da Empresa__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação da Empresa serão desconsiderados\)*

__RN02__

__Campo Código do Estabelecimento__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento serão desconsiderados\)*

__RN03__

__Campo Data da Apuração__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, ou quando for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “Data da apuração não preenchida ou inválida”*

__RN04__

__Campo Código do Bem __

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        * *“O código do Bem é de preenchimento obrigatório”*

Crítica da existência do Bem na SAFX13:

Será verificada a existência do Bem informado \(Código do Bem \+ Código do Incorporador\) na Tabela dos Bens Patrimoniais \(SAFX13\), e caso não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

\(ao recuperar o Bem na SAFX13, considerar apenas os registros com data de validade < = data da apuração informada no campo 03\)

 

*                                             * *“Código do Bem não cadastrado ou inválido para a Data da Apuração”*

Crítica da existência do Bem na APT\_AQUISICAO:

Será verificado se o Bem informado \(Código do Bem e Código do Incorporador\) já existe na Tabela das Aquisições do CIAP \(APT\_AQUISICAO\), em nome da Empresa e Estabelecimento informados\. Caso sim, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                 * *“O Bem informado já consta no Cadastro Geral das Aquisições do CIAP”*

__RN05__

__Campo Código do Incorporador __

Campo de preenchimento __*não*__ __*obrigatório*__\.

Este campo compõe a chave da tabela, logo, quando não for informado, o campo será gravado com um caracter “branco” \(“ “\)

Obs: Todas as tabelas do Mastersaf que possuem o código do incorporador usam este mesmo procedimento, ou seja, quando não existe a informação do incorporador, o campo é sempre gravado com um caracter branco\.

__RN06__

__Campo Data da Ativação do Bem __

Campo de preenchimento __*obrigatório*__\.

Deve ser uma data válida, e de um mês que seja anterior à data da apuração \(informada no campo 03\)\.

Quando não preenchido, ou quando for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “Data da Ativação do Bem não preenchida ou inválida”*

Quando se tratar de uma data válida, mas de mês igual ou superior ao mês da data da apuração informada \(ou seja, não atenda a condição citada acima\), o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                     *

*                                    “A Data da Ativação do Bem deve ser de meses anteriores ao mês da apuração informada”*

Critica da Data da Ativação do Bem x Número de Parcelas x Data da Apuração:

O número de meses existente entre a data da ativação do Bem \(inclusive\) e a data da apuração \(inclusive\) deve ser no mínimo, igual ao número de parcelas \(informado no campo 12\) \+ 1\. Caso este número de meses seja inferior ao mínimo exigido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                  “Data da Ativação do Bem inconsistente em relação à data da apuração informada \(consultar orientações do help\)”*

Na prática esta regra significa que a última parcela a ser calculada para o Bem deve cair no máximo no mês anterior a data da apuração informada\. Não pode cair nem no mês da apuração, nem em meses posteriores\. 

Exemplo:

__Data Ativação__

__N\. de Parcelas__

__Data Apuração __

__Número de Meses Existentes __

__\(Ativação x Apuração\)__

__Número de Meses Mínimo Exigido__

__\(=N\.Parcelas \+ 1\)__

__Crítica__

01/01/2011

48

31/01/2014

__37__

49

Inválido

01/01/2011

48

31/01/2015

49

49

Ok

01/01/2011

48

31/01/2016

61

49

Ok

20/06/2012

48

31/05/2016

__48__

49

Inválido

20/06/2012

48

30/06/2016

49

49

Ok 

15/10/2012

24

30/09/2014

__24__

25

Inválido

15/10/2012

24

31/10/2014

25

25

Ok 

15/10/2012

24

31/03/2016

42

25

Ok 

__RN07__

__Campo Tipo da Movimentação __

Campo de preenchimento __*obrigatório*__\.

Este campo deve estar preenchido com uma das seguintes opções: “IM”, “IA”, “CI”, “MC”\.

Estes são os tipos de movimento de entrada aceitos no registro G125 do Sped Fiscal\. O “SI” não será aceito, pois é utilizado para Bens que já foram escriturados no CIAP em períodos anteriores \(ou seja, já foi informado no G125 de períodos anteriores\)\. 

Quando não preenchido, ou quando for diferente das opções acima, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “O tipo da movimentação deve ser = “IM”, “IA”, “CI”, “MC”*

__RN08__

__Campo Valor do ICMS __

Campo de preenchimento __*não*__ __*obrigatório*__\.

Crítica sobre o preenchimento dos valores:

Nenhum dos quatro campos de valor é de preenchimento obrigatório, no entanto, pelo menos um deles deve estar preenchido com um valor > zero\. Se nenhum deles atender a esta condição, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                        * *“Pelo menos um dos campos de valor do ICMS deve estar preenchido com um valor maior que zero”*

__RN09__

__Campo Valor do ICMS\- ST__

Campo de preenchimento __*não*__ __*obrigatório*__\.

__RN10__

__Campo Valor do ICMS \- Frete__

Campo de preenchimento __*não*__ __*obrigatório*__\.

__RN11__

__Campo Valor do ICMS – DIF__

Campo de preenchimento __*não*__ __*obrigatório*__\.

__RN12__

__Campo Número de Parcelas__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                            “Número de parcelas não preenchido”*

Crítica sobre o número informado:

Se o número informado for = 0 ou > 48, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

                         *“Número de parcelas inválido\. Deve ser um número diferente de zeros, e igual ou inferior a 48”*

__RN13__

<a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>

<a id="OLE_LINK32"></a><a id="OLE_LINK33"></a><a id="OLE_LINK34"></a>__Data da Baixa__                <a id="OLE_LINK20"></a><a id="OLE_LINK21"></a><a id="OLE_LINK22"></a>\(campo criado pela __MFS4805__\)

Campo de preenchimento __*não obrigatório*__\.

Quando preenchido, deve ser uma data válida\.

<a id="OLE_LINK23"></a><a id="OLE_LINK24"></a><a id="OLE_LINK25"></a>Quando a “*Data da Baixa*” for preenchida, e o campo “*Tipo de Movimentação da Baixa*” *não* for preenchido, <a id="OLE_LINK17"></a><a id="OLE_LINK18"></a><a id="OLE_LINK19"></a>o registro não será importado, e no log de erros será gravada a seguinte mensagem:

               *”Quando o campo Data da Baixa for preenchido, é obrigatório informar também o Tipo de Movimentação da Baixa”*

<a id="OLE_LINK74"></a><a id="OLE_LINK75"></a><a id="OLE_LINK76"></a>Crítica da Data da Baixa em relação a Data da Ativação do Bem e o mês da última parcela a ser calculada:

A data informada deve ser de um mês/ano superior ao mês/ano da Data da Ativação do Bem __e__ inferior ao mês/ano correspondente ao mês da última parcela a ser calculada\. Ou seja, deve ser uma data enquadrada no período entre, o mês seguinte a data da ativação do Bem, e o mês anterior ao da última parcela a ser calculada\.

Exemplo:

\- Data Ativação: Jan/2012

\- Número de Parcelas: 48

Neste exemplo, o mês da última parcela seria Dez/2015, considerando 48 parcelas mensais a serem calculadas a partir de Jan/2012\.

Desta forma, pela regra descrita acima, o mês/ano da Data da Baixa deveria se enquadrar no seguinte intervalo: Fev/2012 a Nov/2015\.  

Quando esta condição não for atendida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: *”Data da Baixa inválida em relação à Data da Ativação do Bem ou ao Número de Parcelas\. Consultar as orientações do Manual de Layout”*

__RN14__

__Tipo de Movimentação da Baixa              __\(campo criado pela __MFS4805__\)

Campo de preenchimento __*não obrigatório*__\.

Quando preenchido, o conteúdo deve ser uma das seguintes opções: “AT”, “PE” ou “OT”\.

Obs: o tipo “BA” \(baixa por término do período de apropriação\) não é tratado neste campo, pois nesse caso trata\-se apenas de baixas realizadas antes do término do período de apropriação\.  

Quando for preenchido com conteúdo diferente das três opções descritas acima, o registro não será importado, e no log de erros será gravada a seguinte mensagem: 

 <a id="OLE_LINK43"></a><a id="OLE_LINK44"></a><a id="OLE_LINK45"></a>                                           *“O tipo da movimentação da baixa deve ser = “AT”, “PE” ou “OT”*

<a id="OLE_LINK62"></a><a id="OLE_LINK63"></a><a id="OLE_LINK64"></a>Quando o “*Tipo de Movimentação da Baixa*” for preenchido, e o campo “Data da Baixa” *não* for preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

               *”Quando o campo Tipo de Movimentação da Baixa for preenchido, é obrigatório informar também a Data da Baixa”*

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

