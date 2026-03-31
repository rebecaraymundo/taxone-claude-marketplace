# MTZ_Prodepe_Livro_Saida-Não_Incentivados

> Fonte: MTZ_Prodepe_Livro_Saida-Não_Incentivados.docx




THOMSON REUTERS

Módulo PRODEPE

Livro de Saída – Não Incentivados


Localização: Menu Estadual, Módulo Prodepe, item Obrigações  Livro Registro Saídas  Modelo P2  Não Incentivados

DOCUMENTO DE REQUISITO




REGRAS DE NEGÓCIO









[MFS74877] Tratamento do parâmetro que define a forma de gerar as informações para o Item Principal, somente para o Incentivo de Central de Distribuição.

Recuperação das notas fiscais para a geração do livro - Item Principal Saídas:
Empresa – código da empresa do login;
Estabelecimento – código do estabelecimento selecionado para geração;
Data Fiscal – data enquadrada no período de apuração;
Somente notas de Saída (MOVTO_E_S = ‘9’);
Classificação do Documento Fiscal igual a 1, 3 ou 4;
Nota que não seja de Transferência (IND_TRANSF_CRED = ’0’)
- Produto não parametrizado para Produto Incentivado

- Geração do livro - Regra Específica para Incentivo – Central de Distribuição:
- Se o parâmetro “Demonstrar Somente Operações Incentivadas nos Livros Incentivados” informado na tela de Regras de Incentivo** estiver
- desmarcado, para o grupo de incentivo “Central de Distribuição” referente ao produto da nota
- Serão consideradas todas as notas que não estão gravadas na tabela de Incentivo das Notas Fiscais (ICT_GUIA_INCENT) e que atendam às
- regras de recuperação
- Senão
- Serão consideradas todas as notas que não estão gravadas na tabela de Incentivo das Notas Fiscais (ICT_GUIA_INCENT) e que atendam às
- regras de recuperação. Também serão consideradas as notas gravadas na tabela de Incentivo das Notas Fiscais, que não tem a operação
- (CFOP/Natureza) parametrizada (IND_INCENT = ‘N’).

- ** Menu: Parâmetros  Incentivo – Central de Distribuição  Regras de Incentivo

Como identificar que o produto pertence ao grupo de incentivo – Central de Distribuição: o produto relacionado na nota fiscal vai estar cadastrado na parametrização de Produto Incentivado – Central de Distribuição, para um grupo de incentivo específico.  Este grupo é que vai indicar o tipo de incentivo, através do campo Tipo de Incentivo que deve ser igual a “Central de Distribuição’ (IND_GRP_ESP= ‘3’), da tabela de Grupos de Incentivo (ICT_GRP_INCENT).

Importante à A regra acima que define qual o tipo de nota deve ser gerada no livro incentivado deve ser usada em todas as etapas de geração do Livro (Principal, Resumo CFO, Resumo p/ Alíquota...).


[MFS83974] Tratamento do parâmetro que define a forma de gerar as informações para o Item Principal, somente para o Incentivo da Indústria.

Recuperação das notas fiscais para a geração do livro - Item Principal Saídas:
Empresa – código da empresa do login;
Estabelecimento – código do estabelecimento selecionado para geração;
Data Fiscal – data enquadrada no período de apuração;
Somente notas de Saída (MOVTO_E_S = ‘9’);
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

- ** Menu: Parâmetros  Incentivo – Indústria  Regras de Incentivo

Como identificar que o produto pertence ao grupo de incentivo – Indústria: o produto relacionado na nota fiscal vai estar cadastrado na parametrização de Produto Incentivado – Indústria, para um grupo de incentivo específico.  Este grupo é que vai indicar o tipo de incentivo, através do campo Tipo de Incentivo que deve ser igual a “Indústria” (IND_GRP_ESP= nulo), da tabela de Grupos de Incentivo (ICT_GRP_INCENT).


Importante à A regra acima que define qual o tipo de nota deve ser gerada no relatório incentivado deve ser usada em todos os itens de relatório (Principal, Resumo CFO, Resumo p/ Alíquota...).


[MFS600421] Tratamento do parâmetro que define a forma de gerar as informações para o Item Principal, somente para o Incentivo da Importação.

Recuperação das notas fiscais para a geração do livro - Item Principal Saídas:
Empresa – código da empresa do login;
Estabelecimento – código do estabelecimento selecionado para geração;
Data Fiscal – data enquadrada no período de apuração;
Somente notas de Saída (MOVTO_E_S = ‘9’);
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

- ** Menu: Parâmetros  Incentivo – Importação  Regras de Incentivo

Como identificar que o produto pertence ao grupo de incentivo – Importação: o produto relacionado na nota fiscal vai estar cadastrado na parametrização de Produto Incentivado – Importação, para um grupo de incentivo específico.  Este grupo é que vai indicar o tipo de incentivo, através do campo Tipo de Incentivo que deve ser igual a “Importação” (IND_GRP_ESP= ‘2’), da tabela de Grupos de Incentivo (ICT_GRP_INCENT).


Importante à A regra acima que define qual o tipo de nota deve ser gerada no relatório incentivado deve ser usada em todos os itens de relatório (Principal, Resumo CFO, Resumo p/ Alíquota...).

= = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS74877 | Andréa Rocha | Tratamento do parâmetro específico para Central de Distribuição que trata de um regime especial, que vai definir a forma de gerar o produto incentivado sem operação incentivada na geração do livro de saída. | 12/11/2021 |
| MFS83974 | Andréa Rocha | Tratamento do parâmetro específico para Indústria, que vai definir a forma de gerar o produto incentivado sem operação incentivada na geração do livro de saída. | 19/05/2021 |
| MFS600421 | Andréa Rocha | Tratamento do parâmetro específico para Importação, que vai definir a forma de gerar o produto incentivado sem operação incentivada na geração do livro de saída. | 16/01/2024 |


| RN00 | Regras Gerais |
| --- | --- |


| RN01 | Parâmetros de Tela |
| --- | --- |


| RN02 | Recuperação dos Dados – Incentivo - Central de Distribuição |
| --- | --- |


| RN03 | Recuperação dos Dados - Incentivo – Indústria |
| --- | --- |


| RN04 | Recuperação dos Dados - Incentivo – Importação |
| --- | --- |
