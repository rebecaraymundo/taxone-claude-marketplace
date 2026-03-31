---
source: "MTZ-DW-Manutenção_SAFX331.doc"
category: MasterSAF_DW
converted: auto
---


THOMSON REUTERS

Data WareHouse - Manutenção - SAFX331


Tabela de Informação de Programa de Fidelidade e Fatura da Nota fiscal Eletrônica


 
Localização DW: Menu Básicos, módulo DW, menu Manutenção --> Documento Fiscal --> Doc. Fiscal de Mercadoria 
 
Localização Taxone: Menu Básicos, módulo DW, menu Manutenção --> Novo Documento Fiscal --> Doc. Fiscal de Mercadoria e Serviço 


DOCUMENTO DE REQUISITO

DR
Nome
Descrição
MFS652069
Graciela Soares
Criação da Importação da SAFX331


Sumário
     
      1.	REGRAS GERAIS	2
     2.	LAYOUT DA TELA	2
     3.	REGRAS DE FUNCIONAMENTO DOS CAMPOS	3


1. Regras Gerais:
RN00
SAFX331 - Informação de Programa de Fidelidade e Fatura da Nota fiscal Eletrônica
O objetivo dessa tabela é carregar as informações complementares do programa de fidelidade e fatura da NFCom, que são carregados através da SAFX07. Um item da SAFX07 pode conter apenas um item da SAFX331.
Essas informações fazem parte do layout da NFCom. O Mapeamento completo dos campos da NFCom para as SAFX's (SAFX42, SAFX43, SAFX432,..., SAFX07,SAFX08, SAFX331, SAFX332, SAFX333, SAFX334) está disponível no Share Point (Requisitos - Mastersaf DW TaxOne\Manuais-de-layout\Layout_DEXPARA\ TR_NFCOM_DEXPARA.xlsx).
A manutenção dessa tabela está disponível no Módulo: BÁSICOS > DATAWAREHOUSE > Manutenção > Documento Fiscal > Documento Fiscal de Mercadoria.

