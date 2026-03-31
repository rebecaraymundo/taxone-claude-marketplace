# MTZ_EFD_Manutencao_Bloco B_Profissionais_Habilitados_SAFX222

> Fonte: MTZ_EFD_Manutencao_Bloco B_Profissionais_Habilitados_SAFX222.docx






THOMSON REUTERS

Manutenção Profissionais Habilitados – Registro B510
EFD-Escrituração Fiscal Digital



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3
2.	Sugestão de Layout	6

## Regras dos Campos


Localização da tela: SPED\ EFD-Escrituração Fiscal Digital\ Geração\ Manutenção\ Bloco B (Apuração do ISS)\ Registro B510 (Profissionais Habilitados)

Título da tela: Registro B510 (Profissionais Habilitados)

Regra Geral Botões:

NOVO – Permite inserir novo registro.

ABRE – Permite abrir seleção de registros inseridos.

EXCLUI – Permite excluir registro inserido.

CONFIRMA – Permite salvar registro.

RELATÓRIO – Permite emitir relatório listando todos os registros existentes na base de dados ou de acordo com a Empresa e Estabelecimento selecionados na tela de login (mostrar todos os campos como critério de busca).

FECHA – Permite sair da tela.

Regra Geral:

Podem existir CPF repetidos no mesmo período.

Os tamanhos dos campos devem seguir o tamanho criado em tabela SAFX222.


## Sugestão de Layout





| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-21021 | Julyana Perrucini | Definição das regras de manutenção da Profissionais Habilitados (SAFX222). |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Texto | S | N | Formato:  Combo Box  Default: Bloqueado | Permitir mostrar estabelecimento a ser gerado para o Registro B510.  Tratamento: O campo será bloqueado caso o usuário entre com um estabelecimento no Login, o mesmo será apresentado e não haverá opção de modificar; O campo será habilitado caso o usuário não entre com um estabelecimento no Login, o mesmo deverá apresentar qualquer estabelecimento de qualquer UF; Se o campo não for preenchido, emitir a mensagem: “O Campo Estabelecimento é de preenchimento Obrigatório”. | MFS-21021 |
| Período | Numérico | S | N | Formato:  Texto  Default: Habilitado | Permitir preenchimento do período de lançamento para o Registro B510.  Tratamento: Após registro salvo o mesmo será bloqueado para alteração. Se o campo não for preenchido, emitir a mensagem: “O Campo Período é de preenchimento Obrigatório”. | MFS-21021 |
| CPF do Profissional | Texto | S | S | Formato: Texto  Default: Habilitado | Permitir preenchimento do CPF do profissional.  Tratamento: Se o campo não for preenchido ou for preenchido com menos de 11 posições, emitir a mensagem: “O Campo CPF é de preenchimento Obrigatório”. | MFS-21021 |
| Ind. Habilitação | Texto | N | S | Formato: Combo Box  Default: Habilitado | Permitir a seleção do indicador de habilitação do profissional.  Conteúdo: 0 – Profissional habilitado 1 – Profissional não habilitado | MFS-21021 |
| Ind. Escolaridade | Texto | N | S | Formato: Combo Box  Default: Habilitado | Permitir a seleção do indicador de escolaridade do profissional.  Conteúdo: 0 – Nível superior 1 – Nível médio | MFS-21021 |
| Ind. Participação Societária | Texto | N | S | Formato: Combo Box  Default: Habilitado | Permitir a seleção do indicador de participação societária do profissional.  Conteúdo: 0 – Sócio 1 – Não sócio | MFS-21021 |
| Nome do Profissional | Texto | N | S | Formato: Texto  Default: Habilitado | Permitir preenchimento do nome do profissional. | MFS-21021 |
