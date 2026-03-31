# MTZ_Tela de Complemento de  Lançamentos Contábeis - Manual Diferença de valores

> Fonte: MTZ_Tela de Complemento de  Lançamentos Contábeis - Manual Diferença de valores.docx






THOMSON REUTERS

Matriz da tela Contabilização

Tela de Complemento de  Lançamentos Contábeis - Manual Diferença de valores



DOCUMENTO DE REQUISITO


Sumário

1.	INTRODUÇÃO	3
2.	Documento de Referência	3
3.	Fluxo Principal  – Tela de Complemento de  Lançamentos Contábeis - Manual Dif. de valores	3
4.	Prótotipo - Tela de Complemento de  Lançamentos Contábeis - Manual Diferença de valores	5
2.3	Funcionalidades:	6
2.4	Lista de campos:	6
2.5	Regra de botões:	11
5.	DDL criação de Tabela –  Complemento de  Lançamentos Contábeis - Manual Diferença de valores	14


## INTRODUÇÃO


O objetivo é desenvolver uma tela específica para lançamentos complementares, destinada à geração do JSON. Essa tela será utilizada para a contabilização de ajustes e outros lançamentos que exigem a inclusão de valores adicionais, permitindo ao usuário realizar a contabilização de forma adequada, sem depender dos valores provenientes das apurações de impostos.

## Documento de Referência


MTZ _Tela Seleção de dados
MTZ _ Tela de Parâmetros Ajustes da Apuração Contábeis
MTZ_Tela de Parâmetros de Outros Lançamentos Contábeis
MTZ_Tela de Geração Arquivo JSON
MTZ_Tela de Status
MTZ_Relatório de Status

## Fluxo Principal  – Tela de Complemento de  Lançamentos Contábeis - Manual Dif. de valores









Localização da Tela:


- Agrupamentos: Básico
- Módulo: Manutenção >> Contabilização Apuração >> Tela de Complemento de  Lançamentos Contábeis - Manual Diferença de valores
Menu: Acesso Principal >> Tela de Complemento de Lançamentos Contábeis - Manual Diferença de valores













## Prótotipo - Tela de Complemento de  Lançamentos Contábeis - Manual Diferença de valores




## Funcionalidades:

Acesso Direto: A plataforma disponibiliza tela dedicada que facilita a realização de lançamentos complementares diretamente pelo usuário.
Configuração de Parâmetros: É possível definir parâmetros cruciais para os lançamentos, incluindo tipos de ajustes, outros lançamentos datas e outros critérios relevantes.
Inserção de Valores Adicionais: O usuário pode inserir valores a necessários para a contabilização de ajustes e demais lançamentos.
Independência Fiscal: A realização dos lançamentos complementares ocorre sem depender dos valores provenientes de apurações fiscais.
Grava os dados: Os lançamentos efetuados são registrados pelo sistema, e os dados para integração em formato JSON, acessíveis através da tela de Geração do arquivo e envio através tela de Status.

## Lista de campos:




## Regra de botões:







## DDL criação de Tabela –  Complemento de Lançamentos Contábeis - Manual Diferença de valores

























| OS/CH | Nome | Descrição |
| --- | --- | --- |
| ADO - 966866 | Millys Lopes | Tela de Complemento de  Lançamentos Contábeis - Manual Diferença de valores |
| ADO 1031331 | Millys Lopes | Inclusão do Campo N |


| Documentação do Caso de Uso | Documentação do Caso de Uso |
| --- | --- |
| Ator Principal | Usuário do sistema |
| Pré- Condições | Ter configurado os Parâmetros necessários nas telas de Ajustes ou Outros Lançamentos. |  |
| Pós-Condições | O sistema utiliza os parâmetros configurados para facilitar e automatizar a gravação dos valores dos lançamentos complementares. |


