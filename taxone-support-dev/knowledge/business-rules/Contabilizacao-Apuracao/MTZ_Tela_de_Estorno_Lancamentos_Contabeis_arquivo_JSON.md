---
source: "MTZ_Tela de Estorno – Lançamentos Contábeis arquivo JSON.docx"
category: Contabilização -Apuração
converted: auto
---





THOMSON REUTERS

Matriz da tela Contabilização

Tela de Estorno – Lançamentos Contábeis arquivo JSON


DOCUMENTO DE REQUISITO


Sumário

**1.	Introdução	3**
2.	Documento de Referência	3
3.	Fluxo Principal Seleção de dados:	3
2.1	Prótotipo Tela Estorno:	4
2.3	Funcionalidades:	5
4..1.	Parâmetros para criar o estorno:	5
4..2.	Gravação das informações na Tabela para geração do JSON:	10


# Introdução
O estorno é uma operação contábil utilizada para corrigir ou anular um lançamento anterior que tenha sido registrado de forma inadequada ou que precise ser ajustado. Essa correção é feita por meio de um lançamento inverso, onde os valores originalmente lançados são revertidos:
# Documento de Referência

MTZ_SAFX----Retorno
MTZ_Tela Geração
MTZ_Tela de Status
MTZ_Relatório de Status


# Fluxo Principal Seleção de dados:

Este caso de uso descreve o processo para a geração de arquivos – Lançamentos Contábeis










**Localização da Tela:**

- Agrupamentos: Básico
- Módulo: Manutenção >> Contabilização Apuração >> Tela de Estorno – Lançamentos Contábeis arquivo JSON
- Menu: Acesso Principal >> Tela de Estorno







# Prótotipo Tela Estorno:




# Funcionalidades:

Acesso Direto: A plataforma oferece uma tela dedicada exclusivamente para realização de estornos sobre os impostos ICMS, ICMS-ST, DIFAL,FCP, PIS/COFINS, SCANC
Condição para Estorno: Os estornos só poderão ser realizados mediante a apresentação de um Número de Documento Contábil válido.
Processo de Estorno:
Confirmação de Dados: Após visualizar e confirmar os dados do estorno, o usuário poderá proceder à tela de geração para criar o arquivo necessário.
Cancelamento de Estorno: O cancelamento de um estorno pode ser realizado na tela de Status, especificamente quando o status "Estorno Gerado" estiver ativo. Caso o status seja "Estorno Enviado", o cancelamento não será possível.
Relatório de Status: Os detalhes dos estornos realizados podem ser consultados através de um relatório de status disponível em formato Excel.
# Parâmetros para criar o estorno:







# Gravação das informações na Tabela para geração do JSON:
Tabela


























---

| OS/CH | Nome | Descrição |
| --- | --- | --- |
| ADO 796894 | Millys Lopes | Tela de Estorno – Lançamentos Contábeis arquivo JSON |
|  |  |  |


---

| Documentação do Caso de Uso | Documentação do Caso de Uso |
| --- | --- |
| Ator Principal | Usuário do sistema |
| Pré- Condições | O usuário deve realizar a contabilização no ERP para o retorno do número do documento contábil para criação do estorno. |
| Pós-Condições | O sistema registra e salva os dados necessários para a execução do estorno. |


---

| Ações do Ator | Ações do Sistema |
| --- | --- |
| O usuário acessa a tela. | O sistema exibe o menu principal com as opções disponíveis, incluindo "Parâmetros" e "Número do Documento Contábil" para facilitar a busca. |
| O usuário visualiza os dados dos lançamentos contábeis. | O sistema mostra os detalhes dos lançamentos, incluindo "Conta Crédito (Reversão do Débito do Lançamento Original)" e "Conta Débito (Reversão do Crédito do Lançamento Original)". |
| O usuário clica no botão "Salvar". | O sistema grava os lançamentos contábeis para o estorno. |


---

