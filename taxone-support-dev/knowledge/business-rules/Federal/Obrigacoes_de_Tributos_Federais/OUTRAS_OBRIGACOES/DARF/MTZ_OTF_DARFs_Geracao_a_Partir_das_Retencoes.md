# MTZ_OTF_DARFs_Geracao_a_Partir_das_Retencoes

- **Fonte:** MTZ_OTF_DARFs_Geracao_a_Partir_das_Retencoes.docx
- **Modificado:** 2022-02-02
- **Tamanho:** 77 KB

---

THOMSON REUTERS

DARF’s / Geração – A partir das Retenções

Obrigações de Tributos Federais

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS2821

Marcelo Pessanha

Alteração das Rotinas de DARF para divisão destes pagamentos de acordo com a divisão em quotas de DCTF\.

OS3160

Marcos Roberto de Oliveira

Somente gerar DARF’s quando os valores das Retenções e Retificações forem iguais ou maiores que R$ 10,00\.

OS3509

Marcos Roberto de Oliveira

Gerar DARF’s com 2 ou 3 quotas\.

OS4428

Julyana Perrucini

Reversa do parâmetro “Gerar Observações Automaticamente”\.

CH13117\_2015

Lara Aline

Inclusão de regra para ajustar a geração da data de vencimento dos DARF´s, considerando apenas os dias úteis\.

CH25028\_2015

Lara Aline

Alteração na regra para ajustar a geração da data de vencimento dos DARF´s, considerando apenas os dias úteis como válido para data de vencimento\. Para todos os números de dias \(Corridos antecipados, Corridos postergados e Úteis\)\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

*RN00*

*Reservada para Regra Geral\.*

<OS>\.

RN01

No tratamento de exclusão dos registros, deveremos observar as seguintes regras:

1\) Para os registros que possuem quotas, estes não poderão ser excluídos um a um, ou seja, quando um registro for identificado que possui quotas, este deverá ser excluído juntamente com as demais quotas calculadas no sistema;

2\) Antes da exclusão do registro, se o registro não está com o Status de Pago, o sistema deverá exibir a seguinte mensagem: “Os Tributos relacionados a este DARF serão desconsiderados da Situação=Gerado, se este é um DARF referente a uma parte da divisão em quotas dos Tributos todas as quotas serão excluídas, havendo a necessidade de reprocessar rotina \(Geração de DARF a partir da Retenção\)\. '

Deseja continuar a exclusão?”\. Se o usuário confirmar a operação de exclusão, o sistema deverá verificar se o registro é ou não parte de uma divisão de quotas e caso seja, deverá verificar se existe alguma parcela já paga\. Caso não exista, promover a exclusão de todas as parcelas, caso contrário, tratar conforme abaixo;

3\) Se o registro estiver com o Status de Pago, o sistema deverá exibir a seguinte mensagem: “DARF com Status = Pago, ou parte da divisão em quotas dos Tributos consta como paga, e portanto não pode ser excluído\.” E deverá retornar a tela sem efetuar a exclusão\.

OS2821

RN02

A operação de salvamento das informações deverá seguir as regras abaixo:

1. Para os registros que não possuam divisão em quotas, deverão ser tratados conforme atualmente;

2\) Para os registros que possuam divisão em quotas, quando forem informados os campos de \(Envio bancário e/ou Autenticação Bancária\), deverá ser verificado se existe ainda outras quotas não pagas, caso exista, atualizar apenas as informações da determinada quota, caso contrário, atualizar a tabela de retenções com a informação de Pago, além de atualizar a própria quota;

OS2821

RN03

Deveremos considerar o novo campo de quotas na recuperação das informações, ou seja, garantir que a demonstração da informação no relatório seja de acordo com a informação constante em tela, evitando o aparecimento de diversos registros relativo às quotas\.

OS2821

RN04

A funcionalidade do REDARF deverá levar em consideração a criação do novo campo de Quotas criado para os DARF´s, visto que o REDARF hoje é uma funcionalidade de cadastro que é dependente de um DARF\.

OS2821

RN05

Deveremos criar o campo denominado Quota como numérico inteiro de 2 posições\. Este campo deverá estar disposto tanto em tela quanto no relatório de tela ao lado do campo já existente “Número de Referência”\.

Este campo deverá estar sempre desabilitado para manutenção do usuário ele será apenas informativo\.

OS2821

RN06

Deveremos incluir a informação de Quota proveniente do DARF no cadastro do REDARF, esta informação deverá acompanhar o modelo dos demais campos já existentes, ou seja, não permitir a manutenção deste campo\.

Este campo deverá ser numérico inteiro de 2 posições\.

OS2821

RN07

Deveremos incluir novo campo na parte “Para” da tela a fim de acompanhar o modelo já existente\. Este campo será referente à quota, deverá ser numérico de 2 posições e habilitado para alteração\. Poderá receber o valor zero para indicação de não possuir quota\. 

OS2821

RN08

Deveremos considerar os dois novos campos no relatório, estes deverão estar dispostos do mesmo jeito como na tela de manutenção\.

OS2821

RN09

Deveremos criar a dois novos campos de período a fim de proporcionar maior facilidade ao usuário de visualização de apenas uma DARF relativo à quota com vencimento dentro deste período, ou seja, além do período considerado atualmente que é o de apuração, deveremos considerar também quando informado a data de vencimento\.

Vale ressaltar que este novo parâmetro terá impacto apenas para os DARF´s que possuem informação no novo campo de quotas maior que zero, caso contrário, o sistema somente considerará o período de apuração\.

OS2821

RN10

__\[ALTERADA – OS3509\] __A geração deverá se comportar da seguinte forma:

1. Caso o novo parâmetro de *“Divisão de DARF´s em Quotas\(DCTF\)”* estiver marcado, a geração deverá verificar se a data de competência da retenção é uma das seguintes: se o grupo de tributos seja igual a 01\-IRPJ ou 05 \- CSLL  e os Códigos de Receita possuam a periodicidade igual a Trimestral, caso uma dessas regras não for obedecida, o tributo não será dividido em quotas e o tratamento seguirá conforme atualmente ;
2. Quanto ao valor do débito dos tributos, para os casos de divisão por quotas deverão obedecer os seguintes critérios:

Se valor < 2000,00, não parcelar em quotas;

Se valor entre 2000,00 e 2999,99, parcelar em 2 quotas;

Se valor for igual ou maior a 3000,00, parcelar em 3 quotas; 

1. Para dividir o valor do DARF em quotas o sistema deverá utilizar das regras citadas nos passos anteriores\. Porém ao processar o DARF o sistema deverá verificar a informação do Código DARF na parametrização de “Divisão do DARF em Quotas” no menu Outras Obrigações >> DARF’s >> Divisão do DARF em Quotas\. Seguem os exemplos para processamento:

__Exemplo 1__ – Caso o DARF possua valor < 2000,00 o sistema não irá verificar o campo “Qtde\. Quotas” da parametrização de “Divisão do DARF em Quotas” e irá dividir o DARF em Quota única\.

__Exemplo 2__ \- Caso o DARF possua valor entre 2000,00 e 2999,99 o sistema irá verificar o campo “Qtde\. Quotas” da parametrização de “Divisão do DARF em Quotas”\. Caso o valor seja “2”, o DARF será dividido em duas quotas\. Caso o valor seja “3”, o sistema irá dividir o DARF em duas quotas e não em 3 conforme parametrização, pois o valor mínimo da quota é R$ 1\.000,00\.

__Exemplo 3__ – Caso o DARF possua valor >= 3000,00 o sistema irá verificar o campo “Qtde\. Quotas” da parametrização de “Divisão do DARF em Quotas”\. Caso o valor seja “2”, o DARF será dividido em duas quotas\. Caso o valor seja “3”, o sistema irá dividir o DARF em três quotas\.

Caso o Código DARF não esteja com nenhum valor para a Quantidade de Quotas, o sistema irá adotar a regra citada no passo 2\. __OBS:__ caso o cliente gere o DARF por Empresa, será recuperada a parametrização de DARF em Quotas do Estabelecimento Matriz da Empresa informada\. Caso essa parametrização não exista, o sistema deverá gerar o DARF conforme o passo 2\.

1. Para as quotas geradas nos meses subseqüentes, estas deverão conter o valor do débito parcelado acrescido de juros e multa, tomando como base a data de apuração\.

