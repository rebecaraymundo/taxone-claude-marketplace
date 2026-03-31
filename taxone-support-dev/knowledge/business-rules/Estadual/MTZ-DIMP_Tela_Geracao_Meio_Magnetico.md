# MTZ-DIMP_Tela_Geraçao_Meio_Magnetico

> Fonte: MTZ-DIMP_Tela_Geraçao_Meio_Magnetico.docx






THOMSON REUTERS

Módulo DIMP

Geração do Arquivo Magnético



Localização: Menu Estadual, módulo DIMP, menu Geração à Geração Meio Magnético


DOCUMENTO DE REQUISITO






Sumário


1.	Regras Gerais	2
2.	Parâmetros de Tela	3


























## Regras Gerais


O objetivo desta tela é permitir a geração do meio magnético da DIMP.





## Parâmetros de Tela













| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS436204 | Aline Melo | Criação do documento e criação dos campos em atendimento os registros 0005 e 0006. | 06/02/2023 |
| MFS436210 | Liliane Assaf | Criação do campo Processo Admin/Fiscal da Intimação para geração do registro 0700. | 22/02/2023 |
| MFS748247 | Graciela Soares | Inclisão da Versão versão 10 e nova condição no campo Finalidade. | 18/02/2025 |


| Campo | Tipo | Obrig | Ed | Formato/ Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Data Início | Data (dia, mês e ano) | S | S | DD/MM/AAAA | Neste campo o usuário informar a data inicial (dia, mês e ano) para a geração do arquivo. |
| Data Fim | Data (dia, mês e ano) | S | S | DD/MM/AAAA | Neste campo o usuário informar a data final (dia, mês e ano) para a geração do arquivo. |
| UF | Alfanumérico | S | N | Lista  Default = “Todas UF’s” | Este campo deve apresentar todas as UF’s. |
| Versão do Layout | Alfanumérico | S | N | Lista  Default= “09” | Este campo deve apresentar as seguintes opções:  - 06 - 07 - 09 -10  OBS: Alteração da ordem de seleção do campo Versão em Tela, posicionar antes do campo “Finalidade do Arquivo” |
| Finalidade do arquivo | Alfanumérico | S | N | Lista  Default = “1 – Remessa de arquivo Normal” | Este campo deve apresentar as seguintes opções:  1 – Remessa de arquivo Normal 2 – Remessa de arquivo de retificação de informações 3 - Remessa de arquivo para atender intimação 4 – Remessa de arquivo zerado  5 – Remessa de arquivo de encerramento de atividades 6 – Autorização para Instituição Parceira 7 – Realiza apenas operações dispensadas do envio da DIMP 8 – Não realiza operações na UF de destino do arquivo  [MFS748247] Exclusão das opções de finalidade 7 e 8 a partir da Versão do Layout 10. Quando selecionada a opção 10 ou posteriores no campo “Versão do layout”  não exibir as opções “7 – Realiza apenas operações dispensadas do envio da DIMP” e “8 – Não realiza operações na UF de destino do arquivo” |
| Responsável para Contato | Alfanumérico | S | N | Lista | Neste campo deve ser listado o campo NOM_RESPONSAVEL da tabela RESP_INFORMACAO. |
| Responsável Técnico para Contato | Alfanumérico | N | N | Lista | Neste campo deve ser listado o campo NOM_RESPONSAVEL da tabela RESP_INFORMACAO. |
| Tipo de Ambiente |  | S | N | Radio Button | Apresenta duas opções: - Produção - Homologação |
| Processo Admin/Fiscal da Intimação | Alfanumérico | N | S | Texto Desabilitado | Quando o usuário selecionar no campo Finalidade do Arquivo a opção “3” e na “Versão do Layout” a opção 09 ou superior (versão >=09), então esse campo deve ser habilitado.  Caso contrário, esse campo deve ser limpo e bloqueado. |
| Estabelecimentos | Alfanumérico | S | N |  | Neste campo é exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário. |
| Selecionar | Alfanumérico | N | N |  | Esta opção é um facilitador que permite ao usuário selecionar um ou mais estabelecimentos através de uma janela de seleção da tabela de estabelecimentos.  O filtro dos estabelecimentos disponibilizados para seleção segue a mesma regra descrita para o campo “Estabelecimento”:  - Somente Estabelecimentos da empresa do login;   Quando esta opção é utilizada, após escolher os estabelecimentos e clicar no botão <OK> da janela de seleção, os estabelecimentos selecionados pelo usuário serão demonstrados no campo “Estabelecimentos” já marcados. |
| Marcar todos | Alfanumérico | N | N |  | Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados no campo “Estabelecimentos”. |
