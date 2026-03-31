---
source: "MTZ-DW-Manutenção_SAFX333.doc"
category: MasterSAF_DW
converted: auto
---


THOMSON REUTERS

Data WareHouse - Manutenção - SAFX333


Tabela de Informações do ICMS de Partilha com UF Destinatária em Nota Fiscal Eletrônica


 
Localização DW: Menu Básicos, módulo DW, menu Manutenção --> Documento Fiscal --> Doc. Fiscal de Mercadoria 
 
Localização Taxone: Menu Básicos, módulo DW, menu Manutenção --> Novo Documento Fiscal --> Doc. Fiscal de Mercadoria e Serviço 


DOCUMENTO DE REQUISITO

DR
Nome
Descrição
MFS652075
Graciela Soares
Criação da Importação da SAFX333


Sumário
     
      1.	REGRAS GERAIS	2
     2.	LAYOUT DA TELA	2
     3.	REGRAS DE FUNCIONAMENTO DOS CAMPOS	3


1. Regras Gerais:
RN00
SAFX333 - Informações de Partilha com UF Destinatária em Nota Fiscal Eletrônica
O objetivo dessa tabela é carregar as Informações de Partilha com UF Destinatária em Nota Fiscal Eletrônica NFCom, que são carregados através da SAFX08. Um item da SAFX08 pode conter nhenhum ou diversos itens da SAFX333.
Essas informações fazem parte do layout da NFCom. O Mapeamento completo dos campos da NFCom para as SAFX's (SAFX42, SAFX43, SAFX432,..., SAFX07,SAFX08, SAFX331, SAFX332, SAFX333, SAFX334) está disponível no Share Point (Requisitos - Mastersaf DW TaxOne\Manuais-de-layout\Layout_DEXPARA\ TR_NFCOM_DEXPARA.xlsx).
A manutenção dessa tabela está disponível no Módulo: BÁSICOS > DATAWAREHOUSE > Manutenção > Documento Fiscal > Documento Fiscal de Mercadoria.
Base Legal: Manual de Orientações do Contribuinte da NFCom Visão Geral - versão 1.00a
                   Schema NFCOM 1.00 (https://dfe-portal.svrs.rs.gov.br/NFCOM/ConsultaSchema)

Tabela Definitiva: X333_PART_UF_DEST_NFE
Estrutura da SAFX333:
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
X

16
UF destinatária de Partilha
UF_DESTINO
002
A


17
Valor da BC do ICMS na UF de destino
VLR_BASE_ICMS_DEST
015V002
N


18
Percentual do ICMS relativo ao Fundo de Combate à pobreza (FCP) na UF de destino
PERC_FCP_DEST
003V002
N


19
Alíquota interna da UF de destino
VLR_ALIQ_DESTINO
003V004
N


20
Valor do ICMS relativo ao Fundo de Combate á Pobreza (FCP) da UF de destino
VLR_FCP_UF_DEST
015V002
N


21
Valor do ICMS de partilha para a UF destino
VLR_TRIB_ICMS_DEST
015V002
N


22
Valor do ICMS de partilha para a UF emissão
VLR_ICMS_UF_EMIT
015V002
N


23
Código de Benefício Fiscal na UF destino aplicado ao item
COD_BENEF_FISCAL_DEST
010
A

MFS652075


2. Layout da Tela:

Uma janela de formulário simples, com campos e botões implementados da forma padrão, conforme especificações, filha da SAFX08.


Título da tela: ICMS de Partilha UF Destinatária NFe

Regra Geral Botões:

NOVO - Permite inserir novo registro.

EXCLUI - Permite excluir registro inserido.

CONFIRMA - Permite salvar registro.

FECHA - Permite sair da tela.

Regra Geral: 

- Pode existir nenhum ou diversos itens das Informações de Partilha com UF Destinatária em Nota Fiscal Eletrônica (SAFX333) por Item do Documento Fiscal (SAFX08).


3. Regras de Funcionamento dos Campos
Cód.
Descrição
DR
RN01
Campo UF destinatária de Partilha
      
Obrigatoriedade: Obrigatório
Descrição: UF Dest. Partilha
Nome do Campo: UF_DESTINO
Tamanho: 002
Tipo: A
Edita: Sim

MFS652075
RN02
Campo Valor da BC do ICMS na UF de destino

Obrigatoriedade: Não obrigatório
Descrição: Vlr. BC ICMS UF destino
Nome do Campo: VLR_BASE_ICMS_DEST
Tamanho: 015V002
Tipo: N
Edita: Sim


MFS652075

RN03
Campo Percentual do ICMS relativo ao Fundo de Combate à pobreza (FCP) na UF de destino
      
Obrigatoriedade: Não obrigatório
Descrição: Perc. ICMS FCP
Nome do Campo: PERC_FCP_DEST
Tamanho: 003V002
Tipo: N
Edita: Sim

MFS652075
RN04
Campo Alíquota interna da UF de destino
      
Obrigatoriedade: Não obrigatório
Descrição: Aliq. Interna UF Dest.
Nome do Campo: VLR_ALIQ_DESTINO
Tamanho: 003V004
Tipo: N
Edita: Sim


MFS652075
RN05
Campo Valor do ICMS relativo ao Fundo de Combate á Pobreza (FCP) da UF de destino
      
Obrigatoriedade: Não obrigatório
Descrição: Vlr. ICMS FCP
Nome do Campo: VLR_FCP_UF_DEST
Tamanho: 015V002
Tipo: N
Edita: Sim


MFS652075
RN06
Campo Valor do ICMS de partilha para a UF de destino
      
Obrigatoriedade: Não obrigatório
Descrição: Vlr. ICMS Partilha Destino
Nome do Campo: VLR_TRIB_ICMS_DEST
Tamanho: 015V002
Tipo: N
Edita: Sim


MFS652075
RN07
Campo Valor do ICMS de partilha para a UF de emissão
      
Obrigatoriedade: Não obrigatório
Descrição: Vlr. ICMS Partilha Emissão
Nome do Campo: VLR_ICMS_UF_EMIT
Tamanho: 015V002
Tipo: N
Edita: Sim


MFS652075
RN08
Código de Benefício Fiscal na UF destino aplicado ao item

Obrigatoriedade: Não obrigatório
Descrição: Cód. Benefício Fiscal Destino
Nome do Campo: COD_BENEF_FISCAL_DEST
Tamanho: 010
Tipo: A
Edita: Sim


MFS652075


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

     

