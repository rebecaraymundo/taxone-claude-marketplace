# MTZ_UPLOAD_Arq.CSV_TXT_M100_M110_M115_M500_M510_M515

> Fonte: MTZ_UPLOAD_Arq.CSV_TXT_M100_M110_M115_M500_M510_M515.docx






THOMSON REUTERS

(EFD- Escrituração Fiscal Digital das Contribuições)
UPLOAD
(Estrutura dos Arquivos CSV e TXT)



DOCUMENTO DE REQUISITO






Sumário

1.	TELA	3
2.	Regras dos Campos	3
3.	Abas Geradas	8

Objetivo

O objetivo desta funcionalidade é permitir importação, dos arquivos de créditos dos registros M100_M110_M115_M500_M510_M515, de ajustes complementares da apuração do pis e cofins e também para que esses dados sejam computados na geração do meio magnético do EFD_Contribuições, via solução fiscal TaxOne.

Tela






Regras dos Campos

Localização da tela: Módulo: SPED>> EFD – Escrituração Fiscal Digital das Contribuições
Menu: Obrigações >> Manutenção >> Apuração Geral PIS/COFINS

Título da tela: Upload dos ajustes complementares da Apuração M100_M110_M115_M500_M510_M515.

Nomenclatura dos Arquivos: O nome dos arquivos deve seguir o padrão EPCARQ_ Prefixo (6 posições) e com separador Underline ('_').

EPCARQ_<COD_REG>_<COD_EMP>_<COD_ESTAB>_<ANO_MES_DA_APURACAO>.csv
EPCARQ_<COD_REG>_<COD_EMP>_<COD_ESTAB>_<ANO_MES_DA_APURACAO>.txt

<COD_REG> = Valores possíveis: M100 e M500
<COD_EMP> = Código da Empresa
<COD_ESTAB> = Código do Estabelecimento
<ANO_MES_DA_APURACAO> = Ano e Mês da Apuração no formato: yyyymm



3.1      Registro M100/M500: Crédito de PIS/Pasep e COFINS Relativo ao Período.
Este registro tem por finalidade realizar a consolidação do crédito relativo à contribuição para o PIS/PASEP e COFINS apurado no período. Deve ser gerado um registro M100/M500, específico para cada tipo de crédito apurado (vinculados à receita tributada, vinculados à receita não tributada e vinculados à exportação), conforme a Tabela de tipos de créditos “Tabela 4.3.6”, bem como para créditos de operações próprias e créditos transferidos por eventos de sucessão.



Notas;

Campos Chave: o registro deve existir na tabela EPC_REG_AJT_M100_M500.

É obrigatório que uma das duas alíquotas seja informada.


3.2      Registro M110/M510: Ajustes do Crédito de PIS/Pasep e COFINS Apurado.

Registro a ser preenchido caso a pessoa jurídica tenha de proceder a ajustes de créditos escriturados no período, decorrentes de ação judicial, de processo de consulta, da legislação tributária das contribuições sociais, de estorno ou de outras situações.

Este registro será utilizado pela pessoa jurídica para detalhar as informações prestadas nos campos 09 e 10 do registro pai M100/M500.

Deve ser informado neste registro, como ajuste de redução (Indicador “0”) o valor referente às devoluções de compras ocorridas no período, de bens e mercadorias sujeitas à incidência não cumulativa da Contribuição que, quando da aquisição gerou a apuração de créditos.




Notas;

Campos Chave.

Registro PAI: M100/M500.



Registro M115/M515: Detalhamento dos Ajustes do Crédito de PIS/Pasep e COFINS Apurado.

Registro a ser preenchido para a pessoa jurídica detalhar a operação e valor a que se refere o ajuste de crédito informado no registro pai – M110/M510.



Notas;

Campos Chave.

Registro PAI: M110/M510.

Será rejeitado se o registro PAI tiver sido removido.

Será rejeitado se o registro PAI tiver sido rejeitado


| MFS | Nome | Descrição |
| --- | --- | --- |
| MFS-689652 | Rosemeire Santos | Criação do Documento |
| MFS-689652 | Rosemeire Santos | Este documento tem como objetivo, detalhar a estrutura e upload dos arquivos dos Registros M100_M110_M115_M500_M510_M515. |


