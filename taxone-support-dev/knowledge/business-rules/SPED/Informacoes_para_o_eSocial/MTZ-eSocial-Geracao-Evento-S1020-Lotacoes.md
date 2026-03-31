# MTZ-eSocial-Geracao-Evento-S1020-Lotacoes

- **Fonte:** MTZ-eSocial-Geracao-Evento-S1020-Lotacoes.docx
- **Modificado:** 2022-11-04
- **Tamanho:** 86 KB

---

THOMSON REUTERS

Módulo eSocial

Geração Evento S\-1020 \- Lotações

__Localização__: Menu SPED, módulo Informações para o eSocial, menu Geração 🡪 Geração dos Cadastros 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS15869

Geração do evento das Lotações \(S\-1020\)

Geração dos dados do evento das Lotações \(S\-1020\)\.

08/01/2018 

\(criação do documento\)

MFS16751

Controle dos Status x Regeração

Críticas em relação a regeração dos eventos\. 

28/03/2018

MFS21383

Lara Aline

Inclusão da rotina de geração de Alteração e Exclusão\.

08/10/2018

MFS25900

Liliane Assaf

Criação da parametrização de setores relacionados aos Estabelecimentos Centralizadores\. 

15/04/2019

__MFS\-88130__

__Elisabete Costa__

__Alterações para versão S1\.0\.__

__21/06/2022__

__MFS\-96008 __

__Elisabete Costa__

Retirada do Módulo: __Informações para o E\-Social__ do T1

__04/11/2022__

Sumário

[1\.	Parâmetros da Tela	2](#_Toc517780114)

[2\.	Recuperação dos Dados e Processamento	2](#_Toc517780115)

[3\.	Verificação do Status de Eventos já Gerados	3](#_Toc517780116)

[4\.	Gravação dos Dados	5](#_Toc517780117)

__Devido ao end\-of\-support da mensageria OS E\-Social, e a não utilização de clientes no Tax One integrados, o módulo Informações para o E\-Social será retirado do TAX ONE e deverá permanecer no DW\.__

# <a id="_Toc517780114"></a>Parâmetros da Tela 

Este documento é específico das regras de geração do evento S\-1020\.

Para consultar a tela da geração e o funcionamento dos parâmetros, ver documento “*MTZ\-eSocial\-Geracao\-Cadastros*”\.

Nesta geração os dados serão armazenados em tabelas, já com o formato e hierarquia exigidos no layout do eSocial, para posterior conferência do usuário, e geração dos arquivos XML\.

# <a id="_Toc350763252"></a><a id="_Toc517780115"></a>Recuperação dos Dados e Processamento

Origem dos dados: \- SAFX2037 \- Tabela de Cadastro dos Setores

                               \- Parametrização “Dados Iniciais” do Módulo eSocial

                               \- Parametrização “Informações dos Setores do Estabelecimento” do Módulo eSocial

Critérios para a recuperação dos dados da parametrização “Dados Iniciais”:

     Esta parametrização é por estabelecimento centralizador, e para recuperar os dados, considerar:

- Estabelecimento – estabelecimento selecionado na tela da geração;

Critérios para a recuperação dos dados da SAFX2037:

- Grupo do Setor \(SAFX2037\) \-  Considerar o Grupo de > data de validade que seja <= a data inicial do período informado em tela, para a qual a SAFX2037 esteja associada;
- Data de Validade Inicial do Setor SAFX2037 – Apenas os setores cuja data de validade inicial se enquadre no período informado em tela;

\[MFS25900\]

Critério de recuperação da Parametrização “Informações dos Setores do Estabelecimento”:

Caso o estabelecimento selecionado para geração possua parametrização de “Informações dos Setores do Estabelecimento” então:

Recuperar apenas os Setores parametrizados para o Estabelecimento \(tabela ESOCIAL\_PAR\_SETOR\_ESTAB\)\. 

Considerar os critérios:

- Estabelecimento \(ESOCIAL\_PAR\_SETOR\_ESTAB\)    = estabelecimento selecionado na tela da geração;
- Grupo do Setor \(ESOCIAL\_PAR\_SETOR\_ESTAB\)      = Grupo do Setor \(SAFX2037\);
- Código do Setor \(ESOCIAL\_PAR\_SETOR\_ESTAB\)    = Código do Setor \(SAFX2037\);
- Validade do Setor \(ESOCIAL\_PAR\_SETOR\_ESTAB\) = Validade do Setor \(SAFX2037\);

# <a id="_Toc509582647"></a><a id="_Toc509925718"></a><a id="_Toc517780116"></a><a id="_Hlk509925752"></a>Verificação do Status de Eventos já Gerados

__MFS16751__: Nesta MFS foi implementada a crítica dos status dos eventos já gerados anteriormente\. O objetivo é verificar se o evento pode ou não ser regerado, o que depende do status que constar na tabela da geração \(ESOCIAL\_PGER\_S1020\_OC, coluna IND\_STATUS\)\.

Para cada lotação recuperada, conforme os critérios descritos no item 2, será verificado se já existe um evento gerado para a mesma data de validade\.

__Caso não:__ 

      O evento da lotação será gerado normalmente, como definido no item “*4\-Gravação dos Dados*”\.  

__Caso sim:__ 

      A geração de um novo evento para a lotação dependerá do status do evento já existente, da seguinte forma:

\[MFS21383\]

__Status__

__Permite regeração dos dados__

1\-Aguardando geração XML

Sim

3\-Enviando para mensageria

Não

4\-Erro geração XML

Sim

5\-Evento recebido pela mensageria

Não

6\-Evento rejeitado pela mensageria

Sim 

7\-Em Processamento \(mensageria\)

Não

8\-Recebido pelo Fisco com sucesso

<a id="OLE_LINK5"></a>Sim \(Alteração/Exclusão\)

9\-Recebido pelo Fisco com advertência

Sim \(Alteração/Exclusão\)

10\-Rejeitado pelo Fisco

Sim

12\-Evento Excluído

Sim

14\-Evento excluído na mensageria

Sim

15\-Erro técnico na mensageria

Sim__ __

         Se o status do evento já existente __não permitir regeração__:

               Nesse caso a lotação em questão será desconsiderada da geração, e será gravada a seguinte mensagem de aviso no log:

*                    Aviso: Já existe evento anterior gerado para a lotação\. O status do evento não permite uma nova geração\.*

*                   Dados do Registro:  Código do Setor: XXXXXXX, Validade Inicial: XX/XXXX*

         Se o status do evento já existente __permitir regeração:__

Se status = ‘1\-Aguardando geração XML’, ‘4\-Erro geração XML’, ‘6\-Evento rejeitado pela mensageria’ __\(\*\*\*\)__, ‘10\-Rejeitado pelo Fisco’ __\(\*\*\*\)__, ‘14\-Evento excluído na mensageria’ ou ‘15\-Erro técnico na mensageria’:

Nesse caso o setor em questão será regerado normalmente, como sendo a mesma operação gerada anteriormente de INCLUSÃO, ALTERAÇÃO ou EXCLUSÃO respectivamente;

      Se status = ‘8\-Recebido pelo Fisco com sucesso’ __\(\*\*\*\) __ou ‘9\-Recebido pelo Fisco com advertência’ __\(\*\*\*\)__:

Nesse caso o setor em questão será regerado normalmente SOMENTE se for identificada alguma alteração nas informações de setor ou exclusão das informações de setor, sendo uma operação de ALTERAÇÃO caso houver alteração ou uma operação de EXCLUSÃO caso houver exclusão\. Se não houver alteração ou exclusão não será permitida a regeração;

      Se status = ‘12\-Evento Excluído’ __\(\*\*\*\)__:

                	Nesse caso o setor em questão será regerado normalmente, como sendo uma nova operação de INCLUSÃO;

__\*\*\* Importante:__ Status que deverão manter o histórico, ou seja, o histórico do evento anterior continuará mesmo após a regeração do evento:

6\-Evento rejeitado pela mensageria 

8\-Recebido pelo Fisco com sucesso

9\-Recebido pelo Fisco com advertência

10\-Rejeitado pelo Fisco

12\-Evento Excluído

Para os demais Status serão descartados e substituídos pelos novos eventos regerados\.

*Sobre a limpeza do evento já existente: Se o status do evento já existente for = *__*1*__* \(Aguardando geração XML\), *__*4*__* \(Erro geração XML\) ou *__*14*__* \(Evento excluído na mensageria\), este evento será apagado ao efetuar a regeração de um novo evento\. Nos demais casos, a limpeza do evento já existente não será feita \(para manter o histórico dos erros ocorridos\), e será feita apenas a regeração de um novo evento\.*

__\(\*\*\*\) __*Os status 8 e 9 \(Recebido pelo Fisco com Sucesso ou Advertência\) permitem a regeração de um evento de cadastro no caso de uma alteração ou exclusão do cadastro\. No entanto, este cenário ainda não será tratado no eSocial, uma vez que ainda não foi implementado o controle das alterações \(manutenção e importação dos cadastros\)\.*

# <a id="_Toc517780117"></a>Gravação dos Dados

Para cada setor recuperado, será gerado um evento S\-1020 com as seguintes informações: 

__Registro evtTabLotação__ – Evento tabela de Lotações\.

id

Identificação do evento, conforme REGRA\_VALIDA\_ID\_EVENTO:

“ID” \+ “1” \+ CNPJ do estabelecimento \+ data da geração \(AAAAMMDD\) \+ hora da geração \(HHMMSS\) \+ sequencial

<a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>CNPJ – 8 primeiras posições do CNPJ, completando com zeros à direita;

Sequencial \(99999\) \- Número sequencial da chave\. Deve ser incrementado apenas quando houver a geração de eventos na mesma data/hora\. 

__Registro ideEvento__ \- Informações de Identificação do evento\.

tpAmb

Campo “Tipo de ambiente” da parametrização “Dados Iniciais” \(ver acima a regra para a recuperação dos dados desta parametrização\)

procEmi

Conteúdo fixo = “1” \(= Aplicativo do empregador\)

verProc 

Versão do sistema DW\. Esta informação é gerada de forma fixa = “V2R010”\. 

*Obs: A princípio, a definição previa informar neste campo a versão do eSocial informada na tela da geração\. No entanto, este entendimento é equivocado, pois como descreve o manual trata\-se da versão do aplicativo \(do empregador ou governamental\) utilizado para gerar o evento\. No caso, trata\-se da versão do próprio DW\. O REINF já trabalha desta forma\.*

__Registro ideEmpregador__ \- Informações de identificação do empregador\.

tpInsc

Conteúdo fixo = “1”

nrInsc

CNPJ do estabelecimento, considerando apenas as 8 primeiras posições do CNPJ, completando com zeros à direita;

\[MFS21383\]

__Registro ideLotacao__ \- Informações de identificação da lotação __\(Inclusão\)__

__*Critérios:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1020\_OC campo “IND\_OPER” igual a “I”\.__

codLotacao

Campo 01\-Código do Setor

iniValid

Mês a ano da data de validade inicial do Setor \(campo 02\-Data Inico/Inclusão/Alteração\)

fimValid

Mês a ano da data de validade final do Setor \(campo 05\-Data de Validade FinaI\)

Se a validade final não estiver preenchida, este campo não será gerado\.

<a id="OLE_LINK9"></a><a id="OLE_LINK10"></a><a id="OLE_LINK11"></a>__Registro dadosLotacao__ \- Detalhamento das informações da lotação __\(Inclusão\)__

__*Critérios:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1020\_OC campo “IND\_OPER” igual a “I”\.__

<a id="_Hlk501028537"></a>tpLotacao

Campo 06\-Tipo de Lotação Tributária

Caso este campo não esteja preenchido na SAFX2037, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Tipo de Lotação Tributária \(tpLotacao\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “06\-Tipo de Lotação Tributária” da Tabela de Setores \(SAFX2037\)*

*Dados do Registro: Código do Setor: XXXXXXXXXX*

    

tpInsc

Campo 07\-Tipo de Inscrição da Lotação

Caso este campo não esteja preenchido na SAFX2037 __e__ o Tipo da Lotação Tributária = 02, 03, 04, 05, 06, 07, 08 ou 09, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Tipo de Inscrição \(tpInscr\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “07\-Tipo de Inscrição da Lotação” da Tabela de Setores \(SAFX2037\)*

*Dados do Registro: Código do Setor: XXXXXXXXXX*

nrInsc

Campo 08\-Número de Inscrição da Lotação

Caso este campo não esteja preenchido na SAFX2037 __e__ o Tipo da Lotação Tributária = 02, 03, 04, 05, 06, 07, 08 ou 09, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Número de Inscrição \(tpInscr\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “08\-Número de Inscrição da Lotação” da Tabela de Setores \(SAFX2037\)*

*Dados do Registro: Código do Setor: XXXXXXXXXX*

<a id="OLE_LINK16"></a><a id="OLE_LINK17"></a><a id="OLE_LINK18"></a>__Registro fpasLotacao__ – Informações do FPAS e Terceiros __\(Inclusão\)__

__*Critérios:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1020\_OC campo “IND\_OPER” igual a “I”\.__

fpas

Campo 09\-Código FPAS

Caso este campo não esteja preenchido na SAFX2037, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Código FPAS \(fpas\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “09\-Código FPAS” da Tabela de Setores \(SAFX2037\)*

*Dados do Registro: Código do Setor: XXXXXXXXXX*

codTercs

Campo 10\-Código Terceiros

Caso este campo não esteja preenchido na SAFX2037, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Código de Terceiros \(codTercs\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “10\-Código Terceiros” da Tabela de Setores \(SAFX2037\)*

*Dados do Registro: Código do Setor: XXXXXXXXXX*

codTercsSusp

Campo 11\-Código Combinado de Terceiros \(Recolhimento Suspenso\)

__Registro procJudTerceiro__ – Informações de processo sobre as contribuições destinadas a outras Entidades e Fundos \(Terceiros\)\. __\(Inclusão\)__

Caso não exista a informação deste tipo de processo, este registro __*não*__ será gerado\.

A verificação será feita pelo preenchimento do campo “12\-Código Terceiros – Processo”, ou seja, sempre que este campo estiver preenchido na SAFX2037, o registro procJudTerceiro será gerado\.

__*Critérios:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1020\_OC campo “IND\_OPER” igual a “I”\.__

codTerc

Campo 12\-Código Terceiros – Processo

nrProcJud

Campo 14\-Número do Processo

Caso este campo não esteja preenchido na SAFX2037, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Número de Processo Judicial \(nrProcJud\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “14\-Número do Processo” da Tabela de Setores \(SAFX2037\)*

*Dados do Registro: Código do Setor: XXXXXXXXXX*

codSusp

Campo 15\-Código do Indicativo da Suspensão

Caso este campo não esteja preenchido na SAFX2037, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo *Código do Indicativo da Suspensão *\(codSusp\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “15\-Código do Indicativo da Suspensão” da Tabela de Setores \(SAFX2037\)*

*Dados do Registro: Código do Setor: XXXXXXXXXX*

__Registro dadosOpPort __– Informações do operador portuário\. __\(Inclusão\)__

Caso não exista a informação, este registro __*não*__ será gerado\.

__*Critérios:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1020\_OC campo “IND\_OPER” igual a “I”\.__

__aliqRat__

__MFS\-88130__:__VrsS\-1\.0__

Campo 16\-Alíquota RAT

__A partir da versão S1\.0__, os valores válidos são:

1, 2, 3\.

Nos casos em que o declarante possuir processo judicial/administrativo com decisão/sentença favorável à utilização de alíquota GILRAT ou do FAP diferentes do que é definido pela administração, o declarante deve preencher os campos \{aliqRat\} e \{fap\} com os valores correspondentes\.

__Fap__

__MFS\-88130__:__VrsS\-1\.0__

Campo 17\-Fator Acidentário de Prevenção

__A partir da versão S\-1\.0__

Nos casos em que o declarante possuir processo judicial/administrativo com decisão/sentença favorável à utilização de alíquota GILRAT ou do FAP diferentes do que é definido pela administração, o declarante deve preencher os campos \{aliqRat\} e \{fap\} com os valores correspondentes\.

__Registro ideLotacao__ \- Informações de identificação da lotação __\(Alteração\)__

__*Critérios:*__ Este registro servirá para identificar as informações de alteração do registro, será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1020\_OC campo “IND\_OPER” igual a “A”\.__

Se houve o primeiro envio do evento S1020 com sucesso ou advertência e após for identificado qualquer alteração nas informações do cadastro dos setores será a condição para o registro ser gerado\.

codLotacao

Campo 01\-Código do Setor

iniValid

Mês a ano da data de validade inicial do Setor \(campo 02\-Data Início/Inclusão/Alteração\)

Obs: A informação recuperada do campo data de validade inicial do setor será a informação sem a alteração, ou seja, a data informada anteriormente no registro que se pretende alterar\. A informação nova alterada será gerada no Registro novaValidade\.

fimValid

Mês a ano da data de validade final do Setor \(campo 05\-Data de Validade FinaI\)

Se a validade final não estiver preenchida, este campo não será gerado\.

Obs: A informação recuperada do campo data de validade final do setor será a informação sem a alteração, ou seja, a data informada anteriormente no registro que se pretende alterar\. A informação nova alterada será gerada no Registro novaValidade\.

__Registro dadosLotacao__ \- Detalhamento das informações da lotação __\(Alteração\)__

__*Critérios:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1020\_OC campo “IND\_OPER” igual a “A”\.__

tpLotacao

Campo 06\-Tipo de Lotação Tributária

Caso este campo não esteja preenchido na SAFX2037, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Tipo de Lotação Tributária \(tpLotacao\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “06\-Tipo de Lotação Tributária” da Tabela de Setores \(SAFX2037\)*

*Dados do Registro: Código do Setor: XXXXXXXXXX*

    

tpInsc

Campo 07\-Tipo de Inscrição da Lotação

Caso este campo não esteja preenchido na SAFX2037 __e__ o Tipo da Lotação Tributária = 02, 03, 04, 05, 06, 07, 08 ou 09, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Tipo de Inscrição \(tpInscr\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “07\-Tipo de Inscrição da Lotação” da Tabela de Setores \(SAFX2037\)*

*Dados do Registro: Código do Setor: XXXXXXXXXX*

nrInsc

Campo 08\-Número de Inscrição da Lotação

Caso este campo não esteja preenchido na SAFX2037 __e__ o Tipo da Lotação Tributária = 02, 03, 04, 05, 06, 07, 08 ou 09, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Número de Inscrição \(tpInscr\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “08\-Número de Inscrição da Lotação” da Tabela de Setores \(SAFX2037\)*

*Dados do Registro: Código do Setor: XXXXXXXXXX*

__Registro fpasLotacao__ – Informações do FPAS e Terceiros __\(Alteração\)__

__*Critérios:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1020\_OC campo “IND\_OPER” igual a “A”\.__

fpas

Campo 09\-Código FPAS

Caso este campo não esteja preenchido na SAFX2037, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Código FPAS \(fpas\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “09\-Código FPAS” da Tabela de Setores \(SAFX2037\)*

*Dados do Registro: Código do Setor: XXXXXXXXXX*

codTercs

Campo 10\-Código Terceiros

Caso este campo não esteja preenchido na SAFX2037, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Código de Terceiros \(codTercs\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “10\-Código Terceiros” da Tabela de Setores \(SAFX2037\)*

*Dados do Registro: Código do Setor: XXXXXXXXXX*

codTercsSusp

Campo 11\-Código Combinado de Terceiros \(Recolhimento Suspenso\)

__Registro procJudTerceiro__ – Informações de processo sobre as contribuições destinadas a outras Entidades e Fundos \(Terceiros\)\. __\(Alteração\)__

Caso não exista a informação deste tipo de processo, este registro __*não*__ será gerado\.

A verificação será feita pelo preenchimento do campo “12\-Código Terceiros – Processo”, ou seja, sempre que este campo estiver preenchido na SAFX2037, o registro procJudTerceiro será gerado\.

__*Critérios:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1020\_OC campo “IND\_OPER” igual a “A”\.__

codTerc

Campo 12\-Código Terceiros – Processo

nrProcJud

Campo 14\-Número do Processo

Caso este campo não esteja preenchido na SAFX2037, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo Número de Processo Judicial \(nrProcJud\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “14\-Número do Processo” da Tabela de Setores \(SAFX2037\)*

*Dados do Registro: Código do Setor: XXXXXXXXXX*

codSusp

Campo 15\-Código do Indicativo da Suspensão

Caso este campo não esteja preenchido na SAFX2037, será gerada a seguinte mensagem de aviso no log de erros:

*Erro: O campo *Código do Indicativo da Suspensão *\(codSusp\) é de preenchimento obrigatório e não foi informado*

*Origem: Campo “15\-Código do Indicativo da Suspensão” da Tabela de Setores \(SAFX2037\)*

*Dados do Registro: Código do Setor: XXXXXXXXXX*

<a id="_Hlk522549207"></a>

__Registro dadosOpPort __– Informações do operador portuário\. __\(Alteração\)__

Caso não exista a informação, este registro __*não*__ será gerado\.

__*Critérios:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1020\_OC campo “IND\_OPER” igual a “A”\.__

__aliqRat__

__MFS\-88130__:__VrsS\-1\.0__

Campo 16\-Alíquota RAT

__A partir da versão S1\.0__, os valores válidos são:

1, 2, 3\.

Nos casos em que o declarante possuir processo judicial/administrativo com decisão/sentença favorável à utilização de alíquota GILRAT ou do FAP diferentes do que é definido pela administração, o declarante deve preencher os campos \{aliqRat\} e \{fap\} com os valores correspondentes\.

__Fap__

__MFS\-88130__:__VrsS\-1\.0__

Campo 17\-Fator Acidentário de Prevenção

__A partir da versão S\-1\.0: __

Nos casos em que o declarante possuir processo judicial/administrativo com decisão/sentença favorável à utilização de alíquota GILRAT ou do FAP diferentes do que é definido pela administração, o declarante deve preencher os campos \{aliqRat\} e \{fap\} com os valores correspondentes\.

__Registro novaValidade__ \- Informação exclusivamente em caso de alteração do período de validade das informações do registro identificado no evento\.__ \(Alteração\)__

__*Critério:*__ Este registro servirá para identificar as informações de alteração do período de validade do registro\. Será gerado considerando os seguintes critérios: Caso identificado uma alteração no cadastro dos setores quanto à data início e/ou fim validade, este será considerado como um novo cadastro dos setores, ou seja, esta alteração de período de validade será a condição para o registro ser gerado\.

iniValid

Campo “Validade Inicial” da parametrização “Cadastro dos Setores” \(ver acima a regra para a recuperação dos dados desta parametrização\)

fimValid

Campo “Validade Final” da parametrização “Cadastro dos Setores” \(ver acima a regra para a recuperação dos dados desta parametrização\)\. Se a validade final não estiver preenchida, este campo não será gerado\.

__Registro ideLotacao__ \- Informações de identificação da lotação __\(Exclusão\)__

__*Critérios:*__ Este registro servirá para identificar as informações de exclusão do registro, será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1020\_OC campo “IND\_OPER” igual a “E”\.__

Se houve o primeiro envio do evento S1020 com sucesso ou advertência e após for identificado a exclusão das informações do cadastro dos setores será a condição para o registro ser gerado\.

codLotacao

Campo 01\-Código do Setor

iniValid

Mês a ano da data de validade inicial do Setor \(campo 02\-Data Inico/Inclusão/Alteração\)

fimValid

Mês a ano da data de validade final do Setor \(campo 05\-Data de Validade FinaI\)

Se a validade final não estiver preenchida, este campo não será gerado\.

= = = = = =

 

