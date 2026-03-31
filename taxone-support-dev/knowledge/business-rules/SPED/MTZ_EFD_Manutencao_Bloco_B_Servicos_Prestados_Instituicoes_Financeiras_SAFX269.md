# MTZ_EFD_Manutencao_Bloco B_Servicos_Prestados_Instituicoes_Financeiras_SAFX269

> Fonte: MTZ_EFD_Manutencao_Bloco B_Servicos_Prestados_Instituicoes_Financeiras_SAFX269.docx






THOMSON REUTERS

Matriz da tela Serviços Prestados Instituições Financeiras SAFX269



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3
2.	Sugestão de Layout	7

## Regras dos Campos


Localização da tela: SPED\ EFD-Escrituração Fiscal Digital\ Geração\ Manutenção\ Bloco B (Apuração do ISS)\ B350 (Serviços Prestados Instituições Financeiras)

Título da tela: Registro B350 (Serviços Prestados Instituições Financeiras)

Regra Geral Botões:

NOVO – Permite inserir novo registro.

ABRE – Permite abrir seleção de registros inseridos.

EXCLUI – Permite excluir registro inserido.

CONFIRMA – Permite salvar registro.

RELATÓRIO – Permite emitir relatório listando todos os registros existentes na base de dados ou de acordo com a Empresa e Estabelecimento selecionados na tela de login (mostrar todos os campos como critério de busca).

FECHA – Permite sair da tela.

Regra Geral:

Os tamanhos dos campos devem seguir o tamanho criado em tabela SAFX269.

- O grupo da conta contábil deverá ser validado pelo Estabelecimento e Período da Apuração.


* Descrição não disponível em tela



## Sugestão de Layout




| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-21021 | Julyana Perrucini | Criação da tela de Serviços Prestados por Instituições Financeiras para atendimento do Registro B350 da EFD-ICMS/IPI/ISS. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Texto | S | N | Formato:  Combo Box  Default: Habilitado/Desabilitado (ver tratamento) | Permitir mostrar o estabelecimento a ser parametrizado para geração do registro.  Tratamento: O campo será apresentado de forma desbloqueada e caso o usuário entre com um estabelecimento no Login, somente este será apresentado bloqueado; O campo será apresentado de forma desbloqueada caso o usuário não entre com nenhum estabelecimento no Login, deverá apresentar a lista dos estabelecimentos da empresa iniciada; Se o campo não for preenchido, emitir a mensagem na tela: “O campo Estabelecimento deve ser informado”. | MFS-21021 |
| Período da Apuração | Data | S | N | Formato: MM/AAAA  Default: Não Informado | Nesse campo o usuário deverá informar o período da apuração que as informações serão declaradas.  Tratamento: Se o campo não for preenchido, emitir a mensagem na tela: “O campo Período da Apuração deve ser informado”. | MFS-21021 |
| Conta Contábil | Texto | S | N | Formato: Seleção SAFX2002  Default: Não Informado | Nesse campo o usuário deverá informar o código da conta de receita referente ao serviço prestado no Plano de Contas do declarante (SAFX2002).  Tratamento: Se o campo não for preenchido, emitir a mensagem na tela: “O campo Conta Contábil deve ser informado”. | MFS-21021 |
| Código COSIF | Texto | S | N | Formato: Seleção TFIX64  Default: Não Informado | Nesse campo o usuário deverá informar o código COSIF referente à receita com prestação de serviço (TFIX64).  Tratamento: Considerar apenas contas referenciais iniciadas com “7” (campo COD_CONTA_REF), de entidade igual a “20” (campo COND_ENTIDADE_RESP) e versão igual a “3.00” (campo VERSAO); Se o campo não for preenchido, emitir a mensagem na tela: “O campo Código COSIF deve ser informado”. | MFS-21021 |
| Cód. de Serviço Lei 116 | Texto | S | N | Formato: Seleção (TFIX60)  Default: Não Informado | Nesse campo o usuário deverá informar o item da lista da LC 116/03 correspondente ao serviço prestado (TFIX60).  Tratamento: Se o campo não for preenchido, emitir a mensagem na tela: “O campo Cód. de Serviço Lei 116 deve ser informado”. | MFS-21021 |
| Alíquota do ISS | Numérico | S | S | Formato: Text Input 0,0000  Default: Não Informado | Nesse campo o usuário deverá informar o valor da alíquota de incidência do ISS.  Tratamento: Se o campo não for preenchido, emitir a mensagem na tela: “O campo Alíquota do ISS deve ser informado”. | MFS-21021 |
| Qtd Ocorrências Conta | Numérico | S | S | Formato: Text Input  Default: Não Informado | Nesse campo o usuário deverá informar a quantidade, no período, de Registros B350 da EFD ICMS/IPI que referenciaram o mesmo código de conta.  Tratamento: Se o campo não for preenchido, emitir a mensagem na tela: “O campo Qtd Ocorrências Conta deve ser informado”. | MFS-21021 |
| Valor Contábil | Numérico | S | S | Formato: Text Input 0,00  Default: Não Informado | Nesse campo o usuário deverá informar o valor das prestações referentes à conta de receita.  Tratamento: Se o campo não for preenchido, emitir a mensagem na tela: “O campo Valor Contábil deve ser informado”. | MFS-21021 |
| Vlr. Base do ISS | Numérico | S | S | Formato: Text Input 0,00  Default: Não Informado | Nesse campo o usuário deverá informar o valor da base de cálculo do ISS correspondente às prestações referentes à conta de receita.  Tratamento: Se o campo não for preenchido, emitir a mensagem na tela: “O campo Vlr. Base do ISS deve ser informado”. | MFS-21021 |
| Vlr. do ISS | Numérico | S | S | Formato: Text Input 0,00  Default: Não Informado | Nesse campo o usuário deverá informar o valor do ISS correspondente às prestações referentes à conta de receita.  Tratamento: Se o campo não for preenchido, emitir a mensagem na tela: “O campo Vlr. do ISS deve ser informado”. | MFS-21021 |
| Código da Observação | Texto | N | S | Formato: Seleção SAFX2009  Default: Não Informado | Nesse campo o usuário deverá informar o código da observação do lançamento Fiscal, de acordo com a observação informada no Cadastro de Observações - Ato COTEPE/ICMS 35/05 (SAFX2009). | MFS-21021 |
