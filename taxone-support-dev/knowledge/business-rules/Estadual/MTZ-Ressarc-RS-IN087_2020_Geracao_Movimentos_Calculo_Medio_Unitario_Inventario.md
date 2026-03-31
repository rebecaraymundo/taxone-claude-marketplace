# MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Cálculo Médio Unitario Inventário

> Fonte: MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Cálculo Médio Unitario Inventário.docx






THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS

(IN-RE 087/2020)

Cálculo dos Valores Unitários Médios do Inventário



Localização: Menu Estadual, Módulo: Ressarcimento de ICMS-ST - RS (IN-RE 048/2018), itens:
Geração à IN-RE 087/20 à Geração dos Movimentos



DOCUMENTO DE REQUISITO




Sumário

1.	Introdução	1
2.	Recuperação dos Dados e Processamento	1
1º Passo – Recuperar os Produtos Sujeitos a ST que estão no primeiro período de geração e sem valores unitários no Inventário	1
2º Passo – Recuperar as Notas de Entrada até cobrir a Quantidade do Estoque	1
3º Passo: Calcular os Valores Unitários Médios	1
4º Passo: Gravar os Valores Unitários Médios	1
3.	Relatório de Conferência	1


## Introdução


O Cálculo dos Valores Unitários Médios do ICMS, ICMS-ST, Base de Cálculo do ICMS-ST e FECEP-ST do inventário do produto, para o primeiro período de geração.

Originalmente a rotina de Geração do Movimento exigia que, para o primeiro período da geração de um Produto sujeito a ICMS-ST, os Valores Unitários do ICMS, ICMS-ST, Base de Cálculo do ICMS-ST e FECEP-ST viessem carregados na SAFX52 para o dia imediatamente anterior ao mês da geração. Essa exigência se dava apenas para o primeiro mês, pois a partir do segundo período de geração, os Valores Unitários do ICMS, ICMS-ST, Base de Cálculo do ICMS-ST e FECEP-ST são recuperados do cálculo da média ponderada realizada na geração do movimento do mês anterior.

Mas alguns clientes tiveram dificuldade em calcular esses valores unitários para o primeiro período. Sendo assim, criamos essa rotina para realizar o cálculo dos valores unitários, bastando para isso existir o registro de inventário na SAFX52 com quantidade maior que zero e IND_MOT_INV = 06, para o dia imediatamente anterior ao mês da geração.

Os valores unitários calculados serão armazenados na tabela onde são armazenas as médias ponderadas dos períodos (EST_ST_RS_MEDIA_POND), para o produto e dia imediatamente anterior ao mês da geração.


Sobre Produtos Associados:
Para identificar os produtos sujeitos a ICMS-ST utilizamos as opções de parametrização do menu Parâmetros à Produtos: “Por Código”, ou “Por NCM” ou “CEST”.  A parametrização Por Código aceita trabalharmos com o conceito de Produtos Associados. Parametriza-se um produto “principal” e N produtos associados. O produto “principal” é gravado na tabela (ESP_SP_PROD_ST), e os associados ao produto principal na tabela ESP_SP_PROD_ST_ASS.  Os produtos associados servem para recuperação dos movimentos de entradas, saídas e devoluções (x07/x08/x993/x994).  Mas todo o controle de inventário (x52) é em nome do Produto Principal.  O Cálculo dos Valores Unitários Médios do Inventário é gravado em nome do Produto Principal.



Texto da IN-RE 087/20, Tópico 19.3-A.3 que define Cálculo da Média Pondera Móvel dos Valores Unitários do Inventário:
19.3-A.2.1.2.1 -
No primeiro dia de aplicação da sistemática, deverá ser utilizado o valor calculado no inventário das mercadorias previsto no subitem 19.3-A.3.
19.3-A.3 -
Conforme disposto no RICMS, Livro III, art. 25-B, parágrafo único, I, o contribuinte deverá apresentar o registro H005, com o campo MOT_INV igual a "06" e DT_INV igual ao dia imediatamente anterior ao campo DT_INI informado no registro 0000, com informações do inventário das mercadorias recebidas com substituição tributária existentes em estoque no fim do dia 31 de dezembro de 2020 ou do dia anterior àquele em que passar a apurar o ajuste, se posterior a 1º de janeiro de 2021. (Acrescentado pela IN RE 087/20, de 03/11/20. (DOE 04/11/20) - Efeitos a partir de 04/11/20.)
19.3-A.3.1 -
O inventário deverá ser apresentado no arquivo da EFD-ICMS/IPI do mês subsequente ao evento. (Acrescentado pela IN RE 087/20, de 03/11/20. (DOE 04/11/20) - Efeitos a partir de 04/11/20.)
19.3-A.3.2 -
Na hipótese em que não for possível determinar a correspondência entre a base de cálculo do débito de substituição tributária e a respectiva mercadoria, deverá ser utilizado o valor unitário da base de cálculo do débito de substituição tributária registrado no documento fiscal do último recebimento, proporcional à quantidade existente em estoque, desde que a quantidade constante desse documento fiscal seja maior ou igual ao somatório do estoque inventariado. (Acrescentado pela IN RE 087/20, de 03/11/20. (DOE 04/11/20) - Efeitos a partir de 04/11/20.)
19.3-A.3.2.1 -
Na hipótese em que a quantidade das mercadorias registradas no documento fiscal do último recebimento for menor que o somatório do estoque inventariado, serão adicionados os recebimentos registrados em documentos fiscais imediatamente anteriores, até que se complete a quantidade existente em estoque, hipótese em que deverá ser utilizado o valor médio ponderado unitário da base de cálculo do débito de substituição tributária. (Acrescentado pela IN RE 087/20, de 03/11/20. (DOE 04/11/20) - Efeitos a partir de 04/11/20.)

Obs: texto bastante semelhante ao da CAT42 (Ressarcimento SP) do “MANUAL Sistema Ressarcimento_ICMS_ST.pdf”:

3.3.8 Para efeito de determinação do valor de confronto, e na impossibilidade de identificação da operação de entrada da mercadoria, o contribuinte substituí-do considerará o valor correspondente às entradas mais recentes, suficientes para comportar a quantidade envolvida. Caso o documento fiscal referente à entrada mais recente do item não seja suficiente para comportar a quantidade indicada no documento fiscal de saída, e se faça necessário utilizar documen-to(s) fiscal(ais) anterior(es) ao último, o valor a ser lançado a título de valor de confronto corresponderá à média ponderada dos dados obtidos em todas as notas fiscais utilizadas para comportar a quantidade saída, conforme exemplo a seguir.


## Recuperação dos Dados e Processamento


Visão resumida do Processamento
Esse cálculo considera os Produtos Sujeitos a ST, no primeiro período de geração do movimento da IN-087, cujo Inventário está com Valores Unitários zerados.
Para esses produtos, o cálculo vai varrer as últimas entradas até que a quantidade das entradas atinja a quantidade o inventário, e calcular o valor unitário do ICMS, ICMS-ST, Base ICMS-ST e FECEP-ST.


### 1º Passo – Recuperar os Produtos Sujeitos a ST que estão no primeiro período de geração e sem valores unitários no Inventário


Vamos recuperar os produtos sujeitos a ST cujo cálculo será realizado nos próximos passos.

Origem dos dados: - Parametrização de Produtos (por Código, por NCM e por CEST);
- Tabela do Inventário (X52_INVENT_PRODUTO).
Critérios:
- Empresa – código da empresa do login;


- Estabelecimento – código do estabelecimento selecionado para geração;

- Data do Inventário (campo 03 - DATA_INVENTARIO) último dia do mês anterior ao que está sendo processado;

- Motivo do Inventário (campo 40 - IND_MOT_INV) = “06” - controle das mercadorias sujeitas ao regime de substituição tributária;

- Grupo Contagem (campo 04 - GRUPO_CONTAGEM) à 1, 2, 3 e 5;

- O produto deve constar na parametrização do menu “Parâmetros à Produtos à Por Código”, ou, seu NCM deve estar parametrizado no menu “Parâmetros à Produtos à Por NCM”, ou, seu CEST deve estar parametrizado no menu “Parâmetros à Produtos à Por CEST”.

Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração.

No caso da parametrização dos produtos, primeiro é verificado se o produto consta na parametrização da opção “Por Código”. Ao verificar a parametrização por código, basta considerar o produto “principal”. Pois conforme já explicado, as informações do inventário estão registradas em nome do produto “principal” (ESP_SP_PROD_ST).

A prioridade na pesquisa da parametrização dos produtos é: por Código, por NCM, e por último, por CEST, da seguinte forma:

-Caso o produto conste na parametrização por código, a parametrização por NCM não precisa ser verificada.
-Caso não, é verificado se o NCM do produto (NCM do cadastro do produto) consta na parametrização da opção “Por NCM”.
-Caso o produto conste na parametrização por NCM, a parametrização por CEST não precisa ser verificada.
-Caso não, é verificado se o CEST do produto (CEST do cadastro do produto) consta na parametrização da opção “Por CEST”.

- Quantidade de Inventário (X52) > 0

- Valores Unitários do Inventário (X52) zerados e IND_GRAVACAO (X52) <> ‘9’:   -- significa que o cliente não carregou os valores unitários
- 21 - Valor de ICMS Médio (VLR_ICMS_MEDIO) = 0
- 22 - Valor de ICMS-ST Médio (VLR_ICMSS_MEDIO) = 0
- 43 - Valor Base ICMS-ST Médio (VLR_BASE_ICMSS_MEDIO) = 0
- 44 - Valor FECEP Médio (VLR_FCP_MEDIO) = 0
- IND_GRAVACAO (X52)  <> 9
OU                  -- reprocessamento da geração do movimento qdo já ocorreu a Transferência dos Movimentos p/ EFD
Algum Valor Unitário (X52) diferente de zero e IND_GRAVACAO (X52) = ‘9’ e existe Valor Unitário Calculado por essa rotina:
- 21 - Valor de ICMS Médio (VLR_ICMS_MEDIO) <>  0 OU 22 - Valor de ICMS-ST Médio (VLR_ICMSS_MEDIO) <> 0 OU 43 - Valor Base ICMS-ST Médio (VLR_BASE_ICMSS_MEDIO) <> 0 OU 44 - Valor FECEP Médio (VLR_FCP_MEDIO) <> 0
- IND_GRAVACAO (X52) = 9
- Existe registro na Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” (EST_ST_RS_MEDIA_POND), com os critérios abaixo atendidos:
- - Empresa – código da empresa do login;
- - Estabelecimento – código do estabelecimento selecionado para geração;
- - Data = último dia do mês anterior que está sendo processado;
- - Produto = Produto da Parametrização de Produtos (por Código, por NCM e por CEST);
- - IND_GRAVACAO = ‘A’ – significa que o os valores unitários foram calculados por essa rotina

- Só recuperar os Produtos estão no primeiro período de geração.
Ou seja, o Produto que não possua registro na Tabela de Média Ponderada para algum dia do mês anterior, com quantidade maior que zero:
Origem dos dados: - Tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” (EST_ST_RS_MEDIA_POND).
Critérios:
- Empresa – código da empresa do login;
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data pertencente ao mês anterior que está sendo processado;
- Produto = Produto da Parametrização de Produtos (por Código, por NCM e por CEST);
- Qtde total Convertida Inicial (QTD_CONV_INI) >0 OU Quantidade de Devolução de Saída (QTD_CONV_DEV_SAI_MP) > 0 OU
Quantidade Entrada Convertida (QTD_CONV_ENT_MP)>0 OU Quantidade Devolução de Entrada (QTD_CONV_DEV_ENT_MP) >0 OU
Qtde total Convertida Final (QTD_CONV_FIM)> 0
[MFS81749]
Tratamento para Produtos Farmacêuticos de Distribuidores:
- Não recuperar o inventário de Produtos Farmaceuticos de Estabelecimentos Distribuidores. Ou seja, se os dois critérios a seguir forem atendidos, não recuperar o inventário:
- Estabelecimento é um Distribuidor (atacadista), ou seja, na Tela de Dados Iniciais estiver com o campo “Contribuinte Varejista?” = Não;
- Produto do inventário estiver cadastrado, na tela de Parametrização de Produtos Farmacêuticos por Código, no menu: Parametros >  (IN-RE 087/20) > Produtos Farmacêuticos > Código


