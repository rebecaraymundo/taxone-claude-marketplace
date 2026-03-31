# MTZ_Prodepe_Apuracao-do-ICMS-Não_Incentivados

> Fonte: MTZ_Prodepe_Apuracao-do-ICMS-Não_Incentivados.docx




THOMSON REUTERS

Módulo PRODEPE

Livro de Apuração do ICMS – Não Incentivados


Localização: Menu Estadual, Módulo Prodepe, item Obrigações à Apuração do ICMS à Não Incentivados

DOCUMENTO DE REQUISITO




REGRAS DE NEGÓCIO









[MFS74877] Tratamento do parâmetro que define a forma de gerar as informações para o Item Principal Saídas, somente para o Incentivo de Central de Distribuição.

Recuperação das notas fiscais para a geração do livro - Item Principal Saídas:
Empresa – código da empresa do login;
Estabelecimento – código do estabelecimento selecionado para geração;
Data Fiscal – data enquadrada no período de apuração;
Somente notas de Saída (MOVTO_E_S = ‘9’);
Somente notas não canceladas;
Classificação do Documento Fiscal igual a 1, 3 ou 4;
Nota que não tenham situação especial igual a ‘1’ ou ‘8’ (IND_SITUACAO_ESP <> ‘1’ ou ‘8’);
Nota que não seja de Transferência (IND_TRANSF_CRED = ’0’)
- Produto parametrizado para Produto Incentivado – Central de Distribuição

- Geração do livro - Regra Específica para Incentivo – Central de Distribuição:
- Se o parâmetro “Demonstrar Somente Operações Incentivadas nos Livros Incentivados” informado na tela de Regras de Incentivo** estiver
- desmarcado, para o grupo de incentivo “Central de Distribuição” referente ao produto da nota
- Serão consideradas todas as notas que não estão gravadas na tabela de Incentivo das Notas Fiscais (ICT_GUIA_INCENT) e que atendam às
- regras de recuperação
- Senão
- Serão consideradas todas as notas que não estão gravadas na tabela de Incentivo das Notas Fiscais (ICT_GUIA_INCENT) e que atendam às
- regras de recuperação. Também serão consideradas as notas gravadas na tabela de Incentivo das Notas Fiscais, que não tem a operação
- (CFOP/Natureza) parametrizada (IND_INCENT = ‘N’).

- ** Menu: Parâmetros à Incentivo – Central de Distribuição à Regras de Incentivo

Como identificar que o produto pertence ao grupo de incentivo – Central de Distribuição: o produto relacionado na nota fiscal vai estar cadastrado na parametrização de Produto Incentivado – Central de Distribuição, para um grupo de incentivo específico.  Este grupo é que vai indicar o tipo de incentivo, através do campo Tipo de Incentivo que deve ser igual a “Central de Distribuição’ (IND_GRP_ESP= ‘3’), da tabela de Grupos de Incentivo (ICT_GRP_INCENT).

Importante à A regra acima que define qual o tipo de nota deve ser gerada no livro incentivado deve ser usada em todas as etapas de geração do Livro (Principal Saídas, Resumo, Resumo p/ Alíquota...).



[MFS83974] Tratamento do parâmetro que define a forma de gerar as informações para o Item Principal, somente para o Incentivo da Indústria.

Recuperação das notas fiscais para a conferência do livro - Item Principal Saídas:
Empresa – código da empresa do login;
Estabelecimento – código do estabelecimento selecionado para geração;
Data Fiscal – data enquadrada no período de apuração;
Classificação do Documento Fiscal igual a 1, 3 ou 4;
Nota que não seja de Transferência (IND_TRANSF_CRED = ’0’)
- Produto não parametrizado para Produto Incentivado – Indústria