| Registros M100/M500 | Registros M100/M500 | Registros M100/M500 | Registros M100/M500 | Registros M100/M500 | Registros M100/M500 | Registros M100/M500 | Registros M100/M500 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Número | Campo | Descrição | Tipo | Tamanho | Decimais | Obrigatório | Regras |
| 1 | REG (*) | Código do registro | C | 4 | 0 | Sim | Campo destinado ao código do registro. Valores válidos: M100/M500. |
| 2 | COD_CRED (*) | Código de Tipo de Crédito apurado no período | N | 3 | 0 | Sim | Código de Tipo de Crédito apurado no período, conforme a Tabela 4.3.6 |
| 3 | ALIQ_PIS_COFINS (*) | Alíquota do PIS/COFINS em Percentual | N | 8 | 4 | Não | Campo destinado a Alíquota (em percentual) |
| 4 | ALIQ_PIS_COFINS_QUANT (*) | Alíquota do PI/COFINS em Quantidade | N | 8 | 4 | Não | Campo destinado a Alíquota (em reais) |


| Registro M110/M510 | Registro M110/M510 | Registro M110/M510 | Registro M110/M510 | Registro M110/M510 | Registro M110/M510 | Registro M110/M510 | Registro M110/M510 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Número | Campo | Descrição | Tipo | Tamanho | Decimais | Obrigatório | Regras |
| 1 | REG (*) | Código do registro | C | 4 | 0 | Sim | Campo destinado ao código do registro. Valores válidos: M110/M510. |
| 2 | IND_AJ (*) | Indicador do tipo de ajuste | N | 1 | 0 | Sim | Campo destinado ao tipo de ajustes: 0- Ajuste de redução; 1- Ajuste de acréscimo. |
| 3 | VL_AJ | Valor do ajuste | N | 15 | 2 | Sim | Campo destinado ao valor do ajuste. |
| 4 | COD_AJ (*) | Código do ajuste | C | 10 | 0 | Sim | Código do ajuste, conforme a Tabela indicada no item 4.3.8 |
| 5 | NUM_DOC (*) | Número do processo, documento ou ato concessório (se houver) | C | 100 | 0 | Não | Campo destinado ao Número do processo, documento ou ato concessório ao qual o ajuste está vinculado, se houver. |
| 6 | DESCR_AJ (*) | Descrição resumida do ajuste | C | 400 | 0 | Não | Campo destinado a descrição resumida do ajuste |
| 7 | DT_REF | Data de referência do ajuste | D | 8 | 0 | Não | Campo destinado a Data de referência do ajuste (formato:aaaammdd). |
| 8 | TEXTO | Texto aberto | C | 100 | 0 | Não | Campo destinado a remoção do registro (Escrever "REMOVER" para excluir o registro). Qualquer outro valor será ignorado |


| Registro M115/M515 | Registro M115/M515 | Registro M115/M515 | Registro M115/M515 | Registro M115/M515 | Registro M115/M515 | Registro M115/M515 | Registro M115/M515 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Número | Campo | Descrição | Tipo | Tamanho | Decimais | Obrigatório | Regras |
| 1 | REG (*) | Código do registro | C | 4 | 0 | Sim | Campo destinado ao código do registro. Valores válidos: M115/M515. |
| 2 | DET_VALOR_AJ (*) | Detalhamento do valor ajustado | N | 15 | 2 | Sim | Campo destinado Detalhamento do valor do crédito reduzido ou acrescido, informado no Campo 03 (VL_AJ) do registro M110 |
| 3 | COD_CST (*) | Código CST do PIS/COFINS | N | 2 | 0 | Sim | Campo destinado ao Código da Situação Tributária, conforme tabela TACES65 - Códigos Situação Tributária. |
| 4 | DET_BC_CRED | Detalhamento da base de cálculo geradora de ajuste de crédito | N | 15 | 2 | Sim | Campo destinado ao detalhamento da base de cálculo geradora de ajuste de crédito |
| 5 | DET_ALIQ (*) | Detalhamento da alíquota a que se refere o ajuste de crédito | N | 6 | 2 | Sim | Campo destinado ao detalhamento da alíquota a que se refere o ajuste de crédito |
| 6 | DT_OPER_AJ (*) | Data da operação a que se refere o ajuste informado neste registro. | N | 8 | 0 | Sim | Campo destinado a data da operação a que se refere o ajuste informado neste registro (formato:aaaammdd). |
| 7 | DESC_AJ | Descrição da(s) operação(ões) a que se refere o valor informado no Campo 02 (DET_VALOR_AJ) | C | 400 | 0 | Não | Campo destinado a descrição da(s) operação(ões), a que se refere o valor informado no Campo 02 (DET_VALOR_AJ). |
| 8 | COD_CONTA (*) | Código da conta contábil debitada/creditada | C | 70 | 0 | Não | Campo destinado ao Código da Conta e Subconta Contábil, conforme tabela do Plano de Contas (SAFX2002). |
| 9 | INFO_COMPL | Informação complementar | C | 400 | 0 | Não | Campo destinado a informação complementar. |
| 10 | TEXTO | Texto aberto | C | 100 | 0 | Não | Campo destinado a remoção do registro (Escrever "REMOVER" para excluir o registro). Qualquer outro valor será ignorado |
