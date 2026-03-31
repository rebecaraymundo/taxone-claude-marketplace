# MTZ-Ressarc-RS-Geracao_Transferencia_entre_Apuracoes

- **Fonte:** MTZ-Ressarc-RS-Geracao_Transferencia_entre_Apuracoes.docx
- **Modificado:** 2021-01-14
- **Tamanho:** 106 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS 

\(IN\-RE 048/2018\) 

Geração da Transferência Entre Apurações 

__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS\-ST \- RS \(IN\-RE 048/2018\), itens:

Geração 🡪 IN\-RE 048/2018 🡪 Transferência entre Apurações

	

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS28013__

Liliane Videira Assaf

Geração da transferência entre apurações\.

23/08/2019

__MFS28013__

Liliane Videira Assaf

Inclusão de críticas e gravação da tabela APURACAO\. Ver marcações em verde\.

02/09/2019

Sumário

[1\.	Visão Geral da Solução	2](#_Toc18677447)

[2\.	Introdução	5](#_Toc18677448)

[3\.	Parâmetros da Tela	5](#_Toc18677449)

[4\.	Críticas	7](#_Toc18677450)

[5\.	Processamento	10](#_Toc18677451)

[5\.1 – Etapa 1: Limpeza dos lançamentos gerados por esse processo na SubapuraçãoRS e Apuração do ICMS\-ST	10](#_Toc18677452)

[5\.2 \-  Etapa 2: Recuperar o saldo credor ou devedor da Subapuração RS	11](#_Toc18677453)

[5\.3 – Etapa 3: Gerar lançamento para zerar o saldo na Subapuração do RS	12](#_Toc18677454)

[5\.4 – Etapa 4: Gerar o lançamento para transferir o saldo para a Apuração do ICMS de Substituição Tributária \(P9\-ST\)	14](#_Toc18677455)

[5\.5 – Etapa 5: Recalcular a Subapuração do RS	17](#_Toc18677456)

# <a id="_Toc18677447"></a>Visão Geral da Solução

O processo do cálculo do Ressarcimento/Complemento do RS está dividido em etapas:

1º : Geração dos Movimentos

2º : Transferência do ICMS\-ST da Subapuração para a Apuração do ICMS \(Substituição Tributária\)

3º : Execução da Apuração do ICMS \(P9\) para recalcular os totais do resumo da Substituição Tributária\.

4º : Geração do Sped Fiscal

__Primeira Etapa:__

Na primeira etapa, Geração dos Movimentos, os documentos fiscais são recuperados com base nas parametrizações por produtos sujeitos a ICMS\-ST \(Código, NCM, Cest\) e operações \(CFOP, CFOP/Natureza Operação\) disponíveis no módulo do Ressarcimento RS\. Como resultado desse processo a Subapuração RS é gerada\.

Durante esse processo, os valores de ajuste de ICMS\-ST são calculados para os documentos fiscais e consolidados para realização dos lançamentos na Subapuração RS\. A Subapuração, seus lançamentos e documentos vinculados aos lançamentos são base para a geração dos registros 1900, 1921, 1923 do SPED FISCAL\. 

<a id="_Hlk18344681"></a>Pré\-requisito:

Para que a Subapuração seja gerada, a parametrização em Dados Iniciais deve ser efetuada\. Nesta tela, serão definidos o número da Subapuração e informações dos itens da apuração a serem gerados\. Exemplo:

- Geração das Entradas 🡪 Item da Apuração  = 006 – Outros Créditos
- Geração das Saídas para Consumidor Final 🡪 Item da Apuração  = 002 – Outros Débitos
- Geração das Saídas para Outras Uf’s, Isentas ou não tributadas 🡪 Item da Apuração  = 003 – Estorno de Créditos

O resultado desta primeira etapa pode ser conferido através dos relatórios de conferências do movimento e da Subapuração disponíveis no módulo\.

__Segunda Etapa:__

Na seguda etapa,Transferência do ICMS\-ST da Subapuração para a Apuração do ICMS\-ST, o valor resultante da Subapuração, credor ou devedor do ICMS\-ST, é transferido para Apuração do ICMS\-ST\. 

Durante esse processo dois lançamentos são gerados:

- Um lançamento na SubApuração RS para estornar o valor transferido\. 
- Um lançamento na Apuração do ICMS\-ST para registrar o valor transferido\.

Ao final deste processo a Subapuração RS ficará sempre zerada\.

O resultado esta etapa pode ser conferido através do relatório da Subapuração e de transferências disponíveis no módulo\.

A apuração do ICMS\-ST deve ser consultada diretamente no módulo ICMS\.

<a id="_Hlk18344617"></a>__Terceira Etapa:__

Após a geração da transferência, a Apuração do ICMS deve ser executada para que os subtotais e totais de crédito e débito do Resumo da Substituição Tributária sejam recalculados\. Localização: módulo Estadual >> ICMS, item de menu DATA MART >> Apuração do ICMS\. 

Este procedimento já é adotado no DW, quando utliza\-se o Módulo Lançamentos Automáticos ICMS para gerar automaticamente lançamentos na apuração do ICMS e quando criamos manualmente lançamentos no módulo ICMS\. Em ambas as situações, após a criação dos lançamentos, a Apuração do ICMS deve ser executada\.

O Resumo da Apuração do ICMS\-ST serão recalculados a partir dos lançamentos\. Os valores dos lançamentos da tabela __ITEM\_APURAC\_SUBST__ são consolidados por código de operação, atualizando os códigos de operação do Resumo da Apuração do ICMS\-ST \(RESUMO\_APUR\_ST\)

<a id="_Hlk18344631"></a>__Quarta Etapa:__

A última etapa diz respeito à geração do SPED FISCAL, onde a Subapuração é demostrada nos registros do bloco 9 \(registros 1920, 1921, 1923\) e a apuração do ICMS\-ST no bloco E \(registros E210, E220\)

Tabelas que compõe a Subapuração: 

- Subapuração RS \(registro 1920\)
- Ajustes da Subapuração \(registro 1921\) 
- Identificação dos Documentos fiscais \(registro 1923\)

__Observação__:

A Subapuração gerada no módulo Ressarcimento do RS é diferente da Subapuração do ICMS gerada no módulo ICMS\. Cada módulo só enxerga sua Subapuração\. Ou seja a Subapuração do RS não é enxergada pelo módulo ICMS, e vice\-versa\. 

A decisão de fazermos a Subapuração RS separada da Subapuração do ICMS, se deu pelos seguintes motivos:

- A Subapuração do ICMS tem regras completamente diferentes da Subapuração RS\. O conceito da Subapuração do ICMS é completamente diferente da Subapuração do RS\. A Subapuração do ICMS foi criada para detalhar determinados incentivos fiscal de ICMS criados por alguns estados\. Já a Subapuração do RS foi criada para ICMS\-ST\.
- O lançamento complementar realizado na Subapuração do ICMS, é demonstrado na Apuração do ICMS Oficial \(P9\)\. Como a geração do Ressarmcimento RS gera lançamentos a crédito e a débito de ICMS\-ST na Subapuração RS,se não tratássemos de forma diferenciada da Subapuração do ICMS, todos esses lançamentos iriam aparecer na Apuração do ICMS Oficial, o que estaria incorreto\.

Ou seja mesmo tendo a Subapuração do ICMS e a Subapuração do RS sendo apresentadas no mesmo conjunto de registros do Sped Fiscal, as regras do cálculo das duas apurações são completamente diferentes\.  Por isso a Subapuração do RS foi criada completamente separada da Subapuração do ICMS, tanto processamento quanto o conjunto de tabelas que compõe a Subapuração\. Como consequencia desta decisão, os lançamentos a crédito e a débito gerados na Subapuração RS não podem ser alterados manualmente via tela de manutenção  do módulo ICMS \(menu Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração do ICMS >> Ajuste SINIEF ou Empresas c/ Inscr\. Estadual Única\)\. Como foi dito, cada módulo só manipula a Subapuração gerada por ele\. 

Veja a seguir, o conjunto de tabelas pertinente a cada uma das Sub\-Apurações\.

__Tabelas da APURAÇÃO ICMS__

__Tabelas da SUBAPURAÇÃO ICMS__

__Tabelas da SUBAPURAÇÃO RS__

__Tabelas da APURAÇÃO ICMS\-ST__

ITEM\_APURAC\_CALC

ICT\_SUB\_APURACAO

ICT\_SUB\_APURACAO\_RS

RESUMO\_APUR\_ST

ITEM\_APURAC\_DISCR

ITEM\_APURAC\_DISCR

ITEM\_APURAC\_SUBRS

ITEM\_APURAC\_SUBST

ITEM\_APURAC\_DISCR\_AJUSTE

ITEM\_APURAC\_DISCR\_AJUSTE

ITEM\_APURAC\_SUBRS\_AJUSTE

ITEM\_APURAC\_SUBST\_AJUSTE 

Base Legal: INSTRUÇÃO NORMATIVA RE Nº 048/18 

# <a id="_Toc18677448"></a>Introdução

Este processo consiste em transferir o saldo \(credor ou devedor\) da subapuração do período para a Apuração do ICMS\-ST\.

Para isso são gerados dois lançamentos, um na subapuração para zerar o seu resultado e outro na Apuração do ICMS\-ST, para creditar o imposto a restituir ou debitar o imposto a complementar\.

Pré\-requisito:

- Criar Calendário para a Apuraçao do ICMS – P9, no módulo Estadual >> Controle das Obriações Estaduais, item de menu Obrigações>> Calendário das Obrigações >> Por Estabelecimento\.
- Parametrizar  as informações para os lançamentos à complementar e restituir na tela de Dados Iniciais, disponível neste módulo\.
- Ter realizado a Geração dos Movimentos, disponível neste módulo\.

# <a id="_Toc18677449"></a>Parâmetros da Tela 

Período : \[ dd/aaaa \]

Geração por Inscrição Estadual Única \[ x \]

Estabelecimentos:

 \[ x \] xxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx      

 \[ y \] xxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx      

 \[    \] xxx \- xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Funcionamento dos campos:

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/__

__Default__

__Regra__

<a id="_Hlk517437550"></a>Período 

Data

\(mês e ano\)

S

S

\(MM/AAAA\)

Neste campo será informado o período \(mês e ano\) para a geração dos dados dos cupons fiscais\.

Deve ser um mês válido\.

Geração p/ Inscrição Estadual Ùnica

Check box

N

N

Não

O parâmetro de Geração p/ Inscrição Estadual Ùnica determina os estabelecimentos a serem apresentados\.

\(A inscrição estadual única será tratada na MFS\-29924, sprint 231\)

Estabelecimentos

Alfanumérico 

__S__

S

Neste campo é exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário\.

Serão disponibilizados para seleção apenas os estabelecimentos de RS \(UF do estabelecimento = RS\)\.

Selecionar

N

N

Esta opção é um facilitador que permite ao usuário selecionar um ou mais estabelecimentos através de uma janela de seleção da tabela de estabelecimentos\.

O filtro dos estabelecimentos disponibilizados para seleção segue a mesma regra descrita para o campo “Estabelecimento”:

\- Somente Estabelecimentos da empresa do login;

\- Somente Estabelecimentos da UF de RS;

Quando esta opção é utilizada, após escolher os estabelecimentos e clicar no botão <OK> da janela de seleção, os estabelecimentos selecionados pelo usuário serão demonstrados no campo “Estabelecimentos” já marcados\. 

   

Marcar todos

N

N

Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados no campo “Estabelecimentos”\.

# <a id="_Toc18677450"></a>Críticas 

Os Pré\-requisitos para a geração da transferência são:

- Criar um calendário para a Apuraçao do ICMS – P9, no módulo Estadual >> Controle das Obriações Estaduais, item de menu Obrigações>> Calendário das Obrigações >> Por Estabelecimento\. 

O estabelecimento e período da geração da transferência deve possuir cadastro do Calendário para a Apuração do ICMS, utilizando como código da obrigação 108 ou 165\.

- Parametrizar  as informações para os lançamentos a complementar e restituir na tela de Dados Iniciais, disponível neste módulo\.
- Ter realizado a Geração dos Movimentos, disponível neste módulo

Antes de iniciamos, vamos checar se esse passos foram feitos\. Caso encontre alguma falha nestas verificações, o processo será abortado\.

Verificar se a Geração do Movimento foi realizada \(existência de Subapuração\):

Verificar se a Geração do Movimento foi realizada resultando na existência de uma subapuração para o estabelecimento e período\.

Para isso fazer uma consulta na Tabela do Resumo da Subapuração do RS \(ICT\_SUB\_APURACAO\_RS\), considerando os critérios:

- Empresa de login;
- Estabelecimento informado na tela de geração;
- Período  informado na tela de geração;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.  

                                          "165", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" marcado

Caso não encontre registro, exibir mensagem de erro no Log da Geração:

“*Não é possível realizar a transferência pois não existe subapuração para o estabelecimento e período informado\. Favor efetuar a Geração do Movimento\.” *

Verificar se o Calendário para Apuração do ICMS foi criado, no Módulo Controle das Obrigações Estaduais:

Verificar se existe calendário para a Apuração do ICMS – P9\.

O cadastro do Calendário das Obrigações está localizado no módulo Estadual >> Controle das Obriações Estaduais, item de menu Obrigações>> Calendário das Obrigações >> Por Estabelecimento\.

Verificar se existe Calendário da Obrigação Fiscal por Estabelecimento \(tabela CALEND\_OBRIGACAO\), considerando os critérios: 

- Empresa de login;
- Estabelecimento informado na tela de geração;
- Data da Apuração =Último dia do período informado na tela de geração;
- Obrigação Fiscal = “108”,  quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.

                               "165", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" marcado

Caso não encontre registro, exibir mensagem de erro no Log da Geração:

*“Não é possível realizar a transferência pois não existe Calendário para a Apuração do ICMS – P9 para o estabelecimento e período informados\. Favor criar o calendário, no módulo Estadual >> Controle das Obriações Estaduais, menu Obrigações>> Calendário das Obrigações >> Por Estabelecimento\.”*

Verificar o Status da Apuração do ICMS

Para realizar a geração da transferência, caso exista Apuração do ICMS realizada para o estabelecimento, período e livro \(108 ou 165\), esta não pode estar encerrada\.

Para isso vamos consultar o Status da Obrigação Fiscal \(tabela APURACAO\), no módulo Estadual >> ICMS, item de menu Manuteção >> Status das Obrigações\. Considerar os seguintes critérios:

- Empresa de login;
- Estabelecimento informado na tela de geração;
- Data da Apuração =Último dia do período informado na tela de geração;
- Obrigação Fiscal = “108”,  quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.

                               "165", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" marcado

Caso a apuração esteja com Situação = “Apuração Realizada” \(campo IND\_SITUACAO\_APUR = ‘2’\) e Validade = “Válido” \(campo IND\_VALID\_APUR = ‘2’\), então exibir mensagem de erro no Log da Geração:

*“Não é possível realizar a transferência pois a Apuração do ICMS – P9 encontra\-se encerrada para o estabelecimento e período informados\. Favor reabrir a apuração, no módulo Estadual >> ICMS, menu Manutenção>> Status das Obrigações\.”*

TABELA: Apuracao 

ind\_situacao\_apur 

ind\_valid\_apur

1 \- Não Apurado

2 \- Apuracao realizada

5 \- Apuracao reaberta

1 \- Não analizado

2 \- Válida

3 \- Não válida

Acontecendo qualquer erro, finalizar a geração com status = “\-1” – Erro\.

Paramentrização dos Dados Iniciais:

Verificar se existe parametrização dos Dados Iniciais para a Empresa e Estabelecimento foco da geração\.

Para esta geração, são necessárias as parametrizações que definem os lançamentos de transferência na Subapuração e na Apuração do ICMS\-ST:

Na Subapuração:

- Lançamento do Estorno de Crédito do Valor a Restituir
- Lançamento de Dedução do Valor a Complementar

Na Apuração do ICMS\-ST:

- Lançamento de Outros Débitos do Valor a Complementar
- Lançamento de Outros Créditos do Valor a Restituir 

Se não for encontrada parametrização dos Dados Iniciais, exibir a seguinte mensagem no Log da Geração:

*Faltou realizar parametrização dos Dados Iniciais para o estabelecimento”\.*

Se não for encontrado “Descrição do Lançamento” ou  “Código de Ajuste” do Lançamento de Estorno de Crédito do Valor a Restituir, exibir a seguinte mensagem no Log da Geração:

*“Não foi informado Descrição do Lançamento ou Código de Ajuste do Lançamento de Estorno de Crédito do Valor a Restituir para o Estabelecimento\. Favor realizar parametrização dos Dados Iniciais”\.*

Se não for encontrado “Descrição do Lançamento” ou  “Código de Ajuste” do Lançamento de Dedução do Valor a Complementar, exibir a seguinte mensagem no Log da Geração:

*“Não foi informado Descrição do Lançamento ou Código de Ajuste do Lançamento de Dedução do Valor a Complementar para o Estabelecimento\. Favor realizar parametrização dos Dados Iniciais”\.*

Se não for encontrado “Descrição do Lançamento” ou  “Código de Ajuste” do Lançamento de Outros Débitos do Valor a Complementar, exibir a seguinte mensagem no Log da Geração:

*“Não foi informado Descrição do Lançamento ou Código de Ajuste do Lançamento de Outros Débitos do Valor a Complementar para o Estabelecimento\. Favor realizar parametrização dos Dados Iniciais”\.*

Se não for encontrado “Descrição do Lançamento” ou  “Código de Ajuste” do Lançamento de Outros Créditos do Valor a Restituir, exibir a seguinte mensagem no Log da Geração:

*“Não foi informado Descrição do Lançamento ou Código de Ajuste do Lançamento de Outros Créditos do Valor a Restituir para o Estabelecimento\. Favor realizar parametrização dos Dados Iniciais”\.*

Acontecendo qualquer erro, finalizar a geração com status = “\-1” – Erro\.

# <a id="_Toc18677451"></a>Processamento

## <a id="_Toc18677452"></a>5\.1 – Etapa 1: Limpeza dos lançamentos gerados por esse processo na SubapuraçãoRS e Apuração do ICMS\-ST 

Nesta etapa vamos eliminar os lançamentos de transferência, gerados em processamentos anteriores\.

__Eliminação do Lançamento na Tabela de Ajustes da Subapuração RS \(ITEM\_APURAC\_SUBRS\)__

Identificar o lançamento com os critérios abaixo:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Códigos dos estabelecimentos selecionados em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.  

                                          "165", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" marcado

- Indicador de Lançamento Digitado/calculado  \(ind\_dig\_calculado\) = __‘5’__ \- lançamento gerado via processo de transferência

__Eliminação do Lançamento na Tabela de Lançamentos da Apuração do ICMS\-ST \(ITEM\_APURAC\_SUBST\)__

Identificar o lançamento com os critérios abaixo:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Códigos dos estabelecimentos selecionados em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.  

                                          "165", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" marcado

- Indicador de Lançamento Digitado/calculado  \(ind\_dig\_calculado\) = __‘5’__ \- lançamento gerado via processo de transferência

__Recalcular a Subapuração do RS__

Após a limpeza dos lançamentos, a Subapuração do RS deve ser recalculada, para que os valores do Saldo Credor / Devedor zerados pela execução da Transferência, voltem aos valores resultantes da Geração do Movimento\.

Este procedimento já é realizado na Geração dos Movimentos \(vide documentos matrizes iniciados por “MTZ\-Ressarc\-RS\-Geracao\_Movimentos”\) e está descrito em detalhes na etapa 5 deste documento\.

## <a id="_Toc18677453"></a>5\.2 \-  Etapa 2: Recuperar o saldo credor ou devedor da Subapuração RS

Nesta etapa vamos recuperar os valores das linhas ”Saldo Credor a Transportar” e “ICMS a Recolher” da Subapuração do RS\.

A Subapuração está disponível para conferência no menu Relatório >> Conferência dos Movimentos \(opção Subapuração\)\. 

__Origem dos dados__: \- Tabela do Resumo da Subapuração do RS \(ICT\_SUB\_APURACAO\_RS\);

__Critérios da recuperação: __

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Código do estabelecimento selecionado em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.  

                                          "165", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" marcado

Recuperar as informações:

ICMS a Recolher

Campo “__Valor total de ICMS a recolher”__ gravado na tabela de Tabela do Resumo da Subapuração do RS \(ICT\_SUB\_APURACAO\_RS – campo VLR\_ICMS\_RECOLHER\)\.

Saldo Credor a Transportar

Campo “__Valor total do Saldo credor a transportar para o período seguinte__” gravado na tabela de Tabela do Resumo da Subapuração do RS \(ICT\_SUB\_APURACAO\_RS \-  campo VL\_SLD\_CREDOR\_TRANSP\)\.

## <a id="_Toc18677454"></a>5\.3 – Etapa 3: Gerar lançamento para zerar o saldo na Subapuração do RS

O lançamento a ser gerado na subapuração tem como objetivo estornar o saldo credor ou devedor para zerar a subapuração\. Para isso aplicamos a regra abaixo:

Se a subapuração finalizar com saldo credor \(Saldo Credor a Transportar > 0\), então:

Realizar um lançamento com valor = Saldo Credor a Transportar, para estornar o crédito\. 

O item da apuração, a descrição do lançamento e o código de Ajuste necessários para realizar o lançamento, estão parametrizados em Dados iniciais como “Lançamento do Estorno de Crédito do Valor a Restituir”\.

Campos: COD\_OPER\_APUR\_RESS\_SUB, DSC\_ITEM\_APUR\_RESS\_SUB, COD\_AJUSTE\_ICMS\_RESS\_SUB da tabela EST\_ST\_RS\_DADOS\_INI\.

Se a subapuração finalizar com saldo devedor \(ICMS a Recolher > 0 \), então:

Realizar um lançamento com valor = ICMS a Recolher, para deduzir o débito\. 

O item da apuração, a descrição do lançamento e o código de Ajuste necessários para realizar o lançamento estão parametrizados em Dados iniciais como “Lançamento de Dedução do Valor a Complementar”\.

Campos: COD\_OPER\_APUR\_COMPL\_SUB, DSC\_ITEM\_APUR\_COMPL\_SUB, COD\_AJUSTE\_ICMS\_COMPL\_SUB da tabela EST\_ST\_RS\_DADOS\_INI

Se a subapuração finalizar zerada \(Saldo Credor a Transportar = 0 e ICMS a Recolher = 0\), 

Então não será realizado lançamento\.

__Gravação do Lançamento na Tabela de Ajustes da Subapuração RS \(ITEM\_APURAC\_SUBRS\)__

Esta tabela contém os lançamentos \(Ajustes\) da Subapuração de um estabelecimento e período, que serão apresentados no registro 1921 do SPED FISCAL\. 

Os campos sinalizados com asterisco compõem a chave da tabela\.

__PK__

__Campo__

__Nome na tabela__

__Regra de preenchimento__

__\*\*\*__

__Código da empresa__

COD\_EMPRESA

Código da empresa do login\.

__\*\*\*__

__Código do estabelecimento__

COD\_ESTAB

Código do estabelecimento selecionado em tela\.

__\*\*\*__

__Data da Apuração__

DAT\_APURACAO

Úlitmo dia do mes e ano do Período da informado na tela de geração\.

__\*\*\*__

__Código do Livro __

COD\_TIPO\_LIVRO

Se o opção “Gerar por Inscrição Estadual Única” estiver selecionada, então:

    Gravar o código ‘165’

Senão

    Gravar o código ‘108’

__\*\*\*__

__Identificador da Subapuração__

IND\_SUB\_APUR

Recuperar o código da SUBAPURAÇÃO cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\) para a empresa e estabelecimento foco da geração\.

__\*\*\*__

__Operação da Apuração__

COD\_OPER\_APUR

Recuperar o Código da Operação da Apuração cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\) para a empresa e estabelecimento foco da geração\.

Conforme explicado na regra acima, dependendo se o saldo da subapuração é credor ou devedor, considerar o Item da Apuração do “Lançamento do Estorno de Crédito do Valor a Restituir” ou do “Lançamento de Dedução do Valor a Complementar\.

__\*\*\*__

__Número do Lançamento__

NUM\_DISCRIMINACAO

Sequencial único por Subapuração/Operação da Apuração\. 

Ou seja recuperar o próximo número da seguencia de lançamentos da Subapuração/operação da Apuração que está sendo gerada, considerando a empresa, estabelecimento, data da apuração, código do livro, identificador da Subapuração e a operação da apuração\.

__Valor do Lançamento__

*\(campo 04 do registro 1921\)*

VAL\_ITEM\_DISCRIM

Conforme explicado na regra acima, dependendo se o saldo da subapuração é credor ou devedor, o valor que será gravado no lançamento será:

- Saldo Credor a Transportar 

ou

- ICMS a Recolher\.

__Descrição do Lançamento__

*\(campo 03 do registro 1921\)*

DSC\_ITEM\_APURACAO

Recuperar a Descrição do Lançamento cadastrada na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\) para a empresa e o estabelecimento foco da geração\.

Conforme explicado na regra acima, dependendo se o saldo da subapuração é credor ou devedor, considerar o Item da Apuração do “Lançamento do Estorno de Crédito do Valor a Restituir” ou do “Lançamento de Dedução do Valor a Complementar\.

__Código do Ajuste ICMS__

*\(campo 02 do registro 1921\)*

COD\_AJUSTE\_ICMS

Recuperar o Código de Ajuste Sped Fiscal cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\) para a empresa e o estabelecimento foco da geração\.

Conforme explicado na regra acima, dependendo se o saldo da subapuração é credor ou devedor, considerar o Item da Apuração do “Lançamento do Estorno de Crédito do Valor a Restituir” ou do “Lançamento de Dedução do Valor a Complementar\.

__Indicador do Tipo do Lançamento__

IND\_TIPO\_LANC

Gravar com __“3”\.__

Este valor signfica que o lançamento não possui documentos associados\.

__Indicador de Lançamento Digitado/calculado__

IND\_DIG\_CALCULADO

Gravar com “5”\.

__5 __– lançamento de processo de transferência\.

## <a id="_Toc18677455"></a>5\.4 – Etapa 4: Gerar o lançamento para transferir o saldo para a Apuração do ICMS de Substituição Tributária \(P9\-ST\)

O lançamento a ser gerado na Apuração do ICMS\-ST tem como objetivo receber o saldo credor ou devedor oriundo da subapuração\. Para isso aplicamos a regra abaixo:

Se a subapuração finalizar com saldo credor \(Saldo Credor a Transportar > 0\), então:

Realizar um lançamento com valor = Saldo Credor a Transportar, à crédito\. 

O item da apuração, a descrição do lançamento e o código de Ajuste necessários para realizar o lançamento, estão parametrizados em Dados iniciais como “Lançamento de Outros Créditos do Valor a Restituir”\.

Campos: COD\_OPER\_APUR\_RESS\_P9, DSC\_ITEM\_APUR\_RESS\_P9, COD\_AJUSTE\_ICMS\_RESS\_P9 da tabela EST\_ST\_RS\_DADOS\_INI\.

Se a subapuração finalizar com saldo devedor \(ICMS a Recolher > 0 \), então:

Realizar um lançamento com valor = ICMS a Recolher, à débito\. 

O item da apuração, a descrição do lançamento e o código de Ajuste necessários para realizar o lançamento estão parametrizados em Dados iniciais como “Lançamento de Outros Débitos do Valor a Complementar”\.

Campos: COD\_OPER\_APUR\_COMPL\_P9, DSC\_ITEM\_APUR\_COMPL\_P9, COD\_AJUSTE\_ICMS\_COMPL\_P9 da tabela EST\_ST\_RS\_DADOS\_INI

Se a subapuração finalizar zerada \(Saldo Credor a Transportar = 0 e ICMS a Recolher = 0\), 

Então não será realizado lançamento\.

__Gravação do Lançamento na Tabela de Lançamentos da Apuração do ICMS\-ST \(ITEM\_APURAC\_SUBST\)__

Esta tabela contém os lançamentos da Apuração do ICMS\-ST de um estabelecimento, período e UF, que serão apresentados nos registros do bloco E do SPED FISCAL\. 

Os campos sinalizados com asterisco compõem a chave da tabela\.

__PK__

__Campo__

__Nome na tabela__

__Regra de preenchimento__

__\*\*\*__

__Código da empresa__

COD\_EMPRESA

Código da empresa do login\.

__\*\*\*__

__Código do estabelecimento__

COD\_ESTAB

Código do estabelecimento selecionado em tela\.

__\*\*\*__

__Data da Apuração__

DAT\_APURACAO

Úlitmo dia do mes e ano do Período da informado na tela de geração\.

__\*\*\*__

__Código do Livro __

COD\_TIPO\_LIVRO

Se o opção “Gerar por Inscrição Estadual Única” estiver selecionada, então:

    Gravar o código ‘165’

Senão

    Gravar o código ‘108’

__\*\*\*__

__Identificador do Estado__

IDENT\_ESTADO

Identificador do Estado na tabela ESTADO para o código do estado = “RS”\.

__\*\*\*__

__Indicador da UF__

IND\_UF

Preencher com ‘1’, que significa mesma UF do estabelecimento\.

__\*\*\*__

__Operação da Apuração__

COD\_OPER\_APUR

Recuperar o Código da Operação da Apuração cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\) para a empresa e estabelecimento foco da geração\.

Conforme explicado na regra acima, dependendo se o saldo da subapuração é credor ou devedor, considerar o Item da Apuração do “Lançamento de Outros Créditos do Valor a Restituir” ou do “Lançamento de Outros Débitos do Valor a Complementar\.

__\*\*\*__

__Número do Lançamento__

NUM\_DISCRIMINACAO

Sequencial único por Operação da Apuração \(COD\_OPER\_APUR\)\. 

Ou seja recuperar o próximo número da seguencia de lançamentos da Operação da Apuração que está sendo gravada, considerando a empresa, estabelecimento, data da apuração, código do livro, identificador do Estado \(ident\_estado\), Indicador da UF \(ind\_uf\) e a operação da apuração\.

__Valor do Lançamento__

*\(campo 04 do registro 1921\)*

VAL\_ITEM\_DISCRIM

Conforme explicado na regra acima, dependendo se o saldo da subapuração é credor ou devedor, o valor que será gravado no lançamento será:

- Saldo Credor a Transportar 

ou

- ICMS a Recolher\.

__Descrição do Lançamento__

*\(campo 03 do registro 1921\)*

DSC\_ITEM\_APURACAO

Recuperar a Descrição do Lançamento cadastrada na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\) para a empresa e o estabelecimento foco da geração\.

Conforme explicado na regra acima, dependendo se o saldo da subapuração é credor ou devedor, considerar o Item da Apuração do “Lançamento de Outros Créditos do Valor a Restituir” ou do “Lançamento de Outros Débitos do Valor a Complementar\.

__Código do Ajuste ICMS__

*\(campo 02 do registro 1921\)*

COD\_AJUSTE\_ICMS

Recuperar o Código de Ajuste Sped Fiscal cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\) para a empresa e o estabelecimento foco da geração\.

Conforme explicado na regra acima, dependendo se o saldo da subapuração é credor ou devedor, considerar o Item da Apuração do “Lançamento de Outros Créditos do Valor a Restituir” ou do “Lançamento de Outros Débitos do Valor a Complementar\.

__Indicador do Tipo do Lançamento__

IND\_TIPO\_LANC

Gravar com __“3”\.__

Este valor signfica que o lançamento não possui documentos associados\.

__Indicador de Lançamento Digitado/calculado__

IND\_DIG\_CALCULADO

Gravar com “5”\.

__5 __– lançamento de processo de transferência\.

Demais campos não mencionados não precisam ser preenchidos

 __Gravação da Tabela de Status da Obrigação \(APURACAO\)__

Verificar se existe registro de Status da Obrigação Fiscal \(tabela APURACAO\), no módulo Estadual >> ICMS, item de menu Manuteção >> Status das Obrigações\. Considerar os seguintes critérios:

- Empresa de login;
- Estabelecimento informado na tela de geração;
- Data da Apuração =Último dia do período informado na tela de geração;
- Obrigação Fiscal = “108”,  quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.

                               "165", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" marcado

Caso não exista registro, criar um registro com as seguintes informações:

 Os campos sinalizados com asterisco compõem a chave da tabela\.

__PK__

__Campo__

__Nome na tabela__

__Regra de preenchimento__

__\*\*\*__

__Código da empresa__

COD\_EMPRESA

Código da empresa do login\.

__\*\*\*__

__Código do estabelecimento__

COD\_ESTAB

Código do estabelecimento selecionado em tela\.

__\*\*\*__

__Data da Apuração__

DAT\_APURACAO

Úlitmo dia do mes e ano do Período da informado na tela de geração\.

__\*\*\*__

__Código do Livro __

COD\_TIPO\_LIVRO

Se o opção “Gerar por Inscrição Estadual Única” estiver selecionada, então:

    Gravar o código ‘165’

Senão

    Gravar o código ‘108’

Situação

IND\_SITUACAO\_APUR

Preencher com ‘1’ – Não Apurado

Validade

IND\_VALID\_APUR

Preencher com ‘1’ – Não Analisado

Data da Realização

DAT\_REALIZACAO

Data da execução da geração\.

## <a id="_Toc18677456"></a>5\.5 – Etapa 5: Recalcular a Subapuração do RS

Neste etapa os valores do Resumo da Subapuração do RS serão recalculados a partir dos lançamentos\.

Os valores dos lançamentos da tabela __ITEM\_APURAC\_SUBRS__ são consolidados por código de operação, atualizando o Resumo da Subapuração RS \(tabela ICT\_SUB\_APURACAO\_RS\)\.

Este procedimento já é realizado na Geração dos Movimentos \(vide documentos matrizes iniciados por “MTZ\-Ressarc\-RS\-Geracao\_Movimentos”\)

<a id="_Toc14802388"></a>Gravação dos Dados na Tabela de Resumo da Subapuração RS \(ICT\_SUB\_APURACAO\_RS\)

<a id="_Hlk508706613"></a>Esta tabela contém os totais da Subapuração de um estabelecimento e período, que serão apresentados no registro 1920 do SPED FISCAL\. 

Os campos sinalizados com asterisco compõem a chave da tabela\.

__PK__

__Campo__

__Nome na tabela__

__Regra de preenchimento__

__\*\*\*__

__Código da empresa__

COD\_EMPRESA

Código da empresa do login\.

__\*\*\*__

__Código do estabelecimento__

COD\_ESTAB

Código do estabelecimento selecionado em tela\.

__\*\*\*__

__Data da Apuração__

DAT\_APURACAO

Úlitmo dia do mes e ano do Período da informado na tela de geração\.

__\*\*\*__

__Código do Livro __

COD\_TIPO\_LIVRO

<a id="OLE_LINK22"></a>Se o opção “Gerar por Inscrição Estadual Única” estiver selecionada, então:

    Gravar o código ‘165’

Senão

    Gravar o código ‘108’

__\*\*\*__

__Identificador da Subapuração__

IND\_SUB\_APUR

Recuperar o código da SUBAPURAÇÃO cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\) para o estabelecimento foco da geração\.

__Valor total dos débitos por “Saídas e prestações com débito do imposto”__

*\(campo 02 do registro 1920\)*

VLR\_TOT\_DEB

Gravar zero\.

Estes campo __sempre__ ficará zerado, pois nenhuma das gerações existentes no Módulo Ressarcimento RS utilizará este campo para armazenar seu resultado\. 

__Valor total de “Ajustes a débito”__

*\(campo 03 do registro 1920\)*

VLR\_OUT\_DEB

Este campo contém o resultado somatório dos  lançamentos gravados na tabela de Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\) considerando a empresa, estabelecimento, data da apuração, código do livro, identificador da Subapuração e a operação da apuração = ‘__002’__ – Outros Débitos\.

__OBS__: Conforme parametrização dos Dados Iniciais, ‘002’ é o código de operação destinado ao lançamento resultante do processo de Geração das Saídas para Consumidor Final\.

__Valor total de Ajustes “Estornos de créditos”__

*\(campo 04 do registro 1920\)*

VLR\_ESTORNO\_CRED

Este campo contém o resultado somatório dos  lançamentos gravados na tabela de Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\) considerando a empresa, estabelecimento, data da apuração, código do livro, identificador da Subapuração e a operação da apuração = ‘__003’__ – Estorno de Créditos\.

