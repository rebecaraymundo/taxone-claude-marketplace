# MTZ_EFD_Parametros_Registro_E115_Geral_CST

> Fonte: MTZ_EFD_Parametros_Registro_E115_Geral_CST.docx






THOMSON REUTERS

Módulo Sped Fiscal

Parâmetros p/ Pré-Geração do Registro E115 por CST (Geral)


Localização: Menu Sped, Módulo: Escrituração Fiscal Digital, item Parâmetros  Registro E115/1925   Registro E115 (Geral)  CST




DOCUMENTO DE REQUISITO


Sumário

1.	Introdução	3
2.	Layout da Tela	3
3.	Funcionamento da Tela	4
4.	Botões da barra de menu:	5
5.	Regras de Funcionamento dos Campos	5
6.	Validações	7

## Introdução


Esta tela tem objetivo de promover a manutenção da parametrização dos CST’s a serem utilizados na rotina de pré-geração do registro E115, realizada no menu “Pré-Geração  Registro E115 (Geral)” do módulo Sped Fiscal.

Esta parametrização relaciona por estabelecimento, os CST’s aos Códigos de Informação Adicional, criados no item “”, determinando o valor a ser recuperado do item de mercadoria na pré-geração.


## Layout da Tela



Estabelecimento [XXXXXX – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]
Grupo:          [XXXXXXXXX]
Código:        [...] [XXXX] [xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]

-- CST --------------------------------------------------------------------------------------------------------------------------
Código-Descrição
----------------------------------------------------------------------------------------------------------------------------------------
[ x ] x -xxxxxxxxxxxxxxxxxx
[ x ] x -xxxxxxxxxxxxxxxxxx
[Selecionar Todos] [Desmarcar Todos]

Os dados que definem a chave de identificação da parametrização são os seguintes:
Empresa
Estabelecimento
Código
Grupo CST
CST




## Funcionamento da Tela








## Botões da barra de menu:






## Regras de Funcionamento dos Campos






## Validações



Críticas a serem realizadas antes de salvar a operação:

RN01: Campos Obrigatórios
Validações de Campos Obrigatórios não preenchidos.
Quando o campo é obrigatório e não estiver preenchido, exibir mensagem padrão.
A obrigatoriedade dos campos está definida no tópico “5 – Regras de Funcionamento dos Campos”.




= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS28993 | Andréa Rocha | Criação da parametrização de CST para a pré-geração do registro E115. | 10/09/2019 |
| MFS30407 | Andréa Rocha | Retirar a validação do campo estabelecimento para o estado igual a RS. | 26/09/2019 |


| Passo | Acionador | Descrição |
| --- | --- | --- |
| 1 | Usuário | Usuário seleciona o item de menu Parâmetros  Registro E115/1925   Registro E115 (Geral)  CST |
| 2 | Sistema | Verifica o usuário informou estabelecimento no login do Manager. Se no login foi informado estabelecimento, então: Sistema verifica a UF do Estabelecimento. Se a UF do Estabelecimento de login for igual a RS, então: Sistema apresenta mensagem:  “A parametrização de CST para Informações Adicionas E115 não é válida para estabelecimentos do Rio Grande do Sul” Fecha a janela. Finaliza o fluxo. Senão Segue o fluxo. Senão Segue o fluxo. |
| 3 | Sistema | Sistema abre a tela de seleção dos grupos cadastrados no Relacionamento entre Tabela e Grupos (Relac_Tab_Grupo).  Se no login foi informado estabelecimento, então: Sistema disponibilizados apenas os grupos relacionados ao estabelecimento em questão, relacionados a Tabela Situação Tributária Estadual – B. Senão Sistema exibe os grupos dos estabelecimentos da empresa cuja UF seja diferente de “RS”, relacionados a Tabela Situação Tributária Estadual – B. |
| 4 | Usuário | Usuário seleciona um registro de grupo/estabelecimento do Relacionamento entre Tabela e Grupo. |
| 5 | Sistema | Abre a tela de Parametrização de CST. Se no login foi informado estabelecimento, então: Sistema apresenta o campo Estabelecimento bloqueado e preenchido com o estabelecimento de login. Senão Sistema apresenta o campo Estabelecimento desbloqueado e com a lista de estabelecimentos de UF <> RS.  Sistema monta a Relação de CST’s.  Vide regras descritas no tópico “5 – Regras de Funcionamento dos Campos”. |
| 6 | Usuário | Usuário seleciona ou digita um Código de Informação Adicional no campo “Código”. |
| 7 | Sistema | Valida o Código digitado. Vide regra do campo “Código” descrita no tópico “5 – Regras de Funcionamento dos Campos”. |
| 8 | Usuário | Seleciona um CST. |
| 9 | Usuário | Seleciona botão confirma. |
| 10 | Sistema | Executa validações descritas no tópico 5- Validações.  Caso os dados estejam consistentes, grava as parametrizações na tabela definitiva. |
| 11 | Usuário | Seleciona outras ações disponíveis na barra de menu da janela. Vide tópico “4 - Botões da barra de menu” |


