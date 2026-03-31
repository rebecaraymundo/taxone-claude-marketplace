# MTZ_EFD_Pre_Geracao_Registro_B440

> Fonte: MTZ_EFD_Pre_Geracao_Registro_B440.docx






THOMSON REUTERS

Pré-Geração da Totalização dos Valores Retidos
EFD-Escrituração Fiscal Digital



DOCUMENTO DE REQUISITO



Localização:
Menu Sped, Módulo EFD - Escrituração Fiscal Digital, item Pré-Geração  Registro B440  Geração

REGRAS DE NEGÓCIO





Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:





| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-20990 | Julyana Perrucini | Essa MFS tem como objetivo atender o Ato COTEPE Nº 44/2018, em que será criada uma rotina para gerar a totalização dos valores do Registro B440, e após reaproveitada para geração do relatório de conferência e arquivo magnético. |
| CH17055 - MFS-29264 | Alessandra Cristina Navatta | Considerar na geração do registro B440, as notas fiscais de serviço (SAFX09) preenchidas com o campo TRIB_ISS = ‘3’ (Realizado por Terceiros). (RN00) |
| MFS74369 | Rogério Ohashi | Alteração na regra geral, para tratamento de serviços tomados dos contribuintes do Distrito Federal, para recuperar as Notas Fiscais pelo campo de data do pagamento e retenção do ISS. |
| MFS79708 | Andréa Rocha | Inclusão da recuperação das notas fiscais de modelo 66, pois o o modelo 66 foi incluído no registro B020.  Como este registro é um total de valores do B020/B025, deve-se utilizar o mesmo filtro de modelos. |


| CÓD | DESCRIÇÃO | MFS/CH |
| --- | --- | --- |
| RN00 | Regra Geral  Recuperação dos Dados  [MFS79708] Inclusão do novo modelo “66”, válido a partir do layout 1.15 (Janeiro/2022).  Este processo será realizado apenas para os itens de documento fiscal de serviço que atendam aos seguintes critérios:  Empresa igual a empresa selecionada na geração;  Estabelecimento igual ao estabelecimento selecionado na geração;  Nota fiscal de entrada e saída (serviços tomados e prestados campo 03-MOVTO_E_S = 1, 2, 3, 4, 5 e 9 da tabela SAFX07);  Se a UF do Estabelecimento = “DF” e a nota for de entrada (serviços tomados campo 03-MOVTO_E_S <> ‘9’ da tabela SAFX07), considerar:  A data do pagamento (campo 175-DT_PAGTO_NF da tabela SAFX07) deve ser preenchida e referente ao período informado em tela (>= data inicial e <= data final) E Indicador Tipo Retenção = “RETIDO PELO TOMADOR” (campo 141-IND_TP_RET = ‘1’ da tabela SAFX07)  Se as condições de Data de Pagamento e Tipo de Retenção acima não forem atendidas, as notas não devem ser consideradas no registro.  Senão, considerar:  A data fiscal da nota deve ser referente ao período informado em tela (>= data inicial e <= data final);                            Classificação fiscal 2 e 3 (nota fiscal de serviço e nota fiscal mista campo 12-COD_CLASS_DOC_FIS = 2, 3 da tabela SAFX07);  Modelo 01, 03, 3B, 04, 08, 55, 65 e 66 (campo 13-COD_MODELO = 01, 03, 3B, 04, 08, 55, 65, 66 da tabela SAFX07);  Não considerar notas fiscais canceladas (campo 30-SITUACAO <> S da tabela SAFX07);  Não considerar notas fiscais de serviço sem itens;  Desconsiderar itens das notas ficais cujo serviço foi realizado por intermediário e não tenha incidência do ISS ou Isenção (campo 39-BASE_ISS da tabela SAFX09 quando campo 38-TRIB_ISS da tabela SAFX09 = 3);  Na geração por Inscrição Estadual Única, devem ser considerados os documentos fiscais de todos os Estabelecimentos envolvidos na centralização.  Processamento  Não pode ser informado no registro a mesma combinação de valores dos campos Indicador do Tipo de Operação e Código do Participante, então as notas fiscais deverão ser agrupadas por esses campos de acordo com a recuperação: 03-MOVTO_E_S da tabela SAFX07 e 01-IND_FIS_JUR/02-COD_FIS_JUR da tabela SAFX04 de acordo com 01-IND_FIS_JUR/02-COD_FIS_JUR informado na tabela SAFX07.  Serão processadas inclusive as notas fiscais que não tiverem valores retidos, pois no Guia Prático do ICMS/IPI o registro deve ser informado ainda que não tenha havido retenção de ISS nas aquisições e prestações do declarante, neste caso, informar a base de cálculo de retenção e ISS retido zerados.  Tratamento: Como o campo Indicador do Tipo de Operação é um indicador único para aquisição (notas fiscais de entrada), então é necessário tratar para agrupar as entradas para cada participante (ver layout da EFD ICMS/IPI), ou seja, todas as entradas que serão recuperadas precisam ter um indicador único. | MFS-20990 CH17055 -  MFS-29264 MFS74369 MFS79708 |
| RN01 | Regra p/ Gravação dos Dados  Gravar os valores totalizados em uma tabela interna que servirá para demonstrar as informações no relatório de conferência e para geração do arquivo magnético da EFD ICMS/IPI: | MFS-20990 |
| RN02 | Regra p/ Demonstração dos Dados  Demonstrar a totalização dos valores na aba Relatório da seguinte forma: | MFS-20990 |


| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | MFSNNNN |
| --- | --- | --- |
