# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2103

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2103.docx
- **Modificado:** 2023-10-06
- **Tamanho:** 65 KB

---

THOMSON REUTERS

3

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS28272

Andréa Rocha

Alteração das regras de importação dos campos Campo Conta Débito/Crédito do Lançamento e Centro de Custo\. 

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS28272

RN02

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS28272

RN03

__Campo Código de Aglutinação__

Campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro:

“Código de Aglutinação deve ser preenchido”\.

MFS28272

RN04

__Campo Conta Débito/Crédito do Lançamento__

Campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro:

“Conta Contábil deve ser preenchida”\.

Caso seja importado um registro na SAFX2103 com uma Conta Débito/Crédito do Lançamento que já esteja associada a um código de aglutinação, o sistema não deverá permitir a importação e deverá exibir mensagem de erro:

“Conta Contábil cadastrada para outro Código de Aglutinação”

Obs\.: O sistema não deve permitir que uma conta seja associada a mais de um código de aglutinação, independentemente do nível da conta\.  Atualmente se o nível da conta fosse diferente, a associação era permitida\.

MFS28272

RN05

__Campo Centro de Custo__

Campo de preenchimento não obrigatório\. 

Caso seja importado um registro na SAFX2103 com uma Conta Débito/Crédito do Lançamento \+ centro de custo, que já esteja associada a um código de aglutinação, o sistema não deverá permitir a importação e deverá exibir mensagem de erro:

“Conta Contábil com Centro de Custo já estão cadastrados para outro Código de Aglutinação”

Obs\.: O sistema não deve permitir que uma conta \+ centro de custo seja associada a mais de um código de aglutinação, independentemente do nível da conta\.  Atualmente se o nível da conta fosse diferente, a associação era permitida\.

MFS28272

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

