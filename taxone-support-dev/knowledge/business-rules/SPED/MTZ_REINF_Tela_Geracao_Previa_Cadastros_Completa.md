# MTZ_REINF_Tela_Geracao_Previa_Cadastros_Completa

> Fonte: MTZ_REINF_Tela_Geracao_Previa_Cadastros_Completa.docx






THOMSON REUTERS

Geração Prévia dos Cadastros
SPED – Reinf



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3

## Regras dos Campos


Localização da tela: Módulo: SPED >> EFD – Reinf
Menu: REINF >> Geração Prévia >> Cadastros

Título da tela: Geração Prévia dos Cadastros (Completa)





| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS10757 | EFD- Reinf | Inclusão da Tela de Geração Prévia dos Cadastros (Completa) do EFD – Reinf |
| MFS12178 | Lara Aline | Inclusão de verificação das informações do contribuinte na recuperação dos estabelecimentos. |
| MFS14462 | Lara Aline | Inclusão do campo Versão. |
| MFS18980 | Lara Aline | Inclusão de verificação dos Dados Iniciais na recuperação dos estabelecimentos. |
| MFS24006 | Eduardo Cruz | Permitir apenas a última versão (Layout 1.4) na geração |
| MFS-58345 | Alessandra Cristina Navatta | Reestruturação do Menu |
| MFS-63539 | Alessandra Cristina Navatta | Inclusão de data de validade para a versão 1.5.1 (ambiente produção) |
| MFS-64420 | Alessandra Cristina Navatta | Permitir apenas a última versão (Layout 1.5.1) na geração |
| MFS-79025 | Alessandra Cristina Navatta | Inclusão da versão 2.1 do REINF |
| MFS-79881 | Alessandra Cristina Navatta | Inclusão das Informações do Evento R-1050, atendendo o layout Versão 2.1 |
| MFS-90863 | Alessandra Cristina Navatta | Alteração da versão 2.1 para 2.1.1 |
| MFS-91580 | Alessandra Cristina Navatta | Adequar a regra de multiempresa no componente Empresa/Estabelecimento, considerando os estabelecimentos descentralizados. (A implementação já estava exibindo esses estabelecimentos) |
| MFS-96706 | Alessandra Cristina Navatta | Inclusão de data de validade para a geração da versão 2.1.1 |
| MFS-98390 | Alessandra Cristina Navatta | Retirar a trava de geração da versão 2.1.1. Não permitir a geração da versão 2.1.1 para o ambiente de produção. |
| MFS-518835 | Alessandra Cristina Navatta | Ajustar a mensagem não permitindo a geração da versão 2.1.1 para o ambiente de produção para fatores geradores de março/2023 para setembro/2023. |
| MFS-532750 | Alessandra Cristina Navatta | Inclusão da versão 2.1.2 do REINF.  Não há regras a serem ajustadas neste documento. |
| MFS-550334 | Alessandra Cristina Navatta | Mensagem de bloqueio para a geração da versão 2.1.1.  Atenção: Excluir todos os registros existente na reinf_pger_apur (de versão 2.1.1), já que o governo excluiu essas informações do ambiente ao liberar o ambiente com a versão 2.1.2 (Este ponto, não está detalhado em regra. Foi sinalizado, para histórico das informações). |
| MFS-560534 | Alessandra Cristina Navatta | Não permitir a geração da versão 1.5.1 para o ambiente de produção restrita. |
| MFS-570803 | Alessandra Cristina Navatta | Permitir apenas a última versão (Layout 2.1.2) na geração |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Tipo de Execução | Radio Button | N | S | Default Selecionado: Imediata | Este Campo permite ao usuário programar a importação do arquivo de retorno. Programação que pode ser:  Imediata - Processo de importação realizado naquele exato momento.   Programada – Processo de importação automático programado para a data e hora desejada pelo usuário. | MFS-10757 |
| Data/Hora de Execução | Texto | N | S | Default: Desabilitado | Este campo permite ao usuário informar a data e hora desejada para importação do arquivo (Processo automático).  Campo será habilitado apenas quanto o campo Tipo de Execução na opção “Programada” for selecionado. | MFS-10757 |
| Executar | Botão | N | N |  | Quando acionado o sistema irá iniciar o processo de pré geração dos eventos.  Ao executar, se o estabelecimento estiver configurado em Dados Iniciais com o campo Tipo de Ambiente = Produção, a data da geração (sysdate) for inferior a 21/05/2021 e a versão igual a 1.5.1, não permitir a geração do arquivo e exibir a mensagem: “Em fatos geradores até 20/05/2021, não é permitido utilizar a versão 1.5.1, para o ambiente de produção”  [Exclusão MFS-98390] [Alteração - MFS-96706] Ao executar, se a data da geração (sysdate) for inferior a 01/03/2023 e a versão igual a 2.11, não permitir a geração do arquivo e exibir a mensagem: “Em fatos geradores até 01/03/2023, não é permitido utilizar a versão 2.1.1. Refaça a geração com uma versão válida."  [Exclusão MFS-550334  [Alteração MFS 518835] Ajuste da mensagem para fatos geradores a partir de setembro/2023 [Inclusão MFS-98390] Ao executar, se o estabelecimento estiver configurado em Dados Iniciais com o campo Tipo de Ambiente = Produção, a data da geração (sysdate) for inferior a 01/09/2023 e a versão igual a 2.1.1, não permitir a geração do arquivo e exibir a mensagem: “Em fatos geradores anteriores a 01/09/2023, não é permitido utilizar a versão 2.1.1, para o ambiente de produção. Refaça a geração com uma versão e ambiente válidos”.  [Alteração MFS- 550334] – Mensagem de bloqueio de geração na versão 2.1.1  Ao executar, não permitir a geração da versão 2.1.1 (independente do ambiente). E exibir a mensagem: “Neste momento, não será permitida a geração do REINF na versão 2.1.1. Estamos efetuando os ajustes para atendimento da versão 2.1.2, disponibilizada pelo FISCO em 10/07. Favor aguardar!”  [Alteração MFS-532750] Ajuste da mensagem para fatos geradores a partir de setembro/2023  Ao executar, se o estabelecimento estiver configurado em Dados Iniciais com o campo Tipo de Ambiente = Produção, a data da geração (sysdate) for inferior a 21/09/2023 e a versão igual a 2.1.2, não permitir a geração do arquivo e exibir a mensagem: “Em fatos geradores anteriores a 01/09/2023, não é permitido utilizar a versão 2.1.2, para o ambiente de produção. Refaça a geração com uma versão e ambiente válidos”.  Alteração MFS-560534] Bloquear a geração da versão 1.5.1 para o ambiente de produção restrita Ao executar, se o estabelecimento estiver configurado em Dados Iniciais com o campo Tipo de Ambiente = Produção Restrita, a data da geração (sysdate) for a partir de 22/08/2023 e a versão igual a 1.5.1, não permitir a geração do arquivo e exibir a mensagem: “A partir de 22/08/2023, não é permitido utilizar a versão 1.5.1, para o ambiente de produção restrita. Refaça a geração com a versão 2.1.2”. | MFS-10757 MFS-63539 MFS-96706 MFS-98390 MFS-518835 MFS-532750 MFS-550334 MFS-560534 |
| Período Inicial | Data | S | S | Formato: MM/AAAA | Caso não preenchido exibir a seguinte mensagem: “Informe Período Inicial”. | MFS-10757 |
| Período Final | Data | N | S | Formato: MM/AAAA | Caso não preenchido exibir a seguinte mensagem: “Informe Período Final”. | MFS-10757 |
| Versão | ComboBox | S | S |  | Nesse campo permite o usuário escolher qual versão de layout da EFD-REINF será gerada.  Lista Valida:  1.5.1 1.4 [ALTERAÇÃO MFS-79025] 2.1  [ALTERAÇÃO MFS-90863] 2.1.1 [ALTERAÇÃO MFS-532750] 2.1.2   Tratamento: Caso já tenha sido gerado um cadastro R-1000, R-1050 ou R-1070 para uma versão. No momento que o usuário tentar gerar para outra versão e estiver com situação igual à “Evento REINF Recebido com sucesso ou advertência” não deverá permitir e será exibida uma mensagem no log:  ‘Esse evento já foi gerado, enviado e recebido pelo fisco na versão ‘XX’. Para R-1070: Caso já tenha sido gerado um cadastro R-1070 para uma versão. No momento que o usuário tentar gerar para outra versão e estiver com situação igual à “Enviando para Mensageria” ou “Em Processamento” não deverá permitir e será exibida uma mensagem no log:  ‘Esse evento já foi gerado, enviado para fisco na versão ‘XX’.  Permitir fazer geração apenas da versão 1.4 | MFS-14462 MFS-63539 MFS-64420 MFS-79025 MFS-79881 MFS-90863 MFS-532750 MFS-570803                                 MFS24006 |
| Eventos | Checkbox | S | S | Default: Não selecionado | Serão listados os seguintes eventos:  R-1000 – Informações do Contribuinte R-1050 – Tabela de Entidades Ligadas R-1070 – Processos Administrativos/Judiciais   Ao menos um evento deverá ser selecionado, caso contrário exibir a seguinte mensagem: “Ao menos um evento deve ser selecionado”. | MFS-10757 MFS-79881 |
| Geração Multiempresa | Checkbox | N | S | Default: Não selecionado | Quando selecionado pelo usuário, a geração será multiempresa.  Este campo interfere na montagem da lista dos estabelecimentos para seleção do usuário, conforme especificado no campo abaixo “Empresa/ Estabelecimento”. | MFS-10757 |
| Selecionar | Pasta de Seleção | N | S |  | Pasta padrão que permite seleção de um estabelecimento específico. | MFS-10757 |
| Marcar Todos | Checkbox | N | S | Default: não selecionado | Quando selecionado, deve mudar o status dos estabelecimentos para “selecionado”. | MFS-10757 |
| Empresa/Estabelecimento | Checkbox | S | S | Default: não selecionado | [MFS12178][MFS18980] Nesse campo deverá apresentar todos os estabelecimentos da empresa do login que possuam o cadastro dos Dados Iniciais preenchido e devido à inclusão do campo Geração Multiempresa, seguir a seguinte regra:  Se parâmetro “Geração Multiempresa” estiver marcado  Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento, mas neste caso serão demonstradas todas as empresas, sendo que, o código do estabelecimento deve ser precedido pela palavra “Centralizador” (todos os estabelecimentos centralizados de todas as empresas devem ser exibidos) e “Descentralizado” (todos os estabelecimentos descentralizados de todas as empresas devem ser exibidos):  XXX / Centralizador - XXX-XXXXXXXXXXXXXXXXX (cód. empresa + Centralizador + cód. e razão social do estabelecimento) e   XXX / Descentralizado - XXX-XXXXXXXXXXXXXXXXX (cód. empresa + Descentralizado + cód. e razão social do estabelecimento)   Se parâmetro “Geração Multiempresa” estiver desmarcado  Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento centralizador*, somente da empresa que acessou o módulo. XXX / Centralizador - XXX-XXXXXXXXXXXXXXXXX (cód. empresa + Centralizador + cód. e razão social do estabelecimento)  Caso algum estabelecimento não tenha sido associado a uma centralização, este será demonstrado na listagem de estabelecimentos precedido da palavra “Descentralizado”:  XXX / Descentralizado - XXX-XXXXXXXXXXXXXXXXX (cód. empresa + Descentralizado + cód. e razão social do estabelecimento)   Obs: No caso da geração multiempresa, as regras da geração do arquivo não se modificam. A diferença é apenas na chamada, já que na lista de estabelecimentos para geração do arquivo existirão estabelecimentos de empresas distintas.  * Entende-se Estabelecimento Centralizador aquele que foi cadastrado como tal na tela de “Centralização da Escrituração de Obrigações Federais”, no módulo Parâmetro / menu Preliminares. Caso não exista nenhum estabelecimento cadastrado como centralizador nesta tela para a empresa (ou empresas, no caso de geração multiempresa), serão demonstrados os estabelecimentos como descentralizados.  Ao menos uma Empresa/Estabelecimento deverá ser selecionada, caso contrário exibir a seguinte mensagem: Ao menos uma Empresa/Estabelecimento deve ser selecionada. | MFS-10757 MFS-12178 MFS18980 |
