# MTZ_Tela_Envio_de_Eventos_Grandes_Volumes_Familia_4000

> Fonte: MTZ_Tela_Envio_de_Eventos_Grandes_Volumes_Familia_4000.docx






THOMSON REUTERS
REINF
Envio de Eventos - Grandes Volumes – Família 4000



DOCUMENTO DE REQUISITO


Sumário

1.	Objetivo	3
2.	TELA	3
3.	Regras dos Campos	3
4.	Abas Geradas	5

## Objetivo


O objetivo desta tela é permitir que os arquivos XML da família 4000 sejam enviados por fora do painel de controle de eventos, neste momento, estamos liberando o envio dos eventos R-4010, R-4020, R-4040 e R-4080. Após o envio, a consulta é feita normalmente no painel. Nesta tela, não é gerada a retificação de evento. A retificação é permitida apenas no painel. O envio dos arquivos apartado do painel, foi necessário, devido a grandes volumes de eventos.


## TELA



## Regras dos Campos


Localização da tela: Módulo: SPED>> EFD – REINF
Menu: REINF >> Envio de Eventos - Grandes Volumes >> Família 4000

Título da tela: Envio de Eventos - Grandes Volumes – Família 4000


Campos de preenchimento obrigatório: Empresa, Período (MM/AAAA), Versão, Ambiente, Eventos (pelo menos um deve ser marcado), selecionar um Estabelecimento


## Abas Geradas




| MFS | Nome | Descrição |
| --- | --- | --- |
| MFS-578364 | Alessandra Cristina Navatta | Criação do Documento |
| MFS-598422 | Alessandra Cristina Navatta | Inclusão do Evento R-4010 na tela, campo Eventos |
| MFS-601063 | Alessandra Cristina Navatta | Inclusão do Evento R-4020 na tela, campo Eventos |
| MFS-601064 | Alessandra Cristina Navatta | Inclusão do Evento R-4040 na tela, campo Eventos |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS |
| --- | --- | --- | --- | --- | --- | --- |
| Empresa | Texto | S | N | Código – Razão Social | Apresentar a empresa que está logada no sistema | MFS-578364 |
| Período (MM/AAAA) | Data | S | S | MM/AAAA | Informar o período (mês e ano) que será considerado para recuperar os registros Por default, a tela deve apresentar o mês corrente, mas, o usuário pode alterar a informação. | MFS-578364 |
| Versão | Lista | S | N | Código | Apresenta a versão 2.1.2 | MFS-578364 |
| Ambiente | Radio-Button | S | S | Default: Produção Restrita | Lista de Opções: Produção Produção Restrita | MFS-578364 |
| Eventos | Check-box | S | S | Desmarcado | Lista de opções:  [ALTERAÇÃO MFS-598422] R-4010 – Pagamentos/Créditos a Beneficiário Pessoa Física [ALTERAÇÃO MFS-601063] R-4020 – Pagamentos/Créditos a Beneficiário Pessoa Jurídica [ALTERAÇÃO MFS-601064] R-4040 – Pagamentos/Créditos a Beneficiários não Identificados R-4080 – Retenção no Recebimento | MFS-578364 MFS-598422 MFS-601063 MFS-601064 |
| Estabelecimento | Combo | S | S | Código – Razão Social | Apresenta lista de estabelecimento da empresa logada, que possuam algum registro de evento gerado selecionado, no mês informado, com a mesma versão e tipo de ambiente selecionados na tela. | MFS-578364 |
| Executar | Botão |  |  |  | Mensagens de Erro na Tela:  Se não for informado o Período (MM/AAAA), será exibida a mensagem: “Informe Período (MM/AAAA).” Se não for informado o Estabelecimento, será exibida a mensagem: “Informe Estabelecimento.”  Mensagem exibida no log:  Se não for selecionado pelo menos um evento para processamento, será exibida a mensagem no log: “Ao menos um evento deve ser selecionado.” | MFS-578364 |


| Parâmetros | Esta aba apresenta a tela de manutenção. Conforme mockup e regras definidas nos itens 1. Telas e 2. Regras dos Campos. | MFS-578364 |
| --- | --- | --- |
| Processos | Esta aba será gerada sempre que for criado um processo. Deve conter o número do processo, os parâmetros, a situação do processo, as datas Início Execução e Fim Execução, além da informação do Usuário que fez a execução do processo. | MFS-578364 |
| Logs | Esta aba deve demonstrar os logs do processo. | MFS-578364 |
