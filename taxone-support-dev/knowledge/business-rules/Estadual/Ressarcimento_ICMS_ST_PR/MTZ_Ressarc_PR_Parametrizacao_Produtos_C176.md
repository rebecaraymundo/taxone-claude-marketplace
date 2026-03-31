# MTZ_Ressarc_PR_Parametrizacao_Produtos_C176

- **Fonte:** MTZ_Ressarc_PR_Parametrizacao_Produtos_C176.docx
- **Modificado:** 2021-03-22
- **Tamanho:** 81 KB

---

THOMSON REUTERS

Módulo Ressarcimento de ICMS ST – PR

Parametrização de Produtos 

__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS ST \- PR, item Parâmetros 🡪 Registro C176 🡪 Produtos

__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS ST \- PR, item Parâmetros 🡪 Produtos

*Obs\.: Originalmente, o módulo do Ressarcimento PR não gerava nenhum arquivo magnético, e o controle do ressarcimento e complemento de ICMS\-ST era feito através do registro C176 do Sped Fiscal \(NPF 027/17\)\. Com a atualização legal da NPF 003/20, o controle passou a ser feito via arquivo magnético, e a norma original foi revogada\. O módulo então passou a atender as duas normas \(027/17 e 003/20\)\. Como já existiam clientes que utilizavam o módulo, a parametrização de Produtos e NCM’s continuou a ser feita através das mesmas tabelas, que são as tabelas existentes no módulo Sped Fiscal para a geração do C176\. Por isso, o módulo do PR não usa as mesmas tabelas dos demais módulos de Ressarcimento, cuja parametrização é feita por UF, ao invés de estabelecimento\.*

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS13569__

Andréa Rocha

Criação da parametrização de produtos para geração dos dados do registro C176\. 

12/09/2017

__MFS33878__

Vânia Mattos

Alteração da parametrização de produtos para atender ao arquivo magnético da NPF 003/2020 – PR

24/02/2020

__MFS43627__

Vânia Mattos

Inclusão do campo “%Redução BC”

11/09/2020

__MFS47333__

Andréa Rocha

Alteração da parametrização para incluir uma tabela de produtos associados\.  Esses produtos serão associados ao produto principal e como a tela não está preparada para trabalhar com produtos associados, o seu layout deve ser alterado para este fim\.

16/12/2020

Sumário

