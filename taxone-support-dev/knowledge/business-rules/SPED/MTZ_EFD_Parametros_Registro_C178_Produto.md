# MTZ_EFD_Parametros_Registro_C178_Produto

> Fonte: MTZ_EFD_Parametros_Registro_C178_Produto.docx






THOMSON REUTERS

Matriz da tela de Parametrização por Produto - C178



DOCUMENTO DE REQUISITO


Sumário

1.	TELA A SER DESENVOLVIDA	3
1.1.	Diagrama de Casos de Uso	3
1.1.1.	UC001 – Manutenção da Estrutura Padrão	3
1.1.1.1.1.	Fluxo Principal	4
1.1.1.1.2.	Fluxo Alternativo 1 – Novo Registro	4
2.	Regras dos Campos	4

## TELA A SER DESENVOLVIDA


[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir]

### Diagrama de Casos de Uso




### UC001 – Manutenção da Estrutura Padrão


[Descrever a ação deste caso de uso.

Ex.: Este caso de uso descreve o processo de Cadastro de Estrutura Padrão.]



#### Fluxo Principal



#### Fluxo Alternativo 1 – Novo Registro




## Regras dos Campos


Localização da tela:
Módulo: SPED >> EFD – Escrituração Fiscal Digital
Menu: Parâmetros >> Registro C178

Título da tela: Por Produto

Funcionamento da tela: esta tela foi criada para possibilitar ao usuário a parametrização de produtos cuja tributação de IPI seja cálculada com base em um valor pré determinado pela RFB e não por uma alíquota. Esta informação não consta em NF, trata-se de uma legislação publicada e atualizada pela RFB e que justifica o valor do IPI destacado na nota.

Através desta tela será possível ao contribuinte parametrizar a legislação vigente em determinado período e fornecer ao sistema as informações necessárias para geração do Registro C178 – Operações com Produtos Sujeitos à Tributação do IPI por Unidade ou Quantidade de Produto, no arquivo do SPED Fiscal.

A tela deve permitir a gravação das informações por Estabelecimento, Modelo do Documento, Valor por Unidade Padrão e Vigência da Tributação e para cada combinação destes campos poderão ser informados “N” códigos de Produto. Os códigos de Produto só poderão ser associados a outra parametrização quando a primeira tiver a vigência até informada e a nova parametrização deverá ser posterior à encerrada, sendo esta data no mínimo um dia a mais que a data de encerramento da parametrização anterior.

No acesso à tela o sistema deve exibir a tela padrão de seleção de Estabelecimento/Grupo/Validade:



Na barra de ferramentas, deve existir o botão de seleção de Grupo:

A pesquisa de produtos irá considerar o grupo selecionado no momento da entrada na tela.



* Descrição não disponível em tela



| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4821 | Marcos G. de Paula | Definição das regras da tela de Parametrização por Produto para geração do Registro C178 da EFD. |
|  |  |  |


| Documentação do Caso de Uso | Documentação do Caso de Uso |
| --- | --- |
| Ator Principal | Usuário do Sistema. |
| Pré- Condições | Estar logado no produto MasterSAF DW. |
| Pós-Condições | Não se aplica. |


| Ações do Ator | Ações do Sistema |
| --- | --- |
|  |  |
|  |  |


| Ações do Ator | Ações do Sistema |
| --- | --- |
|  |  |
|  | Fim do fluxo Alternativo |


| Campo | Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Estabelecimento | Editbox | S | N |  | Será preenchido com o código + razão social do estabelecimento que foi selecionado na tela de Estabelecimento/Grupo/Validade no acesso à parametrização. | OS4821 |
| Modelo do Documento | Modelo do Documento | Editbox | S | S |  | Informação padrão Mastersaf de Pasta de Seleção + Código + Descrição. Através da pasta de seleção o usuário deve ter acesso às informação da Tabela de Modelos de Documentos Fiscais (SAFX2024), demonstrando desta tabela apenas os módelos cujo código seja igual a “01”, “1A", “04”, “55” ou “65”. O usuário poderá informar um código de modelo, mas este deverá constar na tabela e pertencer à lista indicada. Caso o usuário não informe um código válido, retornar a mensagem: “Modelo de Documento não cadastrado”. Caso o usuário não informe o modelo do documento, retornar a mensagem: “Modelo do documento não informado”. | OS4821 |
| Unidade de Medida de Tributação | Unidade de Medida de Tributação | Editbox | S | S |  | Informação padrão Mastersaf de Pasta de Seleção + Código + Descrição. Através da Pasta de seleção o usuário deve ter acesso à informação da tabela de Unidade de Medida (SAFX2007). O usuário poderá informar um código de unidade, mas este deverá constar na tabela indicada. Caso o usuário não informe um código válido, retornar a mensagem: “Unidade de Medida não cadastrada”. Caso o usuário não informe a unidade de medida, retornar a mensagem: “Unidade de Medida de Tributação não informada”. | OS4821 |
| Valor por Unidade Padrão | Valor por Unidade Padrão | Editbox | S | S | Formato: 0,00 | Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Valor por Unidade Padrão não informado”. | OS4821 |
| Vigência da Tributação | Dê | Editbox | S | S | Formato: DD/MM/AAAA | Serão dois campos para indicação da vigência, sendo um “dê” e outro “até”. O campo “dê” é obrigatório e se não for informado, retornar a mensagem: “Início da Vigência não informada”.  O campo “Até”, quando for informado deverá ter uma data maior ou igual à informada no campo “Dê”. Se for menor, retornar a mensagem: “Fim de Vigência deve ser maior ou igual ao início”. | OS4821 |
| Vigência da Tributação | Até | Editbox | S | N | Formato: DD/MM/AAAA | Serão dois campos para indicação da vigência, sendo um “dê” e outro “até”. O campo “dê” é obrigatório e se não for informado, retornar a mensagem: “Início da Vigência não informada”.  O campo “Até”, quando for informado deverá ter uma data maior ou igual à informada no campo “Dê”. Se for menor, retornar a mensagem: “Fim de Vigência deve ser maior ou igual ao início”. | OS4821 |
| Informar Código/Descrição para Pesquisa | Informar Código/Descrição para Pesquisa | Editbox / Radiobutton | N | S | Default: Radiobutton Código selecionado | Neste campo teremos opções de pesquisa que irão refletir no resultado demonstrado na Relação de Produtos. Será um campo Editbox + Radiobutton com as opções Código e Descrição. | OS4821 |
| Pesquisar | Pesquisar | Botão | N | S |  | Quando acionado, deve pesquisar o produto através do código ou descrição, conforme selecionado pelo usuário, e atualizar a Relação de Produtos com o resultado encontrado. | OS4821 |
| Relação de Produtos | Relação de Produtos | Checkbox | S | S | Default: Não Selecionado | Neste campo será exibida a relação de produtos (SAFX2013) pertencente ao grupo que acessou a tela.  Caso o usuário utilize as opções de pesquisa, o conteúdo deste campo será atualizado para que seja demonstrado o produto (ou produtos) reflexo da pesquisa realizada, considerando sempre informação do grupo de acesso.  Deverá ser selecionado ao menos um código de produto na parametrização. Caso não seja selecionado nenhum, retornar a mensagem: “Selecione pelo menos um código de produto”.  Caso o usuário escolha na seleção de produtos, pelo menos um código de produto que pertença a uma parametrização do mesmo Estabelecimento, Modelo do Documento, Unidade de Medida de Tributação, mas com vigência final de tributação em aberto (não informada), retornar a mensagem: “Código de Produto associado a uma parametrização vigente. Deseja encerrar a parametrização em aberto?” com as opções SIM e NÃO. Se o usuário escolher SIM, o campo de vigência da tributação “até” que está em aberto deve ser atualizada com o dia anterior à data informada no campo vigência da tributação “dê” da nova parametrização. Se escolher NÃO, não permitir a associação do produto à nova parametrização e retornar a mensagem: “Produto não selecionado por pertencer à parametrização aberta”.  Caso o usuário escolha na seleção de Produtos, pelo menos um código que pertença a uma parametrização do mesmo Estabelecimento, Modelo do Documento, mas com vigência final de tributação encerrada com data posterior à data inicial da parametrização que está sendo criada e sem informar data final de vigência OU, se informar uma data de vigência maior que a data inicial da parametrização existente, retornar a mensagem: “Há conflito de vigência para a parametrização indicada” e não permitir a parametrização. Se a data final da nova parametrização for informada e for menor que a data inicial da parametrização existente, permitir a gravação. | OS4821 |
| Selecionar Todos | Selecionar Todos | Botão | N | S |  | Quando acionado este botão, todos os registros da relação de produtos que estão com status “Não Selecionado” mudarão o status para “Selecionado”. | OS4821 |
| Desmarcar Todos | Desmarcar Todos | Botão | N | S |  | Quando acionado este botão, todos os registros da relação de produtos que estão com status “Selecionado” mudarão o status para “Não Selecionado”. | OS4821 |
| Replicar para os estabelecimentos | Replicar para os estabelecimentos | Checkbox | N | S | Default: Não selecionado | Quando selecionado este parâmetro, será habilitada a caixa de seleção de estabelecimentos para que o usuário indique os estabelecimentos para os quais deseja copiar a parametrização.  Neste campo serão exibidos os estabelecimentos pertencentes a mesma empresa que acessou o módulo e grupo que acessou a tela. | OS4821 |
