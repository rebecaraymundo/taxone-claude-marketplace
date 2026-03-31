---
source: "MTZ_Carga_Importacao_Contabilizacao_SAFX_347-Retorno de Dados Contabilizados Apuração – Sistema SAP.docx"
category: Contabilização -Apuração
converted: auto
---





THOMSON REUTERS


IMPORTAÇÃO - SAFX347 (Retorno de Dados Contabilizados Apuração – Sistema SAP)
TAXONE >> Básicos > Data Warehouse > Manutenção > Contabilização da Apuração


DOCUMENTO DE REQUISITO


# Introdução
A nova SAFX 347 de Retorno será responsável por receber os dados fornecidos pelo sistema SAP via OBI, que disponibilizará informações sobre os dados contabilizados para atualização de Status, Estorno e Contabilização Automática .
O sistema OBI irá consumir esses dados, realizar o processamento necessário e enviar as informações, através da nova SAFX de Retorno, o Tax One, onde serão utilizadas posteriormente.
Os dados serão atualizados com base nos campos-chave: Empresa, Estabelecimento, Período e Número do Documento Contábil.
Sempre que for gerado um número de documento contábil, os dados serão retornados ao Tax One, Esse Retorno  proporcionará os seguintes benefícios:
Atualização automática do status no Relatório de Status do Tax One para Contabilizado.
Registro do número do documento contábil que originou a contabilização.
Disponibilização dos dados necessários para:
**Geração de estornos**
Criação de um fluxo de contabilização automática


**Localização:**

Módulo: Básicos > Guias de Pagamentos
Menu: Guias de Pagamentos

**(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX 347 conforme o Manual de Layout, o que facilita a consulta. Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00).**

Procedimentos para Importação da SAFX

**A importação da SAFX deve atender às seguintes premissas:**

Todos os campos obrigatórios e chaves devem estar preenchidos corretamente.
O processo deve identificar e atualizar o status da guia de forma precisa.

**Resultado da Importação**

Se a importação for bem-sucedida, os dados serão registrados nas seguintes telas:
Tax One > Básico > Data Warehouse > Manutenção > Contabilização da Apuração > Estorno
Tax One > Básico > Data Warehouse > Manutenção > Contabilização da Apuração > Contabilização Automática
Tax One > Básico > Data Warehouse > Manutenção > Contabilização da Apuração > Relatório de Status

Regra Geral para validação

1º ) Consistências Básicas:

Campos Data inválidos
Campos Obrigatórios
Campos Numéricos inválidos
Campo Chave de Identificação – Vide regra RN 01
Campo Período – Vide regra RN 02
Campo Exercício – Vide regra RN 03
Campo Grupo de Imposto -Vide regra RN 13
Campo Imposto – Vide regra RN 14
Campo Código de Ajuste -Vide regra RN 15
Campo Descrição de Ajuste – Vide regra RN 16
Campo Chave de Lançamento (Débito) – Vide regra RN 19
Campo Código da Conta (Débito) – Vide regra RN 20
Campo Descrição da Conta (Débito) – Vide regra RN 21
Campo Chave de Lançamento (Crédito) – Vide regra RN 28
Campo Código da Conta (Crédito) – Vide regra RN 29
Campo Descrição da Conta (Crédito) – Vide regra RN 30
Campo Usuário – Vide regra RN 38











REGRAS DE NEGÓCIO



Considerações deste modelo:

**Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**




---

| MFS | Nome | Descrição |
| --- | --- | --- |
| ADO- 913154 | Beatriz Tie Terada, Millys Lopes | Definição das regras de importação da SAFX 347 |


---

