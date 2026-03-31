# MTZ-DW-Manutenção_SAFX334

> Fonte: MTZ-DW-Manutenção_SAFX334.doc



THOMSON REUTERS

Data WareHouse - Manutenção - SAFX334


Tabela de Infomações de Fundos de Desenvolvimento e Retenções de Tributos Federais  em Nota Fiscal Eletrônica



Localização DW: Menu Básicos, módulo DW, menu Manutenção --> Documento Fiscal --> Doc. Fiscal de Mercadoria

Localização Taxone: Menu Básicos, módulo DW, menu Manutenção --> Novo Documento Fiscal --> Doc. Fiscal de Mercadoria e Serviço




DOCUMENTO DE REQUISITO

DR
Nome
Descrição
MFS652078
Graciela Soares
Criação da Importação da SAFX334















Sumário

      1.	REGRAS GERAIS	2
     2.	LAYOUT DA TELA	2
     3.	REGRAS DE FUNCIONAMENTO DOS CAMPOS	3
























1. Regras Gerais:
RN00
SAFX334 - Infomações de Fundos de Desenvolvimento e Retenções de Tributos Federais em Nota Fiscal Eletrônica
O objetivo dessa tabela é carregar as Infomações de Fundos de Desenvolvimento e Retenções de Tributos Federais em Nota Fiscal Eletrônica NFCom, que são carregados através da SAFX08. Um item da SAFX08 pode conter nhenhum ou apenas um item da SAFX334.
Essas informações fazem parte do layout da NFCom. O Mapeamento completo dos campos da NFCom para as SAFX's (SAFX42, SAFX43, SAFX432,..., SAFX07,SAFX08, SAFX331, SAFX332, SAFX333, SAFX334) está disponível no Share Point (Requisitos - Mastersaf DW TaxOne\Manuais-de-layout\Layout_DEXPARA\ TR_NFCOM_DEXPARA.xlsx).
A manutenção dessa tabela está disponível no Módulo: BÁSICOS > DATAWAREHOUSE > Manutenção > Documento Fiscal > Documento Fiscal de Mercadoria.    Base Legal: Manual de Orientações do Contribuinte da NFCom Visão Geral - versão 1.00a
                   Schema NFCOM 1.00 (https://dfe-portal.svrs.rs.gov.br/NFCOM/ConsultaSchema)

Tabela Definitiva: X334_FUND_TRIB_FED_NFE

Estrutura da SAFX334:
PK
OBRIG
ITEM
DESCRIÇÃO
CAMPO
TAM
TIPO
X
(*)
01
Código da Empresa
COD_EMPRESA
003
A
X
(*)
02
Código do Estabelecimento
COD_ESTAB
006
A
X
(*)
03
Data da Escrita Fiscal
DAT_FISCAL
008
N
X
(*)
04
Movimento Entrada/Saída
MOVTO_E_S
001
A
X
(*)
05
Normal ou Devolução
NORM_DEV
001
A
X
(*)
06
Tipo do Documento
COD_DOCTO
005
A
X
(*)
07
Indicador da Pessoa Física/Jurídica
IND_FIS_JUR
001
A
X
(*)
08
Código do Destinatário/Emitente
COD_FIS_JUR
014
A
X
(*)
09
Número do Documento Fiscal
NUM_DOCFIS
012
A
X

10
Série do Documento Fiscal
SERIE_DOCFIS
003
A
X

11
Subsérie do Documento Fiscal
SUB_SERIE_DOCFIS
002
A


12
Indicador do Produto
IND_PRODUTO
001
A


13
Produto
COD_PRODUTO
006
A


14
Unidade Padrão
COD_UND_PADRAO
008
A


15
Item Nota Fiscal
NUM_ITEM
005
N


16
Valor do PIS retido
VLR_PIS_RETIDO
015V008
N


17
Valor do COFNS retido
VLR_COFINS_RETIDO
015V008
N


18
Valor da CSLL retida
VLR_CSLL_RETIDO
015V008
N


19
Base de cálculo do IRRF
VLR_BC_IRRF
015V008
N


20
Valor do IRRF retido
VLR_IRRF_RETIDO
015V008
N


21
Valor da BC do FUST
VLR_BC_FUST
015V002
N


22
Alíquota do FUST (em percentual)
VLR_ALIQ_FUST
003V002
N


23
Valor do FUST
VLR_FUST
015V002
N


24
Valor da BC do FUNTTEL
VLR_BC_FUNTTEL
015V002
N


25
Alíquota do FUNTTEL (em percentual)
VLR_ALIQ_FUNTTEL
003V002
N


26
Valor do FUNTEL
VLR_FUNTTEL
015V002
N

MFS652075
2. Layout da Tela:

Uma janela de formulário simples, com campos e botões implementados da forma padrão, conforme especificações, filha da SAFX08




Título da tela: ICMS de Partilha UF Destinatária NFe

Regra Geral Botões:

EXCLUI - Permite excluir registro inserido.

CONFIRMA - Permite salvar registro.

FECHA - Permite sair da tela.


Regra Geral:

- Pode existir nenhum ou apenas um item das Infomações de Fundos de Desenvolvimento e Retenções de Tributos Federais em Nota Fiscal Eletrônica (SAFX334) por Item do Documento Fiscal (SAFX08).


3. Regras de Funcionamento dos Campos
Cód.
Descrição
DR
RN01
Campo Valor do PIS retido

Obrigatoriedade: Não obrigatório
Descrição: Vlr. PIS retido
Nome do Campo: VLR_PIS_RETIDO
Tamanho: 015V008
Tipo: N
Edita: Sim


MFS652078
RN02
Campo Valor do COFNS retido

Obrigatoriedade: Não obrigatório
Descrição: Vlr. COFNS retido
Nome do Campo: VLR_COFINS_RETIDO
Tamanho: 015V008
Tipo: N
Edita: Sim


MFS652078

RN03
Campo Valor da CSLL retida

Obrigatoriedade: Não obrigatório
Descrição: Vlr. CSLL retida
Nome do Campo: VLR_CSLL_RETIDO
Tamanho: 015V008
Tipo: N
Edita: Sim


MFS652078
RN04
Campo Base de cálculo do IRRF

Obrigatoriedade: Não obrigatório
Descrição: Vlr. BC IRRF
Nome do Campo: VLR_BC_IRRF
Tamanho: 015V008
Tipo: N
Edita: Sim


MFS652078
RN05
Campo Valor do IRRF retido

Obrigatoriedade: Não obrigatório
Descrição: Vlr. IRRF retido
Nome do Campo: VLR_IRRF_RETIDO
Tamanho: 015V008
Tipo: N
Edita: Sim


MFS652078
RN06
Campo Valor da BC do FUST

Obrigatoriedade: Não obrigatório
Descrição: Vlr. BC FUST
Nome do Campo: VLR_BC_FUST
Tamanho: 015V002
Tipo: N
Edita: Sim


MFS652078
RN07
Campo Alíquota do FUST (em percentual)

Obrigatoriedade: Não obrigatório
Descrição: Vlr. Alíq. FUST
Nome do Campo: VLR_ALIQ_FUST
Tamanho: 003V004
Tipo: N
Edita: Sim


MFS652078
RN08
Campo Valor do FUST

Obrigatoriedade: Não obrigatório
Descrição: Vlr. FUST
Nome do Campo: VLR_FUST
Tamanho: 015V002
Tipo: N
Edita: Sim


MFS652078
RN09
Campo Valor da BC do FUNTTEL

Obrigatoriedade: Não obrigatório
Descrição: Vlr. BC FUNTTEL
Nome do Campo: VLR_BC_FUNTTEL
Tamanho: 015V002
Tipo: N
Edita: Sim


MFS652078
RN10
Campo Alíquota do FUNTTEL (em percentual)

Obrigatoriedade: Não obrigatório
Descrição: Vlr. Alíq. FUNTTEL
Nome do Campo: VLR_ALIQ_FUNTTEL
Tamanho: 003V004
Tipo: N
Edita: Sim


MFS652078
RN11
Campo Valor do FUNTEL

Obrigatoriedade: Não obrigatório
Descrição: Vlr. FUNTTEL
Nome do Campo: VLR_FUNTTEL
Tamanho: 015V002
Tipo: N
Edita: Sim

MFS652078




Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN



