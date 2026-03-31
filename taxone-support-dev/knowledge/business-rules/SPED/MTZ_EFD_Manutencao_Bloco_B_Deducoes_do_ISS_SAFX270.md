# MTZ_EFD_Manutencao_Bloco B_Deducoes_do_ISS_SAFX270

> Fonte: MTZ_EFD_Manutencao_Bloco B_Deducoes_do_ISS_SAFX270.docx






THOMSON REUTERS

Matriz da tela Deduções do ISS SAFX270



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3
2.	Sugestão de Layout	7

## Regras dos Campos


Localização da tela: SPED\ EFD-Escrituração Fiscal Digital\ Geração\ Manutenção\ Bloco B (Apuração do ISS)\ Registro B460 (Deduções do ISS)

Título da tela: Registro B460 (Deduções do ISS)

Regra Geral Botões:

NOVO – Permite inserir novo registro.

ABRE – Permite abrir seleção de registros inseridos.

EXCLUI – Permite excluir registro inserido.

CONFIRMA – Permite salvar registro.

RELATÓRIO – Permite emitir relatório listando todos os registros existentes na base de dados ou de acordo com a Empresa e Estabelecimento selecionados na tela de login (mostrar todos os campos como critério de busca).

FECHA – Permite sair da tela.

Regra Geral:

Os tamanhos dos campos devem seguir o tamanho criado em tabela SAFX270.


* Descrição não disponível em tela



## Sugestão de Layout




| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-21021 | Julyana Perrucini | Criação da tela de Deduções do ISS para atendimento do Registro B460 da EFD-ICMS/IPI/ISS. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Texto | S | N | Formato:  Combo Box  Default: Habilitado/Desabilitado (ver tratamento) | Permitir mostrar o estabelecimento a ser parametrizado para geração do registro.  Tratamento: O campo será apresentado de forma desbloqueada e caso o usuário entre com um estabelecimento no Login, somente este será apresentado bloqueado; O campo será apresentado de forma desbloqueada caso o usuário não entre com nenhum estabelecimento no Login, deverá apresentar a lista dos estabelecimentos da empresa iniciada; Se o campo não for preenchido, emitir a mensagem na tela: “O campo Estabelecimento deve ser informado”. | MFS-21021 |
| Período da Apuração | Data | S | N | Formato: MM/AAAA  Default: Não Informado | Nesse campo o usuário deverá informar o período da apuração que as informações serão declaradas.  Tratamento: Se o campo não for preenchido, emitir a mensagem na tela: “O campo Período da Apuração deve ser informado”. | MFS-21021 |
| Tipo de Dedução | Texto | S | N | Formato: Combo Box  Default: Não Informado | Nesse campo o usuário deverá informar o indicador do tipo de dedução.  Conteúdo: 0 - Compensação do ISS calculado a maior; 1 - Benefício fiscal por incentivo à cultura; 2 - Decisão administrativa ou judicial; 9 - Outros.  Tratamento: Se o campo não for preenchido, emitir a mensagem na tela: “O campo Tipo de Dedução deve ser informado”. | MFS-21021 |
| Indicador da Obrigação | Texto | S | N | Formato: Combo Box  Default: Não Informado | Nesse campo o usuário deverá informar a qual obrigação se refere a dedução.  Conteúdo: 0 - ISS Próprio; 1 - ISS Substituto; 2 - ISS Uniprofissionais.  Tratamento: Se o campo não for preenchido, emitir a mensagem na tela: “O campo Indicador da Obrigação deve ser informado”. | MFS-21021 |
| Valor da Dedução | Numérico | S | S | Formato: Text Input 0,00  Default: Não Informado | Nesse campo o usuário deverá informar o valor da dedução.  Tratamento: Se o campo não for preenchido, emitir a mensagem na tela: “O campo Valor da Dedução deve ser informado”. | MFS-21021 |
| Número do Processo | Texto | N | S | Formato: Text Input  Default: Não Informado | Nesse campo o usuário deverá informar o número do processo ao qual o ajuste está vinculado, se houver. | MFS-21021 |
| Origem do Processo | Texto | N | S | Formato: Combo Box  Default: Não Informado | Nesse campo o usuário deverá informar o indicador da origem do processo.  Conteúdo: 0 - Sefin; 1 - Justiça Federal; 2 - Justiça Estadual; 9 - Outros. | MFS-21021 |
| Descrição do Processo | Texto | N | S | Formato: Text Input  Default: Não Informado | Nesse campo o usuário deverá informar a descrição do processo que embasou o Lançamento. | MFS-21021 |
| Código da Observação | Texto | S | S | Formato: Seleção SAFX2009  Default: Não Informado | Nesse campo o usuário deverá informar o código da observação do lançamento Fiscal, de acordo com a observação informada no Cadastro de Observações - Ato COTEPE/ICMS 35/05 (SAFX2009).   Tratamento: Se o campo não for preenchido, emitir a mensagem na tela: “O campo Código da Observação deve ser informado”. | MFS-21021 |
