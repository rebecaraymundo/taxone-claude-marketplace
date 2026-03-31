# MTZ_EFD_Pre_Geracao_Registro_B470

> Fonte: MTZ_EFD_Pre_Geracao_Registro_B470.docx






THOMSON REUTERS

Pré-Geração da Apuração do ISS
EFD-Escrituração Fiscal Digital



DOCUMENTO DE REQUISITO



Localização:
Menu Sped, Módulo EFD - Escrituração Fiscal Digital, item Pré-Geração  Registro B470

REGRAS DE NEGÓCIO




Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:





| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-20991 | Julyana Perrucini | Essa MFS tem como objetivo atender o Ato COTEPE Nº 44/2018, em que será criada uma rotina para gerar a totalização dos valores do Registro B470, e após reaproveitada para geração do relatório de conferência e arquivo magnético. |
| MFS29820 | Andréa Rocha | Alteração na regra de preenchimento do campo VL_ISNT_ISSQN. |
| MFS63384 | Aline Melo | Ajuste na regra geral, para tratar as notas de serviços tomados dos contriuintes do DF, cujo o periodo a ser considerado deve ser na ocorrerencia da data do pagamento e retenção do ISS. |
| MFS79708 | Andréa Rocha | Inclusão da recuperação das notas fiscais de modelo 66, pois o o modelo 66 foi incluído no registro B020.  Como este registro é um total de valores do B020/B025, deve-se utilizar o mesmo filtro de modelos. |


| CÓD | DESCRIÇÃO | MFS/CH |
| --- | --- | --- |
| RN00 | Regra Geral  Recuperação dos Dados 1  [MFS79708] Inclusão do novo modelo “66”, válido a partir do layout 1.15 (Janeiro/2022).  Origem: SAFX07, SAFX09 e tabelas de cadastros relacionadas.  Este processo será realizado apenas para os itens de documento fiscal de serviço que atendam aos seguintes critérios:  Empresa igual a empresa selecionada na geração;  Estabelecimento igual ao estabelecimento selecionado na geração;  Nota fiscal de entrada e saída (serviços tomados e prestados campo 03-MOVTO_E_S = 1, 2, 3, 4, 5 e 9 da tabela SAFX07);  Se a UF do Estabelecimento = “DF” e a nota for de entrada (serviços tomados campo 03-MOVTO_E_S <> ‘9’ da tabela SAFX07), considerar:  A data do pagamento (campo 175-DT_PAGTO_NF da tabela SAFX07) deve ser preenchida e referente ao período informado em tela (>= data inicial e <= data final) E Indicador Tipo Retenção = “RETIDO PELO TOMADOR” (campo 141-IND_TP_RET = ‘1’ da tabela SAFX07)  Se as condições de Data de Pagamento e Tipo de Retenção acima não forem atendidas, as notas não devem ser consideradas no registro.  Senão, considerar: A data fiscal da nota deve ser referente ao período informado em tela (>= data inicial e <= data final);  Classificação fiscal 2 e 3 (nota fiscal de serviço e nota fiscal mista campo 12-COD_CLASS_DOC_FIS = 2, 3 da tabela SAFX07);  Modelo 01, 03, 3A, 3B, 04, 08, 55, 65 e 66 (campo 13-COD_MODELO = 01, 03, 3A, 3B, 04, 08, 55, 65, 66 da tabela SAFX07);  Não considerar notas fiscais canceladas (campo 30-SITUACAO <> S da tabela SAFX07);  Não considerar notas fiscais de serviço sem itens;  Desconsiderar itens das notas ficais cujo serviço foi realizado por intermediário e não tenha incidência do ISS ou Isenção (campo 39-BASE_ISS da tabela SAFX09 quando campo 38-TRIB_ISS da tabela SAFX09 = 3);  Na geração por Inscrição Estadual Única, devem ser considerados os documentos fiscais de todos os Estabelecimentos envolvidos na centralização.  Recuperação dos Dados 2  Origem: SAFX270.  Este processo será realizado apenas para as deduções do ISS que atendam aos seguintes critérios:  Empresa igual a empresa selecionada na geração;  Estabelecimento igual ao estabelecimento selecionado na geração;  Período de apuração deve ser referente ao período informado em tela (>= data inicial e <= data final);  Na geração por Inscrição Estadual Única, devem ser considerados as deduções de todos os Estabelecimentos envolvidos na centralização.  Recuperação dos Dados 3  Origem: SAFX221.  Este processo será realizado apenas para as deduções do ISS que atendam aos seguintes critérios:  Empresa igual a empresa selecionada na geração;  Estabelecimento igual ao estabelecimento selecionado na geração;  Período do lançamento deve ser referente ao período informado em tela (>= data inicial e <= data final);  Na geração por Inscrição Estadual Única, devem ser considerados as sociedades uniprofissionais de todos os Estabelecimentos envolvidos na centralização.  Processamento  Esse registro deverá ser gerado um por arquivo, por isso, não existe agrupamento a ser feito, ele será totalizado de acordo com o que foi gerado nos registros B420, B440, B460 e B500. Nele será feita a soma dos valores para o período em questão obedecendo a regra do tipo de operação e modelo, então deve ser verificado o tratamento de cada campo conforme a seguir.  Os campos que não tiverem informação de valor, devem ser informados com zero. | MFS-20991 MFS-63384 MFS79708 |
| RN01 | Regra p/ Gravação dos Dados  Gravar os valores totalizados em uma tabela interna que servirá para demonstrar as informações no relatório de conferência e para geração do arquivo magnético da EFD ICMS/IPI. | MFS-20991 |
| RN02 | Regra p/ Gravação do Campo “A – Valor total referente às prestações de serviço do período”:  Esse campo deve corresponder ao somatório dos valores informados no campo "Totalização do Valor Contábil das prestações" do Registro B420.  Preencher com a soma do campo 15-VLR_TOT da tabela SAFX09.  Nesse caso deverão ser somadas todas as notas fiscais de serviços prestados, ou seja, apenas notas fiscais com o campo 03-MOVTO_E_S = 9 da tabela SAFX07, considerando as demais regras de recuperação dos dados. | MFS-20991 |
| RN03 | Regra p/ Gravação do Campo “B – Valor total do material fornecido por terceiros na prestação do serviço”:  De acordo com a recuperação dos dados, preencher com o somatório do campo 56-VLR_MAT_TERC da tabela SAFX09. | MFS-20991 |
| RN04 | Regra p/ Gravação do Campo “C – Valor do material próprio utilizado na prestação do serviço”:  De acordo com a recuperação dos dados, preencher com o somatório do campo 55-VLR_MAT_PROP da tabela SAFX09. | MFS-20991 |
| RN05 | Regra p/ Gravação do Campo “D – Valor total das subempreitadas”:  De acordo com a recuperação dos dados, preencher com o somatório do campo 60-VLR_SUBEMPR_ISS da tabela SAFX09. | MFS-20991 |
| RN06 | Regra p/ Gravação do Campo “E – Valor total das operações isentas ou não-tributadas pelo ISS”:  Esse campo deve corresponder ao somatório dos valores informados no campo "Totalização do Valor das operações Isentas/ Ñ Tributadas" do Registro B420.  [ALTERADA – MFS29820]  Se o campo Tributação ISS (campo 38 da SAFX09) for igual a ‘2’       Preencher com a Base ISS (campo 39 da SAFX09) Senão       Preencher com o Valor do Desconto (campo 21 da SAFX09).  Nesse caso deverão ser somadas todas as notas fiscais de serviços prestados, ou seja, apenas notas fiscais com o campo 03-MOVTO_E_S = 9 da tabela SAFX07, considerando as demais regras de recuperação dos dados. | MFS-20991 MFS29820 |
| RN07 | Regra p/ Gravação do Campo “F – Valor total das deduções da base de cálculo”:  Preencher com o somatório dos valores informados nos campos: “B – Valor total do material fornecido por terceiros na prestação do serviço”, “C – Valor do material próprio utilizado na prestação do serviço”, “D – Valor total das subempreitadas” e “E – Valor total das operações isentas ou não-tributadas pelo ISS”. (B + C + D + E) | MFS-20991 |
| RN08 | Regra p/ Gravação do Campo “G – Valor total da base de cálculo do ISS”:  Esse campo deve corresponder ao somatório dos valores informados no campo "Totalização do Valor da BC do ISS" do Registro B420.  Preencher com a soma do campo 39-BASE_ISS da tabela SAFX09 quando o campo 38-TRIB_ISS da tabela SAFX09 = 1.  Nesse caso deverão ser somadas todas as notas fiscais de serviços prestados, ou seja, apenas notas fiscais com o campo 03-MOVTO_E_S = 9 da tabela SAFX07, considerando as demais regras de recuperação dos dados. | MFS-20991 |
| RN09 | Regra p/ Gravação do Campo “H – Valor total da base de cálculo de retenção do ISS referente às prestações do declarante”:  Esse campo deve corresponder ao somatório dos valores informados no campo "Totalização do Valor da BC de Retenção do ISS" do Registro B440.  Preencher com a soma do campo 57-VLR_BASE_ISS_RETIDO da tabela SAFX09.  Nesse caso deverão ser somadas todas as notas fiscais de serviços prestados, ou seja, apenas notas fiscais com o campo 03-MOVTO_E_S = 9 da tabela SAFX07, desconsiderando notas fiscais de modelo 3A, campo 13-COD_MODELO <> 3A da tabela SAFX07, e considerando as demais regras de recuperação dos dados. | MFS-20991 |
| RN10 | Regra p/ Gravação do Campo “I – Valor total do ISS destacado”:  Esse campo deve corresponder ao somatório dos valores informados no campo "Totalização do Valor do ISS" do Registro B420.  Preencher com a soma do campo 33-VLR_ISS da tabela SAFX09.  Nesse caso deverão ser somadas todas as notas fiscais de serviços prestados, ou seja, apenas notas fiscais com o campo 03-MOVTO_E_S = 9 da tabela SAFX07, considerando as demais regras de recuperação dos dados. | MFS-20991 |
| RN11 | Regra p/ Gravação do Campo “J – Valor total do ISS retido pelo tomador nas prestações do declarante”:  Esse campo deve corresponder ao somatório dos valores informados no campo "Totalização do Valor do ISS Retido" do Registro B440.  Preencher com a soma do campo 58-VLR_ISS_RETIDO da tabela SAFX09.  Nesse caso deverão ser somadas todas as notas fiscais de serviços prestados, ou seja, apenas notas fiscais com o campo 03-MOVTO_E_S = 9 da tabela SAFX07, desconsiderando notas fiscais de modelo 3A e 65, campo 13-COD_MODELO <> 3A, 65 da tabela SAFX07, e considerando as demais regras de recuperação dos dados. | MFS-20991 |
| RN12 | Regra p/ Gravação do Campo “K – Valor total das deduções do ISS próprio”:  De acordo com a recuperação dos dados, preencher com o somatório do campo 06-VLR_DEDUCAO da tabela SAFX270 quando o campo 05-IND_OBRIG = 0 da tabela SAFX270. | MFS-20991 |
| RN13 | Regra p/ Gravação do Campo “L – Valor total apurado do ISS próprio a recolher”:  Preencher com o valor totalizado no campo “I – Valor total do ISS destacado” deduzindo os valores totalizados nos campos “J – Valor total do ISS retido pelo tomador nas prestações do declarante” e “K – Valor total das deduções do ISS próprio”. (I - J - K)  Tratamento: Se o resultado for negativo, informar zero. | MFS-20991 |
| RN14 | Regra p/ Gravação do Campo “M – Valor total do ISS substituto a recolher pelas aquisições do declarante (tomador)”:  Esse campo deve corresponder ao somatório dos valores informados no campo "Totalização do Valor do ISS Retido" do Registro B440.  Preencher com a soma do campo 58-VLR_ISS_RETIDO da tabela SAFX09.  Nesse caso deverão ser somadas todas as notas fiscais de serviços recebidos, ou seja, apenas notas fiscais com o campo 03-MOVTO_E_S <> 9 da tabela SAFX07, desconsiderando notas fiscais de modelo 3A e 65, campo 13-COD_MODELO <> 3A, 65 da tabela SAFX07, e considerando as demais regras de recuperação dos dados.  Após recuperada a informação das aquisições, conforme regra descrita anteriormente, sua soma será deduzida do somatório do campo 06-VLR_DEDUCAO da tabela SAFX270 quando o campo 05-IND_OBRIG = 1 da tabela SAFX270.  Tratamento: Se o resultado for negativo, informar zero. | MFS-20991 |
| RN15 | Regra p/ Gravação do Campo “N – Valor do ISS próprio a recolher pela Sociedade Uniprofissional”:  Preencher com a diferença entre o somatório do campo 06-VLR_ISS_RECOLHER da tabela SAFX221 e do campo 06-VLR_DEDUCAO da tabela SAFX270 quando o campo 05-IND_OBRIG = 2 da tabela SAFX270.  Tratamento: Se o resultado for negativo, informar zero. | MFS-20991 |
| RN16 | Regra p/ Demonstração dos Dados  Demonstrar a totalização dos valores na aba Relatório da seguinte forma: | MFS-20991 |


| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | MFSNNNN |
| --- | --- | --- |