Recuperação da Quantidade da Tabela de Inventário (X52_INVENT_PRODUTO)
Os critérios acima podem retornar mais de um registro de inventário para o mesmo produto. Caso isso ocorra, recuperar registro a registro, individualmente. Considerar as seguintes informações:
- 12 - Unidade de Medida (COD_MEDIDA)
- 13 - Quantidade de Inventário (QUANTIDADE)

Calcular a quantidade convertida:
- Qtde total Convetida Final:
Campo 13-Quantidade de Inventário, aplicando a conversão, quando necessário. Veja:
Se unidade do inventário (*) = unidade do cadastro do produto (**)
(*) unidade do inventário = campo “12-Unidade de Medida” da SAFX52
(**) unidade do produto = campo “14-Código de Medida” da SAFX2013
Nesse caso não há necessidade de conversão, e o campo será a própria quantidade do inventário;
Senão
Nesse caso a quantidade do inventário (SAFX52) será convertida para a unidade de medida do cadastro do produto;
[Quantidade de Inventário (SAFX52) * Fator de Conversão]
Sobre a conversão de medida:
A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW (menu “Manutenção à Cadastros à Conversão de Unidades de Medida”), da seguinte forma:
- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;
- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas será gravada a seguinte mensagem de erro no log:
“Cálculo dos Valores Unitários do Inventário: O cálculo dos Valores Unitários do Inventário não foi realizado para o produto x-yyyyy, pois não foi possível converter a quantidade do inventário para a medida do cadastro do produto (fator de conversão de XXX para XXX não identificado).”
Onde x-yyyyy são o indicador e código do produto.
O primeiro “XXX” é a unidade do inventário, e o segundo “XXX”, a unidade do cadastro do produto.



### 2º Passo – Recuperar as Notas de Entrada até cobrir a Quantidade do Estoque

Para cada produto sujeito a ST recuperado no passo anterior com a quantidade do estoque convertida, recuperar as últimas notas de entradas de períodos anteriores, até atingir a quantidade de estoque, e calcular o valor unitário médio a partir dos valores [ICMS ], [ BC ICMS-ST ], [ ICMS-ST ] e [FECEP-ST ] com base em todas as entradas identificadas.

Neste passo será feita a recuperação das últimas entradas do produto na SAFX07/SAFX08, da nota mais recente para as mais antigas, considerando os critérios a seguir:

Origem dos dados: - SAFX07 / SAFX08 – Tabelas dos Documentos Fiscais (DATAMART ou X07/X08)

Critérios:
- Empresa                  = Código da empresa do login
- Estabelecimento      = Código do estabelecimento selecionado para geração
- Data Fiscal das notas de entradas >= a data informada em “Pesquisar as últimas entradas até” (parâmetro da tela de geração)
- Data Fiscal das notas de entradas <= último dia do mês anterior ao que está sendo processado
- Movimento E/S        = deve ser uma nota de entrada (MOVTO_E_S <> “9”)
- Normal/Devolução   = deve ser uma nota normal (NORM_DEV = ‘1’)
- Somente notas não canceladas;
- Quantidade > 0
- Produto                    = produto sujeito a ST
- O CFOP ou CFOP/Natureza do item deve constar na parametrização do menu “Parâmetros à (IN-RE 087/20) à Operações” para a seguinte operação:
- Entradas (e Devoluções)” (código parâmetro 771)
- Serão recuperadas as notas de entrada suficientes para cobrir a quantidade do Estoque (ver item abaixo que detalha sobre como totalizar a quantidade das entradas);
- A pesquisa das notas será feita até atingir a quantidade do estoque, ou, até que a Data Limite informada para a pesquisa seja atingida. Este limite é identificado através do parâmetro “Pesquisar as últimas entradas até” da tela da geração. Isso significa que devem ser consideradas apenas as notas com a DATA_FISCAL que não exceda a data limite estabelecida no parâmetro;

[MFS591083] Tratamento das Incorporações de Empresas/Estabelecimentos:
- Se o total da quantidade das notas de entrada recuperadas com os critérios acima, não for suficiente para cobrir a quantidade do estoque em questão, verificar se o parâmetro para buscar as notas nas empresas incorporadas está marcado na tela da geração.
- Se o parâmetro “Considerar as notas fiscais da empresa incorporada” estiver marcado:
- Considerar as notas das empresas/estabelecimentos cadastradas como incorporadas na tela de Relação de Empresa
- Incorporadora x Incorporada** para a empresa/estabelecimento da geração (incorporadora), para recuperar as notas de
- entrada afim de atingir a quantidade de estoque do produto.
- Senão
- Considerar somente as notas fiscais da empresa e estabelecimento selecionados para a geração.

- ** Módulo Parâmetros, item Preliminares  Relação de Empresa Incorporadora x Incorporada

O parâmetro “Utilizar DATA MART para períodos anteriores” determinará se a nota fiscal de entrada será recuperada das Tabelas Normais (X07/X08), ou das Tabelas DATAMART (dwt). Caso o parâmetro esteja selecionado, as tabelas DATAMART serão consideradas, caso contrário utilizar as tabelas Normais (X07/X08).

Mensagem de aviso quando não identificar entradas p/ o produto:

