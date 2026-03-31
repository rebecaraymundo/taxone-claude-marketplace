# MTZ_Tela_Importacao_de_Registros_XML_Familia_4000

> Fonte: MTZ_Tela_Importacao_de_Registros_XML_Familia_4000.docx






THOMSON REUTERS
REINF
Arquivos Externos
Importação de Registros XML Família 4000



DOCUMENTO DE REQUISITO






Sumário

1.	TELA	3
2.	Regras dos Campos	3
3.	Abas Geradas	8

## Objetivo


O objetivo desta funcionalidade é permitir importação, via solução fiscal DW/TaxOne, de xml dos eventos R-4010 e/ou R-4020 enviados pelos bancos, atendendo ao cenário de JCP, e ou qualquer outra fonte externa. Sendo possível transmitir esses eventos para mensageria REINF e consequentemente envio a Receita.

## TELA





## Regras dos Campos


Localização da tela: Módulo: SPED>> EFD – REINF
Menu: REINF >> Arquivos Externos >> Importação

Título da tela: Importação de Registros XML Família 4000


Campos de preenchimento obrigatório: Empresa, Diretório Servidor (Name/Path), selecionar pelo menos um Arquivo para Processamento


## Abas Geradas





| MFS | Nome | Descrição |
| --- | --- | --- |
| MFS-561257 | Alessandra Cristina Navatta | Criação do Documento |
| MFS-565763 | Alessandra Cristina Navatta | Inclusão de mensagens para a validação da estrutura do XSD |
| MFS-57284 | Alessandra Cristina Navatta | Inclusão do campo Estabelecimento. Inclusão e exclusões de validação no botão Executar. |
| MFS-587132 | Alessandra Cristina Navatta | Permitir importar arquivos CSV. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS |
| --- | --- | --- | --- | --- | --- | --- |
| Empresa | Texto | S | N | Código – Razão Social | Apresentar a empresa que está logada no sistema | MFS-561257 |
| Período | Data | S | S | MM/AAAA | Informar o período (mês e ano) que será considerado para importar os arquivos. Por default, a tela deve apresentar o mês corrente, mas, o usuário pode alterar a informação. | MFS-561257 |
| Estabelecimento | Lista | S | N | Código – Razão Social | Apresentar os estabelecimentos da empresa que está logada no sistema, considerando os estabelecimentos que estão configurados na tela Dados Iniciais do REINF (tabela reinf_dados_iniciais_estab) | MFS-572084 |
| Diretório Servidor (Name – Path) | Lista | S | S |  | Permite escolher o diretório (criado no servidor), onde o sistema recuperará arquivos para serem processados. | MFS-561257 |
| Tipo de Arquivos | Radion-Button |  |  | CSV | Lista de Opções:  XML CSV | MFS-587132 |
| Sobrescreve registros importados anteriormente | Check-box | N | S | Default: Desmarcado | Quando marcado, permite sobrescrever o registro já importado. (Será considerado a empresa, estabelecimento, e id do evento.) | MFS-561257 |
| ideEvtAdic caso não informada | Texto | N | S |  | Quando preenchido e o campo ideEvtAdic estiver sem preenchimento, será considerada o conteúdo deste campo. | MFS-561257 |
| Arquivos para Processamento | Grid | S | S |  | Exibe todos os arquivos de extensão CSV ou XML (de acordo com o tipo de arquivo selecionado) que estão no campo Diretório Servidor (Name – Path) | MFS-561257 MFS-587132 |
| Selecionar | Botão |  |  |  | Permite que o usuário selecione os Arquivos para Processamento   Tratamentos:  Modal 'Selecionar Arquivos para Processamento ‘ Ao ser acionado abrir o Modal 'Selecionar Arquivos para Processamento’. Apresentando o campo nome   Botões do Modal 'Selecionar Arquivos para Processamento': Critério, Cancelar, OK e Salvar...   Botões Critério, Cancelar, OK e Salvar  - Ao selecionar o botão 'Cancelar', nada será feito e o Modal 'Selecionar Arquivos para Processamento‘ será fechado.  - Ao selecionar o botão 'Critério', os Arquivos poderão ser filtrados e no novo modal serão exibidos habilitado os botões Pesquisar e Cancelar.  -Ao confirmar a seleção dos registros, acionando o botão ‘OK’, apresentar os Arquivos no componente “Arquivos para Processamento” da tela Principal - Permite a seleção de vários registros por vez. - Ao entrar no modal, pelo menos um registro deve ser selecionado, se for selecionado o botão 'Ok', caso contrário, exibir a mensagem “Selecionar pelo menos um Arquivo para Processamento”. -Ao selecionar o botão ’Salvar’, o sistema salva as informações recuperadas. | MFS-561257 |
| Marcar Todos | Botão |  |  |  | Permite ao usuário selecionar ou desmarcar todos os registros da grid Arquivos para Processamento. | MFS-561257 |
| Executar | Botão |  |  |  | Mensagem de erro na tela:  Se não for indicado o diretório: Será exibida a mensagem: “Informe Diretório Servidor (Name – Path).” Se não for informado o período: Será exibida a mensagem: “Informe Período.” Se não for selecionado pelo menos um arquivo para importação: Será exibida a mensagem: “Selecione pelo menos um Arquivo para Processamento.”  Quando a execução é realizada: Exibir a mensagem: ”Execução Finalizada”  Arquivos Importados com sucesso:  Os arquivos importados com sucesso, serão armazenados em uma tabela, criada para manter os arquivos importados por essa funcionalidade (reinf_xml_imp_r4000).  Só serão considerados arquivos com extensão XML, nesta funcionalidade. Na importação dos arquivos XML, sempre o campo ideEvtAdic será preenchido, considerando uma das três regras abaixo:  Os arquivos importados com a informação do campo ideEvtAdic preenchidos no próprio XML, serão importados SEMPRE considerando essa informação.  Arquivos sem a informação do campo ideEvtAdic no XML: Quando não for indicado o campo ‘ideEvtAdic caso não informada’, o sistema irá preencher a informação com a raiz do CNPJ do contribuinte (8 primeiras posições)  Arquivos sem a informação do campo ideEvtAdic no XML: Quando for indicado o campo ‘ideEvtAdic caso não informada’, iremos preencher a informação com o conteúdo deste campo.   Mensagens no Log:  Mensagem de Sucesso:   Para cada arquivo importado com sucesso, será a mensagem: “Importando arquivo <<nome do arquivo>> Arquivo importado com sucesso”   Mensagem de Erro: Caso seja encontrado erro na importação serão exibidas as mensagens, conforme indicado nas validações abaixo:  [ALTERAÇÃO MFS-565763] Inclusão de mensagens, validação do XSD com o XML:   Validação do XSD com o XML: Se não for possível ler o xml por conta da estrutura do arquivo enviado, exibir a mensagem: “Erro ao ler estrutura do xml. Arquivo inválido.” Quando o xml possuir informações incoerentes com as regras do XDS, exibir a mensagem: “Arquivo com informação inválida.” Quando o XSD que foi carregado (pelo sistema, na tela de painel de controle de evento), e que será utilizado para validar o XML (arquivo recebido), estiver com algum problema, exibir a mensagem: “Erro no XSD para a validação do XML.” Outras Validações:  Verifica se a RAIZ do CNPJ (8 primeiras posições do campo nrInsc (da tag ideContri) é igual as 8 primeiras posições do campo nrInscEstab (da tag de ideEstab), caso não seja igual, não importa e exibe a mensagem: “Importando arquivo <<nome do arquivo>> Informação do Contribuinte não relacionada com o Estabelecimento selecionado. Valor da Tag: ideContri\nrInsc: 99999999 Raiz do CNPJ do Estabelecimento: 99999999 Arquivo <<nome do arquivo>> não importado.”  Quando o período indicado na tela é diferente do período existente no arquivo XML, exibir a mensagem:  “Importando arquivo <<nome do arquivo>> Período da apuração diferente do período informado <<exibir período informado na tela, formato MM-AAAA>> Valor da tag: IdeEvento\perApur: << exibir período informado na tela, formato MM-AAAA >> Arquivo <<nome do arquivo>> não importado.”  Quando a versão do XML for diferente de 2.1.2, ou ainda o evento não ser um evento válido, atendido por essa funcionalidade (R-4010 e ou R-4020) exibir a mensagem:   “Importando arquivo <<nome do arquivo>> Versão/Evento do XML não suportado(s) pela aplicação. Erro ao importar o arquivo: <<nome do arquivo>>  Arquivo <<nome do arquivo>> não importado.”  [EXCLUSÃO MFS-572084] Quando não for encontrado o estabelecimento, exibir a mensagem:   “Importando arquivo <<nome do arquivo>> Informação da Identificação do Estabelecimento não encontrada. Valor da tag ideEstab\nrInscEstab: 9999999999999999 Erro ao importar o arquivo: <<nome do arquivo>>  Arquivo <<nome do arquivo>> não importado.”  [EXCLUSÃO MFS-572084] Quando for encontrado mais de um código de estabelecimento com o mesmo CNPJ, exibir a mensagem:   “Importando arquivo <<nome do arquivo>> Mais de um código encontrado para a identificação do estabelecimento. Valor da tag ideEstab\nrInscEstab: 9999999999999999 Erro ao importar o arquivo: <<nome do arquivo>>  Arquivo <<nome do arquivo>> não importado.” Se for importado um arquivo com as mesmas informações de chave, exibir a mensagem:  “Importando arquivo <<nome do arquivo>> Existe registro com a mesma chave importado anteriormente. Erro ao importar o arquivo: <<nome do arquivo>>  Arquivo <<nome do arquivo>> não importado.” [ALTERAÇÃO MFS-572084] Inclusão de validação: Ao ler o arquivo, se o CNPJ do estabelecimento (tag ideEstab, campo nrInscEstab) não for igual a do estabelecimento selecionado na tela, exibir a mensagem: “Informação do Estabelecimento no XML não relacionada com o estabelecimento selecionado.” Valor da Tag: ideEstab/nrInscEstab: XXXXXXXXXXXXXXX CNPJ do Estabelecimento “Cod. Estab”:  XXXXXXXXXXXXXX. Arquivo <<nome do arquivo>> não importado.”  [ALTERAÇÃO MFS-587132] Importação dos Arquivos CSV:  Será desconsiderada a primeira linha do arquivo por ser de header. | MFS-561257 MFS-565673 MFS-572084 MFS-587132 |


| Parâmetros | Esta aba apresenta a tela de importação. Conforme mockup e regras definidas nos itens 1. Telas e 2. Regras dos Campos. | MFS-561257 |
| --- | --- | --- |
| Processos | Esta aba será gerada sempre que for criado um processo. Deve conter o número do processo, os parâmetros, a situação do processo, as datas Início Execução e Fim Execução, além da informação do Usuário que fez a execução do processo. | MFS-561257 |
| Logs | Esta aba deve demonstrar os logs do processo. | MFS-561257 |
