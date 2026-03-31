# MTZ_EFD_Parametros_Registro_E115_Geral_NAT

> Fonte: MTZ_EFD_Parametros_Registro_E115_Geral_NAT.docx






THOMSON REUTERS

Módulo Sped Fiscal

Parâmetros p/ Pré-Geração do Registro E115 por CFOP/Natureza Operação (Geral)


Localização: Menu Sped, Módulo: Escrituração Fiscal Digital, item Parâmetros  Registro E115/1925   Registro E115 (Geral)  CFOP/Natureza Operação




DOCUMENTO DE REQUISITO


Sumário

1.	Introdução	2
2.	Layout da Tela	2
3.	Funcionamento da Tela	3
4.	Botões da barra de menu:	5
5.	Regras de Funcionamento dos Campos	5
6.	Validações	8

## Introdução


Esta tela tem objetivo de promover a manutenção da parametrização dos CFOP’s/Naturezas de Operação a serem utilizados na rotina de pré-geração do registro E115, realizada no menu “Pré-Geração  Registro E115 (Geral)” do módulo Sped Fiscal.

Esta parametrização relaciona por estabelecimento, os CFOP’s/Naturezas de Operação aos Códigos de Informação Adicional, criados no item “”, determinando o valor a ser recuperado do item de mercadoria na pré-geração.

A tela é praticamente a mesma disponibilizada no menu” Parâmetros  Registro E115/1925   Registro E115 (Específico RS)  CFOP/Natureza de Operação”, inclusive tecnicamente grava a mesma tabela (EFD_PAR_EXTCFO_E115).




## Layout da Tela



Estabelecimento [XXXXXX – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]
Grupo Natureza: [XX]
Código:        [...] [XXXX] [xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]


-- CFOP’s/Natureza Operação-----------------------------------------------------------------------------------------------------------------
CFOP-Código-Descrição                            |    Recuperação de Valores       |
-----------------------------------------------------------------------------------------------------------------------------------------------------
[ x ] xxxx - xxxxxx-xxxxxxxxxxxxxxx               | [\/] [Valor Base Isenta   ]
[ x ] xxxx - xxxxxx-xxxxxxxxxxxxxxx               | [\/] [Valor Base Outras  ]
[   ] xxxx - xxxxxx-xxxxxxxxxxxxxxx                | [\/] [                                ]
[Selecionar Todos] [Desmarcar Todos]

Os dados que definem a chave de identificação da parametrização são os seguintes:

Empresa
Estabelecimento
Código
CFOP
Natureza da Operação

A tabela onde a parametrização é gravada é EFD_PAR_EXTCFO_E115.

Observação:
O campo “Gia – Anexo” fisicamente faz parte da chave da tabela, mas é apenas utilizado na parametrização do RS, opção de menu” Parâmetros  Registro E115/1925   Registro E115 (Específico RS)  CFOP/Natureza da Operação”).

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
| MFS24915 | Pré-Geração do E115 (Geral) | Criação da parametrização de CFOP/Natureza da Operação para a pré-geração do registro E115. | 28/02/2019 |
| MFS26565 | Andréa Rocha | Inclusão de novos valores no campo Recuperação de Valores. | 03/05/2019 |
| MFS30407 | Andréa Rocha | Retirar a validação do campo estabelecimento para o estado igual a RS. | 26/09/2019 |


| Passo | Acionador | Descrição |
| --- | --- | --- |
| 1 | Usuário | Usuário seleciona o item de menu Parâmetros  Registro E115/1925   Registro E115 (Geral)  CFOP / Natureza Operação |
| 2 | Sistema | Verifica o usuário informou estabelecimento no login do Manager. Se no login foi informado estabelecimento, então: Sistema verifica a UF do Estabelecimento. Se a UF do Estabelecimento de login for igual a RS, então: Sistema apresenta mensagem:  “A parametrização de CFOP/Natureza Operação para Informações Adicionas E115 não é válida para estabelecimentos do Rio Grande do Sul” Fecha a janela. Finaliza o fluxo. Senão Segue o fluxo. Senão Segue o fluxo. |
| 3 | Sistema | Sistema abre a tela de seleção dos grupos cadastrados no Relacionamento entre Tabela e Grupos (Relac_Tab_Grupo).  Se no login foi informado estabelecimento, então: Sistema disponibilizados apenas os grupos relacionados ao estabelecimento em questão, relacionados a Tabela Natureza de Operação. Senão Sistema exibe os grupos dos estabelecimentos da empresa cuja UF seja diferente de “RS”, relacionados a Tabela Natureza de Operação. |
| 4 | Usuário | Usuário seleciona um registro de grupo/estabelecimento do Relacionamento entre Tabela e Grupo. |
| 5 | Sistema | Abre a tela de Parametrização de CFOP/Natureza Operação, com os campos Estabelecimento e Grupo Natureza preenchidos e bloqueados. Sistema monta a Relação de CFOP’s/Natureza de Operação e a lista do campo “Recuperação de Valores”.  Vide regras descritas no tópico “5 – Regras de Funcionamento dos Campos”. |
| 6 | Usuário | Usuário seleciona ou digita um Código de Informação Adicional no campo “Código”. |
| 7 | Sistema | Valida o Código digitado. Vide regra do campo “Código” descrita no tópico “5 – Regras de Funcionamento dos Campos”. |
| 8 | Usuário | Seleciona um CFOP/Natureza de Operação e preenche o campo Recuperação de Valores. |
| 9 | Usuário | Seleciona botão confirma. |
| 10 | Sistema | Executa validações descritas no tópico 5- Validações.  Caso os dados estejam consistentes, grava as parametrizações na tabela definitiva. |
| 11 | Usuário | Seleciona outras ações disponíveis na barra de menu da janela. Vide tópico “4 - Botões da barra de menu” |


