# MTZ_Sped_Fiscal_Regras_Registro_1400_UF_AC

> Fonte: MTZ_Sped_Fiscal_Regras_Registro_1400_UF_AC.docx






THOMSON REUTERS

Módulo Sped Fiscal

Registro 1400 – Específico por UF - AC


Localização:



DOCUMENTO DE REQUISITO
























## Registro 1400 para o tipo de geração - Específico por UF - AC







| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS43147 | Aline Melo | Inclusão do código ACIPMS04 no processo automático de geração do registro 1400, estado do Acre. | 06/08/2021 |


| RN1400-AC | Em atendimento a publicação da tabela de códigos IPM para a UF do Acre, os códigos podem ser gerados a partir dos dados inseridos na manutenção do registro 1400 (menu “Geração à Manutenção à Regitsro 1400”).  Os valores informados manualmente serão recuperados da seguinte forma:     - Estabelecimento – estabelecimento da geração      - Período – mesmo período da tela da geração (data inicial e final)    - Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =        “Código selecionado (*)”   Poderão existir  vários registros para este código, de diferentes municípios. Para cada registro recuperado, será gravado um registro 1400, da seguinte forma:  02-COD_ITEM_IPM à este campo será preenchido com ”Código selecionado (*)”   03-MUN à Este campo será preenchido com a concatenação do código da UF (campo COD_UF da tabela MUNICIPIO) + código  do município. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve-se completar com zeros à esquerda quando necessário. 04-VALOR à Este campo será preenchido com o resultado descrito abaixo, a partir dos valores inseridos na manutenção:  [Campo “Outros Valores” informado manualmente] (-) [Campo “Outras Deduções” informado manualmente]  Crítica:  Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:  (observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos)   Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:“O campo VALOR esta com conteúdo inválido (valor negativo)”. O log mostrará a identificação do registro (Estab+Município+Código do item) para identificação do usuário e o registro não será gravado para este município.  Resultado final = zero à O registro 1400 não será gravado para este município;  (*) Código selecionado – o código será um dos códigos cadastrados na TACES89 para AC.  Exemplo: ACIPMS04.   OBS: O registro 1400 não é gerado na geração da EFD do menu “Geração-PIM”, conforme consta na regra RN1400. |
| --- | --- |
| RN1400-AC-01 | Código ACIPMS04 – Transporte  MFS43147: A partir dessa demanda, a geração do código “ACIPMS04, deve ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400.  Origem dos dados: Notas Fiscais (SAFX07 e SAFX08)                                   Valores informados manualmente                                    Parametrização de CFOP e CFOP/NAT                                    A apuração deste item é feita a partir das operações da SAFX07/SAFX08 para cada município do Acre.   Este código será gerado a partir dos documentos de saída de transporte (identificados pelo modelo), totalizando o valor contábil das saídas por município de origem acreano, excluindo-se as operações dedutíveis.  Para apurar o total das operações deste item, será feita a totalização dos itens das notas fiscais de entrada gravadas no registro D100.  Critérios de recuperação das notas na SAFX07/SAFX08:  - Código da empresa = código da empresa da geração; - Código do estabelecimento = código do estabelecimento da geração; - Somente notas de saída (campo 03-MOVTO_E_S da SAFX07 = 9); - Data Fiscal no período da geração ou data extemporânea no período de geração; - Modelo (campo13-MODELO da SAFX07) = 07, 08, 8B, 09, 10, 11, 26, 27, 57 ou 67; - Classificação fiscal (campo 12-COD_CLASS_DOC_FIS da SAFX07) igual a 1, 3, 4, 5 ou 6 (a NF de modelo 07 usa classificação 1 ou 3 e os conhecimentos classificação 4, 5 ou 6)/(no caso de nota mista (classif. = 3), considerar apenas os itens de mercadoria; - Somente notas não canceladas (campo 30-SITUACAO da SAFX07 <> S); - CFOP ou CFOP/NAT parametrizados no menu “Parâmetros à Registro 1400 à Específico por UF” para o operação “ACIPMS04”; - No caso das notas de classificação 1 ou 3 serão consideradas apenas as notas em que o município de origem (município onde ocorreu o início da prestação do serviço) seja de AC (campos 117-UF_ORIG_DEST e 182-COD_MUNICIPIO_ORIG da SAFX07);  - No caso das notas de classificação 4, 5 ou 6 serão consideradas apenas as notas em que o município de origem da SAFX07 seja de AC ou, quando este não for informado, o município da coleta na SAFX51 seja de AC (campos 62-COD_ESTADO_COLETA e 42-COD_MUNIC_COLETA da SAFX51);  - Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item; - Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;  OBS:   1-Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I.E.U., serão recuperadas as notas do estabelecimento selecionado (centralizador), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I.E.U. do módulo de controle das obrigações estaduais.  2- Como as regras são as mesmas do D100, além destes critérios de filtro, deve-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL_OPR do registro analítico (D190).  Totalização dos valores:  - Notas de classificação 1 ou 3 à valor contábil do item (campo 64-VLR_CONTAB_ITEM SAFX08) ou valor total da nota (campo 23-VLR_TOT_NOTA da SAFX07), no caso das notas sem itens;  - Notas de classificação 4, 5 ou 6 (a nota não terá itens) à valor total da nota (campo 23-VLR_TOT_NOTA da SAFX07);  As notas/itens recuperados conforme os critérios acima serão totalizados por município de origem.  O município utilizado no agrupamento será o município de origem da NF ou o município de coleta dos itens de frete (SAFX51), quando se tratar de notas de frete (classificação 4/5/6), conforme descrito acima na regra da recuperação dos dados.  OBS: Os CTRC’s têm a classificação 4, 5 ou 6, e não têm itens na SAFX08. Os seus itens ficam na SAFX51, e se referem aos dados das notas fiscais das mercadorias carregadas. Desta forma, o valor do serviço de transporte é sempre o valor da capa (SAFX07), pois os valores da SAFX51 são os valores das notas do carregamento.  Sobre o município de coleta dos itens de frete (SAFX51):   - Ao utilizar o município de coleta da SAFX51, caso exista mais de um item de frete para o mesmo documento, e eles tiverem municípios de coleta diferentes, será gravada a seguinte mensagem no log, e o documento não será considerado: “Existem na base de dados itens de frete para o documento com mais de um município de coleta. O documento não será considerado p/o registro 1400, código TOIPMS04”.   - Caso o município da SAFX51 também não esteja preenchido, será gravada a seguinte mensagem no log, e o documento não será considerado: “Para gerar o registro 1400, cód TOIPMS04, é necessário que o município de origem esteja preenchido (UF/munic origem da SAFX07 ou munic Coleta da SAFX51). O documento não será considerado”.  Apuração dos valores a serem deduzidos:   O valor das deduções será apurado com base nas notas fiscais parametrizadas como dedução (menu Parâmetros à Registro 1400 à Especifico por UF à Deduções)  Critérios de recuperação das notas para dedução (SAFX07/SAFX08):  - Código da empresa igual da empresa informada na tela de geração;  - Código do estabelecimento igual do estabelecimento informado na tela de geração; - Somente notas de entrada (campo 03-MOVTO_E_S da SAFX07 <> 9);  - Data Fiscal no período da geração ou data extemporânea no período de geração;  - Classificação fiscal (campo 12-COD_CLASS_DOC_FIS da SAFX07) igual a 1 ou 3 (no caso de nota mista (classif. = 3), considerar apenas os itens de mercadoria);  - Somente notas não canceladas (campo 30-SITUACAO da SAFX07 <> S);  - Somente notas que não sejam transferências (campo 74-IND_TRANSF_CRED da SAFX07 = 0);  - Somente notas com situação especial (campo 125-IND_SITUACAO_ESP da SAFX07) diferente de 1, 2 e 8;  - Somente as notas em que a UF de origem (campo 117-UF_ORIG_DEST da SAFX07) seja igual a “AC”; - CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à Registro 1400 à Específico por UF à Deduções” para a operação “ACIPMS04”; - Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;  - Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa.  Totalização dos valores:  - Notas com itens (Classificação = ‘1’ ou ‘3’): será totalizado o valor contábil dos itens (campo 64-VLR_CONTAB_ITEM SAFX08); - Notas sem itens (Classificação = ‘1’): será totalizado o valor total da nota (campo 23-VLR_TOT_NOTA da SAFX07);  As notas/itens recuperados conforme os critérios acima serão totalizados por município de origem.  OBS:   1-Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I.E.U., serão recuperadas as notas do estabelecimento selecionado (centralizador), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I.E.U. do módulo de controle das obrigações estaduais.  2-A parametrização das deduções não é obrigatória. Sendo assim, quando não existirem dados parametrizados, ou, quando não existirem notas que atendam à parametrização, não haverá valor de dedução. Gravação do registro 1400:  Para cada município apurado será gravado um registro 1400, da seguinte forma:  02-COD_ITEM_IPM à este campo será preenchido com o conteúdo ”ACIPMS04”   03-MUN à Este campo será preenchido com a concatenação do código da UF (campo COD_UF da tabela MUNICIPIO) + código  do município. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve-se completar com zeros à esquerda quando necessário. 04-VALOR à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 (menu “Geração à Manutenção à Regitsro 1400”). Estes valores informados manualmente serão recuperados da seguinte forma:      - Estabelecimento – estabelecimento da geração    - Período – mesmo período da tela da geração (data inicial e final)    - Município – município da totalização     - Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =      ” ACIPMS04”  Assim, o valor a ser gravado no campo 04-VALOR será o seguinte resultado:   [Valor resultante da totalização] (+) [Campo “Outros Valores” informado manualmente] (-) [Campo “Outras Deduções” informado manualmente]  Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:  Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: “O campo VALOR esta com conteúdo inválido (valor negativo)”. O log mostrará a identificação do registro (Estab+Município+Operação) para identificação do usuário, e o registro não será gravado para este município.  Resultado final = zero à O registro 1400 não será gravado para este município;  Gravação dos valores para tela da manutenção:  O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente.   No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas; No campo “Deduções”:      será gravado zero; No campo “Valor Total”:   será gravado o valor final (valor gravado no registro 1400); |
