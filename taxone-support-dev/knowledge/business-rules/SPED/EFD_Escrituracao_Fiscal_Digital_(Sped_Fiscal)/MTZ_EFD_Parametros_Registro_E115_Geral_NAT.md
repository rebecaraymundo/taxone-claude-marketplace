# MTZ_EFD_Parametros_Registro_E115_Geral_NAT

- **Fonte:** MTZ_EFD_Parametros_Registro_E115_Geral_NAT.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 78 KB

---

THOMSON REUTERS

Módulo Sped Fiscal

Parâmetros p/ Pré\-Geração do Registro E115 por CFOP/Natureza Operação \(Geral\)

__Localização__: Menu Sped, Módulo: Escrituração Fiscal Digital, item Parâmetros 🡪 Registro E115/1925  🡪 Registro E115 \(Geral\) 🡪 CFOP/Natureza Operação

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS24915

Pré\-Geração do E115 \(Geral\)

Criação da parametrização de CFOP/Natureza da Operação para a pré\-geração do registro E115\. 

28/02/2019

MFS26565

Andréa Rocha

Inclusão de novos valores no campo Recuperação de Valores\.

03/05/2019

MFS30407

Andréa Rocha

Retirar a validação do campo estabelecimento para o estado igual a RS\.

26/09/2019

Sumário

