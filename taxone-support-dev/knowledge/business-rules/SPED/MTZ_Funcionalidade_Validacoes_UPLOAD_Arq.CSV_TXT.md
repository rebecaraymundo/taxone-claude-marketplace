# MTZ_Funcionalidade_Validações_UPLOAD_Arq.CSV_TXT

> Fonte: MTZ_Funcionalidade_Validações_UPLOAD_Arq.CSV_TXT.docx






THOMSON REUTERS

(EFD- Escrituração Fiscal Digital das Contribuições)
UPLOAD
Funcionalidade – Dentro da Tela de Apuração Geral PIS/COFINS




DOCUMENTO DE REQUISITO






Sumário

1.	Objetivo	3
2.	Tela	3
3.	Regras dos Campos	4

## Objetivo


O objetivo é detalhar a funcionalidade e regras de validações dos arquivos uploads, dos registros da contribuição dos débitos (M205, M220, M225, M230, M300, M605, M620, M625, M630 e M700) e dos créditos (M115,M515) que são de ajustes complementares da apuração do Pis e Cofins, para que esses dados sejam computados na geração do meio magnético do EFD_Contribuições, via solução fiscal TaxOne.

## Tela






## Regras dos Campos


Localização da tela: Módulo: SPED>> EFD – Escrituração Fiscal Digital das Contribuições
Menu: Obrigações >> Manutenção >> Apuração Geral PIS/COFINS








| MFS | Nome | Descrição |
| --- | --- | --- |
| MFS-689652 | Alessandra Navatta | Criar a funcionalidade de uploads dos Registros de ajustes dos débito: M205, M220, M225, M230, M300, M605, M620, M625, M630 e M700 e dos créditos (M115 e M515) do PIS/COFINS. |


| Cód. | Regra | MFS |
| --- | --- | --- |
| RN00 | UPLOAD  Criar uma funcionalidade de upload para os registros de débitos (M205, M220, M225, M230, M300, M605, M620, M625, M630 e M700) e dos créditos (M115, M515)  A estrutura do arquivo deve estar de acordo com o formato indicado no arquivo:  https://trten.sharepoint.com/sites/REQ_MTZ/Mastersaf%20DW%20TaxOne/Documento_Matriz/SPED/NOVA%20JORNADA%20EFD_CONTRIBUI%C3%87OES%20(TAXONE)/UpLoad/MTZ_UPLOAD_Arq.TXT_M100_M110_M115_M500_M510_M515.docx?web=1   Nomenclatura dos Arquivos: O nome dos arquivos deve seguir o padrão EPCARQ_ Prefixo (6 posições) e com separador Underline ('_'). Onde Prefixo: <COD_REG>_<COD_EMP>_<COD_ESTAB>_<ANO_MES_DA_APURACAO>  EPCARQ_<COD_REG>_<COD_EMP>_<COD_ESTAB>_<ANO_MES_DA_APURACAO>.csv EPCARQ_<COD_REG>_<COD_EMP>_<COD_ESTAB>_<ANO_MES_DA_APURACAO>.txt   <COD_REG> = Valores possíveis: M100 e M500 <COD_EMP> = Código da Empresa <COD_ESTAB> = Código do Estabelecimento <ANO_MES_DA_APURACAO> = Ano e Mês da Apuração no formato: yyyymm  .CSV ou TXT = Extensão do arquivo   Atenção: A inserção de registros, da funcionalidade de upload, será criada sempre no filho, mas, é necessárias as informações do registro pai, para identificar onde será gravada as informações.  Ex.:  M100 (pai) M110 (filho) M115 (filho)  M200 (pai) M205 (filho)  M210 (pai) M220 (filho) M225 (filho) M230 (filho) M300 (filho) | MFS-689652 |
| RN01 | Botão ‘Selecionar arquivo’   O botão: Selecionar arquivo deve estar disponível nos registros M100, M500, M205, M210, M605, M610 da tela Apuração Geral do PIS/COFINS no Módulo: SPED EFD – Escrituração Fiscal Digital das Contribuições.  Para o correto funcionamento e recuperação dos arquivos, o arquivo .CSV e ou TXT deve estar disponível na área de FTP, de acordo com a estrutura e nomenclatura indicada na RN00, deste documento.  Ao selecionar o botão ‘Selecionar arquivo’, abrirá uma tela com o título: Selecione o arquivo     Estarão disponíveis todos os arquivos disponíveis na área de FTP, que atenderam a estrutura, extensão e nomenclatura, indicados na RN00.  Botão CONFIRMAR. Confirma o carregamento do arquivo, selecionado. Botão CANCELAR. Fecha a tela. Mesma função que a opção X, no canto superior direito da tela. | MFS-689652 |
| RN02 | Resultado do Processamento do Arquivo  Após selecionar o botão Confirmar, abrirá uma tela com o título ‘Resultado do Processamento do Arquivo’, onde é exibido um totalizador de registros, registros aceitos, removidos e também de rejeitados. Conforme modelo:     Onde:  Total de Registros: exibe a quantidade de linhas no arquivo Total de Registros Aceitos: quantidade de registros que estão de acordo com a estrutura Total de Registros Removidos: quantidade de linhas que possuem o Remover, no final da linha Total de Registros Rejeitados: quantidade de linhas que foram rejeitados  Há duas maneiras de sair da tela. Pelo ‘X’, no campo superior à direita da tela ou pelo botão ‘Fechar’. | MFS-689652 |
| RN03 | Se houver rejeição, a mensagem é exibida no início do resumo do processamento | MFS-689652 |
| RN04 | Formato das Mensagens: Se o problema estiver relacionado a algum campo específico do registro, deve ser apresentado seguinte formato: Registro M999 – Linha: X. – Mensagem | MFS-689652 |
| RN05 | Validações Registro M205:  Valores inválidos para os campos: REG, NUM_CAMPO, COD_REC e VL_DEB REG Se o tipo de registro for um tipo inválido, exibir a mensagem:  “Registro M205 - Linha: X. – Tipo de registro inválido: <<Valor informado.>> Esperado: M205 NUM_CAMPO Se o campo não for preenchido com uma das opções válidas, exibir a mensagem:  “Registro M205 - Linha: X. – Valor inválido para o campo NUM_CAMPO (Posição 2): <<Valor informado.>>. Esperado: 08 ou 12” COD_RECEITA Se o campo não for preenchido valor válido, exibir a mensagem:  “Registro M205- Linha: X. – Valor inválido para o campo COD_RECEITA (Posição 3): <<Valor informado.>> VL_DEB Se o campo não for preenchido com um valor válido, exibir a mensagem:  “Registro M205 - Linha: X. – Valor inválido para o campo VL_DEB (Posição 4): <<Valor informado.>>. Esperado até 15 inteiros e 2 decimais. Campos obrigatórios não preenchido: NUM_CAMPO, COD_REC e VL_DEB  COD_RECEITA Se o campo obrigatório não for preenchido, exibir a mensagem:  “Registro M205 - Linha: X. – Valor inválido para o campo COD_RECEITA (Posição 3): Não Informado.” VL_DEB Se o campo obrigatório não for preenchido, exibir a mensagem:  “Registro M205 - Linha: X. – Valor inválido para o campo VL_DEB (Posição 4): Não informado. Esperado até 15 inteiros e 2 decimais.  Validações Registro M605:  Considerar as mesmas validações realizadas no M205 | MFS-689652 |
| RN06 | Validações Registro M210:  Valores inválidos para os campos: REG REG Se o tipo de registro for um tipo inválido, exibir a mensagem:  “Registro M210 - Linha: X. – Tipo de registro inválido: <<Valor informado.>> Esperado: M210  Validações Registro M610:  Considerar as mesmas validações realizadas no M210 | MFS-689652 |
| RN07 | Validações Registro M220: VL_AJ Se o campo obrigatório, não for preenchido, exibir a mensagem:  “Registro M220 - Linha: X. – Valor inválido para o campo VL_AJ (Posição 3): Não informado. Esperado até 15 inteiros e 2 decimais.  COD_AJ Se o campo obrigatório, não for preenchido, exibir a mensagem:  “Registro M220 - Linha: X. – Valor inválido para o campo COD_AJ (Posição 4): Conforme tabela 4.3.8.   Validações Registro M620:  Considerar as mesmas validações realizadas no M220 | MFS-689652 |
| RN08 | Validações Registro M225:  Quando removido o registro pai, exibir a mensagem:  “M225 – Linha X: Registro PAI (M220/M620) Removido.” Quando rejeitado o registro pai, exibir a mensagem:  “M225 – Linha X: Registro PAI (M220/M620) Rejeitado.” DET_VALOR_AJ Se o campo obrigatório, não for preenchido, exibir a mensagem:  “Registro M225 - Linha: X. – Valor inválido para o campo DET_VL_AJ (Posição 2):Não Informado. Esperado até 15 inteiros e 2 decimais. COD/CST Se o campo não for preenchido com valor válido, exibir a mensagem:  “Registro M225 - Linha: X. – Valor inválido para o campo COD_CST (Posição 3):<<valor informado>> DET_BC_CRED Se o campo obrigatório, não for preenchido, exibir a mensagem:  “Registro M225 - Linha: X. – Valor inválido para o campo DET_BC_DEC (Posição 4):Não Informado. Esperado até 15 inteiros e 2 decimais. DET_ALIQ Se o campo obrigatório, não for preenchido, exibir a mensagem:  “Registro M225 - Linha: X. – Valor inválido para o campo DET_ALIQ (Posição 5):Não Informado. Esperado até 8 inteiros e 4 decimais. DT_OPER_AJ Se o campo obrigatório, não for preenchido, exibir a mensagem:  “Registro M225 - Linha: X. – Valor inválido para o campo DT_OPER_AJ (Posição 6):Não Informado. Esperado yyyymmdd.  Validações Registro M625  Considerar as mesmas validações realizadas no M225 | MFS-689652 |
| RN09 | Validações Registro M230  REG Se o tipo de registro for um tipo inválido, exibir a mensagem:  “Registro M230 - Linha: X. – Tipo de registro inválido: <<Valor informado.>> Esperado: M230 CNPJ Se o campo obrigatório, não for preenchido, exibir a mensagem:  “Registro M230 - Linha: X. – Valor inválido para o campo CNPJ (Posição 2):. VL_VEND Se o campo obrigatório, não for preenchido, exibir a mensagem:  “Registro M230 - Linha: X. – Valor inválido para o campo VL_VEND (Posição 3):Não Informado. Esperado até 15 inteiros e 2 decimais. VL_NAO_RECEB Se o campo obrigatório, não for preenchido, exibir a mensagem:  “Registro M230 - Linha: X. – Valor inválido para o campo VL_NAO_RECEB (Posição 4):Não Informado. Esperado até 15 inteiros e 2 decimais. VL_CONT_DIF Se o campo obrigatório, não for preenchido, exibir a mensagem:  “Registro M230 - Linha: X. – Valor inválido para o campo VL_CONT_DIF (Posição 5):Não Informado. Esperado até 15 inteiros e 2 decimais. VL_CRED_DIF Se o campo obrigatório, não for preenchido, exibir a mensagem:  “Registro M230 - Linha: X. – Valor inválido para o campo VL_CRED_DIF (Posição 6):Não Informado. Esperado até 15 inteiros e 2 decimais. Quando COD_CRED informado: Se o campo COD_CRED for informado, VL_CRED_DIF deve ser > 0, caso não atenda essa condição, exibir a mensagem: “Registro M230 - Linha: X. – Valor do campo VL_CRED_DIF (Posição 6) deve ser MAIOR que ZERO se o campo COD_CRED (posição 7) for informado. Quando COD_CRED não informado: Se o campo COD_CRED não for informado, VL_CRED_DIF deve ser 0, caso não atenda essa condição, exibir a mensagem:  “Registro M230 - Linha: X. – Valor do campo VL_CRED_DIF (Posição 6) deve ser ZERO se o campo COD_CRED (posição 7) NÃO for informado.  Quando não encontrar M100 correspondente ao tipo de crédito Se não for encontrado M100 correspondente ao tipo de crédito informado, exibir a mensagem: “Registro M230 - Linha: X. – Não foi encontrado M100 correspondente ao tipo de crédito informado. <<exibir valor informado>>  Validações Registro M630  Considerar as mesmas validações realizadas no M230   Quando não encontrar M500 correspondente ao tipo de crédito Se não for encontrado M500 correspondente ao tipo de crédito informado, exibir a mensagem: “Registro M630 - Linha: X. – Não foi encontrado M500 correspondente ao tipo de crédito informado. <<exibir valor informado>> | MFS-689652 |
| RN10 | Validações Registro M300:  REG Se o tipo de registro for um tipo inválido, exibir a mensagem:  “Registro M300 - Linha: X. – Tipo de registro inválido: <<Valor informado.>> Esperado: M300 VL_CONT_APUR_DIFER Se o campo obrigatório, não for preenchido, exibir a mensagem:  “Registro M300 - Linha: X. – Valor inválido para o campo VL_CONT_APUR_DIFER (Posição 2):Não Informado. Esperado até 15 inteiros e 2 decimais. VL_CRED_DESC_DIFER Se o campo obrigatório, não for preenchido, exibir a mensagem:  “Registro M300 - Linha: X. – Valor inválido para o campo VL_CRED_DESC_DIFER (Posição 4):Não Informado. Esperado até 15 inteiros e 2 decimais. PER_APUR Se o campo obrigatório, não for preenchido, exibir a mensagem:  “Registro M300 - Linha: X. – Valor inválido para o campo PER_APUR (Posição 5):Não Informado. Esperado YYYYMM. Campo PER_APUR  não pode ser igual ao  período atual da apuração , caso, contrário, exibir a mensagem:  “Registro M300 - Linha: X. O valor informado para o campo PER_APUR (posição5): <<valor informado>>, não pode ser o mesmo da atual escrituração” DT_RECEB Campo DT_RECEB deve estar compreendido dentro do período de apuração, caso, contrário, exibir a mensagem: “Registro M300 - Linha: X. Valor informado para o campo DT_RECEB (posição 6): <<valor informado>>, deve estar compreendido no período atual da escrituração”  Validações Registro M700:  Considerar as mesmas validações realizadas no M300 | MFS-689652 |
| RN11 | Validações: M110/M115: Registro M110  IND_AJ Se o campo não for preenchido com uma das opções válidas, exibir a mensagem:  “Registro M110 - Linha: X. – Valor inválido para o campo IND_AJ (Posição 2): Não informado. Esperado: 0) Redução, 1) Acréscimo.” VL_AJ Se o campo obrigatório, não for preenchido, exibir a mensagem:  “Registro M110 - Linha: X. – Valor inválido para o campo VL_AJ (Posição 3): Não informado. Esperado até 15 inteiros e 2 decimais. COD_AJ Se o campo obrigatório, não for preenchido, exibir a mensagem:  “Registro M110 - Linha: X. – Valor inválido para o campo COD_AJ (Posição 4): .Conforme tabela 4.3.8.  Registro M115   Quando removido o registro pai, exibir a mensagem:  “M115 – Linha X: Registro PAI (M110/M510) Removido.” Quando rejeitado o registro pai, exibir a mensagem:  “M115 – Linha X: Registro PAI (M110/M510) Rejeitado.”  REG Se o tipo de registro for um tipo inválido, exibir a mensagem:  “Registro M115 - Linha: X. – Tipo de registro inválido: <<Valor informado.>> Esperado: M115 Campos obrigatórios não preenchido DET_VALOR_AJ Se o campo obrigatório, não for preenchido, exibir a mensagem:  “Registro M115 - Linha: X. – Valor inválido para o campo DET_VL_AJ (Posição 2):Não Informado. Esperado até 15 inteiros e 2 decimais. COD/CST Se o campo não for preenchido com valor válido, exibir a mensagem:  “Registro M115 - Linha: X. – Valor inválido para o campo COD_CST (Posição 3):<<valor informado>> DET_BC_CRED Se o campo obrigatório, não for preenchido, exibir a mensagem:  “Registro M115 - Linha: X. – Valor inválido para o campo DET_BC_DEC (Posição 4):Não Informado. Esperado  DET_ALIQ Se o campo obrigatório, não for preenchido, exibir a mensagem:  “Registro M115 - Linha: X. – Valor inválido para o campo DET_ALIQ (Posição 5):Não Informado. Esperado até 8 inteiros e 4 decimais. DT_OPER_AJ Se o campo obrigatório, não for preenchido, exibir a mensagem:  “Registro M115 - Linha: X. – Valor inválido para o campo DT_OPER_AJ (Posição 6):Não Informado. Esperado yyyymmdd.  Validações Registro M510/M515:  Considerar as mesmas validações realizadas no M110/M115 | MFS-689652 |
|  | M100, M110, M115, M500, M510, M515, M205, M210, M220, M230, M300, M605, M610, M620, M630 e M700 |  |
