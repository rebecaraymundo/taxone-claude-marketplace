# MTZ_Tela Parametrização da Outros Lançamentos da Apuração

> Fonte: MTZ_Tela Parametrização da Outros Lançamentos da Apuração.docx






THOMSON REUTERS

Matriz da tela Contabilização
Tela de Parâmetro Outros Lançamentos da Apuração



DOCUMENTO DE REQUISITO


Sumário

1.	INTRODUÇÃO	3
2.	Documento de Referência	3
3.	Fluxo Principal Seleção de dados – Menu Ajustes	3
2.3	Menu Outros Lançamentos da Apuração, Parametrização	4
2.4	Prótotipo - Tela Menu Ajustes Outros lançamentos da Apuração - Parametrização:	4
2.5	Funcionalidades:	6
2.6	Lista de campos:	6
2.7	Regra de botões:	11
4.	DDL criação de Tabela – Parâmetros  Lançamentos Contábeis Outros Lançamentos Contábeis	13
5.	REGRAS DE NEGÓCIO – CÓDIGOS DE AJUSTES DE APURAÇÕES	16
Descrição	16
ADO	16


## INTRODUÇÃO


Desenvolver uma interface de parâmetros que permita ao usuário configurar os códigos de ajustes relacionados à apuração de impostos, tais como ICMS, ICMS Antecipado, ICMS-ST, IPI, PIS/COFINS e SCANC. Após a conclusão da apuração dos tributos, o sistema facilitará a associação desses ajustes às respectivas contas contábeis.

## Documento de Referência

MTZ – Tela Seleção de dados – incluir
MTZ – Tela de Parâmetros Ajustes da Apuração

## Fluxo Principal Seleção de dados – Menu Ajustes

Este caso de uso descreve o processo para a geração de relatórios de Saldos Importados – Importação da Contabilização.


Localização da Tela:
- Agrupamentos: Básico
- Módulo: Manutenção >> Contabilização Apuração >>Seleção de Dados/ Parâmetros >> Paramentos de Outros Lançamentos Contábeis
- Menu: Acesso Principal >> Seleção de Dados


## Menu Outros Lançamentos da Apuração, Parametrização


## Prótotipo - Tela Menu Ajustes Outros lançamentos da Apuração - Parametrização:



## Funcionalidades:

Visualizar lista de ajustes fiscais já cadastrados para o contexto selecionado.
Incluir novo ajuste fiscal, preenchendo campos obrigatórios e opcionais.
Editar ou remover ajustes existentes.
Aplicar regras de negócio específicas por tipo de ajuste e imposto.
Salvar e validar alterações, com mensagens claras de sucesso ou erro.

## Lista de campos:



## Regra de botões:







## DDL criação de Tabela – Parâmetros  Lançamentos Contábeis Outros Lançamentos Contábeis
























## REGRAS DE NEGÓCIO – CÓDIGOS DE AJUSTES DE APURAÇÕES




Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:


Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:























| OS/CH | Nome | Descrição |
| --- | --- | --- |
| ADO 913117 | Millys Lopes | Tela Parametrização Outros Lançamentos Contábeis |
|  |  |  |


| Documentação do Caso de Uso | Documentação do Caso de Uso |
| --- | --- |
| Ator Principal | Usuário do sistema |
| Pré- Condições | Acessa a tela de Principal dos menus |
| Pós-Condições | O sistema abrir como pop-up/modal sobre a tela principal o menu de Outros Lançamentos da Apuração |


| Ações do Ator | Ações do Sistema |
| --- | --- |
| Acesso a Tela Seleção de Dados | O usuário clicar no menu "Outros Lançamentos", que abre a tela correspondente em formato pop-up/modal, permitindo realizar as parametrizações necessárias. |
| Pesquisa de Parametrizações | O usuário realiza pesquisas para localizar parametrizações existentes, utilizando filtros para refinar os resultados. |
| Inclusão/Edição/Exclusão | O sistema permite ao usuário incluir novas parametrizações, editar as existentes ou excluir ajustes conforme necessário. |
| Preenchimento de Campos | Durante a parametrização, o usuário preenche os campos obrigatórios e opcionais, como tipo de documento, conta contábil e chave de lançamento. |
| Importação de Parametrizações | O usuário pode importar parametrizações, preenchendo ou importando dados via job do servidor. O sistema valida o layout e os campos, exibindo erros ou confirmando a importação. |
| Salvamento | O usuário salva a parametrização. O sistema grava as informações no banco de dados, registrando o usuário responsável e a data/hora da operação. |
| Finalização | O usuário pode finalizar as operações ou encerrar a sessão no sistema. |


| Menu | Descrição | Comportamento/Observações |
| --- | --- | --- |
| Outros Lançamentos | Permite acessar tela de ajustes fiscais vinculados aos Grupo de Impostos... | Abrir como pop-up/modal sobre a tela principal |


| Cód. | Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RN00 | Empresa | Campo | S | S | Default: selecionado | Visualizar a empresa selecionada no sistema Tax One | ADO 913117 |
| RN01 | Estabecimento | Checkbox | S | S | Default: Não selecionado | Este campo permite ao usuário selecionar um ou mais estabelecimentos para realizar os parâmetros de ajustes ou visualizar informações já cadastrados. As opções exibidas incluem os estabelecimentos vinculados ao login do usuário e que possuem cadastro liberado nos dados pertinentes. Informações Apresentadas: Cada estabelecimento será exibido na lista com: Código do estabelecimento e Razão social cadastrada O formato de exibição será: XXX - XXXXXXXXXXXXXXXXX  Caso o usuário não selecione nenhum estabelecimento específico, o sistema poderá exibir “Todos” os estabelecimentos disponíveis. | ADO 913117 |
| RN02 | UF | Checkbox | Não | S | Default: Não selecionado | Este campo mostra as UFs dos estabelecimentos que foram selecionados no campo RN01. O usuário pode selecionar uma ou mais UFs para visualizar os ajustes disponíveis para parâmetros atrelados ao grupo de impostos. Se nenhum estabelecimento for selecionado em RN01 ou se o usuário desejar ver todos os estabelecimentos, o campo pode ser preenchido este campo como "Todas UFs". Observação objetivo é facilitar a visualização de ajustes de parâmetros fiscais por UF, baseando-se nos estabelecimentos selecionados.’ | ADO 913117 |
| RN03 | Grupo Imposto | Dropdown | Sim | Sim | Default: Não preenchido | O sistema permite ao usuário selecionar, através de uma lista: Federal Estadual  Caso não selecionado exibir a seguinte mensagem: “Grupo Informar o preenchimento é de âmbito Federal ou Estadual” | ADO 913117 |
| RN04 | Impostos | Dropdown | Sim | Sim | Alfanumérico | Este campo será apresentado apenas quando selecionado o “Grupo Imposto”   Caso selecionado “Federal” deverá listar os seguintes tributos: PIS -Cumulativo PIS -Não Cumulativo COFINS- Cumulativo COFINS-Não Cumulativo IPI Caso selecionado “Estadual” deverá listar os seguintes tributos: ICMS- Próprio ICMS-ST ICMS-Antecipado FCP DIFAL SCANC | ADO 913117 |
| RN05 | Referência | Campo | Não | Não | Alfanumérico | O preenchimento deste campo deve ser realizado manualmente pelo usuário, permitindo a inserção de informações de forma livre, conforme necessário. As informações inseridas  são dadas  para o sistema SAP | ADO 913117 |
| RN06 | Outros Lançamentos | Dropdown | Sim | Sim | Lista | Regra de Seleção Automática: O sistema deve aplicar automaticamente a regra de negócio pertinente ao imposto selecionado. Para cada imposto, os valores associados devem ser exibidos no dropdown "Outros Lançamentos". Funcionamento da Regra: Quando o usuário selecionar os impostos: ICMS Próprio, ICMS-ST,  IPI, : 014-SALDO CREDOR (CRÉDITO MENOS DÉBITO) A TRANSPORTAR P/ O PERÍODO SEGUINTE  011-SALDO DEVEDOR (DÉBITO MENOS CRÉDITO)      PIS - Cumulativo, PIS - Não Cumulativo, COFINS - Cumulativo e COFINS - Não Cumulativo: Saldo Devedor Saldo Credor Total de Crédito Total de Débito F100 - Demais Receitas F100 - Demais Créditos | ADO 913117 |
| RN07 | Código da Op.Apuração ou F100 | Dropdown | Sim | Sim | Alfanúmerico | Automaticamente a regra de negócio pertinente ao imposto selecionado. Para cada imposto selecionado, o sistema deve exibir no dropdown "Código da Natureza/Receita” informando o campo de acordo  e concatenado com Descrição" somente as opções correspondentes, conforme o mapeamento definido nas regras de negócio (RN) especificadas no documento. Após a escolha da opção, o sistema deve aplicar Tratamentos: Mensagem: Ao menos um Código de Ajustes deve ser selecionado. | ADO 913117 |
| RN08 | Indicador da Conta | Dropdown | Sim | Sim | Alfanúmerico | Dropdown: O sistema deve apresentar um menu dropdown que lista valores do campo IND_NATUREZA -SAFX2002. Filtragem de Códigos: Antes de listar no dropdown, o sistema deve filtrar os registros para incluir somente aqueles cujo IND_NATUREZA se enquadra nas categorias '1-Ativo', '2-Passivo' ou '3-Despesa'.para seleção do usuário | ADO 913117 |
| RN09 | Conta Contábil | Dropdown | Sim | Sim | Default: não selecionado | Permitir ao usuário selecionar uma conta contábil ativa de um dropdown que lista códigos de contas cadastrados e que estão ativos na SAFX2002. Situação da Conta (IND_SITUACAO):Incluir apenas contas onde o campo IND_SITUACAO seja igual  Filtragem por Indicador da Conta: As contas devem ser filtradas com base na seleção feita pelo usuário no campo "Indicador da conta". O dropdown permite buscas tanto pelo código da conta (COD_CONTA) quanto pela descrição (DESCRICAO), facilitando a localização e seleção da conta desejada pelo usuário. Se o campo 'Conta Contábil' não for preenchido ou nenhuma conta for selecionada, o sistema deve apresentar a seguinte mensagem de erro: "A conta contábil deve ser informada tanto para débito quanto para crédito." | ADO 913117 |
| RN10 | Chave de Lançamento | campos | Sim | Sim | Default: selecionado | Chave de Lançamento: Criar os campos para apresentar as seguintes opções, permitindo a identificação do tipo de lançamento contábil: 40: Para informar a conta a Débito 50: Para informar a conta a crédito O usuário deverá parametrizar as informações conforme a chave adequada em cada campo, garantindo o correto registro do lançamento contábil. Tratamento: Caso o usuário tente preencher apenas o lançamento a débito e não preencha o lançamento a crédito ou vice e versa, o sistema deverá exibir uma mensagem de alerta informando o preenchimento. informações a débito e crédito é obrigatória para prosseguir. Mensagem sugerida: "É obrigatório lançamentos das informações a  crédito e a débito  para concluir a parametrização e salvar. | ADO 913117 |
| RN11 | Divisão | Campo | Não | Sim | Alfanúmerico | O preenchimento deste campo deve ser realizado manualmente pelo usuário, permitindo a inserção de informações de forma livre, conforme necessário. As informações inseridas são dadas do SAP | ADO 913117 |
| RN12 | Local de Negócio | Campo | Não | Sim | Alfanúmerico | O preenchimento deste campo deve ser realizado manualmente pelo usuário, permitindo a inserção de informações de forma livre, conforme necessário. As informações inseridas  são dadas  para o sistema SAP | ADO 913117 |
| RN13 | Centro | Campo | Não | Sim | Alfanúmerico | O preenchimento deste campo deve ser realizado manualmente pelo usuário, permitindo a inserção de informações de forma livre, conforme necessário. As informações inseridas  são dadas  para o sistema SAP | ADO 913117 |
| RN14 | Código de Custo | Campo | Não | Não | Numérico | O campo "Código de custo" deverá ser preenchido para cada lançamento, tanto para a chave 40 (débito) quanto para a chave 50 (crédito), permitindo a vinculação do respectivo centro de custo ao lançamento contábil. As opções disponíveis para seleção serão apresentadas em formato dropdown, com base nos dados da tabela SAFX2003 – Tabela de Centro de Custo. O sistema deve listar todos os códigos de custo cadastrados e ativos (campo COD_CUSTO) Para cada código exibido no dropdown, o sistema deve concatenar e apresentar também a descrição do centro de custo (campo DESCRICAO), seguindo o padrão:  [COD_CUSTO] - [DESCRICAO] para auxiliar o usuário no preenchimento. | ADO 913117 |
| RN15 | Centro de Lucro | Campo | Não | Sim | Numérico | O preenchimento deste campo deve ser realizado manualmente pelo usuário, permitindo a inserção de informações de forma livre, conforme necessário. As informações inseridas  são dadas  para o sistema SAP | ADO 913117 |
| RN16 | Texto -Histórico |  | Não |  | Alfanúmerico | O preenchimento deste campo deve ser realizado manualmente pelo usuário, permitindo a inserção de informações de forma livre, conforme necessário. As informações inseridas  são dadas  para o sistema SAP | ADO 743907 |
| RN17 | Observação Lançamentos |  | Não |  | Alfanúmerico | O preenchimento deste campo deve ser realizado manualmente pelo usuário, permitindo a inserção de informações de forma livre, conforme necessário. As informações inseridas  são dadas  para o sistema SAP | ADO 743907 |


| Cód. | NOME | Tipo | Obrig | Ed | Formato/Default |  | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Salvar | Botão | _ | - | _ |  | Função: Registra no sistema as informações preenchidas ou alteradas pelo usuário.  Valida todos os campos obrigatórios e as regras de negócio antes de gravar. Caso haja erro, exibe mensagem indicando o campo a ser corrigido. Ao sucesso, grava os dados no banco, registra usuário e data/hora, e exibe mensagem de confirmação. Atualiza imediatamente as listas e relatórios na tela. Após salvar, o formulário pode ser limpo automaticamente ou permanecer preenchido, conforme configuração do sistema. | ADO 913117 |
|  | Limpar | Botão | _ | _ | _ |  | Função: Limpa todos os campos do formulário, permitindo ao usuário iniciar um novo preenchimento. Ao clicar em Limpar, todos os campos do formulário de parametrização retornam ao estado inicial (em branco ou valor default). Não afeta os dados já salvos no banco de dados; apenas limpa o formulário atual. Exibe mensagem de confirmação caso haja dados não salvos no formulário (opcional). | ADO 9131177 |
|  | Editar | Botão | _ | _ | _ |  | Função: Permite ao usuário alterar os dados de uma parametrização já existente. O usuário deve selecionar um registro existente na lista para habilitar o botão Editar. Ao clicar em Editar, os campos do registro selecionado ficam habilitados para alteração. Após editar, o usuário deve clicar em Salvar para registrar as alterações. Se cancelar ou sair sem salvar, as alterações não são gravadas. O sistema registra usuário, data e hora da última alteração. | ADO 913117 |
|  | Excluir | Botão |  |  |  |  | Função: Permite ao usuário remover definitivamente uma parametrização existente. Regras: O usuário deve selecionar um registro existente na lista para habilitar o botão Excluir. Ao clicar em Excluir, o sistema solicita confirmação antes de remover o registro (exemplo: “Deseja realmente excluir esta parametrização?”). Ao confirmar, o sistema remove o registro do banco de dados e atualiza a lista. O sistema registra o usuário, data e hora da exclusão para auditoria. Não é possível desfazer a exclusão após confirmação. | ADO 913117 |
|  | Pesquisar | Botão |  |  |  |  | Este campo permite ao usuário realizar pesquisas em parâmetros previamente cadastrados, utilizando os seguintes critérios: Empresa Estabelecimento UF (Unidade Federativa) Código do Ajuste | ADO 913117 |


| CAMPO | NOME | NOME | COMENTARIO | TIPO | TAMANHO | OBRIG | OBRIG | CHAVE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Código da Empresa | COD_EMPRESA | COD_EMPRESA | Campo destinado ao código da Empresa. Vide regra RN00 | Alfanúmerico | 003 | Sim | Sim | (*) |
| Código do Estabecimento | COD_ESTABELECIMENTO | COD_ESTABELECIMENTO | Campo destinado ao código do Estabelecimento. Vide regra RN01 | Alfanúmerico | 006 | Sim | Sim | (*) |
| UF | UF | UF | Informar a sigla da Unidade Federativa (UF) correspondente ao estabelecimento. | Texto | 002 |  |  |  |
| Referência | REFERENCIA | REFERENCIA | O Preenchimento é livre os dados provenientes dos 'Livros Fiscais' ou da Apuração do Sistema SAP. | Texto | 016 |  |  |  |
| Grupo de Imposto | GRUPO_IMPOSTO | GRUPO_IMPOSTO | Informar o preenchimento é de âmbito Federal ou Estadual. Vide regra RN03 | Texto | 10 | Sim | Sim | (*) |
| Imposto | IMPOSTO | IMPOSTO | Informar o preenchimento do imposto atrelado ao âmbito Federal ou Estadual. Vide regra RN04 | Texto | 030 | Sim | Sim | (*) |
| Local de Negócio | LOCAL_NEGÓCIO | LOCAL_NEGÓCIO | O Preenchimento é livre indica o código correspondente a um estabelecimento dentro da matriz no sistema SAP. | Alfanúmerico | 004 |  |  |  |
| Divisão | DIVISÃO | DIVISÃO | O Preenchimento é livre indica a segregação financeira de um segmento específico dentro do sistema SAP. | Alfanúmerico | 004 |  |  |  |
| Centro | Centro | Centro | O Preenchimento é livre indica a segregação SAP | Alfanúmerico | 004 |  |  |  |
| Outros Lançamentos | OUTRO_LANCAMENTOS_CONTABEIS | OUTRO_LANCAMENTOS_CONTABEIS | Identificar os seguintes tipos de lançamentos (este dado preencher conforme dados da RN07):  Saldo Devedor, Saldo Credor,  Total de Crédito,  Total de Débito,  F100 - Demais Receitas   F100 - Demais Créditos. | Texto | 050 | Sim | Sim |  |
| Código da Natureza da Receita | COD_NAT_REC | COD_NAT_REC | Informar o código da Natureza da Receita  da operação/serviço não tributada ou não sujeita ao pagamento da contribuição PIS/COFINS da SAFX 147 este dado preencher conforme dados da RN07 | Númerico | 003 | Sim | Sim |  |
| Descrição complementar do Documento/Operação | DESC_COMPL | DESC_COMPL | Informar a descrição complementar do Documento/Operação.SAFX147- este dado preencher conforme dados da RN07 | Alfanúmerico | 255 | Sim | Sim |  |
| Código Op.Apuração | COD_OPER_APUR | COD_OPER_APUR | Informar o Código da Apuração do ICMS | Númerico | 005 |  |  |  |
| Descrição da Apuração | DSC_OPER_APUR | DSC_OPER_APUR | Informa a Descrição do código da descrição da Apuração do ICMS | Alfanúmerico | 050 |  |  |  |
| Indicador de Situação da Conta | IND_SITUACAO | IND_SITUACAO | Informar se conta está sendo utilizada ou não pela Contabilidade da empresa. O campo assume os seguintes valores: A – Ativa na SAFX2002 | Alfanúmerico | 001 | Sim | Sim |  |
| Indicador de Natureza | IND_NATUREZA | IND_NATUREZA | Informar o Indicador de Natureza existente na SAFX2002: 1. Ativo 2. Passivo 3. Despesa | Alfanúmerico | 001 | Sim | Sim |  |
| Conta Contábil Débito | COD_CONTA_D | COD_CONTA_D | Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas (SAFX2002). | Númerico | 070 | Sim | Sim |  |
| Descrição da Conta | DESCRICAO_CONTA_D | DESCRICAO_CONTA_D | Informar a Descrição da Conta existente na SAFX2002 | Alfanúmerico | 050 | Sim | Sim |  |
|  |  |  |  |  |  | Sim | Sim |  |
| Chave de lançamento | CHAVE_LANCTO_D | CHAVE_LANCTO_D | Indica que o preenchimento é fixo com o valor '40' para transações de débito. | Númerico | 002 | Sim | Sim |  |
| Código de Custo | COD_CUSTO_C | COD_CUSTO_C | Informar o Centro de Custo. O Código deve estar registrado na Tabela de Centro de Custos (SAFX2003). | Numérico | 020 |  |  |  |
| Descrição do Centro de Custo | DESCRICAO_CENTRO_CUSTO_D | DESCRICAO_CENTRO_CUSTO_D | Informar o Centro de Custo. A descrição do centro de custo deve estar registrada na Tabela de Centro de Custos (SAFX2003). | Alfanúmerico | 050 |  |  |  |
| Centro Lucro | CENTRO_LUCRO_D | CENTRO_LUCRO_D | O preenchimento é livre e informar o código do centro de lucros, utilizado para alocar receitas ou despesas de forma similar ao centro de custo. Este campo é opcional e serve apenas para controle interno. | Numérico | 020 |  |  |  |
| Texto Histórico | TEXTO_D | TEXTO_D | Informar o histórico da contabilização contábil | Alfanúmerico | 020 | Sim | Sim |  |
| Observações Lançamentos | OBSERVAÇÃO_D | OBSERVAÇÃO_D | Registrar a observação referente ao lançamento. | Alfanúmerico | 020 |  |  |  |
| Conta Contábil Crédito | COD_CONTA_C | COD_CONTA_C | Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas (SAFX2002). | Númerico | 070 | Sim | Sim |  |
| Descrição da Conta | DESCRICAO_CONTA_C | DESCRICAO_CONTA_C | Informar a Descrição da Conta existente na SAFX2002 | Alfanúmerico | 050 |  |  |  |
| Chave de lançamento | CHAVE_LANCTO_C | CHAVE_LANCTO_C | Indica que o preenchimento é fixo com o valor '50' para transações de Crédito. | Numérico | 002 | Sim | Sim |  |
| Código de Custo | COD_CUSTO_C | Informar o Centro de Custo. O Código deve estar registrado na Tabela de Centro de Custos (SAFX2003). | Informar o Centro de Custo. O Código deve estar registrado na Tabela de Centro de Custos (SAFX2003). | Informar o Centro de Custo. O Código deve estar registrado na Tabela de Centro de Custos (SAFX2003). | Informar o Centro de Custo. O Código deve estar registrado na Tabela de Centro de Custos (SAFX2003). | Informar o Centro de Custo. O Código deve estar registrado na Tabela de Centro de Custos (SAFX2003). | Numérico | Numérico | Numérico | 020 |  |  |
| Descrição do Centro de Custo | DESCRICAO_CENTRO_CUSTO_C | DESCRICAO_CENTRO_CUSTO_C | Informar o Centro de Custo. A descrição do centro de custo deve estar registrada na Tabela de Centro de Custos (SAFX2003). | Alfanúmerico | 050 |  |  |  |
| Centro Lucro | CENTRO_LUCRO_C | CENTRO_LUCRO_C | Informar o Código do Centro de Custo. | Numérico | 020 |  |  |  |
| Texto Histórico | TEXTO_C | TEXTO_C | Informar o histórico da contabilização contábil | Alfanúmerico | 020 | Sim | Sim |  |
| Observações Lançamentos | OBSERVACAO_C | OBSERVACAO_C | Registrar a observação referente ao lançamento. | Alfanúmerico | 020 |  |  |  |
| Usuário | USUARIO | USUARIO | Informar o login do usuário responsável pela gravação dos dados. | Alfanúmerico | 014 |  |  |  |
| Data Início/Inclusão/Alteração. | DATA_PARAMETRO | DATA_PARAMETRO | Informar a Data Início/Inclusão/Alteração. | Numérico | 008 |  |  |  |


