# MTZ_Manutenção_Anexo_VI-M_Quadros 4 a 15

> Fonte: MTZ_Manutenção_Anexo_VI-M_Quadros 4 a 15.docx






THOMSON REUTERS

Manutenção Anexo VI-M Quadros 4 a 15
Módulo Combustível e Derivados de Petróleo (SCANC)

Localização: Movimento de Refinaria à Manutenção Anexo VI-M à Quadros 4 a 15


DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3

## Regras dos Campos


Localização da tela: Específicos >> Combustível e Derivados de Petróleo
Movimento de Refinaria à Manutenção Anexo VI-M à Quadros 4 a 15

Tabela de Destino: CBT_ANEXO6M_QUADR4A15

Definição dos campos a serem apresentados na tela:

Estabelecimento:
Habilitado se o usuário entrou sem estabelecimento de login.
Desabilitado se o estabelecimento foi informado no login do módulo.
Campo Obrigatório
Gravar campo COD_ESTAB CBT_ANEXO6M_QUADR4A15

Mês/Ano Referência:
Habilitado
Campo obrigatório.
Gravar DAT_APURACAO CBT_ANEXO6M_QUADR4A15, com o último dia do mês/ano informado.

UF Destinatária do Anexo VI-M:
Habilitado
Campo Obrigatório
Gravar IDENT_ESTADO_DESTINO CBT_ANEXO6M_QUADR4A15

Tipo:
Radium Botton com duas opções:
( ) Repasse
( ) Dedução
Default: Repasse
Campo Obrigatório. Não é gravado na tabela CBT_ANEXO6M_QUADR4A15, serve apenas como filtro para a lista a ser apresentada no campo seguinte.

Quadro:
Habilitado
Campo Obrigatório
Lista fixa composta pelos itens abaixo, que são apresentados de acordo com a seleção no campo anterior (Repasse ou Dedução):
4.1.1 - REPASSE POR OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS DE COMBUSTÍVEIS/TRRs (ICMS COBRADO PELO EMITENTE)
4.1.2.1 - REPASSE POR OPERAÇÕES REALIZADAS POR DISTRIBUIDORES DE GÁS EM FAVOR DA UF DE ORIGEM DO GLGN
4.1.2.2 - REPASSE POR OPERAÇÕES REALIZADAS POR DISTRIBUIDORES DE GÁS EM FAVOR DA UF DE DESTINO DO GLP/GLGN
4.2 - REPASSE POR OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS DE COMBUSTÍVEIS/TRRs (ICMS COBRADO POR OUTROS CONTRIBUINTES)
4.3 – REPASSES EXTEPORÂNEOS
5 - REPASSE POR OPERAÇÕES REALIZADAS POR IMPORTADORES
6.1 – REPASSE DE ICMS SOBRE BIOCOMBUSTÍVEL DECORRENTE DE AJUSTES DE REPARTIÇÃO DE RECEITA
6.2 – REPASSES EXTEMPORÂNEOS DE ICMS SOBRE BIOCOMBUSTÍVEL
7.1.1 - DEDUÇÃO POR OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS DE COMBUSTÍVEIS/TRRs (ICMS COBRADO PELO EMITENTE)
7.1.2.1 - DEDUÇÃO POR OPERAÇÕES REALIZADAS POR DISTRIBUIDORES DE GÁS EM FAVOR DA UF DE ORIGEM DO GLGN
7.1.2.2 - DEDUÇÃO POR OPERAÇÕES REALIZADAS POR DISTRIBUIDORES DE GÁS EM FAVOR DA UF DE DESTINO DO GLP/GLGN
7.2 - DEDUÇÃO POR OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS DE COMBUSTÍVEIS/TRRs (ICMS COBRADO POR OUTROS CONTRIBUINTES)
7.3 – DEDUÇÕES EXTEPORÂNEAS
8 - DEDUÇÃO POR OPERAÇÕES REALIZADAS POR IMPORTADORES
9.1 – DEDUÇÃO DE ICMS SOBRE BIOCOMBUSTÍVEL DECORRENTE DE AJUSTES DE REPARTIÇÃO DE RECEITA
9.2 – DEDUÇÃO EXTEMPORÂNEAS DE ICMS SOBRE BIOCOMBUSTÍVEL
10 - DEDUÇÃO POR RESSARCIMENTO EFETUADO A DISTRIBUIDORAS
11 - DEDUÇÃO POR RESSARCIMENTO EFETUADO A TRR
12 - DEDUÇÃO POR RESSARCIMENTO EFETUADO A IMPORTADORES
13 - DEDUÇÃO POR RESSARCIMENTO EFETUADO A OUTROS CONTRIBUINTES
14 - DEDUÇÃO TRANSFERIDA DE OUTRO ESTABELECIMENTO DO SUJEITO PASSIVO POR SUBSTITUIÇÃO
15 - DEDUÇÃO TRANSFERIDA PARA OUTRO ESTABELECIMENTO DO SUJEITO PASSIVO POR SUBSTITUIÇÃO

Gravar os campos COD_TAG e COD_QUADRO CBT_ANEXO6M_QUADR4A15 conforme regra abaixo:


Pessoa Fís/Jur:
Habilitado
Campo Obrigatório
Gravar IDENT_FIS_JUR CBT_ANEXO6M_QUADR4A15
Esse campo varia de acordo com o item selecionado no campo Quadro:


UF do Quadro:
Campo obrigatório exceto para os quadros 10, 11, 12, 13.
Gravar IDENT_ESTADO_QUAD CBT_ANEXO6M_QUADR4A15

