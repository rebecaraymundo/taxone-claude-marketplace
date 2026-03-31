# MTZ-Ressarc-RS-IN087_2020_Parametrizacao_Dados_Iniciais

- **Fonte:** MTZ-Ressarc-RS-IN087_2020_Parametrizacao_Dados_Iniciais.docx
- **Modificado:** 2023-06-19
- **Tamanho:** 90 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS

__\(IN\-RE 048/2018\)__

Parametrização dos Dados Iniciais

__Localização__: Menu Estadual, módulo Ressarcimento de ICMS\-ST \- RS \(IN\-RE 048/2018\), menu Parâmetros 🡪 IN\-RE 087/2020 🡪 Dados Iniciais

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS65137__

Liliane Videira Assaf

Criação da Tela de Dados Iniciais, transferindo os parâmetros da Tela de Geração do Movimento para esta tela\. São eles:

\- Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)

\- Tratamento p/ Entrada objeto da Devolução de períodos anteriores à adoção da sistemática da IN\-RE 087/20:

Valores Unitários Médios recuperados:

\( \) do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)

\( \) da própria Nota de Entrada referenciada pela Devolução

Dt anterior à adoção IN\-RE087/20: \[31/12/2020\]

13/05/2021

MFS72958

Liliane Videira Assaf

Tratamento de produtos novos sem inventário\.

\- Criação do campo Natureza de Estoque\.

21/09/2021

MFS76452

Liliane Videira Assaf

Inclusão dos quadros:

\- Lançamento do Valor a Complementar na Apuração do ICMS\-ST

\- Lançamento do Valor a Restituir na Apuração do ICMS\-ST

\- Lançamento do Valor a Restituir na Apuração do ICMS

\- Lançamento do Estorno do Valor da Compensação na Apuração do ICMS

\- Lançamento do Valor da Compensação na Apuração do ICMS\-ST

03/12/2021

MFS84493

Andréa Rocha

Tratamento de produtos novos sem inventário\.

\- Criação do campo Conta Contábil\.

22/04/2022

MFS99147

Liliane Assaf

Parâmetro na tela de Dados Iniciais “Tratamento p/ saídas com quantidades não acobertadas pelo saldo \(Cálculo da Média Ponderada\)”

18/01/2023

MFS543860

Andréa Rocha

Inclusão de um parâmetro para definir se o valor do FECEP está embutido nos valores de ICMS não destacado e não escriturado\.  Esse parâmetro está sendo criado separado do parâmetro “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)”, porque o parâmetro já existente está vinculado a atualização do DATA MART, e os campos de ICMS não destacado e não escriturado não são gravados com o valor do FECEP embutido durante a equalização\.

19/06/2023

Sumário

[1\.	Regras Gerais	2](#_Toc524527071)

[2\.	Layout da Tela	2](#_Toc524527072)

[3\.	Regras de Funcionamento dos Campos	4](#_Toc524527073)

# <a id="_Toc524527071"></a>Regras Gerais

Esta é uma parametrização de informações diversas, a serem utilizadas na geração do movimento da IN087/20\.

Apenas será possível parametrização para estabelecimentos do Rio grande do Sul\.

# <a id="_Toc524527072"></a>Layout da Tela

Tela do tipo formulário simples\.

Tabela: EST\_ST\_RS\_DADOS\_INI\_IN87

__Botões da barra de menu__:

NOVO

Ao clicar nesta opção os dados da tela serão limpos, e o usuário poderá cadastrar a parametrização para um novo estabelecimento\. 

ABRE

Exibe janela de pesquisa dos dados já parametrizados, para que o usuário selecione a parametrização <a id="OLE_LINK4"></a>desejada a ser exibida em tela\.

EXCLUI

Opção para excluir a parametrização de um estabelecimento

CONFIRMA

Opção para salvar os dados da parametrização incluída / alterada\.

RELATÓRIO

Esta opção permite imprimir os dados da parametrização\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

  

# <a id="_Toc524527073"></a>Regras de Funcionamento dos Campos

Ao acessar a janela através do menu Parâmetros >> IN\-RE 087/2020 >>Dados Iniciais, o sistema deve verificar se o estabelecimento foi informado no login do Manager\.

Caso o estabelecimento tenha sido informado no login e a UF do mesmo seja diferente de RS, o sistema exibir a mensagem a seguir e não abrir a janela:

*“Este estabelecimento não pertence ao Rio Grande do Sul”*

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/__

__Default__

__Regra__

<a id="_Hlk517437550"></a>Estabelecimento

Alfanumérico 

__S__

S

Listbox

Este campo é uma lista dos estabelecimentos da empresa para seleção do usuário\.

Caso o estabelecimento seja informado no login do Manager, este campo deve ser apresentado bloqueado\. 

Caso contrário, apresentar uma lista contendo todos os estabelecimentos da empresa de login, cuja UF seja __RS__\.

Ao salvar o registro fazer as seguintes validações:

1\) Caso o campo “Estabelecimento” não esteja preenchido, então exibir a seguinte mensagem e não salvar registro:

*   “Campo "Estabelecimento" deve ser preenchido\.”*

Contribuinte Varejista?

Alfanumérico 

__S__

S

RadioButton/

Default: __Sim__

Campo composto com as seguintes opções:

- Sim
- Não

Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\) 

Alfanumérico

N

S

Check box\.

Defalt: desmarcado\.

Através deste campo será possível identificar se os valores do ICMS e ICMS\-ST já foram carregados incluindo o FECEP, na X08\_ITENS\_MERC, via interface\. Com essa informação será possível decidir se somamos ou não o FECEP na geração do movimento \(IN087/20\) das Entrada \(C180\) e Devolução de Entrada \(C186\), nos campos que consideram os tributos ICMS\-ST e FECEP\.

Valores de FECEP estão embutidos nos valores de ICMS\-ST não destacado/não escriturado 

Alfanumérico

N

S

Check box\.

Defalt: desmarcado\.

__\[MFS543860\]__ Inclusão do parâmetro para os valores de ICMS não destacado/não escriturado

Através deste campo será possível identificar se os valores do ICMS\-ST não destacado/não escriturado já foram carregados incluindo o FECEP, na X08\_ITENS\_MERC, via interface\. Com essa informação será possível decidir se somamos ou não o FECEP na geração do movimento \(IN087/20\) das Entrada \(C180\) e Devolução de Entrada \(C186\), nos campos que consideram os tributos ICMS\-ST e FECEP\.

Tratamento p/ Entrada objeto da Devolução de períodos anteriores à adoção da sistemática da IN\-RE 087/20

Alfanumérico

S

S

Radium Button

Default: Primeira opção “do Inventário do Produto\.\.\.”

Título: “Valores Unitários Médios recuperados:”

Campo obrigatório com duas opções:

- do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)
- da própria Nota de Entrada referenciada pela Devolução

Esse parâmetro é utilizado na geração do movimento \(IN087/20\) da Devolução das Entradas \(C186\)\.

Data anterior à adoção IN\-RE087/20

Data

S

S

DD/MM/AAAA

Data do Inventário \(Dia imediatamente anterior ao mês/ano inicial da adoção da sistemática da IN\-RE 087/20\)

Data de recuperação do inventário para tratamento das Entradas anteriores ao início da geração dos movimentos pela sistemática da IN\-RE 087/20, aplicado na geração da Devolução das Entradas \(C186\)\.

O campo “Dt anterior à adoção IN\-RE087/20” será apresentado com valor default, igual a 31/12/2020\.

Ao salvar o registro fazer as seguintes validações:

1\) Caso o campo “Dt anterior à adoção IN\-RE087/20” não esteja preenchido, então exibir a mensagem e não salvar registro:

*   “Campo "Data anterior à adoção IN\-RE087/20" não foi preenchido\. Conforme IN\-RE 087/20 este campo deve ser preenchido com data igual ou posterior a 31/12/2020\.”*

2\)  Caso o campo “Data anterior à adoção IN\-RE087/20” seja menor que 31/12/2020, então exibir a mensagem e não salvar registro:

*   “Campo "Data anterior à adoção IN\-RE087/20" não pode ser inferior a 31/12/2020\.”*

__\[MFS72958\]__

Natureza de Estoque

Alfanumérico

Grupo/Pastinha/Código/ Validade/Descrição

Campo para informar a Natureza de Estoque de acordo com a Tabela de Natureza de Estoque \(SAFX2010\)\.

![](data:image/png;base64,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)

\- Grupo: campo desabilitado, Demonstrar o grupo da parametrização de “Relação entre Tabelas e Grupos” \(vide módulo Parâmetros\) de maior validade para o estabelecimento e tabela “Natureza de Estoque \(código “2010”\)\.

\- Código: campo habilitado\. Ao digitar o código, o sistema deve recuperar o registro no cadastro da Tabela de Natureza de Estoque de máxima validade, considerando o grupo e o código informados\.

\- Validade: campo desabilitado\. Demonstrar a validade o registro recuperado da Tabela de Natureza de Estoque\.

\- Descrição: campo desabilitado\. Demonstrar a descrição do registro recuperado da Tabela de Natureza de Estoque\.

\- Pastinha: pesquisa na Tabela de Natureza de Estoque, considerando o grupo\. Caso exista mais de um registro de mesmo grupo e código, recuperar o de máxima validade\.

__\[MFS84493\]__

Conta Contábil

Alfanumérico

N

S

Grupo/Pastinha/Código/ Validade/Descrição

Campo para informar a Conta Contábil de acordo com a Tabela de Plano de Contas \(SAFX2002\)\.

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAArCAYAAADFV9TYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAATZSURBVHhe7d1BcqpMFIZhvevILAvRKheRoftwcjPKEjLPMItIFQ6ziwyyD68HOLnHTh9oEKSR96niB5qm23hFvr8VWRdFcVoBAAAgW3/qOQAAADLFCBswkcfHx3rpei8vL6unp6d6DQDy9vX1VS8hZr/fr47HY71WIbDhJjg4/9MDUQLbw8NDXdrf29vb6vPzswxsPM8Acifvgfq+hd8Oh0N5biCwYRISJDg4Lw9EDWzhQdmVPrca2HieAeRK3wPt/2jiknduILDhJmyoWDJ7II4Z2F5fX+utAJCP7+9vAlsL79zARQdAJrbbbXQCgCXaboufyfLKlS336nrlypZ7dYcqT1UGtilPEGP3bdv02tfyMfoHUshr7/n5OTptNpfHCK9TAPdOQk1RbH8mDTleecwUbXQt7+KPvPkXhTT0f+p7Qui639h9a/ttUuoAY5PX69+/z7/mx2OxOp2q16nMAQDLE/1IdMoAM2TfBDHMiYykSTjz5hLg1uuqrizrBACo6EjWNYZoYwyt32GLnRh0OSwXYb1YnVSx/XU5LBdhPa9OWB7WAaYQC2d2LmSE7XT+j84BAMvQGNjkJCGjVDrZYGO32XJZV7o9rJNirL69cmBqNqzZUGbn56XzJMNsp3OQW5evYwCAZAM5t193Xs91dE30vko05UQhJx6dhjRl38BYdIStUoWy5jkAYCl6B7Y2EpR0JOvWowBT9g30JWFNPv4MR9Jic6nHaxsAKvc+uiaigW3KUSlGxLBUVVgr01ojwhqAeyfBSQKUThqkvPKYKdroWt5FeaeDMCTZk4HdpuU6gqXserhs2X1UUx27Lda+CPuzy5aUx8qE7mf3x7C400HFu9NB+NpsY1+n3OkAwFxwp4N23p0OuDUVboLAVvEC2zUIbADmgsDWjsCGSRHYKgQ2AEtmA9tut6tLESKwYTISJDg4KzawfXx81KXXsYGN5xlAzuQ9EO0IbJjEZrOplyDkQHx/f6/XhiGBjecZwBxc+8nCEv1cdHCelwXeF/NTdW3L1g81bRPaftd2Rep27UM17TOEtscFAACW5+fm70KX7RQGllQpbdm+c9b0NwztFn0AAIB5KX+JU0PTEAFK2xiyLY/XV0rffdsWKe1fY+z2pyDfrQIAAGn2+/3FR8edAptsF14du39qW8LWs+WiT1+xdeXtYzW1LVLaF1qeUtfS9sN+5kyvXgQAAM0Oh8OvK0XdwBYLFm0BItzfqxtu03WvPMZu67Nf37ZF03Zdj9Xx6oa88jnTwMZv7gAA0Cz2s0/uvUQlMHQJDbcMGWFfsixlIvY4pEynNrH928Tat4/Ja69rPwAAYJlGu/l7LjSA6TQG277tQ5ZtiAMAAOijMbClhg0NRW2GCC9eXxqOUh6HJ2X/tjr6N+pcH1eMVw4AAGBdBDYNFzqlBBNP2JZtz+snLFd2uSuvTZXStt1fH6tK+VtiZbZclmO8cgAAsCwXFx0gDzbM3QsuOgAAIE30ogMd9UEe7jGsAQCA65QfiRIQ8sG/BQAACN39VaIAAABzR2ADAADIHIENAAAgcwQ2AACAzBHYAAAAMrcuiuJULwOjkd9h2+129RoAAGgS/g4bgQ03sdls6iUAAJCCwAYAADAjfIcNAAAgcwQ2AACAzBHYAAAAsrZa/QPLGKaYCImPwwAAAABJRU5ErkJggg==)

\- Grupo: campo desabilitado, Demonstrar o grupo da parametrização de “Relação entre Tabelas e Grupos” \(vide módulo Parâmetros\) de maior validade para o estabelecimento e tabela “Plano de Contas \(código “2002”\)\.

\- Código: campo habilitado\. Ao digitar o código, o sistema deve recuperar o registro no cadastro da Tabela de Plano de Contas de máxima validade, considerando o grupo e o código informados\.

\- Validade: campo desabilitado\. Demonstrar a validade o registro recuperado da Tabela de Plano de Contas\.

\- Descrição: campo desabilitado\. Demonstrar a descrição do registro recuperado da Tabela de Plano de Contas\.

\- Pastinha: pesquisa na Tabela de Plano de Contas, considerando o grupo\. Caso exista mais de um registro de mesmo grupo e código, recuperar o de máxima validade\.

__Lançamento do Valor a Complementar na Apuração do ICMS\-ST__

__\(quadro contendo os 3 campos abaixo\)__

Item da Apuração

Alfanumérico 

N

N

Código \+ Descrição /

Default: 002 

Este campo tem como origem o Cadastro de Operações da Apuração – tabela OPERACAO\_APURACAO \(TFIX18\)\.

Apresentar o Código e a Descrição relacionada à operação “002”, cadastrada na tabela OPERACAO\_APURACAO considerando o livro 108\. Com isso, no campo será apresentado a seguinte informação:

CÓDIGO

DESCRIÇÃO

002

OUTROS DÉBITOS   \(DISCRIMINAR ABAIXO\)

Manter o campo desabilitado\.

Futuramente, caso a legislação determine outro código de operação para realização do lançamento, basta habilitarmos este campo para que o usuário possa selecionar o código da operação adequado\.

cod\_oper\_apur\_compl

Descrição do Lançamento

Alfanumérico 

N

S

Campo Texto livre

Texto livre

dsc\_item\_apur\_compl    

Código do Ajuste Sped Fiscal

Alfanumérico

N

S

Pastinha \+ Código \+ Descrição

Este campo tem como origem o Cadastro do Código de Ajuste Sped Fiscal – tabela ICT\_AJUSTE\_ICMS\.

A pastinha de seleção dos códigos de ajuste somente pode apresentar os códigos que obedeçam a seguinte regra de formação:

-  Dois primeiros caracters =  “RS’
- Terceiro caracter = “1”
-  Quarto Caracter = “0” 

Caso seja digitado um código que não atenda a regra acima, exibir a seguinte mensagem:

 *“Código Ajuste inválido ou não cadastrado”*\.

Obs: Esse código é criado via tela de manutenção disponível do módulo ICMS \(menu: Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Código de Ajuste Sped Fiscal\)\.

cod\_ajuste\_icms\_compl

__Lançamento do Valor a Restituir na Apuração do ICMS\-ST__

__\(quadro contendo os 3 campos abaixo\)__

Item da Apuração

Alfanumérico 

N

N

Código \+ Descrição /

Default: 006 

Este campo tem como origem o Cadastro de Operações da Apuração – tabela OPERACAO\_APURACAO \(TFIX18\)\.

Apresentar o Código e a Descrição relacionada à operação “006”, cadastrada na tabela OPERACAO\_APURACAO considerando o livro 108\. Com isso, no campo será apresentado a seguinte informação:

CÓDIGO

DESCRIÇÃO

006

OUTROS CRÉDITOS   \(DISCRIMINAR ABAIXO\)

Manter o campo desabilitado\.

Futuramente, caso a legislação determine outro código de operação para realização do lançamento, basta habilitarmos este campo para que o usuário possa selecionar o código da operação adequado\.

cod\_oper\_apur\_rest\_st

Descrição do Lançamento

Alfanumérico 

N

S

Campo Texto livre

Texto livre

dsc\_item\_apur\_rest\_st

Código do Ajuste Sped Fiscal

Alfanumérico

N

S

Pastinha \+ Código \+ Descrição

Este campo tem como origem o Cadastro do Código de Ajuste Sped Fiscal – tabela ICT\_AJUSTE\_ICMS\.

A pastinha de seleção dos códigos de ajuste somente pode apresentar os códigos que obedeçam a seguinte regra de formação:

-  Dois primeiros caracters =  “RS’
- Terceiro caracter = “1”
-  Quarto Caracter = “2” 

Caso seja digitado um código que não atenda a regra acima, exibir a seguinte mensagem:

 *“Código Ajuste inválido ou não cadastrado”*\.

Obs: Esse código é criado via tela de manutenção disponível do módulo ICMS \(menu: Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Código de Ajuste Sped Fiscal\)\.

cod\_ajuste\_icms\_rest\_st

__Lançamento do Valor a Restituir na Apuração do ICMS__

__\(quadro contendo os 3 campos abaixo\)__

Item da Apuração

Alfanumérico 

N

N

Código \+ Descrição /

Default: 006 

Este campo tem como origem o Cadastro de Operações da Apuração – tabela OPERACAO\_APURACAO \(TFIX18\)\.

Apresentar o Código e a Descrição relacionada à operação “006”, cadastrada na tabela OPERACAO\_APURACAO considerando o livro 108\. Com isso, no campo será apresentado a seguinte informação:

CÓDIGO

DESCRIÇÃO

006

OUTROS CRÉDITOS   \(DISCRIMINAR ABAIXO\)

Manter o campo desabilitado\.

Futuramente, caso a legislação determine outro código de operação para realização do lançamento, basta habilitarmos este campo para que o usuário possa selecionar o código da operação adequado\.

cod\_oper\_apur\_rest\_ic

Descrição do Lançamento

Alfanumérico 

N

S

Campo Texto livre

Texto livre

dsc\_item\_apur\_rest\_ic

Código do Ajuste Sped Fiscal

Alfanumérico

N

S

Pastinha \+ Código \+ Descrição

Este campo tem como origem o Cadastro do Código de Ajuste Sped Fiscal – tabela ICT\_AJUSTE\_ICMS\.

A pastinha de seleção dos códigos de ajuste somente pode apresentar os códigos que obedeçam a seguinte regra de formação:

-  Dois primeiros caracters =  “RS’
- Terceiro caracter = “0”
-  Quarto Caracter = “2” 

Caso seja digitado um código que não atenda a regra acima, exibir a seguinte mensagem:

 *“Código Ajuste inválido ou não cadastrado”*\.

Obs: Esse código é criado via tela de manutenção disponível do módulo ICMS \(menu: Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Código de Ajuste Sped Fiscal\)\.

cod\_ajuste\_icms\_rest\_ic

__Lançamento do Estorno do Valor da Compensação na Apuração do ICMS__

__\(quadro contendo os 3 campos abaixo\)__

Item da Apuração

Alfanumérico 

N

N

Código \+ Descrição /

Default: 003 

Este campo tem como origem o Cadastro de Operações da Apuração – tabela OPERACAO\_APURACAO \(TFIX18\)\.

Apresentar o Código e a Descrição relacionada à operação “003”, cadastrada na tabela OPERACAO\_APURACAO considerando o livro 108\. Com isso, no campo será apresentado a seguinte informação:

CÓDIGO

DESCRIÇÃO

003

ESTORNO DE CRÉDITOS   \(DISCRIMINAR ABAIXO\)

Manter o campo desabilitado\.

Futuramente, caso a legislação determine outro código de operação para realização do lançamento, basta habilitarmos este campo para que o usuário possa selecionar o código da operação adequado\.

cod\_oper\_apur\_estorno

Descrição do Lançamento

Alfanumérico 

N

S

Campo Texto livre

Texto livre

dsc\_item\_apur\_estorno

Código do Ajuste Sped Fiscal

Alfanumérico

N

S

Pastinha \+ Código \+ Descrição

Este campo tem como origem o Cadastro do Código de Ajuste Sped Fiscal – tabela ICT\_AJUSTE\_ICMS\.

A pastinha de seleção dos códigos de ajuste somente pode apresentar os códigos que obedeçam a seguinte regra de formação:

-  Dois primeiros caracters =  “RS’
- Terceiro caracter = “0”
-  Quarto Caracter = “1” 

Caso seja digitado um código que não atenda a regra acima, exibir a seguinte mensagem:

 *“Código Ajuste inválido ou não cadastrado”*\.

Obs: Esse código é criado via tela de manutenção disponível do módulo ICMS \(menu: Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Código de Ajuste Sped Fiscal\)\.

cod\_ajuste\_icms\_estorno

__Lançamento do Valor da Compensação na Apuração do ICMS\-ST__

__\(quadro contendo os 3 campos abaixo\)__

Item da Apuração

Alfanumérico 

N

N

Código \+ Descrição /

Default: 006

Este campo tem como origem o Cadastro de Operações da Apuração – tabela OPERACAO\_APURACAO \(TFIX18\)\.

Apresentar o Código e a Descrição relacionada à operação “006”, cadastrada na tabela OPERACAO\_APURACAO considerando o livro 108\. Com isso, no campo será apresentado a seguinte informação:

CÓDIGO

DESCRIÇÃO

006

OUTROS CRÉDITOS   \(DISCRIMINAR ABAIXO\)

Manter o campo desabilitado\.

Futuramente, caso a legislação determine outro código de operação para realização do lançamento, basta habilitarmos este campo para que o usuário possa selecionar o código da operação adequado\.

cod\_oper\_apur\_compens

Descrição do Lançamento

Alfanumérico 

N

S

Campo Texto livre

Texto livre

dsc\_item\_apur\_compens

Código do Ajuste Sped Fiscal

Alfanumérico

N

S

Pastinha \+ Código \+ Descrição

Este campo tem como origem o Cadastro do Código de Ajuste Sped Fiscal – tabela ICT\_AJUSTE\_ICMS\.

A pastinha de seleção dos códigos de ajuste somente pode apresentar os códigos que obedeçam a seguinte regra de formação:

-  Dois primeiros caracters =  “RS’
- Terceiro caracter = “1”
-  Quarto Caracter = “2” 

Caso seja digitado um código que não atenda a regra acima, exibir a seguinte mensagem:

 *“Código Ajuste inválido ou não cadastrado”*\.

Obs: Esse código é criado via tela de manutenção disponível do módulo ICMS \(menu: Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Código de Ajuste Sped Fiscal\)\.

cod\_ajuste\_icms\_compens

Tratamento p/ saídas com quantidades não acobertadas pelo saldo \(Cálculo da Média Ponderada\)

Alfanumérico

N

S

Check box\.

Defalt: desmarcado\.

__\[MFS99147\]__

Quando a quantidade do saldo não for suficiente para cobrir a quantidade das saídas do dia, o usuário pode escolher essa opção, para que, no Cálculo da Média Ponderada, a quantidade das saídas seja deduzida até a quantidade suportada pelo saldo, evitando saldo negativo

Replicar para os Estabelecimentos

Checkbox

Default: desmarcado

Opção para permitir que a parametrização seja replicada para outros estabelecimentos no momento de salvar a operação\.

A lista dos estabelecimentos para replicação só será habilitada para seleção do usuário, quando esta opção estiver marcada\. Caso contrário, a lista permanece desabilitada, e não será possível selecionar nenhum estabelecimento\. 

Estabelecimentos

Alfanumérico 

N

N

Este campo exibe a lista dos estabelecimentos da empresa para seleção do usuário \(exceto o estabelecimento informado no campo “Estabelecimento”\), considerando apenas os estabelecimentos de RS\.

Selecionar todos

Alfanumérico 

N

N

Opção para marcar / desmarcar todos os estabelecimentos simultaneamente\.

= = = = = =

