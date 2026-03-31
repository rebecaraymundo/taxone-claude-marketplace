# MTZ_EFD_Parametros_Registro_1400_EspecificoUF_Deducoes_CST_Operacao_Produto

> Fonte: MTZ_EFD_Parametros_Registro_1400_EspecificoUF_Deducoes_CST_Operacao_Produto.docx






THOMSON REUTERS

Parâmetros p/ Geração do Registro 1400 Específico por UF
Deduções – Por CST x Operação x Produto
EFD-Escrituração Fiscal Digital


Este menu foi retirado do módulo EFD, conforme reunião interna ocorrida em 02/06/2020 (veu documento de GCM da MFS35568)


DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3
2.	Sugestão de Layout	8

## Regras dos Campos


Localização da tela: SPED\ EFD-Escrituração Fiscal Digital\ Parâmetros\ Registro 1400\ Específico por UF\ Deduções \ Por CST x Operação x Produto

Título da tela: Deduções – Por CST x Operação x Produto

Considerações:

O objetivo dessa parametrização é reconhecer quais produtos que possuem desconto e precisam ser deduzidos dos valores totalizados para o Registro 1400 específico por UF, isso para quaisquer operações que possuam parametrização, identificando-as por CST;
Será permitido a parametrização de vários CST para apenas uma parametrização por Operação e Produto.

Regra Geral Botões:

SELECIONAR GRUPO – Permite selecionar o estabelecimento/grupo/validade relacionado ao CST e produto a ser parametrizado.

NOVO – Permite incluir novo registro.

ABRE – Permite abrir uma janela para seleção dos registros, na tela deverão ser apresentados os campos chave para filtro das informações.

EXCLUI – Permite excluir registro.

CONFIRMA – Permite salvar registro.

RELATÓRIO – Permite emitir relatório listando todos os registros existentes na base de dados ou de acordo com a Empresa e Estabelecimento selecionados na tela de login (mostrar todos os campos como critério de busca).

FECHA – Permite sair da tela.

Funcionamento da Tela:


Funcionamento da Campos:



Incluir uma observação no final da tela referente ao campo Operação:
“A exibição do conteúdo para o campo Operação dependerá da UF do Estabelecimento selecionado. Apenas os Estabelecimentos cuja UF determina uma forma específica de geração apresentarão conteúdo para o campo. Verifique as orientações específicas de cada UF no Manual do Produto.”


## Sugestão de Layout




| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS30891 | Andréa Rocha | Essa MFS tem como objetivo criar parametrização para a geração específica por UF do Registro 1400 para deduções por CST e Produto. |
| MFS35568 | Vânia Mattos | Esta parametrização será retirada do módulo porque foi solicitada pelo cliente CPFL, que “desistiu” de utilizá-la. |


| Passo | Acionador | Descrição |
| --- | --- | --- |
| 1 | Usuário | Usuário seleciona o item de menu Parâmetros\ Registro 1400\ Específico por UF\ Exclusão Itens S/ Receita\ Por CST x Operação x Produto |
| 2 | Sistema | Verifica o usuário informou estabelecimento no login do Manager. |
| 3 | Sistema | Sistema abre a tela de seleção dos grupos cadastrados no Relacionamento entre Tabela e Grupos (Relac_Tab_Grupo).  Se no login foi informado estabelecimento, então: Sistema disponibilizados apenas os grupos relacionados ao estabelecimento em questão, relacionados a Tabela Situação Tributária Estadual – B cadastradas na TACES04 (Y2026_SIT_TRB_UF_B). Senão Sistema exibe os grupos dos estabelecimentos da empresa, relacionados a Tabela Situação Tributária Estadual – B cadastradas na TACES04 (Y2026_SIT_TRB_UF_B). |
| 4 | Usuário | Usuário seleciona um registro de grupo/estabelecimento do Relacionamento entre Tabela e Grupo. |
| 5 | Sistema | Abre a tela de Exclusão de Itens sem Receita – Por CST x Operação, com o campo Estabelecimento preenchido e bloqueado. |
| 6 | Usuário | Usuário seleciona um item na lista de “Operação”. |
| 7 | Sistema | Atualiza a lista de CST, demonstrando os CSTs marcados, caso já estejam gravados para a operação selecionada. |
| 8 | Usuário | Seleciona um ou mais CSTs da lista. |
| 9 | Usuário | Seleciona botão confirma. |
| 10 | Usuário | Seleciona outras ações disponíveis na barra de menu da janela. Vide tópico “Regra dos Botões” |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Texto | S | N | Formato:  Combo Box  Default: Desabilitado (ver tratamento) | Mostra o estabelecimento a ser parametrizado para geração dos registros.  Tratamento: O campo será apresentado de forma desbloqueada. Caso os usuário queira escolher outro estabelecimento, deverá acessar o botão “Selecionar Grupo” - vide tópico “Regra dos Botões”; | MFS-20147 |
| Grupo Produto | Texto | S | N | - | Este campo exibe o grupo selecionado pelo usuário na abertura da tela, ou alterado pelo usuário na opção “Seleciona Grupo” da barra de menu. | MFS-20147 |
| Produto | Texto | S | S | Formato: Pesquisar Pasta – Seleção de Produto  Default: Habilitado | Permitir seleção da tabela de Produtos SAFX2013.  Tratamento: Se o produto não estiver cadastrado enviar mensagem padrão no campo de produto não cadastrado. | MFS-20147 |
| Operação | Texto | S | N | Formato:  Combo Box  Default: Habilitado/Desabilitado (ver tratamento) | Permitir listar as operações específicas por UF.  Conteúdo:   Os códigos exibidos nesta lista correspondem aos códigos da TACES89, tabela que contém todos os itens da tabela “Tabela de Itens UF Índice de Participação dos Municípios”, criada por algumas UF’s para a geração do registro 1400, e disponível no site da EFD.   O campo “Operação” exibe apenas os códigos gerados de forma automática pelo sistema, e cuja geração utiliza esta parametrização. Isso significa que os códigos da TACES89 que não possuem geração automática, ou possuem, mas a geração não usa esta parametrização, não serão visualizados nesta lista.  Até o momento para os itens sem receita que precisa de exclusão no Registro 1400, apenas RS será tratado.  A lista exibirá apenas os códigos referentes à UF do estabelecimento informado, conforme aparece no quadro acima.  Após a escolha do estabelecimento e da operação, o campo “CST” exibirá a lista da Situação Tributária Estadual B disponíveis para cada tipo de operação (*), onde estarão marcados os CST já selecionados anteriormente, quando for o caso. | MFS-20147 |
| CST | Texto | S | S | Formato: Check Box  Default: Habilitado | Permitir demonstrar a Situação Tributária Estadual – B cadastradas na TACES04 da mesma forma que listamos para parâmetro por CFOP ou Natureza.  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. | MFS-20147 |
| Replicar para Estabelecimentos | Texto | N | S | Formato: Check Box  Default: Habilitado | Através desta opção o usuário poderá replicar a parametrização feita para outros estabelecimentos.  Ao clicar na opção “Replicar”, serão disponibilizados para seleção do usuário os estabelecimentos da Empresa do login, com exceção do estabelecimento já informado no campo “Estabelecimento”.  Ao salvar a operação com esta opção ativada, a parametrização feita será gravada para o estabelecimento informado, e também replicada para todos os estabelecimentos selecionados na opção da replicação.   Como facilitador, o usuário poderá utilizar as opções “Selecionar Todos” e “Desmarcar Todos”. | MFS-20147 |
