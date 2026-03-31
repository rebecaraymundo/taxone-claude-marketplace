# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX257

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX257.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 70 KB

---

THOMSON REUTERS

Regras de Importação Online e Batch SAFX257 

JOB Servidor

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-15698

João Henrique de Araujo

Definição das regras de importação, Online e Batch, da SAFX257\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN01__

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX257 – Notas Explicativas dos Demonstrativos Contábeis, que deve ser criada com a seguinte estrutura:

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

Indicador de Balanço DRE

A

001

SIM

SIM

Código de Aglutinação

A

070

SIM

SIM

Data da Demonstração

           D

008

SIM

SIM

Nota Explicativa 

A

255

SIM

NÃO

 

__MFS15698__

__RN02__

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

__MFS15698__

__RN03__

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

__MFS15698__

__RN04__

__Campo Índicador de Balanço DRE__

Campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido, ou seja, preenchido com valor diferente de <B>, <D>, <L> ou <M>, deve ser exibida mensagem de erro:  
 “Indicador de Aglutinação deve ser preenchido com <B>, <D>, <L> ou <M>”\.

__MFS15698__

__RN05__

__Campo Código de Aglutinação__

Campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro:

“Código de Aglutinação deve ser preenchido”\.

__Observações: __

Os códigos de aglutinação necessariamente precisam estar carregados e/ou cadastrados na SAFX2102 \- Códigos de Aglutinação Balanço/DRE/DLPA/DMPL com suas respectivas informações de empresa, estabelecimento e qual indicador de balanço pertence\.

Caso o código de Aglutinação não seja localizado na importação, exibir a mensagem de alerta para o usuário:

*“91943;\-\-Codigo de Aglutinacao nao cadastrado”*

__MFS15698__

__RN06__

__Data da Demonstração__

Campo é obrigatório de preenchimento\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro:

“Data da Demonstração deve ser preenchido”\.

__MFS15698__

__RN07__

__Nota Explicativa__

Preencher o campo com as informações da nota explicativa para o respectivo código de aglutinação\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro:

“Nota Explicativa deve ser preenchido”\.

__MFS15698__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

