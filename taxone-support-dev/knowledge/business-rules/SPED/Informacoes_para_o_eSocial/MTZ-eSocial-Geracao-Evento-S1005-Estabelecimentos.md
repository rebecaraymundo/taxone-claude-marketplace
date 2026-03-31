# MTZ-eSocial-Geracao-Evento-S1005-Estabelecimentos

- **Fonte:** MTZ-eSocial-Geracao-Evento-S1005-Estabelecimentos.docx
- **Modificado:** 2022-11-04
- **Tamanho:** 90 KB

---

THOMSON REUTERS

Módulo eSocial

Geração Evento S\-1005 \- Estabelecimento

__Localização__  Menu SPED, módulo Informações para o eSocial, menu Geração 🡪 Geração dos Cadastros 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS15509

Vânia Mattos

Geração do evento S\-1005 \- Cadastro do Estabelecimento

14/12/2017 

\(criação do documento\)

MFS16751

Vânia Mattos 

Críticas em relação a regeração dos eventos\. 

28/03/2018

MFS16757

Lara Aline

Inclusão da rotina de geração de Alteração e Exclusão\.

16/08/2018

MFS23883

Eduardo Vieira Cruz

Parametrização “Informações do Estabelecimento” por centralizador e centralizado

01/02/2019

__MFS\-88128__

Elisabete Costa

__Alterações para versão S1\.0__

14/06/2022

__MFS\-96008__

__Elisabete Costa__

Retirada do Módulo: __Informações para o E\-Social__ do T1

04/11/2022

Sumário