[1\.	Regras Gerais	1](#_Toc67326330)

[2\.	Layout da Tela	1](#_Toc67326331)

[3\.	Regras de Funcionamento dos Campos	1](#_Toc67326332)

[4\.	Regras de Validação	1](#_Toc67326333)

- 
	1. [RN01 – Validação na gravação de um novo registro:	1](#_Toc67326334)

# <a id="_Toc67326330"></a>Regras Gerais

Os dados parametrizados neste item são utilizados na rotina de pré\-geração do registro C176, realizada no menu “Geração 🡪 Registro C176” do módulo Ressarcimento de ICMS ST \- PR\.

Tabelas: EFD\_PAR\_PROD\_C176 e EFD\_PAR\_PROD\_C176\_ASS

__MFS33878__: Inclusão dos campos “Sujeito ao FCP” e “Alíquota FCP”, para atender ao arquivo magnético da NPF 003/20\. 

__MFS43627__: Inclusão do campo “%Redução BC”\. Este campo é utilizado para calcular a base de cálculo reduzida na operação de venda, nos casos em que o ST é recolhido na origem \(na aquisição\)\. Nesses casos, a nota da venda não tem informação nos campos do valor da redução \(campo 57\) e nem nos campos da Base1/Base3\. Logo, não há como identificar que houve redução de base, então a verificação é feita pelo preenchimento desta alíquota na parametrização\.  

__MFS47333__: Inclusão da opção de associar produtos ao produto principal nesta tela de parametrização\.  Como na tela pode\-se escolher mais de um produto por vez para fazer a parametrização, a tela precisa ser reformulada para parametrizar um produto por vez e poder associar vários produtos ao produto principal\.  Deve ser criada uma nova tabela para se cadastrar os produtos associados ao produto principal\.  A tabela será “filha” da tabela de produtos parametrizados \(EFD\_PAR\_PROD\_C176\)\.  A nova tabela terá todos os campos que fazem parte da PK da tabela EFD\_PAR\_PROD\_C176, mais os campos de indicador e código do produto associado\.

# <a id="_Toc67326331"></a>Layout da Tela

Os dados que definem a chave de identificação da parametrização de produtos são os seguintes:

__     \- Empresa__

__     \- Estabelecimento__

__     \- Indicador e Código do Produto__

__     \- Alíquota Interna__

__     \- Data inicial da validade__

A alíquota faz parte da chave porque ela é usada no cálculo dos ajustes de crédito, e em caso de mudança, é preciso manter o histórico para o caso de processamento de dados antigos \(assim como na parametrização da CAT 17, onde a alíquota interna também é tratada na parametrização dos produtos\)\.

Sobre a ocorrência do mesmo produto em mais de uma parametrização:

  

Um código de produto já parametrizado, só poderá ser associado a outra parametrização quando a primeira já tiver sido “encerrada”, e a nova iniciar sua validade numa data superior ao final da vigência da primeira\.

Ou seja:

  \- A data de validade final da parametrização já existente deve estar preenchida;

  \- A data de validade inicial da nova parametrização deve ser maior que a data de encerramento \(validade final\) da

    parametrização já existente;

__MFS47333__: Inclusão dos Produtos Associados

Os dados que definem a chave de identificação da parametrização de produtos associados são os seguintes:

__     \- Empresa__

__     \- Estabelecimento__

__     \- Indicador e Código do Produto__

__     \- Alíquota Interna__

__     \- Data inicial da validade__

__     \- Indicador e Código do Produto Associado__

__Botões da barra de menu__:

GRUPO

Ao clicar nesta opção será aberta a janela de seleção dos grupos de relacionamento \(relacionamento Tabela x Grupos\), e o usuário poderá selecionar o grupo desejado\.

Caso o usuário tenha informado um estabelecimento no login, serão disponibilizados apenas os grupos relacionados ao estabelecimento em questão, caso contrário, serão exibidos os grupos de todos os estabelecimentos da empresa\.   

NOVO

Ao clicar nesta opção, as informações dos campos serão limpas e o usuário poderá incluir uma nova parametrização\.

ABRE

Ao clicar nesta opção, será aberta a janela para seleção das parametrizações já cadastradas para consulta ou manutenção\. 	

EXCLUI

Esta opção permite a exclusão da parametrização do estabelecimento em questão\. 

CONFIRMA

Opção para salvar as informações da parametrização incluída ou alterada\.

RELATÓRIO

Esta opção permite imprimir os dados da parametrização\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

  

Na abertura da tela, a janela da opção “GRUPO” será aberta automaticamente, obrigando o usuário a selecionar o grupo desejado\. Os critérios para exibição dos grupos são os mesmos descritos acima para a opção “Grupo”\. 

# <a id="_Toc67326332"></a>Regras de Funcionamento dos Campos

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Estabelecimento

Alfanumérico 

__S__

S

Neste campo será exibido o código e a razão social do estabelecimento do Grupo selecionado pelo usuário na abertura da tela, ou através da opção “GRUPO” da barra de menu\.* *

MFS13569

Grupo

Alfanumérico

__S__

S

Neste campo será exibido o Grupo selecionado pelo usuário na abertura da tela, ou através da opção “GRUPO” da barra de menu\.

MFS13569

Alíquota Interna dos Produtos 

Numérico

__S__

S

Valor com  4 decimais

Neste campo será informada a alíquota interna dos produtos que serão selecionados\.

MFS13569

Validade \(de / até\)

Data

__S__ / N

S

  \(dd/mm/aaaa\)

O usuário deverá informar um período de validade da parametrização\.

A data de validade inicial é obrigatória, já a data final pode ficar sem preenchimento\. 

Consistência Validade x Grupo:

A data de validade inicial *não* pode ser inferior à data de validade do Grupo informado \(campo “Grupo”\)\. Caso isso ocorra, será exibida a seguinte mensagem:

*“A validade inicial não pode ser inferior à validade do Grupo informado”*

Consistência Validade Inicial x Validade Final:

A data de validade inicial *não* pode ser superior à data de validade final\. Caso isso ocorra, será exibida a seguinte mensagem:

*“A validade inicial não pode ser superior à validade final\.”*

 

MFS13569

Informar código/descrição para pesquisa

Alfanumérico

N

S

Neste campo o usuário poderá informar os caracteres iniciais do código, ou da descrição a serem pesquisados, através do botão “Pesquisar”\.

MFS13569

Indicador/Código/

Descrição do Produto

Alfanumérico

S

S

Este campo trabalha com janela de seleção dos produtos <a id="OLE_LINK15"></a>da SAFX2013, considerando apenas os produtos do Grupo escolhido na abertura da tela\.

Quando o produto for digitado será validada a sua existência na tabela, e caso não exista, será exibida mensagem de erro padrão\.

<a id="OLE_LINK11"></a>Ao salvar a operação, serão feitas as seguintes críticas:

\- Verifica se o produto informado já consta como um produto associado na parametrização de outro produto qualquer\. Caso sim, a operação não será salva e será exibida a seguinte mensagem de erro: *“O produto principal já encontra\-se cadastrado como produto associado, não será permitida sua inclusão”*\.

\- Um determinado produto só pode ser parametrizado para outra data de validade inicial se a parametrização anterior for finalizada\. Assim, caso o produto já conste na parametrização, a validade final da parametrização já existente \(a mais atual\) deve estar preenchida\. Ou seja, a parametrização mais atual não poderá estar em aberto\. Caso contrário, a operação não será salva e será exibida a seguinte mensagem: *“Foi encontrada parametrizacao para o produto, com datas de vigencia em conflito com as datas de vigencia informadas”*

\- Estando a parametrização anterior já finalizada, será verificado se a validade inicial da nova parametrização é superior à data da validade final da parametrização já existente \(a mais atual\)\. Caso contrário, a operação não será salva e será exibida a seguinte mensagem:*“Foi encontrada parametrizacao para o produto, com datas de vigencia em conflito com as datas de vigencia informadas”*

MFS47333

Pesquisar

Botão

N

S

Ao clicar nesta opção, será feita a pesquisa dos produtos, de acordo com o código ou a descrição informada, e a lista dos produtos será refeita e demonstrada para a seleção do usuário\.

Esta pesquisa considera os produtos cujo código ou descrição, conforme o caso, tenha as mesmas iniciais do código ou da descrição informados\.

   

Observar também que na pesquisa dos produtos serão considerados apenas os produtos do Grupo informado pelo usuário \(campo “Grupo”\)\.  

MFS13569

Relação dos Produtos

Alfanumérico

__S__

S

Neste campo é exibida a lista dos produtos \(SAFX2013\) para seleção do usuário\. Na abertura da tela, são demonstrados todos os produtos da tabela que sejam do Grupo informado \(campo “Grupo”\)\.

Os produtos já parametrizados, aparecerão marcados\.

Posteriormente, esta lista será refeita sempre que o usuário clicar na opção “Pesquisar”\.

Para selecionar os produtos, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”\.

MFS13569

Sujeito ao FCP

Checkbox

N

S

Default = desmarcado

Através deste campo o usuário informa se o produto é sujeito ao Fundo de Combate à Pobreza\.

Este campo será habilitado apenas para os produtos selecionados\.

Quando marcado, o campo “Alíquota FCP” será habilitado\.

Quando desmarcado, o campo “Alíquota FCP” será desabilitado \(e seu conteúdo limpo, quando for o caso\)\.

 

MFS33878

Alíquota FCP

Numérico

N

S

Valor com  4 decimais

Neste campo será informada a alíquota do Fundo de Combate à Pobreza dos produtos que serão selecionados\.

Este campo será habilitado apenas quando o campo “S*ujeito ao FCP*” estiver marcado\. Caso contrário, permanece desabilitado\.

MFS33878

%Redução BC

Numérico

N

S

Valor com  4 decimais

Neste campo será informada a alíquota de redução da base de cálculo do produto, quando for o caso\.

MFS43627

Indicador/Código/

Descrição do Produto Associado

Alfanumérico

N

S

Neste campo o usuário poderá, opcionalmente, informar produtos que serão associados ao produto principal\. 

Da mesma forma que o campo “Produto”, este campo trabalha com janela de seleção dos produtos da SAFX2013, considerando apenas os produtos do Grupo escolhido na abertura da tela\.

Quando o produto for digitado será validada a sua existência na tabela, e caso não exista, será exibida mensagem de erro padrão\.

 

Ao salvar a operação, serão feitas as seguintes críticas:

\- Se um produto associado já tiver sido parametrizado como produto principal,<a id="OLE_LINK12"></a><a id="OLE_LINK13"></a><a id="OLE_LINK14"></a> a operação não será salva e será exibida a seguinte mensagem de erro: *“O produto associado já encontra\-se cadastrado como produto principal, não será permitida sua inclusão”*

<a id="OLE_LINK16"></a>\- Se um produto associado tiver sido informado mais de uma vez, a operação não será salva e será exibida a seguinte mensagem de erro: *“Produto X – XXXXXXXXXXXX já associado”\.*

\- Se um produto associado já constar como associado a outro produto principal, em períodos de vigência paralelos, a operação não será salva e será exibida a seguinte mensagem de erro: *“Foi encontrada parametrizacao para produto associado relacionado a outro produto principal, com datas de vigencia em conflito com as datas de vigencia informadas”\.*

MFS47333

Replicar para os Estabelecimentos

Alfanumérico

N

S

Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados\.

Serão exibidos para seleção *apenas* os estabelecimentos da mesma empresa do estabelecimento parametrizado, e do mesmo Grupo informado e que pertençam ao Paraná\.

Para selecionar os estabelecimentos, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”\.

MFS13569

# <a id="_Toc67326333"></a>Regras de Validação

## <a id="_Toc67326334"></a>RN01 – Validação na gravação de um novo registro:

__MFS47333__

A chave física da tabela é:

     \- Empresa

     \- Estabelecimento

     \- Indicador e Código do Produto

     \- Alíquota Interna

     \- Data inicial da validade

     \- Indicador e Código do Produto Associado

Mas conceitualmente a Alíquota Interna não deveria fazer parte da chave\.

Logo, ao incluir um registro novo, verificar se já existe na base registro de mesma empresa, estabelecimento, produto e Data Inicial Validade\.

Caso exista, exibir mensagem e não salvar o registro:

*Já existe registro na base de mesmo Produto e Data Inicial de Validade informados*

       = = = = = =

