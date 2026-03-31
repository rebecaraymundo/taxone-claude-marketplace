# MTZ_EFD_Parametros_Registro_1400_EE_MG_Deducao_Cliente_Cativo

> Fonte: MTZ_EFD_Parametros_Registro_1400_EE_MG_Deducao_Cliente_Cativo.docx






THOMSON REUTERS

Módulo Sped Fiscal

Parâmetros de Produtos p/ Geração do Registro 1400


Localização: Menu Sped, Módulo: Escrituração Fiscal Digital, item Parâmetros  Registro 1400   Serviço de Energia Elétrica  MG Dedução Cliente Cativo



DOCUMENTO DE REQUISITO


Sumário

1.	Introdução	3
2.	Layout da Tela	3
3.	Funcionamento da Tela	3
4.	Botões da barra de menu:	4
5.	Regras de Funcionamento dos Campos	4
6.	Validações	5





















## Introdução


Esta tela tem objetivo permitir ao usuário informar o valor total apurado por município, referente a dedução cliente cativo. Os valores informados por municipio, irão compor o cálculo do registro 1400, a serem utilizados na rotina de geração do registro 1400, formato  Específico por UF (Estado de Minas Gerais) para Energia Elétrica, realizada no menu “Geração  Meio Magnético” do módulo Sped Fiscal.


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
| MFS45370 | Aline Melo | Criação da tela de manutenção de dedução de cliente cativo, para o cálculo da  geração do 1400, formato Especifico por UF, para o Estado de Minas Gerais. | 16/07/2021 |
|  |  |  |  |
|  |  |  |  |


| Passo | Acionador | Descrição |
| --- | --- | --- |
| 1 | Usuário | Usuário seleciona o item de menu Parâmetros  Registro 1400   Serviço Energia Elétrica  MG  Dedução Cliente Cativo |
| 2 | Sistema | Verifica se o usuário informou estabelecimento no login do Manager. |
| 3 | Sistema | Abre a tela de Dedução Cliente Cativo, com os campos Estabelecimento preenchido e bloqueado. Os campos Período, Municipio e Valor Apurado são apresentados “em branco”. A UF do campo Município vem preenchido com a UF do Estabelecimento logado. |
| 4 | Usuário | Digita o período inicial e final. |
| 5 | Usuário | Digita ou seleciona na pastinha o município. |
| 6 | Sistema | Valida o Município no Cadastro de Municípios (SAFX2097). |
| 7 | Usuário | Usuário informa o valor apurado. |


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
| Período | Numérico | S | S | Text Box | Neste campo o usuário deve informar a data inicial e data final, referente ao período do registro. O formato deve ser dd/mm/aaaa. |  |
| Município | Alfanumérico | S | S | Pasta – Código – Descrição | Este campo trabalha com janela de seleção dos municípios da SAFX2097, considerando apenas os municípios da UF informada no campo.   Quando o código for digitado, será verificada a existência do município na tabela de municípios (SAFX2097). |  |
| Valor Apurado | Numérico | S | S | Text Box | Neste campo o usuário deve informar o valor apurado. |  |
| COD_PARAM | Alfanumérico |  |  |  | Esse campo não deve ser demonstrado na tela nem no relatório.  Gravar o registro com COD_PARAM = 811   Esse código é carregado pela TFIX31. |  |
