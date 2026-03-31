# MTZ_Sped_Fiscal_Regras_Registro_1400_UF_SC

> Fonte: MTZ_Sped_Fiscal_Regras_Registro_1400_UF_SC.docx






THOMSON REUTERS

Módulo Sped Fiscal

Registro 1400 – Específico por UF - SC


Localização:



DOCUMENTO DE REQUISITO
























## Registro 1400 para o tipo de geração - Específico por UF - SC




| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS40285 | Aline Melo | Criação do documento. Inclusão do código 06 no processo de geração automática do registro 1400, para o estado de Santa Catarina. | 01/09/2021 |
|  |  |  |  |


| RN1400-SC | [MFS33871] Inclusão dos códigos para SC  A geração do 1400 para a modalidade “SC” foi desenvolvida de acordo com os dados solicitados no Ato DIAT n° 36/2019.  A princípio os valores de todos os códigos serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 (menu “Geração  Manutenção  Regitsro 1400”).  Os valores informados manualmente serão recuperados da seguinte forma:     - Estabelecimento – estabelecimento da geração    - Período – mesmo período da tela da geração (data inicial e final)    - Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =        “Código selecionado (*)”   Poderão existir  vários registros para este código, de diferentes municípios. Para cada registro recuperado, será gravado um registro 1400, da seguinte forma:  02-COD_ITEM_IPM  este campo será preenchido com ” Código selecionado (*)”   03-MUN  Este campo será preenchido com a concatenação do código da UF (campo COD_UF da tabela MUNICIPIO) + código  do município. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve-se completar com zeros à esquerda quando necessário. 04-VALOR  Este campo será preenchido com o resultado descrito abaixo, a partir dos valores inseridos na manutenção:                    [Campo “Outros Valores” informado manualmente]                                                     (-)                  [Campo “Outras Deduções” informado manualmente]  Crítica:  Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:  (observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos)   Resultado final negativo  Será  gravada uma mensagem de erro no log com a seguinte descrição:“O campo VALOR esta com conteúdo inválido (valor negativo)”. O log mostrará a identificação do registro (Estab+Município+Código do item) para identificação do usuário.  Resultado final = zero  O registro 1400 não será gravado para este município;  (*) Código selecionado – o código será um dos códigos cadastrados na TACES89 para SC.  Exemplo: 01.   OBS: O registro 1400 não é gerado na geração da EFD do menu “Geração-PIM”, conforme consta na regra RN1400. |
| --- | --- |
| RN1400-SC-01 | Código 06 – Saída de mercadoria realizada por estabelecimento diverso  MFS40285: A partir dessa demanda, a geração do código “06”, deve ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400.  Origem dos dados: Notas Fiscais (SAFX07 e SAFX08)                                   Valores informados manualmente                                    Parametrização de CFOP e CFOP/NAT  A apuração deste item é feita a partir das operações da SAFX07/SAFX08 para cada município do SC.   Este código será gerado a partir dos documentos de saída de mercadorias, realizada por estabelecimento diverso, totalizando os valores por município de origem, desde que: - ambos estejam localizados no território catarinense, e - o estabelecimento onde ocorreu a efetiva venda não tenha emitido a NF-e (modelo 55) da venda.  Para apurar o total das operações deste item, será feita a totalização das notas fiscais de saída gravadas nos registros no C100.  Critérios de recuperação das notas na SAFX07/SAFX08:  - Código da empresa = código da empresa da geração; - Código do estabelecimento = código do estabelecimento da geração; - Somente notas de saída (campo 03-MOVTO_E_S da SAFX07 = 9); - Data Fiscal no período da geração ou data extemporânea no período de geração; - Modelo (campo13-MODELO da SAFX07) igual a 01, 1B, 04 ou 65; - Classificação fiscal (campo 12-COD_CLASS_DOC_FIS da SAFX07) igual a 1 ou 3 (no caso de nota mista (classif. = 3), considerar apenas os itens de mercadoria); - Somente notas não canceladas (campo 30-SITUACAO da SAFX07 <> S); - CFOP ou CFOP/NAT parametrizados no menu “Parâmetros à    Registro 1400 à Específico por UF” para o operação “06”; - Serão consideradas apenas as notas em que o município de origem (município onde ocorreu a saída da mercadoria) e destino (município para onde ocorreu a venda) seja de SC: UF Origem (campo 117-UF_ORIG_DEST) e UF Destino (campo 122- UF_DESTINO) = SC - Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item; - Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;  Totalização dos valores:  - Para as notas com itens (Classificação = ‘1’ ou ‘3’): será totalizado o valor contábil dos itens (campo 64-VLR_CONTAB_ITEM SAFX08); - Para as notas sem itens (Classificação = ‘1’ ou ‘4’): será totalizado o valor total da nota (campo 23-VLR_TOT_NOTA da SAFX07);  OBS:  1- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I.E.U., serão recuperadas as notas do estabelecimento selecionado (centralizador), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I.E.U. do módulo de controle das obrigações estaduais.   Gravação do registro 1400:  As notas/itens recuperados conforme os critérios acima, serão totalizados por município de origem:   Para cada município apurado será gravado um registro 1400, da seguinte forma:  02-COD_ITEM_IPM à este campo será preenchido com o conteúdo ”06”   03-MUN à Este campo será preenchido com a concatenação do código da UF (campo COD_UF da tabela MUNICIPIO) + código  do município. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve-se completar com zeros à esquerda quando necessário. 04-VALOR à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 (menu “Geração à Manutenção à Regitsro 1400”). Estes valores informados manualmente serão recuperados da seguinte forma:     - Estabelecimento – estabelecimento da geração    - Período – mesmo período da tela da geração (data inicial e final)    - Município – município da totalização     - Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =      ”06”  Assim, o valor a ser gravado no campo 04-VALOR será o seguinte resultado:   [Valor resultante da totalização] (+) [Campo “Outros Valores” informado manualmente] (-) [Campo “Outras Deduções” informado manualmente]  Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:  Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: “O campo VALOR esta com conteúdo inválido (valor negativo)”. O log mostrará a identificação do registro (Estab+Município+Operação) para identificação do usuário. O registro 1400 não será gravado para este município.  Resultado final = zero à O registro 1400 não será gravado para este município;  Gravação dos valores para tela da manutenção:  O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente.   No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas; No campo “Deduções”:      será gravado zero; No campo “Valor Total”:   será gravado o valor final (valor gravado no registro 1400); |
