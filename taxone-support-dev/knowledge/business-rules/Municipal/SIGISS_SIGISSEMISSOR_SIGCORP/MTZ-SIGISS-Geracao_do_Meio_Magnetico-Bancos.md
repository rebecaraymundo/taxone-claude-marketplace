# MTZ-SIGISS-Geracao_do_Meio_Magnetico-Bancos

- **Fonte:** MTZ-SIGISS-Geracao_do_Meio_Magnetico-Bancos.docx
- **Modificado:** 2026-01-29
- **Tamanho:** 33 KB

---

# SIGISS \- Geração do Meio Magnético \- Bancos

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3474

SIGISS \- Geração do Meio Magnético

Este documento tem como objetivo criar a geração para todos os municípios que são atendidos pelo SIGISS\. Dessa forma utilizaremos o módulo de Parâmetros por Município que servirá para o usuário realizar a parametrização de todos os municípios atendidos pelo SIGISS em um único lugar\. Além disso, também realizaremos a geração dos municípios através de uma única geração, ou seja, quando o cliente clicar em um município da SIGISS será exibida a mesma tela de geração do Meio Magnético\. 

Com essa OS também criaremos as obrigações para os municípios de Marília, Cianorte, Londrina e Sapiranga, entre outros\.

MFS\-1028037

Klemer Monteiro

Este documento tem como objetivo adicionar um novo município que é o de Santa Rita de Sapucaí/MG para o validador SIGISS\. 

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

__Regra p/ Geração do Meio Magnético – Bancos __

A tela Obrigações – Geração do Meio Magnético deve ser feita através de framework\. E deve conter as abas: 

Parâmetros: o sistema deve exibir os parâmetros de entrada da geração\.

Processos: o sistema deve exibir os processos já executados para essa geração\.

Log de Processo: o sistema deve exibir o log gerado durante a geração\.

Arquivo: o sistema deve exibir o arquivo que será gravado\. 

Para o arquivo de plano de contas, deve\-se gravar o seguinte nome:

__MOGIMIRIM\_BANCOS\_PLANO\_CONTAS\_DDMMAAAA\.txt__

     Onde:

__           DDMMAAAA__                                                           __Data Inicial da geração da DMS__

__           MOGIMIRIM\_BANCOS\_PLANO\_CONTAS          Obrigação que está sendo gerada – Plano de Contas__

      Exemplo: MOGIMIRIM\_BANCOS\_PLANO\_CONTAS\_01012010\.txt \(Ano: 2010, Mês: 01, Dia: 01\)

Para o arquivo de movimentação bancária, deve\-se gravar o seguinte nome:

__MOGIMIRIM\_BANCOS\_DDMMAAAA\.txt__

     Onde:

__           DDMMAAAA__                          __Data Inicial da geração da DMS__

__           MOGIMIRIM\_BANCOS          Obrigação que está sendo gerada__

      Exemplo: MOGIMIRIM\_BANCOS\_01012010\.txt \(Ano: 2010, Mês: 01, Dia: 01\)

__OS3474__

__RN02__

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

*Data Inicial:* deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

*Data Final:* deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

Gerar Arquivo de Plano de Contas: Esse campo deve ser um check Box, com as seguintes opções “S” ou “N”\. Por default, o campo deve ser exibido marcado \(“S”\)\.

Quando o campo estivar marcado \(= “S”\), o arquivo de plano de contas deve ser gerado\.

Quando o campo estivar desmarcado \(= “N”\), o arquivo de plano de contas não deve ser gerado\.

*Estabelecimento:* o sistema deve exibir os estabelecimentos pertencentes ao município de Mogi Mirim, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__OS3474__

__RN03__

__Regra p/ geração do arquivo magnético__

O formato utilizado pelo arquivo será texto plano em formato TXT\. As colunas serão delimitadas por PONTO E VIRGULA \(;\)

__OS3474__

__RN03\.a__

__Regra p/ Registro de Plano de Contas__

