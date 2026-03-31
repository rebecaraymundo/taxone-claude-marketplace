# MTZ_Manutenção_Anexo_VII-M_Quadro 2 a 7

> Fonte: MTZ_Manutenção_Anexo_VII-M_Quadro 2 a 7.docx






THOMSON REUTERS

Manutenção Anexo VII-M Quadros 2 a 7
Módulo Combustível e Derivados de Petróleo (SCANC)

Localização: Movimento de Refinaria  Manutenção Anexo VII-M  Quadros 2 a 7


DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3

## Regras dos Campos


Localização da tela: Específicos >> Combustível e Derivados de Petróleo
Movimento de Refinaria  Manutenção Anexo VII-M  Quadros 2 a 7

Tabela de Destino: CBT_ANEXO7M_QUADR2A7

Definição dos campos a serem apresentados na tela:

Estabelecimento:
Habilitado se o usuário entrou sem estabelecimento de login.
Desabilitado se o estabelecimento foi informado no login do módulo.
Campo Obrigatório
Gravar campo COD_ESTAB CBT_ANEXO7M_QUADR2A7

Mês/Ano Referência:
Habilitado
Campo obrigatório.
Gravar DAT_APURACAO CBT_ANEXO7M_QUADR2A7 com o último dia do mês/ano informado.

UF Destinatária do Anexo VII-M:
Habilitado
Campo Obrigatório
Gravar IDENT_ESTADO_DESTINO CBT_ANEXO7M_QUADR2A7

Tipo:
Radium Botton com duas opções:
( ) Repasse
( ) Dedução
Default: Repasse
Campo Obrigatório. Não é gravado na tabela CBT_ANEXO7M_QUADR2A7, serve apenas como filtro para a lista a ser apresentada no campo seguinte.

Quadro:
Habilitado
Campo Obrigatório
Lista fixa composta pelos itens, que são apresentados de acordo com a seleção no campo anterior (Repasse ou Dedução):
2 - REPASSE GLOSADO REFERENTE A OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRR
3 – REPASSE GLOSADO REFERENTE A OPERAÇÕES REALIZADAS POR IMPORTADORES
4 - REPASSE GLOSADO REFERENTE A BIOCOMBUSTÍVEIS
5 – DEDUÇÃO GLOSADA REFERENTE A OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRR
6 - DEDUÇÃO GLOSADA REFERENTE A OPERAÇÕES REALIZADAS POR IMPORTADORES
7 – DEDUÇÃO GLOSADA REFERENTE A BIOCOMBUSTÍVEIS

Gravar os campos COD_TAG CBT_ANEXO7M_QUADR2A7 conforme regra abaixo:


Pessoa Fís/Jur:
Habilitado
Campo Obrigatório
Gravar IDENT_FIS_JUR CBT_ANEXO7M_QUADR2A7

UF do Quadro:
Habilitado.
Campo Obrigatório
Gravar IDENT_ESTADO_QUAD CBT_ANEXO7M_QUADR2A7

Os campos Pessoa Fís/Jur e UF do Quadro variam de acordo com o item selecionado no campo Quadro:



Vlr ICMS
Habilitado
Gravar VLR_ICMS_ST CBT_ANEXO7M_QUADR2A7

No Processo
Desabilitado
Gravar NUM_PROCESSO CBT_ANEXO7M_QUADR2A7

Ind Dig Calc:
Não apresentar na tela.
Gravar:
Gravar:
1 – inserido via tela de manutenção
2 – inserido via geração do Anexo VII-M
3 - inserido via geração do Anexo VII-M e atualizado pela tela de manutenção

Usuário
Não apresentar na tela.
Gravar o usuário de login da aplicação.




| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS535202 |  |  |


| Item | COD_TAG |
| --- | --- |
| 2 | A7MQ2 |
| 3 | A7MQ3 |
| 4 | A7MQ4 |
| 5 | A7MQ5 |
| 6 | A7MQ6 |
| 7 | A7MQ7 |


| Item - Quadro | Título Pessoa Fís/Jur | Título UF do Quadro | Regra do Campo UF do Quadro |
| --- | --- | --- | --- |
| 2 | Distribuidora/TRR | UF Distribuidora/TRR | Habilitado e trazer como default a UF da Pessoa Fis/Jur (Cadastro da X04) |
| 3 | Importadora | UF Importadora | Habilitado e trazer como default a UF da Pessoa Fis/Jur (Cadastro da X04) |
| 4 | Distribuidora/TRR | UF Distribuidora/TRR | Habilitado e trazer como default a UF da Pessoa Fis/Jur (Cadastro da X04) |
| 5 | Distribuidora/TRR | UF Destinatária | Habilitar |
| 6 | Importadora | UF Destinatária | Habilitar |
| 7 | Distribuidora/TRR | UF Destinatária | Habilitar |
|  |  |  |  |


| Tela | PL usado pela tela |
| --- | --- |
| Manutenção Anexo VII-M |  |
| Quadro 1 |  |
| Quadros 2 a 7 | Saf_atualiza_anexo_7M_q1 da Pkg_Cbt_Anexo7_fproc |