Mês/Ano Referência do Quadro:
Habilitado
Campo Obrigatório
Default: preencher com o mesmo conteúdo digitado no campo Mês/Ano Referência. Mas a data pode ser alterada via digitação.
Gravar DAT_REF CBT_ANEXO6M_QUADR4A15 com o último dia do mês/ano informado.

Vlr ICMS
Habilitado
Gravar VLR_ICMS CBT_ANEXO6M_QUADR4A15

Comunicado:
Habilitado
Gravar COMUNIC_REF CBT_ANEXO6M_QUADR4A15

No Processo
Desabilitado
Gravar NUM_PROCESSO CBT_ANEXO6M_QUADR4A15

Ind Dig Calc:
Não apresentar na tela.
Gravar:
1 – inserido via tela de manutenção
2 – inserido via geração do Anexo VI-M
3 - inserido via geração do Anexo VI-M e atualizado pela tela de manutenção

Usuário
Não apresentar na tela.
Gravar o usuário de login da aplicação.







| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS535202 |  |  |


| Item | COD_TAG | COD_QUADRO |
| --- | --- | --- |
| 4.1.1 | A6MQ41 | 1 |
| 4.1.2.1 | A6MQ41 | 21 |
| 4.1.2.2 | A6MQ41 | 22 |
| 4.2 | A6MQ42 |  |
| 4.3 | A6MQ43 |  |
| 5 | A6MQ5 |  |
| 6.1 | A6MQ61 |  |
| 6.2 | A6MQ62 |  |
| 7.1.1 | A6MQ71 | 1 |
| 7.1.2.1 | A6MQ71 | 21 |
| 7.1.2.2 | A6MQ71 | 22 |
| 7.2 | A6MQ72 |  |
| 7.3 | A6MQ73 |  |
| 8 | A6MQ8 |  |
| 9.1 | A6MQ91 |  |
| 9.2 | A6MQ92 |  |
| 10 | A6MQ10 |  |
| 11 | A6MQ11 |  |
| 12 | A6MQ12 |  |
| 13 | A6MQ13 |  |
| 14 | A6MQ14 |  |
| 15 | A6MQ15 |  |


| Item - Quadro | Título Pessoa Fís/Jur | Título UF do Quadro | Regra do Campo UF do Quadro |
| --- | --- | --- | --- |
| 4.1.1 | Distribuidora Combustíveis/TRR | UF Distribuidora/TRR | Habilitado e trazer como default a UF da Pessoa Fis/Jur (Cadastro da X04) |
| 4.1.2.1 | Distribuidora de Gás | UF Distribuidora de Gás | Habilitado e trazer como default a UF da Pessoa Fis/Jur (Cadastro da X04) |
| 4.1.2.2 | Distribuidora de Gás | UF Distribuidora de Gás | Habilitado e trazer como default a UF da Pessoa Fis/Jur (Cadastro da X04) |
| 4.2 | Distribuidora Combustíveis/TRR | UF Distribuidora/TRR | Habilitado e trazer como default a UF da Pessoa Fis/Jur (Cadastro da X04) |
| 4.3 | Distribuidora Gás/Combustíveis/ TRR | UF a Deduzir | Habilitado |
| 5 | Importadores | UF Importadores | Habilitado e trazer como default a UF da Pessoa Fis/Jur (Cadastro da X04) |
| 6.1 | Distribuidora/TRR Biocombustível | UF a Deduzir | Habilitado |
| 6.2 | Distribuidora/TRR Biocombustível | UF a Deduzir | Habilitado |
| 7.1.1 | Distribuidora/TRR | UF a Repassar | Habilitado |
| 7.1.2.1 | Distribuidora de Gás - GLGN | UF a Repassar | Habilitado |
| 7.1.2.2 | Distribuidora de Gás - GLP/GLGN | UF a Repassar | Habilitado |
| 7.2 | Distribuidora Combustíveis/TRR | UF a Provisionar | Habilitado |
| 7.3 | Distribuidora Gás/Combustíveis/ TRR | UF a Repassar | Habilitado |
| 8 | Importadores | UF a Provisionar | Habilitado |
| 9.1 | Distribuidora de Combustíveis/TRR | UF a Repassar |  |
| 9.2 | Distribuidora de Combustíveis/TRR | UF a Repassar | Habilitado |
| 10 | Distribuidora | Inibir o campo UF | Desabilitar e não gravar IDENT_ESTADO_QUAD CBT_ANEXO6M_QUADR4A15 |
| 11 | TRR | Inibir o campo UF | Desabilitar e não gravar IDENT_ESTADO_QUAD CBT_ANEXO6M_QUADR4A15 |
| 12 | Importador | Inibir o campo UF | Desabilitar e não gravar IDENT_ESTADO_QUAD CBT_ANEXO6M_QUADR4A15 |
| 13 | Outros Contribuintes | Inibir o campo UF | Desabilitar e não gravar IDENT_ESTADO_QUAD CBT_ANEXO6M_QUADR4A15 |
| 14 | Estabelecimento da Empresa | UF do Estabelecimento de Transferência | Habilitado e trazer como default a UF da Pessoa Fis/Jur (Cadastro da X04) |
| 15 | Estabelecimento da Empresa | UF do Estabelecimento Transferido | Habilitado e trazer como default a UF da Pessoa Fis/Jur (Cadastro da X04) |


| Tela | PL usado pela tela |
| --- | --- |
| Manutenção Anexo VI-M |  |
| Quadro 1 e 2 |  |
| Quadro 3 | Saf_atualiza_anexo_6M_q1_2 da Pkg_Cbt_Anexo_6 |
| Quadros 4 a 15 | Saf_atualiza_anexo_6M_q1_2 da Pkg_Cbt_Anexo_6 |