__OBS__: Conforme parametrização dos Dados Iniciais, ‘003’ é o código de operação destinado ao lançamento resultante do processo de Geração das Saídas para Outras UF’s\. 

     

__Valor total dos créditos por “Entradas e aquisições com crédito do imposto__

*\(campo 05 do registro 1920\)*

VLR\_TOT\_CRED

Gravar zero\.

Estes campo __sempre__ ficará zerado, pois nenhuma das gerações existentes no Módulo Ressarcimento RS utilizará este campo para armazenar seu resultado\.

__Valor total de “Ajustes a crédito”__

*\(campo 06 do registro 1920\)*

VLR\_OUT\_CRED

Este campo contém o resultado somatório dos  lançamentos gravados na tabela de Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\) considerando a empresa, estabelecimento, data da apuração, código do livro, identificador da Subapuração e a operação da apuração = ‘__006’__ – Outros Créditos\.

__OBS__: Conforme parametrização dos Dados Iniciais, o ‘006’ é o código de operação destinado ao lançamento resultante do processo de Geração das Entradas\.

__Valor total de Ajustes “Estornos de Débitos”__

*\(campo 07 do registro 1920\)*

VLR\_ESTORNO\_DEB

Este campo contém o resultado somatório dos  lançamentos gravados na tabela de Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\) considerando a empresa, estabelecimento, data da apuração, código do livro, identificador da Subapuração e a operação da apuração = ‘__007’__ – Estorno de Débito\.

