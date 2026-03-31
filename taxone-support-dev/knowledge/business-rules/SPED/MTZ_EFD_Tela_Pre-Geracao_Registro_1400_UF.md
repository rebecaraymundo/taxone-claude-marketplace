# MTZ_EFD_Tela_Pre-Geracao_Registro_1400_UF

> Fonte: MTZ_EFD_Tela_Pre-Geracao_Registro_1400_UF.docx






THOMSON REUTERS

Módulo EFD Escrituração Fiscal Digital
Tela de Pré-Geração do Registro 1400 – Periodicidade Anual/Específico por UF

Localização: Menu Sped, Módulo EFD - Escrituração Fiscal Digital, item Pré-Geração  Registro 1400 –Periodicidade Anual/Específico por UF



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3
2.	Layout de Tela	5

## Regras dos Campos


Localização da tela: Menu SPED,  Módulo: EFD Escrituração Fiscal Digital, item de menu Pré-Geração  Registros 1400 – Periodicidade Anual/ Específico por UF

Título da tela: Registros 1400 – Periodicidade Anual/Específico por UF


















## Layout de Tela





| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| OS4728-A | Criação do documento | Criação da Tela Registro 1400 | 27/03/2015 |
| MFS3248 | Lara Aline | Inclusão do campo UF. | 09/11/2016 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Ano Base | Data | S | S | Formato: AAAA | Este campo é de preenchimento obrigatório, nele o usuário informará o ano base das operações a serem totalizadas. | OS4728-A |
| UF | Alfanumérico | S | N | Default: Habilitado | Este campo é de preenchimento obrigatório e deverá ser informado a UF correspondente à geração específica do registro 1400 no Sped Fiscal.  Campo deve exibir as UFs ‘MG e RN’ cadastradas na tabela ESTADO, conforme abaixo:  MG – Minas Gerais RN – Rio Grande do Norte  Obs:  - Quando usuário selecionar o estado de MG – Minas Gerais, deverá ser verificada as regras de pré-geração do documento ‘MTZ-EFD-Pre_Geracao_Registro_1400_MG.docx’ - Quando usuário selecionar o estado de RN – Rio Grande do Norte, deverá ser verificada as regras de pré-geração do documento ‘MTZ-EFD-Pre_Geracao_Registro_1400_RN.docx’ | MFS3248 |
| Geração p/Inscrição Estadual Única | Radio Button | S | S | Default: Não | Este campo é de preenchimento obrigatório deverá ser informado o período de geração correspondente da geração do Sped Fiscal. | OS4728-A |
| Estabelecimento | Alfanumérico | S | N | Formato: <COD ESTAB> - <RAZÃO SOCIAL> | Neste campo serão disponibilizados os estabelecimentos para seleção do usuário, de acordo com os seguintes critérios:      - Somente estabelecimentos da empresa do login;  [ALTERADO MFS3248]      - Se campo UF = MG – Minas Gerais serão apresentados somente estabelecimentos da UF de MG;       - Se campo UF = RN – Rio Grande do Norte serão apresentados somente estabelecimentos da UF de RN;       - Se parâmetro “Geração por inscrição estadual única” = “Sim”: Nesse caso, serão demonstrados apenas os estabelecimentos centralizadores de I.E.U., de acordo com a parametrização do módulo de Controle das Obrigações Estaduais (menu “Obrigações  Empresas/Estabelecimentos com Inscrição Estadual Única”);       - Se parâmetro “Geração por inscrição estadual única” = “Não”. Nesse caso, serão demonstrados todos os estabelecimentos que atendam aos demais critérios; | OS4728-A MFS3248 |
