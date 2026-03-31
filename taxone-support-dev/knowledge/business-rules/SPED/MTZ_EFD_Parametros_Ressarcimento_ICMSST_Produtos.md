# MTZ_EFD_Parametros_Ressarcimento_ICMSST_Produtos

> Fonte: MTZ_EFD_Parametros_Ressarcimento_ICMSST_Produtos.docx






THOMSON REUTERS

Módulo Sped Fiscal

Parametrização Produtos


Localização: Menu Sped, Módulo: Escrituração Fiscal Digital  Parâmetros  Ressarcimento ICMS-ST  Produtos




DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	2




## Regras Gerais


Os dados parametrizados neste item (Escrituração Fiscal Digital  Parâmetros  Ressarcimento ICMS-ST  Produtos) são utilizados na rotina de pré-geração para os registros de Ressarcimento de ICMS-ST, realizada no menu “Pré-Geração  Ressarcimento ICMS-ST (Específico MG)” do módulo Sped Fiscal. Esta parametrização será utilizada na geração dos registros C180, C185.

Tabela: EFD_PAR_PROD_C176

[MFS-37051] Esta parametrização já existe no produto (Localização: Menu Estadual, Módulo: Ressarcimento de ICMS ST - PR, item Parâmetros  Produtos).
A tela e suas regras devem ser replicadas para o módulo EFD – Escrituração Fiscal Digital (Parâmetros  Ressarcimento ICMS-ST  Produtos)


[MFS47958] Inclusão do campo “%Redução BC”.


## Layout da Tela




Os dados que definem a chave de identificação da parametrização são os seguintes:

- Empresa
- Estabelecimento
- Grupo
- Alíquota Interna
- Data inicial da validade

A alíquota faz parte da chave porque ela é usada no cálculo dos ajustes de crédito, e em caso de mudança, é preciso manter o histórico para o caso de processamento de dados antigos (assim como na parametrização da CAT 17, onde a alíquota interna também é tratada na parametrização dos produtos).

Sobre a ocorrência do mesmo produto em mais de uma parametrização:

Um código de produto já parametrizado, só poderá ser associado a outra parametrização quando a primeira já tiver sido “encerrada”, e a nova iniciar sua validade numa data superior ao final da vigência da primeira.
Ou seja:
- A data de validade final da parametrização já existente deve estar preenchida;
- A data de validade inicial da nova parametrização deve ser maior que a data de encerramento (validade final) da
parametrização já existente;

Botões da barra de menu:



Na abertura da tela, a janela da opção “GRUPO” será aberta automaticamente, obrigando o usuário a selecionar o grupo desejado. Os critérios para exibição dos grupos são os mesmos descritos acima para a opção “Grupo”.


## Regras de Funcionamento dos Campos





Críticas a serem realizadas antes de salvar a operação:





= = = = = =


.

| MFS | Descrição | Nome | Data |
| --- | --- | --- | --- |
| MFS-33977 | Criação da parametrização de produtos para geração dos dados dos registros C180. | Alessandra Cristina Navatta | 13/03/2020 |
| MFS-37051 | Considerar o layout de Tela utilizado no Ressarcimento do PR. Este ajuste se faz necessário para contemplar na parametrização a alíquota de FCP. | Alessandra Cristina Navatta | 28/05/2020 |
| MFS47958 | Inclusão do campo “%Redução BC” | Liliane Assaf | 08/12/2020 |


