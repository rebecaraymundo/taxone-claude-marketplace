# MTZ-Ressarc-SP-Parametrizacao_Produtos

- **Fonte:** MTZ-Ressarc-SP-Parametrizacao_Produtos.docx
- **Modificado:** 2024-07-04
- **Tamanho:** 73 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – SP \(Port CAT 42/2018\)

Parametrização de Produtos por Código

__Localização__: Menu Estadual, Módulo: Ressarcimento/Complemento ICMS\-ST \- SP, item Parâmetros à Produtos à Por Código

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS18796

Novo módulo Ressarcimento de  ICMS\-ST – SP

Replicação da parametrização de produtos do módulo Ressarcimento e Complemento ICMS\-ST \(CAT 17/1999\) para o novo módulo “ Ressarcimento e Complemento ICMS\-ST – SP \(CAT 42/2018\)\. 

19/06/2018

MFS24920

Andréa Rocha

Inclusão do campo "% de Redução de BC" e dos campos reservados\.

06/03/2019

Sumário

[1\.	Regras Gerais	2](#_Toc523412845)

[2\.	Layout da Tela	2](#_Toc523412846)

[3\.	Funcionamento da Tela	3](#_Toc523412847)

# <a id="_Toc523412845"></a>Regras Gerais

Esta parametrização é a mesma parametrização disponível no módulo Ressarcimento e Complemento ICMS\-ST \(CAT 17/1999\)\.

Os dados parametrizados são comuns aos dois módulos, e a parametrização foi replicada para o novo módulo “Ressarcimento e Complemento ICMS\-ST – SP \(CAT 42/2018\)”  por uma questão de praticidade\.

O funcionamento e as regras são as mesmas do módulo original\.

 

# <a id="_Toc523412846"></a>Layout da Tela

Tabela: ESP\_SP\_PROD\_ST \(produto principal\)

             ESP\_SP\_PROD\_ST\_ASS \(produtos associados\) 

Dados que definem a chave de tabela principal:

     \- Empresa

     \- Identificador do Estado \(IDENT\_ESTADO\)

     \- Grupo do Produto

     \- Indicador do Produto

     \- Código do Produto

     \- Validade Inicial

# <a id="_Toc523412847"></a>Funcionamento da Tela

Na abertura da tela, a janela de seleção do GRUPO será aberta automaticamente, obrigando o usuário a selecionar o grupo desejado\.

O grupo será utilizado para filtro dos produtos na SAFX2013, e só poderão ser parametrizados produtos do Grupo escolhido\.

*\(estas regras foram transcritas da parametrização original, apenas para efeito de documentação\)*

<a id="OLE_LINK1"></a>

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

Estado

Alfanumérico

__S__

S

Neste campo o usuário seleciona a UF desejada\.

Obs: Apesar de todas as funcionalidades deste modulo trabalharem apenas com estabelecimentos de SP, este campo permite a escolha da UF porque é a mesma parametrização do módulo original \(vide item 1\-Regras Gerais\)\.

<a id="_Hlk517192821"></a>Produto

Alfanumérico

__S__

S

Este campo trabalha com janela de seleção dos produtos <a id="OLE_LINK15"></a>da SAFX2013, considerando apenas os produtos do Grupo escolhido na abertura da tela\.

Quando o produto for digitado será validada a sua existência na tabela, e caso não exista, será exibida mensagem de erro padrão\.

<a id="OLE_LINK11"></a>Ao salvar a operação, serão feitas as seguintes críticas:

\- Verifica se o produto informado já consta como um produto associado na parametrização de outro produto qualquer\. Caso sim, a operação não será salva e será exibida a seguinte mensagem de erro: *“O produto principal já encontra\-se cadastrado como produto associado, não será permitida sua inclusão”*\.

\- Um determinado produto só pode ser parametrizado para outra data de validade inicial se a parametrização anterior for finalizada\. Assim, caso o produto já conste na parametrização, a validade final da parametrização já existente \(a mais atual\) deve estar preenchida\. Ou seja, a parametrização mais atual não poderá estar em aberto\. Caso contrário, a operação não será salva e será exibida a seguinte mensagem: *“Foi identificada parametrização para o produto X\-XXXXXXX com data inicial de vigência igual a 99/99/9999, que entra em conflito com as datas de vigência informadas”*

\- Estando a parametrização anterior já finalizada, será verificado se a validade inicial da nova parametrização é superior à data da validade final da parametrização já existente \(a mais atual\)\. Caso contrário, a operação não será salva e será exibida a seguinte mensagem:  *                   “Foi identificada parametrização para o produto X\-XXXXXXX com datas de vigência iguais a 99/99/9999 e 99/99/9999,                                               que estão em conflito com as datas de vigência informadas”*

Alíquota Interna

Numérico

__S__

S

Valor com 4 decimais

Neste campo será informada a alíquota interna da parametrização\.

Data inicial de vigência

Data

__S__

S

\(dd/mm/aaaa\)

Neste campo será informada a data de validade inicial da parametrização\.

Deve ser uma data válida\.

 

Data final de vigência

Data

N

S

\(dd/mm/aaaa\)

Neste campo será informada a data de validade final da parametrização\.

Deve ser uma data válida, que seja >= a data de vigência inicial\.

% de Redução de BC

Numérico

__N__

S

Valor com 4 decimais

MFS24920\]

Neste campo será informado o percentual de redução da base de cálculo\.

Reservado 1

Numérico

__N__

S

Valor com 2 decimais

MFS24920\]

Este campo será de uso livre para o usuário\.

Reservado 2

Numérico

__N__

S

Valor com 2 decimais

MFS24920\]

Este campo será de uso livre para o usuário\.

Reservado 3

Numérico

__N__

S

Valor com 2 decimais

MFS24920\]

Este campo será de uso livre para o usuário\.

Reservado 4

Alfanumérico

__N__

S

MFS24920\]

Este campo será de uso livre para o usuário\.

Reservado 5

Alfanumérico

__N__

S

MFS24920\]

Este campo será de uso livre para o usuário\.

Reservado 6

Alfanumérico

__N__

S

MFS24920\]

Este campo será de uso livre para o usuário\.

Reservado 7

Alfanumérico

__N__

S

MFS24920\]

Este campo será de uso livre para o usuário\.

Reservado 8

Alfanumérico

__N__

S

MFS24920\]

Este campo será de uso livre para o usuário\.

Produtos Associados

Alfanumérico

N

S

 

Neste campo o usuário poderá, opcionalmente, informar produtos que serão associados ao produto principal\. 

Da mesma forma que o campo “Produto”, este campo trabalha com janela de seleção dos produtos da SAFX2013, considerando apenas os produtos do Grupo escolhido na abertura da tela\.

Quando o produto for digitado será validada a sua existência na tabela, e caso não exista, será exibida mensagem de erro padrão\.

 

Ao salvar a operação, serão feitas as seguintes críticas:

\- Se um produto associado já tiver sido parametrizado como produto principal,<a id="OLE_LINK12"></a><a id="OLE_LINK13"></a><a id="OLE_LINK14"></a> a operação não será salva e será exibida a seguinte mensagem de erro: *“O produto associado já encontra\-se cadastrado como produto principal, não será permitida sua inclusão”*

<a id="OLE_LINK16"></a>\- Se um produto associado tiver sido informado mais de uma vez, a operação não será salva e será exibida a seguinte mensagem de erro: *“Produto X – XXXXXXXXXXXX já associado”\.*

\- Se um produto associado já constar como associado a outro produto principal, em períodos de vigência paralelos, a operação não será salva e será exibida a seguinte mensagem de erro: *“O produto associado X – XXXXXXXXXXXX está relacionado com o produto principal X – XXXXXXXXXX com data inicial de vigência igual a 99/99/9999, que está em conflito com as datas de vigência informadas”\.*

__Segue exemplos de parametrizações válidas e inválidas:__

Parametrização já existente:

Produto ABC

Validade Inicial = 01/06/2018

Validade Final = \(não preenchida\)

Parametrização a ser incluída:

Produto ABC                                           \(Esta nova parametrização __*não*__ seria permitida, pois a anterior está em aberto\)

Validade Inicial = 01/10/2018

Validade Final =

Parametrização já existente:

Produto ABC

Validade Inicial = 01/06/2018

Validade Final = 30/09/2108

Parametrização a ser incluída:

Produto ABC                                           \(Esta nova parametrização seria permitida\)

Validade Inicial = 01/10/2018

Validade Final =

Parametrização já existente:

Produto ABC

Validade Inicial = 01/06/2018

Validade Final = 30/09/2108

Parametrização a ser incluída:

Produto ABC                                  \(Esta nova parametrização __não __seria permitida, pois sua validade inicial não atende a regra 

Validade Inicial = 30/09/2018          definida\. Deveria ser uma data superior a validade final da parametrização anterior\)

Validade Final =

 

       = = = = = =

