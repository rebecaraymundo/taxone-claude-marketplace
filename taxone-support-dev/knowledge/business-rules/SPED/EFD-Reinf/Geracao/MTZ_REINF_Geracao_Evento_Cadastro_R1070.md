# MTZ_REINF_Geracao_Evento_Cadastro_R1070

- **Fonte:** MTZ_REINF_Geracao_Evento_Cadastro_R1070.docx
- **Modificado:** 2023-03-28
- **Tamanho:** 92 KB

---

THOMSON REUTERS

Geração evento R\-1070 \- REINF

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS10757

Elenilson Coutinho

Definição de regras para geração do evento de Cadastro R\-1070 Reinf 

MFS13810

Lara Aline

Ajuste no Layout conforme v1\.2

MFS14930

Lara Aline

Ajuste na geração do campo nrInsc

MFS15750

Lara Aline

Ajuste no Layout conforme v1\.3\.

MFS17237

Lara Aline

Ajuste na tag novaValidade e nos campos iniValid e fimValid da tag infoContri do tipo Alteração\.

MFS10287

Lara Aline

Ajuste no registro InfoProcesso/IdePeriodo \- Informações do processo \(Exclusão\)

MFS\-90001

Alessandra Cristina Navatta

Alteração da versão 2\.1 para 2\.1\.1 e referência do arquivo de de\_para

__Obs\. Os ajustes mapeados nesta demanda, referem\-se a atualização funcional\. Não há impactos na implementação__

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral de Geração do Evento R\-1070\.__

O evento R\-1070 do SPED \- REINF tem por objetivo gerar informações de Processo\. Ele será gerado com os registros:

__Reinf__ – EFD \- Reinf

__evtTabProcesso – __Evento Tabela de Processos

__ideEvento – __Informações de Identificação do Evento

__ideContri – __Informações de identificação do contribuinte

__infoProcesso __\- Informações do Processo

__inclusão \-__ Inclusão de novas informações

__idePeriodo __\- Período de validade das informações incluídas

__ideProcesso __\- Informações de identificação do Processo e validade das informações que estão sendo incluídas

__infoSusp __\- Informações de Suspensão de Exibilidade de tributos

__dadosProcJud __\- Informações Complementares do Processo Judicial

__alteração __\- Alteração das informações

__idePeriodo __\- Período de validade das informações alteradas

__ideProcesso __\- informações de identificação do processo

__infoSusp __\- Informações de Suspensão de Exibilidade de tributos

__dadosProcJud __\- Informações Complementares do Processo Judicial

__novaValidade __\- Novo período de validade das informações

__exclusão __\- Exclusão das informações

__idePeriodo __\- Período de validade das informações excluídas

__ideProcesso \- __Exclusão de processo

Observar orientações existentes no arquivo "TR\_REINF\_DEXPARA\_V2\.1\.1\.xlsx"\.

- __Origem das informações__: SAFX2058, SAFX2059 e Cadastro do Estabelecimento\.
- __Regra de seleção__: O Registro R\-1070 é utilizado para demonstrar informações de Processos\.

Para obtermos as informações para sua geração, devemos recuperar registros das tabelas SAFX2058 e SAFX2059 se campo IND\_REINF = “S”\.

__Mensageria Log:__ 

Se o evento anterior do processo já tiver sido enviado e não tiver retorno ainda \(status 2 \- “Evento REINF Enviado”\) então exibir a seguinte mensagem: 

      Evento R1070 – Tabela de Processos Administrativos/Judiciais

     “Evento não gerado\. Existe evento anterior que foi enviado e ainda aguarda retorno\.”

Identificação do Processo: Tipo do Processo: XXXXX / N° do Processo: XXXXX / Validade Inicial:XXXX

Se não existir evento anterior do processo recebido com sucesso/advertencia no fisco\. Não posso gerar evento de exclusão, então exibir a seguinte mensagem: 

       Evento R1070 – Tabela de Processos Administrativos/Judiciais

      “Evento de exclusão não gerado\. Não existe evento anterior enviado para o fisco e recebido com sucesso ou advertência\.”

