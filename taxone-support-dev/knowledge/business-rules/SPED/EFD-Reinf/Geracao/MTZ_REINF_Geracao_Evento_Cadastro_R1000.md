# MTZ_REINF_Geracao_Evento_Cadastro_R1000

- **Fonte:** MTZ_REINF_Geracao_Evento_Cadastro_R1000.docx
- **Modificado:** 2025-06-20
- **Tamanho:** 94 KB

---

THOMSON REUTERS

Geração evento R\-1000 \- REINF

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-10819

Elenilson Coutinho

Definição de regras para geração do evento de Cadastro R\-1000 Reinf 

MFS14930

Lara Aline

Ajuste na geração do campo nrInsc

MFS15750

Lara Aline

Ajuste no Layout conforme v1\.3\.

MFS17237

Lara Aline

Ajuste na tag novaValidade e nos campos iniValid e fimValid da tag infoContri do tipo Alteração\.

MFS18226

Lara Aline

Inclusão regra para geração do evento R\-1000 de Limpeza para o Tipo de Ambiente = Produção Restrita\.

MFS20215

Lara Aline

Ajuste no campo foneFixo \(RN16\)

MFS\-81450

Alessandra Cristina Navatta

Ajuste no Layout conforme V2\.1

Atualização do documento, referenciando a tela “Informações do Contribuinte” ao invés da tela de “Dados Iniciais” nos registros Informações de Identificação do Contribuinte, InfoContri, infoCadastro – Informações do Contribuinte; Contato – Informações de Contato, softHouse – Informações da empresa desenvolvedora das aplicações, novaValidade \- Informações exclusiva em caso de alteração do período de validade de registro e IdePeriodo \- Informações do processo \(Exclusão\)

MFS\-90001

Alessandra Cristina Navatta

Alteração da versão 2\.1 para 2\.1\.1 e referência do arquivo de de\_para

Obs\. Os ajustes mapeados nesta demanda, referem\-se a atualização funcional\. Não há impactos na implementação

MFS\-523048

Alessandra Cristina Navatta

Inclusão da regra do campo indUniao \(inclusão e alteração\) 

MFS\-840399

Alessandra Cristina Navatta

Inclusão da regra do campo indPertIRRF \(inclusão e alteração\), para atendimento do evento R\-1000, versão 2\.1\.2 \(Nota Técnica 02/2025\)

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS__

RN00

__Regra Geral de Geração do Evento R\-1000\.__

O evento R\-1000 do SPED \- REINF tem por objetivo gerar informações de Processo\. Ele será gerado com os registros:

__Reinf__ – EFD \- Reinf

__evtInfoContri – __Evento de informações do Contribuinte

__ideEvento – __Informações de Identificação do Evento

__ideContri – __Informações de identificação do contribuinte

__infoContri __\- Informações do Processo

__inclusão \-__ Inclusão de novas informações

__idePeriodo __\- Período de validade das informações incluídas

__infoCadastro __\- Informações do Contribuinte

__contato __\- Informações de contato

__softHouse __\- Informações da empresa desenvolvedora da aplicação que gera os arquivos

__infoEFR \- __Informações de órgãos públicos estaduais e municipais relativas a Ente Federativo Responsável \- EFR \(não geramos essa TAG\)

__alteracao __\- Alteração das informações

__idePeriodo __\- Período de validade das informações alteradas

__infoCadastro __\- Informações do contribuinte

__contato __\- Informações de contato

__softHouse __\- Informações da empresa desenvolvedora da aplicação que gera os arquivos

__infoEFR \- __Informações de órgãos públicos estaduais e municipais relativas a Ente Federativo Responsável \- EFR \(não geramos essa TAG\)

__novaValidade __\- Novo período de validade das informações

__exclusão __\- Exclusão das informações

__idePeriodo __\- Período de validade das informações excluídas

Observar orientações existentes no arquivo "TR\_REINF\_DEXPARA\_V2\.1\.1\.xlsx"\.

- __Origem das informações__: Tela de Cadastro de Informações do Contribuinte
- __Regra de seleção__: O Registro R\-1000 é utilizado para demonstrar informações do Contribuinte

Para obtermos as informações para sua geração, devemos recuperar as informações da tela de “Informações do Contribuinte”

__Mensageria Log:__ 

Se o evento anterior do processo já tiver sido enviado e não tiver retorno ainda \(status 2 \- “Evento REINF Enviado”\) então exibir a seguinte mensagem: 

 Evento R1000 – Informações do Contribuinte

“Evento não gerado\. Existe evento anterior que foi enviado e ainda aguarda retorno\.”

Identificação do Contribuinte: Tipo Inscrição: X / N° de Inscrição: XXXXXXXX / Validade Inicial: XXXXX / Cód\. do Estab\.: XXXXXX

Se não existir evento anterior do processo recebido com sucesso/advertencia no fisco\. Não posso gerar evento de exclusão, então exibir a seguinte mensagem: 

 Evento R1000 – Informações do Contribuinte

“Evento de exclusão não gerado\. Não existe evento anterior enviado para o fisco e recebido com sucesso ou advertência\.”

Identificação do Contribuinte: Tipo Inscrição: X / N° de Inscrição: XXXXXXXX / Validade Inicial: XXXXX / Cód\. do Estab\.: XXXXXX

__MFS\-18226\]__

- __Limpeza da Base de Pré\-Produção:__ Critérios de geração do evento:

O evento R\-1000 de limpeza será responsável por apagar todos os dados de determinado contribuinte, ou seja, todos os eventos já gerados ou enviados do contribuinte com sucesso ou não serão excluídos do governo, mensageria e DW\. Porém apenas se o Tipo de Ambiente for 2 – Produção Restrita para o contribuinte que o usuário desejar excluir os dados\.

Dessa forma o critério principal para possibilidade de geração desse evento é o Tipo de Ambiente = 2 – Produção Restrita\.

Critério para apresentar o evento de Limpeza R\-1000 no Painel de Controle de Eventos:

1 \- O evento R\-1000 de Limpeza será apresentado no painel de controle de eventos para geração apenas se existir um evento R\-1000 com a situação Evento Recebido pelo fisco com sucesso/advertência e o Tipo de Ambiente = 2 – Produção Restrita de acordo com os dados pesquisados no Parâmetro para consulta, ou seja, apenas se o governo já recebeu a informação cadastral de determinado contribuinte\. Nesse caso o evento R\-1000 de Limpeza será demostrado com a situação Aguardando Geração de XML no Painel\. 

2 \- O evento R\-1000 de Limpeza será demostrado no painel se o evento R\-1000 de ‘Limpeza’ já tiver sido recebido pelo fisco com sucesso \(Situação: Evento Recebido pelo fisco com sucesso/advertência\) nesse caso irá aparecer no painel apenas para consulta do usuário \(Histórico\)\.

Esse evento de Limpeza será igual a um evento de R\-1000 original de inclusão, com a diferença de existir uma tag <verProc>RemoverContribuinte</verProc>

A geração/envio do evento R\-1000 de Limpeza é possível para o status abaixo:

1 \- Aguardando Geração do XML\.

Abaixo será listado os status que será possível efetuar outro envio e geração do evento, caso ocorra algum erro na primeira tentativa de envio/geração:

14 \- Evento Excluído na Mensageria;

4 \- Erro na Geração do XML; 

15 \- Erro Técnico na Mensageria;

6 \- Evento Rejeitado pela Mensageria;

10 \- Evento Rejeitado pelo Fisco\.

MFS\-10819

MFS18226

MFS\-81450

MFS\-90001

- __Registro ideEvento – Informações de Identificação do Evento__

###### __CÓD__

###### __DESCRIÇÃO__

__MFS__

- __Registro ideContri – Informações de Identificação do Contribuinte__

###### __CÓD__

###### __DESCRIÇÃO__

__MFS__

RN01

__Origem das informações__: Tela de “Informações do Contribuinte”\.

