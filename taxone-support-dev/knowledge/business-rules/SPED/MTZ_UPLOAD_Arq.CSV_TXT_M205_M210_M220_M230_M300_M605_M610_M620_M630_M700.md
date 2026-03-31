# MTZ_UPLOAD_Arq.CSV_TXT_M205_M210_M220_M230_M300_M605_M610_M620_M630_M700

> Fonte: MTZ_UPLOAD_Arq.CSV_TXT_M205_M210_M220_M230_M300_M605_M610_M620_M630_M700.docx






THOMSON REUTERS

(EFD- Escrituração Fiscal Digital das Contribuições)
UPLOAD
(Estrutura dos Arquivos CSV e TXT)



DOCUMENTO DE REQUISITO






Sumário

1.	TELA	3
2.	Regras dos Campos	3
3.	Abas Geradas	8

## Objetivo


O objetivo desta funcionalidade é permitir importação, dos arquivos da contribuição dos registros M205_M210_M220_M225_M230_M300_M605_M610_M620_M625_M630_M700, de ajustes complementares da apuração do pis e cofins e também para que esses dados sejam computados na geração do meio magnético do EFD_Contribuições, via solução fiscal TaxOne.

## Tela












## Regras dos Campos


Localização da tela: Módulo: SPED>> EFD – Escrituração Fiscal Digital das Contribuições
Menu: Obrigações >> Manutenção >> Apuração Geral PIS/COFINS


Título da tela: Upload dos ajustes complementares da Apuração M205_M210_M220_M225_M230_M300_M605_M610_M620_M625_M630_M700.

Nomenclatura dos Arquivos: O nome dos arquivos deve seguir o padrão EPCARQ_ Prefixo (6 posições) e com separador Underline ('_').

EPCARQ_<COD_REG>_<COD_EMP>_<COD_ESTAB>_<ANO_MES_DA_APURACAO>.csv
EPCARQ_<COD_REG>_<COD_EMP>_<COD_ESTAB>_<ANO_MES_DA_APURACAO>.txt

<COD_REG> = Valores possíveis: M205, M210, M605, M610
<COD_EMP> = Código da Empresa
<COD_ESTAB> = Código do Estabelecimento
<ANO_MES_DA_APURACAO> = Ano e Mês da Apuração no formato: yyyymm


Registros M205/M605: Contribuição para o PIS/Pasep e COFINS a Recolher – Detalhamento por Código de Receita.

Neste registro será informado, por código de receita (conforme códigos de débitos informados em DCTF), o detalhamento da contribuição a recolher informada nos campos 08 (regime não cumulativo) e 12 (regime cumulativo) do Registro Pai M200/M600.

Atenção:
1. O código a ser informado no campo 03 (COD_REC) não é o código que consta no DARF (composto de quatro números), mas sim, o código identificador da contribuição na Ficha “Débitos” da DCTF (composto de seis números).
2. O somatório dos valores informados no campo 04 (VL_DÉBITO) informado neste registro, deve corresponder ao valor constante de contribuição a recolher, do Registro Pai M200/M600.











Registros M210/M610: Detalhamento da Contribuição para o PIS/Pasep e COFINS do Período.

Será gerado um Registro “M210/M610” para cada situação geradora contribuição social, especificada na Tabela “4.3.5 – Código de Contribuição Social Apurada”, recuperando os valores referentes às diversas bases de cálculo escriturados nos registros dos Blocos “A”, “C”, “D” e “F”.
Caso sejam recuperados registros dos Blocos “A”, “C”, “D” ou “F” referentes a uma mesma situação com incidência de contribuição social (conforme Tabela 4.3.5), mas sujeitas a mais de uma alíquota de apuração, deve ser escriturado um Registro “M210/M610” em relação a cada alíquota existente na escrituração. Dessa forma a chave do registro é formada pelos campos COD_CONT + ALIQ_PIS_QUANT + ALIQ_PIS.





Notas;

* Campos Chave: o registro deve existir na tabela EPC_REG_AJT_M210_M610.

É obrigatório que uma das duas alíquotas seja informada.



Registros M220/M620: Ajustes da Contribuição para o PIS/Pasep e COFINS Apurada.

Este registro será utilizado pela pessoa jurídica para detalhar as informações prestadas nos campos 09 e 10 do registro pai M210/M610.


Notas;

*Campos Chave.

Registro PAI: M210/M610.


Registros M225/M625: Detalhamento dos Ajustes da Contribuição Para o Pis/Pasep e COFINS Apurada.