__OBS__: Estes campo sempre ficará zerado, pois nenhuma das gerações existentes hoje no Módulo Ressarcimento RS utilizará este campo para armazenar seu resultado\.

__Valor total de “Saldo credor do período anterior”__

*\(campo 08 do registro 1920\)*

VLR\_SALDO\_CRED

Gravar zero\.

Estes campo sempre ficará zerado, pois nenhuma das gerações existentes no Módulo Ressarcimento RS utilizará este campo para armazenar seu resultado\.

__Valor do saldo devedor apurado__

*\(campo 09 do registro 1920\)*

VLR\_SLD\_APURADO

Se \(VLR\_TOT\_DEB   \+  VLR\_OUT\_DEB   \+   VLR\_ESTORNO\_CRED\) \-

     \(VLR\_TOT\_CRED \+  VLR\_OUT\_CRED \+  VLR\_ESTORNO\_DEB \+  VLR\_SALDO\_CRED\) __>__ 0 Então

       Gravar o campo VLR\_SLD\_APURADO com o resultado da expressão:

        \(VLR\_TOT\_DEB    \+  VLR\_OUT\_DEB   \+ VLR\_ESTORNO\_CRED\) \-

        \(VLR\_TOT\_CRED \+ VLR\_OUT\_CRED \+ VLR\_ESTORNO\_DEB \+ VLR\_SALDO\_CRED\)

