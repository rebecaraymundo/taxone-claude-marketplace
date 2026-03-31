# MTZ-RF_Conf_Balancete_XLS

- **Fonte:** MTZ-RF_Conf_Balancete_XLS.docx
- **Modificado:** 2026-03-11
- **Tamanho:** 101 KB

---

THOMSON REUTERS

__Módulo Report Fiscal__

__  __

__Relatório de Balancetes \- Formato XLS__

__Localização__: Menu Básicos, Módulo Report Fiscal, item Gerenciais à Contábil à Geral à Balancete \- Formato XLS

__Localização:__ MastersafDW >> SPED >> Escrituração Contábil Digital>> Relatórios>> Conferência \(Saldos x Movimentos\)

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS36831

Andréa Rocha

Este documento tem como objetivo criar o relatório do balancete em formato XLS

15/05/2020

MFS37618

Andréa Rocha

Este documento tem como objetivo incluir a opção de demonstrar o saldo das contas sintéticas a partir dos saldos das contas analíticas\.

22/06/2020

MFS40185

Andréa Rocha

Este documento tem como objetivo incluir a opção de demonstrar os valores discriminados por estabelecimento ou todos consolidados\.

08/07/2020

MFS\-46761

Alessandra Cristina Navatta

Disponibilizar o relatório também no SPED Contábil

18/11/2020

MFS\-47857

Andréa Rocha

Este documento tem como objetivo incluir dois novos parâmetros na tela, um para demonstrar as contas zeradas e o outro para demonstrar o Saldo Antes do Encerramento\.

15/12/2020

MFS\-66964

Rogério Ohashi

Este documento tem como objetivo criar o relatório de Conferência de Erros em formato XLS, referente ao problema das Contas Sintéticas \(Erro não previsto pelo Sistema\)\.

02/07/2021

MFS\-72085

Rogério Ohashi

Este documento tem como objetivo incluir o erro “quando é informado a própria conta contábil como conta sintética” \(Erro não previsto pelo Sistema\) no relatório de Conferência de Erros em formato XLS\.

08/09/2021

MFS\-1053380

MFS\-1062301

Lyene Benvenutti

Esclarecimento acerca dos valores que devem ser exibidos nas colunas “saldo anterior”, “ind\. saldo anterior”, “débitos”, “créditos”, “saldo atual” e “ind\. saldo atual”\.

11/03/2026

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

Seu objetivo é a conferência do balancete, gerado em formato XLS\.

__\[MFS\-66964\]__

Criação do Relatório de Conferência de Erros, gerado em formato XLS, referente ao Erro não previsto pelo Sistema, em relação a informação do Campo 06 \- COD\_CONTA\_SINT da tabela X2002\_PLANO\_CONTAS\.

__RN01__

__                                                        Parâmetros de Tela__

__Data Inicial __– Neste campo o usuário informará uma data inicial, a ser utilizada como filtro dos documentos fiscais\.

__Data Final __–__ __Neste campo o usuário informará uma data final, a ser utilizada como filtro dos documentos fiscais

__Tipo Balancete__ – Este campo é uma lista com as seguintes opções: “*Analítico*”, “*Sintético*” e “*Ambos*”\. Seu preenchimento é obrigatório\.

__\[MFS37618\]__ Inclusão do novo parâmetro

__Saldo das Contas Sintéticas __\- O parâmetro deve ser do tipo Radiobutton, com as opções:

     \- Calcular o saldo das contas sintéticas a partir do saldo das contas analíticas

     \- Utilizar o saldo mensal das contas sintéticas

__Obs\.: __Somente deve ser habilitado quando for escolhida a opção “Tipo de Balancete” igual a “Ambos”\.

__\[MFS40185\]__ Inclusão do novo parâmetro

__Estabelecimentos__ \- O parâmetro deve ser do tipo Radiobutton, com as opções:

     \- Discriminados

     \- Todos Consolidados

__Obs\.: __Somente deve ser habilitado quando for escolhida a opção “Saldo das Contas Sintéticas” igual a “Calcular o saldo das contas sintéticas a partir do saldo das contas analíticas”\.

__\[MFS47857\]__ Inclusão de dois novos parâmetros

__Demonstrar Contas Zeradas \- __O parâmetro deve ser do tipo checkbox, sendo o default desmarcado\.

__Saldo Antes do Encerramento \- __O parâmetro deve ser do tipo checkbox, sendo o default desmarcado\.