Identificação do Processo: Tipo do Processo: XXXXX / N° do Processo: XXXXX / Validade Inicial:XXXXX

MFS\-10757

MFS\-13810

MFS\-90001

- __Registro ideEvento – Informações de Identificação do Evento__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

- __Registro ideContri – Informações de Identificação do Contribuinte__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN01

- __Origem das informações__: Cadastro do Estabelecimento\.
- __Regra de seleção__: Este registro servirá para identificar o estabelecimento centralizador \(Matriz\)\.
- __Campos\-Chave__: tpInsc, nrInsc
- __Nível hierárquico do registro__: filho do registro evtTabProcesso
- __Ordenação__: não se aplica\.
- __Agrupamento__: não se aplica\.
- __Ocorrência__: Um por arquivo

MFS\-10757

RN02

__Campo tpInsc__

Será gerado com conteúdo igual a “1”\. 

MFS\-10757

RN03

__Campo nrInsc__

Será gerado com as 8 primeiras posições do CNPJ do Estabelecimento\. 

MFS14821

- __Registro InfoProcesso \- Informações do processo \(Inclusão\)__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN02

- __Origem das informações__: SAFX2058
- __Regra de seleção__: Este registro servirá identificar o período de validade das informações de Processo\. Será gerado considerando os seguintes critérios: Tabela REINF\_PGER\_R1070\_OC campo “IND\_OPER” igual a “I”
- __Campos\-Chave__: iniValid, fimValid
- __Nível hierárquico do registro__: filho do registro inclusao\.
- __Ordenação__: Não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Um por arquivo\.

MFS10757

MFS13810

RN03

__Campo iniValid__

Informação será recuperada do campo VALID\_PROC\_ADJ\_INI da SAFX2058\.

MFS10757

MFS13810

RN04

__Campo fimValid__

Informação será recuperada do campo VALID\_PROC\_ADJ\_FIM da SAFX2058\.

MFS10757

MFS13810

- __Registro InfoProcesso/ideProcesso – Informação/Identificação do Processo \(Inclusão\)__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN06

- __Origem das informações__: SAFX2058\.
- __Regra de seleção__: Este registro servirá identificar o processo\. Será gerado considerando os seguintes critérios: Tabela REINF\_PGER\_R1070\_OC campo “IND\_OPER” igual a “I”
- __Campos\-Chave__: tpProc, nrProc, iniValid, fimValid
- __Nível hierárquico do registro__: filho do registro Inclusão
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Um por arquivo\.

MFS10757

MFS13810

RN07

__Campo tpProc__

Informação será recuperada do campo IND\_TP\_PROC\_ADJ da SAFX2058

MFS10757

RN08

__Campo nrProc__

Informação será recuperada do campo NUM\_PROC\_ADJ da SAFX2058\.

MFS10757

RN09

__Campo iniValid__

Informação será recuperada do campo VALID\_PROC\_ADJ\_INI da SAFX2058\.

MFS13810

RN10

__Campo fimValid__

Informação será recuperada do campo VALID\_PROC\_ADJ\_FIM da SAFX2058\.

MFS13810

RN11

__Campo indAutoria__

Recuperar a informação do campo IND\_AUTORIA da SAFX2058\.

MFS13810

- __Registro infoSusp – Informação de Suspensão de Exigibilidade de Tributos__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN12

- __Origem das informações__: SAFX2059\.
- __Regra de seleção__: Este registro servirá para identificar as informações de Suspensão de exigibilidade de Tributos\. Será gerado considerando os seguintes critérios: Tabela REINF\_PGER\_R1070\_OC campo “IND\_OPER” igual a “I”
- __Campos\-Chave__: codSusp
- __Nível hierárquico do registro__: filho do registro ideProcesso\.
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: para cada ideProcesso poderá existir “50” infoSusp\.

MFS10757

RN13

__Campo codSusp__

Informação será recuperada do campo COD\_SUSP da SAFX2059\.

MFS10757

RN14

__Campo indSusp__

Informação será recuperada do campo IND\_SUSP da SAFX2059\.

MFS10757

RN15

__Campo dtDecisao__

Informação será recuperada do campo DAT\_DECISAO da SAFX2059\.

MFS10757

RN16

__Campo indDeposito__

Informação será recuperada do campo IND\_DEPOSITO da SAFX2059\.

MFS10757

- __Registro dadosProcJud \- Informações Complementares do Processo Judicial__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN17

- __Origem das informações__: SAFX2058\.
- __Regra de seleção__: Este registro servirá para identificar as informações Complementares do Processo Judicial\. Será gerado considerando os seguintes critérios: Tabela REINF\_PGER\_R1070\_OC campo “IND\_OPER” igual a “I”
- __Campos\-Chave__: 
- __Nível hierárquico do registro__: filho do registro ideProcesso
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Poderá existir 1 ou não existir\.

MFS10757

RN18

__Campo ufVara__

Informação será recuperada do campo COD\_ESTADO da SAFX2058\.

Caso campo não preenchido exibir a seguinte mensagem no log de pré\-geração:

Evento R1070 – Registro Informações Complementares do Processo Judicial

“Campo UF Seção Judiciária do cadastro de processos não preenchido”

Identificação do Processo: Tipo do Processo: XXXXX / N° do Processo: XXXXX / Validade Inicial: XXXXXX

MFS10757

RN19

__Campo codMunic__

Informação será recuperada do campo COD\_MUNICIPIO da SAFX2058\.

__\[ALTERADO MFS15750\]__

Caso campo não preenchido exibir a seguinte mensagem no log de pré\-geração:

Evento R1070 – Registro Informações Complementares do Processo Judicial

“Campo Código Município não preenchido”

Identificação do Processo: Tipo do Processo: XXXXX / N° do Processo: XXXXX / Validade Inicial: XXXXXX

MFS10757

MFS15750

RN20

__Campo idVara__

Informação será recuperada do campo COD\_VARA da SAFX2058\.

Caso campo não preenchido exibir a seguinte mensagem no log de pré\-geração:

Evento R1070 – Registro Informações Complementares do Processo Judicial 

“Campo Identificação da Vara do cadastro de processos não preenchido”

Identificação do Processo: Tipo do Processo: XXXXX / N° do Processo: XXXXX / Validade Inicial: XXXXXX

MFS10757

RN18

__Campo indAutoria__

Recuperar a informação do campo IND\_AUTORIA da SAFX2058\.

MFS10757

MFS13810

- __Registro InfoProcesso/IdePeriodo \- Informações do processo \(Alteração\)__

###### __CÓD__

###### __DESCRIÇÃO__

###### __OS/CH__

RN02

- Origem das informações: SAFX2058
- Regra de seleção: Este registro servirá identificar o período de validade das informações de Processo\. Será gerado considerando os seguintes critérios: Tabela REINF\_PGER\_R1070\_OC campo “IND\_OPER” igual a “A”
- Campos\-Chave: iniValid, fimValid
- Nível hierárquico do registro: filho do registro Alteracao\.
- Ordenação: Não se aplica\.
- Agrupamento: Não se aplica\.
- Ocorrência: Um por arquivo\.

MFS10757

MFS13810

RN20

__Campo iniValid__

Informação será recuperada do campo VALID\_PROC\_ADJ\_INI da SAFX2058\.

MFS10757

MFS13810

RN21

__Campo fimValid__

Informação será recuperada do campo VALID\_PROC\_ADJ\_FIM da SAFX2058\.

MFS10757

MFS13810

- __Registro InfoProcesso/ideProcesso – Informação/Identificação do Processo \(Alteração\)__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN21

