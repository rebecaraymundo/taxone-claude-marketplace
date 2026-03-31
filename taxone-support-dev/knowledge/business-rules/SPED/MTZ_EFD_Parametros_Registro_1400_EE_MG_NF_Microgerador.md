# MTZ_EFD_Parametros_Registro_1400_EE_ MG_NF_Microgerador

> Fonte: MTZ_EFD_Parametros_Registro_1400_EE_ MG_NF_Microgerador.docx






THOMSON REUTERS

Módulo Sped Fiscal

Parâmetros de Produtos p/ Geração do Registro 1400


Localização: Menu Sped, Módulo: Escrituração Fiscal Digital, item Parâmetros à Registro 1400  à Serviço de Energia Elétrica à MG à Nota Fiscal Microgerador



DOCUMENTO DE REQUISITO


Sumário

1.	Introdução	2
2.	Layout da Tela	2
3.	Funcionamento da Tela	2
4.	Botões da barra de menu:	3
5.	Regras de Funcionamento dos Campos	3
6.	Validações	4





















## Introdução


Essa tela tem como objetivo permitir ao usuário parametrizar as seguintes informações: CFOP, Código de Produto e Código Situação Tributária B. As informações parametrizadas devem ser consideradas no filtro de recuperação de notas fiscais de saída (Emissão Própria), que irão compor o cálculo do valor do registro 1400, a serem utilizados na rotina de geração do registro 1400, formato  Específico por UF (Estado de Minas Gerais) para Energia Elétrica, realizada no menu “Geração à Meio Magnético” do módulo Sped Fiscal.


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


= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS45370 | Aline Melo | Criação da tela de manutenção de nota fiscal microgrador, para o cálculo da  geração do 1400, formato Especifico por UF, para o Estado de Minas Gerais. | 16/07/2021 |
|  |  |  |  |
|  |  |  |  |


| Passo | Acionador | Descrição |
| --- | --- | --- |
| 1 | Usuário | Usuário seleciona o item de menu Parâmetros à Registro 1400  à Serviço Energia Elétrica à MG à Nota Fiscal Microgerador |
| 2 | Sistema | Verifica se o usuário informou estabelecimento no login do Manager. |
| 3 | Sistema | Abre a tela de MG – Nota Fiscal Microgerador, com o campo Estabelecimento preenchido e bloqueado. Os campos Período, CFOP, Produto, Sit. Tributária A e Valor Total são apresentados “em branco”. |
| 4 | Usuário | Digita ou seleciona na pastinha o CFOP. |
| 5 | Sistema | Valida o CFOP na Tabela de Códigos Fiscais (SAFX2012). |
| 6 | Usuário | Digita ou seleciona na pastinha o Código do Produto. |
| 7 | Sistema | Valida o Código do Produto na Tabela de Produto (SAFX2013). |
| 8 | Usuário | Digita ou seleciona na pastinha a Situação Tributária B |
| 9 | Sistema | Valida a Situação Tributária B na Tabela Situação Tributária Estadual “B”. |
| 10 | Usuário | Usuário informa o valor total. |


| NOVO | Ao clicar nesta opção, as informações dos campos serão limpas (exceto os campos Estabelecimento e Grupo que mantém preenchidos e bloqueados) e o usuário poderá incluir uma nova parametrização. |
| --- | --- |
| ABRE | Ao clicar nesta opção, será aberta a janela para seleção dos registros já cadastradas para consulta ou manutenção. |
| EXCLUI | Esta opção permite a exclusão dss registros do estabelecimento. |
| CONFIRMA | Opção para salvar as informações do registro incluído ou alterado. |
| RELATÓRIO | Esta opção permite imprimir os dados do registro. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | N |  | Neste campo será exibido o código e a razão social do estabelecimento. Somente devem ser mostrados os estabelecimentos do estado de “MG”. |  |
| CFOP | Alfanumérico | S | S | Pasta – Código – Descrição | Este campo trabalha com janela de seleção de CFOP da SAFX2012. Quando o código for digitado, será verificada a existência do CFOP na Tabela de Códigos Fiscais (SAFX2012). |  |
| Produto | Alfanumérico | S | S | Pasta – Código – Descrição | Este campo trabalha com janela de seleção de produtos/mercadoria da SAFX2013. Quando o código do digitado, será verificada a existencia do produto Tabela de Produto (SAFX2013). |  |
| Sit. Tributária B | Alfanumérico | S | S | Pasta – Código – Descrição | Este campo trabalha com janela de seleção de Situação Tributária “B”. Quando o código do digitado, será verificada a existencia do código na Tabela Situação Tributária Estadual “B”. |  |
| Replicar para os Estabelecimentos | Alfanumérico | N | S |  | Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados. Serão exibidos para seleção apenas os estabelecimentos da mesma empresa do estabelecimento parametrizado e do mesmo Grupo informado.  Para selecionar os estabelecimentos, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. |  |
| COD_PARAM | Alfanumérico |  |  |  | Esse campo não deve ser demonstrado na tela nem no relatório.  Gravar o registro com COD_PARAM = 812   Esse código é carregado pela TFIX31. |  |
