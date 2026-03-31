# MTZ-OTF-Nomenclatura_IN_698-2006

- **Fonte:** MTZ-OTF-Nomenclatura_IN_698-2006.docx
- **Modificado:** 2020-08-31
- **Tamanho:** 46 KB

---

# Obrigações de Tributos Federais \- Nomenclatura IN 698/2006

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3752

Obrigações de Tributos Federais \- Nomenclatura IN 698/2006

Trata\-se da criação do Informe de Rendimentos Financeiros, de acordo com a IN 698/2006\.

#### Cód\.

### Descrição

###     DR

# RN01

Deverá ser criado no módulo Obrigações de Tributos Federais, a tela “Nomenclatura – IN 698/2006”\. Essa tela irá permitir que o usuário cadastre as classes \(quadros\), linhas e descrições do Informe de Rendimentos Financeiros de acordo com a IN 698/2006\.

Essa tela será disponibilizada abaixo do menu: Parâmetros >> Nomenclatura\.

OS3752

# RN02

A tela “Nomenclatura – IN 698/2006” deverá permitir as operações de inclusão, consulta, alteração e exclusão dos registros\.

OS3752

# RN03

Deverá ser previsto para essa tela um relatório de conferência\.

OS3752

# RN04

Nessa tela deverão ser exibidos os seguintes campos:

- __Classe:__ nesse campo, o sistema deverá permitir a seleção das classes \(quadros\) que compõem o Informe de Rendimentos Financeiros\. Esse campo é obrigatório de preenchimento\. Deverá ser exibida a seguinte opção:
	- 3 – Rendimentos Tributáveis
- __Número:__ nesse campo, o sistema deverá permitir a digitação do número da linha de acordo com a classe informada\. Esse campo deverá ser Numérico de 2 \(duas\) posições\. Campo obrigatório de preenchimento\.
- __Descrição:__ nesse campo, o sistema deverá permitir a digitação da descrição da linha do Informe de Rendimentos\. Esse campo deverá ser Alfanumérico de 100 \(cem\) posições\. Campo obrigatório de preenchimento\.

O sistema não deverá permitir a inclusão de uma nomenclatura com a mesma Classe e Número de um registro já existente\. Caso isso aconteça, deverá ser exibida mensagem de erro: “Não é permitido a inclusão de uma linha no Informe de Rendimentos com Classe e Número idênticos\.”\.

Caso algo dos campos obrigatórios de preenchimento – Classe, Número e/ou Descrição – não estejam preenchidos e o usuário solicite a inclusão do mesmo, deverá ser exibida mensagem de erro padrão do sistema de falta de campo obrigatório preenchido\.

OS3752

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

