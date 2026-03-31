# MTZ-Importacao_SAFX03

- **Fonte:** MTZ-Importacao_SAFX03.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 68 KB

---

THOMSON REUTERS

Regras de Importação SAFX03

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4579

Elenilson Coutinho

Alteração no tamanho do campo NUM\_LANCAMENTO

MFS\-12777

Elenilson Coutinho

Inclusão de campos para atendimento ao SPED REINF

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de Importação do módulo JOB Servidor deve ser ajustada para que contemple a alteração no campo NUM\_LANCAMENTO da tabela SAFX03 – Arquivo de Fornecedores \(Contas a Pagar\), que deve ser criada com a seguinte estrutura:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

NUM\_LANCAMENTO

A

040

NAO

NÃO

INSS Retido 

A

014

SIM

NÃO

Retenção Principal Não Efetuada

A

014

NÃO

NÃO

Tipo de Processo 

A

001

NÃO

SIM

Número do Processo

A

021

NÃO

SIM

Código de Suspensão

A

014

NÃO

SIM

 

OS4579

MFS\-12777

RN02

__Campo INSS Retido__

Crítica: Campo obrigatório, caso não preenchido exibir a seguinte mensagem: Campo Valor INSS Retido deve ser preenchido\.

MFS\-12777

RN03

__Campo Tipo do Processo __

Crítica: Valor esperado 1 e 2 caso contrário exibir a seguinte mensagem: “Tipo de Processo deve ser <1> ou <2>”\.

Se tipo de processo não preenchido e número processo estiver preenchido exibir a seguinte mensagem: “Tipo de Processo” deve ser preenchido referente ao “Número do Processo” identificado\. 

MFS\-12777

RN04

__Campo Número do Processo __

Se Número de Processo não preenchido e Tipo de Processo estiver preenchido exibir a seguinte mensagem: “Número de Processo” deve ser preenchido referente ao “Tipo de Processo” identificado\.

Caso não identificado Número do Processo no cadastro de Processos \(SAFX2058\), exibir a seguinte mensagem: “Número Processo não cadastrado na tabela de Processos \(SAFX2058\)”\.

MFS\-12777

RN05

__Campo Código de Suspensão__

Caso não encontrado o código de suspensão no cadastro de suspensão \(SAFX2059\) referente aos processos identificados pelos campos \(“Tipo do Processo” e “Número do Processo”\) exibir a seguinte mensagem: “Código de Suspensão” deve ser preenchido, referente ao “Tipo do Processo” e “Número do Processo” identificado\.

Caso não identificado Código de Suspensão no cadastro de Suspensão \(SAFX2059\), exibir a seguinte mensagem: “Código de Suspensão não cadastrado na tabela de Processos \(SAFX2058\)”\.

MFS\-12777

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