Ex\.: Valor do Débito: 6000,00 \(Divisão em 3 quotas\) com competência em 31/03/2009: 1ª Quota Vencto em : 31/04/2009; 2ª Quota Vencto em: 31/05/2009 e 3ª Quota Vencto em: 30/06/2009\.

        Primeira quota com vencimento igual ao vencimento da retenção:  2\.000,00 

        Segunda quota com vencimento no final do mês subseqüente a competência da retenção: 2\.000,00 \+ Juros do  período \(onde o período é a partir de da data de vencimento da 1ª quota até a data do vencimento da segunda quota\)

        Terceira quota com vencimento no final do mês subseqüente a segunda quota: 2\.000,00 \+ Juros do  período \(onde o período é a partir de da data de vencimento da 1ª quota até a data do vencimento da terceira quota\);

1. O indicador da quota deverá ser guardado no DARF através do novo campo Quota, a gravação na Retenção das informações do DARF bem como o controle de pagamento deverão continuar os mesmos, ou seja, deveremos considerar o identificador do DARF e o Número de Controle para validação da Situação da Retenção\.

Atenção: deveremos considerar que a partir de agora podemos ter a divisão em quotas ou seja mais de uma ocorrência de DARF para um conjunto consolidado de Retenções\. Antes de proceder quaisquer alterações da situação, deveremos verificar se o DARF possui divisão por quotas ou não através do novo campo quota, quando ele estiver zerado, não possui divisão por quota, caso contrário possuirá\.

1. Caso o usuário tenha marcado a opção de cálculo de Juros e Multa, a quota que receberá os juros e multa será a 1ª   quota, ou seja para o exemplo dado anteriormente, a 1ª quota possuirá o vencimento da retenção \+ Juros do período  \(vencimento da quota até data prevista do pagamento\); As demais quotas deverão ser calculadas normalmente conforme o exemplo anterior\.

OS2821

OS3509

RN11

A geração deverá se comportar da seguinte forma:

1. Caso a nova opção “Data de Vencimento do DARF\(apenas para cálculo de Juros/Multa de DARF dividido em Quotas\)” do parâmetro “Gerar DARF por” estiver selecionado, deveremos considerar os DARF´s com divisão em quotas cujo vencimento tenha ocorrido no período selecionado\.
2. Se na hora do cálculo, o registro for pertinente a um DARF dividido em quotas, deveremos levar em consideração como data base para o cálculo dos juros/multa a data de vencimento da 1ª quota e não a data de vencimento conforme hoje em dia\. 

Ex\.: Valor do Débito: 6000,00 \(Divisão em 3 quotas\) com competência em 31/03/2009: 1ª Quota Vencto em : 31/04/2009; 2ª Quota Vencto em: 31/05/2009 e 3ª Quota Vencto em: 30/06/2009\.

Gerar DARF por: Data de Vencimento do DARF\(apenas para cálculo de Juros/Multa de DARF dividido em Quotas\)

Período de 01/05/2009 a 31/05/2009

Data prevista para pagamento: 06/06/2009

Neste caso apenas a segunda quota se enquadra nesta seleção, então para o cálculo de Juros/ Multa desta quota será:

Segunda quota com vencimento no final do mês subseqüente a competência da retenção: 2\.000,00 \+ Juros do  período \(onde o período é a partir de da data de vencimento da 1ª quota até a data prevista de pagamento\);

ATENÇÃO: NÃO SE ESQUECER DE ATUALIZAR OS CAMPOS DE BANCO E AGENCIA TAMBÉM\.

OS2821

RN12

Deverá ser criado na tela de Parâmetros por DARF/GPS um novo campo chamado “Controle de Retenção Mínima de DARF”\. Esse campo deverá ser criado após os parâmetros “Multa Diária” e “Limite de Multa”\.

Esse campo deverá ser um campo do tipo numérico, contendo 17 posições, sendo 15 inteiras e 2 decimais\.

Por default esse campo irá exibir o valor “10,00” e poderá ser editável\.

OS3160

RN13

Deverá ser criado o campo “Situação Controle Mínimo de Retenção”\. Esse campo deverá ser criado na tela de Controle de Tributos tanto para a aba “Retenção” \(X53\_RETENCAO\_IRRF\) quanto para a aba “Retificações” \(X530\_RETIFICACAO\_IRRF\)\.

Esse campo é de controle do produto para o controle de retenção mínima para recolhimento de um DARF\. Esse campo só será criado nas tabelas definitivas do sistema – X53\_RETENCAO\_IRRF e X530\_RETIFICACAO\_IRRF – e não será criado nas tabelas temporárias para importação da SAFX53\. Logo, as rotinas referentes à Carga, Importação Manual, Importação Batch e Exportação do Job Servidor não serão impactadas\.

