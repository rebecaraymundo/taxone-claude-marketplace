# MTZ-ICMS-Transporte-de-Saldos-Apur-ICMS

- **Fonte:** MTZ-ICMS-Transporte-de-Saldos-Apur-ICMS.docx
- **Modificado:** 2023-12-20
- **Tamanho:** 70 KB

---

 

THOMSON REUTERS

Módulo ICMS

Transporte de Saldos da Apuração do ICMS

__Localização__: Menu Estadual, Módulo: ICMS, menu Apuração à Apuração do ICMS à Transporte de Saldos à ICMS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS592951

Andréa Rocha

Inclusão da verificação do status do livro para permitir a alteração do saldo credor a transportar\. 

20/12/2023

\(criação do documento\)

Sumário

[1\.	Regras de Funcionamento da Tela	3](#_Toc153984020)

[2\.	Regras Específicas dos Campos	5](#_Toc153984021)

__Botões da barra de menu__:

NOVO

Esta opção permite a inclusão de um novo registro\.

ABRE

Quando o usuário clicar nesta opção, será aberta a janela para seleção da apuração para a qual será cadastrado ou consultado o valor do saldo credor\.

Nela serão exibidas as apurações dos livros 108 e 165 com calendário agendado nas seguintes condições:

\- Empresa = empresa do login;

\- Estabelecimento = estabelecimento do login, quando for o caso, ou todos os estabelecimentos da empresa;

\- Obrigação Fiscal = “108” ou 165;

\- Obrigação agendada \(que tenha calendário na tabela CALEND\_OBRIGACAO\), já gerada *ou não*; 

	

CONFIRMA

Opção para salvar as informações incluídas/alteradas\.

FECHA

Fecha a tela

  

# <a id="_Toc153984020"></a>Regras de Funcionamento da Tela

Na abertura da tela será exibida uma janela para seleção da apuração \(é o mesmo procedimento da opção <ABRE>\)\.

Nela serão exibidas as apurações dos livros 108 e 165 com calendário agendado nas seguintes condições:

     \- Empresa = empresa do login;

     \- Estabelecimento = estabelecimento do login, quando for o caso, ou todos os estabelecimentos da empresa;

     \- Obrigação Fiscal = “108” ou 165;

     \- Obrigação agendada \(que tenha calendário na tabela CALEND\_OBRIGACAO\), já gerada *ou não*; 

Após a escolha da apuração, serão realizados os seguintes procedimentos:

   \- O estabelecimento, a obrigação fiscal e a data da apuração escolhida serão exibidos na tela;

     Essas informações serão recuperadas da “Tabela da Apuração ICMS” da seguinte forma:

          \- Empresa = empresa do login;

          \- Estabelecimento = estabelecimento da apuração escolhida;

          \- Obrigação Fiscal = “108” ou “165”, de acordo com a obrigação selecionada;

          \- Data da Apuração = data da apuração escolhida; 

     Caso a pesquisa acima não retorne nenhum dado, a aba das Operações ficará vazia\.

__\[MFS592951\] __Inclusão da verificação do status do livro/data de apuração selecionados

Ao recuperar o registro selecionado, deve\-se verificar o status da apuração informada no módulo de Controle de Obrigações Estaduais, no item de menu Atualização > Status das Obrigações\.

Verificar para a empresa, o estabelecimento, a obrigação fiscal e a data da apuração, os campos situação e validade:

 Se o campo situação = “Apuração Realizada” e o campo validade = “Válido”

      O valor do saldo credor não poderá ser alterado\.  O valor será demonstrado na Aba Operações, mas sem a opção de alteração\. 

 Senão \(Para as demais combinações de situação e validade, o valor poderá ser alterado\.

__A seguir o usuário terá as seguintes opções:__

     \- Usar o botão <__NOVO__> para incluir uma nova Operação com seu respectivo valor;

     \- Usar o botão <CONFIRMA> para atualizar os dados incluídos/alterados;

__Ao clicar na opção <CONFIRMA> a atualização dos dados será feita da seguinte forma__:

Os dados serão atualizados na “Tabela da Apuração ICMS” da seguinte forma:

\- Para cada estabelecimento será gravado um registro na tabela\. *Caso o registro já exista*, será atualizado com o valor do saldo credor

  informado;

\- Os estabelecimentos que já tinham o saldo credor informado, e cujo valor foi alterado pelo  usuário, serão atualizados na tabela com o valor do novo saldo informado \(que poderá ser = zeros\);

Para atualizar os dados da tabela, considerar: 

     \- Empresa = empresa do login;

     \- Estabelecimento = estabelecimento da apuração escolhida;

     \- Obrigação Fiscal = “108” ou “165”, de acordo com a obrigação selecionada;

     \- Data da Apuração = data da apuração escolhida; 

Campo de valor a ser atualizado com o saldo informado para o ICMS para o código de operação = ’014’à “*Valor Apuração”*

# <a id="_Toc153984021"></a>Regras Específicas dos Campos

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Estabelecimento

Alfanumérico 

S

N

Neste campo será exibido o código e a razão social do estabelecimento da apuração escolhida pelo usuário\.

O campo fica sempre desabilitado, e para mudar de estabelecimento o usuário deve clicar na opção <ABRE> e escolher uma nova apuração\.

* *

Obrigação Fiscal

Alfanumérico

S

N

Neste campo será exibido o código da obrigação fiscal \(“108” ou “165”\) e a descrição deste tipo de livro fiscal \(conforme layout da tela\), e a informação __não__ poderá ser alterada pelo usuário\.

Data Apuração

Data

S

N

Neste campo será exibida a data da apuração escolhida pelo usuário\.

O campo fica sempre desabilitado, e para mudar de data o usuário deve clicar na opção <ABRE> e escolher uma nova apuração\.

Saldo credor a transportar p/o período seguinte

Numérico

N

S

Neste campo será informado o valor do saldo credor a transportar\.

       = = = = = =