__Estabelecimentos__ – Neste campo serão disponibilizados para seleção do usuário todos os estabelecimentos da Empresa do login\.

__RN02__

__                                                    Recuperação dos Dados__

__Origem dos dados__: Tabelas dos Saldos Mensais \(SAFX02\), Saldos Contábeis para Centro Custo \(SAFX80\) e Plano de Contas \(SAFX2002\)\.

Critérios de recuperação dos saldos na SAFX02/SAFX80:

     \- COD\_EMPRESA – código da empresa do  login

     \- COD\_ESTAB – estabelecimentos selecionados em tela 

     \- DATA\_SALDO – data fiscal que se enquadre no período informado em tela 

     \- Tipo de Balancete – se parâmetro = “Analítico” à serão consideradas apenas as contas da SAFX2002 em que o Indicador da conta seja de Conta Analítica \(IND\_CONTA = “A”\);

                                 se parâmetro = “Sintético”à serão consideradas apenas as contas da SAFX2002 em que o Indicador da conta seja de Conta Sintética \(IND\_CONTA = “S”\);

                                 se parâmetro = Ambos à serão consideradas todas as contas;

__\[MFS37618\]__ Inclusão do novo parâmetro

Parâmetro: Saldo das Contas Sintéticas

Quando for escolhida a opção “Utilizar o saldo mensal das contas sintéticas”, o funcionamento atual do relatório se mantém, gerando o saldo das contas sintéticas a partir da tabela de Saldo Mensal \(SAFX02 ou SAFX80\)\.

Quando for escolhida a opção “Calcular o saldo das contas sintéticas a partir do saldo das contas analíticas”, o relatório deve gerar os valores consolidados \(Saldo Inicial, Débito, Crédito e Saldo Atual\) das Contas Analíticas referentes à Conta Sintética superior, utilizando os níveis, ou seja, os valores das contas analíticas devem ser totalizados e mostrados na sua respectiva conta sintética\. 

Para cada conta analítica \(campo 4 = “A” da SAFX2002\) mostrada no relatório, verificar se ela tem uma conta sintética \(campo 6 da SAFX2002\) relacionada, se possuir, deve\-se mostrar no relatório a conta sintética relacionada às contas analíticas, ou seja, a conta sintética deve vir acima das suas respectivas contas analíticas, demonstrando o total dos valores das contas analíticas\.  Para relacionar as contas sintéticas às contas analíticas, deve\-se observar o nível de cada conta \(campo 8 da SAFX2002\) para demonstrá\-las no relatório, iniciando pela conta de menor nível \(nível = 1\)\.  Para as colunas de Saldo Inicial e Saldo Atual, deve\-se utilizar o campo Débito/Crédito de cada uma, para calcular o total de cada saldo da conta sintética\.  As contas sintéticas não vão possuir dados na tabela de Saldo Mensal, os valores serão sempre calculados a partir dos valores das contas analíticas\.

Obs\.: O saldo das contas analíticas são recuperados da tabela de Saldo Mensal \(SAFX02\) ou da tabela de Saldos Contábeis para Centro Custo \(SAFX80\)\.

__\[MFS40185\]__ Inclusão do novo parâmetro

Parâmetro: Estabelecimentos

Quando for escolhida a opção “Discriminados”, o funcionamento atual do relatório se mantém, gerando o saldo das contas a partir da tabela de Saldo Mensal \(SAFX02 ou SAFX80\) por estabelecimento\.

Quando for escolhida a opção “Todos Consolidados”, o relatório deve gerar os valores consolidados \(Saldo Inicial, Débito, Crédito e Saldo Atual\) das Contas Analíticas referentes à Conta Sintética superior, utilizando os níveis, ou seja, os valores das contas analíticas devem ser totalizados e mostrados na sua respectiva conta sintética\. E também devem consolidar os valores de todos os estabelecimentos, os valores  \(Saldo Inicial, Débito, Crédito e Saldo Atual\) devem ser consolidados por Empresa e Conta Contábil\.

__\[MFS47857\]__ Inclusão de dois novos parâmetros

Parâmetro: Demonstrar Contas Zeradas

Quando este parâmetro for marcado, as contas contábeis que estão zeradas devem ser demonstradas no relatório, junto com as contas que possuem valores \(saldo/débito/crédito\)\.  Caso contrário, as contas zeradas, ou seja, as contas que não possuem valor de saldo, nem valor de débito e nem de crédito, não devem ser demonstradas no relatório\.

