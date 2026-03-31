# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX701

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX701.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 73 KB

---

THOMSON REUTERS

701

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

CH17082\_2015

Julyana Perrucini

Este documento tem como objetivo alterar a verificação da existência de registro pai na X07\_Docto\_Fiscal incluindo o modelo de documento 15 para o Ato Cotepe\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN00

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX701 – Tabela de Informações de Manifesto de Vôo / Bilhete ou Recibo de Passageiro, que deve ser criada com a seguinte estrutura:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Código da Empresa

A

003

NÃO

SIM

Código do Estabelecimento

A

006

NÃO

SIM

Movimento Entrada/Saída

A

001

NÃO

SIM

Normal ou Devolução

A

001

NÃO

SIM

Tipo de Documento

A

005

NÃO

SIM

Indicador de Pessoa Física/Jurídica

A

001

NÃO

SIM

Código/Destinatário/Emitente/Remetente

A

014

NÃO

SIM

Número do Documento Fiscal/Número do Mapa Resumo de Caixa

A

012

NÃO

SIM

Série do Documento Fiscal

A

003

NÃO

SIM

SubSérie do Documento Fiscal

A

002

NÃO

SIM

Data de Emissão

N

008

NÃO

SIM

Identificação de Vôo

A

010

NÃO

SIM

Unidade da Federação do Documento Fiscal

A

002

NÃO

NÃO

Quantidade de Passageiros Võo

N

004

NÃO

NÃO

Conexão

A

010

NÃO

NÃO

Indicador de Classe da Passagem

A

001

NÃO

NÃO

Poltrona

A

004

NÃO

NÃO

CPF do Participante

 N 

011

NÃO

NÃO

Nome do Participante

A

100

NÃO

NÃO

 

RN01

__Campo Tipo do Documento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido\. Utilizar a mensagem “90119” da TFIX22: “O Campo Codigo do Tipo de Documento nao esta preenchido\.”\.

Deve ser exibida mensagem de erro caso esteja preenchido, mas não validar o grupo\. Utilizar a mensagem “90470” da TFIX22: “Nao foi possivel recuperar para o estabelecimento o grupo de centralizacao do Codigo de Tipo de Documento\.”\.

Deve ser exibida mensagem de erro caso esteja preenchido, mas não estiver cadastrado na SAFX2005\. Utilizar a mensagem “90125” da TFIX22: “O Codigo do Tipo de Documento nao esta cadastrado”\.

__\[ALTERADA \- CH17082\_2015\]__

Faz verificação da existência do registro pai na SAFX07 quando o campo Código Modelo NF \(código do modelo do Ato Cotepe\) for igual a 15, 29, 30\.

Se o campo Identificação de Voo não estiver preenchido então

    Utilizar a mensagem “91422” da TFIX22: “O Campo Identificacao do Voo deve ser preenchido\.”\.

Se o campo Quantidade de Passageiros Voo estiver preenchido e estiver inválido então

    Utilizar a mensagem “91423” da TFIX22: “A quantidade de Passageiros embarcados invalida\.”\.

Verifica o preenchimento de campos na SAFX701:

Se o campo Código Modelo NF for igual a 15 e 29 então

  Se o campo CPF do Participante estiver preenchido então

    Utilizar a mensagem “91455” da TFIX22: “CPF do participante nao deve ser preenchido para o Manifesto de Voo\.”\.

   Se o campo Nome do Participante estiver preenchido então

     Utilizar a mensagem “91456” da TFIX22: “Nome do participante nao deve ser preenchido para o Manifesto de Voo\.”\.

   Se o campo Indicador de Classe da Passagem estiver preenchido então

     Utilizar a mensagem “91457” da TFIX22: “Classe da passagem nao deve ser preenchida para o Manifesto de Voo\.”\.

   Se o campo Indicador de Poltrona estiver preenchido então

     Utilizar a mensagem “91458” da TFIX22: “Numero da poltrona nao deve ser preenchido para o Manifesto Voo\.”\.

   Se o campo Indicador de Conexão estiver preenchido então

     Utilizar a mensagem “91458” da TFIX22: “Conexao nao deve ser preenchida para o Manifesto Voo\.”\.

Senão o campo Código Modelo NF for igual a 30 então

  Se o campo Classe da Passagem estiver preenchido e estiver com valor diferente de 0, 1, 2 então

    Utilizar a mensagem “91469” da TFIX22: “O indicador da Classe da Passagem deve conter os valores  0  , 1  ou  2”\.

  Se o campo Unidade da Federação do Documento Fiscal estiver preenchido então

    Utilizar a mensagem “91460” da TFIX22: “UF de emissao do documento manifesto nao deve ser preenchido para o Bilhete/Recibo\.”\.

  Se o campo Quantidade de Passageiros Voo estiver preenchido então

    Utilizar a mensagem “91461” da TFIX22: “Quantidade de passageiros voo nao deve ser preenchido para o Bilhete/Recibo\.”\.

  Se o campo CPF do Participante estiver preenchido então

    Valida formato da Receita Federal

      Se CPF do Participante com erro então

        Utilizar a mensagem “90063” da TFIX22: “Numero de CPF informado nao e valido, conforme regras da Receita Federal\.”\.

   Senão 

        Utilizar a mensagem “91432” da TFIX22: “CPF do participante passageiro deve ser preenchido\.”\.

CH17082\_2015

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