- __Regra de seleção__: Este registro servirá para identificar o Contribuinte\.
- __Campos\-Chave__: tpInsc, nrInsc
- __Nível hierárquico do registro__: filho do registro evtInfoContri
- __Ordenação__: não se aplica\.
- __Agrupamento__: não se aplica\.
- __Ocorrência__: Um por arquivo

MFS\-10819

RN02

__Campo tpInsc__

Será gerado com conteúdo igual a “1”\. 

MFS\-10819

RN03

__Campo nrInsc__

Será gerado com as 8 primeiras posições do CNPJ do Estabelecimento\. 

MFS14821

- __Registro InfoContri__

###### __CÓD__

###### __DESCRIÇÃO__

__MFS__

RN04

__Origem das informações__: Tela de “Informações do Contribuinte”\.

- __Regra de seleção__: Este registro servirá para identificar informações do Contribuinte\. Será gerado considerando os seguintes critérios: Tabela REINF\_PGER\_R1000\_OC campo “IND\_OPER” igual a “I” \(Inclusão\) e “A” \(Alteração\)
- __Campos\-Chave__: 
- __Nível hierárquico do registro__: filho do registro evtInfoContri\.
- __Ordenação__: Não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Um por arquivo\.

MFS\-10819

RN05

__Campo iniValid__

Informação será recuperada do campo Início Validade da tela de “Informações do Contribuinte”\.

\.

__\[Alterado MFS17237\]__

__Importante:__

Para o tipo de arquivo = ‘Alteração’ \(campo “IND\_OPER” igual a “A” \- Alteração\):

Nesse caso a informação recuperada do campo Início Validade da tela de “Informações do Contribuinte” será a informação sem a alteração, ou seja, a data informada anteriormente no registro que se pretende alterar\. A informação nova alterada será gerada no Registro novaValidade\.

MFS\-10819

MFS17237

RN06

__Campo fimValid__

Informação será recuperada do campo Fim Validade da Tela de “Informações do Contribuinte”\.

\.

__\[Alterado MFS17237\]__

__Importante:__

Para o tipo de arquivo = ‘Alteração’ \(campo “IND\_OPER” igual a “A” \- Alteração\):

Nesse caso a informação recuperada do campo Início Validade da tela de  “Informações do Contribuinte” será a informação sem a alteração, ou seja, a data informada anteriormente no registro que se pretende alterar\. A informação nova alterada será gerada no Registro novaValidade\.

MFS\-10819

MFS17237

- __Registro infoCadastro – Informações do Contribuinte__

###### __CÓD__

###### __DESCRIÇÃO__

__MFS__

RN07

__Origem das informações__: Tela de Informações do Contribuinte\.

- __Regra de seleção__: Este registro servirá para identificar informações do Contribuinte\. Será gerado considerando os seguintes critérios: Tabela REINF\_PGER\_R1000\_OC campo “IND\_OPER” igual a “I” \(Inclusão\) e “A” \(Alteração\)
- __Campos\-Chave__: 
- __Nível hierárquico do registro__: filho do registro Inclusão
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Um por arquivo\.

MFS\-10819

MFS\-81450

RN08

__Campo ClassTrib__

Informação será recuperada do campo Classificação Tributária da tela de “Informações do Contribuinte”\.

MFS\-10819

MFS\-81450

RN09

__indEscrituracao__

Informação será recuperada do campo Escrituração Contábil na ECD da Tela de “Informações do Contribuinte”

MFS\-10819

MFS\-81450

RN10

__indDesoneracao__

Informação será recuperada do campo Desoneração da Folha da Tela de “Informações do Contribuinte”\.

MFS\-10819

MFS\-81450

RN11

__indAcordoIsenMulta__

Informação será recuperada do campo Acordo de Isenção de Multa da Tela de “Informações do Contribuinte”\.

__\[ALTERADO MFS15750\]__

Caso preenchido ‘1 – Com acordo’ e o campo ClassTrib for preenchido com valor diferente de ‘60’ exibir a seguinte mensagem no log de pré\-geração:

