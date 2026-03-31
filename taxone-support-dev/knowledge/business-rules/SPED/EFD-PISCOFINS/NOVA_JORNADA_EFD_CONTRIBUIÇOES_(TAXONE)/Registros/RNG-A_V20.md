# RNG-A_V20

- **Fonte:** RNG-A_V20.docx
- **Modificado:** 2026-01-16
- **Tamanho:** 54 KB

---

Registro D101 EFD Contribuições – Bloco A

Quadro de Revisões

__Data__

__OS / Chamado__

__Descrição__

__Responsável__

09/12/2021

MFS76116

Alteração na geração do Registro A170 – Campo 07 – NAT\_BC\_CRED para considerar o parâmetro do Estabelecimento Centralizado se preenchido\.

Rogério Ohashi

03/07/2023

MFS\-547522

Alteração da regra na geração de notas fiscais nos registros A100/A170 quando Class\.Doc\.Fisc = 9 \- Outros Documentos Não Escriturados

Rosemeire Santos

14/09/2023

MFS\-564542

Tratamento na RNA170\-09, para considerar alíquota do PIS e COFINS com 4 casas decimais, após a virgula na escrituração de notas de transporte com alíquota diferenciada nos Registros A100 e A170\.

Rosemeire Santos

30/10/2023

MFS\-581831

Tratamento nas __RNA170\-9__ e __RNA170\-10, __para considerar apenas 2 casas decimais, após a virgula das alíquotas de PIS e COFINS, na geração do arquivo até com data de até 31/12/2022\.

Rosemeire Santos

__Regras de Recuperação para os registros do bloco A:__

__Registro A010 – Identificação do Estabelecimento__

__RNG\-A010__

CH27235/2013

Gerar um registro A010 para cada CNPJ de estabelecimento que possua movimentação nos registros do bloco A\.

As movimentações do bloco A devem ser geradas imediatamente abaixo do registro A010 do CNPJ do estabelecimento correspondente\.

\* *Foi incluída observação para gerar por CNPJ do estabelecimento por conta de situações onde a empresa tem mais de um estabelecimento com o mesmo CNPJ\. Neste caso, deve ser gerado apenas um A010 por CNPJ e as movimentações serão vinculadas abaixo do CNPJ\.*

__Registro A100 – Notas Fiscais de Serviço__

__RNG\-A100__

Deve ser gerado um registro A100 para cada documento fiscal \(SAFX07\) que atenda aos critérios abaixo:

- Classificação: \(campo “12 – Classificação do Documento” da SAFX07\)

Igual a “2 – Serviço” ou “I – Documento Internacional/Invoice” ou “9 – Outros Documentos Não Escriturados”; 

- Campo Crédito/Contribuição Extemporânea \(campo novo da SAFX08/SAFX09\) preenchido com conteúdo igual a “N”, 	Item não extemporâneo\.

__Obs\.:__ Se os campos “Crédito/Contribuição Extemporânea” e “Data do Lançamento PIS/COFINS” não estiverem preenchidos no item do documento fiscal \(SAFX08\), considerar o conteúdo desses campos informados na capa do documento \(SAFX07\)\.

- Não serão consideradas NFs sem item

__\[ALTERADA CH6690\_2017 \(MFS\-11222\)\]__

- Não serão consideradas NFs de entrada de terceiros com status de cancelada \(campo “03 – Movimento Entrada/Saída” igual a “1 – Documento de Entrada, Documento de Terceiros” e campo “30 – Situação da Nota” diferente de “N – Nota Fiscal não Cancelada” da SAFX07\)\.
- Para um Documento Fiscal de Saída \(Campo MOVTO\_E\_S = 9\), além das regras gerais, __considerar__:

Observar o parâmetro Registro A100, C100, C180 e C190 \- Seleção das Operações Geradoras de Receita disponível na tela de Dados Iniciais\.

__Se o parâmetro estiver preenchido com conteúdo igual a ‘’Data de Lançamento EFD PIS/COFINS’’__, o campo Data do Lançamento \(campo 247 \- DAT\_LANC\_PIS\_COFINS da SAFX07 ou campo 81 \- DAT\_LANC\_PIS\_COFINS da SAFX09\) deve estar preenchido com uma data que esteja entre a Data Inicial e Data Final de geração do arquivo\.

__Se o parâmetro estiver preenchido com conteúdo igual a ‘’Data de Emissão”, o campo Data da Emissão__ \(campo 11 \- DATA\_EMISSAO da SAFX07\) deve estar preenchido com uma data que esteja entre a Data Inicial e Data Final de geração do arquivo\.

__\[ALTERADA \- CH15889\_2018 \(MFS\-19894\)\]__

- Para um Documento Fiscal de Saída \(Campo MOVTO\_E\_S = 9\), além das regras gerais, __desconsiderar__:

Modelo \(campo 13 da SAFX07\) igual a “29”, ou seja, essas notas ficais não deverão compor no registro A100 e filhos\.

	

- Para um Documento Fiscal de Entrada \(Campo MOVTO\_E\_S <> 9\), além das regras gerais, considerar:

__Data de Lançamento PIS/COFINS:__ o campo Data do Lançamento \(campo 247 \- DAT\_LANC\_PIS\_COFINS da SAFX07 ou campo 81 \- DAT\_LANC\_PIS\_COFINS da SAFX09\)\* deve estar preenchido com uma data que esteja entre a Data Inicial e Data Final de geração do arquivo\.

\* Para recuperação das notas de entrada considerar o informado no parâmetro “Registro A100, C100, C190, C395, C500, D100 e D500 \- Seleção das Operações Geradoras de Crédito / Considerar para filtro da Data de Lançamento do EFD PIS/COFINS” disponível na tela de Dados Iniciais\.

__Se no parâmetro indicado for preenchida a opção “Capa NF”__, serão selecionados os registros considerando como critério a Data de Lançamento informada na SAFX07\.

__Se no parâmetro indicado for preenchida a opção “Item NF”__, serão selecionados os registros considerando como critério a Data de Lançamento informada na SAFX09\. Neste caso, se for identificada alguma NF cuja data não tenha sido preenchida na SAFX09, mas esteja preenchida na SAFX07 e esteja no período, também deve ser considerada\.

Observação: Quando houver o preenchimento da data de lançamento na capa e no item da nota fiscal com períodos distintos não haverá tratamento pelo sistema, não pode haver lançamento na capa nesse caso, apenas no item, ou seja, será aceito na geração apenas conteúdo VAZIO ou IGUAL, se houver preenchimento o sistema considerará e a geração estará incorreta, por esse motivo essa orientação será feita ao usuário no manual de layout de importação dos documentos fiscais e no manual operacional\.*  
*

*Exemplo: Data do Lançamento PIS/COFINS 15/07/2013 / Período de Geração: JUL/2013 – Neste exemplo a nota será gerada\.*

- __SE parâmetro Gera NF’s de Entrada sem Crédito = “Não”__ \(parâmetro da tela de geração\), considerar apenas registros cujo CST PIS ou CST COFINS \(campos 175 e 178 da SAFX08, campos 68 e 69 da SAFX09 ou campos 249 e 250 da SAFX07\) estejam preenchidos com conteúdo igual a 50, 51, 52, 53, 54, 55, 56, 60, 61, 62, 63, 64, 65, 66 ou 67\. Senão, considerar todos os CSTs\.

__Tratamento especial para notas canceladas:__

__\[ALTERADA – CH23991\_2014\]__

Quando se tratar de NF cancelada \(campo “30\-Situação da nota” = “S”\) somente poderá ser informado os campos IND\_OPER, campo IND\_EMIT, campo COD\_SIT, campo SER e campo NUM\_DOC\. Não deverão ser informados registros filhos \(A110,A111,A120 e A170\)\.

Além dos campos citados anteriormente, o campo COD\_PART é obrigatório nas operações de contratação de serviços, ou seja, campo IND\_OPER = 0\.

Obs\.: Incluir na importação a crítica para carga de SAFX07 com classificação “2” e com indicador de devolução\.

Atenção: Para a geração do registro A100, deve ser desprezados todos os documentos \(normais ou cancelados\) que possuem o campo modelo \(13 \- COD\_MODELO da SAFX07\) = ‘2D’

\[OS4316\-A\] __Tratamento para Geração de SCPs__