Registro a ser preenchido para a pessoa jurídica detalhar a operação e valor a que se refere o ajuste da contribuição informado no registro pai – M220/M620.




Notas;

*Campos Chave.

Registro PAI: M220/M620.

Será rejeitado se o registro PAI tiver sido removido.

Será rejeitado se o registro PAI tiver sido rejeitado.


Registro M230/M630: Informações Adicionais de Diferimento.

Este registro será utilizado pela pessoa jurídica para detalhar as informações prestadas no campo 11 (VL_CONT_DIFER) do registro pai M210/M610, referente às receitas ainda não recebidas decorrentes da celebração de contratos com pessoa jurídica de direito público, empresa pública, sociedade de economia mista ou suas subsidiárias, relativos à construção por empreitada ou a fornecimento a preço predeterminado de bens ou serviços (parágrafo único e no caput do art. 7º da Lei nº 9.718, de 1998).

Os créditos da não-cumulatividade vinculados a estas receitas ainda não recebidas também deverão ser detalhados neste registro, sendo que o somatório dos campos 11 (VL_CRED_DIF) do registro M100 deverá ser igual ao somatório dos campos VL_CRED_DIF dos registros M230/M630, para o mesmo COD_CRED.
O somatório do campo 05 (VL_CONT_DIF) destes registros deverá ser igual ao valor lançado no respectivo campo 11 do registro pai M210/M610.

Deverá existir um registro M230/M630 para cada CNPJ em que houve contribuição diferida no período e para cada código.








Notas;

Campos Chave.

Registro PAI: M210/M610.

Valor do campo VL_CRED_DIF (posição 6) deve ser MAIOR que ZERO se o campo COD_CRED (posição 7) for informado.
Valor do campo VL_CRED_DIF (posição 6) deve ser ZERO se o campo COD_CRED (posição 7) NÃO for informado.

O código de crédito informado deve estar presente no registro M100/M500.


Registro M300/M700: Contribuição de PIS/PASEP e COFINS Diferida em Períodos Anteriores – Valores a Pagar no Período.

Este registro será utilizado pela pessoa jurídica para detalhar as informações prestadas no campo 12 (VL_CONT_DIFER_ANT) dos diversos registros M210/M610 existentes na escrituração.

Os valores da contribuição diferida em períodos anteriores, que deverão ser pagos no atual período da escrituração, face aos recebimentos ocorridos no mês, descontados dos respectivos créditos diferidos, serão adicionados à respectiva contribuição calculada (COD_CONT) no registro M210/M610, sendo que a soma dos valores do campo 12 de todos os registros M210/M610 deverá ser igual a soma dos campos VL_CONT_DIFER_ANT dos registros M300/M700, para um mesmo COD_CONT.

Deverá existir um registro M300/M700 para cada data em que houve recebimento de receita objeto de diferimento, de maneira combinada com o período da escrituração em que o diferimento ocorreu e para cada tipo de contribuição diferida e natureza do crédito diferido a descontar no período. Assim, a chave deste registro é formada pelos campos COD_CONT + NAT_CRED_DESC + PER_APUR + DT_RECEB.



Notas;

* Campos Chave.

Registro PAI: M210/M610.

O valor de VL_CONT_APUR_DIFER menos VL_CRED_DESC_DIFER não pode resultar em valor negativo.

O valor de PER_APUR não pode ser o período atual da apuração.

O valor de DT_RECEB deve estar dentro do período atual da apuração.

| MFS | Nome | Descrição |
| --- | --- | --- |
| MFS-689652 | Rosemeire Santos | Criação do Documento |
| MFS-689652 | Rosemeire Santos | Este documento tem como objetivo, detalhar a estrutura e upload dos arquivos dos Registros M205_M210_M220_M225_M230_M300_M605_M610_M620_M625_M630_M700. |


| Registros M205/M605 | Registros M205/M605 | Registros M205/M605 | Registros M205/M605 | Registros M205/M605 | Registros M205/M605 | Registros M205/M605 | Registros M205/M605 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Número | Campo | Descrição | Tipo | Tamanho | Decimais | Obrigatório | Regras |
| 1 | REG (*) | Código do registro | C | 4 | 0 | Sim | Campo destinado ao código do registro. Valores válidos: M205/M605 |
| 2 | NUM_CAMPO | Número do Campo do registro | C | 2 | 0 | Sim | Campo destinado ao número do campo do registro “M205/M605” para o tipo de contribuição. Valores válidos: 08 - Contribuição Não Cumulativa; 12 - Contribuição Cumulativa. |
| 3 | COD_REC (*) | Código da Receita referente à contribuição | C | 10 | 0 | Sim | Campo destinado ao código da receita do PIS/PASEP referente à contribuição a recolher, detalhada neste registro. Preencher de acordo com a Tabela de Códigos de Receitas (TACES14). |
| 4 | VL_DEBITO | Valor do Débito correspondente ao código do campo 3 | N | 15 | 2 | Sim | Campo destinado ao Valor do Débito correspondente ao código da receita informado. |
| 5 | TEXTO | Texto aberto | C | 100 | 0 | Não | Campo destinado a remoção do registro (Escrever "REMOVER" para excluir o registro). Qualquer outro valor será ignorado |


| Registros M210/M610 | Registros M210/M610 | Registros M210/M610 | Registros M210/M610 | Registros M210/M610 | Registros M210/M610 | Registros M210/M610 | Registros M210/M610 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Número | Campo | Descrição | Tipo | Tamanho | Decimais | Obrigatório | Regras |
| 1 | REG (*) | Código do registro | C | 4 | 0 | Sim | Campo destinado ao código do registro. Valores válidos: M210/M610 |
| 2 | COD_CONT (*) | Código da Contribuição Social apurada no período | N | 2 | 0 | Sim | Código da contribuição social apurada no período, conforme a Tabela 4.3.5. Valores válidos: 01 Contribuição não-cumulativa apurada a alíquota básica 02 Contribuição não-cumulativa apurada a alíquotas diferenciadas 03 Contribuição não-cumulativa apurada a alíquota por unidade de medida de produto 04 Contribuição não-cumulativa apurada a alíquota básica – Atividade Imobiliária 31 Contribuição apurada por substituição tributaria 32 Contribuição apurada por substituição tributaria – Vendas a Zona Franca de Manaus 51 Contribuição cumulativa apurada a alíquota básica 52 Contribuição cumulativa apurada a alíquotas diferenciadas 53 Contribuição cumulativa apurada a alíquota por unidade de medida de produto 54 Contribuição cumulativa apurada a alíquota básica – Atividade Imobiliária 70 Contribuição apurada da Atividade Imobiliária – RET 71 Contribuição apurada de SCP – Incidência Não Cumulativa 72 Contribuição apurada de SCP – Incidência Cumulativa 99 Contribuição para o PIS/PASEP – Folha de Salários. |
| 3 | ALIQ_PIS_COFINS (*) | Alíquota do PIS/COFINS em Percentual | N | 8 | 4 | Não | Campo destinado a Alíquota (em percentual) |
| 4 | ALIQ_PIS_COFINS_QUANT (*) | Alíquota do PI/COFINS em Quantidade | N | 8 | 4 | Não | Campo destinado a Alíquota (em reais) |


| Registros M220/M620 | Registros M220/M620 | Registros M220/M620 | Registros M220/M620 | Registros M220/M620 | Registros M220/M620 | Registros M220/M620 | Registros M220/M620 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Número | Campo | Descrição | Tipo | Tamanho | Decimais | Obrigatório | Regras |
| 1 | REG (*) | Código do registro | C | 4 | 0 | Sim | Campo destinado ao código do registro. Valores validos: M220/M620 |
| 2 | IND_AJ (*) | Indicador do tipo de ajuste | N | 1 | 0 | Sim | Campo destinado ao indicador do tipo de ajuste. Valores válidos: 0 - Ajuste de redução 1 - Ajuste de acréscimo. |
| 3 | VL_AJ | Valor do ajuste | N | 15 | 2 | Sim | Campo destinado ao valor do ajuste |
| 4 | COD_AJ (*) | Código do ajuste | C | 10 | 0 | Sim | Campo destinado ao código do ajuste. Valores válidos: 01-Ajuste Oriundo de Ação Judicial 02-Ajuste Oriundo de Processo Administrativo 03-Ajuste Oriundo da Legislação Tributária 04-Ajuste Oriundo Especificamente do RTT 05-Ajuste Oriundo de Outras Situações 06-Estorno. |
| 5 | NUM_DOC (*) | Número do processo, documento ou ato concessório (se houver) | C | 100 | 0 | Não | Campo destinado ao Número do processo, documento ou ato concessório. |
| 6 | DESCR_AJ | Descrição resumida do ajuste | C | 400 | 0 | Não | Campo destinado à descrição do ajuste |
| 7 | DT_REF | Data de referência do ajuste | D | 8 | 0 | Não | Campo destinado a data de referência do ajuste. |
| 8 | TEXTO | Texto aberto | C | 100 | 0 | Não | Campo destinado a remoção do registro (Escrever "REMOVER" para excluir o registro). Qualquer outro valor será ignorado |


| Registros M225/M625 | Registros M225/M625 | Registros M225/M625 | Registros M225/M625 | Registros M225/M625 | Registros M225/M625 | Registros M225/M625 | Registros M225/M625 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Número | Campo | Descrição | Tipo | Tamanho | Decimais | Obrigatório | Regras |
| 1 | COD_REG (*) | Código do registro | C | 4 | 0 | Sim | Campo destinado ao código do registro. Valores válidos: M225/M625. |
| 2 | DET_VALOR_AJ (*) | Detalhamento do valor ajustado | N | 15 | 2 | Sim | Campo destinado ao Detalhamento do Valor do Ajuste. |
| 3 | COD_CST (*) | Código CST do PIS/COFINS | N | 2 | 0 | Sim | Campo destinado ao Código da Situação Tributária, conforme tabela TACES65 - Códigos Situação Tributária. |
| 4 | DET_BC_CRED | Detalhamento da base de cálculo geradora de ajuste de contribuição | N | 15 | 2 | Sim | Campo destinado ao Detalhamento do valor da Base de Cálculo do crédito do PIS. |
| 5 | DET_ALIQ (*) | Detalhamento da alíquota a que se refere o ajuste de contribuição | N | 6 | 2 | Sim | Campo destinado ao Detalhamento da Alíquota do PIS. |
| 6 | DT_OPER_AJ (*) | Data da operação a que se refere o ajuste informado neste registro. | N | 8 | 0 | Sim | Campo destinado a Data de Operação do Ajuste. |
| 7 | DESC_AJ | Descrição da(s) operação(ões) a que se refere o valor informado no Campo 02 (DET_VALOR_AJ) | C | 400 | 0 | Não | Campo destinado a Descrição do Ajuste. |
| 8 | COD_CTA (*) | Código da conta contábil debitada/creditada | C | 70 | 0 | Não | Campo destinado ao Código da Conta e Subconta Contábil, conforme tabela do Plano de Contas (SAFX2002). |
| 9 | INFO_COMPL | Informação complementar | C | 400 | 0 | Não | Campo destinado a informação Complementar. |
| 10 | TEXTO | Texto aberto | C | 100 | 0 | Não | Campo destinado a remoção do registro (Escrever "REMOVER" para excluir o registro). Qualquer outro valor será ignorado |