[1\.	Parâmetros da Tela	2](#_Toc517779872)

[2\.	Recuperação dos Dados e Processamento	2](#_Toc517779873)

[3\.	Verificação do Status de Eventos já Gerados	3](#_Toc517779874)

[4\.	Gravação dos Dados	5](#_Toc517779875)

__Devido ao end\-of\-support da mensageria OS E\-Social, e a não utilização de clientes no Tax One integrados, o módulo Informações para o E\-Social será retirado do TAX ONE e deverá permanecer no DW\.__

# <a id="_Toc517779872"></a>Parâmetros da Tela 

Este documento é específico das regras de geração do evento S\-1005\.

Para consultar a tela da geração e o funcionamento dos parâmetros, ver documento “*MTZ\-eSocial\-Geracao\-Cadastros*”\.

Nesta geração os dados serão armazenados em tabelas, já com o formato e hierarquia exigidos no layout do eSocial, para posterior conferência do usuário, e geração dos arquivos XML\.

# <a id="_Toc350763252"></a><a id="_Toc517779873"></a>Recuperação dos Dados e Processamento

Origem dos dados: \- Tabela dos Estabelecimentos

                                \- Parametrização “Dados Iniciais” do Módulo eSocial 

                                \- Parametrização “Informações do Estabelecimento” do Módulo eSocial 

Critérios para a recuperação dos dados da parametrização “Dados Iniciais”:

     Esta parametrização é por estabelecimento centralizador, e para recuperar os dados, considerar:

     \- Estabelecimento – estabelecimento selecionado na tela da geração;

Critérios para a recuperação dos dados da parametrização “Informações do Estabelecimento”:

     Esta parametrização é por estabelecimento centralizador e centralizado, e para recuperar os dados, considerar:

    \- Estabelecimento – estabelecimento selecionado na tela da geração;

    \- Validade inicial – Deve ser a > data de validade inicial cujo mês e ano seja <= ao mês e ano inicial do período informado em tela;

Caso o estabelecimento em questão não tenha dados parametrizados na parametrização “Informações do Estabelecimento”, será gerada a mensagem abaixo no log de erros e este estabelecimento não será processado\.

*“Não foi identificada parametrização válida \(Informações do Estabelecimento\) para o estabelecimento XXXXXX no período informado\. Este estabelecimento não foi processado”*

 \(“XXXXXX” é o código do estabelecimento\)

# <a id="_Toc509582647"></a><a id="_Toc509852358"></a><a id="_Toc517779874"></a>Verificação do Status de Eventos já Gerados

__MFS\-16751__: Nesta MFS foi implementada a crítica dos status dos eventos já gerados anteriormente\. O objetivo é verificar se o evento pode ou não ser regerado, o que depende do status que constar na tabela da geração \(ESOCIAL\_PGER\_S1005\_OC, coluna IND\_STATUS\)\.

Será verificado se já existe um evento gerado para o estabelecimento em questão \(estabelecimento a ser gerado\), para a mesma data de validade\.

__Caso não:__ 

      O evento do estabelecimento será gerado normalmente, como definido no item “*4\-Gravação dos Dados*”\.  

__Caso sim:__ 

A geração de um novo evento para o estabelecimento dependerá do status do evento já existente, da seguinte forma:

__\[MFS\-16757\]__

__Status__

__Permite regeração dos dados__

<a id="_Hlk522205728"></a>1\-Aguardando geração XML

Sim

3\-Enviando para mensageria

Não

<a id="_Hlk522205750"></a>4\-Erro geração XML

Sim

5\-Evento recebido pela mensageria

Não

<a id="_Hlk522205763"></a>6\-Evento rejeitado pela mensageria

Sim 

7\-Em Processamento \(mensageria\)

Não

8\-Recebido pelo Fisco com sucesso

<a id="OLE_LINK5"></a>Sim \(Alteração/Exclusão\)

<a id="_Hlk522205972"></a>9\-Recebido pelo Fisco com advertência

Sim \(Alteração/Exclusão\)

<a id="_Hlk522205783"></a>10\-Rejeitado pelo Fisco

Sim

12\-Evento Excluído

Sim

<a id="_Hlk522205811"></a>14\-Evento excluído na mensageria

Sim

15\-Erro técnico na mensageria

Sim__ __

        Se o status do evento já existente __não__ permitir regeração:

               Nesse caso o estabelecimento em questão será desconsiderado da geração, e será gravada a seguinte mensagem de aviso 

               no log:

*                  Aviso: Já existe evento anterior gerado para o estabelecimento\. O status do evento não permite uma nova geração\.*

*                  Dados do Registro:  Estabelecimento: XXXXX \- XXXXXXXX XXXXXXXXXXXXXXXXXXXX*__*,*__* Validade Inicial: XX/XXXX*

        Se o status do evento já existente permitir regeração:

Se status = ‘1\-Aguardando geração XML’, ‘4\-Erro geração XML’, ‘6\-Evento rejeitado pela mensageria’ __\(\*\*\*\)__, ‘10\-Rejeitado pelo Fisco’ __\(\*\*\*\)__, ‘14\-Evento excluído na mensageria’ ou ‘15\-Erro técnico na mensageria’:

Nesse caso o estabelecimento em questão será regerado normalmente, como sendo a mesma operação gerada anteriormente de INCLUSÃO, ALTERAÇÃO ou EXCLUSÃO respectivamente; 

      Se status = ‘8\-Recebido pelo Fisco com sucesso’ __\(\*\*\*\)__ ou ‘9\-Recebido pelo Fisco com advertência’ __\(\*\*\*\)__:

Nesse caso o estabelecimento em questão será regerado normalmente SOMENTE se for identificada alguma alteração nas informações do estabelecimento ou exclusão das informações do estabelecimento, sendo uma operação de ALTERAÇÃO caso houver alteração ou uma operação de EXCLUSÃO caso houver exclusão\. Se não houver alteração ou exclusão não será permitida a regeração;

      Se status = ‘12\-Evento Excluído’ __\(\*\*\*\)__:

                	Nesse caso o estabelecimento em questão será regerado normalmente, como sendo uma nova operação de INCLUSÃO;

__\*\*\* Importante:__ Status que deverão manter o histórico, ou seja, o histórico do evento anterior continuará mesmo após a regeração do evento:

6\-Evento rejeitado pela mensageria 

8\-Recebido pelo Fisco com sucesso

9\-Recebido pelo Fisco com advertência

10\-Rejeitado pelo Fisco

12\-Evento Excluído

Para os demais Status serão descartados e substituídos pelos novos eventos regerados\.

*Sobre a limpeza do evento já existente: Se o status do evento já existente for = *__*1*__* \(Aguardando geração XML\), *__*4*__* \(Erro geração XML\) ou *__*14*__* \(Evento excluído na mensageria\), este evento será apagado ao efetuar a regeração de um novo evento\. Nos demais casos, a limpeza do evento já existente não será feita \(para manter o histórico dos erros ocorridos\), e será feita apenas a regeração de um novo evento\.*

# <a id="_Toc517779875"></a>Gravação dos Dados

Para cada estabelecimento centralizador selecionado na tela da geração dos dados, será gerado um único evento S\-1005 com as seguintes informações: 

__Registro evtTabEstab__ – Evento tabela de Estabelecimentos\.

__id__

Identificação do evento, conforme REGRA\_VALIDA\_ID\_EVENTO:

“ID” \+ “1” \+ CNPJ do estabelecimento \+ data da geração \(AAAAMMDD\) \+ hora da geração \(HHMMSS\) \+ sequencial

<a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>CNPJ do estabelecimento – 8 primeiras posições do CNPJ, completando com zeros à direita;

Sequencial \(99999\) \- Número sequencial da chave\. Deve ser incrementado apenas quando houver a geração de eventos na mesma data/hora\. 

__Registro ideEvento__ \- Informações de Identificação do evento\.

__tpAmb__

Campo “Tipo de ambiente” da parametrização “Dados Iniciais” \(ver acima a regra para a recuperação dos dados desta parametrização\)

__procEmi__

Conteúdo fixo = “1” \(= Aplicativo do empregador\)

__verProc __

Versão do sistema DW\. Esta informação é gerada de forma fixa = “V2R010”\. 

*Obs: A princípio, a definição previa informar neste campo a versão do eSocial informada na tela da geração\. No entanto, este entendimento é equivocado, pois como descreve o manual trata\-se da versão do aplicativo \(do empregador ou governamental\) utilizado para gerar o evento\. No caso, trata\-se da versão do próprio DW\. O REINF já trabalha desta forma\.*

__Registro ideEmpregador__ \- Informações de identificação do empregador\.

<a id="_Hlk501036993"></a>__tpInsc__

Conteúdo fixo = “1”

__nrInsc__

<a id="OLE_LINK30"></a><a id="OLE_LINK31"></a><a id="OLE_LINK32"></a>CNPJ do estabelecimento, considerando apenas as  8 primeiras posições do CNPJ, completando com zeros à direita;

__\[MFS\-16757\]__

__Registro ideEstab__ \- Informações de identificação do estabelecimento \(Inclusão\)

__*Regra de Seleção:*__ Será gerado considerando os seguintes critérios: Tabela ESOCIAL\_PGER\_<a id="_Hlk522208843"></a>S1005\_OC campo “IND\_OPER” igual a “I”\.

__tpInsc__

Conteúdo fixo = “1”

__nrInsc__

CNPJ do estabelecimento \(neste caso, deve ser o CNPJ completo, com as 14 posições\);

__iniValid__

Campo “Validade Inicial” <a id="OLE_LINK39"></a><a id="OLE_LINK40"></a><a id="OLE_LINK41"></a>da parametrização “Informações do Estabelecimento”<a id="OLE_LINK42"></a><a id="OLE_LINK43"></a><a id="OLE_LINK44"></a> \(ver acima a regra para a recuperação dos dados desta parametrização\)

__fimValid__

Campo “Validade Final” da parametrização “Informações do Estabelecimento” \(ver acima a regra para a recuperação dos dados desta parametrização\)\. Se a validade final não estiver preenchida, este campo não será gerado\.

<a id="OLE_LINK9"></a><a id="OLE_LINK10"></a><a id="OLE_LINK11"></a>__Registro dadosEstab__ \- Detalhamento das informações do estabelecimento __\(Inclusão\) __

__*Regra de Seleção:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1005\_OC campo “IND\_OPER” igual a “I”\.__

<a id="_Hlk501028537"></a>__cnaePrep__

CNAE do estabelecimento centralizador da geração \(campo “Atividade Econômica” do cadastro do estabelecimento\)

__cnpjResp__

CNPJ responsável pela inscrição no cadastro de obras da RFB\.

A partir da versão S1\.0 foi criado o campo cnpjResp\. __O mesmo não deve ser gerado__, pois o campo tpInsc possui o conteúdo fixo=’1’ e de acordo com o layout o campo cnpjResp deve ser igual a '4' \(CNO\-Cadastro Nacional de Obras\)

<a id="OLE_LINK16"></a><a id="OLE_LINK17"></a><a id="OLE_LINK18"></a>__Registro aliqGilrat__ \- Informações sobre a alíquota RAT e o FAP  __\(Inclusão\) __

__*Regra de Seleção:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1005\_OC campo “IND\_OPER” igual a “I”\.__

__aliqRat__

Campo “Alíquota” \(quadro “Informações sobre a alíquota Gilrat”\) da parametrização das informações do estabelecimento;

*Obs: No layout do eSocial está alíquota é um campo numérico de apenas 1 posição\. Mas na tabela da parametrização o campo foi criado com 4 casas decimais apenas por precaução, caso no futuro as alíquotas passem a utilizar decimais\. *

__fap__

Campo “Fator Acidentário de Prevenção \(FAP\)” da parametrização das informações do estabelecimento;

__aliqRatAjust__

__MFS\-88128__:__VrsS\-1\.0__

Resultado da multiplicação: aliqRat x fap; 

Este campo só deve ser gerado até a versão 2\.5, __a partir da versão S1\.0 ele não deve ser gerado\.__

<a id="OLE_LINK15"></a><a id="OLE_LINK19"></a><a id="OLE_LINK20"></a><a id="OLE_LINK21"></a>__Registro procAdmJudRat__ \- Informações de processo sobre a alíquota RAT   __\(Inclusão\) __

Caso não exista a informação deste tipo de processo, este registro *não* será gerado\.

*\(a verificação será feita pelo preenchimento do campo do tipo de processo da alíquota Gilrat\)*

__*Regra de Seleção:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1005\_OC campo “IND\_OPER” igual a “I”\.__

__tpProc__

Tipo do processo do campo “Processo” \(quadro “Informações sobre a alíquota Gilrat”\) da parametrização das informações do estabelecimento ;

__nrProc__

Número do processo do campo “Processo” \(quadro “Informações sobre a alíquota Gilrat”\) da parametrização das informações do estabelecimento;

__codSusp__

Código do Indicativo da Suspensão \(quadro “Informações sobre a alíquota Gilrat”\) da parametrização das informações do estabelecimento;

<a id="OLE_LINK22"></a><a id="OLE_LINK23"></a><a id="OLE_LINK24"></a><a id="OLE_LINK25"></a><a id="OLE_LINK26"></a><a id="OLE_LINK27"></a>__Registro procAdmJudFap__ – Informações de processo sobre o FAP   __\(Inclusão\) __

Caso não exista a informação deste tipo de processo, este registro *não* será gerado\.

*\(a verificação será feita pelo preenchimento do campo do tipo de processo do FAP\)*

__*Regra de Seleção:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1005\_OC campo “IND\_OPER” igual a “I”\.__

__tpProc__

Tipo do processo do campo “Processo” \(quadro “Informações sobre o FAP”\) da parametrização das informações do estabelecimento;

__nrProc__

Número do processo do campo “Processo” \(quadro “Informações sobre o FAP”\) da parametrização das informações do estabelecimento;

__codSusp__

Código do Indicativo da Suspensão \(quadro “Informações sobre o FAP”\) da parametrização das informações do estabelecimento;

__Registro infoTrab__ \- Informações trabalhistas sobre o estabelecimento  __\(Inclusão\) __

__*Regra de Seleção:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1005\_OC campo “IND\_OPER” igual a “I”\.__

__regPt__

__MFS\-88128__:__VrsS\-1\.0__

Opção do campo “Sistema de Controle de Ponto”, da parametrização das informações do estabelecimento;

Este campo só deve ser gerado até a versão 2\.5, __a partir da versão S1\.0 ele não deve ser gerado\.__

__Registro infoApr__ – Informações sobre contratação de aprendiz   __\(Inclusão\) __

__*Regra de Seleção:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1005\_OC campo “IND\_OPER” igual a “I”\.__

__contApr__

__MFS\-88128__:__VrsS\-1\.0__

Opção do campo “Contratação” \(quadro “Informações sobre contratação de aprendiz”\), da parametrização das informações do estabelecimento;

Este campo só deve ser gerado até a versão 2\.5, __a partir da versão S1\.0 ele não deve ser gerado\.__

__nrProcJud__

Número do processo do campo “Processo” \(quadro “Informações sobre contratação de aprendiz”\) da parametrização das informações do estabelecimento\.

Caso este número de processo não esteja preenchido, este campo *não* será gerado\.

__contEntEd__

__MFS\-88128__:__VrsS\-1\.0__

Se o conteúdo do campo “Contratação”  = “1” ou “2”,

Será gravado o conteúdo do campo “Contratação p/intermédio de entidade educativa/prática desportiva” \(S/N\), da       parametrização das informações do estabelecimento;

Senão \(conteúdo = “0”\)

    Este campo não será gerado; 

Este campo só deve ser gerado até a versão 2\.5, __a partir da versão S1\.0 ele não deve ser gerado\.__

__Registro infoEntEduc__ – Identificação de entidade educativa / prática desportiva   __\(Inclusão\) __

__*Regra de Seleção:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1005\_OC campo “IND\_OPER” igual a “I”\.__

__nrInsc__

Campo “CNPJ” \(quadro “Informações sobre contratação de aprendiz”\) da parametrização das informações do estabelecimento\.

Caso o CNPJ não esteja preenchido, este campo não será gerado\.

__Registro infoPCD__ – Informações sobre contratação de pessoas com deficiência   __\(Inclusão\) __

Este registro será gerado apenas se as condições a seguir forem verdadeiras:

\- Quando se tratar do estabelecimento matriz, ou seja, quando o estabelecimento da geração tiver o campo “Matriz/Filial” = Matriz;  

\- Quando o campo “Contratação” \(quadro “Informações sobre contratação de pessoa com deficiência”\) estiver preenchido;

__*Regra de Seleção:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1005\_OC campo “IND\_OPER” igual a “I”\.__

__contPCD__

__MFS\-88128__:__VrsS\-1\.0__

Opção do campo “Contratação” \(quadro “Informações sobre contratação de pessoa com deficiência”\), da parametrização das informações do estabelecimento;

Este campo só deve ser gerado até a versão 2\.5, __a partir da versão S1\.0 ele não deve ser gerado\.__

__nrProcJud__

Número do processo do campo “Processo” \(quadro “Informações sobre contratação de pessoa com deficiência”\) da parametrização das informações do estabelecimento\.

Caso este número de processo não esteja preenchido, este campo *não* será gerado\.

__Registro ideEstab__ \- Informações de identificação do estabelecimento __\(Alteração\)__

__*Critérios:*__ Este registro servirá para identificar as informações de alteração do registro, será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1005\_OC campo “IND\_OPER” igual a “A”\.__

Se houve o primeiro envio do evento S1005 com sucesso ou advertência e após for identificado qualquer alteração nas informações de cadastro do estabelecimento será a condição para o registro ser gerado\.

__tpInsc__

Conteúdo fixo = “1”

__nrInsc__

CNPJ do estabelecimento \(neste caso, deve ser o CNPJ completo, com as 14 posições\);

__iniValid__

Campo “Validade Inicial” da parametrização “Informações do Estabelecimento” \(ver acima a regra para a recuperação dos dados desta parametrização\)

Obs: A informação recuperada do campo “Validade Inicial” da parametrização “Informações do Estabelecimento” será a informação sem a alteração, ou seja, a data informada anteriormente no registro que se pretende alterar\. A informação nova alterada será gerada no Registro novaValidade\.

__fimValid__

Campo “Validade Final” da parametrização “Informações do Estabelecimento” \(ver acima a regra para a recuperação dos dados desta parametrização\)\. Se a validade final não estiver preenchida, este campo não será gerado\.

Obs: A informação recuperada do campo “Validade Final” da parametrização “Informações do Estabelecimento” será a informação sem a alteração, ou seja, a data informada anteriormente no registro que se pretende alterar\. A informação nova alterada será gerada no Registro novaValidade\.

__Registro dadosEstab__ \- Detalhamento das informações do estabelecimento __\(Alteração\)__

__*Critérios:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1005\_OC campo “IND\_OPER” igual a “A”\.__

__cnaePrep__

CNAE do estabelecimento centralizador da geração \(campo “Atividade Econômica” do cadastro do estabelecimento\)

__cnpjResp__

__MFS\-88128__:__VrsS\-1\.0__

CNPJ responsável pela inscrição no cadastro de obras da RFB\.

A partir da versão S1\.0 foi criado o campo cnpjResp\. __O mesmo não deve ser gerado__, pois o campo tpInsc possui o conteúdo fixo=’1’ e de acordo com o layout o campo cnpjResp deve ser igual a '4' \(CNO\-Cadastro Nacional de Obras\)

__Registro aliqGilrat__ \- Informações sobre a alíquota RAT e o FAP __\(Alteração\)__

__*Critérios:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1005\_OC campo “IND\_OPER” igual a “A”\.__

__aliqRat__

Campo “Alíquota” \(quadro “Informações sobre a alíquota Gilrat”\) da parametrização das informações do estabelecimento;

*Obs: No layout do eSocial está alíquota é um campo numérico de apenas 1 posição\. Mas na tabela da parametrização o campo foi criado com 4 casas decimais apenas por precaução, caso no futuro as alíquotas passem a utilizar decimais\. *

__fap__

Campo “Fator Acidentário de Prevenção \(FAP\)” da parametrização das informações do estabelecimento;

__aliqRatAjuste__

__MFS\-88128__:__VrsS\-1\.0__

Resultado da multiplicação: aliqRat x fap;

Este campo só deve ser gerado até a versão 2\.5, __a partir da versão S1\.0 ele não deve ser gerado\.__

__Registro procAdmJudRat__ \- Informações de processo sobre a alíquota RAT    __\(Alteração\)__

Caso não exista a informação deste tipo de processo, este registro *não* será gerado\.

*\(a verificação será feita pelo preenchimento do campo do tipo de processo da alíquota Gilrat\)*

__*Critérios:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1005\_OC campo “IND\_OPER” igual a “A”\.__

__tpProc__

Tipo do processo do campo “Processo” \(quadro “Informações sobre a alíquota Gilrat”\) da parametrização das informações do estabelecimento ;

__nrProc__

Número do processo do campo “Processo” \(quadro “Informações sobre a alíquota Gilrat”\) da parametrização das informações do estabelecimento;

__codSusp__

Código do Indicativo da Suspensão \(quadro “Informações sobre a alíquota Gilrat”\) da parametrização das informações do estabelecimento;

__Registro procAdmJudFap__ – Informações de processo sobre o FAP    __\(Alteração\)__

Caso não exista a informação deste tipo de processo, este registro *não* será gerado\.

*\(a verificação será feita pelo preenchimento do campo do tipo de processo do FAP\)*

__*Critérios:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1005\_OC campo “IND\_OPER” igual a “A”\.__

__tpProc__

Tipo do processo do campo “Processo” \(quadro “Informações sobre o FAP”\) da parametrização das informações do estabelecimento;

__nrProc__

Número do processo do campo “Processo” \(quadro “Informações sobre o FAP”\) da parametrização das informações do estabelecimento;

__codSusp__

Código do Indicativo da Suspensão \(quadro “Informações sobre o FAP”\) da parametrização das informações do estabelecimento;

__Registro infoTrab__ \- Informações trabalhistas sobre o estabelecimento     __\(Alteração\)__

__*Critérios:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1005\_OC campo “IND\_OPER” igual a “A”\.__

__regPt__

__MFS\-88128__:__VrsS\-1\.0__

Opção do campo “Sistema de Controle de Ponto”, da parametrização das informações do estabelecimento;

Este campo só deve ser gerado até a versão 2\.5, __a partir da versão S1\.0 ele não deve ser gerado\.__

__Registro infoApr__ – Informações sobre contratação de aprendiz   __\(Alteração\)__

__*Critérios:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1005\_OC campo “IND\_OPER” igual a “A”\.__

__contApr__

__MFS\-88128__:__VrsS\-1\.0__

Opção do campo “Contratação” \(quadro “Informações sobre contratação de aprendiz”\), da parametrização das informações do estabelecimento;

Este campo só deve ser gerado até a versão 2\.5, __a partir da versão S1\.0 ele não deve ser gerado\.__

__nrProcJud__

Número do processo do campo “Processo” \(quadro “Informações sobre contratação de aprendiz”\) da parametrização das informações do estabelecimento\.

Caso este número de processo não esteja preenchido, este campo *não* será gerado\.

__contEntEd__

__MFS\-88128__:__VrsS\-1\.0__

Se o conteúdo do campo “Contratação”  = “1” ou “2”,

      Será gravado o conteúdo do campo “Contratação p/intermédio de entidade educativa/prática desportiva” \(S/N\), da

      parametrização das informações do estabelecimento;

Senão \(conteúdo = “0”\)

    Este campo não será gerado; 

Este campo só deve ser gerado até a versão 2\.5, __a partir da versão S1\.0 ele não deve ser gerado\.__

__Registro infoEntEduc__ – Identificação de entidade educativa / prática desportiva   __\(Alteração\)__

__*Critérios:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1005\_OC campo “IND\_OPER” igual a “A”\.__

__nrInsc__

Campo “CNPJ” \(quadro “Informações sobre contratação de aprendiz”\) da parametrização das informações do estabelecimento\.

Caso o CNPJ não esteja preenchido, este campo não será gerado\.

__Registro infoPCD__ – Informações sobre contratação de pessoas com deficiência   __\(Alteração\)__

Este registro será gerado apenas se as condições a seguir forem verdadeiras:

\- Quando se tratar do estabelecimento matriz, ou seja, quando o estabelecimento da geração tiver o campo “Matriz/Filial” = Matriz;  

\- Quando o campo “Contratação” \(quadro “Informações sobre contratação de pessoa com deficiência”\) estiver preenchido;

__*Critérios:*__ Será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1005\_OC campo “IND\_OPER” igual a “A”\.__

__contPCD__

__MFS\-88128__:__VrsS\-1\.0__

Opção do campo “Contratação” \(quadro “Informações sobre contratação de pessoa com deficiência”\), da parametrização das informações do estabelecimento;

Este campo só deve ser gerado até a versão 2\.5, __a partir da versão S1\.0 ele não deve ser gerado\.__

__nrProcJud__

Número do processo do campo “Processo” \(quadro “Informações sobre contratação de pessoa com deficiência”\) da parametrização das informações do estabelecimento\.

Caso este número de processo não esteja preenchido, este campo *não* será gerado\.

__Registro novaValidade__ \- Informação exclusivamente em caso de alteração do período de validade das informações do registro identificado no evento\.

__*Critério:*__ Este registro servirá para identificar as informações de alteração do período de validade do registro\. Será gerado considerando os seguintes critérios: Caso identificado uma alteração do processo quanto à data início e/ou fim validade, este será considerado como um novo processo, ou seja, esta alteração de período de validade será a condição para o registro ser gerado\.

__iniValid__

Campo “Validade Inicial” da parametrização “Informações do Estabelecimento” \(ver acima a regra para a recuperação dos dados desta parametrização\)

__fimValid__

Campo “Validade Final” da parametrização “Informações do Estabelecimento” \(ver acima a regra para a recuperação dos dados desta parametrização\)\. Se a validade final não estiver preenchida, este campo não será gerado\.

__Registro ideEstab__ \- Informações de identificação do estabelecimento __\(Exclusão\)__

__*Critérios:*__ Este registro servirá para identificar as informações de exclusão do registro, será gerado considerando os seguintes critérios: __Tabela ESOCIAL\_PGER\_S1005\_OC campo “IND\_OPER” igual a “E”\.__

Se houve o primeiro envio do evento S1005 com sucesso ou advertência e após for identificado a exclusão das informações de cadastro do estabelecimento será a condição para o registro ser gerado\.

__tpInsc__

Conteúdo fixo = “1”

__nrInsc__

CNPJ do estabelecimento \(neste caso, deve ser o CNPJ completo, com as 14 posições\);

__iniValid__

Campo “Validade Inicial” da parametrização “Informações do Estabelecimento” \(ver acima a regra para a recuperação dos dados desta parametrização\)

__fimValid__

Campo “Validade Final” da parametrização “Informações do Estabelecimento” \(ver acima a regra para a recuperação dos dados desta parametrização\)\. Se a validade final não estiver preenchida, este campo não será gerado\.

= = = = = =

