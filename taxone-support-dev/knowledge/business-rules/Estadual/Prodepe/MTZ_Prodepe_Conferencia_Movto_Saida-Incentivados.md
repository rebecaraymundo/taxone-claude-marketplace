# MTZ_Prodepe_Conferencia_Movto_Saida-Incentivados

- **Fonte:** MTZ_Prodepe_Conferencia_Movto_Saida-Incentivados.docx
- **Modificado:** 2024-01-18
- **Tamanho:** 67 KB

---

THOMSON REUTERS

                                                                                     __Módulo PRODEPE__

__  __

__Conferência dos Movimento de Saídas – Incentivados__

__Localização__: Menu Estadual, Módulo Prodepe, item Obrigações à Conferência Entradas / Saídas <a id="_Hlk87627679"></a>🡪 Movimento de Saída 🡪 Incentivados 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS74877__

Andréa Rocha

Tratamento do parâmetro específico para Central de Distribuição que trata de um regime especial, que vai definir a forma de gerar o produto incentivado sem operação incentivada na geração do livro de saída\.

16/11/2021

__MFS83974__

Andréa Rocha

Tratamento do parâmetro específico para Indústria, que vai definir a forma de gerar o produto incentivado sem operação incentivada na geração do livro de saída\.

19/05/2021

__MFS604311__

Andréa Rocha

Tratamento do parâmetro específico para Importação, que vai definir a forma de gerar o produto incentivado sem operação incentivada na conferência de saída\.

19/01/2024

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

  

__RN01__

__                                                        Parâmetros de Tela__

__RN02__

__Recuperação dos Dados – Incentivo \- Central de Distribuição__

__\[MFS74877\] __Tratamento do parâmetro que define a forma de gerar as informações para o Item Principal, somente para o Incentivo de Central de Distribuição\. 

Recuperação das notas fiscais para a conferência dos movimentos de saídas \- Item Principal:

