# MTZ_Manutenção_Anexo_VI-M_Quadro 1 e 2

> Fonte: MTZ_Manutenção_Anexo_VI-M_Quadro 1 e 2.docx






THOMSON REUTERS

Manutenção Anexo VI-M Quadros 1 e 2
Módulo Combustível e Derivados de Petróleo (SCANC)

Localização: Movimento de Refinaria  Manutenção Anexo VI-M  Quadro 1 e 2


DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3

## Regras dos Campos


Localização da tela: Específicos >> Combustível e Derivados de Petróleo
Movimento de Refinaria  Manutenção Anexo VI-M  Quadro 1 e 2

Quadro 1:
O Quadro 1 é uma totalização de quadros 3 ao 15. A tela permite inclusão de registro e alteração dos valores. As telas dos quadros 3 ao 15 atualizam automaticamente os valores do quadro 1, conforme regras abaixo.

Tabela: CBT_ANEXO6M_QUADR1



Quadro 2:

O Quadro 2 é uma totalização de quadros 4.2 e 5. A tela permite inclusão de registro e alteração dos valores. As telas dos quadros 4.2 e 5 atualizam automaticamente os valores do quadro 2, conforme regras abaixo.

Gravar os campos do Quadro 2 conforme regras abaixo.

Tabela: CBT_ANEXO6M_QUADR2




| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS535202 |  |  |
| MFS783073 | Liliane Assaf | Alteração do label dos campos referentes aos valores 1.1.5, 1.1.6, 1.2.4, 1.2.5 para inclusão do GLGNn. |
| MFS917434 | Liliane Assaf | Inclusão da linha 1.1.1.2: Somatório dos registros do quadro 3.1. Inclusão da linha 1.2.0.1: Somatório dos registros do quadro 3.2. Atualização da linha 1.1.7: adicionar o valor da linha 1.1.1.2 no somatório das linhas 1.1.1, 1.1.2, 1.1.3, 1.1.4, 1.1.5, 1.1.6. Atualização da linha 1.2.8: adicionar o valor da linha 1.2.0.1 no somatório das linhas 1.2.1, 1.2.2, 1.2.3, 1.2.4, 1.2.5, 1.2.6, 1.2.7. |


