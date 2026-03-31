# MTZ-Ressarc-RS-IN087_2020_Geracao_Lancamentos_Apuracoes

- **Fonte:** MTZ-Ressarc-RS-IN087_2020_Geracao_Lancamentos_Apuracoes.docx
- **Modificado:** 2023-06-14
- **Tamanho:** 132 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS

\(IN\-RE 087/2020\) 

Geração dos Lançamentos a Complementar e a Restituir nas Apurações do ICMS / ICMS\-ST 

__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS\-ST \- RS \(IN\-RE 048/2018\), itens:

Geração 🡪 IN\-RE 087/20 🡪 Geração dos Lançamentos a Complementar e a Restituir nas Apurações do ICMS / ICMS\-ST

	

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS76452__

Liliane Videira Assaf

Criação da rotina

03/12/2021

__MFS76452__

Liliane Videira Assaf

Inclusão do Recálculo dos Saldos

09/02/2022

__MFS89648__

Liliane Assaf

Atualização legal IN55/22:

Alteração no Lançamento Complementar ou a Restituir para tratar dois cenários:

\- Valor Médio Ponderado Móvel do último dia do mês negativo  \(19\.3\-A\.2\.2\.2\)

\- Quantidade final do último dia do mês zerada \(19\.3\-A\.2\.2\.3 da  na IN\-045/98\)

10/08/2022

__MFS96666__

Liliane Assaf

Atualização legal IN RE 96/22 \(jan\-2023\):

Tópico 19\.3\-A\.1\.12 da IN RE045/98: criação dos códigos RS101, \.\.\., RS156 e RS301, \.\.\., RS356, RS601, \.\.\., RS656 e RS801, \.\.\., RS856 para as saídas internas a consumidor final\.

07/12/2022

Sumário

[1\.	Introdução	1](#_Toc111215498)

[2\.	Parâmetros da Tela	1](#_Toc111215499)

[3\.	Críticas	1](#_Toc111215500)

[4\.	Processamento	1](#_Toc111215501)

[4\.1 – Etapa 1: Limpeza dos lançamentos gerados por esse processo nas Apurações do ICMS e do ICMS\-ST	1](#_Toc111215502)

[4\.2 \-  Etapa 2: Calcular o Valor para Lançamento \(a Complementar ou a Restituir\)	1](#_Toc111215503)

[4\.3 – Etapa 3: Gerar lançamento a Restituir	1](#_Toc111215504)

[4\.4 – Etapa 4: Gerar lançamento a Complementar	1](#_Toc111215505)

[4\.5 – Etapa 5: Compensar o Valor a Complementar	1](#_Toc111215506)

[4\.6 – Etapa 6: Recálculo dos Saldos da Apuração do ICMS e ICMS\-ST	1](#_Toc111215507)

[5\.	Relatório	1](#_Toc111215508)

# <a id="_Toc111215498"></a>Introdução

Este processo consiste em calcular o valor líquido a complementar ou a restituir e gerar os lançamentos complementares nas Apurações do ICMS\-ST e ICMS\.

O cálculo do valor líquido a complementar ou restituir é baseado no registro 1255 \(Tabela de Saldo Consolidado da Restituição/Complemento \- X304\_SALDO\_CONS\_RES\_COMP\_ICMS\) que é gerada pelo processo de Transferência dos Movimentos para a EFD Fiscal\.

Se o cálculo resultar num valor líquido a complementar o lançamento desse valor será realizado na Apuração de ICMS\-ST\. Se o resultado for um valor líquido a restituir o lançamento poderá ser na Apuração do ICMS ou do ICMS\-ST, o usuário irá escolher via parâmetro de tela\.

Quando o resultado for um valor líquido a complementar, pode\-se compensar o Valor a Complementar lançado na Apuração de ICMS\-ST, com o Saldo Credor da Apuração do ICMS\. O valor a compensar não pode ser superior ao valor a complementar e limita\-se ao saldo credor do ICMS\. A realização desta compensação se dá através de dois lançamentos: um lançamento de Estorno de Crédito na Apuração do ICMS e um lançamento a crédito na Apuração do ICMS\-ST\.

A execução dessa geração pode ser realizada antes ou depois da Apuração do ICMS \(Localização: módulo Estadual >> ICMS, item de menu DATA MART >> Apuração do ICMS\)\.

Caso a Apuração do ICMS não tenha sido realizada antes dessa geração, é imprescindível executá\-la após esta geração, para que o Status da Obrigação seja atualizado para Situação = Apuração Realizada e Validade = Não Analisada\.

Caso a Apuração do ICMS tenha sido realizada antes dessa geração, pode apenas emitir o livro de apuração com a opção de "Recalculo dos Saldos" marcada\. Localização: módulo Estadual >> ICMS, item de menu DATA MART >> Emissão Livro Apuração\.

Obs: Apesar dessa rotina já estar fazendo o recálculo dos saldos na etapa 6, manteremos a orientação para emissão do livro de apuração após esta geração, para garantirmos que os totais fiquem corretos nos resumos da apuração do ICMS e ICMS\-ST\.

Pré\-requisito:

- Criar Calendário para a Apuração do ICMS – P9, no módulo Estadual >> Controle das Obrigações Estaduais, item de menu Obrigações>> Calendário das Obrigações >> Por Estabelecimento\.
- Parametrizar as informações para os lançamentos à complementar e restituir na tela de Dados Iniciais, disponível neste módulo\.
- Ter realizado os processos de Geração dos Movimentos e Transferência dos Movimentos para a EFD Fiscal, disponível neste módulo\.

Base legal: 

Tópico __19\.4\-A da INSTRUÇÃO NORMATIVA DRP Nº 045/98__

Não está sendo contemplado nesse processo o acúmulo do valor a restituir no controle de crédito no registro 1200 – tópico __19\.4\-A\.2 item 3 da IN45/98:__

__“3 \-__acumular valor a restituir para ceder a terceiros, hipótese na qual o valor deverá fazer parte do registro da informação prevista pelo número 2 e ser estornado observando o disposto no Capítulo LI, subitem 4\.4\.1, "r", além de ser informado no registro 1200, que deverá citar o código RS090001 no campo COD\_AJ\_APUR e o valor a restituir acumulado no período no campo CRED\_APR\.”

Tópicos 19\.3\-A\.2\.2\.2 \(c\) e 19\.3\-A\.2\.2\.3 \(b\) \[__MFS89648\]__

# <a id="_Toc111215499"></a>Parâmetros da Tela 

Período : \[ dd/aaaa \]

\[ \] Gerar Lançamento a Complementar

\[ \] Gerar Lançamento a Restituir

Realizar o Lançamento a Restituir: 

 \( \) na Apuração do ICMS\-ST 

 \( \) na Apuração do ICMS

\[ \] Compensar o Valor a Complementar com o Saldo Credor do ICMS

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

Neste campo será informado o período \(mês e ano\) para a geração dos lançamentos

Deve ser um mês válido\.

Gerar Lançamento a Complementar

Check\-box

N

S

Default marcado

Gerar Lançamento a Restituir

Check\-box

N

S

Default marcado

Realizar o Lançamento a Restituir

Radiobutton

N

S

Este campo só ficará habilitado caso o campo “Gerar Lançamento a Restituir” for selecionado\.

Opções disponíveis

\- na Apuração do ICMS\-ST

\- na Apuração do ICMS

Default: opção Apuração do ICMS\-ST

Compensar o Valor a Complementar com o Saldo Credor do ICMS

Check\-box

N

S

Este campo só ficará habilitado caso o campo “Gerar Lançamento a Complementar” for selecionado\.

Default: desmarcado

Estabelecimentos

Alfanumérico 

S

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

# <a id="_Toc111215500"></a>Críticas 

Os Pré\-requisitos para a Geração dos Lançamentos nas Apurações do ICMS / ICMS\-ST são:

- Possuir um calendário para a Apuraçao do ICMS – P9, no módulo Estadual >> Controle das Obrigações Estaduais, item de menu Obrigações>> Calendário das Obrigações >> Por Estabelecimento, para o estabelecimento, período e código da obrigação 108\.
- Parametrizar as informações para os lançamentos a complementar e restituir na tela de Dados Iniciais, disponível neste módulo\.
- Ter realizado o processo de Transferência dos Movimentos para a EFD Fiscal, disponível neste módulo

Antes de iniciamos, vamos checar se esses passos foram feitos\. Caso encontre alguma falha nestas verificações, o processo será abortado\.

Verificar se a Transferência dos Movimentos para a EFD Fiscal foi realizada:

Verificar se a Transferência dos Movimentos foi realizada, fazendo uma consulta na Tabela de Saldo Consolidado da Restituição/Complemento \- X304\_SALDO\_CONS\_RES\_COMP\_ICMS, considerando os critérios:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Código do estabelecimento selecionado em tela;
- Data da Apuração = Período informado em tela;

Caso não encontre registro, exibir mensagem de erro no Log da Geração:

*“Não foi possível realizar a geração dos lançamentos, pois não foi encontrado registro na Tabela de Saldo Consolidado da Restituição/Complemento \(SAFX304\)\. Esta tabela é carregada no processamento da Transferência dos Movimentos para a EFD Fiscal\. Certifique que a Transferência dos Movimentos para a EFD Fiscal foi executada para o período e estabelecimento”\.*

Verificar se o Calendário para Apuração do ICMS foi criado, no Módulo Controle das Obrigações Estaduais:

Verificar se existe calendário para a Apuração do ICMS – P9\.

O cadastro do Calendário das Obrigações está localizado no módulo Estadual >> Controle das Obriações Estaduais, item de menu Obrigações>> Calendário das Obrigações >> Por Estabelecimento\.

Verificar se existe Calendário da Obrigação Fiscal por Estabelecimento \(tabela CALEND\_OBRIGACAO\), considerando os critérios: 

- Empresa de login;
- Estabelecimento informado na tela de geração;
- Data da Apuração =Último dia do período informado na tela de geração;
- Obrigação Fiscal = “108”

Caso não encontre registro, exibir mensagem de erro no Log da Geração:

*“Não é possível realizar a geração dos lançamentos, pois não existe Calendário para a Apuração do ICMS – P9 para o estabelecimento e período informados\. Favor criar o calendário, no módulo Estadual >> Controle das Obriações Estaduais, menu Obrigações>> Calendário das Obrigações >> Por Estabelecimento\.”*

Verificar o Status da Apuração do ICMS

Para realizar a geração da transferência, caso exista Apuração do ICMS realizada para o estabelecimento, período e livro \(108 ou 165\), esta não pode estar encerrada\.

Para isso vamos consultar o Status da Obrigação Fiscal \(tabela APURACAO\), no módulo Estadual >> ICMS, item de menu Manuteção >> Status das Obrigações\. Considerar os seguintes critérios:

- Empresa de login;
- Estabelecimento informado na tela de geração;
- Data da Apuração =Último dia do período informado na tela de geração;
- Obrigação Fiscal = “108”

Caso a apuração esteja com Situação = “Apuração Realizada” \(campo IND\_SITUACAO\_APUR = ‘2’\) e Validade = “Válido” \(campo IND\_VALID\_APUR = ‘2’\), então exibir mensagem de erro no Log da Geração:

*“Não é possível realizar a geração dos lançamentos, pois a Apuração do ICMS – P9 encontra\-se encerrada para o estabelecimento e período informados\. Favor reabrir a apuração, no módulo Estadual >> ICMS, menu Manutenção>> Status das Obrigações\.”*

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

Se não for encontrada parametrização dos Dados Iniciais, exibir a seguinte mensagem no Log da Geração:

*“Faltou realizar parametrização dos Dados Iniciais para o estabelecimento\. Vide menu Parâmetros >> IN\-RE87/20 >> Dados Iniciais”\.*

Se o parâmetro “Gerar Lançamento a Complementar” estiver marcado, então:

É obrigatório que os campos Item da Apuração, Descrição do Lançamento e Código de Ajuste do quadro  “__Lançamento do Valor a Complementar na Apuração do ICMS\-ST__” estejam preenchidos na tela dos Dados iniciais \(vide menu Parâmetros >> IN\-RE87/20 >> Dados Iniciais\) \- tabela EST\_ST\_RS\_DADOS\_INI\_IN87, campos cod\_oper\_apur\_compl, dsc\_item\_apur\_compl e 

cod\_ajuste\_icms\_compl\. 

Caso algum dos campos não esteja preenchido exibir a mensagem no Log da Geração:

*“Não foi informado Item da Apuração, Descrição do Lançamento ou Código de Ajuste do Lançamento do Valor a Complementar na Apuração do ICMS\-ST para o Estabelecimento\. Favor realizar parametrização dos Dados Iniciais\. Vide menu Parâmetros >> IN\-RE87/20 >> Dados Iniciais”\.*

Se o parâmetro “Realizar o Lançamento a Restituir” estiver com a opção “na Apuração do ICMS\-ST” marcada, então:

É obrigatório que os campos Item da Apuração, Descrição do Lançamento e Código de Ajuste do quadro  “__Lançamento do Valor a Restituir na Apuração do ICMS\-ST__” estejam preenchidos na tela dos Dados iniciais \(vide menu Parâmetros >> IN\-RE87/20 >> Dados Iniciais\) \- tabela EST\_ST\_RS\_DADOS\_INI\_IN87, campos cod\_oper\_apur\_rest\_st, dsc\_item\_apur\_rest\_st e cod\_ajuste\_icms\_rest\_st\.

Caso algum dos campos não esteja preenchido exibir a mensagem no Log da Geração:

*“Não foi informado Item da Apuração, Descrição do Lançamento ou Código de Ajuste do Lançamento do Valor a Restituir na Apuração do ICMS\-ST para o Estabelecimento\. Favor realizar parametrização dos Dados Iniciais\. Vide menu Parâmetros >> IN\-RE87/20 >> Dados Iniciais”\.*

Se o parâmetro “Realizar o Lançamento a Restituir” estiver com a opção “na Apuração do ICMS” marcada, então:

É obrigatório que os campos Item da Apuração, Descrição do Lançamento e Código de Ajuste do quadro  “__Lançamento do Valor a Restituir na Apuração do ICMS__” estejam preenchidos na tela dos Dados iniciais \(vide menu Parâmetros >> IN\-RE87/20 >> Dados Iniciais\) \- tabela EST\_ST\_RS\_DADOS\_INI\_IN87, campos cod\_oper\_apur\_rest\_ic,  dsc\_item\_apur\_rest\_ic e cod\_ajuste\_icms\_rest\_ic\.

Caso algum dos campos não esteja preenchido exibir a mensagem no Log da Geração:

*“Não foi informado Item da Apuração, Descrição do Lançamento ou Código de Ajuste do Lançamento do Valor a Restituir na Apuração do ICMS para o Estabelecimento\. Favor realizar parametrização dos Dados Iniciais\. Vide menu Parâmetros >> IN\-RE87/20 >> Dados Iniciais”\.*

Se o parâmetro “Compensar o Valor a Complementar com o Saldo Credor do ICMS” estiver marcado, então:

É obrigatório que os campos Item da Apuração, Descrição do Lançamento e Código de Ajuste do quadro  “__Lançamento do Estorno do Valor da Compensação na Apuração do ICMS__” estejam preenchidos na tela dos Dados iniciais \(vide menu Parâmetros >> IN\-RE87/20 >> Dados Iniciais\) \- tabela EST\_ST\_RS\_DADOS\_INI\_IN87, campos cod\_oper\_apur\_estorno, dsc\_item\_apur\_estorno e cod\_ajuste\_icms\_estorno\.

Caso algum dos campos não esteja preenchido exibir a mensagem no Log da Geração:

*“Não foi informado Item da Apuração, Descrição do Lançamento ou Código de Ajuste do Lançamento do Estorno do Valor da Compensação na Apuração do ICMS para o Estabelecimento\. Favor realizar parametrização dos Dados Iniciais\. Vide menu Parâmetros >> IN\-RE87/20 >> Dados Iniciais”\.*

É obrigatório que os campos Item da Apuração, Descrição do Lançamento e Código de Ajuste do quadro  “__Lançamento do Valor da Compensação na Apuração do ICMS\-ST__” estejam preenchidos na tela dos Dados iniciais \(vide menu Parâmetros >> IN\-RE87/20 >> Dados Iniciais\) \- tabela EST\_ST\_RS\_DADOS\_INI\_IN87, campos cod\_oper\_apur\_compens, dsc\_item\_apur\_compens, cod\_ajuste\_icms\_compens\.

Caso algum dos campos não esteja preenchido exibir a mensagem no Log da Geração:

*“Não foi informado Item da Apuração, Descrição do Lançamento ou Código de Ajuste do Lançamento do Valor da Compensação na Apuração do ICMS\-ST para o Estabelecimento\. Favor realizar parametrização dos Dados Iniciais\. Vide menu Parâmetros >> IN\-RE87/20 >> Dados Iniciais”\.*

Acontecendo qualquer erro, finalizar a geração com status = “\-1” – Erro\.

# <a id="_Toc111215501"></a>Processamento

## <a id="_Toc111215502"></a>4\.1 – Etapa 1: Limpeza dos lançamentos gerados por esse processo nas Apurações do ICMS e do ICMS\-ST 

Nesta etapa vamos eliminar os lançamentos complementares, gerados em processamentos anteriores\.

__Eliminação do Lançamento na Tabela de Lançamentos da Apuração do ICMS \(ITEM\_APURAC\_DISCR\)__

Identificar o lançamento com os critérios abaixo:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Códigos dos estabelecimentos selecionados em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108"
- Indicador de Lançamento Digitado/calculado \(ind\_dig\_calculado\) = __‘7’__ \- lançamento gerado por esse processo

__Eliminação do Lançamento na Tabela de Lançamentos da Apuração do ICMS\-ST \(ITEM\_APURAC\_SUBST\)__

Identificar o lançamento com os critérios abaixo:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Códigos dos estabelecimentos selecionados em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108"
- Indicador de Lançamento Digitado/calculado \(ind\_dig\_calculado\) = __‘7’__ \- lançamento gerado por esse processo

__Realizar o Recálculo dos Saldos da Apuração do ICMS e ICMS\-ST:__

Nesse passo os subtotais e totais das Apurações do ICMS e ICMS\-ST são recalculados após a eliminação dos lancamentos complementares realizada acima\.

Esse recálculo é necessário para que o valor do SALDO CREDOR \(item 014\) da Apuração do ICMS volte ao original do período, pois ele pode ser utilizado para compensação do Valor a Complementar\.   

Chamar a procedure SAF\_ICMS\_CALC\_SLD para o livro “108”\.

__Gravação da Tabela de Status da Obrigação \(APURACAO\)__

Verificar se existe registro de Status da Obrigação Fiscal \(tabela APURACAO\), no módulo Estadual >> ICMS, item de menu Manuteção >> Status das Obrigações\. Considerar os seguintes critérios:

- Empresa de login;
- Estabelecimento informado na tela de geração;
- Data da Apuração =Último dia do período informado na tela de geração;
- Obrigação Fiscal = “108”\.

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

Este passo é necessário quando a geração da Apuração do ICMS não foi realizada antes desta geração\. O registro deve ser criado na tabela de Apuração para que os lançamentos possam ser realizados\.

## <a id="_5.2_-_"></a><a id="_4.2_-_"></a><a id="_Toc111215503"></a>4\.2 \- Etapa 2: Calcular o Valor para Lançamento \(a Complementar ou a Restituir\)

Nesta etapa vamos totalizar dois valores: Valor do ICMS\-ST Restituição e Valor do ICMS\-ST Complemento para encontrar o valor do lançamento \(valor líquido a complementar ou restituir\), que será considerado nos lançamentos complementares que serão gerados nos passos a seguir\. 

__Origem dos dados__: \- Tabela de Saldo Consolidado da Restituição/Complemento \- X304\_SALDO\_CONS\_RES\_COMP\_ICMS

__Critérios da recuperação: __

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Código do estabelecimento selecionado em tela;
- Data da Apuração = compreendida no Período informado em tela;

Recuperar as informações:

Valor do ICMS\-ST Restituição

__\[MFS96666\]: Inclusão dos Códigos RS101, \.\.\., RS301, \.\.\., RS601, \.\.\. e RS801, \.\.\., a partir de Jan\-2023:__

Totalizar o campo Valor do ICMS\-ST Restituição \(VLR\_ICMS\_ST\_REST\) para os Códigos de Motivo:

RS100, RS101, RS102, RS103, RS104, RS105, RS151, RS152, RS153, RS154, RS155, RS156

RS800, RS801, RS802, RS803, RS804, RS805, RS851, RS852, RS853, RS854, RS855, RS856

Valor do ICMS\-ST Complemento

Totalizar o campo Valor do ICMS\-ST Complemento \(VLR\_ICMS\_ST\_COMP\) para os Códigos de Motivo:

RS300, RS301, RS302, RS303, RS304, RS305, RS351, RS352, RS353, RS354, RS355, RS356

RS600, RS601, RS602, RS603, RS604, RS605, RS651, RS652, RS653, RS654, RS655, RS656

Valor do Lançamento = Valor do ICMS\-ST Restituição \- Valor do ICMS\-ST Complemento

Após esse cálculo, serão feitos os tratamentos a seguir que podem diminuir ou aumentar o Valor do Lançamento\.

__\[MFS89648\]__

O Valor do Lançamento acima será ajustado com o Valor do ICMS\-ST calculado com base na Média Ponderada, considerando dois cenários:

1\) [Valor Médio Ponderado Móvel](#Medio_Ponderado_Movel_BC_ST) calculado ao final do último dia do mês negativo \(__19\.3\-A\.2\.2\.2__ da IN\-045/98\)\.

2\) Quantidade Final calculada ao final do último dia do mês igual a zero \(__19\.3\-A\.2\.2\.3__ da IN\-045/98\)

<a id="Etapa2_item1"></a>\(1\) __Tratamento para [Valor Médio Ponderado Móvel](#Medio_Ponderado_Movel_BC_ST) do último dia do mês negativo \(19\.3\-A\.2\.2\.2 da IN\-045/98\):__

Fazer uma consulta na tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\) com os seguintes critérios:

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data igual último dia do Período \(Mês/Ano\) informado na Tela de Geração;

\- Valor Médio Unitário da Base de Cálculo do ICMS\-ST \(VLR\_UNIT\_BC\_ST\_FIM\_MP\) < 0

Para cada produto, totalizar o Valor Médio Unitário da Base de Cálculo do ICMS\-ST \(VLR\_UNIT\_BC\_ST\_FIM\_MP\) e calcular o Valor do ICMS\-ST:

Valor do ICMS\-ST = \(Valor Médio Unitário da Base de Cálculo do ICMS\-ST \* Alíquota Interna\) \* Quantidade em Estoque \(__valor resultante negativo__\)

Onde:

\-> Alíquota Interna: 

Alíquota interna parametrizada por Código ou NCM ou CEST do produto, no menu “*Parâmetros 🡪 Produtos 🡪 Por Código*”, __ou__, “*Parâmetros 🡪 Produtos 🡪 Por NCM*”, __ou__, “*Parâmetros 🡪 Produtos 🡪 Por CEST*”\. Considera a parametrização vigente para o último dia do mês\.

\-> Quantidade em Estoque: 

Totalizar a Quantidade de Inventário do produto a partir da consulta a Tabela do Inventário \(X52\_INVENT\_PRODUTO\) considerando os critérios:

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data do Inventário \(campo 03 \- DATA\_INVENTARIO\) último dia do Período \(Mês/Ano\) informado na Tela de Geração;

\- Motivo do Inventário \(campo 40 \- IND\_MOT\_INV\) = “06” \- controle das mercadorias sujeitas ao regime de substituição tributária;

\- Grupo Contagem \(campo 04 \- GRUPO\_CONTAGEM\) 🡪 1, 2, 3 e 5;

\- Produto 🡪 recuperado da tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\),

Se não existir registro de Inventário para o produto, exibir a seguinte mensagem de aviso no log:

*“Inventário para o produto no último dia do mês do período não encontrado\. Desse modo, não foi possível calcular o Valor de ICMS\-ST para ajustar o lançamento conforme determina o tópico 19\.3\-A\.2\.2\.2 da IN\-45/98\.”*

Dados de Identificação: Estabelecimento: xx \- Produto\(ind/cód\) x\-xxx

Se existir, a Quantidade de Inventário recuperada deve ser convertida para a Unidade de Medida do Produto\. Calcular a quantidade convertida:

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

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas será gravada a seguinte mensagem de aviso no log:

“*Fator de conversão de medida de XXX para XXX não encontrado\. Desse modo, não foi possível calcular o Valor de ICMS\-ST para ajustar o lançamento, conforme determina o tópico 19\.3\-A\.2\.2\.2 da IN\-45/98\.”*

\(O primeiro “XXX” é a unidade do inventário, e o segundo “XXX”, a unidade do cadastro do produto\)\.

Dados de Indentificação: Estabelecimento: xx \-  Produto\(ind/cód\) x\-xxx – Grupo Contagem: x – Natureza de Estoque: xx

Totalizar o Valor do ICMS\-ST de todos os produtos e ajustar o valor do lançamento\.

Valor do Lançamento = Valor do Lançamento \+ Valor ICMS\-ST

De acordo com o tópico 19\.3\-A\.2\.2\.2 da IN\-45/98, o Valor do ICMS\-ST calculado irá reduzir o valor da restituição ou aumentar o valor do complemento\. 

<a id="Etapa2_item2"></a>\(2\) __Tratamento para [Quantidade Final ](#Medio_Ponderado_Movel_BC_ST)do último dia do mês zero \(19\.3\-A\.2\.2\.3 da IN\-045/98\):__

Fazer uma consulta na tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\) com os seguintes critérios:

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data igual último dia do Período \(Mês/Ano\) informado na Tela de Geração;

\- Indicador de Utilização do Saldo \(19\.3\-A\.2\.2\.3 IN45/98\) \(IND\_UTIL\_DEV\_ZERA\) = ‘N’

Para cada produto, totalizar o Valor Base de Cálculo do ICMS\-ST \(19\.3\-A\.2\.2\.3 IN45/98\) VLR\_BC\_ST\_DEV\_ZERA, e calcular o Valor do ICMS\-ST:

Valor do ICMS\-ST = Valor Base de Cálculo do ICMS\-ST \(19\.3\-A\.2\.2\.3 IN45/98\) \* Alíquota Interna \(__valor resultante pode ser negativo ou positivo__\)

Onde:

\-> Alíquota Interna: 

Alíquota interna parametrizada por Código ou NCM ou CEST do produto, no menu “*Parâmetros 🡪 Produtos 🡪 Por Código*”, __ou__, “*Parâmetros 🡪 Produtos 🡪 Por NCM*”, __ou__, “*Parâmetros 🡪 Produtos 🡪 Por CEST*”\. Considera a parametrização vigente para o último dia do mês\.

\-> Indicador de Utilização do Saldo \(19\.3\-A\.2\.2\.3 IN45/98\) \(IND\_UTIL\_DEV\_ZERA\) 

Indica se o Saldo calculado no dia em que a devolução das entradas zera a quantidade final, foi utilizado num próximo dia, conforme IN45/98 \- 19\.3\-A\.2\.2\.3 

Se estiver “N” indica que não foi utilizado, e nesse caso, será considerado para o lançamento na apuração\. 

Veja MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Cálculo Média Ponderada\.docx \- 1º Passo – Calcular o Saldo Inicial do Dia\)

Totalizar o Valor do ICMS\-ST de todos os produtos e ajustar o valor do lançamento\.

Valor do Lançamento = Valor do Lançamento \+ Valor ICMS\-ST

De acordo com o tópico 19\.3\-A\.2\.2\.3 da IN\-45/98, o Valor do ICMS\-ST calculado quando negativo, irá reduzir o valor da restituição ou aumentar o valor do complemento, e quando positivo irá aumentar o valor da restituição ou diminuir o valor do complemento\. 

Quando o Valor do Lançamento for positivo se trata de um __valor líquido a restituir__ e quando negativo de __Valor líquido a complementar__\.

  

Se Valor do Lançamento > 0 então 

Valor do Lançamento é o __valor líquido a restituir__ que será lançado na Apuração do ICMS ou na Apuração do ICMS\-ST\. Veja __[Etapa 3](#_5.3_–_Etapa)__[\.](#_5.3_–_Etapa)

Se Valor do Lançamento < 0 então

	Valor do Lançamento \(sem sinal negativo\) é o __Valor líquido a complementar__ que será lançado na Apuração do ICMS\-ST\. Veja __[Etapa 4](#_5.4_–_Etapa)__

Se Valor do Lançamento = 0 então

	Não será realizado lançamento nas apurações\.

	Exibir mensagem de aviso e finalizar a execução da rotina:

“O Valor do ICMS\-ST Restituição é igual ao Valor do ICMS\-ST Complemento para este estabelecimento\. Logo não foram gerados lançamentos nas apurações do ICMS/ ICMS\-ST”\.

## <a id="_5.3_–_Etapa"></a><a id="_4.3_–_Etapa"></a><a id="_Toc111215504"></a>4\.3 – Etapa 3: Gerar lançamento a Restituir

A execução dessa etapa depende do parâmetro “Gerar Lançamento a Restituir” informado na tela de geração\. Caso o parâmetro esteja marcado, o lançamento a restituir será realizado\. Caso contrário, essa etapa não será executada\.

O __valor líquido a restituir__ será lançado na Apuração do ICMS ou na Apuração do ICMS\-ST, dependendo do parâmetro “Realizar o Lançamento a Restituir” indicado na tela de geração\.

Se o parâmetro “Realizar o Lançamento a Restituir” estiver com a opção “na Apuração do ICMS\-ST” marcada, então:

Realizar um lançamento com valor líquido a restituir na Apuração do ICMS\-ST\.

O item da apuração, a descrição do lançamento e o código de Ajuste necessários para realizar o lançamento, estão parametrizados em Dados iniciais como “__Lançamento do Valor a Restituir na Apuração do ICMS\-ST__” \(tabela EST\_ST\_RS\_DADOS\_INI\_IN87, campos cod\_oper\_apur\_rest\_st, dsc\_item\_apur\_rest\_st e cod\_ajuste\_icms\_rest\_st\)\.

Se o parâmetro “Realizar o Lançamento a Restituir” estiver com a opção “na Apuração do ICMS” marcada, então:

Realizar um lançamento com valor líquido a restituir na Apuração do ICMS\.

O item da apuração, a descrição do lançamento e o código de Ajuste necessários para realizar o lançamento, estão parametrizados em Dados iniciais como “__Lançamento do Valor a Restituir na Apuração do ICMS__” \(tabela EST\_ST\_RS\_DADOS\_INI\_IN87, campos cod\_oper\_apur\_rest\_ic,  dsc\_item\_apur\_rest\_ic e cod\_ajuste\_icms\_rest\_ic\)\.

__Gravação do Lançamento na Tabela de Lançamentos da Apuração do ICMS \(ITEM\_APURAC\_DISCR\)__

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

Gravar o código ‘108’

__\*\*\*__

__Operação da Apuração__

COD\_OPER\_APUR

Recuperar o item da apuração cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\_IN87\) para a empresa e estabelecimento foco da geração\.

Considerar quadro __Lançamento do Valor a Restituir na Apuração do ICMS__

__\*\*\*__

__Número do Lançamento__

NUM\_DISCRIMINACAO

Sequencial único por Operação da Apuração \(COD\_OPER\_APUR\)\. 

Ou seja recuperar o próximo número da seguencia de lançamentos da Operação da Apuração que está sendo gravada, considerando a empresa, estabelecimento, data da apuração, código do livro e a operação da apuração\.

__Valor do Lançamento__

VAL\_ITEM\_DISCRIM

valor líquido a restituir

__Descrição do Lançamento__

DSC\_ITEM\_APURACAO

Recuperar a Descrição do Lançamento cadastrada na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\_IN87\) para a empresa e o estabelecimento foco da geração\.

Considerar quadro __Lançamento do Valor a Restituir na Apuração do ICMS__

__Código do Ajuste ICMS__

COD\_AJUSTE\_ICMS

Recuperar o Código de Ajuste Sped Fiscal cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\_IN87\) para a empresa e o estabelecimento foco da geração\.

Considerar \.

Considerar quadro __Lançamento do Valor a Restituir na Apuração do ICMS__

__Indicador do Tipo do Lançamento__

IND\_TIPO\_LANC

Gravar com __“3”\.__

Este valor signfica que o lançamento não possui documentos associados\.

__Indicador de Lançamento Digitado/calculado__

IND\_DIG\_CALCULADO

Gravar com “7”\.

__7 __– identifica os lançamentos gerados por esse processo\.

Demais campos não mencionados não precisam ser preenchidos

__Gravação do Lançamento na Tabela de Lançamentos da Apuração do ICMS\-ST \(ITEM\_APURAC\_SUBST\)__

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

Recuperar o item da apuração cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\_IN87\) para a empresa e estabelecimento foco da geração\.

Considerar quadro __Lançamento do Valor a Restituir na Apuração do ICMS\-ST__

__\*\*\*__

__Número do Lançamento__

NUM\_DISCRIMINACAO

Sequencial único por Operação da Apuração \(COD\_OPER\_APUR\)\. 

Ou seja recuperar o próximo número da seguencia de lançamentos da Operação da Apuração que está sendo gravada, considerando a empresa, estabelecimento, data da apuração, código do livro, identificador do Estado \(ident\_estado\), Indicador da UF \(ind\_uf\) e a operação da apuração\.

__Valor do Lançamento__

VAL\_ITEM\_DISCRIM

valor líquido a restituir

__Descrição do Lançamento__

DSC\_ITEM\_APURACAO

Recuperar a Descrição do Lançamento cadastrada na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\_IN87\) para a empresa e o estabelecimento foco da geração\.

Considerar quadro __Lançamento do Valor a Restituir na Apuração do ICMS\-ST__

__Código do Ajuste ICMS__

COD\_AJUSTE\_ICMS

Recuperar o Código de Ajuste Sped Fiscal cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\_IN87\) para a empresa e o estabelecimento foco da geração\.

Considerar \.

Considerar quadro __Lançamento do Valor a Restituir na Apuração do ICMS\-ST__

__Indicador do Tipo do Lançamento__

IND\_TIPO\_LANC

Gravar com __“3”\.__

Este valor signfica que o lançamento não possui documentos associados\.

__Indicador de Lançamento Digitado/calculado__

IND\_DIG\_CALCULADO

Gravar com “7”\.

__7 __– identifica os lançamentos gerados por esse processo

Demais campos não mencionados não precisam ser preenchidos

## <a id="_5.4_–_Etapa"></a><a id="_4.4_–_Etapa"></a><a id="_Toc111215505"></a>4\.4 – Etapa 4: Gerar lançamento a Complementar

A execução dessa etapa depende do parâmetro “Gerar Lançamento a Complementar” informado na tela de geração\. Caso o parâmetro esteja marcado, o lançamento a complementar será realizado\. Caso contrário, essa etapa não será executada\.

O __valor líquido a complementar__ será lançado na Apuração do ICMS\-ST\.

O item da apuração, a descrição do lançamento e o código de Ajuste necessários para realizar o lançamento, estão parametrizados em Dados iniciais como “__Lançamento do Valor a Complementar na Apuração do ICMS\-ST__” \(tabela EST\_ST\_RS\_DADOS\_INI\_IN87, campos cod\_oper\_apur\_compl, dsc\_item\_apur\_compl e cod\_ajuste\_icms\_compl\)\.

__Gravação do Lançamento na Tabela de Lançamentos da Apuração do ICMS\-ST \(ITEM\_APURAC\_SUBST\)__

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

Recuperar o item da apuração cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\_IN87\) para a empresa e estabelecimento foco da geração\.

Considerar quadro __Lançamento do Valor a Complementar na Apuração do ICMS\-ST__

__\*\*\*__

__Número do Lançamento__

NUM\_DISCRIMINACAO

Sequencial único por Operação da Apuração \(COD\_OPER\_APUR\)\. 

Ou seja recuperar o próximo número da seguencia de lançamentos da Operação da Apuração que está sendo gravada, considerando a empresa, estabelecimento, data da apuração, código do livro, identificador do Estado \(ident\_estado\), Indicador da UF \(ind\_uf\) e a operação da apuração\.

__Valor do Lançamento__

VAL\_ITEM\_DISCRIM

valor líquido a complementar

__Descrição do Lançamento__

DSC\_ITEM\_APURACAO

Recuperar a Descrição do Lançamento cadastrada na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\_IN87\) para a empresa e o estabelecimento foco da geração\.

Considerar quadro __Lançamento do Valor a Complementar na Apuração do ICMS\-ST__

__Código do Ajuste ICMS__

COD\_AJUSTE\_ICMS

Recuperar o Código de Ajuste Sped Fiscal cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\_IN87\) para a empresa e o estabelecimento foco da geração\.

Considerar \.

Considerar quadro __Lançamento do Valor a Complementar na Apuração do ICMS\-ST__

__Indicador do Tipo do Lançamento__

IND\_TIPO\_LANC

Gravar com __“3”\.__

Este valor signfica que o lançamento não possui documentos associados\.

__Indicador de Lançamento Digitado/calculado__

IND\_DIG\_CALCULADO

Gravar com “7”\.

__7 __– identifica os lançamentos gerados por esse processo

Demais campos não mencionados não precisam ser preenchidos

## <a id="_4.5_–_Etapa"></a><a id="_Toc111215506"></a>4\.5 – Etapa 5: Compensar o Valor a Complementar

Se na [Etapa 2](#_5.2_-_) foi calculado um __Valor líquido a complementar__ e foi realizado um lançamento complementar na Apuração do ICMS\-ST, a rotina possibilita compensar o valor a complementar com o Saldo Credor da Apuração do ICMS\.

Caso o parâmetro “Compensar o Valor a Complementar com o Saldo Credor do ICMS” esteja marcado e na [Etapa 2](#_5.2_-_) foi calculado um __Valor líquido a complementar,__ então:

Executar a etapa 5, seguindo os passos a seguir\.

Caso contrário, não executar essa etapa\.

__Passo 1 – Verificar se a Apuração do ICMS possui um Saldo Credor:__

Para isso consultar o Resumo da Apuração do ICMS \(tabela ITEM\_APURAC\_CALC\) com os critérios:

\- Estabelecimento: selecionado para geração;

\- Data da Apuração: Úlitmo dia do mes e ano do Período da informado na tela de geração

\- Código do Livro: 108

\- Operação da Apuração = ‘014’ – Saldo Credor \(Crédito menos débito\) a transportar p/ período seguinte

Se o valor \(VAL\_APURACAO\) recuperado for igual a zero então exibir mensagem no log e não executar os próximos passos\.

“Não foi possível compensar o Valor a Complementar, pois não há saldo credor na Apuração do ICMS para este estabelecimento\.”

Senão

	Continuar os próximos passos\.

__Passo 2 – Calcular o Valor a Compensar:__

Comparar __Valor líquido a complementar__ calculado na [Etapa 2](#_5.2_-_) com o __Valor do Saldo Credor__ recuperado no passo 1\.

A regra fiscal é “*O montante da compensação é limitado ao valor do complemento apurado, ou ao saldo credor do imposto próprio, se inferior ao valor do complemento apurado\.*”

Se __Valor líquido a complementar__ <= o __Valor do Saldo Credor__

	Valor a Compensar = Valor líquido a complementar

Se __Valor líquido a complementar__ > o __Valor do Saldo Credor__

	Valor a Compensar = Valor do Saldo Credor

O Valor a Compensar será utilizado para realizar __DOIS__ lançamentos: um na Apuração do ICMS e outro na do ICMS\-ST\. Para isso execute os passos 3 e 4\.

__Passo 3 – Lançar estorno de crédito do Valor a Compensar na Apuração do ICMS__

O Valor a Compensar será lançado na Apuração do ICMS, como um estorno de crédito\.

O item da apuração, a descrição do lançamento e o código de Ajuste necessários para realizar o lançamento, estão parametrizados em Dados iniciais como “__Lançamento do Estorno do Valor da Compensação na Apuração do ICMS__” \(tabela EST\_ST\_RS\_DADOS\_INI\_IN87, campos cod\_oper\_apur\_estorno, dsc\_item\_apur\_estorno e cod\_ajuste\_icms\_estorno\)\.

__Gravação do Lançamento na Tabela de Lançamentos da Apuração do ICMS \(ITEM\_APURAC\_DISCR\)__

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

Gravar o código ‘108’

__\*\*\*__

__Operação da Apuração__

COD\_OPER\_APUR

Recuperar o item da apuração cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\_IN87\) para a empresa e estabelecimento foco da geração\.

Considerar quadro __Lançamento do Estorno do Valor da Compensação na Apuração do ICMS__

__\*\*\*__

__Número do Lançamento__

NUM\_DISCRIMINACAO

Sequencial único por Operação da Apuração \(COD\_OPER\_APUR\)\. 

Ou seja recuperar o próximo número da seguencia de lançamentos da Operação da Apuração que está sendo gravada, considerando a empresa, estabelecimento, data da apuração, código do livro e a operação da apuração\.

__Valor do Lançamento__

VAL\_ITEM\_DISCRIM

Valor a Compensar

__Descrição do Lançamento__

DSC\_ITEM\_APURACAO

Recuperar a Descrição do Lançamento cadastrada na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\_IN87\) para a empresa e o estabelecimento foco da geração\.

Considerar quadro __Lançamento do Estorno do Valor da Compensação na Apuração do ICMS__

__Código do Ajuste ICMS__

COD\_AJUSTE\_ICMS

Recuperar o Código de Ajuste Sped Fiscal cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\_IN87\) para a empresa e o estabelecimento foco da geração\.

Considerar \.

Considerar quadro __Lançamento do Estorno do Valor da Compensação na Apuração do ICMS__

__Indicador do Tipo do Lançamento__

IND\_TIPO\_LANC

Gravar com __“3”\.__

Este valor signfica que o lançamento não possui documentos associados\.

__Indicador de Lançamento Digitado/calculado__

IND\_DIG\_CALCULADO

Gravar com “7”\.

__7 __– identifica os lançamentos gerados por esse processo\.

Demais campos não mencionados não precisam ser preenchidos

__Passo 4 – Lançar crédito do Valor a Compensar na Apuração do ICMS\-ST__

O Valor a Compensar será lançado na Apuração do ICMS\-ST em outros créditos\.

O item da apuração, a descrição do lançamento e o código de Ajuste necessários para realizar o lançamento, estão parametrizados em Dados iniciais como “__Lançamento do Valor da Compensação na Apuração do ICMS\-ST__” \(tabela EST\_ST\_RS\_DADOS\_INI\_IN87, campos cod\_oper\_apur\_compens, dsc\_item\_apur\_compens, cod\_ajuste\_icms\_compens\)\.

__Gravação do Lançamento na Tabela de Lançamentos da Apuração do ICMS\-ST \(ITEM\_APURAC\_SUBST\)__

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

Recuperar o item da apuração cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\_IN87\) para a empresa e estabelecimento foco da geração\.

