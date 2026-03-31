# MTZ_REINF_Geracao_Evento_Cadastro_R1050

- **Fonte:** MTZ_REINF_Geracao_Evento_Cadastro_R1050.docx
- **Modificado:** 2023-11-16
- **Tamanho:** 78 KB

---

THOMSON REUTERS

Geração evento R\-1050\- Tabela de Entidades Ligada 

 REINF

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

MFS\-79881

Alessandra Cristina Navatta

Geração do Evento R\-1050 – Tabela de Entidades Ligadas \(atendimento ao layout versão 2\.1\)

MFS\-90001

Alessandra Cristina Navatta

Alteração da versão 2\.1 para 2\.1\.1 e referência do arquivo de de\_para

__Obs\. Os ajustes mapeados nesta demanda, referem\-se a atualização funcional\. Não há impactos na implementação__

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS__

RN00

__Regra Geral de Geração do Evento R\-1050\.__

O evento R\-1050 do SPED \- REINF tem por objetivo gerar informações de tabela de entidades ligadas\. Ele será gerado com os registros:

__Reinf__ – EFD \- Reinf

__evtTabLig – __Evento Tabela de Entidades Ligadas

__ideEvento – __Informações de Identificação do Evento

__ideContri – __Informações de identificação do contribuinte

__infoLig __\- Informações relacionadas a entidades ligadas

__inclusao \-__ Inclusão de novas informações

__ideEntLig __– Identificação da entidade ligada

__alteracao __\- Alteração das informações

__ideEntLig __– Identificação da entidade ligada

__novaValidade __\- Novo período de validade das informações que estão sendo alteradas

__exclusao __\- Exclusão das informações

__ideEntLig __– Identificação da entidade ligada

Observar orientações existentes no arquivo “TR\_REINF\_DEXPARA\_V2\.1\.1\.xlsx"\.

- __Origem das informações__: Tela Tabela de Entidades Ligadas
- __Regra de seleção__: O Registro R\-1050 é utilizado para demonstrar informações da tabela de entidades ligadas\.

Para obtermos as informações para sua geração, devemos recuperar as informações da tela “Tabela de Entidades Ligadas”, considerando o registro vigente da tabela de entidade, ou seja, data inicial e final de validade da tabela entidade deve estar compreendida no período de geração do REINF \.

__Mensageria Log:__ 

Se o evento anterior do processo já tiver sido enviado e não tiver retorno ainda \(status 2 \- “Evento REINF Enviado”\) então exibir a seguinte mensagem: 

      Evento R1050 – Tabela de Entidades Ligadas

     “Evento não gerado\. Existe evento anterior que foi enviado e ainda aguarda retorno\.”

Identificação do Processo: Tipo do Processo: XXXXX / N° do Processo: XXXXX / Validade Inicial:XXXX

Se não existir evento anterior do processo recebido com sucesso/advertencia no fisco\. Não posso gerar evento de exclusão, então exibir a seguinte mensagem: 

       Evento R1050 – Tabela de Entidades Ligadas

      “Evento de exclusão não gerado\. Não existe evento anterior enviado para o fisco e recebido com sucesso ou advertência\.”

Identificação do Processo: Tipo do Processo: XXXXX / N° do Processo: XXXXX / Validade Inicial:XXXXX

MFS\-79881

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

- __Origem das informações__: Tela Informações do Contribuinte\.
- __Regra de seleção__: Este registro servirá para identificar o Contribuinte
- __Campos\-Chave__: tpInsc, nrInsc
- __Nível hierárquico do registro__: filho do registro evtTabLig
- __Ordenação__: não se aplica\.
- __Agrupamento__: não se aplica\.
- __Ocorrência__: Um por arquivo

MFS\-10757

RN02

__Campo tpInsc__

Será gerado com conteúdo igual a “1”\. 

MFS\-79881

RN03

__Campo nrInsc__

Será gerado com as 8 primeiras posições do CNPJ do Estabelecimento\.

MFS\-79881

- __Registro InfoLig – Informações Relacionadas a Entidades Ligadas__

###### __CÓD__

###### __DESCRIÇÃO__

__MFS__

RN04

- __Origem das informações__: Tela Tabela de Entidades Ligadas
- __Nível hierárquico do registro__: filho do registro evtTabLig
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Um por arquivo\.

MFS\-79881

RN05

__Campo tpEntLig__

- Informação será recuperada do campo ‘Classificação da Entidade Ligada’ da Tela ‘Tabela de Entidades Ligadas’\.

 

MFS\-79881

RN06

__Campo cnpjLig__

- Informação será recuperada do campo ‘CNPJ da Entidade Ligada’ da Tela ‘Tabela de Entidades Ligadas’\.

MFS\-79881

RN07

__Campo iniValid__

- Informação será recuperada do campo ‘Validade Inicial’ da Tela ‘Tabela de Entidades Ligadas’\.

MFS\-79881

RN08

__Campo fimValid__

- Informação será recuperada do campo ‘Validade Final’ da Tela ‘Tabela de Entidades Ligadas’\.

MFS\-79881

- __Registro Alteração – Alteração de Informações __

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN09

- __Origem das informações__: Tela Tabela de Entidades Ligadas\.
- __Nível hierárquico do registro__: filho do registro infoLig
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Um por arquivo\.

MFS\-79881

RN10

__Campo tpEntLig__

- Informação será recuperada do campo ‘Classificação da Entidade Ligada’ da Tela ‘Tabela de Entidades Ligadas’\.

 

MFS\-79881

RN11

__Campo cnpjLig__

- Informação será recuperada do campo ‘CNPJ da Entidade Ligada’ da Tela ‘Tabela de Entidades Ligadas’\.

MFS\-79881

RN12

__Campo iniValid__

- Informação será recuperada do campo ‘Validade Inicial’ da Tela ‘Tabela de Entidades Ligadas’\.

MFS\-79881

RN13

__Campo fimValid__

- Informação será recuperada do campo ‘Validade Final’ da Tela ‘Tabela de Entidades Ligadas’\.

MFS\-79881

- __Registro Nova Validade – Nova Validade das Informações__

###### __CÓD__

###### __DESCRIÇÃO__

__MFS__

RN14

- __Origem das informações__: Tela Tabela de Entidades Ligadas\.
- __Regra de seleção__: Este registro servirá para identificar as informações de alteração do período de validade do registro\. Será gerado considerando os seguintes critérios: Caso identificado uma alteração das informações do contribuinte quanto à data inicio e/ou fim validade, este será considerado como um novo cadastro, ou seja, esta alteração de período de validade será a condição para o registro ser gerado\.
- __Campos\-Chave__: 
- __Nível hierárquico do registro__: filho do registro alteracao
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Um por arquivo\.

MFS\-79881

RN15

__Campo iniValid__

- Informação será recuperada do campo ‘Validade Inicial’ da Tela ‘Tabela de Entidades Ligadas’\.

MFS\-79881

RN16

__Campo fimValid__

- Informação será recuperada do campo ‘Validade Final’ da Tela ‘Tabela de Entidades Ligadas’\.

MFS\-79881

- __Registro exclusao – Exclusão de Informações __

###### __CÓD__

###### __DESCRIÇÃO__

###### __MFS__

RN17

- __Origem das informações__: Tela Tabela de Entidades Ligadas\.
- Regra de seleção: Este registro servirá identificar o período de validade das informações de Entidades Ligadas\. Será gerado considerando os seguintes critérios: Tabela REINF\_PGER\_R1050\_OC campo “IND\_OPER” igual a “E”
- Campos\-Chave: iniValid, fimValid
- Nível hierárquico do registro: filho do registro InfoLig
- Ordenação: Não se aplica\.
- Agrupamento: Não se aplica\.
- Ocorrência: Até um por arquivo\.

MFS\-79881

RN18

__Campo cnpjLig__

- Informação será recuperada do campo ‘CNPJ da Entidade Ligada’ da Tela ‘Tabela de Entidades Ligadas’\.

MFS\-79881

RN19

__Campo iniValid__

- Informação será recuperada do campo ‘Validade Inicial’ da Tela ‘Tabela de Entidades Ligadas’\.

MFS\-79881

RN20

__Campo fimValid__

- Informação será recuperada do campo ‘Validade Final’ da Tela ‘Tabela de Entidades Ligadas’\.

MFS\-79881

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