Sentão

       Gravar o campo VLR\_SLD\_APURADO com zero\.

__Valor total de “Deduções”__

*\(campo 10 do registro 1920\)*

VLR\_TOT\_DED

Este campo contém o resultado somatório dos lançamentos gravados na tabela de Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\) considerando a empresa, estabelecimento, data da apuração, código do livro, identificador da Subapuração e a operação da apuração = ‘__012’__ – Deduções\.

__OBS__: Conforme parametrização dos Dados Iniciais, o ‘012’ é o código de operação destinado ao lançamento resultante do processo de Transferência entre apurações\.

__Valor total de "ICMS a recolher \(09\-10\)__

*\(campo 11 do registro 1920\)*

VLR\_ICMS\_RECOLHER

Se VLR\_SLD\_APURADO > 0, Então:\.

    Se VLR\_SLD\_APURADO \- VLR\_TOT\_DED > 0 Então:

          Gravar o campo VLR\_ICMS\_RECOLHER com o resultado da expressão:

          VLR\_SLD\_APURADO \- VLR\_TOT\_DED

    Senão

         Gravar o campo VLR\_ICMS\_RECOLHER com zero\.

Senão 

     Gravar o campo VLR\_ICMS\_RECOLHER com zero\.

__Valor total de “Saldo credor a transportar para o período seguinte”__