Recuperar apenas as contas que estão relacionadas às contas referenciais__ __cadastradas na tela Parâmetros – Serviços Bancários – Plano de Conta Referencial e estas parametrizadas aos serviços na tela de Plano de Contas x Códigos de Serviços, pertencentes à UF e município em questão\.

__OS3474__

__MFS\-1028037__

__RN04__

__Regra p/ Registro de Plano de Contas – CMC __

Preencher com o campo insc\_municipal da tabela estabelecimento para o estabelecimento selecionado no menu de geração\.

__OS3474__

__RN05__

__Regra p/ Registro de Plano de Contas – Código do Subtítulo Contábil__

Preencher com o campo Conta Contábil \(Campo cod\_conta da tabela x2002\_plano\_contas\)

__OS3474__

__RN06__

__Regra p/ Registro de Plano de Contas – Nome do Subtítulo Contábil__

Preencher com o campo Descrição \(Campo descrição da tabela x2002\_plano\_contas\)

__OS3474__

__RN07__

__Regra p/ Registro de Plano de Contas – Descrição do Subtítulo Contábil__

Preencher com o campo Descrição \(Campo descrição da tabela x2002\_plano\_contas\)

__OS3474__

__RN08__

__Regra p/ Registro de Plano de Contas – Conta COSIF__

Preencher com o campo cod\_conta\_ref da tabela sped\_contas\_ref relacionada à conta da tabela x2002\_plano\_contas\.

__OS3474__

__RN09__

__Regra p/ Registro de Plano de Contas – Item da Lista de Serviços__

Preencher com o campo Serviço Lei 116/03 da tela Parâmetros por município – Parâmetros – Serviços Bancários – Plano de Conta Referencial x Código de Serviços

__OS3474__

__RN10__

__Regra p/ Registro de Movimentação__

Recuperar a movimentação apenas das contas que estão relacionadas as contas referenciais__ __Parâmetros – Serviços Bancários – Plano de Conta Referencial e estas parametrizadas aos serviços na tela de Plano de Contas x Códigos de Serviços, pertencentes à UF e município em questão\.

__OS3474__

__RN11__

__Regra p/ Registro de Movimentação – CMC __

Preencher com o campo insc\_municipal da tabela estabelecimento para o estabelecimento selecionado no menu de geração e cadastrado na tela Parâmetros por município – Parâmetros – Serviços Bancários – Dados Cadastrais

__OS3474__

__RN12__

__Regra p/ Registro de Movimentação – Mês de Competência__

Preencher com campo data\_saldo da tabela x02\_saldos referentes ao período selecionado na tela de geração\.

Exemplo Formato mm\.

__OS3474__

__RN13__

__Regra p/ Registro de Movimentação – Ano de Competência__

Preencher com campo data\_saldo da tabela x02\_saldos referentes ao período selecionado na tela de geração\.

Exemplo Formato aaaa\.

__OS3474__

__RN14__

__Regra p/ Registro de Movimentação – Código do Subtítulo Contábil __

Preencher com campo cod\_conta da tabela x2002 desde que parametrizada na tela de Plano de Contas x Códigos de Serviços – Bancos\.

__OS3474__

__RN15__

__Regra p/ Registro de Movimentação – Valor__

Para a conta selecionada:

Caso o campo ident\_custo da tabela x2101\_contas\_ref\_ccusto esteja preenchido: preencher com campo vlr\_tot\_cre – vlr\_tot\_deb da tabela x80\_saldos\_ccusto

Caso o campo ident\_custo da tabela x2101\_contas\_ref\_ccusto não esteja preenchido: preencher com campo vlr\_tot\_cre – vlr\_tot\_deb da tabela x02\_saldos

Apenas devem ser considerados os valores para os centros de custos que foram parametrizados anteriormente\. 

__OS3474__

Considerações deste modelo:

__Quando uma Regra de Negócio for excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo descrita abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo descrita abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