Esse campo deverá ficar abaixo do campo “Situação DARF Complementar/Compensação Crédito”\.

OS3160

RN14

O campo “Situação Controle Mínimo de Retenção” só deverá ser exibido para as retenções/retificações que forem consideradas no Controle de Retenção Mínima, ou seja, as retenções/retificações que durante o processo de geração dos DARF’s não atingirem o valor mínimo informado no campo “Controle de Retenção Mínima de DARF” da tela de Parâmetros por DARF/GPS \(hoje 10,00\)\.

As retenções/retificações que não forem consideradas nesse controle, não terão o campo exibido para o registro que estiver sendo consultado \(via tela Controle de Tributos do DW\)\.

OS3160

RN15

Ao gerar os DARF’s, serão recuperadas as retenções da X53\_RETENCAO\_IRRF cujo campo Situação DARF = Não Gerado e que estejam dentro do período informado no período de geração OU as retificações da X530\_RETIFICACAO\_IRRF mais atual cujo campo Situação DARF = Não Gerado\. Para que essas retificações sejam recuperadas a retenção “pai” dessa retificação existente na X53\_RETENCAO\_IRRF deverá estar com o campo Situação DARF = Pago\.

O usuário poderá gerar os DARF’s de acordo com o critério de consolidação escolhido\. Os critérios são:

- Código de Retenção
- Código de Retenção/Data de Vencimento
- Código de Retenção/Data de Vencimento/Receita
- Código de Retenção/Código de Operação/Data de Vencimento/Receita

Caso pelo critério de consolidação informado o valor seja menor do que o valor informado no campo “Controle de Retenção Mínima de DARF” da tela Parâmetros por DARF/GPS, a retenção ou retificação deverá continuar com o campo Situação DARF = Não Gerado e o campo “Situação Controle Mínimo de Retenção” deverá ser considerado como gerado, assim sendo exibido para a retenção ou retificação que estiver sendo consultada via tela\. Os valores dessa retenção ou retificação __não serão gerados em nenhum DARF__, pois a mesma não atingiu o valor mínimo informado no parâmetro que hoje é de R$ 10,00\.

OS3160

RN16

Caso em um período de apuração subseqüente, a rotina para geração dos DARF’s seja executada, a regra de geração é igual à regra RN36 acrescentada de que o sistema irá recuperar as retenções e retificações de períodos anteriores, respeitando sempre o critério de Tipo de Data selecionado \(Data de Movimento, Data do Fato Gerador, Data Inicial e Final de Competência e Data de Vencimento do DARF\) cujo campo Situação DARF = Não Gerado e campo “Situação Controle Mínimo de Retenção” estejam gerados\.

Caso o somatório das retenções do período de apuração atual com as retenções antigas que estavam com o campo Situação DARF = Não Gerado e campo “Situação Controle Mínimo de Retenção” gerado forem iguais ou superiores ao valor mínimo informado no campo “Controle de Retenção Mínima de DARF”, será gerado um DARF na tabela X75\_DCTF\. As retificações que atingiram o valor mínimo, nesse caso, serão geradas na X751\_DCTF\_COMPL\.

As retenções do período de apuração atual passam a ficar com o campo Status = Gerado/Não Pago e o campo “Situação Controle Mínimo de Retenção” fica como não gerado, pois essas retenções nunca fizeram parte do Controle de Retenção Mínima\. 

As retenções e as retificações do período de apuração anterior que antes estavam com o campo Status = Não Gerado passam a ficar com o campo Status = Gerado/Não Pago e com o campo “Situação Controle Mínimo de Retenção” continua como Gerado\. Essas retenções antes faziam parte do Controle de Retenção Mínima e agora não fazem mais parte desse controle\.

Uma retenção ou retificação que uma vez faça parte do Controle Mínimo de Retenção sempre possuirá esse status \(marca\) e esse status nunca irá mudar\.

Deverão ser recalculadas as datas de vencimento para as retenções/retificações que possuem o campo “Situação Controle Mínimo de Retenção” gerado\. A data que será inserida nessas retenções/retificações será de acordo com o Tributo informado nessa retenção/retificação e também de acordo com a parametrização de Tributos – Especificações\. Caso essa retenção possua um Tributo associado que não esteja parametrizado, no momento do processo de geração dos DARF’s será exibido um WARNING na geração e essa retenção será desconsiderada dos DARF’s\.

