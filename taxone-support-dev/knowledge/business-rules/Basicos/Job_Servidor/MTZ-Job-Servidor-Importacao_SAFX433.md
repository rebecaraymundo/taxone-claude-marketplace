# MTZ-Job-Servidor-Importacao_SAFX433

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX433.docx
- **Modificado:** 2026-02-12
- **Tamanho:** 65 KB

---

Job Servidor – SAFX433

Controle de Crédito de Injeção de Energia Elétrica

__Localização:__

__Módulo: __Básicos 🡪 Job Servidor

__Menu: __Carga__ __🡪 Programação 🡪 Execução

Importação 🡪 Programação 🡪 Execução

Importação batch 🡪 Programação 🡪 Execução

\(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX433 conforme o Manual de Layout, o que facilita a consulta\. Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00\)\.

DOCUMENTO DE REQUISITO

DR

Nome

__Descrição__

__MFS981988__

Liliane Videira Assaf

Criação da Importação da SAFX433

[1\.	Introdução	1](#_Toc217928742)

[2\.	Regras de Negócio	1](#_Toc217928743)

[RN00 – Estrutura da SAFX433 – Controle de Crédito de Injeção de Energia Elétrica	1](#_Toc217928744)

[RN01 – Código da Empresa \(COD\_EMPRESA\)	1](#_Toc217928745)

[RN02 – Código do Estabelecimento \(COD\_ESTAB\)	1](#_Toc217928746)

[RN03 – Período de Referência da Apuração \(DAT\_APURACAO\)	1](#_Toc217928747)

[RN04 – Número da Instalação da Unidade Injetora \(NUM\_INSTAL\_INJ\)	1](#_Toc217928748)

[RN05 – Período de Referência da Injeção \(DAT\_REF\_INJ\)	1](#_Toc217928749)

[RN06 – Posto Tarifário da Energia Injetada \(COD\_POSTO\_INJ\)	1](#_Toc217928750)

[RN07 – Tarifa da Energia Injetada \(VLR\_TARIFA\_INJ\)	1](#_Toc217928751)

[RN08 – Quantidade Inicial de Energia em kWh \(QTD\_ENERGIA\_INI\)	1](#_Toc217928752)

[RN09 – Quantidade de Energia Elétrica Injetada em kWh \(QTD\_ENERGIA\_INJ\)	1](#_Toc217928753)

[RN10 – Quantidade de Saída de Energia Elétrica em kWh \(QTD\_ENERGIA\_SAI\)	1](#_Toc217928754)

[RN11 – Quantidade Final de Energia em kWh \(QTD\_ENERGIA\_FIM\)	1](#_Toc217928755)

# <a id="_Toc217928742"></a>Introdução 

Esse documento matriz tem objetivo de descrever as regras de consistências executadas na importação da SAFX433\.

# <a id="_Toc217928743"></a>Regras de Negócio

## <a id="_Toc217928744"></a>RN00 – Estrutura da SAFX433 – Controle de Crédito de Injeção de Energia Elétrica

__Tabela Definitiva:__ X433\_CTRL\_CRED\_EE

__Estrutura da SAFX433:__

__Obrig__

__Item__

__Descrição__

__Campo__

__Tam__

__Tipo__

\(\*\)

01

Código da Empresa

COD\_EMPRESA

003

A

\(\*\)

02

Código do Estabelecimento

COD\_ESTAB

006

A

\(\*\)

03

Período de Referência da Apuração

DAT\_APURACAO

008

N

\(\*\)

04

Número da Instalação da Unidade Injetora

NUM\_INSTAL\_INJ

012

A

\(\*\)

05

Período de Referência da Injeção

DAT\_REF\_INJ

008

N

\(\*\)

06

Posto Tarifário da Energia Injetada

COD\_POSTO\_INJ

002

A

07

Tarifa da Energia Injetada

VLR\_TARIFA\_INJ

005V006

N

08

Quantidade Inicial de Energia em kWh

QTD\_ENERGIA\_INI

010V003

N

09

Quantidade de Energia Elétrica Injetada em kWh

QTD\_ENERGIA\_INJ

009V003

N

10

Quantidade de Saída de Energia Elétrica em kWh

QTD\_ENERGIA\_SAI

009V003

N

11

Quantidade Final de Energia em kWh

QTD\_ENERGIA\_FIM

010V003

N

__Sobre as mensagens de erro:__

Todas as mensagens gravadas no log de erros da importação, devem mostrar os dados de identificação do registro, para permitir ao usuário a identificação do registro com erro\.

## <a id="_Toc217928745"></a>RN01 – Código da Empresa \(COD\_EMPRESA\)

O campo COD\_EMPRESA é de preenchimento obrigatório\.

Quando o campo não for preenchido, o registro não será importado e será gravada no log de erros: 

__90001 – Codigo de Empresa nao esta preenchido__

## <a id="_Toc217928746"></a>RN02 – Código do Estabelecimento \(COD\_ESTAB\)

O campo COD\_ESTAB é de preenchimento obrigatório\.

Quando o campo não for preenchido, o registro não será importado e será gravada no log de erros: 

__90002 – Codigo de Estabelecimento deve ser preenchido__

## <a id="_Toc217928747"></a>RN03 – Período de Referência da Apuração \(DAT\_APURACAO\)

O campo DAT\_APURACAO é de preenchimento obrigatório\.

Quando o campo não for preenchido, o registro não será importado e será gravada no log de erros: 

__93800 – Período de Referência da Apuração nao preenchido ou invalido__

O campo DAT\_APURACAO deve ser uma data válida no formato AAAAMMDD\. 

Quando o campo for preenchido com informação que não é uma data válida, o registro não será importado e será gravada no log de erros: 

__93800 – Período de Referência da Apuração nao preenchido ou invalido__

O campo DAT\_APURACAO deve ser igual ao último dia do mês\. 

Quando o campo não corresponder ao último dia do mês, o registro não será importado e será gravada no log de erros: 

__93801 – Período de Referência da Apuração deve ser igual ao ultimo dia do mes__

## <a id="_Toc217928748"></a>RN04 – Número da Instalação da Unidade Injetora \(NUM\_INSTAL\_INJ\)

O campo NUM\_INSTAL\_INJ é de preenchimento obrigatório\.

Quando o campo não for preenchido, o registro não será importado e será gravada no log de erros: 

__93802 – Número da Instalação da Unidade Injetora deve ser preenchido\.__

## <a id="_Toc217928749"></a>RN05 – Período de Referência da Injeção \(DAT\_REF\_INJ\)

O campo DAT\_REF\_INJ é de preenchimento obrigatório\.

Quando o campo não for preenchido, o registro não será importado e será gravada no log de erros: 

__93803 – Período de Referência da Injeção nao preenchido ou invalido__

O campo DAT\_REF\_INJ deve ser uma data válida no formato AAAAMMDD\. 

Quando o campo for preenchido com informação que não é uma data válida, o registro não será importado e será gravada no log de erros: 

__93803 – Período de Referência da Injeção nao preenchido ou invalido__

O campo DAT\_REF\_INJ deve ser igual ao último dia do mês\. 

Quando o campo não corresponder ao último dia do mês, o registro não será importado e será gravada no log de erros: 

__93804 – Período de Referência da Injeção deve ser igual ao ultimo dia do mes__

## <a id="_Toc217928750"></a>RN06 – Posto Tarifário da Energia Injetada \(COD\_POSTO\_INJ\)

O campo COD\_POSTO\_INJ é de preenchimento obrigatório\.

Quando o campo não for preenchido, o registro não será importado e será gravada no log de erros: 

__93805 – Posto Tarifário da Energia Injetada deve ser preenchido com um valor valido\. Valores Validos: FP, IN, PO\.__

O campo COD\_POSTO\_INJ deve ser preenchido com um valor válido: FP, IN, PO\. 

Quando o campo for preenchido com valor diferente de FP, IN ou PO, o registro não será importado e será gravada no log de erros: 

__93805 – Posto Tarifário da Energia Injetada deve ser preenchido com um valor valido\. Valores Validos: FP, IN, PO\.__

## <a id="_Toc217928751"></a>RN07 – Tarifa da Energia Injetada \(VLR\_TARIFA\_INJ\)

O campo VLR\_TARIFA\_INJ não é obrigatório, mas quando preenchido, deve ser um valor decimal/numerico válido\.

Quando o campo for preenchido com valor inválido, o registro não será importado e será gravada no log de erros: 

__90461 – Valor Decimal ou Numerico com formato invalido\.__

## <a id="_Toc217928752"></a>RN08 – Quantidade Inicial de Energia em kWh \(QTD\_ENERGIA\_INI\)

O campo QTD\_ENERGIA\_INI não é obrigatório, mas quando preenchido, deve ser um valor decimal/numerico válido\.

Quando o campo for preenchido com valor inválido, o registro não será importado e será gravada no log de erros: 

__90461 – Valor Decimal ou Numerico com formato invalido\.__

## <a id="_Toc217928753"></a>RN09 – Quantidade de Energia Elétrica Injetada em kWh \(QTD\_ENERGIA\_INJ\)

O campo QTD\_ENERGIA\_INJ não é obrigatório, mas quando preenchido, deve ser um valor decimal/numerico válido\.

Quando o campo for preenchido com valor inválido, o registro não será importado e será gravada no log de erros: 

__90461 – Valor Decimal ou Numerico com formato invalido\.__

## <a id="_Toc217928754"></a>RN10 – Quantidade de Saída de Energia Elétrica em kWh \(QTD\_ENERGIA\_SAI\)

O campo QTD\_ENERGIA\_SAI não é obrigatório, mas quando preenchido, deve ser um valor decimal/numerico válido\.

Quando o campo for preenchido com valor inválido, o registro não será importado e será gravada no log de erros: 

__90461 – Valor Decimal ou Numerico com formato invalido\.__

## <a id="_Toc217928755"></a>RN11 – Quantidade Final de Energia em kWh \(QTD\_ENERGIA\_FIM\)

O campo QTD\_ENERGIA\_FIM não é obrigatório, mas quando preenchido, deve ser um valor decimal/numerico válido\.

Quando o campo for preenchido com valor inválido, o registro não será importado e será gravada no log de erros: 

__90461 – Valor Decimal ou Numerico com formato invalido\.__