| Nome do Campo | Nome físico do campo | Regra de Preenchimento |
| --- | --- | --- |
| Empresa | Cod_Empresa | Empresa de login |
| Estabelecimento: | Cod_Estab | Estabelecimento selecionado na Geração |
| Mês/Ano Referência: | Dat_apuracao | Último dia do mês/ano informado na tela de geração |
| UF Destinatária do Anexo VI-M | Ident_estado_destino | UF Destinatária do Anexo VI-M recuperada dos quadros selecionados nos campos abaixo. |
| Vlr 1.1.1  ICMS SOBRE OPERAÇÕES POR TRIBUTAÇÃO MONOFÁSICA PRÓPRIAS E RETIDAS (QUADRO 3) | vlr_icms_st_111 | Consultar o Quadro 3 com os critérios: empresa, estabelecimento e mês/ano referência informados para geração. Recuperar Vlr ICMS Total (ICMS Cobrado + Retido) totalizado por UF Destinatária do Anexo VI-M. Gravar esse campo com o Vlr ICMS Total (ICMS Cobrado + Retido). |
| [MFS917434] Vlr 1.1.1.2  ICMS SOBRE OPERAÇÕES COM GLGN DEVIDO A UF DE ORIGEM (QUADRO 3.1) | vlr_icms_st_1112 | Consultar o Quadro 3.1 com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = A6MQ31. Recuperar Vlr ICMS Total (ICMS Cobrado + Retido) totalizado por UF Destinatária do Anexo VI-M. Gravar esse campo com o Vlr ICMS Total (ICMS Cobrado + Retido). |
| Vlr 1.1.2 REPASSE DE ICMS SOBRE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRRs (QUADRO 4.1.1) | vlr_icms_st_112 | Consultar o Quadro 4.1.1 com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = A6MQ41 e COD_QUADRO = 1. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 1.1.3 REPASSE DE ICMS SOBRE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS DE GÁS (QUADRO 4.1.2.) | vlr_icms_st_113 | Consultar os Quadros 4.1.2.1 e 4.1.2.2 com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = A6MQ41 e COD_QUADRO = 21 e 22. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 1.1.4 REPASSE DE ICMS DECORRENTE DE RELATÓRIOS EXTEMPORÂNEOS (QUADRO 4.3) | vlr_icms_st_114 | Consultar o Quadro 4.3 com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = A6MQ43. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 1.1.5 REPASSE DE ICMS SOBRE BIOCOMBUSTÍVEIS OU GLGNn DECORRENTE DE AJUSTES DE REPARTIÇÃO DE RECEITA (QUADRO 6.1) MFS783073 | vlr_icms_st_115 | Consultar o Quadro 6.1 com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = A6MQ61. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 1.1.6 REPASSE DE ICMS SOBRE BIOCOMBUSTÍVEIS OU GLGNn DECORRENTE DE RELATÓRIOS EXTEMPORÂNEOS (QUADRO 6.2) MFS783073 | vlr_icms_st_116 | Consultar o Quadro 6.2 com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = A6MQ62. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI-M. Gravar esse campo com o Vlr ICMS. |
| [MFS917434] Vlr 1.1.7 SUB-TOTAL (1.1.1+1.1.1.2 + 1.1.2 + 1.1.3 + 1.1.4 + 1.1.5 + 1.1.6) | vlr_icms_st_117 | Somatório dos campos Vlr 1.1.1, Vlr 1.1.1.2, Vlr 1.1.2, Vlr 1.1.3, Vlr 1.1.4, Vlr 1.1.5 e Vlr 1.1.6. |
| [MFS917434] Vlr 1.2.0.1  DEDUÇÃO DE ICMS SOBRE OPERAÇÕES COM GLGN DEVIDO A UF DE ORIGEM (QUADRO 3.2) | vlr_icms_st_1201 | Consultar o Quadro 3.2 com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = A6MQ32. Recuperar Vlr ICMS Total (ICMS Cobrado + Retido) totalizado por UF Destinatária do Anexo VI-M. Gravar esse campo com o Vlr ICMS Total (ICMS Cobrado + Retido). |
| Vlr 1.2.1 DEDUÇÃO DE ICMS SOBRE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRRs A SER REPASSADO A OUTRAS UFs (QUADRO 7.1.1) | vlr_icms_st_121 | Consultar o Quadro 7.1.1 com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = A6MQ71 e COD_QUADRO = 1. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 1.2.2 DEDUÇÃO DE ICMS SOBRE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS DE GÁS (QUADRO 7.1.2) | vlr_icms_st_122 | Consultar os Quadros 7.1.2.1 e 7.1.2.2 com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = A6MQ71 e COD_QUADRO = 21 e 22. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 1.2.3 DEDUÇÃO DE ICMS DECORRENTE DE RELATÓRIOS EXTEMPORÂNEOS (QUADRO 7.3) | vlr_icms_st_123 | Consultar o Quadro 7.3 com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = A6MQ73. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 1.2.4 DEDUÇÃO DE ICMS SOBRE BIOCOMBUSTÍVEIS OU GLGNn DECORRENTE DE AJUSTES DE REPARTIÇÃO DE RECEITA (QUADRO 9.1) MFS783073 | vlr_icms_st_124 | Consultar o Quadro 9.1 com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = A6MQ91. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 1.2.5 DEDUÇÃO DE ICMS SOBRE BIOCOMBUSTÍVEIS OU GLGNn DECORRENTE DE RELATÓRIOS EXTEMPORÂNEOS (QUADRO 9.2) MFS783073 | vlr_icms_st_125 | Consultar o Quadro 9.2 com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = A6MQ92. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 1.2.6 PROVISÃO PARA REPASSE POR OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRRs (QUADRO 7.2) | vlr_icms_st_126 | Consultar o Quadro 7.2 com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = A6MQ72. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 1.2.7 PROVISÃO PARA REPASSE POR OPERAÇÕES REALIZADAS POR IMPORTADORES (QUADRO 8) | vlr_icms_st_127 | Consultar o Quadro 8 com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = A6MQ8. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI-M. Gravar esse campo com o Vlr ICMS. |
| [MFS917434] Vlr 1.2.8 SUB-TOTAL DAS DEDUÇÕES (1.2.0.1+1.2.1 + 1.2.2 + 1.2.3 + 1.2.4 + 1.2.5 + 1.2.6 + 1.2.7) | vlr_icms_st_128 | Somatório dos campos Vlr1.2.0.1, Vlr 1.2.1, Vlr 1.2.2, Vlr 1.2.3, Vlr 1.2.4, Vlr 1.2.5, Vlr 1.2.6 e Vlr 1.2.7. |
| Vlr 1.2.9 ICMS RESSARCIDO A DISTRIBUIDORAS (QUADRO 10) | vlr_icms_st_129 | Consultar o Quadro 10 com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = A6MQ10. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 1.2.10 ICMS RESSARCIDO A TRRs (QUADRO 11) | vlr_icms_st_1210 | Consultar o Quadro 11 com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = A6MQ11. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 1.2.11 ICMS RESSARCIDO A IMPORTADORES (QUADRO 12) | vlr_icms_st_1211 | Consultar o Quadro 12 com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = A6MQ12. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 1.2.12 ICMS RESSARCIDO A OUTROS CONTRIBUINTES (QUADRO 13) | vlr_icms_st_1212 | Consultar o Quadro 13 com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = A6MQ13. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 1.2.13 SUB-TOTAL DOS RESSARCIMENTOS (1.2.9 + 1.2.10 + 1.2.11 + 1.2.12) | vlr_icms_st_1213 | Somatório dos campos Vlr 1.2.9, Vlr 1.2.10, Vlr 1.2.11, Vlr 1.2.12 |
| Vlr 1.3 ICMS DEVIDO [1.1.7 - (1.2.8 + 1.2.13)] | vlr_icms_st_13 | Preencher com Vlr 1.1.7 - Vlr 1.2.8 - Vlr 1.2.13 |
| Vlr 1.3.1 DEDUÇÃO TRANSFERIDA DE OUTRO ESTABELECIMENTO DO SUJEITO PASSIVO POR TRIBUTAÇÃO MONOFÁSICA (QUADRO 14) | vlr_icms_st_131 | Consultar o Quadro 14 com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = A6MQ14. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 1.3.2 DEDUÇÃO TRANSFERIDA PARA OUTRO ESTABELECIMENTO DO SUJEITO PASSIVO POR TRIBUTAÇÃO MONOFÁSICA (QUADRO 15) | vlr_icms_st_132 | Consultar o Quadro 15 com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = A6MQ15. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 1.3.3 ICMS A RECOLHER (1.3 + 1.3.1) ou (1.3 - 1.3.2) | vlr_icms_st_133 | Preencher com: Vlr 1.3 + Vlr 1.3.1 ou                            Vlr 1.3 - Vlr 1.3.2 |
| No Processo | Num_Processo | Número do processo da geração |
| Ind Dig Calc | Ind Dig Calc | 1-Inserido manualmente, 2-calculado via Geração do Anexo VII-M, 3-calculado via Geração do Anexo VII-M e atualizado via tela de manutenção. |
| Usuário | Usuario | Usuário da aplicação |