Considerar quadro __Lançamento do Valor da Compensação na Apuração do ICMS\-ST__

__\*\*\*__

__Número do Lançamento__

NUM\_DISCRIMINACAO

Sequencial único por Operação da Apuração \(COD\_OPER\_APUR\)\. 

Ou seja recuperar o próximo número da seguencia de lançamentos da Operação da Apuração que está sendo gravada, considerando a empresa, estabelecimento, data da apuração, código do livro, identificador do Estado \(ident\_estado\), Indicador da UF \(ind\_uf\) e a operação da apuração\.

__Valor do Lançamento__

VAL\_ITEM\_DISCRIM

Valor a Compensar

__Descrição do Lançamento__

DSC\_ITEM\_APURACAO

Recuperar a Descrição do Lançamento cadastrada na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\_IN87\) para a empresa e o estabelecimento foco da geração\.

Considerar quadro __Lançamento do Valor da Compensação na Apuração do ICMS\-ST__

__Código do Ajuste ICMS__

COD\_AJUSTE\_ICMS

Recuperar o Código de Ajuste Sped Fiscal cadastrado na tela de Dados Iniciais \(EST\_ST\_RS\_DADOS\_INI\_IN87\) para a empresa e o estabelecimento foco da geração\.

Considerar quadro __Lançamento do Valor da Compensação na Apuração do ICMS\-ST__

__Indicador do Tipo do Lançamento__

IND\_TIPO\_LANC

Gravar com __“3”\.__

Este valor signfica que o lançamento não possui documentos associados\.

__Indicador de Lançamento Digitado/calculado__

IND\_DIG\_CALCULADO

Gravar com “7”\.

__7 __– identifica os lançamentos gerados por esse processo

Demais campos não mencionados não precisam ser preenchidos

## <a id="_Toc111215507"></a>4\.6 – Etapa 6: Recálculo dos Saldos da Apuração do ICMS e ICMS\-ST

Nesse passo os subtotais e totais das Apurações do ICMS e ICMS\-ST são recalculados para considerar os valores dos lancamentos complementares realizados nas etapas anteriores\.

Sendo assim não é necessário após a execução dessa geração, realizar a Apuração do ICMS novamente ou a Emissão do Livro de Apuração com opção de “Recálculo dos Saldos” marcada\. Os totais da apuração já estarão atualizados ao final desta geração\.

Chamar a procedure SAF\_ICMS\_CALC\_SLD para o livro “108”\.

# <a id="_Toc111215508"></a>Relatório

Gerar um arquivo excel a partir da leitura das tabelas onde foram gerados os lançamentos complementares __ITEM\_APURAC\_DISCR e ITEM\_APURAC\_SUBST__

Nome do arquivo: Relatório\_Conferencia\_Lancamentos\_mm\_aaaa\_cod\_estab\.xlsx

O relatório deve demonstrar os lançamentos que foram gerados nas Apurações do ICMS e ICMS\-ST por esse processo:

\- Lançamento a Restituir \(vide [etapa 3\)](#_4.3_–_Etapa)

\- Lançamento a Complementar \(vide [etapa 4](#_4.4_–_Etapa)\)

\- Lançamento do estorno do crédito do Valor a Compensar \(vide [etapa 5](#_4.5_–_Etapa) – passo 3\)

\- Lançamento do crédito do Valor a Compensar \(vide [etapa 5](#_4.5_–_Etapa) – passo 4\)

Layout do Relatório:

__Campos__

__Regra de Preenchimento__

Código da empresa

Código da empresa do login\.

Código do estabelecimento

Código do estabelecimento selecionado em tela\.

Data da Apuração

Úlitmo dia do mês e ano do Período da informado na tela de geração\.

Código do Livro

Gravar o código ‘108’

Apuração

Para o lançamento realizado na Apuração do ICMS \(__ITEM\_APURAC\_DISCR\):__

   Preencher com “ICMS”

Para o lançamento realizado na Apuração do ICMS\-ST \(__ITEM\_APURAC\_SUBST\):__

   Preencher com “ICMS\-ST”

Lançamento

Para os Lançamentos a Restituir realizados na [etapa 3](#_5.3_–_Etapa):

   Preencher com “Restituição”

Para o Lançamento a Complementar realizado na [etapa 4](#_5.4_–_Etapa):

   Preencher com “Complementação” 

Para o Lançamento do estorno do crédito do Valor a Compensar realizado na [etapa 5](#_4.5_–_Etapa) – passo 3:

   Preencher com “Estorno do Valor da Compensação”

Preencher com Lançamento do crédito do Valor a Compensar realizado na [etapa 5](#_4.5_–_Etapa) – passo 4:

   Preencher com “Crédito do Valor da Compensação”

Item da Apuração \(cod\-desc\)

Código \+ Descrição da Operação da Apuração da Apuração do ICMS \(__ITEM\_APURAC\_DISCR\- COD\_OPER\_APUR\) __ou da Apuração do ICMS\-ST \(__ITEM\_APURAC\_SUBST \- COD\_OPER\_APUR\)\.__

Para recuperar a descrição, consultar a tabela OPERACAO\_APURACAO considerando o livro 108 e o código da operação\.

Exemplo: 002 \- OUTROS DEBITOS \(DISCRIMINAR ABAIXO\)

Descrição do Lançamento

Descrição do Lançamento da Apuração do ICMS \(__ITEM\_APURAC\_DISCR\- DSC\_ITEM\_APURACAO\) __ou da Apuração do ICMS\-ST \(__ITEM\_APURAC\_SUBST \- DSC\_ITEM\_APURACAO\)\.__

Código do Ajuste Sped Fiscal

Código do Ajuste ICMS da Apuração do ICMS \(__ITEM\_APURAC\_DISCR\- COD\_AJUSTE\_ICMS\) __ou da Apuração do ICMS\-ST \(__ITEM\_APURAC\_SUBST \- COD\_AJUSTE\_ICMS\)\.__

Valor do Lançamento

Valor do Lançamento da Apuração do ICMS \(__ITEM\_APURAC\_DISCR\- VAL\_ITEM\_DISCRIM\) __ou da Apuração do ICMS\-ST \(__ITEM\_APURAC\_SUBST \- VAL\_ITEM\_DISCRIM\)\.__

Valor ICMS\-ST Restituição \- Complementação

__MFS89648__

Este campo será preenchido quando o campo “Lançamento” for Restituição” ou “Complementação”\.

Demonstrar o Valor do ICMS\-ST Restituição \- Complemento que compõe o valor do lançamento, conforme  [Etapa 2](#_4.2_-_)\.

Onde:

\- Valor do ICMS\-ST Restituição: total do campo VLR\_ICMS\_ST\_REST da X304 para os Códigos de Motivo:

RS100, RS101, RS102, RS103, RS104, RS105, RS151, RS152, RS153, RS154, RS155, RS156

RS800, RS801, RS802, RS803, RS804, RS805, RS851, RS852, RS853, RS854, RS855, RS856

\- Valor do ICMS\-ST Complemento: total do campo VLR\_ICMS\_ST\_COMP da X304 para os Códigos de Motivo:

RS300, RS301, RS302, RS303, RS304, RS305, RS351, RS352, RS353, RS354, RS355, RS356

RS600, RS601, RS602, RS603, RS604, RS605, RS651, RS652, RS653, RS654, RS655, RS656

Valor ICMS\-ST Média Negativa

__MFS89648__

Este campo será preenchido quando o campo “Lançamento” for Restituição” ou “Complementação”\.

Demonstrar o Valor do ICMS\-ST que foi deduzido/acrescentado do/ao valor do lançamento, com base no tratamento especificado na [Etapa 2](#_4.2_-_) – item [\(1\)](#Etapa2_item1)\. 

Valor do ICMS\-ST Média Zero 

__MFS89648__

Este campo será preenchido quando o campo “Lançamento” for Restituição” ou “Complementação”\.

Demonstrar o Valor do ICMS\-ST que foi deduzido/acrescentado do/ao valor do lançamento, com base no tratamento especificado na [Etapa 2](#_5.2_-_) – item [\(2\)](#Etapa2_item2)\.

= = = = = =

