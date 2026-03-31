# MTZ_Prodepe_Livro de Registro de Entradas

- **Fonte:** MTZ_Prodepe_Livro de Registro de Entradas.docx
- **Modificado:** 2024-01-18
- **Tamanho:** 68 KB

---

THOMSON REUTERS

                                                                                     __Módulo PRODEPE__

__  __

__Livro de Registro de Entradas__

__Localização__: Menu Estadual, Módulo Prodepe, item Obrigações 🡪 Livro de Registros de Entradas

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS62923__

Tratamento de CFOP – Rateio Proporcional – Livro Incentivado

O objetivo dessa demanda é incluir tratamento para os CFOP’s que obrigatoriamente necessitam serem rateados proporcionalmente entre os Livros Incentivados e Não Incentivado\. \(Processo será com base na nova tela de parâmetros\) Industria\. RN02\.a e RN02\.b\.

26/04/2021

__MFS74877__

Andréa Rocha

Tratamento do parâmetro específico para Central de Distribuição que trata de um regime especial, que vai definir a forma de gerar o produto incentivado sem operação incentivada na geração do livro de entrada\.

12/11/2021

__MFS83974__

Andréa Rocha

Tratamento do parâmetro específico para Indústria, que vai definir a forma de gerar o produto incentivado sem operação incentivada na geração do livro de entrada\.

23/05/2022

__MFS600421__

Andréa Rocha

Tratamento do parâmetro específico para Importação, que vai definir a forma de gerar o produto incentivado sem operação incentivada na geração do livro de entrada\.

16/01/2024

REGRAS DE NEGÓCIO

__RN01\.a__

__Tratamento Cálculo de Proporcionalidade – Por CFOP – Livro de Registro de Entradas – Incentivados – P1 e P1A \- INDÚSTRIA__

\[__MFS62923__\] Cálculo de Proporcionalidade para o Livro de Registros de Entradas Incentivado – P1 e P1A \- Industria

<a id="_Hlk70443933"></a><a id="_Hlk70443899"></a>Modalidade de Incentivo: Regra específica do cálculo do incentivo da Indústria\.

Inclusão de regra de tratamento da geração do Livro de Registros de Entradas para os CFOP’s parametrizado na tela “Cálculo de Proporcionalidade – Por CFOP”, devem serem rateados proporcionalmente de acordo com o percentual das saídas, na rotina de geração dos Livros Incentivados no Módulo do Prodepe\. 

__Embasamento legal:__ De acordo com o disposto nas alíneas “c” e “e” do inciso VIII do Art\. 1º da Portaria 239/01\.

__Cálculo de Proporcionalidade – Por CFOP__:

 

O tratamento deverá ser efetuado no momento da geração do Livro de Registros de Entradas, o programa deverá consultar se o CFOP está parametrizado na tela “Cálculo de Proporcionalidade \-Por CFOP” e se caso estiver, aplicar o fator de rateio proporcional de acordo com o percentual das saídas, que deverá ser recuperado da tabela ICT\_TOT\_SAIDA\_INCE, o percentual que será utilizado corresponde ao campo VLR\_PERC\_SAI\. 

Obs\* *Estes percentuais *da tabela *ICT\_TOT\_SAIDA\_INCE são previamente calculados no menu “Cálculo da Proporção das Saídas”\.*

__Tratamento__: 

Conferência das Entradas \- Incentivados:

__Se__ o CFOP estiver preenchido na tela “Cálculo de Proporcionalidade \- Por CFOP” 

  __E__ o campo de SERIE\_LIVRO da tabela ICT\_TOT\_SAIDA\_INC for igual à “B” 

    __E __o campo de SUB\_SERIE\_LIVRO da tabela ICT\_TOT\_SAIDA\_INCE igual ao campo SUB\_SERIE\_LIVRO da tabela ICT\_FAIXA\_INCENT;

     __E __o campo COD\_GRP\_INCENT da tabela ICT\_TOT\_SAIDA\_INCE igual ao campo COD\_GRP\_INCENT LIVRO da tabela ICT\_FAIXA\_INCENT;

__Aplicar__ o rateio proporcional com o percentual do campo VLR\_PERC\_SAI, nos campos de valores \(Valor Contábil, Base de Cálculo e Imposto Creditado\), dos campos preenchidos:

