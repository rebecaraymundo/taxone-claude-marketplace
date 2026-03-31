# MTZ_EFD_Parametros_Registro_1400_Padrao_Deducoes_CST_Produto

> Fonte: MTZ_EFD_Parametros_Registro_1400_Padrao_Deducoes_CST_Produto.docx






THOMSON REUTERS

Parâmetros p/ Geração do Registro 1400 Padrão
Deduções – Por CST x Produto
EFD-Escrituração Fiscal Digital

Este menu foi retirado do módulo EFD, conforme reunião interna ocorrida em 02/06/2020 (veu documento de GCM da MFS35568)


DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3
2.	Sugestão de Layout	6

## Regras dos Campos


Localização da tela: SPED\ EFD-Escrituração Fiscal Digital\ Parâmetros\ Registro 1400\ Padrão\ Deduções\ Por CST x Produto

Título da tela: Deduções – Por CST x Produto

Considerações:

O objetivo dessa parametrização é reconhecer quais produtos que possuem desconto e precisam ser deduzidos dos valores totalizados para o Registro 1400 padrão, isso para quaisquer operações que possuam parametrização, identificando-as por CST;
Será permitido a parametrização de vários CST para o Estabelecimento e Produto parametrizado.

Regra Geral Botões:

SELECIONA GRUPO – Permite selecionar o grupo relacionado ao CST e produto a ser parametrizado.

NOVO – Permite incluir novo registro.

ABRE – Permite abrir uma janela para seleção dos registros, na tela deverão ser apresentados os campos chave para filtro das informações.

EXCLUI – Permite excluir registro.

CONFIRMA – Permite salvar registro.

RELATÓRIO – Permite emitir relatório listando todos os registros existentes na base de dados ou de acordo com a Empresa e Estabelecimento selecionados na tela de login (mostrar todos os campos como critério de busca).

FECHA – Permite sair da tela.



## Sugestão de Layout





| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS30891 | Andréa Rocha | Essa MFS tem como objetivo criar parametrização para a geração padrão do Registro 1400 para deduções por CST e Produto. |
| MFS35568 | Vânia Mattos | Esta parametrização será retirada do módulo porque foi solicitada pelo cliente CPFL, que “desistiu” de utilizá-la. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Texto | S | N | Formato:  Combo Box  Default: Habilitado/Desabilitado (ver tratamento) | Permitir mostrar o estabelecimento a ser parametrizado para geração dos registros.  Tratamento: O campo será apresentado de forma desbloqueada e caso o usuário entre com um estabelecimento no Login, somente este será apresentado bloqueado; O campo será apresentado de forma desbloqueada caso o usuário não entre com nenhum estabelecimento no Login, deverá apresentar a lista dos estabelecimentos da empresa iniciada; Se o campo não for preenchido, emitir a mensagem na tela: “Selecionar o Estabelecimento”. | MFS30891 |
| Grupo Produto | Texto | S | N | - | Este campo exibe o grupo selecionado pelo usuário na abertura da tela, ou alterado pelo usuário na opção “Seleciona Grupo” da barra de menu. | MFS30891 |
| Produto | Texto | S | S | Formato: Pesquisar Pasta – Seleção de Produto  Default: Habilitado | Permitir seleção da tabela de Produtos SAFX2013.  Tratamento: Se o produto não estiver cadastrado enviar mensagem padrão no campo de produto não cadastrado. | MFS30891 |
| CST | Texto | S | S | Formato: Check Box  Default: Habilitado | Permitir demonstrar a Situação Tributária Estadual – B cadastradas na TACES04 da mesma forma que listamos para parâmetro por CFOP ou Natureza.  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. | MFS30891 |
| Replicar para Estabelecimentos | Texto | N | S | Formato: Check Box  Default: Habilitado | Através desta opção o usuário poderá replicar a parametrização feita para outros estabelecimentos.  Ao clicar na opção “Replicar”, serão disponibilizados para seleção do usuário os estabelecimentos da Empresa do login, com exceção do estabelecimento já informado no campo “Estabelecimento”.  Ao salvar a operação com esta opção ativada, a parametrização feita será gravada para o estabelecimento informado, e também replicada para todos os estabelecimentos selecionados na opção da replicação.   Como facilitador, o usuário poderá utilizar as opções “Selecionar Todos” e “Desmarcar Todos”. | MFS30891 |