Se nenhuma entrada for identificada para o produto em questão, o cálculo do Valor Unitário não será realizado, e no log de erro será gravada a seguinte mensagem: “Cálculo dos Valores Unitários do Inventário: O cálculo dos Valores Unitários do Inventário não foi realizado para o produto x-yyyyy, pois não foram encontradas notas de entrada do produto. Consultar os detalhes e pré-requisitos do cálculo no help e roteiro operacional do módulo”.

Onde x-yyyyy são o indicador e código do produto.


Como totalizar a quantidade das notas de entrada e comparar com a QTD do estoque do produto em questão:

A quantidade das notas de entrada, quando necessário, será convertida para a unidade de medida do cadastro do produto (SAFX2013).

Este procedimento é feito antes de utilizar a informação do campo, já que todas as quantidades devem estar na mesma unidade de medida.

Se a unidade de medida do item da entrada = unidade de medida do cadastro do produto:
(campo “25-Unidade de Medida” da SAFX08 = campo “14-Código de Medida” da SAFX2013)
Nesse caso, não é necessário efetuar a conversão;
Senão
Se existir informação no campo “137-Quantidade Convertida” do item (SAFX08)
Nesse caso, será utilizada a informação da quantidade já convertida do campo “137-Quantidade Convertida”;
Senão
Nesse caso a quantidade da entrada item (SAFX08) será convertida para a unidade de medida do cadastro do produto;




Crítica da Quantidade das Entradas x QTD do Estoque:

O total da quantidade das notas de entrada recuperadas da SAFX07/SAFX08 deve ser >= a quantidade do Estoque em questão. Caso contrário, será gravada a seguinte mensagem no log, e o cálculo do Valor Unitário não será realizado para o produto em questão: “Cálculo dos Valores Unitários do Inventário: O cálculo dos Valores Unitários do Inventário não foi realizado para o produto x-yyyyy, pois as entradas recuperadas da SAFX07/SAFX08 não foram suficientes para cobrir a quantidade em estoque”
Este problema poderá ocorrer quando a pesquisa das entradas na SAFX07/SAFX08 for realizada até a data limite especificada, mas a quantidade total das notas recuperadas não for suficiente para cobrir a quantidade do estoque em questão;

(Conforme já citado acima, para totalizar a quantidade das entradas, será utilizada a informação da quantidade já convertida, quando for o caso)



### 3º Passo: Calcular os Valores Unitários Médios



As entradas recuperadas para o produto em questão serão processadas em ordem de data, sempre da mais recente para mais antiga.

Para cada entrada a ser processada será calculado um valor de ICMS, um de ICMS-ST, um de Base ICMS-ST e um de FECEP-ST, conforme a regra abaixo.

- Se quantidade do Estoque = quantidade da entrada, considerar Valor ICMS = Valor ICMS da entrada (vide “Considerações”);
Valor ICMS-ST = Valor ICMS-ST da entrada (vide “Considerações”);
Valor Base ICMS-ST = Valor Base ICMS-ST da entrada (vide “Considerações”);
Valor FECEP-ST = Valor FECEP-ST da entrada (vide “Considerações”);
- Se quantidade do Estoque > quantidade da entrada, considerar Valor ICMS = Valor ICMS da entrada (vide “Considerações”);
- Valor ICMS-ST = Valor ICMS-ST da entrada (vide “Considerações”);
Valor Base ICMS-ST = Valor Base ICMS-ST da entrada (vide “Considerações”);
Valor FECEP-ST = Valor FECEP-ST da entrada (vide “Considerações”);

- Se quantidade do Estoque < quantidade da entrada, calcular os valores do ICMS, ICMS-ST, Base-ST e FECEP-ST proporcional à quantidade restante para cobrir o estoque, da seguinte forma:
[ Valor ICMS = (Valor ICMS da entrada  / quantidade da entrada) * quantidade do estoque ]
[ Valor ICMS-ST = (Valor ICMS-ST da entrada  / quantidade da entrada) * quantidade do estoque]
[Valor Base ICMS-ST = Valor Base ICMS-ST da entrada / quantidade da entrada) * quantidade do estoque]
[ Valor FECEP-ST = (Valor FECEP-ST da entrada  / quantidade da entrada) * quantidade do estoque]

[MFS72429] Substituição do truncamento pelo arredondamento dos campos
Obs.: Todos os valores calculados acima devem ser arredondados, não devem ser truncados.
[MFS90131] Arredondar para 8 casas decimais o resultado dos cáculos acima ( (valor / qtde) * qtde)


Após o processamento de todas as entradas, calcular os Valores Unitários Médios do ICMS, ICMS-ST (sem e com FECEP), Base-ST e do FECEP-ST:


[MFS72429] Substituição do truncamento pelo arredondamento dos campos
Obs.: Todos os valores unitários calculados acima devem ser arredondados, não devem ser truncados.
[MFS90131] Arredondar para 8 casas decimais o resultado dos cáculos (valor / qtde)

Considerações:


- A “quantidade da entrada” utilizada no cálculo é a quantidade da nota de entrada já convertida (conforme a regra de conversão já descrita acima);

- O “Valor ICMS da entrada” utilizado no cálculo será o valor do ICMS do item (campo “43-Valor ICMS”, se preenchido, ou campo “80-ICMS não Escriturado”, se preenchido, ou campo "225-Valor ICMS Não Destacado");

- O “Valor ICMS-ST da entrada” utilizado no cálculo será os valores (“52-Valor ICMS Substituição Tributária”, ou “145-Valor de ICMS-ST não .Escriturado”, ou "133-ICMS-ST Não Escriturado", ou “107-Valor Carga Tributária Origem”), aplicando o tratamento do Fecep embutido, conforme descrito a seguir:

Tratamento do FECEP-ST quando embutido no ICMS-ST
Tratamento do FECEP embutido nos vlrs de ICMS/ICMS-ST (aplicado às Entradas e Devoluções de Entradas):
Se o item de mercadoria foi recuperado das tabelas “normais” (X07/X08), então:
Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS-ST nos itens (SAFX08)” da Parametrização dos Dados Iniciais foi marcado, então:
Se for considerado o “52-Valor ICMS Substituição Tributária” p/ o Valor do ICMS-ST :
Preencher com: (Valor do ICMS-ST- Valor do FECEP-ST)
Senão:
Preencher com: (Valor do ICMS-ST)
Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS-ST nos itens (SAFX08)” da Parametrização dos Dados Iniciais não foi marcado, então:
Preencher com: (Valor do ICMS-ST)

Se o item de mercadoria foi recuperado das tabelas do DATAMART, então:
Se for considerado o “52-Valor ICMS Substituição Tributária” para o Valor do ICMS-ST :
Preencher com:  (Valor do ICMS-ST - Valor do FECEP-ST)
Senão
Preencher com: (Valor do ICMS-ST)
Onde:
- Valor do ICMS-ST (*): Valor do ICMS-ST é oriundo de um dos quatro campos do item da nota fiscal de Entrada (SAFX08), dependendo de qual esteja preenchido:
Se campo “61-BASE_SUB_TRIB_ICMS” e “52-VLR_SUBST_ICMS” estiverem preenchidos, então:
Valor do ICMS-ST = 52-VLR_SUBST_ICMS.
Senão:
Se campo “144- VLR_BASE_ICMSS_N_ESCRIT” e
“145- VLR_ICMSS_N_ESCRIT” estiverem preenchidos, então:
Valor do ICMS-ST = 145- VLR_ICMSS_N_ESCRIT.
Senão:
Se campo “144- VLR_BASE_ICMSS_N_ESCRIT” e
“133- VLR_ICMSS_NDESTAC” preenchidos, então:
Valor do ICMS-ST = 133- VLR_ICMSS_NDESTAC.
Senão:
Se campo “106- VLR_BASE_ICMS_ORIG” e
“107- VLR_TRIB_ICMS_ORIG” preenchidos, então:
Valor do ICMS-ST = 107- VLR_TRIB_ICMS_ORIG

- O “Valor Base ICMS-ST da entrada” utilizado no cálculo será um dos valores (61-BASE_SUB_TRIB_ICMS ou 144 - VLR_BASE_ICMSS_N_ESCRIT ou 106-VLR_BASE_ICMS_ORIG) conforme descrito abaixo:

Preencher com: 61-BASE_SUB_TRIB_ICMS ou 144 - VLR_BASE_ICMSS_N_ESCRIT ou 106-VLR_BASE_ICMS_ORIG (conforme regras abaixo):
Se campo “61-BASE_SUB_TRIB_ICMS” e “52-VLR_SUBST_ICMS” estiverem preenchidos, então:
Considerar os campos “61-BASE_SUB_TRIB_ICMS” da SAFX08.
Senão
Se campo “144- VLR_BASE_ICMSS_N_ESCRIT” e “145- VLR_ICMSS_N_ESCRIT” estiverem preenchidos, então:
Considerar os campos “144- VLR_BASE_ICMSS_N_ESCRIT da SAFX08.
Senão
Se campo “144- VLR_BASE_ICMSS_N_ESCRIT” e “133- VLR_ICMSS_NDESTAC” estiverem preenchidos, então:
Considerar os campos “144- VLR_BASE_ICMSS_N_ESCRIT” da SAFX08
Senão
Se campo “106-VLR_BASE_ICMS_ORIG” e “107-VLR_TRIB_ICMS_ORIG” estiverem preenchidos, então:
Considerar o campo “106-VLR_BASE_ICMS_ORIG” da SAFX08.