| SELECIONAR GRUPO | Ao clicar nesta opção será aberta a janela de seleção dos grupos cadastrados no Relacionamento entre Tabela e Grupos (Relac_Tab_Grupo), e o usuário poderá selecionar o grupo desejado. Se no login foi informado estabelecimento, então: Sistema disponibilizados apenas os grupos relacionados ao estabelecimento em questão, relacionados a Tabela Natureza de Operação. Senão Sistema exibe os grupos dos estabelecimentos da empresa cuja UF seja diferente de “RS”, relacionados a Tabela Natureza de Operação. Seguir o passo 4 do fluxo descrito no tópico 3 – Funcionamento da Tela. |
| --- | --- |
| CONFIRMA | Opção para salvar as informações da parametrização incluída, excluída ou alterada. |
| RELATÓRIO | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | N |  | Neste campo será exibido o código e a razão social do estabelecimento do Grupo selecionado pelo usuário na abertura da tela, ou através da opção “SELECIONAR GRUPO” da barra de menu. |  |
| Grupo Natureza | Alfanumérico | S | N |  | Neste campo será exibido o Grupo selecionado pelo usuário na abertura da tela, ou através da opção “SELECIONAR GRUPO” da barra de menu. |  |
| Código | Alfanumérico | S | S | Formato: Pesquisar Pasta – Seleção da Manutenção Informações Adicionais da Apuração (Registro E115/ 1925) | Permitir seleção da tabela dos Códigos de Informação Adicional parametrizados na Manutenção Informações Adicionais da Apuração (Registro E115/ 1925), item de menu .  Pastinha: Só recuperar os códigos cuja UF seja igual a UF do Estabelecimento;  Consistência: Verificar se o código digitado existe na tabela de Informações Adicionais da Apuração (Registro E115/ 1925), considerando a UF do Estabelecimento. Caso não exista, exibir a seguinte mensagem: Código da Informação Adicional não cadastrado para a UF do Estabelecimento.  Tratamento: Ao selecionar um novo Código, os CFOP’s/Natureza da Operação e  o campo Recuperação Valores devem ser atualizados. Tabela Origem: EFD_INF_ADIC_APUR |  |
| Relação dos CFOP’s/Natureza de Operação | Alfanumérico | S | S |  | Neste campo é exibida a lista dos CFOP’s (SAFX2012) que tenham Natureza de Operação (SAFX2006) vinculada na SAFX2081.  Seleção dos CFOPs com Natureza de Operação (SAFX2012 / SAFX2006): Selecionar todos os registros de CFOP que tenham Natureza da Operação relacionada na SAFX2081.  Recuperar univocamente a relação do Código CFOP com o Código de Natureza de Operação.  Caso exista mais de um registro relacionando o mesmo código CFOP com o mesmo Código de Natureza, recuperar apenas o de máxima validade.  Do conjunto de CFOPs/Naturezas de Operação recuperados, o sistema deve ainda aplicar o seguinte tratamento:  - APRESENTAR MARCADO o CFOP/Natureza da Operação já parametrizado para o estabelecimento e Código de Informação Adicional informados. - APRESENTAR DESMARCADO o CFOP/Natureza da Operação que não está parametrizado para o estabelecimento e Código informados.  Para selecionar os CFOPs/Natureza da Operação, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. |  |
| Recuperação de Valores | Alfanumérico | S | S | Formato: Combo Box | Exibir uma lista composta pela descrição dos seguintes itens: 1 - Base Isenta ICMS 2 - Base Outras ICMS 3 - Base Reduzida ICMS 4 -  5  6 - Valor Desonerado ICMS 7 - Valor Diferido ICMS | MFS26565 |
| Replicar para os Estabelecimentos | Alfanumérico | N | S |  | Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados. Serão exibidos para seleção apenas os estabelecimentos da mesma empresa do estabelecimento parametrizado, do mesmo Grupo informado, e da mesma UF do Estabelecimento informado.  Para selecionar os estabelecimentos, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. |  |
