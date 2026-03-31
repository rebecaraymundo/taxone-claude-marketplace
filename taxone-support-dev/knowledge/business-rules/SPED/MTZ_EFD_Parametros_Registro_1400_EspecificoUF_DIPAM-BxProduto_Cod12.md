# MTZ_EFD_Parametros_Registro_1400_EspecificoUF_DIPAM-BxProduto_Cod12

> Fonte: MTZ_EFD_Parametros_Registro_1400_EspecificoUF_DIPAM-BxProduto_Cod12.docx




THOMSON REUTERS

Módulo Sped Fiscal

Parametrização de Produtos para o código 12 da DIPAM-B (Registro 1400 p/ SP)


Localização: Módulo EFD - Escrituração Fiscal DigitaI, item Parâmetros  Registro 1400  Específico por UF  DIPAM-B – Código 1.2 x Produto (SP)

DOCUMENTO DE REQUISITO












REGRAS DE NEGÓCIO



Esta parametrização foi criada na MFS42617 com objetivo de atender a geração do registro 1400 da EFD, Código 12 da DIPAM-B.

Obs: A geração do registro 1400 para SP foi desenvolvida seguindo as mesmas regras da geração da DIPAM-B (registro 30) da GIA-SP, por isso essa parametrização vai criada também no módulo da GIA-SP.

Opções da barra de menu:

GRUPO – Ao clicar nesta opção, abrirá uma janela de seleção dos grupos de relacionamento das tabelas do Mastersaf, e o usuário deverá selecionar o grupo e estabelecimento. Na abertura da tela esta janela será exibida automaticamente, obrigando o usuário a selecionar o Grupo e Estabelecimento. O grupo e estabelecimento selecionados serão exibidos nos campos “Estabelecimento” e “Grupo”.

Caso tenha sido informado um estabelecimento no login, serão disponibilizados apenas os grupos aos quais o estabelecimento esteja associados. Caso contrário, serão disponibilizados todos os grupos e estabelecimentos da Empresa do login.

NOVO – Limpa todos os campos da tela, com exceção do estabelecimento e do grupo, permitindo a inclusão de um novo registro;

ABRE – Ao clicar nesta opção, serão exibidos para seleção do usuário todos os dados já  parametrizados para o Grupo em questão;

EXCLUI – permite a exclusão dos dados;

CONFIRMA – Salva os dados incluídos ou alterados;

RELATÓRIO – para emitir o relatório o usuário poderá selecionar um estabelecimento, e serão listados todos os dados parametrizados para o estabelecimento selecionado;

FECHA – fecha a janela da parametrização;


Neste campo será exibido o estabelecimento selecionado na janela de seleção do Grupo.


Neste campo será exibido o grupo selecionado na janela de seleção do Grupo.

(Este campo não ficará habilitado para o usuário, pois a alteração do grupo deverá ser feita sempre na opção <GRUPO> da barra de menu. O objetivo deste campo é apenas mostrar o grupo escolhido)


Este campo é uma lista dos indicadores de produto da SAFX2013:

1 - Produto
2 - Matéria Prima/Insumo
3 - Embalagem
4 - Material Uso/Consumo
5 - Outros
6 - Em Elaboração
7 - Intermediário
8 - Miscelâneas


Este campo trabalha com janela de seleção dos produtos da SAFX2013, considerando apenas os produtos do Grupo selecionado e também do indicador de produto selecionado.

Após informar o código inicial, caso o campo “Código Final” ainda não tenha sido informado, o campo do código final será inicializado com o mesmo conteúdo do produto inicial.

Quando o código for digitado, será verificada a existência do produto na tabela de produtos (SAFX2013), considerando o Grupo e o indicador informados. Caso não exista, será exibida mensagem a mensagem “Produto não Cadastrado” no campo destinado a descrição do produto.




Este campo será inicializado com o mesmo código de produto informado no campo “Código Inicial”, mas o usuário poderá alterar este conteúdo através da janela de seleção da SAFX2013 ou de digitação, assim como é feito no campo do código inicial.

Quando o código for digitado, será verificada a existência do produto na tabela de produtos (SAFX2013), considerando o Grupo e o indicador informados. Caso não exista, será exibida a mesma  mensagem já definida para o código inicial.

No momento de salvar a operação, serão realizadas algumas críticas, como descrito a seguir:

Crítica1  verifica se o código final é realmente >= código inicial. Caso não, será exibida a mensagem abaixo, e a operação não será salva:
“Código do produto final deve ser maior ou igual ao código do produto inicial”

Crítica 2  verifica se já existe outro registro na parametrização que contenha o produto informado, ou a faixa de produtos, quando for o caso (ou seja, se haverá faixas de produtos intercalados).

Exemplo I:

Registro 1   Código inicial = 1000500  Código final = 1000599
Registro 2   Código inicial = 1000600  Código final = 1000699
Registro a ser incluído   Código inicial = 1000540  Código final = 1000545

Neste exemplo, teríamos um erro na parametrização, pois a faixa do registro a ser importado já se encontra contida na faixa do registro 1.

Exemplo II:

Registro 1   Código inicial = 1000500  Código final = 1000599
Registro 2   Código inicial = 1000600  Código final = 1000900
Registro a ser incluído   Código inicial = 1000000  Código final = 1000800

Neste exemplo, também teríamos erro na parametrização, pois a faixa do registro a ser importado engloba  toda faixa do registro 1, e além disso, se intercala com a faixa do registro 2.

Quando ocorrer este tipo de problema, a operação não será salva, e será exibida a mensagem abaixo:

“Código Inicial e/ou Final já contido em outra faixa de produtos”



Através deste parâmetro o usuário poderá selecionar alguns produtos da faixa escolhida para desconsiderar da parametrização.

Ao clicar nesta opção, todos os produtos da faixa informada (código inicial ao final) serão exibidos no quadro “Produtos Excluídos da Faixa”.

Ao desmarcar a opção, todo o conteúdo do quadro “Produtos Excluídos da Faixa” será apagado.



Neste quadro serão demonstrados todos os produtos da faixa informada (código inicial ao final), e o usuário poderá selecionar os produtos que desejar para que sejam desconsiderados da parametrização.

O conteúdo deste quadro será automaticamente apagado sempre que o usuário desmarcar a opção “Informar Exclusões”.



Através desta opção o usuário poderá replicar a parametrização feita para outros estabelecimentos.

Serão disponibilizados para seleção do usuário apenas os estabelecimentos associados ao grupo selecionado (campo “Grupo”).



= = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS42617 | Andréa Rocha | Criação da parametrização de produto específica para o código 12 da DIPAM-B, para tratar a situação das notas fiscais escrituradas geradas neste registro | 04/09/2020 |
|  |  |  |  |


| RN00 | Regras Gerais |
| --- | --- |


| RN01 | Campo Estabelecimento: |
| --- | --- |


| RN02 | Campo Grupo: |
| --- | --- |


| RN03 | Campo Grupo: |
| --- | --- |


| RN04 | Campo Código Inicial: |
| --- | --- |


| RN05 | Campo Código Final: |
| --- | --- |


| RN06 | Campo Informar Exclusões: |
| --- | --- |


| RN07 | Campo Produtos Excluídos da Faixa: |
| --- | --- |


| RN08 | Campo Replicar p/os Estabelecimentos: |
| --- | --- |