- O “Valor FECEP-ST da entrada” utilizado no cálculo será o valor do FECEP ICMST-ST do item (campo “140-Valor FECEP ICMS-ST");

- A “quantidade do estoque” utilizado no cálculo é a quantidade que consta na X52_INVENT_PRODUTO. Ao processar a primeira nota de entrada, é utilizada a quantidade integral do estoque. Para as próximas entradas, a “quantidade do estoque” será a quantidade integral do estoque, menos a quantidade das entradas processadas anteriormente (ver o exemplo abaixo);

Observação: As notas de entrada com os valores considerados no cálculo serão demonstradas num relatório gravado em arquivo excel. Ver tópico 3 – Relatório de Conferência.

Exemplo:

O exemplo a seguir é básico, mostra apenas o conceito do cálculo descrito acima e foi feito com base no exemplo dado para o cálculo do valor do confronto na “MTZ-Ressarc-SP-Calculo_Vlr_Confronto_Saidas”.





### 4º Passo: Gravar os Valores Unitários Médios


Para cada Produto sujeito ao ICMS-ST(*), gravar um registro na tabela EST_ST_RS_MEDIA_POND com os valores unitários calculados no Passo 3, para o último dia do mês anterior.



Tabela EST_ST_RS_MEDIA_POND

Os campos sinalizados com asterisco compõem a chave da tabela.


Obs: Limpar os registros de processos anteriores da tabela EST_ST_RS_MEDIA_POND  com IND_GRAVACAO = A.


## Relatório de Conferência

Gravar num arquivo excel com o seguinte conteúdo:
Para cada produto sujeito a ST considerado no cálculo:
- um ou mais registros correspondentes às notas de entrada consideradas no cálculo.
- UM registro demonstrando a quantidade do inventário e os valores unitários médios calculados, que foram gravados na tabela EST_ST_RS_MEDIA_POND.

Nome do arquivo: Relatório_Conferencia_Calculo_Media_Inventário_mm_aaaa_cod_estab.xlsx

Abaixo estão discriminados por cores, os campos que serão gravados para as notas e para o inventário:
- Em azul: campos que devem ser preenchidos apenas para os registros de notas de entrada
- Em verde: campos que devem ser preenchidos para o registro de inventário
- Em preto: campos que devem ser preenchidos para todos os registros (notas e inventário).

MFS591083: Tratamento das Incorporações de Empresas/Estabelecimentos





= = = = = =


| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS72212 | Liliane Videira Assaf | Criação do Cálculo dos Valores Unitários Médios do Inventário | 09/09/2021 |
| MFS72429 | Andréa Rocha | Inclusão do arredondamento dos valores calculados, ou seja, os valores calculados não serão mais truncados.  Conforme informação passada pela SEFAZ/RS. | 01/10/2021 |
| MFS81749 | Liliane Assaf | Tratamento para Notas de Produtos Farmacêuticos de Distribuidores criada pela MFS66473 | 15/03/2022 |
| MFS90131 | Liliane Assaf | Chamado Lasa/Magalu: Tratamento na diferença de 0,000001 do valor médio unitário do último dia do mês para o do primeiro dia do mês seguinte. | 01/08/2022 |
| MFS591083 | Liliane Assaf | Tratamento das Incorporações de Empresas/Estabelecimentos | 22/01/2024 |
|  |  |  |  |


| Exemplo: Último documento de entrada: 10 unidades, a R$15,00 cada. |
| --- |
| Penúltimo documento de entrada: 20 unidades, a R$10,00 cada. |
| Saída: 12 unidades. |
| Valor de Confronto: 10 unidades a R$ 15,00 = R$ 150,00 + 2 unidades a R$ 10,00 = R$ 20,00. |
| Valor total: R$ 170,00, que divididos por 12 = R$ 14,17 (valor unitário a ser informado). |


| Para efetuar a conversão de medida:  A conversão é feita conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW (menu “Manutenção à Cadastros à Conversão de Unidades de Medida”), da mesma forma que é feita na rotina de geração dos movimentos:  - Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto; - Caso não exista, pesquisa o fator na tabela de conversão padrão;  Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o cálculo do Valor Unitário não será realizado para o produto, e no log de erro será gravada a seguinte mensagem: “Cálculo dos Valores Unitários do Inventário: O cálculo dos Valores Unitários do Inventário não foi realizado para o produto x-yyyyy, pois não foi possível converter a quantidade de nota de entrada para a medida do cadastro do produto (fator de conversão de XXX para XXX não identificado).”  Onde x-yyyyy são o indicador e código do produto. O primeiro “XXX” é a unidade do item da entrada, e o segundo “XXX”, a unidade do cadastro do produto.  O log deve exibir as seguintes informações para conferência do usuário: - Identificação do item da nota de entrada (ao menos o número, série, data e item); |
| --- |


| Valor Médio Unitário do ICMS | Somatório do “Valor ICMS” de todas as entradas dividido pela Quantidade do Estoque. |
| --- | --- |
| Valor Médio Unitário do ICMS-ST s/ FECEP | Somatório do “Valor ICMS-ST” de todas as entradas dividido pela Quantidade do Estoque. |
| Valor Médio Unitário do ICMS-ST c/ FECEP | Somatório dos (“Valor ICMS-ST” + “Valor FECEP-ST”) de todas as entradas dividido pela Quantidade do Estoque. |
| Valor Médio Unitário da Base de Cálculo do ICMS-ST | Somatório do “Valor Base ICMS-ST” de todas as entradas dividido pela Quantidade do Estoque. |
| Valor Médio Unitário do FECEP-ST | Somatório do “Valor FECEP-ST” de todas as entradas dividido pela Quantidade do Estoque. |


| EXEMPLO 1: PRODUTO XXX – inventário em 30/04 Notas de Entrada:     Data               NF           QTD       Valor        ICMS   ICMS-ST   BASE-ST   FECEP-ST 25/04/2019      450       10,0000      50,00        6,00       5,00         8,00            4,00 08/05/2019      511         2,0000      13,50        1,62       3,62         5,00            2,62  Inventário:     Data              QTD        30/04/2019       5,0000        Cálculo do Valor Unitário do Inventário de 30/04:  Nota de Entrada: 450 (de 25/04)  A Quantidade do Estoque (5,0000) é < Quantidade da entrada (10,0000), logo:  Valor ICMS = (6,00 / 10,0000) * 5,0000 = 3,00  Valor ICMS-ST = (5,00 / 10,0000) * 5,0000 = 2,50   Valor Base-ST = (8,00 / 10,0000) * 5,0000 = 4,00                                                                                                   Valor Unitário ICMS = (3,00)/5,00 = 0,6                                                                                               Valor Unitário ICMS-ST = (2,50)/5,00 = 0,5                                                                                               Valor Unitário Base ICMS-ST = (4,00)/5,00 = 0,8                                                                                               Valor Unitário FECEP-ST = (2,00)/5,00 = 0,4   EXEMPLO 2: PRODUTO XXX – inventário em 31/05 Notas de Entrada:     Data               NF           QTD       Valor        ICMS   ICMS-ST   BASE-ST   FECEP-ST 25/04/2019      450       10,0000      50,00        6,00       5,00         8,00            4,00 08/05/2019      511         2,0000      13,50        1,62       3,62         5,00            2,62  Inventário:     Data              QTD        31/05/2019       5,0000        Cálculo do Valor Unitário do Inventário de 31/05):    Nota de entrada: 511 (de 08/05) A Quantidade do Estoque (5,0000) é > Quantidade da entrada (2,0000), logo:  Valor ICMS = 1,62   Valor ICMS-ST = 3,62 Valor Base-ST = 5,00  Valor FECEP-ST = 2,62  Saldo quantidade do Estoque a ser considerada no cálculo da próxima entrada: 5,0000 – 2,0000 = 3,0000  Nota de entrada: 450 (de 25/04) A Quantidade da Dev. Saída (3,0000) é < Quantidade da entrada (10,0000), logo:  Valor ICMS = (6,00 / 10,0000) * 3,0000 = 1,80  Valor ICMS-ST = (5,00 / 10,0000) * 3,0000 = 1,50  Valor Base-ST = (8,00 / 10,0000) * 3,0000 = 2,4  Valor FECEP-ST = (4,00 / 10,0000) * 3,0000 = 1,20                                                                                                Valor Unitário ICMS = (1,62 + 1,80)/5,00 = 0,68                                                                                               Valor Unitário ICMS-ST = (3,62 + 1,50)/5,00 = 1,02                                                                                               Valor Unitário Base ICMS-ST = (5,00 + 2,40)/5,00 = 1,48                                                                                               Valor Unitário FECEP-ST = (2,62 + 1,20)/5,00 = 0,76 |
| --- |