| SELECIONAR GRUPO | Ao clicar nesta opção será aberta a janela de seleção dos grupos cadastrados no Relacionamento entre Tabela e Grupos (Relac_Tab_Grupo), e o usuário poderá selecionar o grupo desejado. Se no login foi informado estabelecimento, então: Sistema disponibilizados apenas os grupos relacionados ao estabelecimento em questão, relacionados a Tabela Situação Tributária B. Senão Sistema exibe os grupos dos estabelecimentos da empresa cuja UF seja diferente de “RS”, relacionados a Tabela Situação Tributária B. Seguir o passo 4 do fluxo descrito no tópico 3 – Funcionamento da Tela. |
| --- | --- |
| CONFIRMA | Opção para salvar as informações da parametrização incluída, excluída ou alterada. |
| RELATÓRIO | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | S | Formato: Combo Box | Lista exibindo o código e a razão social dos estabelecimentos. Campo ficará habilitado ou bloqueado dependendo do estabelecimento de login. Se no login foi informado estabelecimento, então: Sistema apresenta o campo Estabelecimento bloqueado e preenchido com o estabelecimento de login. Senão Sistema apresenta o campo Estabelecimento desbloqueado e com a lista de estabelecimentos de UF <> RS.  Tratamento: Ao selecionar um novo estabelecimento, o campo Código deve ser limpo e consequentemente os CST’s devem ser desmarcados. | MFS28993 |
| Grupo | Alfanumérico | S | N |  | Neste campo será exibido o Grupo selecionado pelo usuário na abertura da tela, ou através da opção “SELECIONAR GRUPO” da barra de menu. | MFS28993 |
| Código | Alfanumérico | S | S | Formato: Pesquisar Pasta – Seleção da Manutenção Informações Adicionais da Apuração (Registro E115/ 1925) | Permitir seleção da tabela dos Códigos de Informação Adicional parametrizados na Manutenção Informações Adicionais da Apuração (Registro E115/ 1925), item de menu .  Pastinha: Só recuperar os códigos cuja UF seja igual a UF do Estabelecimento;  Consistência: Verificar se o código digitado existe na tabela de Informações Adicionais da Apuração (Registro E115/ 1925), considerando a UF do Estabelecimento. Caso não exista, exibir a seguinte mensagem: Código da Informação Adicional não cadastrado para a UF do Estabelecimento. Tratamento: Ao selecionar um novo Código, os CST’s devem ser atualizados. Tabela Origem: EFD_INF_ADIC_APUR | MFS28993 |
| Relação dos CST’s | Alfanumérico | S | S |  | Neste campo é exibida a lista dos CST’s cadastrados na TACES04 - Situação Tributária Estadual – B (Y2026_SIT_TRB_UF_B) para seleção do usuário.  Seleção dos CSTs no Cadastro (Y2026_SIT_TRB_UF_B): Selecionar todos os registros de CST da tabela.  Caso exista mais de um registro de mesmo código CST, recuperar apenas o de máxima validade.  Do conjunto de CSTs recuperados, o sistema deve ainda aplicar o seguinte tratamento:  - Apresentar marcado o CST já parametrizado para o estabelecimento e Código de Informação Adicional informados. - Apresentar desmarcado o CST que não está parametrizado para o estabelecimento e Código informados.  Para selecionar os CSTs, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. | MFS28993 |
| Replicar para os Estabelecimentos | Alfanumérico | N | S |  | Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados. Serão exibidos para seleção apenas os estabelecimentos da mesma empresa do estabelecimento parametrizado e da mesma UF do Estabelecimento informado.  Para selecionar os estabelecimentos, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. | MFS28993 |
