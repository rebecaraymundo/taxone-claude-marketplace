# MTZ_EFD_Parametros_Registro_0221_Produtos

> Fonte: MTZ_EFD_Parametros_Registro_0221_Produtos.docx






THOMSON REUTERS

Manutenção Correlação entre Códigos de Itens Comercializados (SAFX278)


Localização: Menu Sped, Módulo EFD - Escrituração Fiscal Digital, item Parâmetros > Registro 0221 > Produtos


DOCUMENTO DE REQUISITO


Sumário



1.1.	Introdução	3
1.2.	Layout da Tela	3
1.3.	Regras dos Campos	3
1.4.	Regra de Validação	5


## Introdução


Esta tela tem como objetivo permitir que o usuário faça a parametrização das informações do registro 0221 - Correlação entre Códigos de Itens Comercializados.

## Layout da Tela






## Regras dos Campos


Essa tela de manutenção é atendida pela SAFX278. Para verificar a sua estrutura, consulte o Manual Layout.

As informações devem ser gravadas nas seguintes tabelas:

EFD_PAR_PROD_0221 (tabela que grava o produto principal)

Campos que compõe a chave da tabela: COD_EMPRESA + COD_ESTAB + GRUPO + IND_PRODUTO + COD_PRODUTO + DATA_INI

EFD_PAR_PROD_0221_ASS (tabela que grava os produtos associados)

Campos que compõe a chave da tabela: COD_EMPRESA + COD_ESTAB + GRUPO + IND_PRODUTO + COD_PRODUTO + DATA_INI + IND_PRODUTO_ASS + COD_PRODUTO_ASS

No acesso à tela o sistema deve exibir a tela padrão de seleção de Estabelecimento/Grupo/Validade.
Na barra de ferramentas, deve existir o botão de seleção de Grupo:




## Regra de Validação


[MFS606215] Retirada da regra de relacionamento de produto principal x produto associado

Ao salvar o registro, devem ser feitas as seguintes validações

Se no campo “Produtos Associados” o item informado já tiver sido associado ao item informado no Produto, a operação não será salva e será exibida a seguinte mensagem de erro: “O produto associado já se encontra cadastrado para o produto principal, e não será permitida a sua inclusão.”

Se para um dos itens informados no campo “Produtos Associados”, NÃO for informada a quantidade, a operação não será salva e será exibida a seguinte mensagem de erro: “Não foi informada a quantidade para um ou mais itens informados no campo Produtos Associados”.

Quando for informado somente um item no campo “Produtos Associados”, e esse item for IGUAL ao item informado no campo “Produto”, deve ser verificado se a quantidade informada é IGUAL a “1”. Se a quantidade for DIFERENTE de “1”, a operação não será salva e será exibida a seguinte mensagem de erro: “Para essa situação, o campo Quantidade deve ser preenchido somente com “1”.


## Cenários


Exemplos de cenários possíveis de correlação de itens:

Cenário 01: Produto “CESTA BÁSICA” composta por 4 itens diferentes (ARROZ, FEIJÃO, AÇUCAR e CAFÉ). Nessa situação o produto “CESTA BÁSICA” deve ser informado no campo “Produto” e seus respectivos itens devem ser informados no campo “Produtos Correlacionados”. Cada item a ser informado para o produto “CESTA BÁSICA” deve ser DIFERENTE do produto “CESTA BÁSICA”. Para cada item do campo “Produtos Correlacionados” deve ser informada a respectiva quantidade.


Cenário 02: Produto “LATA DE REFRIGERANTE X COM 350ML”. Nessa situação o produto “LATA DE REFRIGERANTE X COM 350ML” deve ser informado no campo “Produto” e deve possuir somente 1 item no campo “Produtos Correlacionados”. O item deve ser IGUAL ao campo “Produto” e deve possuir quantidade IGUAL a ‘1’.



Cenário 03: Produto “CAIXA COM 12 LATAS DE REFRIGERANTE X COM 350ML”. Nessa situação o produto “CAIXA COM 12 LATAS DE REFRIGERANTE X COM 350ML” deve ser informado no campo “Produto” e deve possuir somente 1 item no campo “Produtos Correlacionados”. O item deve ser IGUAL ao campo “Produto” e deve possuir a quantidade IGUAL a “12”.




| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS97666 | Aline Melo | Criação da tela de parametrização de produtos e seis itens correlacionados. |
| MFS606215 | Andréa Rocha | Alteração de regra de relacionamento de produto principal x produto associado.  Essa alteração é necessária porque essa regra está impedindo de se fazer um relacionamento válido para a geração do registro 0221 do SPED-EFD. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | N |  | Neste campo será exibido o código e a razão social do estabelecimento do Grupo selecionado pelo usuário na abertura da tela, ou através da opção “GRUPO” da barra de menu. | MFS97666 |
| Validade (de / até) | Data | S / N | S | dd/mm/aaaa | O usuário deverá informar um período de validade da parametrização.  A data de validade inicial é obrigatória, já a data final pode ficar sem preenchimento.   Consistência Validade x Grupo: A data de validade inicial não pode ser inferior à data de validade do Grupo informado (campo “Grupo”). Caso isso ocorra, será exibida a seguinte mensagem:  “A validade inicial não pode ser inferior à validade do Grupo informado”  Consistência Validade Inicial x Validade Final: A data de validade inicial não pode ser superior à data de validade final. Caso isso ocorra, será exibida a seguinte mensagem:  “A validade inicial não pode ser superior à validade final.” | MFS97666 |
| Produto (Grp./Ind./Cód./Desc.) | Alfanumérico | S | N |  | Este campo trabalha com janela de seleção dos produtos da SAFX2013, considerando apenas os produtos do Grupo escolhido na abertura da tela.  Quando o produto for digitado será validada a sua existência na tabela, e caso não exista, será exibida mensagem de erro padrão.  Ao salvar a operação, serão feitas as seguintes críticas:  - Um determinado produto só pode ser parametrizado para outra data de validade inicial se a parametrização anterior for finalizada. Assim, caso o produto já conste na parametrização, a validade final da parametrização já existente (a mais atual) deve estar preenchida. Ou seja, a parametrização mais atual não poderá estar em aberto. Caso contrário, a operação não será salva e será exibida a seguinte mensagem: “Foi encontrada parametrizacao para o produto, com datas de vigencia em conflito com as datas de vigencia informadas”  - Estando a parametrização anterior já finalizada, será verificado se a validade inicial da nova parametrização é superior à data da validade final da parametrização já existente (a mais atual). Caso contrário, a operação não será salva e será exibida a seguinte mensagem:“Foi encontrada parametrizacao para o produto, com datas de vigencia em conflito com as datas de vigencia informadas” | MFS97666 |
| Produtos Associados (Grp./Ind./Cód./Desc.) | Alfanumérico | S | S |  | Neste campo o usuário deve informar um ou mais produtos que serão associados ao produto principal.   Da mesma forma que o campo “Produto”, este campo trabalha com janela de seleção dos produtos da SAFX2013, considerando apenas os produtos do Grupo escolhido na abertura da tela.  Quando o produto for digitado será validada a sua existência na tabela, e caso não exista, será exibida mensagem de erro padrão.   Para as demais validações, verificar o item 4. | MFS97666 |
| Quantidade | Numérico | S | S |  | Neste campo deve ser informado a quantidade do item do produto associado.  Para as demais validações, verificar o item 4. | MFS97666 |
| Replicar para os Estabelecimentos | Alfanumérico | N | S |  | Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados. Serão exibidos para seleção apenas os estabelecimentos da mesma empresa do estabelecimento parametrizado, e do mesmo Grupo informado e que pertençam a UF do estabelecimento informado.  Para selecionar os estabelecimentos, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. | MFS97666 |


| PRODUTO | CESTA BÁSICA |  |
| --- | --- | --- |
| PRODUTOS CORRELACIONADOS | ARROZ | 1 |
|  | FEIJÃO | 2 |
|  | AÇUCAR | 1 |
|  | CAFÉ | 2 |


| PRODUTO | REFRIGERANTE X com 350ml |  |
| --- | --- | --- |
| PRODUTOS CORRELACIONADOS | REFRIGERANTE X com 350ml | 1 |


| PRODUTO | REFRIGERANTE X com 350ml |  |
| --- | --- | --- |
| PRODUTOS CORRELACIONADOS | REFRIGERANTE X com 350ml | 12 |
