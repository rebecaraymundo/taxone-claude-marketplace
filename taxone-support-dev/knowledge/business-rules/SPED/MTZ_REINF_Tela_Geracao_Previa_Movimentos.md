# MTZ_REINF_Tela_Geracao_Previa_Movimentos

> Fonte: MTZ_REINF_Tela_Geracao_Previa_Movimentos.docx




THOMSON REUTERS

Geração Prévia dos Movimentos
SPED – Reinf



DOCUMENTO DE REQUISITO



Sumário

1.	Tela	5
2.	Regras dos Campos	7


## Tela


DW:









TAXONE (trecho da tela exibindo o parâmetro ‘Gerar Todos os Eventos’:





## Regras dos Campos


Localização da tela: Módulo: SPED >> EFD – Reinf
Menu: REINF >> Geração Prévia >> Movimentos

Título da tela: Geração Prévia dos Movimentos






| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS8958 | Elenilson Coutinho | Inclusão da Tela de Geração Prévia dos Eventos do EFD – Reinf |
| MFS11670 | Elenilson Coutinho | Inclusão do Evento R-2040 |
| MFS12178 | Lara Aline | Inclusão de verificação das informações do contribuinte na recuperação dos estabelecimentos. |
| MFS14462 | Lara Aline | Inclusão do campo Versão |
| MFS15338 | Lara Aline | Inclusão do parâmetro ‘Desconsiderar NFs fora da Competência’. |
| MFS15740 | Lara Aline | Inclusão do parâmetro ‘Geração por Estabelecimento’. |
| MFS17973 | Lara Aline | Inclusão do parâmetro ‘R-2099 – Fechamento dos Eventos Periódicos – Sem Movimento’. |
| MFS18980 | Lara Aline | Inclusão de verificação dos Dados Iniciais na recuperação dos estabelecimentos. |
| MFS20732 | Lara Aline | Inclusão campo Período de Entrada das NFs. |
| MFS20930 | Lara Aline | Exclusão do evento R-2070 e ajuste no campo Comp. Sem Movto (MM/AAAA) – Conforme Layout 1.4 |
| MFS24006 | Eduardo Cruz | Permitir apenas a última versão (Layout 1.4) na geração |
| MFS-58345 | Alessandra Cristina Navatta | Reestruturação do Menu |
| MFS-63539 | Alessandra Cristina Navatta | Inclusão de data de validade para a versão 1.5.1 (ambiente produção) |
| MFS-64420 | Alessandra Cristina Navatta | Permitir apenas a última versão (Layout 1.5.1) na geração |
| MFS-67713 | Alessandra Cristina Navatta | Inclusão da geração do evento R-2055. A geração deste evento será feita de forma centralizada e não mais por estabelecimento como era realizada no e-social (evento S-1250) |
| MFS-79025 | Alessandra Cristina Navatta | Inclusão da versão 2.1 do REINF. |
| MFS-79885 | Alessandra Cristina Navatta | Inclusão do evento R-4010 para atendimento à versão 2.1 do REINF. |
| MFS-79893 | Alessandra Cristina Navatta | Inclusão do evento R-4040 para atendimento à versão 2.1 do REINF. |
| MFS-79907 | Alessandra Cristina Navatta | Inclusão do evento R-4080 para atendimento à versão 2.1 do REINF. |
| MFS-79914 | Alessandra Cristina Navatta | Inclusão do evento R-4099 para atendimento à versão 2.1 do REINF. |
| MFS-79890 | Alessandra Cristina Navatta | Inclusão do evento R-4020 para atendimento à versão 2.1 do REINF. |
| MFS-90863 | Alessandra Cristina Navatta | Alteração da versão 2.1 para 2.1.1 |
| MFS-91580 | Alessandra Cristina Navatta | Adequar a regra de multiempresa no componente Empresa/Estabelecimento, considerando os estabelecimentos descentralizados. (A implementação já estava exibindo esses estabelecimentos) |
| MFS- 96706 | Alessandra Cristina Navatta | Inclusão de data de validade para a geração da versão 2.1.1 |
| MFS-98390 | Alessandra Cristina Navatta | Retirar a trava de geração da versão 2.1.1. Não permitir a geração da versão 2.1.1 para o ambiente de produção. Adicionar validação no campo ‘Comp. Sem Movto (MM/AAAA)’, para que não fique habilitado se a versão for posterior a 1.5.1 e apresentar este campo abaixo do evento ‘R-2099 – Fechamento dos Eventos Periódicos – Sem Movimento’ |
| MFS-511449 | Alessandra Cristina Navatta | Exclusão da geração do evento R-4099, por ser dispensável o envio do evento sem movimento. |
| MFS-518835 | Alessandra Cristina Navatta | Ajustar a mensagem não permitindo a geração da versão 2.1.1 para o ambiente de produção para fatores geradores de marco/2023 para setembro/2023. |
| MFS-532750 | Alessandra Cristina Navatta | Inclusão da versão 2.1.2 do REINF. Não permitir a geração da versão 2.1.2 para o ambiente de produção. |
| MFS-532760 | Alessandra Cristina Navatta | Inclusão de regra para a geração centralizada do evento R-4010 |
| MFS-532761 | Alessandra Cristina Navatta | Inclusão de regra para a geração centralizada do evento R-4020 |
| MFS-550334 | Alessandra Cristina Navatta | Mensagem de bloqueio para a geração da versão 2.1.1.  Atenção: Excluir todos os registros existente na reinf_pger_apur (de versão 2.1.1), já que o governo excluiu essas informações do ambiente ao liberar o ambiente com a versão 2.1.2 (Este ponto, não está detalhado em regra. Foi sinalizado, para histórico das informações). |
| MFS-560534 | Alessandra Cristina Navatta | Não permitir a geração da versão 1.5.1 para o ambiente de produção restrita. |
| MFS-570803 | Alessandra Cristina Navatta | Permitir apenas a última versão (Layout 2.1.2) na geração |
| MFS-651982 | Alessandra Cristina Navatta | Permitir gerar os eventos R-4010 e R-4020 de origem de arquivos externos separadamente dos de origem SAFX53 |
| MFS- 777651 | Bruna Mariel Ribeiro | Alteração na geração dos movimentos criando uma opção de Retificação de todos os eventos do R-4010 e R-4020 para a SAFX53. |
| MFS-864330 | Alessandra Cristina Navatta | Para o produto TAXONE: Inserir a opção ‘Gerar Todos os Eventos’ no agrupamento ‘Eventos’, na tela de geração Prévia dos Movimentos. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Tipo de Execução | Radio Button | N | S | Default Selecionado: Imediata | Este Campo permite ao usuário programar a importação do arquivo de retorno. Programação que pode ser:  Imediata - Processo de importação realizado naquele exato momento.   Programada – Processo de importação automático programado para a data e hora desejada pelo usuário. | MFS-8958 |
| Data/Hora de Execução | Texto | N | S | Default: Desabilitado | Este campo permite ao usuário informar a data e hora desejada para importação do arquivo (Processo automático).  Campo será habilitado apenas quanto o campo Tipo de Execução na opção “Programada” for selecionado. | MFS-8958 |
| Executar | Botão | N | N |  | Quando acionado o sistema irá iniciar o processo de pré geração dos eventos.  Ao executar, se o estabelecimento estiver configurado em Dados Iniciais com o campo Tipo de Ambiente = Produção, a data da geração (sysdate) for inferior a 21/05/2021 e a versão igual a 1.5.1, não permitir a geração do arquivo e exibir a mensagem: “Em fatos geradores até 20/05/2021, não é permitido utilizar a versão 1.5.1, para o ambiente de produção”  Exclusão MFS-98390] [Alteração - MFS-96706] Ao executar, se a data da geração (sysdate) for inferior a 01/03/2023 e a versão igual a 2.11, não permitir a geração do arquivo e exibir a mensagem: “Em fatos geradores até 01/03/2023, não é permitido utilizar a versão 2.1.1. Refaça a geração com uma versão válida."  Exclusão MFS-550334  [Alteração MFS-518835] Ajuste da mensagem para fatos geradores a partir de setembro/2023 [Inclusão MFS-98390] Ao executar, se o estabelecimento estiver configurado em Dados Iniciais com o campo Tipo de Ambiente = Produção, a data da geração (sysdate) for inferior a 01/09/2023 e a versão igual a 2.1.1, não permitir a geração do arquivo e exibir a mensagem: “Em fatos geradores anteriores a 01/09/2023, não é permitido utilizar a versão 2.1.1, para o ambiente de produção. Refaça a geração com uma versão e ambiente válidos”.  [Alteração MFS- 550334] – Mensagem de bloqueio de geração na versão 2.1.1  Ao executar, não permitir a geração da versão 2.1.1 (independente do ambiente). E exibir a mensagem: “Neste momento, não será permitida a geração do REINF na versão 2.1.1. Estamos efetuando os ajustes para atendimento da versão 2.1.2, disponibilizada pelo FISCO em 10/07. Favor aguardar!”   [Alteração MFS-532750] Ajuste da mensagem para fatos geradores a partir de setembro/2023  Ao executar, se o estabelecimento estiver configurado em Dados Iniciais com o campo Tipo de Ambiente = Produção, a data da geração (sysdate) for inferior a 21/09/2023 e a versão igual a 2.1.2, não permitir a geração do arquivo e exibir a mensagem: “Em fatos geradores anteriores a 01/09/2023, não é permitido utilizar a versão 2.1.2, para o ambiente de produção. Refaça a geração com uma versão e ambiente válidos”.  Alteração MFS-560534] Bloquear a geração da versão 1.5.1 para o ambiente de produção restrita Ao executar, se o estabelecimento estiver configurado em Dados Iniciais com o campo Tipo de Ambiente = Produção Restrita, a data da geração (sysdate) for a partir de 22/08/2023 e a versão igual a 1.5.1, não permitir a geração do arquivo e exibir a mensagem: “A partir de 22/08/2023, não é permitido utilizar a versão 1.5.1, para o ambiente de produção restrita. Refaça a geração com a versão 2.1.2”. | MFS-8958 MFS-63539 MFS-96706 MFS-98390 MFS-518835 MFS-532750 MFS-550334 MFS-560534 |
| Período (MM/AAAA) | Texto | S | S | Formato: MM/AAAA | Caso não preenchido exibir a seguinte mensagem: “O campo Período deve ser informado”. | MFS-8958 |
| Versão | ComboBox | S | S |  | Nesse campo permite o usuário escolher qual versão de layout da EFD-REINF será gerada.  Permitir fazer geração apenas da versão 1.4  Lista Válida  1.5.1 1.4 2.1 2.1.1 2.1.2 | MFS-14462   MFS-24006  MFS-63539 MFS-64420 MFS-79025 MFS-90863 MFS-532750 MFS-570803 |
| Eventos | Eventos | Eventos | Eventos | Eventos | Eventos |  |
| Gerar Todos os Eventos | Check-box | N | S | Default: não selecionado | Este parâmetro deve ficar disponível apenas no produto TAXONE. Quando o parâmetro estiver marcado, todos os eventos do quadro Eventos ficarão desabilitados para seleção (não poderão ser clicados), mas ainda serão considerados na geração, com exceção do evento R-2099, que é independente deste parâmetro. Quando o parâmetro estiver desmarcado, todos os eventos voltarão a ficar habilitados e poderão ser selecionados individualmente. | MFS-864330 |
| Eventos | Checkbox | S | S | Default: Não selecionado | Serão listados os seguintes eventos:  R-2010 – Retenção Contribuição Previdenciária – Tomadores de Serviços  R-2020 – Retenção Contribuição Previdenciária – Prestadores de Serviços  [MFS11670]  R-2040 – Recursos Repassados para Associação Desportiva  R-2050 – Comercialização da Produção por Produtor Rural PJ/Agroindústria  R-2055 – Aquisição de Produção Rural  R-2060 – Contribuição Previdenciária Sobre a Receita Bruta – CPRB  R-2070 – Retenções na Fonte – IR, CSLL, Cofins, PIS/PASEP – Pagamentos Diversos   [ALTERAÇÃO MFS-79914] no tratamento do evento R-2099 [MFS17973] R-2099 – Fechamento dos Eventos Periódicos – Sem Movimento  Tratamento: Quando o usuário selecionar o evento R-2099 – Fechamento dos Eventos Periódicos – Sem Movimento, todos os outros eventos da família 2000, desse quadro ‘Eventos’ ficarão desabilitados e não selecionados.  [MFS-79885] R-4010 - Pagamentos/Créditos a Beneficiário Pessoa Física - SAFX53  [MFS-651982] R-4010 - Pagamentos/Créditos a Beneficiário Pessoa Física - Arquivos Externos   [MFS-79890] R-4020 - Pagamentos/Créditos a Beneficiário Pessoa Jurídica -SAFX53   [MFS-651982] R-4020 - Pagamentos/Créditos a Beneficiário Pessoa Jurídica - Arquivos Externos    [MFS-79893] R-4040 - Pagamentos/Créditos a Beneficiários não Identificados  [MFS-79907] R-4080 – Retenção no Recebimento  [Exclusão MFS-511449 ] [MFS79914] R-4099 – Fechamento/reabertura dos eventos da série R-4000  Tratamento: Quando o usuário selecionar o evento R-4099 – Fechamento/reabertura dos eventos da série R-4000, todos os outros eventos da família 4000 desse quadro ‘Eventos’ ficarão desabilitados e não selecionados.   Ao menos um evento deverá ser selecionado, caso contrário exibir a seguinte mensagem: “Ao menos um evento deve ser selecionado”. | MFS-8958 MFS17973 MFS20930 MFS-67713 MFS-79885 MFS-79893 MFS-79907 MFS-79914 MFS-79890 MFS-511449 MFS-651982] |
| Comp. Sem Movto (MM/AAAA) | Texto | N | S | Formato: MM/AAAA Default: Desabilitado | Apresentar este campo, embaixo do evento ‘R-2099 – Fechamento dos Eventos Periódicos – Sem Movimento’  Esse campo será habilitado apenas se o evento R-2099 – Fechamento dos Eventos Periódicos – Sem Movimento estiver selecionado E período informado de geração <= 10/2018 (Outubro de 2018) e até a versão 1.5.1. Nas versões posteriores a 1.5.1 não habilitar este campo   Caso o evento R-2099 – Fechamento dos Eventos Periódicos – Sem Movimento estiver selecionado esse campo será obrigatório, se não preenchido exibir a seguinte mensagem: “O campo Comp. Sem Movto deve ser informado”. | MFS17973 MFS20930 MFS-98390 |
| Desconsiderar NFs fora da Competência | Checkbox | N | S | Default: não selecionado | Quando selecionado pelo usuário, o sistema irá desconsiderar todas as notas fiscais que estiverem fora do período de competência para o evento R-2010, esse parâmetro será apenas considerado no evento R-2010.   Se selecionado, na geração a DATA_EMISSAO E DATA_SAIDA_REC deve compreender o período de geração do evento R-2010.   Se não selecionado, na geração a DATA_EMISSAO deve compreender o período de geração do evento R-2010, como o padrão. | MFS-15338 |
| Período de Entrada das NFs | Texto | N | S | Formato: DD/MM/AAAA a DD/MM/AAAA | Esse campo será habilitado apenas se o evento R-2010 – Retenção Contribuição Previdenciária - Serviços Tomados estiver selecionado.  A informação será formada de 2 campos para informar o período DE x ATÉ.  XX/XX/XXXX a XX/XX/XXXX  Caso o usuário preencher somente a data inicial a data final será obrigatória e caso não preenchida será apresentada a mensagem:  Data Final deve ser preenchida.  Caso a Data Inicial preenchida for menor que o Período de geração informado será apresentada a mensagem abaixo:  Data Inicial deve ser posterior ao período de geração.  Caso a Data Final preenchida for menor que a Data Inicial será apresentada a mensagem abaixo:  Data Inicial não deve ser maior que a Data Final.  Esse campo ficará habilitado APENAS se o campo ‘Desconsiderar NFs fora da Competência’ estiver desmarcado. | MFS20732 |
| Geração Multiempresa | Checkbox | N | S | Default: não selecionado | Quando selecionado pelo usuário, a geração será multiempresa.  Este campo interfere na montagem da lista dos estabelecimentos para seleção do usuário, conforme especificado no campo abaixo “Relação de Estabelecimentos”. | MFS-8958 |
| Geração por Estabelecimento | Checkbox | N | S | Default: não selecionado | Quando selecionado pelo usuário, a geração por Estabelecimento.  Este campo interfere na montagem da lista dos estabelecimentos para seleção do usuário, conforme especificado no campo abaixo “Relação de Estabelecimentos”. Na listagem de estabelecimentos devem ser demostrados os estabelecimentos vinculados ao centralizador parametrizado em Dados Iniciais | MFS-15740 |
| Retificação dos Eventos R-4010 e R-4020 | Checkbox | N | S | Default: não selecionado | Quando selecionado pelo usuário, a geração por Retificação dos Eventos R-4010 e R-4020 essa opção irá gerar os movimentos para retificar todos os eventos do R-4010 e R-4020. | MFS-777651 |
| Selecionar | Pasta de Seleção | N | S |  | Pasta padrão que permite seleção de um estabelecimento específico. | MFS-8958 |
| Marcar Todos | Checkbox | N | S | Default: não selecionado | Quando selecionado, deve mudar o status dos estabelecimentos para “selecionado”. | MFS-8958 |
| Empresa/Estabelecimento | Checkbox | S | S | Default: não selecionado | [MFS12178][MFS18980] Nesse campo deverá apresentar todos os estabelecimentos da empresa do login que possuam o cadastro dos Dados Iniciais preenchido e devido à inclusão do campo Geração Multiempresa, seguir a seguinte regra:  Se parâmetro “Geração Multiempresa” estiver marcado  Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento, mas neste caso serão demonstradas todas as empresas, sendo que, o código do estabelecimento deve ser precedido pela palavra “Centralizador” (todos os estabelecimentos centralizados de todas as empresas devem ser exibidos) e “Descentralizado” (todos os estabelecimentos descentralizados de todas as empresas devem ser exibidos):  XXX / Centralizador - XXX-XXXXXXXXXXXXXXXXX (cód. empresa + Centralizador + cód. e razão social do estabelecimento) e   XXX / Descentralizado - XXX-XXXXXXXXXXXXXXXXX (cód. empresa + Descentralizado + cód. e razão social do estabelecimento)    Se parâmetro “Geração Multiempresa” estiver desmarcado  Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento centralizador*, somente da empresa que acessou o módulo. XXX / Centralizador - XXX-XXXXXXXXXXXXXXXXX (cód. empresa + Centralizador + cód. e razão social do estabelecimento)   Caso algum estabelecimento não tenha sido associado a uma centralização, este será demonstrado na listagem de estabelecimentos precedido da palavra “Descentralizado”:  XXX / Descentralizado - XXX-XXXXXXXXXXXXXXXXX (cód. empresa + Descentralizado + cód. e razão social do estabelecimento)   Se parâmetro “Geração por Estabelecimento” estiver marcado  Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento vinculado ao centralizador.  Quando marcado, na listagem de estabelecimentos devem ser demostrados os estabelecimentos vinculados ao centralizador parametrizado em Dados Iniciais e o sistema deverá permitir a geração por estabelecimento.  XXX / XXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento)   Obs: No caso da geração multiempresa, as regras da geração do arquivo não se modificam. A diferença é apenas na chamada, já que na lista de estabelecimentos para geração do arquivo existirão estabelecimentos de empresas distintas.  * Entende-se Estabelecimento Centralizador aquele que foi aquele que foi cadastrado como tal na tela de “Centralização da Escrituração de Obrigações Federais”, no módulo Parâmetro / menu Preliminares. Caso não exista nenhum estabelecimento cadastrado como centralizador nesta tela para a empresa (ou empresas, no caso de geração multiempresa), serão demonstrados os estabelecimentos como descentralizados. Ao menos uma Empresa/Estabelecimento deverá ser selecionada, caso contrário exibir a seguinte mensagem: Ao menos uma Empresa/Estabelecimento deve ser selecionada.   [ALTERAÇÃO MFS-532760 e MFS-532761] Geração Centralizada – Evento R-4010 e R-4020  Se for feita a geração centralizada, para os eventos R-4010 e ou R-4020, o sistema deve considerar a movimentação de todos os estabelecimentos (centralizador e descentralizados) da empresa em questão, em um único arquivo e a informação do contribuinte deve conter apenas os dados do estabelecimento centralizador (independente do estabelecimento que ocorreu a movimentação).  A consolidação das informações será feita pelos campos chaves do evento. Já os campos que não compõem a chave, e que são campos de cadastros, serão considerados conforme cadastrados pelo estabelecimento centralizador. Os campos de valores devem ser somados.  Validações:  Uma vez efetuada a geração centralizada, não será permitida a geração dos estabelecimentos de forma “descentralizada” para o período em questão, pois ele já foi considerado na geração centralizada. Neste caso, se o usuário tentar gerar o arquivo (descentralizado) exibir a mensagem: “Já existe geração para os eventos R-4010 ou R-4020, de forma centralizada para este período de apuração <<cod estab- razão social>>. Por isso, não será permitido efetuar essa geração descentralizada. Caso necessário, deverá ser cancelada a geração anterior destes eventos, no painel de eventos, ou efetuar a exclusão, no caso do evento já ter sido enviado para o governo com sucesso e só então, processar as gerações de forma descentralizadas “   Uma vez efetuada a geração descentralizada, não será permitida a geração dos estabelecimentos de forma “centralizada” para o período em questão, pois ele já foi considerado na geração descentralizada. Neste caso, se o usuário tentar gerar o arquivo (centralizado) exibir a mensagem: “Já existe geração para os eventos R-4010 ou R-4020, de forma descentralizada para este período de apuração <<cod estab- razão social>>. Por isso, não será permitido efetuar essa geração centralizada. Caso necessário, deverá ser cancelada a geração anterior destes eventos, no painel de eventos, ou efetuar a exclusão, no caso do evento já ter sido enviado para o governo com sucesso e só então, processar as gerações de forma centralizadas “ | MFS-8958 MFS-12178 MFS-15740 MFS18980 MFS-91580 MFS-532760 MFS-532761 |
