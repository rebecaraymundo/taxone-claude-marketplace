# MTZ-Tela_Parâmetro_Código_Tributação_por_Municipio

> Fonte: MTZ-Tela_Parâmetro_Código_Tributação_por_Municipio.docx






THOMSON REUTERS

Parâmetros p/ Município



Parâmetro de Código de Tributação p/ Município


Localização: Menu Municipal, módulo Parâmetros por Município à Código de Tributação p/ Municipio


DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	1
2.	Layout da Tela	1
3.	Regras de Funcionamento dos Campos	1



## Regras Gerais


Esta funcionalidade tem como objetivo implementar a tela de parametrização para possibilitar ao cliente realizar o DE/PARA entre o Código de Serviço da Lei Complementar 116/03 e o Código de Tributação, essa solução está sendo criada, conforme alteração de preenchimento da Tag <ItemListaServiço> para o validador FINTELLISS, pela prefeitura de Juiz de Fora, porém poderá ser utilizada para outras Prefeituras, bem como outros validadores.

## Layout da Tela




Nome da Tabela Física: PRT_COD_TRIB_MUNIC

Campos da Tabela:

COD_ESTADO;
COD_MUNICIPIO;
COD_SERVICO;
COD_SERV_LEI_116;
COD_TRIBUTACAO_MUNIC;
DATA_VIGENCIA_INI;
DATA_VIGENCIA_FIM.


Campos chave
++
- UF
- Código de Município
- Código de Serviço
- Código Lei 116
- Data Vigência Inicial

Botões da barra de menu:



## Regras de Funcionamento dos Campos



Começo neste tópico descrevendo de forma geral, como os módulos municipais funcionam.
No Manager, o usuário seleciona no grupo dos Municipais,  o módulo do município que deseja acessar. Exemplo JUIZ DE FORA.
A partir do módulo selecionado no manager, o sistema verifica os validadores que são relacionados ao município do módulo. Há municípios com apenas um validador, como há também os com mais de um validador, pois ao longo do tempo um validador foi substituído por outro.
Caso o município tenha mais de um validador, o sistema abre o módulo do município e disponibiliza uma tela com os validadores, para que o usuário escolha qual irá trabalhar.  Caso o município só tenha um validador, essa tela não é aberta.
Os itens de menu disponível no módulo são determinados pelo validador. Cada validador tem seu grupo de funcionalidades e esta informação é carregada pela TFIX105 (tabela PRT_VALIDADOR_MUNIC).

No caso da tela de Parâmetro de Código de Tributação por Município:


Ao acessar essa tela através do menu “Manutenção à módulo Parâmetros para Município à Códigos de Tributação p/ Muncipio à Parâmetro de Código de Tributação p/ Município, o sistema deve verificar se o estabelecimento foi informado no login do Manager, o sistema deverá recuperar o grupo relacionado ao estabelecimento em questão, da Tabela de Código de Serviço (SAFX2018).

Senão
Sistema exibe os grupos de todos os estabelecimentos da empresa, relacionados a Tabela de Código de Serviço (SAFX2018).

Após o usuário poderá incluir, consultar, alterar e excluir registros da parametrização.

Ao incluir ou alterar um registro, o sistema solicita confirmação desta operação. Neste momento, algumas validações são executadas. Todas estão descritas a seguir.





Obs¹.: Ao efetuar um novo parâmetro e já existir um registro com as mesmas chaves apresentar a seguinte mensagem: Já existe Registro com a chave informada, favor preencher a Data Vigência Final.

Obs².: Caso o usuário for replicar as parametrizações para outros Municípios e a tabela TACES111 não estiver parametrizado para o Município selecionado apresentar a seguinte mensagem: Caso o código de Tributação p/ Município não esteja previamente cadastrado para o Município selecionado,  favor efetuar a parametrização no caminho: BÁSICOS > FERRAMENTAS >  Tabelas Internas > Manter > Tabelas > Código de Tributação p/ Município. Deseja continuar:


= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS515567 | Rogério Ohashi | Criação da tela de Parâmetro de Código de Tributação p/ Município | 11/05/2023 |
|  |  |  |  |


| NOVO | Ao clicar nesta opção os dados da tela serão limpos, e o usuário poderá cadastrar um novo parâmetro de Código de Tributação para um Novo Município. |
| --- | --- |
| ABRE | Exibe janela de pesquisa do parâmetro de UF/Municípios já cadastrados. |
| EXCLUI | Opção para excluir o parâmetro de UF/Municípios cadastrados. |
| CONFIRMA | Opção para salvar os dados |
| RELATÓRIO | Esta opção permite imprimir os dados dos parâmetros existentes de UF/Municípios. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/ Default | Regra |
| --- | --- | --- | --- | --- | --- |
| UF | Alfanumérico | S | S |  | Este campo deverá ser exibido a “UF” devendo ser um combo Box e deverá exibir todas as UF’s cadastradas na tabela ESTADO. |
| Município | Alfanumérico | S | S |  | Este campo deverá recuperar a informações da tabela MUNICIPIO. A recuperação dos municípios deve ser realizada através da pastinha amarela ou por digitação. Quando a recuperação for realizada por digitação, deve-se recuperar apenas os municípios pertencentes ao Estado informado no campo UF. |
| Código de Serviço | Alfanumérico | N | S |  | Este campo deverá ser exibido com a tabela de Código de Serviço (X2018_SERVICOS), conforme escolha do usuário.  Obs.: O Campo de Código de Serviço deverá ser Chave, porém de preenchimento Não Obrigatório.  Obs.: Se caso o Código de Serviço for preenchido o sistema não deverá permitir incluir códigos da Lei 116 diferente para o mesmo código de serviço: conforme exemplo abaixo:     A situação acima não poderá ocorrer.  Deverá permitir somente na situação abaixo: |
| Código Lei 116 | Alfanumérico | S | S |  | Caso o usuário selecione a informação de código de serviço, o sistema deverá recuperar, automaticamente, a informação de Lei 116 do campo Cod_Serv_lei_116 da tabela X2018_SERVICOS e o campo deverá ficar desabilitado.  Senão Se o campo de Código de Serviço não for preenchido, este campo deverá ser exibido com a informação da tabela “DWT_SERVICO_LEI_116”, Campo “COD_SERV_LEI_116”, conforme escolha do usuário. |
| Código de Tributação | Alfanumérico | S | S |  | Este campo deverá ser exibido com a tabela “CAD_TRIBUTACAO_MUNIC”, Campo “COD_TRIBUTACAO_MUNIC” (TACES111), conforme escolha do usuário. |
| Data Vigência Inicial | Date | S | S | 00000000 | Data Inicial de Vigência. |
| Data Vigência Final | Date | N | S | 00000000 | Data Final de Vigência. |
