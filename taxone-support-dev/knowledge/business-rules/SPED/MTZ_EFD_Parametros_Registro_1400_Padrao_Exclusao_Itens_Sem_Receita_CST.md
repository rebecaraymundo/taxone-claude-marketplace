# MTZ_EFD_Parametros_Registro_1400_Padrao_Exclusao_Itens_Sem_Receita_CST

> Fonte: MTZ_EFD_Parametros_Registro_1400_Padrao_Exclusao_Itens_Sem_Receita_CST.docx






THOMSON REUTERS

Parâmetros p/ Geração do Registro 1400 Padrão
Exclusão de Itens Sem Receita – Por CST
EFD-Escrituração Fiscal Digital



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3
2.	Sugestão de Layout	6

## Regras dos Campos


Localização da tela: SPED\ EFD-Escrituração Fiscal Digital\ Parâmetros\ Registro 1400\ Padrão\ Exclusão Itens S/ Receita\ Por CST

Título da tela: Exclusão de Itens sem Receita – Por CST

Considerações:

O intuito dessa parametrização é reconhecer quais produtos/ serviços que não possuem receita e precisam ser desconsiderados da geração da totalização do Registro 1400 específico por UF, isso para quaisquer operações que possuam parametrização, identificando-as por CST;
Será permitido a parametrização de vários CST para o Estabelecimento parametrizado.

Regra Geral Botões:

SELECIONA GRUPO – Permite selecionar o grupo relacionado ao CST a ser parametrizado.

NOVO – Permite incluir novo registro.

ABRE – Permite abrir uma janela para seleção dos registros, na tela deverão ser apresentados os campos chave para filtro das informações.

EXCLUI – Permite excluir registro.

CONFIRMA – Permite salvar registro.

RELATÓRIO – Permite emitir relatório listando todos os registros existentes na base de dados ou de acordo com a Empresa e Estabelecimento selecionados na tela de login (mostrar todos os campos como critério de busca).

FECHA – Permite sair da tela.



## Sugestão de Layout




| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-20147 | Julyana Perrucini | Essa MFS tem como objetivo criar parametrização na regra de geração específica do Registro 1400 para exclusão de itens por CST que não possuem receita. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Texto | S | N | Formato:  Combo Box  Default: Habilitado/Desabilitado (ver tratamento) | Permitir mostrar o estabelecimento a ser parametrizado para geração dos registros.  Tratamento: O campo será apresentado de forma desbloqueada e caso o usuário entre com um estabelecimento no Login, somente este será apresentado bloqueado; O campo será apresentado de forma desbloqueada caso o usuário não entre com nenhum estabelecimento no Login, deverá apresentar a lista dos estabelecimentos da empresa iniciada; Se o campo não for preenchido, emitir a mensagem na tela: “Selecionar o Estabelecimento”. | MFS-20147 |
| CST | Texto | S | S | Formato: Check Box  Default: Habilitado | Permitir demonstrar a Situação Tributária Estadual – B cadastradas na TACES04 da mesma forma que listamos para parâmetro por CFOP ou Natureza.  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. | MFS-20147 |
| Replicar para Estabelecimentos | Texto | N | S | Formato: Check Box  Default: Habilitado | Através desta opção o usuário poderá replicar a parametrização feita para outros estabelecimentos.  Ao clicar na opção “Replicar”, serão disponibilizados para seleção do usuário os estabelecimentos da Empresa do login, com exceção do estabelecimento já informado no campo “Estabelecimento”.  Ao salvar a operação com esta opção ativada, a parametrização feita será gravada para o estabelecimento informado, e também replicada para todos os estabelecimentos selecionados na opção da replicação.   Como facilitador, o usuário poderá utilizar as opções “Selecionar Todos” e “Desmarcar Todos”. | MFS-20147 |