Parâmetro: Saldo Antes do Encerramento

Quando este parâmetro for marcado, será realizado o cálculo abaixo\.  Caso contrário, a geração do relatório não terá alteração\.

Para cada conta, buscar na X01\_CONTABIL todos os lançamentos de encerramento que estiverem dentro do período de geração do balancete e que pertencerem à empresa e estabelecimento selecionados na tela de geração \(podem existir vários lançamentos de encerramento para uma mesma conta por que o encerramento pode ser feito por centro de custo\)\. Depois de recuperados os lançamentos, sumarizar os valores encontrados \(total de créditos – total de débitos\) e o resultado dessa sumarização é o valor a ser demonstrado no relatório para aquela conta\. Além do valor, o balancete deve demonstrar também o indicador \(débito ou crédito\), o indicador do saldo antes do encerramento será sempre o inverso do resultado da sumarização dos lançamentos de encerramento, ou seja, se após a sumarização obteve\-se um valor de R$1000,00 a Crédito, no relatório será apresentado R$1000,00 a Débito\.

__RN03__

__                                                         Processamento __

__\[MFS40185\]__ Inclusão do novo parâmetro

Parâmetro: Estabelecimentos = “Discriminados”

Os dados recuperados serão agrupados por Estabelecimento, e para cada Estabelecimento, será gerado um arquivo no formato XLS\.

Os dados serão ordenados por Empresa, Estabelecimento, Data do Saldo e Conta Contábil

Parâmetro: Estabelecimentos = “Todos Consolidados”

Os dados recuperados serão agrupados por Empresa, será gerado um arquivo no formato XLS\.

Os dados serão ordenados por Empresa, Data do Saldo e Conta Contábil

__RN04__

__                                                Preenchimento dos Dados __

__Empresa__

Código da empresa do login

__Estabelecimento__

__\[MFS40185\]__ Inclusão do novo parâmetro

Se Parâmetro Estabelecimentos = “Discriminados”

   Código do estabelecimento da tabela Estabelecimento

Senão 

   Esta coluna não será gerada\.

__Razão Social __

__\[MFS40185\]__ Inclusão do novo parâmetro

Se Parâmetro Estabelecimentos = “Discriminados”

     Razão social da tabela Estabelecimento

Senão 

     Esta coluna não será gerada\.

__CNPJ__

__\[MFS40185\]__ Inclusão do novo parâmetro

Se Parâmetro Estabelecimentos = “Discriminados”

      CNPJ da tabela Estabelecimento

Senão 

     Esta coluna não será gerada\.

__Insc\. Estadual__

__\[MFS40185\]__ Inclusão do novo parâmetro

Se Parâmetro Estabelecimentos = “Discriminados”

     Inscrição estadual da tabela Registro Estadual, referente a UF do estabelecimento

Senão 

     Esta coluna não será gerada\.

__Período Inicial__

Data inicial informada em tela

__Período Final__

Data final informada em tela

__Conta Número__

Código da conta contábil:

Se o saldo for da SAFX02 à campo 03\- Conta Contábil; 

Se o saldo for da SAFX80 à campo 04\- Conta Contábil;

__Descrição__

Descrição da conta \(campo 03 da SAFX2002\) referente a conta contábil

__Centro de Custo__

Centro de Custo:

Se o saldo for da SAFX02 à neste caso, a coluna não será preenchida; 

Se o saldo for da SAFX80 à campo 05\-Centro de Custo; 

__Saldo Anterior__

Saldo Anterior 

Se o saldo for da SAFX02 à campo 05\- Saldo Inicial; 

Se o saldo for da SAFX80 à campo 06\- Saldo Contábil Anterior;

__\[MFS\-1053380/MFS\-1062301\]__

Considerar a __data inicial__ informada em tela\.

__Ind\. Saldo Anterior__

Indicador de Débito/Crédito do Saldo Anterior 

Se o saldo for da SAFX02 à campo 06\- Débito/Crédito; 

Se o saldo for da SAFX80 à campo 07\-Crédito / Débito Anterior;

__\[MFS\-1053380/MFS\-1062301\]__

Considerar a __data inicial__ informada em tela\.

__Débitos__

Total do Débito 

Se o saldo for da SAFX02 à campo 10\- Total Débito; 

Se o saldo for da SAFX80 à campo 08\- Total Débito;

__\[MFS\-1053380/MFS\-1062301\]__

Considerar __a soma de todos os débitos__ ocorridos entre as datas inicial e final informadas em tela\.

__Créditos__

Total do Crédito 

Se o saldo for da SAFX02 à campo 09\- Total Crédito; 

Se o saldo for da SAFX80 à campo 09\- Total Crédito;

__\[MFS\-1053380/MFS\-1062301\]__

Considerar __a soma de todos os créditos__ ocorridos entre as datas inicial e final informadas em tela\.

__Saldo Atual__

Saldo Atual 

Se o saldo for da SAFX02 à campo 07\- Saldo Final; 

Se o saldo for da SAFX80 à campo 10\- Saldo Contábil Atual;

__\[MFS\-1053380/MFS\-1062301\]__

Considerar a __data final__ informada em tela\.

__Ind\. Saldo Atual__

Indicador de Débito/Crédito do Saldo Atual

Se o saldo for da SAFX02 à campo 08\- Débito/Crédito; 

Se o saldo for da SAFX80 à campo 11\-Crédito / Débito Anterior;

__\[MFS\-1053380/MFS\-1062301\]__

Considerar a __data final__ informada em tela\.

__Saldo Ant Encerramento__

__\[MFS47857\]__

Essa coluna só deve ser demonstrada no relatório, se o parâmetro “Saldo Antes do Encerramento” estiver marcado\.  

Saldo Antes do Encerramento 

campo 07\- Valor do Lançamento Contábil da SAFX01

__Obs__\.: Para maiores detalhes, consultar a regra do parâmetro “Saldo Antes do Encerramento”\.

__Ind\. Saldo Ant Encerramento__

__\[MFS47857\]__

Essa coluna só deve ser demonstrada no relatório, se o parâmetro “Saldo Antes do Encerramento” estiver marcado\.  

Indicador de Débito/Crédito do Saldo Antes do Encerramento

Preencher de acordo com o valor de lançamento da coluna “Saldo Ant Encerramento”\.

__Obs__\.: Para maiores detalhes, consultar a regra do parâmetro “Saldo Antes do Encerramento”\.

__RN05__

__   Exemplo do cálculo do saldo das contas sintéticas a partir do saldo das contas analíticas__

__\[MFS37618\]__ Inclusão do novo parâmetro

Exemplo:

__Relatório de Balancete__

 __Conta Contábil__

__Saldo Inicial__

__IND D/C__

__Débito__

__Crédito__

__Saldo Final__

__IND D/C__

__Indicador__

__da Conta__

__Nível__

1 \- Ativo

2300,00

D

3100,00

1700,00

3700,00

D

S

1

1\.1\- Ativo Circulante

1400,00

D

1500,00

800,00

2100,00

D

S

2

1\.1\.001 – Conta A

1100,00

D

800,00

300,00

1600,00

D

A

3

1\.1\.002 – Conta B

100,00

D

500,00

400,00

200,00

D

A

3

1\.1\.003 – Conta C

200,00

D

200,00

100,00

300,00

D

A

3

1\.2\- Ativo não Circulante

900,00

D

1600,00

900,00

1600,00

D

S

2

1\.2\.001 – Conta J

1000,00

D

900,00

500,00

1400,00

D

A

3

1\.2\.002 – Conta L

100,00

C

700,00

400,00

200,00

D

A

3

__Obs\.:__ As colunas de Indicador da Conta e Nível não são demonstradas no relatório, somente foram incluídas para exemplificar a geração das contas analíticas/sintéticas no relatório\.

__RN06__

__  Relatório de Conferência de Erro__

__\[MFS\-66964\]__ Inclusão de Relatório de Conferência de Erros – Contas Sintéticas inválidas e quando é informado a própria conta contábil como conta sintética

Parâmetros: Deverá ser gerado em tempo de execução do Relatório de Balancete XLS\.

__\[MFS\-72085\]__ Inclusão de Erro Não Tratado – Quando é informado a própria conta contábil como conta sintética

A necessidade de criação desse relatório se deve aos erros “não previsto pelo sistema” na geração do Relatório de Conferência do Balancete em Excel, causando o erro na geração, finalizando a geração em branco ou desconsiderando as contas contábeis com problema, para possibilitar a conferência do usuário, esses erros deverão ser “apontados” no novo “Relatório de Conferência de Erros”, e agrupados por Estabelecimento, a mesma regra da geração do Relatório de Balancete\. 

__Incluir__ no Relatório de Conferência de Erros os “Erros Não Previsto pelo Sistema” conforme relação abaixo:

__1 – Erro Conta Sintética Inválida:__ Quando as “Contas  Sintéticas” são inválidas \(inexistentes na tabela\) preenchidas no Campo 06 \- COD\_CONTA\_SINT da tabela X2002\_PLANO\_CONTAS causando o erro na geração;

Log de Mensagem: “A Conta Sintética informado no Campo 06 \- COD\_CONTA\_SINT da tabela X2002\_PLANO\_CONTAS é inválida ou inexistente, para correção do cadastro de Plano de Contas foi disponibilizado o Relatório “REL\_CONFERENCIA\_ERRO\.xls” na Aba “Arquivos”\. 

__Obs\.:__ O problema ocorre porque o Campo 06 \- COD\_CONTA\_SINT da tabela X2002\_PLANO\_CONTAS não é um campo chave \(*Foreign Key*\) possibilitando ao usuário excluir a Conta Sintética da tabela, ocasionando o erro, porém para não causar impactos a outros clientes, a opção adotada foi criar o Relatório de Erro\.

__2 – Erro Conta Sintética igual à Conta Contábil:__  Quando o Campo 01 \- COD\_CONTA da tabela X2002\_PLANO\_CONTAS for igual a conta contábil informado no Campo 06 \- COD\_CONTA\_SINT da tabela X2002\_PLANO\_CONTAS \(ocorre porque é informado a própria conta contábil como conta sintética, causando o erro não tratado\)\. 

Mensagem de Log: “A Conta Sintética informado no Campo 06 \- COD\_CONTA\_SINT da tabela X2002\_PLANO\_CONTAS é a própria Conta Contábil informado no Campo 02 – COD\_CONTA da tabela X2002\_PLANO\_CONTAS, para correção do cadastro de Plano de Contas foi disponibilizado o Relatório

“REL\_CONFERENCIA\_ERRO\.xls” na Aba “Arquivos”\.

__Obs\.:__ O problema ocorre porque o sistema permite que seja informado a própria conta contábil como conta sintética, caso a conta já tenha sido cadastrada/importada anteriormente\.

O Relatório de Conferência de Erros deverá ser disponibilizado no formato XLS para gravação na Aba “Arquivos”, somente quando for detectado o erro, e nesse caso não deverá ser disponibilizado o Relatório de Balancete para gravação\.

Nome do Arquivo: REL\_CONFERENCIA\_ERRO\.xls

O Relatório terá como base as informações do Cadastro do Plano de Contas, referente a conta contábil relacionada ao Saldo Contábil das tabelas SAFX02 e SAFX80, ou no caso dos Lançamentos antes do Encerramento a tabela SAFX01\.

Quando ocorrer o erro, criar Log de Mensagem na Aba “Log”:

__Preenchimento dos Dados do Relatório__

__Empresa__

Código da empresa do Login              \(Conforme Relatório de Balancete\)

__Estabelecimento__

Código de Estabelecimento                \(Conforme Relatório de Balancete\) 

Senão 

   Esta coluna não será gerada\.

__Conta Número__

Código da Conta Contábil            \(Informações da conta que ocasionou o Erro não Previsto pelo Sistema\)

__Validade Conta__

Validade da Conta Contábil         \(Informações da conta que ocasionou o Erro não Previsto pelo Sistema\)

__Descrição__

Descrição da Conta Contábil       \(Informações da conta que ocasionou o Erro não Previsto pelo Sistema\)

__Indicador da Conta__

Indicador da Conta Contábil        \(Informações da conta que ocasionou o Erro não Previsto pelo Sistema\)

__Natureza da Conta__

Natureza da Conta Contábil        \(Informações da conta que ocasionou o Erro não Previsto pelo Sistema\)

__Nível__

Nível da Conta Contábil               \(Informações da conta que ocasionou o Erro não Previsto pelo Sistema\)

__Situação__

Situação da Conta Contábil         \(Informações da conta que ocasionou o Erro não Previsto pelo Sistema\)

__Código Conta Sintética__

Código da Conta Sintética           \(Informações da conta que ocasionou o Erro não Previsto pelo Sistema\)

__Erro__

Mensagem de Log: O campo de “Código de Conta Sintética” Informado, não existente ou inválida na tabela de Plano de Contas\.

Mensagem de Log: O campo de “Código de Conta Sintética” é a mesma Informado no campo de Código de Conta Contábil\.

