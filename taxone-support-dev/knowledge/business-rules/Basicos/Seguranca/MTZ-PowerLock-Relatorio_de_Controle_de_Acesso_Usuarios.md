# MTZ-PowerLock-Relatorio_de_Controle_de_Acesso_Usuarios

- **Fonte:** MTZ-PowerLock-Relatorio_de_Controle_de_Acesso_Usuarios.docx
- **Modificado:** 2020-09-21
- **Tamanho:** 59 KB

---

# Segurança \- PowerLock

#  Relatório de Concessão/Revogação de Usuários

__Localização: __

__Módulo__: Básicos 🡪 Segurança

__Menu__: Reports 🡪 Users Control Report

##### DOCUMENTO DE REQUISITO

###### MFS

###### Nome

__Descrição__

MFS39518

Andréa Rocha 

O objetivo é criar um relatório para demonstrar o log de concessão e revogação de acessos dos usuários\.

## REGRAS DE NEGÓCIO

#### Cód\.

#### Descrição

#### MFS

__RN00__

__Parâmetros de tela:__

\- Período: informar a data inicial e a data final, campos do tipo data no formato DD/MM/AAAA\.

\- Administrador: campo do tipo listbox, que irá mostrar todos os administradores cadastrados e mais a opção “TODOS”\.

     

MFS39518

__RN01__

Regra geral do relatório

O relatório irá recuperar as informações dos usuários da nova tabela criada para o controle de criação e alteração de usuários \(PL\_USR\_AUDIT\)\.  Esta tabela será gravada quando for criado ou alterado um usuário, e somente serão gravadas as informações referentes ao acesso do usuário, tais como status e data de expiração\. 

Os filtros para o relatório são:

\- Data do registro dentro do período informado em tela;

\- Administrador de acordo com o informado em tela ou todos\.

  

MFS39518

__RN02__

Regra p/ campo Emissão \(Cabeçalho\)

Preencher com o dia e hora em que o relatório foi gerado\. Utilizar SYSDATE\. Formato: DD/MM/AAAA HH:MM:SS\.

MFS39518

__RN03__

Regra p/ campo Período \(Cabeçalho\)

Preencher com o período informado na tela de critério de seleção\. Formato: DD/MM/AAAA\.

O campo deve conter um textbox \+ “à” \+ textox\. Mascara de data para o textbox: DD/MM/AAAA\.

MFS39518

__RN04__

Regra p/ campo Administrador \(Cabeçalho\)

Preencher com o campo “ADM\_KEY” da tabela PL\_USR\_AUDIT\.

MFS39518

__RN05__

Regra p/ campo Login \(Nome\)

Preencher com o campo USR\_KEY da tabela PL\_USR\_AUDIT\.

MFS39518

__RN06__

Regra p/ campo Status

O Preencher com o campo USR\_STATUS da tabela PL\_USR\_AUDIT\.

Se o campo for igual a “0”

      Mostrar “Inativo”

Senão se o campo for igual a “1”

      Mostrar “Ativo”

Senão 

      Mostrar “Não preenchido”\.

MFS39518

__RN07__

Regra p/ campo Expira em

Preencher com o campo USR\_EXPIRE\_DATE da tabela PL\_USR\_AUDIT\. 

Se o campo não estiver preenchido

     Mostrar “Não preenchido”\.

MFS39518

__RN08__

Regra p/ campo Registrado em

Preencher com o campo DT\_REG da tabela PL\_USR\_AUDIT\.

MFS39518

__RN09__

Regra p/ campo Tipo do Registro

Preencher com o campo USR\_MODIFY da tabela PL\_USR\_AUDIT\.

Se o campo for igual a “I”

      Mostrar “Criação”

Senão se o campo for igual a “U”

      Mostrar “Alteração”\.

MFS39518

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

