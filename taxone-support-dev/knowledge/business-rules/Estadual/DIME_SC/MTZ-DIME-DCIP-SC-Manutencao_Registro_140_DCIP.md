# MTZ-DIME-DCIP-SC-Manutencao_Registro_140_DCIP

- **Fonte:** MTZ-DIME-DCIP-SC-Manutencao_Registro_140_DCIP.docx
- **Modificado:** 2021-10-08
- **Tamanho:** 31 KB

---

__DIME/DCIP\-SC – Manutenção do Registro Tipo 140 – Discriminação de crédito imposto retido substituição tributária__

__Módulo:__ Estadual – DIME\-SC

__Menu: __Obrigações  \-> Manutenção – Discriminação de crédito imposto retido substituição tributária

DOCUMENTO DE REQUISITO

__DR__

__Nome__

__Descrição__

OS4232

Inclusão da tela de manutenção

Inclusão da tela de manutenção do Registro Tipo 140 da DCIP

REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Regras Gerais__

Cada linha que é apresentada no arquivo magnético é um registro da nova tabela\. 

__Críticas para esta tela:__

- Se não for preenchido o período, ao salvar dar a crítica: __“Data de Apuração não informado\!”__
- Se o usuário tentar incluir uma manutenção com o campo tipo de crédito já existente no período, dar a crítica: __“Já existe registro com a chave informada\!”\.__

__OS4232__

__RN01__

__Campo: Estabelecimento__

Deverá trazer fixo o estabelecimento que o usuário está logado\. Caso o usuário não esteja logado em um estabelecimento, mostrar a lista de estabelecimento cujo estado seja igual a “SC” 

Campo chave

Campo obrigatório\.

Este campo deverá estar bloqueado para manutenção do registro\.

__ __

__OS4232__

__RN02__

__Campo Período Referência:__

Deverá permitir a gravação do mês/ano \(MM\)\. Utilizar para o critério de busca o mês que o usuário preencheu\.

Campo chave

Campo obrigatório\.

Este campo deverá estar bloqueado para manutenção do registro\.

__OS4232__

__RN03__

__Campo Tipo de crédito:__

Este campo deverá estar livre para que o usuário digite o conteúdo\. Deverá permitir a inserção de código numérico com 03 posições\. Em caso de não ter conteúdo para este campo, trazer a mensagem de alerta: “Tipo de crédito deve ser informado” e não gravar\.

Campo chave

Campo obrigatório

Este campo deverá estar bloqueado para manutenção do registro\.

__OS4232__

__RN04__

__Campo Valor do Crédito__: 

Este campo deverá estar livre para que o usuário digite o conteúdo\. Deverá permitir a inserção de valor numérico com 17 posições, sendo 15 inteiros e 2 decimais\.

Este campo não deverá estar bloqueado para manutenção do registro\.

__OS4232__

__RN05__

__Campo Número do S@T__: 

Este campo deverá estar livre para que o usuário digite o conteúdo\. Deverá permitir a inserção de código numérico com 15 posições\.

Este campo não deverá estar bloqueado para manutenção do registro\.

__OS4232__