VALOR CONTÁBIL = VLR\_CONTABIL \* VLR\_PERC\_SAI \) / 100

BASE DE CÁLCULO = BASE\* VLR\_PERC\_SAI \) / 100

IMPOSTO CREDITADO = IMPOSTO \* VLR\_PERC\_SAI \) / 100

__RN01\.b__

__Tratamento Cálculo de Proporcionalidade – Por CFOP – Livro de Registro de Entradas – Não Incentivados – P1 e P1A \- INDÚSTRIA__

\[__MFS62923__\] Cálculo de Proporcionalidade para o Livro de Registros de Entradas Não Incentivado – P1 e P1A \- Industria

Modalidade de Incentivo: Regra específica do cálculo do incentivo da Indústria\.

Inclusão de regra de tratamento da geração do Livro de Registro de Entradas para os CFOP’s parametrizado na tela “Cálculo de Proporcionalidade – Por CFOP”, devem serem rateados proporcionalmente de acordo com o percentual das saídas, na rotina de geração dos Livros Incentivados no Módulo do Prodepe\. 

__Embasamento legal:__ De acordo com o disposto nas alíneas “c” e “e” do inciso VIII do Art\. 1º da Portaria 239/01\.

__Cálculo de Proporcionalidade – Por CFOP__:

 

O tratamento deverá ser efetuado no momento da geração do Livro de Registro de Entradas\., o programa deverá consultar se o CFOP está parametrizado na tela “Cálculo de Proporcionalidade \-Por CFOP” e se caso estiver, aplicar o fator de rateio proporcional de acordo com o percentual das saídas, que deverá ser recuperado da tabela ICT\_TOT\_SAIDA\_INCE, o percentual que será utilizado corresponde ao campo VLR\_PERC\_SAI\. 

Obs\* *Estes percentuais *da tabela *ICT\_TOT\_SAIDA\_INCE são previamente calculados no menu “Cálculo da Proporção das Saídas”\.*

__Tratamento__: 

Conferência das Entradas \- Não Incentivados:

__Se__ o CFOP estiver preenchido na tela “Cálculo de Proporcionalidade \- Por CFOP” 

  __E__ o campo de SERIE\_LIVRO da tabela ICT\_TOT\_SAIDA\_INC for igual à “A” 

    __E __o campo de SUB\_SERIE\_LIVRO da tabela ICT\_TOT\_SAIDA\_INCE igual ao campo SUB\_SERIE\_LIVRO da tabela ICT\_FAIXA\_INCENT;

     __E __o campo COD\_GRP\_INCENT da tabela ICT\_TOT\_SAIDA\_INCE igual ao campo COD\_GRP\_INCENT LIVRO da tabela ICT\_FAIXA\_INCENT;

__Aplicar__ o rateio proporcional com o percentual do campo VLR\_PERC\_SAI, nos campos de valores \(Valor Contábil, Base de Cálculo e Imposto Creditado\), dos campos preenchidos:

VALOR CONTÁBIL = VLR\_CONTABIL \* VLR\_PERC\_SAI \) / 100

BASE DE CÁLCULO = BASE\* VLR\_PERC\_SAI \) / 100

IMPOSTO CREDITADO = IMPOSTO \* VLR\_PERC\_SAI \) / 100

__RN02__

__Recuperação dos Dados – Incentivo \- Central de Distribuição__

__\[MFS74877\] __Tratamento do parâmetro que define a forma de gerar as informações para o Item Principal, somente para o Incentivo de Central de Distribuição\. 

Recuperação das notas fiscais para a geração do livro \- Item Principal:

- Empresa – código da empresa do login; 
- Estabelecimento – código do estabelecimento selecionado para geração; 
- Data Fiscal – data enquadrada no período de apuração; 
- Somente notas de Entrada \(MOVTO\_E\_S <> ‘9’\);
- Classificação do Documento Fiscal igual a 1, 3 ou 4;
- Nota que não seja de Transferência \(IND\_TRANSF\_CRED = ’0’\)
- [Produto](#ProdutoouNCMsujeitosaICMSST) parametrizado para Produto Incentivado – Central de Distribuição 
- Notas que estejam gravadas na tabela de Incentivo das Notas Fiscais \(ICT\_GUIA\_INCENT\)

 Geração do livro \- Regra Específica para Incentivo – Central de Distribuição – Regra para Livro Incentivado:

       Se o parâmetro “Demonstrar Somente Operações Incentivadas nos Livros Incentivados” informado na tela de Regras de Incentivo\*\* estiver 

            desmarcado, para o grupo de incentivo “Central de Distribuição” referente ao produto da nota

            Serão consideradas todas as notas gravadas na tabela de Incentivo das Notas Fiscais, independente da operação \(CFOP/Natureza\) ser  

             parametrizada ou não \(IND\_INCENT = ‘N’ ou ‘I’\)

       Senão

            Serão consideradas somente as notas gravadas na tabela de Incentivo das Notas Fiscais que são consideradas incentivadas \(IND\_INCENT 

            = ‘I’\), ou seja, são as notas que têm o CFOP ou CFOP/Natureza de Operação parametrizado para em CFOP/Natureza Incentivados

Geração do livro \- Regra Específica para Incentivo – Central de Distribuição – Regra para Livro não Incentivado:

       Se o parâmetro “Demonstrar Somente Operações Incentivadas nos Livros Incentivados” informado na tela de Regras de Incentivo\*\* estiver 

            desmarcado, para o grupo de incentivo “Central de Distribuição” referente ao produto da nota

            Serão consideradas todas as notas que não estão gravadas na tabela de Incentivo das Notas Fiscais \(ICT\_GUIA\_INCENT\) e que atendam às 

            regras de recuperação 

       Senão

            Serão consideradas todas as notas que não estão gravadas na tabela de Incentivo das Notas Fiscais \(ICT\_GUIA\_INCENT\) e que atendam às 

            regras de recuperação\. Também serão consideradas as notas gravadas na tabela de Incentivo das Notas Fiscais, que não tem a operação 

            \(CFOP/Natureza\) parametrizada \(IND\_INCENT = ‘N’\)\.

__\*\*__ Menu: Parâmetros 🡪 Incentivo – Central de Distribuição 🡪 Regras de Incentivo

Como identificar que o produto pertence ao grupo de incentivo – Central de Distribuição: o produto relacionado na nota fiscal vai estar cadastrado na parametrização de Produto Incentivado – Central de Distribuição, para um grupo de incentivo específico\.  Este grupo é que vai indicar o tipo de incentivo, através do campo Tipo de Incentivo que deve ser igual a “Central de Distribuição’ \(IND\_GRP\_ESP= ‘3’\), da tabela de Grupos de Incentivo \(ICT\_GRP\_INCENT\)\.

Importante à A regra acima que define qual o tipo de nota deve ser gerada no livro incentivado deve ser usada em todas as etapas de geração do Livro \(Principal, Resumo CFO, Resumo p/ Alíquota\.\.\.\)\.

__RN03__

__Recuperação dos Dados \- Incentivo – Indústria__

__\[MFS83974\] __Tratamento do parâmetro que define a forma de gerar as informações para o Item Principal, somente para o Incentivo da Indústria\. 

Recuperação das notas fiscais para a geração do livro \- Item Principal:

- Empresa – código da empresa do login; 
- Estabelecimento – código do estabelecimento selecionado para geração; 
- Data Fiscal – data enquadrada no período de apuração; 
- Somente notas de Entrada \(MOVTO\_E\_S <> ‘9’\);
- Classificação do Documento Fiscal igual a 1, 3 ou 4;
- Nota que não seja de Transferência \(IND\_TRANSF\_CRED = ’0’\)
- [Produto](#ProdutoouNCMsujeitosaICMSST) parametrizado para Produto Incentivado – Indústria 
- Notas que estejam gravadas na tabela de Incentivo das Notas Fiscais \(ICT\_GUIA\_INCENT\)

 Geração do livro \- Regra Específica para Incentivo – Indústria – Regra para Livro Incentivado:

       Se o parâmetro “Demonstrar Somente Operações Incentivadas nos Livros Incentivados” informado na tela de Regras de Incentivo\*\* estiver 

            desmarcado, para o grupo de incentivo “Indústria” referente ao produto da nota

            Serão consideradas todas as notas gravadas na tabela de Incentivo das Notas Fiscais, independente da operação \(CFOP/Natureza\) ser  

             parametrizada ou não \(IND\_INCENT = ‘N’ ou ‘I’\)

       Senão

            Serão consideradas somente as notas gravadas na tabela de Incentivo das Notas Fiscais que são consideradas incentivadas \(IND\_INCENT 

            = ‘I’\), ou seja, são as notas que têm o CFOP ou CFOP/Natureza de Operação parametrizado para em CFOP/Natureza Incentivados

Geração do livro \- Regra Específica para Incentivo – Indústria – Regra para Livro não Incentivado:

       Se o parâmetro “Demonstrar Somente Operações Incentivadas nos Livros Incentivados” informado na tela de Regras de Incentivo\*\* estiver 

            desmarcado, para o grupo de incentivo “Indústria” referente ao produto da nota

            Serão consideradas todas as notas que não estão gravadas na tabela de Incentivo das Notas Fiscais \(ICT\_GUIA\_INCENT\) e que atendam às 

            regras de recuperação 

       Senão

            Serão consideradas todas as notas que não estão gravadas na tabela de Incentivo das Notas Fiscais \(ICT\_GUIA\_INCENT\) e que atendam às 

            regras de recuperação\. Também serão consideradas as notas gravadas na tabela de Incentivo das Notas Fiscais, que não tem a operação 

            \(CFOP/Natureza\) parametrizada \(IND\_INCENT = ‘N’\)\.

__\*\*__ Menu: Parâmetros 🡪 Incentivo – Central de Distribuição 🡪 Regras de Incentivo

Como identificar que o produto pertence ao grupo de incentivo – Indústria: o produto relacionado na nota fiscal vai estar cadastrado na parametrização de Produto Incentivado – Indústria, para um grupo de incentivo específico\.  Este grupo é que vai indicar o tipo de incentivo, através do campo Tipo de Incentivo que deve ser igual a “Indústria” \(IND\_GRP\_ESP= nulo\), da tabela de Grupos de Incentivo \(ICT\_GRP\_INCENT\)\.

Importante à A regra acima que define qual o tipo de nota deve ser gerada no livro incentivado deve ser usada em todas as etapas de geração do Livro \(Principal, Resumo CFO, Resumo p/ Alíquota\.\.\.\)\.

__RN04__

__Recuperação dos Dados \- Incentivo – Importação__

__\[MFS600421\] __Tratamento do parâmetro que define a forma de gerar as informações para o Item Principal, somente para o Incentivo da Importação\. 

Recuperação das notas fiscais para a geração do livro \- Item Principal:

- Empresa – código da empresa do login; 
- Estabelecimento – código do estabelecimento selecionado para geração; 
- Data Fiscal – data enquadrada no período de apuração; 
- Somente notas de Entrada \(MOVTO\_E\_S <> ‘9’\);
- Classificação do Documento Fiscal igual a 1, 3 ou 4;
- Nota que não seja de Transferência \(IND\_TRANSF\_CRED = ’0’\)
- [Produto](#ProdutoouNCMsujeitosaICMSST) parametrizado para Produto Incentivado – Importação
- Notas que estejam gravadas na tabela de Incentivo das Notas Fiscais \(ICT\_GUIA\_INCENT\)

 Geração do livro \- Regra Específica para Incentivo – Importação – Regra para Livro Incentivado:

       Se o parâmetro “Demonstrar Somente Operações Incentivadas nos Livros Incentivados” informado na tela de Regras de Incentivo\*\* estiver 

            desmarcado, para o grupo de incentivo “Importação” referente ao produto da nota

            Serão consideradas todas as notas gravadas na tabela de Incentivo das Notas Fiscais, independente da operação \(CFOP/Natureza\) ser  

             parametrizada ou não \(IND\_INCENT = ‘N’ ou ‘I’\)

       Senão

            Serão consideradas somente as notas gravadas na tabela de Incentivo das Notas Fiscais que são consideradas incentivadas \(IND\_INCENT 

            = ‘I’\), ou seja, são as notas que têm o CFOP ou CFOP/Natureza de Operação parametrizado para em CFOP/Natureza Incentivados

Geração do livro \- Regra Específica para Incentivo – Importação – Regra para Livro não Incentivado:

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

Importante à A regra acima que define qual o tipo de nota deve ser gerada no livro incentivado deve ser usada em todas as etapas de geração do Livro \(Principal, Resumo CFO, Resumo p/ Alíquota\.\.\.\)\.

        = = = = =