| PK | Campo |  | Regra de Preenchimento |
| --- | --- | --- | --- |
| (*) | Código do Estabelecimento | COD_ESTAB | Código do estabelecimento SELECIONADO na tela de geração |
| (*) | Código da Empresa | COD_EMPRESA | Código da empresa de login |
| (*) | Código do Estabelecimento | COD_ESTAB_ORIG | Código do estabelecimento SELECIONADO na tela de geração |
| (*) | Data | DATA | Último dia do mês anterior. |
| (*) | Produto | Grupo_Produto, Ind_Produto, Cod_Produto | Produto sujeito ao ICMS-ST foco do processamento. |
| Saldo Inicial do Dia | Saldo Inicial do Dia | Saldo Inicial do Dia | Saldo Inicial do Dia |
|  | Qtde total Convetida Inicial | QTD_CONV_INI | Preencher com zero. |
|  | Valor do ICMS Calculado Inicial | VLR_ICMS_INI_MP | Preencher com zero. |
|  | Valor do ICMS-ST Calculado Inicial | VLR_ICMS_ST_INI_MP | Preencher com zero. |
|  | Valor Base de Cálculo do ICMS-ST Calculado Inicial | VLR_BC_ST_INI_MP | Preencher com zero. |
|  | Valor FECEP-ST Calculado Inicial | VLR_FECEP_ST_INI_MP | Preencher com zero. |
| Devoluções das Saídas do Dia | Devoluções das Saídas do Dia | Devoluções das Saídas do Dia | Devoluções das Saídas do Dia |
|  | Quantidade Devolvida Convertida | QTD_CONV_DEV_SAI_MP | Preencher com zero. |
|  | Valor do ICMS Calculado para Devolução | VLR_ICMS_DEV_SAI_MP | Preencher com zero. |
|  | Valor do ICMS-ST Calculado para Devolução | VLR_ICMS_ST_DEV_SAI_MP | Preencher com zero. |
|  | Valor Base de Cálculo do ICMS-ST Calculado para Devolução | VLR_BC_ST_DEV_SAI_MP | Preencher com zero. |
|  | Valor FECEP-ST Calculado para Devolução | VLR_FECEP_ST_DEV_SAI_MP | Preencher com zero. |
| Entradas do Dia | Entradas do Dia | Entradas do Dia | Entradas do Dia |
|  | Quantidade Entrada Convertida | QTD_CONV_ENT_MP | Preencher com zero. |
|  | Valor do ICMS Calculado para Entrada | VLR_ICMS_ENT_MP | Preencher com zero. |
|  | Valor do ICMS-ST Calculado para Entrada | VLR_ICMS_ST_ENT_MP | Preencher com zero. |
|  | Valor Base de Cálculo do ICMS-ST Calculado para Entrada | VLR_BC_ST_ENT_MP | Preencher com zero. |
|  | Valor FECEP-ST Calculado para Entrada | VLR_FECEP_ST_ENT_MP | Preencher com zero. |
| Devoluções das Entradas do Dia | Devoluções das Entradas do Dia | Devoluções das Entradas do Dia | Devoluções das Entradas do Dia |
|  | Quantidade Devolvida Convertida | QTD_CONV_DEV_ENT_MP | Preencher com zero. |
|  | Valor do ICMS Calculado para Devolução | VLR_ICMS_DEV_ENT_MP | Preencher com zero. |
|  | Valor do ICMS-ST Calculado para Devolução | VLR_ICMS_ST_DEV_ENT_MP | Preencher com zero. |
|  | Valor Base de Cálculo do ICMS-ST Calculado para Devolução | VLR_BC_ST_DEV_ENT_MP | Preencher com zero. |
|  | Valor FECEP-ST Calculado para Devolução | VLR_FECEP_ST_DEV_ENT_MP | Preencher com zero. |
| Saldo Final do Dia | Saldo Final do Dia | Saldo Final do Dia | Saldo Final do Dia |
|  | Qtde total Convetida Final | QTD_CONV_FIM | Preencher com zero. |
|  | Valor do ICMS Calculado Final | VLR_ICMS_FIM_MP | Preencher com zero. |
|  | Valor do ICMS-ST Calculado Final | VLR_ICMS_ST_FIM_MP | Preencher com zero. |
|  | Valor Base de Cálculo do ICMS-ST Calculado Final | VLR_BC_ST_FIM_MP | Preencher com zero. |
|  | Valor FECEP-ST Calculado Final | VLR_FECEP_ST_FIM_MP | Preencher com zero. |
| Valores Médios Unitários Calculados do Dia | Valores Médios Unitários Calculados do Dia | Valores Médios Unitários Calculados do Dia | Valores Médios Unitários Calculados do Dia |
|  | Valor Médio Unitário do ICMS | VLR_UNIT_ICMS_FIM_MP | Valor Médio Unitário do ICMS calculado no passo 3. [MFS90131] Arredondar para 8 casas decimais o resultado do cáculo (vide passo 3). |
|  | Valor Médio Unitário do ICMS-ST s/ FECEP | VLR_UNIT_ICMS_ST_FIM_MP | Valor Médio Unitário do ICMS-ST s/ FECEP calculado no passo 3. [MFS90131] Arredondar para 8 casas decimais o resultado do cáculo (vide passo 3). |
|  | Valor Médio Unitário do ICMS-ST c/ FECEP | VLR_UNIT_ICMS_ST_FECEP_FIM_MP | Valor Médio Unitário do ICMS-ST c/ FECEP calculado no passo 3. [MFS90131] Arredondar para 8 casas decimais o resultado do cáculo (vide passo 3). |
|  | Valor Médio Unitário da Base de Cálculo do ICMS-ST | VLR_UNIT_BC_ST_FIM_MP | Valor Médio Unitário da Base de Cálculo do ICMS-ST calculado no passo 3. [MFS90131] Arredondar para 8 casas decimais o resultado do cáculo (vide passo 3). |
|  | Valor Médio Unitário do FECEP-ST | VLR_UNIT_FECEP_ST_FIM_MP | Valor Médio Unitário do FECEP-ST calculado no passo 3. [MFS90131] Arredondar para 8 casas decimais o resultado do cáculo (vide passo 3). |
|  | Indicador de Gravação | IND_GRAVACAO | ‘A’ – significa que o os valores unitários foram calculados por essa rotina |
|  | Número do Processo | PROC_ID | Número do Processo da geração do movimento |


