# MTZ_EFD_Manutencao_Bloco B_Sociedade_Uniprofissional_SAFX221

> Fonte: MTZ_EFD_Manutencao_Bloco B_Sociedade_Uniprofissional_SAFX221.docx






THOMSON REUTERS

Manutenção Sociedade Profissional – Registro B500
EFD-Escrituração Fiscal Digital



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3
2.	Sugestão de Layout	6

## Regras dos Campos


Localização da tela: SPED\ EFD-Escrituração Fiscal Digital\ Geração\ Manutenção\ Bloco B (Apuração do ISS)\ Registro B500 (Sociedade Uniprofissional)

Título da tela: Registro B500 (Sociedade Uniprofissional)

Regra Geral Botões:

NOVO – Permite inserir novo registro.

ABRE – Permite abrir seleção de registros inseridos.

EXCLUI – Permite excluir registro inserido.

CONFIRMA – Permite salvar registro.

RELATÓRIO – Permite emitir relatório listando todos os registros existentes na base de dados ou de acordo com a Empresa e Estabelecimento selecionados na tela de login (mostrar todos os campos como critério de busca).

FECHA – Permite sair da tela.

Regra Geral:

Não podem existir estabelecimentos com mesmo período de lançamento.

Os tamanhos dos campos devem seguir o tamanho criado em tabela SAFX221.


## Sugestão de Layout





| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-21021 | Julyana Perrucini | Definição das regras de manutenção da Sociedade Uniprofissional (SAFX221). |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Texto | S | N | Formato:  Combo Box  Default: Bloqueado | Permitir mostrar estabelecimento a ser gerado para o Registro B500.  Tratamento: O campo será bloqueado caso o usuário entre com um estabelecimento no Login, o mesmo será apresentado e não haverá opção de modificar; O campo será habilitado caso o usuário não entre com um estabelecimento no Login, o mesmo deverá apresentar qualquer estabelecimento de qualquer UF; Se o campo não for preenchido, emitir a mensagem: “O Campo Estabelecimento é de preenchimento Obrigatório”. | MFS-21021 |
| Período | Numérico | S | N | Formato:  Texto  Default: Habilitado | Permitir preenchimento do período de lançamento para o Registro B500.  Tratamento: Após registro salvo o mesmo será bloqueado para alteração. Se o campo não for preenchido, emitir a mensagem: “O Campo Período é de preenchimento Obrigatório”. | MFS-21021 |
| Valor Mensal Receitas | Numérico | S | S | Formato: Texto  Default: Habilitado | Permitir o preenchimento do valor mensal das receitas auferidas pela sociedade.  Tratamento: Se o campo não for preenchido, emitir a mensagem: “O Campo Valor Mensal Receitas é de preenchimento Obrigatório”. | MFS-21021 |
| Qtde Profissionais Habilitados | Numérico | S | S | Formato: Texto  Default: Habilitado | Permitir o preenchimento da quantidade de profissionais habilitados.  Tratamento: Se o campo não for preenchido, emitir a mensagem: “O Campo Qtde Profissionais Habilitados é de preenchimento Obrigatório”. | MFS-21021 |
| Valor do ISS a Recolher | Numérico | N | S | Formato: Texto  Default: Habilitado | Permitir o preenchimento do valor do ISS a recolher no período. | MFS-21021 |
