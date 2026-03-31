# MTZ_Prodepe_Livro_Saida-Não_Incentivados

- **Fonte:** MTZ_Prodepe_Livro_Saida-Não_Incentivados.docx
- **Modificado:** 2024-01-18
- **Tamanho:** 68 KB

---

THOMSON REUTERS

                                                                                     __Módulo PRODEPE__

__  __

__                                             Livro de Saída – Não Incentivados __

__Localização__: Menu Estadual, Módulo Prodepe, item Obrigações 🡪 Livro Registro Saídas 🡪 Modelo P2 🡪 Não Incentivados 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS74877__

Andréa Rocha

Tratamento do parâmetro específico para Central de Distribuição que trata de um regime especial, que vai definir a forma de gerar o produto incentivado sem operação incentivada na geração do livro de saída\.

12/11/2021

__MFS83974__

Andréa Rocha

Tratamento do parâmetro específico para Indústria, que vai definir a forma de gerar o produto incentivado sem operação incentivada na geração do livro de saída\.

19/05/2021

__MFS600421__

Andréa Rocha

Tratamento do parâmetro específico para Importação, que vai definir a forma de gerar o produto incentivado sem operação incentivada na geração do livro de saída\.

16/01/2024

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

  

__RN01__

__                                                        Parâmetros de Tela__

__RN02__

__Recuperação dos Dados – Incentivo \- Central de Distribuição__

__\[MFS74877\] __Tratamento do parâmetro que define a forma de gerar as informações para o Item Principal, somente para o Incentivo de Central de Distribuição\. 

Recuperação das notas fiscais para a geração do livro \- Item Principal Saídas:

- Empresa – código da empresa do login; 
- Estabelecimento – código do estabelecimento selecionado para geração; 
- Data Fiscal – data enquadrada no período de apuração; 
- Somente notas de Saída \(MOVTO\_E\_S = ‘9’\);
- Classificação do Documento Fiscal igual a 1, 3 ou 4;
- Nota que não seja de Transferência \(IND\_TRANSF\_CRED = ’0’\)
- [Produto](#ProdutoouNCMsujeitosaICMSST) não parametrizado para Produto Incentivado 

 Geração do livro \- Regra Específica para Incentivo – Central de Distribuição:

       Se o parâmetro “Demonstrar Somente Operações Incentivadas nos Livros Incentivados” informado na tela de Regras de Incentivo\*\* estiver 

            desmarcado, para o grupo de incentivo “Central de Distribuição” referente ao produto da nota

            Serão consideradas todas as notas que não estão gravadas na tabela de Incentivo das Notas Fiscais \(ICT\_GUIA\_INCENT\) e que atendam às 

            regras de recuperação 

       Senão

            Serão consideradas todas as notas que não estão gravadas na tabela de Incentivo das Notas Fiscais \(ICT\_GUIA\_INCENT\) e que atendam às 

            regras de recuperação\. Também serão consideradas as notas gravadas na tabela de Incentivo das Notas Fiscais, que não tem a operação 

            \(CFOP/Natureza\) parametrizada \(IND\_INCENT = ‘N’\)\.

__\*\*__ Menu: Parâmetros 🡪 Incentivo – Central de Distribuição 🡪 Regras de Incentivo

Como identificar que o produto pertence ao grupo de incentivo – Central de Distribuição: o produto relacionado na nota fiscal vai estar cadastrado na parametrização de Produto Incentivado – Central de Distribuição, para um grupo de incentivo específico\.  Este grupo é que vai indicar o tipo de incentivo, através do campo Tipo de Incentivo que deve ser igual a “Central de Distribuição’ \(IND\_GRP\_ESP= ‘3’\)<a id="_Hlk87618865"></a>, da tabela de Grupos de Incentivo \(ICT\_GRP\_INCENT\)\.

Importante à A regra acima que define qual o tipo de nota deve ser gerada no livro incentivado deve ser usada em todas as etapas de geração do Livro \(Principal, Resumo CFO, Resumo p/ Alíquota\.\.\.\)\.

__RN03__

__Recuperação dos Dados \- Incentivo – Indústria__

__\[MFS83974\] __Tratamento do parâmetro que define a forma de gerar as informações para o Item Principal, somente para o Incentivo da Indústria\. 

Recuperação das notas fiscais para a geração do livro \- Item Principal Saídas:

- Empresa – código da empresa do login; 
- Estabelecimento – código do estabelecimento selecionado para geração; 
- Data Fiscal – data enquadrada no período de apuração; 
- Somente notas de Saída \(MOVTO\_E\_S = ‘9’\);
- Classificação do Documento Fiscal igual a 1, 3 ou 4;
- Nota que não seja de Transferência \(IND\_TRANSF\_CRED = ’0’\)
- [Produto](#ProdutoouNCMsujeitosaICMSST) não parametrizado para Produto Incentivado – Indústria 

 Regra Específica para Incentivo – Indústria:

Se o parâmetro “Demonstrar Somente Operações Incentivadas nos Livros Incentivados” informado na tela de Regras de Incentivo\*\* estiver 

            desmarcado, para o grupo de incentivo “Indústria” referente ao produto da nota

            Serão consideradas todas as notas que não estão gravadas na tabela de Incentivo das Notas Fiscais \(ICT\_GUIA\_INCENT\) e que atendam às 

            regras de recuperação 

       Senão

            Serão consideradas todas as notas que não estão gravadas na tabela de Incentivo das Notas Fiscais \(ICT\_GUIA\_INCENT\) e que atendam às 

            regras de recuperação\. Também serão consideradas as notas gravadas na tabela de Incentivo das Notas Fiscais, que não tem a operação 

            \(CFOP/Natureza\) parametrizada \(IND\_INCENT = ‘N’\)\.

__\*\*__ Menu: Parâmetros 🡪 Incentivo – Indústria 🡪 Regras de Incentivo

Como identificar que o produto pertence ao grupo de incentivo – Indústria: o produto relacionado na nota fiscal vai estar cadastrado na parametrização de Produto Incentivado – Indústria, para um grupo de incentivo específico\.  Este grupo é que vai indicar o tipo de incentivo, através do campo Tipo de Incentivo que deve ser igual a “Indústria” \(IND\_GRP\_ESP= nulo\), da tabela de Grupos de Incentivo \(ICT\_GRP\_INCENT\)\.

Importante à A regra acima que define qual o tipo de nota deve ser gerada no relatório incentivado deve ser usada em todos os itens de relatório \(Principal, Resumo CFO, Resumo p/ Alíquota\.\.\.\)\.

__RN04__

__Recuperação dos Dados \- Incentivo – Importação__

__\[MFS600421\] __Tratamento do parâmetro que define a forma de gerar as informações para o Item Principal, somente para o Incentivo da Importação\. 

Recuperação das notas fiscais para a geração do livro \- Item Principal Saídas:

- Empresa – código da empresa do login; 
- Estabelecimento – código do estabelecimento selecionado para geração; 
- Data Fiscal – data enquadrada no período de apuração; 
- Somente notas de Saída \(MOVTO\_E\_S = ‘9’\);
- Classificação do Documento Fiscal igual a 1, 3 ou 4;
- Nota que não seja de Transferência \(IND\_TRANSF\_CRED = ’0’\)
- [Produto](#ProdutoouNCMsujeitosaICMSST) não parametrizado para Produto Incentivado – Importação

 Regra Específica para Incentivo – Importação:

Se o parâmetro “Demonstrar Somente Operações Incentivadas nos Livros Incentivados” informado na tela de Regras de Incentivo\*\* estiver 

            desmarcado, para o grupo de incentivo “Importação” referente ao produto da nota

            Serão consideradas todas as notas que não estão gravadas na tabela de Incentivo das Notas Fiscais \(ICT\_GUIA\_INCENT\) e que atendam às 

            regras de recuperação 

       Senão

            Serão consideradas todas as notas que não estão gravadas na tabela de Incentivo das Notas Fiscais \(ICT\_GUIA\_INCENT\) e que atendam às 

            regras de recuperação\. Também serão consideradas as notas gravadas na tabela de Incentivo das Notas Fiscais, que não tem a operação 

            \(CFOP/Natureza\) parametrizada \(IND\_INCENT = ‘N’\)\.

__\*\*__ Menu: Parâmetros 🡪 Incentivo – Importação 🡪 Regras de Incentivo

Como identificar que o produto pertence ao grupo de incentivo – Importação: o produto relacionado na nota fiscal vai estar cadastrado na parametrização de Produto Incentivado – Importação, para um grupo de incentivo específico\.  Este grupo é que vai indicar o tipo de incentivo, através do campo Tipo de Incentivo que deve ser igual a “Importação” \(IND\_GRP\_ESP= ‘2’\), da tabela de Grupos de Incentivo \(ICT\_GRP\_INCENT\)\.

Importante à A regra acima que define qual o tipo de nota deve ser gerada no relatório incentivado deve ser usada em todos os itens de relatório \(Principal, Resumo CFO, Resumo p/ Alíquota\.\.\.\)\.

        = = = = =