| Cód. | Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RN00 | Empresa | Campo | S | S | Default: selecionado | Visualizar a empresa selecionada no sistema Tax One | ADO 796894 |
| RN01 | Estabecimento | Checkbox | S | S | Default: Não selecionado | Este campo permite ao usuário selecionar um ou mais estabelecimentos para realizar os lançamentos complementares. As opções exibidas incluem apenas os estabelecimentos vinculados ao login do usuário e que possuem cadastro ativo nos dados pertinentes. Informações Apresentadas: Cada estabelecimento será exibido na lista com as seguintes informações: Código do estabelecimento Razão social cadastrada O formato de exibição será apresentado da seguinte forma: XXX - XXXXXXXXXXXXXXXXX Caso o usuário opte por não selecionar nenhum estabelecimento específico, o sistema exibirá automaticamente a opção "Todos" os estabelecimentos disponíveis. | ADO 796894 |
| RN02 | UF | Checkbox | Não | S | Default: Não selecionado | Seleção de Unidades Federativas (UFs) Este campo exibe as Unidades Federativas (UFs) dos estabelecimentos selecionados no campo RN01. O usuário pode selecionar Uma ou Mais UFs. | ADO 796894 |
| RN03 | Grupo Imposto | Dropdown | Sim | Sim | Default: Não preenchido | O sistema permite ao usuário selecionar, através de uma lista: Federal Estadual  Caso não selecionado exibir a seguinte mensagem: “Grupo Informar o preenchimento é de âmbito Federal ou Estadual” | ADO 796894 |
| RN04 | Impostos | Dropdown | Sim | Sim |  | Com base na seleção realizada no grupo de impostos e conforme os critérios de Empresa, estabelecimento e UF, o sistema busca na SAFX de Retorno XXX o campo 'Imposto' e o exibe para que o usuário possa fazer sua escolha | ADO 796894 |
| RN05 | Periodo | Campo | Sim | Sim | MM/AAAA | O sistema deve permitir que o usuário defina o mês e o exercício correspondente à apuração, no formato mês/ano, para realizar a busca na SAFX de Retorno. A busca deve considerar os campos 'Mês' e 'Exercício', bem como os critérios selecionados anteriormente nos campos, incluindo Empresa, Estabelecimento, UF, Grupo de Imposto e Imposto. Caso não sejam encontrados dados para o período solicitado, o sistema deve exibir uma mensagem de erro informando “A ausência de dados disponíveis para estorno no período especificado, selecione novo período”. | ADO 796894 |
| RN07 | Local de Negócio | Dropdown |  |  | Default: Não selecionado | Buscar no SAFX de retorno XXXX o campo LOCAL_Negócio, utilizando os parâmetros selecionados (Empresa, Estabelecimento, UF, Grupo de Imposto, Imposto, Período), para exibir o Local de Negócio na lista e permitir que o usuário faça sua seleção caso existente. Este campo não é obrigatório, podendo ou não conter dados disponíveis para o usuário. | ADO 796894 |
| RN08 | Divisão | Dropdown |  |  | Default: Não selecionado | Buscar no SAFX de retorno XXXX o campo DIVISAO, utilizando os parâmetros selecionados (Empresa, Estabelecimento, UF, Grupo de Imposto, Imposto, Período), para exibir a Divisao na lista e permitir que o usuário faça sua seleção caso existente. Este campo não é obrigatório, podendo ou não conter dados disponíveis para o usuário. | ADO 796894 |
| RN09 | Centro | Dropdown |  |  | Default: Não selecionado | Buscar no SAFX de retorno XXXX o campo Centro, utilizando os parâmetros selecionados (Empresa, Estabelecimento, UF, Grupo de Imposto, Imposto, Período), para exibir a Centro na lista e permitir que o usuário faça sua seleção caso existente. Este campo não é obrigatório, podendo ou não conter dados disponíveis para o usuário. | ADO 796894 |
| RN10 | Nº Documento Contábil | Dropdown | Sim | Sim | Default: Não selecionado | Buscar na SAFX de retorno o campo NRO_DOC, utilizando as pré-seleções realizadas (Empresa, Estabelecimento, UF, Grupo de Imposto, Imposto, Período, Local de Negócio, Divisão e Centro). O sistema deve exibir na lista os números de documentos disponíveis para seleção. Caso haja múltiplos números de documentos, o usuário deverá selecionar apenas um por vez para proceder com o estorno. Uma mensagem 'Selecione um documento para seguir com o estorno' será exibida para orientar o usuário. | ADO 796894 |
|  | Código de Ajustes | Dropdown |  |  | Default: selecionado | Este campo será carregado automaticamente com base no campo 'Nº Documento Contábil' preenchido. Se este campo for preenchido automaticamente, os campos 'Outros lançamentos' e 'Código da Natureza OP. ou F100' não poderão ser preenchidos. | ADO 796894 |
| RN11 | Outros Lançamentos | Dropdown |  |  | Default: selecionado | Este campo será carregado automaticamente com base no 'Nº Documento Contábil' preenchido. Caso este campo seja preenchido automaticamente, o campo 'Código de Ajustes' não poderá ser preenchido. | ADO 796894 |
| RN12 | Código da Natureza  OP. ou F100 | Dropdown |  |  | Default: selecionado | Este campo será carregado automaticamente com base no 'Nº Documento Contábil' preenchido. Caso este campo seja preenchido automaticamente, o campo 'Código de Ajustes' não poderá ser preenchido. | ADO 796894 |
| RN13 | Chave de Lançamento |  |  |  | Default: selecionado | A Chave de Lançamento será automaticamente carregada com base no 'Número de Documento Contábil'. As alterações nos campos ocorrerão automaticamente conforme as seguintes regras: No campo 'CHAVE_LANCTO 40' da SAFX de retorno, que registra a conta a débito ('Conta Débito - Reversão do Crédito do Lançamento Original'), a chave será alterada para 50. No campo 'CHAVE_LANCTO 50' da SAFX de retorno, que registra a conta a crédito ('Conta Crédito - Reversão do Débito do Lançamento Original'), a chave será alterada para 40. Exemplo: Se no arquivo original SAFX de Retorno a 'CHAVE_LANCTO' é 40, no arquivo de estorno, ela será alterada para 50." | ADO 796894 |
| RN14 | Conta Contábil | campos | Sim | Sim | Default: selecionado | A conta contábil será carregada automaticamente com base no 'Número de Documento Contábil'. As alterações nos campos serão ajustadas automaticamente conforme as regras descritas abaixo: No campo 'Conta_D' da SAFX de Retorno, destinado a informar a conta a débito ('Conta Débito - Reversão do Crédito do Lançamento Original'), a designação da conta será alterada para 'CONTA_C', mantendo o conteúdo original e ajustando apenas a classificação da conta. No campo 'Conta_C' da SAFX de Retorno, destinado a informar a conta a crédito ('Conta Crédito - Reversão do Débito do Lançamento Original'), a designação da conta será alterada para 'CONTA_D', mantendo o conteúdo original e ajustando apenas a classificação da conta. Exemplo de aplicação: Se no ERP foi contabilizado com 'CONTA_D' 6300336 e 'CONTA_C' 6300337, para efetuar o estorno, os registros seriam ajustados para 'CONTA_C' 6300336 e 'CONTA_D' 6300337." | ADO 796894 |
| RN15 | Centro de Custo | Campo | Não | Não | Default: selecionado | O Centro de Custo será carregado automaticamente com base no 'Número de Documento Contábil'. As alterações nos campos serão ajustadas automaticamente conforme as regras descritas abaixo: No campo 'Centro de Custo' da SAFX de Retorno, destinado a registrar a conta a débito ('Conta Débito - Reversão do Crédito do Lançamento Original'), a designação da conta será alterada para 'CONTA_C', mantendo o conteúdo original e ajustando apenas a classificação da conta. No campo 'CENTRO_CUSTO' da SAFX de Retorno, destinado a registrar a conta a crédito ('Conta Crédito - Reversão do Débito do Lançamento Original'), a designação do centro de custo será alterada para 'CENTRO CUSTO', mantendo o conteúdo original e ajustando apenas a classificação do centro de custo. Exemplo de aplicação: Se no ERP foi contabilizado com: 'CONTA_D' = 6300336 e 'CENTRO_CUSTO' = 99999 'CONTA_C' = 6300337 e 'CENTRO_CUSTO' = 9998 Para efetuar o estorno, os registros seriam ajustados para: 'CONTA_C' = 6300336 e 'CENTRO_CUSTO' = 99999 'CONTA_D' = 6300337 e 'CENTRO_CUSTO' = 9998." | ADO 796894 |
| RN16 | Centro de Lucro | Campo | Não | Sim | Default: selecionado | O Centro de Lucro será carregado automaticamente com base no 'Número de Documento Contábil'. As alterações nos campos serão ajustadas automaticamente conforme as regras descritas abaixo: •No campo Centro de Lucro da SAFX de Retorno, destinado a registrar a conta a débito ('Conta Débito - Reversão do Crédito do Lançamento Original'), a designação da conta será alterada para 'CONTA_C', mantendo o conteúdo original e ajustando apenas a classificação da conta. •No campo 'CENTRO_LUCRO' da SAFX de Retorno, destinado a registrar a conta a crédito ('Conta Crédito - Reversão do Débito do Lançamento Original'), a designação do centro de custo será alterada para 'CENTRO CUSTO', mantendo o conteúdo original e ajustando apenas a classificação do centro de custo. Exemplo de aplicação: Se no ERP foi contabilizado com: •'CONTA_D' = 6300336 e 'CENTRO_CUSTO' = 99999 e CENTRO_LUCRO= 1111 •'CONTA_C' = 6300337 e 'CENTRO_CUSTO' = 9998 e CENTRO_LUCRO= 1112 Para efetuar o estorno, os registros seriam ajustados para: •'CONTA_C' = 6300336 e 'CENTRO_CUSTO' = 99999 e CENTRO_LUCRO= 1111 •'CONTA_D' = 6300337 e 'CENTRO_CUSTO' = 9998." e CENTRO_LUCRO= 1112. | ADO 796894 |
| RN17 | Valor | Campo | Sim | Sim | Default: selecionado | O CAMPO Valor será carregado automaticamente com base no 'Número de Documento Contábil'. As alterações nos campos serão ajustadas automaticamente conforme as regras descritas abaixo: No campo MONTANTE da SAFX de Retorno, destinado a registrar o valor da conta a débito ('Conta Débito - Reversão do Crédito do Lançamento Original'), a classificação da conta será alterada para 'CONTA_C', mantendo o conteúdo original e ajustando apenas a classificação da conta. No campo MONTANTE da SAFX de Retorno, destinado a registrar o valor da conta a crédito ('Conta Crédito - Reversão do Débito do Lançamento Original'), a classificação será ajustada conforme a regra de reversão, mantendo o conteúdo original. Exemplo de aplicação: Se no ERP foi contabilizado com: 'CONTA_D' = 6300336, 'CENTRO_CUSTO' = 99999, 'CENTRO_LUCRO' = 1111 e MONTANTE = 250,00 'CONTA_C' = 6300337, 'CENTRO_CUSTO' = 9998, 'CENTRO_LUCRO' = 1112 e MONTANTE = 250,00 Para efetuar o estorno, os registros seriam ajustados para: 'CONTA_C' = 6300336, 'CENTRO_CUSTO' = 99999, 'CENTRO_LUCRO' = 1111 e MONTANTE = 250,00 'CONTA_D' = 6300337, 'CENTRO_CUSTO' = 9998, 'CENTRO_LUCRO' = 1112 e MONTANTE = 250,00 | ADO 796894 |
| RN18 | Texto -Histórico |  | Não |  | Alfanúmerico | O preenchimento deste campo deve ser realizado manualmente pelo usuário, permitindo a inserção de informações de forma livre, conforme necessário. As informações inseridas  são dadas  para o sistema SAP | ADO 796894 |
| RN19 | Observação Lançamentos |  | Não |  | Alfanúmerico | O preenchimento deste campo deve ser realizado manualmente pelo usuário, permitindo a inserção de informações de forma livre, conforme necessário. As informações inseridas  são dadas  para o sistema SAP | ADO 796894 |


