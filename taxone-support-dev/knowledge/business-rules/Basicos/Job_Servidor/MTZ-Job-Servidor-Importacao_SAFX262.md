# MTZ-Job-Servidor-Importacao_SAFX262

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX262.docx
- **Modificado:** 2022-09-27
- **Tamanho:** 71 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX262

Mapeamento para Plano de Contas das Empresas Consolidadas \(ECD\) 

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS15155

Criação da SAFX262 

Criação da SAFX262 para a importação dos dados do Mapeamento do Plano de Contas das Empresas Consolidadas \(módulo ECD\-Escrituração Contábil Digital\)\. 

17/04/2018

MFS18238

Inclusão de Campo na SAFX262

Essa alteração tem como finalidade incluir na tabela SAFX262 o campo “Código da Conta Consolidadora”\. 

14/05/2018

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX262__ 🡪 vide manual de layout

A SAFX262 foi criada na __MFS15155__, para a importação dos dados do Mapeamento do Plano de Contas das Empresas Consolidadas\.

Estas informações são utilizadas na geração do registro K210 da ECD\-Escrituração Contábil Digital\.

__Tabela definitiva__: SPED\_CONTAS\_EMP\_CONS

*OBS: A tabela definitiva não tem a nomenclatura padrão \(“X\.\.\.”\), pois a tela de manutenção destas informações foi criada primeiro, e a SAFX foi criada posteriormente por solicitação de clientes\. Trata\-se de uma tabela “filha” da SAFX240, embora não tenha sido criada uma FK para a tabela “mãe”\. *

__Campos que compõe a chave da tabela definitiva:__

 Código Empresa \+ Código Estabelecimento \+ Data Inicial \+ Data Final \+ Cód\. Empresa Participante \+ Grupo Conta \+ Código Conta

__RN01__

__Campo Código da Empresa__

Campo de preenchimento obrigatório\.

* \(registros das tabelas SAFX sem a informação da Empresa são desconsiderados\)*

__RN02__

__Campo Código do Estabelecimento__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento são desconsiderados\)*

__RN03__

__Campo Data Inicial do Período da Consolidação __

Campo de preenchimento obrigatório\.

Deve ser uma data válida\.

Quando não preenchida ou inválida, será gravada mensagem de erro padrão e o registro não será importado \(Ex: *“*__*Data Inicial do Período da Consolidação não preenchida ou inválida*__*”*\)\.

__RN04__

__Campo Data Final do Período da Consolidação __

Campo de preenchimento obrigatório\.

Deve ser uma data válida\.

Quando não preenchida ou inválida, será gravada uma mensagem de erro no log e o registro *não* será importado \(Ex: *“*__*Data Final do Período da Consolidação não preenchida ou inválida*__*”*\)\.

Deve ser uma data superior ou igual a data informada no campo “*03\-Data Inicial do Período da Consolidação*”\. Caso contrário, será gravada uma mensagem de erro no log e o registro *não* será importado \(Ex: *“*__*A Data Final do Período da Consolidação não pode ser inferior a Data Inicial*__*”*\)\.

__RN05__

__Campo Código da Empresa Participante __

Campo de preenchimento obrigatório\.

Quando não preenchido, será gravada uma mensagem de erro no log e o registro *não* será importado \(Ex: *“*__*O Código da Empresa Participante deve ser informado*__*”*\)\.

O código informado deve constar na tabela “Relação das Empresas Consolidadas” \(SAFX240\), junto com as datas informadas nos campos 03 e 04\. Para essa verificação, será feita a pesquisa na SAFX240 a partir dos seguintes critérios:

     \- COD\_EMPRESA = código da empresa informada no campo 01;

     \- COD\_ESTAB  = código do estabelecimento informado no campo 02;

     \- DATA\_INI\_CONS = data inicial do período da consolidação informada no campo 03; 

     \- DATA\_FIM\_CONS = data final do período da consolidação informada no campo 04;

     \- COD\_EMP\_PART = código da empresa participante informada neste campo \(campo 05\);

Quando não existir o registro na SAFX240, será gravada a seguinte mensagem de erro no log e o registro *não* será importado:

*“*__*O código da Empresa Participante não foi identificado na Tabela de Relação das Empresas Consolidadas para o período informado*__*”*

__RN06__

__Campo Código da Conta Contábil __

Campo de preenchimento obrigatório\.

1\-Crítica do campo não preenchido:

Quando não preenchido, será gravada uma mensagem de erro no log e o registro *não* será importado \(Ex: *“*__*O Código da Conta Contábil deve ser informado*__*”*\)\.

2\-Crítica da existência da conta na SAFX2002:

A conta for informada deve existir na Tabela do Plano de Contas \(SAFX2002\), considerando o Grupo \(Relacionamento Tabela x Grupo\) a ser utilizado __\(\*\*\*\)__, e deve ter uma data de validade inicial que seja <= a data informada no campo 03 \(Data Inicial do Período da Consolidação\) 

Quando o código não existir na SAFX2002 \(*considerando as condições acima*\), será gravada a seguinte mensagem de erro no log, e o registro *não* será importado: 

                                                        __*“Conta contábil não existente ou inválida”*__

__\(\*\*\*\)* *__*Grupo a ser utilizado na pesquisa da SAFX2002: O Grupo a ser utilizado será obtido a partir da regra básica, considerando o Grupo \(Relacionamento Tabelas x Grupos\) de maior data de validade, que seja <= a data informada no campo 03 \(Data Inicial do Período da Consolidação\), e para o qual a tabela SAFX2002 esteja associada\.*

3\-Crítica do indicador do tipo de conta:

Quando a conta contábil for identificada na SAFX2002, será verificada se é uma conta analítica ou sintética, da seguinte forma: 

Se campo “04\-Indicador de Conta” <> ‘A’,

      Neste caso, será gravada a seguinte mensagem de erro no log, e o registro *não* será importado: 

                                                        __*“A conta contábil deve ser uma conta analítica”*__

__RN07__

__Campo Código da Conta Consolidadora__

Esse campo deve retornar apenas as contas analíticas consolidadoras de maior validade, ou seja, quando o campo 14 \- IND\_CONTA\_CONSOLID for = “S” e o campo 04 \- IND\_CONTA = “A”, na tabela SAFX2002 – Tabela do Plano de Contas\.

__Tratamentos:__

- Se o sistema não localizar uma conta analítica consolidado campo 04 \- IND\_CONTA = “A”, deverá exibir a seguinte mensagem: __*“O Código da conta consolidada não está cadastrado ou não é uma conta analítica”\.*__
- Se o sistema não localizar uma conta que faça parte do plano consolidado 14 \- IND\_CONTA\_CONSOLID for = “S”, deverá exibir a seguinte mensagem:__* “O código de conta consolidada deve constar no plano de contas consolidado"\.*__

__Observação:__ A descrição e a data da conta devem ser exibidas na tela somente para visualização\.

Campo Não Obrigatório

Tamanho: 04 Posições

Tipo: Alfanumérico 

MFS18238