Deverá ser aplicados Juros e Multa sobre o Valor Total do DARF de acordo com as regras atuais para Juros e Multa existentes hoje no produto \(caso seja necessário à aplicação de Juros e Multa\)\.

OS3160

RN17

Caso um determinado período de apuração seja reprocessado as retenções/retificações que estejam dentro do Controle Mínimo de Retenção não terão esse status alterado\.

OS3160

RN18

Ao final do processamento para geração dos DARF’s, caso o valor não seja o valor mínimo para geração dos mesmos – ou seja 10,00 – os seguintes campos deverão ser atualizados:

\- Indicador de Cálculo da Data de Vencimento para “S”

\- Campo Situação de Controle Mínimo de Retenção para gerado

OS3160

RN19

Na tela de Manutenção do DARF caso o mesmo esteja com o status “Em aberto” e o mesmo seja excluído, as retenções e retificações que compuseram o DARF e que possuem o campo “Situação Controle Mínimo de Retenção” = “Gerado” mudam o campo Situação DARF = “Gerado/Não Pago” muda para “Não Gerado” para que em um futuro próximo essa retenção possa voltar a fazer parte de um DARF\.

Quando o status do campo Situação Controle Mínimo de Retenção mudar de Gerado para Não Gerado, o mesmo continua aparecendo no Controle da Retenção ou Retificação\.

Os créditos gerados na tabela X751\_DCTF\_COMPL não serão controlados através da sistemática de Retenção Mínima \(10,00\)\.

OS3160

RN20

Caso o cliente possua uma retenção cujo DARF gerado possua valor suficiente para pagamento do mesmo \(Lei nº 9\.430 de 1996 que é de R$ 10,00\) e pague o mesmo, e em um período de apuração subsequente o cliente importe uma retificação dessa retenção que gere um DARF menor que R$ 10,00 esse DARF não será gerado\. Além disso, é importante frisar que caso o cliente tente importar um novo registro para corrigir a primeira retificação – aquela que não gerou um DARF por possuir um valor insuficiente – só será possível o cliente corrigir essa informação alterando manualmente a retificação, pois o sistema não permite a importação de uma retificação, cujo registro anterior não tenha sido pago\. Não há tratativa no sistema para corrigir essa situação\.

OS3160

RN21

Ao gerar um DARF e o mesmo recupere as retenções e/ou retificações de períodos anteriores e as do período atual, as informações dos campos “Início Competência” e “Fim Competência” deverão ser atualizadas com as informações do período de geração do DARF, independente do parâmetro “Atualiza Data Competência” estiver selecionado ou não na tela de Tributos Especificações\.

OS3160

RN22

__Rotina parâmetro “Gerar Observações Automaticamente”:__

__\[ALTERADA – OS4428\]__

__*Considerar tela padrão \- campo ind\_geracao\_darf = 0 da tabela prt\_juros\_multa*__

__\- Quando o parâmetro “Gerar Observações Automaticamente” estiver marcado: __a rotina será processada por Estabelecimento sem considerar qualquer consolidação conforme os parâmetros de tela \(ver documento matriz MTZ\_OTF\_Tela\_DARFs\_Geracao\_a\_Partir\_das\_Retencoes\.docx\), deve alimentar o campo OBSERVACAO da SAFX75 concatenando o número do documento fiscal com a razão social do fornecedor da SAFX53 e com o código do estabelecimento processado;

__\- Quando o parâmetro “Gerar Observações Automaticamente” estiver desmarcado:__ o campo não será preenchido\.

__*Considerar da tela padrão \- campo ind\_geracao\_darf = 1 da tabela prt\_juros\_multa \- Compensação*__

__\- Quando o parâmetro “Gerar Observações Automaticamente” estiver marcado: __a rotina será processada por Estabelecimento sem considerar qualquer consolidação conforme os parâmetros de tela \(ver documento matriz MTZ\_OTF\_Tela\_DARFs\_Geracao\_a\_Partir\_das\_Retencoes\.docx\), deve alimentar o campo OBSERVACAO da SAFX75 ou SAFX751 se houver compensação, concatenando o número do documento fiscal com a razão social do fornecedor da SAFX53 ou SAFX530 se houver compensação, e com o código do estabelecimento processado;

__\- Quando o parâmetro “Gerar Observações Automaticamente” estiver desmarcado:__ o campo não será preenchido\.

OS4428

RN23

__Rotina parâmetro “DARF por Empresa”:__

Manter tratamentos atuais\.

__\[ALTERADA – OS4428\]__

__*Considerar tela padrão \- campo ind\_geracao\_darf = 0 da tabela prt\_juros\_multa*__

__\- __Quando o parâmetro “DARF por Empresa” estiver marcado e o parâmetro “Consolidar Retenções” e suas opções estiverem desmarcados, considerar como default a consolidação por código de retenção\.

__*Considerar tela padrão \- campo ind\_geracao\_darf = 1 da tabela prt\_juros\_multa*__

__\- __Quando o parâmetro “DARF por Empresa” e o parâmetro “Consolidar Retenções” e suas opções estiverem desmarcados, considerar como default a consolidação por código de retenção\.

__Observação:__ Sempre que o usuário optar pela geração utilizando o parâmetro “DARF por Empresa” as informações dos tributos deverá ser consolidado para o Estabelecimento Matriz, por esse motivo a importância de mantermos um tratamento default\.

OS4428

RN24

Ao gerar um DARF e o mesmo recupere as retenções e/ou retificações de um período, a informação do campo “Data de Vencimento” deverá ser atualizado de acordo com o período de geração do DARF considerando APENAS os dias úteis \(todos os dias excluindo os finais de semana e feriados\) como Data de Vencimento válida, conforme o Número de Dias \(Corridos antecipados, Corridos postergados ou Úteis\) ou o parâmetro de Último Dia útil informados na tela de Tributos – Especificações \(DW – Manutenção – Cadastros – Tributos\-Especificações\), conforme abaixo:

Número de Dias \(Tributos – Especificações\):

Exemplos:

__*Corridos antecipados:*__

Darf: 5952

Data Apuração: 31/08/2015

Corridos antecipados: 20

Data do Vencimento: __18/09/2015__

Considerar os dias corridos de acordo com o numero de dias informados no campo Corridos antecipados da tela de Tributos – Especificações \(DW – Manutenção – Cadastros – Tributos\-Especificações\), considerando que se o último dia cair em final de semana ou feriado deverá ser antecipada a data de vencimento para o primeiro dia útil anterior\.

__*Corridos postergados:*__

Darf: 3280

Data Apuração: 31/08/2015

Corridos postergados: 20

Data do Vencimento: __21/09/2015__

Considerar os dias corridos de acordo com o numero de dias informados no campo Corridos postergados da tela de Tributos – Especificações \(DW – Manutenção – Cadastros – Tributos\-Especificações\), considerando que se o último dia cair em final de semana ou feriado deverá ser postergada a data de vencimento para o primeiro dia útil posterior\.

__*Úteis:*__

Darf: 1708

Data Apuração: 31/08/2015

Úteis: 20

Data do Vencimento: __28/09/2015__

Considerar os dias úteis de acordo com o numero de dias informados no campo Úteis da tela de Tributos – Especificações \(DW – Manutenção – Cadastros – Tributos\-Especificações\), no somatório dos dias se farão apenas pelos dias úteis \(segunda à sexta\-feira\) considerando os feriados caso os mesmos caiam entre segunda à sexta\-feira até completar o numero de dias informados\. Porém caso o último dia do numero de dias informados cair em um feriado esse não poderá ser considerado como Data de vencimento, devendo postergada a data de vencimento para o primeiro dia útil posterior\.

Parâmetro Último Dia útil \(Tributos – Especificações\):

__*Último Dia útil:*__

Darf: 3280

Periodicidade: Mensal

Data Apuração: 31/08/2015

Último Dia útil: Selecionado

Data do Vencimento: __30/09/2015__

Considerar os dias corridos de acordo com a Periodicidade informada no campo Periodicidade da tela de Tributos – Especificações \(DW – Manutenção – Cadastros – Tributos\-Especificações\), considerando sempre o próximo mês ao da apuração e caso o último dia cair em um final de semana ou feriado deverá ser antecipada a data de vencimento para o primeiro dia útil anterior\.

CH13117\_2015

CH25028\_2015

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