| Registros M230/M630 | Registros M230/M630 | Registros M230/M630 | Registros M230/M630 | Registros M230/M630 | Registros M230/M630 | Registros M230/M630 | Registros M230/M630 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Número | Campo | Descrição | Tipo | Tamanho | Decimais | Obrigatório | Regras |
| 1 | REG (*) | Código do registro | C | 4 | 0 | Sim | Campo destinado ao código do registro. Valores Válidos: M230/M630 |
| 2 | CNPJ (*) | CNPJ da pessoa jurídica de direito público, empresa pública, sociedade de economia mista ou suas subsidiárias. | N | 14 | 0 | Sim | Campo destinado ao CNPJ da pessoa jurídica de direito público, empresa pública, sociedade de economia mista ou suas subsidiárias |
| 3 | VL_VEND | Valor Total das vendas no período | N | 15 | 2 | Sim | Campo destinado ao Valor Total das Vendas no período |
| 4 | VL_NAO_RECEB | Valor Total não recebido no período | N | 15 | 2 | Sim | Campo destinado ao Valor total não recebido no período |
| 5 | VL_CONT_DIF | Data da operação a que se refere o ajuste informado neste registro. | N | 15 | 2 | Sim | Campo destinado ao Valor da contribuição diferida no período |
| 6 | VL_CRED_DIF | Valor do Crédito diferido no período | N | 15 | 2 | Sim | Campo destinado ao Valor do crédito diferido no período |
| 7 | COD_CRED (*) | Código de Tipo de Crédito diferido no período | C | 3 | 0 | Não | Conforme tabela 4.3.6. Valores Válidos: 101 - Crédito vinculado à receita tributada no mercado interno – Alíquota Básica 102 - Crédito vinculado à receita tributada no mercado interno – Alíquotas Diferenciadas 103 - Crédito vinculado à receita tributada no mercado interno – Alíquota por Unidade de Produto 104 - Crédito vinculado à receita tributada no mercado interno – Estoque de Abertura 105 - Crédito vinculado à receita tributada no mercado interno – Aquisição Embalagens para revenda 106 - Crédito vinculado à receita tributada no mercado interno – Presumido da Agroindústria 107 - Crédito vinculado à receita tributada no mercado interno – Outros Créditos Presumidos 108 - Crédito vinculado à receita tributada no mercado interno – Importação 109 - Crédito vinculado à receita tributada no mercado interno – Atividade Imobiliária 199 - Crédito vinculado à receita tributada no mercado interno – Outros 201 - Crédito vinculado à receita não tributada no mercado interno – Alíquota Básica 202 - Crédito vinculado à receita não tributada no mercado interno – Alíquotas Diferenciadas 203 - Crédito vinculado à receita não tributada no mercado interno – Alíquota por Unidade de Produto 204 - Crédito vinculado à receita não tributada no mercado interno – Estoque de Abertura 205 - Crédito vinculado à receita não tributada no mercado interno – Aquisição Embalagens para revenda 206 - Crédito vinculado à receita não tributada no mercado interno – Presumido da Agroindústria 207 - Crédito vinculado à receita não tributada no mercado interno – Outros Créditos Presumidos 208 - Crédito vinculado à receita não tributada no mercado interno – Importação 299 - Crédito vinculado à receita não tributada no mercado interno – Outros 301 - Crédito vinculado à receita de exportação – Alíquota Básica 302 - Crédito vinculado à receita de exportação – Alíquotas Diferenciadas 303 - Crédito vinculado à receita de exportação – Alíquota por Unidade de Produto 304 - Crédito vinculado à receita de exportação – Estoque de Abertura 305 - Crédito vinculado à receita de exportação – Aquisição Embalagens para revenda 306 - Crédito vinculado à receita de exportação – Presumido da Agroindústria 307 - Crédito vinculado à receita de exportação – Outros Créditos Presumidos 308 - Crédito vinculado à receita de exportação – Importação 399 - Crédito vinculado à receita de exportação – Outros |
| 8 | TEXTO | Texto aberto | C | 100 | 0 | Não | Campo destinado a remoção do registro. (Escrever "REMOVER" para excluir o registro). Qualquer outro valor será ignorado |


| Registros M300/M700 | Registros M300/M700 | Registros M300/M700 | Registros M300/M700 | Registros M300/M700 | Registros M300/M700 | Registros M300/M700 | Registros M300/M700 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Número | Campo | Descrição | Tipo | Tamanho | Decimais | Obrigatório | Regras |
| 1 | REG (*) | Código do registro | C | 4 | 0 | Sim | Campo destinado ao código do registro. Valores Válidos: M300/M700 |
| 2 | VL_CONT_APUR_DIFER | Valor da Contribuição Apurada, diferida em períodos anteriores. | N | 15 | 2 | Sim | Campo destinado ao Valor da Contribuição a Recolher, diferida em períodos anteriores (Campo 03 – Campo 05). Atenção: Este campo será calculado pelo sistema. Caso seja enviado algum valor, o mesmo será desconsiderado. |
| 3 | NAT_CRED_DESC (*) | Natureza do Crédito Diferido, vinculado à receita tributada no mercado interno, a descontar | C | 2 | 0 | Não | Campo destinado a Natureza do Crédito Diferido, vinculado à receita tributada no mercado interno, a descontar. Valores válidos: 01 – Crédito a Alíquota Básica 02 - Crédito a Alíquota Diferenciada 03 - Crédito a Alíquota por Unidade de Produto 04 - Crédito Presumido da Agroindústria |
| 4 | VL_CRED_DESC_DIFER | Valor do Crédito a Descontar vinculado à contribuição diferida. | N | 15 | 2 | Sim | Campo destinado ao Valor do crédito a descontar, vinculado à Contribuição diferida. |
| 5 | PER_APUR (*) | Período de apuração da contribuição social e dos créditos diferidos | C | 6 | 0 | Sim | Campo destinado ao Período da Apuração da contribuição social e dos créditos diferidos. (Formato: AAAAMM) |
| 6 | DT_RECEB (*) | Data de recebimento da receita, objeto de diferimento | C | 8 | 0 | Não | Campo destinado a Data de recebimento da receita, objeto de diferimento. |
| 7 | TEXTO | Texto aberto | C | 100 | 0 | Não | Campo destinado a remoção do registro (Escrever "REMOVER" para excluir o registro). Qualquer outro valor será ignorado |
