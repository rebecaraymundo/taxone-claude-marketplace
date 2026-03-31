# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2104

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2104.docx
- **Modificado:** 2024-03-06
- **Tamanho:** 71 KB

---

THOMSON REUTERS

Regras de Importação Online e Batch SAFX2104

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS3835\-C11

Marcos G\. de Paula

Definição das regras de importação, Online e Batch, da SAFX2104\.

CH9543/2014

Marcos G\. de Paula

Ajuste na regra de validação da conta contábil\.

MFS11008

Lara Aline

Ajuste para inclusão da RN00\. Possibilidade de validação dos dados também pela SAFX225\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN00

__Regras Gerais__

A rotina de importação, online e batch da tabela SAFX2104 \- Lançamento Contábil X Histórico do Fato Contábil é validada com os dados da SAFX01\.

Quando o parâmetro “Gerar BP e DRE com base nos valores em Moeda Funcional” da tela de Dados Iniciais da ECD estiver selecionado, deverá considerar também os dados da SAFX225, considerando o registro da tabela SAFX225 do estabelecimento centralizador e seus centralizados\. 

MFS11008

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX203 \- Lançamentos de Ajuste EFD\-Contribuições Financeiras, que deve ser criada com a seguinte estrutura:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Código da Empresa

A

003

SIM

SIM

Código do Estabelecimento

A

006

SIM

SIM

Código de Aglutinação

A

070

SIM

SIM

Indicador de Utilização do Código de Aglutinação

A

001

SIM

SIM

Conta Débito/Crédito do Lançamento

A

070

SIM

SIM

Data da Operação

N

008

SIM

SIM

Débito/Crédito do Lançamento Contábil

A

001

SIM

SIM

Arquivamento

A

050

SIM

SIM

Código do Histórico do Fato Contábil

A

006

SIM

SIM

 

OS3835\-C1

RN02

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS3835\-C1

RN03

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

OS3835\-C1

RN04

__Campo Código de Aglutinação__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Código de Aglutinação não informado”\.

OS3835\-C1

RN05

__Campo Indicador de Utilização do Código de Aglutinação__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Indicador de Utilização do Código de Aglutinação não informado”\.

O campo deve aceitar apenas os conteúdos “L” ou “M”\. Caso seja informado um conteúdo diferente, retornar a mensagem: "Indicador de Aglutinação inválido\. Informe <L> ou <M>"\.

OS3835\-C1

RN06

__Identificação dos Registros de Códigos de Aglutinação X Contas Contábeis__

Verificar através dos campos Código da Empresa, Código do Estabelecimento\*, Código de Aglutinação, Indicador de Utilização do Código de Aglutinação e Conta Débito/Crédito do Lançamento se existe registro correspondente na SAFX2103 – Códigos de Aglutinação X Contas Contábeis\. Caso não exista, retornar mensagem de erro: "Não existe registro correspondente de Códigos de Aglutinação X Contas Contábeis na SAFX2103"\.

\* Realizar a seguinte verificação em relação ao código do estabelecimento: se o estabelecimento parametrizado não for um centralizador, na consulta ao para Identificação dos Registros de Códigos de Aglutinação X Contas Contábeis o sistema deve verificar se o código do estabelecimento pertence a um grupo de centralização, conforme parametrização de centralização \(módulo Parâmetros / menu Preliminares >> Centralização da Escrituração de Obrigações Federais\) e realizar a consulta por código do estabelecimento centralizador\. Se o estabelecimento for centralizador, considerar o próprio código do estabelecimento\.

OS3835\-C1

CH9543/2014

RN07

__Identificação dos Registros de Códigos de Aglutinação Balanço/DRE__

Verificar através dos campos Código da Empresa, Código do Estabelecimento\*, Código de Aglutinação e Indicador de Utilização do Código de Aglutinação se existe registro correspondente na SAFX2102 – Códigos de Aglutinação Balanço/DRE\. Caso não exista, retornar mensagem de erro: "Não existe Cadastro de Código de Aglutinação correspondente na SAFX2102\. É pré\-requisito SAFX2102 e SAFX2103 correspondente"\.

\* Realizar a seguinte verificação em relação ao código do estabelecimento: se o estabelecimento parametrizado não for um centralizador, na consulta ao para Identificação dos Registros de Códigos de Aglutinação Balanço/DRE o sistema deve verificar se o código do estabelecimento pertence a um grupo de centralização, conforme parametrização de centralização \(módulo Parâmetros / menu Preliminares >> Centralização da Escrituração de Obrigações Federais\) e realizar a consulta por código do estabelecimento centralizador\. Se o estabelecimento for centralizador, considerar o próprio código do estabelecimento\.

OS3835\-C1

CH9543/2014

RN08

__Identificação do Lançamento Contábil__

Verificar através dos campos Código da Empresa, Código do Estabelecimento\*, Conta Débito/Crédito do Lançamento, Data da Operação, Débito/Crédito do Lançamento Contábil e Arquivamento se existe registro correspondente na SAFX01 – Arquivo Contábil\. Caso não exista, retornar mensagem de erro: “Lançamento Contábil não encontrado”\.

OS3835\-C1

RN09

__Campo Código do Histórico do Fato Contábil__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Campo Código do Histórico do Fato Contábil é obrigatório”\.

Verificar a existência do código informado na tabela SAFX2056\. Caso não exista, retornar mensagem de erro: “Campo Código do Histórico do Fato Contábil não cadastrado”\.

OS3835\-C1

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