Evento R1000 – Registro Informações do Contribuinte

“Campo ’Indicativo da existência de acordo internacional para isenção de multa’ só pode ser igual a ‘1’ se campo ‘Classificação Tributária’ for igual a ‘60’”

Identificação do Contribuinte: Número de Inscrição: XXXXXXXXXXXX 

MFS\-10819

MFS15750

MFS\-81450

RN12

__indSitPJ__

Informação será recuperada do campo Situação Pessoa Jurídica da Tela de “Informações do Contribuinte”\.

MFS\-10819

MFS\-81450

RN12\.1

__indUniao__

Este campo passa a existir no REINF, a partir da versão 2\.1 2\.1\.1 do REINF\.

__\[ALTERAÇÃO MFS\-523048\]__ \- Informação será recuperada do campo Indicativo de Entidade Vinculada a União’ da Tela de “Informações do Contribuinte”\.Caso o campo esteja sem informação na tela, não gerar este campo\.

Campo não Obrigatório

MFS\-81450

MFS\-90001

MFS\-523048

RN12\.2

__dtTransfFinsLucr__

Este campo passa a existir no REINF, a partir da versão 2\.1 2\.1\.1 do REINF\.

Informação será recuperada do campo ‘Data da Transformação de Entidade Beneficente de Assistência Social Isenta de Contribuições Sociais em Sociedade com Fins Lucrativos \- Art\. 13 \- Lei 11096/2005\.’ da Tela de “Informações do Contribuinte”\. 

Campo não Obrigatório

MFS\-81450

MFS\-90001

RN12\.3

__dtObito__

Este campo passa a existir no REINF, a partir da versão 2\.1 2\.1\.1 do REINF\.

Este campo só deve ser informado, quando tpInsc do contribuinte for igual a \[2\], como não geramos essa opção, não preencher este campo\.

Campo não Obrigatório

MFS\-81450

MFS\-90001

RN12\.4

Este campo passa a existir no REINF, a partir da versão 2\.1\.2 do REINF\.

Informação será recuperada do campo Pertencimento do IRRF da Tela de “Informações do Contribuinte”,  se o campo estiver marcado gravar ‘S’, caso contrário, não gravar nada\. 

Campo não Obrigatório

MFS\-840399

- __Registro Contato – Informações de Contato__

###### __CÓD__

###### __DESCRIÇÃO__

__MFS__

RN13

- __Origem das informações__: Tela de “Informações do Contribuinte”\.
- __Regra de seleção__: Este registro servirá para identificar informações do Contribuinte\. Será gerado considerando os seguintes critérios: Tabela REINF\_PGER\_R1000\_OC campo “IND\_OPER” igual a “I” \(Inclusão\) e “A” \(Alteração\)\.
- __Campos\-Chave__: codSusp
- __Nível hierárquico do registro__: filho do registro infoCadastro\.
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Um por Arquivo\.

MFS\-10819

MFS\-81450

RN14

__Campo nmCtt__

Informação será recuperada do campo Nome do Contato da tela de “Informações do Contribuinte”\.

MFS\-10819

MFS\-81450

RN15

__Campo cpfCtt__

Informação será recuperada do campo CPF da tela de “Informações do Contribuinte”\.

MFS\-10819

MFS\-81450

RN16

__Campo foneFixo__

Informação será recuperada do campo Telefone da tela de “Informações do Contribuinte”\.

__\[MFS20215\]__

Obs: Caso número de telefone seja maior que 10 posições a informação será truncada no XML, utilizando as 10 ultimas posições da direita para esquerda\.

MFS\-10819

MFS20215

MFS\-81450

RN17

__Campo foneCel__

Informação será recuperada do campo Celular da tela de “Informações do Contribuinte”\.

MFS\-10819

MFS\-81450

RN18

__Campo email__

Informação será recuperada do campo email da tela de “Informações do Contribuinte”\.

MFS\-10819

MFS\-81450

