# MTZ_Sped_Fiscal_Regras_Registro_1400_UF_PR

> Fonte: MTZ_Sped_Fiscal_Regras_Registro_1400_UF_PR.docx






THOMSON REUTERS

Módulo Sped Fiscal

Registro 1400 – Específico por UF - PR


Localização:



DOCUMENTO DE REQUISITO
























## Registro 1400 para o tipo de geração - “Específico por UF” - UF PR








| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS62608 | Aline Melo | Inclusão de código, para a geração manual do registro 1400 do Estado do Paraná. | 13/04/2021 |
| MFS62640 | Aline Melo | Inclusão do código PRDISTRIBEE01 na geração automática do registro 1400, em atendimento ao cenário de empresas de distribuição de Energia Elétrica , para o estado do Paraná. | 16/06/2021 |
| MFS710625 | Graciela Soares | Inclusão do modelo 66 na regra do código PRDISTRIBEE01 - Distribuição de Energia, efetuada por contribuinte com CNAE principal 3514-0/00; | 03/02/2025 |


| RN1400-PR | [MFS62608] Inclusão dos códigos para PR  A geração do 1400 para a modalidade “PR” foi desenvolvida de acordo com os dados  solicitados pela NPF 017/2021, publicado na SEFAZ do Paraná.  Para o código abaixo, a geração é feita de forma manual e automática. As regras estão organizadas da seguinte forma:  RN1400-PR-01 - geração para o código “PRDISTRIBEE01” (deve ser gerado somente a partir de 01/05/2021)   Para os demais códigos, os valores serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 (menu “Geração à Manutenção à Registro 1400”).  Os valores informados manualmente serão recuperados da seguinte forma:     - Estabelecimento – estabelecimento da geração    - Período – mesmo período da tela da geração (data inicial e final)    - Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =        “Código selecionado (*)”   Poderão existir  vários registros para este código, de diferentes municípios. Para cada registro recuperado, será gravado um registro 1400, da seguinte forma:  02-COD_ITEM_IPM à este campo será preenchido com ” Código selecionado (*)”   03-MUN à Este campo será preenchido com a concatenação do código da UF (campo COD_UF da tabela MUNICIPIO) + código  do município. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve-se completar com zeros à esquerda quando necessário. 04-VALOR à Este campo será preenchido com o resultado descrito abaixo, a partir dos valores inseridos na manutenção:  [Campo “Outros Valores” informado manualmente] (-) [Campo “Outras Deduções” informado manualmente]  Crítica:  Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:  (observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos)   Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:“O campo VALOR esta com conteúdo inválido (valor negativo)”. O log mostrará a identificação do registro (Estab+Município+Código do item) para identificação do usuário. O registro 1400 não será gravado para este município.  Resultado final = zero à O registro 1400 não será gravado para este município;  (*) Código selecionado – o código será um dos códigos cadastrados na TACES89 para PR.    OBS: O registro 1400 não é gerado na geração da EFD do menu “Geração-PIM”, conforme consta na regra RN1400. |
| --- | --- |
| RN1400-PR-01 | Código PRDISTRIBEE01 - Distribuição de Energia, efetuada por contribuinte com CNAE principal 3514-0/00.   [MFS62640] Esse código trata a Distribuição de Energia, efetuada por contribuinte com CNAE principal 3514-0/00. O valor correspondente ao total mensal do produto fornecido deve ser informado para o município onde ocorreu o fornecimento. Deve ser gerado somente a partir de 01/05/2021.  A apuração deste item é feita a partir das operações da SAFX42/SAFX43 para cada município do Paraná, em atendimento ao cenário de empresas de Distribuição de Energia Elétrica, levantado pelo cliente CPFL. A regras se aplicam apenas a Energia Elétrica e foram implementadas pelas MFS46087 e MFS58137, no processo de geração padrão do registro 1400, e através da demanda MFS62640, será implementada no processo de geração automática Específico por UF.  Essa regra consiste em somar as bases de ICMS Tributada, Isenta e Outras, de acordo determinados códigos de Situação Tributária B e subtrair o Valor do Desconto dos itens de dedução. Além disso os itens de Dedução tem tratamento particular para cada tipo de base. Veja o cálculo de cada parcela que compõe o valor da Operação para Energia Elétrica.  Origem:                - Notas Fiscais de Utilities (SAFX42 e SAFX43)               - Atividade Economica (CNAE) do Cadastro de Estabelecimento               - Valores informados manualmente                Tratam-se das notas fiscais de saída gravadas nos registros específicos C500, C600 ou C700 para o segmento de energia elétrica.  Critérios para Recuperação das Notas:  Totalizar o valor do serviço das notas da SAFX42/SAFX43 que atendam aos seguintes critérios:   - Código da empresa = código da empresa da geração; - Código do estabelecimento = código do estabelecimento da geração; - Data (campo 03 da SAFX42) no período da geração ou data extemporânea no período de    Geração - Somente notas de saída (SAFX42 se aplica apenas para saídas); - Situação = somente as não canceladas - Não considerar os itens informativos (itens da SAFX43 com o campo 10-Tipo de    Item = 1) - Município de Terminal Faturado (campo 76 da SAFX42) deve ser um município da   UF do Estabelecimento - CNAE ( campo Atividade Economica do Cadastro de Estabelecimento) = “3514-0/00” e UF do Estabelecimento = “PR”  OBS: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I.E.U., serão recuperadas as notas do estabelecimento selecionado (centralizador), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I.E.U. do módulo de controle das obrigações estaduais. |


|  | Totalização das Notas recuperadas :  >> Base Tributada de ICMS: Para calcular a Base Tributada de ICMS, recuperar os itens da SAFX43 que atendam aos critérios:  Critérios para recuperação de notas, conforme definidos no início da regra; Modelo (campo 13 da SAFX42) = “06  ou 66”; Código Situação Tributária B (campo 33 da SAFX43)= “00”; Base Tributada ICMS (campo 23 da SAFX43) > 0,00;  Para esses itens, recuperar os campos: Base Tributada ICMS (campo 23 da SAFX43);  Valor do Desconto (campo 18 da SAFX43); Adição/Desconto (campo 20 da SAFX43);   OBS.: O valor do Desconto é subtraído duas vezes, pois um é o próprio valor do desconto e o outro é a Base Tributada ICMS Negativada, que na prática é o mesmo valor do desconto. Explicação dada na reunião de 14/09/2020: https://web.microsoftstream.com/video/2caeaf7f-d9ed-4c2d-a8c3-ce91bf5a5612 Como o campo “20-Adição/Desconto” não é obrigatório, caso esteja nulo é considerado como item de Adição (“A”).  >> Base Isenta de ICMS: Para calcular a Base Isenta de ICMS, recuperar os itens da SAFX43 que atendam aos critérios:  Critérios para recuperação de notas, conforme definidos no início da regra; Modelo (campo 13 da SAFX42) = “06 ou 66”;  Código Situação Tributária B (campo 33 da SAFX43)= “40”; Base Isenta ICMS (campo 24 da SAFX43) > 0,00; Desconsiderar os itens com Adição/Desconto = “D” (campo 20 da SAFX43); MFS58137: Considerar todos os produtos ou apenas os Parametrizados com Isenção de ICMS, conforme regra a seguir:  Caso a opção “Utilizar a parametrização de produtos com Isenção de ICMS para Energia Elétrica” esteja marcada na Tela de Dados Iniciais em:   Tipo de Geração: Específico por UF, no item Dados para geração específica (PR):   Considerar apenas itens da SAFX43 com Produtos (campos 11 e 12) pertencentes à Parametrização de Produtos com Isenção de ICMS (menu: Parâmetros >> Registro 1400 >> Serviço de Energia Elétrica >> Produto com Isenção de ICMS)  Caso a opção “Utilizar a parametrização de produtos com Isenção de ICMS para Energia Elétrica” esteja desmarcada na Tela de Dados Iniciais, então: Todos os produtos devem ser considerados, não aplicando a Parametrização de Produtos com Isenção de ICMS.      Para esses itens, recuperar o campo: Base Isenta ICMS (campo 24 da SAFX43);    >> Base Outras de ICMS (CST de Diferimento):  Para calcular a Base Outras de ICMS, recuperar os itens da SAFX43 que atendam aos critérios: Critérios para recuperação de notas, conforme definidos no início da regra; Modelo (campo 13 da SAFX42) = “06 ou 66”; Código Situação Tributária B (campo 33 da SAFX43)= “51”; Base Outras ICMS (campo 25 da SAFX43) > 0,00; Desconsiderar os itens com Adição/Desconto = “D” (campo 20 da SAFX43);  Para esses itens, recuperar o campo: Base Outras ICMS (campo 25 da SAFX43);    >> Desconto ST:  Para calcular o Desconto ST, recuperar os itens da SAFX43 que atendam aos critérios: Critérios para recuperação de notas, conforme definidos no início da regra; Modelo (campo 13 da SAFX42) = “06  ou 66”; itens com Adição/Desconto = “D” (campo 20 da SAFX43); MFS58137: Considerar todos os produtos ou apenas os Parametrizados com Desconto, conforme regra a seguir: Caso a opção “Utilizar a parametrização de produtos com Desconto para Energia Elétrica” esteja marcada na Tela de Dados Iniciais em:  Tipo de Geração: Específico por UF, no item Dados para geração específica (PR)   Considerar apenas itens da SAFX43 com Produtos (campos 11 e 12) pertencentes à Parametrização de Produtos com Desconto (menu: Parâmetros >> Registro 1400 >> Serviço de Energia Elétrica >> Produto com Desconto) Caso a opção “Utilizar a parametrização de produtos com Desconto para Energia Elétrica” esteja desmarcada na Tela de Dados Iniciais, então: Todos os produtos devem ser considerados, não aplicando a Parametrização de Produtos com Desconto. 	 Para esses itens, recuperar o campo: Valor do Desconto (campo 18 da SAFX43);  	  Valor a ser totalizado:     Resultado a ser gravado no registro 1400 para cada município:  Para cada município apurado será gerado um registro 1400, da seguinte forma:  02-COD_ITEM_IPM à este campo será preenchido c/o conteúdo ”PRDISTRIBEE01”   03-MUN à Este campo informa o município do ponto de consumo, e será preenchido com a concatenação do código da UF (campo COD_UF da tabela MUNICIPIO) + código  do município. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve-se completar com zeros à esquerda quando necessário. 04-VALOR à Este campo será preenchido com o valor apurado para o município (conforme descrito em Valor a ser totalizado), mais os valores inseridos na manutenção do registro 1400 (menu “Geração à Manutenção à Regitsro 1400”).  Estes valores informados manualmente serão recuperados da seguinte forma:     - Estabelecimento – estabelecimento da geração    - Período – mesmo período da tela da geração (data inicial e final)    - Município – município da totalização     - Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =      ”PRDISTRIBEE01”  Assim, o valor a ser gravado no campo 04-VALOR será o seguinte resultado:                     [Valor resultante da totalização – valor da dedução apurada]                                                         (+)                         [Campo “Outros Valores” informado manualmente]                                                         (-)                         [Campo “Outras Deduções” informado manualmente]  Crítica:  Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:  - Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: “O campo VALOR esta com conteúdo inválido (valor negativo)”. O log mostrará a identificação do registro (Estab+Município+Código do item) para identificação do usuário. O registro 1400 não será gravado para este município.  - Resultado final = zero à O registro 1400 não será gravado para este município;  Gravação dos valores para tela da manutenção:  O valor resultante da totalização das notas fiscais (SAFX42/SAFX43), o valor da dedução apurada, e também o valor final gravado no registro 1400, serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente (menu “Geração à Manutenção à Registro 1400”):   - No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas; - No campo “Deduções”:      será gravado zero; - No campo “Valor Total”:   será gravado o valor final (valor gravado no registro 1400); |
| --- | --- |