| CÓD | DESCRIÇÃO | ADO |
| --- | --- | --- |
| RN00 |  | ADO- 913154 |
| RN00.1 | Campos Obrigatório não preenchido  Se algum campo de preenchimento obrigatório não estiver preenchido, exibir a mensagem “Campo <<Nome do campo>> deve ser preenchido” | ADO- 913154 |
| RN01 | Campo 01 – Código da Empresa  Tabela: SAFX 347 Item: 01 Nome do Campo: COD_EMPRESA Descrição: Código da Empresa Tipo: A Tamanho: 003 Campo Obrigatório Chave Primária Comentário: Informar o Código da Empresa  Exibir a mensagem da TFIX 22 CÓDIGO 90001 |  |
| RN02 | Campo 02 – Código do Estabelecimento    Tabela: SAFX 347 Item: 02 Nome do Campo: COD_ESTAB Descrição: Código do Estabelecimento Tipo: A Tamanho: 006 Campo Obrigatório Chave Primária  Comentário: Informar o código do estabelecimento advindo do sistema SAP e previamente preenchido pelo usuário Exibir a mensagem da TFIX 22 CÓDIGO 90002 |  |
| RN03 | Campo 03 – Chave de Identificação   Tabela: SAFX 347 Item: 03 Nome do Campo: CHAVE_ID Descrição: Chave de Rastreabilidade Tipo: A Tamanho: 070 Campo Obrigatório Chave Primária Comentário: Informar a Chave de Rastreabilidade  Exibir a mensagem da TFIX 22 CÓDIGO 913331 | ADO- 913154 |
| RN04 | Campo 04 - Período  Tabela: SAFX 347 Item: 04 Nome do Campo: PERIODO Descrição: Período Mensal da Apuração Tipo: A Tamanho: 002 Campo Obrigatório Chave Primária Comentário: Informar o Período Mensal da Apuração Exibir a mensagem da TFIX 22 CÓDIGO 913333 | ADO- 913154 |
| RN05 | Campo 05 – Exercício Tabela: SAFX 347 Item: 05 Nome do Campo: EXERCICIO Descrição: Ano da apuração Tipo: N Tamanho: 004 Campo Obrigatório Chave Primária  Comentário:  Informar o Ano da Apuração  Exibir a mensagem da TFIX 22 CÓDIGO 913334 | ADO- 913154 |
| RN06 | Campo 06 – Data do Documento  Tabela: SAFX 347 Item: 06 Nome do Campo: DT_DOCTO Descrição: Data do Documento Tipo: N Tamanho: 008 Campo Não Obrigatório Comentário:  Informar a Data do Documento | ADO- 913154 |
| RN07 | Campo 07 – Data do Lançamento  Tabela: SAFX 347 Item: 07 Nome do Campo: DT_LANCTO Descrição: Data do Lançamento Tipo: N Tamanho: 008 Campo Não Obrigatório Comentário: Informar a Data do Lançamento | ADO- 913154 |
| RN08 | Campo 08 – Unidade Federal   Tabela: SAFX 347 Item: 08 Nome do Campo: UF  Descrição: Informar a sigla da Unidade Federativa (UF) correspondente ao estabelecimento.  Tipo: C  Tamanho: 002  Campo Não Obrigatório  Comentário:   Informa as UFs dos Estabelecimentos previamente selecionados. | ADO- 913154 |
| RN09 | Campo 09 – Referência  Tabela: SAFX 347 Item: 09 Nome do Campo: REFERENCIA  Descrição: O Preenchimento é livre e os dados são provenientes dos 'Livros Fiscais' ou da Apuração do Sistema SAP.  Tipo: C  Tamanho: 016  Campo Não Obrigatório  Comentário:  Informar ao usuário a rastreabilidade dos dados preenchidos referentes aos Livros Fiscais ou Apuração provenientes do sistema SAP. | ADO- 913154 |
| RN10 | Campo 10 – Local de Negócio   Tabela: SAFX 347 Item: 10 Nome do Campo: LOCAL_NEGOCIO  Descrição: O Preenchimento é livre e indica o código correspondente a um estabelecimento dentro da matriz no sistema SAP.  Tipo: A  Tamanho: 004  Campo Não Obrigatório  Comentário:  Informar o código do estabelecimento advindo do sistema SAP e previamente preenchido pelo usuário | ADO- 913154 |
| RN11 | Campo 11 – Divisão  Tabela: SAFX 347 Item: 11 Nome do Campo: DIVISAO  Descrição: O Preenchimento é livre indica a segregação financeira de um segmento específico dentro do sistema SAP.  Tipo: A  Tamanho: 004  Campo Não Obrigatório  Comentário:  Informar o código do segmento/divisão financeira conforme cadastro no SAP. | ADO- 913154 |
| RN12 | Campo 12 – Centro  Tabela: SAFX 347 Item: 12 Nome do Campo: CENTRO Descrição: O Preenchimento é livre indica a segregação SAP  Tipo: A Tamanho: 004 Campo Não Obrigatório  Comentário:  Informar o Centro onde ocorreu a operação que deu origem ao registro. | ADO- 913154 |
| RN13 | Campo 13 – Grupo de Imposto  Tabela: SAFX 347 Item: 13 Nome do Campo: GRUPO_IMPOSTO  Descrição: Informa se o preenchimento é Federal ou Estadual. Tipo: C  Tamanho: 010  Campo Obrigatório  Chave Primária  Comentário:   Permitir ao usuário escolher entre as opções ‘Federal’ ou ‘Estadual’  Exibir a mensagem da TFIX 22 CÓDIGO 913312 | ADO- 913154 |
| RN14 | Campo 14 – Imposto  Tabela: SAFX 347 Item: 14 Nome do Campo: IMPOSTO  Descrição: Indica os tributos aplicáveis, como ICMS, ICMS-ST, IPI, DIFAL, FCP, PIS e COFINS. Tipo: C  Tamanho: 020  Campo Obrigatório  Chave Primária  Comentário:  Este campo informa os tributos que compõem o campo GRUPO_IMPOSTO (RN04), sendo eles, de âmbito Federal: PIS/PASEP-Cumulativo, PIS/PASEP-Não Cumulativo, COFINS- Cumulativo, COFINS-Não Cumulativo, IPI. E de âmbito Estadual: ICMS- Próprio, ICMS-ST, ICMS-Antecipado, FCP, DIFAL, SCANC  Exibir a mensagem da TFIX 22 CÓDIGO 913313 | ADO- 913154 |
| RN15 | Campo 15 – Código de Ajuste  Tabela: SAFX 347 Item: 15 Nome do Campo: COD_AJUSTE  Descrição: Informa o código de ajuste conforme a apuração dos tributos ICMS, ICMS-Antecipado, ICMS-ST, IPI, DIFAL, FCP e SCANC, PIS e COFINS.   Tipo: A Tamanho: 015 Campo Obrigatório  Chave Primária  Comentário:  Ao selecionar o Grupo de Imposto (Federal e Estadual) — ICMS-Próprio, ICMS-Antecipado, ICMS-ST, DIFAL, FCP, IPI, PIS (Cumulativo e Não Cumulativo), COFINS (Cumulativo e Não Cumulativo) e SCANC — o sistema deve: (1) identificar o "Imposto Relacionado"; (2) consultar a tabela de ajustes correspondente ao tributo (para ICMS/DIFAL/FCP/ICMS-ST usar ICT_AJUSTE_ICMS; para IPI/PIS/COFINS/SCANC usar a tabela própria do tributo); (3) recuperar os campos de código e descrição do ajuste; e (4) concatenar esses valores para preencher automaticamente o campo "Código de Ajuste".  Exibir a mensagem da TFIX 22 CÓDIGO 913314 |  |
| RN16 | Campo 16 – Descrição de Ajuste  Tabela: SAFX 347 Item: 16 Nome do Campo: DESCRICAO_AJUSTE  Descrição: Informar a descrição dos ajustes realizados nas apurações de ICMS, ICMS-ST, IPI, DIFAL, FCP, PIS e COFINS. Tipo: C  Tamanho: 050  Campo Obrigatório  Comentário:  Este campo deve ser concatenado ao campo COD_AJUSTE (RN10) e informa ao usuário a descrição referente ao código de ajuste, conforme a apuração dos tributos ICMS, ICMS-Antecipado, ICMS-ST, IPI, DIFAL, FCP e SCANC, PIS e COFINS  Exibir a mensagem da TFIX 22 CÓDIGO 913315 |  |
| RN17 | Campo 17 – Chave de Lançamento (Débito)   Tabela: SAFX 347 Item: 17 Nome do Campo: CHAVE_LANCTO_D  Descrição: Indica que o preenchimento é fixo com o valor '40' para transações de débito.  Tipo: N  Tamanho: 002  Campo Obrigatório  Comentário:  Informar a identificação do tipo de Lançamento Contábil, nesse caso, indicar o preenchimento fixo com o valor '40' para transações de débito  Exibir a mensagem da TFIX 22 CÓDIGO 913321 | ADO- 913154 |
| RN18 | Campo 18 – Código da Conta (Débito)  Tabela: SAFX 347 Item: 18 Nome do Campo: COD_CONTA_D  Descrição: Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas (SAFX2002).  Tipo: N Tamanho: 070  Campo Obrigatório  Comentário:  Informar o Código da Conta e Subconta (referente a operações de Débito), que deve estar registrada na Tabela de Plano de Contas (SAFX2002)  Exibir a mensagem da TFIX 22 CÓDIGO 913322 | ADO- 913154 |
| RN19 | Campo 19 – Descrição da Conta (Débito)   Tabela: SAFX 347 Item: 19 Nome do Campo: DESCRICAO_CONTA_D  Descrição: Informar a Descrição da Conta existente na SAFX2002  Tipo: A  Tamanho: 050  Campo Obrigatório  Comentário:  Informar a Descrição da Conta (referente a operações de Débito) existente na SAFX2002  Exibir a mensagem da TFIX 22 CÓDIGO 913323 | ADO- 913154 |
| RN20 | Campo 20 – Montante (Débito)  Tabela: SAFX 347 Item: 20 Nome do Campo: MONTANTE_D Descrição: Informa o valor do lançamento contábil Tipo: N Tamanho: 017V002 Campo Obrigatório Comentário: Informar o Valor do Lançamento Contábil para transações de Débito | ADO- 913154 |
| RN21 | Campo 21 – Centro de Custo (Débito)  Tabela: SAFX 347 Item: 21 Nome do Campo: CENTRO_CUSTO_D  Descrição: Informar o Centro de Custo. O Código deve estar registrado na Tabela de Centro de Custos (SAFX2003).  Tipo: N  Tamanho: 020  Campo Não Obrigatório  Comentário:  Informar o Código do Centro de Custo (referente a operações de Débito), conforme registro prévio na Tabela de Centro de Custos da SAFX2003 | ADO- 913154 |
| RN22 | Campo 22 – Descrição do Centro de Custo (Débito)  Tabela: SAFX 347 Item: 22 Nome do Campo: DESCRICAO_CENTRO_CUSTO_D  Descrição: Informar o Centro de Custo. A descrição do centro de custo deve estar registrada na Tabela de Centro de Custos (SAFX2003).  Tipo: A  Tamanho: 050  Campo Não Obrigatório  Comentário:  Informar a Descrição do Centro de Custo (referente a operações de Débito) conforme registro prévio na SAFX2003 | ADO- 913154 |
| RN23 | Campo 23 – Centro de Lucro (Débito)  Tabela: SAFX 347 Item: 23 Nome do Campo: CENTRO_LUCRO_D  Descrição: O preenchimento é livre e informar o código do centro de lucros, utilizado para alocar receitas ou despesas de forma similar ao centro de custo. Este campo é opcional e serve apenas para controle interno. Tipo: N  Tamanho: 020  Campo Não Obrigatório  Comentário:  Informar o Código do Centro de Lucro (referente a operações de Débito), este campo é opcional e serve apenas para controle interno. | ADO- 913154 |
| RN24 | Campo 24 – Texto do Histórico (Débito)   Tabela: SAFX 347 Item: 24 Nome do Campo: TEXTO_D  Descrição: Campo para informar o histórico de lançamento dado preenchido pelo usuário Tipo: A  Tamanho: 020  Campo Não Obrigatório   Comentário:  Informar o histórico de lançamento dado preenchido pelo usuário para transações de débito | ADO- 913154 |
| RN25 | Campo 25 – Observação (Débito) Tabela: SAFX 347 Item: 25 Nome do Campo: OBSERVAÇÃO_D  Descrição: Registrar a observação referente ao lançamento.  Tipo: A  Tamanho: 020  Campo Não Obrigatório  Comentário:  Informar observações relevantes referentes ao tipo de lançamento, nesse caso, Débito | ADO- 913154 |
| RN26 | Campo 26 – Chave de Lançamento (Crédito)   Tabela: SAFX 347 Item: 26 Nome do Campo: CHAVE_LANCTO_C  Descrição: Indica que o preenchimento é fixo com o valor '50' para transações de Crédito.  Tipo: N  Tamanho: 002  Campo Obrigatório  Comentário:  Informar a identificação do tipo de Lançamento Contábil, nesse caso, indicar o preenchimento fixo com o valor '50' para transações de crédito  Exibir a mensagem da TFIX 22 CÓDIGO 913326 | ADO- 913154 |
| RN27 | Campo 27 – Código da Conta (Crédito)   Tabela: SAFX 347 Item: 27 Nome do Campo: COD_CONTA_C  Descrição: Informar o Código da Conta e Subconta, que deve estar registrada na Tabela de Plano de Contas (SAFX2002).   Tipo: N  Tamanho: 070  Campo Obrigatório  Comentário:  Informar o Código da Conta e Subconta (referente a operações de Crédito), que deve estar registrada na Tabela de Plano de Contas (SAFX2002).  Exibir a mensagem da TFIX 22 CÓDIGO 913327 | ADO- 913154 |
| RN28 | Campo 28 – Descrição da Conta (Crédito)  Tabela: SAFX 347 Item: 28 Nome do Campo: DESCRICAO_CONTA_C  Descrição: Informar a Descrição da Conta existente na SAFX2002  Tipo: A  Tamanho: 050  Campo Obrigatório  Comentário:  Informar a Descrição da Conta (referente a operações de Crédito) existente na SAFX2002  Exibir a mensagem da TFIX 22 CÓDIGO 913328 | ADO- 913154 |
| RN29 | Campo 29 – Montante (Crédito)  Tabela: SAFX Item: 29 Nome do Campo: MONTANTE_C Descrição: Informa o valor do lançamento contábil  Tipo: N Tamanho: 017V002 Campo Obrigatório Comentário: Informar o valor do lançamento contábil para transações de Crédito | ADO- 913154 |
| RN30 | Campo 30 – Centro de Custo (Crédito)  Tabela: SAFX 347 Item: 30 Nome do Campo: CENTRO_CUSTO_C  Descrição: Informar o Centro de Custo. O Código deve estar registrado na Tabela de Centro de Custos (SAFX2003). Tipo: N  Tamanho: 020  Campo Não Obrigatório  Comentário:  Informar o Código do Centro de Custo (referente a operações de Crédito), que deve estar registrado na Tabela de Centro de Custos (SAFX2003). | ADO- 913154 |
| RN31 | Campo 31 – Descrição do Centro de Custo (Crédito)  Tabela: SAFX 347 Item: 31 Nome do Campo: DESCRICAO_CENTRO_CUSTO_C  Descrição: Informar o Centro de Custo. A descrição do centro de custo deve estar registrada na Tabela de Centro de Custos (SAFX2003). Tipo: A Tamanho: 050 Campo Não Obrigatório Comentário: Informar a Descrição do Centro de Custo (referente a operações de Crédito) conforme registro prévio na SAFX2003 | ADO- 913154 |
| RN32 | Campo 32 – Centro de Lucro (Crédito)  Tabela: SAFX Item: 32 Nome do Campo: CENTRO_LUCRO_C Descrição: Informar o Código do Centro de Custo. Tipo: N Tamanho: 020 Campo Não Obrigatório Comentário: Informar o Código do Centro de Lucro (referente a operações de Crédito), este campo é opcional e serve apenas para controle interno |  |
| RN33 | Campo 33 – Texto do Histórico (Crédito)   Tabela: SAFX 347 Item: 33 Nome do Campo: TEXTO_C Descrição: Campo para informar o histórico de lançamento dado preenchido pelo usuário Tipo: A  Tamanho: 020  Campo Não Obrigatório  Comentário:  Informar o histórico de lançamento dado preenchido pelo usuário para transações de crédito |  |
| RN34 | Campo 34 – Observação (Crédito)   Tabela: SAFX 347 Item: 34 Nome do Campo: OBSERVACAO_C Descrição: Registrar a observação referente ao lançamento.  Tipo: A  Tamanho: 020  Campo Não Obrigatório  Comentário:  Informar observações relevantes referentes ao tipo de lançamento, nesse caso, Crédito |  |
| RN35 | Campo 35 – Usuário  Tabela: SAFX 347 Item: 35 Nome do Campo: USUARIO Descrição: Nome do analista responsável pela contabilização Tipo: A Tamanho: 014 Campo Obrigatório  Comentário:  Informar o login do usuário responsável pela gravação dos dados.  Exibir a mensagem da TFIX 22 CÓDIGO 913304 |  |
| RN36 | Campo 36 – Número do Documento Contábil  Tabela: SAFX 347 Item: 36 Nome do Campo: NRO_DOC_CONTABIL Descrição: Informa o Número do Documento Contábil criado no SAP.   Tipo: N Tamanho: 010 Campo Obrigatório  Comentário:  Informa o Número do Documento Contábil criado no SAP.   Exibir a mensagem da TFIX 22 CÓDIGO 913358 |  |


---

| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |

