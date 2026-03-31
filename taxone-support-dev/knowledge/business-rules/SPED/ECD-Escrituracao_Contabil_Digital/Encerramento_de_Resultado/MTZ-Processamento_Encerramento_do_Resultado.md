# MTZ-Processamento_Encerramento_do_Resultado

- **Fonte:** MTZ-Processamento_Encerramento_do_Resultado.docx
- **Modificado:** 2026-02-20
- **Tamanho:** 136 KB

---

THOMSON REUTERS

Módulo Sped Contábil

Processamento Encerramento do Resultado

__Localização__: Menu Sped, Módulo: Escrituração Contábil Digital à Geraçãoà Encerramento do Resultado

Sumário

[CONTROLE DE ALTERAÇÕES	3](#_Toc48738317)

[1\.1\.	INTRODUÇÃO	3](#_Toc48738318)

[1\.2\.	DOCUMENTOS DE REFERÊNCIA	3](#_Toc48738319)

[1\.3\.	DEFINIÇÃO DAS REGRAS	4](#_Toc48738320)

<a id="_Toc45638640"></a><a id="_Toc45638672"></a>

# <a id="_Toc462320891"></a><a id="_Toc27038219"></a><a id="_Toc48738317"></a>CONTROLE DE ALTERAÇÕES

__Data__

__Demanda__

__Descrição__

__Autor__

14/07/2020

MFS\-39909

Criação do Documento\. Nesta demanda estamos documentando o que foi implementado, através de Engenharia Reversa\.

Alessandra Cristina Navatta

18/08/2020

MFS\-34603

Ajuste na funcionalidade, considerando os estudos realizados na MFS39910 \(RP01 e RP03\)

Alessandra Cristina Navatta

13/04/2021

MFS\-62795

Tratamento na geração do Processo “Criar os Lançamento de Encerramento”, para “bloquear” a geração caso seja identificado que o processo foi executado, sem antes executar o Processo de “Excluir os Lançamentos de Encerramento Criados pelo Sistema”\. O objetivo é evitar que o usuário gere 2 vezes seguidas o processo de “Criar os Lançamento de Encerramento”, causando erros na base\.

Rogério Ohashi

17/06/2021

MFS\-67497

Tratamento na geração do Campo 16 \- NUM\_LANCAMENTO da tabela SAFX01, na criação dos lançamentos de encerramento, deverá ser concatenado “E” \+ “MM” \+ “AAAA” antes do número sequencial\. \(na Partida e Contrapartida\)\. 

Rogério Ohashi

12/07/2021

MFS\-68760

Ajustes na funcionalidade do Parâmetro “Considerar Saldos por Centro de Custo \(SAFX80\)” regra__ RP01__ e Aba de Relatório de Conferência regra __RP04__\.

Rogério Ohashi

21/09/2021

MFS\-72676

Alteração na geração do Encerramento Contábil para considerar os Saldos se a conta contábil estiver __inativada, porém __houver a mesma conta com Data de Validade Anterior com a situação __Ativa__\.

Rogério Ohashi

13/07/2022

MFS\-89543

Tratamento na geração do Processo de Encerramento do Exercício, para considerar o campo “Centro de Custo de Contrapartida” para efetuar os lançamentos de contrapartida para a tabela de Saldos por Centro de Custos \(SAFX80\)\.

Rogério Ohashi

11/11/2022

MFS\-96911

Tratamento na geração do Processo de Encerramento do Exercício, para considerar o Campo de “Dia e Mês do Encerramento do Exercício Social”, para atendimento aos clientes com Situação Especial, em que a data seja diferente de 31/12\.

Rogério Ohashi

04/05/2023

MFS\-532288

Readequação da Regra para Geração do arquivo Meio Magnético para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis \+ Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, recuperando o Saldo das Tabelas SAFX02 e SAFX80, da mesma conta contábil para o mesmo período\.

Rogério Ohashi

20/02/2026

MFS\-1040618

Inclusão de dois novos parâmetros para gerar os lançamentos de encerramento: “Centralizado” e “Geração para empresas com lançamentos/saldos entre filiais” conforme cenário/solicitação do cliente Bunge\.

Lyene Benvenutti

# <a id="_Toc462320892"></a><a id="_Toc27038220"></a><a id="_Toc48738318"></a>INTRODUÇÃO* *

Este processo deverá ser utilizado pelas empresas que não tenham realizado os lançamentos contábeis de encerramento das contas de resultado\.

# <a id="_Toc27038221"></a><a id="_Toc48738319"></a>DOCUMENTOS DE REFERÊNCIA

*MTZ\-Tela\_Encerramento\_de\_Resultado\.docx*

# <a id="_Toc27038222"></a><a id="_Toc48738320"></a>DEFINIÇÃO DAS REGRAS

__Número__

__Regra__

__Demanda__

RP00

Esta funcionalidade tem o propósito de gerar os lançamentos de encerramento de contas de natureza de resultado, além de criar o respectivo lançamento de contrapartida na conta \(indicada na tela de geração ‘Resultado de Encerramento’ e atualizar os saldos das contas de resultados\.

Esta rotina será acionada através da tela ‘Resultado de Encerramento’, localizada no Menu Sped, Módulo: Escrituração Contábil Digital à Geraçãoà Encerramento do Resultado

__\[MFS\-96911\] __Tratamento para considerar o Campo Dia e Mês do Encerramento do Exercício Social da tela de Dados Iniciais

__Tratamento:__

     __Considerar__ o dia/mês da tela de Dados Iniciais, do parâmetro “Dia e Mês do Encerramento do Exercício Social”, como período para execução do processo de Encerramento\.

__Obs\.:__ Essa alteração é para atendimento aos clientes com Situação Especial, em que a data não seja 31/12\.

__\[MFS\-72676\]__ Tratamento para contas inativadas x contas ativas na tabela SAFX2002 \(Plano de conta\)  

__Tratamento:  __

 

      __Se__ a conta contábil da tabela “X2002\_PLANO\_CONTAS” \(maior validade\), o campo “IND\_SITUACAO” estiver preenchido com “I”;

        __E se houver __a mesma conta contábil com Data de Validade anterior \(cadastrada no Plano de Contas\) com o campo “IND\_SITUACAO” preenchido com “A”;  

         __Então__ considerar o Saldo das tabelas SAFX02, SAFX80, dessa Conta Contábil na geração do Encerramento Contábil\.

__Senão__ não considerar a conta contábil para geração do Encerramento Contábil\.

MFS\-39909

__MFS\-72676__

__MFS\-96911__

<a id="RP01_RecuperacaoC180"></a>RP01

__Se na tela for marcada a opção do Processo “Geração”:__

__\[MFS\-68760\] Regra Parâmetro \- *Considerar Saldos por Centro de Custo \(SAFX80\)*__

O sistema deverá buscar os saldos de todas as contas de resultado, com situação igual a ‘Ativa’, de naturezas igual a ‘3’\- despesa, ‘4’\- receita, ‘5’\- mutações ativas e ‘8’– custo e que possuam saldo final diferente de zero no último dia do período indicado na tela\. 

__Parâmetro Desmarcado: __Caso o parâmetro “__*Considerar Saldos por Centro de Custo \(SAFX80\)*__” estiver desmarcado, o sistema deverá considerar os saldos por conta contábil \(SAFX02\) com valores de saldo final diferente de zero\. 

__Importante:__ Deverão ser considerados __somente__ os saldos por conta contábil da tabela SAFX02, ignorando a tabela de saldo por centro de custos \(SAFX80\), se existir\.

__Parâmetro marcado: __Caso o parâmetro “__*Considerar Saldos por Centro de Custo \(SAFX80\)*__” estiver marcado, o sistema deverá considerar os saldos por conta contábil \(SAFX02\) __*e, também *__os saldos por centro de custo \(SAFX80\), com valores de saldo final diferente de zero\. Caso contrário, __não existindo__ informações de saldo por centro de custos \(SAFX80\), serão consideradas as informações da SAFX02\.

__Importante:__ Caso houver movimentação de saldo por conta contábil \(SAFX02\) e por centro de custos \(SAFX80\) para __mesma conta contábil__\), o sistema deverá efetuar todo o processo de “encerramento” considerando, __somente__, o saldo por centro de custos \(SAFX80\), porém o sistema deverá “__*zerar as contas*__”, __*também*__, os saldos por conta contábil \(SAFX02\), mas __não deverá__ criar os lançamentos de encerramento \(SAFX01\), para não causar duplicidades\.

__\[MFS\-89543\] Tratamento p/ lançamentos de contrapartida utilizando Saldo por Centro de Custo \(SAFX80\)\. __

__Se__ o campo “*Centro de Custo de Contrapartida*” estiver preenchido, o sistema deverá efetuar os lançamentos de contrapartida do encerramento, considerando a tabela de Saldos por centro de custo \(SAFX80\), ou seja, se informado um código de centro de custo válido, os valores dos lançamentos de contrapartida serão gravados no lançamento de Saldo por Centro de Custos \(SAFX80\), considerando a Conta Contábil \+ Centro de Custos, informado em tela\.

 

__Obs\.:__ Se existir um lançamento por Saldo Contábil \(SAFX02\), para o período, da conta contábil informado em tela, a mesma deverá ser desprezada\.

__Senão__ 

__Se__ o campo “*Centro de Custo de Contrapartida*” não estiver preenchido o sistema deverá seguir conforme regras atuais, utilizando somente a conta contábil de contrapartida \(SAFX02\), a Conta Contábil informado em tela\.

__Habilitar__ o campo “*Centro de Custo de Contrapartida*” apenas se o parâmetro “__*Considerar Saldos por Centro de Custo \(SAFX80\)”*__ estiver __marcado__\.

__\[ALTERAÇÃO\- MFS\-532288\]__ Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis \+ Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”\.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis \+ Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período\.

__Obs\.:__ Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis \+ Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos\.

__Tratamento:__

__Parâmetro Marcado:__ Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis \+ Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”\. esteja “__marcado__”, o sistema deverá recuperar as informações de Saldos das tabelas SAFX02 __e__ SAFX80, considerando a mesma Conta Contábil e período\.

__Parâmetro Desmarcado:__ Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis \+ Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”\. esteja “__desmarcado__”, o sistema deverá recuperar as informações dos Saldos da SAFX02 __ou__ SAFX80, conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”\. 

Default: Desmarcado\.

__Importante:__ A regra de preenchimento dos indicadores de Débito e Crédito, para efetuar os lançamentos para o Saldo por Centro de Custos \(SAFX80\) e criação dos Lançamentos Contábeis, bem como a regra de exclusão dos lançamentos para reversão do encerramento, deverá ser semelhante ao processo implementada para o Saldo por conta contábil \(SAFX02\), conforme regras abaixo:

Para cada conta de resultado que for encontrado saldo diferente de zero no último dia do mês indicado na tela, o sistema, deve criar um lançamento de encerramento, para zerar o saldo final desta conta\. Abaixo será detalhado como será gerado os valores dos lançamentos e seus indicadores:  

1. __Valor e Indicador de cada lançamento:__

A composição do valor será feita pela tabela de Saldos 

1\.1 Para indicador de lançamento do saldo inicial = “D”

Valor do saldo a zerar \(saldo final\) = Saldo Inicial \+ Débitos – Créditos

Indicador do saldo a zerar 

Será “D” se o cálculo do valor do saldo a zerar for >0

Será “C” se o cálculo do valor do saldo a zerar for <0

	

1\.2 Para indicador de lançamento do saldo inicial = “C”

Valor do saldo a zerar \(saldo final\) = Saldo Inicial \- Débitos \+ Créditos

Indicador do saldo a zerar

Será “C” se o cálculo do valor do saldo a zerar for >0

Será “D” se o cálculo do valor do saldo a zerar for <0

Valor do lançamento = valor do saldo a zerar \(1\.1 ou 1\.2\)

1.  Indicador do lançamento = indicador inverso ao do valor do saldo a zerar:

	Será “D” se o indicador do saldo a zerar = “C”

	Será “C” se o indicador do saldo a zerar = “D”

Dados a serem gravados na SAFX01 \(Lançamento de Encerramento\):

Campo 

Conteúdo

Empresa 

Empresa informada na tela de processamento

Data do Lançamento

Último dia do período \(mm/aaaa\) informado na tela de processamento

Conta contábil

Código da conta contábil \(de natureza de resultado\)

Contrapartida

Conta contábil de contrapartida informada na tela de processamento \(conta de patrimônio líquido\)

Centro de Custo

Informar o centro de custo, somente se houver centro de custo 

Valor do Lançamento

Cálculo demonstrado acima \(item 1\)

Indicador do Lançamento

Cálculo demonstrado acima \(item 2\)

Arquivamento

Será calculado pelo sistema, concatenando:

 __E__ “__\-__“ <<__Código do Estabelecimento__>> “__\-__“ <<__número sequencial__\*>>

\*Número sequencial é fixo 10 posições, caso necessário incluir zeros a esquerda para atingir a quantidade,

Histórico complementar

__Considerar o  Histórico da Conta de Resultado, indicado na tela __

Tipo de Lançamento

Fixar “Encerramento”

Número do Lançamento

Será calculado pelo sistema, concatenando:

__“E”__ \+ “MM” \+ “AAAA” \+ <<__número sequencial__\*>>

Onde:

MM = mês;

AAAA = Ano\.

\*Número sequencial é fixo 10 posições, caso necessário incluir zeros a esquerda para atingir a quantidade\.

Ex\.: E1220200000000001

Para cada Lançamento de encerramento criado, geraremos um lançamento da Contrapartida:

Campo 

Conteúdo

Empresa 

Empresa informada na tela de processamento

Data do Lançamento

Último dia do período \(mm/aaaa\) informado na tela de processamento

Conta contábil

Código da conta contábil \(de natureza de PL, indicada na tela de processamento\)

Centro de Custo

Informar o centro de custo, somente se houver centro de custo \(Nova regra\)\.

Contrapartida

Nulo

Valor do Lançamento

Mesmo valor de lançamento gerado para a de resultado a ser encerrada,

Indicador do Lançamento

Indicador inverso ao indicador obtido no lançamento de encerramento\.

Número de arquivamento

Será calculado pelo sistema, concatenando:

 __E__ “__\-__“ <<__Código do Estabelecimento__>> “__\-__“ <<__número sequencial__\*>>

\*Número sequencial é fixo 10 posições, caso necessário incluir zeros a esquerda para atingir a quantidade,

Histórico complementar

__ Considerar o   Histórico da ContraPartida,  indicado na tela__

Tipo de Lançamento

Fixar “Encerramento”

Número do Lançamento

Será calculado pelo sistema, concatenando:

__“E”__ \+ “MM” \+ “AAAA” \+ <<__número sequencial__\*>>

Onde:

MM = mês;

AAAA = Ano\.

\*Número sequencial é fixo 10 posições, caso necessário incluir zeros a esquerda para atingir a quantidade\.

Ex\.: E1220200000000001

Ao final do processamento \(criação dos lançamentos de encerramento\), os valores \(total de débito, total de crédito e saldo final\) das contas de resultado deverão ser recalculados na tabela de saldos/saldos por centro de custo \(quando se aplicar\)\.

Isto permitirá que os valores de lançamentos e saldo final da Tabela de Saldos, ou Saldos por Centro de Custo reflitam os novos valores, considerando os lançamentos criados por este processamento\.

\[__MFS\-62795__\]__ Tratamento Geração Processo – Criar os Lançamentos de Encerramento\.__

\- Quando a opção do Processo “Criar os Lançamento de Encerramento” for marcada, para garantir que não haverá duplicidade de informações, caso seja executado novamente, o sistema deverá bloquear a execução, caso exista lançamentos do Tipo E\.

   __Se__ houver lançamentos no campo “tipo\_lancto” da tabela X01\_contabil igual a “E”\.

     __Não executar__ \(Bloquear\) a geração do processo do Processo “Criar os Lançamento de Encerramento” e gravar Log de Geração:  

   Criar os Lançamentos de Encerramento à gravar mensagem no log com a seguinte descrição: “Identificado lançamentos na base com o Tipo de Lançamento Igual a E, antes de executar novamente o processo, executar o processo de “Excluir os Lançamentos de Encerramento Criados pelo Sistema”\.

MFS\-39909

MFS\-34603

MFS\-68760

MFS\-89543

MFS\-67497

MFS\-89543

MFS\-532288

RP02

__Se na tela for marcada a opção do Processo “Excluir os Lançamento de Encerramento Criados pelo Sistema”:__

O sistema deve excluir todos os registros que foram calculados/criados por este processo \(excluir os lançamentos de encerramento, o lançamento de contrapartida e voltar os valores \(total de crédito, total de débito e saldo final\), da tabela de saldos / saldos por centro de custo \(quando se aplicar\)\.

MFS\-39909

MFS\-34603

RP03

__Aba LOGs__

- Caso já exista na base o lançamento de encerramento para a conta/ou conta e centro de custo de resultado, exibir a mensagem de erro no log “O lançamento de encerramento não foi criado, pois já existe na base”\. Exibir no log os campos necessários para facilitar a identificação da conta e lançamento pelo usuário\.
- Apresentar os totais de quantos lançamentos de encerramento, contrapartida foram criados\. Quantos saldos foram atualizados\. 
- Apresentar no log as contas de resultado que não foram calculados/criados os lançamentos de encerramento pois estavam com situação igual a ‘Inativa’, Critério completo de seleção desses cadastros: Situação Inativa, naturezas iguais a ‘3’\- despesa, ‘4’\- receita, ‘5’ – mutações ativa e ‘8’\- custo e que possuem saldo final diferente de zero no último dia do período indicado na tela\)\. Deve ser exibida a mensagem: “Não foi criado o lançamento de encerramento para a conta, pois a mesma está cadastrada com situação Inativa\.” Exibir no log os campos necessários para facilitar a identificação da conta\.

MFS\-39909

MFS\-34603

RP04

__Aba Relatório de Conferência__

__\[MFS\-68760\]__ __Tratamento Relatório de Conferência__

*Este relatório deverá demonstrar um resumo \(por conta de resultado\), do saldo existente anteriormente \(antes do processo\) e o saldo atualizado conforme abaixo:*

__\- Parâmetro: *Considerar Saldos por Centro de Custo \(SAFX80\)*__

__Parâmetro Desmarcado: __Caso o parâmetro “__*Considerar Saldos por Centro de Custo \(SAFX80\)*__” estiver desmarcado, o sistema deverá demonstrar no Relatório de Conferência *um resumo \(por conta de resultado\), do saldo existente anteriormente \(antes do processo\) e o saldo atualizado, considerando somente a SAFX02\.*

__Parâmetro marcado: __Caso o parâmetro “__*Considerar Saldos por Centro de Custo \(SAFX80\)*__” estiver marcado, o sistema deverá demonstrar no Relatório de Conferência *um resumo \(por conta de resultado\), do saldo existente anteriormente \(antes do processo\) e o saldo atualizado, considerando a SAFX80 e SAFX02, \(porém a SAFX02 deverá ser utilizado, *__*somente*__*,*__* *__*se não existir o saldo na SAFX80\)\.*

MFS\-68760

RP05

__\[MFS\-1040618\]__ Inclusão de dois novos parâmetros conforme cenário/solicitação do cliente Bunge\.

 

Criar um novo parâmetro: "__Centralizado__"

Deve vir habilitado por padrão\.

Se habilitado:

        deve exibir os estabelecimentos que o usuário tem acesso no quadro de estabelecimentos para o usuário selecionar  
        deve gerar um arquivo com os lançamentos de encerramento para todos os estabelecimentos centralizados que foram selecionados

Criar um novo parâmetro: "__Geração para empresas com lançamentos/saldos entre filiais__"

Deve vir desabilitado por padrão, mantendo o comportamento atual do sistema\.

Se habilitado:

        deve desabilitar automaticamente o parâmetro “Centralizado”

        deve exibir apenas a opção “Todos” para o usuário selecionar no quadro de estabelecimentos

        deve gerar um arquivo com os lançamentos de encerramento ocorridos entre os estabelecimentos

MFS\-1040618

