# MTZ_Tela_Envio_de_Registros_XML_de_Arquivos_Externos_Grandes_Volumes

> Fonte: MTZ_Tela_Envio_de_Registros_XML_de_Arquivos_Externos_Grandes_Volumes.docx






THOMSON REUTERS
REINF >> Envio de Eventos – Grandes Volumes
Envio de Registros XML de Arquivos Externos - Grandes Volumes



DOCUMENTO DE REQUISITO


Sumário

1.	Objetivo	3
2.	TELA	3
3.	Regras dos Campos	4
4.	Abas Geradas	7

## Objetivo


O objetivo desta tela é permitir que os arquivos XML de origem externa sejam enviados por fora do painel de controle de eventos. Após o envio, a consulta é feita normalmente no painel. Nesta tela, não é gerada a retificação de eventos dos arquivos de origem externa. A retificação é permitida apenas no painel.
O envio dos arquivos apartado do painel, foi necessário, devido a grandes volumes de eventos importados atendendo o cenário do JCP.


## TELA




## Regras dos Campos


Localização da tela: Módulo: SPED>> EFD – REINF
Menu: REINF >> Envio de Eventos – Grandes Volumes >> Arquivos de Origem Externa

Título da tela: Envio de Registros XML de Arquivos Externos - Grandes Volumes


Campos de preenchimento obrigatório: Empresa, Período (MM/AAAA), Versão, Ambiente, Eventos (pelo menos um deve ser marcado), selecionar um Estabelecimento


## Abas Geradas




| MFS | Nome | Descrição |
| --- | --- | --- |
| MFS-577767 | Alessandra Cristina Navatta | Criação do Documento |
| MFS-578364 | Alessandra Cristina Navatta | Adequação de Menu |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS |
| --- | --- | --- | --- | --- | --- | --- |
| Empresa | Texto | S | N | Código – Razão Social | Apresentar a empresa que está logada no sistema | MFS-577767 |
| Período (MM/AAAA) | Data | S | S | MM/AAAA | Informar o período (mês e ano) que será considerado para recuperar os registros Por default, a tela deve apresentar o mês corrente, mas, o usuário pode alterar a informação. | MFS-577767 |
| Versão | Lista | S | N | Código | Apresenta a versão 2.1.2 | MFS-577767 |
| Ambiente | Radio-Button | S | S | Default: Produção Restrita | Lista de Opções: Produção Produção Restrita | MFS-577767 |
| Eventos | Check-box | S | S | Ambas opções marcadas | Lista de opções:  R-4010 – Pagamentos/Créditos a Beneficiário Pessoa Física R-4020 - Pagamentos/Créditos a Beneficiário Pessoa Jurídica | MFS-577767 |
| Estabelecimento | Combo | S | S | Código – Razão Social | Apresenta lista de estabelecimento da empresa logada, que possuam algum arquivo importado no mês informado, com a mesma versão e tipo de ambiente selecionados na tela. | MFS-577767 |
| Executar | Botão |  |  |  | Mensagens de Erro na Tela:  Se não for informado o Período (MM/AAAA), Será exibida a mensagem: “Informe Período (MM/AAAA).” Se não for selecionado pelo menos um evento para processamento: Será exibida a mensagem: “Ao menos um evento deve ser selecionado.” Se não for informado o Estabelecimento: Será exibida a mensagem: “Informe Estabelecimento.” | MFS-577767 |


| Parâmetros | Esta aba apresenta a tela de manutenção. Conforme mockup e regras definidas nos itens 1. Telas e 2. Regras dos Campos. | MFS-577767 |
| --- | --- | --- |
| Processos | Esta aba será gerada sempre que for criado um processo. Deve conter o número do processo, os parâmetros, a situação do processo, as datas Início Execução e Fim Execução, além da informação do Usuário que fez a execução do processo. | MFS-577767 |
| Logs | Esta aba deve demonstrar os logs do processo. | MFS-577767 |
