# MTZ_EFD_Tela_Pre_Geracao_Ressarcimento_ICMSST_MG_Calculo_ICMS_ST

> Fonte: MTZ_EFD_Tela_Pre_Geracao_Ressarcimento_ICMSST_MG_Calculo_ICMS_ST.docx







THOMSON REUTERS

Módulo Sped Fiscal

Tela Cálculo ICMS-ST


Localização: Menu Sped, Módulo: Escrituração Fiscal Digital à Pré-Geraçãoà Ressarcimento ICMS-ST (Específico MG)




DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	2
2.1.	Abas que podem ser geradas:	7




## Regras Gerais


Ao gerar este processo, serão calculadas as informações de ICMS-ST considerando as notas de saída, entrada e inventários dos produtos parametrizações sujeitas ao ICMS-ST. Essas informações serão gravadas na tabela x296_info_compl_st_itens_merc (utilizada para a geração dos registros C180, C185), x299_inf_comp_st_res_mod_02 (utilizada para a geração dos registros C330), x302_inf_comp_st_res_it_ecf (utilizada para a geração dos registros C430) e x304_saldo_cons_res_comp_icms (para a geração dos registros 1250,1255). Além disso, também será possível atualizar os campos 21-VLR_ICMS_MEDIO, 22-VLR_ICMSS_MEDIO, 43-VLR_BASE_ICMSS_MEDIO e 44-VLR_FCP_MEDIO da tabela de inventário x52_invent_produto (que serão considerados para a geração do H030). Atualmente este processo será realizado apenas para a UF de Minas Gerais.

## Layout da Tela
















Campos de preenchimento obrigatório: Período, Pesquisar Notas de Entrada até, pelo menos um tipo de registro e Estabelecimentos. Caso um desses campos não esteja preenchidos, verificar a mensagem a ser exibida, nas regras abaixo.




#### Abas que podem ser geradas:




| MFS | Descrição | Nome | Data |
| --- | --- | --- | --- |
| MFS-33977 | Criação da tela do processamento de cálculo das informações de ICMS-ST para a geração dos registros C180/C185 da EFD. | Alessandra Cristina Navatta | 13/03/2020 |
| MFS-35337 | Liberação da opção do registro C330 na tela. | Alessandra Cristina Navatta | 25/03/2020 |
| MFS-35339 | Liberação da opção do registro C430 na tela. | Alessandra Cristina Navatta | 03/04/2020 |
| MFS-35340 | Liberação da opção dos registros 1250/1255 na tela. | Alessandra Cristina Navatta | 07/04/2020 |
| MFS-36146 | Inclusão da opção do registro H030 na tela. | Alessandra Cristina Navatta | 17/04/2020 |
| MFS-39378 | Incluir campo ‘Pesquisar Notas de Entrada até” | Alessandra Cristina Navatta | 26/06/2020 |
| MFS-62563 | Inclusão do C181 | Liliane Assaf | 09/06/2021 |
| MFS-64570 | Inclusão do C186 | Liliane Assaf | 18/06/2021 |
| MFS67658 | Inclusão do C195/C197 | Liliane Assaf | 27/07/2021 |
| MFS-58456 | Inclusão do parâmetro “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS-ST nos itens (SAFX08)” na Tela de Geração e tratamento na geração dos registros C180, C186 e Cálculo da Média Ponderada do Produto no Período. | Liliane Assaf | 03/09/2021 |
| MFS74069 | Inclusão de um parâmetro para indicar se deve ser gerado o log de erro de produto sem inventário somente para produtos com movimentação. | Andréa Rocha | 29/10/2021 |
| MFS74991 | Inclusão de um parâmetro para indicar se deve ser gerado o registro de inventário (SAFX52), para os produtos que tem movimentação no mês e não tem saldo de inventário do mês anterior. E inclusão do campo natureza de estoque que será usado para gerar um registro na SAFX52. | Andréa Rocha | 17/11/2021 |
| MFS74991 | Inclusão de um parâmetro para indicar se deve ser gerado o registro de inventário (SAFX52), para os produtos que tem movimentação no mês e não tem saldo de inventário do mês anterior. E inclusão do campo natureza de estoque que será usado para gerar um registro na SAFX52. | Andréa Rocha | 17/11/2021 |
| MFS86641 | Inclusão do campo conta contábil que será usado para gerar um registro na SAFX52. | Andréa Rocha | 03/06/2022 |
| MFS90139 | Retirar o vínculo do parâmetro do log de erro de produto sem inventário com o parâmetro de gerar o registro de inventário | Andréa Rocha | 30/08/2022 |
| MFS511653 | Criação check-box “Gerar Relatórios de Conferência” na tela da pré-geração. | Liliane Assaf | 07/03/2023 |
| MFS591080 | Tratamento das Incorporações de Empresas/Estabelecimentos: inclusão do parâmetro em tela “Considerar as notas fiscais da empresa incorporada”. | Liliane Assaf | 06/12/2023 |
| MFS977849 | Inclusão do parâmetro “Vlrs de FECEP estão embutidos nos vlrs de ICMS-ST não destacado/não escriturado” na Tela de Geração e tratamento na geração dos registros C180, C186 e Cálculo da Média Ponderada do Produto no Período. | Andréa Rocha | 18/11/2025 |


| Campo | Regra | Demanda |
| --- | --- | --- |
| Pesquisar Notas de Entrada até | Iremos recuperar notas de entrada para calcular os registros de inventário (H030) e ou o cálculo dos valores médios do inventário para o cálculo dos registros de saída (C185, C330 e ou C430), até o limite desta data. | MFS-39378 |
| UF | Mostrar este campo desabilitado e preenchido com a UF = MG | MFS-33977 |
| Utilizar somente DATA MART p/ períodos anteriores | Através deste campo o usuário pode optar como será feita a recuperação dos dados de notas de períodos anteriores, nos casos em que este procedimento for necessário. Maiores detalhes, verificar regra RP02 (item *** Recuperação de notas de Período anterior) do arquivo ‘MTZ-EFD_Processamento_Ressarcimento_ICMSST_MG_Calculo_ICMS_ST.docx’.   Por default, ele estará habilitado e marcado | MFS-33977 |
| Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS-ST nos itens (SAFX08) | Check-box, com default habilitado e desmarcado. Através desse campo o usuário indica se o valor do Fecep vem escriturado na nota fiscal embutido aos valores de ICMS e ICMS-ST (campos 43 e 53 da SAFX08 já contém o valor do Fecep). Essa orientação é importante pois, na geração dos registros C180 e C186, o valor do ICMS-ST deve ser demonstrado com o FECEP incluído. Se este já vier embutido no valor do ICMS-ST, o FECEP não pode ser somado para não gerar duplicidade. | MFS-58456 |
| Vlrs de FECEP estão embutidos nos vlrs de ICMS-ST não destacado/não escriturado | Check-box, com default habilitado e desmarcado. Através desse campo o usuário indica se o valor do Fecep vem escriturado na nota fiscal embutido aos valores de ICMS-ST não destacado/não escriturado. Essa orientação é importante pois, na geração dos registros C180 e C186, o valor do ICMS-ST deve ser demonstrado com o FECEP incluído. Se este já vier embutido no valor do ICMS-ST, o FECEP não pode ser somado para não gerar duplicidade. | MFS-977849 |
| Gerar Relatórios de Conferência | Esta opção, quando selecionada, disponibiliza os relatórios de Conferência dos registros em arquivos formato Excel.  Por default, esse campo estará habilitado e marcado. Os seguintes relatórios são gerados: - Relatório de Conferência do Cálculo da Média Ponderada; - Relatório de Conferência do Cálculo da Média do Inventário; [MFS511653] - Relatório de Conferência do Registro C181; - Relatório de Conferência do Registro C185; [MFS511653] - Relatório de Conferência do Registro C186; - Relatório de Conferência do Registro C195; - Relatório de Conferência do Registro C197; - Relatório de Conferência do Lançamento no P9-ST; | MFS511653 |
| Registro a ser Calculado | Lista de valores:  C180 - Entrada de mercadorias sujeitas à substituição tributária (01, 1B, 04, 55 e 65) C181 – Devoluções de Saídas de mercadorias sujeitas à substituição tributária (01, 1B, 04, 55 e 65) C185 - Saída de mercadorias sujeitas à substituição tributária (01, 1B, 04, 55 e 65) C186 – Devoluções de Entradas de mercadorias sujeitas à substituição tributária (01, 1B, 04, 55 e 65) C195/C197 – Observação/Ajuste e Lançamento Complementar na Apuração ICMS-ST C330 - Saída de mercadorias sujeitas à substituição tributária (02) C430 - Saída de mercadorias sujeitas à substituição tributária (02, 02D e 60) 1250/1255 - Saldos de restituição, ressarcimento e complementação do ICMS H030 - Inventário das mercadorias sujeitas ao regime de substituição tributária | MFS-33977 MFS-35338 MFS-35339 MFS-35340 MFS-36146 MFS-62563 MFS-64570 MF-S67658 |
| Sobrepor os valores calculados na tabela de inventário (Registro H030) | Este campo só deve ser habilitado se a opção do registro ‘H030 - Informações complementares do inventário das mercadorias sujeitas ao regime de substituição tributária’, for selecionado.  Por default, ele estará desabilitado e desmarcado.  Se marcada a opção, o processo atualizará as informações que forem calculadas no registro de inventário recuperado, ou seja, se já existir informações nos campos calculados pelo processo, as mesmas serão sobrepostas. Caso desmarcada, o processo só irá recuperar registros de inventário que tenham os campos 21-VLR_ICMS_MEDIO, 22-VLR_ICMSS_MEDIO, 43-VLR_BASE_ICMSS_MEDIO e 44-VLR_FCP_MEDIO sem preenchimento ou igual a zero, para atualizar os valores dos mesmos (após serem calculados pelo sistema). | MFS-36146 |
| Gerar registro de inventário p/ produtos c/ movimento e sem inventário | Check-box, com default habilitado e desmarcado.  Através desse campo o usuário indica se devem ser gerados os registros de inventário na SAFX52, para os produtos que não tem inventário e tem movimentação de notas no período da geração. | MFS-74991 |
| Considerar as notas fiscais da empresa incorporada | Check-box, com default habilitado e desmarcado. Este campo é um checkbox onde o usuário informa se vai considerar as notas fiscais de entrada da empresa incorporada, além das notas fiscais da empresa/estabelecimento da geração. | MFS591080 |
| Grupo | Campo do tipo Listbox.  Este campo somente deve ficar habilitado se o parâmetro “Gerar registro de inventário p/ produtos c/ movimento e sem inventário”  estiver marcado.  Demonstrar os grupos da parametrização de “Relação entre Tabelas e Grupos” (vide módulo Parâmetros) para a empresa selecionada. | MFS-74991 |
| Natureza de Estoque | Campo do tipo Listbox.  Este campo somente deve ficar habilitado se o parâmetro “Gerar registro de inventário p/ produtos c/ movimento e sem inventário”  estiver marcado.  Campo para informar a Natureza de Estoque de acordo com a Tabela de Natureza de Estoque (SAFX2010).  Para selecionar uma natureza, o usuário deverá clicar na pastinha de pesquisa, onde será aberta uma janela de pesquisa da Tabela de Natureza de Estoque. Serão disponibilizados para seleção apenas os códigos de natureza do Grupo já selecionado. | MFS-74991 |
| Conta Contábil | Campo do tipo pastinha.  Este campo somente deve ficar habilitado se o parâmetro “Gerar registro de inventário p/ produtos c/ movimento e sem inventário”  estiver marcado.  Campo para informar a Conta Contábil de acordo com a Tabela de Plano de Contas (SAFX2002).  Para selecionar uma conta, o usuário deverá clicar na pastinha de pesquisa, onde será aberta uma janela de pesquisa da Tabela de Plano de Contas. Serão disponibilizados para seleção apenas os códigos de conta do Grupo já selecionado.  Campo não obrigatório. | MFS-86641 |
| Somente mostrar log de produto sem inventário p/ produtos c/ movimento | [MFS-90139] Retirar o vínculo entre os dois parâmetros, pois podem existir produtos parametrizados para o ressarcimento e sem movimentação no mês de geração  Check-box, com default habilitado e desmarcado.   Através desse campo o usuário indica se deve ser gerado o log de erro de produto sem inventário somente para produtos com movimentação de notas no período da geração. | MFS-74069 MFS-74991 MFS-90139 |
| Grid Estabelecimentos | Exibir todos os estabelecimentos da empresa selecionada no menu, que o usuário tenha acesso e que seja da UF = MG.  [MFS74991] Caso o usuário tenha optado por selecionar uma natureza de estoque, serão considerados apenas os estabelecimentos associados ao Grupo informado no campo Grupo. | MFS-33977 MFS-74991 |
| Selecionar | Permite que o usuário selecione os Estabelecimentos que serão gerados os cálculos:  Tratamentos:  Modal 'Selecionar Estabelecimentos‘ Ao ser acionado abrir o Modal 'Selecionar Estabelecimentos‘. Apresentando os campos Cód. Estab e Descrição Botões do Modal 'Selecionar Estabelecimentos': Critério, Cancelar, OK e Salvar...   Botões Critério, Cancelar, OK e Salvar  - Ao selecionar o botão 'Cancelar', nada será feito e o Modal 'Selecionar Estabelecimentos‘ será fechado.  - Ao selecionar o botão 'Critério', os estabelecimentos poderão ser filtrados e no novo modal serão exibidos habilitado os botões Pesquisar e Cancelar.  -Ao confirmar a seleção dos registros, acionando o botão ‘OK’, apresentar os estabelecimentos no componente “Estabelecimentos” da tela Principal - Permite a seleção de vários registros por vez. - Ao entrar no modal, pelo menos um registro deve ser selecionado, se for selecionado o botão 'Ok', caso contrário, exibir a mensagem “Selecionar pelo menos um registro”. -Ao selecionar o botão ’Salvar’, o sistema salva as informações recuperadas dos estabelecimentos (no diretório local e formato que o usuário informar). | MFS-33977 |
| Marcar Todos | Permite ao usuário selecionar ou desmarcar todos os registros da grid Estabelecimentos. | MFS-33977 |
| Executar | Mensagens que bloqueiam a geração do processo:  Ao acionar este campo, verificar se na tela:  Campo Período está preenchido. Caso não esteja preenchido exibir a mensagem: Informe o Período. Campo Pesquisar Notas de Entrada até. Caso não esteja preenchido exibir a mensagem: Informe Pesquisar Notas de Entrada até. Deve ser marcada pelo menos um estabelecimento. Caso contrário, exibir a mensagem “Selecione pelo menos um Estabelecimento”. A data indicada no campo ‘Pesquisar Notas de Entrada até’ deve ser menor que o mês indicado no campo Período. Caso seja igual ou maior, exibir a mensagem: “A data limite para Pesquisar Notas de Entrada deve ser anterior ao período a ser calculado”.   Ao acionar este campo, verificar e se necessário exibir a mensagem na aba de Logs: Deve ser marcado pelo menos um registro a ser calculado. Caso contrário, exibir a mensagem “Selecione pelo menos um Registro a ser Calculado”  Se não há dados no período a ser processo (Saldo Inicial, Notas de entrada (no mês atual e no mês anterior), notas de saída no mês), exibir a mensagem: “O processo não foi executado, pois não foi encontrado dados na base para o período”    Regras do Processo:  Considerar as regras existentes no documento “MTZ-EFD_Processamento_Ressarcimento_ICMS_ST_MG_Calculo.docx” | MFS-33977 MFS-39378 |


| Processos | Esta aba será gerada sempre que for criado um processo. Deve conter o número do processo, os parâmetros, a situação do processo, as datas Início Execução e Fim Execução, além da informação do Usuário que fez a execução do processo. | MFS-33977 |
| --- | --- | --- |
| Logs | Esta aba deve demonstrar os logs do processo.   Na parte superior da tela exibir os parâmetros que foram indicados na tela de geração, seguindo o formato abaixo: | MFS-33977 |
