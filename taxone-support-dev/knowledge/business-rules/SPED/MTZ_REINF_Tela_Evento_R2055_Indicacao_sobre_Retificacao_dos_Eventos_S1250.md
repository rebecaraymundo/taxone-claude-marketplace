# MTZ_REINF_Tela_Evento_R2055_Indicacao_sobre_Retificacao_dos_Eventos_S1250

> Fonte: MTZ_REINF_Tela_Evento_R2055_Indicacao_sobre_Retificacao_dos_Eventos_S1250.docx






THOMSON REUTERS

Evento R-2055 - Indicação sobre Retificação dos Eventos S-1250
SPED – Reinf (TELA OCULTA DO MENU)



DOCUMENTO DE REQUISITO



Sumário

1.	Introdução	3
2.	Regras dos Campos	3
3.	Botões da Barra de Ferramenta	7
4.	Tela de Relatório	7

## Introdução


Esta tela foi criada para o usuário indicar quais produtores tiveram suas aquisições entregues no e-Social e que agora devem ser retificados na EFD-REINF.
Para conseguir indicar as retificações, é necessário a geração dos eventos R-2055 através da tela de Geração Prévia (Evento R-2055).
Note que pela estrutura liberada no layout 1.5.1 esta retificação não é por apuração e sim por produtor rural. Diante disso, se faz necessário, o usuário indicar quais produtores devem conter a indicação de retificação.

## Regras dos Campos



[ALTERAÇÃO MFS-67713] – Ocultar tela do Menu

Localização da tela: Módulo: SPED >> EFD – Reinf
Menu: REINF >>
Título da tela: Evento R-2055 - Indicação sobre Retificação dos Eventos S-1250

Obs: Ao abrir a tela Evento R-2055 - Indicação sobre Retificação dos Eventos S-1250 deverá abrir uma subtela para seleção do período de geração.




Regra Geral: Só devem ser exibidos na tela as apurações que possuírem eventos R-2055, atendendo os filtros indicado na tela (estabelecimento, apuração), cujo o campo indRetif for igual a “1”, perApur for anterior 202105 (esses campos estão no Registro ideEvento, do próprio R-2055) e que estão com Status = Aguardando geração do XML.










## Botões da Barra de Ferramenta


Confirma, Relatório, Fecha

## Tela de Relatório


4.1 Seleção do Relatório


4.2 Layout



| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS59340 | Alessandra Cristina Navatta | Criação da Tela Evento R-2055 - Indicação sobre Retificação dos Eventos S-1250, para atender o layout 1.5.1 do REINF |
| MFS-67713 | Alessandra Cristina Navatta | O campo retifS1250, do Registro ideEvento, não está sendo tratado atualmente pelo FISCO, mas também não foi retirado do layout. Diante disso, estamos ocultando esta tela do Menu. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Texto | S | N | Código + Estabelecimento | Exibir o estabelecimento selecionado na chamada da subtela de seleção. | MFS-59340 |
| Versão | Texto | S | N | 1.5.1 | Exibir a versão da apuração que foi selecionada na chamada da subtela de seleção. | MFS-59340 |
| Ambiente | Texto | S | N | Produção | Exibir o ambiente da apuração que foi selecionada na chamada da subtela de seleção.   Lista de Valores Válidos:  Produção Produção Restrita | MFS-59340 |
| Evento | Texto | S | N | R-2055 – Aquisição de Produção Rural | Exibir fixo o texto ‘R-2055 – Aquisição de Produção Rural’ | MFS-59340 |
| Pesquisar | TextBox | N | S |  | Permite pesquisar o produtor pelo CNPJ ou CPF | MFS-59340 |
| Marcar Todos | Botão | - | - | Default Desmarcado | Ao selecionar o botão todos os registros da grid serão marcados (caso não estejam selecionados). Se já estivererm selecionados e o botão for acionado, os registros serão desmarcados, | MFS-59340 |
| GRID dos Produtores | GRID dos Produtores | GRID dos Produtores | GRID dos Produtores | GRID dos Produtores | GRID dos Produtores | GRID dos Produtores |
| Retificação do Evento S-1250 | Check-box | - | - |  | Permite selecionar ou não o produtor.   Quando selecionado, este produtor terá a indicação no evento R-2055 que existem informações de retificação para o evento S-1250 (do e-Social) | MFS-59340 |
| CNP/CPF | Texto | S | N | Se CNPJ: XX.XXX.XXX/XXXX-XX Se CPF: XXX.XXX.XXX-XX | Exibir o CNPJ ou CPF do produtor | MFS-59340 |