| Nome do Campo | Nome físico do campo | Regra de Preenchimento |
| --- | --- | --- |
| Empresa | Cod_Empresa | Empresa de login |
| Estabelecimento: | Cod_Estab | Estabelecimento selecionado na Geração |
| Mês/Ano Referência: | Dat_apuracao | Último dia do mês/ano da geração |
| UF Destinatária do Anexo VI-M | Ident_estado_destino | UF Destinatária do Anexo VI-M recuperada dos quadros selecionados nos campos abaixo. |
| Vlr 2.1 ICMS SOBRE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRRs (QUADRO 4.2) | vlr_icms_st_21 | Consultar o Quadro 4.2 com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = A6MQ42. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 2.2 ICMS SOBRE OPERAÇÕES REALIZADAS POR IMPORTADORES (QUADRO 5) | vlr_icms_st_22 | Consultar o Quadro 5 com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = A6MQ5. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 2.3 ICMS PROVISIONADO (2.1 + 2.2) | vlr_icms_st_23 | Preencher com Vlr 2.1 + Vlr 2.2 |
| No Processo | Num_Processo | Número do processo da geração |
| Ind Dig Calc | Ind Dig Calc | 1-Inserido manualmente, 2-calculado via Geração do Anexo VII-M, 3-calculado via Geração do Anexo VII-M e atualizado via tela de manutenção. |
| Usuário | Usuario | Usuário da aplicação |