| Ações do Ator | Ações do Sistema |
| --- | --- |
| Acesso a Tela | O usuário acessa a tela de lançamentos complementares através do menu principal do sistema. |
| Seleção de Informações | O usuário buscar dados dos parâmetros necessários para os lançamentos, o que pode incluir a seleção de tipos de ajustes, datas ou outros critérios relevantes. |
| Inserção de Valores | Insere os valores adicionais necessários para os lançamentos complementares de acordo com a conta e demais informações |
| Revisão e Salvamento dos Dados: | Após inserir os valores, revisa todos os dados inseridos e salva |
| Processamento pelo Sistema: | O sistema processa os lançamentos com base nos valores e parâmetros configurados e salva os dados para geração JSON na tela geração |


| Cód. | Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RN00 | Empresa | Campo | S | S | Default: selecionado | Visualizar a empresa selecionada no sistema Tax One | ADO - 966866 |
| RN01 | Estabecimento | Checkbox | S | S | Default: Não selecionado | Este campo permite ao usuário selecionar um ou mais estabelecimentos para realizar os lançamentos complementares. As opções exibidas incluem apenas os estabelecimentos vinculados ao login do usuário e que possuem cadastro ativo nos dados pertinentes. Informações Apresentadas: Cada estabelecimento será exibido na lista com as seguintes informações: Código do estabelecimento Razão social cadastrada O formato de exibição será apresentado da seguinte forma: XXX - XXXXXXXXXXXXXXXXX Caso o usuário opte por não selecionar nenhum estabelecimento específico, o sistema exibirá automaticamente a opção "Todos" os estabelecimentos disponíveis. | ADO - 966866 |
| RN02 | UF | Checkbox | Não | S | Default: Não selecionado | Seleção de UFs Este campo exibe as Unidades Federativas (UFs) dos estabelecimentos selecionados no campo RN01. O usuário pode selecionar uma ou mais UFs para realizar os lançamentos complementares. Caso nenhum estabelecimento seja selecionado no campo RN01, ou se o usuário desejar visualizar todos os estabelecimentos, o campo poderá ser preenchido com a opção "Todas UFs". Observação: O objetivo deste campo é facilitar a visualização e o ajuste de parâmetros fiscais por UF, considerando os estabelecimentos selecionados. | ADO - 966866 |
| RN03 | Divisão |  |  |  |  | O preenchimento deste campo deve ser realizado manualmente pelo usuário, permitindo a inserção de informações de forma livre, conforme necessário. As informações inseridas  são dadas  para o sistema SAP | ADO - 966866 |
| RN04 | Local de Negócio |  |  |  |  | O preenchimento deste campo deve ser realizado manualmente pelo usuário, permitindo a inserção de informações de forma livre, conforme necessário. As informações inseridas  são dadas  para o sistema SAP | ADO - 966866 |
| RN05 | Centro |  |  |  |  | O preenchimento deste campo deve ser realizado manualmente pelo usuário, permitindo a inserção de informações de forma livre, conforme necessário. As informações inseridas  são dadas  para o sistema SAP | ADO - 966866 |
| RN06 | Grupo Imposto | Dropdown | Sim | Sim | Default: Não preenchido | O sistema permite ao usuário selecionar, através de uma lista: Federal Estadual  Caso não selecionado exibir a seguinte mensagem: “Grupo Informar o preenchimento é de âmbito Federal ou Estadual” | ADO - 966866 |
| RN07 | Impostos | Dropdown | Sim | Sim |  | Este campo será apresentado apenas quando selecionado o “Grupo Imposto”  Caso selecionado “Federal” deverá listar os seguintes tributos: PIS/PASEP-Cumulativo PIS/PASEP-Não Cumulativo COFINS- Cumulativo COFINS-Não Cumulativo IPI Caso selecionado “Estadual” deverá listar os seguintes tributos: ICMS- Próprio ICMS-ST ICMS-Antecipado FCP DIFAL SCANC | ADO - 966866 |
| RN08 | Mês da Apuração | Campo | Sim | Sim | MM | O preenchimento deste campo deve ser realizado manualmente pelo usuário, permitindo a inserção de informações de forma livre, conforme necessário. | ADO - 966866 |
| RN09 | Ano da Apuração | Campo | Sim | Sim | AAAA | O preenchimento deste campo deve ser realizado manualmente pelo usuário, permitindo a inserção de informações de forma livre, conforme necessário. | ADO - 966866 |
| RN10 | Referência | Campo | Não | Não | Alfanumérico | O preenchimento deste campo deve ser realizado manualmente pelo usuário, permitindo a inserção de informações de forma livre, conforme necessário. As informações inseridas  são dadas  para o sistema SAP | ADO - 966866 |
| RN11 | Tipo de Parâmetro | Dropdown | Sim | Sim | Default: não selecionado | O sistema deve realizar uma busca nas informações registradas nas telas, com base nos campos especificados: Parâmetros de Ajustes da Apuração: Localizar e recuperar os dados relacionados aos parâmetros gravados por meio da tela Ajustes da Apuração na tabelaXXX(Em desenvolvimento) de ajustes da apuração, considerando os seguintes critérios: Empresa, Estabelecimento, Grupo de Imposto e Imposto selecionado. Outros Lançamentos da Apuração: Identificar e buscar as informações referentes a outros lançamentos, com base nos parâmetros gravados por meio da tela Ajustes da Apuração na tabelaXXX(Em Desenvolvimento), levando em conta os seguintes critérios: Empresa, Estabelecimento, Grupo de Imposto e Imposto selecionado. | ADO - 966866 |
| RN12 | Código de Ajustes | Dropdown | Sim | Sim | Númerico | Quando o campo Tipo de Parâmetro for definido como Ajustes da Apuração, o sistema deve apresentar no dropdown uma concatenação do Código de Ajustes com a Descrição, recuperando da Tela de Parâmetros Ajustes da Apuração  , exibindo apenas as opções que correspondem à Empresa, Estabelecimento, Grupo de Imposto e Imposto selecionados. Além disso, se o Tipo de Parâmetro for Ajustes da Apuração e nenhum Código de Ajustes for selecionado, o sistema deve exibir a mensagem de erro: "Selecione um código de ajustes para prosseguir." Por outro lado, quando o Tipo de Parâmetro for definido como Outros Lançamentos, o campo dropdown não deve carregar nenhuma opção. | ADO - 966866 |
| RN13 | Outros Lançamentos | Dropdown | Sim | Sim | Default: não selecionado | Quando o campo Tipo de Parâmetro for definido como Outros Lançamentos, o sistema deve apresentar, no dropdown, uma lista de Outros Lançamentos recuperando da Tela de Parâmetros Outros Lançamentos , exibindo apenas as opções que correspondem à Empresa, Estabelecimento, Grupo de Imposto e Imposto selecionados. Caso o Tipo de Parâmetro seja definido como Outros Lançamentos e nenhum Código seja selecionado, o sistema deverá exibir a seguinte mensagem de erro: "Selecione um código de Outros Lançamentos para prosseguir." Por outro lado, quando o Tipo de Parâmetro for definido como Ajustes da Apuração , o campo dropdown não deve carregar nenhuma opção. | ADO - 966866 |
| RN14 | Código  Op. Apuração. ou F100 | Dropdown | Sim | Sim | Default: não selecionado | Quando o campo Tipo de Parâmetro for definido como Outros Lançamentos, o sistema deve apresentar, no dropdown, uma lista de Código da Natureza ou os dados do F100 Lançamentos recuperando da Tela de Parâmetros Outros Lançamentos , exibindo apenas as opções que correspondem à Empresa, Estabelecimento, Grupo de Imposto e Imposto selecionados. Caso o Tipo de Parâmetro seja definido como Outros Lançamentos e nenhum Código seja selecionado, o sistema deverá exibir a seguinte mensagem de erro: "Selecione um código para prosseguir." Por outro lado, quando o Tipo de Parâmetro for definido como Ajustes da Apuração , o campo dropdown não deve carregar nenhuma opção. | ADO - 966866 |
| RN15 | Indicador da Conta | Dropdown | Sim | Sim | Default: não selecionado | Configuração do Dropdown: O sistema deve apresentar um menu dropdown que inicialmente não está selecionado. As opções disponíveis devem ser configuradas com base em critérios específicos, incluindo Empresa, Estabelecimento, Grupo de Imposto, Imposto, Tipo de Parâmetro selecionado, e as condições RN12 ou RN13 ou RN14. Filtragem de Códigos: Antes de apresentar as opções no dropdown, o sistema deve efetuar uma filtragem detalhada na busca e está filtragem assegura a inclusão apenas dos registros cujo IND_NATUREZA se enquadra nas categorias '1-Ativo', '2-Passivo', ou '3-Despesa'. Além disso, a filtragem deve ser realizada de forma alinhada com o Tipo de Parâmetro já selecionado, garantindo que as opções exibidas sejam pertinentes e adequadas à seleção do usuário. | ADO - 966866 |
| RN16 | Conta Contábil | Dropdown | Sim | Sim | Default: não selecionado | Permissão de Visualização: O sistema deve facilitar que o usuário visualize e selecione a conta contábil desejada. Esta funcionalidade é projetada para assegurar que a escolha seja realizada de maneira simples e intuitiva. Filtragem por Indicador da Conta: As contas contábeis devem ser recuperadas com base na seleção do usuário no campo "Indicador da conta". Por exemplo, se o indicador "1-Ativo" for selecionado, o sistema deve exibir no dropdown as contas correspondentes. As contas são apresentadas no formato Código da Conta concatenado com a Descrição, e a filtragem leva em consideração os seguintes critérios: Empresa, Estabelecimento, Grupo de Imposto, Imposto, Tipo de Parâmetro, Indicador da Conta, e as condições RN12 ou RN13, RN14. Validação de Campo: Se o campo 'Conta Contábil' estiver vazio ou se nenhuma conta for selecionada, o sistema deve exibir a mensagem de erro: "A conta contábil deve ser informada tanto para débito quanto para crédito." | ADO - 966866 |
| RN17 | Chave de Lançamento | campos | Sim | Sim | Default: selecionado | Chave de Lançamento: Criar os campos para apresentar as seguintes opções, permitindo a identificação do tipo de lançamento contábil: 40: Para informar a conta a Débito 50: Para informar a conta a crédito O usuário deverá parametrizar as informações conforme a chave adequada em cada campo, garantindo o correto registro do lançamento contábil. Tratamento: Caso o usuário tente preencher apenas o lançamento a débito e não preencha o lançamento a crédito ou vice e versa, o sistema deverá exibir uma mensagem de alerta informando o preenchimento. informações a débito e crédito é obrigatória para prosseguir. Mensagem sugerida: "É obrigatório lançamentos das informações a  crédito e a débito  para concluir a e salvar o lançamento. | ADO - 966866 |
| RN18 | Divisão | Campo | Não | Sim | Alfanúmerico | O preenchimento deste campo deve ser realizado manualmente pelo usuário, permitindo a inserção de informações de forma livre, conforme necessário. As informações inseridas são dadas do SAP | ADO - 966866 |
| RN19 | Local de Negócio | Campo | Não | Sim | Alfanúmerico | O preenchimento deste campo deve ser realizado manualmente pelo usuário, permitindo a inserção de informações de forma livre, conforme necessário. As informações inseridas  são dadas  para o sistema SAP | ADO - 966866 |
| RN20 | Centro | Campo | Não | Sim | Alfanúmerico | O preenchimento deste campo deve ser realizado manualmente pelo usuário, permitindo a inserção de informações de forma livre, conforme necessário. As informações inseridas  são dadas  para o sistema SAP | ADO - 966866 |
| RN21 | Centro de Custo | Campo | Não | Não | Numérico | O sistema deve recuperar os dados do Centro de Custo com base nos critérios selecionados pelo usuário, incluindo Empresa, Grupo de Imposto, Imposto, Tipo de Parâmetro e Conta Contábil. | ADO - 966866 |
| RN22 | Centro de Lucro | Campo | Não | Sim | Numérico | O sistema deve recuperar os dados do Centro de Custo com base nos critérios selecionados pelo usuário, incluindo Empresa, Grupo de Imposto, Imposto, Tipo de Parâmetro e Conta Contábil. | ADO - 966866 |
| RN23 | Digite o Valor | Campo | Sim | Sim |  | O preenchimento deste campo deve ser realizado manualmente pelo usuário, permitindo a inserção de informações de forma livre, conforme necessário tanto para débito e crédito. | ADO - 966866 |
| RN24 | Texto -Histórico |  | Não |  | Alfanúmerico | O preenchimento deste campo deve ser realizado manualmente pelo usuário, permitindo a inserção de informações de forma livre, conforme necessário. As informações inseridas  são dadas  para o sistema SAP | ADO - 966866 |
| RN25 | Observação Lançamentos |  | Não |  | Alfanúmerico | O preenchimento deste campo deve ser realizado manualmente pelo usuário, permitindo a inserção de informações de forma livre, conforme necessário. As informações inseridas  são dadas  para o sistema SAP | ADO - 966866 |
| RN26 | Número Documento Contábil | Campo | Sim |  | Default: selecionado | O campo “Número de Documento Contábil” Número de Documento Contábil será executado na Tela, considerando os filtros selecionados pelo usuário. Filtros obrigatórios para consulta (SAFX 347) A recuperação do número deve considerar todos os filtros abaixo, conforme selecionados na tela: Empresa ,Estabelecimento, Grupo de Imposto, Imposto , Mês da Apuração, Ano da Apuração, Tipo do Parâmetro, Código de Ajustes ou Outros Lançamentos Atenção: O sistema deve impedir que o usuário prossiga com o Lançamento Complementar caso o campo Número de Documento Contábil: Não exista; Não seja retornado pela SAFX nº 347; Esteja vazio ou nulo; Não atenda aos filtros selecionados. Se NRO_DOC_CONTABIL existe → campo é preenchido automaticamente e o usuário pode seguir com o lançamento. Se NRO_DOC_CONTABIL não existe → exibir erro e impedir qualquer avanço. Mensagem de Erro “O Lançamento Complementar só poderá ser realizado se houver Número de Documento Contábil. Por favor, verifique se existe lançamento contábil para o período informado e para os Ajustes ou Outros Lançamentos selecionados | ADO 1031331 |


| Cód. | NOME | Tipo | Obrig | Ed | Formato/Default |  | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Salvar | Botão | _ | - | _ |  | Função: Registra no sistema as informações preenchidas ou alteradas pelo usuário.  Valida todos os campos obrigatórios e as regras de negócio antes de gravar. Caso haja erro, exibe mensagem indicando o campo a ser corrigido. Ao sucesso, grava os dados no banco, registra usuário e data/hora, e exibe mensagem de confirmação. Atualiza imediatamente as listas e relatórios na tela. Após salvar, o formulário pode ser limpo automaticamente ou permanecer preenchido, conforme configuração do sistema. | ADO - 966866 |
|  | Limpar | Botão | _ | _ | _ |  | Função: Limpa todos os campos do formulário, permitindo ao usuário iniciar um novo preenchimento. Ao clicar em Limpar, todos os campos do formulário de parametrização retornam ao estado inicial (em branco ou valor default). Não afeta os dados já salvos no banco de dados; apenas limpa o formulário atual. Exibe mensagem de confirmação caso haja dados não salvos no formulário (opcional). | ADO - 966866 |
|  | Editar | Botão | _ | _ | _ |  | Função: Permite ao usuário alterar os dados de uma parametrização já existente. O usuário deve selecionar um registro existente na lista para habilitar o botão Editar. Ao clicar em Editar, os campos do registro selecionado ficam habilitados para alteração. Após editar, o usuário deve clicar em Salvar para registrar as alterações. Se cancelar ou sair sem salvar, as alterações não são gravadas. O sistema registra usuário, data e hora da última alteração. | ADO - 966866 |
|  | Excluir | Botão |  |  |  |  | Função: Permite ao usuário remover definitivamente uma parametrização existente. Regras: O usuário deve selecionar um registro existente na lista para habilitar o botão Excluir. Ao clicar em Excluir, o sistema solicita confirmação antes de remover o registro (exemplo: “Deseja realmente excluir esta parametrização?”). Ao confirmar, o sistema remove o registro do banco de dados e atualiza a lista. O sistema registra o usuário, data e hora da exclusão para auditoria. Não é possível desfazer a exclusão após confirmação. | ADO - 966866 |
|  | Pesquisar | Botão |  |  |  |  | Este campo permite ao usuário realizar pesquisas em parâmetros previamente cadastrados, utilizando os seguintes critérios: Empresa Estabelecimento UF (Unidade Federativa) Código do Ajuste | ADO - 966866 |


| CAMPO | NOME | COMENTARIO | TIPO | TAMANHO | OBRIG | CHAVE |
| --- | --- | --- | --- | --- | --- | --- |
| Código da Empresa | COD_EMPRESA | Campo destinado ao código da Empresa. Vide regra RN00 | Alfanúmerico | 003 | Sim | (*) |
| Código do Estabecimento | COD_ESTABELECIMENTO | Campo destinado ao código do Estabelecimento. Vide regra RN01 | Alfanúmerico | 006 | Sim | (*) |
| UF | UF | Informar a sigla da Unidade Federativa (UF) correspondente ao estabelecimento. | Texto | 002 |  |  |
| Grupo de Imposto | GRUPO_IMPOSTO | Informar o preenchimento é de âmbito Federal ou Estadual. Vide regra RN03 | Texto | 10 | Sim | (*) |
| Imposto | IMPOSTO | Informar o preenchimento do imposto atrelado ao âmbito Federal ou Estadual. Vide regra RN04 | Texto | 030 | Sim | (*) |
| Local de Negócio | LOCAL_NEGÓCIO | O Preenchimento é livre indica o código correspondente a um estabelecimento dentro da matriz no sistema SAP. | Alfanúmerico | 004 |  |  |
| Divisão | DIVISÃO | O Preenchimento é livre indica a segregação financeira de um segmento específico dentro do sistema SAP. | Alfanúmerico | 004 |  |  |
| Centro | Centro | O Preenchimento é livre indica a segregação SAP | Alfanúmerico | 004 |  |  |
| Periodo (Mês) | MES | Informa o mês correspondente apuração | MM | 02 | Sim |  |
| Periodo (Ano) | EXERCICIO | Informa o Ano da Apuração | AAAA | 04 | Sim |  |
| Código de Ajuste | COD_AJUSTE | Informar o código de ajuste conforme a apuração dos tributos ICMS, ICMS-Antecipado, ICMS-ST, IPI, DIFAL, FCP e SCANC, PIS e COFINS. Vide regra RN06 | Alfanúmerico | 15 | Sim | (*) |
| Descrição do Ajuste | DESCRICAO_AJUSTE | Informar a descrição dos ajustes realizados nas apurações de ICMS, ICMS-Antecipado, ICMS-ST, IPI, DIFAL, FCP e SCANC, PIS e COFINS. Vide regra | Texto | 050 | Sim |  |
| Chave de lançamento | CHAVE_LANCTO_D | Indica que o preenchimento é fixo com o valor '40' para transações de débito. | Númerico | 002 | Sim |  |
| Conta Contábil Débito | COD_CONTA_D | Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas (SAFX retorno xxxx). | Númerico | 070 | Sim |  |
| Descrição da Conta | DESCRICAO_CONTA_D | Informar a Descrição da Conta existente na SAFXde retorno | Alfanúmerico | 050 |  |  |
| Centro Custo | CENTRO_CUSTO_D | Informar o Centro de Custo. O Código deve estar registrado na Tabela de Centro de Custos (SAFX2003). | Numérico | 020 |  |  |
| Descrição do Centro de Custo | DESCRICAO_CENTRO_CUSTO_D | Informar o Centro de Custo. A descrição do centro de custo deve estar registrada na Tabela de Centro de Custos (SAFX Retorno). |  |  |  |  |
| Valor do Complemento_D | MONTANTE_D | Informa o valor do lançamento contábil a débito recuperado da SAFX de Retorno após conversão da RN | Numérico | 011V002 |  |  |
| Centro Lucro | CENTRO_LUCRO_D | O preenchimento é livre e informar o código do centro de lucros, utilizado para alocar receitas ou despesas de forma similar ao centro de custo. Este campo é opcional e serve apenas para controle interno. | Numérico | 020 |  |  |
| Texto Histórico | TEXTO_D | Informar o histórico da contabilização contábil | Alfanúmerico | 020 | Sim |  |
| Observações de Lançamentos | OBSERVAÇÃO_D | Registrar a observação referente ao lançamento. | Alfanúmerico | 020 |  |  |
| Chave de lançamento | CHAVE_LANCTO_C | Indica que o preenchimento é fixo com o valor '40' para transações de débito. | Númerico | 002 | Sim |  |
| Conta Contábil Débito | COD_CONTA_C | Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas (SAFX2002). | Númerico | 070 | Sim |  |
| Descrição da Conta | DESCRICAO_CONTA_C | Informar a Descrição da Conta existente na SAFX2002 | Alfanúmerico | 050 |  |  |
| Centro Custo | CENTRO_CUSTO_C | Informar o Centro de Custo. O Código deve estar registrado na Tabela de Centro de Custos (SAFX2003). | Numérico | 020 |  |  |
| Descrição do Centro de Custo | DESCRICAO_CENTRO_CUSTO_C | Informar o Centro de Custo. A descrição do centro de custo deve estar registrada na Tabela de Centro de Custos (SAFX2003). |  |  |  |  |
| Centro Lucro | CENTRO_LUCRO_C | O preenchimento é livre e informar o código do centro de lucros, utilizado para alocar receitas ou despesas de forma similar ao centro de custo. Este campo é opcional e serve apenas para controle interno. | Numérico | 020 |  |  |
| Valor do Complemento_C | MONTANTE_C | Informa o valor do lançamento contábil a débito recuperado da SAFX de Retorno após conversão da RN | Numérico | 011V002 | sim |  |
| Texto Histórico | TEXTO_C | Informar o histórico da contabilização contábil | Alfanúmerico | 020 | Sim |  |
| Observações de Lançamentos | OBSERVAÇÃO_C | Registrar a observação referente ao lançamento. | Alfanúmerico | 020 |  |  |
| Usuário | USUARIO | Informar o login do usuário responsável pela gravação dos dados. | Alfanúmerico | 014 |  |  |
| Data da gravação do  Complemento Contábil | DATA_ COMPLEMENTO_CONTABIL | Descrição: Este campo deve ser preenchido com a data de criação do estorno. Ele indica que, para a data, mês e ano da apuração selecionada, o usuário possui um arquivo disponível para o estorno. | Numérico | 008 |  |  |
| Indicador de Complemento de Lançamento Contábil | ID_COMPLEMENTO_CONTABIL | O campo ID_ESTORNO é utilizado para identificar de forma única o complemento associado a um arquivo ou operação específica. Este identificador será usado para vincular os dados relacionados ao complemento na geração e manipulação dos arquivos. Para um Complemento realizado em outubro de 2025, o identificador pode ser algo como: 10252001, onde os primeiros dígitos correspondem ao mês e ano, seguidos por um número sequencial único. | Numérico |  |  |  |
