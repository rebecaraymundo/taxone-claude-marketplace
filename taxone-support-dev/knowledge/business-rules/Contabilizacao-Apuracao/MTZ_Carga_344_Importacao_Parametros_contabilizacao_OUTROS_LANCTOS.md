---
source: "MTZ_Carga_344_Importacao_Parametros_contabilizaçao_OUTROS_LANCTOS.docx"
category: Contabilização -Apuração
converted: auto
---





THOMSON REUTERS


TAX PAYMENTS – IMPORTAÇÃO - SAFX344 (Integração de Contabilização – Parâmetros – Outros Lançamentos da Apuração)
TAXONE >> Básicos > Data Warehouse > Manutenção > Contabilização Apuração >>Seleção de Dados/ Parâmetros >> Paramentos de Outros Lançamentos

DOCUMENTO DE REQUISITO



# Introdução

Implantar uma interface de parametrização dos "Outros Lançamentos da Apuração", destinada a configurar, de forma simples e segura, os códigos de outros lançamentos contábeis e sua vinculação às contas contábeis. O objetivo é permitir que o usuário selecione empresa/estabelecimento/UF, defina o grupo de imposto (Federal ou Estadual) e escolha tributos como ICMS (próprio, ST, antecipado, FCP, DIFAL, SCANC), IPI e PIS/COFINS, aplicando automaticamente as regras de negócio correspondentes para garantir consistência dos dados


**Localização:**
**Agrupamentos: Básico >> Job Servidor**
Menu: Carga > Programação > Execução
Importação > Programação > Execução
Importação batch > Programação > Execução

**(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX344 conforme o Manual de Layout, o que facilita a consulta. Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00).**

Procedimentos para a Importação da SAFX344:

A importação da SAFX344 deve seguir as seguintes premissas de negócio e comportamentos:
- Layout e fontes de dados: o arquivo deve obedecer ao Manual de Layout SAFX(inserir número) e às estruturas de referência utilizadas pelo sistema: SAFX2002 (Plano de Contas), SAFX2003 (Centro de Custo), SAFX2006 (Natureza da Operação) e SAFX147 (Operação de Crédito).

**Resultado da Importação:**
Caso a importação seja realizada com sucesso, os dados serão preenchidos nas seguintes telas:
**Módulo: Manutenção >> Contabilização Apuração >>Seleção de Dados/ Parâmetros >> Paramentos de Outros Lançamentos**
**Menu: Acesso Principal >> Parâmetros**




Regra Geral para validação

1º ) Consistências Básicas:

Campos Data inválidos
Campos Obrigatórios
Campos Numéricos inválidos
Campo Grupo de Imposto -Vide regra RN 05
Campo Imposto – Vide regra RN 06
Campo Outros Lançamentos Contábeis – Vide regra RN 10
Campo Código da Natureza da Receita – Vide regra RN 11
Campo Descrição Complementar – Vide regra RN 12
Campo Descrição da Natureza da Operação – Vide regra RN 14
Campo Indicador de Situação – Vide regra RN 15
Campo Indicador de Natureza – Vide regra RN 16
Campo Código da Conta (Débito) – Vide regra RN 17
Campo Descrição da Conta (Débito) – Vide regra RN 18
Campo Chave de Lançamento (Débito) – Vide regra RN 19
Campo Código da Conta (Crédito) – Vide regra RN 25
Campo Chave de Lançamento (Crédito) – Vide regra RN 27
Campo Usuário – Vide regra RN 33


REGRAS DE NEGÓCIO



Considerações deste modelo:

**Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**




---

| MFS | Nome | Descrição |
| --- | --- | --- |
| ADO- 973594 | Beatriz Tie Terada, Millys Lopes | Definição das regras de importação da SAFX344 |


---

| CÓD | DESCRIÇÃO | ADO |
| --- | --- | --- |
| RN00 |  | ADO- 973594 |
| RN00.1 | Campos Obrigatório não preenchido  Se algum campo de preenchimento obrigatório não estiver preenchido, exibir a mensagem “Campo <<Nome do campo>> deve ser preenchido” | ADO- 973594 |
| RN01 | Campo 01 - Código da empresa   Tabela: SAFX344 Item: 01 Nome do Campo: COD_EMPRESA Descrição: Campo destinado ao código da Empresa. Vide regra RN00 Tipo: A Tamanho: 003 Campo Obrigatório Chave Primária Comentário: Informar o Código da Empresa Exibir a mensagem da TFIX 22 CÓDIGO 90001 | ADO- 973594 |
| RN02 | Campo 02 - Código do estabelecimento  Tabela: SAFX344 Item: 02 Nome do Campo: COD_ESTAB Descrição: Campo destinado ao código do Estabelecimento. Vide regra RN01 Tipo: A Tamanho: 006  Campo Obrigatório Chave Primária Comentário: Informar o Código do Estabelecimento Exibir a mensagem da TFIX 22 CÓDIGO 90002 | ADO- 973594 |
| RN03 | Campo 03 – Unidade Federal Tabela: SAFX344 Item: 03 Nome do Campo: UF Descrição: Informar a sigla da Unidade Federativa (UF) correspondente ao estabelecimento. Tipo: C Tamanho: 002 Campo Não Obrigatório Comentário:  Informa as UFs dos Estabelecimentos previamente selecionados na RN01. | ADO- 973594 |
| RN04 | Campo 04 – Referência  Tabela: SAFX344 Item: 04 Nome do Campo: REFERENCIA Descrição: O Preenchimento é livre os dados provenientes dos 'Livros Fiscais' ou da Apuração do Sistema SAP. Tipo: C Tamanho: 016 Campo Não Obrigatório Comentário:  Informar ao usuário a rastreabilidade dos dados preenchidos referentes aos Livros Fiscais ou Apuração provenientes do sistema SAP. | ADO- 973594 |
| RN05 | Campo 05 – Grupo do Imposto  Tabela: SAFX344 Item: 05 Nome do Campo: IMPOSTO Descrição: Informar o preenchimento do imposto atrelado ao âmbito Federal ou Estadual. Vide regra RN04 Tipo: C Tamanho: 010 Campo Obrigatório Chave Primária Comentário: Permitir ao usuário escolher entre as opções ‘Federal’ ou ‘Estadual’ Exibir a mensagem da TFIX 22 CÓDIGO 913312 | ADO- 973594 |
| RN06 | Campo 06 – Imposto  Tabela: SAFX344 Item: 06 Nome do Campo: IMPOSTO Descrição: Informar o preenchimento do imposto atrelado ao âmbito Federal ou Estadual. Vide regra RN04 Tipo: C Tamanho: 016 Campo Obrigatório Chave Primária Comentário: Este campo informa os tributos que compõem o campo GRUPO_IMPOSTO (RN04), sendo eles, de âmbito Federal: PIS/PASEP-Cumulativo, PIS/PASEP-Não Cumulativo, COFINS- Cumulativo, COFINS-Não Cumulativo, IPI. E de âmbito Estadual: ICMS- Próprio, ICMS-ST, ICMS-Antecipado, FCP, DIFAL, SCANC Exibir a mensagem da TFIX 22 CÓDIGO 913313 | ADO- 973594 |
| RN07 | Campo 07 – Local de Negócio   Tabela: SAFX344 Item: 07 Nome do Campo: LOCAL_NEGOCIO Descrição: O Preenchimento é livre e indica o código correspondente a um estabelecimento dentro da matriz no sistema SAP. Tipo: A Tamanho: 004 Campo Não Obrigatório Comentário: Informar o código do estabelecimento advindo do sistema SAP e previamente preenchido pelo usuário | ADO- 973594 |
| RN08 | Campo 08 – Divisão  Tabela: SAFX344 Item: 08 Nome do Campo: DIVISAO Descrição: O Preenchimento é livre indica a segregação financeira de um segmento específico dentro do sistema SAP. Tipo: A Tamanho: 004 Campo Não Obrigatório Comentário: Informar o código do segmento/divisão financeira conforme cadastro no SAP. | ADO- 973594 |
| RN09 | Campo 09 – Centro  Tabela: SAFX344 Item: 09 Nome do Campo: CENTRO Descrição: O Preenchimento é livre indica a segregação SAP Tipo: A Tamanho: 004 Campo Não Obrigatório Comentário: Informar o Centro onde ocorreu a operação que deu origem ao registro. | ADO- 973594 |
| RN10 | Campo 10 – Código do tipo do Livro Tabela: SAFX344 Item: 10 Nome do Campo: COD_TIPO_LIVRO Descrição: Informar o código do livro fiscal “108” (Livro de Apuração) ou “165” (Livro de Apuração por Inscrição Estadual Única) 002 – Livro de Apuração IPI Tipo: A Tamanho: 003 Campo Obrigatório Comentário: Este campo informa o tipo do livro para os impostos ICMS Próprio, ICMS-ST, ICMS Antecipado, IPI, FCP, DIFAL: | ADO- 973594 |
| RN11 | Campo 11 – Outros Lançamentos Contábeis    Tabela: SAFX344 Item: 11 Nome do Campo: OUTROS_LANCAMENTOS_CONTABEIS Descrição: Identificar os seguintes tipos de lançamentos (este dado preencher conforme dados da RN07):  - Saldo Devedor, - Saldo Credor,  - Total de Crédito,  - Total de Débito,  - F100 - Demais Receitas  - F100 - Demais Créditos. Tipo: C Tamanho: 050 Campo Obrigatório Comentário: Este campo informa aos usuários os valores associados às duas categorias de tributos que podem ser selecionadas, sendo elas:  ICMS Próprio, ICMS-ST, ICMS Antecipado, IPI, FCP, DIFAL: Saldo Devedor Saldo Credor Total de Crédito Total de Débito PIS - Cumulativo, PIS - Não Cumulativo, COFINS - Cumulativo e COFINS - Não Cumulativo: Saldo Devedor Saldo Credor Total de Crédito Total de Débito F100 - Demais Receitas F100 - Demais Créditos Exibir a mensagem da TFIX 22 CÓDIGO 913316 | ADO- 973594 |
| RN12 | Campo 12 – Código da Natureza da Receita  Tabela: SAFX344 Item: 12 Nome do Campo: COD_NAT_REC  Descrição: Informar o código da Natureza da Receita da operação/serviço não tributada ou não sujeita ao pagamento da contribuição PIS/COFINS da SAFX 147  Tipo: N Tamanho: 003 Campo Obrigatório Comentário: Informar o código da Natureza da Receita da operação/serviço não tributada ou não sujeita ao pagamento da contribuição PIS/COFINS da SAFX 147  Exibir a mensagem da TFIX 22 CÓDIGO 913317 | ADO- 973594 |
| RN13 | Campo 13 – Descrição Complementar do Documento/Operação Tabela: SAFX344344 Item: 13 Nome do Campo: DESC_COMPL Descrição: Informar a descrição complementar do Documento/Operação.SAFX147 Tipo: A Tamanho: 255 Campo Obrigatório Comentário: Informar a descrição complementar do Documento/Operação (SAFX147), fazer concatenação com o campo COD_NAT_REC Exibir a mensagem da TFIX 22 CÓDIGO 913318 | ADO- 973594 |
| RN14 | Campo 14 – Código Natureza da Operação  Tabela: SAFX344344 Item: 14 Nome do Campo: COD_NATUREZA_OP Descrição: Informar o Código da Natureza de Operação conforme SAFX2006 Tipo: A Tamanho: 001 Campo Obrigatório Comentário: Informar o Código da Natureza de Operação conforme SAFX2006 Exibir a mensagem da TFIX 22 CÓDIGO 913319 | ADO- 973594 |
| RN15 | Campo 15 – Descrição da Natureza da Operação  Tabela: SAFX344 Item: 15 Nome do Campo: DESCRICAO_DSC_OPER_APUR Descrição: Informar a Descrição da Natureza da Operação. SAFX2006 Tipo: A Tamanho: 255 Campo Obrigatório Comentário: Informar a Descrição da Natureza da Operação, conforme SAFX2006 Exibir a mensagem da TFIX 22 CÓDIGO 913320 | ADO- 973594 |
| RN16 | Campo 16 – Chave de Lançamento (Débito)  Tabela: SAFX344 Item: 16 Nome do Campo: CHAVE_LANCTO_D Descrição: Indica que o preenchimento é fixo com o valor '40' para transações de débito. Tipo: N Tamanho: 002 Campo Obrigatório Comentário: Informar a identificação do tipo de Lançamento Contábil, nesse caso, indicar o preenchimento fixo com o valor '40' para transações de débito Exibir a mensagem da TFIX 22 CÓDIGO 913321 | ADO- 973594 |
| RN17 | Campo 17 – Código da Conta (Débito)  Tabela: SAFX344 Item: 17 Nome do Campo: COD_CONTA_D Descrição: Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas (SAFX2002). Tipo: A Tamanho: 070 Campo Obrigatório Comentário: Informar o Código da Conta e Subconta (referente a operações de Débito), que deve estar registrada na Tabela de Plano de Contas (SAFX2002) Exibir a mensagem da TFIX 22 CÓDIGO 913322 | ADO- 973594 |
| RN18 | Campo 18 – Descrição da Conta (Débito) Tabela: SAFX344 Item: 18 Nome do Campo: DESCRICAO_CONTA_D Descrição: Informar a Descrição da Conta existente na SAFX2002 Tipo: A Tamanho: 050 Campo Obrigatório Comentário: Informar a Descrição da Conta (referente a operações de Débito) existente na SAFX2002 Exibir a mensagem da TFIX 22 CÓDIGO 913323 | ADO- 973594 |
| RN19 | Campo 19 – Indicador da Situação (Débito) Tabela: SAFX344 Item: 19 Nome do Campo: IND_SITUACAO_D Descrição: Informar se a conta de débito está sendo utilizada ou não pela Contabilidade da empresa. O campo assume os seguintes valores: A – Ativa na SAFX2002 Tipo: A Tamanho: 001 Campo Obrigatório Comentário: Informar se a conta de débito está sendo utilizada ou não pela Contabilidade da empresa. O campo assume os seguintes valores: A – Ativa na SAFX2002 Exibir a mensagem da TFIX 22 CÓDIGO 913324 |  |
| RN20 | Campo 20 – Indicador da Natureza (Débito) Tabela: SAFX344 Item: 20 Nome do Campo: IND_NATUREZA_D Descrição: Informar o Indicador de Natureza (débito) existente na SAFX2002: 1. Ativo 2. Passivo 3. Despesa Tipo: A Tamanho: 001 Campo Obrigatório Comentário: Informar o Indicador de Natureza (débito) existente na SAFX2002: 1. Ativo 2. Passivo 3. Despesa  Exibir a mensagem da TFIX 22 CÓDIGO 913325 |  |
| RN21 | Campo 20 – Centro de Custo (Débito)  Tabela: SAFX344 Item: 20 Nome do Campo: CENTRO_CUSTO_D Descrição: Informar o Centro de Custo. O Código deve estar registrado na Tabela de Centro de Custos (SAFX2003). Tipo: N Tamanho: 020 Campo Não Obrigatório Comentário: Informar o Código do Centro de Custo (referente a operações de Débito) conforme registro prévio na SAFX2003 | ADO- 973594 |
| RN22 | Campo 22 – Centro de Lucro (Débito)  Tabela: SAFX344 Item: 22 Nome do Campo: CENTRO_LUCRO_D Descrição: O preenchimento é livre e informar o código do centro de lucros, utilizado para alocar receitas ou despesas de forma similar ao centro de custo. Este campo é opcional e serve apenas para controle interno. Tipo: N Tamanho: 020 Campo Não Obrigatório Comentário: Informar o Código do Centro de Lucro (referente a operações de Débito), este campo é opcional e serve apenas para controle interno. | ADO- 973594 |
| RN23 | Campo 23 – Texto do Histórico (Débito)  Tabela: SAFX344 Item: 23 Nome do Campo: TEXTO_D Descrição: Informar o histórico da contabilização contábil  Tipo: A Tamanho: 020 Campo Não Obrigatório  Comentário: Informar o histórico da contabilização contábil para transações de débito | ADO- 973594 |
| RN24 | Campo 24 – Observação (Débito)  Tabela: SAFX344 Item: 24 Nome do Campo: OBSERVAÇÃO_D Descrição: Registrar a observação referente ao lançamento. Tipo: A Tamanho: 020 Campo Não Obrigatório Comentário: Informar observações relevantes referentes ao tipo de lançamento, nesse caso, Débito | ADO- 973594 |
| RN25 | Campo 25 – Chave de Lançamento (Crédito) Tabela: SAFX344 Item: 25 Nome do Campo: CHAVE_LANCTO_C Descrição: Indica que o preenchimento é fixo com o valor '50' para transações de Crédito. Tipo: N Tamanho: 002 Campo Obrigatório Comentário: Informar a identificação do tipo de Lançamento Contábil, nesse caso, indicar o preenchimento fixo com o valor '50' para transações de crédito Exibir a mensagem da TFIX 22 CÓDIGO 913326 | ADO- 973594 |
| RN26 | Campo 26 – Código da Conta (Crédito)  Tabela: SAFX344 Item: 26 Nome do Campo: COD_CONTA_C Descrição: Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas (SAFX2002).  Tipo: N Tamanho: 070 Campo Obrigatório Comentário: Informar o Código da Conta e Subconta (referente a operações de Crédito), que deve estar registrada na Tabela de Plano de Contas (SAFX2002). Exibir a mensagem da TFIX 22 CÓDIGO 913327 | ADO- 973594 |
| RN27 | Campo 27 – Descrição da Conta (Crédito)  Tabela: SAFX344 Item: 27 Nome do Campo: DESCRICAO_CONTA_C Descrição: Informar a Descrição da Conta existente na SAFX2002 Tipo: A Tamanho: 050 Campo Obrigatório Comentário: Informar a Descrição da Conta (referente a operações de Crédito) existente na SAFX2002 Exibir a mensagem da TFIX 22 CÓDIGO 913328 | ADO- 973594 |
| RN28 | Campo 28 – Indicador de Situação (Crédito)  Tabela: SAFX344 Item: 28 Nome do Campo: IND_SITUACAO_C Descrição: Informar se a conta de crédito está sendo utilizada ou não pela Contabilidade da empresa. O campo assume os seguintes valores: A – Ativa na SAFX2002 Tipo: A Tamanho: 001 Campo Obrigatório Comentário: Informar se a conta de crédito está sendo utilizada ou não pela Contabilidade da empresa. O campo assume os seguintes valores: A – Ativa na SAFX2002Exibir a mensagem da TFIX 22 CÓDIGO 913329 |  |
| RN29 | Campo 29 – Indicador da Natureza (Crédito)  Tabela: SAFX344 Item: 29 Nome do Campo: IND_NATUREZA_C Descrição: Informar o Indicador de Natureza (crédito) existente na SAFX2002: 1. Ativo 2. Passivo 3. Despesa Tipo: A Tamanho: 001 Campo Obrigatório Comentário:  Informar o Indicador de Natureza (crédito) existente na SAFX2002: 1. Ativo 2. Passivo 3. Despesa Exibir a mensagem da TFIX 22 CÓDIGO 913330 |  |
| RN30 | Campo 30 – Centro de Custo (Crédito) Tabela: : SAFX Item: 30 Nome do Campo: CENTRO_CUSTO_C Descrição: Informar o Código do Centro de Custo. Tipo: A Tamanho: 050 Campo Não Obrigatório Comentário: Informar o Código do Centro de Custo. | ADO- 973594 |
| RN31 | Campo 31 – Centro de Lucro (Crédito)  Tabela: SAFX344 Item: 31 Nome do Campo: CENTRO_LUCRO_C Descrição: Informar o Código do Centro de Lucro. Tipo: N Tamanho: 020 Campo Não Obrigatório Comentário: Informar o Código do Centro de Lucro (referente a operações de Crédito), este campo é opcional e serve apenas para controle interno. | ADO- 973594 |
| RN32 | Campo 32 – Texto do Histórico (Crédito)  Tabela: SAFX344 Item: 32 Nome do Campo: TEXTO_C Descrição: Informar o histórico da contabilização contábil Tipo: A Tamanho: 020 Campo Não Obrigatório Comentário: Informar o histórico da contabilização contábil para transações de crédito | ADO- 973594 |
| RN33 | Campo 33 – Observação (Crédito)  Tabela: SAFX344 Item: 33 Nome do Campo: OBSERVACAO_C Descrição: Registrar a observação referente ao lançamento. Tipo: A Tamanho: 020 Campo Não Obrigatório Comentário: Informar observações relevantes referentes ao tipo de lançamento, nesse caso, Crédito |  |
| RN34 | Campo 34 – Usuário  Tabela: SAFX344 Item: 34 Nome do Campo: USUARIO Descrição: Informar o login do usuário responsável pela gravação dos dados. Tipo: A Tamanho: 014 Campo Obrigatório Comentário: Informar o login do usuário responsável pela gravação dos dados. Exibir a mensagem da TFIX 22 CÓDIGO 913304 |  |
| RN35 | Campo 35 – Data do Parâmetro  Tabela: SAFX344 Item: 36 Nome do Campo: DATA_PARAMETRO Descrição: Informar a Data Início/Inclusão/Alteração. Tipo: N Tamanho: 008 Campo Não Obrigatório Comentário: Informar a Data Início/Inclusão/Alteração do parâmetro |  |


---

| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |

