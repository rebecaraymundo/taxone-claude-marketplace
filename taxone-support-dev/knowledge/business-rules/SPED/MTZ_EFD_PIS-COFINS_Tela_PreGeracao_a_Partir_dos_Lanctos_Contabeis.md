# MTZ_EFD PIS-COFINS_Tela_PreGeracao_a_Partir_dos_Lanctos_Contabeis

> Fonte: MTZ_EFD PIS-COFINS_Tela_PreGeracao_a_Partir_dos_Lanctos_Contabeis.docx






THOMSON REUTERS

Tela Pré-Geração a Partir dos Lanctos Contábeis

Módulo Sped Contribuições


Localização: Menu Sped, Módulo: EFD Escrituração Fiscal Digital das Contribuições  Manutenção Registro do Bloco F  Demais Documentos e Operações Geradoras de Contribuição e Créditos (F100) Pré-Geração a Partir dos Lantos Contábeis




DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	3
2.	Layout da Tela	3
2.1.	Abas que podem ser geradas:	8


























## Regras Gerais


Ao gerar este processo, serão consideradas as informações existentes na base, considerando os lançamentos contábeis (tabela X01 – Arquivo Contábil), que estão compreendidos no período indicado na tela de pré-geração, além de levar em consideração a parametrização da ‘Conta Contábil X Centro de Custo/CST/Operação/Nat. Base de Crédito’ (existentes em Parâmetros > Registro F100, do módulo EFD-Escrituração Fiscal Digital das Contribuições), conforme pré-definido em Dados Iniciais,  para gravarmos as informações na tabela x147_oper_cred.

## Layout da Tela





Campos de preenchimento obrigatório: Período, Estabelecimento ou Empresa (esse último, se o campo Geração Multiempresa estiver selecionado). Caso um desses campos não esteja preenchidos, verificar a mensagem a ser exibida, nas regras abaixo:


#### Abas que podem ser geradas:




| MFS | Descrição | Nome | Data |
| --- | --- | --- | --- |
| MFS-64743 | Criação da tela ‘Pré-Geração a Partir dos Lanctos Contábeis’ para criamos um processo que a partir dos lançamentos contábeis existente na base e a parametrização definida para a geração do registro F100 do SPED Contribuições (em dados iniciais do módulo), grava as informações na x147_oper_cred. | Alessandra Cristina Navatta | 18/05/2021 |


| .Campo | Regra | Demanda |
| --- | --- | --- |
| Geração Multiempresa | Default do Campo: Desmarcado Quando desmarcado, serão apresentados os estabelecimentos que o usuário tem acesso, da empresa que está logada, na grid Empresa/Estabelecimento. Quando marcado, serão apresentadas as empresas que o usuário tem acesso, na grid Empresa/Estabelecimento. | MFS-64743 |
| Grid Empresa/Estabelecimento | Exibir todos os estabelecimentos ou empresa, que o usuário tem acesso, conforme regra do campo Geração Multiempresa. | MFS-64743 |
| Selecionar | Permite que o usuário selecione um ou mais Empresa/Estabelecimento que serão considerados no processamento:  Tratamentos:  Modal 'Selecionar Empresa/Estabelecimento‘ Ao ser acionado abrir o Modal 'Selecionar Empresa/Estabelecimento‘. Apresentando os campos Cód. Estab e Descrição Botões do Modal 'Selecionar Empresa/Estabelecimento': Critério, Cancelar, OK e Salvar...   Botões Critério, Cancelar, OK e Salvar  - Ao selecionar o botão 'Cancelar', nada será feito e o Modal 'Selecionar Empresa/Estabelecimento‘ será fechado.  - Ao selecionar o botão 'Critério', os estabelecimentos poderão ser filtrados e no novo modal serão exibidos habilitado os botões Pesquisar e Cancelar.  -Ao confirmar a seleção dos registros, acionando o botão ‘OK’, apresentar as empresas/estabelecimentos no componente “Empresa/Estabelecimento” da tela Principal - Permite a seleção de vários registros por vez. - Ao entrar no modal, pelo menos um registro deve ser selecionado, se for selecionado o botão 'Ok', caso contrário, exibir a mensagem “Selecionar pelo menos um registro”. -Ao selecionar o botão ’Salvar’, o sistema salva as informações recuperadas das empresas/estabelecimentos (no diretório local e formato que o usuário informar). | MFS-64743 |
| Marcar Todos | Permite ao usuário selecionar ou desmarcar todos os registros da grid Empresa / Estabelecimento. | MFS-64743 |
| Executar | Mensagens que bloqueiam a geração do processo:  Ao acionar este campo, verificar se na tela:  Campo Período está preenchido. Caso não esteja preenchido exibir a mensagem: Informe o Período. Empresa/estabelecimento deve estar preenchido. Caso nenhum registro esteja marcado na grid Empresa/Estabelecimento, exibir a mensagem: “Informe pelo menos uma Empresa/Estabelecimento”.  Ao acionar este campo, verificar as seguintes situações e se necessário exibir a mensagem na aba de Logs:  Se o parâmetro ‘Registro F100 – Demais Documentos e Operações Geradoras de Contribuição e Crédito’ em Dados Iniciais estiver marcado com: ‘Utilizar a parametrização do Tipo de Documento X CST/Operação/Nat. Base de Crédito’, exibir a mensagem: “O processo não foi executado, pois o parâmetro ‘Registro F100 – Demais Documentos e Operações Geradoras de Contribuição e Crédito’ em Dados Iniciais, não está marcado com  Conta Contábil X Centro de Custo/CST/Operação/Nat. Base de Crédito’.  Se não há dados no período a ser processado (Lançamentos contábeis no período indicado em tela, para empresa/estabelecimento), exibir a mensagem: “O processo não foi executado, pois não foi encontrado dados na base para o período”.  Se não for encontrado nenhuma parametrização na base por ‘Conta Contábil X Centro de Custo/CST/Operação/Nat. Base de Crédito’ (de acordo com o que foi pré-definido em Dados Iniciais), exibir a mensagem: “O processo não foi executado, pois não foi encontrado parametrização por ‘Conta Contábil X Centro de Custo/CST/Operação/Nat. Base de Crédito’, para a geração do Registro F100 – Demais Documentos e Operações Geradoras de Contribuição e Crédito. (Parâmetros > Registro F100, do módulo EFD-Escrituração Fiscal Digital das Contribuições).  Se existir lançamentos contábeis no período indicado em tela e existir parametrização na base, porém, nenhuma parametrização atender a pelo menos um lançamento contábil, exibir a mensagem: “O processo não foi executado, pois não foi possível enquadrar ao menos um lançamento contábil com as parametrizações existentes. Reveja a as parametrizações em Parâmetros > Registro F100 > Conta Contábil X Centro de Custo/CST/Operação/Nat. Base de Crédito’, do módulo EFD-Escrituração Fiscal Digital das Contribuições ”.  Regras do Processo:  Considerar as regras existentes no documento “MTZ_EFD PIS-COFINS_Processo_PreGeracao_a_Partir_dos_Lanctos_Contabeis.docx” | MFS-64743 |


| Processos | Esta aba será gerada sempre que for criado um processo. Deve conter o número do processo, os parâmetros, a situação do processo, as datas Início Execução e Fim Execução, além da informação do Usuário que fez a execução do processo. | MFS-64743 |
| --- | --- | --- |
| Logs | Esta aba deve demonstrar os logs do processo.   Na parte superior da tela exibir os parâmetros que foram indicados na tela de geração, seguindo o formato abaixo: | MFS-64743 |
