# MTZ_Tela_Parametros_Apuracao_Identificador da Natureza da Receita

> Fonte: MTZ_Tela_Parametros_Apuracao_Identificador da Natureza da Receita.docx






THOMSON REUTERS

Identificador da Natureza Receita



DOCUMENTO DE REQUISITO


Sumário

1.	OBJETIVO	3
2.	Regras dos Campos	3
2.1.	Botões da Toolbar	3
2.2.	Tela e Regras dos Campos	3

## OBJETIVO



## Regras dos Campos


#### Botões da Toolbar


Novo, Abre, Exclui, Confirma, Relatório e Fecha.

#### Tela e Regras dos Campos




Localização da tela: Módulo:  SPED >> EFD – Escrituração Fiscal Digital das Contribuições
Menu: Parâmetros >> Apuração >> Identificador da Natureza da Receita

Título da tela: Novo Identificador da Natureza da Receita







| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4706 | Elenilson Coutinho | Criação do parâmetro CST/Conta Contábil |
| MFS-31306 | Alessandra Cristina Navatta | Criar a funcionalidade de Replicar para os Estabelecimentos na tela |
| MFS-682770 | Alessandra Cristina Navatta | Documentar as regras da tela (reversa) |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Lista | S |  | Cód - Descrição | Apresenta todos os estabelecimentos da empresa logada, para seleção, quando selecionado na header a opção “Todos” no campo de estabelecimento.  Caso definido um estabelecimento específico, no header, este estabelecimento é atribuído no campo de estabelecimento da tela (sem possível alteração) | MFS-682770 |
| Tipo Parametrização | Radio-button | S | S | Default: Produto/NBM | [ALTERAÇÂO] Opções Válidas: Produto/NBM Serviço CST/Alíquota CST/Conta Contábil   [OS4706 ]– Quando CST/Conta Contábil, selecionado: O campo “Conta Contábil” passará a compor a chave da tabela, porém não obrigatório. Para os casos de não preenchimento do campo deverá preencher com “Null” na tabela.   Obs: Após a inclusão do registro, somente os campos “Código Natureza da Receita”, “Conta Contábil” e “Descrição Resumida” ficarão habilitados na consulta. | OS4706 MFS-682770 |
| Validade | Data | S | S | Inicial: DD/MM/AAAA Final: DD/MM/AAAA | Apenas a validade Inicial é de preenchimento obrigatório. Caso não preenchido, exibir a mensagem: “Necessário Informar a Data Inicial de Validade.” | MFS-682770 |
| CST PIS/COFINS | Pasta | N | S |  | Recupera as informações da TACES65 - Códigos Situação Tributária.  Se não for informado Data de Validade Inicial e selecionar o campo, exibir a mensagem: “Necessário Informar a Data Inicial de Validade.” | MFS-682770 |
| Produto (Gr./Ind./Cód./ Val.) | Pasta | N | S |  | Recupera as informações da tabela de produtos (SAFX2013).  Quando o campo Tipo Parametrização = Serviço, OU  CST/Alíquota, OU CST/Conta Contábil, este campo deve ficar desabilitado.  Quando o campo Tipo Parametrização = Produto e se não for informado Data de Validade Inicial e selecionar o produto, exibir a mensagem: “Grupo de Produto não definido. Informar Data Inicial de Validade.” | MFS-682770 |
| NCM Inicial (Gr./Cód./ Val.) | Pasta | N | S |  | Recupera as informações da SAFX2043 - Códigos NBM   Quando o campo Tipo Parametrização = Serviço, OU CST/Alíquota, OU CST/Conta Contábil, este campo deve ficar desabilitado.   Quando o campo Tipo Parametrização = Produto e se não for informado Data de Validade Inicial e selecionar o campo, exibir a mensagem: “Necessário Informar a Data Inicial de Validade.” | MFS-682770 |
| NCM Final (Gr./Cód./ Val.) | Pasta | N | S |  | Recupera as informações da a SAFX2043 - Códigos NBM  Quando o campo Tipo Parametrização = Serviço, OU CST/Alíquota, OU CST/Conta Contábil, este campo deve ficar desabilitado.   Quando o campo Tipo Parametrização = Produto e se não for informado Data de Validade Inicial e selecionar o campo, exibir a mensagem: “Necessário Informar a Data Inicial de Validade.” | MFS-682770 |
| Serviço | Pasta | N | S |  | Recupera as informações da tabela de serviços (SAFX2018).  Quando o campo Tipo Parametrização = Produto/NCM, OU CST/Alíquota, OU CST/Conta Contábil, este campo deve ficar desabilitado.  Quando o campo Tipo Parametrização = Serviço e se não for informado Data de Validade Inicial e selecionar o campo, exibir a mensagem: ”Grupo de Serviço não definido. Informar Data Inicial de Validade.” | MFS-682770 |
| Cód. Natureza da Receita | Pasta | S | S |  | Recuperar as informações da TACES72, de acordo com a informação indicada no campo de CST PIS/COFINS indicada no respectivo campo.  Se não for informado Data de Validade Inicial e selecionar o campo, exibir a mensagem: “Necessário Informar a Data Inicial de Validade.” | MFS-682770 |
| CFOP | Pasta | N | S |  | Recupera as informações da tabela de Códigos fiscais (SAFX2012).  Quando o campo Tipo Parametrização = Serviço, OU CST/Conta Contábil, este campo deve ficar desabilitado.  Quando o campo Tipo Parametrização = Produto, OU CST/Alíquota, e se não for informado Data de Validade Inicial e selecionar o campo, exibir a mensagem: “Informar a Data Inicial de Validade.” | MFS-682770 |
| Conta Contábil (Gr./Cód./ Val./Desc.) | Pasta | N | S |  | Recupera as informações da tabela de plano de contas (SAFX2002).  Se não for informado Data de Validade Inicial e selecionar o campo, exibir a mensagem: “Não Existe Grupo válido para Plano de Conta na tabela Operação.” | MFS-682770 |
| Alíquota PIS (em %) | Numérico | N | S | 0,0000 | Quando o campo Tipo Parametrização = CST/Conta Contábil, este campo deve ficar desabilitado. | MFS-682770 |
| Alíquota COFINS (em %) | Numérico | N | S | 0,0000 | Quando o campo Tipo Parametrização = CST/Conta Contábil, este campo deve ficar desabilitado. | MFS-682770 |
| Alíquota PIS (em Reais) | Numérico | N | S | 0,0000 | Quando o campo Tipo Parametrização = CST/Conta Contábil, este campo deve ficar desabilitado. | MFS-682770 |
| Alíquota COFINS (em Reais) | Numérico | N | S | 0,0000 | Quando o campo Tipo Parametrização = CST/Conta Contábil, este campo deve ficar desabilitado. | MFS-682770 |
| Descrição Resumida | Texto | N | S |  | Informar uma descrição, quando necessário. | MFS-682770 |
| Replicar para os Estabelecimentos | Check-box | N | S | Default: Não selecionado | Serão apresentados no componente, todos os estabelecimentos da empresa que está logada. E só ficarão habilitados para serem marcados se a opção ‘Replicar para os Estabelecimentos’ estiver selecionada. Neste caso, poderá ser selecionado um ou mais estabelecimentos.  Se a opção ‘Replicar para os Estabelecimentos’ estiver selecionada, os botões ‘Selecionar Todos’ e ‘Desmarcar Todos’ devem ficar habilitados.   Ao selecionar o botão “Selecionar Todos’, todos os estabelecimentos do componente ‘Replicar para os Estabelecimentos serão selecionados.’  Ao selecionar o botão “Desmarcar Todos’, todos os estabelecimentos do componente ‘Replicar para os Estabelecimentos serão desmarcados.’  Se a opção ‘Replicar para os Estabelecimentos’ estiver marcada e clicar em confirma, pelo menos um estabelecimento deve estar marcado para replicar a parametrização, caso contrário, exibir a mensagem: ‘Selecionar pelo menos um estabelecimento para a Replicação.’  Se a opção ‘Replicar para os Estabelecimentos’ estiver marcada e existir um ou mais estabelecimentos selecionados, ao clicar no botão confirma, a parametrização criada, será replicada a todos os estabelecimentos que foram selecionados no componente. | MFS-31306 |
| Confirma | Botão |  |  |  | Validação de Datas Se Validade Inicial estiver sem preenchimento, exibir: “Favor Informar a Validade Inicial.”  Data de Validade Final deve ser maior que a Inicial, quando preenchida. Caso contrário, exibir a mensagem: ”Validade Final deve ser maior que a Inicial”  Quando Tipo Parametrização = Produto/NBM:  Se for preenchido o campo NBM Final e o NBM Inicial, estiver sem preenchimento, exibir a mensagem: “Favor Informar NBM Inicial.”  Quando Tipo Parametrização = Produto/NBM ou Serviço:  Se o campo CST PIS/COFINS estiver sem preenchimento, exibir: “Favor Informar o CST PIS/COFINS.”  Se Tipo parametrização igual a Produto/NBM e campo Produto/NBM sem preenchimento, ou se Tipo Parametrização = Serviço e se Serviço estiver sem preenchimento, exibir: “Favor Informar o Produto/NBM ou Serviço.”  Se o campo Cód. Natureza da Receita estiver sem preenchimento, exibir: “Favor Informar o Cód. Natureza da Receita.”  Quando Tipo Parametrização = CST/Alíquota ou CST/Conta Contábil:  Se o campo CST PIS/COFINS estiver sem preenchimento, exibir: “Favor Informar o CST PIS/COFINS.”  Se o campo Cód. Natureza da Receita estiver sem preenchimento, exibir: “Favor Informar o Cód. Natureza da Receita.”  Quando Tipo Parametrização diferente de CST/Conta Contábil e os campos de Alíquota PIS e / ou COFINS estiver preenchido para Valor (R$) e também para Percentual (%):  Exibir a mensagem: “A Alíquota para PIS e COFINS deve ser informada, em Valor (R$) ou em Percentual(%).” e não gravar as alíquotas. | MFS-682770 |
