---
source: "MTZ-Report_Fiscal-Conferencia_do_FCEP-Utilities.doc"
category: Report_Fiscal
converted: auto
---

Report Fiscal - Conferência de Notas Fiscais/FECEP - Utilities

Localização:
Módulo: Básicos --> Report Fiscal
Menu: Gerenciais --> Documentos Fiscais  --> Conferência de Notas Fiscais/FECEP - Utilities


DOCUMENTO DE REQUISITO

DR
Nome
Descrição
OS3511-A
Criação de Relatório - Conferência de Notas Fiscais/FECEP - Utilities
Geração de um novo relatório onde sejam descriminados os documentos fiscais e itens de Utilities que possuem valores de FECEP.

MFS6705
Relatório CONFERENCIA NOTAS FISCAIS FECEP
Melhoria na geração do relatório CONFERENCIA NOTAS FISCAIS FECEP apareça a mensagem que o mesmo está sem movimento

REGRAS DE NEGÓCIO

Cód.
Descrição
DR
RN00
Regra geral - Critérios para a recuperação dos dados:

Para a geração deste relatório serão filtrados os  documentos fiscais e itens de Utilities que possuem valores de FECEP (Campo 103 e 104 da SAFX43).

- Origem dos dados: Tabelas de itens e documentos fiscais de Utilities ( SAFX42 e SAFX43);
- Quando o documento não possuir mostrar o resultado dos valores com zeros;
- Somente os dados que possuem um ou mais dos campos abaixo maiores que zero:

Descrição do Campo
TABELA
ITEM
Descrição do Campo
FECEP - ICMS
SAFX43
103
FECEP ICMS
FECEP - Alíquota de ICMS
SAFX43
104
FECEP - ALIQUOTA ICMS


- Considerar notas fiscais "Normais", "Canceladas" e "Refaturamento/ Substituto" no relatório (campo 21 da SAFX42, SITUACAO igual a "N" ou "S" ou "R");

- Considerar notas de "Mercadoria", "Serviço" e "Mercadoria e Serviço" (campo 50 da SAFX42, COD_CLASS_DOC_FIS igual a "1" ou "2" ou "3");

 
OS3511-A
RN01
Layout do Relatório

O layout do relatório deverá possuir um cabeçalho conforme os padrões de relatórios da Mastersaf e deverão apresentar os valores os seguintes campos:

Relatório de Conferência do FCEP - Utilities
Nome do Campo
TABELA
ITEM
Descrição do campo
Regra 
Documento
SAFX42
06
Número do Documento Fiscal

Serie / Subsérie
SAFX42
07/08
Série / Subsérie

Sub-Série
SAFX42
08
Subsérie

Data Fiscal
SAFX42
03
Data de Emissão/Escr. Fiscal

Modelo
SAFX42
13
Modelo de Documento

UF
SAFX04
19
UF
Unidade de Federação da Pessoa Física/Jurídica correspondente aos campos 04 e 05 da SAFX42 (Indicador e código da PFJ) 
CFOP
SAFX42
10
Código de CFOP

Pessoa Física/Jurídica
SAFX42
"04" - "05"
"Indicador Pessoa Física/Jurídica" + "Código/Destinatário/Emitente/Remetente"
"Indicador" + Traço "-" + "Código da PFJ"
Valor Contábil
SAFX42
17
Valor Total do Documento Fiscal

ICMS - Base
SAFX42
22
Base de Cálculo

ICMS - Valor
SAFX42
26
Valor ICMS

ICMS - Alíquota
SAFX42
27
Alíquota ICMS

FECEP - ICMS
SAFX43
103
FECEP ICMS
Valor total (Soma) de todos os itens do documento (SAFX42)
FECEP - Alíquota
SAFX43
104
FECEP - ALÍQUOTA ICMS
Alíquota única para todos os itens, neste caso, buscar a alíquota do primeiro item do documento fiscal (SAFX42)

OS3511-A
RN01
 Ao final do relatório deve ser demonstrado um resumo por CFOP/Alíquota  conforme demonstrado abaixo:

Resumo por CFOP do período
Nome do Campo
TABELA
ITEM
Descrição do campo
Regra 
CFOP
SAFX42
10
Código de CFOP
Resumo por CFOP
Valor Contábil
SAFX42
17
Valor Total do Documento Fiscal
Valor Total (Soma) dos valores contábeis do CFOP correspondente.
ICMS - Base
SAFX42
22
Base de Cálculo
Valor Total (Soma) das bases do CFOP correspondente.
ICMS - Valor
SAFX42
26
Valor ICMS
Valor Total (Soma) dos valores de ICMS do CFOP correspondente.
ICMS - Alíquota
SAFX42
27
Alíquota ICMS
Informar a alíquota do CFOP correspondente. Caso existam mais de uma Alíquota para um mesmo CFOP, então totalizar cada alíquota em uma linha diferente. Ou seja, pode haver mai de uma linha para um único CFOP.
FECEP - ICMS
SAFX43
103
FECEP ICMS
Valor total (Soma) de todos os itens do documento (SAFX42) do CFOP correspondente.
FECEP - Alíquota
SAFX43
104
FECEP - ALÍQUOTA ICMS
Informar a alíquota do CFOP correspondente. Caso existam mais de uma Alíquota para um mesmo CFOP, então totalizar cada alíquota em uma linha diferente. Ou seja, pode haver mais de uma linha para um único CFOP.


OS3511-A
RN02
De acordo com os critérios informados na tela de emissão caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a mensagem "SEM MOVIMENTO".
MFS6705


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

