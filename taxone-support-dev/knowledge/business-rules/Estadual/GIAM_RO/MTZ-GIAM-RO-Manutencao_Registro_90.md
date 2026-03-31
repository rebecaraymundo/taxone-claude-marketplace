# MTZ-GIAM-RO-Manutencao_Registro_90

- **Fonte:** MTZ-GIAM-RO-Manutencao_Registro_90.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 28 KB

---

GIAM\-RO – Manutenção do Registro Tipo 90 – Créditos Fiscais Antecipados

__Módulo:__ Estadual – GIAM\-RO

__Menu: __Manutenção \-> Registro Tipo 90 – Crédito Fiscal Antecipado 

DOCUMENTO DE REQUISITO

__DR__

__Nome__

__Descrição__

OS3592

Inclusão da tela de manutenção

Inclusão da tela de manutenção do Registro Tipo 90

REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Regras Gerais__

Cada linha que é apresentada no arquivo magnético é um registro da nova tabela\. Deverá emitir o Relatório de Conferência dos campos do registro\.

Poderão existir várias receitas iguais ou diferentes para o mesmo período se a Guia de Lançamento for de numeração diferente\.

__Críticas para esta tela:__

- Se não for preenchido o período, ao salvar dar a crítica: __“Período não informado\!”__
- Se o usuário tentar incluir uma manutenção com código de Guia de Lançamento já existente no período, dar a crítica: __“Já existe registro com a chave informada\!”\.__

__OS3592__

__RN01__

__Campo: Estabelecimento__

Deverá trazer fixo o estabelecimento que o usuário está logado\. Caso o usuário não esteja logado em nenhum estabelecimento, listar todos os estabelecimentos cuja UF seja igual a RO \(no cadastro: módulo Parâmetros → Preliminares → Empresa/Estabelecimento\)\.

Campo chave

Campo obrigatório\.

Este campo deverá estar bloqueado para manutenção do registro\.

__ __

__OS3592__

__RN02__

__Campo Período:__

Deverá permitir a gravação do mês/ano \(00/0000\)\. Utilizar para o critério de busca o mês que o usuário preencheu\.

Campo chave

Campo obrigatório\.

Este campo deverá estar bloqueado para manutenção do registro\.

__OS3592__

__RN03__

__Campo Guia de Lançamento__: 

Este campo deverá estar livre para que o usuário digite o conteúdo\. Deverá permitir a inserção de valor numérico com 14 posições\.

Campo chave

Campo obrigatório

Este campo deverá estar bloqueado para manutenção do registro\.

__OS3592__

__RN04__

__Campo Parcela__: 

Este campo deverá estar livre para que o usuário digite o conteúdo\. Deverá permitir a inserção de valor numérico com 02 posições\.

Este campo não deverá estar bloqueado para manutenção do registro\.

__OS3592__

__RN05__

__Campo Código Receita__: 

Este campo deverá estar livre para que o usuário digite o conteúdo\. Deverá permitir a inserção de código numérico com 04 posições\.

Campo obrigatório

Este campo não deverá estar bloqueado para manutenção do registro\.

__OS3592__

__RN06__

__Campo Retificadora__:

Este campo deverá estar livre para que o usuário escolha o conteúdo\. Deverá apresentar o conteúdo “Não” ou “Sim” no ComboBox\. Default do campo igual a “Não”\.

Este campo não deverá estar bloqueado para manutenção do registro\.

__OS3592__

__RN07__

__Campo Valor do Crédito__: 

Este campo deverá estar livre para que o usuário digite o valor do crédito\. Deverá permitir a inserção de valor numérico com 17 posições, sendo 15 inteiros e 2 decimais\.

Este campo não deverá estar bloqueado para manutenção do registro\.

__OS3592__