*\(campo 12 do registro 1920\)*

VL\_SLD\_CREDOR\_TRANSP

Se \(VLR\_TOT\_DEB   \+  VLR\_OUT\_DEB   \+   VLR\_ESTORNO\_CRED\) \-

     \(VLR\_TOT\_CRED \+  VLR\_OUT\_CRED \+  VLR\_ESTORNO\_DEB \+  VLR\_SALDO\_CRED\) __>__ 0 Então

         Gravar o campo VLR\_SLD\_CREDOR\_TRANSP com zero\.

Sentão

       Gravar o campo VLR\_SLD\_CREDOR\_TRANSP com o resultado da expressão:

        \(VLR\_TOT\_CRED \+ VLR\_OUT\_CRED \+ VLR\_ESTORNO\_DEB \+ VLR\_SALDO\_CRED\) \- 

        \(VLR\_TOT\_DEB    \+  VLR\_OUT\_DEB   \+ VLR\_ESTORNO\_CRED\) 

__Valores recolhidos ou a recolher, extraapuração\.__

*\(campo 13 do registro 1920\)*

VLR\_DEB\_ESP

Gravar zero\.

Estes campo sempre ficará zerado, pois nenhuma das gerações existentes no Módulo Ressarcimento RS utilizará este campo para armazenar seu resultado\.

	

= = = = = =

 