- __Origem das informações__: SAFX2058\.
- __Regra de seleção__: Este registro servirá identificar o processo\. Será gerado considerando os seguintes critérios: Tabela REINF\_PGER\_R1070\_OC campo “IND\_OPER” igual a “A”
- __Campos\-Chave__: tpProc, nrProc, iniValid, fimValid
- __Nível hierárquico do registro__: filho do registro alteracao
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Um por arquivo\.

MFS10757

MFS13810

RN22

__Campo tpProc__

Informação será recuperada do campo IND\_TP\_PROC\_ADJ da SAFX2058

MFS10757

RN23

__Campo nrProc__

Informação será recuperada do campo NUM\_PROC\_ADJ da SAFX2058

MFS10757

RN24

__Campo iniValid__

__\[Alterado MFS17237\]__

A informação recuperada do campo VALID\_PROC\_ADJ\_INI da SAFX2058 será a informação sem a alteração, ou seja, a data informada anteriormente no registro que se pretende alterar\. A informação nova alterada será gerada no Registro novaValidade\.

MFS13810

MFS17237

RN25

__Campo fimValid__

__\[Alterado MFS17237\]__

A informação recuperada do campo VALID\_PROC\_ADJ\_FIM da SAFX2058 será a informação sem a alteração, ou seja, a data informada anteriormente no registro que se pretende alterar\. A informação nova alterada será gerada no Registro novaValidade\.

MFS13810

MFS17237

RN26

__Campo indAutoria__

Recuperar a informação do campo IND\_AUTORIA da SAFX2058\.

MFS13810

- __Registro infoSusp – Informação de Suspensão de Exigibilidade de Tributos__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN27

- __Origem das informações__: SAFX2059\.
- __Regra de seleção__: Este registro servirá para identificar as informações de Suspensão de exigibilidade de Tributos\. Será gerado considerando os seguintes critérios: Tabela REINF\_PGER\_R1070\_OC campo “IND\_OPER” igual a “A”
- __Campos\-Chave__: codSusp
- __Nível hierárquico do registro__: filho do registro ideProcesso\.
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: para cada ideProcesso poderá existir “50” infoSusp\.

MFS10757

RN28

__Campo codSusp__

Informação será recuperada do campo COD\_SUSP da SAFX2059\.

MFS10757

RN29

__Campo indSusp__

Informação será recuperada do campo IND\_SUSP da SAFX2059\.

MFS10757

RN30

__Campo dtDecisao__

Informação será recuperada do campo DAT\_DECISAO da SAFX2059\.

MFS10757

RN31

__Campo indDeposito__

Informação será recuperada do campo IND\_DEPOSITO da SAFX2059\.

MFS10757

- __Registro dadosProcJud \- Informações Complementares do Processo Judicial__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN32

- __Origem das informações__: SAFX2058\.
- __Regra de seleção__: Este registro servirá para identificar as informações Complementares do Processo Judicial\. Será gerado considerando os seguintes critérios: Tabela REINF\_PGER\_R1070\_OC campo “IND\_OPER” igual a “A”
- __Campos\-Chave__: 
- __Nível hierárquico do registro__: filho do registro ideProcesso
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Poderá existir 1 ou não existir\.

MFS10757

RN33

__Campo ufVara__

Informação será recuperada do campo COD\_ESTADO da SAFX2058\.

Caso campo não preenchido exibir a seguinte mensagem no log de pré\-geração:

Evento R1070 – Registro Informações Complementares do Processo Judicial 

“Campo UF Seção Judiciária do cadastro de processos não preenchido”

Identificação do Processo: Tipo do Processo: XXXXX / N° do Processo: XXXXX / Validade Inicial: XXXXXX

MFS10757

RN34

__Campo codMunic__

Informação será recuperada do campo COD\_MUNICIPIO da SAFX2058\.

__\[ALTERADO MFS15750\]__

Caso campo não preenchido exibir a seguinte mensagem no log de pré\-geração:

Evento R1070 – Registro Informações Complementares do Processo Judicial

“Campo Código Município não preenchido”

Identificação do Processo: Tipo do Processo: XXXXX / N° do Processo: XXXXX / Validade Inicial: XXXXXX

