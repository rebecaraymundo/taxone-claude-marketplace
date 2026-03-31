# MTZ_Manutenção_Anexo_VII-M_Quadro 1

> Fonte: MTZ_Manutenção_Anexo_VII-M_Quadro 1.docx






THOMSON REUTERS

Manutenção Anexo VII-M Quadro 1
Módulo Combustível e Derivados de Petróleo (SCANC)

Localização: Movimento de Refinaria  Manutenção Anexo VII-M  Quadro 1


DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3

## Regras dos Campos


Localização da tela: Específicos >> Combustível e Derivados de Petróleo
Movimento de Refinaria  Manutenção Anexo VII-M  Quadro 1

O Quadro 1 é uma totalização dos quadros 2 ao 7 e do valor 2.3 do quadro 2 do Anexo VI-M.
A tela permite digitação livre dos valores.
Ao fazer manutenção nos quadros 2 ao 7, os valores do quadro 1 são recalculados.
O quadro 1 é recalculado como um todo na rotina de Geração dos Anexos VII e VII-M

Tabela: CBT_ANEXO7M_QUADR1



| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS535202 |  |  |


| Nome do Campo | Nome físico do campo | Regra de Preenchimento |
| --- | --- | --- |
| Empresa | Cod_Empresa | Empresa de login |
| Estabelecimento: | Cod_Estab | Estabelecimento selecionado na Geração |
| Mês/Ano Referência: | Dat_apuracao | Último dia do mês/ano informado na tela de geração |
| UF Destinatária do Anexo VII-M | Ident_estado_destino | UF Destinatária do Anexo VII-M recuperada dos quadros selecionados nos campos abaixo. |
| Vlr 1.1 VALOR PROVISIONADO CONFORME LINHA 2.3 DO QUADRO 2 DO ANEXO VI-A | vlr_icms_st_11 | Consultar o Quadro 2 do Anexo VI-M com os critérios: empresa, estabelecimento e mês/ano referência informados para geração. Recuperar Vlr 2.3 por UF Destinatária do Anexo VII-M. Gravar esse campo com o Vlr 2.3. |
| Vlr 1.2 REPASSE GLOSADO REFERENTE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRRs (QUADRO 2) | vlr_icms_st_12 | Consultar o Quadro 2 do Anexo VII-M com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = “A7MQ2”. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VII-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 1.3 REPASSE GLOSADO REFERENTE OPERAÇÕES REALIZADAS POR IMPORTADORES (QUADRO 3) | vlr_icms_st_13 | Consultar o Quadro 3 do Anexo VII-M com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = “A7MQ3”. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VII-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 1.4 REPASSE GLOSADO REFERENTE A BIOCOMBUSTÍVEIS (QUADRO 4) | vlr_icms_st_14 | Consultar o Quadro 4 do Anexo VII-M com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = “A7MQ4”. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VII-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 1.5 VALOR DA PROVISÃO A SER REPASSADA (1.1 - 1.2 - 1.3 - 1.4) | vlr_icms_st_15 | Somatório dos campos Vlr 1.1, Vlr 1.2, Vlr 1.3, Vlr 1.4. |
| Vlr 1.6 DEDUÇÃO GLOSADA REFERENTE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRRs (QUADRO 5) | vlr_icms_st_16 | Consultar o Quadro 5 do Anexo VII-M com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = “A7MQ5”. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VII-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 1.7 DEDUÇÃO GLOSADA REFERENTE OPERAÇÕES REALIZADAS POR IMPORTADORES (QUADRO 6) | vlr_icms_st_17 | Consultar o Quadro 6 do Anexo VII-M com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = “A7MQ6”. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VII-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 1.8 DEDUÇÃO GLOSADA REFERENTE A BIOCOMBUSTÍVEIS (QUADRO 7) | vlr_icms_st_18 | Consultar o Quadro 7 do Anexo VII-M com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD_TAG = “A7MQ7”. Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VII-M. Gravar esse campo com o Vlr ICMS. |
| Vlr 1.9 VALOR DA PROVISÃO PARA DEDUÇÃO GLOSADA (1.6 + 1.7 + 1.8) | vlr_icms_st_19 | Somatório dos campos Vlr 1.6, Vlr 1.7, Vlr 1.8. |
| Vlr 1.10 ICMS A RECOLHER (1.5 + 1.9) | vlr_icms_st_110 | Somatório dos campos Vlr 1.5, Vlr 1.9 |
| No Processo | Num_Processo | Número do processo da geração |
| Ind Dig Calc | Ind Dig Calc | 2 |
| Usuário | Usuario | Usuário da aplicação |