| GRUPO | Ao clicar nesta opção será aberta a janela de seleção dos grupos de relacionamento (relacionamento Tabela x Grupos), e o usuário poderá selecionar o grupo desejado. Caso o usuário tenha informado um estabelecimento no login, serão disponibilizados apenas os grupos relacionados ao estabelecimento em questão, caso contrário, serão exibidos os grupos de todos os estabelecimentos da empresa. |
| --- | --- |
| NOVO | Ao clicar nesta opção, as informações dos campos serão limpas e o usuário poderá incluir uma nova parametrização. |
| ABRE | Ao clicar nesta opção, será aberta a janela para seleção das parametrizações já cadastradas para consulta ou manutenção. |
| EXCLUI | Esta opção permite a exclusão da parametrização do estabelecimento em questão. |
| CONFIRMA | Opção para salvar as informações da parametrização incluída ou alterada. |
| RELATÓRIO | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | S |  | Neste campo será exibido o código e a razão social do estabelecimento do Grupo selecionado pelo usuário na abertura da tela, ou através da opção “GRUPO” da barra de menu. | MFS37051 |
| Grupo | Alfanumérico | S | S |  | Neste campo será exibido o Grupo selecionado pelo usuário na abertura da tela, ou através da opção “GRUPO” da barra de menu. | MFS37051 |
| Alíquota Interna dos Produtos | Numérico | S | S | Valor com  4 decimais | Neste campo será informada a alíquota interna dos produtos que serão selecionados. | MFS37051 |
| Validade (de / até) | Data | S / N | S | (dd/mm/aaaa) | O usuário deverá informar um período de validade da parametrização.  A data de validade inicial é obrigatória, já a data final pode ficar sem preenchimento.   Consistência Validade x Grupo: A data de validade inicial não pode ser inferior à data de validade do Grupo informado (campo “Grupo”). Caso isso ocorra, será exibida a seguinte mensagem:  “A validade inicial não pode ser inferior à validade do Grupo informado” | MFS37051 |
| Informar código/descrição para pesquisa | Alfanumérico | N | S |  | Neste campo o usuário poderá informar os caracteres iniciais do código, ou da descrição a serem pesquisados, através do botão “Pesquisar”. | MFS37051 |
| - Código  - Descrição | Radio Button | N | S | Opção default:     “Código” | Estas duas opções indicam a forma como será feita a pesquisa dos produtos a serem disponibilizados para seleção do usuário no campo “Relação dos Produtos”. As opções são alternativas, pois o filtro dos produtos é feito pelo código, ou pela descrição do produto. |  |
| Pesquisar | Botão | N | S |  | Ao clicar nesta opção, será feita a pesquisa dos produtos, de acordo com o código ou a descrição informada, e a lista dos produtos será refeita e demonstrada para a seleção do usuário.  Esta pesquisa considera os produtos cujo código ou descrição, conforme o caso, tenha as mesmas iniciais do código ou da descrição informados.     Observar também que na pesquisa dos produtos serão considerados apenas os produtos do Grupo informado pelo usuário (campo “Grupo”). | MFS37051 |
| Relação dos Produtos | Alfanumérico | S | S |  | Neste campo é exibida a lista dos produtos (SAFX2013) para seleção do usuário. Na abertura da tela, são demonstrados todos os produtos da tabela que sejam do Grupo informado (campo “Grupo”).  Os produtos já parametrizados, aparecerão marcados.  Posteriormente, esta lista será refeita sempre que o usuário clicar na opção “Pesquisar”.  Para selecionar os produtos, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. | MFS37051 |
| Sujeito ao FCP | Checkbox | N | S | Default = desmarcado | Através deste campo o usuário informa se o produto é sujeito ao Fundo de Combate à Pobreza.  Este campo será habilitado apenas para os produtos selecionados.  Quando marcado, o campo “Alíquota FCP” será habilitado.  Quando desmarcado, o campo “Alíquota FCP” será desabilitado (e seu conteúdo limpo, quando for o caso). | MFS37051 |
| Alíquota FCP | Numérico | N | S | Valor com  4 decimais | Neste campo será informada a alíquota do Fundo de Combate à Pobreza dos produtos que serão selecionados.  Este campo será habilitado apenas quando o campo “Sujeito ao FCP” estiver marcado. Caso contrário, permanece desabilitado. | MFS37051 |
| %Redução BC | Numérico | N | S | Valor com  4 decimais | Neste campo será informada a alíquota de redução da base de cálculo do produto, quando for o caso. | MFS47958 |
| Replicar para os Estabelecimentos | Alfanumérico | N | S |  | Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados. Serão exibidos para seleção apenas os estabelecimentos da mesma empresa do estabelecimento parametrizado, e do mesmo Grupo informado e que pertençam ao Paraná.  Para selecionar os estabelecimentos, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. | MFS37051 |


| RN01 | Ao incluir uma nova parametrização:  Caso já exista parametrização informada para o mesmo Estabelecimento, Grupo e Alíquota, a nova parametrização só poderá ser salva se as seguintes condições forem verdadeiras:  - A parametrização já existente tiver uma data de validade final preenchida; - A nova parametrização tiver uma data de validade inicial superior à data final da parametrização já existente;  Se uma destas condições não for atendida, será exibida mensagem de erro, conforme a regra abaixo, e a operação não será salva.   Se a primeira condição não for atendida:       “Operação não permitida: já existe parametrização em aberto para o mesmo Grupo e Alíquota” Senão (significa que foi a segunda condição que não foi atendida)      “Operação não permitida: a validade inicial informada se enquadra na vigência de outra parametrização já encerrada do        mesmo Grupo e Alíquota”; |
| --- | --- |
| RN02 | Sobre a ocorrência do mesmo produto em mais de uma parametrização:  Um produto não poderá constar de outra parametrização do mesmo estabelecimento, exceto quando a seguinte condição for verdadeira:  - A data de validade final da parametrização já existente deve estar preenchida (ou seja, já foi “encerrada”);  Quando a condição não for atendida, será exibida a mensagem abaixo e a operação não será salva.                 “Existem produtos já informados em parametrização ainda vigente para o Estabelecimento” |
