# MTZ_Parametros_para_Municipio_Tela_de_parametrizacao_Plano_de_ContasxProdutos_Servicos_DESIF

- **Fonte:** MTZ_Parametros_para_Municipio_Tela_de_parametrizacao_Plano_de_ContasxProdutos_Servicos_DESIF.docx
- **Modificado:** 2020-05-18
- **Tamanho:** 226 KB

---

THOMSON REUTERS

Módulo Parâmetros para Município

# Planos de Contas Empresa x Produtos e Serviços DESIF

__Localização__: Módulo Municipal >> Parâmetros para Município, menu: Parâmetros 🡪 Serviços Bancários 🡪 DES\-IF 🡪 Plano de Contas da Empresa x Produtos e Serviços

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS36719__

Liliane Assaf

Criação da tela de parametrização para atendimento ao módulo 3 da DES\-IF\.

13/05/2020

Sumário

[1\.	Regras Gerais	1](#_Toc37236796)

[2\.	Layout da Tela	1](#_Toc37236797)

[3\.	Regras de Funcionamento dos Campos	1](#_Toc37236798)

# <a id="_Toc37236796"></a>Regras Gerais

Esta funcionalidade tem como objetivo permitir que seja feito o relacionamento da Conta Contabíl pertencente ao Plano de Contas da Empresa com o código de Produtos e Serviços da DES\-IF, oriunda do Anexo 10\. As informações aqui carregadas são apresentadas no registro 0300 do arquivo Módulo 3 do validador da DES\-IF\.

A Tabela de Outros Produtos e Serviços \- Anexo 10 é carregada via importação da TACES105, sem possibilidade de interferência manual\.

Observação:

Esta parametrização possui datas de vigência Inicial e Final, o que permite realizar manutenção nas informações sem perda da parametrização anterior\. 

Importante atentar para o fato que se faz necessário gerar o arquivo do módulo 3, para todo período em que houver alteração nas informações de produtos e serviços aqui parametrizadas\. 

 

# <a id="_Toc37236797"></a>Layout da Tela

Data Vigência Inicial:                   \[DD/MM/AAAA\]

         

Conta Contábil \(Gr\./Cód/Data/Dsc\):    \[grupo\] \[pastinha\]  \[código                                      \]

                                                             \[dd/mm/aaaa\]       \[descrição                                             \]

Data Vigência Final:                   \[DD/MM/AAAA\]

Cod\. Produto/Serviço DES\-IF:           \[código\]  \[pastinha\] \[grupo prod/serviço \]

                                                                                          \[descrição  do produto/serviço             \]                        

Desc\. Complementar:                \[                                                                                                   \]

A chave do registro:

\- Grupo da Conta Contábil

\- Código da Conta Contábil

\- Data Vigência Inicial                

Nome da Tabela Física: PRT\_CONTA\_PSERV\_DESIF

__Botões da barra de menu__:

NOVO

Ao clicar nesta opção os dados da tela serão limpos, e o usuário poderá cadastrar um novo registro da parametrização da Conta Contábil para o Código do Produto/Serviço DES\-IF\.

ABRE

Exibe janela de pesquisa dos registros das parametrizaçoes já gravadas, para que o usuário selecione <a id="OLE_LINK4"></a>a que desejar exibir em tela\.

EXCLUI

Opção para excluir o registro da parametrização da conta contábil para o Código do Produto/Serviço DES\-IF\.

CONFIRMA

Opção para salvar os dados do registro da parametriização incluída / alterada\.

RELATÓRIO

Esta opção permite imprimir os dados das parametrizações das Contas Contábeis para os Códigos dos Produtos/Serviços DES\-IF\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da parametrização\.

  

# <a id="_Toc37236798"></a>Regras de Funcionamento dos Campos

Ao entrar na tela será disponibilizada a Tela de Seleção dos Grupos/Estabelecimento/Validade, onde os grupos são apresentados obedecendo a seguinte a regra:

Se no login foi informado estabelecimento, então:

Sistema disponibilizados apenas os grupos relacionados ao estabelecimento em questão, relacionados a Tabela do Plano de Contas \(SAFX2002\)\.

Senão

           Sistema exibe os grupos de todos os estabelecimentos da empresa, relacionados a Tabela do Plano de Contas \(SAFX2002\)\.

Após a escolha do grupo, a tela de parametrização objeto deste documento é apresentada, para que o usuário possa incluir, consultar, alterar e excluir registros da parametrização\.

Ao incluir ou alterar um registro, o sistema solicita confirmação desta operação\. Neste momento, algumas validações são executadas\. Todas estão descritas a seguir\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/__

__Default__

__Regra__

Data Vigência Inicial

Data 

__S__

S

DD/MM/AAAA

Campo de preenchimento __*obrigatório*__\.

A data informada deve ser maior ou igual a data de validade do grupo, escolhido na Tela de Seleção de Grupo\. Caso seja digitada uma data anterior a data de validade do grupo, exibir a seguinte mensagem:

*“Validade Inicial deve ser maior ou igual a Data de Validade Inicial do Grupo\.”*

Ao salvar o registro, caso a data não esteja preenchida, exibir mensagem:

*                  “Data de Vigência Inicial deve ser preenchida\.”*

Conta Contábil

Alfanumérico 

__S__

S

Pastinha \+ Grupo \+ Código \+ data de validade \+ descrição

Campo de preenchimento __*obrigatório*__\.

Origem da informação: Tabela do Plano de Contas \(SAFX2002\)\. 

A conta contábil pode ser informada utilizando a pastinha ou digitando seu código\.

A conta contábil informada terá seu cadastro recuperado através dos critérios:

\- Grupo escolhido na Tela de Seleção de Grupo

\- Data de Validade menor ou igual a Data de Vigência Inicial informada\.

Caso mais de um cadastro exista para a conta, considerar o de máxima validade, atendendo os cirtérios acima\.

Caso o código da conta digitado não seja encontrado no Cadastro do Plano de Contas da empresa \(SAFX2002\), exibir mensagem no campo descrição:

“*Conta Não Encontrada*\.”

Ao salvar o registro, caso o campo não esteja preenchido, exibir a seguinte mensagem: 

“*Conta Contabil deve ser preenchida*\.”

Ao salvar o registro, caso a conta não exista no cadastro, exibir a seguinte mensagem:  “*Conta Contabil inválida\.* ”

Data Vigência Final

Data 

N

S

DD/MM/AAAA

__Campo Data de Vigência Final__

Campo não obrigatório\.

Ao salvar o registro, executar as seguintes consistências:

Se o usuário informar uma data final de vigência menor que a data inicial de vigência, exibir a seguinte mensagem: 

*   “Data de Vigência Final não pode ser menor que Data de Vigência Inicial\.”*

Se já existir registro na base para a Conta Contábil \(grupo e código da conta\), então verificar se período formado pelas datas de vigência Inicial e Final do registro que está sendo gravado, não se intercala com o período de algum registro existente na Tabela de Parametrização do Plano de Contas da Empresa x Produtos e Serviços\.

Para isso executar o seguinte procedimento:

1\) Recuperar o registro imediatamente anterior ao que está sendo gravado:

Recuperar o registro da “Tabela de Parametrização do Plano de Contas da Empresa x Produtos e Serviços” de acordo com os seguintes critérios:

- Grupo e Código da Conta Contábil igual ao do registro ser gravado;
- Data de Vigência Inicial menor que a Data de Vigência Inicial do registro a ser gravado\.

Recuperar o registro de máxima Data de Vigência Inicial que atenda aos critérios acima\.

Caso seja encontrado registro, então comparar a Data de Vigência Final do registro recuperado com a Data de Vigência Inicial do registro a ser gravado\.

Se Data de Vigência Final do registro recuperado for nulo,

ou 

Se Data de Vigência Final do registro recuperado >= Data de Vigência Inicial do registro a ser gravado, então:

O registro não será gravado e será exibida a seguinte mensagem de erro:

*“Existe parametrizacao para esta Conta Contabil com Vigencia Inicial anterior a que esta sendo gravada e com Data de Vigencia Final nula ou maior que a Data de Vigencia Inicial a ser salva\. Favor rever a Data de Vigência Final da parametrização já existente, antes de incluir a nova parametrização\.” *

2\) Recuperar o registro imediatamente posterior ao que está sendo gravado:

Recuperar o registro da “Tabela de Parametrização do Plano de Contas da Empresa x Produtos e Serviços” de com os seguintes critérios:

- Grupo e Código da Conta Contábil igual ao do registro ser gravado;
- Data de Vigência Inicial maior que a Data de Vigência Inicial do registro a ser gravado\.

Recuperar o registro de menor Data de Vigência Inicial que atenda aos critérios acima\.

Caso seja encontrado registro, então comparar a Data de Vigência Inicial do registro recuperado com a Data de Vigência Final do registro a ser gravado\.

Se Data de Vigência Final do registro a ser gravado for nulo,

Ou

Se Data de Vigência Final do registro a ser gravado for >= Data de Vigência Inicial do registro recuperado, o registro  não será salvo e será exibida a seguinte mensagem de erro:

*“A Data de Vigência Final deve ser anterior a DD/MM/AAAA, que é a Data de Vigência Inicial da parametrização já existente na base para esta Conta Contabil\.” *

Onde *DD/MM/AAAA*: é a Data de Vigência Inicial do registro recuperado\.

Cód\. Produto/Serviço DES\-IF

Alfanumérico 

__S__

S

Pastinha \+ Código \+ grupo \+ descrição

Campo de preenchimento __*obrigatório*__\.

Origem da informação: Tabela de Outros Produtos e Serviços da DESIF – Anexo 10 \(TACES105 \- CAD\_PSERV\_DESIF\)\. 

O Produto/Serviço DES\-IF pode ser informado utilizando a pastinha ou digitando seu código\.

Caso o código digitado não seja encontrado na Tabela de Outros Produtos e Serviços da DESIF – Anexo 10, exibir mensagem no campo descrição:

“*Código de Produto/Serviço DES\-IF não cadastrado\.*”

Ao salvar o registro, caso o campo não esteja preenchido, exibir a seguinte mensagem: 

“*Código de Produto/Serviço DES\-IF deve ser preenchido*\.”

Ao salvar o registro, caso o código digitado não exista na Tabela de Outros Produtos e Serviços da DESIF – Anexo 10, exibir mensagem:

*“Código de Produto/Serviço DES\-IF não cadastrado\.”*

Desc\. Complementar

Alfanumérico

N

S

Campo não obrigatório\.

Campo de preenchimento obrigatório caso o Cód\. Produto/Serviço DES\-IF selecionado, possua Indicador de Obrigatóriedade de Complemento = ‘S’, na Tabela de Outros Produtos e Serviços da DESIF – Anexo 10 \(TACES105 \- CAD\_PSERV\_DESIF – campo IND\_OBRIG\_COMPL\)\.

Ao salvar o registro, verificar o campo IND\_OBRIG\_COMPL da tabela CAD\_PSERV\_DESIF para o Cód\. Produto/Serviço DES\-IF selecionado\. Caso esteja preenchido com “Sim”, exibir a seguinte mensagem: 

“*Descrição Complementar deve ser preenchida para o Código de Produto ou Serviço informado\.*”

![](data:image/x-emf;base64,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EQDe/xEA3v8QALb/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABEAwP8TAO3/EwDs/2FV8v//////QTPu/xIA6f8SAOn/EgDo/2FV8P//////QTPr/xIA5f9xZu///////1FE6v8SAOP/0Mz5/7Cq9f8SAOH/EgDg/xIA4P8RAN//EQDe/xAAtv8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEQDA/xMA7f8TAO3/YlXy/////////////////4F38/8SAOn/YVXw//////9BM+z/EgDm/0Ez6v//////YVXt/xIA4//QzPn////////////QzPn/EgDg/xIA4P8RAN//EAC2/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARAMH/EwDu/xMA7f9iVfP//////0Ez7/9hVfL//////1FE7/9hVfD//////0Ez7f8SAOf/cWbw//////9RROz/EgDk/9DM+f+wqvb/EgDi/xIA4v8SAOH/EgDg/xIA4P8QALf/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABEAwf8TAO//EwDu/2JV8///////QjPw/2FV8v//////YVXx/2FV8P//////QTPt/yIR6v/QzPr/3938/xIA5f8SAOX/0Mz6/7Cq9v8SAOP/EgDi/xIA4v8SAOH/EgDg/xAAt/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEQDB/xMA7/8TAO//YlX0/////////////////8C7+v8SAOv/YVXx/////////////////8C7+f9BM+z/EgDm/xIA5f/QzPr////////////v7v3/EgDi/xIA4v8SAOH/EAC3/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARAML/EwDw/xMA7/8TAO//EwDu/xMA7f8TAO3/EwDs/xIA6/8SAOv/EgDq/xIA6f8SAOn/EgDo/xIA6P8SAOf/EgDm/xIA5f8SAOX/EgDk/xIA4/8SAOP/EgDi/xIA4v8QALj/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABEAwv8TAPH/EwDw/xMA7/8TAO//EwDu/xMA7f8TAO3/EwDs/xIA6/8SAOv/EgDq/xIA6f8SAOn/EgDo/xIA6P8SAOf/EgDm/xIA5f8SAOX/EgDk/xIA4/8SAOP/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)

= = = = = =

