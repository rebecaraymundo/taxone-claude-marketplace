# MTZ_EFD_Parametros_Registro_1400_EE_Produto_Isencao

> Fonte: MTZ_EFD_Parametros_Registro_1400_EE_Produto_Isencao.docx






THOMSON REUTERS

Módulo Sped Fiscal

Parâmetros de Produtos com Isenção de ICMS p/ Geração do Registro 1400 (Energia Elétrica)


Localização: Menu Sped, Módulo: Escrituração Fiscal Digital, item Parâmetros  Registro 1400  Serviço de Energia Elétrica  Produto com Isenção de ICMS




DOCUMENTO DE REQUISITO


Sumário

1.	Introdução	2
2.	Layout da Tela	2
3.	Funcionamento da Tela	3
4.	Botões da barra de menu:	5
5.	Regras de Funcionamento dos Campos	5
6.	Validações	8

## Introdução


Esta tela tem objetivo de promover a parametrização dos produtos a serem utilizados na rotina de geração do registro 1400, formato Padrão e formato Especifico por UF (estado do Paraná) para Energia Elétrica, realizada no menu “Geração  Meio Magnético” do módulo Sped Fiscal.

Essa parametrização trabalha com uma faixa de produtos determinada pelo Código do Produto Inicial e Final, significando que todos os códigos contidos nessa faixa são considerados com Isenção de ICMS.

A tela permite excluir alguns produtos dessa faixa deixando-os de forma da parametrização.

A faixa de produtos parametrizada é armazenada na tabela PRT_PROD_MSAF, cuja chave de identificação é formada pelos campos:

Empresa
Estabelecimento
Código Parâmetro
Grupo do Produto
Indicador do Produto
Código do Produto Inicial

Os produtos excluídos da faixa são armazenados na tabela PRT_PROD_EXC_MSAF, cuja chave de identificação é formada pelos campos:

Empresa
Estabelecimento
Código Parâmetro
Grupo do Produto
Indicador do Produto
Código do Produto Inicial
Código do Produto Excluído




## Layout da Tela




## Funcionamento da Tela







## Botões da barra de menu:






## Regras de Funcionamento dos Campos






## Validações



No momento de salvar a operação, serão realizadas algumas críticas, como descrito a seguir:

Critica 1: Campos Obrigatórios

Validações de Campos Obrigatórios não preenchidos.
Quando o campo é obrigatório e não estiver preenchido, exibir mensagem padrão.
A obrigatoriedade dos campos está definida no tópico “5 – Regras de Funcionamento dos Campos”.

Crítica 2: Código Final x Código Inicial

Verifica se o código final é realmente >= código inicial. Caso não, será exibida a mensagem abaixo, e a operação não será salva:
“Código do produto final deve ser maior ou igual ao código do produto inicial”

Crítica 3: Faixas de Códigos intercaladas

Verifica se já existe outro registro na parametrização que contenha o produto informado, ou a faixa de produtos, quando for o caso (ou seja, se haverá faixas de produtos intercalados).

Exemplo I:

Registro 1   Código inicial = 1000500  Código final = 1000599
Registro 2   Código inicial = 1000600  Código final = 1000699
Registro a ser incluído   Código inicial = 1000540  Código final = 1000545

Neste exemplo, teríamos um erro na parametrização, pois a faixa do registro a ser importado já se encontra contida na faixa do registro 1.

Exemplo II:

Registro 1   Código inicial = 1000500  Código final = 1000599
Registro 2   Código inicial = 1000600  Código final = 1000900
Registro a ser incluído   Código inicial = 1000000  Código final = 1000800

Neste exemplo, também teríamos erro na parametrização, pois a faixa do registro a ser gravada engloba  toda faixa do registro 1, e além disso, se intercala com a faixa do registro 2.

Quando ocorrer este tipo de problema, a operação não será salva, e será exibida a mensagem abaixo:

“Código Inicial e/ou Final já contido em outra faixa de produtos”



= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS58137 | Liliane Assaf | Criação da parametrização de produtos para geração do 1400 formato Padrão em atendimento a Energia Elétrica | 04/03/2021 |
| MFS62640 | Aline Melo | Ajuste do item de menu de parametrização de produtos para geração do 1400 formato Padrão, para ser disponibilizado para a geração Específico por UF, em atendimento a Energia Elétrica | 16/06/2021 |
|  |  |  |  |


| Passo | Acionador | Descrição |
| --- | --- | --- |
| 1 | Usuário | Usuário seleciona o item de menu Parâmetros  Registro 1400   Padrão  Serviço de Energia Elétrica  Produto com Isenção de ICMS |
| 2 | Sistema | Verifica o usuário informou estabelecimento no login do Manager. |
| 3 | Sistema | Sistema abre a tela de seleção dos grupos cadastrados no Relacionamento entre Tabela e Grupos (Relac_Tab_Grupo).  Se no login foi informado estabelecimento, então: Sistema disponibilizados apenas os grupos relacionados ao estabelecimento em questão, relacionados a Tabela Produto. Senão Sistema exibe os grupos dos estabelecimentos da empresa, relacionados a Tabela Produto. |
| 4 | Usuário | Usuário seleciona um registro de grupo/estabelecimento do Relacionamento entre Tabela e Grupo. |
| 5 | Sistema | Abre a tela de Parametrização dos Produtos, com os campos Estabelecimento e Grupo preenchidos e bloqueados. Os campos Indicador, Código Inicial, Código Final são apresentados “em branco”. |
| 6 | Usuário | Usuário seleciona um indicador do produto na lista do campo “Indicador”. |
| 7 | Sistema | Sistema habilida os campos Código Inicial, Código Final. |
| 8 | Usuário | Digita ou seleciona na pastinha o Código Inicial. |
| 9 | Sistema | Valida o Código Inicial no Cadastro de Produtos (SAFX2013). Vide regra do campo “Início Validade” descrita no tópico “5 – Regras de Funcionamento dos Campos”. |
| 10 | Usuário | Digita ou seleciona na pastinha o Código Final. |
| 11 | Sistema | Valida o Código Final no Cadastro de Produtos (SAFX2013). Vide regra do campo “Início Validade” descrita no tópico “5 – Regras de Funcionamento dos Campos”. |
| 12 | Usuário | Usuário escolhe “Informar Exclusões”. |
| 13 | Sistema | Sistema apresenta o conjunto de produtos cujo código está compreendido entre os Códigos Inicial e Final informados. |
| 14 | Usuário | Seleciona alguns produtos a serem excluídos da faixa. |
| 15 | Usuário | Seleciona botão confirma. |
| 16 | Sistema | Executa validações descritas no tópico 6- Validações.  Caso os dados estejam consistentes, grava as parametrizações na tabela definitiva. |
| 17 | Usuário | Seleciona outras ações disponíveis na barra de menu da janela. Vide tópico “4 - Botões da barra de menu” |


| SELECIONAR GRUPO | Ao clicar nesta opção será aberta a janela de seleção dos grupos de relacionamento (relacionamento Tabela x Grupos), e o usuário poderá selecionar o grupo desejado. Se no login foi informado estabelecimento, então: Sistema disponibilizados apenas os grupos relacionados ao estabelecimento em questão, relacionados a Tabela Produto. Senão Sistema exibe os grupos dos estabelecimentos da empresa, relacionados a Tabela Produto.  Seguir o passo 4 do fluxo descrito no tópico 3 – Funcionamento da Tela. |
| --- | --- |
| NOVO | Ao clicar nesta opção, as informações dos campos serão limpas (exceto os campos Estabelecimento e Grupo que mantém preenchidos e bloqueados) e o usuário poderá incluir uma nova parametrização. |
| ABRE | Ao clicar nesta opção, será aberta a janela para seleção das parametrizações já cadastradas para consulta ou manutenção. |
| EXCLUI | Esta opção permite a exclusão das parametrizações do estabelecimento, grupo, Data Início Validade e Código em questão. |
| CONFIRMA | Opção para salvar as informações da parametrização incluída ou alterada. |
| RELATÓRIO | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | N |  | Neste campo será exibido o código e a razão social do estabelecimento do Grupo selecionado pelo usuário na abertura da tela, ou através da opção “SELECIONAR GRUPO” da barra de menu. |  |
| Grupo | Alfanumérico | S | N |  | Neste campo será exibido o Grupo selecionado pelo usuário na abertura da tela, ou através da opção “SELECIONAR GRUPO” da barra de menu. |  |
| Indicador | Alfanumérico | S | N | Lista | Este campo é uma lista dos indicadores de produto da SAFX2013:  1 - Produto 2 - Matéria Prima/Insumo 3 - Embalagem 4 - Material Uso/Consumo 5 - Outros 6 - Em Elaboração 7 - Intermediário 8 - Miscelâneas |  |
| Código Inicial | Alfanumérico | S | S | Pasta – Código – Descrição | Este campo trabalha com janela de seleção dos produtos da SAFX2013, considerando apenas os produtos do Grupo selecionado e também do indicador de produto selecionado.   Após informar o código inicial, caso o campo “Código Final” ainda não tenha sido informado, o campo do código final será inicializado com o mesmo conteúdo do produto inicial.  Quando o código for digitado, será verificada a existência do produto na tabela de produtos (SAFX2013), considerando o Grupo e o indicador informados. Caso não exista, será exibida mensagem a mensagem “Produto não Cadastrado” no campo destinado a descrição do produto. |  |
| Código Final | Alfanumérico | S | S | Pasta – Código – Descrição | Este campo será inicializado com o mesmo código de produto informado no campo “Código Inicial”, mas o usuário poderá alterar este conteúdo através da janela de seleção da SAFX2013 ou de digitação, assim como é feito no campo do código inicial.  Quando o código for digitado, será verificada a existência do produto na tabela de produtos (SAFX2013), considerando o Grupo e o indicador informados. Caso não exista, será exibida a mesma mensagem já definida para o código inicial. |  |
| Informar Exclusão | Alfanumérico | N | S | Checkbox | Através deste parâmetro o usuário poderá selecionar alguns produtos da faixa escolhida para desconsiderar da parametrização.   Ao clicar nesta opção, todos os produtos da faixa informada (código inicial ao final) serão exibidos no quadro “Produtos Excluídos da Faixa”.  Ao desmarcar a opção, todo o conteúdo do quadro “Produtos Excluídos da Faixa” será apagado. |  |
| Produtos Excluídos da Faixa | Radio Button | N | S |  | Neste quadro serão demonstrados todos os produtos da faixa informada (código inicial ao final), e o usuário poderá selecionar os produtos que desejar para que sejam desconsiderados da parametrização.   O conteúdo deste quadro será automaticamente apagado sempre que o usuário desmarcar a opção “Informar Exclusões”. |  |
| Replicar para os Estabelecimentos | Alfanumérico | N | S |  | Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados. Serão exibidos para seleção apenas os estabelecimentos da mesma empresa do estabelecimento parametrizado e do mesmo Grupo informado.  Para selecionar os estabelecimentos, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. |  |
| COD_PARAM | Alfanumérico |  |  |  | Esse campo não deve ser demonstrado na tela nem no relatório. Gravar o registro com COD_PARAM = 788.  Esse código é carregado pela TFIX31. |  |
