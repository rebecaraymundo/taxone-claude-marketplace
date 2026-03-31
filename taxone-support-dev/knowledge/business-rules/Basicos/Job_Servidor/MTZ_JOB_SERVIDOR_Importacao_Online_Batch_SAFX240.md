# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX240

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX240.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 76 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX240

Tabela Período da Escrituração Contábil Consolidada / Relação das Empresas Consolidadas

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Carga 🡪 Execução

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

\- Exportação Dados 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-9667

Lara Aline

Definição das regras de carga, exportação, importação Online e Batch da SAF240\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX240 – Relação das Empresas Consolidadas, que deve ser criada com a seguinte estrutura:

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

Data Inicial do período consolidado

N

008

SIM

SIM

Data Final do período consolidado

N

008

SIM

SIM

Código da Empresa Participante

A

004

SIM

SIM

Nome da Empresa Participante

A

100

SIM

NAO

CNPJ da Empresa Participante

A

014

NÃO

NAO

Evento Ocorrido no Período

A

001

SIM

NAO

Percentual de Participação Total

A

008

SIM

NAO

Percentual de Consolidação no Final Período

A

008

SIM

NAO

Data Início da Consolidação

N

008

SIM

NAO

Data Final da Consolidação

N

008

SIM

NAO

Código do País

A

003

SIM

NAO

 

MFS\-9667

RN02

__Código da Empresa__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “Código de Empresa não está preenchido”\.

*\(registros das tabelas SAFX sem a informação da Empresa serão desconsiderados\)*

MFS\-9667

RN03

__Código do Estabelecimento__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “Código de Estabelecimento deve ser preenchido”\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento serão desconsiderados\)*

MFS\-9667

RN04

__Data Inicial do período consolidado__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Data Início do período consolidado é obrigatório \- deve ser preenchido”\. Quando informado se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Campo de Data Início do período consolidado com formato invalido”\.

MFS\-9667

RN05

__Data Final do período consolidado__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Data Final do período consolidado é obrigatório \- deve ser preenchido”\. Quando informado se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Campo de Data Final do período consolidado com formato invalido”\. 

A data informada neste campo deve ser maior ou igual à data informada no campo Data Início da Consolidação\. Caso seja menor, retornar mensagem de erro: “A Data Final do período consolidado não pode ser menor que a Data Inicial do período consolidado”\.

MFS\-9667

RN06

__Código da Empresa Participante __

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Código da Empresa Participante é obrigatório \- deve ser preenchido”\. 

MFS\-9667

RN07

__Nome da Empresa Participante __

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Nome da Empresa Participante é obrigatório \- deve ser preenchido”\.

MFS\-9667

RN08

__CNPJ da Empresa Participante __

Campo de preenchimento não obrigatório, quando informado se for um CNPJ inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “Numero de CNPJ informado nao e valido, conforme regras da Secretaria de Fazenda\.”\.

MFS\-9667

RN09

__Evento Ocorrido no Período __

Opções válidas:

S – Sim

N – Não

Campo de preenchimento obrigatório, caso não preenchido exibir a seguinte mensagem: “O Campo Evento Ocorrido no Período é obrigatório \- deve ser preenchido”\. Quando informado uma opção inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Campo Evento Ocorrido no Período com opção invalida”\.

MFS\-9667

RN10

__Percentual de Participação Total __

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Percentual de Participação Total é obrigatório \- deve ser preenchido”\.

MFS\-9667

RN11

__Percentual de Consolidação no Final Período__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Percentual de Consolidação no Final Período é obrigatório \- deve ser preenchido”\.

MFS\-9667

RN12

__Data Início da Consolidação __

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Data Início da Consolidação é obrigatório \- deve ser preenchido”\. Quando informado se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Campo de Data Início da Consolidação com formato invalido”\.

A data informada neste campo deve ser maior ou igual à data informada no campo Data Inicial do período consolidado\. Caso seja menor, retornar mensagem de erro: “A Data Início da Consolidação não pode ser menor que a Data Inicial do período consolidado”\.

MFS\-9667

RN13

__Data Final da Consolidação __

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Data Final da Consolidação é obrigatório \- deve ser preenchido”\. Quando informado se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Campo de Data Final da Consolidação com formato invalido”\.

A data informada neste campo deve ser maior ou igual à data informada no campo Data Início da Consolidação\. Caso seja menor, retornar mensagem de erro: “A Data Final da Consolidação não pode ser menor que a Data Inicial da Consolidação”\.

Verificar também que a data informada neste campo deve ser menor ou igual à data informada no campo Data Final do período consolidado\. Caso seja maior, retornar mensagem de erro: “A Data Final da Consolidação não pode ser maior que a Data Final do período consolidado”\.

MFS\-9667

RN14

__Código do País __

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “Codigo do Pais deve ser preenchido”\.

Crítica da existência do País na tabela ‘pais’:

Será verificada a existência do País informado \(Código do Pais\) na Tabela PAIS, e caso não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Campo Codigo de Pais nao esta cadastrado”\.

__Tratamento:__

Caso o campo “CNPJ da Empresa Participante” estiver preenchido, será verificado se o campo “Código do País” está preenchido com o código correspondente a “105 \- Brasil”, caso negativo exibir a seguinte mensagem: “Caso o Campo ‘CNPJ da Empresa Participante’ estiver preenchido, o campo ‘Código do País’ deve correspondente a “Brasil”\.”\.

MFS\-9667

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

