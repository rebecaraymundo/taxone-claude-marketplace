# MTZ_REINF_Regra_Geracao_Ajustes_CPRB

> Fonte: MTZ_REINF_Regra_Geracao_Ajustes_CPRB.docx






THOMSON REUTERS

Módulo EFD-REINF
Regra de recuperação dos Ajustes – SAFX252



DOCUMENTO DE REQUISITO



REGRAS DE NEGÓCIO





Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:



| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS15093 | Lara Aline | Regra de recuperação das informações dos ajustes. Primeiramente para o Ajustes 6 - Vendas Canceladas e os descontos incondicionais concedidos. (SAFX252). |


| CÓD | DESCRIÇÃO | MFS/CH |
| --- | --- | --- |
| RN00 | Regras Gerais  Essa rotina tem por finalidade efetuar a geração automática dos ajustes da CPRB. Esses ajustes serão lançados na SAFX252 da mesma forma que é feito atualmente se incluído o ajuste manualmente pela tela de manutenção da CPRB.  - Deverão ser consideradas todas as validações abaixo para compor o Log do Processo:  1 – Caso o valor do ajuste de redução encontrado seja maior que o Valor da Receita Bruta do Estabelecimento (VLR_REC_BRT_ATIV da SAFX185), será gravada a seguinte mensagem de erro no log do processo:  “O valor do ajuste de redução é maior que o valor da Receita Bruta do Estabelecimento. Nesse caso será gravado o valor 0 - zero.”.   O log exibirá os dados de identificação da nota fiscal em questão (Número de nota fiscal/Série/SubSérie e Data fiscal), para que o usuário possa conferir os dados. | MFS15093 |
| RN01 | Processamento dos Dados  Origem dos Dados: Tabela dos Documentos Fiscais (SAFX08/SAFX09)                                   Parametrização dos Ajustes da CPRB (menu Parâmetros > CPRB > Parametrização dos Ajustes da CPRB > Por CFOP ou CFOP/Natureza (*)                                   Parametrização dos Ajustes da CPRB (menu Parâmetros > CPRB > Parametrização dos Ajustes da CPRB > Serviço (**)  Destino: Tabela SAX252 - Ajuste da Contribuição Previdenciária Apurada.                Tabela SAX185 - Apuração da Contribuição Previdenciária sobre a Receita Bruta – Bloco P.  O processamento é por Estabelecimento.  Para cada Estabelecimento, será calculado o valor total de cada ajuste.  O Processamento é de acordo com as notas do período de referência informado em tela.  Origem das informações para SAFX252:    Importante: Sempre que o processo for efetuado pela rotina automática dos ajustes, as informações e ajustes encontrados irão sobrescrever as informações anteriormente carregadas para o ajuste, período e atividade que o usuário efetuar a geração. Ou seja, o ajuste efetuado anteriormente pelo processo manual será descartado e substituído pelo ajuste no processo automático.  A seguir serão definidas as regras desse processamento. | MFS15093 |
| RN02 | Critérios para a recuperação dos documentos  Tipo de Ajuste: Ajuste de redução   Código do Ajuste = 6 - Vendas canceladas e os descontos incondicionais concedidos:      - Empresa = código da empresa do login;      - Estabelecimento = código do estabelecimento da geração;       - Data Emissão = deve ser uma data referente ao período informado em tela;      - Somente notas não canceladas;      - Classificação fiscal = 1, 2 ou 3;      - Considerar todas as notas que: O CFOP ou CFOP/Natureza estejam cadastrados na Parametrização dos Ajustes da CPRB (*) para a Tipo de Ajuste = ‘Ajuste de redução’ e Código do Ajuste = ‘6 - Vendas canceladas e os descontos incondicionais concedidos’ ou O Serviço estejam cadastrados na Parametrização dos Ajustes da CPRB (**) para a Tipo de Ajuste = ‘Ajuste de redução’ e Código do Ajuste = ‘6 - Vendas canceladas e os descontos incondicionais concedidos’.  Obs.: Essa rotina de recuperação será efetuada após o cálculo da CPRB, ou seja, as informações serão previamente levantadas para o período/estabelecimento e a partir dela encontraremos a informação do/s Código de Atividade para geração do R-2060 (SAFX185). Para cada CFOP ou CFOP/Natureza e Serviço parametrizado o usuário vinculará o Código de Atividade pertencente, e a totalização dessas notas se fará pelo código de Atividade parametrizado.  Totalização do Valor de Ajuste:  Para cada item a ser totalizado por Código de Atividade:  Caso encontrado valor informado no campo VLR_DESCONTO da SAFX08/SAFX09 será recuperado o valor do campo VLR_DESCONTO SAFX08/SAFX09. Caso contrário, será recuperado o valor do (campo VLR_CONTAB_ITEM das notas de saída SAFX08 (CFOP/CFOP/Natureza (*)) ou campo VLR_TOT das notas de saída SAFX09 (Serviço (**))).   Esse valor será gravado no campo Valor de Ajuste (VL_AJ_REINF – SAFX252).       Cálculo do Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta (SAFX185):       Para cada item processado, calcular o Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta da seguinte forma:          Valor totalizado da Ajuste por Atividade = Será o valor recuperado da Totalização do Valor de Ajuste descrita acima.          Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta = Valor da Receita Bruta do Estabelecimento (VLR_REC_BRT_ATIV – SAFX185) – Valor totalizado da Ajuste por Atividade.    Importante: Para esse ajuste como se trata de um ajuste de redução o valor será deduzido da Receita da Atividade, mas deverão ser totalizados ao final todos os ajustes de redução encontrados para a atividade e período, tanto via processo manual quanto via processo automático para popular a informação do campo (VLR_EXC_REC_BRT - SAFX185) e o campo Valor Ajuste Exclusão do quadro Valores EFD-REINF da tela de manutenção da CPRB - Contribuição Previdenciária Sobre a Receita Bruta.  Após essa totalização esse será o valor final totalizado que será deduzido do campo (VLR_REC_BRT_ATIV - SAFX185) para encontrarmos o Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta (VLR_BASE_CONT_PREV – SAFX185).  Cálculo do Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta na tela de manutenção da CPRB:  Campo Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta do quadro ‘Valores EFD – Contribuições’:   Nesse campo serão apenas deduzidos os ajustes de redução, ajustes de acréscimo não serão considerados no cálculo desse campo.  Valor totalizado da Ajuste por Atividade = Será o valor recuperado da Totalização do Valor de Ajuste descrita acima.  Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta = Valor da Receita Bruta do Estabelecimento (VLR_REC_BRT_ATIV – SAFX185) – Valor totalizado da Ajuste por Atividade  Campo Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta do quadro ‘Valores EFD – REINF’:   Nesse campo serão considerados todos os ajustes, deduzidos os ajustes de redução e somados os ajustes de acréscimo no cálculo desse campo.  Valor totalizado da Ajuste por Atividade = Será o valor recuperado da Totalização do Valor de Ajuste descrita acima.  Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta = Valor da Receita Bruta do Estabelecimento (VLR_REC_BRT_ATIV – SAFX185) – Valor totalizado da Ajuste por Atividade | MFS15093 |
|  |  |  |
|  |  |  |
|  |  |  |


| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |
