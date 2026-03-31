# MTZ_EFD_Parametros_Registro_E115_Geral_CFOP

- **Fonte:** MTZ_EFD_Parametros_Registro_E115_Geral_CFOP.docx
- **Modificado:** 2026-03-13
- **Tamanho:** 79 KB

---

THOMSON REUTERS

Módulo Sped Fiscal

Parâmetros p/ Pré\-Geração do Registro E115 por CFOP \(Geral\)

__Localização__: Menu Sped, Módulo: Escrituração Fiscal Digital, item Parâmetros 🡪 Registro E115/1925  🡪 Registro E115 \(Geral\) 🡪 CFOP

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS24914

Pré\-Geração do E115 \(Geral\)

Criação da parametrização de CFOP para a pré\-geração do registro E115\. 

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

Esta tela tem objetivo de promover a manutenção da parametrização dos CFOP’s a serem utilizados na rotina de pré\-geração do registro E115, realizada no menu “Pré\-Geração 🡪 Registro E115 \(Geral\)” do módulo Sped Fiscal\.

Esta parametrização relaciona por estabelecimento, os CFOP’s aos Códigos de Informação Adicional, criados no item “Parâmetro 🡪 Registros E115/1925🡪 Informações Adicionais da Apuração \(Registros E115/1925\)”, determinando o valor a ser recuperado do item de mercadoria na pré\-geração\.

A tela é praticamente a mesma disponibilizada no menu” Parâmetros 🡪 Registro E115/1925  🡪 Registro E115 \(Específico RS\) 🡪 CFOP”, inclusive tecnicamente grava a mesma tabela \(EFD\_PAR\_CFO\_E115\)\.

# <a id="_Toc2189878"></a>Layout da Tela

Estabelecimento \[XXXXXX – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

Código:        \[\.\.\.\] \[XXXX\] \[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

\-\- CFOP’s \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

         Código\-Descrição                   |   Recuperação de Valores          | 

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

\[ x \] x \-xxxxxxxxxxxxxxxxxx         |  \[\\/\] \[Valor Base Isenta  \]  

\[ x \] x \-xxxxxxxxxxxxxxxxxx         |  \[\\/\] \[Valor Base Outras  \]

\[Selecionar Todos\] \[Desmarcar Todos\]

Os dados que definem a chave de identificação da parametrização são os seguintes:

- __Empresa__
- __Estabelecimento__
- __Código__
- __CFOP__

A tabela onde a parametrização é gravada é EFD\_PAR\_CFO\_E115\.

Observação: 

O campo “Gia – Anexo” fisicamente faz parte da chave da tabela, mas é apenas utilizado na parametrização do RS, opção de menu” Parâmetros 🡪 Registro E115/1925  🡪 Registro E115 \(Específico RS\) 🡪 CFOP”\)\.

# <a id="_Funcionamento_da_Tela"></a><a id="_Toc2189879"></a>Funcionamento da Tela

__Passo__

__Acionador__

__Descrição__

1

Usuário

Usuário seleciona o item de menu Parâmetros 🡪 Registro E115/1925  🡪 Registro E115 \(Geral\) 🡪 CFOP

2

Sistema

Verifica o usuário informou estabelecimento no login do Manager\.

Se no login foi informado estabelecimento, então:

Sistema verifica a UF do Estabelecimento\.

Se a UF do Estabelecimento de login for igual a __RS__, então:

Sistema apresenta mensagem: 

“*A parametrização de CFOP para Informações Adicionas E115 não é válida para estabelecimentos do Rio Grande do Sul”*

Fecha a janela\.

Finaliza o fluxo\.

Senão

Segue o fluxo\.

Senão

Segue o fluxo\.

3

Sistema

Abre a tela de Parametrização de CFOP\.

Se no login foi informado estabelecimento, então:

Sistema apresenta o campo Estabelecimento bloqueado e preenchido com o estabelecimento de login\.

Senão

Sistema apresenta o campo Estabelecimento desbloqueado e com a lista de estabelecimentos de UF <> RS\.

Sistema monta a Relação de CFOP’s e a lista do campo “Recuperação de Valores”\. 

Vide regras descritas no tópico “[5 – Regras de Funcionamento dos Campos](#_Regras_de_Funcionamento)”\.

4

Usuário

Usuário seleciona ou digita um Código de Informação Adicional no campo “Código”\.

5

Sistema

Valida o Código digitado\.

Vide regra do campo “Código” descrita no tópico “[5 – Regras de Funcionamento dos Campos](#_Regras_de_Funcionamento)”\.

6

Usuário

Seleciona um CFOP e preenche o campo Recuperação de Valores\.

7

Usuário 

Seleciona botão confirma\.

8

Sistema

Executa validações descritas no tópico [5\- Validações](#_Validações)\. 

Caso os dados estejam consistentes, grava as parametrizações na tabela definitiva\.

9

Usuário

Seleciona outras ações disponíveis na barra de menu da janela\.

Vide tópico “[4 \- Botões da barra de menu](#_Botões_da_barra)”

# <a id="_Botões_da_barra"></a><a id="_Toc2189880"></a>Botões da barra de menu:

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

S

Formato:

Combo Box

Lista exibindo o código e a razão social dos estabelecimentos\.

Campo ficará habilitado ou bloqueado dependendo do estabelecimento de login\.

Se no login foi informado estabelecimento, então:

Sistema apresenta o campo Estabelecimento bloqueado e preenchido com o estabelecimento de login\.

Senão

Sistema apresenta o campo Estabelecimento desbloqueado e com a lista de estabelecimentos de UF <> RS\.

__Tratamento:__

- Ao selecionar um novo estabelecimento, o campo Código deve ser limpo e consequentemente os CFOP’s devem ser desmarcados e campo Recuperação de Valores anulado\.

MFS30407

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

- Ao selecionar um novo Código, os CFOP’s e o campo Recuperação Valores devem ser atualizados\.

__Tabela Origem:__

EFD\_INF\_ADIC\_APUR

Relação dos CFOP’s

Alfanumérico

__S__

__S__

Neste campo é exibida a lista dos CFOP’s \(SAFX2012\) para seleção do usuário\.

__Seleção dos CFOPs no Cadastro \(SAFX2012\):__

Selecionar todos os registros de CFOP da tabela\.  Caso exista mais de um registro de mesmo código CFOP, recuperar apenas o de máxima validade\.

Do conjunto de CFOPs recuperados, o sistema deve ainda aplicar o seguinte tratamento:

 \- APRESENTAR MARCADO o CFOP já parametrizado para o estabelecimento e Código de Informação Adicional informados\.

\- APRESENTAR DESMARCADO o CFOP que não está parametrizado para o estabelecimento e Código informados\.

Para selecionar os CFOPs, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”\.

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

Serão exibidos para seleção *apenas* os estabelecimentos da mesma empresa do estabelecimento parametrizado e da mesma UF do Estabelecimento informado\.

Para selecionar os estabelecimentos, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”\.

# <a id="_Validações"></a><a id="_Toc517344573"></a>

# <a id="_Toc2189882"></a>Validações

__Críticas a serem realizadas antes de salvar a operação:__

- __RN01: Campos Obrigatórios__

Validações de Campos Obrigatórios não preenchidos\.

Quando o campo é obrigatório e não estiver preenchido, exibir mensagem padrão\.

A obrigatoriedade dos campos está definida no tópico “[5 – Regras de Funcionamento dos Campos](#_Regras_de_Funcionamento)”\.

       = = = = = =