| Código da empresa | Empresa de login |
| --- | --- |
| Código do estabelecimento | Estabelecimento informado na tela de geração. |
| Período (mês e ano) | Período informado na tela de geração. |
| Produto (ind-cod) | Indicador + - + Código do produto da Nota de entrada recuperada no passo 3 (campo 13 e 14 - SAFX08). |
| Data Inventário | Data do Inventario recuperado no passo 1 (último dia do mês anterior ao que está sendo processado) |
| Cod Empresa do Doc Fiscal | Codigo da Empresa da Nota de Entrada (campo 01 - SAFX08) |
| Cod Estab do Doc Fiscal | Codigo do Estabelecimento da Nota de Entrada (campo 01 - SAFX08) |
| Data Fiscal | Data Fiscal da Nota de entrada considerada no cálculo no passo 3 (campo 03 - SAFX08). |
| Tipo do Documento | Tipo Documento da Nota de entrada considerada no cálculo no passo 3 (campo 06 - SAFX08). |
| Número do Documento | Número da Nota de entrada considerada no cálculo no passo 3 (campo 09 -SAFX08). |
| Série do Documento | Série da Nota de entrada considerada no cálculo no passo 3 (campo 10 -SAFX08). |
| Subsérie do Documento | Subsérie da Nota de entrada considerada no cálculo no passo 3 (campo 11 -SAFX08). |
| Pessoa Fis/Jur (ind-cod) | Indicador + - + Código da Pessoa Fis/Jur da Nota de entrada considerada no cálculo no passo 3 (campo 07 e 08 -SAFX08). |
| Número do Item | Número do item da Nota de entrada considerada no cálculo no passo 3 (campo 18 -SAFX08). |
| Medida do Produto | Unidade de Medida do Cadastro do Produto (campo 14 – SAFX2013) |
| Medida da Nota | Unidade de Medida da Nota de entrada considerada no cálculo no passo 3 (campo 25 -SAFX08). |
| Quantidade Estoque | Quantidade recuperada do inventário já convertida (vide passo 1) |
| Quantidade da nota | Quantidade da Nota de entrada recuperada no passo 3 (campo 24 -SAFX08). |
| Quantidade da nota Convertida (1) | Quantidade da Nota de entrada recuperada no passo 3, convertida para unidade de medida do produto. |
| Quantidade da nota Utilizada (2) | Quantidade da Nota de entrada utilizada para atingir a quantidade do estoque, conforme explicado no passo 3. |
| Valor do ICMS da nota (3) | “Valor ICMS da entrada” conforme explicado no passo 3 em “Considerações”. |
| Valor do ICMS-ST da nota (sem fecep) (4) | “Valor ICMS-ST da entrada” conforme explicado no passo 3 em “Considerações”. |
| Valor da Base ICMS-ST da nota (5) | “Valor Base ICMS-ST da entrada” conforme explicado no passo 3 em “Considerações”. |
| Valor do FECEP-ST da nota (6) | “Valor FECEP-ST da entrada” conforme explicado no passo 3 em “Considerações”. |
| Valor do ICMS Proporcional ((3)/(1) *(2)) | Conforme explicado no passo 3, é o valor do ICMS utilizado para cobrir a quantidade de estoque. |
| Valor do ICMS-ST Proporcional ((4)/(1) *(2)) | Conforme explicado no passo 3, é o valor do ICMS-ST utilizado para cobrir a quantidade de estoque. |
| Valor da Base ICMS-ST Proporcional ((5)/(1) *(2)) | Conforme explicado no passo 3, é o valor da Base ICMS-ST utilizado para cobrir a quantidade de estoque. |
| Valor da FECEP-ST Proporcional ((6)/(1) *(2)) | Conforme explicado no passo 3, é o valor do FECEP-ST utilizado para cobrir a quantidade de estoque. |
| Valor Médio Unitário do ICMS | Valor Unitário Médio do ICMS calculado para o produto e gravado na EST_ST_RS_MEDIA_POND com (vide passo 4). |
| Valor Médio Unitário do ICMS-ST s/ FECEP | Valor Unitário Médio do ICMS-ST sem Fecep calculado para o produto e gravado na EST_ST_RS_MEDIA_POND com (vide passo 4). |
| Valor Médio Unitário do ICMS-ST c/ FECEP | Valor Unitário Médio do ICMS-ST com Fecep calculado para o produto e gravado na EST_ST_RS_MEDIA_POND com (vide passo 4). |
| Valor Médio Unitário da Base de Cálculo do ICMS-ST | Valor Unitário Médio da Base do ICMS-ST calculado para o produto e gravado na EST_ST_RS_MEDIA_POND com (vide passo 4). |
| Valor Médio Unitário do FECEP-ST | Valor Unitário Médio do FECEP-ST calculado para o produto e gravado na EST_ST_RS_MEDIA_POND com (vide passo 4). |
