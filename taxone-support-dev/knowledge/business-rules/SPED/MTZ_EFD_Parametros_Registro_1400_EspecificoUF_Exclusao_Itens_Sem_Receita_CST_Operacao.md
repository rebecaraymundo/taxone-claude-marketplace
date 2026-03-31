# MTZ_EFD_Parametros_Registro_1400_EspecificoUF_Exclusao_Itens_Sem_Receita_CST_Operacao

> Fonte: MTZ_EFD_Parametros_Registro_1400_EspecificoUF_Exclusao_Itens_Sem_Receita_CST_Operacao.docx






THOMSON REUTERS

Parâmetros p/ Geração do Registro 1400 Específico por UF
Exclusão de Itens Sem Receita – Por CST x Operação
EFD-Escrituração Fiscal Digital



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3
2.	Sugestão de Layout	7

## Regras dos Campos


Localização da tela: SPED\ EFD-Escrituração Fiscal Digital\ Parâmetros\ Registro 1400\ Específico por UF\ Exclusão Itens S/ Receita\ Por CST x Operação

Título da tela: Exclusão de Itens sem Receita – Por CST x Operação

Considerações:

O intuito dessa parametrização é reconhecer quais produtos/ serviços que não possuem receita e precisam ser desconsiderados da geração da totalização do Registro 1400 específico por UF, isso para quaisquer operações que possuam parametrização, identificando-as por CST e Operação;
Será permitido a parametrização de vários CST para apenas uma parametrização por Operação.

Regra Geral Botões:

SELECIONA GRUPO – Permite selecionar o grupo relacionado ao CST a ser parametrizado.

NOVO – Permite incluir novo registro.

ABRE – Permite abrir uma janela para seleção dos registros, na tela deverão ser apresentados os campos chave para filtro das informações.

EXCLUI – Permite excluir registro.

CONFIRMA – Permite salvar registro.

RELATÓRIO – Permite emitir relatório listando todos os registros existentes na base de dados ou de acordo com a Empresa e Estabelecimento selecionados na tela de login (mostrar todos os campos como critério de busca).

FECHA – Permite sair da tela.


[MFS30891]
Incluir uma observação no final da tela referente ao campo Operação:
“A exibição do conteúdo para o campo Operação dependerá da UF do Estabelecimento selecionado. Apenas os Estabelecimentos cuja UF determina uma forma específica de geração apresentarão conteúdo para o campo. Verifique as orientações específicas de cada UF no Manual do Produto.”


## Sugestão de Layout




| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-20147 | Julyana Perrucini | Essa MFS tem como objetivo criar parametrização na regra de geração específica do Registro 1400 para exclusão de itens por CST e Operação que não possuem receita. |
| MFS30891 | Andréa Rocha | Inclusão da observação para o campo Operação. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Texto | S | N | Formato:  Combo Box  Default: Habilitado/Desabilitado (ver tratamento) | Permitir mostrar o estabelecimento a ser parametrizado para geração dos registros.  Tratamento: O campo será apresentado de forma desbloqueada e caso o usuário entre com um estabelecimento no Login, somente este será apresentado bloqueado; O campo será apresentado de forma desbloqueada caso o usuário não entre com nenhum estabelecimento no Login, deverá apresentar a lista dos estabelecimentos da empresa iniciada; Se o campo não for preenchido, emitir a mensagem na tela: “Selecionar o Estabelecimento”. | MFS-20147 |
| Operação | Texto | S | N | Formato:  Combo Box  Default: Habilitado/Desabilitado (ver tratamento) | Permitir listar as operações específicas por UF.  Conteúdo:   Os códigos exibidos nesta lista correspondem aos códigos da TACES89, tabela que contém todos os itens da tabela “Tabela de Itens UF Índice de Participação dos Municípios”, criada por algumas UF’s para a geração do registro 1400, e disponível no site da EFD.   O campo “Operação” exibe apenas os códigos gerados de forma automática pelo sistema, e cuja geração utiliza esta parametrização. Isso significa que os códigos da TACES89 que não possuem geração automática, ou possuem, mas a geração não usa esta parametrização, não serão visualizados nesta lista.  Até o momento para os itens sem receita que precisa de exclusão no Registro 1400, apenas RS será tratado.  A lista exibirá apenas os códigos referentes à UF do estabelecimento informado, conforme aparece no quadro acima.  Após a escolha do estabelecimento e da operação, o campo “CST” exibirá a lista da Situação Tributária Estadual B disponíveis para cada tipo de operação (*), onde estarão marcados os CST já selecionados anteriormente, quando for o caso. | MFS-20147 |
| CST | Texto | S | S | Formato: Check Box  Default: Habilitado | Permitir demonstrar a Situação Tributária Estadual – B cadastradas na TACES04 da mesma forma que listamos para parâmetro por CFOP ou Natureza.  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. | MFS-20147 |
| Replicar para Estabelecimentos | Texto | N | S | Formato: Check Box  Default: Habilitado | Através desta opção o usuário poderá replicar a parametrização feita para outros estabelecimentos.  Ao clicar na opção “Replicar”, serão disponibilizados para seleção do usuário os estabelecimentos da Empresa do login, com exceção do estabelecimento já informado no campo “Estabelecimento”.  Ao salvar a operação com esta opção ativada, a parametrização feita será gravada para o estabelecimento informado, e também replicada para todos os estabelecimentos selecionados na opção da replicação.   Como facilitador, o usuário poderá utilizar as opções “Selecionar Todos” e “Desmarcar Todos”. | MFS-20147 |