Quando a geração for realizada através da tela de "Geração dos Registros" do menu "Obrigações SCP", além da regra padrão de seleção, deve ser considerado:

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\.

\[OS4316\-C\] Observar a parametrização de "Dados Iniciais" \(menu: Parâmetros >> Dados Iniciais\) para geração ou não do registro\. Se houver um cadastro de "Dados Iniciais" cujo campo Código da SCP esteja preenchido para a SCP que o arquivo está sendo gerado e que o registro se enquadre no critério de geração, respeitar o parametrizado para a SCP\. Se não houver, considerar o cadastro de Dados Iniciais do Sócio Ostensivo \(Código da SCP não informada\) como valido também para a SCP para o qual o arquivo está sendo gerado\.

Para a geração do arquivo do Sócio Ostensivo, permanece como válido o registro cujo campo código da SCP não está preenchido\.

Dúvidas:

1 \- Se existirem itens com CST’s diferentes \(um com crédito e um sem crédito\) devemos levar a nota para o arquivo com seus valores totais ou apenas com os valores do item com crédito?

__Resposta:__ A NF será gerada com o valor total no A100 independente do critério de geração dos itens ser com ou sem crédito

OS4403/

CH28382

CH6594/2015

OS4816

CH6690/2017 \(MFS\-11222\)

MFS\- 547522

__RNA100\-02__

Campo IND\_OPER:

A partir do conteúdo do indicador de Entrada/Saída da nota \(campo 03\-Movimento Entrada/Saída da SAFX07\), verificar:

Se indicador de movimento E/S = 9 à gravar 1 \(Serviço Prestado no Estabelecimento\)

Se indicador de movimento E/S <> 9 à gravar 0 \(Serviço Contratado pelo Estabelecimento\)

__RNA100\-03__

Campo IND\_EMIT:

Este campo deve ser preenchido a partir do indicador de Entrada/Saída da nota \(campo 03\-Movimento Entrada/Saída da SAFX07\)\. 

Se indicador de movimento E/S = 1 à gravar 1 \(emissão terceira\)

Se indicador de movimento E/S = 2, 3, 4, 5,9 à gravar 0 \(emissão própria\)

__RNA100\-04__

Campo COD\_PART:

Para notas canceladas este campo não deverá ser informado\.

Para as notas representativas de operações de vendas a consumidor final \(SAFX09, campo 04 \- MOVTO\_E\_S = ‘9’ e cuja pessoa campo 08 \- ‘COD\_FIS\_JUR’ tenha no seu cadastro \(na SAFX4\), o campo 31 \- ‘IND\_CLIENTE\_SID’ preenchido com ‘S’\), este campo não deverá ser informado\.

\[OS4751\] Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

CH10603/2013

OS4751

__RNA100\-05__

Campo COD\_SIT:

Para o preenchimento deste campo deverão ser verificados alguns campos da SAFX07, conforme segue:

Se for nota cancelada \(campo “30\-Situação da nota” será = “S”\) à gravar “02”

Senão \(a nota é normal\) à gravar “00”

__RNA100\-06__

Campo SER:

 Para notas canceladas e campo “IND\_EMIT” igual a “1”  ou igual “0”, este campo deverá ser informado\.

__RNA100\-08__

Campo NUM\_DOC: 

Para notas canceladas e campo “IND\_EMIT” igual a “1” ou igual “0”, este campo deverá ser informado\.

\[26080/2015\] __Preenchimento do Campo:__

Se existir um registro na tela de “Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)” \(Modulo: Básicos >> Parâmetros / Menu: Preliminares >> Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)\) para o estabelecimento da NF de Serviço que está sendo gerada __E__ que tenha o campo Data Início menor ou igual a Data Fiscal da NF __E__ que tenha o campo NUM\_DOCFIS\_SERV preenchido, gerar aqui o conteúdo do campo NUM\_DOCFIS\_SERV\. Senão, preencher com o NUM\_DOCFIS\.

OS3341\-A4

26080/2015

__RNA100\-09__

Campo CHV\_NFSE:

Para notas canceladas este campo não deverá ser informado\.

__RNA100\-10__

Campo DT\_DOC:

Para notas canceladas este campo não deverá ser informado\.

__RNA100\-11__

Campo DT\_EXE\_SERV:

Para notas canceladas este campo não deverá ser informado\.

__RNA100\-12__

Campo VL\_DOC:

Para notas canceladas este campo não deverá ser informado\.

__RNA100\-13__

Campo IND\_PGTO:

A partir do conteúdo do tipo de faturamento \(campo 99\-Tipo de Faturamento da SAFX07\), verificar:

Se tipo faturamento = 1 \(a vista\)               à gravar “0”

Se tipo faturamento = 2 \(a prazo\)              à gravar “1”

Se tipo faturamento = 3 \(sem pagamento\) à gravar “9

Para notas canceladas este campo não deverá ser informado\.

__RNA100\-14__

Campo VL\_DESC:

Para as notas *sem* itens à o campo deve ser preenchido com o valor desconto da SAFX07 \(campo 28\-Valor Descontos\);

Para as notas *com *itens à deve\-se totalizar o valor do desconto de todos os itens da nota, considerando o campo “21\-Valor do Desconto” da SAFX09\.

Para notas canceladas este campo não deverá ser informado\.

__RNA100\-15__

Campo VL\_BC\_PIS:

Para as notas *sem* itens à o campo deve ser preenchido com o valor da base de cálculo PIS da SAFX07 \(campo 102\-Base PIS\);

Para as notas *com *itens à deve\-se totalizar o valor da base de cálculo PIS de todos os itens da nota, considerando o campo “46\-Base PIS” da SAFX09\.

Para notas canceladas este campo não deverá ser informado\.

__RNA100\-16__

Campo: VL\_PIS:

Para as notas *sem* itens à o campo deve ser preenchido com o valor do PIS da SAFX07 \(campo 103\-Valor PIS\);

Para as notas *com *itens à deve\-se totalizar o valor do PIS de todos os itens da nota, considerando o campo “48\-Valor PIS” da SAFX09\.

Para notas canceladas este campo não deverá ser informado\.

__RNA100\-17__

Campo VL\_BC\_COFINS:

Para as notas *sem* itens à o campo deve ser preenchido com o valor da base de cálculo COFINS da SAFX07 \(campo 104\-Base COFINS\);

Para as notas *com *itens à deve\-se totalizar o valor da base de cálculo COFINS de todos os itens da nota, considerando o campo “49\-Base COFINS” da SAFX09\.

Para notas canceladas este campo não deverá ser informado\.

__RNA100\-18__

Campo VL\_COFINS:

Para as notas *sem* itens à o campo deve ser preenchido com o valor da COFINS da SAFX07 \(campo 105\-Valor COFINS\);

Para as notas *com *itens à deve\-se totalizar o valor da COFINS de todos os itens da nota, considerando o campo “51\-Valor COFINS” da SAFX09\.

Para notas canceladas este campo não deverá ser informado\.

__RNA100\-19__

Campo VL\_PIS\_RET:

Para as notas *sem* itens à o campo deve ser preenchido com o valor do PIS retido da SAFX07;

Para as notas *com *itens à deve\-se totalizar o valor do PIS retido de todos os itens da nota\.

Para notas canceladas este campo não deverá ser informado\.

__RNA100\-20__

Campo VL\_COFINS\_RET:

Para as notas *sem* itens à o campo deve ser preenchido com o valor COFINS retido da SAFX07;

Para as notas *com *itens à deve\-se totalizar o valor COFINS retido de todos os itens da nota;

Para notas canceladas este campo não deverá ser informado\.

__RNA100\-21__

Campo VL\_ISS:

Para as notas *sem* itens à o campo deve ser preenchido com o valor do ISS da SAFX07 \(campo 46\-Valor ISS\);

Para as notas *com *itens à deve\-se totalizar o valor do ISS de todos os itens da nota, considerando o campo “33\-Valor ISS” da SAFX09\.

Para notas canceladas este campo não deverá ser informado\.

__Registro A110 – Informação Complementar da NF__

__RNG\-A110__

Nesse registro devem ser gravados os registros da SAFX112 relacionados ao documento gerado no registro A100 que atendam aos critérios abaixo:

Vinculação: \(campo ‘’15 – Vinculação da SAFX112\)	

             Igual a ‘’2 – EFD PIS/COFINS

Tipo de Observação: \(campo “13 – Tipo de Observação” da SAFX112\)

	Igual a “I \- Observação referente às Informações Complementares da Nota”

__RNA110\-01__

Campo COD\_INF:

Se o parâmetro “Justificar a esquerda”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da esquerda para direita\.

Se o parâmetro “Justificar a direita”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da direita para esquerda\. Esta opção deve estar por default selecionado\.

__Registro A111 – Processo Referenciado__

__RNG\-A111__

Nesse registro devem ser gravados os registros da SAFX114 relacionados ao documento gerado no registro A100 que atendam ao critério abaixo:

Vinculação: \(campo ‘’15 – Vinculação da SAFX112\)

             Igual a ‘’2 – EFD PIS/COFINS

Origem do Processo: \(campo “14 – Origem do Processo” da SAFX114\)

	Igual a “1 – Justiça Federal”, “3 – Secex/RFB” ou “9 – Outros”

Dúvidas: 1\- Criar indicador para diferenciar os processos referenciados do ICMS/IPI dos processos do PIS/COFINS nos registros da SAFX114?

__Resposta__: Criação de um campo para indicar que o processo refere\-se ao EFD PIS/COFINS

__Registro A120 – Operações de Importação__

__RNG\-A120__

Gerar um registro A120 para cada nota fiscal gravada no registro A100 que atenda às regras abaixo:

Movimento Entrada/Saída:

	Diferente de “9 – Saída”

UF da Pessoa Fis/Jur participante da NF:

	Igual a “EX”

Data do Pagamento da NF: \(campo 175 da SAFX07\)

	Entre a data inicial e data final de geração do arquivo

__Obs\.: __Se a NF possuir item, só devem ser considerados na geração desse registro os itens que tenham atendido à regra de geração das notas com item do registro A100\.

__RNA120\-02__

Campo VL\_TOT\_SERV:

Para as notas *sem* itens à o campo deve ser preenchido com o valor total do serviço da SAFX07 \(campo 22 \- Valor dos Produtos/Serviços\)\.

Para as notas *com *itens à deve\-se totalizar o valor total do serviço de todos os itens da nota, considerando o campo “15 \- Valor Total do Serviço” da SAFX09\.

__RNA120\-03__

Campo VL\_BC\_PIS:

Para as notas *sem* itens à o campo deve ser preenchido com o valor da base de Calculo PIS da SAFX07 \(campo 102 \- Base PIS\)\.

Para as notas *com *itens à deve\-se totalizar o valor da base de Calculo PIS de todos os itens da nota, considerando o campo “46 \- Base de Calculo PIS” da SAFX09\.

__RNA120\-04__

Campo VL\_PIS\_IMP:

Para as notas *sem* itens à o campo deve ser preenchido com o valor do PIS da SAFX07 \(campo 103 \- Valor PIS\)\.

Para as notas *com *itens à deve\-se totalizar o valor tributo PIS de todos os itens da nota, considerando o campo “48 \- Valor Tributo PIS” da SAFX09\.

__RNA120\-06__

Campo VL\_BC\_COFINS:

Para as notas *sem* itens à o campo deve ser preenchido com o valor da base de Calculo COFINS da SAFX07 \(campo 104 \- Base COFINS\)\.

Para as notas *com* itens à deve\-se totalizar o valor da base de Calculo COFINS de todos os itens da nota, considerando o campo “49 \- Base de Calculo COFINS” da SAFX09\.

__RNA120\-07__

Campo VL\_COFINS\_IMP:

Para as notas *sem* itens à o campo deve ser preenchido com o valor COFINS da SAFX07 \(campo 105 \- Valor COFINS\)\.

Para as notas *com *itens à deve\-se totalizar o valor COFINS de todos os itens da nota, considerando o campo “51 \- Valor Tributo COFINS” da SAFX09\.

__Registro A170 – Itens do Documento__

__RNG\-A170__

Gerar um registro A170 para cada item \(SAFX09\) da nota fiscal gravada no registro A100 que atenda às regras abaixo:

SE for um documento fiscal de saída:

Gerar um registro A170 para cada item \(SAFX09\) da nota fiscal gravada no registro A100 que tenha atendido às regras de geração das notas com itens

SE for um documento fiscal de entrada:

	SE parâmetro “Gera Itens sem Crédito” = ‘’N’’: \(parâmetro da tela de geração\)

Gerar um registro A170 para cada item \(SAFX09\) da nota fiscal gravada no registro A100 que tenha atendido às regras de geração das notas com itens

	SENÃO: \(parâmetro Gera Itens sem Crédito =’S’’\)

Além de gerar um registro A170 para cada item que tenha atendido às regras de geração das notas com itens do registro A100, gerar um registro A170 para os itens que tenham atendido parcialmente a essa regra, porque possuem CST PIS/COFINS = “70”, ‘’71’’, ‘’72’’, ‘’73’’, ‘’74’’,’’75’’, ‘’98’’ e ‘’99’’

Exceto documentos cancelados, onde o COD\_SIT = 02 \(cancelado\) não deverá ser informado registros filhos\. 

Dúvidas: Se uma mesma NF possui item com crédito e item sem crédito, devo levar os dois itens para o arquivo?

__Resposta__: *Serão considerados todos os itens do documento fiscal, quando qualquer um dos itens for gerador de crédito, conforme o email do Jonathan*

__RNA170\-03__

Campo COD\_ITEM:

Se parâmetro ‘Considerar o Indicador no Código do Item’, na tela de Dados Iniciais estiver marcado:

Se o parâmetro “Substituir o Código do Serviço pelo Código da Natureza do Serviço” estiver desmarcado \(nos dados iniciais\):

	Gravar a concatenação “S” \+ “\-“ \+ Código do Serviço

Senão \(se estiver marcado\)

	Gravar a concatenação “S” \+ “\-“ \+ Código da Natureza do Serviço

Se parâmetro ‘Considerar o Indicador no Código do Item’, na tela de Dados Iniciais estiver desmarcado:

Se o parâmetro “Substituir o Código do Serviço pelo Código da Natureza do Serviço” estiver desmarcado \(nos dados iniciais\):

	Gravar o Código do Serviço

Senão \(se estiver marcado\)

	Gravar o  Código da Natureza do Serviço

__RNA170\-07__

Campo NAT\_BC\_CRED:

Se o parâmetro “__Considerar a Natureza da Base de Crédito a partir dos Documentos__” estiver marcado \(nos dados iniciais\):

        Gravar o conteúdo do campo Natureza da Base de Crédito \(SAFX09\) informada no documento fiscal\.   

Senão \( se o parâmetro estiver desmarcado\)

\[__MFS76116__\] Tratamento p/ considerar a parametrização de Indicador da Natureza da Base do Crédito \(p/ Código de Serviço\) do Estabelecimento centralizado \(filial\)

Gravar o código da Natureza da Base de Cálculo do Crédito da tabela 4\.3\.7 através do parâmetro “Código do Serviço X Código da Base Cálculo do Crédito”, no menu Parâmetros \-> Identificador da Nat\. da Base de Crédito > Por Código de Serviço\. *\(campo COD\_PARAM da tabela PRT\_SERV\_MSAF for igual à ‘453’\)*  

__Tratamento__

 __   __O sistema deverá consultar também os Estabelecimentos centralizados \(Filiais\), __se__ o parâmetro “Por Código de Serviço” estiver parametrizado;

     __Preencher__ o campo com a __Natureza da Base de Crédito__ parametrizado para o Estabelecimento centralizado \(Filial\);

__Criar Log por Estabelecimento__: “COD\_ESTAB” – “NAT\_BC\_CRED”  \- Campo 07 \- NAT\_BC\_CRED preenchido conforme  parametrização do Estabelecimento centralizado \(filial\)\. Consultar o menu Parâmetros \-> Identificador da Nat\. da Base de Crédito > Por Código de Serviço __\(Essa mensagem deve ser apresentado somente 1 vez, por Estabelecimento\)\.__

__Senão __

__Preencher__ o campo com a __Natureza da Base de Crédito__ parametrizado para o Estabelecimento centralizador, conforme regra original \(Matriz ou Estabelecimento selecionado na tela de geração\); 

 

Se não existir parametrização nesse menu para o código de serviço em questão, verificar se existe parametrização no menu: Parâmetros > Identificador da Nat\. da Base de Crédito > Por CFOP __ou__ Por Extensões de CFOP\.

__\[ALTERADA – CH24679\_2017 \(MFS\-15805\)\]__

__Tratamento:__

- De acordo com o setor de Informação \(esclarecimento no item 21 do chamado 24679\) para receitas, ou seja, notas fiscais de saída, esse campo não deve ser preenchido, pois o mesmo deverá ser considerado apenas para crédito\. __*Observação:*__* Nós consideramos a alteração porque o contribuinte utiliza o mesmo código de serviço tanto para serviços tomados, quanto para serviços prestados, e o sistema está preenchendo o código da natureza da base de crédito no registro A170, para ambos os casos, o que está errado, pois a natureza da base crédito só deve ser informada nos serviços tomados \(Crédito\)\. Não se preenche o código da natureza da base de crédito para os serviços prestados, pois são Receitas\.*

__RNA170\-08__

Campo IND\_ORIG\_CRED:

Para o preenchimento deste campo deverá ser verificado:

Se for um documento fiscal de entrada

Movimento Entrada/Saída: \(campo 03 da SAFX07\)

		Diferente a “9 – Documento de Saída”

          Se a UF da pessoa fis/jur \(SAFX04\) relacionada no documento fiscal = EX à Gravar ‘’1’’ \(Operação de Importação\) Senão: Gravar ‘’0’’ \(Operação no Mercado Interno\)

SE for um documento fiscal de saída:

        Movimento Entrada/Saída: \(campo 03 da SAFX07\)

		Igual a “9 – Documento de Saída”

          Esse campo não deve ser preenchido, ou seja, deve gravar ||

__RNA170\-09__

Campo ALIQ\_PIS:

__\[Inclusão\-MFS564542\] Regra para Alíquota com 4 casas decimais após a virgula\.__

Portal SPED, a versão 5\.1\.0 – Alíquota 1,2375%, diferenciada

De acordo com a [NOTA AOS CONTRIBUINTES EFD\-CONTRIBUIÇÕES](http://sped.rfb.gov.br/pagina/show/7165) publicado em 02/03/2023, na possibilidade de crédito presumido na razão de 75% das alíquotas básicas da não cumulatividade de PIS/Cofins, todas as pessoas jurídicas que contratem serviço de transporte de carga prestados por transportadoras optantes pelo SIMPLES e pessoa física, transportador autônomo no caso da prestação se sujeitar à emissão de nota fiscal de serviço \(ISS\), segundo as regras vigentes da EFD\-Contribuições, a nota deve ser escriturada no bloco A, registros A100 e A170\.

Tratar o campo Alíquota PIS na TFIX71, para considerar as 4 casas decimais após a virgula\.

__Importante:__ Nessa situação o __VLR\_ALIQ\_PIS = 1,2375 \- __deve ser gerado com as 4 casas decimais após a virgula, sem arredondamento no arquivo\.

__\[Alteração \- MFS581831\] – Arquivo gerado até 31/12/2022\.__

Ajustar a regra na geração do arquivo, considerando apenas 2 casas decimais após a virgula, para os arquivos com data de até 31/12/2022\.

Arquivos com data superior a 31/12/2022, permanece com as 4 casas decimais após a virgula, sem arredondamento no arquivo\.

__Exemplo: 0,65 e ou 1,65__

__RNA170\-10__

Campo ALIQ\_COFINS:

__\[Inclusão\-MFS564542\] Regra para Alíquota com 4 casas decimais após a virgula\.__

Tratar o campo Alíquota COFINS na TFIX71, para considerar as 4 casas decimais após a virgula\.

__Importante:__ Nessa situação o __VLR\_ALIQ\_COFINS = 7,6000 \- __deve ser gerado com as 4 casas decimais após a virgula, sem arredondamento no arquivo\.

__\[Alteração \- MFS581831\] – Arquivo gerado até 31/12/2022\.__

Ajustar a regra na geração do arquivo, considerando apenas 2 casas decimais após a virgula, para os arquivos com data de até 31/12/2022\.

Arquivos com data superior a 31/12/2022, permanece com as 4 casas decimais após a virgula, sem arredondamento no arquivo\.

__Exemplo: 3,00 e ou 7,60__