[1\.	Introdução	2](#_Toc2189877)

[2\.	Layout da Tela	2](#_Toc2189878)

[3\.	Funcionamento da Tela	3](#_Toc2189879)

[4\.	Botões da barra de menu:	5](#_Toc2189880)

[5\.	Regras de Funcionamento dos Campos	5](#_Toc2189881)

[6\.	Validações	8](#_Toc2189882)

# <a id="_Toc2189877"></a>Introdução

Esta tela tem objetivo de promover a manutenção da parametrização dos CFOP’s/Naturezas de Operação a serem utilizados na rotina de pré\-geração do registro E115, realizada no menu “Pré\-Geração 🡪 Registro E115 \(Geral\)” do módulo Sped Fiscal\.

Esta parametrização relaciona por estabelecimento, os CFOP’s/Naturezas de Operação aos Códigos de Informação Adicional, criados no item “Parâmetro 🡪 Registros E115/1925🡪 Informações Adicionais da Apuração \(Registros E115/1925\)”, determinando o valor a ser recuperado do item de mercadoria na pré\-geração\.

A tela é praticamente a mesma disponibilizada no menu” Parâmetros 🡪 Registro E115/1925  🡪 Registro E115 \(Específico RS\) 🡪 CFOP/Natureza de Operação”, inclusive tecnicamente grava a mesma tabela \(EFD\_PAR\_EXTCFO\_E115\)\.

# <a id="_Toc2189878"></a>Layout da Tela

Estabelecimento \[XXXXXX – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

Grupo Natureza: \[XX\]

Código:        \[\.\.\.\] \[XXXX\] \[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

\-\- CFOP’s/Natureza Operação\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

         CFOP\-Código\-Descrição                            |    Recuperação de Valores       |                

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

\[ x \] xxxx \- xxxxxx\-xxxxxxxxxxxxxxx               | \[\\/\] \[Valor Base Isenta   \]    

\[ x \] xxxx \- xxxxxx\-xxxxxxxxxxxxxxx               | \[\\/\] \[Valor Base Outras  \]    

\[   \] xxxx \- xxxxxx\-xxxxxxxxxxxxxxx                | \[\\/\] \[                                \]    

\[Selecionar Todos\] \[Desmarcar Todos\]

Os dados que definem a chave de identificação da parametrização são os seguintes:

- __Empresa__
- __Estabelecimento__
- __Código__
- __CFOP__
- __Natureza da Operação__

A tabela onde a parametrização é gravada é EFD\_PAR\_EXTCFO\_E115\.

Observação: 

O campo “Gia – Anexo” fisicamente faz parte da chave da tabela, mas é apenas utilizado na parametrização do RS, opção de menu” Parâmetros 🡪 Registro E115/1925  🡪 Registro E115 \(Específico RS\) 🡪 CFOP/Natureza da Operação”\)\.

# <a id="_Funcionamento_da_Tela"></a><a id="_Toc2189879"></a>Funcionamento da Tela

__Passo__

__Acionador__

__Descrição__

1

Usuário

Usuário seleciona o item de menu Parâmetros 🡪 Registro E115/1925  🡪 Registro E115 \(Geral\) 🡪 CFOP / Natureza Operação

2

Sistema

Verifica o usuário informou estabelecimento no login do Manager\.

Se no login foi informado estabelecimento, então:

Sistema verifica a UF do Estabelecimento\.

Se a UF do Estabelecimento de login for igual a __RS__, então:

Sistema apresenta mensagem: 

“*A parametrização de CFOP/Natureza Operação para Informações Adicionas E115 não é válida para estabelecimentos do Rio Grande do Sul”*

Fecha a janela\.

Finaliza o fluxo\.

Senão

Segue o fluxo\.

Senão

Segue o fluxo\.

3

Sistema

Sistema abre a tela de seleção dos grupos cadastrados no Relacionamento entre Tabela e Grupos \(Relac\_Tab\_Grupo\)\.

Se no login foi informado estabelecimento, então:

Sistema disponibilizados apenas os grupos relacionados ao estabelecimento em questão, relacionados a Tabela Natureza de Operação\.

Senão

Sistema exibe os grupos dos estabelecimentos da empresa cuja UF seja diferente de “RS”, relacionados a Tabela Natureza de Operação\.

4

Usuário

Usuário seleciona um registro de grupo/estabelecimento do Relacionamento entre Tabela e Grupo\.

5

Sistema

Abre a tela de Parametrização de CFOP/Natureza Operação, com os campos Estabelecimento e Grupo Natureza preenchidos e bloqueados\.

Sistema monta a Relação de CFOP’s/Natureza de Operação e a lista do campo “Recuperação de Valores”\. 

Vide regras descritas no tópico “[5 – Regras de Funcionamento dos Campos](#_Regras_de_Funcionamento)”\.

6

Usuário

Usuário seleciona ou digita um Código de Informação Adicional no campo “Código”\.

7

Sistema

Valida o Código digitado\.

Vide regra do campo “Código” descrita no tópico “[5 – Regras de Funcionamento dos Campos](#_Regras_de_Funcionamento)”\.

8

Usuário

Seleciona um CFOP/Natureza de Operação e preenche o campo Recuperação de Valores\.

9

Usuário 

Seleciona botão confirma\.

10

Sistema

Executa validações descritas no tópico [5\- Validações](#_Validações)\. 

Caso os dados estejam consistentes, grava as parametrizações na tabela definitiva\.

11

Usuário

Seleciona outras ações disponíveis na barra de menu da janela\.

Vide tópico “[4 \- Botões da barra de menu](#_Botões_da_barra)”

# <a id="_Botões_da_barra"></a><a id="_Toc2189880"></a>Botões da barra de menu:

SELECIONAR GRUPO

Ao clicar nesta opção será aberta a janela de seleção dos grupos cadastrados no Relacionamento entre Tabela e Grupos \(Relac\_Tab\_Grupo\), e o usuário poderá selecionar o grupo desejado\.

Se no login foi informado estabelecimento, então:

Sistema disponibilizados apenas os grupos relacionados ao estabelecimento em questão, relacionados a Tabela Natureza de Operação\.

Senão

Sistema exibe os grupos dos estabelecimentos da empresa cuja UF seja diferente de “RS”, relacionados a Tabela Natureza de Operação\.

Seguir o *passo 4* do fluxo descrito no tópico [3 – Funcionamento da Tela](#_Funcionamento_da_Tela)\.

CONFIRMA

Opção para salvar as informações da parametrização incluída, excluída ou alterada\.

RELATÓRIO

Esta opção permite imprimir os dados da parametrização\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

  

# <a id="_Regras_de_Funcionamento"></a><a id="_Toc2189881"></a>Regras de Funcionamento dos Campos

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Estabelecimento

Alfanumérico 

__S__

__N__

Neste campo será exibido o código e a razão social do estabelecimento do Grupo selecionado pelo usuário na abertura da tela, ou através da opção “SELECIONAR GRUPO” da barra de menu\.

Grupo Natureza

Alfanumérico

__S__

__N__

Neste campo será exibido o Grupo selecionado pelo usuário na abertura da tela, ou através da opção “SELECIONAR GRUPO” da barra de menu\.

Código 

Alfanumérico

__S__

S

Formato:

Pesquisar Pasta – Seleção da Manutenção Informações Adicionais da Apuração \(Registro E115/ 1925\)

Permitir seleção da tabela dos Códigos de Informação Adicional parametrizados na Manutenção Informações Adicionais da Apuração \(Registro E115/ 1925\), item de menu Parâmetro 🡪 Registros E115/1925🡪 Informações Adicionais da Apuração \(Registros E115/1925\)\.

__Pastinha:__

- Só recuperar os códigos cuja UF seja igual a UF do Estabelecimento;

__Consistência:__

- Verificar se o código digitado existe na tabela de Informações Adicionais da Apuração \(Registro E115/ 1925\), considerando a UF do Estabelecimento\. Caso não exista, exibir a seguinte mensagem:

*Código da Informação Adicional não cadastrado para a UF do Estabelecimento\.*

__Tratamento:__

- Ao selecionar um novo Código, os CFOP’s/Natureza da Operação e 

o campo Recuperação Valores devem ser atualizados\.

__Tabela Origem:__

EFD\_INF\_ADIC\_APUR

Relação dos CFOP’s/Natureza de Operação

Alfanumérico

__S__

__S__

Neste campo é exibida a lista dos CFOP’s \(SAFX2012\) que tenham Natureza de Operação \(SAFX2006\) vinculada na SAFX2081\.

__Seleção dos CFOPs com Natureza de Operação \(SAFX2012 / SAFX2006\):__

Selecionar todos os registros de CFOP que tenham Natureza da Operação relacionada na SAFX2081\. 

Recuperar univocamente a relação do Código CFOP com o Código de Natureza de Operação\.  Caso exista mais de um registro relacionando o mesmo código CFOP com o mesmo Código de Natureza, recuperar apenas o de máxima validade\.

Do conjunto de CFOPs/Naturezas de Operação recuperados, o sistema deve ainda aplicar o seguinte tratamento:

 \- APRESENTAR MARCADO o CFOP/Natureza da Operação já parametrizado para o estabelecimento e Código de Informação Adicional informados\.

\- APRESENTAR DESMARCADO o CFOP/Natureza da Operação que não está parametrizado para o estabelecimento e Código informados\.

Para selecionar os CFOPs/Natureza da Operação, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”\. 

Recuperação de Valores          

Alfanumérico

__S__

__S__

Formato:

Combo Box

Exibir uma lista composta pela descrição dos seguintes itens:

1 \- Base Isenta ICMS

2 \- Base Outras ICMS

3 \- Base Reduzida ICMS

4 \- Base Isenta ICMS \+ Base Reduzida ICMS

5 \- Base Outras ICMS \+ Valor do ICMS\-S

6 \- Valor Desonerado ICMS

7 \- Valor Diferido ICMS

 

MFS26565

Replicar para os Estabelecimentos

Alfanumérico

N

S

Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados\.

Serão exibidos para seleção *apenas* os estabelecimentos da mesma empresa do estabelecimento parametrizado, do mesmo Grupo informado, e da mesma UF do Estabelecimento informado\.

Para selecionar os estabelecimentos, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”\.

# <a id="_Validações"></a><a id="_Toc517344573"></a>

# <a id="_Toc2189882"></a>Validações

__Críticas a serem realizadas antes de salvar a operação:__

- __RN01: Campos Obrigatórios__

Validações de Campos Obrigatórios não preenchidos\.

Quando o campo é obrigatório e não estiver preenchido, exibir mensagem padrão\.

A obrigatoriedade dos campos está definida no tópico “[5 – Regras de Funcionamento dos Campos](#_Regras_de_Funcionamento)”\.

       = = = = = =

