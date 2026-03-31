# MTZ_DAPI-MG_Relatorio_Demonstrativo_Operacoes_Prestacoes

- **Fonte:** MTZ_DAPI-MG_Relatorio_Demonstrativo_Operacoes_Prestacoes.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 75 KB

---

THOMSON REUTERS

                                                                              __Módulo GIA – MG \(DAPI\-MG\)__

__                                      Relatório Demonstrativo das Operações / Prestações__

__Localização__: Menu Estadual, Módulo Obrigações Acessórias \- MG,  menu Relatórios 🡪 Demonstrativo das Operações/Prestações

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS4252

Novo relatório da GIA\-MG

Novo relatório “Demonstrativo das Operações/Prestações” detalhado por documento fiscal 

28/04/2014

\(criação do relatório\)

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

Este relatório demonstra as operações da DAPI a partir do __*Demonstrativo das Operações / Prestações *__*\(Q*uadros IV e V\), detalhados por documento fiscal, no mesmo formato apresentado na tela de consulta do demonstrativo \(menu ““Obrigações 🡪 DAPI 🡪 Manutenção 🡪 Demonstrativo das Operações/Prestações”\)\.

O objetivo do relatório é possibilitar a conferência dos documentos fiscais considerados na apuração de cada uma das operações\.

O relatório é gerado a partir das informações armazenadas durante a geração dos dados da DAPI \(menu “Obrigações 🡪 DAPI 🡪 Geração 🡪 Geração dos Registros”\)\. Para que o detalhamento das notas fiscais seja armazenado, é necessário que o parâmetro “*Gerar o detalhamento das NF’s p/o relatório Demonstrativo das Operações/Prestações”* seja selecionado na tela da geração\.

__RN01__

__                                                        Parâmetros de Tela__

__Mês/Ano de Referência__ 🡪 Mês e ano \(MM/AAAA\) para emissão do relatório\.

__Tipo de Operação__ 🡪 Este campo é uma lista com as seguintes opções:

  Entradas

  Saídas

  Todas

*Não* há opção default \(na abertura da tela a lista aparecerá em branco\)

__Selecionar Operação __🡪 Através deste campo o usuário informará se deseja ou não selecionar uma única operação para emissão do relatório\. 

Default = desmarcado\.

Enquanto desmarcado, o campo para seleção da operação ficará desabilitado\.

Se marcado, o campo para seleção da operação ficará habilitado, e o usuário poderá escolher um código na janela de seleção das operações\. A janela irá disponibilizar todas as operações existentes na TFIX42 \(tabela EST\_MG\_OPER\_CFOP\), mas mostrando uma única linha para cada operação\. 

*Obs: A TFIX42 é a parametrização das operações por CFOP \(menu “Obrigações 🡪 DAPI 🡪 Manutenção 🡪 Operações”\), e assim, existem várias linhas para cada operação, uma para cada CFOP parametrizado\.*

* *

*\(como a tabela não possui a descrição das operações serão exibidos apenas os códigos\)*

Além disso, será considerada também a informação do parâmetro “Tipo de Operação”, conforme descrito a seguir:

\- Se o tipo de operação informado = “Entradas” 🡪 serão disponibilizadas apenas as operações de entrada;

\- Se o tipo de operação informado = “Saídas” 🡪 serão disponibilizadas apenas as operações de saída;

\- Se o tipo de operação informado = “Todas” 🡪 serão disponibilizadas tanto as operações de entrada, como de saída;

Para identificar quando se trata de entrada ou saída, a TFIX42 tem um identificador \(IND\_ENT\_SAI, sendo 1 = entrada e 2 = saída\)\.

__Estabelecimentos __🡪 Serão exibidos para seleção do usuário todos os estabelecimentos da empresa do login cuja UF = MG\.

__RN02__

__                                     Recuperação e Processamento dos Dados__

