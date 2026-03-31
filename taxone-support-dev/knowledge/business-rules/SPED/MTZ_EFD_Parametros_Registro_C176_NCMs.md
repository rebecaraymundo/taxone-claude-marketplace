# MTZ_EFD_Parametros_Registro_C176_NCMs

> Fonte: MTZ_EFD_Parametros_Registro_C176_NCMs.docx






THOMSON REUTERS

Módulo Sped Fiscal

Parametrização de NCM’s p/a Geração do C176


Localização: Menu Sped, Módulo: Escrituração Fiscal Digital, item Parâmetros à Registro C176 à NCM’s




DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	2
3.	Regras de Funcionamento dos Campos	3


























## Regras Gerais


Os dados parametrizados neste item são utilizados na rotina de pré-geração do registro C176, realizada no menu “Pré-Geração à Registro C176” do módulo Sped Fiscal.


## Layout da Tela



Os dados que definem a chave de identificação da parametrização são os seguintes:

- Empresa
- Estabelecimento
- Alíquota Interna
- Data inicial da validade

A alíquota faz parte da chave porque ela é usada no cálculo dos ajustes de crédito, e em caso de mudança, é preciso manter o histórico para o caso de processamento de dados antigos (assim como na parametrização da CAT 17, onde a alíquota interna também é tratada na parametrização dos produtos).

Sobre a ocorrência do mesmo NCM em mais de uma parametrização:

Um NCM já parametrizado, só poderá ser associado a outra parametrização quando a primeira já tiver sido “encerrada”, e a nova iniciar sua validade numa data superior ao final da vigência da primeira.
Ou seja:
- A data de validade final da parametrização já existente deve estar preenchida;
- A data de validade inicial da nova parametrização deve ser maior que a data de encerramento (validade final) da
parametrização já existente;

Botões da barra de menu:





## Regras de Funcionamento dos Campos





Críticas a serem realizadas antes de salvar a operação:





= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS2772 | Atendimento a Portaria CAT 158 | Criação da parametrização de NCM’s para geração dos dados do registro C176. | 25/05/2016 |
|  |  |  |  |
|  |  |  |  |


| NOVO | Ao clicar nesta opção, as informações dos campos serão limpas e o usuário poderá incluir uma nova parametrização. |
| --- | --- |
| ABRE | Ao clicar nesta opção, será aberta a janela para seleção das parametrizações já cadastradas para consulta ou manutenção. |
| EXCLUI | Esta opção permite a exclusão da parametrização do estabelecimento em questão. |
| CONFIRMA | Opção para salvar as informações da parametrização incluída ou alterada. |
| RELATÓRIO | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | S |  | Este campo é uma lista dos estabelecimentos da empresa do login para seleção do usuário. Quando for informado um estabelecimento no login, o campo mostrará fixo este estabelecimento, e usuário não poderá alterá-lo. |  |
| Alíquota Interna dos Produtos | Numérico | S | S | Valor com  4 decimais | Neste campo será informada a alíquota interna dos produtos cujos NCM’s serão selecionados. |  |
| Validade (de / até) | Data | S / N | S | (dd/mm/aaaa) | O usuário deverá informar um período de validade da parametrização.  A data de validade inicial é obrigatória, já a data final pode ficar sem preenchimento. |  |
| Informar código/descrição para pesquisa | Alfanumérico | N | S |  | Neste campo o usuário poderá informar os caracteres iniciais do código, ou da descrição a serem pesquisados, através do botão “Pesquisar”. |  |
| - Código  - Descrição | Radio Button | N | S | Opção default:     “Código” | Estas duas opções indicam a forma como será feita a pesquisa dos NCM’s a serem disponibilizados para seleção do usuário no campo “Relação de NCM’s”. As opções são alternativas, pois o filtro dos NCM’s é feito pelo código, ou pela descrição do NCM. |  |
| Pesquisar | Botão | N | S |  | Ao clicar nesta opção, será feita a pesquisa dos NCM’s, de acordo com o código ou a descrição informada, e a lista dos NCM’s será refeita e demonstrada para a seleção do usuário.  Esta pesquisa considera os NCM’s cujo código ou descrição, conforme o caso, tenha as mesmas iniciais do código ou da descrição informados. |  |
| Relação de NCM’s | Alfanumérico | S | S |  | Neste campo é exibida a lista dos NCM’s (SAFX2043) para seleção do usuário. Na abertura da tela, são demonstrados todos os NCM’s da tabela.  Posteriormente, esta lista será refeita sempre que o usuário clicar na opção “Pesquisar”.  Para selecionar os NCM’s, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. |  |
| Replicar para os Estabelecimentos | Alfanumérico | N | S |  | Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados. Serão exibidos para seleção apenas os estabelecimentos da mesma empresa do estabelecimento parametrizado.  Para selecionar os estabelecimentos, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. |  |


| RN01 | Ao incluir uma nova parametrização:  Caso já exista parametrização informada para o mesmo Estabelecimento e Alíquota, a nova parametrização só poderá ser salva se as seguintes condições forem verdadeiras:  - A parametrização já existente tiver uma data de validade final preenchida; - A nova parametrização tiver uma data de validade inicial superior à data final da parametrização já existente;  Se uma destas condições não for atendida, será exibida mensagem de erro, conforme a regra abaixo, e a operação não será salva.   Se a primeira condição não for atendida:       “Operação não permitida: já existe parametrização em aberto para a mesma Alíquota” Senão (significa que foi a segunda condição que não foi atendida)      “Operação não permitida: a validade inicial informada se enquadra na vigência de outra parametrização já encerrada da        mesma Alíquota”; |
| --- | --- |
| RN02 | Sobre a ocorrência do mesmo NCM em mais de uma parametrização:  Um NCM não poderá constar de outra parametrização do mesmo estabelecimento, exceto quando a seguinte condição for verdadeira:  - A data de validade final da parametrização já existente deve estar preenchida (ou seja, já foi “encerrada”);  Quando a condição não for atendida, será exibida a mensagem abaixo e a operação não será salva.                 “Existem NCM’s já informados em parametrização ainda vigente para o Estabelecimento” |
