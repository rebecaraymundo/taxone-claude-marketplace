# MTZ_Parametros_para_Municipio_Tela_de_parametrizacao_Plano_de_ContasxTarifas_Bancarias_DESIF

- **Fonte:** MTZ_Parametros_para_Municipio_Tela_de_parametrizacao_Plano_de_ContasxTarifas_Bancarias_DESIF.docx
- **Modificado:** 2020-05-06
- **Tamanho:** 79 KB

---

THOMSON REUTERS

Módulo Parâmetros para Município

# Planos de Contas Empresa x Tarifas Bancárias DESIF

__Localização__: Módulo Municipal >> Parâmetros para Município, menu: Parâmetros 🡪 Serviços Bancários 🡪 DES\-IF 🡪 Plano de Contas da Empresa x Tarifas Bancárias

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS33130__

Liliane Assaf

Criação da tela de parametrização para atendimento ao módulo 3 da DES\-IF\.

05/05/2020

Sumário

[1\.	Regras Gerais	1](#_Toc37236796)

[2\.	Layout da Tela	1](#_Toc37236797)

[3\.	Regras de Funcionamento dos Campos	1](#_Toc37236798)

# <a id="_Toc37236796"></a>Regras Gerais

Esta funcionalidade tem como objetivo permitir que seja feito o relacionamento da Conta Contabíl pertencente ao Plano de Contas da Empresa com o código da Tarifa Bancária, oriunda do Anexo 9 da DESIF\. As informações aqui carregadas são apresentadas no registro 0200 do arquivo Módulo 3 do validador da DES\-IF\.

A Tabela de Tarifas Bancárias é carregada via importação da TACES104, sem possibilidade de interferência manual\.

Observação:

Esta parametrização possui datas de vigência Inicial e Final, o que permite realizar manutenção nas informações das tarifas bancárias da conta contábil sem perda da parametrização anterior\. 

Importante atentar para o fato que se faz necessário gerar o arquivo do módulo 3, para todo período em que houver alteração nas informações de tarifas bancárias aqui parametrizadas\. 

 

# <a id="_Toc37236797"></a>Layout da Tela

Data Vigência Inicial:                   \[DD/MM/AAAA\]

         

Conta Contábil \(Gr\./Cód/Data/Dsc\):    \[grupo\] \[pastinha\] \[código                                      \]

                                                             \[dd/mm/aaaa\]       \[ descrição                                \]

Data Vigência Final:                   \[DD/MM/AAAA\]

Cod\. Tarifa Bancária:                 \[código\]  \[pastinha\] 

                                                   \[grupo da tarifa \] \[descrição  da tarifa bancária            \]                        

Vlr\. Unitário Tabelado:               \[             0,00\]

Vlr\. Percentual Tabelado:          \[             0,00 % \]

A chave do registro:

\- Grupo da Conta Contábil

\- Código da Conta Contábil

\- Data Vigência Inicial                

Nome da Tabela Física: PRT\_CONTA\_TARIFA\_DESIF

__Botões da barra de menu__:

NOVO

Ao clicar nesta opção os dados da tela serão limpos, e o usuário poderá cadastrar um novo registro da parametrização da Conta Contábil para a Tarifa Bancária\.

ABRE

Exibe janela de pesquisa dos registros das parametrizaçoes já gravadas, para que o usuário selecione <a id="OLE_LINK4"></a>a que desejar exibir em tela\.

EXCLUI

Opção para excluir o registro da parametrização da conta contábil para a tarifa bancária\.

CONFIRMA

Opção para salvar os dados do registro da parametriização incluída / alterada\.

RELATÓRIO

Esta opção permite imprimir os dados das parametrizações das Contas Contábeis para Tarifas Bancárias\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

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

*“Data deVigência Inicial deve ser maior ou igual a Data de Validade Inicial do Grupo\.”*

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

Se já existir registro na base para a Conta Contábil \(grupo e código da conta\), então verificar se período formado pelas datas de vigência Inicial e Final do registro que está sendo gravado, não se intercala com o período de algum registro existente na Tabela de Parametrização do Plano de Contas da Empresa x Tarifas Bancárias\.

Para isso executar o seguinte procedimento:

1\) Recuperar o registro imediatamente anterior ao que está sendo gravado:

Recuperar o registro da “Tabela de Parametrização do Plano de Contas da Empresa x Tarifas Bancárias” de acordo com os seguintes critérios:

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

Recuperar o registro da “Tabela de Parametrização do Plano de Contas da Empresa x Tarifas Bancárias” de com os seguintes critérios:

- Grupo e Código da Conta Contábil igual ao do registro ser gravado;
- Data de Vigência Inicial maior que a Data de Vigência Inicial do registro a ser gravado\.

Recuperar o registro de menor Data de Vigência Inicial que atenda aos critérios acima\.

Caso seja encontrado registro, então comparar a Data de Vigência Inicial do registro recuperado com a Data de Vigência Final do registro a ser gravado\.

Se Data de Vigência Final do registro a ser gravado for nulo,

Ou

Se Data de Vigência Final do registro a ser gravado for >= Data de Vigência Inicial do registro recuperado, o registro  não será salvo e será exibida a seguinte mensagem de erro:

*“A Data de Vigência Final deve ser anterior a DD/MM/AAAA, que é a Data de Vigência Inicial da parametrização já existente na base para esta Conta Contabil\.” *

Onde *DD/MM/AAAA*: é a Data de Vigência Inicial do registro recuperado\.

Cód\. Tarifa Bancária

Alfanumérico 

__S__

S

Pastinha \+ Código \+ grupo \+ descrição

Campo de preenchimento __*obrigatório*__\.

Origem da informação: Tabela do Tarifas Bancárias DESIF – Anexo 9 \(TACES104 \- CAD\_TARIFA\_DESIF\)\. 

A Tarifa pode ser informada utilizando a pastinha ou digitando seu código\.

Caso o código digitado não seja encontrado na Tabela de Tarifas Bancárias DESIF, exibir mensagem no campo descrição:

“*Código da Tarifa Bancária não cadastrado*”

Ao salvar o registro, caso o campo não esteja preenchido, exibir a seguinte mensagem: 

“*Código da Tarifa Bancária deve ser preenchido*\.”

Vlr\. Unitário Tabelado

Numérico 

N

S

0,00

Campo não obrigatório\.

Vlr\. Percentual Tabelado

Numérico 

N

S

0,00 %

Campo não obrigatório\.

= = = = = =

