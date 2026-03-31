# MTZ_Tela_Manutencao_de_Registros_XML_Familia_4000

> Fonte: MTZ_Tela_Manutencao_de_Registros_XML_Familia_4000.docx






THOMSON REUTERS
REINF
Arquivos Externos
Manutenção de Registros XML Família 4000



DOCUMENTO DE REQUISITO


Sumário

1.	Objetivo	3
2.	TELA	3
3.	Regras dos Campos	3
4.	Abas Geradas	7

## Objetivo


O objetivo desta tela é permitir excluir ou dar manutenção nos arquivos XML importados através da tela Importação de Registros XML Família 4000.


## TELA




## Regras dos Campos


Localização da tela: Módulo: SPED>> EFD – REINF
Menu: REINF >> Arquivos Externos >> Manutenção

Título da tela: Manutenção de Registros XML Família 4000


Campos de preenchimento obrigatório: Empresa, Período, Ambiente, Tipo de Evento, Operação , selecionar pelo menos um Registro para Processamento


## Abas Geradas




| MFS | Nome | Descrição |
| --- | --- | --- |
| MFS-561257 | Alessandra Cristina Navatta | Criação do Documento |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS |
| --- | --- | --- | --- | --- | --- | --- |
| Empresa | Texto | S | N | Código – Razão Social | Apresentar a empresa que está logada no sistema | MFS-561257 |
| Período | Data | S | S | MM/AAAA | Informar o período (mês e ano) que será considerado para recuperar os registros Por default, a tela deve apresentar o mês corrente, mas, o usuário pode alterar a informação. | MFS-561257 |
| Ambiente | Radio-Button | S | S | Default: Produção Restrita | Lista de Opções: Produção Produção Restrita | MFS-561257 |
| Eventos | Radio-Button | S | S | Default: R-4010 | Lista de Opções: R-4010 R-4020 | MFS-561257 |
| Estabelecimentos | Combo | S | S | Código – Razão Social | Exibe os estabelecimentos da empresa que está logada | MFS-561257 |
| Operação | Radio-Button | S | S | Default: Atualizar Registros | Lista de Opções: Excluir Registros Atualizar Registros | MFS-561257 |
| Substituir ideEvtAdic por | Texto | N | S |  | Quando preenchido e o campo ideEvtAdic estiver sem preenchimento, será considerada a informação do campo. | MFS-561257 |
| Registros para Processamento | Grid | S | S |  | Exibe todos os arquivos de extensão xml que estão na tabela reinf_xml_imp_r4000, da empresa, estabelecimento, período, ambiente, e evento, indicado em tela | MFS-561257 |
| Selecionar | Botão |  |  |  | Permite que o usuário selecione os Registros para Processamento   Tratamentos:  Modal 'Selecionar Registros para Processamento ‘ Ao ser acionado abrir o Modal 'Selecionar Registros para Processamento’. Apresentando o campo nome   Botões do Modal 'Selecionar Registros para Processamento': Critério, Cancelar, OK e Salvar...   Botões Critério, Cancelar, OK e Salvar  - Ao selecionar o botão 'Cancelar', nada será feito e o Modal 'Selecionar Registros para Processamento ‘ será fechado.  - Ao selecionar o botão 'Critério', os Arquivos poderão ser filtrados e no novo modal serão exibidos habilitado os botões Pesquisar e Cancelar.  -Ao confirmar a seleção dos registros, acionando o botão ‘OK’, apresentar os Arquivos no componente “Registros para Processamento” da tela Principal - Permite a seleção de vários registros por vez. - Ao entrar no modal, pelo menos um registro deve ser selecionado, se for selecionado o botão 'Ok', caso contrário, exibir a mensagem “Selecionar pelo menos um Arquivo para Processamento”. -Ao selecionar o botão ’Salvar’, o sistema salva as informações recuperadas. | MFS-561257 |
| Marcar Todos | Botão |  |  |  | Permite ao usuário selecionar ou desmarcar todos os registros da grid Registros para Processamento. | MFS-561257 |
| Executar | Botão |  |  |  | Mensagens de Erro na Tela:  Se não for informado o período: Será exibida a mensagem: “Informe Período (MM/AAAA).” Se não for selecionado pelo menos um arquivo para processamento: Será exibida a mensagem: “Selecione pelo menos um Arquivo para Processamento.” Quando a operação for “Atualizar Registros” e o campo ‘Substituir ideEvtAdic por’ estiver sem preenchimento, exibir a mensagem: “Informe Substituir ideEvtAdic por”  Quando a execução é realizada: Exibir a mensagem: ”Execução Finalizada”  Mensagens de Erro no Log:  Se não for possível excluir um registro, exibir a mensagem:"Não foi possível excluir registro na tabela reinf_xml_imp_r4000."  Se não for possível atualizar um registro, exibir a mensagem: "Não foi possível atualizar registro na tabela reinf_xml_imp_r4000."    Mensagens de Totalizadores do Log    Operação Excluir Registros  Iniciando Processamento! Processamento Finalizado! Total de registros excluídos: 1  Operação Atualizar Registros  Iniciando Processamento! Processamento Finalizado! Total de registros atualizados: 1 | MFS-561257 |


| Parâmetros | Esta aba apresenta a tela de manutenção. Conforme mockup e regras definidas nos itens 1. Telas e 2. Regras dos Campos. | MFS-561257 |
| --- | --- | --- |
| Processos | Esta aba será gerada sempre que for criado um processo. Deve conter o número do processo, os parâmetros, a situação do processo, as datas Início Execução e Fim Execução, além da informação do Usuário que fez a execução do processo. | MFS-561257 |
| Logs | Esta aba deve demonstrar os logs do processo. | MFS-561257 |
