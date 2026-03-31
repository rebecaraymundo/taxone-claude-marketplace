# MTZ_PowerLock_Controle de Seguranca

- **Fonte:** MTZ_PowerLock_Controle de Seguranca.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 29 KB

---

# Power Lock – Controle de Segurança – Parâmetros

__Localização:__

Powerlock > File > Controle de Segurança > Parâmetros

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3894

DW \- BASICOS \- SEGURANÇA \- Tratamento para utilização de password

O objetivo da OS é criar novas regras para a criação/alteração de senhas no PowerLock\.

OS4381

DW \- BASICOS \- Powerlock \- USUÁRIOS SIMULTANEOS

Criação de parâmetro para Bloquear acessos Simultâneos

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Regra p/ campo Não permitir senha derivada do login do usuário__

Esse campo deve ser um checkbox e deve ter as seguintes opções: “S” – marcado e “N” – desmarcado \(default\)\. 

OS3894

__RN01__

__Regra p/ campo Não permitir senha composta por sequencias do mesmo caracter 4 vezes ou mais__

Esse campo deve ser um checkbox e deve ter as seguintes opções: “S” – marcado e “N” – desmarcado \(default\)\.

OS3894

__RN02__

__Regra p/ campo Não permitir senha composta pelas palavras parametrizadas aqui__

Esse campo deve ser um checkbox e deve ter as seguintes opções: “S” – marcado e “N” – desmarcado \(default\)\.

OS3894

__RN03__

__Regra p/ campo Bloquear Acessos Simultâneos \(frame Acessos Simultâneos\)__

Esse campo deve ser um checkbox e deve ter as seguintes opções: “S” – marcado e “N” – desmarcado \(default\)\.

OS4381

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

