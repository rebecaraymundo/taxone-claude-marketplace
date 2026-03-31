# MTZ_Tela_Detalhamento_Ajustes_BC_Valores_Extra_Apuracao

> Fonte: MTZ_Tela_Detalhamento_Ajustes_BC_Valores_Extra_Apuracao.docx






THOMSON REUTERS

Matriz da tela Detalhamento de Ajustes de BC - Valores Extra Escrituração - 1050



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3
2.	Sugestão de Layout	9

## Regras dos Campos


Localização da tela:
Módulo: SPED >> EFD-Contribuições Financeira/Assemelhada
Menu: Obrigações >> Manutenção >> Registros do Bloco 1 >> Ajustes BC - Valores Extra Escrituração – (1050)

Deverá ser criada a tela “Detalhamento de Ajustes de BC - Valores Extra Escrituração - 1050” para que seja possível realizar a geração do registro 1050 da EFD- Financeira.

Regra Geral Botões:

NOVO – Permite incluir novo registro.

ABRE – Permite abrir uma janela para seleção dos registros, na tela deverão ser apresentados os campos chave para filtro das informações.

EXCLUI – Permite excluir registro.

CONFIRMA – Permite salvar registro.

RELATÓRIO – Permite emitir relatório listando todos os registros existentes na base de dados ou de acordo com a Empresa e Estabelecimento selecionados na tela de login (mostrar todos os campos como critério de busca).

FECHA – Permite sair da tela.

Tratamento:
- Não será possível repetir o mesmo valor para o campo: “Estabelecimento”,  “Mês/ Ano Apuração”, “Data Referência”, “Indicador Natureza” e “Apropriação Ajuste”; e se houver, emitir a mensagem na tela: “Atenção, já existe registro com a chave informada, favor corrigir manutenção.”.


* Descrição não disponível em tela


## Sugestão de Layout




| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS25094 | Andréa Rocha | Criação da tela de Detalhamento de Ajustes de Base de Cálculo - Valores Extra Escrituração - 1050 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Texto | S | N | Formato:  Combo Box  Default: Habilitado/Desabilitado (ver tratamento) | Permitir mostrar o estabelecimento a ser parametrizado para geração do registro.  Tratamento: O campo será apresentado de forma desbloqueada e caso o usuário entre com um estabelecimento no Login, somente este será apresentado bloqueado; O campo será apresentado de forma desbloqueada caso o usuário não entre com nenhum estabelecimento no Login, deverá apresentar a lista dos estabelecimentos da empresa iniciada; Se o campo não for preenchido, emitir a mensagem na tela: “O campo Estabelecimento deve ser informado”. | MFS25094 |
| Mês/ Ano Apuração | Data | S | N | Formato: MM/AAAA  Default: Não Informado | Nesse campo o usuário deverá informar o mês e o ano da apuração em que os ajustes serão declarados.  Tratamento: Se o campo não for preenchido, emitir a mensagem na tela: “O campo Mês/ Ano Apuração deve ser informado”. | MFS25094 |
| Data Referência | Data | S | S | Formato: DD/MM/AAAA  Default: Não Informado | Nesse campo o usuário deverá informar a data de referência do ajuste.  Tratamento: Aceitar inclusive nulo. | MFS25094 |
| Indicador Natureza | Texto | S | S | Formato: Combo Box  Default: Não Informado | Nesse campo o usuário deverá informar a natureza do ajuste da base de cálculo conforme tabela externa disponibilizada pela Receita Federal.  Conteúdo: 01-Vendas canceladas de receitas tributadas em períodos anteriores; 02-Devoluções de vendas tributadas em períodos anteriores; 21-ICMS a recolher sobre Operações próprias; 41-Outros valores a excluir, vinculados a decisão judicial; 42-Outros valores a excluir, não vinculados a decisão judicial. | MFS25094 |
| Apropriação Ajuste | Texto | S | S | Formato: ComboBox  Default: Não Informado | Nesse campo o usuário deverá informar o indicador da apropriação do ajuste.  Conteúdo: 01 – Referente ao PIS/Pasep e a Cofins; 02 – Referente unicamente ao PIS/Pasep; 03 – Referente unicamente à Cofins.  Tratamento: Se o campo não for preenchido, emitir a mensagem na tela: “O campo Apropriação Ajuste deve ser informado”. | MFS25094 |
| CNPJ | Texto | S | S | Formato: 00.000.000/0000-00  Default: Não Informado | Nesse campo o usuário deverá informar o CNPJ do estabelecimento da empresa, a que se refere o ajuste informado no campo “Código do Ajuste”. Caso o ajuste não se refira a um estabelecimento específico, poderá ser informado pela empresa o CNPJ do estabelecimento matriz.  Tratamento: Se o campo não for preenchido, emitir a mensagem na tela: “O campo CNPJ deve ser informado”. | MFS25094 |
| Valor Total Ajuste | Numérico | N | S | Formato: 0,00  Default: Não Informado | Nesse campo o usuário deverá informar o valor total do ajuste. | MFS25094 |
| Valor Ajuste CST01 | Numérico | N | S | Formato: 0,00  Default: Não Informado | Nesse campo o usuário deverá informar a parcela do ajuste a apropriar na base de cálculo referente ao CST 01. | MFS25094 |
| Valor Ajuste CST02 | Numérico | N | S | Formato: 0,00  Default: Não Informado | Nesse campo o usuário deverá informar a parcela do ajuste a apropriar na base de cálculo referente ao CST 02. | MFS25094 |
| Valor Ajuste CST03 | Numérico | N | S | Formato: 0,00  Default: Não Informado | Nesse campo o usuário deverá informar a parcela do ajuste a apropriar na base de cálculo referente ao CST 03. | MFS25094 |
| Valor Ajuste CST04 | Numérico | N | S | Formato: 0,00  Default: Não Informado | Nesse campo o usuário deverá informar a parcela do ajuste a apropriar na base de cálculo referente ao CST 04. | MFS25094 |
| Valor Ajuste CST05 | Numérico | N | S | Formato: 0,00  Default: Não Informado | Nesse campo o usuário deverá informar a parcela do ajuste a apropriar na base de cálculo referente ao CST 05. | MFS25094 |
| Valor Ajuste CST06 | Numérico | N | S | Formato: 0,00  Default: Não Informado | Nesse campo o usuário deverá informar a parcela do ajuste a apropriar na base de cálculo referente ao CST 06. | MFS25094 |
| Valor Ajuste CST07 | Numérico | N | S | Formato: 0,00  Default: Não Informado | Nesse campo o usuário deverá informar a parcela do ajuste a apropriar na base de cálculo referente ao CST 07. | MFS25094 |
| Valor Ajuste CST08 | Numérico | N | S | Formato: 0,00  Default: Não Informado | Nesse campo o usuário deverá informar a parcela do ajuste a apropriar na base de cálculo referente ao CST 08. | MFS25094 |
| Valor Ajuste CST09 | Numérico | N | S | Formato: 0,00  Default: Não Informado | Nesse campo o usuário deverá informar a parcela do ajuste a apropriar na base de cálculo referente ao CST 09. | MFS25094 |
| Valor Ajuste CST49 | Numérico | N | S | Formato: 0,00  Default: Não Informado | Nesse campo o usuário deverá informar a parcela do ajuste a apropriar na base de cálculo referente ao CST 49. | MFS25094 |
| Valor Ajuste CST99 | Numérico | N | S | Formato: 0,00  Default: Não Informado | Nesse campo o usuário deverá informar a parcela do ajuste a apropriar na base de cálculo referente ao CST 99. | MFS25094 |
| Nº Recibo | Texto | N | S | Formato: Text Input  Default: Não Informado | Nesse campo o usuário deverá informar o número do recibo da escrituração a que se refere o ajuste. | MFS25094 |
| Informação Complementar | Texto | N | S | Formato: Text Input  Default: Não Informado | Nesse campo o usuário poderá utilizar para acrescentar informações complementares do registro. | MFS25094 |
