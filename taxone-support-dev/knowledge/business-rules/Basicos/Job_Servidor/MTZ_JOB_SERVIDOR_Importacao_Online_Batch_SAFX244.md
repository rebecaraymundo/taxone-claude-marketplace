# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX244

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX244.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 69 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX244

Tabela Empresas Contrapartes das Parcelas do Valor Eliminado Total

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

Definição das regras de carga, exportação, importação Online e Batch da SAF244\.

MFS26488

Andréa Rocha

Retirar a regra de validação da empresa da contrapartida em relação a empresa detentora\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX244 – Empresas Contrapartes das Parcelas do Valor Eliminado Total, que deve ser criada com a seguinte estrutura:

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

Data do Saldo consolidado

N

008

SIM

SIM

Código da conta consolidada

A

070

SIM

SIM

Código da empresa detentora do valor aglutinado que foi eliminado

A

004

SIM

SIM

Código da empresa da contrapartida

A

004

SIM

SIM

Código da conta consolidada da contrapartida

A

070

SIM

SIM

Parcela da contrapartida do valor eliminado total

N

017

SIM

NAO

Indicador da situação do valor eliminado

A

001

SIM

NAO

__Verificação de existência do registro pai__

Por ser esta tabela filha da SAFX243, no momento da importação deve ser verificada a existência de registro correspondente na tabela pai, considerando como chave de relacionamento os campos Código da Empresa, Código do Estabelecimento, Data do Saldo consolidado, Código da conta consolidada, Código da empresa detentora do valor aglutinado que foi eliminado\. Caso não encontre, retornar a mensagem: “SAFX243 correspondente a SAFX244 não localizada”\.

 

MFS\-9667

RN02

__Código da Empresa__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “Código de Empresa não está preenchido”\.

*\(registros das tabelas SAFX sem a informação da Empresa serão desconsiderados\)\. *

MFS\-9667

RN03

__Código do Estabelecimento__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “Código de Estabelecimento deve ser preenchido”\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento serão desconsiderados\)*

MFS\-9667

RN04

__Data do Saldo consolidado __

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Data do Saldo consolidado é obrigatório \- deve ser preenchido”\. Quando informado se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Campo de Data do Saldo consolidado com formato invalido”\. 

MFS\-9667

RN05

__Código da conta consolidada __

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Código da conta consolidada é obrigatório \- deve ser preenchido”\. 

Crítica da existência do código da conta na SAFX2002:

Será verificada a existência do código da conta informado \(Código da Conta\) na Tabela do Plano de Contas – SAFX2002 e se é analítica \(campo 04 \- Indicador de Conta = ‘A’\), e caso não exista ou não seja analítica, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Código da conta consolidada nao esta cadastrado ou não é uma conta analítica”\.

MFS\-9667

RN06

__Código da empresa detentora do valor aglutinado que foi eliminado__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Código da empresa detentora do valor aglutinado que foi eliminado é obrigatório \- deve ser preenchido”\. 

Crítica da existência do Código da empresa detentora do valor aglutinado que foi eliminado na SAFX240:

Será verificada a existência do Código da empresa detentora do valor aglutinado que foi eliminado informado \(Código da Empresa Participante\) na Tabela SAFX240, e caso não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Código da empresa detentora do valor aglutinado que foi eliminado nao esta cadastrado”\.

MFS\-9667

RN06

__Código da empresa da contrapartida __

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Código da empresa da contrapartida é obrigatório \- deve ser preenchido”\. 

Crítica da existência do Código da empresa da contrapartida na SAFX240:

Será verificada a existência do Código da empresa da contrapartida informado \(Código da Empresa Participante\) na Tabela SAFX240, e caso não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Código da empresa da contrapartida nao esta cadastrado”\.

\[MFS26488\] – Retirar a crítica abaixo, já que o validador do ECD só dá um aviso para esta situação:

Verificar também que o Código da empresa da contrapartida informado neste campo não poderá ser igual ao informado no campo Código da empresa detentora do valor aglutinado que foi eliminado\. Caso o código seja igual, retornar mensagem de erro: “O Código da empresa da contrapartida não pode ser igual ao Código da empresa detentora do valor aglutinado que foi eliminado informado”\. 

MFS\-9667/ MFS26488

RN06

__Código da conta consolidada da contrapartida__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Código da conta consolidada da contrapartida é obrigatório \- deve ser preenchido”\. 

Crítica da existência do código da conta na SAFX2002:

Será verificada a existência do código da conta informado \(Código da Conta\) na Tabela do Plano de Contas – SAFX2002 e se é analítica \(campo 04 \- Indicador de Conta = ‘A’\), e caso não exista ou não seja analítica, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Código da conta consolidada da contrapartida nao esta cadastrado ou não é uma conta analítica”\.

MFS\-9667

RN07

__Parcela da contrapartida do valor eliminado total __

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Parcela da contrapartida do valor eliminado total é obrigatório \- deve ser preenchido”\. 

MFS\-9667

RN08

__Indicador da situação do valor eliminado__

Opções válidas:

D – Devedor 

C – Credor 

Campo de preenchimento obrigatório, caso não preenchido exibir a seguinte mensagem: “O Campo Indicador da situação do valor eliminado é obrigatório \- deve ser preenchido”\. Quando informado uma opção inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Campo Indicador da situação do valor eliminado com opção invalida”\.

MFS\-9667

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