---

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
| Número de documento Contábil | NRO_DOC | Informa o Número Documento criado no SAP | Númerico | 10 |  |  |
| Código de Ajuste | COD_AJUSTE | Informar o código de ajuste conforme a apuração dos tributos ICMS, ICMS-Antecipado, ICMS-ST, IPI, DIFAL, FCP e SCANC, PIS e COFINS. Vide regra RN06 | Alfanúmerico | 15 | Sim | (*) |
| Descrição do Ajuste | DESCRICAO_AJUSTE | Informar a descrição dos ajustes realizados nas apurações de ICMS, ICMS-Antecipado, ICMS-ST, IPI, DIFAL, FCP e SCANC, PIS e COFINS. Vide regra | Texto | 050 | Sim |  |
| Chave de lançamento | CHAVE_LANCTO_D | Indica que o preenchimento é fixo com o valor '40' para transações de débito. | Númerico | 002 | Sim |  |
| Conta Contábil Débito | COD_CONTA_D | Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas (SAFX retorno xxxx). | Númerico | 070 | Sim |  |
| Descrição da Conta | DESCRICAO_CONTA_D | Informar a Descrição da Conta existente na SAFXde retorno | Alfanúmerico | 050 |  |  |
| Centro Custo | CENTRO_CUSTO_D | Informar o Centro de Custo. O Código deve estar registrado na Tabela de Centro de Custos (SAFX2003). | Numérico | 020 |  |  |
| Descrição do Centro de Custo | DESCRICAO_CENTRO_CUSTO_D | Informar o Centro de Custo. A descrição do centro de custo deve estar registrada na Tabela de Centro de Custos (SAFX Retorno). |  |  |  |  |
| Valor_D | MONTANTE_D | Informa o valor do lançamento contábil a débito recuperado da SAFX de Retorno após conversão da RN | Numérico | 011V002 |  |  |
| Centro Lucro | CENTRO_LUCRO_D | O preenchimento é livre e informar o código do centro de lucros, utilizado para alocar receitas ou despesas de forma similar ao centro de custo. Este campo é opcional e serve apenas para controle interno. | Numérico | 020 |  |  |
| Texto Histórico | TEXTO_D | Informar o histórico da contabilização contábil | Alfanúmerico | 020 | Sim |  |
| Observações de Lançamentos | OBSERVAÇÃO_D | Registrar a observação referente ao lançamento. | Alfanúmerico | 020 |  |  |
| Chave de lançamento | CHAVE_LANCTO_C | Indica que o preenchimento é fixo com o valor '40' para transações de débito. | Númerico | 002 | Sim |  |
| Conta Contábil Débito | COD_CONTA_C | Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas (SAFX2002). | Númerico | 070 | Sim |  |
| Descrição da Conta | DESCRICAO_CONTA_C | Informar a Descrição da Conta existente na SAFX2002 | Alfanúmerico | 050 |  |  |
| Centro Custo | CENTRO_CUSTO_C | Informar o Centro de Custo. O Código deve estar registrado na Tabela de Centro de Custos (SAFX2003). | Numérico | 020 |  |  |
| Descrição do Centro de Custo | DESCRICAO_CENTRO_CUSTO_C | Informar o Centro de Custo. A descrição do centro de custo deve estar registrada na Tabela de Centro de Custos (SAFX2003). |  |  |  |  |
| Centro Lucro | CENTRO_LUCRO_C | O preenchimento é livre e informar o código do centro de lucros, utilizado para alocar receitas ou despesas de forma similar ao centro de custo. Este campo é opcional e serve apenas para controle interno. | Numérico | 020 |  |  |
| Valor_C | MONTANTE_C | Informa o valor do lançamento contábil a débito recuperado da SAFX de Retorno após conversão da RN | Numérico | 011V002 | sim |  |
| Texto Histórico | TEXTO_C | Informar o histórico da contabilização contábil | Alfanúmerico | 020 | Sim |  |
| Observações de Lançamentos | OBSERVAÇÃO_C | Registrar a observação referente ao lançamento. | Alfanúmerico | 020 |  |  |
| Usuário | USUARIO | Informar o login do usuário responsável pela gravação dos dados. | Alfanúmerico | 014 |  |  |
| Data da gravação do Estorno | DATA_ESTORNO | Descrição: Este campo deve ser preenchido com a data de criação do estorno. Ele indica que, para a data, mês e ano da apuração selecionada, o usuário possui um arquivo disponível para o estorno. | Numérico | 008 |  |  |
| Indicador de Estorno | ID_Estorno | O campo ID_ESTORNO é utilizado para identificar de forma única o estorno associado a um arquivo ou operação específica. Este identificador será usado para vincular os dados relacionados ao estorno na geração e manipulação dos arquivos. Para um estorno realizado em outubro de 2025, o identificador pode ser algo como: 10252001, onde os primeiros dígitos correspondem ao mês e ano, seguidos por um número sequencial único. | Numérico |  |  |  |
