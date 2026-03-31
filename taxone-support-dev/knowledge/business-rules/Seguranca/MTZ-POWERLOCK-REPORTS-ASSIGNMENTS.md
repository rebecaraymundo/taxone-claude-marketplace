---
source: "MTZ-POWERLOCK-REPORTS-ASSIGNMENTS.doc"
category: Seguranca
converted: auto
---

POWER LOCK - Reports - Assignments

Localização:
Módulo: Básicos -->Segurança
Menu: Reports --> Assignments
Aba: Assignments


DOCUMENTO DE REQUISITO

DR
Nome
Descrição
OS3605
Criação do documento

Definição das regras dos relatórios Assignments.


REGRAS DE NEGÓCIO

Cód.
Descrição
DR
RN00

Regra Geral

Selecione um dos componentes do PowerLock (Reports) e as atribuições de componente  (Assignmentes) para especificar qual relatório será gerado.

As atribuições serão apresentadas conforme a regra de cada um dos componentes.
As atribuições, por default, vêm com todas as opções selecionadas e podem ser as seguintes:

* Users
* Applications
* Database Connections
* Groups
* Roles

       Para desmarcar, clique sobre a linha. 

Especifique o critério de seleção e os campos que indicarão os filtros de dados do relatório.


OS3605
RN01
Layout do relatório


Título do relatório:
                          "NOME_DO_COMPONENTE" ASSIGNMENT REPORT"
                                        d/m/aa hh:mm AM/PM


Corpo do relatório:

NOME_DO_COMPONENTE: %XXXX%

               Tributo (Assignment): %YYYYY%
                                    %XYYYY%
                                    %YMYYY%
                                  

               Tributo (Assignment): %YYYXY%
                                    %YYRYY%
                                    %YYYYT%

NOME_DO_COMPONENTE: %WWWW%

               Tributo (Assignment): %ZMZZZ%
                                    %ZZZXZ%
                                    %ZZTZZ%
                                  

               Tributo (Assignment): %YYYBY%
                                    %YRYYY%
                                    %YYYYF%


Rodapé do Relatório:

"NOME_DO_COMPONENTE" ASSIGNMENT REPORT"                                                                  Page "X" of "Y"

OS3605
RN02
Critério de seleção (Search Column):

No critério de seleção o usuário poderá filtrar dados no relatório de acordo com a sua necessidade.
Podem ser criados quantos filtros forem necessários para a pesquisa.

SERACH COLUMN
As opções da coluna do filtro dependerão do componente selecionado, e estes podem ser visualizados nas regras de cada um dos componentes.

OPERATOR
=
<
>
<=
>=
<>
IN
LIKE
BETWEEN
NOT IN
NOT LIKE
NOT BETWEEN

SERACH COLUMN
As opções de valor da pesquisa dependerão do componente selecionado, e estes podem ser visualizados nas regras de cada um dos componentes.

LOGICAL
AND
OR


OS3605
RN03
Sort Criteria

Campo deve ser mantido desabilitado da aba "Assignments"

OS3605


Reports - Componente USERS:


Cód.
Descrição
DR
RN00
Regra Geral

Quando selecionado o componente "USERS", exibir as seguintes atribuições em Assignments:

* Applications
* Database Connections
* Groups
* Roles

      
   Para o critério de seleção (Search Criteria), exibir seguintes informações em "Search Column":
      
   * First Name
   * Last Name
   * Login
   * Status

            Quando selecionado por "Status", exibir na coluna "Search Value" os seguintes status:
            
                * Active
                * Inactive
            

OS3605


Reports -  Componente GROUPS:


Cód.
Descrição
DR
RN00
Regra Geral

Quando selecionado o componente "GROUPS", exibir as seguintes atribuições em Assignments:

* Applications
* Database Connections
* Roles
* Users


   Para o critério de seleção (Search Criteria), exibir seguintes informações em "Search Column":
   
   * Group name

OS3605


Reports -  Componente APPLICATIONS:


Cód.
Descrição
DR
RN00
Regra Geral

Quando selecionado o componente "APPLICATIONS", exibir as seguintes atribuições em Assignments:

* Database Connections
* Groups
* Users


   Para o critério de seleção (Search Criteria), exibir seguintes informações em "Search Column":
   
   * Application Name
   * Status

            Quando selecionado por "Status", exibir na coluna "Search Value" os seguintes status:
            
                * Active
                * Inactive


OS3605


Reports -  Componente DATABASE CONNECTIONS:


Cód.
Descrição
DR
RN00
Regra Geral

Quando selecionado o componente "DATABASE CONNECTIONS", exibir as seguintes atribuições em Assignments:

* Applications
* Groups
* Users


     Para o critério de seleção (Search Criteria), exibir seguintes informações em "Search Column":
     
     * Connection Name
     * Database
     * DB Parm
     * DBMS

            Quando selecionado por "DBMS", exibir na coluna "Search Value" os seguintes status:
            
                * Allbase/SQL
                * Grupta
                * IBM
                * Informix
                * MDI
                * NetGateway
                * ODBC
                * Oracle 6
                * Oracle 7
                * Sybase
                * XDB

OS3605


Reports -  Componente ROLES:


Cód.
Descrição
DR
RN00
Regra Geral

Quando selecionado o componente "ROLES", exibir as seguintes atribuições em Assignments:

* Application
* Role

OS3605


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

