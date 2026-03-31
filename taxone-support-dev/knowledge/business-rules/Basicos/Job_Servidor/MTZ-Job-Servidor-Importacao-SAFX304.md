# MTZ-Job-Servidor-Importacao-SAFX304

- **Fonte:** MTZ-Job-Servidor-Importacao-SAFX304.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 68 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX304

Tabela do Saldo Consolidado do Ressarcimento/Complemento de ICMS

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS31410

Andréa Rocha

Criação da tabela SAFX304 para geração do registro 1255, da nova versão do SPED Fiscal \(vigência Jan/2020\)\. 

19/12/2019

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX304__ 🡪 vide manual de layout

__Campos que compõe a chave da tabela:__

                      \[Código da empresa \+ Código do estabelecimento \+ Data da apuração \+ Código do Motivo\]

A manutenção da tabela é feita no módulo SPED Fiscal\.

MFS31410

__RN01__

__Campo Código da Empresa__

Campo de preenchimento __*obrigatório\.*__

*\(registros das tabelas SAFX sem a informação da Empresa são desconsiderados\)*

MFS31410

__RN02__

__Campo Código do Estabelecimento__

Campo de preenchimento __*obrigatório*__\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento são desconsiderados\)*

MFS31410

__RN03__

__Campo Data Apuração__

Campo de preenchimento __*obrigatório*__\.

Deve ser uma data válida\.

Quando não preenchida, ou data inválida, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*Data de Apuração não preenchida ou inválida”*\)\.

MFS31410

__RN04__

__Campo Código do Motivo__

Campo de preenchimento __*obrigatório*__\.

Será validada a existência do código do motivo na tabela dos códigos de motivo de restituição / complementação de ICMS \(DWT\_COD\_MOTIVO\_SPED\)\.  

Quando não preenchido, ou o código do motivo inválido, o registro não será importado, e no log de erros será gravada uma mensagem de erro *\(“Código do motivo* *não preenchido ou inválido”*\)\.

MFS31410

__RN05__

__Campo Valor do ICMS__

Campo de preenchimento __*não*__ obrigatório\.

MFS31410

__RN06__

__Campo Valor do ICMS ST Restituição__

Campo de preenchimento __*não*__ obrigatório\.

MFS31410

__RN07__

<a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>

<a id="OLE_LINK32"></a><a id="OLE_LINK33"></a><a id="OLE_LINK34"></a>__Campo Valor do FCP ST Restituição__

Campo de preenchimento __*não*__ obrigatório\.

MFS31410

__RN08__

__Campo Valor do ICMS ST Complemento__

Campo de preenchimento __*não*__ obrigatório\.

MFS31410

__RN09__

__Campo Valor do FCP ST Complemento__

Campo de preenchimento __*não*__ obrigatório\.

MFS31410

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