- __Registro softHouse – Informações da empresa desenvolvedora das aplicações\.__

###### __CÓD__

###### __DESCRIÇÃO__

__MFS__

RN19

- __Origem das informações__: Tela Informações do Contribuinte
- __Regra de seleção__: Este registro servirá para identificar informações do Contribuinte\. Será gerado considerando os seguintes critérios: Tabela REINF\_PGER\_R1000\_OC campo “IND\_OPER” igual a “I” \(Inclusão\) e “A” \(Alteração\)\.
- __Campos\-Chave__: 
- __Nível hierárquico do registro__: filho do registro infoCadastro
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Poderá existir nenhum ou 99\.

MFS\-10819

MFS\-81450

RN20

__Campo cnpjSoftHouse__

Informação será recuperada do campo CNPJ da tela de “Informações do Contribuinte”\.

MFS\-10819

MFS\-81450

RN21

__Campo nmRazao__

Informação será recuperada do campo Nome/Razão da tela de “Informações do Contribuinte”\.\.

MFS\-10819

MFS\-81450

RN22

__Campo nmCont__

Informação será recuperada do campo Nome do contato da tela de  “Informações do Contribuinte”\.

MFS\-10819

MFS\-81450

RN23

__Campo telefone__

Informação será recuperada do campo telefone da tela de “Informações do Contribuinte”\.

MFS\-10819

MFS\-81450

RN24

__Campo email__

Informação será recuperada do campo E\-mail da tela de “Informações do Contribuinte”\.

MFS\-10819

MFS\-81450

- __Registro infoEFR – Informações de órgãos públicos estaduais e municipais relativas a Ente Federativo Responsável \- EFR__

###### __CÓD__

###### __DESCRIÇÃO__

__MFS__

RN24

Esta tag não é gerada pelo sistema, pois, não temos clientes de Órgãos Públicos

MFS\-81450

- __Registro novaValidade \- Informações exclusiva em caso de alteração do período de validade de registro__

###### __CÓD__

###### __DESCRIÇÃO__

__MFS__

RN25

- __Origem das informações__: SAFX2058\.
- __Regra de seleção__: Este registro servirá para identificar as informações de alteração do período de validade do registro\. Será gerado considerando os seguintes critérios: Caso identificado uma alteração das informações do contribuinte quanto à data inicio e/ou fim validade, este será considerado como um novo cadastro, ou seja, esta alteração de período de validade será a condição para o registro ser gerado\.
- __Campos\-Chave__: iniValid, fimValid
- __Nível hierárquico do registro__: filho do registro Alteracao
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Poderá existir 1 ou não existir\.

MFS\-10819

MFS17237

RN26

__Campo iniValid__

Informação será recuperada do campo Início Validade da tela de “Informações do Contribuinte”\.

MFS\-10819

MFS\-81450

RN27

__Campo fimValid__

Informação será recuperada do campo Fim Validade da tela de “Informações do Contribuinte”\.

MFS\-10819

MFS\-81450

- __Registro IdePeriodo \- Informações do processo \(Exclusão\)__

###### __CÓD__

###### __DESCRIÇÃO__

###### __MFS__

RN28

- Origem das informações: SAFX2058
- __Regra de seleção__: Este registro servirá para identificar informações do Contribuinte\. Será gerado considerando os seguintes critérios: Tabela REINF\_PGER\_R1000\_OC campo “IND\_OPER” igual a “E”\.
- Campos\-Chave: iniValid, fimValid
- Nível hierárquico do registro: filho do registro exclusao\.
- Ordenação: Não se aplica\.
- Agrupamento: Não se aplica\.
- Ocorrência: Um por arquivo\.

MFS\-10819

RN29

__Campo iniValid__

Informação será recuperada do campo Início Validade da tela de “Informações do Contribuinte”\.

MFS\-10819

MFS\-81450

RN30

__Campo fimValid__

Informação será recuperada do campo Fim Validade da tela de “Informações do Contribuinte”\.

MFS\-10819

MFS\-81450

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