| Cód. | Descrição | ADO |
| --- | --- | --- |
| RN18 | Campo: Código Op. Apuração / F100 Regras de funcionamento Seleção do Imposto Ao selecionar o imposto "ICMS-Próprio", o sistema deve: Consultar a tabela OPERACAO_APURACAO e recuperar os valores dos campos COD_OPER_APUR e DSC_OPER_APUR. Para cada COD_OPER_APUR obtido na etapa anterior, o sistema deve considerar o COD_TIPO_LIVRO igual a 108 ou 165 Considerar os registros que serão utilizados para a parametrização de acordo com a conta informada pelo usuário, por exemplo: Concatenar os valores dos campos COD_OPER_APUR e DSC_OPER_APUR para preencher automaticamente o campo Código Op. Apuração / F100. Para usuário selecionar a opções desejada. | ADO 913117 |
| RN19 | Campo: Código Op. Apuração / F100 Regras de funcionamento Seleção do Imposto Ao selecionar o imposto "ICMS-ST", o sistema deve: Consultar a tabela OPERACAO_APURACAO e recuperar os valores dos campos COD_OPER_APUR e DSC_OPER_APUR. Para cada COD_OPER_APUR obtido na etapa anterior, o sistema deve considerar o COD_TIPO_LIVRO igual a 108 ou 165 Considerar os registros que serão utilizados para a parametrização de acordo com a conta informada pelo usuário, por exemplo: Concatenar os valores dos campos COD_OPER_APUR e DSC_OPER_APUR para preencher automaticamente o campo Código Op. Apuração / F100. Para usuário selecionar a opções desejada. |  |
| RN20 | Campo: Código Op. Apuração / F100 Regras de funcionamento Seleção do Imposto Ao selecionar o imposto "IPI", o sistema deve: Consultar a tabela OPERACAO_APURACAO e recuperar os valores dos campos COD_OPER_APUR e DSC_OPER_APUR. Para cada COD_OPER_APUR obtido na etapa anterior, o sistema deve considerar o COD_TIPO_LIVRO igual a 108 ou 165 Considerar os registros que serão utilizados para a parametrização de acordo com a conta informada pelo usuário, por exemplo: Concatenar os valores dos campos COD_OPER_APUR e DSC_OPER_APUR para preencher automaticamente o campo Código Op. Apuração / F100. Para usuário selecionar a opções desejada. |  |
| RN21 | Campo: Código Op. Apuração / F100 Regras de funcionamento Seleção do Imposto Ao selecionar o imposto "PIS", o sistema deve: Consultar a tabela OPERACAO_APURACAO e recuperar os valores dos campos COD_OPER_APUR e DSC_OPER_APUR. Para cada COD_OPER_APUR obtido na etapa anterior, o sistema deve considerar Considerar os registros que serão utilizados para a parametrização de acordo com a conta informada pelo usuário, por exemplo: Concatenar os valores dos campos COD_OPER_APUR e DSC_OPER_APUR para preencher automaticamente o campo Código Op. Apuração / F100. Para usuário selecionar a opções desejada. |  |
| RN22 | Campo: Código Op. Apuração / F100 Regras de funcionamento Seleção do Imposto Ao selecionar o imposto "COFINS", o sistema deve: Consultar a tabela OPERACAO_APURACAO e recuperar os valores dos campos COD_OPER_APUR e DSC_OPER_APUR. Para cada COD_OPER_APUR obtido na etapa anterior, o sistema deve considerar  Considerar os registros que serão utilizados para a parametrização de acordo com a conta informada pelo usuário, por exemplo: Concatenar os valores dos campos COD_OPER_APUR e DSC_OPER_APUR para preencher automaticamente o campo Código Op. Apuração / F100. Para usuário selecionar a opções desejada. |  |
| RN23 |  |  |
| RN24 |  |  |
| RN25 |  |  |
| RN26 |  |  |
| RN27 |  |  |
|  |  |  |


| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |


| RN01 | [ALTERADA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |
