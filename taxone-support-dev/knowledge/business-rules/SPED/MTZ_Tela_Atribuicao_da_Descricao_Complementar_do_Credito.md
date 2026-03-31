# MTZ_Tela_Atribuicao_da_Descricao_Complementar_do_Credito

> Fonte: MTZ_Tela_Atribuicao_da_Descricao_Complementar_do_Credito.doc

EFD - Contribuições - Tela Atribuição da Descrição Complementar do Crédito


DOCUMENTO DE REQUISITO


### REGRAS DE NEGÓCIO











| DR | Nome | Descrição | Data Alteração |
| --- | --- | --- | --- |
| OS3859 | Criação de Tela | Criar a tela ‘Atribuição da Descrição Complementar do Crédito’ | 19/02/2013 |
| OS4058 | Criação de Campos | Criação de campos na tela “Atribuição da Descrição Complementar do Crédito” | 09/06/2014 |


| Cód. |  | DR |
| --- | --- | --- |
| RN00 | Criar a tela ‘Atribuição da Descrição Complementar do Crédito’, no Módulo: SPED EFD-Escrituração Fiscal Digital das Contribuições, Menu: Parâmetros  Apuração | OS3859 |
| RN01 | Na tela de Pesquisa: Exibir os campos: Estabelecimento, Cód. Tipo Crédito, Natureza da Base do Crédito, Válido Em. | OS3859 |
| RN02 | Na tela de Inclusão: Inclusão dos campos: Estabelecimento, Validade Inicial, Cód. Tipo Crédito, Natureza da Base do Crédito, Descrição Complementar do Crédito. |  |
| RN02 | Campos Obrigatórios: Estabelecimento, Validade Inicial, Cód. Tipo Crédito, Natureza da Base do Crédito, Descrição Complementar do Crédito. | OS3859 |
| RN03 | Campos Chaves: Estabelecimento, Validade Inicial, Cód. Tipo Crédito, Natureza da Base do Crédito. | OS3859 |
| RN04 | Campo Tipo de Crédito:  Opções válidas:                                 Obs. Se o cliente optar por escolher a opção ‘Todos’, a parametrização será considerada para todos os tipos de creditos existentes. | OS3859 |
| RN05 | Campo Natureza da Base do Crédito:  Opções válidas: | OS3859 |
| RN06 | Campo Descrição Complementar do Crédito: Tipo: A Tamanho: 60 | OS3859 |
| RN07 | Incluir a opção de Replicar para os Estabelecimentos a parametrização.  Funcionamento do botão Confirma Replicação: O usuário seleciona os Estabelecimentos que precisa replicar a parametrização, caso clique em Confirma Replicação, irá aparecer a mensagem: "Deseja realmente replicar as informações para o(s) Estabelecimento(s) selecionado(s) ?" Clicando em Sim, será feita a replicação, caso contrário, nada será feito. | OS3859 |
| RN08 | A parametrização realizada para um estabelecimento centralizador deverá ser utilizada para todos os seus estabelecimentos centralizados. | OS3859 |
| RN09 | Procedimento realizado pela tela: No momento da geração dos registros M105/M505 a rotina deve verificar se há uma descrição associada nesta tela, para o tipo de crédito e natureza da receita. Caso exista, o campo ‘dsc_cred’ dos registros M105 e M505 serão populados. | OS3859 |
| RN10 | Se o usuário tentar gravar um registro, com as mesmas informações (nos campos chaves), de um registro que já está na base, exibir a seguinte msg: “Já existe uma parametrização nesta data para este tipo de crédito e natureza da base de crédito, você deseja sobrepor o registro? “  Se não, nada será gravado.  Se sim, o registro será sobreposto. | OS3859 |
| RN11 | Cód. Sit. Trib. PIS (Cód/Desc)  Campo do tipo Editbox, este será chave e não obrigatório, caso não preenchido assumir NULL. Se preenchido, informar de acordo com a Tabela indicada no site da Receita (http://www1.receita.fazenda.gov.br/sped-fiscal-pis-cofins/tabelas-de-codigos.htm)  seguindo a regra:  Conteúdo da TACES65 de acordo com os códigos 50 a 66. | OS4058 |
| RN12 | Cód. Sit. Trib. COFINS (Cód/Desc)  Campo do tipo Editbox, este será chave e não obrigatório, caso não preenchido assumir NULL. Se preenchido informar de acordo com a Tabela indicada no site da Receita (http://www1.receita.fazenda.gov.br/sped-fiscal-pis-cofins/tabelas-de-codigos.htm) seguindo a regra:  Conteúdo da TACES65 de acordo com os códigos 50 a 66. | OS4058 |
| RN13 | Alíquota PIS:   Campo do tipo Editbox, este será chave e não obrigatório, caso não preenchido assumir NULL. Se preenchido informar a alíquota PIS (em percentual), de acordo com as tabelas externas disponibilizadas pela RFB. Caso este campo for preenchido o campo “Alíquota PIS – em reais” deverá ser desabilitado. | OS4058 |
| RN14 | Alíquota COFINS:   Campo do tipo Editbox, este será chave e não obrigatório, caso não preenchido assumir NULL. Se preenchido Informar a alíquota COFINS (em percentual), de acordo com as tabelas externas disponibilizadas pela RFB. Caso este campo preenchido o campo “Alíquota COFINS – em reais” deverá ser desabilitado. | OS4058 |
| RN15 | Alíquota PIS – em reais:   Campo do tipo Editbox, este será chave e não obrigatório, caso não preenchido assumir NULL. Se preenchido informar a alíquota PIS (em reais), de acordo com as tabelas externas disponibilizadas pela RFB. Caso este campo preenchido o campo “Alíquota PIS” deverá ser desabilitado. | OS4058 |
| RN16 | Alíquota COFINS – em reais:   Campo do tipo Editbox, este será chave e não obrigatório, Caso não preenchido assumir NULL. Se preenchido informar a alíquota COFINS (em reais), de acordo com as tabelas externas disponibilizadas pela RFB. Caso este campo preenchido o campo “Alíquota COFINS” deverá ser desabilitado. | OS4058 |