- Regra Específica para Incentivo – Indústria:
- Se o parâmetro “Demonstrar Somente Operações Incentivadas nos Livros Incentivados” informado na tela de Regras de Incentivo** estiver
- desmarcado, para o grupo de incentivo “Indústria” referente ao produto da nota
- Serão consideradas todas as notas que não estão gravadas na tabela de Incentivo das Notas Fiscais (ICT_GUIA_INCENT) e que atendam às
- regras de recuperação
- Senão
- Serão consideradas todas as notas que não estão gravadas na tabela de Incentivo das Notas Fiscais (ICT_GUIA_INCENT) e que atendam às
- regras de recuperação. Também serão consideradas as notas gravadas na tabela de Incentivo das Notas Fiscais, que não tem a operação
- (CFOP/Natureza) parametrizada (IND_INCENT = ‘N’).

- ** Menu: Parâmetros à Incentivo – Indústria à Regras de Incentivo

Como identificar que o produto pertence ao grupo de incentivo – Indústria: o produto relacionado na nota fiscal vai estar cadastrado na parametrização de Produto Incentivado – Indústria, para um grupo de incentivo específico.  Este grupo é que vai indicar o tipo de incentivo, através do campo Tipo de Incentivo que deve ser igual a “Indústria” (IND_GRP_ESP= nulo), da tabela de Grupos de Incentivo (ICT_GRP_INCENT).


Importante à A regra acima que define qual o tipo de nota deve ser gerada no relatório incentivado deve ser usada em todos os itens de relatório (Principal, Resumo CFO, Resumo p/ Alíquota...).


[MFS600421] Tratamento do parâmetro que define a forma de gerar as informações para o Item Principal, somente para o Incentivo da Importação.

Recuperação das notas fiscais para a conferência do livro - Item Principal Saídas:
Empresa – código da empresa do login;
Estabelecimento – código do estabelecimento selecionado para geração;
Data Fiscal – data enquadrada no período de apuração;
Classificação do Documento Fiscal igual a 1, 3 ou 4;
Nota que não seja de Transferência (IND_TRANSF_CRED = ’0’)
- Produto não parametrizado para Produto Incentivado – Importação

- Regra Específica para Incentivo – Importação:
- Se o parâmetro “Demonstrar Somente Operações Incentivadas nos Livros Incentivados” informado na tela de Regras de Incentivo** estiver
- desmarcado, para o grupo de incentivo “Importação” referente ao produto da nota
- Serão consideradas todas as notas que não estão gravadas na tabela de Incentivo das Notas Fiscais (ICT_GUIA_INCENT) e que atendam às
- regras de recuperação
- Senão
- Serão consideradas todas as notas que não estão gravadas na tabela de Incentivo das Notas Fiscais (ICT_GUIA_INCENT) e que atendam às
- regras de recuperação. Também serão consideradas as notas gravadas na tabela de Incentivo das Notas Fiscais, que não tem a operação
- (CFOP/Natureza) parametrizada (IND_INCENT = ‘N’).

- ** Menu: Parâmetros à Incentivo – Importação à Regras de Incentivo

Como identificar que o produto pertence ao grupo de incentivo – Importação: o produto relacionado na nota fiscal vai estar cadastrado na parametrização de Produto Incentivado – Importação, para um grupo de incentivo específico.  Este grupo é que vai indicar o tipo de incentivo, através do campo Tipo de Incentivo que deve ser igual a “Importação” (IND_GRP_ESP= ‘2’), da tabela de Grupos de Incentivo (ICT_GRP_INCENT).


Importante:  A regra acima que define qual o tipo de nota deve ser gerada no relatório incentivado deve ser usada em todos os itens de relatório (Principal, Resumo CFO, Resumo p/ Alíquota...).



[MFS62923] Cálculo de Proporcionalidade para o livro de Não incentivado – Industria

Modalidade de Incentivo: Regra específica do cálculo do incentivo da Indústria.

Inclusão de regra de tratamento para geração do Livro de Apuração de ICMS, do item “Principal Entradas”, para os CFOP’s parametrizado na tela “Cálculo de Proporcionalidade – Por CFOP”, devem serem rateados proporcionalmente de acordo com o percentual das saídas, na rotina de geração do Livros Não Incentivados no Módulo do Prodepe.

Embasamento legal: De acordo com o disposto nas alíneas “c” e “e” do inciso VIII do Art. 1º da Portaria 239/01.



Cálculo de Proporcionalidade – Por CFOP:

O tratamento deverá ser efetuado no momento de geração das “Principal Entradas”, o programa deverá consultar se o CFOP está parametrizado na tela “Cálculo de Proporcionalidade - Por CFOP” e se caso estiver, aplicar o fator de rateio proporcional de acordo com o percentual das saídas, que deverá ser recuperado da tabela ICT_TOT_SAIDA_INCE, o percentual que será utilizado corresponde ao campo VLR_PERC_SAI.

Obs* Estes percentuais da tabela ICT_TOT_SAIDA_INCE são previamente calculados no menu “Cálculo da Proporção das Saídas”.



Tratamento:

Livro Não Incentivados - Principais Entradas:

Se o CFOP estiver preenchido na tela “Cálculo de Proporcionalidade - Por CFOP”
E o campo de SERIE_LIVRO da tabela ICT_TOT_SAIDA_INC for igual à “A”
E o campo de SUB_SERIE_LIVRO da tabela ICT_TOT_SAIDA_INCE igual ao campo SUB_SERIE_LIVRO da tabela ICT_FAIXA_INCENT;
E o campo COD_GRP_INCENT da tabela ICT_TOT_SAIDA_INCE igual ao campo COD_GRP_INCENT LIVRO da tabela ICT_FAIXA_INCENT;
Aplicar o rateio proporcional com o percentual do campo VLR_PERC_SAI, nos campos abaixo se preenchido:

- valor da Coluna “Valores Contábeis”: (VLR_CONTABIL * VLR_PERC_SAI) / 100
- valor da coluna “Base de Cálculo”: (VLR_BASE * VLR_PERC_SAI) / 100
- valor da coluna “Imposto Creditado”: (VLR_IMPOSTO * VLR_PERC_SAI) / 100
- valor da coluna “Isentas ou Não Tributadas”: (VLR_ISENTAS * VLR_PERC_SAI) / 100
- valor da coluna “Outras”: (VLR_OUTRAS * VLR_PERC_SAI) / 100





Importante à É importante garantir que o valor já esteja preenchido corretamente na montagem do item “Principais Entradas” para prosseguir sem impactos nas próximas etapas de geração do Livro, (Resumo da Apuração, Demonstrativos do Prodepe).






= = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS62923 | Tratamento de CFOP – Livro Não Incentivado | O objetivo dessa demanda é incluir tratamento para os CFOP’s que obrigatoriamente necessitam serem rateados proporcionalmente entre os livros Incentivados e Não Incentivados. (Processo será com base na nova tela de parâmetros) Industria. |  |
| MFS74877 | Andréa Rocha | Tratamento do parâmetro específico para Central de Distribuição que trata de um regime especial, que vai definir a forma de gerar o produto incentivado sem operação incentivada na geração do livro de apuração. | 12/11/2021 |
| MFS83974 | Andréa Rocha | Tratamento do parâmetro específico para Indústria, que vai definir a forma de gerar o produto incentivado sem operação incentivada na geração do livro de apuração. | 19/05/2021 |
| MFS600421 | Andréa Rocha | Tratamento do parâmetro específico para Importação, que vai definir a forma de gerar o produto incentivado sem operação incentivada na geração do livro de apuração. | 16/01/2024 |


| RN00 | Regras Gerais |
| --- | --- |


| RN01 | Parâmetros de Tela |
| --- | --- |


| RN02 | Recuperação dos Dados – Incentivo - Central de Distribuição |
| --- | --- |


| RN02a | Recuperação dos Dados - Incentivo – Indústria |
| --- | --- |


| RN02b | Recuperação dos Dados - Incentivo – Importação |
| --- | --- |


| RN03 | Tratamento Cálculo de Proporcionalidade – Por CFOP – Item Principais Entradas - INDÚSTRIA |
| --- | --- |


| RN04 |  |
| --- | --- |
