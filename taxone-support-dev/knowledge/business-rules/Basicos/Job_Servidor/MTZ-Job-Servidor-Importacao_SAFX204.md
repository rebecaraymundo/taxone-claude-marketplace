# MTZ-Job-Servidor-Importacao_SAFX204

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX204.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 77 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX204

 Tabela das Formas de Pagamento do CFe 

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS10565

Tabela das Formas de Pagamento do CFe\.

Criação da SAFX204 para carregar as informações referentes às Formas de Pagamento do CFe para atendimento à Portaria CAT87/06\.

12/05/2017

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX204__ 🡪 vide manual de layout

A SAFX204 é uma tabela “filha” da SAFX201, e seu objetivo é informar para um determinado Cupom Fiscal Eletrônico \(identificado pelos campos 01 a 05\), as Formas de Pagamento do CFe \(campos 06 a 11\)\. Para cada cupom da SAFX201, poderão ser informadas uma ou várias formas de pagamento\.

Para detalhes sobre o objetivo e utilização desta tabela, consultar o manual de layout \(aba Indice e Tabelas SAFX\)\.

__Campos que compõe a chave da tabela:__

                           __                      Campos chave da SAFX201 \(campo 01 a 05\)__

__                                                                               \+__

__                                                        __

__                            Campos de identificação da forma de pagamento \(campo 06 e 07\)__

A manutenção da tabela é feita na tela de manutenção dos cupons fiscais eletrônicos, na aba “Formas de Pagamento”\.

__Crítica da existência do item na SAFX201:__

Após a validação dos campos que identificam o Cupom Fiscal \(campo 01 a 05\), conforme as regras descritas abaixo, será verificado se existe o cupom fiscal na base de dados \(SAFX201\)\. 

Caso o cupom não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                          “O Cupom Fiscal Eletrônico informado não foi identificado na Tabela de Cupons Fiscais Eletrônicos”*

Para facilitar a identificação do problema, o log deve informar os dados básicos do cupom informado nos campos 01 ao 05\.  

 

MFS10565

__RN01__

__Campo Código da Empresa__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação da Empresa serão desconsiderados\)*

MFS10565

__RN02__

__Campo Código do Estabelecimento__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento serão desconsiderados\)*

MFS10565

__RN03__

__Campo Número do Equipamento__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*‘Número de série do equipamento SAT deve ser preenchido\.’*

MFS10565

__RN04__

__Campo Número do Cupom Fiscal Eletrônico __

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*‘Numero do cupom fiscal eletrônico deve ser preenchido\.’*

MFS10565

__RN05__

__Campo Data de Emissão__

Campo de preenchimento __*obrigatório*__\.

Deve ser uma data válida\.

Quando não preenchido, ou quando for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “Data de Emissão não preenchida ou inválida”*

MFS10565

__RN06__

__Campo Código da Operação__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão\)\.

Será verificada a existência do código de operação informado na Tabela de Códigos de Operação \(SAFX2001\)\. Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que o código não existe na tabela \(mensagem padrão\)\.

MFS10565

__RN07__

<a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>

<a id="OLE_LINK32"></a><a id="OLE_LINK33"></a><a id="OLE_LINK34"></a>__Campo Comprovante de Pagamento__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*‘Comprovante do Pagamento deve ser preenchido\.’*

MFS10565

__RN08__

__Campo Natureza da Operação__

Campo de preenchimento __*obrigatório*__\.

Valores válidos: “1” ou “2” \(“1” para crédito; “2” para débito\)      

Quando não for preenchido ou o contéudo não for válido, o registro não será importado, e no log de erros será gravada uma mensagem informando que:

*“Campo Natureza de Operação deve ser preenchido com ”1” para crédito ou “2” para débito\.”*

MFS10565

__RN09__

__Campo Valor da Operação__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*‘Valor da Operação deve ser preenchido\.’*

MFS10565

__RN10__

__Campo CEP__

Campo de preenchimento __*não obrigatório*__\.

MFS10565

__RN11__

__Campo Ponto de Venda__

Campo de preenchimento __*não obrigatório*__\.

MFS10565

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