Base Legal: Manual de Orientações do Contribuinte da NFCom Visão Geral - versão 1.00a
                   Schema NFCOM 1.00 (https://dfe-portal.svrs.rs.gov.br/NFCOM/ConsultaSchema)

Tabela Definitiva: X331_PROG_FIDEL_FAT_NFE
Estrutura da SAFX331:
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
Saldo de pontos do cliente na data de ref.
QTD_PTS_PROG_FIDEL
020
A


13
Data de aferição do saldo de pontos
DAT_AFER_PROG_FIDEL
008
N


14
Qtd de pontos resgatados na data de ref.
QTD_REGAT_PROG_FIDEL
020
A


15
Data de resgate dos pontos
DAT_REGAT_PROG_FIDEL
008
N


16
Ano e mês referência do faturamento 
ANO_MES_REFERENCIA_FAT
006
N


17
Data de vencimento da fatura
DAT_VENCTO
008
N


18
Linha digitável do código de barras
COD_BARRAS
048
A


19
Código de autorização débito em conta
COD_DEBITO_AUTO
020
A


20
Número do banco para débito em conta
COD_BANCO_AUTO
005
A


21
Número da agência bancária para débito em conta
COD_AGENCIA_AUTO
010
A


22
URL do QRCode do PIX que será apresentado na fatura
COD_QRCODE_PIX
2000
A


23
Período de uso inicial
DATA_CONSUMO_INI
008
N


24
Período de uso final
DATA_CONSUMO_FIM
008
N

MFS652069


2. Layout da Tela:

Uma janela de formulário simples, com campos e botões implementados da forma padrão, conforme especificações filha da SAFX07


Título da tela: Informações do Programa de Fidelidade e da Fatura da Nota fiscal Eletrônica

Regra Geral Botões:

NOVO - Permite inserir novo registro.

EXCLUI - Permite excluir registro inserido.

CONFIRMA - Permite salvar registro.

FECHA - Permite sair da tela.

Regra Geral: 

- Pode existir nenhum ou apenas item das Informação de Programa de Fidelidade e Fatura da Nota fiscal Eletrônica (SAFX331) por capa de Documento Fiscal (SAFX07).


3. Regras de Funcionamento dos Campos
Cód.
Descrição
DR
RN01
Campo Saldo de pontos do cliente na data de referência
      
Obrigatoriedade: Não obrigatório
Descrição: Saldo de Pontos do Cliente
Nome do Campo: QTD_PTS_PROG_FIDEL
Tamanho: 020
Tipo: A
Edita: Sim


RN02
Campo Data de aferição do saldo de pontos
      
Obrigatoriedade: Não obrigatório
Descrição: Data Aferição do Saldo de Pontos
Nome do Campo: DAT_AFER_PROG_FIDEL
Tamanho: 008
Tipo: N (Campo Data)
Edita: Sim


RN03
Campo Qtd de pontos resgatados na data de referência
      
Obrigatoriedade: Não obrigatório
Descrição: Quantidade de Pontos resgatados
Nome do Campo: QTD_REGAT_PROG_FIDEL
Tamanho: 020
Tipo: A
Edita: Sim


RN04
Campo Data de resgate dos pontos
      
Obrigatoriedade: Não obrigatório
Descrição: Data Resgate dos Pontos
Nome do Campo: DAT_REGAT_PROG_FIDEL
Tamanho: 008
Tipo: N (Campo Data)
Edita: Sim


RN05
Campo Ano e mês referência do faturamento (AAAAMM)
      
Obrigatoriedade: Não obrigatório
Descrição: Período do Faturamento (AAAAMM)
Nome do Campo: ANO_MES_REFERENCIA_FAT
Tamanho: 006
Tipo: N
Edita: Sim


RN06
Campo Data de vencimento da fatura
      
Obrigatoriedade: Não obrigatório
Descrição: Vencimento da Fatura
Nome do Campo: DAT_VENCTO
Tamanho: 008
Tipo: N (Campo Data)
Edita: Sim


RN07
Campo Linha digitável do código de barras
      
Obrigatoriedade: Não obrigatório
Descrição: Código de Barras
Nome do Campo: COD_BARRAS
Tamanho: 048
Tipo: A
Edita: Sim


RN08
Campo Código de autorização débito em conta
      
Obrigatoriedade: Não obrigatório
Descrição: Cod. Autorização Débito em Conta:
Nome do Campo: COD_DEBITO_AUTO
Tamanho: 020
Tipo: A
Edita: Sim


RN09
Campo Número do banco para débito em conta
      
Obrigatoriedade: Não obrigatório
Descrição: Banco Débito em Conta:
Nome do Campo: COD_BANCO_AUTO
Tamanho: 005
Tipo: A
Edita: Sim


RN10
Campo Número da agência bancária para débito em conta
      
Obrigatoriedade: Não obrigatório
Descrição: Agência Débito em Conta:
Nome do Campo: COD_AGENCIA_AUTO
Tamanho: 010
Tipo: A
Edita: Sim


RN11
Campo URL do QRCode do PIX que será apresentado na fatura
      
Obrigatoriedade: Não obrigatório
Descrição: URL QRCode do PIX
Nome do Campo: COD_QRCODE_PIX
Tamanho: 2000
Tipo: A
Edita: Sim


RN12
Campo Período de uso inicial
      
Obrigatoriedade: Não obrigatório
Descrição: Data Inicial Consumo
Nome do Campo: DATA_CONSUMO_INI
Tamanho: 008
Tipo: N (Campo Data)
Edita: Sim


RN13
Campo Período de uso final
      
Obrigatoriedade: Não obrigatório
Descrição: Data Final Consumo
Nome do Campo: DATA_CONSUMO_FIM
Tamanho: 008
Tipo: N (Campo Data)
Edita: Sim


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

     