- Empresa – código da empresa do login; 
- Estabelecimento – código do estabelecimento selecionado para geração; 
- Data Fiscal – data enquadrada no período de apuração; 
- Somente notas de Saída \(MOVTO\_E\_S = ‘9’\);
- Classificação do Documento Fiscal igual a 1, 3 ou 4;
- Nota que não seja de Transferência \(IND\_TRANSF\_CRED = ’0’\)
- [Produto](#ProdutoouNCMsujeitosaICMSST) parametrizado para Produto Incentivado – Central de Distribuição 
- Notas que estejam gravadas na tabela de Incentivo das Notas Fiscais \(ICT\_GUIA\_INCENT\)

 Regra Específica para Incentivo – Central de Distribuição:

       Se o parâmetro “Demonstrar Somente Operações Incentivadas nos Livros Incentivados” informado na tela de Regras de Incentivo\*\* estiver 

            desmarcado, para o grupo de incentivo “Central de Distribuição” referente ao produto da nota

            Serão consideradas todas as notas gravadas na tabela de Incentivo das Notas Fiscais, independente da operação \(CFOP/Natureza\) ser  

             parametrizada ou não \(IND\_INCENT = ‘N’ ou ‘I’\)

       Senão

            Serão consideradas somente as notas gravadas na tabela de Incentivo das Notas Fiscais que são consideradas incentivadas \(IND\_INCENT 

            = ‘I’\), ou seja, são as notas que têm o CFOP ou CFOP/Natureza de Operação parametrizado para em CFOP/Natureza Incentivados\.

__\*\*__ Menu: Parâmetros 🡪 Incentivo – Central de Distribuição 🡪 Regras de Incentivo

Como identificar que o produto pertence ao grupo de incentivo – Central de Distribuição: o produto relacionado na nota fiscal vai estar cadastrado na parametrização de Produto Incentivado – Central de Distribuição, para um grupo de incentivo específico\.  Este grupo é que vai indicar o tipo de incentivo, através do campo Tipo de Incentivo que deve ser igual a “Central de Distribuição’ \(IND\_GRP\_ESP= ‘3’\), da tabela de Grupos de Incentivo \(ICT\_GRP\_INCENT\)\.

Importante à A regra acima que define qual o tipo de nota deve ser gerada no relatório incentivado deve ser usada em todos os itens de relatório \(Principal, Resumo CFO, Resumo p/ Alíquota\.\.\.\)\.

__RN03__

__Recuperação dos Dados \- Incentivo – Indústria__

__\[MFS83974\] __Tratamento do parâmetro que define a forma de gerar as informações para o Item Principal, somente para o Incentivo da Indústria\. 

Recuperação das notas fiscais para a conferência dos movimentos de saídas \- Item Principal:

- Empresa – código da empresa do login; 
- Estabelecimento – código do estabelecimento selecionado para geração; 
- Data Fiscal – data enquadrada no período de apuração; 
- Somente notas de Saída \(MOVTO\_E\_S = ‘9’\);
- Classificação do Documento Fiscal igual a 1, 3 ou 4;
- Nota que não seja de Transferência \(IND\_TRANSF\_CRED = ’0’\)
- [Produto](#ProdutoouNCMsujeitosaICMSST) parametrizado para Produto Incentivado – Indústria 
- Notas que estejam gravadas na tabela de Incentivo das Notas Fiscais \(ICT\_GUIA\_INCENT\)

 Regra Específica para Incentivo – Indústria:

       Se o parâmetro “Demonstrar Somente Operações Incentivadas nos Livros Incentivados” informado na tela de Regras de Incentivo\*\* estiver 

            desmarcado, para o grupo de incentivo “Indústria” referente ao produto da nota

            Serão consideradas todas as notas gravadas na tabela de Incentivo das Notas Fiscais, independente da operação \(CFOP/Natureza\) ser  

             parametrizada ou não \(IND\_INCENT = ‘N’ ou ‘I’\)

       Senão

            Serão consideradas somente as notas gravadas na tabela de Incentivo das Notas Fiscais que são consideradas incentivadas \(IND\_INCENT 

            = ‘I’\), ou seja, são as notas que têm o CFOP ou CFOP/Natureza de Operação parametrizado para em CFOP/Natureza Incentivados\.

__\*\*__ Menu: Parâmetros 🡪 Incentivo – Indústria 🡪 Regras de Incentivo

Como identificar que o produto pertence ao grupo de incentivo – Indústria: o produto relacionado na nota fiscal vai estar cadastrado na parametrização de Produto Incentivado – Indústria, para um grupo de incentivo específico\.  Este grupo é que vai indicar o tipo de incentivo, através do campo Tipo de Incentivo que deve ser igual a “Indústria” \(IND\_GRP\_ESP= nulo\), da tabela de Grupos de Incentivo \(ICT\_GRP\_INCENT\)\.

Importante à A regra acima que define qual o tipo de nota deve ser gerada no relatório incentivado deve ser usada em todos os itens de relatório \(Principal, Resumo CFO, Resumo p/ Alíquota\.\.\.\)\.

__RN04__

__Recuperação dos Dados \- Incentivo – Importação__

__\[MFS604311\] __Tratamento do parâmetro que define a forma de gerar as informações para o Item Principal, somente para o Incentivo da Importação\. 

Recuperação das notas fiscais para a conferência dos movimentos de saídas \- Item Principal:

- Empresa – código da empresa do login; 
- Estabelecimento – código do estabelecimento selecionado para geração; 
- Data Fiscal – data enquadrada no período de apuração; 
- Somente notas de Saída \(MOVTO\_E\_S = ‘9’\);
- Classificação do Documento Fiscal igual a 1, 3 ou 4;
- Nota que não seja de Transferência \(IND\_TRANSF\_CRED = ’0’\)
- [Produto](#ProdutoouNCMsujeitosaICMSST) parametrizado para Produto Incentivado – Importação
- Notas que estejam gravadas na tabela de Incentivo das Notas Fiscais \(ICT\_GUIA\_INCENT\)

 Regra Específica para Incentivo – Importação:

       Se o parâmetro “Demonstrar Somente Operações Incentivadas nos Livros Incentivados” informado na tela de Regras de Incentivo\*\* estiver 

            desmarcado, para o grupo de incentivo “Importação” referente ao produto da nota

            Serão consideradas todas as notas gravadas na tabela de Incentivo das Notas Fiscais, independente da operação \(CFOP/Natureza\) ser  

             parametrizada ou não \(IND\_INCENT = ‘N’ ou ‘I’\)

       Senão

            Serão consideradas somente as notas gravadas na tabela de Incentivo das Notas Fiscais que são consideradas incentivadas \(IND\_INCENT 

            = ‘I’\), ou seja, são as notas que têm o CFOP ou CFOP/Natureza de Operação parametrizado para em CFOP/Natureza Incentivados\.

__\*\*__ Menu: Parâmetros 🡪 Incentivo – Importação 🡪 Regras de Incentivo

Como identificar que o produto pertence ao grupo de incentivo – Importação: o produto relacionado na nota fiscal vai estar cadastrado na parametrização de Produto Incentivado – Importação, para um grupo de incentivo específico\.  Este grupo é que vai indicar o tipo de incentivo, através do campo Tipo de Incentivo que deve ser igual a “Indústria” \(IND\_GRP\_ESP= ‘2’\), da tabela de Grupos de Incentivo \(ICT\_GRP\_INCENT\)\.

Importante à A regra acima que define qual o tipo de nota deve ser gerada no relatório incentivado deve ser usada em todos os itens de relatório \(Principal, Resumo CFO, Resumo p/ Alíquota\.\.\.\)\.

        = = = = =