__Origem dos dados: __Tabela dos documentos fiscais de cada operação dos Quadros IV e V da DAPI\. Estas informações são armazenadas durante a geração dos dados da DAPI \(menu “Obrigações 🡪 DAPI 🡪 Geração 🡪 Geração dos Registros”\), sempre que o parâmetro “*Gerar o detalhamento das NF’s p/o relatório Demonstrativo das Operações/Prestações”* for selecionado na tela da geração\.

*\(para consultar os detalhes da geração destes dados, ver o documento de regras “MTZ – DAPI – MG Geracao dos Registros”, item *__*RN12*__*\)*

Para cada estabelecimento selecionado em tela, será gerado um relatório\.

Para a recuperação dos dados, serão considerados:

  

Empresa

Empresa do login

Estabelecimento

Estabelecimento selecionado em tela

Mês e Ano de Referência          

Mês e ano informado em tela

Indicador do tipo de operação \(entrada ou saída\)

Dependendo do tipo de operação informado em tela, será considerada apenas a                                                                   movimentação das entradas \(linhas com o indicador = “1”\), apenas a movimentação das saídas \(linhas com indicador = “2”\), ou ambas\.

Código da Operação

Caso o usuário tenha selecionado uma operação em tela, será considerada apenas a movimentação desta operação \(linhas com o código da operação informada\)\.

Caso contrário, será considerada toda a movimentação que atenda aos parâmetros anteriores\. 

Os dados recuperados para cada Estabelecimento serão ordenados pelo código da operação, data de emissão e número da nota fiscal, e serão demonstrados de acordo com o layout anexo\.   

__RN03__

__                                           Preenchimento dos Dados no Relatório__

__Layout__ 🡪 ver planilha anexa “Layout Relatorio Demonstrativo Oper Prestacoes”

O formato deste relatório é o mesmo da consulta disponibilizada no menu “Obrigações 🡪 DAPI 🡪 Manutenção 🡪 Demonstrativo das Operações/Prestações”, sendo que para cada operação, é demonstrado o detalhamento das notas fiscais que compõe o total geral da operação\.

Observar que o layout das entradas \(aba “Entradas”\) é igual ao das saídas \(aba “Saídas”\), com as seguintes diferenças:

     1\-Nas linhas de título das operações internas, interestaduais e externas, muda o título “Entradas” por “Saídas”;

     2\-Nas linhas de totalização das operações internas, interestaduais e externas, muda o título “Entradas” por “Saídas”;

     3\-A coluna “Imposto Creditado” muda para “Imposto Debitado” quando se tratar das operações de saídas; 

     3\-Nas saídas __*não*__ existe a coluna “Imposto sem Aprov\. Crédito”;  

__Detalhes da emissão:__

\- Saltar página ao mudar das operações internas p/as interestaduais

\- Saltar página ao mudar das operações interestaduais p/as operações c/ exterior

\- Saltar página ao mudar o tipo de operação \(das entradas para as saídas\)

\- Os códigos de operação deste demonstrativo são subdivididos em operações internas, interestaduais e internacionais, como é

  demonstrado na tela de consulta \(menu ““Obrigações 🡪 DAPI 🡪 Manutenção 🡪 Demonstrativo das Operações/Prestações”\)\. As

  operações próprias de cada uma destas subdivisões são as seguintes:

                  __Entradas – Operações Internas__:

__Operação__

__Descrição__

16

Compras

17

Transferências

18

Devolução

19

Energia Elétrica

20

Comunicação

21

Transportes

22

Ativo Permanente

23

Uso Consumo

24

Outras

                  __Entradas – Operações Interestaduais__:

__Operação__

__Descrição__

26

Compras

27

Transferências

28

Devolução

29

Energia Elétrica

30

Comunicação

31

Transportes

32

Ativo Permanente

33

Uso Consumo

34

Outras

  

                  __Entradas – Operações c/Exterior__:

__Operação__

__Descrição__

36

Compras

37

Devolução

38

Com\./Transp\./Energia

39

Ativo Permanente

40

Uso Consumo

41

Outras

                  __Saídas – Operações Internas__:

__Operação__

__Descrição__

44

Vendas

45

Transferências

46

Devolução

47

Energia Elétrica

48

Comunicação

49

Transportes

50

Outras

                  __Saídas – Operações Interestaduais__:

__Operação__

__Descrição__

52

Vendas

53

Transferências

54

Devolução

55

Energia Elétrica

56

Comunicação

57

Transportes

58

Outras

  

                  __Saídas – Operações c/Exterior__:

__Operação__

__Descrição__

60

Vendas

61

Devolução

62

Com\./Transp\./Energia

63

Outras

__Ordenação dos Dados__ 🡪 Para cada tipo de entrada ou saída \(Internas, Interestaduais, ou Exterior\), as operações aparecerão ordenadas pelo código, e para cada operação, as notas aparecerão ordenadas por: data de emissão e número da nota\.

Segue conteúdo de cada uma das colunas do relatório:

__Cabeçalho:__

Primeira linha

Nesta linha serão impressas as seguintes informações: razão social da Empresa, data da emissão do relatório e a página\. 

Segunda linha

Nesta linha serão impressas as seguintes informações: código, razão social e a inscrição estadual do estabelecimento\. 

Terceira linha 

Nesta linha serão impressas as seguintes informações:

\- título do relatório

\- mês e ano de referência \(mês e ano informados em tela\)

\- tipo de operação \(tipo de operação informado em tela, que será: “Entradas”, “Saídas” ou “Todas”\)

\- operação \(código da operação informada em tela, e caso não exista, será impresso “Todas”\)

__Linha de cabeçalho das Operações Internas, Interestaduais ou Operações com Exterior:__

Entradas \- Operações Internas

Entradas \- Operações Interestaduais

Entradas \- Operações Exterior

Saídas \- Operações Internas

Saídas \- Operações Interestaduais

Saídas \- Operações Exterior

Esta linha inicia as operações de uma determinada categoria \(entradas internas, entradas interestaduais, entradas do exterior, saídas internas, etc \.\.\.\), de acordo com a lista descrita acima, no item “Detalhes da Emissão”\.

Cada uma destas linhas será demonstrada apenas quando existirem dados para o tipo de operação\. Caso contrário, não serão impressas, assim como a linha de total respectiva\. 

__Linha de cabeçalho de cada Operação:__

Operação

Esta linha inicia as notas fiscais de uma determinada operação\. 

Neste campo será impresso o código e a descrição da operação\.

Obs: como a TFIX42 *não* tem a descrição das operações, esta informação será tratada de acordo com a lista descrita acima, no item “Detalhes da Emissão” 

__Linhas de detalhe dos documento fiscais:__

Nota Fiscal

Todas estas informações são recuperadas da tabela que armazena os documentos fiscais de cada   operação dos Quadros IV e V da DAPI\.

Estas informações são geradas durante a geração dos dados da DAPI\-MG\. 

Para consultar os detalhes da geração destes dados, ver o documento de regras “*MTZ – DAPI – MG Geracao dos Registros*”, item __RN12__\. De acordo com a regra, cada documento processado na geração do Demonstrativo das Operações/Prestações, *gera uma linha na tabela*, com os valores correspondentes a cada coluna, e que compõe o total da operação\.

Data Emissão

Valor Contábil

Base de Cálculo

Imposto Creditado

ou

Imposto Debitado

Imposto sem Aprov\. Crédito

Isentas

Não Tributadas

Base Reduzida

Diferidas

Suspensas

Substituição Tributária

Outras

__Linhas dos totais de cada operação:__

Esta linha demonstra o total de cada operação, conforme demonstrado no layout anexo\.

__Linhas dos totais de cada tipo de entrada ou saída: \(entradas internas, interestaduais, etc \.\.\.\)__

Esta linha demonstra o total de cada um dos tipos de entradas ou saídas, conforme demonstrado no layout anexo:

\- Entradas \- Operações Internas

\- Entradas \- Operações Interestaduais

\- Entradas \- Operações Exterior

\- Saídas \- Operações Internas

\- Saídas \- Operações Interestaduais

\- Saídas \- Operações Exterior

	

        = = = = =