MFS10757

MFS15750

RN35

__Campo idVara__

Informação será recuperada do campo COD\_VARA da SAFX2058\.

Caso campo não preenchido exibir a seguinte mensagem no log de pré\-geração:

Evento R1070 – Registro Informações Complementares do Processo Judicial 

“Campo Identificação da Vara do cadastro de processos não preenchido”

Identificação do Processo: Tipo do Processo: XXXXX / N° do Processo: XXXXX / Validade Inicial: XXXXXX

MFS10757

RN36

__Campo indAutoria__

Recuperar a informação do campo IND\_AUTORIA da SAFX2058\.

MFS10757

MFS13810

- __Registro novaValidade \- Informações exclusiva em caso de alteração do período de validade de registro__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN36

- __Origem das informações__: SAFX2058\.
- __Regra de seleção__: Este registro servirá para identificar as informações de alteração do período de validade do registro\. Será gerado considerando os seguintes critérios: Caso identificado uma alteração do processo quanto à data início e/ou fim validade, este será considerado como um novo processo, ou seja, esta alteração de período de validade será a condição para o registro ser gerado\.
- __Campos\-Chave__: iniValid, fimValid
- __Nível hierárquico do registro__: filho do registro Alteracao
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Poderá existir 1 ou não existir\.

MFS10757

MFS17237

RN37

__Campo iniValid__

Informação será recuperada do campo VALID\_PROC\_ADJ\_INI da SAFX2058\.

MFS10757

RN38

__Campo fimValid__

Informação será recuperada do campo VALID\_PROC\_ADJ\_FIM da SAFX2058\.

MFS10757

- __Registro InfoProcesso/IdePeriodo \- Informações do processo \(Exclusão\)__

###### __CÓD__

###### __DESCRIÇÃO__

###### __OS/CH__

RN39

- Origem das informações: SAFX2058
- Regra de seleção: Este registro servirá identificar o período de validade das informações de Processo\. Será gerado considerando os seguintes critérios: Tabela REINF\_PGER\_R1070\_OC campo “IND\_OPER” igual a “E”
- Campos\-Chave: iniValid, fimValid
- Nível hierárquico do registro: filho do registro exclusao\.
- Ordenação: Não se aplica\.
- Agrupamento: Não se aplica\.
- Ocorrência: Um por arquivo\.

MFS10757

RN40

__Campo iniValid__

Informação será recuperada do campo VALID\_PROC\_ADJ\_INI da SAFX2058\.

MFS10757

RN41

__Campo fimValid__

Informação será recuperada do campo VALID\_PROC\_ADJ\_FIM da SAFX2058\.

MFS10757

- __Registro ideProcesso – Identificação do Processo__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN42

- __Origem das informações__: SAFX2058\.
- __Regra de seleção__: Este registro servirá identificar o processo\. Será gerado considerando os seguintes critérios: Tabela REINF\_PGER\_R1070\_OC campo “IND\_OPER” igual a “E”\. Esse registro será gerado se o usuário efetuar uma exclusão das Informações de Suspensão de Exigibilidade de Tributos \(SAFX2059\) tanto manualmente pela tela de cadastro no Módulo DW \(Manutenção > Códigos > Processo Administrativo Judicial \(REINF/eSocial\)\) como também pela exclusão efetuada pelo módulo Ferramentas \(Rotinas Acessórias > Inicialização > Exclusão Processo Administrativo Judicial \(REINF/eSocial\)\)\. 
- __Campos\-Chave__: tpProc, nrProc
- __Nível hierárquico do registro__: filho do registro exclusao
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Um por arquivo\.

MFS10757

MFS10287

RN43

__Campo tpProc__

Informação será recuperada do campo IND\_TP\_PROC\_ADJ da SAFX2058

MFS10757

RN44

__Campo nrProc__

Informação será recuperada do campo NUM\_PROC\_ADJ da SAFX2058

MFS10757

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

